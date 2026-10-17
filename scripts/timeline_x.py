#!/usr/bin/env python3
"""
timeline_x.py — Tinh toa do x-pixel cho mot ngay bat ky tren timeline
Master Schedule draw.io (thang weekly 5-ngay hoac thang monthly gop).

Dung de thay cho tinh tay bang mat, la nguon loi hay gap nhat khi dung
XML thu cong (bar/milestone/connector lech ngay).

Cach dung:
    python3 timeline_x.py --config timeline_config.json --date 2027-05-03
    python3 timeline_x.py --config timeline_config.json --range 2026-12-30 2027-05-03
    python3 timeline_x.py --config timeline_config.json --validate

timeline_config.json:
{
  "segments": [
    {"type": "weekly",  "start": "2026-09-01", "x_start": 140, "unit_width": 18},
    {"type": "monthly", "start": "2027-01-01", "x_start": 572, "unit_width": 18},
    {"type": "weekly",  "start": "2027-09-01", "x_start": 716, "unit_width": 18}
  ]
}

- "weekly": moi thang chia 6 coc (5,10,15,20,25,30/31), moi coc rong unit_width.
  Vi tri trong thang duoc noi suy tuyen tinh theo ngay/5.
- "monthly": ca thang gop thanh 1 coc rong unit_width, ngay noi suy tuyen tinh
  theo day/days_in_month trong pham vi coc do.
- Doan sau phai bat dau dung ngay ke tiep doan truoc (vd doan truoc ket thuc
  31/12/2026 thi doan sau phai start=2027-01-01) de khong ho/chong toa do.
"""

import argparse
import calendar
import json
import sys
from datetime import date, timedelta


def parse_date(s: str) -> date:
    y, m, d = (int(x) for x in s.split("-"))
    return date(y, m, d)


def month_add(d: date, months: int) -> date:
    total = (d.month - 1) + months
    y = d.year + total // 12
    m = total % 12 + 1
    return date(y, m, 1)


def segment_end(seg: dict, next_seg: dict | None) -> date:
    """Ngay ket thuc (khong bao gom) cua 1 segment, suy ra tu segment tiep theo,
    hoac +1 nam neu la segment cuoi (chi de validate/hien thi)."""
    if next_seg is not None:
        return parse_date(next_seg["start"])
    start = parse_date(seg["start"])
    return date(start.year + 1, start.month, start.day)


def x_for_date(segments: list[dict], target: date) -> float:
    for i, seg in enumerate(segments):
        start = parse_date(seg["start"])
        nxt = segments[i + 1] if i + 1 < len(segments) else None
        end = segment_end(seg, nxt)
        if start <= target < end or (nxt is None and target >= start):
            return _x_within_segment(seg, start, target)
    raise ValueError(f"Ngay {target} nam ngoai moi segment trong config.")


def _x_within_segment(seg: dict, seg_start: date, target: date) -> float:
    x0 = seg["x_start"]
    uw = seg["unit_width"]
    if seg["type"] == "weekly":
        months_in = (target.year - seg_start.year) * 12 + (target.month - seg_start.month)
        day = target.day
        # 6 coc/thang: coc index = floor((day-1)/5), phan du noi suy trong coc
        col = (day - 1) // 5
        frac = ((day - 1) % 5) / 5.0
        return x0 + months_in * 6 * uw + col * uw + frac * uw
    elif seg["type"] == "monthly":
        months_in = (target.year - seg_start.year) * 12 + (target.month - seg_start.month)
        days_in_month = calendar.monthrange(target.year, target.month)[1]
        frac = (target.day - 1) / days_in_month
        return x0 + months_in * uw + frac * uw
    else:
        raise ValueError(f"Khong nhan dien type segment: {seg['type']}")


def validate(segments: list[dict]) -> list[str]:
    problems = []
    for i in range(len(segments) - 1):
        cur_end = segment_end(segments[i], segments[i + 1])
        nxt_start = parse_date(segments[i + 1]["start"])
        if cur_end != nxt_start:
            problems.append(
                f"Ho/chong toa do giua segment {i} (ket thuc {cur_end}) "
                f"va segment {i+1} (bat dau {nxt_start})"
            )
        if segments[i + 1]["x_start"] <= segments[i]["x_start"]:
            problems.append(
                f"x_start cua segment {i+1} phai lon hon segment {i}"
            )
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True, help="Duong dan file timeline_config.json")
    ap.add_argument("--date", help="Ngay can tinh x, dinh dang YYYY-MM-DD")
    ap.add_argument("--range", nargs=2, metavar=("START", "END"), help="Tinh x cho ca ngay bat dau va ket thuc, kem width")
    ap.add_argument("--validate", action="store_true", help="Chi kiem tra config co ho/chong toa do khong")
    args = ap.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    segments = cfg["segments"]

    problems = validate(segments)
    if problems:
        print("CANH BAO cau hinh timeline:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        if args.validate:
            sys.exit(1)

    if args.validate:
        print("Config hop le, khong ho/chong toa do.")
        return

    if args.date:
        d = parse_date(args.date)
        x = x_for_date(segments, d)
        print(f"{args.date} -> x = {x:.1f}")

    if args.range:
        d1 = parse_date(args.range[0])
        d2 = parse_date(args.range[1])
        x1 = x_for_date(segments, d1)
        x2 = x_for_date(segments, d2)
        print(f"Bat dau {args.range[0]} -> x = {x1:.1f}")
        print(f"Ket thuc {args.range[1]} -> x = {x2:.1f}")
        print(f"width (dung cho geometry cua bar) = {x2 - x1:.1f}")

    if not args.date and not args.range:
        print("Can truyen --date hoac --range (hoac --validate). Xem --help.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
