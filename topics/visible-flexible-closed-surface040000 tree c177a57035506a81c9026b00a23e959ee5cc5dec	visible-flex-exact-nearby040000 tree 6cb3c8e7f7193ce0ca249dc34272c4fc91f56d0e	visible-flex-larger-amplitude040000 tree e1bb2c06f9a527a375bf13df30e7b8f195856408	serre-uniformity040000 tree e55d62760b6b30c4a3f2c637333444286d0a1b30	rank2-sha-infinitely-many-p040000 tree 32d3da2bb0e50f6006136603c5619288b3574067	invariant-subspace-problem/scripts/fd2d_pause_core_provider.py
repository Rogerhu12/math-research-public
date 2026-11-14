#!/usr/bin/env python3
"""One-pause C2 prefix provider for the NEW elliptic design's finite m2 port.

The numerical inlet proxy uses only the ellipse's mean radius and first
support coefficient; it is not the exact ellipse. This forward linear screen
is ill-conditioned near horizontal segments and is not nonlinear closure.
The actual XYZ initial-value diagnostic uses the exact ellipse separately.
The completed prefix segments can be reused as a fixed candidate metric, but
must be solved/refined at that same metric before any G5 conclusion.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import importlib.util,json,math,argparse,hashlib,numpy as np
from pathlib import Path
P=Path(__file__).resolve().parent.parent
s=importlib.util.spec_from_file_location('short',P/'scripts/fd2d_short_core_screen.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
m.load_port(P/'notes/2026-11-12-fd2d-ellipse-cuff032-cut04-port.json');m.CORE_RADIUS=.9870588543320401;m.CORE_AMPLITUDE=.458780797

def coast(dr,p):
 L=dr/math.sin(p) if abs(p)>1e-14 else 0
 if L < -1e-10:raise ValueError('negative coast')
 return dict(kind='coast',p0=p,p1=p,L=max(0,L),dr=dr,dh=max(0,L)*math.cos(p),K=0)
def stages(v0,rpause,K0,Kmid,pdeep,Kdeep,pause):
 pp=math.asin(v0)
 a=m.piece('turn',0,-pp,K0);b=m.piece('turn',-pp,0,Kmid)
 first=[a,coast(rpause-b['dr']-m.CORE_RADIUS-a['dr'],-pp),b]
 c=m.piece('turn',0,-pdeep,Kdeep);d=m.piece('brake',-pdeep,m.pt,m.ps)
 last=[c,coast(m.rc-d['dr']-rpause-c['dr'],-pdeep),d]
 return first+[dict(kind='coast',p0=0,p1=0,L=pause,dr=0,dh=pause,K=0)]+last

def trial(x):
 r0=m.evaluate_segments(stages(*x,0),True);r1=m.evaluate_segments(stages(*x,1),True)
 target=-m.wc*(m.rc*m.D[2]-4)/3
 def scalar(r):return r['cut'][0]['f']-target*r['cut'][0]['g']
 t=-scalar(r0)/(scalar(r1)-scalar(r0))
 if t<0:return dict(config=x,pause=t,invalid='negative required pause')
 r=m.evaluate_segments(stages(*x,t),True);r.update(config=x,pause=t)
 return r
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--out',type=Path,required=True)
 p.add_argument('--configs',type=Path,help='Replay the config arrays in a prior report.')
 p.add_argument('--nearflat',action='store_true')
 args=p.parse_args()
 if args.configs:
  d=json.loads(args.configs.read_text());configs=[r['config'] for r in (d['rows'] if isinstance(d,dict) else d)]
 elif args.nearflat:configs=[[.65,.7,4.,4.,pd,7.] for pd in [1.565,1.568,1.57]]
 else:configs=[[v,rp,kk,kk,1.55,7.] for v in [.5,.65,.8] for rp in [.65,.7,.75] for kk in [4.,7.]]
 report=dict(scope=__doc__,core_radius=m.CORE_RADIUS,core_proxy_amplitude=m.CORE_AMPLITUDE,
  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  linear_screen_sha256=hashlib.sha256((P/'scripts/fd2d_short_core_screen.py').read_bytes()).hexdigest(),
  port_sha256=hashlib.sha256((P/'notes/2026-11-12-fd2d-ellipse-cuff032-cut04-port.json').read_bytes()).hexdigest(),
  nonlinear_solution=False,rows=[])
 for x in configs:
  try:r=trial(x)
  except Exception as exc:r=dict(config=x,error=str(exc))
  report['rows'].append(r);args.out.write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(dict(event='complete',candidates=len(report['rows']),
  errors=sum('error' in r for r in report['rows']),
  max_direction_residual=max((abs(r['residual'][0]) for r in report['rows'] if 'residual' in r),default=None))))
if __name__=='__main__':main()
