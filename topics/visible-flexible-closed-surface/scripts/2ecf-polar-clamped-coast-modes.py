#!/usr/bin/env python3
"""18 clamped Cartesian coast-profile controls, full unchanged H65 fixed-g objective."""
import argparse
import copy
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

for key in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):os.environ[key]="1"
import numpy as np
from scipy.interpolate import BSpline


def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m)
    return m


def radial(nodes,b):
    relative=np.array([.0125,.025,.05,.08,.12,.18])
    knots=np.r_[np.repeat(b,6),b+relative,np.repeat(b+.24,6)]
    curve=BSpline(knots,np.eye(len(knots)-6),5,extrapolate=False)
    mats=[]
    for j in range(3):
        mat=np.zeros((len(nodes),len(relative)))
        active=(nodes>b)&(nodes<b+.24)
        mat[active]=curve(nodes[active],nu=j)[:,3:-3]
        mats.append(mat)
    return mats


def variation(mats,delta,amplitude):
    val,first,second=(m@amplitude for m in mats)
    change=val[:,None,None,:]*delta
    change[:,1]+=first[:,None,:]*delta[:,0]
    change[:,3]+=2*first[:,None,:]*delta[:,1]+second[:,None,:]*delta[:,0]
    change[:,4]+=first[:,None,:]*delta[:,2]
    return change


def summary(val):
    return {k:val[k] for k in ("squaredNorm","groupSquaredNorm","maxRelativeMetric","maxCurvature","minHeldDistance","worstMetric","worstCurvature","rowCount")}


def run(args):
    tick=time.monotonic()
    here=Path(__file__).resolve().parent
    prior=load(here/"2ecf-polar-extended-coast-splice.py","coast_actual_input")
    saved,definition,basis,caches,mods,state=prior.source(args)
    z=np.asarray(state["z"]).reshape(basis.nb,basis.na)
    joint=load(args.scripts/"6a65-geometry-gap-window-two-grid-cartesian.py","mode_joint")
    area=load(args.scripts/"6a65-geometry-area-ratio-power-two.py","mode_area")
    load(here/"2ecf-polar-complete-two-grid-streamed.py","mode_streaming").install(joint)
    config=mods["stream"].point.PointConfig(**definition["pointConfig"])
    weights={k:{n:.5*np.asarray(v) for n,v in r["weights"].items()} for k,r in saved["caches"].items()}
    recipe=copy.deepcopy(definition["recipe"]);recipe["cachePointBlocks"]=False
    recipe["basis"].update(radialBasisCount=basis.nb,support="b_to_developed_cut")
    area_def=dict(targetAreaRatio=.5,strength=1.,reciprocalPower=2)
    data={}
    for key,path in (("training",args.training_coast),("observer",args.observer_coast)):
        cache=caches[key];ix,coast,meta=prior.verified_coast(path,prior.sha(args.prepared),key,cache.nodes,cache.u)
        whole=cache.jets+basis.packet(basis.matrices(cache.nodes),z,len(cache.u))
        base=whole[ix].copy()
        box=copy.copy(cache);box.jets=whole
        data[key]=(box,ix,base,coast-base,radial(cache.nodes[ix],basis.c))
    zero=np.zeros_like(z)
    def evaluate(a):
        for box,ix,base,delta,mats in data.values():
            box.jets[ix]=base+variation(mats,delta,a)
        groups={k:v[0] for k,v in data.items()}
        val,_=area.observe(joint,mods["stream"],basis,groups,weights,zero,config,recipe,area_def)
        if val["rowCount"]!=4291840:raise ArithmeticError("Missing physical rows")
        return summary(val)
    def normeq(a):
        gram=np.zeros((18,18));S=np.zeros_like(gram);grad=np.zeros(18);local_cost=0.
        for key,(box,ix,base,delta,mats) in data.items():
            N=len(box.u)
            for start in range(0,len(ix),8):
                sl=slice(start,start+8);i=ix[sl];M=[m[sl] for m in mats];D=delta[sl]
                jet=base[sl]+variation(M,D,a)
                W={k:v[i,None]/N for k,v in weights[key].items()}
                bb=box.radius[i,0,None]
                phys=mods["stream"].point.PointLinearized(jet.swapaxes(1,2),bb,config,W)
                ap=area.AreaPacket(jet,bb,W["metric"],.5)
                residual=np.r_[phys.residual.ravel(),ap.residual.ravel()]
                J=np.empty((len(residual),18))
                V=np.empty((jet.size,18))
                # New actual Cartesian H² on the physical two-grid domain.
                # The mixed partial carries multiplicity two in |D²|².
                rs=np.sqrt(W["metric"])[:,None,:,None]*np.sqrt(np.array([.01,1.,1.,.001,.002,.001]))[None,:,None,None]
                for k in range(18):
                    control=np.zeros((6,3));control.flat[k]=1.
                    v=variation(M,D,control)
                    J[:,k]=np.r_[phys.jvp(v.swapaxes(1,2)).ravel(),ap.jvp(v[:,1],v[:,2]).ravel()]
                    V[:,k]=(rs*v).ravel()
                gram+=J.T@J;grad+=J.T@residual;S+=V.T@V
                local_cost+=float(residual@residual)
        return gram,grad,S,local_cost
    a=np.zeros((6,3));current=evaluate(a)
    if abs(current["squaredNorm"]-state["evaluation"]["squaredNorm"])>1e-11:raise ArithmeticError("Parent cost mismatch")
    history=[dict(own=0,amplitudes=a.tolist(),evaluation=current)]
    damping=args.damping
    for idx in range(1,args.steps+1):
        gram,gradient,S,part=normeq(a)
        H=gram+damping*S
        scale=1/np.sqrt(np.diag(H))
        d=-scale*np.linalg.solve(scale[:,None]*H*scale[None,:],scale*gradient)
        relative=float(np.linalg.norm(H@d+gradient)/np.linalg.norm(gradient))
        if relative>1e-8:raise ArithmeticError("Mixed correction normal solve failed")
        slope=float(gradient@d)
        if idx==1:
            v=np.random.default_rng(2026112819).standard_normal(18);v/=np.linalg.norm(v)
            eps=1e-7
            up=evaluate(a+eps*v.reshape(6,3))["squaredNorm"]
            down=evaluate(a-eps*v.reshape(6,3))["squaredNorm"]
            exact=float(2*gradient@v);fd=(up-down)/(2*eps)
            fd_error=abs(fd-exact)/max(1e-10,abs(exact))
            if fd_error>1e-3:raise ArithmeticError(("Actual full objective derivative failed",fd,exact,fd_error))
        trials=[];accepted=False
        for length in (1.,.5,.25,.125,.0625,.03125,.015625,.0078125):
            test=evaluate(a+length*d.reshape(6,3))
            accepted=bool(slope<0 and test["squaredNorm"]<current["squaredNorm"] and test["squaredNorm"]<=current["squaredNorm"]+2e-4*length*slope)
            trials.append(dict(length=length,accepted=accepted,evaluation=test))
            if accepted:
                a=a+length*d.reshape(6,3);current=test
                break
        history.append(dict(own=idx if accepted else idx-1,amplitudes=a.tolist(),evaluation=current,
            fullNonlinearAccepted=accepted,normalRelative=relative,damping=damping,allTrials=trials,localGradientBearingSquaredNorm=part))
        print(idx,accepted,current["squaredNorm"],current["maxRelativeMetric"],current["maxCurvature"],flush=True)
        if not accepted:break
        damping=damping/3 if length==1 else 2*damping
    out=dict(schema="clamped-H65-actual-18-coast-profile-physical-fixed-target-v1",entrySHA256=prior.sha(__file__),
        parentSHA256=prior.sha(args.state),preparedSHA256=prior.sha(args.prepared),trainingCoastSHA256=prior.sha(args.training_coast),
        observerCoastSHA256=prior.sha(args.observer_coast),physicalRows=4291840,sourceOutsideSupportAndBothTwoJetsUnchanged=True,
        innerProducts="two complete G10 grids, all original nonlinear residual rows. Only Jacobian-zero rows outside correction support omitted from normal",
        correction="diag(6 clamped quintic coefficients per XYZ) times prolonged coast minus actual parent field",
        firstFullObjectiveDirectionalDerivative=dict(epsilon=eps,finiteDifference=fd,analytic=exact,relativeError=fd_error),
        history=history,seconds=time.monotonic()-tick)
    with args.output.open("x") as f:
        json.dump(out,f,indent=2)
        f.write("\n")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    for name in ("scripts","state","prepared","training-coast","observer-coast","output"):p.add_argument("--"+name,required=True,type=Path)
    p.add_argument("--steps",type=int,required=True);p.add_argument("--damping",type=float,required=True)
    args=p.parse_args()
    if not 1<=args.steps<=20 or args.damping<=0:raise ValueError("A positive finite epoch is required")
    run(args)
