#!/usr/bin/env python3
"""Bind a resumed first complete evaluation to its authentic saved state.

This covers stages before the first iteration callback.  It handles attempts
which stop during the first full Jacobian after loading an existing accepted
inner trial and therefore have no new accepted-trial event of their own.
The exact binary seed, recovery plan and every completed/hit input key are
checked. No ODE, Jacobian, worker, or numerical acceptance is performed here.
"""
import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path
import struct


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('checkpoint', 'seed', 'trace', 'plan', 'source-topic', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    args = parser.parse_args()
    sha = lambda data: hashlib.sha256(data).hexdigest()
    read = lambda path: json.loads(gzip.decompress(path.read_bytes()) if path.suffix == '.gz' else path.read_bytes())
    record, seed, plan = read(args.checkpoint), read(args.seed), read(args.plan)
    if record['status'] != 'iteration-recovery-only' or record['iteration']['phase'] != 'accepted-trial-recovery-only':
        raise ValueError('An authentic accepted inner trial is required')
    recovery = plan['iteration_recovery']
    if recovery['source_sha256'] != sha(args.checkpoint.read_bytes()):
        raise ValueError('The actual recovery plan has a different input')
    values = record['checkpoint']['states']
    flat = [x for row in values for x in row]
    binary = struct.pack('<'+'d'*len(flat), *flat)
    marker = seed['checkpoint']['exactInitialSeed']
    packed = marker['states']
    seed_bytes = base64.b64decode(packed['base64'], validate=True)
    if (packed['encoding'] != 'Float64LE-base64' or packed['shape'] != [len(values), len(values[0])]
            or seed_bytes != binary or packed['sha256'] != sha(binary)
            or recovery['full_state_from_saved_JSON_float64LE_sha256'] != sha(binary)):
        raise ValueError('The actually saved exact initial seed changed a state byte')
    identity = marker['stageIdentitySHA']
    core = args.source_topic/'scripts/78718-tail-tangent-core.mjs'
    anchor = 'try{f=cellFlow(n,states[n+1],withJac);}'
    if core.read_text().count(anchor) != 1:
        raise ValueError('The original stage-input formula changed')
    rows = [json.loads(line) for line in args.trace.read_bytes().splitlines() if line.strip()]
    stops = [i for i,row in enumerate(rows) if row.get('event') == 'iteration']
    end = stops[0] if stops else len(rows)
    events = [row for row in rows[:end] if row.get('event') == 'exact_stage_cache'
        and row.get('kind') in ('restored-exact-stage', 'stored-completed-stage')]
    if not events:
        raise ValueError('No completed initial-evaluation stage was recorded')
    checks = []
    for event in events:
        n = int(event['stage'])
        if not 0 <= n < len(values)-1:
            raise ValueError('A stage is outside the full state grid')
        source = struct.pack('<'+'d'*len(values[n+1]), *values[n+1])
        key = sha((identity+':'+str(n)+':true:').encode()+source)
        checks.append(dict(stage=n, kind=event['kind'], source_state_row=n+1,
            input_sha256=sha(source), full_key=key,
            passed=event['identitySHA'] == identity and event['inputSHA'] == sha(source) and event['key'] == key))
    passed = all(row['passed'] for row in checks)
    result = dict(scope=__doc__, passed=passed, source_sha256_at_start={str(p):sha(p.read_bytes())
        for p in (Path(__file__), core, args.checkpoint, args.seed, args.trace, args.plan)},
        checkpoint=str(args.checkpoint), complete_state_Float64LE_sha256=sha(binary),
        actual_binary_seed_state_bytes_identical=True, original_stage_input_formula=anchor,
        cache_identity_sha256=identity, first_iteration_callback_seen=bool(stops),
        checked_stages=len(checks), restored_stages=sum(r['kind']=='restored-exact-stage' for r in checks),
        newly_completed_stages=sum(r['kind']=='stored-completed-stage' for r in checks),
        full_stage_count=len(values)-1, checks=checks, numerical_solution_accepted=False,
        physical_evaluations=0, Node_workers=0)
    with args.out.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps({k:result[k] for k in ('passed','checked_stages','restored_stages','newly_completed_stages')}), flush=True)
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
