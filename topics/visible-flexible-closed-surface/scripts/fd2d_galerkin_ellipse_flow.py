#!/usr/bin/env python3
"""Oversampled nonlinear elliptic-core design with a projected velocity field.

Unlike point-collocation Frenet stepping, the RHS is evaluated on a finer
angular grid and then projected to the state Fourier space. Curvature bounds
use the ACTUAL projected velocity and its time derivative; metric diagnostics
include E, F, G on the finer grid. These remain finite design diagnostics, not
an all-angle certificate, a fixed-g refinement, a tail match, or a closed map.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import resample
from scipy.special import ellipe

HERE=Path(__file__).resolve().parent
_sp=importlib.util.spec_from_file_location('fd2d_control',HERE/'fd2d_controlled_ellipse_flow.py')
ctl=importlib.util.module_from_spec(_sp);_sp.loader.exec_module(ctl)


class ProjectedFlow:
    def __init__(self,control,nodes,oversample,A,B,K,tracking,max_calls,filter_strength=0.,filter_order=16,symmetry=False):
        self.control=control;self.nodes=nodes;self.work=nodes*oversample
        self.A=A;self.B=B;self.K=K;self.tracking=tracking;self.max_calls=max_calls;self.calls=0
        self.filter_strength=filter_strength;self.filter_order=filter_order;self.symmetry=symmetry
        self.a0=2*A*float(ellipe(1-(B/A)**2))/math.pi
        theta=np.arange(nodes)*(2*np.pi/nodes)
        self.initial=np.column_stack((A*np.cos(theta),B*np.sin(theta),np.zeros(nodes)))
        tw=np.arange(self.work)*(2*np.pi/self.work)
        self.initial_speed=np.sqrt(A*A*np.sin(tw)**2+B*B*np.cos(tw)**2)
        self.k=np.fft.fftfreq(self.work,1/self.work)
        self.cache_s=None;self.cache_y=None;self.cache_f=None

    def derivative(self,x,order=1):
        return np.fft.ifft(np.fft.fft(x,axis=0)*((1j*self.k)**order)[:,None],axis=0).real

    def project(self,x):
        coarse=resample(x,self.nodes,axis=0)
        if self.filter_strength>0 or self.symmetry:
            coeff=np.fft.rfft(coarse,axis=0);kk=np.arange(len(coeff))
            if self.filter_strength>0:
                coeff*=np.exp(-self.filter_strength*(kk/(self.nodes/2))**self.filter_order)[:,None]
            if self.symmetry:
                keep=np.zeros_like(coeff);odd=kk%2==1;even=kk%2==0
                keep[odd,0]=coeff[odd,0].real;keep[odd,1]=1j*coeff[odd,1].imag
                keep[even,2]=coeff[even,2].real;coeff=keep
            coarse=np.fft.irfft(coeff,n=self.nodes,axis=0)
        return coarse,resample(coarse,self.work,axis=0)

    def frame(self,s,y):
        if s==self.cache_s and self.cache_y is not None and np.array_equal(y,self.cache_y):
            return self.cache_f
        X=resample(np.asarray(y)[:-2].reshape(self.nodes,3),self.work,axis=0)
        u,aa=map(float,y[-2:]);xp,xpp=self.derivative(X),self.derivative(X,2)
        ell=np.linalg.norm(xp,axis=1);T=xp/ell[:,None]
        c=xpp-np.sum(xpp*T,axis=1)[:,None]*T;clen=np.linalg.norm(c,axis=1)
        kappa=clen/ell**2;N=c/clen[:,None];B=np.cross(T,N)
        selected=kappa[self.work//4];vv=u*aa*selected
        alpha=-u*selected/kappa;chart=1-alpha**2;beta=np.sqrt(np.maximum(chart,1e-14))
        Vraw=alpha[:,None]*N+beta[:,None]*B
        Vcoarse,V=self.project(Vraw);vp,vpp=self.derivative(V),self.derivative(V,2)
        ell_s=np.sum(T*vp,axis=1);Ts=(vp-ell_s[:,None]*T)/ell[:,None]
        xt=np.sum(xpp*T,axis=1)
        cs=vpp-(np.sum(vpp*T,axis=1)+np.sum(xpp*Ts,axis=1))[:,None]*T-xt[:,None]*Ts
        ksvec=cs/ell[:,None]**2-2*(ell_s/ell)[:,None]*(kappa[:,None]*N)
        ks=np.sum(N*ksvec,axis=1);Ns=(ksvec-ks[:,None]*N)/kappa[:,None]
        Bs=np.cross(Ts,N)+np.cross(T,Ns);selected_s=ks[self.work//4]
        alphas0=-u*(selected_s/kappa-selected*ks/kappa**2)
        common=N-(alpha/beta)[:,None]*B
        _,Xss0=self.project(alphas0[:,None]*common+alpha[:,None]*Ns+beta[:,None]*Bs)
        _,Xss_rate=self.project(-(selected/kappa)[:,None]*common)
        normal=np.cross(xp,V);normal/=np.linalg.norm(normal,axis=1)[:,None]
        EE=np.sum(V*V,axis=1);FF=np.sum(V*xp,axis=1);GG=ell**2
        L0=np.sum(normal*Xss0,axis=1);coefficient=np.sum(normal*Xss_rate,axis=1)
        MM=np.sum(normal*vp,axis=1);NN=np.sum(normal*xpp,axis=1);K=self.K
        plus=K*GG+NN;minus=K*GG-NN
        if min(float(plus.min()),float(minus.min()))<=0 or float(coefficient.min())<=0:
            lo,hi=1.,-1.;feasibility=-1.
        else:
            lower=-K*EE+(K*FF+MM)**2/plus
            upper=K*EE-(K*FF-MM)**2/minus
            lo=float(np.max((lower-L0)/coefficient));hi=float(np.min((upper-L0)/coefficient))
            feasibility=min(hi-lo,float((plus/GG).min()),float((minus/GG).min()))
        target=self.control.jet(s)[0]*min(1.,float(kappa.min()/selected))
        desired=self.tracking*(target-u);mid=(lo+hi)/2;half=max(0.,(hi-lo)/2)
        rate=mid+half*math.tanh((desired-mid)/half) if half>1e-14 else mid
        LL=L0+coefficient*rate;detI=EE*GG-FF*FF
        tr=(GG*LL-2*FF*MM+EE*NN)/detI;det=(LL*NN-MM*MM)/detI
        curv=abs(tr)/2+np.sqrt(np.maximum(tr*tr/4-det,0.))
        target_ell=aa/self.a0*self.initial_speed
        de=EE-1;df=FF/target_ell;dg=GG/target_ell**2-1
        metric=abs(de+dg)/2+np.hypot((de-dg)/2,df)
        delta=Vraw-V
        horizontal=X[:,0]**2+(X[:,1]-self.A)**2;mask=horizontal<.9**2
        shift=float(np.max(np.sqrt(.9**2-horizontal[mask])-X[mask,2])) if np.any(mask) else None
        acc=rate*aa*selected+u*vv*selected+u*aa*selected_s
        f=dict(X=X,V=V,Vcoarse=Vcoarse,aa=aa,vv=vv,acc=acc,u=u,up=rate,chart=chart,
               rate_feasibility=feasibility,requested_control=target,curvature=curv,
               normal=normal,metric_error=float(metric.max()),angular_error=float(abs(dg).max()),
               E_error=float(abs(de).max()),F_error=float(abs(df).max()),
               velocity_projection_error=float(np.linalg.norm(delta,axis=1).max()),
               velocity_projection_first_derivative_error=float(np.linalg.norm(self.derivative(delta),axis=1).max()),
               held_shift=shift)
        self.cache_s=s;self.cache_y=np.array(y,copy=True);self.cache_f=f
        return f

    def rhs(self,s,y):
        self.calls+=1
        if self.calls>self.max_calls:raise RuntimeError('Finite design RHS-call limit; no complete endpoint.')
        f=self.frame(s,y)
        return np.r_[f['Vcoarse'].ravel(),f['up'],f['vv']]

    def diagnostics(self,s,y):
        f=self.frame(s,y);X=f['X']
        return dict(s=float(s),radius=f['aa'],radial_speed=f['vv'],radial_acceleration=f['acc'],
                    control=f['u'],control_rate=f['up'],requested_control=f['requested_control'],
                    minimum_chart=float(f['chart'].min()),relative_metric_error=f['metric_error'],
                    metric_angular_error=f['angular_error'],metric_E_error=f['E_error'],metric_F_error=f['F_error'],
                    sampled_curvature_max=float(f['curvature'].max()),
                    sampled_support_min=float(np.sum(X*f['normal'],axis=1).min()),
                    maximum_radius=float(np.linalg.norm(X,axis=1).max()),
                    maximum_abs_z=float(abs(X[:,2]).max()),maximum_abs_y=float(abs(X[:,1]).max()),
                    held_witness_min_distance=float(np.linalg.norm(X-np.array([0.,self.A,0.]),axis=1).min()),
                    held_required_upward_shift=f['held_shift'],curvature_rate_feasibility=f['rate_feasibility'],
                    velocity_projection_error=f['velocity_projection_error'],
                    velocity_projection_first_derivative_error=f['velocity_projection_first_derivative_error'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--checkpoint',type=Path)
    p.add_argument('--nodes',type=int,default=256);p.add_argument('--oversample',type=int,default=2)
    p.add_argument('--B',type=float,default=.5);p.add_argument('--umax',type=float,default=.85)
    p.add_argument('--ramp',type=float,default=.25);p.add_argument('--hold',type=float,default=0.)
    p.add_argument('--turn',type=float,default=.3);p.add_argument('--finish',type=float,default=.45)
    p.add_argument('--lead',type=float,default=0.);p.add_argument('--K',type=float,default=7.1)
    p.add_argument('--tracking',type=float,default=20.);p.add_argument('--max-calls',type=int,default=24000)
    p.add_argument('--filter-strength',type=float,default=0.)
    p.add_argument('--filter-order',type=int,default=16);p.add_argument('--symmetry',action='store_true')
    args=p.parse_args();control=ctl.Control(args.umax,args.ramp,args.hold,args.turn,args.finish,args.lead)
    flow=ProjectedFlow(control,args.nodes,args.oversample,1.4,args.B,args.K,args.tracking,args.max_calls,
                       args.filter_strength,args.filter_order,args.symmetry)
    y=np.r_[flow.initial.ravel(),0.,flow.a0]
    def chart_event(s,y):return float(flow.frame(s,y)['chart'].min())-1e-4
    def metric_event(s,y):return 2e-5-flow.frame(s,y)['metric_error']
    def rate_event(s,y):return flow.frame(s,y)['rate_feasibility']
    def slab_event(s,y):return .75-float(abs(flow.frame(s,y)['X'][:,1]).max())
    events=[chart_event,metric_event,rate_event,slab_event];names=['chart','metric','curvature_rate','slab']
    for e in events:e.terminal=True;e.direction=-1
    report=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        control=control.rows,nodes=args.nodes,geometry_grid=flow.work,ellipse_A=1.4,ellipse_B=args.B,
        metric_a0=flow.a0,sampled_curvature_budget=args.K,tracking=args.tracking,
        filter_strength=args.filter_strength,filter_order=args.filter_order,symmetry=args.symmetry,
        initial=flow.diagnostics(0.,y),complete_control=False,closed_surface=False,metric_frozen=False,
        rows=[],metric_knots=[])
    last_s=0.
    try:
        for j,part in enumerate(control.rows):
            sol=solve_ivp(flow.rhs,(part['s0'],part['s1']),y,method='DOP853',rtol=2e-10,atol=2e-12,
                          max_step=.002,t_eval=np.linspace(part['s0'],part['s1'],41),events=events)
            rec=[flow.diagnostics(s,z) for s,z in zip(sol.t,sol.y.T)]
            last_s=float(sol.t[-1]);y=sol.y[:,-1]
            if sol.status==1:
                for ts,zs in zip(sol.t_events,sol.y_events):
                    if len(ts):last_s=float(ts[-1]);y=zs[-1];rec.append(flow.diagnostics(last_s,y))
            report['metric_knots'].extend([{k:r[k] for k in ('s','radius','radial_speed','radial_acceleration')} for r in rec])
            shifts=[r['held_required_upward_shift'] for r in rec if r['held_required_upward_shift'] is not None]
            if shifts:report['sampled_additional_lead_required']=max(report.get('sampled_additional_lead_required',0.),max(shifts))
            row=dict(index=j,status=sol.status,message=sol.message,
                events={name:ts.tolist() for name,ts in zip(names,sol.t_events)},last=rec[-1] if rec else None,
                extrema={key:(min(r[key] for r in rec) if 'min' in key or 'feasibility' in key else max(r[key] for r in rec))
                    for key in ('minimum_chart','relative_metric_error','metric_angular_error','metric_E_error',
                                'metric_F_error','sampled_curvature_max','sampled_support_min','maximum_radius',
                                'maximum_abs_z','maximum_abs_y','held_witness_min_distance','curvature_rate_feasibility',
                                'velocity_projection_error','velocity_projection_first_derivative_error')})
            report['rows'].append(row);args.out.write_text(json.dumps(report,indent=2)+'\n')
            if args.checkpoint:
                np.savez_compressed(args.checkpoint,state=y,s=last_s,
                    parameters=json.dumps({k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()}),
                    source_sha256=report['source_sha256'])
            print(json.dumps(row),flush=True)
            if sol.status!=0:break
        else:report['complete_control']=True
    except Exception as exc:report['failure']=str(exc)
    report['rhs_calls']=flow.calls;args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(event='complete',complete_control=report['complete_control'],
                         rhs_calls=flow.calls,failure=report.get('failure'))))


if __name__=='__main__':main()
