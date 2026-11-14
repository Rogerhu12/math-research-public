#!/usr/bin/env python3
"""Combine the same accepted A's old nine directions with four new loop columns.

The original primary/control exchange and nine directions remain exact saved
arrays. The four additional core-held directions come from a new complete
same-state J solve, whose repeated primary columns are compared numerically.
This is a local linear response collection, never a nonlinear solution.
"""
from __future__ import annotations

import argparse
import copy
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np

EXTRA=('loop_curvature','loop_radius','loop_speed','terminal_peak_fraction')


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--old',type=Path,required=True)
    parser.add_argument('--new',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    old,new=[json.loads(path.read_text()) for path in (args.old,args.new)]
    for value in (old,new):
        if value.get('schema')!='fixed-actual-to-three-control-response-v1' or not value.get('finished') or value.get('new_solution'):
            raise ValueError('Both original full responses must have finished')
    for key in ('modes','angular','nodes','physical_core_parameter_scales','control_order'):
        if old[key]!=new[key]:raise ValueError('Response dimensions or units differ: '+key)
    for key in ('profile','core','gauge','numerical_reference_knots','reference_coefficients'):
        if old['baseline'][key]!=new['baseline'][key]:raise ValueError('Response baseline differs: '+key)
    for key in ('input_raw','input_checkpoint'):
        if old['samechart_response_adapter'][key]!=new['samechart_response_adapter'][key]:
            raise ValueError('The complete accepted field source differs: '+key)
    for value in (old,new):
        if not value['baseline']['raw_state_bitwise_equal'] or not value['input_identity']['full_height_bitwise_equal']:
            raise ValueError('The original complete raw/H identity checks did not pass')
    differences=[]
    for field in ('delta','boost_length','boost_speed'):
        vectors=[]
        for value in (old,new):
            items=[item for item in value['tangent_arrays'] if item['file'].endswith('-external-'+field+'.npy.gz')]
            if len(items)!=1 or sha(items[0]['file'])!=items[0]['sha256']:raise ValueError('A repeated primary array changed')
            with gzip.open(items[0]['file'],'rb') as stream:vectors.append(np.load(stream,allow_pickle=False))
        units=np.r_[np.full(3*old['modes']*old['nodes']+old['nodes'],old['baseline']['gauge']),old['physical_core_parameter_scales']]
        relative=float(np.max(abs(units*(vectors[0]-vectors[1])))/max(float(np.max(abs(units*vectors[0]))),np.finfo(float).tiny))
        if relative>2e-7:raise ValueError('Same-state repeated primary response disagrees: '+field)
        differences.append(dict(field=field,physical_scaled_complete_relative_difference=relative))
    result=copy.deepcopy(old)
    for field in EXTRA:
        if field in result['fields']:raise ValueError('The loop control was already present')
        result['fields'].append(field)
        for key,label in (('external_responses','field'),('additional_core_held_directions','external_field')):
            matches=[row for row in new[key] if row[label]==field]
            if len(matches)!=1:raise ValueError('Missing complete new response: '+field)
            result[key].append(matches[0])
        for item in new['tangent_arrays']:
            if any(item['file'].endswith('-'+prefix+field+'.npy.gz') for prefix in
                    ('external-','external-half-','forcing-full-','forcing-half-','core-held-')):
                if sha(item['file'])!=item['sha256']:raise ValueError('A new complete response array changed')
                result['tangent_arrays'].append(item)
    result['source_sha256'].update(new['source_sha256'])
    result['source_sha256'][str(Path(__file__).resolve())]=sha(__file__)
    result['loop_same_state_collection']=dict(scope=__doc__,old=str(args.old),old_sha256=sha(args.old),
        new=str(args.new),new_sha256=sha(args.new),added_controls=list(EXTRA),
        repeated_full_primary_comparison=differences,
        original_nine_arrays_preserved=True,new_bridge_and_prefix_controls_synchronized=True,
        physical_tail_cut_and_parameters_unchanged=True,new_nonlinear_solution=False)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out),fields=len(result['fields']),repeated_primary_comparison=differences)),flush=True)


if __name__=='__main__':main()
