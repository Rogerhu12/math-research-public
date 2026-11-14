#!/usr/bin/env python3
"""Replay a saved finite-tail plan after relocating only source and output paths.

No numerical or physical argument is changed.  The supplied old successful
checkpoint remains the warm start.  The new report distinguishes reproduction
of an external boundary experiment from a coupled stronger prefix or closure.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--source-topic', type=Path, required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text())
    argv = list(plan['arguments'])
    probe = Path(argv[1])
    if sha256(probe) != plan['probe_script_sha256']:
        raise ValueError('Saved numerical probe source differs from recorded plan')
    base = Path(plan['base_actual_response'])
    if sha256(base) != plan['base_actual_response_sha256']:
        raise ValueError('Saved successful initial tail differs from recorded plan')
    direction = Path(plan['direction_file'])
    if sha256(direction) != plan['direction_sha256']:
        raise ValueError('Saved full boundary direction differs from recorded plan')
    if not (args.source_topic / 'source-origin.json').exists():
        raise FileNotFoundError('Materialize the recorded source subset first')
    replacements = []
    for flag, value in [('--source-topic', str(args.source_topic.resolve())),
                        ('--out-prefix', str(args.out_prefix))]:
        index = argv.index(flag) + 1
        replacements.append({'flag': flag, 'old': argv[index], 'new': value})
        argv[index] = value
    if argv[0] != sys.executable:
        replacements.append({'flag': 'python-executable', 'old': argv[0],
                             'new': sys.executable})
        argv[0] = sys.executable
    normalized_old = list(plan['arguments'])
    normalized_new = list(argv)
    for flag in ['--source-topic', '--out-prefix']:
        normalized_old[normalized_old.index(flag) + 1] = '<path>'
        normalized_new[normalized_new.index(flag) + 1] = '<path>'
    normalized_old[0] = normalized_new[0] = '<python>'
    if normalized_old != normalized_new:
        raise AssertionError('A non-I/O command argument changed')
    args.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    record = args.out_prefix.with_name(args.out_prefix.name + '-replay-plan.json')
    with record.open('x') as stream:
        json.dump({'scope': __doc__, 'original_plan': str(args.plan),
                   'original_plan_sha256': sha256(args.plan),
                   'arguments': argv, 'path_changes': replacements,
                   'all_non_path_arguments_exactly_preserved': True,
                   'probe_sha256': sha256(probe),
                   'base_response_sha256': sha256(base),
                   'source_origin': json.loads((args.source_topic / 'source-origin.json').read_text()),
                   'script_sha256': sha256(Path(__file__))}, stream, indent=2)
        stream.write('\n')
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
               MKL_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1')
    subprocess.run(argv, env=env, check=True)


if __name__ == '__main__':
    main()
