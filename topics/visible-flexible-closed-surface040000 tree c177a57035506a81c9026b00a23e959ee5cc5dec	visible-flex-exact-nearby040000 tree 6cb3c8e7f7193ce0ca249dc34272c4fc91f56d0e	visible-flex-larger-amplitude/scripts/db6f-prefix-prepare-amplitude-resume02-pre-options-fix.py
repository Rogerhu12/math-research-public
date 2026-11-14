#!/usr/bin/env python3
"""Verify the closed s=.25 response and prepare resume02; never launch a solver."""
import gzip
import hashlib
import json
import math
import sys
from pathlib import Path


def read(p):
    p=Path(p);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def write(p,data):
    p=Path(p)
    if p.exists():raise FileExistsError(p)
    raw=(json.dumps(data,indent=2,allow_nan=False)+'\n').encode()
    if len(raw)>1_000_000:raise ValueError('Unexpected large metadata')
    p.write_bytes(raw);p.chmod(0o444)


def main():
    script=Path(__file__).resolve();repo=script.parents[3];topic=script.parent.parent;notes=topic/'notes'
    recovery='2026-11-09-db6f-prefix-amplitude-recovery-s025-iter004-01'
    original='2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-01'
    resume=notes/'2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02'
    response_path=notes/(recovery+'_tail_0001.json.gz');summary_path=notes/(recovery+'-summary.json')
    old_cp_path=notes/'2026-11-09-db6f-prefix-amplitude-continuation-01-interrupted-recovery-iteration004.json.gz'
    original_config=notes/(original+'-config.json');recovery_config=notes/(recovery+'-config.json')
    target_path=notes/'2026-11-09-db6f-prefix-flat-v17v18-m15-affine-cut-predictor-from14q512.json.gz'
    original_binding=notes/(original+'-input-bindings.json')
    previous_launch=notes/'2026-11-09-db6f-prefix-amplitude-continuation-recovery-launch.json'
    response=read(response_path);closed=read(summary_path);actual=response['response'];cp=actual['checkpoint']
    old=read(old_cp_path);cfg=read(original_config);rcfg=read(recovery_config);target=read(target_path)
    source_binding=read(original_binding);launch=read(previous_launch)
    tol=cfg['solveTolerance'];M=cfg['modes'];history=actual.get('history',[])
    if tol!=2e-9 or cfg['maxIterations']!=36 or rcfg['maxIterations']!=32:
        raise ValueError('Original/recovery numerical budget changed')
    if actual.get('converged') is not True or actual.get('failed'):
        raise ValueError('Response is not a genuine success')
    residual=actual.get('residual')
    if not isinstance(residual,(float,int)) or not math.isfinite(residual) or not 0<=residual<tol:
        raise ValueError('Original shooting tolerance not met')
    if closed.get('actual_worker_exit_code')!=0 or closed.get('error') is not None or not closed.get('converged'):
        raise ValueError('Recovery summary has no clean worker completion')
    if closed['response_record_sha256']!=sha(response_path):raise ValueError('Closed response hash mismatch')
    if response['request'].get('jacobian') is not True or response['request'].get('audit') is not False:
        raise ValueError('Unexpected final recovery request')
    if actual.get('audit') is not None:raise ValueError('This recovery is an unaudited warm record')
    jac=actual.get('heightJetJacobian')
    if not isinstance(jac,list) or len(jac)!=(3*M+2)*M or not all(math.isfinite(v) for v in jac):
        raise ValueError('Missing finite original DN Jacobian')
    wanted=[v*(.25**(j+1)) for j,v in enumerate(target['predicted_cut_height'])]
    for values in [response['request']['height'],cp['cutHeight'],old['checkpoint']['cutHeight']]:
        if values!=wanted:raise ValueError('Physical cut target differs from frozen H(.25)')
    if cp['parameters']!=old['checkpoint']['parameters']:raise ValueError('Tail parameters changed')
    if (M,cp['parameters']['quadrature'],cp['parameters']['physicalDepth'],cp['parameters']['shootingParts'],cp['parameters']['steps'],cp['parameters']['projectionFloor'])!=(15,256,12,8,32,.05):
        raise ValueError('Wrong original discretization')
    for key,value in target['physical_tail_parameters'].items():
        if cfg.get(key)!=value:raise ValueError('Frozen physical metric mismatch: '+key)
    if not history or history[-1]['norm']!=residual or history[-1]['iteration']!=len(history)-1:
        raise ValueError('Incomplete original iteration history')
    if history[0]['norm']!=old['iteration']['norm']:raise ValueError('Recovered base not reproduced')
    completed_before=4;unique_bases=completed_before+len(history)
    if unique_bases<=7:raise ValueError('The observed history does not justify halving the next step')
    controller=script.with_name('db6f-prefix-tail-amplitude-continuation.py')
    client=script.with_name('db6f-prefix-tail-continuation-client.py')
    if sha(controller)!=source_binding['script_sha256'] or sha(client)!=source_binding['client_sha256']:
        raise ValueError('Reviewed controller/client changed')
    for item in launch['bound_files']:
        if sha(item['path'])!=item['sha256']:raise ValueError('Frozen source/input changed: '+item['path'])
    source_root=topic/'repro/source-root'
    command=[sys.executable,str(controller),'--source-root',str(source_root),
        '--config',str(original_config),'--target-prefix',str(target_path),'--out-prefix',str(resume),
        '--initial-scale','.25','--initial-step','.0625','--maximum-step','.2',
        '--minimum-step','.000244140625','--max-attempts','64','--node-heap','1536',
        '--resume-checkpoint',str(response_path),'--resume-scale','.25']
    files={Path(item['path']) for item in launch['bound_files']}
    files.update([script,controller,client,response_path,summary_path,original_config,recovery_config,
                  original_binding,previous_launch,target_path])
    binding_path=notes/'2026-11-09-db6f-prefix-amplitude-resume02-launch.json'
    result_path=notes/'2026-11-09-db6f-prefix-amplitude-s025-recovery-result.json'
    result=dict(status='TRUE_FINITE_DN_WARM_AT_S025_PREFIX_STILL_UNSOLVED',
        source_response=str(response_path),source_response_sha256=sha(response_path),source_summary_sha256=sha(summary_path),
        original_tolerance=tol,residual=residual,converged=True,audited=False,
        original_jacobian_requested=True,jacobian_entries=len(jac),all_jacobian_entries_finite=True,
        fixed_physical_and_numerical_parameters_identical=True,physical_H025_bitwise_identical=True,
        original_completed_iterations_before_interruption=completed_before,
        original_recorded_base_evaluations_before_interruption=5,recovery_history_count=len(history),
        distinct_base_states_on_recovered_trajectory=unique_bases,
        actual_recorded_fullJac_base_evaluations=5+len(history),
        accepted_updates=completed_before+sum('step' in row for row in history),
        final_minA=history[-1]['minA'],final_minD=history[-1]['minD'],
        actual_worker_exit_code=closed['actual_worker_exit_code'],
        actual_tool_exit_code=0,tool_exit_source='Parent root explicitly observed write_stdin(session_id=48634) return exit_code 0.',
        recovery_seconds=closed['seconds'],planned_resume_scale=.25,planned_next_step=.0625,
        planned_next_requested_scale=.3125,resume_prepared_only=True,
        scope='Only the s=.25 physical cut target has a converged finite M15 tail. No actual full-prefix coupling, no source audit, no full XYZ claim, and no infinite-tail/README completion.')
    write(result_path,result);files.add(result_path)
    bound=[dict(path=str(p.resolve()),sha256=sha(p),bytes=p.stat().st_size) for p in sorted(files)]
    binding=dict(status='PREPARED_ONLY_NO_RESUME_STARTED_BY_THIS_AGENT',cwd=str(repo),command=command,
        stdout_log=str(resume)+'-run.log',stderr='redirect to stdout_log',out_prefix=str(resume),
        resume_response_sha256=sha(response_path),resume_scale=.25,next_requested_scale=.3125,
        initial_step=.0625,step_rule='Original .125 first step is halved after the completed >7-iteration warm trajectory; no physical or solver tolerance change.',
        bound_files=bound,required_prelaunch_checks_passed=True,
        preparation_script_sha256=sha(script),original_controller_sha256=sha(controller),original_client_sha256=sha(client),
        scope='Continue the already reviewed original controller from a genuine converged H(.25) response. All later s<1 points remain warm; s=1 and its audit precede actual prefix correction.')
    write(binding_path,binding)
    print(json.dumps(dict(verified=True,response_sha256=sha(response_path),residual=residual,
        history=len(history),distinct_base_states=unique_bases,actual_fullJac_bases=5+len(history),
        accepted_updates=result['accepted_updates'],launch=str(binding_path),launch_sha256=sha(binding_path),
        solver_launches=0)),flush=True)


if __name__=='__main__':main()
