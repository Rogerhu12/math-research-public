#!/usr/bin/env python3
"""NEW full lambda-coefficient base locus of the actual Phi P6 and C6.
This does not rerun a Sylvester, resultant, determinant, or rank gate.
Only the fixed original scalar definitions are reconstructed. Every
new polynomial is a complete exact combination of their lambda
coefficients, allowing division only by previously paid weight units
and nonzero QQ constants. A returned constant 1 excludes a whole
lambda fibre at every allowed weight; it does NOT exclude actual
finite lambda roots or the whole Phi branch.
180 seconds / 4 GiB, including all necessary source prefixes.
Historical coefficients are used only in runner memory, never copied
into this source, saved as a cache, encoded, or split into artifacts.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,math,heapq
from pathlib import Path
from flint import fmpq
START=time.perf_counter();DEADLINE=START+180
signal.setitimer(signal.ITIMER_REAL,180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
name="2026-11-28-unit211-Phi-zero-whole-H42-fixed-twelve-original-scalar-intersection-8542.py"
path=Path(os.environ.get("ISP_PHI_H42_FIXED12_SOURCE",str(Path(__file__).with_name(name))))
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="150c6d10552e97914de24d46da398371740963205022cebd92f80586aa917e94"
mark=b"\np=1009\n";assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==4023
assert hashlib.sha256(prefix).hexdigest()=="e1a1cdafa32725323b50ac115368a24b77a77ca039c6dde3cdbf43c67241c844"
sc={"__file__":str(path),"__name__":"new_original_scalar_coefficient_definition_only"}
oa=signal.alarm;ot=signal.setitimer;original_setrlimit=resource.setrlimit
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return ot(which,seconds,interval)
 assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return ot(which,min(left,float(seconds) if seconds>0 else left),0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
def fixed_prefix_resource(which,limits):
 if which==resource.RLIMIT_AS:
  return original_setrlimit(which,(4*1024**3,4*1024**3))
 return original_setrlimit(which,limits)
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
resource.setrlimit=fixed_prefix_resource
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":necessary-original-P6-C6-definitions","exec"),sc)
finally:
 resource.setrlimit=original_setrlimit
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
ctx,zero,geo,P6,C6,pc,cc=[sc[k] for k in ["ctx","zero","geo","P6","C6","pc","cc"]]
one=ctx.from_dict({(0,0,0,0,0):fmpq(1)})
lam=ctx.from_dict({(0,0,1,0,0):fmpq(1)})
assert sum((pc[j]*lam**j for j in range(7)),zero)==P6
assert sum((cc[j]*lam**j for j in range(7)),zero)==C6
def data(poly):
 return [[[int(z) for z in ex[:2]],str(c)]
         for ex,c in sorted(poly.to_dict().items())]
def prof(poly):
 ar=data(poly);b=json.dumps(ar,separators=(",",":")).encode()
 return dict(totalDegree=int(poly.total_degree()),
             degrees=list(map(int,poly.degrees()[:2])),
             terms=len(ar),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def lt(poly):
 dd=poly.to_dict();assert dd
 ex=max(dd,key=lambda m:(int(m[0])+int(m[1]),int(m[0])))
 assert not any(ex[2:])
 return tuple(map(int,ex)),dd[ex]
def monomial(ex,c=fmpq(1)):
 assert all(z>=0 for z in ex) and not any(ex[2:])
 return ctx.from_dict({tuple(ex):c})
def divides(a,b):return all(a[j]<=b[j] for j in range(5))
transcript=hashlib.sha256();transcript_bytes=0;nodes=0
polynomial_returns=0;weight_divisions=0;reductions=0
def node(op,parents,poly,**params):
 global nodes,transcript_bytes
 record=dict(id=nodes,op=op,parents=parents,parameters=params,
             terms=len(poly.to_dict()),totalDegree=int(poly.total_degree()))
 line=json.dumps(record,separators=(",",":")).encode()
 transcript.update(line+b"\n");transcript_bytes+=len(line)+1
 result={"id":nodes,"poly":poly};nodes+=1
 return result
def paid_normalize(a):
 global polynomial_returns,weight_divisions
 f=a["poly"]
 if not f:return a
 r,u,hist=geo["strip_paid"](f,False)
 assert r*u==f
 polynomial_returns+=1
 if u!=one:
  weight_divisions+=1
  a=node("divide_only_original_paid_weight",[a["id"]],r,
         originalPaidFactor=prof(u),originalPaidHistory=hist,
         exactFullPolynomialProductReturned=True)
 else:r=f
 _,lc=lt(r)
 if lc!=1:
  rr=r/lc;assert rr*lc==r
  polynomial_returns+=1
  a=node("divide_nonzero_QQ_constant",[a["id"]],rr,constant=str(lc))
 return a
seeds=[]
for family,coeffs in [("P6",pc),("C6",cc)]:
 for j,poly in enumerate(coeffs):
  for ex in poly.to_dict():assert not any(ex[2:])
  if poly:
   a=node("actual_original_lambda_coefficient",[],poly,
          originalFamily=family,lambdaPower=j,
          actualCoefficient=prof(poly))
   seeds.append((family,j,paid_normalize(a)))
say("new_original_scalar_complete_coefficient_input",
 originalP6LambdaDegree=6,originalC6LambdaDegree=6,
 bothFullCoefficientAssemblyProductsReturned=True,
 originalP6Identity="P6*D in I4; P6 is necessary only on physical D!=0",
 originalC6Identity="C6 in I10 on the whole current Phi weight chart",
 nonzeroCoefficientCount=len(seeds),
 paidStrippedCoefficientProfiles=[dict(family=f,lambdaPower=j,polynomial=prof(a["poly"]))
                                 for f,j,a in seeds],
 onlyPreviouslyPaidWeightUnitsDivided=True,
 noNewHeadOrGeometricDInverse=True,
 noPriorResultantDeterminantOrRankGateReplayed=True,
 noWholePhiExclusionClaim=True)
basis=[];heads=[];pairs=[];pair_serial=0
processed_pairs=0;product_pairs=0
def checkpoint(stage,**extra):
 say(stage,basisSize=len(basis),pendingPairs=len(pairs),
     processedPairs=processed_pairs,productCriterionPairs=product_pairs,
     reductions=reductions,exactFullPolynomialReturns=polynomial_returns,
     originalPaidWeightDivisions=weight_divisions,
     sourceDAGNodes=nodes,sourceDAGDefinitionBytes=transcript_bytes,
     sourceDAGDefinitionSHA256=transcript.hexdigest(),**extra)
def reduce_full(a):
 global reductions,polynomial_returns
 while a["poly"]:
  dd=a["poly"].to_dict();chosen=None
  for ex in sorted(dd,key=lambda m:(int(m[0])+int(m[1]),int(m[0])),reverse=True):
   for i,(hm,hc) in enumerate(heads):
    if divides(hm,ex):
     chosen=(ex,dd[ex],i,hm,hc);break
   if chosen is not None:break
  if chosen is None:return a
  ex,c,i,hm,hc=chosen
  exp=tuple(int(ex[j])-hm[j] for j in range(5))
  scalar=c/hc;q=monomial(exp,scalar)
  r=a["poly"]-q*basis[i]["poly"]
  assert r+q*basis[i]["poly"]==a["poly"]
  polynomial_returns+=1;reductions+=1
  a=node("exact_complete_original_polynomial_reduction",
         [a["id"],basis[i]["id"]],r,
         multiplierMonomial=list(exp[:2]),multiplierConstant=str(scalar))
  if reductions%50==0:
   checkpoint("new_original_scalar_coefficient_ideal_reduction_checkpoint",
              currentPolynomial=prof(r),unitIdealNotYetClaimed=True)
 return a
def add_basis(a):
 global pair_serial
 a=paid_normalize(reduce_full(a))
 if not a["poly"]:return None
 # Dividing a paid factor may change the leading monomial.
 a=reduce_full(a)
 if not a["poly"]:return None
 a=paid_normalize(a)
 i=len(basis);hm,hc=lt(a["poly"])
 basis.append(a);heads.append((hm,hc))
 for j,(jm,jc) in enumerate(heads[:-1]):
  lm=tuple(max(hm[z],jm[z]) for z in range(5))
  heapq.heappush(pairs,(sum(lm),lm[0],pair_serial,j,i,lm))
  pair_serial+=1
 checkpoint("new_original_scalar_coefficient_ideal_generator",
            newGenerator=i,newPolynomial=prof(a["poly"]),
            isNonzeroQQConstant=(int(a["poly"].total_degree())==0),
            noWholePhiExclusionClaim=True)
 return i
unit_index=None
seeds.sort(key=lambda item:(int(item[2]["poly"].total_degree()),
                             len(item[2]["poly"].to_dict()),item[0],item[1]))
for family,j,a in seeds:
 i=add_basis(a)
 if i is not None and int(basis[i]["poly"].total_degree())==0:
  unit_index=i;break
while unit_index is None and pairs:
 _,_,_,i,j,lm=heapq.heappop(pairs)
 processed_pairs+=1
 hi,ci=heads[i];hj,cj=heads[j]
 if all(min(hi[z],hj[z])==0 for z in range(5)):
  product_pairs+=1;continue
 ei=tuple(lm[z]-hi[z] for z in range(5))
 ej=tuple(lm[z]-hj[z] for z in range(5))
 mi=monomial(ei,1/ci);mj=monomial(ej,1/cj)
 s=mi*basis[i]["poly"]-mj*basis[j]["poly"]
 assert s+mj*basis[j]["poly"]==mi*basis[i]["poly"]
 polynomial_returns+=1
 a=node("exact_original_coefficient_critical_pair",
        [basis[i]["id"],basis[j]["id"]],s,
        leftMonomial=list(ei[:2]),leftConstant=str(1/ci),
        rightMonomial=list(ej[:2]),rightConstant=str(1/cj))
 index=add_basis(a)
 if index is not None and int(basis[index]["poly"].total_degree())==0:
  unit_index=index;break
if unit_index is not None:
 assert basis[unit_index]["poly"]==one
 checkpoint("new_complete_original_scalar_coefficient_unit_identity",
  actualConstantOneReturned=True,finalSourceDAGNode=basis[unit_index]["id"],
  exactOriginalConsequence="1 belongs to the ideal of every lambda coefficient of P6 and C6, after only previously paid weight localization",
  noAllowedWeightHasBothScalarPolynomialsIdenticallyZero=True,
  everyFixedPhysicalWeightHasSomeNonzeroNecessaryLambdaPolynomialOfDegreeAtMostSix=True,
  noFiniteLambdaRootDiscarded=True,
  allH42H19AndOtherLeadingZeroFibresRetained=True,
  noWholePhiExclusionClaim=True,ordinaryISPClaim=False,
  noRecomputablePayloadSaved=True,
  peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
else:
 checkpoint("new_original_scalar_coefficient_base_locus_not_excluded",
  actualConstantOneReturned=False,
  finalNecessaryGeneratorProfiles=[prof(a["poly"]) for a in basis],
  noBaseLocusEmptinessClaim=True,
  allFiniteExceptionalWeightsAndLambdaFibresRetained=True,
  noWholePhiExclusionClaim=True,ordinaryISPClaim=False,
  noRecomputablePayloadSaved=True,
  peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
