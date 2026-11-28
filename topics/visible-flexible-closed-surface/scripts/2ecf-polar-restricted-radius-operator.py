"""Exact restriction of the Cartesian/log-radius operator to free suffix coefficients."""
import gc
import numpy as np
from scipy.linalg import cholesky_banded, cho_solve_banded


class RestrictedLinear:
    def __init__(self, full, locked):
        self.full = full
        self.locked = locked
        self.basis = full.basis
        width = full.columns_per_radial_row
        if not 0 < locked < full.basis.nb:
            raise ValueError("A proper nonempty radial suffix is required")
        indices = np.arange(full.shape[1])
        is_radius = indices % width == width - 1
        self.keep = indices[~is_radius | (indices // width >= locked)]
        self.radius_indices = np.flatnonzero(is_radius[self.keep])
        self.position_indices = np.flatnonzero(~is_radius[self.keep])
        self.residual = full.residual
        self.shape = (full.shape[0], len(self.keep))

    def expand(self, vector):
        out = np.zeros(self.full.shape[1])
        out[self.keep] = vector
        return out

    def pack(self, z, alpha):
        return self.full.pack(z, alpha)[self.keep]

    def split(self, vector):
        return self.full.split(self.expand(vector))

    def matvec(self, vector):
        return self.full.matvec(self.expand(vector))

    def transpose(self, covector):
        return self.full.transpose(covector)[self.keep]

    def sobolev_apply(self, vector):
        return self.full.sobolev_apply(self.expand(vector))[self.keep]

    def cross_normal(self):
        cross, gram = self.full.cross_normal()
        return cross[:, self.locked:], gram[self.locked:, self.locked:]


class RestrictedNormal:
    def __init__(self, full_operator, linear, damping):
        self.linear = linear
        self.damping = damping
        full_factor = full_operator.FullDesignNormal(linear.full, damping)
        band = full_factor.unscaled_band
        source_receipt = full_factor.receipt
        self.half_bandwidth = min(len(linear.keep)-1, full_factor.half_bandwidth)
        del full_factor
        gc.collect()
        keep = linear.keep
        reduced = np.zeros((self.half_bandwidth+1,len(keep)))
        for offset in range(self.half_bandwidth+1):
            count = len(keep)-offset
            columns = keep[:count]
            distances = keep[offset:]-columns
            inside = distances < len(band)
            reduced[offset,:count][inside] = band[distances[inside],columns[inside]]
        del band
        self.unscaled_band = reduced.copy()
        self.scale = 1/np.sqrt(reduced[0])
        for offset in range(len(reduced)):
            count = len(keep)-offset
            reduced[offset,:count] *= self.scale[:count]*self.scale[offset:]
        self.factor = cholesky_banded(reduced,lower=True)
        self.receipt = dict(schema="exact-principal-submatrix-restricted-log-radius-normal-v1",
            fullAssembly=source_receipt,actualColumns=len(keep),lockedPrefix=linear.locked,
            retainedCartesian=len(linear.position_indices),retainedRadius=len(linear.radius_indices),
            allCrossTermsAmongAdmissibleColumnsRetained=True)

    def solve(self, gradient):
        return self.scale*cho_solve_banded((self.factor,True),self.scale*gradient)

    def residual(self, direction):
        return (self.linear.transpose(self.linear.matvec(direction)) +
                self.damping*self.linear.sobolev_apply(direction) +
                self.linear.transpose(self.linear.residual))
