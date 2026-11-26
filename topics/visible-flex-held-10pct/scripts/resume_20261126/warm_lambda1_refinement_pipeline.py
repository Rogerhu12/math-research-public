#!/usr/bin/env python3
"""Three actual refinements triggered only by an accepted warm lambda=1 field.

This preserves one complete warm core definition, actual delta/profile,
linear-DN physical tail, material chart, gauge and mean1168. Three accepted
finite fields and observed C2 differences do not prove a Cauchy limit. The
original nonlinear tail, closed geometry and full-time conditions remain
unpaid. No smaller-lambda or rejected field triggers any solve or port job.
"""
import argparse
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback

KIND='warm-supported-material-phase-fixed-metric'
PROBLEM_KEYS=('model_kind','warm_definition','warm_provider_sha256',
    'frozen_profile','physical_tail_parameters','physical_tail_cut',
    'angular_chart','gauge_q','warp_reference','mean_nodes','bc_normalization',
    'terminal_kind','parameter_zero_meaning','frozen_source_signature',
    'origin_design_sha256')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def problem(record):
    return {key:copy.deepcopy(record[key]) for key in PROBLEM_KEYS}


def require_lambda1(record):
    if (record.get('model_kind')!=KIND or record.get('homotopy')!=1. or
            record.get('warm_definition',{}).get('homotopy')!=1.):
        raise ValueError('Only the declared warm family at literal lambda=1 triggers refinement')
    if (not record.get('fixed_metric') or record.get('fixed_core') is not False or
            record.get('terminal_kind')!='original_linear_dn' or
            record.get('parameter_zero_meaning')!='log(q_aux/gauge_q)'):
        raise ValueError('The source fixed-metric/linear-DN/auxiliary-coordinate contract differs')
    if (record.get('actual_tail_requested') or record.get('original_actual_nonlinear_tail') or
            record.get('mean_nodes')!=1168 or record.get('bc_normalization')!=.02):
        raise ValueError('This pipeline preserves the original linear DN and declared mean1168')
    if (record.get('status')!='audited_finite_linear_candidate' or record.get('error') or
            not record.get('solver_success') or not record.get('finite_linear_candidate_pass') or
            not record.get('raw_return',{}).get('success') or not record.get('physical_sha256')):
        raise ValueError('A real accepted raw return and physical C2 export are required')
    gates=record['gates']
    for field,gate in (('original_scaled_bc_max','bc_tol'),
                       ('linear_dn_physical_bc_max','physical_bc_tol')):
        value=record.get(field)
        if not isinstance(value,(int,float)) or not math.isfinite(value) or value>gates[gate]:
            raise ValueError('The accepted flag lacks its actual boundary gate: '+field)
    rms=record['raw_return'].get('rms')
    if not isinstance(rms,(int,float)) or not math.isfinite(rms) or rms>gates['tol']:
        raise ValueError('The actual RMS does not satisfy the declared tolerance')
    rows=record.get('metric_diagnostics')
    if not rows:
        raise ValueError('Missing actual full-relative finite metric diagnostics')
    for row in rows:
        if int(row.get('angular',0))<16*(3*int(record['modes'])+1):
            raise ValueError('A finite angular audit omitted the original resolution floor')
        for key in ('legacy_max_component_fft_l1','sample_operator_max'):
            if not isinstance(row.get(key),(int,float)) or not math.isfinite(row[key]) or row[key]>1e-6:
                raise ValueError('An actual finite metric gate did not pass')
    return problem(record)


def verify_field(path,record):
    raw=path.parent/record['raw_return']['file']
    physical=path.parent/'physical.npz'
    if sha(raw)!=record['raw_return']['sha256'] or sha(physical)!=record['physical_sha256']:
        raise ValueError('An actual raw/physical field changed')
    port=Path(record['linear_port_path'])
    if sha(port)!=record['linear_port_sha256']:
        raise ValueError('The actual numerical port bytes changed')
    origin=Path(record['origin_design_run'])
    if sha(origin)!=record['origin_design_sha256']:
        raise ValueError('The fixed branch source identity changed')


def metric_max(record):
    return {key:max(row[key] for row in record['metric_diagnostics']) for key in
            ('legacy_max_component_fft_l1','sample_operator_max')}


def pair_trend(comparisons):
    """Two modal differences on the same declared angular grids; no theorem."""
    modal=[row for row in comparisons if row['kind']=='modal_increment' and row.get('status')=='evaluated']
    if len(modal)!=2:
        return dict(available=False,C2_convergence_proven=False)
    left,right=modal
    a={row['angular']:row for row in left['rows']}
    b={row['angular']:row for row in right['rows']}
    if set(a)!=set(b):
        raise ValueError('Modal comparison angular grids differ')
    rows=[]
    for angular in sorted(a):
        da,db=(x[angular]['sampled_complete_C2_jet_difference'] for x in (a,b))
        ratios={key:(db[key]/da[key] if da[key]>0 else None) for key in da}
        rows.append(dict(angular=angular,first_modal_difference=da,second_modal_difference=db,
                         ratios=ratios,each_jet_nonincreasing=all(db[key]<=da[key] for key in da),
                         max_jet_strictly_decreased=max(db.values())<max(da.values())))
    ca,cb=(x['phase_control_literal_distances'] for x in modal)
    return dict(available=True,rows=rows,
        phase_control_difference_first=ca,phase_control_difference_second=cb,
        all_sampled_maxima_strictly_decreased=all(row['max_jet_strictly_decreased'] for row in rows),
        radial_sample_scope='Each pair uses both actual meshes, their midpoints and the same uniform grid',
        observed_finite_comparison_only=True,continuous_C2_bound_certified=False,
        C2_convergence_proven=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('repo','work','source-run','outdir'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--mode-levels',type=int,nargs=3,
                   help='Default: actual source M, M+8, M+16; first level must retain source M')
    p.add_argument('--compare-angular',type=int,nargs='+')
    p.add_argument('--max-nodes',type=int,default=6000)
    p.add_argument('--jac-batch',type=int,default=8)
    a=p.parse_args()
    repo,work,out=a.repo.resolve(),a.work.resolve(),a.outdir.resolve()
    source_path=a.source_run.resolve()
    if work not in source_path.parents or work not in out.parents or repo in out.parents or repo==out:
        raise ValueError('Actual fields and generated arrays must stay under work outside the repository')
    if a.max_nodes<1 or a.jac_batch<1:
        raise ValueError('Positive solver budget and Jacobian batch required')
    out.mkdir(parents=True,exist_ok=False)
    begin=time.monotonic()
    scripts=repo/'topics/visible-flex-held-10pct/scripts'
    current=scripts/'resume_20261126'
    driver=current/'warm_fixed_m3_step.py'
    compare=current/'warm_fixed_m3_compare_c2.py'
    summary=out/'summary.json'
    state=dict(scope=__doc__,status='checking_lambda1_trigger',stages=[],comparisons=[],progress={},
        result=dict(C2_convergence_proven=False,complete_surface=False),
        command=[sys.executable,*sys.argv],fixed_metric=True,fixed_metric_refinement=True,
        fixed_metric_design_continuation=False,mean_nodes=1168,homotopy=1.,
        complete_surface=False,source_run=str(source_path))
    def save():
        state['elapsed']=time.monotonic()-begin
        state['progress']['accepted_stages']=sum(x.get('accepted',False) for x in state['stages'])
        state['progress']['comparisons_evaluated']=sum(x.get('status')=='evaluated' for x in state['comparisons'])
        full=out/'pipeline.json'
        full_tmp=full.with_suffix('.tmp')
        full_tmp.write_text(json.dumps(state,indent=2,allow_nan=False)+'\n')
        full_tmp.replace(full)
        stages=[]
        for item in state['stages']:
            row={key:value for key,value in item.items() if key!='raw_return'}
            row['raw_return']={key:value for key,value in (item.get('raw_return') or {}).items()
                               if key!='parameters'}
            stages.append(row)
        comparisons=[]
        for item in state['comparisons']:
            row={key:item[key] for key in ('kind','status','file','sha256',
                 'observed_height_quadrature_change') if key in item}
            row['rows']=[dict(angular=r['angular'],
                jets=r['sampled_complete_C2_jet_difference'],core=r['sampled_core_C2_difference'])
                for r in item.get('rows',[])]
            row['phase_l1']={key:value['decimal'] for key,value in
                             item.get('phase_control_literal_distances',{}).items()}
            comparisons.append(row)
        result=copy.deepcopy(state['result'])
        trend=result.get('modal_trend',{})
        for key in ('phase_control_difference_first','phase_control_difference_second'):
            if key in trend:
                trend[key]={k:v['decimal'] for k,v in trend[key].items()}
        result['comparisons']=comparisons
        result['full_record']=str(full)
        compact=dict(scope=__doc__,status=state['status'],stages=stages,
            progress=state['progress'],result=result,error=state.get('error'),
            elapsed=state['elapsed'],homotopy=1.,mean_nodes=1168,complete_surface=False)
        temp=summary.with_suffix('.tmp')
        temp.write_text(json.dumps(compact,indent=2,allow_nan=False)+'\n')
        temp.replace(summary)
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',
             MKL_NUM_THREADS='1',PYTHONUNBUFFERED='1',
             VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
             VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
                 'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
    for key in ('LD_LIBRARY_PATH','LD_PRELOAD'):
        env.pop(key,None)
    def invoke(name,command):
        state['status']=name
        state['progress'].update(command=list(map(str,command)),active=name)
        save()
        log=out/(name+'.log')
        with log.open('x') as stream:
            process=subprocess.Popen(list(map(str,command)),cwd=repo,env=env,
                stdout=stream,stderr=subprocess.STDOUT)
            while process.poll() is None:
                state['progress']['last_log']=log.read_text(errors='replace')[-1600:]
                save()
                time.sleep(15)
        state['progress']['returncode']=process.returncode
        save()
        return process.returncode
    save()
    try:
        initial=load(source_path)
        try:
            contract=require_lambda1(initial)
            verify_field(source_path,initial)
        except Exception as error:
            state.update(status='not_triggered_source_not_accepted_warm_lambda1',error=repr(error))
            save()
            return 2
        for file in (driver,compare,current/'warm_fixed_m3_model.py',current/'warm_supported_core_factory.py'):
            if not file.is_file():
                raise ValueError('Missing declared warm numerical source: '+str(file))
        if sha(current/'warm_supported_core_factory.py')!=initial['warm_provider_sha256']:
            raise ValueError('The warm core definition source changed')
        modes=int(initial['modes'])
        levels=a.mode_levels or [modes,modes+8,modes+16]
        if not levels[0]==modes<levels[1]<levels[2]:
            raise ValueError('Three levels must be source M followed by two genuine modal increments')
        maximum_floor=16*(3*levels[-1]+1)
        comparison_angles=sorted({max(maximum_floor,int(n)) for n in
            (a.compare_angular or [maximum_floor,2*maximum_floor])})
        definitions=[]
        for index,(level,tol,bc,refine) in enumerate(zip(levels,[1e-8,1e-9,1e-10],
                                                       [1e-9,1e-10,1e-11],[2,1,1])):
            bc=min(bc,initial['gates']['bc_tol'],initial['gates']['physical_bc_tol']/.02)
            floor=16*(3*level+1)
            definitions.append(dict(name='level-%d-M%d'%(index+1,level),modes=level,
                angular=max(int(initial['angular']),64*level if index<2 else 96*level),
                refine=refine,tol=min(tol,initial['gates']['tol']),bc_tol=bc,
                physical_bc_tol=.02*bc,audit_angular=[floor,2*floor]))
        state.update(status='accepted_lambda1_triggered',source_run_sha256=sha(source_path),
            fixed_problem=contract,definitions=definitions,compare_angular=comparison_angles,
            source_hashes={str(file):sha(file) for file in
                (Path(__file__),driver,compare,current/'warm_fixed_m3_model.py',
                 current/'warm_supported_core_factory.py')},
            initial_metric=metric_max(initial),expected_stages=3,
            expected_modal_increments=2,linear_dn_only=True)
        save()
        ports={modes:Path(initial['linear_port_path'])}
        def port_for(level):
            if level in ports:
                return ports[level]
            settings=load(work/'m24-tail-settings.json')
            settings['modes']=level
            while int(settings['quadrature'])<=4*level*int(settings['spacing']):
                settings['quadrature']*=2
            config=out/('tail-M%d.json'%level)
            config.write_text(json.dumps(settings,indent=2)+'\n')
            port=out/('port-M%d.json'%level)
            code=invoke('export-M%d'%level,[sys.executable,
                scripts/'resume_m3/recovered_q021/export_original_worker_port.py',
                '--source-topic',work/'shared-source','--config',config,'--out',port])
            if code:
                raise RuntimeError('Original higher-mode port exporter failed')
            value=load(port)
            value['cut']['_prefix_bridge']=contract['frozen_profile']['prefix_bridge']
            if value['parameters']!=contract['physical_tail_parameters'] or value['cut']!=contract['physical_tail_cut']:
                raise ValueError('A higher numerical port changed the physical tail metric')
            ports[level]=port
            return port
        previous=source_path
        previous_record=initial
        for index,definition in enumerate(definitions):
            name=definition['name']
            directory=out/name
            command=[sys.executable,driver,'--source-run',previous,'--outdir',directory,
                '--homotopy',1,'--modes',definition['modes'],'--angular',definition['angular'],
                '--port',port_for(definition['modes']),'--refine',definition['refine'],
                '--mean-nodes',1168,'--phase-scale',contract['warm_definition']['phase_control_scale'],
                '--tol',definition['tol'],'--bc-tol',definition['bc_tol'],
                '--physical-bc-tol',definition['physical_bc_tol'],
                '--max-nodes',a.max_nodes,'--jac-batch',a.jac_batch,
                '--audit-angular',*definition['audit_angular']]
            stage=dict(definition=definition,source_run=str(previous),accepted=False,status='running')
            state['stages'].append(stage)
            code=invoke(name,command)
            returned=directory/'run.json'
            stage['returncode']=code
            if not returned.is_file():
                raise RuntimeError('The actual stage returned no run.json: '+name)
            candidate=load(returned)
            stage.update(run=str(returned),run_sha256=sha(returned),status=candidate.get('status'),
                solver_success=candidate.get('solver_success'),raw_return=candidate.get('raw_return'),
                error=candidate.get('error'),physical_bc=candidate.get('linear_dn_physical_bc_max'))
            try:
                candidate_problem=require_lambda1(candidate)
                if code or candidate_problem!=contract:
                    raise ValueError('The returned stage changed the complete problem or exited unsuccessfully')
                if (candidate.get('same_complete_problem_as_source') is not True or
                        candidate.get('fixed_metric_refinement') is not True or
                        candidate.get('fixed_metric_design_continuation') is not False):
                    raise ValueError('The solver did not identify this as same-lambda refinement')
                if candidate['raw_return']['rms']>definition['tol']:
                    raise ValueError('The requested actual RMS target was not reached')
                verify_field(returned,candidate)
            except Exception as error:
                stage['gate_error']=repr(error)
                state.update(status='stopped_on_rejected_fixed_lambda_stage',error=repr(error))
                save()
                return 2
            stage.update(accepted=True,metric=metric_max(candidate),
                         actual_q_aux=candidate.get('actual_q_aux'))
            state['result']['last_accepted_run']=str(returned)
            save()
            pair_path=out/(name+'-c2.json')
            pair=dict(kind='same_M_numerical_refinement' if index==0 else 'modal_increment',
                first_run=str(previous),second_run=str(returned),status='running')
            state['comparisons'].append(pair)
            command=[sys.executable,compare,'--first-run',previous,'--second-run',returned,
                '--out',pair_path,'--mean-nodes',1168,'--angular',*comparison_angles]
            code=invoke(name+'-compare',command)
            if code or not pair_path.is_file():
                pair.update(status='error',returncode=code)
                state.update(status='stopped_on_actual_C2_comparison_error',
                             error='The same-problem actual comparison did not return')
                save()
                return 3
            result=load(pair_path)
            if result.get('status')!='evaluated' or result.get('homotopy')!=1.:
                raise ValueError('Unexpected actual C2 comparison result')
            pair.update(status='evaluated',file=str(pair_path),sha256=sha(pair_path),
                rows=result['rows'],phase_control_literal_distances=result['phase_control_literal_distances'],
                observed_height_quadrature_change=result['observed_height_quadrature_change'],
                height_quadrature_error_certified=False,continuous_C2_bound_certified=False,
                same_limit_core_proven=False)
            previous,previous_record=returned,candidate
            save()
        state['status']='three_actual_fixed_lambda_stages_evaluated'
        state['result'].update(last_accepted_run=str(previous),all_finite_stages_passed=True,
            modal_trend=pair_trend(state['comparisons']),
            observed_metric_sequence=[state['initial_metric'],*[x['metric'] for x in state['stages']]],
            C2_convergence_proven=False,same_limit_core_proven=False,
            full_nonlinear_tail_paid=False,continuous_time_family_provided=False,complete_surface=False)
        save()
        return 0
    except Exception as error:
        state.update(status='fixed_lambda_pipeline_error',error=repr(error),
                     exception=traceback.format_exc()[-6000:])
        save()
        return 1


if __name__=='__main__':
    sys.exit(main())
