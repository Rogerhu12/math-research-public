#!/usr/bin/env python3
"""Continue an accepted material-core prefix through the unchanged true DN.

This runs in the same workspace as the H8 initializer and first positive-lambda
linear prefix. Generated arrays are local working data. Every later stage must
pass its original nonlinear DN, Frenet, boundary and sampled metric gates.
Even success at lambda=1 and curvature_blend=1 is only a finite prefix/tail
design: fixed-metric refinement, complete closure, held diameter and reach
remain separate tasks.
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
    parser.add_argument('--only-current',action='store_true')
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
    if not prefix_gate(initial_record):
        raise ValueError('The first material prefix has not passed its original finite metric gate')
    if initial_record['gauge_q']!=.06 or initial_record['modes']!=8:
        raise ValueError('This run is the declared q=.06/M8 material continuation')
    raw=initial/initial_record['raw_return']['file']
    bootstrap=json.loads((work/'bootstrap.json').read_text())
    source=Path(bootstrap['source_topic'])
    short=Path(bootstrap['short_bridge'])
    env=dict(os.environ,PYTHONUNBUFFERED='1',VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
             VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(
                 scripts/'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
    summary=work/'material-continuation.json'
    state=dict(scope=__doc__,stages=[],status='preparing_native',complete_surface=False)
    def save():
        summary.write_text(json.dumps(state,indent=2)+'\n')
    def run(command,environment=env):
        print(json.dumps(dict(event='command',argv=list(map(str,command)))),flush=True)
        return subprocess.run(list(map(str,command)),cwd=repo,env=environment,check=True)
    save()

    shared=work/'material-shared-source'
    native_source=work/'material-native-source'
    executable=work/'material-frozen-flow-batch'
    run([sys.executable,resume/'install_shared_tail_engines.py',
         '--copy-from',source,'--source-topic',shared,
         '--manifest',work/'material-shared-install.json',
         '--export-modules',work/'material-shared-modules'])
    run([sys.executable,scripts/'resume_n4_tail/install_periodic_quadrature.py',
         '--source-topic',shared,'--manifest',work/'material-periodic-install.json'])
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
    native_runs=work/'material-native-runs'
    native_runs.mkdir(exist_ok=False)
    stages=[(float(config['homotopy']),float(config['curvature_blend']))]
    if not args.only_current:
        start=stages[0]
        stages.extend((lam,start[1]) for lam in (.04,.08,.16,.32,.64,.82,1.)
                      if lam>start[0])
        if stages[-1][0]==1.:
            stages.extend((1.,blend) for blend in (.1,.2,.4,.6,.8,1.)
                          if blend>stages[-1][1])
    for index,(lam,blend) in enumerate(stages):
        current={**config,'homotopy':lam,'curvature_blend':blend}
        config_path=work/f'material-stage-{index:02d}.json'
        config_path.write_text(json.dumps(current,indent=2)+'\n')
        output=work/f'material-actual-{index:02d}'
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
        run(command,environment)
        record=load_run(output)
        accepted=actual_gate(record)
        row=dict(index=index,homotopy=lam,curvature_blend=blend,
                 accepted=accepted,source_raw_sha256=digest(raw),
                 solver_success=record.get('solver_success'),error=record.get('error'),
                 nodes=record.get('raw_return',{}).get('nodes'),
                 rms=record.get('raw_return',{}).get('rms'),
                 metric_l1=record.get('prefix_audit',{}).get('metric_l1'),
                 original_actual_checks=record.get('actual_outer_checks'),
                 tail_seam=record.get('tail_seam'),
                 parameter_controls=record.get('raw_return',{}).get('actual_core_corrections'),
                 run_sha256=digest(output/'run.json'))
        state['stages'].append(row)
        state['status']='finite_stage_accepted' if accepted else 'finite_stage_failed'
        save()
        print(json.dumps(dict(event='material_actual_terminal',**row)),flush=True)
        if not accepted:
            return 2
        raw=output/record['raw_return']['file']
    state['status']='declared_finite_stages_completed'
    state['last_raw_sha256']=digest(raw)
    save()
    return 0


if __name__=='__main__':
    sys.exit(main())
