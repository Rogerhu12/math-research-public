#!/usr/bin/env python3
"""Read bounded first and last tracebacks of one actual returned Actions child.

This independent full reader is derived from read_actual_followup_failure.py
(ef017af52fd8b9801434b3af655f9fccb7d7a51e9bf0abb3ff5e85496659e338).
A launcher may append its own CalledProcessError after the original driver
traceback. Both tracebacks are therefore kept separately, with explicit bounded
tail and clipping scopes. No scientific arrays, report, F, J, or root are read.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path

DERIVED_FROM_SOURCE_SHA256 = 'ef017af52fd8b9801434b3af655f9fccb7d7a51e9bf0abb3ff5e85496659e338'
SCHEMA = 'actual-public-followup-first-and-last-failure-tracebacks-v1'
MARKER = b'Traceback (most recent call last):'


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            digest.update(block)
    return digest.hexdigest()


def clip(text, limit):
    if len(text) <= limit:
        return text, False
    separator = '\n[bounded diagnostic: middle characters omitted]\n'
    available = limit - len(separator)
    prefix = available // 2
    return text[:prefix] + separator + text[-(available-prefix):], True


def last_line(text, limit=2048):
    line = next((value.strip() for value in reversed(text.splitlines())
                 if value.strip()), '')
    return clip(line, limit)


def parse():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--status', type=Path, required=True)
    parser.add_argument('--step-id', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--expected-run-id', required=True)
    parser.add_argument('--expected-source-sha256', required=True)
    parser.add_argument('--expected-log-path', type=Path, required=True)
    parser.add_argument('--maximum-tail-bytes', type=int, default=64000)
    parser.add_argument('--maximum-excerpt-characters', type=int, default=7000)
    args = parser.parse_args()
    if not 1024 <= args.maximum_tail_bytes <= 64000:
        parser.error('Use at most 64000 bytes of the actual original log tail')
    if not 512 <= args.maximum_excerpt_characters <= 8000:
        parser.error('Use independently bounded tracebacks of at most 8000 characters')
    if (len(args.expected_source_sha256) != 64
            or any(c not in '0123456789abcdef' for c in args.expected_source_sha256)):
        parser.error('Expected source must be an actual lowercase SHA256')
    return args


def main():
    args = parse()
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'
            or os.environ.get('GITHUB_RUN_ID') != args.expected_run_id):
        raise RuntimeError('Read the declared actual child only in its original public Actions run')
    status_path = args.status.resolve()
    raw_root = status_path.parent.parent
    output = args.output.resolve()
    if raw_root not in output.parents or output.exists():
        raise ValueError('Use a fresh current-run raw diagnostic output')
    captured_status = status_path.read_bytes()
    status = json.loads(captured_status)
    matches = [record for record in status.get('completed', [])
               if record.get('step_id') == args.step_id]
    if len(matches) != 1:
        raise ValueError('The declared child must have exactly one actual returned status record')
    record = matches[0]
    if record.get('returncode') in (0, None):
        raise ValueError('Read a real failed child, not an unstarted step or success')
    if record.get('source_sha256') != args.expected_source_sha256:
        raise ValueError('Actual returned child source differs from its explicit expected source')
    log = Path(record['log']).resolve()
    if log != args.expected_log_path.resolve():
        raise ValueError('The actual completed child log differs from the explicitly declared original log')
    if raw_root not in log.parents or not log.is_file() or output in (status_path, log):
        raise ValueError('Read an existing original log inside this runner and preserve both inputs')
    before = log.stat()
    start = max(0, before.st_size - args.maximum_tail_bytes)
    with log.open('rb') as stream:
        stream.seek(start)
        tail_bytes = stream.read(args.maximum_tail_bytes)
    log_sha = sha(log)
    after = log.stat()
    if ((before.st_size, before.st_mtime_ns) !=
            (after.st_size, after.st_mtime_ns) or len(tail_bytes) != before.st_size-start):
        raise ValueError('The returned child log changed during this readonly capture')
    positions = []
    at = tail_bytes.find(MARKER)
    while at >= 0:
        positions.append(at)
        at = tail_bytes.find(MARKER, at+len(MARKER))
    first_text = ''
    last_text = ''
    if positions:
        first_end = positions[1] if len(positions) > 1 else len(tail_bytes)
        first_text = tail_bytes[positions[0]:first_end].decode('utf-8', errors='replace')
        last_text = tail_bytes[positions[-1]:].decode('utf-8', errors='replace')
    first_excerpt, first_clipped = clip(first_text, args.maximum_excerpt_characters)
    last_excerpt, last_clipped = clip(last_text, args.maximum_excerpt_characters)
    first_exception, first_exception_clipped = last_line(first_text)
    last_exception, last_exception_clipped = last_line(last_text)
    no_traceback_excerpt = ''
    no_traceback_clipped = False
    if not positions:
        no_traceback_excerpt, no_traceback_clipped = clip(
            '\n'.join(tail_bytes.decode('utf-8', errors='replace').splitlines()[-24:]),
            args.maximum_excerpt_characters)
    result = dict(
        schema=SCHEMA, source_sha256=sha(__file__),
        derived_from_source_sha256=DERIVED_FROM_SOURCE_SHA256,
        status_sha256=hashlib.sha256(captured_status).hexdigest(),
        status_sha256_scope='exact captured status bytes, not a later mutable status version',
        step_id=args.step_id, actual_source_sha256=record['source_sha256'],
        actual_source_commit=record.get('source_commit'),
        actual_returncode=record['returncode'],
        actual_recorded_seconds=record.get('seconds'),
        actual_log_path=str(log), actual_log_sha256=log_sha,
        actual_log_bytes=before.st_size,
        log_unchanged_during_read=True,
        tail_start_byte=start, tail_bytes_read=len(tail_bytes),
        maximum_tail_bytes=args.maximum_tail_bytes,
        captured_tail_contains_entire_log=(start == 0),
        captured_tail_sha256=hashlib.sha256(tail_bytes).hexdigest(),
        traceback_markers_in_captured_tail=len(positions),
        first_traceback_found=bool(positions),
        first_traceback_start_byte=(start+positions[0] if positions else None),
        first_traceback_is_first_in_entire_log=(start == 0 if positions else None),
        first_traceback_excerpt=first_excerpt,
        first_traceback_excerpt_clipped=first_clipped,
        first_traceback_final_nonempty_line=first_exception,
        first_traceback_final_line_clipped=first_exception_clipped,
        last_traceback_found=bool(positions),
        last_traceback_start_byte=(start+positions[-1] if positions else None),
        last_traceback_excerpt=last_excerpt,
        last_traceback_excerpt_clipped=last_clipped,
        last_traceback_final_nonempty_line=last_exception,
        last_traceback_final_line_clipped=last_exception_clipped,
        first_and_last_are_same_traceback=(len(positions) == 1),
        no_traceback_tail_excerpt=no_traceback_excerpt,
        no_traceback_tail_excerpt_clipped=no_traceback_clipped,
        maximum_excerpt_characters=args.maximum_excerpt_characters,
        traceback_scope='first and last markers in bounded original log tail; no missing prefix inferred',
        complete_log_published=False, scientific_arrays_read=False,
        scientific_reports_read=False, field_or_J_evaluations=0,
        numerical_failure_cause_inferred=False,
        github_run_id=os.environ.get('GITHUB_RUN_ID'),
        github_run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key: result[key] for key in
        ('schema', 'step_id', 'actual_returncode', 'actual_log_sha256',
         'traceback_markers_in_captured_tail',
         'first_traceback_final_nonempty_line', 'last_traceback_final_nonempty_line')},
        ensure_ascii=False, allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
