import sys, os, pandas as pd
from PIL import Image, ImageDraw
S=os.path.dirname(os.path.abspath(__file__)); REPO='/home/user/top-keywords'
m=pd.read_csv(os.path.join(S,'ocr_matched.csv'))
pairs=[l.split('|',1) for l in sys.argv[2].split(';;')]
out=sys.argv[1]
rows=[]
for mk,kw in pairs:
    x=m[(m.market==mk)&(m.keyword==kw)]
    if len(x)==0: print('NOT FOUND',mk,kw); continue
    r=x.iloc[0]; rows.append((mk,kw,r.file,int(r.y)))
W=Image.new('RGB',(2200,len(rows)*44),'white')
cache={}
for i,(mk,kw,f,y) in enumerate(rows):
    if f not in cache: cache[f]=Image.open(os.path.join(REPO,f)).convert('RGB')
    im=cache[f]
    # keyword+vol+3m+yoy+comp, then bids
    a=im.crop((380,y,2256,y+40)); b=im.crop((2644,y,3420,y+40))
    row=Image.new('RGB',(1876+776,40),'white'); row.paste(a,(0,0)); row.paste(b,(1876,0))
    row=row.resize((2200,int(40*2200/2652)))
    W.paste(row,(0,i*44))
W.save(out); print(len(rows))
