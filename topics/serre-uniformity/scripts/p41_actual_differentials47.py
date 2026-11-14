#!/usr/bin/env python3
"""Exact actual-section evaluations and rational-coordinate differential jets.

Reusable R194 recovery engine.  Every int64 matrix multiplication is delegated
to the published bounded implementation; no floating point arithmetic is used.
"""
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys

P = 47
Q = P**4
Q3 = P**3
PIN = {
    'p41_makdisi47_certificate.json.gz': 'c6ea2f89f4f64eec78039c5b14b6835295b045ea24ae26f885c4047b21e96222',
    'p41_cusp_divisors47_certificate.json.gz': 'ae902f25e6d3674b6d474a70ee12a925c0934c198eff94581cfd5dbba30023fb',
    'p41_cm4_divisor47_certificate.json': 'f98b13cbc7afb3ed5d8b2f9249fbe815198b478b23559c319c5ba56b6bd83540',
    'p41_group47_checkpoint.json.gz': '4f982a4801332f9eff196ff9e9f866883b01014579896c20e65d044530b8b655',
    'p41_evaluation_jets47_checkpoint.json.gz': 'a4ff695e00a7dc7d662f3db0d675549852bc7f3490b5c34d3a18dd98a7528b5d',
    'p41_local47_torsion_certificate.json': '6384cdce4d6c885f3d2cf706eda2d9af0a8a85d103da42ec6535977aaddc2253',
    'p41_hecke3_abel_bases_checkpoint.json.gz': '2c0c16acee560af04582de86e345fe3ded57c8c0d5f8c5f56b2631aaf00e3a8d',
    'p41_hecke3_formal_height47_compact.json.gz': '2be64539b101b8f4363d14e813571e5853fb7b9163dbd21a171ab630674a3800',
    'p41_miller_completion47_compact.json.gz': '69a33e8c944447e439804a842f418ea2f4e04b03ca5ccc8691a396e96036ffa0',
    'p41_formal47_log_compact.json.gz': '19dfec0db35016d2ac1f2750a134290d9084138581f538bda083b5b1b112090b',
    'p41_cm16_hecke47_verified.json.gz': 'a387489a44357abc78811de1bace6af2d4e42b77c3561f2ef18269e32996bcc2',
    'p41_cm36_hecke47_raw.json.gz': '3ea9d90b3889ef835fc0254673b9358841ee597d37e2a38622906356ed4bd495',
    'p41_hecke47_compact.json.gz': 'fc47c5a88596e57d21461acd08a9a865808b54b579ecc5dd06d9819512fc49b8',
}


def digest(data):
    return hashlib.sha256(json.dumps(data, separators=(',', ':')).encode()).hexdigest()


def flat(v):
    return [x[0] if len(x) == 1 else x for x in v]


def report(text):
    print(text+'; maxRSS MiB='+str(round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2)), flush=True)


def save(path, obj):
    raw = (json.dumps(obj, sort_keys=True, indent=2)+'\n').encode()
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(gzip.compress(raw, mtime=0) if path.name.endswith('.gz') else raw)
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ActualModel:
    def __init__(self, script_dir, derivatives=True):
        self.folder = Path(script_dir).resolve()
        sys.path.insert(0, str(self.folder))
        import numpy as np
        import p41_r2_matrix as r
        from p41_group_operations47 import load_sources, make_model
        from p41_cm4_divisor47 import kernel
        self.np, self.r, self.kernel = np, r, kernel
        self.inputs = {}
        sources, hashes = load_sources(self.folder/'data')
        for name, h in hashes.items():
            assert h == PIN[name], name
        self.inputs.update(hashes)
        self.model, self.cusp, self.cm4, self.group = sources
        self.M = make_model(sources)
        self.K1 = r.from_json(kernel(73, self.cusp['cusp_rank_columns_1based'], self.cusp['cusp_free_columns_1based'], self.cusp['canonical_kernel_block']))
        self.fc = r.mm(self.K1, r.column(self.cusp['canonical_coefficients']))
        self.f = r.mm(self.M['W'], self.fc)
        assert np.all(r.units(self.f))
        self.a2, self.b2 = zip(*[(a-1, b-1) for a, b in self.cusp['square_basis_monomials_1based']])
        self.a3, self.b3 = zip(*[(a-1, b-1) for a, b in self.group['cubic_selected_pairs_1based']])
        self.C2 = r.from_json(self.cusp['square_basis_inverse'])
        self.E3 = r.from_json(self.group['cubic_extra_inverse'])
        old = [self.M['P2'][b] for b in self.b3]
        self.lam = r.mul((self.M['W'][0][old, self.a3][None, :], self.M['W'][1][old, self.a3][None, :]),
                         r.inverse_values((self.f[0][old].T, self.f[1][old].T)))
        self.ifP2 = r.inverse_values((self.f[0][self.M['P2']].T, self.f[1][self.M['P2']].T))
        self.C = r.rows(r.mul(r.mul(self.f, self.M['V2']), self.ifP2), [n-1 for n in self.group['cubic_extra_rows_1based']])
        if derivatives:
            d = self.read('p41_evaluation_jets47_checkpoint.json.gz')
            WD = r.from_json(d['evaluation_derivatives'])
            fd = r.mm(WD, self.fc)
            Hv = self.scale(r.sub(r.mul(WD, self.f), r.mul(self.M['W'], fd)), -27652*pow(3, -1, Q))
            self.H = r.rows(Hv, self.M['P3'])
            assert r.equal(r.mm(self.M['V3'], self.H), Hv)
            assert r.iszero(r.mm(self.H, self.fc))
            self.H_sha = digest(r.to_json(self.H))
            assert self.H_sha == '475ebf071503f2f12285a041c88dfc5ab290a7953aba72df9df2cf43cf5f0988'
            del d, WD, fd, Hv
        report('Actual model and derivation verified')

    def read(self, name):
        raw = (self.folder/'data'/name).read_bytes()
        h = hashlib.sha256(raw).hexdigest()
        if name in PIN:
            assert h == PIN[name], name
        self.inputs[name] = h
        return json.loads(gzip.decompress(raw) if name.endswith('.gz') else raw)

    @staticmethod
    def scale(A, c, q=Q):
        c %= q
        return tuple(x*c % q for x in A)

    @staticmethod
    def reduce(A, q):
        return tuple(x % q for x in A)

    def evaluate(self, W):
        r = self.r
        f = r.mm(W, self.fc)
        V2 = r.mm(r.mul(r.cols(W, self.a2), r.cols(W, self.b2)), self.C2)
        raw = r.mul(r.cols(V2, self.b3), r.sub(r.cols(W, self.a3), r.mul(f, self.lam)))
        extra = r.mm(raw, self.E3)
        V3 = r.hcat(r.sub(r.mul(r.mul(f, V2), self.ifP2), r.mm(extra, self.C)), extra)
        return V2, V3

    def rational_coordinate(self, seed=0):
        r = self.r
        c = r.cols(self.M['A1'], [seed])
        c[0][seed, 0] = (c[0][seed, 0]+1) % Q
        assert r.equal(r.mm(self.M['A1'], r.conjugate(c)), c)
        return c

    def local_jets(self, W0, order=3, coordinate_seed=0):
        r, np = self.r, self.np
        npoints = W0[0].shape[0]
        c = self.rational_coordinate(coordinate_seed)
        f0 = r.mm(W0, self.fc)
        assert np.all(r.units(f0))
        ws = [r.mul(W0, r.inverse_values(f0))]
        v2, v3, hs, hc, hi = [], [], [], [], []
        for n in range(order+1):
            raw = r.zeros(npoints, 199)
            for k in range(n+1):
                raw = r.add(raw, r.mul(r.cols(ws[k], self.a2), r.cols(ws[n-k], self.b2)))
            v2.append(r.mm(raw, self.C2))
            raw = r.zeros(npoints, 126)
            for k in range(n+1):
                raw = r.add(raw, r.mul(r.cols(ws[k], self.a3), r.cols(v2[n-k], self.b3)))
            raw = r.sub(raw, r.mul(r.cols(v2[n], self.b3), self.lam))
            extra = r.mm(raw, self.E3)
            v3.append(r.hcat(r.sub(r.mul(v2[n], self.ifP2), r.mm(extra, self.C)), extra))
            hs.append(r.mm(v3[n], self.H))
            hc.append(r.mm(hs[n], c))
            if n == 0:
                assert np.all(r.units(hc[0]))
                hi.append(r.inverse_values(hc[0]))
            else:
                t = r.zeros(npoints, 1)
                for k in range(1, n+1):
                    t = r.add(t, r.mul(hc[k], hi[n-k]))
                hi.append(r.neg(r.mul(t, hi[0])))
            if n < order:
                t = r.zeros(npoints, 73)
                for k in range(n+1):
                    t = r.add(t, r.mul(hs[k], hi[n-k]))
                t = self.scale(t, pow(n+1, -1, Q))
                assert r.iszero(r.mm(t, self.fc))
                assert r.equal(r.mm(t, c), r.column([[int(n == 0), 0]]*npoints))
                ws.append(t)
        return {'W': ws, 'V2': v2, 'V3': v3, 'H': hs, 'Hc': hc, 'inverse_Hc': hi,
                'coordinate': c, 'f0': f0}

    def product_space(self, U, expected):
        """Generate W*U using one 73-column block, then immediately compress."""
        r = self.r
        selected = r.zeros(820, 0)
        history = []
        for k in range(U[0].shape[1]):
            V = r.hcat(selected, r.mul(self.M['W'], r.cols(U, [k])))
            rr, cc = r.rank_pivots(V)
            rank = len(rr)
            history.append(rank)
            V = r.cols(V, cc)
            selected = r.mm(V, r.inverse_matrix(r.rows(V, rr)))
            assert r.equal(r.rows(selected, rr), r.eye(rank))
            assert r.equal(r.mm(self.M['V3'], r.rows(selected, self.M['P3'])), selected)
            report('Product block '+str(k+1)+': rank '+str(rank)+' / '+str(expected))
            if rank == expected:
                return selected, rr, history
            assert rank < expected
        raise AssertionError(('product rank', history, expected))

    def field_setup(self):
        if hasattr(self, 'field_polynomial'):
            return
        r, np = self.r, self.np
        t = self.read('p41_local47_torsion_certificate.json')
        self.field_polynomial = np.asarray(t['field_polynomial_ascending'], dtype=np.int64)
        assert len(self.field_polynomial) == 81 and self.field_polynomial[-1] == 1
        self.ii = np.asarray(self.model['sqrt_minus_one_lift'], dtype=np.int64)
        assert 80*(Q-1)**2 < 2**63
        basis = []
        for k in range(40):
            e = np.zeros(80, dtype=np.int64)
            e[k] = 1
            basis.append(e)
        basis += [self.field_mul(self.ii, a) for a in basis[:40]]
        E = np.stack(basis, axis=1)
        inv = r.inverse_matrix((E, np.zeros_like(E)))
        assert not np.any(inv[1])
        self.field_basis_inverse = inv[0]

    def field_mul(self, a, b):
        out = self.np.convolve(a, b) % Q
        for k in range(158, 79, -1):
            c = int(out[k])
            if c:
                out[k-80:k] = (out[k-80:k]-c*self.field_polynomial[:-1]) % Q
        return out[:80]

    def field_rows(self, values, C):
        a = self.np.asarray(values, dtype=self.np.int64)
        assert a.shape[0] == C[0].shape[0] <= 820
        re, im = C[0].T@a % Q, C[1].T@a % Q
        return [(x+self.field_mul(self.ii, y)) % Q for x, y in zip(re, im)]

    def field_coordinates(self, values):
        a = self.np.asarray(values, dtype=self.np.int64)
        c = a@self.field_basis_inverse.T % Q
        return c[:, :40].T.copy(), c[:, 40:].T.copy()

    def cusp_evaluations(self, index):
        self.field_setup()
        cw = self.np.asarray(self.cusp['cusp_values'][index], dtype=self.np.int64)
        z = self.field_rows(cw, self.fc)
        assert not self.np.any(z)
        V2 = self.field_rows([self.field_mul(cw[a], cw[b]) for a, b in zip(self.a2, self.b2)], self.C2)
        extra = self.field_rows([self.field_mul(cw[a], V2[b]) for a, b in zip(self.a3, self.b3)], self.E3)
        V3 = [(-x) % Q for x in self.field_rows(extra, self.C)]+extra
        return self.field_coordinates(V2), self.field_coordinates(V3)
