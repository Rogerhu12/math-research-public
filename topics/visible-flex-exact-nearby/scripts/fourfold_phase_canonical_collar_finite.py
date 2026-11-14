#!/usr/bin/env python3
"""Finite physical canonical coordinates for the actual positive root collar.

Work in progress: the CLI is an explicitly local directed diagnostic.  It
does not declare a complete angular or radial cover.  The finite coordinates
are defined by their true root coefficient functions, not by rounding those
functions to the midpoints of the enclosing balls.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import time

from flint import acb, acb_series, arb, ctx

from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_interval import series_real, series_constant
from fourfold_phase_beta_parameter_germ import ParameterGermBallTarget, provenance
from fourfold_phase_canonical_root_jets import (
    CanonicalRootModel, along_shear, cross, derivative, dot, jet_function, jet_sin_cos,
    real_jet, root_family, root_series, time_function, trim,
)
from fourfold_time_angle_jets import TimeAngleJet as Jet


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def series_trim(value, n):
    if n < 1 or n > value.prec:
        raise ValueError("unknown angular coefficient requested")
    return acb_series([value[j] for j in range(n)], prec=n)


def series_sum(terms):
    if not terms:
        raise ValueError("empty sum needs a known angular precision")
    n = min(v.prec for v in terms)
    return sum((series_trim(v, n) for v in terms),
               acb_series([acb(0)], prec=n))


def series_product(left, right):
    n = min(left.prec, right.prec)
    return series_trim(left, n)*series_trim(right, n)


def radial_series(value, i):
    if not 0 <= i < value.m:
        raise ValueError("unknown radial coefficient requested")
    return acb_series([value.coefficient(i, j) for j in range(value.n)], prec=value.n)


def angular_lift(value, m, n):
    if n > value.prec:
        raise ValueError("unknown angular coefficient in finite chart")
    return Jet([[value[j]]+[acb(0)]*(m-1) for j in range(n)],
               time_precision=m, angle_precision=n)


def align(*values):
    m, n = min(v.m for v in values), min(v.n for v in values)
    return [trim(v, m, n) for v in values]


def mul(left, right):
    a, b = align(left, right)
    return a*b


def add(*values):
    values = align(*values)
    return sum(values[1:], values[0])


def physical_radial_derivative(value, scale):
    return -derivative(value, "radial")/scale


def polynomial_shift(value, center, precision):
    """Exact finite polynomial shift, not an uncharged analytic composition."""
    if precision > value.prec:
        raise ValueError("shift requested more coefficients than known")
    out = []
    for j in range(precision):
        total = acb(0)
        for k in range(value.prec-1, j-1, -1):
            total = total*center+math.comb(k, j)*value[k]
        out.append(total)
    return acb_series(out, prec=precision)


def cauchy_shift_tail(full_modulus, physical_radius, scale, offset, start, order):
    """Tail in the local native time coefficient after a nonzero real shift.

    The exact series variable is w=(t-r)/scale.  For q=|offset|/R,
    sum_{n>=P} binom(n,j) q^(n-j) is the j-th divided derivative
    of q^P/(1-q), evaluated by its finite Leibniz formula.
    """
    if start <= order:
        raise ValueError("the retained polynomial must exceed derivative order")
    q = (abs(offset).upper()/physical_radius).upper()
    if not q < 1:
        raise ValueError("real shifted collar exceeds the proved Cauchy disk")
    geometric = sum((math.comb(start, a)*q**(start-a)/(1-q)**(order-a+1)
                     for a in range(order+1)), arb(0))
    return (full_modulus*(scale/physical_radius)**order*geometric).upper()


class PhysicalRootGeometry(CanonicalRootModel):
    """A higher finite jet of exactly the same native scalar-germ object."""

    def __init__(self, object_path, half_width, root_certificate, *, nodes=512,
                 radial_precision=10, angle_precision=16, scale=Fraction(1, 1024)):
        self.m, self.n = radial_precision, angle_precision
        self.scale = exact_arb(scale)
        self.target = ParameterGermBallTarget(object_path, half_width, nodes, nodes)
        self.root, self.spans = root_family(self.target, root_certificate)
        # High physical derivatives of a shifted analytic germ need a much
        # longer polynomial than function-value evaluation alone.
        self.polynomial_order = 80
        self.offset = None
        self._states = {}
        self.prepare_offset(arb(0))
        old = ctx.cap
        ctx.cap = max(self.m+3, self.n+3)
        try:
            self.root_kappa = acb_series(
                [-self.K[j+1]/self.scale for j in range(self.m-1)], prec=self.m-1)
        finally:
            ctx.cap = old
        if not self.root_kappa[0].real > 0:
            raise ValueError("actual root deflation lost positivity")

    def prepare_offset(self, offset):
        offset = arb(offset)
        key = offset.repr()
        if key in self._states:
            state = self._states[key]
            for name, value in state.items():
                setattr(self, name, value)
            return
        center = self.root+offset
        # Real inputs must remain inside the exact common actual root germ.
        # Larger Cauchy disks below refer only to that polynomial germ.
        for span in self.spans:
            sign = span["sign"]
            if not (exact_arb(Fraction(span["left"])) < sign*center
                    and sign*center < exact_arb(Fraction(span["right"]))):
                raise ValueError("finite collar leaves an actual root scalar span")
        old = ctx.cap
        ctx.cap = max(self.m+3, self.n+3, self.polynomial_order if offset.is_zero() else 1)
        try:
            if offset.is_zero():
                budget = self.target.analytic_input_budget(
                    center, arb(".003"), arb(".32"), arb(".0025"))
                coefficient, radius, E, C, K = self.target.target(center, self.scale, budget)
                self.root_coefficient, self.root_E = coefficient, E
                self.root_budget = budget
                primitive_fees = [(budget["field_errors"][0]*(self.scale/budget["radial_radius"])**j).upper()
                                  for j in range(self.m)]
            else:
                budget = self.root_budget
                w0 = -acb(offset)/self.scale
                coefficient = self.root_coefficient.copy()
                for index in __import__("numpy").ndindex(coefficient.shape):
                    coefficient[index] = polynomial_shift(self.root_coefficient[index], w0, self.m)
                radius = self.target.scalars(acb(center), -self.scale)[2]
                out_precision = self.m+3
                shifted_E = polynomial_shift(self.root_E, w0, out_precision)
                E = acb_series([
                    acb(shifted_E[j].real+arb(0, cauchy_shift_tail(
                        budget["E_full_bound"], budget["E_radius"], self.scale, offset,
                        self.root_E.prec, j)))
                    for j in range(out_precision)], prec=out_precision)
                ar, arr = -radius.derivative()/self.scale, radius.derivative().derivative()/self.scale**2
                Er = -E.derivative()/self.scale
                C = ar*Er-2*arr*E
                K = C/(2*radius*E**2)
                q = (abs(offset).upper()/budget["radial_radius"]).upper()
                if not q < 1:
                    raise ValueError("primitive shift leaves its true analytic germ disk")
                full = budget["finite_field_bounds"][0]+budget["field_errors"][0]
                primitive_fees = []
                for j in range(self.m):
                    infinite = budget["field_errors"][0]*(self.scale/budget["radial_radius"])**j/(1-q)**(j+1)
                    tail = cauchy_shift_tail(full, budget["radial_radius"], self.scale, offset,
                                             self.root_coefficient[0, 0].prec, j)
                    primitive_fees.append((infinite+tail).upper())
            beta, gamma, _, _ = self.target.scalars(acb(center), -self.scale)
        finally:
            ctx.cap = old
        state = dict(center=center, offset=offset, budget=budget,
                     coefficient=coefficient, radius=radius, E=E, C=C, K=K,
                     beta=beta, gamma=gamma, primitive_fees=primitive_fees)
        self._states[key] = state
        for name, value in state.items():
            setattr(self, name, value)

    def position(self, angle, tangent):
        """True primitive with charged shifted radial series and angular ODE."""
        old, ctx.cap = ctx.cap, self.m
        try:
            first = [series_constant(0, self.m) for _ in range(3)]
            for k, frequency in enumerate(self.target.frequency):
                phase = (acb(0, frequency)*acb(angle.mid())).exp()
                for component in range(3):
                    first[component] += acb_series(
                        [self.coefficient[k, component][j] for j in range(self.m)], prec=self.m)*phase
            first = [acb_series([acb(first[c][j].real+arb(0, self.primitive_fees[j]))
                                 for j in range(self.m)], prec=self.m) for c in range(3)]
            aT = [self.lift(self.radius)*v for v in tangent]
            h = angle.rad().upper()
            padded = [[], [], []]
            for i in range(self.m):
                forcing = [aT[j].coefficient(i, 0).real for j in range(3)]
                sizes = [abs(forcing[0]+first[1][i].real).upper(),
                         abs(forcing[1]-first[0][i].real).upper(), abs(forcing[2]).upper()]
                fees = [(h*sizes[0]+h*h*sizes[1]/2).upper(),
                        (h*sizes[1]+h*h*sizes[0]/2).upper(), (h*sizes[2]).upper()]
                for j in range(3):
                    padded[j].append(acb(first[j][i].real+arb(0, fees[j])))
            first = [acb_series(padded[j], prec=self.m) for j in range(3)]
            rows = [[first[j]] for j in range(3)]
            for k in range(1, self.n):
                force = [acb_series([aT[j].coefficient(i, k-1) for i in range(self.m)], prec=self.m)
                         for j in range(3)]
                rows[0].append((force[0]+rows[1][k-1])/k)
                rows[1].append((force[1]-rows[0][k-1])/k)
                rows[2].append(force[2]/k)
            return [real_jet(Jet([[rows[j][k][i] for i in range(self.m)]
                                  for k in range(self.n)], time_precision=self.m,
                                 angle_precision=self.n)) for j in range(3)]
        finally:
            ctx.cap = old

    def principal(self, angle, *, at_root=False):
        if at_root and not self.offset.is_zero():
            raise ValueError("root quotient requested away from the true root")
        old = ctx.cap
        ctx.cap = max(self.m+3, self.n+3)
        try:
            beta, gamma = self.phases(angle)
            sb, cb = jet_sin_cos(trim(beta, self.m, self.n))
            sg, cg = jet_sin_cos(trim(gamma, self.m, self.n))
            tangent = [-sb*cg, cb*cg, sg]
            F = self.position(angle, tangent)
            m, n = self.m-1, self.n
            keep = lambda v: trim(v, m, n)
            bt, gt = keep(derivative(beta, "angle")), keep(derivative(gamma, "angle"))
            br = -trim(derivative(beta, "radial"), m, n)/self.scale
            gr = -trim(derivative(gamma, "radial"), m, n)/self.scale
            sb, cb, sg, cg = map(keep, (sb, cb, sg, cg))
            tangent = list(map(keep, tangent))
            X = [-derivative(v, "radial")/self.scale for v in F]
            F = list(map(keep, F))
            h = -sb*X[0]+cb*X[1]
            v = -cb*X[0]-sb*X[1]
            Q = cg*X[2]-sg*h
            W = real_jet(Q*Q+v*v)
            D = real_jet((1+bt)*cg*Q-gt*v)
            M = real_jet(br*cg*Q-gr*v)
            H = real_jet(dot(cross(tangent, X), F))
            for name, value in (("Fz", F[2]), ("D", D), ("W", W), ("H", H)):
                if not value.coefficient(0, 0).real > 0:
                    raise ValueError("unresolved positive actual coefficient "+name)
                constant = value.coefficient(0, 0).real
                if not 8*constant.rad() < constant.mid():
                    raise ValueError("actual principal factor needs a narrower angle/radial box: "+name)
            invD, invH = jet_function(D, "inverse"), jet_function(H, "inverse")
            alpha = real_jet(F[2]*F[2]*D*invH*invH)
            eta = real_jet(F[2]*F[2]*W*W*invD*invH*invH)
            q = real_jet(M*invD)
            Kseries = self.K
            if at_root:
                # Each actual parameter uses its own exact root.  Only this
                # exact constant is removed; every higher true jet is kept.
                Kseries = acb_series([acb(0)]+[self.K[j] for j in range(1, self.K.prec)],
                                    prec=self.K.prec)
            K = self.lift(Kseries, m=m, n=n)
            b11 = alpha
            b12 = -alpha*q
            b22 = real_jet(alpha*q*q+eta*K)
            result = dict(alpha=alpha, eta=eta, q=q, K=K,
                          B11=b11, B12=b12, B22=b22, Fz=F[2], W=W, D=D, H=H)
            if at_root:
                kappa = self.lift(self.root_kappa, m=m, n=n)
                Vstar = real_jet(kappa*W*W*invD*invD)
                logV = jet_function(kappa, "log")+2*jet_function(W, "log")-2*jet_function(D, "log")
                d = real_jet(jet_function(logV/2, "exp"))
                # Keep the exact real logarithmic branch, as in R83.
                yp = time_function(-root_series(logV, n)/2, "exp")
                result.update(kappa=kappa, Vstar=Vstar, d=d, Yprime=yp)
            return result
        finally:
            ctx.cap = old


class FiniteRootCoordinates:
    """The actual degree-six coordinate functions, with interval jet bounds.

    x=t-r, x=rho*z^2.  Only S_+ is needed because S_-(z)=S_+(-z).
    S_0 is never assigned a spurious value: only its derivative Y_0' occurs.
    """

    def __init__(self, principal, scale, degree=6):
        if degree != 6:
            raise ValueError("the current explicit matching proof uses degree six")
        self.scale, self.degree = scale, degree
        q, d, yp = principal["q"], principal["d"], principal["Yprime"]
        N = min(q.n, d.n, yp.prec)
        if q.m < degree or d.m < degree or N < 12:
            raise ValueError("insufficient actual mixed jets for degree-six chart")
        zero = lambda n: acb_series([acb(0)], prec=n)
        sigma = scale*scale.sqrt()
        S = [None, zero(N)]
        for index in range(2, 2*degree+2):
            terms = []
            for j in range(min(q.m-1, (index-2)//2)+1):
                k = index-2-2*j
                if k < 0:
                    continue
                derivative_S = yp if k == 0 else S[k].derivative()
                terms.append(2*scale*series_product(radial_series(q, j), derivative_S))
            for j in range(min(d.m-1, (index-3)//2)+1):
                k = index-3-2*j
                if k < 0:
                    continue
                derivative_S = yp if k == 0 else S[k].derivative()
                terms.append(2*sigma*series_product(radial_series(d, j), derivative_S))
            value = -series_sum(terms)/index
            if index == 3:
                # d(0)*Y_0'=1 identically in theta and in the parameter.
                # Do not lose this identity through separate interval factors.
                exact = -2*sigma/3
                if not value[0].real.contains(exact):
                    raise ValueError("root characteristic normalization is inconsistent")
                value = acb_series([acb(exact)], prec=N)
            S.append(value)
        self.S = S
        self.n = min(yp.prec, *(S[k].prec for k in range(2, 2*degree+2)))
        hcoeff = [series_trim(-3*S[2*j+3]/(2*sigma), self.n)
                  for j in range(degree)]
        # The leading coefficient is exactly one, with all angle derivatives 0.
        hcoeff[0] = acb_series([acb(1)], prec=self.n)
        hjet = Jet([[hcoeff[i][j] for i in range(degree)] for j in range(self.n)],
                   time_precision=degree, angle_precision=self.n)
        power = real_jet(jet_function(jet_function(hjet, "log")*arb(2)/3, "exp"))
        self.xi = [zero(self.n)]+[
            acb_series([scale*power.coefficient(i, j) for j in range(self.n)], prec=self.n)
            for i in range(degree)]
        self.phi_delta = [zero(self.n)]+[
            series_trim(S[2*i], self.n) for i in range(1, degree+1)]
        self.yp = series_trim(yp, self.n)

    def polynomial(self, coefficients, w, *, theta_order=0, w_order=0):
        m, n = w.m, min(w.n, *(v.prec-theta_order for v in coefficients))
        if n < 1:
            raise ValueError("unknown angular derivative of finite coordinates")
        w = trim(w, m, n)
        out = Jet.constant(0, time_precision=m, angle_precision=n)
        for k in range(len(coefficients)-1, w_order-1, -1):
            a = coefficients[k]
            for _ in range(theta_order):
                a = a.derivative()
            a = a*math.factorial(k)/math.factorial(k-w_order)
            out = out*w+angular_lift(a, m, n)
        return real_jet(out)

    def positive(self, offset, m, n):
        # Real physical offset s=r-t >=0, native local time r=center-rho*w.
        # Thus the old negative coordinate is w_old=-s/rho+w.
        n = min(n, self.n-1)
        w = Jet.constant(-offset/self.scale, time_precision=m, angle_precision=n)
        w = w+Jet.variable("time", time_precision=m, angle_precision=n)
        y = -self.polynomial(self.xi, w)
        defining_ratio = self.polynomial(self.xi[1:], w)/self.scale
        ys = self.polynomial(self.xi, w, w_order=1)/self.scale
        yt = -self.polynomial(self.xi, w, theta_order=1)
        ps = -self.polynomial(self.phi_delta, w, w_order=1)/self.scale
        pt = self.polynomial(self.phi_delta, w, theta_order=1)+angular_lift(self.yp, m, n)
        J = real_jet(ys*pt-yt*ps)
        return dict(y=y, defining_ratio=defining_ratio, ys=ys, yt=yt, ps=ps, pt=pt, J=J)


def canonical_derivative(value, chart, scale, axis):
    radial = physical_radial_derivative(value, scale)
    angular = derivative(value, "angle")
    if axis == "normal":
        numerator = add(mul(chart["pt"], radial), -mul(chart["ps"], angular))
    elif axis == "angle":
        numerator = add(-mul(chart["yt"], radial), mul(chart["ys"], angular))
    else:
        raise ValueError("unknown canonical derivative")
    return real_jet(mul(numerator, jet_function(chart["J"], "inverse")))


def root_potential_coefficients(principal, scale):
    """R83's exact formulas before converting physical theta derivatives."""
    q = principal["q"]
    logk, logz, logw, logh, logd = [
        jet_function(principal[name], "log") for name in ("kappa", "Fz", "W", "H", "D")]
    logU, logV = logk+4*logz+2*logw-4*logh, logk+2*logw-2*logd
    nf = q.n-3
    qtheta = derivative(q, "angle")
    jac = [root_series(qtheta, nf),
           root_series(along_shear(qtheta, q, scale), nf)/2,
           root_series(along_shear(along_shear(qtheta, q, scale), q, scale), nf)/6]
    def jets(value):
        a = along_shear(value, q, scale)
        b = along_shear(a, q, scale)
        c = along_shear(b, q, scale)
        return [root_series(a, nf), root_series(b, nf)/2, root_series(c, nf)/6]
    ss, vv = jets(logU), jets(logV)
    h1, h2, h3 = [vv[i]/2-jac[i] for i in range(3)]
    d1, d2, d3 = h1, h2+h1*h1/2, h3+h1*h2+h1**3/6
    cc, ee = 2*d1/5, 2*d2/7-d1*d1/25
    ff = 2*d3/9-2*d1*d2/35+4*d1**3/375
    l1 = (ss[0]-cc)/2
    l2 = (ss[1]-ee+cc*cc/2)/2
    l3 = (ss[2]-ff+cc*ee-cc**3/3)/2
    L1, L2 = l1, l2-cc*l1
    L3 = l3-2*cc*l2+(2*cc*cc-ee)*l1
    u0, w0 = root_series(logU, nf+2), root_series(logV, nf+2)
    g, b0 = -u0/4, (u0+w0)/2
    q1 = -time_function(w0, "exp")*(g.derivative().derivative()
                                    +g.derivative()**2+b0.derivative()*g.derivative())
    q1 = series_trim(q1, nf)
    return dict(v0=-L2-L1*L1/4, v1=q1-3*L3-L1*L2,
                q0=root_series(q, nf), Yprime=series_trim(principal["Yprime"], nf))


def physical_polynomial_trial(root_values, chart, offset, scale):
    """Real B,C with exactly the R53 common-root Cauchy jets."""
    v0, v1, q0, yp = [root_values[name] for name in ("v0", "v1", "q0", "Yprime")]
    v0theta = v0.derivative()
    b1 = series_sum([v1/3, -series_product(q0, v0theta)])
    c2 = series_product(v0theta, time_function(yp, "inverse"))/2
    m, n = chart["y"].m, min(chart["y"].n, v0.prec, b1.prec, c2.prec)
    s = Jet.constant(offset, time_precision=m, angle_precision=n)
    s -= scale*Jet.variable("time", time_precision=m, angle_precision=n)
    B = -angular_lift(v0, m, n)+s*angular_lift(b1, m, n)
    C = s*s*angular_lift(c2, m, n)
    return dict(trial_B=real_jet(B), trial_C=real_jet(C))


def trial_residual_coefficients(values, amplitudes, scale):
    """Full principal-free terms, kept separate by their true radial order."""
    B, C = amplitudes["trial_B"], amplitudes["trial_C"]
    dy = lambda f: canonical_derivative(f, values, scale, "normal")
    dp = lambda f: canonical_derivative(f, values, scale, "angle")
    By, Cy = dy(B), dy(C)
    Bp, Cp = dp(B), dp(C)
    Byy, Cyy = dy(By), dy(Cy)
    Bpp, Cpp = dp(Bp), dp(Cp)
    y, V = values["y"], values["V"]
    db = add(V, -B, -2*mul(y, By))
    dc = add(Cy, mul(y, Bp))
    return {
        "DB_without_Cphi": real_jet(db),
        "DB_Cphi": real_jet(2*mul(y, Cp)),
        "DC": real_jet(dc),
        "LC_normal": -Cyy, "LC_angle": -mul(y, Cpp), "LC_potential": mul(V, C),
        "LB_normal": -Byy, "LB_angle": -mul(y, Bpp), "LB_potential": mul(V, B),
        "E12_normal": dy(values["cross_error"]),
        "E12_angle": dp(values["cross_error"]),
        "E22_angle": dp(values["tangential_error"]),
        "B_y": By, "B_phi": Bp, "B_yphi": dp(By), "B_phiphi": Bpp,
        "C_y": Cy, "C_phi": Cp, "C_yphi": dp(Cy), "C_phiphi": Cpp,
        **amplitudes}


def finite_canonical_operator(principal, chart, scale):
    y, ys, yt, ps, pt, J = [chart[name] for name in ("y", "ys", "yt", "ps", "pt", "J")]
    B11, B12, B22 = [principal[name] for name in ("B11", "B12", "B22")]
    B11, B12, B22, y, ys, yt, ps, pt, J = align(B11, B12, B22, y, ys, yt, ps, pt, J)
    if not J.coefficient(0, 0).real > 0:
        raise ValueError("finite physical coordinate Jacobian is not certified positive")
    j0 = J.coefficient(0, 0).real
    if not 8*j0.rad() < j0.mid():
        raise ValueError("finite coordinate Jacobian interval is too wide")
    invJ = jet_function(J, "inverse")
    A11 = real_jet((B11*ys*ys+2*B12*ys*yt+B22*yt*yt)*invJ)
    A12 = real_jet((B11*ys*ps+B12*(ys*pt+yt*ps)+B22*yt*pt)*invJ)
    A22 = real_jet((B11*ps*ps+2*B12*ps*pt+B22*pt*pt)*invJ)
    if not A11.coefficient(0, 0).real > 0:
        raise ValueError("finite canonical principal normal coefficient is unresolved")
    a0 = A11.coefficient(0, 0).real
    if not 8*a0.rad() < a0.mid():
        raise ValueError("finite canonical normal coefficient interval is too wide")
    invA11 = jet_function(A11, "inverse")
    height = real_jet(jet_function(jet_function(A11, "log")*(-arb(1)/2), "exp"))
    C12, C22 = real_jet(A12*invA11), real_jet(A22*invA11)
    hs, ht = physical_radial_derivative(height, scale), derivative(height, "angle")
    fs = add(mul(B11, hs), mul(B12, ht))
    ft = add(mul(B12, hs), mul(B22, ht))
    div = add(physical_radial_derivative(fs, scale), derivative(ft, "angle"))
    V = -mul(mul(height, invJ), div)
    Vy = canonical_derivative(V, chart, scale, "normal")
    # P_ground(t U o Psi)=(J/t) (P_can U) o Psi, exactly.
    physical_source_factor = real_jet(J*jet_function(height, "inverse"))
    return dict(**chart, A11=A11, height=height, cross_error=C12,
                tangential_error=C22-y, V=V, Vy=Vy,
                physical_source_factor=physical_source_factor)


def jet_summary(value, *, max_radial=2, max_angle=2, scale=None):
    result = []
    for i in range(min(max_radial+1, value.m)):
        row = []
        for j in range(min(max_angle+1, value.n)):
            v = value.coefficient(i, j).real*math.factorial(i)*math.factorial(j)
            if scale is not None:
                v *= (-1/scale)**i
            row.append(ball_record(v))
        result.append(row)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    parser.add_argument("--half-width", type=Fraction, default=Fraction(1, 2500000))
    parser.add_argument("--root-certificate", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json"))
    parser.add_argument("--angle", type=Fraction, default=Fraction(0),
                        help="center physical angle as a rational multiple of pi")
    parser.add_argument("--angle-radius", type=Fraction, default=Fraction(0),
                        help="physical angle half-width, also a rational multiple of pi")
    parser.add_argument("--offset", type=Fraction, default=Fraction(0),
                        help="actual real s=r-t center")
    parser.add_argument("--offset-radius", type=Fraction, default=Fraction(0))
    parser.add_argument("--nodes", type=int, default=512)
    parser.add_argument("--bits", type=int, default=256)
    parser.add_argument("--radial-precision", type=int, default=10)
    parser.add_argument("--angle-precision", type=int, default=16)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.angle_radius < 0 or args.offset_radius < 0 or args.offset-args.offset_radius < 0:
        raise ValueError("positive collar diagnostics require nonnegative real offset range")
    ctx.prec = args.bits
    ctx.cap = max(args.radial_precision+3, args.angle_precision+3)
    start = time.monotonic()
    model = PhysicalRootGeometry(args.object, args.half_width, args.root_certificate,
                                 nodes=args.nodes, radial_precision=args.radial_precision,
                                 angle_precision=args.angle_precision)
    angle = (exact_arb(args.angle)+arb(0, exact_arb(args.angle_radius)))*arb.pi()
    offset = exact_arb(args.offset)+arb(0, exact_arb(args.offset_radius))
    root_principal = model.principal(angle, at_root=True)
    coordinates = FiniteRootCoordinates(root_principal, model.scale)
    root_values = root_potential_coefficients(root_principal, model.scale)
    model.prepare_offset(offset)
    actual = model.principal(angle, at_root=offset.is_zero())
    chart = coordinates.positive(offset, model.m-1, model.n)
    values = finite_canonical_operator(actual, chart, model.scale)
    amplitudes = physical_polynomial_trial(root_values, chart, offset, model.scale)
    residual = trial_residual_coefficients(values, amplitudes, model.scale)
    report = {
        "kind": "actual_finite_positive_canonical_collar_local_diagnostic",
        "proved_global_cover": False, "source_sha256": sha(__file__),
        "dependencies": {name: sha(Path(__file__).parent/name) for name in (
            "fourfold_phase_canonical_root_jets.py", "fourfold_time_angle_jets.py",
            "fourfold_phase_beta_parameter_germ.py", "fourfold_phase_beta_interval.py")},
        "object": provenance(model.target, args.object),
        "root_certificate_sha256": sha(args.root_certificate),
        "root": ball_record(model.root),
        "physical_angle": ball_record(angle), "physical_positive_offset": ball_record(offset),
        "root_coordinate_degree": 6, "retained_chart_angle_precision": coordinates.n,
        "root_Y_prime": ball_record(coordinates.yp[0].real),
        "coordinate_coefficients": {
            "xi_in_w": [ball_record(a[0].real) for a in coordinates.xi],
            "phi_minus_Y0_in_w": [ball_record(a[0].real) for a in coordinates.phi_delta]},
        "operator_jet_bounds": {name: jet_summary(value, max_radial=5, max_angle=2,
                                                 scale=model.scale)
                                for name, value in values.items()},
        "trial_residual_jet_bounds": {name: jet_summary(value, max_radial=7, max_angle=2,
                                                       scale=model.scale)
                                      for name, value in residual.items()},
        "root_potential_values": {name: [ball_record(value[j].real*math.factorial(j))
                                         for j in range(min(6, value.prec))]
                                 for name, value in root_values.items()},
        "seconds": time.monotonic()-start,
        "limitations": [
            "A single specified real angle/offset box only, not a full circle or collar certificate.",
            "The formal root matching theorem and complete continuous cover must be recorded separately.",
            "No complete R53 residual constant or feedback cutoff is asserted."]}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({name: value.coefficient(0, 0).real.str(18)
                      for name, value in values.items()}), flush=True)
    print(json.dumps({"seconds": report["seconds"], "source_sha256": sha(__file__)}), flush=True)


if __name__ == "__main__":
    main()
