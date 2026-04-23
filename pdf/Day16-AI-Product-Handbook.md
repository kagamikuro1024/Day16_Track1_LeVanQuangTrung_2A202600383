---
title: Bạn là Agent đa nhân cách.md؆؆؆
source: Day16-AI-Product-Handbook.pdf
pages: 20
converted_at: 2026-04-23T09:28:15.311201
---

| Khi bạn cần… | Mở phần… |
| --- | --- |
| Hiểu mạch logic tổng thể | §1 |
| Đọc nhanh một khái niệm | §2 |
| Điền template workshop | §3 |
| Chạy AI critique / market sizing | §4 (Prompts) |
| Biết output gì cần có ở mỗi checkpoint | §6 |
| Xem tiêu chí chấm điểm & cách submit | §7 (Rubric & Submission) |
| Chuẩn bị bản nộp cuối buổi | §8 (Final submission) |
| Đọc tham khảo sâu hơn | §10 (References) |

### Day 16 — Sổ tay học viên
### AI Product Strategy & Market Analysis
Builder-to-Product Bridge
### A good AI idea can still become a bad product.
### Một ý tưởng AI đúng xu thế vẫn có thể trở thành một sản phẩm sai.
### 0. Cách dùng sổ tay này
### Đây là tài liệu tham khảo để dùng trong lúc làm workshop, không phải để đọc hết một
### lượt. Mỗi lần team bí ở một mắt xích, hãy mở về đúng phần đó:
### Khi bạn cần… Mở phần…
### Hiểu mạch logic tổng thể §1
### Đọc nhanh một khái niệm §2
### Điền template workshop §3
### Chạy AI critique / market sizing §4 (Prompts)
### Biết output gì cần có ở mỗi checkpoint §6
Xem tiêu chí chấm điểm & cách submit §7 (Rubric & Submission)
### Chuẩn bị bản nộp cuối buổi §8 (Final submission)
### Đọc tham khảo sâu hơn §10 (References)
### Quy ước ngôn ngữ: Tiếng Việt ưu tiên. Các term, công thức, prompt giữ tiếng Anh để
### không lệch nghĩa khi làm việc với AI.
### 1. Mạch logic Day 16

| # | Mắt xích | Câu hỏi cần trả lời | Sản phẩm đầu ra |
| --- | --- | --- | --- |
| 1 | Idea | Insight nào làm ý tưởng xuất hiện? | Idea reframed |
| 2 | Customer | Nên phục vụ ai trước? | Customer / Segment Card |
| 3 | Need | Điều gì đang bị phục vụ chưa tốt? | Need Map (2–3 needs) |
| 4 | Strategy | Nước đi sản phẩm đúng là gì? | Strategy Statement |
| 5 | Moat | Lợi thế nào có thể mạnh dần? | Moat Hypothesis |
| 6 | Market
Size | Thị trường này có đáng để làm
không? | Initial TAM / SAM / SOM
view |

Toàn bộ buổi học đi theo 6 mắt xích. Mỗi mắt xích trả lời một câu hỏi dứt khoát, và chỉ
đi tiếp khi câu hỏi đã có câu trả lời đủ sắc.
Idea (cid:0)(cid:0)(cid:0) Customer (cid:0)(cid:0)(cid:0) Need (cid:0)(cid:0)(cid:0) Strategy (cid:0)(cid:0)(cid:0) Moat (cid:0)(cid:0)(cid:0) Market Size
# Mắt xích Câu hỏi cần trả lời Sản phẩm đầu ra
1 Idea Insight nào làm ý tưởng xuất hiện? Idea reframed
2 Customer Nên phục vụ ai trước? Customer / Segment Card
3 Need Điều gì đang bị phục vụ chưa tốt? Need Map (2–3 needs)
4 Strategy Nước đi sản phẩm đúng là gì? Strategy Statement
5 Moat Lợi thế nào có thể mạnh dần? Moat Hypothesis
Market Thị trường này có đáng để làm Initial TAM / SAM / SOM
6
Size không? view
Nguyên tắc neo suốt buổi:
Respect the idea, but do not trust its first product definition.
Tôn trọng ý tưởng, nhưng đừng vội tin phiên bản định nghĩa sản phẩm đầu tiên của
nó.
2. Các khái niệm chính
2.1 Idea vs. Product definition
Idea = một cảm giác đúng về một khoảng trống, một bất công, hoặc một cơ hội công
nghệ.
Product definition = phiên bản cụ thể đầu tiên mà team nghĩ ra để giải quyết idea đó.
luôn còn sai hoặc còn
Idea có thể đúng, nhưng product definition đầu tiên gần như
thô kiểm tra và nâng cấp
. Day 16 không tạo idea mới — Day 16 product definition.
2.2 Customer Segment — định nghĩa đúng
Một customer segment tốt được định nghĩa bằng job-to-be-done + workflow + pain
moment, chứ không phải bằng một đặc điểm hạ tầng quá rộng.

| Thuộc tính dùng để định nghĩa customer | Có đủ sắc không? |
| --- | --- |
| Loại hình doanh nghiệp (e.g. “SME”) | (cid:0) Quá rộng |
| Đặc điểm hạ tầng sở hữu (e.g. “có kho vận riêng”) | (cid:0) Quá rộng |
| Ngành + workflow lặp lại + pain moment + consequence | (cid:0) Đủ sắc |

| Loại tín hiệu | Ví dụ | Bản chất |
| --- | --- | --- |
| FOMO signal | “Chúng tôi cũng muốn có AI” | Tín hiệu yếu — chỉ mở được cửa
conversation đầu |
| Feature request
trá hình | “Chúng tôi muốn một
chatbot” | Đang nói giải pháp, không phải
pain |
| Real need | “Chúng tôi mất doanh thu khi
bị nhỡ cuộc gọi” | Tín hiệu mạnh — gắn với
business consequence |

Thuộc tính dùng để định nghĩa customer Có đủ sắc không?
Loại hình doanh nghiệp (e.g. “SME”) (cid:0) Quá rộng
Đặc điểm hạ tầng sở hữu (e.g. “có kho vận riêng”) (cid:0) Quá rộng
Ngành + workflow lặp lại + pain moment + consequence (cid:0) Đủ sắc
4 tiêu chuẩn của một early segment tốt:
1. Specific — cụ thể đến mức nhóm khác hình dung được trong một câu
2. Painful enough — có một pain moment lặp lại, rõ ràng
3. Operationally visible — pain nhìn thấy được trong vận hành
4. Reachable — có đường tiếp cận rõ ràng
2.3 Need vs. Feature vs. FOMO signal
Đây là nơi nhiều team nhầm nhất.
Loại tín hiệu Ví dụ Bản chất
Tín hiệu yếu — chỉ mở được cửa
FOMO signal “Chúng tôi cũng muốn có AI”
conversation đầu
Feature request “Chúng tôi muốn một Đang nói giải pháp, không phải
trá hình chatbot” pain
“Chúng tôi mất doanh thu khi Tín hiệu mạnh — gắn với
Real need
bị nhỡ cuộc gọi” business consequence
Quy tắc vàng:
A real need hurts even before AI exists.
vẫn đau ngay cảkhi AI chưa tồn tại
Need thật là thứ .
5 tiêu chuẩn của một need đủ mạnh:
Không phải feature trá hình
Có pain lặp lại (recurring)
Hiện đã có workaround (khách đang giải quyết tạm bợ theo cách nào đó)
Có evidence hoặc proxy evidence (không chỉ dựa vào tưởng tượng của team)
Giải quyết xong sẽ thay đổi một outcome có ý nghĩa về business
2.4 Job-To-Be-Done (JTBD) — công thức viết need

| Loại moat | Cơ chế |
| --- | --- |
| Domain-learning
flywheel | Càng triển khai nhiều trong 1 vertical (cid:0) workflow
understanding càng sâu (cid:0) output càng đúng (cid:0) khách càng
tin (cid:0) càng nhiều triển khai |
| Data compounding | Dữ liệu sử dụng tạo ra dữ liệu tốt hơn cho model riêng của
bạn |
| Workflow embedding | Khi đã được tích hợp vào vận hành thì chi phí chuyển đổi
cao |

Dùng công thức này để ép need rõ hơn, tránh viết need mơ hồ:
When [situation], I want [motivation], so I can [desired outcome].
Situation = tình huống vận hành cụ thể, có thể quan sát được
Motivation = điều khách hàng muốn đạt trong tình huống đó
Desired outcome = kết quả business / operational cuối cùng
2.5 Strategy Statement — công thức
Strategy không phải một danh sách tính năng. Strategy là lựa chọn.
For
[target customer]
who struggle with
[underserved need],
our product helps them
[core outcome]
through
[distinct approach],
unlike
[current alternatives],
because we can leverage
[advantage].
Công thức này buộc team phải trả lời 6 câu hỏi: khách hàng ai, đau gì, ta giúp họ đạt gì,
bằng cách nào, khác alternatives ở đâu, và vì sao ta làm được.
2.6 Moat — lợi thế bền (durable advantage)
Moat = cơ chế làm cho lợi thế của bạn mạnh dần theo thời gian, chứ không phải một
cảm giác “mình giỏi hơn”.
Trong AI products, moat không nên chỉ dựa vào model quality (vì model thay đổi rất
nhanh). Các dạng moat thường bền hơn:
Loại moat Cơ chế
Càng triển khai nhiều trong 1 vertical (cid:0) workflow
Domain-learning
understanding càng sâu (cid:0) output càng đúng (cid:0) khách càng
flywheel
tin (cid:0) càng nhiều triển khai
Dữ liệu sử dụng tạo ra dữ liệu tốt hơn cho model riêng của
Data compounding
bạn
Khi đã được tích hợp vào vận hành thì chi phí chuyển đổi
Workflow embedding
cao

| Distribution/channel | Tiếp cận độc quyền một kênh khó replicate |
| --- | --- |

| Thuật ngữ | Cách hiểu làm việc | Câu hỏi tương ứng |
| --- | --- | --- |
| TAM (Total
Addressable Market) | Tổng không gian thị trường
nếu bài toán được phục vụ
toàn diện | Nếu mọi khách hàng tiềm năng
đều mua, thị trường lớn bao
nhiêu? |
| SAM (Serviceable
Addressable Market) | Phần thị trường phù hợp với
segment và phạm vi hiện tại | Với segment và sản phẩm ta
đang làm, ta có thể phục vụ
được bao nhiêu? |
| SOM (Serviceable
Obtainable Market) | Phần thực tế có thể giành
được trong ngắn hạn | Trong 12–24 tháng tới, ta có thể
chiếm được bao nhiêu? |

Distribution/channel Tiếp cận độc quyền một kênh khó replicate
Durable AI advantage often comes from repeated workflow learning, not just model
quality.
Lợi thế bền trong AI thường đến từ việc học sâu một workflow lặp đi lặp lại, không
chỉ từ chất lượng model.
2.7 TAM / SAM / SOM — market sizing
Thuật ngữ Cách hiểu làm việc Câu hỏi tương ứng
Tổng không gian thị trường Nếu mọi khách hàng tiềm năng
TAM (Total
nếu bài toán được phục vụ đều mua, thị trường lớn bao
Addressable Market)
toàn diện nhiêu?
Với segment và sản phẩm ta
SAM (Serviceable Phần thị trường phù hợp với
đang làm, ta có thể phục vụ
Addressable Market) segment và phạm vi hiện tại
được bao nhiêu?
SOM (Serviceable Phần thực tế có thể giành Trong 12–24 tháng tới, ta có thể
Obtainable Market) được trong ngắn hạn chiếm được bao nhiêu?
Nguyên tắc quan trọng về thời điểm:
chỉcó ý nghĩa sau khi
Market sizing customer, need, và strategy đã sắc hơn. Làm quá
sớm sẽ ra những con số ảo.
Nguyên tắc về chất lượng con số:
Luôn tách facts (có nguồn) ra khỏi assumptions (bạn giả định)
Dùng range khi uncertainty cao, không dùng con số giả chính xác
Nêu rõ unknowns cần research thêm
Mục tiêu không phải ra con số đẹp, mà ra logic ước lượng có thể challenge được
3. Workshop toolkits & templates
4.1 Workshop 1 — Customer / Segment Card
Thời lượng: 40 phút
Câu hỏi chính: Who should this idea serve first? / Ý tưởng này nên phục vụ ai trước?

Template (điền cho 1 segment):
Segment name : ________________________________________
Operational context : ________________________________________
(bối cảnh vận hành)
Recurring workflow : ________________________________________
(workflow lặp lại)
Pain moment : ________________________________________
(thời điểm đau nhất trong workflow đó)
Why now : ________________________________________
(vì sao đáng làm lúc này, không phải 2 năm trước hay 2 năm sau)
Access path : ________________________________________
(đường tiếp cận thực tế tới nhóm này)
Quality test: Can another team picture this customer in one sentence?
4.2 Workshop 2 — Need Map
Thời lượng: 40 phút
Câu hỏi chính: What real pain exists here, even before AI? / Nỗi đau thật ở đây là gì, ngay cả
trước khi có AI?
Mục tiêu: Giữ lại 2–3 needs đủ mạnh.
Template (điền cho mỗi need ưu tiên):
Need #___
Need statement : ________________________________________
(viết theo JTBD: When..., I want..., so I can...)
Current workaround : ________________________________________
(khách hàng đang giải quyết tạm bằng cách nào?)
Pain signal : ________________________________________

(mất thời gian? mất tiền? mất cơ hội? stress vận hành?)
Evidence (or proxy) : ________________________________________
(bằng chứng trực tiếp hoặc gián tiếp — không được bịa)
Why underserved : ________________________________________
(vì sao thị trường hiện tại đang phục vụ nó chưa tốt?)
4.3 Workshop 3 — Strategy Statement + Moat
Thời lượng: 35 phút
Câu hỏi chính: Given this customer and need, what is the right product move?
Template strategy statement (giữ tiếng Anh để AI xử lý ổn định):
For _______________________________________________
[target customer]
who struggle with __________________________________
[underserved need]
our product helps them _____________________________
[core outcome]
through ____________________________________________
[distinct approach]
unlike _____________________________________________
[current alternatives]
because we can leverage ____________________________
[advantage].
Template moat hypothesis:
Our moat mechanism is: ______________________________
(ví dụ: domain-learning flywheel, data compounding, workflow embedding...)
If we deploy 50 times in the same vertical,

the following things get systematically better:
1. __________________________________________________
2. __________________________________________________
3. __________________________________________________
Why competitors cannot easily replicate this:
_____________________________________________________
Template positioning note (2 câu):
Câu 1 (what you are):
_____________________________________________________
Câu 2 (what you are not / not yet):
_____________________________________________________
4. Prompts cho Vibe Coding (English-only)
Lưu ý: giữtiếng Anh 100%
Tất cả prompt dưới đây . Lý do: khi critique cấu trúc logic
hoặc ước lượng thị trường, AI giữ ngữ nghĩa ổn định hơn với tiếng Anh. Sau khi có kết
quả, team có thể thảo luận bằng tiếng Việt.
5.1 Structured Critique Prompt
Dùng sau khi đã có Customer Card + Need Map + Strategy Statement + Moat Hypothesis
nháp. Mục tiêu: AI chỉ ra chỗ yếu, không viết hộ.
Review this Day 16 draft.
For each issue, return:
1. issue name
2. evidence from the draft
3. why it is weak
4. rewrite suggestion
Check these 5 issues:
- customer too broad
- need is actually a solution

- lack of evidence
- strategy too generic
- moat too weak
Important:
Do not add imaginary facts.
Draft:
[paste idea + customer + needs + strategy + moat here]
Cách dùng:
1. Paste toàn bộ draft của team vào cuối prompt
2. Chạy prompt
3. Với mỗi issue AI chỉ ra, team quyết định: accept (sửa theo), reject (giữ nguyên, có
lý do), hay partial (sửa một phần)
4. Quan trọng: Team phải tự viết lại, không copy-paste câu rewrite của AI nguyên văn
5.2 TAM / SAM / SOM Prompt
Dùng sau khi đã chạy critique và có version 2 của product logic.
You are helping an early-stage AI product team estimate market potential.
Based on the following inputs:
- target customer segment
- underserved need
- product strategy
- geography
- pricing logic if available
Please produce:
1. a TAM estimate with explicit assumptions
2. a SAM estimate for the chosen segment and scope
3. a SOM estimate for a realistic near-term capture
4. key unknowns that require further research
5. a final judgment: is this market worth pursuing now?
Important rules:
- do not invent precise numbers without assumptions
- show the estimation logic clearly

- use ranges when uncertainty is high
- separate facts from assumptions
Inputs:
[paste your customer + need + strategy + geography + pricing here]
Output tối thiểu team cần có:
TAM: range + logic
SAM: con số hoặc range + logic
SOM: con số realistic + assumption chính
Top 3 unknowns cần research thêm
Judgment: “worth pursuing now” / “worth pursuing but not now” / “not worth
pursuing as framed”
5.3 Prompt cho các task bổ sung (optional)
Rewrite need theo JTBD:
Rewrite the following need using the JTBD formula:
"When [situation], I want [motivation], so I can [desired outcome]."
Make the situation concrete and observable.
Make the outcome a business or operational consequence.
Do not add assumptions not present in the original.
Original need:
[paste need here]
So sánh 2 segment alternatives:
Compare these two candidate customer segments for an early-stage AI product.
For each, score 1–5 on:
- specificity
- pain intensity
- operational visibility
- reachability
- packaging feasibility

| (cid:0) Use AI to | (cid:0) Do NOT use AI to |
| --- | --- |
| summarize | invent customer facts |
| critique | invent evidence |
| compare options | decide strategy for you |
| rewrite more clearly | produce polished nonsense |
| estimate with explicit assumptions | generate precise numbers without logic |

Then recommend which one to pursue first and explain the trade-off.
Segment A: [...]
Segment B: [...]
5. Vibe Coding rules
(cid:0) Use AI to (cid:0) Do NOT use AI to
summarize invent customer facts
critique invent evidence
compare options decide strategy for you
rewrite more clearly produce polished nonsense
estimate with explicit assumptions generate precise numbers without logic
3 rule bắt buộc:
1. Facts vs assumptions vs unknowns — mọi output của AI phải tách rõ ba thứ này
2. Team ownership — mọi câu trong bản submit cuối phải được team hiểu và bảo vệ
được, dù nó do AI gợi ý
3. No polished nonsense — câu nghe hay mà không có logic đằng sau thì loại
6. Checkpoints — Output yêu cầu
Day 16 có 2 checkpoint giữa buổi + 1 final checklist cuối buổi. Mỗi checkpoint là một
cổng: không pass thì không đi tiếp.
6.1 Checkpoint 1 — Segment Review Gate
Khi nào: Sau Workshop 1 (sau khi có Customer / Segment Card)
Mục tiêu: Khóa chất lượng segment trước khi đi vào need.
Output cần có:
1 Customer / Segment Card đã điền đầy đủ 6 ô
Segment đã vượt qua 4 tiêu chuẩn: specific, painful enough, operationally visible,
reachable

| (cid:0) PASS | (cid:0) FAIL |
| --- | --- |
| Nhóm khác đọc 1 câu là hình dung được
customer | Phải giải thích 2–3 phút mới hình
dung ra |
| Có pain moment cụ thể | Chỉ có “pain chung chung” |
| Có access path rõ | Không biết tiếp cận bằng kênh nào |
| Team tự tin với kill question | Team lảng tránh kill question |

| (cid:0) PASS | (cid:0) FAIL |
| --- | --- |
| Need hurts even before AI exists | Need chỉ tồn tại vì “AI đang là trend” |
| Có workaround hiện tại rõ | Không ai trong thị trường đang giải quyết nó theo
cách nào |

Kill question:
If you could keep only one customer for the first 6 months, would you still keep this
one?
Nếu chỉ được giữ một nhóm khách hàng trong 6 tháng đầu, nhóm này có còn là lựa
chọn không?
Pass / Fail signals:
(cid:0) PASS (cid:0) FAIL
Nhóm khác đọc 1 câu là hình dung được Phải giải thích 2–3 phút mới hình
customer dung ra
Có pain moment cụ thể Chỉ có “pain chung chung”
Có access path rõ Không biết tiếp cận bằng kênh nào
Team tự tin với kill question Team lảng tránh kill question
6.2 Checkpoint 2 — Need Review Gate
Khi nào: Sau Workshop 2 (sau khi có Need Map)
Mục tiêu: Loại need giả / need yếu. Chỉ giữ 2–3 needs đủ mạnh.
Output cần có:
Need Map với 2–3 needs (không nhiều hơn)
Mỗi need có đủ: statement (JTBD) + workaround + pain signal + evidence + why
underserved
Kill question:
If this need is solved well, what clearly changes in the business?
Nếu need này được giải quyết tốt, điều gì thay đổi rõ nhất về mặt kinh doanh?
Pass / Fail signals:
(cid:0) PASS (cid:0) FAIL
Need hurts even before AI exists Need chỉ tồn tại vì “AI đang là trend”
Không ai trong thị trường đang giải quyết nó theo
Có workaround hiện tại rõ
cách nào

| Có evidence hoặc proxy
evidence | Dựa 100% vào tưởng tượng của team |
| --- | --- |
| Giải quyết xong thay đổi
outcome rõ | “Giải quyết xong thì khách hàng vui hơn” (không đo
được) |

|  | Phiên bản A — End-of-session | Phiên bản B — BTVN |
| --- | --- | --- |
| Nộp khi
nào | Cuối buổi sáng Day 16 (trước
13:00) | Trước 23:59 cùng ngày Day 16 |
| Nộp ở
đâu | Submit trực tiếp trên LMS | Submit link public GitHub lên LMS |
| Bao gồm | Bản nháp Day 16 Package đã
qua AI critique | Bản hoàn chỉnh hơn trong
submission.md trên GitHub |

Có evidence hoặc proxy
Dựa 100% vào tưởng tượng của team
evidence
Giải quyết xong thay đổi “Giải quyết xong thì khách hàng vui hơn” (không đo
outcome rõ được)
6.3 Final Checkpoint — Day 16 Package Checklist
Khi nào: Cuối buổi (trước 13:00)
Mục tiêu: Khóa toàn bộ Day 16 package để sang Day 17.
[ ] 1. Idea reframed as a product opportunity
[ ] 2. A sharp customer / segment card
[ ] 3. 2–3 underserved needs with evidence or proxy evidence
[ ] 4. 1 strategy statement (theo đúng formula 6 dòng)
[ ] 5. 1 moat hypothesis (có cơ chế, không chỉ là cảm giác)
[ ] 6. 1 initial TAM / SAM / SOM view with assumptions
[ ] 7. 1 short positioning note (2 câu)
Ngưỡng tối thiểu: Nếu các phần này còn yếu, Day 17 sẽ rất khó đi tiếp.
7. Rubric & Submission
7.1 Cách nộp bài — 2 phiên bản bắt buộc
Day 16 yêu cầu 2 lần submit riêng biệt, đều là cá nhân (không theo nhóm):
Phiên bản A — End-of-session Phiên bản B — BTVN
Nộp khi Cuối buổi sáng Day 16 (trước
Trước 23:59 cùng ngày Day 16
nào 13:00)
Nộp ở
Submit trực tiếp trên LMS Submit link public GitHub lên LMS
đâu
Bản nháp Day 16 Package đã Bản hoàn chỉnh hơn trong
Bao gồm
qua AI critique submission.md trên GitHub

| Mục
đích | Snapshot tư duy tại thời điểm
kết thúc buổi học | Bản làm tốt nhất sau khi có thêm thời
gian suy nghĩ |
| --- | --- | --- |

Mục Snapshot tư duy tại thời điểm Bản làm tốt nhất sau khi có thêm thời
đích kết thúc buổi học gian suy nghĩ
Lưu ý quan trọng:
Phiên bản A là bắt buộc — không có A thì không chấm được tiêu
chí so sánh A(cid:0)B. Nộp muộn hoặc thiếu A sẽ ảnh hưởng trực tiếp đến điểm.
7.2 Rubric — 100 điểm, 5 tiêu chí
Bài được chấm trên cả 2 phiên bản. Không tiêu chí nào chỉ chấm một phiên bản duy
nhất.
Tiêu chí 1 — Product Judgment (35 điểm)
Đây là tiêu chí quan trọng nhất, chiếm trọng số lớn nhất.
Chấm mức độ sắc bén của 4 mắt xích cốt lõi: Customer / Segment, Need, Strategy, Moat.
Một bài điểm cao ở tiêu chí này phải cho thấy được: customer cụ thể đến mức hình dung
được trong 1 câu, need gắn với business consequence thực tế (không phải FOMO AI),
strategy có lựa chọn rõ ràng (không phải danh sách tính năng), và moat có cơ chế có thể
mạnh dần (không chỉ là cảm giác).
Chấm chủ yếu ở phiên bản B, đối chiếu với A.
Tiêu chí 2 — Market Awareness (15 điểm)
Chấm khả năng ước lượng thị trường có trách nhiệm: không bịa số, biết phân biệt
facts và assumptions, biết đặt tên cho những điều chưa biết (unknowns), và đưa ra được
judgment “thị trường này có đáng để theo đuổi không” — kể cả khi câu trả lời là chưa.
Chấm ở phiên bản B.
Tiêu chí 3 — Research Rigor (15 điểm)
Chấm cách học viên làm việc với AI và với thông tin: có tỉnh táo khi dùng AI không
(không copy-paste nguyên block), có proxy evidence thực tế không, có phân biệt được
điều mình biết thật vs điều mình đang giả định không. Tiêu chí này không thưởng viết
nhiều — thưởng tỉnh táo.
Chấm ở cả A và B.

| Band | Điểm | Ý nghĩa |
| --- | --- | --- |
| Outstanding | 90–
100 | Output vượt template — không chỉ điền đúng, mà cho thấy
insight riêng vượt ra ngoài khuôn hướng dẫn sẵn |
| Strong | 75–89 | Đủ chất để đi tiếp Day 17 ngay |
| Pass | 60–74 | Đi tiếp được nhưng cần revisit ít nhất 1 mắt xích |
| Needs
rework | 40–59 | Cần làm lại customer / need trước Day 17 |
| Fail | <40 | Chưa đạt minimum bar của Day 16 |

Tiêu chí 4 — Story Consistency (15 điểm)
Chấm mức độ nhất quán của toàn bộ Day 16 Package: Customer (cid:0) Need (cid:0) Strategy (cid:0)
Moat (cid:0) Market phải là một câu chuyện liên kết, không phải các phần điền rời nhau. Học
viên có thể viết rất đầy đủ từng phần mà vẫn bị điểm thấp ở tiêu chí này nếu các phần
không khớp nhau.
Chấm chủ yếu ở phiên bản B.
Tiêu chí 5 — Iteration Quality (20 điểm)
Chấm mức độ cải thiện thực sự giữa A và B: B có tốt hơn A không, tốt hơn ở chỗ nào,
và học viên có thể giải thích được vì sao không. Tiêu chí này thưởng người dám sửa —
bao gồm cả việc pivot sang customer hoặc need khác sau khi nhận ra cái cũ còn yếu.
Điểm cao nhất dành cho những bài B vượt hẳn kỳ vọng so với A, kèm reflection honest về
quá trình thay đổi.
Chấm bằng cách so sánh trực tiếp A vs B.
7.3 Grade bands
Band Điểm Ý nghĩa
90– Output vượt template — không chỉ điền đúng, mà cho thấy
Outstanding
100 insight riêng vượt ra ngoài khuôn hướng dẫn sẵn
Strong 75–89 Đủ chất để đi tiếp Day 17 ngay
Pass 60–74 Đi tiếp được nhưng cần revisit ít nhất 1 mắt xích
Needs
40–59 Cần làm lại customer / need trước Day 17
rework
Fail <40 Chưa đạt minimum bar của Day 16
7.4 Một vài lưu ý khi làm bài
Viết ít nhưng đúng tốt hơn viết nhiều nhưng mơ hồ. Rubric không chấm độ dài.
Phiên bản A là snapshot thật của bạn tại thời điểm cuối buổi. Đừng chỉnh A
sau khi đã nộp — A được dùng để đo mức độ cải thiện sang B.
GitHub repo phải public khi nộp. Nếu repo không truy cập được lúc chấm, bài sẽ
không được chấm phần BTVN.

AI là công cụ hỗ trợ, không phải người nộp bài. Mọi nội dung trong submission
phải là thứ bạn hiểu và bảo vệ được bằng lời nói.
8. Final submission — Day 16 Package
Đây là bản nộp cuối buổi cho assignment. Copy template dưới đây, điền đầy đủ, và
submit.
# Day 16 Submission — Team [tên team]
## Members
- [tên + vai trò]
- [tên + vai trò]
- [tên + vai trò]
---
## 1. Idea reframed
Original idea:
> [mô tả ý tưởng ban đầu của team, 1–2 câu]
Reframed as a product opportunity:
> [diễn giải lại như một cơ hội sản phẩm, nêu rõ observed gap và founding belief, 3–4 câ
---
## 2. Customer / Segment Card
- **Segment name:** [...]
- **Operational context:** [...]
- **Recurring workflow:** [...]
- **Pain moment:** [...]
- **Why now:** [...]
- **Access path:** [...]
One-sentence description:
> [một câu mô tả customer để nhóm khác hình dung được]

---
## 3. Need Map (2–3 needs)
### Need #1 (priority)
- **Statement (JTBD):** When [...], I want [...], so I can [...].
- **Current workaround:** [...]
- **Pain signal:** [...]
- **Evidence / proxy evidence:** [...]
- **Why underserved:** [...]
### Need #2
- **Statement (JTBD):** [...]
- **Current workaround:** [...]
- **Pain signal:** [...]
- **Evidence / proxy evidence:** [...]
- **Why underserved:** [...]
### Need #3 (optional)
- **Statement (JTBD):** [...]
- **Current workaround:** [...]
- **Pain signal:** [...]
- **Evidence / proxy evidence:** [...]
- **Why underserved:** [...]
---
## 4. Strategy Statement
For [target customer]
who struggle with [underserved need],
our product helps them [core outcome]
through [distinct approach],
unlike [current alternatives],
because we can leverage [advantage].
---
## 5. Moat Hypothesis

**Moat mechanism:** [e.g. domain-learning flywheel]
If we deploy [N] times in [vertical/context], the following improve:
1. [...]
2. [...]
3. [...]
Why competitors cannot easily replicate this:
> [...]
---
## 6. Initial TAM / SAM / SOM view
| Layer | Estimate | Key assumptions | Confidence |
|---|---|---|---|
| TAM | [range, e.g. $X–$Y M/year] | [...] | low / med / high |
| SAM | [range] | [...] | low / med / high |
| SOM | [12–24mo target] | [...] | low / med / high |
**Top 3 unknowns requiring further research:**
1. [...]
2. [...]
3. [...]
**Judgment:**
- [ ] Worth pursuing now
- [ ] Worth pursuing but not now (need to validate [...] first)
- [ ] Not worth pursuing as currently framed
---
## 7. Positioning Note (2 sentences)
**What we are:**
> [1 câu]
**What we are not / not yet:**
> [1 câu]

---
## 8. Self-assessment before Day 17
Trong 6 mắt xích (Idea (cid:0) Customer (cid:0) Need (cid:0) Strategy (cid:0) Moat (cid:0) Market Size), mắt xích nà
> [trả lời thật — đây là input quan trọng cho Day 17]
Open questions chúng tôi muốn khám phá thêm ở Day 17:
1. [...]
2. [...]
3. [...]
9. Bridge to Day 17
Day 16 đã trả lời:
Real opportunity đằng sau idea là gì?
Ai là early customer?
Need thật là gì?
Product move đúng là gì?
Moat nào có thể compound?
Thị trường có đáng để theo đuổi không?
Day 17 sẽ trả lời:
What exactly do we build first? (MVP scope)
Viết PRD thế nào?
Assumption nào cần validate trước tiên?
Experiment nào chạy trong 2 tuần đầu?
10. References
Core readings
1. The Lean Product Playbook — Dan Olsen.
https://leanproductplaybook.com/
Gốc của Lean Product thinking (Problem Space vs Solution Space, Product-Market
Fit Pyramid).

| Lúc nào nhớ câu nào |
| --- |
| “Respect the idea, but do not trust its first product definition.” |
| “Interest is not willingness to pay.” |
| “FOMO AI is not a need.” |
| “A real need hurts even before AI exists.” |
| “Do not sell a tool people must configure; sell a result people can use.” |
| “Durable advantage comes from repeated workflow learning.” |
| “Market sizing is meaningful only after product logic becomes sharper.” |

2. TAM, SAM, and SOM: Made Simple for Growing Businesses — Salesforce.
https://www.salesforce.com/blog/tam-sam-som/
Giới thiệu cơ bản và dễ hiểu về market sizing.
Further reading (optional, nếu team muốn đào sâu hơn)
3. Jobs to Be Done: Theory to Practice — Anthony W. Ulwick.
Kinh điển về JTBD framework.
4. The Mom Test — Rob Fitzpatrick.
Cách phỏng vấn khách hàng mà không bị “mom answer” làm lệch kết quả. Rất liên
quan đến phần evidence vs proxy evidence.
5. 7 Powers: The Foundations of Business Strategy — Hamilton Helmer.
Phân tích 7 loại moat (Scale Economies, Network Economies, Counter-Positioning,
Switching Costs, Branding, Cornered Resource, Process Power).
6. Competing Against Luck — Clayton Christensen.
Case-driven, giải thích JTBD qua nhiều ví dụ đời thực.
Quick reference — các câu chốt Day 16
Lúc nào nhớ câu nào
“Respect the idea, but do not trust its first product definition.”
“Interest is not willingness to pay.”
“FOMO AI is not a need.”
“A real need hurts even before AI exists.”
“Do not sell a tool people must configure; sell a result people can use.”
“Durable advantage comes from repeated workflow learning.”
“Market sizing is meaningful only after product logic becomes sharper.”
Chúc các bạn có một Day 16 đầy tension tốt và những câu hỏi đúng.

