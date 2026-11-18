#!/usr/bin/env python3
"""Collect a finished path-run record without importing any numerical model.

Original process exit, inner acceptance, actual-tail acceptance and complete
physical audit are separate fields. Large raw arrays remain in scratch; this
collector hashes them and emits only necessary parameters and terminal scalars.
"""
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ref(path):return dict(path=str(Path(path).resolve()),sha256=sha(path))
def load(path):
    path=Path(path);data=path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix=='.gz' else data)
def write(path,value):
    with Path(path).open('x') as stream:json.dump(value,stream,indent=2,allow_nan=False);stream.write('\n')


def collect(directory,session,start_chunk,terminal_chunk,output):
    directory=Path(directory).resolve();plan=load(directory/'launch-plan.json')
    runner=load(directory/'runner-terminal.json');resource=load(directory/'resource.json')
    summary=load(directory/'seed-summary.json')
    if resource['status']!='observed_terminal' or resource['child_returncode'] is None:
        raise ValueError('A real observed terminal is required')
    for file,digest in plan['source_sha256'].items():
        if sha(file)!=digest:raise ValueError('Executed source changed: '+file)
    raw_paths=sorted(directory.glob('inner-*.json.gz'))
    returned=sorted(directory.glob('inner-??-returned.json.gz'))
    raw_manifest=[ref(p) for p in raw_paths]
    side_manifest=[ref(p) for p in sorted(directory.glob('inner-*-dn-anchor.json'))]
    inner=[]
    for file in returned:
        r=load(file);p=r['p'];scales=r['parameter_scales']
        controls=[p[j+1]*scales[j] for j in range(len(scales))]
        if controls!=r['original_physical_controls'] or not all(math.isfinite(v) for v in r['rms_residuals']):
            raise ValueError('Stored complete parameters/RMS identity differs')
        if len(r['y'])!=25 or any(len(v)!=len(r['x']) for v in r['y']):
            raise ValueError('Incomplete returned raw state')
        inner.append(dict(raw=ref(file),sidecar=ref(file.with_name(file.name.replace('.json.gz','-dn-anchor.json'))),
            solver_success=r['solver_success'],status=r['status'],message=r['message'],
            nodes=len(r['x']),mesh_iterations=r['niter'],maximum_rms=max(r['rms_residuals']),
            full_parameters=p,parameter_scales=scales,physical_controls=controls,
            candidate_H=r['candidate_cut_height'],raw_cubic_shape=[len(r['raw_cubic']['c']),
                len(r['raw_cubic']['c'][0]),len(r['raw_cubic']['c'][0][0])]))
    tails=[]
    for file in sorted(directory.glob('seed_tail_????.json.gz')):
        r=load(file);s=r['response'];accepted=s.get('converged') is True and math.isfinite(s.get('residual',math.inf)) and s['residual']<r['config']['solveTolerance']
        tails.append(dict(record=ref(file),request=r['request'],original_gate=r['config']['solveTolerance'],
            converged=accepted,residual=s.get('residual'),failure=s.get('failed'),last_iteration=s.get('lastIteration'),
            audit_returned=s.get('audit') is not None,checkpoint_available=s.get('checkpoint') is not None))
    events=[json.loads(line) for line in (directory/'domain-newton.jsonl').read_text().splitlines()]
    latest_stats=next((e['stats'] for e in reversed(events) if 'stats' in e),None)
    cp=directory/'seed.json.gz';physical=None
    if cp.exists():
        data=load(cp)
        physical=dict(checkpoint=ref(cp),original_solver_success=data.get('solver_success'),
            summary_saved='summary' in data,tail_seam_saved='tail_seam' in data,
            metric=data.get('summary',{}).get('metric_l1'),darboux=data.get('summary',{}).get('darboux_l1'),
            full_finite_terminal_saved=all(k in data for k in ('summary','tail_seam','actual_outer_checks')))
    manifest=directory/'terminal-input-manifest.json'
    write(manifest,dict(source_sha256=plan['source_sha256'],raw_snapshots=raw_manifest,raw_sidecars=side_manifest,
        returned_raw_records=[ref(p) for p in returned],tail_records=[r['record'] for r in tails]))
    result=dict(scope=__doc__,collector=ref(__file__),run_directory=str(directory),
        plan=ref(directory/'launch-plan.json'),preparation_plan=ref(directory/'continuation-plan.json'),
        resource=ref(directory/'resource.json'),runner_terminal=ref(directory/'runner-terminal.json'),
        original_summary=ref(directory/'seed-summary.json'),complete_input_manifest=ref(manifest),
        command_file=ref(directory/'launch-command.json'),original_execution_source=plan['runner'],
        observed_session=session,observed_launch_chunk=start_chunk,observed_terminal_chunk=terminal_chunk,
        observed_utc=resource['observed_utc'],child_returncode=resource['child_returncode'],
        worker_returncode=runner['observed_worker_returncode'],seconds=resource['seconds'],
        lambda_value=plan['design']['lambda_value'],support_q=plan['design']['new_q']['q_binary64'],
        q_gauge=.06,base_profile=plan['design']['physical_profile'],
        original_main_returned=runner['original_main_returned'],original_solver_success=runner.get('original_solver_success'),
        error=runner.get('original_error'),raw_inner_calls=runner['raw_inner_calls'],
        actual_tail_calls=runner['actual_tail_calls'],verified_source_count=len(plan['source_sha256']),
        raw_snapshot_count=len(raw_manifest),raw_sidecar_count=len(side_manifest),
        original_newton_stats=latest_stats,returned_inner=inner,actual_tail=tails,
        physical_terminal=physical,full_prefix_metric_obtained=bool(physical and physical['summary_saved']),
        scope_boundaries='A zero process exit is not mathematical acceptance. An accepted inner does not imply an accepted changed-H tail or a complete physical audit. No model, flow, BVP, tail, mean or metric is recomputed by this collector.')
    write(output,result)
    print(json.dumps(dict(output=ref(output),source_count=len(plan['source_sha256']),raw=len(raw_manifest),
                          inner=len(inner),tails=len(tails),physical=physical)))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',type=Path,required=True);parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--session',type=int,required=True)
    parser.add_argument('--launch-chunk',required=True);parser.add_argument('--terminal-chunk',required=True)
    a=parser.parse_args();collect(a.run,a.session,a.launch_chunk,a.terminal_chunk,a.out)
