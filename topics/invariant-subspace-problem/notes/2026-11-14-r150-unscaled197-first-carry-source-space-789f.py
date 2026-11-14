#!/usr/bin/env python3
"""Read the completed197 systems: actual source coordinates, not new VQ or products."""
from __future__ import annotations
import argparse,gzip,hashlib,json,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
from flint import nmod_mat
P=31
LOCK={
 "prepared_receipt":"afdc1b2495b22111ae04b25f9d0ddec7c10b803ebb029ffab0257788532b1e32",
 "prepared_system":"9aa1b6e3fd97a3502d1929633656364277711991ae452e7a1d6c8e63a1823ece",
 "complete_receipt":"c1e2b8e1fcf4c31972e1cc34b253824b39cb3c6a724baac69766761d9f129739",
 "complete_system":"d62a5e1705d0cbc0ce0544e65ff47f2c1c76208e5843de0ab9d812e7aebd9796"}
def sha(b):return hashlib.sha256(b).hexdigest()
def arr(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def sub(M,rows,cols):
 rows=list(rows);cols=list(cols)
 return nmod_mat(len(rows),len(cols),[int(M[i,j]) for i in rows for j in cols],P)
def zero(n,m):return nmod_mat(n,m,P)
def iszero(M):return all(int(x)==0 for x in M.entries())
def join(A,B):
 if A.nrows()!=B.nrows():raise ValueError("join row mismatch")
 return nmod_mat(A.nrows(),A.ncols()+B.ncols(),[int(M[i,j]) for i in range(A.nrows()) for M in (A,B) for j in range(M.ncols())],P)
def pivots(A):
 R,rank=A.rref();ps=[]
 for i in range(rank):
  j=next((j for j in range(R.ncols()) if R[i,j]),None)
  if j is None:raise ValueError("actual rref rank")
  ps.append(j)
 return ps
def solve(B,T):
 if B.nrows()!=T.nrows():raise ValueError("solve row mismatch")
 if not B.ncols():
  if not iszero(T):raise ValueError("nonzero target in empty span")
  return zero(0,T.ncols())
 rows=pivots(B.transpose())
 if len(rows)!=B.ncols():raise ValueError("basis independence")
 C=sub(B,rows,range(B.ncols())).inv()*sub(T,rows,range(T.ncols()))
 if B*C!=T:raise ValueError("complete source-coordinate identity")
 return C
def block(data,meta,key):
 d=meta["matrices"][key];n=d["rows"];m=d["columns"];raw=data[d["offset"]:d["offset"]+n*m]
 if len(raw)!=n*m or sha(raw)!=d["sha256"] or any(v>=31 for v in raw):raise ValueError("actual matrix block "+key)
 return nmod_mat(n,m,list(raw),P)
def poly_action(J,C,poly):
 R=zero(C.nrows(),C.ncols())
 for x in reversed(poly):R=J*R+C*x
 return R
def closed_image(J,C,labels):
 n=J.nrows();allcols=C;current=C;provenance=[dict(x,power=0) for x in labels];last=-1;largest=0
 for step in range(n+1):
  rank=allcols.rank();largest=step
  if rank==last:break
  last=rank
  if step==n:raise ValueError("finite-dimensional polynomial closure did not stabilize")
  current=J*current;allcols=join(allcols,current);provenance.extend(dict(x,power=step+1) for x in labels)
 ps=pivots(allcols);B=sub(allcols,range(n),ps);action=solve(B,J*B);coordinates=solve(B,C)
 if B.rank()!=len(ps) or B*action!=J*B or B*coordinates!=C:raise ValueError("complete finite image identity")
 return {"constantRank":C.rank(),"polynomialImageDimension":len(ps),"maximumPowerConstructed":largest,
  "basisSourceMonomials":[provenance[i] for i in ps],"basisCoordinates":arr(B),
  "basisAction":arr(action),"originalGeneratorCoordinates":arr(coordinates),
  "allPolynomialImageRelationsVerified":True},B
def main():
 ap=argparse.ArgumentParser()
 for name in LOCK:ap.add_argument("--"+name.replace("_","-"),type=Path,required=True)
 ap.add_argument("--out",type=Path,required=True)
 a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic();inputs={}
 raw={}
 for name,expected in LOCK.items():
  p=getattr(a,name);b=p.read_bytes()
  if sha(b)!=expected:raise ValueError("frozen actual input "+name)
  raw[name]=b;inputs[name]={"bytes":len(b),"sha256":expected}
 prep=json.loads(raw["prepared_receipt"]);complete=json.loads(raw["complete_receipt"])
 pb=gzip.decompress(raw["prepared_system"]);cb=gzip.decompress(raw["complete_system"])
 if sha(pb)!=prep["system"]["uncompressedSHA256"] or sha(cb)!=complete["system"]["uncompressedSHA256"]:raise ValueError("actual decompressed system")
 if pb[:8]!=b"R1503P1A" or cb[:8]!=b"R1503G1A":raise ValueError("saved actual system magic")
 if prep.get("status")!="completed" or complete.get("status")!="completed" or not complete.get("all197ThirdDirectionsComputed") or complete.get("newRelatedThirdImageRank")!=0:raise ValueError("completed197 actual input")
 if not all(complete.get(k) is True for k in ("all197OriginalLocalTenJetIdentitiesVerified","all143LocalCoordinatesRetained","all104LocalFreeChecksVerified","completeRelevantLowInitialThirdImageComputed")):raise ValueError("actual input identity flags")
 V=block(cb,complete,"V10");J=block(cb,complete,"J10");D=block(cb,complete,"projected315ThirdColumns")
 if V!=block(pb,prep,"V10") or J!=block(pb,prep,"J10") or V.rank()!=10 or (D.nrows(),D.ncols())!=(315,197):raise ValueError("same true V10 basis and197 columns")
 C=solve(V,D);oldC=block(pb,prep,"trueSevenCancellation")
 if oldC.nrows()!=7 or oldC.ncols()!=197:raise ValueError("actual first cancellation shape")
 if complete["sourceLabels"]!=prep["remaining197Labels"]:raise ValueError("same original source ordering")
 labels=complete["sourceLabels"]
 quotient={}
 source_labels=[{"family":"unscaled-old-high-kernel","originalHighIndex":i+2,"headLabel":labels[i]} for i in range(197)]
 for cut in (7,8,9):
  if not iszero(sub(J,range(cut,10),range(cut))):raise ValueError("paid U"+str(cut)+" invariance")
  JC=sub(J,range(cut,10),range(cut,10));CC=sub(C,range(cut,10),range(197))
  report,_=closed_image(JC,CC,source_labels);report["quotientCoordinatesInTrueSourceBasis"]=arr(CC)
  report["ambientDimension"]=10-cut;report["ambientAction"]=arr(JC)
  quotient["U"+str(cut)]=report
 # The newly allowed bare S2 source relation has first carry D; retain paid b8 explicitly.
 tail=sub(C,range(7,10),range(197));B8=nmod_mat(3,1,[1,0,0],P);combined=join(B8,tail)
 combined_labels=[{"family":"paid-eighth-source","sourceLabel":7003}]+source_labels
 related,BB=closed_image(sub(J,range(7,10),range(7,10)),combined,combined_labels)
 if not iszero(poly_action(sub(J,range(7,10),range(7,10)),combined,[4,27,1])):raise ValueError("actual (s-2)^2 bound in V10/U7")
 nonzero_tail=[{"originalHighIndex":i+2,"headLabel":labels[i],"b8b9b10":[int(C[k,i]) for k in (7,8,9)]} for i in range(197) if any(C[k,i] for k in (7,8,9))]
 result={"status":"completed","format":"r150-unscaled197-first-carry-true-source-space-v1",
  "author":"Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro",
  "actualSourceRun":43653360404,"actualSourceCommit":"4ee8d886cd88893411c91e6ef0b685a87f3e44f6",
  "inputs":inputs,"sourceLabels":labels,"sourceHighIndicesOneBased":list(range(2,199)),
  "all197ProjectedColumnsExpressedInTrueV10":True,"allActualSourceCoordinateIdentitiesVerified":True,
  "allQuotientActionsVerified":True,"higherIntegerProductsRecomputed":False,
  "fullOriginalS2HigherLiftComputed":False,"characteristicZeroIdentityAsserted":False,
  "rankProjected197":D.rank(),"trueV10Action":arr(J),"trueV10Coordinates":arr(C),
  "oldTrueSevenCancellation":arr(oldC),"quotients":quotient,
  "combinedImageWithPaidB8ModuloU7":related,"nonzeroB8B9B10Columns":nonzero_tail,
  "currentTargetQuotientWasNotUsedAsCompatibilityTest":True,
  "scope":"Exact readout of existing197 projected third columns. Bare unscaled S2 source first-carry interpretation uses the complete S2 source-envelope proof; no second or third Bockstein of that larger matrix is computed.",
  "elapsedSeconds":time.monotonic()-start}
 out=a.out/"unscaled197-first-carry-source-space-receipt.json";out.write_text(json.dumps(result,indent=2)+"\n")
 print(json.dumps({"status":"completed","all197ProjectedColumnsExpressedInTrueV10":True,"allActualSourceCoordinateIdentitiesVerified":True,
  "allQuotientActionsVerified":True,"rankProjected197":result["rankProjected197"],
  "modU7Dimension":quotient["U7"]["polynomialImageDimension"],"modU8Dimension":quotient["U8"]["polynomialImageDimension"],
  "modU9Dimension":quotient["U9"]["polynomialImageDimension"],"combinedB8ModuloU7Dimension":related["polynomialImageDimension"],
  "fullOriginalS2HigherLiftComputed":False,"elapsedSeconds":result["elapsedSeconds"]}),flush=True)
if __name__=="__main__":main()
