#!/usr/bin/env python3
"""Full1200-component positive selfmap and derivative certificate.

Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
All proof comparisons are exact.  Floating arithmetic only proposes positive
distance weights; every proposed weight is then consumed by the complete
original rational image and Jw, including the infinite-high component.
This certifies the mixed-boundary outer equations, not parameter cut closure.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import time

import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def ex(v):
    if isinstance(v, F):
        return v
    if isinstance(v, int):
        return F(v)
    if isinstance(v, dict):
        return F(int(v['numerator']), int(v['denominator']))
    return F(int(v[0])) * F(2)**int(v[1])


def up(v, bits=128):
    if v < 0:
        raise ArithmeticError('Nonnegative exact value required')
    if not v:
        return F(0)
    unit = F(2)**(v.numerator.bit_length()-v.denominator.bit_length()-bits)
    return (v//unit+1)*unit


def pack_exact(v):
    if not v:
        return [0, 0]
    if v.denominator & (v.denominator-1):
        raise ArithmeticError('Outward dyadic required')
    return [str(v.numerator), -(v.denominator.bit_length()-1)]


def pack(v):
    return pack_exact(up(v))


def checked(record):
    if sha(record['path']) != record['sha256']:
        raise ArithmeticError('A frozen actual input changed: '+record['path'])
    return read(record['path'])


def save(path, data):
    if Path(path).exists():
        raise FileExistsError(path)
    raw = (json.dumps(data, separators=(',', ':'))+'\n').encode()
    if str(path).endswith('.gz'):
        raw = gzip.compress(raw, compresslevel=9, mtime=0)
    if len(raw) >= 5_000_000:
        raise ArithmeticError('Partition an output exceeding5MB')
    Path(path).write_bytes(raw)
    return dict(path=str(path), sha256=sha(path), bytes=len(raw))


class LowInterface:
    """Frequency-resolved low image and Jw in the same R126 coordinates."""

    def __init__(self, source_summary, low_summary, nonlow):
        s, l, a = source_summary, low_summary, nonlow
        if not (s['all_gates'] and all(s['gates'].values()) and l['all_gates']
                and s['comparison_partition'] == l['comparison_partition'] == a['comparison_partition']):
            raise ArithmeticError('Same actual original source and target partition required')
        self.KT = 270*F(2)**-34
        self.Rstar = F(2)**-34
        self.C = F(10)
        self.cu, self.cm, self.um, self.pairs = [], [], [], []
        self.vv, self.vh, self.hh = [], [], []
        self.sources = []
        for j, record in enumerate(s['source_records']):
            b = checked(record)
            if not (b['index'] == j and b['modes'] == list(range(2, 93, 2))
                    and ex(b['complete_T_Hessian']) == self.KT
                    and ex(b['complete_T_physical_domain']) == self.Rstar
                    and b['C_times_high_exactly_zero'] and b['u_times_high_exactly_zero']):
                raise ArithmeticError('Complete actual frequency/source domain differs')
            self.sources.append(record)
            self.cu.append([[ex(x) for x in row] for row in b['C_times_u']])
            self.cm.append([max(map(ex, row)) for row in b['C_times_middle']])
            um = [[F(0)]*46 for _ in range(46)]
            for mi, m in enumerate(b['modes']):
                for ni, n in enumerate(b['middle_inputs']):
                    k = n-m
                    if 2 <= k <= 92:
                        um[mi][k//2-1] = ex(b['u_times_middle'][mi][ni])
            self.um.append(um)
            self.pairs.append([(x['m']//2-1, x['k']//2-1, x['n']//2-1, ex(x['coefficient']))
                               for x in b['u_squared_terms']])
            for name in ('vv', 'vh', 'hh'):
                key = {'vv': 'middle_squared', 'vh': 'middle_high', 'hh': 'high_squared'}[name]
                getattr(self, name).append(list(map(ex, b[key])))
        if len(self.sources) != 25:
            raise ArithmeticError('All25 source blocks required')
        B, S, R = map(ex, (a['physical_high_conversion'], a['profile_to_V_upper'], a['profile_physical_upper']))
        self.g2, self.gr, self.gs = [], [], []
        for i, record in enumerate(l['target_records']):
            target = checked(record)
            if target['target_block'] != i:
                raise ArithmeticError('All25 ordered actual low targets required')
            materials = [[[F(0)]*46 for _ in range(3)] for _ in range(25)]
            for row in target['kernels']:
                j, p = row['source_block'], 2-row['power']
                materials[j][p] = [ex(v['common_sigma']['P'])+ex(v['common_sigma']['K']) for v in row['mode_rows']]
            g2, gr, gs = [], [], []
            for j, (g, one, zero) in enumerate(materials):
                c, square = g[:], g[:]
                if j == 5:
                    c, square = [B*x for x in one], [B*B*x for x in zero]
                elif j == 21:
                    c = [min(S*x, R*y) for x, y in zip(g, one)]
                    square = [min(S*S*x, S*R*y, R*R*z) for x, y, z in zip(g, one, zero)]
                g2.append(g); gr.append(c); gs.append(square)
            self.g2.append(g2); self.gr.append(gr); self.gs.append(gs)

    def source(self, u, r, h, direction=None):
        p2, pr, ps = [], [], []
        for j in range(25):
            U = sum(u[j], F(0)); t = U+r[j]
            a, b, c = [F(0)]*46, [F(0)]*46, [F(0)]*46
            if direction is None:
                for m in range(46):
                    a[m] = (sum((v*x for v, x in zip(self.cu[j][m], u[j])), F(0))
                        +self.cm[j][m]*r[j]
                        +r[j]*sum((v*x for v, x in zip(self.um[j][m], u[j])), F(0))
                        +self.vv[j][m]*r[j]*r[j]
                        +self.KT*(self.C*t+t*t/2))
                    b[m] = self.vh[j][m]*r[j]*h[j]+self.KT*(self.C+t)*h[j]
                    c[m] = self.hh[j][m]*h[j]*h[j]+self.KT*h[j]*h[j]/2
                for m, k, n, value in self.pairs[j]:
                    a[m] += value*u[j][k]*u[j][n]
            else:
                du, dr, dh = direction; dU = sum(du[j], F(0)); dt = dU+dr[j]
                for m in range(46):
                    a[m] = (sum((v*x for v, x in zip(self.cu[j][m], du[j])), F(0))
                        +self.cm[j][m]*dr[j]
                        +dr[j]*sum((v*x for v, x in zip(self.um[j][m], u[j])), F(0))
                        +r[j]*sum((v*x for v, x in zip(self.um[j][m], du[j])), F(0))
                        +2*self.vv[j][m]*r[j]*dr[j]+self.KT*(self.C+t)*dt)
                    b[m] = (self.vh[j][m]*(dr[j]*h[j]+r[j]*dh[j])
                        +self.KT*(h[j]*dt+(self.C+t)*dh[j]))
                    c[m] = 2*self.hh[j][m]*h[j]*dh[j]+self.KT*h[j]*dh[j]
                for m, k, n, value in self.pairs[j]:
                    a[m] += value*(u[j][k]*du[j][n]+du[j][k]*u[j][n])
            # Outward rounding only increases complete positive source sums;
            # it does not delete tiny positive high-cancellation terms.
            p2.append(list(map(up, a))); pr.append(list(map(up, b))); ps.append(list(map(up, c)))
        return p2, pr, ps

    def apply(self, source):
        a, b, c = source
        return [[up(sum((self.g2[i][j][m]*a[j][m]+self.gr[i][j][m]*b[j][m]
                         +self.gs[i][j][m]*c[j][m] for j in range(25)), F(0)))
                 for m in range(46)] for i in range(25)]

    def images(self, u, r, h):
        return self.apply(self.source(u, r, h))

    def action(self, u, r, h, du, dr, dh):
        return self.apply(self.source(u, r, h, (du, dr, dh)))


class FloatProposal:
    """A fast positive Jw approximation used solely to choose weights."""

    def __init__(self, low, conditional, u, r, h):
        self.u = np.array(u, dtype=float); self.r = np.array(r, dtype=float); self.h = np.array(h, dtype=float)
        self.g2 = np.array(low.g2, dtype=float); self.gr = np.array(low.gr, dtype=float); self.gs = np.array(low.gs, dtype=float)
        cu = np.array(low.cu, dtype=float); um = np.array(low.um, dtype=float)
        cm = np.array(low.cm, dtype=float); vv = np.array(low.vv, dtype=float)
        vh = np.array(low.vh, dtype=float); hh = np.array(low.hh, dtype=float)
        kt = float(low.KT); t = self.u.sum(axis=1)+self.r
        self.du2 = cu+self.r[:, None, None]*um+kt*(10+t[:, None, None])
        for j in range(25):
            for m, k, n, value in low.pairs[j]:
                a = float(value)
                self.du2[j, m, k] += a*self.u[j, n]
                self.du2[j, m, n] += a*self.u[j, k]
        self.dr2 = cm+np.einsum('jmn,jn->jm', um, self.u)+2*vv*self.r[:, None]+kt*(10+t[:, None])
        self.dur = kt*self.h
        self.drr = (vh+kt)*self.h[:, None]
        self.dhr = vh*self.r[:, None]+kt*(10+t[:, None])
        self.dhs = (2*hh+kt)*self.h[:, None]
        self.lf = np.zeros((25, 25, 46)); self.lh = np.zeros((25, 25))
        self.nn = np.zeros((25, 25, 4))
        for i, row in enumerate(conditional['rows']):
            for j, col in enumerate(row['complete_low_input_derivative_columns']):
                if col['source_block'] != j:
                    raise ArithmeticError('Source order differs')
                self.lf[i, j] = [float(ex(x)) for x in col['finite_by_low_input']]
                self.lh[i, j] = float(ex(col['high_same_for_each_low_input']))
            for j, vals in enumerate(row['complete_causal_nonlow_derivative']):
                self.nn[i, j] = [float(ex(x)) for x in vals]
        self.scale = np.r_[self.u.ravel(), self.r, self.h]
        if not np.all(np.isfinite(self.scale)) or not np.all(self.scale > 0):
            raise ArithmeticError('Strictly positive finite proposal scales required')

    def action(self, value):
        direction = self.scale*value
        du = direction[:1150].reshape(25, 46); dr = direction[1150:1175]; dh = direction[1175:]
        du_sum = du.sum(axis=1)
        a = np.einsum('jmn,jn->jm', self.du2, du)+self.dr2*dr[:, None]
        b = self.dur[:, None]*du_sum[:, None]+self.drr*dr[:, None]+self.dhr*dh[:, None]
        c = self.dhs*dh[:, None]
        lo = np.einsum('ijm,jm->im', self.g2, a)+np.einsum('ijm,jm->im', self.gr, b)+np.einsum('ijm,jm->im', self.gs, c)
        fi = np.einsum('ijn,jn->i', self.lf, du)+self.nn[:, :, 0]@dr+self.nn[:, :, 1]@dh
        hi = self.lh@du_sum+self.nn[:, :, 2]@dr+self.nn[:, :, 3]@dh
        result = np.r_[lo.ravel(), fi, hi]/self.scale
        if not np.all(np.isfinite(result)) or np.any(result < 0):
            raise ArithmeticError('A positive proposal action became invalid')
        return result

    def weights(self, max_steps=512):
        w = np.ones(1200); history = []
        for n in range(max_steps):
            aw = self.action(w)
            ratio = float(np.max(aw/w))
            history.append(dict(iteration=n, maximum_ratio=ratio, largest_relative_weight=float(np.max(w))))
            if ratio < .49:
                return w, history
            w = 1+aw/.375
            if not np.all(np.isfinite(w)) or np.max(w) > 1e150:
                break
        return None, history


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    args = ap.parse_args(); started = time.monotonic()
    args.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    if list(args.out_prefix.parent.glob(args.out_prefix.name+'-*')):
        raise FileExistsError('Fresh complete certificate prefix required')
    ids = read(args.inputs)
    conditional = checked(ids['conditional_nonlow'])
    conditional_resource = checked(ids['conditional_resource'])
    independent = checked(ids['conditional_independent'])
    source_summary = checked(ids['low_source_summary']); low_summary = checked(ids['low_summary'])
    initial_low = checked(source_summary['conditional_image_record'])
    joint = checked(ids['joint']); checked(ids['near'])
    interface = ids['nonlow_interface']
    if sha(interface['path']) != interface['sha256']:
        raise ArithmeticError('Frozen nonlow source interface differs')
    spec = importlib.util.spec_from_file_location('frozen_nonlow_interface', interface['path'])
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    nonlow = module.NonlowInterface(ids['joint']['path'], ids['near']['path'])
    gates = dict(conditional_actual_gates=conditional['all_gates'] and all(conditional['gates'].values()),
        conditional_actual_exit_zero=conditional_resource['exitcode'] == 0 and conditional_resource['termination_signal'] is None,
        conditional_independent=independent['all_gates'], same_actual_parameter_domain=conditional['same_R126_parameter_domain']
            and ex(conditional['transverse_radius']) == F(1, 32), original_complete_T_domain=nonlow.Rstar == F(2)**-34)
    if not all(gates.values()):
        raise ArithmeticError('Actual original conditional inputs required')
    u = [[ex(x) for x in row] for row in conditional['low_mode_radii']]
    r = [ex(row['finite_radius']) for row in conditional['rows']]
    h = [ex(row['high_radius']) for row in conditional['rows']]
    gates['candidate_exactly_twice_original_conditional_low_caps'] = all(u[j][m] == 2*ex(initial_low['rows'][j]['separate_mode_caps'][m])
        for j in range(25) for m in range(46))
    if not gates['candidate_exactly_twice_original_conditional_low_caps']:
        raise ArithmeticError('The actual declared candidate changed')
    low = LowInterface(source_summary, low_summary, joint)
    prepared = nonlow.prepare(u)
    low_image = low.images(u, r, h)
    other = nonlow.images(prepared, r, h)
    exact_radii = [x for row in u for x in row]+r+h
    exact_images = [x for row in low_image for x in row]+list(map(up, other['finite']))+list(map(up, other['high']))
    image_gates = [value < radius for value, radius in zip(exact_images, exact_radii)]
    domain = list(map(up, other['domain']))
    gates['all1200_strict_selfmaps'] = all(image_gates)
    gates['all25_entire_complete_physical_balls'] = all(x < nonlow.Rstar for x in domain)
    report = dict(schema='visible-flex-full1200-positive-outer-ball-v1', source_sha256=sha(__file__),
        input_manifest_sha256=sha(args.inputs), inputs=ids, gates=gates,
        same_R100_parameter_domain='six complex original unit axes times T weighted-l1 radius1/32',
        low_modes=list(range(2, 93, 2)), middle_modes=[94, 34814], infinite_high_cutoff=34816,
        low_mode_radii=[[pack_exact(x) for x in row] for row in u], finite_radii=list(map(pack_exact, r)), high_radii=list(map(pack_exact, h)),
        exact_positive_source_rounding='128bit upward dyadic, with positive infinite cancellation paid before rounding',
        complete_images=list(map(pack_exact, exact_images)), complete_selfmap_gates=image_gates,
        physical_domains=list(map(pack_exact, domain)), complete_mean_and_inverse_retained=True,
        prescribed_boundary_scope='R126 true nonlow initial trace and original low mixed boundary; parameter cut still separate',
        parameter_cut_closed=False, closed_surface_claimed=False)
    print(json.dumps(dict(event='complete_selfmap', all1200=all(image_gates), physical=all(x < nonlow.Rstar for x in domain),
        largest_image_ratio=float(max(v/z for v, z in zip(exact_images, exact_radii))), bad_rows=[i for i, ok in enumerate(image_gates) if not ok])), flush=True)
    if all(image_gates) and gates['all25_entire_complete_physical_balls']:
        proposal = FloatProposal(low, conditional, u, r, h)
        w, history = proposal.weights()
        report['float_proposal_history'] = history
        report['float_proposal_is_not_a_proof'] = True
        if w is not None:
            weights = [up(radius*F.from_float(float(value))) for radius, value in zip(exact_radii, w)]
            du = [weights[j*46:(j+1)*46] for j in range(25)]
            dr, dh = weights[1150:1175], weights[1175:]
            lo_jw = low.action(u, r, h, du, dr, dh)
            nh_jw = nonlow.action(prepared, r, h, du, dr, dh)
            jw = [x for row in lo_jw for x in row]+list(map(up, nh_jw['finite']))+list(map(up, nh_jw['high']))
            metric_gates = [value < weight/2 for value, weight in zip(jw, weights)]
            report.update(distance_weights=list(map(pack_exact, weights)), complete_Jw=list(map(pack_exact, jw)),
                complete_distance_gates=metric_gates, contraction_target_rational=[1, 2],
                maximum_weighted_distance_upper=pack(max(v/z for v, z in zip(jw, weights))))
            gates['all1200_exact_distance_rows_below_one_half'] = all(metric_gates)
            print(json.dumps(dict(event='complete_exact_distance', all1200=all(metric_gates),
                maximum=float(max(v/z for v, z in zip(jw, weights))), proposal_steps=len(history))), flush=True)
        else:
            gates['all1200_exact_distance_rows_below_one_half'] = False
    else:
        gates['all1200_exact_distance_rows_below_one_half'] = False
    report['all_gates'] = all(gates.values())
    report['full_outer_mixed_boundary_fixed_point_claimed'] = report['all_gates']
    report['elapsed_seconds'] = time.monotonic()-started
    report['peak_rss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    primary = save(Path(str(args.out_prefix)+'-certificate.json.gz'), report)
    summary = {k: v for k, v in report.items() if k not in ('low_mode_radii', 'finite_radii', 'high_radii', 'complete_images',
        'complete_selfmap_gates', 'physical_domains', 'distance_weights', 'complete_Jw', 'complete_distance_gates')}
    summary['primary'] = primary
    save(Path(str(args.out_prefix)+'-summary.json'), summary)
    print(json.dumps(dict(all_gates=report['all_gates'], elapsed_seconds=report['elapsed_seconds'],
        peak_rss_kib=report['peak_rss_kib'], primary=primary)), flush=True)


if __name__ == '__main__':
    main()
