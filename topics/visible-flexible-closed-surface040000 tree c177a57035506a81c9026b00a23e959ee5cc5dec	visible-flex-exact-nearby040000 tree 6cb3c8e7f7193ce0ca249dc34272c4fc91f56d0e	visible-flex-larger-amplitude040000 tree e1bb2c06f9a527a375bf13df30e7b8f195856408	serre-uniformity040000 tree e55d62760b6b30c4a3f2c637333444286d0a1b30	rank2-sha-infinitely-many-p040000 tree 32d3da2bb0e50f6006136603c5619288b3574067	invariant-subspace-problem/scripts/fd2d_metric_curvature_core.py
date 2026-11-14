#!/usr/bin/env python3
"""R116 fixed-perimeter central curvature family, based on the R115 seed.

The mathematical seed is A=7/5, B=1/2, support p1=1/200.  Material u has
speed a0 for every d, and n_d(u)=n_seed(u)+sum_j d_j*cos(2*j*u).  Numerical
evaluation uses longdouble arithmetic and finite Gauss quadrature; it is
not an interval certificate or a solution of the complete surface BVP.

The GC column convention is [n,m,X(3),e1(3),e2(3),N(3)].  N=e1 cross e2
is the inward planar normal at the upper central inlet, and n is positive.
"""
from __future__ import annotations
import os
for _thread_variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_thread_variable] = '1'
from fractions import Fraction
from functools import lru_cache
import numpy as np
import mpmath as mp

LD = np.longdouble
PI = np.arccos(LD(-1))
PERIOD = 2*PI
HALF_PI = PI/2
EPS = np.finfo(LD).eps


def exact_rational(value):
    """Preserve an incoming binary floating value, or parse an exact string."""
    if isinstance(value, Fraction):
        return value
    if isinstance(value, str):
        return Fraction(value)
    if hasattr(value, 'as_integer_ratio'):
        return Fraction(*value.as_integer_ratio())
    return Fraction(value)


def to_ld(value):
    q = exact_rational(value)
    return LD(q.numerator)/LD(q.denominator)


@lru_cache(maxsize=12)
def gauss_rule(order):
    """Legendre rule on [0,1], Newton evaluated in the working precision."""
    if order < 4:
        raise ValueError('Gauss order must be at least four')
    i = np.arange(1, order+1, dtype=LD)
    x = np.cos(PI*(i-LD('0.25'))/(LD(order)+LD('0.5')))
    for _ in range(40):
        p0, p1 = np.ones_like(x), x.copy()
        for k in range(2, order+1):
            p0, p1 = p1, ((2*k-1)*x*p1-(k-1)*p0)/k
        dp = order*(x*p1-p0)/(x*x-1)
        step = p1/dp
        x -= step
        if np.max(abs(step)) <= 4*EPS:
            break
    p0, p1 = np.ones_like(x), x.copy()
    for k in range(2, order+1):
        p0, p1 = p1, ((2*k-1)*x*p1-(k-1)*p0)/k
    dp = order*(x*p1-p0)/(x*x-1)
    w = 2/((1-x*x)*dp*dp)
    # Symmetry is part of the rule definition, not an estimated small mode.
    x = (x-x[::-1])/2
    w = (w+w[::-1])/2
    ids = np.argsort(x)
    points, weights = (x[ids]+1)/2, w[ids]/2
    points.flags.writeable = weights.flags.writeable = False
    return points, weights


class SupportSeed:
    """The exact R115 p1=1/200 curve, numerically represented in longdouble.

    Its normal-angle arclength is inverted using a checked monotone bracket.
    Quadrature is used only for numerical evaluation of the known integral.
    The exact a0 is defined by the complete elliptic integral, independently
    of the quadrature table; it does not depend on the curvature parameters.
    """
    def __init__(self, normal_panels=64, quadrature_order=24):
        self.A, self.B, self.p = LD(7)/5, LD(1)/2, LD(1)/200
        with mp.workdps(80):
            a = mp.mpf(7)/5
            self.a0 = LD(str(2*a*mp.ellipe(1-(mp.mpf(1)/2/a)**2)/mp.pi))
        self.panels, self.order = int(normal_panels), int(quadrature_order)
        if self.panels < 8:
            raise ValueError('At least eight seed quadrature panels are required')
        self.gx, self.gw = gauss_rule(self.order)
        self.edges = np.linspace(LD(0), HALF_PI, self.panels+1, dtype=LD)
        self.width = HALF_PI/self.panels
        phi = self.edges[:-1, None]+self.width*self.gx
        rho = self._ellipse_rho(phi)
        panel = self.width*np.sum(rho*self.gw, axis=1, dtype=LD)
        self.arc_nodes = np.concatenate((np.zeros(1, dtype=LD), np.cumsum(panel, dtype=LD)))
        self.quarter_arc_quadrature_discrepancy = self.arc_nodes[-1]-self.a0*HALF_PI
        # This endpoint is an exact identity of the analytic seed.
        self.arc_nodes[-1] = self.a0*HALF_PI
        self.seed_arc_nodes = self.arc_nodes-LD(3)*self.p*np.sin(2*self.edges)/2
        self.seed_arc_nodes[0], self.seed_arc_nodes[-1] = 0, self.a0*HALF_PI
        if np.any(np.diff(self.seed_arc_nodes) <= 0):
            raise ArithmeticError('The numerical seed arclength table is not monotone')

    def _ellipse_rho(self, phi):
        h = np.sqrt((self.A*np.cos(phi))**2+(self.B*np.sin(phi))**2)
        return (self.A*self.B)**2/h**3

    def ellipse_arc_quarter(self, phi):
        phi = np.asarray(phi, dtype=LD)
        j = np.minimum(np.maximum(np.floor(phi/self.width).astype(int), 0), self.panels-1)
        width = phi-self.edges[j]
        nodes = self.edges[j, None]+width[..., None]*self.gx
        result = self.arc_nodes[j]+width*np.sum(self._ellipse_rho(nodes)*self.gw, axis=-1, dtype=LD)
        return np.where(phi == 0, LD(0), np.where(phi == HALF_PI, self.a0*HALF_PI, result))

    @staticmethod
    def quarter_reduce(angle):
        wrapped = np.mod(np.asarray(angle, dtype=LD), PERIOD)
        quadrant = np.minimum(np.floor(wrapped/HALF_PI).astype(int), 3)
        local = wrapped-quadrant*HALF_PI
        reduced = np.where(quadrant % 2, HALF_PI-local, local)
        return np.clip(reduced, 0, HALF_PI), quadrant

    def evaluate(self, u):
        u = np.asarray(u, dtype=LD)
        reduced, quadrant = self.quarter_reduce(u)
        target = self.a0*reduced
        j = np.clip(np.searchsorted(self.seed_arc_nodes, target, side='right')-1, 0, self.panels-1)
        lo, hi = self.edges[j].copy(), self.edges[j+1].copy()
        phi = lo+(hi-lo)*(target-self.seed_arc_nodes[j])/(self.seed_arc_nodes[j+1]-self.seed_arc_nodes[j])
        at0, at1 = reduced == 0, reduced == HALF_PI
        tolerance = 24*EPS*np.maximum(LD(1), abs(target))
        for iteration in range(32):
            residual = self.ellipse_arc_quarter(phi)-LD(3)*self.p*np.sin(2*phi)/2-target
            residual = np.where(at0 | at1, LD(0), residual)
            done = abs(residual) <= tolerance
            if np.all(done):
                break
            lo = np.where((residual < 0) & ~done, phi, lo)
            hi = np.where((residual > 0) & ~done, phi, hi)
            rho = self._ellipse_rho(phi)-3*self.p*np.cos(2*phi)
            trial = phi-residual/rho
            bad = (trial <= lo) | (trial >= hi) | ~np.isfinite(trial)
            phi = np.where(done, phi, np.where(bad, (lo+hi)/2, trial))
        phi = np.where(at0, LD(0), np.where(at1, HALF_PI, phi))
        residual = self.ellipse_arc_quarter(phi)-LD(3)*self.p*np.sin(2*phi)/2-target
        residual = np.where(at0 | at1, LD(0), residual)
        if np.max(abs(residual), initial=LD(0)) > 128*EPS*np.maximum(LD(1), np.max(abs(target), initial=LD(0))):
            raise ArithmeticError('Seed arclength inversion did not converge')
        co, si = np.cos(phi), np.sin(phi)
        co, si = np.where(at1, LD(0), co), np.where(at0, LD(0), si)
        h0 = np.sqrt((self.A*co)**2+(self.B*si)**2)
        hp0 = (self.B**2-self.A**2)*si*co/h0
        rho0 = (self.A*self.B)**2/h0**3
        h = h0+self.p*np.cos(2*phi)
        hp = hp0-2*self.p*np.sin(2*phi)
        rho = rho0-3*self.p*np.cos(2*phi)
        rhop = -3*rho0*hp0/h0+6*self.p*np.sin(2*phi)
        sx = np.where((quadrant == 0) | (quadrant == 3), LD(1), LD(-1))
        sy = np.where(quadrant < 2, LD(1), LD(-1))
        z = np.zeros_like(u)
        outward = np.stack((sx*co, sy*si, z), axis=-1)
        tangent = np.stack((-sy*si, sx*co, z), axis=-1)
        X = np.stack((sx*(h*co-hp*si), sy*(h*si+hp*co), z), axis=-1)
        rhop = np.where(quadrant % 2, -rhop, rhop)
        return dict(X=X, T=tangent, N=-outward, n=1/rho,
                    n_u=-self.a0*rhop/rho**3, rho=rho,
                    arc_residual=residual, arc_iterations=iteration+1)

    def reference_coordinate(self, theta):
        """ONE original-ellipse eccentric angle, shared by every d and seed.

        This is not a parameter-dependent normal angle or an eccentric angle
        of the non-elliptic support seed.  Its speed is ell_E(theta).
        """
        theta = np.asarray(theta, dtype=LD)
        turns = np.floor(theta/PERIOD)
        wrapped = theta-turns*PERIOD
        ct, st = np.cos(wrapped), np.sin(wrapped)
        phi = np.mod(np.arctan2(self.A*st, self.B*ct), PERIOD)
        reduced, quadrant = self.quarter_reduce(phi)
        small = self.ellipse_arc_quarter(reduced)
        quarter = self.a0*HALF_PI
        arc = np.select((quadrant == 0, quadrant == 1, quadrant == 2),
                        (small, 2*quarter-small, 2*quarter+small), 4*quarter-small)
        ell = np.sqrt((self.A*st)**2+(self.B*ct)**2)
        ell_prime = (self.A**2-self.B**2)*st*ct/ell
        return dict(u=turns*PERIOD+arc/self.a0, u_theta=ell/self.a0,
                    u_theta_theta=ell_prime/self.a0, ell_reference=ell)


class CurvatureCore:
    """A fixed material-u curve and its exact analytic parameter derivatives."""
    def __init__(self, coefficients=(), *, seed=None, panels=None, quadrature_order=20):
        self.exact_coefficients = tuple(exact_rational(x) for x in coefficients)
        self.d = np.array([to_ld(x) for x in self.exact_coefficients], dtype=LD)
        self.J = len(self.d)
        self.modes = 2*np.arange(1, self.J+1, dtype=LD)
        self.seed = SupportSeed() if seed is None else seed
        self.a0 = self.seed.a0
        self.T0_exact = sum(map(abs, self.exact_coefficients), Fraction())
        if self.T0_exact >= Fraction(200, 787):
            raise ValueError('The sufficient strictly positive curvature domain was left')
        self.panels = max(64, 4*self.J) if panels is None else int(panels)
        if self.panels < 1:
            raise ValueError('Positive quadrature panel count required')
        self.order = int(quadrature_order)
        self.gx, self.gw = gauss_rule(self.order)
        self.width = PI/self.panels
        self.edges = np.linspace(LD(0), PI, self.panels+1, dtype=LD)
        self.full_u = self.edges[:-1, None]+self.width*self.gx
        self._full_frame = None
        self._partial_cache = None

    def _basis(self, u):
        u = np.mod(np.asarray(u, dtype=LD), PERIOD)
        phase = u[..., None]*self.modes
        return np.cos(phase), np.sin(phase)*(self.a0/self.modes) if self.J else phase

    def _frame(self, u):
        u = np.asarray(u, dtype=LD)
        seed = self.seed.evaluate(u)
        cosine, qbasis = self._basis(u)
        delta = qbasis @ self.d
        sd, cd = np.sin(delta), np.cos(delta)
        T = cd[..., None]*seed['T']+sd[..., None]*seed['N']
        N = cd[..., None]*seed['N']-sd[..., None]*seed['T']
        difference = (-2*np.sin(delta/2)**2)[..., None]*seed['T']+sd[..., None]*seed['N']
        n = seed['n']+cosine @ self.d
        phase = np.mod(u, PERIOD)[..., None]*self.modes
        n_u = seed['n_u']-np.sin(phase) @ (self.modes*self.d)
        return dict(seed=seed, T=T, N=N, difference=difference, n=n, n_u=n_u,
                    cosine=cosine, qbasis=qbasis, delta_angle=delta)

    def _integration_frames(self, u):
        u = np.asarray(u, dtype=LD)
        key = (u.shape, u.tobytes())
        if self._full_frame is None:
            self._full_frame = self._frame(self.full_u)
        if self._partial_cache is not None and self._partial_cache[0] == key:
            return self._full_frame, self._partial_cache[1]
        wrapped = np.mod(u, PERIOD)
        sign = np.where(wrapped >= PI, LD(-1), LD(1))
        reduced = np.where(wrapped >= PI, wrapped-PI, wrapped)
        j = np.clip(np.floor(reduced/self.width).astype(int), 0, self.panels-1)
        width = reduced-self.edges[j]
        partial_u = self.edges[j, None]+width[..., None]*self.gx
        partial = dict(frame=self._frame(partial_u), indices=j, width=width, sign=sign)
        self._partial_cache = (key, partial)
        return self._full_frame, partial

    def _centered_integral(self, full_values, partial_values, partial):
        full = self.width*np.sum(full_values*self.gw[:, None], axis=1, dtype=LD)
        cumulative = np.concatenate((np.zeros((1, 3), dtype=LD), np.cumsum(full, axis=0, dtype=LD)))
        small = partial['width'][..., None]*np.sum(partial_values*self.gw[:, None], axis=-2, dtype=LD)
        return (cumulative[partial['indices']]+small-cumulative[-1]/2)*partial['sign'][..., None]

    @staticmethod
    def gc_columns(data):
        return np.concatenate((data['n'][..., None], data['m'][..., None], data['X'],
                               data['e1'], data['e2'], data['N']), axis=-1)

    def evaluate(self, u):
        u = np.asarray(u, dtype=LD)
        point = self._frame(u)
        if np.any(self.d != 0):
            full, partial = self._integration_frames(u)
            correction = self.a0*self._centered_integral(full['difference'], partial['frame']['difference'], partial)
            X = point['seed']['X']+correction
        else:
            X = point['seed']['X'].copy()
        zero = np.zeros_like(X)
        e1 = zero.copy(); e1[..., 2] = 1
        out = dict(X=X, X_u=self.a0*point['T'],
                   X_uu=self.a0**2*point['n'][..., None]*point['N'],
                   X_s=e1, X_ss=zero.copy(), X_su=zero.copy(),
                   e1=e1, e2=point['T'], N=point['N'], n=point['n'],
                   m=np.zeros_like(u), n_u=point['n_u'], m_u=np.zeros_like(u),
                   material_u=u, seed_arc_residual=point['seed']['arc_residual'],
                   delta_angle=point['delta_angle'])
        out['gc_values'] = self.gc_columns(out)
        return out

    def jvp(self, u, direction):
        """Derivative at FIXED material u; no finite difference or FFT is used."""
        u = np.asarray(u, dtype=LD)
        v = np.asarray(direction, dtype=LD)
        if v.shape != self.d.shape:
            raise ValueError('The parameter direction has the wrong shape')
        point = self._frame(u)
        qv, dn = point['qbasis'] @ v, point['cosine'] @ v
        full, partial = self._integration_frames(u)
        fq = full['qbasis'] @ v
        pq = partial['frame']['qbasis'] @ v
        dX = self.a0*self._centered_integral(full['N']*fq[..., None],
                partial['frame']['N']*pq[..., None], partial)
        dT = point['N']*qv[..., None]
        dN = -point['T']*qv[..., None]
        zero = np.zeros_like(dX)
        out = dict(X=dX, X_u=self.a0*dT,
                   X_uu=self.a0**2*(dn[..., None]*point['N']+point['n'][..., None]*dN),
                   X_s=zero.copy(), X_ss=zero.copy(), X_su=zero.copy(),
                   e1=zero.copy(), e2=dT, N=dN, n=dn, m=np.zeros_like(u),
                   n_u=-np.sin(np.mod(u, PERIOD)[..., None]*self.modes) @ (self.modes*v),
                   m_u=np.zeros_like(u), material_u=u)
        out['gc_values'] = self.gc_columns(out)
        return out

    def parameter_jacobian(self, u):
        """Stack JVP columns as (J, *u.shape, component); JVP avoids this cost."""
        keys = ('X', 'X_u', 'X_uu', 'X_s', 'X_ss', 'X_su', 'e1', 'e2', 'N', 'n', 'm', 'n_u', 'm_u', 'gc_values')
        columns = [self.jvp(u, v) for v in np.eye(self.J, dtype=LD)]
        if not columns:
            base = self.evaluate(u)
            return {k:np.empty((0,)+base[k].shape, dtype=LD) for k in keys}
        return {k:np.stack([col[k] for col in columns]) for k in keys}

    @staticmethod
    def _add_reference_jets(out, coordinate):
        first, second = coordinate['u_theta'], coordinate['u_theta_theta']
        out['X_theta'] = out['X_u']*first[..., None]
        out['X_theta_theta'] = out['X_uu']*first[..., None]**2+out['X_u']*second[..., None]
        out['X_s_theta'] = out['X_su']*first[..., None]
        out['n_theta'] = out['n_u']*first
        out['m_theta'] = out['m_u']*first
        out.update(coordinate)
        return out

    def evaluate_reference_angle(self, theta):
        coordinate = self.seed.reference_coordinate(theta)
        return self._add_reference_jets(self.evaluate(coordinate['u']), coordinate)

    def jvp_reference_angle(self, theta, direction):
        coordinate = self.seed.reference_coordinate(theta)
        return self._add_reference_jets(self.jvp(coordinate['u'], direction), coordinate)

    def summary(self):
        weighted = sum((abs(d)/int(m) for d, m in zip(self.exact_coefficients, self.modes)), Fraction())
        s_upper = Fraction(201, 200)*weighted
        displacement_upper = Fraction(11, 7)*Fraction(201, 200)**2*weighted
        return dict(seed=dict(A_exact='7/5', B_exact='1/2', support_p1_exact='1/200'),
            a0_numeric=float(self.a0), a0_definition='2*(7/5)*E(1-(5/14)^2)/pi',
            coefficients_exact=[str(x) for x in self.exact_coefficients],
            frequencies=[int(x) for x in self.modes], T0_exact=str(self.T0_exact),
            S0_numeric=float(self.a0*to_ld(weighted)), S0_rational_upper=str(s_upper),
            shape_displacement_rational_upper=str(displacement_upper),
            curvature_lower_exact=str(Fraction(200, 787)-self.T0_exact),
            curvature_upper_exact=str(Fraction(1400, 229)+self.T0_exact),
            central_window_proved_by_rational_bounds=self.T0_exact <= Fraction(1, 20) and s_upper <= Fraction(1, 2000),
            quadrature_panels=self.panels, quadrature_order=self.order,
            seed_quarter_arc_quadrature_discrepancy=float(self.seed.quarter_arc_quadrature_discrepancy),
            numeric_precision_mantissa_bits=int(np.finfo(LD).nmant),
            fixed_material_metric='ds^2+a0^2*du^2 on the central cylinder, independent of d',
            reference_coordinate='ONE original-ellipse eccentric theta; u_theta=ell_E(theta)/a0',
            gc_column_order=['n', 'm', 'X_x', 'X_y', 'X_z', 'e1_x', 'e1_y', 'e1_z',
                             'e2_x', 'e2_y', 'e2_z', 'N_x', 'N_y', 'N_z'],
            exact_analytic_central_family=True, numerical_values_are_interval_certified=False,
            complete_BVP_solved=False, closed_surface=False, full_reach_or_held_proved=False)
