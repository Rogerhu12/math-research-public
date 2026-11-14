#!/usr/bin/env python3
"""Actual field polynomial from scalar time-circle samples and two true disks.

The R3 domain supplies sharp low-order Fourier moduli; the larger R6 domain
pays time aliases and the complete omitted time tail. The exact finite P is
stored through the same dyadic schema as the independently computed jet P.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time
import numpy as np
from flint import arb,acb,ctx
from fourfold_phase_scalar_time_circle import SharedBudgetScalarField
from fourfold_phase_scalar_time_circle_direct import circle_coefficients,upper_record
from fourfold_phase_actual_field_fourier_package import preserve_polynomial,load_polynomial
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_boundary_fourier_budget import reconstruction_budget,full_fourier_factor


def read_json(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def rational_time(value):
    if isinstance(value,str):return Fraction(value)
    if Fraction(value['pi_coefficient'])!=0:
        raise ValueError('this actual ordinary-time entry expects rational endpoints')
    return Fraction(value['rational'])


def extra_domain(path,model):
    domain=read_json(path)
    if not (domain.get('complete') and domain.get('complete_common_span_coverage')
            and domain.get('proved_full_physical_angle_and_complex_time_domain')):
        raise ValueError('completed actual larger time domain required')
    for key,expected in [('target_object_sha256',sha(model.object_path)),
                         ('target_root_sha256',sha(model.root_path)),
                         ('retarget_descriptor_sha256',sha(model.descriptor_path)),
                         ('exact_delta_fraction',model.domain['exact_delta_fraction'])]:
        if domain[key]!=expected:raise ValueError('larger domain identity differs: '+key)
    if (tuple(map(rational_time,domain['exact_time_endpoints']))!=model.time_endpoints
            or Fraction(domain['physical_theta_strip'])!=Fraction(model.domain['physical_theta_strip'])
            or domain['branch_sign']!=model.sign):
        raise ValueError('larger domain has different coordinates, angle strip, or branch')
    selected=[r for r in domain['germs'] if tuple(map(Fraction,r['common_span']))==model.cell]
    if len(selected)!=1 or not selected[0]['passed']:
        raise ValueError('larger domain does not certify the same entire germ')
    if [tuple(map(Fraction,row)) for row in domain['required_common_spans']] != [model.cell]:
        raise ValueError('this package requires the actual full real interval to be in the selected single germ')
    return exact_arb(Fraction(domain['time_radius'])),upper_record(selected[0]['true_field_moduli']['f']),domain


def combined_budget(nodes,degree,outer_strip,inner_strip,time_inner,errors,
                    domains,time_circle,time_nodes,derivative):
    """All coefficient errors and the complete infinite time-angle complement."""
    m=len(errors);r=exact_arb(time_inner);rho=exact_arb(time_circle)
    R,M=domains[-1]
    if not 0<rho<R or not all(r<rad for rad,_ in domains):
        raise ValueError('invalid actual time disks')
    ratio=(rho/R)**time_nodes;alias_factor=ratio/(1-ratio)
    alias_moduli=[(M/R**i*alias_factor).upper() for i in range(m)]
    coefficient_moduli=[min((mod/rad**i for rad,mod in domains),key=lambda z:float(z)).upper()
                         for i in range(m)]
    # g_i = f_i + the true positive-time alias series.  Both are holomorphic
    # in the same physical-angle strip.  Their exact sum is what the nodes
    # enclose; no time-alias term is folded into independent angular noise.
    summed_modulus=sum((r**i*(coefficient_moduli[i]+alias_moduli[i]) for i in range(m)),arb(0)).upper()
    summed_error=sum((r**i*errors[i] for i in range(m)),arb(0)).upper()
    result=reconstruction_budget(nodes,degree,arb(0),outer_strip,inner_strip,
                                  summed_modulus,summed_error,derivative=derivative)
    result.pop('total')
    factor=full_fourier_factor(outer_strip,inner_strip,derivative)
    result['time_circle_alias']=(factor*sum((r**i*alias_moduli[i] for i in range(m)),arb(0))).upper()
    choices=[mod*factor*(r/rad)**m/(1-r/rad) for rad,mod in domains]
    result['omitted_true_time_tail']=min(choices,key=lambda z:float(z)).upper()
    result['total']=sum(result.values(),arb(0)).upper()
    if not all(v.is_finite() and v>=0 for v in result.values()):
        raise ValueError('nonfinite actual reconstruction bound')
    return result


def finite_difference(first,second,strip):
    first_m,second_m=first.shape[0],second.shape[0]
    first_K,second_K=(first.shape[1]-1)//2,(second.shape[1]-1)//2
    out=[arb(0),arb(0),arb(0)]
    for k in range(-max(first_K,second_K),max(first_K,second_K)+1):
        coefficient_sum=arb(0)
        for i in range(max(first_m,second_m)):
            a=first[i,k+first_K] if i<first_m and abs(k)<=first_K else acb(0)
            b=second[i,k+second_K] if i<second_m and abs(k)<=second_K else acb(0)
            coefficient_sum+=abs(a-b)
        weight=(4*abs(k)*strip).exp()
        for j in range(3):out[j]+=coefficient_sum*weight*(4*abs(k))**j
    return [v.upper() for v in out]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--descriptor',type=Path,default=Path('data/phase_ring_continuation/step5_retargeted_reference/descriptor.json'))
    p.add_argument('--domain',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json'))
    p.add_argument('--larger-domain',type=Path,default=Path('data/phase_ring_continuation/step5_sharp_time_domain_R6_order40/forward_0419_r.json.gz'))
    p.add_argument('--comparison-polynomial',type=Path,default=Path('data/phase_ring_continuation/step5_reference419_main_field_polynomial/manifest.json'))
    p.add_argument('--comparison-certificate',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_main_actual_field_fourier.json'))
    p.add_argument('--angles',type=int,default=4096);p.add_argument('--degree',type=int,default=1800)
    p.add_argument('--primitive-nodes',type=int,default=1024);p.add_argument('--time-nodes',type=int,default=40)
    p.add_argument('--terms',type=int,default=35);p.add_argument('--radius',default='5/4')
    p.add_argument('--inner-strip',default='81/10000');p.add_argument('--bits',type=int,default=320)
    p.add_argument('--polynomial-dir',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits;ctx.cap=max(21,args.terms+3)
    start,cpu=time.monotonic(),time.process_time()
    model=SharedBudgetScalarField(args.descriptor,args.domain,germ=-1,nodes=args.primitive_nodes)
    R6,M6,larger=extra_domain(args.larger_domain,model)
    domains=[(model.outer,model.modulus),(R6,M6)]
    if not R6>model.outer:raise ValueError('second true time disk is not larger')
    inner=exact_arb(Fraction(args.inner_strip))
    if not 0<=inner<model.strip:raise ValueError('inner physical-angle strip leaves actual domain')
    model.precision=args.terms
    a,b=model.time_endpoints
    identity=dict(object_sha256=sha(model.object_path),root_certificate_sha256=sha(model.root_path),
        domain_certificate_sha256=sha(args.domain),larger_domain_certificate_sha256=sha(args.larger_domain),
        exact_delta_fraction=str(model.root_package.exact_delta),exact_time_endpoints=list(map(str,model.time_endpoints)),
        tau_center=str((a+b)/2),time_halfwidth=str((b-a)/2),common_span=list(map(str,model.cell)),branch_sign=model.sign,
        coefficient_origin='exact complex-time DFT g_i; positive time aliases paid by separate complete certificate',
        time_circle_radius=args.radius,time_circle_nodes=args.time_nodes)
    report=dict(kind='actual_scalar_time_circle_finite_field_with_two_true_time_domains',complete=False,
        source_sha256=sha(__file__),identity=identity,bits=args.bits,angular_nodes=args.angles,
        retained_Fourier_degree=args.degree,retained_time_terms=args.terms,primitive_nodes=args.primitive_nodes,
        physical_inner_strip=args.inner_strip,physical_outer_strip=model.domain['physical_theta_strip'],
        actual_time_domains=[dict(radius=ball_record(R),modulus=ball_record(M)) for R,M in domains],
        root_refinement=model.root_package.provenance,init_seconds=time.monotonic()-start,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
          'fourfold_phase_scalar_time_circle.py','fourfold_phase_scalar_time_circle_direct.py',
          'fourfold_phase_actual_field_fourier_package.py','fourfold_native_series_fft.py',
          'fourfold_boundary_fourier_budget.py','fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_interval.py')})
    args.out.parent.mkdir(parents=True,exist_ok=True)
    def save():args.out.write_text(json.dumps(report,indent=2)+'\n')
    save()
    values,timing=circle_coefficients(model,args.angles,args.time_nodes,args.terms,Fraction(args.radius))
    report['scalar_circle_timing']=timing;save()
    manifest,errors,noise=preserve_polynomial(model,values,args.degree,args.polynomial_dir,identity)
    report['polynomial_manifest']=str(manifest);report['polynomial_manifest_sha256']=sha(manifest)
    report['node_and_DFT_error_of_aliased_time_coefficients']=[ball_record(e) for e in errors]
    report['DFT_seconds']=noise['DFT_seconds'];report['DFT_cpu_seconds']=noise['DFT_cpu_seconds'];save()
    budgets={str(j):{key:ball_record(value) for key,value in combined_budget(
       args.angles,args.degree,model.strip,inner,1,errors,domains,Fraction(args.radius),args.time_nodes,j).items()}
       for j in range(3)}
    report['complete_time_angle_derivative_error']=budgets
    new_manifest,new_coefficients=load_polynomial(manifest)
    old_manifest,old_coefficients=load_polynomial(args.comparison_polynomial)
    old_certificate=read_json(args.comparison_certificate)
    if (old_certificate['polynomial_manifest_sha256']!=sha(args.comparison_polynomial)
            or not old_certificate['continuous_field_on_selected_germ_extension_proved']
            or Fraction(old_certificate['physical_inner_strip'])!=Fraction(args.inner_strip)):
        raise ValueError('comparison field certificate/strip mismatch')
    for k in ('object_sha256','root_certificate_sha256','exact_delta_fraction','exact_time_endpoints','common_span','branch_sign'):
        if old_manifest['identity'][k]!=identity[k]:raise ValueError('independent polynomial identity mismatch')
    difference=finite_difference(new_coefficients,old_coefficients,inner)
    for j,value in enumerate(difference):
        allowance=upper_record(budgets[str(j)]['total'])+upper_record(old_certificate['complete_time_Fourier_derivative_error_budgets'][str(j)]['total'])
        if not value<allowance:raise ValueError('two independent finite polynomials violate their proved common-field bounds')
    report['independent_jet_polynomial_comparison']=dict(manifest_sha256=sha(args.comparison_polynomial),
       certificate_sha256=sha(args.comparison_certificate),whole_finite_difference=[ball_record(v) for v in difference],
       all_differences_below_sum_of_actual_error_bounds=True)
    report['complete']=True;report['exact_finite_polynomial_saved']=True
    report['actual_full_time_segment_and_angle_field_proved']=True
    report['elapsed_seconds']=time.monotonic()-start;report['cpu_seconds']=time.process_time()-cpu
    report['limitations']=['Same actual delta5 segment419 and branch only; other intervals and parameters are not inferred.',
                          'No full nonuniform reference composition, true return-map, or nonlinear PDE assertion.']
    save();print(json.dumps(dict(complete=True,cpu_seconds=report['cpu_seconds'],elapsed_seconds=report['elapsed_seconds'],
       bounds={j:b['total']['ball'] for j,b in budgets.items()})),flush=True)


if __name__=='__main__':main()
