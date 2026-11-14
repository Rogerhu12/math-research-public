#!/usr/bin/env python3
"""Continue a running same-H RK solve into actual nodes, errors and closed meshes.

The solver's real finished/success record is required before reading its new
states. Large nodes remain in the requested scratch work directory. Every
command has a start/actual-exit lifecycle entry. No repository or network
operation is performed.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def write(path,data):
    with Path(path).open('x')as f:
        json.dump(data,f,indent=2,allow_nan=False);f.write('\n')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('repo-root','source-topic','solve-dir','baseline-readout','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--wait-for-solve',action='store_true')
    p.add_argument('--node-heap-mib',type=int,default=512)
    a=p.parse_args();repo=a.repo_root.resolve();topic=repo/'topics/visible-flex-larger-amplitude'
    comp=topic/'computations';notes=topic/'notes';out=a.out.resolve();out.mkdir(parents=True,exist_ok=False)
    stem='2026-11-13-strong-q126-m32-tail2-actual-r1'
    checkpoint=notes/(stem+'.json.gz');baseline_config=notes/(stem+'-config.json')
    baseline_response=notes/(stem+'-tail-response_0003.json.gz');port=comp/'alternative-neck-provider-smallcut30-port32-r2048.json'
    sources=[Path(__file__),comp/'exact_20261114_resolved_radial_readout.mjs',
        comp/'exact_20261114_resolved_common_grid.py',comp/'exact_20261114_common_grid_refinement.py',
        comp/'exact_20261114_resolved_closed_assembly.py',comp/'exact_20261114_closed_display_adapter.py',
        comp/'exact_20261114_refined_closed_assembly.py',comp/'exact_20261114_refined_tail_adapter.py',
        comp/'exact_20261114_closed_background.mjs',comp/'exact_20261114_closed_mesh_summary.py']
    source_hashes={str(path.resolve()):sha(path)for path in sources}
    write(out/'intent.json',dict(schema='resolved-tail-local-pipeline-intent-v1',started_utc=utc(),
        argv=sys.argv,source_sha256_at_start=source_hashes,solve_dir=str(a.solve_dir.resolve()),
        baseline_readout=str(a.baseline_readout.resolve()),levels=[1,2,4,8],angles=1024,
        fixed_cut_width=.01,phase_samples=9,large_sidecars_in_scratch=True))
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    started=time.monotonic();commands=[];success=False;failure=None
    lifecycle=out/'lifecycle.jsonl'
    def event(row):
        with lifecycle.open('a')as f:f.write(json.dumps(row)+'\n')
        print(json.dumps(row),flush=True)
    def run(label,argv):
        command=list(map(str,argv));begin=time.monotonic()
        row=dict(label=label,command=command,started_utc=utc())
        event(dict(event='start',**row))
        with (out/(label+'.log')).open('wb')as log:
            code=subprocess.run(command,cwd=repo,env=env,stdout=log,stderr=subprocess.STDOUT).returncode
        row.update(actual_exit_code=code,finished_utc=utc(),seconds=time.monotonic()-begin)
        commands.append(row);event(dict(event='exit',**row))
        if code:raise RuntimeError(label+' exited '+str(code))
    try:
        result_path=a.solve_dir/'result.json'
        if a.wait_for_solve:
            event(dict(event='waiting_for_actual_solver_terminal',file=str(result_path)))
            while not result_path.is_file():time.sleep(5)
        solved=json.loads(result_path.read_text())
        if not solved.get('finished')or not solved.get('success')or solved.get('actual_exit_code')!=0:
            raise RuntimeError('The original fixed-H solver did not finish successfully')
        config=a.solve_dir/'config.json';response=a.solve_dir/'response.json.gz'
        write(out/'solver-terminal.json',dict(result=solved,response_sha256=sha(response),config_sha256=sha(config)))
        node=['node','--expose-gc','--max-old-space-size='+str(a.node_heap_mib),'--max-semi-space-size=4']
        readout=out/'readout'
        run('resolved-node-readout',node+[comp/'exact_20261114_resolved_radial_readout.mjs',
            '--repo-root',repo,'--source-topic',a.source_topic,'--config',config,'--response',response,
            '--baseline-config',baseline_config,'--baseline-response',baseline_response,
            '--levels','1,2,4,8','--out-dir',readout])
        shared=['--source-topic',a.source_topic,'--checkpoint',checkpoint,'--port',port,'--angles','1024']
        common=[sys.executable,'-u',comp/'exact_20261114_resolved_common_grid.py']
        args=[]
        for level in (1,2,4):args+=['--complete',readout/('complete-'+str(level)+'.json')]
        run('common-124-and-original4',common+args+['--complete',a.baseline_readout,
            '--labels','resolved24-f1,resolved24-f2,resolved24-f4,original12-f4',
            '--background',readout/'background-4.json','--out',out/'common-124-and-original4.json']+shared)
        run('common-4-to-8',common+['--complete',readout/'complete-4.json','--complete',readout/'complete-8.json',
            '--labels','resolved24-f4,resolved24-f8','--background',readout/'background-8.json',
            '--out',out/'common-4-to-8.json']+shared)
        prefix=out/'closed'/'refined-A-closed';prefix.parent.mkdir()
        assembly=[sys.executable,'-u',comp/'exact_20261114_resolved_closed_assembly.py']
        args=['--source-topic',a.source_topic,'--checkpoint',checkpoint,'--port',port,
            '--config',config,'--complete',readout/'complete-8.json','--out-prefix',prefix]
        run('closed-plan',assembly+['plan']+args+['--angular','96','--phase-samples','9','--cut-correction-width','.01'])
        plan=Path(str(prefix)+'-plan.json');background=out/'closed'/'background.json'
        run('closed-source-background',node+[comp/'exact_20261114_closed_background.mjs',
            '--repo-root',repo,'--source-topic',a.source_topic,'--config',config,'--plan',plan,'--out',background])
        run('closed-render-all-phase',assembly+['render']+args+['--plan',plan,'--heights',background])
        run('closed-mesh-summary',[sys.executable,'-u',comp/'exact_20261114_closed_mesh_summary.py',
            '--directory',prefix.parent,'--out',out/'closed'/'summary.json'])
        success=True
    except Exception as error:
        failure=str(error)
    write(out/'terminal.json',dict(schema='resolved-tail-local-pipeline-terminal-v1',finished=True,
        success=success,failure=failure,finished_utc=utc(),seconds=time.monotonic()-started,
        source_sha256_at_start=source_hashes,commands=commands,task_completed=False))
    event(dict(event='terminal',success=success,failure=failure))
    return 0 if success else 1


if __name__=='__main__':raise SystemExit(main())
