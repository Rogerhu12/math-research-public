"""R786. Delay the true terminal roll in arclength before applying the same R785 two-cap shear."""
import numpy as np

import r785_two_cap_separable_world_shear as shear
from r742_tilted_disk_two_jets import J, gather, trig, unary

base = shear.base
P, L, SM, HALF_WIDTH, R = base.P, base.L, base.SM, base.HALF_WIDTH, base.R
MILD_ANGLES = shear.MILD_ANGLES
offset = shear.offset
disk_world = shear.disk_world
end_limits = shear.end_limits
normal_to_disk_material = shear.normal_to_disk_material
profile_marks = shear.profile_marks
axial_marks = shear.axial_marks
angular_breaks = shear.angular_breaks
THICKNESS = .0024
RECOVERY_START = .004
RECOVERY_LENGTH = .08
PHASE_RAMP = .006


def clipped_quintic_jet(x):
    z = np.clip(x.v, 0., 1.)
    value = z**3 * (10. + z * (-15. + 6. * z))
    first = 30. * z**2 * (1. - z)**2
    second = 60. * z * (1. - z) * (1. - 2. * z)
    return unary(x, value, first, second)


def delay(phase):
    z = np.clip(float(phase) / PHASE_RAMP, 0., 1.)
    return THICKNESS * z**3 * (10. + z * (-15. + 6. * z))


def terminal_stations(phase):
    h = delay(phase)
    return [0., L - RECOVERY_START - RECOVERY_LENGTH, L - RECOVERY_START,
            L - THICKNESS, L - h, L - h/2., L]


def terminal_meridian(b, phase, order):
    v = L - b
    h = delay(phase)
    queued = v - h * (1 - clipped_quintic_jet((v - RECOVERY_START) / RECOVERY_LENGTH))
    s = unary(queued, np.maximum(queued.v, 0.), (queued.v > 0.).astype(float),
              np.zeros_like(queued.v))
    # p(s)-s and d(s) have orders 9 and 5 at zero. The resulting composition has
    # the same two-jet on either side of the positive-part switch.
    p, d = base.smooth_curve(s, L, base.RH, SM, order)
    pb, db = end_limits(order)
    return R - db + v + (p - s), pb - d


def chart_jet(chart, u, v, phase=0., order=20, mode="balanced", m=2, xi=.02,
              mix=1., turns=MILD_ANGLES):
    if not chart.startswith("end") or not phase:
        return shear.chart_jet(chart, u, v, phase, order, mode, m, xi, mix, turns)
    a, b = np.broadcast_arrays(np.asarray(u, float), np.asarray(v, float))
    flat_a, flat_b = a.ravel(), b.ravel()
    use = (L - flat_b) <= (RECOVERY_START + RECOVERY_LENGTH)
    out = np.empty((len(flat_a), 6, 3))
    if np.any(~use):
        out[~use] = shear.chart_jet(chart, flat_a[~use], flat_b[~use], phase,
                                    order, mode, m, xi, mix, turns)
    if np.any(use):
        e = J(flat_a[use], s=1.)
        radial, axial = terminal_meridian(J(flat_b[use], a=1.), phase, order)
        co, si = trig(e/R)
        sign = 1 if chart.endswith("+") else -1
        rim = .5 if sign > 0 else .5 - 6*base.half_table(float(phase), order)[1][-1, 0]
        field = gather([radial*co, rim + sign*axial, radial*si], len(radial.v))
        out[use] = shear.transform_jet(field, phase, order, turns)
    return out.reshape(a.shape+(6, 3))
