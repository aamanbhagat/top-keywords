import sys, numpy as np
from PIL import Image
SEP=(218,220,224)
def find_rows(path):
    im=np.array(Image.open(path).convert('RGB')).astype(int)
    H=im.shape[0]
    def is_sep(y):
        return all(abs(im[y,x]-SEP).sum()<12 for x in (700,1500,2700))
    seps=[y for y in range(H) if is_sep(y)]
    # collapse consecutive
    groups=[]
    for y in seps:
        if groups and y-groups[-1][1]<=1: groups[-1][1]=y
        else: groups.append([y,y])
    rows=[]
    for a,b in zip(groups,groups[1:]):
        top=a[1]+1; bot=b[0]
        h=bot-top
        if 30<=h<=50 and (im[top:bot,700]==255).all():
            rows.append((top,bot))
    return im.shape, rows
if __name__=='__main__':
    for p in sys.argv[1:]:
        shp,rows=find_rows(p)
        hs=[b-a for a,b in rows]
        print(p, shp, len(rows), sorted(set(hs)))
