#!/usr/bin/env python3
"""First-time original-cell8..1 material enclosures, one immutable producer per cell.

Every child uses the unchanged producer and existing R26 parent radii. No ODE
or new radius quadrature is requested. Per-cell actual wait4 records are kept.
Large regenerable material groups remain scratch; small manifests and hashes
are sufficient to reproduce their exact mathematical payload.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

base = Path(__file__).resolve().parent
inputs = base/'outer-continuation-inputs'
producer = inputs/'sources/tail_outer_positive_moment_groups.py'
ready = inputs/'2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json'
radius = inputs/'2026-11-12-root-real-outer-radius-v4-recovered-full.json'
pins = [(producer,'a0575cf86ec70ce3b2f5455b81403a53647c2a574cb66661bf62b24e17278405'),
        (ready,'563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6'),
        (radius,'28d491b998174029a80daf41e9365de6ab2c54757419de7b64f54445047b717f')]
for path, expected in pins:
    if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
        raise ValueError('Frozen source or original mathematical input changed')
result = base/'outer8to1-material-r1-driver.json'
if result.exists():
    raise FileExistsError('Fresh driver output required')
records=[]
started=time.monotonic()
for cell in range(8,0,-1):
    prefix=base/f'outer-cell{cell}-material-r1'
    resource=prefix.with_name(prefix.name+'-resource.json')
    manifest=prefix.with_name(prefix.name+'-manifest.json')
    if resource.exists() or manifest.exists():
        raise FileExistsError('Do not repeat or overwrite an existing cell run')
    command=[sys.executable,str(base/'strong_resource_run.py'),'--out',str(resource),'--',
        sys.executable,str(producer),'--ready',str(ready),'--radius-ledger',str(radius),
        '--cell',str(cell),'--out-prefix',str(prefix),'--precision','256','--rss-limit-mib','96']
    print(json.dumps({'event':'first_time_original_cell','cell':cell}),flush=True)
    proc=subprocess.run(command,check=False)
    if not resource.exists():
        raise RuntimeError('Actual child resource record missing')
    r=json.loads(resource.read_text())
    rec={'cell':cell,'returncode':proc.returncode,'resource':str(resource),
        'resource_sha256':hashlib.sha256(resource.read_bytes()).hexdigest()}
    records.append(rec)
    if proc.returncode!=0 or r['exitcode']!=0 or r['termination_signal'] is not None:
        result.write_text(json.dumps({'status':'actual child failure retained','records':records},indent=2)+'\n')
        raise RuntimeError('Original material child failed; no weakened rerun')
    m=json.loads(manifest.read_text())
    if not all(m['checks'].values()) or m['cell']!=cell:
        raise ArithmeticError('An original cell material gate failed')
    rec.update(manifest=str(manifest),manifest_sha256=hashlib.sha256(manifest.read_bytes()).hexdigest(),
        panels=m['panels'],mathematical_payload_sha256=m['exact_nondisplay_payload_sha256'],
        wall_seconds=r['wall_seconds'],peak_rss_kib=r['peak_rss_kib'])
    print(json.dumps({'event':'complete_original_cell','cell':cell,'panels':m['panels'],
                     'elapsed_seconds':time.monotonic()-started}),flush=True)
result.write_text(json.dumps({'schema':'first-time-original-outer8to1-material-v1',
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'original_ready_sha256':pins[1][1],'original_radius_sha256':pins[2][1],
    'all_cells':[8,7,6,5,4,3,2,1],'records':records,'all_actual_exit_zero':True,
    'new_ODE_or_radius_quadrature':0,'elapsed_seconds':time.monotonic()-started},indent=2)+'\n')
