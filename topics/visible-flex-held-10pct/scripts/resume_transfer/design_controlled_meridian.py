#!/usr/bin/env python3
"""Physical m=2 meridian inverse design; linear diagnostics only.

The free part has a_s=cos(theta), z_s=sin(theta), with
 theta=pi/2+A*tanh(sum c_j sin(2*pi*j*x)*(1-cos(2*pi*x))).
Reflection x->1-x makes its exact radial displacement zero. End acceleration
vanishes, so it attaches C2 to the original fixed ShortBridge. No nonlinear
surface, capacity or continuous geometric certificate is asserted.
"""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import argparse, hashlib, importlib.util, json, math, sys, time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize


def load_bridge(path, slope, curvature, peak):
    spec=importlib.util.spec_from_file_location("controlled_short_bridge",path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    cut=dict(radius=.3,backgroundSlope=.08,backgroundSecond=-7*.08/.3)
    bridge=module.ShortBridge(cut,curvature=curvature,peak_fraction=peak)
    m2=4;C=-.08*(.3*slope-m2)/(m2-1)
    def rhs(s,y):
        ar,ap,_=bridge.profile(s);r=float(ar[0]);v=float(ap[0]);b=math.sqrt(1-v*v)
        return np.array([-3*v*y[0]-4*b*y[1],3*v*v*y[0]/b+4*v*y[1]])/r
    sol=solve_ivp(rhs,(bridge.L,0.),[C,1.],method="DOP853",rtol=2e-12,atol=2e-13,max_step=bridge.L/160)
    if not sol.success:raise RuntimeError(sol.message)
    return bridge,sol.y[:,-1]


class ControlledTransfer:
    def __init__(self,bridge,port_vector,steps=256,A=1.45):
        self.bridge=bridge;self.B=port_vector;self.steps=steps;self.A=A
        self.x=np.linspace(0.,1.,2*steps+1)
        self.base=1-np.cos(2*np.pi*self.x)
        self.basep=2*np.pi*np.sin(2*np.pi*self.x)
        freqs=2*np.pi*np.arange(1,5)[:,None]
        self.basis=np.sin(freqs*self.x)*self.base
        self.dbasis=freqs*np.cos(freqs*self.x)*self.base+np.sin(freqs*self.x)*self.basep
        ss=np.linspace(0,bridge.L,257);ar,ap,app=bridge.profile(ss)
        zz=np.r_[0,np.cumsum(np.diff(ss)*(np.sqrt(1-ap[:-1]**2)+np.sqrt(1-ap[1:]**2))/2)]
        self.bridge_r=ar;self.bridge_z=zz
    def calculate(self,p):
        L=float(p[0]);h=np.asarray(p[1:])@self.basis
        th=np.pi/2+self.A*np.tanh(h)
        cc=np.cos(th);bb=np.sin(th)
        curvature=self.A*(1-np.tanh(h)**2)*(np.asarray(p[1:])@self.dbasis)/L
        y=np.array([1.,0.,1.,0.,0.,1.]);values=[y[:2].copy()];dt=1/self.steps
        def rhs(v,c,b):
            r,z,a00,a01,a10,a11=v
            if r<=.02:raise ValueError("radius below design domain")
            h=L/r;k00=-3*c*h;k01=-4*b*h;k10=3*c*c*h/b;k11=4*c*h
            return np.array([L*c,L*b,k00*a00+k01*a10,k00*a01+k01*a11,k10*a00+k11*a10,k10*a01+k11*a11])
        for k in range(self.steps):
            i=2*k;k1=rhs(y,cc[i],bb[i]);k2=rhs(y+dt*k1/2,cc[i+1],bb[i+1]);k3=rhs(y+dt*k2/2,cc[i+1],bb[i+1]);k4=rhs(y+dt*k3,cc[i+2],bb[i+2])
            y=y+dt*(k1+2*k2+2*k3+k4)/6;values.append(y[:2].copy())
        det=y[2]*y[5]-y[3]*y[4]
        core=np.array([y[5]*self.B[0]-y[3]*self.B[1],-y[4]*self.B[0]+y[2]*self.B[1]])/det
        values=np.asarray(values);r,z=values.T
        rad=np.r_[np.hypot(r,z),np.hypot(self.bridge_r,y[1]+self.bridge_z)]
        support=r*bb[::2]-z*cc[::2]
        return dict(parameters=list(map(float,p)),core=core.tolist(),projective_residual=float(core[1]/np.linalg.norm(core)),H_per_unit_core=float(1/core[0]),transfer_determinant=float(det),radial_closure=float(y[0]-1),prefix_height=float(y[1]),total_height=float(y[1]+self.bridge_z[-1]),radius_max=float(r.max()),center_radius_max=float(rad.max()),support_min=float(support.min()),curvature_max=float(np.max(abs(curvature))),theta_range=[float(th.min()),float(th.max())])


def main():
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('--short-bridge',type=Path,required=True);a.add_argument('--out',type=Path,required=True)
    a.add_argument('--slope',type=float,default=11.85689844448521);a.add_argument('--curvature',type=float,default=4.);a.add_argument('--peak',type=float,default=.2)
    a.add_argument('--steps',type=int,default=192);a.add_argument('--maxiter',type=int,default=100);a.add_argument('--Kmax',type=float,default=9.)
    args=a.parse_args();args.out.mkdir(parents=True,exist_ok=True);start=time.time()
    bridge,B=load_bridge(args.short_bridge,args.slope,args.curvature,args.peak)
    model=ControlledTransfer(bridge,B,args.steps)
    rec=dict(scope=__doc__,argv=sys.argv,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),bridge_sha256=hashlib.sha256(args.short_bridge.read_bytes()).hexdigest(),bridge=bridge.summary(),linear_port=args.slope,roots=[],optimizations=[])
    def save():
        rec['seconds']=time.time()-start;(args.out/'record.json').write_text(json.dumps(rec,indent=2)+'\n')
    for amp in (-.25,-.5,-.8,-1.2,-2.,-3.,-5.):
        cache={}
        def evaluate(L):
            if L not in cache:cache[L]=model.calculate([L,amp,0,0,0])
            return cache[L]
        grid=np.linspace(.10,1.7,28);rows=[]
        for L in grid:
            try:rows.append((L,evaluate(L)['projective_residual']))
            except Exception:rows.append((L,None))
        for (lo,u),(hi,v) in zip(rows,rows[1:]):
            if u is None or v is None or u*v>=0:continue
            L=brentq(lambda s:evaluate(s)['projective_residual'],lo,hi,xtol=1e-11)
            row=evaluate(L);rec['roots'].append(row);print(json.dumps(dict(event='root',**row)),flush=True);save()
    seeds=sorted(rec['roots'],key=lambda d:abs(d['H_per_unit_core']))[:4]
    for seed in seeds:
        cache={}
        def calc(p):
            key=tuple(p)
            if key not in cache:cache[key]=model.calculate(p)
            return cache[key]
        def fun(p):return math.log(max(1e-30,abs(calc(p)['H_per_unit_core'])))
        def eq(p):return calc(p)['projective_residual']
        def iq(p):
            d=calc(p)
            return np.array([args.Kmax-d['curvature_max'],1.25-d['total_height'],1.35-d['radius_max'],1.55-d['center_radius_max'],d['support_min']-.15])
        p0=seed['parameters'];z=minimize(fun,p0,method='SLSQP',bounds=[(.10,1.7)]+[(-7.,7.)]*4,constraints=[dict(type='eq',fun=eq),dict(type='ineq',fun=iq)],options=dict(maxiter=args.maxiter,ftol=2e-10,disp=False))
        d=calc(z.x);row=dict(status=int(z.status),message=str(z.message),nfev=int(z.nfev),nit=int(z.nit),inequalities=iq(z.x).tolist(),result=d)
        fine=ControlledTransfer(bridge,B,args.steps*4).calculate(z.x);row['four_times_steps_same_parameters']=fine
        rec['optimizations'].append(row);print(json.dumps(dict(event='optimized',**row)),flush=True);save()
    save()

if __name__=='__main__':main()
