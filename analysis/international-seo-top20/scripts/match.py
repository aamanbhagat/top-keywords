import json, glob, os, re, sys
import pandas as pd
from rapidfuzz import process, fuzz
S=os.path.dirname(os.path.abspath(__file__))
REPO='/home/user/top-keywords'
CSV={'BR':'br','DE':'de','ES':'es','ID':'id','JP':'jp','JP_EN':'jp_en','MX':'mx','PL':'pl','TR':'tr'}
VOLS=['0 – 10','10 – 100','100 – 1K','1K – 10K','10K – 100K','100K – 1M','1M – 10M']
def norm_vol(s):
    t=s.replace(' ','').replace('–','-').replace('—','-').upper().replace('O','0')
    m=re.match(r'^(\d+K?|\d+M?)-(\d+K?M?)',t)
    if not m: return ''
    a,b=m.group(1),m.group(2)
    for v in VOLS:
        va,vb=v.replace(' ','').split('–')
        if a==va and b.startswith(vb): return v
    return 'UNPARSED:'+s
def norm_pct(s):
    t=s.replace(' ','')
    if not t: return ''
    if re.match(r'^\+?(00|oo|co|∞)%?$',t,re.I): return '+∞'
    m=re.match(r'^([+-]?)([\d,]+)%',t)
    if m: return f"{m.group(1)}{m.group(2)}%"
    return 'UNPARSED:'+s
def norm_comp(s):
    for c in ('Low','Medium','High'):
        if c.lower() in s.lower(): return c
    return ''
def norm_bid(s):
    t=s.replace(',','').replace(' ','')
    m=re.search(r'(\d+\.\d\d)',t)
    return float(m.group(1)) if m else None
def clean_kw(s):
    s=s.strip()
    s=re.sub(r'\s+',' ',s)
    return s
rows=[]
import numpy as np
def kp_norm(k):
    # Keyword Planner displays keywords with punctuation such as - . / replaced by spaces
    return re.sub(r'\s+',' ',re.sub(r'[-./_]',' ',k.lower())).strip()
def mk(r,m,k,kw,csvkw,score,status,amb):
    return dict(file=r['file'],market=m,row=r['idx'],y=r['y'],ocr_kw=k,keyword=kw,csv_keyword=csvkw,match_score=round(float(score),1),status=status,trunc_ambiguous=bool(amb),
        vol=norm_vol(r['vol']),vol_raw=r['vol'],m3=norm_pct(r['m3']),yoy=norm_pct(r['yoy']),comp=norm_comp(r['comp']),comp_raw=r['comp'],
        bid_lo=norm_bid(r['bidlo']),bid_hi=norm_bid(r['bidhi']),bid_lo_raw=r['bidlo'],bid_hi_raw=r['bidhi'])
def data_rows(d):
    out=[]
    for r in d:
        k=clean_kw(r['kw'])
        if k.lower().startswith('keyword') and 'monthly' in r['vol'].lower(): continue
        if not k and not r['vol']: continue
        out.append((r,k))
    return out
for f in sorted(glob.glob(os.path.join(S,'ocr','*.png.json'))):
    d=json.load(open(f))
    m=d[0]['market'] if d else None
    kws=list(pd.read_csv(os.path.join(REPO,CSV[m]+'.csv'))['Keyword'])
    dr=data_rows(d)
    if m=='JP':
        C=[k.replace(' ','').lower() for k in kws]
        res=[]
        for r,k in dr:
            trunc=k.endswith('...') or k.endswith('…')
            q=k.rstrip('.…').replace(' ','').lower()
            sc=np.array([fuzz.ratio(q,c[:len(q)]) if trunc else fuzz.ratio(q,c) for c in C])
            i=int(sc.argmax()); res.append([i,float(sc[i]),'matched' if sc[i]>=70 else None])
        # fill gaps by CSV order when neighbours are confident and the gap sizes agree
        idx=[t for t in range(len(res)) if res[t][2]]
        for x,y in zip(idx,idx[1:]):
            gr=y-x-1; gc=res[y][0]-res[x][0]-1
            if gr>0 and gr==gc:
                for t in range(1,gr+1): res[x+t][0]=res[x][0]+t; res[x+t][2]='order_inferred'
        for t,(r,k) in enumerate(dr):
            i,sc,st=res[t]
            if st is None: rows.append(mk(r,m,k,k,'',0,'unmatched',False))
            else: rows.append(mk(r,m,k,kws[i],kws[i],sc,st,False))
        continue
    low=[kp_norm(k) for k in kws]
    p=-1; used=set()
    for r,k in dr:
        trunc=k.endswith('...') or k.endswith('…')
        q=kp_norm(k.rstrip('.…').strip())
        sc=np.array([fuzz.ratio(q,c[:len(q)]) if trunc else fuzz.ratio(q,c) for c in low])
        best=sc.max()
        cand=[i for i in np.where(sc>=best-3)[0] if i not in used]
        if not cand: cand=list(np.where(sc>=best-3)[0])
        after=[i for i in cand if i>p]
        i=min(after) if after else min(cand,key=lambda i:abs(i-p))
        status='matched' if sc[i]>=85 else 'unmatched'
        ambiguous=trunc and (sc>=best-3).sum()>1
        used.add(i)
        if status=='matched': p=max(p,i)
        rows.append(mk(r,m,k,kws[i] if status=='matched' else k,kws[i],sc[i],status,ambiguous))
df=pd.DataFrame(rows)
df.to_csv(os.path.join(S,'ocr_matched.csv'),index=False)
print(df.groupby('market').agg(n=('keyword','size'),uniq=('keyword','nunique'),lowmatch=('status',lambda s:(s!='matched').sum()),amb=('trunc_ambiguous','sum')))
print(df['vol'].value_counts(dropna=False).head(20))
print(df[df.vol.str.startswith('UNPARSED')][['file','ocr_kw','vol_raw']].head(20))
print(df[df.m3.str.startswith('UNPARSED')|df.yoy.str.startswith('UNPARSED')][['file','ocr_kw','m3','yoy']].head(20))
