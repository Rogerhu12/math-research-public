"""Replace the single normalized central-gap row in an unscaled normal.

This is a NEW finite goal at the SAME field. It is not a continuation at a
new accepted vector, nor reuse of an old discretization as a new one. The
caller owns the in-memory normal; no checkpoint is read or overwritten.
All subsequent scaling, damping, Schur constraints and actual trials must
use the new goal explicitly. In particular this does not retarget an
already scaled Schur packet.
"""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path
import numpy as np


SCHEMA = 'fd2d-single-gap-row-retargeted-unscaled-normal-v1'


def _canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'),
                      ensure_ascii=False, allow_nan=False)


def _identity(array):
    a = np.ascontiguousarray(array)
    return dict(shape=list(a.shape), dtype=a.dtype.str,
                sha256=hashlib.sha256(a.tobytes()).hexdigest())


def gap_retarget_binding(old_binding, new_target):
    """Change exactly mathematical_settings.gap in an explicit finite goal."""
    new = copy.deepcopy(old_binding)
    old_target = float(new['mathematical_settings']['gap'])
    target = float(new_target)
    if not (np.isfinite(old_target) and old_target > 0 and
            np.isfinite(target) and target > 0):
        raise ValueError('Both normalized gap targets must be strictly positive')
    new['mathematical_settings']['gap'] = target
    return new


def replace_gap_row_in_place(normal, *, actual_gap, central_gap_gradient,
                             old_binding, new_binding):
    """Update only Hpp, gp, parameter squared norms, and residual squared.

    central_gap_gradient is the complete existing axes['gap_jacobian'] at
    the bound field, BEFORE division by target. It occupies the initial
    central columns; independent-tail and radial-design entries are zero.
    The normal must contain exactly one gap row and be unscaled/complete.
    Unchanged buffers are not copied or reassociated.
    """
    old_target = float(old_binding['mathematical_settings']['gap'])
    new_target = float(new_binding['mathematical_settings']['gap'])
    expected = gap_retarget_binding(old_binding, new_target)
    if _canonical(expected) != _canonical(new_binding):
        raise ValueError('This operation changes only the single gap target')
    if normal.row_groups.get('gap') != 1:
        raise ValueError('Exactly one original central-gap row is required')
    info = normal.info
    if info.get('full_finite_objective') is not True:
        raise ValueError('Use a complete finite normal, not a partial tile')
    if info.get('scaling_or_damping_applied') is not False:
        raise ValueError('Only unscaled, undamped normal blocks may be retargeted')
    current_binding = info.get('state_binding', {}).get('opaque_binding', {}).get(
        'field_and_finite_objective')
    if current_binding != old_binding:
        raise ValueError('The original normal does not bind the declared field and goal')
    gap = float(actual_gap)
    central = np.asarray(central_gap_gradient, float)
    if (not np.isfinite(gap) or central.ndim != 1 or not len(central)
            or len(central) > normal.mapping.P or not np.all(np.isfinite(central))):
        raise ValueError('A complete finite central gap derivative is required')
    gradient = np.zeros(normal.mapping.P)
    gradient[:len(central)] = central
    old_row = gradient/old_target
    new_row = gradient/new_target
    old_value = (gap-old_target)/old_target
    new_value = (gap-new_target)/new_target
    parent_squared = float(normal.residual_squared)
    update_pp = np.outer(new_row, new_row)-np.outer(old_row, old_row)
    update_gp = new_row*new_value-old_row*old_value
    update_norm = new_row*new_row-old_row*old_row
    update_squared = new_value*new_value-old_value*old_value
    if old_target != new_target:
        normal.Hpp += update_pp
        normal.gp += update_gp
        normal.parameter_norm_squared += update_norm
        normal.residual_squared += float(update_squared)
    if not (np.all(np.isfinite(normal.Hpp)) and np.all(np.isfinite(normal.gp))
            and np.all(np.isfinite(normal.parameter_norm_squared))
            and np.isfinite(normal.residual_squared)):
        raise FloatingPointError('Nonfinite derived normal')
    proof = dict(schema=SCHEMA, old_target=old_target, new_target=new_target,
        actual_gap=gap, unnormalized_parameter_gradient=_identity(gradient),
        old_gap_row=_identity(old_row), new_gap_row=_identity(new_row),
        old_gap_residual=old_value, new_gap_residual=new_value,
        parameter_normal_update=_identity(update_pp),
        parameter_gradient_update=_identity(update_gp),
        parameter_column_squares_update=_identity(update_norm),
        old_residual_squared=parent_squared,
        residual_squared_update=float(update_squared),
        new_residual_squared=float(normal.residual_squared),
        same_state=True, same_physical_metric_and_field=True,
        finite_goal_changed=(old_target != new_target),
        whole_F_or_J_recomputed=False,
        original_scaled_Schur_reused=False,
        unchanged_field_blocks_and_arrow=True,
        floating_bit_identity_with_reassembly_claimed=False,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    # The derived object does not pretend that old tile ledgers were recomputed.
    normal.info = dict(schema=SCHEMA, complete=True, full_finite_objective=True,
        scaling_or_damping_applied=False, rows=int(normal.rows),
        local_blocks=int(normal.blocks), row_groups=dict(normal.row_groups),
        residual_squared=float(normal.residual_squared),
        parent_complete_normal_info=copy.deepcopy(info),
        original_finite_goal=copy.deepcopy(old_binding),
        derived_finite_goal=copy.deepcopy(new_binding),
        gap_row_replacement=proof,
        newly_assembled_tile_set_claimed=False,
        exact_arithmetic_normal_for_declared_new_goal=True)
    return proof
