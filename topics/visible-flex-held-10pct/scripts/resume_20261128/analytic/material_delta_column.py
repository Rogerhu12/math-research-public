"""Analytical additive-delta RHS column on the original R53 design chart.

The complete original multistage profile, moving physical s(t), normalized
angular chart, finite GL64 ShortBridge radius, exact core/reference lift,
Frenet root and convection are differentiated. The primary support, all high
controls, computational t and full unknown Y are fixed. This standalone
column changes no solver and grants no acceptance. It must first be compared
with the whole original RHS differences on actual source fields.
"""
import numpy as np


def xyz(value):
    value = np.asarray(value)
    return np.stack((value.real, value.imag, np.zeros_like(value.real)), axis=-1)


class OriginalDeltaColumn:
    def __init__(self, obj, p, window=(.5, .9)):
        if obj.fixed or obj.cfg.get("ramp_law") != "held10_multistage_flat_v1":
            raise ValueError("Require the original additive-delta multistage design")
        obj.initial(p)
        self.obj, self.p = obj, np.asarray(p, float).copy()
        self.flow, self.core, self.window = obj.flow(p[0]), obj._core, tuple(window)
        self.delta = float(obj.cfg["delta"]+p[0])
        f = self.flow
        if (not 0 < self.delta or f.prefix_end != f.period
                or not 0 < window[0] < window[1] < 1
                or not hasattr(f.bridge, "g") or len(f.bridge.g) != 64
                or f.cfg["prefix_bridge"] != dict(kind="turn_plateau_v1", curvature=4, peak_fraction=.2)):
            raise ValueError("This column's original source contracts differ")
        self.prefix_derivative = f.prefix_end/self.delta
        self.end_derivative = self.prefix_derivative

    def moving_chart(self, t):
        obj, f = self.obj, self.flow
        t = np.asarray(t, float)
        s, ds = obj.chart(t, self.p[0])
        join = obj.chart_join
        u = np.clip((t-join)/(1-join), 0., 1.)
        S = u**3*(10-15*u+6*u*u)
        Sp = 30*u*u*(1-u)**2
        r_delta = self.prefix_derivative/obj.chart_reference_prefix
        s_delta = np.where(t <= join, t*self.prefix_derivative/join,
            self.prefix_derivative+f.bridge.L*r_delta*(u-S))
        ds_delta = np.where(t <= join, self.prefix_derivative/join,
            f.bridge.L/(1-join)*r_delta*(1-Sp))
        return s, ds, s_delta, ds_delta

    @staticmethod
    def finite_integral_derivative(bridge, u, part):
        """Derivative of the literal GL64 expression, including its leading u."""
        u = np.asarray(u, float).reshape(-1)
        nodes = (1+bridge.g)/2
        x = u[:, None]*nodes[None, :]
        if part == 0:
            phase = bridge.peak*(3*x*x-2*x*x*x)
            phase_x = 6*bridge.peak*x*(1-x)
        elif part == 2:
            phase = bridge.peak-bridge.eps*x*x
            phase_x = -2*bridge.eps*x
        else:
            raise ValueError("The literal ShortBridge has only the first and last integral pieces")
        return .5*(np.sin(phase)@bridge.gw)+u/2*((np.cos(phase)*phase_x*nodes)@bridge.gw)

    def radius_columns(self, t, s, s_delta):
        f, delta = self.flow, self.delta
        a, ap, app = f.profile(s)
        a_delta = (a-1)/delta
        ap_delta = np.zeros_like(s)
        on_bridge = t > self.obj.chart_join
        if np.any(on_bridge):
            bridge = f.bridge
            z = s[on_bridge]-f.prefix_end
            z_delta = s_delta[on_bridge]-self.prefix_derivative
            u = np.clip(z/bridge.L1, 0., 1.)
            v = np.clip((z-bridge.L1-bridge.L2)/bridge.L3, 0., 1.)
            # The value definition clips its integral arguments. At the two
            # internal joins, left/right derivatives agree to quadrature and
            # floating error; the original finite difference remains the check.
            first = (z > 0) & (z <= bridge.L1)
            plateau = (z > bridge.L1) & (z <= bridge.L1+bridge.L2)
            last = (z > bridge.L1+bridge.L2) & (z < bridge.L)
            da_dz = -(first*self.finite_integral_derivative(bridge, u, 0)+
                plateau*np.sin(bridge.peak)+last*self.finite_integral_derivative(bridge, v, 2))
            a_delta[on_bridge] = da_dz*z_delta
            phase, phase_s = bridge.angle(z)
            ap_delta[on_bridge] = -np.cos(phase)*phase_s*z_delta
        return a, ap, app, a_delta, ap_delta

    def angle_columns(self, s, s_delta, N):
        f = self.flow
        x = s/f.end
        x_delta = (s_delta-x*self.end_derivative)/f.end
        h, hx, hxx = (f.spline(x, order) for order in range(3))
        u = np.clip((x-.75)/.25, 0., 1.)
        S = u**3*(10-15*u+6*u*u)
        Sx = 30*u*u*(1-u)**2/.25
        Sxx = 60*u*(1-u)*(1-2*u)/.25**2
        c, cx, cxx = 1-S, -Sx, -Sxx
        e = f.warp_e*h*c
        ex = f.warp_e*(hx*c+h*cx)
        exx = f.warp_e*(hxx*c+2*hx*cx+h*cxx)
        e_delta = ex*x_delta
        ep = ex/f.end
        ep_delta = exx*x_delta/f.end-ex*self.end_derivative/f.end**2
        psi = 2*np.pi*np.arange(N)/N
        sn, co = np.sin(3*psi)[None, :], np.cos(3*psi)[None, :]
        theta = psi[None, :]-e[:, None]*sn/3
        theta_delta = -e_delta[:, None]*sn/3
        rho, rhop = 1-e[:, None]*co, 3*e[:, None]*sn
        rho_delta, rhop_delta = -e_delta[:, None]*co, 3*e_delta[:, None]*sn
        theta_s = -ep[:, None]*sn/3
        theta_s_delta = -ep_delta[:, None]*sn/3
        v_delta = (theta_s_delta*rho-theta_s*rho_delta)/rho**2
        return theta, theta_delta, rho, rhop, rho_delta, rhop_delta, theta_s, theta_s_delta, v_delta

    def rhs(self, t, y):
        obj, f = self.obj, self.flow
        if obj._core is not self.core or obj.flow(self.p[0]) is not self.flow:
            raise ValueError("Do not reuse a delta column after changing its base core or Flow")
        t = np.asarray(t, float)
        s, ds, sd, dsd = self.moving_chart(t)
        a, ap, _, ad, apd = self.radius_columns(t, s, sd)
        answer = np.empty_like(y)
        for first in range(0, len(t), 64):
            sl = slice(first, first+64)
            # This original call both retains the domain guard and fills the
            # source's exact-lift cache at the actual full RHS angular grid.
            frame = f.frame(s[sl], obj.q*y[:, sl])
            N = f.B.shape[1]
            H, H1, H2 = f.exact_lift_cache[N]
            theta, td, rho, rhop, rd, rpd, ts, tsd, vd = self.angle_columns(s[sl], sd[sl], N)
            aa, av = a[sl, None], ap[sl, None]
            aad, avd = ad[sl, None], apd[sl, None]
            z = np.exp(1j*theta)
            d1 = xyz((1j*(aad*rho+aa*rd)-aa*rho*td)*z)
            d2 = xyz((aad*(1j*rhop-rho*rho)+aa*(1j*rpd-2*rho*rd)+
                      1j*aa*td*(1j*rhop-rho*rho))*z)
            gs_delta = xyz((avd+1j*(aad*ts+aa*tsd)+1j*td*(av+1j*aa*ts))*z)
            lo, hi = self.window
            span = (hi-lo)*f.prefix_end
            xx = np.clip((s[sl]-lo*f.prefix_end)/span, 0., 1.)
            chi = 1-xx**3*(10-15*xx+6*xx*xx)
            chip = -30*xx*xx*(1-xx)**2/span
            hd = ad[sl]*chi
            hpd = -chip/self.delta
            d1 += hd[:, None, None]*H1
            d2 += hd[:, None, None]*H2
            gs_delta += hpd[:, None, None]*H
            alpha_explicit = (-avd/aa+av*aad/aa**2)/frame["kap"]
            beta_explicit = -frame["alpha"]*alpha_explicit/frame["beta"]
            velocity_delta = (f.frame_jvp(frame, d1, d2)+
                alpha_explicit[:, :, None]*frame["N"]+
                beta_explicit[:, :, None]*frame["Bin"]+
                vd[:, :, None]*frame["d"]+frame["geo"]["v"][:, :, None]*d1)
            base_rhs = f.project(frame["V"]-frame["geo"]["s1"], f.B)/obj.q
            partial_rhs = f.project(velocity_delta-gs_delta, f.B)/obj.q
            answer[:, sl] = dsd[sl][None, :]*base_rhs+ds[sl][None, :]*partial_rhs
        return answer

    def state_jvp(self, t, y, direction):
        """The original full state derivative, including angular convection."""
        obj, f = self.obj, self.flow
        s, ds = obj.chart(t, self.p[0])
        answer = np.empty_like(y)
        for first in range(0, len(s), 64):
            sl = slice(first, first+64)
            frame = f.frame(s[sl], obj.q*y[:, sl])
            d1 = obj.q*f.values(direction[:, sl], f.B1)
            d2 = obj.q*f.values(direction[:, sl], f.B2)
            velocity = f.frame_jvp(frame, d1, d2)+frame["geo"]["v"][:, :, None]*d1
            answer[:, sl] = ds[sl][None, :]*f.project(velocity, f.B)/obj.q
        return answer

    def collocation(self, x, y, midpoint_y):
        """The complete F_delta with its original cubic-midpoint dependence."""
        h = np.diff(x)
        nodes = self.rhs(x, y)
        midpoint_x = (x[:-1]+x[1:])/2
        midpoint_direction = -h[None, :]*(nodes[:, 1:]-nodes[:, :-1])/8
        middle = (self.rhs(midpoint_x, midpoint_y)+
                  self.state_jvp(midpoint_x, midpoint_y, midpoint_direction))
        interior = -h[None, :]*(nodes[:, :-1]+4*middle+nodes[:, 1:])/6
        # At the inlet all s/end and profile changes vanish. At the physical
        # cut, the original linear Robin equation uses fixed physical data;
        # the complete lift and two angular-chart jets are already zero.
        boundary = np.zeros(self.obj.n+self.obj.M)
        return np.r_[interior.ravel(order="F"), boundary]
