#!/usr/bin/env python3
"""Compute the actual degree-four T2C pole divisor on SS_j10_11 without p-division."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys


def read(p):
    p=Path(p)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ['script-dir','support','work-dir','output']:
        ap.add_argument('--'+key,type=Path,required=True)
    args=ap.parse_args()
    sys.path.insert(0,str(args.script_dir.resolve()))
    from p41_actual_differentials47 import ActualModel,save
    from p41_projective_jet_frames47 import ProjectiveJetFrames,install_exact_float_mm
    from p41_native_r2_linear47 import install
    from p41_finite_flat_divisor_constraints47 import finite_flat_constraints
    import p41_r2_matrix as r
    install_exact_float_mm(r)
    install(r,args.work_dir/'native')
    a=ActualModel(args.script_dir)
    frames=ProjectiveJetFrames(a)
    support=read(args.support)
    assert support['source_disk_id']=='SS_j10_11'
    cm=a.read('p41_cm_quadratic_jets47_raw.json.gz')
    u=next(x for x in cm['records'] if x['label']=='P_minus12')['normalized_weight2_coefficients'][0]
    points=r.from_json(support['actual_T2_targets_fc_normalized']+[u])
    assert r.equal(r.mm(points,a.fc),r.column([[1,0]]*4))
    rawrank=len(r.rank_pivots(points)[0])
    assert rawrank==3
    constraints,certificate=finite_flat_constraints(a,frames,points)
    pair=[x for x in certificate['records'] if len(x['indices_0based'])==2]
    assert len(pair)==1 and pair[0]['indices_0based']==[0,3]
    rr,cc=r.rank_pivots(constraints)
    K,_,_=r.kernel_from_rows(r.rows(constraints,rr),rr,cc)
    assert r.iszero(r.mm(constraints,K))
    bases=a.read('p41_hecke3_abel_bases_checkpoint.json.gz')
    I=[i-1 for f in bases['families'] for i in f['points_1based']]
    source=r.from_json([support['actual_source_W_fc_normalized']])
    rng=random.Random(4104737211)
    for attempt in range(100):
        x=r.mm(K,r.column([[rng.randrange(47),rng.randrange(47)] for _ in range(69)]))
        q=r.add(x,r.mm(a.M['A1'],r.conjugate(x)))
        assert r.iszero(r.mm(constraints,q)) and r.iszero(r.mm(points,q))
        if a.np.all(r.units(r.mm(r.rows(a.M['W'],I),q))) and a.np.all(r.units(r.mm(source,q))):
            break
    else:
        raise AssertionError('No actual degree-four divisor denominator unit at all required evaluation points')
    assert r.equal(r.mm(a.M['A1'],r.conjugate(q)),q)
    out={'result':'R372','disk_id':'SS_j10_11','actual_T2C_poles':'three genuine T2(P) targets and u; the first target and u are distinct lifts of one residue point',
         'original_four_evaluation_rows_rank_mod47':rawrank,
         'finite_flat_divisor_constraint_certificate':certificate,
         'actual_T2_targets_and_u_W_fc_normalized':r.to_json(points),
         'actual_linear_denominator_coefficients_mod47four':r.to_json(q),
         'all_actual_four_point_values_zero_mod47four':True,
         'all108_Abel_family_values_and_source_value_units':True,
         'source_denominator_value_mod47four':r.to_json(r.mm(source,q)),
         'actual_Frobenius_rational_denominator':True,'denominator_attempt_0based':attempt,
         'division_by_nonunit_or47_used':False,'complete_actual_height':False,
         'input_sha256':dict(a.inputs,**{str(args.support):sha(args.support)}),
         'source_sha256':sha(__file__),
         'helper_sha256':sha(Path(__file__).with_name('p41_finite_flat_divisor_constraints47.py')),
         'scope':'Actual T2 pole divisor, integral divided differences, and a full four-digit linear denominator; no principal chain or center height has been executed.'}
    print('PASS CM48 actual confluent T2 divisor',save(args.output,out),flush=True)


if __name__=='__main__':
    main()
