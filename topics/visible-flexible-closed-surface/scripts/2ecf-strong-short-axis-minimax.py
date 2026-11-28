#!/usr/bin/env python3
"""True length and fixed endpoint tangents/curvatures for two projected symmetry-plane meridians."""
import os
for n in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[n]="1"
import argparse
import importlib.util
import json
from pathlib import Path
import sys
from math import pi
import numpy as np
from scipy.interpolate import BSpline,CubicHermiteSpline
from scipy.integrate import cumulative_simpson
from scipy.optimize import minimize

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj;spec.loader.exec_module(obj);return obj
c=load(Path(__file__).with_name("2ecf-strong-new-material-clock.py"),"axial_length_inputs")

def sim(y,t):
    return cumulative_simpson(y,x=t,axis=0,initial=0.)

def design(args):
    saved,definition,coarse,fine,caches,mods,z,alpha,radius,parent=c.inputs(args)
    cache=caches["training"]
    clockrec=json.loads(args.clock.read_text())
    if clockrec["definition"]["parentDesignStateSHA256"]!=c.sha(args.parent):raise ValueError("Wrong clock parent")
    clock=c.Clock(fine,[float.fromhex(g) for g in clockrec["definition"]["gammaHex"]])
    keep=(cache.nodes>=fine.c)&(cache.nodes<=fine.end);x=cache.nodes[keep]
    s,v,vx=clock.jets(x)
    p=cache.jets[keep]+fine.packet(fine.matrices(x),z,len(cache.u))
    p=c.physical_jet(p,v,vx)
    cuts=int(args.spans)
    knots=np.r_[np.zeros(4),np.arange(1,cuts)/cuts,np.ones(4)]
    fulln=len(knots)-4
    spline=BSpline(knots,np.eye(fulln),3)
    ts=np.linspace(0,1,257)
    sw=np.ones(len(ts));sw[1:-1:2]=4;sw[2:-1:2]=2;sw*=1/(3*(len(ts)-1))
    length=s[-1]-s[0]
    B=spline(ts)[:,2:-2]
    D=spline(ts,nu=1)[:,2:-2]/length
    D2=spline(ts,nu=2)[:,2:-2]/length**2
    rows={}
    for k,name,component in [(len(cache.u)//4,"short",1)]:
        P=p[:,:,k][:,:,[component,2]]
        start=P[0,0];end=P[-1,0]
        tangent=P[:,1];acc=P[:,3]
        theta=np.unwrap(np.arctan2(tangent[:,1],tangent[:,0]))
        basecurv=(tangent[:,0]*acc[:,1]-tangent[:,1]*acc[:,0])/np.linalg.norm(tangent,axis=1)**3
        endangle=theta[-1]+(2*pi*args.winding if name=="short" else 0.)
        core=CubicHermiteSpline([0,1],[theta[0],endangle],length*basecurv[[0,-1]])
        C=core(ts);Cp=core(ts,nu=1)/length;Cpp=core(ts,nu=2)/length**2
        prior=np.interp(ts,(s-s[0])/length,theta)+(endangle-theta[-1])*ts
        smooth=args.smoothing
        desired=end-start
        def path(a):
            th=C+B@a
            dr=np.stack((np.cos(th),np.sin(th)),axis=1)
            return start+length*sim(dr,ts)
        def pathjac(a):
            th=C+B@a
            return length*sim(np.stack((-np.sin(th),np.cos(th)),axis=1)[:,:,None]*B[:,None,:],ts)
        def value(a):
            delta=C+B@a-prior
            bend=Cpp+D2@a
            return .5*(sw@(delta**2+smooth*bend**2)),B.T@(sw*delta)+smooth*D2.T@(sw*bend)
        def eq(a):return path(a)[-1]-end
        def ej(a):return pathjac(a)[-1]
        def bounds(a):
            kappa=Cp+D@a
            points=path(a)[::4];r,h=points.T
            central=definition["pointConfig"]["central_a"]
            held=(central-r)**2+h*h if name=="short" else central**2+r*r+h*h
            ball=1.59**2-r*r-h*h
            out=[args.kappa-kappa,args.kappa+kappa,h-.10,.529-h,ball,held-.65**2]
            if name=="short":out.append(.885-r)
            return np.concatenate(out)
        def bj(a):
            points=path(a)[::4];J=pathjac(a)[::4];r,h=points.T;dr,dh=J[:,0],J[:,1]
            central=definition["pointConfig"]["central_a"]
            hj=(2*(r-central) if name=="short" else 2*r)[:,None]*dr+2*h[:,None]*dh
            rows=[-D,D,dh,-dh,-2*r[:,None]*dr-2*h[:,None]*dh,hj]
            if name=="short":rows.append(-dr)
            return np.vstack(rows)
        a0=np.linalg.lstsq(B,prior-C,rcond=None)[0]
        best=None
        histories=[]
        rg=np.random.default_rng(2026112821)
        rngs=[(0.,0.,0.), (1.,0.,0.),(-1.,0.,0.),(0.,1.,0.),(0.,-1.,0.),(0.,0.,1.),(0.,0.,-1.)]
        ts0=np.linspace(0.,1.,len(a0)+2)[1:-1]
        for j in range(args.seed_count):
            amp=rngs[j] if j<len(rngs) else rg.normal(0.,1.2,3)
            init=a0+sum(amp[m]*np.sin((m+1)*pi*ts0) for m in range(3))
            klimit=np.max(abs(Cp+D@init))+3.
            def augmented_value(t):
                cc=t[:-1];kvar=t[-1]
                cost,jac=value(cc)
                return kvar+.04*cost,np.r_[.04*jac,1.]
            def minimax_cons(t):
                v=bounds(t[:-1])
                v[:2*len(ts)]+=t[-1]-args.kappa
                return v
            def minimax_jac(t):
                jac=bj(t[:-1]);col=np.zeros(jac.shape[0]);col[:2*len(ts)]=1.
                return np.column_stack((jac,col))
            opt=minimize(augmented_value,np.r_[init,klimit],jac=True,method="SLSQP",
                bounds=[(None,None)]*len(init)+[(0.,200.)],constraints=[
                dict(type="eq",fun=lambda t:eq(t[:-1]),jac=lambda t:np.column_stack((ej(t[:-1]),[0.,0.]))),
                dict(type="ineq",fun=minimax_cons,jac=minimax_jac)],
                options=dict(ftol=2e-10,maxiter=200,disp=False))
            a=opt.x[:-1];peak=np.max(abs(Cp+D@a))
            good=min(minimax_cons(opt.x))>-1e-6 and np.max(np.abs(eq(a)))<1e-7
            histories.append(dict(index=j,success=bool(opt.success),feasible=bool(good),
                message=opt.message,kappa=float(peak),enderr=float(np.linalg.norm(eq(a))),
                residual=float(min(minimax_cons(opt.x)))))
            if good and (best is None or peak<best.fun):
                from types import SimpleNamespace
                best=SimpleNamespace(x=a,fun=float(peak),nit=opt.nit)
            if good and peak<args.kappa-.02:break
        if best is None:
            rows[name]=dict(success=False,histories=histories,portCurvatures=basecurv[[0,-1]].tolist(),
                thetaEndpoints=[float(theta[0]),float(endangle)]);continue
        a=best.x
        tt=np.linspace(0.,1.,8193)
        ang=core(tt)+spline(tt)[:,2:-2]@a
        kap=core(tt,nu=1)/length+spline(tt,nu=1)[:,2:-2]@a/length
        points=start+length*sim(np.stack((np.cos(ang),np.sin(ang)),axis=1),tt)
        posfit=np.max(np.linalg.norm(points-np.stack([np.interp(tt,(s-s[0])/length,P[:,0,j]) for j in range(2)],axis=1),axis=1))
        rows[name]=dict(success=True,histories=histories,iterations=best.nit,angleCoefficientsHex=[float(q).hex() for q in a],
            coreAngles=[float(theta[0]),float(endangle)],coreSignedCurvatures=basecurv[[0,-1]].tolist(),portPositions=[start.tolist(),end.tolist()],
            independent8193EndpointError=(points[-1]-end).tolist(),independent8193MaximumCurvature=float(np.max(abs(kap))),
            independent8193MinHeight=float(points[:,1].min()),independent8193MaxHeight=float(points[:,1].max()),
            independent8193MinRadius=float(points[:,0].min()),independent8193MaxRadius=float(points[:,0].max()),
            maximumDisplacementFromWarmPolyline=float(posfit),objective=float(best.fun))
    out=dict(schema="two-real-planar-axis-new-material-length-v1",entry=c.sha(__file__),prepared=c.sha(args.prepared),
        parent=c.sha(args.parent),clock=c.sha(args.clock),length=length,startS=float(s[0]),endS=float(s[-1]),
        winding=args.winding,seedCount=args.seed_count,training257Independent8193=True,spans=cuts,knots=knots.tolist(),kappaGuide=args.kappa,
        smoothing=args.smoothing,axes=rows,scope="Two symmetry-plane meridians only; not a surface field",
        allPhysicalSourceJetsUsedAtPorts=True,noClosedMetricReachClaim=True)
    h=c.save(args.output,out)
    print(json.dumps(dict(SHA256=h,length=length,axes={n:{k:v for k,v in d.items() if k not in ("angleCoefficientsHex","coreAngles","coreSignedCurvatures","portPositions")} for n,d in rows.items()})),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    c.common_args(ap);ap.add_argument("--clock",required=True,type=Path);ap.add_argument("--output",required=True,type=Path)
    ap.add_argument("--spans",type=int,default=16);ap.add_argument("--kappa",type=float,default=9.2)
    ap.add_argument("--smoothing",type=float,default=1e-6)
    ap.add_argument("--winding",type=int,default=0);ap.add_argument("--seed-count",type=int,default=12)
    design(ap.parse_args())
