#!/usr/bin/env python3
"""Complete the missing suffix of the one signed raw-centre mean retraction.

Public Actions only.  The complete old 7721-row scalar-mean native is read
unchanged.  No old Green, response, target, angular or candidate producer
is called.  The new flow holds the original u and j=v/mean(v) fixed and
sets the waist mean to -a(0), at the original nu0 and over the entire
original affine parameter interval.  It is not the selected delta family.
The saved 6791-cell successful prefix is consumed without recomputation.
Only the unfinished suffix is advanced, using positive endpoint reciprocal
bounds instead of division by a wide positive centered-ball product.
The whole signed enclosure and three-valued physical/1e-4 gates are saved
even when the old row ranges cannot decide them.  Detailed row data stay
in a temporary private trace; only its count and hash are published.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import time

REPO = 'Rogerhu12/math-research-public'
KIND = 'R144_raw_nu0_signed_forward_mean_retraction_v1'
NATIVE = 'e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b'
OLD_SOURCE = '6edd8abf820c4e11a25b496c08d0585fb7c943397e7f919ed3774a0b841b0d93'
CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
ALPHA = '6890507429876859/9007199254740992'
NU = '-2572625729470897/72057594037927936'
V0 = '1270129564654771/158456325028528675187087900672'
A0 = ['53436641/50000000', '1068732841/1000000000']
ROWS, JOINS = 7721, 6143
START = 6791
PREFIX_SHA = '478a807d1caf93fd441949eca6565c1188b34ab44ba007c37b2221ffbe21782f'
PREFIX_EXECUTION_SHA = '773e2e5eb43017e77a0a7460a697ebad30e55172a4f88c5cd01600cf3a326f1d'
PREFIX_SOURCE_SHA = 'cdac407570960062945c6d846d7a14d04bcbb50945b03e5fd4ef3c745f82538f'
PREFIX_RUN = '45770488571'
ZEROS = ('old_scientific_targets_called old_mean_Green_targets_called '
         'old_response_targets_called old_target_ODE_calls old_angular_solver_calls '
         'published_arrays').split()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'),
                       ensure_ascii=False, allow_nan=False)+'\n').encode('utf-8')


def atomic(path, raw):
    path = Path(path)
    temp = path.with_name(path.name+'.tmp')
    with temp.open('wb') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)


def parse(raw):
    return json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mean', type=Path, required=True)
    ap.add_argument('--waist', type=Path, required=True)
    ap.add_argument('--old-process', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--resume', type=Path, required=True)
    ap.add_argument('--resume-execution', type=Path, required=True)
    args = ap.parse_args()
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_REPOSITORY') == REPO,
            'scientific execution only in the authorized public Actions repository')
    require(not args.output.exists(), 'preserve every old complete, false and partial output')
    from flint import arb, ctx
    ctx.prec = 320
    began = time.monotonic()

    def rat(value):
        q = Fraction(value)
        return arb(q.numerator)/arb(q.denominator)

    def old_ball(value):
        require(isinstance(value, dict) and 'lower' in value and 'upper' in value,
                'complete original lower/upper scalar record')
        z = arb(value['lower']).lower().union(arb(value['upper']).upper())
        require(z.is_finite(), 'finite complete original scalar')
        return z

    def unpack(value):
        e = int(value['decimal_exponent'])
        scale = rat(10**e) if e >= 0 else rat(Fraction(1, 10**(-e)))
        m, r = rat(int(value['midpoint_integer']))*scale, rat(int(value['radius_integer']))*scale
        return (m-r).lower().union((m+r).upper())

    def recorded(value, direction='enclosure'):
        require(value.is_finite(), 'finite complete new scalar')
        m, r, e = value.mid_rad_10exp(75)
        result = dict(kind='complete_decimal_ball_v1', mathematical_direction=direction,
                      midpoint_integer=str(int(m)), radius_integer=str(int(r)),
                      decimal_exponent=str(int(e)))
        require(int(r) >= 0 and unpack(result).contains(value),
                'whole saved decimal scalar contains the directed Arb value')
        return result

    def nonnegative(value):
        require(value.upper() >= 0, 'known nonnegative true scalar lost its enclosure')
        return value.intersection(arb(0).union(value.upper()))

    def symmetric(radius):
        require(radius >= 0, 'nonnegative interface enclosure radius')
        return (-radius).lower().union(radius.upper())

    def positive_inverse_kernel(n, Y):
        # A centered-ball product of wide positive factors can contain zero.
        # Monotone endpoint bounds never invert such a wide product.
        nl, nu = n.lower(), n.upper()
        yl, yu = Y.lower(), Y.upper()
        require(nl > 0 and yl > 0, 'strict positive mean-ratio inputs')
        snl, snu = nl.sqrt().lower(), nu.sqrt().upper()
        syl, syu = yl.sqrt().lower(), yu.sqrt().upper()
        lower_denominator = (syl*(snl+syl)).lower()
        upper_denominator = (syu*(snu+syu)).upper()
        require(lower_denominator > 0 and upper_denominator > 0,
                'explicit positive endpoint denominator bounds')
        lo, hi = (1/upper_denominator).lower(), (1/lower_denominator).upper()
        return lo.union(hi), hi, lower_denominator

    doc = dict(identity=dict(kind=KIND, source_sha256=sha(Path(__file__).read_bytes()),
            original_mean_native_sha256=NATIVE, original_mean_source_sha256=OLD_SOURCE,
            original_candidate_sha256=CANDIDATE, exact_alpha=ALPHA, exact_nu=NU,
            original_parameter_half_width='1/1000000000',
            arithmetic_bits=320, original_modes=32, exact_interval=['0', '25/8'],
            fixed_shape='u_raw and j_raw=v_raw/mean_phi(v_raw)',
            initial_condition='Y_flat(0)=1; Y=a^2/m^2',
            new_error_equation="D'=2 beta <u_raw^2> D - tau R0; D+ = D- - [n]",
            original_sources_and_jumps_kept=True),
        complete=False, proved=False, failure=None, stage='input-admission',
        expected_common_cells=ROWS, completed_common_cells=0,
        expected_mean_interfaces=JOINS, completed_mean_interfaces=0,
        current_exact_right='0', complete_new_scalars={},
        continuation=dict(original_run_id=PREFIX_RUN, original_prefix_sha256=PREFIX_SHA,
            original_execution_sha256=PREFIX_EXECUTION_SHA, original_source_sha256=PREFIX_SOURCE_SHA,
            requested_first_unfinished_row=START, expected_new_cells=ROWS-START,
            completed_old_prefix_rows_recomputed=0, completed_new_cells=0,
            prefix_witness_history_not_available=True,
            absence_of_prefix_witness_not_interpreted_as_no_violation=True),
        strict_gates=dict(positive_mean_everywhere='unknown',
            componentwise_moving_C0_within_1e4='unknown', outer_mean_unchanged='unknown'),
        scope=dict(original_Qraw_nu0_only=True, original_entire_affine_parameter_interval=True,
            same_u_and_material_density_j=True, mean_interfaces_retained=True,
            detailed_rows_private_only=True, full_signed_forward_target_complete=False,
            old_Gamma_or_backward_mean_gain_recomputed=False,
            true_point_eta0_correlated_integral=False, Qrepair_or_selected_delta_inherited=False,
            selected_phase_preserved=False, nonmean_equations_solved=False,
            outer_cap_or_height_matched=False, body_inverse_proved=False, final_topic_complete=False),
        private_trace=dict(records=0, bytes=0, sha256=None, content_published=False),
        seconds=0.0, **{key: 0 for key in ZEROS})
    trace = args.output.with_name('private-forward-mean-retraction.ndjson')
    trace_hash = hashlib.sha256()
    trace_bytes, trace_records = 0, 0
    prefix_trace = None
    doc['identity']['old_process_sha256'] = sha(args.old_process.read_bytes())
    doc['identity']['waist_record_sha256'] = sha(args.waist.read_bytes())
    atomic(args.output, encode(doc))

    def snapshot():
        segment = dict(kind='new_unfinished_suffix_trace', records=trace_records,
            bytes=trace_bytes, sha256=trace_hash.hexdigest())
        segments = ([dict(kind='immutable_original_completed_prefix_trace', **prefix_trace)]
                    if prefix_trace is not None else [])+[segment]
        doc['private_trace'] = dict(
            records=sum(item['records'] for item in segments),
            bytes=sum(item['bytes'] for item in segments),
            sha256=None, content_published=False, segments=segments,
            metadata_chain_sha256=sha(encode(segments)),
            concatenated_content_sha256_not_claimed=True)
        doc['continuation']['completed_new_cells'] = trace_records
        doc['seconds'] = time.monotonic()-began
        atomic(args.output, encode(doc))

    try:
        raw = args.mean.read_bytes()
        require(sha(raw) == NATIVE, 'the exact complete original native container')
        native = parse(gzip.decompress(raw))
        old_process = parse(args.old_process.read_bytes())
        require(old_process['complete'] is True and old_process['actual_returncode'] == 0
                and old_process['result_complete'] is True and old_process['result_failure'] is None
                and old_process['out_sha256'] == NATIVE
                and old_process['source_sha256'] == OLD_SOURCE
                and old_process['completed_rows'] == ROWS
                and old_process['total_closed_cells'] == ROWS,
                'unchanged completed old scalar-mean process')
        require(native['kind'] == 'actual_final_complete_scalar_mean_Green_cached_full_target'
                and native['complete'] is True and native['failure'] is None
                and native['source_sha256'] == OLD_SOURCE
                and native['candidate_sha256'] == CANDIDATE
                and native['exact_amplitude'] == ALPHA and native['exact_nu'] == NU
                and native['exact_interval'] == ['0', '25/8']
                and native['original_parameter_half_width'] == '1/1000000000'
                and native['whole_original_affine_parameter_interval'] is True
                and native['all_exact_mean_interfaces_retained'] is True
                and native['candidate_metadata']['modes'] == 32
                and len(native['rows']) == ROWS and len(native['interfaces']) == JOINS,
                'complete original raw-centre source, parameter and interface identity')
        waist = parse(args.waist.read_bytes())
        require(waist['kind'] == 'actual_final_waist_complete_amplitude_coordinate_rational_certificate'
                and waist['complete'] is True and waist['candidate_sha256'] == CANDIDATE
                and waist['exact_alpha'] == ALPHA
                and waist['exact_full_V_coefficients'][0] == V0
                and waist['exact_target_waist_radius_enclosure'] == A0
                and waist['whole_original_affine_parameter_interval'] is True
                and waist['actual_nu_bump_identically_zero_at_waist'] is True,
                'the completed exact raw waist initial mean and original radius enclosure')
        rows, jumps = native['rows'], native['interfaces']
        jump_map = {item['common_row']: item for item in jumps}
        require(len(jump_map) == JOINS, 'all distinct original mean joins')
        prefix_raw = args.resume.read_bytes()
        execution_raw = args.resume_execution.read_bytes()
        require(sha(prefix_raw) == PREFIX_SHA and sha(execution_raw) == PREFIX_EXECUTION_SHA,
                'exact immutable failed-run output and execution receipt')
        prefix, execution = parse(prefix_raw), parse(execution_raw)
        require(prefix['complete'] is False and prefix['proved'] is False
                and prefix['failure'] == dict(type='ValueError', message='finite complete new scalar')
                and prefix['stage'] == 'whole-signed-forward-flow'
                and prefix['completed_common_cells'] == START
                and prefix['expected_common_cells'] == ROWS
                and prefix['expected_mean_interfaces'] == JOINS
                and prefix['identity']['source_sha256'] == PREFIX_SOURCE_SHA
                and prefix['identity']['kind'] == KIND
                and prefix['identity']['original_mean_native_sha256'] == NATIVE
                and prefix['identity']['original_candidate_sha256'] == CANDIDATE
                and prefix['identity']['exact_alpha'] == ALPHA
                and prefix['identity']['exact_nu'] == NU
                and prefix['identity']['original_parameter_half_width'] == '1/1000000000'
                and all(prefix[key] == 0 for key in ZEROS),
                'actual successful 6791-cell prefix of the same unfinished target')
        require(execution['repository'] == REPO and execution['run_id'] == PREFIX_RUN
                and str(execution['run_attempt']) == '1'
                and execution['complete'] is False and execution['actual_child_returncode'] == 1
                and execution['scientific_children'] == 1
                and execution['old_completed_targets_recomputed'] == 0
                and execution['old_numerical_producers_called'] == 0
                and len(execution['scientific_files']) == 1
                and execution['scientific_files'][0]['sha256'] == PREFIX_SHA
                and execution['scientific_files'][0]['bytes'] == len(prefix_raw),
                'actual failed public child with complete saved successful prefix')
        previous_row, first_row = rows[START-1], rows[START]
        require(prefix['current_exact_right'] == previous_row['interval'][1]
                and prefix['current_exact_right'] == first_row['interval'][0]
                and previous_row['common_row'] == START-1 and first_row['common_row'] == START,
                'saved scalar state is exactly the first unfinished left endpoint')
        prefix_interface_count = sum(1 for key in jump_map if key < START)
        possible_partial_increment = int(START in jump_map)
        reported_interfaces = prefix['completed_mean_interfaces']
        require(prefix_interface_count <= reported_interfaces <=
                    prefix_interface_count+possible_partial_increment,
                'failed partial-row counter reconciled with immutable native join locations')
        old = prefix['complete_new_scalars']
        needed = {'initial_D', 'D_at_current_right', 'forward_multiplier_at_current_right',
            'propagated_initial_at_current_right', 'signed_bulk_at_current_right',
            'mean_interface_at_current_right', 'Y_lower_over_completed_cells',
            'v_difference_upper_on_positive_certified_cells'}
        require(set(old) == needed, 'all actual complete saved prefix scalars retained')
        D0 = unpack(old['initial_D'])
        D = unpack(old['D_at_current_right'])
        G = unpack(old['forward_multiplier_at_current_right'])
        bulk = unpack(old['signed_bulk_at_current_right'])
        atoms = unpack(old['mean_interface_at_current_right'])
        D = D.intersection(G*D0+bulk+atoms)
        y_lower = unpack(old['Y_lower_over_completed_cells']).lower()
        v_upper = unpack(old['v_difference_upper_on_positive_certified_cells']).upper()
        require(G > 0 and y_lower > 0 and v_upper >= 0,
                'this saved prefix proves positive Y and a whole C0 upper')
        all_positive, certified_outside, certified_nonpositive = True, False, False
        first_unknown, first_outside, violation_witness = None, None, None
        negative_Y_witness = None
        previous = dict(candidate_piece=previous_row['candidate_piece'],
            m=old_ball(previous_row['scalar_mean']['actual_m']),
            a=old_ball(previous_row['actual_target']['a']))
        rightmost = Fraction(prefix['current_exact_right'])
        last_Y = last_mean_shift = None
        raw_trace = prefix['private_trace']
        require(raw_trace['records'] == START and raw_trace['content_published'] is False
                and raw_trace['bytes'] == 19064094
                and raw_trace['sha256'] == '361ed5fcedde835356c885aea5951e63818e90a271b9fc2d3616f9fa7be6c763',
                'unchanged original private completed-prefix trace metadata')
        prefix_trace = {key: raw_trace[key] for key in ('records', 'bytes', 'sha256')}
        doc['complete_new_scalars'] = dict(old)
        doc['completed_common_cells'] = START
        doc['completed_mean_interfaces'] = prefix_interface_count
        doc['current_exact_right'] = str(rightmost)
        doc['continuation'].update(original_reported_interface_count=reported_interfaces,
            verified_completed_prefix_interfaces=prefix_interface_count,
            unconsumed_failed_row_counter_increment=reported_interfaces-prefix_interface_count,
            resume_exact_radius=str(rightmost),
            prefix_positive_Y_proved_from_saved_lower=True,
            prefix_v_upper_is_not_a_lower_or_violation=True,
            original_prefix_scope=prefix['scope'])
        doc['stage'] = 'whole-signed-forward-flow'
        with trace.open('wb') as stream:
            for i in range(START, len(rows)):
                row = rows[i]
                left, right = map(Fraction, row['interval'])
                require(row['common_row'] == i and left == rightmost and left < right,
                        'complete adjacent original closed radial cover')
                gl, gr = map(Fraction, row['actual_scalar_germ'])
                require(gl <= left < right <= gr, 'unchanged full original scalar germ')
                z = {key: old_ball(value) for key, value in row['scalar_mean'].items()}
                a = {key: old_ball(value) for key, value in row['actual_target'].items()}
                m, n, tau = z['actual_m'], z['n'], z['mean_transform_tau']
                require(a['a'] > 0 and m < 0 and n > 0 and tau > 0,
                        'the complete old mean chart remains strictly resolved')
                U, V = nonnegative(z['nonmean_u_square']), nonnegative(z['nonmean_v_square'])
                c, f = 2*a['beta']*U, -tau*z['actual_mean_residual']
                jump_fee = arb(0)
                changed = previous is not None and previous['candidate_piece'] != row['candidate_piece']
                require((i in jump_map) is changed,
                        'exactly the complete original candidate mean-interface locations')
                if changed:
                    item = jump_map[i]
                    require(item['radius'] == str(left)
                            and item['candidate_join'] == row['candidate_piece'],
                            'same whole original mean join')
                    dm = abs(old_ball(item['exact_mean_jump_abs'])).upper()
                    gap = min((-previous['m']).lower(), (-m).lower()).lower()
                    aa = min(previous['a'].upper(), a['a'].upper()).upper()
                    require(gap > 0 and aa > 0, 'both one-sided original negative means')
                    jump_fee = (2*aa**2*dm/gap**3).upper()
                    jump_box = symmetric(jump_fee)
                    D += jump_box
                    atoms += jump_box
                    doc['completed_mean_interfaces'] += 1
                length = rat(right-left)
                partial_time = arb(0).union(length.upper())
                all_exponents = partial_time*c
                Epartial = all_exponents.exp()
                # Every exp(int_s^t c) belongs to Epartial, which is positive.
                # For the complete endpoint t=length the integration length
                # is exact.  For a whole-cell tube it ranges from 0 to length.
                Kend = length*Epartial
                Kpartial = partial_time*Epartial
                Dstart = D
                Dtube = Epartial*Dstart+Kpartial*f
                Eend = (length*c).exp()
                D = Eend*Dstart+Kend*f
                G = Eend*G
                bulk = Eend*bulk+Kend*f
                atoms = Eend*atoms
                D = D.intersection(G*D0+bulk+atoms)
                Ytube, Yend = n+Dtube, n+D
                y_lower = Ytube.lower() if y_lower is None else min(y_lower, Ytube.lower()).lower()
                physical = bool(Ytube > 0)
                cell_v_bound = mean_shift = None
                if physical:
                    kernel, kernel_upper, denominator_lower = positive_inverse_kernel(n, Ytube)
                    ratio_abs = (abs(Dtube).upper()*kernel_upper).upper()
                    # The raw candidate has exactly M=32 cosine modes.
                    # Cauchy--Schwarz gives ||v_raw||inf <= |m|+sqrt(2 M V).
                    cell_v_bound = (((-m).upper()+(64*V.upper()).sqrt().upper())*ratio_abs).upper()
                    v_upper = max(v_upper, cell_v_bound).upper()
                else:
                    all_positive = False
                    if first_unknown is None:
                        first_unknown = i
                if Yend > 0:
                    kernel, kernel_upper, denominator_lower = positive_inverse_kernel(n, Yend)
                    mean_shift = (-m*D)*kernel
                    if i == START:
                        unsafe_denominator = Yend.sqrt()*(n.sqrt()+Yend.sqrt())
                        unsafe_quotient = -m*D/unsafe_denominator
                        doc['continuation']['first_unfinished_inverse_diagnostic'] = dict(
                            row=i, n_positive=bool(n > 0), Y_positive=bool(Yend > 0),
                            old_centered_denominator_contains_zero=bool(unsafe_denominator.contains(0)),
                            old_quotient_finite=bool(unsafe_quotient.is_finite()),
                            new_positive_denominator_lower=recorded(denominator_lower, 'lower'),
                            new_inverse_kernel=recorded(kernel), new_mean_shift_finite=bool(mean_shift.is_finite()))
                    saved_shift_lower = recorded(abs(mean_shift).lower(), 'lower')
                    if unpack(saved_shift_lower).lower() > rat('1/10000'):
                        certified_outside = True
                        if first_outside is None:
                            first_outside = i
                            violation_witness = dict(row=i, radius=str(right),
                                kind='absolute_mean_shift_strict_lower',
                                value=saved_shift_lower)
                elif Yend.upper() < 0:
                    saved_Y_upper = recorded(Yend.upper(), 'upper')
                    if unpack(saved_Y_upper).upper() < 0:
                        certified_outside = certified_nonpositive = True
                        if negative_Y_witness is None:
                            negative_Y_witness = dict(row=i, radius=str(right),
                                kind='negative_Y_strict_upper', value=saved_Y_upper)
                        if first_outside is None:
                            first_outside = i
                            violation_witness = negative_Y_witness
                event = dict(common_row=i, interval=row['interval'],
                    candidate_piece=row['candidate_piece'],
                    c=recorded(c), signed_forcing=recorded(f),
                    mean_interface_radius=recorded(jump_fee, 'upper'),
                    D_at_left_after_interface=recorded(Dstart),
                    D_tube=recorded(Dtube), D_at_right=recorded(D),
                    Y_tube=recorded(Ytube), Y_at_right=recorded(Yend),
                    v_difference_upper=None if cell_v_bound is None else recorded(cell_v_bound, 'upper'),
                    physical_mean_on_whole_cell=physical)
                payload = encode(event)
                stream.write(payload)
                trace_hash.update(payload)
                trace_bytes += len(payload)
                trace_records += 1
                previous = dict(candidate_piece=row['candidate_piece'], m=m, a=a['a'])
                rightmost = right
                last_Y, last_mean_shift = Yend, mean_shift
                doc['completed_common_cells'] = i+1
                doc['current_exact_right'] = str(right)
                doc['complete_new_scalars'].update(
                    D_at_current_right=recorded(D),
                    forward_multiplier_at_current_right=recorded(G),
                    propagated_initial_at_current_right=recorded(G*D0),
                    signed_bulk_at_current_right=recorded(bulk),
                    mean_interface_at_current_right=recorded(atoms),
                    Y_lower_over_completed_cells=recorded(y_lower, 'lower'),
                    v_difference_upper_on_positive_certified_cells=recorded(v_upper, 'upper'))
                if (i+1) % 256 == 0:
                    stream.flush()
                    snapshot()
                    print(json.dumps(dict(completed_cells=i+1, right=str(right),
                        completed_mean_interfaces=doc['completed_mean_interfaces'])), flush=True)
            stream.flush()
            os.fsync(stream.fileno())
        require(rightmost == Fraction(25, 8)
                and doc['completed_mean_interfaces'] == JOINS
                and START+trace_records == ROWS, 'the entire original forward target completed')
        whole_upper = v_upper if all_positive else None
        doc['complete_new_scalars'].update(
            D_at_R=recorded(D), Y_at_R=recorded(last_Y),
            whole_v_difference_upper=None if whole_upper is None else recorded(whole_upper, 'upper'),
            mean_shift_at_R=None if last_mean_shift is None else recorded(last_mean_shift),
            first_unresolved_positivity_row=first_unknown,
            first_certified_outside_ball_row=first_outside,
            certified_violation_witness=violation_witness,
            certified_negative_Y_witness=negative_Y_witness)
        # Save complete signed enclosures before making the final gates.
        snapshot()
        saved = parse(args.output.read_bytes())
        require(saved['completed_common_cells'] == ROWS
                and saved['completed_mean_interfaces'] == JOINS
                and saved['current_exact_right'] == '25/8'
                and saved['private_trace']['records'] == ROWS,
                'actual saved complete whole-flow conclusion read back before gates')
        saved_scalars = saved['complete_new_scalars']
        saved_upper = saved_scalars['whole_v_difference_upper']
        positive_saved = bool(unpack(saved_scalars['Y_lower_over_completed_cells']).lower() > 0)
        witness = saved_scalars['certified_violation_witness']
        outside_saved = False
        if witness is not None:
            value = unpack(witness['value'])
            outside_saved = ((witness['kind'] == 'absolute_mean_shift_strict_lower'
                and value.lower() > rat('1/10000')) or
                (witness['kind'] == 'negative_Y_strict_upper' and value.upper() < 0))
        negative_witness = saved_scalars['certified_negative_Y_witness']
        negative_saved = (negative_witness is not None
            and unpack(negative_witness['value']).upper() < 0)
        close = True if (positive_saved and saved_upper is not None
            and unpack(saved_upper).upper() <= rat('1/10000')) else (
            False if outside_saved else 'unknown')
        physical_gate = True if positive_saved else (False if negative_saved else 'unknown')
        saved_D = unpack(saved_scalars['D_at_R'])
        outer_same = False if saved_D.lower() > 0 or saved_D.upper() < 0 else 'unknown'
        if saved_D == 0:
            outer_same = True
        doc['strict_gates'] = dict(positive_mean_everywhere=physical_gate,
            componentwise_moving_C0_within_1e4=close, outer_mean_unchanged=outer_same,
            comparison_radius='1/10000',
            true_means_whole_upper_proved=True,
            false_means_certified_violation_for_every_original_parameter=True,
            unknown_means_only_saved_ranges_are_insufficient=True,
            all_complete_signed_scalars_saved_before_gates=True)
        doc['complete'] = doc['proved'] = True
        doc['stage'] = 'complete-original-raw-nu0-signed-forward-mean-retraction'
        doc['continuation']['complete_suffix_without_prefix_recomputation'] = True
        doc['scope']['full_signed_forward_target_complete'] = True
    except BaseException as exc:
        doc['failure'] = dict(type=type(exc).__name__, message=str(exc))
        raise
    finally:
        snapshot()
    print(json.dumps(dict(complete=doc['complete'], proved=doc['proved'],
        rows=doc['completed_common_cells'], gates=doc['strict_gates'],
        output_sha256=sha(args.output.read_bytes()))), flush=True)


if __name__ == '__main__':
    main()
