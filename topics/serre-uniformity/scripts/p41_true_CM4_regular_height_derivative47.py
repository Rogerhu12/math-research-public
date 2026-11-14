#!/usr/bin/env python3
"""Actual coarse CM4 jets and the regular combined F2/F3 height differential.

Keep the original rational SS frame and coordinate.  Divide only by proved
formal powers of z and by units.  This does not compute a height constant.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace


def read(p):
    b = Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--work-dir', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    args.script_dir = args.script_dir.resolve()
    args.work_dir.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(args.script_dir))
    import numpy as np
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel, save
    from p41_native_r2_linear47 import install
    from p41_projective_jet_frames47 import ProjectiveJetFrames, install_exact_float_mm
    from p41_elliptic_coarse_atlas47 import ClassicalInvariants, Series
    install_exact_float_mm(r)
    install(r, args.work_dir / 'native')
    a = ActualModel(args.script_dir)
    frames = ProjectiveJetFrames(a)
    Q, q = r.Q, 47**3
    start = time.monotonic()
    inputs = {}

    def load(name):
        p = args.script_dir / 'data' / name
        inputs[name] = sha(p)
        return read(p)

    atlas = load('p41_rational_SS_residue_atlas47_complete.json.gz')
    coarse = load('p41_elliptic_coarse_atlas47_verified.json.gz')
    deriv = load('p41_cleared_serre_derivative47_complete.json.gz')
    eta = load('p41_eta_calibration47_complete.json.gz')
    tiny = load('p41_all129_tiny_Abel47_complete.json.gz')
    oldtiny = load('p41_abel_coordinates_and_tiny47_complete.json.gz')
    assert tiny['input_sha256']['p41_abel_coordinates_and_tiny47_complete.json.gz'] == inputs['p41_abel_coordinates_and_tiny47_complete.json.gz']
    assert oldtiny['input_sha256']['p41_rational_SS_residue_atlas47_complete.json.gz'] == inputs['p41_rational_SS_residue_atlas47_complete.json.gz']
    v = r.from_json(deriv['chosen_clearing_section'])
    G = r.from_json(deriv['cleared_derivative_coefficients'])
    inv = ClassicalInvariants(SimpleNamespace(a=a, r=r, v=v, G=G))
    sourcecoarse = next(c for c in coarse['elliptic_charts'] if c['kind'] == 'CM4')
    assert sourcecoarse['parameter'] == 'u=B^2'
    assert sourcecoarse['curve_A'] == 1 and sourcecoarse['curve_B'] == 0
    sB, qB = [r.from_json(eta[k], q) for k in
              ['numerator_coefficients', 'denominator_coefficients']]
    assert eta['coefficient_precision'] >= 3
    records = []
    charts = [c for c in atlas['charts'] if c['reference_key'] == 'CM4']
    assert {d for c in charts for d in c['disk_ids']} == {'SS_j36_02', 'SS_j36_06'}

    def red(x):
        return a.reduce(x, q)

    def product(xs, ys, n, modulus=q):
        out = []
        for k in range(n):
            z = r.zeros(xs[0][0].shape[0], xs[0][0].shape[1])
            for i in range(k+1):
                if i < len(xs) and k-i < len(ys):
                    z = r.add(z, r.mul(xs[i], ys[k-i], modulus), modulus)
            out.append(z)
        return out

    def inverse(xs, n, modulus=q):
        out = [r.inverse_values(xs[0], modulus)]
        for k in range(1, n):
            z = r.zeros(xs[0][0].shape[0], xs[0][0].shape[1])
            for i in range(1, min(k, len(xs)-1)+1):
                z = r.add(z, r.mul(xs[i], out[k-i], modulus), modulus)
            out.append(r.neg(r.mul(out[0], z, modulus), modulus))
        return out

    for ch in charts:
        frame, coord = [r.from_json(ch[k]) for k in ['frame', 'coordinate']]
        assert r.equal(frame, a.fc)
        W0 = r.from_json(ch['W_coefficients_0to3'][0])
        J = frames.local_jets(W0, frame, coord, order=6)
        for kind in ['W', 'V2', 'V3']:
            for k in range(4):
                assert r.equal(J[kind][k], r.from_json(ch[kind+'_coefficients_0to3'][k]))
        assert all(not np.any(x[1]) for x in J['Hc'])
        assert np.all(r.units(J['Hc'][0]))
        iv = inv.series(J['W'])
        assert r.iszero(iv['v'][0])
        assert r.iszero(iv['Bv3'][0]) and r.iszero(iv['Bv3'][1])
        V, A, B = iv['v'][1:6], iv['Av'][:5], iv['Bv3'][2:7]
        assert all(np.all(r.units(t[0])) for t in [V, A, B])
        S = Series(a, 5)
        uunit = S.mul(S.power(B, 2), S.inverse(S.mul(S.power(A, 3), S.power(V, 3))))
        u = [r.zeros(W0[0].shape[0], 1)] + uunit[:4]
        denom = S.scale(u, 27)
        denom[0] = r.add(denom[0], r.column([[4, 0]]*W0[0].shape[0]))
        j = S.scale(S.inverse(denom), 6912)
        assert r.equal(j[0], r.column([[1728, 0]]*W0[0].shape[0]))
        assert np.all(r.units(j[1]))

        # Independent physical coarse-to-chart transport through degree three.
        # Its input is the already certified actual (A=1,B=0,u=B^2) family.
        indices = ch['original_input_rows_0based']
        labels = [sourcecoarse['indices_1based'][k] for k in indices]
        assert labels == [5, 614]
        physical_chart = dict(J, indices_0based=indices)
        z_of_u = frames.coarse_to_chart(sourcecoarse, physical_chart)
        recovered_u = Series(a, 4).reversion(z_of_u, 4)
        assert all(r.equal(x, y) for x, y in zip(u[:4], recovered_u))
        actual_raw = [r.rows(r.from_json(x), indices) for x in sourcecoarse['coarse_values']]
        normalized = Series(a, 4).mul(actual_raw,
                     Series(a, 4).inverse([r.mm(x, frame) for x in actual_raw]))
        composed = Series(a, 4).compose(J['W'][:4], z_of_u, 4)
        assert all(r.equal(x, y) for x, y in zip(normalized, composed))

        # Verify the canonical differentials in exactly the old coordinate.
        t = next(c for c in tiny['charts'] if c['disk_ids'] == ch['disk_ids'])
        ot = next(c for c in oldtiny['charts'] if c['disk_ids'] == ch['disk_ids'])
        assert t['origin'] == 'R230_SS'
        assert t['origin_chart_0based'] == ot['chart_0based'] == ch['chart_0based']
        assert t['canonical_differential_coefficients_0to2_mod47four'] == ot['canonical_differential_coefficients_0to2_mod47four']
        omega = Series(a, 3).mul([r.mm(w, a.K1) for w in J['W'][:3]],
                                J['inverse_Hc'][:3])
        for k in range(3):
            assert r.equal(omega[k], r.from_json(
                t['canonical_differential_coefficients_0to2_mod47four'][k]))

        nb = [r.mm(red(x), sB, q) for x in J['V3'][:4]]
        db = [r.mm(red(x), qB, q) for x in J['V2'][:5]]
        assert r.iszero(db[0]), 'The exact CM4 pole is at z=0'
        assert np.all(r.units(db[1])), 'A repeated auxiliary zero needs its own cancellation'
        dzb = db[1:5]
        scaled_n = product(nb, [red(x) for x in J['inverse_Hc'][:4]], 4)
        beta = product(scaled_n, inverse(dzb, 4), 4)
        assert r.equal(beta[0], r.column([[1, 0]]*W0[0].shape[0])), 'Actual residue +1'
        eta_regular = beta[1:4]

        # j-1728=z*Junit.  Its logarithmic pole and that of eta_B cancel.
        junit = [red(x) for x in j[1:5]]
        jprime = [a.scale(red(j[k+1]), k+1, q) for k in range(3)]
        jsecond = [a.scale(red(j[k+2]), (k+2)*(k+1), q) for k in range(3)]
        junitprime = [a.scale(junit[k+1], k+1, q) for k in range(3)]
        dlogjunit = product(junitprime, inverse(junit, 3), 3)
        dlogjprime = product(jsecond, inverse(jprime, 3), 3)
        dlogj = product(jprime, inverse([red(x) for x in j[:3]], 3), 3)
        combined = [
            r.add(r.add(a.scale(dlogjprime[k], -4, q),
                        a.scale(dlogj[k], 8*pow(3, -1, q), q), q),
                  a.scale(r.sub(dlogjunit[k], eta_regular[k], q), 2, q), q)
            for k in range(3)]
        assert all(not np.any(x[1]) for x in combined)
        rec = {
            'disk_ids': ch['disk_ids'], 'chart_0based': ch['chart_0based'],
            'necklace_labels_1based': labels,
            'frame': ch['frame'], 'coordinate': ch['coordinate'],
            'original_R228_coordinate_unchanged': True,
            'W_coefficients_0to6': [r.to_json(x) for x in J['W']],
            'V2_coefficients_0to6': [r.to_json(x) for x in J['V2']],
            'V3_coefficients_0to6': [r.to_json(x) for x in J['V3']],
            'Hc_coefficients_0to6': [r.to_json(x) for x in J['Hc']],
            'original_clearing_v_coefficients_0to6': [r.to_json(x) for x in iv['v']],
            'Av_coefficients_0to6': [r.to_json(x) for x in iv['Av']],
            'Bv3_coefficients_0to6': [r.to_json(x) for x in iv['Bv3']],
            'u_over_z_coefficients_0to4': [r.to_json(x) for x in uunit],
            'u_coefficients_0to4': [r.to_json(x) for x in u],
            'j_coefficients_0to4': [r.to_json(x) for x in j],
            'coarse_u_transport_coefficients_0to3': [r.to_json(x) for x in recovered_u],
            'eta_B_numerator_coefficients_0to3_mod47cubed': [r.to_json(x) for x in nb],
            'eta_B_denominator_coefficients_0to4_mod47cubed': [r.to_json(x) for x in db],
            'eta_B_residue': 1,
            'eta_B_regular_coefficients_0to2_mod47cubed': [r.to_json(x) for x in eta_regular],
            'dlog_jminus1728_over_z_coefficients_0to2_mod47cubed': [r.to_json(x) for x in dlogjunit],
            'regular_F2_combination_coefficients_0to2_mod47cubed': [r.to_json(x) for x in combined],
            'regular_F3_combination_coefficients_0to2_mod47cubed':
                [r.to_json(a.scale(x, pow(2, -1, q), q)) for x in combined],
            'exact_formal_v_and_Bv3_orders': [1, 2],
            'Av_v_over_z_Bv3_over_z2_all_units': True,
            'jprime_and_j_units_in_original_z': True,
            'all73_physical_coarse_compositions_through_degree3': True,
            'all54_canonical_differentials_through_degree2_match_original_tiny': True,
            'actual_eta_B_simple_pole_and_residue_one': True,
            'no_nonunit_inversion_or_division_by47': True,
        }
        records.append(rec)
        print('ACTUAL_CM4_REGULAR_COMBINATION', ch['disk_ids'],
              [r.to_json(x) for x in combined], flush=True)
    out = {
        'result': 'R554', 'level': 41, 'auxiliary_prime': 47,
        'modulus': Q, 'differential_modulus': q, 'charts': records,
        'formula': '-4*jsecond/jprime+(8/3)*jprime/j+2*(dlog((j-1728)/z)-(eta_B/dz-1/z))',
        'scope': 'Actual coarse coordinate and joint removable-pole differential only; no height constant, Norm or disk exclusion claim.',
        'both_true_rational_CM4_disks_complete': True,
        'source_sha256': sha(__file__), 'input_sha256': dict(a.inputs, **inputs),
        'runtime_seconds': round(time.monotonic()-start, 3)}
    digest = save(args.output, out)
    print('COMPLETE_TRUE_CM4_REGULARIZATION', digest, flush=True)


if __name__ == '__main__':
    main()
