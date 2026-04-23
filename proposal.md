# PROPOSAL: TA_Chatbot — Hệ Thống AI Trợ Giảng
**VinUniversity · Department of Computer Science · AI TA Chatbot Team**
**Ngày:** 22/04/2026 | **Phiên bản:** 1.0


---


## 1. PROJECT OVERVIEW


### 1.1 Tóm tắt sản phẩm


**TA_Chatbot — AI Trợ Giảng** là hệ thống chatbot thông minh hỗ trợ sinh viên trả lời các câu hỏi về các môn học lập trình có lab/code. Hệ thống kết hợp **ReAct Agent + RAG Pipeline** để cung cấp câu trả lời có căn cứ từ tài liệu khóa học, hoạt động 24/7 mà không phụ thuộc vào giờ hành chính của giảng viên/TA.


### 1.2 Bài toán được giải quyết


| # | Vấn đề | Mô tả |
|---|--------|-------|
| 1 | **Hỗ trợ ngoài giờ** | Sinh viên cần giải đáp thắc mắc kỹ thuật vào ban đêm, cuối tuần — không có TA nào sẵn sàng |
| 2 | **TA quá tải** | TA mất nhiều thời gian trả lời các câu hỏi lặp đi lặp lại (syntax, build error, cơ bản) |
| 3 | **Thiếu nguồn đáng tin cậy** | Sinh viên tìm câu trả lời trên StackOverflow/ChatGPT — dễ nhận thông tin sai lệch, không grounded trong course materials |
| 4 | **Khó tiếp cận với môn học** | Sinh viên gặp khó khăn khi tiếp cận các môn học mới, đặc biệt là các môn có lab thực hành |
| 5 | **Cần hỗ trợ 1-1** | Sinh viên cần hỗ trợ 1-1 với TA để giải đáp các câu hỏi phức tạp -> Hệ thống có luồng hỗ trợ kết nối TA qua mail|
| 6 | **Thông tin môn học/kiến thức chuyên môn không được cập nhật kịp thời** | Sinh viên không thể tiếp cận thông tin/kiến thức chuyên môn môn học một cách nhanh chóng -> Hệ thống có luồng hỗ trợ cập nhật thông tin môn học dành cho giáo viên/TA |


### 1.3 Người dùng chính


- **Primary**: ~300 sinh viên/khóa học/kỳ học. Tầm 1000 sinh viên/năm (3 - 5 khóa học)
- **Secondary**: Giảng viên/TA — nhận escalation khi chatbot không tự tin trả lời
- **Admin**: Quản trị hệ thống, cập nhật thông tin môn học, xem thống kê.


### 1.4 Trạng thái hiện tại (Current State)


```
✅ ReAct Agent (LangGraph) — đang hoạt động
✅ RAG Pipeline với FAISS — semantic retrieval từ course materials
✅ 5 Tools: search_materials, analyze_code, verify_info, escalate, detect_trigger
✅ System prompt v2 với guardrails & escalation logic
✅ Deployed trên Railway (MVP)
⚠️  Chưa có: model routing, semantic caching, on-premise LLM
⚠️  Chưa có: load testing, CI/CD, cost monitoring
```


---


## 2. ENTERPRISE CONTEXT


### 2.1 Bối cảnh tổ chức


| Tiêu chí | Chi tiết |
|----------|---------|
| **Khách hàng** | VinUniversity — Department of Computer Science |
| **Quy mô** | ~300 sinh viên/khóa học/kỳ học, tổng khoảng 1000 sinh viên, ~ 10 - 20 TA/giảng viên |
| **Phạm vi áp dụng** | Tất cả khóa học (5–10 khóa học/năm) |
| **Môi trường vận hành** | Academic term — cần sẵn sàng liên tục, đặc biệt trong kỳ thi |


### 2.2 Phân loại dữ liệu

| Loại dữ liệu | Ví dụ | Mức nhạy cảm | Yêu cầu |
|-------------|-------|-------------|---------|
| **PII Sinh viên** | Tên, Student ID, lịch học, điểm số | 🔴 CAO | Encrypt at rest (AES-256), audit trail (7 years), PDPA compliance, **KHÔNG rời Việt Nam** |
| **Academic Records** | Kết quả bài tập, đánh giá | 🔴 CAO | PDPA compliance, RBAC, retention 2 years, right to delete |
| **Course Materials** | Slides, FAQ, code samples | 🟢 THẤP | Có thể public/cloud, no encryption needed |
| **Query Logs** | Câu hỏi của sinh viên | 🟡 TRUNG BÌNH | Anonymize (remove PII) trước khi lưu dài hạn, retain 90 days hot + 1 year warm |

**Data Flow Policy:**
- **On-Premise Only:** Student PII, sensitive queries, audit logs
- **Cloud Allowed:** Non-PII queries, aggregated metrics, course materials
- **Encryption:** TLS 1.3 in transit, AES-256 at rest (PostgreSQL, Redis)


### 2.3 Ràng buộc Enterprise (Top 3)

**① Data Residency — Dữ liệu sinh viên PHẢI lưu trong lãnh thổ Việt Nam**
> Student PII không được truyền trực tiếp lên OpenAI API hoặc bất kỳ server nước ngoài nào. Vi phạm điều này dẫn đến trách nhiệm pháp lý và rủi ro danh tiếng nghiêm trọng cho trường.
>
> **Implementation:**
> - PII Classifier với confidence threshold 90% (see Section 2.4)
> - Nếu PII detected hoặc uncertain (<90% confidence) → route to **On-Premise LLM ONLY**
> - Chỉ các query đã được xác nhận **KHÔNG** chứa PII (confidence > 90%) mới được gửi lên Cloud API
> - Logging đầy đủ để audit trail

**② PDPA Compliance — Cơ chế bảo mật & Phân loại dữ liệu (PII Detection)**
> Hệ thống áp dụng cơ chế **Fail-safe Detection** (multi-layer):
> - **Layer 1 — Regex:** Email (`/^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/i`), Phone (`/^(\+84|0)[1-9]\d{8}$/`), Student ID (`/^[A-Z]{2}\d{6,8}/`), Vietnamese names
> - **Layer 2 — NER:** spaCy `vi_core_news_lg` để detect PERSON, ORG, DATE với confidence scoring
> - **Layer 3 — Heuristics:** Keyword detection ("mã số", "họ tên", "điểm"), code context analysis
> - **Ensemble:** Weighted average (Regex 40%, NER 40%, Heuristics 20%)
> - **Threshold:** confidence < 90% → route on-prem (fail-safe), confidence > 90% PII → on-prem, confidence < 10% PII → cloud
> - **Audit:** Tất cả classification decisions được log với full metadata
> - **RBAC:** Chỉ authorized personnel (TA/Admin) có thể xem PII data

**③ 24/7 Reliability — Sẵn sàng trong toàn bộ học kỳ**
> Uptime tối thiểu 99% trong academic term. Đặc biệt quan trọng trong 2 tuần trước thi khi traffic tăng đột biến 3–5x.
>
> **SLO Targets:**
> - Response latency p95: < 3 giây
> - Error rate: < 1%
> - RAG hit rate (hit@3): > 70%
> - Fallback activation rate: < 10%
> - System uptime: > 99% (academic term)
>
> **Multi-layer fallback:**
> 1. OpenAI timeout/5xx → retry 3× (exponential backoff 1s→2s→4s) → fallback to on-prem LLM
> 2. On-prem LLM fail (GPU down) → switch to OpenAI Opus (if PII not detected)
> 3. Both fail OR FAISS offline → Human escalation (TA notified immediately via email + dashboard alert)
> 4. Railway instance crash → auto-restart, load balancer routes to healthy
>
> **Disaster Recovery:**
> - RTO (Recovery Time Objective): < 15 minutes for full system
> - RPO (Recovery Point Objective): < 5 minutes data loss (WAL streaming)
> - Backup strategy: Daily full + continuous WAL (PostgreSQL), FAISS index backup hourly


---


## 3. DEPLOYMENT CHOICE: HYBRID ARCHITECTURE


### 3.1 Kết luận: Chọn mô hình **Hybrid (On-Premise + Cloud)**


#### So sánh các phương án


| Tiêu chí | ☁️ Full Cloud | 🖥️ Full On-Premise | 🔀 Hybrid *(Chọn)* |
|----------|------------|-----------------|-----------------|
| Data Control | ❌ Thấp | ✅ Cao | ✅ Cao |
| PDPA Compliance | ❌ Vi phạm | ✅ Tuân thủ | ✅ Tuân thủ |
| Setup Time | ✅ Phút | ❌ Tuần | ✅ ~1 tuần |
| Chi phí MVP | $50/tháng | $0 + GPU | $70/tháng |
| Khả năng scale | ✅ Tốt | ❌ Cần thêm GPU | ✅ Tốt |
| Độ phức tạp | Thấp | Cao | ⚠️ Trung bình |


### 3.2 Lý do chọn Hybrid


**Lý do 1: Compliance & Fail-safe Data Control**


Dữ liệu nhạy cảm của sinh viên (PII, query context) không được rời khỏi Việt Nam. Kiến trúc Hybrid tích hợp lớp **PII Scrubber/Classifier** để tự động điều hướng: các câu hỏi chứa thông tin cá nhân sẽ được xử lý 100% tại **on-premise LLM (Llama 3/vLLM)**, chỉ các câu hỏi kiến thức chung mới được gửi lên Cloud API.


**Lý do 2: Cost-Performance Balance (Optimized)**


Phân tích traffic dự kiến: 80% queries là đơn giản (syntax, basic concepts) → xử lý bằng Cloud API model nhỏ (Haiku) để tiết kiệm. 20% queries phức tạp hoặc nhạy cảm → xử lý On-prem. Mô hình này giúp tránh việc đầu tư quá nhiều GPU server ngay từ đầu mà vẫn đảm bảo an toàn dữ liệu.


### 3.3 Kiến trúc triển khai


```
┌─────────────────────────────────────────────────────────┐
│                    USER (Sinh viên)                      │
└─────────────────────┬───────────────────────────────────┘
                      │ HTTPS Query
                      ▼
┌─────────────────────────────────────────────────────────┐
│         FRONTEND LAYER (Cloud — Railway)                 │
│   Streamlit UI + PII Classifier (Regex/NER)              │
└────────┬──────────────────────────┬──────────────────────┘
         │                          │
    [PII Detected or Unsure]    [Clean/Public Content]
         │                          │
         ▼                          ▼
┌─────────────────┐     ┌──────────────────────────────┐
│  ON-PREMISE LLM  │     │   CLOUD API (OpenAI/Anthropic)│
│  Ollama / vLLM   │     │   Haiku 3.5 (simple queries)  │
│  (VN Server)     │     │   (non-sensitive content)     │
└────────┬────────┘     └──────────────┬───────────────┘
         │                             │
         └─────────────┬───────────────┘
                       ▼
         ┌─────────────────────────────┐
         │   RAG LAYER (On-Premise)     │
         │   FAISS Vector Index         │
         │   Course Materials Store     │
         └─────────────────────────────┘
```


**Trade-off chấp nhận:** Độ phức tạp vận hành tăng (cần quản lý cả on-prem + cloud), nhưng đây là điều kiện bắt buộc để đảm bảo PDPA compliance.


### 3.4 Cấu hình phần cứng & Mô hình On-premise


| Thành phần | Chi tiết cấu hình |
|------------|-------------------|
| **Model** | Llama 3 - 8B / 70B (Quantized 4-bit/8-bit) |
| **GPU / VRAM** | Min 12GB (RTX 3060) | Rec 24GB (RTX 4090/A10G) |
| **Inference Engine** | vLLM (Hỗ trợ Continuous Batching) |
| **Latency Target** | < 100ms/token (On-prem) |


---


## 4. COST ANALYSIS


### 4.1 Giả định & Ước tính Lưu lượng (Conservative Estimate)


| Metric | MVP Tier | Growth Tier |
|--------|----------|-------------|
| Users | 50 sinh viên (1 lớp pilot) | 300–500 sinh viên (3–4 lớp) |
| Requests/ngày | 100–150 queries | 500–800 queries |
| Peak (queries/giờ) | 30–40 (tối + kỳ thi) | 100–150 |
| Avg tokens/request | Input: 800 / Output: 300 | Tương tự |


### 4.2 Phân tích chi phí theo layer


#### Layer 1 — API Tokens (OpenAI Haiku 3.5)


| | MVP | Growth |
|-|-----|--------|
| Requests/ngày | 100 | 600 |
| Tính toán | 100 × 1,100 tokens × 30 ngày × $0.000003 | 600 × 1,100 × 30 × $0.000003 |
| **Chi phí** | **~$9/tháng** | **~$54/tháng** |


#### Layer 2 — Compute


| Thành phần | MVP | Growth |
|-----------|-----|--------|
| Railway (Frontend + Retriever) | $5/tháng | $15/tháng |
| GPU Server (On-prem Ollama) | $0 (khởi động) | $50/tháng |
| **Subtotal** | **$5/tháng** | **$65/tháng** |


#### Layer 3 — Vector Storage (FAISS)


| | MVP | Growth |
|-|-----|--------|
| FAISS local | $0 | $0 |
| Cloud Vector DB (nếu scale) | N/A | $20–50/tháng |
| **Subtotal** | **$0** | **$20/tháng** |


#### Layer 4 — Human Review & Monitoring


| Thành phần | MVP | Growth |
|-----------|-----|--------|
| TA review (2h/tuần × $10/h) | $80/tháng | $150/tháng (3h/tuần) |
| Monitoring & logging | $10/tháng | $20/tháng |
| **Subtotal** | **$90/tháng** | **$170/tháng** |


#### Layer 5 — Hidden Costs (thường bị bỏ quên)


| Thành phần | Tỷ lệ | Ghi chú |
|-----------|-------|---------|
| Retry overhead (LLM fail) | +10% token cost | ~$1/tháng MVP |
| Safety filtering & guardrails | +5% compute | ~$0.5/tháng MVP |
| Logging & audit trail | Cố định | $10–20/tháng |
| A/B testing models & prompts | One-time effort | ~20h setup |
| Evaluation pipeline benchmark | One-time effort | ~20h setup |


### 4.3 Tổng hợp chi phí


```
╔══════════════════════════════════════════════════════════╗
║              MVP TIER (50 users, 100 req/ngày)           ║
╠══════════════════════════════════════════════════════════╣
║  API Tokens (OpenAI)       :   $9/tháng                  ║
║  Compute (Railway)         :   $5/tháng                  ║
║  Vector Storage            :   $0/tháng                  ║
║  Human Review              :  $80/tháng   ← Cost driver  ║
║  Monitoring                :  $10/tháng                  ║
║  Hidden costs (15%)        :  $16/tháng                  ║
╠══════════════════════════════════════════════════════════╣
║  TỔNG CỘNG MVP             : ~$120/tháng                 ║
║  Chi phí/user              :   $2.4/user/tháng           ║
╚══════════════════════════════════════════════════════════╝


╔══════════════════════════════════════════════════════════╗
║            GROWTH TIER (300 users, 600 req/ngày)         ║
╠══════════════════════════════════════════════════════════╣
║  API Tokens (OpenAI)       :  $54/tháng                  ║
║  Compute (Railway + GPU)   :  $65/tháng                  ║
║  Vector Storage (Pinecone) :  $20/tháng                  ║
║  Human Review              : $150/tháng   ← Cost driver  ║
║  Monitoring                :  $20/tháng                  ║
║  Hidden costs (15%)        :  $46/tháng                  ║
╠══════════════════════════════════════════════════════════╣
║  TỔNG CỘNG GROWTH          : ~$355/tháng                 ║
║  Chi phí/user              :   $1.2/user/tháng (scale)   ║
╚══════════════════════════════════════════════════════════╝
```


### 4.4 Phân tích Cost Driver


```
Cost Distribution (MVP):
  Human Review    ████████████████████████████████  67%  ← Tối ưu ưu tiên
  Compute         ████████                           17%
  API Tokens      ████████                            8%
  Monitoring      ████                                8%
```


> **Insight quan trọng:** Human review chiếm 67% tổng chi phí — đây là cost driver lớn nhất. Chiến lược tối ưu phải tập trung vào việc **giảm tỷ lệ phản hồi cần review thủ công** (nâng accuracy từ 70% → 85%+).


### 4.5 Chiến lược giảm chi phí Human Review


Để giảm gánh nặng chi phí TA, hệ thống áp dụng 3 cơ chế:
1. **Confidence Thresholding**: Chỉ đẩy câu hỏi cho TA khi AI tự đánh giá độ tin cậy < 0.75.
2. **Auto-Approval**: Các câu hỏi FAQ hoặc Syntax cơ bản có độ tương đồng cao (>0.9) với bộ dữ liệu chuẩn sẽ được tự động trả lời mà không cần review.
3. **HITL Feedback Loop**: TA chỉ cần sửa các câu trả lời sai. Các bản sửa này được dùng để refine prompt và cập nhật RAG context ngay lập tức, giúp AI không lặp lại lỗi cũ.


---


## 5. OPTIMIZATION PLAN


### 5.1 Ba chiến lược tối ưu


#### Chiến lược 1: Model Routing — Haiku cho simple, Opus cho complex


| Thông tin | Chi tiết |
|-----------|---------|
| **Tiết kiệm** | 40–60% token cost |
| **Cơ chế** | Phân loại query complexity (embedding similarity / keyword rules) → Simple → Haiku 3.5 ($3/1M tokens); Complex → Opus ($15/1M tokens) |
| **Trade-off** | +50ms latency cho classification step |
| **Khi áp dụng** | 🟢 **Ngay lập tức (MVP)** — ROI cao, dễ implement |
| **Tiết kiệm ước tính** | $4–5/tháng (MVP) → $20–30/tháng (Growth) |


**Phân loại query:**
```
Simple (→ Haiku):
  - Câu hỏi syntax: "Cách khai báo mảng trong C?"
  - Định nghĩa khái niệm cơ bản: "Con trỏ là gì?"
  - Tra cứu trong course materials


Complex (→ Opus / On-prem):
  - Debug lỗi segmentation fault phức tạp
  - Phân tích kiến trúc chương trình
  - Giải thích trade-off giữa các cách tiếp cận
```


#### Chiến lược 2: Semantic Caching — Cache các câu hỏi tương tự


| Thông tin | Chi tiết |
|-----------|---------|
| **Tiết kiệm** | 20–40% (nếu queries lặp lại nhiều) |
| **Cơ chế** | Embed query → compare cosine similarity với cache (threshold > 0.85) → Nếu match: reuse response (chỉ tính 10% token cost) |
| **Stack** | Redis (local) hoặc in-memory cache |
| **Trade-off** | Thêm Redis dependency, stale cache risk nếu course materials thay đổi |
| **Khi áp dụng** | 🟡 **Sau MVP** — khi phát hiện repeated question patterns |
| **Tiết kiệm ước tính** | $10–20/tháng (Growth tier) |


#### Chiến lược 3: Context Compression — Tóm tắt tài liệu trước khi gửi LLM


| Thông tin | Chi tiết |
|-----------|---------|
| **Tiết kiệm** | 15–30% input tokens |
| **Cơ chế** | RAG retrieve → dùng Haiku tóm tắt chunk (từ 800 → 300 tokens) → gửi summary + question lên main LLM |
| **Trade-off** | Có thể mất chi tiết kỹ thuật quan trọng — cần A/B test kỹ |
| **Khi áp dụng** | 🟡 **Growth tier** — khi context window trở nên costly |
| **Tiết kiệm ước tính** | $5–10/tháng (MVP) → $40–60/tháng (Growth) |


### 5.2 Bảng so sánh & Lộ trình áp dụng


| Chiến lược | Tiết kiệm | Độ phức tạp | Khi áp dụng | ROI |
|-----------|----------|-----------|-----------|-----|
| Model Routing | 40–60% | 🟢 Thấp | Ngay (MVP) | ⭐⭐⭐ Cao |
| Semantic Caching | 20–40% | 🟡 Trung bình | Sau 1 tháng | ⭐⭐⭐ Cao |
| Context Compression | 15–30% | 🟡 Trung bình | Growth tier | ⭐⭐ Trung |


```
Lộ trình tối ưu chi phí:
  MVP (hiện tại)   : $120/tháng
  + Chiến lược 1   : → ~$70/tháng  (tiết kiệm 42%)
  + Chiến lược 2   : → ~$55/tháng  (tại Growth tier: $355 → $250)
  + Chiến lược 3   : → tiếp tục giảm 15%
```


---


## 6. RELIABILITY & SCALING PLAN


### 6.1 Ba kịch bản lỗi & phương án xử lý


#### Kịch bản 1: OpenAI API Timeout


| | Chi tiết |
|-|---------|
| **Xác suất xảy ra** | ~5% (cao nhất vào peak hours) |
| **Tác động** | Sinh viên không nhận được câu trả lời, trải nghiệm xấu |
| **Xử lý ngắn hạn** | Retry logic: 3 lần, exponential backoff (1s → 2s → 4s) → sau 10s fallback sang on-premise Ollama |
| **Giải pháp dài hạn** | Multi-provider fallback (Anthropic Claude làm backup); alert khi error rate > 5% |
| **Metrics theo dõi** | API latency (p50/p95/p99), error rate, fallback activation rate |


#### Kịch bản 2: FAISS Index Offline


| | Chi tiết |
|-|---------|
| **Xác suất xảy ra** | ~1% (đặc biệt nếu chạy on-premise) |
| **Tác động** | Agent không retrieve được course materials → blind responses |
| **Xử lý ngắn hạn** | Graceful degradation: trả lời "Xin lỗi, hệ thống đang lỗi. Vui lòng liên hệ TA." + log + alert ngay lập tức |
| **Giải pháp dài hạn** | Backup FAISS index trên S3/cloud; auto-recovery script khi phát hiện index corrupt |
| **Metrics theo dõi** | Index health check (mỗi 5 phút), retrieval latency, hit rate |


#### Kịch bản 3: Peak Traffic Surge (Kỳ thi)


| | Chi tiết |
|-|---------|
| **Xác suất xảy ra** | ~20% trong 2 tuần thi |
| **Tác động** | Response time > 5s, hàng đợi tích tụ, user experience xấu nghiêm trọng |
| **Xử lý ngắn hạn** | Queue incoming requests (async processing); tự động downgrade sang model nhỏ hơn (Haiku) |
| **Giải pháp dài hạn** | Auto-scale Railway instances; load balancer; pre-warming instance trước kỳ thi |
| **Metrics theo dõi** | Request latency, queue depth, throughput (req/s) |


### 6.2 Monitoring & SLO Targets


```
SLO Targets (Service Level Objectives):
┌──────────────────────────────────────────────────────┐
│  Response latency p95     : < 3 giây                 │
│  Error rate               : < 1%                     │
│  Fallback activation rate : < 10%                    │
│  RAG hit rate (hit@3)     : > 70%                    │
│  System uptime            : > 99% (trong academic term)│
│  User satisfaction score  : > 4/5 (nếu có feedback)  │
└──────────────────────────────────────────────────────┘


Alert Thresholds:
  ⚠️  Latency > 5s          → Kiểm tra API status, scale up
  🔴  Error rate > 5%        → Activate on-premise fallback
  🔴  FAISS offline           → Pager alert TA ngay lập tức
  ⚠️  Daily cost > $5         → Investigate usage spike
  ⚠️  Fallback rate > 15%    → Review provider health
```


### 6.3 Fallback Strategy


| Kịch bản lỗi | Fallback | Thời gian kích hoạt |
|------------|---------|-------------------|
| OpenAI timeout | Retry × 3 → Ollama on-premise | 10 giây |
| FAISS offline | "Contact TA" + escalation alert | Ngay lập tức |
| Peak traffic | Queue + downgrade model | 30 giây (auto) |
| Multiple failures | Human escalation (TA nhận thông báo) | 30 giây |


### 6.4 Scaling Roadmap


| Giai đoạn | Cấu hình | Users | Chi phí ước tính |
|-----------|---------|-------|-----------------|
| **MVP** | 1 Railway instance + local FAISS | 50 | $120/tháng |
| **Growth** | 2–3 instances + load balancer + Pinecone | 300–500 | $355/tháng |
| **Scale** | Multi-instance, VN-region only, Redis cache | 1,000+ | ~$800/tháng |


---


## 7. TRACK RECOMMENDATION & NEXT STEPS


### 7.1 Self-Assessment (Trạng thái hiện tại của nhóm)


| Mảng kỹ năng | Điểm | Điểm mạnh | Điểm yếu |
|-------------|------|-----------|---------|
| **Business / Product** | 3/5 | User story rõ ràng; đã demo & collect feedback | Chưa formal user research; chưa có business case / revenue model |
| **Infra / Data / Ops** | 3.5/5 | Deployed on Railway; FAISS working; basic logging | Chưa có on-prem LLM; chưa CI/CD; chưa load testing |
| **AI Engineering** | 4/5 | ReAct agent; RAG pipeline; 5 tools; safety guardrails | Chưa optimize latency/cost; evaluation pipeline chưa hoàn thiện |


### 7.2 Track khuyến nghị cho Phase 2


#### ✅ Recommended: **Track 2+3 — Infra/Ops + AI Engineering (Hybrid)**


**Căn cứ lựa chọn:**
- Điểm mạnh nhất nằm ở **AI Engineering (4/5)** — nên tiếp tục phát triển theo hướng này
- Infra ở mức trung bình (3.5/5) — có nền tảng nhưng cần nhiều improvement để scale
- Business (3/5) — biết user nhưng chưa cần đầu tư sâu ở giai đoạn này vì đây là internal tool
- Dự án hiện tại cần: cost optimization (Infra) + RAG quality improvement (AI Engineering)


| Track | Mô tả | Phù hợp với TA_Chatbot? |
|-------|-------|------------------------|
| Track 1: Product/Biz | Monetization, market fit, user research | ❌ Chưa cần (internal tool) |
| **Track 2: Infra/Ops** | Deep dive deployment, cost, reliability | ✅ **CẦN THIẾT** |
| **Track 3: AI/Advancement** | RAG quality, multi-agent, evaluation | ✅ **CẦN THIẾT** |


### 7.3 Kỹ năng cần phát triển


| # | Kỹ năng | Lý do | Ứng dụng vào dự án |
|---|---------|-------|-------------------|
| 1 | **Distributed Systems** | Cần scale lên 300+ users, load balancing | Multi-instance Railway, Redis cache, request queue |
| 2 | **LLMOps** | Accuracy ~70% → cần nâng lên 85%+ | Prompt optimization, A/B testing models, evaluation pipeline |
| 3 | **Data Pipeline / ETL** | Course materials cập nhật theo từng học kỳ | Automated FAISS re-indexing khi có tài liệu mới |


### 7.4 Lộ trình Phase 2 (12 tuần)


```
Tháng 1 (Tuần 1–4): Foundation & Evaluation
  ├─ Week 1–4: Setup on-premise LLM infrastructure (vLLM + Llama 3)
  ├─ Week 2:   Xây dựng Golden Dataset (200+ case chuẩn)
  └─ Week 4:   Benchmark hệ thống hiện tại (Baseline)


Tháng 2 (Tuần 5–8): Scale & Monitor
  ├─ Week 5–6: Implement model routing (Haiku ↔ On-prem)
  ├─ Week 7:   Full monitoring stack (Grafana/Prometheus)
  └─ Week 8:   Load testing & Semantic Caching


Tháng 3 (Tuần 9–12): Quality & Advanced Features
  ├─ Week 9–10:  Optimization vòng 2 (nâng accuracy → 85%+)
  ├─ Week 11:    Automated ETL cho course materials mới
  └─ Week 12:    Multi-agent prototype & Final Audit
```


### 7.5 Khung đánh giá chất lượng (Evaluation Framework)


Để đảm bảo hệ thống không chỉ là "demo", chúng tôi xây dựng quy trình benchmark định kỳ dựa trên:
- **Golden Dataset**: Bộ 200+ câu hỏi & câu trả lời chuẩn (Ground Truth) được TA phê duyệt.
- **Metrics đo lường (RAGAS framework)**:
    - **Faithfulness**: Câu trả lời có trung thành với context không? (Tránh bịa đặt).
    - **Answer Relevance**: Câu trả lời có đúng trọng tâm câu hỏi không?
    - **Context Precision**: Tài liệu retrieve được có thực sự liên quan không?
- **Chỉ số vận hành**: Hallucination Rate < 2% và Latency p95 < 3.0s.


---


## 8. TRẢI NGHIỆM NGƯỜI DÙNG & TÁC ĐỘNG DOANH NGHIỆP


### 8.1 Thiết kế UX & Lòng tin (Trust)
Hệ thống được thiết kế để sinh viên luôn nắm quyền kiểm soát:
- **Citations**: Mỗi câu trả lời đều đính kèm nguồn trích dẫn (Slide ID, PDF Page) để sinh viên tự kiểm chứng.
- **Confidence Scoring**: Hiển thị mức độ tự tin của AI bằng màu sắc (Xanh: High, Vàng: Medium).
- **Smooth Escalation**: Nếu AI không chắc chắn, nút "Gửi yêu cầu cho TA" sẽ hiện lên cùng với lịch sử chat để TA nắm bắt ngữ cảnh nhanh nhất.


### 8.2 Chỉ số tác động Business (KPIs)
- **Auto-resolution Rate**: Mục tiêu 65% câu hỏi được giải quyết hoàn toàn bởi AI.
- **Efficiency Gain**: Dự kiến tiết kiệm 20 giờ làm việc/tuần cho mỗi team TA qua việc giảm trả lời các câu hỏi lặp lại.
- **Response Velocity**: Giảm thời gian chờ đợi của sinh viên từ vài tiếng (chờ TA online) xuống còn < 5 giây.


---


## APPENDIX: SUMMARY DASHBOARD


```
╔══════════════════════════════════════════════════════════════╗
║              TA_CHATBOT — PROPOSAL SUMMARY                   ║
╠══════════════════════════════════════════════════════════════╣
║  DEPLOYMENT    : Hybrid (On-Premise PII + Cloud non-PII)     ║
║  COMPLIANCE    : PDPA ✅ | Data Residency VN ✅               ║
╠══════════════════════════════════════════════════════════════╣
║  COST MVP      : $120/tháng  ($2.4/user)                     ║
║  COST GROWTH   : $355/tháng  ($1.2/user)                     ║
║  COST DRIVER   : Human Review (67%) ← ưu tiên tối ưu         ║
╠══════════════════════════════════════════════════════════════╣
║  OPTIMIZATION  :                                             ║
║    Phase 1 → Model Routing   : -42% cost (ngay)              ║
║    Phase 2 → Semantic Cache  : -20% thêm (sau 1 tháng)       ║
║    Phase 3 → Context Compress: -15% thêm (Growth tier)       ║
╠══════════════════════════════════════════════════════════════╣
║  RELIABILITY   :                                             ║
║    Uptime SLO  : 99% (academic term)                         ║
║    Latency p95 : < 3 giây                                    ║
║    Fallback    : Cloud → On-prem → Human escalation          ║
╠══════════════════════════════════════════════════════════════╣
║  TRACK P2      : Infra/Ops + AI Engineering (Track 2+3)      ║
║  TOP SKILLS    : Distributed Systems | LLMOps | Data Pipeline ║
╚══════════════════════════════════════════════════════════════╝
```


---


*Proposal này được chuẩn bị bởi nhóm AI TA Chatbot · VinUniversity · 22/04/2026*

