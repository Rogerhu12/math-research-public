#!/usr/bin/env python3
"""Read the true kappa=0 HoldProfile interface using the R630 physical-phi formulas.
The a'>0 orientation is fixed: r=a, w=sqrt(1-a'^2)/a', h_r=h_s/a'.
Every physical Fourier mode is retained. This is a finite trace, not a DN map.
"""
import argparse,gzip,hashlib,importlib.util,json
from pathlib import Path
import numpy as np
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main(a):
 d=json.loads(gzip.decompress(a.input.read_bytes()));source=sha(a.hold_source)
 if not d.get('ivp_reached_end') or d.get('old_prefix_C2_join_completed') or source!=d['hold_profile_sha256']:raise ValueError('Require the unmodified true IVP and its actual scalar')
 spec=importlib.util.spec_from_file_location('actual_hold_trace_scalar',a.hold_source);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 profile=m.HoldProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin'],d['hold_scalar_profile']['cut'],d['hold_scalar_profile']['quadrature'])
 if profile.spec()!=d['hold_scalar_profile']:raise ValueError('The scalar changed')
 s=d['mesh'][-1];r,ap,app=profile(s);M=d['M'];N=a.angles;nu=2*np.arange(1,M+1)
 if not 0<ap<1 or abs(profile.meridian(s)['curvature'])>1e-10:raise ValueError('Require the specified type interface with a_prime>0')
 if N%2 or N<4*M+4:raise ValueError('Insufficient angular diagnostic grid')
 y=np.array(d['states'][-1]);v=np.array(d['rhs'][-1]);acc=np.array(d['d2'][-1]);h=y[2*M+1:];hs=v[2*M+1:];hss=acc[2*M+1:]
 n=np.sqrt(1-ap*ap);w=n/ap;wr=-app/(ap**3*n);rc=(1-nu**2)*np.array(d['original_core_coefficients'])
 pc=-nu*h[1:]/(r*w);kc=hs[1:]/n;cm=hs[0]/n-1;hr=hs/ap;hrr=(hss*ap-hs*app)/ap**3
 phi=2*np.pi*np.arange(N)/N;cs=np.cos(phi[:,None]*nu);sn=np.sin(phi[:,None]*nu)
 rho=1+cs@rc;rhop=-sn@(nu*rc);pt=sn@pc;K=cm+cs@kc;P=pt/rho;T=(cs@(nu*pc))/rho**2-pt*rhop/rho**3;U=-(sn@(nu*kc))/rho-P
 z=w*w;E=1+z;A=2*K+K*K+E*P*P;S=1-z*P*P;D=1-z*A;L=1+K+E*T;bn=1+z*(1+K)*T/S
 mean=None
 if min(S.min(),D.min())>0:
  q=np.sqrt(D);B=A/(q*(1+q))+(1+K)*T/(S*q);mean=float(np.mean(rho*B))
 report=dict(scope=__doc__,source_sha256=sha(__file__),input_sha256=sha(a.input),hold_profile_sha256=source,s=s,physical_modes=M,angles=N,r=r,a_prime=ap,a_second=app,w=w,w_r=wr,
  rho_cos_coefficients=rc.tolist(),Ptilde_sin_coefficients=pc.tolist(),K_mean=float(cm),K_cos_coefficients=kc.tolist(),height_mean=float(h[0]),height_cos_coefficients=h[1:].tolist(),
  height_r_mean=float(hr[0]),height_r_cos_coefficients=hr[1:].tolist(),height_rr_mean=float(hrr[0]),height_rr_cos_coefficients=hrr[1:].tolist(),
  R_cos_coefficients=y[:M+1].tolist(),T_sin_coefficients=y[M+1:2*M+1].tolist(),
  sampled=dict(rho_min=float(rho.min()),P_max=float(max(abs(P))),Ptilde_max=float(max(abs(pt))),K_max=float(max(abs(K))),T_max=float(max(abs(T))),U_max=float(max(abs(U))),
   S_min=float(S.min()),D_min=float(D.min()),L_min=float(L.min()),y_min=float((1+K).min()),N_min=float(bn.min()),weighted_mean=mean),
  limitations='All physical modes are retained without material-angle re-expansion. Branch/mean extrema are sampled, and metric error is inherited from the actual finite IVP. No DN or closed geometry is asserted.')
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if not k.endswith('coefficients')},indent=2));print(json.dumps(dict(output_sha256=sha(a.out))))
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for k in ('input','hold-source','out'):p.add_argument('--'+k,type=Path,required=True)
 p.add_argument('--angles',type=int,default=8192);main(p.parse_args())
