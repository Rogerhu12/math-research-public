#!/usr/bin/env python3
"""Complete root2 third page from the actually completed saturated second page.
No old q1/q2/q3 is recomputed. Full targets and all original source labels remain.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
from flint import nmod_mat
P=31;P6=887503681
HELPER="2026-11-14-r150-ninth-first-matrices-789f.py"
HELPER_SHA="3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a"
TARGETS=list(range(2,11))
OLD6=[7001,7002,7005,7006,7007,7004]
ALL204=OLD6+list(range(15001,15199))
ROOT2_ANN=[30,18,13,9,21,1]
def sha(b):return hashlib.sha256(b).hexdigest()
def load(path,name):
 q=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(q);q.loader.exec_module(m);return m
def save(path,obj):path.write_text(json.dumps(obj,separators=(",",":"))+"\n")
def rows(A):return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def block(h,b,r,k):return h.block(b,r,k)
def spec(path,labels,L,ring):
 path.write_text("R150_S2_LOCAL_JET_SPEC_V1\n31 "+str(len(labels))+" "+str(L)+" "+str(ring)+"\n"+" ".join(map(str,labels))+"\n")
def trim(p):
 p=[int(x)%31 for x in p]
 while p and p[-1]==0:p.pop()
 return p
def add(a,b,c=1):
 a=list(a)+[0]*max(0,len(b)-len(a))
 for i,x in enumerate(b):a[i]=(a[i]+c*x)%31
 return trim(a)
def t_integer_lift(poly):
 # The input is the chosen canonical s-polynomial, not a fresh canonical t lift.
 from math import comb
 return [sum(int(poly[d])*comb(d,k)*2**(d-k) for d in range(k,len(poly)))%P6 for k in range(len(poly))]
def bind_input(path):return {"bytes":path.stat().st_size,"sha256":sha(path.read_bytes())}
def prepare(a,h,started):
 pr=json.loads(a.second_prepared_receipt.read_text());pb=h.actual(a.second_prepared_system,pr["system"]["uncompressedSHA256"])
 sr=json.loads(a.second_complete_receipt.read_text());sb=h.actual(a.second_complete_system,sr["system"]["uncompressedSHA256"])
 kernel=json.loads(a.second_kernel.read_text())
 if pb[:8]!=b"R150SP2A" or sb[:8]!=b"R150SS2A":raise ValueError("actual completed saturated second matrix formats")
 for k in ("all204TrueOriginalSecondSourcesComputed","completeRelevantSaturatedSecondImageComputed","completeNextPolynomialSourceKernelSaved",
           "fullRawTargetsPreserved","all315TargetDecompositionVerified","otherPrimaryTargetsPaidByTrueU9"):
  if sr.get(k) is not True:raise ValueError("actual completed second field "+k)
 if sr.get("status")!="completed" or sr["complete204SourceLabels"]!=ALL204:raise ValueError("actual all204 source identity")
 if not all(kernel.get(k) for k in ("allGeneratorImagesVerifiedZero","completePolynomialSourceKernelByActualSection","all204ActualIntegerSecondSourcesRequired")):raise ValueError("whole second source kernel, not only an image span")
 if kernel["sourceLabels204"]!=ALL204 or kernel["formula"]!="I-T*C and T*(sI-J)":raise ValueError("actual entire next-source construction")
 state,J=h.load_state(a.notes_root,a.out)
 D=block(h,sb,sr,"all204Projected315SecondColumns");U9=block(h,sb,sr,"U9")
 U7=block(h,pb,pr,"U7");J9=block(h,sb,sr,"J9")
 V10=block(h,pb,pr,"V10");C197=block(h,pb,pr,"trueV10Coordinates")
 PM=block(h,pb,pr,"whole315PrimaryProjector");raw=block(h,sb,sr,"rawTargets")
 outside=block(h,sb,sr,"otherPrimaryRawTargets");outsideCoordinates=block(h,sb,sr,"trueU9OutsideTargetCoordinates")
 if PM*D!=D or J*U9!=U9*J9 or raw-PM*raw!=outside or U9*outsideCoordinates!=outside:raise ValueError("full raw targets and same root2 quotient")
 r=sr["secondImageRank"];T=kernel["sectionPolynomialsAscending"];F=kernel["generatorPolynomialsAscending"]
 labels=kernel["sourceLabelsForNextPage"];n=len(labels)
 if len(T)!=204 or any(len(row)!=r for row in T) or len(F)!=204 or any(len(row)!=n for row in F):raise ValueError("complete next-source polynomial dimensions")
 if n!=204+r or n>229 or n<204 or labels!=list(range(20001,20001+n)):raise ValueError("full actual next source count and labels")
 if max([len(p)-1 for row in F for p in row]+[-1])>5:raise ValueError("same proven next source degree bound")
 incomingSecond=h.source_action(J,D,T);incoming=h.join(U9,incomingSecond)
 if incoming.rank()!=9+r:raise ValueError("independent actual U9 and second-image lift basis")
 ia=h.solve_span(incoming,J*incoming)
 if ia["indices"]!=list(range(9+r)) or not all(ia["flags"]):raise ValueError("entire incoming space must be J invariant")
 Jin=ia["solution"]
 if incoming*Jin!=J*incoming:raise ValueError("actual incoming action identity")
 M=h.source_action(J,D,F)
 b8=h.sub(U9,range(315),[7]);d2=V10*h.sub(C197,range(10),[0]);first=h.join(h.join(U7,b8),d2)
 sol=h.solve_span(first,M)
 if sol["indices"]!=list(range(9)) or not all(sol["flags"]) or first*sol["solution"]!=M:
  save(a.out/"actual-third-kernel-first-correction-failure.json",{"status":"failed","residual":rows(sol["residual"])})
  raise ValueError("actual next kernel must be paid by true U7,b8,D3_K2")
 Ct=sol["solution"]
 F_t=[[t_integer_lift(p) for p in row] for row in F]
 if any(len(p)>6 for row in F_t for p in row):raise ValueError("integer s-to-t conversion degree")
 mats=[("U7",U7),("U9",U9),("J9",J9),("whole315PrimaryProjector",PM),
       ("rawTargets",raw),("root2ProjectedRawTargets",PM*raw),("otherPrimaryRawTargets",outside),
       ("trueU9OutsideTargetCoordinates",outsideCoordinates),("old204Projected315SecondColumns",D),
       ("incomingSecondBasis315",incomingSecond),("incomingSpace315",incoming),("incomingAction",Jin),
       ("nextKernelProjected315BeforeCorrection",M),("trueU7B8D2Basis315",first),("trueU7B8D2Correction",Ct)]
 for k in ("globalTwoPrimaryBasis","localTwoPrimaryBasis","localTwoPrimaryLeftInverse"):mats.append((k,block(h,pb,pr,k)))
 desc,system=h.save_system(a.out,"prepared-saturated-third.bin.gz",b"R150SP3A",[31,315,204,n,9],mats)
 spec(a.out/"third-q4-root2-ten.spec",labels,10,2);spec(a.out/"third-state-crt8.spec",labels,8,12)
 result={"format":"r150-saturated-third-source-preparation-v1","status":"completed","secondImageRank":r,
  "sourceLabels204":ALL204,"thirdSourceLabels":labels,"thirdSourceCount":n,
  "generatorPolynomialsInSAscending":F,"generatorIntegerTaylorCoefficientsMod31Six":F_t,
  "trueU7B8D2Correction":rows(Ct),"incomingSecondSectionPolynomials":T,
  "incomingDimension":9+r,"root2ThirdQuotientDimension":25-r,
  "completeSecondPolynomialSourceKernelRetained":True,"all204ActualSourceFamiliesRetained":True,
  "allNextSourceImagesPaidByTrueFirstBasis":True,"integerTaylorLiftIncludesAllCarry":True,
  "fullRawTargetsPreserved":True,"otherPrimaryTargetsPaidByTrueU9":True,
  "all315IncomingSourceIdentitiesVerified":True,"newThirdMathematicsComputed":False,
  "whole315ProjectorPolynomialAscending":pr["whole315ProjectorPolynomialAscending"],
  "localTwoPrimaryPivotRows":pr["localTwoPrimaryPivotRows"],
  "inputs":{k:bind_input(getattr(a,k)) for k in ("second_prepared_receipt","second_prepared_system","second_complete_receipt","second_complete_system","second_kernel")},
  "matrices":desc,"system":system,"elapsedSeconds":time.monotonic()-started}
 save(a.out/"prepared-saturated-third-receipt.json",result)
 print(json.dumps({k:result[k] for k in ("status","thirdSourceCount","completeSecondPolynomialSourceKernelRetained","allNextSourceImagesPaidByTrueFirstBasis","integerTaylorLiftIncludesAllCarry","elapsedSeconds")}),flush=True)
def complete(a,h,started):
 r=json.loads(a.prepared_receipt.read_text());b=h.actual(a.prepared_system,r["system"]["uncompressedSHA256"])
 if b[:8]!=b"R150SP3A" or r.get("status")!="completed" or not all(r.get(k) for k in ("completeSecondPolynomialSourceKernelRetained","allNextSourceImagesPaidByTrueFirstBasis","integerTaylorLiftIncludesAllCarry","fullRawTargetsPreserved")):raise ValueError("same exact third-source preparation")
 labels=r["thirdSourceLabels"];n=len(labels);rin=r["incomingDimension"]
 state,J=h.load_state(a.notes_root,a.out)
 product=json.loads(a.original_metadata.read_text());normal=json.loads(a.normal_metadata.read_text())
 if product.get("status")!="completed" or product.get("targetLabels")!=labels or product.get("divisorExponents")!=[5]*n or product.get("computedTaylorPrecision")!=10 or product.get("retainedFormalPrecision")!=5 or not all(product.get(k) for k in ("allOriginal17CoefficientsDivisible","originalRowScaleTransportVerified","allOriginalIntegerSourceJetsSaved","allDividedIntegerJetsSaved")):raise ValueError("all true third sources have original p5 identity and five effective jets")
 if normal.get("status")!="completed" or normal.get("targets")!=n or not all(normal.get(k) for k in ("fullLocalPrebasisSourceIdentity","fullLocalGQuotientIdentity","allRemaindersStandard")):raise ValueError("whole actual original third-source local quotient")
 mb=a.map.read_bytes();mr=json.loads(a.map_receipt.read_text())
 if sha(mb)!="3f291285db5a6e97a5db977b3402dbdcc9f7b9e5fb8a48d31b0e219e89e71716" or sha(a.map_receipt.read_bytes())!="5d3e09b26487355b32f20600764664def3dee0be34120e1c8202307eda5526df":raise ValueError("same full143 quotient map")
 M={k:h.block(mb,mr,k) for k in mr["matrices"]}
 q=a.standard_state.read_bytes()
 if q[:8]!=b"R150SE31" or struct.unpack_from("<4I",q,8)!=(31,820,n,8):raise ValueError("all true next-source standard-state dimensions")
 got=list(struct.unpack_from("<"+str(n)+"H",q,24));p=24+2*n
 coords=[list(struct.unpack_from("<HB",q,p+3*i)) for i in range(820)];p+=2460
 if got!=labels or coords!=mr["standardCoordinates"] or len(q)!=p+820*n:raise ValueError("same complete820 coordinate dictionary")
 E=nmod_mat(820,n,list(q[p:]),31);Y=M["Pi"]*E;free=M["freeChecks"]*Y;D39=M["torsionCoordinates"]*Y
 if not h.zero(free) or M["torsionEmbedding"]*D39!=Y:
  save(a.out/"actual-third-local-free-failure.json",{"status":"failed","nonzero":[[i,j,int(free[i,j])] for i in range(104) for j in range(n) if free[i,j]]})
  raise ValueError("all104 third-source local free conditions")
 B=block(h,b,r,"globalTwoPrimaryBasis");Li=block(h,b,r,"localTwoPrimaryLeftInverse")
 D=B*Li*h.sub(D39,r["localTwoPrimaryPivotRows"],range(n))
 if M["globalTorsionTo39"]*D!=D39:raise ValueError("whole315 reconstruction of actual third classes")
 incoming=block(h,b,r,"incomingSpace315");Jin=block(h,b,r,"incomingAction")
 U9=block(h,b,r,"U9");target=block(h,b,r,"rawTargets");PM=block(h,b,r,"whole315PrimaryProjector")
 outside=block(h,b,r,"otherPrimaryRawTargets");outsideCoordinates=block(h,b,r,"trueU9OutsideTargetCoordinates")
 if PM*D!=D or J*incoming!=incoming*Jin or target-PM*target!=outside or U9*outsideCoordinates!=outside:raise ValueError("same complete incoming quotient and full targets")
 project,Jq,pivots,qr,Ii,If=h.quotient(J,incoming)
 qdim=315-rin;C0=project(D);qt=project(target)
 if qt!=project(PM*target):raise ValueError("full target root2 equivalence in the true incoming quotient")
 C=C0;full=D;cur=C0;fcur=D;oldrank=-1;maximum=0
 for power in range(5):
  rank=C.rank();maximum=power
  print(json.dumps({"phase":"full-saturated-third-source-krylov","maximumPower":power,"rank":rank,"elapsedSeconds":time.monotonic()-started}),flush=True)
  if rank>r["root2ThirdQuotientDimension"]:raise ValueError("third image exceeds actual root2 quotient")
  if rank==oldrank:break
  if power<4:oldrank=rank;cur=Jq*cur;fcur=J*fcur;C=h.join(C,cur);full=h.join(full,fcur)
 if not h.zero(h.action(ROOT2_ANN,Jq,C0)):raise ValueError("actual t5 third-source annihilator")
 sol=h.solve_span(C,qt);basis=sol["basis"];rank=len(sol["indices"])
 JA=sol["inverse"]*h.sub(Jq*basis,sol["rows"],range(rank)) if rank else nmod_mat(0,0,31)
 if basis*JA!=Jq*basis:raise ValueError("complete third image is invariant")
 flags=sol["flags"];F=h.polynomial_solution(sol["indices"],sol["solution"],n)
 for j,ok in enumerate(flags):
  if not ok:
   for i in range(n):F[i][j]=[]
 combo=h.source_action(J,D,F);masked=nmod_mat(rows(target),31)
 for j,ok in enumerate(flags):
  if not ok:
   for i in range(315):masked[i,j]=0
 correction=Ii*h.sub(masked-combo,pivots,range(9))
 if incoming*correction!=masked-combo:raise ValueError("all locally positive full315 source identities")
 T=r["incomingSecondSectionPolynomials"]
 secondF=[[[] for _ in range(9)] for _ in range(204)]
 for i in range(204):
  for j in range(9):
   for k in range(rin-9):
    if T[i][k] and correction[9+k,j]:secondF[i][j]=add(secondF[i][j],T[i][k],int(correction[9+k,j]))
 duals=[]
 for j,ok in enumerate(flags):
  if ok:duals.append(None);continue
  k=next(i for i in range(qdim) if sol["residual"][i,j]);d=nmod_mat(1,qdim,31);d[0,k]=1
  if rank:
   arow=h.sub(basis,[k],range(rank))*sol["inverse"]
   for i,ri in enumerate(sol["rows"]):d[0,ri]-=arow[0,i]
  value=int((d*qt)[0,j]);d=pow(value,-1,31)*d
  if not h.zero(d*C) or (d*qt)[0,j]!=1:raise ValueError("entire third polynomial-image dual")
  fullrow=nmod_mat(1,315,31)
  for i,ri in enumerate(qr):fullrow[0,ri]=d[0,i]
  arow=d*If*Ii
  for i,ri in enumerate(pivots):fullrow[0,ri]-=arow[0,i]
  fullrow=h.row_action(r["whole315ProjectorPolynomialAscending"],J,fullrow)
  if not h.zero(fullrow*incoming) or not h.zero(fullrow*full) or (fullrow*target)[0,j]!=1:raise ValueError("complete full315 original-source obstruction dual")
  duals.append({"target":TARGETS[j],"full315Weights":[int(fullrow[0,i]) for i in range(315)],"targetValue":1,
   "annihilatesTrueU9AndCompleteSecondImage":True,"annihilatesCompleteThirdPolynomialImage":True,
   "scope":"complete root2 pages of the proved full original S2 envelope; necessary obstruction to original p2h0 modulo p6"})
 outcome=("complete-root2-third-obstruction" if not any(flags) else
          "third-page-all-local-compatible-global-continuation-required" if all(flags) else
          "third-page-partial-local-compatible-global-continuation-required")
 mats=[("allThirdLocal143",Y),("all104FreeChecks",free),("allThirdLocal39",D39),("allProjected315ThirdColumns",D),
       ("incomingSpace315",incoming),("incomingAction",Jin),("rawTargets",target),("otherPrimaryRawTargets",outside),
       ("trueU9OutsideTargetCoordinates",outsideCoordinates),("quotientAction",Jq),("completeThirdKrylov",C),
       ("full315ThirdKrylov",full),("imageBasis",basis),("imageAction",JA),("targetResidual",sol["residual"]),
       ("localPositiveThirdCombination",combo),("localPositiveIncomingCorrection",correction)]
 desc,system=h.save_system(a.out,"complete-saturated-third.bin.gz",b"R150SS3A",[31,315,9,n,rin],mats)
 result={"format":"r150-complete-saturated-third-page-v1","status":"completed","outcome":outcome,
  "targetLabels":TARGETS,"thirdSourceLabels":labels,"thirdSourceCount":n,"incomingDimension":rin,
  "allTrueOriginalThirdSourcesComputed":True,"allOriginal17DivisionsVerified":True,
  "allThirdIntegerSourcesAndFiveEffectiveJetsSaved":True,"all104LocalFreeChecksVerified":True,
  "completeRelevantSaturatedSecondImageReused":True,"completeRelevantSaturatedThirdImageComputed":True,
  "completeOriginalS2SourceCoverageRetained":True,"globalAllOriginalSourceMod31SixObstructionVerified":not any(flags),
  "globalAllOriginalSourceMod31SixDecisionComputed":not any(flags),"characteristicZeroIdentityAsserted":False,
  "thirdImageRank":rank,"KrylovMaximumPower":maximum,"root2ThirdQuotientDimension":r["root2ThirdQuotientDimension"],
  "individualTargetCompatible":flags,"compatibleTargetLabels":[x for x,ok in zip(TARGETS,flags) if ok],
  "originalMod31SixObstructedTargetLabels":[x for x,ok in zip(TARGETS,flags) if not ok],
  "solutionThirdSourcePolynomialsAscending":F,"solutionSecondSourcePolynomialsAscending":secondF,
  "trueU9CorrectionCoordinates":rows(h.sub(correction,range(9),range(9))),
  "allPositiveLocal315IdentitiesVerified":True,"fullRawTargetsPreserved":True,
  "otherPrimaryTargetsPaidByTrueU9":True,"allCompatibleTargetsOriginalIdentityVerified":False,
  "fullOriginalAllNineMod887503681IdentityVerified":False,"finitePositiveSourceBudgetsVerified":False,
  "completedOriginalTargetLabels":[],"actualFinalSourceCostsBySlot":[-1]*9,"finite_budget_verified":False,
  "thirdPageDuals":duals,"matrices":desc,"system":system,"elapsedSeconds":time.monotonic()-started}
 save(a.out/"complete-saturated-third-page-receipt.json",result)
 print(json.dumps({k:result[k] for k in ("status","allTrueOriginalThirdSourcesComputed","completeRelevantSaturatedThirdImageComputed","completeOriginalS2SourceCoverageRetained","thirdImageRank","individualTargetCompatible","outcome","elapsedSeconds")}),flush=True)
def main():
 p=argparse.ArgumentParser();p.add_argument("--mode",choices=("prepare","complete"),required=True)
 p.add_argument("--notes-root",type=Path,required=True);p.add_argument("--out",type=Path,required=True)
 for k in ("second-prepared-receipt","second-prepared-system","second-complete-receipt","second-complete-system","second-kernel",
           "prepared-receipt","prepared-system","original-metadata","normal-metadata","map","map-receipt","standard-state"):
  p.add_argument("--"+k,type=Path)
 a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True);started=time.monotonic();path=a.notes_root/HELPER
 if sha(path.read_bytes())!=HELPER_SHA:raise ValueError("same exact source arithmetic helper")
 h=load(path,"r150_saturated_third_exact_arithmetic")
 if a.mode=="prepare":prepare(a,h,started)
 else:complete(a,h,started)
if __name__=="__main__":main()
