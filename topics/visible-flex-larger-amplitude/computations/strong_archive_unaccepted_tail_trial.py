#!/usr/bin/env python3
"""Snapshot a real accepted tail Newton trial without calling it a solution.

Author: strong_recovery (GPT-6 Astra Pro, AI assisted), 2026-11-13.
Read one immutable byte snapshot of the running worker's recovery file.
Check its complete states, raw-node subset, actual new-H request and all
non-I/O tail parameters against the authentic prior response and launch.
No worker, residual evaluation, Jacobian, audit or acceptance is performed.
"""
from __future__ import annotations
import argparse
import datetime
import gzip
import hashlib
import json
import math
from pathlib import Path
import struct

IO = {'traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint'}
def sha(data): return hashlib.sha256(data).hexdigest()
def load_bytes(path):
    data=Path(path).read_bytes()
    return data,json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)
def bits(values): return b''.join(struct.pack('<d',float(v)) for v in values)
def put(path,data):
    if path.exists():
        if path.read_bytes()!=data:raise FileExistsError(path)
    else:
        with path.open('xb') as stream:stream.write(data)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('checkpoint','trace','prior-tail','launch-plan','archive-topic','out-prefix'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--expected-call',type=int,required=True)
    ap.add_argument('--expected-iteration',type=int,required=True)
    a=ap.parse_args();gates={}
    def check(name,value):
        if not value:raise ValueError(name)
        gates[name]=True
    raw,data=load_bytes(a.checkpoint);prior_bytes,prior=load_bytes(a.prior_tail)
    plan_bytes,plan=load_bytes(a.launch_plan);row=data.get('iteration',{})
    check('original_explicit_unconverged_trial',data.get('status')=='iteration-recovery-only'
          and data.get('call')==a.expected_call and row.get('iteration')==a.expected_iteration
          and row.get('phase')=='accepted-trial-recovery-only'
          and row.get('acceptedFromIteration')==a.expected_iteration-1
          and 0<float(row.get('acceptedStep',0))<=1 and math.isfinite(float(row['norm'])))
    checkpoint=data['checkpoint'];base=prior['response']['checkpoint']
    M=len(checkpoint['cutHeight']);K=2*M
    states=checkpoint['states'];nodes=checkpoint['rawNode'];subset=checkpoint['rawStates']
    check('complete_original_state_layout',M==int(prior['config']['modes'])
          and len(states)==len(base['states']) and nodes==base['rawNode']
          and len(subset)==len(nodes)
          and all(len(s)==K and all(math.isfinite(float(v)) for v in s) for s in states))
    check('complete_raw_subset_exact_JSON_bits',all(bits(subset[j])==bits(states[k]) for j,k in enumerate(nodes)))
    check('all_non_IO_parameters_exact',all(checkpoint['parameters'].get(k)==base['parameters'].get(k)
          for k in (set(checkpoint['parameters'])|set(base['parameters']))-IO))
    check('prior_response_original_full_J_converged',prior['response']['converged']
          and prior['request']['jacobian'] and prior['response']['residual']<=prior['config']['solveTolerance']
          and len(prior['response']['heightJetJacobian'])==(3*M+2)*M)
    cmd=plan['command'];prior_arg=cmd[cmd.index('--actual-reference-tail')+1]
    check('prior_tail_is_original_launch_input',Path(prior_arg).resolve()==a.prior_tail.resolve())
    wanted=plan['input_sha256'].get(str(a.prior_tail)) or plan['input_sha256'].get(prior_arg)
    check('prior_tail_original_launch_SHA',wanted==sha(prior_bytes))
    for name,digest in plan['source_sha256'].items():
        check('source_'+name,sha(Path(name).read_bytes())==digest)
    trace_bytes=a.trace.read_bytes();end=trace_bytes.rfind(b'\n')+1;trace_prefix=trace_bytes[:end]
    trace=[json.loads(line) for line in trace_prefix.splitlines() if line]
    requests=[r for r in trace if r.get('event')=='request' and r.get('call')==a.expected_call]
    check('one_actual_request_for_call',len(requests)==1)
    request=requests[0]
    check('complete_current_H_request_bits',len(request['height'])==M
          and bits(request['height'])==bits(checkpoint['cutHeight']))
    trials=[r for r in trace if r.get('event')=='iteration' and r.get('call')==a.expected_call
            and r.get('phase')=='accepted-trial-recovery-only' and r.get('iteration')==a.expected_iteration]
    check('actual_trace_trial_matches_saved_recovery',len(trials)==1
          and all(trials[0].get(k)==v for k,v in row.items()))
    check('trace_current_H_requires_original_full_J',request.get('jacobian') is True)
    changed=[r for r in trace if r.get('event')=='full_flow_tangent_restored']
    check('prior_fullflow_is_initial_guess_only',len(changed)==1 and changed[0].get('initialGuessOnly')
          and changed[0].get('completeFrozenIdentityMatched') and not changed[0].get('newTargetAccepted'))
    target=a.archive_topic/'notes';target.mkdir(parents=True,exist_ok=True)
    snapshot=target/(a.out_prefix.name+'-checkpoint.json.gz');put(snapshot,raw)
    evidence=dict(schema='unaccepted-tail-trial-recovery-snapshot-v1',scope=__doc__,
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),all_checks=all(gates.values()),
        gates=gates,source_sha256=sha(Path(__file__).read_bytes()),
        original_checkpoint_file=str(a.checkpoint),original_snapshot_sha256=sha(raw),
        original_trace_file=str(a.trace),read_trace_complete_prefix_bytes=len(trace_prefix),
        read_trace_complete_prefix_sha256=sha(trace_prefix),original_actual_request=request,
        original_accepted_trial_record=trials[0],original_fullflow_restoration=changed[0],
        launch_plan=dict(file=str(a.launch_plan),sha256=sha(plan_bytes)),
        prior_tail=dict(file=str(a.prior_tail),sha256=sha(prior_bytes)),
        states_shape=[len(states),K],raw_nodes=nodes,complete_current_H=request['height'],
        complete_H_f64le_sha256=sha(bits(request['height'])),
        complete_saved_JSON_state_f64le_sha256=sha(b''.join(bits(s) for s in states)),
        current_tail_solution_accepted=False,current_full_J_finished=False,current_audit_finished=False,
        current_full_BVP_accepted=False,original_running_job_changed=False,Node_ODE_or_newton_calls=0,
        files=[dict(file='notes/'+snapshot.name,bytes=len(raw),sha256=sha(raw))])
    out=a.out_prefix.with_suffix('.json');put(out,(json.dumps(evidence,indent=2,allow_nan=False)+'\n').encode())
    print(json.dumps(dict(out=str(out),sha256=sha(out.read_bytes()),checks=len(gates),
                         original_iteration=a.expected_iteration,norm=row['norm'],
                         current_solution_accepted=False)),flush=True)


if __name__=='__main__':main()
