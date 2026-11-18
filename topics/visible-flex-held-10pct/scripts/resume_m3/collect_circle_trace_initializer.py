#!/usr/bin/env python3
"""Make a compact record from an existing trace-space initializer probe."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import struct


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
def packed(values):return struct.pack('<'+'d'*len(values),*values)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--probe',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--session',type=int,required=True)
    a=p.parse_args();d=load(a.probe)
    if d['BVP_solver_invoked'] is not False or d['actual_tail_solver_invoked'] is not False:
        raise ValueError('Only the finite no-solver initializer probe is eligible')
    for path,digest in d['source_sha256'].items():
        if sha(path)!=digest:raise ValueError('Source changed: '+path)
    for key in ['actual_seed_checkpoint','actual_affine_tail_anchor','original_gauge_seed_record']:
        ref=d[key]
        if sha(ref['path'])!=ref['sha256']:raise ValueError('Input or initializer record changed: '+key)
    for path,digest in d['coefficient_chunks'].items():
        if sha(path)!=digest:raise ValueError('Physical coefficient chunk changed: '+path)
    cmd=d['command'];run=Path(cmd[cmd.index('--reference-run')+1])
    launch=load(run/'continuation-command.json')
    for path,digest in launch['inputs'].items():
        if sha(path)!=digest:raise ValueError('Recorded reference-run input changed: '+path)
    gauge=load(d['original_gauge_seed_record']['path'])
    tail=load(d['actual_affine_tail_anchor']['path'])
    if packed(gauge['initial_tail_height'])!=packed(tail['request']['height']):
        raise ValueError('The recorded original gauge initializer has another complete H')
    if d['interface_checks']['retained_raw_jets_binary64_identical']!=[True]*5:
        raise ValueError('One retained raw source jet changed')
    mapping=d['initialization_mapping']
    intended=list(mapping['old_full_controls'])
    intended[-2:]=[mapping['trace_coordinates']['t'],mapping['trace_coordinates']['u']]
    result=dict(status='New finite-space initializer diagnostic only; no BVP or actual tail solve',
        observed_execution=dict(session=a.session,observed_returncode=0,seconds=d['seconds'],
            command=['python',*d['command']]),
        scope=d['scope'],probe=dict(path=str(a.probe.resolve()),sha256=sha(a.probe)),
        collector_sha256=sha(__file__),source_sha256=d['source_sha256'],
        reference_run_launch=dict(path=str((run/'continuation-command.json').resolve()),sha256=sha(run/'continuation-command.json')),
        reference_run_inputs=launch['inputs'],
        actual_seed_checkpoint=d['actual_seed_checkpoint'],coefficient_chunks=d['coefficient_chunks'],
        actual_affine_tail_anchor=d['actual_affine_tail_anchor'],
        original_gauge_seed_record=d['original_gauge_seed_record'],
        original_gauge_seed_full_H_binary64_verified=True,
        original_gauge_seed_H_binary64_sha256=hashlib.sha256(packed(gauge['initial_tail_height'])).hexdigest(),
        new_candidate_full_H_formed='full_H_binary64_equal' in d['finite_initializer'],
        new_candidate_full_H_binary64_verified=d['finite_initializer'].get('full_H_binary64_equal'),
        new_core_settings=d['new_core_settings'],modes=d['modes'],angular=d['angular'],
        initial_nodes_argument=d['initial_nodes_argument'],projection_angular=d['projection_angular'],
        initialization_mapping=mapping,intended_physical_controls=intended,
        numerical_coordinate_scales=gauge['original_control_scales'],
        interface_checks=d['interface_checks'],
        actual_initial_core=d.get('actual_initial_core'),finite_initializer=d['finite_initializer'],
        derived_core_source_sha256=d['core_definition_provenance']['derived_core_source_sha256'],
        combined_guard_scope=d['core_definition_provenance']['control_guard_budget_scope'],
        unchanged_rho_floor=d['core_definition_provenance']['unchanged_rho_floor'],
        unchanged_grid_ceiling=d['core_definition_provenance']['unchanged_grid_ceiling'],
        BVP_solver_invoked=False,actual_tail_solver_invoked=False,
        limits=d['limits'])
    a.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),sha256=sha(a.out),bytes=a.out.stat().st_size)))


if __name__=='__main__':main()
