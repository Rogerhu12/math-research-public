#!/usr/bin/env python3
"""Refit both true material components and material length on a real all-grid held-feasible stadium."""
import os
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[k]="1"
import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy import sparse
from scipy.optimize import linprog


def load(p,n):
    specs=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(specs)
    sys.modules[n]=m;specs.loader.exec_module(m);return m


joint=load(Path(__file__).with_name("2ecf-strong-stadium-physical-guide-spectrum.py"),"redesigned_physical_solver")
c=joint.c
class NewClock:
    def __init__(self,old,raw,coef):
        self.old,self.raw,self.coef=old,raw,coef
        T=raw.breaks;self.T=T
        self.gauss,self.weight=np.polynomial.legendre.leggauss(24)
        self.cum=np.r_[0.,np.cumsum(self.integral(T[:-1],T[1:]))]
    def integral(self,l,r):
        x=.5*(l+r)[:,None]+.5*(r-l)[:,None]*self.gauss
        q=np.sqrt(1+self.raw.matrices(x.ravel())[0]@self.coef)
        h=self.old.jets(x.ravel())[1]
        return .5*(r-l)*(((q-1)*h).reshape(x.shape)@self.weight)
    def jets(self,x):
        x=np.asarray(x);s,h,hx=self.old.jets(x)
        B,Bx,_=self.raw.matrices(x)
        q=np.sqrt(1+B@self.coef);qx=(Bx@self.coef)/(2*q)
        t=np.clip(x,self.T[0],self.T[-1])
        ii=np.clip(np.searchsorted(self.T,t,side="right")-1,0,len(self.T)-2)
        return s+self.cum[ii]+self.integral(self.T[ii],t),h*q,hx*q+h*qx
    def physical_matrices(self,basis,x):return c.Clock.physical_matrices(self,basis,x)


def prepare(args):
    definition,basis,oldclock,phys,g11,weights,mods,radius,meta,_=joint.actual_stadium(args)
    sg=json.loads(args.prior_guide.read_text());hp=json.loads(args.projected.read_text())
    if (sg["model"]["fixedStadiumCompleteSource"]!=c.sha(args.fixed_stadium)
            or hp["parent"]!=c.sha(args.prior_guide) or hp["metric"]!=meta["actualMetric"]
            or hp["originalG11Untouched"]!=True):
        raise ValueError("True guide field and its actual complete projection required")
    z=(np.asarray(sg["coefficients"])+np.asarray(hp["coefficients"])).reshape(basis.nb,basis.na)
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","redesign_physical_G11").direct_packet
    groups=dict(**phys,independent=g11)
    for name,obj in groups.items():
        for j in range(0,len(obj.nodes),12):
            sl=slice(j,j+12);x=obj.nodes[sl]
            obj.jets[sl]+=direct(basis,x,z,obj.u) if name=="independent" else basis.packet(basis.matrices(x),z,len(obj.u))
    saved=json.loads(args.prepared.read_text())
    pre=joint.hf.sample(groups,mods,saved,definition,oldclock,args)
    for name,p in pre.items():
        if max(abs(p[key]-hp["G10G11"][name][key]) for key in ("metric","curvature","held","original"))>1e-8:
            raise ArithmeticError(("Held-feasible true baseline differs",name))
    raw=copy.copy(basis);del raw.matrices;raw.definition=basis.definition["sourceChartBasis"]
    x=phys["training"].nodes;active=np.flatnonzero((x>raw.c)&(x<raw.end))
    B,Bs,Bss=basis.matrices(x[active]);n=raw.nb
    qs=[]
    for v in phys.values():
        U=v.jets[active,1];V=v.jets[active,2]/v.radius[active,0,None,None]
        qs.append(np.stack((np.sum(U*U,axis=-1),np.sum(U*V,axis=-1),np.sum(V*V,axis=-1)),axis=-1))
    E,F,G=np.concatenate(qs,axis=1).transpose(2,0,1)
    ref=float(np.max(abs(F)/np.sqrt(E*G)))
    mm=[];mmin=[];mmax=[]
    for t in np.pi*np.arange(args.directions)/args.directions:
        a=np.cos(t)**2;b=1-a
        gr=a*E+np.sin(2*t)*F+b*G
        mm.append(sparse.hstack((a*B,b*B),format="csr"))
        mmin.append(gr.min(axis=1));mmax.append(gr.max(axis=1))
    M=sparse.vstack(mm,format="csr");lower=np.concatenate(mmin);upper=np.concatenate(mmax)
    coarse=np.unique(np.r_[raw.breaks,(raw.breaks[:-1]+raw.breaks[1:])/2])
    _,D1,D2=basis.matrices(coarse)
    boxes=[];rr=[]
    for mat,lim in ((D1,args.first),(D2,args.second)):
        dd=sparse.block_diag((mat,mat),format="csr")
        boxes.extend((dd,-dd));rr.extend((np.full(dd.shape[0],lim),np.full(dd.shape[0],lim)))
    box=sparse.vstack(boxes,format="csr");br=np.concatenate(rr)
    eye=sparse.eye(2*n,format="csr");Z=sparse.csr_matrix((2*n,2*n))
    meas=(raw.knots[6:]-raw.knots[:-6])[3:-3]/6
    objective=np.r_[np.zeros(2*n),meas,meas]
    def minimax(e):
        D=sparse.vstack((-(1+e)*M,(1-e)*M,box),format="csr")
        L=sparse.vstack((sparse.hstack((D,sparse.csr_matrix((D.shape[0],2*n)))),
            sparse.hstack((eye,-eye)),sparse.hstack((-eye,-eye))),format="csr")
        rhs=np.r_[1+e-upper,lower-1+e,br,np.zeros(4*n)]
        sol=linprog(objective,A_ub=L,b_ub=rhs,bounds=[(-args.box,args.box)]*(2*n)+[(0,args.box)]*(2*n),method="highs")
        return (None if not sol.success else sol.x[:2*n]),sol.message
    top=max(v["metric"] for k,v in pre.items() if k!="independent")
    lo=0.;hi=top;best=np.zeros(2*n);history=[]
    def physical_peak(zz):
        ei=(1+B@zz[:n])[:,None];gi=(1+B@zz[n:])[:,None]
        a=E/ei-1;g=G/gi-1;b=F/np.sqrt(ei*gi)
        return float(np.max(abs((a+g)/2)+np.hypot((a-g)/2,b)))
    for i in range(args.divisions):
        eps=(lo+hi)/2;zz,msg=minimax(eps)
        history.append(dict(eps=eps,feasible=zz is not None,trueAllAngles=physical_peak(zz) if zz is not None else None,message=msg))
        if zz is None:lo=eps
        else:hi=eps;best=zz
    sel=best
    fractions=[(a,physical_peak(a*best)) for a in np.linspace(0,1,17)]
    factor=min(fractions,key=lambda p:p[1])[0];sel=best*factor
    ce,cg=sel[:n],sel[n:];clock=NewClock(oldclock,raw,ce)
    spec=dict(schema="two-positive-stadium-target-factors-and-integrated-true-material-length-v1",
        entry=c.sha(__file__),oldActualMetric=meta["actualMetric"],oldFullXYZ=hp["actualSource"],
        guide=c.sha(args.prior_guide),projection=c.sha(args.projected),oldClockFunction="p32 matched .018 physical clock",
        knots=raw.knots.tolist(),coeffSquaredSpeedHex=[float(a).hex() for a in ce],
        coeffSquaredAngularRatioHex=[float(a).hex() for a in cg],minimumFactorsLower=1-args.box,
        newS=float(clock.jets([raw.end])[0][0]),deltaS=float(clock.cum[-1]),
        target="dsnew^2+fnew^2du^2; dsnew/dsold=sqrt(1+Bce); fnew=fold*sqrt(1+Bcg)",
        allRadiiHaveExactZeroCoefficientTwoJetsAtEndpoints=True,selectionIsG10Only=True)
    target=c.stable(spec);new_b=c.physical_basis(raw,clock,target)
    for name,obj in groups.items():
        x=obj.nodes;b,bs,bss=basis.matrices(x)
        q=np.sqrt(1+b@ce);dq=(bs@ce)/(2*q)
        w=np.sqrt(1+b@cg);ws=(bs@cg)/(2*w);wss=(bss@cg)/(2*w)-(bs@cg)**2/(4*w**3)
        a,aa,aaa=obj.radius.T
        rz=np.stack((a*w,aa*w+a*ws,aaa*w+2*aa*ws+a*wss),axis=1)
        rz[:,2]=rz[:,2]/q**2-rz[:,1]*dq/q**3;rz[:,1]/=q
        obj.radius=rz
        for j in range(0,len(x),12):
            sl=slice(j,j+12);obj.jets[sl]=c.physical_jet(obj.jets[sl],q[sl],dq[sl])
        s,h,hx=clock.jets(x);obj.s,obj.h,obj.hx=s,h,hx
        if name!="independent":weights[name]={k:.5*np.asarray(w)*h for k,w in saved["caches"][name]["weights"].items()}
    post=joint.hf.sample(groups,mods,saved,definition,clock,args)
    for name in pre:
        if abs(pre[name]["held"]-post[name]["held"])>1e-12 or abs(pre[name]["curvature"]-post[name]["curvature"])>2e-9:
            raise ArithmeticError(("Material clock changed the source image",name))
    report=dict(schema=spec["schema"],spec=spec,SHA=target,before=pre,after=post,ringShearFloor=ref,directionalHistory=history,
        chosenG10Factor=factor,oldG10SamplesPreserved=True,angles=args.directions,actualRayTrial=[(float(a),v) for a,v in fractions])
    c.save(Path(str(args.prefix)+"-redesigned.json"),report)
    meta.update(actualMetric=target,physicalBasis=new_b.definition,newFreeMeridianInput=spec,
        positiveFullMaterialClock=True,heldFeasiblePhysicalSource=c.sha(args.projected),inheritedNewMetricIterations=0)
    print(json.dumps(dict(event="actualNewStadiumMetric",newS=spec["newS"],deltaS=spec["deltaS"],floor=ref,
        before=pre["independent"]["metric"],g11={k:post["independent"][k] for k in ("metric","curvature","held")},target=target)),flush=True)
    return definition,new_b,clock,phys,g11,weights,mods,radius,meta,(sum(v["original"] for k,v in post.items() if k!="independent"),post["independent"]["metric"])


if __name__=="__main__":
    ap=joint.slope.args_base()
    for n in ("fixed-stadium","prior-guide","projected"):ap.add_argument("--"+n,type=Path,required=True)
    ap.add_argument("--guide-scale",type=float,default=.0015);ap.add_argument("--directions",type=int,default=20)
    ap.add_argument("--divisions",type=int,default=9);ap.add_argument("--box",type=float,default=.25)
    ap.add_argument("--first",type=float,default=3.);ap.add_argument("--second",type=float,default=65.)
    args=ap.parse_args();args.resume=None
    if args.source_only:prepare(args)
    else:
        joint.full.prepare=prepare
        joint.main(args)
