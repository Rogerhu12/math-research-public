#!/usr/bin/env python3
"""Observe an unchanged command, preserving atomic live and terminal metadata.

A stale live record is not an exit code or evidence of a mathematical failure.
Namespace process IDs and sampled RSS do not establish whole-host process or
memory state. No equation, solver option or acceptance gate is modified.
"""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import time


def process_tree(root):
    todo, seen, values = [root], set(), {}
    while todo:
        pid = todo.pop()
        if pid in seen:
            continue
        seen.add(pid)
        base = Path('/proc') / str(pid)
        try:
            fields = {line.split(':', 1)[0]: line.split(':', 1)[1].strip()
                      for line in (base / 'status').read_text().splitlines() if ':' in line}
            values[str(pid)] = dict(name=fields['Name'],
                                    rss_kib=int(fields.get('VmRSS', '0 kB').split()[0]),
                                    hwm_kib=int(fields.get('VmHWM', '0 kB').split()[0]))
            todo.extend(int(x) for x in (base / 'task' / str(pid) / 'children').read_text().split())
        except (OSError, ValueError, KeyError):
            pass
    return values


def atomic(path, record):
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(record, indent=2) + '\n')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--log', type=Path, required=True)
    parser.add_argument('command', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command and args.command[0] == '--' else args.command
    if not command:
        raise ValueError('A command is required')
    live = args.out.with_name(args.out.stem + '-live.json')
    if args.out.exists() or args.log.exists() or live.exists():
        raise FileExistsError('Use a new observation/output prefix')
    args.log.parent.mkdir(parents=True, exist_ok=True)
    began = time.monotonic()
    maximum, peak, samples = 0, {}, 0
    common = dict(scope=__doc__, command=command,
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    with args.log.open('x') as log:
        process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT)
        while process.poll() is None:
            current = process_tree(process.pid)
            samples += 1
            total = sum(row['rss_kib'] for row in current.values())
            if total > maximum:
                maximum, peak = total, current
            atomic(live, dict(**common, status='observed_running',
                              observed_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                              namespace_child_pid=process.pid,
                              elapsed_seconds=time.monotonic() - began, samples=samples,
                              maximum_sampled_tree_rss_kib=maximum,
                              current_sampled_tree=current, child_returncode=None))
            time.sleep(2)
        returncode = process.wait()
    usage = resource.getrusage(resource.RUSAGE_CHILDREN)
    record = dict(**common, status='observed_terminal', child_returncode=returncode,
                  observed_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                  seconds=time.monotonic() - began, samples=samples,
                  maximum_sampled_tree_rss_kib=maximum, tree_at_sampled_peak=peak,
                  child_rusage_maxrss_kib=usage.ru_maxrss,
                  child_user_seconds=usage.ru_utime, child_system_seconds=usage.ru_stime)
    atomic(args.out, record)
    atomic(live, record)
    print(json.dumps(record))
    raise SystemExit(returncode)


if __name__ == '__main__':
    main()
