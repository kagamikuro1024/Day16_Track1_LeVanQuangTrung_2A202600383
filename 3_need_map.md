# 3. NEED MAP
## TA_Chatbot — AI Trợ Giảng

---

### Câu hỏi chính: What real pain exists here, even before AI?
**Nỗi đau thật ở đây là gì, ngay cả trước khi có AI?**

---

## 2-3 UNDERSERVED NEEDS

### Need #1 (Priority) — Immediate Help Outside TA Hours

**Need statement (JTBD):**
```
When I'm working on a programming lab at night and encounter a bug I can't solve,
I want to get a reliable, course-specific answer within 5 minutes,
so I can continue my work without losing momentum or missing the deadline.
```

**Current workaround:**
- Google/StackOverflow (30-60 phút tìm kiếm, thông tin không chắc chắn, có thể sai với khóa học)
- Hỏi bạn cùng lớp (chất lượng hỗ trợ không đồng đều, họ cũng có thể sai)
- Đợi mail của TA (chỉ ban ngày, không phải tối/cuối tuần), câu hỏi bị đưa vào hàng đợi hoặc bị quên trả lời
- Bỏ qua/tạm dừng bài tập → mất thời gian, nộp bài trễ/không hoàn thiện

**Pain signal:**
- **Time loss**: 2-4 giờ mỗi lần bị stuck với bug đơn giản, câu hỏi gửi cho TA bị quá tải và đưa vào hàng đợi từ 12h - 24h
- **Deadline anxiety**: Sinh viên thức trắng đêm, stress cao, chất lượng bài nộp giảm
- **Learning disruption**: Mất flow, khó tiếp thu kiến thức mới khi bị kẹt
- **Frustration**: Cảm giác bỏ cuộc, giảm motivation học tập

**Evidence / Proxy evidence:**
- **Direct evidence**: TA office hours chỉ ban ngày, sinh viên cần hỗ trợ tối/cuối tuần
- **Proxy evidence**:
  - Industry standard: 70%+ của câu hỏi trong programming labs là cơ bản (syntax, debugging, concept) — có thể tự động hóa
  - Observation: Sinh viên năm 1 có nhiều câu hỏi lặp lại nhất (theo TA experience)
  - Data point: TA workload phân bổ 60% thời gian cho các câu hỏi lặp lại (theo proposal)
  - Gen Z behavior: Quen với instant support (messenger, ChatGPT) — kỳ vọng response < 5 phút

**Why underserved:**
- Current solution (TA office hours) không match với **actual workflow** của sinh viên (học tối/cuối tuần)
- StackOverflow/Google cung cấp thông tin **không grounded** trong course materials → có thể gây hiểu sai
- No existing system provides **24/7, course-specific, reliable** support
- TA resources limited (1:50 ratio) → không thể scale với demand

---

### Need #2 — Trustworthy, Course-Grounded Answers

**Need statement (JTBD):**
```
When I'm learning a new programming concept and need clarification,
I want to receive answers that are directly sourced from my course materials,
so I can trust the information and avoid learning incorrect concepts that will hurt my exams and future courses.
```

**Current workaround:**
- Đọc lại slides/PDF (chậm, khó tìm đúng section)
- Hỏi TA (giới hạn giờ, chờ đợi)
- Tìm trên Google/YouTube (thông tin không nhất quán với giáo trình)
- Hỏi ChatGPT (có thể "hallucinate" — tạo thông tin sai không grounded trong khóa học)

**Pain signal:**
- **Misinformation risk**: Nhận câu trả lời sai từ ChatGPT/StackOverflow → học sai concept → fail exam
- **Time waste**: Phải cross-check nhiều nguồn để đảm bảo đúng với khóa học
- **Confusion**: Different sources nói khác nhau → không biết tin ai
- **Learning inefficiency**: Không chắc câu trả lời có đúng với cách giảng dạy của professor không

**Evidence / Proxy evidence:**
- **Direct evidence**: "Sinh viên tìm câu trả lời trên StackOverflow/ChatGPT — dễ nhận thông tin sai lệch, không grounded trong course materials"
- **Proxy evidence**:
  - LLM hallucination rate: 5-15% trên các câu hỏi chuyên môn (industry benchmark)
  - Student surveys: 68% sinh viên báo cáo từng nhận thông tin sai từ ChatGPT về programming concepts
  - Academic integrity concern: Professors cấm sử dụng ChatGPT vì fear of misinformation
  - RAG hit rate target >70% trong proposal → chứng tỏ cần grounding vào course materials

**Why underserved:**
- Generic LLM (ChatGPT) không biết context của khóa học cụ thể → không thể đảm bảo accuracy
- Current TA system không scale để trả lời tất cả câu hỏi với quality control
- No existing solution kết hợp **24/7 availability + course-specific grounding + citations**

---

### Need #3 — Reduce TA Repetitive Workload (Secondary Need)

**Need statement (JTBD):**
```
As a TA/teaching assistant,
I want to offload repetitive, low-value questions (syntax errors, basic concepts) to an automated system,
so I can focus my limited time on high-value, complex questions that truly require human expertise.
```

**Current workaround:**
- Trả lời tất cả câu hỏi thủ công (email, office hours, chat groups)
- Lặp lại câu trả lời gần như tương tự cho nhiều sinh viên (copy-paste, trả lời trực tiếp lặp lại trong giờ thực hành,...)
- Mất 10-20 giờ/tuần cho các câu hỏi cơ bản
- Không có thời gian cho các câu hỏi sâu, phức tạp

**Pain signal:**
- **Time drain**: 60% thời gian TA đi vào questions có sẵn câu trả lời trong slides/FAQ
- **Burnout**: Lặp lại cùng câu hỏi hàng trăm lần mỗi học kỳ
- **Low impact**: Không có thời gian mentoring sinh viên yếu, thiết kế lab tốt hơn
- **Scalability limit**: Thêm sinh viên = thêm workload tuyến tính, không scale

**Evidence / Proxy evidence:**
- **Direct evidence**: "TA quá tải — mất nhiều thời gian trả lời các câu hỏi lặp đi lặp lại"
- **Proxy evidence**:
  - Industry: 70% của support tickets là repetitive/known issues (Pareto principle)
  - TA-to-student ratio: 1:50 là insufficient cho 24/7 support
  - Cost analysis: Human review chiếm 67% chi phí → cần giảm
  - Observation: Các câu hỏi syntax error ("lỗi biên dịch", "khai báo biến") xuất hiện hàng nghìn lần mỗi học kỳ

**Why underserved:**
- No tooling để automatically handle FAQ/repetitive questions
- TA phải là single point of failure cho tất cả câu hỏi
- Không có tri thức phân phối (knowledge base) được maintain một cách chủ động

---

### Checkpoint 2 — Need Review Gate

**Kill question cho mỗi need:**
Nếu need này được giải quyết tốt, điều gì thay đổi rõ nhất về mặt kinh doanh?

**Need #1 (Immediate help):**
→ Sinh viên giảm stress, tăng completion rate, cải thiện learning outcome
→ Đo được: Giảm số lượng hỏi "deadline extension", tăng điểm trung bình lớp

**Need #2 (Trustworthy answers):**
→ Giảm misinformation, tăng confidence của sinh viên vào hệ thống
→ Đo được: Giảm số lượng student complaints về thông tin sai, tăng trust score

**Need #3 (Reduce TA workload):**
→ TA có thời gian cho high-value tasks, giảm burnout
→ Đo được: Giảm 20 giờ/tuần TA workload, tăng satisfaction score

**5 Tiêu chuẩn đánh giá:**

| Tiêu chí | Need #1 | Need #2 | Need #3 |
|----------|---------|---------|---------|
| **Not a disguised feature** | ✅ (Pain: stuck at night) | ✅ (Pain: misinformation) | ✅ (Pain: repetitive work) |
| **Recurring pain** | ✅ (3-5x/tuần/sv) | ✅ (Mỗi lần học concept mới) | ✅ (Hàng nghìn câu/học kỳ) |
| **Workaround exists** | ✅ (Google, wait for TA) | ✅ (ChatGPT, StackOverflow) | ✅ (Trả lời thủ công) |
| **Evidence present** | ✅ (TA hours mismatch) | ✅ (Hallucination risk) | ✅ (Time tracking data) |
| **Solves changes outcome** | ✅ (Completion rate ↑) | ✅ (Learning quality ↑) | ✅ (TA efficiency ↑) |

**Kết luận**: All 3 needs PASS — Priority order: #1 > #2 > #3

---

