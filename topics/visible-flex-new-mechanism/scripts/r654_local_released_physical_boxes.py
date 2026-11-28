"""Adaptive material-cell bounds when global coefficient sums do not certify a trial."""
from fractions import Fraction as F
from flint import arb,ctx
from r654_actual_seed_balls import fr
from r654_released_rest_physical_base import derivative
from r654_released_rest_four_end_chart import FourEndPending


def interval(lo,hi):
    return arb(fr((lo+hi)/2))+arb(0,1)*arb(fr((hi-lo)/2))


def poly(c,t):
    v=arb(0)
    for a in reversed(c):
        v=v*t+a
    return v


class LocalBoxes:
    def __init__(self,base,clock,nodes,depth):
        self.base,self.clock,self.nodes,self.depth=base,clock,nodes,depth
        self.records=[]
        eta=F(0)
        self.reference=[]
        for p in base.pieces:
            h0,k0=p.h[0],p.k[0]
            hs=tuple(arb(fr(v)) for v in p.h)
            ks=tuple(arb(fr(v)) for v in p.k)
            self.reference.append((hs,ks,tuple(arb(fr(v)) for v in derivative(p.h)),
                tuple(arb(fr(v)) for v in derivative(p.k)),arb(fr(eta)),arb(fr(h0)),arb(fr(k0))))
            eta+=(sum(p.k)-k0)/(2*h0)

    def __getattr__(self,name):
        return getattr(self.base,name)

    def physical_enclosure(self,q,taus):
        initial=self.base.physical_enclosure(q,taus)
        if initial["sufficient_bounds_closed"]:
            return initial
        ctx.prec=96
        times=[p.duration if p.control is None else F(float(taus[p.control])) for p in self.base.pieces]
        length=sum(times)
        if min(times)<=0 or not F(21,10)<=length<=F(79,10):
            raise FloatingPointError("Actual L or a segment duration violates the original domain")
        pi=arb.pi()
        h_modes=[(pi*j,arb(fr(F(float(v))/(1+j*j)))) for j,v in enumerate(q[:129]) if v!=0.]
        k_modes=[(pi*(2*j+1)/2,arb(fr(F(float(v))/(1+(2*j+1)**2)))) for j,v in enumerate(q[129:]) if v!=0.]
        rec={"state":"pending","shape_parameters":list(map(float,q)),"durations":list(map(float,taus)),
             "closed_cells":0,"visited_cells":0,"pending":[]}
        self.records.append(rec)
        correct=arb(0)
        start=F(0)
        for j,(T,data) in enumerate(zip(times,self.reference)):
            hb,kb,hbt,kbt,eta0,h0,k0=data
            stack=[(0,0)]
            while stack:
                depth,path=stack.pop()
                self.clock.check("R654_material_interval_physical_frontier")
                rec["visited_cells"]+=1
                lo,hi=F(path,2**depth),F(path+1,2**depth)
                t=interval(lo,hi)
                x=interval((start+T*lo)/length,(start+T*hi)/length)
                hB,kB,ht,kt=poly(hb,t),poly(kb,t),poly(hbt,t),poly(kbt,t)
                f=g=fx=gx=arb(0)
                for w,c in h_modes:
                    angle=w*x
                    f+=c*angle.cos()
                    fx-=w*c*angle.sin()
                for w,c in k_modes:
                    angle=w*x
                    g+=c*angle.sin()
                    gx+=w*c*angle.cos()
                h,k=hB+f,kB+g
                target={"h":(h,arb(fr(F(4,5))),arb(3)),"k":(k,arb(-2),arb(2)),
                    "gamma":(ht/arb(fr(T))+fx/arb(fr(length)),arb(-6),arb(6)),
                    "upsilon":(kt/arb(fr(T))+gx/arb(fr(length)),arb(-6),arb(6))}
                if h>0 and hB>0:
                    error_rate=gx*arb(fr(T/length))/(2*h)-kt*f/(2*hB*h)
                    etaB=eta0+(kB-k0)/(2*h0)
                    target["eta"]=(etaB+correct+interval(F(0),hi-lo)*error_rate,arb(-1),arb(1))
                for field,(v,lower,upper) in target.items():
                    if v<=lower or v>=upper:
                        rec.update(state="verified_violation",piece=j,depth=depth,path=path,
                                   field=field,enclosure=v.str(24))
                        raise FloatingPointError("Certified material cell violates the original "+field+" box")
                if len(target)==5 and all(v>lower and v<upper for v,lower,upper in target.values()):
                    correct+=arb(fr(hi-lo))*error_rate
                    rec["closed_cells"]+=1
                    continue
                if depth>=self.depth or rec["visited_cells"]>=self.nodes:
                    rec.update(piece=j,depth=depth,path=path,remaining_same_piece=[(depth,path)]+stack,
                        remaining_pieces=list(range(j+1,len(times))),eta_error_prefix=correct.str(32),
                        field_enclosures={k:v[0].str(24) for k,v in target.items()})
                    raise FourEndPending(rec)
                stack.append((depth+1,2*path+1))
                stack.append((depth+1,2*path))
            start+=T
        rec.update(state="certified",eta_error_final=correct.str(24))
        return {"sufficient_bounds_closed":True,"all_five_fields_certified_by_material_cell_balls":True,
                "visited_cells":rec["visited_cells"],"closed_cells":rec["closed_cells"]}
