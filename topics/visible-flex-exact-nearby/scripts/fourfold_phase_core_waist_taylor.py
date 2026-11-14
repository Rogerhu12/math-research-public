#!/usr/bin/env python3
"""Actual removable waist quotient for the correlated finite core engine.

Only the first positive common span uses this extension. Its exact explicit
symmetry gives gamma(0)=Z(0)=0 for every affine parameter, so both the finite
and infinite vertical primitives vanish at r=0. Dividing by r is analytic,
with its own complete Fourier and radial Taylor fees.
"""
from __future__ import annotations

import math
import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_beta_bulk_box import (
    FastBulkTarget, CBox, Box, arb_box, reduce_box, cstack, zeros,
    cdot, ccross, complex_sincos, stack)
from fourfold_phase_beta_interval import (
    ball_record, primitive_fourier_budget, analytic_tail_derivative)
from fourfold_phase_actual_positive_cap import complex_separation
from fourfold_phase_core_radial_taylor import CorrelatedCoreTarget


class WaistCoreTarget(CorrelatedCoreTarget):
    def build_native_taylor(self):
        if self.cell[0] != 0:
            return super().build_native_taylor()
        if self.native_poly is not None:
            return
        old_cap = ctx.cap
        try:
            ctx.cap = max(21, self.native_order)
            coefficients, _ = self.primitive(acb(0), 1)
            result = zeros((self.native_order, self.nodes, 3))
            for k in range(self.nodes):
                for component in range(3):
                    for j in range(self.native_order):
                        value = coefficients[k, component][j]
                        if component == 2 and j == 0:
                            if not value.real.contains(0) or not value.imag.contains(0):
                                raise ValueError('the exact waist vertical-zero identity lost its enclosure')
                            # This equality follows from explicit gamma(0)=Z(0)=0,
                            # not from deciding that a small computed value is zero.
                            result[j, k, component] = 0
                        else:
                            result[j, k, component] = CBox.from_acb(value)
            self.native_poly = result
            self.native_budget = self.analytic_input_budget(
                arb(0), self.native_radius, self.tail_sigma, self.native_radius/2)
        finally:
            ctx.cap = old_cap

    def finite_data(self, radial):
        if self.cell[0] != 0:
            return super().finite_data(radial)
        self.build_native_taylor()
        radius = self.scalar_data(radial)
        delta = CBox.from_acb(radial)
        jet = zeros((4, self.nodes, 3))
        for j in range(self.native_order-1, -1, -1):
            jet = jet*delta+cstack([self.native_poly[j], jet[0], 2*jet[1], 3*jet[2]])
        return jet, radius

    def tail_errors(self, radial, inner_sigma=arb(0)):
        if self.cell[0] != 0:
            return super().tail_errors(radial, inner_sigma)
        self.build_native_taylor()
        infinite = FastBulkTarget.tail_errors(self, radial, inner_sigma)
        distance = abs(radial).upper()
        if not distance < self.native_radius:
            raise ValueError('radial Taylor evaluation exceeds its paid analytic disk')
        key = inner_sigma.str(40)
        if key not in self.native_majorants:
            budget = self.native_budget
            _, finite = primitive_fourier_budget(
                self.nodes, self.tail_sigma, inner_sigma, self.native_radius,
                budget['radius_bound'], budget['height_bound'], budget['tangent_bound'])
            self.native_majorants[key] = finite
        finite = self.native_majorants[key]
        extra = []
        derivative_rows = []
        for angular in range(3):
            derivative_tails = []
            for radial_order in range(4):
                value = (arb(0) if distance == 0 else analytic_tail_derivative(
                    finite[angular], self.native_radius, distance,
                    self.native_order, radial_order))
                derivative_tails.append(value.upper())
            # The established bulk API uses j! error / tail_radius^j.  This
            # maximum makes that contract include every radial Taylor tail.
            effective = max((derivative_tails[j]*self.tail_radius**j
                             /math.factorial(j)).upper() for j in range(4))
            extra.append(effective)
            derivative_rows.append(derivative_tails)
        self.last_native_remainders = dict(
            exact_single_germ=True,
            radial_distance=ball_record(distance),
            outer_radial_radius=ball_record(self.native_radius),
            complete_finite_primitive_moduli=[ball_record(x) for x in finite],
            radial_remainders=[[ball_record(x) for x in row] for row in derivative_rows],
            effective_extra_errors=[ball_record(x) for x in extra],
            original_infinite_primitive_errors=[ball_record(x) for x in infinite])
        return [(a+b).upper() for a, b in zip(infinite, extra)]


    def waist_quotient_fields(self, radial, sigma=None):
        if self.cell[0] != 0:
            raise ValueError('the waist quotient is restricted to the first positive common germ')
        self.build_native_taylor()
        distance = abs(radial).upper()
        if not distance < self.native_radius:
            raise ValueError('the waist quotient exceeds its analytic primitive disk')
        inner_sigma = arb(0) if sigma is None else sigma+arb.pi()/self.angles
        budget = self.native_budget
        infinite, finite = primitive_fourier_budget(
            self.nodes, self.tail_sigma, inner_sigma, self.native_radius,
            budget['radius_bound'], budget['height_bound'], budget['tangent_bound'])
        delta = CBox.from_acb(radial)
        qcoef = zeros((self.nodes,))
        for j in range(self.native_order-1, 0, -1):
            qcoef = qcoef*delta+self.native_poly[j, :, 2]
        frequency = np.asarray(self.frequency)
        coefficients = (qcoef, qcoef*CBox(0., Box(frequency)))
        if sigma is not None:
            modes = np.abs(frequency//4)
            variation = stack([arb_box((abs(int(k))*sigma).exp()
                *abs(int(k))*arb.pi()/self.angles
                +(abs(int(k))*sigma).exp()-1) for k in modes])
        fields, fees = [], []
        q = distance/self.native_radius
        for angular_order in range(2):
            # Both P_Q,z and F_z vanish exactly at r=0. The quotient maximum
            # principle gives M/R*, and the retained quotient has P-1 terms.
            tail = (arb(0) if distance == 0 else
                finite[angular_order]/self.native_radius
                *q**(self.native_order-1)/(1-q))
            full_error = (tail+infinite[angular_order]/self.native_radius).upper()
            values = coefficients[angular_order]
            data = zeros((self.angles,))
            data[(frequency//4) % self.angles] = values
            samples = (self.fast_fourier.fft(data, inverse=True)*self.angles)[:self.sample_count]
            fee = arb_box(full_error)
            if sigma is None:
                field = samples.pad(fee, radial.imag == 0)
            else:
                var = (fee+reduce_box(Box(values.magnitude_upper())*variation)).hi
                field = CBox(samples.real+Box(-var, var), samples.imag+Box(-var, var))
            fields.append(field)
            fees.append(full_error)
        self.last_waist_quotient = dict(
            exact_zero_identity='gamma(0,theta)=Z(0)=0 for every parameter by the explicit symmetric object; finite P_Q,z(0,theta)=F_z(0,theta)=0.',
            quotient='Q=F_z/r, Qtheta=(F_z/r)_theta, both analytically continued at zero',
            outer_radial_radius=ball_record(self.native_radius),
            complete_errors=[ball_record(x) for x in fees])
        return tuple(fields)

    def coefficient_values(self, radial, coefficient, K0, errors, sigma=None):
        if self.cell[0] != 0:
            return super().coefficient_values(radial, coefficient, K0, errors, sigma)
        real = radial.imag == 0
        fields = self.fast_fields(radial, coefficient, errors, real, sigma)
        if real and sigma is None:
            for value in fields.values():
                if np.any(value.imag.lo > 0) or np.any(value.imag.hi < 0):
                    raise ValueError('a true real core field lost the real axis')
            fields = {key:CBox(value.real) for key, value in fields.items()}
        F, X, Y, Frr, Frt, Ftt = [fields[key] for key in
            ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2))]
        cross = ccross(Y, X)
        G, R2, support = cdot(cross, cross), cdot(F, F), cdot(cross, F)
        l, m, n = [cdot(cross, value) for value in (Frr, Frt, Ftt)]
        rlo = complex_separation(R2, 'F dot F')
        slo = complex_separation(support, 'the true support numerator')
        nlo = complex_separation(n, 'the true raw N')
        Qz, Qzt = self.waist_quotient_fields(radial, sigma)
        zlo = complex_separation(Qz, 'the analytic waist F_z/r')
        ell = Qzt/Qz-cdot(F, Y)/R2
        factor = R2/(support*support)
        a, b, c0 = -n*factor, m*factor, -l*factor
        chat = -(m*m+K0*G*G)*factor/n
        omega = c0-chat
        FX, FY = cdot(F, X), cdot(F, Y)
        d0 = (a*(cdot(X, X)-FX*FX/R2)
              +2*b*(cdot(X, Y)-FX*FY/R2)
              +c0*(cdot(Y, Y)-FY*FY/R2))/R2
        values = dict(a=a, b=b, c=chat, tau=d0+omega*ell*ell, sigma=omega*ell)
        if any(not np.all(np.isfinite(v.magnitude_upper())) for v in values.values()):
            raise ValueError('a true coefficient enclosure is not finite')
        self.last_geometric_domain = dict(
            R2_modulus_lower=ball_record(rlo), support_modulus_lower=ball_record(slo),
            Nraw_modulus_lower=ball_record(nlo), height_quotient_modulus_lower=ball_record(zlo),
            height_chart='analytic Q=F_z/r including r=0')
        return values



    def coefficient_moduli_bidisk(self, radial, coefficient, K0, errors, strip):
        """Whole angular strip moduli with the analytic waist quotient."""
        if self.cell[0] != 0:
            return super().coefficient_moduli_bidisk(radial, coefficient, K0, errors, strip)
        fields = self.fast_fields(radial, coefficient, errors, radial.imag == 0, strip)
        F, X, Y, Frr, Frt, Ftt = [fields[key] for key in
            ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2))]
        cross = ccross(Y, X)
        Gbox, Rbox, Sbox = cdot(cross, cross), cdot(F, F), cdot(cross, F)
        lbox, mbox, nbox = [cdot(cross, value) for value in (Frr, Frt, Ftt)]
        upper = lambda value:arb(float(np.max(value.magnitude_upper()))).upper()
        Rlo = complex_separation(Rbox, 'F dot F on the whole angular strip')
        Slo = complex_separation(Sbox, 'support on the whole angular strip')
        beta, gamma, radius, _ = self.last_scalar
        ss, cc = self.angle_shift_cache[strip.str(35)]
        frequency = CBox((4*np.arange(1, self.modes+1)).reshape(-1, 1))
        b = (beta[0].reshape(-1, 1)*ss).sum()
        g = (gamma[0].reshape(-1, 1)*ss).sum()
        bt = (beta[0].reshape(-1, 1)*frequency*cc).sum()
        gt = (gamma[0].reshape(-1, 1)*frequency*cc).sum()
        sb, cb = complex_sincos(b)
        sg, cg = complex_sincos(g)
        horizontal_gamma = -sb*X[:, 0]+cb*X[:, 1]
        v = -cb*X[:, 0]-sb*X[:, 1]
        Q = cg*X[:, 2]-sg*horizontal_gamma
        Plo = self.phase_boundary_P_lower(radial, strip)
        clo = complex_separation(cg, 'cos gamma')
        Qlo = complex_separation(Q, 'moving-frame Q')
        alo = complex_separation(radius[0], 'phase circumference radius')
        Dlo = (Plo*clo*Qlo-upper(gt)*upper(v)).lower()
        if not Dlo > 0:
            raise ValueError('the correlated moving-frame product modulus does not separate N')
        Nlo = (alo*alo*Dlo).lower()
        # n = -a^2(P cos(gamma) Q - gamma_theta v) exactly.  The bound above
        # establishes nonvanishing even when the rectangular n enclosure wraps.
        Qz, Qzt = self.waist_quotient_fields(radial, strip)
        Zlo = complex_separation(Qz, 'the analytic waist F_z/r on the angular strip')
        ell = upper(Qzt)/Zlo+upper(cdot(F, Y))/Rlo
        G, R2 = upper(Gbox), upper(Rbox)
        L, M, N = upper(lbox), upper(mbox), upper(nbox)
        factor = R2/Slo**2
        A, B, C0 = N*factor, M*factor, L*factor
        C = (M*M+upper(K0)*G*G)*factor/Nlo
        omega = C0+C
        FX, FY = upper(cdot(F, X)), upper(cdot(F, Y))
        d0 = (A*(upper(cdot(X, X))+FX*FX/Rlo)
             +2*B*(upper(cdot(X, Y))+FX*FY/Rlo)
             +C0*(upper(cdot(Y, Y))+FY*FY/Rlo))/Rlo
        self.last_geometric_domain = dict(
            R2_modulus_lower=ball_record(Rlo), support_modulus_lower=ball_record(Slo),
            Nraw_modulus_lower=ball_record(Nlo),
            height_quotient_modulus_lower=ball_record(Zlo),
            height_chart='analytic Q=F_z/r including r=0',
            N_factorization='n=-a^2*((1+beta_theta)*cos(gamma)*Q-gamma_theta*v)',
            factor_moduli_lower=[ball_record(x) for x in (alo, Plo, clo, Qlo)],
            P_real_boundary_lower=self.last_P_boundary_lowers,
            D_product_minus_remainder_lower=ball_record(Dlo),
            full_ell_modulus_upper=ball_record(ell.upper()))
        return {key:value.upper() for key, value in
                dict(a=A, b=B, c=C, tau=d0+omega*ell*ell, sigma=omega*ell).items()}



