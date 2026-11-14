#!/usr/bin/env python3
"""Record a completed tool-session poll without touching the numerical worker.

Call after each actual write_stdin poll. This records observation times, tool
exit status, the latest mathematical trace row, checkpoint freshness, and free
memory/disk. It does not infer why a process died or treat tool exit0 as a
successful nonlinear response.
"""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--prefix', type=Path, required=True)
p.add_argument('--session', type=int, required=True)
p.add_argument('--state', choices=('running', 'exited'), required=True)
p.add_argument('--tool-exit-code', type=int)
p.add_argument('--stdout-chars', type=int, default=0)
a = p.parse_args()
file = lambda suffix: a.prefix.with_name(a.prefix.name + suffix)
row = {'observed_at_UTC': datetime.now(timezone.utc).isoformat(),
       'tool_session': a.session, 'tool_state': a.state,
       'tool_exit_code': a.tool_exit_code, 'stdout_chars': a.stdout_chars}
try:
    for line in Path('/proc/meminfo').read_text().splitlines():
        if line.startswith('MemAvailable:'):
            row['machine_available_memory_KiB'] = int(line.split()[1])
            break
    fs = os.statvfs(a.prefix.parent)
    row['filesystem_available_bytes'] = fs.f_bavail * fs.f_frsize
    trace = file('-trace.jsonl')
    if trace.exists():
        with trace.open('rb') as stream:
            stream.seek(max(0, trace.stat().st_size - 16384))
            lines = stream.read().splitlines()
        if lines:
            latest = json.loads(lines[-1])
            keys = ('time', 'event', 'call', 'iteration', 'norm', 'phase', 'converged', 'residual')
            row['latest_trace'] = {key: latest[key] for key in keys if key in latest}
    checkpoint = file('-iteration.json.gz')
    if checkpoint.exists():
        stat = checkpoint.stat()
        row['iteration_checkpoint'] = {'bytes': stat.st_size, 'mtime_unix': stat.st_mtime}
    summary = file('-summary.json')
    if summary.exists():
        saved = json.loads(summary.read_text())
        keys = ('external_boundary_target_reached', 'converged', 'residual', 'error', 'worker_returncode_at_error',
                'worker_returncode_final', 'peak_child_rss_KiB')
        row['saved_report_status'] = {key: saved[key] for key in keys if key in saved}
except (OSError, ValueError, json.JSONDecodeError) as exc:
    row['observation_error'] = repr(exc)
with file('-session-watch.jsonl').open('a') as stream:
    stream.write(json.dumps(row, separators=(',', ':')) + '\n')
print(json.dumps(row))
