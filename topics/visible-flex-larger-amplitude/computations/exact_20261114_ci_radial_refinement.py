#!/usr/bin/env python3
"""Run the fixed-A tail reconstruction chain on the public CI runner.

The caller prepares source-dependencies.json's 91 pinned files. This chain
needs the committed tail checkpoint and saved mean/flow sidecars; it does
not need the prefix solve's external raw pickle. Large Cartesian node
sidecars remain under RUNNER_TEMP. Only finite reports, hashes, lifecycle
records, and actual exit codes are copied to --out.
"""
from __future__ import annotations
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)


def utc():return dt.datetime.now(dt.timezone.utc).isoformat()


def write(path,value):
    with Path(path).open('x')as f:json.dump(value,f,indent=2,allow_nan=False);f.write('\n')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo-root',type=Path,default=Path(__file__).resolve().parents[3])
    p.add_argument('--source-topic',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--steps',type=int,default=24)
    p.add_argument('--angles',type=int,default=1024)
    p.add_argument('--horizontal-rr',choices=['nonuniform-difference','target-metric'],default='nonuniform-difference')
    p.add_argument('--node-heap-mib',type=int,default=384)
    a=p.parse_args()
    repo=a.repo_root.resolve();source=a.source_topic.resolve();out=a.out.resolve()
    topic=repo/'topics/visible-flex-larger-amplitude';comp=topic/'computations';notes=topic/'notes'
    out.mkdir(parents=True,exist_ok=True)
    if (out/'exact-radial-lifecycle.jsonl').exists():raise ValueError('Fresh CI result prefix required')
    if a.steps<12 or a.steps%4 or a.angles<512 or a.angles%2:raise ValueError('Invalid fixed-family refinement')
    origin=read(source/'source-origin.json')
    if origin['source_revision']!='869436630c99aa5a68afb55bd8877c826034d117':raise ValueError('Wrong source revision')
    work=Path(tempfile.mkdtemp(prefix='visible-flex-exact-radial-',dir=os.environ.get('RUNNER_TEMP')))
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    start=time.monotonic();records=[]
    paths=[Path(__file__).resolve(),comp/'source-dependencies.json',
        comp/'geometry_20261114_actual_A_tail_allnodes_firstjet_readout.mjs',
        comp/'exact_20261114_radial_perturbation_readout.mjs',
        comp/'exact_20261114_background_preserving_metric.py',
        notes/'2026-11-13-strong-q126-m32-tail2-actual-r1-config.json',
        notes/'2026-11-13-strong-q126-m32-tail2-actual-r1-tail-response_0003.json.gz']
    source_hashes={str(q.relative_to(repo)):sha(q) for q in paths}
    write(out/'exact-radial-intent.json',dict(schema='fixed-A-radial-CI-intent-v1',started_utc=utc(),
        steps=a.steps,angles=a.angles,horizontal_rr=a.horizontal_rr,levels=[1,2,4],source_topic=str(source),source_origin=origin,
        source_sha256=source_hashes,working_directory=str(work),
        python=sys.version,numpy=importlib.metadata.version('numpy'),
        scope=__doc__,large_node_sidecars_retained_in_runner_temp=True))

    def run(label,argv):
        t=time.monotonic();row=dict(label=label,command=[str(q)for q in argv],started_utc=utc())
        with (out/'exact-radial-lifecycle.jsonl').open('a')as f:f.write(json.dumps(dict(event='start',**row))+'\n')
        print(json.dumps(dict(event='start',label=label,started_utc=row['started_utc'])),flush=True)
        completed=subprocess.run(row['command'],cwd=topic,env=env,check=False)
        row.update(finished_utc=utc(),actual_exit_code=completed.returncode,wall_seconds=time.monotonic()-t)
        records.append(row)
        with (out/'exact-radial-lifecycle.jsonl').open('a')as f:f.write(json.dumps(dict(event='exit',**row))+'\n')
        print(json.dumps(dict(event='exit',label=label,actual_exit_code=completed.returncode,wall_seconds=row['wall_seconds'])),flush=True)
        if completed.returncode:raise RuntimeError(label+' exited '+str(completed.returncode))

    node=['node','--expose-gc','--max-old-space-size='+str(a.node_heap_mib),'--max-semi-space-size=4']
    failure=None;comparisons={};status=False
    try:
        original_dir=work/'original-nodes'
        run('original-577-node-readout',node+[comp/'geometry_20261114_actual_A_tail_allnodes_firstjet_readout.mjs',
            '--repo-root',repo,'--source-topic',source,'--first-node','0','--last-node-exclusive','577','--out-dir',original_dir])
        # The readout writes complete.json directly under its --out-dir. Verify
        # the actual produced path and contents; no hard-coded extra /nodes.
        original_complete=original_dir/'complete.json'
        if not original_complete.is_file():raise RuntimeError('Original readout did not produce complete.json at its declared output directory')
        original=read(original_complete)
        if original['completedNodes']!=577 or not original['whole_577_node_readout_complete']:raise RuntimeError('Incomplete original node readout')
        write(out/'exact-original-node-summary.json',{k:original[k]for k in
            ['schema','finished','source_sha256','original_fullflow_identity_sha256','completedNodes','angular','summary','evaluations','seconds']if k in original})
        refined=work/('steps'+str(a.steps))
        run('actual-RK-interior-readout',node+[comp/'exact_20261114_radial_perturbation_readout.mjs',
            '--repo-root',repo,'--source-topic',source,'--complete',original_complete,'--out-dir',refined,'--steps',str(a.steps)])
        readout=read(refined/'result.json')
        if not readout['finished'] or readout['steps']!=a.steps:raise RuntimeError('Incomplete refinement readout')
        shutil.copyfile(refined/'result.json',out/'exact-radial-readout-result.json')
        for level in [1,2,4]:
            complete=refined/('complete-'+str(level)+'.json');background=refined/('background-'+str(level)+'.json')
            result=out/('exact-radial-metric-'+str(level)+'.json')
            run('metric-radial-'+str(level),[sys.executable,'-u',comp/'exact_20261114_background_preserving_metric.py',
                '--complete',complete,'--background',background,'--variants','correct_background_quadrature',
                '--angles',str(a.angles),'--horizontal-rr',a.horizontal_rr,'--out',result])
            v=read(result)
            comparisons[str(level)]=dict(nodes=v['nodes'],angular_evaluation=v['angular_evaluation'],
                radial_samples=v['radial_samples'],metric_report_sha256=sha(result),
                maxima=v['variants']['correct_background_quadrature']['maxima'],
                witnesses=v['variants']['correct_background_quadrature']['witnesses'])
        status=True
    except Exception as error:
        failure=str(error)
    final=dict(schema='fixed-A-radial-CI-terminal-record-v1',finished=True,success=status,
        finished_utc=utc(),wall_seconds=time.monotonic()-start,steps=a.steps,angles=a.angles,horizontal_rr=a.horizontal_rr,
        commands=records,source_sha256=source_hashes,refinement=comparisons,failure=failure,
        current_driver_sha256=sha(__file__),working_directory=str(work),
        retained_large_sidecars=False,
        limitations=['This is a finite reconstruction and sampled same-g refinement, not an exact or closed-surface theorem.',
            'Fixed accepted shooting endpoint states are retained; recorded RK endpoint defects are not hidden.',
            'Large Cartesian sidecars are reproducible from these pinned committed inputs and the recorded commands.'])
    write(out/'exact-radial-terminal.json',final)
    print(json.dumps(dict(event='terminal',success=status,failure=failure,seconds=final['wall_seconds'],refinement=comparisons)),flush=True)
    return 0 if status else 1


if __name__=='__main__':raise SystemExit(main())
