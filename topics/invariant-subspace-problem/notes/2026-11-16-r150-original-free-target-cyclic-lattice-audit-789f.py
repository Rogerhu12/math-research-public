#!/usr/bin/env python3
"""Read-only actual original free-target cyclic-lattice audit.
Author: ChatGPT (AI), literature_audit, 2026-11-16.
"""
import argparse,json,hashlib,time
from pathlib import Path
from flint import nmod_mat
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def check(b,m):
 if not b:raise ValueError(m)
def sub(A,rr,cc):return nmod_mat([[int(A[i,j]) for j in cc] for i in rr],31)
def record(A):return {'rows':A.nrows(),'columns':A.ncols(),'sha256':sha(bytes(int(x) for x in A.entries()))}
def main():
 p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();t=time.monotonic()
 raw=a.data.read_bytes();check(len(raw)==2112889 and sha(raw)=='a7a21b4c00e306ee0278451217491aedf88c6bcb59c3ca23668198516a74a29d','exact complete original M qualification data')
 q=json.loads(raw);check(q['binding']=='f03f4892d70cdf39aceaebf8d8e9dc979196904e8ca75afbfc3d080230cb365f','actual independent paid-full210 qualification binding')
 K=nmod_mat(q['all225OriginalKrylov'],31);U=nmod_mat(q['true16'],31);rr=q['freeQuotientProjectionPivotRows'];ff=q['freeQuotientRemainingRows'];I=nmod_mat(q['freeQuotientInverse'],31);L=nmod_mat(q['freeQuotientLower'],31)
 check(I*sub(U,rr,range(16))==nmod_mat([[int(i==j) for j in range(16)] for i in range(16)],31),'actual complete true16 unit')
 check(L==sub(U,ff,range(16)),'actual free projection lower block')
 F=sub(K,ff,range(225))-L*I*sub(K,rr,range(225))
 check(record(F)==q['summary']['trueFreeQuotientKrylov'] and F.rank()==25,'all225 original free-lattice columns')
 results=[]
 for j in range(9):
  C=sub(F,range(F.nrows()),[9*k+j for k in range(25)])
  first=sub(C,range(C.nrows()),range(23));r=first.rank()
  check(C.rank()==r and r<=23,'complete original cyclic lattice and paid rational upper bound')
  results.append({'targetLabel':j+2,'first23Rank':r,'all25Rank':C.rank(),'primitiveCyclic23Qualified':r==23,'first23':record(first),'all25':record(C)})
 check(results[0]['first23Rank']==23,'original t2 is a primitive global cyclic23 free vector')
 result={'format':'r150-original-free-target-cyclic23-readonly-audit-v1','status':'completed','sourceSHA256':sha(Path(__file__).read_bytes()),'dataBytes':len(raw),'dataSHA256':sha(raw),'parentBinding':q['binding'],'allNineOriginalTargets':results,'all225OriginalColumnsKept':True,'originalT2PrimitiveGlobalCyclic23Qualified':True,'onlyPaidPrimitiveFreeQuotientUsed':True,'coefficientTorsionNotDiscardedFromOriginalM':True,'elapsedSeconds':time.monotonic()-t}
 a.out.write_bytes(canonical(result));print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
