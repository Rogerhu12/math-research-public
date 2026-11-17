#!/usr/bin/env python3
"""Preserve named leading finite residual rows and source hashes, not full tables."""
import argparse
import json
from pathlib import Path
import shlex
from record_fixed_actual import sha, scalar_tree, load


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--diagnostic', type=Path, required=True)
    parser.add_argument('--resource', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    raw, resource = load(args.diagnostic), load(args.resource)
    assert not raw['inputAccepted']
    assert raw['replayNormalizedResidual'] == raw['inputLastIteration']['norm']
    result = scalar_tree(raw)
    result.update(collector_sha256=sha(__file__),
                  primary_row=raw['largestResidual'][0],
                  secondary_row=raw['largestResidual'][1],
                  lowest_A_row=raw['lowestA'][0],
                  diagnostic_sha256=sha(args.diagnostic),
                  resource_sha256=sha(args.resource),
                  resource=scalar_tree(resource),
                  actual_command=shlex.join(resource['command']),
                  omitted_derived_tables='largestResidual and lowestA; three named rows retained only',
                  data_policy='Complete finite state and full regenerated diagnostic tables remain scratch-only; the failed state is not promoted to accepted.')
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(bytes=args.out.stat().st_size, sha256=sha(args.out))))


if __name__ == '__main__':
    main()
