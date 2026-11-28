#!/usr/bin/env python3
"""Per-ring unconstrained best invariant diagonal target for complete physical HF fields."""
import os
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[k]="1"

import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s)
    sys.modules[name]=m
    s.loader.exec_module(m)
    return m


full=load(Path(__file__).with_name("2ecf-strong-hf-new-clock-full-position.py"),"free_diagonal_physical")
hf,c=full.hf,full.c


def solve(x,u,E,F,G):
    det=E*G-F*F
    if np.min(det)<=0:raise ArithmeticError("Actual SPD forms required")
    # A positive diagonal change of material coordinates does not change the
    # optimum for all diagonal targets. These E,F,G use the actual fixed g
    # as the normalization, so t is an aspect correction around that metric.
    centers=.5*np.log(E/G)
    lo=centers.min(axis=1);hi=centers.max(axis=1)
    rr=np.arange(len(x))
    def branch(t):
        aa=E*np.exp(-t)[:,None];dd=G*np.exp(t)[:,None]
        gap=np.hypot(aa-dd,2*F)
        top=.5*(aa+dd+gap)
        upper=np.argmax(top,axis=1)
        inverse=np.argmax(top/det,axis=1)
        slope=np.divide(dd-aa,gap,out=np.zeros_like(gap),where=gap>0)
        return top,upper,inverse,slope[rr,upper]+slope[rr,inverse]
    for _ in range(58):
        mid=(lo+hi)*.5
        _,_,_,sg=branch(mid)
        greater=sg>=0
        hi=np.where(greater,mid,hi);lo=np.where(greater,lo,mid)
    t=(lo+hi)*.5;mu,p,q,_=branch(t)
    U=mu[rr,p];L=det[rr,q]/mu[rr,q];opt=(U-L)/(U+L)
    shear=abs(F)/np.sqrt(E*G)
    # Interior source Hermite cells only, to allow an independent exact dyadic
    # witness without relying on any tabulated inlet/exit angular derivatives.
    contained=(x>.210)&(x<.95)
    vals=np.where(contained[:,None],shear,-1)
    i,j=map(int,np.unravel_index(np.argmax(vals),vals.shape))
    b=int(np.argmax(opt))
    arg=lambda col,cls:dict(type=cls,index=int(col),u=float(u[col]),E=float(E[b,col]),F=float(F[b,col]),G=float(G[b,col]))
    support=sorted(set([int(p[b]),int(q[b])]))
    return dict(maxBestRingMetric=float(opt[b]),radiusIndex=b,x=float(x[b]),t=float(t[b]),bestMeanScale=float((U[b]+L[b])/2),
        upper=arg(p[b],"upper"),lower=arg(q[b],"lower"),bestRingTargetUncoupledAndFloating=True,
        tSearchFinalWidth=float((hi-lo)[b]),numberOfRings=len(x),materialAngles=len(u),
        worstInteriorSingleShear=dict(x=float(x[i]),u=float(u[j]),index=[i,j],value=float(shear[i,j]),
            E=float(E[i,j]),F=float(F[i,j]),G=float(G[i,j])),maxSinglePointShear=float(shear.max()),
        actuallyAttainedRingTargets=[[float(a),float(b)] for a,b in zip(t,(U+L)/2)])


def main(args):
    tic=time.monotonic()
    args.metric_sextic=.2;args.curvature_tau=2.
    definition,basis,clock,physical,ind,weights,mods,radius,meta,expect=full.prepare(args)
    physical["independent"]=ind
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","free_diag_G11").direct_packet
    results=[]
    for path in [None]+args.fields:
        z=np.zeros((basis.nb,basis.na))
        if path:
            st=json.loads(path.read_text())
            md=st["model"]
            if md["warp"]!=meta["warp"] or md["actualMetric"]!=meta["actualMetric"] or md["physicalBasis"]!=meta["physicalBasis"]:
                raise ValueError("All fields must have common model, g and actual base")
            z=np.asarray(st.get("totalCoefficients",st["coefficients"])).reshape(basis.nb,basis.na)
        tensors={}
        for name,cache in physical.items():
            const=np.empty((len(cache.nodes),len(cache.u),3))
            for s0 in range(0,len(cache.nodes),24):
                s=slice(s0,s0+24);x=cache.nodes[s]
                corr=direct(basis,x,z,cache.u) if name=="independent" else basis.packet(basis.matrices(x),z,len(cache.u))
                X=cache.jets[s]+corr
                U,V=X[:,1],X[:,2]/cache.radius[s,0,None,None]
                const[s]=np.stack([np.sum(a*b,axis=-1) for a,b in ((U,U),(U,V),(V,V))],axis=-1)
            tensors[name]=const
        if not np.array_equal(physical["training"].nodes,physical["observer"].nodes):raise ValueError("Both G10 radial grids required")
        rows={}
        for n,ns in (("completeG10",("training","observer")),("G11",("independent",))):
            x=physical[ns[0]].nodes;u=np.concatenate([physical[v].u for v in ns])
            tensor=np.concatenate([tensors[v] for v in ns],axis=1)
            row=solve(x,u,*tensor.transpose(2,0,1))
            row["sAtMax"]=float(clock.jets([row["x"]])[0][0])
            rows[n]=row
        results.append(dict(field=c.sha(path) if path else "frozen two-material base; zero extra Cartesian XYZ",groups=rows))
        print(json.dumps(dict(field=str(path),G10=rows["completeG10"]["maxBestRingMetric"],G11=rows["G11"]["maxBestRingMetric"],
            G11InteriorSingleRealShear=rows["G11"]["worstInteriorSingleShear"])),flush=True)
    out=dict(schema="all-angular-independent-free-ring-diagonal-minimum-R274-v1",entry=c.sha(__file__),
        physicalEntry=c.sha(full.__file__),source=meta,results=results,releasedCommonLengthAndAllRadialRegularity=True,
        numericalUncertaintyOnly=True,wholeDomainMetricCertified=False,timeSeconds=time.monotonic()-tic)
    print(c.save(args.output,out),flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser();hf.args_hf(ap)
    for k in ("diagonal","warp","output"):ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--fields",type=Path,nargs="*",default=[])
    main(ap.parse_args())
