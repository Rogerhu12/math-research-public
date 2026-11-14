#!/usr/bin/env python3
"""Small final certificate for two actual inverse Abel charts and their value at Y."""
import argparse,gzip,hashlib,json,sys
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--work-dir',type=Path,default=Path('/tmp'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_formal47_exponential_compact.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import p41_r2_matrix as r
    from p41_cm4_divisor47 import kernel
    from p41_poincare_norms47 import determinant
    from p41_formal47_multiply import point_hash,write_checkpoint
    names=['p41_formal47_abel_jets_checkpoint.json.gz','p41_formal47_abel_bases_checkpoint.json.gz',
           'p41_formal47_exponential_checkpoint.json.gz','p41_formal47_exponential_comparison.json.gz']
    raws=[(args.work_dir/name).read_bytes() for name in names]
    jets,base,exp,comparison=[json.loads(gzip.decompress(raw)) for raw in raws]
    assert comparison['exponential_sha256']==hashlib.sha256(raws[2]).hexdigest()
    assert exp['bases_sha256']==hashlib.sha256(raws[1]).hexdigest()
    assert exp['jets_sha256']==hashlib.sha256(raws[0]).hexdigest()
    model=json.loads(gzip.decompress((folder/'data/p41_makdisi47_certificate.json.gz').read_bytes()))
    divs=json.loads(gzip.decompress((folder/'data/p41_cusp_divisors47_certificate.json.gz').read_bytes()))
    K=r.from_json(kernel(73,divs['cusp_rank_columns_1based'],divs['cusp_free_columns_1based'],divs['canonical_kernel_block']))
    W=r.from_json(model['evaluation_matrix']);A=r.from_json(model['frobenius_basis_matrix'])
    records=[];beta0=-3*pow(27652,-1,r.Q)%r.Q
    for j,(rec,point) in enumerate(zip(base['families'],exp['exponentials'])):
        indices=[i-1 for i in rec['points_1based']];tangent=r.mm(r.rows(W,indices),K)
        canonical=determinant(tangent);actual=determinant(tuple(a*beta0%r.Q for a in tangent))
        assert canonical is not None and actual is not None
        for name in ['v_coefficients','g_coefficients']:
            coef=r.from_json(rec[name]);assert r.equal(r.mm(A,r.conjugate(coef)),coef)
        records.append({'points_1based':rec['points_1based'],
                        'canonical_evaluation_determinant':canonical,
                        'actual_abel_tangent_determinant':actual,
                        'v_coefficients':rec['v_coefficients'],'g_coefficients':rec['g_coefficients'],
                        'v_seed':rec['v_seed'],'g_seed':rec['g_seed'],
                        'parameters_at_published_Y':point['parameters'],
                        'actual_point_sha256':point_hash(r.from_json(point['point_coordinates']),r.from_json(point['point_frobenius']))})
    records[1]['disjointness_determinant']=base['families'][1]['disjointness_determinant']
    sources=['p41_formal47_abel_jets.gp','p41_formal47_abel_jets.py','p41_formal47_exponential.py',
             'verify_p41_formal47_exponential.py','p41_formal47_exponential_compact.py']
    out={'level':41,'auxiliary_prime':47,'precision':4,'modulus':r.Q,
         'source_sha256':exp['source_sha256'],
         'raw_data_sha256':{name:hashlib.sha256(raw).hexdigest() for name,raw in zip(names,raws)},
         'generating_source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in sources},
         'published_log_sha256':exp['log_sha256'],'published_Y_sha256':comparison['long_multiple_sha256'],
         'published_Y_point_sha256':comparison['long_multiple_point_sha256'],
         'families':records,
         'status':'both actual Galois-stable inverse Abel charts agree in all820x73 Picard coordinates with the published304-bit long multiple; generic exponentials use the same integral inverse chart'}
    digest,size=write_checkpoint(args.output,out)
    print('Final small exponential certificate',size,digest,flush=True)
    print('Actual Abel tangent determinants',[item['actual_abel_tangent_determinant'] for item in records],flush=True)
    print('Disjointness unit',records[1]['disjointness_determinant'],flush=True)

if __name__=='__main__':main()
