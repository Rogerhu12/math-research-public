#!/usr/bin/env python3
"""Construct the full ideal of Q2=2P_minus7+Z_minus8 in the actual 2L space."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def determinant_pair(A,p=47):
    n=len(A);M=[[(int(a)%p,int(b)%p) for a,b in row] for row in A]
    def mul(a,b):return ((a[0]*b[0]-a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    def inv(a):
        d=pow((a[0]*a[0]+a[1]*a[1])%p,-1,p)
        return a[0]*d%p,-a[1]*d%p
    det=(1,0)
    for k in range(n):
        j=next(j for j in range(k,n) if M[j][k]!=(0,0))
        if j!=k:M[k],M[j]=M[j],M[k];det=((-det[0])%p,(-det[1])%p)
        pivot=M[k][k];det=mul(det,pivot);iv=inv(pivot)
        for j in range(k+1,n):
            c=mul(M[j][k],iv)
            for l in range(k,n):
                v=mul(c,M[k][l]);M[j][l]=((M[j][l][0]-v[0])%p,(M[j][l][1]-v[1])%p)
    return list(det)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--cm7',type=Path,default=Path('/tmp/p41_cm7_q2_support47_verified.json.gz'))
    parser.add_argument('--cm8',type=Path,default=Path('/tmp/p41_cm8_q2_support47_verified.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_q2_ideal47_certificate.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_cm4_divisor47 import kernel
    from p41_formal47_multiply import write_checkpoint
    paths=[args.cm7,args.cm8,folder/'data/p41_makdisi47_certificate.json.gz',folder/'data/p41_cusp_divisors47_certificate.json.gz']
    raws=[p.read_bytes() for p in paths];cm7,cm8,model,divisors=[json.loads(gzip.decompress(b)) for b in raws]
    assert all('independent group-law' in d['status'] for d in [cm7,cm8])
    assert (cm7['CM_discriminant'],cm8['CM_discriminant'])==(-7,-8)
    W7=[r.from_json(A) for A in cm7['weight2_evaluation_coefficients']];W8=r.from_json(cm8['weight2_evaluation_coefficients'][0])
    pairs=divisors['square_basis_monomials_1based'];left=[a-1 for a,b in pairs];right=[b-1 for a,b in pairs]
    C2=r.from_json(divisors['square_basis_inverse'])
    def square(W):return r.mm(r.mul(r.cols(W,left),r.cols(W,right)),C2)
    V7=square(W7[0])
    D7=r.mm(r.add(r.mul(r.cols(W7[1],left),r.cols(W7[0],right)),r.mul(r.cols(W7[0],left),r.cols(W7[1],right))),C2)
    V8=square(W8);R=tuple(np.vstack([V7[i],D7[i],V8[i]]) for i in range(2))
    rr,cc=r.rank_pivots(R);assert len(rr)==22
    K,free,block=r.kernel_from_rows(r.rows(R,rr),rr,cc);assert K[0].shape==(199,177) and r.iszero(r.mm(R,K))
    minor=r.cols(r.rows(R,rr),cc);inverse=r.inverse_matrix(minor)
    W=r.from_json(model['evaluation_matrix']);V2=square(W);P2=[i-1 for i in divisors['square_pivot_rows_1based']]
    tau=[i-1 for i in model['frobenius_permutation_1based']];A2=r.rows(r.conjugate(r.rows(V2,tau)),P2)
    tauR=[0,1]+[i+1 for i in cm8['fixed_frobenius_permutation_1based']]
    assert r.equal(r.mm(R,A2),r.conjugate(r.rows(R,tauR)))
    K1=r.from_json(kernel(73,divisors['cusp_rank_columns_1based'],divisors['cusp_free_columns_1based'],divisors['canonical_kernel_block']))
    fc=r.mm(K1,r.column(divisors['canonical_coefficients']))
    canonical7=r.mm(W7[0],fc);canonical8=r.mm(W8,fc)
    # Independent projective separation of all twenty simple CM8 support points mod47.
    for j in range(20):
        a=r.rows(W8,[j]);pivot=next(k for k in range(73) if r.units(r.cols(a,[k]))[0,0])
        normalized=r.mul(a,r.inverse_values(r.cols(a,[pivot])))
        for k in range(j):
            b=r.rows(W8,[k])
            if r.units(r.cols(b,[pivot]))[0,0]:
                other=r.mul(b,r.inverse_values(r.cols(b,[pivot])))
                assert not all(np.array_equal(x%47,y%47) for x,y in zip(normalized,other))
    enc=lambda A:hashlib.sha256(json.dumps(r.to_json(A),separators=(',',':')).encode()).hexdigest()
    result={'level':41,'auxiliary_prime':47,'precision':4,
            'source_sha256':{p.name:hashlib.sha256(b).hexdigest() for p,b in zip(paths,raws)},
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'effective_divisor':'Q2=2 P_minus7 + Z_minus8','degree':22,'geometric_support_size':21,
            'ambient_space':'H0(2L), dimension199','complete_ideal_dimension':177,
            'restriction_row_order':'CM7 value, CM7 derivative in B-B0, twenty CM8 values in certificate order',
            'restriction_sha256':enc(R),'kernel_basis_sha256':enc(K),
            'restriction_rank_rows_1based':[i+1 for i in rr],'restriction_rank_columns_1based':[i+1 for i in cc],
            'restriction_unit_minor_mod47':determinant_pair(r.to_json(minor)),
            'restriction_unit_minor_inverse_mod47four':r.to_json(inverse),
            'kernel_free_columns_1based':[i+1 for i in free],
            'restriction_frobenius_permutation_1based':[i+1 for i in tauR],
            'fixed_canonical_CM7_value':r.to_json(canonical7),
            'fixed_canonical_CM8_values':r.to_json(canonical8),
            'fixed_canonical_nonunit_support_rows_1based':[i+1 for i,v in enumerate(r.units(canonical8)[:,0]) if not v],
            'status':'actual full degree22 Q2 ideal, unit22 minor, complete177-dimensional kernel and Frobenius descent PASS; all support/jet inputs independently verified'}
    digest,size=write_checkpoint(args.output,result)
    print('ACTUAL Q2 IDEAL PASS',size,digest,'minor',result['restriction_unit_minor_mod47'],
          'canonical bad rows',result['fixed_canonical_nonunit_support_rows_1based'],flush=True)
if __name__=='__main__':main()

