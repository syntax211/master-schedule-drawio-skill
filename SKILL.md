---
name: master-schedule-drawio
description: Vẽ bảng tiến độ tổng thể dự án (Master Schedule / Gantt chart dạng bảng) trên draw.io (app.diagrams.net), gọn trong 1 trang khổ A3 ngang, có thanh timeline header + footer, các lane theo bên liên quan (Employer/Engineer/Contractor/Design Consultant), bar-chart công việc với nhãn ngày bắt đầu/kết thúc, connector nối đúng critical path (đỏ) và liên kết phụ (xám nét đứt), mốc milestone (chấm tròn đen), đường data date (ngày cập nhật hiện tại), và thanh actual progress (tiến độ thực tế). Dùng skill này bất cứ khi nào người dùng yêu cầu "vẽ bảng tiến độ", "master schedule", "Gantt chart", "tiến độ tổng thể dự án", "timeline dự án" trên draw.io/diagrams.net, kể cả khi họ chỉ nói "vẽ tiến độ" mà không nhắc rõ từng chi tiết trên. Áp dụng cho MỌI dự án bất kỳ (xây dựng, thiết kế, CNTT...) miễn người dùng cung cấp đủ hoặc xác nhận các thông tin ở bước hỏi-xác nhận bên dưới — KHÔNG tự vẽ khi thông tin chưa được người dùng xác nhận.
---

# Master Schedule trên draw.io (1 trang A3 ngang)

Skill này dựng bảng tiến độ tổng thể (Gantt dạng bảng, không dùng plugin Gantt có sẵn của draw.io) bằng cách vẽ trực tiếp các hình chữ nhật/hình elip + connector thật của draw.io, theo đúng quy trình đã kiểm chứng: khung lưới cố định (khoá), bar-chart công việc và milestone (mở khoá để người dùng tự kéo cập nhật sau này).

**Nguyên tắc bắt buộc: KHÔNG bao giờ vẽ ngay.** Luôn đi qua bước "Thu thập & xác nhận thông tin" trước, trình bày lại tóm tắt cho người dùng duyệt, chỉ vẽ sau khi họ xác nhận (hoặc sửa rồi xác nhận). Nếu người dùng cung cấp thiếu, gợi ý phương án hợp lý (dựa vào loại dự án, độ dài, ngày hôm nay) rồi hỏi lại — không đoán và vẽ luôn.

## Quy trình tổng quan

1. Thu thập & xác nhận thông tin dự án (bước bắt buộc, xem mục A)
2. Thu thập & xác nhận cấu trúc timeline (mục B)
3. Thu thập & xác nhận các bên liên quan + đầu việc chính (mục C)
4. Tính toán lưới toạ độ (mục D, dùng `scripts/timeline_x.py`)
5. Dựng XML draw.io theo layer: khung → timeline → lane label → task bar → milestone → connector → data date line → actual progress (mục E, F, G)
6. Gọi `mcp__draw_io__create_diagram` (tạo mới) hoặc yêu cầu người dùng dán vào **Extras → Edit Diagram** nếu họ đưa link file Drive riêng (skill này KHÔNG đọc/ghi trực tiếp vào file Drive của người dùng — xem mục H)

---

## A. Thu thập & xác nhận thông tin dự án

Hỏi (hoặc trích từ nội dung người dùng đã cung cấp trong hội thoại) các mục sau. Nếu thiếu, đề xuất giá trị hợp lý rồi hỏi xác nhận:

- Tên dự án (tiếng Việt/tiếng Anh song ngữ nếu người dùng dùng song ngữ)
- Vị trí/địa điểm dự án
- Chủ đầu tư / Client
- Ngày bắt đầu dự án, ngày hoàn thành dự kiến, tổng thời gian (số tháng) — nếu người dùng chỉ cho ngày đầu/cuối, tự tính số tháng và xác nhận lại
- Revision hiện tại (vd Rev_1, Baseline, Rev_6.1...) và có phải bản cập nhật so với baseline trước không

Trình bày lại dạng tóm tắt ngắn (bảng hoặc gạch đầu dòng) và hỏi "Đúng chưa?" trước khi qua bước B.

## B. Thu thập & xác nhận cấu trúc timeline

Bảng có **2 thanh timeline**: một ở đầu bảng (ngay dưới tiêu đề, phía trên hàng Project Milestone) và một lặp lại ở cuối bảng (dưới lane cuối cùng) để dò mốc khi nhìn nửa dưới. Cả hai đều gồm 3 hàng con: **Năm** → **Tháng** → **thang chi tiết** (5 ngày/tuần hoặc gộp theo tháng).

Hỏi người dùng:
- Khoảng thời gian tổng của bảng (từ tháng/năm nào đến tháng/năm nào)
- **Những tháng nào cần chia theo 5 ngày/tuần** (thường là các tháng có nhiều mốc/công việc ngắn, sát ngày hiện tại hoặc đầu-cuối dự án) — mỗi tháng chia 6 cột (5/10/15/20/25/30)
- **Những tháng nào chỉ cần gộp theo tháng** (giai đoạn thi công dài, ít mốc chi tiết) — gộp thành 1 cột hẹp (~18-70px tuỳ tổng chiều rộng còn lại) ghi "Jan/Feb/Mar..." hoặc nhãn "Monthly scale"
- Milestone nào cần thể hiện ở hàng "Project Milestone" trên cùng (mỗi milestone = **chấm tròn đen đặc**, kèm nhãn text ghi rõ **tên công việc + ngày**, đặt cạnh chấm; nếu nhiều mốc gần nhau, so le 2-3 tầng để không đè chữ)

Nếu người dùng không phân biệt rõ, đề xuất mặc định: các tháng đầu (3-4 tháng đầu dự án) và 3-4 tháng cuối dùng thang 5-ngày (vì đó là giai đoạn hay có nhiều mốc/thủ tục ngắn), khoảng giữa dùng thang tháng — rồi hỏi xác nhận.

## C. Thu thập & xác nhận các bên liên quan + đầu việc chính

4 lane chuẩn (đổi tên theo dự án thực tế nếu người dùng cho tên khác):

- **PROJECT MILESTONE** — hàng tổng hợp mốc, không phải "bên" nào cả
- **THE EMPLOYER / CHỦ ĐẦU TƯ** — vd: Ký hợp đồng tư vấn, công tác pháp lý (Authority Permits/giấy phép), phê duyệt, tạm ứng (Advance Payment), các mốc phải chờ chủ đầu tư ra quyết định
- **THE ENGINEER / TƯ VẤN QUẢN LÝ DỰ ÁN (PPMV/PM)** — vd: ký hợp đồng với CĐT, Quản lý thiết kế, Quản lý đấu thầu (Tender Management), Giám sát thi công (Construction Supervision)
- **THE DESIGN CONSULTANT / TƯ VẤN THIẾT KẾ** — vd: thiết kế cơ sở, thiết kế kỹ thuật, thiết kế thi công, nội thất/cảnh quan
- **THE CONTRACTOR / NHÀ THẦU** — vd: huy động & chuẩn bị (Mobilization), công tác cọc (Pile test), công tác móng, xây dựng chính, nghiệm thu, bàn giao từng phần (Partial Handover), khắc phục tồn tại (Rectification), bàn giao cuối (Final Handover)

Với mỗi lane, hỏi hoặc gợi ý danh sách đầu việc chính kèm ngày bắt đầu/kết thúc (hoặc 1 ngày nếu là milestone). Việc nào là **chuỗi găng (critical path)** — chuỗi công việc quyết định ngày hoàn thành dự án — cần người dùng xác nhận rõ, vì đây là chuỗi sẽ tô đỏ và nối bằng connector nét liền.

Xác nhận lại toàn bộ danh sách công việc theo bên trước khi vẽ.

## D. Tính toán lưới toạ độ

Dùng `scripts/timeline_x.py` để tính x-pixel cho một ngày bất kỳ, tránh tính tay sai số (đây là lỗi hay gặp nhất khi làm thủ công). Cách dùng:

```bash
python3 scripts/timeline_x.py --config timeline_config.json --date 2027-05-03
```

`timeline_config.json` mô tả các đoạn theo thứ tự trái→phải, mỗi đoạn có `type` (`weekly` = chia 5 ngày, `monthly` = gộp cả tháng), `start` (ngày bắt đầu đoạn, dạng YYYY-MM-DD), `x_start` (toạ độ x bắt đầu đoạn), và `unit_width` (bề rộng 1 đơn vị: với `weekly` là bề rộng 1 mốc-5-ngày ~60-70px; với `monthly` là bề rộng 1 tháng gộp ~18-70px tuỳ độ dài dải monthly). Xem `references/xml_patterns.md` mục "Cấu hình timeline_config.json mẫu" để lấy file mẫu đúng theo case đã làm (Rev_6.1: Sep-Dec 2026 weekly, Jan-Aug 2027 monthly, Sep-Dec 2027 weekly).

Nếu không chạy được script (không có Python), tính tay theo công thức:
- Đoạn `weekly`: `x = x_start + floor((day-1)/5)*unit_width + ((day-1)%5)/5*unit_width` (xấp xỉ tuyến tính trong tháng, ngày 1-5 ở cột đầu, 6-10 cột 2, v.v., ngày 30/31 có thể lấn nhẹ vào cột 6)
- Đoạn `monthly`: `x = x_start + (month_index)*unit_width + (day/days_in_month)*unit_width`

Ghi lại toạ độ x tính được cho **mọi** điểm bắt đầu/kết thúc của mọi bar-chart và milestone trước khi viết XML, để tránh vẽ sai lệch ngày.

## E. Cấu trúc khung A3 (khoá cứng — locked)

Trang draw.io: `pageWidth="1169" pageHeight="826"` (khổ A3 ngang ở 96dpi, giữ tỉ lệ in vừa 1 trang khi Page Setup chọn A3 Landscape + Fit to page). Toàn bộ nội dung phải nằm trong `x: 10-1158, y: 6-816`.

Các phần tử khung (LUÔN có `locked=1` trong `style`, để người dùng không kéo nhầm khi họ tự sửa file sau này):

- Tiêu đề dự án + subtitle (tên, rev, vị trí, chủ đầu tư)
- Color legend (chip màu cho từng bên + "Critical Path" + "Milestone" + "Actual progress" + "Data date")
- Cột sọc nền xen kẽ (fillColor `#f5f5f5`/trong suốt) chạy dọc toàn bộ chiều cao thân bảng, để dò cột khi mắt lướt ngang
- Thanh timeline **header**: hàng Năm → hàng Tháng → hàng thang chi tiết (5-ngày/monthly), đúng theo mục B
- **Nhãn lane** bên trái mỗi hàng bên liên quan: dùng **hình chữ nhật thường** (`rounded=0;html=1;whiteSpace=wrap;align=center;verticalAlign=middle`), **KHÔNG dùng `swimlane`/container** — vì container khi khoá sẽ khoá luôn các task bar nằm bên trong nó, khiến người dùng không kéo cập nhật được. Chữ đọc ngang bình thường, tự xuống dòng trong ô rộng ~130px.
- Đường phân cách mảnh (`fillColor=#999999`, cao 2px) giữa các lane
- Thanh timeline **footer**: lặp lại cấu trúc header, đặt ngay dưới lane cuối cùng

## F. Task bar, milestone, connector (mở khoá — người dùng tự kéo sau)

- **Bar-chart công việc**: hình chữ nhật bo góc (`rounded=1;whiteSpace=wrap`), màu theo bên (xem bảng màu mục G), width = (x kết thúc − x bắt đầu) tính từ mục D. **Không** đặt `locked=1`.
- **Milestone 1 ngày**: hình tròn đặc (`ellipse;fillColor=<màu bên>;strokeColor=<màu đậm hơn>`), không phải hình chữ nhật — vì milestone không có độ dài. Nhãn tên+ngày đặt cạnh (không đè lên chấm).
- **Nhãn ngày bắt đầu/kết thúc**: với MỌI bar-chart có độ dài (không áp dụng cho milestone 1-ngày vì ngày đã có trong nhãn cạnh chấm), thêm 2 ô text nhỏ (`fontSize=5-6;fontStyle=1` — **in đậm**) ngay sát mép dưới thanh (không để khoảng trắng, `y` = đáy thanh, `verticalAlign=top`): một căn trái (`align=left`) ở đầu thanh ghi ngày bắt đầu, một căn phải (`align=right`) ở cuối thanh ghi ngày kết thúc.
- **Connector**: dùng edge thật của draw.io (`edge="1"`, có `source`/`target` trỏ đúng id ô), **không** vẽ đường tự do. Luôn set rõ điểm neo bằng `exitX/exitY` và `entryX/entryY` (0=trái/trên, 1=phải/dưới, 0.5=giữa) để đường nối bám vào **đúng đầu hoặc cuối** thanh — never để draw.io tự chọn điểm giữa cạnh một cách ngẫu nhiên. Ví dụ nối 2 task nối tiếp: `exitX=1;exitY=0.5` (giữa cạnh phải của task trước) → `entryX=0;entryY=0.5` (giữa cạnh trái của task sau). Nối task → milestone phía trên: `exitX=0.5;exitY=0` → `entryX=0.5;entryY=1`.
- **Critical path**: chuỗi việc quyết định ngày hoàn thành dự án (đã xác nhận ở mục C) — connector nối chuỗi này màu đỏ (`strokeColor=#b85450` hoặc đỏ đậm hơn), **nét liền**, `strokeWidth=2-3`. Các liên kết phụ khác: xám (`strokeColor=#999999`), **nét đứt** (`dashed=1`), `strokeWidth` mảnh hơn.
- **Style `edgeStyle=orthogonalEdgeStyle;rounded=1`** cho mọi connector để đường đi vuông góc, dễ nhìn khi cắt qua ô khác (không dùng đường cong tự do).

## G. Bảng màu theo bên (mặc định, có thể đổi theo yêu cầu người dùng)

| Bên | fillColor | strokeColor | fontColor (chữ trong bar) |
|---|---|---|---|
| Employer/Chủ đầu tư | `#f8cecc` | `#b85450` | `#a02020` |
| Engineer/PM | `#dae8fc` | `#6c8ebf` | `#1a3e73` |
| Design Consultant | `#d5e8d4` | `#82b366` | `#14591f` |
| Contractor/Nhà thầu | `#e1d5e7` | `#9673a6` | `#4a2578` |
| Việc đã hoàn thành/info | `#f5f5f5` | `#999999` | `#666666` |
| Cảnh báo/mốc "?" chưa chắc | `#fff0f0`, viền đỏ nét đứt | `#b85450` | `#a02020` |

## H. Data date (đường cập nhật tiến độ) & Actual progress

Khi người dùng yêu cầu "cập nhật tiến độ đến ngày X" (mặc định: ngày hôm nay nếu không nói rõ):

1. Tính x-pixel của ngày đó (mục D). Vẽ **1 đường thẳng đứng màu đỏ** (`fillColor=#ff0000`, width 2px) chạy suốt từ đỉnh thanh timeline header đến đáy thanh timeline footer — xuyên qua toàn bộ bảng, không chỉ phần thân. Gắn nhãn "TODAY <ngày>" hoặc "DATA DATE <ngày>" gần đường này, `locked=1` (đường này là mốc tham chiếu tĩnh, không phải task).
2. Với mỗi task đang thi công (có % hoàn thành thực tế do người dùng cung cấp), vẽ thêm **1 hình chữ nhật màu xám đậm/tối màu hơn thanh gốc** (`fillColor=#3d5f8a` hoặc tối hơn màu bên tương ứng), đè lên phần đầu của thanh task gốc, bắt đầu từ mép trái thanh, **kết thúc đúng tại đường data date** (không phải kết thúc tuỳ ý theo %) — vì actual progress trong Gantt chuẩn thể hiện tiến độ thực tế tính đến ngày cập nhật.
3. Ghi nhãn **% hoàn thành ngay sau (bên phải) mép cuối của đoạn actual-progress đó** (không đặt ở cuối toàn bộ thanh task) — `fontStyle=1`, `align=left`, đặt ngay sau khối tô đậm.
4. Actual-progress bar và nhãn % **không** `locked=1` — người dùng cần tự kéo lại khi cập nhật tiến độ kỳ sau.

**Lưu ý quan trọng cho người dùng khi bàn giao skill**: nhãn ngày và actual-progress là các ô độc lập, KHÔNG gắn (bind) vào thanh task — nếu người dùng kéo dài/ngắn một thanh sau này, các nhãn/đoạn tô đậm liên quan sẽ không tự di chuyển theo, cần kéo tay. Luôn nói rõ điều này sau khi vẽ xong.

## I. Khoá bảng (locking) khi bàn giao

Khi người dùng yêu cầu khoá bảng để tránh chỉnh nhầm khung nhưng vẫn cho sửa tiến độ:
- Thêm `locked=1` vào `style` của: tiêu đề, legend, cột sọc nền, toàn bộ hàng timeline (header+footer), nhãn lane, đường phân cách, đường data date + nhãn của nó.
- **Không** thêm `locked=1` vào: mọi bar-chart công việc, milestone (ellipse), nhãn ngày bắt đầu/kết thúc, actual-progress bar + nhãn %, và mọi connector.
- Nhắc người dùng: nếu khoá không có hiệu lực ngay trên client họ dùng, chọn thủ công các phần tử khung rồi bấm khoá qua Format panel.

## J. Tạo file & bàn giao (draw.io connector)

- Nếu người dùng chưa có board/diagram nào: gọi `mcp__draw_io__create_diagram` với toàn bộ XML đã dựng (một lần, đầy đủ — không tạo từng phần rồi update nhiều lần trừ khi đang sửa lỗi cụ thể).
- Nếu người dùng đưa **link file draw.io lưu trên Google Drive/tài khoản riêng của họ** (dạng `https://app.diagrams.net/...#G<id>...`): công cụ `create_diagram` **không** đọc/ghi được vào file đó — nói rõ điều này, gửi XML đã dựng, và hướng dẫn: mở file của họ → **Extras → Edit Diagram** → xoá nội dung cũ → dán XML mới → OK.
- Sau khi vẽ, xuất PDF: **File → Page Setup → A3, Landscape** → **File → Export as → PDF** → tick **Fit Page**, bỏ tick **Crop** — vì trang đã đúng tỉ lệ A3 nên tỉ lệ in sẽ là 100%, không bị cắt 2 đầu như khi export ảnh theo viewport.

---

## Checklist trước khi gọi tool vẽ

- [ ] Đã xác nhận thông tin dự án (mục A) với người dùng
- [ ] Đã xác nhận cấu trúc timeline — đoạn nào weekly, đoạn nào monthly, milestone nào (mục B)
- [ ] Đã xác nhận danh sách lane + đầu việc + chuỗi critical path (mục C)
- [ ] Đã tính x-pixel cho mọi mốc/đầu-cuối bar bằng `timeline_x.py` hoặc công thức tay (mục D), không đoán bằng mắt
- [ ] Trang page = A3 ngang (1169×826), toàn bộ nội dung trong x:10-1158
- [ ] Lane label là hình chữ nhật thường, không phải swimlane/container
- [ ] Mọi connector có `source`/`target` + `exitX/exitY/entryX/entryY` rõ ràng, không thả nổi điểm neo
- [ ] Critical path đỏ nét liền; liên kết phụ xám nét đứt
- [ ] Mỗi bar có 2 nhãn ngày (đầu/cuối) in đậm, sát mép thanh
- [ ] Nếu có yêu cầu cập nhật tiến độ: đường data date xuyên suốt header→footer + actual-progress kết thúc đúng tại đường đó + % ngay sau đoạn tô đậm
- [ ] Nếu người dùng yêu cầu khoá: đúng nhóm phần tử được khoá theo mục I

Nếu bất kỳ mục nào ở trên chưa rõ/chưa được xác nhận, hỏi lại người dùng — không tự suy diễn rồi vẽ.

---

Xem thêm `references/xml_patterns.md` để lấy khối XML mẫu đầy đủ (khung A3, timeline 2 thang, lane không-container, style connector, actual-progress) có thể copy và chỉnh số liệu, đúng theo case thực tế đã dựng thành công trước đó (dự án trường học VSIP Hải Phòng, Rev_6.0 và Rev_6.1).
