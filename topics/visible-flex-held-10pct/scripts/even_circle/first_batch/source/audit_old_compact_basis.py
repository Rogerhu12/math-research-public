#!/usr/bin/env python3
"""Independent old compact-basis low-moment conditioning diagnostic.

No PDE solve or new basis is performed. Conditioning and sampled rho are
floating diagnostics, not a general compatibility obstruction.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import sys,json,hashlib,argparse
import numpy as np

p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--run-summary',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();sys.path.insert(0,str(a.source.resolve()));from homotopy_plateau_core import HomotopyPlateauCore as Core
from plateau_core import PlateauSupportCore
run=json.loads(a.run_summary.read_text());base=next(r for r in run['rows']if r.get('success')and r['homotopy']==0.)
args=run['arguments'];q=base['q'];half=args['halfwidth'];transition=args['transition'];center=args['center'];rows=[]
def diagnostics(M):
 core=Core(q,np.zeros(M-1),4,halfwidth=half,transition=transition,center=center,homotopy=0.,arc_nodes=512)
 mats=[]
 for N in [128,256]:
  x,w=np.polynomial.legendre.leggauss(N);phi=center+half+core.L*(x+1)/2;f=PlateauSupportCore._basis(core,phi)[0];freq=4*np.arange(1,M+1);C=core.L/core.T*(f*w)@np.sin(freq[:,None]*phi).T
  S=(C*freq).T;R=S*(1-freq**2)[:,None];mats.append((S,R))
 S,R=mats[-1];rho=R[1:];sup=S[1:]
 row=dict(M=M,controls=M-1,core_sector_length=core.T,complement_length=core.L,rho_moment_cond=float(np.linalg.cond(rho)),support_moment_cond=float(np.linalg.cond(sup)),rho_column_normalized_cond=float(np.linalg.cond(rho/np.linalg.norm(rho,axis=0))),rho_singular_values=np.linalg.svd(rho,compute_uv=False).tolist(),support_singular_values=np.linalg.svd(sup,compute_uv=False).tolist(),quadrature128_256_rho_maxdiff=float(abs(mats[0][1]-R).max()))
 return row,core,S,R
for M in [4,6,8,10,12]:
 r,*_=diagnostics(M);rows.append(r);print(json.dumps(r),flush=True)
M=base['modes'];r,zero,S,R=diagnostics(M);c=np.asarray(base['physical_core_corrections']);phi=2*np.pi*np.arange(65536)/65536
core=Core(q,c,4,halfwidth=half,transition=transition,center=center,homotopy=0.,arc_nodes=512);compact=PlateauSupportCore._basis(core,phi);r_comp=c@(compact[1]+compact[3]);r_low=c@(core._truncated_derivative(phi,1)+core._truncated_derivative(phi,3));rho0=1-15*q*np.cos(4*phi)+r_low
chi=core.chi(phi);target=-15*(chi-core.mean_chi)/(1-core.mean_chi);drho=q*(target+15*np.cos(4*phi))+r_comp-r_low
mask=drho<0;threshold=rho0[mask]/(-drho[mask]);j=int(np.argmin(threshold));phi_loss=float(phi[mask][j]);limit=float(threshold[j]);rho15=rho0+.15*drho
sv=np.linalg.svd(R[1:],compute_uv=False);c_min=np.linalg.lstsq(R[1:],(R@c)[1:],rcond=None)[0]
actual=dict(q=q,M=M,correction_l1=float(abs(c).sum()),correction_l2=float(np.linalg.norm(c)),correction_linf=float(abs(c).max()),low_support_primary=float((S@c)[0]),low_support_high_l1=float(abs((S@c)[1:]).sum()),low_rho_high_l1=float(abs((R@c)[1:]).sum()),full_compact_rho_correction_linf=float(abs(r_comp).max()),truncated_rho_correction_linf=float(abs(r_low).max()),compact_high_remainder_linf=float(abs(r_comp-r_low).max()),rho0_min_sample=float(rho0.min()),rho_lambda015_min_sample=float(rho15.min()),lambda_first_zero_sample=limit,phi_first_zero_sample=phi_loss,control_over_low_rho_l2=float(np.linalg.norm(c)/np.linalg.norm((R@c)[1:])),inverse_rho_singular_max=float(1/sv[-1]),same_low_moments_recovered_control_relative_error=float(np.linalg.norm(c-c_min)/np.linalg.norm(c)),scope='Fixed old lambda0 control vector blended to exact compact support; failure of this predictor is not nonexistence of another nonlinear branch.')
print(json.dumps(actual),flush=True)
out=dict(scope=__doc__,arguments={k:str(v)if isinstance(v,Path)else v for k,v in vars(a).items()},matrix_definition='S[k,j] is the cosine support coefficient of b_j=f_j prime at frequency4(k+1); R[k,j]=(1-(4(k+1))^2)S[k,j]. Square submatrix drops primary k=0, since primary line is at its designed root.',conditioning=rows,actual_lambda0_controls=actual,source_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in [Path(__file__),a.source/'plateau_core.py',a.source/'homotopy_plateau_core.py',a.run_summary]})
a.out.write_text(json.dumps(out,indent=2)+'\n')
