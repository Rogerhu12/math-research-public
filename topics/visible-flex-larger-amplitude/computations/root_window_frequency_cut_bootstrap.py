#!/usr/bin/env python3
"""Finite frequency bootstrap of the existing R127 field and its true cut.

Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
The actual185 window caps and the old shared middle mass are simultaneous
constraints. Every arithmetic comparison is exact; exp uses outward Arb.
Only finite substitutions in an already proved fixed point are asserted.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx, fmpq as Q

MODES = list(range(2, 93, 2))
M = 34816
TAU = Q(18, 125)
RSTAR = Q(1, 2**34)
ZERO = Q(0)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def ex(v):
    if isinstance(v, Q):
        return v
    if isinstance(v, int):
        return Q(v)
    if isinstance(v, dict):
        return Q(int(v['numerator']), int(v['denominator']))
    m, e = int(v[0]), int(v[1])
    return Q(m)*Q(2)**e


def pack(value):
    x = value if isinstance(value, arb) else arb(value)
    if not x.is_finite() or x < 0:
        raise ArithmeticError('Every upper bound must be finite and nonnegative')
    x = x.upper()
    if x == 0:
        return [0, 0]
    m, e = map(int, x.man_exp())
    shift = max(0, m.bit_length()-128)
    if shift:
        m = -((-m)//2**shift)
        e += shift
    return [str(m), e]


def up(value):
    ans = ex(pack(value))
    if not isinstance(value, arb) and ans < value:
        raise ArithmeticError('Outward rounding moved down')
    return ans


def save(path, data):
    path = Path(path)
    if path.exists():
        raise FileExistsError(path)
    raw = (json.dumps(data, separators=(',', ':'))+'\n').encode()
    if str(path).endswith('.gz'):
        raw = gzip.compress(raw, compresslevel=9, mtime=0)
    if len(raw) >= 5_000_000:
        raise ArithmeticError('Partition output larger than5MB')
    path.write_bytes(raw)
    return dict(path=str(path), sha256=sha(path), bytes=len(raw))


def checked(record):
    if sha(record['path']) != record['sha256']:
        raise ArithmeticError('Actual frozen input changed: '+record['path'])
    return read(record['path'])


def support(coefficients, caps, mass):
    """Exact support of 0<=x_w<=caps_w, sum x_w<=mass; sparse pairs."""
    if mass < 0 or any(a < 0 for _, a in coefficients):
        raise ArithmeticError('Positive support requires positive data')
    left, result = mass, ZERO
    for w, a in sorted(coefficients, key=lambda p: p[1], reverse=True):
        if not a or not left:
            break
        take = min(left, caps[w])
        result += a*take
        left -= take
    return up(result)


class Bootstrap:
    def __init__(self, inputs):
        self.inputs = inputs
        self.exp_cache = {}
        self.joint = joint = checked(inputs['joint1200'])
        window = checked(inputs['window_caps'])
        sources = checked(inputs['low_sources'])
        low = checked(inputs['low_kernels'])
        nonlow = checked(inputs['nonlow'])
        centre = checked(inputs['low_spectrum'])
        if not (joint['all_gates'] and window['all_gates'] and sources['all_gates']
                and low['all_gates'] and nonlow['all_gates'] and centre['all_gates']):
            raise ArithmeticError('All original proven input gates are required')
        if not (window['same_existing_full_outer_fixed_point']
                and joint['complete_mean_and_inverse_retained']
                and window['all_complete_mean_inverse_and_source_materials_retained']):
            raise ArithmeticError('A complete original fixed point is required')
        partition = low['comparison_partition']
        if not (partition == sources['comparison_partition']
                == window['comparison_partition'] == nonlow['comparison_partition']):
            raise ArithmeticError('Actual25 comparison blocks changed')
        if joint['low_modes'] != MODES or joint['infinite_high_cutoff'] != M:
            raise ArithmeticError('Complete original frequency range changed')
        self.windows = [r['window'] for r in window['windows']]
        covered = [m for lo, hi in self.windows for m in range(lo, hi+1, 2)]
        if covered != list(range(94, M, 2)) or len(self.windows) != 185:
            raise ArithmeticError('Actual185 windows must partition every middle mode')
        self.window_of = {m: w for w, (lo, hi) in enumerate(self.windows) for m in range(lo, hi+1, 2)}
        self.u = [[ex(x) for x in row] for row in joint['low_mode_radii']]
        self.r = list(map(ex, joint['finite_radii']))
        self.h = list(map(ex, joint['high_radii']))
        if not (self.r == list(map(ex, window['retained_global_middle_mass_radii']))
                and self.h == list(map(ex, window['retained_global_high_mass_radii']))):
            raise ArithmeticError('The simultaneous global middle/high radii changed')
        self.v = [[ex(w['rows'][j]['actual_window_mass_upper']) for w in window['windows']] for j in range(25)]
        if any(not row['whole_window_mass_not_per_mode_sum'] for row in window['windows']):
            raise ArithmeticError('Each window must bound a whole l1 mass')
        if any(x < 0 or x > self.r[j] for j, row in enumerate(self.v) for x in row):
            raise ArithmeticError('An actual window cap is invalid')
        self.caps = [ex(r['bound']) for r in centre['final_caps']]
        if [r['mode'] for r in centre['final_caps']] != MODES or sum(self.caps, ZERO) >= 10:
            raise ArithmeticError('Same R101 true low centre required')
        self.V = [ex(r['V_max']) for r in nonlow['rows']]
        self.B = ex(nonlow['physical_high_conversion'])
        self.S = ex(nonlow['profile_to_V_upper'])
        self.R = ex(nonlow['profile_physical_upper'])
        self.b = [self.B if j == 5 else self.R if j == 21 else self.V[j] for j in range(25)]
        self.blocks = []
        self.read_records = []
        for j, rec in enumerate(sources['source_records']):
            a = checked(rec); self.read_records.append(rec)
            if not (a['index'] == j and a['modes'] == MODES
                    and a['C_times_high_exactly_zero'] and a['u_times_high_exactly_zero']
                    and ex(a['complete_T_physical_domain']) == RSTAR):
                raise ArithmeticError('An actual complete low source block changed')
            a['smin'] = Q(*map(int, a['sigma_min']))
            a['smax'] = Q(*map(int, a['sigma_max']))
            for key in ['C_times_u', 'C_times_middle', 'u_times_middle']:
                a[key] = [[ex(x) for x in row] for row in a[key]]
            for key in ['middle_squared', 'middle_high', 'high_squared']:
                a[key] = list(map(ex, a[key]))
            a['pairs'] = [(r['m']//2-1, r['k']//2-1, r['n']//2-1, ex(r['coefficient'])) for r in a['u_squared_terms']]
            self.blocks.append(a)
        self.targets = []
        for i, rec in enumerate(low['target_records']):
            target = checked(rec); self.read_records.append(rec)
            if target['target_block'] != i or target['modes'] != MODES:
                raise ArithmeticError('Actual original low target order changed')
            mats = [[[ZERO]*46 for _ in range(3)] for _ in range(25)]
            for row in target['kernels']:
                mats[row['source_block']][2-row['power']] = [ex(x['common_sigma']['P'])+ex(x['common_sigma']['K']) for x in row['mode_rows']]
            self.targets.append(self.convert(mats))
        cut = checked(low['cut_record']); self.read_records.append(low['cut_record'])
        if cut['modes'] != MODES or not cut['physical_F_rx_W_and_frame_paid_once']:
            raise ArithmeticError('Original46 axis cut kernels required')
        mats = [[[ZERO]*46 for _ in range(3)] for _ in range(25)]
        for row in cut['rows']:
            mats[row['source_block']][2-row['power']] = [ex(x['raw_original_axis_cut']) for x in row['mode_rows']]
        self.cut_kernels = self.convert(mats)
        self.qvv = self.build_vv()

    def exp(self, value):
        if value not in self.exp_cache:
            self.exp_cache[value] = up(arb(value).exp())
        return self.exp_cache[value]

    def convert(self, materials):
        result = []
        for j, (g, one, zero) in enumerate(materials):
            if j == 5:
                cross, square = [self.B*x for x in one], [self.B*self.B*x for x in zero]
            elif j == 21:
                cross = [min(self.S*x, self.R*y) for x, y in zip(g, one)]
                square = [min(self.S*self.S*x, self.S*self.R*y, self.R*self.R*z) for x, y, z in zip(g, one, zero)]
            else:
                cross, square = g[:], g[:]
            result.append((g, cross, square))
        return result

    def build_vv(self):
        """All possible positive difference-frequency window edges, once."""
        answers = []
        for j, a in enumerate(self.blocks):
            row = []
            for mi, m in enumerate(MODES):
                outer = []
                for w, (lo, hi) in enumerate(self.windows):
                    edges = []
                    for z in range(w, len(self.windows)):
                        zlo, zhi = self.windows[z]
                        nlo, nhi = max(lo, zlo-m), min(hi, zhi-m)
                        if zlo > hi+m:
                            break
                        if nlo <= nhi:
                            c = Q(5, 4)*self.exp(-2*nlo*a['smin'])
                            edges.append((z, c))
                    if edges:
                        outer.append((w, support(edges, self.v[j], self.r[j])))
                nested = support(outer, self.v[j], self.r[j])
                old = a['middle_squared'][mi]*self.r[j]**2
                row.append(up(min(nested, old)))
            answers.append(row)
        return answers

    def sources(self, u):
        result = []
        for j, a in enumerate(self.blocks):
            terms = {k: [ZERO]*46 for k in ['C_low', 'low_squared', 'low_middle', 'middle_squared', 'middle_high', 'high_squared']}
            for mi, m in enumerate(MODES):
                terms['C_low'][mi] = sum((c*x for c, x in zip(a['C_times_u'][mi], u[j])), ZERO)
                coeff = {}
                for ni, n in enumerate(a['middle_inputs']):
                    k = n-m
                    if 2 <= k <= 92:
                        c = a['C_times_middle'][mi][ni]+a['u_times_middle'][mi][ni]*u[j][k//2-1]
                        w = self.window_of[n]
                        coeff[w] = max(coeff.get(w, ZERO), c)
                terms['low_middle'][mi] = support(list(coeff.items()), self.v[j], self.r[j])
                terms['middle_squared'][mi] = self.qvv[j][mi]
                tailmass = min(self.r[j], sum((self.v[j][w] for w, (lo, hi) in enumerate(self.windows) if hi >= M-m), ZERO))
                terms['middle_high'][mi] = a['middle_high'][mi]*tailmass*self.h[j]
                terms['high_squared'][mi] = a['high_squared'][mi]*self.h[j]**2
            for mi, ki, ni, c in a['pairs']:
                terms['low_squared'][mi] += c*u[j][ki]*u[j][ni]
            for k in terms:
                terms[k] = list(map(up, terms[k]))
            q2 = [up(sum((terms[k][mi] for k in ['C_low', 'low_squared', 'low_middle', 'middle_squared']), ZERO)) for mi in range(46)]
            choices = []
            for di in range(5):
                delta = a['smin']*Q(di, 4)
                c = up(sum((x*self.exp(-m*(TAU-a['smax']+delta)) for m, x in zip(MODES, self.caps)), ZERO))
                ul = up(sum((x*self.exp(-m*delta) for m, x in zip(MODES, u[j])), ZERO))
                vl = support([(w, self.exp(-lo*delta)) for w, (lo, hi) in enumerate(self.windows)], self.v[j], self.r[j])
                hl = up(self.h[j]*self.exp(-M*delta))
                physical = up(self.V[j]*(c+ul+vl)+self.b[j]*hl)
                if not (0 < physical < RSTAR < Q(1, 128)):
                    raise ArithmeticError('A complete angular-loss physical domain failed')
                kt, t = 270*physical, ul+vl
                choices.append(dict(delta=delta, centre=c, low=ul, middle=vl, high=hl,
                    domain=physical, two=up(kt*(c*t+t*t/2)), cross=up(kt*(c+t)*hl), square=up(kt*hl*hl/2)))
            result.append(dict(Q2=q2, QR=terms['middle_high'], QRR=terms['high_squared'], terms=terms, T=choices))
        return result

    def T_value(self, src, kernels, mi):
        g, cross, square = kernels
        return up(min(self.exp(MODES[mi]*d['delta'])*(g[mi]*d['two']+cross[mi]*d['cross']+square[mi]*d['square']) for d in src['T']))

    def images(self, sources):
        out = []
        for kernels in self.targets:
            row = []
            for mi in range(46):
                v = ZERO
                for j, src in enumerate(sources):
                    g, cross, square = kernels[j]
                    v += (g[mi]*src['Q2'][mi]+cross[mi]*src['QR'][mi]+square[mi]*src['QRR'][mi]
                          +self.T_value(src, kernels[j], mi))
                row.append(up(v))
            out.append(row)
        return out

    def cut(self, sources):
        components = {k: [ZERO]*46 for k in ['C_low', 'low_squared', 'low_middle', 'middle_squared', 'middle_high', 'high_squared', 'complete_T']}
        T_shared = ZERO
        source_rows = []
        for j, src in enumerate(sources):
            kernels = self.cut_kernels[j]
            g, cross, square = kernels
            for name, vals in src['terms'].items():
                kg = cross if name == 'middle_high' else square if name == 'high_squared' else g
                for mi in range(46):
                    components[name][mi] += kg[mi]*vals[mi]
            per_mode = [self.T_value(src, kernels, mi) for mi in range(46)]
            for mi, v in enumerate(per_mode):
                components['complete_T'][mi] += v
            # One common complete-T source mass, paid once over all40 T modes.
            shared_candidates = []
            for d in src['T']:
                weighted_max = [max(k[mi]*self.exp(MODES[mi]*d['delta']) for mi in range(6, 46)) for k in kernels]
                shared_candidates.append(sum((k*d[name] for k, name in zip(weighted_max, ['two', 'cross', 'square'])), ZERO))
            shared = up(min(min(shared_candidates), sum(per_mode[6:], ZERO)))
            T_shared += shared
            source_rows.append(dict(source_block=j, T_common_mass_paid_once=pack(shared),
                T_separate_caps_sum=pack(sum(per_mode[6:], ZERO)),
                angular_loss_domains=[dict(delta=[str(d['delta'].p), str(d['delta'].q)], physical_domain=pack(d['domain'])) for d in src['T']]))
        values = [up(sum((v[mi] for v in components.values()), ZERO)) for mi in range(46)]
        S = max(values[:6])
        T = up(sum((sum(v[6:], ZERO) for k, v in components.items() if k != 'complete_T'), ZERO)+T_shared)
        return dict(mode_caps=[pack(v) for v in values], S_max=pack(S), T_l1=pack(T),
            complete_T_shared=pack(T_shared), source_rows=source_rows,
            component_mode_caps={k: [pack(up(x)) for x in v] for k, v in components.items()},
            component_T_l1_display={k: float(sum(v[6:], ZERO)) for k, v in components.items()},
            norm=pack(max(S, T)), norm_below_one_over1000=max(S, T)<Q(1, 1000))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--substitutions', type=int, default=4)
    args = ap.parse_args()
    ctx.prec = 256
    began = time.monotonic()
    if not (1 <= args.substitutions <= 64):
        raise ValueError('Explicit finite substitution count between1 and64 required')
    if list(args.out_prefix.parent.glob(args.out_prefix.name+'-*')):
        raise FileExistsError('Fresh complete output prefix required')
    args.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    inputs = read(args.inputs)
    b = Bootstrap(inputs)
    initial = [row[:] for row in b.u]
    u = initial
    records, history = [], []
    for iteration in range(args.substitutions):
        sources = b.sources(u)
        cut = b.cut(sources)
        image = b.images(sources)
        new = [[min(x, y) for x, y in zip(old, row)] for old, row in zip(u, image)]
        changed = sum(x != y for a, c in zip(u, new) for x, y in zip(a, c))
        body = dict(iteration=iteration, existing_field_bounds_before=[[pack(x) for x in row] for row in u],
            complete_low_images=[[pack(x) for x in row] for row in image],
            existing_field_bounds_after=[[pack(x) for x in row] for row in new],
            cut=cut, finite_substitution_only=True, original_mean_inverse_and_infinite_high_retained=True,
            original_radii_and_window_caps_used_simultaneously=True)
        rec = save(str(args.out_prefix)+f'-step{iteration:02d}.json.gz', body)
        records.append(rec)
        display = dict(iteration=iteration, updated_mode_caps=changed,
            cut_S=float(ex(cut['S_max'])), cut_T=float(ex(cut['T_l1'])),
            cut_component_T=cut['component_T_l1_display'],
            low_block_sum_display=[float(sum(row, ZERO)) for row in new])
        history.append(display)
        print(json.dumps(display, separators=(',', ':')), flush=True)
        u = new
    final_sources = b.sources(u)
    final_cut = b.cut(final_sources)
    result = dict(schema='R127-complete185-window-low-and-cut-finite-bootstrap-v1',
        author='/root (GPT-6 Astra Pro, AI-assisted)', source_sha256=sha(__file__),
        input_manifest_sha256=sha(args.inputs), inputs=inputs, actual_read_records=b.read_records,
        all_input_identity_and_domain_gates=True, same_existing_R127_field=True,
        finite_substitution_count=args.substitutions, step_records=records,
        final_low_caps=[[pack(x) for x in row] for row in u],
        retained_middle_radii=[pack(x) for x in b.r], retained_high_radii=[pack(x) for x in b.h],
        retained_window_caps=[[pack(x) for x in row] for row in b.v],
        final_cut=final_cut, history=history,
        parameter_cut_claimed=False, closed_surface_claimed=False,
        no_new_ODE_or_new_fixed_point=True, elapsed_seconds=time.monotonic()-began,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    record = save(str(args.out_prefix)+'-certificate.json.gz', result)
    summary = dict(certificate=record, source_sha256=sha(__file__),
        all_input_identity_and_domain_gates=True, actual_finite_substitutions=args.substitutions,
        final_cut_S=float(ex(final_cut['S_max'])), final_cut_T=float(ex(final_cut['T_l1'])),
        final_cut_norm_below_one_over1000=final_cut['norm_below_one_over1000'],
        elapsed_seconds=result['elapsed_seconds'], peak_rss_kib=result['peak_rss_kib'])
    save(str(args.out_prefix)+'-summary.json', summary)
    print(json.dumps(summary, separators=(',', ':')), flush=True)


if __name__ == '__main__':
    main()
