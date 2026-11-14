#!/usr/bin/env python3
"""Common-grid comparison with explicit new-shooting versus old-endpoint provenance.

The unchanged comparison evaluates the actual fixed-width patched fields.
This entry validates and records the same-H re-solve binding and removes the
old entry's blanket statement that every layer reuses old shooting endpoints.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(add_help=False)
    p.add_argument('--complete',type=Path,action='append',required=True)
    p.add_argument('--out',type=Path,required=True)
    a,_=p.parse_known_args()
    own_hash=sha(__file__)
    bindings={}
    for path in a.complete:
        data=json.loads(path.read_text())
        binding=data.get('refinement_binding')
        if binding is not None:
            for flag in ('all_physical_parameters_equal','all_complete_H_equal','actual_newton_converged','DN_jacobian_present'):
                if binding.get(flag) is not True:
                    raise ValueError('Missing fixed-H shooting refinement binding: '+flag)
            if binding['original_endpoint_nonmean_jets_reused'] or not binding['residual']<binding['original_tolerance']:
                raise ValueError('Old endpoints or unaccepted residual in a claimed re-solve')
            if any(binding[key] not in data['input_sha256'].values() for key in
                   ('baseline_config_sha256','baseline_response_sha256','config_sha256','response_sha256')):
                raise ValueError('Refinement response/config provenance is not an input')
            bindings[str(path.resolve())]=dict(kind='new fixed-H shooting states',**binding)
        else:
            bindings[str(path.resolve())]=dict(kind='original accepted shooting endpoints',
                integration_steps=data['steps'],source_definition='Original endpoints remain fixed; genuine interior RK readout may use a finer step count.')
    original=HERE/'exact_20261114_common_grid_refinement.py'
    spec=importlib.util.spec_from_file_location('exact_resolved_common_base',original)
    base=importlib.util.module_from_spec(spec);sys.modules[spec.name]=base;spec.loader.exec_module(base)
    base.main()
    result=json.loads(a.out.read_text())
    baseline=result.pop('same_accepted_actual_response_sha256')
    for binding in bindings.values():
        if binding['kind']=='new fixed-H shooting states' and binding['baseline_response_sha256']!=baseline:
            raise ValueError('Refined layer belongs to another accepted prefix/H')
    result['schema']='same-g-resolved-shooting-common-grid-comparison-v1'
    result['baseline_accepted_actual_response_sha256']=baseline
    result['source_sha256_at_start'][str(Path(__file__).resolve())]=own_hash
    result['readout_state_provenance']=bindings
    result['accepted_prefix_resolved']=False
    result['limitations']=[x for x in result['limitations'] if not x.startswith('Original accepted shooting endpoint data remain fixed;')]
    result['limitations'].append('New shooting layers are finite fixed-H tail re-solves. The original prefix supplies the common cut target and is not re-solved or re-accepted.')
    a.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='resolved_provenance_complete',output=str(a.out),layers=len(bindings))),flush=True)


if __name__=='__main__':
    main()
