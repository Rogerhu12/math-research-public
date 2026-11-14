#!/usr/bin/env python3
"""Actual primary check, then the complete integer-admissible eta8 second image."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
HELPER="2026-11-14-r150-ninth-first-matrices-789f.py"
HELPER_SHA="3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a"
FIXED={"first_receipt":"7af477b589130f60ef5f39a98e1bc7e8ccdf50e8ffb4964b1f2c5c84ea7d949f",
 "first_system":"2213c4ac1215cd7e34ce0427ba10f512a6f0a847b3e81f08d495c107596f2656",
 "action_receipt":"4b7795994a5281f82eb63d2ae640026239bb4de6a9d92c3036e4b2406a14bc84",
 "action_system":"cd10635dee8b3fda4f1b32d0818358cfb7421655a81792834d421194200636a6",
 "current_remainders":"51ec0f7bbb843e1a6cb10b37de0e3a55888095e10961620e4e8fb758fa9a7486"}
TARGETS=list(range(2,11));NEW=[9101];C_EXPECTED=[28,3,24,3,25,2,23,8,0]
def sha(b):return hashlib.sha256(b).hexdigest()
def import_helper(notes):
 path=notes/HELPER
 if sha(path.read_bytes())!=HELPER_SHA:raise ValueError("exact complete arithmetic helper")
 spec=importlib.util.spec_from_file_location("r150_eighth_admissible_arithmetic",path)
 h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h);return h
def primary(h,J):
 cp=J.charpoly();characteristic=[int(cp[i]) for i in range(cp.degree()+1)]
 rest=characteristic[:];f=[1];multiplicities={}
 for root in (1,2):
  exponent=0
  while len(rest)>1 and h.value(rest,root)==0:
   rest,r=h.divmodp(rest,[-root,1])
   if r:raise ValueError("exact complete characteristic primary division")
   f=h.mul(f,[-root,1]);exponent+=1
  multiplicities[str(root)]=exponent
 if len(characteristic)!=316 or multiplicities!={"1":7,"2":32}:raise ValueError("same315 characteristic and full1/2 primary multiplicities")
 P=h.mul(rest,h.inverse_mod(rest,f))
 if len(P)>315 or h.divmodp(h.add(h.mul(P,P),P,-1),characteristic)[1] or h.divmodp(h.add(P,[1],-1),f)[1] or h.divmodp(P,rest)[1]:raise ValueError("actual characteristic-polynomial primary projector")
 return characteristic,f,P,multiplicities
def minimum_on_columns(h,J,V,dimension):
 from flint import nmod_mat
 if h.zero(V):return [1],0
 cols=V;power=V;old=-1
 for d in range(dimension+1):
  solve=h.solve_span(cols,nmod_mat(J.nrows(),1,31));r=len(solve["indices"])
  if r==old or r==dimension:break
  old=r;power=J*power;cols=h.join(cols,power)
 else:raise ValueError("bounded invariant-span closure")
 B=solve["basis"];A=solve["inverse"]*h.sub(J*B,solve["rows"],range(r))
 if B*A!=J*B:raise ValueError("actual cyclic-span action")
 p=A.minpoly();result=[int(p[i]) for i in range(p.degree()+1)]
 if not h.zero(h.action(result,J,V)):raise ValueError("actual minimum-polynomial multiplyback")
 return result,r
def prepare(a,h,start):
 from flint import nmod_mat
 first=json.loads(h.actual(a.first_receipt,FIXED["first_receipt"]));fbytes=h.actual(a.first_system,FIXED["first_system"])
 saved=json.loads(h.actual(a.action_receipt,FIXED["action_receipt"]));sbytes=h.actual(a.action_system,FIXED["action_system"])
 if first.get("status")!="completed" or not first.get("fullF9FirstImageComplete") or first.get("newFirstImageRank")!=0 or first.get("individualTargetCompatible")!=[False]*9:raise ValueError("actual completed F9 full first image")
 if fbytes[:8]!=b"R150F931" or sbytes[:8]!=b"R150U931":raise ValueError("exact completed matrix formats")
 state,J=h.load_state(a.notes_root,a.out);U9=h.block(sbytes,saved,"U9");J9=h.block(sbytes,saved,"J9")
 if U9!=h.block(fbytes,first,"U9") or J9!=h.block(fbytes,first,"J9") or U9.rank()!=9 or J*U9!=U9*J9:raise ValueError("identical actual nine-dimensional augmented source")
 D=h.block(fbytes,first,"actualAll315NewColumns");V=h.block(fbytes,first,"actual820NewColumns")
 if sha(a.current_remainders.read_bytes())!=FIXED["current_remainders"]:raise ValueError("same original ten complete remainders")
 Dcheck,Vcheck,_=h.actual_ten_classes(a.current_remainders,state)
 if Dcheck!=D or Vcheck!=V:raise ValueError("same true505 free tests and315 current coordinates")
 raw=h.sub(D,range(315),range(1,10))
 C=h.block(sbytes,saved,"newSevenCoordinatesInU9")
 c=[int(C[i,2]) for i in range(9)]
 if c!=C_EXPECTED or c[8]!=0:raise ValueError("actual K4_7003 cancellation already in U8")
 characteristic,f12,P,multiplicities=primary(h,J)
 PU=h.action(P,J,U9);PR=h.action(P,J,raw)
 if PU!=U9 or h.action(P,J,PR)!=PR or not h.zero(h.action(f12,J,PR)):raise ValueError("actual full primary projector identities")
 project,Jq,rows,free,inverse,Uf=h.quotient(J,U9)
 if not h.zero(project(h.sub(D,range(315),[0]))):raise ValueError("ninth first relation really vanishes in whole quotient")
 support=[n==0 for n in h.counts(raw-PR)]
 minimum,raw_rank=minimum_on_columns(h,J,raw,315)
 quotient_minimum,quotient_rank=minimum_on_columns(h,Jq,project(raw),306)
 blocks,system=h.save_system(a.out,"prepared-eighth-second.bin.gz",b"R150E2P1",[31,315,9,9,1],
  [("U9",U9),("J9",J9),("rawTargets",raw),("projectedRawTargets",PR),
   ("eighthFirstCorrection",nmod_mat([[x] for x in c],31)),("quotientAction",Jq)])
 result={"format":"r150-actual-eighth-integer-admissible-second-preparation-v1","status":"completed",
  "sourceRun":43638830039,"oldNineRawAndSourcesRecomputed":False,"all505FreeObservationsVerified":True,
  "all315RawCoordinatesMatchedSavedProduct":True,"fullF9FirstImageZeroVerified":True,
  "actualEighthFirstCorrection":c,"ninthCorrectionExactlyZero":True,
  "individualRawSupportedAt1And2":support,"allNineRawSupportedAt1And2":all(support),
  "wholeRawMinimumAnnihilatorAscending":minimum,"wholeRawGeneratedModuleDimension":raw_rank,
  "rawQuotientMinimumAnnihilatorAscending":quotient_minimum,"rawQuotientGeneratedModuleDimension":quotient_rank,
  "rawColumnRank":raw.rank(),"rawQuotientColumnRank":project(raw).rank(),
  "integerSourceLattice":"c8 divisible31 and c9 divisible31^2",
  "admissibleFirstDigitKernel":"kerAbar plus eta1,...,eta8; eta9 not admitted",
  "onlyUnpaidRelatedSecondDirection":"eta8",
  "completeLowerInitialFreedomComputed":False,"old198ThirdImagesNotClaimedZero":True,
  "characteristicPolynomialAscending":characteristic,"completePrimaryMultiplicities":multiplicities,
  "primaryProjectorPolynomialAscending":P,"primaryProjectorDegree":len(P)-1,
  "relevantPrimaryDimension":39,"relevantQuotientDimension":30,
  "matrices":blocks,"system":system,"elapsedSeconds":time.monotonic()-start}
 (a.out/"prepared-eighth-second-receipt.json").write_text(json.dumps(result,separators=(",",":"))+"\n")
 print(json.dumps({k:result[k] for k in ("status","fullF9FirstImageZeroVerified","ninthCorrectionExactlyZero",
  "allNineRawSupportedAt1And2","rawQuotientColumnRank","elapsedSeconds")}),flush=True)
def one_class(path,state,h):
 from flint import nmod_mat
 data=path.read_bytes();wide=data[:8]==b"R150NX31"
 if (not wide and data[:8]!=b"R150NF31") or struct.unpack_from("<3I",data,8)!=(0,1,1034):raise ValueError("one actual complete eighth G remainder")
 index={tuple(c):i for i,c in enumerate(state["coordinates"])};V=nmod_mat(820,1,31);offset=20
 raw,label,count=struct.unpack_from("<IHI",data,offset);offset+=10
 if raw or label!=9101:raise ValueError("genuine eighth direction label")
 previous=0
 for _ in range(count):
  component=struct.unpack_from("<H",data,offset)[0];offset+=2
  size=2 if wide else 1;length=int.from_bytes(data[offset:offset+size],"little");offset+=size
  if component<=previous or component>1034 or length<1:raise ValueError("complete actual remainder dictionary")
  previous=component
  for degree in range(length):
   x=data[offset];offset+=1
   if x>30:raise ValueError("actual remainder field coefficient")
   if x:
    if (component,degree) not in index:raise ValueError("actual eighth residue contains a high free remainder")
    V[index[component,degree],0]=x
 if offset!=len(data):raise ValueError("actual one remainder tail")
 free=[i for i in range(820) if i+1 not in set(state["pivotStateCoordinates"])]
 D=h.sub(V,free,[0]);K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose();O=nmod_mat(state["observabilityEchelon"],31)
 if K*D!=V or not h.zero(O*V):raise ValueError("actual full505 free tests and315 reconstruction")
 return D,V,data
def complete(a,h,start):
 from flint import nmod_mat
 prep=json.loads(a.prepared_receipt.read_text());pbytes=h.actual(a.prepared_system,prep["system"]["uncompressedSHA256"])
 if prep.get("status")!="completed" or not prep.get("allNineRawSupportedAt1And2") or not prep.get("fullF9FirstImageZeroVerified") or not prep.get("ninthCorrectionExactlyZero") or pbytes[:8]!=b"R150E2P1":raise ValueError("actual admissible primary preparation")
 original=json.loads(a.original_metadata.read_text());image=json.loads(a.image_metadata.read_text())
 if original.get("status")!="completed" or original.get("modulus")!=887503681 or original.get("divisor")!=28629151 or original.get("targetCount")!=1 or original.get("targetMode")!=0 or original.get("targetLabels")!=NEW or not original.get("allOriginalProductCoefficientsDivisible") or not original.get("originalRowScaleTransportVerified"):raise ValueError("one true full original17 H5 divisibility")
 if image.get("status")!="completed" or image.get("targets")!=1 or not image.get("fullImageQuotientIdentity") or not image.get("everyRemainderIsIrreducible"):raise ValueError("one true full G identity")
 state,J=h.load_state(a.notes_root,a.out)
 U9=h.block(pbytes,prep,"U9");J9=h.block(pbytes,prep,"J9");raw=h.block(pbytes,prep,"rawTargets")
 if U9.rank()!=9 or J*U9!=U9*J9:raise ValueError("actual U9 module")
 characteristic,f12,P,multiplicities=primary(h,J)
 if P!=prep["primaryProjectorPolynomialAscending"] or h.action(P,J,raw)!=raw or h.action(P,J,U9)!=U9:raise ValueError("actual full315 primary support cannot be assumed")
 D,V,remainder_bytes=one_class(a.image_remainders,state,h);PD=h.action(P,J,D)
 project,Jq,rows,free,inverse,Uf=h.quotient(J,U9);qt=project(raw)
 current=project(PD);fullcurrent=PD;unprojectedcurrent=D
 columns=current;fullcolumns=fullcurrent;unprojectedcolumns=unprojectedcurrent
 oldrank=-1;stable=False
 for degree in range(32):
  indices=h.pivots(columns);rank=len(indices)
  if rank>30:raise ValueError("admissible related rank exceeds39minus9")
  print(json.dumps({"phase":"complete-eighth-admissible-second-krylov","maximumPower":degree,"rank":rank,
   "columns":columns.ncols(),"elapsedSeconds":time.monotonic()-start}),flush=True)
  if rank==oldrank or rank==30:stable=True;break
  oldrank=rank;current=Jq*current;fullcurrent=J*fullcurrent;unprojectedcurrent=J*unprojectedcurrent
  columns=h.join(columns,current);fullcolumns=h.join(fullcolumns,fullcurrent);unprojectedcolumns=h.join(unprojectedcolumns,unprojectedcurrent)
 if not stable:raise ValueError("complete30-dimensional admissible primary closure")
 solve=h.solve_span(columns,qt);rank=len(solve["indices"]);basis=solve["basis"]
 actionq=solve["inverse"]*h.sub(Jq*basis,solve["rows"],range(rank)) if rank else nmod_mat(0,0,31)
 if basis*actionq!=Jq*basis:raise ValueError("actual arbitrary-degree complete admissible related image")
 if rank:
  cp=actionq.minpoly();ann=[int(cp[i]) for i in range(cp.degree()+1)]
  if not h.zero(h.action(ann,Jq,project(PD))):raise ValueError("actual related cyclic annihilator")
 else:ann=[1]
 projected_solution=h.polynomial_solution(solve["indices"],solve["solution"],1)
 small=h.solve_span(project(unprojectedcolumns),qt);small_solution=h.polynomial_solution(small["indices"],small["solution"],1)
 flags=solve["flags"];used_projection=[False]*9;F=[[[] for _ in range(9)]]
 for j in range(9):
  if not flags[j]:continue
  if small["flags"][j]:F[0][j]=small_solution[0][j]
  else:F[0][j]=h.mul(P,projected_solution[0][j]);used_projection[j]=True
 combination=h.source_action(J,D,F);masked=h.sub(raw,range(315),range(9))
 for j in range(9):
  if not flags[j]:
   for i in range(315):masked[i,j]=0
 difference=masked-combination;C=inverse*h.sub(difference,rows,range(9))
 if U9*C!=difference:raise ValueError("positive target must hold in entire315 with actual U9 source correction")
 duals=[]
 for j in range(9):
  if flags[j]:duals.append(None);continue
  coordinate=next(i for i in range(306) if solve["residual"][i,j]);dual=nmod_mat(1,306,31);dual[0,coordinate]=1
  if rank:
   correction=h.sub(basis,[coordinate],range(rank))*solve["inverse"]
   for i,r in enumerate(solve["rows"]):dual[0,r]-=correction[0,i]
  val=int((dual*qt)[0,j]);dual=pow(val,-1,31)*dual
  if not h.zero(dual*columns) or (dual*qt)[0,j]!=1:raise ValueError("actual complete related quotient dual")
  lift=nmod_mat(1,315,31)
  for i,r in enumerate(free):lift[0,r]=dual[0,i]
  eliminate=dual*Uf*inverse
  for i,r in enumerate(rows):lift[0,r]-=eliminate[0,i]
  fulldual=h.row_action(P,J,lift)
  if not h.zero(fulldual*U9) or not h.zero(fulldual*unprojectedcolumns) or (fulldual*raw)[0,j]!=1:raise ValueError("true full315 projector-composed dual")
  duals.append({"target":TARGETS[j],"original315Coordinates":[int(fulldual[0,i]) for i in range(315)],
   "annihilatesU9":True,"annihilatesCompleteIntegerAdmissibleRelatedSecondImage":True,"targetValue":1,
   "scope":"current F9 initial source modulo31, with c8 divisible31 and c9 divisible31^2; lower initial sources remain unpaid"})
 maximum=max([len(p)-1 for row in F for p in row]+[-1])
 if maximum>343:raise ValueError("paid314 projector plus29 cyclic degree")
 blocks,system=h.save_system(a.out,"complete-eighth-second-image.bin.gz",b"R150E2G1",[31,315,9,306,1,columns.ncols(),rank,9],
  [("actualAll315NewSecondColumns",D),("actual820NewSecondColumns",V),("projectedAll315NewSecondColumns",PD),
   ("U9",U9),("J9",J9),("allNineRawTargets",raw),("quotientAction",Jq),("completeRelatedKrylov",columns),
   ("full315RelatedKrylov",fullcolumns),("full315UnprojectedKrylov",unprojectedcolumns),
   ("selectedImageBasis",basis),("selectedBasisAction",actionq),("relatedBasisSolution",solve["solution"]),
   ("relatedResidual",solve["residual"]),("full315ChosenSourceCombination",combination),("oldNineConstantCorrection",C)])
 result={"format":"r150-complete-integer-admissible-eighth-related-second-image-v1","status":"completed","prime":31,
  "targetLabels":TARGETS,"newGenuineSecondDirectionsComputed":1,"newDirectionLabel":9101,
  "actualH5OriginalMod31SixDivisibilityVerified":True,"all505FreeObservationsVerified":True,
  "all315CoordinatesRetained":True,"allNineRawSupportedAt1And2":True,
  "integerAdmissibleRelatedSecondImageComplete":True,"old198RelevantSecondCoverageUsed":True,
  "old4ExactAugmentedCoverageUsed":True,"old1632ExactSyzygyCoverageUsed":True,"oldFirstSevenRelatedSecondCoverageUsed":True,
  "ninthDirectionExcludedByOriginalIntegerLattice":True,"completeOtherPrimarySecondImageAsserted":False,
  "completeLowerInitialFreedomComputed":False,"whole315TorsionDimension":315,"quotientTorsionDimension":306,
  "relevantPrimaryDimension":39,"relevantQuotientDimension":30,"relatedSecondImageRank":rank,
  "newSecondDirectionAlreadyPrimary":D==PD,"KrylovMaximumPower":degree,"KrylovColumnCount":columns.ncols(),
  "KrylovBasisColumnIndicesZeroBased":solve["indices"],"relatedImageMinimumAnnihilatorAscending":ann,
  "individualTargetCompatible":flags,"compatibleTargetLabels":[j for j,f in zip(TARGETS,flags) if f],
  "obstructedTargetLabels":[j for j,f in zip(TARGETS,flags) if not f],"allNineCompatible":all(flags),"numberOfCompatibleTargets":sum(flags),
  "finiteUnprojectedCombinationCompatible":small["flags"],"unprojectedTrialMaximumPower":degree,
  "unprojectedTrialNotClaimedComplete":True,"primaryProjectorUsedForTarget":used_projection,
  "characteristicPolynomialAscending":characteristic,"completePrimaryMultiplicities":multiplicities,
  "primaryProjectorPolynomialAscending":P,"primaryProjectorDegree":len(P)-1,
  "newSecondSolutionPolynomialsAscending":F,"oldNineConstantCorrection":[[int(C[i,j]) for j in range(9)] for i in range(9)],
  "maximumSolutionDegree":maximum,"allCompatibleWhole315IdentitiesVerified":True,"completeRelatedDuals":duals,
  "negativeScope":"all F9 source corrections preserving the actual initial source modulo31 and the original p2-integer lattice; no claim for lower initial choices or unrestricted rational original sources",
  "positiveScope":"entire315 identity ready for original31squaredh0 modulo31^6 recovery; original17 identity still requires actual multiplyback",
  "finite_budget_verified":False,"fullOriginalMod31SixIdentityVerified":False,"characteristicZeroIdentityAsserted":False,
  "matrices":blocks,"system":system,"inputs":{"preparedReceiptSHA256":sha(a.prepared_receipt.read_bytes()),
   "originalMetadataSHA256":sha(a.original_metadata.read_bytes()),"imageMetadataSHA256":sha(a.image_metadata.read_bytes()),
   "imageRemaindersSHA256":sha(remainder_bytes),"stateSHA256":h.STATE_SHA},"elapsedSeconds":time.monotonic()-start}
 (a.out/"complete-eighth-second-image-receipt.json").write_text(json.dumps(result,separators=(",",":"))+"\n")
 print(json.dumps({k:result[k] for k in ("status","integerAdmissibleRelatedSecondImageComplete","relatedSecondImageRank",
  "individualTargetCompatible","allCompatibleWhole315IdentitiesVerified","maximumSolutionDegree","elapsedSeconds")}),flush=True)
def main():
 p=argparse.ArgumentParser();p.add_argument("--mode",choices=("prepare","complete"),required=True)
 for name in ("notes-root","out"):p.add_argument("--"+name,type=Path,required=True)
 for name in ("first-receipt","first-system","action-receipt","action-system","current-remainders",
              "prepared-receipt","prepared-system","image-remainders","image-metadata","original-metadata"):
  p.add_argument("--"+name,type=Path)
 a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic();h=import_helper(a.notes_root)
 if a.mode=="prepare":prepare(a,h,start)
 else:complete(a,h,start)
if __name__=="__main__":main()
