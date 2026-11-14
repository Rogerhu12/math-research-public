#!/usr/bin/env python3
"""Exact small checks for the reconstructed R588 table; not a numerical L-value test.
The all-prime representation and Haar-measure arguments remain in the proof.
"""
from fractions import Fraction as Q
from math import factorial
import json,hashlib
from pathlib import Path

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def scale(x,a):return (x[0]*a,x[1]*a)
def conj(x):return (x[0]-x[1],-x[1])
one=(Q(1),Q(0));zero=(Q(0),Q(0));z=(Q(0),Q(1));z2=mul(z,z)
assert add(add(one,z),z2)==zero
v1=[one,scale(z2,-4)];v0=[neg(z2),scale(one,4)]
def T(v):return [mul(z,neg(v[0])),mul(z,add(scale(v[0],-4),v[1]))]
assert T([conj(x) for x in v0])==[neg(x) for x in v0]
assert T([conj(x) for x in v1])==[neg(mul(z,x)) for x in v1]
def norm(c):
 G=[[Q(4,3),Q(-2,3)],[Q(-2,3),Q(4,3)]];a=zero
 for i in range(2):
  for j in range(2):a=add(a,scale(mul(c[i],conj(c[j])),G[i][j]))
 return a
assert norm([one,neg(z2)])==(Q(2),Q(0))
assert norm([neg(z2),one])==(Q(2),Q(0))
# Complete algebraic cancellation of the rational table after
# Omega^2/(sqrt(3)*pi*A)=2/3. The exponents of A,p,(4pi) are in the proof.
base=Q(243*16,9*4*1296)*Q(2,3)
assert base==Q(1,18)
records=[]
for m,target in [(0,Q(1,18)),(2,Q(8))]:
 d=factorial(m)*factorial(m+1);got=base*d*d;assert got==target
 records.append({'m':m,'m_factorial_times_next':d,'norm_coefficient_excluding_Ntheta_and_pplus1':str(got)})
out={'result':'R588 recovered exact local-vector and constant checks','passed':True,'arithmetic':'Fraction in Q[zeta]/(zeta^2+zeta+1)','finite_2_vector_norms':['2','2'],'antilinear_eigenvalues':['-1','-zeta'],'local_factors':{'2':'2/3','3':'1/(3*sqrt(3))','p':'Ntheta/(p+1)^2','infinity':'8*m!*(m+1)!/(4*pi)^(2*m+3)'},'global_torus_volume':'2/(3*sqrt(3))','actual_adelic_CM_value':'y^(m+1)*delta_2^m(F)/(6*p)','finite_projection':'A_T=Tr_T/(p+1)','finite_norm_definition':'Ntheta=G(e0,Tr_T(e0))=(p+1)*G(A_T(e0),A_T(e0))','G':'G(e_r,e_s)=p*delta_rs-1','norm_constants':records,'what_this_checks':['both exact tame conjugation matrices','actual two-old-vector Hermitian norms','rational factor 1/18 and both factorial cases'],'what_this_does_not_replace':['Waldspurger formula','compact-induction support at 3','all-prime finite type and all Haar volumes','analytic-to-algebraic CM period comparison'],'old_p_adic_orbits_repeated':False,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
p=Path(__file__).with_name('R588_exact_normalization_certificate.recovered.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','source_sha256':out['source_sha256'],'certificate':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
