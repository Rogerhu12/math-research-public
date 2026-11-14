#!/usr/bin/env python3
"""Finite elliptic-flow design with an explicit sampled curvature budget.

The scalar control rate is restricted using both principal-curvature matrix
inequalities at every angular node. These sampled restrictions are a design
method, not an interval proof of all-angle reach. An adopted full candidate
must freeze one a(s), solve/refine on that same g, close its actual tail, and
check global normal injectivity. No production metric is changed here.
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
from scipy.special import ellipe

HERE=Path(__file__).resolve().parent
_sp=importlib.util.spec_from_file_location('fd2d_controlled',HERE/'fd2d_controlled_ellipse_flow.py')
ctl=importlib.util.module_from_spec(_sp);_sp.loader.exec_module(ctl)


class CurvatureFlow(ctl.ControlledFlow):
    def __init__(self,control,*args,K=7.1,tracking=20.,**kwargs):
        super().__init__(control,*args,**kwargs)
        self.K=K;self.tracking=tracking

    def frame(self,s,flat):
        X=np.asarray(flat)[:-2].reshape(self.nodes,3);u,aa=map(float,flat[-2:])
        xp,xpp=self.derivative(X),self.derivative(X,2)
        ell=np.linalg.norm(xp,axis=1);T=xp/ell[:,None]
        c=xpp-np.sum(xpp*T,axis=1)[:,None]*T;clen=np.linalg.norm(c,axis=1)
        kappa=clen/ell**2;N=c/clen[:,None];B=np.cross(T,N)
        selected=kappa[self.nodes//4];vv=u*aa*selected
        alpha=-u*selected/kappa;chart=1-alpha**2;beta=np.sqrt(np.maximum(chart,1e-14))
        V=alpha[:,None]*N+beta[:,None]*B
        f=dict(X=X,xp=xp,xpp=xpp,ell=ell,T=T,N=N,B=B,kappa=kappa,aa=aa,vv=vv,
               alpha=alpha,beta=beta,chart=chart,V=V,u=u,selected=selected)
        vp,vpp=self.derivative(V),self.derivative(V,2)
        ell_s=np.sum(T*vp,axis=1);Ts=(vp-ell_s[:,None]*T)/ell[:,None]
        xt=np.sum(xpp*T,axis=1)
        cs=vpp-(np.sum(vpp*T,axis=1)+np.sum(xpp*Ts,axis=1))[:,None]*T-xt[:,None]*Ts
        ksvec=cs/ell[:,None]**2-2*(ell_s/ell)[:,None]*(kappa[:,None]*N)
        ks=np.sum(N*ksvec,axis=1);Ns=(ksvec-ks[:,None]*N)/kappa[:,None]
        Bs=np.cross(Ts,N)+np.cross(T,Ns)
        selected_s=ks[self.nodes//4]
        alpha_s0=-u*(selected_s/kappa-selected*ks/kappa**2)
        common=N-(alpha/beta)[:,None]*B
        Xss0=alpha_s0[:,None]*common+alpha[:,None]*Ns+beta[:,None]*Bs
        normal=np.cross(T,V);normal/=np.linalg.norm(normal,axis=1)[:,None]
        L0=np.sum(normal*Xss0,axis=1)
        mixed=np.sum(normal*vp,axis=1)/ell
        angular=np.sum(normal*xpp,axis=1)/ell**2
        coefficient=selected/(kappa*beta)
        K=self.K
        if np.max(abs(angular))>=K:
            lo,hi=1.,-1.
        else:
            lo=float(np.max((-K+mixed*mixed/(K+angular)-L0)/coefficient))
            hi=float(np.min((K-mixed*mixed/(K-angular)-L0)/coefficient))
        desired_control=self.control.jet(s)[0]
        desired_control*=min(1.,float(kappa.min()/selected))
        desired_rate=self.tracking*(desired_control-u)
        mid=(hi+lo)/2;half=max(0.,(hi-lo)/2)
        rate=mid+half*math.tanh((desired_rate-mid)/half) if half>1e-14 else mid
        acc=rate*aa*selected+u*vv*selected+u*aa*selected_s
        f.update(up=rate,acc=acc,rate_lower=lo,rate_upper=hi,
                 rate_feasibility=min(hi-lo,K-float(abs(angular).max())),
                 requested_control=desired_control,selected_s=selected_s)
        return f

    def rhs(self,s,y):
        self.calls+=1
        if self.calls>self.max_calls:raise RuntimeError('Finite diagnostic RHS-call limit; no complete endpoint.')
        f=self.frame(s,y)
        return np.r_[f['V'].ravel(),f['up'],f['vv']]

    def acceleration(self,f,ks):return f['acc']

    def diagnostics(self,s,y):
        out=super().diagnostics(s,y);f=self.frame(s,y)
        horizontal=f['X'][:,0]**2+(f['X'][:,1]-1.4)**2
        mask=horizontal<.9**2
        shift=float(np.max(np.sqrt(.9**2-horizontal[mask])-f['X'][mask,2])) if np.any(mask) else None
        out.update(control=f['u'],control_rate=f['up'],requested_control=f['requested_control'],
                   radial_acceleration=f['acc'],curvature_rate_feasibility=f['rate_feasibility'],
                   held_required_upward_shift=shift)
        return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--nodes',type=int,default=128)
    p.add_argument('--umax',type=float,default=.85);p.add_argument('--ramp',type=float,default=.3)
    p.add_argument('--hold',type=float,default=0.);p.add_argument('--turn',type=float,default=.4)
    p.add_argument('--finish',type=float,default=.35);p.add_argument('--lead',type=float,default=.2)
    p.add_argument('--K',type=float,default=7.1);p.add_argument('--tracking',type=float,default=20.)
    p.add_argument('--B',type=float,default=.45,help='Exact ellipse short semiaxis; long semiaxis remains 1.4.')
    p.add_argument('--max-calls',type=int,default=18000)
    p.add_argument('--continue-past-position-gates',action='store_true',
                   help='Design only: finish the same geometric trajectory to measure the required cylinder lead.')
    args=p.parse_args();control=ctl.Control(args.umax,args.ramp,args.hold,args.turn,args.finish,args.lead)
    a0=2*1.4*float(ellipe(1-(args.B/1.4)**2))/math.pi
    flow=CurvatureFlow(control,args.nodes,1.4,args.B,a0,args.max_calls,K=args.K,tracking=args.tracking)
    y=np.r_[flow.initial.ravel(),0.,flow.a0]
    def chart_event(s,y):return float(flow.frame(s,y)['chart'].min())-1e-4
    def metric_event(s,y):return 2e-5-flow.metric_error(s,y)
    def rate_event(s,y):return flow.frame(s,y)['rate_feasibility']
    def slab_event(s,y):return .75-float(abs(np.asarray(y)[:-2].reshape(args.nodes,3)[:,1]).max())
    def height_event(s,y):return 1.2886410585615193-float(abs(np.asarray(y)[:-2].reshape(args.nodes,3)[:,2]).max())
    def held_event(s,y):return float(np.linalg.norm(np.asarray(y)[:-2].reshape(args.nodes,3)-np.array([0.,1.4,0.]),axis=1).min())-.9
    events=[chart_event,metric_event,rate_event,slab_event,height_event,held_event]
    names=['chart','metric','curvature_rate','slab','height','held']
    if args.continue_past_position_gates:
        events=[chart_event,metric_event,rate_event,slab_event]
        names=['chart','metric','curvature_rate','slab']
    for e in events:e.terminal=True;e.direction=-1
    report=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                control=control.rows,nodes=args.nodes,ellipse_A=1.4,ellipse_B=args.B,metric_a0=a0,
                sampled_curvature_budget=args.K,
                tracking=args.tracking,position_gates_active=not args.continue_past_position_gates,
                initial=flow.diagnostics(0.,y),
                complete_control=False,closed_surface=False,metric_frozen=False,rows=[],metric_knots=[])
    try:
        for j,part in enumerate(control.rows):
            sol=solve_ivp(flow.rhs,(part['s0'],part['s1']),y,method='DOP853',
                          rtol=2e-10,atol=2e-12,max_step=.002,t_eval=np.linspace(part['s0'],part['s1'],41),
                          events=events)
            rec=[flow.diagnostics(s,z) for s,z in zip(sol.t,sol.y.T)]
            if sol.status==1:
                for ts,zs in zip(sol.t_events,sol.y_events):
                    if len(ts):rec.append(flow.diagnostics(ts[-1],zs[-1]))
            report['metric_knots'].extend([{k:r[k] for k in ('s','radius','radial_speed','radial_acceleration')} for r in rec])
            shifts=[r['held_required_upward_shift'] for r in rec if r['held_required_upward_shift'] is not None]
            if shifts:
                report['sampled_additional_lead_required']=max(report.get('sampled_additional_lead_required',0.),max(shifts))
            row=dict(index=j,status=sol.status,message=sol.message,
                events={name:ts.tolist() for name,ts in zip(names,sol.t_events)},last=rec[-1] if rec else None,
                extrema={key:(min(r[key] for r in rec) if 'min' in key or 'feasibility' in key else max(r[key] for r in rec))
                    for key in ('minimum_chart','metric_angular_error','sampled_curvature_max',
                                'sampled_support_min','maximum_radius','maximum_abs_z','maximum_abs_y',
                                'held_witness_min_distance','curvature_rate_feasibility')})
            report['rows'].append(row);args.out.write_text(json.dumps(report,indent=2)+'\n')
            print(json.dumps(row),flush=True)
            if sol.status!=0:break
            y=sol.y[:,-1]
        else:report['complete_control']=True
    except Exception as exc:report['failure']=str(exc)
    report['rhs_calls']=flow.calls;args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(event='complete',complete_control=report['complete_control'],
                         rhs_calls=flow.calls,failure=report.get('failure'))))


if __name__=='__main__':main()
