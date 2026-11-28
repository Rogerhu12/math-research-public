#!/usr/bin/env python3
"""Fit a full quadrant of actual radial/height curves using prescribed speed and physical port two-jets."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.interpolate import BSpline, CubicHermiteSpline
from scipy.integrate import cumulative_simpson
from scipy.fft import dct
from scipy.optimize import minimize

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
def run(a):
    here=Path(__file__).parent
    ob=load(here/'2ecf-polar-raised-monotone-oblique-connector.py','family_endpoint')
    ends=ob.Ends(a.scripts,a.ramp,a.coast,a.amplitude,a.flat,a.trace_nodes)
    theta=np.linspace(0,np.pi/2,a.angles+1)
    p=[np.stack([q[1][k](theta) for k in ('rho','z')],axis=-1) for q in ends.specs]
    b=float(a.b);S=float(a.end);L=S-b
    t=np.linspace(0,1,257);dt=np.linspace(0,1,4097);stride=4096//a.h
    if int(stride)*a.h!=4096:raise ValueError('Physical h must divide integration audit grid')
    ww=np.ones(len(t));ww[1:-1:2]=4;ww[2:-1:2]=2;ww/=3*(len(t)-1)
    knots=np.r_[np.zeros(4),np.arange(1,a.spans)/a.spans,np.ones(4)]
    op=BSpline(knots,np.eye(len(knots)-4),3)
    bs=op(t)[:,2:-2];ds=op(t,nu=1)[:,2:-2];ds2=op(t,nu=2)[:,2:-2]
    fineB=op(dt)[:,2:-2];fineD=op(dt,nu=1)[:,2:-2]
    init=None;rows=[];curves=[];lastprev=None;fails=0
    for i,angle in enumerate(theta):
        left,right=p[0][i],p[1][i];P0,V0,K0=left;P1,V1,K1=right
        v0,v1=np.linalg.norm(V0),np.linalg.norm(V1)
        t0,t1=np.arctan2(V0[1],V0[0]),np.arctan2(V1[1],V1[0]);t1=np.pi+(t1-np.pi+np.pi)%(2*np.pi)-np.pi+2*np.pi*a.winding
        cross=lambda x,y:x[0]*y[1]-x[1]*y[0]
        h=CubicHermiteSpline([0,1],[t0,t1],L*np.array([cross(V0,K0)/v0**2,cross(V1,K1)/v1**2]))
        spd=CubicHermiteSpline([0,1],[v0,v1],L*np.array([V0@K0/v0,V1@K1/v1]))
        v=spd(t);vd=spd(dt);vprime=spd(dt,nu=1)/L
        if min(vd)<.7:raise ArithmeticError('Regular speed needed')
        C=h(t);Cp=h(t,nu=1);Cpp=h(t,nu=2)
        I=cumulative_simpson(np.eye(len(t)),x=t,axis=0,initial=0.)[::4]
        ortho=np.array([[0.,1.],[-1.,0.]])
        H=L*I*v[None,:]
        ca,sa=np.cos(angle),np.sin(angle)
        def geometry(x):
            dr=vel(x);normal=dr@ortho
            points=P0+H@dr
            jac=np.einsum('ij,jk,ja->ika',H,normal,bs,optimize=True)
            radi,height=points.T
            yr=radi*sa
            held=np.sqrt(radi**2-2*ends.master.A*yr+ends.master.A**2+height**2)
            ball=np.hypot(radi,height)
            sm=np.clip((radi-.52)/.02,0,1)
            allow=.415+.113*sm**3*(10+sm*(-15+6*sm))
            allowd=.113/.02*30*sm**2*(1-sm)**2
            # Values are positive exactly when that internal guide is violated.
            vals=np.stack([.65-held,yr-.885,height-allow,.10-height,ball-1.59])
            grads=[(-(radi-ends.master.A*sa)*jac[:,0].T-height*jac[:,1].T)/held,
                   sa*jac[:,0].T,jac[:,1].T-allowd*jac[:,0].T,-jac[:,1].T,
                   (radi*jac[:,0].T+height*jac[:,1].T)/ball]
            pos=np.maximum(vals,0.)
            return .5*np.mean(np.sum(pos**2,axis=0)),sum(g@v for g,v in zip(grads,pos))/len(radi)
        def vel(x):
            ang=C+bs@x
            return np.stack([np.cos(ang),np.sin(ang)],axis=1)
        def eq(x):return L*(ww*v)@vel(x)-(P1-P0)
        def ej(x):
            q=vel(x);return L*(np.stack([-q[:,1],q[:,0]])*(ww*v))@bs
        def value(x):
            grad=Cp+ds@x;d2=Cpp+ds2@x
            curv=grad/(v*L);excess=np.maximum(abs(curv)-a.kappa,0)*np.sign(curv)
            delta=(x-init) if init is not None else 0*x
            gv,gg=geometry(x)
            return (.5*(ww@(grad*grad+.0008*d2*d2+a.penalty*excess*excess))+.004*delta@delta+a.geometry_weight*gv,
                      ds.T@(ww*grad)+.0008*ds2.T@(ww*d2)+a.penalty*ds.T@(ww*excess/(v*L))+.008*delta+a.geometry_weight*gg)
        pred=(init+(init-lastprev) if init is not None and lastprev is not None else init)
        starts=[pred,init] if init is not None else []
        starts += [z*np.sin(np.linspace(0,np.pi,bs.shape[1]+2)[1:-1]) for z in (0,-1.5,1.4,-3.0,3.0)]
        opts=[]
        for a0 in starts:
            if a0 is None:continue
            res=minimize(value,a0,jac=True,method='SLSQP',constraints=[dict(type='eq',fun=eq,jac=ej)],options=dict(ftol=2e-10,maxiter=150,disp=False))
            err=np.linalg.norm(eq(res.x))
            if err<3e-7 and np.all(np.isfinite(res.x)):
                opts.append(res)
                if init is not None and err<1e-9:break
        if not opts:
            fails+=1;print('failed',i,res.message,float(np.linalg.norm(eq(res.x))),flush=True)
            # Keep the genuine last fit and pay a complete smooth endpoint position correction.
            best=res
        else:best=min(opts,key=lambda r:value(r.x)[0])
        lastprev=init;init=best.x.copy()
        ang=h(dt)+fineB@init;angp=(h(dt,nu=1)+fineD@init)/L
        tangent=np.stack([np.cos(ang),np.sin(ang)],axis=1)
        velD=vd[:,None]*tangent
        accD=vprime[:,None]*tangent+vd[:,None]*angp[:,None]*np.stack([-tangent[:,1],tangent[:,0]],axis=1)
        pos=P0+L*cumulative_simpson(velD,x=dt,axis=0,initial=0.)
        fix=P1-pos[-1];s5=dt**3*(10+dt*(-15+6*dt))
        pos+=s5[:,None]*fix;velD+=(30*dt**2*(1-dt)**2/L)[:,None]*fix
        accD+=(60*dt*(1-dt)*(1-2*dt)/L**2)[:,None]*fix
        speed=np.linalg.norm(velD,axis=1)
        if min(pos[:,0])<=.04 or min(speed)<.05:raise ArithmeticError('Singular physical ray')
        kap=abs(velD[:,0]*accD[:,1]-velD[:,1]*accD[:,0])/speed**3
        arr=np.stack([pos[::stride],velD[::stride],accD[::stride]],axis=1)
        log=arr.copy();rr=arr[:,0,0]
        log[:,0,0]=np.log(rr);log[:,1,0]=arr[:,1,0]/rr;log[:,2,0]=arr[:,2,0]/rr-log[:,1,0]**2
        curves.append(log)
        dist=np.sqrt((pos[:,0]*np.cos(angle))**2+(pos[:,0]*np.sin(angle)-ends.master.A)**2+pos[:,1]**2)
        row=dict(theta=float(angle),objective=float(best.fun),maxRayKappa=float(max(kap)),minRaySpeed=float(min(speed)),
            maxRaySpeed=float(max(speed)),minHeight=float(min(pos[:,1])),maxHeight=float(max(pos[:,1])),minHeld=float(min(dist)),
            minRad=float(min(rr)),maxRad=float(max(rr)),twoComponentActualEndRepair=fix.tolist(),ownSLSQPSuccess=bool(best.success),
            storedAngleCoefficients=init.tolist(),maxCoeffStep=None if lastprev is None else float(np.max(abs(init-lastprev))))
        rows.append(row)
        if i%4==0:print(i,row['maxRayKappa'],row['minHeight'],row['maxHeight'],row['minHeld'],flush=True)
    coeff=dct(np.array(curves),type=1,axis=0)/a.angles;coeff[[0,-1]]*=.5
    # Re[(sum c_j exp(2ij*theta))] on every physical polar ray, with exact source traces at b and S.
    with a.field.open('xb') as f:np.savez_compressed(f,coeff=coeff,knots=np.linspace(b,S,a.h+1),modes=2*np.arange(a.angles+1))
    out=dict(schema='R273-complete-quadrant-fixed-physical-speed-ray-seed-v1',sourceSHA256=sha(__file__),portCodeSHA256=sha(ob.__file__),
        amp=a.amplitude,flat=a.flat,length=L,b=b,S=S,physicalIntervals=a.h,quadrantIntervals=a.angles,thetaWinding=a.winding,
        curvatureGuide=a.kappa,curvaturePenalty=a.penalty,geometryWeight=a.geometry_weight,rampSHA256=sha(a.ramp),coastSHA256=sha(a.coast),failedSLSQPRays=fails,
        fieldSHA256=sha(a.field),rows=rows,finiteOnly=True,completeSurfaceObservationPending=True)
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','field','output'):p.add_argument('--'+k,type=Path,required=True)
    for k,v in [('spans',12),('angles',64),('h',64),('winding',0),('trace-nodes',1024)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('b',.1815625),('end',.9772364498716914),('amplitude',.4),('flat',.56),('kappa',9.5),('penalty',3.),('geometry-weight',60000.)]:p.add_argument('--'+k,type=float,default=v)
    run(p.parse_args())
