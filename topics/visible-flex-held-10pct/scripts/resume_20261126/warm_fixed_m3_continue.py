#!/usr/bin/env python3
"""Continue a genuinely accepted positive-lambda field in the warm core family.

Actual delta, tail metric, gauge, complete baseline support and mean1168 are
frozen. Lambda changes only the declared core family, so the chain is not
reported as convergence of one complete fixed boundary problem. All stages
use the original linear DN; actual fullH, closed geometry and reach remain
separate obligations even if lambda=1 is reached.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('repo','work','source-run','outdir'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--port32',type=Path)
    p.add_argument('--targets',type=float,nargs='+',
                   default=[.004,.008,.016,.032,.064,.128,.256,.512,.75,1.])
    p.add_argument('--mode-levels',type=int,nargs='+',default=[24,32,40,48,64,80,96,128])
    p.add_argument('--minimum-lambda-step',type=float,default=1e-5)
    p.add_argument('--max-nodes',type=int,default=6000)
    a=p.parse_args()
    repo,work,out=a.repo.resolve(),a.work.resolve(),a.outdir.resolve()
    initial_run=a.source_run.resolve()
    if work not in out.parents or work not in initial_run.parents:
        raise ValueError('Keep actual fields and generated arrays in the shared work directory')
    if not all(0<x<=1 for x in a.targets) or a.targets!=sorted(set(a.targets)):
        raise ValueError('Lambda targets must increase in (0,1]')
    if a.mode_levels!=sorted(set(a.mode_levels)) or a.minimum_lambda_step<=0:
        raise ValueError('Mode levels increase and the minimum continuation step is positive')
    scripts=repo/'topics/visible-flex-held-10pct/scripts'
    current=scripts/'resume_20261126'
    resume=scripts/'resume_m3'
    sys.path.insert(0,str(resume))
    from continue_material_true_tail import prefix_gate
    source=load(initial_run)
    out.mkdir(parents=True,exist_ok=False)
    state=dict(scope=__doc__,status='preparing',stages=[],progress={},result={},
               fixed_metric=True,fixed_metric_refinement=False,
               fixed_metric_design_continuation=True,complete_surface=False,
               warm_anchor_accepted=False,
               source_hashes={str(initial_run):sha(initial_run),str(Path(__file__)):sha(__file__)})
    summary=out/'summary.json'
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',
             MKL_NUM_THREADS='1',PYTHONUNBUFFERED='1',
             VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
             VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
                 'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
    for name in ('LD_LIBRARY_PATH','LD_PRELOAD'):
        env.pop(name,None)
    def save():
        temp=summary.with_suffix('.tmp')
        temp.write_text(json.dumps(state,indent=2,allow_nan=False)+'\n')
        temp.replace(summary)
    def invoke(name,command):
        state.update(status=name,progress=dict(command=list(map(str,command))))
        save()
        log=out/(name+'.log')
        with log.open('x') as stream:
            proc=subprocess.Popen(list(map(str,command)),cwd=repo,env=env,
                                  stdout=stream,stderr=subprocess.STDOUT)
            while proc.poll() is None:
                state['progress']['last_log']=log.read_text(errors='replace')[-2000:]
                save()
                time.sleep(15)
        state['progress']['returncode']=proc.returncode
        save()
        return proc.returncode
    ports={int(source['modes']):Path(source['command'][source['command'].index('--port')+1])}
    if a.port32:
        ports[32]=a.port32.resolve()
    def port_for(modes):
        if modes in ports:
            return ports[modes]
        settings=load(work/'m24-tail-settings.json')
        settings['modes']=modes
        while int(settings['quadrature'])<=4*modes*int(settings['spacing']):
            settings['quadrature']*=2
        config=out/('tail-M%d.json'%modes)
        config.write_text(json.dumps(settings,indent=2)+'\n')
        port=out/('port-M%d.json'%modes)
        code=invoke('export-M%d'%modes,[sys.executable,
            resume/'recovered_q021/export_original_worker_port.py',
            '--source-topic',work/'shared-source','--config',config,'--out',port])
        if code:
            raise RuntimeError('Original enlarged physical port exporter failed')
        ports[modes]=port
        return port
    save()
    try:
        if (not prefix_gate(source) or not source.get('raw_return',{}).get('success') or
                source.get('actual_tail_requested') or source.get('fixed_metric_refinement')):
            raise ValueError('This branch begins with an actual accepted original R53 linear prefix')
        if source.get('core_settings',{}).get('curvature_blend')!=1.:
            raise ValueError('The warm anchor must have the fixed R53 target curvature')
        initial_lambda=float(source['core_settings']['homotopy'])
        if not 0<initial_lambda<=1:
            raise ValueError('A strictly positive actual anchor lambda is required')
        # First solve the new square fixed-delta system at exactly the old
        # lambda. This is a d=0 full-geometric handoff, not a cold R52 seed.
        targets=[initial_lambda]+[x for x in a.targets if x>initial_lambda]
        last_accepted_run=initial_run
        last_accepted_lambda=initial_lambda
        seed_run=initial_run
        modes=int(source['modes'])
        levels=sorted(set([modes,*[m for m in a.mode_levels if m>=modes]]))
        attempt=0
        allow_metric_seed=False
        while targets:
            target=targets[0]
            name='attempt-%03d'%attempt
            attempt+=1
            directory=out/name
            command=[sys.executable,current/'warm_fixed_m3_step.py',
                '--source-run',seed_run,'--outdir',directory,'--homotopy',target,
                '--modes',modes,'--angular',32*modes,'--port',port_for(modes),
                '--mean-nodes',1168,'--max-nodes',a.max_nodes]
            if allow_metric_seed:
                command.append('--allow-metric-failing-seed')
            code=invoke(name,command)
            path=directory/'run.json'
            returned=load(path) if path.exists() else {}
            accepted=bool(code==0 and returned.get('finite_linear_candidate_pass') and
                          returned.get('raw_return',{}).get('success'))
            row=dict(name=name,homotopy=target,modes=modes,source_run=str(seed_run),
                source_accepted=returned.get('source_accepted'),accepted=accepted,
                solver_success=returned.get('solver_success'),error=returned.get('error'),
                physical_bc_max=returned.get('linear_dn_physical_bc_max'),
                metric_diagnostics=returned.get('metric_diagnostics'),
                raw_return=returned.get('raw_return'),
                run=str(path),run_sha256=sha(path) if path.exists() else None,returncode=code)
            state['stages'].append(row)
            state['result']=dict(last_attempt=row,last_accepted_run=str(last_accepted_run),
                                 accepted_lambda=last_accepted_lambda)
            save()
            if accepted:
                state['warm_anchor_accepted']=True
                last_accepted_run=seed_run=path
                last_accepted_lambda=target
                targets.pop(0)
                allow_metric_seed=False
                continue
            larger=[m for m in levels if m>modes]
            bc=returned.get('linear_dn_physical_bc_max')
            scaled=returned.get('original_scaled_bc_max')
            boundary_converged=bool(returned.get('solver_success') and not returned.get('error') and
                returned.get('status')=='audited_finite_linear_candidate' and
                returned.get('metric_diagnostics') and
                returned.get('raw_return',{}).get('success') and
                returned.get('physical_sha256') and bc is not None and scaled is not None and
                bc<=returned['gates']['physical_bc_tol'] and scaled<=returned['gates']['bc_tol'])
            if boundary_converged:
                if not larger:
                    state['status']='warm_same_metric_requires_more_modes';save();return 2
                # This failed finite-metric stage is only a labelled initial
                # guess at the same lambda for the larger full lift system.
                seed_run=path
                modes=larger[0]
                allow_metric_seed=True
                continue
            step=target-last_accepted_lambda
            if step/2>=a.minimum_lambda_step:
                targets.insert(0,last_accepted_lambda+step/2)
                seed_run=last_accepted_run
                allow_metric_seed=False
                continue
            if larger:
                modes=larger[0]
                seed_run=last_accepted_run
                allow_metric_seed=False
                continue
            state['status']='warm_same_metric_continuation_failed'
            save()
            return 2
        state['status']='declared_warm_same_metric_stages_passed'
        state['result']=dict(accepted_lambda=last_accepted_lambda,run=str(last_accepted_run),
            lambda_one_reached=last_accepted_lambda==1.,fixed_lambda_C2_refinement_paid=False,
            full_nonlinear_tail_paid=False,complete_surface=False)
        save()
        return 0
    except Exception as error:
        state.update(status='warm_same_metric_entry_error',error=repr(error),
                     exception=traceback.format_exc()[-6000:])
        save()
        return 1


if __name__=='__main__':
    sys.exit(main())
