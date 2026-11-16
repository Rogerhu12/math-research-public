#!/usr/bin/env python3
"""Qualify every original coefficient of the Bell cube model at prime7.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

This computes no Macaulay rank. It retains all seventeen original gradients,
three exact rational Bell-cube components, and complete weighted dictionaries.
Only sources, parameters, execution identity and hashes may be committed.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,resource,signal,time
from pathlib import Path
from flint import fmpq
FORMAT="r150-original-bell-cube-complete-prime7-coefficient-audit-v1"
PINS={
 "producer":(26381,"213c10f680c5325e62b5245b0796062b5024c1499e9d1d68346ad65868d120dd"),
 "model":(31156,"da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d"),
 "helper":(16964,"31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10")}
class Budget(Exception):pass
def need(v,msg):
 if not v:raise ValueError(msg)
def identity(p):
 raw=p.read_bytes();return {"path":p.name,"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}
def module(p,name):
 sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def main():
 ap=argparse.ArgumentParser()
 for name in ("producer","model","helper","out"):ap.add_argument("--"+name,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=90)
 ap.add_argument("--memory-mib",type=int,default=768)
 a=ap.parse_args()
 need(0<a.seconds<=180 and 256<=a.memory_mib<=2048,"bounded coefficient-only resources")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 a.out.mkdir(parents=True,exist_ok=True);begin=time.monotonic()
 pins={}
 for k,(size,digest) in PINS.items():
  pins[k]=identity(getattr(a,k));need(pins[k]["bytes"]==size and pins[k]["sha256"]==digest,"exact original "+k)
 fd=module(a.model,"r150_p7_complete_model")
 prod=module(a.producer,"r150_p7_three_targets")
 physical=module(a.helper,"r150_p7_original_physical")
 sem={"format":FORMAT,"source":identity(Path(__file__)),"inputs":pins,"prime":7,
      "originalVariableCount":17,"originalGradientCount":17,"rationalTargetCount":3,"targetWeight":9,
      "algorithm":"all-original-Q-coefficients-and-complete-weighted-source-output-dictionaries"}
 binding=fd.digest(fd.canonical(sem))
 rec={"format":FORMAT,"binding":binding,"status":"running","parameters":{"semantic":sem,
      "seconds":a.seconds,"memoryMiB":a.memory_mib,"MacaulayRankComputed":False,
      "newBellMembershipOrNonmembershipClaimed":False}}
 rp=a.out/"original-bell-cube-complete-prime7-coefficient-audit.json"
 def save():
  rec["elapsedSeconds"]=time.monotonic()-begin
  rec["parameters"]["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  fd.json_save(rp,rec)
 def stop(signum,frame):raise Budget("coefficient audit signal "+str(signum))
 signal.signal(signal.SIGALRM,stop);signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 signal.setitimer(signal.ITIMER_REAL,a.seconds)
 code=1
 try:
  save();model=prod.prepare(fd,physical)
  need(model["all17OriginalGradientPolynomialsVerified"] and model["allWeightedEulerCoefficientsVerified"] and
       model["allThreeTargetsWeightNineVerified"] and model["allThreeFieldComponentsRecombineToOriginalCube"],
       "all complete original Q and legal127 model products")
  families={"gradients":model["originalSeventeenGradients"],
            "bellComponents":model["BellFieldComponents"],
            "cubeComponents":model["naturalCubeRationalComponents"]}
  bad=[];counts={};field={};total=0
  for label,polys in families.items():
   field[label]=[];counts[label]=[]
   for col,poly in enumerate(polys):
    one={};invalid=0
    for exponent,coefficient in poly:
     need(len(exponent)==17 and all(type(x) is int and x>=0 for x in exponent),"all original exponent coordinates")
     q=fmpq(coefficient);num=int(q.numer());den=int(q.denom());total+=1
     if den%7==0:
      invalid+=1
      if len(bad)<32:bad.append({"family":label,"column":col,"exponent":exponent,
                                "numerator":str(num),"denominator":str(den)})
     else:
      value=(num%7)*pow(den%7,-1,7)%7
      if value:one[tuple(exponent)]=value
    field[label].append(fd.poly_record(one))
    counts[label].append({"rationalTerms":len(poly),"field7NonzeroTerms":len(one),"badDenominatorCount":invalid})
  cubic=[int(x) for x in model["matchedCubic"]]
  values=[sum(c*pow(x,i,7) for i,c in enumerate(cubic))%7 for x in range(7)]
  jdet=int(model["J3Determinant"])
  admissible=(not any(z["badDenominatorCount"] for family in counts.values() for z in family)
              and cubic[-1]%7!=0 and jdet%7!=0 and all(values))
  output=physical.weighted_monomials(9)
  five=physical.weighted_monomials(5);four=physical.weighted_monomials(4)
  need(len(output)==49368 and len(five)==1264 and len(four)==423 and
       len(set(output))==49368 and len(set(five))==1264 and len(set(four))==423,
       "complete original weighted dictionaries and no duplicate monomials")
  need(all(sum(e*w for e,w in zip(z,physical.WEIGHTS))==9 for z in output) and
       all(sum(e*w for e,w in zip(z,physical.WEIGHTS))==5 for z in five) and
       all(sum(e*w for e,w in zip(z,physical.WEIGHTS))==4 for z in four),
       "all original weights of complete source and output dictionaries")
  need(11*len(five)+6*len(four)==16442,"all complete original weighted9 source columns")
  if admissible:
   from flint import nmod_mpoly_ctx
   ctx=nmod_mpoly_ctx.get(tuple(physical.VARNAMES),7,"lex")
   bells=[ctx.from_dict({tuple(e):int(c) for e,c in z}) for z in field["bellComponents"]]
   products=[ctx.from_dict({}) for _ in range(7)]
   for i in range(3):
    for j in range(3):
     for k in range(3):products[i+j+k]+=bells[i]*bells[j]*bells[k]
   monic=[(c%7)*pow(cubic[-1]%7,-1,7)%7 for c in cubic[:3]]
   for degree in range(6,2,-1):
    z=products[degree]
    for k in range(3):products[degree-3+k]-=z*monic[k]
    products[degree]=ctx.from_dict({})
   need(all(products[k]==ctx.from_dict({tuple(e):int(c) for e,c in field["cubeComponents"][k]})
            for k in range(3)),"all three independent F7 coefficient-algebra cube products")
  data={"format":FORMAT+"-complete-data","binding":binding,"semantic":sem,
        "completeOriginalRationalModel":model,"allField7Polynomials":field,
        "completeWeight9OutputMonomials":output,"completeQuarticWeight5SourceMonomials":five,
        "completeQuinticWeight4SourceMonomials":four,
        "field7ModelAdmitted":admissible,"rankNotComputed":True}
  desc=fd.gz_save(a.out/"complete-original-weight9-prime7-model.json.gz",data)
  rec["parameters"].update(
   allOriginalCoefficientCount=total,perPolynomialCounts=counts,
   firstBadDenominators=bad,originalJ3DeterminantModulo7=jdet%7,
   originalMatchedCubicModulo7=[c%7 for c in cubic],allSevenCubicValues=values,
   cubicIrreducibleOverF7=(cubic[-1]%7!=0 and all(values)),
   completeOriginalWeight9OutputRows=49368,completeOriginalWeight9SourceColumns=16442,
   weight5SourceMonomials=1264,weight4SourceMonomials=423,
   completeOutputDictionarySHA256=fd.digest(fd.canonical(output)),
   completeQuarticSourceDictionarySHA256=fd.digest(fd.canonical(five)),
   completeQuinticSourceDictionarySHA256=fd.digest(fd.canonical(four)),
   allThreeF7CoefficientAlgebraCubeProductsVerified=admissible,
   allCompleteOriginalRationalProductsVerified=True,allOriginalCoefficients7Integral=not any(
       z["badDenominatorCount"] for family in counts.values() for z in family),
   prime7CompleteOriginalModelAdmitted=admissible,
   temporaryCompleteModel=desc,
   outcome="complete-original-prime7-coefficient-admission" if admissible else "prime7-admission-not-established",
   noRankOrNewMembershipConclusion=True)
  rec["status"]="completed";save();code=0
 except Budget as e:
  rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
  save();code=75
 except BaseException as e:
  rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
  save();code=1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);save()
  print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
 return code
if __name__=="__main__":raise SystemExit(main())
