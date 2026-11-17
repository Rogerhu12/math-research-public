import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
import sys,json,math,copy
import numpy as np
from scipy.optimize import brentq
from even_mode_loader import load,module,TRANSFORMS
b=Path('/workspace/scratch/f00f08c94d46');r=b/'even_plateau_work';source=b/'m3_flat17_work/recovered/bundle/topics/visible-flexible-closed-surface';comp=b/'m3_flat17_work/recovered/bundle/topics/visible-flex-larger-amplitude/computations'
ad=load(source,4);short=module('even_short_bridge',comp/'root_short_bridge.py');short.install()
port=json.loads((r/'mode4_port8.json').read_text());rows=[]
for vu,vd in [(.17,.18),(.25,.3),(.25,.5),(.3,.5),(.35,.5),(.35,.6),(.4,.6)]:
 cfg=dict(direction='outward',vu=vu,vd=vd,delta=.035,ramp=.4,ramp_eta=.05,ramp_law='flat',cycles=1,prefix_bridge=dict(kind='turn_plateau_v1',curvature=4.,peak_fraction=.2));p=copy.deepcopy(port);p['cut']['_prefix_bridge']=cfg['prefix_bridge'];Flow,_=ad.build_classes(dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.));cache={}
 def make(x):return Flow({**cfg,'delta':float(x)},p,4,.005,128,4,warp_q=.005)
 def f(x):
  if x not in cache:cache[x]=float(make(x).backward_line().core[1])
  return cache[x]
 try:
  samples=[(x,f(x))for x in [.003,.006,.01,.015,.02,.03,.045,.065,.09,.13]]
  brackets=[(x,y)for (x,u),(y,v)in zip(samples,samples[1:])if u*v<0]
  if not brackets:raise ValueError('No bracket')
  lo,hi=min(brackets,key=lambda z:abs(.5*sum(z)-.035));delta=brentq(f,lo,hi,xtol=2e-12);cfg['delta']=delta;flow=make(delta);line=flow.backward_line();line_end=np.asarray(line.evaluate(flow.end)) if hasattr(line,'evaluate') else None
  x=np.linspace(0,1,65);ss=x*flow.end;fg=np.empty((2,len(ss)))
  for j,(s0,s1,sol,scale)in enumerate(line.segments):
   mask=(ss>=s0)&((ss<s1)if j+1<len(line.segments)else(ss<=s1))
   if np.any(mask):fg[:,mask]=sol(ss[mask])*math.exp(scale-line.logscale)/line.core[0]
  ar,ap,_=flow.profile(ss);h=fg[0]/ar;rhs=flow.linear_rhs(flow.end,fg[:,-1]);hp=(rhs[0]*ar[-1]-fg[0,-1]*ap[-1])/ar[-1]**2*flow.end
  chart=dict(knots=x.tolist(),values=h.tolist(),final_derivative=float(hp),reference_profile=cfg)
  s=np.unique(np.r_[np.linspace(0,flow.end,2049),flow.breaks]);a,v,k=flow.profile(s);co=np.sqrt(1-v*v)
  rec=dict(vu=vu,vd=vd,delta=delta,background_height=float(np.trapezoid(co,s)),background_curvature=float(np.max(abs(k)/co)),background_r_max=float(a.max()),linear_H_per_q=float(fg[1,-1]),next_transversality=float(flow.backward_line(1).core[1]),end=flow.end,success=True)
  dest=r/f'vu{round(100*vu):02d}-vd{round(100*vd):02d}';dest.mkdir(exist_ok=True);(dest/'profile.json').write_text(json.dumps(cfg,indent=2)+'\n');(dest/'chart.json').write_text(json.dumps(chart,indent=2)+'\n');rec['directory']=str(dest)
 except Exception as e:rec=dict(vu=vu,vd=vd,success=False,error=repr(e))
 rows.append(rec);print(json.dumps(rec),flush=True);(r/'linear_even_screen.json').write_text(json.dumps(dict(scope='Linear finite port design only, new mode4 source transformations',rows=rows,source_transforms=TRANSFORMS),indent=2)+'\n')
