import sys, os, json, subprocess, io, numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from rows import find_rows
COLS={'kw':(384,644),'vol':(650,1092),'m3':(1100,1480),'yoy':(1488,1868),'comp':(1870,2256),'ais':(2260,2644),'bidlo':(2650,3032),'bidhi':(3040,3420),'status':(3424,3840)}
LANG={'BR':'por','DE':'deu','ES':'spa','ID':'ind','JP_EN':'eng','JP':'jpn','MX':'spa','PL':'pol','TR':'tur'}
SLOT=64; SCALE=1.5
def market(fn):
    b=os.path.basename(fn).upper()
    if b.startswith('JP_EN'): return 'JP_EN'
    return b[:2]
def ocr_stack(img, lang, psm=6):
    buf=io.BytesIO(); img.save(buf,format='PNG')
    r=subprocess.run(['tesseract','stdin','stdout','-l',lang,'--psm',str(psm),'tsv'],input=buf.getvalue(),capture_output=True)
    out=r.stdout.decode('utf-8','replace').splitlines()
    words=[]
    for line in out[1:]:
        p=line.split('\t')
        if len(p)<12 or p[0]!='5': continue
        txt=p[11]
        if not txt.strip(): continue
        words.append((int(p[6]),int(p[7]),int(p[8]),int(p[9]),float(p[10]),txt))
    return words
def strip_currency(crop):
    # the rupee glyph is ~6px wide at this scale; blank it so it is not read as a digit
    g=np.array(crop.convert('L'))
    xs=np.where((g<200).any(axis=0))[0]
    if len(xs)==0: return crop
    arr=np.array(crop); arr[:,:xs[0]+6]=255
    return Image.fromarray(arr)
def run(path):
    m=market(path)
    pil=Image.open(path).convert('RGB')
    shp,rows=find_rows(path)
    res=[{'file':os.path.basename(path),'market':m,'idx':i,'y':a} for i,(a,b) in enumerate(rows)]
    for col,(x0,x1) in COLS.items():
        if col in ('ais','status'): continue
        w=x1-x0
        lang=LANG[m] if col=='kw' else 'eng'
        if col=='kw' and m=='JP': lang='jpn+eng'
        per={}
        CH=150
        for c0 in range(0,len(rows),CH):
            chunk=rows[c0:c0+CH]
            stack=Image.new('RGB',(w+40,SLOT*len(chunk)+20),(255,255,255))
            for i,(a,b) in enumerate(chunk):
                crop=pil.crop((x0,a+2,x1,b-2))
                if col in ('bidlo','bidhi'): crop=strip_currency(crop)
                stack.paste(crop,(20,i*SLOT+12))
            stack=stack.resize((int(stack.width*SCALE),int(stack.height*SCALE)),Image.LANCZOS)
            words=ocr_stack(stack,lang)
            for (l,t,ww,h,conf,txt) in words:
                cy=(t+h/2)/SCALE
                idx=int(cy//SLOT)
                if 0<=idx<len(chunk): per.setdefault(c0+idx,[]).append((l,txt,conf))
        for i in range(len(rows)):
            ws=sorted(per.get(i,[]))
            res[i][col]=' '.join(t for _,t,_ in ws)
            res[i][col+'_conf']=min([c for *_,c in ws],default=-1)
    return res
def one(args):
    out,f=args
    o=os.path.join(out,os.path.basename(f)+'.json')
    if os.path.exists(o): return 0
    r=run(f); json.dump(r,open(o,'w'),ensure_ascii=False); print(f,len(r),flush=True); return len(r)
if __name__=='__main__':
    out=sys.argv[1]; files=sys.argv[2:]
    from multiprocessing import Pool
    with Pool(4) as p:
        n=p.map(one,[(out,f) for f in files])
    print(sum(n))
