#!/usr/bin/env python3
"""New-cuff short n2 prefix design screen, not a nonlinear flexible surface.

All profiles are C2 and use the same *new* finite physical tail port within a
single run. The core line is propagated by the exact linearized warped-metric
system, with finite RK and quadrature errors. The q=.3 XYZ model is a first-order
proxy only: it has quadratic metric defects and is not the exact support core.
The recorded height, slab, and held diagnostics may reject an unpromising seed;
they do not prove any nonlinear geometry or common-g closure.
No production BVP, existing metric, or physical finite-tail parameters are edited.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np, math, json, argparse, hashlib
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, least_squares
from pathlib import Path
G,W=np.polynomial.legendre.leggauss(32);G=(G+1)/2;W=W/2
PORT=None
CORE_RADIUS=1.
CORE_AMPLITUDE=.3
rc=wc=wrc=pt=ps=None
D={}
def load_port(path):
 global PORT,rc,wc,wrc,pt,ps,D
 PORT=json.loads(Path(path).read_text())
 rc=PORT['cut']['r'];wc=PORT['cut']['w'];wrc=PORT['cut']['wr'];pt=-math.atan2(1,wc);ps=-wrc/(1+wc*wc)**1.5
 D={r['mode']:r['slope'] for r in PORT['rows']}
def ramp(u,e=.08):
 u=np.asarray(u);t=np.clip(np.minimum(u,1-u)/e,0,1);z=3*t*t-2*t*t*t
 x=np.clip(u/e,0,1);left=e*(x**3-x**4/2)
 x=np.clip((1-u)/e,0,1);right=1-e-e*(x**3-x**4/2)
 return z,np.where(u<e,left,np.where(u>1-e,right,u-e/2))
def phase(seg,u):
 if seg['kind']=='turn':return seg['p0']+(seg['p1']-seg['p0'])*ramp(u)[1]/.92
 if seg['kind']=='brake':return seg['p0']+(seg['p1']-seg['p0'])*np.asarray(u)**2
 return 0*np.asarray(u)+seg['p0']
def piece(kind,p0,p1,K):
 L=abs(p1-p0)/(K*.92) if kind=='turn' else 2*(p1-p0)/ps
 s=dict(kind=kind,p0=p0,p1=p1,L=L,K=K)
 # Split quadrature at the smooth turn ramp joins.
 cuts=[0,.08,.92,1] if kind=='turn' else [0,1]
 s['dr']=0.;s['dh']=0.
 for lo,hi in zip(cuts[:-1],cuts[1:]):
  p=phase(s,lo+(hi-lo)*G);s['dr']+=L*(hi-lo)*np.dot(np.sin(p),W);s['dh']+=L*(hi-lo)*np.dot(np.cos(p),W)
 return s
def profile(pplus,pdown,Kout,Kturn):
 segs=[piece('turn',0,pplus,Kout),piece('turn',pplus,-pdown,Kturn)]
 b=piece('brake',-pdown,pt,ps)
 a=CORE_RADIUS+sum(s['dr'] for s in segs)
 L=(rc-b['dr']-a)/math.sin(-pdown)
 if L<0:raise ValueError('no coast')
 segs.append(dict(kind='coast',p0=-pdown,p1=-pdown,L=L,dr=L*math.sin(-pdown),dh=L*math.cos(pdown),K=0))
 segs.append(b)
 return segs
def evaluate(x,detail=False,modes=(2,)):
 return evaluate_segments(profile(*x),detail,modes,x)
def evaluate_segments(segs,detail=False,modes=(2,),x=None):
 state=np.r_[CORE_RADIUS,0.,np.tile([1.,0.],len(modes))];records=[]
 for seg in segs:
  def fun(u,y):
   ph=float(phase(seg,u));v=math.sin(ph);b=math.cos(ph);a=y[0];d=[v,b]
   for j,m in enumerate(modes):
    f,g=y[2+2*j:4+2*j];mm=m*m;d.extend([(-(mm-1)*v*f-mm*b*g)/a,((mm-1)*v*v/b*f+mm*v*g)/a])
   return seg['L']*np.array(d)
  sol=solve_ivp(fun,(0,1),state,method='DOP853',rtol=5e-10,atol=1e-12,max_step=.12,dense_output=detail)
  if not sol.success:raise RuntimeError(sol.message)
  if detail:records.append((seg,sol.sol(np.linspace(0,1,201))))
  state=sol.y[:,-1]
 res=[];traces=[]
 for j,m in enumerate(modes):
  f,g=state[2+2*j:4+2*j];T=np.array([-wc*(rc*D[m]-m*m)/(m*m-1),1]);T/=np.linalg.norm(T)
  res.append((f*T[1]-g*T[0])/math.hypot(f,g));traces.append(dict(mode=m,f=f,g=g))
 if not detail:return np.array(res)
 fields=np.hstack([z for s,z in records]);r=fields[0];h=fields[1]
 f=fields[2];g=fields[3]
 q=CORE_AMPLITUDE;B=np.maximum((r+q*f)**2+(h+q*g)**2,(r-q*f)**2+(h-q*g)**2)
 theta=np.linspace(0,2*np.pi,257)[:-1];ct=np.cos(theta)[None,:];st=np.sin(theta)[None,:];c2=np.cos(2*theta)[None,:];s2=np.sin(2*theta)[None,:]
 rad=r[:,None]+q*f[:,None]*c2;tan=-q*f[:,None]*s2/2
 xx=rad*ct-tan*st;yy=rad*st+tan*ct;zz=h[:,None]+q*g[:,None]*c2
 d2=xx*xx+(yy-(CORE_RADIUS+q))**2+zz*zz
 proxy=dict(max_y=float(yy.max()),max_abs_z=float(abs(zz).max()),held_witness_distance=float(np.sqrt(d2.min())),held_protection_max_violation=float((yy-(CORE_RADIUS-q)-zz*zz/(4*q)).max()))
 return dict(linear_geometry_proxy=proxy,x=list(x) if x is not None else None,residual=res,cut=traces,background_height=state[1],full_background_height=state[1]+PORT['stats']['heightSpan'],linear_height_span=float(np.max(h+q*np.abs(g))),linear_ball_D=2*float(np.sqrt(B.max())),min_radius=float(r.min()),max_radius=float(r.max()),fmax=float(abs(f).max()),gmax=float(abs(g).max()),segments=segs)
def main():
 global CORE_RADIUS,CORE_AMPLITUDE
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--port',type=Path,required=True)
 p.add_argument('--out',type=Path,required=True)
 p.add_argument('--core-radius',type=float,default=1.)
 p.add_argument('--core-amplitude',type=float,default=.3)
 p.add_argument('--replay',type=Path,help='Evaluate the stored four-parameter candidates without another scan.')
 p.add_argument('--single',nargs=4,type=float,metavar=('PPLUS','PDOWN','KOUT','KTURN'))
 args=p.parse_args();load_port(args.port);CORE_RADIUS=args.core_radius;CORE_AMPLITUDE=args.core_amplitude
 rows=[];errors=[]
 report=dict(scope=__doc__,port=str(args.port),port_sha256=hashlib.sha256(args.port.read_bytes()).hexdigest(),
   source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
   core_radius=CORE_RADIUS,core_amplitude_for_linear_proxy=CORE_AMPLITUDE,finite_linear_port=True,nonlinear_solution=False,
   geometry_certificate=False,rows=rows,errors=errors)
 def save():args.out.write_text(json.dumps(report,indent=2)+'\n')
 def record(x):
  z=evaluate(x,True);rows.append(z);save()
  print(json.dumps({k:z[k] for k in ('x','residual','cut','full_background_height','linear_geometry_proxy')}),flush=True)
 if args.single:record(args.single)
 elif args.replay:
  old=json.loads(args.replay.read_text());old=old.get('rows',old) if isinstance(old,dict) else old
  for row in old:record(row['x'])
 else:
  for ko in [8.,10.]:
   for kt in [8.,10.]:
    for pd in [1.45,1.54,1.56]:
     prev=None
     for pp in np.linspace(.6,1.45,13):
      try:
       r=float(evaluate([pp,pd,ko,kt])[0])
       if prev is not None and r*prev[1]<0:
        root=brentq(lambda v:float(evaluate([v,pd,ko,kt])[0]),prev[0],pp,xtol=1e-10)
        record([root,pd,ko,kt])
       prev=pp,r
      except Exception as exc:
       errors.append(dict(x=[pp,pd,ko,kt],error=str(exc)));prev=None;save()
 save();print(json.dumps(dict(event='complete',candidates=len(rows),errors=len(errors))))
if __name__=='__main__':main()
