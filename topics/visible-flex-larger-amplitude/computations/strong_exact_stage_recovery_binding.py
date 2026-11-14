#!/usr/bin/env python3
"""Bind completed stage keys to the exact saved accepted-trial input rows.

The retained shooting core integrates stage n from states[n+1] to states[n].
No physical source is constructed and no cached numerical map is recalculated.
Only stages completed after the matching accepted-trial event are compared.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import struct


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('checkpoint', 'trace', 'source-topic', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--prior-inline-same-node-failed', action='store_true')
    args = parser.parse_args()
    sources = {str(Path(__file__).resolve()): sha(Path(__file__).read_bytes())}
    raw = args.checkpoint.read_bytes()
    record = json.loads(gzip.decompress(raw) if args.checkpoint.suffix == '.gz' else raw)
    checkpoint, progress = record['checkpoint'], record['iteration']
    if record['status'] != 'iteration-recovery-only' or progress['phase'] != 'accepted-trial-recovery-only':
        raise ValueError('An actual accepted inner-trial checkpoint is required')
    core = args.source_topic/'scripts/78718-tail-tangent-core.mjs'
    core_bytes = core.read_bytes()
    anchor = 'try{f=cellFlow(n,states[n+1],withJac);}'
    if core_bytes.decode().count(anchor) != 1:
        raise ValueError('Original stage input-index formula differs')
    sources[str(core)] = sha(core_bytes)
    trace_bytes = args.trace.read_bytes()
    rows = [json.loads(line) for line in trace_bytes.splitlines() if line.strip()]
    starts = [i for i, row in enumerate(rows) if row.get('event') == 'iteration'
        and row.get('phase') == progress['phase'] and row.get('iteration') == progress['iteration']
        and row.get('norm') == progress['norm']]
    if len(starts) != 1:
        raise ValueError('Matching actual accepted-trial event is not unique')
    selected = [row for row in rows[starts[0]+1:] if row.get('event') == 'exact_stage_cache'
        and row.get('kind') == 'stored-completed-stage']
    if not selected:
        raise ValueError('No newly completed stages follow this accepted trial')
    checks, wrong_same_node_matches = [], 0
    states = checkpoint['states']
    for row in selected:
        n, identity = int(row['stage']), row['identitySHA']
        if not 0 <= n < len(states)-1:
            raise ValueError('Stage index exceeds the complete raw state')
        values = states[n+1]
        data = struct.pack('<'+'d'*len(values), *values)
        key = sha((identity+':'+str(n)+':true:').encode()+data)
        wrong = struct.pack('<'+'d'*len(states[n]), *states[n])
        wrong_same_node_matches += sha(wrong) == row['inputSHA']
        checks.append(dict(stage=n, source_state_row=n+1, input_sha256=sha(data), key=key,
            identity_sha256=identity, input_matches=sha(data) == row['inputSHA'],
            complete_key_matches=key == row['key']))
    passed = all(row['input_matches'] and row['complete_key_matches'] for row in checks)
    result = dict(scope=__doc__, passed=passed, source_sha256_at_start=sources,
        checkpoint=str(args.checkpoint), checkpoint_sha256=sha(raw),
        trace=str(args.trace), trace_sha256=sha(trace_bytes),
        original_input_formula=anchor, original_stage_direction='n+1 to n',
        checked_completed_stages=len(checks), full_stage_count=len(states)-1,
        partial_Jacobian_only=len(checks) < len(states)-1,
        uncomputed_stage_input_bytes_not_claimed_checked=True,
        prior_inline_same_node_assumption=dict(incorrect_formula='states[n]',
            earlier_inline_failure_reported=args.prior_inline_same_node_failed,
            matching_inputs=wrong_same_node_matches,
            correction='Use the actual retained core formula states[n+1]. No mathematical code was changed.'),
        checks=checks, physical_evaluations=0, Node_workers=0,
        numerical_solution_accepted=False)
    with args.out.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(dict(passed=passed, checked_completed_stages=len(checks),
        original_stage_direction='n+1 to n', physical_evaluations=0, Node_workers=0)), flush=True)
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
