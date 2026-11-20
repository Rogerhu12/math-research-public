#!/usr/bin/env python3
"""Optional fixed-SPD PCG for the unchanged complete inequality QP.

Minimize .5*||A z+r||^2+.5*mu^2*||z||^2 subject to the original C z<=b.
No field representation, target, regularizer, row or nonlinear acceptance is
changed. None delegates literally to the byte-bound published v3 solver.
With fixed B, the active-face map is P B P; the original Euclidean ||P g||
stopping and R668 unit-release tests remain. A release keeps its Euclidean
inward starter; a new PCG chain follows its first positive feasible step.

Source preparation only. This module supplies no full driver, preconditioner
builder, fixture or automatic beta. Numerical entry is public Actions only.
"""
from dataclasses import dataclass
import hashlib
import importlib.util
import os
from pathlib import Path
import sys
import time

import numpy as np
from scipy.linalg.blas import dnrm2


BASE_V3_SHA256 = 'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4'
_BASE_MODULES = {}


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Run the scientific QP only in the public repository Actions')


def _load_base(path=None):
    path = (Path(path) if path is not None else
            Path(__file__).with_name('fullspace_feasible_active_cg_v3.py')).resolve()
    if not path.is_file() or path.stat().st_size > 100000:
        raise ValueError('Need the small published frozen v3 source')
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != BASE_V3_SHA256:
        raise ValueError('The required original v3 implementation changed')
    key = str(path)
    if key not in _BASE_MODULES:
        name = '_full_Phi_v4_frozen_v3_'+digest[:16]
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        _BASE_MODULES[key] = module
    return _BASE_MODULES[key], dict(path=key, bytes=len(raw), sha256=digest)


@dataclass
class Parameters:
    maxiter: int = 256
    atol: float = 1e-12
    rtol: float = 1e-6
    feasibility_tolerance: float = 2e-11
    early_release_every: int = 8
    early_release_relative_gain: float = .1
    rank_tolerance: float = 2e-12
    gradient_refresh: int = 32
    progress_every: int = 16
    gradient_replacement_restart_relative: float = .1
    minimum_direction_descent_fraction: float = .01



def _solve_pcg(base, operator, residual, row_matrix, bounds, *, damping,
               apply_preconditioner, preconditioner_metadata, base_record,
               parameters=None, block_columns=32768, callback=None):
    """Return (z, diagnostics); no nonlinear state is modified here."""
    p = parameters or Parameters()
    if (p.early_release_every < 1 or p.early_release_relative_gain < 0
            or p.gradient_refresh < 1 or p.progress_every < 1
            or not 0 < p.gradient_replacement_restart_relative < 1
            or not 0 < p.minimum_direction_descent_fraction < 1):
        raise ValueError('Need positive intervals and declared relative replacement/descent safeguards')
    bounds = np.asarray(bounds, dtype=float)
    rows = base.StreamedRows(row_matrix, block_columns)
    m, n = rows.shape
    if operator.shape[1] != n or bounds.shape != (m,):
        raise ValueError('QP operator, row matrix and bounds have different spaces')
    if not np.isfinite(bounds).all() or np.min(bounds, initial=0.0) < -p.feasibility_tolerance:
        raise ValueError('Zero is not a feasible QP start; an explicit restoration is required')
    if not np.isfinite(damping) or damping <= 0:
        raise ValueError('A positive damping makes this quadratic strictly convex')
    mu2 = float(damping)**2
    if not np.isfinite(mu2) or mu2 <= 0:
        raise ValueError('The declared original damping squared must be finite and positive')
    started = time.monotonic()
    z = np.zeros(n)
    data_residual = np.array(residual, dtype=float, copy=True)
    gradient = np.asarray(operator.rmatvec(data_residual))
    initial_gradient_norm = float(np.linalg.norm(gradient))
    gradient_tolerance = p.atol + p.rtol*initial_gradient_norm
    face = base.ActiveFace(rows, p.rank_tolerance)
    cz = np.zeros(m)
    direction = None
    direction_kind = None
    preconditioned_gradient = None
    preconditioned_energy = None
    euclidean_starter_pending = False
    history = []
    transitions = []
    restarts = []
    replacements = []
    same_face_advances = 0
    longest_same_face_advances = 0
    advances = 0
    operator_products = dict(matvec=0, rmatvec=1)
    status = 'iteration_limit'
    initial_data_objective = float(data_residual @ data_residual)/2
    objective = initial_data_objective
    maximum_face_rank = 0
    preconditioner_state = dict(applications=0, seconds=0., failures=[],
        euclidean_release_starters_completed=0, last_success=None)

    def projected_preconditioner(pg, phase):
        # The caller declares one FIXED real linear SPD map for this QP.
        # Both projections use the original Euclidean active-face projector.
        before = time.monotonic()
        preconditioner_state['applications'] += 1
        try:
            raw_value = np.asarray(apply_preconditioner(np.array(pg, copy=True)))
            if (raw_value.shape != (n,) or np.iscomplexobj(raw_value)
                    or not np.all(np.isfinite(raw_value))):
                raise ArithmeticError('The fixed SPD apply returned a nonfinite or non-real vector of the wrong shape')
            value = face.project(np.asarray(raw_value, dtype=float))
            energy = float(pg @ value)
            if not np.isfinite(energy) or energy <= 0:
                raise ArithmeticError('Nonpositive or nonfinite computed Pg dot PBPg')
            value_norm = float(dnrm2(value))
            if not np.isfinite(value_norm) or value_norm <= 0:
                raise ArithmeticError('The preconditioned Euclidean norm is not finite and positive in the declared float arithmetic')
            preconditioner_state['last_success'] = dict(advance=advances,
                phase=phase, projected_metric_energy=energy,
                projected_preconditioned_gradient_norm=value_norm)
            return value, energy
        except Exception as error:
            # Explicit truncated failure: never change B to identity while
            # preserving a PCG chain constructed with another metric.
            preconditioner_state['failures'].append(dict(advance=advances,
                phase=phase, exception_type=type(error).__name__,
                message=str(error)[:2000], fallback_to_identity_performed=False))
            return None, None
        finally:
            preconditioner_state['seconds'] += time.monotonic()-before

    def emit(kind, **values):
        if callback is not None:
            callback(dict(event=kind, advances=advances,
                          seconds=time.monotonic()-started, **values))

    # More zero-length transitions than this indicate numerical cycling;
    # stopping retains a true feasible truncated direction, never a fake KKT.
    max_transitions = max(32, 8*p.maxiter+4*m)
    while advances < p.maxiter:
        if len(transitions) > max_transitions:
            status = 'active_set_transition_limit'
            break
        projected_gradient = face.project(gradient)
        pg2 = float(projected_gradient @ projected_gradient)
        pg_norm = np.sqrt(pg2)
        check_release = (bool(face.indices) and
            (advances % p.early_release_every == 0 or direction is None
             or pg_norm <= gradient_tolerance))
        release_values = []
        if check_release:
            release_values, multipliers, inverse = face.release_candidates(gradient)
            gain_threshold = max(gradient_tolerance, p.early_release_relative_gain*pg_norm)
            if release_values and release_values[0]['normalized_descent_gain'] > gain_threshold:
                chosen = release_values[0]
                position = chosen['position']
                coefficients = inverse[:, position]
                unit_direction = -(face.Q[:len(face.indices)].T @
                                   (coefficients/np.linalg.norm(coefficients)))
                literal_row = rows.row(chosen['row'])
                actual_unit_slope = float(gradient @ unit_direction)
                actual_unit_inward = float(literal_row @ unit_direction)
                unit_norm = float(np.linalg.norm(unit_direction))
                if (not np.isfinite(actual_unit_slope) or actual_unit_slope >= 0
                        or actual_unit_inward >= 0):
                    transitions.append(dict(kind='early_release_direction_sign_failure',
                        advances=advances, **chosen,
                        actual_unit_slope=actual_unit_slope,
                        actual_unit_inward=actual_unit_inward, unit_norm=unit_norm))
                    status = 'early_release_direction_numeric_sign_failure'
                    break
                removed = face.remove(position)
                restarts.append(dict(advance=advances, reason='active_row_released', row=removed))
                same_face_advances = 0
                direction = -face.project(gradient)
                direction_kind = 'euclidean_release_starter'
                euclidean_starter_pending = True
                preconditioned_gradient = preconditioned_energy = None
                new_slope = float(gradient @ direction)
                released_row_derivative = float(literal_row @ direction)
                record = dict(kind='release_negative_multiplier_early', advances=advances,
                    **chosen, gain_threshold=gain_threshold,
                    face_gradient_norm_before=pg_norm,
                    actual_unit_slope=actual_unit_slope,
                    actual_unit_inward=actual_unit_inward, unit_norm=unit_norm,
                    new_projected_direction_slope=new_slope,
                    released_row_new_direction_derivative=released_row_derivative,
                    active_rows_after=len(face.indices))
                transitions.append(record)
                emit('qp_release_early', **{key: value for key, value in record.items()
                                          if key not in ('kind', 'advances')})
                if new_slope >= 0 or released_row_derivative >= 0:
                    status = 'released_face_direction_numeric_sign_failure'
                    break
                del literal_row, unit_direction, inverse
                # All remaining inactive inequalities still pass the literal
                # maximum-feasible-step test; no extrapolated feasibility claim.
                # Use this released-face descent direction for that line test
                # immediately, before considering another early release at the
                # same advance count.
                projected_gradient = -direction
                pg2 = float(projected_gradient @ projected_gradient)
                pg_norm = np.sqrt(pg2)
        if pg_norm <= gradient_tolerance:
            if not face.indices or not release_values:
                status = 'numerical_kkt_tolerance'
            else:
                # Do not call this exact KKT: a nearly dependent negative raw
                # multiplier may remain although every individual normalized
                # feasible release direction is below the declared tolerance.
                status = 'face_and_unit_release_direction_tolerances'
            break
        if direction is None:
            if euclidean_starter_pending:
                direction = -projected_gradient
                direction_kind = 'euclidean_release_starter'
            else:
                if preconditioned_gradient is None:
                    preconditioned_gradient, preconditioned_energy = projected_preconditioner(
                        projected_gradient, 'new_PCG_chain')
                if preconditioned_gradient is None:
                    status = 'fixed_preconditioner_application_failed'
                    break
                direction = -preconditioned_gradient
                direction_kind = 'preconditioned_steepest'
        gd = float(gradient @ direction)
        if not np.isfinite(gd) or gd >= 0:
            if euclidean_starter_pending:
                status = 'released_face_direction_numeric_sign_failure'
                break
            if preconditioned_gradient is None:
                preconditioned_gradient, preconditioned_energy = projected_preconditioner(
                    projected_gradient, 'non_descent_restart')
            if preconditioned_gradient is None:
                status = 'fixed_preconditioner_application_failed'
                break
            direction = -preconditioned_gradient
            direction_kind = 'preconditioned_steepest'
            gd = float(gradient @ direction)
            restarts.append(dict(advance=advances, reason='non_descent_direction_before_advance'))
            if not np.isfinite(gd) or gd >= 0:
                status = 'preconditioned_direction_numeric_descent_failure'
                break
        # BLAS scaled sum-of-squares avoids overflow of intermediate d_i^2
        # when the actual finite Euclidean norm is still representable.
        direction_norm = float(dnrm2(direction))
        if not np.isfinite(direction_norm) or direction_norm <= 0:
            status = 'preconditioned_direction_nonfinite_or_zero_norm'
            break
        cd = rows.matvec(direction)
        inactive = np.ones(m, dtype=bool)
        inactive[face.indices] = False
        eligible = inactive & (cd > 0)
        slack = bounds-cz
        current_violation = float(np.max(-slack, initial=0.0))
        if current_violation > p.feasibility_tolerance:
            status = 'linear_feasibility_roundoff_failure'
            break
        blocker = None
        blocking_alpha = float('inf')
        if np.any(eligible):
            indices = np.flatnonzero(eligible)
            ratios = np.maximum(slack[eligible], 0.0)/cd[eligible]
            where = int(np.argmin(ratios))
            blocker = int(indices[where])
            blocking_alpha = float(ratios[where])
        # Under B -> t B, d scales by t and alpha by 1/t. The actual
        # ORIGINAL-coordinate displacement is the appropriate zero-step
        # scale. None still delegates to v3's unchanged literal alpha rule.
        # Compare by division; an overflowing alpha*norm must never become
        # a fictitious zero step. A genuinely unrepresentable norm already
        # returned the explicit numerical-failure status above.
        with np.errstate(over='ignore', under='ignore'):
            zero_alpha_limit = float(np.divide(1e-15, direction_norm))
        blocking_length = None
        blocking_length_overflow = False
        if np.isfinite(blocking_alpha):
            with np.errstate(over='ignore'):
                largest_safe_alpha = float(np.divide(np.finfo(float).max, direction_norm))
            if blocking_alpha <= largest_safe_alpha:
                blocking_length = blocking_alpha*direction_norm
                if not np.isfinite(blocking_length):
                    blocking_length = None
                    blocking_length_overflow = True
            else:
                blocking_length_overflow = True
        if np.isfinite(blocking_alpha) and blocking_alpha <= zero_alpha_limit:
            added = face.add(blocker)
            transitions.append(dict(kind='zero_length_blocker', advances=advances,
                                    **added))
            if not added.get('added'):
                status = 'dependent_blocker_at_zero_step'
                break
            maximum_face_rank = max(maximum_face_rank, len(face.indices))
            direction = None
            direction_kind = None
            preconditioned_gradient = preconditioned_energy = None
            # If a release has not yet achieved a positive feasible step,
            # retain its Euclidean starter policy through this face change.
            restarts.append(dict(advance=advances, reason='zero_length_active_row_added', row=blocker))
            same_face_advances = 0
            continue
        ad = np.asarray(operator.matvec(direction))
        operator_products['matvec'] += 1
        curvature = float(ad @ ad) + mu2*float(direction @ direction)
        if not np.isfinite(curvature) or curvature <= 0:
            status = 'nonpositive_computed_quadratic_curvature'
            break
        unconstrained_alpha = -gd/curvature
        alpha = min(unconstrained_alpha, blocking_alpha)
        if not np.isfinite(alpha) or alpha <= 0:
            status = 'nonpositive_step_length'
            break
        hd = np.asarray(operator.rmatvec(ad)) + mu2*direction
        operator_products['rmatvec'] += 1
        z += alpha*direction
        data_residual += alpha*ad
        gradient += alpha*hd
        cz += alpha*cd
        advances += 1
        same_face_advances += 1
        longest_same_face_advances = max(longest_same_face_advances, same_face_advances)
        blocked = blocking_alpha <= unconstrained_alpha*(1+1e-13)
        replacement = None
        if advances % p.gradient_refresh == 0:
            # Use the actual linear residual, not just A* applied to its
            # accumulated recurrence. No nonlinear field is evaluated here.
            actual_data_residual = np.asarray(operator.matvec(z)) + residual
            operator_products['matvec'] += 1
            residual_defect = float(np.linalg.norm(actual_data_residual-data_residual))
            actual_gradient = np.asarray(operator.rmatvec(actual_data_residual)) + mu2*z
            operator_products['rmatvec'] += 1
            projected_defect = float(np.linalg.norm(face.project(actual_gradient-gradient)))
            projected_actual_norm = float(np.linalg.norm(face.project(actual_gradient)))
            relative_defect = projected_defect/max(projected_actual_norm, gradient_tolerance,
                                                   np.finfo(float).tiny)
            replacement = dict(advance=advances,
                actual_linear_residual_relative_defect=residual_defect/max(
                    float(np.linalg.norm(actual_data_residual)), np.finfo(float).tiny),
                projected_gradient_absolute_defect=projected_defect,
                projected_gradient_relative_defect=relative_defect,
                projected_actual_gradient_norm=projected_actual_norm,
                forces_restart=bool(relative_defect > p.gradient_replacement_restart_relative))
            replacements.append(replacement)
            data_residual = actual_data_residual
            gradient = actual_gradient
            cz = rows.matvec(z)
        data_objective = float(data_residual @ data_residual)/2
        objective = data_objective + mu2*float(z @ z)/2
        record = dict(iteration=advances, objective=objective,
                      data_objective=data_objective, alpha=alpha,
                      unconstrained_alpha=unconstrained_alpha,
                      blocking_alpha=blocking_alpha if np.isfinite(blocking_alpha) else None,
                      blocker=blocker if blocked else None,
                      half_objective_slope=gd,
                      projected_gradient_norm_before=pg_norm,
                      direction_norm=direction_norm,
                      blocking_coordinate_length=blocking_length,
                      blocking_coordinate_length_overflow=blocking_length_overflow,
                      direction_kind=direction_kind,
                      preconditioned_projected_gradient_energy_before=preconditioned_energy,
                      euclidean_release_starter=bool(euclidean_starter_pending),
                      same_face_advances_through_step=same_face_advances,
                      data_hessian_direction_energy=float(ad @ ad),
                      regularized_direction_energy=curvature,
                      residual_replacement=replacement,
                      active_rows=len(face.indices),
                      maximum_linear_violation=float(np.max(cz-bounds, initial=0.0)))
        history.append(record)
        completed_euclidean_starter = bool(euclidean_starter_pending)
        if completed_euclidean_starter:
            preconditioner_state['euclidean_release_starters_completed'] += 1
            euclidean_starter_pending = False
        if blocked:
            added = face.add(blocker)
            transitions.append(dict(kind='blocking_step', advances=advances, **added))
            if not added.get('added'):
                status = 'dependent_blocker_after_feasible_step'
                break
            maximum_face_rank = max(maximum_face_rank, len(face.indices))
            direction = None
            direction_kind = None
            preconditioned_gradient = preconditioned_energy = None
            restarts.append(dict(advance=advances, reason='blocking_active_row_added', row=blocker))
            same_face_advances = 0
        else:
            new_projected_gradient = face.project(gradient)
            new_pg2 = float(new_projected_gradient @ new_projected_gradient)
            reason = None
            candidate = None
            beta = None
            preconditioned_gradient = preconditioned_energy = None
            skip_next = None
            if completed_euclidean_starter:
                # R677: complete the original Euclidean inward feasible step,
                # THEN begin a fresh correct PCG chain on the resulting face.
                # Do not claim an arbitrary Euclidean first d obeys every
                # historical PCG conjugacy identity in a different metric.
                reason = 'completed_euclidean_release_starter'
            elif advances >= p.maxiter:
                skip_next = 'inner_iteration_budget_reached'
            elif new_pg2 <= gradient_tolerance*gradient_tolerance:
                skip_next = 'Euclidean_projected_gradient_tolerance_reached'
            else:
                preconditioned_gradient, preconditioned_energy = projected_preconditioner(
                    new_projected_gradient, 'fixed_face_PCG_update')
                if preconditioned_gradient is None:
                    record.update(projected_gradient_norm_after=float(np.sqrt(new_pg2)),
                        restart_reason='fixed_preconditioner_application_failed',
                        conjugate_coefficient=None)
                    status = 'fixed_preconditioner_application_failed'
                    del ad, hd
                    break
                # y=P B P g_new; beta=y^T H d/(d^T H d) uses the already
                # paid H d. On an unchanged exact face this gives adjacent
                # H-conjugacy, and is the usual PCG recurrence in its metric.
                beta = float(preconditioned_gradient @ hd)/curvature
                if replacement is not None and replacement['forces_restart']:
                    reason = 'large_projected_gradient_replacement_defect'
                elif not np.isfinite(beta) or beta < 0:
                    reason = 'negative_or_nonfinite_conjugate_coefficient'
                else:
                    candidate = face.project(-preconditioned_gradient+beta*direction)
                    candidate_slope = float(gradient @ candidate)
                    # Pg^T PBPg is the actual preconditioned steepest slope.
                    # It, the candidate and its slope all scale by t under
                    # B -> t B. Raw ||Pg||^2 would have the wrong units here.
                    threshold = -p.minimum_direction_descent_fraction*preconditioned_energy
                    if (not np.isfinite(candidate_slope) or candidate_slope >= 0
                            or candidate_slope > threshold):
                        reason = 'insufficient_literal_preconditioned_descent_after_conjugate_update'
                    else:
                        record['next_direction_slope'] = candidate_slope
                        record['next_descent_reference_energy'] = preconditioned_energy
                        record['next_slope_over_preconditioned_reference'] = candidate_slope/preconditioned_energy
                        record['previous_direction_H_conjugacy_relative'] = abs(float(candidate @ hd))/max(
                            float(np.linalg.norm(candidate))*float(np.linalg.norm(hd)), np.finfo(float).tiny)
            record['conjugate_coefficient'] = beta
            record['projected_gradient_norm_after'] = float(np.sqrt(new_pg2))
            record['preconditioned_projected_gradient_energy_after'] = preconditioned_energy
            record['restart_reason'] = reason
            if skip_next is not None:
                record['next_direction_preparation_skipped'] = skip_next
            if reason is not None:
                restarts.append(dict(advance=advances, reason=reason))
                direction = None
                direction_kind = None
            else:
                direction = candidate
                direction_kind = 'preconditioned_conjugate' if candidate is not None else None
        if advances % p.progress_every == 0:
            emit('qp_linear_progress', **record,
                 operator_products=operator_products.copy())
        del ad, hd

    # Pay the actual linear residual and transpose at the final z for honest
    # KKT diagnostics, even when the inner count truncated the solve.
    actual_data_residual = np.asarray(operator.matvec(z)) + residual
    operator_products['matvec'] += 1
    final_residual_relative_defect = float(np.linalg.norm(actual_data_residual-data_residual))/max(
        float(np.linalg.norm(actual_data_residual)), np.finfo(float).tiny)
    data_residual = actual_data_residual
    gradient = np.asarray(operator.rmatvec(data_residual)) + mu2*z
    operator_products['rmatvec'] += 1
    cz = rows.matvec(z)
    multipliers = face.multipliers(gradient)
    projected_gradient = face.project(gradient)
    release_values, _, _ = face.release_candidates(gradient)
    final_release = dict(negative_raw_multiplier_count=int(np.count_nonzero(multipliers < 0)),
        largest_normalized_descent_gain=(release_values[0]['normalized_descent_gain']
                                        if release_values else 0.),
        normalized_candidates=release_values,
        actual_release_threshold=max(gradient_tolerance,
            p.early_release_relative_gain*float(np.linalg.norm(projected_gradient))),
        release_scope='Euclidean unit inward directions in the original augmented step norm; not raw multiplier magnitudes')
    active_slack = (bounds-cz)[face.indices]
    report = dict(
        schema='fullspace-feasible-active-set-fixed-PCG-v4', status=status,
        advances=advances, maxiter=p.maxiter, seconds=time.monotonic()-started,
        initial_data_objective=initial_data_objective,
        final_data_objective=float(data_residual @ data_residual)/2,
        final_regularized_objective=float(data_residual @ data_residual)/2+mu2*float(z@z)/2,
        coordinate_norm=float(np.linalg.norm(z)), damping=float(damping),
        frozen_v3_source=base_record,
        implementation_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        fixed_preconditioner=dict(enabled=True,
            declared_real_linear_SPD=True, global_SPD_proved_by_this_QP=False,
            source_and_scale_metadata=dict(preconditioner_metadata or {}),
            active_face_map='P B P in the ORIGINAL Euclidean coordinates',
            applications=preconditioner_state,
            solver_replaced_preconditioner=False,
            caller_required_to_freeze_operator=True,
            automatic_background_scale_selection=False,
            application_failure_policy='Explicit truncated failure with final actual diagnostics; no silent identity substitution',
            release_policy='Original Euclidean inward starter through its positive feasible step, followed by a new PCG chain'),
        initial_gradient_norm=initial_gradient_norm,
        gradient_tolerance=gradient_tolerance,
        final_face_projected_gradient_norm=float(np.linalg.norm(projected_gradient)),
        maximum_linear_violation=float(np.max(cz-bounds, initial=0.0)),
        minimum_multiplier=float(np.min(multipliers, initial=0.0)),
        maximum_complementarity_residual=float(np.max(np.abs(multipliers*active_slack), initial=0.0)),
        multipliers=multipliers.tolist(), active_face=face.metadata(),
        maximum_active_face_rank=maximum_face_rank,
        normalized_bounds=bounds.tolist(), normalized_row_values=cz.tolist(),
        normalized_final_slack=(bounds-cz).tolist(),
        row_matvec_calls=rows.dot_count, row_load_calls=rows.row_count,
        operator_products=operator_products, history=history, transitions=transitions,
        restarts=restarts, residual_replacements=replacements,
        longest_same_face_advances=longest_same_face_advances,
        final_actual_linear_residual_relative_defect=final_residual_relative_defect,
        final_normalized_release_diagnostics=final_release,
        reliable_update=dict(interval=p.gradient_refresh,
            unconditional_periodic_Krylov_restart=False,
            actual_linear_residual_recomputed=True,
            projected_replacement_restart_relative=p.gradient_replacement_restart_relative,
            minimum_literal_direction_descent_fraction=p.minimum_direction_descent_fraction,
            conjugate_coefficient='(P B P g_new)^T H d/(d^T H d), using the already paid H d',
            minimum_descent_reference='(P g_new)^T (P B P g_new), not raw ||P g_new||^2',
            preconditioned_residual_inner_product='(P g)^T (P B P g)',
            new_preconditioner=True, original_quadratic_and_Euclidean_step_norm_preserved=True,
            additional_matvec_budget='One actual A z at each existing refresh and at final diagnostics; no extra CG advances'),
        initial_point='z=0; original bounds retained, no artificial homogeneous tangency',
        zero_blocking_step_rule='alpha_block <= 1e-15/stable_BLAS_norm(d), equivalent to original-coordinate displacement <=1e-15; no alpha*norm overflow used for the decision',
        early_release=dict(interval=p.early_release_every,relative_gain=p.early_release_relative_gain,
            measure='-g dot unit inward feasible release direction; invariant under positive row rescaling',
            raw_multiplier_magnitude_threshold_used=False,
            same_direction_float_checks='literal g dot w, c_i dot w, g dot d, c_i dot d must have descent/inward signs'),
        nonlinear_acceptance_performed=False,
        limitations='A truncated numerical solution of this declared finite linear-inequality step QP; not a nonlinear geometry certificate')
    return z, report



def solve(operator, residual, row_matrix, bounds, *, damping,
          parameters=None, block_columns=32768, callback=None,
          preconditioner=None, preconditioner_metadata=None, v3_source=None):
    """Original solve interface plus an optional FIXED real linear SPD apply.

    preconditioner is a callable or an object with .apply. Keep its state,
    parent-dependent matrix and positive scales fixed until solve returns.
    The solver does not construct or rescale it. Supply its exact metadata
    explicitly. A failed application returns a truthful truncated status;
    no silent replacement by identity occurs. None delegates to the frozen
    original v3 solve and returns its unmodified report.
    """
    require_actions()
    base, base_record = _load_base(v3_source)
    if preconditioner is None:
        return base.solve(operator, residual, row_matrix, bounds, damping=damping,
            parameters=parameters, block_columns=block_columns, callback=callback)
    apply = getattr(preconditioner, 'apply', preconditioner)
    if not callable(apply):
        raise ValueError('Need one fixed real linear SPD callable or .apply object')
    return _solve_pcg(base, operator, residual, row_matrix, bounds, damping=damping,
        parameters=parameters, block_columns=block_columns, callback=callback,
        apply_preconditioner=apply, preconditioner_metadata=preconditioner_metadata,
        base_record=base_record)
