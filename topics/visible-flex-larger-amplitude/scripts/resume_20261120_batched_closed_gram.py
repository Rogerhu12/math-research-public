#!/usr/bin/env python3
"""Batched implementation of the original finite ClosedGram operator.

All physical stages, affine coordinates, and the untruncated analytic
circle lift are unchanged.  ``quarter=True`` evaluates the reflection
orbits of an even Fourier field on 0 <= phi <= pi/2.  Residuals and Jv
then include sqrt(orbit multiplicity), so their Euclidean norm and
normal equations agree with the original full, uniform angular grid.

The raw physical Gram components are available through raw_residual()
or unweight().  External stage/Frobenius weights must still be applied
to both forward and transpose; do not apply orbit weights a second time.
No nonlinear solver or input generation is launched on import.
"""
from pathlib import Path
import importlib.util
import sys
import numpy as np
from scipy.fft import dct, dst


class SampledTrig:
    """Vector view of a batched cosine/sine map and its Euclidean transpose."""

    def __init__(self, owner, kind, *, constant=True, transposed=False, sign=1):
        self.owner, self.kind = owner, kind
        self.constant = bool(constant and kind == 'cos')
        self.transposed, self.sign = bool(transposed), int(sign)

    @property
    def shape(self):
        n, m = self.owner.N, self.owner.M + int(self.constant)
        return (m, n) if self.transposed else (n, m)

    @property
    def T(self):
        return SampledTrig(self.owner, self.kind, constant=self.constant,
                           transposed=not self.transposed, sign=self.sign)

    def __neg__(self):
        return SampledTrig(self.owner, self.kind, constant=self.constant,
                           transposed=self.transposed, sign=-self.sign)

    def __getitem__(self, key):
        if (self.transposed or self.kind != 'cos' or not self.constant
                or not isinstance(key, tuple) or len(key) != 2
                or key[0] != slice(None) or key[1] != slice(1, None)):
            raise IndexError('Only C[:,1:] is used by the original operator')
        return SampledTrig(self.owner, 'cos', constant=False, sign=self.sign)

    def __matmul__(self, value):
        value = np.asarray(value)
        if value.ndim != 1 or value.shape[0] != self.shape[1]:
            raise ValueError('Wrong finite trigonometric vector shape')
        if self.transposed:
            out = self.owner._trig_adjoint(value[None, :], self.kind)[0]
            if self.kind == 'cos' and not self.constant:
                out = out[1:]
        else:
            if self.kind == 'cos' and not self.constant:
                value = np.concatenate((np.zeros(1, dtype=value.dtype), value))
            out = self.owner._trig_values(value[None, :], self.kind)[0]
        return self.sign * out


class BatchedMixin:
    """Attach to the unchanged original ClosedGram class.

    ``N`` at construction means the original full angular count.  The
    instance's ``N`` is the number of evaluated angles, while ``full_N``
    always retains the original count.  At M160/J923/N2048 the quarter
    cache is about 45.4 MB and one returned residual about 22.7 MB.
    ``stage_block`` bounds transform/intermediate storage independently
    of the number of stages.
    """

    def __init__(self, *args, stage_block=64, quarter=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.full_N = self.N
        self.quarter = bool(quarter)
        self.stage_block = int(stage_block)
        if self.stage_block < 1:
            raise ValueError('stage_block must be positive')
        if self.full_N % 2 or self.full_N <= 4*self.M:
            raise ValueError('The FFT representation requires even full N > 4M')
        if self.quarter and self.full_N % 4:
            raise ValueError('Quarter orbits require full N divisible by four')
        self._frequencies = 2*np.arange(1, self.M+1)
        if self.quarter:
            self._L = self.full_N//4
            self.N = self._L+1
            self.phi = np.pi*np.arange(self.N)/(2*self._L)
            self.multiplicity = np.full(self.N, 4., dtype=float)
            self.multiplicity[[0, -1]] = 2.
        else:
            self._L = None
            self.multiplicity = np.ones(self.N, dtype=float)
        self.sqrt_multiplicity = np.sqrt(self.multiplicity)
        self.multiplicity.setflags(write=False)
        self.sqrt_multiplicity.setflags(write=False)
        self.cos = SampledTrig(self, 'cos')
        self.sin = SampledTrig(self, 'sin')
        self._mid_weights_array = np.asarray(self.mid_weights)
        self._base_x = None
        self._base_p = None
        self._base_first = None
        self.cache_builds = 0
        self.cache_hits = 0

    def _trig_values_real(self, coeffs, kind):
        coeffs = np.asarray(coeffs)
        if self.quarter:
            if kind == 'cos':
                padded = np.zeros(coeffs.shape[:-1]+(self.N,), dtype=coeffs.dtype)
                padded[..., 0] = coeffs[..., 0]
                padded[..., 1:self.M+1] = coeffs[..., 1:]/2
                return dct(padded, type=1, axis=-1)
            padded = np.zeros(coeffs.shape[:-1]+(self.N-2,), dtype=coeffs.dtype)
            padded[..., :self.M] = coeffs/2
            result = np.zeros(coeffs.shape[:-1]+(self.N,), dtype=coeffs.dtype)
            result[..., 1:-1] = dst(padded, type=1, axis=-1)
            return result
        spectrum = np.zeros(coeffs.shape[:-1]+(self.N//2+1,), dtype=complex)
        if kind == 'cos':
            spectrum[..., 0] = self.N*coeffs[..., 0]
            spectrum[..., self._frequencies] = (self.N/2)*coeffs[..., 1:]
        else:
            spectrum[..., self._frequencies] = (-.5j*self.N)*coeffs
        return np.fft.irfft(spectrum, n=self.N, axis=-1)

    def _trig_values(self, coeffs, kind):
        coeffs = np.asarray(coeffs)
        if np.iscomplexobj(coeffs):
            return (self._trig_values_real(coeffs.real, kind)
                    + 1j*self._trig_values_real(coeffs.imag, kind))
        return self._trig_values_real(coeffs, kind)

    def _trig_adjoint_real(self, values, kind):
        values = np.asarray(values)
        if self.quarter:
            if kind == 'cos':
                padded = values.copy()
                padded[..., 1:-1] *= .5
                return dct(padded, type=1, axis=-1)[..., :self.M+1]
            return .5*dst(values[..., 1:-1], type=1, axis=-1)[..., :self.M]
        spectrum = np.fft.rfft(values, axis=-1)
        if kind == 'sin':
            return -spectrum[..., self._frequencies].imag
        return np.concatenate((spectrum[..., :1].real,
                               spectrum[..., self._frequencies].real), axis=-1)

    def _trig_adjoint(self, values, kind):
        values = np.asarray(values)
        if np.iscomplexobj(values):
            return (self._trig_adjoint_real(values.real, kind)
                    + 1j*self._trig_adjoint_real(values.imag, kind))
        return self._trig_adjoint_real(values, kind)

    def _stage_pair(self, jets, start, stop):
        """Vectorized original node/quintic-midpoint Y and U values."""
        stages = np.arange(start, stop)
        left = stages//2
        odd = (stages % 2).astype(bool)
        values = jets[left, :2, :].copy()
        if np.any(odd):
            cells = left[odd]
            endpoints = np.stack((jets[cells], jets[cells+1]), axis=1)
            values[odd] = np.einsum('bqc,bcn->bqn',
                self._mid_weights_array[cells, :2, :],
                endpoints.reshape((-1, 6, self.n)))
        return values[:, 0], values[:, 1]

    def _stage_pair_adjoint(self, grad, start, stop, gy, gu):
        stages = np.arange(start, stop)
        left = stages//2
        odd = (stages % 2).astype(bool)
        even = ~odd
        if np.any(even):
            cells = left[even]
            grad[cells, 0] += gy[even]
            grad[cells, 1] += gu[even]
        if np.any(odd):
            cells = left[odd]
            w = self._mid_weights_array[cells]
            contribution = (w[:, 0, :, None]*gy[odd, None, :]
                            + w[:, 1, :, None]*gu[odd, None, :])
            # Within each update the indices are distinct.  Left and right
            # updates are sequential so shared endpoint contributions add.
            grad[cells] += contribution[:, :3]
            grad[cells+1] += contribution[:, 3:]

    def _linear_fields(self, y, u):
        """Return synth(U) and angular(Y), with all six transforms batched."""
        M, nu = self.M, self.freq
        dtype = np.result_type(y.dtype, u.dtype, float)
        c = np.empty((len(y), 3, M+1), dtype=dtype)
        s = np.empty((len(y), 3, M), dtype=dtype)
        # Cosine fields: V_R, V_Z, d_T.
        c[:, 0] = u[:, :M+1]
        c[:, 1] = u[:, 2*M+1:]
        c[:, 2] = y[:, :M+1]
        c[:, 2, 1:] += nu*y[:, M+1:2*M+1]
        # Sine fields: V_T, d_R, d_Z.
        s[:, 0] = u[:, M+1:2*M+1]
        s[:, 1] = -nu*y[:, 1:M+1]-y[:, M+1:2*M+1]
        s[:, 2] = -nu*y[:, 2*M+2:]
        cv = self._trig_values(c, 'cos')
        sv = self._trig_values(s, 'sin')
        V = np.empty((len(y), self.N, 3), dtype=dtype)
        d = np.empty_like(V)
        V[:, :, 0], V[:, :, 1], V[:, :, 2] = cv[:, 0], sv[:, 0], cv[:, 1]
        d[:, :, 0], d[:, :, 1], d[:, :, 2] = sv[:, 1], cv[:, 2], sv[:, 2]
        return V, d

    def _linear_fields_adjoint(self, gV, gd):
        """Ordinary bilinear transpose; complex inputs are continued linearly."""
        c = np.stack((gV[:, :, 0], gV[:, :, 2], gd[:, :, 1]), axis=1)
        s = np.stack((gV[:, :, 1], gd[:, :, 0], gd[:, :, 2]), axis=1)
        ct = self._trig_adjoint(c, 'cos')
        st = self._trig_adjoint(s, 'sin')
        M, nu = self.M, self.freq
        gu = np.empty((len(gV), self.n), dtype=np.result_type(gV.dtype, gd.dtype, float))
        gy = np.empty_like(gu)
        gu[:, :M+1] = ct[:, 0]
        gu[:, M+1:2*M+1] = st[:, 0]
        gu[:, 2*M+1:] = ct[:, 1]
        gy[:, :M+1] = ct[:, 2]
        gy[:, 1:M+1] -= nu*st[:, 1]
        gy[:, M+1:2*M+1] = -st[:, 1]+nu*ct[:, 2, 1:]
        gy[:, 2*M+1] = 0.
        gy[:, 2*M+2:] = -nu*st[:, 2]
        return gy, gu

    def prepare(self, x):
        x = np.asarray(x)
        if (self._base_x is not None and x.dtype == self._base_x.dtype
                and x.shape == self._base_x.shape and np.array_equal(x, self._base_x)):
            self.cache_hits += 1
            return self._base_p
        return super().prepare(x)

    def _first_batch_uncached(self, p, start, stop):
        y, u = self._stage_pair(p.jets, start, stop)
        V, d = self._linear_fields(y, u)
        cp = self.lift_scalar[start:stop, 1]
        f = self.lift_scalar[start:stop, 3]
        fp = self.lift_scalar[start:stop, 4]
        V += fp[:, None, None]*p.er[None, :, :]
        V[:, :, 2] += cp[:, None]*p.height
        d += f[:, None, None]*(p.rho[:, None]*p.et)[None, :, :]
        return V, d

    def _first_batch(self, p, start, stop):
        if p is self._base_p and self._base_first is not None:
            return self._base_first[0, start:stop], self._base_first[1, start:stop]
        return self._first_batch_uncached(p, start, stop)

    def _first(self, p, stage):
        if p is self._base_p and self._base_first is not None:
            return self._base_first[0, stage], self._base_first[1, stage]
        return super()._first(p, stage)

    def set_base(self, x):
        """Cache the actual real point once; no automatic candidate caching."""
        x = np.asarray(x)
        if np.iscomplexobj(x) or x.dtype != np.dtype(float) or x.shape != (self.free_size,):
            raise ValueError('Base cache requires the actual float64 free vector')
        p = super().prepare(x)
        values = np.empty((2, self.P, self.N, 3), dtype=float)
        for start in range(0, self.P, self.stage_block):
            stop = min(start+self.stage_block, self.P)
            values[0, start:stop], values[1, start:stop] = self._first_batch_uncached(p, start, stop)
        frozen = x.copy()
        frozen.setflags(write=False)
        values.setflags(write=False)
        self._base_x, self._base_p, self._base_first = frozen, p, values
        self.cache_builds += 1
        return dict(first_derivative_cache_bytes=int(values.nbytes),
                    base_vector_bytes=int(frozen.nbytes), full_stages=self.P,
                    evaluated_angles=self.N, full_angles=self.full_N,
                    stage_block=self.stage_block, cache_builds=self.cache_builds,
                    quarter_orbits=self.quarter, same_full_grid_squared_norm=True)

    def clear_base(self):
        self._base_x = self._base_p = self._base_first = None

    @staticmethod
    def _bdot(a, b):
        return np.einsum('bni,bni->bn', a, b)

    def raw_residual(self, x):
        """Unweighted physical (ss,sphi,phiphi) relative Gram components."""
        p = self.prepare(x)
        result = np.empty((self.P, self.N, 3), dtype=np.result_type(p.jets.dtype, float))
        with np.errstate(over='raise', invalid='raise', divide='raise'):
            for start in range(0, self.P, self.stage_block):
                stop = min(start+self.stage_block, self.P)
                V, d = self._first_batch(p, start, stop)
                ar = self.a[start:stop, None]*p.rho[None, :]
                result[start:stop, :, 0] = self._bdot(V, V)-1
                result[start:stop, :, 1] = self._bdot(V, d)/ar
                result[start:stop, :, 2] = self._bdot(d, d)/(ar*ar)-1
        return result

    def residual(self, x):
        result = self.raw_residual(x)
        if self.quarter:
            result *= self.sqrt_multiplicity[None, :, None]
        return result

    def unweight(self, values):
        """Remove only orbit weights, preserving the input's shape."""
        values = np.asarray(values)
        if values.size != self.P*self.N*3:
            raise ValueError('Expected all stage/angle/Gram rows')
        out = values.reshape((self.P, self.N, 3))/self.sqrt_multiplicity[None, :, None]
        return out.reshape(values.shape)

    def jvp(self, x, direction):
        p = self.prepare(x)
        djets, dH, dc = self.unpack(direction, tangent=True)
        drho = self.cos[:, 1:]@(self.qfreq*dc)
        dtheta = self.sin@((self.qfreq/self.freq)*dc)
        dtheta_et = dtheta[:, None]*p.et
        lift_d = drho[:, None]*p.et-(p.rho*dtheta)[:, None]*p.er
        result = np.empty((self.P, self.N, 3),
                          dtype=np.result_type(p.jets.dtype, djets.dtype, float))
        with np.errstate(over='raise', invalid='raise', divide='raise'):
            for start in range(0, self.P, self.stage_block):
                stop = min(start+self.stage_block, self.P)
                dy, du = self._stage_pair(djets, start, stop)
                dV, dd = self._linear_fields(dy, du)
                cp = self.lift_scalar[start:stop, 1]
                f = self.lift_scalar[start:stop, 3]
                fp = self.lift_scalar[start:stop, 4]
                dV += fp[:, None, None]*dtheta_et[None, :, :]
                dV[:, :, 2] += cp[:, None]*dH
                dd += f[:, None, None]*lift_d[None, :, :]
                V, d = self._first_batch(p, start, stop)
                a = self.a[start:stop, None]
                ar = a*p.rho[None, :]
                result[start:stop, :, 0] = 2*self._bdot(V, dV)
                result[start:stop, :, 1] = (
                    (self._bdot(d, dV)+self._bdot(V, dd))/ar
                    - self._bdot(V, d)*drho[None, :]/(a*p.rho[None, :]**2))
                result[start:stop, :, 2] = (
                    2*self._bdot(d, dd)/(ar*ar)
                    - 2*self._bdot(d, d)*drho[None, :]/(a*a*p.rho[None, :]**3))
        if self.quarter:
            result *= self.sqrt_multiplicity[None, :, None]
        return result

    def vjp(self, x, weights):
        p = self.prepare(x)
        weights = np.asarray(weights)
        if weights.size != self.P*self.N*3:
            raise ValueError('Adjoint needs every evaluated stage/angle/Gram value')
        weights = weights.reshape((self.P, self.N, 3))
        dtype = np.result_type(p.jets.dtype, weights.dtype, float)
        grad = np.zeros(p.jets.shape, dtype=dtype)
        theta_total = np.zeros(self.N, dtype=dtype)
        rho_total = np.zeros(self.N, dtype=dtype)
        gh = np.zeros((), dtype=dtype)
        with np.errstate(over='raise', invalid='raise', divide='raise'):
            for start in range(0, self.P, self.stage_block):
                stop = min(start+self.stage_block, self.P)
                V, d = self._first_batch(p, start, stop)
                w = weights[start:stop]
                if self.quarter:
                    w = w*self.sqrt_multiplicity[None, :, None]
                w0, w1, w2 = w[:, :, 0], w[:, :, 1], w[:, :, 2]
                a = self.a[start:stop, None]
                ar = a*p.rho[None, :]
                gV = 2*w0[:, :, None]*V+(w1/ar)[:, :, None]*d
                gd = (w1/ar)[:, :, None]*V+(2*w2/(ar*ar))[:, :, None]*d
                grho = (-w1*self._bdot(V, d)/(a*p.rho[None, :]**2)
                        - 2*w2*self._bdot(d, d)/(a*a*p.rho[None, :]**3))
                gy, gu = self._linear_fields_adjoint(gV, gd)
                self._stage_pair_adjoint(grad, start, stop, gy, gu)
                cp = self.lift_scalar[start:stop, 1]
                f = self.lift_scalar[start:stop, 3]
                fp = self.lift_scalar[start:stop, 4]
                theta_total += np.sum(
                    fp[:, None]*np.einsum('bni,ni->bn', gV, p.et)
                    - f[:, None]*p.rho[None, :]*np.einsum('bni,ni->bn', gd, p.er), axis=0)
                rho_total += np.sum(
                    f[:, None]*np.einsum('bni,ni->bn', gd, p.et)+grho, axis=0)
                gh += np.sum(cp[:, None]*gV[:, :, 2])
        gc = ((self.qfreq/self.freq)*(self.sin.T@theta_total)
              + self.qfreq*(self.cos[:, 1:].T@rho_total))
        grad[0, 0, 1:self.M+1] += gc
        return self._free_adjoint(grad, gh)

    def affine_diagnostics(self, x):
        result = super().affine_diagnostics(x)
        result.update(full_angular_residual_values=self.P*self.full_N*3,
                      evaluated_residual_values=self.P*self.N*3,
                      quarter_orbits=self.quarter,
                      full_grid_squared_norm_preserved=True)
        return result


def create(dense_source, *args, **kwargs):
    """Use the original ClosedGram class from a module or source path."""
    if hasattr(dense_source, 'ClosedGram'):
        dense = dense_source
    else:
        path = Path(dense_source).resolve()
        name = '_batched_closed_gram_base'
        spec = importlib.util.spec_from_file_location(name, path)
        dense = importlib.util.module_from_spec(spec)
        sys.modules[name] = dense
        spec.loader.exec_module(dense)
    class BatchedClosedGram(BatchedMixin, dense.ClosedGram):
        pass
    return BatchedClosedGram(*args, **kwargs)


if __name__ == '__main__':
    raise SystemExit('Import this module and pass the original ClosedGram source and actual fixed inputs.')
