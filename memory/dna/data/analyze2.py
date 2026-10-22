import json,glob,pickle
from collections import defaultdict
from parse import num
from analyze import isWA, rp, q
P=print
def rows(kind):
    out={}
    for f in glob.glob('bd/*_%s.json'%kind):
        a=f.split('/')[-1].split('_')[0]; out[a]=[x for x in json.loads(json.load(open(f))['ad_entities']) if isWA(x)]
    return out
def agg(rs,key,minspend=0):
    G=defaultdict(lambda:[0,0,0,0])
    for x in rs:
        k=key(x); g=G[k]; g[0]+=num(x['amount_spent']); g[1]+=num(x['results']); g[2]+=num(x['impressions']); g[3]+=num(x.get('link_click'))
    return G
def show(G,sort=None,minspend=0):
    for k,g in (sorted(G.items()) if sort is None else sorted(G.items(),key=sort)):
        if g[0]<minspend: continue
        P(' ',k,'spend',rp(g[0]),'chat',int(g[1]),'CPR',rp(g[0]/g[1]) if g[1] else '-','CPM',rp(g[0]/g[2]*1000) if g[2] else '-','CTR %.2f'%(g[3]/g[2]*100 if g[2] else 0),'chat/klik %.1f'%(g[1]/g[3]*100 if g[3] else 0))
H=rows('hour'); P('=== JAM (90 hari, campaign WA, semua akun digabung) ===')
allh=[x for v in H.values() for x in v]
G=agg(allh,lambda x:x['hourly_stats_aggregated_by_advertiser_time_zone'][:2]); show(G)
P('per akun jam CPR terbaik/terburuk:')
for a,v in sorted(H.items()):
    G=agg(v,lambda x:x['hourly_stats_aggregated_by_advertiser_time_zone'][:2]); L=[(k,g[0]/g[1]) for k,g in G.items() if g[1]>=10]
    L.sort(key=lambda t:t[1]); P(' ',a,'best',[(k,rp(c)) for k,c in L[:3]],'worst',[(k,rp(c)) for k,c in L[-3:]])
# blocks
P('blok jam:')
blk=lambda h:'00-04' if h<5 else '05-09' if h<10 else '10-14' if h<15 else '15-19' if h<20 else '20-23'
G=agg(allh,lambda x:blk(int(x['hourly_stats_aggregated_by_advertiser_time_zone'][:2]))); show(G)
PL=rows('place'); P('\n=== PENEMPATAN (90 hari; AIni,Tira,Irfan,Nida,Diana,Hanif) ===')
allp=[x for v in PL.values() for x in v]
G=agg(allp,lambda x:x['publisher_platform']+'/'+x['platform_position']); show(G,sort=lambda t:-t[1][0],minspend=50000)
P('per akun:')
for a,v in sorted(PL.items()):
    G=agg(v,lambda x:x['publisher_platform']+'/'+x['platform_position']); P(' ',a,{k:(rp(g[0]/g[1]) if g[1] else '-',int(g[1])) for k,g in sorted(G.items(),key=lambda t:-t[1][0]) if g[0]>100000})
# inline placement
P('inline (Allif/Fifi/Fikri):')
G=defaultdict(lambda:[0,0])
for l in open('place_inline.tsv'):
    if l.startswith('#'): continue
    a,c,p,s,r=l.split('\t'); G[p][0]+=float(s); G[p][1]+=float(r)
for k,g in sorted(G.items(),key=lambda t:-t[1][0]): P(' ',k,rp(g[0]),int(g[1]),rp(g[0]/g[1]) if g[1] else '-')
AG=rows('agegender'); P('\n=== USIA x GENDER (90 hari, sampel 1000 baris/akun) ===')
alla=[x for v in AG.values() for x in v]
show(agg(alla,lambda x:x['gender']))
show(agg(alla,lambda x:x['age']))
show(agg(alla,lambda x:x['age']+'/'+x['gender']),sort=lambda t:-t[1][0],minspend=500000)
RG=rows('region'); P('\n=== WILAYAH (90 hari; AIni,Tira,Fifi,Fikri,Hanif,Nida) ===')
allr=[x for v in RG.values() for x in v]
show(agg(allr,lambda x:x['region']),sort=lambda t:-t[1][0],minspend=1000000)
# ADSET
AS=rows('adset'); P('\n=== AD SET (lifetime) ===')
alls=[x for v in AS.values() for x in v]
for a,v in AS.items():
    for x in v: x['_acc']=a
P('n adset WA',len(alls))
show(agg(alls,lambda x:x.get('optimization_goal')))
show(agg(alls,lambda x:x.get('destination_type')))
def bud(x):
    b=num(x.get('daily_budget'))
    if not b: return 'CBO/none'
    for t in [50e3,75e3,100e3,150e3,200e3,300e3,500e3]:
        if b<=t: return '<=%dk'%(t/1000)
    return '>500k'
P('budget harian ad set:'); show(agg(alls,bud))
def fq(x):
    i=num(x['impressions']); r=num(x['reach']); f=i/r if r else 0
    for t in [1.1,1.2,1.4,1.6,2,3]:
        if f<=t: return 'freq<=%.1f'%t
    return 'freq>3'
P('frekuensi ad set (spend>=100k):'); show(agg([x for x in alls if num(x['amount_spent'])>=100000],fq))
def sp(x):
    s=num(x['amount_spent'])
    for t in [100e3,250e3,500e3,1e6,2e6,5e6]:
        if s<=t: return 'spend<=%s'%rp(t)
    return 'spend>5jt'
P('total spend ad set:'); show(agg(alls,sp))
# ads per adset & concentration from ad data
M=pickle.load(open('M.pkl','rb'))
by=defaultdict(list)
for x,m in M: by[(x['_acc'],x.get('campaign_name'),x.get('adset_name'),x['created_time'][:10])].append(m)
G=defaultdict(lambda:[0,0,0,[]])
for k,ms in by.items():
    n=len(ms); s=sum(m['s'] for m in ms); r=sum(m['r'] for m in ms)
    if s<100000: continue
    top=max(m['s'] for m in ms)/s
    key='%d iklan'%n if n<=6 else '7+ iklan'
    g=G[key]; g[0]+=s; g[1]+=r; g[2]+=1; g[3].append(top)
P('\n=== JUMLAH IKLAN PER AD SET (grup adset+tgl buat, spend>=100rb) ===')
for k in sorted(G): g=G[k]; P(' ',k,'grup',g[2],'CPR',rp(g[0]/g[1]) if g[1] else '-','median porsi spend iklan teratas %.0f%%'%(q(g[3],.5)*100))
