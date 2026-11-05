#!/usr/bin/env python3
"""Bangun "tabel_bawah" laporan pagi: anggaran bulan berjalan per platform (4 Nov 2026).

User: "laporan anggaran cukup tulis tiktok haji umroh dan nanti lainya misal muncul invoice gads".
Baris: Meta Umroh, Meta Haji (spend Meta tgl 1 s.d. kemarin, semua campaign termasuk non-chat),
lalu satu baris per platform lain (TikTok, Google Ads, ...) dari memory/invoice-iklan.json
(jumlah = total dibayar termasuk PPN, invoice bertanggal tgl 1 s.d. kemarin).
Invoice baru: tambahkan entri ke memory/invoice-iklan.json.

Pemakaian: python3 tools/pengeluaran_bulan.py <biaya_meta_umroh> <biaya_meta_haji> [<biaya_meta_profile>]
(5 Nov 2026, user: "laporan masukan juga elharamain profile" → baris "Meta Profile" = spend akun
elharamain Profile 873443374652541, campaign awareness, bukan chat.)
Output: JSON list untuk "tabel_bawah" (dipakai tools/laporan_email_html.py).
"""
import json
import subprocess
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
t = dict(l.split("=", 1) for l in subprocess.run(
    [sys.executable, str(here / "tanggal_laporan.py")], capture_output=True, text=True, check=True
).stdout.strip().splitlines())
umroh, haji = int(sys.argv[1]), int(sys.argv[2])
baris = [{"nama": "Meta Umroh", "biaya": umroh}, {"nama": "Meta Haji", "biaya": haji}]
if len(sys.argv) > 3:
    baris.append({"nama": "Meta Profile", "biaya": int(sys.argv[3])})
lain = {}
for inv in json.load(open(here.parent / "memory" / "invoice-iklan.json")):
    if t["AWAL_BULAN_ISO"] <= inv["tanggal"] <= t["KEMARIN_ISO"]:
        lain[inv["platform"]] = lain.get(inv["platform"], 0) + int(inv["jumlah"])
baris += [{"nama": p, "biaya": b} for p, b in lain.items()]
print(json.dumps([{"judul": f"Anggaran {t['AWAL_BULAN_LABEL']} s.d. {t['KEMARIN_LABEL']}",
                   "label": "Platform", "hanya_biaya": True, "urut": False, "baris": baris}],
                 ensure_ascii=False))
