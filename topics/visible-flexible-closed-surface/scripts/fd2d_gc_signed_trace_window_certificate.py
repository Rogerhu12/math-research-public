"""Continuous positive-K windows for one explicitly saved R171 target.

Only the scalar accurate profile is evaluated.  The proof uses the frozen
R175 Bernstein enclosure, with a finite exact cover and explicit bounds
for changes of the seven physical bump coefficients.  No raw field,
Gauss--Codazzi system, body ODE, Jacobian or existing solver is changed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
import traceback

from flint import ctx
import numpy as np

from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_current_native_interval import aq, bound_record, rational, rational_pair
from fd2d_gc_r136_arb_profile import ends
from fd2d_gc_r136_bernstein_bumps import BernsteinBumpProfile, exact_bump_range


WINDOWS = (
    dict(name='middle_positive', sign=1, binary_endpoints=(.90, .915, .985, .99)),
    dict(name='late_negative', sign=-1, binary_endpoints=(1.423, 1.428, 1.442, 1.445)),
)


def exact_record(value):
    value = F(value)
    return dict(exact=rational_pair(value), display=float(value))


def positive_dyadic_below(value):
    value = F(value)
    if value <= 0:
        raise ValueError('A positive margin is required')
    q = F(1)
    while q > value:
        q /= 2
    return q


def cover(profile, left, right, maximum_width, *, expected_sign):
    """Every exact cover member is retained; no sample is used as a bound."""
    left, right, maximum_width = map(F, (left, right, maximum_width))
    ratio = (right-left)/maximum_width
    count = max(1, (ratio.numerator+ratio.denominator-1)//ratio.denominator)
    points = [left+(right-left)*F(j, count) for j in range(count+1)]
    rows = []
    for index, (lo, hi) in enumerate(zip(points, points[1:])):
        q = profile.physical_box(lo, hi)
        if q['K'] is None or not q['target_metric_positive_on_box']:
            raise ArithmeticError('The actual target radius is unresolved')
        kl, ku = ends(q['K'])
        if expected_sign == 1 and not kl > 0:
            raise ArithmeticError(f'Positive K is unresolved on {lo}, {hi}')
        if expected_sign == -1 and not ku < 0:
            raise ArithmeticError(f'Negative K is unresolved on {lo}, {hi}')
        row = dict(index=index, interval=[rational_pair(lo), rational_pair(hi)],
                   a=bound_record(q['a']), K=bound_record(q['K']),
                   a_ss=bound_record(q['a_ss']),
                   base_a_ss=bound_record(q['base_jets'][2]),
                   possible_accurate_pieces=q['piece_indices'])
        if expected_sign == 1:
            margin = -ends(q['a_ss'])[1]
            if not margin > 0:
                raise ArithmeticError('K sign and a_ss sign enclosure disagree')
            basis = [exact_bump_range(lo, hi, a, b, 2) for a, b in profile.supports]
            absolute = [max(abs(x) for x in ends(v)) for v in basis]
            row.update(second_derivative_basis=[bound_record(v) for v in basis],
                       derivative_absolute_bounds=[rational_pair(v) for v in absolute],
                       current_a_ss_negative_margin=rational_pair(margin),
                       perturbation_budget=rational_pair(margin/2))
        rows.append(row)
    return rows


def decode_pair(pair):
    return F(int(pair[0]), int(pair[1]))


def bound_ends(record):
    # The stable public interval record contains exact dyadic endpoints.
    def binary(pair):
        mantissa, exponent = int(pair[0]), int(pair[1])
        return F(mantissa)*(F(2)**exponent)
    return binary(record['lower_binary']), binary(record['upper_binary'])


def window_summary(profile, raw, rows, mesh):
    A, B, C, D = map(rational, raw['binary_endpoints'])
    radius_lower = profile.base_lower+sum((min(F(0), v) for v in profile.delta), F(0))
    uniform_candidates = [radius_lower/(2*len(profile.delta))]
    basis_active = set()
    for row in rows:
        absolute = list(map(decode_pair, row['derivative_absolute_bounds']))
        total = sum(absolute, F(0))
        basis_active.update(j for j, v in enumerate(absolute) if v > 0)
        if total:
            uniform_candidates.append(decode_pair(row['perturbation_budget'])/total)
    uniform = positive_dyadic_below(min(uniform_candidates))
    min_a_ss_margin = min(decode_pair(r['current_a_ss_negative_margin']) for r in rows)
    max_a = max(bound_ends(r['a'])[1] for r in rows)
    result = dict(name=raw['name'], sign=int(raw['sign']),
        endpoints=[exact_record(v) for v in (A, B, C, D)],
        support_scope='w>0 exactly on (A,D); both endpoints have w=w_s=w_ss=0',
        plateau_scope='w=1 on the closed interval [B,C]',
        weight='S5 rising on [A,B], 1 on [B,C], 1-S5 falling on [C,D], 0 elsewhere',
        step_polynomial='10*t^3-15*t^4+6*t^5',
        exact_cover_rows=len(rows), complete_closed_support_positive_K=True,
        current_K_lower=exact_record(min(bound_ends(r['K'])[0] for r in rows)),
        current_K_upper=exact_record(max(bound_ends(r['K'])[1] for r in rows)),
        active_bump_parameter_indices_zero_based=sorted(basis_active),
        uniform_delta_linf_radius=exact_record(uniform),
        uniform_neighborhood_K_lower=exact_record(
            (min_a_ss_margin/2)/(max_a+len(profile.delta)*uniform)),
        neighborhood_rule='For every row: sum_j B_ij*abs(delta_j-new_center_j) <= margin_i/2; also sum_j abs(change_j) < current global radius lower. The stated uniform box is a simpler closed sufficient subset.',
        complete_P1_hat_indices_in_plateau=[j for j in range(1,len(mesh)-1)
            if B <= rational(mesh[j-1]) and rational(mesh[j+1]) <= C],
        node_indices_in_plateau=[j for j,v in enumerate(mesh) if B <= rational(v) <= C],
        partial_hats_not_removed=True)
    # A useful sharper one-sided condition, when only one convex-end bump
    # is active.  Its base is independent of every current delta.
    if len(basis_active) == 1:
        j = next(iter(basis_active))
        limits = []
        eligible = True
        for row in rows:
            bl, bu = bound_ends(row['second_derivative_basis'][j])
            base_upper = bound_ends(row['base_a_ss'])[1]
            if bl < 0 or bu <= 0 or base_upper >= 0:
                eligible = False
                break
            limits.append(-base_upper/bu)
        if eligible and min(limits) > profile.delta[j]:
            cap = (min(limits)+profile.delta[j])/2
            # A simple exact decimal upper bound remains above the actual
            # center when possible.  Rounding is always downwards.
            simple = F((cap*10**6).numerator//(cap*10**6).denominator, 10**6)
            if simple > profile.delta[j]:
                cap = simple
            result['one_sided_parameter_condition'] = dict(
                parameter_index_zero_based=j, delta_upper=exact_record(cap),
                other_parameters_do_not_act_on_this_support=True,
                radius_positivity_still_required=True,
                a_ss_upper=exact_record(max(
                    bound_ends(row['base_a_ss'])[1]+cap*bound_ends(row['second_derivative_basis'][j])[1]
                    for row in rows)),
                reason='The only active bump has nonnegative second derivative throughout every exact support box; the analytic base has strictly negative a_ss.')
    return result


def run(args):
    started = time.monotonic()
    ctx.prec = int(args.precision)
    report_path = args.out_prefix.with_name(args.out_prefix.name+'-report.json')
    rows_path = args.out_prefix.with_name(args.out_prefix.name+'-rows.json.gz')
    if report_path.exists() or rows_path.exists():
        raise FileExistsError('Use an immutable new output stem')
    args.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    report = dict(schema='fd2d-R182-signed-disjoint-positive-K-window-certificate-v1',
        source=identity(__file__), profile_packet=identity(args.profile_packet),
        actual_field=identity(args.field), passed=False,
        field_Jacobian_BVP_or_body_evaluated=False,
        old_or_active_solver_source_changed=False)
    try:
        if report['actual_field']['sha256'] != args.field_sha256:
            raise ValueError('Unexpected actual field archive')
        profile = BernsteinBumpProfile.from_packet(args.profile_packet,
            expected_sha256=args.profile_sha256)
        if profile.inputs['field_arrays']['sha256'] != args.field_sha256:
            raise ValueError('The accurate profile belongs to another actual delta')
        arrays = load_npz(args.field)
        mesh = np.asarray(arrays['mesh'])
        if not np.all(np.diff(mesh)>0):
            raise ValueError('A strictly increasing saved mesh is required')
        report.update(profile_input_binding_sha256=profile.input_binding_sha256,
            enclosure_backend=identity(Path(__file__).with_name('fd2d_gc_r136_bernstein_bumps.py')),
            center_delta_exact=[rational_pair(v) for v in profile.delta],
            bump_supports_exact=[[rational_pair(v) for v in pair] for pair in profile.supports],
            saved_mesh_count=len(mesh),
            exact_global_radius_lower=exact_record(profile.base_lower+sum(
                (min(F(0),v) for v in profile.delta),F(0))))
        all_rows = {}
        summaries = []
        for window in WINDOWS:
            A, B, C, D = map(rational, window['binary_endpoints'])
            if not A < B <= C < D:
                raise ValueError('Ordered support and plateau endpoints are required')
            width = F(1,1000) if window['name']=='middle_positive' else F(1,4000)
            rows = cover(profile,A,D,width,expected_sign=1)
            all_rows[window['name']] = rows
            summaries.append(window_summary(profile,window,rows,mesh))
        negative_rows = cover(profile,F(145,100),F(1462,1000),F(1,1000),expected_sign=-1)
        all_rows['negative_gap_witness'] = negative_rows
        report['windows'] = summaries
        report['common_delta_linf_radius'] = exact_record(min(
            decode_pair(s['uniform_delta_linf_radius']['exact']) for s in summaries))
        report['negative_gap_witness'] = dict(
            interval=[rational_pair(F(145,100)),rational_pair(F(1462,1000))],
            complete_closed_interval_negative_K=True,
            K_upper=exact_record(max(bound_ends(r['K'])[1] for r in negative_rows)),
            positive_K_bridge_to_old_terminal_window_claimed=False)
        old_trace = json.loads(str(arrays['positive_trace_definition']))
        report['unchanged_terminal_window'] = old_trace
        report['disjoint_from_existing_terminal_weight'] = bool(
            rational(WINDOWS[-1]['binary_endpoints'][-1]) < rational(old_trace['start']))
        if not report['disjoint_from_existing_terminal_weight']:
            raise ValueError('The new isolated window overlaps the old terminal window')
        report['selected_profile_points'] = [dict(node_index=j,s_exact=rational_pair(rational(mesh[j])),
            K=bound_record(profile.physical_box(rational(mesh[j]),rational(mesh[j]))['K']))
            for j in (84,118)]
        payload=(json.dumps(dict(schema='fd2d-R182-exact-cover-rows-v1',
            source=report['source'],profile_packet=report['profile_packet'],
            actual_field=report['actual_field'],rows=all_rows),sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()
        with rows_path.open('wb') as stream:
            with gzip.GzipFile(filename='',fileobj=stream,mode='wb',mtime=0) as out:
                out.write(payload)
        report['continuous_rows'] = dict(**identity(rows_path),uncompressed_bytes=len(payload),
            uncompressed_sha256=hashlib.sha256(payload).hexdigest())
        report['field_unchanged'] = identity(args.field)==report['actual_field']
        if not report['field_unchanged']:
            raise AssertionError('The immutable input changed during the scalar cover')
        report['passed'] = True
    except Exception as exc:
        report['error'] = dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        raise
    finally:
        report['seconds'] = time.monotonic()-started
        report['peak_rss_kib'] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
        print(json.dumps(dict(passed=report['passed'],report=str(report_path),
            seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib']),allow_nan=False))


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile-packet',type=Path,required=True)
    parser.add_argument('--profile-sha256',required=True)
    parser.add_argument('--field',type=Path,required=True)
    parser.add_argument('--field-sha256',required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--precision',type=int,default=256)
    run(parser.parse_args())
