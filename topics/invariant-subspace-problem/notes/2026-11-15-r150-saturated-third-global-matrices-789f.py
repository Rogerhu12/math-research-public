#!/usr/bin/env python3
"""Whole315 reconciliation for the actual constant saturated-third positive source.
No local page is recomputed. Every displayed correction has real original sources.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
from flint import nmod_mat
P=31;P6=887503681;TARGETS=list(range(2,11))
HELPER="2026-11-14-r150-ninth-first-matrices-789f.py"
HELPER_SHA="3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a"
LAMBDA=[1,28,16,11,7,7,4,1,11]
PARENT=[344,409,327,102,1,16]
def sha(data):return hashlib.sha256(data).hexdigest()
def load(path,name):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def rows(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def save(path,data):path.write_text(json.dumps(data,separators=(",",":"))+"\n")
def get_system(h,receipt,path):
 r=json.loads(receipt.read_text());b=h.actual(path,r["system"]["uncompressedSHA256"])
 return r,b
def kernel_labels(path):
 with path.open("rb") as f:
  if f.read(8)!=b"R150KK31" or struct.unpack("<4I",f.read(16))!=(31,6188,200,85):raise ValueError("original complete200 kernel header")
  labels=[]
  for j in range(200):
   graph,head,cost,source,raw=struct.unpack("<IHHII",f.read(16))
   if cost!=(80 if j<160 else 81 if j<198 else 85) or not 1035<=head<=3229 or not 1<=source<=2195 or not 1<=raw<=6188:raise ValueError("same original kernel dictionary")
   labels.append(head)
 return labels
def nine_classes(path,state,h,labels):
 data=path.read_bytes();wide=data[:8]==b"R150NX31"
 if (not wide and data[:8]!=b"R150NF31") or struct.unpack_from("<3I",data,8)!=(0,9,1034):raise ValueError("nine complete irreducible G remainders")
 index={tuple(c):i for i,c in enumerate(state["coordinates"])};V=nmod_mat(820,9,31);off=20
 for j in range(9):
  raw,label,n=struct.unpack_from("<IHI",data,off);off+=10
  if raw or label!=labels[j]:raise ValueError("exact auxiliary original labels")
  previous=0
  for _ in range(n):
   c=struct.unpack_from("<H",data,off)[0];off+=2;sz=2 if wide else 1;l=int.from_bytes(data[off:off+sz],"little");off+=sz
   if not previous<c<=1034 or l<1:raise ValueError("irreducible coordinate dictionary")
   previous=c
   for d in range(l):
    x=data[off];off+=1
    if x>30:raise ValueError("field coefficient")
    if x:
     if (c,d) not in index:raise ValueError("actual polynomial source has high free remainder")
     V[index[c,d],j]=x
 if off!=len(data):raise ValueError("irreducible remainder tail")
 free=[i for i in range(820) if i+1 not in set(state["pivotStateCoordinates"])]
 D=h.sub(V,free,range(9));K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose();O=nmod_mat(state["observabilityEchelon"],31)
 if K*D!=V or not h.zero(O*V):raise ValueError("all505 free observations and complete315 reconstruction")
 return D,V
def exact_span(h,U,V,name):
 sol=h.solve_span(U,V)
 if sol["indices"]!=list(range(U.ncols())) or not all(sol["flags"]) or U*sol["solution"]!=V:raise ValueError(name)
 return sol["solution"]
def context(a,h):
 pr,pb=get_system(h,a.third_prepared_receipt,a.third_prepared_system)
 cr,cb=get_system(h,a.third_complete_receipt,a.third_complete_system)
 if pr.get("status")!="completed" or cr.get("status")!="completed" or cr.get("individualTargetCompatible")!=[True]*9:raise ValueError("actual completed all-positive third page required")
 for k in ("completeOriginalS2SourceCoverageRetained","completeRelevantSaturatedThirdImageComputed","allPositiveLocal315IdentitiesVerified","allOriginal17DivisionsVerified"):
  if cr.get(k) is not True:raise ValueError("actual local completed field "+k)
 U9=h.block(pb,pr,"U9");U7=h.block(pb,pr,"U7");PM=h.block(pb,pr,"whole315PrimaryProjector")
 raw=h.block(pb,pr,"rawTargets");W=h.block(pb,pr,"incomingSecondBasis315")
 if U9.ncols()!=9 or W.ncols()!=4 or h.join(U9,W).rank()!=13:raise ValueError("same complete incoming13")
 return pr,pb,cr,cb,U7,U9,PM,raw,W
def prepare(a,h,started):
 pr,pb,cr,cb,U7,U9,PM,raw,W=context(a,h)
 sr=json.loads(a.second_prepared_receipt.read_text());oldlabels=kernel_labels(a.old_kernel)
 if sr["sourceLabels197"][:7]!=oldlabels[1:8] or sr["omegaOriginalHighIndices"][:6]!=list(range(3,9)):raise ValueError("same seven original high sources")
 F=pr["generatorPolynomialsInSAscending"];f3=cr["solutionThirdSourcePolynomialsAscending"]
 if len(F)!=204 or len(f3)!=208 or pr["thirdSourceLabels"][10:12]!=[20011,20012]:raise ValueError("actual source208 dictionaries")
 parent=[]
 for i in range(204):
  if len(F[i][10])>1 or len(F[i][11])>1:raise ValueError("selected parents are truly constant")
  parent.append((F[i][10][0] if F[i][10] else 0)+16*(F[i][11][0] if F[i][11] else 0))
 if [i for i,x in enumerate(parent) if x]!=list(range(6,12)) or parent[6:12]!=PARENT:raise ValueError("actual unreduced integer parent vector")
 for i,row in enumerate(f3):
  for j,p in enumerate(row):
   expected=LAMBDA[j] if i==10 else (16*LAMBDA[j])%31 if i==11 else 0
   if len(p)>1 or (p[0] if p else 0)!=expected:raise ValueError("actual nine constant third solutions")
 D=h.block(cb,cr,"allProjected315ThirdColumns");F3=nmod_mat([[p[0] if p else 0 for p in r] for r in f3],31)
 f2=cr["solutionSecondSourcePolynomialsAscending"]
 if any(len(p)>1 for r in f2 for p in r) or any(any(p for p in f2[i]) for i in list(range(6))+list(range(10,204))):raise ValueError("four paid constant second corrections")
 C2=nmod_mat([[p[0] if p else 0 for p in r] for r in f2[6:10]],31);C9=nmod_mat(cr["trueU9CorrectionCoordinates"],31)
 if D*F3+W*C2+U9*C9!=raw:raise ValueError("full315 actual original nine local identities")
 # w[k][slot] gives six omega parent constants.  Sixth slot is zeta2.
 w=[[int(k==j) if j<4 else PARENT[k] if j==4 else 0 for j in range(9)] for k in range(6)]
 H=[[0]*9 for _ in range(7)];Kappa=[[0]*9 for _ in range(7)];K8=[0]*9
 C=sr["trueSevenCancellation197"];C198=sr["trueSevenCancellation198"]
 for j in range(9):
  for k in range(6):
   c=w[k][j];H[k+1][j]+=c;H[0][j]-=c*sr["omegaBetaD2"][k];K8[j]-=c*sr["omegaAlphaB8"][k]
  if j==5:H[0][j]+=1
  for i in range(7):
   ei=1 if i<2 else 2
   Kappa[i][j]=-(31**(2-ei))*sum(H[k][j]*C[i][k] for k in range(7))-(31**(3-ei))*sum(w[k][j]*C198[i][k] for k in range(6))
 projector=pr["whole315ProjectorPolynomialAscending"]
 if projector!=sr["whole315ProjectorPolynomialAscending"] or len(projector)!=197:raise ValueError("same exact196-degree full315 projector")
 result={"format":"r150-actual-third-six-slot-global-preparation-v1","status":"completed",
  "targetLabels":TARGETS,"oldKernelLabels":oldlabels,"selectedKernelOneBased":list(range(2,9)),
  "globalQ1Slots":list(range(2,9)),"auxiliaryRoles":["W2-15001","W2-15002","W2-15003","W2-15004","third-20011-plus16-20012","first-D2",None,None,None],
  "unreducedIntegerParentConstants":PARENT,"lambda":LAMBDA,"projectorPolynomialAscending":projector,
  "initialKernelCoefficients":H,"initialSevenOriginalCoefficients":Kappa,"initialKappa8OriginalCoefficients":K8,
  "allNineSaved315PositiveIdentitiesVerified":True,"allSelectedParentsActuallyConstant":True,
  "initialSourceCostBound":177,"q1SourceMode":"raw","finalSourceCostBound":1345,
  "sourceCosts":[177,373,469,665,761,957,1053,1249,1345],
  "whole315RawTargetsRetained":True,"characteristicZeroIdentityAsserted":False,"elapsedSeconds":time.monotonic()-started}
 save(a.out/"global-source-preparation.json",result);print(json.dumps(result),flush=True)
def reconcile(a,h,started):
 pr,pb,cr,cb,U7,U9,PM,raw,W=context(a,h);state,J=h.load_state(a.notes_root,a.out)
 om=json.loads(a.original_metadata.read_text());im=json.loads(a.image_metadata.read_text())
 div={"L3":29791,"L4":923521,"final":28629151}[a.mode];first={29791:9702,923521:9802,28629151:9902}[div];labels=list(range(first,first+9))
 if om.get("status")!="completed" or om.get("targetLabels")!=labels or om.get("divisor")!=div or om.get("modulus")!=P6 or not om.get("allOriginalProductCoefficientsDivisible"):raise ValueError("full original auxiliary division identity")
 if im.get("status")!="completed" or not im.get("fullImageQuotientIdentity") or not im.get("everyRemainderIsIrreducible"):raise ValueError("complete global G quotient identity")
 D,V=nine_classes(a.image_remainders,state,h,labels)
 if PM*D!=D:raise ValueError("actual whole-source P must retain only root2 torsion")
 mats=[("actualWhole315Columns",D),("actualWhole820Columns",V)]
 result={"format":"r150-actual-third-six-slot-whole315-v1","status":"completed","mode":a.mode,
  "all505FreeObservationsVerified":True,"all315OriginalSourceCoordinatesVerified":True,
  "allWhole315ReconciliationIdentitiesVerified":True,"originalDivisor":div,"originalLabels":labels,
  "originalSourceCost":om["actualSourceCosts"],"characteristicZeroIdentityAsserted":False}
 if a.mode=="L3":
  if any(D[i,j] for i in range(315) for j in range(6,9)):raise ValueError("inactive original L3 slots")
  desired=nmod_mat(rows(D),31)
  for i in range(315):desired[i,5]=0
  C7=exact_span(h,U7,desired,"five projected p3 parents must have full315 class in U7")
  HD=h.sub(D,range(315),[5]);oldD2=h.sub(h.block(pb,pr,"trueU7B8D2Basis315"),range(315),[8])
  HDdiff=exact_span(h,U7,HD-oldD2,"true global D2 differs only by U7")
  firstBasis=h.join(U7,h.sub(U9,range(315),[7]),HD)
  if firstBasis.rank()!=9 or h.join(U9,HD).rank()!=9:raise ValueError("true first basis U7,b8,globalD2")
  result.update(actualSevenCorrections=rows(C7),globalD2DifferenceInU7=rows(HDdiff),
   trueGlobalD2OriginalDivisor=29791,trueGlobalD2Saved=True)
  mats += [("actualSevenCorrections",C7),("globalD2",HD),("trueGlobalFirstBasis",firstBasis)]
 elif a.mode=="L4":
  dr,db=get_system(h,a.d_receipt,a.d_system);HD=h.block(db,dr,"globalD2")
  if dr.get("mode")!="L3" or not dr.get("trueGlobalD2Saved"):raise ValueError("actual p3 D2 source required")
  if any(D[i,j] for i in range(315) for j in range(5,9)):raise ValueError("inactive original L4 slots")
  HW=h.sub(D,range(315),range(4));diff=exact_span(h,U9,HW-W,"four whole global p4 classes must give same complete W2 modulo U9")
  incoming=h.join(U9,HW)
  if incoming.rank()!=13:raise ValueError("four actual independent global second sources")
  desired=nmod_mat(315,9,31)
  for i in range(315):desired[i,4]=D[i,4]
  firstBasis=h.join(U7,h.sub(U9,range(315),[7]),HD)
  C=exact_span(h,firstBasis,desired,"selected third parent needs true U7,b8,D2 correction")
  result.update(actualFirstCorrections=rows(C),globalW2DifferenceInU9=rows(diff),
   allFourGlobalW2OriginalSourcesVerified=True,allFourGlobalW2Divisors=923521,
   firstCorrectionUsesOnlyExponent3D2=True,unscaledKappa9UsedAtP4=False)
  mats += [("globalW2",HW),("globalW2DifferenceInU9",diff),("actualFirstCorrections",C),("globalIncoming13",incoming)]
 else:
  wr,wb=get_system(h,a.w_receipt,a.w_system);HW=h.block(wb,wr,"globalW2")
  if wr.get("mode")!="L4" or not wr.get("allFourGlobalW2OriginalSourcesVerified"):raise ValueError("four real global W2 sources required")
  if any(D[i,j] for i in range(315) for j in range(9) if j!=4):raise ValueError("only selected main p5 source is active")
  main=h.sub(D,range(315),[4]);wanted=raw-main*nmod_mat([LAMBDA],31)
  incoming=h.join(U9,HW);C=exact_span(h,incoming,wanted,"all nine full315 raw targets require actual U9+globalW2 correction")
  result.update(actualNineCorrections=rows(h.sub(C,range(9),range(9))),
   actualFourW2Corrections=rows(h.sub(C,range(9,13),range(9))),
   full315FinalReconciliationVerified=True,allNineRawTargetsVerified=True,lambdaValues=LAMBDA,
   allAuxiliarySourcePreimagesActuallyPresent=True)
  mats += [("full315RawTargets",raw),("mainGlobalP5Class",main),("whole315TargetDifference",wanted),("actualFinalIncoming13",incoming),("actualFinalCorrections",C)]
 blocks,system=h.save_system(a.out,"global-reconciliation.bin.gz",b"R150G3PA",[31,315,9],mats)
 result.update(matrices=blocks,system=system,elapsedSeconds=time.monotonic()-started)
 save(a.out/"global-reconciliation.json",result)
 print(json.dumps({k:v for k,v in result.items() if k not in ("matrices","system")}),flush=True)
def main():
 p=argparse.ArgumentParser();p.add_argument("--mode",choices=["prepare","L3","L4","final"],required=True)
 for k in ("notes-root","second-prepared-receipt","third-prepared-receipt","third-prepared-system","third-complete-receipt","third-complete-system","old-kernel","original-metadata","image-metadata","image-remainders","d-receipt","d-system","w-receipt","w-system","out"):p.add_argument("--"+k,type=Path)
 a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True);path=a.notes_root/HELPER
 if sha(path.read_bytes())!=HELPER_SHA:raise ValueError("exact original matrix/state helper")
 h=load(path,"saturated_third_global_actual_helper");start=time.monotonic()
 if a.mode=="prepare":prepare(a,h,start)
 else:reconcile(a,h,start)
if __name__=="__main__":main()
