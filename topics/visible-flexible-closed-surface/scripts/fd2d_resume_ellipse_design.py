#!/usr/bin/env python3
"""Continue a saved actual elliptic prefix with curvature-limited metric design.

This extension selects NEW a(s). It is not a same-g refinement past the saved
interface and not a nonlinear tail match. The initial scalar control is chosen
to reproduce the frozen prefix's a,a',a'' at that interface. A later complete
candidate must freeze the resulting shared jets and be solved at that one g.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,json,math,importlib.util
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

HERE=Path(__file__).resolve().parent
def module(name,path):
    sp=importlib.util.spec_from_file_location(name,HERE/path)
    obj=importlib.util.module_from_spec(sp);sp.loader.exec_module(obj);return obj
fm=module('fd2d_frozen_resume','fd2d_frozen_ellipse_candidate.py')
gf=module('fd2d_galerkin_resume','fd2d_galerkin_ellipse_flow.py')


class ResumeControl:
    def __init__(self,start,blend,finish,target):
        self.start=start;self.blend=blend;self.end=start+blend+finish
        self.initial_target=0.;self.target=target
    def jet(self,s):
        t=float(np.clip((s-self.start)/self.blend,0.,1.))
        return (self.initial_target+(self.target-self.initial_target)*t*t*(3-2*t),
                (self.target-self.initial_target)*6*t*(1-t)/self.blend)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate',type=Path,required=True);p.add_argument('--state',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--checkpoint',type=Path,required=True)
    p.add_argument('--target',type=float,default=-.85);p.add_argument('--blend',type=float,default=.06)
    p.add_argument('--finish',type=float,default=1.);p.add_argument('--stop-radius',type=float,default=.45)
    p.add_argument('--K',type=float,default=7.1);p.add_argument('--tracking',type=float,default=20.)
    p.add_argument('--max-calls',type=int,default=40000)
    args=p.parse_args();candidate=fm.Candidate(json.loads(args.candidate.read_text()))
    saved=np.load(args.state);start=float(saved['s']);state=np.asarray(saved['state'],dtype=float)
    if state.size%3:raise ValueError('Expected the XYZ-only checkpoint of fd2d_fixed_ellipse_flow.py')
    if str(saved['candidate_sha256'])!=fm.digest(args.candidate):raise ValueError('Frozen candidate hash mismatch')
    nodes=state.size//3;control=ResumeControl(start,args.blend,args.finish,args.target)
    flow=gf.ProjectedFlow(control,nodes,2,candidate.ellipse.A,candidate.ellipse.B,
                          args.K,args.tracking,args.max_calls,36.,16,True)
    X=gf.resample(state.reshape(nodes,3),flow.work,axis=0)
    xp=flow.derivative(X);xpp=flow.derivative(X,2)
    ell=np.linalg.norm(xp,axis=1);T=xp/ell[:,None]
    curv=np.linalg.norm(xpp-np.sum(xpp*T,axis=1)[:,None]*T,axis=1)/ell**2
    aa,vv,acc=[float(a[0]) for a in candidate.profile([start])]
    selected=float(curv[flow.work//4]);u=vv/(aa*selected);y=np.r_[state,u,aa]
    def initial_frame(target):
        control.initial_target=target;flow.cache_s=None;return flow.frame(start,y)
    lo=initial_frame(-1e6);hi=initial_frame(1e6);lo_rate=lo['up'];hi_rate=hi['up']
    probe=initial_frame(0.);needed_rate=probe['up']+(acc-probe['acc'])/(aa*selected)
    if not lo_rate<needed_rate<hi_rate:raise ValueError('Frozen interface acceleration lies outside the current strict curvature interval')
    mid=(lo_rate+hi_rate)/2;half=(hi_rate-lo_rate)/2
    desired=mid+half*math.atanh((needed_rate-mid)/half)
    ratio=min(1.,float(curv.min()/selected))
    control.initial_target=(u+desired/args.tracking)/ratio
    flow.cache_s=None;initial=flow.diagnostics(start,y)
    report=dict(scope=__doc__,source_sha256=fm.digest(__file__),candidate_sha256=fm.digest(args.candidate),
        state_sha256=fm.digest(args.state),nodes=nodes,geometry_grid=flow.work,
        interface_s=start,interface_target_jet=[aa,vv,acc],initial=initial,
        initial_control_target=control.initial_target,goal=args.target,blend=args.blend,
        first_acceleration_mismatch=initial['radial_acceleration']-acc,
        metric_frozen_on_extension=False,complete_to_radius=False,closed_surface=False,rows=[],metric_knots=[])
    def chart(s,y):return float(flow.frame(s,y)['chart'].min())-1e-4
    def metric(s,y):return 2e-5-flow.frame(s,y)['metric_error']
    def rate(s,y):return flow.frame(s,y)['rate_feasibility']
    def slab(s,y):return .75-float(abs(flow.frame(s,y)['X'][:,1]).max())
    def height(s,y):return 1.2886410585615193-float(abs(flow.frame(s,y)['X'][:,2]).max())
    def radius(s,y):return float(y[-1])-args.stop_radius
    events=[chart,metric,rate,slab,height,radius];names=['chart','metric','curvature_rate','slab','height','radius']
    for e in events:e.terminal=True;e.direction=-1
    last_s=start;left=start
    try:
        for index,right in enumerate(np.r_[np.arange(start+.05,control.end,.05),control.end]):
            sol=solve_ivp(flow.rhs,(left,right),y,method='DOP853',rtol=2e-10,atol=2e-12,
                          max_step=.001,t_eval=np.linspace(left,right,11),events=events)
            rec=[flow.diagnostics(s,z) for s,z in zip(sol.t,sol.y.T)]
            last_s=float(sol.t[-1]);y=sol.y[:,-1]
            if sol.status==1:
                for ts,zs in zip(sol.t_events,sol.y_events):
                    if len(ts):last_s=float(ts[-1]);y=zs[-1];rec.append(flow.diagnostics(last_s,y))
            report['metric_knots'].extend([{k:r[k] for k in ('s','radius','radial_speed','radial_acceleration')} for r in rec])
            def extreme(key):
                values=[r[key] for r in rec if r[key] is not None]
                return (min(values) if 'min' in key or 'feasibility' in key else max(values)) if values else None
            row=dict(index=index,status=sol.status,last=rec[-1],events={name:ts.tolist() for name,ts in zip(names,sol.t_events)},
                extrema={key:extreme(key)
                    for key in ('minimum_chart','relative_metric_error','sampled_curvature_max','maximum_abs_y','maximum_abs_z',
                                'held_witness_min_distance','held_required_upward_shift','curvature_rate_feasibility')})
            report['rows'].append(row);args.out.write_text(json.dumps(report,indent=2)+'\n')
            np.savez_compressed(args.checkpoint,state=y,s=last_s,source_sha256=report['source_sha256'])
            print(json.dumps(row),flush=True)
            if sol.status!=0:
                report['complete_to_radius']=bool(len(sol.t_events[-1]));break
            left=right
    except Exception as exc:report['failure']=str(exc)
    report['rhs_calls']=flow.calls;report['last_s']=last_s
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report.get(k) for k in ('complete_to_radius','rhs_calls','last_s','failure')}),flush=True)


if __name__=='__main__':main()
