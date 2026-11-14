#!/usr/bin/env python3
"""Choose a new radial metric with actual-curvature feedback, finite IVP screen.

The exact formal construction uses a'=u(s)*a*kappa(s,theta=pi/2), with a fixed
C1 control u. The Frenet equation then preserves ds^2+(a/a0)^2*ell0(theta)^2
dtheta^2 while its positive-binormal chart exists. Numerical records below do
not prove continuum existence, all-time geometry, a tail match, or closure.
The feedback defines a new metric; it is not a refinement of a production g.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

HERE=Path(__file__).resolve().parent
_sp=importlib.util.spec_from_file_location('fd2d_nonlinear_flow',HERE/'fd2d_frenet_ivp_screen.py')
base=importlib.util.module_from_spec(_sp);_sp.loader.exec_module(base)


class Control:
    def __init__(self,umax=.8,ramp=.25,hold=.1,turn=.4,finish=.65,lead=0.):
        self.rows=[];s=0.
        for length,u0,u1 in [(lead,0.,0.),(ramp,0.,umax),(hold,umax,umax),
                              (turn,umax,-umax),(finish,-umax,-umax)]:
            if length<=1e-14:continue
            self.rows.append(dict(s0=s,s1=s+length,L=length,u0=u0,u1=u1));s+=length
        self.end=s

    def jet(self,s):
        row=next((r for r in self.rows if s<r['s1']-1e-14),self.rows[-1])
        x=np.clip((s-row['s0'])/row['L'],0.,1.)
        return (row['u0']+(row['u1']-row['u0'])*x*x*(3-2*x),
                (row['u1']-row['u0'])*6*x*(1-x)/row['L'])


class ControlledFlow(base.Flow):
    def __init__(self,control,*args,**kwargs):
        super().__init__(None,*args,**kwargs)
        self.control=control

    def frame(self,s,flat):
        X=np.asarray(flat)[:-1].reshape(self.nodes,3);aa=float(flat[-1])
        xp,xpp=self.derivative(X),self.derivative(X,2)
        ell=np.linalg.norm(xp,axis=1);T=xp/ell[:,None]
        c=xpp-np.sum(xpp*T,axis=1)[:,None]*T;clen=np.linalg.norm(c,axis=1)
        kappa=clen/ell**2;N=c/clen[:,None];B=np.cross(T,N)
        u,up=self.control.jet(s);selected=kappa[self.nodes//4]
        vv=u*aa*selected
        alpha=-u*selected/kappa;chart=1-alpha**2;beta=np.sqrt(np.maximum(chart,1e-14))
        V=alpha[:,None]*N+beta[:,None]*B
        return dict(X=X,xp=xp,xpp=xpp,ell=ell,T=T,N=N,B=B,kappa=kappa,
                    aa=aa,vv=vv,acc=None,alpha=alpha,beta=beta,chart=chart,V=V,u=u,up=up,
                    selected=selected)

    def acceleration(self,f,ks):
        return f['up']*f['aa']*f['selected']+f['u']*f['vv']*f['selected']+f['u']*f['aa']*ks[self.nodes//4]

    def rhs(self,s,y):
        self.calls+=1
        if self.calls>self.max_calls:raise RuntimeError('Finite diagnostic RHS-call limit; no complete endpoint.')
        f=self.frame(s,y)
        return np.r_[f['V'].ravel(),f['vv']]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--nodes',type=int,default=64)
    p.add_argument('--umax',type=float,default=.8);p.add_argument('--ramp',type=float,default=.25)
    p.add_argument('--hold',type=float,default=.1);p.add_argument('--turn',type=float,default=.4)
    p.add_argument('--finish',type=float,default=.65);p.add_argument('--max-calls',type=int,default=12000)
    p.add_argument('--lead',type=float,default=0.)
    args=p.parse_args();control=Control(args.umax,args.ramp,args.hold,args.turn,args.finish,args.lead)
    flow=ControlledFlow(control,args.nodes,1.4,.45,.9870588543320401,args.max_calls)
    y=np.r_[flow.initial.ravel(),flow.a0]
    def chart_event(s,y):return float(flow.frame(s,y)['chart'].min())-1e-4
    def metric_event(s,y):return 2e-5-flow.metric_error(s,y)
    def slab_event(s,y):return .75-float(abs(np.asarray(y)[:-1].reshape(args.nodes,3)[:,1]).max())
    def height_event(s,y):return 1.2886410585615193-float(abs(np.asarray(y)[:-1].reshape(args.nodes,3)[:,2]).max())
    for e in (chart_event,metric_event,slab_event,height_event):e.terminal=True;e.direction=-1
    report=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                control=control.rows,nodes=args.nodes,initial=flow.diagnostics(0.,y),
                complete_control=False,closed_surface=False,rows=[])
    try:
        for j,part in enumerate(control.rows):
            sol=solve_ivp(flow.rhs,(part['s0'],part['s1']),y,method='DOP853',
                          rtol=2e-10,atol=2e-12,max_step=.002,t_eval=np.linspace(part['s0'],part['s1'],41),
                          events=[chart_event,metric_event,slab_event,height_event])
            rec=[flow.diagnostics(s,z) for s,z in zip(sol.t,sol.y.T)]
            if sol.status==1:
                for ts,zs in zip(sol.t_events,sol.y_events):
                    if len(ts):rec.append(flow.diagnostics(ts[-1],zs[-1]))
            row=dict(index=j,status=sol.status,message=sol.message,
                events={name:ts.tolist() for name,ts in zip(('chart','metric','slab','height'),sol.t_events)},
                last=rec[-1] if rec else None,
                extrema={key:(min(r[key] for r in rec) if 'min' in key else max(r[key] for r in rec))
                    for key in ('minimum_chart','metric_angular_error','sampled_curvature_max',
                                'sampled_support_min','maximum_radius','maximum_abs_z','maximum_abs_y',
                                'held_witness_min_distance')})
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
