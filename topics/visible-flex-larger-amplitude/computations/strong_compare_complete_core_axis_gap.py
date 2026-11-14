#!/usr/bin/env python3
"""Compare the same complete-core axis formula in two actual endpoints.

AI-assisted research, strong_recovery, 2026-11-13.
The core coefficients are read from original, genuinely accepted M32 files.
For h(phi)=1+sum_j c_j cos(2*j*phi), the exact saved-coefficient axis
difference is h(0)-h(pi/2)=2*sum_{j odd} c_j. Exact rational arithmetic
here concerns only these stored binary coefficients, not a continuum BVP.
The previously saved finite-set witness is separately identified as the
unsolved A warm field. It is neither the earlier q122 actual core value nor
the whole closed-surface Hausdorff amplitude or rigidly registered delta_E.
"""
from __future__ import annotations
import argparse
import datetime
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def rational(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator), display=float(value))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('previous', 'previous-owned', 'actual', 'actual-owned',
                 'warm-core', 'warm-distance', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    inputs, checks = {}, {}

    def check(name, condition):
        if not condition:
            raise ValueError('Complete saved-core comparison failed: '+name)
        checks[name] = True

    def load(path):
        inputs[str(path)] = sha(path)
        return read(path)

    def core(label, values):
        check(label+'_all_32_finite_coefficients', len(values) == 32 and all(math.isfinite(v) for v in values))
        coefficients = [Fraction.from_float(float(value)) for value in values]
        h0 = Fraction(1)+sum(coefficients)
        h90 = Fraction(1)+sum(((-1)**(j+1))*value for j,value in enumerate(coefficients))
        gap = h0-h90
        check(label+'_same_full_core_formula', gap == 2*sum(coefficients[::2]))
        return dict(coefficients=values, frequencies=list(range(2,65,2)),
            q_coordinate=values[0], exact_saved_binary_h0=rational(h0),
            exact_saved_binary_h_pi_over_2=rational(h90),
            exact_saved_binary_axis_gap=rational(gap)), gap

    def accepted(label, primary_path, owned_path):
        primary, resource = load(primary_path), load(owned_path)
        check(label+'_original_owned_exit_zero', resource.get('exitcode') == 0 and resource.get('wait4_observed') is True)
        check(label+'_genuine_finite_actual_accepted', primary.get('solver_success') is True
            and primary.get('audit_pending') is False and primary['config'].get('actual_nonlinear_tail') is True
            and primary['max_rms_collocation_residual'] <= primary['config']['tol']
            and primary['summary']['physical_bc_max'] <= primary['actual_tail']['actual_physical_bc_tolerance'])
        check(label+'_exact_original_resource_path', primary_path.name.removesuffix('.json.gz')+'-resource.json' == owned_path.name)
        check(label+'_physical_32_mode_layout', primary['modes'] == 32
            and primary['core']['frequencies'] == list(range(2,65,2)))
        result, gap = core(label, primary['core']['coefficients'])
        stored = float(primary['core']['phase_pi_over_base_mode_support_gap_at_phi0'])
        check(label+'_archived_same_axis_summary_agrees', abs(stored-float(gap)) <= 32*math.ulp(stored))
        result.update(primary_file=str(primary_path),primary_sha256=sha(primary_path),
            original_owned_file=str(owned_path),original_owned_sha256=sha(owned_path),
            original_archived_axis_gap=stored, archived_summary_minus_exact_binary_formula=stored-float(gap),
            physical_profile=primary['frozen_profile'],nodes=primary['nodes'],
            original_accepted_finite_BVP=True, refinement_comparison=False)
        return primary, result, gap

    previous, prior, gp = accepted('previous_q122', args.previous, args.previous_owned)
    actual, current, ga = accepted('actual_A_q126', args.actual, args.actual_owned)
    prepared, distance = load(args.warm_core), load(args.warm_distance)
    warm, gw = core('unsolved_A_warm', prepared['actual_complete_core'])
    check('warm_constructed_from_previous_actual_reference', prepared['actual_reference_sha256'] == sha(args.previous))
    check('A_warm_and_A_actual_same_prescribed_low3', prepared['actual_complete_core'][:3] == actual['core']['coefficients'][:3])
    stored_gap = distance['complete_stored_core_axis_support_gap']
    check('finite_witness_report_uses_exact_same_A_warm_core',
          Fraction(int(stored_gap['numerator']),int(stored_gap['denominator'])) == gw)
    check('finite_witness_explicitly_unsolved_warm',
          distance['set_and_family_scope']['P'] == 'Exactly the saved unsolved fine warm Cartesian prefix samples.')
    finite = distance['distance_diagnostics']['quarter_rotated_prefix']
    low, high = [Fraction(int(finite[key]['numerator']),int(finite[key]['denominator']))
                 for key in ('finite_set_min_distance_lower','finite_set_min_distance_upper')]
    check('finite_witness_bounds_ordered', low <= high)
    profile_changes = {key:dict(previous=previous['frozen_profile'].get(key),actual=actual['frozen_profile'].get(key))
        for key in sorted(set(previous['frozen_profile'])|set(actual['frozen_profile']))
        if previous['frozen_profile'].get(key) != actual['frozen_profile'].get(key)}
    check('these_are_different_physical_designs_not_same_g_refinement', bool(profile_changes))
    q_difference = Fraction.from_float(actual['core']['coefficients'][0])-Fraction.from_float(previous['core']['coefficients'][0])
    result = dict(schema='same-complete-core-axis-gap-actual-comparison-v1',scope=__doc__,
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_sha256=sha(__file__),
        input_sha256=inputs,checks=checks,all_checks=True,
        formula='h(0)-h(pi/2) = sum_m (1-(-1)^(m/2))*c_m = 2*sum_{m=2 mod 4} c_m, using all 32 modes',
        previous_actual=prior,current_actual=current,unsolved_current_warm=warm,
        actual_minus_previous_axis_gap=rational(ga-gp),
        relative_actual_axis_gap_increase=float((ga-gp)/gp),
        actual_q_coordinate_increase=rational(q_difference),
        difference_from_twice_q_coordinate_increase=rational((ga-gp)-2*q_difference),
        actual_minus_current_warm_axis_gap=rational(ga-gw),
        previous_finite_witness=dict(original_report=str(args.warm_distance),
            sha256=sha(args.warm_distance),belongs_to='unsolved A q126 warm, not q122 actual',
            saved_P_and_quarter_turn_distance_bounds=[rational(low),rational(high)],
            finite_point_distance_minus_warm_core_axis_gap_bounds=[rational(low-gw),rational(high-gw)],
            complete_closed_surface_distance_not_measured=True),
        changed_physical_profile_keys=profile_changes,
        use_for_design=dict(full_core_linear_objective_weights=[2 if m%4==2 else 0 for m in range(2,65,2)],
            direction_derivative='Apply these weights to every full core_derivative vector at the actual new baseline.',
            divide_by_actual_geometric_size_only_after_separate_geometry=True,
            q_coordinate_alone_is_not_an_amplitude_measure=True,
            full_closed_Hausdorff_delta_hold_or_delta_E_certified=False),
        ODE_Node_Newton_or_new_geometry_calls=0)
    with args.out.open('x') as stream:
        json.dump(result,stream,indent=2,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(out=str(args.out),sha256=sha(args.out),checks=len(checks),
        previous_axis_gap=float(gp),actual_axis_gap=float(ga),warm_axis_gap=float(gw),
        actual_increase=float(ga-gp),actual_minus_warm=float(ga-gw))),flush=True)


if __name__ == '__main__':
    main()
