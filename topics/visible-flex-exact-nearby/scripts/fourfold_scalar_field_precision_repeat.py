#!/usr/bin/env python3
"""Three same-time samples per fresh model to separate initialization/warm cost."""
from __future__ import annotations
import json
from pathlib import Path
import statistics
import time
from flint import arb,acb,ctx
from fourfold_phase_unified_scalar_time_circle import UnifiedScalarTimeCircleField
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_interval import ball_record


def main():
    base=Path('data/phase_ring_continuation')
    descriptor=base/'step5_retargeted_reference/descriptor.json'
    domain=base/'step5_sharp_time_domain_full/forward_0014_r.json.gz'
    out=Path('notes/2026-11-12-ordinary14-field-precision-repeat.json')
    report=dict(kind='actual_same_u_scalar_sample_repeated_precision_benchmark',
        complete=False,source_sha256=sha(__file__),descriptor_sha256=sha(descriptor),
        domain_sha256=sha(domain),primitive_nodes=1024,root_nodes=1024,
        angular_nodes=2048,radial_degree=96,normalized_time='i',runs=[],
        limitation='A cost and enclosure comparison at one time, not a whole time-circle proof.')
    baseline=None
    for bits in (192,320):
        ctx.prec,ctx.cap=bits,100
        tic,cpu=time.monotonic(),time.process_time()
        model=UnifiedScalarTimeCircleField(descriptor,domain,nodes=1024,root_nodes=1024,radial_degree=96)
        row=dict(bits=bits,init_wall=time.monotonic()-tic,init_CPU=time.process_time()-cpu,samples=[])
        for trial in range(3):
            tic,cpu=time.monotonic(),time.process_time()
            values,details=model.sample(acb(0,1),2048)
            elapsed,cost=time.monotonic()-tic,time.process_time()-cpu
            overlap=baseline is None or all(a.real.overlaps(b.real) and a.imag.overlaps(b.imag)
                                           for a,b in zip(baseline,values))
            if not overlap:raise ValueError('same true sample enclosures differ')
            if baseline is None:baseline=values
            row['samples'].append(dict(trial=trial,CPU=cost,wall=elapsed,
                maximum_component_radius=details['maximum_component_radius'],
                all_nodes_overlap_first=True))
            print(json.dumps(dict(bits=bits,trial=trial,CPU=cost,
                radius=details['maximum_component_radius']['ball'])),flush=True)
        row['median_sample_CPU']=statistics.median(r['CPU'] for r in row['samples'])
        row['mean_warm_sample_CPU']=statistics.mean(r['CPU'] for r in row['samples'][1:])
        report['runs'].append(row)
        out.write_text(json.dumps(report,indent=2)+'\n')
    report['192_over_320_median_sample_CPU']=report['runs'][0]['median_sample_CPU']/report['runs'][1]['median_sample_CPU']
    report['192_over_320_warm_sample_CPU']=report['runs'][0]['mean_warm_sample_CPU']/report['runs'][1]['mean_warm_sample_CPU']
    report['complete']=True
    out.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':main()
