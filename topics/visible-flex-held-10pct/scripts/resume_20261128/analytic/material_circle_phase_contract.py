#!/usr/bin/env python3
"""Explicit rational phase interval and material grip for a genuine circle arc.

This is the R54/R87 circle identity, independent of a mesh or numerical solve.
The actual source must already pass its own full lambda-one source gate.
The numerical center returned below evaluates the declared real expression;
it is not a new exact defining constant or a complete geometry certificate.
"""
from fractions import Fraction as Q
import math
import numpy as np


def describe(model, phase_end, held_width):
    phase_end, held_width = Q(phase_end), Q(held_width)
    core = model.prefix.core
    if (core.base_mode != 3 or core.homotopy != 1.
            or core.curvature_blend != 1.
            or not model.cylinder_half_length > 0):
        raise ValueError('Use an actual lambda-one constant-curvature arc and positive cylinder')
    k, S, b = (float(core.k), float(core.halfwidth), float(core.transition))
    if (not all(math.isfinite(v) for v in (k, S, b))
            or min(k, S, b) <= 0 or float(core.target_curvature) != k):
        raise ValueError('The actual circular curvature/window contract changed')
    if phase_end <= 0 or held_width <= 0:
        raise ValueError('The exact phase length and grip width must be positive')
    low, high = (phase_end-held_width)/2, (phase_end+held_width)/2
    margin = Q.from_float(S)-high
    if margin <= 0:
        raise ValueError('The entire grip sweep must lie strictly inside the actual circular window')
    return dict(
        phase_end_exact=str(phase_end), time_interval_exact=['0','1'],
        phase_definition=f'alpha(t)=({phase_end})*t',
        held_material_width_exact=str(held_width),
        grip_offsets_from_halfperiod_exact=[str(low),str(high)],
        complete_sweep_offsets_exact=[str(-high),str(high)],
        actual_binary_halfwidth_exact=str(Q.from_float(S)),
        strict_material_window_margin_exact=str(margin),
        actual_binary_transition_exact=str(Q.from_float(b)),
        actual_binary_circular_curvature_exact=str(Q.from_float(k)),
        actual_binary_cylinder_half_length_exact=str(Q.from_float(float(model.cylinder_half_length))),
        circle_identity='Gamma(L+x)=O+(1/k)*e(L+k*x)',
        held_rigid_expression='R_(-(1-k)*alpha)G_alpha+O-R_(k*alpha)O',
        symbolic_sweep_inclusion_checked=True,
        numerical_center_is_exact_defining_constant=False,
        sampled_mesh_proves_metric_reach_or_held_ratio=False)


def held_frame(model, phase_end, held_width, circle):
    describe(model, phase_end, held_width)
    core = model.prefix.core
    center = np.asarray(core.evaluate(np.asarray([core.halfperiod]))['F'][0],float).copy()
    center -= np.asarray(circle(core.halfperiod),float)/float(core.k)
    if center.shape != (3,) or not np.all(np.isfinite(center)):
        raise ValueError('The actual arc-center evaluation is nonfinite')
    return center, float(core.k)
