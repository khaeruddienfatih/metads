#!/usr/bin/env python3
"""Cek laporan SEBELUM email dikirim (2 Nov 2026, perintah user: "kamu cek dulu sebelum
model mengirim ... kalau sudah diterima pimpinan saya akan kena masalah").

Pemakaian:
    python3 tools/cek_laporan.py pagi  /tmp/laporan.json "<subjek email>"
    python3 tools/cek_laporan.py harian /tmp/laporan.json "<subjek email>"

Keluar dengan kode 0 + "LOLOS" kalau aman. Kode 1 + daftar masalah kalau ada yang salah —
routine TIDAK BOLEH mengirim email ke penerima laporan; kirim peringatan ke
elharamainwisata@gmail.com saja.

Yang dicek:
- subjek PERSIS sesuai format & tanggal dari tools/tanggal_laporan.py
  (pagi: KEMARIN_LABEL + "(Rekap Harian)"; harian: HARI_INI_LABEL + "(Siang/Sore/Malam)")
- judul & judul tabel memakai tanggal yang sama; tidak ada tanggal lain (mis. kemarin lusa)
- 4 tabel lengkap (Ringkasan, Umroh per akun, Haji per CS, Haji per akun)
- angka masuk akal: biaya & chat bilangan bulat >= 0, total Umroh/Haji di ringkasan
  sama dengan jumlah tabel per akun, total Haji per CS = total Haji per akun
- tidak ada kolom pembanding hari sebelumnya (user: "ga perlu ada perbandingan kemarin")
"""
import json
import re
import subprocess
import sys
from pathlib import Path

BULAN = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]
POLA_TGL = re.compile(r"\b\d{2} (?:%s) \d{4}\b" % "|".join(BULAN))


def tanggal():
    out = subprocess.run([sys.executable, str(Path(__file__).with_name("tanggal_laporan.py"))],
                         capture_output=True, text=True, check=True).stdout
    return dict(l.split("=", 1) for l in out.strip().splitlines())


def total(tabel):
    return (sum(int(r.get("biaya", 0)) for r in tabel["baris"]),
            sum(int(r.get("chat", 0)) for r in tabel["baris"]))


def main():
    jenis, path, subjek = sys.argv[1], sys.argv[2], sys.argv[3]
    t = tanggal()
    data = json.load(open(path))
    masalah = []

    if jenis == "pagi":
        tgl = t["KEMARIN_LABEL"]
        subjek_benar = f"Laporan Iklan Elharamain Wisata {tgl} (Rekap Harian)"
    else:
        tgl = t["HARI_INI_LABEL"]
        subjek_benar = f"Laporan Iklan Elharamain Wisata {tgl} ({t['SESI']})"
    if subjek.strip() != subjek_benar:
        masalah.append(f"Subjek salah: '{subjek}' — seharusnya '{subjek_benar}'")

    teks_judul = [data.get("judul", "")] + [x.get("judul", "") for x in data.get("tabel", [])]
    for j in teks_judul:
        for d in POLA_TGL.findall(j):
            if d != tgl:
                masalah.append(f"Judul memakai tanggal {d}, seharusnya {tgl}: '{j}'")
    if tgl not in data.get("judul", ""):
        masalah.append(f"Judul utama tidak memuat tanggal {tgl}: '{data.get('judul')}'")

    cari = lambda awal: next((x for x in data.get("tabel", []) if x.get("judul", "").startswith(awal)), None)
    ring, umroh, cs, haji = cari("Ringkasan"), cari("Umroh per akun"), cari("Haji per CS"), cari("Haji per akun")
    for nama, x in [("Ringkasan", ring), ("Umroh per akun", umroh), ("Haji per CS", cs), ("Haji per akun", haji)]:
        if x is None:
            masalah.append(f"Tabel '{nama}' tidak ada")
    for x in data.get("tabel", []):
        for r in x.get("baris", []):
            for k in ("biaya", "chat", "biaya_lalu", "chat_lalu"):
                if k in r and (not isinstance(r[k], int) or r[k] < 0):
                    masalah.append(f"Nilai {k} tidak valid di '{x.get('judul')}' / {r.get('nama')}: {r[k]}")

    if ring and umroh and cs and haji:
        rb = {r["nama"].lower(): r for r in ring["baris"]}
        if "umroh" in rb and (rb["umroh"]["biaya"], rb["umroh"]["chat"]) != total(umroh):
            masalah.append(f"Ringkasan Umroh {rb['umroh']['biaya']}/{rb['umroh']['chat']} != total Umroh per akun {total(umroh)}")
        if "haji" in rb and (rb["haji"]["biaya"], rb["haji"]["chat"]) != total(haji):
            masalah.append(f"Ringkasan Haji {rb['haji']['biaya']}/{rb['haji']['chat']} != total Haji per akun {total(haji)}")
        if total(cs) != total(haji):
            masalah.append(f"Total Haji per CS {total(cs)} != total Haji per akun {total(haji)}")
    # 2 Nov 2026, perintah user "ga perlu ada perbandingan kemarin": tidak boleh ada kolom pembanding
    for x in data.get("tabel", []):
        for r in x.get("baris", []):
            if "biaya_lalu" in r or "chat_lalu" in r:
                masalah.append(f"Ada data pembanding (biaya_lalu/chat_lalu) di '{x.get('judul')}' — tidak boleh")
                break

    if masalah:
        print("GAGAL — JANGAN KIRIM:")
        for m in masalah:
            print("- " + m)
        sys.exit(1)
    print(f"LOLOS — subjek '{subjek_benar}', tanggal {tgl}")


if __name__ == "__main__":
    main()
