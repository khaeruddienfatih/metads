# Prosedur cek tiap jam: nyalakan lagi ad set yang dimatikan auto rule

Perintah user (30 Okt 2026): "aktipan adset cek tiap jam kamu cek yang cpr di bawah 30rb dan terkena off oleh auto rules saya".
User memilih CPR dihitung dari **data hari ini**.

## Akun yang dicek (14)

Diana 1076195694707828 · Tira 868364731529534 · Nida 1019832712800468 · Hanif 482252744648260 ·
Allif 4678183395742010 · Fikri 1676215979752437 · AIni 814396810761205 · Irfan 1060984719243481 ·
Fifi 521083143750270 · Elharamain Haji 947788760498911 · Haji 2 1032468828178224 ·
Haji 3 794403715776985 · Haji 4 1526562231314028 · haji 1050343302646341

## Langkah per akun

1. `ads_account_get_activity_logs` — `event_category: status`, `start_time` = hari ini 00:00 WIB
   (`YYYY-MM-DDT00:00:00+07:00`), `limit` 200.
   Ambil entri `event_type` "Ad set status updated" yang `extra_data` punya `rule_info` dan
   `new_value` "Inactive" (dimatikan auto rule). Catat `object_id`, nama rule, jam.
2. Ad set kandidat → `ads_get_ad_entities` level `adset`, `object_ids`, `date_preset: today`,
   field `name, status, effective_status, amount_spent, results, cost_per_result, campaign_id`.
3. Nyalakan HANYA jika semua terpenuhi:
   - status sekarang masih PAUSED/tidak aktif (belum dinyalakan orang lain);
   - campaign-nya ACTIVE (jangan nyalakan ad set di campaign yang di-PAUSE);
   - chat WA hari ini ≥ 1 dan biaya per chat hari ini (spend ÷ chat) **< Rp30.000**;
   - **(30 Okt, user "2 iya") CPR 3 hari terakhir juga < Rp50.000**: ambil lagi dengan
     `date_preset: last_3d` (3 hari sebelum hari ini). Lolos jika chat ≥ 1 dan spend ÷ chat < Rp50.000,
     atau spend 3 hari < Rp35.000 (data masih sedikit). Gagal jika 0 chat dengan spend ≥ Rp35.000;
   - ad set ini belum dinyalakan ≥ 2 kali hari ini oleh prosedur ini (cek log aktivitas: entri
     "Ad set status updated" dengan `application_name` "ads MCP server" Inactive→Active hari ini).
     Kalau rule terus mematikannya, berhenti di 2 kali supaya tidak bolak-balik.
4. Nyalakan: `ads_activate_entity` `object_ids: [adset_id]`, `publish_as_active: true`.
   Kalau ditolak "has no staged changes in the draft" (akun mode draft seperti Diana/Nida), ulangi
   dengan `entity_type: ad_set` + `entity_id` tanpa `object_ids`. Lalu verifikasi dengan
   `ads_get_ad_entities` `object_ids`.
5. Jangan ubah budget, targeting, iklan, atau apa pun selain status ad set itu.

## Bagian B — matikan ad set boros hari ini (30 Okt, perintah user)

Perintah user: "adset aturan perhari matikan adset yang habis 25ribu tapi tidak ada chat".

1. Per akun: `ads_get_ad_entities` level `adset`, filter `effective_status IN [ACTIVE]`, `date_preset: today`,
   field `name, campaign_name, optimization_goal, amount_spent, results, cost_per_result`.
2. PAUSE jika: spend hari ini **≥ Rp25.000** dan **0 chat WA hari ini** (messaging conversation started;
   kosong/"Not available" = 0).
3. Kecualikan ad set yang hasilnya bukan chat WA (mis. Haji 4 campaign pixel/add-to-cart: optimization_goal
   bukan CONVERSATIONS) — jangan di-pause.
4. Pause: `ads_update_entity` `ad_account_id`, `entity_id` = ad set, `fields {"status":"PAUSED"}`. Verifikasi.
   Ubah status saja, jangan sentuh budget/targeting/iklan.
5. Bagian A tidak akan menyalakannya lagi hari itu (syarat A butuh ≥1 chat & CPR < Rp30rb). Besok (data
   hari baru) ad set ini TIDAK otomatis dinyalakan — hanya ad set yang dimatikan auto rule yang diproses Bagian A.

## Pelaporan

- Kalau ada ad set yang dinyalakan (A) atau di-PAUSE (B): tambah entri di akhir `memory/chat-log.md`
  (`### YYYY-MM-DD HH:MM — cek tiap jam: ad set dinyalakan lagi`) berisi akun, ID, nama, rule,
  chat & CPR hari ini; lalu commit, `git pull origin main`, `git push origin main`.
- Kalau tidak ada yang memenuhi syarat: tidak perlu menulis log/commit.

Meta Ads: `client_conversation_id` `Hn4fT8qLz2WcP7xR1bVk`.
