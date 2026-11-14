#!/usr/bin/env python3
"""Exact mod47 norms of T47 and T47+-48 in all8 actual Hecke fields."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path
from p41_global_qc_polynomials47 import Field


def determinant(M):
    A=[[x%47 for x in row] for row in M];value=1
    for c in range(len(A)):
        pivot=next((i for i in range(c,len(A)) if A[i][c]),None)
        if pivot is None:return 0
        if pivot!=c:A[pivot],A[c]=A[c],A[pivot];value=-value
        x=A[c][c];value=value*x%47;A[c]=[z*pow(x,-1,47)%47 for z in A[c]]
        for i in range(c+1,len(A)):
            x=A[i][c];A[i]=[(z-x*w)%47 for z,w in zip(A[i],A[c])]
    return value%47


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--full-certificate',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();raw=args.full_certificate.read_bytes();full=json.loads(gzip.decompress(raw))
    k=[m['n'] for m in full['row_metadata']].index(47);records=[]
    for i,ff in enumerate(full['fields'],1):
        F=Field(ff['factor_descending']);T=F.val(ff['directions'][k][0]);out={}
        for shift in [-48,0,48]:
            t=F.add(T,[shift]);out[str(shift)]=determinant([F.mul(t,[0]*j+[1]) for j in range(F.d)])
            assert out[str(shift)]
        records.append({'field':i,'degree':F.d,'det_T47_plus_shift_mod47':out})
    x={'fields':records,'all24_norms_nonzero_mod47':True,
       'status':'Actual norms are units; invertibility of a chosen SS Sylvester combination is a separate computation',
       'input_sha256':{args.full_certificate.name:hashlib.sha256(raw).hexdigest()},
       'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(x,indent=2)+'\n');print('PASS all24 actual field norms nonzero mod47',flush=True)


if __name__=='__main__':main()
