#!/usr/bin/env python3
"""Continuous six jets, Gram, curvature, support and size of the released full-tail Cartesian correction."""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import sys
import numpy as np


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m
    spec.loader.exec_module(m)
    return m


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ff(x):
    return F.from_float(float(x))


def fracrows(x):
    return [[ff(y) for y in row] for row in np.asarray(x)]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('scripts','work','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--state',type=Path,help='new whole-half NPZ; omit only for the reconstructed base-tail audit')
    p.add_argument('--parent',type=Path)
    p.add_argument('--angles',type=int,default=192)
    p.add_argument('--radial-subdivisions',type=int,default=4)
    a=p.parse_args()
    if a.out.exists() or a.angles<8 or a.radial_subdivisions<1:raise ValueError('Invalid report, radial or angular options')
    S=a.scripts;notes=S.parent/'notes'
    native=load(S/'prefix-production-kernel/m12-prefix-total-gram-full.py','wT_original_prefix')
    core=load(S/'2ecf-r262-true-three-arcs-cut-directed-position-kernel.py','wT_true_cartesian_kernel')
    core.setup(native)
    k=native.kern;I=k.I;B=load(S/'6a65-m12-local-bernstein-angular-metric-budget.py','wT_bernstein')
    supplier=load(S/'78718-prefix-metric-supplier-storage-v1.py','wT_original_chart')
    data=a.work/'m12-prefix-data.npz.gz'
    g=a.work/'h2-c2-m48-g12-04r1';wp=g/'result.json.field.npz'
    if sha(wp)!='e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a' or sha(data)!=B.DATA_SHA:raise ValueError('Unknown true G12 field or reference')
    def frozen(name,digest):
        f=notes/name
        if sha(f)!=digest:raise ValueError(name)
        return json.loads(f.read_text())
    meta=frozen('2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json',B.META_SHA)
    bridge=frozen('2026-11-09-db6f-root-exact-bridge-m12.json',B.BRIDGE_SHA)
    manifest=frozen('2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json',B.MANIFEST_SHA)
    budget=frozen('2026-11-09-db6f-prefix-m12-segment-ball-budget.json','f08875b25cc46328e0c04171fdbf7f50b802dac6951381e4fb2c64d5839c483c')
    rCut,rCuff=[ff(manifest['parameters'][n]) for n in ('rCut','rCuff')];h=rCut-rCuff
    cfg=meta['frozen_profile'];delta,vu,vd,eps=[ff(cfg[n]) for n in ('delta','vu','vd','ramp')]
    span=delta/((1-eps)*vu)+delta/((1-eps)*vd)
    SL=span+F(bridge['exact_L']['lo']);SH=span+F(bridge['exact_L']['hi'])
    SS=I.bounds(SL,SH);TT=SS+h
    _,ch=supplier.exact_clamped_spline(meta['chart'])
    with np.load(io.BytesIO(gzip.decompress(data.read_bytes())),allow_pickle=False) as raw:
        rows=fracrows(raw['jets'][:,0,:]);end=ff(raw['mesh'][-1])
    C=native.base.centralmod.Central(rows,8*ff(meta['warp_reference_q'])*ch[0][0],16*ff(meta['warp_reference_q'])*ch[0][2]/end**2)
    with np.load(wp,allow_pickle=False) as w:
        kw=list(map(ff,w['unit_knots']));pm=list(map(int,w['planar_modes']));zm=list(map(int,w['vertical_modes']))
        oldpower=[(l,r,core.power(b)) for l,r,b in B.extract_bezier(kw,fracrows(w['coefficients']))]
    complete=a.state is not None
    generator='86833bbafd7715c924916f48f3c8b3325cb8a4008d7b7a95398b9e5546621841'
    if complete:
        if a.parent is None:raise ValueError('Missing actual prefix parent')
        with np.load(a.parent,allow_pickle=False) as st:
            if str(st['fieldSHA'])!=sha(wp) or 'heightDropEnd' in st:raise ValueError('Not the true original stationary tail family')
            physicalSources={'94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6','29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902','e680b0027ae94d138cee8ac5488169927324df3afab58ec74b5e76c569e24a3e'}
            if str(st['sourceSHA']) not in physicalSources or str(st['cutSHA'])!='4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8':
                raise ValueError('Another prefix or common-cut source')
            phS,phT,phc=map(ff,(st['S'],st['T'],st['fullSleeve']));c=F(str(float(st['fullSleeve'])))
        with np.load(a.state,allow_pickle=False) as st:
            if set(st.files)!={'sourceSHA','parentSHA','fieldSHA','unitKnots','wholeTailXYZ','modes','c','actualCommonCut','actualCuffCoordinate'}:raise ValueError('Unknown new correction channels')
            if str(st['sourceSHA'])!=generator or str(st['parentSHA'])!=sha(a.parent) or str(st['fieldSHA'])!=sha(wp):raise ValueError('Unbound whole-half correction')
            if [ff(st[n]) for n in ('actualCommonCut','actualCuffCoordinate','c')]!=[phS,phT,phc]:raise ValueError('Different physical knots or seam')
            kn=list(map(ff,st['unitKnots']));m=int(st['modes']);x=st['wholeTailXYZ'].copy()
        if x.shape!=(len(kn)-12,3*m+2) or not np.isfinite(x).all() or kn!=sorted(kn) or kn[:6]!=[F(0)]*6 or kn[-6:]!=[F(1)]*6 or any(kn.count(t)>3 for t in set(kn) if 0<t<1):raise ValueError('Invalid complete physical quintic')
        newpower=[(l,r,core.power(b)) for l,r,b in B.extract_bezier(kn,fracrows(x))]
        # Every actual column is evaluated; no D3 reduction is assumed for the new field.
    else:
        c=F(0);newpower=[(F(0),F(1),None)];m=0
    def vspan(l,r,offset):
        # v=1-(1-t)*(1+(S-offset)/h); monotone in t, antitone in S.
        return max(F(0),1-(1-l)*(1+(SH-offset)/h)),min(F(1),1-(1-r)*(1+(SL-offset)/h))
    kk=2/I(5).sqrt();aa=1-kk;bb=F(28)*h/(25*rCut)
    R=[I(0),kk,-bb/2,6*aa+3*bb/2,-8*aa-3*bb/2,3*aa+bb/2]
    Rp=[j*x for j,x in enumerate(R) if j];Rpp=[j*x for j,x in enumerate(Rp) if j]
    n=a.angles
    edge=I(np.arange(n+1,dtype=k.LD))*2*k.PI/n
    theta=I(edge.lo[:-1],edge.hi[1:]);tr=core.BoxTrig(theta)
    dtheta=k.Jet.variable(theta,1)
    speed=C.speed(dtheta,core.Tr(dtheta))
    inv=C.a/speed.c[0];inv2=-C.a.square()*speed.c[1]/(speed.c[0].square()*speed.c[0])
    u=C.u(theta);sn,co=k.sincos(u)
    def norm(v):
        t=core.sq(v);return I(np.maximum(0,t.lo),t.hi).sqrt()
    def harmonic_rows(modes,kind):
        angles=[tr(int(i)) for i in modes];result=[]
        for d in range(3):
            terms=[]
            for i,(sn0,co0) in zip(modes,angles):
                vals=(co0,-sn0,-co0) if kind=='cos' else (sn0,co0,-sn0)
                terms.append(vals[d]*int(i)**d)
            result.append(I(np.stack(np.broadcast_arrays(*[z.lo for z in terms],theta.lo)[:-1],axis=-1),
                            np.stack(np.broadcast_arrays(*[z.hi for z in terms],theta.hi)[:-1],axis=-1)))
        return result
    def isum_last(z):
        while z.shape[-1]>1:
            n=z.shape[-1]//2;v=z[...,:2*n:2]+z[...,1:2*n:2]
            if z.shape[-1]%2:v=I(np.concatenate((v.lo,z.lo[...,-1:]),axis=-1),np.concatenate((v.hi,z.hi[...,-1:]),axis=-1))
            z=v
        return z[...,0]
    def field_value(coeff,t,l,r,scale,table):
        vals=core.horn(coeff,(t-l)/(r-l),(r-l)*scale);out=[]
        for j,d in core.ORD:
            out.append([isum_last(vals[j][...,sl]*row[d]) if row is not None else I(0) for sl,row in table])
        return out
    oldtable=[(slice(0,len(pm)),harmonic_rows(pm,'cos')),(slice(0,len(pm)),harmonic_rows(pm,'sin')),
              (slice(len(pm),None),harmonic_rows(zm,'cos'))]
    if complete:
        newtable=[(slice(0,m+1),harmonic_rows(range(m+1),'cos')),
                  (slice(m+1,2*m+1),harmonic_rows(range(1,m+1),'sin') if m else None),
                  (slice(2*m+1,None),harmonic_rows(range(m+1),'cos'))]
    def mag(x):return I(x.abs_upper())
    def maxup(x):return k.exact(k.up(np.max(x.hi)))
    def lower(x):return k.exact(k.down(np.min(x.lo)))
    d0=I(F(257212,10**13));K0=I(F(4763997235009095,562949953421312));CX=I(F('26.000001'))
    bounds={k:F(0) for k in ('position','ds','du_over_r','dss','dsu_over_r','duu_over_r2','differential','second','metricTriangle','relativeGram','curvature','norm','mixed')}
    support=F(10);height=F(10);worst={};covered=[];leaves=0;failed=0
    U0=I(F(budget['planar_perturbation_upper']['exact']));V0=I(F(budget['height_perturbation_upper']['exact']))
    zmin=I(F(budget['cut_height_lower']['exact']))-V0
    maxH=I(F(budget['cut_height_upper']['exact'])+F(budget['complete_background_height_upper']['exact']))+V0
    baseR=I(F('1.888068'))
    hrecord=frozen('2026-11-09-db6f-tail-background-height-rigorous.json','dd64e00bf25124b03e725792e321e961106c6ee643f5526e0b5b95383161ff01')
    amax=F(budget['exact_alpha_interval'][1]['exact'])
    innerLower=rCut-sum((ff(y['A'][1])+amax*ff(y['B'][1]) for y in hrecord['segments']),F(0))
    if innerLower<=F('.29'):raise ValueError('Cell-zero inner anchor mismatch')
    for il,ir,old in oldpower:
        ol,orr=vspan(il,ir,F(0))
        if orr<=ol:continue
        for nl,nr,new in newpower:
            wl,wr=vspan(nl,nr,c);left,right=max(ol,wl),min(orr,wr)
            if right<=left:continue
            covered.append((left,right))
            for part in range(a.radial_subdivisions):
                l=left+(right-left)*F(part,a.radial_subdivisions);r=left+(right-left)*F(part+1,a.radial_subdivisions)
                v=I.bounds(l,r);xi=SS+h*v;oldT=xi/TT
                p0=field_value(old,oldT,il,ir,TT,oldtable)
                if complete:
                    qv=(xi-c)/(TT-c);jv=field_value(new,qv,nl,nr,TT-c,newtable)
                    p0=[core.add(x,y) for x,y in zip(p0,jv)]
                rraw=I(rCut)-h*k.poly(R,v);rho=I(np.maximum(rraw.lo,I(rCuff).lo),np.minimum(rraw.hi,I(rCut).hi));rp=k.poly(Rp,v);rpp=k.poly(Rpp,v)
                if np.any(rp.lo<=0):raise ArithmeticError('Chart derivative not enclosed positive; subdivide')
                # Cell 0 comprises the outer tail. Below radius .29 all original cells satisfy w<=1/49;
                # Radius membership is tested with the outward upper bound and the exact certified lower anchor.
                slope=I.bounds(F(0),F(1,49) if k.exact(rho.hi)<=innerLower else F(16,15));E=1+slope.square();rt=E.sqrt()
                qs=1/(rp*rt)
                # |r_ss|=|kappa_r|*w/sqrt(1+w^2), original radial curvature at most 6.
                rslim=6*slope/rt;rss=I(-rslim.hi,rslim.hi)
                qss=-(rss+(rpp/h)*qs.square())/rp
                P,Q,V,QQ,QV,VV=p0
                ps=core.mul(Q,qs);pu=core.mul(V,inv/rho)
                pss=core.add(core.mul(QQ,qs.square()),core.mul(Q,qss))
                psu=core.mul(QV,qs*inv/rho)
                puu=core.mul(core.add(core.mul(VV,inv.square()),core.mul(V,inv2)),1/rho.square())
                p1,p2=norm(ps),norm(pu);d2=p1.square()+p2.square();dp=I(np.maximum(0,d2.lo),d2.hi).sqrt()
                a2,b2,c2=norm(pss),norm(psu),norm(puu);dw=a2+2*b2+c2
                tri=d0+2*(1+d0)*dp+dp.square();normal=(3*dp+dp.square())/(1-d0)
                eta=norm(P)
                hlow=I(F('.737'))-I(F('1.9'))*normal-eta
                # The original source differential is the rotational graph plus R230's V jets.
                # Correlate with the rotational part, enclose old perturbation by its full source bounds.
                tangentS=[-co/rt,-sn/rt,slope/rt];tangentU=[-sn,co,I(0)]
                vs=I(F('.013364'));vu=I(F('.002867'))/rho
                e=mag(2*core.dot(tangentS,ps)+core.dot(ps,ps))+2*vs*p1
                f=mag(core.dot(tangentS,pu)+core.dot(tangentU,ps)+core.dot(ps,pu))+vs*p2+vu*p1
                gg=mag(2*core.dot(tangentU,pu)+core.dot(pu,pu))+2*vu*p2
                # Absolute row-sum bound, adding the proved source spectral norm.
                gr=I(np.maximum((e+f).hi,(gg+f).hi))+d0
                clean=min(maxup(gr),maxup(tri))
                if clean>=1:
                    failed+=1;cup=None
                else:
                    cup=(K0*(1+d0)+normal*CX+dw)/(1-I(clean))
                floorHeight=zmin-norm([P[2]]);maxnorm=baseR+eta
                mix=norm([I(F('2.194'))+rho+U0+norm(P[:2]),I(F('.233'))+maxH+norm([P[2]])])
                values={'position':eta,'ds':p1,'du_over_r':p2,'dss':a2,'dsu_over_r':b2,'duu_over_r2':c2,'differential':dp,'second':dw,'metricTriangle':tri,'relativeGram':I(clean),'norm':maxnorm,'mixed':mix}
                if cup is not None:values['curvature']=cup
                for key,value in values.items():
                    mx=maxup(value)
                    if mx>bounds[key]:bounds[key]=mx;worst[key]=[str(l),str(r)]
                support=min(support,lower(hlow));height=min(height,lower(floorHeight));leaves+=1
    end=F(0)
    for l,r in sorted(covered):
        if l>end:raise ArithmeticError('Tail chart coverage gap')
        end=max(end,r)
    if end!=1:raise ArithmeticError('Missing true cuff')
    result=dict(schema='true-released-whole-tail-actual-six-jets-and-R230-geometry-v1',fieldSHA=sha(wp),parentSHA=sha(a.parent) if complete else None,
                stateSHA=sha(a.state) if complete else None,sourceSHA=sha(Path(__file__)),releasedXYZIncluded=complete,
                sourceScope='All true M12 source elements including deep/infinite profile and exact cuff by R21/R25/R230',
                angularDomain='all 2pi, no symmetry reduction',angularBoxes=n,radialLeaves=leaves,closedIntersections=len(covered),
                fullTrueTailCovered=True,unresolvedCurvatureLeaves=failed,upper={key:str(z) for key,z in bounds.items()},
                upperDisplay={key:float(z) for key,z in bounds.items()},worstRadialIntervals=worst,
                supportLower=str(support),heightLower=str(height),supportLowerDisplay=float(support),heightLowerDisplay=float(height),
                shapePassed=bounds['norm']<=F('1.915') and bounds['mixed']<=F('3.830'),
                fullTailGeometryPassed=failed==0 and support>F('.115') and height>F('.348') and bounds['curvature']<=F(200,23),
                note='The prefix, the closed unarmed union and all attached arms require their own corresponding proofs. A loose upper bound does not exclude the actual state.')
    with a.out.open('x') as f:
        json.dump(result,f,indent=2)
        f.write('\n')
    print(json.dumps({k:result[k] for k in ('fullTailGeometryPassed','shapePassed','radialLeaves','upperDisplay','supportLowerDisplay','heightLowerDisplay')}),flush=True)


if __name__=='__main__':
    main()
