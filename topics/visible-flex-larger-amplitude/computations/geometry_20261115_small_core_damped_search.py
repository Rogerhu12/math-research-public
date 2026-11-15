"""Bounded LM candidate search on the unchanged original R259 three equations.

Only the three-parameter search direction is new. The original CircleReference
evaluate/jacobian/description, unweighted merit, scalar-domain exceptions,
Armijo factor .2, full-right candidate threshold, final Arb expression and full
zero-core circle check are retained. This is not a BVP or native acceptance.

Every scientific operation is restricted to the public repository's Actions.
"""
from __future__ import annotations

import argparse
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
PARENT78_SHA256 = '09031496410951afc018b223b921db111a43b3e0852592b87aafd5351b4f0c40'
PARENT78_BYTES = 50438
SCHEMA = 'R259-original-three-equation-column-scaled-LM-candidate-v1'


def file_sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def original_module():
    path = HERE/ORIGINAL_NAME
    if file_sha(path) != ORIGINAL_SHA256:
        raise ValueError('Retain the exact original R259 scientific source')
    spec = importlib.util.spec_from_file_location('actual_R259_original_for_damped_candidate', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def damped_direction(np, derivative, residual, damping):
    """One 6x3 augmented least-squares solve, without normal equations.

    For D_j=||J[:,j]||_2 (D_j=1 if the column is exactly zero), put A=J/D.
    The ideal model is min_z .5||Az+r||^2+.5*damping^2||z||^2, d=z/D.
    All finite arrays and the recovered unscaled Jd are saved. The caller still
    checks the actual original r@(J@d) and performs original nonlinear trials.
    """
    if derivative.shape != (3, 3) or residual.shape != (3,):
        raise ValueError('Retain all and only the original three parameter equations')
    if not np.all(np.isfinite(derivative)) or not np.all(np.isfinite(residual)):
        raise FloatingPointError('The actual original small system is nonfinite')
    column_norms = np.hypot.reduce(np.abs(derivative), axis=0)
    zero_columns = column_norms == 0
    scale = np.where(zero_columns, 1., column_norms)
    scaled = derivative/scale[None, :]
    augmented = np.vstack((scaled, damping*np.eye(3)))
    rhs = np.r_[-residual, np.zeros(3)]
    if not np.all(np.isfinite(augmented)) or not np.all(np.isfinite(scale)):
        raise FloatingPointError('The explicitly formed damped direction model is nonfinite')
    z, lstsq_residuals, rank, singular_values = np.linalg.lstsq(augmented, rhs, rcond=None)
    direction = z/scale
    if not np.all(np.isfinite(z)) or not np.all(np.isfinite(direction)):
        raise FloatingPointError('The actual recovered damped candidate direction is nonfinite')
    diagnostic = dict(
        schema='original-three-equation-column-scaled-LM-direction-v1',
        unscaled_equation=residual.tolist(), unscaled_jacobian=derivative.tolist(),
        column_norms=column_norms.tolist(), coordinate_scale=scale.tolist(),
        exactly_zero_columns=np.flatnonzero(zero_columns).tolist(),
        zero_column_scale_policy='Use one for an exactly zero column; keep all three columns',
        positive_damping=float(damping), scaled_jacobian=scaled.tolist(),
        augmented_matrix=augmented.tolist(), augmented_rhs=rhs.tolist(),
        augmented_lstsq_rank=int(rank), augmented_lstsq_singular_values=singular_values.tolist(),
        augmented_lstsq_returned_residuals=lstsq_residuals.tolist(), lstsq_rcond_argument=None,
        scaled_direction=z.tolist(), recovered_original_parameter_direction=direction.tolist(),
        original_jacobian_times_recovered_direction=(derivative@direction).tolist(),
        normal_equations_formed=False, row_equations_reweighted=False,
        damping_added_to_original_nonlinear_residual=False,
        finite_lstsq_is_not_a_convergence_or_existence_proof=True,
        model_diagnostics_are_not_extra_acceptance_gates=True)
    return direction, diagnostic


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('accepted', 'prepared', 'tail-anchor', 'tail-config', 'parent-status', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
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
        raise ValueError('This candidate retains the actual78 threshold and original Arb budget')
    parent_raw = args.parent_status.read_bytes()
    if len(parent_raw) != PARENT78_BYTES or hashlib.sha256(parent_raw).hexdigest() != PARENT78_SHA256:
        raise ValueError('Start only from the complete genuine actual78 original status')
    parent = json.loads(parent_raw)
    if (parent.get('phase') != 'diagnostic-completed' or parent.get('diagnostic_completed') is not True
            or parent.get('consumed_source_sha256', {}).get(ORIGINAL_NAME) != ORIGINAL_SHA256
            or parent.get('native_nonlinear_solver_called') is not False):
        raise ValueError('Actual78 is a completed diagnostic, never a native or nonzero parent')
    base = original_module()
    np, original, EXPECTED, setup, write = base.np, base.original, base.EXPECTED, base.setup, base.write
    if parent['input_sha256'] != EXPECTED:
        raise ValueError('The actual78 and current original four mathematical inputs must agree')
    for name, digest in EXPECTED.items():
        if original.sha(getattr(args, name)) != digest:
            raise ValueError('Retain the complete original actual input: '+name)
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError('Use a fresh independent damped-candidate output directory')
    # Retain exact parent bytes. They identify parameters, not a solved field.
    (args.out/'actual78-parent-status.json').write_bytes(parent_raw)
    source, accepted, anchor = [original.read(path) for path in (args.prepared, args.accepted, args.tail_anchor)]
    profile, flow, boundary = setup(accepted, source, anchor, 4096, 1)
    J = np.asarray(anchor['heightJetJacobian']).reshape(3*flow.M+2, flow.M)[:flow.M]
    target = np.asarray(accepted['core']['coefficients'])[:3]
    model = base.CircleReference(profile, source['mesh'], J, target, boundary.eh, boundary.cut_scale)
    names = (Path(__file__).name, ORIGINAL_NAME, 'geometry_20261114_constrained_trust_warm.py',
        'geometry_20261114_constrained_collocation.py', 'geometry_20261114_full_dn_augmented.py',
        'geometry_20261114_full_dn_boundary.py', 'geometry_20261114_physical_test_boundary.py',
        'geometry_20261114_lifted_modes_profile.py', 'geometry_20261114_full_prefix_operator.py',
        'geometry_20261114_direct_operator_cell.py')
    status = dict(schema=SCHEMA, scope=__doc__, phase='starting',
        input_sha256=EXPECTED, consumed_source_sha256={name: original.sha(HERE/name) for name in names},
        original_diagnostic_source_sha256=ORIGINAL_SHA256,
        parent_actual78=dict(file='actual78-parent-status.json', bytes=len(parent_raw), sha256=PARENT78_SHA256,
            parameters_field='final.parameters', parent_is_not_a_nonzero_or_native_solution=True),
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
        write(args.out/'damped-search-status.json', status)
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
            write(args.out/'damped-search-status.json', status)
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
        write(args.out/'damped-search-status.json', status)


if __name__ == '__main__':
    raise SystemExit(main())
