#!/usr/bin/env python3
"""Read only saved complete seven-second data; derive exact U9/J9 and original-source valuations."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
HELPER="2026-11-14-r150-augmented-seven-second-matrices-789f.py"
HELPER_SHA="5e77a941ddd9fd624b838071006f6e1105842ffabf28276ce0254107ee89a7d7"
FIXED={
 "receipt":"39f51dce5abdc58051e3cdfdf6620b0ec0bbb4dcc1c47087291a75a0b3e043c6",
 "system":"6c5479690979af66251447f8567301e8e65263629e137fb680161a9809991ed8",
 "prepared_receipt":"ad4040900b4f7947f81fcdb291e0cf65eef962841b4ce50323907604b7212a14",
 "prepared_system":"76a441cbdb4aa37f94224555e88f4dfae0bc2b4873185c246e173a7f7707f5ec",
 "k4_source":"a5e16cfe2f6c6665c0806c488ea0ba3db11516e81be259c1f213126d9339566a",
 "current_seven_source":"05740d8f8556491a19a3af15ea495ef782b1736f647b6ae5fdc5e83402174d6d",
 "current_pair_source":"81783ab62815a8b4355bc2b91eea2a34a92f7913b8b7fce9987d6cc2a47825e1"}
def sha(b):return hashlib.sha256(b).hexdigest()
def degree(mult):
 d=0
 while mult:d+=mult%8;mult//=8
 return d
def original_source(path,expected,labels):
 data=path.read_bytes()
 if sha(data)!=expected or data[:8]!=b"R150P531":raise ValueError("same actual primitive modulo31five source")
 prime,modulus,rows,nt,bound=struct.unpack_from("<5I",data,8)
 if (prime,modulus,rows,nt)!=(31,28629151,6188,len(labels)):raise ValueError("same actual full original source header")
 offset=28
 actual=list(struct.unpack_from("<"+"H"*nt,data,offset));offset+=2*nt
 if actual!=labels:raise ValueError("same actual original target labels")
 minimum=[5]*nt;costs=[-1]*nt;nonzero=[0]*nt
 for r in range(1,6189):
  raw,e,mult,delta=struct.unpack_from("<IBQH",data,offset);offset+=15
  if raw!=r or e!=(r-1)%17 or delta!=10*(degree(mult)+1)+(0 if e<11 else 5):raise ValueError("full original row dictionary")
  for j in range(nt):
   length=struct.unpack_from("<H",data,offset)[0];offset+=2
   if length>bound-delta+1:raise ValueError("paid original source coefficient degree")
   coefficients=struct.unpack_from("<"+"I"*length,data,offset);offset+=4*length
   if length and not coefficients[-1]:raise ValueError("canonical actual source polynomial")
   for d,a in enumerate(coefficients):
    if a>=modulus:raise ValueError("canonical actual source coefficient")
    if a:
     nonzero[j]+=1;costs[j]=max(costs[j],d+delta)
     v=0
     while a%31==0:v+=1;a//=31
     minimum[j]=min(minimum[j],v)
 if offset!=len(data):raise ValueError("actual full source tail")
 return {"labels":labels,"modulus":modulus,"recordedBound":bound,"actualSourceCosts":costs,
         "minimum31Valuations":minimum,"nonzeroCoefficients":nonzero,"all6188RowsRead":True,
         "inputSHA256":expected,"inputBytes":len(data)}
def main():
 p=argparse.ArgumentParser()
 for key in ("notes-root","receipt","system","prepared-receipt","prepared-system","k4-source","current-seven-source","current-pair-source","out"):
  p.add_argument("--"+key,type=Path,required=True)
 a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
 helper=a.notes_root/HELPER
 if sha(helper.read_bytes())!=HELPER_SHA:raise ValueError("same complete arithmetic reader")
 spec=importlib.util.spec_from_file_location("r150_saved_second_helper",helper);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
 from flint import nmod_mat
 result=json.loads(h.actual(a.receipt,FIXED["receipt"]));data=h.actual(a.system,FIXED["system"])
 prepared=json.loads(h.actual(a.prepared_receipt,FIXED["prepared_receipt"]));pbytes=h.actual(a.prepared_system,FIXED["prepared_system"])
 if result.get("status")!="completed" or not result.get("allSevenCompatible") or result.get("KrylovBasisColumnIndicesZeroBased")!=[3] or result.get("maximumSolutionDegree")!=0:raise ValueError("actual complete seven-second result")
 if data[:8]!=b"R150A2G1" or struct.unpack_from("<8I",data,8)!=(31,315,8,307,7,14,1,7):raise ValueError("actual complete new seven system")
 state,J=h.load_state(a.notes_root,a.out)
 U8=h.block(data,result,"U8");J8=h.block(data,result,"J8")
 D=h.block(data,result,"actualAll315NewSecondColumns");PD=h.block(data,result,"projectedAll315NewSecondColumns")
 raw=h.block(data,result,"allNineRawTargets");oldD=h.block(pbytes,prepared,"oldAll315Columns")
 if D!=PD or J*U8!=U8*J8:raise ValueError("actual full new directions already primary")
 v9=h.sub(D,range(315),[3]);U9=h.join(U8,v9)
 rows=h.pivots(U9.transpose())
 if len(rows)!=9:raise ValueError("true ninth independent source")
 inverse=h.sub(U9,rows,range(9)).inv()
 J9=inverse*h.sub(J*U9,rows,range(9));C=inverse*h.sub(D,rows,range(7));R=inverse*h.sub(raw,rows,range(9))
 if U9*J9!=J*U9 or U9*C!=D or U9*R!=raw:raise ValueError("complete315 ninth action and all actual source identities")
 if [int(J9[8,j]) for j in range(9)]!=[0]*8+[2] or int(C[8,3])!=1:raise ValueError("actual ninth quotient action and normalization")
 rows8=h.pivots(U8.transpose());inv8=h.sub(U8,rows8,range(8)).inv()
 old7=h.sub(oldD,range(315),range(7));old7C=inv8*h.sub(old7,rows8,range(7))
 if U8*old7C!=old7:raise ValueError("old first seven relation images paid in U8")
 if [prepared["oldSevenConstantCorrection"][i][2] for i in range(7)]!=[int(J8[i,7]) for i in range(7)]:raise ValueError("same actual eighth relation source K4_7003")
 minimum=J9.minpoly();minimum=[int(minimum[i]) for i in range(minimum.degree()+1)]
 characteristic=J9.charpoly();characteristic=[int(characteristic[i]) for i in range(characteristic.degree()+1)]
 expected=[1]
 for root,times in ((1,2),(2,7)):
  for _ in range(times):expected=h.mul(expected,[-root,1])
 if minimum!=[27,8,26,1] or characteristic!=expected:raise ValueError("actual nine-dimensional primary action")
 coeff=[int(C[8,j]) for j in range(7)]
 third_kernel=[[[] for _ in range(7)] for _ in range(7)]
 for j in range(7):
  if j==3:third_kernel[3][j]=[-2,1]
  else:
   third_kernel[j][j]=[1]
   if coeff[j]:third_kernel[3][j]=[-coeff[j]]
 one_relation=[[[-int(J9[i,8])]] if J9[i,8] else [[]] for i in range(8)]+[[[-2,1]]]
 checks={"K4":original_source(a.k4_source,FIXED["k4_source"],list(range(7001,7008))),
         "currentSeven":original_source(a.current_seven_source,FIXED["current_seven_source"],[2,3,4,5,7,8,10]),
         "currentPair":original_source(a.current_pair_source,FIXED["current_pair_source"],[6,9])}
 if checks["K4"]["actualSourceCosts"]!=[86,87,88,87,87,88,87] or checks["currentSeven"]["actualSourceCosts"]!=[87]*7 or checks["currentPair"]["actualSourceCosts"]!=[87,87]:raise ValueError("actual original source costs must match completed products")
 blocks,system=h.save_system(a.out,"ninth-source-action.bin.gz",b"R150U931",[31,315,9,7,9],
  [("U9",U9),("J9",J9),("newSevenCoordinatesInU9",C),("oldNineRawCoordinatesInU9",R),("oldFirstSevenCoordinatesInU8",old7C)])
 answer={"format":"r150-actual-ninth-source-action-and-next-kernel-v1","status":"completed",
  "sourceRun":43634830833,"allDataFromCompletedSources":True,"ninthRelationLabel":7004,
  "ninthOriginalDivisor":923521,"ninthOriginalSourceCost":87,"U9Dimension":9,
  "J9":[[int(J9[i,j]) for j in range(9)] for i in range(9)],
  "ninthRelationOldEightCorrection":[int(J9[i,8]) for i in range(8)],
  "ninthQuotientEigenvalue":2,"newSevenCoordinatesInU9":[[int(C[i,j]) for j in range(7)] for i in range(9)],
  "newSecondImageCoefficientVector":coeff,"sevenThirdKernelPolynomialsAscending":third_kernel,
  "singleNinthFirstRelationPolynomialsAscending":one_relation,
  "U9MinimumAnnihilatorAscending":minimum,"U9CharacteristicPolynomialAscending":characteristic,
  "oldNineRawCoordinatesInU9":[[int(R[i,j]) for j in range(9)] for i in range(9)],
  "oldNineRawRank":R.rank(),"oldFirstSevenImagesInU8Verified":True,
  "eighthFirstImageIsExistingK4Column7003":True,"eighthFirstImageZeroInQmodU9":True,
  "fullF9FirstImageRequiresOnlyNinthRelation":True,
  "completeF9HigherInitialFreedomNotComputed":True,"old198ThirdImagesNotClaimedZero":True,
  "originalA87CharacteristicZeroRankLowerBound":226091,"exactFourthSmithValuationClaimed":False,
  "originalSourceValuationScans":checks,"matrices":blocks,"system":system,
  "elapsedSeconds":time.monotonic()-start}
 (a.out/"ninth-source-action-receipt.json").write_text(json.dumps(answer,separators=(",",":"))+"\n")
 print(json.dumps({k:answer[k] for k in ("status","U9Dimension","fullF9FirstImageRequiresOnlyNinthRelation","elapsedSeconds")}),flush=True)
if __name__=="__main__":main()
