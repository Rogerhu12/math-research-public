#!/usr/bin/env python3
"""Prepared exact R96 pure-source consumer for a REAL middle Green output.

No ODE, flint, source integration, or claim of a full low/high solution.
The upstream actual Green keeps BOTH prescribed true physical head
components. This consumer replaces only the generic 216 pure-low cap
by the already certified R96 modewise complete nonlinear source.
It computes a genuine fixed-low finite-window radius proposal and
checks every scalar self-map/domain/contraction inequality exactly.

The original Green file and failed coarse probe stay unchanged.
Author: exact_closure, GPT-6 Astra Pro (AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import time

ALLOWED_GREEN_SOURCES = {
    '6655a72f38f89d6eb31ded7b78bd4b84f94c500653bbb8e6c3ca2611d6af2e31':
        'closure_outer_middle_volterra_recovered_v1.py',
    'a285a385d657e226ddcb7a080f86478b627e7406f970bb85b7ffc70a6c42feeb':
        'closure_outer_middle_mixed_density_v2.py',
}
WIDE_SHA = '0b9519dafcda5b0ae02f1191539d6054a9a0722f6207c14b96844d9520082de3'
WIDE_SOURCE = 'ee68d5b7773ee0caff312edb334e123fc4fa4aa4bf46a4e27ed61fad52c0bac1'


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def dyad(x):
    return F(int(x[0]))*F(2)**int(x[1])


def up(x, bits=128):
    x = F(x)
    if x < 0:
        raise ArithmeticError('A positive cap cannot be negative')
    if not x:
        return [0, 0]
    e = x.numerator.bit_length()-x.denominator.bit_length()-bits+1
    v = x/F(2)**e
    return [-((-v.numerator)//v.denominator), e]


def exact(x):
    x = F(x)
    return dict(numerator=str(x.numerator), denominator=str(x.denominator))


def save(path, obj):
    p = Path(path)
    if p.exists() or Path(str(p)+'.partial').exists():
        raise FileExistsError('Preserve prior mathematical outputs and failures')
    payload = (json.dumps(obj, separators=(',', ':'))+'\n').encode()
    if len(payload) > 5*1024*1024:
        raise ArithmeticError('The complete primary exceeds the 5MiB repository gate')
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = Path(str(p)+'.partial')
    tmp.write_bytes(payload)
    tmp.rename(p)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--green', type=Path, required=True)
    ap.add_argument('--green-sha256', required=True)
    ap.add_argument('--green-source', type=Path, required=True)
    ap.add_argument('--r96-wide', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--rss-kib', type=int, default=40960)
    args = ap.parse_args()
    began = time.monotonic()
    if digest(args.green) != args.green_sha256:
        raise ValueError('The fresh actual Green primary differs from its declared SHA')
    if digest(args.r96_wide) != WIDE_SHA:
        raise ValueError('The complete independent R96 wide-tail ledger differs')
    src = digest(args.green_source)
    if src not in ALLOWED_GREEN_SOURCES:
        raise ValueError('This is not one of the explicitly prepared true middle equations')
    g = json.loads(args.green.read_text())
    w = json.loads(args.r96_wide.read_text())
    if (not g['all_enclosure_gates'] or not all(g['enclosure_gates'].values())
            or g['config']['entrypoint_sha256'] != src
            or g['config']['source_strip'] != '18/125'
            or g['config']['cells'] != [11, 10]
            or g['counts']['original_panels'] != 10793
            or not g['config']['no_new_high_linear_head_slope']
            or not g['config']['no_outer_high_Dirichlet_constraint']):
        raise ValueError('Require the whole real two-cell enclosure with both actual head traces')
    if (not w['all_gates'] or len(w['gates']) != 11 or not all(w['gates'].values())
            or w['source_sha256'] != WIDE_SOURCE
            or w['original_constant_strip'] != '18/125'
            or w['new_R92_domain_claimed'] is not False):
        raise ValueError('Retain the old real R74 complete-mean finite centre and its whole source tail')
    modes = g['declared_modes']
    if (modes != sorted(set(modes)) or any(m < 94 or m > 5758 or m % 2 for m in modes)
            or [r['mode'] for r in g['rows']] != modes):
        raise ValueError('The explicit window must lie in the same actual middle range')
    direct = {r['mode']: dyad(r['chosen_source_upper'])
              for r in w['source_rows94_to552']}
    blocks = w['complete_middle554_to5758_blocks']
    def source(m):
        if m <= 552:
            return direct[m]
        block = next(z for z in blocks if z['first_mode'] <= m <= z['last_mode'])
        if block['formula'] != 'common_factor*(3/8)^mode':
            raise ValueError('The complete high part of the middle source changed definition')
        return dyad(block['common_factor'])*F(3, 8)**m
    residual = F(0)
    gamma = F(0)
    rows = []
    for row in g['rows']:
        m = row['mode']
        gm = dyad(row['base_source_Green_upper'])
        bm = source(m)
        if gm < 0 or bm < 0:
            raise ArithmeticError('A complete kernel/source comparison is negative')
        gamma = max(gamma, gm)
        residual += gm*bm
        rows.append(dict(mode=m,actual_Green_upper=up(gm),
                         R96_complete_pure_source_upper=up(bm),
                         pure_source_response_upper=up(gm*bm)))
    if gamma > dyad(g['maximum_base_kernel']):
        raise ArithmeticError('The complete per-mode kernel and upstream maximum disagree')
    C0, V0 = F(10), F(1, 2**40)
    if not dyad(w['same_actual_low_centre_norm']) < C0:
        raise ArithmeticError('The same actual low centre is not in the ten-ball')
    head = dyad(g['complete_given_head_lift'])
    c0 = head+residual
    a0 = 4*C0*gamma
    radius = 2*c0/(1-a0) if a0 < 1 and c0 > 0 else None
    gates = dict(
        complete_actual_real_middle_enclosure=True,
        both_true_initial_physical_components_retained=True,
        same_real_R74_low_centre_complete_mean_and_inverse=True,
        source_mode_sum_not_replaced_by_one_maximum=True,
        diagonal_source_operator_uses_valid_fixed_mass_maximum=True,
        positive_linear_margin=bool(a0 < 1),
        strictly_positive_proposal=bool(radius is not None and radius > 0))
    proposal = None
    if radius is not None:
        R = (C0+radius)*V0
        leading = F(5,4)*R+4*R*R
        image = c0+a0*radius+2*gamma*radius*radius
        lip = 4*(C0+radius)*gamma
        gates.update(
            radius_within_one_eighth=bool(radius <= F(1,8)),
            whole_pointwise_mean_domain=bool(R < F(1,64)),
            complete_Wiener_inverse=bool(leading < 1),
            genuine_finite_window_selfmap=bool(image < radius),
            genuine_finite_window_contraction=bool(lip < 1))
        proposal = dict(radius=exact(radius),image_upper=up(image),
                        Lipschitz_upper=up(lip),physical_radius_upper=up(R),
                        complete_leading_norm_upper=up(leading),
                        selfmap_slack=exact(radius-image),
                        contraction_slack=exact(1-lip))
    else:
        gates.update(radius_within_one_eighth=False,
                     whole_pointwise_mean_domain=False,
                     complete_Wiener_inverse=False,
                     genuine_finite_window_selfmap=False,
                     genuine_finite_window_contraction=False)
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if peak > args.rss_kib:
        raise MemoryError('Observed owned RSS exceeds the declared stop threshold: '+str(peak))
    result = dict(
        status='Exact actually consumed finite-window proposal; inspect all mathematical gates',
        entrypoint_sha256=digest(__file__),
        input_hashes={str(args.green):args.green_sha256,
                      str(args.green_source):src,
                      str(args.r96_wide):WIDE_SHA},
        all_gates=all(gates.values()),gates=gates,
        declared_modes=modes,mode_rows=rows,
        source_units='source-x (s+abs(ell))*V^2; output1+m already included in the actual Green',
        parameter_domain='Original real R74 domain only; not new R92 transverse axes',
        actual_low_local_cap=exact(C0),
        exact_kernel_maximum=exact(gamma),
        actual_head_lift_upper=up(head),
        complete_R96_pure_source_response_upper=up(residual),
        complete_constant_residual_upper=up(c0),
        exact_linear_feedback_bound=exact(a0),
        proposed_finite_window=proposal,
        old_coarse_probe_selfmap=g['conditional_window_selfmap'],
        old_coarse_probe_contraction=g['conditional_window_contraction'],
        original_Green_output_unchanged=True,
        low_field_fixed_not_resolved=True,
        other_middle_and_high_fields_fixed_to_zero_for_this_projection=True,
        all_middle_modes_covered=(modes==list(range(94,5759,2))),
        low_middle_high_joint_solution_claimed=False,
        cut_consistency_or_closed_surface_claimed=False,
        upstream_formal_exit_evidence_must_be_retained_separately=True,
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=peak)
    save(args.out,result)
    print(json.dumps(dict(event='R96_middle_window_exact_probe_complete',
                          all_gates=result['all_gates'],output=str(args.out),
                          output_sha256=digest(args.out),
                          elapsed_seconds=result['elapsed_seconds'],
                          peak_RSS_KiB=peak)),flush=True)


if __name__ == '__main__':
    main()
