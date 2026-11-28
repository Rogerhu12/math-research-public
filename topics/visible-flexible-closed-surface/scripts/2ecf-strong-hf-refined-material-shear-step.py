#!/usr/bin/env python3
"""Full-periodic material trials on actual previously optimized and refined Cartesian HF fields."""
import os
for name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[name]="1"
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import BSpline


def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m)
    return m


root=Path(__file__).resolve().parent
core=load(root/"2ecf-strong-hf-fixed-metric-full-spectral-position.py","full_shape_for_new_warp")
car=load(root/"2ecf-strong-hf-refined-spectral-carrier.py","refined_shape_for_warp")
seed=load(root/"2ecf-strong-hf-two-clock-spectral.py","material_all_spectral_seed")
c=core.c;two=core.full.two


class RealWave(two.Wave):
    def __init__(self,knots,order):
        super().__init__(knots,np.repeat(np.arange(order+1),2)[1:],False)
        self.sin_channel=np.zeros(len(self.k),bool);self.sin_channel[2::2]=True
    def angular(self,u,j):
        theta=np.asarray(u)[...,None]*self.k+j*np.pi/2
        return self.k**j*np.where(self.sin_channel,np.sin(theta),np.cos(theta))


def xyz(spline,x,u):
    M=(spline.c.shape[1]//3-1)//2
    sw=np.ones((3,len(x),2*M+1));sw[1:,:,0]=0.
    mode=np.arange(1,M+1)
    for j in range(3):
        arg=u[:,None]*mode+j*np.pi/2
        sw[j,:,1::2]=mode**j*np.cos(arg);sw[j,:,2::2]=mode**j*np.sin(arg)
    matrices=[spline(x,nu=i).reshape(len(x),3,-1) for i in range(3)]
    return [np.einsum("nck,nk->nc",matrices[i],sw[j],optimize=True) for i,j in two.PAIRS]


class Field:
    def __init__(self,args,meta):
        self.root=two.ArbitraryHF(args)
        warp=json.loads(args.warp.read_text());factor=warp["actualG10Trials"][warp["chosen"]]["factor"]
        self.p=two.Wave(warp["radialKnots"],warp["pFrequencies"],False)
        self.q=two.Wave(warp["radialKnots"],warp["qFrequencies"],True)
        self.pc,self.qc=[factor*np.array([float.fromhex(v) for v in warp[k]]) for k in ("pCoefficientHex","qCoefficientHex")]
        self.cart=[]
        for file,td,tag in ((args.warm,meta["trueCarrierBasis"]["sourceChartBasis"],"totalCoefficients"),
                (args.refined_state,meta["physicalBasis"]["sourceChartBasis"],"totalRefinedCoefficients")):
            st=json.loads(file.read_text())
            coeff=np.array(st.get(tag,st["coefficients"])).reshape(td["radialBasisCount"],-1)
            self.cart.append(BSpline(td["physicalKnots"],np.pad(coeff,((3,3),(0,0))),5,extrapolate=False))
    def before(self,x,u):
        p=self.p.paired(x,u,self.pc);q=self.q.paired(x,u,self.qc)
        p[0]+=x;p[1]+=1;q[0]+=u;q[2]+=1
        a=two.chain(self.root.original(np.clip(p[0],self.root.T[0],self.root.T[-1]),q[0]),p,q)
        z=xyz(self.cart[0],x,u);w=xyz(self.cart[1],x,u)
        return [a0+b0+c0 for a0,b0,c0 in zip(a,z,w)]
    def actual(self,x,u,wave,pc,qc):
        x,u=np.broadcast_arrays(x[:,None],u[None,:]);shape=x.shape
        x=x.ravel();u=u.ravel();result=np.empty((len(x),6,3))
        for i in range(0,len(x),256):
            sl=slice(i,i+256);a=x[sl];b=u[sl]
            p=wave.paired(a,b,pc);q=wave.paired(a,b,qc)
            p[0]+=a;p[1]+=1;q[0]+=b;q[2]+=1
            old=self.before(np.clip(p[0],self.root.T[0],self.root.T[-1]),q[0])
            result[sl]=np.stack(two.chain(old,p,q),axis=1)
        return result.reshape(*shape,6,3).swapaxes(1,2)


def main(args):
    tic=time.monotonic()
    args.metric_sextic=.2;args.curvature_tau=2.
    definition,basis,clock,physical,g11,weights,mods,radius,meta,expected,refined=car.prepare(args,core)
    field=Field(args,meta)
    knots=np.unique(np.r_[field.root.orig.knots,field.root.T[1:-1:4]])
    knots=np.r_[np.repeat(knots[0],5),knots,np.repeat(knots[-1],5)]
    wave=RealWave(knots,args.order);groups={}
    for n,x in physical.items():
        _,h,hx=clock.jets(x.nodes);h=h[:,None,None];hx=hx[:,None,None]
        j=x.jets.copy()
        j[:,3]=j[:,3]*h**2+j[:,1]*hx;j[:,1]*=h;j[:,4]*=h
        groups[n]=dict(cache=x,radius=x,jets=j)
    pc,qc,history=seed.learn(groups,wave,wave,clock,basis,np.zeros(basis.nb))
    del groups
    pd,pu=wave.bounds(pc);qd,qu=wave.bounds(qc)
    det=(1-pd)*(1-qu)-pu*qd
    if pd>=1 or qu>=1 or det<=0:raise ArithmeticError("Orientation bound failed")
    physical["independent"]=g11
    saved=json.loads(args.prepared.read_text())
    def samples(factor,names):
        caches={};shears={}
        for n in names:
            v=physical[n];x=v.nodes;u=v.u;_,h,hx=clock.jets(x);data=v.jets.copy()
            ix=np.flatnonzero((x>=basis.c)&(x<=basis.end))
            if factor:
                for i in range(0,len(ix),12):
                    sl=ix[i:i+12]
                    data[sl]=c.physical_jet(field.actual(x[sl],u,wave,factor*pc,factor*qc),h[sl],hx[sl])
            V,U=data[:,1],data[:,2]
            sh=abs(np.sum(V*U,axis=-1))/np.sqrt(np.sum(V*V,axis=-1)*np.sum(U*U,axis=-1))
            shears[n]=float(sh.max())
            caches[n]=SimpleNamespace(nodes=x,u=u,jets=data,h=h,radius=v.radius)
        return core.hf.sample(caches,mods,saved,definition,clock,args),shears
    src=physical["training"];x=src.nodes;u=src.u
    ix=np.flatnonzero((x>=basis.c)&(x<=basis.end))
    j=ix[np.unique(np.r_[0,1,2,np.linspace(0,len(ix)-1,12,dtype=int),-2,-1])]
    _,h,hx=clock.jets(x[j])
    zero=c.physical_jet(field.actual(x[j],u,wave,pc*0,qc*0),h,hx)
    audit=np.max(abs(zero-src.jets[j]),axis=(0,2,3))
    if audit.max()>3e-7:raise ArithmeticError(("Warm zero identity all actual six jets failed",audit))
    rows=[]
    for t in (0.,1.,.5,.25):
        g,shear=samples(t,("training","observer"))
        v=dict(trial=t,G10=g,shear=shear,peak=max(a["metric"] for a in g.values()),cost=sum(a["original"] for a in g.values()))
        rows.append(v);print(json.dumps(dict(factor=t,peak=v["peak"],shear=max(shear.values()),cost=v["cost"])),flush=True)
    if abs(rows[0]["cost"]-expected[0])>1e-10:raise ArithmeticError("Original physical baseline differs")
    ok=[i for i,r in enumerate(rows) if r["peak"]<rows[0]["peak"] and r["cost"]<rows[0]["cost"]
        and max(r["shear"].values())<max(rows[0]["shear"].values())]
    pick=min(ok,key=lambda i:rows[i]["peak"]) if ok else 0
    g,sh=samples(rows[pick]["trial"],("independent",));ind=g["independent"]
    o=dict(schema="full-periodic-double-material-step-on-true-refined-HF-real-positions-v1",
        entry=c.sha(__file__),proposal=c.sha(seed.__file__),warm=c.sha(args.warm),refined=c.sha(args.refined_state),
        warp=c.sha(args.warp),target=meta["actualMetric"],knots=knots.tolist(),modes=wave.k.tolist(),
        sine=wave.sin_channel.tolist(),p=[float(a).hex() for a in pc],q=[float(a).hex() for a in qc],
        columns=2*wave.n,allNewSixJets=two.PAIRS,determinantLower=det,history=history,zeroAudit=audit.tolist(),
        actualTrials=rows,pickByG10=pick,g11=ind,g11Shear=sh["independent"],seconds=time.monotonic()-tic)
    print(json.dumps(dict(SHA=c.save(args.output,o),pick=pick,G11=ind["metric"],curvature=ind["curvature"],shear=sh["independent"])),flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser();core.hf.args_hf(ap)
    for n in ("diagonal","warp","warm","refined-state","output"):ap.add_argument("--"+n,type=Path,required=True)
    ap.add_argument("--order",type=int,default=8);ap.add_argument("--frequency",type=int,default=32)
    main(ap.parse_args())
