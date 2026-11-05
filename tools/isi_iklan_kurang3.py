import sys, json, time, urllib.request, urllib.parse, urllib.error
sys.path.insert(0, "/home/khaeruddien/metaads/telegram")
import auto_rules as ar
S="/tmp/claude-1000/-home-khaeruddien/e1dfc6eb-eb6f-4725-8689-c623a384ccda/scratchpad/"
LOG=open(S+"isi_iklan.log","a")
def log(*a):
    m=" ".join(str(x) for x in a); print(m,flush=True); LOG.write(m+"\n"); LOG.flush()
def post(path,p):
    p={k:(v if isinstance(v,str) else json.dumps(v,ensure_ascii=False)) for k,v in p.items()}; p["access_token"]=ar.TOKEN
    for _ in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(f"{ar.GRAPH}/{path}",data=urllib.parse.urlencode(p).encode()),timeout=90) as r: return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            er=json.loads(e.read().decode())["error"]; msg=er.get("error_user_msg") or er.get("message")
            if "rate limit" in msg.lower() or "too many" in msg.lower(): time.sleep(35); continue
            return {"ERROR":msg}
        except Exception as e:
            time.sleep(5)
    return {"ERROR":"gagal/limit"}
IRF="1060984719243481"; TIRA="868364731529534"; H947="947788760498911"
POOL={
 "9":[("Desain 10 Januari #1","c9d52119db8bd263260fe3319b1f4746",IRF),("Desain 10 Januari #2","1876421815adf0bee3356b6708ad979a",IRF),("Desain 10 Januari #3","de1239752674a2cf4ccc5394ab558e6b",IRF),("Desain 10 Januari #4","de8fcb9f4613b59b047a73a725195e43",IRF),("Desain 7 Januari #1","f7a8b8feb2d1c1fd23314ce3ce61f7d5",IRF),("Desain 7 Januari #2","3bf4c1012340e97790e1844a0870448b",IRF),("Desain 7 Januari #3","56f81ba5cc52b2d0a615bd24bf211fa9",IRF),("Desain 7 Januari #4","07566885d144c8d631d3de1f26e62603",IRF),("Desain 7 Januari #5","077afea06c8234cf494c45f548a8f499",IRF),("Desain 4 Musim Dingin #1","5f19147a691faaa84ea7426662622e83",IRF),("Desain 4 Musim Dingin #2","6ddb24c9d82f674e0496e9320dfdfe31",IRF)],
 "12":[("Desain 3 12 Hari #1","b01865ed2afe0c80fe64f2a31e0b1904",IRF),("Desain 3 12 Hari #2","eb8283be6b32e68a98989cd5e739eefd",IRF),("Desain 3 12 Hari #3","69565d88a3d3455c040e7256c8ed4df5",TIRA),("Desain 3 12 Hari #4","2a9fb2def420bdbff954173d2a6aee36",IRF),("Desain 2 12 Hari #1","2b398b78bd35e8270efcac552f539b89",IRF),("Desain 2 12 Hari #2","3398a95afcd9fa3d47e5243e6b71e423",IRF),("Desain 2 12 Hari #3","59a43f4ec56059a5bd9f0f9bca0fd821",IRF),("Desain 2 12 Hari #4","d262258ba80dbc03291f005bd5c65b17",IRF),("Desain 2 12 Hari #5","de51b929ce5ce30d2647b9a193717960",IRF)],
 "R":[("Desain 3 Ramadhan #1","1b89d79c373660da473c70717ff5ad8a",IRF),("Desain 3 Ramadhan #2","319de1b8a5db6a0f6109538b71131d6e",IRF),("Desain 3 Ramadhan #3","cd6794a9f07e8caff3b1fac788279a1e",IRF),("Desain 3 Ramadhan #4","f8426a854ea121ba8d8f9dfdc3fe7b01",IRF),("Desain 3 Ramadhan #5","dcf6a819e82e1cc98dfd471cfc6904ff",TIRA),("Desain 3 Ramadhan #6","32ff78e3110c4a57eba6be383aaefc5a",TIRA),("Desain 2 Ramadhan #1","ff829074139e5b991284d6e8847c3337",IRF),("Desain 2 Ramadhan #2","2145ec23353c1d430e06243004d6cf8c",IRF),("Desain 2 Ramadhan #3","dd4722e254ac97d2c39fb72fe8d7e39e",TIRA),("Desain 2 Ramadhan #4","23a0d1d7ce7176dc2b3cd6c0fd643fb7",IRF),("Desain 2 Ramadhan #5","10b14ee6e87ff5791a4c19cbfb58492e",IRF)],
 "HAJI":[("Haji Desain 8 #1","004214c2847b0f4595257549a36568c8",H947),("Haji Desain 8 #2","1b532c28cdd50236a2e119eb38eb51c7",H947),("Haji Desain 8 #3","72897c381f9a292b7e8fefdbe5f5194a",H947),("Haji Desain 8 #4","d022f450d3de2b4351e014b3e40c6da8",H947),("Haji Desain 7 #1","b8322605b8b43fc10eeafd623c27937c",H947),("Haji Desain 7 #2","6b5cd4f06e665e29fc67177af0247210",H947),("Haji Desain 7 #3","2cdb97ff8229b75f3f2e18317548be21",H947),("Haji Desain 7 #4","07c2230da10d0830b859f1f555c2adf2",H947),("Haji Desain 6 #1","a804fb88928fad463221f24981a38986",H947),("Haji Desain 4 #1","9e871e2365363c8d542ba5927fd9422a",H947),("Haji Desain 4 #2","83dd8870ad5b83bb30392542a6081756",H947),("Haji Desain 4 #3","946fdd4713642148b6edf811ab08bd21",H947),("Haji Desain 4 #4","6cc11e4653d6eceabbf4155df6c974ef",H947)]}
pt=open("/home/khaeruddien/metaads/memory/primary-texts.md").read()
def sec(h):
    a=pt.index("```",pt.index(h))+4; return pt[a:pt.index("```",a)].rstrip("\n")
TXT={"9":sec("## 9 Hari Januari"),"12":sec("## 12 Hari Januari"),"R":sec("## Ramadhan"),"HAJI":sec("## Haji Plus")}
LBL={"9":"9 Hari Januari","12":"12 Hari Januari","R":"Ramadhan","HAJI":"Haji"}
IB=["Assalamualaikum info paket umrah Elharamain Wisata Terimakasih","Assalamualaikum info paket umrah 9 Hari Elharamain Wisata Terimakasih","Assalamualaikum info paket umrah 12 Hari Elharamain Wisata Terimakasih"]
def pwm(pk):
    ib=(["Assalamualaikum info paket umrah Ramadhan Elharamain Wisata Terimakasih"]+IB) if pk=="R" else IB
    return json.dumps({"type":"VISUAL_EDITOR","version":2,"landing_screen_type":"welcome_message","media_type":"text","text_format":{"customer_action_type":"ice_breakers","message":{"ice_breakers":[{"title":x} for x in ib],"quick_replies":[],"text":"Assalamualaikum Warahmatullahi Wabarakatuh, Elharamain Wisata Siap Melayani Anda"}}},ensure_ascii=False)
H=["7000+ Google Review ⭐️⭐️⭐️⭐️⭐️ (5.0)","✈️ Tiket Sudah Confirm, Jadwal Pasti"]
plan=json.load(open(S+"plan_isi.json"))
# hash dipakai per campaign (iklan lama) + batch
camp_used={}
for p in plan: camp_used.setdefault(p["camp_id"],set()).update(p["hashes"])
use_count={}
copied=set(); mcp=[]; hasil=[]
for p in plan:
    if not p["need"]: continue
    used=camp_used[p["camp_id"]]
    pool=[x for x in POOL[p["pk"]] if x[1] not in used] or POOL[p["pk"]]
    pool.sort(key=lambda x:use_count.get(x[1],0))
    pick=pool[:p["need"]]
    for n,(nm,h,src) in enumerate(pick):
        used.add(h); use_count[h]=use_count.get(h,0)+1
        if (p["akun_id"],h) not in copied and src!=p["akun_id"]:
            r=post(f"act_{p['akun_id']}/adimages",{"copy_from":{"source_account_id":src,"hash":h}}); copied.add((p["akun_id"],h))
            if "ERROR" in r: log("COPY GAGAL",p["akun"],nm,r)
        if p["pk"]=="HAJI":
            ld={"link":"https://api.whatsapp.com/send","message":TXT["HAJI"],"name":"✈️ Berangkat Haji Lebih Cepat, Amankan Porsi Haji Sekarang","description":"7000+ Google Review ⭐️⭐️⭐️⭐️⭐️ (5.0)","image_hash":h,"call_to_action":{"type":"WHATSAPP_MESSAGE","value":{"app_destination":"WHATSAPP","link":"https://api.whatsapp.com/send"}}}
        else:
            ld={"link":"https://api.whatsapp.com/send","message":TXT[p["pk"]],"name":H[n%2],"description":"Hotel Bintang 5 · Seat terbatas 45/keberangkatan","image_hash":h,"page_welcome_message":pwm(p["pk"]),"call_to_action":{"type":"WHATSAPP_MESSAGE","value":{"app_destination":"WHATSAPP","link":"https://api.whatsapp.com/send"}}}
        oss={"page_id":p["page"],"link_data":ld}
        if p["ig"]: oss["instagram_user_id"]=p["ig"]
        name=f'{LBL[p["pk"]]} | {nm} | baru'
        item={"akun":p["akun"],"akun_id":p["akun_id"],"campaign":p["campaign"],"adset":p["adset"],"adset_id":p["id"],"name":name,"creative":{"object_story_spec":oss}}
        if p["page"]=="637020022834756": mcp.append(item); log("MCP-ANTRI",p["akun"],p["adset"],name); continue
        r=post(f"act_{p['akun_id']}/ads",{"name":name,"adset_id":p["id"],"status":"PAUSED","creative":dict(item["creative"],contextual_multi_ads={"enroll_status":"OPT_OUT"})})
        if "ERROR" in r and "Halaman" in r["ERROR"]: mcp.append(item); log("MCP-ANTRI(izin)",p["akun"],p["adset"],name); continue
        item["hasil"]=r; hasil.append(item); log(p["akun"],"|",p["campaign"],"›",p["adset"],"|",name,"|",r); time.sleep(1.5)
json.dump(hasil,open(S+"isi_hasil.json","w"),ensure_ascii=False); json.dump(mcp,open(S+"isi_mcp.json","w"),ensure_ascii=False)
log("SELESAI graph:",sum(1 for x in hasil if "id" in x["hasil"]),"ok,",sum(1 for x in hasil if "ERROR" in x["hasil"]),"gagal | antre MCP:",len(mcp))
