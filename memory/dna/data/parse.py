import json,sys,csv
def num(v):
    if v is None: return 0.0
    if isinstance(v,dict):
        if 'values' in v:
            return sum(float(x['value']) for x in v['values'] if x['value'] not in ('Not available',))
        v=v.get('value')
    try: return float(str(v).replace(',','.').replace('%',''))
    except: return 0.0
def load(path):
    d=json.load(open(path)); rows=json.loads(d['ad_entities']); return rows
if __name__=='__main__':
    rows=load(sys.argv[1]); print(len(rows))
    print(json.dumps(rows[0])[:800])
