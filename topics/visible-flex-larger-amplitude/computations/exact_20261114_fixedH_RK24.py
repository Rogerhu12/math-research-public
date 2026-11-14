#!/usr/bin/env python3
"""Re-solve the original fixed-g/depth8/complete32H tail with RK24.

The original RK12 shooting packet is only a warm start. Original Newton,
line search, convergence tolerance, full requested DN Jacobian and finite
audit remain active. Only steps/auditSteps and private I/O paths change.
"""
import argparse,datetime,gzip,hashlib,json,os,subprocess,time
from pathlib import Path


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)


def write(p,obj,compressed=False):
    b=(json.dumps(obj,separators=(',',':'),allow_nan=False)+'\n').encode()
    with Path(p).open('xb')as f:f.write(gzip.compress(b,mtime=0) if compressed else b)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('topic','source-topic','out-dir'):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--steps',type=int,default=24);p.add_argument('--node-heap-mib',type=int,default=512)
    a=p.parse_args();topic=a.topic.resolve();source=a.source_topic.resolve();out=a.out_dir.resolve()
    out.mkdir(parents=True,exist_ok=False);notes=topic/'notes';comp=topic/'computations'
    stem='2026-11-13-strong-q126-m32-tail2-actual-r1'
    old_config_path=notes/(stem+'-config.json');old_response_path=notes/(stem+'-tail-response_0003.json.gz')
    old=read(old_config_path);packet=read(old_response_path);H=packet['request']['height']
    if not packet['response']['converged'] or len(H)!=32 or old['depth']!=8 or old['modes']!=32 or a.steps<=old['steps']:
        raise ValueError('Original accepted32H/depth8 input and a true RK refinement are required')
    config=dict(old);config.update(steps=a.steps,auditSteps=a.steps,initialCheckpoint=str(old_response_path),
        traceFile=str(out/'trace.jsonl'),iterationCheckpointFile=str(out/'iteration.json.gz'),
        trialDiagnosticFile=str(out/'trials.jsonl'))
    allowed={'steps','auditSteps','initialCheckpoint','traceFile','iterationCheckpointFile','trialDiagnosticFile'}
    if {k:v for k,v in old.items() if k not in allowed}!={k:v for k,v in config.items() if k not in allowed}:
        raise ValueError('Physical/source parameter changed')
    if packet['response']['checkpoint']['cutHeight']!=H:raise ValueError('Complete H differs')
    request=dict(height=H,jacobian=True,audit=True)
    write(out/'config.json',config);write(out/'request.json',request)
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
        VISIBLE_FLEX_SOURCE_TOPIC=str(source),VISIBLE_FLEX_SOURCE_ROOT=str(source/'repro/source-root'),
        CLOSING_TAIL_CACHE=str(source/'repro/source-root/topics/large-amplitude-twist-flex/scripts'),
        VISIBLE_FLEX_FROZEN_LEDGER_READY=str(notes/'2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json'),
        VISIBLE_FLEX_FROZEN_STORED_READY=str(notes/'2026-11-13-strong-m28-recovered-full-audit-r1-ready.json'),
        VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND='fourier-root',VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND='tangent',
        VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT='8')
    command=['node','--expose-gc','--max-old-space-size='+str(a.node_heap_mib),'--max-semi-space-size=4',
             str(comp/'tail_frozen_worker.mjs'),str(out/'config.json')]
    hashes={str(p):sha(p)for p in [Path(__file__),old_config_path,old_response_path,comp/'tail_frozen_worker.mjs',
        comp/'tail_frozen_geometry.mjs',comp/'tail_resumable_engine.mjs',Path(env['VISIBLE_FLEX_FROZEN_LEDGER_READY']),
        Path(env['VISIBLE_FLEX_FROZEN_STORED_READY'])]}
    write(out/'intent.json',dict(started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_sha256_at_start=hashes,command=command,old_steps=old['steps'],new_steps=a.steps,
        complete_H_unchanged=True,depth_unchanged=8,modes_unchanged=32,changed_keys=sorted(allowed),scope=__doc__))
    start=time.monotonic();ready=None;response=None;messages=[]
    with (out/'stderr.log').open('wb')as err:
        child=subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err,text=True,env=env,bufsize=1)
        for line in child.stdout:
            row=json.loads(line)
            if row.get('event')=='ready':
                ready=row;write(out/'ready.json.gz',row,True)
                print(json.dumps(dict(event='ready',warm_embedding=row.get('warmEmbedding'),steps=a.steps)),flush=True)
                child.stdin.write(json.dumps(request)+'\n'+json.dumps(dict(stop=True))+'\n')
                child.stdin.flush();child.stdin.close()
            elif 'converged'in row or 'failed'in row:
                response=row;write(out/'response.json.gz',row,True)
                print(json.dumps(dict(event='response',converged=row.get('converged'),residual=row.get('residual'),failed=row.get('failed'))),flush=True)
            else:messages.append(row)
        code=child.wait()
    success=code==0 and response is not None and response.get('converged')is True and response['residual']<config['solveTolerance'] and response.get('audit')is not None and response.get('heightJetJacobian')is not None
    result=dict(finished=True,success=success,actual_exit_code=code,seconds=time.monotonic()-start,
        old_steps=old['steps'],new_steps=a.steps,source_sha256_at_start=hashes,messages=messages,
        complete_H_unchanged=True,all_physical_and_source_parameters_unchanged=True,
        ready_received=ready is not None,response_received=response is not None,
        requested_full_DN_Jacobian=True,requested_full_finite_audit=True,
        output_files={p.name:sha(p)for p in out.iterdir()if p.is_file()},
        scope='A finite discretization refinement at the same exact original metric and all32 fixed heights, not a new accepted prefix or infinite solution.')
    if response is not None:result.update(residual=response.get('residual'),converged=response.get('converged'),audit=response.get('audit'),failed=response.get('failed'))
    write(out/'result.json',result)
    print(json.dumps(dict(event='terminal',success=success,actual_exit_code=code,seconds=result['seconds'])),flush=True)
    return 0 if success else 1


if __name__=='__main__':raise SystemExit(main())
