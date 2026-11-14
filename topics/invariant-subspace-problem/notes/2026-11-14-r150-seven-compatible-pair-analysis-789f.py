#!/usr/bin/env python3
"""Read only the saved complete seven-relation system; export exact eighth column and all nine raw annihilators."""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
from flint import nmod_mat
GLOBAL_SHA="7e461b35ac41e0bb0c76462c8c61c4a8ebf9d55ff3ea8fdd0560146ed8809420"
SYSTEM_SHA="8ad7a408081b1ae32a87c8c653212f74e9bec6b4ef25263e7d3b3b6d4234b647"
READER_SHA="8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2"
STATE_SHA="06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf"
def sha(b):return hashlib.sha256(b).hexdigest()
def sub(M,rows,cols):
 rows,cols=list(rows),list(cols);A=nmod_mat(len(rows),len(cols),31)
 for i,r in enumerate(rows):
  for j,c in enumerate(cols):A[i,j]=M[r,c]
 return A
def join(*matrices):return nmod_mat([[int(M[i,j]) for M in matrices for j in range(M.ncols())] for i in range(matrices[0].nrows())],31)
def pivots(M):
 R,r=M.rref();return [next(j for j in range(M.ncols()) if R[i,j]) for i in range(r)]
def serial(M):return bytes(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))
def annihilator(J,V):
 """First dependence of all matrix entries pays the complete vector/multitarget minimum."""
 basis={};current=V
 for degree in range(J.nrows()+1):
  x=[int(current[i,j]) for i in range(current.nrows()) for j in range(current.ncols())]
  relation=[0]*degree+[1]
  for row,(v,c) in sorted(basis.items()):
   if x[row]:
    factor=x[row];x=[(a-factor*b)%31 for a,b in zip(x,v)]
    for j,a in enumerate(c):relation[j]=(relation[j]-factor*a)%31
  pivot=next((i for i,a in enumerate(x) if a),None)
  if pivot is None:
   if relation[-1]!=1:raise ValueError("monic exact Krylov dependence")
   check=nmod_mat(V.nrows(),V.ncols(),31);power=V
   for a in relation:
    if a:check+=a*power
    power=J*power
   if check!=nmod_mat(V.nrows(),V.ncols(),31):raise ValueError("complete annihilator multiplyback")
   return relation
  scale=pow(x[pivot],-1,31)
  basis[pivot]=([(a*scale)%31 for a in x],[(a*scale)%31 for a in relation])
  current=J*current
 raise ValueError("finite full-action Krylov bound")
def main():
 p=argparse.ArgumentParser()
 for key in ("notes-root","receipt","system","out"):p.add_argument("--"+key,type=Path,required=True)
 a=p.parse_args();started=time.monotonic();a.out.mkdir(parents=True,exist_ok=True)
 text=a.receipt.read_bytes()
 if sha(text)!=GLOBAL_SHA:raise ValueError("actual complete global receipt")
 r=json.loads(text);data=gzip.decompress(a.system.read_bytes())
 if sha(data)!=SYSTEM_SHA or data[:8]!=b"R150S731" or struct.unpack_from("<8I",data,8)!=(31,315,7,308,16,14,1,9):raise ValueError("actual complete global binary")
 def block(name):
  m=r["matrices"][name];b=data[m["offset"]:m["offset"]+m["rows"]*m["columns"]]
  if sha(b)!=m["sha256"] or any(x>30 for x in b):raise ValueError("saved global matrix "+name)
  return nmod_mat([list(b[i*m["columns"]:(i+1)*m["columns"]]) for i in range(m["rows"])],31)
 U=block("oldSevenSources");J7=block("oldSevenAction");J308=block("quotientAction")
 D=block("actualAll315NewColumns");Q=block("actualQuotientColumns");K=block("full315Krylov")
 B=block("selectedImageBasis");action=block("selectedBasisAction");F=block("basisSolution");C=block("oldSevenConstantCorrection")
 if r["KrylovBasisColumnIndicesZeroBased"]!=[2] or action!=nmod_mat([[2]],31):raise ValueError("actual eighth source must be7003 with eigenvalue2")
 new=sub(D,range(315),range(7));target=sub(D,range(315),range(7,16))
 beta=sub(Q,range(308),range(7));raw308=sub(Q,range(308),range(7,16))
 pivot=pivots(B.transpose())[0];coeff=[int(beta[pivot,j])*pow(int(B[pivot,0]),-1,31)%31 for j in range(7)]
 if B*nmod_mat([coeff],31)!=beta or coeff[2]!=1:raise ValueError("all seven first-image coefficients")
 reader=a.notes_root/"2026-11-14-r150-torsion-characteristic-789f.py"
 if sha(reader.read_bytes())!=READER_SHA:raise ValueError("same torsion reader")
 state=gzip.decompress((a.notes_root/"2026-11-14-r150-torsion-state.bin-789f.gz").read_bytes())
 if sha(state)!=STATE_SHA:raise ValueError("same full315 state")
 path=a.out/"same-state-input.bin";path.write_bytes(state)
 spec=importlib.util.spec_from_file_location("r150_pair_actual_state",reader);helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
 saved=helper.load_state(path);path.unlink();J=nmod_mat(saved["matrices"]["action"],31)
 if J*U!=U*J7 or J*new!=sub(K,range(315),range(7,14)):raise ValueError("actual315 action and stored full Krylov")
 eighth=sub(new,range(315),[2]);U8=join(U,eighth)
 rows=pivots(U8.transpose());inverse=sub(U8,rows,range(8)).inv();J8=inverse*sub(J*U8,rows,range(8))
 if len(rows)!=8 or U8*J8!=J*U8:raise ValueError("complete eighth invariant submodule")
 free=[i for i in range(315) if i not in set(rows)];Uf=sub(U8,free,range(8))
 def project(M):return sub(M,free,range(M.ncols()))-Uf*inverse*sub(M,rows,range(M.ncols()))
 J307=sub(J,free,free)-Uf*inverse*sub(J,rows,free);raw307=project(target)
 flags=[all(not raw307[i,j] for i in range(307)) for j in range(9)]
 if flags!=[False,False,False,False,True,False,False,True,False]:raise ValueError("all actual individual flags")
 rawcounts=[sum(bool(raw308[i,j]) for i in range(308)) for j in range(9)]
 if not all(rawcounts):raise ValueError("all nine fixed unit-family residuals must really be nonzero")
 individual315=[annihilator(J,sub(target,range(315),[j])) for j in range(9)]
 individual308=[annihilator(J308,sub(raw308,range(308),[j])) for j in range(9)]
 individual307=[annihilator(J307,sub(raw307,range(307),[j])) for j in range(9)]
 common315=annihilator(J,target);common308=annihilator(J308,raw308);common307=annihilator(J307,raw307)
 # A basis of the seven new relation-kernel, in unchanged theta1..theta7 coordinates.
 theta_kernel=[]
 for j in range(7):
  col=[[] for _ in range(7)]
  if j==2:col[2]=[-2,1]
  else:col[j]=[1];col[2]=[-coeff[j]] if coeff[j] else []
  theta_kernel.append(col)
 result={"format":"r150-actual-eighth-source-and-nine-raw-annihilators-v1","status":"completed",
  "sourceRun":43630666145,"allDataFromSavedGlobalSystem":True,"whole315CoordinatesUsed":True,
  "eighthRelationLabel":7003,"eighthOriginalSourceCost":87,"eighthOriginalDivisor":29791,
  "newImageEigenvalue":2,"sevenFirstImageCoefficients":coeff,
  "J8":[[int(J8[i,j]) for j in range(8)] for i in range(8)],
  "eighthRelationOldSevenCorrection":[int(J8[i,7]) for i in range(7)],
  "kernelOfNewFirstImageColumnsAscending":theta_kernel,
  "actualNineRawNonzeroCountsModuloU":rawcounts,"allNineRawNonzeroModuloU":True,
  "individualCompatibleAfterWholeFirstImage":flags,
  "allNineExcludedFromFixedInfiniteUnitFamily":True,
  "originalA87CharacteristicZeroRankLowerBound":226090,
  "exactThirdSmithValuationClaimed":False,
  "individualRawAnnihilatorsEntire315Ascending":individual315,
  "individualRawAnnihilatorsModuloUAscending":individual308,
  "individualRawAnnihilatorsModuloU8Ascending":individual307,
  "commonRawAnnihilatorEntire315Ascending":common315,
  "commonRawAnnihilatorModuloUAscending":common308,
  "commonRawAnnihilatorModuloU8Ascending":common307,
  "rawTargetRankModuloU":raw308.rank(),"rawTargetRankModuloU8":raw307.rank(),
  "fullInitialFreedomComputed":False,"newSecondBocksteinComputed":False,
  "positiveTargetsStillRequireFullOriginalProduct":[6,9],"elapsedSeconds":time.monotonic()-started}
 payload=bytearray(b"R150E831")+struct.pack("<4I",31,315,8,9);blocks={}
 for name,M in [("U8",U8),("J8",J8),("whole315RawTargets",target),("quotient307Action",J307),("quotient307RawTargets",raw307),("sevenFirstImageCoefficients",nmod_mat([coeff],31))]:
  b=serial(M);blocks[name]={"offset":len(payload),"rows":M.nrows(),"columns":M.ncols(),"sha256":sha(b)};payload.extend(b)
 targetpath=a.out/"eighth-and-raw-annihilators.bin.gz";targetpath.write_bytes(gzip.compress(payload,mtime=0))
 result["matrices"]=blocks;result["system"]={"file":targetpath.name,"uncompressedBytes":len(payload),"uncompressedSHA256":sha(payload),"compressedBytes":targetpath.stat().st_size,"compressedSHA256":sha(targetpath.read_bytes())}
 (a.out/"eighth-and-raw-annihilators-receipt.json").write_text(json.dumps(result,indent=2)+"\n")
 print(json.dumps({"status":"completed","allNineRawNonzeroModuloU":True,"newImageEigenvalue":2,"rawTargetRankModuloU8":result["rawTargetRankModuloU8"],"elapsedSeconds":result["elapsedSeconds"]}),flush=True)
if __name__=="__main__":main()
