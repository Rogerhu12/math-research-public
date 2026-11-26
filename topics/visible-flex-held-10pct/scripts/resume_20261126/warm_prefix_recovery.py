#!/usr/bin/env python3
"""Recover an M24 field through an M16 initial guess and the original lift.

The M16 field is used only as an initializer when its original BVP actually
converges and its physical C2 file is saved. Its metric may fail and is never
called accepted. The M24 solve must pass every original finite prefix gate
before the existing three separate research continuations start. Observer
snapshots are unaccepted Newton inputs. No numerical gate is relaxed.
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


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def tail_lines(path,count=32,limit=12000):
    if not path.exists():
        return []
    with path.open('rb') as stream:
        stream.seek(max(0,path.stat().st_size-limit))
        return stream.read().decode('utf-8','replace').splitlines()[-count:]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('repo','work','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    a=parser.parse_args()
    repo,work,out=a.repo.resolve(),a.work.resolve(),a.outdir.resolve()
    if work not in out.parents or repo==work or repo in work.parents:
        raise ValueError('Keep generated fields under work outside the repository')
    out.mkdir(parents=True,exist_ok=False)
    scripts=repo/'topics/visible-flex-held-10pct/scripts'
    resume=scripts/'resume_m3'
    current=scripts/'resume_20261126'
    sys.path.insert(0,str(resume))
    from continue_material_true_tail import prefix_gate
    state=dict(scope=__doc__,status='recording_prior_failure',stages=[],progress={},
               source_hashes={},complete_surface=False,fixed_metric_refinement=False)
    active=None
    stream=None

    def save():
        temporary=out/'summary.json.tmp'
        temporary.write_text(json.dumps(state,indent=2,allow_nan=False)+'\n')
        temporary.replace(out/'summary.json')

    save()
    try:
        prior_path=work/'m24-direct-recovery/run.json'
        prior_log=work/'live-held10-m24-direct-recovery-20261126-01.log'
        if prior_path.exists():
            prior=read(prior_path)
            state['exception']=dict(source=str(prior_path),
                error=prior.get('error'),solver_success=prior.get('solver_success'),
                raw_return=prior.get('raw_return'),
                traceback=str(prior.get('traceback','')).splitlines()[-32:],
                original_command_log_tail=tail_lines(prior_log))
            state['source_hashes'][str(prior_path)]=digest(prior_path)
            save()
        for path in (Path(__file__),resume/'portable_prefix_continue.py',
                     resume/'prepare_lifted_mode_restart.py',
                     current/'tail_observe_prefix.py',current/'streamed_release_prefix_driver.py',
                     current/'material_parallel_continue.py'):
            state['source_hashes'][str(path)]=digest(path)
        controls_path=work/'m24-recovery-controls.json'
        complete=read(controls_path)['full_actual_controls']
        if len(complete)!=23:
            raise ValueError('Expected all 23 recorded M24 controls')
        controls=out/'m16-initial-controls.json'
        controls.write_text(json.dumps(dict(full_actual_controls=complete[:15],
            scope='First 15 recorded M24 controls for an M16 initial guess only',
            source_sha256=digest(controls_path)),indent=2)+'\n')
        state['source_hashes'][str(controls_path)]=digest(controls_path)
        state['source_hashes'][str(controls)]=digest(controls)
        env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
                 PYTHONUNBUFFERED='1',VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
                 VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
                     'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
        for key in ('LD_LIBRARY_PATH','LD_PRELOAD'):
            env.pop(key,None)

        def run_stage(name,command,directory,observer=None):
            nonlocal active,stream
            command=list(map(str,command))
            row=dict(name=name,status='running',directory=str(directory),command=command)
            state['stages'].append(row)
            state['status']=name
            state['progress']=dict(current_stage=name)
            save()
            logfile=out/(name+'.log')
            stream=logfile.open('x')
            active=subprocess.Popen(command,cwd=repo,env=env,stdout=stream,stderr=subprocess.STDOUT)

            def refresh():
                if observer is not None:
                    for line in reversed(tail_lines(observer/'resources.jsonl',count=10)):
                        try:
                            data=json.loads(line)
                            state['progress']['last_actual_resource']={k:v for k,v in data.items()
                                if v is None or isinstance(v,(str,bool,int,float))}
                            break
                        except ValueError:
                            pass
                    checkpoint=observer/'last-jac-input.npz'
                    if checkpoint.exists():
                        state['progress']['unaccepted_initializer']=str(checkpoint)
                for line in reversed(tail_lines(directory/'events.jsonl',count=8)):
                    try:
                        data=json.loads(line)
                        state['progress']['last_actual_prefix_event']={k:v for k,v in data.items()
                            if v is None or isinstance(v,(str,bool,int,float))}
                        break
                    except ValueError:
                        pass
                result=directory/'run.json'
                if result.exists():
                    try:
                        data=read(result)
                        row['result']={k:data[k] for k in
                            ('solver_success','error','raw_return','prefix_audit','physical_sha256',
                             'domain_newton_stats','domain_error_counts') if k in data}
                    except (OSError,ValueError):
                        pass
                child_summary=directory/'summary.json'
                if child_summary.exists():
                    try:
                        data=read(child_summary)
                        row['result']={k:data[k] for k in
                            ('status','progress','error') if k in data}
                    except (OSError,ValueError):
                        pass
                state['progress']['last_log_lines']=tail_lines(logfile,count=12,limit=4000)
                save()

            while active.poll() is None:
                refresh()
                time.sleep(15)
            refresh()
            row.update(status='finished',returncode=active.returncode)
            stream.close()
            stream=None
            code=active.returncode
            active=None
            save()
            if code:
                raise RuntimeError(name+' returned '+str(code))
            return row

        common=['--source-topic',work/'multistage-source',
            '--short-bridge',work/'runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py',
            '--profile',work/'m24-recovery-profile.json','--chart',work/'inputs/reference/chart.json',
            '--port',work/'m24-linear-port.json','--core-module',resume/'material_support_factory.py',
            '--core-config',resume/'multistage_wide_circle_lambda0p002.json',
            '--amplitude','.06','--warp-reference','.06','--audit-angular','512',
            '--max-nodes','6000','--tol','1e-6','--bc-tol','1e-7','--physical-bc-tol','2e-9']

        def observed_command(directory,observer,modes,angular,nodes,extra):
            return [sys.executable,'-u',current/'tail_observe_prefix.py',
                '--observer-dir',observer,'--driver',current/'streamed_release_prefix_driver.py',
                '--','--rhs-block','8',*common,'--modes',modes,'--angular',angular,
                '--nodes',nodes,*extra,'--outdir',directory]

        m16=out/'m16-initializer'
        observer16=out/'m16-observer'
        row16=run_stage('m16_original_bvp',
            observed_command(m16,observer16,16,512,201,['--control-record',controls]),m16,observer16)
        record16=read(m16/'run.json')
        physical16=m16/'physical.npz'
        returned16=record16.get('raw_return') or {}
        raw16=m16/returned16.get('file','missing-raw')
        usable=bool(record16.get('solver_success') and not record16.get('error')
                    and returned16.get('success') and physical16.exists()
                    and raw16.exists() and digest(physical16)==record16.get('physical_sha256')
                    and digest(raw16)==returned16.get('sha256'))
        row16.update(usable_initializer=usable,accepted_prefix=False,
                     original_metric_gate_passed=prefix_gate(record16),
                     scope='M16 is only an initializer; its metric is not used to accept the M24 prefix')
        save()
        if not usable:
            raise RuntimeError('M16 did not return a converged BVP with its complete physical field')
        transfer=out/'m16-to-m24'
        row_transfer=run_stage('original_lift_to_m24',
            [sys.executable,'-u',resume/'prepare_lifted_mode_restart.py',
             '--source-run',m16/'run.json','--port',work/'m24-linear-port.json',
             '--modes','24','--angular','768','--check-angular','2048','--outdir',transfer],transfer)
        transfer_record=read(transfer/'transfer.json')
        raw=transfer/'initial.npz'
        if (transfer_record.get('status')!='nodal_initial_guess_ready' or not raw.exists()
                or digest(raw)!=transfer_record['initial_raw_sha256']):
            raise RuntimeError('Original continuous-reference lift did not return its declared nodal guess')
        row_transfer['result']={k:transfer_record[k] for k in
            ('status','initial_raw_sha256','reference_two_jet_checks','diagnostics','accepted_bvp')
            if k in transfer_record}
        save()
        m24=out/'m24-recovered'
        observer24=out/'m24-observer'
        row24=run_stage('m24_original_bvp',
            observed_command(m24,observer24,24,768,401,['--raw-restart',raw]),m24,observer24)
        record24=read(m24/'run.json')
        accepted=bool(prefix_gate(record24) and record24.get('raw_return',{}).get('success'))
        row24['original_finite_prefix_gates_passed']=accepted
        save()
        if not accepted:
            raise RuntimeError('M24 failed an original finite prefix gate; no continuation was launched')
        parallel=out/'continuations'
        run_stage('three_separate_continuations',
            [sys.executable,'-u',current/'material_parallel_continue.py',
             '--repo',repo,'--work',work,'--source-run',m24/'run.json','--outdir',parallel],parallel)
        state.update(status='declared_recovery_and_continuations_returned',returncode=0,
                     result=dict(source_run=str(m24/'run.json'),source_run_sha256=digest(m24/'run.json'),
                                 original_finite_prefix_gates_passed=True,complete_surface=False))
        save()
        return 0
    except Exception as exc:
        if active is not None and active.poll() is None:
            active.terminate()
            try:
                active.wait(timeout=20)
            except subprocess.TimeoutExpired:
                active.kill()
                active.wait()
        if stream is not None:
            stream.close()
        state.update(status='declared_stage_failed',returncode=2,error=repr(exc),
                     result=dict(exception=traceback.format_exc().splitlines()[-32:]))
        save()
        return 2


if __name__=='__main__':
    sys.exit(main())
