#!/usr/bin/env python3
"""Actual Q384/Q512 parameter-source comparison at one full complex-time grid.

This diagnostic does not certify a complete time circle or a smaller-Q leaf.
Every returned node is an actual infinite-source enclosure from the existing
sampler. Subsequent complete leaves still pay their own full joint RMS gate.
"""
import argparse
from fractions import Fraction
from pathlib import Path
import time
from flint import arb,acb,ctx
from fourfold_phase_parameter_time_circle import ParameterTimeCircleField
from fourfold_phase_uniform_parameter_time_circle import UniformParameterTimeCircleField
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_affine import sha
from fourfold_forward_density_pipeline_Q1024_v3 import save


def main():
    p=argparse.ArgumentParser(description=__doc__);base=Path('data/phase_ring_continuation')
    p.add_argument('--descriptor',type=Path,default=base/'step5_retargeted_reference/descriptor.json')
    p.add_argument('--domain',type=Path,default=base/'step5_sharp_time_domain_R6_order40/forward_0419_r.json.gz')
    p.add_argument('--local-root-jets',type=Path,default=base/'type_fixed_step02_d5_step5_local_parameter_root_jets_h1e14.json')
    p.add_argument('--wide-root-jets',type=Path,default=base/'type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json')
    p.add_argument('--half-width',type=Fraction,default=Fraction(0))
    p.add_argument('--nodes',type=int,default=2048);p.add_argument('--bits',type=int,default=256)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args();ctx.prec=args.bits;ctx.cap=7
    report=dict(kind='actual_parameter_primitive_one_complex_time_node_diagnostic',complete=False,
        source_sha256=sha(__file__),descriptor_sha256=sha(args.descriptor),domain_sha256=sha(args.domain),
        exact_real_parameter_half_width=str(args.half_width),actual_time_u=['0','1'],angles=args.nodes,
        complete_time_circle_proved=False,models=[])
    samples=[]
    for Q in (512,384):
        tic,cpu=time.monotonic(),time.process_time()
        options=dict(nodes=Q,root_nodes=1024,outer=Fraction(3))
        if args.half_width:
            model=UniformParameterTimeCircleField(args.descriptor,args.domain,args.local_root_jets,
                args.wide_root_jets,half_width=args.half_width,**options)
        else:model=ParameterTimeCircleField(args.descriptor,args.domain,args.local_root_jets,**options)
        init_cpu=time.process_time()-cpu
        values,timing=model.sample(acb(0,1),args.nodes)
        if any(not z.is_finite()for z in values.flat):raise ValueError('nonfinite actual parameter node')
        rows=[]
        for j in (1,2):
            errors=[abs(z-acb(z.real.mid(),z.imag.mid())).upper()for z in values[:,j]]
            rms=(sum((v*v for v in errors),arb(0))/args.nodes).sqrt().upper()
            rows.append(dict(parameter_order=j,normalized_angular_RMS_error=ball_record(rms),
                largest_node_ball_error=ball_record(max(v.upper()for v in errors)),
                maximum_true_node_modulus=ball_record(max(abs(z).upper()for z in values[:,j]))))
        report['models'].append(dict(primitive_nodes=Q,root_primitive_nodes=1024,
            identity=model.identity(),parameter_nodes=rows,init_cpu_seconds=init_cpu,
            total_cpu_seconds=time.process_time()-cpu,total_wall_seconds=time.monotonic()-tic,
            sampler_timing=timing))
        samples.append(values);save(args.out,report)
        print(dict(Q=Q,parameter_RMS=[row['normalized_angular_RMS_error']['upper']for row in rows],
            cpu=report['models'][-1]['total_cpu_seconds']),flush=True)
    report['same_actual_node_enclosures_overlap']=[all(
        a.real.overlaps(b.real)and a.imag.overlaps(b.imag)
        for a,b in zip(samples[0][:,j],samples[1][:,j]))for j in (1,2)]
    if not all(report['same_actual_node_enclosures_overlap']):
        raise ValueError('different-Q enclosures of the same true parameter source do not overlap')
    report.update(complete=True,limitations=[
        'One exact complex-time node and the stated full real-angle grid only.',
        'This RMS is not a whole-time-circle RMS and cannot replace future sampled-node fees.',
        'No new complete density, twist, or global parameter budget is asserted.'])
    save(args.out,report);print(dict(complete=True,sha256=sha(args.out)),flush=True)


if __name__=='__main__':main()

