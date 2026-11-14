#!/usr/bin/env python3
"""Run an explicitly bound command; keep input bindings immutable, finalize separately."""
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

binding=Path(sys.argv[1])
data=json.loads(binding.read_text())
for item in data['bound_files']:
    p=Path(item['path'])
    if hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:
        raise ValueError('Bound input changed: '+str(p))
out=Path(data['out_prefix'])
repro=out.with_name(out.name+'-reproduction.json')
if repro.exists():raise FileExistsError(repro)
start=time.monotonic()
with out.with_name(out.name+'-run.log').open('x') as log:
    run=subprocess.run(data['command'],stdout=log,stderr=subprocess.STDOUT)
result=dict(data,input_bindings=str(binding),
            input_bindings_sha256=hashlib.sha256(binding.read_bytes()).hexdigest(),
            launcher_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            exit_code=run.returncode,seconds=time.monotonic()-start)
summary=out.with_name(out.name+'-summary.json')
if summary.is_file():
    values=json.loads(summary.read_text())
    result.update(mathematical_success=values.get('solver_success'),error=values.get('error'))
repro.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result.get(k) for k in ['exit_code','seconds','mathematical_success','error']}),flush=True)
raise SystemExit(run.returncode)
