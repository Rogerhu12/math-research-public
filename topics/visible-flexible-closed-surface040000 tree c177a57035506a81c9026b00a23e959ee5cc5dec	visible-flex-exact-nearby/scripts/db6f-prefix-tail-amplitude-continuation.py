#!/usr/bin/env python3
"""Actual finite-tail boundary continuation on one fixed metric and discretization.

Intermediate H_j(s)=s**(j+1)*H_target[j] solves are warm states only and do
not match the complete target prefix. Only s=1 is the target DN; even then
the original actual prefix boundary correction remains necessary.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
import sys
import time
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent


def read(p):
    p=Path(p)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_text())


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def atomic_json(p,data):
    p=Path(p);raw=(json.dumps(data,indent=2)+'\n').encode()
    if len(raw)>1_000_000:raise ValueError('Progress metadata exceeds uncompressed limit')
    temp=p.with_name(p.name+'.tmp')
    with temp.open('wb') as f:f.write(raw);f.flush();os.fsync(f.fileno())
    os.replace(temp,p)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-root',type=Path,required=True)
    ap.add_argument('--config',type=Path,required=True)
    ap.add_argument('--target-prefix',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--initial-scale',type=float,default=.25)
    ap.add_argument('--initial-step',type=float,default=.125)
    ap.add_argument('--maximum-step',type=float,default=.2)
    ap.add_argument('--minimum-step',type=float,default=1/4096)
    ap.add_argument('--max-attempts',type=int,default=64)
    ap.add_argument('--node-heap',type=int,default=1536)
    ap.add_argument('--resume-checkpoint',type=Path)
    ap.add_argument('--resume-scale',type=float)
    a=ap.parse_args();start=time.monotonic();out=a.out_prefix.resolve()
    if any(p.name!=out.name+'-run.log' for p in out.parent.glob(out.name+'*')):
        raise FileExistsError('Output prefix already used')
    if not 0<a.initial_scale<=1 or not 0<a.minimum_step<=a.initial_step<=a.maximum_step<=1:
        raise ValueError('Invalid continuation scales')
    if bool(a.resume_checkpoint)!=(a.resume_scale is not None):
        raise ValueError('Both resume arguments are required together')
    original=read(a.config);prefix=read(a.target_prefix)
    goal=np.asarray(prefix['predicted_cut_height'],dtype=float)
    M=original['modes'];tol=original['solveTolerance']
    if goal.shape!=(M,) or not np.all(np.isfinite(goal)):
        raise ValueError('Wrong physical target-height vector')
    if prefix['config']['modes']!=M or prefix['config'].get('actual_nonlinear_tail') is not False:
        raise ValueError('Target must be the explicit auxiliary M-mode prefix')
    for key,value in prefix['physical_tail_parameters'].items():
        if original.get(key)!=value:raise ValueError('Physical tail mismatch: '+key)
    powers=np.arange(1,M+1)
    def target(s):return goal.copy() if s==1 else goal*np.float64(s)**powers
    cfg=dict(original)
    # A fresh run starts from the original linear shooting initial state.
    # It deliberately does not carry the previous failed macro state.
    cfg.pop('initialCheckpoint',None)
    paths=dict(traceFile=str(out)+'-active-trace.jsonl',
               iterationCheckpointFile=str(out)+'-iteration.json.gz',
               trialDiagnosticFile=str(out)+'-active-trials.jsonl',
               trialStatePrefix=str(out)+'-stage-input')
    cfg.update(paths)
    last_scale=None;last_record=None;last_hash=None
    if a.resume_checkpoint:
        saved=read(a.resume_checkpoint)
        if not saved.get('response',{}).get('converged') or not 0<=saved['response']['residual']<tol:
            raise ValueError('Resume record is not an actual converged response')
        if not 0<a.resume_scale<1 or not np.array_equal(np.asarray(saved['request']['height']),target(a.resume_scale)):
            raise ValueError('Resume scale does not exactly identify the fixed target path')
        cfg['initialCheckpoint']=str(a.resume_checkpoint.resolve())
        last_scale=a.resume_scale;last_record=str(a.resume_checkpoint.resolve());last_hash=sha(a.resume_checkpoint)
    config_path=Path(str(out)+'-config.json');config_path.write_text(json.dumps(cfg,indent=2)+'\n')
    client=HERE/'db6f-prefix-tail-continuation-client.py'
    spec=importlib.util.spec_from_file_location('amplitude_continuation_client',client)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    binding=dict(scope=__doc__,command=[sys.executable,str(Path(__file__).resolve()),*sys.argv[1:]],
        script_sha256=sha(__file__),client_sha256=sha(client),config=str(config_path),config_sha256=sha(config_path),
        original_config=str(a.config.resolve()),original_config_sha256=sha(a.config),
        target_prefix=str(a.target_prefix.resolve()),target_prefix_sha256=sha(a.target_prefix),
        target_height=goal.tolist(),indexing='stored index j=0 uses exponent j+1; height is physical, with no extra r^4 conversion',
        initial_scale=a.initial_scale,initial_step=a.initial_step,maximum_step=a.maximum_step,
        minimum_step=a.minimum_step,max_attempts=a.max_attempts,
        source_map_sha256=sha(HERE.parent/'notes/2026-11-09-db6f-prefix-tail-continuation-source-map.json'),
        resume_record=last_record,resume_record_sha256=last_hash)
    Path(str(out)+'-input-bindings.json').write_text(json.dumps(binding,indent=2)+'\n')
    state=dict(scope=__doc__,status='RUNNING_WARM_CONTINUATION',target_reached=False,target_audited=False,
        last_converged_scale=last_scale,last_converged_record=last_record,last_converged_sha256=last_hash,
        original_tail_tolerance=tol,attempts=[])
    progress=Path(str(out)+'-progress.json');atomic_json(progress,state)
    port=None;step=a.initial_step;candidate=a.initial_scale if last_scale is None else min(1,last_scale+step)
    def rotate(call):
        result=[]
        for kind,key in [('trace','traceFile'),('trials','trialDiagnosticFile')]:
            active=Path(cfg[key])
            if active.exists():
                dest=Path(str(out)+f'-call{call:03d}-{kind}.jsonl')
                if dest.exists():raise FileExistsError(dest)
                os.rename(active,dest)
                result.append(dict(path=str(dest),sha256=sha(dest),bytes=dest.stat().st_size))
        return result
    try:
        port=mod.WeightedTailPort(config_path,a.source_root.resolve(),str(out)+'_tail',a.node_heap)
        for attempt in range(a.max_attempts):
            state.update(current_attempt=attempt,current_requested_scale=candidate,current_step=step)
            atomic_json(progress,state)
            error=None;response=None
            try:
                response=port.solve(target(candidate),jacobian=False,audit=False)
            except FloatingPointError as exc:
                error=repr(exc)
            call=port.calls;record=Path(str(out)+f'_tail_{call:04d}.json.gz')
            if not record.is_file():raise RuntimeError('No complete atomic response record')
            actual=read(record)['response']
            success=bool(actual.get('converged')) and math.isfinite(actual.get('residual',math.inf)) and 0<=actual['residual']<tol
            if response is not None and not success:raise RuntimeError('Success protocol disagrees with original residual tolerance')
            row=dict(attempt=attempt,call=call,scale=candidate,step=step,converged=success,
                residual=actual.get('residual'),error=error,response_record=str(record),response_sha256=sha(record),
                intermediate_scope='target DN' if candidate==1 else 'WARM ONLY: does not match the complete target prefix',
                last_iteration=actual.get('lastIteration'),logs=rotate(call))
            if success:
                history=actual.get('history',[]);row['iterations']=len(history)
                last_scale=candidate;last_record=str(record);last_hash=sha(record)
                state.update(last_converged_scale=last_scale,last_converged_record=last_record,last_converged_sha256=last_hash)
                if candidate==1:
                    state['target_reached']=True
                elif len(history)<=3:step=min(a.maximum_step,1.5*step)
                elif len(history)>7:step=max(a.minimum_step,.5*step)
            else:
                # The unchanged worker updates its internal last state only on
                # a converged response, so the failed trial never becomes warm.
                if last_scale is None:candidate*=.5
                else:step=.5*(candidate-last_scale)
            state['attempts'].append(row);atomic_json(progress,state)
            print(json.dumps({k:row.get(k) for k in ['attempt','call','scale','converged','residual','iterations','error']}),flush=True)
            if state['target_reached']:break
            if (last_scale is None and candidate<a.minimum_step) or step<a.minimum_step:
                state['status']='UNCONVERGED_CONTINUATION_STEP_LIMIT';break
            if last_scale is not None:candidate=min(1,last_scale+step)
        else:state['status']='UNCONVERGED_CONTINUATION_ATTEMPT_LIMIT'
        if state['target_reached']:
            # An exact copy of the fixed target, not a cumulative continuation
            # update, is sent for the final original tangent and source audit.
            final=port.solve(goal.copy(),jacobian=True,audit=True)
            if not final['converged'] or not 0<=final['residual']<tol:
                raise RuntimeError('Final target audit did not meet original tolerance')
            call=port.calls;record=Path(str(out)+f'_tail_{call:04d}.json.gz')
            state.update(status='TARGET_DN_CONVERGED_AND_AUDITED_PREFIX_STILL_UNSOLVED',target_audited=True,
                         final_target_record=str(record),final_target_sha256=sha(record),
                         final_residual=final['residual'],final_audit=final.get('audit'),final_logs=rotate(call))
    except Exception as exc:
        state.update(status='UNCONVERGED_CONTINUATION_EXCEPTION',exception=repr(exc))
        if port is not None and port.calls:
            record=Path(str(out)+f'_tail_{port.calls:04d}.json.gz')
            if record.is_file() and not any(row['call']==port.calls for row in state['attempts']):
                state['exception_response']=dict(path=str(record),sha256=sha(record))
    finally:
        if port is not None:port.close()
        if port is not None:state['remaining_closed_logs']=rotate(port.calls)
        state.update(seconds=time.monotonic()-start,worker_exit_code=None if port is None else port.proc.poll())
        atomic_json(progress,state)
        Path(str(out)+'-reproduction.json').write_text(json.dumps(dict(binding,result=state),indent=2)+'\n')
        print(json.dumps({k:state.get(k) for k in ['status','target_reached','target_audited','last_converged_scale','final_residual','exception','worker_exit_code','seconds']}),flush=True)


if __name__=='__main__':main()
