#!/usr/bin/env python3
"""Angular Frenet RHS spectrum at specified saved-prefix latitudes.

Reprojection at larger Fourier cutoffs uses the same saved curve, not a new
BVP solution. It distinguishes unresolved angular structure from quadrature
error and predicts only the projection error of this particular curve.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,importlib.util,json,sys
from pathlib import Path
import numpy as np
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent

def main():
 p=argparse.ArgumentParser(description=__doc__)
 for k in ('input','source-topic','port','out'):p.add_argument('--'+k,type=Path,required=True)
 p.add_argument('--s',type=float,nargs='+',required=True);p.add_argument('--angular',type=int,default=4096)
 p.add_argument('--cutoffs',type=int,nargs='+',default=[20,24,28,32,40,48,64])
 a=p.parse_args();sp=importlib.util.spec_from_file_location('geometric_spectrum_pullback',HERE/'geometric-checkpoint-core-pullback.py')
 m=importlib.util.module_from_spec(sp);sys.modules[sp.name]=m;sp.loader.exec_module(m)
 saved,_=m.load_saved(a.input,a.source_topic,a.port,angular=512);f=saved.flow
 B,B1,B2=f.basis(a.angular);s=np.asarray(a.s);Y=saved.sol.sol(s);fr=f.frame(s,f.q*Y,B1,B2)
 W=fr['V']-fr['geo']['s1'];phi=2*np.pi*np.arange(a.angular)/a.angular;c=np.cos(phi);sn=np.sin(phi)
 cyl=np.stack((c*W[:,:,0]+sn*W[:,:,1],-sn*W[:,:,0]+c*W[:,:,1],W[:,:,2]),axis=-1)
 cyl[:,:,2]-=np.mean(cyl[:,:,2],axis=1)[:,None]
 ff=np.fft.fft(cyl,axis=1)/a.angular;freq=np.fft.fftfreq(a.angular)*a.angular
 rows=[]
 for j,ss in enumerate(s):
  row=dict(s=float(ss),curve_curvature_min=float(fr['kap'][j].min()),
   frenet_margin_min=float(fr['margin'][j].min()),chart_rho_min=float(fr['geo']['rho'][j].min()),
   nonlinear_RHS_modes=[dict(mode=k,physical_frequency=2*k,cos_sin_vector_amplitude=(2*abs(ff[j,2*k])).tolist())for k in range(1,65)],
   cutoffs=[])
  for cut in a.cutoffs:
   tail=ff[j].copy();tail[abs(freq)<=2*cut]=0
   residual=np.fft.ifft(tail*a.angular,axis=0).real
   i=int(np.argmax(np.linalg.norm(residual,axis=1)))
   row['cutoffs'].append(dict(modes=cut,maximum_projection_defect_sample=float(np.linalg.norm(residual,axis=1).max()),
    fourier_l1_tail=float(np.linalg.norm(tail,axis=1).sum()),psi=float(phi[i])))
  rows.append(row)
 out=dict(scope=__doc__,input_file=str(a.input),input_sha256=hashlib.sha256(a.input.read_bytes()).hexdigest(),
  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),angular=a.angular,rows=rows)
 a.out.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps([dict(s=r['s'],margin=r['frenet_margin_min'],cutoffs=r['cutoffs'])for r in rows]))
if __name__=='__main__':main()
