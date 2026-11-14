#!/usr/bin/env python3
"""Refine original A at the same full H, warming from an already solved RK level.

Original source geometry, physical depth, modes, parameters, Newton, line
search and tolerance remain fixed. A prior converged response supplies only
the warm state. The original worker must finish its full J and finite audit.
"""
import argparse
import datetime
import json
import os
from pathlib import Path
import subprocess
import time
from exact_20261114_fixedH_RK24 import sha,read,write


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('topic','source-topic','warm-response','out-dir'):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--steps',type=int,required=True);p.add_argument('--node-heap-mib',type=int,default=512)
    a=p.parse_args();topic=a.topic.resolve();source=a.source_topic.resolve();notes=topic/'notes';comp=topic/'computations'
    stem='2026-11-13-strong-q126-m32-tail2-actual-r1'
    old_config_path=notes/(stem+'-config.json');old_response_path=notes/(stem+'-tail-response_0003.json.gz')
    old=read(old_config_path);packet=read(old_response_path);warm_path=a.warm_response.resolve();record=read(warm_path)
    warm=record.get('response',record);H=packet['request']['height']
    allowed={'steps','auditSteps','initialCheckpoint','traceFile','iterationCheckpointFile','trialDiagnosticFile'}
    project=lambda q:{k:v for k,v in q.items()if k not in allowed}
    if not packet['response']['converged']or not warm['converged']or warm['checkpoint']['cutHeight']!=H:
        raise ValueError('Original complete H and a converged same-H warm response are required')
    if project(warm['checkpoint']['parameters'])!=project(packet['response']['checkpoint']['parameters']):
        raise ValueError('Warm physical/source parameters differ')
    previous_steps=warm['checkpoint']['parameters']['steps']
    if a.steps<=previous_steps or len(H)!=32 or old['depth']!=8 or old['modes']!=32:
        raise ValueError('Require a genuine RK refinement of original A M32/depth8')
    out=a.out_dir.resolve();out.mkdir(parents=True,exist_ok=False)
    config=dict(old);config.update(steps=a.steps,auditSteps=a.steps,initialCheckpoint=str(warm_path),
        traceFile=str(out/'trace.jsonl'),iterationCheckpointFile=str(out/'iteration.json.gz'),trialDiagnosticFile=str(out/'trials.jsonl'))
    if project(config)!=project(old):raise ValueError('Original physical parameters changed')
    request=dict(height=H,jacobian=True,audit=True)
    write(out/'config.json',config);write(out/'request.json',request)
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
        VISIBLE_FLEX_SOURCE_TOPIC=str(source),VISIBLE_FLEX_SOURCE_ROOT=str(source/'repro/source-root'),
        CLOSING_TAIL_CACHE=str(source/'repro/source-root/topics/large-amplitude-twist-flex/scripts'),
        VISIBLE_FLEX_FROZEN_LEDGER_READY=str(notes/'2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json'),
        VISIBLE_FLEX_FROZEN_STORED_READY=str(notes/'2026-11-13-strong-m28-recovered-full-audit-r1-ready.json'),
        VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND='fourier-root',VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND='tangent',VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT='8')
    command=['node','--expose-gc','--max-old-space-size='+str(a.node_heap_mib),'--max-semi-space-size=4',str(comp/'tail_frozen_worker.mjs'),str(out/'config.json')]
    hashes={str(q):sha(q)for q in [Path(__file__),Path(__file__).with_name('exact_20261114_fixedH_RK24.py'),
        old_config_path,old_response_path,warm_path,comp/'tail_frozen_worker.mjs',comp/'tail_frozen_geometry.mjs',
        comp/'tail_resumable_engine.mjs',Path(env['VISIBLE_FLEX_FROZEN_LEDGER_READY']),Path(env['VISIBLE_FLEX_FROZEN_STORED_READY'])]}
    write(out/'intent.json',dict(started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_sha256_at_start=hashes,
        command=command,baseline_steps=old['steps'],previous_steps=previous_steps,new_steps=a.steps,complete_H_unchanged=True,
        all_physical_and_source_parameters_unchanged=True,changed_keys=sorted(allowed),scope=__doc__))
    started=time.monotonic();ready=None;response=None;messages=[]
    with (out/'stderr.log').open('wb')as err:
        child=subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err,text=True,env=env,bufsize=1)
        for line in child.stdout:
            row=json.loads(line)
            if row.get('event')=='ready':
                ready=row;write(out/'ready.json.gz',row,True)
                print(json.dumps(dict(event='ready',previous_steps=previous_steps,steps=a.steps)),flush=True)
                child.stdin.write(json.dumps(request)+'\n'+json.dumps(dict(stop=True))+'\n');child.stdin.flush();child.stdin.close()
            elif 'converged'in row or 'failed'in row:
                response=row;write(out/'response.json.gz',row,True)
                print(json.dumps(dict(event='response',converged=row.get('converged'),residual=row.get('residual'),failed=row.get('failed'))),flush=True)
            else:messages.append(row)
        code=child.wait()
    success=code==0 and response is not None and response.get('converged')is True and response['residual']<config['solveTolerance'] and response.get('audit')is not None and response.get('heightJetJacobian')is not None
    result=dict(finished=True,success=success,actual_exit_code=code,seconds=time.monotonic()-started,
        baseline_steps=old['steps'],previous_steps=previous_steps,new_steps=a.steps,source_sha256_at_start=hashes,messages=messages,
        complete_H_unchanged=True,all_physical_and_source_parameters_unchanged=True,ready_received=ready is not None,response_received=response is not None,
        requested_full_DN_Jacobian=True,requested_full_finite_audit=True,output_files={q.name:sha(q)for q in out.iterdir()if q.is_file()},
        scope='Finite fixed-H RK refinement. No new accepted prefix, infinite nonlinear solution or complete-task claim.')
    if response is not None:result.update(residual=response.get('residual'),converged=response.get('converged'),audit=response.get('audit'),failed=response.get('failed'))
    write(out/'result.json',result)
    print(json.dumps(dict(event='terminal',success=success,actual_exit_code=code,seconds=result['seconds'])),flush=True)
    return 0 if success else 1


if __name__=='__main__':raise SystemExit(main())
