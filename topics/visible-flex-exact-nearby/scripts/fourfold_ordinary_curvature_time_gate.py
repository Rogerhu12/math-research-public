#!/usr/bin/env python3
"""Correlated scalar curvature Taylor gate on a larger ordinary time disk.

One true scalar K time jet replaces a rectangular radial sign test. Its
coefficients include the infinite primitive correction before division.
A separate complete a/E denominator gate and true K modulus on the larger
time disk pay every omitted time coefficient. A closed circular cover then
proves Re(-K)>0 by harmonic minimum, retaining time correlations.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
import time

from flint import arb, acb, acb_series, acb_poly, ctx

from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb, complex_pad
from fourfold_phase_beta_interval import (
    array_derivative, vector_dot, series_constant, ball_record,
)
from fourfold_phase_sine_time_geometry import sine_radial_displacement
from fourfold_phase_unified_scalar_time_circle import UnifiedScalarTimeCircleField
from fourfold_forward_density_pipeline import read, save


def ordinary_curvature_disk(model, inner=6, outer=8, *, order=40,
                            boundary_nodes=128):
    """Return complete ordinary K-domain inputs for this exact time/germ.

    No full-angle time grid is computed. Both the finite coefficient balls
    and the larger-disk modulus refer to the identical true infinite K.
    The old scalar sampler's cached point budget is restored on return.
    """
    if model.turn:
        raise ValueError('ordinary curvature gate requires an ordinary germ')
    R, S = map(exact_arb, (inner, outer))
    if not 1 < R < S or order < 4 or boundary_nodes < 8:
        raise ValueError('nested time disks, enough coefficients and cells required')
    tic, cpu = time.monotonic(), time.process_time()
    m = int(order)+1
    oldcap = ctx.cap
    previous = model.target.__dict__.get('analytic_input_budget')
    if previous is not None:
        del model.target.analytic_input_budget
    try:
        ctx.cap = max(21, m+3)
        center = model.root*model.tau0.sin()
        if not center.overlaps(model.center):
            raise ValueError('sampler center is inconsistent with the exact time map')
        budget = model.target.analytic_input_budget(acb(center), model.R0,
                                                    model.sigma, model.RE)
        coefficient, _, _, _, radial_K = model.target.target(center, model.RE, budget)
        del coefficient
        tau = acb_series([acb(model.tau0), acb(model.h)])
        radial = model.root*tau.sin()
        # Exact identity r(0)=center, not a discarded independent root error.
        argument = acb_series([0]+[-radial[j]/model.RE for j in range(1, radial.prec)],
                              prec=radial.prec)
        composed = radial_K(argument)
        # At the real exact center, all true time coefficients are real.
        coefficients = [acb(composed[j].real) for j in range(m)]
        ctx.cap = 4
        enlargement = sine_radial_displacement(model.root, model.tau0, model.h, S)
        outer_radial = complex_pad(acb(center), enlargement)
        finite, Kdisk, _, outer_budget = model.target.complete_data(outer_radial)
        first = array_derivative(finite)
        Efinite = sum((vector_dot(first[k], first[(-k) % model.nodes])
                       for k in range(model.nodes)), series_constant(0))[0]
        Etrue = complex_pad(Efinite, outer_budget['E_error'])
        a = model.target.scalars(outer_radial, 1)[2][0]
        if not (a.abs_lower() > 0 and Etrue.abs_lower() > 0 and Kdisk.is_finite()):
            raise ValueError('larger ordinary K disk has no true holomorphic a/E gate')
        M = abs(Kdisk).upper()
        ratio = R/S
        tail = (M*ratio**m/(1-ratio)).upper()
        # Re(-K) is harmonic; the closed cells cover the full boundary circle.
        # For each center angle phi, use its exact first derivative and a
        # global second derivative norm of the finite boundary polynomial.
        boundary = [-z*R**j for j, z in enumerate(coefficients)]
        polynomial = acb_poly(boundary)
        first_polynomial = acb_poly([acb(0, j)*z for j, z in enumerate(boundary)])
        second_modulus = sum((j*j*abs(z) for j,z in enumerate(boundary)), arb(0)).upper()
        step = arb.pi()/boundary_nodes
        second_fee = (second_modulus*step**2/2).upper()
        minimum = None
        worst = None
        for j in range(boundary_nodes):
            angle = 2*arb.pi()*j/boundary_nodes
            z = acb(angle.cos(), angle.sin())
            value = polynomial(z).real
            slope = first_polynomial(z).real
            endpoint_lower = (value-abs(slope)*step-second_fee-tail).lower()
            if minimum is None or endpoint_lower < minimum:
                minimum, worst = endpoint_lower, j
        Kmodulus = (sum((abs(z) for z in boundary), arb(0))+tail).upper()
        H = abs(model.h)*R
        cosine = (abs(model.tau0.cos())*H.cosh()+abs(model.tau0.sin())*H.sinh()).upper()
        result = dict(kind='ordinary_negative_curvature',
            method='true scalar time jet, full Cauchy complement, closed boundary harmonic minimum',
            passed=bool(minimum > 0), time_radius=str(inner), larger_time_radius=str(outer),
            time_order=int(order), time_coefficients=m, boundary_nodes=int(boundary_nodes),
            minus_K_real_lower=ball_record(minimum), K_modulus=ball_record(Kmodulus),
            K_time_tail=ball_record(tail), K_larger_time_modulus=ball_record(M),
            larger_radial_image_enlargement=ball_record(enlargement),
            a_modulus_lower=ball_record(a.abs_lower()), E_modulus_lower=ball_record(Etrue.abs_lower()),
            true_E_infinite_error=ball_record(outer_budget['E_error']),
            central_time_coefficient_balls=list(map(lambda z: ball_record(z.real), coefficients)),
            boundary_second_derivative_modulus=ball_record(second_modulus),
            boundary_second_order_fee=ball_record(second_fee), worst_boundary_cell=int(worst),
            cosine_modulus=ball_record(cosine),
            exact_time_constant_cancellation='r(u)-r(0), with r(0)=t*sin(tau_center) by definition',
            wall_seconds=time.monotonic()-tic, cpu_seconds=time.process_time()-cpu)
        return Kmodulus, cosine, result
    finally:
        ctx.cap = oldcap
        if previous is not None:
            model.target.analytic_input_budget = previous


def main():
    p=argparse.ArgumentParser(description=__doc__)
    base=Path('data/phase_ring_continuation')
    p.add_argument('--descriptor',type=Path,default=base/'step5_retargeted_reference/descriptor.json')
    p.add_argument('--domain',type=Path,default=base/'step5_sharp_time_domain_full/forward_0004_r.json.gz')
    p.add_argument('--germs',default='all');p.add_argument('--R',type=Fraction,default=Fraction(6))
    p.add_argument('--S',type=Fraction,default=Fraction(8));p.add_argument('--order',type=int,default=40)
    p.add_argument('--boundary-nodes',type=int,default=128);p.add_argument('--nodes',type=int,default=512)
    p.add_argument('--bits',type=int,default=192);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec=a.bits;ctx.cap=4
    domain=read(a.domain);indices=(range(len(domain['germs'])) if a.germs=='all'
                                else list(map(int,a.germs.split(','))))
    result=dict(kind='actual_ordinary_curvature_time_domain_pilot',complete=False,
        source_sha256=sha(__file__),domain_path=str(a.domain),domain_sha256=sha(a.domain),
        descriptor_sha256=sha(a.descriptor),bits=a.bits,nodes=a.nodes,rows=[],
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_unified_scalar_time_circle.py','fourfold_phase_sine_time_geometry.py',
            'fourfold_phase_beta_interval.py','fourfold_phase_beta_bulk_interval.py',
            'fourfold_phase_beta_affine.py')})
    save(a.out,result)
    for index in indices:
        model=UnifiedScalarTimeCircleField(a.descriptor,a.domain,germ=index,nodes=a.nodes,root_nodes=a.nodes)
        try:
            _,_,row=ordinary_curvature_disk(model,a.R,a.S,order=a.order,boundary_nodes=a.boundary_nodes)
        except Exception as exc:
            row=dict(passed=False,failure=type(exc).__name__+': '+str(exc))
        row.update(germ_index=index,common_span=list(map(str,model.cell)),identity=model.identity())
        result['rows'].append(row);save(a.out,result)
        print({key:row.get(key) for key in ('germ_index','passed','minus_K_real_lower','K_time_tail',
            'K_larger_time_modulus','failure','cpu_seconds','wall_seconds')},flush=True)
    result.update(complete=True,proved_all_selected_curvature_disks=all(row['passed'] for row in result['rows']),
        limitations=['Only curvature analyticity and negative-real branch; D/M/W still require their own domain.',
            'No whole returned flow or residual is certified by this scalar gate.'])
    save(a.out,result)


if __name__=='__main__':main()
