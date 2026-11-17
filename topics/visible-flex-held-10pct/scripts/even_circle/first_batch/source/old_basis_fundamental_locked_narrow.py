#!/usr/bin/env python3
"""Old t^6(1-t)^6 basis: fair fundamental-locked canonical controls.

Only the old basis is tested. Low support moments are integrated with an
80-digit exponential-polynomial primitive; physical suprema are sampled.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,json,math,sys,hashlib
from pathlib import Path
import numpy as np
import mpmath as mp
p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);args=p.parse_args();sys.path.insert(0,str(args.source.resolve()));from plateau_core import PlateauSupportCore as Core
mp.mp.dps=80
B=[0]*6+[4096*(-1)**j*math.comb(6,j)for j in range(7)]
def J(z,phase):
 iz=1j*z
 if abs(z)<mp.mpf('1e-50'):return mp.cos(phase)*sum(mp.mpf(B[j])/(j+1)for j in range(13))
 e=mp.exp(iz);I=mp.expm1(iz)/iz;total=B[0]*I
 for j in range(1,13):I=e/iz-j*I/iz;total+=B[j]*I
 return mp.re(mp.exp(1j*phase)*total)
def moments(core,M,a):
 T=mp.pi/2;L=T-2*mp.mpf(str(a));AA=mp.mpf(str(a));S=mp.matrix(M,len(core.c))
 for k in range(1,M+1):
  freq=4*k
  for j in range(1,len(core.c)+1):
   w=2*mp.pi*j;norm=mp.mpf(str(core.norms[j-1]));S[k-1,j-1]=freq*L/(T*norm)*(J(w-freq*L,-freq*AA)-J(w+freq*L,freq*AA))
 return S
def deriv(core,phi,j):
 t=(phi-core.a)%core.T/core.L;inside=t<1;t=np.clip(t,0,1);w=core.omega[:,None];ang=w*t[None,:]
 ans=sum(math.comb(j,k)*core.polys[j-k](t)[None,:]*w**k*np.sin(ang+k*np.pi/2)for k in range(j+1))/core.L**j/core.norms[:,None]
 return np.where(inside[None,:],ans,0.)
rows=[]
for a in [.145]:
 for M in [4,6,8]:
  row=dict(halfwidth=a,M=M,controls_locked=M,controls_unlocked=M-1)
  for locked in [False,True]:
   core=Core(.005,np.zeros(M if locked else M-1),4,halfwidth=a,transition=.08,homotopy=1.,center=0.,arc_nodes=512);Smp=moments(core,M,a);S=np.array(Smp.tolist(),float);sqmp=Smp if locked else Smp[1:,:];sq=np.array(sqmp.tolist(),float);freq=4*np.arange(1,M+1);rho_sq=sq*(1-freq[(0 if locked else 1):]**2)[:,None]
   coefficients=[]
   for k in range(1,M):
    target=mp.matrix(M if locked else M-1,1);target[k if locked else k-1]=1
    coefficients.append([float(x)for x in mp.lu_solve(sqmp,target)])
   C=np.array(coefficients).T;phi=core.T*np.arange(16384)/16384;r=deriv(core,phi,1)+deriv(core,phi,3);rp=deriv(core,phi,2)+deriv(core,phi,4);R=C.T@r;RP=C.T@rp
   rho=np.max(abs(R),axis=1);rho_p=np.max(abs(RP),axis=1);fund=S[0]@C
   name='locked'if locked else'unlocked';row[name]=dict(support_moment_condition=float(np.linalg.cond(sq)),rho_moment_condition=float(np.linalg.cond(rho_sq)),support_column_normalized_condition=float(np.linalg.cond(sq/np.linalg.norm(sq,axis=0))),fundamental_leakage_per_unit_high_support=fund.tolist(),canonical_rho_sup_per_unit_high_support=rho.tolist(),canonical_rho_prime_sup_per_unit_high_support=rho_p.tolist(),canonical_rho_sup_per_unit_high_rho=(rho/(freq[1:]**2-1)).tolist(),canonical_rho_prime_sup_per_unit_high_rho=(rho_p/(freq[1:]**2-1)).tolist(),sample_count=16384,finite_moment_identity_error=float(abs(sq@C-(np.eye(M)[:,1:]if locked else np.eye(M-1))).max()))
  rows.append(row);print(json.dumps(row),flush=True)
out=dict(scope=__doc__,target='Each canonical column has cosine support moment 1 at one mode8,...,4M and zero at all other represented higher moments; locked also has primary mode4 moment zero. Mean is exactly zero for derivative compact functions.',rows=rows,source_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in [Path(__file__),args.source/'plateau_core.py']})
args.out.write_text(json.dumps(out,indent=2)+'\n')
