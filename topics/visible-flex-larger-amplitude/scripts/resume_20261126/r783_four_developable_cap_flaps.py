"""R783. Four independent exact disk developments of the R781 circular right cap.

The mild profile gives one entire physical closed reference, including the two
rolls and both caps. Angular arclength and all jet slots follow R781. Angles are
nonnegative radians in the actual world X and Z directions. Integral values
are evaluated at the supplied quadrature order on each original clock piece.
"""
from functools import lru_cache

import numpy as np

import r781_round_three_lobe_spatial_rings as base
from r742_tilted_disk_two_jets import J, cap_s7, gather, trig, unary


P, L, SM, HALF_WIDTH, R = base.P, base.L, base.SM, base.HALF_WIDTH, base.R
offset = base.offset
end_limits = base.end_limits
disk_world = base.disk_world
normal_to_disk_material = base.normal_to_disk_material
profile_marks = base.profile_marks
axial_marks = base.axial_marks

WIDTH = .08
MAX_ANGLE = .08
MILD_ANGLES = (.020, .022, .024, .025)
SMALL_TUBE_ANGLES = (.00000080, .00000085, .00000090, .00000100)
DIRECTIONS = ((0, 1), (0, -1), (2, 1), (2, -1))
GATE_START = .36
GATE_WIDTH = .165


def cap_dimensions(order):
    axial_end, radial_end = end_limits(order)
    radius = R - radial_end
    return radius, radius / np.sqrt(2.), .5 + axial_end


def clock_angle(distance, amplitude):
    value, rate, acceleration = base.clock(distance / WIDTH)
    return amplitude * value, amplitude * rate / WIDTH, amplitude * acceleration / WIDTH**2


@lru_cache(maxsize=256)
def integrated_turn(amplitude, order):
    cut = WIDTH * np.array([0., base.ROUND, 1. - base.ROUND, 1.])
    nodes, weights = base.rule(order)
    spans = np.diff(cut)
    angles = clock_angle(cut[:-1, None] + spans[:, None] * nodes, amplitude)[0]
    rates = np.column_stack(((-2 * np.sin(angles / 2)**2) @ weights,
                             np.sin(angles) @ weights))
    return cut, np.vstack((np.zeros(2), np.cumsum(spans[:, None] * rates, axis=0)))


def turn_jet(u, start, amplitude, order):
    distance = u.v - start
    cut, table = integrated_turn(float(amplitude), order)
    clipped = np.clip(distance, 0., WIDTH)
    index = np.clip(np.searchsorted(cut, clipped, side="right") - 1, 0, len(cut) - 2)
    span = clipped - cut[index]
    nodes, weights = base.rule(order)
    angles = clock_angle(cut[index, None] + span[:, None] * nodes, amplitude)[0]
    delta = table[index] + span[:, None] * np.column_stack(
        ((-2 * np.sin(angles / 2)**2) @ weights, np.sin(angles) @ weights))
    exterior = np.maximum(distance - WIDTH, 0.)
    delta[:, 0] -= 2 * np.sin(amplitude / 2)**2 * exterior
    delta[:, 1] += np.sin(amplitude) * exterior
    angle, rate, acceleration = clock_angle(distance, amplitude)
    cosine, sine = trig(unary(u, angle, rate, acceleration))
    displacement = unary(u, delta[:, 0], -2 * np.sin(angle / 2)**2, -sine.v * rate)
    height = unary(u, delta[:, 1], sine.v, cosine.v * rate)
    return displacement, height, cosine, sine


def material_cap_jet(x, z, phase=0., order=20, turns=MILD_ANGLES):
    """Actual Cartesian disk map and six material jet slots on the entire initial disk."""
    aa, bb = np.broadcast_arrays(np.asarray(x, float), np.asarray(z, float))
    top = cap_dimensions(order)[2]
    coordinates = (J(aa.ravel(), s=1.), J(np.full(aa.size, top)), J(bb.ravel(), a=1.))
    initial = gather(coordinates, aa.size)
    return transform_jet(initial, phase, order, turns).reshape(aa.shape + (6, 3))


def checked_angles(turns):
    angles = np.asarray(turns, dtype=float)
    if angles.shape != (4,) or not np.all(np.isfinite(angles)) or np.any(
            (angles < 0.) | (angles > MAX_ANGLE)):
        raise ValueError("four independent maximum angles in [0,.08] are required")
    return angles


def transform_jet(field, phase=0., order=20, turns=MILD_ANGLES):
    """Apply a single world map to all R781 charts, including both sides of each seam."""
    angles = checked_angles(turns)
    phase = float(phase)
    if not 0. <= phase <= np.pi / 2 + 2.e-14:
        raise ValueError("phase outside the R781 interval")
    if not phase or not np.any(angles):
        return field
    shape = field.shape
    flat = np.asarray(field, float).reshape(-1, 6, 3)
    x, y, z = (J(*flat[:, :, i].T) for i in range(3))
    _, start, top = cap_dimensions(order)
    depth = y - top
    gate = cap_s7((y - GATE_START) / GATE_WIDTH)
    corrections = [J(np.zeros(flat.shape[0])) for _ in range(3)]
    amplitudes = angles * np.sin(phase)**2
    for (axis, sign), amplitude in zip(DIRECTIONS, amplitudes):
        if amplitude == 0.:
            continue
        u = sign * (x if axis == 0 else z)
        delta, height, cosine, sine = turn_jet(u, start, amplitude, order)
        corrections[axis] = corrections[axis] + sign * (delta - depth * sine)
        corrections[1] = corrections[1] + height + depth * (cosine - 1.)
    physical = [coordinate + gate * change
                for coordinate, change in zip((x, y, z), corrections)]
    return gather(physical, len(flat)).reshape(shape)


def chart_jet(chart, u, v, phase=0., order=20, mode="short", m=2, xi=0.,
              mix=1., turns=MILD_ANGLES):
    source = base.chart_jet(chart, u, v, phase, order, mode=mode, m=m, xi=xi, mix=mix)
    return transform_jet(source, phase, order, turns)


def angular_breaks(order=20):
    """True cap-rim directional activation and clock joins, plus the R781 marks."""
    radius, start, _ = cap_dimensions(order)
    marks = list(base.profile_marks())
    for station in (start, start + WIDTH * base.ROUND,
                    start + WIDTH * (1 - base.ROUND), start + WIDTH):
        if station >= radius:
            continue
        beta = np.arccos(station / radius)
        for orientation in np.arange(4) * np.pi / 2:
            for sign in (-1., 1.):
                marks.append(R * ((orientation + sign * beta) % (2 * np.pi)))
    return np.unique(marks).tolist()
