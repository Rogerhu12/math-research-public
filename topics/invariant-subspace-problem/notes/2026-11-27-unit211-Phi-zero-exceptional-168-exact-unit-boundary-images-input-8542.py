#!/usr/bin/env python3
"""NEW exact QQ original unit-boundary images for the 168-point Phi branch.
Use saved F26, PB C31,50, mixed C34,48 only; no old determinants or
resultants are recomputed.  At rho=0,+/-1,+/-3,3/2 evaluate all THREE
same-rho original necessary polynomials, take the actual QQ gcd, and
factor it with complete product checks.  Compare these genuine QQ
image factors with the already-returned common mod polynomial.
A boundary IMAGE is not an entire-fiber exclusion.  No such claim is made.
120 seconds / 1 GiB; three exact JSON dependencies beside this source.
No helpers or arguments. All full dependency bytes are SHA256 checked.
"""
import time,json,hashlib,base64,zlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx,nmod_poly
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
began=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw),flush=True)
ctx=fmpq_mpoly_ctx.get(("rho","lam"),"lex")
def load_poly(data,payload_sha,poly_sha,degrees,terms):
 raw=zlib.decompress(base64.b64decode(data))
 assert hashlib.sha256(raw).hexdigest()==payload_sha
 obj=json.loads(raw);assert obj["variables"]==["rho","lam"]
 pp=ctx.from_dict({(int(i),int(j)):fmpq(c) for i,j,c in obj["terms"]})
 assert list(map(int,pp.degrees()))==degrees and len(pp.to_dict())==terms
 assert hashlib.sha256(str(sorted(pp.to_dict().items())).encode()).hexdigest()==poly_sha
 return pp
def dependency(name,sha256):
 path=Path(__file__).with_name(name)
 raw=path.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha256,("wrong exact dependency",name)
 return json.loads(raw)
inputF=dependency(
 "2026-11-27-unit211-Phi-zero-exceptional-F26-exact-input-8542.json",
 "67c73f8f5fef33d509ffebd8165487e5b6abcc59fe391acc4075da1f22287d61")
inputG=dependency(
 "2026-11-27-unit211-Phi-zero-exceptional-PB-core-and-mod-resultant-exact-input-8542.json",
 "74891d2b2f8bd21f74ff063cef7aeed85532a2378e71dac07ad5cfc4d240c8c9")
inputH=dependency(
 "2026-11-27-unit211-Phi-zero-exceptional-mixed-core-and-mod-return-exact-input-8542.json",
 "a9ab01ff03d894ed1fe6033b68268ecbf7b9d36dc2cd4ff3d7bf69b771387073")
rf,rg,rh=(obj["polynomial"] for obj in (inputF,inputG,inputH))
F=load_poly(rf["data"],rf["payloadSha256"],
 "9057238c5d37c8cd9f62f3f512dcff1f6d2e385cd6c0e39250a571713f0aaac7",[26,26],729)
G=load_poly(rg["data"],rg["payloadSha256"],
 "3d850765f6c9338aa8f79af2b5889582cf8d4f45fd81ad90f4743fb5bebd5f6c",[31,50],1632)
H=load_poly(rh["data"],rh["payloadSha256"],
 "496ce5b01ff327ac7b1fa6a125f04808d368aca7a88b0078f0e0622ced90f8e4",[34,48],1715)
def old_mod(data,sha,expected_sha,degree):
 raw=zlib.decompress(base64.b64decode(data))
 assert hashlib.sha256(raw).hexdigest()==sha
 p=nmod_poly(json.loads(raw),1009)
 assert p.degree()==degree and hashlib.sha256(str(p).encode()).hexdigest()==expected_sha
 return p
rrec=inputG["full_fixed_mod1009_resultant"]
srec=inputH["fixed_mod_resultant"]
grec=inputH["actual_common_mod_input"]
oldR=old_mod(rrec["fullCoefficientsData"],rrec["fullCoefficientsPayloadSha256"],
 "f4505a726a6c2691ac52b92ec424160f7cc748d6a9b17751ce8b2f9f3f0eaa85",2033)
oldS=old_mod(srec["fullCoefficientsData"],srec["fullCoefficientsPayloadSha256"],
 "060c2f63b871fec6e649ce3bdfbf29612df9402b07c3c4d381245f639edb8e12",2050)
oldg=nmod_poly(grec["coefficientsAscending"],1009)
assert oldg.degree()==168
assert oldR%oldg==0 and oldS%oldg==0
def evaluate_rho(p,value):
 value=fmpq(value);d0,d1=map(int,p.degrees())
 powers=[fmpq(1)]
 for i in range(d0):powers.append(powers[-1]*value)
 out=[fmpq(0)]*(d1+1)
 for ex,c in p.to_dict().items():out[int(ex[1])]+=c*powers[int(ex[0])]
 return fmpq_poly(out)
def coeffs(p):return [str(p[i]) for i in range(p.degree()+1)]
def mbar(p):
 vals=[]
 for j in range(p.degree()+1):
  v=fmpq(p[j]);dd=int(v.denominator)%1009
  assert dd
  vals.append(int(v.numerator)%1009*pow(dd,-1,1009)%1009)
 return nmod_poly(vals,1009)
def valuation_mod(p,phi):
 e=0;cur=p
 while cur and cur%phi==0:
  q=cur//phi;assert q*phi==cur;cur=q;e+=1
 return e
unique={}
boundaries=[("rho0:1-Q",fmpq(0)),("rho1:Q",fmpq(1)),
 ("rho-1:Q",fmpq(-1)),("rho3:T0",fmpq(3)),
 ("rho-3:u",fmpq(-3)),("rho3/2:u+Q-1",fmpq(3,2))]
for label,rho0 in boundaries:
 values=[evaluate_rho(p,rho0) for p in (F,G,H)]
 assert any(values)
 g=values[0].gcd(values[1]).gcd(values[2])
 assert g
 for v in values:
  qq,rem=divmod(v,g);assert rem==0 and qq*g==v
 scalar,factors=g.factor();prod=fmpq_poly([scalar]);out=[]
 for phi,mult in factors:
  prod*=phi**mult
  phi=phi*(1/phi[phi.degree()])
  assert phi[phi.degree()]==1
  for v in values:
   qq,rem=divmod(v,phi);assert rem==0 and qq*phi==v
  key=str(phi)
  if key not in unique:unique[key]={"phi":phi,"boundaries":[]}
  unique[key]["boundaries"].append(label)
  out.append(dict(degree=int(phi.degree()),multiplicityInBoundaryGcd=int(mult),
   monicCoefficients=coeffs(phi),polynomial=str(phi)))
 assert prod==g
 say("new_exact_QQ_same_rho_original_unit_boundary_image",
     boundary=label,rho=str(rho0),
     threeOriginalSpecializedDegrees=[int(v.degree()) for v in values],
     fullQQGcdDegree=int(g.degree()),fullQQGcdPolynomial=str(g),
     irreducibleQQFactors=factors and out or [],
     allOriginalDivisionsAndFactorProductReturned=True,
     imageOnlyNotWholeParameterFiberExclusion=True)
support=nmod_poly([1],1009);cases=[]
for ix,entry in enumerate(unique.values()):
 phi=entry["phi"];bar=mbar(phi)
 assert bar.degree()==phi.degree() and int(bar[bar.degree()])==1
 vr,vs,vg=valuation_mod(oldR,bar),valuation_mod(oldS,bar),valuation_mod(oldg,bar)
 assert vr>=1 and vs>=1 and vg>=1
 support*=bar
 item=dict(index=ix,degree=int(phi.degree()),monicCoefficients=coeffs(phi),
  polynomial=str(phi),originalUnitBoundaries=entry["boundaries"],
  modCoefficientsAscending=[int(bar[j]) for j in range(bar.degree()+1)],
  fullModRMultiplicity=vr,fullModSMultiplicity=vs,commonModMultiplicity=vg,
  QQFactorSource="actual gcd of all three originals at one exact rational rho boundary",
  QQFirstPowerResultantDivisibilityPaidByCommonBoundaryRoot=True,
  higherQQDivisibilityMultiplicitiesNotYetPaid=True,
  WholeQQParameterFiberNotYetExcluded=True)
 cases.append(item)
 say("new_genuine_QQ_boundary_image_factor_and_mod_multiplicities",**item)
remaining=oldg
removed_degree=0
while remaining.degree()>0:
 gg=remaining.gcd(support)
 if gg.degree()==0:break
 qq=remaining//gg;assert qq*gg==remaining;remaining=qq
 removed_degree+=int(gg.degree())
say("complete_new_exact_boundary_image_support_input",
 uniqueQQImageFactorCount=len(cases),
 trueQQImageFactors=cases,
 actualCommonModDegree=168,
 degreeSupportedOnKnownQQBoundaryImages=removed_degree,
 residualModDegree=int(remaining.degree()),
 residualModCoefficientsAscending=[int(remaining[j]) for j in range(remaining.degree()+1)],
 exactImageFactorsAreNotDeclaredWholeFiberExclusions=True,
 commonQQDivisibilityMultiplicitiesStillNeeded=True,
 oldOriginalDeterminantsAndProjectionsNotReplayed=True,
 wholeExceptionalBranchExcluded=False,ordinaryISPClaim=False)
