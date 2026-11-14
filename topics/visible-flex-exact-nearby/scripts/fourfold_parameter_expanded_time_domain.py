#!/usr/bin/env python3
"""Actual parameter source bounds on a separately proved larger true disk.

The selected germ's central D/curvature bounds come from the completed R6
true-domain certificate.  All parameter geometry and primitive budgets are
recomputed on the enlarged radial disk.  Uniform real-p losses are then paid
by the existing exact mean-value formulas.  These are analytic complement
bounds only; an ordinary sampler may retain its original R3 error budget.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction
from pathlib import Path
import time
import traceback
from flint import arb,acb,ctx

from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_parameter_time_circle import ParameterTimeCircleField,ParameterRootDeflation
from fourfold_phase_uniform_parameter_time_circle import UniformParameterTimeCircleField
from fourfold_forward_density_pipeline_spatial_v7 import checked_extended_domain
from fourfold_saved_circle_field_multidomain_budget import read
from fourfold_forward_density_pipeline_Q1024_v3 import save


def expanded_central(source,domain_path,expanded_path,germ_index,radial_degree):
    """Reuse definitions, then prove the new disk; do not retitle an old bound."""
    doc,row=checked_extended_domain(expanded_path,domain_path,germ_index)
    if (source.base.domain['segment']!=doc['segment'] or source.base.cell!=
        tuple(map(Fraction,row['common_span']))):
        raise ValueError('the parameter source selected a different actual germ')
    result=copy.copy(source)
    result.base=copy.copy(source.base)
    result.target=copy.copy(source.target)
    result.base.selected=copy.deepcopy(row)
    result.outer=exact_arb(Fraction(doc['time_radius']))
    result.base.outer=result.outer
    if not result.outer>source.outer:
        raise ValueError('the new actual time disk is not larger')
    H=abs(result.h)*result.outer
    result.center=result.root*result.tau0.sin()
    result.radial_enlargement=(abs(result.root)*(abs(result.tau0.sin())*(H.cosh()-1)
                                               +abs(result.tau0.cos())*H.sinh())).upper()
    common=result.target.parameter_input_budget2(acb(result.center),
        result.R0+result.radial_enlargement,result.sigma,result.RE+result.radial_enlargement)
    result.common_budgets=[]
    for item in common:
        budget=dict(item);budget['radial_radius'],budget['E_radius']=result.R0,result.RE
        result.common_budgets.append(budget)
    result.deflation=ParameterRootDeflation(result,radial_degree) if result.turn else None
    result.moduli=result.complete_source_moduli()
    return result


def prove(descriptor,domain_path,expanded_path,output,*,local_root_jets,wide_root_jets,
          half_width=Fraction(1,10**9),nodes=1024,root_nodes=1024,germ_index=0,
          radial_degree=40,bits=320,central=None):
    ctx.prec,ctx.cap=bits,7;tick,cpu=time.monotonic(),time.process_time()
    result=dict(kind='actual_expanded_time_parameter_source_bounds',complete=False,
        source_sha256=sha(__file__),domain_path=str(domain_path),domain_sha256=sha(domain_path),
        expanded_true_domain_path=str(expanded_path),expanded_true_domain_sha256=sha(expanded_path),
        selected_germ_index=germ_index,nodes=nodes,root_nodes=root_nodes,bits=bits,
        exact_parameter_half_width=str(half_width),point_sampler_domain_unchanged=True,
        original_continuous_crossing_caps_still_required=True,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_parameter_time_circle.py','fourfold_phase_parameter_time_circle_ordinary_v1.py',
            'fourfold_phase_uniform_parameter_time_circle.py','fourfold_forward_density_pipeline_spatial_v7.py',
            'fourfold_phase_fixed_tau_parameter_bounds.py','fourfold_phase_unified_scalar_time_circle.py',
            'fourfold_native_series_fft.py')})
    try:
        central=central or ParameterTimeCircleField(descriptor,domain_path,local_root_jets,
            nodes=nodes,root_nodes=root_nodes,germ=germ_index,radial_degree=radial_degree)
        result['original_central_identity']=central.identity()
        larger=expanded_central(central,domain_path,expanded_path,germ_index,radial_degree)
        result.update(time_radius=str(larger.outer),physical_theta_strip=str(larger.strip),
            center_source_moduli=larger.moduli,center_parameter_identity=larger.identity(),
            complete_center_source_proved=True)
        if half_width:
            uniform=UniformParameterTimeCircleField(descriptor,domain_path,local_root_jets,wide_root_jets,
                half_width=half_width,nodes=nodes,root_nodes=root_nodes,outer=Fraction(result['time_radius']),
                germ=germ_index,radial_degree=radial_degree,central=larger)
            result.update(uniform_source_moduli=uniform.moduli,uniform_parameter_identity=uniform.identity(),
                          complete_uniform_real_parameter_source_proved=True)
        result['complete']=True
    except Exception as exc:
        result.update(failure=type(exc).__name__+': '+str(exc),traceback=traceback.format_exc())
    result.update(wall_seconds=time.monotonic()-tick,cpu_seconds=time.process_time()-cpu)
    save(output,result);return result


def main():
    p=argparse.ArgumentParser(description=__doc__);base=Path('data/phase_ring_continuation')
    p.add_argument('--descriptor',type=Path,default=base/'step5_retargeted_reference/descriptor.json')
    p.add_argument('--domain',type=Path,required=True)
    p.add_argument('--expanded-domain',type=Path,required=True)
    p.add_argument('--local-root-jets',type=Path,default=base/'type_fixed_step02_d5_step5_local_parameter_root_jets_h1e14.json')
    p.add_argument('--wide-root-jets',type=Path,default=base/'type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json')
    p.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    p.add_argument('--nodes',type=int,default=1024);p.add_argument('--root-nodes',type=int,default=1024)
    p.add_argument('--germ',type=int,default=0);p.add_argument('--radial-degree',type=int,default=40)
    p.add_argument('--bits',type=int,default=320);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    result=prove(args.descriptor,args.domain,args.expanded_domain,args.out,
        local_root_jets=args.local_root_jets,wide_root_jets=args.wide_root_jets,
        half_width=args.half_width,nodes=args.nodes,root_nodes=args.root_nodes,
        germ_index=args.germ,radial_degree=args.radial_degree,bits=args.bits)
    print({k:result.get(k) for k in ('complete','complete_center_source_proved',
        'complete_uniform_real_parameter_source_proved','failure','wall_seconds','cpu_seconds')},flush=True)
    return 0 if result['complete'] else 2

if __name__=='__main__':raise SystemExit(main())
