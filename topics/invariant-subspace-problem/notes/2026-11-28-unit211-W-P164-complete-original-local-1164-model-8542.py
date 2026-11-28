#!/usr/bin/env python3
"""NEW complete P164 finite local model, with all original I11 conditions.
The already proved integral e97 model over
A=Z_(1009)[k]_(1009,k-3), then true monic chi_lambda6 and q_Z2,
gives a finite FREE polynomial environment of rank 1164 over A.
Only if every weight denominator is a true unit in the ENTIRE residue
weight algebra and ALL primary components return the original unit 1,
finite-cokernel Nakayama excludes the QQ(k) generic original system.
No geometric D inverse, no modular D-power lifting, no lambda leading
inverse, no original quotient freeness, no old norm/resultant gate.
180s /4GiB; no coefficient/cache/encoded/split payload output.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import nmod_poly,fmpq
started=time.perf_counter();deadline=started+180
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
prime=1009;fixed_k=3
def say(**kw):
 kw['seconds']=time.perf_counter()-started
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def mp(p):
 return dict(degree=int(p.degree()),**digest([int(c) for c in p.coeffs()]))
def source_prefix(name,fullsha,marker,nbytes,presha):
 path=Path(__file__).with_name(name);raw=path.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==fullsha
 assert raw.count(marker)==1
 pre=raw.split(marker)[0]
 assert len(pre)==nbytes and hashlib.sha256(pre).hexdigest()==presha
 ns={'__file__':str(path),'__name__':'new_complete_local_finite_original_model'}
 oldalarm=signal.alarm;oldtimer=signal.setitimer
 def timer(which,seconds,interval=0.0):
  if which!=signal.ITIMER_REAL:return oldtimer(which,seconds,interval)
  assert not interval
  left=max(.001,deadline-time.perf_counter())
  return oldtimer(which,min(left,float(seconds) if seconds>0 else left),0.0)
 def alarm(seconds):
  old=timer(signal.ITIMER_REAL,seconds);return math.ceil(old[0])
 signal.alarm=alarm;signal.setitimer=timer
 try:
  with contextlib.redirect_stdout(io.StringIO()):
   exec(compile(pre,str(path)+'#necessary_definition_only','exec'),ns)
 finally:
  signal.alarm=oldalarm;signal.setitimer=oldtimer
 oldtimer(signal.ITIMER_REAL,max(.001,deadline-time.perf_counter()))
 return ns
# Only the exact mod P definition is needed.  Skip the already completed
# QQ e=2,3,5 vertical-component return and every old determinant tail.
pp=source_prefix(
 '2026-11-28-unit211-W-native-P164-fixed-integral-slice-and-original-vertical-content-8542.py',
 'f99bfbb7612bf53d9f9326b76d6d6f210be5a342d6c513cc96cb9ebbf786bab3',
 b'\n# A genuinely new QQ vertical-content test.',7922,
 '2a472842e709377b6ef7cc496492a2fe602af88c64f2469a8522f2d06b6c6d54')
assert pp['degree_preserving_slice']
modulus=pp['slice_monic']
assert mp(modulus)==dict(degree=97,bytes=380,sha256='ebe334f55739f723b57d093e4b990bdf53e2be2b05758edce7324d98ab5c7b93')
native=pp['native'];cn=native['ns']
# Only the original N1 coordinate and qZ definition; skip all previous
# twenty-row construction and the two large scalar targets.
val=source_prefix(
 '2026-11-28-unit211-W-H198-full-original-values-first-mean-reduction-twenty-two-model-8542.py',
 'f6f07b2f3fdb50f59565ef6501cbc2121d5882ce7cb32f7d17a4a1d2d139b6a1',
 b'\n# The exact I4 construction:',5551,
 '9a6f12dad89cc77c651f902bf881b53eca708cd8f0dcfab2961dabb089ed3523')
phys=val['phys'];old=val['old'];original=val['original']
# Native same-lambda multiplication, the coefficient definition of the
# previously proved global characteristic relation. No QQ Faddeev tail.
NR=cn['R'];basis=cn['basis'];variables=cn['variables']
mats=cn['matrices'];errs=cn['errors'];old_original=cn['original']
lc=cn['coeffmap'](cn['symbolic']['lam'])
mons=[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
assert set(lc).issubset(set(mons))
alpha=[lc.get(mm,NR()) for mm in mons]
ML=[[alpha[0]*int(i==j)+sum((alpha[a+1]*mats[a][i][j] for a in range(3)),NR())
     for j in range(6)] for i in range(6)]
EL=[[sum((alpha[a+1]*errs[a][i][g] for a in range(3)),NR())
     for g in range(4)] for i in range(6)]
for i in range(6):
 assert cn['symbolic']['lam']*basis[i]-sum((ML[i][j]*basis[j] for j in range(6)),NR())==sum((EL[i][g]*old_original[g] for g in range(4)),NR())
 for co in ML[i]:native['paid_scalar'](co)
 for co in EL[i]:native['paid_poly'](co.d)
# Original rational geometry bases; no mean reduction or value cofactor.
Nold,Pold,Eold=old['N4'],old['P2'],old['E']
nb=Nold(old['rows'][2]).b;pb=Pold(old['rows'][2]).b
l0=old['l'];m0=old['u']-l0;t0=old['T'];lam0=old['lam']
V0=[Eold(1),Eold(lam0-1-t0),Eold(1+t0/l0),Eold(1+t0/l0)]
V1=[Eold(),Eold(),Eold(m0/l0,-1),Eold(m0/l0,1)]
zz0=Nold(V0);zz2=Nold(V1)
zz1=Nold([V0[j]+V1[j] for j in range(4)])-zz0-zz2
assert not zz0.b and not zz1.b and not zz2.b
for co in [old['u'],old['Q'],l0,m0,1-old['Q'],old['M']]:
 val['pay'](co.n);val['pay'](co.d)
val['pay_chart'](val['Delta'].n);val['pay_chart'](val['Delta'].d)
say(stage='new_complete_P164_local_model_definitions',
 exactWeightResidue=mp(modulus),
 base='Z_(1009)[k]_(1009,k-3)',
 weightRank=97,lambdaRank=6,ZRank=2,freePolynomialEnvironmentRank=1164,
 sameOriginalLambdaSixProductsReturned=True,
 completeOddNandPAndEntireN4VOriginalDefinitions=True,
 noQQCharacteristicOrOldTwentyRowCofactorReplayed=True,
 originalDNotInverted=True,wholeWExcluded=False)

zA=nmod_poly([],prime);oA=nmod_poly([1],prime)
def aa(p):return p%modulus
def am(a,b):return (a*b)%modulus
inverse_count=0;integral_count=0;den_cache={}
class ModelFailure(Exception):
 def __init__(self,reason,detail):
  super().__init__(reason);self.reason=reason;self.detail=detail
def apart(c):
 ss=str(c).split('/')
 return int(ss[0]),(int(ss[1]) if len(ss)==2 else 1)
def vp(n):
 assert n;n=abs(n);v=0
 while n%prime==0:n//=prime;v+=1
 return v
def cval(c):
 a,b=apart(c);assert a
 return vp(a)-vp(b)
def scale_p(v):
 return fmpq(1,prime**v) if v>=0 else fmpq(prime**(-v))
def residue(c):
 global integral_count
 a,b=apart(c)
 if b%prime==0:
  raise ModelFailure('actual_QQ_coefficient_not_p_integral_after_common_denominator_normalization',
                     dict(rationalDefinition=digest(str(c))))
 integral_count+=1
 return a%prime*pow(b%prime,prime-2,prime)%prime
def inverse(a,where):
 global inverse_count
 a=aa(a)
 gg,s,t=a.xgcd(modulus)
 assert s*a+t*modulus==gg
 if gg.degree()!=0:
  raise ModelFailure('weight_denominator_not_unit_in_entire_P_residue',
                     dict(where=where,denominator=mp(a),nonunitGcd=mp(gg)))
 s=s*pow(int(gg[0]),prime-2,prime);s=aa(s)
 assert am(a,s)==oA
 inverse_count+=1
 return s
def groups(co):
 # Rational polynomial in the three geometry slots. Normalize the
 # WHOLE denominator p-content, then verify every numerator coefficient.
 if not hasattr(co,'n'):co=NR(co)
 assert all(not any(mm[j] for j in range(2,len(mm))) for mm in co.d.to_dict())
 key=str(co.d)
 if key in den_cache:sc,di=den_cache[key]
 else:
  v=min(cval(c) for c in co.d.to_dict().values() if c)
  sc=scale_p(v)
  arr=[0]*(max((int(mm[0]) for mm in co.d.to_dict()),default=-1)+1)
  for mm,c in co.d.to_dict().items():
   arr[int(mm[0])]=(arr[int(mm[0])]+residue(c*sc)*pow(fixed_k,int(mm[1]),prime))%prime
  den=aa(nmod_poly(arr,prime));di=inverse(den,'QQ rational-polynomial weight denominator')
  den_cache[key]=(sc,di)
 arrays={}
 deg=max((int(mm[0]) for mm in co.n.to_dict()),default=-1)
 for mm,c in co.n.to_dict().items():
  assert not any(mm[j] for j in range(5,len(mm)))
  mon=tuple(int(mm[j]) for j in [2,3,4])
  arr=arrays.setdefault(mon,[0]*(deg+1))
  ie,ik=int(mm[0]),int(mm[1])
  arr[ie]=(arr[ie]+residue(c*sc)*pow(fixed_k,ik,prime))%prime
 return {mon:am(nmod_poly(arr,prime),di) for mon,arr in arrays.items()}
def weight(co):
 gg=groups(co)
 assert all(mon==(0,0,0) for mon in gg)
 return gg.get((0,0,0),zA)
def matmul(A,B):
 return [[sum((am(A[i][h],B[h][j]) for h in range(6)),zA)%modulus
          for j in range(6)] for i in range(6)]
def run_model():
 # Every inverse is in the ENTIRE e97 algebra, not a selected field.
 M=[[weight(c) for c in row] for row in ML]
 I=[[oA if i==j else zA for j in range(6)] for i in range(6)]
 B=I;descending=[oA]
 for j in range(1,7):
  NB=matmul(M,B)
  tr=sum((NB[i][i] for i in range(6)),zA)%modulus
  cc=aa(-pow(j,prime-2,prime)*tr)
  assert aa(j*cc)==-tr
  B=[[aa(NB[i][h]+(cc if i==h else zA)) for h in range(6)] for i in range(6)]
  descending.append(cc)
 assert not any(c for row in B for c in row)
 chi=list(reversed(descending));assert chi[-1]==oA
 say(stage='new_complete_P164_same_lambda_monic_six_residue',
  exactSameOriginalCharacteristicViaUniversalFaddeev=True,
  characteristicDegree=6,leadingOne=True,
  B6ActuallyZero=True,allIntegerTraceDivisionsReturned=True,
  entireWeightAlgebraUsed=True,
  chiDefinition=digest([[int(c) for c in p.coeffs()] for p in chi]),
  currentWeightInverses=inverse_count,wholeWExcluded=False)
 def ez():return [zA]*6
 def es(a):
  return [aa(a),zA,zA,zA,zA,zA]
 def eadd(a,b):return [aa(a[j]+b[j]) for j in range(6)]
 def eneg(a):return [-c for c in a]
 def escale(a,c):return [am(x,c) for x in a]
 def emul(a,b):
  if not any(a) or not any(b):return ez()
  if not any(b[1:]):return escale(a,b[0])
  if not any(a[1:]):return escale(b,a[0])
  tmp=[zA]*11
  for i in range(6):
   if a[i]:
    for j in range(6):
     if b[j]:tmp[i+j]=aa(tmp[i+j]+am(a[i],b[j]))
  for j in range(10,5,-1):
   if tmp[j]:
    co=tmp[j]
    for t in range(6):tmp[j-6+t]=aa(tmp[j-6+t]-am(co,chi[t]))
   tmp[j]=zA
  return tmp[:6]
 def epow(a,n):
  out=es(oA)
  while n:
   if n&1:out=emul(out,a)
   n//=2
   if n:a=emul(a,a)
  return out
 L6=[zA,oA,zA,zA,zA,zA]
 def lco(co):
  gg=groups(co);out=ez()
  for mon,a in gg.items():
   assert mon[0]==mon[1]==0
   out=eadd(out,escale(epow(L6,mon[2]),a))
  return out
 beta0=lco(val['beta0']);beta1=lco(val['beta1'])
 class C:
  __slots__=('a','b')
  def __init__(self,value=0):
   if isinstance(value,C):self.a=value.a;self.b=value.b;return
   if isinstance(value,nmod_poly):co=aa(value)
   else:co=nmod_poly([residue(value)],prime)
   self.a=es(co);self.b=ez()
  @classmethod
  def pair(cls,a,b):
   out=object.__new__(cls);out.a=a;out.b=b;return out
  def __bool__(self):return any(self.a) or any(self.b)
  def __eq__(self,other):
   other=C(other);return self.a==other.a and self.b==other.b
  def __neg__(self):return C.pair(eneg(self.a),eneg(self.b))
  def __add__(self,other):
   other=C(other);return C.pair(eadd(self.a,other.a),eadd(self.b,other.b))
  __radd__=__add__
  def __sub__(self,other):return self+-C(other)
  def __rsub__(self,other):return C(other)+-self
  def __mul__(self,other):
   other=C(other)
   aa0=emul(self.a,other.a)
   cross=eadd(emul(self.a,other.b),emul(self.b,other.a))
   bb=emul(self.b,other.b)
   return C.pair(eadd(aa0,eneg(emul(beta0,bb))),
                 eadd(cross,eneg(emul(beta1,bb))))
  __rmul__=__mul__
  def __truediv__(self,other):
   other=C(other)
   assert not any(other.b) and not any(other.a[1:]),'no geometric inverse'
   inv=inverse(other.a[0],'explicit original pure-weight divisor')
   return C.pair(escale(self.a,inv),escale(self.b,inv))
  def __pow__(self,n):
   assert n>=0
   out=C(1);base=self
   while n:
    if n&1:out=out*base
    n//=2
    if n:base=base*base
   return out
  def vector(self):return self.a+self.b
 L=C.pair(L6,ez());Z=C.pair(ez(),es(oA))
 def coeff(co):return C.pair(lco(co),ez())
 def evalpoly(co,images):
  gg=groups(co);maxd=[max((m[j] for m in gg),default=0) for j in range(3)]
  powers=[]
  for j in range(3):
   rr=[C(1)]
   for k in range(maxd[j]):rr.append(rr[-1]*images[j])
   powers.append(rr)
  out=C()
  for mon,coefficient in gg.items():
   value=C(coefficient)
   for j in range(3):value=value*powers[j][mon[j]]
   out=out+value
  return out
 a,c=weight(val['aa']),weight(val['cc'])
 dn=weight(val['Delta'])
 dn_inv=inverse(dn,'entire original N1 coordinate determinant H198')
 p0,p1,p2=[coeff(p) for p in val['ns']['nrow']]
 X=(p2*Z+C(c)*p0)*C(dn_inv)
 Y=(-p1*Z-C(a)*p0)*C(dn_inv)
 assert p0+p1*X+p2*Y==0
 assert C(a)*X+C(c)*Y==Z
 assert Z*Z+C.pair(beta1,ez())*Z+C.pair(beta0,ez())==0
 tvalue=evalpoly(phys['tnew'],[X,Y,L])
 assert evalpoly(old['lam'],[X,Y,tvalue])==L
 generators=[evalpoly(ff,[X,Y,L]) for ff in original]
 labels=['E1','EBe','EBo','N1','NS','PS']
 ntag=val['ntag'];ztag=val['ns']['ztag']
 assert generators[3]+sum((coeff(ntag[i])*generators[i] for i in range(3)),C())==0
 assert sum((coeff(ztag[i])*generators[i] for i in range(3)),C())==0
 def oldeval(pp):return evalpoly(pp,[X,Y,tvalue])
 u,Q,ell,M,P02,J=[C(weight(old[key])) for key in ['u','Q','l','M','P02','J']]
 m=u-ell;delta=1-Q
 # Assert the exact original weight divisors, before any original value.
 for unit in [m,u,Q,ell,delta,M]:assert unit*(C(1)/unit)==1
 T=oldeval(old['T'])
 Al=2*L*L-2*L+1;Bl=4*L**3-6*L*L+3*L-1
 D=ell*Al-T*T;K=ell*ell*Bl-3*ell*T*Al+2*T**3
 Ast=4*u*Q-J;Cst=Ast*m*m+J*delta*ell*ell;cval=3-2*L
 ad=M*ell*ell*Q*(3-4*L)+M*Ast*T*T+2*M*u*Q*cval*ell*T+Cst*D
 bd=2*M*m*(Ast*T+u*Q*cval*ell)
 qt=(2*m*D*ad+K*bd)/(8*m*u*Q*ell*ell*delta)
 R6=M*K*K-4*m*m*D**3
 A0=1+T/ell
 Nlow=D*oldeval(nb)+(2*L*P02/m)*K*A0+(4*L*P02*m/(ell*M))*D*D
 Plow=D*oldeval(pb)+(3*P02/(2*m))*K*A0*A0
 Plow=Plow+(P02*(3*m*m/(ell*ell)+delta)/(2*m*M))*K*D+(6*P02*m/(ell*M))*A0*D*D
 Vlow=D*oldeval(zz0.a)+(K*oldeval(zz1.a))/(2*m)+(D*D*oldeval(zz2.a))/M
 generators += [qt,R6,Nlow,Plow,Vlow]
 labels += ['qT4','R6','Nlow','Plow','entire_Vlow']
 assert len(generators)==11
 monomials=[L**j for j in range(6)]+[Z*(L**j) for j in range(6)]
 columns=[];definitions=[]
 for name,gen in zip(labels,generators):
  for j,monomial in enumerate(monomials):
   columns.append((gen*monomial).vector());definitions.append([name,j])
 assert len(columns)==132 and all(len(v)==12 for v in columns)
 matrix_digest=digest([[[int(c) for c in p.coeffs()] for p in col] for col in columns])
 say(stage='new_complete_original_I11_in_1164_free_polynomial_environment',
  allElevenOriginalConditions=labels,actualColumns=132,actualRows=12,
  entireWeightDegree=97,monomialBasis='lambda^j Z^epsilon:0<=j<6,0<=epsilon<2',
  originalN1AndMonicQZSubstitutionIdentitiesActuallyReturned=True,
  sameOriginalPhysicalLambdaAndTActuallyRecovered=True,
  originalValuesComputedDirectlyBeforeAnyIdealSaturation=True,
  noOriginalDOrLambdaLeadingInverse=True,
  exactColumnDefinition=matrix_digest,
  weightInverses=inverse_count,checkedPIntegralCoefficients=integral_count,
  allDenominatorsUnitInEntireWeightAlgebra=True,
  originalQuotientFree=False,wholeWExcluded=False)
 # Full primary factorization, retaining every power. Never interpret
 # one of these finite-field factors as a QQ factor.
 scalar,factors=modulus.factor()
 factors=sorted([(f,int(mult)) for f,mult in factors],
                key=lambda fm:(fm[0].degree(),tuple(int(c) for c in fm[0].coeffs())))
 prod=nmod_poly([int(scalar)],prime)
 for f,mult in factors:
  assert f and f[f.degree()]==1 and mult>0
  prod*=f**mult
 assert prod==modulus
 def powmod(a,n,h):
  ans=nmod_poly([1],prime);a=a%h
  while n:
   if n&1:ans=(ans*a)%h
   n//=2
   if n:a=(a*a)%h
  return ans
 def prime_divisors(n):
  out=[];d=2
  while d*d<=n:
   if n%d==0:
    out.append(d)
    while n%d==0:n//=d
   d+=1
  if n>1:out.append(n)
  return out
 xp=nmod_poly([0,1],prime)
 for index,(f,mult) in enumerate(factors):
  degree=int(f.degree());powers={0:xp%f};cur=xp%f
  for j in range(1,degree+1):
   cur=powmod(cur,prime,f);powers[j]=cur
  assert powers[degree]==xp%f
  for q in prime_divisors(degree):
   assert (powers[degree//q]-xp).gcd(f).degree()==0
  for g,_ in factors[:index]:assert g.gcd(f).degree()==0
 say(stage='new_full_P164_primary_residue_cover_verified',
  factors=[dict(index=i,irreducible=mp(f),multiplicity=m,
                primaryDegree=int(f.degree())*m) for i,(f,m) in enumerate(factors)],
  allRabinConditionsActuallyVerified=True,
  fullProductReturned=True,allPowersRetained=True,
  noneTreatedAsQQFactors=True,wholeWExcluded=False)
 global_coefficients=[zA]*len(columns);idempotents=[];block_records=[]
 all_units=True
 for index,(f,mult) in enumerate(factors):
  h=f**mult;degree=int(h.degree())
  z=nmod_poly([],prime);o=nmod_poly([1],prime)
  def product(a,b):return (a*b)%h
  invs=0
  def invprimary(a):
   nonlocal invs
   gg,s,t=a.xgcd(h);assert s*a+t*h==gg
   assert gg.degree()==0
   out=(s*pow(int(gg[0]),prime-2,prime))%h
   assert product(a,out)==o;invs+=1
   return out
  original_cols=[[p%h for p in col] for col in columns]
  selected=[];pivots={}
  for column_index,col in enumerate(original_cols):
   v=col[:];comb=[z]*12;comb[len(selected)]=o
   for pos in sorted(pivots):
    bv,bc=pivots[pos];co=v[pos]
    if co:
     v=[(v[i]-product(co,bv[i]))%h for i in range(12)]
     comb=[(comb[i]-product(co,bc[i]))%h for i in range(12)]
   pos=next((i for i in range(12) if i not in pivots and v[i].gcd(f).degree()==0),None)
   if pos is None:continue
   inv=invprimary(v[pos])
   v=[product(q,inv) for q in v];comb=[product(q,inv) for q in comb]
   assert v[pos]==o
   selected.append(column_index)
   for oldpos,(bv,bc) in list(pivots.items()):
    co=bv[pos]
    if co:
     pivots[oldpos]=([(bv[i]-product(co,v[i]))%h for i in range(12)],
                     [(bc[i]-product(co,comb[i]))%h for i in range(12)])
   pivots[pos]=(v,comb)
   if len(selected)==12:break
  full=len(selected)==12
  if full:
   for pos in range(12):
    v,comb=pivots[pos]
    assert v==[o if i==pos else z for i in range(12)]
    for i in range(12):
     ret=sum((product(comb[j],original_cols[selected[j]][i]) for j in range(12)),z)%h
     assert ret==(o if i==pos else z)
   unitcomb=pivots[0][1]
   quotient,remainder=divmod(modulus,h)
   assert not remainder and quotient*h==modulus
   ei=aa(quotient*invprimary(quotient%h))
   assert ei%h==o and am(ei,ei)==ei
   idempotents.append(ei)
   for j,colindex in enumerate(selected):
    global_coefficients[colindex]=aa(global_coefficients[colindex]+am(ei,unitcomb[j]))
   certificate=digest([[[int(c) for c in p.coeffs()] for p in pivots[pos][1]] for pos in range(12)])
  else:
   all_units=False;certificate=None
  record=dict(index=index,irreducibleDegree=int(f.degree()),multiplicity=mult,
   primaryDegree=degree,rankOverResidueField=len(selected),
   actualFullPrimaryUnitReturn=full,
   selectedOriginalColumns=[definitions[i] for i in selected],
   all144OriginalMatrixProductsReturned=full,
   primaryInverses=invs,certificate=certificate)
  block_records.append(record)
  say(stage='new_original_I11_full_primary_matrix_return',**record,
      noDInverseOrDPowerPromotion=True,
      allNonunitOrRankDeficientSupportRetained=not full,wholeWExcluded=False)
 if all_units:
  assert sum(idempotents,zA)%modulus==oA
  for i,ei in enumerate(idempotents):
   for ej in idempotents[:i]:assert not am(ei,ej)
  for coordinate in range(12):
   ret=sum((am(global_coefficients[j],columns[j][coordinate]) for j in range(len(columns))),zA)%modulus
   assert ret==(oA if coordinate==0 else zA)
  say(stage='new_complete_P164_generic_original_unit_by_integral_Nakayama',
   exactWholeWeightPrimaryCRTProductAndSumReturned=True,
   actualGlobalOriginal132ColumnCombinationEqualsOne=True,
   actualGlobalCertificate=digest([[int(c) for c in p.coeffs()] for p in global_coefficients]),
   finiteFreeEnvironmentOverLocalA=1164,
   allWeightDenominatorsBecomeUnitsInBOverLocalAByFiniteNakayama=True,
   finiteCokernelZeroModuloMaximalIdealImpliesZeroOverLocalA=True,
   entireQQkOriginalP164GenericSystemExcluded=True,
   previousNoQQPureKContentTheoremRequired=True,
   remainingWWeightSupportZeroDimensionalAfterPreviouslyFiniteH198Branch=True,
   finiteWeightOrGeometricPointsStillRequireOriginalReturns=True,
   noExplicitQQUnitCombinationOrFiniteKCoverClaimed=True,
   allOriginalDNonzeroScopeRetainedWithoutDInverse=True,
   wholeWExcluded=False)
 else:
  say(stage='accurate_new_complete_finite_model_retains_primary_support',
      unresolved=[r for r in block_records if not r['actualFullPrimaryUnitReturn']],
      noQQGenericExclusionOrZeroDimensionalClaim=True,
      noRetryPrimeKOrderOrBudget=True,wholeWExcluded=False)
 return all_units
try:
 success=run_model()
except ModelFailure as exc:
 success=False
 say(stage='accurate_new_integral_model_not_paid',reason=exc.reason,detail=exc.detail,
     entireObstructedSupportRetained=True,noQQGenericExclusionOrZeroDimensionalClaim=True,
     noAlternativePrimeKOrDenominatorSaturation=True,wholeWExcluded=False)
say(stage='new_complete_P164_local_original_model_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 wholeGenericOriginalModelUnitActuallyReturned=success,
 noOldQQNormResultantOrCofactorGateReplayed=True,
 noGeometricDInverseOrModDPowerLift=True,
 noEncodedSplitOrCoefficientCacheSaved=True,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False,wholeWExcluded=False)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
