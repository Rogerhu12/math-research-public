#!/usr/bin/env python3
"""Actual fixed-tau f, fp, fpp on a paid complex-time/physical-angle germ.

Only the exact saved central parameter is used for these signed sources.
The larger real parameter tube is paid separately by R80.  E, Ep and Epp
remain complex at complex r.  Turn parameter derivatives are deflated
before the square root, using the exact identities K(t(p),p)=0.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import math
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, acb_series, acb_poly, ctx

from fourfold_phase_fixed_tau_parameter_bounds import (
    ParameterSecondTarget, NormJet, composed_norm, multiply, quotient_norm,
    sha, read, save, interval, absup,
)
from fourfold_phase_real_parameter_forcing import normalized_total, parameter_series
from fourfold_phase_beta_interval import (
    array_derivative, series_derivative, vector_dot, series_constant,
    primitive_fourier_budget, ball_record,
)
from fourfold_phase_beta_bulk_interval import exact_arb, complex_pad
from fourfold_phase_unified_scalar_time_circle import (
    UnifiedScalarTimeCircleField, complex_record,
)
from fourfold_phase_uniform_field_time_grid_fast import f_invariants
from fourfold_native_series_fft import NativeSeriesFFT


def lower(row):
    return arb(row["lower"]).lower()


def upper(row):
    return arb(row["upper"]).upper()


class CentralParameterTarget(ParameterSecondTarget):
    """Exact central geometry with analytic first/second formal directions."""
    def initialize_parameter(self, object_path, half_width, definition, direction, center):
        super().initialize_parameter(object_path, half_width, definition, direction, center)
        self.parameter_half_width = Fraction(0)
        self.parameter_interval = (center, center)
        self.parameter_ball = exact_arb(center)

    def parameter_target2(self, center, scale, budgets):
        F, Fp, Fpp, a, ap = self.primitive_parameter2(center, -scale)
        self.last_primitive = F, Fp, Fpp, a, ap
        X, Xp, Xpp = (array_derivative(v, -scale) for v in (F, Fp, Fpp))
        def pair(U, V):
            return sum((vector_dot(U[k], V[(-k) % self.nodes])
                        for k in range(self.nodes)), series_constant(0))
        finite = pair(X, X), 2*pair(X, Xp), 2*(pair(Xp, Xp)+pair(X, Xpp))
        E, Ep, Epp = [acb_series([
            complex_pad(v[n], budget["E_error"]*(abs(scale)/budget["E_radius"])**n)
            for n in range(v.prec)], prec=v.prec) for v, budget in zip(finite, budgets)]
        if not (a[0].abs_lower() > 0 and E[0].abs_lower() > 0):
            raise ValueError("actual complex a or E enclosure does not exclude zero")
        ar, arr = series_derivative(a, -scale), series_derivative(a, -scale, 2)
        apr, appr = series_derivative(ap, -scale), series_derivative(ap, -scale, 2)
        Er, Epr, Eppr = (series_derivative(v, -scale) for v in (E, Ep, Epp))
        C = ar*Er-2*arr*E
        Cp = apr*Er+ar*Epr-2*appr*E-2*arr*Ep
        Cpp = 2*apr*Epr+ar*Eppr-4*appr*Ep-2*arr*Epp
        denominator = 2*a*E**2
        K = C/denominator
        logarithmic = ap/a+2*Ep/E
        logarithmic_p = -(ap/a)**2+2*Epp/E-2*(Ep/E)**2
        Kp = Cp/denominator-K*logarithmic
        Kpp = Cpp/denominator-2*Kp*logarithmic-K*(logarithmic**2+logarithmic_p)
        return dict(a=a, E=E, Ep=Ep, Epp=Epp, C=C, Cp=Cp, Cpp=Cpp,
                    K=K, Kp=Kp, Kpp=Kpp)


_CENTRAL_ROOT_CACHE = {}


def refine_central_root_parameters(field):
    """Actual implicit derivatives on the already refined true central root."""
    key = (sha(field.object_path), sha(field.root_path), field.nodes, ctx.prec,
           field.root.str(ctx.dps+8), str(field.tp), str(field.tpp))
    if key in _CENTRAL_ROOT_CACHE:
        return _CENTRAL_ROOT_CACHE[key]
    target = CentralParameterTarget(field.object_path, Fraction(1, 10**14),
        field.nodes, field.nodes, field.R0, field.RE, field.sigma)
    target.fourier = NativeSeriesFFT()
    target.set_cell(*map(Fraction, field.base.root_package.provenance["root_common_span"]))
    oldcap, ctx.cap = ctx.cap, 7
    try:
        scale = exact_arb(Fraction(1, 4096))
        budget = target.parameter_input_budget2(acb(field.root), field.R0, field.sigma, field.RE)
        data = target.parameter_target2(acb(field.root), scale, budget)
        K, Kp, Kpp = data["K"], data["Kp"], data["Kpp"]
        Kr = series_derivative(K, -scale)[0].real
        Krr = series_derivative(K, -scale, 2)[0].real
        Krp = series_derivative(Kp, -scale)[0].real
        if not (K[0].real.contains(0) and Kr > 0):
            raise ValueError("refined central root or simple-root derivative gate failed")
        tp = -Kp[0].real/Kr
        tpp = -(Kpp[0].real+2*Krp*tp+Krr*tp**2)/Kr
        if not (tp.overlaps(field.tp) and tpp.overlaps(field.tpp)):
            raise ValueError("central implicit derivatives disagree with the proved real parameter tube")
        tp, tpp = tp.intersection(field.tp), tpp.intersection(field.tpp)
        report = dict(proved=True, actual_central_parameter_only=True,
            refined_true_root=ball_record(field.root), primitive_nodes=field.nodes,
            real_K_at_true_root=ball_record(K[0].real), positive_Kr=ball_record(Kr),
            fixed_r_Kp=ball_record(Kp[0].real), fixed_r_Kpp=ball_record(Kpp[0].real),
            Krp=ball_record(Krp), Krr=ball_record(Krr),
            true_root_parameter_first=ball_record(tp), true_root_parameter_second=ball_record(tpp),
            formulas=["t_p=-K_p/K_r", "t_pp=-(K_pp+2*K_rp*t_p+K_rr*t_p^2)/K_r"],
            real_projection_only_at_actual_real_root=True,
            larger_real_parameter_branch_witness=sha(field.local_root_jets))
        _CENTRAL_ROOT_CACHE[key] = tp, tpp, report
        return tp, tpp, report
    finally:
        ctx.cap = oldcap


def majorant_complex_scalars(target, center, width):
    """All needed mixed jets on a complex radial ball and whole theta strip."""
    beta, gamma, a, height = target.scalars(center, 1)
    bp, gp, ap, hp = target.direction_scalars(center, 1)
    weights = [(4*(k+1)*width).cosh() for k in range(target.modes)]
    sine_weights = [(4*(k+1)*width).sinh() for k in range(target.modes)]
    def modes(v0, v1, angular=0):
        out = NormJet()
        for i in range(4):
            for j, values in enumerate((v0, v1)):
                out[i, j] = sum((absup(v[i])*weights[k]*(4*(k+1))**angular
                                 for k, v in enumerate(values)), arb(0)).upper()
        return out
    def scalar(v0, v1):
        out = NormJet()
        for i in range(4):
            out[i, 0], out[i, 1] = absup(v0[i]), absup(v1[i])
        return out
    B, G = modes(beta, bp), modes(gamma, gp)
    Bt, Gt = modes(beta, bp, 1), modes(gamma, gp, 1)
    A, Zr = scalar(a, ap), scalar(height.derivative(), hp.derivative())
    imaginary = width
    for row in (beta, gamma):
        imaginary += sum((absup(v[0].real)*s+absup(v[0].imag)*c
                          for v, s, c in zip(row, sine_weights, weights)), arb(0))
    imaginary = imaginary.upper()
    increment = B+G
    increment[0, 0] = 0
    T = increment.exp(lambda _: imaginary.exp().upper())
    Tr, Ttheta = T*(B.derivative()+G.derivative()), T*(1+Bt+Gt)
    X = (A*T).derivative()*(arb.pi()/2)+Zr
    cross = X*T
    return dict(D=cross*Ttheta, M=cross*Tr, W=cross*cross,
                tangent_imaginary_bound=imaginary)


class ParameterRootDeflation:
    """J_j(rho)=-partial_p^j K(t(p)-rho,p)/rho, j=0,1,2."""
    def __init__(self, field, degree=40, radius=Fraction(3, 1250)):
        self.field, self.degree, self.RK = field, int(degree), exact_arb(radius)
        if degree < 4 or not field.R0 > field.RE > self.RK > 0:
            raise ValueError("invalid radial deflation degree or nested domains")
        self.target = CentralParameterTarget(field.object_path, Fraction(1, 10**14),
            field.nodes, field.nodes, field.R0, field.RE, field.sigma)
        self.target.fourier = NativeSeriesFFT()
        self.target.set_cell(*map(Fraction, field.base.root_package.provenance["root_common_span"]))
        oldcap = ctx.cap
        try:
            ctx.cap = degree+6
            budget = self.target.parameter_input_budget2(acb(field.root), field.R0, field.sigma, field.RE)
            data = self.target.parameter_target2(acb(field.root), self.RK, budget)
            K, Kp, Kpp = data["K"], data["Kp"], data["Kpp"]
            Kr, Krr = series_derivative(K, -self.RK), series_derivative(K, -self.RK, 2)
            Krp = series_derivative(Kp, -self.RK)
            totals = [K, Kp+field.tp*Kr,
                      Kpp+2*field.tp*Krp+field.tp**2*Krr+field.tpp*Kr]
            if any(not v[0].real.contains(0) for v in totals):
                raise ValueError("actual root parameter zero identities are inconsistent")
            # All coefficients are real at the true real root. The constant
            # is identically zero for all three actual p derivatives.
            self.coefficients = [[acb((-v[j+1]/self.RK).real)
                                  for j in range(degree)] for v in totals]
            ctx.cap = 7
            disk = complex_pad(acb(field.root), self.RK)
            budget = self.target.parameter_input_budget2(disk, field.R0, field.sigma, field.RE)
            data = self.target.parameter_target2(disk, arb(1), budget)
            K, Kp, Kpp = data["K"], data["Kp"], data["Kpp"]
            Kr, Krr = series_derivative(K, -1), series_derivative(K, -1, 2)
            Krp = series_derivative(Kp, -1)
            self.bounds = [
                absup(K[0]),
                (absup(Kp[0])+absup(field.tp)*absup(Kr[0])).upper(),
                (absup(Kpp[0])+2*absup(field.tp)*absup(Krp[0])
                 +absup(field.tp)**2*absup(Krr[0])+absup(field.tpp)*absup(Kr[0])).upper()]
            if not all(v.is_finite() for v in self.bounds):
                raise ValueError("nonfinite complete parameter curvature disk bounds")
            self.domain = dict(radius=str(radius), degree=degree,
                K_total_parameter_moduli=list(map(ball_record, self.bounds)),
                a_modulus_lower=ball_record(data["a"][0].abs_lower()),
                E_modulus_lower=ball_record(data["E"][0].abs_lower()),
                all_three_exact_root_constants_removed=True)
        finally:
            ctx.cap = oldcap

    def evaluate_j(self, rho, parameter_order, radial_order=0):
        z = rho/self.RK
        q = absup(z)
        if not q < 1:
            raise ValueError("parameter root quotient leaves its paid radial disk")
        coefficients = self.coefficients[parameter_order]
        d, L = int(radial_order), self.degree
        polynomial = acb_poly(coefficients)
        for _ in range(d):
            polynomial = polynomial.derivative()
        value = polynomial(z)/self.RK**d
        if d == 0:
            series_tail = q**L/(1-q)
        elif d == 1:
            series_tail = L*q**(L-1)/(1-q)+q**L/(1-q)**2
        elif d == 2:
            series_tail = (L*(L-1)*q**(L-2)/(1-q)
                +2*L*q**(L-1)/(1-q)**2+2*q**L/(1-q)**3)
        else:
            raise ValueError("only two radial derivatives enter fixed-tau parameters")
        error = (self.bounds[parameter_order]/self.RK**(d+1)*series_tail).upper()
        return complex_pad(value, error)

    def quotient_parameter_series(self, eta):
        cosine = eta.cos()
        denominator = 1+cosine
        if not denominator.abs_lower() > 0:
            raise ValueError("turn quotient denominator is not separated")
        rho = self.field.root*(1-cosine)
        rp, rpp = self.field.tp*(1-cosine), self.field.tpp*(1-cosine)
        J, Jr, Jrr = [self.evaluate_j(rho, 0, d) for d in (0, 1, 2)]
        Jp, Jrp = [self.evaluate_j(rho, 1, d) for d in (0, 1)]
        Jpp = self.evaluate_j(rho, 2)
        Jtotal = parameter_series([J, Jp+rp*Jr, (Jpp+2*rp*Jrp+rp**2*Jrr+rpp*Jr)/2])
        tjet = parameter_series([self.field.root, self.field.tp, self.field.tpp/2])
        return tjet*Jtotal/denominator

    def wave_parameter_series(self, eta):
        Q = self.quotient_parameter_series(eta)
        if not Q[0].real > 0:
            raise ValueError("actual root-deflated Q branch is not separated at this sample")
        return eta.sin()*Q.sqrt()


class ParameterTimeCircleField:
    """Uniform real-angle samples, with actual analytic parameter derivatives."""
    def __init__(self, descriptor, domain, local_root_jets, *, nodes=512, root_nodes=1024,
                 outer=Fraction(3), germ=-1, radial_degree=40):
        self.base = UnifiedScalarTimeCircleField(descriptor, domain, germ=germ,
            nodes=nodes, root_nodes=root_nodes, radial_degree=radial_degree)
        base = self.base
        self.object_path, self.root_path = base.object_path, base.root_path
        self.root, self.nodes = base.root, nodes
        self.local_root_jets = Path(local_root_jets)
        local = read(local_root_jets)
        if not (local.get("proved") and local["object_sha256"] == sha(self.object_path)
                and local["point_root_sha256"] == sha(self.root_path)):
            raise ValueError("root parameter jets belong to another exact object")
        self.tp, self.tpp = interval(local["root_parameter_first"]), interval(local["root_parameter_second"])
        self.outer = exact_arb(outer)
        if not 1 < self.outer <= base.outer:
            raise ValueError("selected parameter source time disk leaves actual domain")
        self.strip, self.sign, self.turn = base.strip, base.sign, base.turn
        self.R0, self.RE, self.sigma = base.R0, base.RE, base.sigma
        self.exact_tau0, self.exact_h = base.exact_tau0, base.exact_h
        self.tau0, self.h = base.tau0, base.h
        self.cell = base.cell
        self.tp, self.tpp, self.root_parameter_refinement = refine_central_root_parameters(self)
        self.target = CentralParameterTarget(self.object_path, Fraction(1, 10**14),
            nodes, nodes, self.R0, self.RE, self.sigma)
        self.target.fourier = NativeSeriesFFT()
        self.target.set_cell(*self.cell)
        H = abs(self.h)*self.outer
        self.center = self.root*self.tau0.sin()
        self.radial_enlargement = (abs(self.root)*(abs(self.tau0.sin())*(H.cosh()-1)
                                            +abs(self.tau0.cos())*H.sinh())).upper()
        common = self.target.parameter_input_budget2(acb(self.center),
            self.R0+self.radial_enlargement, self.sigma, self.RE+self.radial_enlargement)
        self.common_budgets = []
        for row in common:
            copy = dict(row)
            copy["radial_radius"], copy["E_radius"] = self.R0, self.RE
            self.common_budgets.append(copy)
        self.deflation = ParameterRootDeflation(self, radial_degree) if self.turn else None
        self.moduli = self.complete_source_moduli()

    def complete_source_moduli(self):
        """Continuous whole-theta/time bounds for the actual central sources."""
        oldcap, ctx.cap = ctx.cap, 7
        try:
            tau = complex_pad(acb(self.tau0), abs(self.h)*self.outer)
            sine, cosine = tau.sin(), tau.cos()
            radial = complex_pad(acb(self.center), self.radial_enlargement)
            geometry = majorant_complex_scalars(self.target, radial, self.strip)
            r1, r2 = absup(self.tp*sine), absup(self.tpp*sine)
            D, M, W = [composed_norm(geometry[key], r1, r2) for key in ("D", "M", "W")]
            Dmin = lower(self.base.selected["D_lower"])
            if not Dmin > 0:
                raise ValueError("actual central D domain is not separated")
            drift = quotient_norm(M, D, Dmin, (M[0]/Dmin).upper())
            wave = quotient_norm(W, D, Dmin, (W[0]/Dmin).upper())
            curvature = self.base.selected["curvature"]
            if self.turn:
                eta = acb(self.base.eta0)+self.base.eta1*complex_pad(acb(0), self.outer)
                Q = self.deflation.quotient_parameter_series(eta)
                Qmin = lower(curvature["Q_real_lower"])
                qnorm = [absup(Q[j]) for j in range(3)]
                square = [qnorm[0].sqrt().upper(),
                    (qnorm[1]/(2*Qmin.sqrt())).upper(),
                    (qnorm[2]/(2*Qmin.sqrt())+qnorm[1]**2/(8*Qmin**(arb(3)/2))).upper()]
                square = [absup(eta.sin())*x for x in square]
                extra = dict(deflated_Q_normalized_parameter_bounds=list(map(ball_record, qnorm)),
                             actual_Q_real_lower=ball_record(Qmin))
            else:
                data = self.target.parameter_target2(radial, arb(1), self.common_budgets)
                Ktotal = normalized_total(data["K"], data["Kp"], data["Kpp"], arb(1),
                                         self.tp*sine, self.tpp*sine)
                knorm = [absup(v) for v in Ktotal]
                Kmin = lower(curvature["minus_K_real_lower"])
                square = [knorm[0].sqrt().upper(),
                    (knorm[1]/(2*Kmin.sqrt())).upper(),
                    (knorm[2]/(2*Kmin.sqrt())+knorm[1]**2/(8*Kmin**(arb(3)/2))).upper()]
                extra = dict(K_normalized_parameter_bounds=list(map(ball_record, knorm)),
                             actual_minus_K_real_lower=ball_record(Kmin))
            inner = [d+w for d, w in zip(drift, multiply(square, wave))]
            rtau = [absup(self.root*cosine), absup(self.tp*cosine), absup(self.tpp*cosine)/2]
            result = multiply(rtau, inner)
            result[2] *= 2
            if not all(v.is_finite() for v in result):
                raise ValueError("nonfinite complete actual parameter source moduli")
            return dict(proved=True, f=ball_record(result[0]), fp=ball_record(result[1]),
                fpp=ball_record(result[2]), D_lower=ball_record(Dmin),
                tangent_imaginary_bound=ball_record(geometry["tangent_imaginary_bound"]), **extra)
        finally:
            ctx.cap = oldcap

    def sample(self, u, angles, imaginary_theta=Fraction(0)):
        """True central [f,fp,fpp] arrays at one complex normalized time."""
        u, width = acb(u), exact_arb(Fraction(imaginary_theta))
        if not abs(u).upper() < self.outer or not abs(width) < self.strip:
            raise ValueError("parameter sample leaves paid time/angle domain")
        angles = int(angles)
        if angles < self.nodes or angles & (angles-1):
            raise ValueError("power of two angle nodes at least the primitive grid required")
        oldcap, ctx.cap = ctx.cap, 7
        wall, cpu = time.monotonic(), time.process_time()
        try:
            if self.turn and u.imag == 0 and u.real.is_exact():
                exact_u = Fraction(str(u.real.fmpq()))
                if (self.base.exact_eta0+self.base.exact_eta1*exact_u).is_zero():
                    result = np.empty((angles, 3), object); result.fill(acb(0))
                    return result, dict(exact_turn_zero=True)
            tau = acb(self.tau0)+self.h*u
            sine, cosine = tau.sin(), tau.cos()
            radial, rp, rpp = self.root*sine, self.tp*sine, self.tpp*sine
            data = self.target.parameter_target2(radial, arb(1), self.common_budgets)
            F, Fp, Fpp, _, _ = self.target.last_primitive
            coefficient = np.empty((angles, 9), object)
            coefficient.fill(None)
            for key in np.ndindex(coefficient.shape):
                coefficient[key] = parameter_series([0, 0, 0])
            for k, frequency in enumerate(self.target.frequency):
                weight = (-frequency*width).exp()
                for component in range(3):
                    values = normalized_total(F[k, component], Fp[k, component], Fpp[k, component],
                                              arb(1), rp, rpp, radial_order=1)
                    coefficient[(frequency//4) % angles, component] = parameter_series(values)*weight
            beta, gamma, _, _ = self.target.scalars(radial, -1)
            bp, gp, _, _ = self.target.direction_scalars(radial, -1)
            zero = acb_series([0], prec=ctx.cap)
            phase = []
            for order in (0, 1):
                for row, change in ((beta, bp), (gamma, gp)):
                    phase.append([parameter_series(normalized_total(v, vp, zero, arb(1), rp, rpp,
                                                  radial_order=order)) for v, vp in zip(row, change)])
            for k, values in enumerate(zip(*phase), 1):
                for sign in (-1, 1):
                    frequency = 4*sign*k
                    factor, slot = acb(0, -sign)*(-frequency*width).exp()/2, (sign*k) % angles
                    coefficient[slot, 3:7] = [v*factor for v in values]
                    coefficient[slot, 7] = values[0]*factor*acb(0, frequency)
                    coefficient[slot, 8] = values[1]*factor*acb(0, frequency)
            samples = self.target.fourier.fft(coefficient, inverse=True)*angles
            primitive_errors = [primitive_fourier_budget(self.nodes, self.sigma, 4*abs(width), self.R0,
                b["radius_bound"], b["height_bound"], b["tangent_bound"])[0][0] for b in self.common_budgets]
            e0, e1, e2 = primitive_errors
            fees = [(e0/self.R0).upper(),
                    (e1/self.R0+absup(rp)*2*e0/self.R0**2).upper(),
                    ((e2/self.R0+2*absup(rp)*2*e1/self.R0**2
                       +absup(rp)**2*6*e0/self.R0**3+absup(rpp)*2*e0/self.R0**2)/2).upper()]
            if self.turn:
                wave = self.deflation.wave_parameter_series(acb(self.base.eta0)+self.base.eta1*u)
            else:
                Ktotal = parameter_series(normalized_total(data["K"], data["Kp"], data["Kpp"],
                                            arb(1), rp, rpp))
                if not (-Ktotal[0]).real > 0:
                    raise ValueError("actual ordinary curvature branch enclosure failed")
                wave = (-Ktotal).sqrt()
            rtau = parameter_series([self.root*cosine, self.tp*cosine, self.tpp*cosine/2])
            result = np.empty((angles, 3), object)
            minimum_D = None
            for j in range(angles):
                X = [parameter_series([complex_pad(samples[j, c][p], fees[p])
                                       for p in range(3)]) for c in range(3)]
                D, M, W = f_invariants(X, samples[j, 3:])
                if not D[0].abs_lower() > 0:
                    raise ValueError("pointwise actual D enclosure contains zero")
                minimum_D = D[0].abs_lower() if minimum_D is None else min(minimum_D, D[0].abs_lower())
                value = -rtau*(M+self.sign*wave*W)/D
                result[j] = [value[0], value[1], 2*value[2]]
            return result, dict(primitive_X_normalized_parameter_fees=list(map(ball_record, fees)),
                sample_D_lower=ball_record(minimum_D), elapsed_seconds=time.monotonic()-wall,
                cpu_seconds=time.process_time()-cpu, complex_E_preserved=True)
        finally:
            ctx.cap = oldcap

    def identity(self):
        return dict(kind="actual_central_parameter_time_circle_sources",
            base_identity=self.base.identity(), source_sha256=sha(__file__),
            local_root_jets_sha256=sha(self.local_root_jets),
            source_time_radius=str(self.outer), source_physical_theta_strip=str(self.strip),
            actual_center_parameter_only=True, fixed_physical_tau_parameter_derivatives=True,
            actual_root_parameter_first=ball_record(self.tp), actual_root_parameter_second=ball_record(self.tpp),
            central_root_parameter_refinement=self.root_parameter_refinement,
            complete_source_moduli=self.moduli,
            deflation=None if self.deflation is None else self.deflation.domain,
            limitations=["One selected actual analytic germ, not any neighboring real spline germ.",
                "No parameter Fourier/time interpolant or density integral is asserted by sampling alone.",
                "Crossing fp/fpp germ differences require their own lower-order cap fees."])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    base = Path("data/phase_ring_continuation")
    p.add_argument("--descriptor", type=Path, default=base/"step5_retargeted_reference/descriptor.json")
    p.add_argument("--domain", type=Path, required=True)
    p.add_argument("--local-root-jets", type=Path, default=base/"type_fixed_step02_d5_step5_local_parameter_root_jets_h1e14.json")
    p.add_argument("--primitive-nodes", type=int, default=512)
    p.add_argument("--root-nodes", type=int, default=1024)
    p.add_argument("--angles", type=int, default=512)
    p.add_argument("--bits", type=int, default=256)
    p.add_argument("--outer", type=Fraction, default=Fraction(3))
    p.add_argument("--radial-degree", type=int, default=40)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    ctx.prec, ctx.cap = args.bits, 7
    started, cpu = time.monotonic(), time.process_time()
    model = ParameterTimeCircleField(args.descriptor, args.domain, args.local_root_jets,
        nodes=args.primitive_nodes, root_nodes=args.root_nodes, outer=args.outer, radial_degree=args.radial_degree)
    report = dict(**model.identity(), complete=False, samples=[])
    save(args.out, report)
    for u in (acb(0), acb(1), acb(0, 1)):
        values, details = model.sample(u, args.angles)
        base_values, _ = model.base.sample(u, args.angles)
        if any(not (a[0].real.overlaps(b.real) and a[0].imag.overlaps(b.imag))
               for a, b in zip(values, base_values)):
            raise ValueError("parameter source f0 and independent scalar field disagree")
        report["samples"].append(dict(u=complex_record(u), all_f0_scalar_nodes_overlap=True,
            maximum_source_moduli=[ball_record(max(absup(v) for v in values[:, j])) for j in range(3)],
            maximum_component_radii=[ball_record(max(max(v.real.rad().upper(), v.imag.rad().upper())
                                                       for v in values[:, j])) for j in range(3)],
            retained_checks=[dict(index=j, sources=list(map(complex_record, values[j])))
                             for j in sorted({0, args.angles//7, args.angles//3, args.angles-1})],
            **details))
        save(args.out, report)
        print(dict(u=str(u), passed=True, elapsed=time.monotonic()-started), flush=True)
    report.update(complete=True, elapsed_seconds=time.monotonic()-started, cpu_seconds=time.process_time()-cpu)
    save(args.out, report)
    print(dict(complete=True, sha256=sha(args.out), elapsed=report["elapsed_seconds"]), flush=True)


if __name__ == "__main__":
    main()
