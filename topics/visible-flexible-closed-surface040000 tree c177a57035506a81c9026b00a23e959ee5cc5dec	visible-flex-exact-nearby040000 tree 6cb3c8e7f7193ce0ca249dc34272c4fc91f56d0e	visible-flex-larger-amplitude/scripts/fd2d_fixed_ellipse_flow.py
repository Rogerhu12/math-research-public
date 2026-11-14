#!/usr/bin/env python3
"""Actual projected Frenet IVP on one frozen elliptic candidate metric.

The candidate JSON is read, hashed, and never modified. E, F, G and curvature
are computed from the actual projected velocity, not from formal identities.
The finite event screen is not a continuous error certificate or a BVP solve.
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

HERE=Path(__file__).resolve().parent
def module(name,file):
    sp=importlib.util.spec_from_file_location(name,HERE/file)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
fm=module('fd2d_frozen','fd2d_frozen_ellipse_candidate.py')
gf=module('fd2d_galerkin','fd2d_galerkin_ellipse_flow.py')


class FixedFlow(gf.ProjectedFlow):
    def __init__(self,candidate,nodes=256,oversample=2,max_calls=30000):
        self.candidate=candidate
        super().__init__(None,nodes,oversample,candidate.ellipse.A,candidate.ellipse.B,
                         7.1,0.,max_calls,36.,16,True)

    def frame(self,s,y):
        if s==self.cache_s and self.cache_y is not None and np.array_equal(y,self.cache_y):return self.cache_f
        X=resample(np.asarray(y).reshape(self.nodes,3),self.work,axis=0)
        aa,vv,acc=[float(v[0]) for v in self.candidate.profile([s])]
        xp,xpp=self.derivative(X),self.derivative(X,2)
        ell=np.linalg.norm(xp,axis=1);T=xp/ell[:,None]
        c=xpp-np.sum(xpp*T,axis=1)[:,None]*T;clen=np.linalg.norm(c,axis=1)
        kappa=clen/ell**2;N=c/clen[:,None];B=np.cross(T,N)
        alpha=-vv/(aa*kappa);chart=1-alpha**2;beta=np.sqrt(np.maximum(chart,1e-14))
        Vraw=alpha[:,None]*N+beta[:,None]*B
        Vcoarse,V=self.project(Vraw);vp,vpp=self.derivative(V),self.derivative(V,2)
        ell_s=np.sum(T*vp,axis=1);Ts=(vp-ell_s[:,None]*T)/ell[:,None]
        xt=np.sum(xpp*T,axis=1)
        cs=vpp-(np.sum(vpp*T,axis=1)+np.sum(xpp*Ts,axis=1))[:,None]*T-xt[:,None]*Ts
        ksvec=cs/ell[:,None]**2-2*(ell_s/ell)[:,None]*(kappa[:,None]*N)
        ks=np.sum(N*ksvec,axis=1);Ns=(ksvec-ks[:,None]*N)/kappa[:,None]
        Bs=np.cross(Ts,N)+np.cross(T,Ns)
        alphas=-acc/(aa*kappa)+vv*vv/(aa*aa*kappa)+vv*ks/(aa*kappa*kappa)
        _,Xss=self.project(alphas[:,None]*(N-(alpha/beta)[:,None]*B)+alpha[:,None]*Ns+beta[:,None]*Bs)
        normal=np.cross(xp,V);normal/=np.linalg.norm(normal,axis=1)[:,None]
        EE=np.sum(V*V,axis=1);FF=np.sum(V*xp,axis=1);GG=ell**2
        LL=np.sum(normal*Xss,axis=1);MM=np.sum(normal*vp,axis=1);NN=np.sum(normal*xpp,axis=1)
        detI=EE*GG-FF*FF;tr=(GG*LL-2*FF*MM+EE*NN)/detI;det=(LL*NN-MM*MM)/detI
        curv=abs(tr)/2+np.sqrt(np.maximum(tr*tr/4-det,0.))
        target_ell=aa/self.a0*self.initial_speed
        de=EE-1;df=FF/target_ell;dg=GG/target_ell**2-1
        metric=abs(de+dg)/2+np.hypot((de-dg)/2,df)
        delta=Vraw-V
        f=dict(X=X,V=V,Vcoarse=Vcoarse,aa=aa,vv=vv,acc=acc,chart=chart,curvature=curv,
            normal=normal,metric_error=float(metric.max()),angular_error=float(abs(dg).max()),
            E_error=float(abs(de).max()),F_error=float(abs(df).max()),
            velocity_projection_error=float(np.linalg.norm(delta,axis=1).max()))
        self.cache_s=s;self.cache_y=np.array(y,copy=True);self.cache_f=f
        return f

    def rhs(self,s,y):
        self.calls+=1
        if self.calls>self.max_calls:raise RuntimeError('Finite frozen-metric RHS-call limit')
        return self.frame(s,y)['Vcoarse'].ravel()

    def diagnostics(self,s,y):
        f=self.frame(s,y);X=f['X']
        return dict(s=float(s),radius=f['aa'],radial_speed=f['vv'],radial_acceleration=f['acc'],
            minimum_chart=float(f['chart'].min()),relative_metric_error=f['metric_error'],
            metric_angular_error=f['angular_error'],metric_E_error=f['E_error'],metric_F_error=f['F_error'],
            sampled_curvature_max=float(f['curvature'].max()),
            maximum_radius=float(np.linalg.norm(X,axis=1).max()),maximum_abs_z=float(abs(X[:,2]).max()),
            maximum_abs_y=float(abs(X[:,1]).max()),
            held_witness_min_distance=float(np.linalg.norm(X-np.array([0.,self.A,0.]),axis=1).min()),
            velocity_projection_error=f['velocity_projection_error'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--checkpoint',type=Path);p.add_argument('--nodes',type=int,default=256)
    p.add_argument('--oversample',type=int,default=2);p.add_argument('--max-calls',type=int,default=30000)
    p.add_argument('--stop-at',type=float)
    args=p.parse_args();bundle=json.loads(args.candidate.read_text());candidate=fm.Candidate(bundle)
    flow=FixedFlow(candidate,args.nodes,args.oversample,args.max_calls);y=flow.initial.ravel()
    end=min(candidate.end,args.stop_at) if args.stop_at is not None else candidate.end
    def chart(s,y):return float(flow.frame(s,y)['chart'].min())-1e-4
    def metric(s,y):return 2e-5-flow.frame(s,y)['metric_error']
    def curvature(s,y):return 1/.136-float(flow.frame(s,y)['curvature'].max())
    def slab(s,y):return .75-float(abs(flow.frame(s,y)['X'][:,1]).max())
    def height(s,y):return 1.2886410585615193-float(abs(flow.frame(s,y)['X'][:,2]).max())
    events=[chart,metric,curvature,slab,height];names=['chart','metric','curvature','slab','height']
    for e in events:e.terminal=True;e.direction=-1
    report=dict(scope=__doc__,candidate=args.candidate.name,candidate_sha256=fm.digest(args.candidate),
        source_sha256=fm.digest(__file__),provider_sha256=fm.digest(HERE/'fd2d_frozen_ellipse_candidate.py'),
        nodes=args.nodes,geometry_grid=flow.work,metric_frozen=True,closed_surface=False,
        reaches_requested_endpoint=False,initial=flow.diagnostics(0.,y),rows=[])
    last_s=0.
    try:
        for j,seg in enumerate(candidate.segments):
            if seg['s0']>=end-1e-14:break
            right=min(seg['s1'],end)
            sol=solve_ivp(flow.rhs,(seg['s0'],right),y,method='DOP853',rtol=2e-10,atol=2e-12,
                max_step=.002,t_eval=np.linspace(seg['s0'],right,5),events=events)
            rec=[flow.diagnostics(s,z) for s,z in zip(sol.t,sol.y.T)]
            last_s=float(sol.t[-1]);y=sol.y[:,-1]
            if sol.status==1:
                for ts,zs in zip(sol.t_events,sol.y_events):
                    if len(ts):last_s=float(ts[-1]);y=zs[-1];rec.append(flow.diagnostics(last_s,y))
            row=dict(index=j,segment_kind=seg['kind'],segment_label=seg.get('label'),status=sol.status,
                events={name:ts.tolist() for name,ts in zip(names,sol.t_events)},last=rec[-1],
                extrema={key:(min(r[key] for r in rec) if 'min' in key else max(r[key] for r in rec))
                    for key in ('minimum_chart','relative_metric_error','metric_angular_error','metric_E_error',
                        'metric_F_error','sampled_curvature_max','maximum_radius','maximum_abs_z','maximum_abs_y',
                        'held_witness_min_distance','velocity_projection_error')})
            report['rows'].append(row);args.out.write_text(json.dumps(report,indent=2)+'\n')
            if args.checkpoint:np.savez_compressed(args.checkpoint,state=y,s=last_s,candidate_sha256=report['candidate_sha256'])
            if sol.status!=0:print(json.dumps(row),flush=True);break
        report['reaches_requested_endpoint']=abs(last_s-end)<1e-12
    except Exception as exc:report['failure']=str(exc)
    report['rhs_calls']=flow.calls;report['last_s']=last_s
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report.get(k) for k in ('reaches_requested_endpoint','rhs_calls','last_s','failure')}),flush=True)


if __name__=='__main__':main()
