#!/usr/bin/env python3
"""Small targeted m4 linear screen with explicit consumed circular window.

Every row is a new metric. A linear root is not a nonlinear isometric prefix.
The true finite tail port is consumed with its literal frequencies.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp,quad
from scipy.optimize import brentq
from consumed_short_profile import ConsumedShortLoop,configure

def integrate(profile,port,count=1,dense=False):
 m=np.array(port['modes'][:count],float);r=port['cut']['radius'];w=port['cut']['backgroundSlope'];D=np.array(port['linearSlope'][:count]);state=np.stack((-w*(r*D-m*m)/(m*m-1),np.ones(count)),axis=1);state/=np.linalg.norm(state,axis=1)[:,None];terminal=state.copy();logs=np.zeros(count);segments=[]
 def rhs(s,y):
  a,v,_=profile.profile([s]);a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v);z=y.reshape(count,2);F=z[:,0];G=z[:,1]
  return np.stack((-(m*m-1)*v*F-m*m*b*G,(m*m-1)*v*v*F/b+m*m*v*G),axis=1).ravel()/a
 for low,high in reversed(list(zip(profile.breaks[:-1],profile.breaks[1:]))):
  if high-low<1e-14:continue
  z=solve_ivp(rhs,[high,low],state.ravel(),rtol=2e-10,atol=2e-12,method='DOP853',max_step=(high-low)/4,dense_output=dense)
  if not z.success:raise RuntimeError(z.message)
  if dense:segments.append((low,high,z.sol,logs.copy()))
  state=z.y[:,-1].reshape(count,2);scales=np.linalg.norm(state,axis=1);state/=scales[:,None];logs+=np.log(scales)
 return dict(core=state,logs=logs,H_per_q=terminal[:,1]*np.exp(-logs)/state[:,0],segments=sorted(segments,key=lambda z:z[0]),rhs=rhs)

def geometry(f,R=.325):
 s=np.unique(np.r_[np.linspace(0,f.end,4001),f.breaks]);a,v,acc=f.profile(s);b=np.sqrt(1-v*v)
 def chi(s):
  aa,vv,kk=f.profile([s]);return math.sqrt(max(float(kk[0]),0)/(float(aa[0])*(1/R**2-float(vv[0])**2)))
 cuts=[x for x in f.breaks if x<=f.first_positive_K+1e-14];loss=0.;err=0.
 for lo,hi in zip(cuts,cuts[1:]):
  z,e=quad(chi,lo,hi,epsabs=2e-12,epsrel=2e-12,limit=100);loss+=z;err+=e
 p=f.parameters;aramp=1+p['delta']*p['epsilon']/(2*(1-p['epsilon']));A0=p['vu']/(p['epsilon']*f.Tu*(1-p['eta']))
 # asin(y)-asin(x)>=y-x; this elementary expression is a lower bound.
 lower=R*(p['vu']/math.sqrt(aramp*A0)+(p['extra_speed']-p['vu'])/math.sqrt(f.a_extra*p['extra_acceleration']))
 return dict(background_height=float(np.trapezoid(b,s)),background_radius=float(a.max()),background_kappa=float(np.max(np.maximum(abs(acc)/b,b/a))),background_root_min=float((1-v*v).min()),length=f.end,first_positive_K=f.first_positive_K,circle_characteristic_loss=loss,circle_loss_quadrature_error=err,circle_loss_elementary_lower=lower,circle_loss_over_R=loss/R,circle_loss_lower_over_R=lower/R,circle_required_halfwidth=R*.28,coast_length=float(f.lengths[3]))

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--port',type=Path,required=True);p.add_argument('--head-source',type=Path,required=True);p.add_argument('--short-source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True);configure(a.head_source,a.short_source);port=json.loads(a.port.read_text())
 if port['modes']!=[4*(i+1)for i in range(len(port['modes']))]:raise ValueError('Expected literal m4,m8,... physical port')
 rows=[];roots=[];start=time.time()
 cases=[dict(extra_speed=.60,extra_acceleration=2.,return_speed=.60,turn_acceleration=5.5),dict(extra_speed=.55,extra_acceleration=2.,return_speed=.60,turn_acceleration=5.5),dict(extra_speed=.65,extra_acceleration=2.,return_speed=.65,turn_acceleration=5.5),dict(extra_speed=.60,extra_acceleration=1.5,return_speed=.60,turn_acceleration=5.5),dict(extra_speed=.60,extra_acceleration=3.,return_speed=.65,turn_acceleration=5.5),dict(extra_speed=.60,extra_acceleration=2.,return_speed=.60,turn_acceleration=3.5)]
 for ci,cfg in enumerate(cases):
  previous=None
  for ac in [1.8,2.2,2.8,3.6,4.8,6.2]:
   try:
    f=ConsumedShortLoop(port['cut'],**cfg,stop_acceleration=ac);g=geometry(f);val=float(integrate(f,port)['core'][0,1]);row=dict(case=ci,parameters=f.parameters,residual=val,**g);rows.append(row)
    print(json.dumps(dict(event='probe',case=ci,stop=ac,residual=val,height=g['background_height'],K=g['background_kappa'],Rmax=g['background_radius'],loss_over_R=g['circle_loss_over_R'])),flush=True)
    if previous is not None and previous[1]*val<0:
     acroot=brentq(lambda z:integrate(ConsumedShortLoop(port['cut'],**cfg,stop_acceleration=z),port)['core'][0,1],previous[0],ac,xtol=2e-11)
     ff=ConsumedShortLoop(port['cut'],**cfg,stop_acceleration=acroot);lin=integrate(ff,port,4,dense=True);gg=geometry(ff);result=dict(case=ci,parameters=ff.parameters,residuals=lin['core'][:,1].tolist(),linear_H_per_q=lin['H_per_q'].tolist(),**gg);roots.append(result)
     x=np.linspace(0,1,97);ss=x*ff.end;fg=np.zeros((2,len(ss)))
     for lo,hi,sol,ls in lin['segments']:
      mask=(ss>=lo-1e-14)&(ss<=hi+1e-14)
      if np.any(mask):fg[:,mask]=sol(ss[mask]).reshape(4,2,-1)[0]*math.exp(ls[0]-lin['logs'][0])/lin['core'][0,0]
     aa,ap,_=ff.profile(ss);h=fg[0]/aa;endstate=np.zeros((4,2));endstate[0]=fg[:,-1];rhs=lin['rhs'](ff.end,endstate.ravel()).reshape(4,2)[0];hp=(rhs[0]*aa[-1]-fg[0,-1]*ap[-1])/aa[-1]**2*ff.end
     dest=a.out/f'case{ci}-root{len(roots)}';dest.mkdir(exist_ok=True);(dest/'profile.json').write_text(json.dumps(ff.parameters,indent=2)+'\n');(dest/'chart.json').write_text(json.dumps(dict(knots=x.tolist(),values=h.tolist(),final_derivative=float(hp),reference_profile=ff.parameters),indent=2)+'\n');(dest/'linear.json').write_text(json.dumps(result,indent=2)+'\n');result['directory']=str(dest);print(json.dumps(dict(event='root',**result)),flush=True)
    previous=(ac,val)
   except Exception as e:
    row=dict(case=ci,parameters={**cfg,'stop_acceleration':ac},error=repr(e));rows.append(row);print(json.dumps(dict(event='rejected',**row)),flush=True);previous=None
  summary=dict(scope=__doc__,port_sha256=hashlib.sha256(a.port.read_bytes()).hexdigest(),source_sha256={str(x):hashlib.sha256(x.read_bytes()).hexdigest()for x in [Path(__file__),Path(__file__).with_name('consumed_short_profile.py'),a.head_source,a.short_source]},rows=rows,roots=roots,seconds=time.time()-start)
  (a.out/'screen.json').write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps(dict(event='complete',roots=len(roots),seconds=time.time()-start)),flush=True)
if __name__=='__main__':main()
