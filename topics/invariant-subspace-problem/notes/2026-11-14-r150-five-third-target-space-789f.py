#!/usr/bin/env python3
"""Read-only exact postprocessing of the completed five-third run; no native mathematics is rerun."""
import argparse,gzip,hashlib,json,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
P=31
RECEIPT_SHA="d6f1981d28dee4dff86e11842b3f54aae62b1cf41e1ae71e435304a428016333"
SYSTEM_SHA="6030938d53584f139eb1fe45ff8011b9a9fcaaa85dba4da4125f93dcb9224e43"
GZIP_SHA="a73d7b1617db09c753f8a1f2183203ca32954dda33173f29b2346c05c8af9917"
OUTER_SHA="0ac91df70eab1ee11ea9a092a83055abe8fefad7a9b1043e89fc9408e01512d8"
ORIGINAL_SHA="ae0839ae0518f81bf9032febb3d2c77a6f7e31fadd95c880210a4dc22de08a3c"
NEW=[9301,9302,9305,9306,9307]
TARGETS=list(range(2,11))
def sha(b):return hashlib.sha256(b).hexdigest()
def trans(A):return [list(x) for x in zip(*A)]
def sub(A,rows,cols):return [[A[i][j] for j in cols] for i in rows]
def join(*args):return [sum((A[i] for A in args),[]) for i in range(len(args[0]))]
def mul(A,B):
 bt=trans(B)
 return [[sum(x*y for x,y in zip(row,col))%P for col in bt] for row in A]
def minus(A,B):return [[(x-y)%P for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,c):return [[x*c%P for x in a] for a in A]
def zero(A):return not any(x for a in A for x in a)
def pivots(A):
 M=[r[:] for r in A];n=len(M);m=len(M[0]) if n else 0;k=0;out=[]
 for j in range(m):
  q=next((i for i in range(k,n) if M[i][j]),None)
  if q is None:continue
  M[k],M[q]=M[q],M[k];v=pow(M[k][j],-1,P);M[k]=[x*v%P for x in M[k]]
  for i in range(k+1,n):
   c=M[i][j]
   if c:M[i]=[(x-c*y)%P for x,y in zip(M[i],M[k])]
  out.append(j);k+=1
  if k==n:break
 return out
def inv(A):
 n=len(A)
 if any(len(row)!=n for row in A):raise ValueError("square exact inverse")
 M=[r[:]+[int(i==j) for j in range(n)] for i,r in enumerate(A)]
 for j in range(n):
  q=next((i for i in range(j,n) if M[i][j]),None)
  if q is None:raise ValueError("singular selected actual minor")
  M[j],M[q]=M[q],M[j];v=pow(M[j][j],-1,P);M[j]=[x*v%P for x in M[j]]
  for i in range(n):
   if i!=j:
    c=M[i][j]
    if c:M[i]=[(x-c*y)%P for x,y in zip(M[i],M[j])]
 return [r[n:] for r in M]
def solve(A,T):
 columns=pivots(A);B=sub(A,range(len(A)),columns);rows=pivots(trans(B))
 if len(rows)!=len(columns):raise ValueError("rank factorization")
 if columns:
  C=mul(inv(sub(B,rows,range(len(columns)))),sub(T,rows,range(len(T[0]))))
  R=minus(T,mul(B,C))
 else:C=[];R=[x[:] for x in T]
 flags=[not any(row[j] for row in R) for j in range(len(T[0]))]
 return columns,B,C,R,flags
def actual_file(root,names,expected):
 for name in names:
  p=root/name
  if p.is_file():
   b=p.read_bytes()
   if sha(b)==expected:return p,b
 raise ValueError("saved exact file unavailable: "+",".join(names))
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--data-dir",type=Path,required=True);p.add_argument("--out",type=Path,required=True)
 a=p.parse_args();start=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
 rp,rb=actual_file(a.data_dir,["complete-five-third__complete-five-third-image-receipt.json",
  "complete-five-third/complete-five-third-image-receipt.json",
  "recovery-files/complete-five-third/complete-five-third-image-receipt.json"],RECEIPT_SHA)
 r=json.loads(rb)
 if r.get("status")!="completed" or r.get("fiveRelatedImageRank")!=1 or r.get("newDirectionLabels")!=NEW or r.get("targetLabels")!=TARGETS or r.get("individualTargetCompatible")!=[False]*9 or r.get("KrylovBasisColumnIndicesZeroBased")!=[2] or r.get("fiveRelatedImageMinimumAnnihilatorAscending")!=[29,1]:raise ValueError("same actual completed five-source conclusion")
 op,ob=actual_file(a.data_dir,["genuine-five-h5-original__genuine-five-h5-original-original-product.json",
  "genuine-five-h5-original/genuine-five-h5-original-original-product.json",
  "recovery-files/genuine-five-h5-original/genuine-five-h5-original-original-product.json"],ORIGINAL_SHA)
 original=json.loads(ob)
 if r["inputs"]["originalMetadataSHA256"]!=ORIGINAL_SHA or original.get("status")!="completed" or original.get("targetLabels")!=NEW or original.get("modulus")!=887503681 or original.get("divisor")!=28629151 or not original.get("allOriginalProductCoefficientsDivisible") or not original.get("originalRowScaleTransportVerified"):raise ValueError("same genuine five H5 source costs and p5 divisibility")
 costs=original["actualSourceCosts"]
 if costs!=[86,87,87,88,87]:raise ValueError("same five actual paid source costs")
 plain=None;compressed=None;system_path=None;outer=None
 for name in ["complete-five-third/complete-five-third-image.bin.gz",
              "recovery-files/complete-five-third/complete-five-third-image.bin.gz"]:
  q=a.data_dir/name
  if q.is_file() and sha(q.read_bytes())==GZIP_SHA:compressed=q.read_bytes();system_path=q;break
 if compressed is None:
  system_path,outer=actual_file(a.data_dir,["certificates/complete-five-third__complete-five-third-image.bin.gz.gz"],OUTER_SHA)
  compressed=gzip.decompress(outer)
 if len(compressed)!=33007 or sha(compressed)!=GZIP_SHA:raise ValueError("exact preserved inner gzip")
 plain=gzip.decompress(compressed)
 if len(plain)!=122023 or sha(plain)!=SYSTEM_SHA or plain[:8]!=b"R150F3G1":raise ValueError("exact saved complete315 matrix system")
 def block(name):
  s=r["matrices"][name];b=plain[s["offset"]:s["offset"]+s["rows"]*s["columns"]]
  if len(b)!=s["rows"]*s["columns"] or sha(b)!=s["sha256"] or any(x>=31 for x in b):raise ValueError("complete matrix "+name)
  return [list(b[i*s["columns"]:(i+1)*s["columns"]]) for i in range(s["rows"])]
 U=block("U9");J9=block("J9");R=block("allNineRawTargets");D=block("actualAll315NewThirdColumns")
 PD=block("projectedAll315NewThirdColumns");K=block("completeFiveRelatedKrylov");FK=block("full315RelatedKrylov");Jq=block("quotientAction")
 if len(pivots(U))!=9 or FK!=join(PD,sub(FK,range(315),range(5,10))):raise ValueError("same full related source columns")
 rows=pivots(trans(U));free=[i for i in range(315) if i not in set(rows)];Ui=inv(sub(U,rows,range(9)));Uf=sub(U,free,range(9))
 def project(M):return minus(sub(M,free,range(len(M[0]))),mul(mul(Uf,Ui),sub(M,rows,range(len(M[0])))))
 qR=project(R);qD=project(PD);base=sub(PD,range(315),[2]);qbase=project(base)
 if project(FK)!=K or len(pivots(qD))!=1 or len(pivots(qR))!=4 or zero(qbase):raise ValueError("actual projected rank1 and old target rank4")
 if mul(Jq,qR)!=scale(qR,2) or mul(Jq,qD)!=scale(qD,2) or sub(K,range(306),range(5,10))!=mul(Jq,qD):raise ValueError("exact saved quotient action at2")
 S=join(U,base);indices,B,Cfive,res,flags=solve(S,PD)
 if len(indices)!=10 or not all(flags) or not zero(res) or mul(S,Cfive)!=PD:raise ValueError("five true projected sources in actual U9 plus projected9305")
 union_rank=len(pivots(join(U,R,PD)));target_span_rank=len(pivots(join(U,R)));paid_rank=len(pivots(S))
 in_old=solve(join(U,R),base)
 lies=all(in_old[4])
 if lies!=(union_rank==target_span_rank):raise ValueError("actual intersection rank")
 # Full315 expression of the new projected9305 in old U9+raw, when it exists.
 relation=None
 if lies:
  full=[0]*18
  for j,c in zip(in_old[0],in_old[2]):full[j]=c[0]
  if mul(join(U,R),[[x] for x in full])!=base:raise ValueError("complete new source relation")
  relation={"U9Coefficients":full[:9],"rawTargetCoefficients":full[9:],"identity":"projected_d9305 = U9*c + rawTargets*f"}
 # Same row-pivot quotient, now adding the new paid source.
 srows=pivots(trans(S));sfree=[i for i in range(315) if i not in set(srows)]
 Si=inv(sub(S,srows,range(10)));Sf=sub(S,sfree,range(10))
 residual=minus(sub(R,sfree,range(9)),mul(mul(Sf,Si),sub(R,srows,range(9))))
 tidx,TB,TC,tres,tflags=solve(residual,residual)
 remaining=len(tidx)
 if not all(tflags) or not zero(tres) or remaining!=union_rank-paid_rank:raise ValueError("complete remaining target module coordinates")
 rawbasis=sub(R,range(315),tidx);diff=minus(R,mul(rawbasis,TC))
 ssolve=solve(S,diff)
 if not all(ssolve[4]) or not zero(ssolve[3]) or mul(S,ssolve[2])!=diff:raise ValueError("all nine full315 residual source relations")
 jbase=sub(FK,range(315),[7]);delta=minus(jbase,scale(base,2))
 udelta=mul(Ui,sub(delta,rows,[0]))
 if mul(U,udelta)!=delta:raise ValueError("complete J(projected9305) source correction")
 J10=[J9[i][:]+[udelta[i][0]] for i in range(9)]+[[0]*9+[2]]
 raw_vs_actual=solve(S,D)
 actual_family=solve(join(U,D),D)
 actual_basis_labels=[NEW[i-9] for i in actual_family[0] if i>=9]
 actual_low=[j for j,c in enumerate(costs) if c<=87]
 low_family=solve(join(U,sub(D,range(315),actual_low)),D)
 low_basis_labels=[NEW[actual_low[i-9]] for i in low_family[0] if i>=9]
 if not all(actual_family[4]) or not zero(actual_family[3]) or mul(actual_family[1],actual_family[2])!=D:raise ValueError("all five unprojected whole315 source coordinates")
 result={"format":"r150-five-third-paid-rank1-and-remaining-target-space-v1","status":"completed","prime":31,
  "sourceRun":43646683083,"sourceDataCommit":"ca194ccead4869f8548748a3fd792963e49d63b0",
  "noNativeMathematicsRecomputed":True,"old198ThirdDirectionsComputed":False,"completeLowInitialThirdImageComputed":False,
  "actualFiveH5SourceCosts":costs,"rankActualFiveColumns":len(pivots(D)),
  "rankU9ActualFive":len(actual_family[0]),"newUnprojectedIndependentLabelsAboveU9":actual_basis_labels,
  "actualFiveSourceCoordinatesRelativeToU9ThenIndependentNew":actual_family[2],
  "sourceCost87EligibleLabels":[NEW[j] for j in actual_low],
  "rankU9ActualCost87Columns":len(low_family[0]),"newCost87IndependentLabelsAboveU9":low_basis_labels,
  "newUnprojectedClassesAboveU9":len(actual_family[0])-9,"newCost87ClassesAboveU9":len(low_family[0])-9,
  "unprojectedNewSpanInvarianceAsserted":False,
  "rankU9":9,"rankU9Raw":target_span_rank,"rankU9ProjectedFive":paid_rank,"rankU9RawProjectedFive":union_rank,
  "oldTargetQuotientDimension":4,"paidFiveQuotientDimension":1,"paidDirectionInsideOldTargetSpace":lies,
  "intersectionDimensionModuloU9":4+1-(union_rank-9),"remainingTargetQuotientDimension":remaining,
  "newDirectionLabels":NEW,"targetLabels":TARGETS,"projectedSourceBasisLabel":9305,
  "fiveProjectedSourceCoefficientsRelativeToU9ThenProjected9305":Cfive,
  "projected9305InU9AndOldTargets":relation,
  "remainingTargetBasisLabels":[TARGETS[j] for j in tidx],
  "remainingTargetCoordinates":TC,
  "rawTargetCorrectionRelativeToU9ThenProjected9305":ssolve[2],
  "remainingTargetAction":[[2*int(i==j) for j in range(remaining)] for i in range(remaining)],
  "remainingTargetActionIsScalar2":True,
  "J10ForU9ThenProjected9305":J10,
  "allNineRawFull315DecompositionsVerified":True,
  "allFiveProjectedFull315SourceRelationsVerified":True,
  "unprojectedDirectionColumnsInThisTenDimensionalSpace":raw_vs_actual[4],
  "projectionPolynomialAscending":r["primaryProjectorPolynomialAscending"],
  "inputs":{"receipt":str(rp),"receiptSHA256":RECEIPT_SHA,"originalReceipt":str(op),"originalReceiptSHA256":ORIGINAL_SHA,"savedSystem":str(system_path),
   "preservedOuterGzipSHA256":OUTER_SHA if outer is not None else None,"innerGzipSHA256":GZIP_SHA,"completeSystemSHA256":SYSTEM_SHA,
   "allUsedMatrixBlockSHA256":{key:r["matrices"][key]["sha256"] for key in ["U9","J9","allNineRawTargets","actualAll315NewThirdColumns","projectedAll315NewThirdColumns","completeFiveRelatedKrylov","full315RelatedKrylov","quotientAction"]}},
  "elapsedSeconds":time.monotonic()-start,
  "scope":"Exact finite postprocessing of already completed matrices. The new paid source is projected9305, with its actual CRT polynomial retained. No unprojected or characteristic-zero source identity is inferred."}
 (a.out/"five-third-target-space-receipt.json").write_text(json.dumps(result,indent=2)+"\n")
 print(json.dumps({key:result[key] for key in ["status","rankU9RawProjectedFive","paidDirectionInsideOldTargetSpace","remainingTargetQuotientDimension","elapsedSeconds"]}),flush=True)
if __name__=="__main__":main()
