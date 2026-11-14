#!/usr/bin/env python3
"""Saved true invariant time norms plus a correlated scalar curvature gate.

The coefficient reuse and all angular/time complements are the frozen
extension formulas. Ordinary K uses a separately paid whole-circle time
Taylor gate; no broad radial box is required to have negative curvature.
The old extension module and scalar samplers remain unchanged.
"""
from __future__ import annotations
import time
from flint import arb
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_sine_time_geometry import whole_angle_outer_invariants
from fourfold_phase_full_angle_time_domain import fourier_fee
from fourfold_forward_density_pipeline import upper, lower
from fourfold_saved_invariant_time_extension import true_root_Q_disk
from fourfold_ordinary_curvature_time_gate import ordinary_curvature_disk


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
        curvature_modulus,factor,curvature=ordinary_curvature_disk(model,inner,outer)
        if not curvature['passed']:
            raise ValueError('correlated ordinary K boundary gate did not pass')
        wave=curvature_modulus.sqrt().upper()
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

