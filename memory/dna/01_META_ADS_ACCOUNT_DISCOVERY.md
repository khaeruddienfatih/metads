# 01 — META ADS ACCOUNT DISCOVERY — Elharamain Wisata (Umroh, 9 akun)

Dibuat 22 Okt 2026 dari data Meta Ads MCP (skill 1 "Build DNA"). Jangan berisi rekomendasi —
hanya temuan. Data mentah ringkas: [`data/ringkasan_iklan_lifetime.txt`](data/ringkasan_iklan_lifetime.txt),
[`data/ringkasan_breakdown_90hari.txt`](data/ringkasan_breakdown_90hari.txt).

Akun: AIni 814396810761205 · Tira 868364731529534 · Allif 4678183395742010 · Fifi 521083143750270 ·
Irfan 1060984719243481 · Fikri 1676215979752437 · Nida 1019832712800468 · Diana 1076195694707828 ·
Hanif 482252744648260. (Akun Elharamain Haji 947788760498911 tidak ikut — produk beda.)

## GATE 0 — Status data

| Item | Nilai |
|---|---|
| Konversi yang dipakai | **Percakapan WhatsApp dimulai** (`messaging_conversation_started_7d`). Tidak ada pixel/purchase — bisnis closing di WA. |
| Total konversi (lifetime, iklan WA) | **16.516 chat** dari 13.945 iklan, spend Rp679.951.435 → CPR rata-rata **Rp41.169** |
| Total hari data | Mei 2025 – 22 Okt 2026 (±17 bulan; volume besar mulai Mar 2026) |
| Attribution window | default Meta untuk percakapan pesan (7 hari) |
| Pixel health / error rate | **DATA TIDAK TERSEDIA** — tidak ada pixel; tracking = event percakapan di Meta |
| Anomali periode | AIni 0 spend 6 Agu–8 Sep 2026 (akun berhenti ±1 bulan). Budget change log hampir kosong (Fikri: 3 perubahan dalam 6 bulan). |
| Batas data | Tidak ada data jamaah yang **closing/DP** → ROAS, profit, CVR-ke-penjualan = **DATA TIDAK TERSEDIA** |

**DATA STATUS: HIJAU untuk volume chat (16.516 > 100), MERAH untuk profit (0 data penjualan).
Lanjut dengan confidence: TINGGI untuk pola biaya-per-chat, RENDAH untuk apa pun yang menyangkut penjualan.**

Catatan cakupan: data iklan diambil sampai 3.000 iklan/akun terbaru (AIni, Tira 1.700, akun lain 2.000; Allif & Fikri
lengkap). Breakdown jam/penempatan/usia/wilayah = 90 hari terakhir, halaman pertama (±1.000 baris/akun).

## BAGIAN 1 — Account overview (distribusi per iklan, spend ≥ Rp20rb, n = 5.558)

| Metrik | P25 | Median | P75 | P90 |
|---|---|---|---|---|
| Spend per iklan | Rp31.810 | Rp51.187 | Rp98.624 | Rp231.585 |
| Chat per iklan | 0 | 1 | 2 | 7 |
| CPR (iklan yang dapat chat, n=3.322) | Rp27.883 | Rp39.285 | Rp54.912 | Rp73.836 |
| CTR link | 0,42% | 0,68% | 1,03% | 1,47% |
| CPM | Rp45.228 | Rp77.900 | Rp118.078 | Rp163.545 |
| Chat / klik link | 0% | 12,5% | 25% | 50% |
| Frequency | 1,06 | 1,09 | 1,15 | 1,24 |

40,2% iklan yang sudah spend ≥ Rp20rb tidak pernah dapat chat.

Per akun (lifetime, iklan WA):

| Akun | Spend WA | Chat | CPR | Spend non-WA |
|---|---|---|---|---|
| Fifi | Rp89,5 jt | 2.602 | **Rp34.383** (terbaik) | Rp3,6 jt |
| Diana | Rp80,4 jt | 2.149 | Rp37.392 | Rp1,3 jt |
| Hanif | Rp89,1 jt | 2.158 | Rp41.306 | Rp10,0 jt (lead form) |
| AIni | Rp99,9 jt | 2.388 | Rp41.850 | Rp1,0 jt |
| Tira | Rp56,7 jt | 1.338 | Rp42.355 | — |
| Nida | Rp65,6 jt | 1.546 | Rp42.443 | **Rp151,9 jt** (reach/profile visit/ad recall) |
| Fikri | Rp75,4 jt | 1.749 | Rp43.129 | Rp0,2 jt |
| Irfan | Rp85,6 jt | 1.863 | Rp45.923 | Rp0,2 jt |
| Allif | Rp37,8 jt | 723 | **Rp52.255** (terburuk) | Rp3,3 jt |

## BAGIAN 2 — Account DNA

- **Karakter akun:** volume tinggi, creative banyak (13.945 iklan WA), budget terpusat di campaign (CBO —
  99% spend ad set tanpa budget ad set). Semua ad set WA pakai performance goal `CONVERSATIONS` destinasi WhatsApp.
- **Buyer:** 79% spend ke perempuan; usia 35–44 menyerap spend terbesar (Rp79 jt / 90 hari).
- **Conversion:** 1 chat rata-rata butuh ±8 klik link (chat/klik 12,5% median). WA Status memberi chat termurah walau CTR terendah.
- **Traffic:** CTR median 0,68% — rendah; Meta benchmark (Tira, Irfan) menyebut CTR 52–60% di bawah peer.
- **Pola Pareto:** ✓ TERBUKTI [800 iklan] — 5,7% iklan (≥5 chat) menghasilkan **70% semua chat** dengan 52% spend, CPR Rp30.963.

## BAGIAN 3 — Performance driver: apa yang paling menentukan CPR?

Iklan spend ≥ Rp50rb & chat > 0 (n = 2.454). Korelasi terhadap CPR dan CPR per kuartil:

| Variabel | Korelasi | Q1 → Q4 CPR |
|---|---|---|
| **CPM** | +0,17 | Rp28.757 → Rp36.447 → Rp38.573 → **Rp44.761** (selisih 56%) |
| Chat/klik (CVR) | −0,23 | Rp37.114 → Rp35.755 → Rp33.303 → Rp34.045 |
| CTR | −0,11 | Rp35.902 → Rp34.307 → Rp35.853 → Rp33.898 (datar) |
| Frequency | −0,12 | Q4 (1,19–2,20) justru termurah Rp32.309 |

Ranking: **#1 CPM** (~ PROBABLE — kuartil monoton, 2.454 iklan), **#2 chat/klik** (~ PROBABLE), **#3 CTR** (? HIPOTESIS — pengaruh lemah).
✗ DIBANTAH: "CTR tinggi = CPR murah" — iklan testimoni CTR 1,15% tapi CPR Rp64.073.

## BAGIAN 4 — Creative DNA

| Keluarga creative (dari nama iklan) | Iklan | Spend | Chat | CPR | CTR |
|---|---|---|---|---|---|
| **post** (pakai ulang post) | 1.101 | Rp53,0 jt | 1.569 | **Rp33.748** | 0,84% |
| 10_hari_riyad | 115 | Rp6,4 jt | 177 | Rp36.349 | 0,71% |
| saudia_9_hari | 191 | Rp11,9 jt | 311 | Rp38.162 | 0,47% |
| januari_ | 481 | Rp31,8 jt | 784 | Rp40.589 | 0,60% |
| Desain 3 | 291 | Rp14,2 jt | 316 | Rp44.835 | 0,55% |
| Desain 2 | 464 | Rp17,9 jt | 395 | Rp45.303 | 0,74% |
| Desain 7 | 81 | Rp1,5 jt | 29 | Rp51.195 | 0,82% |
| Desain 4 | 34 | Rp2,0 jt | 33 | Rp60.415 | 0,71% |
| **testi** | 89 | Rp3,9 jt | 61 | **Rp64.073** | 1,15% |

Video/post vs gambar: video Rp40.457 (11.543 chat) vs gambar Rp42.822 (4.973 chat) — beda 6%.
Winner CPR terendah (≥5 chat): campaign salinan "new - Salin" / "Paket - Salin" di Fifi, AIni, Diana ("Dubai") CPR Rp4–13rb (Mar–Apr 2026).
Hook / angle / persona per iklan: **DATA TIDAK TERSEDIA** (nama iklan tidak mencatat hook; isi visual tidak terbaca tool) — perlu tagging.

## BAGIAN 5 — Conversion DNA
Chat/klik tertinggi di **IG Feed 24,7%**, terendah di **WA Status 7,9%** — tapi WA Status CPM Rp8.239 (11× lebih murah) sehingga CPR tetap termurah.
Paket Turki chat/klik 25,5% (klik sedikit tapi niat tinggi); LAT 8,8% (terendah).

## BAGIAN 6 — Audience discovery
- Semua ad set: lokasi kota/provinsi + penempatan manual; tidak ada data LLA/Interest yang terpisah konsisten
  (beberapa ad set bernama "LLA", "interest", "broud"). Benchmark Meta: ad set LLA Tira CTR 52% di bawah peer.
- Penempatan (90 hari, 6 akun): WA Status CPR **Rp26.568**, FB Reels Rp29.548, IG Reels Rp34.286, FB Stories Rp33.996,
  IG Stories Rp39.841, FB Feed Rp40.697, **IG Feed Rp45.073** (spend terbesar Rp26,9 jt).
- Usia: 25–34 CPR Rp39.839 (termurah), 35–44 Rp44.497, 45–54 Rp49.264 (termahal). Laki-laki Rp40.022 vs perempuan Rp45.238.
- Wilayah: Meta **tidak mengembalikan jumlah chat per wilayah** → CPR per kota DATA TIDAK TERSEDIA. CPM: Jakarta Rp72.160, Jabar Rp48.583, Banten Rp46.886, Jateng Rp24.628, Jatim Rp34.379.

## BAGIAN 7 — Budget discovery
- Ad set lifetime spend ≤ Rp100rb: CPR Rp93.020; ≤ Rp250rb: Rp56.242; Rp1–2 jt: Rp35.099; > Rp5 jt: **Rp31.534**.
  Peringatan: ini efek seleksi — Meta memberi spend ke ad set yang sudah konversi.
- Budget ad set ≤ Rp50rb/hari (ABO kecil): CPR **Rp79.459** vs CBO Rp44.682.
- Histori kenaikan budget: **DATA TIPIS** — log Fikri hanya 3 perubahan (6 bln, semua turun). Log akun lain gagal diambil (502).

## BAGIAN 8 — Scaling discovery
DATA TIDAK TERSEDIA untuk event naik budget (lihat Bagian 7). Yang terlihat: duplikasi ("- Salin") dipakai luas;
winner terbaik akun berasal dari campaign salinan (Fifi "new - Salin - Salin", Diana "Dubai - Salin").

## BAGIAN 9 — Fatigue discovery
Frequency ad set (spend ≥ Rp100rb): ≤1,1 Rp41.329 · ≤1,2 Rp44.241 · ≤1,4 Rp42.216 · ≤1,6 Rp38.501 · **≤2,0 Rp32.661** · **>2,0–3,0 Rp46.579**.
→ CPR baru naik setelah frequency > 2,0 (+43%). CTR tidak turun sampai frequency 2,0. Kapan CTR mulai turun per hari: DATA TIDAK TERSEDIA (tidak ada seri harian per iklan).

## BAGIAN 10 — Cannibalism (4 level)
1. **Campaign:** DATA TIDAK TERSEDIA (tidak ada seri harian per campaign). Risiko struktural: 9 akun menargetkan kota & Page yang sama dengan creative yang sama → bersaing di lelang yang sama. ? HIPOTESIS.
2. **Ad set (overlap):** tool tidak menyediakan audience overlap → DATA TIDAK TERSEDIA.
3. **Ads:** ad set dengan 3 iklan → iklan teratas menyerap median **68%** spend; 5 iklan → 55%; 7+ → 32%.
   CPR per jumlah iklan: 1 iklan Rp32.890 · 2 Rp36.698 · 3 Rp39.268 · 5 Rp41.214 · 7+ Rp40.423.
4. **Creative:** gambar sama dipakai di banyak ad set/akun (aturan user "gambar unik" muncul setelah user hapus kembaran). Dampak: DATA TIDAK TERSEDIA.

## BAGIAN 11 — Time-based pattern (90 hari, campaign WA)
Blok jam: 20–23 **Rp35.967** · 05–09 Rp37.058 · 00–04 Rp38.335 · 10–14 Rp40.239 · 15–19 **Rp41.787**.
Jam terbaik berbeda tiap akun (Allif 17 & 07, Diana 13 & 09, Fifi 23 & 00, Irfan 11 & 06). Selisih blok ±16% → sensitivitas waktu rendah.
Hari dalam minggu: DATA TIDAK TERSEDIA (chat harian akun tidak tersedia di level akun).
Tren bulanan (iklan per bulan dibuat): Mar 2026 Rp23.029 → Apr 31.533 → Mei 35.266 → Jun 40.975 → Jul 46.647 → Agu 38.828 → Sep 43.291 → **Okt 48.096**.

## BAGIAN 12 — Account rule extraction (≥20)
1. Jika iklan spend Rp20–35rb maka 74% belum dapat chat. ✓ TERBUKTI — 1.220 dari 1.657.
2. Jika iklan spend Rp35–50rb maka 59% belum dapat chat. ✓ TERBUKTI — 615 dari 1.046.
3. Jika iklan spend Rp50–75rb maka 31% tanpa chat. ✓ — 310 dari 999.
4. Jika iklan spend Rp75–100rb maka 14% tanpa chat. ✓ — 67 dari 482.
5. Jika iklan spend ≥ Rp100rb maka hampir selalu dapat chat (≤4% nol). ✓ — 24 dari 1.374.
6. Jika iklan sudah ≥ Rp250rb maka CPR Rp32,5rb (lebih murah dari rata-rata). ✓ — 510 iklan (efek seleksi Meta).
7. Jika iklan ≥5 chat maka CPR rata-rata Rp30.963. ✓ — 800 iklan.
8. Jika CPM iklan ≤ Rp36,5rb maka CPR ±Rp28,8rb; jika > Rp104rb maka ±Rp44,8rb. ~ PROBABLE — 2.454 iklan, korelasi 0,17.
9. Jika penempatan WA Status maka CPR lebih murah daripada IG Feed (Rp19–38rb vs Rp43–55rb). ✓ TERBUKTI — 7 dari 8 akun yang punya data WA Status; pengecualian Allif (Feed Rp31,7rb vs WA Rp33,8rb). AIni tidak punya data WA Status.
10. Jika penempatan IG Feed maka CPR lebih mahal daripada IG Reels. ~ PROBABLE — 7 dari 9 akun; pengecualian Nida (Reels Rp58.511) dan Allif (Reels Rp34,8rb vs Feed Rp31,7rb).
11. Jika usia 45–54 maka CPR ±24% lebih mahal dari 25–34. ~ PROBABLE — sampel 6 akun, 90 hari.
12. Jika creative "testi"/testimoni maka CTR tinggi (1,15%) tapi CPR Rp64rb. ~ PROBABLE — 89 iklan.
13. Jika creative pakai ulang post ("post") maka CPR Rp33,7rb (–19% vs rata-rata). ✓ — 1.101 iklan.
14. Jika paket LAT maka CPR Rp59rb, chat/klik 8,8%. ✓ — 601 iklan.
15. Jika paket 9 Hari Januari maka CPR Rp41rb dan volume terbesar (3.387 chat). ✓ — 2.266 iklan.
16. Jika paket 12 Hari Januari maka CPR Rp47rb (14% lebih mahal dari 9 Hari). ✓ — 2.133 iklan.
17. Jika frequency ad set 1,6–2,0 maka CPR termurah Rp32,7rb; > 2,0 naik ke Rp46,6rb. ~ PROBABLE — spend Rp77 jt vs Rp12 jt.
18. Jika ad set budget sendiri ≤ Rp50rb/hari maka CPR Rp79rb (vs CBO Rp45rb). ~ PROBABLE — 172 chat.
19. Jika ad set berisi 3 iklan maka 1 iklan menyerap ±68% spend. ✓ — 433 grup ad set.
20. Jika objective bukan WA (lead form Hanif) maka biaya per lead Rp121.811. ? HIPOTESIS — 74 lead.
21. Jika iklan dibuat Okt 2026 maka CPR Rp48rb (tertinggi sejak Feb 2026). ✓ — 1.894 iklan.
22. Jika blok jam 15–19 maka CPR ±16% lebih mahal dari 20–23. ? HIPOTESIS — beda kecil, tidak konsisten per akun.

## BAGIAN 13 — Final discovery summary
- **Faktor #1 penentu CPR:** CPM (lelang/penempatan) — bukan CTR.
- **Faktor #1 penentu "ROAS":** DATA TIDAK TERSEDIA (tidak ada data closing).
- **Dibantah data:** CTR tinggi ≠ CPR murah; frequency 1,2–2,0 belum fatigue.
- **Peluang terbesar:** porsi WA Status + Reels; scale iklan ≥5 chat (70% chat dari 5,7% iklan); pakai ulang post winner.
- **Risiko terbesar:** CPR naik terus sejak Mar (Rp23rb → Rp48rb); 9 akun bersaing di audiens yang sama; aturan kill Rp35rb memotong iklan sebelum mencapai median biaya 1 chat (Rp39rb).
- **Wajib diuji berikutnya:** tracking closing dari WA (jamaah DP) per iklan; tagging hook/angle di nama iklan; ambang kill Rp35rb vs Rp50rb.
