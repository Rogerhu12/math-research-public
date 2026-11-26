#!/usr/bin/env python3
"""Exact angular-channel radial GN blocks for the complete 13-row target.

This independent solver helper does not alter the frozen stream or point
operator.  Its augmented operator preserves the OLD Sobolev LM quadratic,
including every physical row, column, and inter-channel coupling.  Only the
right preconditioner uses angular-channel principal blocks.  No complete
Jacobian or complete normal matrix is formed here.
"""
import math
import time
import numpy as np
from scipy.linalg import cholesky_banded, solve_banded
from scipy.sparse.linalg import LinearOperator


def lower_product_band(lower):
    """Packed lower band of L L^T, from the actual old Cholesky factor."""
    lower = np.asarray(lower, dtype=float)
    width, n = lower.shape[0]-1, lower.shape[1]
    out = np.zeros_like(lower)
    for d in range(width+1):
        for t in range(width-d+1):
            if t < n-d:
                out[d, t:n-d] += lower[d+t, :n-d-t]*lower[t, :n-d-t]
    return out


def triangular_apply(lower, value, transpose=False):
    """Multiply by the saved lower triangular band (or its transpose)."""
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


class ExactChannelBlocks:
    """Actual J_m^T J_m + eta S_m, retaining exact quintic bandwidth five."""
    def __init__(self, linear, eta=1e-3):
        started = time.monotonic()
        eta = float(eta)
        if not math.isfinite(eta) or eta <= 0:
            raise ValueError("Explicit finite positive block regularization required")
        self.linear, self.basis, self.eta = linear, linear.basis, eta
        basis, N = self.basis, linear.N
        if (linear.shape != (len(linear.nodes)*N*13, basis.dimension) or
                basis.dimension != basis.nb*basis.na or basis.degree != 5 or
                linear.preconditioner.bandwidth != 5):
            raise ValueError("Unchanged complete 13-row clamped-quintic layout required")
        self.old_groups = []
        self.old_bands = np.empty((basis.na, 6, basis.nb))
        for lower, _, columns in linear.preconditioner.factors.values():
            lower, columns = lower.copy(), columns.copy()
            self.old_groups.append((lower, columns))
            self.old_bands[columns] = lower_product_band(lower)
        self.normal_blocks = np.zeros_like(self.old_bands)
        timings = dict(pointCovarianceSeconds=0., angularContractionSeconds=0.,
                       radialAccumulationSeconds=0., bandCholeskySeconds=0.)
        largest_temporary = 0
        skipped_zero_points, covariance_points, local_vjp_calls = 0, 0, 0
        maximum_q_asymmetry = 0.
        for block_index, sl in enumerate(linear.slices):
            B = np.stack([b[sl].toarray() for b in linear.matrices])
            live = np.any(B != 0., axis=0)
            for row in live:
                active = np.flatnonzero(row)
                if len(active) and (len(active) > 6 or active[-1]-active[0] > 5):
                    raise ValueError("Actual basis has nonlocal or oversized radial support")
            if not np.any(live):
                skipped_zero_points += B.shape[1]*N
                continue
            part = linear._get_block(block_index, sl)
            if part.residual.shape != (B.shape[1], N, 13):
                raise ValueError("All original point residual rows required")
            t0 = time.monotonic()
            # Sum the outer products of the thirteen complete point rows.
            # The covariance is local (18 physical jet entries), not global J.
            gram = np.zeros((B.shape[1], N, 3, 6, 6))
            cotangent = np.zeros_like(part.residual)
            for row in range(13):
                cotangent[..., row] = 1.
                derivative = part.vjp(cotangent)
                gram += np.einsum("suic,sujc->sucij", derivative, derivative,
                                  optimize=True)
                cotangent[..., row] = 0.
            spectrum = np.fft.rfft(gram, axis=1)
            largest_temporary = max(largest_temporary,
                                    gram.nbytes+spectrum.nbytes+cotangent.nbytes+
                                    derivative.nbytes+B.nbytes)
            del gram, cotangent, derivative
            timings["pointCovarianceSeconds"] += time.monotonic()-t0
            covariance_points += B.shape[1]*N
            local_vjp_calls += 13
            t0 = time.monotonic()
            Q = np.empty((basis.na, B.shape[1], 3, 3))
            for channel, (component, k, kind) in enumerate(basis.channels):
                zero = spectrum[:, 0, component].real
                if k:
                    frequency = 2*k
                    # N > 2M still permits 2k above the rFFT half-grid.
                    # Use its exact discrete conjugate alias, not truncation.
                    moment = (spectrum[:, frequency, component] if frequency <= N//2
                              else spectrum[:, N-frequency, component].conj())
                    sign = 1. if kind == "cos" else -1.
                    pp = .5*(zero+sign*moment.real)
                    pdp = .5*sign*k*moment.imag
                    dpdp = .5*k*k*(zero-sign*moment.real)
                else:
                    if kind != "cos":
                        raise ValueError("Only the actual constant cosine channel is valid")
                    pp, pdp, dpdp = zero, np.zeros_like(zero), np.zeros_like(zero)
                A, C = np.zeros((3, 6)), np.zeros((3, 6))
                A[0, 0], A[0, 5], A[1, 1], A[2, 3] = 1., -k*k, 1., 1.
                C[0, 2], C[1, 4] = 1., 1.
                q = (np.einsum("di,sij,ej->sde", A, pp, A, optimize=True)+
                     np.einsum("di,sij,ej->sde", A, pdp, C, optimize=True)+
                     np.einsum("di,sij,ej->sde", C, pdp, A, optimize=True)+
                     np.einsum("di,sij,ej->sde", C, dpdp, C, optimize=True))
                maximum_q_asymmetry = max(maximum_q_asymmetry,
                                          float(np.max(np.abs(q-q.swapaxes(1, 2)))))
                Q[channel] = .5*(q+q.swapaxes(1, 2))
            del spectrum
            timings["angularContractionSeconds"] += time.monotonic()-t0
            t0 = time.monotonic()
            for offset in range(6):
                end = basis.nb-offset
                self.normal_blocks[:, offset, :end] += np.einsum(
                    "asj,msab,bsj->mj", B[:, :, offset:], Q, B[:, :, :end],
                    optimize=True)
            timings["radialAccumulationSeconds"] += time.monotonic()-t0
        if not np.all(np.isfinite(self.normal_blocks)):
            raise ValueError("Nonfinite actual normal principal block")
        self.factors = []
        t0 = time.monotonic()
        for channel in range(basis.na):
            packed = self.normal_blocks[channel]+eta*self.old_bands[channel]
            lower = cholesky_banded(packed, lower=True, check_finite=True)
            upper = np.zeros_like(lower)
            for d in range(6):
                upper[5-d, d:] = lower[d, :basis.nb-d]
            self.factors.append((lower, upper))
        timings["bandCholeskySeconds"] = time.monotonic()-t0
        self.receipt = dict(
            schema="6a65-actual-complete-channel-principal-block-assembly-v1",
            columns=basis.dimension, physicalRows=linear.shape[0],
            radialBlocks=basis.nb, angularChannels=basis.na, radialHalfBandwidth=5,
            eta=eta, assembledPoints=covariance_points,
            structurallyZeroPreconditionerPoints=skipped_zero_points,
            zeroPointRowsStillRetainedInFullOperator=True,
            localCompleteVJPCalls=local_vjp_calls,
            allThirteenRowsInPointCovariance=True,
            completeJacobianFormed=False, completeNormalMatrixFormed=False,
            principalBandBytes=self.normal_blocks.nbytes,
            largestExplicitCovarianceTemporaryBytes=largest_temporary,
            temporaryBytesAreNotProcessRSS=True,
            maximumLocalQAntisymmetryBeforeRoundoffSymmetrization=maximum_q_asymmetry,
            blockAssemblyUsesDiscreteAngularMomentsWithoutModeTruncation=True,
            timings=timings, seconds=time.monotonic()-started)

    def unpack(self, vector):
        x = np.asarray(vector, dtype=float).reshape(self.basis.nb, self.basis.na)
        out = np.empty_like(x)
        for column, (_, upper) in enumerate(self.factors):
            out[:, column] = solve_banded((0, 5), upper, x[:, column], check_finite=False)
        return out

    def transpose(self, gradient):
        x = np.asarray(gradient, dtype=float).reshape(self.basis.nb, self.basis.na)
        out = np.empty_like(x)
        for column, (lower, _) in enumerate(self.factors):
            out[:, column] = solve_banded((5, 0), lower, x[:, column], check_finite=False)
        return out.ravel()

    def old_factor(self, coefficients, transpose=False):
        x = np.asarray(coefficients, dtype=float).reshape(self.basis.nb, self.basis.na)
        out = np.empty_like(x)
        for lower, columns in self.old_groups:
            out[:, columns] = triangular_apply(lower, x[:, columns], transpose)
        return out


class SameSobolevAugmented:
    """[J T; sqrt(lambda) L_S^T T] with the OLD physical regularizer S."""
    def __init__(self, linear, damping, eta=1e-3):
        self.linear, self.damping = linear, float(damping)
        if not math.isfinite(self.damping) or self.damping <= 0:
            raise ValueError("Actual positive original LM lambda required")
        self.blocks = ExactChannelBlocks(linear, eta)
        self.root_damping = math.sqrt(self.damping)
        self.shape = (linear.shape[0]+linear.shape[1], linear.shape[1])
        self.operator = LinearOperator(self.shape, matvec=self.matvec,
                                       rmatvec=self.rmatvec, dtype=np.float64)
        self.rhs = np.r_[-linear.residual, np.zeros(linear.shape[1])]
        self.receipt = dict(
            schema="6a65-same-Sobolev-full-target-augmented-LM-v1",
            physicalRows=linear.shape[0], explicitRegularizerRows=linear.shape[1],
            columns=linear.shape[1], damping=self.damping,
            requiredLSMRDamp=0., oldSobolevQuadraticPreserved=True,
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
        r = self.linear.shape[0]
        gradient = self.raw_transpose(vector[:r])
        gradient += self.root_damping*self.blocks.old_factor(vector[r:], False)
        return self.blocks.transpose(gradient)

    def physical_normal_residual(self, direction):
        x = np.asarray(direction, dtype=float).reshape(self.linear.basis.nb, self.linear.basis.na)
        result = self.raw_transpose(self.raw_matvec(x)+self.linear.residual)
        result += self.damping*self.blocks.old_factor(self.blocks.old_factor(x, True), False)
        return result.ravel()
