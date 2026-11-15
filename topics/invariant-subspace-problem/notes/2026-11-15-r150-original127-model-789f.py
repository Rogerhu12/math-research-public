#!/usr/bin/env python3
"""Exact original17 model for the independent fixed-prime127 computation.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-15.
All4433 original coefficients and all6188 original source labels are checked.
No F31 coefficient, prebasis operation or parameter-module basis is lifted.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,sys,time
from pathlib import Path
P=127
PRIMITIVE_RAW_SHA="fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3"
MODEL31_SHA="291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"
def sha(b):return hashlib.sha256(b).hexdigest()
def check(ok,msg):
 if not ok:raise ValueError(msg)
def atomic(path,obj):
 q=path.with_name(path.name+".tmp")
 q.write_text(json.dumps(obj,sort_keys=True,separators=(",",":"))+"\n")
 os.replace(q,path)
def monomials(degree):
 result=[]
 def visit(left,lo,key):
  if left==0:result.append(key);return
  for i in range(lo,11):visit(left-1,i,key+(1<<(3*i)))
 visit(degree,0,0)
 return result
def main():
 p=argparse.ArgumentParser()
 for key in ("primitive","original-model","out"):p.add_argument("--"+key,type=Path,required=True)
 a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
 r={"format":"r150-original-fixed127-model-v2","status":"running",
    "parameters":{"prime":P,"author":"Astra-ISP-789f / normal_annihilator",
    "aiAssisted":"GPT-6 Astra Pro","newModuleRankComputed":False,
    "newTorsionDegreeComputed":False,"newInfinityGoodReductionProved":False,
    "largeDataTemporaryOnly":True},"events":[]}
 try:
  raw=a.primitive.read_bytes()
  if raw[:2]==b"\x1f\x8b":raw=gzip.decompress(raw)
  check(len(raw)==158741 and sha(raw)==PRIMITIVE_RAW_SHA,"original integer equations")
  exact=json.loads(raw)
  check(exact["format"]=="r150-original-primitive-integer-equations-v1","primitive format")
  old=a.original_model.read_bytes()
  check(len(old)==128145 and sha(old)==MODEL31_SHA,"paid original source dictionary")
  tokens=old.decode("ascii").split();at=0
  check(tokens[at]=="R150_NATIVE_NF_V1","paid F31 input header");at+=1
  eq=[[[int(c) for c in poly] for poly in row] for row in exact["equations"]]
  check(len(eq)==17 and all(len(row)==77 for row in eq),"original17/77 entries")
  denominator=int(exact["denominator"]);contents=[int(x) for x in exact["contents"]]
  check(len(contents)==17 and all(x%31 for x in [denominator,*contents]),"paid31 row units")
  units127=all(x%P for x in [denominator,*contents])
  r["parameters"]["allOriginalRowNormalizationConstantsAre127Units"]=units127
  r["parameters"]["rowNormalizationResidues127"]=[x%P for x in [denominator,*contents]]
  check(units127,"fixed127 row normalization qualification failed")
  arrays=[];checked=0
  def coeff(poly,k):return poly[k] if k<len(poly) else 0
  for i in range(11):
   row=eq[i]
   check(all(not any(q[1:]) for q in row[11:]),"constant N quadratic heads")
   check(all(not any(q[11:]) for q in row[:11]),"N linear parameter bound10")
   values=[coeff(row[11+k],0) for k in range(66)]
   values += [coeff(row[v],d) for v in range(11) for d in range(11)]
   for c in values:
    check(c%31==int(tokens[at]),"original N all-coefficient mod31 identity")
    at+=1;checked+=1
   arrays.append([c%P for c in values])
  check(int(tokens[at])==3333,"same source selection count");at+=1
  pre=[]
  for _ in range(3333):
   e,mult,pivot,raw_id=map(int,tokens[at:at+4]);at+=4
   pre.append([e,mult,pivot,raw_id])
  gamma=[]
  for i in range(11,17):
   row=eq[i]
   check(all(not any(q) for q in row[:11]),"Gamma has no linear part")
   check(all(not any(q[6:]) for q in row[11:]),"Gamma parameter bound5")
   values=[coeff(row[11+k],d) for k in range(66) for d in range(6)]
   for c in values:
    check(c%31==int(tokens[at]),"original Gamma all-coefficient mod31 identity")
    at+=1;checked+=1
   gamma.append([c%P for c in values])
  ns,nt=map(int,tokens[at:at+2]);at+=2
  check((ns,nt)==(2195,9),"legacy source subset and nine targets only")
  legacy_rest=[]
  for _ in range(ns):
   legacy_rest.append(list(map(int,tokens[at:at+3])));at+=3
  targets=list(map(int,tokens[at:at+nt]));at+=nt
  check(at==len(tokens) and targets==list(range(2,11)),"complete original dictionary EOF")
  source_mon=sum((monomials(d) for d in range(4)),[])
  source_index={key:i for i,key in enumerate(source_mon)}
  check(len(source_mon)==364 and len(source_index)==364,"all original multiplier monomials")
  output_mon={d:set(monomials(d)) for d in range(1,6)}
  def degree(k):return sum((k>>(3*i))&7 for i in range(11))
  ids=[]
  for e,mult,pivot,raw_id in pre:
   check(0<=e<11 and mult in source_index,"prebasis original N multiplier")
   check(raw_id==17*source_index[mult]+e+1,"prebasis exact original source index")
   check(pivot in output_mon[degree(mult)+2],"old proposed pivot dictionary only")
   ids.append(raw_id)
  check(len(ids)==3333 and len(set(ids))==3333,"distinct original prebasis sources")
  pre_ids=set(ids);legacy_ids=[]
  for e,mult,raw_id in legacy_rest:
   check(0<=e<17 and mult in source_index,"legacy remaining original source multiplier")
   check(raw_id==17*source_index[mult]+e+1,"legacy exact original source index")
   check(raw_id not in pre_ids,"legacy source outside the original prebasis")
   legacy_ids.append(raw_id)
  check(len(legacy_ids)==2195 and len(set(legacy_ids))==2195,"distinct legacy source subset")
  # The old input omits 660 original labels. Their old-field behaviour is not used.
  # Generate every source directly, then take only the exact prebasis complement.
  all_sources=[[e,mult,17*k+e+1] for k,mult in enumerate(source_mon) for e in range(17)]
  check([v[2] for v in all_sources]==list(range(1,6189)),"entire monomial-major original source dictionary")
  rest=[v for v in all_sources if v[2] not in pre_ids]
  rest_ids={v[2] for v in rest};ns=len(rest)
  check(len(pre)+ns==6188 and len(rest_ids)==ns,"complete original prebasis complement")
  check(set(legacy_ids)<=rest_ids,"legacy subset included in new complete input")
  omitted=sorted(rest_ids-set(legacy_ids))
  check(ns==2855 and len(omitted)==660,"exact newly restored original source count")
  check(sorted(ids+[v[2] for v in rest])==list(range(1,6189)),"3333 plus2855 is a disjoint complete original partition")
  def histogram(rows):
   by_equation=[0]*17;by_degree=[0]*4;joint=[[0]*4 for _ in range(17)]
   for row in rows:
    e,mult=row[:2];d=degree(mult)
    by_equation[e]+=1;by_degree[d]+=1;joint[e][d]+=1
   return {"byEquation":by_equation,"byMultiplierDegree":by_degree,"byEquationAndMultiplierDegree":joint}
  omitted_set=set(omitted)
  histograms={"prebasis3333":histogram(pre),"legacySubset2195":histogram(legacy_rest),
              "restored660":histogram([v for v in rest if v[2] in omitted_set]),
              "completeComplement":histogram(rest)}
  check(checked==4433,"all original parameter coefficients retained")
  lines=["R150_NATIVE_NF127_V2"]
  lines.extend(" ".join(map(str,v)) for v in arrays)
  lines.append("3333");lines.extend(" ".join(map(str,v)) for v in pre)
  lines.extend(" ".join(map(str,v)) for v in gamma)
  lines.append(str(ns)+" "+str(nt));lines.extend(" ".join(map(str,v)) for v in rest)
  lines.append(" ".join(map(str,targets)))
  data=("\n".join(lines)+"\n").encode("ascii")
  model_path=a.out/"original127-normal-form-input.txt";model_path.write_bytes(data)
  original_dictionary={"originalSelected3333":pre,"originalRemainingSources":rest,
                       "originalSourceCount":6188,"remainingSourceCount":ns,
                       "legacySubsetOriginalSourceIDs":legacy_ids,
                       "newlyRestoredOriginalSourceIDs":omitted,
                       "targetLabels":targets,"field":P}
  dictionary=a.out/"original127-source-dictionary.json"
  atomic(dictionary,original_dictionary)
  binding_data={"primitiveSHA256":PRIMITIVE_RAW_SHA,"oldModelSHA256":MODEL31_SHA,
                "sourceSHA256":sha(Path(__file__).read_bytes()),"prime":P}
  r["binding"]=sha(json.dumps(binding_data,sort_keys=True,separators=(",",":")).encode())
  r["parameters"].update({"identity":binding_data,"all4433OriginalCoefficientChecks":True,
    "all6188OriginalSourceLabelsVerified":True,"allOriginalSourcesPartitioned":True,
    "selectedSourceCount":len(pre),"remainingSourceCount":ns,"originalSourceCount":6188,
    "legacyRemainingSourceCount":len(legacy_ids),"newlyRestoredSourceCount":len(omitted),
    "sourceSubsetHistograms":histograms,"legacyAndPrebasisEachDistinctAndDisjoint":True,
    "newlyRestoredSourcesAssumedZero":False,"everyRemainingSourceMustBeRecomputedAt127":True,
    "oldField31OperationsReused":False,"oldPivotPositionsRequiredAt127":False,
    "originalModel":{"file":model_path.name,"bytes":len(data),"sha256":sha(data)},
    "originalDictionary":{"file":dictionary.name,"bytes":dictionary.stat().st_size,
                          "sha256":sha(dictionary.read_bytes())},
    "originalNHeadAndGammaDegreeBoundsVerified":True})
  r["status"]="completed";r["outcome"]="exact-original127-model-ready-no-new-module-computation";rc=0
 except BaseException as e:
  r["status"]="failed";r["errorType"]=type(e).__name__;r["error"]=str(e);rc=1
 r["elapsedSeconds"]=time.monotonic()-start
 atomic(a.out/"original127-model-receipt.json",r)
 print(json.dumps({"status":r["status"],"elapsedSeconds":r["elapsedSeconds"],"error":r.get("error")}),flush=True)
 return rc
if __name__=="__main__":sys.exit(main())
