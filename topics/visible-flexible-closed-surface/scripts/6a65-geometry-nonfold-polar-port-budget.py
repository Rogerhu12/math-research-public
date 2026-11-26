#!/usr/bin/env python3
"""Actual polar-chart and positive-height endpoint budget for a new C2 seed.

No target-metric cache, old solver checkpoint or numerical acceptance is used.
All whole-angle statements in this script are explicitly sampled diagnostics.
"""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[key]="1"
import argparse,hashlib,importlib.util,json,math,sys,time
from pathlib import Path
import numpy as np


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def jmul(a,b):
    return np.stack((a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[0]*b[2]+a[1]*b[1]+a[2]*b[0]))


def jinv(a):
    return np.stack((1/a[0],-a[1]/a[0]**2,a[1]**2/a[0]**3-a[2]/a[0]**2))


def angular_clock(port,u):
    def jet(prefix):
        return np.stack((port[prefix],port[prefix+"u"],port[prefix+"uu"]/2))
    P,V,A=jet("P"),jet("V"),jet("A")
    R2=jmul(P[:,:,0],P[:,:,0])+jmul(P[:,:,1],P[:,:,1]);rec=jinv(R2)
    cross=lambda x,y:jmul(x[:,:,0],y[:,:,1])-jmul(x[:,:,1],y[:,:,0])
    dot=lambda x,y:jmul(x[:,:,0],y[:,:,0])+jmul(x[:,:,1],y[:,:,1])
    ts=jmul(cross(P,V),rec)
    tss=jmul(cross(P,A),rec)-2*jmul(jmul(dot(P,V),rec),ts)
    x,y=port["P"][:,:2].T;xu,yu=port["Pu"][:,:2].T
    xuu,yuu=port["Puu"][:,:2].T
    theta=u+np.arctan2(y*np.cos(u)-x*np.sin(u),x*np.cos(u)+y*np.sin(u))
    tu=(x*yu-y*xu)/(x*x+y*y)
    tuu=(x*yuu-y*xuu)/(x*x+y*y)-2*(x*xu+y*yu)*tu/(x*x+y*y)
    return dict(theta=theta,theta_u=tu,theta_uu=tuu,
        theta_s=ts[0],theta_su=ts[1],theta_suu=2*ts[2],
        theta_ss=tss[0],theta_ssu=tss[1],theta_ssuu=2*tss[2],
        radius=np.hypot(x,y))


def inverse_angle(provider,theta):
    u=np.asarray(theta,float).copy()
    for iteration in range(15):
        port=provider(u);clock=angular_clock(port,u)
        error=np.arctan2(np.sin(clock["theta"]-theta),np.cos(clock["theta"]-theta))
        if np.any(clock["theta_u"]<=0):raise ArithmeticError("Sampled polar angle is not increasing")
        if np.max(abs(error))<5e-14:return u,port,clock,float(np.max(abs(error))),iteration+1
        u-=error/clock["theta_u"]
    raise ArithmeticError("Actual boundary polar inverse did not converge")


def fixed_polar(port,clock):
    P,V,A=port["P"],port["V"],port["A"]
    U,SU,UU=port["Pu"],port["Vu"],port["Puu"]
    r=clock["radius"]
    dot=lambda x,y:np.sum(x[:,:2]*y[:,:2],axis=1)
    rs=dot(P,V)/r;ru=dot(P,U)/r
    rss=(dot(V,V)+dot(P,A)-rs*rs)/r
    rsu=(dot(U,V)+dot(P,SU)-rs*ru)/r
    ruu=(dot(U,U)+dot(P,UU)-ru*ru)/r
    us=-clock["theta_s"]/clock["theta_u"]
    uss=-(clock["theta_ss"]+2*clock["theta_su"]*us+clock["theta_uu"]*us*us)/clock["theta_u"]
    return dict(r=r,rs=rs+ru*us,rss=rss+2*rsu*us+ruu*us*us+ru*uss,
        z=P[:,2],zs=V[:,2]+U[:,2]*us,
        zss=A[:,2]+2*SU[:,2]*us+UU[:,2]*us*us+U[:,2]*uss)


def bounds(x,theta):
    i=int(np.argmin(x));j=int(np.argmax(x))
    return dict(minimum=float(x[i]),maximum=float(x[j]),
                minimumAt=float(theta[i]),maximumAt=float(theta[j]))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--scripts",type=Path,required=True)
    ap.add_argument("--ramp-master",type=Path,required=True)
    ap.add_argument("--coast-master",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--angles",type=int,default=1024)
    ap.add_argument("--degree",type=int,default=31)
    args=ap.parse_args()
    if args.output.exists():raise FileExistsError("A fresh endpoint audit is required")
    start=time.monotonic()
    warm=module(args.scripts/"6a65-geometry-cauchy-unit-t-warm.py","nonfold_endpoint_warm")
    L=.7956739498716915
    master=warm.WarmMaster(args.ramp_master,args.coast_master,
        amplitude=.8746432018013935,Z=.51,right_length=L,coast_length=.02)
    providers=[lambda u:master.coast_port(.02,u),master.cut_port]
    angles=2*np.pi*np.arange(args.angles)/args.angles
    data=[];fixed=[];inverses=[]
    for provider in providers:
        material=provider(angles);clock=angular_clock(material,angles)
        data.append(clock)
        u,port,exactclock,residual,iterations=inverse_angle(provider,angles)
        fixed.append(fixed_polar(port,exactclock))
        inverses.append(dict(maximumResidual=residual,iterations=iterations))
    left,right=fixed;N=args.degree
    delta=right["z"]-left["z"]
    four=np.stack((left["zs"],left["zs"]+L*left["zss"]/N,
                   right["zs"]-L*right["zss"]/N,right["zs"]))
    inner=((N+1)*delta/L-np.sum(four,axis=0))/(N-3)
    height=np.r_[four,inner[None,:]]
    # These are the six degree-5 Bernstein coefficients of Theta_u(s,u).
    l,r=data
    clock_controls=np.stack((l["theta_u"],l["theta_u"]+L*l["theta_su"]/5,
        l["theta_u"]+2*L*l["theta_su"]/5+L*L*l["theta_ssu"]/20,
        r["theta_u"]-2*L*r["theta_su"]/5+L*L*r["theta_ssu"]/20,
        r["theta_u"]-L*r["theta_su"]/5,r["theta_u"]))
    rows=[]
    for label,clock,b in zip(("coast","true_R205_cut"),data,fixed):
        rows.append(dict(side=label,radius=bounds(clock["radius"],angles),
            materialPolarAngleDerivative=bounds(clock["theta_u"],angles),
            materialPhaseShift=bounds(clock["theta"]-angles,angles),
            fixedPolarHeight=bounds(b["z"],angles),
            fixedPolarHeightSpeed=bounds(b["zs"],angles),
            fixedPolarHeightAcceleration=bounds(b["zss"],angles),
            fixedPolarRadiusSpeed=bounds(b["rs"],angles),
            zeroHeightSpeedWithIncompatibleAccelerationPoints=int(np.count_nonzero(
                (np.abs(b["zs"])<1e-15)&((b["zss"]<0) if label=="coast" else (b["zss"]>0))))))
    report=dict(schema="6a65-nonfold-polar-positive-height-endpoint-budget-v1",
        scriptSHA256=sha(__file__),warmSourceSHA256=sha(args.scripts/"6a65-geometry-cauchy-unit-t-warm.py"),
        rampMasterSHA256=sha(args.ramp_master),coastMasterSHA256=sha(args.coast_master),
        parameters=dict(c=master.c,b=master.coast_end,S=master.cut,cuff=master.cuff,
            L=L,amplitude=master.amplitude,Z=master.Z,heightVelocityDegree=N,angles=args.angles),
        boundaries=rows,actualAngleInverse=inverses,heightIncrement=bounds(delta,angles),
        heightVelocityEndControls=[bounds(row,angles) for row in four],
        commonInteriorHeightVelocityControl=bounds(inner,angles),
        minimumAllHeightControls=float(np.min(height)),
        minimumQuinticClockDerivativeControl=float(np.min(clock_controls)),
        clockDerivativeControlBounds=[bounds(row,angles) for row in clock_controls],
        sampledPositiveHeightBudget=bool(np.all(delta>0)&np.all(height>=0)&np.all(inner>0)),
        sampledPositiveQuinticClockBudget=bool(np.all(clock_controls>0)),
        allRadialPositionsBoundByBernsteinOnlyAtTheSampledAngles=True,
        continuousAngularCertificate=False,noWholeFieldConstructedYet=True,
        originalFrozenMetricValueNotEvaluated=True,acceptedResearchSteps=0,
        seconds=time.monotonic()-start,OSExitCode=None,externalExitReceiptRequired=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps(report,allow_nan=False),flush=True)


if __name__=="__main__":main()
