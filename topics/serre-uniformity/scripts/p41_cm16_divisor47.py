#!/usr/bin/env python3
"""Actual B_minus16, T2 B_minus4 and the exact principal transport between divisors."""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--cm16',type=Path,default=Path('/tmp/p41_cm16_hecke47_verified.json.gz'))
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_cm16_divisor47_checkpoint.json.gz'))
    args=p.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model,replay_negative
    from p41_cm4_divisor47 import kernel
    from p41_hecke3_hessian47 import section_jets
    from p41_poincare_miller47 import addflip_with_section
    from p41_formal47_multiply import write_checkpoint,point_hash
    sources,hashes=load_sources(folder/'data');M=make_model(sources);d=sources[1]
    raw=args.cm16.read_bytes();cm16=json.loads(gzip.decompress(raw));assert 'independent' in cm16['status']
    W=r.from_json(cm16['weight2_values']);V2,_=section_jets([W],sources,M,r);V2=V2[0]
    K1=r.from_json(kernel(73,d['cusp_rank_columns_1based'],d['cusp_free_columns_1based'],d['canonical_kernel_block']))
    fc=r.mm(K1,r.column(d['canonical_coefficients']));fval=r.mm(W,fc)
    assert np.all(r.units(fval)),'The actual canonical divisor meets CM16; change the canonical divisor explicitly'
    KI=r.from_json(kernel(199,d['K_rank_columns_1based'],d['K_free_columns_1based'],d['K_kernel_block']))
    restriction=r.mm(V2,KI);rr,cc=r.rank_pivots(restriction);assert len(rr)==20
    ker,free,block=r.kernel_from_rows(r.rows(restriction,rr),rr,cc)
    B16=r.mm(KI,ker);B16,brows,bcols,change=r.normalize(B16,73)
    A16=r.rows(r.mm(M['A2'],r.conjugate(B16)),brows)
    assert r.equal(r.mm(B16,A16),r.mm(M['A2'],r.conjugate(B16))) and r.equal(r.mm(A16,r.conjugate(A16)),r.eye(73))
    assert r.iszero(r.mm(V2,B16))
    tau=[j-1 for j in cm16['target_frobenius_permutation_1based']]
    assert r.equal(r.mm(V2,M['A2']),r.conjugate(r.rows(V2,tau)))
    neg,Aneg=replay_negative(M,sources[3]);rng=random.Random(4104716501)
    minus2,Aminus2,fd,rd=addflip_with_section(B16,A16,B16,A16,M,rng,'CM16 negative double',r,same=True)
    T2B,AT2,fa,ra=addflip_with_section(neg,Aneg,minus2,Aminus2,M,rng,'Actual T2 B4 via B4 plus2B16',r)
    qcoeff=r.mm(M['B'],r.column(sources[3]['negative_flip_section_seeds_and_coefficients'][0][1]))
    transport={'numerator_cubic_coefficients':r.to_json(fa),'denominator_cubic_coefficients':r.to_json(fd),
               'denominator_quadratic_coefficients':r.to_json(qcoeff),'base_linear_coefficients':r.to_json(fc),
               'actual_function':'(fa/f0^3)/((fd/f0^3)*(qB/f0^2)) = fa*f0^2/(fd*qB)',
               'actual_divisor':'A_T2B - T2(A_B4) = A_T2B - A_B4 - 2*A_B16'}
    result={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
            'CM16_source_sha256':hashlib.sha256(raw).hexdigest(),
            'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'B16_point_coordinates':r.to_json(B16),'B16_point_frobenius':r.to_json(A16),'B16_point_sha256':point_hash(B16,A16),
            'restriction_rank':20,'restriction_rank_columns_1based':[j+1 for j in cc],
            'restriction_kernel_block_sha256':hashlib.sha256(json.dumps(r.to_json(block),separators=(',',':')).encode()).hexdigest(),
            'canonical_values_on_CM16':r.to_json(fval),'double_record':rd,'add_record':ra,
            'negative2_B16_point_sha256':point_hash(minus2,Aminus2),
            'T2B_point_coordinates':r.to_json(T2B),'T2B_point_frobenius':r.to_json(AT2),'T2B_point_sha256':point_hash(T2B,AT2),
            'principal_transport':transport,
            'status':'actual full CM16 divisor ideal, exact T2B=B4+2B16 and retained principal transport; not a local-height value'}
    sha,size=write_checkpoint(args.output,result)
    print('ACTUAL CM16 DIVISOR AND T2B PASS',point_hash(B16,A16),point_hash(T2B,AT2),'bytes',size,'sha',sha,flush=True)

if __name__=='__main__':main()

