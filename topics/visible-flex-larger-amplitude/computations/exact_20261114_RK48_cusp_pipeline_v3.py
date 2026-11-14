#!/usr/bin/env python3
"""Finish true RK48/16 readout with original source knots retained.

The regional recorder keeps the original complete six-jet values and adds
patch/outside-patch maxima. Two independent comparisons separate the RK24->48
change at eight subdivisions from the RK48 eight->sixteen spatial change.
The same complete H, source metric, original prefix and width-.01 cut patch
are retained. Source knots are read separately at each regular level: some
coincide with odd sixteenths and must survive coarsening to eighths. Nothing is uploaded or committed by this local/CI driver.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import threading
import time
import numpy as np
from exact_20261114_compare_depth import read,compare


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(path,data):
    with Path(path).open('x')as f:json.dump(data,f,indent=2,allow_nan=False);f.write('\n')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('repo-root','source-topic','solve-dir','old-solve-dir','old-readout','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--wait-until-file',type=Path)
    p.add_argument('--comparison-processes',type=int,choices=[1,2],default=2)
    a=p.parse_args();repo=a.repo_root.resolve();topic=repo/'topics/visible-flex-larger-amplitude';comp=topic/'computations';notes=topic/'notes'
    out=a.out.resolve();out.mkdir(parents=True,exist_ok=False)
    sources=[Path(__file__),comp/'exact_20261114_resolved_radial_readout.mjs',comp/'exact_20261114_cusp_point_readout.mjs',
        comp/'exact_20261114_source_partition_background.mjs',comp/'exact_20261114_regional_common_grid.py',
        comp/'exact_20261114_common_grid_refinement.py',comp/'exact_20261114_refined_tail_adapter.py',
        comp/'exact_20261114_resolved_closed_assembly.py',comp/'exact_20261114_closed_display_adapter.py',
        comp/'exact_20261114_refined_closed_assembly.py',comp/'exact_20261114_closed_background.mjs',
        comp/'exact_20261114_closed_mesh_summary.py',comp/'exact_20261114_finite_collar_bound.py',comp/'exact_20261114_compare_RK.py']
    source_hashes={str(q):sha(q)for q in sources};started=time.monotonic();commands=[];lock=threading.Lock();lifecycle=out/'lifecycle.jsonl'
    write(out/'intent.json',dict(started_utc=utc(),argv=sys.argv,source_sha256_at_start=source_hashes,
        comparison_processes=a.comparison_processes,source_knots_retained=True,fixed_cut_width=.01,
        wait_until_file_is_only_a_resource_barrier=True,scope=__doc__))
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    def event(data):
        with lock:
            with lifecycle.open('a')as f:f.write(json.dumps(data)+'\n')
            print(json.dumps(data),flush=True)
    def run(label,argv):
        command=list(map(str,argv));row=dict(label=label,command=command,started_utc=utc());begin=time.monotonic()
        event(dict(event='start',**row))
        with (out/(label+'.log')).open('wb')as log:
            code=subprocess.run(command,cwd=repo,env=env,stdout=log,stderr=subprocess.STDOUT).returncode
        row.update(actual_exit_code=code,finished_utc=utc(),seconds=time.monotonic()-begin)
        with lock:commands.append(row)
        event(dict(event='exit',**row))
        if code:raise RuntimeError(label+' exited '+str(code))
    success=False;failure=None
    try:
        waits=[a.solve_dir/'result.json']+([a.wait_until_file]if a.wait_until_file else [])
        event(dict(event='waiting',paths=list(map(str,waits))))
        while not all(q.is_file()for q in waits):time.sleep(5)
        solved=read(a.solve_dir/'result.json');old_solved=read(a.old_solve_dir/'result.json')
        if any(not q.get('success')or q.get('actual_exit_code')!=0 for q in (solved,old_solved)):
            raise ValueError('Both real RK solves must have successful terminal records')
        config=a.solve_dir/'config.json';response=a.solve_dir/'response.json.gz'
        old_config=a.old_solve_dir/'config.json';old_response=a.old_solve_dir/'response.json.gz'
        if read(config)['steps']!=48 or read(old_config)['steps']!=24:raise ValueError('This concrete comparison is RK24 to48')
        write(out/'completed-solver-inputs.json',dict(new=solved,old=old_solved,
            response_sha256={str(q):sha(q)for q in (config,response,old_config,old_response)}))
        stem='2026-11-13-strong-q126-m32-tail2-actual-r1';checkpoint=notes/(stem+'.json.gz')
        baseline_config=notes/(stem+'-config.json');baseline_response=notes/(stem+'-tail-response_0003.json.gz')
        port=comp/'alternative-neck-provider-smallcut30-port32-r2048.json'
        run('compare-RK12-to48',[sys.executable,'-u',comp/'exact_20261114_compare_RK.py','--topic',topic,
            '--new-dir',a.solve_dir,'--out',out/'compare-RK12-to48.json'])
        old,new=read(old_response),read(response);M=read(config)['modes']
        if old['checkpoint']['cutHeight']!=new['checkpoint']['cutHeight']:raise ValueError('Adjacent RK complete H differs')
        oldJ=np.asarray(old['heightJetJacobian']).reshape(3*M+2,M);newJ=np.asarray(new['heightJetJacobian']).reshape(3*M+2,M)
        blocks={'slope':slice(0,M),'second':slice(M,2*M),'meanSlopeCorrection':slice(2*M,2*M+1),
                'meanSecondCorrection':slice(2*M+1,2*M+2),'height':slice(2*M+2,3*M+2)}
        write(out/'compare-RK24-to48.json',dict(finished=True,old_steps=24,new_steps=48,
            source_sha256_at_start=source_hashes[str(Path(__file__))],input_sha256={str(q):sha(q)for q in(old_response,response)},
            complete_H_exactly_equal=True,physical_identity_via_original_baseline=True,
            jets={k:compare(old['jets'][k],new['jets'][k])for k in('height','slope','second')},
            means={k:compare([old['jets'][k]],[new['jets'][k]])for k in('meanSlope','meanSecond','meanSlopeCorrection','meanSecondCorrection')},
            Jacobian_blocks={k:compare(oldJ[sl],newJ[sl])for k,sl in blocks.items()},
            canonical_states=compare(old['checkpoint']['states'],new['checkpoint']['states']),
            scope='Two completed finite fixed-H RK solves; no new accepted prefix or infinite nonlinear solution.'))
        node=['node','--expose-gc','--max-old-space-size=384','--max-semi-space-size=4'];regular=out/'regular48'
        run('RK48-real-sixteenth-nodes',node+[comp/'exact_20261114_resolved_radial_readout.mjs','--repo-root',repo,
            '--source-topic',a.source_topic,'--config',config,'--response',response,'--baseline-config',baseline_config,
            '--baseline-response',baseline_response,'--levels','1,8,16','--out-dir',regular])
        cusp24=out/'cusp24';cusp48=out/'cusp48-sixteen';cusp48eight=out/'cusp48-eight'
        for label,conf,resp,base,bg,dest in [
            ('RK24-source-knots',old_config,old_response,a.old_readout/'complete-8.json',a.old_readout/'background-8.json',cusp24),
            ('RK48-source-knots-eight',config,response,regular/'complete-8.json',regular/'background-8.json',cusp48eight),
            ('RK48-source-knots-sixteen',config,response,regular/'complete-16.json',regular/'background-16.json',cusp48)]:
            run(label,node+[comp/'exact_20261114_cusp_point_readout.mjs','--repo-root',repo,'--source-topic',a.source_topic,
                '--config',conf,'--response',resp,'--complete',base,'--background',bg,'--stages','all','--out-dir',dest])
        for label,conf,complete,bg in [
            ('background24-eight',old_config,cusp24/'complete.json',cusp24/'background-8.json'),
            ('background48-eight',config,cusp48eight/'complete.json',cusp48eight/'background-8.json'),
            ('background48-sixteen',config,cusp48/'complete.json',cusp48/'background-16.json')]:
            run(label,node+[comp/'exact_20261114_source_partition_background.mjs','--repo-root',repo,
                '--source-topic',a.source_topic,'--config',conf,'--complete',complete,'--out',bg])
        common=[sys.executable,'-u',comp/'exact_20261114_regional_common_grid.py']
        shared=['--source-topic',a.source_topic,'--checkpoint',checkpoint,'--port',port,'--angles','1024']
        comparisons=[('common-RK24-to48-eight',common+['--complete',cusp24/'complete.json','--complete',cusp48eight/'complete.json',
            '--labels','rk24-f8-cusp,rk48-f8-cusp','--background',cusp48eight/'background-8.json',
            '--out',out/'common-RK24-to48-eight.json']+shared),
            ('common-RK48-eight-to-sixteen',common+['--complete',cusp48eight/'complete.json','--complete',cusp48/'complete.json',
            '--labels','rk48-f8-cusp,rk48-f16-cusp','--background',cusp48/'background-16.json',
            '--out',out/'common-RK48-eight-to-sixteen.json']+shared)]
        with ThreadPoolExecutor(max_workers=a.comparison_processes)as pool:
            jobs=[pool.submit(run,label,argv)for label,argv in comparisons]
            for job in jobs:job.result()
        run('finite-collar-bound',[sys.executable,'-u',comp/'exact_20261114_finite_collar_bound.py',
            '--complete',cusp48/'complete.json','--out',out/'finite-collar-bound.json'])
        prefix=out/'closed'/'refined-A-closed';prefix.parent.mkdir()
        args=['--source-topic',a.source_topic,'--checkpoint',checkpoint,'--port',port,'--config',config,
            '--complete',cusp48/'complete.json','--out-prefix',prefix]
        assembly=[sys.executable,'-u',comp/'exact_20261114_resolved_closed_assembly.py']
        run('closed-plan',assembly+['plan']+args+['--angular','96','--phase-samples','9','--cut-correction-width','.01'])
        plan=Path(str(prefix)+'-plan.json');background=prefix.parent/'background.json'
        run('closed-source-background',node+[comp/'exact_20261114_closed_background.mjs','--repo-root',repo,
            '--source-topic',a.source_topic,'--config',config,'--plan',plan,'--out',background])
        run('closed-render-all-phase',assembly+['render']+args+['--plan',plan,'--heights',background])
        run('closed-mesh-summary',[sys.executable,'-u',comp/'exact_20261114_closed_mesh_summary.py',
            '--directory',prefix.parent,'--out',prefix.parent/'summary.json'])
        success=True
    except Exception as error:failure=str(error)
    write(out/'terminal.json',dict(finished=True,success=success,failure=failure,finished_utc=utc(),
        seconds=time.monotonic()-started,source_sha256_at_start=source_hashes,commands=commands,task_completed=False))
    event(dict(event='terminal',success=success,failure=failure));return 0 if success else 1


if __name__=='__main__':raise SystemExit(main())
