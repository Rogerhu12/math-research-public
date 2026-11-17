import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
import json,math,numpy as np
from scipy.optimize import brentq
from scipy.integrate import cumulative_trapezoid,quad
from even_mode_loader import load,module,TRANSFORMS
r=Path(__file__).resolve().parent;root=r.parent;src=root/'m3_flat17_work/recovered/bundle/topics/visible-flexible-closed-surface';ad=load(src,4);module('short_compact_window',src.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py').install();port=json.load(open(r/'mode4_port8.json'));rows=[]
for vu,vd,eps in [(.3,.35,.4),(.35,.4,.4),(.4,.4,.4),(.4,.45,.4),(.45,.45,.4),(.35,.4,.45),(.4,.4,.45),(.4,.45,.45)]:
 cfg=dict(direction='outward',vu=vu,vd=vd,delta=.035,ramp=eps,ramp_eta=.05,ramp_law='flat',cycles=1,prefix_bridge=dict(kind='turn_plateau_v1',curvature=4.,peak_fraction=.2));p=json.loads(json.dumps(port));p['cut']['_prefix_bridge']=cfg['prefix_bridge'];Flow,_=ad.build_classes(dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.))
 def make(d):return Flow({**cfg,'delta':float(d)},p,4,.005,128,4,warp_q=.005)
 def fun(d):return float(make(d).backward_line().core[1])
 try:
  d=brentq(fun,.008,.09,xtol=2e-12);cfg['delta']=d;f=make(d);line=f.backward_line();x=np.linspace(0,1,65);ss=x*f.end;fg=np.empty((2,len(ss)))
  for j,(lo,hi,sol,scale)in enumerate(line.segments):
   mask=(ss>=lo)&((ss<hi)if j+1<len(line.segments)else(ss<=hi))
   if np.any(mask):fg[:,mask]=sol(ss[mask])*math.exp(scale-line.logscale)/line.core[0]
  a,v,_=f.profile(ss);h=fg[0]/a;rhs=f.linear_rhs(f.end,fg[:,-1]);hp=(rhs[0]*a[-1]-fg[0,-1]*v[-1])/a[-1]**2*f.end
  chart=dict(knots=x.tolist(),values=h.tolist(),final_derivative=float(hp),reference_profile=cfg)
  s=np.unique(np.r_[np.linspace(0,f.end,12001),f.breaks]);ar,av,acc=f.profile(s);co=np.sqrt(1-av*av);z=cumulative_trapezoid(co,s,initial=0);ball=np.sqrt(ar*ar+(z+.25)**2)
  R=.1
  def ch(u):
   aa,vv,kk=[float(v[0])for v in f.profile([u])];return math.sqrt(max(kk,0)/(aa*(1-R*R*vv*vv)))
  knots=sorted(set([0.,float(f.Tu)]+[float(v)for v in f.breaks if 0<v<f.Tu]));loss=sum(quad(ch,lo,hi,epsabs=1e-11)[0]for lo,hi in zip(knots,knots[1:]))
  rec=dict(success=True,parameters=cfg,background_height=float(z[-1]),sample_ball_radius_with_half_cylinder_025=float(ball.max()),sample_K=float(np.max(np.maximum(abs(acc)/co,co/ar))),circle_R=.1,characteristic_loss_div_R=loss,linear_H_per_q=float(fg[1,-1]),chart_range=[float(h.min()),float(h.max())],next_transversality=float(f.backward_line(1).core[1]))
  dest=r/f'compact-v{int(100*vu):02d}-{int(100*vd):02d}-r{int(100*eps):02d}';dest.mkdir(exist_ok=True);(dest/'profile.json').write_text(json.dumps(cfg,indent=2)+'\n');(dest/'chart.json').write_text(json.dumps(chart,indent=2)+'\n');rec['directory']=str(dest)
 except Exception as e:rec=dict(success=False,parameters=cfg,error=repr(e))
 rows.append(rec);print(json.dumps(rec),flush=True);(r/'compact_window_screen.json').write_text(json.dumps(dict(scope='Finite linear and sampled round-background diagnostics for the narrower n4 core; no nonlinear or closed claim.',rows=rows,source_transforms=TRANSFORMS),indent=2)+'\n')
