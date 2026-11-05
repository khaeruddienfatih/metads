#!/usr/bin/env python3
"""Bangun HTML email laporan chat WA (Umroh/Haji) dengan tabel ber-style inline.

Dipakai routine email (06:00, 08:00, 12/16/21). Gmail membuang <style>, jadi semua
style ditulis inline di setiap sel.

Pemakaian:
    python3 tools/laporan_email_html.py data.json > email.html

Format data.json:
{
  "judul": "Laporan Malam 01 Nov 2026 s.d. 21:17 WIB",
  "tabel": [
    {"judul": "Ringkasan", "label": "Kategori", "urut": false, "total": false,
     "baris": [{"nama": "Umroh", "biaya": 4979532, "chat": 139,
                "biaya_lalu": 4800000, "chat_lalu": 130}]},
    {"judul": "Umroh per akun", "label": "Akun",
     "baris": [{"nama": "Fifi", "biaya": 1001799, "chat": 28}]}
  ],
  "catatan": ["CS Haji CPR terendah: Fikri Rp17,2rb", "..."],
  "tabel_bawah": [{"judul": "Anggaran 01 Nov 2026 s.d. 03 Nov 2026", "label": "Platform",
                   "hanya_biaya": true, "urut": false,
                   "baris": [{"nama": "Meta Umroh", "biaya": 18600000}, {"nama": "TikTok", "biaya": 6826500}]}]
}
- "hanya_biaya": true → tabel hanya kolom nama + Biaya (+ total).
- "kolom_hasil" / "kolom_biaya_hasil" opsional (5 Nov 2026, tabel elharamain Profile): ganti judul kolom
  "Chat"/"CPR" (mis. "Hasil" / "Biaya/hasil"); angkanya tetap di field "chat".
- baris "tanpa_chat": true (5 Nov 2026, user: "untuk laporan elharamain profile kamu masukan di atas bagian
  haji umroh dan profile jadi pimpinan tau habis berapa dalam 1 hari"): baris elharamain Profile di
  Ringkasan — kolom Chat/CPR "-", biayanya ikut Total, tapi CPR Total hanya dari baris chat.
- "tabel_bawah" opsional (buat dengan tools/pengeluaran_bulan.py): tabel yang ditaruh PALING BAWAH, setelah Catatan (4 Nov 2026, user:
  "laporan setiap pagi itu ada laporan pengeluaran mulai tanggal 1 sampai tanggal saat ini
  dalam bentuk table di bawah").
- "biaya" & "chat" angka mentah (rupiah, jumlah chat). CPR dihitung otomatis.
- "urut" (default true): urutkan baris dari biaya terbesar.
- "total" (default true): tambah baris total tebal di bawah.
- "biaya_lalu"/"chat_lalu" opsional: kalau ada, tabel diberi kolom
  Biaya kemarin lusa | Chat kemarin lusa | Perubahan chat.
"""
import html
import json
import sys

FONT = "font-family:Arial,Helvetica,sans-serif;"
TABLE = "border-collapse:collapse;margin:4px 0 18px 0;font-size:13px;" + FONT
TH = ("border:1px solid #9aa5b1;background-color:#1f4e79;color:#ffffff;padding:6px 8px;"
      "font-weight:bold;white-space:nowrap;")
TD = "border:1px solid #c3cbd3;padding:5px 8px;white-space:nowrap;"
NUM = "text-align:right;"
ZEBRA = "background-color:#f2f6fa;"
TOTAL = "background-color:#dde7f0;font-weight:bold;"
H2 = "font-size:15px;color:#1f4e79;margin:14px 0 4px 0;" + FONT


def rp(n):
    return "Rp" + f"{int(round(n)):,}".replace(",", ".")


def cpr(biaya, chat):
    if not chat:
        return "-"
    if biaya / chat < 1000:  # hasil murah (tayangan/jangkauan elharamain Profile)
        return rp(biaya / chat)
    v = biaya / chat / 1000
    return "Rp" + f"{v:.1f}".replace(".", ",") + "rb"


def sel(teks, gaya):
    return f'<td style="{gaya}">{html.escape(str(teks))}</td>'


def tabel(t):
    baris = list(t.get("baris", []))
    if t.get("urut", True):
        baris.sort(key=lambda r: r.get("biaya", 0), reverse=True)
    ada_lalu = any("biaya_lalu" in r or "chat_lalu" in r for r in baris)
    hb = t.get("hanya_biaya", False)  # 4 Nov 2026: tabel anggaran cukup kolom Biaya
    kolom = [t.get("label", "Akun"), "Biaya"] if hb else [t.get("label", "Akun"), "Biaya",
                                                                t.get("kolom_hasil", "Chat"), t.get("kolom_biaya_hasil", "CPR")]
    if ada_lalu:
        kolom += ["Biaya kemarin lusa", "Chat kemarin lusa", "Perubahan chat"]
    out = [f'<div style="{H2}"><b>{html.escape(t["judul"])}</b></div>',
           f'<table style="{TABLE}" cellpadding="0" cellspacing="0">', "<tr>"]
    for i, k in enumerate(kolom):
        out.append(f'<th bgcolor="#1f4e79" style="{TH}{"" if i == 0 else NUM}"><font color="#ffffff">{html.escape(k)}</font></th>')
    out.append("</tr>")

    def isi(r, gaya_baris):
        b, c = r.get("biaya", 0), r.get("chat", 0)
        cells = [sel(r["nama"], TD + gaya_baris), sel(rp(b), TD + NUM + gaya_baris)]
        if not hb and r.get("tanpa_chat"):
            cells += [sel("-", TD + NUM + gaya_baris), sel("-", TD + NUM + gaya_baris)]
        elif not hb:
            cells += [sel(c, TD + NUM + gaya_baris), sel(cpr(r.get("biaya_cpr", b), c), TD + NUM + gaya_baris)]
        if ada_lalu:
            bl, cl = r.get("biaya_lalu"), r.get("chat_lalu")
            cells.append(sel(rp(bl) if bl is not None else "-", TD + NUM + gaya_baris))
            cells.append(sel(cl if cl is not None else "-", TD + NUM + gaya_baris))
            if cl is not None:
                d = c - cl
                cells.append(sel(f"{d:+d}", TD + NUM + gaya_baris))
            else:
                cells.append(sel("-", TD + NUM + gaya_baris))
        warna = "#dde7f0" if gaya_baris == TOTAL else ("#f2f6fa" if gaya_baris == ZEBRA else "")
        tr = f'<tr bgcolor="{warna}">' if warna else "<tr>"
        return tr + "".join(cells) + "</tr>"

    for i, r in enumerate(baris):
        out.append(isi(r, ZEBRA if i % 2 else ""))
    if t.get("total", True) and baris:
        tot = {"nama": t.get("label_total", "Total"),
               "biaya": sum(r.get("biaya", 0) for r in baris),
               "chat": sum(r.get("chat", 0) for r in baris if not r.get("tanpa_chat")),
               "biaya_cpr": sum(r.get("biaya", 0) for r in baris if not r.get("tanpa_chat"))}
        if ada_lalu:
            tot["biaya_lalu"] = sum(r.get("biaya_lalu") or 0 for r in baris)
            tot["chat_lalu"] = sum(r.get("chat_lalu") or 0 for r in baris)
        out.append(isi(tot, TOTAL))
    out.append("</table>")
    return "\n".join(out)


def main():
    data = json.load(open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin)
    # 1 Nov 2026, perintah user: "kalau mau kirim email isinya pakai salam dulu ya"
    salam = data.get("salam", "Assalamu'alaikum Warahmatullahi Wabarakatuh,")
    pembuka = data.get("pembuka", "Berikut laporan chat WhatsApp dan biaya iklan Meta Elharamain Wisata:")
    penutup = data.get("penutup", "Wassalamu'alaikum Warahmatullahi Wabarakatuh.")
    parts = [f'<div style="{FONT}font-size:13px;color:#222;">',
             f'<p style="margin:0 0 4px 0;">{html.escape(salam)}</p>',
             f'<p style="margin:0 0 12px 0;">{html.escape(pembuka)}</p>',
             f'<div style="font-size:17px;font-weight:bold;color:#1f4e79;margin:0 0 6px 0;">'
             f'{html.escape(data["judul"])}</div>']
    for t in data.get("tabel", []):
        parts.append(tabel(t))
    catatan = data.get("catatan") or []
    if catatan:
        parts.append(f'<div style="{H2}"><b>Catatan</b></div><ul style="margin:4px 0;padding-left:18px;">')
        parts += [f'<li style="margin:2px 0;">{html.escape(c)}</li>' for c in catatan]
        parts.append("</ul>")
    for t in data.get("tabel_bawah", []):
        parts.append(tabel(t))
    parts.append(f'<p style="margin:14px 0 0 0;">{html.escape(penutup)}</p>')
    parts.append("</div>")
    print("\n".join(parts))


if __name__ == "__main__":
    main()
