#!/usr/bin/env python3
"""W/J19: new finite original 48x35 return on the entire QQ F588 cover away
from explicitly retained original weight-norm fibers.  A complete modular
constant-algebra full-column-rank proof is lifted only by finite-module Gauss.
The frozen source is used solely to regenerate the exact published F588 and
same original Gram coefficients; no old result is made a new completion gate.
180 seconds / 4 GiB.  Only small profiles and certificate hashes are emitted.
"""
import json,time,hashlib,signal,resource,math,contextlib,io
from pathlib import Path
from fractions import Fraction
from flint import fmpq_poly,fmpq,nmod_poly,fmpz_mod_poly_ctx,fq_default_ctx,fq_default_poly_ctx
start=time.perf_counter();deadline=start+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
def coefficients(pp):return [str(c) for c in pp.coeffs()]
def qexact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a;return q
P=lambda v=():fmpq_poly([fmpq(x) for x in v])
one=P([1]);kk=P([0,1])
def sf(pp):
 assert pp
 if pp.degree()==0:return one
 qq=qexact(pp,pp.gcd(pp.derivative()));return qq/qq[qq.degree()]
def digest_json(obj):
 bb=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
def report_poly(pp):
 co=coefficients(pp);out=dict(degree=int(pp.degree()),**digest_json(co))
 if out['bytes']<=8192:out['coefficients']=co
 return out
dependency=Path(__file__).with_name('2026-11-27-unit211-generic-LS-W-J19-quartic-six-generator-original-finite-cover-8542.py')
raw=dependency.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='f43664bf12637f8add0a01589a854d2cafe22a2711b7dfd826752f90831aa784'
ns={'__file__':str(dependency),'__name__':'__necessary_published_cover_regeneration__'}
captured=io.StringIO()
with contextlib.redirect_stdout(captured):exec(compile(raw,str(dependency),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
cover=ns['cover']
assert cover.degree()==588 and cover[588]==1 and cover.gcd(cover.derivative()).degree()==0
assert digest_json(coefficients(cover))['sha256']=='7bea5212e64f8a52cc8d6dc82a229d65596654cf7e5c73d91ccea2071b0ff9b1'
original=ns['original'];GA=ns['A'];detP=ns['detP'];R=ns['R'];F=ns['F']
names=ns['names'];k,e,u,Q,V,ell,d,bc,P02,Phi,T0,J,M=[ns[x] for x in ['k','e','u','Q','V','ell','d','bc','P02','Phi','T0','J','M']]
say(stage='new_J19_finite_return_exact_input_regenerated',publishedCoverDegree=588,publishedCoverSHA256='7bea5212e64f8a52cc8d6dc82a229d65596654cf7e5c73d91ccea2071b0ff9b1',dependencySourceSHA256='f43664bf12637f8add0a01589a854d2cafe22a2711b7dfd826752f90831aa784',regenerationLogSHA256=hashlib.sha256(captured.getvalue().encode()).hexdigest(),newReturnInput='fixed original degree-four Macaulay rows at finite k',oldSourceNotUsedAsNewResultGate=True,claimExcluded=False)
basis=[GA([0]*j+[1]) for j in range(4)]
def norm(v):
 cols=[v*z for z in basis];den=one
 for col in cols:den*=qexact(col.d,den.gcd(col.d))
 mat=[[cols[j].n[i]*qexact(den,cols[j].d) for j in range(4)] for i in range(4)]
 return R(detP(mat),den**4)
H=4*e*k-k*k-4*k-8
C9=4*e*e*k*k-e*(k**4+9*k**3+20*k*k+16*k)+k**3+10*k*k+24*k+16
paid=[('k',k),('k+1',k+1),('k+2',k+2),('k+4',k+4),('e',e),('u',u),('Q',Q),('V',V),('1-Q',d),('bc',bc),('P02',P02),('Phi',Phi),('ell',ell),('ell-u',ell-u),('Q-2',Q-2),('u-Q',u-Q),('H',H),('C9',C9),('2e+1',2*e+1),('T0',T0),('J-Q',J-Q)]
normcover=one;normprofiles=[];integral_arrays=[cover]
def include(pp):
 global normcover
 if not pp or pp.degree()<=0:return
 atom=sf(pp);normcover*=qexact(atom,normcover.gcd(atom))
for name,val in paid:
 nv=norm(val)
 assert nv.n, 'A generic paid-unit norm is identically zero; retain instead of discard'
 include(nv.n);include(nv.d);include(val.d)
 normprofiles.append(dict(name=name,numerator=report_poly(nv.n),denominator=report_poly(nv.d),allFiniteNormZeroFibersRetained=True))
 integral_arrays.extend([nv.n,nv.d,val.d])
rawrows=[]
for pp in original:
 rr={}
 for mon,cf in pp.terms.items():
  rr[mon]=(cf.n,cf.d);include(cf.d);integral_arrays.extend(cf.n+[cf.d])
 rawrows.append(rr)
for ff in F:integral_arrays.append(ff)
low=cover.gcd(normcover);low=low/low[low.degree()]
high=qexact(cover,low);assert high*low==cover and high.gcd(low).degree()==0
assert high.gcd(normcover).degree()==0
integral_arrays.extend([normcover,low,high])
initial_C15=(kk+1)*(kk+2)*(kk+4)*(kk*kk+5*kk+8)*(kk*kk+5*kk+2)*(kk**8+4*kk**7-39*kk**6-334*kk**5-1304*kk**4-3128*kk**3-4640*kk*kk-3712*kk-1024)
initial_remaining=(kk*kk+5*kk+8)*(kk*kk+5*kk+2)*(kk**8+4*kk**7-39*kk**6-334*kk**5-1304*kk**4-3128*kk**3-4640*kk*kk-3712*kk-1024)
assert not divmod(low,initial_remaining)[1]
lc,lf=low.factor();back=P([lc])
lowfactors=[]
for ff,mult in lf:
 back*=ff**int(mult);lowfactors.append(dict(multiplicity=int(mult),**report_poly(ff)))
assert back==low
say(stage='new_J19_entire_QQ_finite_cover_weight_norm_partition',fullCover=report_poly(cover),retainedLowNormCover=report_poly(low),retainedLowNormQQFactors=lowfactors,highNormUnitCover=report_poly(high),allOriginalUnitNormNumeratorDenominators=normprofiles,entireC15TwoQuadraticAndOcticFibersRetained=True,exactFullCoverPartitionProductVerified=True,wholeJ19Excluded=False,claimExcluded=False)
def cm(cc,p):
 q=Fraction(str(cc));assert q.denominator%p
 return q.numerator%p*pow(q.denominator%p,-1,p)%p
rejected=[];prime=None
for pp in [1009,1013,1019,1021,1031,1033,1039,1049,1051]:
 if any(Fraction(str(c)).denominator%pp==0 for f in integral_arrays for c in f.coeffs()):
  rejected.append([pp,'an actual rational coefficient denominator is not p-integral']);continue
 mp=lambda f:nmod_poly([cm(c,pp) for c in f.coeffs()],pp)
 hh,nn=mp(high),mp(normcover)
 if hh.degree()!=high.degree() or int(hh[hh.degree()])!=1:
  rejected.append([pp,'monic QQ high-cover degree failed']);continue
 gg,ss,tt=hh.xgcd(nn)
 assert ss*hh+tt*nn==gg
 if gg.degree()!=0:
  rejected.append([pp,'an exact norm complement meets the modular high cover']);continue
 assert (ss*pow(int(gg[0]),-1,pp))*hh+(tt*pow(int(gg[0]),-1,pp))*nn==nmod_poly([1],pp)
 prime=pp;break
assert prime is not None
MP=lambda f:nmod_poly([cm(c,prime) for c in f.coeffs()],prime)
hmod=MP(high);nmod=MP(normcover)
for pp in integral_arrays:
 assert all(Fraction(str(c)).denominator%prime for c in pp.coeffs())
assert hmod.degree()==high.degree() and hmod.gcd(nmod).degree()==0
content,factors=hmod.factor();modback=nmod_poly([content],prime)
for ff,mult in factors:modback*=ff**int(mult)
assert modback==hmod
say(stage='new_J19_finite_original_good_prime_and_complete_k_factorization',prime=prime,rejectedPrimes=rejected,QQHighDegree=int(high.degree()),modularHighDegree=int(hmod.degree()),QQLeadingCoefficientActuallyOne=True,allActualOriginalQQCoefficientDenominatorsPUnits=True,completeNormBezoutActuallyMultipliedBack=True,fullModularFactorizationProductActuallyReturned=True,modularFactors=[dict(degree=int(ff.degree()),multiplicity=int(mul),coefficients=[int(c) for c in ff.coeffs()]) for ff,mul in factors],noMultivariateModularEmptinessClaim=True,claimExcluded=False)
monomials=sorted([(i,j,h) for i in range(5) for j in range(5-i) for h in range(5-i-j)],key=lambda z:(sum(z),z[1],z[0],z[2]),reverse=True)
assert len(monomials)==35 and monomials[-1]==(0,0,0)
monindex={m:i for i,m in enumerate(monomials)}
allresults=[];splitrecords=[];inverse_count=0
class EZeroDivisor(Exception):
 def __init__(self,g,q):self.g=g;self.q=q
for factor_index,(ff,multiplicity) in enumerate(factors):
 # fq_default_ctx checks this fmpz_mod_poly modulus for irreducibility.
 # nmod_poly in python-flint 0.9.0 has no is_irreducible method.
 kmod=fmpz_mod_poly_ctx(prime)([int(c) for c in ff.coeffs()])
 FC=fq_default_ctx(modulus=kmod,var='k',check_modulus=True)
 assert FC.modulus()==kmod
 kg=FC([0,1]);fc0=FC(0);fc1=FC(1)
 assert sum((FC(int(ff[j]))*kg**j for j in range(ff.degree()+1)),fc0)==0
 PC=fq_default_poly_ctx(FC)
 def ev(pp):return FC([cm(c,prime) for c in pp.coeffs()])
 jraw=PC([ev(z) for z in F]);lead=ev(F[4]);leadi=lead.inverse();assert lead*leadi==fc1
 jmonic=jraw*leadi;assert jmonic*lead==jraw and jmonic.degree()==4
 native_original=[]
 for rr in rawrows:
  out={}
  for mon,(nums,den) in rr.items():
   dd=ev(den);di=dd.inverse();assert dd*di==fc1
   out[mon]=PC([ev(nn) for nn in nums])*di
  native_original.append(out)
 def pdata(pp):return [[int(c) for c in z.to_list()] for z in pp.coeffs()]
 def process(H,path):
  global inverse_count
  class A:
   def __init__(self,v=0):
    if isinstance(v,A):self.p=v.p;return
    vv=PC(v);qq,rr=divmod(vv,H)
    assert qq*H+rr==vv;self.p=rr
   def __bool__(self):return bool(self.p)
   def __neg__(self):return A(-self.p)
   def __add__(self,v):return A(self.p+A(v).p)
   __radd__=__add__
   def __sub__(self,v):return A(self.p-A(v).p)
   def __rsub__(self,v):return A(v)-self
   def __mul__(self,v):return A(self.p.mul_mod(A(v).p,H))
   __rmul__=__mul__
   def __eq__(self,v):return self.p==A(v).p
   def inv(self):
    global inverse_count
    assert self
    gg,ss,tt=self.p.xgcd(H)
    assert ss*self.p+tt*H==gg
    if gg.degree()>0:
     qq,rr=divmod(H,gg);assert not rr and qq*gg==H and 0<gg.degree()<H.degree()
     raise EZeroDivisor(gg,qq)
    out=A(ss*gg[0].inverse());assert self*out==1
    inverse_count+=1;return out
   def data(self):return pdata(self.p)
  try:
   rows=[];labels=[]
   for ni,rr in enumerate(native_original):
    formal_degree=2 if ni<4 else 3
    for mm in sorted([m for m in monomials if sum(m)<=4-formal_degree],key=lambda z:(sum(z),z[1],z[0],z[2])):
     row=[A() for _ in monomials]
     for m,c in rr.items():
      target=tuple(m[j]+mm[j] for j in range(3));assert sum(target)<=4
      row[monindex[target]]=row[monindex[target]]+A(c)
     rows.append(row);labels.append([names[ni],mm])
   assert len(rows)==48
   basis0=[];tags=[];pivots=[]
   for idx,rawrow in enumerate(rows):
    row=rawrow[:];tag={idx:A(1)}
    for brow,pv,bt in zip(basis0,pivots,tags):
     cf=row[pv]
     if not cf:continue
     row=[row[j]-cf*brow[j] for j in range(35)]
     for ii,vv in bt.items():tag[ii]=tag.get(ii,A())-cf*vv
    if not any(row):continue
    pv=next(j for j,v in enumerate(row) if v);iv=row[pv].inv()
    row=[v*iv for v in row];tag={j:v*iv for j,v in tag.items() if v}
    assert row[pv]==1 and all(not row[j] for j in pivots)
    for j in range(35):assert sum((vv*rows[ii][j] for ii,vv in tag.items()),A())==row[j]
    basis0.append(row);tags.append(tag);pivots.append(pv)
    if len(basis0)==35:break
   full=len(basis0)==35;actual={};unit_verified=False
   if full:
    target=[A(int(j==34)) for j in range(35)];rem=target[:]
    for brow,pv,bt in zip(basis0,pivots,tags):
     cf=rem[pv]
     if not cf:continue
     rem=[rem[j]-cf*brow[j] for j in range(35)]
     for ii,vv in bt.items():actual[ii]=actual.get(ii,A())+cf*vv
    assert not any(rem)
    for j in range(35):assert sum((vv*rows[ii][j] for ii,vv in actual.items()),A())==target[j]
    unit_verified=True
   cert=dict(prime=prime,kFactor=[int(c) for c in ff.coeffs()],eModulus=pdata(H),labels=labels,pivots=pivots,allBasisRows=[{str(j):v.data() for j,v in tag.items()} for tag in tags],originalUnitCombination={str(j):v.data() for j,v in actual.items()})
   rec=dict(kFactorIndex=factor_index,kDegree=int(ff.degree()),kMultiplicity=int(multiplicity),ePath=path,eDegree=int(H.degree()),originalRows=48,columns=35,rank=len(basis0),allBasisOriginalThirtyFiveColumnProductsActuallyVerified=True,originalUnitThirtyFiveColumnProductsActuallyVerified=unit_verified,allActualInverseProductsOne=True,fullColumnRank=full,certificate=digest_json(cert))
   allresults.append(rec)
   say(stage='new_J19_finite_whole_e_algebra_original_48x35_return',**rec,wholeJ19Excluded=False,claimExcluded=False)
  except EZeroDivisor as ex:
   assert ex.g*ex.q==H and 0<ex.g.degree()<H.degree() and 0<ex.q.degree()<H.degree()
   rec=dict(kFactorIndex=factor_index,ePath=path,left=pdata(ex.g),right=pdata(ex.q),wholeEPolynomialProductActuallyVerified=True,bothOriginalBranchesRetained=True)
   splitrecords.append(rec)
   say(stage='new_J19_finite_actual_e_zero_divisor_complete_split',**rec,claimExcluded=False)
   process(ex.g,path+'/a');process(ex.q,path+'/b')
 process(jmonic,'J19')
passed=bool(allresults) and all(r['fullColumnRank'] and r['originalUnitThirtyFiveColumnProductsActuallyVerified'] for r in allresults)
signal.alarm(0)
say(stage='new_J19_entire_high_QQ_cover_original_finite_Gauss_return_complete',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),prime=prime,fullPublishedCoverDegree=588,entireQQHighCover=report_poly(high),retainedQQNormZeroCover=report_poly(low),retainedQQNormZeroFactors=lowfactors,modularConstantAlgebraReturns=allresults,completeESplits=splitrecords,actualInverseCount=inverse_count,allHighQQFibersExcludedByFiniteConstantAlgebraGauss=passed,multiplicitiesRetainedByFiniteArtinianNakayama=True,noModularDOnlyMembershipLiftUsed=True,allLowNormOriginalFibersStillRequireQQReturn=True,noMultivariateGcdOrSamplingEmptinessClaim=True,wholeJ19Excluded=False,claimExcluded=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
