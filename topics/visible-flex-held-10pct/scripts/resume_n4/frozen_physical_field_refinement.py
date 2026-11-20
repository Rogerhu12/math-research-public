"""One field-only correction with every physical prefix parameter frozen.

No numerical execution is recorded by adding this source.  This is an
in-process interface for an already reconstructed fixed=True n4 object with
its original actual nonlinear tail attached.  It is not a replacement for
the complete metric, tail, mean/nonmean two-jet, or README acceptance gates.
Only nodal field values move; the inlet is eliminated exactly, and optional
physical height anchors are eliminated at the last node.

A single call may perform one field Jacobian, a sparse LSMR solve and up to
max_backtracks+1 original nonlinear tail evaluations.  Its output arrays
belong in transient working storage, never in Git or CI artifacts.
"""
import copy
import math
from types import SimpleNamespace
import numpy as np
from scipy.integrate import _bvp
from scipy.sparse import csc_matrix, diags, vstack
from scipy.sparse.linalg import lsmr, splu


class ActualTailRejected(FloatingPointError):
    pass


def _maxabs(value):
    return float(np.max(np.abs(value))) if np.size(value) else 0.


class FrozenPhysicalField:
    """Keep the fully interpreted physical profile/core/chart fixed.

    obj must be the full-reference-lift fixed-profile object, not a
    design-only object whose p[0] means a profile displacement.  At this
    interface p[0]=log(q_actual/q_gauge), p[1:]*pscale are physical controls.
    The same immutable p is passed on every original field evaluation.
    supplied_tail_tolerance is the existing finite-tail gate, not a new one.
    """
    def __init__(self, obj, parameters, *, fixed_heights=None,
                 supplied_tail_tolerance=2e-9):
        self.obj = obj
        if not bool(obj.fixed):
            raise ValueError("Interpret and freeze the physical design first")
        self.p = np.array(parameters, dtype=float, copy=True)
        self.p.setflags(write=False)
        self.n, self.M = int(obj.n), int(obj.M)
        if self.n != 3*self.M+1 or self.p.shape != (self.M,):
            raise ValueError("Expected the original complete three-block state")
        if not hasattr(obj, "tail"):
            raise ValueError("Attach the original actual nonlinear tail")
        self.tail_tolerance = float(supplied_tail_tolerance)
        if self.tail_tolerance != 2e-9:
            raise ValueError("This n4 interface retains the original 2e-9 gate")
        self.initial = np.asarray(obj.initial(self.p), float).copy()
        self.flow = obj.flow(float(self.p[0]))
        if (getattr(self.flow, "exact_lift_core", None) is not obj._core or
                self.initial.shape != (self.n,)):
            raise ValueError("The full exact-core reference must be installed")
        self.profile = copy.deepcopy(obj.cfg)
        self.qg = float(obj.q)
        self.q_actual = float(obj.support_amplitude)
        self.scales = np.asarray(obj.pscale, float).copy()
        self.controls = self.scales*self.p[1:]
        self.sigma = float(obj.bridge.sigma)
        self.cut_E = float(obj.port["cut"]["E"])
        self.bcweights = np.asarray(obj.bcweights, float).copy()
        self.iz = int(obj.iz)
        if (self.iz != 2*self.M+1 or self.qg == 0 or self.cut_E <= 0 or
                self.bcweights.shape != (self.M,) or
                np.any(self.bcweights <= 0)):
            raise ValueError("Invalid original state, gauge, cut, or BC scales")
        self.fixed_heights = {int(j): float(h) for j, h in
                              (fixed_heights or {}).items()}
        if any(j < 0 or j >= self.M or not np.isfinite(h)
               for j, h in self.fixed_heights.items()):
            raise ValueError("Height keys are zero-based physical mode slots")
        self.description = dict(
            fixed_profile=copy.deepcopy(self.profile),
            q_gauge=self.qg, q_actual=self.q_actual,
            physical_controls=self.controls.tolist(),
            fixed_parameters=self.p.tolist(),
            fixed_height_targets=self.fixed_heights,
            reference_lift_coefficient=1.,
            primary_and_controls_are_unknowns=False,
            extra_forcing_parameters=False,
            mean_height_additive_constant_free=False,
            tail_kind="actual original nonlinear finite DN",
            tail_tolerance=self.tail_tolerance)

    def check_frozen(self):
        if (self.obj.cfg != self.profile or float(self.obj.q) != self.qg or
                not np.array_equal(np.asarray(self.obj.pscale), self.scales)):
            raise ValueError("Physical profile, gauge, or control scale changed")
        self.obj.initial(self.p)
        if (float(self.obj.support_amplitude) != self.q_actual or
                self.obj.flow(float(self.p[0])) is not self.flow):
            raise ValueError("Physical core or frozen chart/flow changed")

    def canonical(self, y):
        y = np.array(y, dtype=float, copy=True)
        if y.ndim != 2 or y.shape[0] != self.n or y.shape[1] < 2:
            raise ValueError("The full field on at least two nodes is required")
        y[:, 0] = self.initial
        for j, height in self.fixed_heights.items():
            y[self.iz+j, -1] = height/(self.sigma*self.qg)
        return y

    def free_columns(self, nodes, *, include_height_coordinates=False):
        free = np.arange(self.n, self.n*nodes, dtype=int)
        if self.fixed_heights and not include_height_coordinates:
            locked = np.array([(nodes-1)*self.n+self.iz+j
                               for j in self.fixed_heights], dtype=int)
            free = free[~np.isin(free, locked)]
        return free

    def fun(self, x, y, unused_p):
        return self.obj.fun(x, y, self.p)

    def fun_jac(self, x, y, unused_p):
        self.check_frozen()
        s, ds = self.obj.chart(np.asarray(x), float(self.p[0]))
        field_jac, _ = self.flow.fun_jac(s, y, self.p)
        # No analytic/finite-difference core-parameter columns are evaluated.
        return (np.asarray(ds)[None, None, :]*field_jac,
                np.zeros((self.n, self.M, len(x))))

    def _tail(self, yb, jacobian):
        height = self.sigma*self.qg*yb[self.iz:]
        response = self.obj.tail.solve(height, jacobian=jacobian)
        # The temporary affine inner port has neither accepted original
        # convergence nor residual fields and is deliberately refused here.
        if (response.get("converged") is not True or
                not np.isfinite(response.get("residual", np.inf)) or
                response.get("residual", np.inf) > self.tail_tolerance):
            raise ActualTailRejected("Original actual tail did not pass")
        return response

    def bc(self, ya, yb, unused_p):
        self.check_frozen()
        dy = self.flow.fun(np.array([self.flow.end]),
                           yb.astype(np.longdouble)[:, None], self.p)[:, 0]
        response = self._tail(yb, False)
        terminal = (self.qg*dy[self.iz:] -
                    np.asarray(response["jets"]["slope"])/math.sqrt(self.cut_E))
        return np.r_[ya-self.initial,
                     np.asarray(terminal/self.bcweights, float)]

    def bc_jac(self, ya, yb, unused_p):
        self.check_frozen()
        response = self._tail(yb, True)
        tail_jac = np.asarray(response["heightJetJacobian"], float)
        tail_jac = tail_jac.reshape(3*self.M+2, self.M)[:self.M]
        field_jac, _ = self.flow.fun_jac(
            np.array([self.flow.end]),
            yb.astype(np.longdouble)[:, None], self.p)
        terminal = self.qg*field_jac[self.iz:, :, 0].copy()
        terminal[:, self.iz:] -= (
            self.sigma*self.qg*tail_jac/math.sqrt(self.cut_E))
        A = np.zeros((self.n+self.M, self.n))
        B = np.zeros_like(A)
        A[:self.n] = np.eye(self.n)
        B[self.n:] = terminal/self.bcweights[:, None]
        return A, B, np.zeros((self.n+self.M, self.M))

    def assemble(self, x, y, *, jacobian=True):
        self.check_frozen()
        x = np.asarray(x, float)
        y = self.canonical(y)
        h = np.diff(x)
        if (x.ndim != 1 or len(x) != y.shape[1] or
                not np.all(np.isfinite(x)) or np.any(h <= 0) or
                x[0] != 0. or x[-1] != 1.):
            raise ValueError("Use the original normalized chart on [0,1]")
        col_fun, sys_jac = _bvp.prepare_sys(
            self.n, len(x), self.M, self.fun, self.bc,
            self.fun_jac, self.bc_jac, x, h)
        col, ym, f, fm = col_fun(y, self.p)
        spline = _bvp.create_spline(y, f, x, h)
        # Evaluate the same two extra points used by the original RMS rule.
        # Any original Frenet domain exception rejects the trial unchanged.
        mid = x[:-1]+h/2
        offset = .5*h*np.sqrt(3./7.)
        for sample in (mid-offset, mid+offset):
            self.fun(sample, spline(sample), self.p)
        bc0 = self.bc(y[:, 0], y[:, -1], self.p)
        if not np.array_equal(bc0[:self.n], np.zeros(self.n)):
            raise ValueError("The fixed full-core inlet was not eliminated")
        r = np.r_[col.ravel(order="F"), bc0[self.n:]]
        J = None
        if jacobian:
            full = sys_jac(y, self.p, ym, f, fm, bc0)
            count = self.n*(len(x)-1)
            rows = np.r_[np.arange(count),
                         np.arange(self.n*len(x), self.n*len(x)+self.M)]
            # Physical p columns are discarded. They were identically zero
            # in the assembly; no hidden parameter is solved.
            J = full[rows, :self.n*len(x)].tocsc()
        rms = _bvp.estimate_rms_residuals(
            self.fun, spline, x, h, self.p, 1.5*col/h, fm)
        self.check_frozen()
        return dict(x=x, y=y, residual=r, jacobian=J, f=f, f_middle=fm,
                    spline=spline, rms=rms,
                    original_bc_max=_maxabs(bc0[self.n:]),
                    original_inlet_max=_maxabs(bc0[:self.n]))

    def correct_once(self, x, y, *, ode_tolerance=1e-8,
                     bc_tolerance=1e-8, lsmr_maxiter=200,
                     max_backtracks=8):
        """Return one guarded candidate; never return a physical pass flag."""
        if min(ode_tolerance, bc_tolerance) <= 0:
            raise ValueError("Positive declared original residual scales required")
        y_input = np.asarray(y, float)
        base = self.assemble(x, y_input, jacobian=True)
        x, y, r = base["x"], base["y"], base["residual"]
        free = self.free_columns(len(x))
        J = base["jacobian"][:, free]
        h = np.diff(x)
        # Frozen-per-step weights approximate an integral ODE residual norm;
        # the 1/h factor prevents spurious improvement from shorter intervals.
        w_col = (1./np.sqrt(h)[None, :] /
                 (1.+np.abs(base["f_middle"])) / ode_tolerance)
        weights = np.r_[w_col.ravel(order="F"),
                        np.full(self.M, 1./bc_tolerance)]
        Jw = diags(weights)@J
        rw = weights*r
        norms = np.sqrt(np.asarray(Jw.power(2).sum(axis=0)).ravel())
        if not np.all(np.isfinite(norms)) or np.any(norms == 0):
            raise FloatingPointError("Zero/nonfinite field Jacobian column")
        colscale = 1./norms
        linear = lsmr(Jw@diags(colscale), -rw, atol=1e-10, btol=1e-10,
                      conlim=1e12, maxiter=int(lsmr_maxiter))
        step = colscale*linear[0]
        slope = float(rw@(Jw@step))
        merit = float(rw@rw)
        report = dict(
            kind="one frozen-physical field correction",
            nodes=len(x), state_unknowns=len(free),
            equations=len(r), surplus=len(r)-len(free),
            initial_field_clamp_max=_maxabs(y-y_input),
            max_rms_before=_maxabs(base["rms"]),
            actual_dn_before=base["original_bc_max"],
            lsmr_stop=int(linear[1]), lsmr_iterations=int(linear[2]),
            lsmr_reported_condition=float(linear[6]),
            linear_weighted_residual=float(linear[3]),
            weighted_merit_before=merit,
            predicted_directional_derivative=slope,
            accepted_step=False, domain_rejections=[],
            parameters_changed=False, original_physical_pass=False,
            full_metric_evaluated=False, full_seam_evaluated=False,
            README5_fixed_parameters_convergence_claim=False)
        chosen = base
        if np.all(np.isfinite(step)) and slope < 0:
            for k in range(int(max_backtracks)+1):
                alpha = 2.**(-k)
                flat = y.ravel(order="F").copy()
                flat[free] += alpha*step
                try:
                    trial = self.assemble(
                        x, flat.reshape(y.shape, order="F"), jacobian=False)
                except FloatingPointError as exc:
                    report["domain_rejections"].append(
                        dict(alpha=alpha, kind=type(exc).__name__, reason=str(exc)))
                    continue
                trial_merit = float(np.sum((weights*trial["residual"])**2))
                if trial_merit <= merit+2e-4*alpha*slope:
                    chosen = trial
                    report.update(accepted_step=True, alpha=alpha,
                                  weighted_merit_after=trial_merit)
                    break
        report.update(
            max_rms_after=_maxabs(chosen["rms"]),
            actual_dn_after=chosen["original_bc_max"],
            inlet_after=chosen["original_inlet_max"])
        return SimpleNamespace(x=x, y=chosen["y"], p=self.p.copy(),
                               sol=chosen["spline"], report=report)

    def compatibility_debt(self, x, y):
        """One exact-linearization formula, with a measured solve defect.

        This optional diagnostic may be ill-conditioned: no inverse bound
        or rigorous lower bound is claimed by a floating sparse LU.
        """
        data = self.assemble(x, y, jacobian=True)
        nodes = len(data["x"])
        # For the formula A is square before eliminating the two optional
        # height coordinates. Their equations are appended to C explicitly.
        columns = self.free_columns(nodes, include_height_coordinates=True)
        J = data["jacobian"][:, columns]
        count = self.n*(nodes-1)
        A, C = J[:count].tocsc(), J[count:].tocsc()
        rE, rT = data["residual"][:count], data["residual"][count:]
        labels = ["DN_"+str(j) for j in range(self.M)]
        if self.fixed_heights:
            rows, extra_residual = [], []
            for j, height in self.fixed_heights.items():
                row = np.zeros(len(columns))
                column = (nodes-1)*self.n+self.iz+j
                row[np.flatnonzero(columns == column)[0]] = self.sigma*self.qg
                rows.append(row)
                extra_residual.append(
                    self.sigma*self.qg*data["y"][self.iz+j, -1]-height)
                labels.append("physical_H_"+str(j))
            C = vstack([C, csc_matrix(np.asarray(rows))], format="csc")
            rT = np.r_[rT, extra_residual]
        factor = splu(A)
        v = factor.solve(rE)
        debt = rT-C@v
        return dict(
            formula="eta=r_T-C A^{-1} r_E",
            residual_scopes=labels, compatibility_debt=debt.tolist(),
            internal_feedback=(C@v).tolist(),
            raw_terminal_residual=rT.tolist(),
            linear_solve_defect=_maxabs(A@v-rE),
            linear_solve_rhs_max=_maxabs(rE),
            internal_newton_field_correction_max=_maxabs(v),
            boundary_units="DN uses original bcweights; added H is physical",
            compatibility_is_float_diagnostic=True,
            rigorous_inverse_bound=False, nonlinear_nonexistence_claim=False)
