#!/usr/bin/env python3
"""Genuine physical p32 return lifts, translated developed tail/disks and the R293 complete cap."""
import os
for tag in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):os.environ[tag]="1"
import importlib.util
from pathlib import Path
import sys
from types import SimpleNamespace
import time
import json
import numpy as np
from scipy.spatial import cKDTree


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp)
    sys.modules[n]=m;sp.loader.exec_module(m);return m


here=Path(__file__).parent;sep=load(here/"2ecf-strong-stadium-real-pair-separation.py","elevated_stadium_primal")
arb=sep.arb;mat=sep.mat;c=arb.c
base_source=mat.source_rows;base_coarse=sep.coarse
def install_r293_evaluator(f):
    # The former input domain validator binds Z to the original R219 hat.
    # Validate every inherited setting there and the new physical Z in the R293 window.
    prior=f.stream.point.PointConfig
    def new_config(**parameters):
        z=parameters["true_cuff_height"]
        if not .4799<=z<=.60:raise ValueError("R293 true complete-cuff window")
        old=prior(**dict(parameters,true_cuff_height=.51))
        return SimpleNamespace(**dict(vars(old),true_cuff_height=z))
    f.stream.point.PointConfig=new_config


class RaisedField(arb.Field):
    def __init__(self,a):
        super().__init__(a);install_r293_evaluator(self);self.elevation=arb.rd(a.elevation)
        self.dz,self.left,self.right=[float.fromhex(self.elevation[k]) for k in ("deltaZ","physicalStart","physicalEnd")]
        self.true_cuff_z=.51+self.dz
        if not (self.newb<=self.left<self.right<=self.dclock.jets([self.end])[0][0] and .4799<=self.true_cuff_z<=.60):raise ValueError("Real R293 interface window")
        if self.elevation["metricOnCore"]!=self.ident:raise ValueError("Same actual core metric required")
        parents=self.elevation["originalCore"];actual=[c.sha(p) for p in a.extra_state]
        if actual[:len(parents)]!=parents:raise ValueError("Exact original p32 shape chain required")
        for p in a.extra_state[len(parents):]:
            if arb.rd(p).get("elevation")!=c.sha(a.elevation):raise ValueError("Spatial successor belongs to a different complete cuff")
        self.definition["pointConfig"]["true_cuff_height"]=self.true_cuff_z
    def jets(self,x,u):
        Y,rad=super().jets(x,u);s=self.dclock.jets(x)[0]
        apply(Y,s,self.dz,self.left,self.right)
        return Y,rad


def profile(s,left,right):
    t=np.clip((s-left)/(right-left),0,1);inside=(s>left)&(s<right)
    h=t**3*(10+t*(-15+6*t))
    h1=np.where(inside,30*(t*(1-t))**2/(right-left),0.)
    h2=np.where(inside,60*t*(1-t)*(1-2*t)/(right-left)**2,0.)
    return h,h1,h2


def apply(Y,s,dz,left,right):
    h,h1,h2=profile(s,left,right)
    Y[:,0,:,2]+=dz*h[:,None];Y[:,1,:,2]+=dz*h1[:,None];Y[:,3,:,2]+=dz*h2[:,None]


def elevated_rows(f,g):
    x,u,Y,rad,w=base_source(f,g);Y[x>f.end,0,:,2]+=f.dz
    return x,u,Y,rad,w


def elevated_coarse(f,args):
    x,u,J=base_coarse(f,args);J[x>f.end,0,:,2]+=f.dz
    return x,u,J


def gridgeom(f,base,s,u,z,left,right,R,batch=36):
    J=base.copy();h,h1,_=profile(s,left,right);J[:,0,:,2]+=z*h[:,None];J[:,1,:,2]+=z*h1[:,None]
    P=J[:,0].reshape(-1,3);n=np.cross(J[:,1],J[:,2]).reshape(-1,3);n/=np.linalg.norm(n,axis=1)[:,None]
    rd=[0.]+list(np.repeat(np.arange(1,9)*.32/9,len(u)));vd=np.r_[0.,np.tile(u,8)]
    D=np.column_stack([rd*np.cos(vd),rd*np.sin(vd),np.full(len(rd),.51+z)])
    P=np.r_[P,D];n=np.r_[n,np.tile([0,0,1],(len(D),1))]
    matl=np.r_[np.repeat(s,len(u)),np.full(len(D),s[-1])+(.32-np.array(rd))]
    ang=np.r_[np.tile(u,len(s)),vd];both=np.flatnonzero(matl>0);flip=[1,1,-1]
    P=np.r_[P,P[both]*flip];n=np.r_[n,n[both]*flip];matl=np.r_[matl,-matl[both]];ang=np.r_[ang,ang[both]]
    tree=cKDTree(P);minimum=np.inf;minFar=np.inf;record=None;pairs=0
    # Rebuild the tree for each actual spatial input, and retain every close ordered pair.
    for b in range(0,len(P),batch):
        top=min(b+batch,len(P));a=tree.query_ball_point(P[b:top],2*R+.004)
        I=np.repeat(np.arange(b,top),list(map(len,a)));Q=np.concatenate(a).astype(int);ok=I!=Q;I,Q=I[ok],Q[ok]
        d=P[Q]-P[I];d2=np.einsum("ij,ij->i",d,d);den=2*abs(np.einsum("ij,ij->i",n[I],d))
        rr=np.divide(d2,den,out=np.full_like(d2,np.inf),where=den>0);idx=int(np.argmin(rr));pairs+=len(rr)
        if rr[idx]<minimum:
            i,j=I[idx],Q[idx];minimum=float(rr[idx]);record=[float(matl[i]),float(ang[i]),float(matl[j]),float(ang[j]),float(np.sqrt(d2[idx]))]
        far=abs(matl[I]-matl[Q])>.19
        if np.any(far):minFar=min(minFar,float(np.min(rr[far])))
    return dict(radius=minimum,far=minFar,arg=record,actualCloudPoints=len(P),orderedNearPairs=pairs,
        maximumAbsoluteZ=float(abs(P[:,2]).max()),maximumRadius=float(np.linalg.norm(P,axis=1).max()))


def main(args):
    start=time.monotonic();f=arb.Field(args);install_r293_evaluator(f);x,u,J=base_coarse(f,args);s=f.dclock.jets(x)[0]
    train={k:base_source(f,k) for k in ("training","observer")};cfg=f.definition["pointConfig"]
    states=[];span=f.dclock.jets([f.end])[0][0]-f.newb
    for lo,hi in ((0.,.84),(.08,.93),(.18,.99),(.03,.66),(.18,.75),(.28,1.)):
        left=f.newb+lo*span;right=f.newb+hi*span
        for delta in args.lifts:
            cfg["true_cuff_height"]=.51+delta
            stats={}
            for k,(gx,gu,Y,rad,w) in train.items():
                raised=Y.copy();apply(raised,f.dclock.jets(gx)[0],delta,left,right)
                stats[k]=mat.observed(f,None,None,(gx,gu,raised,rad,w),None,None,False,args)
                # Keep the original .51 guide as a full diagnostic, with every other Cartesian row identical.
                oldcfg=dict(cfg,true_cuff_height=.51);geom=f.stream.point.geometry_cache(raised[:,0],f.stream.point.PointConfig(**oldcfg))
                sw=w["geometry"];newcfg=f.stream.point.geometry_cache(raised[:,0],f.stream.point.PointConfig(**cfg))
                stats[k]["originalHeightPlusAndMinus"]=np.max(geom["residual"][...,3:5],axis=(0,1)).tolist()
                stats[k]["nativeHeightPlusAndMinus"]=np.max(newcfg["residual"][...,3:5],axis=(0,1)).tolist()
                del raised
            pair=gridgeom(f,J,s,u,delta,left,right,.097)
            metric=max(q["metric"] for q in stats.values());curv=max(q["curvature"] for q in stats.values());held=min(q["held"] for q in stats.values())
            merit=max(.097/pair["radius"],curv/10.24,metric/.225,.65/held,pair["maximumAbsoluteZ"]/.635)
            record=dict(delta=delta,left=left,right=right,trueCuff=.51+delta,nonlocalObservation=pair,G10=stats,merit=merit)
            states.append(record)
            print(json.dumps(dict(trial=len(states),Z=.51+delta,range=[lo,hi],radius=pair["radius"],far=pair["far"],metric=metric,curvature=curv,held=held,merit=merit)),flush=True)
    chosen=min(range(len(states)),key=lambda i:states[i]["merit"]);sel=states[chosen]
    spec=dict(schema="genuine-p32-R293-Z-and-full-recomputed-throat-to-replace-R219-cap-v1",entry=c.sha(__file__),
        originalCore=[c.sha(p) for p in args.extra_state],source=c.sha(args.background),metricOnCore=f.ident,
        physicalStart=float(sel["left"]).hex(),physicalEnd=float(sel["right"]).hex(),deltaZ=float(sel["delta"]).hex(),
        cuffHeight=float(sel["trueCuff"]).hex(),caps="complete R293 with a=.30,ac=.32,C=.635; eta=.635-Z; induced metric of this fixed cap",
        centralAndDevelopedPortFirstAndSecondJetsPreservedUnderTheirRespectiveTranslations=True)
    digest=c.save(Path(str(args.prefix)+"-elevation.json"),spec)
    native=sel["G10"];cfg["true_cuff_height"]=sel["trueCuff"]
    xx,uu,Y,rad,w=base_source(f,"independent");apply(Y,f.dclock.jets(xx)[0],sel["delta"],sel["left"],sel["right"])
    observed=mat.observed(f,None,None,(xx,uu,Y,rad,w),None,None,False,args)
    full=dict(schema="complete-actual-elevated-p32-shapes-with-selected-R293-interface-v1",entry=c.sha(__file__),
        selected=chosen,sourceElevation=digest,trials=states,independentSelected=observed,allOriginalPhysicalRows=4291840,
        continuousReachCertified=False,continuousMetricCertified=False,seconds=time.monotonic()-start)
    out=c.save(Path(str(args.prefix)+"-actual-elevated-receipt.json"),full)
    print(json.dumps(dict(selected=chosen,G11=[observed[k] for k in ("metric","curvature","held")],elevation=digest,receipt=out)),flush=True)


if __name__=="__main__":
    p=arb.parser();p.add_argument("--lifts",nargs="+",type=float,default=[.03,.055,.080])
    p.add_argument("--count",type=int,default=48);a=p.parse_args();a.resume=None;main(a)
