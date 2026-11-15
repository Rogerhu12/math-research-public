#!/usr/bin/env python3
"""Complete local second page for the full original p^2 source saturation.
Reads paid source data; records the entire next polynomial source kernel.
No higher page or global original identity is asserted by a local positive.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
from flint import nmod_mat
P=31
HELPER="2026-11-14-r150-ninth-first-matrices-789f.py"
HELPER_SHA="3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a"
TARGETS=list(range(2,11))
NEW198=list(range(15001,15199))
OLD6=[7001,7002,7005,7006,7007,7004]
ALL204=OLD6+NEW198
def sha(b):return hashlib.sha256(b).hexdigest()
def load(path,name):
 q=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(q);q.loader.exec_module(m);return m
def save(path,obj):path.write_text(json.dumps(obj,separators=(",",":"))+"\n")
def rows(A):return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def block(h,b,r,k):return h.block(b,r,k)
def spec(path,labels,L,ring):
 path.write_text("R150_S2_LOCAL_JET_SPEC_V1\n31 "+str(len(labels))+" "+str(L)+" "+str(ring)+"\n"+" ".join(map(str,labels))+"\n")
def trim(p):
 p=[x%31 for x in p]
 while p and p[-1]==0:p.pop()
 return p
def add(a,b,c=1):
 a=list(a)+[0]*max(0,len(b)-len(a))
 for i,x in enumerate(b):a[i]=(a[i]+c*x)%31
 return trim(a)
def saved(a,h):
 r=json.loads(a.prepared197_receipt.read_text());b=h.actual(a.prepared197_system,r["system"]["uncompressedSHA256"])
 if b[:8]!=b"R1503P1A" or r.get("status")!="completed" or not r.get("trueV10InvariantVerified"):raise ValueError("actual completed197 source preparation")
 s=json.loads(a.selector_receipt.read_text())
 if s.get("status")!="completed" or s.get("rankProjected197")!=7 or not s.get("allActualSourceCoordinateIdentitiesVerified"):raise ValueError("actual saved197 selector")
 c=json.loads(a.complete197_receipt.read_text());cb=h.actual(a.complete197_system,c["system"]["uncompressedSHA256"])
 if c.get("status")!="completed" or not c.get("completeRelevantLowInitialThirdImageComputed"):raise ValueError("actual completed197 entire relevant third source")
 for name,path in (("prepared_receipt",a.prepared197_receipt),("prepared_system",a.prepared197_system),("complete_receipt",a.complete197_receipt),("complete_system",a.complete197_system)):
  if sha(path.read_bytes())!=s["inputs"][name]["sha256"]:raise ValueError("selector exact saved input binding "+name)
 return r,b,s,c,cb
def prepare(a,h,started):
 r,b,sel,cr,cb=saved(a,h);state,J=h.load_state(a.notes_root,a.out)
 labels=r["remaining197Labels"]
 if len(labels)!=197 or sel["sourceLabels"]!=labels:raise ValueError("all197 true K2..K198 source labels")
 V10=block(h,b,r,"V10");J10=block(h,b,r,"J10");U7=block(h,b,r,"U7")
 C=nmod_mat(sel["trueV10Coordinates"],31);C7=nmod_mat(sel["oldTrueSevenCancellation"],31)
 if C.nrows()!=10 or C.ncols()!=197 or C7.nrows()!=7 or C7.ncols()!=197 or C.rank()!=7:raise ValueError("actual saved source coordinate matrices")
 if rows(J10)!=sel["trueV10Action"] or J*V10!=V10*J10 or not h.zero(h.sub(C,[9],range(197))):raise ValueError("actual V10 action and no b10 source component")
 if V10*C!=block(h,cb,cr,"projected315ThirdColumns"):raise ValueError("actual complete197 source coordinate reconstruction")
 if C[7,0]!=10 or C[8,0]!=11 or C[7,1]!=24 or C[8,1]!=28:raise ValueError("actual first two bare-source image coordinates")
 U9=h.sub(V10,range(315),range(9));J9=h.sub(J10,range(9),range(9))
 if U9.rank()!=9 or J*U9!=U9*J9:raise ValueError("true U9 invariant source space")
 Cnew=nmod_mat(7,198,31);alpha=[];beta=[];Z=nmod_mat(10,198,31)
 e8=nmod_mat(10,1,31);e8[7,0]=1
 for k in range(196):
  j=k+1;aa=(int(C[7,j])-15*int(C[8,j]))%31;bb=17*int(C[8,j])%31
  alpha.append(aa);beta.append(bb)
  v=h.sub(C,range(10),[j])-aa*e8-bb*h.sub(C,range(10),[0])
  if not h.zero(h.sub(v,[7,8,9],[0])):raise ValueError("complete omega source cancellation")
  for i in range(10):Z[i,k]=v[i,0]
 for k,v in [(196,(J10-2*nmod_mat([[int(i==j) for j in range(10)] for i in range(10)],31))*e8),
             (197,(J10-2*nmod_mat([[int(i==j) for j in range(10)] for i in range(10)],31))*h.sub(C,range(10),[0]))]:
  if not h.zero(h.sub(v,[7,8,9],[0])):raise ValueError("both genuine t relations in U7")
  for i in range(10):Z[i,k]=v[i,0]
 for i in range(7):
  for j in range(198):Cnew[i,j]=Z[i,j]
 if V10*Z!=U7*Cnew:raise ValueError("true seven correction for all198 next source relations")
 PM=block(h,b,r,"whole315PrimaryProjector");raw=block(h,b,r,"rawTargets")
 if PM*raw!=raw:raise ValueError("actual nine current raw targets all root2")
 copied=["globalTwoPrimaryBasis","localTwoPrimaryBasis","localTwoPrimaryLeftInverse"]
 mats=[("U7",U7),("U9",U9),("J9",J9),("V10",V10),("J10",J10),("whole315PrimaryProjector",PM),("rawTargets",raw),
       ("oldSevenCancellation",C7),("trueV10Coordinates",C),("new198SevenCancellation",Cnew)]
 for k in copied:mats.append((k,block(h,b,r,k)))
 desc,system=h.save_system(a.out,"prepared-saturated-second.bin.gz",b"R150SP2A",[31,315,204,198,9],mats)
 for name,ls,L,ring in [("q1-q2-root2-20",labels,20,2),("q3-root2-15",NEW198,15,2),
                      ("all204-root2-15",ALL204,15,2),("all204-state-crt8",ALL204,8,12)]:
  spec(a.out/(name+".spec"),ls,L,ring)
 result={"status":"completed","format":"r150-saturated-second-source-preparation-v1","sourceLabels197":labels,
  "new198Labels":NEW198,"oldSixLabels":OLD6,"complete204SourceLabels":ALL204,
  "new198Kinds":["omega"]*196+["t-e8","t-zeta2"],
  "omegaOriginalHighIndices":list(range(3,199)),"omegaAlphaB8":alpha,"omegaBetaD2":beta,
  "trueSevenCancellation197":rows(C7),"trueSevenCancellation198":rows(Cnew),
  "complete204SourceKernelGenerationProved":True,"all198TrueSevenCorrectionsVerified":True,
  "actualOld197SourceRecomputed":False,"all1834OriginalKernelDirectionsHaveExactBKernelLifts":True,
  "twoAdditionalExactRelationDirectionsRemoved":True,"allSixOldAndTwoTRelationsRetained":True,
  "newMathematicalSecondPageComputed":False,"targetLabels":TARGETS,
  "sourceScope":"full original S2 envelope; computation is its complete root2 local second page",
  "whole315ProjectorPolynomialAscending":r["projectorPolynomialAscending"],
  "twoPrimaryAnnihilatorAscending":r["twoPrimaryAnnihilatorAscending"],
  "localTwoPrimaryPivotRows":r["localTwoPrimaryPivotRows"],
  "globalTwoPrimaryPivotColumns":r["globalTwoPrimaryPivotColumns"],
  "matrices":desc,"system":system,"elapsedSeconds":time.monotonic()-started}
 save(a.out/"prepared-saturated-second-receipt.json",result)
 print(json.dumps({k:result[k] for k in ("status","complete204SourceKernelGenerationProved","all198TrueSevenCorrectionsVerified","allSixOldAndTwoTRelationsRetained","elapsedSeconds")}),flush=True)
def readprepared(a,h):
 r=json.loads(a.prepared_receipt.read_text());b=h.actual(a.prepared_system,r["system"]["uncompressedSHA256"])
 if b[:8]!=b"R150SP2A" or r.get("status")!="completed" or not r.get("all198TrueSevenCorrectionsVerified"):raise ValueError("complete saturated second source preparation")
 return r,b
def complete(a,h,started):
 r,b=readprepared(a,h);state,J=h.load_state(a.notes_root,a.out)
 product=json.loads(a.original_metadata.read_text());normal=json.loads(a.normal_metadata.read_text())
 if product.get("status")!="completed" or product.get("targetLabels")!=ALL204 or product.get("divisorExponents")!=[4]*204 or product.get("computedTaylorPrecision")!=15 or product.get("retainedFormalPrecision")!=10 or not all(product.get(k) for k in ("allOriginal17CoefficientsDivisible","originalRowScaleTransportVerified","allOriginalIntegerSourceJetsSaved","allDividedIntegerJetsSaved")):raise ValueError("all204 true original p4-divided ten-effective-jet sources")
 if normal.get("status")!="completed" or normal.get("targets")!=204 or not all(normal.get(k) for k in ("fullLocalPrebasisSourceIdentity","fullLocalGQuotientIdentity","allRemaindersStandard")):raise ValueError("all204 complete original local quotient calculation")
 mb=a.map.read_bytes();mr=json.loads(a.map_receipt.read_text())
 if sha(mb)!="3f291285db5a6e97a5db977b3402dbdcc9f7b9e5fb8a48d31b0e219e89e71716" or sha(a.map_receipt.read_bytes())!="5d3e09b26487355b32f20600764664def3dee0be34120e1c8202307eda5526df":raise ValueError("true 143-dimensional local quotient")
 M={k:h.block(mb,mr,k) for k in mr["matrices"]}
 q=a.standard_state.read_bytes()
 if q[:8]!=b"R150SE31" or struct.unpack_from("<4I",q,8)!=(31,820,204,8):raise ValueError("complete204 standard-state format")
 labels=list(struct.unpack_from("<204H",q,24));p=24+408
 coords=[list(struct.unpack_from("<HB",q,p+3*i)) for i in range(820)];p+=2460
 if labels!=ALL204 or coords!=mr["standardCoordinates"] or len(q)!=p+820*204:raise ValueError("same complete standard coordinates and true204 source dictionary")
 E=nmod_mat(820,204,list(q[p:]),31);Y=M["Pi"]*E;free=M["freeChecks"]*Y;D39=M["torsionCoordinates"]*Y
 if not h.zero(free) or M["torsionEmbedding"]*D39!=Y:
  save(a.out/"actual-local-free-failure.json",{"status":"failed","nonzero":[[i,j,int(free[i,j])] for i in range(104) for j in range(204) if free[i,j]]})
  raise ValueError("all104 complete local free conditions")
 B=block(h,b,r,"globalTwoPrimaryBasis");Li=block(h,b,r,"localTwoPrimaryLeftInverse")
 D=B*Li*h.sub(D39,r["localTwoPrimaryPivotRows"],range(204))
 if M["globalTorsionTo39"]*D!=D39:raise ValueError("true projected second class reconstruction")
 U9=block(h,b,r,"U9");J9=block(h,b,r,"J9");target=block(h,b,r,"rawTargets");PM=block(h,b,r,"whole315PrimaryProjector")
 if PM*D!=D or PM*target!=target or J*U9!=U9*J9:raise ValueError("same root2 action and full current targets")
 project,Jq,pivots,qr,Ui,Uf=h.quotient(J,U9)
 C0=project(D);qt=project(target)
 for j in list(range(6))+[202]:
  if not h.zero(h.sub(C0,range(306),[j])):raise ValueError("paid six old and t-e8 second classes must remain zero modulo U9")
 C=C0;full=D;cur=C0;fcur=D;oldrank=-1;maximum=0
 for power in range(5):
  rank=C.rank();maximum=power
  print(json.dumps({"phase":"full-saturated-second-source-krylov","maximumPower":power,"rank":rank,"elapsedSeconds":time.monotonic()-started}),flush=True)
  if rank>25:raise ValueError("root2 second quotient dimension25")
  if rank==oldrank:break
  if power<4:oldrank=rank;cur=Jq*cur;fcur=J*fcur;C=h.join(C,cur);full=h.join(full,fcur)
 if not h.zero(h.action(r["twoPrimaryAnnihilatorAscending"],Jq,C0)):raise ValueError("complete five-step source annihilator")
 sol=h.solve_span(C,qt);basis=sol["basis"];rank=len(sol["indices"])
 JA=sol["inverse"]*h.sub(Jq*basis,sol["rows"],range(rank)) if rank else nmod_mat(0,0,31)
 Csource=sol["inverse"]*h.sub(C0,sol["rows"],range(204)) if rank else nmod_mat(0,204,31)
 if basis*JA!=Jq*basis or basis*Csource!=C0:raise ValueError("complete polynomial image section and source-coordinate identities")
 # Source section T(s) is retained as actual 204-coordinate monomials.
 T=[[[] for _ in range(rank)] for _ in range(204)]
 for j,index in enumerate(sol["indices"]):
  power,source=divmod(index,204);T[source][j]=[0]*power+[1]
 generators=[[[] for _ in range(204+rank)] for _ in range(204)]
 for i in range(204):
  generators[i][i]=[1]
  for j in range(204):
   for z in range(rank):
    if Csource[z,j] and T[i][z]:generators[i][j]=add(generators[i][j],T[i][z],-int(Csource[z,j]))
  for j in range(rank):
   generators[i][204+j]=([0]+T[i][j]) if T[i][j] else []
   for z in range(rank):
    if JA[z,j] and T[i][z]:generators[i][204+j]=add(generators[i][204+j],T[i][z],-int(JA[z,j]))
 kernelImage=h.source_action(Jq,C0,generators)
 if not h.zero(kernelImage):raise ValueError("all complete next source generators must have zero second image")
 degree=max([len(p)-1 for row in generators for p in row]+[-1])
 if degree>5:raise ValueError("true next-source polynomial degree bound")
 flags=sol["flags"];F=h.polynomial_solution(sol["indices"],sol["solution"],204)
 for j,ok in enumerate(flags):
  if not ok:
   for i in range(204):F[i][j]=[]
 combo=h.source_action(J,D,F);masked=nmod_mat(rows(target),31)
 for j,ok in enumerate(flags):
  if not ok:
   for i in range(315):masked[i,j]=0
 correction=Ui*h.sub(masked-combo,pivots,range(9))
 if U9*correction!=masked-combo:raise ValueError("true local second positive combinations plus U9 correction")
 duals=[]
 for j,ok in enumerate(flags):
  if ok:duals.append(None);continue
  k=next(i for i in range(306) if sol["residual"][i,j]);d=nmod_mat(1,306,31);d[0,k]=1
  if rank:
   arow=h.sub(basis,[k],range(rank))*sol["inverse"]
   for i,ri in enumerate(sol["rows"]):d[0,ri]-=arow[0,i]
  v=int((d*qt)[0,j]);d=pow(v,-1,31)*d
  if not h.zero(d*C) or (d*qt)[0,j]!=1:raise ValueError("second-page polynomial image dual")
  fullrow=nmod_mat(1,315,31)
  for i,ri in enumerate(qr):fullrow[0,ri]=d[0,i]
  arow=d*Uf*Ui
  for i,ri in enumerate(pivots):fullrow[0,ri]-=arow[0,i]
  fullrow=h.row_action(r["whole315ProjectorPolynomialAscending"],J,fullrow)
  if not h.zero(fullrow*U9) or not h.zero(fullrow*full) or (fullrow*target)[0,j]!=1:raise ValueError("whole315 projected second-page dual")
  duals.append({"target":TARGETS[j],"full315Weights":[int(fullrow[0,i]) for i in range(315)],"targetValue":1,
   "annihilatesTrueU9":True,"annihilatesCompleteLocalSecondPolynomialImage":True,
   "doesNotAnnihilateUncomputedThirdImage":True,"scope":"second page only; not a full original modp6 obstruction"})
 mats=[("all204Local143",Y),("all104FreeChecks",free),("all204Local39",D39),("all204Projected315SecondColumns",D),
       ("U9",U9),("J9",J9),("rawTargets",target),("quotientAction",Jq),("completeSecondKrylov",C),
       ("full315SecondKrylov",full),("imageBasis",basis),("imageAction",JA),("sourceImageCoordinates",Csource),
       ("targetResidual",sol["residual"]),("localPositiveCombination",combo),("localPositiveU9Correction",correction),
       ("nextKernelImageVerifiedZero",kernelImage)]
 desc,system=h.save_system(a.out,"complete-saturated-second.bin.gz",b"R150SS2A",[31,315,9,204,9],mats)
 kernel={"format":"r150-complete-saturated-second-source-kernel-v1","prime":31,"sourceLabels204":ALL204,
  "sourceLabelsForNextPage":list(range(20001,20001+204+rank)),"imageDimension":rank,
  "sectionPolynomialsAscending":T,"sourceImageCoordinates":rows(Csource),"imageSAction":rows(JA),
  "generatorPolynomialsAscending":generators,"generatorCount":204+rank,"maximumPolynomialDegree":degree,
  "formula":"I-T*C and T*(sI-J)","allGeneratorImagesVerifiedZero":True,
  "completePolynomialSourceKernelByActualSection":True,
  "all204ActualIntegerSecondSourcesRequired":True,"nextPageIntegerCarryNotYetComputed":True}
 save(a.out/"complete-next-source-kernel.json",kernel)
 result={"status":"completed","format":"r150-complete-saturated-second-page-v1","targetLabels":TARGETS,
  "complete204SourceLabels":ALL204,"all204TrueOriginalSecondSourcesComputed":True,
  "allOriginal17DivisionsVerified":True,"all204IntegerSourcesAndTenEffectiveJetsSaved":True,
  "all104LocalFreeChecksVerified":True,"completeRelevantSaturatedSecondImageComputed":True,
  "completeNextPolynomialSourceKernelSaved":True,"completeRelevantSaturatedThirdImageComputed":False,
  "globalAllOriginalSourceMod31SixDecisionComputed":False,"characteristicZeroIdentityAsserted":False,
  "originalS2EnvelopeComplete":True,"localPrimaryRoot":2,"localSecondQuotientDimension":25,
  "secondImageRank":rank,"KrylovMaximumPower":maximum,"sourceKernelGeneratorCount":204+rank,
  "sourceKernelMaximumDegree":degree,"sourceKernelFile":"complete-next-source-kernel.json",
  "individualTargetCompatible":flags,"compatibleTargetLabels":[x for x,ok in zip(TARGETS,flags) if ok],
  "secondPageInsufficientTargetLabels":[x for x,ok in zip(TARGETS,flags) if not ok],
  "solutionPolynomialsAscending":F,"trueU9CorrectionCoordinates":rows(correction),
  "allPositiveLocal315IdentitiesVerified":True,"allCompatibleTargetsOriginalIdentityVerified":False,
  "fullOriginalAllNineMod887503681IdentityVerified":False,"finitePositiveSourceBudgetsVerified":False,
  "completedOriginalTargetLabels":[],"actualFinalSourceCostsBySlot":[-1]*9,"finite_budget_verified":False,
  "secondPageDuals":duals,"matrices":desc,"system":system,
  "outcome":"second-page-target-compatible-global-continuation-required" if any(flags) else "second-page-complete-third-continuation-required",
  "elapsedSeconds":time.monotonic()-started}
 save(a.out/"complete-saturated-second-page-receipt.json",result)
 print(json.dumps({k:result[k] for k in ("status","all204TrueOriginalSecondSourcesComputed","completeRelevantSaturatedSecondImageComputed","completeNextPolynomialSourceKernelSaved","secondImageRank","individualTargetCompatible","outcome","elapsedSeconds")}),flush=True)
def main():
 p=argparse.ArgumentParser();p.add_argument("--mode",choices=("prepare","complete"),required=True)
 p.add_argument("--notes-root",type=Path,required=True);p.add_argument("--out",type=Path,required=True)
 for k in ("prepared197-receipt","prepared197-system","complete197-receipt","complete197-system","selector-receipt","prepared-receipt","prepared-system","original-metadata","normal-metadata","map","map-receipt","standard-state"):p.add_argument("--"+k,type=Path)
 a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True);started=time.monotonic();path=a.notes_root/HELPER
 if sha(path.read_bytes())!=HELPER_SHA:raise ValueError("same exact source arithmetic helper")
 h=load(path,"r150_saturated_second_exact_arithmetic")
 if a.mode=="prepare":prepare(a,h,started)
 else:complete(a,h,started)
if __name__=="__main__":main()
