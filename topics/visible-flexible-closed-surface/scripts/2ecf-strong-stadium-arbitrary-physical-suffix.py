#!/usr/bin/env python3
"""Pointwise full-Cartesian p32 post-H65 suffix from every literal parent field and material clock."""
import os
for key in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):os.environ[key]="1"
import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.interpolate import BPoly,BSpline


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m;spec.loader.exec_module(m);return m


home=Path(__file__).parent
normal=load(home/"2ecf-strong-stadium-full-normal-correction.py","stadium_arb_normal")
source=normal.source;c=normal.c;physical=source.physical;joint=normal.joint
rd=lambda p:json.loads(Path(p).read_text())


class Field:
    def __init__(self,args):
        self.arg=args
        self.stream=load(args.scripts/"6a65-cartesian-complete-stream.py","stadium_arb_cart")
        freq=load(args.helpers/"2ecf-polar-fourier-refinement.py","stadium_arb_all_channels")
        self.direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","stadium_arb_angles").direct_packet
        self.full_channels=freq.full_channels
        self.saved=rd(args.prepared)
        warm,ref,diag,warp=map(rd,(args.warm,args.refined_state,args.diagonal,args.warp))
        m=ref["model"]
        for k,p in (("physicalSource",args.field),("baseAngleClock",args.angular_clock),("target",args.diagonal),
                ("warp",args.warp),("prepared",args.prepared),("parent",args.parent),("observer",args.observer),
                ("ramp",args.ramp),("coast",args.coast),("literalParent",args.warm)):
            if m[k]!=c.sha(p):raise ValueError(("Changed literal source",k))
        big,small,stadium,guide,proj,red,bg=map(rd,(args.refined_state,args.stadium_carrier,args.fixed_stadium,
            args.prior_guide,args.projected,args.redesigned_state,args.background))
        rs=rd(args.radius_spec);ds=rd(args.design_spec);ls=rd(args.longer_spec)
        if (rs["newGSHA"]!=stadium["model"]["stadiumTarget"] or ds["SHA"]!=red["model"]["actualMetric"]
                or ls["SHA"]!=bg["model"]["actualMetric"] or ls["newG"]["priorPhysical"]!=c.sha(args.redesigned_state)
                or rs["newG"]["ramp"]!=c.sha(args.stadium_ramp) or rs["newG"]["coast"]!=c.sha(args.stadium_coast)
                or guide["model"]["fixedStadiumCompleteSource"]!=c.sha(args.fixed_stadium) or proj["parent"]!=c.sha(args.prior_guide)
                or ds["spec"]["projection"]!=c.sha(args.projected) or ds["spec"]["guide"]!=c.sha(args.prior_guide)):
            raise ValueError("All matched actual p32 source stages required")
        self.ident=bg["model"]["actualMetric"]
        self.raw24=self.raw(m["trueCarrierBasis"]["sourceChartBasis"])
        self.raw32=self.raw(m["physicalBasis"]["sourceChartBasis"])
        self.cutraw=self.raw(bg["model"]["physicalBasis"]["sourceChartBasis"])
        self.b,self.end=self.raw32.c,self.raw32.end
        self.a=physical.hf.d.SquareClock(self.raw24,np.array([float.fromhex(v) for v in diag["definition"]["CEradialHex"]]))
        self.ba24=c.physical_basis(self.raw24,self.a,m["actualMetric"]);self.ba32=c.physical_basis(self.raw32,self.a,m["actualMetric"])
        self.z24=np.asarray(warm["totalCoefficients"]).reshape(self.ba24.nb,self.ba24.na)
        self.za=np.asarray(big["totalRefinedCoefficients"]).reshape(self.ba32.nb,self.ba32.na)+np.asarray(small["coefficients"]).reshape(self.ba32.nb,self.ba32.na)
        self.bclock=physical.Clock(self.a,self.b,self.end,float.fromhex(rs["newG"]["delta"]))
        self.bb32=c.physical_basis(self.raw32,self.bclock,stadium["model"]["actualMetric"])
        self.zb=sum(np.asarray(st["coefficients"]).reshape(self.bb32.nb,self.bb32.na) for st in (stadium,guide,proj))
        self.ce,self.cg=[np.array([float.fromhex(v) for v in ds["spec"][k]]) for k in ("coeffSquaredSpeedHex","coeffSquaredAngularRatioHex")]
        self.cclock=source.red.NewClock(self.bclock,self.raw32,self.ce)
        self.bc32=c.physical_basis(self.raw32,self.cclock,red["model"]["actualMetric"])
        self.zc=np.asarray(red["coefficients"]).reshape(self.bc32.nb,self.bc32.na)
        long=ls["newG"];self.cut=float(long["oldComputationalCut"]);self.newb=long["newEndOfLockedCoast"];self.ell=long["wholeCoastRealLength"]
        self.dclock=physical.Clock(self.cclock,self.newb,self.end,long["extraMaterial"])
        self.bd=c.physical_basis(self.cutraw,self.dclock,self.ident)
        self.zd=np.asarray(bg["coefficients"]).reshape(self.bd.nb,self.bd.na)
        self.blend=float(ls["chosen"]);self.rblend=long["radiusBlendWidth"]
        self.bRight=rs["newG"]["physicalEnds"][1]
        self.radius=BPoly(np.array(rs["newG"]["outerQuintic"])[:,None],[self.b,self.bRight],extrapolate=False)
        self.logRadius=[float.fromhex(q) for q in rs["newG"]["logExpCoefficientsHex"]]
        self.lift=float(rs["selectedLength"])
        self.pref=joint.slope.MatchedPrefix(args,self.b);self.p0=self.pref.master
        self.definition=copy.deepcopy(self.saved["definition"]);self.definition["pointConfig"]["central_a"]=float(self.pref.support.A)
        self.arb=physical.core.full.two.ArbitraryHF(args)
        self.p=physical.core.full.two.Wave(self.arb.orig.knots,warp["pFrequencies"],False)
        self.q=physical.core.full.two.Wave(self.arb.orig.knots,warp["qFrequencies"],True)
        factor=warp["actualG10Trials"][warp["chosen"]]["factor"]
        self.pv,self.qv=[factor*np.array([float.fromhex(s) for s in warp[k]]) for k in ("pCoefficientHex","qCoefficientHex")]
        self.extra=[]
        for fn in args.extra_state:
            st=rd(fn);s=st["physicalCorrectionBasis"]["sourceChartBasis"]
            if (st["source"]!=c.sha(args.background) or st["sourceMetric"]!=self.ident
                    or st.get("previousPhysicalCorrection")!=(c.sha(self.extra[-1][2]) if self.extra else None)):
                raise ValueError("Ordered full corrected Cartesian chain required")
            if "physicalKnots" in s:raw=self.raw(s)
            else:
                raw=self.stream.HalfTurnBasis(self.cut,self.end,radial_count=s["radialBasisCount"],
                    max_frequency=s["maxAngularFrequency"],normalized_breaks=s["normalizedBreaks"])
            basis=c.physical_basis(raw,self.dclock,self.ident)
            if basis.definition!=st["physicalCorrectionBasis"]:raise ValueError("Same literal angular, radial and physical coefficients required")
            self.extra.append((basis,np.asarray(st["coefficients"]).reshape(basis.nb,basis.na),fn))
        self.portcache={}
    def raw(self,spec):
        o=object.__new__(self.stream.HalfTurnBasis);o.definition=spec;o.knots=np.array(spec["physicalKnots"])
        o.breaks=np.unique(o.knots);o.c,o.end=o.breaks[[0,-1]];o.degree=5;o.full_count=len(o.knots)-6;o.nb=o.full_count-6
        o.M=int(spec["maxAngularFrequency"]);o.channels=self.full_channels(o.M);o.na=len(o.channels)
        o.dimension=o.nb*o.na;o.modes=np.array([n for _,n,_ in o.channels])
        o._spline=BSpline(o.knots,np.eye(o.full_count),5,extrapolate=False)
        if o.dimension!=spec["dimension"]:raise ValueError("Actual declared full Cartesian source")
        return o
    def ports(self,u):
        k=u.tobytes()
        if k not in self.portcache:
            inlet=physical.difference(self.p0.coast_port(self.p0.coast,u),self.arb.ports[0](u))
            right=self.p0.coast_port(self.ell,u)
            self.portcache[k]=inlet,right
        return self.portcache[k]
    def jets(self,x,u):
        x=np.asarray(x,dtype=float);u=np.asarray(u,dtype=float)
        if not (x.ndim==1 and u.ndim==1 and np.all(x>=0) and np.all(x<=self.end)):raise ValueError("Genuine p32 pre-R205 domain required")
        out=np.zeros((len(x),6,len(u),3));rad=np.zeros((len(x),3))
        i0=np.flatnonzero(x<=self.b);i1=np.flatnonzero((x>self.b)&(x<=self.cut));ii=np.flatnonzero(x>self.cut)
        if len(i0):out[i0],rad[i0]=self.pref.rows(x[i0],u)
        if len(i1):
            for k in i1:
                s=self.dclock.jets(x[k:k+1])[0][0];sig=self.p0.coast+s-self.b;P=self.p0.coast_port(sig,u)
                out[k]=np.stack([P[kk] for kk in ("P","V","Pu","A","Vu","Puu")])
                rad[k]=[self.p0.curve.a+self.p0.v*sig,self.p0.v,0.]
        if not len(ii):return out,rad
        xx=x[ii];sa,ha,hxa=self.a.jets(xx);sb,qb,qbp=self.bclock.relative(sa)
        X=c.physical_jet(self.arb.actual(xx,u,self.p,self.q,self.pv,self.qv),ha,hxa)
        X+=self.direct(self.ba24,xx,self.z24,u)+self.direct(self.ba32,xx,self.za,u)
        X=c.physical_jet(X,qb,qbp);ep,true=self.ports(u)
        physical.add_lift(X,sb-self.b,ep,self.lift,1.)
        X+=self.direct(self.bb32,xx,self.zb,u)
        bb,bbs,bbss=self.bb32.matrices(xx)
        d,ds,dss=[M@self.logRadius for M in (bb,bbs,bbss)]
        pv,ps,pss=[self.radius(sb,nu=j) for j in range(3)]
        a,aa,aaa=(np.exp(d)[:,None]*np.stack((pv,ps+pv*ds,pss+2*ps*ds+pv*(dss+ds*ds)),axis=1)).T
        qc=np.sqrt(1+bb@self.ce);qcp=(bbs@self.ce)/(2*qc)
        w=np.sqrt(1+bb@self.cg);ws=(bbs@self.cg)/(2*w);wss=(bbss@self.cg)/(2*w)-(bbs@self.cg)**2/(4*w**3)
        rz=np.stack((a*w,aa*w+a*ws,aaa*w+2*aa*ws+a*wss),axis=1)
        rz[:,2]=rz[:,2]/qc**2-rz[:,1]*qcp/qc**3;rz[:,1]/=qc
        X=c.physical_jet(X,qc,qcp)+self.direct(self.bc32,xx,self.zc,u)
        sc=self.cclock.jets(xx)[0];s,qd,qdp=self.dclock.relative(sc)
        X=c.physical_jet(X,qd,qdp);rz[:,2]=rz[:,2]/qd**2-rz[:,1]*qdp/qd**3;rz[:,1]/=qd
        delta=s-self.newb;front=delta<self.blend
        if np.any(front):X[front]=source.product_blend(X[front],source.develop(true,delta[front]),delta[front]/self.blend,self.blend)
        front=delta<self.rblend
        if np.any(front):
            dist=delta[front];f0=self.p0.curve.a+self.p0.v*self.ell
            left=np.column_stack((f0+self.p0.v*dist,np.full(len(dist),self.p0.v),np.zeros(len(dist))))
            rz[front]=source.scalar_blend(rz[front],left,dist/self.rblend,self.rblend)
        X+=self.direct(self.bd,xx,self.zd,u)
        for basis,z,_ in self.extra:X+=self.direct(basis,xx,z,u)
        out[ii]=X;rad[ii]=rz
        return out,rad


def parser():
    ap=joint.slope.args_base()
    for name in ("fixed-stadium","prior-guide","projected","redesigned-state","background","radius-spec","design-spec","longer-spec"):ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--extra-state",nargs="*",type=Path,default=[])
    for name,v in (("guide-scale",.0025),("box",.25),("first",3.),("second",65.),("extension",.04),("add-length",.014),("radius-blend",.18),("curvature-tau",2.),("metric-sextic",.2)):
        ap.add_argument("--"+name,type=float,default=v)
    for name,v in (("directions",20),("divisions",9),("correction-frequency",12)):ap.add_argument("--"+name,type=int,default=v)
    ap.add_argument("--blends",type=float,nargs="+",default=[.06,.095,.14,.19,.25,.33,.42]);return ap


def validate(args):
    tic=time.monotonic();field=Field(args);_,_,_,gr,g11,_,_,_,_,_=normal.prepare(args)
    rows=[]
    for name,obj in list(gr.items())+[("independent",g11)]:
        idx=np.flatnonzero((obj.nodes>=field.b-.002)&(obj.nodes<=field.end))
        select=np.unique(np.r_[idx[::max(1,len(idx)//28)],idx[-1],idx[np.argsort(abs(obj.nodes[idx]-field.cut))[:5]]])
        ai=np.arange(0,len(obj.u),max(1,len(obj.u)//20));u=obj.u[ai]
        actual,rad=field.jets(obj.nodes[select],u);bg=obj.jets[select][:,:,ai,:].copy()
        for bb,z,_ in field.extra:bg+=field.direct(bb,obj.nodes[select],z,u)
        err=np.max(abs(actual-bg),axis=(0,2,3));re=np.max(abs(rad-obj.radius[select]),axis=0)
        rows.append(dict(group=name,nodes=select.tolist(),angles=ai.tolist(),jetErrors=err.tolist(),radiusErrors=re.tolist()))
        print(json.dumps(dict(group=name,jet=err.tolist(),radius=re.tolist())),flush=True)
        if max(err)>1e-7 or max(re)>2e-8:raise ArithmeticError(("Full physical regression failed",name))
    o=dict(schema="arbitrary-real-p32-physical-six-jets-through-the-longer-V24-suffix-v1",entry=c.sha(__file__),source=c.sha(args.background),
        physicalMetric=field.ident,extraStates=[c.sha(p) for p in args.extra_state],actualRows=rows,seconds=time.monotonic()-tic)
    c.save(Path(str(args.prefix)+"-arbitrary-validation.json"),o)


if __name__=="__main__":
    args=parser().parse_args();args.resume=None;validate(args)
