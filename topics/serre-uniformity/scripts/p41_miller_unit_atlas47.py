#!/usr/bin/env python3
"""Evaluate the saved 454-step Miller SLP in integral local unit frames.

No Jacobian group operation is repeated.  The projective jet provider supplies
actual local section germs.  Weierstrass factors are retained and checked along
every step; unit logarithms are combined with exact precomputed SLP weights.
"""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time

P = 47
Q = P**4
ZERO, ONE = (0, 0), (1, 0)


def add(a, b): return ((a[0]+b[0]) % Q, (a[1]+b[1]) % Q)
def neg(a): return (-a[0] % Q, -a[1] % Q)
def sub(a, b): return add(a, neg(b))
def mul(a, b): return ((a[0]*b[0]-a[1]*b[1]) % Q, (a[0]*b[1]+a[1]*b[0]) % Q)
def scale(a, n): return (a[0]*n % Q, a[1]*n % Q)
def inv(a):
    n = pow((a[0]*a[0]+a[1]*a[1]) % Q, -1, Q)
    return (a[0]*n % Q, -a[1]*n % Q)
def unit(a): return (a[0]*a[0]+a[1]*a[1]) % P != 0


def power(a, e):
    if e < 0: return power(inv(a), -e)
    out = ONE
    while e:
        if e & 1: out = mul(out, a)
        a = mul(a, a)
        e >>= 1
    return out


def log_unit(a):
    assert unit(a)
    z = sub(power(a, P*P-1), ONE)
    assert all(x % P == 0 for x in z)
    return scale(add(sub(z, scale(mul(z, z), pow(2, -1, Q))),
                     scale(mul(mul(z, z), z), pow(3, -1, Q))),
                 pow(P*P-1, -1, Q))


def poly_mul(a, b):
    out = [ZERO]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] = add(out[i+j], mul(x, y))
    return out


def poly_div(a, b):
    a = [tuple(x) for x in a]
    b = [tuple(x) for x in b]
    assert b[-1] == ONE
    e = len(b)-1
    if len(a) < len(b): return [ZERO], a+[ZERO]*(e-len(a))
    out = [ZERO]*(len(a)-e)
    for k in range(len(a)-1, e-1, -1):
        out[k-e] = a[k]
        for j in range(e+1): a[k-e+j] = sub(a[k-e+j], mul(out[k-e], b[j]))
    return out, a[:e]


def exact_quotient(a, b):
    out, rem = poly_div(a, b)
    assert all(x == ZERO for x in rem), ('distinguished divisor mismatch', a, b, rem)
    while len(out) > 1 and out[-1] == ZERO: out.pop()
    assert out[-1] == ONE
    return out


def evaluate(coeff, z):
    out = ZERO
    for a in reversed(coeff): out = add(a, mul(z, out))
    return out


def flat(coeff): return [x[0] if len(x) == 1 else x for x in coeff]


class NeedMoreJets(Exception):
    pass


def prepare_series(germ):
    """Exact W and the first four coefficients of U in germ=W*U."""
    from p41_weierstrass_unit47 import prepare_unit
    degree = next((i for i, a in enumerate(germ) if unit(a)), None)
    if degree is None or 4*degree+3 >= len(germ):
        raise NeedMoreJets((degree, len(germ)-1))
    if degree == 0: return [ONE], germ[:4], 0
    prepared = prepare_unit(germ, degree=degree)
    W = [tuple(x) for x in prepared['weierstrass_coefficients']]
    quotient, rem = poly_div(germ[:4*degree+4], W)
    assert all(a == ZERO for a in rem)
    U = quotient[:4]
    assert len(U) == 4 and U[0] == tuple(prepared['unit_constant'])
    assert unit(U[0])
    return W, U, degree


def logarithm_series(U):
    v = inv(U[0])
    a, b, c = [mul(x, v) for x in U[1:4]]
    return [log_unit(U[0]), a,
            sub(b, scale(mul(a, a), pow(2, -1, Q))),
            add(sub(c, mul(a, b)), scale(mul(mul(a, a), a), pow(3, -1, Q)))]


def slp_weights(steps):
    weights = []
    negative = 0
    e = 1
    for step in steps:
        sign = 1 if e > 0 else -1
        if step['operation'] == 'double':
            factor = -2
            e = -2*e
        else:
            assert step['operation'] == 'add'
            factor = -1
            e = -(e+sign)
        weights = [factor*w for w in weights]
        negative *= factor
        if factor == -1 and sign == -1: negative += 1
        weights.append(-1)
        assert (1 if e > 0 else -1) == step['sign']
    return weights, negative, e


class MillerUnitAtlas:
    def __init__(self, a):
        self.a, self.r, self.np = a, a.r, a.np
        r = self.r
        from p41_formal47_multiply import point_hash
        self.slp = a.read('p41_poincare_miller_jets47_saved.json.gz')
        self.completion = a.read('p41_miller_completion47_compact.json.gz')
        self.bases = a.read('p41_hecke3_abel_bases_checkpoint.json.gz')
        self.formal = a.read('p41_hecke3_formal_height47_compact.json.gz')
        assert len(self.slp['steps']) == 454 and self.slp['bits_done'] == 304
        assert point_hash(r.from_json(self.slp['point_coordinates']),
                          r.from_json(self.slp['point_frobenius'])) == self.slp['point_sha256']
        assert self.slp['point_sha256'] == self.completion['old_point_sha256']
        weights, self.negative_weight, self.multiplier = slp_weights(self.slp['steps'])
        assert self.multiplier == int(self.slp['target_multiplier'])
        self.weights = weights
        self.weight_column = r.column([[w % Q, 0] for w in weights])
        co = []
        for step in self.slp['steps']:
            data = step['principal_section_coefficients']
            digest = hashlib.sha256(json.dumps(data, separators=(',', ':')).encode()).hexdigest()
            assert digest == step['principal_coefficient_sha256']
            co.append(r.column(flat(data)))
        self.coefficients = r.hcat(*co)
        self.fixed_coefficients = {
            'negative': ('V2', r.mm(a.M['B'], r.column(a.group['negative_flip_section_seeds_and_coefficients'][0][1]))),
            'old': ('V2', r.column(flat(self.completion['endpoint_transfer']['old_section_coefficients']))),
            'new': ('V2', r.column(flat(self.completion['endpoint_transfer']['new_section_coefficients']))),
            'v0': ('W', r.column(flat(self.bases['families'][0]['v_coefficients']))),
            'fc': ('W', a.fc),
        }
        self.ideals = {
            'initial': a.M['B'],
            'negative': r.from_json(a.kernel(199, a.group['negative_rank_columns_1based'],
                                           a.group['negative_free_columns_1based'], a.group['negative_kernel_block'])),
            'current': r.from_json(self.slp['point_coordinates']),
        }
        family = self.formal['families'][0]
        self.physical_displacements = dict(zip(family['points_1based'],
                                              [tuple(x) for x in family['actual_parameters'][0]]))

    @staticmethod
    def germ(values, point, col):
        return [(int(x[0][point, col]), int(x[1][point, col])) for x in values]

    def prepare_ideal(self, values, point):
        degrees = []
        for col in range(73):
            germ = self.germ(values, point, col)
            degrees.append(next((n for n, z in enumerate(germ) if unit(z)), 10**9))
        degree = min(degrees)
        if 4*degree >= len(values): raise NeedMoreJets(('ideal', degree, len(values)-1))
        witness = degrees.index(degree)
        from p41_weierstrass_unit47 import prepare_unit
        prepared = prepare_unit(self.germ(values, point, witness), degree=degree)
        W = [tuple(x) for x in prepared['weierstrass_coefficients']]
        if degree:
            for col in range(73):
                rem = poly_div(self.germ(values, point, col)[:4*degree], W)[1]
                assert all(v == ZERO for v in rem), ('ideal column', point, col)
        return W, witness+1

    def section_data(self, values):
        """Vectorized unit logarithms, with explicit preparation at every zero."""
        r, np = self.r, self.np
        points, columns = values[0][0].shape
        bad = np.argwhere(~r.units(values[0]))
        U = [(x[0].copy(), x[1].copy()) for x in values[:4]]
        W = {}
        hist = [Counter({0: columns}) for _ in range(points)]
        for point, col in bad.tolist():
            w, u, degree = prepare_series(self.germ(values, point, col))
            W[(point, col)] = w
            hist[point][0] -= 1
            hist[point][degree] += 1
            for n in range(4):
                U[n][0][point, col], U[n][1][point, col] = u[n]
        assert np.all(r.units(U[0]))
        iu = r.inverse_values(U[0])
        aa, bb, cc = [r.mul(x, iu) for x in U[1:4]]
        ll = [r.zeros(points, columns), aa,
              r.sub(bb, self.a.scale(r.mul(aa, aa), pow(2, -1, Q))),
              r.add(r.sub(cc, r.mul(aa, bb)), self.a.scale(r.mul(r.mul(aa, aa), aa), pow(3, -1, Q)))]
        # Iwasawa logarithm of all unit constants: all products remain in R2.
        one = (np.ones((points, columns), dtype=np.int64), np.zeros((points, columns), dtype=np.int64))
        out, cur, e = one, U[0], P*P-1
        while e:
            if e & 1: out = r.mul(out, cur)
            cur = r.mul(cur, cur)
            e >>= 1
        z = r.sub(out, one)
        assert not np.any(z[0] % P) and not np.any(z[1] % P)
        z2, z3 = r.mul(z, z), r.mul(r.mul(z, z), z)
        ll[0] = self.a.scale(r.add(r.sub(z, self.a.scale(z2, pow(2, -1, Q))),
                                  self.a.scale(z3, pow(3, -1, Q))), pow(P*P-1, -1, Q))
        return ll, W, hist

    def process_chart(self, chart, point_metadata, physical_z=None):
        """Return one certified batch; metadata order follows chart rows."""
        r = self.r
        number = chart['W'][0][0].shape[0]
        assert len(point_metadata) == number
        step_values = [r.mm(v, self.coefficients) for v in chart['V3']]
        logs, step_W, hist = self.section_data(step_values)
        combined = [r.mm(ll, self.weight_column) for ll in logs]
        fixed = {}
        for name, (basis, coeff) in self.fixed_coefficients.items():
            values = [r.mm(v, coeff) for v in chart[basis]]
            ll, ww, _ = self.section_data(values)
            fixed[name] = (ll, ww)
        weights = {'negative': self.negative_weight, 'old': 1, 'v0': 1,
                   'new': -1, 'fc': -self.multiplier}
        for name, weight in weights.items():
            for n in range(4): combined[n] = r.add(combined[n], self.a.scale(fixed[name][0][n], weight))
        ideal_values = {name: [r.mm(v, coeff) for v in chart['V2']] for name, coeff in self.ideals.items()}
        records = []
        for point in range(number):
            meta = point_metadata[point]
            wi, iw = self.prepare_ideal(ideal_values['initial'], point)
            wn, nw = self.prepare_ideal(ideal_values['negative'], point)
            wf, fw = self.prepare_ideal(ideal_values['current'], point)
            getW = lambda key: fixed[key][1].get((point, 0), [ONE])
            assert wn == exact_quotient(getW('negative'), wi)
            current, e = wi, 1
            for k, step in enumerate(self.slp['steps']):
                sign = 1 if e > 0 else -1
                if step['operation'] == 'double':
                    other, e = current, -2*e
                else:
                    other, e = (wi if sign == 1 else wn), -(e+sign)
                current = exact_quotient(step_W.get((point, k), [ONE]), poly_mul(current, other))
            assert e == self.multiplier and current == wf
            top = poly_mul(wf, getW('new'))
            bottom = poly_mul(getW('old'), getW('v0'))
            zcoeff = None
            displacement = None
            if physical_z is not None:
                zcoeff = self.germ(physical_z, point, 0)
                assert zcoeff[0] == ZERO and unit(zcoeff[1])
            if meta['kind'] == 'CM4':
                assert wi == poly_mul([ZERO, ONE], getW('fc'))
                assert top == bottom
            else:
                assert wi == getW('fc'), ('initial and canonical differ', meta, wi, getW('fc'))
                if meta['kind'] == 'ordinary' and int(meta['reference']) == 9 and meta['necklace_index_1based'] in self.physical_displacements:
                    assert zcoeff is not None and len(zcoeff) >= 5
                    ti = self.physical_displacements[meta['necklace_index_1based']]
                    zi = evaluate(zcoeff, ti)
                    assert poly_mul(top, [ZERO, ONE]) == poly_mul(bottom, [neg(zi), ONE]), ('D0 projective factor', meta)
                    displacement = {'physical_t': ti, 'projective_z': zi}
                else:
                    assert top == bottom, ('unexpected endpoint divisor', meta, top, bottom)
            rec = dict(meta)
            rec.update({'unit_log_coefficients': self.germ(combined, point, 0),
                        'initial_W': wi, 'negative_W': wn, 'current_W': wf,
                        'fixed_W': {k: getW(k) for k in fixed},
                        'ideal_witnesses_1based': [iw, nw, fw],
                        'all_ideal_columns_checked': 73,
                        'all_454_distinguished_steps_checked': True,
                        'section_degree_histogram': dict(sorted(hist[point].items())),
                        'physical_to_projective_coefficients': zcoeff,
                        'D0_displacement': displacement})
            records.append(rec)
        return records


def save(path, data):
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    out = gzip.compress(raw, mtime=0) if path.name.endswith('.gz') else raw
    temp = path.with_name(path.name+'.writing')
    temp.write_bytes(out)
    temp.replace(path)
    return hashlib.sha256(out).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--helper-dir', type=Path, required=True)
    ap.add_argument('--output-dir', type=Path, required=True)
    ap.add_argument('--references', default='9,10,44,0,36,CM4,CM3')
    ap.add_argument('--batch-size', type=int, default=64)
    ap.add_argument('--jet-order', type=int, default=27)
    ap.add_argument('--max-batches', type=int)
    args = ap.parse_args()
    sys.path[:0] = [str(args.script_dir.resolve()), str(args.helper_dir.resolve())]
    from p41_projective_jet_frames47 import ProjectiveJetFrames, install_exact_float_mm
    import p41_r2_matrix as matrix_ring
    install_exact_float_mm(matrix_ring)
    from p41_elliptic_coarse_atlas47 import setup
    from p41_scalar_primitive_atlas47 import ScalarPrimitiveAtlas
    from p41_actual_differentials47 import digest
    at = setup(args.script_dir.resolve())
    a, r = at.a, at.r
    primitives = ScalarPrimitiveAtlas(at, args.script_dir/'data/p41_elliptic_coarse_atlas47_verified.json.gz')
    miller = MillerUnitAtlas(a)
    provider = ProjectiveJetFrames(a)
    started = time.monotonic()
    batches = 0
    for ref in args.references.split(','):
        path = args.output_dir/('p41_Miller_unit_atlas_'+ref+'47.json.gz')
        if ref in ('CM4', 'CM3'):
            # The exact coarse label order and values come from R208.
            coarse_data = next(x for x in primitives.coarse['elliptic_charts'] if x['kind'] == ref)
            raw = [r.from_json(v) for v in coarse_data['coarse_values']]
            W0 = raw[0]
            labels = coarse_data['indices_1based']
            kind = ref
        else:
            j = int(ref)
            raw, ordinary, patches, _ = primitives.ordinary_jets(j, order=4)
            assert len(raw) == 5
            W0 = r.rows(raw[0], ordinary)
            raw = [r.rows(v, ordinary) for v in raw]
            labels = [i+1 for i in ordinary]
            kind = 'ordinary'
        if path.exists():
            result = json.loads(gzip.decompress(path.read_bytes()))
            assert result['reference'] == ref and result['multiplier'] == str(miller.multiplier)
            assert result['SLP_sha256'] == a.inputs['p41_poincare_miller_jets47_saved.json.gz']
        else:
            result = {'reference': ref, 'precision': 4, 'modulus': Q,
                      'multiplier': str(miller.multiplier), 'SLP_steps': 454,
                      'SLP_sha256': a.inputs['p41_poincare_miller_jets47_saved.json.gz'],
                      'SLP_weights_mod47_fourth': [w % Q for w in miller.weights],
                      'SLP_negative_weight_mod47_fourth': miller.negative_weight % Q,
                      'expected_labels_1based': labels, 'charts': [], 'records': [], 'complete': False}
        done = {x['necklace_index_1based'] for x in result['records']}
        remaining = [i for i, label in enumerate(labels) if label not in done]
        if not remaining:
            assert result['complete']
            continue
        # Each provider batch is independent and can be resumed by label.
        source0 = r.rows(W0, remaining)
        source_raw = [r.rows(v, remaining) for v in raw]
        for chart in provider.iter_charts(source0, order=args.jet_order, max_points=args.batch_size, label=ref):
            I = chart['indices_0based']
            selected = [remaining[i] for i in I]
            meta = [{'kind': kind, 'reference': ref, 'necklace_index_1based': labels[i]} for i in selected]
            z = provider.physical_to_chart(source_raw, chart, order=4 if kind == 'ordinary' else 3)
            records = miller.process_chart(chart, meta, z)
            chartid = len(result['charts'])
            for rec in records: rec['chart_index_0based'] = chartid
            result['charts'].append({'frame': r.to_json(chart['frame']),
                                     'coordinate': r.to_json(chart['coordinate']),
                                     'jet_order': args.jet_order,
                                     'labels_1based': [x['necklace_index_1based'] for x in records],
                                     'frame_derivation_certificate': {
                                         'source820_identity_verified': chart['frame_source820_verified'],
                                         'frame_kind': chart['frame_kind'],
                                         'coordinate_candidate': chart['coordinate_candidate']},
                                     'W_jets_sha256': [digest(r.to_json(v)) for v in chart['W']]})
            result['records'].extend(records)
            result['complete'] = len(result['records']) == len(labels)
            result['input_sha256'] = a.inputs
            result['generating_source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
            result['jet_helper_sha256'] = hashlib.sha256((args.helper_dir/'p41_projective_jet_frames47.py').read_bytes()).hexdigest()
            sha = save(path, result)
            batches += 1
            maxe = max(max(map(int, x['section_degree_histogram'])) for x in records)
            print(ref, len(result['records']), '/', len(labels), 'max_order', maxe,
                  'seconds', round(time.monotonic()-started, 2), 'sha', sha, flush=True)
            if args.max_batches and batches >= args.max_batches: return


if __name__ == '__main__':
    main()
