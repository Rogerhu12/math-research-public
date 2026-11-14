#!/usr/bin/env python3
"""Extend a true turn field's time domain using saved invariant coefficients.

Reuses ONLY the saved retained DFT coefficient norms, which already enclose
the true primitive/time coefficients. Fourier alias, omitted frequencies and
all infinite time tails are recomputed using NEW whole-angle outer moduli.
There is no new full angular time-jet grid. The original scalar sampler can
continue to use its smaller proved domain at its existing sample points.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, acb, ctx

from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb, complex_pad
from fourfold_phase_beta_interval import ball_record, array_derivative, vector_dot, series_constant
from fourfold_phase_unified_scalar_time_circle import UnifiedScalarTimeCircleField
from fourfold_phase_sine_time_geometry import whole_angle_outer_invariants, sine_radial_displacement
from fourfold_phase_full_angle_time_domain import fourier_fee
from fourfold_forward_density_pipeline import read, save, upper, lower
from fourfold_phase_time_circle_field_package import combined_budget


def true_root_Q_disk(model, radius):
    """Full root-deflated Q, including every omitted radial coefficient."""
    R = exact_arb(radius)
    H = abs(model.eta1)*R
    eta_modulus = abs(model.eta0)+H
    deviation = (eta_modulus.cosh()-1).upper()
    rho = (abs(model.root)*deviation).upper()
    deflation = model.deflation
    ratio = (rho/deflation.RK).upper()
    if not ratio < 1 or not 2-deviation > 0:
        raise ValueError('new inner disk leaves the full root-deflation disk')
    tail = (deflation.K_bound/deflation.RK*ratio**deflation.degree/(1-ratio)).upper()
    variation = (sum((abs(z)*ratio**j for j,z in enumerate(deflation.coefficient) if j),
                     arb(0))+tail).upper()
    J = complex_pad(deflation.coefficient[0], variation)
    Q = model.root*J/(2+complex_pad(acb(0), deviation))
    if not Q.real > 0:
        raise ValueError('new inner disk does not separate the true Q branch')
    sine = (abs(model.eta0.sin())*H.cosh()+abs(model.eta0.cos())*H.sinh()).upper()
    return Q, sine, dict(kind='root_deflated_Q',
        Q_real_lower=ball_record(Q.real.lower()), Q_modulus=ball_record(abs(Q).upper()),
        normalized_radial_modulus=ball_record(ratio),
        full_radial_deflation_tail=ball_record(tail),
        root_curvature_domain=deflation.domain,
        curvature_radial_radius=ball_record(deflation.RK),
        radial_degree=deflation.degree,
        sin_eta_modulus=ball_record(sine))


def true_ordinary_K_disk(model, radius):
    """Full infinite curvature on the new inner radial image, no time truncation."""
    R=exact_arb(radius)
    image=sine_radial_displacement(model.root,model.tau0,model.h,R)
    radial=complex_pad(acb(model.center),image)
    previous=model.target.__dict__.get('analytic_input_budget')
    if previous is not None:del model.target.analytic_input_budget
    oldcap,ctx.cap=ctx.cap,4
    try:
        coefficient,K,_,budget=model.target.complete_data(radial)
        first=array_derivative(coefficient)
        Efinite=sum((vector_dot(first[k],first[(-k)%model.nodes])
                     for k in range(model.nodes)),series_constant(0))[0]
        E=complex_pad(Efinite,budget['E_error'])
        a=model.target.scalars(radial,1)[2][0]
        if not (a.abs_lower()>0 and E.abs_lower()>0 and K.is_finite() and (-K).real>0):
            raise ValueError('new ordinary disk has no negative-curvature holomorphic branch')
        H=abs(model.h)*R
        cosine=(abs(model.tau0.cos())*H.cosh()+abs(model.tau0.sin())*H.sinh()).upper()
        return K,cosine,dict(kind='ordinary_negative_curvature',
            minus_K_real_lower=ball_record((-K).real.lower()),K_modulus=ball_record(abs(K).upper()),
            exact_radial_image_enlargement=ball_record(image),
            a_modulus_lower=ball_record(a.abs_lower()),E_modulus_lower=ball_record(E.abs_lower()),
            true_E_infinite_error=ball_record(budget['E_error']),
            cosine_modulus=ball_record(cosine),
            method='direct full complex radial interval; no omitted time coefficients')
    finally:
        ctx.cap=oldcap
        if previous is not None:model.target.analytic_input_budget=previous


def extension(model, saved, N, K, inner, outer, narrow, wide):
    """All new bounds refer to the identical exact center, scale and germ."""
    R, S = map(exact_arb, (inner, outer))
    if not 1 < R < S or not wide > narrow > 0:
        raise ValueError('strictly nested time and angle domains required')
    tic, cpu = time.monotonic(), time.process_time()
    # The scalar sampler installs a shared budget for its original time disk.
    # It must NOT be reused for an enlarged radial disk.
    shared_budget_override = model.target.__dict__.get('analytic_input_budget')
    if shared_budget_override is not None:
        del model.target.analytic_input_budget
    try:
        coarse, _, _, info = whole_angle_outer_invariants(model, outer, narrow)
        wide_coarse, _, _, wide_info = whole_angle_outer_invariants(model, outer, wide)
    finally:
        if shared_budget_override is not None:
            model.target.analytic_input_budget = shared_budget_override
    alias, fourier_tail = fourier_fee(N, K, 4*exact_arb(wide), 4*exact_arb(narrow))
    alpha = abs(arb(saved['anchor']['u_anchor']['ball'])).upper()
    if not alpha < S:
        raise ValueError('saved genuine anchor leaves the enlarged outer disk')
    base = lower(saved['anchor']['D_anchor_lower'])
    rows = {}
    for name in ('D', 'M', 'W'):
        original = saved['invariant_bounds'][name]
        retained = [upper(v) for v in original['retained_DFT_coefficient_norms']]
        m = len(retained)
        complete = [(v+wide_coarse[name]*(alias+fourier_tail)/S**i).upper()
                    for i,v in enumerate(retained)]
        time_tail = (coarse[name]*(R/S)**m/(1-R/S)).upper()
        modulus = (sum((v*R**i for i,v in enumerate(complete)), arb(0))+time_tail).upper()
        rows[name] = dict(full=complete, modulus=modulus, time_tail=time_tail,
                          retained=retained, coarse=coarse[name], wide_coarse=wide_coarse[name])
    D = rows['D']
    m = len(D['full'])
    anchor_tail = (coarse['D']*(alpha/S)**m/(1-alpha/S)).upper()
    variation = (sum((D['full'][i]*(R**i+alpha**i) for i in range(1,m)), arb(0))
                  +D['time_tail']+anchor_tail).upper()
    Dlower = (base-variation).lower()
    if model.turn:
        Q, factor, curvature = true_root_Q_disk(model, inner)
        wave=(factor*abs(Q).sqrt()).upper()
    else:
        curvature_value,factor,curvature=true_ordinary_K_disk(model,inner)
        wave=abs(curvature_value).sqrt().upper()
    passed = bool(Dlower > 0)
    result = dict(time_radius=str(inner), larger_time_radius=str(outer),
        physical_theta_strip=str(narrow), wider_physical_theta_strip=str(wide),
        passed=passed, reused_time_coefficients=m,
        D_anchor_lower=ball_record(base), u_anchor_modulus=ball_record(alpha),
        D_difference_from_actual_anchor=ball_record(variation), D_lower=ball_record(Dlower),
        curvature=curvature, Fourier_alias_per_unit_modulus=ball_record(alias),
        Fourier_omitted_per_unit_modulus=ball_record(fourier_tail),
        coarse_narrow_domain={k:ball_record(v) for k,v in info.items()},
        coarse_wide_domain={k:ball_record(v) for k,v in wide_info.items()},
        invariant_bounds={name:dict(
            retained_DFT_coefficient_norms=list(map(ball_record,row['retained'])),
            true_time_coefficient_norms=list(map(ball_record,row['full'])),
            whole_strip_time_modulus=ball_record(row['modulus']),
            full_infinite_time_tail=ball_record(row['time_tail']),
            larger_time_narrow_angle_modulus=ball_record(row['coarse']),
            larger_time_wide_angle_modulus=ball_record(row['wide_coarse']))
            for name,row in rows.items()})
    if passed:
        rt = (abs(model.root)*factor).upper()
        M,W=rows['M']['modulus'],rows['W']['modulus']
        field = (rt*(M+wave*W)/Dlower).upper()
        field1=(rt*((coarse['M1']+wave*coarse['W1'])/Dlower
                    +(M+wave*W)*coarse['D1']/Dlower**2)).upper()
        field2=(rt*((coarse['M2']+wave*coarse['W2'])/Dlower
             +(2*(coarse['M1']+wave*coarse['W1'])*coarse['D1']+(M+wave*W)*coarse['D2'])/Dlower**2
             +2*(M+wave*W)*coarse['D1']**2/Dlower**3)).upper()
        result['true_field_moduli'] = dict(f=ball_record(field),f_theta=ball_record(field1),
            f_theta2=ball_record(field2),r_tau=ball_record(rt),wave_factor=ball_record(wave))
    result.update(wall_seconds=time.monotonic()-tic, cpu_seconds=time.process_time()-cpu)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    base = Path('data/phase_ring_continuation')
    parser.add_argument('--descriptor', type=Path, default=base/'step5_retargeted_reference/descriptor.json')
    parser.add_argument('--domain', type=Path,
        default=base/'type_fixed_step02_d5_exact_affine_step5_forward001_turn_domain.json')
    parser.add_argument('--germ', type=int, default=0)
    parser.add_argument('--domains', default='9/2:6,6:8')
    parser.add_argument('--nodes', type=int, default=512)
    parser.add_argument('--bits', type=int, default=192)
    parser.add_argument('--radial-degree', type=int, default=64)
    parser.add_argument('--layout-reference', type=Path,
        default=base/'step5_forward_density_complete/forward_0001_ef134f2a18.json.gz')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    ctx.cap = 4
    start, cpu = time.monotonic(), time.process_time()
    original = read(args.domain)
    model = UnifiedScalarTimeCircleField(args.descriptor, args.domain, germ=args.germ,
        nodes=args.nodes, root_nodes=args.nodes, radial_degree=args.radial_degree)
    if not model.turn:
        raise ValueError('this pilot extends a root-deflated turn field only')
    saved = original['germs'][args.germ]
    if 'invariant_bounds' not in saved:
        raise ValueError('load the original full invariant report, not an inherited summary')
    narrow, wide = map(Fraction,(original['physical_theta_strip'],original['wider_physical_theta_strip']))
    N, K = int(original['angles']), int(original['cutoff'])
    counts = {len(saved['invariant_bounds'][name]['retained_DFT_coefficient_norms'])
              for name in ('D','M','W')}
    if len(counts) != 1:
        raise ValueError('saved invariant time orders differ')
    result = dict(kind='true_turn_time_domain_extension_from_saved_invariant_coefficients',
        complete=False, source_sha256=sha(__file__), original_domain=str(args.domain),
        original_domain_sha256=sha(args.domain), original_germ_index=args.germ,
        descriptor_sha256=sha(args.descriptor), identity=model.identity(),
        saved_retained_norms_already_enclose_true_infinite_time_coefficients=True,
        no_new_full_angle_time_jet_grid=True,
        bits=args.bits, nodes=args.nodes, original_angle_nodes=N, original_cutoff=K,
        extensions=[], dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_unified_scalar_time_circle.py','fourfold_phase_sine_time_geometry.py',
            'fourfold_phase_full_angle_time_domain.py','fourfold_phase_field_time_refined_root.py',
            'fourfold_phase_beta_affine.py','fourfold_phase_time_circle_field_package.py')})
    save(args.out,result)
    for spec in args.domains.split(','):
        inner, outer = map(Fraction,spec.split(':'))
        try:
            row = extension(model,saved,N,K,inner,outer,narrow,wide)
        except Exception as exc:
            row = dict(time_radius=str(inner),larger_time_radius=str(outer),passed=False,
                       failure=type(exc).__name__+': '+str(exc))
        result['extensions'].append(row)
        save(args.out,result)
        print({k:row.get(k) for k in ('time_radius','larger_time_radius','passed','D_lower','failure')},flush=True)
    if args.layout_reference.exists():
        reference = read(args.layout_reference)
        if reference['identity']['field']['target_object_sha256'] != model.identity()['target_object_sha256']:
            raise ValueError('layout reference exact target differs')
        ps = upper(reference['field_compression']['working_strip'])
        target = lower(reference['field_layout']['target_error'])
        oldlayout = reference['field_layout']
        domains = [(model.outer,model.modulus)]+[
            (exact_arb(Fraction(r['time_radius'])),upper(r['true_field_moduli']['f']))
            for r in result['extensions'] if r['passed']]
        proposals = []
        for terms in range(12,oldlayout['time_nodes']+1,2):
            budget = combined_budget(oldlayout['nodes'],oldlayout['degree'],model.strip,ps,1,
                [arb(0)]*terms,domains,Fraction(reference['time_circle_radius']),terms,0)
            if budget['total'] <= target/4:
                proposals.append(dict(time_nodes=terms,terms=terms,
                    angular_nodes=oldlayout['nodes'],Fourier_degree=oldlayout['degree'],
                    analytic_error_before_fresh_node_fees=ball_record(budget['total']),
                    target_quarter=ball_record(target/4)))
                break
        result['layout_comparison'] = dict(reference_sha256=sha(args.layout_reference),
            old_time_nodes=oldlayout['time_nodes'],proposals=proposals,
            actual_resampling_not_performed=True)
    result.update(complete=True,wall_seconds=time.monotonic()-start,cpu_seconds=time.process_time()-cpu,
        limitations=['Only the named exact germ and exact center/scale; no reference flow certified.',
            'Finite true retained coefficient balls reused; every new angular/time complement is paid.',
            'Failed extensions grant no domain; proposed smaller sampling must still pay actual node fees.'])
    save(args.out,result)


if __name__ == '__main__':
    main()
