#!/usr/bin/env python3
"""Add native shared-worker and initial-iterate provenance to the original audit."""
import argparse
import contextlib
import io
import json
from pathlib import Path
import sys
from record_fixed_actual import main as base_main, load, sha, scalar_tree


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('prefix', 'input-prefix', 'resource', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    previous_argv = sys.argv
    try:
        sys.argv = [str(Path(__file__).with_name('record_fixed_actual.py')),
                    '--prefix', str(args.prefix), '--input-prefix', str(args.input_prefix),
                    '--out', str(args.out)]
        with contextlib.redirect_stdout(io.StringIO()):
            base_main()
    finally:
        sys.argv = previous_argv
    result = load(args.out)
    summary = load(args.prefix.with_name(args.prefix.name + '-summary.json'))
    resource = load(args.resource)
    result.update(collector_wrapper_sha256=sha(__file__),
                  execution_wrapper=summary['execution_wrapper'],
                  tail_initial_record_status=summary['tail_initial_record_status'],
                  initial_tail_sha256=summary['input_tail_sha256'],
                  resource=scalar_tree(resource), resource_sha256=sha(args.resource),
                  resource_semantics='RUSAGE_CHILDREN maxrss is not the peak sum of all concurrently running processes. /proc samples are reported only as sampled observations, not a complete memory bound.')
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(bytes=args.out.stat().st_size, sha256=sha(args.out),
                          ratios=result['observed_ratios'])))


if __name__ == '__main__':
    main()
