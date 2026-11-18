#!/usr/bin/env python3
"""Compare stored 60/90 digit stage readouts; never rerun a point root or flow."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import struct
import mpmath as mp
from record_fixed_actual import load, scalar_tree, sha


mp.mp.dps = 140


def identity(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def packed(values):
    return struct.pack('<'+'d'*len(values), *values)


def text(value):
    return mp.nstr(value, 32)


SKELETON_FIELDS = {
    'rk_field': ('profile', 'step', 'label'),
    'root_start': (), 'evaluate_start': ('needJac',),
    'domain': ('n', 'D_pass', 'S_compared', 'S_pass', 'A_compared', 'A_pass'),
    'evaluate_end': (), 'spd_positive': ('i', 'positive'),
    'root_stop': ('iteration', 'accepted'), 'trial_start': ('k',),
    'trial_judgment': ('k', 'improves', 'tolerance_compared', 'within_tolerance', 'accepted'),
    'trial_caught': ('k', 'message'), 'fallback_judgment': ('accepted',),
    'root_return': ('iteration', 'roundoffFallback')}


def skeleton(events):
    h = hashlib.sha256()
    counts = {}
    for row in events:
        event = row['event']
        keys = SKELETON_FIELDS[event]
        record = dict(event=event, **{key: row[key] for key in keys})
        h.update((json.dumps(record, sort_keys=True, separators=(',', ':'))+'\n').encode())
        counts[event] = counts.get(event, 0)+1
    return h.hexdigest(), counts


def require_file(entry):
    if sha(entry['path']) != entry['sha256']:
        raise ValueError('A bound file differs: '+entry['path'])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mp60', type=Path, required=True)
    p.add_argument('--mp90', type=Path, required=True)
    p.add_argument('--resource60', type=Path, required=True)
    p.add_argument('--resource90', type=Path, required=True)
    p.add_argument('--log60', type=Path, required=True)
    p.add_argument('--log90', type=Path, required=True)
    p.add_argument('--float-baseline', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise ValueError('A completed comparison already exists')
    s60, s90, baseline = load(a.mp60), load(a.mp90), load(a.float_baseline)
    if s60['precision'] != s90['precision'] or s60['precision'] != 'mp' or (s60['dps'], s90['dps']) != (60, 90):
        raise ValueError('This is the declared 60/90 digit comparison')
    if (not baseline['all_original_operands_and_judgments_bitwise_identical'] or
            not baseline['all_three_outputs42_bitwise_identical']):
        raise ValueError('An exact original float baseline is required')
    for key in ('source_sha256', 'bridge_sha256', 'capsule_summary_sha256'):
        if not s60[key] == s90[key] == baseline[key]:
            raise ValueError('The two readouts differ from their accepted baseline: '+key)
    for summary in (s60, s90):
        if summary['validated_baseline_sha256'] != sha(a.float_baseline):
            raise ValueError('A readout used another float baseline')
        if sha(summary['command'][0]) != summary['source_sha256']:
            raise ValueError('The executed frozen evaluator source changed')
        for field in ('whole_tail_evaluated', 'nonlinear_tail_solver_invoked',
                      'physical_checkpoint_written', 'production_source_changed'):
            if summary[field]:
                raise ValueError('This comparison only supports the declared read-only scope')
        require_file(summary['raw'])
    capsule_summary = load(s60['capsule_summary_path'])
    if sha(s60['capsule_summary_path']) != s60['capsule_summary_sha256']:
        raise ValueError('The original capsule summary changed')
    for key in ('source_sha256', 'additional_original_root_sources'):
        for path, value in capsule_summary[key].items():
            if sha(path) != value:
                raise ValueError('An original bound source changed: '+path)
    for key in ('coefficients', 'reference', 'fixture', 'original_output', 'input'):
        require_file(capsule_summary[key])
    capsule = load(capsule_summary['coefficients']['path'])
    reference = load(capsule_summary['reference']['path'])
    raw60, raw90 = load(s60['raw']['path']), load(s90['raw']['path'])
    results = {}
    max_all42_cross = mp.mpf(0)
    all_same_rounded = all_same_decisions = True
    for fixture, original, low, high, old_scalar, low_scalar, high_scalar in zip(
            capsule['fixtures'], reference['rows'], raw60['rows'], raw90['rows'],
            baseline['named_results'], s60['named_results'], s90['named_results'], strict=True):
        stage = fixture['stage']
        if not stage == original['stage'] == low['stage'] == high['stage']:
            raise ValueError('Named stage differs between readouts')
        if len(low['state']) != 42 or len(high['state']) != 42:
            raise ValueError('Every state and both means must be retained')
        lo, hi = [mp.mpf(v) for v in low['state']], [mp.mpf(v) for v in high['state']]
        old = [mp.mpf(float(v)) for v in original['state']]
        target = [mp.mpf(float(v)) for v in fixture['targetNode40']]
        ratio = mp.mpf(float(fixture['portRatio']))
        scale = mp.mpf(float(fixture['normalizationScale']))
        low_physical = [v if j < 20 else v/ratio for j, v in enumerate(lo[:40])]
        high_physical = [v if j < 20 else v/ratio for j, v in enumerate(hi[:40])]
        old_physical = [v if j < 20 else v/ratio for j, v in enumerate(old[:40])]
        low_residual = [v-target[j] for j, v in enumerate(low_physical)]
        high_residual = [v-target[j] for j, v in enumerate(high_physical)]
        lo_peak = max(range(40), key=lambda j: abs(low_residual[j]))
        hi_peak = max(range(40), key=lambda j: abs(high_residual[j]))
        cross = [lo[j]-hi[j] for j in range(42)]
        difference = [hi[j]-old[j] for j in range(42)]
        old_peak = old_scalar['peak_component']
        signed_move = high_physical[old_peak]-old_physical[old_peak]
        original_ulp = mp.mpf(math.ulp(float(old_physical[old_peak])))
        rounded60, rounded90 = [float(v) for v in lo], [float(v) for v in hi]
        same_rounded = packed(rounded60) == packed(rounded90)
        all_same_rounded = all_same_rounded and same_rounded
        rounded_physical = [v if j < 20 else v/fixture['portRatio'] for j, v in enumerate(rounded90[:40])]
        rounded_residual = [v-fixture['targetNode40'][j] for j, v in enumerate(rounded_physical)]
        rounded_peak = max(range(40), key=lambda j: abs(rounded_residual[j]))
        sk_old, count_old = skeleton(original['events'])
        sk_low, count_low = skeleton(low['events'])
        sk_high, count_high = skeleton(high['events'])
        same_decisions = sk_low == sk_high
        all_same_decisions = all_same_decisions and same_decisions
        maximum_cross = max(map(abs, cross))
        max_all42_cross = max(max_all42_cross, maximum_cross)
        results[str(stage)] = dict(
            original_normalized_residual=old_scalar['normalized_residual'],
            mp60_normalized_residual=text(max(map(abs, low_residual))/scale),
            mp90_normalized_residual=text(max(map(abs, high_residual))/scale),
            mp60_peak_component=lo_peak, mp90_peak_component=hi_peak,
            mp90_peak_physical_mode=(hi_peak % 20+1)*4,
            original_peak_component=old_peak, original_peak_physical_mode=(old_peak % 20+1)*4,
            mp90_signed_residual_at_original_peak=text(high_residual[old_peak]),
            mp90_flow_move_at_original_peak=text(signed_move),
            mp90_flow_move_at_original_peak_over_original_ulp=text(signed_move/original_ulp),
            ulp_scope='Ratio to math.ulp of the original binary64 flow; not a count of prescribed nextafter updates or a precision lower bound.',
            mp60_to_mp90_maximum_all42_difference=text(maximum_cross),
            mp60_to_mp90_maximum_mean2_difference=text(max(map(abs, cross[40:]))),
            mp60_to_mp90_maximum_normalized_physical_difference=text(max(abs(a-b)/scale for a, b in zip(low_physical, high_physical))),
            mp90_to_original_maximum_all42_difference=text(max(map(abs, difference))),
            mp90_to_original_maximum_mean2_difference=text(max(map(abs, difference[40:]))),
            all42_round_to_same_binary64=same_rounded,
            rounded42_sha256=hashlib.sha256(packed(rounded90)).hexdigest(),
            original42_sha256=original['state42_sha256'],
            rounded_binary64_normalized_residual=max(map(abs, rounded_residual))/fixture['normalizationScale'],
            rounded_binary64_peak_component=rounded_peak,
            mp90_fixed_target_stage_maximum_below_reference_gate=max(map(abs, high_residual))/scale < mp.mpf(float(capsule['original_tail_gate'])),
            stage_gate_scope='A readout of this isolated stage at its fixed target only; not original-worker or complete-tail acceptance.',
            root_decision_sequences_equal_60_90=same_decisions,
            root_decision_sequence_equal_original=sk_high == sk_old,
            root_decision_sha256_original=sk_old, root_decision_sha256_mp60=sk_low, root_decision_sha256_mp90=sk_high,
            root_event_counts_original=count_old, root_event_counts_mp60=count_low, root_event_counts_mp90=count_high,
            mp60_root_iterations=low_scalar['root_iteration_counts'],
            mp90_root_iterations=high_scalar['root_iteration_counts'],
            mp60_root_roundoff_fallbacks=low_scalar['root_roundoff_fallbacks'],
            mp90_root_roundoff_fallbacks=high_scalar['root_roundoff_fallbacks'],
            mp60_maximum_reported_root_relative_residual=low_scalar['maximum_reported_root_relative_residual'],
            mp90_maximum_reported_root_relative_residual=high_scalar['maximum_reported_root_relative_residual'],
            mp60_minA=low_scalar['minA'], mp90_minA=high_scalar['minA'],
            mp60_minD=low_scalar['minD'], mp90_minD=high_scalar['minD'])
    resources = {}
    for name, resource, log in (('mp60', a.resource60, a.log60), ('mp90', a.resource90, a.log90)):
        data = load(resource)
        if data['status'] != 'observed_terminal' or data['child_returncode'] != 0:
            raise ValueError('Actual complete terminal required: '+name)
        resources[name] = dict(identity=identity(resource), log=identity(log), metadata=scalar_tree(data),
                               actual_command=data['command'])
    out = dict(
        confidence='Finite numerical evidence, not a rigorous error bound.',
        scope='Completed independent 60/90 digit readouts of three frozen original binary64 coefficient stage maps with the original RK16 and original root stopping/halving/domain rules. No complete tail or new nonlinear solution.',
        collector=identity(__file__), collector_helper_sha256=sha(Path(__file__).with_name('record_fixed_actual.py')),
        comparison_decimal_digits=140,
        evaluator_sha256=s60['source_sha256'], bridge_sha256=s60['bridge_sha256'],
        float_baseline=identity(a.float_baseline), capsule_summary=identity(s60['capsule_summary_path']),
        mp60_summary=identity(a.mp60), mp90_summary=identity(a.mp90),
        mp60_raw=s60['raw'], mp90_raw=s90['raw'],
        original_coefficients=capsule_summary['coefficients'], original_reference=capsule_summary['reference'],
        original_failed_state=capsule_summary['input'],
        source_sha256=capsule_summary['source_sha256'], additional_original_root_sources=capsule_summary['additional_original_root_sources'],
        coefficient_convention=s60['coefficient_convention'],
        all_three_42_outputs_round_to_same_binary64=all_same_rounded,
        all_three_root_decision_sequences_equal_60_90=all_same_decisions,
        mp60_to_mp90_maximum_all42_difference=text(max_all42_cross),
        named_results=results, resources=resources,
        scope_limits='Stability across precision levels is evidence only for this fixed-coefficient finite algorithm, including its unchanged root stopping rule. It is not a continuous-profile/ODE error bound, a full-stage Jacobian, a full-tail replay, or a solver acceptance. Static coefficient and Fourier truncation errors were not removed.',
        production_source_changed=False, complete_tail_solver_invoked=False, physical_checkpoint_written=False,
        data_policy='Only scalar comparisons and source/input/output identities are committed; full states, coefficient tables, and root traces remain scratch-only.')
    output = json.dumps(out, ensure_ascii=False, indent=2)+'\n'
    if len(output.encode()) >= 100000:
        raise ValueError('Compact record exceeds100KB')
    a.out.write_text(output)
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out), maximum_all42_cross=out['mp60_to_mp90_maximum_all42_difference'])))


if __name__ == '__main__':
    main()
