# 2. CUSTOMER / SEGMENT CARD
## TA_Chatbot — AI Trợ Giảng

---

### Segment name
**First-year CS students struggling with programming labs during peak study hours**

*(Sinh viên năm 1 ngành Computer Science gặp khó khăn với các bài lab lập trình trong giờ học cao điểm và sau giờ học)*

---

### Bối cảnh vận hành (Operational context)
Sinh viên năm 1 (khoảng 150-200 sv/khóa, khoa CS của VinUni) đang học các môn cơ bản như Intro to Programming, Data Structures. Họ thường:
- Làm bài tập/lab vào **tối (19h-23h)** và **cuối tuần** khi không có lớp
- Có ít kinh nghiệm debug, dễ mắc lỗi syntax và logic cơ bản
- Chưa quen với tài liệu khóa học, thường tìm kiếm nhanh trên Google/StackOverflow
- Cảm thấy **lo lắng** khi không có TA hỗ trợ (TA office hours thường ban ngày)
- Deadline bài tập thường vào cuối tuần/tối → áp lực cao

---

### Workflow lặp lại (Recurring workflow)
```
1. Nhận assignment/lab specification
2. Đọc tài liệu khóa học (slides, code samples)
3. Bắt đầu code → gặp lỗi (syntax error, runtime error, logic bug)
4. Tìm cách giải quyết:
   - Option A: Google/StackOverflow (có thể nhận thông tin sai)
   - Option B: Hỏi bạn (chất lượng hỗ trợ không đồng đều)
   - Option C: Đợi TA online trả lời(không có vào tối/cuối tuần)
   - Option D: Bỏ qua/tạm dừng bài tập → không tốt
5. Mất nhiều thời gian (2-4 giờ) cho một bug đơn giản
6. Deadline đến → stress, chất lượng bài nộp thấp
```

**Workflow này lặp lại 3-5 lần/tuần trong mỗi học kỳ.**

---

### Thời điểm đau nhất (Pain moment)
**Khoảnh khắc "stuck on a simple bug" vào 22h đêm trước deadline 0h sáng và không có ai giúp đỡ.**

Chi tiết:
- Lúc 22h, sinh viên mới bắt đầu làm bài
- Gặp lỗi segmentation fault hoặc logic bug
- Google 30 phút không thấy giải pháp rõ ràng
- Không có TA nào online để hỏi
- Bạn cùng lớp cũng bí
- Cảm giác: **panic, frustration, helplessness**
- Kết quả: Hoặc là thức trắng đêm debug, hoặc nộp bài chưa hoàn thiện

Đây là **pain moment cụ thể, có thể quan sát được, lặp lại hàng tuần**.

---

### Vì sao đáng làm lúc này (Why now)
1. **Academic pressure tăng**: Học kỳ đầu là khó khăn nhất, tỷ lệ bỏ học/dropout cao ở năm 1
2. **Behavioral shift**: Gen Z sinh viên **quen với instant support** (messenger, ChatGPT) — họ kỳ vọng trả lời ngay
3. **TA resources limited**: Tỷ lệ TA/sinh viên ~1:50, không thể cover 24/7
4. **Technology now viable**: LLM đủ tốt để giải quyết 70%+ câu hỏi cơ bản (syntax, debugging, concept explanation)
5. **Compliance requirement**: VinUniversity cần bảo vệ dữ liệu sinh viên → cần solution on-premise/hybrid (không phải pure cloud)

**Đây là thời điểm vàng để triển khai — nếu không làm bây giờ, sinh viên sẽ tiếp tục chịu stress và chất lượng học tập giảm.**

---

### Đường tiếp cận thực tế (Access path)
**Làm sao tiếp cận được segment này?**

1. **Direct integration**: Embed chatbot vào LMS (Canvas/Moodle) của VinUniversity — mỗi khi sinh viên xem assignment, chatbot hiện sẵn
2. **Orientation week**: Demo chatbot cho sinh viên năm 1 trong tuần orientation
3. **TA endorsement**: TA giới thiệu chatbot như một "resource bổ trợ" trong lớp
4. **Feedback loop**: Sinh viên báo cáo bugs, TA cập nhật course materials → chatbot học hỏi
5. **Low-friction signup**: Single sign-on với university account, không cần register thêm

**Access path rõ ràng, có thể thực hiện trong 2-4 tuần.**

---

### Quality test: Có thể hình dung customer trong 1 câu không?
**YES / NO**

> "First-year CS students who panic at 10pm the night before a lab deadline when they hit a bug they can't solve and have no TA to ask."

*(Sinh viên năm 1 CS hoảng loạn lúc 10h đêm trước deadline lab khi gặp bug không giải quyết được và không có TA để hỏi)*

**Nếu nhóm khác đọc câu này và hình dung được chính xác customer — Segment Card đã đủ sắc.**

---

### Checkpoint 1 — Segment Review Gate

**Kill question:**
Nếu chỉ được giữ một nhóm khách hàng trong 6 tháng đầu, nhóm này có còn là lựa chọn?

**Answer**: ✅ YES — vì:
- Segment này có pain rõ ràng, lặp lại
- Có access path rõ (LMS integration)
- Impact business outcome: giảm stress, tăng completion rate, cải thiện learning outcome
- Nếu thành công với năm 1, có thể expand sang năm 2, 3 sau

**4 Tiêu chuẩn đánh giá:**

| Tiêu chí | PASS | FAIL |
|----------|------|------|
| **Specific** | Có thể mô tả trong 1 câu rõ ràng | Phải giải thích 2-3 phút mới hiểu |
| **Painful enough** | Có pain moment cụ thể (22h đêm, deadline sáng) | Chỉ có "pain chung chung" (khó học) |
| **Operationally visible** | Pain nhìn thấy trong workflow (bug → Google → stress) | Pain chỉ là cảm xúc, không đo được |
| **Reachable** | Có access path rõ (LMS, orientation, TA endorsement) | Không biết làm sao tiếp cận |

**Kết luận**: Segment này PASS tất cả 4 tiêu chí.

---
