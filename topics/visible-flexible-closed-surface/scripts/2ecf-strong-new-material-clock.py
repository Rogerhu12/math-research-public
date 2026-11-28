#!/usr/bin/env python3
"""New physical meridian length with exact two-jet matching and full Cartesian consumers.

The independent monotone coordinate x labels old source samples, including adjacent doubles.
The physical coordinate is s(x)=x+integral B(x)gamma dx. Matrices returned to the
physical operators always contain derivatives with respect to s, on both grids.
"""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np
from scipy import sparse
from scipy.interpolate import BSpline
from scipy.optimize import minimize

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(1<<20),b""):
            h.update(block)
    return h.hexdigest()

def stable(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()

def save(path,obj):
    with Path(path).open("x") as f:
        json.dump(obj,f,separators=(",",":"),allow_nan=False)
        f.write("\n")
    return sha(path)

def inputs(args):
    here=args.helpers.resolve()
    prepare=load(here/"2ecf-polar-raw-ramp-source-compose.py","newclock_original_prepared")
    saved,definition,full,caches,mods,*_=prepare.validate_prepared(args)
    coarse,_=load(here/"2ecf-polar-fixed-prefix-position-basis.py","newclock_coarse").restrict(full)
    fine,_=load(here/"2ecf-polar-local-suffix-boehm.py","newclock_fine").build(coarse)
    parent=json.loads(args.parent.read_text())
    target=parent["provisionalMetricDefinition"]
    if (parent["modelDefinition"]["basis"]!=fine.definition
            or parent["modelDefinition"]["coarseRadiusBasis"]!=coarse.definition
            or parent["preparedSHA256"]!=sha(args.prepared)
            or parent["modelDefinition"]["solveEntrySHA256"]!=sha(here/"2ecf-polar-H65-two-space-design.py")
            or stable(target)!=parent["provisionalMetricDefinitionSHA256"]
            or target["exactCoefficientHex"]!=[float(y).hex() for y in parent["logRadiusCoefficients"]]):
        raise ValueError("The actual H65 mixed position and explicit radius are required")
    z=np.asarray(parent["z"]).reshape(fine.nb,fine.na)
    alpha=np.asarray(parent["logRadiusCoefficients"])
    radius=load(here/"2ecf-polar-log-radius-operator.py","newclock_source_radius")
    return saved,definition,coarse,fine,caches,mods,z,alpha,radius,parent

class Clock:
    def __init__(self,basis,gamma):
        self.basis=basis
        self.gamma=np.array(gamma,dtype=float)
        if self.gamma.shape!=(basis.nb,) or not np.all(np.isfinite(self.gamma)) or self.gamma.min()<=-.5:
            raise ValueError("The actual positive clock needs finite coefficients above -1/2")
        self.spline=BSpline(basis.knots,np.r_[np.zeros(3),self.gamma,np.zeros(3)],5,extrapolate=False)
        self.primitive=self.spline.antiderivative()
        self.delta=float(self.primitive(basis.end)-self.primitive(basis.c))
    def jets(self,x):
        x=np.asarray(x,dtype=float)
        xc=np.clip(x,self.basis.c,self.basis.end)
        inside=(x>self.basis.c)&(x<self.basis.end)
        s=x+self.primitive(xc)-self.primitive(self.basis.c)
        h=np.where(inside,1+self.spline(xc),1.)
        hx=np.where(inside,self.spline(xc,nu=1),0.)
        return s,h,hx
    def physical_matrices(self,basis,x):
        _,v,dv=self.jets(x)
        B,Bx,Bxx=basis.matrices(x)
        return B,sparse.diags(1/v)@Bx,sparse.diags(1/v**2)@Bxx-sparse.diags(dv/v**3)@Bx

def physical_basis(parent,clock,clock_sha):
    obj=copy.copy(parent)
    obj.matrices=lambda x:clock.physical_matrices(parent,x)
    obj.definition=dict(schema="new-material-composed-clamped-physical-s-basis-v1",sourceChartBasis=parent.definition,
        physicalDomain=clock.jets(np.array([parent.c,parent.end]))[0].tolist(),
        computationalNodes="x exact binary64 old material coordinates",physicalDerivatives="B_s=B_x/v; B_ss=B_xx/v^2-B_x*v_x/v^3",
        clockDefinitionSHA256=clock_sha,dimension=parent.dimension)
    return obj

def physical_jet(jets,h,hx):
    out=np.array(jets,copy=True)
    v=h[:,None,None]
    dv=hx[:,None,None]
    out[:,3]=jets[:,3]/v**2-jets[:,1]*dv/v**3
    out[:,1]=jets[:,1]/v
    out[:,4]=jets[:,4]/v
    return out

def physical_cache(cache,clock,radius):
    s,h,hx=clock.jets(cache.nodes)
    a,ax,axx=cache.radius.T
    target=np.column_stack((a,ax/h,axx/h**2-ax*hx/h**3))
    result=radius.ArrayCache(cache.nodes,cache.u,physical_jet(cache.jets,h,hx),target)
    result.s,result.h=s,h
    return result

def fit(args):
    saved,definition,coarse,fine,caches,mods,z,alpha,radius,parent=inputs(args)
    stream=mods["stream"]
    config=stream.point.PointConfig(**definition["pointConfig"])
    nodes=caches["training"].nodes
    Bs=fine.matrices(nodes)[0].toarray()
    integ=(fine.knots[6:]-fine.knots[:-6])[3:-3]/6
    # Here q(l) is the three-component normalized metric Frobenius defect
    # squared per angle, l=h^-2. Expand in l-1 to preserve small defects.
    moments=np.zeros((len(nodes),5))
    geom=np.zeros(len(nodes))
    min_area=np.inf
    for name,c in caches.items():
        if not np.array_equal(c.nodes,nodes):raise ValueError("The original two grids require the same x")
        base=radius.LogRadiusCache(coarse,c,alpha)
        w={k:.5*np.asarray(v) for k,v in saved["caches"][name]["weights"].items()}
        N=len(c.u)
        for lo in range(0,len(nodes),16):
            sl=slice(lo,lo+16)
            packet=c.jets[sl]+fine.packet(fine.matrices(nodes[sl]),z,N)
            a=base.radius[sl,0,None]
            point=stream.point.PointLinearized(packet.swapaxes(1,2),a,config,{k:v[sl,None]/N for k,v in w.items()})
            e,f,g=point.metric.transpose(2,0,1)
            E=e+1
            A=E**2
            B=2*e*E+f**2
            C=e**2+f**2+g**2
            # Sum over angles of q+q^2/tau^2.
            t=config.metric_tau**-2
            poly=[C+t*C*C,B+2*t*B*C,A+t*(B*B+2*A*C),2*t*A*B,t*A*A]
            for j,v in enumerate(poly):
                moments[sl,j]+=w["metric"][sl]*np.mean(v,axis=1)
            geom[sl]+=np.sum(point.residual[...,3:]**2,axis=(1,2))
            min_area=min(min_area,float(np.min(np.sqrt(point.curvature["w2"])/a)))
    bound=args.bound
    if not 0<bound<.5 or min_area/(1+bound)<=.5:
        raise ValueError("Original q2 barrier must vanish for the full proposed speed box")
    moments[:,0]+=geom
    def cost_and_jac(gamma):
        h=1+Bs@gamma
        v=h**-2-1
        p=moments[:,4].copy()
        dp=np.zeros(len(h))
        for j in (3,2,1,0):
            dp=dp*v+p
            p=p*v+moments[:,j]
        return float(h@p),Bs.T@(p-2*dp/h**2)
    initial=np.full(fine.nb,args.delta/integ.sum())
    zero=cost_and_jac(np.zeros(fine.nb))[0]
    res=minimize(cost_and_jac,initial,jac=True,method="SLSQP",bounds=[(-bound,bound)]*fine.nb,
        constraints=[dict(type="eq",fun=lambda c:float(integ@c-args.delta),jac=lambda c:integ)],
        options=dict(ftol=2e-14,maxiter=600,disp=False))
    clock=Clock(fine,res.x)
    if not res.success or abs(clock.delta-args.delta)>2e-11:
        raise ArithmeticError(str((res.message,clock.delta)))
    binding=dict(schema="new-meridian-material-length-frozen-clock-v1",parentPreparedSHA256=sha(args.prepared),
        parentDesignStateSHA256=sha(args.parent),fitEntrySHA256=sha(__file__),parentSource=definition["sourceIdentity"],
        parentFrozenRadiusSHA256=parent["provisionalMetricDefinitionSHA256"],gammaHex=[float(c).hex() for c in res.x],
        chartBasis=fine.definition,clock="s(x)=x+integral_b^min(max(x,b),S) B(y) gamma dy",
        newTarget="ds^2+a_old(x(s))^2 du^2; a_old includes all 36 frozen parent coefficients",
        newPhysicalSource="complete H65 Cartesian Xold(x(s),u), all original tail/cuff images retained",
        chartToPhysicalJet="Ds=Dx/v; Dss=Dxx/v^2-Dx*v_x/v^3",speedLowerBound=1+min(0.,float(res.x.min())),
        speedUpperBound=1+max(0.,float(res.x.max())),firstTwoSpeedJetsClamped=True,
        deltaRequested=args.delta,coefficientBox=bound,actualLengthIncrease=clock.delta,
        cutOld=fine.end,cutNew=float(clock.jets([fine.end])[0][0]),newCuff=float(clock.jets([nodes[-1]])[0][0]),
        physicalWeights="every original fixed quadrature row in x, multiplied by exact v(x)=ds/dx",
        ownXYZAccepted=0,designIsNotFixedMetricConvergence=True)
    out=dict(definition=binding,definitionSHA256=stable(binding),solver=res.message,iterations=int(res.nit),
        parentQuarticObjective=parent["evaluation"]["squaredNorm"],originalAggregatedObjective=zero,
        objectiveAtPositiveConstantInitial=cost_and_jac(initial)[0],fittedNewMaterialObjective=cost_and_jac(res.x)[0],
        minimumWarmAreaOverBothGrids=min_area,allClocksInProposedBoxHaveInactiveQ2=True,
        fullPhysicalRowCount=4291840,trainingGridSizes=[[958,128],[958,192]],independentUsedToFit=False)
    if abs(zero-parent["evaluation"]["squaredNorm"])>1e-9:raise ArithmeticError("Actual parent complete objective differs")
    digest=save(args.output,out)
    print(json.dumps(dict(clockSHA256=digest,delta=clock.delta,old=zero,new=out["fittedNewMaterialObjective"],iterations=out["iterations"])),flush=True)

def common_args(parser):
    for k in ("helpers","scripts","prepared","parent"):
        parser.add_argument("--"+k,type=Path,required=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    common_args(ap)
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--delta",type=float,default=.006)
    ap.add_argument("--bound",type=float,default=.18)
    fit(ap.parse_args())
