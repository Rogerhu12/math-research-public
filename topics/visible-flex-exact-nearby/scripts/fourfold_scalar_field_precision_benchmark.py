#!/usr/bin/env python3
"""Actual same-germ scalar-field precision comparison at one complex time.

This records true node enclosures and CPU time.  It does not transfer one
sample's rounding bound to the remaining time-circle nodes.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
import time

from flint import arb,acb,ctx
from fourfold_phase_unified_scalar_time_circle import UnifiedScalarTimeCircleField
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_saved_circle_field_multidomain_budget import read,upper


def main():
    p=argparse.ArgumentParser(description=__doc__)
    base=Path('data/phase_ring_continuation')
    p.add_argument('--descriptor',type=Path,default=base/'step5_retargeted_reference/descriptor.json')
    p.add_argument('--domain',type=Path,default=base/'step5_sharp_time_domain_full/forward_0014_r.json.gz')
    p.add_argument('--layout-report',type=Path,default=base/'step5_forward_density_complete/forward_0014_ef134f2a18.json.gz')
    p.add_argument('--precisions',default='320,192')
    p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--primitive-nodes',type=int,default=1024)
    p.add_argument('--root-nodes',type=int,default=1024)
    p.add_argument('--radial-degree',type=int,default=96)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    saved=read(args.layout_report)
    if saved['domain_sha256']!=sha(args.domain):
        raise ValueError('saved layout and benchmark domain differ')
    layout=saved['field_layout']
    if layout['nodes']!=args.angles:
        raise ValueError('requested angle grid differs from the actual layout')
    physical=Fraction(saved['real_reference_gate']['physical_approximation_strip'])
    K,m=layout['degree'],layout['terms']
    rho=Fraction(saved['time_circle_radius'])
    report=dict(kind='actual_same_germ_scalar_field_precision_benchmark',complete=False,
        source_sha256=sha(__file__),descriptor_sha256=sha(args.descriptor),
        domain_path=str(args.domain),domain_sha256=sha(args.domain),
        layout_report_path=str(args.layout_report),layout_report_snapshot_sha256=sha(args.layout_report),
        normalized_time='i',angles=args.angles,primitive_nodes=args.primitive_nodes,
        root_nodes=args.root_nodes,radial_degree=args.radial_degree,
        field_target_error=layout['target_error'],physical_working_strip=str(physical),
        sampled_layout=dict(nodes=args.angles,degree=K,time_terms=m,time_circle_radius=str(rho)),
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_unified_scalar_time_circle.py','fourfold_phase_field_time_refined_root.py',
            'fourfold_phase_beta_affine.py','fourfold_phase_beta_interval.py',
            'fourfold_native_series_fft.py','fourfold_phase_uniform_field_time_grid_fast.py')},
        runs=[],limitations=['Only the actual u=i node vector is computed here.',
          'The displayed full-rectangle noise estimate assumes every time sample has this same maximum error; it is not a full time-circle certificate.',
          'Every future complete leaf must still check its own true node/DFT/selection/analytic errors.'])
    previous=None
    for bits in map(int,args.precisions.split(',')):
        ctx.prec,ctx.cap=bits,max(21,args.radial_degree+4)
        start,cpu=time.monotonic(),time.process_time()
        model=UnifiedScalarTimeCircleField(args.descriptor,args.domain,germ=-1,
            nodes=args.primitive_nodes,root_nodes=args.root_nodes,radial_degree=args.radial_degree)
        init_wall,init_cpu=time.monotonic()-start,time.process_time()-cpu
        identity=model.identity()
        start,cpu=time.monotonic(),time.process_time()
        values,timing=model.sample(acb(0,1),args.angles)
        sample_wall,sample_cpu=time.monotonic()-start,time.process_time()-cpu
        eps=max(((v.real.rad()**2+v.imag.rad()**2).sqrt().upper() for v in values),key=lambda z:z)
        mean=sum(((v.real.rad()**2+v.imag.rad()**2).sqrt() for v in values),arb(0))/args.angles
        time_weight=sum((exact_arb(rho)**(-i) for i in range(m)),arb(0))
        angle_weight=1+2*sum(((4*k*exact_arb(physical)).exp() for k in range(1,K+1)),arb(0))
        conditional_noise=(eps*time_weight*angle_weight).upper()
        overlap=None
        if previous is not None:
            overlap=all(a.real.overlaps(b.real) and a.imag.overlaps(b.imag)
                        for a,b in zip(previous,values))
            if not overlap:raise ValueError('same actual sample enclosures do not overlap')
        previous=values
        row=dict(bits=bits,identity=identity,initialization_cpu_seconds=init_cpu,
            initialization_wall_seconds=init_wall,sample_cpu_seconds=sample_cpu,
            sample_wall_seconds=sample_wall,sample_details=timing,
            maximum_complex_node_radius=ball_record(eps),mean_complex_node_radius=ball_record(mean.upper()),
            all_actual_enclosures_finite=all(v.is_finite() for v in values),
            all_2048_nodes_overlap_previous_precision=overlap,
            conditional_entire_rectangle_node_noise=ball_record(conditional_noise),
            conditional_noise_to_actual_field_target=ball_record(conditional_noise/upper(layout['target_error'])))
        report['runs'].append(row)
        args.out.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(dict(bits=bits,init_cpu=init_cpu,sample_cpu=sample_cpu,
            max_radius=timing['maximum_component_radius']['ball'],
            conditional_noise=ball_record(conditional_noise),overlap=overlap)),flush=True)
    if len(report['runs'])==2:
        report['second_over_first_sample_CPU_ratio']=report['runs'][1]['sample_cpu_seconds']/report['runs'][0]['sample_cpu_seconds']
        report['second_over_first_initialization_CPU_ratio']=report['runs'][1]['initialization_cpu_seconds']/report['runs'][0]['initialization_cpu_seconds']
    report['complete']=True
    args.out.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':main()
