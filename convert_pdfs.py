#!/usr/bin/env python3
"""
PDF to Markdown Converter
Converts all PDF files in a folder to well-structured Markdown (.md) files.

Features:
- Table extraction and Markdown formatting
- Heading detection based on font size
- Slide deck detection (landscape, large fonts)
- Image extraction to assets folder
- OCR fallback for scanned PDFs
- Batch processing with progress tracking
- Comprehensive error handling
- YAML front matter with metadata
"""

import argparse
import logging
import os
import sys
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import re

# Core PDF processing
import pdfplumber
import fitz  # pymupdf

# Table extraction - try pdfminer but it's optional
try:
    from pdfminer.high_level import extract_text
except ImportError:
    extract_text = None

try:
    import camelot
except ImportError:
    camelot = None

# Image & OCR
try:
    import pytesseract
    from pdf2image import convert_from_path
    PYTESSERACT_AVAILABLE = True
except ImportError:
    PYTESSERACT_AVAILABLE = False

# Progress tracking
from tqdm import tqdm

# ============================================================================
# CONFIGURATION MANAGEMENT
# ============================================================================

class ConfigManager:
    """Manage configuration from YAML file and CLI arguments."""
    
    DEFAULT_CONFIG = {
        "output_folder": None,  # None = save next to original PDF
        "extract_images": True,
        "ocr_fallback": True,
        "ocr_language": "eng",
        "heading_size_threshold": 14,  # font size in pt
        "slide_detection": True,
        "recursive": True,
        "log_file": "conversion_log.txt"
    }
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize config from file or defaults."""
        self.config = self.DEFAULT_CONFIG.copy()
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    user_config = yaml.safe_load(f) or {}
                    self.config.update(user_config)
                logging.info(f"Loaded config from {config_path}")
            except Exception as e:
                logging.warning(f"Failed to load config file: {e}. Using defaults.")
    
    def get(self, key: str, default=None):
        """Get config value."""
        return self.config.get(key, default)
    
    def set(self, key: str, value):
        """Set config value."""
        self.config[key] = value


# ============================================================================
# LOGGING SETUP
# ============================================================================

class ConversionLogger:
    """Track conversion results per file."""
    
    def __init__(self, log_path: Path):
        self.log_path = log_path
        self.entries = []
    
    def log_conversion(self, filename: str, status: str, pages: int, 
                       tables_found: int, errors: List[str]):
        """Log a conversion result."""
        entry = {
            "filename": filename,
            "status": status,
            "pages": pages,
            "tables_found": tables_found,
            "errors": errors,
            "timestamp": datetime.now().isoformat()
        }
        self.entries.append(entry)
    
    def save(self):
        """Write log to file."""
        try:
            with open(self.log_path, 'w') as f:
                f.write("PDF to Markdown Conversion Log\n")
                f.write("=" * 60 + "\n\n")
                for entry in self.entries:
                    f.write(f"File: {entry['filename']}\n")
                    f.write(f"Status: {entry['status']}\n")
                    f.write(f"Pages: {entry['pages']}\n")
                    f.write(f"Tables Found: {entry['tables_found']}\n")
                    if entry['errors']:
                        f.write(f"Errors: {'; '.join(entry['errors'])}\n")
                    f.write(f"Timestamp: {entry['timestamp']}\n")
                    f.write("-" * 60 + "\n\n")
        except Exception as e:
            logging.error(f"Failed to write log file: {e}")


# ============================================================================
# PDF ANALYSIS & DETECTION
# ============================================================================

def detect_pdf_type(pdf_path: str) -> str:
    """
    Detect if PDF is a slide deck or regular document.
    Slide decks typically have: landscape orientation, large fonts, short text blocks.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            if len(pdf.pages) < 2:
                return "document"  # Single page likely not a slide deck
            
            # Sample first 3 pages
            sample_pages = pdf.pages[:min(3, len(pdf.pages))]
            landscape_count = 0
            avg_text_length = 0
            
            for page in sample_pages:
                # Check orientation
                if page.width > page.height:
                    landscape_count += 1
                
                # Check text density
                text = page.extract_text() or ""
                avg_text_length += len(text) / len(sample_pages)
            
            # Heuristics: landscape orientation + short text = likely slide deck
            is_landscape = landscape_count >= 2
            is_short_content = avg_text_length < 500
            
            if is_landscape and is_short_content:
                return "slide"
            return "document"
    except Exception as e:
        logging.warning(f"Error detecting PDF type for {pdf_path}: {e}")
        return "document"


def is_scanned_pdf(pdf_path: str) -> bool:
    """
    Detect if PDF is scanned (image-based) with no selectable text.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            if len(pdf.pages) == 0:
                return False
            
            # Check first page for selectable text
            first_page = pdf.pages[0]
            text = first_page.extract_text() or ""
            
            # If less than 50 characters on first page, likely scanned
            return len(text.strip()) < 50
    except Exception:
        return False


# ============================================================================
# TABLE EXTRACTION
# ============================================================================

def extract_tables_pdfplumber(pdf_path: str, page_num: int) -> List[List[List[str]]]:
    """
    Extract tables from a specific page using pdfplumber.
    Returns list of tables, each table is list of rows.
    """
    tables = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            if page_num >= len(pdf.pages):
                return tables
            
            page = pdf.pages[page_num]
            
            # pdfplumber's table detection
            extracted_tables = page.extract_tables()
            if extracted_tables:
                for table in extracted_tables:
                    # Convert to list of lists for consistency
                    table_data = [list(row) for row in table]
                    tables.append(table_data)
    except Exception as e:
        logging.debug(f"pdfplumber table extraction failed for page {page_num}: {e}")
    
    return tables


def extract_tables_camelot(pdf_path: str, page_num: int) -> List[List[List[str]]]:
    """
    Extract tables using Camelot (better for borderless tables).
    page_num is 0-indexed, but Camelot uses 1-indexed page numbers.
    """
    if camelot is None:
        return []
    
    tables = []
    try:
        # Camelot pages are 1-indexed
        camelot_tables = camelot.read_pdf(
            pdf_path,
            pages=str(page_num + 1),
            flavor='stream'  # 'stream' works better for borderless tables
        )
        
        for table in camelot_tables:
            # Convert DataFrame to list of lists
            table_data = table.data
            tables.append(table_data)
    except Exception as e:
        logging.debug(f"Camelot table extraction failed for page {page_num}: {e}")
    
    return tables


def tables_to_markdown(tables: List[List[List[str]]]) -> str:
    """
    Convert table data to Markdown table syntax.
    Handles alignment and column width.
    """
    if not tables:
        return ""
    
    markdown = ""
    for table in tables:
        if not table or not table[0]:
            continue
        
        # Extract header and body
        header = table[0] if table else []
        body = table[1:] if len(table) > 1 else []
        
        # Ensure all rows have same number of columns
        num_cols = len(header)
        
        # Build separator row
        separator = "| " + " | ".join(["---"] * num_cols) + " |"
        
        # Build header row
        header_row = "| " + " | ".join(str(cell).strip() for cell in header) + " |"
        
        # Build body rows
        body_rows = []
        for row in body:
            # Pad row if needed
            padded_row = row + [""] * (num_cols - len(row))
            row_str = "| " + " | ".join(str(cell).strip() for cell in padded_row[:num_cols]) + " |"
            body_rows.append(row_str)
        
        # Combine table
        markdown += header_row + "\n" + separator + "\n"
        if body_rows:
            markdown += "\n".join(body_rows) + "\n"
        markdown += "\n"
    
    return markdown


# ============================================================================
# TEXT EXTRACTION & PROCESSING
# ============================================================================

def extract_text_with_fonts(pdf_path: str, page_num: int) -> Dict:
    """
    Extract text with font information for heading detection.
    Returns dict with: text, font_sizes, raw_text
    """
    result = {
        "text": "",
        "font_sizes": {},  # {text_fragment: font_size}
        "raw_text": "",
        "is_empty": False
    }
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            if page_num >= len(pdf.pages):
                result["is_empty"] = True
                return result
            
            page = pdf.pages[page_num]
            
            # Extract text
            text = page.extract_text() or ""
            result["raw_text"] = text
            
            # Extract words with font info
            if hasattr(page, 'chars'):
                font_sizes = {}
                for char in page.chars:
                    if char.get('text', '').strip():
                        size = char.get('size', 0)
                        text_frag = char['text']
                        font_sizes[text_frag] = size
                result["font_sizes"] = font_sizes
            
            # Simple text extraction
            result["text"] = text
            result["is_empty"] = len(text.strip()) < 20
            
    except Exception as e:
        logging.debug(f"Error extracting text with fonts from page {page_num}: {e}")
        result["is_empty"] = True
    
    return result


def detect_headings(text: str, font_sizes: Dict, threshold: float) -> str:
    """
    Convert text to Markdown with heading detection.
    Maps font sizes to heading levels (H2-H4).
    
    Args:
        text: Plain text extracted from PDF
        font_sizes: Dict mapping text fragments to font sizes
        threshold: Font size threshold for H2 heading
    """
    if not text:
        return ""
    
    lines = text.split('\n')
    markdown = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            markdown.append("")
            continue
        
        # Try to find font size for this line
        line_font_size = None
        for frag, size in font_sizes.items():
            if frag in line:
                line_font_size = size
                break
        
        # Apply heading markup based on font size
        if line_font_size and line_font_size >= threshold + 10:
            # H2 for very large text
            markdown.append(f"## {stripped}")
        elif line_font_size and line_font_size >= threshold:
            # H3 for large text
            markdown.append(f"### {stripped}")
        else:
            # Regular text
            markdown.append(stripped)
    
    return "\n".join(markdown)


def process_lists(text: str) -> str:
    """
    Ensure lists are properly formatted in Markdown.
    Preserves bullet points, numbered lists, and nesting.
    """
    lines = text.split('\n')
    result = []
    
    for line in lines:
        # Already formatted list items
        if line.strip().startswith(('- ', '* ', '+ ', '1. ', '2. ')):
            result.append(line)
        # Detect common list markers
        elif re.match(r'^\s*[•◦◾▪▫]\s+', line):
            # Convert bullet symbols to markdown
            converted = re.sub(r'^\s*[•◦◾▪▫]\s+', '- ', line)
            result.append(converted)
        else:
            result.append(line)
    
    return "\n".join(result)


# ============================================================================
# IMAGE EXTRACTION
# ============================================================================

def extract_images(pdf_path: str, output_folder: Path, extract: bool = True) -> List[str]:
    """
    Extract images from PDF and save to assets folder.
    Returns list of image references in Markdown format.
    
    Args:
        pdf_path: Path to PDF file
        output_folder: Where to save images
        extract: Whether to actually extract images
    
    Returns:
        List of Markdown image references: ["![Image 1](path/to/image_1.png)", ...]
    """
    references = []
    
    if not extract:
        return references
    
    try:
        doc = fitz.open(pdf_path)
        pdf_name = Path(pdf_path).stem
        assets_folder = output_folder / f"{pdf_name}_assets"
        
        image_count = 0
        for page_num, page in enumerate(doc):
            image_list = page.get_images()
            
            for img_index, img in enumerate(image_list):
                try:
                    xref = img[0]
                    pix = fitz.Pixmap(doc, xref)
                    
                    # Create assets folder if needed
                    if not assets_folder.exists():
                        assets_folder.mkdir(parents=True, exist_ok=True)
                    
                    # Save image
                    image_count += 1
                    image_filename = f"image_{page_num}_{img_index}.png"
                    image_path = assets_folder / image_filename
                    
                    if pix.n - pix.alpha < 4:  # GRAY or RGB
                        pix.save(str(image_path))
                    else:  # CMYK, convert to RGB
                        rgb_pix = fitz.Pixmap(fitz.csRGB, pix)
                        rgb_pix.save(str(image_path))
                    
                    # Add reference (relative path)
                    rel_path = f"{pdf_name}_assets/{image_filename}"
                    references.append(f"![Image {image_count}]({rel_path})")
                    
                except Exception as e:
                    logging.debug(f"Failed to extract image {img_index} from page {page_num}: {e}")
        
        if image_count > 0:
            logging.info(f"Extracted {image_count} images from {Path(pdf_path).name}")
    
    except Exception as e:
        logging.warning(f"Error extracting images from {pdf_path}: {e}")
    
    return references


# ============================================================================
# OCR FALLBACK
# ============================================================================

def ocr_pdf_page(pdf_path: str, page_num: int, language: str = "eng") -> str:
    """
    Use OCR (Tesseract) to extract text from a scanned PDF page.
    """
    if not PYTESSERACT_AVAILABLE:
        logging.warning("pytesseract not available. Install it for OCR support.")
        return ""
    
    try:
        images = convert_from_path(pdf_path, first_page=page_num+1, last_page=page_num+1)
        if not images:
            return ""
        
        # OCR the image
        text = pytesseract.image_to_string(images[0], lang=language)
        return text
    except Exception as e:
        logging.debug(f"OCR failed for page {page_num}: {e}")
        return ""


# ============================================================================
# MARKDOWN GENERATION
# ============================================================================

def build_markdown_document(pdf_path: str, config: ConfigManager, is_slide: bool) -> Tuple[str, int, int, List[str]]:
    """
    Build complete Markdown document from PDF.
    
    Returns:
        (markdown_content, num_pages, tables_found, errors)
    """
    errors = []
    tables_found = 0
    markdown_parts = []
    
    try:
        doc_info = {
            "title": Path(pdf_path).stem,
            "source": Path(pdf_path).name,
            "pages": 0,
            "converted_at": datetime.now().isoformat()
        }
        
        with pdfplumber.open(pdf_path) as pdf:
            if len(pdf.pages) == 0:
                errors.append("Empty PDF")
                return "", 0, 0, errors
            
            doc_info["pages"] = len(pdf.pages)
            num_pages = len(pdf.pages)
            
            # Try to get PDF title from metadata
            if pdf.metadata and pdf.metadata.get('Title'):
                doc_info["title"] = pdf.metadata['Title']
        
        # Add YAML front matter
        yaml_front = "---\n"
        yaml_front += f"title: {doc_info['title']}\n"
        yaml_front += f"source: {doc_info['source']}\n"
        yaml_front += f"pages: {doc_info['pages']}\n"
        yaml_front += f"converted_at: {doc_info['converted_at']}\n"
        yaml_front += "---\n\n"
        markdown_parts.append(yaml_front)
        
        # Check if scanned PDF
        scanned = is_scanned_pdf(pdf_path)
        if scanned and config.get("ocr_fallback"):
            logging.info(f"Scanned PDF detected: {Path(pdf_path).name}")
        
        # Extract images
        output_folder = config.get("output_folder")
        if output_folder is None:
            output_folder = Path(pdf_path).parent
        else:
            output_folder = Path(output_folder)
        
        image_refs = extract_images(pdf_path, output_folder, config.get("extract_images"))
        
        # Process each page
        for page_num in range(num_pages):
            # For slide decks, separate with horizontal rules
            if is_slide and page_num > 0:
                markdown_parts.append("\n---\n\n")
                markdown_parts.append(f"## Slide {page_num + 1}\n\n")
            
            # Extract text with font information
            text_data = extract_text_with_fonts(pdf_path, page_num)
            
            if text_data["is_empty"] and scanned and config.get("ocr_fallback"):
                # Fallback to OCR
                text = ocr_pdf_page(pdf_path, page_num, config.get("ocr_language"))
                if text:
                    markdown_parts.append(text)
                    markdown_parts.append("\n")
                else:
                    errors.append(f"Page {page_num + 1}: No text extracted (OCR failed)")
                continue
            
            # Extract tables
            page_tables = extract_tables_pdfplumber(pdf_path, page_num)
            
            # If pdfplumber missed tables, try Camelot
            if not page_tables and camelot:
                page_tables = extract_tables_camelot(pdf_path, page_num)
            
            # Convert tables to Markdown
            if page_tables:
                table_md = tables_to_markdown(page_tables)
                markdown_parts.append(table_md)
                tables_found += len(page_tables)
            
            # Process text with heading detection
            if text_data["text"]:
                heading_md = detect_headings(
                    text_data["text"],
                    text_data["font_sizes"],
                    config.get("heading_size_threshold")
                )
                
                # Apply list formatting
                heading_md = process_lists(heading_md)
                
                markdown_parts.append(heading_md)
                markdown_parts.append("\n\n")
        
        # Add image references if any
        if image_refs:
            markdown_parts.append("\n## Images/Figures\n\n")
            markdown_parts.append("\n".join(image_refs))
            markdown_parts.append("\n")
        
        markdown_content = "".join(markdown_parts)
        
        return markdown_content, num_pages, tables_found, errors
    
    except Exception as e:
        errors.append(f"Document processing error: {str(e)}")
        logging.error(f"Error building markdown for {pdf_path}: {e}")
        return "", 0, 0, errors


# ============================================================================
# FILE OPERATIONS
# ============================================================================

def scan_folder(folder: Path, recursive: bool = True) -> List[Path]:
    """
    Scan folder for all PDF files.
    
    Returns:
        List of PDF file paths
    """
    pdfs = []
    
    if recursive:
        # Recursive search
        pdfs = list(folder.rglob("*.pdf"))
        # Also check for .PDF (uppercase)
        pdfs.extend(folder.rglob("*.PDF"))
    else:
        # Only in top directory
        pdfs = list(folder.glob("*.pdf"))
        pdfs.extend(folder.glob("*.PDF"))
    
    # Remove duplicates
    pdfs = list(set(pdfs))
    pdfs.sort()
    
    return pdfs


def save_markdown_file(content: str, pdf_path: Path, output_folder: Optional[Path] = None) -> Path:
    """
    Save Markdown file.
    
    Args:
        content: Markdown content
        pdf_path: Original PDF path
        output_folder: Where to save (None = same folder as PDF)
    
    Returns:
        Path to saved file
    """
    if output_folder is None:
        output_folder = pdf_path.parent
    else:
        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)
    
    # Generate markdown filename
    md_filename = pdf_path.stem + ".md"
    md_path = output_folder / md_filename
    
    try:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return md_path
    except Exception as e:
        logging.error(f"Failed to save markdown file {md_path}: {e}")
        raise


# ============================================================================
# MAIN CONVERSION LOGIC
# ============================================================================

def convert_pdf(pdf_path: str, config: ConfigManager) -> Tuple[bool, str, int]:
    """
    Convert a single PDF to Markdown.
    
    Returns:
        (success: bool, status: str, tables_found: int)
    """
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        return False, "❌ File not found", 0
    
    if not pdf_path.suffix.lower() == '.pdf':
        return False, "❌ Not a PDF file", 0
    
    try:
        # Detect PDF type
        pdf_type = config.get("slide_detection") and detect_pdf_type(str(pdf_path)) or "document"
        is_slide = pdf_type == "slide"
        
        # Build markdown
        markdown, num_pages, tables_found, errors = build_markdown_document(
            str(pdf_path), config, is_slide
        )
        
        if num_pages == 0:
            return False, "❌ Empty PDF", 0
        
        # Save markdown
        output_folder = config.get("output_folder")
        if output_folder:
            output_folder = Path(output_folder)
        else:
            output_folder = pdf_path.parent
        
        md_path = save_markdown_file(markdown, pdf_path, output_folder)
        
        # Determine status
        if not errors:
            status = "✅ Success"
        else:
            status = "⚠️  Partial"
        
        logging.info(f"{status}: {pdf_path.name} → {md_path.name}")
        return True, status, tables_found
    
    except Exception as e:
        logging.error(f"Conversion failed for {pdf_path}: {e}")
        return False, f"❌ Error: {str(e)[:50]}", 0


def main():
    """Main entry point."""
    
    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Convert PDF files to Markdown (.md)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python convert_pdfs.py --input ./my_pdfs
  python convert_pdfs.py --input ./my_pdfs --output ./markdown_files
  python convert_pdfs.py --input ./my_pdfs --config config.yaml
        """
    )
    
    parser.add_argument(
        "--input", "-i",
        help="Input folder path containing PDFs",
        type=str
    )
    parser.add_argument(
        "--output", "-o",
        help="Output folder for Markdown files (default: same as input)",
        type=str
    )
    parser.add_argument(
        "--config", "-c",
        help="Path to config.yaml file",
        type=str
    )
    parser.add_argument(
        "--no-ocr",
        action="store_true",
        help="Disable OCR fallback for scanned PDFs"
    )
    parser.add_argument(
        "--extract-images",
        action="store_true",
        default=True,
        help="Extract images from PDFs"
    )
    
    args = parser.parse_args()
    
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Get input folder
    if args.input:
        input_folder = Path(args.input)
    else:
        # Interactive prompt
        print("\n" + "="*60)
        print("PDF to Markdown Converter")
        print("="*60)
        input_path = input("Enter path to folder containing PDFs: ").strip()
        if not input_path:
            print("Error: No path provided.")
            sys.exit(1)
        input_folder = Path(input_path)
    
    # Validate input folder
    if not input_folder.exists():
        logging.error(f"Folder not found: {input_folder}")
        sys.exit(1)
    
    if not input_folder.is_dir():
        logging.error(f"Not a directory: {input_folder}")
        sys.exit(1)
    
    # Load configuration
    config = ConfigManager(args.config)
    
    # Override with CLI arguments
    if args.output:
        config.set("output_folder", args.output)
    if args.no_ocr:
        config.set("ocr_fallback", False)
    if args.extract_images:
        config.set("extract_images", True)
    
    # Scan for PDFs
    pdf_files = scan_folder(input_folder, config.get("recursive"))
    
    if not pdf_files:
        logging.warning(f"No PDF files found in {input_folder}")
        sys.exit(0)
    
    logging.info(f"Found {len(pdf_files)} PDF file(s)")
    
    # Create output folder if specified
    output_folder = config.get("output_folder")
    if output_folder:
        Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Setup logging
    log_path = Path(output_folder or input_folder) / "conversion_log.txt"
    converter_log = ConversionLogger(log_path)
    
    # Process each PDF
    print("\n" + "="*60)
    print("Starting Conversion")
    print("="*60 + "\n")
    
    successful = 0
    failed = 0
    
    for i, pdf_path in enumerate(tqdm(pdf_files, desc="Converting PDFs"), 1):
        print(f"[{i}/{len(pdf_files)}] Converting: {pdf_path.name}... ", end="", flush=True)
        
        success, status, tables_found = convert_pdf(str(pdf_path), config)
        print(status)
        
        if success:
            successful += 1
            converter_log.log_conversion(pdf_path.name, status, 0, tables_found, [])
        else:
            failed += 1
            converter_log.log_conversion(pdf_path.name, status, 0, 0, [status])
    
    # Save conversion log
    converter_log.save()
    
    # Summary
    print("\n" + "="*60)
    print("Conversion Summary")
    print("="*60)
    print(f"Total:      {len(pdf_files)}")
    print(f"Successful: {successful}")
    print(f"Failed:     {failed}")
    print(f"Log file:   {log_path}")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
