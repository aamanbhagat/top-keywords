import pandas as pd, json, os
from PIL import Image, ImageDraw, ImageFont
S='/tmp/claude-0/-home-user-top-keywords/72fe8ed4-a1a2-512f-9b4a-4bc293bbd17d/scratchpad'
REPO='/home/user/top-keywords'
mem=pd.read_csv(f'{REPO}/analysis/international-seo-top20/top20_keyword_clusters.csv')
ocr=pd.read_csv(f'{S}/ocr_matched.csv')
vis=mem[mem.source_screenshot.notna()&(mem.source_screenshot!='')].copy()
vis=vis.drop_duplicates(['market','keyword'])
rows=[]
for r in vis.itertuples():
    x=ocr[(ocr.market==r.market)&(ocr.keyword==r.keyword)]
    if not len(x): continue
    o=x.iloc[0]
    def s(v): return '' if pd.isna(v) else str(v)
    rows.append(dict(market=r.market,keyword=r.keyword,file=o.file,y=int(o.y),
        vol=s(o.vol) or '—',m3=s(o.m3) or '—',yoy=s(o.yoy) or '—',comp=s(o.comp) or '—',
        bid_lo=('—' if pd.isna(o.bid_lo) else f'₹{o.bid_lo:,.2f}'),bid_hi=('—' if pd.isna(o.bid_hi) else f'₹{o.bid_hi:,.2f}')))
rows.sort(key=lambda r:(r['file'],r['y']))
PER=30; os.makedirs(f'{S}/volcheck/sheets',exist_ok=True)
try: font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',26)
except Exception: font=ImageFont.load_default()
cache={}; manifest=[]
for si in range(0,len(rows),PER):
    chunk=rows[si:si+PER]; n=si//PER+1
    W=Image.new('RGB',(2290,len(chunk)*46+10),'white'); dr=ImageDraw.Draw(W)
    for i,r in enumerate(chunk):
        if r['file'] not in cache:
            cache.clear(); cache[r['file']]=Image.open(f"{REPO}/{r['file']}").convert('RGB')
        im=cache[r['file']]; y=r['y']
        a=im.crop((380,y,2256,y+40)); b=im.crop((2644,y,3420,y+40))
        row=Image.new('RGB',(2652,40),'white'); row.paste(a,(0,0)); row.paste(b,(1876,0))
        row=row.resize((2200,33))
        W.paste(row,(85,i*46+6)); dr.text((8,i*46+6),f'{i+1:>2}',fill='red',font=font)
        dr.line((0,i*46+44,2290,i*46+44),fill=(200,200,200))
        r['row']=i+1
    p=f'{S}/volcheck/sheets/sheet_{n:02d}.png'; W.save(p)
    manifest.append(dict(sheet=n,image=p,rows=[{k:r[k] for k in ('row','market','keyword','vol','m3','yoy','comp','bid_lo','bid_hi','file','y')} for r in chunk]))
json.dump(manifest,open(f'{S}/volcheck/manifest.json','w'),ensure_ascii=False,indent=1)
print(len(rows),'rows',len(manifest),'sheets')
