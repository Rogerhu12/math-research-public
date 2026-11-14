#!/usr/bin/env python3
"""Actual frequency-preserving low reception kernels and conditional images.

Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
Consume R125 and R126 without another ODE/source integral.  All mathematical
bounds use exact rationals and outward Arb.  This computes reception of the
already certified, fixed-low-centre nonlow ball; it does NOT close feedback.
The angular derivatives in Q are paid by (5*k*n+1)/(4*(1+k)*(1+n)).
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
NEAR = list(range(94, 185, 2))
POWERS = [2, 1, 0]
M = 34816
TAU = Q(18, 125)
RSTAR = Q(1, 2**34)
KT = 270 * RSTAR


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def exact(v):
    if isinstance(v, dict):
        return Q(int(v['numerator']), int(v['denominator']))
    m, e = int(v[0]), int(v[1])
    return Q(m * 2**e) if e >= 0 else Q(m, 2**(-e))


def pack(value):
    x = value if isinstance(value, arb) else arb(value)
    if not x.is_finite() or x < 0:
        raise ArithmeticError('Every positive envelope must be finite')
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
    result = exact(pack(value))
    if not isinstance(value, arb) and result < value:
        raise ArithmeticError('Upward dyadic conversion moved down')
    return result


def expup(value):
    return up(arb(value).exp())


def rational(v):
    return [str(v.p), str(v.q)]


def alpha(k, n):
    return Q(5*k*n+1, 4*(1+k)*(1+n))


def save(path, data):
    raw = (json.dumps(data, ensure_ascii=False, separators=(',', ':'))+'\n').encode()
    if str(path).endswith('.gz'):
        raw = gzip.compress(raw, compresslevel=9, mtime=0)
    if len(raw) >= 5_000_000:
        raise ArithmeticError('A single output must stay below5MB')
    if Path(path).exists():
        raise FileExistsError(path)
    Path(path).write_bytes(raw)
    return dict(path=str(path), sha256=sha(path), bytes=len(raw))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    args = ap.parse_args()
    ctx.prec = 256
    began = time.monotonic()
    if list(args.out_prefix.parent.glob(args.out_prefix.name+'-*')):
        raise FileExistsError('Fresh output prefix required')
    args.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    inputs = read(args.inputs)
    gates = {}

    def gate(name, condition):
        if not condition:
            raise ArithmeticError(name)
        gates[name] = True

    def checked(name):
        r = inputs[name]
        gate('identity_'+name, sha(r['path']) == r['sha256'])
        return read(r['path'])

    low = checked('low_summary')
    nonlow = checked('nonlow')
    spectrum = checked('low_spectrum')
    aggregate = checked('low_aggregate')
    gate('same25_original_blocks', low['comparison_partition'] == nonlow['comparison_partition']
         and len(nonlow['rows']) == 25)
    gate('R125_complete_actual_inputs', low['all_gates'] and all(low['gates'].values())
         and low['original_parent_count'] == 10793 and low['complete_geometry_subpanels'] == 10878)
    gate('R126_complete_actual_nonlow_ball', nonlow['all_gates'] and all(nonlow['gates'].values())
         and nonlow['high_cutoff'] == M and exact(nonlow['transverse_radius']) == Q(1, 32))
    gate('R101_same_complete_low_spectrum', spectrum['all_gates'] and all(spectrum['gates'].values())
         and [r['mode'] for r in spectrum['final_caps']] == MODES)
    caps = {r['mode']: exact(r['bound']) for r in spectrum['final_caps']}
    gate('complete_centre_strong_bound_below10', sum(caps.values(), Q(0)) < 10)
    gate('original_complete_Hessian_domain', exact(nonlow['complete_Hessian_domain_upper']) == RSTAR
         and RSTAR < Q(1, 128) and exact(nonlow['maximum_whole_ball_physical_domain']) < RSTAR
         and exact(nonlow['full_complete_Hessian_upper']) == Q(23, 9)+KT)

    # Replay the exact original entry jumps and continuous losses.  The new
    # source coefficients are bounded on the same source blocks as R125.
    record = inputs['common_leaves']
    gate('identity_common_leaves', sha(record['path']) == record['sha256'])
    partition = low['comparison_partition']
    block_of = {}
    for j, b in enumerate(partition):
        for panel in range(b['first_panel'], b['last_panel_exclusive']):
            key = (b['cell'], b['segment'], panel)
            gate('partition_unique_'+str(j)+'_'+str(panel), key not in block_of)
            block_of[key] = j
    sigma = TAU
    smin, smax = [None]*25, [None]*25
    counts, vmax = [0]*25, [Q(0)]*25
    with gzip.open(record['path'], 'rt') as stream:
        for line in stream:
            leaf = json.loads(line)
            j = block_of[(leaf['cell'], leaf['segment'], leaf['panel'])]
            jump = Q(*map(int, leaf['common_entry_jump']))
            loss = Q(*map(int, leaf['common_continuous_loss']))
            hi, lo = sigma-jump, sigma-jump-loss
            if not (jump >= 0 and loss >= 0 and Q(1, 64) < lo <= hi <= sigma):
                raise ArithmeticError('The original common strip was not preserved')
            smin[j] = lo if smin[j] is None else min(smin[j], lo)
            smax[j] = hi if smax[j] is None else max(smax[j], hi)
            vmax[j] = max(vmax[j], exact(leaf['V']))
            counts[j] += 1
            sigma = lo
    gate('all_original10793_leaves', sum(counts) == 10793
         and counts == [b['panels'] for b in partition]
         and vmax == [exact(r['V_max']) for r in nonlow['rows']]
         and sigma == Q(*map(int, low['common_sigma_final'])))

    # Coefficient check at every vertex of the original (s,ell,w^2) material
    # triangle, for all finite input pairs that will actually be indexed.
    pair_checks = 0
    for k in MODES:
        for n in MODES+NEAR:
            bound = alpha(k, n)*(1+k)*(1+n)
            for z in (Q(0), Q(1, 4)):
                E = 1+z
                for s, ell in ((Q(1), Q(0)), (Q(0), Q(1)), (Q(0), Q(-1))):
                    difference = [E*s+ell*(E*k*n-z), E*(s*n+ell*k),
                                  E*(s*k+ell*n), E*s*k*n+ell*(E-z)]
                    summation = [-E*s+ell*(E*k*n+z), E*(-s*n+ell*k),
                                 E*(-s*k+ell*n), -E*s*k*n+ell]
                    if max(map(abs, difference+summation)) > bound:
                        raise ArithmeticError('An angular derivative cost was omitted')
                    pair_checks += 8
    gate('all_indexed_full_angular_derivative_coefficients', pair_checks == 46*92*6*8)

    # R125 component suprema are added only after their separate radial
    # suprema have been paid.  No W, F, r_x or frame factor is added again.
    K = [[[[Q(0) for _ in MODES] for _ in POWERS] for _ in range(25)] for _ in range(25)]
    target_ids = []
    for i, rec in enumerate(low['target_records']):
        gate('identity_low_target'+str(i), sha(rec['path']) == rec['sha256'])
        target_ids.append(rec)
        target = read(rec['path'])
        gate('target_mode_shape'+str(i), target['target_block'] == i
             and target['modes'] == MODES and target['powers'] == POWERS)
        for row in target['kernels']:
            j, p = row['source_block'], POWERS.index(row['power'])
            if [a['mode'] for a in row['mode_rows']] != MODES:
                raise ArithmeticError('A mode is missing from an actual target row')
            for mi, item in enumerate(row['mode_rows']):
                K[i][j][p][mi] = exact(item['common_sigma']['P'])+exact(item['common_sigma']['K'])
            if max(K[i][j][p]) > exact(aggregate['Gamma_max_mode']['common_sigma'][i][j][p]):
                raise ArithmeticError('The independent exact R125 aggregate differs')
    gate('all25x25x3x46_original_positive_kernels', True)

    # Source-only kernels: output m and input n.  Modes in the low unknown
    # keep their identity, even when their total strong norm is small.
    blocks, source_records = [], []
    for j in range(25):
        cq_low, cq_middle, uq_middle = [], [], []
        uu_terms = []
        for m in MODES:
            lr, mr, ur = [], [], []
            for n in MODES:
                total = Q(0)
                for signed_n in (n, -n):
                    k = abs(m-signed_n)
                    if k in caps:
                        sig = smax[j] if m >= n else smin[j]
                        exponent = (m-n)*sig-k*TAU
                        total += alpha(k, n)*caps[k]*expup(exponent)
                lr.append(up(total))
            for n in NEAR:
                k = n-m
                mr.append(up(alpha(k, n)*caps[k]*expup(-k*(TAU+smin[j]))) if k in caps else Q(0))
                ur.append(up(alpha(k, n)*expup(-2*k*smin[j])) if k in caps else Q(0))
            cq_low.append(lr)
            cq_middle.append(mr)
            uq_middle.append(ur)
        for ki, k in enumerate(MODES):
            for n in MODES[ki:]:
                if k+n <= 92:
                    uu_terms.append(dict(m=k+n, k=k, n=n,
                        coefficient=pack(alpha(k, n)/(2 if k == n else 1)), branch='sum'))
                if n > k:
                    uu_terms.append(dict(m=n-k, k=k, n=n,
                        coefficient=pack(alpha(k, n)*expup(-2*k*smin[j])), branch='difference'))
        # These positive infinite bounds are never replaced by machine zero.
        vv = [up(Q(5, 4)*expup(-188*smin[j])) for _ in MODES]
        vh = [up(Q(5, 4)*expup(-2*(M-m)*smin[j])) for m in MODES]
        hh = [up(Q(5, 4)*expup(-2*M*smin[j])) for _ in MODES]
        gate('all_infinite_cancellation_bounds_strictly_positive'+str(j), min(vh+hh) > 0)
        block = dict(index=j, sigma_min=rational(smin[j]), sigma_max=rational(smax[j]),
            modes=MODES, middle_inputs=NEAR,
            C_times_u=[[pack(x) for x in row] for row in cq_low],
            C_times_middle=[[pack(x) for x in row] for row in cq_middle],
            u_times_middle=[[pack(x) for x in row] for row in uq_middle],
            u_squared_terms=uu_terms,
            middle_squared=[pack(x) for x in vv],
            middle_high=[pack(x) for x in vh], high_squared=[pack(x) for x in hh],
            C_times_high_exactly_zero=True, u_times_high_exactly_zero=True,
            angular_derivative_pair_constant='(5*k*n+1)/(4*(1+k)*(1+n))',
            complete_T_Hessian=pack(KT), complete_T_physical_domain=pack(RSTAR))
        path = Path(str(args.out_prefix)+f'-source-block{j:02d}.json.gz')
        source_records.append(save(path, block))
        blocks.append((cq_low, cq_middle, uq_middle, vv, vh, hh))

    # Conditional reception of the complete R126 ball at u=0.  Each output
    # cap is valid separately.  The complete T common mass is also consumed
    # once through Gamma_max_mode for a separate total-norm cap.
    r = [exact(x['finite_radius']) for x in nonlow['rows']]
    h = [exact(x['high_radius']) for x in nonlow['rows']]
    B = exact(nonlow['physical_high_conversion'])
    Rmax, S = exact(nonlow['profile_physical_upper']), exact(nonlow['profile_to_V_upper'])
    images = []
    for i in range(25):
        component = {n: [Q(0)]*46 for n in ('linear_C_middle', 'quadratic_middle',
                    'quadratic_middle_high', 'quadratic_high', 'complete_T')}
        total_T_once = Q(0)
        total_linear_once = Q(0)
        for j in range(25):
            _, cm, _, vv, vh, hh = blocks[j]
            g2, g1, g0 = K[i][j]
            gr, gRR = g2, g2
            if j == 5:
                gr, gRR = [B*x for x in g1], [B*B*x for x in g0]
            if j == 21:
                gr = [min(S*x, Rmax*y) for x, y in zip(g2, g1)]
                gRR = [min(S*S*x, S*Rmax*y, Rmax*Rmax*z) for x, y, z in zip(g2, g1, g0)]
            # All source positions of the original noncausal low kernel are
            # retained, including sources strictly to the right of target.
            for mi in range(46):
                component['linear_C_middle'][mi] += g2[mi]*max(cm[mi])*r[j]
                component['quadratic_middle'][mi] += g2[mi]*vv[mi]*r[j]*r[j]
                component['quadratic_middle_high'][mi] += gr[mi]*vh[mi]*r[j]*h[j]
                component['quadratic_high'][mi] += gRR[mi]*hh[mi]*h[j]*h[j]
                component['complete_T'][mi] += KT*(g2[mi]*(10*r[j]+r[j]*r[j]/2)
                    +gr[mi]*(10+r[j])*h[j]+gRR[mi]*h[j]*h[j]/2)
            total_linear_once += max(sum((g2[mi]*cm[mi][ni] for mi in range(46)), Q(0))
                                     for ni in range(46))*r[j]
            total_T_once += KT*(max(g2)*(10*r[j]+r[j]*r[j]/2)
                    +max(gr)*(10+r[j])*h[j]+max(gRR)*h[j]*h[j]/2)
        caps_out = [up(sum((component[n][mi] for n in component), Q(0))) for mi in range(46)]
        total_once = (total_linear_once+total_T_once
            +sum(component['quadratic_middle']+component['quadratic_middle_high']+component['quadratic_high'], Q(0)))
        images.append(dict(target_block=i, modes=MODES, separate_mode_caps=[pack(x) for x in caps_out],
            component_caps={n: [pack(x) for x in v] for n, v in component.items()},
            separate_mode_caps_sum=pack(sum(caps_out, Q(0))),
            combined_norm_upper=pack(min(total_once, sum(caps_out, Q(0)))),
            complete_T_common_mass_paid_once=pack(total_T_once),
            conditional_existing_R126_nonlow_only=True))
    image_record = save(Path(str(args.out_prefix)+'-conditional-images.json.gz'), dict(
        schema='r127-conditional-low-reception-of-R126-ball-v1', rows=images,
        low_feedback_fixed_point_claimed=False, all_frequency_PDE_claimed=False,
        complete_mean_and_inverse_retained=True, same_fixed_background=True))
    summary = dict(schema='r127-low-frequency-reception-kernels-v1', all_gates=all(gates.values()),
        gates=gates, source_sha256=sha(__file__), input_manifest_sha256=sha(args.inputs), inputs=inputs,
        comparison_partition=partition, common_strip_final=rational(sigma),
        pair_coefficient_vertex_checks=pair_checks, source_records=source_records,
        conditional_image_record=image_record, original_target_records=target_ids,
        full_low_mode_count=46, original_parent_count=10793,
        low_feedback_fixed_point_claimed=False, full_cut_claimed=False,
        complete_mean_and_inverse_retained=True,
        condition='The already certified R126 fixed-low-centre nonlow ball on its stated R100 domain.',
        no_new_ODE_or_source_integral=True, elapsed_seconds=time.monotonic()-began,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    save(Path(str(args.out_prefix)+'-summary.json.gz'), summary)
    print(json.dumps(dict(all_gates=summary['all_gates'], source_blocks=25,
        exact_pair_checks=pair_checks, conditional_total_display=[float(exact(x['combined_norm_upper'])) for x in images],
        elapsed_seconds=summary['elapsed_seconds'], peak_rss_kib=summary['peak_rss_kib']), separators=(',', ':')), flush=True)


if __name__ == '__main__':
    main()
