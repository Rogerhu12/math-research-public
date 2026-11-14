#!/usr/bin/env python3
"""First-order m3 ball envelope and exact tangent-core rational tail bounds.
The envelope is a comparison for a linear field, never a nonlinear enclosure.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,json,math
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.integrate import cumulative_trapezoid
from root_general_prefix_scan import install
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--source-root',required=True,type=Path);p.add_argument('--ellipse-notes',required=True,type=Path)
p.add_argument('--prefix-scan',required=True,type=Path);p.add_argument('--out',required=True,type=Path)
a=p.parse_args();backward=install(a.ellipse_notes,a.source_root)
d=json.loads(a.prefix_scan.read_text());port=d['port'];cfg=d['rows'][0]['roots'][0]['config'];prof,line=backward(cfg,port)
x=np.unique(np.r_[np.linspace(0,prof.end,8193),prof.breaks]);radius,v,acc=prof.profile(x)
z=cumulative_trapezoid(np.sqrt(1-v*v),x,initial=0);fg=np.empty((2,len(x)))
for k,(lo,hi,sol,scale) in enumerate(line.segments):
 mask=(x>=lo)&((x<hi) if k+1<len(line.segments) else (x<=hi))
 fg[:,mask]=sol(x[mask])*np.exp(scale-line.logscale)/line.core[0]
f,g=fg;rows=[]
for q in [.08,.09,.1]:
 ell=2*q;norm2=np.maximum((radius+q*f)**2+(z+ell+q*g)**2,(radius-q*f)**2+(z+ell-q*g)**2)
 i=int(np.argmax(norm2));top=float(z[-1]+ell+abs(q*g[-1]))
 rows.append(dict(q=q,ell=ell,prefix_ball_D=float(2*np.sqrt(norm2[i])),at_s=float(x[i]),cut_z_max=top,
  cut_radial_max=float(radius[-1]+abs(q*f[-1])),conditional_tail_top_z=top+.022,
  conditional_full_D=float(max(2*np.sqrt(norm2[i]),2*np.hypot(.601,top+.022))),cutoff_height_amplitude=float(abs(q*g[-1]))))
B=Fraction(11,50);u=B/2;E=1/(1-B*B/4);bounds=[]
for M in[4,6,8]:
 e1=2*E*u**(M+1)/math.factorial(M+1)/(1-u/Fraction(M+2));e2=6*E*u**(M+1)/math.factorial(M)/(1-u/Fraction(M+1))
 bounds.append(dict(M=M,derivative_fraction=str(e1),second_fraction=str(e2),metric_fraction=str(2*e1+e1*e1)))
result=dict(scope=__doc__,config=cfg,envelope=rows,core=dict(B=str(B),support_gap_lower=str(3*B/4-3*B**3/32),rational_bounds=bounds))
a.out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(envelope=[dict(q=r['q'],comparison_D=r['conditional_full_D']) for r in rows],support_gap_lower=result['core']['support_gap_lower'])))
