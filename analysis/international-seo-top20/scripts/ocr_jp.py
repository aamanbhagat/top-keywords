import sys, os, json, io, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rows import find_rows
from ocr import ocr_stack
from PIL import Image
S=os.path.dirname(os.path.abspath(__file__))
SL=64; SC=3
def redo(path):
    shp,rows=find_rows(path)
    pil=Image.open(path).convert('L')
    jf=os.path.join(S,'ocr',os.path.basename(path)+'.json')
    d=json.load(open(jf))
    assert len(d)==len(rows)
    per={}
    CH=60
    for c0 in range(0,len(rows),CH):
        chunk=rows[c0:c0+CH]
        st=Image.new('L',(300,SL*len(chunk)+20),255)
        for i,(a,b) in enumerate(chunk):
            st.paste(pil.crop((384,a+2,644,b-2)),(20,i*SL+12))
        st=st.resize((st.width*SC,st.height*SC),Image.LANCZOS)
        for (l,t,w,h,conf,txt) in ocr_stack(st,'jpn'):
            idx=int(((t+h/2)/SC)//SL)
            if 0<=idx<len(chunk): per.setdefault(c0+idx,[]).append((l,txt))
    for i in range(len(rows)):
        d[i]['kw_old']=d[i]['kw']
        d[i]['kw']=' '.join(t for _,t in sorted(per.get(i,[])))
    json.dump(d,open(jf,'w'),ensure_ascii=False)
    print(path,len(d))
if __name__=='__main__':
    from multiprocessing import Pool
    with Pool(2) as p: p.map(redo,sys.argv[1:])
