# 6. TAM / SAM / SOM
## TA_Chatbot — AI Trợ Giảng

---

### Phương pháp ước lượng

**Nguyên tắc**: Tách rõ facts vs assumptions, dùng range khi uncertainty cao, không bịa số.

---

### TAM (Total Addressable Market)

**Câu hỏi**: Nếu mọi khách hàng tiềm năng đều mua, thị trường lớn bao nhiêu?

**Definition**: Tất cả sinh viên Computer Science/IT tại các trường đại học Việt Nam cần hỗ trợ lập trình 24/7.

**Assumptions & Logic**:

1. **Total CS/IT students in Vietnam (university level)**:
   - Fact: Có ~200-300 trường đại học tại Việt Nam
   - Assumption: Trung bình mỗi trường có 200-500 sinh viên CS/IT (tùy quy mô)
   - Estimate: 250 schools × 350 avg students = **~87,500 CS/IT students** nationwide
   - Confidence: Low (không có data chính thức, dùng estimate)

2. **Percentage that would benefit from 24/7 AI TA**:
   - Assumption: 70% của sinh viên CS/IT cần hỗ trợ ngoài giờ (dựa trên: first-year students là nhóm có nhu cầu cao nhất)
   - Estimate: 87,500 × 70% = **~61,250 students** (potential market)

3. **Willingness to pay (WTP)**:
   - Current state: Sinh viên không trả tiền trực tiếp cho TA support (đây là internal tool)
   - Assumption: Nếu là SaaS product, universities có thể trả $5-10/student/năm
   - But: Đây là internal tool cho VinUniversity — không phải commercial product
   - **Adjustment**: Vì đây là internal project, TAM nên tính theo **cost savings** thay vì revenue
   - Cost savings: Giảm 20 giờ/tuần TA × $10/hour × 50 TAs = **~$10,000/year savings** cho một trường quy mô 1000 students

**TAM Estimate**:
- **Scope**: All CS/IT students in Vietnam universities who need after-hours support
- **Number**: ~61,250 students (if commercial)
- **Cost savings potential**: $10,000-20,000/year per university (for 1000-student scale)
- **Confidence**: Low — đây là estimate rộng, cần research thêm

---

### SAM (Serviceable Addressable Market)

**Câu hỏi**: Với segment và phạm vi hiện tại, ta có thể phục vụ được bao nhiêu?

**Definition**: First-year CS students tại VinUniversity trong academic year hiện tại.

**Assumptions & Logic**:

1. **VinUniversity CS students**:
   - Fact (từ proposal): ~300 sinh viên/khóa học/kỳ học, tổng ~1000 sinh viên/năm
   - Assumption: First-year students là 30% của tổng (300 students)
   - Estimate: **~300 first-year CS students** per academic year

2. **Phạm vi hiện tại**:
   - Chỉ triển khai cho **CS department** (không phải toàn trường)
   - Chỉ support **programming labs** (không phải tất cả môn học)
   - Chỉ **first-year** (chưa expand sang năm 2, 3, 4)

3. **Adoption rate**:
   - Assumption: 80% adoption trong first-year class (vì được integrate vào LMS)
   - Estimate: 300 × 80% = **~240 active users** trong năm đầu

**SAM Estimate**:
- **Segment**: First-year CS students at VinUniversity
- **Number**: ~240 active users (trong 1000 total CS students)
- **Scope**: Programming labs only, PDPA-compliant hybrid deployment
- **Confidence**: Medium — có data cụ thể từ proposal

---

### SOM (Serviceable Obtainable Market)

**Câu hỏi**: Trong 12-24 tháng tới, ta có thể chiếm được bao nhiêu?

**Definition**: Realistic number of active users trong năm đầu triển khai tại VinUniversity.

**Assumptions & Logic**:

1. **Pilot phase (Months 1-3)**:
   - Target: 1 lớp pilot với 50 students
   - Assumption: 60% adoption (do awareness chưa cao)
   - Estimate: **~30 active users**

2. **Scale phase (Months 4-12)**:
   - Expand to tất cả first-year classes (3-4 lớp, 150-200 students)
   - Assumption: 80% adoption (sau khi đã demo, feedback tích cực)
   - Estimate: 200 × 80% = **~160 active users**

3. **Year 2 (Months 13-24)**:
   - Expand to second-year courses
   - Assumption: 100% first-year + 50% second-year = 300 + 150 = 450 students
   - Adoption: 85% → **~380 active users**

**SOM Estimate**:
- **Month 1-3**: ~30 active users (pilot)
- **Month 4-12**: ~160 active users (full first-year)
- **Month 13-24**: ~380 active users (first-year + partial second-year)
- **Confidence**: Medium-High — dựa trên adoption curve điển hình cho educational tools

---

### Tóm tắt TAM/SAM/SOM

| Layer | Estimate | Key assumptions | Confidence |
|-------|----------|-----------------|------------|
| **TAM** | ~61,250 students (nationwide CS/IT) OR $10-20K savings/university/year | 250 schools × 350 avg CS students × 70% need; $10/hour TA cost | Low |
| **SAM** | ~240 active users (VinUniversity first-year CS) | 300 first-year × 80% adoption | Medium |
| **SOM (12-24 months)** | ~380 active users | Expand to second-year, 85% adoption | Medium-High |

---

### Top 3 unknowns requiring further research

1. **Actual TA workload & cost structure tại VinUniversity**:
   - Hiện tại TA làm việc bao nhiêu giờ/tuần?
   - Chi phí cho TA personnel là bao nhiêu?
   - Điều này ảnh hưởng đến ROI calculation

2. **Student willingness to use AI vs human TA**:
   - Sinh viên có tin tưởng chatbot không?
   - Adoption rate thực tế có đạt 80% không?
   - Cần survey/pilot để validate

3. **Course materials availability & quality**:
   - Tất cả course materials (slides, labs, assignments) có sẵn trong digital format không?
   - FAISS indexing có đủ quality để đạt hit rate >70% không?
   - Cần audit course materials trước khi triển khai

---

### Final judgment: Is this market worth pursuing now?

**✅ Worth pursuing now** — với các điều kiện:

**Reasons to pursue**:
1. **Clear problem**: Sinh viên cần help ngoài giờ, TA quá tải — đều là real pains
2. **Compliance moat**: Hybrid deployment tạo barrier cho competitors pure-cloud
3. **Early adopter sẵn sàng**: VinUniversity là trường mới, open to innovation, có CS department
4. **Cost savings tangible**: Giảm 20 giờ/tuần TA = ~$10K/year savings (đủ justify investment)
5. **Expandable**: Sau thành công với CS, có thể expand sang các môn khác (Math, Physics)

**Caveats**:
- Chưa có revenue model (internal tool) — cần approval từ VinUniversity budget
- Technical complexity (hybrid deployment) cao hơn pure cloud
- Cần validate RAG quality với course materials thực tế

**Next steps before full commitment**:
1. Run 4-week pilot với 1 lớp (50 students) để đo adoption rate, accuracy, user satisfaction
2. Audit course materials để đảm bảo đủ quality cho RAG
3. Confirm TA workload data để tính ROI chính xác

---
