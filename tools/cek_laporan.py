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
- laporan pagi (4 Nov 2026): wajib ada "tabel_bawah" "Anggaran <AWAL_BULAN_LABEL> s.d. <KEMARIN_LABEL>"
  (dari tools/pengeluaran_bulan.py) dengan baris Meta Umroh & Meta Haji >= biaya kemarin
- KONTROL (5 Nov 2026, setelah campaign Tira "new" terlewat di laporan pimpinan): "kontrol" per akun
  (biaya level akun + SEMUA campaign ber-spend) wajib ada untuk 15 akun (14 + elharamain Profile); jumlah campaign = biaya akun,
  baris tabel = isi kontrol; laporan pagi juga "kontrol_bulan" (biaya akun 1 s.d. kemarin) = Meta Umroh+Haji
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


AKUN_UMROH = {"1076195694707828": "Diana", "868364731529534": "Tira", "1019832712800468": "Nida",
              "482252744648260": "Hanif", "4678183395742010": "Allif", "1676215979752437": "Fikri",
              "814396810761205": "AIni", "1060984719243481": "Irfan", "521083143750270": "Fifi"}
AKUN_HAJI = {"947788760498911": "Elharamain Haji", "1032468828178224": "Haji 2", "794403715776985": "Haji 3",
             "1526562231314028": "Haji 4", "1050343302646341": "haji"}
# 5 Nov 2026, user: "laporan masukan juga elharamain profile". Campaign awareness (bukan chat WA):
# tabel sendiri "elharamain Profile" (Biaya, Hasil = results Meta), tidak masuk Ringkasan/CPR chat;
# di Anggaran jadi baris "Meta Profile".
AKUN_PROFILE = {"873443374652541": "elharamain Profile"}


def toleransi(x, jenis="pagi"):
    # pagi = data kemarin (sudah final): ketat. harian = data hari ini yang masih berjalan
    # (biaya bisa naik beberapa ribu antara query campaign & query akun): sedikit longgar.
    if jenis == "pagi":
        return max(1000, int(x * 0.002))
    return max(3000, int(x * 0.01))


def cek_kontrol(data, jenis, ring, umroh, haji, masalah):
    """5 Nov 2026 (user: "untuk tira jadi keributan di team kamu harus bener bener cek"):
    laporan pimpinan 04 Nov melewatkan campaign Tira "new". Sekarang setiap akun wajib punya
    "kontrol": biaya level AKUN dari Meta (query terpisah) + daftar SEMUA campaign ber-spend.
    Jumlah campaign harus sama dengan biaya akun → campaign terlewat langsung ketahuan."""
    kontrol = data.get("kontrol")
    if not isinstance(kontrol, list):
        masalah.append("Tidak ada 'kontrol' per akun (biaya level akun + daftar campaign) — wajib sejak 5 Nov")
        return
    semua = {**AKUN_UMROH, **AKUN_HAJI, **AKUN_PROFILE}
    prof = next((x for x in data.get("tabel", []) if x.get("judul", "").startswith("elharamain Profile")), None)
    per = {str(k.get("akun_id")): k for k in kontrol}
    for aid, nama in semua.items():
        if aid not in per:
            masalah.append(f"Kontrol akun {nama} ({aid}) tidak ada")
    tot = {"umroh": 0, "haji": 0, "nonchat": 0}
    chat_tot = {"umroh": 0, "haji": 0}
    baris_umroh = {r["nama"].lower(): r for r in (umroh or {}).get("baris", [])}
    baris_haji = {r["nama"].lower(): r for r in (haji or {}).get("baris", [])}
    for aid, k in per.items():
        nama = semua.get(aid, aid)
        if "error" in k:
            continue  # akun error dicatat di catatan, tidak bisa dicek
        ba = k.get("biaya_akun")
        camps = k.get("campaign", [])
        if not isinstance(ba, int) or ba < 0:
            masalah.append(f"Kontrol {nama}: biaya_akun tidak valid ({ba})")
            continue
        sc = sum(int(c.get("biaya", 0)) for c in camps)
        if abs(sc - ba) > toleransi(ba, jenis):
            masalah.append(f"Kontrol {nama}: jumlah campaign Rp{sc:,} != biaya akun Rp{ba:,} "
                           f"(selisih Rp{ba - sc:,}) — ada campaign TERLEWAT/salah baca, ambil ulang semua campaign akun ini")
        if aid in AKUN_PROFILE:
            pb_ = sum(int(c.get("biaya", 0)) for c in camps)
            ph_ = sum(int(c.get("chat", 0)) for c in camps)
            if pb_ > 0:
                if prof is None:
                    masalah.append(f"Tabel 'elharamain Profile' tidak ada (biaya Rp{pb_:,})")
                else:
                    tb = sum(r.get("biaya", 0) for r in prof.get("baris", []))
                    th = sum(r.get("chat", 0) for r in prof.get("baris", []))
                    if abs(tb - pb_) > 1 or th != ph_:
                        masalah.append(f"Tabel elharamain Profile {tb}/{th} != kontrol {pb_}/{ph_}")
            continue
        chat_b = {"umroh": 0, "haji": 0}
        chat_c = {"umroh": 0, "haji": 0}
        for c in camps:
            j = c.get("jenis", "chat")
            b, ch = int(c.get("biaya", 0)), int(c.get("chat", 0))
            if j == "nonchat":
                tot["nonchat"] += b
                continue
            kat = "umroh" if (aid in AKUN_UMROH or j == "yoga") else "haji"
            chat_b[kat] += b
            chat_c[kat] += ch
        for kat in ("umroh", "haji"):
            tot[kat] += chat_b[kat]
            chat_tot[kat] += chat_c[kat]
        # baris per akun harus sama dengan isi kontrol
        if aid in AKUN_UMROH and chat_b["umroh"] > 0:
            r = baris_umroh.get(nama.lower())
            if r is None:
                masalah.append(f"Umroh per akun tidak punya baris {nama} (biaya chat Rp{chat_b['umroh']:,})")
            elif abs(r["biaya"] - chat_b["umroh"]) > 1 or r["chat"] != chat_c["umroh"]:
                masalah.append(f"Umroh per akun {nama}: {r['biaya']}/{r['chat']} != kontrol {chat_b['umroh']}/{chat_c['umroh']}")
        if aid in AKUN_HAJI and chat_b["haji"] > 0:
            r = baris_haji.get(nama.lower())
            if r is None:
                masalah.append(f"Haji per akun tidak punya baris {nama} (biaya chat Rp{chat_b['haji']:,})")
            elif abs(r["biaya"] - chat_b["haji"]) > 1 or r["chat"] != chat_c["haji"]:
                masalah.append(f"Haji per akun {nama}: {r['biaya']}/{r['chat']} != kontrol {chat_b['haji']}/{chat_c['haji']}")
    if ring:
        rb = {r["nama"].lower(): r for r in ring["baris"]}
        # 5 Nov 2026: baris "elharamain Profile" wajib di Ringkasan (di bawah Umroh & Haji) bila ada biaya
        for aid in AKUN_PROFILE:
            k = per.get(aid)
            pbiaya = int(k.get("biaya_akun", 0)) if k and "error" not in k else 0
            r = rb.get("elharamain profile")
            if pbiaya > 0 and r is None:
                masalah.append(f"Ringkasan tidak punya baris 'elharamain Profile' (biaya Rp{pbiaya:,})")
            elif r is not None and (abs(r["biaya"] - pbiaya) > 1 or not r.get("tanpa_chat")):
                masalah.append(f"Ringkasan elharamain Profile Rp{r['biaya']:,} != kontrol Rp{pbiaya:,} atau tanpa 'tanpa_chat': true")
        for kat, label in (("umroh", "Umroh"), ("haji", "Haji")):
            if kat in rb and (abs(rb[kat]["biaya"] - tot[kat]) > 1 or rb[kat]["chat"] != chat_tot[kat]):
                masalah.append(f"Ringkasan {label} {rb[kat]['biaya']}/{rb[kat]['chat']} != jumlah kontrol {tot[kat]}/{chat_tot[kat]}")
    if jenis != "pagi":
        return
    kb = data.get("kontrol_bulan")
    if not isinstance(kb, list):
        masalah.append("Tidak ada 'kontrol_bulan' (biaya level akun 1 s.d. kemarin per akun) — wajib sejak 5 Nov")
        return
    pb = {str(k.get("akun_id")): k for k in kb}
    for aid, nama in semua.items():
        if aid not in pb:
            masalah.append(f"Kontrol bulan akun {nama} ({aid}) tidak ada")
    total_bulan = sum(int(k.get("biaya_akun", 0)) for k in pb.values() if "error" not in k)
    umroh_min = sum(int(pb[a].get("biaya_akun", 0)) for a in AKUN_UMROH if a in pb and "error" not in pb[a])
    bawah = data.get("tabel_bawah") or []
    nb = {r.get("nama"): r.get("biaya", 0) for x in bawah for r in x.get("baris", [])}
    prof_bulan = sum(int(pb[a].get("biaya_akun", 0)) for a in AKUN_PROFILE if a in pb and "error" not in pb[a])
    if prof_bulan > 0 and "Meta Profile" not in nb:
        masalah.append(f"Tabel anggaran tidak punya baris 'Meta Profile' (biaya akun Rp{prof_bulan:,})")
    if "Meta Umroh" in nb and "Meta Haji" in nb:
        meta = nb["Meta Umroh"] + nb["Meta Haji"] + nb.get("Meta Profile", 0)
        if abs(meta - total_bulan) > toleransi(total_bulan):
            masalah.append(f"Anggaran Meta Umroh+Haji+Profile Rp{meta:,} != total biaya akun 1 s.d. kemarin Rp{total_bulan:,} "
                           f"(selisih Rp{total_bulan - meta:,}) — ada campaign terlewat")
        if nb["Meta Umroh"] + toleransi(umroh_min) < umroh_min:
            masalah.append(f"Anggaran Meta Umroh Rp{nb['Meta Umroh']:,} < total akun Umroh Rp{umroh_min:,}")


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

    if jenis == "pagi":
        jb = f"Anggaran {t['AWAL_BULAN_LABEL']} s.d. {tgl}"
        bawah = data.get("tabel_bawah") or []
        peng = next((x for x in bawah if x.get("judul") == jb), None)
        if peng is None:
            masalah.append(f"Tabel bawah '{jb}' tidak ada (buat dengan tools/pengeluaran_bulan.py)")
        else:
            nb = {r.get("nama"): r for r in peng.get("baris", [])}
            for r in nb.values():
                if not isinstance(r.get("biaya"), int) or r["biaya"] < 0:
                    masalah.append(f"Biaya tidak valid di tabel anggaran / {r.get('nama')}: {r.get('biaya')}")
            for k in ("Meta Umroh", "Meta Haji"):
                if k not in nb:
                    masalah.append(f"Tabel anggaran tidak punya baris '{k}'")
            if ring and umroh and haji and "Meta Umroh" in nb and "Meta Haji" in nb:
                if nb["Meta Umroh"]["biaya"] < total(umroh)[0]:
                    masalah.append("Anggaran Meta Umroh bulan berjalan lebih kecil dari biaya Umroh kemarin")
                if nb["Meta Haji"]["biaya"] < total(haji)[0]:
                    masalah.append("Anggaran Meta Haji bulan berjalan lebih kecil dari biaya Haji kemarin")
    cek_kontrol(data, jenis, ring, umroh, haji, masalah)
    if masalah:
        print("GAGAL — JANGAN KIRIM:")
        for m in masalah:
            print("- " + m)
        sys.exit(1)
    print(f"LOLOS — subjek '{subjek_benar}', tanggal {tgl}")


if __name__ == "__main__":
    main()
