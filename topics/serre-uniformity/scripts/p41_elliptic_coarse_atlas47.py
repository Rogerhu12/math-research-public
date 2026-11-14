#!/usr/bin/env python3
"""Recover actual elliptic coarse frames from the global Serre derivation.

No new 41-torsion enumeration is used.  The scalar invariants A*v and B*v^3
are reconstructed as honest homogeneous polynomials in the published W basis.
All cancellation below is division by the formal variable with certified zero
coefficients, followed by unit inversions, never division by 47.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time


def setup(folder):
    sys.path.insert(0, str(folder))
    from p41_supersingular_atlas47 import Atlas
    return Atlas(folder, folder/'data/p41_cleared_serre_derivative47_complete.json.gz')


class Series:
    def __init__(self, a, n):
        self.a, self.r, self.n = a, a.r, n

    def add(self, x, y):
        return [self.r.add(a, b) for a, b in zip(x, y)]

    def sub(self, x, y):
        return [self.r.sub(a, b) for a, b in zip(x, y)]

    def scale(self, x, c):
        return [self.a.scale(a, c) for a in x]

    def mul(self, x, y):
        out = []
        for n in range(min(self.n, len(x), len(y))):
            v = self.r.mul(x[0], y[n])
            for k in range(1, n+1):
                v = self.r.add(v, self.r.mul(x[k], y[n-k]))
            out.append(v)
        return out

    def inverse(self, x):
        out = [self.r.inverse_values(x[0])]
        for n in range(1, min(self.n, len(x))):
            v = self.r.mul(x[1], out[n-1])
            for k in range(2, n+1):
                v = self.r.add(v, self.r.mul(x[k], out[n-k]))
            out.append(self.r.neg(self.r.mul(out[0], v)))
        return out

    def power(self, x, n):
        assert n >= 1
        out = x
        for _ in range(n-1):
            out = self.mul(out, x)
        return out

    def compose(self, x, y, order=None):
        """Rowwise composition, including vector-valued x, y(0)=0."""
        r, np = self.r, self.a.np
        assert r.iszero(y[0])
        N = min(self.n, len(y), order or self.n)
        nrow, ncol = x[0][0].shape
        out = [r.zeros(nrow, ncol) for _ in range(N)]
        one = (np.ones((nrow, 1), dtype=np.int64), np.zeros((nrow, 1), dtype=np.int64))
        pw = [one]+[r.zeros(nrow, 1) for _ in range(N-1)]
        for k in range(min(N, len(x))):
            for j in range(N):
                out[j] = r.add(out[j], r.mul(x[k], pw[j]))
            pw = self.mul(pw, y[:N])
        return out

    def reversion(self, x, order):
        r = self.r
        assert r.iszero(x[0]) and self.a.np.all(r.units(x[1]))
        nrow = x[0][0].shape[0]
        z = [r.zeros(nrow, 1), r.inverse_values(x[1])]
        for n in range(2, order):
            z.append(r.zeros(nrow, 1))
            value = self.compose(x[:n+1], z, n+1)[n]
            z[n] = r.neg(r.mul(value, r.inverse_values(x[1])))
        comp = self.compose(x, z, order)
        assert r.iszero(comp[0])
        assert r.equal(comp[1], self.r.mul(x[1], r.inverse_values(x[1])))
        assert all(r.iszero(c) for c in comp[2:])
        return z


class ClassicalInvariants:
    """Homogeneous A*v (degree3), B*v^3 (degree6), in the actual basis."""
    def __init__(self, atlas):
        self.at, self.a, self.r = atlas, atlas.a, atlas.r
        self.v, self.G = atlas.v, atlas.G
        # At the source A=1.  Evaluation on820 points is injective on3L.
        values = self.r.mm(self.a.M['W'], self.v)
        self.Av = self.r.rows(values, self.a.M['P3'])
        assert self.r.equal(self.r.mm(self.a.M['V3'], self.Av), values)

    def section_series(self, W):
        a, r = self.a, self.r
        s = Series(a, len(W))
        f = [r.mm(w, a.fc) for w in W]
        Wa = [r.cols(w, a.a2) for w in W]
        Wb = [r.cols(w, a.b2) for w in W]
        V2 = [r.mm(c, a.C2) for c in s.mul(Wa, Wb)]
        residual = s.mul([r.cols(v, a.b3) for v in V2],
                         [r.sub(r.cols(w, a.a3), r.mul(ff, a.lam)) for w, ff in zip(W, f)])
        extra = [r.mm(c, a.E3) for c in residual]
        first = s.mul(f, V2)
        V3 = [r.hcat(r.sub(r.mul(c, a.ifP2), r.mm(e, a.C)), e)
              for c, e in zip(first, extra)]
        return V2, V3

    def directional_series(self, W, Z, V2=None):
        """d V3(W)[Z], with an independent formal directional variable."""
        a, r = self.a, self.r
        s = Series(a, len(W))
        if V2 is None:
            V2 = self.section_series(W)[0]
        f = [r.mm(w, a.fc) for w in W]
        df = [r.mm(w, a.fc) for w in Z]
        Wa, Wb = [r.cols(w, a.a2) for w in W], [r.cols(w, a.b2) for w in W]
        Za, Zb = [r.cols(w, a.a2) for w in Z], [r.cols(w, a.b2) for w in Z]
        dV2 = [r.mm(c, a.C2) for c in s.add(s.mul(Za, Wb), s.mul(Wa, Zb))]
        z = [r.sub(r.cols(w, a.a3), r.mul(ff, a.lam)) for w, ff in zip(W, f)]
        dz = [r.sub(r.cols(w, a.a3), r.mul(ff, a.lam)) for w, ff in zip(Z, df)]
        residual = s.add(s.mul([r.cols(v, a.b3) for v in dV2], z),
                         s.mul([r.cols(v, a.b3) for v in V2], dz))
        extra = [r.mm(c, a.E3) for c in residual]
        first = s.add(s.mul(df, V2), s.mul(f, dV2))
        return [r.hcat(r.sub(r.mul(c, a.ifP2), r.mm(e, a.C)), e)
                for c, e in zip(first, extra)]

    def series(self, W):
        a, r = self.a, self.r
        from p41_actual_differentials47 import Q
        s = Series(a, len(W))
        V2, V3 = self.section_series(W)
        vv = [r.mm(w, self.v) for w in W]
        av = [r.mm(v, self.Av) for v in V3]
        G = [r.mm(v, self.G) for v in V3]
        dav = [r.mm(v, self.Av) for v in self.directional_series(W, G, V2)]
        gv = [r.mm(g, self.v) for g in G]
        bv3 = s.scale(s.sub(s.mul(vv, dav), s.mul(av, gv)), pow(6, -1, Q))
        return {'v': vv, 'Av': av, 'Bv3': bv3, 'V2': V2, 'V3': V3}


def coarse(atlas, inv, kind, order=3):
    a, r = atlas.a, atlas.r
    from p41_actual_differentials47 import Q, digest
    if kind == 'CM4':
        W0 = r.from_json(a.cm4['coarse_point_values'])
        indices = a.cm4['elliptic_necklace_indices_1based']
        shift_b, coarse_exponent = 2, 2
    else:
        data = a.read('p41_cm3_makdisi47_certificate.json')
        W0 = r.from_json([data['coarse_evaluation_coefficients'][0]])
        indices = [data['CM_necklace_index_1based']]
        shift_b, coarse_exponent = 1, 3
    # Need b through degree order+shift_b, and one extra coordinate coefficient.
    J = a.local_jets(W0, order=order+shift_b, coordinate_seed=0)
    W = J['W']
    zseries = inv.series(W)
    v, av, b = zseries['v'], zseries['Av'], zseries['Bv3']
    assert r.iszero(v[0])
    assert all(r.iszero(c) for c in b[:shift_b])
    assert a.np.all(r.units(v[1])) and a.np.all(r.units(av[0]))
    assert a.np.all(r.units(b[shift_b]))
    s = Series(a, order+1)
    vv, bb = v[1:order+2], b[shift_b:order+shift_b+1]
    aa = av[:order+1]
    if kind == 'CM4':
        unit_u = s.mul(s.power(bb, 2), s.inverse(s.mul(s.power(aa, 3), s.power(vv, 3))))
        scale = s.mul(s.mul(aa, s.power(vv, 2)), s.inverse(bb))
    else:
        unit_u = s.mul(s.mul(s.power(aa, 3), s.power(vv, 3)), s.inverse(s.power(bb, 2)))
        scale = s.mul(bb, s.inverse(s.mul(s.power(aa, 2), vv)))
    uz = [r.zeros(W0[0].shape[0], 1)]+unit_u[:order]
    z_of_u = s.reversion(uz, order+1)
    reg_z = s.mul(W[:order+1], scale)
    reg_u = s.compose(reg_z, z_of_u, order+1)
    assert r.equal(reg_u[0], W0), 'The coarse frame is reconstructed with its exact scale'
    if kind == 'CM3':
        for k in range(3):
            assert r.equal(reg_u[k], r.from_json([data['coarse_evaluation_coefficients'][k]])), k
    tau = [n-1 for n in a.cm4['elliptic_frobenius_permutation_1based']] if kind == 'CM4' else [0]
    for value in reg_u:
        assert r.equal(r.mm(value, a.M['A1']), r.conjugate(r.rows(value, tau)))
    # Exact universal KS factors: at A=1, B=t, u=t^2 (CM4);
    # at B=1, A=t, u=t^3 (CM3).  Their constant frame values agree.
    beta0 = -3*pow(8, -1, Q)%Q if kind == 'CM4' else pow(18, -1, Q)
    z1 = r.mul(a.scale(r.mm(W0, a.fc), beta0), J['Hc'][0])
    assert r.equal(z_of_u[1], z1)
    return {
        'kind': kind, 'curve_A': 1 if kind == 'CM4' else 0,
        'curve_B': 0 if kind == 'CM4' else 1,
        'parameter': 'u=B^2' if kind == 'CM4' else 'u=A^3',
        'stack_frame': 'W_raw=B*W_coarse' if kind == 'CM4' else 'W_raw=A^2*W_coarse',
        'indices_1based': indices, 'coarse_order': len(reg_u)-1,
        'coarse_values': [r.to_json(w) for w in reg_u],
        'projective_coordinate': r.to_json(J['coordinate']),
        'projective_coordinate_of_u': [r.to_json(v) for v in z_of_u],
        'u_of_projective_coordinate': [r.to_json(v) for v in uz],
        'regular_scale_of_projective_coordinate': [r.to_json(v) for v in scale],
        'vanishing_orders': {'v': 1, 'Av': 0, 'Bv3': shift_b},
        'coarse_values_sha256': [digest(r.to_json(w)) for w in reg_u],
        'existing_CM3_coefficients_independently_recovered': kind == 'CM3',
        'exact_KS_first_coefficient_matches': True,
        'Frobenius_all_coarse_coefficients': True,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    start = time.monotonic()
    from_dir = args.script_dir.resolve()
    at = setup(from_dir)
    a, r = at.a, at.r
    from p41_actual_differentials47 import Q, digest, save
    inv = ClassicalInvariants(at)
    tests = []
    for ell, branch in [(2, 2), (3, 0), (3, 2), (3, 3)]:
        t = at.raw['operators'][str(ell)]['targets'][branch]
        A, B = at.curve_coordinates(t)
        W = r.from_json(t['evaluation_matrix'])
        d = inv.series([W])
        av_expected = at.matrix_scale(d['v'][0], A)
        bv3_expected = at.matrix_scale(r.mul(r.mul(d['v'][0], d['v'][0]), d['v'][0]), B)
        assert r.equal(d['Av'][0], av_expected)
        assert r.equal(d['Bv3'][0], bv3_expected)
        tests.append({'ell':ell, 'branch':branch, 'all_820_Av_values':True, 'all_820_Bv3_values':True})
    records = [coarse(at, inv, k, order=3) for k in ['CM4', 'CM3']]
    out = {
        'scope':'Actual elliptic coarse frames and scalar A/B invariants; no height or QC-root claim',
        'level':41, 'auxiliary_prime':47, 'precision':4, 'modulus':Q,
        'clearing_section':r.to_json(inv.v), 'Av_cubic_coefficients':r.to_json(inv.Av),
        'Av_cubic_coefficients_sha256':digest(r.to_json(inv.Av)),
        'Bv3_formula':'(v*d(Av)[G] - Av*(G*v))/6; G=v*delta(W)',
        'independent_model_checks':tests, 'elliptic_charts':records,
        'input_sha256':a.inputs, 'derivative_sha256':at.derivative_sha,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    h = save(args.output, out)
    print('COMPLETE', h, 'seconds', round(time.monotonic()-start,3), flush=True)


if __name__ == '__main__':
    main()
