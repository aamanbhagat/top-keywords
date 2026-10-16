import sys, os, json
import pandas as pd
B=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(B); sys.path.insert(0,B)
import details, serp_evidence, discovery
OUT='/home/user/top-keywords/analysis/international-seo-top20'
T=pd.read_csv(os.path.join(OUT,'top20.csv')); A=pd.read_csv(os.path.join(OUT,'candidates_scored.csv'))
M=pd.read_csv(os.path.join(S,'master.csv')); AU=pd.read_csv(os.path.join(S,'screenshot_audit.csv'))
serp={s['serp_id']:s for s in serp_evidence.S}
def md(df):
    cols=list(df.columns); out='| '+' | '.join(cols)+' |\n|'+'|'.join(['---']*len(cols))+'|\n'
    for r in df.itertuples(index=False):
        out+='| '+' | '.join(str(v).replace('|','/').replace('\n',' ') if not (isinstance(v,float) and pd.isna(v)) else '' for v in r)+' |\n'
    return out
def links(ids):
    o=[]
    for sid in str(ids).split(';'):
        s=serp.get(sid)
        if not s: continue
        u=', '.join(f'[{i+1}]({x})' for i,x in enumerate(s['urls'][:8]))
        o.append(f"{sid} ({s['search_mode']}, \"{s['query']}\"): {u}")
    return '<br>'.join(o)
# ---- audit table
g=M.groupby('market').agg(CSV_keywords=('keyword','size'),visible_in_screenshots=('in_screenshot','sum'),with_volume=('vol_rank',lambda s:s.notna().sum()),
  vol_10K_plus=('vol_rank',lambda s:(s>=4).sum()),vol_1K_10K=('vol_rank',lambda s:(s==3).sum()),vol_100_1K=('vol_rank',lambda s:(s==2).sum()),with_bids=('bid_hi',lambda s:s.notna().sum()))
g['shown_as_dash']=g.visible_in_screenshots-g.with_volume; g['not_visible']=g.CSV_keywords-g.visible_in_screenshots
g['coverage_%']=(g.visible_in_screenshots/g.CSV_keywords*100).round(1)
sc=AU.groupby('market').agg(screenshots=('screenshot','size'))
g=g.join(sc).fillna(0).reset_index()
g['screenshots']=g.screenshots.astype(int)
g=g[['market','screenshots','CSV_keywords','visible_in_screenshots','coverage_%','with_volume','shown_as_dash','not_visible','vol_10K_plus','vol_1K_10K','vol_100_1K','with_bids']]
tot=g.sum(numeric_only=True); 
# ---- top20 table
tt=T[['rank','id','concept','markets','primary_keyword','primary_avg_monthly_searches','cluster_10k_plus','cluster_1k_10k','cluster_100_1k','A_organic_25','B_demand_20','C_toolfit_20','D_intent_10','E_cluster_10','F_monetisation_10','G_feasibility_5','total_100','confidence']].copy()
tt.columns=['#','ID','Opportunity','Market','Primary keyword','KP avg. monthly (range)','Kw ≥10K','Kw 1K–10K','Kw 100–1K','A /25','B /20','C /20','D /10','E /10','F /10','G /5','Score','Confidence']
tt['Opportunity']=tt['ID'].map(details.SHORT)
# ---- entries
E=[]
for r in T.itertuples():
    d=details.D[r.id]
    lang=r.language
    E.append(f"""### {r.rank}. {r.concept}  
`{r.id}` · **Market:** {r.markets} · **Language:** {lang} · **Score {r.total_100}/100** · **Confidence: {r.confidence}**

| Field | Detail |
|---|---|
| Primary keyword | **{r.primary_keyword}**: {r.primary_avg_monthly_searches} avg. monthly searches; 3-mo {r.primary_3m_change or '—'}; YoY {r.primary_yoy or '—'}; Ads competition {r.primary_ads_competition or '—'}; top-of-page bid {r.primary_top_bid_INR or '— (not shown)'} |
| Related keywords / intent cluster | {r.related_keywords} |
| Keyword Planner demand & source | Cluster: {r.cluster_kw_with_volume} keywords with volume ({r.cluster_10k_plus} at ≥10K–100K, {r.cluster_1k_10k} at 1K–10K, {r.cluster_100_1k} at 100–1K); sum of bucket lower bounds = {r.cluster_floor_sum:,}/month (indicative floor; may double-count close variants); {r.cluster_not_visible} cluster keywords are in the CSV but not visible in any screenshot. Source: {r.primary_source_screenshot}; location = market, All languages, Sep 2025 – Aug 2026. |
| Organic competition (A = {r.A_organic_25}/25) | {r.organic_assessment} |
| SERP evidence | {links(A.loc[A.id==r.id,'serp_ids'].iloc[0])} |
| Competitors & weaknesses | {d['comp']} |
| Why this beats other candidates | {d['why']} |
| URL / page structure | {d['url']} |
| Minimum viable functionality | {d['mvp']} |
| Localisation | {d['loc']} |
| Monetisation | {d['money']} |
| Score explanation | {r.score_explanation.replace(' | ','<br>')} |
| Validate before development | {d['validate']} |
""")
# ---- rejected
rj=A[A.decision=='REJECTED'].copy()
rj=rj[['id','markets','concept','primary_keyword','primary_vol','total','A','reason']]
rj.columns=['ID','Market','Candidate','Primary keyword','KP range','Score','A','Why it missed']
disc=pd.DataFrame(discovery.L,columns=['Market','Keyword / family (native)','Gloss','How found','Why it matters','Validation status'])
VOL=pd.read_csv(os.path.join(OUT,'top20_search_volume.csv')); VOLD=pd.read_csv(os.path.join(OUT,'top20_search_volume_keywords.csv'))
vt=VOL[['rank','opportunity','markets','primary_keyword','primary_avg_monthly_searches','primary_three_month_change','primary_yoy_change','kw_100K_1M','kw_10K_100K','kw_1K_10K','kw_100_1K','kw_10_100','kw_shown_as_dash','kw_not_visible','cluster_range_text']].copy()
vt['kw_10K_100K']=vt.kw_10K_100K+vt.kw_100K_1M
vt=vt.drop(columns=['kw_100K_1M'])
vt.columns=['#','Opportunity','Market','Primary keyword','Primary: avg. monthly searches','3-mo','YoY','Kw ≥10K','Kw 1K–10K','Kw 100–1K','Kw 10–100','Kw "—"','Kw not visible','Cluster range (sum of bounds)/month']
det=[]
for (rk,name),g in VOLD.groupby(['rank','opportunity'],sort=True):
    gg=g.head(10)
    det.append(f"**{rk}. {name}** ({len(g)} keywords with a range)\n\n"+md(gg[['market','keyword','avg_monthly_searches','three_month_change','yoy_change','ads_competition']].rename(columns={'market':'Market','keyword':'Keyword','avg_monthly_searches':'Avg. monthly searches','three_month_change':'3-mo','yoy_change':'YoY','ads_competition':'Ads comp.'})))
VOLCHECK=open(os.path.join(S,'volcheck','note.txt')).read().strip() if os.path.exists(os.path.join(S,'volcheck','note.txt')) else ''
tpl=open(os.path.join(B,'report_template.md')).read()
rep=(tpl.replace('{{AUDIT_TABLE}}',md(g)).replace('{{AUDIT_TOT}}',f"Totals: {int(tot.CSV_keywords):,} CSV keywords; {int(tot.visible_in_screenshots):,} visible with a matched row; {int(tot.with_volume):,} with a volume range; {int(tot.shown_as_dash):,} shown as '—'; {int(tot.not_visible):,} not visible (incl. all 1,277 TR).")
   .replace('{{TOP20_TABLE}}',md(tt)).replace('{{ENTRIES}}','\n'.join(E)).replace('{{REJECTED_TABLE}}',md(rj)).replace('{{DISCOVERY_TABLE}}',md(disc)).replace('{{VOLUME_TABLE}}',md(vt)).replace('{{VOLUME_DETAIL}}','\n'.join(det)).replace('{{VOLCHECK_NOTE}}',VOLCHECK))
open(os.path.join(OUT,'REPORT.md'),'w').write(rep)
print(len(rep))
