#!/usr/bin/env python3
"""Physical linear prefix for a planar m-fold support perturbation.

The circle radius profile is reused unchanged; only the perturbation frequency
is generalized. The inherited nonplanar-core reflection guard is not invoked
with mode3. This is a linear geometry screen, never a closed-surface result.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[k]='1'
import argparse,hashlib,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def install(ellipse_notes,source_root):
    sys.path.insert(0,str(ellipse_notes))
    sys.path.insert(0,str(source_root/'topics/large-amplitude-twist-flex/scripts'))
    from repo_scan_ellipse_line import CycleBridgeProfile
    from f6curve_outward_bridge_linear import BackwardLine
    class GeneralProfile(CycleBridgeProfile):
        def __init__(self,cfg,port):
            super().__init__(cfg,port)
            self.mode=int(port['linearModes'][0])
        def rhs(self,s,y):
            a,v,_=self.profile(np.array([s]));a=float(a[0]);v=float(v[0])
            b=math.sqrt(1-v*v);m2=self.mode**2
            return np.array([-(m2-1)*v*y[0]-m2*b*y[1],
                 (m2-1)*v*v*y[0]/b+m2*v*y[1]])/a
        def terminal(self):
            r=self.port['cut']['radius'];w=self.port['cut']['backgroundSlope']
            D=self.port['linearSlope'][0];m2=self.mode**2
            return np.array([self.bridge.sigma*w*(r*D-m2)/(m2-1),1.])
    def backward(cfg,port):
        profile=GeneralProfile(cfg,port)
        return profile,BackwardLine(profile.rhs,profile.breaks,profile.terminal())
    return backward


def describe(backward,cfg,port,q=.1,ell=.2):
    profile,line=backward(cfg,port)
    x=np.unique(np.concatenate([np.linspace(lo,hi,65) for lo,hi in zip(profile.breaks[:-1],profile.breaks[1:])]))
    r,v,acc=profile.profile(x);b=np.sqrt(1-v*v)
    height=float(np.trapezoid(b,x));k=float(np.max(np.maximum(abs(acc)/b,b/r)))
    gain=float(line.terminal[1]*math.exp(-line.logscale)/line.core[0])
    diameter=2*math.hypot(float(np.max(r))+q,height+ell+.03)
    m=port['linearModes'][0]
    return dict(config=cfg,mode=m,core_direction=line.core.tolist(),
      gain=gain,terminal_height_first_order=q*abs(gain),
      background_height=height,background_kappa=k,length=profile.end,
      radius_min=float(min(r)),radius_max=float(max(r)),
      comparison_D=diameter,comparison_hold_ratio=min(2*q,ell)/diameter,
      comparison_background_kappaD=max(k,1/(1-(m*m-1)*q))*diameter,
      comparison_is_not_a_nonlinear_bound=True)


def main():
    pa=argparse.ArgumentParser(description=__doc__)
    pa.add_argument('--source-root',type=Path,required=True)
    pa.add_argument('--ellipse-notes',type=Path,required=True)
    pa.add_argument('--linear-port',type=Path,required=True)
    pa.add_argument('--out',type=Path,required=True)
    pa.add_argument('--configs',type=Path)
    a=pa.parse_args();backward=install(a.ellipse_notes,a.source_root)
    d=json.loads(a.linear_port.read_text());r=d['config']['rCut'];w=d['config']['wCut']
    port={'cut':dict(radius=r,backgroundSlope=w,backgroundSecond=-7*w/r,E=1+w*w,Ep=-14*w*w/r),
          'linearSlope':[row['cutSlope'] for row in d['rows']],
          'linearModes':[row['mode'] for row in d['rows']]}
    threshold=d['rows'][0]['linearTPositivityAmplitudeThreshold']
    configs=json.loads(a.configs.read_text()) if a.configs else [
        dict(direction='outward',vu=u,vd=v,ramp=.4,cycles=n,cut_radius=r,cut_slope=w)
        for u,v in [(.25,.4),(.35,.5),(.5,.7)] for n in [1,2,3]]
    report=dict(scope=__doc__,input_sha256=hashlib.sha256(a.linear_port.read_bytes()).hexdigest(),
                port=port,tail_linear_T_threshold=threshold,rows=[])
    start=time.time()
    for cfg in configs:
        previous=None;roots=[];errors=[]
        for delta in cfg.get('deltas',[.01,.02,.035,.06,.1,.16,.24,.36,.54,.8]):
            try:
                current=float(backward({**cfg,'delta':delta},port)[1].core[1])
                if previous and previous[1]*current<0:
                    root=brentq(lambda t:float(backward({**cfg,'delta':t},port)[1].core[1]),previous[0],delta,xtol=2e-11)
                    row=describe(backward,{**cfg,'delta':root},port)
                    row['tail_threshold_ratio']=row['terminal_height_first_order']/threshold
                    roots.append(row)
                previous=(delta,current)
            except Exception as exc:
                errors.append({'delta':delta,'error':repr(exc)});previous=None
        report['rows'].append(dict(config=cfg,roots=roots,errors=errors))
        report['elapsed_seconds']=time.time()-start
        a.out.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(dict(config=cfg,roots=roots,errors=errors,elapsed_seconds=report['elapsed_seconds'])),flush=True)

if __name__=='__main__':main()
