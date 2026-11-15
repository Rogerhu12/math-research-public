from pathlib import Path
import base64,gzip,hashlib,json,time
began=time.monotonic()
root=Path(__file__).resolve().parent
outer=base64.b64decode((root/"paid-prepared197-outer.base64").read_text())
assert hashlib.sha256(outer).hexdigest()=="cb12c5a66c57d97ce3221beb9baa24c5e09b8fc48aef838f97d87faae8b752f7"
inner=gzip.decompress(outer);assert hashlib.sha256(inner).hexdigest()=="9aa1b6e3fd97a3502d1929633656364277711991ae452e7a1d6c8e63a1823ece"
data=gzip.decompress(inner);meta=json.loads((root/"paid-prepared197-receipt.json").read_text())
assert hashlib.sha256(data).hexdigest()==meta["system"]["uncompressedSHA256"]
def block(k):
 d=meta["matrices"][k];b=data[d["offset"]:d["offset"]+d["rows"]*d["columns"]]
 assert hashlib.sha256(b).hexdigest()==d["sha256"]
 return [list(b[i*d["columns"]:(i+1)*d["columns"]]) for i in range(d["rows"])]
def mul(A,B):
 return [[sum(x*B[k][j] for k,x in enumerate(row))%31 for j in range(len(B[0]))] for row in A]
def sub(A,B):return [[(x-y)%31 for x,y in zip(a,b)] for a,b in zip(A,B)]
def rank(A):
 A=[row[:] for row in A];r=0
 for j in range(len(A[0])):
  k=next((k for k in range(r,len(A)) if A[k][j]),None)
  if k is None:continue
  A[r],A[k]=A[k],A[r];iv=pow(A[r][j],-1,31);A[r]=[v*iv%31 for v in A[r]]
  for i in range(r+1,len(A)):
   if A[i][j]:
    v=A[i][j];A[i]=[(x-v*y)%31 for x,y in zip(A[i],A[r])]
  r+=1
 return r
U=[row[:9] for row in block("V10")];P=block("whole315PrimaryProjector");raw=block("rawTargets")
projected=mul(P,raw);outside=sub(raw,projected)
aug=[a+b for a,b in zip(U,outside)];r=0
for j in range(9):
 k=next(i for i in range(r,315) if aug[i][j]);aug[r],aug[k]=aug[k],aug[r];v=pow(aug[r][j],-1,31);aug[r]=[v*x%31 for x in aug[r]]
 for i in range(315):
  if i!=r and aug[i][j]:
   v=aug[i][j];aug[i]=[(x-v*y)%31 for x,y in zip(aug[i],aug[r])]
 r+=1
assert all(not any(a) for a in aug[9:])
C=[row[9:] for row in aug[:9]];assert mul(U,C)==outside
J=[row[:9] for row in block("J10")[:9]]
JminusI=[[(J[i][j]-int(i==j))%31 for j in range(9)] for i in range(9)]
ann=C
for _ in range(3):ann=mul(JminusI,ann)
result={"status":"completed","sourceRun":43653360404,"sourceSystemUncompressedSHA256":meta["system"]["uncompressedSHA256"],
"fullRawTargetsPreserved":True,"rawEqualsRoot2Projection":raw==projected,
"outsideRoot2TargetRank":rank(outside),"individualOutsideNonzero":[any(outside[i][j] for i in range(315)) for j in range(9)],
"outsideAllInActualU9":True,"actualU9OutsideCoordinates":C,
"outsideKilledBySMinusOneCubed":not any(any(row) for row in ann),
"rawTargetRank":rank(raw),"projectedTargetRank":rank(projected),
"noOriginalSourceOrNormalFormRecomputed":True,"elapsedSeconds":time.monotonic()-began}
(root/"saturated-target-scope-readout.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result))
