#!/usr/bin/env python3
"""Run the pinned original QQ source, retain only compact execution identities."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import resource
import selectors
import signal
import subprocess
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('--checkout', required=True)
parser.add_argument('--source', required=True)
parser.add_argument('--seconds', type=int, default=900)
parser.add_argument('--expected-blob', required=True)
args = parser.parse_args()
rules = {
    'README.md': '99c5ad8d06e939e6cfbbab1afdeffa5463f15f18',
    'topics/invariant-subspace-problem/README.md': '5fbd905291dd044c88d35bd9c07ac0e586ff795a',
}
source = Path(args.source)
actual_source = hashlib.sha256(source.read_bytes()).hexdigest()
source_bytes = source.read_bytes()
actual_blob = hashlib.sha1(b'blob ' + str(len(source_bytes)).encode() + b'\0' + source_bytes).hexdigest()
assert actual_blob == args.expected_blob, (actual_blob, args.expected_blob)
compile(source.read_text(), str(source), 'exec')
reads = []

def git(*argv):
    return subprocess.check_output(['git', '-C', args.checkout, *argv], text=True, timeout=180).strip()

def pull_and_read_rules():
    before = git('rev-parse', 'HEAD')
    subprocess.run(['git', '-C', args.checkout, 'pull', '--rebase', 'origin', 'main'], check=True, timeout=180)
    after = git('rev-parse', 'HEAD')
    delta = git('diff', before, after, '--', *rules)
    blobs = {p: git('hash-object', p) for p in rules}
    receipt = {
        'before': before, 'after': after,
        'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'rules_unchanged': not delta and blobs == rules,
        'rules_git_blobs': blobs,
    }
    reads.append(receipt)
    print('ISP_RULES_READ ' + json.dumps(receipt, sort_keys=True), flush=True)
    if not receipt['rules_unchanged']:
        if delta:
            print(delta, flush=True)
        raise RuntimeError('README changed: root must read exact differences before continuing')

pull_and_read_rules()
started = time.monotonic()
last_pull = started
stdout_hash = hashlib.sha256()
stdout_bytes = 0
stop_reason = None

def child_limits():
    resource.setrlimit(resource.RLIMIT_AS, (12 * 1024**3,) * 2)

child = subprocess.Popen(
    [sys.executable, '-u', str(source)], stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT, start_new_session=True, preexec_fn=child_limits,
)
selector = selectors.DefaultSelector()
selector.register(child.stdout, selectors.EVENT_READ)
while selector.get_map():
    now = time.monotonic()
    if child.poll() is None and now - started > args.seconds:
        stop_reason = 'wall_time_limit'
        os.killpg(child.pid, signal.SIGKILL)
    if child.poll() is None and now - last_pull >= 3300:
        try:
            pull_and_read_rules()
        except Exception as exc:
            stop_reason = 'rule_check_failed: ' + str(exc)
            os.killpg(child.pid, signal.SIGKILL)
        last_pull = time.monotonic()
    for key, _ in selector.select(timeout=30):
        data = os.read(key.fileobj.fileno(), 65536)
        if not data:
            selector.unregister(key.fileobj)
            continue
        stdout_hash.update(data)
        stdout_bytes += len(data)
        sys.stdout.buffer.write(data)
        sys.stdout.buffer.flush()
exit_code = child.wait()
receipt = {
    'schema': 'isp-frozen-exact-actions-execution-v1',
    'session': 'Astra-ISP-8542378f-20261127',
    'run_id': os.environ.get('GITHUB_RUN_ID'),
    'run_attempt': os.environ.get('GITHUB_RUN_ATTEMPT'),
    'source_commit': os.environ.get('ISP_PIN'),
    'source_sha256': actual_source,
    'source_git_blob': actual_blob,
    'source_exit_code': exit_code,
    'stop_reason': stop_reason,
    'elapsed_seconds': time.monotonic() - started,
    'max_child_rss_kib': resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
    'stdout_bytes': stdout_bytes,
    'stdout_sha256': stdout_hash.hexdigest(),
    'rules_reads': reads,
    'ordinary_isp_claim': False,
}
print('\nISP_EXECUTION_RECEIPT ' + json.dumps(receipt, sort_keys=True), flush=True)
raise SystemExit(0 if exit_code == 0 and stop_reason is None else 1)
