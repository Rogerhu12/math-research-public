#!/usr/bin/env python3
"""Run at most three actual original portable delta-design BVP attempts.

Copy the real source's solver command and keep its original gates and RMS
guard.  A zero-control reexpression is an independently verified initial
representation, never an invented successful solver return.  Only genuine
new finite passes become accepted anchors.  A metric-only failure may seed
the original complete-lift mode transfer.  This is not fixed-g refinement.
An optional saved metric-only return is a separate unaccepted solver seed;
the accepted anchor and lambda bracket remain those of its saved summary.
The optional existing streamed wrapper changes radial execution grouping,
not the original problem, resolution, tolerances or acceptance gates.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import copy
import json
import math
from pathlib import Path
import subprocess
import sys
import time
import traceback
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import warm_delta_phase_entry_v5 as entry


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','work','source-run','outdir'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--targets',type=float,nargs='+',
        default=[.004,.008,.016,.032,.064,.128,.256,.512,.75,1.])
    parser.add_argument('--mode-levels',type=int,nargs='+',default=[24,32,40,48,64,80,96,128])
    parser.add_argument('--max-attempts',type=int,default=3)
    parser.add_argument('--minimum-lambda-step',type=float,default=1e-5)
    parser.add_argument('--phase-scale',type=float,default=1.)
    parser.add_argument('--tail-settings',type=Path)
    parser.add_argument('--resume-metric-summary',type=Path,
        help='Resume only a saved metric-only budget return; retain its exact pending targets and accepted anchor')
    parser.add_argument('--streamed-rhs-block',type=int,
        help='Use the existing streamed/released-LU wrapper with this positive radial block')
    args=parser.parse_args()
    repo=args.repo.resolve();work=args.work.resolve();out=args.outdir.resolve()
    source=args.source_run.resolve()
    if work not in out.parents or work not in source.parents:
        raise ValueError('Actual fields must remain inside the declared runner work directory')
    if args.resume_metric_summary and work not in args.resume_metric_summary.resolve().parents:
        raise ValueError('The saved actual summary must remain in the declared work directory')
    if (not 1<=args.max_attempts<=3 or
            not all(math.isfinite(v) and 0<v<=1 for v in args.targets) or
            args.targets!=sorted(set(args.targets)) or
            args.mode_levels!=sorted(set(args.mode_levels)) or
            not all(v>0 for v in args.mode_levels) or
            not math.isfinite(args.minimum_lambda_step) or args.minimum_lambda_step<=0 or
            (args.streamed_rhs_block is not None and args.streamed_rhs_block<1)):
        raise ValueError('Use increasing physical lambda/mode targets and at most three actual attempts')
    out.mkdir(parents=True,exist_ok=False)
    scripts=repo/'topics/visible-flex-held-10pct/scripts'
    resume=scripts/'resume_m3'
    wrapper=scripts/'resume_20261126/streamed_release_prefix_driver.py'
    state=dict(scope=__doc__,status='preparing',stages=[],progress={},result={},
        source_run=str(source),source_run_sha256=entry.sha(source),
        source_hashes={str(HERE/name):entry.sha(HERE/name) for name in
            ('warm_delta_phase_factory_v5.py','warm_delta_phase_entry_v5.py',
             'warm_delta_phase_continue_v5.py')},
        model_kind=entry.KIND,fixed_metric=False,fixed_metric_refinement=False,
        actual_tail_requested=False,complete_surface=False,max_actual_attempts=args.max_attempts)
    if args.streamed_rhs_block is not None:
        state['source_hashes'][str(wrapper)]=entry.sha(wrapper)
        state['execution_policy']=dict(streamed_rhs_block=args.streamed_rhs_block,
            wrapper=str(wrapper),wrapper_sha256=entry.sha(wrapper),
            original_driver_sha256=entry.sha(resume/'portable_prefix_continue.py'),
            original_resolution_and_gates_unchanged=True,
            floating_point_bit_identity_claimed=False)
    summary=out/'summary.json'
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',
        MKL_NUM_THREADS='1',PYTHONUNBUFFERED='1',VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
        VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
            'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
    for key in ('LD_LIBRARY_PATH','LD_PRELOAD'):
        env.pop(key,None)
    def save():
        entry.write(summary,state)
    def invoke(name,command):
        command=list(map(str,command))
        state.update(status=name,progress=dict(command=command))
        save()
        log=out/(name+'.log')
        with log.open('x') as stream:
            process=subprocess.Popen(command,cwd=repo,env=env,stdout=stream,stderr=subprocess.STDOUT)
            while process.poll() is None:
                with log.open('rb') as reader:
                    reader.seek(max(0,log.stat().st_size-4096))
                    text=reader.read().decode('utf-8',errors='replace')
                # Do not copy raw-return parameter vectors into the public
                # small projection. Only solver progress table lines survive.
                lines=[line for line in text.splitlines() if not line.lstrip().startswith('{')]
                state['progress']['last_solver_log']='\n'.join(lines[-3:])[-1500:]
                save();time.sleep(15)
        state['progress']['returncode']=process.returncode;save()
        return process.returncode
    ports={}
    def enlarged_port(M,seed):
        if M in ports:
            return ports[M]
        base=args.tail_settings or work/'m24-tail-settings.json'
        settings=dict(entry.load(base),modes=M)
        while int(settings['quadrature'])<=4*M*int(settings['spacing']):
            settings['quadrature']*=2
        config=out/('tail-M%d.json'%M);entry.write(config,settings)
        port=out/('port-M%d.json'%M)
        code=invoke('export-M%d'%M,[sys.executable,
            resume/'recovered_q021/export_original_worker_port.py',
            '--source-topic',work/'shared-source','--config',config,'--out',port])
        if code:
            raise RuntimeError('Original enlarged linear-port exporter failed')
        ports[M]=port
        return port
    def transfer(seed_path,seed,M,attempt):
        # This original entry requires a REAL successful source solver, so
        # it is deliberately never called on the zero-solve reexpression.
        if seed.get('acceptance_kind')!=entry.SOLVER_RETURN or not entry.gate_checks(seed)['solver_and_boundary_pass']:
            raise ValueError('Mode transfer requires an actual solver/boundary return, not a reexpression')
        entry.artifact_data(seed_path,seed)
        port=enlarged_port(M,seed);directory=out/(attempt+'-transfer')
        code=invoke(attempt+'-transfer',[sys.executable,resume/'prepare_lifted_mode_restart.py',
            '--source-run',seed_path,'--modes',M,'--port',port,
            '--angular',32*M,'--outdir',directory])
        if code:
            raise RuntimeError('Original complete exact-lift transfer failed')
        report=entry.load(directory/'transfer.json');result=report['result']
        raw_path=Path(result['initial_raw'])
        if entry.sha(raw_path)!=result['initial_raw_sha256'] or report['exact_lift_coefficient']!=1:
            raise ValueError('Transferred nodal field or complete lift coefficient changed')
        phase_report=directory/'actual-phase-embedding.json'
        code=invoke(attempt+'-phase-inspection',[sys.executable,HERE/'warm_delta_phase_entry_v5.py',
            '--repo',repo,'--source-run',seed_path,'--inspect-transfer',directory/'transfer.json',
            '--out-report',phase_report])
        if code:
            raise ValueError('The actual complete-anchor/phase input inspection failed')
        phase_diagnostic=entry.load(phase_report)
        state['progress']['v5_phase_embedding']=phase_diagnostic
        state['result'].setdefault('transfers',[]).append(dict(attempt=attempt,**phase_diagnostic))
        save()
        return raw_path,Path(result['port'])

    def metric_resume(current_path,current):
        previous_path=args.resume_metric_summary.resolve()
        previous=entry.load(previous_path)
        prior=previous.get('result') or {};last=prior.get('last_attempt') or {}
        if (previous.get('model_kind')!=entry.KIND or
                previous.get('status')!='actual_attempt_budget_returned' or
                not previous.get('stages') or previous['stages'][-1]!=last or
                last.get('metric_only_failure') is not True or last.get('accepted') is not False or
                last.get('complete_saved_initializer') is not True or last.get('returncode')!=0 or
                Path(prior['last_accepted_run']).resolve()!=current_path):
            raise ValueError('Use the saved metric-only budget return and its unchanged accepted anchor')
        seed_path=Path(last['run']).resolve()
        if work not in seed_path.parents or entry.sha(seed_path)!=last.get('run_sha256'):
            raise ValueError('The saved real metric-only solver return changed')
        seed=entry.actual_input(seed_path,require_metric=False)
        settings=seed.get('core_settings') or {}
        if (seed.get('model_kind')!=entry.KIND or
                seed.get('acceptance_kind')!=entry.SOLVER_RETURN or
                seed.get('solver_invoked') is not True or
                seed.get('finite_linear_candidate_pass') is not False or
                settings.get('model_kind')!=entry.KIND or settings.get('fixed_metric') is not False or
                settings.get('phase_parameter_scale_rule')!=entry.factory_module.SCALE_RULE or
                Path(entry.option(seed,'--core-module')).resolve()!=HERE/'warm_delta_phase_factory_v5.py' or
                entry.load(entry.option(seed,'--core-config'))!=settings):
            raise ValueError('The unaccepted seed lacks the original v5 solver/provider semantics')
        entry.factory_module.checked_provider(settings)
        metric=seed['prefix_audit']['metric_l1']
        if not entry.finite(metric) or metric<=1e-6:
            raise ValueError('This narrow resume requires a finite metric-only failure')
        for key in ('physical_profile','physical_tail_parameters','physical_tail_cut',
                    'angular_chart','gauge_q','warp_reference','origin_design_run','origin_design_sha256'):
            if seed.get(key)!=current.get(key):
                raise ValueError('The metric seed changed the declared design input: '+key)
        if ({k:v for k,v in settings.items() if k!='homotopy'}!=
                {k:v for k,v in current['core_settings'].items() if k!='homotopy'}):
            raise ValueError('The complete v5 anchor, phase family or scale changed')
        accepted_lambda=float(current['core_settings']['homotopy'])
        pending=prior.get('pending_targets')
        if (not isinstance(pending,list) or not pending or
                not all(isinstance(v,(int,float)) and math.isfinite(v) and accepted_lambda<v<=1 for v in pending) or
                pending!=sorted(set(pending)) or prior.get('accepted_lambda')!=accepted_lambda or
                pending[0]!=settings['homotopy'] or last.get('homotopy')!=pending[0] or
                last.get('modes')!=seed['modes'] or
                last.get('raw_sha256')!=seed['raw_return']['sha256'] or
                last.get('physical_sha256')!=seed['physical_sha256']):
            raise ValueError('The exact pending target, actual seed or accepted lambda bracket changed')
        if '--targets' in sys.argv and args.targets!=pending:
            raise ValueError('A metric resume retains the complete saved pending-target list')
        larger=[v for v in args.mode_levels if v>seed['modes']]
        if not larger:
            raise ValueError('The saved metric-only seed needs a declared larger mode count')
        record=dict(summary=str(previous_path),summary_sha256=entry.sha(previous_path),
            previous_controller_source_hashes=copy.deepcopy(previous.get('source_hashes',{})),
            current_controller_sha256=entry.sha(__file__),
            accepted_anchor=dict(run=str(current_path),run_sha256=entry.sha(current_path),
                homotopy=accepted_lambda,acceptance_kind=current['acceptance_kind']),
            unaccepted_solver_seed=dict(run=str(seed_path),run_sha256=entry.sha(seed_path),
                raw_sha256=seed['raw_return']['sha256'],physical_sha256=seed['physical_sha256'],
                homotopy=settings['homotopy'],modes=seed['modes'],metric=metric,
                acceptance_kind=entry.SOLVER_RETURN,finite_linear_candidate_pass=False),
            next_modes=larger[0],pending_targets=copy.deepcopy(pending),
            target_source='unchanged_saved_pending_targets',
            seed_promoted_to_accepted_anchor=False,prior_solver_attempt_repeated=False)
        state['metric_resume']=record
        return seed_path,seed,larger[0],pending

    def numerical_command(command):
        command=list(map(str,command))
        if args.streamed_rhs_block is None:
            return command
        if len(command)<2 or Path(command[1]).resolve()!=resume/'portable_prefix_continue.py':
            raise ValueError('The streamed wrapper must call the recorded original portable driver')
        return [sys.executable,str(wrapper),'--rhs-block',str(args.streamed_rhs_block),*command[2:]]

    def execution_record(name,command,executed,directory):
        value=dict(actual_argv=executed,original_portable_argv=list(map(str,command)),
            wrapper_invoked=args.streamed_rhs_block is not None,
            controller_sha256=entry.sha(__file__),original_portable_command_fabricated=False)
        if args.streamed_rhs_block is not None:
            provenance=directory/'radial-batching.json'
            data=entry.load(provenance)
            if (data.get('command')!=executed[1:] or
                    data.get('wrapper_sha256')!=entry.sha(wrapper) or
                    data.get('original_driver_sha256')!=entry.sha(resume/'portable_prefix_continue.py') or
                    data.get('radial_rhs_jacobian_block')!=args.streamed_rhs_block or
                    data.get('mathematical_parameters_changed') is not False or
                    data.get('original_gates_relaxed') is not False):
                raise ValueError('The actual streamed-wrapper execution provenance changed')
            value.update(wrapper=str(wrapper),wrapper_sha256=entry.sha(wrapper),
                streamed_rhs_block=args.streamed_rhs_block,
                provenance=str(provenance),provenance_sha256=entry.sha(provenance),
                floating_point_bit_identity_claimed=False)
        path=out/(name+'-execution.json');entry.write(path,value)
        return value,dict(record=str(path),record_sha256=entry.sha(path),
            wrapper_invoked=value['wrapper_invoked'],
            streamed_rhs_block=value.get('streamed_rhs_block'),
            wrapper_sha256=value.get('wrapper_sha256'),provenance_sha256=value.get('provenance_sha256'))
    try:
        if args.resume_metric_summary and entry.load(source).get('model_kind')!=entry.KIND:
            raise ValueError('A metric resume must use its already verified v5 accepted anchor')
        if entry.load(source).get('model_kind')==entry.KIND:
            current_path=source;current=entry.accepted_input(source)
        else:
            code=invoke('zero-control-reexpression',[sys.executable,HERE/'warm_delta_phase_entry_v5.py',
                '--repo',repo,'--source-run',source,'--outdir',out/'zero-control',
                '--phase-scale',args.phase_scale])
            if code:
                state['status']='zero_control_reexpression_failed';save();return 2
            current_path=out/'zero-control/run.json';current=entry.accepted_input(current_path)
        accepted_lambda=float(current['core_settings']['homotopy'])
        targets=[v for v in args.targets if v>accepted_lambda]
        seed_path,seed=current_path,current
        M=int(current['modes'])
        if args.resume_metric_summary:
            seed_path,seed,M,targets=metric_resume(current_path,current)
        state['result']=dict(last_accepted_run=str(current_path),accepted_lambda=accepted_lambda,
            new_actual_solver_passes=0,full_nonlinear_tail_paid=False,complete_surface=False)
        if args.resume_metric_summary:
            state['result']['initial_unaccepted_solver_seed']=copy.deepcopy(
                state['metric_resume']['unaccepted_solver_seed'])
            state['result']['resumed_next_modes']=M
        attempts=0
        while targets and attempts<args.max_attempts:
            target=targets[0];name='attempt-%03d'%attempts;directory=out/name
            raw=seed_path.parent/seed['raw_return']['file'];port=Path(entry.option(seed,'--port'))
            if entry.sha(raw)!=seed['raw_return']['sha256']:
                raise ValueError('Actual raw seed changed')
            if M>int(seed['modes']):
                raw,port=transfer(seed_path,seed,M,name)
            settings=copy.deepcopy(seed['core_settings']);settings['homotopy']=target
            config=out/(name+'-core.json');entry.write(config,settings)
            command=entry.raw_command(seed,raw,HERE/'warm_delta_phase_factory_v5.py',config,directory)
            for flag,value in (('--port',port),('--modes',M),('--angular',max(int(seed['angular']),32*M))):
                entry.replace_option(command,flag,value)
            attempts+=1
            executed=numerical_command(command)
            code=invoke(name,executed)
            path=directory/'run.json';returned=entry.load(path) if path.exists() else {}
            checks=entry.gate_checks(returned);artifact_error=None;complete=False
            execution=None;execution_summary=None
            try:
                execution,execution_summary=execution_record(name,command,executed,directory)
                if returned.get('command')!=list(map(str,command)):
                    raise ValueError('The real portable driver did not record the expected literal command')
                entry.verify_bindings(returned);entry.artifact_data(path,returned)
                if (returned['core_settings']!=settings or
                        any(returned[k]!=seed[k] for k in ('physical_profile','physical_tail_parameters',
                            'physical_tail_cut','angular_chart','gauge_q','warp_reference'))):
                    raise ValueError('The actual solver changed a declared design input')
                complete=True
            except Exception as error:
                artifact_error=repr(error)
            accepted=bool(code==0 and complete and checks['solver_and_boundary_pass'] and checks['metric'])
            metric=(returned.get('prefix_audit') or {}).get('metric_l1')
            metric_only=bool(code==0 and complete and checks['solver_and_boundary_pass'] and
                entry.finite(metric) and metric>1e-6)
            if path.exists():
                raw_row=returned.get('raw_return') or {}
                raw_file=path.parent/raw_row.get('file','missing-actual-raw')
                has_return=bool(raw_row.get('sha256') and raw_file.is_file() and
                                entry.sha(raw_file)==raw_row['sha256'])
                # These annotations do not replace or invent ANY solver
                # success/status/residual field from the real driver return.
                returned.update(model_kind=entry.KIND,
                    acceptance_kind=(entry.SOLVER_RETURN if has_return else
                        'original_portable_driver_attempt_without_saved_solver_return'),
                    driver_invoked=True,solver_invoked=True if has_return else None,
                    finite_linear_candidate_pass=accepted,
                    fixed_metric=False,fixed_metric_refinement=False,
                    parameter_zero_meaning=entry.factory_module.SCALE_RULE['parameter_zero'],
                    origin_design_run=current['origin_design_run'],
                    origin_design_sha256=current['origin_design_sha256'],
                    source_seed_run=str(seed_path),source_seed_run_sha256=entry.sha(seed_path),
                    actual_audit_mean_nodes=(returned.get('prefix_audit') or {}).get('samples_psi'),
                    scope_v5='Actual original fixed=False solver; delta designs g, d1 remains zero; no nonlinear tail or fixed-g refinement paid')
                if execution is not None:
                    returned['execution_provenance']=execution
                    returned['execution_record']=execution_summary
                    if args.streamed_rhs_block is not None:
                        returned.setdefault('source_hashes',{})[str(wrapper)]=entry.sha(wrapper)
                entry.write(path,returned)
            if accepted:
                entry.accepted_input(path)
                current_path,current=path,returned;accepted_lambda=target
                state['result']['new_actual_solver_passes']+=1
            raw_result=returned.get('raw_return') or {};audit=returned.get('prefix_audit') or {}
            row=dict(name=name,homotopy=target,modes=M,accepted=accepted,metric_only_failure=metric_only,
                run=str(path),run_sha256=entry.sha(path) if path.exists() else None,returncode=code,
                solver_success=returned.get('solver_success'),raw_status=raw_result.get('status'),
                nodes=raw_result.get('nodes'),rms=raw_result.get('rms'),metric=metric,
                physical_bc_max=audit.get('physical_bc_max'),actual_audit_mean_nodes=audit.get('samples_psi'),
                raw_sha256=raw_result.get('sha256'),physical_sha256=returned.get('physical_sha256'),
                actual_delta=(returned.get('frozen_profile') or {}).get('delta'),
                error=returned.get('error'),artifact_error=artifact_error,
                original_finite_checks=checks,complete_saved_initializer=complete,
                execution=execution_summary,
                domain_newton_stats=returned.get('domain_newton_stats'),
                domain_error_counts=returned.get('domain_error_counts'))
            state['stages'].append(row)
            state['result'].update(last_attempt=row,last_accepted_run=str(current_path),
                accepted_lambda=accepted_lambda,actual_attempts=attempts)
            save()
            if accepted:
                targets.pop(0);seed_path,seed=current_path,current
            elif metric_only:
                larger=[v for v in args.mode_levels if v>M]
                if not larger:
                    state['status']='design_requires_more_modes';save();return 2
                seed_path,seed=path,returned;M=larger[0]
            else:
                step=(target-accepted_lambda)/2
                if step<args.minimum_lambda_step:
                    state['status']='design_step_failed';save();return 2
                targets.insert(0,accepted_lambda+step)
                seed_path,seed=current_path,current
                # Do not route a no-solve anchor through a solver-only lift.
                M=int(current['modes'])
        state['status']=('requested_finite_design_targets_passed' if not targets else
                         'actual_attempt_budget_returned')
        state['result']['pending_targets']=targets
        save();return 0 if not targets else 2
    except Exception as error:
        state.update(status='v5_entry_error',error=repr(error),exception=traceback.format_exc())
        save();return 1


if __name__=='__main__':
    sys.exit(main())
