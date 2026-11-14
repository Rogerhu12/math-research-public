#!/usr/bin/env python3
"""Independent stored-fraction/colon/trace/arithmetic audit for R259."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--certificate', type=Path, required=True)
    ap.add_argument('--build-dir', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel
    from p41_projective_jet_frames47 import install_exact_float_mm
    from p41_native_r2_linear47 import install
    install_exact_float_mm(r)
    install(r, args.build_dir)
    a = ActualModel(args.script_dir)
    data = read(args.certificate)
    assert data['complete_actual_local_sigma_F2_center_height']
    assert sha(args.certificate) == 'afd046cbad7657edf0dc13950b5bdad3031ad59872174a492d1228ae1dd4eded'
    Q, q = 47**4, 47**3
    reduce = lambda x: a.reduce(x, q)
    mm = lambda x, y: r.mm(x, y, q)
    beta = -3*pow(27652, -1, q) % q
    bases = a.read('p41_hecke3_abel_bases_checkpoint.json.gz')
    I2 = [j-1 for j in bases['families'][1]['points_1based']]
    Omega2 = a.scale(mm(reduce(r.rows(a.M['W'], I2)), reduce(a.K1)), beta, q)
    assert len(r.rank_pivots(Omega2)[0]) == 54
    rho = [x-1 for x in a.cusp['cusp_frobenius_permutation_1based']]
    cusp_orbits = []
    for start in [0, 11]:
        orbit, x = [], start
        while x not in orbit:
            orbit.append(x)
            x = rho[rho[x]]
        assert x == start and len(orbit) == 10
        cusp_orbits.append(orbit)
    assert set(cusp_orbits[0]).isdisjoint(cusp_orbits[1])
    assert set(cusp_orbits[0]+cusp_orbits[1]) == set(range(20))
    a.field_setup()
    cusp_values = [(reduce(a.field_coordinates(a.cusp['cusp_values'][j])), reduce(a.cusp_evaluations(j)[0]))
                   for j in [0, 11]]
    rng = random.Random(259260473)
    records = {}
    for name, rec in data['actual_connections'].items():
        if name == 'T2C':
            continue
        W = r.from_json(rec['finite_pole_coordinates_fc_normalized'])
        n = W[0].shape[0]
        assert n == len(rec['finite_residues'])
        assert sum(rec['finite_residues'])+20*rec['cusp_residue'] == 0
        assert r.equal(r.mm(W, a.fc), r.column([[1, 0]]*n))
        s, den = r.from_json(rec['numerator_quadratic_coefficients_mod47cubed']), r.from_json(rec['denominator_linear_coefficients_mod47four'])
        V2, V3 = a.evaluate(W)
        dden = r.mm(r.mm(V3, a.H), den)
        assert r.iszero(r.mm(W, den)) and np.all(r.units(dden))
        want = r.mul(reduce(dden), r.column([[v % q, 0] for v in rec['finite_residues']]), q)
        assert r.equal(mm(reduce(V2), s), want)
        for CW, CV2 in cusp_values:
            assert r.equal(a.scale(mm(CV2, s), 41, q), a.scale(mm(CW, reduce(den)), rec['cusp_residue'], q))
        source_den = r.mm(a.M['W'], den)
        values2 = mm(reduce(r.rows(a.M['V2'], I2)), s)
        gradient = r.from_json(rec['calibration_gradient_original_nu_mod47cubed'])
        target = r.mul(reduce(r.rows(source_den, I2)), tuple(x.T.copy() for x in gradient), q)
        assert r.equal(a.scale(values2, beta, q), target)
        assert r.equal(mm(reduce(a.M['A2']), r.conjugate(s, q)), s)
        # Rebuild the colon with independent random test sections.  Every
        # cleared identity lives in H0(3L), degree378, below the row count.
        wr, wc = r.rank_pivots(W)
        assert len(wr) == n
        K, _, _ = r.kernel_from_rows(r.rows(W, wr), wr, wc)
        good = np.flatnonzero(r.units(source_den)[:, 0]).tolist()
        assert len(good) > 378
        E = reduce(r.rows(a.M['V2'], good))
        er, ec = r.rank_pivots(E)
        assert len(er) == 199
        Ei = r.inverse_matrix(r.rows(E, er), q)
        iq = r.inverse_values(reduce(r.rows(source_den, good)), q)
        constraint = r.zeros(0, 199)
        tested_ranks = []
        for trial in range(8):
            seed = r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(73-n)])
            g = r.mm(K, seed)
            multiplier = r.mul(reduce(r.rows(r.mm(a.M['W'], g), good)), iq, q)
            block = r.mul(multiplier, E, q)
            residual = r.sub(block, mm(E, mm(Ei, r.rows(block, er))), q)
            joined = tuple(np.concatenate([x, y], axis=0) for x, y in zip(constraint, residual))
            rr, cc = r.rank_pivots(joined)
            assert len(rr) <= 126-n
            constraint = r.rows(joined, rr)
            tested_ranks.append(len(rr))
            assert r.iszero(mm(constraint, s))
            if len(rr) == 126-n:
                break
        assert tested_ranks[-1] == 126-n
        records[name] = {'finite_simple_pole_count': n, 'full_allowed_pole_degree_including_cusps': n+20,
                         'line_bundle_degree': 126+n, 'full_RR_dimension': 73+n,
                         'independent_colon_rank_history': tested_ranks, 'good_rows': len(good),
                         'all_actual_finite_and_full_cusp_residues_verified': True,
                         'all54_actual_family2_calibration_values_verified': True,
                         'full_RR_numerator_membership_verified': True}
        print('PASS independent stored fraction and complete colon', name, tested_ranks, flush=True)
    # Actual T2 pullback trace is independently compared after clearing qT.
    h = a.read('p41_hecke47_full_saved.json.gz')['operators']['2']
    permutation = [i-1 for i in h['necklace_transport_1based']]
    sC = r.from_json(data['actual_connections']['C']['numerator_quadratic_coefficients_mod47cubed'])
    qC = r.from_json(data['actual_connections']['C']['denominator_linear_coefficients_mod47four'])
    total, mask = r.zeros(820, 1), np.ones(820, dtype=bool)
    for branch in h['targets']:
        W = r.from_json(branch['evaluation_matrix'])
        V2, _ = a.evaluate(W)
        denominator = r.mm(W, qC)
        good = np.flatnonzero(r.units(denominator)[:, 0]).tolist()
        value = r.zeros(820, 1)
        quotient = r.mul(mm(reduce(r.rows(V2, good)), sC), r.inverse_values(reduce(r.rows(denominator, good)), q), q)
        for k in range(2):
            value[k][good] = quotient[k]
        total = r.add(total, r.rows(value, permutation), q)
        mask &= r.units(denominator)[:, 0][permutation]
    total = a.scale(total, pow(2, -1, q), q)
    good = np.flatnonzero(mask).tolist()
    assert len(good) == 819
    rec = data['actual_connections']['T2C']
    sT = r.from_json(rec['numerator_quadratic_coefficients_mod47cubed'])
    qT = r.from_json(rec['denominator_linear_coefficients_mod47four'])
    lhs = mm(reduce(r.rows(a.M['V2'], good)), sT)
    rhs = r.mul(reduce(r.rows(r.mm(a.M['W'], qT), good)), r.rows(total, good), q)
    assert r.equal(lhs, rhs)
    for CW, CV2 in cusp_values:
        assert r.iszero(mm(CV2, sT))
    # A separate scalar-pair implementation recomputes all eight tiny sums.
    def plus(x, y): return [(x[k]+y[k]) % Q for k in range(2)]
    def times(x, y): return [(x[0]*y[0]-x[1]*y[1]) % Q, (x[0]*y[1]+x[1]*y[0]) % Q]
    parameters = data['physical_family1_parameters'][0]
    tinies = {}
    for name, jets in data['integrand_coefficients_0to2'].items():
        answer = [0, 0]
        for j, t in enumerate(parameters):
            assert all(x % 47 == 0 for x in t)
            power = t
            for k in range(3):
                term = times(power, jets[k][j][0])
                answer = plus(answer, [x*pow(k+1, -1, Q) % Q for x in term])
                power = times(power, t)
        assert answer == [data['all_actual_tiny_integrals_mod47four'][name], 0]
        tinies[name] = answer[0]
    weights = {'T2C': 27, 'C': 4, 'u_minus_b': 162, 'Z8_minus20b': -27,
               'c7_minus_b': -54, 'K_g1_minus106b': 4}
    tinyD = sum(weight*tinies[name] for name, weight in weights.items()) % Q
    assert tinyD == data['second_divisor_tiny_integral_mod47four'] == 4160581
    m = data['actual_integer_scale']
    assert m % Q == 459340 and pow(m, -1, Q) == 4074216
    normelement = (tinyD+data['first_variable_principal_log_norm_mod47four'])*pow(m, -1, Q) % Q
    actual = (normelement+data['canonical_sigma_coordinate_log_mod47four']) % Q
    assert normelement == 2731264 and actual == data['actual_local_sigma_F2_height_mod47four'] == 4213785
    output = {'result': 'R259 independent audit', 'input_certificate_sha256': sha(args.certificate),
              'source_sha256': sha(__file__), 'five_actual_fractions_and_full_colon_spaces': records,
              'family2_canonical_evaluation_rank': 54, 'complete_cusp_orbits_0based': cusp_orbits,
              'actual_T2_trace_rows_independently_checked': len(good), 'T2_trace_scale': '1/2',
              'all_eight_scalar_tiny_integrals': tinies, 'second_divisor_tiny': tinyD,
              'actual_norm_element_height': normelement, 'actual_canonical_F2_height': actual,
              'complete_actual_stored_fraction_and_arithmetic_audit': True}
    args.output.write_text(json.dumps(output, sort_keys=True, indent=2)+'\n')
    print('PASS INDEPENDENT R259 AUDIT', actual, sha(args.output), flush=True)


if __name__ == '__main__':
    main()
