#!/usr/bin/env python3
"""Seven genuine augmented second directions: whole315 arithmetic and complete1/2 primary image."""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
from flint import nmod_mat
P=31
READER_SHA="8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2"
STATE_SHA="06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"
SEVEN_RECEIPT_SHA="7e461b35ac41e0bb0c76462c8c61c4a8ebf9d55ff3ea8fdd0560146ed8809420"
SEVEN_SYSTEM_SHA="8ad7a408081b1ae32a87c8c653212f74e9bec6b4ef25263e7d3b3b6d4234b647"
PAIR_RECEIPT_SHA="82b377e242dadc2a55a515c6f5acf77f58cc49cd6acf2c69873ae52c0157734d"
PAIR_SYSTEM_SHA="d4e3bd9805f45fc6c2135bbdfdc483a89babd3a5b3a0d98f66e7d3d0be79e095"
LABEL7=list(range(7001,7008))
TARGETS=[2,3,4,5,7,8,10]
def sha(b):return hashlib.sha256(b).hexdigest()
def actual(path,expected):
 data=path.read_bytes()
 if path.suffix==".gz":data=gzip.decompress(data)
 if sha(data)!=expected:raise ValueError("exact saved data "+str(path))
 return data
def sub(M,rows,cols):
 rows,cols=list(rows),list(cols);A=nmod_mat(len(rows),len(cols),31)
 for i,r in enumerate(rows):
  for j,c in enumerate(cols):A[i,j]=M[r,c]
 return A
def join(*matrices):
 return nmod_mat([[int(M[i,j]) for M in matrices for j in range(M.ncols())] for i in range(matrices[0].nrows())],31)
def serial(M):return bytes(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))
def pivots(M):
 R,r=M.rref()
 return [next(j for j in range(M.ncols()) if R[i,j]) for i in range(r)]
def zero(M):return M==nmod_mat(M.nrows(),M.ncols(),31)
def counts(M):return [sum(bool(M[i,j]) for i in range(M.nrows())) for j in range(M.ncols())]
def trim(p):
 p=[int(x)%31 for x in p]
 while p and not p[-1]:p.pop()
 return p
def add(a,b,c=1):
 out=[0]*max(len(a),len(b))
 for i,x in enumerate(a):out[i]+=x
 for i,x in enumerate(b):out[i]+=c*x
 return trim(out)
def mul(a,b):
 if not a or not b:return []
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%31
 return trim(out)
def divmodp(a,b):
 a=trim(a);b=trim(b)
 if not b:raise ValueError("polynomial division byzero")
 q=[0]*max(0,len(a)-len(b)+1);inv=pow(b[-1],-1,31)
 while len(a)>=len(b):
  d=len(a)-len(b);c=a[-1]*inv%31;q[d]=c
  for j,x in enumerate(b):a[d+j]=(a[d+j]-c*x)%31
  a=trim(a)
 return trim(q),a
def inverse_mod(a,b):
 r0,r1=trim(b),divmodp(a,b)[1];s0,s1=[],[1]
 while r1:
  q,r=divmodp(r0,r1);r0,r1=r1,r;s0,s1=s1,add(s0,mul(q,s1),-1)
 if len(r0)!=1:raise ValueError("primary factors not coprime")
 answer=divmodp([x*pow(r0[0],-1,31)%31 for x in s0],b)[1]
 if divmodp(mul(a,answer),b)[1]!=[1]:raise ValueError("actual primary inverse")
 return answer
def value(poly,r):
 result=0
 for x in reversed(poly):result=(result*r+x)%31
 return result
def action(poly,J,V):
 result=nmod_mat(V.nrows(),V.ncols(),31)
 for c in reversed(poly):
  result=J*result
  if c%31:result+=(c%31)*V
 return result
def row_action(poly,J,V):
 result=nmod_mat(V.nrows(),V.ncols(),31)
 for c in reversed(poly):
  result=result*J
  if c%31:result+=(c%31)*V
 return result
def source_action(J,D,polys):
 nc=len(polys[0]);maximum=max([len(p)-1 for row in polys for p in row]+[-1])
 result=nmod_mat(D.nrows(),nc,31);power=D
 for d in range(maximum+1):
  C=nmod_mat([[p[d]%31 if d<len(p) else 0 for p in row] for row in polys],31)
  if not zero(C):result+=power*C
  if d<maximum:power=J*power
 return result
def block(data,metadata,name):
 item=metadata["matrices"][name];n=item["rows"]*item["columns"]
 raw=data[item["offset"]:item["offset"]+n]
 if len(raw)!=n or sha(raw)!=item["sha256"] or any(x>30 for x in raw):raise ValueError("saved matrix "+name)
 return nmod_mat([list(raw[i*item["columns"]:(i+1)*item["columns"]]) for i in range(item["rows"])],31)
def load_state(notes,out):
 reader=notes/"2026-11-14-r150-torsion-characteristic-789f.py";actual(reader,READER_SHA)
 raw=actual(notes/"2026-11-14-r150-torsion-state.bin-789f.gz",STATE_SHA)
 path=out/"same-state-input.bin";path.write_bytes(raw)
 try:
  spec=importlib.util.spec_from_file_location("r150_actual_second_state",reader)
  helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper);state=helper.load_state(path)
 finally:path.unlink(missing_ok=True)
 return state,nmod_mat(state["matrices"]["action"],31)
def save_system(out,name,magic,header,items):
 payload=bytearray(magic)+struct.pack("<"+"I"*len(header),*header);blocks={}
 for key,M in items:
  raw=serial(M);blocks[key]={"offset":len(payload),"rows":M.nrows(),"columns":M.ncols(),"sha256":sha(raw)};payload.extend(raw)
 path=out/name;path.write_bytes(gzip.compress(payload,mtime=0))
 return blocks,{"file":path.name,"uncompressedBytes":len(payload),"uncompressedSHA256":sha(payload),
               "compressedBytes":path.stat().st_size,"compressedSHA256":sha(path.read_bytes())}
def quotient(J,U):
 rows=pivots(U.transpose());rank=U.ncols()
 if len(rows)!=rank:raise ValueError("actual independent source quotient")
 inverse=sub(U,rows,range(rank)).inv();free=[i for i in range(J.nrows()) if i not in set(rows)]
 Uf=sub(U,free,range(rank))
 def project(V):return sub(V,free,range(V.ncols()))-Uf*inverse*sub(V,rows,range(V.ncols()))
 actionq=project(sub(J,range(J.nrows()),free))
 if not zero(project(J*U)):raise ValueError("quotiented source span is not invariant")
 return project,actionq,rows,free,inverse,Uf
def solve_span(columns,target):
 selected=pivots(columns);B=sub(columns,range(columns.nrows()),selected)
 rows=pivots(B.transpose());rank=len(selected)
 if rank:
  inverse=sub(B,rows,range(rank)).inv();F=inverse*sub(target,rows,range(target.ncols()))
 else:inverse=nmod_mat(0,0,31);F=nmod_mat(0,target.ncols(),31)
 residual=target-B*F
 return {"indices":selected,"basis":B,"rows":rows,"inverse":inverse,"solution":F,"residual":residual,
         "flags":[n==0 for n in counts(residual)]}
def polynomial_solution(indices,F,n=7):
 answer=[[[] for _ in range(F.ncols())] for _ in range(n)]
 for r,column in enumerate(indices):
  generator=column%n;power=column//n
  for j in range(F.ncols()):
   if F[r,j]:
    answer[generator][j]+=[0]*max(0,power+1-len(answer[generator][j]))
    answer[generator][j][power]=int(F[r,j])
 return answer

def prepare(a,start):
 seven=json.loads(actual(a.seven_receipt,SEVEN_RECEIPT_SHA))
 sdata=actual(a.seven_system,SEVEN_SYSTEM_SHA)
 pair=json.loads(actual(a.pair_receipt,PAIR_RECEIPT_SHA));pdata=actual(a.pair_system,PAIR_SYSTEM_SHA)
 if sdata[:8]!=b"R150S731" or struct.unpack_from("<8I",sdata,8)!=(31,315,7,308,16,14,1,9):raise ValueError("same complete seven first image")
 if pdata[:8]!=b"R150E831" or struct.unpack_from("<4I",pdata,8)!=(31,315,8,9):raise ValueError("same actual eighth matrix")
 if pair["sevenFirstImageCoefficients"]!=[0,0,1,18,22,2,15] or pair["commonRawAnnihilatorEntire315Ascending"]!=[27,8,26,1]:raise ValueError("actual c and raw primary support")
 state,J=load_state(a.notes_root,a.out)
 U8=block(pdata,pair,"U8");J8=block(pdata,pair,"J8");raw=block(pdata,pair,"whole315RawTargets")
 U=block(sdata,seven,"oldSevenSources");D=block(sdata,seven,"actualAll315NewColumns")
 if sub(U8,range(315),range(7))!=U or J*U8!=U8*J8 or sub(D,range(315),range(7,16))!=raw:raise ValueError("same actual315 sources, action and current raw targets")
 if not zero(action([27,8,26,1],J,raw)):raise ValueError("all actual raw primary support multiplyback")
 columns=pair["kernelOfNewFirstImageColumnsAscending"]
 L=[[list(columns[j][i]) for j in range(7)] for i in range(7)]
 if L[2][2]!=[-2,1] or any(len(p)>2 for row in L for p in row):raise ValueError("same seven polynomial kernel")
 d=source_action(J,sub(D,range(315),range(7)),L)
 rows=pivots(U.transpose());inverse=sub(U,rows,range(7)).inv();C=inverse*sub(d,rows,range(7))
 if U*C!=d:raise ValueError("seven genuine phi first quotients must lie in actual U")
 blocks,system=save_system(a.out,"prepared-seven-second.bin.gz",b"R150A231",[31,315,8,7,9],
  [("U8",U8),("J8",J8),("rawTargets",raw),("oldAll315Columns",D),("cancelledFirstColumns",d),("oldSevenCorrection",C)])
 result={"format":"r150-actual-seven-augmented-second-preparation-v1","status":"completed",
  "sevenGenuineKernelPolynomialsAscending":L,"oldSevenConstantCorrection":[[int(C[i,j]) for j in range(7)] for i in range(7)],
  "allSevenCancelledFirstClassesInU":True,"allNineRawSupportedAt1And2":True,"all315CoordinatesVerified":True,
  "inputK3CostBound":88,"newKernelSourcesNotYetComputed":True,"matrices":blocks,"system":system,
  "inputs":{"sevenReceiptSHA256":SEVEN_RECEIPT_SHA,"sevenSystemSHA256":SEVEN_SYSTEM_SHA,
            "pairReceiptSHA256":PAIR_RECEIPT_SHA,"pairSystemSHA256":PAIR_SYSTEM_SHA,"stateSHA256":STATE_SHA},
  "elapsedSeconds":time.monotonic()-start}
 (a.out/"prepared-seven-second-receipt.json").write_text(json.dumps(result,separators=(",",":"))+"\n")
 print(json.dumps({"status":"completed","allSevenCancelledFirstClassesInU":True,"allNineRawSupportedAt1And2":True,"elapsedSeconds":result["elapsedSeconds"]}),flush=True)

def actual_seven_classes(path,state):
 data=path.read_bytes();wide=data[:8]==b"R150NX31"
 if (not wide and data[:8]!=b"R150NF31") or struct.unpack_from("<3I",data,8)!=(0,7,1034):raise ValueError("same seven complete G remainders")
 index={tuple(c):i for i,c in enumerate(state["coordinates"])};V=nmod_mat(820,7,31);offset=20
 for j in range(7):
  raw,label,count=struct.unpack_from("<IHI",data,offset);offset+=10
  if raw or label!=LABEL7[j]:raise ValueError("actual seven phi labels")
  previous=0
  for _ in range(count):
   component=struct.unpack_from("<H",data,offset)[0];offset+=2
   size=2 if wide else 1;length=int.from_bytes(data[offset:offset+size],"little");offset+=size
   if component<=previous or component>1034 or length<1:raise ValueError("actual G remainder dictionary")
   previous=component
   for degree in range(length):
    x=data[offset];offset+=1
    if x>30:raise ValueError("actual remainder coefficient")
    if x:
     if (component,degree) not in index:raise ValueError("genuine second direction has high free remainder")
     V[index[component,degree],j]=x
 if offset!=len(data):raise ValueError("actual seven remainder tail")
 free=[i for i in range(820) if i+1 not in set(state["pivotStateCoordinates"])]
 D=sub(V,free,range(7))
 K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose()
 O=nmod_mat(state["observabilityEchelon"],31)
 if K*D!=V or not zero(O*V):raise ValueError("all505 original free observations and315 reconstruction")
 return D,V,data

def complete(a,start):
 prepared=json.loads(a.prepared_receipt.read_text());data=actual(a.prepared_system,prepared["system"]["uncompressedSHA256"])
 if prepared.get("status")!="completed" or not prepared.get("allSevenCancelledFirstClassesInU") or data[:8]!=b"R150A231":raise ValueError("actual new seven preparation")
 original=json.loads(a.original_metadata.read_text());image=json.loads(a.image_metadata.read_text())
 if original.get("status")!="completed" or original.get("modulus")!=28629151 or original.get("divisor")!=923521 or original.get("targetCount")!=7 or original.get("targetMode")!=0 or original.get("targetLabels")!=LABEL7 or not original.get("allOriginalProductCoefficientsDivisible") or not original.get("originalRowScaleTransportVerified"):raise ValueError("all actual original17 newK4/p4 divisibilities")
 if image.get("status")!="completed" or image.get("targets")!=7 or not image.get("fullImageQuotientIdentity") or not image.get("everyRemainderIsIrreducible"):raise ValueError("actual seven full G identities")
 state,J=load_state(a.notes_root,a.out);U8=block(data,prepared,"U8");J8=block(data,prepared,"J8")
 raw=block(data,prepared,"rawTargets")
 if U8.rank()!=8 or J*U8!=U8*J8:raise ValueError("actual U8 action")
 D,V,remainder_bytes=actual_seven_classes(a.image_remainders,state)
 project,Jq,rows,free,inverse,Uf=quotient(J,U8)
 characteristic=J.charpoly();char=[int(characteristic[i]) for i in range(characteristic.degree()+1)]
 rest=char[:];f12=[1];multiplicities={}
 for root in (1,2):
  exponent=0
  while len(rest)>1 and value(rest,root)==0:
   rest,remainder=divmodp(rest,[-root,1])
   if remainder:raise ValueError("exact primary polynomial factor")
   f12=mul(f12,[-root,1]);exponent+=1
  multiplicities[str(root)]=exponent
 if len(char)!=316 or sum(multiplicities.values())!=39 or not all(multiplicities.values()):raise ValueError("same full315 torsion and39-dimensional1/2 primary")
 projector=mul(rest,inverse_mod(rest,f12))
 if len(projector)>315 or divmodp(add(mul(projector,projector),projector,-1),char)[1] or divmodp(add(projector,[1],-1),f12)[1] or divmodp(projector,rest)[1]:raise ValueError("complete characteristic-polynomial CRT projector")
 PD=action(projector,J,D)
 if action(projector,J,U8)!=U8 or action(projector,J,raw)!=raw or action(projector,J,PD)!=PD or not zero(action(f12,J,PD)):raise ValueError("actual full315 primary projection checks")
 target=sub(raw,range(315),[j-2 for j in TARGETS]);qt=project(target)
 current=project(PD);fullcurrent=PD;unprojectedcurrent=D
 columns=current;fullcolumns=fullcurrent;unprojectedcolumns=unprojectedcurrent
 oldrank=-1;stable=False
 for degree in range(33):
  indices=pivots(columns);rank=len(indices)
  if rank>31:raise ValueError("primary quotient rank exceeds39minus8")
  print(json.dumps({"phase":"complete-related-second-krylov","maximumPower":degree,"rank":rank,"columns":columns.ncols(),"elapsedSeconds":time.monotonic()-start}),flush=True)
  if rank==oldrank or rank==31:stable=True;break
  oldrank=rank;current=Jq*current;fullcurrent=J*fullcurrent;unprojectedcurrent=J*unprojectedcurrent
  columns=join(columns,current);fullcolumns=join(fullcolumns,fullcurrent);unprojectedcolumns=join(unprojectedcolumns,unprojectedcurrent)
 if not stable:raise ValueError("complete31-dimensional relevant Krylov closure")
 solve=solve_span(columns,qt);rank=len(solve["indices"]);basis=solve["basis"]
 if rank:actionq=solve["inverse"]*sub(Jq*basis,solve["rows"],range(rank))
 else:actionq=nmod_mat(0,0,31)
 if basis*actionq!=Jq*basis:raise ValueError("actual complete arbitrary-degree related second image")
 projected_solution=polynomial_solution(solve["indices"],solve["solution"])
 small=solve_span(project(unprojectedcolumns),qt)
 small_solution=polynomial_solution(small["indices"],small["solution"])
 flags=solve["flags"];used_projection=[False]*7
 F=[[[] for _ in range(7)] for _ in range(7)]
 for j in range(7):
  if not flags[j]:continue
  for i in range(7):
   if small["flags"][j]:F[i][j]=small_solution[i][j]
   else:F[i][j]=mul(projector,projected_solution[i][j]);used_projection[j]=True
 combination=source_action(J,D,F)
 masked=sub(target,range(315),range(7))
 for j in range(7):
  if not flags[j]:
   for i in range(315):masked[i,j]=0
 difference=masked-combination;C=inverse*sub(difference,rows,range(7))
 if U8*C!=difference:raise ValueError("every positive combination must already hold in entire315 with actual U8 correction")
 duals=[]
 for j in range(7):
  if flags[j]:duals.append(None);continue
  coordinate=next(i for i in range(307) if solve["residual"][i,j])
  dual=nmod_mat(1,307,31);dual[0,coordinate]=1
  if rank:
   correction=sub(basis,[coordinate],range(rank))*solve["inverse"]
   for i,r in enumerate(solve["rows"]):dual[0,r]-=correction[0,i]
  val=int((dual*qt)[0,j]);dual=pow(val,-1,31)*dual
  if not zero(dual*columns) or (dual*qt)[0,j]!=1:raise ValueError("exact related quotient dual")
  lift=nmod_mat(1,315,31)
  for i,r in enumerate(free):lift[0,r]=dual[0,i]
  eliminate=dual*Uf*inverse
  for i,r in enumerate(rows):lift[0,r]-=eliminate[0,i]
  full_dual=row_action(projector,J,lift)
  if not zero(full_dual*U8) or not zero(full_dual*unprojectedcolumns) or (full_dual*target)[0,j]!=1:raise ValueError("actual full315 projector-composed arbitrary-degree dual")
  duals.append({"target":TARGETS[j],"original315Coordinates":[int(full_dual[0,i]) for i in range(315)],
    "annihilatesU8":True,"annihilatesCompleteRelatedSecondImage":True,"targetValue":1,
    "scope":"all mod31 initial sources for A+ modulo31^3, using proved old1834 relevant-second-image coverage"})
 maximum=max([len(p)-1 for row in F for p in row]+[-1])
 if maximum>344:raise ValueError("paid degree314 projector plus degree30 source bound")
 blocks,system=save_system(a.out,"complete-augmented-second-image.bin.gz",b"R150A2G1",[31,315,8,307,7,columns.ncols(),rank,7],
  [("actualAll315NewSecondColumns",D),("actual820NewSecondColumns",V),("projectedAll315NewSecondColumns",PD),
   ("U8",U8),("J8",J8),("allNineRawTargets",raw),("quotientAction",Jq),("completeRelatedKrylov",columns),
   ("full315RelatedKrylov",fullcolumns),("full315UnprojectedKrylov",unprojectedcolumns),
   ("selectedImageBasis",basis),("selectedBasisAction",actionq),("relatedBasisSolution",solve["solution"]),
   ("relatedResidual",solve["residual"]),("full315ChosenSourceCombination",combination),("oldEightConstantCorrection",C)])
 result={"format":"r150-complete-relevant-second-image-of-actual-seven-augmented-directions-v1","status":"completed",
  "prime":31,"targetLabels":TARGETS,"newGenuineSecondDirectionsComputed":7,
  "allSevenOriginalMod31FiveDivisibilitiesVerified":True,"all505FreeObservationsVerified":True,"all315CoordinatesRetained":True,
  "relevantPrimaryImageComplete":True,"old198RelevantCoverageUsed":True,"old4ExactAugmentedCoverageUsed":True,
  "old1632ExactSyzygyCoverageUsed":True,"completeOtherPrimarySecondImageAsserted":False,
  "whole315TorsionDimension":315,"quotientTorsionDimension":307,"relevantPrimaryDimension":39,"relevantQuotientDimension":31,
  "relatedSecondImageRank":rank,"KrylovMaximumPower":degree,"KrylovColumnCount":columns.ncols(),
  "KrylovBasisColumnIndicesZeroBased":solve["indices"],"individualTargetCompatible":flags,
  "compatibleTargetLabels":[j for j,f in zip(TARGETS,flags) if f],"obstructedTargetLabels":[j for j,f in zip(TARGETS,flags) if not f],
  "allSevenCompatible":all(flags),"numberOfCompatibleTargets":sum(flags),
  "finiteUnprojectedCombinationCompatible":small["flags"],"unprojectedTrialMaximumPower":degree,
  "unprojectedTrialNotClaimedComplete":True,"primaryProjectorUsedForTarget":used_projection,
  "characteristicPolynomialAscending":char,"completePrimaryMultiplicities":multiplicities,
  "primaryProjectorPolynomialAscending":projector,"primaryProjectorDegree":len(projector)-1,
  "whole315ProjectorIdentityVerified":True,"newSecondSolutionPolynomialsAscending":F,
  "oldEightConstantCorrection":[[int(C[i,j]) for j in range(7)] for i in range(8)],
  "maximumSolutionDegree":maximum,"allCompatibleWhole315IdentitiesVerified":True,"completeRelatedDuals":duals,
  "negativeScope":"A+ has no h0*t_j source modulo31^3 for each listed obstruction, allowing all mod31 initial sources; no claim about unrestricted original rational sources",
  "positiveScope":"full315 identity ready for genuine original17 source recovery; no original product claimed here",
  "finite_budget_verified":False,"fullOriginalMod31FiveIdentityVerified":False,"characteristicZeroIdentityAsserted":False,
  "matrices":blocks,"system":system,
  "inputs":{"preparedReceiptSHA256":sha(a.prepared_receipt.read_bytes()),"originalMetadataSHA256":sha(a.original_metadata.read_bytes()),
   "imageMetadataSHA256":sha(a.image_metadata.read_bytes()),"imageRemaindersSHA256":sha(remainder_bytes),"stateSHA256":STATE_SHA},
  "elapsedSeconds":time.monotonic()-start}
 (a.out/"complete-augmented-second-image-receipt.json").write_text(json.dumps(result,separators=(",",":"))+"\n")
 print(json.dumps({k:result[k] for k in ("status","relevantPrimaryImageComplete","relatedSecondImageRank","individualTargetCompatible",
  "allCompatibleWhole315IdentitiesVerified","maximumSolutionDegree","elapsedSeconds")}),flush=True)
def main():
 p=argparse.ArgumentParser();p.add_argument("--mode",choices=("prepare","complete"),required=True)
 for name in ("notes-root","out"):p.add_argument("--"+name,type=Path,required=True)
 for name in ("seven-receipt","seven-system","pair-receipt","pair-system","prepared-receipt","prepared-system",
              "image-remainders","image-metadata","original-metadata"):p.add_argument("--"+name,type=Path)
 a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
 if a.mode=="prepare":prepare(a,start)
 else:complete(a,start)
if __name__=="__main__":main()
