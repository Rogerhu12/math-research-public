#!/usr/bin/env python3
"""Read only the paid complete second-page matrix; no original source recomputation.
Author: Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
"""
import base64,gzip,hashlib,json,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
P=31
def sha(b):return hashlib.sha256(b).hexdigest()
def rank(a):
 a=[r[:] for r in a];r=0
 for c in range(len(a[0]) if a else 0):
  q=next((i for i in range(r,len(a)) if a[i][c]%P),None)
  if q is None:continue
  a[r],a[q]=a[q],a[r];v=pow(a[r][c]%P,-1,P);a[r]=[x*v%P for x in a[r]]
  for i in range(r+1,len(a)):
   if a[i][c]%P:
    v=a[i][c]%P;a[i]=[(x-v*y)%P for x,y in zip(a[i],a[r])]
  r+=1
 return r
def solve(a,b):
 n=len(a[0]);m=len(b[0]);z=[x[:]+y[:] for x,y in zip(a,b)];r=0;pv=[]
 for c in range(n):
  q=next((i for i in range(r,len(z)) if z[i][c]),None)
  if q is None:continue
  z[r],z[q]=z[q],z[r];v=pow(z[r][c],-1,P);z[r]=[x*v%P for x in z[r]]
  for i in range(len(z)):
   if i!=r and z[i][c]:
    v=z[i][c];z[i]=[(x-v*y)%P for x,y in zip(z[i],z[r])]
  pv.append(c);r+=1
 if len(pv)!=n or any(any(row[n:]) for row in z[r:]):raise ValueError("exact paid source span")
 return [z[i][n:] for i in range(n)]
def mul(a,b):
 bt=list(zip(*b));return [[sum(x*y for x,y in zip(row,col))%P for col in bt] for row in a]
started=time.monotonic()
receiptBytes=(ROOT/"paid-second-complete-receipt.json").read_bytes()
r=json.loads(receiptBytes)
outer=base64.b64decode((ROOT/"paid-second-complete-system-outer.base64").read_bytes())
inner=gzip.decompress(outer);data=gzip.decompress(inner)
assert sha(inner)=="f20487d290193e738a5df67dccdf0c6d11c1c0b9e224dbd310fdc1a0180acaf7"
assert len(data)==552512 and sha(data)=="caeede65edee080936680c459082f1b8d6b1523ac00e00b592cc3d9174dc7aa1"
def block(k):
 d=r["matrices"][k];b=data[d["offset"]:d["offset"]+d["rows"]*d["columns"]]
 assert sha(b)==d["sha256"] and all(x<P for x in b)
 return [list(b[i*d["columns"]:(i+1)*d["columns"]]) for i in range(d["rows"])]
R=block("targetResidual");B=block("imageBasis");J=block("quotientAction")
D=block("all204Projected315SecondColumns");U9=block("U9");raw=block("rawTargets")
assert rank(B)==4 and rank(R)==1
pivot=next(i for i in range(306) if R[i][0])
co=[x*pow(R[pivot][0],-1,P)%P for x in R[pivot]]
assert all(co) and all(R[i][j]==co[j]*R[i][0]%P for i in range(306) for j in range(9))
JR=mul(J,R);dif=[[(JR[i][j]-2*R[i][j])%P for j in range(9)] for i in range(306)]
actionCorrection=solve(B,dif)
assert mul(B,actionCorrection)==dif
paid=[U9[i]+[D[i][k] for k in (6,7,8,9)] for i in range(315)]
difference=[[(raw[i][j]-co[j]*raw[i][0])%P for j in range(9)] for i in range(315)]
sourceCorrection=solve(paid,difference)
assert mul(paid,sourceCorrection)==difference
assert rank(paid)==13 and rank([paid[i]+raw[i] for i in range(315)])==14
out={"format":"r150-paid-second-target-line-readout-v1","status":"completed","prime":31,
"sourceRun":43662590949,"sourceDataCommit":"d6e445205653e2ab4296a47d2b6c94358b84a80e",
"completeSystemCompressedSHA256":sha(inner),"completeSystemUncompressedSHA256":sha(data),
"targetLabels":list(range(2,11)),"paidSpaceBasis":["b1","b2","b3","b4","b5","b6","b7","b8","b9","D4_15001","D4_15002","D4_15003","D4_15004"],
"paidSpaceDimension":13,"paidSpaceWithAllRawTargetsDimension":14,"remainingTargetQuotientDimension":1,
"remainingTargetBasisLabel":2,"allNineRemainingClassesNonzero":True,"remainingTargetCoordinates":co,
"remainingTargetSAction":[[2]],"allNineExactAnnihilatorsAscending":[[29,1] for _ in range(9)],
"full315DifferenceSourceCoordinates":sourceCorrection,
"quotientActionCorrectionInSecondImage":actionCorrection,
"full315AllDifferenceIdentitiesVerified":True,"completeOriginalThirdNotComputed":True,
"thirdLocalCompatibilityMustBeAllOrNone":True,
"scope":"Only the actual paid second-page quotient. The common nonzero target line may still be met by the pending complete third image. No original modp6 obstruction is asserted.",
"elapsedSeconds":time.monotonic()-started}
(ROOT/"saturated-second-target-line-readout.json").write_text(json.dumps(out,separators=(",",":"))+"\n")
print(json.dumps(out))
