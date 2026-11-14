#!/usr/bin/env python3
"""Complete actual parameter nodes at arbitrary admissible even DFT lengths.

This copies the full frozen central sample formulas and their infinite
primitive fees.  Only the old power-of-two guard is generalized: the actual
NativeSeriesFFT uses Arb's finite acb.dft at any positive length.  All finite
primitive and phase frequencies are checked injective modulo N.  Thus the
inverse DFT evaluates exactly the same trigonometric polynomials at the new
N points; no new alias or primitive-tail assumption is introduced.  The
caller still pays complete true-field Fourier/time reconstruction and the
actual joint node RMS at this new grid.  Uniform fields use their genuine
interval target and true root jets through precisely the same method.
"""
from __future__ import annotations
from fractions import Fraction
import time
import numpy as np
from flint import arb,acb,acb_series,ctx
from fourfold_phase_parameter_time_circle import (
    exact_arb,parameter_series,normalized_total,primitive_fourier_budget,
    complex_pad,absup,ball_record,f_invariants,NativeSeriesFFT,
)

def sample_parameter_grid(field, u, angles, imaginary_theta=Fraction(0)):
    """True central [f,fp,fpp] arrays at one complex normalized time."""
    u, width = acb(u), exact_arb(Fraction(imaginary_theta))
    if not abs(u).upper() < field.outer or not abs(width) < field.strip:
        raise ValueError("parameter sample leaves paid time/angle domain")
    angles = int(angles)
    if angles < field.nodes or angles < 2 or angles % 2:
        raise ValueError("even angle nodes at least the complete primitive grid required")
    if not isinstance(field.target.fourier,NativeSeriesFFT):
        raise ValueError("arbitrary-length native Arb DFT engine required")
    slots=[(int(frequency)//4)%angles for frequency in field.target.frequency]
    if len(slots)!=len(set(slots)):
        raise ValueError("finite primitive frequencies collide on this evaluation grid")
    oldcap, ctx.cap = ctx.cap, 7
    wall, cpu = time.monotonic(), time.process_time()
    try:
        if field.turn and u.imag == 0 and u.real.is_exact():
            exact_u = Fraction(str(u.real.fmpq()))
            if (field.base.exact_eta0+field.base.exact_eta1*exact_u).is_zero():
                result = np.empty((angles, 3), object); result.fill(acb(0))
                return result, dict(exact_turn_zero=True)
        tau = acb(field.tau0)+field.h*u
        sine, cosine = tau.sin(), tau.cos()
        radial, rp, rpp = field.root*sine, field.tp*sine, field.tpp*sine
        data = field.target.parameter_target2(radial, arb(1), field.common_budgets)
        F, Fp, Fpp, _, _ = field.target.last_primitive
        coefficient = np.empty((angles, 9), object)
        coefficient.fill(None)
        for key in np.ndindex(coefficient.shape):
            coefficient[key] = parameter_series([0, 0, 0])
        for k, frequency in enumerate(field.target.frequency):
            weight = (-frequency*width).exp()
            for component in range(3):
                values = normalized_total(F[k, component], Fp[k, component], Fpp[k, component],
                                          arb(1), rp, rpp, radial_order=1)
                coefficient[(frequency//4) % angles, component] = parameter_series(values)*weight
        beta, gamma, _, _ = field.target.scalars(radial, -1)
        bp, gp, _, _ = field.target.direction_scalars(radial, -1)
        zero = acb_series([0], prec=ctx.cap)
        phase = []
        for order in (0, 1):
            for row, change in ((beta, bp), (gamma, gp)):
                phase.append([parameter_series(normalized_total(v, vp, zero, arb(1), rp, rpp,
                                              radial_order=order)) for v, vp in zip(row, change)])
        if 2*len(phase[0])>=angles:
            raise ValueError("finite phase frequencies collide on this evaluation grid")
        for k, values in enumerate(zip(*phase), 1):
            for sign in (-1, 1):
                frequency = 4*sign*k
                factor, slot = acb(0, -sign)*(-frequency*width).exp()/2, (sign*k) % angles
                coefficient[slot, 3:7] = [v*factor for v in values]
                coefficient[slot, 7] = values[0]*factor*acb(0, frequency)
                coefficient[slot, 8] = values[1]*factor*acb(0, frequency)
        samples = field.target.fourier.fft(coefficient, inverse=True)*angles
        primitive_errors = [primitive_fourier_budget(field.nodes, field.sigma, 4*abs(width), field.R0,
            b["radius_bound"], b["height_bound"], b["tangent_bound"])[0][0] for b in field.common_budgets]
        e0, e1, e2 = primitive_errors
        fees = [(e0/field.R0).upper(),
                (e1/field.R0+absup(rp)*2*e0/field.R0**2).upper(),
                ((e2/field.R0+2*absup(rp)*2*e1/field.R0**2
                   +absup(rp)**2*6*e0/field.R0**3+absup(rpp)*2*e0/field.R0**2)/2).upper()]
        if field.turn:
            wave = field.deflation.wave_parameter_series(acb(field.base.eta0)+field.base.eta1*u)
        else:
            Ktotal = parameter_series(normalized_total(data["K"], data["Kp"], data["Kpp"],
                                        arb(1), rp, rpp))
            if not (-Ktotal[0]).real > 0:
                raise ValueError("actual ordinary curvature branch enclosure failed")
            wave = (-Ktotal).sqrt()
        rtau = parameter_series([field.root*cosine, field.tp*cosine, field.tpp*cosine/2])
        result = np.empty((angles, 3), object)
        minimum_D = None
        for j in range(angles):
            X = [parameter_series([complex_pad(samples[j, c][p], fees[p])
                                   for p in range(3)]) for c in range(3)]
            D, M, W = f_invariants(X, samples[j, 3:])
            if not D[0].abs_lower() > 0:
                raise ValueError("pointwise actual D enclosure contains zero")
            minimum_D = D[0].abs_lower() if minimum_D is None else min(minimum_D, D[0].abs_lower())
            value = -rtau*(M+field.sign*wave*W)/D
            result[j] = [value[0], value[1], 2*value[2]]
        return result, dict(primitive_X_normalized_parameter_fees=list(map(ball_record, fees)),
            sample_D_lower=ball_record(minimum_D), elapsed_seconds=time.monotonic()-wall,
            cpu_seconds=time.process_time()-cpu, complex_E_preserved=True)
    finally:
        ctx.cap = oldcap
