#!/usr/bin/env python3
"""Read one actual returned child failure without recomputing any science.

Only the declared current-run status and its genuine child log are read.
The compact output retains a bounded final Python traceback, file identities,
and the actual child return code. Scientific arrays/reports are not opened.
The complete log remains on the runner and is never published by this source.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--status', type=Path, required=True)
    p.add_argument('--step-id', required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--maximum-tail-bytes', type=int, default=16384)
    p.add_argument('--maximum-excerpt-characters', type=int, default=6000)
    args = p.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Actual runner-failure attribution belongs in the public repository Actions')
    if not 1024 <= args.maximum_tail_bytes <= 32768 or not 512 <= args.maximum_excerpt_characters <= 8000:
        raise ValueError('Use a bounded compact diagnostic, never the complete log')
    status_path = args.status.resolve()
    raw_root = status_path.parent.parent
    output = args.output.resolve()
    if raw_root not in output.parents or output.exists():
        raise ValueError('Use a fresh current-run raw diagnostic output')
    status = json.loads(status_path.read_text())
    matches = [record for record in status.get('completed', [])
               if record.get('step_id') == args.step_id]
    if len(matches) != 1:
        raise ValueError('The declared child must have exactly one actual returned status record')
    record = matches[0]
    if record.get('returncode') in (0, None):
        raise ValueError('This reader accepts a real failed child, not a setup failure or a success')
    log = Path(record['log']).resolve()
    if raw_root not in log.parents or not log.is_file():
        raise ValueError('The actual child log must remain inside the same runner work root')
    size = log.stat().st_size
    with log.open('rb') as stream:
        stream.seek(max(0, size-args.maximum_tail_bytes))
        tail = stream.read(args.maximum_tail_bytes).decode('utf-8', errors='replace')
    at = tail.rfind('Traceback (most recent call last):')
    excerpt = tail[at:] if at >= 0 else '\n'.join(tail.splitlines()[-12:])
    clipped = len(excerpt) > args.maximum_excerpt_characters
    excerpt = excerpt[-args.maximum_excerpt_characters:]
    exception = next((line.strip() for line in reversed(excerpt.splitlines()) if line.strip()), '')
    result = dict(schema='actual-public-followup-failure-attribution-v1',
        source_sha256=sha(__file__), status_sha256=sha(status_path),
        step_id=args.step_id, actual_source_sha256=record.get('source_sha256'),
        actual_source_commit=record.get('source_commit'),
        actual_returncode=record['returncode'], actual_recorded_seconds=record.get('seconds'),
        actual_log_path=str(log), actual_log_sha256=sha(log), actual_log_bytes=size,
        final_python_traceback_found=at >= 0, final_exception_line=exception,
        bounded_failure_excerpt=excerpt, excerpt_character_limit_reached=clipped,
        complete_log_published=False, scientific_arrays_read=False,
        field_or_J_evaluations=0, numerical_failure_cause_inferred=False,
        github_run_id=os.environ.get('GITHUB_RUN_ID'))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key: result[key] for key in
        ('schema', 'step_id', 'actual_returncode', 'actual_log_sha256', 'final_exception_line')},
        ensure_ascii=False, allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
