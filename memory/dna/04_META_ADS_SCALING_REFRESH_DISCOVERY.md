# 04 — META ADS SCALING & REFRESH DISCOVERY — Elharamain Umroh

Skill 4 (22 Okt 2026). Membangun di atas file 01–03.

**Batas data:** log perubahan budget hampir kosong (Fikri: 3 perubahan Mei–Okt, semua turun; akun lain
gagal diambil, error 502), dan tidak ada seri harian per campaign/iklan. Karena itu semua bagian
"sebelum vs sesudah scale" berstatus **DATA TIDAK TERSEDIA / HIPOTESIS**. Angka yang bisa dipakai berasal
dari distribusi lifetime per iklan dan per ad set.

## BAGIAN 1 — Scaling history mapping
| Tanggal | Objek | Budget | Metode | Hasil |
|---|---|---|---|---|
| 13 Mei 2026 | Fikri "new" | Rp30rb → Rp90rb/hari (+200%) | vertikal | sebelum/sesudah: DATA TIDAK TERSEDIA |
| 1 Okt 2026 | Fikri "Fikri" | Rp350rb → Rp250rb (−29%) | turun | — |
| 1 Okt 2026 | Fikri "Riyad Air" | Rp250rb → Rp100rb (−60%) | turun (paket dihentikan) | — |
| 29 Sep 2026 | akun Haji (bukan Umroh) | +15%, 6 campaign | vertikal | dicatat di chat-memory, hasil tidak diukur |

Pola yang muncul: scaling **horizontal** (duplikasi "- Salin", campaign baru per wilayah, akun baru) jauh lebih sering daripada naik budget.

## BAGIAN 2 — Vertical scaling (+10/20/30/50/100%)
DATA TIDAK TERSEDIA. Cara menemukan: catat setiap kenaikan budget di `chat-log.md` + CPR 3 hari sebelum & sesudah.

## BAGIAN 3 — Horizontal scaling
- Duplikasi campaign/ad set ("- Salin") menghasilkan winner terbaik di Fifi, AIni, Diana (CPR Rp4–13rb, Mar–Apr 2026). ? HIPOTESIS — 3 akun, masa CPM murah (Mar CPM Rp13rb).
- Campaign baru per wilayah (Okt) → CPR iklan Okt Rp48rb (tertinggi). ~ PROBABLE — 1.894 iklan.
- Fresh broad / ASC: tidak pernah dipakai → DATA TIDAK TERSEDIA.

## BAGIAN 4 — Scaling trigger discovery
Dari iklan yang akhirnya menjadi winner (≥5 chat, n = 800, CPR Rp30.963):
- Minimum chat sebelum layak scale: **5 chat** (di bawah itu, CPR iklan masih acak — 40% iklan ≥ Rp20rb nol chat).
- CPR maksimum: **≤ Rp39rb** (median akun) — winner rata-rata Rp31rb.
- Spend minimum: **≥ Rp100rb** (di bawah itu 4–96% iklan masih nol).
- CTR minimum: tidak relevan (CTR bukan driver).
- Label: ~ PROBABLE (threshold dari distribusi lifetime, bukan uji scale).

## BAGIAN 5 — Budget threshold (4 zona)
Budget harian campaign per akun saat ini: CBO Rp100rb untuk campaign "(baru)"; campaign lama Rp100–350rb (contoh Fikri Rp250rb).
Hubungan budget harian ↔ CPR: DATA TIDAK TERSEDIA (tidak ada seri harian). Proxy dari total spend ad set:

| Zona | Proxy (lifetime ad set) | CPR | Label |
|---|---|---|---|
| Comfort | ad set Rp1–5 jt | Rp35,1–35,4rb | ~ |
| Growth | ad set > Rp5 jt | Rp31,5rb | ~ (efek seleksi) |
| Aggressive | DATA TIDAK TERSEDIA | — | — |
| Dangerous | ad set ABO ≤ Rp50rb/hari | Rp79,5rb | ~ PROBABLE |

## BAGIAN 6–9 — Bid cap, cost cap, min ROAS, ASC
Semua ad set memakai **lowest cost** (tanpa cap). Bid/cost cap, min ROAS, ASC: **tidak pernah dipakai → DATA TIDAK TERSEDIA**.
Angka acuan jika nanti diuji (dari distribusi CPR): konservatif = P25 **Rp27.883**, normal = median **Rp39.285**, agresif = P75 **Rp54.912**.
Min ROAS tidak bisa dipakai (tidak ada nilai konversi).

## BAGIAN 10–12 — Refresh discovery
- Jenis refresh yang dipakai: creative baru (iklan baru tiap 2–7 hari; 3.072 iklan dibuat Sep, 1.894 Okt) dan campaign baru.
- Hasil: iklan baru Okt CPR Rp48rb vs winner lama Rp31rb. Refresh **tidak** memperbaiki CPR rata-rata. ~ PROBABLE.
- Refresh yang merusak winner: ad set winner yang di-PAUSE (contoh 7 hari terakhir: Allif Ramadhan "Desain 2 #5" Rp24rb/chat, Fikri "Desember - 4" Rp16rb/chat, Nida "Desember - Img 4" Rp29,5rb/chat — semua PAUSED). ✓ terlihat di data 7 hari.
- Kapan refresh: frequency ad set > 2,0 (CPR +43%). Hari/spend sebelum fatigue: DATA TIDAK TERSEDIA.

## BAGIAN 13 — Audience expansion
Broad belum diuji (selalu kota/provinsi). LLA: 1 ad set, CTR di bawah peer. Expansion = penambahan 25 kota radius 40 km (22 Okt) — hasil belum ada.

## BAGIAN 14 — Cannibalism deep discovery
| Level | Merugikan bila | Tidak berpengaruh bila | Budget berbahaya |
|---|---|---|---|
| Campaign/akun | 9 akun × kota sama × creative sama (hipotesis) | — | DATA TIDAK TERSEDIA |
| Ad set | — | — | DATA TIDAK TERSEDIA (overlap tidak tersedia di tool) |
| Ads | > 3 iklan: iklan ke-4+ hampir tidak dapat spend; 1 iklan ambil 55–68% | 1–2 iklan | semua budget |
| Creative | gambar sama dipakai di beberapa ad set satu campaign | gambar unik | — |

## BAGIAN 15 — Learning phase
Status learning ad set tidak ditarik → DATA TIDAK TERSEDIA. Yang paling mungkin merusak learning: pause/aktif ulang
ad set & ganti target berkali-kali (log 22 Okt: banyak edit lokasi/penempatan) — ? HIPOTESIS.
Cara menemukan: field `learning_stage_info` ad set aktif.

## BAGIAN 16 — CPR ceiling protection
Episode CPR harian tidak tersedia → batas dihitung dari distribusi lifetime CPR iklan (n = 3.322 iklan dengan chat):

| Batas | Nilai | Dasar |
|---|---|---|
| CPR baseline sehat | **Rp27.883 – Rp39.285** | P25 – median |
| CPR SAFE CEILING | **Rp54.912** | P75 — 75% iklan dengan chat ada di bawah ini |
| CPR DANGER CEILING | **Rp73.836** | P90 |
| CPR KILL TRIGGER | **> Rp73.836 lifetime**, atau **spend ≥ Rp78.570 (2× median CPR) dengan 0 chat** | P90; 2× median — 86% iklan yang sampai Rp75–100rb sudah dapat chat |

- "Jika CPR lifetime > Rp73.836 → KILL." ~ PROBABLE (hanya 10% iklan ber-chat seburuk ini).
- "Jika spend ≥ Rp78.570 dan 0 chat → KILL." ~ PROBABLE (iklan nol chat di Rp75–100rb tinggal 14%; di ≥ Rp100rb 4%).
- Pulih dari CPR tinggi: DATA TIDAK TERSEDIA (tidak ada seri harian).
- Aturan user yang sudah berlaku tetap jadi acuan eksekusi: hapus bila spend ≥ Rp35rb & 0 chat; hapus bila CPR > Rp50rb kecuali ≥ 5 chat.
  Data: Rp35rb < median biaya 1 chat (Rp39rb) → sebagian iklan dibunuh sebelum sempat dapat chat pertama. ? HIPOTESIS — perlu uji A/B ambang.

## BAGIAN 17 — Recovery pattern
DATA TIDAK TERSEDIA. Satu-satunya pola: akun AIni berhenti 6 Agu–8 Sep; iklan Sep CPR Rp61rb (lebih buruk dari Agu Rp36,8rb) → restart akun = CPR lebih mahal. ? HIPOTESIS — 1 kasus.

## BAGIAN 18 — Minimum viable test budget
| Item | Nilai |
|---|---|
| Median CPR historis | Rp39.285 |
| Durasi learning | DATA TIDAK TERSEDIA |
| Budget minimum di mana learning selesai | DATA TIDAK TERSEDIA |
| Minimum test budget/hari (per ad set) | **Rp39.285** (1× median) |
| Ideal test budget/hari | **Rp78.570** (2× median) |
| Budget 1 siklus testing | Rp78.570 × N hari (N = DATA TIDAK TERSEDIA; isi dari learning_stage_info) |

Struktur testing paling hemat yang terlihat berhasil: 1 campaign CBO | 3 ad set (per paket) | ≤3 iklan per ad set — sesuai pola "(baru)" 22 Okt.
Hari sampai chat pertama: DATA TIDAK TERSEDIA.

## BAGIAN 19–20 — Scaling formula, refresh formula, operating rules

**Scaling formula (10)** — semua ~ PROBABLE / ? HIPOTESIS karena belum ada histori scale:
1. Jika iklan ≥5 chat DAN CPR ≤ Rp39rb → salin iklan (source_ad_id) ke ad set lain di akun yang sama. ?
2. Jika ad set ≥10 chat/7 hari DAN CPR ≤ Rp39rb → naikkan budget campaign +20%, tunggu 3 hari. ?
3. Jika winner di akun A → pakai ulang post (object_story_id) di akun B (Page sama). ~ — post Rp33,7rb.
4. Jika akun CPR ≤ Rp37rb (Fifi, Diana) → akun pertama yang dinaikkan budget. ✓ (lifetime).
5. Jika akun CPR > Rp50rb (Allif) → tidak dinaikkan. ✓.
6. Jika paket 9 Hari → budget terbesar (CPR termurah di 9/9 akun dibanding 12 Hari). ✓.
7. Jika 12 Hari → budget kedua, target Rp47rb. ✓.
8. Jika Ramadhan → naikkan hanya di Allif & Diana (murah); akun lain uji dulu. ?
9. Jika scale → jangan tambah iklan baru ke ad set winner. ~.
10. Jika CPR naik > 20% setelah naik budget → kembalikan budget. ? (belum ada kasus).

**Refresh formula (10)**:
1. Frequency > 2,0 → buat ad set baru dengan creative baru, ad set lama tetap. ?
2. CTR < 0,42% & spend ≥ Rp50rb → ganti creative. ~.
3. Chat/klik < 8% di IG Feed → ganti creative. ?
4. Spend ≥ Rp78.570 & 0 chat → hapus (lihat Bagian 16). ~.
5. Jangan refresh winner yang CPR ≤ Rp39rb walau umur > 30 hari. ~ (Fikri Post bertahan 5 bulan).
6. Refresh pakai visual dasar winner (saudia_9_hari, januari_), bukan poster baru. ~.
7. Refresh maksimal 1 creative baru per ad set per minggu. ?
8. Jangan PAUSE ad set yang punya iklan CPR ≤ Rp30rb dalam 7 hari terakhir. ✓ (lihat Bagian 10–12).
9. Paket LAT tidak di-refresh — hentikan. ✓.
10. Setelah refresh, nilai iklan baru setelah ≥ Rp39rb spend. ~.

**Operating rules (30)** — lihat juga 02 Bagian 13:
1. Tidak ada scale tanpa ≥5 chat. 2. Tidak ada kill sebelum Rp39rb kecuali aturan user Rp35rb. 3. Kill di CPR > Rp73,8rb.
4. Safe ceiling Rp54,9rb. 5. Baseline Rp27,9–39,3rb. 6. Test budget Rp39–79rb/hari per ad set. 7. Maks 3 iklan per ad set.
8. CBO, bukan ABO kecil. 9. Optimasi CONVERSATIONS WA. 10. Penempatan default (IG + FB Story + WA Status + Threads).
11. Catat setiap kenaikan budget + CPR sebelum/sesudah. 12. Naik budget +20% per 3 hari (uji). 13. Tidak ada bid cap sampai ada histori.
14. Prioritas budget: Fifi > Diana > Hanif/AIni/Tira/Nida > Fikri > Irfan > Allif. 15. Paket 9 Hari > Ramadhan (Allif/Diana) > 12 Hari > Desember.
16. LAT stop. 17. Objective non-WA stop. 18. Jangan pause winner. 19. Frequency > 2,0 = refresh. 20. Satu perubahan besar per objek per hari.
21. Iklan baru jangan masuk ad set winner. 22. Gunakan post winner lintas akun. 23. Nilai wilayah dari closing CS. 24. Dayparting tidak perlu.
25. Jangan aktifkan semua akun dengan creative identik di kota sama sekaligus (uji). 26. Ad set < Rp250rb lifetime belum divonis.
27. Akun CPR naik > 20% bulan ke bulan → audit. 28. Iklan Okt dibandingkan dengan winner lama, bukan rata-rata. 29. Tracking closing per iklan (target). 30. Semua tindakan ke Meta hanya dengan konfirmasi user.

## BAGIAN 21 — Final report
- **DNA scaling:** akun ini scale secara horizontal (iklan/campaign/akun baru), bukan vertikal; hasilnya CPR iklan baru naik (Okt Rp48rb).
- **DNA refresh:** refresh terlalu sering & winner ikut di-pause.
- **CPR ceiling:** baseline Rp27,9–39,3rb · safe Rp54,9rb · danger Rp73,8rb · kill > Rp73,8rb atau Rp78,6rb tanpa chat.
- **Minimum test budget:** Rp39rb (min) – Rp79rb (ideal) per ad set per hari.
- **Terbukti:** konsentrasi winner, zona spend nol-chat. **Hipotesis:** semua formula scale. **Wajib diuji:** +20%/3 hari pada 1 akun (Fifi), ambang kill Rp35rb vs Rp50rb.
