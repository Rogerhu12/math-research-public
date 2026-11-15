#!/usr/bin/env python3
"""Rebuild the complete root2 fourth-page source recipes from paid B2/B3.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-15.

This computes only finite-field source recipes, whole315 correction maps and
their exact completeness checks. It does not compute any new original p^7
product or assert the fourth image rank. All 210 recipes are retained.
"""
from __future__ import annotations
import argparse, gzip, hashlib, importlib.util, json, os, resource
import signal, struct, sys, time
from math import comb
from pathlib import Path
sys.dont_write_bytecode = True
from flint import nmod_mat

P = 31
P7 = 27512614111
AUTHOR = "Astra-ISP-789f / normal_annihilator"
HELPER_SHA = "3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a"
READER_SHA = "8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2"
STATE_SHA = "06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"
ALL204 = [7001,7002,7005,7006,7007,7004] + list(range(15001,15199))
ALL208 = list(range(20001,20209))
ALL210 = list(range(30001,30211))
PINS = {
 "second_prepared_receipt": (18840, "f8ffc939972363e79d0027946c5268c32f869e90adc6fead115fbd29b0ea1ca4"),
 "second_prepared_system": (42012, "691717421b0b7558f7ca053054c6c3f23bde5aa96fc93f36a744ad1171c4ba03"),
 "second_complete_receipt": (22107, "50e8aa0cecafc697b1d52a43792e095be35c4dadc71eff07b861569591d092b7"),
 "second_complete_system": (72934, "f20487d290193e738a5df67dccdf0c6d11c1c0b9e224dbd310fdc1a0180acaf7"),
 "third_complete_receipt": (17757, "3bb98210ccf8a7941f2a9a71c0d8d1a5fc8c0e11891c26d0e76d8079fa413619"),
 "third_complete_system": (70591, "786333a4baa562a15e38666a31207e3ce0179e03a0e9505da2d6a4cc5fbe7c2c"),
}
OLD_KERNEL_BYTES = 137217
OLD_KERNEL_SHA = "f136d6f396831091766bf10cf77421af7dbedf58ab9f87a417b00133e38dfe7d"

class BudgetStop(Exception): pass
def check(ok, text):
 if not ok: raise ValueError(text)
def sha(raw): return hashlib.sha256(raw).hexdigest()
def canonical(obj):
 return json.dumps(obj, sort_keys=True, separators=(",",":"), ensure_ascii=True).encode("ascii")
def atomic(path, obj):
 tmp = path.with_name(path.name+".tmp")
 tmp.write_bytes(canonical(obj)+b"\n")
 os.replace(tmp,path)
def import_module(path, name, expected):
 check(sha(path.read_bytes()) == expected, "pinned Python source "+path.name)
 spec=importlib.util.spec_from_file_location(name,path)
 module=importlib.util.module_from_spec(spec)
 spec.loader.exec_module(module)
 return module
def rows(A):
 return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def serial(A):
 return bytes(int(A[i,j]) for i in range(A.nrows()) for j in range(A.ncols()))
def matrix_record(A):
 raw=serial(A)
 return {"rows":A.nrows(),"columns":A.ncols(),"sha256":sha(raw)}
def identity(n):
 return nmod_mat([[int(i==j) for j in range(n)] for i in range(n)], P)
def section(n, indices):
 T=[[[] for _ in indices] for _ in range(n)]
 for j,i in enumerate(indices): T[i][j]=[1]
 return T
def source_kernel(h,C,J,T):
 n=C.ncols(); r=C.nrows()
 F=[[[] for _ in range(n+r)] for _ in range(n)]
 for i in range(n):
  F[i][i]=[1]
  for k in range(r):
   if not T[i][k]: continue
   for j in range(n):
    if C[k,j]: F[i][j]=h.add(F[i][j],T[i][k],-int(C[k,j]))
  for j in range(r):
   F[i][n+j]=([0]+T[i][j]) if T[i][j] else []
   for k in range(r):
    if J[k,j] and T[i][k]:
     F[i][n+j]=h.add(F[i][n+j],T[i][k],-int(J[k,j]))
 return F
def compose(h,A,B):
 result=[[[] for _ in B[0]] for _ in A]
 for i,row in enumerate(A):
  for k,a in enumerate(row):
   if a:
    for j,b in enumerate(B[k]):
     if b: result[i][j]=h.add(result[i][j],h.mul(a,b))
 return result
def evaluate(h,A,s):
 return nmod_mat([[h.value(p,s) for p in row] for row in A],P)
def t_lift(polynomial):
 return [sum(int(polynomial[d])*comb(d,k)*2**(d-k)
             for d in range(k,len(polynomial))) % P7
         for k in range(len(polynomial))]
def read_system(path, receipt, magic):
 raw=gzip.decompress(path.read_bytes())
 q=receipt["system"]
 check(len(raw)==q["uncompressedBytes"] and sha(raw)==q["uncompressedSHA256"],
       "complete historical matrix payload")
 check(raw[:8]==magic, "historical matrix magic")
 return raw
def require_flags(receipt, flags):
 check(receipt.get("status")=="completed", "paid complete historical result")
 for flag in flags: check(receipt.get(flag) is True, "paid flag "+flag)

def main():
 ap=argparse.ArgumentParser()
 for key in tuple(PINS)+("state","reader","helper","out"):
  ap.add_argument("--"+key.replace("_","-"),type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=30)
 ap.add_argument("--memory-mib",type=int,default=512)
 a=ap.parse_args()
 check(0<a.seconds<=120 and 256<=a.memory_mib<=2048,"explicit resource bounds")
 a.out.mkdir(parents=True,exist_ok=True)
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 started=time.monotonic()
 receipt_path=a.out/"root2-fourth-complete210-source-preparation-receipt.json"
 rec={"format":"r150-root2-fourth-complete210-source-preparation-v1",
      "status":"running","parameters":{"author":AUTHOR,"aiAssisted":"GPT-6 Astra Pro",
      "prime":P,"newOriginalMod31SevenProductsComputed":False,
      "newFourthImageComputed":False,"fourthImageRank":None,
      "largeDataTemporaryOnly":True},"events":[]}
 def tick():
  if time.monotonic()-started>=a.seconds: raise BudgetStop("preparation budget")
 def interrupted(signum,frame): raise BudgetStop("preparation signal")
 signal.signal(signal.SIGTERM,interrupted);signal.signal(signal.SIGINT,interrupted)
 signal.signal(signal.SIGALRM,interrupted);signal.setitimer(signal.ITIMER_REAL,a.seconds)
 try:
  actual={}
  for key,(size,digest) in PINS.items():
   path=getattr(a,key); raw=path.read_bytes()
   check(len(raw)==size and sha(raw)==digest,"exact historical "+key)
   actual[key]={"bytes":size,"sha256":digest}
  h=import_module(a.helper,"r150_b4_paid_matrix_arithmetic",HELPER_SHA)
  reader=import_module(a.reader,"r150_b4_paid_torsion_reader",READER_SHA)
  state_raw=a.state.read_bytes()
  if state_raw[:2]==b"\x1f\x8b": state_raw=gzip.decompress(state_raw)
  check(len(state_raw)==1470456 and sha(state_raw)==STATE_SHA,"whole315 torsion state")
  state_path=a.out/"same-original-torsion-state.bin"
  state_path.write_bytes(state_raw)
  try: state=reader.load_state(state_path)
  finally: state_path.unlink(missing_ok=True)
  check((state["stateDimension"],state["torsionDimension"],state["observabilityRank"])==(820,315,505),
        "same full820/315/505 state")
  J=nmod_mat(state["matrices"]["action"],P)
  check(J.nrows()==315 and J.ncols()==315,"complete original multiplication by s")
  pr=json.loads(a.second_prepared_receipt.read_text())
  sr=json.loads(a.second_complete_receipt.read_text())
  tr=json.loads(a.third_complete_receipt.read_text())
  require_flags(pr,("complete204SourceKernelGenerationProved",
    "all198TrueSevenCorrectionsVerified","all1834OriginalKernelDirectionsHaveExactBKernelLifts",
    "twoAdditionalExactRelationDirectionsRemoved","allSixOldAndTwoTRelationsRetained"))
  require_flags(sr,("all204TrueOriginalSecondSourcesComputed","allOriginal17DivisionsVerified",
    "all104LocalFreeChecksVerified","completeRelevantSaturatedSecondImageComputed",
    "completeNextPolynomialSourceKernelSaved","originalS2EnvelopeComplete"))
  require_flags(tr,("allTrueOriginalThirdSourcesComputed","allOriginal17DivisionsVerified",
    "all104LocalFreeChecksVerified","completeRelevantSaturatedThirdImageComputed",
    "completeOriginalS2SourceCoverageRetained"))
  check(sr["complete204SourceLabels"]==ALL204 and tr["thirdSourceLabels"]==ALL208,
        "same complete original 204/208 source labels")
  check(sr["secondImageRank"]==4 and tr["thirdImageRank"]==2,
        "paid ranks, not new fourth ranks")
  pb=read_system(a.second_prepared_system,pr,b"R150SP2A")
  sb=read_system(a.second_complete_system,sr,b"R150SS2A")
  tb=read_system(a.third_complete_system,tr,b"R150SS3A")
  U7=h.block(pb,pr,"U7");U9=h.block(sb,sr,"U9");J9=h.block(sb,sr,"J9")
  V10=h.block(pb,pr,"V10");C197=h.block(pb,pr,"trueV10Coordinates")
  PM=h.block(pb,pr,"whole315PrimaryProjector")
  check(h.block(pb,pr,"U9")==U9 and h.block(pb,pr,"J9")==J9,"same U9 basis")
  check(U7.rank()==7 and U9.rank()==9 and J*U9==U9*J9,"actual first incoming basis")
  D4=h.block(sb,sr,"all204Projected315SecondColumns")
  check(PM*D4==D4 and h.zero(h.block(sb,sr,"all104FreeChecks")),"all204 full free gates")
  project2,Jq2,_,_,_,_=h.quotient(J,U9)
  C0=project2(D4);B2=h.block(sb,sr,"imageBasis")
  C2=h.block(sb,sr,"sourceImageCoordinates");J2=h.block(sb,sr,"imageAction")
  check(Jq2==h.block(sb,sr,"quotientAction"),"same complete second quotient")
  check(h.pivots(h.join(C0,Jq2*C0))==[6,7,8,9],"same second section")
  check(B2==h.sub(C0,range(306),[6,7,8,9]) and B2*C2==C0 and B2*J2==Jq2*B2,
        "all204 image factorization and s action")
  T2=section(204,[6,7,8,9]);Tm2=evaluate(h,T2,0)
  check(C2*Tm2==identity(4),"second section right inverse")
  F2=source_kernel(h,C2,J2,T2)
  check(h.zero(h.source_action(Jq2,C0,F2)),"all208 complete second kernel generators")
  old_kernel={"format":"r150-complete-saturated-second-source-kernel-v1","prime":31,
   "sourceLabels204":ALL204,"sourceLabelsForNextPage":ALL208,"imageDimension":4,
   "sectionPolynomialsAscending":T2,"sourceImageCoordinates":rows(C2),"imageSAction":rows(J2),
   "generatorPolynomialsAscending":F2,"generatorCount":208,
   "maximumPolynomialDegree":max(len(p)-1 for row in F2 for p in row),
   "formula":"I-T*C and T*(sI-J)","allGeneratorImagesVerifiedZero":True,
   "completePolynomialSourceKernelByActualSection":True,
   "all204ActualIntegerSecondSourcesRequired":True,"nextPageIntegerCarryNotYetComputed":True}
  old_bytes=(json.dumps(old_kernel,separators=(",",":"))+"\n").encode()
  check(len(old_bytes)==OLD_KERNEL_BYTES and sha(old_bytes)==OLD_KERNEL_SHA,
        "exact reconstruction of paid complete 208 recipe bytes")
  rec["events"].append({"event":"paid208-source-recipe-reconstructed","sha256":sha(old_bytes),
                        "elapsedSeconds":time.monotonic()-started})
  tick()
  b8=h.sub(U9,range(315),[7]);d3=V10*h.sub(C197,range(10),[0])
  true9=h.join(U7,b8,d3)
  check(true9.rank()==9,"true first nine original divide-source basis")
  M4=h.source_action(J,D4,F2)
  old_corr=h.solve_span(true9,M4)
  check(old_corr["indices"]==list(range(9)) and all(old_corr["flags"])
        and true9*old_corr["solution"]==M4,"all315 old true corrections")
  W2=D4*Tm2
  canonical13=h.join(U9,W2)
  check(canonical13==h.block(tb,tr,"incomingSpace315"),"same complete third incoming basis")
  check(canonical13.rank()==13 and J*canonical13==canonical13*h.block(tb,tr,"incomingAction"),
        "all original third incoming action")
  D5=h.block(tb,tr,"allProjected315ThirdColumns")
  check(PM*D5==D5 and h.zero(h.block(tb,tr,"all104FreeChecks")),"all208 third free gates")
  project3,Jq3,_,_,_,_=h.quotient(J,canonical13)
  C03=project3(D5)
  check(Jq3==h.block(tb,tr,"quotientAction"),"same entire third quotient")
  check(h.join(C03,Jq3*C03)==h.block(tb,tr,"completeThirdKrylov"),
        "all208 third columns and complete s closure retained")
  check(h.pivots(h.join(C03,Jq3*C03))==[10,11],"actual third section, not a chosen guess")
  B3=h.sub(C03,range(302),[10,11]);J3=h.block(tb,tr,"imageAction")
  check(B3==h.block(tb,tr,"imageBasis") and B3.rank()==2,"paid actual two-dimensional image")
  sol3=h.solve_span(B3,C03)
  check(sol3["indices"]==[0,1] and all(sol3["flags"]),"whole208 image coordinates")
  C3=sol3["solution"]
  check(B3*C3==C03 and B3*J3==Jq3*B3,"all208 image factorization and complete s action")
  T3=section(208,[10,11]);Tm3=evaluate(h,T3,0)
  check(C3*Tm3==identity(2),"third section right inverse")
  F3=source_kernel(h,C3,J3,T3)
  check(len(F3)==208 and all(len(row)==210 for row in F3),"all210 generators retained")
  check(h.zero(h.source_action(Jq3,C03,F3)),"complete fourth initial kernel in entire quotient")
  true13=h.join(true9,W2)
  check(true13.rank()==13,"true original divide-source incoming13")
  bridge=h.solve_span(canonical13,true13)
  check(bridge["indices"]==list(range(13)) and all(bridge["flags"]) and
        bridge["solution"].rank()==13 and canonical13*bridge["solution"]==true13,
        "same incoming13 with actual original source transport")
  Jin=h.solve_span(true13,J*true13)
  check(all(Jin["flags"]) and true13*Jin["solution"]==J*true13,"true13 s action")
  M5=h.source_action(J,D5,F3)
  correction=h.solve_span(true13,M5)
  check(correction["indices"]==list(range(13)) and all(correction["flags"]) and
        true13*correction["solution"]==M5,"all315 fourth initial corrections")
  next15=h.join(canonical13,D5*Tm3)
  check(next15.rank()==15,"complete incoming for the future fourth image")
  next_action=h.solve_span(next15,J*next15)
  check(all(next_action["flags"]) and next15*next_action["solution"]==J*next15,
        "complete future incoming s closure")
  F23=compose(h,F2,F3)
  zero2=[j for j in range(208) if all(not F2[i][j] for i in range(204))]
  zero3=[j for j in range(210) if all(not F3[i][j] for i in range(208))]
  zero23=[j for j in range(210) if all(not F23[i][j] for i in range(204))]
  check(zero2==[6,7,8,9] and zero3==[10,11] and zero23==list(range(6,12)),
        "separate direct zero recipes from merely inherited field zero recipes")
  candidate=[j for j in range(210) if j not in zero23]
  candidate_matrix=evaluate(h,[[row[j] for j in candidate] for row in F23],3)
  check(len(candidate)==204 and candidate_matrix.rank()==204,
        "204 independent polynomial recipes in the original204 domain")
  check(J2==2*identity(4) and (J3-2*identity(2))**5==nmod_mat(2,2,P),
        "section transition determinant has only the retained root2 support")
  tick()
  source_hash=sha(Path(__file__).read_bytes())
  identity_data={"sourceSHA256":source_hash,"historicalInputs":actual,
   "stateSHA256":STATE_SHA,"helperSHA256":HELPER_SHA,"readerSHA256":READER_SHA,
   "algorithm":"same whole315 B2/B3 sections; all210 fourth initial recipes; true13 correction"}
  binding=sha(canonical(identity_data));rec["binding"]=binding
  payload={"format":"r150-root2-fourth-complete210-source-preparation-data-v1","binding":binding,
   "prime":P,"sourceLabels204":ALL204,"sourceLabels208":ALL208,"sourceLabels210":ALL210,
   "secondSectionIndices":[6,7,8,9],"thirdSectionIndices":[10,11],
   "secondSectionPolynomialsAscending":T2,"thirdSectionPolynomialsAscending":T3,
   "secondSourceImageCoordinates":rows(C2),"thirdSourceImageCoordinates":rows(C3),
   "secondImageSAction":rows(J2),"thirdImageSAction":rows(J3),
   "secondKernelGeneratorsInSAscending":F2,"thirdKernelGeneratorsInSAscending":F3,
   "thirdKernelCanonicalIntegerTaylorMod31Seven":[[t_lift(p) for p in row] for row in F3],
   "composedOriginal204GeneratorsFieldOnly":F23,
   "oldTrueFirstNineCorrectionsForAll208":rows(old_corr["solution"]),
   "trueThirteenCorrectionsForAll210":rows(correction["solution"]),
   "trueThirteenOriginalDivisorExponents":[1,1,2,2,2,2,2,3,3,4,4,4,4],
   "fourthPrecorrectionMultipliers31Powers":[4,4,3,3,3,3,3,2,2,1,1,1,1],
   "canonical13ToTrue13":rows(bridge["solution"]),
   "true13Full315":rows(true13),"true13SAction":rows(Jin["solution"]),
   "futureCompleteIncoming15Full315":rows(next15),
   "futureCompleteIncoming15SAction":rows(next_action["solution"]),
   "fourthInitialAll210Full315":rows(M5),
   "directZeroF3Indices":zero3,"inheritedFieldZeroF2Indices":zero2,
   "candidate204IndicesAfterSixIntegerZeroGates":candidate,
   "integerCarryScope":{"all210MustBeCarried":True,"originalP7ProductsPaid":False,
    "fourInheritedL5ColumnsExactlyZeroPaid":False,
    "doNotUseComposedFieldRecipesAsIntegerCarry":True,
    "requiredSourcePrecisionChain":[25,20,15,10,5],
    "requiredOriginalModulus":P7,"p7RequiresUint64StorageAndUint128Multiplication":True}}
  raw=canonical(payload)+b"\n";path=a.out/"complete210-fourth-source-recipes.json.gz"
  compressed=gzip.compress(raw,compresslevel=1,mtime=0)
  temp=path.with_name(path.name+".tmp");temp.write_bytes(compressed);os.replace(temp,path)
  record={"file":path.name,"bytes":len(compressed),"sha256":sha(compressed),
          "payloadBytes":len(raw),"payloadSHA256":sha(raw),"temporaryOnly":True}
  rec["parameters"].update({"identity":identity_data,"sourceLabels210":ALL210,
   "completeKernelGenerators":210,"candidateFreeBasisSize":204,
   "actualSecondImageRank":4,"actualThirdImageRank":2,
   "trueIncomingDimension":13,"futureFourthIncomingDimension":15,
   "all315OldAndNewInitialSourceIdentitiesVerified":True,
   "all208ThirdSourceColumnsAndSMultiplesRetained":True,
   "all210InitialKernelImagesVerifiedZero":True,
   "old208RecipeReconstructedByteExactly":True,
   "directZeroF3Indices":zero3,"inheritedFieldZeroF2Indices":zero2,
   "sixOriginalIntegerZeroCarryGatesStillRequired":True,
   "noSourceDroppedFromIntegerContinuation":True,
   "fourthImageRankNotComputed":True,
   "thirdImageSAction":rows(J3),"original204CandidateEvaluationRank":204,
   "retainedAll210TrueCorrectionMatrix":matrix_record(correction["solution"]),
   "futureIncoming15":matrix_record(next15),"savedCompleteRecipe":record})
  rec["status"]="completed";rec["outcome"]="complete210-recipes-ready-original-p7-carry-still-required"
  rc=0
 except BudgetStop as exc:
  rec["status"]="budget-checkpoint";rec["error"]=str(exc);rc=75
 except BaseException as exc:
  rec["status"]="failed";rec["errorType"]=type(exc).__name__;rec["error"]=str(exc);rc=1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0)
  rec["elapsedSeconds"]=time.monotonic()-started
  atomic(receipt_path,rec)
 print(json.dumps({"status":rec["status"],"outcome":rec.get("outcome"),
                  "elapsedSeconds":rec["elapsedSeconds"],"error":rec.get("error")}),flush=True)
 return rc

if __name__=="__main__": sys.exit(main())
