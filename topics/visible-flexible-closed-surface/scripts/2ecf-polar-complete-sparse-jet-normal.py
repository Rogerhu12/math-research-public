#!/usr/bin/env python3
"""Two-grid complete 14-row normal with exact sparse-jet angular algebra.

Static provenance: original complete normal body is copied with only the
angular contraction replaced. This is a distinct numerical consumer.
Point covariance, radial accumulation, physical S and band factor remain.

Every complete point row and every Cartesian angular cross term is retained.
Discrete angular products use exact signed rFFT moments, including aliases.
Only the invertible right preconditioner changes. The physical LM quadratic
remains ||J d+r||^2 + lambda ||L_S^T d||^2 with the original Sobolev factor.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[_key]='1'
import hashlib
import importlib.util
from pathlib import Path
import sys
ORIGINAL_SHA = '8e8d40c05ba5b5e15c49be4c7d91c882d93007567f67caa19a4a43ad39bc2084'
KERNEL_SHA = '79735d9dcdbc37dec7de70f7ac7bd16dfd766621ca18187cb7816356683e4ddb'
_kernel_path=Path(__file__).with_name('2ecf-polar-complete-sparse-jet-angular.py')
if hashlib.sha256(_kernel_path.read_bytes()).hexdigest()!=KERNEL_SHA:raise ValueError('Audited complete angular kernel changed')
_spec=importlib.util.spec_from_file_location('actual_complete_sparse_jet_angular',_kernel_path)
sparse_angular=importlib.util.module_from_spec(_spec);sys.modules[_spec.name]=sparse_angular;_spec.loader.exec_module(sparse_angular)
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


class CompleteAreaRadialNormal:
    """Full J^T J in radial-major scalar band form, no cross-channel dropping."""
    def __init__(self, linear, eta=.1):
        started = time.monotonic()
        eta = float(eta)
        if not math.isfinite(eta) or eta <= 0:
            raise ValueError("Explicit finite positive preconditioner regularization required")
        self.linear, self.basis, self.eta = linear, linear.basis, eta
        basis = self.basis
        nc, nb = basis.na, basis.nb
        if (tuple(linear.names) != ("training", "observer")
            or linear.statistics.get("schema") !=
                "6a65-complete-original13-plus-reciprocal-area-power-two-row-v1"
            or basis.dimension != nb*nc or basis.degree != 5
            or linear.preconditioner.bandwidth != 5
            or linear.preconditioner is not linear.parent.preconditioner):
            raise ValueError("Actual q=2 two-grid complete periodic Cartesian layout required")
        total_rows = 0
        grid_receipts = []
        for name in linear.names:
            original, area = linear.parent.groups[name], linear.groups[name]
            N = original.N
            if (original.basis is not basis or area.basis is not basis
                or original.preconditioner is not linear.preconditioner
                or N != area.N or N % 2 or N <= 2*basis.M
                or original.shape != (len(original.nodes)*N*13, basis.dimension)
                or len(area.residual) != len(original.nodes)*N
                or area.stats.get("reciprocalPower") != 2
                or not np.array_equal(original.nodes, area.cache.nodes)
                or not np.array_equal(area.cache.u, 2*np.pi*np.arange(N)/N)
                or original.slices != area.slices
                or any((a != b).nnz for a, b in zip(original.matrices, area.matrices))):
                raise ValueError("Both original13 and actual q=2 rows must share their exact grid")
            total_rows += len(original.nodes)*N*14
            grid_receipts.append(dict(name=name, radialPoints=len(original.nodes),
                fullAngles=N, originalRows=original.shape[0], areaRows=len(area.residual),
                areaGradientsAlreadyWeighted=True, extraWeightApplied=False))
        if linear.shape != (total_rows, basis.dimension):
            raise ValueError("Every 14-row point from both grids is required")
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
        for name in linear.names:
            original, area = linear.parent.groups[name], linear.groups[name]
            N = original.N
            for block_index, sl in enumerate(original.slices):
                B = np.stack([b[sl].toarray() for b in original.matrices])
                live = np.any(B != 0., axis=0)
                for row in live:
                    active = np.flatnonzero(row)
                    if len(active) and (len(active) > 6 or np.any(np.diff(active) != 1)):
                        raise ValueError("Contiguous quintic radial support of size at most six required")
                if not np.any(live):
                    skipped_points += B.shape[1]*N
                    continue
                part = original._get_block(block_index, sl)
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
                area_packet = area.packets[block_index]
                derivative = np.zeros((B.shape[1], N, 6, 3))
                # gs/gu ALREADY contain sqrt(strength * half-grid metric weight/N).
                # The q=2 derivative includes -2*target**2/sigma**3/a. No new
                # quadrature or grid factor is applied here.
                derivative[:, :, 1] = area_packet.gs
                derivative[:, :, 2] = area_packet.gu
                gram += np.einsum("suic,sujd->sucdij", derivative, derivative,
                                  optimize=True)
                spectrum = np.fft.rfft(gram, axis=1)
                largest_temporary = max(largest_temporary, gram.nbytes+spectrum.nbytes+
                                        cotangent.nbytes+derivative.nbytes+B.nbytes)
                del gram, cotangent, derivative
                timings["pointCovarianceSeconds"] += time.monotonic()-t0
                covariance_points += B.shape[1]*N
                vjp_calls += 13
                t0 = time.monotonic()
                Q, angular_receipt = sparse_angular.contract(spectrum, basis.channels, N)
                alias_frequency_pairs += angular_receipt['discreteAliasedFrequencyPairs']
                maximum_imaginary = max(maximum_imaginary, angular_receipt['maximumImaginaryFinalContraction'])
                maximum_moment_real = max(maximum_moment_real, angular_receipt['maximumRealFinalContraction'])
                largest_temporary = max(largest_temporary, spectrum.nbytes+Q.nbytes+B.nbytes)
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
            schema="2ecf-complete-physical-normal-sparse-jet-angular-v1",
            originalAssemblyEntrySHA256=ORIGINAL_SHA,
            angularKernelEntrySHA256=KERNEL_SHA,
            sameCompletePointCovarianceRadialAccumulationAndFactorization=True,
            completeSignedFourierJetPolynomialContraction=True,
            columns=basis.dimension, physicalRows=linear.shape[0], radialBlocks=nb,
            angularChannels=nc, radialBlockHalfBandwidth=5,
            scalarHalfBandwidth=self.half_bandwidth, eta=eta,
            completeNormalBandBytes=self.normal_band.nbytes,
            bandFactorBytes=self.factor.nbytes, completeJacobianFormed=False,
            completeDenseNormalMatrixFormed=False,
            fullPhysicalNormalAssembledWithoutCrossChannelDropping=True,
            everyCartesianCrossComponentCovarianceRetained=True,
            allThirteenRowsInPointCovariance=True, localCompleteVJPCalls=vjp_calls,
            allActualInverseSquareAreaRowsInPointCovariance=True,
            reciprocalAreaPower=2, areaGradientsNotReweighted=True,
            bothCompleteGrids=grid_receipts, commonOldSobolevAddedExactlyOnce=True,
            assembledPoints=covariance_points, structurallyZeroPreconditionerPoints=skipped_points,
            zeroPointRowsStillRetainedInFullOperator=True,
            discreteAngularMomentsWithoutModeTruncation=True,
            conjugateAliasFrequencyPairsUsed=alias_frequency_pairs,
            maximumImaginaryFinalContractionRoundoff=maximum_imaginary,
            relativeImaginaryFinalContractionRoundoff=maximum_imaginary/max(1., maximum_moment_real),
            maximumQAntisymmetryBeforeRoundoffSymmetrization=maximum_q_asymmetry,
            diagonalEquilibrationChangesPhysicalPreconditioner=False,
            diagonalScaleMinimum=float(np.min(self.diagonal_scale)),
            diagonalScaleMaximum=float(np.max(self.diagonal_scale)),
            triangularSolves="BLAS dtbsv on the saved lower band factor",
            largestTrackedOuterTemporaryBytes=largest_temporary,
            sparseAngularInternalTemporaryBytesNotIncluded=True,
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


class SameSobolevAreaFullBandAugmented:
    """[J T; sqrt(lambda) L_S^T T], full-band T and the OLD physical S."""
    def __init__(self, linear, damping, eta=.1):
        self.linear, self.damping = linear, float(damping)
        if not math.isfinite(self.damping) or self.damping <= 0:
            raise ValueError("Actual positive original LM lambda required")
        self.blocks = CompleteAreaRadialNormal(linear, eta)
        self.root_damping = math.sqrt(self.damping)
        self.shape = (linear.shape[0]+linear.shape[1], linear.shape[1])
        self.operator = LinearOperator(self.shape, matvec=self.matvec,
                                       rmatvec=self.rmatvec, dtype=np.float64)
        self.rhs = np.r_[-linear.residual, np.zeros(linear.shape[1])]
        self.receipt = dict(schema="6a65-two-grid-q2-area-same-Sobolev-full-band-preconditioned-LM-v1",
            physicalRows=linear.shape[0], explicitRegularizerRows=linear.shape[1],
            columns=linear.shape[1], damping=self.damping, requiredLSMRDamp=0.,
            oldSobolevQuadraticPreserved=True,
            allPhysicalRowsAndCrossChannelCouplingsRetained=True,
            completeTargetOrBasisChanged=False, assembly=self.blocks.receipt)

    def raw_matvec(self, coefficients):
        linear = self.linear
        x = np.asarray(coefficients, dtype=float).reshape(linear.basis.nb, linear.basis.na)
        originals = []
        for name in linear.names:
            original = linear.parent.groups[name]
            out = np.empty((len(original.nodes), original.N, 13))
            for index, sl in enumerate(original.slices):
                packet = original.basis.packet(tuple(b[sl] for b in original.matrices), x, original.N)
                out[sl] = original._get_block(index, sl).jvp(packet.swapaxes(1, 2))
            originals.append(out.ravel())
        # Match CompleteAreaTwoGrid exactly: original13 training/observer,
        # then area training/observer, with no permutation or row deletion.
        return np.concatenate(originals+[linear.groups[name].jvp_coefficients(x)
                                         for name in linear.names])

    def raw_transpose(self, vector):
        linear = self.linear
        vector = np.asarray(vector, dtype=float)
        if vector.shape != (linear.shape[0],):
            raise ValueError("Every original13 and inverse-square-area cotangent required")
        out = np.zeros((linear.basis.nb, linear.basis.na))
        for grid_index, name in enumerate(linear.names):
            original = linear.parent.groups[name]
            begin, end = linear.parent.boundaries[grid_index:grid_index+2]
            q = vector[begin:end].reshape(len(original.nodes), original.N, 13)
            for index, sl in enumerate(original.slices):
                packet = original._get_block(index, sl).vjp(q[sl]).swapaxes(1, 2)
                out += original.basis.packet_adjoint(tuple(b[sl] for b in original.matrices), packet)
            begin, end = linear.boundaries[grid_index+1:grid_index+3]
            out += linear.groups[name].vjp_coefficients(vector[begin:end])
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
