#!/usr/bin/env python3
"""Collect an observed completed q060 M8 trace initializer without rerunning it."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ref(path):return dict(path=str(Path(path).resolve()),sha256=sha(path))
def load(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
def binary(value):return np.asarray(value,dtype='float64').tobytes()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ['probe','resource','log','out']:
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--terminal-tool-chunk',required=True)
    args=parser.parse_args();d=load(args.probe);resource=load(args.resource)
    if resource['status']!='observed_terminal' or resource['child_returncode']!=0:
        raise ValueError('A genuine observed successful process termination is required')
    if resource['command'][1:]!=d['command'][1:]:raise ValueError('The observer belongs to another command')
    observer=Path(__file__).resolve().parent.parent/'resume_n4/observe_command_live.py'
    if sha(observer)!=resource['script_sha256']:raise ValueError('The observer source changed')
    plan=d['plan'];e=d['evaluation'];f=e['finite_initializer'];design=plan['design']
    if (e['BVP_solver_invoked'] or e['actual_tail_solver_invoked'] or e['original_restart_called'] or
        e['native_reference_constructed'] is not True or f['mean_height_reconstructed'] or f['full_metric_computed']):
        raise ValueError('The execution scope changed')
    for path,digest in e['source_sha256'].items():
        if sha(path)!=digest:raise ValueError('An executed source changed: '+path)
    for item in [d['evaluation_plan'],design['old_reference_binding'],design['old_checkpoint'],
                 design['reader'],design['actual_affine_tail_anchor'],*design['old_coefficient_chunks']]:
        if sha(item['path'])!=item['sha256']:raise ValueError('A frozen input changed: '+item['path'])
    frozen=load(d['evaluation_plan']['path'])
    if frozen['identity_sha256']!=plan['identity_sha256'] or e['plan_identity_sha256']!=plan['identity_sha256']:
        raise ValueError('The executed plan identity changed')
    tail=load(design['actual_affine_tail_anchor']['path'])
    H=tail['request']['height']
    if binary(H)!=binary(f['old_H']):raise ValueError('The original complete actual H changed')
    actual_H_equal=binary(f['full_H'])==binary(H)
    if actual_H_equal!=f['full_H_binary64_equal']:raise ValueError('The full-H equality report is inconsistent')
    c=e['actual_core'];physical=np.asarray(c['parameters'][1:])*np.asarray(c['parameter_scales'])
    if binary(physical)!=binary(c['physical_controls']):raise ValueError('The complete physical parameter chain changed')
    if f['actual_q']!=design['new_q']['binary64'] or f['new_p0']!=0. or f['final_frozen_delta']!=design['physical_profile']['delta']:
        raise ValueError('The unique new q or final-profile p0 convention changed')
    result=dict(status='Finite original initial-domain checks passed; no new solution was computed',
        probe=ref(args.probe),resource=ref(args.resource),combined_stdout_stderr_log=ref(args.log),
        observer_source=ref(observer),collector_sha256=sha(__file__),
        observed_execution=dict(tool_chunk=args.terminal_tool_chunk,observed_returncode=0,
            child_returncode=resource['child_returncode'],observed_utc=resource['observed_utc'],
            child_seconds=resource['seconds'],probe_seconds=d['seconds'],command=resource['command'],
            exit_provenance='Original command exit observed by the independent observer and the terminal exec tool.'),
        evaluation_plan=d['evaluation_plan'],plan_identity_sha256=plan['identity_sha256'],
        source_sha256=e['source_sha256'],old_reference_binding=design['old_reference_binding'],
        old_checkpoint=design['old_checkpoint'],old_coefficient_chunks=design['old_coefficient_chunks'],
        actual_affine_tail_anchor=design['actual_affine_tail_anchor'],
        new_core_settings=design['new_core_settings'],new_primary_q=design['new_q'],
        old_modes=8,new_modes=8,state_components=25,
        physical_profile=design['physical_profile'],meridian_length_binary64=design['meridian_length_binary64'],
        warp_reference_q=design['warp_reference_q'],original_chart=design['original_chart'],
        chart_payload_sha256=design['chart_payload_sha256'],physical_port=design['physical_port'],
        trace_mapping=e['trace_mapping'],actual_core=e['actual_core'],finite_initializer=f,
        native_reference_constructed=True,full_physical_control_chain_binary64_verified=True,
        complete_eight_H_encoding_comparison_verified=True,
        core_definition_provenance=e['core_definition_provenance'],
        BVP_solver_invoked=False,actual_tail_solver_invoked=False,original_restart_called=False,
        full_metric_computed=False,mean_height_reconstructed=False,
        limits='The initializer passes original numerical core/Frenet checks but is not an accepted BVP. The reference comparison uses the represented Fourier part; its omitted mean-height trajectory has not been reconstructed. The unchanged original actual tail is only an affine anchor for initial residual evaluation. No R38/R40/R41 geometric claim transfers to this new endpoint span.')
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=sha(args.out),bytes=args.out.stat().st_size)),flush=True)


if __name__=='__main__':main()
