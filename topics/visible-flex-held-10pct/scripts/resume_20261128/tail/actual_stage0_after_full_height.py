#!/usr/bin/env python3
"""After a genuine full-H response, export/certify only its actual full stage 0.

This orchestration measures output bytes and sampled summed descendant RSS;
it never starts geometry from a predictor or a partial native return.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import time


def ref(path):
    p = Path(path).resolve()
    return dict(path=str(p), sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def tree_rss(pid):
    """Sum resident pages, including shared pages separately, conservatively."""
    seen, total, todo = set(), 0, [pid]
    while todo:
        p = todo.pop()
        if p in seen:
            continue
        seen.add(p)
        try:
            root = Path('/proc') / str(p)
            total += int((root / 'statm').read_text().split()[1]) * os.sysconf('SC_PAGE_SIZE')
            todo.extend(map(int, (root / 'task' / str(p) / 'children').read_text().split()))
        except (OSError, ValueError, IndexError):
            pass
    return total


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'full-height-summary', 'outdir'):
        p.add_argument('--' + name, type=Path, required=True)
    a = p.parse_args()
    repo, work, summary, out = map(lambda p:p.resolve(),
        (a.repo, a.work, a.full_height_summary, a.outdir))
    if repo == work or repo in work.parents or work not in out.parents or out.exists():
        raise ValueError('Use a new geometry output under the external work directory')
    print(json.dumps(dict(event='waiting_for_genuine_fullH', summary=str(summary))), flush=True)
    while True:
        state = json.loads(summary.read_text())
        if (state.get('status') == 'original_complete_height_tail_returned'
                and state.get('result', {}).get('accepted') is True
                and state['result'].get('original_full_height_returned') is True):
            break
        if state.get('status', '').endswith('_failed'):
            raise RuntimeError('No genuine complete field returned; geometry not launched')
        time.sleep(5)
    row = state['stages'][-1]
    manifest = json.loads(Path(row['native_manifest']['path']).read_text())
    packet = Path(state['result']['full_height_record'])
    if ref(packet) != row['packet'] or ref(row['native_manifest']['path']) != row['native_manifest']:
        raise ValueError('The real packet or native manifest changed')
    free = shutil.disk_usage(work).free
    if free < 64_000_000:
        raise RuntimeError('Insufficient scratch for the actual stage-zero size measurement')
    entry = repo / 'topics/visible-flex-held-10pct/scripts/resume_20261126/seam_run_tail_geometry_v2.py'
    command = [sys.executable, str(entry), '--tail-response', str(packet),
        '--source-port', str(work / 'm24-linear-port.json'), '--source-topic', manifest['source_topic'],
        '--native-record-dir', str(packet.parent / 'native-runs'),
        '--height-reference', state['result']['height_reference'],
        '--height-reference-key', state['result']['height_reference_key'],
        '--warm-factor', '1', '--height-arithmetic', 'numpy', '--background-summary',
        str(work / 'tail-background-20261128/summary.json'), '--outdir', str(out), '--phase', 'stage0']
    record = dict(source=ref(__file__), geometry_entry=ref(entry), accepted_summary=ref(summary),
        actual_command=command, disk_free_before=free, full_spectrum_preserved=True,
        scope='Only actual complete stage0; output sizes and resource observations, not global completion')
    launch = summary.parent / 'geometry-autostart.json'
    launch.open('x').write(json.dumps(record, indent=2) + '\n')
    print(json.dumps(dict(event='actual_full_spectrum_stage0_starting', command=command)), flush=True)
    started = time.monotonic()
    child = subprocess.Popen(command, cwd=repo)
    peak = 0
    while child.poll() is None:
        peak = max(peak, tree_rss(os.getpid()))
        time.sleep(.25)
    record.update(returncode=child.returncode, wall_seconds=time.monotonic()-started,
        sampled_peak_summed_tree_RSS_bytes=peak, RSS_poll_seconds=.25,
        peak_child_rusage_RSS_KiB=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        summed_RSS_counts_shared_pages_in_each_process=True,
        output_bytes=sum(p.stat().st_size for p in out.rglob('*') if p.is_file()),
        disk_free_after=shutil.disk_usage(work).free)
    if (out / 'summary.json').exists():
        record['actual_geometry_summary'] = ref(out / 'summary.json')
    terminal = summary.parent / 'geometry-stage0-resources.json'
    terminal.open('x').write(json.dumps(record, indent=2) + '\n')
    print(json.dumps(dict(event='actual_stage0_terminal', record=ref(terminal), **record)), flush=True)
    return child.returncode


if __name__ == '__main__':
    sys.exit(main())
