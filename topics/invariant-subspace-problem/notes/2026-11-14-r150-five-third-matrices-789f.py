#!/usr/bin/env python3
"""Five genuine lower-initial third directions; all positives reach the whole315 source identity."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
HELPER="2026-11-14-r150-ninth-first-matrices-789f.py"
HELPER_SHA="3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a"
FIXED={
 "eighth_prepared_receipt":"faf051ea66d4eea0460d3c26c45b6f50d41c9ef12d99c4bff94d1a42bcd9cc12",
 "eighth_prepared_system":"e1355a42f0c5d2a7609a0d7bfb686dbf663bedfd6d9e67f50ad6a26d010e0100",
 "eighth_complete_receipt":"0b06ac8b848d34a6007cee59b1fe6823ffe2de8bdbf8804b8fe0a9ff9fa619e9",
 "eighth_complete_system":"75983e0e5db7bc718957066c6736014dd35488cc64395c2378bfa63cd4ab64d6",
 "action_receipt":"4b7795994a5281f82eb63d2ae640026239bb4de6a9d92c3036e4b2406a14bc84",
 "action_system":"cd10635dee8b3fda4f1b32d0818358cfb7421655a81792834d421194200636a6",
 "current_remainders":"51ec0f7bbb843e1a6cb10b37de0e3a55888095e10961620e4e8fb758fa9a7486"}
TARGETS=list(range(2,11));NEW=[9301,9302,9305,9306,9307];SOURCE_COLUMNS=[0,1,4,5,6]
C_EXPECTED=[[25,3,30,17,29],[12,20,24,17,14],[2,7,20,21,0],[0,23,5,0,4],
 [0,27,25,25,5],[0,27,30,18,24],[0,24,4,27,3],[0,1,6,22,17],[0,0,29,21,2]]
def sha(b):return hashlib.sha256(b).hexdigest()
def import_helper(notes):
 path=notes/HELPER
 if sha(path.read_bytes())!=HELPER_SHA:raise ValueError("same complete arithmetic helper")
 spec=importlib.util.spec_from_file_location("r150_five_third_arithmetic",path)
 h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h);return h
def primary_two(h,J):
 cp=J.charpoly();characteristic=[int(cp[i]) for i in range(cp.degree()+1)]
 rest=characteristic[:];f=[1];exponent=0
 while len(rest)>1 and h.value(rest,2)==0:
  rest,r=h.divmodp(rest,[-2,1])
  if r:raise ValueError("exact whole characteristic2-primary division")
  f=h.mul(f,[-2,1]);exponent+=1
 if len(characteristic)!=316 or exponent!=32:raise ValueError("same complete315 module and32-dimensional2-primary")
 P=h.mul(rest,h.inverse_mod(rest,f))
 if len(P)>315 or h.divmodp(h.add(h.mul(P,P),P,-1),characteristic)[1] or h.divmodp(h.add(P,[1],-1),f)[1] or h.divmodp(P,rest)[1]:raise ValueError("complete characteristic-polynomial2-projector")
 return characteristic,f,P
def prepare(a,h,start):
 ep=json.loads(h.actual(a.eighth_prepared_receipt,FIXED["eighth_prepared_receipt"]))
 epb=h.actual(a.eighth_prepared_system,FIXED["eighth_prepared_system"])
 ec=json.loads(h.actual(a.eighth_complete_receipt,FIXED["eighth_complete_receipt"]))
 ecb=h.actual(a.eighth_complete_system,FIXED["eighth_complete_system"])
 saved=json.loads(h.actual(a.action_receipt,FIXED["action_receipt"]));sb=h.actual(a.action_system,FIXED["action_system"])
 if ep.get("status")!="completed" or not ep.get("fullF9FirstImageZeroVerified") or not ep.get("allNineRawSupportedAt1And2") or ep.get("rawQuotientMinimumAnnihilatorAscending")!=[29,1] or ep.get("rawQuotientGeneratedModuleDimension")!=4:raise ValueError("actual current raw and F9 first image")
 if ec.get("status")!="completed" or not ec.get("integerAdmissibleRelatedSecondImageComplete") or ec.get("relatedSecondImageRank")!=0 or not ec.get("newSecondDirectionAlreadyPrimary") or ec.get("individualTargetCompatible")!=[False]*9:raise ValueError("actual completed eighth second image")
 if epb[:8]!=b"R150E2P1" or ecb[:8]!=b"R150E2G1" or sb[:8]!=b"R150U931":raise ValueError("actual saved complete matrix formats")
 state,J=h.load_state(a.notes_root,a.out);U9=h.block(epb,ep,"U9");J9=h.block(epb,ep,"J9");raw=h.block(epb,ep,"rawTargets")
 if U9!=h.block(ecb,ec,"U9") or U9!=h.block(sb,saved,"U9") or J9!=h.block(ecb,ec,"J9") or J9!=h.block(sb,saved,"J9") or U9.rank()!=9 or J*U9!=U9*J9:raise ValueError("identical real U9 module")
 if raw!=h.block(ecb,ec,"allNineRawTargets"):raise ValueError("same actual whole315 targets")
 if sha(a.current_remainders.read_bytes())!=FIXED["current_remainders"]:raise ValueError("same original ten G remainders")
 Dold,Vold,_=h.actual_ten_classes(a.current_remainders,state)
 if h.sub(Dold,range(315),range(1,10))!=raw:raise ValueError("full505 observations and315 old raw match")
 project,Jq,rows,free,inverse,Uf=h.quotient(J,U9)
 eighth=h.block(ecb,ec,"actualAll315NewSecondColumns")
 eighthC=inverse*h.sub(eighth,rows,[0])
 if U9*eighthC!=eighth:raise ValueError("eighth second direction is in U9 in the whole315 space")
 Cfull=h.block(sb,saved,"newSevenCoordinatesInU9");C=h.sub(Cfull,range(9),SOURCE_COLUMNS)
 c=[[int(C[i,j]) for j in range(5)] for i in range(9)]
 if c!=C_EXPECTED:raise ValueError("actual selected five K4 cancellation coefficients")
 characteristic,f2,P=primary_two(h,J)
 PU=h.action(P,J,U9);PR=h.action(P,J,raw)
 if not h.zero(project(PU)) or PU.rank()!=7 or not h.zero(project(raw-PR)) or h.action(P,J,PR)!=PR or not h.zero(h.action(f2,J,PR)):raise ValueError("actual2-primary quotient and true U9 correction")
 rawC=inverse*h.sub(raw-PR,rows,range(9))
 if U9*rawC!=raw-PR or not h.zero(h.action([-2,1],Jq,project(raw))) or project(raw).rank()!=4:raise ValueError("same actual four-dimensional semisimple2 target quotient")
 blocks,system=h.save_system(a.out,"prepared-five-third.bin.gz",b"R150F3P1",[31,315,9,9,5],
  [("U9",U9),("J9",J9),("rawTargets",raw),("projectedRawTargets",PR),("rawProjectionU9Correction",rawC),
   ("fiveK4Correction",C),("eighthSecondU9Correction",eighthC),("quotientAction",Jq)])
 result={"format":"r150-actual-five-lower-initial-third-preparation-v1","status":"completed",
  "sourceCurrentRun":43638830039,"sourceEighthRun":43644262244,"oldNineRawAndSourcesRecomputed":False,
  "oldEighthDirectionRecomputed":False,"all505FreeObservationsVerified":True,"all315RawCoordinatesMatchedSavedProduct":True,
  "fullF9FirstImageZeroVerified":True,"eighthSecondImageZeroInEntireQmodU9Verified":True,
  "selectedK4SourceLabels":[7001,7002,7005,7006,7007],"newDirectionLabels":NEW,"actualFiveK4Correction":c,
  "allNineRawSupportedAt2ModuloU9":True,"rawProjectionDifferenceHasTrueU9Sources":True,
  "rawQuotientMinimumAnnihilatorAscending":[29,1],"rawQuotientDimension":4,"whole2PrimaryDimension":32,
  "U9TwoPrimaryDimension":7,"relevantQuotientDimension":25,
  "eighthSecondCoordinatesInU9":[int(eighthC[i,0]) for i in range(9)],
  "old198ThirdDirectionsComputed":False,"completeLowInitialThirdImageComputed":False,
  "characteristicPolynomialAscending":characteristic,"twoPrimaryFactorAscending":f2,
  "primaryProjectorPolynomialAscending":P,"primaryProjectorDegree":len(P)-1,
  "matrices":blocks,"system":system,"elapsedSeconds":time.monotonic()-start}
 (a.out/"prepared-five-third-receipt.json").write_text(json.dumps(result,separators=(",",":"))+"\n")
 print(json.dumps({k:result[k] for k in ("status","fullF9FirstImageZeroVerified",
  "eighthSecondImageZeroInEntireQmodU9Verified","allNineRawSupportedAt2ModuloU9","relevantQuotientDimension","elapsedSeconds")}),flush=True)
def five_classes(path,state,h):
 from flint import nmod_mat
 data=path.read_bytes();wide=data[:8]==b"R150NX31"
 if (not wide and data[:8]!=b"R150NF31") or struct.unpack_from("<3I",data,8)!=(0,5,1034):raise ValueError("five true complete G remainders")
 index={tuple(c):i for i,c in enumerate(state["coordinates"])};V=nmod_mat(820,5,31);offset=20
 for j in range(5):
  raw,label,count=struct.unpack_from("<IHI",data,offset);offset+=10
  if raw or label!=NEW[j]:raise ValueError("actual five third direction labels")
  previous=0
  for _ in range(count):
   component=struct.unpack_from("<H",data,offset)[0];offset+=2
   size=2 if wide else 1;length=int.from_bytes(data[offset:offset+size],"little");offset+=size
   if component<=previous or component>1034 or length<1:raise ValueError("complete G remainder dictionary")
   previous=component
   for degree in range(length):
    x=data[offset];offset+=1
    if x>30:raise ValueError("actual remainder field coefficient")
    if x:
     if (component,degree) not in index:raise ValueError("true new third direction contains a high free remainder")
     V[index[component,degree],j]=x
 if offset!=len(data):raise ValueError("actual five remainder tail")
 free=[i for i in range(820) if i+1 not in set(state["pivotStateCoordinates"])]
 D=h.sub(V,free,range(5));K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose();O=nmod_mat(state["observabilityEchelon"],31)
 if K*D!=V or not h.zero(O*V):raise ValueError("full505 free tests and315 reconstruction")
 return D,V,data
def complete(a,h,start):
 from flint import nmod_mat
 prep=json.loads(a.prepared_receipt.read_text());pb=h.actual(a.prepared_system,prep["system"]["uncompressedSHA256"])
 if prep.get("status")!="completed" or not prep.get("allNineRawSupportedAt2ModuloU9") or not prep.get("eighthSecondImageZeroInEntireQmodU9Verified") or pb[:8]!=b"R150F3P1":raise ValueError("actual five-source preparation")
 original=json.loads(a.original_metadata.read_text());image=json.loads(a.image_metadata.read_text())
 if original.get("status")!="completed" or original.get("modulus")!=887503681 or original.get("divisor")!=28629151 or original.get("targetCount")!=5 or original.get("targetMode")!=0 or original.get("targetLabels")!=NEW or not original.get("allOriginalProductCoefficientsDivisible") or not original.get("originalRowScaleTransportVerified"):raise ValueError("five true full original17 H5 divisibilities")
 if image.get("status")!="completed" or image.get("targets")!=5 or not image.get("fullImageQuotientIdentity") or not image.get("everyRemainderIsIrreducible"):raise ValueError("five true full G identities")
 state,J=h.load_state(a.notes_root,a.out)
 U9=h.block(pb,prep,"U9");J9=h.block(pb,prep,"J9");raw=h.block(pb,prep,"rawTargets")
 if U9.rank()!=9 or J*U9!=U9*J9:raise ValueError("actual U9 module")
 project,Jq,rows,free,inverse,Uf=h.quotient(J,U9)
 characteristic,f2,P=primary_two(h,J)
 if P!=prep["primaryProjectorPolynomialAscending"] or not h.zero(project(h.action(P,J,raw)-raw)) or not h.zero(project(h.action(P,J,U9))):raise ValueError("actual2-primary quotient support with U9 carry")
 D,V,remainder_bytes=five_classes(a.image_remainders,state,h);PD=h.action(P,J,D)
 qt=project(raw);current=project(PD);fullcurrent=PD;unprojectedcurrent=D
 columns=current;fullcolumns=fullcurrent;unprojectedcolumns=unprojectedcurrent
 oldrank=-1;stable=False
 for degree in range(27):
  indices=h.pivots(columns);rank=len(indices)
  if rank>25:raise ValueError("five-source2-primary quotient rank exceeds32minus7")
  print(json.dumps({"phase":"five-third-related-krylov","maximumPower":degree,"rank":rank,"columns":columns.ncols(),"elapsedSeconds":time.monotonic()-start}),flush=True)
  if rank==oldrank or rank==25:stable=True;break
  oldrank=rank;current=Jq*current;fullcurrent=J*fullcurrent;unprojectedcurrent=J*unprojectedcurrent
  columns=h.join(columns,current);fullcolumns=h.join(fullcolumns,fullcurrent);unprojectedcolumns=h.join(unprojectedcolumns,unprojectedcurrent)
 if not stable:raise ValueError("complete25-dimensional five-generator module closure")
 solve=h.solve_span(columns,qt);rank=len(solve["indices"]);basis=solve["basis"]
 actionq=solve["inverse"]*h.sub(Jq*basis,solve["rows"],range(rank)) if rank else nmod_mat(0,0,31)
 if basis*actionq!=Jq*basis:raise ValueError("whole polynomial module of the five new directions")
 if rank:
  cp=actionq.minpoly();ann=[int(cp[i]) for i in range(cp.degree()+1)]
  if not h.zero(h.action(ann,Jq,project(PD))):raise ValueError("actual five-source module annihilator")
 else:ann=[1]
 projected_solution=h.polynomial_solution(solve["indices"],solve["solution"],5)
 small=h.solve_span(project(unprojectedcolumns),qt);small_solution=h.polynomial_solution(small["indices"],small["solution"],5)
 flags=solve["flags"];used_projection=[False]*9;F=[[[] for _ in range(9)] for _ in range(5)]
 for j in range(9):
  if not flags[j]:continue
  for i in range(5):
   if small["flags"][j]:F[i][j]=small_solution[i][j]
   else:F[i][j]=h.mul(P,projected_solution[i][j]);used_projection[j]=True
 combination=h.source_action(J,D,F);masked=h.sub(raw,range(315),range(9))
 for j in range(9):
  if not flags[j]:
   for i in range(315):masked[i,j]=0
 difference=masked-combination;C=inverse*h.sub(difference,rows,range(9))
 if U9*C!=difference:raise ValueError("each positive target must hold in entire315 with true U9 source correction")
 duals=[]
 for j in range(9):
  if flags[j]:duals.append(None);continue
  coordinate=next(i for i in range(306) if solve["residual"][i,j]);dual=nmod_mat(1,306,31);dual[0,coordinate]=1
  if rank:
   correction=h.sub(basis,[coordinate],range(rank))*solve["inverse"]
   for i,r in enumerate(solve["rows"]):dual[0,r]-=correction[0,i]
  val=int((dual*qt)[0,j]);dual=pow(val,-1,31)*dual
  if not h.zero(dual*columns) or (dual*qt)[0,j]!=1:raise ValueError("exact five-direction quotient dual")
  lift=nmod_mat(1,315,31)
  for i,r in enumerate(free):lift[0,r]=dual[0,i]
  eliminate=dual*Uf*inverse
  for i,r in enumerate(rows):lift[0,r]-=eliminate[0,i]
  fulldual=h.row_action(P,J,lift)
  if not h.zero(fulldual*U9) or not h.zero(fulldual*unprojectedcolumns) or (fulldual*raw)[0,j]!=1:raise ValueError("whole315 projector-composed five-direction dual")
  duals.append({"target":TARGETS[j],"original315Coordinates":[int(fulldual[0,i]) for i in range(315)],
   "annihilatesU9":True,"annihilatesWholeFiveDirectionPolynomialModule":True,"targetValue":1,
   "old198ThirdDirectionsCovered":False,
   "scope":"only initial changes generated by phi1,phi2,phi5,phi6,phi7 and the already-paid higher digits; not the full lower-initial problem"})
 maximum=max([len(p)-1 for row in F for p in row]+[-1])
 if maximum>338:raise ValueError("paid314 projector plus24 source degree")
 blocks,system=h.save_system(a.out,"complete-five-third-image.bin.gz",b"R150F3G1",[31,315,9,306,5,columns.ncols(),rank,9],
  [("actualAll315NewThirdColumns",D),("actual820NewThirdColumns",V),("projectedAll315NewThirdColumns",PD),
   ("U9",U9),("J9",J9),("allNineRawTargets",raw),("quotientAction",Jq),("completeFiveRelatedKrylov",columns),
   ("full315RelatedKrylov",fullcolumns),("full315UnprojectedKrylov",unprojectedcolumns),
   ("selectedImageBasis",basis),("selectedBasisAction",actionq),("relatedBasisSolution",solve["solution"]),
   ("relatedResidual",solve["residual"]),("full315ChosenSourceCombination",combination),("oldNineConstantCorrection",C)])
 result={"format":"r150-five-genuine-lower-initial-third-directions-v1","status":"completed","prime":31,
  "targetLabels":TARGETS,"newGenuineThirdDirectionsComputed":5,"newDirectionLabels":NEW,
  "selectedK4SourceLabels":[7001,7002,7005,7006,7007],"actualFiveH5OriginalMod31SixDivisibilitiesVerified":True,
  "all505FreeObservationsVerified":True,"all315CoordinatesRetained":True,"allNineRawSupportedAt2ModuloU9":True,
  "fiveDirectionRelatedImageComplete":True,"old198ThirdDirectionsComputed":False,"completeLowInitialThirdImageComputed":False,
  "whole315TorsionDimension":315,"quotientTorsionDimension":306,"relevantPrimaryDimension":32,
  "U9TwoPrimaryDimension":7,"relevantQuotientDimension":25,"fiveRelatedImageRank":rank,
  "newDirectionsAlreadyTwoPrimary":D==PD,"KrylovMaximumPower":degree,"KrylovColumnCount":columns.ncols(),
  "KrylovBasisColumnIndicesZeroBased":solve["indices"],"fiveRelatedImageMinimumAnnihilatorAscending":ann,
  "individualTargetCompatible":flags,"compatibleTargetLabels":[j for j,f in zip(TARGETS,flags) if f],
  "obstructedByTheseFiveTargetLabels":[j for j,f in zip(TARGETS,flags) if not f],
  "allNineCompatible":all(flags),"numberOfCompatibleTargets":sum(flags),
  "finiteUnprojectedCombinationCompatible":small["flags"],"unprojectedTrialMaximumPower":degree,
  "unprojectedTrialNotClaimedComplete":True,"primaryProjectorUsedForTarget":used_projection,
  "characteristicPolynomialAscending":characteristic,"twoPrimaryFactorAscending":f2,
  "primaryProjectorPolynomialAscending":P,"primaryProjectorDegree":len(P)-1,
  "newThirdSolutionPolynomialsAscending":F,"oldNineConstantCorrection":[[int(C[i,j]) for j in range(9)] for i in range(9)],
  "maximumSolutionDegree":maximum,"allCompatibleWhole315IdentitiesVerified":True,"completeFiveDirectionDuals":duals,
  "negativeScope":"these five lower-initial directions are insufficient for each listed target; the old198 third directions remain unpaid and the full third image is not excluded",
  "positiveScope":"entire315 identity ready for original31squaredh0 modulo31^6 recovery; actual original17 multiplyback remains required",
  "finite_budget_verified":False,"fullOriginalMod31SixIdentityVerified":False,"characteristicZeroIdentityAsserted":False,
  "matrices":blocks,"system":system,"inputs":{"preparedReceiptSHA256":sha(a.prepared_receipt.read_bytes()),
   "originalMetadataSHA256":sha(a.original_metadata.read_bytes()),"imageMetadataSHA256":sha(a.image_metadata.read_bytes()),
   "imageRemaindersSHA256":sha(remainder_bytes),"stateSHA256":h.STATE_SHA},"elapsedSeconds":time.monotonic()-start}
 (a.out/"complete-five-third-image-receipt.json").write_text(json.dumps(result,separators=(",",":"))+"\n")
 print(json.dumps({k:result[k] for k in ("status","fiveDirectionRelatedImageComplete","fiveRelatedImageRank",
  "individualTargetCompatible","allCompatibleWhole315IdentitiesVerified","old198ThirdDirectionsComputed",
  "completeLowInitialThirdImageComputed","maximumSolutionDegree","elapsedSeconds")}),flush=True)
def main():
 p=argparse.ArgumentParser();p.add_argument("--mode",choices=("prepare","complete"),required=True)
 for name in ("notes-root","out"):p.add_argument("--"+name,type=Path,required=True)
 for name in ("eighth-prepared-receipt","eighth-prepared-system","eighth-complete-receipt","eighth-complete-system",
              "action-receipt","action-system","current-remainders","prepared-receipt","prepared-system",
              "image-remainders","image-metadata","original-metadata"):p.add_argument("--"+name,type=Path)
 a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic();h=import_helper(a.notes_root)
 if a.mode=="prepare":prepare(a,h,start)
 else:complete(a,h,start)
if __name__=="__main__":main()
