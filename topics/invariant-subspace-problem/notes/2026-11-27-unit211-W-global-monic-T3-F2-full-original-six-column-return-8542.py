#!/usr/bin/env python3
"""Whole remaining W: new original monic T3/F2 six-column system.
After the whole lambda=3/2 exclusion, keep q4 remainder, R6, all original
Gram rows, D^2 individual N, D^3 individual P, and N4(D*Vval).
Every arithmetic product is reduced in the true monic tower and multiplied
back to both original rules. No D/norm inverse and no parameter rank sampling.
180 seconds / 4 GiB. Only frozen construction prefixes are regenerated."""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
dep=Path(__file__).with_name('2026-11-27-unit211-W-global-monic-T4-F2-original-eight-column-return-8542.py')
raw=dep.read_bytes();assert hashlib.sha256(raw).hexdigest()=='af928bbd7240d5235feb3188e65fc8ee5c92aaf8866433a077f1ab96b7507913'
marker=b"\nsay(stage='new_W_actual_monic_T4_F2_same_original_input',"
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
old={'__file__':str(dep),'__name__':'__old_original_construction_only_for_new_six_columns__'}
captured=io.StringIO()
with contextlib.redirect_stdout(captured):exec(compile(prefix,str(dep),'exec'),old)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,P=old['C'],old['P']
e,k,u,Q,ell,M,Phi,P02,bc,J,T0,Pf,d,m,lam,F,S,T,qF,q4,R4,D,K=[
 old[n] for n in ['e','k','u','Q','ell','M','Phi','P02','bc','J','T0','Pf','d','m','lam','F','S','T','qF','qT','R4','D','K']]
original=old['original'];orig=old['ns'];convert=old['convert'];profile=old['profile']
new_atoms=old['paid_atoms']+[T0.n,(J-Q).n,(3-2*lam).n]
den_checked=set()
def paid(v):
 v=C(v);key=str(v.d)
 if key in den_checked:return
 remaining=v.d
 for atom in new_atoms:
  while True:
   g=remaining.gcd(atom)
   if g.total_degree()==0:break
   q=remaining/g;assert q*g==remaining;remaining=q
 assert remaining.total_degree()==0,'unpaid new coefficient denominator'
 den_checked.add(key)
def ppaid(pp):
 for cc in pp.t.values():paid(cc)
theta=8*M*M*u*Q*(3-2*lam)*ell**3*d*(2*u*Q-J)
assert 2*u*Q-J==-Pf/Phi and Pf==T0*(J-Q)
paid(1/theta)
L4=R4.t.get((0,4),C())
r3=R4-q4.scale(L4)
assert r3.t.get((0,3),C())==theta and r3.degree()==3
assert all(mm[0]==0 for mm in r3.t)
q3=r3.scale(1/theta)
assert q3.t.get((0,3),C())==1 and q3.degree()==3
assert q3.scale(theta)+q4.scale(L4)==R4
ppaid(q3);ppaid(qF)
basis=[(0,j) for j in range(3)]+[(1,j) for j in range(3)]
bp=[P.monomial(mm) for mm in basis]
rewrite_count=0
def reduce_poly(pp):
 global rewrite_count
 initial=P(pp);rem=P(pp);tf=P();tt=P()
 while any(mm[0]>=2 for mm in rem.t):
  mm=max((v for v in rem.t if v[0]>=2),key=lambda x:(x[0],x[1]))
  cf=rem.t[mm];term=P.monomial((mm[0]-2,mm[1]),cf)
  rem=rem-term*qF;tf=tf+term
 while any(mm[1]>=3 for mm in rem.t):
  mm=max((v for v in rem.t if v[1]>=3),key=lambda x:(x[1],x[0]))
  cf=rem.t[mm];term=P.monomial((mm[0],mm[1]-3),cf)
  rem=rem-term*q3;tt=tt+term
 assert all(mm in basis for mm in rem.t)
 assert rem+tf*qF+tt*q3==initial
 rewrite_count+=1
 return rem,tf,tt
def digest_parts(parts):
 hh=hashlib.sha256();n=0
 for pp in parts:
  bb=json.dumps(P(pp).data(),separators=(',',':')).encode()
  hh.update(bb);hh.update(b'\n');n+=len(bb)+1
 return dict(bytes=n,sha256=hh.hexdigest())
say(stage='whole_W_new_actual_monic_T3_F2_input',
 originalConstructionPrefixSHA256=hashlib.sha256(prefix).hexdigest(),
 fullTwoOriginalQuarticCombinationActuallyVerified=True,
 monicT3Leading='8*M^2*u*Q*(3-2lambda)*ell^3*d*(2uQ-J)',
 allLeadingFactorsPreviouslyPaid=True,noA143OrB239Inverse=True,
 q3=profile(q3),qF=profile(qF),claimExcluded=False)
# Actual twelve original multiplication columns. The final physical quotient
# is not assumed free; only this ordered monic polynomial environment is free.
maps=[]
for variable,name in [(F,'F'),(S,'S')]:
 ma=[]
 for bb in bp:
  rr,tf,tt=reduce_poly(bb*variable);ppaid(rr);ma.append(rr)
 maps.append(ma)
 say(stage='whole_W_six_column_true_multiplication_complete',variable=name,
     allSixOriginalRuleProductsActuallyReturned=True,
     coefficientCertificate=digest_parts(ma),claimExcluded=False)
class A6:
 def __init__(self,v=0):
  if isinstance(v,A6):self.p=P(v.p);return
  pp=P(v)
  if all(mm in basis for mm in pp.t):self.p=pp
  else:self.p=reduce_poly(pp)[0]
 @classmethod
 def remainder(cls,p):
  assert all(mm in basis for mm in p.t)
  out=cls.__new__(cls);out.p=P(p);return out
 def __bool__(self):return bool(self.p)
 def __neg__(self):return A6.remainder(-self.p)
 def __add__(self,v):v=A6(v);return A6.remainder(self.p+v.p)
 __radd__=__add__
 def __sub__(self,v):return self+-A6(v)
 def __rsub__(self,v):return A6(v)+-self
 def __mul__(self,v):v=A6(v);return A6(self.p*v.p)
 __rmul__=__mul__
 def scale(self,c):return A6.remainder(self.p.scale(C(c)))
 def __pow__(self,n):
  assert n>=0
  out=A6(1);v=self
  while n:
   if n&1:out=out*v
   n//=2
   if n:v=v*v
  return out
 def __eq__(self,v):return self.p==A6(v).p
class E6:
 def __init__(self,a=0,b=0):
  if isinstance(a,E6):self.a=A6(a.a);self.b=A6(a.b);return
  self.a=A6(a);self.b=A6(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __neg__(self):return E6(-self.a,-self.b)
 def __add__(self,v):v=E6(v);return E6(self.a+v.a,self.b+v.b)
 __radd__=__add__
 def __sub__(self,v):return self+-E6(v)
 def __rsub__(self,v):return E6(v)+-self
 def __mul__(self,v):
  v=E6(v);return E6(self.a*v.a+(self.b*v.b).scale(d),self.a*v.b+self.b*v.a)
 __rmul__=__mul__
 def scale(self,c):return E6(self.a.scale(c),self.b.scale(c))
 def __pow__(self,n):
  assert n>=0
  out=E6(1);v=self
  while n:
   if n&1:out=out*v
   n//=2
   if n:v=v*v
  return out
 def conj(self):return E6(self.a,-self.b)
 def __eq__(self,v):v=E6(v);return self.a==v.a and self.b==v.b
def embed_original_extension(v):
 aa=convert(v.a);bb=convert(v.b);ppaid(aa);ppaid(bb)
 return E6(A6(aa),A6(bb))
pointrows=[];labels=[]
def save_row(name,v,route):
 pp=A6(v).p;ppaid(pp)
 pointrows.append(pp);labels.append(name)
 say(stage='whole_W_new_six_column_original_row_mathematical_return',
     name=name,route=route,allSixCoefficientsComputedInTrueOriginalTower=True,
     everyMultiplicationRuleReturnActuallyVerified=True,claimExcluded=False)
 say(stage='whole_W_new_six_column_original_row_profile',
     name=name,normalForm=profile(pp),claimExcluded=False)
for name in ['E1','EBe','EBo','N1','NS','PS']:
 rr,tf,tt=reduce_poly(original[name])
 save_row(name,A6.remainder(rr),'full original polynomial quotient identity')
r2,tf,tt=reduce_poly(q4)
assert r2.degree()<=2 and not tf
save_row('original_value_q4_remainder_r2',A6.remainder(r2),'retained original C4; no quadratic head inverted')
R6=(K*K).scale(M)-(D**3).scale(4*m*m)
rr,tf,tt=reduce_poly(R6)
save_row('original_same_value_second_third_moment_R6',A6.remainder(rr),'full original same-value moment identity')
DQ,TQ,KQ=A6(D),A6(T),A6(K)
D2=DQ*DQ;D3=D2*DQ
hbar=E6(DQ+(DQ*TQ).scale(1/ell)+KQ.scale(1/(2*ell)),
        -KQ.scale(1/(2*m)))
kbar=hbar.conj()
# These are D*hU and D*kU from the same original s=K/(2mD).
# No D division is performed in this source.
Nold,Pold=orig['N4'],orig['P2'];rawGram=orig['rows']
n2raw,n3raw=Nold(rawGram[2]),Nold(rawGram[3])
p2raw,p3raw=Pold(rawGram[2]),Pold(rawGram[3])
assert n3raw==n2raw.conj() and p3raw==p2raw.conj()
n2=embed_original_extension(n2raw);n3=embed_original_extension(n3raw)
p2=embed_original_extension(p2raw);p3=embed_original_extension(p3raw)
DN2=n2*E6(D2)-(hbar**2).scale(2*lam*P02)
DN3=n3*E6(D2)-(kbar**2).scale(2*lam*P02)
assert DN3==DN2.conj()
save_row('D_squared_individual_N_even',DN2.a,'same original hU,kU and D^2 clearing')
save_row('D_squared_individual_N_odd',DN2.b,'both singleton N conditions retained by exact conjugacy')
DP2=p2*E6(D3)-(hbar**3).scale(P02)
DP3=p3*E6(D3)-(kbar**3).scale(P02)
assert DP3==DP2.conj()
save_row('D_cubed_individual_P_even',DP2.a,'same original hU,kU and D^3 clearing')
save_row('D_cubed_individual_P_odd',DP2.b,'both singleton P conditions retained by exact conjugacy')
# N4 is homogeneous quadratic in its vector argument. Its exact diagonal
# and polarization coefficients are built from the original N4 formula.
# Evaluating this quadratic at D*Vval is exactly D^2*N4(Vval).
Eold=orig['E']
vbasis=[[Eold(1 if i==j else 0) for i in range(4)] for j in range(4)]
diagraw=[Nold(v) for v in vbasis]
diag=[embed_original_extension(v) for v in diagraw]
cross={}
for i in range(4):
 for j in range(i+1,4):
  rawij=Nold([vbasis[i][h]+vbasis[j][h] for h in range(4)])-diagraw[i]-diagraw[j]
  cross[(i,j)]=embed_original_extension(rawij)
Dval=[E6(DQ),E6(DQ*(A6(lam-1)-TQ)),hbar,kbar]
NV=E6()
for i in range(4):NV=NV+diag[i]*(Dval[i]**2)
for (i,j),cf in cross.items():NV=NV+cf*Dval[i]*Dval[j]
assert not NV.b
save_row('full_original_N4_D_times_Vval',NV.a,'entire homogeneous original N4(D*Vval), not a Phi multiple')
assert len(pointrows)==13 and len(labels)==13
for rr in pointrows:ppaid(rr)
say(stage='whole_W_monic_T3_F2_full_original_six_column_input_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 scalarVariables=['e','k','lambda'],basis=['1','S','S^2','F','F*S','F*S^2'],
 originalRowLabels=labels,allThirteenNecessaryOriginalRowsActuallyReturned=True,
 allTwelveOriginalMultiplicationColumnsActuallyVerified=True,
 actualOriginalRuleRewriteProducts=rewrite_count,
 allFinalScalarDenominatorsActuallyPaid=True,
 checkedDistinctDenominators=len(den_checked),
 fullIndividualOriginalNPAndFullN4VRepresentedWithDPolynomialClearing=True,
 noPhysicalDOrAnyNormInverse=True,noA143OrB239Inverse=True,
 originalR2LeadingZeroFiberRetained=True,
 orderedMonicAmbientFreeOriginalPhysicalQuotientNotAssumedFree=True,
 coefficientCertificate=digest_parts(pointrows),
 largeRegenerableMatrixCachesWritten=False,
 noParameterCofactorYetComputed=True,wholeWExcluded=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
