#!/usr/bin/env python3
"""Add regional maxima to the unchanged complete six-jet common-grid consumer.

Every original point, coefficient, arithmetic operation and full-domain
maximum is retained. A recorder partitions the very same computed arrays
at the fixed-width cut patch. It also preserves the explicit new-shooting
provenance checks of the resolved entry. No physical problem is changed.
"""
import argparse
import json
from pathlib import Path
import numpy as np
import exact_20261114_common_grid_refinement as core

HERE=Path(__file__).resolve().parent


def main():
    p=argparse.ArgumentParser(add_help=False)
    p.add_argument('--complete',type=Path,action='append',required=True)
    p.add_argument('--labels',required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--cut-width',type=float,default=.01)
    a,_=p.parse_known_args();labels=a.labels.split(',');own_hash=core.sha(__file__)
    if len(labels)!=len(a.complete):raise ValueError('Layer labels differ')
    bindings={}
    for path in a.complete:
        data=json.loads(path.read_text());binding=data.get('refinement_binding')
        if binding is not None:
            for flag in ('all_physical_parameters_equal','all_complete_H_equal','actual_newton_converged','DN_jacobian_present'):
                if binding.get(flag)is not True:raise ValueError('Missing fixed-H shooting refinement binding: '+flag)
            if binding['original_endpoint_nonmean_jets_reused']or not binding['residual']<binding['original_tolerance']:
                raise ValueError('Old endpoints or unaccepted residual in a claimed re-solve')
            if any(binding[key]not in data['input_sha256'].values()for key in ('baseline_config_sha256','baseline_response_sha256','config_sha256','response_sha256')):
                raise ValueError('Refinement response/config provenance is not an input')
            bindings[str(path.resolve())]=dict(kind='new fixed-H shooting states',**binding)
        else:
            bindings[str(path.resolve())]=dict(kind='original accepted shooting endpoints',integration_steps=data['steps'])
    original_layer=core.Layer;original_update=core.update;groups={};cut=None;next_comparison=0
    def make_group(kind,**names):
        return dict(kind=kind,**names,regions={k:dict(radial_samples=0,maxima={},witnesses={})for k in ('outer_patch_region','outside_patch')})
    def recording_layer(*args,**kwargs):
        nonlocal cut
        result=original_layer(*args,**kwargs)
        if cut is not None and cut!=result.assembly.cut:raise ValueError('Different physical cut radii')
        cut=result.assembly.cut
        groups[id(result.maxima)]=make_group('layer',label=result.label)
        return result
    def recording_update(maxima,witnesses,key,values,stage,points,theta):
        nonlocal next_comparison
        original_update(maxima,witnesses,key,values,stage,points,theta)
        identity=id(maxima)
        if identity not in groups:
            if key!='position'or next_comparison>=len(labels)-1:raise ValueError('Unexpected original common-grid update layout')
            i=next_comparison;next_comparison+=1
            groups[identity]=make_group('adjacent_comparison',left=labels[i],right=labels[i+1])
        group=groups[identity];r=np.asarray([q['r']for q in points],np.longdouble)
        patch=r>=np.longdouble(cut-a.cut_width)
        for name,mask in [('outer_patch_region',patch),('outside_patch',~patch)]:
            ids=np.flatnonzero(mask)
            if not len(ids):continue
            record=group['regions'][name]
            subset=[points[i]for i in ids]
            original_update(record['maxima'],record['witnesses'],key,values[ids],stage,subset,theta)
            if key==('metric'if group['kind']=='layer'else'position'):record['radial_samples']+=len(ids)
    core.Layer=recording_layer;core.update=recording_update
    try:
        core.main()
    finally:
        core.Layer=original_layer;core.update=original_update
    result=json.loads(a.out.read_text());baseline=result.pop('same_accepted_actual_response_sha256')
    for binding in bindings.values():
        if binding['kind']=='new fixed-H shooting states'and binding['baseline_response_sha256']!=baseline:
            raise ValueError('Refined layer belongs to another accepted prefix/H')
    if next_comparison!=len(labels)-1:raise ValueError('An adjacent comparison was not recorded')
    result.update(schema='same-g-resolved-regional-six-jet-comparison-v1',baseline_accepted_actual_response_sha256=baseline,
        readout_state_provenance=bindings,accepted_prefix_resolved=False,
        regional_recording=dict(definition='The unchanged original longdouble sample arrays, partitioned at r >= cut - width. No arithmetic or sample grid is replaced.',cut_radius=cut,cut_width=a.cut_width,groups=list(groups.values()),
            original_prefix=dict(same_saved_field=True,all_position_first_and_second_jet_differences=0.,reason='Every compared tail is attached to the exact same saved prefix and its unchanged mean anchor.')))
    result['source_sha256_at_start'][str(Path(__file__).resolve())]=own_hash
    result['limitations']=[x for x in result['limitations']if not x.startswith('Original accepted shooting endpoint data remain fixed;')]
    result['limitations'].append('New shooting layers are finite fixed-H tail re-solves. Original prefix supplies the common cut target and is not re-solved or re-accepted.')
    a.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='regional_resolved_complete',out=str(a.out),groups=len(groups),source_sha256_at_start=own_hash)),flush=True)

if __name__=='__main__':main()
