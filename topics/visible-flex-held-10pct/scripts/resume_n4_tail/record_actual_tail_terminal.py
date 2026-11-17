#!/usr/bin/env python3
"""Record an unaccepted actual tail terminal, distinguishing saved from accepted."""
import argparse
import json
from pathlib import Path
import shlex
from record_fixed_actual import sha, scalar_tree, load


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prefix', type=Path, required=True)
    parser.add_argument('--resource', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    stem = args.prefix
    source = stem.with_name(stem.name + '-summary.json')
    raw = load(source)
    assert not raw['solver_success']
    trace = stem.with_name(stem.name + '-worker-trace.jsonl')
    events = [json.loads(line) for line in trace.read_text().splitlines()]
    iterations = [row for row in events
                  if row.get('event') == 'iteration' and 'norm' in row]
    responses = {}
    accepted = 0
    for path in sorted(stem.parent.glob(stem.name + '-tail_*.json.gz')):
        rec = load(path)
        result = rec['response']
        success = bool(result.get('converged')) and not result.get('failed')
        accepted += int(success)
        responses[path.name] = dict(
            sha256=sha(path), accepted=success,
            failed=result.get('failed'), residual=result.get('residual'),
            last_iteration=result.get('lastIteration'),
            saved_iteration_checkpoint=bool(result.get('checkpoint')),
            request_audit=rec['request']['audit'],
            request_jacobian=rec['request']['jacobian'])
    resource = load(args.resource)
    result = scalar_tree(raw)
    result.update(
        scope='The full-height initial actual tail stopped at the original finite shooting line-search gate. The saved failed iterate is not an accepted tail. No prefix refinement, closed surface or mathematical nonexistence claim follows.',
        collector_sha256=sha(__file__),
        actual_command=shlex.join(raw['command']),
        raw_summary_sha256=sha(source),
        last_observed_iteration=iterations[-1] if iterations else None,
        observed_worker_events=len(events), tail_response_files=responses,
        accepted_tail_response_count=accepted,
        output_prefix_checkpoint_exists=stem.with_suffix('.json.gz').exists(),
        resource=scalar_tree(resource), resource_sha256=sha(args.resource),
        resource_semantics='child_rusage_maxrss_kib is the reported RUSAGE_CHILDREN maximum, not the sum or peak of a whole process tree. The sampled /proc tree here contains only the Python process, so its sampled maximum does not cover worker memory. Neither establishes an out-of-memory cause.',
        run_file_hashes={p.name: sha(p) for p in sorted(stem.parent.glob(stem.name + '*'))
                         if p.is_file()},
        log_sha256=sha(stem.parent.with_suffix('.log')),
        data_policy='Only source identities, parameters, named scalar diagnostics and hashes. Failed finite states and certificate tables remain scratch-only.')
    assert accepted == 0
    assert not result['output_prefix_checkpoint_exists']
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(bytes=args.out.stat().st_size, sha256=sha(args.out))))


if __name__ == '__main__':
    main()
