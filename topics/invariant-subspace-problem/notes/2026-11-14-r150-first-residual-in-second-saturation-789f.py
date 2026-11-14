#!/usr/bin/env python3
"""Full315 constant coordinates for the original h0 first residual in actual M:31^2 sources.

This tiny saved-data calculation does not compute a new VQ or original17 lift.
"""
from __future__ import annotations
import argparse, gzip, hashlib, json, struct, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
from flint import nmod_mat

INPUTS = {
 "global": ("all198", "global-check/selected-global315-reconciliation.bin.gz", "ab7b852301f1d495bef67b6322ca6bb54de17a62457a43bd2441177afd8e85f8"),
 "four": ("notes", "r150-four-second-bockstein-actions-789f/43615783424-1/four-second-bockstein-system.bin.gz", "57a5c3314281fd82cd4ba306b7d9c015a543b8aae05fd2713b50b303ca059f2d"),
 "first": ("notes", "r150-high-kernel-bockstein-actions-789f/43605503242-1/complete-infinite-quotient-system.bin.gz", "4a412dec33139ca7f41beb90a9a037e08ff9f2023a47f9e482f7c75ac3794449"),
 "state": ("notes", "2026-11-14-r150-torsion-state.bin-789f.gz", "5d86da2405f357c165d80d7fc2def5f419163b1e5d5a14bc9fa33fc05fafb60c"),
}

def sha(data): return hashlib.sha256(data).hexdigest()
def matrix(data, offset, rows, columns):
 block = data[offset:offset + rows * columns]
 if len(block) != rows * columns or any(v > 30 for v in block): raise ValueError("actual matrix dimensions/field")
 return nmod_mat([list(block[i*columns:(i+1)*columns]) for i in range(rows)], 31)
def join(*matrices):
 return nmod_mat([[int(M[i,j]) for M in matrices for j in range(M.ncols())] for i in range(matrices[0].nrows())],31)
def selected(M, rows, columns):
 return nmod_mat([[int(M[i,j]) for j in columns] for i in rows],31)
def serial(M): return bytes(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))

def main():
 parser=argparse.ArgumentParser()
 for name in ("notes-root","all198-recovery","out"): parser.add_argument("--"+name,type=Path,required=True)
 args=parser.parse_args();start=time.monotonic();args.out.mkdir(parents=True,exist_ok=True)
 scopes={"notes":args.notes_root,"all198":args.all198_recovery};inputs={};data={}
 for name,(scope,relative,expected) in INPUTS.items():
  path=scopes[scope]/relative;compressed=path.read_bytes()
  if sha(compressed)!=expected: raise ValueError("frozen actual input SHA "+name)
  data[name]=gzip.decompress(compressed)
  inputs[name]={"file":str(path),"compressedSHA256":expected,"uncompressedSHA256":sha(data[name]),"uncompressedBytes":len(data[name])}
 g,f,r,s=(data[name] for name in ("global","four","first","state"))
 if g[:8]!=b"R150GP31" or struct.unpack_from("<4I",g,8)!=(31,315,9,2): raise ValueError("actual selected global315 system")
 if f[:8]!=b"R150D2S1" or struct.unpack_from("<5I",f,8)!=(31,315,4,6,9): raise ValueError("actual four global315 system")
 if r[:8]!=b"R150BI31" or struct.unpack_from("<7I",r,8)!=(31,315,200,1152,9,2,6): raise ValueError("original h0 first residual system")
 if s[:8]!=b"R150FW31" or struct.unpack_from("<8I",s,8)[:7]!=(1034,8,820,13,315,9,505): raise ValueError("same whole torsion state")
 D=matrix(g,24,315,9);W=matrix(g,24+4*315*9,315,2)
 old=matrix(f,28+6*4,315,4)
 if W!=matrix(f,28+6*4+315*4,315,2): raise ValueError("same full first image basis")
 first_matrix_offset=36+200*16+1152*8
 first_image=matrix(r,first_matrix_offset,315,1152)
 if W!=selected(first_image,range(315),[1150,1151]): raise ValueError("beta199/beta200 actual source dictionary")
 R=matrix(r,first_matrix_offset+315*1152,315,9)
 J=matrix(s,40+820*3+13*2+820*820+13*820+9*820+315*820,315,315)
 U=join(W,old,D);reduced,rank=U.rref()
 pivots=[next(j for j in range(U.ncols()) if reduced[i,j]) for i in range(rank)]
 B=selected(U,range(315),pivots);transposed,rowrank=B.transpose().rref()
 rows=[next(j for j in range(315) if transposed[i,j]) for i in range(rowrank)]
 if rank!=7 or rowrank!=7: raise ValueError("actual seven-dimensional source span changed")
 inverse=selected(B,rows,range(rank)).inv()
 F=inverse*selected(R,rows,range(9))
 JB=inverse*selected(J*B,rows,range(rank))
 if B*F!=R or B*JB!=J*B: raise ValueError("full315 constant reconstruction or J invariance failed")
 Id=nmod_mat([[int(i==j) for j in range(rank)] for i in range(rank)],31)
 if JB*JB-3*JB+2*Id!=nmod_mat(rank,rank,31): raise ValueError("actual seven-source image not killed by ell")
 C=nmod_mat(15,9,31)
 for i,pivot in enumerate(pivots):
  for j in range(9): C[pivot,j]=F[i,j]
 if U*C!=R: raise ValueError("all15 genuine source coordinates must give all315 original residual coordinates")
 descriptors=[{"family":"first-beta","label":199,"sourceCost":85,"divisionBy31Power":1},
              {"family":"first-beta","label":200,"sourceCost":85,"divisionBy31Power":1}]
 descriptors += [{"family":"old-second","label":label,"sourceCost":cost,"divisionBy31Power":2}
                 for label,cost in zip([4001,4002,4003,4004],[86,86,86,87])]
 descriptors += [{"family":"selected-second","label":j,"sourceCost":85,"divisionBy31Power":2} for j in range(2,11)]
 bound=max([85]+[descriptors[i]["sourceCost"] for i in range(15) if any(C[i,j] for j in range(9))])
 payload=bytearray(b"R150PHS1")+struct.pack("<5I",31,315,15,7,9)
 blocks={}
 for name,M in (("actualSources",U),("originalFirstResidual",R),("constantCoefficients",C),("selectedBasis",B),("basisCoefficients",F),("basisAction",JB)):
  block=serial(M);blocks[name]={"offset":len(payload),"rows":M.nrows(),"columns":M.ncols(),"sha256":sha(block)};payload.extend(block)
 output=args.out/"first-residual-in-actual-second-saturation.bin.gz";output.write_bytes(gzip.compress(bytes(payload),mtime=0))
 result={"format":"r150-original-h0-first-residual-in-actual-second-saturation-v1","status":"completed","prime":31,
  "sourceSHA256":sha(Path(__file__).read_bytes()),"inputs":inputs,
  "actualGlobalSourceRank":rank,"augmentedOriginalFirstResidualRank":join(U,R).rank(),"full315JInvarianceVerified":True,
  "complete315ConstantIdentityVerified":True,"usesPrimaryProjection":False,
  "basisSourceIndicesOneBased":[i+1 for i in pivots],"basisPivotRowsOneBased":[i+1 for i in rows],
  "actualSourceDescriptors":descriptors,"constantCoefficientMatrix15By9":[[int(C[i,j]) for j in range(9)] for i in range(15)],
  "selectedBasisCoefficientMatrix7By9":[[int(F[i,j]) for j in range(9)] for i in range(7)],
  "everyFull315ResidualZero":True,"rightHandSideCostBound":bound,"constructiveSourceCostBound":bound+96,
  "candidateOriginalTarget":"31*h0*T modulo29791","candidatePrimitiveSourceFormula":"31*x0 +31*kappa*f + K2*g +961*z",
  "newVQComputed":False,"fullOriginalTarget31h0Mod29791IdentityNumericallyVerified":False,
  "characteristicZeroIdentityAsserted":False,"newHighPrecisionOrKernelRunPerformed":False,
  "matrices":blocks,"system":{"file":output.name,"bytes":len(payload),"sha256":sha(payload),"compressedBytes":output.stat().st_size,"compressedSHA256":sha(output.read_bytes())},
  "elapsedSeconds":time.monotonic()-start}
 (args.out/"first-residual-in-actual-second-saturation-receipt.json").write_text(json.dumps(result,indent=2)+"\n")
 print(json.dumps({k:result[k] for k in ("status","actualGlobalSourceRank","augmentedOriginalFirstResidualRank","complete315ConstantIdentityVerified","basisSourceIndicesOneBased","rightHandSideCostBound","constructiveSourceCostBound","elapsedSeconds")}),flush=True)
if __name__=="__main__": main()
