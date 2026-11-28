#!/usr/bin/env python3
"""R317/R319 continuous position inequalities and both true physical arclength derivatives relative to the original R262 center.
Same-q original cut field with the new adjacent true circular windows and its own fixed metric refinement.
Intervals cover all original native angles separately from all material angles of the actual corrections.
"""
import argparse
import bisect
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import numpy as np

SAME="94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6"
CUT="4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8"
ANGLE="a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e"


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m
    spec.loader.exec_module(m)
    return m


def sha(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as f:
        for block in iter(lambda:f.read(2**20),b""):
            h.update(block)
    return h.hexdigest()


def fq(x):
    return F.from_float(float(x))


def array_q(I,seq):
    a=[I(v) for v in seq]
    return I(np.array([v.lo for v in a]),np.array([v.hi for v in a]))


def upper_sqrt(kern,x):
    v=np.maximum(0,x)
    h=kern.up(np.sqrt(v)+np.longdouble("1e-12"))
    h=np.where(v==0,0,h)
    if np.any((v>0)&(kern.down(h*h)<v)):
        raise ArithmeticError("vector square-root verification")
    return h


def native_cover(raw,kern,nang,corrected_after,cut_delta):
    # Original Hermite values use exact cumulative mean increments, not stored rounded cumulative heights.
    I=kern.I
    mesh=raw["mesh"]
    jets=raw["jets"]
    n=len(mesh)-1
    M=(jets.shape[-1]-2)//3
    mean=[F(0)]
    for v in raw["mean_increments"]:
        mean.append(mean[-1]+fq(v))
    p=I(jets[0])
    p.lo=p.lo.copy()
    p.hi=p.hi.copy()
    exact_mean=array_q(I,mean)
    p.lo[:,-1],p.hi[:,-1]=exact_mean.lo,exact_mean.hi
    h=(I(mesh[1:])-I(mesh[:-1])).reshape(n,1)
    d=I(jets[1])
    dd=I(jets[2])
    controls=[p[:-1],p[:-1]+h*d[:-1]/5,p[:-1]+2*h*d[:-1]/5+h.square()*dd[:-1]/20,
              p[1:]-2*h*d[1:]/5+h.square()*dd[1:]/20,p[1:]-h*d[1:]/5,p[1:]]
    phi=kern.PI*I(np.arange(nang,dtype=int),np.arange(1,nang+1,dtype=int))/nang
    trig=[kern.sincos(k*phi) for k in range(1,M+1)]
    rho=np.zeros((n,nang),dtype=kern.LD)
    zlo=np.full_like(rho,np.inf)
    zhi=np.full_like(rho,-np.inf)
    for ctrl in controls:
        R=ctrl[:,0].reshape(n,1)
        T=I(0)
        Z=ctrl[:,-1].reshape(n,1)
        for k,(s,c) in enumerate(trig,1):
            R=R+ctrl[:,k].reshape(n,1)*c
            T=T+ctrl[:,M+k].reshape(n,1)*s
            Z=Z+ctrl[:,2*M+k].reshape(n,1)*c
        rho=np.maximum(rho,upper_sqrt(kern,(R.square()+T.square()).hi))
        zlo=np.minimum(zlo,Z.lo)
        zhi=np.maximum(zhi,Z.hi)
    # On each old native cell, the same nonnegative degree-five Bernstein weights enter XYZ.
    # The planar rotation of (R,T) preserves radius. All psi have been covered.
    pad=I(cut_delta)
    rho[corrected_after:]=kern.up(rho[corrected_after:]+pad.hi)
    zlo[corrected_after:]=kern.down(zlo[corrected_after:]-pad.hi)
    zhi[corrected_after:]=kern.up(zhi[corrected_after:]+pad.hi)
    return rho,zlo,zhi


SUPPORT=[0.09999976505231697,0.00017340635052370438,-0.000020726030862500148,2.732239542665825e-9,1.364904959536114e-9,-6.697024595314116e-10,2.5420195020236015e-11,2.7693941053364423e-11,2.279645039764186e-11,7.050341026639808e-10,5.749608505622311e-11,2.4233142751359304e-10]

def adjacent_trace(raw,meta,kern,anchor,n=4096):
    I=kern.I
    span=kern.PI*F(2,3)
    U=span/2
    def enclose_decimal(s):
        v=F(s);w=fq(float(s))
        return I.bounds(min(v,w),max(v,w))
    k=enclose_decimal(".63")
    v0=enclose_decimal(".536")
    v1=enclose_decimal(".548")
    ends=[I(0),v0,v1,U]
    t=I(np.arange(n),np.arange(1,n+1))/n
    def gate_at(p):
        return p**3*(10+p*(-15+6*p))
    ones=np.ones(n,dtype=kern.LD)
    g=I(gate_at(I(t.lo)).lo,gate_at(I(t.hi)).hi)
    arrays=[]
    for l,(a,b) in enumerate(zip(ends[:-1],ends[1:])):
        dv=(b-a)/n;v=a+(b-a)*t
        gate=[I(0),g,I(1)][l]
        rb=I(1)
        for h,cf in enumerate(SUPPORT,1):
            rb+=I(fq(cf)*(1-9*h*h)*(-1)**h)*kern.sincos((3*h)*v)[1]
        arrays.append((v,dv,I(ones)*(1-gate)/k,gate*rb))
    offset=sum((dv*aa.sum() for v,dv,aa,bb in arrays),I(0))
    mass=sum((dv*bb.sum() for v,dv,aa,bb in arrays),I(0))
    scale=(U-offset)/mass
    def join(items):
        return I(np.concatenate([v.lo for v in items]),np.concatenate([v.hi for v in items]))
    ds=[];dx=[];dy=[];angles=[];rads=[]
    for l,(v,dv,aa,bb) in enumerate(arrays):
        r=aa+bb*scale
        si,co=kern.sincos(v)
        ds.append(r*dv);dx.append(-r*dv*si);dy.append(r*dv*co)
        angles.append(ends[l]+(ends[l+1]-ends[l])*I(np.arange(n))/n);rads.append(r)
    def cum(a):
        lo=np.empty(len(a.lo)+1,dtype=kern.LD);hi=np.empty_like(lo)
        lo[0]=hi[0]=0
        for j in range(len(a.lo)):
            lo[j+1]=kern.down(lo[j]+a.lo[j]);hi[j+1]=kern.up(hi[j]+a.hi[j])
        return I(lo,hi)
    rad=join(rads)
    require(np.min(rad.lo)>0,"positive physical curvature radius")
    gmax=(1/rad).hi.max()
    arc=cum(join(ds));xx=cum(join(dx));yy=cum(join(dy))
    phi=join(angles+[I(np.atleast_1d(U.lo),np.atleast_1d(U.hi))])
    su,cu=kern.sincos(U)
    A=-xx[-1]+cu*yy[-1]/su
    # The normalized new curve has true final arclength U by its defining integral identity.
    arc.lo[-1]=U.lo;arc.hi[-1]=U.hi
    require(np.all(np.diff(arc.lo[:-1])>=0) and np.all(np.diff(arc.hi[:-1])>=0),"slope regularity")
    theta=span*I(np.arange(n),np.arange(1,n+1))/n
    e0=8*fq(meta["warp_reference_q"])*fq(meta["chart"]["values"][0])
    require(abs(e0)<1,"old material angle not regular")
    u=(theta-I(e0)*kern.sincos(3*theta)[0]/3).widen(I(F(26,10**11)))
    row=raw["jets"][0,0];M=(len(row)-2)//3
    require(np.count_nonzero(row[2*M+1:])==0,"original center not planar")
    R,T=I(fq(row[0])),I(0)
    R1,T1,R2,T2=I(0),I(0),I(0),I(0)
    for h in range(1,M+1):
        m=3*h
        si,co=kern.sincos(m*theta)
        cr,ct=I(fq(row[h])),I(fq(row[M+h]))
        R+=cr*co;T+=ct*si
        R1-=m*cr*si;T1+=m*ct*co
        R2-=m*m*cr*co;T2-=m*m*ct*si
    si,co=kern.sincos(theta)
    mean=I.bounds(1-F(7,10**15),1-F(4,10**15))
    px=(R*co-T*si)/mean;py=(R*si+T*co)/mean
    vr=R1-T;vt=T1+R
    ar=R2-R-2*T1;at=T2-T+2*R1
    speed=(vr.square()+vt.square()).sqrt()
    tx=(vr*co-vt*si)/speed;ty=(vr*si+vt*co)/speed
    oldK=mean*(vr*at-vt*ar)/speed**3
    off=u+I(anchor)
    mid=(off.lo+off.hi)/2
    sector=np.rint(mid/float(span.lo)).astype(int)
    rel=mid-sector*float(span.lo)
    sign=np.where(rel<0,-1,1)
    # This approximate nearest node only chooses a comparison point; its actual signed
    # material error is paid for by the interval calculation immediately below.
    mids=(arc.lo+arc.hi)/2
    mids[-1]=max(mids[-2],mids[-1])
    ix=np.clip(np.searchsorted(mids,abs(rel)),0,len(mids)-1)
    prv=np.maximum(0,ix-1)
    ix=np.where(abs(mids[prv]-abs(rel))<abs(mids[ix]-abs(rel)),prv,ix)
    nominal=I(sector)*span+I(sign)*arc[ix]
    pad=I((off-nominal).abs_upper())
    sn,cn=kern.sincos(I(sector)*span-I(anchor))
    x=xx[ix]+A;y=I(sign)*yy[ix]
    zx=cn*x-sn*y;zy=sn*x+cn*y
    nY,nX=kern.sincos(I(sector)*span-I(anchor)+I(sign)*phi[ix])
    # The true distance to the nearest symmetry axis on the periodic physical
    # material line is 1-Lipschitz. This also covers crossing either reflected seam.
    near=arc[ix].widen(pad)
    # Use only interior nodes for searches; the normalization fixes the exact end.
    l=np.clip(np.searchsorted(arc.hi[:-1],near.lo,side="left")-1,0,len(rad.lo)-1)
    rr=np.clip(np.searchsorted(arc.lo[:-1],near.hi,side="right")-1,0,len(rad.lo)-1)
    inv=1/rad
    K=I(np.array([inv.lo[i:j+1].min() for i,j in zip(l,rr)]),
        np.array([inv.hi[i:j+1].max() for i,j in zip(l,rr)]))
    refNormalX=ty;refNormalY=-tx
    def norm(x,y):return I(upper_sqrt(kern,(x.square()+y.square()).hi))
    dp=norm(zx-px,zy-py)+pad
    dt=norm(-nY-tx,nX-ty)+I(gmax)*pad
    dk=I((K-oldK).abs_upper())
    da=norm(K*nX-oldK*refNormalX,K*nY-oldK*refNormalY)+I(gmax)**2*pad
    def describe(z):
        true=kern.exact(np.max(z.hi))
        return dict(upperExact=str(true),upper=float(true),angularCell=int(np.argmax(z.hi)))
    return dict(nativeSectorAngleBoxes=n,normalAnglePanels=3*n,curvePosition=describe(dp),unitTangent=describe(dt),
        signedCurvature=describe(dk),curvatureVector=describe(da),actualMeanInterval=["1-7e-15","1-4e-15"],
        trueMaterialCoordinate="R226 normalized original U0(theta); D3 on the material circle",
        radiusBounds=[float(np.min(rad.lo)),float(np.max(rad.hi))],scaleBounds=[float(scale.lo),float(scale.hi)])

def s5(t):
    t=max(F(0),min(F(1),t))
    return t**3*(10+t*(-15+6*t))


def deboor(knot,coef,d,x):
    if x<=knot[0]:return coef[0]
    if x>=knot[-1]:return coef[-1]
    j=bisect.bisect_right(knot,x)-1
    v=list(coef[j-d:j+1])
    for a in range(1,d+1):
        for k in range(d,a-1,-1):
            left=knot[j-d+k];right=knot[j+1+k-a]
            t=(x-left)/(right-left)
            v[k]=(1-t)*v[k-1]+t*v[k]
    return v[-1]


def require(ok,message):
    if not ok:raise ValueError(message)


def old_bounds(a,kern,raw,meta,bridge,cut):
    fld=a.work/"h2-c2-m48-g12-04r1"
    field=fld/"result.json.field.npz"
    query=fld/"exact-tail-queries.json"
    cache=Path(str(query)+".npz")
    report=json.loads(query.read_text())
    require(report["endpoint_cache_sha256"]==sha(cache) and report["manifest_sha256"]==cut.MANIFEST_SHA,
            "old tail and common cut came from another source")
    _,width,m,delta=cut.correction_bounds(raw,meta,bridge,cache)
    common=sum((row[0]+F(2,5)*width*row[1]+width**2*row[2]/20 for row in delta),F(0))
    with np.load(field,allow_pickle=False) as f:
        pm=f["planar_modes"]
        hm=f["vertical_modes"]
        coeff=f["coefficients"]
        require(coeff.shape[1]==len(pm)+len(hm) and len(f["unit_knots"])==len(coeff)+12 and
                np.all(np.diff(f["unit_knots"])>=0),"old full field dimensions")
        xy=max(sum(map(abs,map(fq,row[:len(pm)])),F(0)) for row in coeff)
        z=max(sum(map(abs,map(fq,row[len(pm):])),F(0)) for row in coeff)
    tol=F(253,10**12)
    rho,zlo,zhi=native_cover(raw,kern,a.angles,int(meta["correction_start_index"]),common)
    rho=kern.up(rho+kern.I(xy+tol).hi)
    zlo=kern.down(zlo-kern.I(z+tol).hi)
    zhi=kern.up(zhi+kern.I(z+tol).hi)
    return (rho,zlo,zhi),xy,z,common,sha(field)



def sharp_cut(a,state,common,old_cut,raw,meta,kern,mesh,s0,s1,r,sphere,mixed,lowz,mask,limits,arm):
    """For identity-gate late cells, enclose the correlated complete XYZ, using the exact angle charts."""
    I=kern.I
    old=load(a.scripts/"6a65-m12-original-common-cut-prefix-source-bounds.py","R312sharpCommon")
    spline=load(a.scripts/"6a65-m12-weak-stress-recovered-v2.py","R312sharpSpline")
    knot_chart,poly_chart=spline.exact_clamped_spline(meta["chart"])
    end=mesh[-1];warp=8*fq(meta["warp_reference_q"]);e0=warp*poly_chart[0][0]
    def e_range(i):
        l,rr=mesh[i]/end,mesh[i+1]/end
        packed=[]
        for j,(a0,b0) in enumerate(zip(knot_chart,knot_chart[1:])):
            x=max(l,a0);y=min(rr,b0)
            if x>=y:continue
            ed=sorted(set([x,y]+([F(3,4)] if x<F(3,4)<y else [])))
            for x,y in zip(ed,ed[1:]):
                pol=old.compose(poly_chart[j],x-a0,y-x)
                if x>=F(3,4):
                    pol=old.product(old.compose(poly_chart[j],x-a0,y-x),
                                    old.compose([1,0,0,-10,15,-6],4*x-3,4*(y-x)))
                packed.extend(warp*v for v in old.bernstein(pol))
        return I.bounds(min(packed),max(packed))
    kn=list(map(fq,state["knots"]))
    W=np.pad(state["actualPhysicalXYZ"],((3,3),(0,0)))
    m=int(state["modes"])
    # The remaining psi domain is a sextant only under these literal channel equalities.
    if np.any(W[:,0]) or any(np.any(W[:,k]) or np.any(W[:,m+k]) for k in range(3,m+1,3)):
        raise ValueError("D3 zero channels differ")
    for k in range(1,m+1):
        if k%3 and not np.array_equal(W[:,m+k], (1 if k%3==1 else -1)*W[:,k]):
            raise ValueError("D3 planar mode differs")
        if k%3 and np.any(W[:,2*m+1+k]):raise ValueError("D3 vertical mode differs")
    def literal_radii(x,h):
        i=bisect.bisect_right(kn,x)-1
        if x<=kn[0]:v=I(W[0])
        elif x>=kn[-1]:v=I(W[-1])
        else:
            vals=[I(w) for w in W[i-5:i+1]]
            for level in range(1,6):
                for j in range(5,level-1,-1):
                    left=kn[i-5+j];right=kn[i+1+j-level]
                    t=I((x-left)/(right-left))
                    vals[j]=(1-t)*vals[j-1]+t*vals[j]
            v=vals[-1]
        slope=np.zeros(W.shape[1],dtype=kern.LD)
        for j in range(len(W)-1):
            if kn[j+1]>=x+h or kn[j+6]<=x-h:continue
            if kn[j+6]==kn[j+1]:continue
            diff=5*(I(W[j+1])-I(W[j]))/I(kn[j+6]-kn[j+1])
            slope=np.maximum(slope,diff.abs_upper())
        return v.widen(I(slope)*I(h))
    def theta_enclosure(u):
        vals=[]
        for endpoint in (u.lo,u.hi):
            # Numerical angle is a freely chosen center; the true inverse follows from the signed residual.
            t=endpoint.copy();ef=float(e0)
            for unused in range(9):t-=(t-ef*np.sin(3*t)/3-endpoint)/(1-ef*np.cos(3*t))
            q=I(t);v=q-I(e0)*kern.sincos(3*q)[0]/3-I(endpoint)
            err=I(v.abs_upper())/(1-I(abs(e0)))+F(13,10**11)
            vals.append(q.widen(err))
        return I(vals[0].lo,vals[1].hi)
    oldxy,oldz=common[1:3]
    old_R=I(F(2131902881202937,1125899906842624)+oldxy+oldz+F(253,10**12))
    mean=[F(0)]
    for v in raw["mean_increments"]:mean.append(mean[-1]+fq(v))
    jets=raw["jets"];M=(jets.shape[-1]-2)//3
    D2=I(limits[1]).lo;Dmix2=I(limits[2]).lo;Rp=I(limits[0]).lo
    cutoff=max(fq(state["liftEnd"]),fq(state["fullSleeve"])+fq(state["fullGate"]))
    n=max(384,a.angles)
    psi=kern.PI*I(np.arange(n),np.arange(1,n+1))/(3*n)
    sk,ck=kern.sincos(psi)
    old_trig=[kern.sincos(3*k*psi) for k in range(1,M+1)]
    angular3=old_trig[0][0]
    critical=np.flatnonzero(mask&((sphere.max(axis=1)>D2)|(mixed.max(axis=1)>Dmix2)|(r.max(axis=1)>Rp)))
    red=0
    for i in critical:
        qlo=s0*mesh[i]/end;qhi=s1*mesh[i+1]/end
        if qlo<cutoff:continue
        e=e_range(i)
        u=psi-e*angular3/3
        theta=theta_enclosure(u)
        coeff=literal_radii((qlo+qhi)/2,(qhi-qlo)/2)
        wx=coeff[0];wy=I(0);wz=coeff[2*m+1]
        for k in range(1,m+1):
            skk,ckk=kern.sincos(k*theta)
            wx=wx+coeff[k]*ckk;wy=wy+coeff[m+k]*skk;wz=wz+coeff[2*m+1+k]*ckk
        wr=wx*ck+wy*sk;wt=-wx*sk+wy*ck
        w2=wx.square()+wy.square()+wz.square()
        h=I(mesh[i+1]-mesh[i])
        p0=I(jets[0,i]);p1=I(jets[0,i+1])
        p0=I(p0.lo.copy(),p0.hi.copy());p1=I(p1.lo.copy(),p1.hi.copy())
        p0.lo[-1],p0.hi[-1]=I(mean[i]).lo,I(mean[i]).hi
        p1.lo[-1],p1.hi[-1]=I(mean[i+1]).lo,I(mean[i+1]).hi
        v0=I(jets[1,i]);v1=I(jets[1,i+1]);a0=I(jets[2,i]);a1=I(jets[2,i+1])
        controls=[p0,p0+h*v0/5,p0+2*h*v0/5+h.square()*a0/20,
                  p1-2*h*v1/5+h.square()*a1/20,p1-h*v1/5,p1]
        dx=I(oldxy+F(253,10**12)+(old_cut if i>=meta["correction_start_index"] else 0))
        dz=I(oldz+F(253,10**12)+(old_cut if i>=meta["correction_start_index"] else 0))
        bounds=np.zeros((3,n),dtype=kern.LD)
        scalar=np.full(n,-np.inf,dtype=kern.LD)
        for cc in controls:
            nr=cc[0];nt=I(0);zz=cc[-1]
            for k,(so,co) in enumerate(old_trig,1):
                nr=nr+cc[k]*co;nt=nt+cc[M+k]*so;zz=zz+cc[2*M+k]*co
            nr=nr.widen(dx);nt=nt.widen(dx);zz=zz.widen(dz)
            scalar=np.maximum(scalar,(nr*wr+nt*wt+zz*wz).hi)
            rho2=(nr+wr).square()+(nt+wt).square()
            znew=zz+wz
            xy=I(upper_sqrt(kern,rho2.hi))
            bounds[0]=np.maximum(bounds[0],xy.hi)
            bounds[1]=np.maximum(bounds[1],(rho2+znew.square()).hi)
            bounds[2]=np.maximum(bounds[2],((I(arm)+xy).square()+(F(233,1000)+I(znew.abs_upper())).square()).hi)
        bounds[1]=np.minimum(bounds[1],(old_R.square()+2*I(scalar)+w2).hi)
        r[i]=np.minimum(r[i],bounds[0].max())
        sphere[i]=np.minimum(sphere[i],bounds[1].max())
        mixed[i]=np.minimum(mixed[i],bounds[2].max())
        red+=1
    return {"lateNativeCellsReevaluated":red,"actualCorrelatedMaterialAngleBoxes":n,"rawOriginalNormUsed":str(F(2131902881202937,1125899906842624))}


def parent_state(a,state,physical,common,raw,meta,bridge,kern,cache_pad):
    I=kern.I
    field_hash,old_xy,old_z,old_data,old_cut=common
    require(str(state["fieldSHA"])==field_hash and str(state["sourceSHA"])==physical and
            str(state["comparisonSHA"])==ANGLE and float(state["lam"])==1.,"actual input binding")
    low=fq(state["low"])
    anchor=fq(state["anchor"])
    c=fq(state["fullSleeve"])
    require(float(low)==.63 and float(c) in (.350,.545,.660,.780) and str(state["cutSHA"])==CUT,"unpaid true port or cut")
    if (low,anchor) not in cache_pad:
        cache_pad[low,anchor]=adjacent_trace(raw,meta,kern,anchor,a.trace_angles)
    comparisons=cache_pad[low,anchor]
    arc=F(comparisons["curvePosition"]["upperExact"])
    # Use the exact bridge as well as the direct stored affine parameterization throughout.
    lam=bridge["arclength_rescale"]
    mesh=list(map(fq,raw["mesh"]))
    total=mesh[-1]
    s0=total/F(lam["hi"])
    s1=total/F(lam["lo"])
    sd=fq(state["S"])
    s0=min(sd,s0);s1=max(sd,s1)
    known={"fieldSHA","sourceSHA","comparisonSHA","S","T","fullGate","fullSleeve","liftEnd","heightDropEnd",
           "rawDropKnots","rawDropVelocity","reduced","actualPhysicalXYZ","metricQ","metricW","metricKnots",
           "knots","lam","low","anchor","modes","spans","cutSHA"}
    require(set(state.files)<=known,"unknown additional state arrays; bind any separate physical correction before evaluation")
    W=state["actualPhysicalXYZ"]
    m=int(state["modes"])
    kn=list(map(fq,state["knots"]))
    require(W.shape==(len(kn)-12,3*m+2) and all(x<=y for x,y in zip(kn,kn[1:])),"new genuine open spline")
    require(kn[:6]==[kn[0]]*6 and kn[-6:]==[kn[-1]]*6 and
            all(kn.count(v)<=5 for v in set(kn[6:-6])),"clamped two-jet spline supports")
    # X cos/Y sin coefficients at each k give a planar ellipse of radius max(|a|,|b|).
    rows=[(abs(fq(row[0]))+sum((max(abs(fq(row[j])),abs(fq(row[m+j]))) for j in range(1,m+1)),F(0)),
           sum((abs(fq(v)) for v in row[2*m+1:]),F(0))) for row in W]
    width=fq(state["fullGate"])
    lift=lambda q:F(0)
    liftend=fq(state["liftEnd"])
    D=F("3.830");arm=F("2.194");Rp=D/2
    rho,oldlo,oldhi=old_data
    pxy=[];pz=[];axlo=[];axhi=[];mixlo=[];mixhi=[]
    for cell,(left,right) in enumerate(zip(mesh[:-1],mesh[1:])):
        qlo=s0*left/total;qhi=s1*right/total
        qpad=arc*(1-s5(qlo/liftend))
        use=[v for i,v in enumerate(rows) if kn[i+3]<qhi and kn[i+9]>qlo]
        pxy.append(qpad+max([F(0)]+[v[0] for v in use]))
        pz.append(max([F(0)]+[v[1] for v in use]))
        axlo.append(lift(qhi));axhi.append(lift(qlo))
        if physical==SAME:
            mixlo.append(s5((qlo-c)/width));mixhi.append(s5((qhi-c)/width))
    r=kern.up(rho+array_q(I,pxy).hi[:,None])
    plus=array_q(I,pz).hi[:,None]
    lowz=kern.down(kern.down(oldlo+array_q(I,axlo).lo[:,None])-plus)
    highz=kern.up(kern.up(oldhi+array_q(I,axhi).hi[:,None])+plus)
    if physical==SAME:
        # Actual X is (1-g) cylinder + g(old+arc lift) + learned W. W vanishes up to c;
        # assign the full W bound to both endpoints to keep the convex estimate valid.
        qa=array_q(I,[s0*v/total for v in mesh[:-1]])
        qb=array_q(I,[s1*v/total for v in mesh[1:]])
        gate=I(array_q(I,mixlo).lo[:,None],array_q(I,mixhi).hi[:,None])
        baseR=I(F("1.278"))+array_q(I,[max([F(0)]+[v[0] for i,v in enumerate(rows)
                 if kn[i+3]<s1*y/total and kn[i+9]>s0*x/total]) for x,y in zip(mesh[:-1],mesh[1:])]).reshape(-1,1)
        r=((1-gate)*baseR+gate*I(r)).hi
        lowz=((1-gate)*I(kern.down(qa.lo[:,None]-plus))+gate*I(lowz)).lo
        highz=((1-gate)*I(kern.up(qb.hi[:,None]+plus))+gate*I(highz)).hi
        mask=qb.hi>=float(c)
    else:mask=np.ones(len(mesh)-1,dtype=bool)
    zabs=np.maximum(abs(lowz),abs(highz))
    sphere=(I(r).square()+I(zabs).square()).hi
    mixed=((I(arm)+I(r)).square()+(I(F(".233"))+I(zabs)).square()).hi
    def worst(x):
        val=x[mask]
        ij=np.unravel_index(np.argmax(val),val.shape)
        i=np.flatnonzero(mask)[ij[0]]
        return {"upperExact":str(kern.exact(val[ij])),"upper":float(val[ij]),"nativeCell":int(i),
                "nativeAngleBox":int(ij[1]),"sourceInterval":[float(mesh[i]),float(mesh[i+1])]}
    limits=[Rp,D**2/4,D**2]
    sharp=sharp_cut(a,state,common,old_cut,raw,meta,kern,mesh,s0,s1,r,sphere,mixed,lowz,mask,limits,arm) if physical==SAME else None
    rec=[worst(v) for v in (r,sphere,mixed)]
    # R25 position budget for the original exact tail; actual old W is included across every knot.
    # The terminal flat disks lie below 1.823242 and inside radius .15; central C vanishes on tail.
    tail=[F(".60014")+old_xy,F("1.888068")+old_xy+old_z,F("1.824077")+old_z]
    tail_ok=tail[0]<F(".601") and tail[1]<F("1.889") and tail[2]<F("1.825")
    return dict(schema="continuous-R317-actual-adjacent-low-ports-cut-with-complete-tail",trueOriginalTrace=comparisons,
       fieldSHA=field_hash,sharpFullLateCut=sharp,low=float(low),sleeve=float(c),sourceSHA=physical,centerDeltaUpper=str(arc),
       centerDeltaUpperDisplay=float(arc),allOriginalCells=len(mesh)-1,angularBoxesPerOriginalHalfPeriod=a.angles,
       rawCommonGeometrySourceBound=True,originalLearnedPositionBounds=[str(old_xy),str(old_z)],
       physicalTailPlanarNormHeightUpper=[str(q) for q in tail],tailPass=bool(tail_ok),
       limits=[str(v) for v in limits],positionBounds=rec,externalZLowerExact=str(kern.exact(lowz[mask].min())),
       externalZLower=float(lowz[mask].min()),newPrefixSufficientBounds=all(F(v["upperExact"])<=l for v,l in zip(rec,limits)),
       allR317PositionBudgets=bool(tail_ok and all(F(v["upperExact"])<=l for v,l in zip(rec,limits))))


def main(a):
    S=a.scripts
    kern=load(S/"m12-correlated-gram-interval-kernel.py","R312directedPositions")
    cut=load(S/"6a65-m12-original-common-cut-prefix-source-bounds.py","R312CommonPort")
    notes=S.parent/"notes"
    mp=notes/"2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json"
    bp=notes/"2026-11-09-db6f-root-exact-bridge-m12.json"
    dp=a.work/"m12-prefix-data.npz.gz"
    require([sha(p) for p in (mp,bp,dp)]==[cut.META_SHA,cut.BRIDGE_SHA,cut.DATA_SHA],"old exact original definition")
    meta=json.loads(mp.read_text());bridge=json.loads(bp.read_text())
    with np.load(io.BytesIO(gzip.decompress(dp.read_bytes())),allow_pickle=False) as payload:
        raw={k:payload[k].copy() for k in ("mesh","jets","mean_increments")}
    if a.trace_only:
        record=adjacent_trace(raw,meta,kern,fq(np.pi/3),a.trace_angles)
        result=dict(sourceSHA=sha(__file__),originalDataSHA=sha(dp),physicalSourceSHA=SAME,comparison=record)
        with a.out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
        print('R317_RAW_CONTINUOUS',json.dumps(record),flush=True)
        return
    require(a.states,"supply actual R317 states or --trace-only")
    field,wx,wz,dc,h=old_bounds(a,kern,raw,meta,bridge,cut)
    common=(h,wx,wz,field,dc);cache={}
    print("R317_RAW_MATERIAL_READY",float(dc),float(wx),float(wz),flush=True)
    out=[]
    for path in a.states:
        with np.load(path,allow_pickle=False) as st:
            physical=str(st["sourceSHA"])
            require(physical==SAME,"unknown physical definition: "+physical)
            rec=parent_state(a,st,physical,common,raw,meta,bridge,kern,cache)
        rec["stateSHA"]=sha(path);rec["stateName"]=path.name
        out.append(rec)
        print("R317_ACTUAL_CONTINUOUS",path.name,rec["newPrefixSufficientBounds"],[v["upper"] for v in rec["positionBounds"]],
              "external-z",rec["externalZLower"],flush=True)
    result=dict(sourceSHA=sha(__file__),originalSourceSHA=sha(dp),oldRawFieldSHA=h,
                commonCutCoordinatePaddingExact=str(dc),guards=["R21 original common cut","R226 |C|<2.53e-10",
                "R226 inverse central angle error","R25 complete tail original positions","R317 new adjacent double-low central radial support"],states=out)
    with a.out.open("x") as f:
        json.dump(result,f,indent=2,allow_nan=False)
        f.write("\n")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    for key in ("scripts","work","out"):
        p.add_argument("--"+key,type=Path,required=True)
    p.add_argument("--states",type=Path,nargs="+")
    p.add_argument("--trace-only",action="store_true")
    p.add_argument("--trace-angles",type=int,default=4096)
    p.add_argument("--angles",type=int,default=48)
    main(p.parse_args())
