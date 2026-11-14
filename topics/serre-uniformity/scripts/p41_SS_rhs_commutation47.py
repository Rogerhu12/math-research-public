#!/usr/bin/env python3
"""Verify every T2/T3 compatibility equation of the actual SS Abel RHS."""
import argparse,gzip,hashlib,json
from pathlib import Path
import numpy as np


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--graph',type=Path,required=True);p.add_argument('--rhs',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    g=json.load(gzip.open(args.graph,'rt'));d=json.load(gzip.open(args.rhs,'rt'));q=47**3
    A2=np.asarray(g['adjacency']['2']);A3=np.asarray(g['adjacency']['3'])
    M2=np.asarray(d['multiplication_matrices']['2'],dtype=np.int64);M3=np.asarray(d['multiplication_matrices']['3'],dtype=np.int64)
    assert not np.any((M2@M3-M3@M2)%q)
    Y2=np.asarray(d['rhs']['2'],dtype=np.int64);Y3=np.asarray(d['rhs']['3'],dtype=np.int64)
    for i in range(2):
        r=(Y3[:,:,i][A2].sum(axis=1)-Y3[:,:,i]@M2-Y2[:,:,i][A3].sum(axis=1)+Y2[:,:,i]@M3)%q
        assert not np.any(r)
    x={'all3154_by54_R2_Hecke_RHS_commutation_equations':True,'modulus':q,
       'formula':'A2*Y3-Y3*M2-A3*Y2+Y2*M3=0',
       'input_sha256':{z.name:hashlib.sha256(z.read_bytes()).hexdigest() for z in [args.graph,args.rhs]}}
    args.output.write_text(json.dumps(x,indent=2)+'\n')
    print('PASS all3154x54 complex RHS commutation equations',flush=True)


if __name__=='__main__':main()
