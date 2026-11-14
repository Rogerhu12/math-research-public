#!/usr/bin/env python3
"""CI driver for refined-tail finite closed assembly and all-phase pair samples.

The caller prepares the pinned source tree. Without --complete this rebuilds
the original accepted-A 577/2305 node readout in RUNNER_TEMP. A later actual
candidate can supply its own bound readout/config/checkpoint. Only meshes,
compact finite reports, hashes and lifecycle records are saved in OUT_DIR.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def write(path, obj):
    with Path(path).open('x') as f:
        json.dump(obj, f, indent=2, allow_nan=False)
        f.write('\n')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo-root',type=Path,default=Path(__file__).resolve().parents[3])
    p.add_argument('--source-topic',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    for name in ('complete','config','checkpoint','port'):
        p.add_argument('--'+name,type=Path)
    p.add_argument('--steps',type=int,default=12)
    p.add_argument('--angular',type=int,default=96)
    p.add_argument('--phase-samples',type=int,default=9)
    p.add_argument('--marker-k',type=float,default=1/160)
    p.add_argument('--node-heap-mib',type=int,default=384)
    a=p.parse_args()
    repo=a.repo_root.resolve();topic=repo/'topics/visible-flex-larger-amplitude'
    comp=topic/'computations';notes=topic/'notes';out=a.out.resolve()
    out.mkdir(parents=True,exist_ok=True)
    lifecycle=out/'exact-closed-lifecycle.jsonl'
    if lifecycle.exists():
        raise ValueError('Fresh CI output required')
    defaults=dict(config=notes/'2026-11-13-strong-q126-m32-tail2-actual-r1-config.json',
        checkpoint=notes/'2026-11-13-strong-q126-m32-tail2-actual-r1.json.gz',
        port=comp/'alternative-neck-provider-smallcut30-port32-r2048.json')
    if a.complete is None and any(getattr(a,key) is not None for key in defaults):
        raise ValueError('Automatic A readout cannot be transplanted onto a different candidate')
    for key,value in defaults.items():
        setattr(a,key,(getattr(a,key) or value).resolve())
    a.source_topic=a.source_topic.resolve()
    work=Path(tempfile.mkdtemp(prefix='visible-flex-exact-closed-',dir=os.environ.get('RUNNER_TEMP')))
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    own_hash=sha(__file__);started=time.monotonic();commands=[];success=False;failure=None
    sources=[Path(__file__).resolve(),comp/'exact_20261114_refined_tail_adapter.py',
        comp/'exact_20261114_refined_closed_assembly.py',comp/'exact_20261114_closed_background.mjs',
        comp/'geometry_20261114_actual_A_tail_allnodes_firstjet_readout.mjs',
        comp/'exact_20261114_radial_perturbation_readout.mjs',comp/'geometric-closed-assembly.py',
        comp/'geometric-checkpoint-core-pullback.py',comp/'root_phase_reach.py']
    source_hashes={str(path.relative_to(repo)):sha(path) for path in sources}
    write(out/'exact-closed-intent.json',dict(schema='refined-tail-closed-CI-intent-v1',started_utc=utc(),
        source_sha256_at_start=source_hashes,working_directory=str(work),
        steps=a.steps,mesh_angular=a.angular,phase_samples=a.phase_samples,marker_k=a.marker_k,
        fixed_cut_correction_width=.01,complete_input=str(a.complete) if a.complete else None,
        inputs={key:dict(file=str(getattr(a,key)),sha256=sha(getattr(a,key))) for key in defaults},
        scope=__doc__))

    def run(label, argv):
        row=dict(label=label,command=[str(x) for x in argv],started_utc=utc())
        t=time.monotonic()
        with lifecycle.open('a') as f:
            f.write(json.dumps(dict(event='start',**row))+'\n')
        print(json.dumps(dict(event='start',label=label)),flush=True)
        result=subprocess.run(row['command'],cwd=repo,env=env,check=False)
        row.update(finished_utc=utc(),actual_exit_code=result.returncode,wall_seconds=time.monotonic()-t)
        commands.append(row)
        with lifecycle.open('a') as f:
            f.write(json.dumps(dict(event='exit',**row))+'\n')
        print(json.dumps(dict(event='exit',label=label,actual_exit_code=result.returncode,seconds=row['wall_seconds'])),flush=True)
        if result.returncode:
            raise RuntimeError(label+' exited '+str(result.returncode))

    try:
        node=['node','--expose-gc','--max-old-space-size='+str(a.node_heap_mib),'--max-semi-space-size=4']
        if a.complete is None:
            original=work/'original-nodes'
            run('original-A-577-readout',node+[comp/'geometry_20261114_actual_A_tail_allnodes_firstjet_readout.mjs',
                '--repo-root',repo,'--source-topic',a.source_topic,'--first-node','0','--last-node-exclusive','577','--out-dir',original])
            if not (original/'complete.json').is_file():
                raise RuntimeError('Original producer did not create its declared complete.json')
            refined=work/'refined-nodes'
            run('original-A-2305-readout',node+[comp/'exact_20261114_radial_perturbation_readout.mjs',
                '--repo-root',repo,'--source-topic',a.source_topic,'--complete',original/'complete.json',
                '--out-dir',refined,'--steps',a.steps])
            a.complete=refined/'complete-4.json'
            write(out/'exact-closed-readout-result.json',json.loads((refined/'result.json').read_text()))
        else:
            a.complete=a.complete.resolve()
        prefix=out/'refined-A-closed'
        shared=['--source-topic',a.source_topic,'--checkpoint',a.checkpoint,'--port',a.port,
            '--config',a.config,'--complete',a.complete,'--out-prefix',prefix]
        run('finite-closed-plan',[sys.executable,'-u',comp/'exact_20261114_refined_closed_assembly.py','plan']+shared+[
            '--angular',a.angular,'--phase-samples',a.phase_samples,'--marker-k',a.marker_k,'--cut-correction-width','.01'])
        plan=Path(str(prefix)+'-plan.json');background=out/'refined-A-closed-background.json'
        run('unchanged-source-background',node+[comp/'exact_20261114_closed_background.mjs',
            '--repo-root',repo,'--source-topic',a.source_topic,'--config',a.config,'--plan',plan,'--out',background])
        run('finite-closed-render-and-all-phase-samples',[
            sys.executable,'-u',comp/'exact_20261114_refined_closed_assembly.py','render']+shared+[
            '--plan',plan,'--heights',background])
        report=json.loads(Path(str(prefix)+'-assembly.json').read_text())
        if not report['finished']:
            raise RuntimeError('Assembly has no finished result')
        success=True
    except Exception as error:
        failure=str(error)
    write(out/'exact-closed-terminal.json',dict(schema='refined-tail-closed-CI-terminal-v1',finished=True,
        success=success,failure=failure,finished_utc=utc(),wall_seconds=time.monotonic()-started,
        source_sha256_at_start=source_hashes,driver_sha256_at_start=own_hash,commands=commands,
        large_sidecars_in_runner_temp=True,task_completed=False))
    print(json.dumps(dict(event='terminal',success=success,failure=failure,seconds=time.monotonic()-started)),flush=True)
    return 0 if success else 1


if __name__=='__main__':
    raise SystemExit(main())
