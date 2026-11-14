#!/usr/bin/env python3
"""Refine the actual accepted-A finite tail at unchanged metric and complete H.

Only physical depth is increased. Existing 577 states are retained by the
recorded depth warm remesher, and the appended states are only an initial
guess. The original finite nonlinear solver and full requested audit decide
whether the new finite tail succeeds. This is not a closed surface certificate.
"""
from __future__ import annotations
import argparse
import datetime
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path,value,compressed=False):
    raw=(json.dumps(value,separators=(',',':'),allow_nan=False)+'\n').encode()
    if compressed: raw=gzip.compress(raw,mtime=0)
    with Path(path).open('xb') as out: out.write(raw)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topic',type=Path,required=True)
    parser.add_argument('--source-topic',type=Path,required=True)
    parser.add_argument('--out-dir',type=Path,required=True)
    parser.add_argument('--depth',type=int,default=12)
    parser.add_argument('--node-heap-mib',type=int,default=384)
    args=parser.parse_args()
    topic=args.topic.resolve(); source=args.source_topic.resolve(); work=args.out_dir.resolve()
    work.mkdir(parents=True,exist_ok=False)
    notes=topic/'notes'; comp=topic/'computations'
    base='2026-11-13-strong-q126-m32-tail2-actual-r1'
    old_config_path=notes/(base+'-config.json')
    old_packet_path=notes/(base+'-tail-response_0003.json.gz')
    old_config=read(old_config_path); old_packet=read(old_packet_path)
    response=old_packet['response']; H=old_packet['request']['height']
    assert response['converged'] and response['residual']<old_config['solveTolerance']
    assert old_config['depth']==8 and old_config['modes']==32
    assert args.depth>8 and args.depth<old_config['linearFar']
    assert response['checkpoint']['cutHeight']==H and len(H)==32
    config=dict(old_config)
    config.update(depth=args.depth,initialCheckpoint=str(old_packet_path),
                  traceFile=str(work/'trace.jsonl'),
                  iterationCheckpointFile=str(work/'iteration.json.gz'),
                  trialDiagnosticFile=str(work/'trials.jsonl'))
    allowed={'depth','initialCheckpoint','traceFile','iterationCheckpointFile','trialDiagnosticFile'}
    assert {k:v for k,v in old_config.items() if k not in allowed}=={
        k:v for k,v in config.items() if k not in allowed}
    write(work/'config.json',config)
    request={'height':H,'jacobian':False,'audit':True}
    write(work/'request.json',request)
    env=os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
      VISIBLE_FLEX_SOURCE_TOPIC=str(source),
      VISIBLE_FLEX_SOURCE_ROOT=str(source/'repro/source-root'),
      CLOSING_TAIL_CACHE=str(source/'repro/source-root/topics/large-amplitude-twist-flex/scripts'),
      VISIBLE_FLEX_FROZEN_LEDGER_READY=str(notes/'2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json'),
      VISIBLE_FLEX_FROZEN_STORED_READY=str(notes/'2026-11-13-strong-m28-recovered-full-audit-r1-ready.json'),
      VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND='fourier-root',
      VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND='tangent',
      VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT='8',
      EXACT_DEPTH_ADAPTER_RECORD=str(work/'adapter.json'))
    command=['node','--expose-gc','--max-old-space-size='+str(args.node_heap_mib),
             '--max-semi-space-size=4',str(comp/'exact_20261114_stored_depth_worker.mjs'),str(work/'config.json')]
    begin=time.monotonic()
    inputs={str(p):sha(p) for p in (old_config_path,old_packet_path,
        Path(env['VISIBLE_FLEX_FROZEN_LEDGER_READY']),Path(env['VISIBLE_FLEX_FROZEN_STORED_READY']),
        comp/'exact_20261114_stored_depth_worker.mjs',Path(__file__).resolve())}
    write(work/'intent.json',dict(command=command,input_sha256=inputs,
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        scope=__doc__,fixed_H=H,old_depth=8,new_depth=args.depth))
    ready=None; final=None; messages=[]
    with (work/'stderr.log').open('xb') as stderr:
        process=subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                                 stderr=stderr,text=True,env=env,bufsize=1)
        for line in process.stdout:
            row=json.loads(line)
            if row.get('event')=='ready':
                ready=row;write(work/'ready.json.gz',row,compressed=True)
                print(json.dumps({'event':'ready','depth':args.depth,
                    'nodes':row['warmEmbedding']['nodeCount'],
                    'old_node_max_difference':row['warmEmbedding']['maxExistingStateDifference']}),flush=True)
                process.stdin.write(json.dumps(request)+'\n'+json.dumps({'stop':True})+'\n')
                process.stdin.flush();process.stdin.close()
            elif 'converged' in row or 'failed' in row:
                final=row;write(work/'response.json.gz',row,compressed=True)
                print(json.dumps({'event':'response','converged':row.get('converged'),
                    'residual':row.get('residual'),'failed':row.get('failed')}),flush=True)
            else:
                messages.append(row)
        code=process.wait()
    success=code==0 and ready is not None and final is not None and final.get('converged') is True
    if success: success=final['residual']<config['solveTolerance'] and final.get('audit') is not None
    record=dict(scope=__doc__,actual_exit_code=code,wall_seconds=time.monotonic()-begin,
        success=success,old_depth=8,new_depth=args.depth,input_sha256=inputs,
        unchanged_physical_configuration=True,complete_cut_H_unchanged=True,
        source_A_sha256=sha(notes/(base+'.json.gz')),messages=messages,
        output_files={p.name:sha(p) for p in sorted(work.iterdir()) if p.is_file()},
        ready_received=ready is not None,response_received=final is not None,
        closed_surface_or_infinite_tail_claimed=False)
    if final is not None:
        record.update(converged=final.get('converged'),residual=final.get('residual'),
                      audit=final.get('audit'),failed=final.get('failed'))
    write(work/'result.json',record)
    print(json.dumps({'event':'completed','success':success,'exit_code':code,
                      'wall_seconds':record['wall_seconds'],'out_dir':str(work)}),flush=True)
    return 0 if success else 1


if __name__=='__main__': raise SystemExit(main())
