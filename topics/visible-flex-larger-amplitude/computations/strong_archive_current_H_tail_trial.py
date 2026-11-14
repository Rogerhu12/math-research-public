#!/usr/bin/env python3
"""Freeze an original accepted tail trial at the full pending-prefix H.

This is recovery only. The original pending prefix, its complete cut H, the
prior true finite-tail packet and current original trace remain bound by SHA.
No completed full Jacobian, audit, coupled prefix or closed surface is inferred
from an accepted trial, even when its recorded norm is below tolerance.
"""
from __future__ import annotations
import argparse
import datetime
import gzip
import hashlib
import io
import json
from pathlib import Path
import numpy as np

IO_KEYS = {'traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('iteration-checkpoint','trace','pending-prefix-manifest','prior-tail',
                 'config','launch-plan','out-prefix','archive-topic'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--expected-call',type=int,required=True)
    p.add_argument('--expected-iteration',type=int,required=True)
    a = p.parse_args()
    trial, pending, prior, config = [read(path) for path in
        (a.iteration_checkpoint,a.pending_prefix_manifest,a.prior_tail,a.config)]
    event, checkpoint = trial['iteration'], trial['checkpoint']
    if (trial['status'] != 'iteration-recovery-only' or trial['call'] != a.expected_call
            or event['iteration'] != a.expected_iteration
            or event['phase'] != 'accepted-trial-recovery-only'
            or not np.isfinite(event['norm']) or not 0 < event['acceptedStep'] <= 1):
        raise ValueError('The original requested accepted trial is missing')
    if (not pending['complete_raw_array_hashes_shapes_and_coverage_verified']
            or not pending['actual_nonlinear_coupling_pending'] or pending['solver_success']
            or pending['original_inner_RMS'] > pending['original_RMS_tolerance']
            or pending['prior_warm_tail']['sha256'] != sha(a.prior_tail)):
        raise ValueError('The real complete pending prefix/prior-tail binding differs')
    raw_path = Path(pending['raw_file'])
    if sha(raw_path) != pending['raw_sha256']:
        raise ValueError('The original pending raw header differs')
    raw = read(raw_path)
    blocks, end = [], 0
    metadata = raw['arrays']['y']
    for chunk in metadata['chunks']:
        path = raw_path.parent/chunk['file']
        if chunk['first'] != end or sha(path) != chunk['sha256']:
            raise ValueError('The complete original raw field chunk coverage/checksum differs')
        block = np.load(io.BytesIO(gzip.decompress(path.read_bytes())),allow_pickle=False)
        if block.shape != (chunk['count'],) or block.dtype != np.float64 or not np.isfinite(block).all():
            raise ValueError('The original complete raw field is invalid')
        blocks.append(block);end += len(block)
    if end != int(np.prod(metadata['shape'])):
        raise ValueError('The complete original raw field was not retained')
    y = np.concatenate(blocks).reshape(metadata['shape'])
    m, nodes = pending['modes'], pending['nodes']
    if y.shape != (3*m+1,nodes) or raw['identity']['modes'] != m:
        raise ValueError('The original pending mode/field shape differs')
    H = -float(raw['identity']['gauge'])*y[2*m+1:,-1]
    if (H.tobytes() != np.asarray(pending['full_current_H'],dtype=np.float64).tobytes()
            or H.tobytes() != np.asarray(checkpoint['cutHeight'],dtype=np.float64).tobytes()):
        raise ValueError('The complete actual pending H bits do not match this original trial')
    prior_response = prior['response']
    if (not prior['request']['jacobian'] or not prior_response['converged']
            or prior_response['residual'] > prior['config']['solveTolerance']
            or not prior_response['fullFlowTangentSnapshot']['roundtrip']['allBaseAndFlowValuesBitwiseEqual']
            or canonical(prior['config']) != canonical(config)):
        raise ValueError('The original same-configuration full-J prior tail differs')
    if canonical({k:v for k,v in checkpoint['parameters'].items() if k not in IO_KEYS}) != canonical(
            {k:v for k,v in prior_response['checkpoint']['parameters'].items() if k not in IO_KEYS}):
        raise ValueError('The original effective mathematical tail parameters changed')
    states = np.asarray(checkpoint['states'],dtype=np.float64)
    idx = np.asarray(checkpoint['rawNode'],dtype=np.int64)
    raw_states = np.asarray(checkpoint['rawStates'],dtype=np.float64)
    if (states.shape != (checkpoint['parameters']['depth']+1,2*m)
            or raw_states.shape != (len(idx),2*m) or not np.isfinite(states).all()
            or np.any(idx < 0) or np.any(idx >= len(states))
            or idx.tolist() != prior_response['checkpoint']['rawNode']
            or states[idx].tobytes() != raw_states.tobytes()):
        raise ValueError('The complete original current shooting states/raw indices differ')
    trace = [json.loads(line) for line in a.trace.read_text().splitlines()]
    match = [row for row in trace if row.get('event') == 'iteration'
        and row.get('call') == a.expected_call and all(row.get(k) == v for k,v in event.items())]
    if len(match) != 1:
        raise ValueError('No unique original accepted-trial trace receipt exists')
    observed = [row for row in trace if row.get('call') == a.expected_call
        and row.get('event') in ('request','tangent_warm_predictor','exact_initial_stage_seed_saved','iteration')]
    snapshot = Path(str(a.out_prefix)+'.json.gz')
    trace_path = Path(str(a.out_prefix)+'-observed-trace.json')
    for file,payload in ((snapshot,a.iteration_checkpoint.read_bytes()),
            (trace_path,(json.dumps(observed,indent=2,allow_nan=False)+'\n').encode())):
        file.parent.mkdir(parents=True,exist_ok=True)
        with file.open('xb') as stream:stream.write(payload)
    entries = []
    for file in (snapshot,trace_path,a.config):
        payload = file.read_bytes()
        if len(payload) >= 5_000_000:raise ValueError('Original repository single-file cap exceeded')
        target = a.archive_topic/'notes'/file.name
        if target.exists():
            if target.read_bytes() != payload:raise ValueError('Existing immutable recovery bytes differ')
        else:
            with target.open('xb') as stream:stream.write(payload)
        entries.append(dict(file='notes/'+file.name,sha256=sha(file),bytes=len(payload)))
    result = dict(scope=__doc__,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        archiver_source_sha256=sha(__file__),
        source_identity={str(path):sha(path) for path in
            (a.iteration_checkpoint,a.pending_prefix_manifest,a.prior_tail,a.config,a.launch_plan,raw_path)},
        original_call=a.expected_call,original_iteration=event,modes=m,
        shooting_states_shape=list(states.shape),raw_states_shape=list(raw_states.shape),
        complete_original_pending_H_bits_verified=True,complete_current_H=H.tolist(),
        original_effective_mathematical_parameters_unchanged=True,
        original_current_H_final_Jacobian_pending=True,original_physical_BC_and_audit_pending=True,
        actual_coupled_prefix_or_closed_surface_accepted=False,original_live_job_unchanged=True,
        prior_full_J_source_sha256=prior['source_sha256'],
        files=entries,total_bytes=sum(row['bytes'] for row in entries))
    manifest = Path(str(a.out_prefix)+'-manifest.json')
    with manifest.open('x') as stream:json.dump(result,stream,indent=2,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(manifest=str(manifest),sha256=sha(manifest),
        norm=event['norm'],complete_current_H_bits_verified=True,files=len(entries))),flush=True)


if __name__ == '__main__':
    main()
