"""Re-match a short linear prefix to the supplied tail's own mode-two DN."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,importlib.util,json,math
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--bundle',type=Path,required=True);p.add_argument('--diagnostic',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
C=a.bundle/'bundle/topics/visible-flex-larger-amplitude/computations';S=a.bundle/'bundle/topics/visible-flexible-closed-surface'
spec=importlib.util.spec_from_file_location('held10_coupled_linear',C/'numerical-m2-prefix.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);ad=mod.load(S);short=mod.source_module('held10_short',C/'root_short_bridge.py');short.install()
Flow,_=ad.build_classes(dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.))
d=json.loads(a.diagnostic.read_text());cfg=d['config'];r=cfg['rCut'];w=cfg['wCut'];D=d['linear']['cutSlope']
port=json.loads((C/'numerical-m2-port24.json').read_text());port['cut']=dict(radius=r,backgroundSlope=w,backgroundSecond=-7*w/r,E=1+w*w,Ep=-14*w*w/r);port['linearSlope']=[D]+port['linearSlope'][1:]
profile=dict(direction='outward',vu=.55,vd=.6,ramp=.4,cycles=1,cut_radius=r,cut_slope=w,ramp_law='flat',ramp_eta=.05)
if r<.4:
 profile['prefix_bridge']=dict(kind='turn_plateau_v1',curvature=4.,peak_fraction=.5);port['cut']['_prefix_bridge']=profile['prefix_bridge']
def make(delta):return Flow({**profile,'delta':float(delta)},port,1,.001,32,2)
def target(delta):return make(delta).backward_line().core[1]
delta=brentq(target,.10,.24,xtol=2e-12);flow=make(delta);line=flow.backward_line();gain=line.terminal[1]*math.exp(-line.logscale)/line.core[0]
z,g=np.polynomial.legendre.leggauss(16);height=0.
for lo,hi in zip(flow.breaks[:-1],flow.breaks[1:]):
 _,v,_=flow.profile((lo+hi)/2+(hi-lo)*z/2);height+=(hi-lo)/2*float(g@np.sqrt(1-v*v))
result=dict(scope='First-mode linear tail diagnostic divided by the newly matched linear core-to-tail gain. Not a nonlinear upper bound, finite-q solution, fixed-g refinement or closed surface.',profile=profile|dict(delta=delta),tail_D2=D,tail_height=d['stats']['heightSpan'],tail_linear_T_threshold=d['linear']['linearTPositivityAmplitudeThreshold'],terminal_height_over_core_support=gain,prefix_background_height=height,core_normalized_linear_gate=d['linear']['linearTPositivityAmplitudeThreshold']/abs(gain))
a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
