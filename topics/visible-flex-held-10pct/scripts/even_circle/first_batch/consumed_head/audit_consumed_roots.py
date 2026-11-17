#!/usr/bin/env python3
"""Full m4 finite-port transversality and sampled radial size of two roots."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,math
import numpy as np
from consumed_short_profile import configure,ConsumedShortLoop
from screen_consumed_short import integrate,geometry

p=argparse.ArgumentParser();p.add_argument('--port',type=Path,required=True);p.add_argument('--head-source',type=Path,required=True);p.add_argument('--short-source',type=Path,required=True);p.add_argument('--root',type=Path,nargs='+',required=True);args=p.parse_args();configure(args.head_source,args.short_source);port=json.loads(args.port.read_text())
for root in args.root:
 cfg=json.loads((root/'profile.json').read_text());f=ConsumedShortLoop(port['cut'],**cfg);lin=integrate(f,port,8);diag=geometry(f)
 s=np.unique(np.r_[np.linspace(0,f.end,16001),f.breaks]);a,v,acc=f.profile(s);g,w=np.polynomial.legendre.leggauss(8);z=np.r_[0.,np.cumsum((s[1:]-s[:-1])/2*(np.sqrt(1-f.profile(((s[1:]+s[:-1])[:,None]/2+(s[1:]-s[:-1])[:,None]/2*g).ravel())[1]**2).reshape(-1,8)@w))]
 radius=np.sqrt(a*a+(z+.35)**2);ix=int(np.argmax(radius));tail=math.sqrt(port['cut']['radius']**2+(z[-1]+.35+.025)**2)
 fp={k:F(str(cfg[k]))for k in ['delta','vu','epsilon','eta','extra_speed','extra_acceleration','return_speed','turn_acceleration']};d,u,e,h,V,A,ret,turn=[fp[k]for k in ['delta','vu','epsilon','eta','extra_speed','extra_acceleration','return_speed','turn_acceleration']]
 Tu=d/(u*(1-e));aramp=1+d*e/(2*(1-e));A0=u/(e*Tu*(1-h));aextra=1+d*(1-F(3,2)*e)/(1-e)+(V-u)*(V+u)/(2*A*(1-h))
 def sqrt_upper(x):
  n=1
  while F(n,100)**2<=x:n+=1
  return F(n,100)
 U0=sqrt_upper(aramp*A0);U1=sqrt_upper(aextra*A);loss_ratio_lower=u/U0+(V-u)/U1
 t=(1-h)*V/(V+ret)+h/2;assert h<t<1-h
 P=(t*t/2-h*t/2+F(3,20)*h*h)/(1-h);Lt=(V+ret)/(turn*(1-h));rmax_exact=aextra+Lt*(V*t-(V+ret)*P)
 Kbound=max(float(A0)/math.sqrt(1-float(u)**2),float(A)/math.sqrt(1-float(V)**2),float(turn)/math.sqrt(1-max(float(V),float(ret))**2),cfg['stop_acceleration']/math.sqrt(1-float(ret)**2),cfg['bridge_curvature'],1/port['cut']['radius'],abs(f.bridge.ps))
 cert=dict(scope='Exact rational checks for the negative-K head. These prove a conservative characteristic loss bound independently of the floating linear root.',initial_denominator_square=str(aramp*A0),extra_denominator_square=str(aextra*A),initial_sqrt_upper=str(U0),extra_sqrt_upper=str(U1),loss_over_R_lower=str(loss_ratio_lower),loss_over_R_lower_decimal=float(loss_ratio_lower),required=str(F(7,25)),strictly_consumed=bool(loss_ratio_lower>F(7,25)),background_rmax_exact=str(rmax_exact),background_rmax_decimal=float(rmax_exact))
 out=dict(scope=__doc__,profile=cfg,physical_modes=port['modes'],normalized_core_lines=lin['core'].tolist(),transversality=lin['core'][:,1].tolist(),H_at_cut_per_unit_core_mode=lin['H_per_q'].tolist(),max_primary_residual=abs(float(lin['core'][0,1])),head_certificate=cert,elementary_background_curvature_upper=Kbound,geometry=diag,center_cylinder_halfheight=.35,nominal_tail_rise=.025,sampled_background_radius_after_center=float(radius[ix]),sample_radius_arg_s=float(s[ix]),sample_radius_arg_az=[float(a[ix]),float(z[ix])],quadrature_background_height=float(z[-1]),nominal_tail_radius_upper=tail,sampled_and_nominal_tail_radius=max(float(radius[ix]),tail),continuous_size_certificate=False,source_sha256={str(q):hashlib.sha256(q.read_bytes()).hexdigest()for q in [Path(__file__),Path(__file__).with_name('consumed_short_profile.py'),Path(__file__).with_name('screen_consumed_short.py'),args.head_source,args.short_source,args.port,root/'profile.json']})
 (root/'full-diagnostic.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(root=str(root),transversality=out['transversality'],H=out['H_at_cut_per_unit_core_mode'],K_upper=Kbound,R_center=out['sampled_background_radius_after_center'],R_nominal_tail=out['sampled_and_nominal_tail_radius'],head_certificate=cert)),flush=True)
