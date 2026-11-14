#!/usr/bin/env python3
"""Bounded full-H subspace corrections for the original finite inequalities.

H=A.T@A+damping**2*I is always applied through the complete original A.
C is only a preconditioner. Approximate inverse actions generate full
global vectors; they are never substituted into an assumed positive
Schur matrix. The reduced metric is formed from actual A basis actions
and damping. Zero belongs to every search subspace, and the actual input
LSMR direction is retained as the first basis vector when nonzero.

At most 32 finite inequality rows are in the working set. All original
rows of the supplied B are checked to select additions and to repair the
final candidate. This module does not solve nonlinear equations, replace
scientific acceptance, claim a full-QP optimum, or trigger any workflow.
All numerical calls belong to this public repository's GitHub Actions.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np

from geometry_20261114_full_angle_projection_warm import (
    radial_feasible, choose_feasible_descent)


HERE = Path(__file__).resolve().parent
SCHEMA = "complete-H-bounded-active-subspace-inequality-correction-v1"
FROZEN = {
    "geometry_20261114_full_angle_projection_warm.py":
        "7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152",
    "geometry_20261114_full_angle_domain_operator.py":
        "af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7",
}


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Numerical work belongs to this public repository's Actions")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def identity(value):
    value = np.asarray(value)
    digest = hashlib.sha256(str(value.shape).encode()+b"\0"
        +value.dtype.str.encode()+b"\0"+value.tobytes(order="C")).hexdigest()
    return dict(shape=list(value.shape), dtype=value.dtype.str, sha256=digest,
        bytes=int(value.nbytes),
        definition="shape, NUL, dtype.str, NUL, actual C-order bytes")


def real_vector(value, size, name, copy=True):
    value = np.asarray(value)
    if value.dtype != np.dtype("float64") or value.shape != (size,):
        raise ValueError(f"{name} must retain a complete float64 vector of length {size}")
    if not np.all(np.isfinite(value)):
        raise FloatingPointError(f"{name} contains nonfinite values")
    return np.array(value, copy=True) if copy else value


def maxabs(value):
    return float(np.max(abs(value), initial=0))


def dot(a, b):
    value = float(np.dot(a, b))
    if not np.isfinite(value):
        raise FloatingPointError("A full finite-model scalar product is nonfinite")
    return value


def norm(a):
    return float(np.sqrt(max(0., dot(a, a))))


def generic_labels(value):
    if isinstance(value, dict):
        names = {"final_all_10240_linear_slack": "final_all_selected_linear_slack",
            "all_10240_rows_verified_nonnegative": "all_selected_rows_verified_nonnegative"}
        return {names.get(key, key): generic_labels(child) for key, child in value.items()}
    if isinstance(value, list):
        return [generic_labels(child) for child in value]
    return value


class WorkLimit(RuntimeError):
    pass


class _CountedA:
    def __init__(self, model):
        self.model, self.shape = model, model.A.shape

    def __matmul__(self, value):
        return self.model.apply_A(value)

    def matvec(self, value):
        return self.model.apply_A(value)

    def rmatvec(self, value):
        return self.model.apply_AT(value)


class _CountedB:
    def __init__(self, model):
        self.model, self.shape = model, model.domain.shape

    def matvec(self, value):
        return self.model.apply_B(value)

    def rmatvec(self, value):
        return self.model.apply_BT(value)


class _Model:
    def __init__(self, A, b, damping, C, domain, c, z0, deadline,
                 max_h_products, input_identity, progress):
        self.A, self.domain = A, domain
        self.m, self.n = map(int, A.shape)
        self.rows, bn = map(int, domain.shape)
        if bn != self.n:
            raise ValueError("B and the complete original A must use the same scaled coordinates")
        self.b = real_vector(b, self.m, "complete weighted residual b")
        self.C = real_vector(C, self.n, "original complete column preconditioner C")
        self.c = real_vector(c, self.rows, "all positive inequality offsets c")
        self.z0 = real_vector(z0, self.n, "actual complete scaled LSMR direction")
        self.damping = float(damping)
        self.lam2 = self.damping*self.damping
        if (not np.isfinite(self.lam2) or self.lam2 <= 0 or self.damping <= 0
                or np.any(self.C <= 0) or np.any(self.c <= 0)):
            raise ValueError("Retain positive damping, original positive C and strictly positive offsets")
        self.deadline = float(deadline)
        self.max_h_products = int(max_h_products)
        if not np.isfinite(self.deadline) or self.max_h_products < 1:
            raise ValueError("Supply a finite absolute monotonic deadline and positive H-work budget")
        self.started = time.monotonic()
        self.counts = dict(A=0, AT=0, B=0, BT=0, H=0, mandatory_H_after_deadline=0)
        self.progress_callback = progress
        self.sources = {name: sha(HERE/name) for name in FROZEN}
        if self.sources != FROZEN:
            raise ValueError("A frozen feasibility/selection or domain source changed")
        self.sources[Path(__file__).name] = sha(__file__)
        self.input_identity = (json.loads(json.dumps(input_identity, allow_nan=False))
            if input_identity is not None else None)
        self.fixed_identity = dict(schema=SCHEMA, source_sha256=self.sources,
            input_identity=self.input_identity,
            complete_A_shape=[self.m, self.n], complete_B_shape=[self.rows, self.n],
            domain_model_sha256=getattr(domain, "model_sha256", None),
            b=identity(self.b), C=identity(self.C), c=identity(self.c),
            actual_scaled_z0=identity(self.z0), damping=self.damping,
            supplied_A_must_be_the_same_fixed_A_as_b_and_domain=True,
            same_A_b_domain_identity_is_a_caller_contract=True,
            black_box_A_binding_not_independently_proved_by_this_helper=True,
            original_weights_are_not_recomputed_or_changed=True)
        self.g = self.apply_AT(self.b)
        self.f0 = .5*dot(self.b, self.b)
        self.proxy_A, self.proxy_B = _CountedA(self), _CountedB(self)
        self.certificates = []
        self.best_bound = None
        self.best_bound_point = None

    def _input(self, x, size, name):
        return real_vector(x, size, name, copy=False)

    def apply_A(self, x):
        self.counts["A"] += 1
        return real_vector(self.A.matvec(self._input(x, self.n, "A input")),
            self.m, "complete A action")

    def apply_AT(self, x):
        self.counts["AT"] += 1
        return real_vector(self.A.rmatvec(self._input(x, self.m, "AT input")),
            self.n, "complete AT action")

    def apply_B(self, x):
        self.counts["B"] += 1
        return real_vector(self.domain.matvec(self._input(x, self.n, "B input")),
            self.rows, "complete selected-angle B action")

    def apply_BT(self, x):
        self.counts["BT"] += 1
        return real_vector(self.domain.rmatvec(self._input(x, self.rows, "BT input")),
            self.n, "complete selected-angle BT action")

    def work_available(self, reserve_h=0):
        return (time.monotonic() < self.deadline
            and self.counts["H"]+int(reserve_h) <= self.max_h_products)

    def H(self, x, mandatory=False):
        # The action cap is hard, including final residual rereads. PCG
        # reserves the final action before every update. Only the elapsed
        # time boundary may be crossed to finish a mandatory diagnostic.
        if self.counts["H"] >= self.max_h_products:
            raise WorkLimit("Hard total complete-H action cap reached")
        if time.monotonic() >= self.deadline:
            if not mandatory:
                raise WorkLimit("Discretionary full-H elapsed-time budget reached")
            self.counts["mandatory_H_after_deadline"] += 1
        self.counts["H"] += 1
        x = self._input(x, self.n, "H input")
        value = self.apply_AT(self.apply_A(x))+self.lam2*x
        if not np.all(np.isfinite(value)):
            raise FloatingPointError("The original complete H action is nonfinite")
        return value

    def progress(self, name, **report):
        if self.progress_callback is not None:
            self.progress_callback(dict(event=name, elapsed_seconds=time.monotonic()-self.started,
                complete_action_counts=dict(self.counts), **report))

    def measure(self, x, mu, label):
        """Always recompute the original full model; no reduced/CG residual substitute."""
        x = real_vector(x, self.n, "full evidence point")
        mu = real_vector(mu, self.rows, "full original-row multipliers")
        if np.any(mu < 0):
            raise ValueError("A claimed dual evidence point must have nonnegative multipliers")
        Ax = self.apply_A(x)
        residual = self.b+Ax
        gradient = self.apply_AT(residual)+self.lam2*x
        BTmu = self.apply_BT(mu)
        r = gradient-BTmu
        slack = self.c+self.apply_B(x)
        if not all(np.all(np.isfinite(v)) for v in (gradient, r, slack, residual)):
            raise FloatingPointError("The full original model evidence is nonfinite")
        objective = .5*(dot(residual, residual)+self.lam2*dot(x, x))
        gdot = dot(self.b, Ax)
        quadratic = dot(Ax, Ax)+self.lam2*dot(x, x)
        complementarity = dot(mu, slack)
        r2 = dot(r, r)
        # R267: x need not be feasible. This is a raw floating evaluation
        # of its real-algebra lower bound, not an outward-rounded certificate.
        lower = objective-complementarity-r2/(2*self.lam2)
        feasible = bool(np.all(slack >= 0))
        local_E = complementarity+r2/(2*self.lam2) if feasible else None
        summary = dict(label=label, x=identity(x), multipliers=identity(mu),
            stationarity_residual=identity(r), original_slack=identity(slack),
            objective=objective, original_model_gdot=gdot,
            original_quadratic_term=quadratic,
            algebraic_model_decrease=-gdot-.5*quadratic,
            direct_objective_decrease=self.f0-objective,
            whole_gradient_L2=norm(gradient), whole_stationarity_L2=norm(r),
            whole_stationarity_Linf=maxabs(r), preconditioned_stationarity_L2=norm(r/self.C),
            preconditioned_residual_not_substituted_for_original=True,
            minimum_original_slack=float(np.min(slack)),
            maximum_relative_primal_violation=float(np.max(np.maximum(-slack, 0.)/self.c)),
            all_supplied_inequalities_feasible=feasible,
            nonnegative_multipliers=True, multiplier_L2=norm(mu),
            original_complementarity_sum=complementarity,
            original_complementarity_absolute_max=maxabs(mu*slack),
            R265_single_point_E=local_E,
            R267_lower_bound_raw_float=lower,
            real_algebra_lower_bound_valid_for_infeasible_x=True,
            floating_arithmetic_enclosure_provided=False,
            lower_bound_not_a_validated_certificate=True)
        self.certificates.append(summary)
        point = dict(x=x, mu=mu, r=r, slack=slack, Ax=Ax, gradient=gradient, report=summary)
        if np.isfinite(lower) and (self.best_bound is None or lower > self.best_bound):
            self.best_bound = lower
            self.best_bound_point = point
        return point


def _pcg(model, rhs, initial, label, *, max_iterations, relative_tolerance,
         recompute_every=8):
    """Preconditioned CG, with original full residual replacement and final reread.

    C is applied as two divisions, avoiding the formation of C**2.
    A small recursive or preconditioned residual never declares convergence.
    """
    rhs = real_vector(rhs, model.n, "full H right-hand side")
    x = real_vector(initial, model.n, "full H initial iterate")
    begin, h_before = time.monotonic(), model.counts["H"]
    threshold = float(relative_tolerance)*norm(rhs)
    history, reason = [], "maximum-inner-iterations"
    if not model.work_available(2):
        return x, dict(label=label, started=False, reason="no-discretionary-H-budget",
            original_residual_verified=False, converged=False, H_products=0, history=[])
    try:
        r = rhs-model.H(x)
    except WorkLimit as error:
        return x, dict(label=label, started=False, reason=str(error),
            original_residual_verified=False, converged=False, H_products=0, history=[])
    original_norm = norm(r)
    if original_norm <= threshold:
        return x, dict(label=label, started=True, reason="original-residual-tolerance-at-entry",
            original_residual_verified=True, original_residual_L2=original_norm,
            original_residual_Linf=maxabs(r), preconditioned_residual_L2=norm(r/model.C),
            rhs_L2=norm(rhs), tolerance=threshold, converged=True,
            H_products=model.counts["H"]-h_before, history=[], seconds=time.monotonic()-begin)
    z = (r/model.C)/model.C
    rz = dot(r, z)
    p = z.copy()
    is_true = True
    for iteration in range(int(max_iterations)):
        if not model.work_available(2):
            reason = "discretionary-H-work-or-time-limit"
            break
        if rz <= 0:
            reason = "nonpositive-preconditioned-product-with-nonzero-original-residual"
            break
        try:
            Hp = model.H(p)
        except WorkLimit:
            reason = "discretionary-H-time-limit-before-action"
            break
        curvature = dot(p, Hp)
        if curvature <= 0:
            reason = "nonpositive-computed-full-H-curvature"
            break
        alpha = rz/curvature
        candidate = x+alpha*p
        recursive = r-alpha*Hp
        if not np.all(np.isfinite(candidate)) or not np.all(np.isfinite(recursive)):
            reason = "nonfinite-inner-update"
            break
        x, r, is_true = candidate, recursive, False
        recursive_norm = norm(r)
        recompute = ((iteration+1) % int(recompute_every) == 0
            or recursive_norm <= threshold or iteration+1 == int(max_iterations)
            or not model.work_available(2))
        row = dict(iteration=iteration+1, recursive_residual_L2=recursive_norm,
            full_H_curvature=curvature, step=alpha, residual_recomputed=False)
        if recompute:
            # A final true residual is mandatory diagnostic work even if the
            # elapsed-time boundary was crossed inside the last A action.
            actual = rhs-model.H(x, mandatory=True)
            row.update(residual_recomputed=True,
                recursive_to_original_residual_difference_L2=norm(actual-r),
                original_residual_L2=norm(actual), original_residual_Linf=maxabs(actual),
                original_preconditioned_residual_L2=norm(actual/model.C))
            r, is_true = actual, True
        history.append(row)
        if is_true and norm(r) <= threshold:
            reason = "original-full-residual-tolerance"
            break
        new_z = (r/model.C)/model.C
        new_rz = dot(r, new_z)
        if new_rz <= 0:
            reason = "nonpositive-preconditioned-product-after-update"
            break
        if recompute:
            # Residual replacement restarts conjugacy; it does not pretend
            # the recursively accumulated residual is the actual full one.
            p = new_z.copy()
        else:
            p = new_z+(new_rz/rz)*p
        z, rz = new_z, new_rz
    if not is_true:
        r = rhs-model.H(x, mandatory=True)
    true_norm = norm(r)
    report = dict(label=label, started=True, reason=reason,
        original_residual_verified=True, original_residual_L2=true_norm,
        original_residual_Linf=maxabs(r), preconditioned_residual_L2=norm(r/model.C),
        rhs_L2=norm(rhs), tolerance=threshold,
        converged=bool(true_norm <= threshold), completed_iterations=len(history),
        relative_tolerance=relative_tolerance, maximum_iterations=int(max_iterations),
        original_residual_replacement_every=int(recompute_every),
        preconditioned_or_recursive_stop_not_used_as_original_residual=True,
        H_products=model.counts["H"]-h_before, seconds=time.monotonic()-begin,
        solution=identity(x), actual_full_residual=identity(r), history=history)
    return x, report


class _Basis:
    def __init__(self, model, maximum_columns):
        self.model, self.maximum_columns = model, int(maximum_columns)
        self.vectors, self.A_vectors, self.B_vectors, self.reports = [], [], [], []

    def add(self, value, label, preserve_input=False):
        if len(self.vectors) >= self.maximum_columns:
            raise ValueError("The declared finite global-subspace budget was exceeded")
        model = self.model
        v = real_vector(value, model.n, "full global basis proposal")
        Av = model.apply_A(v)
        initial_energy = dot(Av, Av)+model.lam2*dot(v, v)
        report = dict(label=label, original_vector=identity(v),
            original_H_energy=initial_energy, inserted=False,
            all_global_coordinates_retained=True)
        if initial_energy == 0:
            report["reason"] = "zero-global-direction"
            self.reports.append(report)
            return False
        if preserve_input:
            if self.vectors:
                raise ValueError("Only the first original LSMR vector is retained without rescaling")
            # Retain the actual z0 bytes, not only its ideally proportional
            # rounded normalization. Thus zero and the actual z0 really
            # belong to the finite real span of the stored columns.
            self.vectors.append(v)
            self.A_vectors.append(Av)
            Bv = model.apply_B(v)
            self.B_vectors.append(Bv)
            report.update(inserted=True, reason="original-LSMR-vector-retained-byte-for-byte",
                basis_index=0, original_input_bytes_preserved=True,
                stored_basis_vector=identity(v), actual_A_vector=identity(Av),
                actual_B_vector=identity(Bv), actual_H_energy=initial_energy)
            self.reports.append(report)
            return True
        # Two complete H-inner-product Gram-Schmidt passes. A newly
        # dependent basis vector may be omitted, but the selected original
        # inequality itself is still retained in the working set.
        for _ in range(2):
            for old, Aold in zip(self.vectors, self.A_vectors):
                old_energy = dot(Aold, Aold)+model.lam2*dot(old, old)
                coefficient = (dot(Aold, Av)+model.lam2*dot(old, v))/old_energy
                v -= coefficient*old
                Av -= coefficient*Aold
        Av = model.apply_A(v)
        energy = dot(Av, Av)+model.lam2*dot(v, v)
        relative = float(np.sqrt(max(0., energy/initial_energy)))
        floor = 128*np.finfo(float).eps
        report.update(post_orthogonalization_H_energy=energy,
            relative_H_norm=relative, algorithmic_basis_redundancy_floor=floor,
            redundancy_floor_not_a_mode_cut_or_scientific_tolerance=True)
        if energy <= 0 or relative <= floor:
            report["reason"] = "numerically-redundant-iteration-vector"
            self.reports.append(report)
            return False
        v /= np.sqrt(energy)
        # Read actual A and B again after the rounded normalization.
        Av, Bv = model.apply_A(v), model.apply_B(v)
        if not np.all(np.isfinite(v)):
            raise FloatingPointError("The global iteration basis is nonfinite")
        self.vectors.append(v)
        self.A_vectors.append(Av)
        self.B_vectors.append(Bv)
        report.update(inserted=True, reason="complete-global-H-vector",
            basis_index=len(self.vectors)-1,
            stored_basis_vector=identity(v), actual_A_vector=identity(Av),
            actual_B_vector=identity(Bv),
            actual_H_energy=dot(Av, Av)+model.lam2*dot(v, v))
        self.reports.append(report)
        return True

    def combine(self, coefficients, values=None):
        values = self.vectors if values is None else values
        size = self.model.n if not values else len(values[0])
        answer = np.zeros(size)
        for coefficient, vector in zip(coefficients, values):
            answer += coefficient*vector
        return answer

    def gram(self):
        k, model = len(self.vectors), self.model
        R = np.empty((k, k))
        for i in range(k):
            for j in range(i+1):
                value = (dot(self.A_vectors[i], self.A_vectors[j])
                    +model.lam2*dot(self.vectors[i], self.vectors[j]))
                R[i, j] = R[j, i] = value
        gradient = np.array([dot(v, model.g) for v in self.vectors])
        direct_gradient = np.array([dot(Av, model.b) for Av in self.A_vectors])
        return R, gradient, direct_gradient


def _subspace_dual(model, basis, active_rows, previous_mu, max_sweeps):
    """Solve only the current full-H subspace problem, with honest finite work.

    R comes from actual A basis actions and lambda, never from B times
    an assumed exact/inexact inverse. Its Cholesky is not repaired by a
    ridge or eigenvalue clipping. Original active rows are never discarded.
    """
    R, gradient, direct_gradient = basis.gram()
    if not len(gradient):
        raise ValueError("A nonzero full-global iteration basis is required")
    diagonal = np.sqrt(np.diag(R))
    if not np.all(np.isfinite(diagonal)) or np.any(diagonal <= 0):
        raise FloatingPointError("The actual full-H reduced Gram has a nonpositive diagonal")
    scaled_R = np.empty_like(R)
    for i in range(len(gradient)):
        for j in range(i+1):
            scaled_R[i, j] = scaled_R[j, i] = (R[i, j]/diagonal[i])/diagonal[j]
    factor = np.linalg.cholesky(scaled_R)

    def solve_R(rhs):
        return np.linalg.solve(factor.T, np.linalg.solve(factor, rhs/diagonal))/diagonal

    unconstrained = -solve_R(gradient)
    active = np.asarray(active_rows, dtype=np.int64)
    if len(active):
        T = np.array([[vector[row] for vector in basis.B_vectors] for row in active])
        # R=D L L.T D. G=(L^-1 D^-1 T.T).T (L^-1 D^-1 T.T)
        # is a dot-built positive Gram in
        # exact arithmetic, including rank-dependent original rows.
        Q = np.linalg.solve(factor, T.T/diagonal[:, None])
        G = np.empty((len(active), len(active)))
        for i in range(len(active)):
            for j in range(i+1):
                G[i, j] = G[j, i] = dot(Q[:, i], Q[:, j])
        offset = model.c[active]+T@unconstrained
        mu = np.array([previous_mu.get(int(row), 0.) for row in active])
    else:
        T, G, offset, mu = np.empty((0, len(gradient))), np.empty((0, 0)), np.empty(0), np.empty(0)
    if not all(np.all(np.isfinite(v)) for v in (R, gradient, T, G, offset, mu)):
        raise FloatingPointError("The actual full-H subspace arrays are nonfinite")
    if np.any(mu < 0):
        raise ValueError("Retain nonnegative working-set multipliers")
    history, reason = [], "empty-working-set" if not len(active) else "maximum-dual-sweeps"
    for sweep in range(int(max_sweeps)) if len(active) else ():
        if not model.work_available():
            reason = "discretionary-time-or-H-budget"
            break
        largest_change = 0.
        degenerate = []
        for i in range(len(active)):
            if G[i, i] <= 0:
                # No inverse/ridge is invented. Zero rows have positive
                # c in the exact restricted problem; contradictory stored
                # arithmetic is explicitly recorded and stops this sweep.
                if np.any(G[i] != 0) or offset[i]+dot(G[i], mu) < 0:
                    degenerate.append(int(active[i]))
                else:
                    # A genuinely zero stored row with positive offset
                    # has its dual minimum at zero, not at an old mu.
                    mu[i] = 0.
                continue
            derivative = offset[i]+dot(G[i], mu)
            new = max(0., mu[i]-derivative/G[i, i])
            change = new-mu[i]
            if not np.isfinite(new):
                raise FloatingPointError("The finite active dual update is nonfinite")
            mu[i] = new
            largest_change = max(largest_change, abs(change)*np.sqrt(G[i, i]))
        small_slack = offset+G@mu
        row = dict(sweep=sweep+1, maximum_H_normalized_multiplier_update=largest_change,
            active_predicted_minimum_slack=float(np.min(small_slack)),
            active_predicted_relative_violation=float(np.max(np.maximum(-small_slack, 0.)/model.c[active])),
            small_dual_objective=.5*dot(mu, G@mu)+dot(offset, mu),
            degenerate_violated_original_rows=degenerate)
        history.append(row)
        if degenerate:
            reason = "degenerate-stored-dual-Gram-with-violated-row"
            break
        if largest_change == 0:
            reason = "floating-coordinate-fixed-point"
            break
    coefficients = unconstrained+solve_R(T.T@mu) if len(active) else unconstrained
    point = basis.combine(coefficients)
    full_mu = np.zeros(model.rows)
    full_mu[active] = mu
    predicted_A = basis.combine(coefficients, basis.A_vectors)
    predicted_B = basis.combine(coefficients, basis.B_vectors)
    small_slack = offset+G@mu if len(active) else np.empty(0)
    restricted_stationarity = R@coefficients+gradient-T.T@mu
    report = dict(working_rows=active.tolist(), basis_columns=len(basis.vectors),
        complete_coordinates=model.n, complete_A_rows=model.m,
        metric="V.T (A.T A + damping^2 I) V, built from actual A V and V",
        approximate_inverse_Schur_not_used=True,
        zero_is_strictly_feasible_in_current_linear_subspace=True,
        subspace_contains_actual_LSMR_direction_in_real_algebra=True,
        full_original_QP_optimality_claimed=False,
        Cholesky_ridge_or_eigenvalue_clipping_used=False,
        full_H_Gram=R.tolist(), reduced_Gram_diagonal_scale=diagonal.tolist(),
        scaled_full_H_Gram=scaled_R.tolist(), reduced_gradient=gradient.tolist(),
        scaled_Gram_uses_one_shared_symmetric_triangle=True,
        restricted_stationarity_in_original_reduced_Gram=restricted_stationarity.tolist(),
        restricted_stationarity_in_original_reduced_Gram_L2=norm(restricted_stationarity),
        A_transpose_gradient_contraction_difference=(
            gradient-direct_gradient).tolist(),
        actual_active_B_basis=T.tolist(), finite_dual_Gram=G.tolist(),
        finite_dual_offset=offset.tolist(), coefficients=coefficients.tolist(),
        original_row_multipliers=mu.tolist(),
        active_predicted_slack=small_slack.tolist(),
        maximum_dual_sweeps=int(max_sweeps), completed_dual_sweeps=len(history),
        dual_stop_reason=reason, dual_history=history,
        dual_subproblem_not_assumed_converged=True)
    return point, full_mu, coefficients, predicted_A, predicted_B, report


def full_metric_inequality_correction(
        A, b, damping, C, domain, c, z0, deadline, *,
        max_active=32, max_h_products=1200, max_inner_iterations=64,
        inner_relative_tolerance=1e-8, max_dual_sweeps=200,
        input_identity=None, progress=None):
    """Return a candidate and complete actual fixed-model diagnostics.

    All arrays use the original full scaled-z coordinates. c must be the
    caller's declared strictly positive reserve offsets; this helper does
    not select theta or alter any constraint row. deadline is an absolute
    time.monotonic() time. Only discretionary inverse/basis/dual work is
    stopped at that deadline; final full-model/feasibility diagnostics may
    finish afterward and remain counted in the report. max_h_products is
    a hard total H-action cap, including original residual rereads.

    The result is not a nonlinear step or an accepted full BVP. The caller
    still applies the original complete merit and all-domain line search.
    """
    require_actions()
    max_active, max_inner_iterations, max_dual_sweeps = (
        int(max_active), int(max_inner_iterations), int(max_dual_sweeps))
    if (not 0 <= max_active <= 32 or not 1 <= max_inner_iterations <= 200
            or not 1 <= max_dual_sweeps <= 1000
            or not np.isfinite(inner_relative_tolerance)
            or inner_relative_tolerance <= 0):
        raise ValueError("Use at most 32 original working rows and explicit finite work bounds")
    model = _Model(A, b, damping, C, domain, c, z0, deadline,
        max_h_products, input_identity, progress)
    # Top-level operator-call bounds from the finite loops and the pinned
    # original selector (at most 12 B calls per radial repair). They do
    # not count the arithmetic hidden inside one supplied A/B action.
    action_caps = dict(H=int(max_h_products),
        A=int(max_h_products)+19+5*max_active,
        AT=int(max_h_products)+8+2*max_active,
        B=73+15*max_active, BT=6+3*max_active,
        A_plus_AT=2*int(max_h_products)+27+7*max_active)
    zero_mu = np.zeros(model.rows)
    raw = model.measure(model.z0, zero_mu, "actual-raw-LSMR-zero-dual-evidence")
    if (raw["report"]["original_model_gdot"] >= 0
            or raw["report"]["original_quadratic_term"] <= 0):
        return dict(usable_direction=False, direction=None,
            report=dict(schema=SCHEMA, fixed_model=model.fixed_identity,
                status="actual-LSMR-input-is-not-a-strict-complete-model-descent-ray",
                raw=raw["report"], original_action_counts=dict(model.counts),
                a_priori_complete_action_caps=action_caps,
                all_scientific_acceptance_unchanged=True),
            raw_evidence=raw, best_lower_bound_evidence=model.best_bound_point)
    ray = min(1., -raw["report"]["original_model_gdot"]
        /raw["report"]["original_quadratic_term"])
    backup, backup_repair = radial_feasible(model.proxy_B, ray*model.z0, model.c)
    backup_point = model.measure(backup, zero_mu, "actual-feasible-LSMR-ray-backup")
    best_feasible = backup_point
    basis = _Basis(model, max_active+2)
    basis.add(model.z0, "actual-complete-LSMR-direction", preserve_input=True)
    inverse_reports, active_history = [], []
    center, center_report = _pcg(model, -model.g, model.z0,
        "complete-H-unconstrained-refinement", max_iterations=max_inner_iterations,
        relative_tolerance=inner_relative_tolerance)
    inverse_reports.append(center_report)
    center_unchanged = identity(center) == raw["report"]["x"]
    center_evidence = (raw if center_unchanged else
        model.measure(center, zero_mu, "actual-H-refined-unconstrained-evidence"))
    center_report["unchanged_point_reuses_original_raw_evidence"] = center_unchanged
    if center_report["started"] and model.work_available():
        basis.add(center, "actual-complete-H-refined-center")
    active, previous_mu = [], {}
    stop = "maximum-working-rows"
    last_subspace = None
    for stage in range(max_active+1):
        if not model.work_available():
            stop = "discretionary-work-limit-before-next-subspace"
            break
        try:
            x, mu, coefficients, predicted_A, predicted_B, small = _subspace_dual(
                model, basis, active, previous_mu, max_dual_sweeps)
        except (np.linalg.LinAlgError, FloatingPointError, ValueError) as error:
            stop = "finite-subspace-factorization-or-arithmetic-failure"
            active_history.append(dict(stage=stage, working_rows=list(active),
                failure=repr(error), no_ridge_no_constraint_deletion=True))
            break
        evidence = model.measure(x, mu, f"full-H-subspace-{stage:02d}-unrepaired-evidence")
        small["actual_A_action_vs_basis_combination_max"] = maxabs(evidence["Ax"]-predicted_A)
        small["actual_B_action_vs_basis_combination_max"] = maxabs(
            evidence["slack"]-model.c-predicted_B)
        repaired, repair = radial_feasible(model.proxy_B, x, model.c)
        repaired_mu = float(repair["factor"])*mu
        feasible = model.measure(repaired, repaired_mu,
            f"full-H-subspace-{stage:02d}-all-row-feasible-evidence")
        if not feasible["report"]["all_supplied_inequalities_feasible"]:
            raise FloatingPointError("The original full-row repair did not verify")
        if feasible["report"]["objective"] < best_feasible["report"]["objective"]:
            best_feasible = feasible
        entry = dict(stage=stage, working_rows=list(active), subspace=small,
            actual_unrepaired=evidence["report"],
            all_row_radial_repair=repair,
            actual_repaired=feasible["report"],
            repaired_multiplier_rule="same positive radial factor times the nonnegative original-row multipliers; no KKT assertion")
        active_history.append(entry)
        last_subspace = dict(x=x, mu=mu, coefficients=coefficients, report=small)
        previous_mu = {int(j):float(mu[j]) for j in active}
        model.progress("full_H_active_subspace", stage=stage, working_rows=len(active),
            basis_columns=len(basis.vectors),
            original_full_stationarity_L2=evidence["report"]["whole_stationarity_L2"],
            original_max_relative_violation=evidence["report"]["maximum_relative_primal_violation"],
            best_feasible_objective=best_feasible["report"]["objective"],
            best_cross_point_lower_bound_raw_float=model.best_bound)
        if np.all(evidence["slack"] >= 0):
            stop = "all-supplied-linear-inequalities-feasible-at-subspace-point"
            break
        if len(active) >= max_active:
            stop = "maximum-32-or-requested-working-row-budget"
            break
        violation = np.maximum(-evidence["slack"], 0.)/model.c
        inactive = violation.copy()
        if active:
            inactive[np.asarray(active, dtype=int)] = -1.
        selected = int(np.argmax(inactive))
        if inactive[selected] <= 0:
            stop = "working-row-dual-unresolved-with-no-new-violated-row"
            break
        if not model.work_available(2):
            stop = "discretionary-work-limit-before-new-full-H-row-solve"
            break
        unit = np.zeros(model.rows)
        unit[selected] = 1.
        rhs = model.apply_BT(unit)
        vector, inverse = _pcg(model, rhs, np.zeros(model.n),
            f"complete-H-inverse-original-B-row-{selected}",
            max_iterations=max_inner_iterations,
            relative_tolerance=inner_relative_tolerance)
        inverse_reports.append(inverse)
        if not inverse["started"]:
            stop = "no-budget-for-selected-original-row"
            break
        if time.monotonic() >= model.deadline:
            stop = "deadline-after-row-inverse-before-working-row-or-basis-insertion"
            entry["completed_row_inverse_not_inserted"] = dict(index=selected,
                actual_slack=float(evidence["slack"][selected]),
                original_positive_offset=float(model.c[selected]),
                complete_B_transpose_row=identity(rhs),
                inverse_report_index=len(inverse_reports)-1,
                working_row_added=False, basis_vector_added=False)
            break
        active.append(selected)
        added = basis.add(vector, f"global-inverse-direction-for-original-row-{selected}")
        entry["next_selected_original_row"] = dict(index=selected,
            actual_slack=float(evidence["slack"][selected]),
            original_positive_offset=float(model.c[selected]),
            actual_relative_violation=float(violation[selected]),
            complete_B_transpose_row=identity(rhs), inverse_report_index=len(inverse_reports)-1,
            global_basis_direction_added=added,
            original_constraint_retained_even_if_basis_vector_dependent=True)
    # Reuse the frozen complete-model segment/ray selection, with all
    # original coordinates, all supplied rows and the same b/A/damping.
    selected, selected_action, selected_B, selection, candidates = choose_feasible_descent(
        model.proxy_B, model.proxy_A, model.b, model.z0,
        best_feasible["x"], model.damping, model.c)
    selection = generic_labels(selection)
    if selection["selection"] == "verified-radial-original-direction-backup":
        selected_mu = np.zeros(model.rows)
    else:
        multiplier_factor = (float(selection["segment_parameter"])
            *float(selection["projected_candidate_feasibility_repair"]["factor"])
            *float(selection["composed_direction_feasibility_repair"]["factor"]))
        selected_mu = multiplier_factor*best_feasible["mu"]
    final = model.measure(selected, selected_mu, "final-original-full-model-selected-evidence")
    if (not final["report"]["all_supplied_inequalities_feasible"]
            or final["report"]["original_model_gdot"] >= 0
            or final["report"]["algebraic_model_decrease"] <= 0):
        raise FloatingPointError("The final actually recomputed full-model direction is not usable")
    best_bound = model.best_bound
    cross_gap = final["report"]["objective"]-best_bound
    same_model = model.fixed_identity
    report = dict(schema=SCHEMA, fixed_model=same_model,
        status="bounded-full-H-subspace-candidate-and-original-feasible-descent-verified",
        numerical_execution_scope="one supplied fixed finite A/b/damping/B/c model",
        full_QP_optimality_claimed=False, finite_subspace_method=True,
        C_used_only_as_preconditioner=True, complete_H_metric_retained=True,
        maximum_working_rows=max_active, actual_working_rows=active,
        last_solved_working_rows=(last_subspace["report"]["working_rows"]
            if last_subspace is not None else []),
        maximum_basis_columns=max_active+2, actual_basis_columns=len(basis.vectors),
        all_global_coordinate_count=model.n, no_physical_mode_or_global_control_removed=True,
        all_supplied_inequality_rows_rechecked=True,
        active_selection="maximum actual (-slack)_+/c over all nonworking supplied rows",
        active_stop_reason=stop, inner_relative_tolerance=inner_relative_tolerance,
        maximum_inner_iterations=max_inner_iterations, maximum_dual_sweeps=max_dual_sweeps,
        max_total_H_products=int(max_h_products),
        maximum_CG_calls=max_active+1,
        maximum_subspace_solves=max_active+1,
        maximum_total_dual_sweeps=(max_active+1)*max_dual_sweeps,
        a_priori_complete_action_caps=action_caps,
        action_cap_scope="Top-level complete A/AT/B/BT calls; no new whole-field Jacobian is constructed.",
        supplied_absolute_monotonic_deadline=float(deadline),
        implicit_total_wall_seconds_default=None,
        budget_scope="Hard total H-action cap; deadline stops discretionary work, while final original residual, full-model, feasibility evidence and selection may finish afterward.",
        mandatory_post_budget_work_may_finish_after_deadline=True,
        original_action_counts=dict(model.counts), elapsed_seconds=time.monotonic()-model.started,
        input_feasible_ray_repair=backup_repair,
        best_full_H_feasible_candidate_improved_over_original_ray=(
            best_feasible["report"]["objective"] < backup_point["report"]["objective"]),
        final_direction_bytes_equal_original_feasible_ray=(
            final["report"]["x"] == backup_point["report"]["x"]),
        original_frozen_selection=selection, selection_candidate_rows=candidates,
        raw_original_evidence=raw["report"],
        H_refined_center_evidence=center_evidence["report"],
        final_original_evidence=final["report"],
        best_R267_lower_bound_raw_float=best_bound,
        best_R267_lower_bound_evidence=model.best_bound_point["report"],
        all_measured_R267_lower_bound_evidence=model.certificates,
        final_feasible_cross_point_objective_gap_raw_float=cross_gap,
        final_cross_point_gap_nonnegative_in_stored_arithmetic=bool(cross_gap >= 0),
        final_cross_point_distance_bound_raw_float=(
            float(np.sqrt(2*cross_gap))/model.damping if cross_gap >= 0 else None),
        R267_bounds_are_real_algebra_statements_but_float_values_are_not_validated_enclosures=True,
        original_residual_not_replaced_by_preconditioned_or_reduced_residual=True,
        original_nonlinear_backtracking_and_scientific_acceptance_not_run=True,
        new_scientific_acceptance_gate=False,
        source_mutation=False, native_tail_called=False)
    return dict(usable_direction=True, direction=selected,
        multipliers=selected_mu, stationarity_residual=final["r"],
        original_slack=final["slack"], original_A_direction=final["Ax"],
        raw_evidence=raw, H_refined_center_evidence=center_evidence,
        best_lower_bound_evidence=model.best_bound_point,
        best_subspace_feasible_evidence=best_feasible,
        final_evidence=final, last_subspace=last_subspace,
        basis_vectors=np.column_stack(basis.vectors),
        actual_A_basis=np.column_stack(basis.A_vectors),
        actual_B_basis=np.column_stack(basis.B_vectors),
        basis_generation_reports=basis.reports,
        inverse_reports=inverse_reports, active_history=active_history, report=report)

