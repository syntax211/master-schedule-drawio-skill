# XML mẫu cho Master Schedule draw.io

Các khối dưới đây trích từ bảng tiến độ đã dựng thành công (dự án Multilevel Hai Phong School, Rev_6.0 baseline và Rev_6.1 cập nhật). Copy, đổi tọa độ/text theo dự án mới — không cần nghĩ lại cấu trúc từ đầu.

## 1. Khung trang A3 ngang + tiêu đề + legend

```xml
<mxGraphModel dx="1400" dy="900" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="826" math="0" shadow="0" adaptiveColors="auto">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <mxCell id="ttl" value="TEN DU AN — Master Schedule Rev_X" style="text;html=1;fontSize=11;fontStyle=1;verticalAlign=middle;locked=1;" vertex="1" parent="1">
      <mxGeometry x="10" y="6" width="680" height="18" as="geometry"/>
    </mxCell>
    <mxCell id="sub" value="Thoi gian | Data date | Baseline | Vi tri | Chu dau tu" style="text;html=1;fontSize=6;fontColor=#666666;verticalAlign=middle;locked=1;" vertex="1" parent="1">
      <mxGeometry x="10" y="24" width="680" height="14" as="geometry"/>
    </mxCell>

    <!-- Legend: 1 chip mau cho moi ben, cong critical path + milestone + actual progress + data date -->
    <mxCell id="lgA" value="Employer" style="rounded=1;html=1;fontSize=6;fontStyle=1;fillColor=#f8cecc;strokeColor=#b85450;locked=1;" vertex="1" parent="1">
      <mxGeometry x="700" y="6" width="110" height="14" as="geometry"/>
    </mxCell>
    <mxCell id="lgE" value="Critical Path" style="rounded=1;html=1;fontSize=6;fontStyle=1;fillColor=none;strokeColor=#b85450;strokeWidth=2;fontColor=#b85450;locked=1;" vertex="1" parent="1">
      <mxGeometry x="700" y="24" width="110" height="14" as="geometry"/>
    </mxCell>
    <mxCell id="lgM" value="&#9679;  Milestone (1 day)" style="text;html=1;fontSize=6;fontStyle=1;align=center;locked=1;" vertex="1" parent="1">
      <mxGeometry x="816" y="24" width="110" height="14" as="geometry"/>
    </mxCell>
    <mxCell id="lgP" value="Actual progress" style="rounded=0;html=1;fontSize=6;fontStyle=1;fillColor=#3d5f8a;strokeColor=none;fontColor=#ffffff;locked=1;" vertex="1" parent="1">
      <mxGeometry x="932" y="24" width="110" height="14" as="geometry"/>
    </mxCell>
    <mxCell id="lgT" value="Data date (today)" style="rounded=0;html=1;fontSize=6;fontStyle=1;fillColor=none;strokeColor=#ff0000;strokeWidth=2;fontColor=#cc0000;locked=1;" vertex="1" parent="1">
      <mxGeometry x="1048" y="24" width="110" height="14" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>
```

## 2. Cột sọc nền (dò cột) — lặp lại với x tăng dần, cùng width/height

```xml
<mxCell id="sh1" value="" style="rounded=0;html=1;fillColor=#f5f5f5;strokeColor=none;locked=1;" vertex="1" parent="1">
  <mxGeometry x="158" y="92" width="18" height="670" as="geometry"/>
</mxCell>
<!-- lap lai sh2, sh3... cach nhau 36px (18 mau + 18 trang), height = tong chieu cao than bang -->
```

## 3. Timeline header — 3 hàng con: Năm / Tháng / thang chi tiết

Ví dụ case Rev_6.1: Sep-Dec 2026 chia 5-ngày (mỗi tháng 6 cột x 18px = 108px/tháng), Jan-Aug 2027 gộp tháng (18px/tháng), Sep-Dec 2027 chia 5-ngày lại.

```xml
<!-- Hang Nam -->
<mxCell id="y26" value="2026" style="rounded=0;html=1;fontSize=8;fontStyle=1;fillColor=#e6e6e6;strokeColor=#999999;locked=1;" vertex="1" parent="1">
  <mxGeometry x="140" y="44" width="432" height="16" as="geometry"/>
</mxCell>
<mxCell id="y27" value="2027" style="rounded=0;html=1;fontSize=8;fontStyle=1;fillColor=#e6e6e6;strokeColor=#999999;locked=1;" vertex="1" parent="1">
  <mxGeometry x="572" y="44" width="576" height="16" as="geometry"/>
</mxCell>

<!-- Hang Thang: 108px cho thang weekly (chua 6 cot con), 18px cho thang monthly gop -->
<mxCell id="m1" value="September" style="rounded=0;html=1;fontSize=7;fontStyle=1;fillColor=#f5f5f5;strokeColor=#999999;locked=1;" vertex="1" parent="1">
  <mxGeometry x="140" y="60" width="108" height="18" as="geometry"/>
</mxCell>
<mxCell id="m5" value="Jan" style="rounded=0;html=1;fontSize=5;fontStyle=1;fillColor=#f5f5f5;strokeColor=#999999;locked=1;" vertex="1" parent="1">
  <mxGeometry x="572" y="60" width="18" height="18" as="geometry"/>
</mxCell>

<!-- Hang thang chi tiet: 6 cot 5/10/15/20/25/30 (18px/cot) trong doan weekly -->
<mxCell id="d1" value="5" style="rounded=0;html=1;fontSize=6;fontColor=#666666;fillColor=#ffffff;strokeColor=#d9d9d9;locked=1;" vertex="1" parent="1">
  <mxGeometry x="140" y="78" width="18" height="14" as="geometry"/>
</mxCell>
<!-- ... d2..d6 cach nhau 18px ... -->

<!-- Doan monthly: 1 o rong gop ghi chu "Monthly scale (...)" thay vi 6 cot ngay -->
<mxCell id="dmid" value="Monthly scale (Jan - Aug 2027)" style="rounded=0;html=1;fontSize=6;fontColor=#666666;fillColor=#ffffff;strokeColor=#d9d9d9;locked=1;" vertex="1" parent="1">
  <mxGeometry x="572" y="78" width="144" height="14" as="geometry"/>
</mxCell>
```

Timeline **footer** lặp lại y-hệt cấu trúc trên (đổi id, đặt y = đáy thân bảng), có thể gộp gọn hơn (Sep 2026 / Oct 2026 / ... thay vì đủ 3 hàng) nếu bảng đã dài, xem case Rev_6.1 phần footer chỉ có 2 hàng (tháng rút gọn + phân kỳ theo quý).

## 4. Nhãn lane (KHÔNG dùng swimlane) — hình chữ nhật thường, chữ ngang

```xml
<mxCell id="lblEM" value="THE EMPLOYER&#10;TEN CHU DAU TU" style="rounded=0;html=1;whiteSpace=wrap;align=center;verticalAlign=middle;fontSize=7;fontStyle=1;fillColor=#f5f5f5;strokeColor=#999999;locked=1;" vertex="1" parent="1">
  <mxGeometry x="10" y="152" width="130" height="200" as="geometry"/>
</mxCell>
```

`&#10;` xuống dòng giữa tên vai trò và tên tổ chức thực tế. Chiều cao (200 ở ví dụ) = tổng chiều cao mọi hàng công việc bên trong lane đó, phải khớp với các task bar cùng lane.

## 5. Task bar + nhãn ngày đầu/cuối (in đậm, sát mép)

```xml
<mxCell id="pB" value="Ten cong viec (ngay bat dau - ngay ket thuc)" style="rounded=1;html=1;whiteSpace=wrap;fontSize=6;fontStyle=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontColor=#1a3e73;" vertex="1" parent="1">
  <mxGeometry x="151" y="408" width="792" height="28" as="geometry"/>
</mxCell>
<mxCell id="pBS" value="03.09.26" style="text;html=1;fontSize=5;fontStyle=1;fontColor=#1a3e73;align=left;verticalAlign=top;" vertex="1" parent="1">
  <mxGeometry x="151" y="436" width="60" height="9" as="geometry"/>
</mxCell>
<mxCell id="pBE" value="03.11.27" style="text;html=1;fontSize=5;fontStyle=1;fontColor=#1a3e73;align=right;verticalAlign=top;" vertex="1" parent="1">
  <mxGeometry x="883" y="436" width="60" height="9" as="geometry"/>
</mxCell>
```

`y` của 2 nhãn ngày = đáy thanh (`bar.y + bar.height`), KHÔNG cộng thêm khoảng cách — nếu để dư dù chỉ 1-2px, khi render trông sẽ như có khoảng trắng lớn (đã gặp lỗi này, người dùng phản hồi "để xa quá").

## 6. Milestone 1 ngày (chấm tròn, không phải hình chữ nhật)

```xml
<mxCell id="cA" value="" style="ellipse;html=1;fillColor=#b85450;strokeColor=#7a2020;strokeWidth=1;" vertex="1" parent="1">
  <mxGeometry x="209" y="173" width="14" height="14" as="geometry"/>
</mxCell>
<mxCell id="cAt" value="Ten moc – ngay (0%)" style="text;html=1;fontSize=6;fontStyle=1;fontColor=#a02020;" vertex="1" parent="1">
  <mxGeometry x="227" y="174" width="130" height="12" as="geometry"/>
</mxCell>
```

Ở hàng Project Milestone trên cùng, chấm luôn màu đen (`fillColor=#000000`), không theo màu bên.

## 7. Connector — neo đúng đầu/cuối, critical path đỏ vs liên kết phụ xám

```xml
<!-- Critical path: noi tiep 2 task, do net lien -->
<mxCell id="e1" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor=#b85450;strokeWidth=2;endArrow=classic;endSize=4;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="cA" target="cB">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>

<!-- Lien ket phu len milestone: xam net dut, xuat phat DUNG tu CUOI thanh (khong phai dau) neu ngay hoan thanh la ngay dinh nghia moc -->
<mxCell id="e9" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;dashed=1;strokeColor=#999999;endArrow=classic;endSize=4;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="kA" target="msD">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

**Lỗi hay gặp**: nối từ sai đầu thanh (vd milestone ghi "Construction Completion – ngày X" nhưng connector lại xuất phát từ đầu task thay vì cuối task). Luôn kiểm tra: milestone đại diện cho ngày nào (bắt đầu hay kết thúc của task nguồn) rồi chọn `exitX=0` (đầu) hay `exitX=1` (cuối) tương ứng.

## 8. Data date line + Actual progress + % label

```xml
<!-- Duong data date: xuyen suot header -> footer -->
<mxCell id="ddLine" value="" style="rounded=0;html=1;fillColor=#ff0000;strokeColor=none;locked=1;" vertex="1" parent="1">
  <mxGeometry x="207" y="92" width="2" height="670" as="geometry"/>
</mxCell>
<mxCell id="ddTag" value="TODAY 19.09.2026" style="rounded=0;html=1;fontSize=6;fontStyle=1;fillColor=#ff0000;strokeColor=none;fontColor=#ffffff;locked=1;" vertex="1" parent="1">
  <mxGeometry x="166" y="802" width="84" height="14" as="geometry"/>
</mxCell>

<!-- Actual progress: de tren task bar, KET THUC DUNG TAI x cua ddLine -->
<mxCell id="pBprog" value="" style="rounded=0;html=1;fillColor=#3d5f8a;strokeColor=none;" vertex="1" parent="1">
  <mxGeometry x="153" y="416" width="54" height="12" as="geometry"/>
</mxCell>
<!-- width = ddLine.x - pBprog.x, KHONG phai tuy y theo % -->
<mxCell id="pBpct" value="4%" style="text;html=1;fontSize=6;fontStyle=1;fontColor=#1a3e73;align=left;" vertex="1" parent="1">
  <mxGeometry x="210" y="416" width="30" height="12" as="geometry"/>
</mxCell>
<!-- nhan % dat NGAY SAU pBprog (x = pBprog.x + pBprog.width + 3), KHONG dat o cuoi toan bo task bar -->
```

## 9. Cấu hình timeline_x.py mẫu (case Rev_6.1)

```json
{
  "segments": [
    {"type": "weekly",  "start": "2026-09-01", "x_start": 140, "unit_width": 18},
    {"type": "monthly", "start": "2027-01-01", "x_start": 572, "unit_width": 18},
    {"type": "weekly",  "start": "2027-09-01", "x_start": 716, "unit_width": 18}
  ]
}
```

`unit_width` của `weekly` = bề rộng 1 mốc 5-ngày; của `monthly` = bề rộng gộp cả tháng. Đoạn tiếp theo phải có `start` khớp đúng ngày kết thúc đoạn trước để không bị hở/chồng toạ độ — script tự kiểm tra việc này khi chạy `--validate`.
