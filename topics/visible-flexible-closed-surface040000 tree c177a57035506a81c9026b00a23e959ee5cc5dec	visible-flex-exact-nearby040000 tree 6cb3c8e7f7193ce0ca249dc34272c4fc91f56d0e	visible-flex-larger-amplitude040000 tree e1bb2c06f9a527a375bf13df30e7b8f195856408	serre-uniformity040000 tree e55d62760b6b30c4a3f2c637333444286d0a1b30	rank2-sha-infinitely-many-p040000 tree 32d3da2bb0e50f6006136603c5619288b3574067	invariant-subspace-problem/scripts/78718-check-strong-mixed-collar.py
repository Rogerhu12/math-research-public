#!/usr/bin/env python3
"""Replay only the frozen author's 44 exact scalar checks; no PDE or geometry."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

topic = Path(__file__).resolve().parents[1]
source = topic / 'notes/2026-11-10-db6f-strong-support-mixed-curvature-collar-v1.md'
expected = '0bb11a1acad3d19f2751cbaa554a0e727aaed192559e5b709281da0e78fb3955'
raw = source.read_bytes()
if hashlib.sha256(raw).hexdigest() != expected:
    raise SystemExit('Frozen author source differs')
blocks = re.findall(r'```javascript\n(.*?)\n```', raw.decode(), re.S)
if len(blocks) != 1:
    raise SystemExit('Expected one frozen JavaScript block')
js = blocks[0]
runner = (
    "const fs=require('fs'),vm=require('vm');"
    "const r=vm.runInNewContext(fs.readFileSync(0,'utf8'));"
    "process.stdout.write(JSON.stringify(r));"
)
run = subprocess.run(['node', '-e', runner], input=js, text=True,
                     capture_output=True, check=True)
result = json.loads(run.stdout)
if result['pass'] != 44 or result['fail'] != 0:
    raise SystemExit('Unexpected scalar result')
for key in ('pde_runs', 'solver_runs', 'geometry_arrays', 'terminal_math_runs'):
    if result[key] != 0:
        raise SystemExit('Unexpected mathematical execution claim')
report = {
    'status': 'PASS_FROZEN_44_SCALAR_GATES_ONLY',
    'observer': 'Astra-visible-flex-78718bd0/root',
    'source_markdown_sha256': expected,
    'extracted_javascript_sha256': hashlib.sha256(js.encode()).hexdigest(),
    'runner_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'node_exit_code': run.returncode,
    'result': result,
    'scope': 'Exact rational comparisons only; no PDE, numerical cap, mesh, or G5.'
}
out = topic / 'notes/2026-11-10-78718-strong-mixed-collar-scalar-replay.json'
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'status': report['status'], 'pass': result['pass'],
                  'node_exit_code': run.returncode,
                  'report_sha256': hashlib.sha256(out.read_bytes()).hexdigest()}))
