#!/usr/bin/env python3
"""Actual Makdisi representatives of P_minus12-b and P_minus7-b, retaining h=f_b/f0."""
import argparse,gzip,hashlib,json,random,sys
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--script-dir',type=Path,required=True)
    p.add_argument('--jets',type=Path,default=Path('/tmp/p41_cm_quadratic_jets47_raw.json.gz'))
    p.add_argument('--output',type=Path,default=Path('/tmp/p41_cm_based_points47_checkpoint.json.gz'))
    args=p.parse_args();sys.path.insert(0,str(args.script_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources,make_model
    from p41_hecke3_hessian47 import section_jets
    from p41_formal47_multiply import write_checkpoint,point_hash
    from p41_poincare_norms47 import determinant
    sources,hashes=load_sources(args.script_dir/'data');M=make_model(sources)
    raw=args.jets.read_bytes();jets=json.loads(gzip.decompress(raw));assert jets['source_sha256']==hashes
    points=jets['records'][:3];assert [a['label'] for a in points]==['P_minus3','P_minus12','P_minus7']
    W0=r.from_json([a['normalized_weight2_coefficients'][0] for a in points]);db=r.from_json([points[0]['normalized_weight2_coefficients'][1]])
    vb=r.rows(W0,[0]);rr,cc=r.rank_pivots(vb);HB,free,block=r.kernel_from_rows(r.rows(vb,rr),rr,cc)
    assert HB[0].shape==(73,72) and r.iszero(r.mm(vb,HB))
    AH=r.rows(r.mm(M['A1'],r.conjugate(HB)),free)
    assert r.equal(r.mm(HB,AH),r.mm(M['A1'],r.conjugate(HB)))
    rng=random.Random(4104716019)
    for attempt in range(1,1001):
        seed,small=r.rational_trace(AH,rng);fbcoeff=r.mm(HB,small);fb=r.mm(M['W'],fbcoeff)
        if np.all(r.units(fb)) and np.all(r.units(r.mm(r.rows(W0,[1,2]),fbcoeff))) and r.units(r.mm(db,fbcoeff))[0,0]:break
    else:raise RuntimeError('No actual f_b with the required simple and disjoint divisor')
    assert r.iszero(r.mm(vb,fbcoeff)) and r.equal(r.mm(M['A1'],r.conjugate(fbcoeff)),fbcoeff)
    invfb=r.inverse_values(fb);constraints=[];colon_sources=[]
    for trial in range(1,11):
        hs,hcsmall=r.rational_trace(AH,rng);hc=r.mm(HB,hcsmall);hv=r.mm(M['W'],hc)
        scaled=r.mul(r.mul(hv,invfb),M['V2']);residual=r.sub(scaled,r.mm(M['V2'],r.rows(scaled,M['P2'])))
        constraints.append(residual);colon_sources.append(r.to_json(hc))
        R=(np.vstack([a[0] for a in constraints]),np.vstack([a[1] for a in constraints]))
        rr,cc=r.rank_pivots(R);assert len(rr)<=125
        if len(rr)==125:break
    else:raise RuntimeError('Actual colon did not reach the complete74-dimensional divisor ideal')
    DB,ff,bb=r.kernel_from_rows(r.rows(R,rr),rr,cc);assert DB[0].shape==(199,74) and r.iszero(r.mm(R,DB))
    V2,_=section_jets([W0],sources,M,r);records=[]
    for row,P in enumerate(points[1:],1):
        restriction=r.mm(r.rows(V2[0],[row]),DB);pr,pc=r.rank_pivots(restriction);assert len(pr)==1
        reduced,efree,eblock=r.kernel_from_rows(r.rows(restriction,pr),pr,pc)
        E=r.mm(DB,reduced);E,er,ec,Echange=r.normalize(E,73)
        A=r.rows(r.mm(M['A2'],r.conjugate(E)),er)
        assert r.equal(r.mm(E,A),r.mm(M['A2'],r.conjugate(E))) and r.equal(r.mm(A,r.conjugate(A)),r.eye(73))
        assert r.iszero(r.mm(r.rows(V2[0],[row]),E))
        assert len(r.rank_pivots(r.mm(r.rows(V2[0],[0]),E))[0])==1,'The actual E_P unexpectedly contains b'
        records.append({'point_label':P['label'],'point_coordinates':r.to_json(E),'point_frobenius':r.to_json(A),
                        'point_sha256':point_hash(E,A),'normalization_rows_1based':[a+1 for a in er],
                        'actual_divisor':'E_P=div(f_b)-b+P; E_P-div(f0)=P-b+div(f_b/f0)'})
    out={'level':41,'auxiliary_prime':47,'precision':4,'source_sha256':hashes,
         'jet_source_sha256':hashlib.sha256(raw).hexdigest(),
         'generating_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'f_b_attempt':attempt,'f_b_seed':r.to_json(seed),'f_b_coefficients':r.to_json(fbcoeff),
         'f_b_derivative_at_b':r.to_json(r.mm(db,fbcoeff)),
         'f_b_over_f0_at_CM12_CM7':r.to_json(r.mm(r.rows(W0,[1,2]),fbcoeff)),
         'colon_trials':trial,'colon_rank':125,'colon_dimension':74,
         'colon_test_section_coefficients':colon_sources,
         'colon_rank_rows_1based':[a+1 for a in rr],'colon_rank_columns_1based':[a+1 for a in cc],
         'colon_kernel_block_sha256':hashlib.sha256(json.dumps(r.to_json(bb),separators=(',',':')).encode()).hexdigest(),
         'records':records,'status':'actual based CM Jacobian points and explicit initial principal transport h=f_b/f0; no additional long multiplication or Hecke-r transport claimed'}
    sha,size=write_checkpoint(args.output,out)
    print('ACTUAL BASED CM POINTS PASS',[(a['point_label'],a['point_sha256']) for a in records],
          'colon',trial,125,'bytes',size,'sha',sha,flush=True)

if __name__=='__main__':main()
