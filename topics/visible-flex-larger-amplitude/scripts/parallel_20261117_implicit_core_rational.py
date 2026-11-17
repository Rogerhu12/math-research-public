#!/usr/bin/env python3
"""Exact-rational perturbation certificate for one fixed finite core C_U.
Reuse the published R638 rho bound after exact coefficient matching.
No FFT, matrix factorization, nonlinear solve, or rho re-certification.
The bound concerns the mathematical Galerkin operator in orthogonal L2,
not the separately rounded NumPy FFT matrix.
"""
import argparse,gzip,hashlib,json
from fractions import Fraction as F
from pathlib import Path
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(gzip.decompress(p.read_bytes()))
def ff(x):return F.from_float(x)
def sumabs(v):return sum(map(abs,v),F())
def main(a):
 expected={a.warm:'1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057',
  a.reference:'aa1cf41faf83a9e2b3e90167d0bc9e00e48c8d84cc2aec707c2da17c45f0ca15',
  a.rho_report:'d3fe8df338482e0ac01f3d65a2ee91baa5f2996814188a7adb31a4ec01ff9f37',
  a.rho_source:'f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d'}
 source=sha(__file__)
 for p,h in expected.items():
  if sha(p)!=h:raise ValueError('Frozen input changed: '+str(p))
 w=read(a.warm);ref=read(a.reference);cert=json.loads(a.rho_report.read_text());M=w['M'];N=w['N'];n=3*M+2
 if (M,N,n,ref['M'])!=(160,2048,482,320):raise ValueError('Different complete finite core')
 y=list(map(ff,w['states'][0]));u=list(map(ff,w['full_ode_rhs_at_nodes'][0]));R=y[:M+1];T=y[M+1:2*M+1];Z=y[2*M+1:]
 core=list(map(ff,ref.get('original_core_coefficients',ref['states'][0][1:ref['M']+1])))
 if R[0]!=1 or any(Z)or core[:M]!=R[1:]or any(core[M:]):raise ValueError('The exact core rho does not match R638')
 if list(map(ff,ref['states'][0][:M+1]))!=R:raise ValueError('Reference core values differ')
 first=w['fixed_scalar_profile']['geometry']['knots'][0]
 if ff(first['s'])!=0 or ff(first['a'])!=1 or ff(first['ap'])!=0:raise ValueError('The literal core scalar jet changed')
 rho=F(159,1000)
 if cert['input_sha256']!=expected[a.reference]or cert['source_sha256']!=expected[a.rho_source]or not cert['positive']or not cert['strict_under_stated_IEEE_arithmetic']or ff(cert['rho_all_angle_lower'])<=rho:raise ValueError('Missing the published strict rho premise')
 eps=[T[j-1]+2*j*R[j]for j in range(1,M+1)]
 E0=sumabs(eps);E1=sum((2*j*abs(eps[j-1])for j in range(1,M+1)),F());E2=sum((((2*j)**2+1)*abs(eps[j-1])for j in range(1,M+1)),F())
 vR=sumabs(u[:M+1]);vT=sumabs(u[M+1:2*M+1]);vZ=abs(u[2*M+1]-1)+sumabs(u[2*M+2:])
 delta=E0+3*E1+E2+2*(vR+vT+vZ)
 L=sum((2*j*abs((1-(2*j)**2)*R[j])for j in range(1,M+1)),F())
 B=2/rho+L/rho**2+F(1,2);product=B*delta
 if product>=1:raise ValueError('The Neumann perturbation gate failed')
 inverse=B/(1-product);d0=rho-E1;e0=rho-2*E1;cross=d0*e0-E0*(L+E2)
 if min(d0,e0,cross)<=0 or inverse>=728:raise ValueError('The stated strict core bounds failed')
 values=dict(rho_lower=rho,E0=E0,E1=E1,E2=E2,velocity_R_l1=vR,velocity_T_l1=vT,velocity_Z_minus_one_l1=vZ,
  perturbation_delta=delta,rho_derivative_l1=L,baseline_inverse_bound=B,Neumann_product=product,actual_inverse_bound=inverse,
  dT_lower=d0,minus_eR_lower=e0,normal_z_lower=cross)
 for p,h in expected.items():
  if sha(p)!=h:raise ValueError('Frozen input changed during exact calculation')
 if sha(__file__)!=source:raise ValueError('Source changed')
 out=dict(scope=__doc__,source_sha256=source,inputs={str(p):h for p,h in expected.items()},M=M,N=N,dimension=n,
  exact_core_density_match=True,high_reference_core_coefficients_zero=True,actual_core_planar=True,literal_core_k_zero=True,
  nonzero_binary_left_relation_defects=sum(z!=0 for z in eps),actual_saved_velocity_exact_ez=bool(vR==vT==vZ==0),
  exact_rational_bounds={k:str(v)for k,v in values.items()},approximate_display_only={k:float(v)for k,v in values.items()},
  strict_Neumann_product_below_one=True,strict_inverse_bound_below_728=True,strict_positive_normal_z=True,
  positive_branch_exact_Galerkin_velocity_unique_ez=True,implicit_node_acceleration_Z_exact_zero=True,
  proof_scope='The final two properties also use the exact core/k=0 block equations and the positive-normal-velocity branch, as proved in the companion appendix. Finite-tolerance nodes and all tail points are outside this certificate.',
  numerical_FFT_rounding_certified=False,new_BVP_solved=False,rho_certificate_recomputed=False)
 a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));print(json.dumps(dict(report_sha256=sha(a.out))))
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for k in ('warm','reference','rho-report','rho-source','out'):p.add_argument('--'+k,type=Path,required=True)
 main(p.parse_args())
