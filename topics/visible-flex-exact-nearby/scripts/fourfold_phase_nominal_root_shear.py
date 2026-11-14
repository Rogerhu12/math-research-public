#!/usr/bin/env python3
"""A fixed real analytic root-shear reference and its full operator error.

The exact midpoint trigonometric polynomials define only the computational
reference. The entire actual parameter family is compared with it in L2
operator norm, before finite canonical or physical truncation is applied.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path

from flint import arb, ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_root_fourier_fit import read, save, sha, stored, decode, dyadic


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--fit', type=Path, default=Path('notes/2026-11-12-actual-root-Fourier-fit-and-H-primitive.json.gz'))
    p.add_argument('--bits', type=int, default=320)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args(); ctx.prec = a.bits
    fit = read(a.fit)
    if not fit['proved'] or sha(fit['grid_manifest_path']) != fit['grid_manifest_sha256']:
        raise ValueError('actual root Fourier fit is incomplete or changed')
    if sha(fit['complex_root_path']) != fit['complex_root_sha256']:
        raise ValueError('complete actual root strip changed')
    Y, V = [fit['fields'][name] for name in ('Y_prime', 'residual_v0')]
    yc, vc = [[decode(c) for c in field['nonnegative_cosine_DFT_coefficients']] for field in (Y,V)]
    Kf = len(yc)-1
    if len(vc) != len(yc):
        raise ValueError('the two exact physical polynomial grids differ')
    q = stored(fit['true_frequency']); q0 = decode(fit['finite_H_frequency_dyadic'])
    dq = abs(q-q0).upper(); qlo = min(q.lower(), q0)
    EY, EV = [stored(field['uniform_real_error']).upper() for field in (Y,V)]
    EH = stored(fit['true_H_minus_finite_H_real_uniform_error']).upper()
    m = stored(fit['true_Hprime_complex_real_lower']).lower()
    M = stored(fit['true_Hprime_complex_modulus_upper']).upper()
    my = stored(Y['complete_outer_strip_modulus']).upper()
    absolute_sum = lambda c: abs(c[0])+2*sum((abs(v) for v in c[1:-1]),arb(0))+abs(c[-1])
    Ysize = min(my+EY, absolute_sum(yc).upper())
    Vsize = min(stored(V['complete_outer_strip_modulus']).upper()+EV, absolute_sum(vc).upper())
    Vderivative = (2*sum((4*n*abs(vc[n]) for n in range(1,Kf)),arb(0))
                   +4*Kf*abs(vc[Kf])).upper()
    hp_error = (q.upper()*EY+dq*Ysize+abs(q0*yc[0]-1)).upper()
    nominal_lower = (m-hp_error).lower()
    if not nominal_lower > 0:
        raise ValueError('the exact nominal root map is not certified orientation preserving')
    nu_error = (EV+Vderivative*EH/m).upper()
    # The shared canonical coordinate has period pi/2 for both maps.
    # nu_ref=finite_v0_residual composed with the inverse nominal map.
    L = arb(2048)
    da = dq/(4*qlo*q0)
    dt = dq/(L*qlo)
    a_nonzero = 1/(4*qlo)
    constant_q_error = 5050*(2*a_nonzero*da+2*dt/L)
    residual_q_error = 2*Vsize*(da+dt/L)
    potential_error = nu_error*(1+L**(-2))
    canonical_error = constant_q_error+residual_q_error+potential_error
    D_norm = 5050*(1-L**(-2))+Vsize*(1+L**(-2))
    D_derivative = 5050/(4*q0*q0)+(Vsize/q0)*(1+1/L)
    map_error = hp_error/nominal_lower*D_norm+2*(M/nominal_lower).sqrt()*EH*D_derivative
    full_error = (canonical_error+map_error).upper()
    low = 0
    while 4*q0*(low+1) < L:
        low += 1
    Sfrac = Fraction(fit['exact_physical_strip']); S = arb(Sfrac.numerator)/Sfrac.denominator
    hp_complex = (1+q0*(2*sum((abs(yc[n])*(4*n*S).cosh()
                       for n in range(1,Kf)),arb(0))+abs(yc[Kf])*(4*Kf*S).cosh())).upper()
    hp_real_loss = (q0*(2*sum((abs(yc[n])*((4*n*S).cosh()-1)
                       for n in range(1,Kf)),arb(0))+abs(yc[Kf])*((4*Kf*S).cosh()-1))).upper()
    hp_complex_real_lower = (nominal_lower-hp_real_loss).lower()
    if not hp_complex_real_lower > 0:
        raise ValueError('nominal root half-density has no proved branch on the requested strip')
    H_imaginary = (S+q0*(2*sum((abs(yc[n])*(4*n*S).sinh()/(4*n)
                      for n in range(1,Kf)),arb(0))+abs(yc[Kf])*(4*Kf*S).sinh()/(4*Kf))).upper()
    nu_complex = (abs(vc[0])+2*sum((abs(vc[n])*(4*n*S).cosh()
                      for n in range(1,Kf)),arb(0))+abs(vc[Kf])*(4*Kf*S).cosh()).upper()
    report = dict(kind='actual_full_root_shear_comparison_with_fixed_nominal_operator', proved=True,
        source_sha256=sha(__file__), bits=a.bits, fit_path=str(a.fit), fit_sha256=sha(a.fit),
        dependencies={name:sha(Path(__file__).parent/name) for name in
            ('fourfold_phase_root_fourier_fit.py','fourfold_phase_beta_interval.py')},
        identity=fit['identity'], true_frequency=fit['true_frequency'], nominal_frequency_dyadic=dyadic(q0),
        canonical_nominal_low_cutoff=low, nominal_low_dimension=2*low+1,
        complete_shear_difference_rank_upper=2*(2*low+1),
        definitions=dict(H0='theta+q0*zero_mean_primitive(P_Y)', H0prime='1+q0*(P_Y-c_Y0)',
            nu0='P_v composed with H0 inverse', U0='sqrt(H0prime)*(f composed with H0)',
            Delta0='U0*[5050*(A0^2-T0^2)+A0*M_nu0*A0-T0*M_nu0*T0]*U0star'),
        true_map_real_error=ball_record(EH), true_map_derivative_real_error=ball_record(hp_error),
        nominal_map_derivative_real_lower=ball_record(nominal_lower),
        nominal_residual_potential_real_modulus=ball_record(Vsize),
        physical_finite_potential_derivative_modulus=ball_record(Vderivative),
        true_minus_nominal_canonical_potential_uniform_error=ball_record(nu_error),
        A_frequency_error=ball_record(da.upper()), T_frequency_error=ball_record(dt.upper()),
        canonical_constant_frequency_error=ball_record(constant_q_error.upper()),
        canonical_residual_frequency_error=ball_record(residual_q_error.upper()),
        canonical_potential_error=ball_record(potential_error.upper()),
        nominal_canonical_shear_operator_modulus=ball_record(D_norm.upper()),
        nominal_canonical_shear_first_derivative_operator_modulus=ball_record(D_derivative.upper()),
        full_change_of_angle_operator_error=ball_record(map_error.upper()),
        complete_actual_minus_nominal_shear_operator_error=ball_record(full_error),
        exact_physical_strip=str(Sfrac), nominal_Hprime_complex_modulus=ball_record(hp_complex),
        nominal_Hprime_complex_real_lower=ball_record(hp_complex_real_lower),
        nominal_H_imaginary_modulus=ball_record(H_imaginary),
        nominal_physical_potential_complex_modulus=ball_record(nu_complex),
        true_canonical_inverse_strip=fit['strict_canonical_image_strip'],
        true_residual_potential_complex_modulus=V['complete_outer_strip_modulus'],
        scope=['The comparison is a full L2 operator estimate for the entire actual narrow parameter family.',
               'Both root-angle half-density changes are actual onto unitaries; their full shear outputs have one controlled derivative.',
               'The exact mean, frequency dependence, low cross terms and infinite Fourier modes are retained.',
               'No finite physical column matrix or complete feedback inverse has been computed by this aggregation.'])
    save(a.out,report)
    print(dict(proved=True, low=low, full_error=report['complete_actual_minus_nominal_shear_operator_error'],
               nominal_potential=report['nominal_residual_potential_real_modulus'],
               nominal_Hprime_complex_real_lower=report['nominal_Hprime_complex_real_lower'],
               nominal_H_imaginary=report['nominal_H_imaginary_modulus'],
               nominal_potential_complex=report['nominal_physical_potential_complex_modulus']),flush=True)


if __name__ == '__main__':
    main()
