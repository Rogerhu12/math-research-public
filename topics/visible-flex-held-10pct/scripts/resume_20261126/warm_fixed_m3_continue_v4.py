#!/usr/bin/env python3
"""Actual v4 continuation from the verified original-map reexpression.

The first unchanged-lambda coordinate conversion has no invented solver
return. Every later lambda step invokes the actual full BVP and original
gates. Failed trials never become accepted seeds; lambda steps are reduced
from the last genuinely accepted field. More modes are tried only for a
completed successful finite solve whose remaining failure is metric error.
This is fixed-metric design until lambda one, not a convergence certificate.
"""
import os
import argparse
import json
import math
from pathlib import Path
import subprocess
import sys
import time
import traceback


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--work',type=Path,required=True)
    p.add_argument('--source-run',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    p.add_argument('--port32',type=Path)
    p.add_argument('--targets',type=float,nargs='+',default=[.004,.008,.016,.032,.064,.125,.25,.5,.75,1.])
    p.add_argument('--mode-levels',type=int,nargs='+',default=[24,32,40,48,64])
    p.add_argument('--minimum-lambda-step',type=float,default=1e-6)
    p.add_argument('--max-attempts',type=int,default=96)
    p.add_argument('--max-nodes',type=int,default=6000)
    a=p.parse_args()
    repo,work,out=a.repo.resolve(),a.work.resolve(),a.outdir.resolve()
    source_run=a.source_run.resolve()
    if work not in out.parents or work not in source_run.parents:
        raise ValueError('Keep real fields in the same explicit runner work directory')
    if (a.targets!=sorted(set(a.targets)) or not all(0<x<=1 for x in a.targets) or
            a.mode_levels!=sorted(set(a.mode_levels)) or a.minimum_lambda_step<=0 or
            a.max_attempts<1):
        raise ValueError('Positive increasing design targets and bounded explicit attempts are required')
    scripts=repo/'topics/visible-flex-held-10pct/scripts'
    current=scripts/'resume_20261126'
    sys.path.insert(0,str(current))
    import warm_fixed_m3_model_v4 as model
    out.mkdir(parents=True,exist_ok=False)
    begin=time.monotonic()
    state=dict(scope=__doc__,status='preparing',stages=[],progress={},result={},error=None,
        fixed_metric=True,fixed_metric_design_continuation=True,
        fixed_metric_refinement=False,complete_surface=False,
        source_run=str(source_run),source_run_sha256=model.sha(source_run),
        source_sha256=model.sha(__file__))
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
        PYTHONUNBUFFERED='1',VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
        VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
            'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
    for name in ('LD_LIBRARY_PATH','LD_PRELOAD'):
        env.pop(name,None)
    def compact(row):
        value={key:row.get(key) for key in ('kind','name','homotopy','modes','run',
            'run_sha256','returncode','accepted','solver_invoked','solver_success','error',
            'raw','scaled_bc_max','physical_bc_max','next_action','next_lambda',
            'domain_newton_stats','auxiliary_domain_guard') if key in row}
        if row.get('metric_diagnostics'):
            value['metric']=[{key:item[key] for key in
                ('angular','legacy_max_component_fft_l1','sample_operator_max')}
                for item in row['metric_diagnostics']]
        return value
    def save():
        state['elapsed']=time.monotonic()-begin
        full=out/'pipeline.json';tmp=full.with_suffix('.tmp')
        tmp.write_text(json.dumps(state,indent=2,allow_nan=False)+'\n')
        tmp.replace(full)
        visible=dict(state,stages=[compact(row) for row in state['stages'][-8:]],
            stages_total=len(state['stages']),
            complete_stage_record=dict(path=str(full),sha256=model.sha(full)))
        visible['result']=dict(state['result'])
        if 'last_attempt' in visible['result']:
            visible['result']['last_attempt']=compact(visible['result']['last_attempt'])
        path=out/'summary.json';tmp=path.with_suffix('.tmp')
        tmp.write_text(json.dumps(visible,indent=2,allow_nan=False)+'\n')
        tmp.replace(path)
    def invoke(name,command):
        state['status']=name
        state['progress']=dict(command=list(map(str,command)))
        save()
        log=out/(name+'.log')
        with log.open('x') as stream:
            proc=subprocess.Popen(list(map(str,command)),cwd=repo,env=env,
                                  stdout=stream,stderr=subprocess.STDOUT)
            while proc.poll() is None:
                state['progress']['last_log']=log.read_text(errors='replace')[-1800:]
                save()
                time.sleep(10)
        state['progress']['returncode']=proc.returncode
        save()
        return proc.returncode
    ports={}
    if a.port32:
        ports[32]=a.port32.resolve()
    def port_for(modes):
        if modes in ports:
            return ports[modes]
        settings=model.load(work/'m24-tail-settings.json')
        settings['modes']=modes
        while int(settings['quadrature'])<=4*modes*int(settings['spacing']):
            settings['quadrature']*=2
        config=out/('tail-M%d.json'%modes)
        config.write_text(json.dumps(settings,indent=2)+'\n')
        port=out/('port-M%d.json'%modes)
        code=invoke('export-M%d'%modes,[sys.executable,
            scripts/'resume_m3/recovered_q021/export_original_worker_port.py',
            '--source-topic',work/'shared-source','--config',config,'--out',port])
        if code:
            raise RuntimeError('Actual original physical port export failed')
        ports[modes]=port
        return port
    try:
        source=model.load(source_run)
        if source.get('model_kind')!=model.KIND:
            if source.get('model_kind')!='warm-supported-material-phase-fixed-metric-v3':
                raise ValueError('The new finite family starts only from its accepted zero-control v3 anchor')
            conversion=out/'reexpressed-anchor'
            code=invoke('zero-control-reexpression',[sys.executable,
                current/'warm_zero_control_reexpression_v4.py','--source-run',source_run,
                '--outdir',conversion])
            path=conversion/'run.json'
            converted=model.load(path) if path.exists() else {}
            row=dict(kind='coordinate_reexpression',run=str(path),returncode=code,
                solver_invoked=False,accepted=bool(converted.get('finite_linear_candidate_pass')),
                error=converted.get('error'))
            state['stages'].append(row);save()
            if code:
                state['status']='zero_control_reexpression_failed';save();return code
            source_run=path
        source=model.accepted_input(source_run)
        ports[source['modes']]=Path(source['linear_port_path'])
        accepted_run=source_run
        accepted_lambda=float(source['homotopy'])
        modes=int(source['modes'])
        levels=sorted(set([modes,*[m for m in a.mode_levels if m>=modes]]))
        targets=[value for value in a.targets if value>accepted_lambda]
        if accepted_lambda<1. and (not targets or targets[-1]!=1.):
            targets.append(1.)
        state['result']=dict(last_accepted_run=str(accepted_run),accepted_lambda=accepted_lambda,
            source_acceptance_kind=source['acceptance_kind'],lambda_one_reached=accepted_lambda==1.,
            fixed_lambda_C2_refinement_paid=False,actual_nonlinear_tail_paid=False)
        save()
        attempt=0
        while targets:
            if attempt>=a.max_attempts:
                state['status']='explicit_continuation_attempt_limit';save();return 2
            target=targets[0]
            name='attempt-%03d'%attempt;attempt+=1
            destination=out/name
            command=[sys.executable,current/'warm_fixed_m3_step_v4.py',
                '--source-run',accepted_run,'--outdir',destination,'--homotopy',target,
                '--modes',modes,'--angular',max(source['angular'],32*modes),
                '--port',port_for(modes),'--max-nodes',a.max_nodes,
                '--tol',source['gates']['tol'],'--bc-tol',source['gates']['bc_tol'],
                '--physical-bc-tol',source['gates']['physical_bc_tol']]
            code=invoke(name,command)
            path=destination/'run.json'
            record=model.load(path) if path.exists() else {}
            accepted=False
            acceptance_error=None
            if code==0:
                try:
                    model.accepted_input(path)
                    accepted=True
                except Exception as error:
                    acceptance_error=repr(error)
            raw=record.get('raw_return',{})
            row=dict(kind='actual_warm_bvp',name=name,source_run=str(accepted_run),
                homotopy=target,modes=modes,run=str(path),
                run_sha256=model.sha(path) if path.exists() else None,returncode=code,
                accepted=accepted,solver_invoked=record.get('solver_invoked'),
                solver_success=record.get('solver_success'),error=record.get('error') or acceptance_error,
                raw=dict(file=raw.get('file'),sha256=raw.get('sha256'),success=raw.get('success'),
                    status=raw.get('status'),nodes=raw.get('nodes'),rms=raw.get('rms')),
                scaled_bc_max=record.get('original_scaled_bc_max'),
                physical_bc_max=record.get('linear_dn_physical_bc_max'),
                domain_newton_stats=record.get('domain_newton_stats'),
                auxiliary_domain_guard=record.get('auxiliary_domain_guard'),
                metric_diagnostics=record.get('metric_diagnostics'))
            state['stages'].append(row)
            state['result']['last_attempt']=row
            save()
            if accepted:
                accepted_run=path
                accepted_lambda=float(target)
                source=record
                targets.pop(0)
                state['result'].update(last_accepted_run=str(accepted_run),
                    accepted_lambda=accepted_lambda,lambda_one_reached=accepted_lambda==1.)
                save()
                continue
            # A completed successful solve with correct boundary and an
            # actual metric report is the only automatic mode-enlargement case.
            metric_values=[item[key] for item in record.get('metric_diagnostics',[])
                           for key in ('legacy_max_component_fft_l1','sample_operator_max')]
            finite_metric_report=bool(metric_values) and all(
                isinstance(value,(int,float)) and math.isfinite(value) and value>=0
                for value in metric_values)
            only_metric=(record.get('status')=='audited_finite_linear_candidate' and
                not record.get('error') and record.get('solver_success') and raw.get('success') and
                raw.get('status')==0 and finite_metric_report and
                raw.get('rms',math.inf)<=source['gates']['tol'] and
                record.get('original_scaled_bc_max',math.inf)<=source['gates']['bc_tol'] and
                record.get('linear_dn_physical_bc_max',math.inf)<=source['gates']['physical_bc_tol'] and
                any(value>1e-6 for value in metric_values))
            larger=[value for value in levels if value>modes]
            if only_metric and larger:
                modes=larger[0]
                row['next_action']='retry_target_from_last_accepted_field_with_more_modes'
                save()
                continue
            distance=target-accepted_lambda
            if distance<=a.minimum_lambda_step:
                state['status']='actual_continuation_stalled_at_minimum_step'
                row['next_action']='no_failed_candidate_is_promoted'
                save();return 2
            midpoint=accepted_lambda+distance/2
            if midpoint==accepted_lambda or midpoint==target:
                state['status']='no_distinct_binary_lambda_midpoint';save();return 2
            targets.insert(0,midpoint)
            row['next_action']='bisect_lambda_from_last_accepted_field'
            row['next_lambda']=midpoint
            save()
        state['status']='actual_lambda_one_finite_linear_candidate'
        state['result'].update(last_accepted_run=str(accepted_run),accepted_lambda=accepted_lambda,
            lambda_one_reached=accepted_lambda==1.,fixed_lambda_C2_refinement_paid=False,
            actual_nonlinear_tail_paid=False,complete_surface=False)
        save();return 0
    except Exception as error:
        state.update(status='error',error=repr(error),traceback=traceback.format_exc())
        save();return 1


if __name__=='__main__':
    sys.exit(main())
