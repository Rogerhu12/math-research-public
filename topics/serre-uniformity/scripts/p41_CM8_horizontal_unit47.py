#!/usr/bin/env python3
"""Exact CM(-8) horizontal unit (j-j_T2)/(j-8000), without 47-division.

All formal quotients divide by t before specialization. A separate scalar
six-digit Hensel calculation verifies the four-digit answer after only then
removing the known common factor 47. This is an algebraic branch unit, not a
height or a CM reciprocity assignment.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

P=47

def add(a,b,q,n):return [((a[k] if k<len(a) else 0)+(b[k] if k<len(b) else 0))%q for k in range(n)]
def neg(a,q,n):return [-(a[k] if k<len(a) else 0)%q for k in range(n)]
def scale(a,c,q,n):return [(a[k] if k<len(a) else 0)*c%q for k in range(n)]
def mul(a,b,q,n):return [sum(a[i]*b[k-i] for i in range(k+1) if i<len(a) and k-i<len(b))%q for k in range(n)]
def power(a,e,q,n):
 assert e>=0;v=[1]+[0]*(n-1)
 while e:
  if e&1:v=mul(v,a,q,n)
  a,e=mul(a,a,q,n),e//2
 return v
def inverse(a,q,n):
 v=[pow(a[0],-1,q)]
 for k in range(1,n):v.append(-v[0]*sum(a[i]*v[k-i] for i in range(1,k+1) if i<len(a))%q)
 return v
def compose(a,b,q,n):
 assert b[0]==0;v=[0]*n
 for c in reversed(a):v=mul(v,b,q,n);v[0]=(v[0]+c)%q
 return v
def evaluate(a,x,q):
 v=0
 for c in reversed(a):v=(v*x+c)%q
 return v
def jseries(A,B,q,n):
 A3=power(A,3,q,n);den=add(scale(A3,4,q,n),scale(power(B,2,q,n),27,q,n),q,n)
 return scale(mul(A3,inverse(den,q,n),q,n),6912,q,n)
def logunit(u,q):
 z=(pow(u,46,q)-1)%q;assert z%47==0
 # All callers use q=47^4.
 return (z-z*z*pow(2,-1,q)+z*z*z*pow(3,-1,q))*pow(46,-1,q)%q

def horizontal_unit_certificate(jvalue):
 Q=47**4;N=5;A=[-30%Q]+[0]*4;B=[56,1,0,0,0];r=[4,0,0,0,0]
 for k in range(1,N):
  residual=add(add(power(r,3,Q,N),mul(A,r,Q,N),Q,N),B,Q,N)
  r[k]=-residual[k]*pow(18,-1,Q)%Q
 assert add(add(power(r,3,Q,N),mul(A,r,Q,N),Q,N),B,Q,N)==[0]*N
 At=add(scale(A,-4,Q,N),scale(power(r,2,Q,N),-15,Q,N),Q,N)
 Bt=add(scale(B,22,Q,N),scale(mul(A,r,Q,N),14,Q,N),Q,N)
 assert At[0]==-120%Q and Bt[0]==-448%Q
 js,jt=jseries(A,B,Q,N),jseries(At,Bt,Q,N)
 assert js[0]==jt[0]==8000 and jt[1]==-js[1]%Q
 delta=list(js);delta[0]=0
 numerator=add(js,neg(jt,Q,N),Q,N);assert numerator[0]==0
 Uphysical=mul(numerator[1:],inverse(delta[1:],Q,4),Q,4)
 inverse_j=[0,pow(js[1],-1,Q),0,0,0]
 for k in range(2,N):inverse_j[k]=-compose(delta,inverse_j,Q,N)[k]*pow(js[1],-1,Q)%Q
 assert compose(delta,inverse_j,Q,N)==[0,1,0,0,0]
 Uj=compose(Uphysical,inverse_j,Q,4)
 target_in_j=compose(jt,inverse_j,Q,N)
 assert Uj==[(1-target_in_j[1])%Q]+[-v%Q for v in target_in_j[2:]]
 assert Uj[0]==2
 displacement=(int(jvalue)-8000)%Q;assert displacement%47==0
 value=evaluate(Uj,displacement,Q);assert value%47==2
 # Independent finite-ring Newton calculations at six digits. The arbitrary
 # fifth digit of j cannot affect this analytic unit modulo four digits.
 checks=[];Q6=47**6
 for extra in [0,1]:
  jl=int(jvalue)+extra*Q;A0=-30
  B2=pow(A0,3,Q6)*(6912*pow(jl,-1,Q6)-4)*pow(27,-1,Q6)%Q6
  b=56
  for _ in range(4):b=(b+ B2*pow(b,-1,Q6))*pow(2,-1,Q6)%Q6
  assert b*b%Q6==B2
  root=4
  for _ in range(4):root=(root-(root**3+A0*root+b)*pow(3*root*root+A0,-1,Q6))%Q6
  assert (root**3+A0*root+b)%Q6==0
  ap=(-4*A0-15*root*root)%Q6;bp=(22*b+14*A0*root)%Q6
  jtarget=6912*pow(ap,3,Q6)*pow((4*pow(ap,3,Q6)+27*bp*bp)%Q6,-1,Q6)%Q6
  den=(jl-8000)%Q6;num=(jl-jtarget)%Q6
  v=0;dd=den
  while dd%47==0 and dd:v+=1;dd//=47
  assert v==1 and num%(47**v)==0
  quotient=(num//(47**v))*pow(den//(47**v),-1,Q6//(47**v))%(Q6//(47**v))
  assert quotient%Q==value
  checks.append({'chosen_j_lift_mod47six':jl,'A':A0,'B_mod47six':b,'kernel_root_mod47six':root,'target_j_mod47six':jtarget,'common_47_valuation':v,'quotient_mod47five':quotient,'four_digit_quotient_matches_formal_unit':True})
 assert checks[0]['target_j_mod47six']%Q==checks[1]['target_j_mod47six']%Q
 return {'model_at_CM8':{'A':-30,'B':56,'j':8000,'kernel_root':4,'target_A':-120,'target_B':-448},
 'formal_parameter':'A=-30, B=56+t; Delta=j-8000 is the etale j-parameter',
 'kernel_r_coefficients_0to4_mod47four':r,'source_j_coefficients_0to4_in_t_mod47four':js,'target_j_coefficients_0to4_in_t_mod47four':jt,
 't_coefficients_0to4_in_Delta_j_mod47four':inverse_j,'target_j_coefficients_0to4_in_Delta_j_mod47four':target_in_j,
 'horizontal_derivative_in_j_at_CM8':-1,'U_coefficients_0to3_in_t_mod47four':Uphysical,
 'U_coefficients_0to3_in_Delta_j_mod47four':Uj,'source_j_mod47four':int(jvalue)%Q,'source_Delta_j_mod47four':displacement,
 'U_mod47four':value,'log_U_mod47four':logunit(value,Q),'formal_t_factor_removed_before_evaluation':True,
 'independent_six_digit_Newton_checks':checks,'four_digit_precision_is_independent_of_the_chosen_fifth_j_digit':True,
 'scope':'Actual algebraic CM(-8) 2-isogeny branch unit only; no local height constant assigned.'}

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--j',type=int,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 x=horizontal_unit_certificate(args.j);x['result']='R367';x['modulus']=47**4;x['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 raw=(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode();args.output.write_bytes(gzip.compress(raw,mtime=0))
 print('PASS actual horizontal CM8 unit',x['U_mod47four'],'log',x['log_U_mod47four'],'SHA',hashlib.sha256(args.output.read_bytes()).hexdigest())
if __name__=='__main__':main()
