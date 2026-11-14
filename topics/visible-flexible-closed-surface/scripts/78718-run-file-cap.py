#!/usr/bin/env python3
"""Exec an unchanged command with a strict per-file write resource limit.

The default limit is 4,999,999 bytes, strictly below the repository's 5 MB
per-file rule.  This does not bound aggregate storage, process memory, or
pre-existing files.  A larger attempted write fails in the original process;
such a process/output is not a successful mathematical result.
"""
import argparse
import json
import os
import resource


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cap-bytes', type=int, default=4_999_999)
    parser.add_argument('command', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if not 0 < args.cap_bytes < 5_000_000:
        parser.error('cap-bytes must be positive and strictly below 5,000,000')
    command = args.command
    if command[:1] == ['--']:
        command = command[1:]
    if not command:
        parser.error('An actual command is required after --')
    inherited = resource.getrlimit(resource.RLIMIT_FSIZE)
    finite = [x for x in inherited if x != resource.RLIM_INFINITY]
    cap = min([args.cap_bytes] + finite)
    resource.setrlimit(resource.RLIMIT_FSIZE, (cap, cap))
    effective = resource.getrlimit(resource.RLIMIT_FSIZE)
    if effective != (cap, cap):
        raise RuntimeError('Actual RLIMIT_FSIZE differs from the requested cap')
    print(json.dumps({'resource_only': 'RLIMIT_FSIZE', 'effective_bytes': list(effective),
                      'original_argv_and_environment_preserved': True}), flush=True)
    os.execvpe(command[0], command, os.environ.copy())


if __name__ == '__main__':
    main()
