#!/usr/bin/env python3
"""Complete canonical coefficients of the fixed R92 nominal potential.

The nonuniform quadrature is enclosed. Native Arb computes the unit roots;
binary64 complex powers carry an explicit absolute roundoff induction, not
an assumed libm accuracy. All physical trapezoidal aliases are paid on the
complete analytic strip of the fixed finite reference functions.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
import time

import numpy as np
from flint import acb, arb, ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_root_fourier_fit import read, save, sha, stored, decode, dyadic


def evaluate_cosine(coefficients, grid):
    K = len(coefficients)-1
    if grid <= 2*K:
        raise ValueError('evaluation grid must exceed twice the exact finite degree')
    padded = [acb(0) for _ in range(grid)]
    padded[0] = coefficients[0]
    for n in range(1,K):
        padded[n] = padded[-n] = acb(coefficients[n])
    padded[K] = padded[-K] = acb(coefficients[K]/2)
    values = [v*grid for v in acb.dft(padded,inverse=True)]
    if any(not z.imag.contains(0) for z in values):
        raise ValueError('exact real cosine polynomial lost its real axis')
    return [z.real for z in values]


def evaluate_angle(coefficients,q0,grid):
    K = len(coefficients)-1
    padded = [acb(0) for _ in range(grid)]
    for n in range(1,K):
        padded[n] = acb(0,-q0*coefficients[n]/(4*n))
        padded[-n] = padded[n].conjugate()
    padded[K] = acb(0,-q0*coefficients[K]/(8*K))
    padded[-K] = padded[K].conjugate()
    values = [v*grid for v in acb.dft(padded,inverse=True)]
    if any(not z.imag.contains(0) for z in values):
        raise ValueError('exact real sine primitive lost its real axis')
    return [v.real+arb.pi()*j/(2*grid) for j,v in enumerate(values)]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--nominal',type=Path,default=Path('notes/2026-11-12-actual-to-nominal-root-shear.json'))
    p.add_argument('--modes',type=int,default=2048)
    p.add_argument('--grid',type=int,default=16384)
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec=a.bits
    if (a.grid<4 or a.grid&(a.grid-1) or a.modes<1 or sys.float_info.mant_dig!=53
            or np.dtype(np.complex128).itemsize!=16):
        raise ValueError('the explicit binary64 quadrature contract is not met')
    wall,cpu=time.monotonic(),time.process_time()
    nominal=read(a.nominal)
    if not nominal['proved'] or sha(nominal['fit_path'])!=nominal['fit_sha256']:
        raise ValueError('the complete nominal root-map comparison changed')
    fit=read(nominal['fit_path'])
    yc,vc=[[decode(c) for c in fit['fields'][name]['nonnegative_cosine_DFT_coefficients']]
           for name in ('Y_prime','residual_v0')]
    q0=decode(nominal['nominal_frequency_dyadic'])
    y=evaluate_cosine(yc,a.grid);v=evaluate_cosine(vc,a.grid)
    angle=evaluate_angle(yc,q0,a.grid)
    weights=np.empty(a.grid,dtype=np.float64);roots=np.empty(a.grid,dtype=np.complex128)
    mean_weight_error=arb(0);mean_weight_size=arb(0)
    root_error=angle_error=arb(0)
    for j in range(a.grid):
        hp=1+q0*(y[j]-yc[0])
        if not hp>0:raise ValueError('positive exact nominal angle Jacobian unresolved')
        weight=hp*v[j];middle=float(weight.mid());weights[j]=middle
        mean_weight_error+=abs(weight-arb(middle)).upper()
        mean_weight_size+=abs(arb(middle))
        angle_middle=float(angle[j].mid())
        angle_error=max(angle_error,abs(angle[j]-arb(angle_middle)).upper())
        phase=acb(0,-4*arb(angle_middle)).exp()
        z=complex(float(phase.real.mid()),float(phase.imag.mid()));roots[j]=z
        root_error=max(root_error,(abs(phase.real-arb(z.real))+abs(phase.imag-arb(z.imag))).upper())
    mean_weight_error=(mean_weight_error/a.grid).upper()
    mean_weight_size=(mean_weight_size/a.grid).upper()
    # With |p|,|z|<2, each of four binary64 products and two sums has
    # absolute error safely dominated by 2^-46 in complex L1 norm.
    # d_m <= m*(root_error+2^-46)*exp(m*root_error) proves this invariant.
    multiply_error=arb(2)**(-46)
    final_power_error=a.modes*(root_error+multiply_error)*(a.modes*root_error).exp()
    if not final_power_error<arb(1)/4 or not root_error<arb(1)/4:
        raise ValueError('unit-power roundoff induction does not close')
    u=arb(2)**(-53);gamma=(2*a.grid+2)*u/(1-(2*a.grid+2)*u)
    sum_error=(2*gamma*mean_weight_size).upper()
    S=arb(fit['exact_physical_strip'])
    Hp=stored(nominal['nominal_Hprime_complex_modulus']).upper()
    HI=stored(nominal['nominal_H_imaginary_modulus']).upper()
    VP=stored(nominal['nominal_physical_potential_complex_modulus']).upper()
    denominator=1-(-4*S*a.grid).exp()
    alias_max=(2*VP*Hp*(4*a.modes*HI-4*S*a.grid).exp()/denominator).upper()
    if not alias_max<arb('1e-8'):
        raise ValueError('the actual nominal physical alias needs a larger quadrature grid')
    trueV=stored(nominal['true_residual_potential_complex_modulus']).upper()
    inverse_strip=stored(nominal['true_canonical_inverse_strip']).lower()
    nu_comparison=stored(nominal['true_minus_nominal_canonical_potential_uniform_error']).upper()
    report=dict(kind='enclosed_canonical_modes_of_exact_nominal_root_potential',complete=False,
        source_sha256=sha(__file__),bits=a.bits,nominal_path=str(a.nominal),nominal_sha256=sha(a.nominal),
        fit_sha256=nominal['fit_sha256'],identity=nominal['identity'],modes=a.modes,grid=a.grid,
        dependency_sha256={name:sha(Path(__file__).parent/name) for name in
            ('fourfold_phase_root_fourier_fit.py','fourfold_phase_beta_interval.py')},
        exact_nominal_frequency=nominal['nominal_frequency_dyadic'],
        quadrature_identity='nu0_hat_m=average_theta[P_v(theta)*H0prime(theta)*exp(-4im H0(theta))]',
        mean_exact_weight_to_binary64_error=ball_record(mean_weight_error),
        mean_binary64_weight_modulus=ball_record(mean_weight_size),
        maximum_nominal_angle_to_binary64_error=ball_record(angle_error),
        maximum_Arb_unit_root_to_binary64_error=ball_record(root_error),
        per_complex_multiply_absolute_error=ball_record(multiply_error),
        maximum_inducted_unit_power_error=ball_record(final_power_error.upper()),
        arbitrary_order_binary64_sum_error=ball_record(sum_error),
        maximum_complete_physical_quadrature_alias=ball_record(alias_max),
        exact_even_canonical_potential=True,coefficients=[],actual_parameter_family_coefficients_claimed=False)
    save(a.out,report)
    power=np.ones(a.grid,dtype=np.complex128)
    for m in range(a.modes+1):
        value=float(np.sum(weights*power.real,dtype=np.float64)/a.grid)
        power_fee=m*(root_error+multiply_error)*(m*root_error).exp()
        phase_fee=4*m*angle_error
        alias=(2*VP*Hp*(4*m*HI-4*S*a.grid).exp()/denominator).upper()
        fee=(mean_weight_error+mean_weight_size*(power_fee+phase_fee)+sum_error+alias).upper()
        enclosure=arb(value)+arb(0,fee)
        independent_bound=trueV*(-4*inverse_strip*m).exp()+nu_comparison
        enclosure=enclosure.intersection(arb(0,independent_bound.upper()))
        report['coefficients'].append(dict(index=m,midpoint_dyadic=dyadic(arb(value)),
            nominal_coefficient=ball_record(enclosure),
            midpoint_error=ball_record(abs(enclosure-arb(value)).upper())))
        if m<a.modes:power*=roots
        if m and m%256==0:
            report.update(wall_seconds=time.monotonic()-wall,cpu_seconds=time.process_time()-cpu)
            save(a.out,report)
            print(dict(completed_modes=m,requested_modes=a.modes,wall_seconds=report['wall_seconds']),flush=True)
    report.update(complete=True,wall_seconds=time.monotonic()-wall,cpu_seconds=time.process_time()-cpu)
    save(a.out,report)
    print(dict(complete=True,modes=a.modes,wall_seconds=report['wall_seconds'],cpu_seconds=report['cpu_seconds'],
               first_coefficients=report['coefficients'][:4]),flush=True)


if __name__=='__main__':
    main()
