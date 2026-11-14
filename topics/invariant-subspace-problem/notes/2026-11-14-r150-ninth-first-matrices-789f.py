#!/usr/bin/env python3
"""Complete first image of F9: one actual new relation, nine new original residuals, all315/free coordinates."""
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


LABEL10=[9001]+list(range(2,11))
LABEL9=list(range(2,11))
def actual_ten_classes(path,state):
 data=path.read_bytes();wide=data[:8]==b"R150NX31"
 if (not wide and data[:8]!=b"R150NF31") or struct.unpack_from("<3I",data,8)!=(0,10,1034):raise ValueError("same ten complete G remainders")
 index={tuple(c):i for i,c in enumerate(state["coordinates"])};V=nmod_mat(820,10,31);offset=20
 for j in range(10):
  raw,label,count=struct.unpack_from("<IHI",data,offset);offset+=10
  if raw or label!=LABEL10[j]:raise ValueError("actual ninth plus current nine labels")
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
     if (component,degree) not in index:raise ValueError("actual new residue has high free remainder; not a completed torsion conclusion")
     V[index[component,degree],j]=x
 if offset!=len(data):raise ValueError("actual ten remainder tail")
 free=[i for i in range(820) if i+1 not in set(state["pivotStateCoordinates"])]
 D=sub(V,free,range(10))
 K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose()
 O=nmod_mat(state["observabilityEchelon"],31)
 if K*D!=V or not zero(O*V):raise ValueError("all505 original free observations and315 reconstruction")
 return D,V,data

def main():
 parser=argparse.ArgumentParser()
 for name in ("notes-root","prepared-receipt","prepared-system","image-remainders","image-metadata","original-metadata","out"):
  parser.add_argument("--"+name,type=Path,required=True)
 a=parser.parse_args();a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
 prepared=json.loads(a.prepared_receipt.read_text())
 data=actual(a.prepared_system,prepared["system"]["uncompressedSHA256"])
 if prepared.get("status")!="completed" or not prepared.get("fullF9FirstImageRequiresOnlyNinthRelation") or data[:8]!=b"R150U931":raise ValueError("actual nine-source preparation")
 original=json.loads(a.original_metadata.read_text());image=json.loads(a.image_metadata.read_text())
 if original.get("status")!="completed" or original.get("modulus")!=887503681 or original.get("divisor")!=28629151 or original.get("targetCount")!=10 or original.get("targetMode")!=0 or original.get("targetLabels")!=LABEL10 or not original.get("allOriginalProductCoefficientsDivisible") or not original.get("originalRowScaleTransportVerified"):raise ValueError("same ten actual original17 divisibilities")
 if image.get("status")!="completed" or image.get("targets")!=10 or not image.get("fullImageQuotientIdentity") or not image.get("everyRemainderIsIrreducible"):raise ValueError("actual ten complete G identities")
 state,J=load_state(a.notes_root,a.out)
 U9=block(data,prepared,"U9");J9=block(data,prepared,"J9")
 if U9.rank()!=9 or J*U9!=U9*J9:raise ValueError("actual full U9 action")
 D,V,remainder_bytes=actual_ten_classes(a.image_remainders,state)
 new=sub(D,range(315),[0]);target=sub(D,range(315),range(1,10))
 project,Jq,rows,free,inverse,Uf=quotient(J,U9)
 qt=project(target);current=project(new);fullcurrent=new
 columns=current;fullcolumns=fullcurrent;oldrank=-1;stable=False
 for degree in range(307):
  selected=pivots(columns);rank=len(selected)
  print(json.dumps({"phase":"complete-ninth-first-krylov","maximumPower":degree,"rank":rank,"columns":columns.ncols(),"elapsedSeconds":time.monotonic()-start}),flush=True)
  if rank==oldrank or rank==306:stable=True;break
  oldrank=rank;current=Jq*current;fullcurrent=J*fullcurrent
  columns=join(columns,current);fullcolumns=join(fullcolumns,fullcurrent)
 if not stable:raise ValueError("complete306-dimensional full cyclic closure")
 solve=solve_span(columns,qt);rank=len(solve["indices"]);basis=solve["basis"]
 if rank:actionq=solve["inverse"]*sub(Jq*basis,solve["rows"],range(rank))
 else:actionq=nmod_mat(0,0,31)
 if basis*actionq!=Jq*basis:raise ValueError("actual arbitrary-degree complete first image")
 if rank:
  poly=actionq.charpoly();alpha=[int(poly[i]) for i in range(poly.degree()+1)]
  if len(alpha)!=rank+1 or not zero(action(alpha,Jq,project(new))):raise ValueError("actual cyclic minimum annihilator")
 else:alpha=[1]
 flags=solve["flags"];F=polynomial_solution(solve["indices"],solve["solution"],1)
 for j,f in enumerate(flags):
  if not f:F[0][j]=[]
 combination=source_action(J,new,F);masked=sub(target,range(315),range(9))
 for j in range(9):
  if not flags[j]:
   for i in range(315):masked[i,j]=0
 difference=masked-combination;C=inverse*sub(difference,rows,range(9))
 if U9*C!=difference:raise ValueError("all compatible full315 source identities")
 duals=[]
 for j in range(9):
  if flags[j]:duals.append(None);continue
  coordinate=next(i for i in range(306) if solve["residual"][i,j])
  dual=nmod_mat(1,306,31);dual[0,coordinate]=1
  if rank:
   correction=sub(basis,[coordinate],range(rank))*solve["inverse"]
   for i,r in enumerate(solve["rows"]):dual[0,r]-=correction[0,i]
  val=int((dual*qt)[0,j]);dual=pow(val,-1,31)*dual
  if not zero(dual*columns) or (dual*qt)[0,j]!=1:raise ValueError("complete first quotient dual")
  lift=nmod_mat(1,315,31)
  for i,r in enumerate(free):lift[0,r]=dual[0,i]
  eliminate=dual*Uf*inverse
  for i,r in enumerate(rows):lift[0,r]-=eliminate[0,i]
  if not zero(lift*U9) or not zero(lift*fullcolumns) or (lift*target)[0,j]!=1:raise ValueError("actual full315 arbitrary-degree dual")
  duals.append({"target":LABEL9[j],"original315Coordinates":[int(lift[0,i]) for i in range(315)],
    "annihilatesU9":True,"annihilatesCompleteF9FirstImage":True,"targetValue":1,
    "scope":"all first-kernel corrections of F9 while keeping the current source modulo31^2; not all lower initial sources"})
 maximum=max([len(p)-1 for row in F for p in row]+[-1])
 if maximum>305:raise ValueError("finite306-dimensional cyclic coefficient bound")
 blocks,system=save_system(a.out,"complete-ninth-first-image.bin.gz",b"R150F931",[31,315,9,306,10,columns.ncols(),rank,9],
  [("actualAll315NewColumns",D),("actual820NewColumns",V),("U9",U9),("J9",J9),("quotientAction",Jq),
   ("completeFirstKrylov",columns),("full315FirstKrylov",fullcolumns),("selectedImageBasis",basis),
   ("selectedBasisAction",actionq),("imageBasisSolution",solve["solution"]),("imageResidual",solve["residual"]),
   ("full315ChosenSourceCombination",combination),("oldNineConstantCorrection",C)])
 result={"format":"r150-complete-first-image-of-actual-ninth-augmented-module-v1","status":"completed","prime":31,
  "targetLabels":LABEL9,"newGenuineFirstDirectionsComputed":1,"allTenOriginalMod31SixDivisibilitiesVerified":True,
  "all505FreeObservationsVerified":True,"all315CoordinatesRetained":True,"fullF9FirstImageComplete":True,
  "all1834OriginalAndEightAugmentedDirectionsCovered":True,"completeHigherInitialFreedomComputed":False,
  "otherPrimaryFirstImageIncluded":True,"whole315TorsionDimension":315,"quotientTorsionDimension":306,
  "newFirstImageRank":rank,"KrylovMaximumPower":degree,"KrylovColumnCount":columns.ncols(),
  "KrylovBasisColumnIndicesZeroBased":solve["indices"],"newFirstImageMinimumAnnihilatorAscending":alpha,
  "individualTargetCompatible":flags,"compatibleTargetLabels":[j for j,f in zip(LABEL9,flags) if f],
  "obstructedTargetLabels":[j for j,f in zip(LABEL9,flags) if not f],"allNineCompatible":all(flags),
  "numberOfCompatibleTargets":sum(flags),"firstSolutionPolynomialsAscending":F,
  "oldNineConstantCorrection":[[int(C[i,j]) for j in range(9)] for i in range(9)],
  "maximumSolutionDegree":maximum,"allCompatibleWhole315IdentitiesVerified":True,"completeFirstDuals":duals,
  "negativeScope":"listed current F9 sources modulo31^2 cannot be lifted one more digit using the full first kernel image; lower initial source changes remain unpaid",
  "positiveScope":"full315 identity ready for actual31^2h0 modulo31^6 original17 recovery",
  "finite_budget_verified":False,"fullOriginalMod31SixIdentityVerified":False,"characteristicZeroIdentityAsserted":False,
  "matrices":blocks,"system":system,"inputs":{"preparedReceiptSHA256":sha(a.prepared_receipt.read_bytes()),
   "originalMetadataSHA256":sha(a.original_metadata.read_bytes()),"imageMetadataSHA256":sha(a.image_metadata.read_bytes()),
   "imageRemaindersSHA256":sha(remainder_bytes),"stateSHA256":STATE_SHA},"elapsedSeconds":time.monotonic()-start}
 (a.out/"complete-ninth-first-image-receipt.json").write_text(json.dumps(result,separators=(",",":"))+"\n")
 print(json.dumps({k:result[k] for k in ("status","fullF9FirstImageComplete","newFirstImageRank","individualTargetCompatible",
  "allCompatibleWhole315IdentitiesVerified","maximumSolutionDegree","elapsedSeconds")}),flush=True)
if __name__=="__main__":main()
