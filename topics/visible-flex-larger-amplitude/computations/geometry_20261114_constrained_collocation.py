#!/usr/bin/env python3
"""Exact inlet/constant-state coordinates for the original full collocation.

This module does not change the physical ODE, its collocation formula, or
the complete right boundary.  Every constant core/control row and every
left boundary row becomes an algebraic identity.  No frequency is removed.
The diagonal weights define an optimization penalty, not a certified C2
norm.  In particular core weights include the inlet t_j=-2j*c_j term.
"""
from __future__ import annotations

import json
import resource
import time
import numpy as np
from scipy.interpolate import CubicHermiteSpline
from scipy.sparse.linalg import LinearOperator

from geometry_20261114_full_dn_augmented import SeparatedBoundary
from geometry_20261114_full_dn_prefix_controls import rms_domain
from geometry_20261114_separated_qr_bvp import local_blocks


class ExactCoordinates:
    def __init__(self, flow, boundary, nodes):
        self.flow, self.boundary = flow, boundary
        self.M, self.n, self.k, self.K = flow.M, flow.n, flow.k, boundary.K
        self.m = int(nodes)
        self.free = self.M - self.K
        self.physical_size = (self.m - 1) * self.n
        self.size = self.physical_size + self.free + self.k
        if self.size != (self.m - 1) * self.n + boundary.T:
            raise ValueError("The exact-coordinate problem must retain every right row")
        self.frequency = 2 * np.arange(1, self.M + 1)
        self.inlet = np.zeros((self.n, self.free))
        j = np.arange(self.K, self.M)
        self.inlet[j + 1, np.arange(self.free)] = 1
        self.inlet[self.M + 1 + j, np.arange(self.free)] = -self.frequency[j]
        physical_scale = np.r_[1., (1 + self.frequency) ** 2,
            (1 + self.frequency) ** 2, 1., 1 + self.frequency ** 2]
        core_scale = np.sqrt(physical_scale[1:self.M+1] ** 2
            + (self.frequency * physical_scale[self.M+1:2*self.M+1]) ** 2)[self.K:]
        stations = list(flow.profile.knots)
        for bump in getattr(flow.profile, "bumps", []):
            stations.extend(np.linspace(bump.left, bump.right, 33).tolist())
        if self.k:
            samples = np.asarray([flow.profile.control_jets(s) for s in stations])
            control_scale = np.maximum(1., np.max(abs(samples), axis=(0, 1)))
        else:
            control_scale = np.empty(0)
        self.scale = np.r_[np.tile(physical_scale, self.m - 1), core_scale, control_scale]
        if self.scale.shape != (self.size,) or np.any(self.scale <= 0):
            raise ValueError("Every exact coordinate needs a positive algorithmic scale")

    def unpack_parts(self, value):
        value = np.asarray(value, float)
        if value.shape != (self.size,):
            raise ValueError("Supply every physical, free-core and global-control coordinate")
        physical = value[:self.physical_size].reshape(self.m-1, self.n)
        free = value[self.physical_size:self.physical_size+self.free]
        control = value[self.physical_size+self.free:]
        return physical, free, control

    def expand(self, value):
        physical, free, control = self.unpack_parts(value)
        core = np.r_[self.boundary.target, free]
        result = np.zeros((self.m, self.flow.dimension))
        result[1:, :self.n] = physical
        result[0, 0] = 1.
        result[0, 1:self.M+1] = core
        result[0, self.M+1:2*self.M+1] = -self.frequency * core
        result[:, self.flow.core_slice] = core
        result[:, self.flow.parameter_slice] = control
        return result

    def pack(self, augmented):
        augmented = np.asarray(augmented, float)
        if augmented.shape != (self.m, self.flow.dimension):
            raise ValueError("Complete augmented source states are required")
        if (not np.all(augmented[:, self.flow.core_slice] == augmented[0, self.flow.core_slice])
                or not np.all(augmented[:, self.flow.parameter_slice] == augmented[0, self.flow.parameter_slice])):
            raise ValueError("Do not turn varying c(s) or p(s) into a fixed-metric warm")
        return np.r_[augmented[1:, :self.n].ravel(),
            augmented[0, self.n+self.K:self.n+self.M], augmented[0, self.flow.parameter_slice]]

    def lift_direction(self, value):
        physical, core, control = self.unpack_parts(value)
        result = np.zeros((self.m, self.flow.dimension))
        result[1:, :self.n] = physical
        result[0, :self.n] = self.inlet @ core
        result[:, self.n+self.K:self.n+self.M] = core
        result[:, self.flow.parameter_slice] = control
        return result

    def description(self):
        return dict(physical_rows=self.n, nodes=self.m, fixed_core_modes=self.K,
            free_core_modes=self.free, global_controls=self.k, dimension=self.size,
            exact_left_and_constant_rows_by_construction=True,
            scale_definition="r/t: (1+2j)^2; z: 1+(2j)^2; core: sqrt(wr_j^2+(2j*wt_j)^2); controls: sampled max of their 0/1/2 scalar jets, at least 1",
            scale_is_an_optimization_penalty_not_a_geometric_C2_certificate=True,
            core_scale_includes_inlet_tangent_cubic_frequency_cost=True,
            minimum_scale=float(self.scale.min()), maximum_scale=float(self.scale.max()))


class CompleteResidual:
    def __init__(self, mesh, flow, boundary):
        self.x = np.asarray(mesh, float)
        self.h = np.diff(self.x)
        self.mid = .5*(self.x[:-1]+self.x[1:])
        self.flow, self.boundary = flow, boundary
        self.chart = ExactCoordinates(flow, boundary, len(self.x))
        self.separated = SeparatedBoundary(boundary)
        frequency = self.chart.frequency
        self.rho_cosine = np.cos(frequency[:, None]
            *(2*np.pi*np.arange(boundary.trace.N)/boundary.trace.N))
        if np.any(self.h <= 0):
            raise ValueError("Use the complete strictly increasing original mesh")

    def evaluate(self, coordinates, require_rms=False):
        y = self.chart.expand(coordinates)
        f = self.flow(self.x, y.T).T
        middle = .5*(y[:-1]+y[1:]) - self.h[:, None]*(f[1:]-f[:-1])/8
        fm = self.flow(self.mid, middle.T).T
        col = y[1:]-y[:-1]-self.h[:, None]*(f[:-1]+f[1:]+4*fm)/6
        core = y[-1, self.flow.core_slice]
        rho = 1+((1-self.chart.frequency**2)*core)@self.rho_cosine
        rho_valid = bool(np.all(np.isfinite(core)) and np.all(np.isfinite(rho)) and np.min(rho) > 0)
        boundary_domain_error = None
        if not rho_valid:
            bc = np.full(self.flow.dimension, np.nan)
            boundary_domain_error = "Original uniform-physical-phi material_angles density guard"
        else:
            try:
                bc = self.separated(y[0], y[-1])
            except FloatingPointError as error:
                bc = np.full(self.flow.dimension, np.nan)
                boundary_domain_error = repr(error)
            except RuntimeError as error:
                if str(error) != "Material angle inversion did not converge":
                    raise
                bc = np.full(self.flow.dimension, np.nan)
                boundary_domain_error = str(error)
        finite_nodes = np.all(np.isfinite(f), axis=1)
        finite_mid = np.all(np.isfinite(fm), axis=1)
        finite = bool(np.all(finite_nodes) and np.all(finite_mid)
            and np.all(np.isfinite(col)) and np.all(np.isfinite(bc)))
        report = dict(node_domain_failures=int(np.count_nonzero(~finite_nodes)),
            midpoint_domain_failures=int(np.count_nonzero(~finite_mid)),
            boundary_finite=bool(np.all(np.isfinite(bc))), finite=finite,
            original_uniform_phi_rho_guard_valid=rho_valid,
            original_rho_guard_angles=self.boundary.trace.N,
            original_uniform_phi_rho_min=float(np.min(rho)) if np.all(np.isfinite(rho)) else None,
            boundary_domain_error=boundary_domain_error,
            complete_trial_RHS_recomputed=True,
            all_core_states_identical=bool(np.all(y[:, self.flow.core_slice] == y[0, self.flow.core_slice])),
            all_control_states_identical=bool(np.all(y[:, self.flow.parameter_slice] == y[0, self.flow.parameter_slice])),
            left_residual_max=(float(np.max(abs(bc[:self.separated.left_count]), initial=0))
                if np.all(np.isfinite(bc[:self.separated.left_count])) else None))
        if finite:
            report.update(physical_collocation_max=float(np.max(abs(col[:, :self.flow.n]))),
                complete_boundary_max=float(np.max(abs(bc))),
                constant_collocation_max=float(np.max(abs(col[:, self.flow.n:]), initial=0)))
        if require_rms and finite:
            bad, checks = rms_domain(self.x, y, f, self.flow)
            report.update(original_RMS_query_domain_failures=len(bad), original_RMS_query_checks=checks)
            finite = finite and not len(bad)
            report["finite"] = bool(finite)
        vector = np.r_[col[:, :self.flow.n].ravel(), bc[self.separated.left_count:]]
        return dict(y=y, f=f, middle=middle, fm=fm, collocation=col, boundary=bc,
            vector=vector, finite=bool(finite), report=report)

    def weights(self, state):
        # Fixed during each actual merit comparison, including every trial.
        # This is an optimization merit, not a replacement of final RMS.
        physical = 1/(self.h[:, None]*(1+abs(state["fm"][:, :self.flow.n])))
        return np.r_[physical.ravel(), np.full(self.boundary.T, 1e5)]


class CompleteLinearization:
    def __init__(self, problem, state, chunk=16):
        self.problem, self.chart = problem, problem.chart
        self.n, self.m = self.chart.n, self.chart.m
        self.k, self.free = self.chart.k, self.chart.free
        self.L = np.empty((self.m-1, self.n, self.n))
        self.R = np.empty_like(self.L)
        self.P = np.empty((self.m-1, self.n, self.k))
        self.samples = []
        begin = time.monotonic()
        flow = problem.flow
        for start in range(0, self.m-1, chunk):
            end = min(self.m-1, start+chunk)
            node = flow.jac(problem.x[start:end+1], state["y"][start:end+1].T)
            mid = flow.jac(problem.mid[start:end], state["middle"][start:end].T)
            for j in range(start, end):
                L, R = local_blocks(problem.h[j], node[:, :, j-start],
                    mid[:, :, j-start], node[:, :, j-start+1])
                self.L[j], self.R[j] = L[:self.n, :self.n], R[:self.n, :self.n]
                self.P[j] = L[:self.n, flow.parameter_slice]+R[:self.n, flow.parameter_slice]
                if j in (0, (self.m-1)//2, self.m-2):
                    self.samples.append((j, L, R))
                if (np.any(L[:self.n, flow.core_slice] != 0)
                        or np.any(R[:self.n, flow.core_slice] != 0)):
                    raise ValueError("The original local RHS unexpectedly gained an explicit core column")
            print(json.dumps(dict(event="constrained_original_blocks", intervals=end,
                total=self.m-1, seconds=time.monotonic()-begin,
                maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
        A, B = problem.separated.jacobian(state["y"][0], state["y"][-1])
        self.original_boundary_left, self.original_boundary_right = A, B
        right = B[problem.separated.left_count:]
        self.BY = right[:, :self.n]
        self.BC = right[:, self.n+self.chart.K:self.n+self.chart.M]
        self.BP = right[:, flow.parameter_slice]
        if not all(np.all(np.isfinite(v)) for v in (self.L, self.R, self.P, self.BY, self.BC, self.BP)):
            raise FloatingPointError("The actual full linearization is nonfinite")

    def matvec(self, direction):
        field, core, control = self.chart.unpack_parts(direction)
        y = np.vstack((self.chart.inlet @ core, field))
        col = (np.einsum("mij,mj->mi", self.L, y[:-1])
            + np.einsum("mij,mj->mi", self.R, y[1:]))
        if self.k:
            col += np.einsum("mij,j->mi", self.P, control)
        right = self.BY@y[-1]+self.BC@core+self.BP@control
        return np.r_[col.ravel(), right]

    def rmatvec(self, dual):
        dual = np.asarray(dual)
        split = (self.m-1)*self.n
        w, wb = dual[:split].reshape(self.m-1, self.n), dual[split:]
        left = np.einsum("mij,mi->mj", self.L, w)
        physical = np.einsum("mij,mi->mj", self.R, w)
        physical[:-1] += left[1:]
        physical[-1] += self.BY.T@wb
        core = self.chart.inlet.T@left[0]+self.BC.T@wb
        control = np.einsum("mij,mi->j", self.P, w)+self.BP.T@wb
        return np.r_[physical.ravel(), core, control]

    def operator(self, weights):
        weights = np.asarray(weights)
        scale = self.chart.scale
        return LinearOperator((self.chart.size, self.chart.size), dtype=float,
            matvec=lambda z: weights*self.matvec(np.asarray(z)/scale),
            rmatvec=lambda w: self.rmatvec(weights*np.asarray(w))/scale)

    def column_norms_squared(self, weights):
        """Exact column squared norms for diagonal preconditioning only."""
        split = (self.m-1)*self.n
        w, wb = weights[:split].reshape(self.m-1, self.n), weights[split:]
        left, right = np.empty((self.m-1, self.n)), np.empty((self.m-1, self.n))
        for start in range(0, self.m-1, 16):
            end = min(self.m-1, start+16)
            ww = w[start:end]**2
            left[start:end] = np.einsum("mij,mi,mij->mj", self.L[start:end], ww, self.L[start:end])
            right[start:end] = np.einsum("mij,mi,mij->mj", self.R[start:end], ww, self.R[start:end])
        right[:-1] += left[1:]
        right[-1] += np.sum((wb[:, None]*self.BY)**2, axis=0)
        first = self.L[0]@self.chart.inlet
        core = np.sum((w[0, :, None]*first)**2, axis=0)+np.sum((wb[:, None]*self.BC)**2, axis=0)
        control = np.einsum("mij,mi,mij->j", self.P, w**2, self.P)+np.sum((wb[:, None]*self.BP)**2, axis=0)
        return np.r_[right.ravel(), core, control]/self.chart.scale**2

    def verify(self, weights, state):
        rng = np.random.default_rng(20261114)
        op = self.operator(weights)
        reports = []
        for kind in ("all", "global-core-and-controls", "first-last-physical"):
            z, w = rng.standard_normal(self.chart.size), rng.standard_normal(self.chart.size)
            if kind == "global-core-and-controls":
                z[:self.chart.physical_size] = 0
            if kind == "first-last-physical":
                z[self.n:self.chart.physical_size-self.n] = 0
                z[self.chart.physical_size:] = 0
            Az, Atw = op@z, op.rmatvec(w)
            left, right = float(Az@w), float(z@Atw)
            denominator = max(1., float(np.linalg.norm(Az)*np.linalg.norm(w)),
                float(np.linalg.norm(z)*np.linalg.norm(Atw)))
            reports.append(dict(kind=kind, forward_dual=left, adjoint_dual=right,
                normwise_adjoint_error=abs(left-right)/denominator))
        direction = rng.standard_normal(self.chart.size)/self.chart.scale
        lifted = self.chart.lift_direction(direction)
        actual = self.matvec(direction)
        errors = []
        for j, L, R in self.samples:
            reference = (L@lifted[j]+R@lifted[j+1])[:self.n]
            got = actual[j*self.n:(j+1)*self.n]
            errors.append(float(np.max(abs(reference-got)))/max(1., float(np.max(abs(reference)))))
        b = self.original_boundary_left@lifted[0]+self.original_boundary_right@lifted[-1]
        errors.append(float(np.max(abs(b[self.problem.separated.left_count:]-actual[-self.problem.boundary.T:])))/max(1., float(np.max(abs(b)))))
        # This independently differentiates the entire original nonlinear
        # collocation evaluation, including its actual Hermite midpoint.
        # Never pass complex coordinates through the real chart.expand.
        import scipy.integrate._bvp as backend
        step = 1e-25
        direct_direction = direction.copy()
        direct_direction[:self.chart.physical_size] = 0
        direct_lifted = self.chart.lift_direction(direct_direction)
        complex_state = state["y"].T.astype(complex)+1j*step*direct_lifted.T
        col = backend.collocation_fun(lambda x, y, p: self.problem.flow(x, y),
            complex_state, np.empty(0), self.problem.x, self.problem.h)[0]
        direct = col[:self.n].imag.T.ravel()/step
        split = (self.m-1)*self.n
        direct_matrix = self.matvec(direct_direction)[:split]
        physical_error = float(np.max(abs(direct-direct_matrix)))/max(1., float(np.max(abs(direct))))
        passed = (max(row["normwise_adjoint_error"] for row in reports) <= 5e-12
            and max(errors) <= 5e-12 and np.isfinite(physical_error) and physical_error <= 5e-5)
        return dict(complete_adjoint_checks=reports,
            original_augmented_vs_exact_coordinate_action_relative_errors=errors,
            independent_original_nonlinear_collocation_complex_direction_relative_error=physical_error,
            independent_physical_direction_threshold=5e-5,
            physical_complex_direction_includes_actual_nonlinear_midpoint=True,
            independent_direction_scope="Only all free inlet core and global controls; interior physical coordinates zero",
            implementation_check_passed=bool(passed), verification_threshold=5e-12,
            no_native_tail_called=True, no_scientific_acceptance_claim=True)


def regularized_operator(operator, column_norm_squared, damping):
    """Column-precondition [A; damping I] without forming normal equations.

LSMR is called with damp=0 on this explicit rectangular operator.  Its
penalty is exactly damping**2 * ||z||**2, independently of preconditioning.
"""
    if not np.isfinite(damping) or damping <= 0:
        raise ValueError("Every trial model uses a strictly positive damping")
    n = operator.shape[1]
    diagonal = np.sqrt(np.asarray(column_norm_squared)+damping*damping)
    if np.any(~np.isfinite(diagonal)) or np.any(diagonal <= 0):
        raise ValueError("Every preconditioner column must be finite and positive")
    def mv(t):
        z = np.asarray(t)/diagonal
        return np.r_[operator@z, damping*z]
    def rmv(w):
        return (operator.rmatvec(np.asarray(w)[:n])+damping*np.asarray(w)[n:])/diagonal
    return LinearOperator((2*n, n), dtype=float, matvec=mv, rmatvec=rmv), diagonal
