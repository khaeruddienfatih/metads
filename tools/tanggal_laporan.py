#!/usr/bin/env python3
"""Cetak tanggal & label laporan dalam WIB (UTC+7) — dipakai routine email.

2 Nov 2026: laporan pagi sempat berlabel "31 Okt" padahal datanya 1 Nov, karena
model salah memilih tanggal. Routine WAJIB memakai output script ini apa adanya.

Pemakaian: python3 tools/tanggal_laporan.py
Output (KEY=VALUE per baris):
  HARI_INI_ISO, HARI_INI_LABEL   tanggal hari ini (WIB)
  KEMARIN_ISO,  KEMARIN_LABEL    tanggal kemarin = tanggal data laporan pagi
  LUSA_ISO,     LUSA_LABEL       kemarin lusa = pembanding laporan pagi
  JAM                            HH:MM WIB sekarang
  SESI                           Siang (<14), Sore (14-18), Malam (>=19) untuk laporan 12/16/21
"""
from datetime import datetime, timedelta, timezone

BULAN = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]
WIB = timezone(timedelta(hours=7))  # tidak bergantung tzdata


def label(d):
    return f"{d.day:02d} {BULAN[d.month - 1]} {d.year}"


now = datetime.now(WIB)
hari_ini = now.date()
kemarin = hari_ini - timedelta(days=1)
lusa = hari_ini - timedelta(days=2)
sesi = "Siang" if now.hour < 14 else ("Sore" if now.hour < 19 else "Malam")

print(f"HARI_INI_ISO={hari_ini.isoformat()}")
print(f"HARI_INI_LABEL={label(hari_ini)}")
print(f"KEMARIN_ISO={kemarin.isoformat()}")
print(f"KEMARIN_LABEL={label(kemarin)}")
print(f"LUSA_ISO={lusa.isoformat()}")
print(f"LUSA_LABEL={label(lusa)}")
print(f"JAM={now:%H:%M}")
print(f"SESI={sesi}")
