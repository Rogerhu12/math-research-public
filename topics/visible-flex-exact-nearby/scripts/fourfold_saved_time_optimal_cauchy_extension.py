#!/usr/bin/env python3
"""Optimize a true invariant Taylor cutoff with a fresh larger outer disk.

Saved coefficient balls are never de-noised. For each m, retain only the
first m true coefficient bounds and replace the entire remaining infinite
block by a newly paid Cauchy tail. Each candidate is a complete bound.
The invariant outer disk and the curvature outer disk are independent.
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
from fourfold_phase_full_angle_time_domain import fourier_fee
from fourfold_forward_density_pipeline import read,save,upper,lower
from fourfold_phase_unified_scalar_time_circle import UnifiedScalarTimeCircleField
from fourfold_expand_saved_time_domain import resolve_retained_norms
from fourfold_saved_invariant_time_extension import true_root_Q_disk
from fourfold_ordinary_curvature_time_gate import ordinary_curvature_disk


def extension(model,saved,N,K,inner,outer,narrow,wide,*,curvature_outer=8):
    R,S=map(exact_arb,(inner,outer))
    if not 1<R<S or not wide>narrow>0:
        raise ValueError('strictly nested invariant disks and angular strips required')
    tic,cpu=time.monotonic(),time.process_time()
    previous=model.target.__dict__.get('analytic_input_budget')
    if previous is not None:del model.target.analytic_input_budget
    try:
        coarse,_,_,info=whole_angle_outer_invariants(model,outer,narrow)
        wide_coarse,_,_,wide_info=whole_angle_outer_invariants(model,outer,wide)
    finally:
        if previous is not None:model.target.analytic_input_budget=previous
    alias,angular_tail=fourier_fee(N,K,4*exact_arb(wide),4*exact_arb(narrow))
    alpha=abs(arb(saved['anchor']['u_anchor']['ball'])).upper()
    if not alpha<S:raise ValueError('actual anchor leaves the invariant outer disk')
    base=lower(saved['anchor']['D_anchor_lower'])
    rows={}
    D_candidates=[]
    for name in ('D','M','W'):
        retained=[upper(v) for v in saved['invariant_bounds'][name]['retained_DFT_coefficient_norms']]
        full=[(v+wide_coarse[name]*(alias+angular_tail)/S**j).upper()
              for j,v in enumerate(retained)]
        candidates=[]
        for m in range(1,len(full)+1):
            tail=(coarse[name]*(R/S)**m/(1-R/S)).upper()
            modulus=(sum((v*R**j for j,v in enumerate(full[:m])),arb(0))+tail).upper()
            row=dict(retained_terms=m,whole_strip_time_modulus=ball_record(modulus),
                     entire_omitted_time_block=ball_record(tail))
            candidates.append((modulus,m,tail,row))
            if name=='D':
                anchor_tail=(coarse[name]*(alpha/S)**m/(1-alpha/S)).upper()
                variation=(sum((full[j]*(R**j+alpha**j) for j in range(1,m)),arb(0))
                           +tail+anchor_tail).upper()
                D_candidates.append((variation,m,tail,anchor_tail,dict(
                    retained_terms=m,D_difference_from_actual_anchor=ball_record(variation),
                    inner_entire_omitted_time_block=ball_record(tail),
                    anchor_entire_omitted_time_block=ball_record(anchor_tail))))
        best=min(candidates,key=lambda row:row[0])
        rows[name]=dict(full=full,retained=retained,modulus=best[0],selected_terms=best[1],
            time_tail=best[2],candidates=[row[3] for row in candidates],
            coarse=coarse[name],wide_coarse=wide_coarse[name])
    chosen=min(D_candidates,key=lambda row:row[0])
    variation,m_D=chosen[0],chosen[1]
    Dlower=(base-variation).lower()
    # Cache only on this immutable, already initialized exact model instance.
    cache=getattr(model,'_correlated_curvature_gate_cache',{})
    key=(str(inner),str(curvature_outer),ctx.prec)
    if key not in cache:
        if model.turn:
            Q,factor,curvature=true_root_Q_disk(model,inner)
            wave=(factor*abs(Q).sqrt()).upper()
        else:
            Kmod,factor,curvature=ordinary_curvature_disk(model,inner,curvature_outer)
            if not curvature['passed']:raise ValueError('correlated ordinary curvature gate failed')
            wave=Kmod.sqrt().upper()
        cache[key]=(factor,curvature,wave)
        model._correlated_curvature_gate_cache=cache
    factor,curvature,wave=cache[key]
    passed=bool(Dlower>0)
    result=dict(time_radius=str(inner),larger_time_radius=str(outer),
        curvature_larger_time_radius=str(curvature_outer),physical_theta_strip=str(narrow),
        wider_physical_theta_strip=str(wide),passed=passed,
        D_anchor_lower=ball_record(base),u_anchor_modulus=ball_record(alpha),
        D_difference_from_actual_anchor=ball_record(variation),D_lower=ball_record(Dlower),
        D_selected_retained_terms=m_D,D_cutoff_candidates=[row[4] for row in D_candidates],
        curvature=curvature,
        Fourier_alias_per_unit_modulus=ball_record(alias),
        Fourier_omitted_per_unit_modulus=ball_record(angular_tail),
        coarse_narrow_domain={k:ball_record(v) for k,v in info.items()},
        coarse_wide_domain={k:ball_record(v) for k,v in wide_info.items()},
        invariant_bounds={name:dict(
            retained_DFT_coefficient_norms=list(map(ball_record,row['retained'])),
            true_time_coefficient_norms=list(map(ball_record,row['full'])),
            selected_retained_terms=row['selected_terms'],cutoff_candidates=row['candidates'],
            whole_strip_time_modulus=ball_record(row['modulus']),
            entire_omitted_time_block=ball_record(row['time_tail']),
            larger_time_narrow_angle_modulus=ball_record(row['coarse']),
            larger_time_wide_angle_modulus=ball_record(row['wide_coarse'])) for name,row in rows.items()},
        original_saved_ball_radii_are_not_subtracted=True,
        all_candidate_cutoffs_include_the_full_infinite_complement=True)
    if passed:
        rt=(abs(model.root)*factor).upper()
        M,W=rows['M']['modulus'],rows['W']['modulus']
        field=(rt*(M+wave*W)/Dlower).upper()
        field1=(rt*((coarse['M1']+wave*coarse['W1'])/Dlower
            +(M+wave*W)*coarse['D1']/Dlower**2)).upper()
        field2=(rt*((coarse['M2']+wave*coarse['W2'])/Dlower
            +(2*(coarse['M1']+wave*coarse['W1'])*coarse['D1']+(M+wave*W)*coarse['D2'])/Dlower**2
            +2*(M+wave*W)*coarse['D1']**2/Dlower**3)).upper()
        result['true_field_moduli']=dict(f=ball_record(field),f_theta=ball_record(field1),
            f_theta2=ball_record(field2),r_tau=ball_record(rt),wave_factor=ball_record(wave))
    result.update(wall_seconds=time.monotonic()-tic,cpu_seconds=time.process_time()-cpu)
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    base=Path('data/phase_ring_continuation')
    p.add_argument('--domain',type=Path,default=base/'step5_sharp_time_domain_full/forward_0004_r.json.gz')
    p.add_argument('--descriptor',type=Path,default=base/'step5_retargeted_reference/descriptor.json')
    p.add_argument('--germ',type=int,default=1);p.add_argument('--domains',default='5:8,6:12,6:16')
    p.add_argument('--curvature-outer',type=Fraction,default=Fraction(8))
    p.add_argument('--nodes',type=int,default=512);p.add_argument('--bits',type=int,default=192)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args();ctx.prec=a.bits;ctx.cap=4
    original=read(a.domain)
    saved,provenance=resolve_retained_norms(a.domain,original,a.germ)
    model=UnifiedScalarTimeCircleField(a.descriptor,a.domain,germ=a.germ,nodes=a.nodes,root_nodes=a.nodes)
    narrow,wide=map(Fraction,(original['physical_theta_strip'],original['wider_physical_theta_strip']))
    result=dict(kind='actual_invariant_optimal_cutoff_time_domain_extensions',complete=False,
        source_sha256=sha(__file__),domain_path=str(a.domain),domain_sha256=sha(a.domain),
        descriptor_sha256=sha(a.descriptor),germ_index=a.germ,identity=model.identity(),
        retained_coefficient_provenance=provenance,bits=a.bits,nodes=a.nodes,extensions=[],
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_ordinary_curvature_time_gate.py','fourfold_saved_invariant_time_extension.py',
            'fourfold_expand_saved_time_domain.py','fourfold_phase_sine_time_geometry.py',
            'fourfold_phase_full_angle_time_domain.py','fourfold_phase_unified_scalar_time_circle.py')})
    save(a.out,result)
    for text in a.domains.split(','):
        R,S=map(Fraction,text.split(':'))
        try:
            row=extension(model,saved,provenance['angle_nodes'],provenance['cutoff'],R,S,narrow,wide,
                          curvature_outer=a.curvature_outer)
        except Exception as exc:
            row=dict(time_radius=str(R),larger_time_radius=str(S),passed=False,
                     failure=type(exc).__name__+': '+str(exc))
        result['extensions'].append(row);save(a.out,result)
        print({key:row.get(key) for key in ('time_radius','larger_time_radius','passed','D_lower',
            'D_selected_retained_terms','true_field_moduli','failure','cpu_seconds','wall_seconds')},flush=True)
    result.update(complete=True,
        limitations=['Only the selected actual germ is tested; no complete real-time germ cover is asserted.',
            'The true invariant and curvature outer disks have separate proofs.',
            'Every cutoff retains old true coefficient balls and pays the whole remaining infinite block.'])
    save(a.out,result)


if __name__=='__main__':main()
