"""R733 physical insertion, with native meridian and circle arclength derivatives."""
import os

import numpy as np
from numpy.polynomial.legendre import leggauss


START_X = 0.80
BUFFER = 0.01
LEG = 0.018
ANGLE = 0.16
LENGTH = 4 * LEG
SMOOTH_WIDTH = 0.001
SLOPE_NORM = 0.998


def step_jet(s):
    """Clamped C3 ramp S, S', S'' in the dimensionless argument."""
    s = np.asarray(s, dtype=float)
    if not np.isfinite(s).all():
        raise ValueError("finite ramp coordinates required")
    left = np.minimum(s, 1 - s)
    z = np.clip((left - 0.0005) / SMOOTH_WIDTH, 0.0, 1.0)
    q = z**3 * (10 + z * (-15 + 6 * z))
    integral = z**4 * (2.5 + z * (-3 + z))
    p = (SMOOTH_WIDTH * integral + np.maximum(left - 0.0015, 0.0)) / SLOPE_NORM
    dp = q / SLOPE_NORM
    ddp = 30 * z**2 * (1 - z)**2 / (SMOOTH_WIDTH * SLOPE_NORM)
    return np.where(s <= 0.5, p, 1 - p), dp, np.where(s <= 0.5, ddp, -ddp)


class InsertedMeridian:
    """Right native material x starts at .80. The left copy is reflected."""
    def __init__(self, order=48):
        if os.environ.get("GITHUB_ACTIONS") != "true":
            raise RuntimeError("public Actions only")
        if int(order) != order or not 32 <= order <= 96:
            raise ValueError("integer Gauss order in [32,96] required")
        self.order = int(order)
        self.nodes, self.weights = leggauss(self.order)
        # Only integrate the first half. The last half obeys the actual reflection.
        cuts = {0.0, 2 * LEG}
        for a, width in ((0.0, LEG), (LEG, 2 * LEG)):
            for v in (0.0, 0.0005, 0.0015, 0.5, 0.9985, 0.9995, 1.0):
                t = a + width * v
                if t <= 2 * LEG:
                    cuts.add(t)
        self.cuts = np.array(sorted(cuts))
        primitives = self._integral(self.cuts[:-1], self.cuts[1:])
        self.prefix = np.vstack((np.zeros((1, 2)), np.cumsum(primitives, axis=0)))
        self.advance = float(2 * self.prefix[-1, 0])
        self.fillet_translation = BUFFER + self.advance

    @staticmethod
    def angle_jet(l):
        """Return theta, dtheta/dl and d2theta/dl2."""
        l = np.asarray(l, dtype=float)
        if not np.isfinite(l).all() or np.any((l < 0) | (l > LENGTH)):
            raise ValueError("material meridian arclength lies outside [0,.072]")
        right = l > 2 * LEG
        v = np.where(right, LENGTH - l, l)
        first = v < LEG
        width = np.where(first, LEG, 2 * LEG)
        s = np.where(first, v, v - LEG) / width
        step, step_d, step_dd = step_jet(s)
        start = np.where(first, 0.0, -ANGLE)
        amplitude = np.where(first, -ANGLE, 2 * ANGLE)
        theta = start + amplitude * step
        theta_d = amplitude * step_d / width
        theta_dd = amplitude * step_dd / width**2
        return np.where(right, -theta, theta), theta_d, np.where(right, -theta_dd, theta_dd)

    def _integral(self, lo, hi):
        half = (hi - lo) / 2
        points = lo[:, None] + half[:, None] * (1 + self.nodes)
        angle = self.angle_jet(points)[0]
        return half[:, None] * np.stack((np.cos(angle) @ self.weights,
                                          np.sin(angle) @ self.weights), axis=-1)

    def profile(self, l):
        """Absolute positive x, signed inward distance u, and the two native jets."""
        l = np.asarray(l, dtype=float)
        angle, curvature, _ = self.angle_jet(l)
        right = l > 2 * LEG
        v = np.where(right, LENGTH - l, l)
        unique, inverse = np.unique(v, return_inverse=True)
        i = np.clip(np.searchsorted(self.cuts, unique, side="right") - 1,
                    0, len(self.cuts) - 2)
        pos = self.prefix[i] + self._integral(self.cuts[i], unique)
        pos = pos[inverse.reshape(-1)].reshape(l.shape + (2,))
        x = START_X + np.where(right, self.advance - pos[..., 0], pos[..., 0])
        c, s = np.cos(angle), np.sin(angle)
        return (x, pos[..., 1], c, s, -curvature * s, curvature * c)

    def ring_jets(self, l, gamma, tangent, inward, kappa, kappa_s, side=1):
        """P, P_l, P_sigma, P_ll, P_lsigma, P_sigmasigma, each with last axis xyz.

        Inputs use actual native unit-speed circle data in yz. Normalize a circle
        coordinate in the caller using the real perimeter and the chain rule.
        """
        if side not in (-1, 1):
            raise ValueError("side must be 1 or -1")
        gamma, tangent, inward = (np.asarray(a, dtype=float) for a in (gamma, tangent, inward))
        if any(a.ndim == 0 or a.shape[-1] != 2 for a in (gamma, tangent, inward)):
            raise ValueError("gamma, tangent and inward must have last dimension 2")
        shape = np.broadcast_shapes(np.shape(l), np.shape(kappa), np.shape(kappa_s),
                                    gamma.shape[:-1], tangent.shape[:-1], inward.shape[:-1])
        gamma, tangent, inward = (np.broadcast_to(a, shape + (2,)) for a in (gamma, tangent, inward))
        l, kappa, kappa_s = (np.broadcast_to(a, shape) for a in (l, kappa, kappa_s))
        if not all(np.isfinite(a).all() for a in (gamma, tangent, inward, kappa, kappa_s)):
            raise ValueError("nonfinite physical circle data")
        x, u, dx, du, ddx, ddu = self.profile(l)
        a = 1 - u * kappa
        if np.any(a <= 0):
            raise ValueError("singular inward parallel circle coordinates")
        def xyz(xpart, yz):
            return np.concatenate((np.broadcast_to(xpart, shape)[..., None], yz), axis=-1)
        return (xyz(side*x, gamma + u[..., None]*inward),
                xyz(side*dx, du[..., None]*inward),
                xyz(0.0, a[..., None]*tangent),
                xyz(side*ddx, ddu[..., None]*inward),
                xyz(0.0, (-du*kappa)[..., None]*tangent),
                xyz(0.0, (a*kappa)[..., None]*inward - (u*kappa_s)[..., None]*tangent))
