#!/usr/bin/env python3
"""All-channel physical radial normal bands, preserving the original LM.

Every complete point row and every Cartesian angular cross term is retained.
Discrete angular products use exact signed rFFT moments, including aliases.
Only the invertible right preconditioner changes. The physical LM quadratic
remains ||J d+r||^2 + lambda ||L_S^T d||^2 with the original Sobolev factor.
"""
import math
import time
import numpy as np
from scipy.linalg import cholesky_banded
from scipy.linalg.blas import dtbsv
from scipy.sparse.linalg import LinearOperator


def lower_product_band(lower):
    width, n = lower.shape[0]-1, lower.shape[1]
    out = np.zeros_like(lower)
    for d in range(width+1):
        for t in range(width-d+1):
            if t < n-d:
                out[d, t:n-d] += lower[d+t, :n-d-t]*lower[t, :n-d-t]
    return out


def triangular_apply(lower, value, transpose=False):
    value = np.asarray(value, dtype=float)
    if value.ndim != 2 or value.shape[0] != lower.shape[1]:
        raise ValueError("Matching radial-by-channel matrix required")
    out = np.zeros_like(value)
    n = len(value)
    for d in range(lower.shape[0]):
        if transpose:
            out[:n-d] += lower[d, :n-d, None]*value[d:]
        else:
            out[d:] += lower[d, :n-d, None]*value[:n-d]
    return out


def channel_terms(channels):
    """p(u)=sum_j coefficient[j] exp(i frequency[j] u), exactly two slots."""
    count = len(channels)
    frequency = np.zeros((2, count), dtype=int)
    coefficient = np.zeros((2, count), dtype=complex)
    for j, (_, k, kind) in enumerate(channels):
        if k == 0:
            if kind != "cos":
                raise ValueError("Only the actual constant cosine channel is valid")
            coefficient[0, j] = 1.
        elif k > 0 and kind in ("cos", "sin"):
            frequency[:, j] = k, -k
            coefficient[:, j] = (.5, .5) if kind == "cos" else (-.5j, .5j)
        else:
            raise ValueError("Declared real sine/cosine Cartesian channels required")
    return frequency, coefficient


def positive_exponential_moment(spectrum, frequency, N):
    """Sum_u C(u) exp(+i frequency*u) from the full discrete rFFT of C."""
    wrapped = np.mod(frequency, N)
    index = np.minimum(wrapped, N-wrapped)
    values = spectrum[:, index]
    # rFFT uses the negative exponential. For the positive half use its
    # conjugate; a wrapped negative/aliased frequency uses the saved half.
    return np.where((wrapped <= N//2)[None, ..., None, None],
                    values.conj(), values)


class CompleteRadialNormal:
    """Full J^T J in radial-major scalar band form, no cross-channel dropping."""
    def __init__(self, linear, eta=.1):
        started = time.monotonic()
        eta = float(eta)
        if not math.isfinite(eta) or eta <= 0:
            raise ValueError("Explicit finite positive preconditioner regularization required")
        self.linear, self.basis, self.eta = linear, linear.basis, eta
        basis, N = self.basis, linear.N
        nc, nb = basis.na, basis.nb
        if (linear.shape != (len(linear.nodes)*N*13, basis.dimension)
            or basis.dimension != nb*nc or basis.degree != 5
            or linear.preconditioner.bandwidth != 5 or N % 2 or N <= 2*basis.M):
            raise ValueError("Unchanged complete 13-row quintic Cartesian layout required")
        self.half_bandwidth = min(6*nc-1, basis.dimension-1)
        self.normal_band = np.zeros((self.half_bandwidth+1, basis.dimension))
        self.old_groups = []
        coverage = np.zeros(nc, dtype=int)
        for lower, _, columns in linear.preconditioner.factors.values():
            lower, columns = lower.copy(), columns.copy()
            self.old_groups.append((lower, columns))
            coverage[columns] += 1
        if np.any(coverage != 1):
            raise ValueError("Every original Sobolev channel must occur exactly once")
        frequency, coefficient = channel_terms(basis.channels)
        components = np.array([c for c, _, _ in basis.channels], dtype=int)
        Amatrix = np.zeros((nc, 3, 6))
        Amatrix[:, 0, 0] = 1.
        Amatrix[:, 0, 5] = -np.array([k*k for _, k, _ in basis.channels])
        Amatrix[:, 1, 1] = 1.
        Amatrix[:, 2, 3] = 1.
        Cmatrix = np.zeros((3, 6))
        Cmatrix[0, 2] = Cmatrix[1, 4] = 1.
        timings = dict(pointCovarianceSeconds=0., angularContractionSeconds=0.,
                       radialAccumulationSeconds=0., equilibrationSeconds=0.,
                       bandCholeskySeconds=0.)
        largest_temporary = covariance_points = skipped_points = vjp_calls = 0
        maximum_imaginary = maximum_moment_real = maximum_q_asymmetry = 0.
        alias_frequency_pairs = 0
        triangle_cache = {}
        for block_index, sl in enumerate(linear.slices):
            B = np.stack([b[sl].toarray() for b in linear.matrices])
            live = np.any(B != 0., axis=0)
            for row in live:
                active = np.flatnonzero(row)
                if len(active) and (len(active) > 6 or np.any(np.diff(active) != 1)):
                    raise ValueError("Contiguous quintic radial support of size at most six required")
            if not np.any(live):
                skipped_points += B.shape[1]*N
                continue
            part = linear._get_block(block_index, sl)
            if part.residual.shape != (B.shape[1], N, 13):
                raise ValueError("Every original point residual row is required")
            t0 = time.monotonic()
            # Full (Cartesian component, jet) covariance, including xy/xz/yz.
            gram = np.zeros((B.shape[1], N, 3, 3, 6, 6))
            cotangent = np.zeros_like(part.residual)
            for row in range(13):
                cotangent[..., row] = 1.
                derivative = part.vjp(cotangent)
                gram += np.einsum("suic,sujd->sucdij", derivative, derivative,
                                  optimize=True)
                cotangent[..., row] = 0.
            spectrum = np.fft.rfft(gram, axis=1)
            largest_temporary = max(largest_temporary, gram.nbytes+spectrum.nbytes+
                                    cotangent.nbytes+derivative.nbytes+B.nbytes)
            del gram, cotangent, derivative
            timings["pointCovarianceSeconds"] += time.monotonic()-t0
            covariance_points += B.shape[1]*N
            vjp_calls += 13
            t0 = time.monotonic()
            Q = np.empty((B.shape[1], nc, nc, 3, 3))
            for ca in range(3):
                ia = np.flatnonzero(components == ca)
                for cb in range(3):
                    ib = np.flatnonzero(components == cb)
                    if not len(ia) or not len(ib):
                        continue
                    moments = [np.zeros((B.shape[1], len(ia), len(ib), 6, 6), complex)
                               for _ in range(4)]
                    for left_sign in range(2):
                        fa = frequency[left_sign, ia][:, None]
                        za = coefficient[left_sign, ia][:, None]
                        for right_sign in range(2):
                            fb = frequency[right_sign, ib][None, :]
                            zb = coefficient[right_sign, ib][None, :]
                            weight = za*zb
                            if not np.any(weight):
                                continue
                            freq = fa+fb
                            alias_frequency_pairs += int(np.count_nonzero(
                                (np.abs(freq) > N//2) & (weight != 0)))
                            F = positive_exponential_moment(spectrum[:, :, ca, cb], freq, N)
                            factors = (weight, weight*(1j*fb), weight*(1j*fa), -weight*fa*fb)
                            for moment, factor in zip(moments, factors):
                                moment += F*factor[None, ..., None, None]
                            largest_temporary = max(largest_temporary,
                                spectrum.nbytes+Q.nbytes+B.nbytes+F.nbytes+
                                sum(value.nbytes for value in moments))
                            del F
                    for moment in moments:
                        maximum_imaginary = max(maximum_imaginary,
                                                float(np.max(np.abs(moment.imag))))
                        maximum_moment_real = max(maximum_moment_real,
                                                  float(np.max(np.abs(moment.real))))
                    aa, ab = Amatrix[ia], Amatrix[ib]
                    q = (np.einsum("mdi,smnij,nej->smnde", aa, moments[0].real, ab, optimize=True)+
                         np.einsum("mdi,smnij,ej->smnde", aa, moments[1].real, Cmatrix, optimize=True)+
                         np.einsum("di,smnij,nej->smnde", Cmatrix, moments[2].real, ab, optimize=True)+
                         np.einsum("di,smnij,ej->smnde", Cmatrix, moments[3].real, Cmatrix, optimize=True))
                    Q[:, ia[:, None], ib[None, :], :, :] = q
                    del moments, q
            transpose = Q.transpose(0, 2, 1, 4, 3)
            maximum_q_asymmetry = max(maximum_q_asymmetry,
                                      float(np.max(np.abs(Q-transpose))))
            Q = .5*(Q+transpose)
            del transpose, spectrum
            timings["angularContractionSeconds"] += time.monotonic()-t0
            t0 = time.monotonic()
            for row, mask in enumerate(live):
                active = np.flatnonzero(mask)
                if not len(active):
                    continue
                width = len(active)*nc
                if width not in triangle_cache:
                    rr, cc = np.tril_indices(width)
                    triangle_cache[width] = rr, cc, rr-cc
                rr, cc, distance = triangle_cache[width]
                weights = B[:, row, active]
                local = np.einsum("di,mnde,ej->imjn", weights, Q[row], weights,
                                  optimize=True).reshape(width, width)
                columns = int(active[0])*nc+cc
                # Each (distance, column) pair is unique within this point.
                self.normal_band[distance, columns] += local[rr, cc]
                largest_temporary = max(largest_temporary,
                    Q.nbytes+B.nbytes+local.nbytes+rr.nbytes+cc.nbytes+
                    distance.nbytes+columns.nbytes)
            timings["radialAccumulationSeconds"] += time.monotonic()-t0
        if not np.all(np.isfinite(self.normal_band)):
            raise ArithmeticError("Nonfinite complete physical normal band")
        t0 = time.monotonic()
        packed = np.array(self.normal_band, order="F")
        for lower, channels in self.old_groups:
            old_band = lower_product_band(lower)
            for offset in range(6):
                count = nb-offset
                columns = (np.arange(count)[:, None]*nc+channels[None, :]).ravel()
                packed[offset*nc, columns] += eta*np.broadcast_to(
                    old_band[offset, :count, None], (count, len(channels))).ravel()
        diagonal = packed[0].copy()
        if np.any(diagonal <= 0) or not np.all(np.isfinite(diagonal)):
            raise ArithmeticError("Positive complete physical preconditioner diagonal required")
        self.diagonal_scale = 1/np.sqrt(diagonal)
        for offset in range(self.half_bandwidth+1):
            count = basis.dimension-offset
            packed[offset, :count] *= self.diagonal_scale[offset:]*self.diagonal_scale[:count]
        timings["equilibrationSeconds"] = time.monotonic()-t0
        t0 = time.monotonic()
        self.factor = np.asfortranarray(cholesky_banded(
            packed, lower=True, overwrite_ab=True, check_finite=True))
        timings["bandCholeskySeconds"] = time.monotonic()-t0
        self.receipt = dict(
            schema="6a65-complete-all-angular-physical-normal-band-assembly-v1",
            columns=basis.dimension, physicalRows=linear.shape[0], radialBlocks=nb,
            angularChannels=nc, radialBlockHalfBandwidth=5,
            scalarHalfBandwidth=self.half_bandwidth, eta=eta,
            completeNormalBandBytes=self.normal_band.nbytes,
            bandFactorBytes=self.factor.nbytes, completeJacobianFormed=False,
            completeDenseNormalMatrixFormed=False,
            fullPhysicalNormalAssembledWithoutCrossChannelDropping=True,
            everyCartesianCrossComponentCovarianceRetained=True,
            allThirteenRowsInPointCovariance=True, localCompleteVJPCalls=vjp_calls,
            assembledPoints=covariance_points, structurallyZeroPreconditionerPoints=skipped_points,
            zeroPointRowsStillRetainedInFullOperator=True,
            discreteAngularMomentsWithoutModeTruncation=True,
            conjugateAliasFrequencyPairsUsed=alias_frequency_pairs,
            maximumImaginaryMomentRoundoff=maximum_imaginary,
            relativeImaginaryMomentRoundoff=maximum_imaginary/max(1., maximum_moment_real),
            maximumQAntisymmetryBeforeRoundoffSymmetrization=maximum_q_asymmetry,
            diagonalEquilibrationChangesPhysicalPreconditioner=False,
            diagonalScaleMinimum=float(np.min(self.diagonal_scale)),
            diagonalScaleMaximum=float(np.max(self.diagonal_scale)),
            triangularSolves="BLAS dtbsv on the saved lower band factor",
            largestExplicitAssemblyTemporaryBytes=largest_temporary,
            temporaryBytesAreNotProcessRSS=True, timings=timings,
            seconds=time.monotonic()-started)

    def unpack(self, vector):
        vector = np.asarray(vector, dtype=float)
        if vector.size != self.basis.dimension:
            raise ValueError("Every actual Cartesian coefficient coordinate required")
        value = dtbsv(self.half_bandwidth, self.factor, vector.ravel(), lower=1, trans=1)
        return (self.diagonal_scale*value).reshape(self.basis.nb, self.basis.na)

    def transpose(self, gradient):
        gradient = np.asarray(gradient, dtype=float)
        if gradient.size != self.basis.dimension:
            raise ValueError("Every actual physical gradient coordinate required")
        return dtbsv(self.half_bandwidth, self.factor,
                     self.diagonal_scale*gradient.ravel(), lower=1, trans=0)

    def old_factor(self, coefficients, transpose=False):
        x = np.asarray(coefficients, dtype=float).reshape(self.basis.nb, self.basis.na)
        out = np.empty_like(x)
        for lower, columns in self.old_groups:
            out[:, columns] = triangular_apply(lower, x[:, columns], transpose)
        return out


class SameSobolevFullBandAugmented:
    """[J T; sqrt(lambda) L_S^T T], full-band T and the OLD physical S."""
    def __init__(self, linear, damping, eta=.1):
        self.linear, self.damping = linear, float(damping)
        if not math.isfinite(self.damping) or self.damping <= 0:
            raise ValueError("Actual positive original LM lambda required")
        self.blocks = CompleteRadialNormal(linear, eta)
        self.root_damping = math.sqrt(self.damping)
        self.shape = (linear.shape[0]+linear.shape[1], linear.shape[1])
        self.operator = LinearOperator(self.shape, matvec=self.matvec,
                                       rmatvec=self.rmatvec, dtype=np.float64)
        self.rhs = np.r_[-linear.residual, np.zeros(linear.shape[1])]
        self.receipt = dict(schema="6a65-same-Sobolev-full-band-preconditioned-LM-v1",
            physicalRows=linear.shape[0], explicitRegularizerRows=linear.shape[1],
            columns=linear.shape[1], damping=self.damping, requiredLSMRDamp=0.,
            oldSobolevQuadraticPreserved=True,
            allPhysicalRowsAndCrossChannelCouplingsRetained=True,
            completeTargetOrBasisChanged=False, assembly=self.blocks.receipt)

    def raw_matvec(self, coefficients):
        linear = self.linear
        x = np.asarray(coefficients, dtype=float).reshape(linear.basis.nb, linear.basis.na)
        out = np.empty((len(linear.nodes), linear.N, 13))
        for index, sl in enumerate(linear.slices):
            packet = linear.basis.packet(tuple(b[sl] for b in linear.matrices), x, linear.N)
            out[sl] = linear._get_block(index, sl).jvp(packet.swapaxes(1, 2))
        return out.ravel()

    def raw_transpose(self, vector):
        linear = self.linear
        q = np.asarray(vector, dtype=float).reshape(len(linear.nodes), linear.N, 13)
        out = np.zeros((linear.basis.nb, linear.basis.na))
        for index, sl in enumerate(linear.slices):
            packet = linear._get_block(index, sl).vjp(q[sl]).swapaxes(1, 2)
            out += linear.basis.packet_adjoint(tuple(b[sl] for b in linear.matrices), packet)
        return out

    def unpack(self, vector):
        return self.blocks.unpack(vector)

    def matvec(self, vector):
        direction = self.unpack(vector)
        return np.r_[self.raw_matvec(direction),
                     self.root_damping*self.blocks.old_factor(direction, True).ravel()]

    def rmatvec(self, vector):
        vector = np.asarray(vector, dtype=float)
        if vector.shape != (self.shape[0],):
            raise ValueError("All physical and original regularizer cotangent rows required")
        size = self.linear.shape[0]
        gradient = self.raw_transpose(vector[:size])
        gradient += self.root_damping*self.blocks.old_factor(vector[size:], False)
        return self.blocks.transpose(gradient)

    def physical_normal_residual(self, direction):
        x = np.asarray(direction, dtype=float).reshape(self.linear.basis.nb, self.linear.basis.na)
        result = self.raw_transpose(self.raw_matvec(x)+self.linear.residual)
        result += self.damping*self.blocks.old_factor(self.blocks.old_factor(x, True), False)
        return result.ravel()
