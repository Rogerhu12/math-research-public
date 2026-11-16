#!/usr/bin/env python3
"""Independent original point-matrix audit using symmetric quadratic forms.
Author: ChatGPT (AI), root. Date: 2026-11-16.
The producer's polynomial core, compression routine and elimination are not
imported. All original projected rows are rebuilt from the primitive equations.
Mathematical arrays are temporary only.
"""
import argparse,gzip,hashlib,itertools,json,math,time
from pathlib import Path
from flint import nmod_mat
P=127;S=63
PRIMITIVE=(65159,'44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe')
DECODED=(158741,'fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3')
DATA=(125275,'0795447edab5684100db0d3b82a08446b2059737a5a4c8ba8a55b204642114ad')
RECEIPT=(3208,'041d65424636c7db5539bc7b0b3b1b4003642f07e82af55266505ea4edf3de2b')
def require(c,m):
 if not c:raise ValueError(m)
def canonical(x):return (json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True)+'\n').encode()
def identity(p):
 b=p.read_bytes();return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def pin(p,expected):
 b=p.read_bytes();require((len(b),hashlib.sha256(b).hexdigest())==expected,'entire input '+str(p));return b
def value(c):
 a=0
 for z in reversed(c):a=(a*S+int(z))%P
 return a
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--primitive',type=Path,required=True);ap.add_argument('--completed-dir',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();start=time.monotonic()
 primitive=gzip.decompress(pin(a.primitive,PRIMITIVE));require((len(primitive),hashlib.sha256(primitive).hexdigest())==DECODED,'whole decoded primitive')
 equations=json.loads(primitive)['equations'];require(len(equations)==17 and all(len(r)==77 for r in equations),'all original ordinary coefficients')
 dp=a.completed_dir/'original-whole-w127-root63-point-data.json';rp=a.completed_dir/'original-whole-w127-root63-projection-receipt.json'
 d=json.loads(pin(dp,DATA));r=json.loads(pin(rp,RECEIPT))
 binding=hashlib.sha256(canonical(r['parameters']['bindingObject'])).hexdigest();require(binding==r['binding']==d['binding'],'entire semantic binding')
 T=nmod_mat([[math.comb(i,j)*pow(S,i-j,P)%P if i>=j else 0 for j in range(11)] for i in range(11)],P)
 require(int(T.det())==1,'full original unipotent coordinate change')
 # Ordinary off-diagonal coefficients become half entries of a symmetric
 # form, so T^t Q T independently performs the entire quadratic substitution.
 pairs=list(itertools.combinations_with_replacement(range(11),2));half=pow(2,-1,P);fields=[]
 for row in equations:
  z=[value(c) for c in row];L=nmod_mat([z[:11]],P)*T;Q=[[0]*11 for _ in range(11)]
  for (i,j),c in zip(pairs,z[11:]):
   Q[i][j]=c if i==j else c*half%P;Q[j][i]=Q[i][j]
  B=T.transpose()*nmod_mat(Q,P)*T
  f={(i,):int(L[0,i]) for i in range(11) if L[0,i]}
  for i,j in pairs:
   c=int(B[i,j])*(1 if i==j else 2)%P
   if c:f[(i,j)]=c
  fields.append(f)
 pc=[tuple([0]*i+[1]*(n-i)) for n in range(1,6) for i in range(n+1)]
 nc=[tuple([0]*i+[1]*(n-i)+[j]) for n in range(5) for i in range(n+1) for j in range(2,11)]
 targets=pc+nc;ti={m:i for i,m in enumerate(targets)}
 require(len(targets)==155 and hashlib.sha256(canonical(targets)).hexdigest()==d['originalProjectedTargetDictionaryLogicalSha256'],'entire original projected dictionary')
 mon=[m for n in range(4) for m in itertools.combinations_with_replacement(range(11),n)];rows=[];labels=[]
 for eq,f in enumerate(fields):
  for m in mon:
   v=[0]*155
   for n,c in f.items():
    j=ti.get(tuple(sorted(m+n)))
    if j is not None:v[j]=(v[j]+c)%P
   rows.append(v);labels.append([eq,list(m)])
 require(len(rows)==6188,'all original source rows')
 full_sha=hashlib.sha256(canonical(rows)).hexdigest();require(full_sha==d['full6188By155LogicalSha256']==r['parameters']['full6188By155LogicalSha256'],'all original projected matrix coefficients')
 require(hashlib.sha256(canonical(labels)).hexdigest()==d['originalSourceDictionaryLogicalSha256'],'entire original source dictionary')
 A=nmod_mat(rows,P);K=nmod_mat(d['completePointKernel155'],P);C=nmod_mat(d['compressed224'],P)
 require(A.rank()==C.rank()==142 and K.rank()==13,'independent FLINT full ranks')
 require(not any(A*K) and not any(C*K),'every full and compressed kernel product')
 ri=d['originalSourceRowProfile'];ci=d['projectedTargetColumnProfile'];minor=[[rows[i][j] for j in ci] for i in ri]
 require(minor==d['originalUnitMinor'] and int(nmod_mat(minor,P).det())==97,'actual original unit minor reconstructed and determinant checked')
 result={'format':'r150-root-independent-whole-w127-quadratic-form-audit-v1','status':'completed','source':identity(Path(__file__)),'primitive':identity(a.primitive),'receipt':identity(rp),'completePointData':identity(dp),'binding':binding,'method':'original-symmetric-quadratic-congruence-and-FLINT-full-matrix-rank','all6188OriginalRowsReconstructed':True,'allOriginalDictionaryAndCoefficientHashesVerified':True,'fullProjectionRank':142,'compressedProjectionRank':142,'completeKernelDimension':13,'allOriginalKernelProductsZero':True,'originalMinorSize':142,'originalMinorDeterminant':97,'mathematicalArraysTemporaryOnly':True,'elapsedSeconds':time.monotonic()-start}
 a.out.write_bytes(canonical(result));print(canonical(result).decode(),end='')
if __name__=='__main__':main()
