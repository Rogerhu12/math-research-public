#!/usr/bin/env python3
"""Compare two actual inverse Abel constructions with the published long multiple."""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path

def move_away(K,A,points,M,derivative,r,rng):
    """An actual residual flip using766 evaluations when E meets the fixed pool."""
    import numpy as np
    S=r.mm(M['V2'],K);remaining=[i for i in range(820) if i not in set(points)]
    small,piv,cols,C=r.normalize(r.rows(M['V2'],remaining),199);assert cols==list(range(199))
    # The derivative of an actual V2 section follows the published quadratic basis.
    model_divs=M['_divs'];pairs=[(a-1,b-1) for a,b in model_divs['square_basis_monomials_1based']]
    dproducts=r.add(r.mul(r.cols(derivative,[a for a,b in pairs]),r.cols(M['W'],[b for a,b in pairs])),
                    r.mul(r.cols(M['W'],[a for a,b in pairs]),r.cols(derivative,[b for a,b in pairs])))
    dV2=r.mm(dproducts,r.from_json(model_divs['square_basis_inverse']));dS=r.mm(r.rows(dV2,points),K)
    for attempt in range(1,101):
        fs,fc=r.rational_trace(A,rng);f=r.mm(S,fc)
        if not np.all(r.units(r.rows(f,remaining))) or not np.all(r.units(r.mm(dS,fc))):continue
        gs,gc=r.rational_trace(A,rng);g=r.mm(S,gc)
        scaled=r.mul(r.mul(r.rows(g,remaining),r.inverse_values(r.rows(f,remaining))),small)
        residual=r.sub(scaled,r.mm(small,r.rows(scaled,piv)));rr,cc=r.rank_pivots(residual)
        if len(rr)!=126:continue
        out,free,block=r.kernel_from_rows(r.rows(residual,rr),rr,cc);assert r.iszero(r.mm(residual,out))
        out=r.mm(C,out);out,opiv,ocols,_=r.normalize(out,73);assert ocols==list(range(73))
        OA=r.rows(r.mm(M['A2'],r.conjugate(out)),opiv)
        assert r.equal(r.mm(out,OA),r.mm(M['A2'],r.conjugate(out)))
        assert r.equal(r.mm(OA,r.conjugate(OA)),r.eye(73))
        values=r.mm(M['V2'],out);assert np.all(np.any(r.units(values),axis=1))
        record={'excluded_points_1based':[i+1 for i in points],
                'restricted_pivot_rows_1based':[i+1 for i in piv],'restricted_basis_inverse':r.to_json(C),
                'f_seed':r.to_json(fs),'f_coefficients':r.to_json(fc),
                'g_seed':r.to_json(gs),'g_coefficients':r.to_json(gc),
                'rank_rows_1based':[i+1 for i in rr],'rank_columns_1based':[i+1 for i in cc],
                'kernel_block':r.to_json(block),'coordinate_pivot_rows_1based':[i+1 for i in opiv]}
        return out,OA,record
    raise RuntimeError('Unable to move actual divisor away from the820 evaluation points')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--exponential',type=Path,default=Path('/tmp/p41_formal47_exponential_checkpoint.json.gz'))
    parser.add_argument('--output',type=Path,default=Path('/tmp/p41_formal47_exponential_comparison.json.gz'))
    args=parser.parse_args();folder=args.script_dir.resolve();sys.path.insert(0,str(folder))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model,flip
    from p41_formal47_chart import make_chart,evaluate_chart,chart_record
    from p41_formal47_multiply import point_hash,write_checkpoint
    sources,hashes=load_sources(folder/'data');M=make_model(sources);M['_divs']=sources[1];chart=make_chart(M,sources[0])
    derivative=r.from_json(json.loads(gzip.decompress((folder/'data/p41_evaluation_jets47_checkpoint.json.gz').read_bytes()))['evaluation_derivatives'])
    base=json.loads(gzip.decompress(Path('/tmp/p41_formal47_abel_bases_checkpoint.json.gz').read_bytes()))
    eraw=args.exponential.read_bytes();exp=json.loads(gzip.decompress(eraw));assert exp['source_sha256']==hashes
    pr=(folder/'data/p41_formal47_multiplication_saved.json.gz').read_bytes();p=json.loads(gzip.decompress(pr));assert p['source_sha256']==hashes
    assert p['bits_done']==304 and p['sign']==1
    rng=random.Random(4104713403);K,A=r.from_json(p['point_coordinates']),r.from_json(p['point_frobenius'])
    known,witness=evaluate_chart(K,A,M,chart,rng)
    records=[witness]
    print('Published304-bit long multiple: full820x73 chart reconstructed.',flush=True)
    for j,item in enumerate(exp['exponentials']):
        K,A=r.from_json(item['point_coordinates']),r.from_json(item['point_frobenius'])
        assert r.equal(r.mm(K,A),r.mm(M['A2'],r.conjugate(K)))
        K,A,moving=move_away(K,A,[i-1 for i in base['families'][j]['points_1based']],M,derivative,r,rng)
        K,A,moving_back=flip(r.mm(M['V2'],K),A,M,rng,'Moving actual Abel representative back')
        value,witness=evaluate_chart(K,A,M,chart,rng)
        assert r.equal(value,known), 'Actual inverse Abel class differs from long-multiplication class'
        records.append({'first_residual_flip':moving,'second_residual_flip':moving_back,'chart':witness})
        print('Actual inverse Abel family',j+1,': all820x73 Picard chart entries agree with the actual long multiple PASS.',flush=True)
    out={'source_sha256':hashes,'exponential_sha256':hashlib.sha256(eraw).hexdigest(),
         'long_multiple_sha256':hashlib.sha256(pr).hexdigest(),'long_multiple_point_sha256':p['point_sha256'],
         'chart':chart_record(chart),'comparisons':records,
         'status':'both actual inverse Abel ideals equal the304-bit actual multiple modulo47^4; all full chart entries verified'}
    digest,size=write_checkpoint(args.output,out);print('Comparison certificate',size,digest,flush=True)

if __name__=='__main__':main()
