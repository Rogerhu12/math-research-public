#!/usr/bin/env python3
"""Actual nonlinear ring arclength reset and physical scaling on the frozen HF64-M80 suffix."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
import types
for v in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[v]="1"
import numpy as np


def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp)
    sys.modules[name]=m;sp.loader.exec_module(m);return m


def sha(p):
    d=hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):d.update(b)
    return d.hexdigest()


def dot(x,y):return np.sum(x*y,axis=-1)


class RingSource:
    def __init__(self,hf,field,basis,q,scripts,ramp,coast):
        self.hf=hf;self.k=field["knots"];self.base=field["coefficients"];self.fine=basis;self.q=q
        self.W=field["physicalW"];self.m=self.base.shape[2]
        self.end=[]
        grid=2*np.pi*np.arange(q)/q
        for p in hf.numerical_endpoint_pair(scripts,ramp,coast,grid):
            f=2*np.fft.rfft(p[:,0],axis=1)/q
            f[:,0]*=.5;self.end.append(f[:,:-1])
        self.kmin=float(self.k[0]);self.kmax=float(self.k[-1])

    def coefficients(self,s,wm=None):
        j=int(np.clip(np.searchsorted(self.k,s,side="right")-1,0,len(self.k)-2))
        h=self.k[j+1]-self.k[j]
        first=self.end[0] if j==0 else self.base[j]
        last=self.end[1] if j==len(self.k)-2 else self.base[j+1]
        nw=max(first.shape[1],last.shape[1])
        both=np.zeros((6,nw,3),complex);both[:3,:first.shape[1]]=first;both[3:,:last.shape[1]]=last
        mat=np.stack([self.hf.weights((s-self.k[j])/h,h,l) for l in range(3)])
        co=(mat@both.reshape(6,-1)).reshape(3,nw,3)
        if wm is None:wm=[(m@self.W)[0] for m in self.fine.matrices(np.asarray([s]))]
        for j,(d,k,kind) in enumerate(self.fine.channels):
            co[:,k,d]+=np.asarray([v[j] for v in wm])*(1 if kind=="cos" else -1j)
        return co


def frequency_packets(co):
    # Six physical jets plus d_u X_ss for the derivative of the angular length.
    parts=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(2,1))
    freq=1j*np.arange(co.shape[1])[:,None]
    return np.stack([co[i]*freq**k for i,k in parts])


def at(co,x):
    phase=np.exp(1j*x[:,None]*np.arange(co.shape[1]))
    ans=(phase@co.transpose(1,0,2).reshape(co.shape[1],-1)).real
    return ans.reshape(len(x),co.shape[0],3).transpose(1,0,2)


def grid_packets(co,q):
    c=co*(q/2);c[:,0]*=2
    return np.fft.irfft(c,n=q,axis=1)


def cumulative(h):
    q=h.shape[0];wave=np.arange(q//2+1)
    c=np.fft.rfft(h,axis=0)
    d=np.fft.irfft(c*(1j*wave[:,None]),n=q,axis=0)
    c[0]=0;c[1:]/=(1j*wave[1:,None]);c[-1]=0
    periodic=np.fft.irfft(c,n=q,axis=0);mu=h.mean(axis=0)
    step=2*np.pi/q
    v=np.arange(q)*step;parts=v[:,None]*mu+periodic-periodic[0]
    last=np.r_[parts[1:],(2*np.pi*mu)[None]]
    # Quintic primitive Hermite with authentic spectral nodal first and second derivatives.
    p0=parts;p1=h*step;p2=.5*d*step**2
    v0=last-p0-p1-p2;v1=np.roll(h,-1,axis=0)*step-p1-2*p2
    v2=np.roll(d,-1,axis=0)*step**2-2*p2
    c3=10*v0-4*v1+.5*v2;c4=-15*v0+7*v1-v2;c5=6*v0-3*v1+.5*v2
    return np.stack((p0,p1,p2,c3,c4,c5),axis=1),np.r_[parts[:,0],2*np.pi*mu[0]],mu


def evalprimitive(poly,v):
    q=len(poly);step=2*np.pi/q
    ind=np.minimum(np.floor(v/step).astype(int),q-1);frac=v/step-ind
    c=poly[ind];p=c[:,-1].copy();dp=np.zeros_like(p)
    for j in range(4,-1,-1):
        dp=dp*frac[:,None]+p;p=p*frac[:,None]+c[:,j]
    return p,dp/step


def transformed(co,rad,u,q,variants):
    p=frequency_packets(co);X,S,U,SS,SU,UU,SSU=grid_packets(p,q)
    speed=np.linalg.norm(U,axis=1)
    if speed.min()<=1e-3:raise ArithmeticError("Angular immersion failed")
    hs=dot(U,SU)/speed;hss=(dot(SU,SU)+dot(U,SSU)-hs**2)/speed
    poly,table,(a,as_,ass)=cumulative(np.column_stack((speed,hs,hss)))
    C=np.mean(X*speed[:,None],axis=0)/a
    Cs=(np.mean(S*speed[:,None]+X*hs[:,None],axis=0)-C*as_)/a
    Css=(np.mean(SS*speed[:,None]+2*S*hs[:,None]+X*hss[:,None],axis=0)-2*Cs*as_-C*ass)/a
    f,fs,fss=rad
    scale=f/a;ls=(fs-scale*as_)/a;lss=(fss-2*ls*as_-scale*ass)/a
    if np.any(np.diff(table)<=0):raise ArithmeticError("Numerical cumulative arc lost monotonicity")
    v=np.interp(a*u,table,np.linspace(0,2*np.pi,q+1))
    for i in range(6):
        val,d=evalprimitive(poly,v);res=val[:,0]-u*a
        if np.max(abs(res))<3e-14:break
        v=np.clip(v-res/d[:,0],0,2*np.pi)
    else:raise ArithmeticError("Ring arclength inverse failed")
    atv=at(p[:6],v);_,_,U,_,SU,UU=atv
    h=np.linalg.norm(U,axis=1);hs=dot(U,SU)/h;hv=dot(U,UU)/h
    vs=(u*as_-val[:,1])/h;vu=a/h
    vss=(u*ass-val[:,2]-2*hs*vs-hv*vs**2)/h
    vsu=(as_-(hs+hv*vs)*vu)/h;vuu=-a*a*hv/h**3
    fields={}
    for b in set(pair[0] for pair in variants):
        loc=atv if b==1 else at(p[:6],u+b*(v-u))
        X,S,U,SS,SU,UU=loc
        ths=b*vs;thu=1+b*(vu-1)
        Q=X-C;Qs=S+U*ths[:,None]-Cs
        Qss=SS+2*SU*ths[:,None]+UU*(ths**2)[:,None]+U*(b*vss)[:,None]-Css
        Qu=U*thu[:,None]
        Qsu=(SU+UU*ths[:,None])*thu[:,None]+U*(b*vsu)[:,None]
        Quu=UU*(thu**2)[:,None]+U*(b*vuu)[:,None]
        for beta,gamma in variants:
            if beta!=b:continue
            l=1+gamma*(scale-1);dl=gamma*ls;ddl=gamma*lss
            fields[(b,gamma)]=np.stack((C+l*Q,Cs+dl*Q+l*Qs,l*Qu,Css+ddl*Q+2*dl*Qs+l*Qss,
                                  dl*Qu+l*Qsu,l*Quu))
    return fields,dict(inverseResidual=float(abs(res).max()),interpolatedSpeedError=float(abs(d[:,0]-h).max()),
        scale=float(scale),angleShift=float(abs(v-u).max()),minSpeed=float(speed.min()))


def execute(args):
    started=time.monotonic();root=args.scripts;here=Path(__file__).parent
    hf=load(args.hf_entry,"ring_HF_source");hr=json.loads(args.hf_report.read_text())
    if sha(args.field)!=hr['fieldSHA256'] or sha(args.hf_entry)!=hr['sourceSHA256'] or sha(args.frozen)!=hr['frozenStateSHA256']:
        raise ValueError("True frozen HF64-M80 source required")
    if hr['preparedSHA256']!=sha(args.prepared) or hr['independentSHA256']!=sha(args.independent):raise ValueError("Actual source grids required")
    al=load(here/'2ecf-polar-log-radius-operator.py','ring_alpha')
    pr=load(here/'2ecf-polar-raw-ramp-source-compose.py','ring_saved')
    saved,definition,basis,caches,mods,*_=pr.validate_prepared(args)
    coarse=load(here/'2ecf-polar-fixed-prefix-position-basis.py','ring_coarse').restrict(basis)[0]
    fine=load(here/'2ecf-polar-local-suffix-boehm.py','ring_refine').build(coarse)[0]
    stream=mods['stream'];area=load(root/'6a65-geometry-area-ratio-power-two.py','ring_area')
    cfg=stream.point.PointConfig(**definition['pointConfig'])
    target=json.loads(args.frozen.read_text());field=np.load(args.field,allow_pickle=False)
    alpha=field['alpha']
    if target['provisionalMetricDefinition']['exactCoefficientHex']!=[float(a).hex() for a in alpha]:raise ValueError("Exact frozen scalar target mismatch")
    q=args.quadrature;src=RingSource(hf,field,fine,q,root,args.ramp,args.coast)
    ind=json.loads(args.independent.read_text())
    entries={k:(cache.nodes,cache.u,cache.jets,cache.radius,saved['caches'][k]['weights']) for k,cache in caches.items()}
    entries['independent']=(np.array(ind['physicalNodes']),np.array(ind['angles']),np.load(ind['files']['jets'],mmap_mode='r'),
                              np.load(ind['files']['radius'],mmap_mode='r'),None)
    variants=[tuple(map(float,k.split(','))) for k in args.variants]
    if (0.,0.) not in variants:raise ValueError("Baseline required")
    out={};keys=('metric','curvature','geometry')
    for gr,(nodes,u,base,rad,weights) in entries.items():
        radius=al.LogRadiusCache(coarse,types.SimpleNamespace(nodes=nodes,u=u,jets=None,radius=rad),alpha).radius
        wm=[m@src.W for m in fine.matrices(nodes)]
        allv={v:None for v in variants};area2={v:0. for v in variants};maxG={v:0. for v in variants}
        audit=dict(maxInverseResidual=0.,maxInterpolatedSpeedError=0.,scaleRange=[1.,1.],maxAngleShift=0.)
        for lo in range(0,len(nodes),12):
            ns=nodes[lo:lo+12];bb=radius[lo:lo+len(ns),0,None]
            packets={v:base[lo:lo+len(ns)].copy() for v in variants}
            for j,s in enumerate(ns):
                if src.kmin<s<src.kmax:
                    idx=lo+j;cf=src.coefficients(s,[m[idx] for m in wm])
                    fields,info=transformed(cf,radius[idx],u,q,variants)
                    for v,val in fields.items():packets[v][j]=val
                    audit['maxInverseResidual']=max(audit['maxInverseResidual'],info['inverseResidual'])
                    audit['maxInterpolatedSpeedError']=max(audit['maxInterpolatedSpeedError'],info['interpolatedSpeedError'])
                    audit['scaleRange']=[min(audit['scaleRange'][0],info['scale']),max(audit['scaleRange'][1],info['scale'])]
                    audit['maxAngleShift']=max(audit['maxAngleShift'],info['angleShift'])
            W={k:np.ones((len(ns),1))/len(u) if weights is None else .5*np.asarray(weights[k][lo:lo+len(ns)])[:,None]/len(u) for k in keys}
            for v,jet in packets.items():
                op=stream.point.PointLinearized(jet.swapaxes(1,2),np.broadcast_to(bb,(len(ns),len(u))),cfg,W)
                val=stream._block_statistics(op,ns,len(u));val['worstMetric']['u']+=float(u[0]);val['worstCurvature']['u']+=float(u[0])
                allv[v]=stream._merge_statistics(allv[v],val)
                aq=area.AreaPacket(jet,bb,W['metric'],.5);area2[v]+=aq.stats['squaredNorm']
                maxG[v]=max(maxG[v],float(np.max(abs(np.sum(jet[:,2]**2,axis=-1)/bb**2-1))))
        totals={}
        for v,stat in allv.items():
            pl=stat['squaredNorm']+area2[v] if weights is not None else None
            totals[str(v)]=dict(fullPhysicalR2=pl,actual14Rows=14*len(nodes)*len(u),maxMetric=stat['maxRelativeMetric'],
                  maxG=maxG[v],maxCurvature=stat['maxCurvature'],minHeld=stat['minHeldDistance'],minArea=float(np.sqrt(stat['minImmersion'])),
                  worstMetric=stat['worstMetric'],worstCurvature=stat['worstCurvature'],geometryViolations=stat['geometryMaximumViolations'])
        out[gr]=dict(totals=totals,audit=audit,radials=len(nodes),angles=len(u))
        print(gr,{v:[x['maxMetric'],x['maxCurvature'],x['minHeld']] for v,x in totals.items()},flush=True)
    g10={str(v):out['training']['totals'][str(v)]['fullPhysicalR2']+out['observer']['totals'][str(v)]['fullPhysicalR2'] for v in variants}
    if sum(out[k]['totals'][str(variants[0])]['actual14Rows'] for k in ('training','observer'))!=4291840:raise ArithmeticError("Physical rows lost")
    receipt=dict(schema='HF64-M80-frozen-g-actual-normalized-ring-transform-v1',sourceSHA256=sha(__file__),fieldSHA256=sha(args.field),
        hfEntrySHA256=sha(args.hf_entry),hfSourceReportSHA256=sha(args.hf_report),targetDefinitionSHA256=hr['targetDefinitionSHA256'],
        oldRampSHA256=sha(args.ramp),coastSHA256=sha(args.coast),preparedSHA256=sha(args.prepared),independentSHA256=sha(args.independent),
        finiteQuadrature=q,fullNonlinearPointObservations=out,g10OriginalQuarticR2=g10,
        noOwnOptimizationAccepts=True,allCompletePhysicalRows=True,seconds=time.monotonic()-started)
    with args.output.open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
if __name__=='__main__':
    ap=argparse.ArgumentParser()
    for name in ('scripts','hf-entry','hf-report','field','prepared','independent','frozen','ramp','coast','output'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--quadrature',type=int,required=True)
    ap.add_argument('--variants',nargs='+',required=True)
    execute(ap.parse_args())
