"""Analytical lambda column of the literal R53 collocation.

This differentiates the existing finite Gauss rule, its cumulative primitive,
and its real-origin projection. It does not replace that finite core by a true
integral. The full reference lift, its inlet projection, coordinate convection,
and the collocation midpoint dependence are retained. No solve or acceptance
is performed here. Saved initially before complete-column execution; compare
this column with complete residual differences on
the same actual field before using it as a numerical continuation direction.
"""
import numpy as np


def xyz(value):
    value = np.asarray(value)
    return np.stack((value.real, value.imag, np.zeros_like(value.real)), axis=-1)


class CoreLambdaJets:
    def __init__(self, core):
        required = ("_phase_fields", "_fields", "_omega", "_window",
                    "_integration_grid", "_gx", "_gw", "_beta_all")
        if any(not hasattr(core, name) for name in required):
            raise TypeError("The literal original R53 material core is required")
        if not 0 < core.homotopy <= 1:
            raise ValueError("A positive original R53 homotopy is required")
        self.core = core
        edges = core._integration_grid
        increments = self.position_integral(edges[:-1], edges[1:])
        self.primitive = np.r_[0j, np.cumsum(increments)]
        # Match the source constructor's real projection of the closing origin.
        self.origin = complex((self.primitive[-1]/np.expm1(1j*core.period)).real)

    def phase_fields(self, theta):
        core = self.core
        theta = np.asarray(theta, dtype=float).reshape(-1)
        original = core._fields(theta)
        x, W, _, _, C = core._window(theta)
        phase_lambda = core._omega(theta)[:, 0]+(x-C)*core._beta_all[0]
        curvature_lambda = (1-W)*(core.k-original["kappa"])+core.beta*W
        phase = original["phi"]+core.homotopy*phase_lambda
        curvature = original["kappa"]+core.homotopy*curvature_lambda
        return phase, curvature, phase_lambda, curvature_lambda

    def position_integral(self, first, last):
        core = self.core
        first, last = (np.asarray(value, dtype=float).reshape(-1)
                       for value in (first, last))
        theta = ((first[:, None]+last[:, None])/2+
                 (last-first)[:, None]*core._gx[None, :]/2)
        phase, _, phase_lambda, _ = self.phase_fields(theta.reshape(-1))
        values = (-np.exp(1j*phase)*phase_lambda).reshape(
            len(first), core.quadrature_order)
        return np.einsum("q,nq->n", core._gw, values)*(last-first)/2

    def evaluate(self, theta):
        core = self.core
        theta = np.asarray(theta, dtype=float).reshape(-1)
        sectors = np.floor(theta/core.period)
        local = theta-sectors*core.period
        phase, curvature, C, Cprime = self.phase_fields(local)
        indices = np.searchsorted(core._integration_grid, local, side="right")-1
        indices = np.clip(indices, 0, len(core._integration_grid)-2)
        primitive = (self.primitive[indices]+
                     self.position_integral(core._integration_grid[indices], local))
        rotation = np.exp(1j*sectors*core.period)
        normal = np.exp(1j*phase)*rotation
        return (xyz((self.origin+primitive)*rotation), xyz(-normal*C),
                xyz(-normal*(Cprime+1j*curvature*C)))


class OriginalLambdaColumn:
    """Partial lambda derivatives at one fixed original (Y,p,t) state."""
    def __init__(self, obj, p, window=(.5, .9)):
        obj.initial(p)
        self.obj, self.p = obj, np.asarray(p, dtype=float).copy()
        self.flow, self.window = obj.flow(p[0]), tuple(window)
        self.core = obj._core
        self.jets = CoreLambdaJets(self.core)
        self.fields = {}
        # The inlet uses the source's own quadrature, not the RHS angular grid.
        N = max(2048, 128*obj.M)
        angular = self.flow.angular(N)
        basis = self.flow.basis(N)[0]
        d0 = self.jets.evaluate(angular[1])[0]
        self.inlet = self.flow.project(d0[None, :, :], basis)[:, 0]/obj.q

    def lift_fields(self, N):
        if N not in self.fields:
            f = self.flow
            angular = f.angular(N)
            d0, d1, d2 = self.jets.evaluate(angular[1])
            rho, rhop = angular[2][:, None], angular[3][:, None]
            derivatives = (d0, d1*rho, d2*rho*rho+d1*rhop)
            basis = f.basis(N)
            self.fields[N] = tuple(value-f.values(
                self.obj.q*self.inlet[:, None], B)[0]
                for value, B in zip(derivatives, basis))
        return self.fields[N]

    def rhs(self, t, y):
        obj, f = self.obj, self.flow
        if obj._core is not self.core or obj._flow is not self.flow:
            raise ValueError("Do not reuse a lambda column after changing its base core")
        s, ds = obj.chart(t, self.p[0])
        H, H1, H2 = self.lift_fields(f.B.shape[1])
        a, v, _ = f.profile(s)
        lo, hi = self.window
        span = (hi-lo)*f.prefix_end
        xx = np.clip((s-lo*f.prefix_end)/span, 0., 1.)
        chi = 1-xx**3*(10-15*xx+6*xx*xx)
        chip = -30*xx*xx*(1-xx)**2/span
        h, hp = a*chi, v*chi+a*chip
        answer = np.empty_like(y)
        for first in range(0, len(s), 64):
            sl = slice(first, first+64)
            frame = f.frame(s[sl], obj.q*y[:, sl])
            d1, d2 = h[sl, None, None]*H1, h[sl, None, None]*H2
            velocity = (f.frame_jvp(frame, d1, d2)+
                        frame["geo"]["v"][:, :, None]*d1-
                        hp[sl, None, None]*H)
            answer[:, sl] = ds[sl][None, :]*f.project(velocity, f.B)/obj.q
        return answer

    def state_jvp(self, t, y, direction):
        obj, f = self.obj, self.flow
        s, ds = obj.chart(t, self.p[0])
        answer = np.empty_like(y)
        for first in range(0, len(s), 64):
            sl = slice(first, first+64)
            frame = f.frame(s[sl], obj.q*y[:, sl])
            d1 = obj.q*f.values(direction[:, sl], f.B1)
            d2 = obj.q*f.values(direction[:, sl], f.B2)
            velocity = (f.frame_jvp(frame, d1, d2)+
                        frame["geo"]["v"][:, :, None]*d1)
            answer[:, sl] = ds[sl][None, :]*f.project(velocity, f.B)/obj.q
        return answer

    def collocation(self, x, y, midpoint_y):
        step = np.diff(x)
        partial_nodes = self.rhs(x, y)
        midpoint_direction = -step[None, :]*(partial_nodes[:, 1:]-partial_nodes[:, :-1])/8
        midpoint_x = (x[:-1]+x[1:])/2
        partial_middle = (self.rhs(midpoint_x, midpoint_y)+
                          self.state_jvp(midpoint_x, midpoint_y, midpoint_direction))
        interior = -step[None, :]*(partial_nodes[:, :-1]+4*partial_middle+
                                   partial_nodes[:, 1:])/6
        # Original Robin rows have no explicit lambda term: the full lift and
        # both radial jets vanish strictly before the actual short-bridge cut.
        if not self.flow.end > self.window[1]*self.flow.prefix_end:
            raise ValueError("The literal complete lift does not vanish at the cut")
        boundary = np.r_[-self.inlet, np.zeros(len(self.p))]
        return np.r_[interior.ravel(order="F"), boundary]
