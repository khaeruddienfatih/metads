import json,glob,re,statistics as st
from collections import defaultdict
from parse import num
WA='messaging_conversation_started'
def isWA(x): r=x.get('results') or {}; return isinstance(r,dict) and WA in (r.get('indicator') or '')
def load(pat):
    out=defaultdict(dict)
    for f in glob.glob(pat):
        acc=f.split('/')[-1].split('_')[0]
        for x in json.loads(json.load(open(f))['ad_entities']):
            out[acc][x.get('id','')+str(x.get('hourly_stats_aggregated_by_advertiser_time_zone',''))+str(x.get('publisher_platform',''))+str(x.get('platform_position',''))+str(x.get('age',''))+str(x.get('gender',''))+str(x.get('region',''))]=x
    return {a:list(v.values()) for a,v in out.items()}
def q(v,p):
    v=sorted(v); 
    if not v: return 0
    k=(len(v)-1)*p; f=int(k); c=min(f+1,len(v)-1); return v[f]+(v[c]-v[f])*(k-f)
def rp(x): return 'Rp{:,.0f}'.format(x).replace(',','.')
P=print
ads=load('raw/*.txt')
P('=== AD LEVEL (lifetime, iklan dengan spend>0, objective WA) ===')
allwa=[]
for a in sorted(ads):
    rows=ads[a]; wa=[x for x in rows if isWA(x) and num(x['amount_spent'])>0]
    for x in wa: x['_acc']=a
    allwa+=wa
    S=sum(num(x['amount_spent']) for x in wa); R=sum(num(x['results']) for x in wa)
    oth=sum(num(x['amount_spent']) for x in rows if not isWA(x))
    dts=sorted(x['created_time'][:10] for x in wa)
    P(a,'ads_total',len(rows),'ads_WA',len(wa),'spendWA',rp(S),'chat',int(R),'CPR',rp(S/R if R else 0),'spend_nonWA',rp(oth),'WA from',dts[0] if dts else '-', 'to',dts[-1] if dts else '-')
S=sum(num(x['amount_spent']) for x in allwa); R=sum(num(x['results']) for x in allwa)
P('TOTAL WA ads',len(allwa),'spend',rp(S),'chat',int(R),'CPR',rp(S/R))
# distributions among ads with spend>=20000
def met(x):
    s=num(x['amount_spent']); r=num(x['results']); i=num(x['impressions']); c=num(x['link_click']); rc=num(x['reach'])
    return dict(s=s,r=r,i=i,c=c,cpr=s/r if r else None,ctr=c/i*100 if i else 0,cpm=s/i*1000 if i else 0,cvr=r/c*100 if c else None,freq=i/rc if rc else 0)
M=[(x,met(x)) for x in allwa]
big=[m for x,m in M if m['s']>=20000]
P('\n--- Distribusi per iklan (spend>=20rb, n=%d) P25/Med/P75/P90 ---'%len(big))
for k in ['s','r','cpr','ctr','cpm','cvr','freq']:
    v=[m[k] for m in big if m[k] is not None]
    P(k, len(v), [round(q(v,p),2) for p in (.25,.5,.75,.9)])
P('zero-result share among spend>=20k:', round(sum(1 for m in big if m['r']==0)/len(big)*100,1),'%')
# spend bucket vs zero-result & CPR
P('\n--- Spend bucket iklan vs hasil ---')
B=[0,10e3,20e3,35e3,50e3,75e3,100e3,150e3,250e3,500e3,1e9]
for lo,hi in zip(B,B[1:]):
    g=[m for x,m in M if lo<=m['s']<hi]
    if not g: continue
    s=sum(m['s'] for m in g); r=sum(m['r'] for m in g)
    P(f'{rp(lo)}-{rp(hi)} n={len(g)} zero={sum(1 for m in g if m["r"]==0)} ({sum(1 for m in g if m["r"]==0)/len(g)*100:.0f}%) CPR={rp(s/r) if r else "-"} medCTR={q([m["ctr"] for m in g],.5):.2f}')
# first chat cost: for ads with r==1.., cpr dist
# product by name
def prod(n):
    n=n.lower()
    for k,v in [('ramadhan','Ramadhan'),('ramadan','Ramadhan'),('12 hari','12 Hari Januari'),('12_hari','12 Hari Januari'),('12 januari','12 Hari Januari'),('9 hari','9 Hari Januari'),('januari','9 Hari Januari'),('9_hari','Desember'),('desember','Desember'),('saudia','Desember'),('akhir tahun','LAT'),('lat','LAT'),('riyad','Riyadh Air'),('november','Riyadh Air'),('10_hari','Riyadh Air'),('qatar','Qatar'),('turki','Turki'),('haji','Haji')]:
        if k in n: return v
    return 'Lain/umum'
P('\n--- Per paket (dari nama iklan+adset+campaign) ---')
G=defaultdict(lambda:[0,0,0,0,0])
for x,m in M:
    p=prod(x['name']+' '+x.get('adset_name','')+' '+x.get('campaign_name',''))
    g=G[p]; g[0]+=m['s']; g[1]+=m['r']; g[2]+=1; g[3]+=m['c']; g[4]+=m['i']
for p,g in sorted(G.items(),key=lambda t:-t[1][0]):
    P(p,'ads',g[2],'spend',rp(g[0]),'chat',int(g[1]),'CPR',rp(g[0]/g[1]) if g[1] else '-','CTR',round(g[3]/g[4]*100,2) if g[4] else 0,'chat/klik',round(g[1]/g[3]*100,1) if g[3] else 0)
# creative family
def fam(n):
    n=n.lower()
    m=re.search(r'desain[ _]?(\d+)',n)
    if 'premium' in n: return 'Desain Premium'
    if 'musim dingin' in n: return 'Desain 4 Musim Dingin'
    if m: return 'Desain '+m.group(1)
    for k in ['saudia_9_hari','januari_','12_hari_januari','10_hari_riyad','design_14','hajj','post','testi','video']:
        if k in n: return k
    return 'lain'
P('\n--- Per keluarga creative (nama iklan) ---')
G=defaultdict(lambda:[0,0,0,0,0])
for x,m in M:
    f=fam(x['name']); g=G[f]; g[0]+=m['s']; g[1]+=m['r']; g[2]+=1; g[3]+=m['c']; g[4]+=m['i']
for p,g in sorted(G.items(),key=lambda t:-t[1][0]):
    if g[0]<200000: continue
    P(p,'ads',g[2],'spend',rp(g[0]),'chat',int(g[1]),'CPR',rp(g[0]/g[1]) if g[1] else '-','CTR',round(g[3]/g[4]*100,2) if g[4] else 0,'chat/klik',round(g[1]/g[3]*100,1) if g[3] else 0)
# video vs image
P('\n--- Video vs gambar ---')
for lab,cond in [('video',lambda x:num(x.get('video_play_actions'))>0),('gambar',lambda x:not num(x.get('video_play_actions')))]:
    g=[(x,m) for x,m in M if cond(x)]; s=sum(m['s'] for x,m in g); r=sum(m['r'] for x,m in g)
    P(lab,len(g),rp(s),int(r),rp(s/r) if r else '-')
vids=[(x,m) for x,m in M if num(x.get('video_play_actions'))>0 and m['s']>=50000]
if vids:
    hr=[(num(x.get('video_p25_watched_actions'))/num(x['impressions'])*100 if num(x['impressions']) else 0,m['cpr']) for x,m in vids]
    P('video spend>=50k n',len(vids),'median p25/impr %',round(q([h for h,_ in hr],.5),2))
# CTR vs CPR correlation & CPM vs CPR, freq vs CPR (ads spend>=50k with r>0)
import math
def corr(a,b):
    ma,mb=st.mean(a),st.mean(b); sa=math.sqrt(sum((x-ma)**2 for x in a)); sb=math.sqrt(sum((y-mb)**2 for y in b)); 
    return sum((x-ma)*(y-mb) for x,y in zip(a,b))/(sa*sb) if sa and sb else 0
g=[m for x,m in M if m['s']>=50000 and m['r']>0 and m['c']>0]
P('\n--- Korelasi (iklan spend>=50rb & chat>0, n=%d) terhadap CPR ---'%len(g))
for k in ['ctr','cpm','cvr','freq','s']:
    P(k, round(corr([m[k] for m in g],[m['cpr'] for m in g]),3))
# quartile analysis: CPR by CVR quartile and CPM quartile
for k in ['cvr','ctr','cpm','freq']:
    v=sorted(g,key=lambda m:m[k]); n=len(v); out=[]
    for i in range(4):
        c=v[i*n//4:(i+1)*n//4]; s=sum(m['s'] for m in c); r=sum(m['r'] for m in c)
        out.append(f"Q{i+1}[{c[0][k]:.2f}-{c[-1][k]:.2f}] CPR {rp(s/r)}")
    P(k,' | '.join(out))
# by month created
P('\n--- Per bulan iklan dibuat ---')
G=defaultdict(lambda:[0,0,0])
for x,m in M:
    k=x['created_time'][:7]; G[k][0]+=m['s']; G[k][1]+=m['r']; G[k][2]+=1
for k in sorted(G): g=G[k]; P(k,'ads',g[2],rp(g[0]),int(g[1]),rp(g[0]/g[1]) if g[1] else '-')
# status
P('\n--- Status iklan WA ---')
G=defaultdict(lambda:[0,0,0])
for x,m in M:
    k=x['effective_status']; G[k][0]+=m['s']; G[k][1]+=m['r']; G[k][2]+=1
for k,g in G.items(): P(k,g[2],rp(g[0]),int(g[1]),rp(g[0]/g[1]) if g[1] else '-')
# top / bottom ads
P('\n--- TOP 25 iklan (chat>=5) CPR terendah ---')
t=sorted([(x,m) for x,m in M if m['r']>=5],key=lambda t:t[1]['cpr'])
for x,m in t[:25]: P(x['_acc'],'|',x['name'][:60],'|',x.get('adset_name','')[:20],'| spend',rp(m['s']),'chat',int(m['r']),'CPR',rp(m['cpr']),'CTR %.2f'%m['ctr'],'chat/klik %.0f'%(m['cvr'] or 0))
P('\n--- TOP 15 iklan by chat ---')
for x,m in sorted(M,key=lambda t:-t[1]['r'])[:15]: P(x['_acc'],'|',x['name'][:60],'| spend',rp(m['s']),'chat',int(m['r']),'CPR',rp(m['cpr'] or 0),'CTR %.2f'%m['ctr'],'freq %.2f'%m['freq'],x['created_time'][:10])
P('\n--- BOTTOM 20 (spend tertinggi dengan chat 0-1) ---')
for x,m in sorted([t for t in M if t[1]['r']<=1],key=lambda t:-t[1]['s'])[:20]: P(x['_acc'],'|',x['name'][:60],'| spend',rp(m['s']),'chat',int(m['r']),'CTR %.2f'%m['ctr'],'CPM',rp(m['cpm']))
import pickle; pickle.dump([(x,m) for x,m in M],open('M.pkl','wb'))
