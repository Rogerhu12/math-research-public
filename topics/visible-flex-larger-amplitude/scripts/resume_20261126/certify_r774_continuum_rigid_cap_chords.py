#!/usr/bin/env python3
"""R774 continuum upper/lower chord bounds for the two registered rigid translations.

Local interval arithmetic encloses exact real elementary formulae. IEEE-754 binary64
round-to-nearest elementary +,-,*,/ and sqrt each receive an outward nextafter.
No system trigonometric routine enters a bound. Material integrals use pointwise
rectangle enclosures on every complete cell and a zero-to-width partial cell.
The maximum lower bound is a witness for every material point of its displayed
box. Reflected lower material has the same norm. The test concerns a necessary
end chord and the registered convex-map guard only; it does not certify a filling.
"""
import argparse
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import os
import numpy as np

def down(x): return np.nextafter(x,-np.inf)
def up(x): return np.nextafter(x,np.inf)

class I:
    __array_priority__=10000
    def __init__(self,lo,hi=None):
        self.lo=np.asarray(lo,dtype=np.float64)
        self.hi=self.lo if hi is None else np.asarray(hi,dtype=np.float64)
    def __add__(a,b):
        b=iv(b);return I(down(a.lo+b.lo),up(a.hi+b.hi))
    __radd__=__add__
    def __neg__(a):return I(-a.hi,-a.lo)
    def __sub__(a,b):return a+(-iv(b))
    def __rsub__(a,b):return iv(b)+(-a)
    def __mul__(a,b):
        b=iv(b);x=a.lo*b.lo;y=a.lo*b.hi;z=a.hi*b.lo;w=a.hi*b.hi
        return I(down(np.minimum(np.minimum(x,y),np.minimum(z,w))),
                 up(np.maximum(np.maximum(x,y),np.maximum(z,w))))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=iv(b)
        if np.any(b.lo<=0):raise ArithmeticError("positive divisor required")
        return a*I(down(1/b.hi),up(1/b.lo))
    def __getitem__(a,k):return I(a.lo[k],a.hi[k])
    def square(a):
        lo=np.maximum(0.,np.maximum(a.lo,-a.hi))
        hi=np.maximum(abs(a.lo),abs(a.hi))
        return I(np.maximum(0.,down(lo*lo)),up(hi*hi))
    def sqrt(a):
        if np.any(a.hi<0):raise ArithmeticError("invalid squared radius")
        return I(np.maximum(0.,down(np.sqrt(np.maximum(a.lo,0.)))),up(np.sqrt(a.hi)))

def iv(x):return x if isinstance(x,I) else I(x)

def rat(q):
    f=float(Fraction(q));return I(down(f),up(f))

def clip(v,lo,hi):
    return I(np.minimum(np.maximum(v.lo,lo),hi),np.minimum(np.maximum(v.hi,lo),hi))

def positive(v):return I(np.maximum(0.,v.lo),np.maximum(0.,v.hi))

def where(test,a,b):
    a,b=iv(a),iv(b);return I(np.where(test,a.lo,b.lo),np.where(test,a.hi,b.hi))

def atan_inverse(q,k):
    s=sum(((-1)**i*Fraction(1,(2*i+1)*q**(2*i+1)) for i in range(k)),Fraction(0))
    t=s+(-1)**k*Fraction(1,(2*k+1)*q**(2*k+1))
    return min(t,s),max(t,s)

a,b=atan_inverse(5,32);c,d=atan_inverse(239,12)
PI=I(rat(16*a-4*d).lo,rat(16*b-4*c).hi)
HALF=PI/2
RAMP=rat(".0004")
T=rat(".44")+rat(".132")*HALF+rat(".0005")
DB=I(rat(".132").lo,rat(".1325").hi)
PB=DB
PE=I(rat(".439").lo,rat(".44").hi)
WALL=rat(".95")
WALLRATE=rat("5.4")

def trig(v,cosine=False):
    # The rounded midpoint is just a real number in the Taylor identity; the
    # distance to either endpoint is computed outward. For |x|<=4 the degree
    # 34/35 polynomials are their degree-35 expansions and have remainder <=4^36/36!.
    mid=.5*v.lo+.5*v.hi
    if np.max(abs(mid))>4:raise ArithmeticError("trigonometric Taylor range")
    rad=up(np.maximum(abs(mid-v.lo),abs(v.hi-mid)))
    x=I(mid);xx=-x.square()
    term=I(1) if cosine else x
    value=term
    for k in range(1,18):
        den=(2*k-1 if cosine else 2*k+1)*(2*k)
        term=term*xx/den;value=value+term
    # Both degree-34 cosine and degree-35 sine are their Taylor expansions
    # through degree 35, including cosine's zero odd coefficient.
    from math import factorial
    rem=rat(Fraction(4**36,factorial(36))).hi
    err=up(rad+rem)
    return clip(value+I(-err,err),-1.,1.)

def sine(x):return trig(x)
def cosine(x):return trig(x,True)

def clock(z,length,edge,degree):
    # f(x)=edge*integral_0^clamp(x/edge) S + (x-edge)_+; the smoothed
    # trapezoid integral is f(z)-f(z-(length-edge)). Both endpoints plateau.
    def f(x):
        u=clip(x/edge,0.,1.);u2=u.square();u4=u2.square()
        if degree==5:p=u4*(rat("2.5")+u*(-3+u))
        else:p=(u4*u)*(7+u*(-14+u*(10-rat("2.5")*u)))
        return edge*clip(p,0.,.5)+positive(x-edge)
    gap=length-edge
    v=clip((f(z)-f(z-gap))/gap,0.,1.)
    return where(z.hi<=0,0,where(z.lo>=length.hi,1,v))

def heading(a):
    P,N=rat("1.44"),rat(".71")
    start=WALL-2*(P+N)/WALLRATE-4*RAMP-rat(".06")-rat(".001")
    h=I(0)
    for i,(amp,sign) in enumerate(((P,1),(P,-1),(N,-1),(N,1))):
        length=amp/WALLRATE+RAMP
        h=h+sign*amp*clock(a-start,length,RAMP,5)
        start=start+length+(rat(".06") if i==0 else 0)
    return clip(h,rat("-.71").lo,rat("1.44").hi)

def path_angles(name,u):
    if name=="negative_bend":
        length=rat(".26");beta=HALF*clock(u*length,length,rat(".0325"),5)
        v=clock(beta-rat(".617"),HALF-rat(".005")-rat(".617"),rat(".012"),7)
    elif name=="straight_tongue":
        length=rat(".44");beta=HALF;v=I(1)
    elif name=="U_turn":
        length=rat(".15")*PI+rat(".001")
        x=PI*clock(u*length,length,rat(".001"),5);beta=HALF-x
        v=1-clock(x-rat(".98"),rat("1.02"),rat(".02"),7)
    else:raise ValueError(name)
    return length,beta,v

def tangent_difference(beta,eta):
    # beta_new=beta-eta; these formulae retain cancellation as theta tends to zero.
    z=2*sine(eta/2);a=beta-eta/2
    return z*sine(a),-z*cosine(a)

def unit_boxes(n):
    # n is a power of two and all grid endpoints are exactly representable.
    g=np.arange(n+1,dtype=float)/n
    return I(g[:-1],g[1:])

def prefix(x):
    # For sequential binary64 cumsum, gamma_n<=2*n*2^-53. The conservative
    # absolute allowance below also covers gradual underflow and partial sums.
    n=x.lo.shape[-1];amp=np.maximum(1.,np.maximum(np.max(abs(x.lo),axis=-1),
                                                 np.max(abs(x.hi),axis=-1)))
    err=up((4*n*n*np.finfo(float).eps)*amp)[...,None]
    zero=np.zeros(x.lo.shape[:-1]+(1,))
    return I(np.concatenate((zero,down(np.cumsum(x.lo,axis=-1)-err)),axis=-1),
             np.concatenate((zero,up(np.cumsum(x.hi,axis=-1)+err)),axis=-1))

def integral_cells(initial,derivative,width):
    d=derivative*width
    p=prefix(d);full=initial+p[...,-1:]
    partial=I(np.minimum(d.lo,0.),np.maximum(d.hi,0.))
    return initial+p[...,:-1]+partial,full

def root_lookup(wanted,grid,height):
    # At a candidate g_i, strict lower H(g_i)>wanted.hi implies g_i is below
    # every root; strict upper H(g_i)<wanted.lo implies it is above every root.
    # On [0,1.397], H decreases since |g*h|<pi and h is nonzero on an open set.
    lesser=height.lo[None,:]>wanted.hi.reshape(-1,1)
    greater=height.hi[None,:]<wanted.lo.reshape(-1,1)
    lo=np.max(np.where(lesser,grid.lo[None,:],0.),axis=1)
    hi=np.min(np.where(greater,grid.hi[None,:],grid.hi[-1]),axis=1)
    exists=(height.lo[0]>=wanted.hi.reshape(-1))&(height.hi[-1]<=wanted.lo.reshape(-1))
    if np.any(lo>hi):raise ArithmeticError("contradictory wall intervals")
    return I(lo[:,None],hi[:,None]),exists
def broadcast(x,shape):
    return I(np.broadcast_to(x.lo,shape),np.broadcast_to(x.hi,shape))

def new_stat():
    return dict(pass_boxes=0,fail_boxes=0,unknown_boxes=0,root_unresolved_boxes=0,
                supremum_lower=None,supremum_upper=None)

def record(stat,x,name,phase_start,nt,ns,exists):
    count=len(exists);x=broadcast(x,(count,ns));ok=np.broadcast_to(exists[:,None],(count,ns))
    passes=x.hi<0;fails=x.lo>0
    stat["pass_boxes"]+=int(np.count_nonzero(ok&passes))
    stat["fail_boxes"]+=int(np.count_nonzero(ok&fails))
    stat["unknown_boxes"]+=int(np.count_nonzero(ok&~(passes|fails)))
    stat["root_unresolved_boxes"]+=int(np.count_nonzero(~ok))
    for key,arr,mask in (("supremum_lower",x.lo,ok),("supremum_upper",x.hi,None)):
        if mask is not None and not np.any(mask):continue
        candidate=arr if mask is None else np.where(mask,arr,-np.inf)
        i,j=np.unravel_index(int(np.argmax(candidate)),candidate.shape)
        z=float(candidate[i,j]);old=stat[key]
        if old is None or z>old["value"]:
            stat[key]=dict(value=z,piece=name,phase_bin=[int(phase_start+i),nt],
                           material_bin=[int(j),ns],root_bracket_verified=bool(exists[i]))

def verdict(s):
    if s["fail_boxes"]:return "strictly_positive_on_a_proved_box"
    if s["unknown_boxes"] or s["root_unresolved_boxes"]:return "unresolved"
    return "strictly_negative_everywhere"

def pass_level(nt,ns,ng,keep_local):
    all_stats={k:{} for k in ("left","common")};local_stats={k:{} for k in all_stats}
    measured=("raw_3d_minus_T","raw_XZ_minus_guard","flat_four_corner_squared_excess")
    for st in all_stats.values():
        for name in measured:st[name]=new_stat()
    u=unit_boxes(ns);wall_heading=heading(WALL*u)
    ggrid=rat("1.397")*I(np.arange(ng+1,dtype=float)/ng)
    gl,gh=[],[]
    # This table uses point arguments, including exactly 0 and the true decimal
    # 1.397; input constants are enclosed when converted to binary64.
    for i in range(0,ng+1,16):
        curve=cosine(ggrid[i:i+16,None]*wall_heading)
        heights=prefix(curve*(WALL/ns))[...,-1]
        gl.extend(heights.lo.tolist());gh.extend(heights.hi.tolist())
    heights=I(gl,gh);g0,ok0=root_lookup(rat(".92"),ggrid,heights)
    pieces={name:path_angles(name,u) for name in ("negative_bend","straight_tongue","U_turn")}
    phase=unit_boxes(nt);roots=dict(gamma0=[float(g0.lo[0,0]),float(g0.hi[0,0])],
                                     gamma0_verified=bool(ok0[0]),all_phases_verified=0,
                                     unresolved_phase_bins=[],gamma_range=[None,None],
                                     min_height_at_zero=float(heights.lo[0]),
                                     max_height_at_1_397=float(heights.hi[-1]))
    def charge(mode,what,x,piece,i,n,exists):
        record(all_stats[mode][what],x,piece,i,nt,n,exists)
        if keep_local:
            st=local_stats[mode].setdefault(piece,{}).setdefault(what,new_stat())
            record(st,x,piece,i,nt,n,exists)
    for i in range(0,nt,16):
        t=phase[i:i+16,None];ph=rat(".90")*t;batch=len(t.lo)
        valid=np.ones(batch,dtype=bool);startx=I(np.zeros((batch,1)));startz=startx
        def check(piece,raw_for,n,ok):
            for mode,c,e in (("left",I(0),I(0)),("common",rat(".12"),rat(".42"))):
                raw=raw_for(c)
                dy=PE+PB-e*t
                radius=((T-rat(".005")).square()-dy.square()).sqrt()
                guard=rat(".9")*radius if mode=="left" else radius-rat(".001")
                charge(mode,"raw_3d_minus_T",(raw.square()+dy.square()).sqrt()-T,piece,i,n,ok)
                charge(mode,"raw_XZ_minus_guard",raw-guard,piece,i,n,ok)
        # Prior left-wall/flat/straight sections have delta-q exactly zero.
        # Unit initial normal gives the reverse and direct triangle inequalities.
        def left_raw(c):
            d=c*t
            small=np.maximum(0.,np.maximum((DB-d).lo,(d-DB).lo))
            return I(small,(DB+d).hi)
        check("unchanged_prefix_all_normals",left_raw,1,valid)
        for mode,c,e in (("left",I(0),I(0)),("common",rat(".12"),rat(".42"))):
            d=c*t;dy=PE+PB-e*t
            excess=2*rat("1.30")*d+d.square()+DB.square()+dy.square()-T.square()
            charge(mode,"flat_four_corner_squared_excess",excess,"flat_four_corners",i,1,valid)
        def planar(c,beta,dx,dz):
            return ((c*t-dx+DB*sine(beta)).square()+(-dz-DB*cosine(beta)).square()).sqrt()
        for piece,(length,beta,weight) in pieces.items():
            fx,fz=tangent_difference(beta,ph*weight)
            dx,startx=integral_cells(startx,broadcast(fx,(batch,ns)),length/ns)
            dz,startz=integral_cells(startz,broadcast(fz,(batch,ns)),length/ns)
            check(piece,lambda c:planar(c,beta,dx,dz),ns,valid)
        check("straight_descent",lambda c:((c*t-startx-DB).square()+startz.square()).sqrt(),1,valid)
        wanted=rat(".92")+startz
        gamma,exists=root_lookup(wanted,ggrid,heights);exists=exists&ok0[0]
        roots["all_phases_verified"]+=int(np.count_nonzero(exists))
        roots["unresolved_phase_bins"].extend(int(i+j) for j in np.flatnonzero(~exists))
        l=float(np.min(gamma.lo));h=float(np.max(gamma.hi))
        if roots["gamma_range"][0] is None:roots["gamma_range"]=[l,h]
        else:roots["gamma_range"]=[min(l,roots["gamma_range"][0]),max(h,roots["gamma_range"][1])]
        beta=-HALF+g0*wall_heading
        fx,fz=tangent_difference(beta,(g0-gamma)*wall_heading)
        dx,_=integral_cells(startx,fx,WALL/ns);dz,_=integral_cells(startz,fz,WALL/ns)
        check("right_four_clock_wall",lambda c:planar(c,beta,dx,dz),ns,exists)
    for mode,stats in all_stats.items():
        for v in stats.values():v["sign_verdict"]=verdict(v)
    out=dict(phase_subintervals=nt,material_subintervals_per_variable_piece=ns,
             gamma_inverse_intervals=ng,closure=roots,registered_poses=all_stats)
    if keep_local:out["per_piece"]=local_stats
    return out

def main(folder):
    folder.mkdir(parents=True,exist_ok=True)
    path=folder/"interval.json";src=Path(__file__).resolve()
    actual=dict(schema="R774-continuum-registered-cap-chords-v1",run=os.getenv("GITHUB_RUN_ID"),
                attempt=os.getenv("GITHUB_RUN_ATTEMPT"),source_commit=os.getenv("R774_SOURCE_COMMIT"),
                source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),numpy_version=np.__version__,
                source_model="r774_common_left_body_and_complete_caps.py, exact real clocks and integral closure",
                model_git_blob="4c0e736366276321072e68ef2eaf5e5c8e5ad391",
                method="Outward IEEE basic interval operations; Machin rational pi; Taylor sine/cosine with absolute degree-35 remainder and midpoint Lipschitz radius; interval rectangle integrals with bounded prefix rounding; monotone gamma inversion.",
                domain="Upper full arclength chain from the common start, and its reflected lower half. phase_bin=[i,n] means theta/.90 in [i/n,(i+1)/n]. material_bin=[j,m] means normalized local arclength in [j/m,(j+1)/m]. Each unchanged extended piece is covered at once.",
                pieces=dict(negative_bend_length=".26",straight_tongue_length=".44",U_turn_length=".15*pi+.001",right_four_clock_wall_length=".95",left_and_descent="Constant delta-q, every point in each unchanged block is bounded."),
                units="Three-dimensional/raw guard excesses are lengths, flat four-corner excess is a squared length.",
                constants=dict(T=[float(T.lo),float(T.hi)],db=[float(DB.lo),float(DB.hi)],
                               pb=[float(PB.lo),float(PB.hi)],pE=[float(PE.lo),float(PE.hi)]),
                interpretation="A strictly positive raw 3D excess excludes that exact registered rigid-cap pose family at the interval witness. A positive guard excess only activates the curve clipping. A strict negative upper bound pays only the named chord inequality, not isometry, reach, existence of a fitting surface or arbitrary other rigid poses.",
                levels=[],completed=False)
    def save():
        data=(json.dumps(actual,ensure_ascii=False,separators=(",",":"),allow_nan=False)+"\n").encode()
        if len(data)>=100000:raise ValueError("public semantic certificate exceeds the single-file size limit")
        tmp=path.with_suffix(".tmp");tmp.write_bytes(data);tmp.replace(path)
    save()
    try:
        for nt,ns,ng in ((32,128,128),(128,512,512),(512,2048,2048)):
            row=pass_level(nt,ns,ng,nt==512);actual["levels"].append(row);save()
            print(json.dumps({"phase_bins":nt,"material_bins":ns,
                  "signs":{k:{m:v["sign_verdict"] for m,v in vals.items()} for k,vals in row["registered_poses"].items()}},
                  separators=(",",":")),flush=True)
        actual["completed"]=True;save()
    except Exception as exc:
        actual["error"]={"type":type(exc).__name__,"message":str(exc)};save();raise

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--folder",type=Path,required=True)
    main(p.parse_args().folder)
