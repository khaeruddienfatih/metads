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
  "catatan": ["CS Haji CPR terendah: Fikri Rp17,2rb", "..."]
}
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
TH = ("border:1px solid #9aa5b1;background:#1f4e79;color:#ffffff;padding:6px 8px;"
      "font-weight:bold;white-space:nowrap;")
TD = "border:1px solid #c3cbd3;padding:5px 8px;white-space:nowrap;"
NUM = "text-align:right;"
ZEBRA = "background:#f2f6fa;"
TOTAL = "background:#dde7f0;font-weight:bold;"
H2 = "font-size:15px;color:#1f4e79;margin:14px 0 4px 0;" + FONT


def rp(n):
    return "Rp" + f"{int(round(n)):,}".replace(",", ".")


def cpr(biaya, chat):
    if not chat:
        return "-"
    v = biaya / chat / 1000
    return "Rp" + f"{v:.1f}".replace(".", ",") + "rb"


def sel(teks, gaya):
    return f'<td style="{gaya}">{html.escape(str(teks))}</td>'


def tabel(t):
    baris = list(t.get("baris", []))
    if t.get("urut", True):
        baris.sort(key=lambda r: r.get("biaya", 0), reverse=True)
    ada_lalu = any("biaya_lalu" in r or "chat_lalu" in r for r in baris)
    kolom = [t.get("label", "Akun"), "Biaya", "Chat", "CPR"]
    if ada_lalu:
        kolom += ["Biaya kemarin lusa", "Chat kemarin lusa", "Perubahan chat"]
    out = [f'<div style="{H2}"><b>{html.escape(t["judul"])}</b></div>',
           f'<table style="{TABLE}" cellpadding="0" cellspacing="0">', "<tr>"]
    for i, k in enumerate(kolom):
        out.append(f'<th style="{TH}{"" if i == 0 else NUM}">{html.escape(k)}</th>')
    out.append("</tr>")

    def isi(r, gaya_baris):
        b, c = r.get("biaya", 0), r.get("chat", 0)
        cells = [sel(r["nama"], TD + gaya_baris), sel(rp(b), TD + NUM + gaya_baris),
                 sel(c, TD + NUM + gaya_baris), sel(cpr(b, c), TD + NUM + gaya_baris)]
        if ada_lalu:
            bl, cl = r.get("biaya_lalu"), r.get("chat_lalu")
            cells.append(sel(rp(bl) if bl is not None else "-", TD + NUM + gaya_baris))
            cells.append(sel(cl if cl is not None else "-", TD + NUM + gaya_baris))
            if cl is not None:
                d = c - cl
                cells.append(sel(f"{d:+d}", TD + NUM + gaya_baris))
            else:
                cells.append(sel("-", TD + NUM + gaya_baris))
        return "<tr>" + "".join(cells) + "</tr>"

    for i, r in enumerate(baris):
        out.append(isi(r, ZEBRA if i % 2 else ""))
    if t.get("total", True) and baris:
        tot = {"nama": t.get("label_total", "Total"),
               "biaya": sum(r.get("biaya", 0) for r in baris),
               "chat": sum(r.get("chat", 0) for r in baris)}
        if ada_lalu:
            tot["biaya_lalu"] = sum(r.get("biaya_lalu") or 0 for r in baris)
            tot["chat_lalu"] = sum(r.get("chat_lalu") or 0 for r in baris)
        out.append(isi(tot, TOTAL))
    out.append("</table>")
    return "\n".join(out)


def main():
    data = json.load(open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin)
    parts = [f'<div style="{FONT}font-size:13px;color:#222;">',
             f'<div style="font-size:17px;font-weight:bold;color:#1f4e79;margin:0 0 6px 0;">'
             f'{html.escape(data["judul"])}</div>']
    for t in data.get("tabel", []):
        parts.append(tabel(t))
    catatan = data.get("catatan") or []
    if catatan:
        parts.append(f'<div style="{H2}"><b>Catatan</b></div><ul style="margin:4px 0;padding-left:18px;">')
        parts += [f'<li style="margin:2px 0;">{html.escape(c)}</li>' for c in catatan]
        parts.append("</ul>")
    parts.append("</div>")
    print("\n".join(parts))


if __name__ == "__main__":
    main()
