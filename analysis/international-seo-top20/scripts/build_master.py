import pandas as pd, numpy as np, os
S=os.path.dirname(os.path.abspath(__file__)); REPO='/home/user/top-keywords'
CSV={'BR':'br','DE':'de','ES':'es','ID':'id','JP':'jp','JP_EN':'jp_en','MX':'mx','PL':'pl','TR':'tr'}
LANG={'BR':'Portuguese (pt-BR)','DE':'German','ES':'Spanish (es-ES)','ID':'Indonesian','JP':'Japanese','JP_EN':'English (Japan-related)','MX':'Spanish (es-MX)','PL':'Polish','TR':'Turkish'}
COUNTRY={'BR':'Brazil','DE':'Germany','ES':'Spain','ID':'Indonesia','JP':'Japan','JP_EN':'Japan (location) - English queries','MX':'Mexico','PL':'Poland','TR':'Turkey'}
VOLRANK={'0 – 10':0,'10 – 100':1,'100 – 1K':2,'1K – 10K':3,'10K – 100K':4,'100K – 1M':5,'1M – 10M':6}
m=pd.read_csv(os.path.join(S,'ocr_matched.csv')).fillna('')
m=m[m.status!='unmatched']
kov_path=os.path.join(S,'volcheck','keyword_overrides.csv')
if os.path.exists(kov_path):
    for o in pd.read_csv(kov_path).itertuples():
        idx=m[(m.file==o.file)&(m.y==o.y)].index
        m.loc[idx,'keyword']=o.new_keyword; m.loc[idx,'status']='matched (visually corrected)'
    print('applied keyword overrides')
# apply visually verified corrections (volcheck workflow) if present
ov_path=os.path.join(S,'volcheck','overrides.csv')
if os.path.exists(ov_path):
    ov=pd.read_csv(ov_path).fillna('')
    FIELD={'vol':'vol','3m':'m3','yoy':'yoy','comp':'comp','bid_low':'bid_lo','bid_high':'bid_hi'}
    for o in ov.itertuples():
        col=FIELD.get(o.field)
        if not col: continue
        val=str(o.value).strip()
        if val in ('—','-','–'): val=''
        if col in ('bid_lo','bid_hi'):
            val=float(val.replace('₹','').replace(',','')) if val else float('nan')
        idx=m[(m.market==o.market)&(m.keyword==o.keyword)].index
        m.loc[idx,col]=val
        m.loc[idx,'corrected']='visually corrected: '+o.field
    print('applied overrides:',len(ov))
# per keyword: consolidate duplicates (overlapping screenshots)
def consolidate(g):
    g=g.copy()
    vols=set(v for v in g.vol if v)
    r=g.iloc[0].to_dict()
    # prefer row with a volume value
    gv=g[g.vol!='']
    if len(gv): r=gv.iloc[0].to_dict()
    r['n_obs']=len(g); r['vol_conflict']=len(vols)>1
    r['files']='; '.join(sorted(set(g.file)))
    return pd.Series(r)
c=m.groupby(['market','keyword'],sort=False).apply(consolidate,include_groups=False).reset_index()
rows=[]
for mk,f in CSV.items():
    kw=pd.read_csv(os.path.join(REPO,f+'.csv'))
    for _,k in kw.iterrows():
        rows.append(dict(market=mk,country=COUNTRY[mk],language=LANG[mk],source_file=f+'.csv',keyword=k['Keyword'],campaign=k['Campaign'],ad_group=k['Ad group']))
base=pd.DataFrame(rows)
if 'corrected' not in c.columns: c['corrected']=''
cc=c.rename(columns={'files':'screenshot_files'})[['market','keyword','screenshot_files','vol','m3','yoy','comp','bid_lo','bid_hi','status','match_score','trunc_ambiguous','vol_conflict','n_obs','ocr_kw','corrected']]
out=base.merge(cc,on=['market','keyword'],how='left')
out['in_screenshot']=out.screenshot_files.notna()
out['vol_rank']=out.vol.map(VOLRANK)
def vstat(r):
    if not r.in_screenshot: return 'NOT IN SCREENSHOTS (no Keyword Planner metric visible)'
    if r.vol=='' or pd.isna(r.vol): return 'In screenshot; metric shown as "—" (unknown)'
    flags=[]
    if r.status=='order_inferred': flags.append('keyword identity inferred from row order (OCR weak)')
    if r.trunc_ambiguous: flags.append('truncated keyword in UI; identity inferred from order')
    if r.vol_conflict: flags.append('conflicting values across overlapping screenshots')
    return 'KP screenshot (OCR-extracted)'+(' | '+'; '.join(flags) if flags else '')
out['validation_status']=out.apply(vstat,axis=1)
# extra screenshot keywords not in CSV
extra=c[~c.set_index(['market','keyword']).index.isin(base.set_index(['market','keyword']).index)]
out.to_csv(os.path.join(S,'master.csv'),index=False)
print('extra not in csv:',len(extra))
summ=out.groupby('market').agg(csv_keywords=('keyword','size'),in_screens=('in_screenshot','sum'),with_volume=('vol_rank',lambda s:s.notna().sum()),
    ge1k=('vol_rank',lambda s:(s>=3).sum()),ge10k=('vol_rank',lambda s:(s>=4).sum()),ge100k=('vol_rank',lambda s:(s>=5).sum()))
summ['coverage_%']=(summ.in_screens/summ.csv_keywords*100).round(1)
print(summ.to_string())
print(m.groupby('market').file.unique().apply(lambda x:len(x)))
