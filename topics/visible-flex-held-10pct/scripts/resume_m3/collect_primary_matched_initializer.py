#!/usr/bin/env python3
"""Collect the completed unique-q trace initializer; no numerical rerun."""
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import struct


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def binary(values):return struct.pack('<'+'d'*len(values),*values)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probe',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--observed-tool-chunk',required=True)
    args=parser.parse_args();d=json.loads(args.probe.read_text())
    if d['BVP_solver_invoked'] or d['actual_tail_solver_invoked'] or d['original_restart_predictor_called']:
        raise ValueError('This record is only for the declared no-solver/no-predictor probe')
    for path,digest in d['source_sha256'].items():
        if sha(path)!=digest:raise ValueError('A source changed: '+path)
    for name in ['actual_seed_checkpoint','actual_affine_tail_anchor','unique_primary_mapping','old_constructor_check','reused_interface_checks']:
        item=d[name]
        if sha(item['path'])!=item['sha256']:raise ValueError('An input identity changed: '+name)
    for path,digest in d['coefficient_chunks'].items():
        if sha(path)!=digest:raise ValueError('An old physical coefficient chunk changed')
    mapping=json.loads(Path(d['unique_primary_mapping']['path']).read_text())
    if d['initialization_mapping']['actual_q']!=mapping['matched_q']['binary64']:
        raise ValueError('This initializer did not use the uniquely matched q')
    tail=json.loads(gzip.decompress(Path(d['actual_affine_tail_anchor']['path']).read_bytes()))
    finite=d['finite_initializer'];old_H=tail['request']['height']
    if binary(old_H)!=binary(finite['original_H']):raise ValueError('The complete actual affine-anchor H changed')
    new_H=finite['full_H'];changed=[i for i,(x,y) in enumerate(zip(new_H,old_H)) if binary([x])!=binary([y])]
    if changed!=finite['changed_H_components']:raise ValueError('The full-H difference count changed')
    differences=[dict(component=i,old=old_H[i],new=new_H[i],difference=new_H[i]-old_H[i],
        exactly_nextafter=math.nextafter(old_H[i],new_H[i])==new_H[i]) for i in changed]
    core=dict(d['actual_initial_core']);core['summary']={k:v for k,v in core['summary'].items() if not isinstance(v,(dict,list))}
    result=dict(status='Original initial core/domain checks passed; initial RMS is not an accepted BVP solution',
        observed_execution=dict(tool_chunk=args.observed_tool_chunk,observed_returncode=0,
            exit_provenance='Actual exec_command terminal tool observation; no independent resource observer was used.',
            seconds=d['seconds'],command=['python',*d['command']]),
        probe=dict(path=str(args.probe.resolve()),sha256=sha(args.probe)),collector_sha256=sha(__file__),
        source_sha256=d['source_sha256'],actual_seed_checkpoint=d['actual_seed_checkpoint'],
        coefficient_chunks=d['coefficient_chunks'],actual_affine_tail_anchor=d['actual_affine_tail_anchor'],
        unique_primary_mapping=d['unique_primary_mapping'],old_constructor_check=d['old_constructor_check'],
        new_core_settings=d['new_core_settings'],modes=d['modes'],angular=d['angular'],
        projection_angular=d['projection_angular'],initial_nodes_argument=d['initial_nodes_argument'],
        initialization_mapping=d['initialization_mapping'],actual_initial_core=core,
        finite_initializer=finite,full_H_differences=differences,
        represented_map_scope='The position/angular jets compared are geo plus the complete represented Fourier field. The state has no mean-height primitive; its true mean-height trajectory must still be rebuilt by the original flow.height_integral. These differences do not claim to copy the full physical three-dimensional map.',
        interface_evidence_reused=d['reused_interface_checks'],
        core_definition_provenance=d['core_definition_provenance'],
        primary_match_initializer_source_transform=d['primary_match_initializer_source_transform'],
        BVP_solver_invoked=False,actual_tail_solver_invoked=False,original_restart_predictor_called=False,
        limits='New physical endpoint design and new finite control span. No complete metric or accepted actual tail at the rounded new H is asserted, and no R38/R40/R41 geometry is inherited. The previous finite zero-trace/primitive checks retain their recorded scope; no numerical map/field arrays are stored here.')
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=sha(args.out),bytes=args.out.stat().st_size)),flush=True)


if __name__=='__main__':main()
