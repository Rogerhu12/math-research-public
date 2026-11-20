#!/usr/bin/env python3
"""Continuous true-g bounds for saved stages of one shared literal-R tail.

The finite nodal jets define exact quintics; no original PDE derivative or
JS background accuracy is assumed.  Equal-frequency linear Gram terms are
combined exactly.  When needed, low quadratic terms are also combined and
every omitted high quadratic product is bounded explicitly.
"""
import argparse
from fractions import Fraction as Q
import gzip
import json
import math
from pathlib import Path
import time

import certify_q060_stage127_r_quintic as lib
from q060_true_background_oracle import (
    Q060TrueBackgroundOracle, file_sha256, mpf_fraction,
)


CHECKPOINT_SHA = "302662026a7e213647d8bfb2813f970174c8c919bb6f4d406e073ef9f3c110de"


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def product(a, b):
    result = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return lib.trim(result)


def neighbor(n, j, outward):
    if outward:
        return (n, j + 1) if j < 8 else (n - 1, 0)
    return (n, j - 1) if j > 0 else (n + 1, 8)


def local_background_cover(o, d):
    """Monotone true-R cover, including both sides of source interfaces."""
    n, j = int(d['rawCell']), int(d['rawSegment'])
    a, b = Q.from_float(d['rawLeft']), Q.from_float(d['rawRight'])
    rlo, rhi = (Q.from_float(d['nodes'][k]['radiusJS']) for k in (0, -1))
    delta = Q(1, 10**6)
    cut = Q.from_float(o.constants['parameters']['rCut'])
    for _ in range(16):
        ranges = [(n, j, max(Q(0), a-delta), min(Q(1), b+delta))]
        if a-delta < 0:
            ni, ji = neighbor(n, j, False)
            ranges.insert(0, (ni, ji, 1+a-delta, Q(1)))
        if b+delta > 1 and (n, j) != (0, 8):
            no, jo = neighbor(n, j, True)
            ranges.append((no, jo, Q(0), b+delta-1))
        first, last = ranges[0], ranges[-1]
        left = o.primitives(*first[:2], first[2])['r']
        right = o.primitives(*last[:2], last[3])['r']
        left_ok = o.hi(left) < o.lo(o.qi(rlo))
        exact_cut = (n, j, b) == (0, 8, Q(1)) and rhi == cut
        right_ok = exact_cut or o.lo(right) > o.hi(o.qi(rhi))
        if left_ok and right_ok:
            break
        delta *= 2
    else:
        raise ArithmeticError('No true-R cover for stage ' + str(d['stage']))
    if delta >= Q(1, 100):
        raise ArithmeticError('Unexpectedly large source cover')
    w_ranges = []
    for nc, jc, l, r in ranges:
        for k in range(8):
            l0, r0 = l+(r-l)*Q(k, 8), l+(r-l)*Q(k+1, 8)
            jets = o.local_jets(nc, jc, l0, r0)
            if o.lo(jets['w_x']) >= 0 or o.hi(jets['w_x']) <= 0:
                w_ranges += [o.local_jets(nc, jc, x)['w'] for x in (l0, r0)]
            else:
                w_ranges.append(jets['w'])
    w = o.k.hull(w_ranges)
    w0 = Q.from_float(float((o.lo(w)+o.hi(w))/2))
    dw = max(abs(mpf_fraction(o.lo(w))-w0), abs(mpf_fraction(o.hi(w))-w0))
    return {'kind': 'true_primitive_monotone_R_cover',
            'source_ranges': [[nc, jc, str(l), str(r)] for nc, jc, l, r in ranges],
            'literal_R_exact': [str(rlo), str(rhi)],
            'left_true_R': o.bounds(left), 'right_true_R': o.bounds(right),
            'right_exact_cut': exact_cut, 'strict_monotone_cover_verified': True,
            'true_w_range': o.bounds(w), 'auxiliary_w0_exact': str(w0),
            'absolute_w_minus_w0_upper_exact': str(dw)}, w0, dw


def prepare(d):
    pm, hm = list(map(int, d['planarModes'])), list(map(int, d['heightModes']))
    modes, P = pm+hm, len(pm)
    nodes, mids = d['nodes'], d['midpoints']
    radii = [Q.from_float(n['radiusJS']) for n in nodes]
    if len(mids) != len(nodes)-1 or not all(0 < x < y for x, y in zip(radii, radii[1:])):
        raise ValueError('Not an increasing literal-R mesh')
    spans, identities = [], 0
    for index, (left, right, mid) in enumerate(zip(nodes, nodes[1:], mids)):
        r0, r1 = radii[index:index+2]
        h = r1-r0
        deriv, norm = [[], [], []], [[], [], []]
        for c in range(len(modes)):
            l, r = ([Q.from_float(v[c]) for v in n['coefficients']] for n in (left, right))
            poly = lib.hermite(*l, *r, h)
            for order in range(3):
                pp = lib.derivative(poly, h, order)
                if lib.evaluate(pp, Q(0)) != l[order] or lib.evaluate(pp, Q(1)) != r[order]:
                    raise ArithmeticError('Exact common endpoint two-jet identity failed')
                identities += 2
                deriv[order].append(pp)
                norm[order].append(lib.bernstein_abs(pp))
        v, vr, vrr = [sum(row, Q(0)) for row in norm]
        vt = sum((abs(m)*v for m, v in zip(modes, norm[0])), Q(0))
        vrt = sum((abs(m)*v for m, v in zip(modes, norm[1])), Q(0))
        vtt = sum((m*m*v for m, v in zip(modes, norm[0])), Q(0))
        hz_r = sum(norm[1][P:], Q(0))
        hz_t = sum((m*v for m, v in zip(hm, norm[0][P:])), Q(0))
        eta_sq = vr*vr+(vt/r0)**2
        h11, h12, h22 = vrr+Q(82, 25)*vr, (vrt+vt/r0)/r0, vtt/r0**2+vr/r0
        beta_sq = h11*h11+2*h12*h12+h22*h22
        t = (Q.from_float(mid['radiusJS'])-r0)/h
        if not 0 < t < 1:
            raise ValueError('Saved midpoint lies outside the new span')
        gaps = [sum((abs(lib.evaluate(deriv[k][i], t)-Q.from_float(mid['coefficients'][k][i]))
                     for i in range(len(modes))), Q(0)) for k in range(3)]
        spans.append(dict(index=index, r0=r0, r1=r1, h=h, deriv=deriv, norm=norm,
                          v=v, vr=vr, vt=vt, hz_r=hz_r, hz_t=hz_t,
                          eta_sq=eta_sq, beta_sq=beta_sq, midpoint_gaps=gaps))
    return pm, hm, spans, identities


def gram_span(s, pm, hm, w0, dw, quadratic_cutoff=None):
    r0, h, d = s['r0'], s['h'], s['deriv']
    P, modes = len(pm), pm+hm
    aa, bb, cc = {}, {}, {}
    for i, m in enumerate(pm):
        lib.harmonic_add(aa, m-1, lib.scale(d[1][i], 2))
        lib.harmonic_add(bb, m-1, lib.add(lib.radius_product(d[1][i], r0, h), lib.scale(d[0][i], -m)), sine=True)
        lib.harmonic_add(cc, m-1, lib.scale(lib.radius_product(d[0][i], r0, h), 2*m))
    for j, m in enumerate(hm):
        lib.harmonic_add(aa, m, lib.scale(d[1][P+j], 2*w0))
        lib.harmonic_add(bb, m, lib.scale(d[0][P+j], -w0*m), sine=True)
    if quadratic_cutoff is None:
        remainder = [s['vr']**2, s['vr']*s['vt'], s['vt']**2]
        method = 'all_linear_Fourier_merged_all_quadratic_norm_bounded'
    else:
        lp = [i for i, m in enumerate(pm) if abs(m) <= quadratic_cutoff]
        lh = [i for i, m in enumerate(hm) if m <= quadratic_cutoff]
        low = set(lp+[P+i for i in lh])
        high = set(range(len(modes)))-low
        for i in lp:
            m = pm[i]
            for j in lp:
                n = pm[j]
                lib.harmonic_add(aa, m-n, product(d[1][i], d[1][j]))
                lib.harmonic_add(bb, m-n, lib.scale(product(d[1][i], d[0][j]), n), sine=True)
                lib.harmonic_add(cc, m-n, lib.scale(product(d[0][i], d[0][j]), m*n))
        for i in lh:
            m = hm[i]
            for j in lh:
                n = hm[j]
                aij = lib.scale(product(d[1][P+i], d[1][P+j]), Q(1, 2))
                bij = lib.scale(product(d[1][P+i], d[0][P+j]), -Q(n, 2))
                cij = lib.scale(product(d[0][P+i], d[0][P+j]), Q(m*n, 2))
                lib.harmonic_add(aa, m-n, aij)
                lib.harmonic_add(aa, m+n, aij)
                lib.harmonic_add(bb, n+m, bij, sine=True)
                lib.harmonic_add(bb, n-m, bij, sine=True)
                lib.harmonic_add(cc, m-n, cij)
                lib.harmonic_add(cc, m+n, lib.scale(cij, -1))
        rl = sum((s['norm'][1][i] for i in low), Q(0))
        rh = sum((s['norm'][1][i] for i in high), Q(0))
        tl = sum((abs(modes[i])*s['norm'][0][i] for i in low), Q(0))
        th = sum((abs(modes[i])*s['norm'][0][i] for i in high), Q(0))
        remainder = [2*rl*rh+rh*rh, rl*th+rh*tl+rh*th, 2*tl*th+th*th]
        method = 'all_linear_and_low_quadratic_Fourier_merged_high_quadratic_bounded'
    merged = [sum((lib.bernstein_abs(v) for v in z.values()), Q(0)) for z in (aa, bb, cc)]
    A = merged[0]+2*dw*s['hz_r']+remainder[0]
    B = (merged[1]+dw*s['hz_t']+remainder[1])/r0
    C = (merged[2]+remainder[2])/r0**2
    return {'method': method, 'metric': max(A, C)+B, 'components': (A, B, C),
            'merged': merged, 'quadratic_remainder': remainder}


def certify(o, d, quadratic_cutoff=12):
    rlo = Q.from_float(d['nodes'][0]['radiusJS'])
    rhi = Q.from_float(d['nodes'][-1]['radiusJS'])
    if o.hi(o.radius_deep) >= o.lo(o.qi(rlo)) or rhi > Q.from_float(o.constants['parameters']['rCut']):
        raise ValueError('The literal radius stage leaves the proved true-background domain')
    pm, hm, spans, identities = prepare(d)
    gate = Q(1, 10**6)
    cover = {'kind': 'R58_global_true_background_bound',
             'auxiliary_w0_exact': '0', 'absolute_w_minus_w0_upper_exact': '41/100'}
    w0, dw = Q(0), Q(41, 100)
    grams = [gram_span(s, pm, hm, w0, dw) for s in spans]
    if max(g['metric'] for g in grams) >= gate:
        cover, w0, dw = local_background_cover(o, d)
        grams = [gram_span(s, pm, hm, w0, dw) for s in spans]
        for i, (s, g) in enumerate(zip(spans, grams)):
            if g['metric'] >= gate:
                alternative = gram_span(s, pm, hm, w0, dw, quadratic_cutoff)
                if alternative['metric'] < g['metric']:
                    grams[i] = alternative
    metric = max(g['metric'] for g in grams)
    eta = o.iv.sqrt(o.qi(max(s['eta_sq'] for s in spans)))
    beta = o.iv.sqrt(o.qi(max(s['beta_sq'] for s in spans)))
    if o.hi(eta) >= 1:
        raise ArithmeticError('Immersion not proved by the perturbation bound')
    K = (8+beta)/(1-eta)**2
    rows = []
    for s, g in zip(spans, grams):
        rows.append({'span': s['index'], 'R_exact': [str(s['r0']), str(s['r1'])],
                     'method': g['method'], 'metric_upper_exact': str(g['metric']),
                     'Gram_components_upper_exact': list(map(str, g['components'])),
                     'merged_numerators_l1_exact': list(map(str, g['merged'])),
                     'quadratic_remainders_exact': list(map(str, g['quadratic_remainder'])),
                     'eta_squared_exact': str(s['eta_sq']), 'beta_squared_exact': str(s['beta_sq']),
                     'position_upper_exact': str(s['v']),
                     'saved_midplane_jet_gaps_exact': list(map(str, s['midpoint_gaps']))})
    return {'status': 'shared_R_stage_continuous_metric_passed' if metric < gate else 'shared_R_stage_metric_not_proved',
            'stage': d['stage'], 'map_hash': d['sharing']['mapHash'], 'metric_gate_passed': metric < gate,
            'continuous_metric_operator_upper': o.bounds(o.qi(metric)),
            'normalized_first_jet_upper': o.bounds(eta),
            'normalized_covariant_Hessian_upper': o.bounds(beta),
            'principal_curvature_upper': o.bounds(K),
            'position_perturbation_upper': o.bounds(o.qi(max(s['v'] for s in spans))),
            'saved_midplane_jet_gaps': [o.bounds(o.qi(max(s['midpoint_gaps'][k] for s in spans))) for k in range(3)],
            'spans': len(spans), 'shared_two_jet_scalar_equalities': identities,
            'background_cover': cover, 'quadratic_mode_cutoff': quadratic_cutoff,
            'mean_definition': d['meanDefinition'], 'rows': rows}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('manifest', 'constants', 'normalization-certificate', 'outdir'):
        ap.add_argument('--'+name, type=Path, required=True)
    ap.add_argument('--stages', required=True, help='comma list of actually exported stage ids')
    ap.add_argument('--quadratic-mode-cutoff', type=int, default=12)
    a = ap.parse_args()
    started = time.monotonic()
    if a.outdir.exists():
        raise ValueError('Use a new certificate directory')
    a.outdir.mkdir(parents=True)
    manifest = read(a.manifest)
    if manifest['existingCheckpoint']['sha256'] != CHECKPOINT_SHA:
        raise ValueError('This execution is bound to the saved .25 response')
    stages = sorted(set(map(int, a.stages.split(','))))
    files = {r['stage']: r for r in manifest['files']}
    if not set(stages).issubset(files):
        raise ValueError('Selected stage has not actually been exported')
    if a.quadratic_mode_cutoff < 0:
        raise ValueError('Nonnegative low-mode cutoff required')
    o = Q060TrueBackgroundOracle(a.constants, a.normalization_certificate)
    result = {'status': 'running', 'source_sha256': file_sha256(__file__),
              'polynomial_library_sha256': file_sha256(lib.__file__),
              'manifest_sha256': file_sha256(a.manifest), 'checkpoint_sha256': CHECKPOINT_SHA,
              'oracle_provenance': o.provenance, 'selected_stages': stages, 'stages': [],
              'all_angle_and_continuous_radius': True, 'original_BVP_solves': 0,
              'shooting_iterations': 0, 'full_H': False, 'global_tail_complete': False,
              'map_scope': 'The same true R58 background plus exact common literal-R Fourier quintics, with original cumulative perturbation mean. Source FD second jets are only chosen finite nodal parameters.',
              'mean_scope': 'No reset, re-integration, or replacement of the saved cumulative perturbation mean.',
              'upper_height_scope': 'Reflect both the true background and all perturbation height terms together; these metric and curvature bounds are unchanged.'}
    for stage in stages:
        entry = files[stage]
        if file_sha256(entry['path']) != entry['sha256']:
            raise ValueError('Exported stage bytes changed')
        d = read(entry['path'])
        if d['stage'] != stage or d['sharing']['mapHash'] != entry['mapHash']:
            raise ValueError('Exported stage identity changed')
        if d['finiteScope']['M'] != 24 or d['finiteScope']['quadrature'] != 512:
            raise ValueError('Unexpected finite field scope')
        if not all(d['physicalParameters'].get(k) == v for k, v in o.constants['parameters'].items()):
            raise ValueError('Physical background parameters differ')
        t0 = time.monotonic()
        row = certify(o, d, a.quadratic_mode_cutoff)
        row.update(data_sha256=entry['sha256'], seconds=time.monotonic()-t0)
        name = a.outdir/('stage-'+str(stage).zfill(4)+'.json')
        name.write_text(json.dumps(row, indent=2)+'\n')
        small = {k: v for k, v in row.items() if k not in ('rows', 'background_cover', 'mean_definition')}
        small.update(path=str(name.resolve()), sha256=file_sha256(name))
        result['stages'].append(small)
        result['seconds'] = time.monotonic()-started
        (a.outdir/'summary.json').write_text(json.dumps(result, indent=2)+'\n')
        print(json.dumps({'stage': stage, 'status': row['status'],
                          'metric_upper': row['continuous_metric_operator_upper']['upper'],
                          'K_upper': row['principal_curvature_upper']['upper'],
                          'background': row['background_cover']['kind'],
                          'seconds': row['seconds']}), flush=True)
    passed = all(r['metric_gate_passed'] for r in result['stages'])
    result['status'] = 'selected_shared_R_stages_continuously_certified' if passed else 'some_shared_R_stages_not_proved'
    result['seconds'] = time.monotonic()-started
    (a.outdir/'summary.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'stages': len(stages),
                      'seconds': result['seconds'], 'summary_sha256': file_sha256(a.outdir/'summary.json')}), flush=True)


if __name__ == '__main__':
    main()
