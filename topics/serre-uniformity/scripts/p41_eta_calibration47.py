#!/usr/bin/env python3
"""Recover the actual R194 third-kind differential in a 93-dimensional space."""
import argparse
import hashlib
from pathlib import Path
import time

from p41_actual_differentials47 import ActualModel, Q, Q3, digest, flat, report, save


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    started = time.monotonic()
    a = ActualModel(args.script_dir)
    r, np, M, K = a.r, a.np, a.M, a.kernel
    group, cusp = a.group, a.cusp
    Kneg = r.from_json(K(199, group['negative_rank_columns_1based'], group['negative_free_columns_1based'], group['negative_kernel_block']))
    KI = r.from_json(K(199, cusp['K_rank_columns_1based'], cusp['K_free_columns_1based'], cusp['K_kernel_block']))
    Uneg, Rneg, hneg = a.product_space(r.mm(M['V2'], Kneg), 199)
    Ucan, Rcan, hcan = a.product_space(r.mm(M['V2'], KI), 219)
    residual = r.sub(Ucan, r.mm(Uneg, r.rows(Ucan, Rneg)))
    rr, cc = r.rank_pivots(residual)
    assert len(rr) == 126
    J, free, block = r.kernel_from_rows(r.rows(residual, rr), rr, cc)
    assert r.iszero(r.mm(residual, J))
    S = r.mm(r.rows(Ucan, M['P3']), J)
    assert S[0].shape == (325, 93)
    sr, sc = r.rank_pivots(S)
    assert len(sr) == 93 and sc == list(range(93))
    AS = r.mm(r.inverse_matrix(r.rows(S, sr)), r.rows(r.mm(M['A3'], r.conjugate(S)), sr))
    assert r.equal(r.mm(S, AS), r.mm(M['A3'], r.conjugate(S)))
    qco = r.mm(M['B'], r.column(group['negative_flip_section_seeds_and_coefficients'][0][1]))
    assert np.all(r.units(r.mm(M['V2'], qco)))
    assert r.equal(r.mm(M['A2'], r.conjugate(qco)), qco)
    del residual, Uneg, Ucan, Kneg, KI, J
    report('Actual third-kind space rank 93 and Frobenius verified')
    WZ = r.from_json(a.cm4['coarse_point_values'])
    WZ = r.mul(WZ, r.inverse_values(r.mm(WZ, a.fc)))
    V2Z, V3Z = a.evaluate(WZ)
    assert r.iszero(r.mm(V2Z, qco))
    HZ = r.mm(V3Z, a.H)
    dqmon = r.mm(a.C2, qco)
    dqraw = r.add(r.mul(r.cols(WZ, a.a2), r.cols(HZ, a.b2)), r.mul(r.cols(HZ, a.a2), r.cols(WZ, a.b2)))
    dq = r.mm(dqraw, dqmon)
    assert np.all(r.units(dq))
    CMrows = r.mul(r.mm(V3Z, S), r.inverse_values(dq))
    assert len(r.rank_pivots(CMrows)[0]) == 20
    rows = [CMrows]
    rhs = [r.column([[1, 0]]*20)]
    cusp_indices = [0, 11]
    cusp_orbits = []
    perm = [v-1 for v in cusp['cusp_frobenius_permutation_1based']]
    for index in cusp_indices:
        orbit = []
        k = index
        while k not in orbit:
            orbit.append(k)
            k = perm[perm[k]]
        assert k == index and len(orbit) == 10
        cusp_orbits.append([k+1 for k in orbit])
        CV2, CV3 = a.cusp_evaluations(index)
        rows.append(a.scale(r.mm(CV3, S), 41))
        rhs.append(r.neg(r.mm(CV2, qco)))
    assert set(cusp_orbits[0]).isdisjoint(cusp_orbits[1])
    def vcat(xs):
        return tuple(np.concatenate([x[k] for x in xs], axis=0) for k in range(2))
    poleRows, poleRHS = vcat(rows), vcat(rhs)
    assert len(r.rank_pivots(poleRows)[0]) == 39
    report('20 actual CM residues and both full R80 cusp equations verified')
    frame = a.read('p41_hecke3_formal_height47_compact.json.gz')
    bases = a.read('p41_hecke3_abel_bases_checkpoint.json.gz')
    completion = a.read('p41_miller_completion47_compact.json.gz')
    I = [i-1 for i in frame['families'][1]['points_1based']]
    assert frame['families'][1]['points_1based'] == bases['families'][1]['points_1based']
    CV = r.mm(r.rows(M['W'], I), a.K1)
    assert len(r.rank_pivots(CV)[0]) == 54
    g = r.column(flat(completion['actual_initial_fibre_Lie_gradient_mod47_cubed']), Q3)
    qv = a.reduce(r.mm(r.rows(M['V2'], I), qco), Q3)
    assert np.all(r.units(qv))
    calrows = a.reduce(r.mm(r.rows(M['V3'], I), S), Q3)
    calrhs = r.mul(qv, r.mm(a.reduce(CV, Q3), g, Q3), Q3)
    A = vcat([a.reduce(poleRows, Q3), calrows])
    b = vcat([a.reduce(poleRHS, Q3), calrhs])
    rr, cc = r.rank_pivots(A)
    assert len(rr) == 93 and cc == list(range(93))
    co = r.mm(r.inverse_matrix(r.rows(A, rr), Q3), r.rows(b, rr), Q3)
    assert r.equal(r.mm(A, co, Q3), b)
    assert r.equal(r.mm(a.reduce(AS, Q3), r.conjugate(co, Q3), Q3), co)
    s = r.mm(a.reduce(S, Q3), co, Q3)
    qco = a.reduce(qco, Q3)
    assert r.equal(r.mm(a.reduce(M['A3'], Q3), r.conjugate(s, Q3), Q3), s)
    assert r.equal(r.mm(a.reduce(M['A2'], Q3), r.conjugate(qco, Q3), Q3), qco)
    ssha, qsha = digest(r.to_json(s)), digest(r.to_json(qco))
    assert ssha == 'f1be6a6ae4e9cee06e0439d49c02234926099ba7825ee0cbacabe93d072a3e87'
    assert qsha == '26c3d25651a22b75eb3b337c4a35980102ec7529077f5598a1e4a53d767dc5ae'
    out = {'status': 'all 154 equations, residues, full cusp fields and Frobenius independently re-executed after environment reset',
           'level': 41, 'auxiliary_prime': 47, 'coefficient_precision': 3,
           'numerator_coefficients': r.to_json(s), 'denominator_coefficients': r.to_json(qco),
           'numerator_sha256': ssha, 'denominator_sha256': qsha,
           'product_rank_histories': {'negative': hneg, 'canonical': hcan},
           'product_ranks': [199,219], 'intersection_rank': 93, 'CM_residue_rank': 20,
           'combined_residue_rank': 39, 'final_calibration_rank': 93, 'equations_checked': 154,
           'residue_and_calibration_unit_minor_rows_1based': [x+1 for x in rr],
           'CM_residues': [1]*20, 'cusp_residue': -1, 'cusp_Fr_squared_orbits_1based': cusp_orbits,
           'Lie_gradient_mod47_cubed': r.to_json(g), 'calibration_points_1based': [i+1 for i in I],
           'global_derivation_coefficients_sha256': a.H_sha,
           'normalization': 'R145 family1 actual Poincare initial fibre gradient from R151; KS omega=dx/(2y) retained',
           'input_sha256': a.inputs, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'engine_sha256': hashlib.sha256(Path(__file__).with_name('p41_actual_differentials47.py').read_bytes()).hexdigest()}
    h = save(args.output, out)
    report('R194 restored and all intrinsic SHA matched; seconds='+str(round(time.monotonic()-started, 3)))
    print(str(args.output)+' SHA256 '+h, flush=True)


if __name__ == '__main__':
    main()
