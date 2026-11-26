#!/usr/bin/env python3
"""Complete fixed-g Cartesian streaming J/JT, restored after scratch loss.

This is a newly reconstructed text identity. It retains all 13 point rows,
the full proper-half-turn Cartesian space, physical s derivatives, and
exactly clamped endpoint two-jets. It does not construct a dense Jacobian
or a parameter normal matrix. Numerical samples are not certificates.
"""
from pathlib import Path
import importlib.util
import sys
import numpy as np
from scipy.interpolate import BSpline
from scipy import sparse
from scipy.linalg import cholesky_banded, solve_banded
from scipy.sparse.linalg import LinearOperator

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "complete_cartesian_point", HERE/"6a65-cartesian-complete-point-operator.py")
point = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = point
_spec.loader.exec_module(point)


def chunks(length, block):
    for start in range(0, length, block):
        yield slice(start, min(length, start+block))


class HalfTurnBasis:
    """Full real parity space for R_z(pi), with fixed endpoint two-jets."""
    def __init__(self, c, end, radial_count=80, max_frequency=32,
                 normalized_breaks=None):
        if not (np.isfinite(c) and np.isfinite(end) and 0 < c < end):
            raise ValueError("Finite physical correction interval required")
        if (type(radial_count) is not int or radial_count < 4 or
                type(max_frequency) is not int or max_frequency < 2):
            raise ValueError("Explicit radial count and angular frequency required")
        self.c, self.end, self.nb, self.M = float(c), float(end), radial_count, max_frequency
        if normalized_breaks is None:
            normalized = np.linspace(0., 1., radial_count+2)
        else:
            normalized = np.asarray(normalized_breaks, dtype=float)
            if (normalized.shape != (radial_count+2,) or normalized[0] != 0 or
                    normalized[-1] != 1 or not np.all(np.diff(normalized) > 0)):
                raise ValueError("Exactly J+2 increasing normalized breaks required")
        self.breaks = self.c+(self.end-self.c)*normalized
        self.breaks[0], self.breaks[-1] = self.c, self.end
        self.degree = 5
        self.knots = np.r_[np.repeat(self.c, 6), self.breaks[1:-1], np.repeat(self.end, 6)]
        self.full_count = len(self.knots)-6
        if self.full_count != self.nb+6:
            raise ArithmeticError("Unexpected clamped quintic dimension")
        self.channels = []
        for component in (0, 1):
            for k in range(1, self.M+1, 2):
                self.channels.extend(((component, k, "cos"), (component, k, "sin")))
        self.channels.append((2, 0, "cos"))
        for k in range(2, self.M+1, 2):
            self.channels.extend(((2, k, "cos"), (2, k, "sin")))
        self.na = len(self.channels)
        self.modes = np.array([k for _, k, _ in self.channels], dtype=int)
        self.dimension = self.nb*self.na
        self.definition = dict(
            schema="6a65-complete-proper-half-turn-clamped-quintic-basis-v1",
            radialBasisCount=self.nb, angularChannels=self.na,
            maxAngularFrequency=self.M, dimension=self.dimension,
            physicalDomain=[self.c, self.end], normalizedBreaks=normalized.tolist(),
            degree=5, fullRadialBasisCount=self.full_count,
            omittedEndpointColumns=[0, 1, 2, self.full_count-3, self.full_count-2, self.full_count-1],
            channelOrder=[dict(component=k, frequency=n, kind=t) for k, n, t in self.channels],
            reflectionRestriction=False, allSixEndpointJetsZero=True)
        self._spline = BSpline(self.knots, np.eye(self.full_count), 5, extrapolate=False)

    def matrices(self, nodes):
        nodes = np.asarray(nodes, dtype=float)
        if nodes.ndim != 1 or not np.all(np.isfinite(nodes)):
            raise ValueError("Finite physical radial sample vector required")
        valid = (nodes >= self.c) & (nodes <= self.end)
        result = []
        for derivative in range(3):
            values = np.zeros((len(nodes), self.nb))
            if np.any(valid):
                values[valid] = self._spline(nodes[valid], nu=derivative)[:, 3:-3]
            # These rows are mathematically exactly zero for the retained
            # clamped columns, including the order-two physical derivative.
            values[(nodes == self.c) | (nodes == self.end)] = 0.
            result.append(sparse.csr_matrix(values))
        return tuple(result)

    def angular(self, amplitude, N, derivative=0):
        amplitude = np.asarray(amplitude, dtype=float)
        if amplitude.ndim != 2 or amplitude.shape[1] != self.na:
            raise ValueError("Complete independent Cartesian angular amplitudes required")
        if type(N) is not int or N % 2 or N <= 2*self.M:
            raise ValueError("Even full-angle grid strictly above Nyquist required")
        if type(derivative) is not int or not 0 <= derivative <= 2:
            raise ValueError("Angular derivative order must be 0, 1, or 2")
        spectrum = np.zeros((len(amplitude), 3, N//2+1), dtype=complex)
        for column, (component, k, kind) in enumerate(self.channels):
            factor = (1j*k)**derivative
            if k == 0:
                spectrum[:, component, 0] += N*amplitude[:, column]*factor
            else:
                factor *= N/2 if kind == "cos" else -1j*N/2
                spectrum[:, component, k] += amplitude[:, column]*factor
        return np.fft.irfft(spectrum, n=N, axis=-1).transpose(0, 2, 1)

    def angular_adjoint(self, values, derivative=0):
        values = np.asarray(values, dtype=float)
        if values.ndim != 3 or values.shape[-1] != 3:
            raise ValueError("Full-angle Cartesian cotangent required")
        N = values.shape[1]
        if N % 2 or N <= 2*self.M:
            raise ValueError("Even full-angle cotangent grid strictly above Nyquist required")
        if type(derivative) is not int or not 0 <= derivative <= 2:
            raise ValueError("Angular derivative order must be 0, 1, or 2")
        spectrum = np.fft.rfft(values.transpose(0, 2, 1), axis=-1)
        out = np.empty((len(values), self.na))
        for column, (component, k, kind) in enumerate(self.channels):
            value = (-1j*k)**derivative*spectrum[:, component, k]
            out[:, column] = value.real if kind == "cos" else -value.imag
        return out

    def packet(self, matrices, coefficients, N):
        coefficients = np.asarray(coefficients, dtype=float)
        if coefficients.shape != (self.nb, self.na):
            raise ValueError("Full Cartesian coefficient matrix required")
        a0, a1, a2 = (b@coefficients for b in matrices)
        return np.stack((self.angular(a0, N), self.angular(a1, N),
                         self.angular(a0, N, 1), self.angular(a2, N),
                         self.angular(a1, N, 1), self.angular(a0, N, 2)), axis=1)

    def packet_adjoint(self, matrices, values):
        values = np.asarray(values, dtype=float)
        if values.ndim != 4 or values.shape[1] != 6 or values.shape[-1] != 3:
            raise ValueError("Full six-jet Cartesian cotangent required")
        q0 = self.angular_adjoint(values[:, 0])+self.angular_adjoint(values[:, 2], 1)+self.angular_adjoint(values[:, 5], 2)
        q1 = self.angular_adjoint(values[:, 1])+self.angular_adjoint(values[:, 4], 1)
        q2 = self.angular_adjoint(values[:, 3])
        return matrices[0].T@q0+matrices[1].T@q1+matrices[2].T@q2


class BandedSobolev:
    """Positive banded H2-based change of coordinates; no rows are removed."""
    def __init__(self, basis, nodes, weights, config=None):
        config = {} if config is None else dict(config)
        if config.get("kind", "banded_sobolev_h2") != "banded_sobolev_h2":
            raise ValueError("Explicit banded Sobolev preconditioner required")
        self.basis = basis
        beta0, beta1, beta2 = (float(config.get(k, d)) for k, d in
                              (("beta0", .01), ("beta1", 1.), ("beta2", .001)))
        if not all(np.isfinite(x) and x > 0 for x in (beta0, beta1, beta2)):
            raise ValueError("Positive finite Sobolev coefficients required")
        weights = np.asarray(weights, dtype=float)
        if weights.shape != np.asarray(nodes).shape or np.any(weights < 0) or not np.all(np.isfinite(weights)):
            raise ValueError("Explicit nonnegative physical radial Sobolev weights required")
        b0, b1, b2 = basis.matrices(nodes)
        M, K1, K2 = ((b.T@b.multiply(weights[:, None])).toarray() for b in (b0, b1, b2))
        self.bandwidth = 5
        self.factors = {}
        rows, cols = np.indices(M.shape)
        exterior = abs(rows-cols) > self.bandwidth
        if any(np.any(a[exterior] != 0) for a in (M, K1, K2)):
            raise ArithmeticError("Nonzero matrix entries outside the exact quintic bandwidth")
        for k in np.unique(basis.modes):
            matrix = beta1*K1+(beta0+beta1*k*k)*M+beta2*(K2+2*k*k*K1+k**4*M)
            band = np.zeros((6, basis.nb))
            for offset in range(6):
                band[offset, :basis.nb-offset] = np.diag(matrix, k=-offset)
            lower = cholesky_banded(band, lower=True, check_finite=True)
            upper = np.zeros_like(lower)
            for offset in range(6):
                upper[5-offset, offset:] = lower[offset, :basis.nb-offset]
            self.factors[int(k)] = (lower, upper, np.flatnonzero(basis.modes == k))
        self.definition = dict(kind="banded_sobolev_h2", beta0=beta0, beta1=beta1,
                               beta2=beta2, bandwidth=5, denseInverseConstructed=False)

    def unpack(self, vector):
        vector = np.asarray(vector, dtype=float).reshape(self.basis.nb, self.basis.na)
        out = np.empty_like(vector)
        for lower, upper, columns in self.factors.values():
            out[:, columns] = solve_banded((0, 5), upper, vector[:, columns], check_finite=False)
        return out

    def transpose(self, gradient):
        gradient = np.asarray(gradient, dtype=float).reshape(self.basis.nb, self.basis.na)
        out = np.empty_like(gradient)
        for lower, upper, columns in self.factors.values():
            out[:, columns] = solve_banded((5, 0), lower, gradient[:, columns], check_finite=False)
        return out.ravel()


def _validate_grid(basis, nodes, weights, coefficients, N, block):
    nodes = np.asarray(nodes, dtype=float)
    coefficients = np.asarray(coefficients, dtype=float)
    if nodes.ndim != 1 or len(nodes) == 0 or not np.all(np.isfinite(nodes)):
        raise ValueError("Finite complete physical sample vector required")
    if coefficients.shape != (basis.nb, basis.na) or not np.all(np.isfinite(coefficients)):
        raise ValueError("Finite complete Cartesian coefficient matrix required")
    if type(N) is not int or N % 2 or N <= 2*basis.M:
        raise ValueError("Even full-angle grid strictly above Nyquist required")
    if type(block) is not int or block < 1:
        raise ValueError("Positive radial block size required")
    if set(weights) != {"metric", "curvature", "geometry"}:
        raise ValueError("All three complete residual weight vectors required")
    result = {}
    for key, value in weights.items():
        value = np.asarray(value, dtype=float)
        if value.shape != nodes.shape or np.any(value < 0) or not np.all(np.isfinite(value)):
            raise ValueError("Finite nonnegative complete physical weights required")
        result[key] = value
    return nodes, result, coefficients


def _point_block(basis, matrices, nodes, weights, background, coefficients, N, config):
    jets, radius = background(nodes, N)
    jets, radius = np.asarray(jets, dtype=float), np.asarray(radius, dtype=float)
    if jets.shape != (len(nodes), 6, N, 3) or radius.shape != (len(nodes), N):
        raise ValueError("Actual background requires full six-jets and target radius at every angle")
    packet = jets+basis.packet(matrices, coefficients, N)
    return point.PointLinearized(packet.swapaxes(1, 2), radius, config,
                                 {key: value[:, None]/N for key, value in weights.items()})


def _block_statistics(linear, nodes, N):
    out = linear.statistics()
    e, sf, g = (linear.metric[..., j] for j in range(3))
    relative = np.abs((e+g)/2)+np.hypot((e-g)/2, sf/np.sqrt(2.))
    ri, ui = np.unravel_index(int(np.argmax(relative)), relative.shape)
    out["worstMetric"] = dict(s=float(nodes[ri]), u=float(2*np.pi*ui/N),
                              relative=float(relative[ri, ui]), e=float(e[ri, ui]),
                              f=float(sf[ri, ui]/np.sqrt(2.)), g=float(g[ri, ui]))
    absolute = np.max(np.abs(linear.curvature["eigenvalues"]), axis=-1)
    ri, ui = np.unravel_index(int(np.argmax(absolute)), absolute.shape)
    out["worstCurvature"] = dict(s=float(nodes[ri]), u=float(2*np.pi*ui/N),
                                 absolute=float(absolute[ri, ui]),
                                 eigenvalues=linear.curvature["eigenvalues"][ri, ui].tolist())
    return out


def _merge_statistics(total, part):
    if total is None:
        return part
    for key in ("pointCount", "rowCount", "squaredNorm", "curvatureThresholdPoints"):
        total[key] += part[key]
    for key in ("metric", "curvature", "geometry"):
        total["groupSquaredNorm"][key] += part["groupSquaredNorm"][key]
    for key, witness in (("maxRelativeMetric", "worstMetric"), ("maxCurvature", "worstCurvature")):
        if part[key] > total[key]:
            total[key], total[witness] = part[key], part[witness]
    for key in ("maxRadius", "maxAbsoluteY", "maxAdjustedHeightExcess"):
        total[key] = max(total[key], part[key])
    for key in ("minImmersion", "minHeldDistance"):
        total[key] = min(total[key], part[key])
    for key in point.GEOMETRY_ROWS:
        total["geometryMaximumViolations"][key] = max(
            total["geometryMaximumViolations"][key], part["geometryMaximumViolations"][key])
    return total


def observe(basis, nodes, weights, background, coefficients, N, point_config, block=16):
    nodes, weights, coefficients = _validate_grid(basis, nodes, weights, coefficients, N, block)
    matrices = basis.matrices(nodes)
    total = None
    for sl in chunks(len(nodes), block):
        linear = _point_block(basis, tuple(b[sl] for b in matrices), nodes[sl],
                              {k: v[sl] for k, v in weights.items()}, background,
                              coefficients, N, point_config)
        total = _merge_statistics(total, _block_statistics(linear, nodes[sl], N))
    return total


class CompleteStreamingLinearized:
    """Complete matrix-free Gauss--Newton rows in preconditioned coordinates."""
    def __init__(self, basis, nodes, weights, background, coefficients, N,
                 point_config, block=16, preconditioner=None, sobolev_weights=None,
                 cache_point_blocks=False):
        self.basis, self.N, self.config, self.block = basis, N, point_config, block
        self.nodes, self.weights, self.coefficients = _validate_grid(
            basis, nodes, weights, coefficients, N, block)
        self.background = background
        self.matrices = basis.matrices(self.nodes)
        self.slices = list(chunks(len(self.nodes), block))
        self.cache_point_blocks = bool(cache_point_blocks)
        self.point_blocks = []
        residual = np.empty((len(self.nodes), N, 13))
        self.statistics = None
        for sl in self.slices:
            value = self._build_block(sl)
            residual[sl] = value.residual
            self.statistics = _merge_statistics(self.statistics, _block_statistics(value, self.nodes[sl], N))
            if self.cache_point_blocks:
                self.point_blocks.append(value)
        self.residual = residual.ravel()
        self.shape = (self.residual.size, basis.dimension)
        if sobolev_weights is None:
            sobolev_weights = self.weights["metric"]
        self.preconditioner = BandedSobolev(basis, self.nodes, sobolev_weights, preconditioner)
        self.operator = LinearOperator(self.shape, matvec=self.matvec,
                                       rmatvec=self.rmatvec, dtype=np.float64)

    def _build_block(self, sl):
        return _point_block(self.basis, tuple(b[sl] for b in self.matrices), self.nodes[sl],
                            {k: v[sl] for k, v in self.weights.items()}, self.background,
                            self.coefficients, self.N, self.config)

    def _get_block(self, index, sl):
        return self.point_blocks[index] if self.cache_point_blocks else self._build_block(sl)

    def unpack(self, vector):
        vector = np.asarray(vector, dtype=float)
        if vector.size != self.shape[1] or not np.all(np.isfinite(vector)):
            raise ValueError("Finite complete parameter direction required")
        return self.preconditioner.unpack(vector)

    def matvec(self, vector):
        direction = self.unpack(vector)
        output = np.empty((len(self.nodes), self.N, 13))
        for index, sl in enumerate(self.slices):
            packet = self.basis.packet(tuple(b[sl] for b in self.matrices), direction, self.N)
            output[sl] = self._get_block(index, sl).jvp(packet.swapaxes(1, 2))
        return output.ravel()

    def rmatvec(self, vector):
        vector = np.asarray(vector, dtype=float)
        if vector.size != self.shape[0] or not np.all(np.isfinite(vector)):
            raise ValueError("Finite complete residual cotangent required")
        cotangent = vector.reshape(len(self.nodes), self.N, 13)
        gradient = np.zeros((self.basis.nb, self.basis.na))
        for index, sl in enumerate(self.slices):
            packet = self._get_block(index, sl).vjp(cotangent[sl]).swapaxes(1, 2)
            gradient += self.basis.packet_adjoint(tuple(b[sl] for b in self.matrices), packet)
        return self.preconditioner.transpose(gradient)
