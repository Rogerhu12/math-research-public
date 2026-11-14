#!/usr/bin/env python3
"""Minimize finite curvature from all five or six current-baseline controls.

Consumes only complete actual-J full-mean fields from one accepted baseline.
The optional sixth direction is core-held start_acceleration from that exact
baseline's actual full-J. A new accepted point requires new fields for every
control; no old-baseline geometry slope is imported. All original finite rows
are rechecked. Predictions remain floating design data, not certificates.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import resource
import tempfile

for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'

import numpy as np
from root_geometry_array_io import read_chunks,sha
from root_geometry_streaming_lp_resident import release_pages
from root_saved_geometry_minimax import whole_field_summary
from root_geometry_minimax_from_plan import load_field
from root_geometry_minimax_variable_controls import solve_minimax


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--plan',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--q1-factors',type=float,nargs='+',default=[.5,1.,2.])
    ap.add_argument('--size-factors',type=float,nargs='+',default=[.999,1.,1.001,1.002])
    ap.add_argument('--trust-factor',type=float,default=1.)
    ap.add_argument('--rss-limit-mib',type=float,default=192.)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Use a fresh result path')
    if any(not np.isfinite(v) or v<=0 for v in args.q1_factors+args.size_factors+[args.trust_factor]):
        raise ValueError('Finite positive trust, growth, and size factors required')
    plan=json.loads(args.plan.read_text())
    if plan['baseline_only'] or len(plan['candidates'])!=1+2*len(plan['directions']):
        raise ValueError('Every current control requires its complete positive and negative field')
    if Path.cwd()!=Path(plan['cwd']):
        raise ValueError('Run in the original plan cwd to retain all input path identities')
    for path,wanted in plan['source_and_input_sha256'].items():
        if sha(path)!=wanted:raise ValueError('A prepared source/input changed: '+path)
    rows={row['name']:row for row in plan['candidates']}
    directions=plan['directions']
    original_names=['actual_q1','actual_q4','actual_c6','vu','descending_turn_curvature']
    names=[r['name'] for r in directions]
    if names not in (original_names,original_names+['start_acceleration']):
        raise ValueError('Require all five original controls and optionally current core-held start_acceleration in order')
    controls=len(directions)
    if set(rows)!={'baseline',*[name+sign for name in names for sign in ('-plus','-minus')]}:
        raise ValueError('Current complete field names differ from the recorded directions')
    candidate=rows['actual_q1-plus']['command']
    response_path=Path(candidate[candidate.index('--response-data')+1])
    response=json.loads(response_path.read_text())
    response_rows={r['direction']:r for r in response['prescribed_low_core_responses']}
    response_rows.update({r['external_field']:r for r in response['additional_core_held_directions']})
    if not response['finished'] or response['new_solution'] or response['modes']!=plan['modes']:
        raise ValueError('Missing complete current actual response')
    shape=tuple(json.loads(Path(rows['baseline']['field']).read_text())['shape'])
    inputs=[]
    for row in rows.values():
        for key in ('report','resource','field'):
            inputs.append(dict(path=row[key],sha256=sha(row[key])))
        for chunk in json.loads(Path(row['field']).read_text())['chunks']:
            inputs.append(dict(path=str(Path(row['field']).with_name(chunk['file'])),sha256=chunk['sha256']))
    predictions,derivatives,second_differences=[],[],[]
    with tempfile.TemporaryDirectory(prefix='vfla-current-minimax-') as work:
        work=Path(work)
        base=np.memmap(work/'base',dtype='float64',mode='w+',shape=shape)
        plus=np.memmap(work/'plus',dtype='float64',mode='w+',shape=shape)
        minus=np.memmap(work/'minus',dtype='float64',mode='w+',shape=shape)
        slopes=np.memmap(work/'slopes',dtype='float64',mode='w+',shape=(*shape,controls))
        base_field=load_field(rows['baseline'],plan,base)
        baseline=whole_field_summary(base_field,base)
        baseline.update(height_abs_max_sample=base_field['height_abs_max_sample'],
                        horizontal_radius_max_sample=base_field['horizontal_radius_max_sample'])
        for column,direction in enumerate(directions):
            name=direction['name']
            fp=load_field(rows[name+'-plus'],plan,plus);release_pages(plus)
            fm=load_field(rows[name+'-minus'],plan,minus);release_pages(minus)
            sp,sm=whole_field_summary(fp,plus),whole_field_summary(fm,minus)
            for field,summary in [(fp,sp),(fm,sm)]:
                summary.update(height_abs_max_sample=field['height_abs_max_sample'],
                               horizontal_radius_max_sample=field['horizontal_radius_max_sample'])
            second=np.zeros(3)
            for first in range(0,shape[0],32):
                sl=slice(first,min(first+32,shape[0]))
                slopes[sl,:,:,column]=(plus[sl]-minus[sl])/2
                second=np.maximum(second,abs(plus[sl]+minus[sl]-2*base[sl]).max(axis=(0,1)))
                release_pages(base,plus,minus,slopes)
            derivatives.append(dict(direction=name,step=direction['step'],plus=sp,minus=sm,
                scalar_max_central_differences={k:(sp[k]-sm[k])/2 for k in
                  ('max_abs_curvature','max_twice_norm','product','complete_core_axis_phase_gap',
                   'height_abs_max_sample','horizontal_radius_max_sample')},
                derivatives_are_finite_model_differences=True))
            second_differences.append(dict(direction=name,observed_second_difference=second.tolist(),
                                           certified_nonlinear_remainder=False))
        for qstep in args.q1_factors:
            for factor in args.size_factors:
                cap=baseline['max_twice_norm']*factor
                result=solve_minimax(base,slopes,cap,qstep,trust=args.trust_factor)
                result.update(fixed_q1_factor=qstep,size_factor=factor,size_cap=cap,
                              other_control_trust_factor=args.trust_factor,
                              all_geometry_slopes_from_this_new_baseline=True,
                              stale_q095_or_other_baseline_slopes_used=False)
                if result['success']:
                    physical={d['name']:d['step']*v for d,v in zip(directions,result['normalized_steps'])}
                    inc_profile,inc_core={},np.zeros(plan['modes'])
                    for name,weight in physical.items():
                        row=response_rows[name]
                        inc_core+=weight*np.asarray(row['core_derivative'])
                        for key,value in row['physical_profile_derivative'].items():
                            inc_profile[key]=inc_profile.get(key,0.)+weight*value
                    gap=baseline['complete_core_axis_phase_gap']+2*float(inc_core[::2].sum())
                    result.update(physical_steps=physical,predicted_profile_increment=inc_profile,
                        predicted_complete_core_increment=inc_core.tolist(),predicted_complete_axis_gap=gap,
                        predicted_axis_gap_over_twice_norm=gap/result['predicted_max_twice_norm'],
                        predicted_relative_kappa_size_change=result['predicted_kappa_times_twice_norm']/baseline['product']-1,
                        candidate_is_new_nonlinear_solution=False)
                predictions.append(result)
                print(json.dumps({key:result.get(key) for key in ('fixed_q1_factor','size_factor','success',
                    'normalized_steps','predicted_max_abs_curvature','predicted_kappa_times_twice_norm')}),flush=True)
                release_pages(base,plus,minus,slopes)
                if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>args.rss_limit_mib*1024:
                    raise MemoryError('Observed minimax RSS exceeded configured guard')
        del base,plus,minus,slopes
    record=dict(scope=__doc__,source_sha256=sha(__file__),plan=str(args.plan),plan_sha256=sha(args.plan),
        minimax_algorithm_source_sha256=sha(Path(__file__).with_name('root_geometry_minimax_variable_controls.py')),
        complete_field_loader_source_sha256=sha(Path(__file__).with_name('root_geometry_minimax_from_plan.py')),
        whole_field_summary_source_sha256=sha(Path(__file__).with_name('root_saved_geometry_minimax.py')),
        response_file=str(response_path),response_sha256=sha(response_path),inputs=inputs,
        shape=list(shape),control_count=controls,directions=directions,baseline=baseline,directional_summaries=derivatives,
        observed_second_differences=second_differences,predictions=predictions,
        stale_geometry_slopes_used=False,accepted_nonlinear_solution=False,
        continuous_geometry_certified=False,actual_closed_diameter_certified=False,
        actual_reach_certified=False,new_bvp_or_tail_worker_started=False)
    args.out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out),sha256=sha(args.out),predictions=len(predictions))),flush=True)


if __name__=='__main__':
    main()
