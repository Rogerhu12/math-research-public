#!/usr/bin/env python3
"""NEW complete J2(lambda)=3lambda^2-2lambda+1 original collision fiber.
Read the four exact original same-point polynomials. Reduce every lambda
coefficient in the WHOLE quadratic QQ field, strip only explicitly proved
original weight units, and form exact same-lambda cross and norm identities.
All new coefficient/head zeros remain. Any new Q projection uses fixed
original degrees. 120 seconds /1 GiB; no earlier projection is recomputed."""
import json,time,hashlib,signal,resource,base64,zlib
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start);print(json.dumps(kw),flush=True)
spec=[["2026-11-27-unit211-collision-Delta-nonzero-four-original-exact-input-part1-8542.json","c4723da150647c453cd53151b4e9f84e5d6ed1c45dffcf4c39299b9ef968c3e6"],["2026-11-27-unit211-collision-Delta-nonzero-four-original-exact-input-part2-8542.json","8f8a547ba11ffc2baafd0229f9ffce5a16576206d06460d627927b80d4671682"]];parts=[]
for i,(name,sha) in enumerate(spec):
 raw=Path(__file__).with_name(name).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
 data=json.loads(raw);assert data["part"]==i+1 and data["total"]==2
 parts.append(data["dataChunk"])
raw=zlib.decompress(base64.b64decode("".join(parts)))
assert hashlib.sha256(raw).hexdigest()=="11046373e5362f4b5606e2940483929954a74382e152e40f211fbe79ec42b292"
data=json.loads(raw);assert data["variables"]==["lambda","u","Q"]
phi=fmpq_poly([fmpq(1,3),fmpq(-2,3),1])
lv=fmpq_poly([0,1]);Ap=2*lv**2-2*lv+1;Bp=4*lv**3-6*lv**2+3*lv-1
assert (Ap**3-fmpq(1,2)*Bp**2)%phi==0
assert (Bp-(1-lv)*Ap)%phi==0
assert (Ap**2-fmpq(1,2)*(1-lv)*Bp)%phi==0
for p in [Ap,Bp,lv,1-lv,5-4*lv,4-3*lv]:
 g,a,b=p.xgcd(phi);assert a*p+b*phi==g and g.degree()==0
ctx=fmpq_mpoly_ctx.get(("u","Q"),"lex");u,Q=ctx.gens();one=ctx.constant(1);zero=ctx.constant(0)
ell=fmpq(1,2);T0=2*u-ell*Q-2*u*u
P02=(2-3*u)*(2*u-ell*Q)-Q*u+2*u**3
Phi=T0+4*u-4+Q
assert P02==-(u-2)*T0
assert ell**2*(1-Q)-(u-ell)**2==T0/2
units=[("u",u),("u-1",u-1),("u-2 from P02/T0",u-2),
       ("u-ell",2*u-1),("Q",Q),("1-Q",1-Q),
       ("T0 and bc",T0),("Phi",Phi),("u+Q-1",u+Q-1)]
def strip(p):
 orig=p;prod=one;hist=[]
 if not p:return p,prod,hist
 for label,a in units:
  count=0
  while True:
   gg=p.gcd(a)
   if gg.total_degree()==0:break
   q=p/gg;assert q*gg==p;p=q;prod*=gg;count+=1
  if count:hist.append([label,count])
 assert p*prod==orig
 return p,prod,hist
def profile(p):
 rr=[[list(map(int,e)),str(c)] for e,c in sorted(p.to_dict().items())]
 raw=json.dumps(rr,separators=(",",":")).encode()
 return dict(degrees_u_Q=list(map(int,p.degrees())),totalDegree=int(p.total_degree()),
             terms=len(rr),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def save(p):
 rr=[[list(map(int,e)),str(c)] for e,c in sorted(p.to_dict().items())]
 raw=json.dumps({"variables":["u","Q"],"terms":rr},separators=(",",":")).encode()
 out=dict(profile=profile(p),payloadBytes=len(raw),payloadSHA256=hashlib.sha256(raw).hexdigest())
 if len(raw)<100000:
  enc=zlib.compress(raw,9);back=json.loads(zlib.decompress(enc))
  assert ctx.from_dict({tuple(e):fmpq(c) for e,c in back["terms"]})==p
  out.update(encoding="base64+zlib+json",data=base64.b64encode(enc).decode())
 return out
pairs={};reduction_count=0
for label,terms in data["polynomials"].items():
 grouped={}
 for (j,i,k),c in terms:
  key=(int(i),int(k));cc=[fmpq(0)]*(int(j)+1);cc[int(j)]=fmpq(c)
  grouped[key]=grouped.get(key,fmpq_poly([]))+fmpq_poly(cc)
 aa={};bb={}
 for e,p in grouped.items():
  quotient,rem=divmod(p,phi);assert quotient*phi+rem==p;reduction_count+=1
  if rem[0]:aa[e]=rem[0]
  if rem[1]:bb[e]=rem[1]
 a=ctx.from_dict(aa);b=ctx.from_dict(bb)
 common=a.gcd(b);res,paid,history=strip(common)
 if paid:
  na=a/paid;nb=b/paid;assert na*paid==a and nb*paid==b;a,b=na,nb
 pairs[label]=(a,b)
 say("new_J2_complete_original_lambda_field_coefficients",original=label,
     firstCoefficient=save(a),lambdaCoefficient=save(b),
     onlyPaidCommonContent=history,completeOriginalLambdaDivisionProducts=True)
say("new_J2_entire_same_original_value_fiber",
    phiAscending=["1/3","-2/3","1"],entireConstantDegree=2,
    originalConstants={"ell":"1/2","xi":"1-lambda","T":"(1-lambda)/2"},
    completeExactConstantIdentitiesReturned=True,lambdaCoefficientDivisions=reduction_count,
    allConstantEmbeddingsAndCoefficientZeroFibersRetained=True,
    allFourSameLambdaOriginalRowsRetained=True)
cores={};constant=[]
def addcore(label,p,identity):
 if not p:
  say("new_J2_identically_zero_original_parameter_identity",name=label,identity=identity);return
 c,removed,hist=strip(p);scalar=c.coefficient(0);c=c/scalar;removed*=scalar;assert c*removed==p
 cores[label]=c
 if c.total_degree()==0:constant.append(label)
 say("new_J2_exact_same_lambda_original_parameter_identity",name=label,
     originalIdentity=identity,necessaryPolynomial=save(c),onlyPaidRemovals=hist,
     allProductsReturned=True,wholeOriginalJ2FiberExcluded=c.total_degree()==0)
labels=list(pairs)
for label,(a,b) in pairs.items():
 # 3Theta=B^2*(3lambda^2-2lambda+1)-(3B lambda-2B-3A)*(A+B lambda).
 pp=3*a*a+2*a*b+b*b
 co=[b*b, -2*b*b,3*b*b]
 product=[(-2*b-3*a)*a,(3*b)*a+(-2*b-3*a)*b,3*b*b]
 assert co[0]-product[0]==pp and co[1]-product[1]==0 and co[2]-product[2]==0
 addcore("norm_"+label,pp,"3Theta=B^2*J2-(3B*lambda-2B-3A)*R")
for i in range(len(labels)):
 for j in range(i+1,len(labels)):
  a,b=pairs[labels[i]];c,d=pairs[labels[j]]
  cross=d*a-b*c;assert d*b-b*d==0
  addcore("cross_"+labels[i]+"_"+labels[j],cross,"cross=Bj*Ri-Bi*Rj")
for label,p in cores.items():
 scalar,factors=p.factor();prod=ctx.constant(scalar);rec=[]
 for f,n in factors:prod*=f**n;rec.append(dict(multiplicity=int(n),factor=save(f)))
 assert prod==p
 say("new_J2_parameter_identity_complete_QQ_factor_cover",name=label,scalar=str(scalar),
     factors=rec,wholeQQProductReturned=True,allFactorsRetained=True)
if not constant and cores:
 ordered=sorted(cores.items(),key=lambda v:(int(v[1].degrees()[1]),int(v[1].total_degree())))
 label,p=ordered[0]
 if int(p.degrees()[1])==0:
  say("new_J2_complete_original_u_cover",source=label,cover=save(p),allQFibersRetained=True)
 else:
  pick=None
  for name,q in ordered[1:]:
   if p*q.coefficient(0)!=q*p.coefficient(0):pick=(name,q);break
  if pick:
   name,q=pick;result=p.resultant(q,"Q")
   say("new_J2_fixed_original_Q_projection",originalRows=[label,name],
       fixedQDegrees=[int(p.degrees()[1]),int(q.degrees()[1])],
       fullQQResultant=save(result),allQLeadingZeroFibersRetained=True,
       noExclusionFromUnitMultivariateGcd=True)
   if result:
    core,paid,hist=strip(result)
    scalar,factors=core.factor();prod=ctx.constant(scalar);rec=[]
    for f,n in factors:prod*=f**n;rec.append(dict(multiplicity=int(n),factor=save(f)))
    assert prod==core
    say("new_J2_complete_original_u_factor_cover",factors=rec,
        onlyPaidRemovals=hist,allFullQQFactorProductsReturned=True,
        allUAndQFibersRetained=True,wholeOriginalJ2FiberExcluded=core.total_degree()==0)
say("new_entire_J2_original_norm_cross_return_finished",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    constantOriginalNecessaryRows=constant,
    wholeOriginalJ2FiberExcluded=bool(constant),noOldProjectionRecomputed=True,
    ordinaryISPClaim=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
