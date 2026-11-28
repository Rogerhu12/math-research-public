"""Continuous original five-field boxes, with centered Fourier Taylor sums.

A serialized R654 frontier resumes at the first unresolved cell, carrying
its outward eta-error ball. No previously closed cell is entered again.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from flint import arb, ctx

from r632_true_hermite_bvp import emit
from r654_actual_seed_balls import fr
from r654_local_released_physical_boxes import interval
from r654_released_rest_physical_base import compose, derivative
from r654_released_rest_four_end_chart import FourEndPending


@lru_cache(maxsize=65536)
def bernstein_bounds(p,lo,hi):
    c=compose(p,(lo,hi-lo))
    n=len(c)-1
    b=[sum(F(comb(i,k),comb(n,k))*c[k] for k in range(i+1)) for i in range(n+1)]
    return min(b),max(b)


def range_poly(p,lo,hi):
    return interval(*bernstein_bounds(p,lo,hi))


class Fourier:
    def __init__(self, q, sine):
        pi=arb.pi()
        self.sine=sine
        self.terms=[]
        self.second=self.third=arb(0)
        for j,v in enumerate(q):
            if float(v)==0.:
                continue
            mode=2*j+1 if sine else j
            w=pi*mode/(2 if sine else 1)
            c=arb(fr(F(float(v))/(1+mode**2)))
            self.terms.append((w,c))
            self.second+=abs(c)*w**2
            self.third+=abs(c)*w**3

    def bounds(self,mid,radius):
        v=slope=sec=arb(0)
        for w,c in self.terms:
            sn,cs=(w*mid).sin_cos()
            common=c*(sn if self.sine else cs)
            v+=common
            slope+=w*c*(cs if self.sine else -sn)
            sec-=w*w*common
        unit=arb(0,1)
        delta=unit*radius
        return (v+slope*delta+unit*self.second*radius**2/2,
                slope+sec*delta+unit*self.third*radius**2/2)


class PhysicalFrontier:
    def __init__(self,base,clock,nodes,depth):
        self.base,self.clock,self.nodes,self.depth=base,clock,nodes,depth
        self.records=[]
        self.cache={}
        self.unclosed={}
        self.violations={}
        self.latest_pending=None
        eta=F(0)
        self.reference=[]
        for p in base.pieces:
            self.reference.append((p.h,p.k,derivative(p.h),derivative(p.k),eta))
            eta+=(sum(p.k)-p.k[0])/(2*p.h[0])

    def __getattr__(self,name):
        return getattr(self.base,name)

    @staticmethod
    def key(q,tau):
        return tuple(map(float,q)),tuple(map(float,tau))

    def install_paid_accepted(self,q,tau,certificate):
        if not (certificate["sufficient_bounds_closed"] and
                certificate["all_five_fields_certified_by_material_cell_balls"]):
            raise ValueError("Actual accepted source has no complete five-field certificate")
        self.cache[self.key(q,tau)]=dict(certificate,from_paid_R654_accepted_source=True)

    def physical_enclosure(self,q,tau):
        key=self.key(q,tau)
        if key in self.cache:
            return self.cache[key]
        if key in self.violations:
            raise FloatingPointError(self.violations[key])
        return self.qualify(q,tau,self.unclosed.get(key))

    def qualify(self,q,tau,paid):
        ctx.prec=128
        key=self.key(q,tau)
        if paid is not None and (key!=self.key(paid["shape_parameters"],paid["durations"]) or
                paid["state"]!="pending" or not paid["remaining_same_piece"]):
            raise ValueError("Unclosed source pair or frontier differs")
        times=[p.duration if p.control is None else F(float(tau[p.control])) for p in self.pieces]
        length=sum(times)
        if min(times)<=0 or not F(21,10)<=length<=F(79,10):
            raise FloatingPointError("Actual duration or L outside original domain")
        hF,kF=Fourier(q[:129],False),Fourier(q[129:],True)
        first=0 if paid is None else paid["piece"]
        carried=0 if paid is None else paid["closed_cells"]
        correct=arb(0) if paid is None else arb(paid["eta_error_prefix"])
        rec={"state":"pending","shape_parameters":list(key[0]),"durations":list(key[1]),
             "source_closed_cells_carried":carried,"new_closed_cells":0,"new_visited_cells":0}
        self.records.append(rec)
        start=sum(times[:first])
        for j in range(first,len(times)):
            T=times[j]
            hp,kp,htp,ktp,eta0=self.reference[j]
            if paid is not None and j==first:
                remaining=paid["remaining_same_piece"]
                if list(remaining[0])!=[paid["depth"],paid["path"]] or (
                        list(range(j+1,len(times)))!=paid["remaining_pieces"]):
                    raise ValueError("Malformed material prefix frontier")
                stack=[*remaining[1:],remaining[0]]
            else:
                stack=[(0,0)]
            while stack:
                depth,path=stack.pop()
                lo,hi=F(path,2**depth),F(path+1,2**depth)
                # Record before clock or evaluation so an interrupted cell can resume.
                rec.update(piece=j,depth=depth,path=path,remaining_same_piece=[(depth,path),*stack],
                    remaining_pieces=list(range(j+1,len(times))),eta_error_prefix=correct.str(40),
                    closed_cells=carried+rec["new_closed_cells"])
                self.latest_pending=rec
                self.unclosed[key]=rec
                self.clock.check("current_unclosed_centered_material_cell")
                rec["new_visited_cells"]+=1
                mid=arb(fr((start+T*(lo+hi)/2)/length))
                radius=arb(fr(T*(hi-lo)/(2*length)))
                f,fx=hF.bounds(mid,radius)
                g,gx=kF.bounds(mid,radius)
                hB,kB,ht,kt=[range_poly(p,lo,hi) for p in (hp,kp,htp,ktp)]
                h,k=hB+f,kB+g
                target={"h":(h,arb(fr(F(4,5))),arb(3)),"k":(k,arb(-2),arb(2)),
                    "gamma":(ht/arb(fr(T))+fx/arb(fr(length)),arb(-6),arb(6)),
                    "upsilon":(kt/arb(fr(T))+gx/arb(fr(length)),arb(-6),arb(6))}
                if h>0 and hB>0:
                    rate=gx*arb(fr(T/length))/(2*h)-kt*f/(2*hB*h)
                    etaB=arb(fr(eta0))+(kB-arb(fr(kp[0])))/(2*arb(fr(hp[0])))
                    target["eta"]=(etaB+correct+interval(F(0),hi-lo)*rate,arb(-1),arb(1))
                for name,(v,lower,upper) in target.items():
                    if v<=lower or v>=upper:
                        rec.update(state="verified_violation",field=name,enclosure=v.str(32))
                        self.unclosed.pop(key,None)
                        self.violations[key]="Certified original field violation: "+name
                        raise FloatingPointError(self.violations[key])
                if len(target)==5 and all(v>low and v<high for v,low,high in target.values()):
                    correct+=arb(fr(hi-lo))*rate
                    rec["new_closed_cells"]+=1
                elif depth>=self.depth or rec["new_visited_cells"]>=self.nodes:
                    rec["field_enclosures"]={name:v[0].str(32) for name,v in target.items()}
                    emit("R674_MATERIAL_FRONTIER",rec)
                    raise FourEndPending(rec)
                else:
                    stack.extend([(depth+1,2*path+1),(depth+1,2*path)])
            start+=T
        rec.update(state="certified",closed_cells=carried+rec["new_closed_cells"],
                   eta_error_final=correct.str(40),remaining_same_piece=[],remaining_pieces=[])
        certificate={"sufficient_bounds_closed":True,"all_five_fields_certified_by_material_cell_balls":True,
            "closed_cells":rec["closed_cells"],"source_closed_cells_carried":carried,
            "new_visited_cells":rec["new_visited_cells"],"new_closed_cells":rec["new_closed_cells"]}
        self.unclosed.pop(key,None)
        self.cache[key]=certificate
        return certificate
