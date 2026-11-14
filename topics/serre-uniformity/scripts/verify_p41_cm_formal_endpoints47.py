#!/usr/bin/env python3
"""Independent integer determinant and a non-scalar-square witness for R167."""
import argparse,gzip,hashlib,json
from pathlib import Path
from flint import fmpz_mat

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,default=Path(__file__).with_name('data')/'p41_cm_formal_endpoints47_checkpoint.json.gz')
    ap.add_argument('--output',type=Path,default=Path('/tmp/p41_cm_formal_endpoints47_independent.json'))
    args=ap.parse_args();raw=args.input.read_bytes();d=json.loads(gzip.decompress(raw));N=d['H47_differential_matrix'];Q=47**4;n=54
    A=[[int(v[0]) for v in row] for row in N];B=[[int(v[1]) for v in row] for row in N]
    block=[A[i]+[-x for x in B[i]] for i in range(n)]+[B[i]+A[i] for i in range(n)]
    z=int(fmpz_mat(block).det())%Q;assert z==pow(d['target_multiplier'],2,Q)
    witness=None
    for i in range(n):
        for j in range(n):
            if i==j:continue
            re=sum(A[i][k]*A[k][j]-B[i][k]*B[k][j] for k in range(n))%47
            im=sum(A[i][k]*B[k][j]+B[i][k]*A[k][j] for k in range(n))%47
            if re or im:
                witness={'row_1based':i+1,'column_1based':j+1,'H47_squared_entry_mod47':[re,im]};break
        if witness:break
    assert witness
    out={'source_sha256':hashlib.sha256(raw).hexdigest(),
         'verification_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'independent_algorithm':'FLINT exact integer determinant of108x108 real block; only reduce after determinant',
         'real_block_determinant_mod47_4':z,'expected_square_of_m_mod47_4':pow(d['target_multiplier'],2,Q),
         'non_scalar_square_witness':witness,'status':'PASS'}
    args.output.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');print(json.dumps(out),flush=True)

if __name__=='__main__':main()
