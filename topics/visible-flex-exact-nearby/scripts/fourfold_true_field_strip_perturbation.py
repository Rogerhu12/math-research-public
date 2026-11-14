#!/usr/bin/env python3
"""Pay a wider physical-angle field strip by an actual D_theta bound.

No saved narrow-strip Fourier coefficient norm is transferred to the wider
strip. A fresh true whole-angle/complex-time majorant supplies D_theta,M,W.
The already proved narrow-strip lower bound on |D| then pays the vertical
angle displacement. Curvature is independent of theta and retains its own
previous true time-domain certificate.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb,ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_sine_time_geometry import whole_angle_outer_invariants
from fourfold_phase_unified_scalar_time_circle import UnifiedScalarTimeCircleField
from fourfold_forward_density_pipeline import read,save,upper,lower


def widen(model,width):
    width=Fraction(width)
    old=Fraction(model.domain['physical_theta_strip'])
    if not width>old:raise ValueError('new physical-angle strip must be wider')
    tic,cpu=time.monotonic(),time.process_time()
    previous=model.target.__dict__.get('analytic_input_budget')
    if previous is not None:del model.target.analytic_input_budget
    try:
        bounds,_,_,info=whole_angle_outer_invariants(model,Fraction(model.domain['time_radius']),width)
    finally:
        if previous is not None:model.target.analytic_input_budget=previous
    base=lower(model.selected['D_lower'])
    derivative=bounds['D1']
    displacement=(exact_arb(width-old)*derivative).upper()
    Dlower=(base-displacement).lower()
    H=abs(model.h)*model.outer
    curvature=model.selected['curvature']
    if model.turn:
        factor=(abs(model.eta0.sin())*H.cosh()+abs(model.eta0.cos())*H.sinh()).upper()
        wave=(factor*upper(curvature['Q_modulus']).sqrt()).upper()
    else:
        factor=(abs(model.tau0.cos())*H.cosh()+abs(model.tau0.sin())*H.sinh()).upper()
        wave=upper(curvature['K_modulus']).sqrt().upper()
    rt=(abs(model.root)*factor).upper()
    result=dict(physical_theta_strip=str(width),old_physical_theta_strip=str(old),
        time_radius=model.domain['time_radius'],passed=bool(Dlower>0),
        old_D_lower=ball_record(base),new_whole_strip_D_theta_modulus=ball_record(derivative),
        full_vertical_angle_perturbation=ball_record(displacement),D_lower=ball_record(Dlower),
        new_invariant_moduli={key:ball_record(value) for key,value in bounds.items()},
        new_whole_angle_domain={key:ball_record(value) for key,value in info.items()},
        curvature_certificate_independent_of_theta=curvature,
        cosine_or_sine_modulus=ball_record(factor),
        no_narrow_strip_coefficient_norms_reused_as_wide_strip_norms=True)
    if Dlower>0:
        M,W=bounds['M'],bounds['W']
        field=(rt*(M+wave*W)/Dlower).upper()
        result['true_field_moduli']=dict(f=ball_record(field),r_tau=ball_record(rt),wave_factor=ball_record(wave))
    result.update(wall_seconds=time.monotonic()-tic,cpu_seconds=time.process_time()-cpu)
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    base=Path('data/phase_ring_continuation')
    p.add_argument('--descriptor',type=Path,default=base/'step5_retargeted_reference/descriptor.json')
    p.add_argument('--domain',type=Path,required=True);p.add_argument('--germ',type=int,default=-1)
    p.add_argument('--widths',default='3/128,1/32');p.add_argument('--nodes',type=int,default=512)
    p.add_argument('--bits',type=int,default=192);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec=a.bits;ctx.cap=4
    model=UnifiedScalarTimeCircleField(a.descriptor,a.domain,germ=a.germ,nodes=a.nodes,root_nodes=a.nodes)
    result=dict(kind='actual_true_field_wider_angle_strip_perturbation',complete=False,
        source_sha256=sha(__file__),domain_path=str(a.domain),domain_sha256=sha(a.domain),
        descriptor_sha256=sha(a.descriptor),germ_index=a.germ,identity=model.identity(),extensions=[],
        bits=a.bits,nodes=a.nodes,dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_sine_time_geometry.py','fourfold_phase_unified_scalar_time_circle.py',
            'fourfold_phase_beta_interval.py','fourfold_phase_beta_bulk_interval.py')})
    save(a.out,result)
    for spec in a.widths.split(','):
        try:row=widen(model,Fraction(spec))
        except Exception as exc:row=dict(physical_theta_strip=spec,passed=False,failure=type(exc).__name__+': '+str(exc))
        result['extensions'].append(row);save(a.out,result)
        print({key:row.get(key) for key in ('physical_theta_strip','passed','new_whole_strip_D_theta_modulus',
            'D_lower','failure','cpu_seconds','wall_seconds')},flush=True)
    result.update(complete=True,limitations=['A failed sufficient perturbation gate does not prove an actual zero.',
        'Each result is for this exact germ, complex-time disk and target only; no flow residual is claimed.'])
    save(a.out,result)


if __name__=='__main__':main()
