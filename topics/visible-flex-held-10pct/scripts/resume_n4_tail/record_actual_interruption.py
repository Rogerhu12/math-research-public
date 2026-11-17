#!/usr/bin/env python3
"""Record an observed worker interruption without labeling its unknown cause."""
import argparse
import json
from pathlib import Path
import shlex
from record_fixed_actual import sha,scalar_tree


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prefix',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();stem=args.prefix
    source=stem.with_name(stem.name+'-summary.json');raw=json.loads(source.read_text())
    if raw['solver_success']:raise ValueError('This collector records only an unaccepted terminal')
    trace=stem.with_name(stem.name+'-worker-trace.jsonl')
    events=[json.loads(line)for line in trace.read_text().splitlines()]
    iterations=[r for r in events if r.get('event')=='iteration'and 'norm'in r]
    record=scalar_tree(raw)
    record.update(scope='Observed worker signal termination during an unaccepted full-height initial actual tail. No BVP or tail success, mathematical failure or out-of-memory diagnosis is inferred.',
                  collector_sha256=sha(__file__),actual_command=shlex.join(raw['command']),
                  raw_summary_sha256=sha(source),last_observed_iteration=iterations[-1]if iterations else None,
                  observed_worker_events=len(events),
                  accepted_tail_response_files=len(list(stem.parent.glob(stem.name+'-tail_*.json.gz'))),
                  output_prefix_checkpoint_exists=stem.with_suffix('.json.gz').exists(),
                  run_file_hashes={p.name:sha(p)for p in sorted(stem.parent.glob(stem.name+'*'))if p.is_file()},
                  log_sha256=sha(stem.parent.with_suffix('.log')))
    args.out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(bytes=args.out.stat().st_size,sha256=sha(args.out))))


if __name__=='__main__':main()
