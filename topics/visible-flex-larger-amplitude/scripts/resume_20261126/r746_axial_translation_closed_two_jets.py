#!/usr/bin/env python3
"""R746 axial translation on an entire periodic cylinder, with moving free ends.

The direct physical two-jet order is (F, F_u, F_v, F_uu, F_uv, F_vv).
Arguments broadcast; Phase is the physical angle in [0,pi/2], not a derivative
coordinate. All geometric quadrature is performed on the public runner.
"""
from dataclasses import dataclass
from functools import lru_cache
import numpy as np

import r744_extruded_closed_two_jets as old
from r742_tilted_disk_two_jets import J, cap_s7, gather, unary


RADIUS = old.PLANAR_TURN
CAP_RADIUS = .04
CAP_X = 0.


@dataclass(frozen=True)
class EndModes:
    """Independent outward amplitudes for the two rolled annuli and flat caps."""
    roll_plus: float = 1.e-6
    roll_minus: float = 2.e-6
    cap_plus: float = .75
    cap_minus: float = .50


REFERENCE = EndModes()
ZERO_ENDS = EndModes(0., 0., 0., 0.)


@lru_cache(maxsize=None)
def axis(order=32):
    """The genuine center of the constant-curvature right turn, not its comparison center."""
    old.disk._public()
    _, _, main_end, _, _, *_ = old.profile_constants(order)
    s = main_end + old.PLANAR_BLEND + RADIUS * .35
    q, _, n, _, _ = old.profile_coordinates(np.asarray(s), order)
    return tuple(q - RADIUS * n)


def grip_arclength(alpha, order=32):
    """Material s for points on the exact right circle; .10 <= alpha <= 1.05 is the grip."""
    old.disk._public()
    _, _, main_end, _, _, *_ = old.profile_constants(order)
    return main_end + old.PLANAR_BLEND / 2 + RADIUS * np.asarray(alpha)


def cap_displacement(x, z, coefficient):
    a = 1 - ((x-CAP_X)*(x-CAP_X) + z*z) / CAP_RADIUS**2
    positive = np.maximum(a.v, 0.)
    fourth = unary(a, positive**4, 4*positive**3, 12*positive**2)
    return coefficient * CAP_RADIUS**2 * fourth


def cap_point(chart, u, v, order):
    p_end, t_end = old.end_limits(order)
    sg = 1 if chart.endswith("+") else -1
    if chart.startswith("cap-cartesian"):
        x, z = u, v
    else:
        q, n = old.profile(u, order)
        if chart.startswith("cap-normal"):
            if np.any((v.v < 0) | (v.v > old.CAP_NORMAL_CHART_WIDTH+2e-14)):
                raise ValueError("planar collar coordinate outside chart")
            x, z = [q[i]-(t_end+v)*n[i] for i in range(2)]
        else:
            if np.any((v.v < 0) | (v.v > 1+2e-14)):
                raise ValueError("planar radial fraction outside chart")
            x = old.CENTER_X + v*(q[0]-t_end*n[0]-old.CENTER_X)
            z = v*(q[1]-t_end*n[1])
    return x, sg*J(1+p_end), z


def source_chart(chart, u, v, phase, modes, order):
    """Physical points and full material jets before the spatial rotation."""
    amp = np.sin(phase)
    if chart == "cylinder":
        if np.any(np.abs(v.v) > 1+2e-14):
            raise ValueError("transverse coordinate outside cylinder")
        q, _ = old.profile(u + RADIUS*phase, order)
        return q[0], v, q[1]
    if chart in ("end+", "end-"):
        if np.any((v.v < 0) | (v.v > old.END_LENGTH+2e-14)):
            raise ValueError("rolling arclength outside end")
        chi = 1-cap_s7(v / old.END_LENGTH)
        q, n = old.profile(u+RADIUS*phase*chi, order)
        p, t = old.end_offsets(v, order)
        x, z = [q[i]-t*n[i] for i in range(2)]
        p_end, _ = old.end_limits(order)
        w = p / p_end
        bell = 4*w*(1-w)
        bell2 = bell*bell
        sg = 1 if chart.endswith("+") else -1
        coefficient = modes.roll_plus if sg == 1 else modes.roll_minus
        y = sg*(1+p+coefficient*amp*bell2*bell2*(1+.20*x+.10*z))
        return x, y, z
    if chart in ("cap+", "cap-", "cap-normal+", "cap-normal-",
                 "cap-cartesian+", "cap-cartesian-"):
        x, y, z = cap_point(chart, u, v, order)
        sg = 1 if chart.endswith("+") else -1
        coefficient = modes.cap_plus if sg == 1 else modes.cap_minus
        return x, y + sg*cap_displacement(x, z, coefficient*amp), z
    raise ValueError("unknown R746 chart " + str(chart))


def chart_jet(chart, u, v, phase=0., order=32, modes=REFERENCE, free_field=None):
    """Physical two-jets on every closed chart, with both ends available for correction.

    Coordinates are R744 cylinder (u=s,v=y), end± (u=s,v=outward
    arclength), cap± (u=s,v=star fraction), cap-normal± (u=s,v=extra
    inward offset), or cap-cartesian± (u=x,v=z in the actual star disk).
    free_field(x,y,z,phase) may return three additive J-valued physical
    coordinates in the pre-rotation frame. The same field on overlapping
    charts changes the actual image and its seam, including cap rims. To
    retain a fixed grip it must vanish on the swept physical grip sector.
    The bounds in the paper apply to the named modes with free_field=None.
    """
    old.disk._public()
    u0, v0, ph0 = np.broadcast_arrays(np.asarray(u,dtype=float),
                                       np.asarray(v,dtype=float),
                                       np.asarray(phase,dtype=float))
    if np.any((ph0<0) | (ph0>np.pi/2+2e-14)):
        raise ValueError("R746 phase outside certified range")
    ph = ph0.ravel()
    x,y,z = source_chart(chart,J(u0.ravel(),s=1.),J(v0.ravel(),a=1.),ph,modes,order)
    if free_field is not None:
        dx,dy,dz = free_field(x,y,z,ph)
        x,y,z = x+dx,y+dy,z+dz
    ox,oz = axis(order)
    c,si = np.cos(ph),np.sin(ph)
    dx,dz = x-ox,z-oz
    points = (ox+c*dx-si*dz,y,oz+si*dx+c*dz)
    return gather(points,u0.size).reshape(u0.shape+(6,3))
