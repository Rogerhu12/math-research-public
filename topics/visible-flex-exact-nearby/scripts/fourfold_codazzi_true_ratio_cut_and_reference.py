"""All four GCS ratio branches, locked whole GPR carrier and radial subpieces."""
from fractions import Fraction
from pathlib import Path
import gzip,hashlib,json,struct
from math import isfinite
from flint import arb
from fourfold_codazzi_true_phase_original_inputs import CUT,check
from fourfold_codazzi_true_ratio_label_mesh import M,CELLS,stream_row

GCS_SHA="9af56c23e91a021f0463aa01b68ea93916ba11d374ecd7323ce4c4b51b3da9ba"
GCS_BYTES=11131542
GCS_RUN="46132087372"
GCS_RECEIPT_SHA="201c8215275b04dfa69c6a9b03248dea6bde01bd782969d006c823088c0637b7"
L=struct.Struct("<I");B=struct.Struct("<dddd")


def file_sha(path):
    with Path(path).open("rb") as f:return hashlib.file_digest(f,"sha256").hexdigest()


def cut_ratio(path):
    check(path.stat().st_size==GCS_BYTES and file_sha(path)==GCS_SHA,"actual whole original cut seed")
    names=["R_"+s+"_"+e for s in ("plus","minus") for e in ("positive","negative")]
    data={k:[] for k in names}
    prefactor=None
    with gzip.open(path,"rb") as f:
        nr,=L.unpack(f.read(4));head=json.loads(f.read(nr))
        old=head["cells"];shape=head["schema"]
        check(old==2048 and old%CELLS==0 and head["cut"]==str(CUT)
              and all(dict(shape)[k]==M+1 for k in names),"actual four signed GCS ratios")
        for kind in range(2):
            for i in range(old):
                for name,n in shape:
                    v=f.read(B.size*n)
                    check(len(v)==B.size*n,"all complete original cut rectangles")
                    if not kind:continue
                    if name in data:
                        row=[]
                        for rl,rh,il,ih in B.iter_unpack(v):
                            check(all(map(isfinite,(rl,rh,il,ih))) and rl<=0<=rh and il<=ih,
                                  "real parameter implies a purely imaginary signed ratio")
                            row.append(arb(il).union(arb(ih)))
                        data[name].append(row)
                    if name=="omega":
                        rl,rh,il,ih=B.unpack_from(v)
                        check(arb(rl)>arb(4)/10**8 and il<=0<=ih and rl<=rh,
                              "actual entire GCS cut common-gap lower")
                    if name=="radial_prefactor":
                        rl,rh,il,ih=B.unpack(v);check(rl>0 and il<=0<=ih,"radial cut scalar")
                        z=arb(rl).union(arb(rh))
                        prefactor=z if prefactor is None else prefactor.intersection(z)
        check(not f.read(1) and prefactor is not None,"whole verified cut seed")
    allbins=[]
    for i in range(old):
        row=list(data[names[0]][i])
        for (sign,eps,name) in ((1,-1,names[1]),(-1,1,names[2]),(-1,-1,names[3])):
            v=data[name][(sign*i)%old]
            row=[z.intersection(w*(eps*sign**(j+1))) for j,(z,w) in enumerate(zip(row,v))]
        allbins.append(row)
    ratio=old//CELLS
    check(ratio%2==0,"complete centered fine/coarse bins")
    coarse=[]
    for i in range(CELLS):
        indices=[(i*ratio+j)%old for j in range(-(ratio//2),ratio//2+1)]
        row=allbins[indices[0]].copy()
        for j in indices[1:]:row=[a.union(b) for a,b in zip(row,allbins[j])]
        coarse.append(row)
    return coarse,prefactor


class Phase:
    def __init__(self,path,expected,plan):
        check(path.stat().st_size==expected["bytes"] and file_sha(path)==expected["sha256"],
              "actual complete GPR gzip identity")
        self.f=gzip.open(path,"rb");self.h=hashlib.sha256()
        raw=self.f.read(4);n,=L.unpack(raw);payload=self.f.read(n)
        self.h.update(raw+payload);self.size=4+n
        self.head=json.loads(payload)
        check(self.head["schema"]=="GPR-1" and self.head["cut"]==str(CUT)
              and self.head["positive_modes"]==128 and self.head["time_degree"]==6 and self.head["jet_order"]==9
              and self.head["seed_sha256"]==GCS_SHA and self.head["seed_bytes"]==GCS_BYTES
              and self.head["inward_plan"]==[[str(l),str(r),k,i] for l,r,k,i in plan],
              "same complete ordered physical ray path")
        self.expected=expected;self.count=0

    def row(self):
        q,e,b=stream_row(self.f,self.head);self.h.update(b);self.size+=len(b);self.count+=1
        return q,e

    def close(self):
        check(not self.f.read(1) and self.count==len(self.head["inward_plan"])
              and self.h.hexdigest()==self.expected["uncompressed_sha256"]
              and self.size==self.expected["uncompressed_bytes"],"full original natural GPR readback")
        self.f.close()


def subcells(l,r,root_lower):
    cur=r
    while cur>l:
        # Preserve exact dyadics at new radial knots. A geometric refinement
        # is restricted to the few cells near the root; no original seam moves.
        length=r-l
        while 16*length>root_lower-cur:length/=2
        other=max(l,cur-length)
        yield other,cur
        cur=other
