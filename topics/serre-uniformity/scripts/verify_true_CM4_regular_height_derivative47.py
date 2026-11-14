#!/usr/bin/env python3
"""Independent Python-integer replay of actual CM4 jets and Laurent cancellation."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys


def read(p):
    b = Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


class Ring:
    def __init__(self, modulus):
        self.m = modulus
        self.zero = (0, 0)
        self.one = (1, 0)

    def cv(self, x):
        return (int(x[0]) % self.m, int(x[1]) % self.m)

    def add(self, x, y):
        return ((x[0]+y[0]) % self.m, (x[1]+y[1]) % self.m)

    def sub(self, x, y):
        return ((x[0]-y[0]) % self.m, (x[1]-y[1]) % self.m)

    def mul(self, x, y):
        return ((x[0]*y[0]-x[1]*y[1]) % self.m,
                (x[0]*y[1]+x[1]*y[0]) % self.m)

    def scale(self, x, n):
        return (x[0]*n % self.m, x[1]*n % self.m)

    def unit(self, x):
        return bool(x[0] % 47 or x[1] % 47)

    def inverse(self, x):
        assert self.unit(x)
        d = pow((x[0]*x[0]+x[1]*x[1]) % self.m, -1, self.m)
        return (x[0]*d % self.m, -x[1]*d % self.m)

    def dot(self, xs, ys):
        assert len(xs) == len(ys)
        return (sum(x[0]*y[0]-x[1]*y[1] for x, y in zip(xs, ys)) % self.m,
                sum(x[0]*y[1]+x[1]*y[0] for x, y in zip(xs, ys)) % self.m)

    def rowmat(self, row, cols):
        return [self.dot(row, col) for col in cols]

    def product(self, xs, ys, n):
        out = []
        for i in range(n):
            z = self.zero
            for k in range(i+1):
                if k < len(xs) and i-k < len(ys):
                    z = self.add(z, self.mul(xs[k], ys[i-k]))
            out.append(z)
        return out

    def invseries(self, xs, n):
        out = [self.inverse(xs[0])]
        for i in range(1, n):
            z = self.zero
            for k in range(1, min(i, len(xs)-1)+1):
                z = self.add(z, self.mul(xs[k], out[i-k]))
            out.append(self.scale(self.mul(out[0], z), -1))
        return out

    def power(self, xs, exponent, n):
        out = xs
        for _ in range(exponent-1):
            out = self.product(out, xs, n)
        return out

    def vadd(self, x, y):
        return [self.add(a, b) for a, b in zip(x, y)]

    def vsub(self, x, y):
        return [self.sub(a, b) for a, b in zip(x, y)]

    def vmul(self, x, y):
        return [self.mul(a, b) for a, b in zip(x, y)]

    def vmulscalar(self, x, c):
        return [self.mul(a, c) for a in x]

    def vconv(self, xs, ys, n):
        out = [self.zero]*len(xs[0])
        for k in range(n+1):
            out = self.vadd(out, self.vmul(xs[k], ys[n-k]))
        return out

    def svconv(self, xs, ys, n):
        out = [self.zero]*len(ys[0])
        for k in range(n+1):
            out = self.vadd(out, self.vmulscalar(ys[n-k], xs[k]))
        return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for k in ['script-dir', 'certificate', 'generator', 'output']:
        ap.add_argument('--'+k, type=Path, required=True)
    args = ap.parse_args()
    S = args.script_dir.resolve()
    x = read(args.certificate)
    assert x['result'] == 'R554' and x['source_sha256'] == sha(args.generator)
    for name, digest in x['input_sha256'].items():
        path = S/'data'/Path(name).name
        assert path.exists() and sha(path) == digest, path
    sys.path.insert(0, str(S))
    from p41_actual_differentials47 import ActualModel
    a = ActualModel(S)
    conv = a.r.to_json
    R, T = Ring(47**4), Ring(47**3)

    def colvector(matrix):
        return [R.cv(row[0]) for row in conv(matrix)]

    def columns(matrix):
        return list(zip(*conv(matrix)))

    fc = colvector(a.fc)
    lam, ifp = [[R.cv(z) for z in conv(y)[0]] for y in [a.lam, a.ifP2]]
    C2, E3, C, H, K1 = [columns(y) for y in [a.C2, a.E3, a.C, a.H, a.K1]]
    derivative = read(S/'data/p41_cleared_serre_derivative47_complete.json.gz')
    v = [R.cv(z[0]) for z in derivative['chosen_clearing_section']]
    G = list(zip(*derivative['cleared_derivative_coefficients']))
    av_values = [R.dot(row, v) for row in conv(a.M['W'])]
    Av = [av_values[k] for k in a.M['P3']]
    eta = read(S/'data/p41_eta_calibration47_complete.json.gz')
    sB, qB = [[T.cv(z[0]) for z in eta[k]] for k in
              ['numerator_coefficients', 'denominator_coefficients']]
    atlas = read(S/'data/p41_rational_SS_residue_atlas47_complete.json.gz')
    tiny = read(S/'data/p41_all129_tiny_Abel47_complete.json.gz')
    records, ode_entries, section_entries = [], 0, 0

    for cert in x['charts']:
        ch = next(c for c in atlas['charts'] if c['disk_ids'] == cert['disk_ids'])
        assert cert['frame'] == ch['frame'] and cert['coordinate'] == ch['coordinate']
        assert cert['W_coefficients_0to6'][:4] == ch['W_coefficients_0to3']
        coordinate = [R.cv(z[0]) for z in ch['coordinate']]
        t = next(c for c in tiny['charts'] if c['disk_ids'] == ch['disk_ids'])
        for row, disk in enumerate(cert['disk_ids']):
            vals = lambda key: [R.cv(z[row][0]) for z in cert[key]]
            W = [[R.cv(z) for z in coeff[row]] for coeff in cert['W_coefficients_0to6']]
            f = [R.dot(w, fc) for w in W]
            assert f == [R.one]+[R.zero]*6
            assert [R.dot(w, coordinate) for w in W[1:]] == [R.one]+[R.zero]*5
            wa = [[w[k] for k in a.a2] for w in W]
            wb = [[w[k] for k in a.b2] for w in W]
            z3 = [R.vsub([w[k] for k in a.a3], R.vmulscalar(lam, f[n]))
                  for n, w in enumerate(W)]
            V2, V3, v2b = [], [], []
            for n in range(7):
                V2.append(R.rowmat(R.vconv(wa, wb, n), C2))
                v2b.append([V2[n][k] for k in a.b3])
                extra = R.rowmat(R.vconv(v2b, z3, n), E3)
                first = R.svconv(f, V2, n)
                V3.append(R.vsub(R.vmul(first, ifp), R.rowmat(extra, C))+extra)
                assert V2[n] == [R.cv(z) for z in cert['V2_coefficients_0to6'][n][row]]
                assert V3[n] == [R.cv(z) for z in cert['V3_coefficients_0to6'][n][row]]
                section_entries += 199+325
            h = [R.rowmat(vv, H) for vv in V3]
            hc = [R.dot(vv, coordinate) for vv in h]
            assert hc == vals('Hc_coefficients_0to6') and R.unit(hc[0])
            for n in range(6):
                for c in range(73):
                    lhs = R.zero
                    for k in range(n+1):
                        lhs = R.add(lhs, R.mul(hc[k], R.scale(W[n-k+1][c], n-k+1)))
                    assert lhs == h[n][c], (disk, n, c)
                    ode_entries += 1

            # Replay the published homogeneous invariant definition by its
            # formal directional derivative, entirely with Python integers.
            zg = [R.rowmat(vv, G) for vv in V3]
            df = [R.dot(zz, fc) for zz in zg]
            za = [[zz[k] for k in a.a2] for zz in zg]
            zb = [[zz[k] for k in a.b2] for zz in zg]
            dz3 = [R.vsub([zz[k] for k in a.a3], R.vmulscalar(lam, df[n]))
                   for n, zz in enumerate(zg)]
            dV2, dV3, dv2b = [], [], []
            for n in range(7):
                dV2.append(R.rowmat(R.vadd(R.vconv(za, wb, n), R.vconv(wa, zb, n)), C2))
                dv2b.append([dV2[n][k] for k in a.b3])
                extra = R.rowmat(R.vadd(R.vconv(dv2b, z3, n), R.vconv(v2b, dz3, n)), E3)
                first = R.vadd(R.svconv(df, V2, n), R.svconv(f, dV2, n))
                dV3.append(R.vsub(R.vmul(first, ifp), R.rowmat(extra, C))+extra)
            vv = [R.dot(w, v) for w in W]
            aa = [R.dot(z, Av) for z in V3]
            dav = [R.dot(z, Av) for z in dV3]
            gv = [R.dot(z, v) for z in zg]
            bb = [R.scale(R.sub(y, z), pow(6, -1, R.m)) for y, z in
                  zip(R.product(vv, dav, 7), R.product(aa, gv, 7))]
            assert vv == vals('original_clearing_v_coefficients_0to6')
            assert aa == vals('Av_coefficients_0to6') and bb == vals('Bv3_coefficients_0to6')
            assert vv[0] == bb[0] == bb[1] == R.zero
            assert all(R.unit(z) for z in [vv[1], aa[0], bb[2]])
            uunit = R.product(R.power(bb[2:7], 2, 5),
                       R.invseries(R.product(R.power(aa[:5], 3, 5),
                                             R.power(vv[1:6], 3, 5), 5), 5), 5)
            u = [R.zero]+uunit[:4]
            denom = [R.scale(z, 27) for z in u]
            denom[0] = R.add(denom[0], (4, 0))
            j = [R.scale(z, 6912) for z in R.invseries(denom, 5)]
            assert uunit == vals('u_over_z_coefficients_0to4')
            assert u == vals('u_coefficients_0to4')
            assert u[:4] == vals('coarse_u_transport_coefficients_0to3')
            assert j == vals('j_coefficients_0to4') and j[0] == (1728, 0) and R.unit(j[1])
            womega = [R.rowmat(w, K1) for w in W[:3]]
            ihc = R.invseries(hc, 3)
            for n in range(3):
                om = R.svconv(ihc, womega, n)
                assert om == [R.cv(z) for z in t['canonical_differential_coefficients_0to2_mod47four'][n][row]]

            nb = [T.dot(z, sB) for z in V3[:4]]
            db = [T.dot(z, qB) for z in V2[:5]]
            cvt = lambda key: [T.cv(z[row][0]) for z in cert[key]]
            assert nb == cvt('eta_B_numerator_coefficients_0to3_mod47cubed')
            assert db == cvt('eta_B_denominator_coefficients_0to4_mod47cubed')
            assert db[0] == T.zero and T.unit(db[1])
            beta = T.product(T.product(nb, T.invseries([T.cv(z) for z in hc], 4), 4),
                             T.invseries(db[1:], 4), 4)
            assert beta[0] == T.one
            regular = beta[1:]
            assert regular == cvt('eta_B_regular_coefficients_0to2_mod47cubed')
            jj = [T.cv(z) for z in j]
            jp = [T.scale(jj[n+1], n+1) for n in range(3)]
            jpp = [T.scale(jj[n+2], (n+2)*(n+1)) for n in range(3)]
            junit = jj[1:]
            juprime = [T.scale(junit[n+1], n+1) for n in range(3)]
            logu = T.product(juprime, T.invseries(junit, 3), 3)
            logp = T.product(jpp, T.invseries(jp, 3), 3)
            logj = T.product(jp, T.invseries(jj, 3), 3)
            combined = [T.add(T.add(T.scale(logp[n], -4), T.scale(logj[n], 8*pow(3, -1, T.m))),
                              T.scale(T.sub(logu[n], regular[n]), 2)) for n in range(3)]
            assert logu == cvt('dlog_jminus1728_over_z_coefficients_0to2_mod47cubed')
            assert combined == cvt('regular_F2_combination_coefficients_0to2_mod47cubed')
            assert [T.scale(z, pow(2, -1, T.m)) for z in combined] == cvt('regular_F3_combination_coefficients_0to2_mod47cubed')
            records.append({'disk_id': disk, 'j_coefficients_0to4': j,
                            'eta_B_regular_coefficients': regular,
                            'regular_F2_combination_coefficients': combined,
                            'actual_residue_eta_B': 1, 'joint_polar_coefficient': 0,
                            'unit_Hc_and_jprime': [hc[0], j[1]]})
            print('INDEPENDENT_TRUE_CM4', disk, combined, flush=True)
    assert len(records) == 2 and ode_entries == 2*6*73 and section_entries == 2*7*(199+325)
    out = {
        'result': 'R554', 'certificate_sha256': sha(args.certificate),
        'generator_sha256': sha(args.generator), 'source_sha256': sha(__file__),
        'all876_projective_ODE_entries_replayed': True,
        'all7336_V2_V3_section_entries_reconstructed': True,
        'all_homogeneous_invariants_reconstructed_by_exact_directional_derivative': True,
        'both_actual_coarse_j_series_and_unit_tangents_replayed': True,
        'both_actual_eta_B_simple_poles_and_joint_cancellation_replayed': True,
        'both_all54_tiny_differentials_match_original_coordinate': True,
        'records': records, 'model_input_sha256': a.inputs,
        'scope': 'Independent Python integer-pair arithmetic reconstructs V2/V3, verifies the projective ODE and homogeneous scalar invariant formula, and recomputes the actual Laurent cancellation. The published exact model supplies coefficient matrices. No Norm, height constant or exclusion claim.',
        'actual_height_or_Norm_computed': False}
    args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
    print('PASS_R554_INDEPENDENT_INTEGER_AUDIT', sha(args.output), flush=True)


if __name__ == '__main__':
    main()
