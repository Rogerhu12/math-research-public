#!/usr/bin/env python3
"""Correlated radial Taylor primitive for a true single-span core generator.

The finite primitive is Taylor expanded before taking any radial interval.
Fourier modes therefore retain their radial decay. Both its complete radial
Taylor remainder and the existing infinite primitive remainder are paid.
No completed core propagation or infinite Schur inverse is asserted here.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import time
import traceback

import numpy as np
from flint import arb, acb, acb_mat, ctx

from fourfold_native_series_fft import NativeSeriesFFT
from fourfold_phase_beta_affine import provenance
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_bulk_box import (
    CBox, Box, arb_box, reduce_box, cstack, zeros, cdot, ccross,
    complex_sincos, trig_jets, jet_product, stack)
from fourfold_phase_beta_interval import (
    ball_record, primitive_fourier_budget, analytic_tail_derivative)
from fourfold_phase_actual_positive_cap import complex_separation
from fourfold_phase_core_low_coefficients import TrueCoreCoefficientTarget, extend_half


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def frobenius(value):
    # abs(z) may be an Arb enclosure whose representational lower endpoint
    # is slightly negative when z contains zero. Squaring that ball and then
    # taking sqrt can return nan. Square exact nonnegative upper bounds.
    bounds = [abs(value[i, j]).upper() for i in range(value.nrows())
              for j in range(value.ncols())]
    if any(not x.is_finite() for x in bounds):
        raise ValueError('nonfinite entry in a claimed matrix norm bound')
    answer = sum((x*x for x in bounds), arb(0)).sqrt().upper()
    if not answer.is_finite():
        raise ValueError('nonfinite matrix norm upper bound')
    return answer


def complex_record(value):
    return dict(real=ball_record(value.real), imag=ball_record(value.imag))


def matrix_record(value):
    return [[complex_record(value[i, j]) for j in range(value.ncols())]
            for i in range(value.nrows())]


class CorrelatedCoreTarget(TrueCoreCoefficientTarget):
    def __init__(self, *args, native_order=32, native_radius=Fraction(1, 64), **kwargs):
        super().__init__(*args, **kwargs)
        if native_order <= 3:
            raise ValueError('the primitive Taylor degree must support three radial derivatives')
        self.native_order = int(native_order)
        self.native_radius = exact_arb(Fraction(native_radius))
        self.fourier = NativeSeriesFFT()
        self.native_key = None
        self.native_poly = None
        self.native_majorants = {}

    def set_cell(self, left, right):
        super().set_cell(left, right)
        key = self.cell, ctx.prec, self.native_order
        if key != self.native_key:
            # Only the current cell's primitive is retained in memory.
            self.native_key = key
            self.native_poly = None
            self.native_majorants = {}

    def build_native_taylor(self):
        if self.native_poly is not None:
            return
        old_cap = ctx.cap
        try:
            ctx.cap = max(21, self.native_order)
            coefficients, _ = self.primitive(acb(self.anchor), 1)
            result = zeros((self.native_order, self.nodes, 3))
            for k in range(self.nodes):
                for component in range(3):
                    for j in range(self.native_order):
                        result[j, k, component] = CBox.from_acb(coefficients[k, component][j])
            self.native_poly = result
            self.native_budget = self.analytic_input_budget(
                self.anchor, self.native_radius, self.tail_sigma, self.native_radius/2)
        finally:
            ctx.cap = old_cap

    def scalar_data(self, radial):
        # Complete degree-20 scalar germ, including the exact affine parameter.
        delta = CBox.from_acb(radial-acb(self.anchor))
        jet = zeros((4, 2*self.modes+2))
        for j in range(20, -1, -1):
            jet = jet*delta+cstack([self.scalar_poly[j], jet[0], 2*jet[1], 3*jet[2]])
        beta = jet[:, :self.modes]
        gamma = jet[:, self.modes:2*self.modes]
        radius, height = jet[:, -2], jet[:, -1]
        self.last_scalar = beta, gamma, radius, height
        return radius

    def finite_data(self, radial):
        self.build_native_taylor()
        radius = self.scalar_data(radial)
        delta = CBox.from_acb(radial-acb(self.anchor))
        jet = zeros((4, self.nodes, 3))
        for j in range(self.native_order-1, -1, -1):
            jet = jet*delta+cstack([self.native_poly[j], jet[0], 2*jet[1], 3*jet[2]])
        return jet, radius

    def tail_errors(self, radial, inner_sigma=arb(0)):
        self.build_native_taylor()
        infinite = super().tail_errors(radial, inner_sigma)
        distance = abs(radial-acb(self.anchor)).upper()
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

    def complete_fast_data(self, radial):
        coefficient, radius = self.finite_data(radial)
        errors = self.tail_errors(radial)
        reverse = (-np.arange(self.nodes)) % self.nodes
        E0 = cdot(coefficient[1], coefficient[1, reverse]).sum()
        E1 = 2*cdot(coefficient[1], coefficient[2, reverse]).sum()
        eps = [arb_box(math.factorial(j)*errors[0]/self.tail_radius**j)
               for j in range(3)]
        bounds = [Box(np.max(reduce_box(Box(coefficient[j].magnitude_upper())).hi))
                  for j in range(3)]
        fees = [3*(2*bounds[1]*eps[1]+eps[1]*eps[1]),
                6*(bounds[1]*eps[2]+bounds[2]*eps[1]+eps[1]*eps[2])]
        real = radial.imag == 0
        E0, E1 = [value.pad(fee, real) for value, fee in zip((E0, E1), fees)]
        a, ar, arr = radius[0], radius[1], radius[2]
        alo = complex_separation(a, 'the exact radius germ')
        elo = complex_separation(E0, 'the true target E')
        K = (ar*E1-2*arr*E0)/(2*a*E0*E0)
        if real:
            K = CBox(K.real)
        self.last_curvature_domain = dict(
            radius_modulus_lower=ball_record(alo),
            E_modulus_lower=ball_record(elo),
            target_K=complex_record(K.to_acb()))
        return coefficient, K, None, errors, real

    def fast_fields(self, radial, coefficient, errors, real, sigma=None):
        if sigma is not None:
            errors = self.tail_errors(radial, sigma+arb.pi()/self.angles)
            modes = np.abs(np.asarray(self.frequency)//4)
            variation = stack([arb_box((abs(int(k))*sigma).exp()
                *abs(int(k))*arb.pi()/self.angles
                +(abs(int(k))*sigma).exp()-1) for k in modes]).reshape(-1, 1)
        fields = {}
        for radial_order in range(3):
            values = coefficient[radial_order]
            fee = arb_box(math.factorial(radial_order)*errors[0]/self.tail_radius**radial_order)
            data = zeros((self.angles, 3))
            data[(np.asarray(self.frequency)//4) % self.angles] = values
            samples = (self.fast_fourier.fft(data, inverse=True)*self.angles)[:self.sample_count]
            if sigma is None:
                fields[radial_order, 0] = samples.pad(fee, real)
            else:
                # Both components of a complex-r center remain complex.
                # No real-axis projection is made on this bidisk cover.
                var = (fee+reduce_box(Box(values.magnitude_upper())*variation)).hi
                fields[radial_order, 0] = CBox(
                    samples.real+Box(-var, var), samples.imag+Box(-var, var))
        beta, gamma, radius, _ = self.last_scalar
        ss, cc = self.angle_sines, self.angle_cosines
        if sigma is not None:
            key = sigma.str(35)
            if key not in self.angle_shift_cache:
                gap, width = arb_box(arb.pi()/self.angles).hi, arb_box(sigma).hi
                shift = CBox(Box(-gap, gap), Box(-width, width))
                s, c = complex_sincos(CBox(np.arange(1, self.modes+1))*shift)
                s, c = s.reshape(-1, 1), c.reshape(-1, 1)
                self.angle_shift_cache[key] = ss*c+cc*s, cc*c-ss*s
            ss, cc = self.angle_shift_cache[key]
        b = (beta.reshape(4, self.modes, 1)
             *ss.reshape(1, self.modes, self.sample_count)).sum(1)
        g = (gamma.reshape(4, self.modes, 1)
             *ss.reshape(1, self.modes, self.sample_count)).sum(1)
        sb, cb = trig_jets(b)
        sg, cg = trig_jets(g)
        T = cstack([-jet_product(cg, sb), jet_product(cg, cb), sg], -1)
        modes = CBox((4*np.arange(1, self.modes+1)).reshape(-1, 1))
        bt = (beta[0].reshape(-1, 1)*modes*cc).sum()
        gt = (gamma[0].reshape(-1, 1)*modes*cc).sum()
        dT = cstack([sg[0]*gt*sb[0]-cg[0]*cb[0]*bt-T[0, :, 1],
                     -sg[0]*gt*cb[0]-cg[0]*sb[0]*bt+T[0, :, 0],
                     cg[0]*gt], -1)
        fields[0, 1] = radius[0]*T[0]
        fields[1, 1] = radius[1]*T[0]+radius[0]*T[1]
        fields[0, 2] = radius[0]*dT
        if real and sigma is None:
            for key in ((0, 1), (1, 1), (0, 2)):
                fields[key] = CBox(fields[key].real)
        return fields

    def coefficient_values(self, radial, coefficient, K0, errors, sigma=None):
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
        if radial == acb(0):
            zlo = complex_separation(X[:, 2], 'the waist Fr_z')
            ell = Frt[:, 2]/X[:, 2]-cdot(F, Y)/R2
        else:
            if radial.real.contains(0) and radial.imag.contains(0):
                raise ValueError('a waist disk requires the separately removable Fz/r implementation')
            zlo = complex_separation(F[:, 2], 'the ordinary F_z')
            ell = Y[:, 2]/F[:, 2]-cdot(F, Y)/R2
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
            Nraw_modulus_lower=ball_record(nlo), height_numerator_modulus_lower=ball_record(zlo))
        return values



    def phase_boundary_P_lower(self, radial, strip):
        """Re(1+beta_theta) on both angular strip boundaries, correlated in r."""
        gap = arb_box(arb.pi()/self.angles).hi
        modes = CBox(np.arange(1, self.modes+1).reshape(-1, 1))
        shift = CBox(Box(-gap, gap))
        sgap, cgap = complex_sincos(modes*shift)
        ss = self.angle_sines*cgap+self.angle_cosines*sgap
        cc = self.angle_cosines*cgap-self.angle_sines*sgap
        ch = stack([arb_box((j*strip).cosh()) for j in range(1, self.modes+1)]).reshape(-1, 1)
        sh = stack([arb_box((j*strip).sinh()) for j in range(1, self.modes+1)]).reshape(-1, 1)
        delta = CBox.from_acb(radial-acb(self.anchor))
        lowers = []
        for sign in (-1, 1):
            boundary_cosine = CBox(cc.real*ch, -sign*ss.real*sh)
            value = CBox(np.zeros(self.sample_count))
            for radial_order in range(20, -1, -1):
                coefficient = self.scalar_poly[radial_order, :self.modes].reshape(-1, 1)
                angular = (coefficient*(4*modes)*boundary_cosine).sum(0)
                value = value*delta+angular
            lowers.append(arb(float(np.min((1+value).real.lo))))
        lower = min(lowers).lower()
        self.last_P_boundary_lowers = [ball_record(x) for x in lowers]
        if not lower > 0:
            raise ValueError('correlated boundary Re(1+beta_theta) lower is '+lower.str(18))
        # For every fixed complex r in the box, Re P is harmonic and periodic
        # in angular x. Its minimum on the full closed strip is at y=+-strip.
        return lower


    def coefficient_moduli_bidisk(self, radial, coefficient, K0, errors, strip):
        """Whole angular strip moduli without dividing a wrapping N rectangle."""
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
        if radial == acb(0):
            Zlo = complex_separation(X[:, 2], 'waist Fr_z on the whole angular strip')
            ell = upper(Frt[:, 2])/Zlo+upper(cdot(F, Y))/Rlo
        else:
            if radial.real.contains(0) and radial.imag.contains(0):
                raise ValueError('a waist disk needs an analytic Fz/r quotient')
            Zlo = complex_separation(F[:, 2], 'ordinary F_z on the whole angular strip')
            ell = upper(Y[:, 2])/Zlo+upper(cdot(F, Y))/Rlo
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
            height_numerator_modulus_lower=ball_record(Zlo),
            N_factorization='n=-a^2*((1+beta_theta)*cos(gamma)*Q-gamma_theta*v)',
            factor_moduli_lower=[ball_record(x) for x in (alo, Plo, clo, Qlo)],
            P_real_boundary_lower=self.last_P_boundary_lowers,
            D_product_minus_remainder_lower=ball_record(Dlo),
            full_ell_modulus_upper=ball_record(ell.upper()))
        return {key:value.upper() for key, value in
                dict(a=A, b=B, c=C, tau=d0+omega*ell*ell, sigma=omega*ell).items()}



    def whole_generator_modulus(self, radial, cutoff, momentum_scale=8):
        """Holomorphic finite generator on a complex r box by scalar accretivity.

        Only the full real angular circle is needed for this radial Cauchy
        domain. Angular analytic strips are paid separately at each time-DFT
        node. This avoids treating correlated Fourier coefficients as arbitrary
        unrelated matrix entries on a broad radial box.
        """
        coefficient, curvature, _, errors, _ = self.complete_fast_data(radial)
        values = self.coefficient_values(radial, coefficient, curvature, errors, arb(0))
        lower = arb(float(np.min(values['a'].real.lo))).lower()
        if not lower > 0:
            raise ValueError('whole real-angle accretivity Re a lower is '+lower.str(18))
        moduli = {key:arb(float(np.max(value.magnitude_upper()))).upper()
                  for key, value in values.items()}
        lam = arb(4*cutoff)
        scale = exact_arb(Fraction(momentum_scale))
        if not scale > 0:
            raise ValueError('positive momentum scale required')
        inverse = (1/lower).upper()
        f11 = (inverse*moduli['b']*lam).upper()
        f12 = (scale*inverse).upper()
        H = (moduli['tau']+2*lam*moduli['sigma']).upper()
        f21 = ((lam*lam*moduli['b']**2*inverse
                +lam*lam*moduli['c']+H)/scale).upper()
        total = (2*f11*f11+f12*f12+f21*f21).sqrt().upper()
        self.last_generator_domain = dict(
            all_real_angular_cells_covered=True,
            geometric_denominators=self.last_geometric_domain,
            target_curvature_denominators=self.last_curvature_domain,
            true_scalar_real_part_a_lower=ball_record(lower),
            finite_projected_A_inverse_operator_bound=ball_record(inverse),
            proof_of_inverse='Re <P_N a P_N v,v> = integral Re(a)|v|^2 >= lower*||v||^2 for every complex retained vector.',
            coefficient_full_real_angle_moduli={key:ball_record(value) for key,value in moduli.items()},
            true_zero_order_operator_modulus=ball_record(H),
            zero_order_identity='H=P_N tau P_N + D(P_N sigma P_N)-(P_N sigma P_N)D, ||D||=4N.',
            block_operator_moduli=[[ball_record(f11),ball_record(f12)],
                                   [ball_record(f21),ball_record(f11)]],
            scaled_generator_operator_upper=ball_record(total),
            primitive_remainders=self.last_native_remainders,
            angular_strip_scope='This outer radial holomorphy proof uses the full real angular circle. It makes no outer-r times nonzero-angle-strip claim; sample-node angular aliases are paid independently.')
        return total


    def projected_generator(self, radial, cutoff, normalized_strip, momentum_scale=8):
        coefficient, curvature, _, errors, real = self.complete_fast_data(radial)
        values = self.coefficient_values(radial, coefficient, curvature, errors)
        moduli = self.coefficient_moduli_bidisk(radial, coefficient, curvature, errors, normalized_strip)
        coefficients = {}
        for name, value in values.items():
            parity = -1 if name in ('b', 'sigma') else 1
            transformed = self.fast_fourier.fft(extend_half(value, parity))/self.angles
            rows = {}
            for lag in range(-2*cutoff, 2*cutoff+1):
                alias = moduli[name]*(
                    (-(self.angles-abs(lag))*normalized_strip).exp()
                    +(-(self.angles+abs(lag))*normalized_strip).exp()
                )/(1-(-self.angles*normalized_strip).exp())
                error = arb(0, alias.upper())
                rows[lag] = transformed[lag % self.angles].to_acb()+acb(error, error)
            coefficients[name] = rows
        indices = list(range(-cutoff, cutoff+1))
        n = len(indices)
        matrices = {key:acb_mat([[row[i-j] for j in indices] for i in indices])
                    for key, row in coefficients.items()}
        A, B, C = [matrices[name] for name in ('a', 'b', 'c')]
        H = acb_mat([[coefficients['tau'][i-j]
            +acb(0, 4*(i-j))*coefficients['sigma'][i-j] for j in indices] for i in indices])
        D = acb_mat([[acb(0, 4*i) if i == j else 0 for j in indices] for i in indices])
        inverse = A.inv()
        scale = exact_arb(Fraction(momentum_scale))
        F11, F12 = -inverse*B*D, scale*inverse
        F21 = (D*B*inverse*B*D-D*C*D-H)/scale
        F22 = -D*B*inverse
        generator = acb_mat([[([F11, F12] if i < n else [F21, F22])[j//n][i % n, j % n]
                              for j in range(2*n)] for i in range(2*n)])
        if not all(generator[i, j].is_finite() for i in range(2*n) for j in range(2*n)):
            raise ValueError('projected A inverse is not verified on this entire complex box')
        self.last_generator_domain = dict(
            all_angular_cells_covered=True,
            geometric_denominators=self.last_geometric_domain,
            target_curvature_denominators=self.last_curvature_domain,
            coefficient_strip_moduli={key:ball_record(value) for key, value in moduli.items()},
            primitive_remainders=self.last_native_remainders,
            finite_projected_A_inverse_frobenius=ball_record(frobenius(inverse)),
            scaled_generator_frobenius_upper=ball_record(frobenius(generator)))
        return generator


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--object', type=Path, default=Path(
        'data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    parser.add_argument('--common-span', type=int, default=90)
    parser.add_argument('--modes', type=int, default=4)
    parser.add_argument('--primitive-nodes', type=int, default=512)
    parser.add_argument('--angles', type=int, default=1024)
    parser.add_argument('--bits', type=int, default=192)
    parser.add_argument('--native-order', type=int, default=32)
    parser.add_argument('--native-radius', type=Fraction, default=Fraction(1, 64))
    parser.add_argument('--outer-radius', type=Fraction, default=Fraction(3))
    parser.add_argument('--normalized-strip', type=Fraction, default=Fraction(1, 16))
    parser.add_argument('--momentum-scale', type=Fraction, default=Fraction(8))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec, ctx.cap = args.bits, 4
    wall, cpu = time.monotonic(), time.process_time()
    report = dict(kind='single_span_true_core_correlated_radial_Taylor_domain',
        complete=False, source_sha256=sha(__file__), bits=args.bits,
        common_span_index=args.common_span, modes=args.modes,
        primitive_nodes=args.primitive_nodes, angular_nodes=args.angles,
        native_order=args.native_order, native_radius=str(args.native_radius),
        normalized_outer_radius=str(args.outer_radius),
        normalized_angular_strip=str(args.normalized_strip),
        momentum_scale=str(args.momentum_scale),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_native_series_fft.py','fourfold_phase_beta_affine.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_bulk_box.py',
            'fourfold_phase_beta_interval.py','fourfold_phase_core_low_coefficients.py',
            'fourfold_phase_actual_positive_cap.py')},
        scope='Only the stated finite projected generator and exact common-span analytic extension; no cell flow, full core DN, or infinite Schur inverse.')
    try:
        target = CorrelatedCoreTarget(args.object, args.primitive_nodes, args.angles,
            arb('.003'), arb('.0025'), arb('.32'),
            native_order=args.native_order, native_radius=args.native_radius)
        report.update({key:value for key, value in provenance(target, args.object).items()
                       if key not in ('source_sha256', 'dependency_sha256')})
        points = sorted({Fraction(0), Fraction(1, 4)}
            |{x for x in target.common_cells() if 0 < x < Fraction(1, 4)})
        if not 0 <= args.common_span < len(points)-1:
            raise ValueError('requested half-core common span is absent')
        left, right = points[args.common_span:args.common_span+2]
        target.set_cell(left, right)
        center, half = (left+right)/2, (right-left)/2
        report.update(exact_common_span=[str(left), str(right)],
                      exact_center=str(center), exact_halfwidth=str(half))
        width = exact_arb(half*args.outer_radius)
        radial = acb(exact_arb(center)+arb(0, width), arb(0, width))
        modulus = target.whole_generator_modulus(radial, args.modes, args.momentum_scale)
        report.update(complete=True, actual_whole_complex_domain=target.last_generator_domain,
                      true_projected_generator_operator_modulus=ball_record(modulus))
    except Exception as exc:
        report.update(failure=repr(exc), traceback=traceback.format_exc())
    report.update(CPU_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-wall)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key:report.get(key) for key in
        ('complete','exact_common_span','failure','CPU_seconds','wall_seconds')}), flush=True)
    if not report['complete']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
