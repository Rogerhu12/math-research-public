#!/usr/bin/env python3
"""Find a physical m=2 stable line with planar initial data (f,g)=(1,0).

The planar elliptic cylinder changes the linear initial condition from the
old wavy curve's g/f<0 to g/f=0. This script adjusts a finite cycle excursion,
with all other controls fixed, and checks the resulting linear holonomy
independently by forward integration. No nonlinear elliptic collar is claimed.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


class CycleBridgeProfile:
    def __init__(self,cfg,port):
        from f6curve_outward_bvp import OutwardPrefix
        from f6curve_inward_bvp import InwardPrefix
        from f6curve_bidirectional_bridge import DirectionalBridge
        self.cfg=cfg
        self.port=port
        inward=cfg.get('direction','outward')=='inward'
        cls=InwardPrefix if inward else OutwardPrefix
        delta=cfg['delta']/(1-cfg['delta']) if inward else cfg['delta']
        self.prefix=cls(1,.01,delta,cfg['vu'],cfg['vd'],cfg['ramp'],
                        cfg['cycles'],128,2,compute_stable=False)
        self.prefix_end=self.prefix.end
        self.bridge=DirectionalBridge(port['cut'])
        self.end=self.prefix_end+self.bridge.L
        U,D=self.prefix.Tu,self.prefix.Td
        first,second=(D,U) if inward else (U,D)
        eps=cfg['ramp']
        self.breaks=np.unique(np.r_[np.concatenate([
            c*self.prefix.period+np.array([0,eps*first,(1-eps)*first,first,
            first+eps*second,first+(1-eps)*second,first+second])
            for c in range(cfg['cycles'])]),self.end])

    def profile(self,s):
        s=np.atleast_1d(s)
        a,v,acc=self.prefix.profile(np.minimum(s,self.prefix_end))
        mask=s>self.prefix_end
        if np.any(mask):
            a[mask],v[mask],acc[mask]=self.bridge.profile(s[mask]-self.prefix_end)
        return a,v,acc

    def rhs(self,s,y):
        a,v,_=self.profile(np.array([s]))
        a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
        return np.array([-3*v*y[0]-4*b*y[1],3*v*v*y[0]/b+4*v*y[1]])/a

    def terminal(self):
        r=self.port['cut']['radius'];w=self.port['cut']['backgroundSlope']
        D=self.port['linearSlope'][0]
        return np.array([self.bridge.sigma*w*(r*D-4)/3,1.])


def backward(cfg,port):
    from f6curve_outward_bridge_linear import BackwardLine
    profile=CycleBridgeProfile(cfg,port)
    line=BackwardLine(profile.rhs,profile.breaks,profile.terminal())
    return profile,line


def describe(cfg,port,verify=False):
    profile,line=backward(cfg,port)
    x=np.unique(np.concatenate([np.linspace(lo,hi,65)
        for lo,hi in zip(profile.breaks[:-1],profile.breaks[1:])]))
    a,v,acc=profile.profile(x)
    b=np.sqrt(1-v*v)
    row=dict(config=cfg,backward_core_unit=line.core.tolist(),
             rho=float(line.core[1]/line.core[0]),
             root_component=float(line.core[1]),
             physical_endpoint_gain=float(line.terminal[1]*math.exp(-line.logscale)/line.core[0]),
             logscale=line.logscale,meridian_length=profile.end,
             background_height=float(np.trapezoid(b,x)),
             background_radius_min=float(np.min(a)),background_radius_max=float(np.max(a)),
             background_kappa_max=float(np.max(np.maximum(abs(acc)/b,b/a))),
             bridge_length=profile.bridge.L,
             initial_up_speed=cfg['vu'],
             circle_initial_data_only=True,nonlinear_ellipse_verified=False)
    if verify:
        # Different solver and a fresh forward IVP, never a reused backward
        # dense solution, to detect a wrong eigenline/normalization.
        s=solve_ivp(profile.rhs,[0,profile.end],[1.,0.],method='RK45',
            rtol=2e-11,atol=2e-13,max_step=min(np.diff(profile.breaks))/10)
        u=s.y[:,-1];target=profile.terminal()
        determinant=u[0]*target[1]-u[1]*target[0]
        row['independent_linear_forward']=dict(method='RK45',success=bool(s.success),
            terminal=u.tolist(),target_line=target.tolist(),
            normalized_line_determinant=float(abs(determinant)/(np.linalg.norm(u)*np.linalg.norm(target))),
            initial_data=[1.,0.],calls=s.nfev)
    return row


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--configs',type=Path)
    args=parser.parse_args()
    sys.path.insert(0,str(args.source_root/'topics/large-amplitude-twist-flex/scripts'))
    from f6curve_outward_bridge_linear import read_port
    from repo_scan_gentle import scaled_port,finite_value
    src=read_port(args.source_root/'topics/large-amplitude-twist-flex/notes/f6curve_wide_m2_r2_m16_linear_port.json')
    configs=json.loads(args.configs.read_text()) if args.configs else [
        dict(direction='outward',vu=u,vd=v,ramp=.4,cycles=1,cut_radius=.6,cut_slope=.5)
        for u,v in [(.25,.5),(.25,.8),(.25,.95),(.35,.5),(.35,.8),(.35,.95),(.5,.7),(.5,.9)]]
    report=dict(scope=__doc__,source_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                rows=[],roots=[],source_root=str(args.source_root))
    start=time.time()
    def save():
        report['elapsed_seconds']=time.time()-start
        with gzip.open(args.out,'wt',compresslevel=9) as h:
            json.dump(finite_value(report),h,indent=2,allow_nan=False);h.write('\n')
        summary=args.out.with_name(args.out.name.removesuffix('.json.gz')+'_summary.json')
        summary.write_text(json.dumps(finite_value(dict(scope=__doc__,
            coarse_samples=len(report['rows']),roots=report['roots'],
            elapsed_seconds=report['elapsed_seconds'])),indent=2,allow_nan=False)+'\n')
    for j,base in enumerate(configs):
        port=scaled_port(src,base['cut_radius'],base.get('cut_slope'),base.get('dimensionless_D'))
        deltas=base.get('deltas',[.06,.12,.22,.38,.6,.9,1.3])
        previous=None
        for delta in deltas:
            cfg={**base,'delta':delta}
            try:
                row=describe(cfg,port)
                report['rows'].append(row)
                current=(delta,row['root_component'])
                if previous and previous[1]*current[1]<0:
                    def fun(d):
                        return backward({**base,'delta':d},port)[1].core[1]
                    root=brentq(fun,previous[0],current[0],xtol=2e-11,rtol=1e-12)
                    found=describe({**base,'delta':float(root)},port,verify=True)
                    found['bracket']=[previous[0],current[0]]
                    found['port']=port
                    report['roots'].append(found)
                    print(json.dumps(finite_value(dict(event='root',config=found['config'],
                        rho=found['rho'],gain=found['physical_endpoint_gain'],
                        height=found['background_height'],length=found['meridian_length'],
                        kappa=found['background_kappa_max'],
                        verification=found['independent_linear_forward']['normalized_line_determinant']))),flush=True)
                previous=current
            except Exception as exc:
                report['rows'].append(dict(config=cfg,error=repr(exc)))
                previous=None
            save()
        print(json.dumps(dict(event='profile_finished',index=j+1,total=len(configs),
                              roots=len(report['roots']),seconds=round(time.time()-start,2))),flush=True)


if __name__=='__main__':
    main()
