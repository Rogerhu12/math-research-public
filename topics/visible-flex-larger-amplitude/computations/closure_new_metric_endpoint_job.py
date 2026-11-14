#!/usr/bin/env python3
"""Prepare or run an explicit old-metric -> rational-new-metric endpoint job.

The prepare command is read/metadata only. The run command consumes an immutable
plan and requires the separately scheduled exclusive Node window. Old results
are warm starts, never relabeled as a same-g refinement of the new model.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import time

from closure_scaled_endpoint_replay import endpoint_diagnostic, cut_jet_norm_comparison


def sha(raw):return hashlib.sha256(raw).hexdigest()


def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),raw


GEOMETRY_KEYS=['rCut','wCut','width','curvatureBound','delta0','R','a','etaPower',
    'etaRatioAtN0','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell',
    'calibrationSteps','warpSteps','quadratureTolerance','slopeCap','capTransition',
    'capMode','cuspAwareQuadrature','valleyControls','rejoinR20At','rejoinIndexOffset',
    'pulseCaps','valleyCaps','flatOuterThroughCell','flatSlope','flatOuterStartSegment',
    'warpWeightLevels']
DEFAULTS=dict(delta0=.006,R=64,a=2.75,etaPower=1.5,etaRatioAtN0=.05,
    rejoinR20At=None,rejoinIndexOffset=4,pulseCaps=None,valleyCaps=None,
    flatOuterThroughCell=None,flatSlope=None,flatOuterStartSegment=2,warpWeightLevels=[])
MODEL_KEYS=['definition','sourceRevision','sourceHashes','start','deepAlpha','exactSourceConstants','frozenWarpAlpha','headFingerprint']
OWN_FILES=['closure_new_metric_endpoint_job.py','closure_scaled_endpoint_replay.py',
    'closure_scaled_endpoint_worker.mjs','closure_scaled_endpoint_engine.mjs',
    'closure_scaled_endpoint_graphs.mjs','closure_rational_tail_model.mjs',
    'closure_depth_warm_remesh.mjs','closure_linear_stage_graphs.mjs',
    'closure_bounded_point_cache.mjs','numerical-tail-slope-jacobian.mjs']


def own_hashes():
    return {name:sha(Path(__file__).with_name(name).read_bytes()) for name in OWN_FILES}


def prepare(args):
    prior,prior_raw=read(args.input)
    reference,reference_raw=read(args.reference_ready)
    model=reference['rationalDeepModel'];physical=model['physicalParameters']
    cfg=dict(prior['config']);height=list(prior['request']['height'])
    if not prior['response'].get('converged') or not prior['response'].get('checkpoint'):
        raise ValueError('A completed old-metric actual response/checkpoint is required')
    if len(height)!=cfg['modes'] or not 1<=len(height)<=46:
        raise ValueError('The complete actual low-height vector must have 1..46 modes')
    missing=[k for k in GEOMETRY_KEYS if k not in cfg and k not in DEFAULTS]
    if missing:raise ValueError('Unspecified geometric inputs: '+','.join(missing))
    old_geometry={k:cfg.get(k,DEFAULTS.get(k)) for k in GEOMETRY_KEYS}
    reference_geometry={k:physical.get(k,DEFAULTS.get(k)) for k in GEOMETRY_KEYS}
    changed=[k for k in GEOMETRY_KEYS if old_geometry[k]!=reference_geometry[k]]
    if changed:raise ValueError('The proposed frozen shallow metric does not match old input: '+','.join(changed))
    if args.depth<cfg['depth']:raise ValueError('Do not shorten the actual nonlinear depth')
    prefix=args.out_prefix.resolve()
    paths={name:Path(str(prefix)+suffix) for name,suffix in [
        ('plan','-plan.json'),('config','-config.json'),('ready','-ready.json'),
        ('response','-response.json.gz'),('summary','-summary.json'),
        ('trace','-trace.jsonl'),('iteration','-iteration-recovery.json.gz'),('trials','-trials.jsonl')]}
    if any(x.exists() for x in paths.values()):raise FileExistsError('Use a fresh output prefix')
    prefix.parent.mkdir(parents=True,exist_ok=True)
    for k in ['traceFile','iterationCheckpointFile','trialDiagnosticFile','trialStatePrefix','initialCheckpoint']:
        cfg.pop(k,None)
    cfg.update(initialCheckpoint=str(args.input.resolve()),depth=args.depth,linearFar=args.linear_far,
        traceFile=str(paths['trace']),iterationCheckpointFile=str(paths['iteration']),
        trialDiagnosticFile=str(paths['trials']),rationalPointCacheLimit=96,
        rationalFrozenWarpAlpha=model['frozenWarpAlpha'])
    cfg['auditSteps']=max(cfg.get('auditSteps',0),cfg['steps'])
    cfg_bytes=(json.dumps(cfg,indent=2)+'\n').encode();paths['config'].write_bytes(cfg_bytes)
    plan=dict(schema='rational-new-metric-endpoint-job-v1',status='PREPARED ONLY; no worker has been started',
        original_input=str(args.input.resolve()),original_input_sha256=sha(prior_raw),
        warm_source=str(args.input.resolve()),warm_source_sha256=sha(prior_raw),
        warm_source_status='completed old-metric response used only as a starting iterate',
        reference_ready=str(args.reference_ready.resolve()),reference_ready_sha256=sha(reference_raw),
        source_topic=str(args.source_topic.resolve()),paths={k:str(v) for k,v in paths.items()},
        config_sha256=sha(cfg_bytes),expected_new_metric={k:model[k] for k in MODEL_KEYS},
        geometry_keys_verified=GEOMETRY_KEYS,geometry_inputs=old_geometry,
        request=dict(height=height,jacobian=False,audit=True),
        old_resolution={k:prior['config'].get(k) for k in ['modes','quadrature','depth','steps','shootingParts','linearFar','linearSteps']},
        new_resolution={k:cfg.get(k) for k in ['modes','quadrature','depth','steps','shootingParts','linearFar','linearSteps']},
        own_hashes=own_hashes(),
        semantics=['This starts a NEW fixed metric beyond cell160, with exact deep alpha65/64.',
            'Every captured shallow geometric input and the frozen binary global warp alpha are retained.',
            'The original complete actual H vector is retained; its old response is a warm start only.',
            'The original nonlinear solve tolerance and acceptance gates are retained.',
            'Physical depth extension is nonlinear re-solving, not a linear-tail substitution.',
            'Exact R_out/E/Ep source-vs-stored port differences remain R26 responsibilities.'],
        scheduling='Run only in the explicitly assigned exclusive large-Node window; preparation itself starts no process.')
    paths['plan'].write_text(json.dumps(plan,indent=2)+'\n')
    print(json.dumps(dict(plan=str(paths['plan']),status=plan['status'],modes=len(height),H2=height[0],
        old_resolution=plan['old_resolution'],new_resolution=plan['new_resolution'])))


def recover(args):
    old,old_raw=read(args.plan)
    if old['schema']!='rational-new-metric-endpoint-job-v1':raise ValueError('Wrong old plan schema')
    recovery_path=Path(old['paths']['iteration'])
    recovery,recovery_raw=read(recovery_path)
    if recovery.get('status')!='iteration-recovery-only' or not recovery.get('checkpoint'):
        raise ValueError('The scheduled job has no recovery-only checkpoint')
    cfg_raw=Path(old['paths']['config']).read_bytes()
    if sha(cfg_raw)!=old['config_sha256']:raise ValueError('Old prepared config changed')
    cfg=json.loads(cfg_raw)
    prefix=args.out_prefix.resolve()
    paths={name:Path(str(prefix)+suffix) for name,suffix in [
        ('plan','-plan.json'),('config','-config.json'),('ready','-ready.json'),
        ('response','-response.json.gz'),('summary','-summary.json'),
        ('trace','-trace.jsonl'),('iteration','-iteration-recovery.json.gz'),('trials','-trials.jsonl')]}
    if any(x.exists() for x in paths.values()):raise FileExistsError('Use a fresh recovery output prefix')
    cfg.update(initialCheckpoint=str(recovery_path.resolve()),traceFile=str(paths['trace']),
        iterationCheckpointFile=str(paths['iteration']),trialDiagnosticFile=str(paths['trials']))
    cfg_raw=(json.dumps(cfg,indent=2)+'\n').encode();paths['config'].write_bytes(cfg_raw)
    new={**old,'status':'PREPARED RECOVERY ONLY; checkpoint is not a converged result',
        'paths':{k:str(v) for k,v in paths.items()},'config_sha256':sha(cfg_raw),
        'own_hashes':own_hashes(),'warm_source':str(recovery_path.resolve()),
        'warm_source_sha256':sha(recovery_raw),'warm_source_status':'iteration-recovery-only',
        'recovered_from_plan':str(args.plan.resolve()),'recovered_from_plan_sha256':sha(old_raw),
        'recovery_iteration':recovery.get('iteration')}
    paths['plan'].write_text(json.dumps(new,indent=2)+'\n')
    print(json.dumps(dict(plan=str(paths['plan']),status=new['status'],iteration=new['recovery_iteration'])))


def run(args):
    plan,plan_raw=read(args.plan)
    if plan['schema']!='rational-new-metric-endpoint-job-v1':raise ValueError('Wrong job schema')
    if own_hashes()!=plan['own_hashes']:raise ValueError('Runtime source changed; prepare a new auditable plan')
    paths={k:Path(v) for k,v in plan['paths'].items()}
    for key in ['ready','response','summary','trace','iteration','trials']:
        if paths[key].exists():raise FileExistsError('Job already started; preserve it and prepare a recovery job explicitly')
    cfg_raw=paths['config'].read_bytes()
    if sha(cfg_raw)!=plan['config_sha256']:raise ValueError('Prepared config changed')
    prior,prior_raw=read(Path(plan['original_input']))
    if sha(prior_raw)!=plan['original_input_sha256']:raise ValueError('Actual input changed')
    if sha(Path(plan.get('warm_source',plan['original_input'])).read_bytes())!=plan.get('warm_source_sha256',plan['original_input_sha256']):
        raise ValueError('Prepared warm/recovery checkpoint changed')
    if sha(Path(plan['reference_ready']).read_bytes())!=plan['reference_ready_sha256']:
        raise ValueError('Frozen source reference changed')
    cfg=json.loads(cfg_raw);topic=Path(plan['source_topic']);root=topic/'repro/source-root'
    env=dict(os.environ,VISIBLE_FLEX_SOURCE_TOPIC=str(topic),VISIBLE_FLEX_SOURCE_ROOT=str(root),
        CLOSING_TAIL_CACHE=str(root/'topics/large-amplitude-twist-flex/scripts'),
        VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND='fourier-root',VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND='tangent',
        NODE_OPTIONS=f'--max-old-space-size={args.node_heap}')
    worker=Path(__file__).with_name('closure_scaled_endpoint_worker.mjs');started=time.monotonic()
    proc=subprocess.Popen(['node','--expose-gc',str(worker),str(paths['config'])],stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE,text=True,bufsize=1,env=env)
    try:
        line=proc.stdout.readline()
        if not line:raise RuntimeError(f'Worker initialization failed: exit {proc.wait()}')
        ready=json.loads(line);paths['ready'].write_text(json.dumps(ready,indent=2)+'\n')
        if ready.get('endpointJacobianAdapter',{}).get('name')!='closure-scaled-endpoint-worker-v1':
            raise RuntimeError('Wrong endpoint worker')
        differences=[k for k,v in plan['expected_new_metric'].items() if ready['rationalDeepModel'][k]!=v]
        if differences:raise RuntimeError('Prepared new metric changed: '+','.join(differences))
        print(json.dumps(dict(event='ready',seconds=time.monotonic()-started,new_metric=True,
            old_input_only_warm_start=True)),flush=True)
        proc.stdin.write(json.dumps(plan['request'])+'\n');proc.stdin.flush()
        line=proc.stdout.readline()
        if not line:raise RuntimeError(f'Worker ended without a response: exit {proc.wait()}')
        response=json.loads(line)
        # Save the complete response immediately; a later stop/summary failure
        # must not destroy a completed nonlinear result.
        record=dict(request=plan['request'],response=response,config=cfg,ready=ready,
            provenance=dict(plan=str(args.plan.resolve()),plan_sha256=sha(plan_raw),
                original_input=plan['original_input'],original_input_sha256=plan['original_input_sha256'],
                semantic_change='NEW fixed rational-deep g; old response was only a warm start.'))
        raw=gzip.compress((json.dumps(record,separators=(',',':'))+'\n').encode(),mtime=0)
        if len(raw)>=5_000_000:raise RuntimeError('Repository file cap exceeded')
        paths['response'].write_bytes(raw)
        proc.stdin.write('{"stop":true}\n');proc.stdin.flush()
        if proc.wait():raise RuntimeError('Worker failed after complete response was saved')
    finally:
        if proc.poll() is None:
            proc.terminate()
            try:proc.wait(timeout=5)
            except subprocess.TimeoutExpired:proc.kill();proc.wait()
        for stream in [proc.stdin,proc.stdout]:
            if stream:stream.close()
    summary=dict(status='Actual finite solve on the explicitly NEW rational-deep metric',
        converged=response.get('converged'),residual=response.get('residual'),history=response.get('history'),
        audit=response.get('audit'),endpoint_diagnostic=endpoint_diagnostic(ready,response),
        old_to_new_shallow_cut_comparison=cut_jet_norm_comparison(prior['response']['jets'],response['jets'],cfg['spacing']),
        seconds=time.monotonic()-started,peak_child_RSS_KiB=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
        response=str(paths['response']),response_sha256=sha(raw),response_bytes=len(raw),
        limits=['No same-g old-to-new refinement claim.','Finite modes/depth and finite far linear graph remain explicit.',
            'True source/port, complete-frequency nonlinear matching and global closed geometry remain separate.'])
    paths['summary'].write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:summary[k] for k in ['converged','residual','seconds','peak_child_RSS_KiB','response_bytes']}),flush=True)


def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='action',required=True)
    a=sub.add_parser('prepare');a.add_argument('--input',type=Path,required=True)
    a.add_argument('--reference-ready',type=Path,required=True);a.add_argument('--source-topic',type=Path,required=True)
    a.add_argument('--out-prefix',type=Path,required=True);a.add_argument('--depth',type=int,default=12)
    a.add_argument('--linear-far',type=int,default=225)
    b=sub.add_parser('run');b.add_argument('--plan',type=Path,required=True);b.add_argument('--node-heap',type=int,default=768)
    c=sub.add_parser('recover');c.add_argument('--plan',type=Path,required=True);c.add_argument('--out-prefix',type=Path,required=True)
    args=p.parse_args();{'prepare':prepare,'run':run,'recover':recover}[args.action](args)


if __name__=='__main__':main()
