import pandas as pd, json, glob, os
S=os.path.dirname(os.path.abspath(__file__)); REPO='/home/user/top-keywords'
CSV={'BR':'br','DE':'de','ES':'es','ID':'id','JP':'jp','JP_EN':'jp_en','MX':'mx','PL':'pl','TR':'tr'}
m=pd.read_csv(os.path.join(S,'ocr_matched.csv'))
out=[]
for f,g in m.groupby('file',sort=True):
    mk=g.market.iloc[0]
    kws=list(pd.read_csv(os.path.join(REPO,CSV[mk]+'.csv'))['Keyword'])
    idx={k:i for i,k in enumerate(kws)}
    g=g.sort_values('y')
    ys=list(g.y); segs=1+sum(1 for a,b in zip(ys,ys[1:]) if b-a>60)
    ci=[idx.get(k) for k in g.keyword if k in idx]
    lo,hi=min(ci),max(ci)
    covered=set(ci)
    missing=[i for i in range(lo,hi+1) if i not in covered]
    out.append(dict(screenshot=f,market=mk,rows_extracted=len(g),capture_segments=segs,first_keyword=kws[lo],last_keyword=kws[hi],
        csv_range_size=hi-lo+1,csv_keywords_in_range_not_visible=len(missing),
        rows_with_volume=int((g.vol.notna()&(g.vol!='')).sum()),rows_volume_dash=int((g.vol.isna()|(g.vol=='')).sum()),
        rows_order_inferred=int((g.status=='order_inferred').sum()),rows_unmatched=int((g.status=='unmatched').sum()),
        location='', language='All languages', network='Google', date_range='Sep 2025 – Aug 2026', currency='INR (₹) bids'))
o=pd.DataFrame(out)
LOC={'BR':'Brazil','DE':'Germany','ES':'Spain','ID':'Indonesia','JP':'Japan','JP_EN':'Japan','MX':'Mexico','PL':'Poland'}
o['location']=o.market.map(LOC)
o.to_csv(os.path.join(S,'screenshot_audit.csv'),index=False)
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',40)
print(o.drop(columns=['language','network','date_range','currency']).to_string())
