"""Resume the original R259 column-scaled LM candidate from a real parent.

Only parent provenance and the diagnostic output schema are generalized. The
frozen 1691 direction engine and original 3b9 CircleReference equations,
jacobian, domain, unweighted merit, Armijo loop, FD, Arb scalar expression and
complete zero-core circle check remain unchanged. No BVP or native solution is
claimed. A parent is a completed candidate diagnostic, never a solved field.

Every scientific operation is restricted to the public repository's Actions.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
ORIGINAL_NAME = 'geometry_20261114_small_core_resonance.py'
ORIGINAL_SHA256 = '3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5'
ENGINE_NAME = 'geometry_20261115_small_core_damped_search.py'
ENGINE_SHA256 = '1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728'
ENGINE_SCHEMA = 'R259-original-three-equation-column-scaled-LM-candidate-v1'
ENTRY_NAME = 'geometry_20261115_small_core_damped_resume.py'
SCHEMA = 'R259-original-three-equation-column-scaled-LM-resume-v1'
MODEL_SOURCE_NAMES = (
    ORIGINAL_NAME, 'geometry_20261114_constrained_trust_warm.py',
    'geometry_20261114_constrained_collocation.py', 'geometry_20261114_full_dn_augmented.py',
    'geometry_20261114_full_dn_boundary.py', 'geometry_20261114_physical_test_boundary.py',
    'geometry_20261114_lifted_modes_profile.py', 'geometry_20261114_full_prefix_operator.py',
    'geometry_20261114_direct_operator_cell.py')


def file_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def direction_engine_module():
    path = HERE/ENGINE_NAME
    if file_sha(path) != ENGINE_SHA256:
        raise ValueError('Retain the exact actual80 positive-damped direction engine')
    spec = importlib.util.spec_from_file_location('actual_R259_frozen_damped_engine_for_resume', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def checked_parent(path, expected_sha256, current_source_sha256):
    """Read provenance and literal parameters only; never reuse a numerical state.

    The CLI digest is the hash of the supplied file bytes, including gzip when
    present. The complete original bytes are copied unchanged to this run.
    Completed outputs of the immutable actual80 engine and of this exact resume
    producer are supported. All shared mathematical source hashes and the four
    input hashes are checked separately before creating the output directory.
    """
    if (len(expected_sha256) != 64
            or any(c not in '0123456789abcdef' for c in expected_sha256)):
        raise ValueError('Declare the real parent file SHA256, not a prospective value')
    raw = Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise ValueError('The supplied real parent status does not match its declared SHA256')
    compressed = raw.startswith(b'\x1f\x8b')
    decoded = gzip.decompress(raw) if compressed else raw
    parent = json.loads(decoded)
    if not isinstance(parent, dict):
        raise ValueError('The complete parent status must be a JSON object')
    if (parent.get('phase') != 'diagnostic-completed' or parent.get('diagnostic_completed') is not True
            or parent.get('native_nonlinear_solver_called') is not False
            or parent.get('success') is not False
            or parent.get('full_nonlinear_nonzero_lambda_solution_computed') is not False
            or parent.get('original_diagnostic_source_sha256') != ORIGINAL_SHA256):
        raise ValueError('Resume only a complete original-equation candidate diagnostic, never a native solution')
    consumed = parent.get('consumed_source_sha256')
    if not isinstance(consumed, dict):
        raise ValueError('The complete parent mathematical source identities are required')
    if parent.get('schema') == ENGINE_SCHEMA:
        producer_name, producer_sha256 = ENGINE_NAME, ENGINE_SHA256
        required_names = {ENGINE_NAME, *MODEL_SOURCE_NAMES}
    elif parent.get('schema') == SCHEMA:
        producer_name, producer_sha256 = ENTRY_NAME, current_source_sha256
        required_names = {ENTRY_NAME, ENGINE_NAME, *MODEL_SOURCE_NAMES}
        if (parent.get('source_sha256') != current_source_sha256
                or parent.get('direction_engine_source_sha256') != ENGINE_SHA256):
            raise ValueError('A resume parent must identify this exact producer and the frozen direction engine')
    else:
        raise ValueError('Unsupported parent diagnostic schema; no old output may be relabelled')
    if set(consumed) != required_names or consumed.get(producer_name) != producer_sha256:
        raise ValueError('The parent producer and complete common source set are not the declared originals')
    for name, digest in consumed.items():
        if file_sha(HERE/name) != digest:
            raise ValueError('Retain the actual parent mathematical source: '+name)
    parameters = parent.get('final', {}).get('parameters')
    if (not isinstance(parameters, list) or len(parameters) != 3
            or any(isinstance(v, bool) or not isinstance(v, (int, float))
                   or not math.isfinite(v) for v in parameters)):
        raise ValueError('Use all three finite literal final parameters of the real parent')
    receipt = dict(file='parent-damped-status.json'+('.gz' if compressed else ''),
        bytes=len(raw), sha256=expected_sha256, encoding='gzip-json' if compressed else 'json',
        decoded_bytes=len(decoded), decoded_sha256=hashlib.sha256(decoded).hexdigest(),
        schema=parent['schema'], producer_name=producer_name, producer_sha256=producer_sha256,
        parameters_field='final.parameters', literal_parameters=parameters,
        parent_damping_cli_text=parent.get('damping_cli_text'),
        parent_damping_binary64=parent.get('damping_binary64'),
        parent_is_not_a_nonzero_or_native_solution=True,
        only_literal_parameters_reused=True, parent_J_or_merit_or_state_reused=False)
    return raw, parent, receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('accepted', 'prepared', 'tail-anchor', 'tail-config', 'parent-status', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--parent-status-sha256', type=str, required=True,
                        help='Actual hash of the complete supplied parent status bytes, compressed if gzip')
    parser.add_argument('--damping', type=str, required=True,
                        help='Explicit positive coefficient of the three augmented penalty rows')
    parser.add_argument('--candidate-steps', dest='newton_steps', type=int, default=8,
                        help='Compatibility bound only; each direction is LM, not an undamped Newton solve')
    parser.add_argument('--backtracks', type=int, default=20)
    parser.add_argument('--candidate-resonance-tolerance', type=float, default=1e-8)
    parser.add_argument('--interval-bits', type=int, default=160)
    parser.add_argument('--interval-depth', type=int, default=14)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError("All numerical work belongs to the public repository's own Actions")
    damping = float(args.damping)
    if not math.isfinite(damping) or damping <= 0:
        raise ValueError('Declare one finite strictly positive damping coefficient')
    if not 0 <= args.newton_steps <= 12 or not 1 <= args.backtracks <= 20:
        raise ValueError('Keep the original optional candidate search explicitly bounded')
    if args.candidate_resonance_tolerance != 1e-8 or args.interval_bits != 160 or args.interval_depth != 14:
        raise ValueError('This candidate retains the original threshold and original Arb budget')
    if Path(__file__).name != ENTRY_NAME:
        raise ValueError('Retain the independent resume source basename for provenance')
    current_source_sha256 = file_sha(__file__)
    parent_raw, parent, parent_receipt = checked_parent(
        args.parent_status, args.parent_status_sha256, current_source_sha256)
    engine = direction_engine_module()
    base = engine.original_module()
    damped_direction = engine.damped_direction
    np, original, EXPECTED, setup, write = base.np, base.original, base.EXPECTED, base.setup, base.write
    if parent['input_sha256'] != EXPECTED:
        raise ValueError('The real parent and current original four mathematical inputs must agree')
    for name, digest in EXPECTED.items():
        if original.sha(getattr(args, name)) != digest:
            raise ValueError('Retain the complete original actual input: '+name)
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError('Use a fresh independent damped-candidate output directory')
    # Retain exact parent bytes. They identify parameters, not a solved field.
    (args.out/parent_receipt['file']).write_bytes(parent_raw)
    source, accepted, anchor = [original.read(path) for path in (args.prepared, args.accepted, args.tail_anchor)]
    profile, flow, boundary = setup(accepted, source, anchor, 4096, 1)
    J = np.asarray(anchor['heightJetJacobian']).reshape(3*flow.M+2, flow.M)[:flow.M]
    target = np.asarray(accepted['core']['coefficients'])[:3]
    model = base.CircleReference(profile, source['mesh'], J, target, boundary.eh, boundary.cut_scale)
    names = (ENTRY_NAME, ENGINE_NAME, *MODEL_SOURCE_NAMES)
    status = dict(schema=SCHEMA, scope=__doc__, phase='starting',
        source_sha256=current_source_sha256, direction_engine_source_sha256=ENGINE_SHA256,
        input_sha256=EXPECTED, consumed_source_sha256={name: original.sha(HERE/name) for name in names},
        original_diagnostic_source_sha256=ORIGINAL_SHA256,
        parent_status=parent_receipt,
        parent_parameters_are_initial_guess_not_completed_field=True,
        initial_model_evaluation_and_description_are_fresh=True,
        parent_model_values_are_not_relabelled_as_current_values=True,
        candidate_algorithm='one column-scaled positive-damped 6x3 least-squares direction per iteration',
        damping_cli_text=args.damping, damping_binary64=damping,
        direction_model='min_z 0.5||J D^-1 z+r||_2^2+0.5 eta^2||z||_2^2; d=D^-1 z',
        candidate_iteration_budget=args.newton_steps, original_backtrack_budget=args.backtracks,
        original_armijo_coefficient=.2, candidate_resonance_tolerance=args.candidate_resonance_tolerance,
        scalar_interval_bits=args.interval_bits, scalar_interval_maximum_depth=args.interval_depth,
        original_equation_and_jacobian_functions_reused=True,
        unweighted_original_merit_and_domain_functions_reused=True,
        same_complete_original_scalar_formula_and_three_supports=True,
        design_parameters_are_varied_not_claimed_one_fixed_metric_during_search=True,
        original_mesh_nodes=len(model.x), field_and_tail_modes=flow.M,
        low_modes_diagnosed=[1, 2, 3], complete_zero_slope_J_retained=True,
        native_nonlinear_solver_called=False, original_Gauss_app_used_as_a_derivative=False,
        original_full_BVP_or_large_amplitude_acceptance_claimed=False,
        straight_homotopy_only=True, weighted_lambda_j_homotopies_not_excluded=True,
        searches=[], success=False)
    start = time.monotonic()
    try:
        parameters = np.asarray(parent['final']['parameters'])
        state = model.evaluate(parameters)
        status['initial'] = model.description(state)
        write(args.out/'damped-resume-status.json', status)
        if args.newton_steps and (not model.exactly_diagonal or np.any(target == 0)):
            raise ValueError('This optional diagonal three-equation search cannot replace high-core Schur or a zero-target expansion')
        for iteration in range(args.newton_steps):
            residual = state['equation']
            if np.max(abs(residual)) <= args.candidate_resonance_tolerance:
                break
            derivative = model.jacobian(parameters)
            direction, direction_report = damped_direction(np, derivative, residual, damping)
            before = .5*float(residual@residual)
            slope = float(residual@(derivative@direction))
            row = dict(iteration=iteration, parameters=parameters.tolist(),
                residual=residual.tolist(), derivative=derivative.tolist(),
                direction_model=direction_report,
                true_model_merit_slope=slope, trials=[], accepted=False)
            status['searches'].append(row)
            if not np.isfinite(slope) or slope >= 0:
                row['reason'] = 'No finite strict descent of the actual low-mode equations'
                break
            for trial in range(args.backtracks):
                alpha = 2.**(-trial)
                item = dict(alpha=alpha, accepted=False)
                row['trials'].append(item)
                try:
                    candidate = model.evaluate(parameters+alpha*direction)
                    value = candidate['equation']
                    merit = .5*float(value@value)
                    item.update(actual_merit=merit, merit_before=before)
                    if merit <= before+.2*alpha*slope:
                        parameters = parameters+alpha*direction
                        state = candidate
                        item['accepted'] = row['accepted'] = True
                        break
                except (FloatingPointError, np.linalg.LinAlgError) as error:
                    item['domain_or_cell_error'] = repr(error)
            write(args.out/'damped-resume-status.json', status)
            if not row['accepted']:
                break
        status['final'] = model.description(state)
        specification = base.scalar_spec(profile, source['complete_scalar_profile']['complete_original_port'],
            parameters, EXPECTED['accepted'])
        status['complete_scalar_domain'] = base.scalar_domain(profile, specification, args.out,
            args.interval_bits, args.interval_depth)
        status['original_complete_circle_check'] = base.complete_reference_check(model, state, profile, flow,
            boundary, args.out, source, EXPECTED['prepared'])
        small = bool(np.max(abs(state['full_right'])) <= args.candidate_resonance_tolerance)
        status.update(phase='diagnostic-completed', diagnostic_completed=True,
            low_mode_candidate_has_small_full_recorded_right_residual=small,
            this_candidate_threshold_is_not_an_original_BVP_acceptance_gate=True,
            full_nonlinear_nonzero_lambda_solution_computed=False,
            high_mode_nonresonance_or_interval_transversality_proved=False,
            original_circle_reference_schema_retained=True)
        return 0
    except Exception as error:
        status.update(phase='exception', exception=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        status['seconds'] = time.monotonic()-start
        write(args.out/'damped-resume-status.json', status)


if __name__ == '__main__':
    raise SystemExit(main())
