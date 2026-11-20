#!/usr/bin/env python3
"""Correct one projected material seed with the unchanged true nonlinear DN.

The input may fail the metric candidate gate and is used ONLY as a numerical
initial field. It must have an actual guarded prefix solve and stored physical
field. This does not accept that input or advance its material homotopy.
The corrected state must pass the same original BVP, true-DN and metric gates;
otherwise this fixed design is reported as unsuccessful. No complete-surface
or fixed-all-parameter convergence conclusion is implied.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_run(directory):
    return json.loads((directory/'run.json').read_text())


def prefix_gate(record):
    metric=record.get('prefix_audit',{}).get('metric_l1')
    return bool(record.get('solver_success') and not record.get('error')
                and metric is not None and metric<=1.e-6)


def actual_gate(record):
    checks=record.get('actual_outer_checks',[])
    seam=record.get('tail_seam',{})
    return bool(prefix_gate(record) and record.get('actual_tail_requested')
                and checks and checks[-1]['actual_bc']<=record['gates']['bc_tol']
                and seam.get('tail_converged')
                and seam.get('tail_shooting_residual',float('inf'))<=2.e-9)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','workdir','prefix-dir','core-config'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--workers',type=int,default=2)
    parser.add_argument('--tail-warmup',type=float,nargs='*',default=[.25,.5,.75,.9])
    args=parser.parse_args()
    repo,work=args.repo.resolve(),args.workdir.resolve()
    topic=repo/'topics/visible-flex-held-10pct'
    scripts=topic/'scripts'
    resume=scripts/'resume_m3'
    native=scripts/'resume_n4_tail/native_extended'
    inputs=work/'inputs'
    config=json.loads(args.core_config.read_text())
    initial=args.prefix_dir.resolve()
    initial_record=load_run(initial)
    if not (initial_record.get('solver_success') and not initial_record.get('error')
            and initial_record.get('raw_return',{}).get('success')
            and (initial/'physical.npz').is_file()):
        raise ValueError('The input must be an actual guarded projected solve with its physical field')
    if not initial_record.get('physical_sha256') or digest(initial/'physical.npz') != initial_record['physical_sha256']:
        raise ValueError('The actual physical field does not match the original run record')
    core=initial_record['raw_return'].get('core_summary',{})
    if core.get('core_kind') != 'material-curvature-flattening':
        raise ValueError('This correction is for the actual R53 material-core seed')
    for key in ('homotopy','curvature_blend','target_curvature','halfwidth','transition'):
        if float(config[key]) != float(core[key]):
            raise ValueError('Core design parameters differ from the source field')
    if initial_record['gauge_q']!=.06 or initial_record['modes']!=8:
        raise ValueError('This run is the declared q=.06/M8 material continuation')
    raw=initial/initial_record['raw_return']['file']
    if digest(raw) != initial_record['raw_return']['sha256']:
        raise ValueError('Raw initial field differs from its actual solver record')
    bootstrap=json.loads((work/'bootstrap.json').read_text())
    source=Path(bootstrap['source_topic'])
    short=Path(bootstrap['short_bridge'])
    env=dict(os.environ,PYTHONUNBUFFERED='1',VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
             VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(
                 scripts/'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
    summary=work/'material-corrector-summary.json'
    state=dict(scope=__doc__,stages=[],status='preparing_native',complete_surface=False,
               initial_metric_gate_pass=prefix_gate(initial_record),
               initial_metric_l1=initial_record.get('prefix_audit',{}).get('metric_l1'),
               initial_run_sha256=digest(initial/'run.json'),
               initial_raw_sha256=digest(raw),material_parameter_advanced=False)
    def save():
        summary.write_text(json.dumps(state,indent=2)+'\n')
    def run(command,environment=env):
        print(json.dumps(dict(event='command',argv=list(map(str,command)))),flush=True)
        return subprocess.run(list(map(str,command)),cwd=repo,env=environment,check=True)
    save()

    shared=work/'corrector-shared-source'
    native_source=work/'corrector-native-source'
    executable=work/'corrector-frozen-flow-batch'
    run([sys.executable,resume/'install_shared_tail_engines.py',
         '--copy-from',source,'--source-topic',shared,
         '--manifest',work/'corrector-shared-install.json',
         '--export-modules',work/'corrector-shared-modules'])
    run([sys.executable,scripts/'resume_n4_tail/install_periodic_quadrature.py',
         '--source-topic',shared,'--manifest',work/'corrector-periodic-install.json'])
    run(['g++','-std=c++17','-O2','-fno-fast-math','-ffp-contract=off',
         '-fexcess-precision=standard','-frounding-math','-DVF_BUILD_MAIN',
         native/'frozen_flow_production.cpp','-o',executable,'-lm'])
    run([sys.executable,native/'prepare_recovered_native.py',
         '--source-topic',shared,'--dest',native_source,'--native-cli',executable,
         '--modes','8','--spacing','3','--quadrature','128','--steps','16',
         '--workers',str(args.workers)])
    manifest=native_source/'native-manifest.json'
    state.update(native_manifest_sha256=digest(manifest),
                 native_binary_sha256=digest(executable),status='native_ready')
    save()
    native_runs=work/'corrector-native-runs'
    native_runs.mkdir(exist_ok=False)
    stages=[(float(config['homotopy']),float(config['curvature_blend']))]
    for index,(lam,blend) in enumerate(stages):
        current={**config,'homotopy':lam,'curvature_blend':blend}
        config_path=work/f'corrector-stage-{index:02d}.json'
        config_path.write_text(json.dumps(current,indent=2)+'\n')
        output=work/f'corrector-actual-{index:02d}'
        environment=dict(env,VISIBLE_FLEX_NATIVE_MANIFEST=str(manifest),
                         VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=digest(manifest),
                         VISIBLE_FLEX_NATIVE_RUN_DIR=str(native_runs/f'stage-{index:02d}'))
        command=[sys.executable,'-u',resume/'portable_prefix_continue.py',
            '--source-topic',native_source,'--short-bridge',short,
            '--profile',inputs/'q060-profile.json','--chart',inputs/'reference/chart.json',
            '--port',inputs/'q060-port.json','--tail-config',inputs/'q060-tail.json',
            '--raw-restart',raw,'--core-module',resume/'material_support_factory.py',
            '--core-config',config_path,'--amplitude','.06','--warp-reference','.06',
            '--modes','8','--angular','256','--audit-angular','512','--nodes','401',
            '--max-nodes','6000','--outdir',output]
        if args.tail_warmup:
            command+=['--tail-warmup',*map(str,args.tail_warmup)]
        print(json.dumps(dict(event='corrector_command',argv=list(map(str,command)))),flush=True)
        returned=subprocess.run(list(map(str,command)),cwd=repo,env=environment,check=False)
        record=load_run(output)
        accepted=bool(returned.returncode==0 and actual_gate(record))
        row=dict(index=index,homotopy=lam,curvature_blend=blend,
                 accepted=accepted,process_returncode=returned.returncode,source_raw_sha256=digest(raw),
                 solver_success=record.get('solver_success'),error=record.get('error'),
                 nodes=record.get('raw_return',{}).get('nodes'),
                 rms=record.get('raw_return',{}).get('rms'),
                 metric_l1=record.get('prefix_audit',{}).get('metric_l1'),
                 original_actual_checks=record.get('actual_outer_checks'),
                 tail_seam=record.get('tail_seam'),
                 parameter_controls=record.get('raw_return',{}).get('actual_core_corrections'),
                 full_parameter_vector=record.get('raw_return',{}).get('parameters'),
                 run_sha256=digest(output/'run.json'))
        state['stages'].append(row)
        state['status']='finite_stage_accepted' if accepted else 'finite_stage_failed'
        save()
        print(json.dumps(dict(event='projected_seed_true_dn_terminal',**row)),flush=True)
        if not accepted:
            return 2
        raw=output/record['raw_return']['file']
    state['status']='corrected_finite_candidate_passed_original_gates'
    state['last_raw_sha256']=digest(raw)
    save()
    return 0


if __name__=='__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        import traceback
        try:
            directory=Path(sys.argv[sys.argv.index('--workdir')+1]).resolve()
            target=directory/'material-corrector-summary.json'
            state=json.loads(target.read_text()) if target.exists() else {}
            state.update(status='corrector_error',error=repr(exc),
                         traceback=traceback.format_exc()[-6000:],complete_surface=False)
            target.write_text(json.dumps(state,indent=2)+'\\n')
        except Exception:
            pass
        raise
