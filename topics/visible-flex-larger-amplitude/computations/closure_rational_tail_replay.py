#!/usr/bin/env python3
"""Replay one actual finite tail in the separately named rational-deep metric.

This does not append to an old fixed-g refinement chain. The old checkpoint is
only a warm start; the original nonlinear residual and solve tolerance decide
success. Data are retained as one gzip file and a small JSON summary.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time


def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--source-topic',type=Path,required=True)
    p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--linear-far',type=int,default=192)
    p.add_argument('--linear-steps',type=int)
    p.add_argument('--node-heap',type=int,default=1024)
    args=p.parse_args()
    prior=read(args.input)
    cfg=dict(prior['config'])
    height=prior['request']['height']
    pre=args.out_prefix.resolve()
    paths={name:Path(str(pre)+suffix) for name,suffix in [
        ('config','-config.json'),('response','-response.json.gz'),
        ('summary','-summary.json'),('trace','-trace.jsonl'),('ready','-ready.json')]}
    if any(x.exists() for x in paths.values()):raise FileExistsError('Use a fresh output prefix')
    pre.parent.mkdir(parents=True,exist_ok=True)
    # Only I/O paths and the explicitly NEW deep model's linear boundary are
    # replaced. Every nonlinear resolution and acceptance parameter is kept.
    for k in ['traceFile','iterationCheckpointFile','trialDiagnosticFile','trialStatePrefix','initialCheckpoint']:
        cfg.pop(k,None)
    cfg.update(initialCheckpoint=str(args.input.resolve()),linearFar=args.linear_far,
               traceFile=str(paths['trace']),rationalPointCacheLimit=96)
    if args.linear_steps is not None:cfg['linearSteps']=args.linear_steps
    paths['config'].write_text(json.dumps(cfg,indent=2)+'\n')
    topic=args.source_topic.resolve();root=topic/'repro/source-root'
    env=dict(os.environ,VISIBLE_FLEX_SOURCE_TOPIC=str(topic),VISIBLE_FLEX_SOURCE_ROOT=str(root),
             CLOSING_TAIL_CACHE=str(root/'topics/large-amplitude-twist-flex/scripts'),
             VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND='fourier-root',VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND='tangent',
             NODE_OPTIONS=f'--max-old-space-size={args.node_heap}')
    worker=Path(__file__).with_name('closure_rational_tail_worker.mjs')
    source_hashes={x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in [Path(__file__),worker]}
    t0=time.monotonic()
    proc=subprocess.Popen(['node',str(worker),str(paths['config'])],stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE,text=True,bufsize=1,env=env)
    try:
        ready_line=proc.stdout.readline()
        if not ready_line:
            code=proc.wait()
            raise RuntimeError(f'New rational tail worker failed during initialization, exit {code}')
        ready=json.loads(ready_line);paths['ready'].write_text(json.dumps(ready,indent=2)+'\n')
        if ready.get('endpointJacobianAdapter',{}).get('name')!='closure-rational-deep-worker-v1':
            raise RuntimeError('Wrong new-g worker')
        print(json.dumps(dict(event='ready',elapsed=time.monotonic()-t0,modes=len(height),
                              shallowHeadPreserved=ready.get('shallowHeadPreserved'))),flush=True)
        request=dict(height=height,jacobian=False,audit=True)
        proc.stdin.write(json.dumps(request)+'\n');proc.stdin.flush()
        line=proc.stdout.readline()
        if not line:raise RuntimeError('New rational tail worker ended without a response')
        response=json.loads(line)
        proc.stdin.write('{"stop":true}\n');proc.stdin.flush()
        code=proc.wait()
        if code:raise RuntimeError(f'New rational tail worker ended with exit {code}')
    finally:
        if proc.poll() is None:
            proc.terminate()
            try:proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill();proc.wait()
        for stream in [proc.stdin,proc.stdout]:
            if stream:stream.close()
    record=dict(request=request,response=response,config=cfg,ready=ready,
                provenance=dict(input=str(args.input.resolve()),input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
                                entrypoint_sha256=source_hashes,
                                semantic_change='New fixed rational source for n>=protectCell; old g_stored is not relabeled.'))
    data=gzip.compress((json.dumps(record,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(data)>=5_000_000:raise RuntimeError('Completed response exceeds the repository file cap')
    paths['response'].write_bytes(data)
    summary=dict(status='finite nonlinear solve in a new fixed metric',
                 converged=response.get('converged',False),residual=response.get('residual'),failed=response.get('failed'),
                 audit=response.get('audit'),elapsed=time.monotonic()-t0,
                 peak_child_RSS_KiB=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
                 shallowHeadPreserved=ready.get('shallowHeadPreserved'),
                 model=ready.get('rationalDeepModel'),history=response.get('history'),
                 response=str(paths['response']),response_sha256=hashlib.sha256(data).hexdigest(),response_bytes=len(data),
                 limits=['Finite-M and finite nonlinear depth only.','A fixed far Robin graph is not the full nonlinear R15 trace.',
                         'No complete strong closed surface or reach certificate.'])
    paths['summary'].write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:summary[k] for k in ['converged','residual','failed','audit','elapsed','response_bytes']}),flush=True)


if __name__=='__main__':main()
