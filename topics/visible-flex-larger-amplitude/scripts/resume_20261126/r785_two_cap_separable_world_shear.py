"""R785. A common four-sector development of both complete R781 end caps.

The map acts on every chart, including the entire axial cylinder, by one
separable world shear. Its MILD_ANGLES and balanced xi in [0,.02] have a
whole-surface reach bound above .03 times the original diameter.
"""
import numpy as np

import r783_four_developable_cap_flaps as flaps
from r742_tilted_disk_two_jets import J, gather


base = flaps.base
P, L, SM, HALF_WIDTH, R = base.P, base.L, base.SM, base.HALF_WIDTH, base.R
MILD_ANGLES = flaps.MILD_ANGLES
offset = base.offset
end_limits = base.end_limits
disk_world = base.disk_world
normal_to_disk_material = base.normal_to_disk_material
profile_marks = base.profile_marks
axial_marks = base.axial_marks
angular_breaks = flaps.angular_breaks


def transform_jet(field, phase=0., order=20, turns=MILD_ANGLES):
    angles = flaps.checked_angles(turns)
    phase = float(phase)
    if not 0. <= phase <= np.pi / 2 + 2.e-14:
        raise ValueError("phase outside the R781 interval")
    if not phase or not np.any(angles):
        return field
    shape = field.shape
    flat = np.asarray(field, float).reshape(-1, 6, 3)
    x, y, z = (J(*flat[:, :, i].T) for i in range(3))
    horizontal = {0: x, 2: z}
    moved = [x, y, z]
    _, start, _ = flaps.cap_dimensions(order)
    for (axis, sign), amplitude in zip(flaps.DIRECTIONS, angles * np.sin(phase)**2):
        if amplitude == 0.:
            continue
        delta, height, _, _ = flaps.turn_jet(sign * horizontal[axis], start, amplitude, order)
        moved[axis] = moved[axis] + sign * delta
        moved[1] = moved[1] + height
    return gather(moved, len(flat)).reshape(shape)


def chart_jet(chart, u, v, phase=0., order=20, mode="balanced", m=2, xi=.02,
              mix=1., turns=MILD_ANGLES):
    source = base.chart_jet(chart, u, v, phase, order, mode=mode, m=m, xi=xi, mix=mix)
    return transform_jet(source, phase, order, turns)
