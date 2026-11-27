#!/usr/bin/env python3
"""NEW P25,3 input: deflate only the actual Delta/Tnum common Q factor,
which is a unit at every remaining original point. Form lower original
Q equations and their fixed Sylvester resultants, then true weight norms.
Intersect the NEW exact lambda cover with the saved F1474. No completed
R/W Euclidean certificate or old projection is rerun. All new chart
denominators and all actual Q-leading-zero fibres are retained.
180 seconds /4 GiB.
"""
import json,time,hashlib,signal,resource,contextlib,io,math,zlib,base64
from pathlib import Path
from flint import fmpq,fmpq_poly
start=time.perf_counter();deadline=start+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw,separators=(',',':')),flush=True)
dep=Path(__file__).with_name("2026-11-28-unit211-collision-P25-3-whole-weight-original-Q-Delta-power-8542.py")
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="d6cad40d79310912a20bfd9270303f52683d05c6b61b85b6399d1d5a4281f37a"
marker=b"\nreturned=False;power=None;current=values[\"R\"];"
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
ns={"__file__":str(dep),"__name__":"__only_saved_original_cubic_weight_input__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep),"exec"),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
ns["say"]=say
A,U,lam,u,Q,ell,xi,T0,J,Phi,S,eta,NF,Delta,values=[ns[k] for k in
 ["A","U","lam","u","Q","ell","xi","T0","J","Phi","S","eta","NF","Delta","values"]]
lp,one,zero,pol,Rat,exact,monic,pdigest,coefficients,divide,euclid=[ns[k] for k in
 ["lp","one","zero","pol","Rat","exact","monic","pdigest","coefficients","divide","euclid"]]
# This cover has only the actual input coefficients, the whole P3 u head,
# and the paid A/B inverses used to write the original Delta.
chart=ns["cover"]
def keep(p):
 global chart
 if p.degree()>0:
  p=monic(p);chart=monic(chart*exact(p,chart.gcd(p)))
def keepU(p):
 for c in p.c:keep(c.d)
def digest_obj(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def emit_coefficients(stage,p,**kw):
 raw=json.dumps(coefficients(p),separators=(',',':')).encode()
 data=base64.b64encode(zlib.compress(raw,9)).decode()
 assert zlib.decompress(base64.b64decode(data))==raw
 chunks=[data[i:i+75000] for i in range(0,len(data),75000)]
 say(stage,degree=int(p.degree()),rawBytes=len(raw),rawSHA256=hashlib.sha256(raw).hexdigest(),
     base64Characters=len(data),chunks=len(chunks),**kw)
 for i,s in enumerate(chunks):
  say(stage+"_chunk",index=i,total=len(chunks),data=s)

A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam**2+3*lam-1
T=A2**2/B3;w=lam-1-T
V2=2*u-ell*Q
P02=(2-3*u)*V2-Q*u+2*u**3
Pf=T0*(J-Q);G=lam*P02-(1-u)*T0
Pc=Q*P02*(ell+T)-G*T0
NC=eta*(-G*xi+Q*w*u)
Tnum=Pf*NC-Pc*NF
keepU(Tnum)
say("new_original_Delta_Tnum_low_Q_input_on_entire_P3",
    DeltaQDegree=Delta.degree(),TnumQDegree=Tnum.degree(),
    frozenInputPrefixBytes=len(prefix),previousRWGcdGateNotExecuted=True)
Gamma=euclid(Delta,Tnum,"NEW actual Delta,Tnum low Q common factor")
assert Gamma and Gamma.degree()>0
dquot,drem=divide(Delta,Gamma,"new actual Delta Gamma factor")
nquot,nrem=divide(Tnum,Gamma,"new actual Tnum Gamma factor")
assert not drem and not nrem
assert dquot*Gamma==Delta and nquot*Gamma==Tnum
keepU(Gamma);keepU(dquot);keepU(nquot)
say("new_actual_common_Q_factor_is_physical_unit",
    GammaQDegree=Gamma.degree(),GammaLeadingOne=Gamma.c[-1]==1,
    exactOriginalDeltaAndTnumProductsReturned=True,
    physicalUnitReason="Gamma divides the true original Delta, already nonzero",
    gammaExactCoefficients=digest_obj(Gamma.data()),
    allGammaCoefficientZeroDenominatorsRetained=True)
deflated={};powers={}
for name in ["R","W","O","N1"]:
 cur=values[name];power=0
 for j in range(2):
  quotient,remainder=divide(cur,Gamma,"new "+name+" physical Gamma factor")
  if remainder:break
  assert quotient*Gamma==cur
  cur=quotient;power+=1
 assert cur*(Gamma**power)==values[name]
 deflated[name]=cur;powers[name]=power;keepU(cur)
 say("new_lower_Q_original_equivalent_equation",
     original=name,originalQDegree=values[name].degree(),
     actualGammaPowerRemoved=power,newQDegree=cur.degree(),
     completeOriginalPolynomialProductReturned=True,
     originalEquivalenceOnlyWhereTrueDeltaAndRetainedChartUnitsNonzero=True,
     coefficientLambdaDegree=cur.complexity())
# Unlike the preceding GENERIC ideal return, the following output is
# the UNIVERSAL fixed-degree Sylvester polynomial in the new coefficients.
# Intermediate computational inverse poles are not physical assumptions.
# The checked division recurrence computes that polynomial over QQ(lambda);
# equality then extends through its transient pivots in the free monic
# rank-three weight algebra wherever actual input/output coefficients exist.
def resultant(a,b,label):
 a=U(a);b=U(b);assert a and b
 original_degrees=[a.degree(),b.degree()]
 accumulator=A(1);step=0
 while b.degree()>0:
  m,n=a.degree(),b.degree()
  quotient,remainder=divide(a,b,label+" actual lower-Q Sylvester recurrence")
  if not remainder:
   say("new_original_lower_Q_resultant_zero",
       pair=label,fixedOriginalQDegrees=original_degrees,
       actualDivisionProductsReturned=True,noExclusionClaim=True)
   return A()
  r=remainder.degree()
  accumulator=accumulator*((-1)**(m*n))*(b.c[-1]**(m-r))
  a,b=b,remainder;step+=1
  say("new_original_lower_Q_fixed_resultant_step",
      pair=label,step=step,newDegrees=[a.degree(),b.degree()],
      allThreeWeightComponentsOfDivisionIdentityReturned=True)
 answer=accumulator*(b.c[0]**a.degree())
 say("new_complete_fixed_original_lower_Q_resultant",
     pair=label,fixedOriginalQDegrees=original_degrees,
     fixedSylvesterSize=sum(original_degrees),
     answerLambdaDegree=answer.complexity(),
     exactUniversalDeterminantRecurrence="Res(A,B)=(-1)^(mn)*lc(B)^(m-r)*Res(B,remainder)",
     allSpecializedQLeadingZeroFibersRetained=True,
     transientArithmeticPivotZeroNotDiscarded=True,
     coefficients=digest_obj(answer.data()))
 return answer
def norm(a,label):
 cols=[a*(u**j) for j in range(3)]
 for c in cols:keep(c.d)
 mm=[[cols[j].n[i] for j in range(3)] for i in range(3)]
 nn=(mm[0][0]*(mm[1][1]*mm[2][2]-mm[1][2]*mm[2][1])
    -mm[0][1]*(mm[1][0]*mm[2][2]-mm[1][2]*mm[2][0])
    +mm[0][2]*(mm[1][0]*mm[2][1]-mm[1][1]*mm[2][0]))
 adj=[[zero for _ in range(3)] for _ in range(3)]
 for i in range(3):
  for j in range(3):
   sub=[[mm[r][c] for c in range(3) if c!=i] for r in range(3) if r!=j]
   adj[i][j]=((-1)**(i+j))*(sub[0][0]*sub[1][1]-sub[0][1]*sub[1][0])
 for i in range(3):
  for j in range(3):
   assert sum((mm[i][k]*adj[k][j] for k in range(3)),zero)==(nn if i==j else zero)
 dd=one
 for c in cols:dd*=c.d
 ans=Rat(nn,dd);keep(ans.d)
 say("new_complete_original_lower_Q_resultant_weight_norm",
     pair=label,weightBasis=["1","u","u^2"],
     fullThreeByThreeAdjugateProductActuallyReturned=True,
     numerator=pdigest(ans.n),denominator=pdigest(ans.d),
     normZeroNecessaryForEveryActualCommonQRoot=True,
     noUnpaidNormZeroFiberRemoved=True)
 return ans
norms=[]
for name in ["W","N1"]:
 ans=resultant(deflated["R"],deflated[name],"R/"+str(powers["R"])+" and "+name+"/"+str(powers[name]))
 keep(ans.d)
 nr=norm(ans,name)
 if nr.n:norms.append(nr.n)
 else:say("new_zero_norm_retained",original=name,noFiniteCoverClaimFromThisNorm=True)
assert norms
common=norms[0]
for p in norms[1:]:common=common.gcd(p)
assert common
for p in norms:assert exact(p,common)*common==p
newcover=monic(chart*common)
newcover=monic(exact(newcover,newcover.gcd(newcover.derivative())))
paid=[("lambda",lp),("A",2*lp**2-2*lp+1),("B",4*lp**3-6*lp**2+3*lp-1),
      ("S",(2*lp-1)*(2*lp**2-1)),("entire_J2",3*lp**2-2*lp+1)]
paid_removed=[]
for label,p in paid:
 gg=newcover.gcd(p)
 if gg.degree()>0:
  old=newcover;newcover=monic(exact(newcover,gg))
  assert monic(newcover*gg)==monic(old)
  paid_removed.append([label,int(gg.degree())])
say("new_independent_exact_lambda_cover_from_original_deflated_Q_norms",
    completeActualChart=pdigest(chart),actualNormGcd=pdigest(common),
    completeNewCover=pdigest(newcover),paidScalarRemovals=paid_removed,
    everyOriginalP3PointCovered=True,allUnpaidLambdaHeadFibersRetained=True)
# Reuse the exact old cover as DATA, never recompute its generic gate.
mpath=Path(__file__).with_name("2026-11-28-unit211-collision-P3-exact-1474-cover-8542.manifest.json")
manifest=json.loads(mpath.read_bytes())
assert manifest["degree"]==1474 and manifest["rawBytes"]==893821
assert manifest["rawSHA256"]=="19d13559553f93f4839a17f5264f552b67cfb74a0b931d4edbb196a4546da0ce"
parts=[]
for i,rec in enumerate(manifest["chunks"]):
 assert rec["index"]==i and Path(rec["file"]).name==rec["file"]
 raw=Path(__file__).with_name(rec["file"]).read_bytes()
 assert len(raw)==rec["bytes"] and hashlib.sha256(raw).hexdigest()==rec["sha256"]
 item=json.loads(raw);assert item["index"]==i and item["total"]==7
 data=item["dataChunk"]
 assert len(data)==rec["dataCharacters"] and hashlib.sha256(data.encode()).hexdigest()==rec["dataSHA256"]
 parts.append(data)
encoded="".join(parts)
assert hashlib.sha256(encoded.encode()).hexdigest()==manifest["base64SHA256"]
raw=zlib.decompress(base64.b64decode(encoded))
assert len(raw)==893821 and hashlib.sha256(raw).hexdigest()==manifest["rawSHA256"]
oldcover=pol(json.loads(raw));assert oldcover.degree()==1474 and oldcover[1474]==1
reduced,sa,sb=oldcover.xgcd(newcover)
assert sa*oldcover+sb*newcover==reduced and reduced
reduced=monic(reduced)
assert exact(oldcover,reduced)*reduced==oldcover
assert exact(newcover,reduced)*reduced==newcover
say("new_complete_original_P3_two_covers_true_QQ_intersection",
    oldCoverDegree=1474,newIndependentCoverDegree=int(newcover.degree()),
    newCompleteCoverDegree=int(reduced.degree()),
    bothDivisionsAndFullQQBezoutActuallyReturned=True,
    wholeP3Excluded=(reduced.degree()==0),
    allRemainingLambdaUQFibersStillRequireOriginalReturn=True)
emit_coefficients("new_deflated_original_P3_exact_complete_lambda_cover",reduced,
    everyOriginalP3PointCovered=True,noOldGenericInputReplayed=True)
say("new_original_P3_low_factor_deflation_and_fixed_norm_projections_complete",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    GammaDegree=Gamma.degree(),GammaPowersRemoved=powers,
    actualOriginalQDegrees={k:v.degree() for k,v in deflated.items()},
    actualNewQDivisionProducts=ns["divisions"],
    actualNewDivisionCertificateSHA256=ns["trace"].hexdigest(),
    actualWholeWeightInverseProducts=len(ns["inverses"]),
    completeLambdaCoverDegree=int(reduced.degree()),
    wholeP3Excluded=(reduced.degree()==0),wholeCollisionExcluded=False,
    ordinaryISPClaim=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
