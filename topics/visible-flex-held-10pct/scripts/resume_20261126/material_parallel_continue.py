#!/usr/bin/env python3
"""Run three separate continuations of one actual recovered M24 prefix.

The nonlinear-DN branch, fixed-g diagnostic branch, and lambda design branch
have distinct identities. Their results cannot be combined into a certified
surface. A failed child does not cancel the other research calculations.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('repo','work','source-run','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args()
    repo,work,out=args.repo.resolve(),args.work.resolve(),args.outdir.resolve()
    source=args.source_run.resolve()
    if work not in out.parents or work not in source.parents:
        raise ValueError('Keep source and generated arrays in the work directory')
    scripts=repo/'topics/visible-flex-held-10pct/scripts'
    resume=scripts/'resume_m3'
    current=scripts/'resume_20261126'
    sys.path.insert(0,str(resume))
    from continue_material_true_tail import prefix_gate
    record=json.loads(source.read_text())
    out.mkdir(parents=True,exist_ok=False)
    if not prefix_gate(record) or not record.get('raw_return',{}).get('success'):
        (out/'summary.json').write_text(json.dumps(dict(status='source_prefix_rejected',
            error='The actual recovered M24 prefix has not passed its original gates',
            result={k:record.get(k) for k in ('solver_success','error','raw_return','prefix_audit')},
            source_hashes={str(source):digest(source)},complete_surface=False),indent=2)+'\n')
        return 2
    if record['modes']!=24 or record.get('actual_tail_requested'):
        raise ValueError('This entry continues the declared M24 linear prefix')
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
             VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
             VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
                 'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
    state=dict(scope=__doc__,status='preparing',progress={},results={},stages=[],
               source_hashes={str(source):digest(source),str(Path(__file__)):digest(__file__)},
               complete_surface=False)
    processes={}
    streams={}
    tasks={}
    audit_seen=set()
    audit_process=None
    audit_path=None
    audit_stream=None
    audit_packet=None
    target=out/'summary.json'

    def save():
        tmp=target.with_suffix('.tmp')
        tmp.write_text(json.dumps(state,indent=2,allow_nan=False)+'\n')
        tmp.replace(target)

    def start(name,script,arguments,directory):
        command=[sys.executable,'-u',str(script),*map(str,arguments)]
        streams[name]=(out/(name+'.log')).open('x')
        processes[name]=subprocess.Popen(command,cwd=repo,env=env,stdout=streams[name],
                                         stderr=subprocess.STDOUT)
        tasks[name]=directory
        state['results'][name]=dict(status='running',command=command,
                                    script_sha256=digest(script))
        save()

    def refresh():
        for name,proc in processes.items():
            row=state['results'][name]
            path=tasks[name]/'summary.json'
            if path.exists():
                try:
                    detail=json.loads(path.read_text())
                    row['diagnostics']={k:detail[k] for k in
                        ('status','stages','progress','result','error') if k in detail}
                    if isinstance(row['diagnostics'].get('stages'),list):
                        row['diagnostics']['stages']=row['diagnostics']['stages'][-6:]
                except (OSError,ValueError):
                    pass
            returned=proc.poll()
            if returned is not None:
                if not streams[name].closed:
                    streams[name].close()
                row.update(status='finished',returncode=returned)
            row['last_log']=(out/(name+'.log')).read_text(errors='replace')[-1000:]
        save()

    save()
    # Existing native warm/full-H work does not depend on the enlarged port.
    tail_dir=out/'true-tail'
    start('true-tail',current/'tail_continue_recovered_prefix.py',
          ['--repo',repo,'--work',work,'--source-run',source,'--outdir',tail_dir],tail_dir)
    config=json.loads((work/'m24-tail-settings.json').read_text())
    config['modes']=32
    while int(config['quadrature'])<=4*32*int(config['spacing']):
        config['quadrature']*=2
    settings=out/'tail-M32.json'
    settings.write_text(json.dumps(config,indent=2)+'\n')
    port=out/'port-M32.json'
    with (out/'port-export.log').open('x') as stream:
        exported=subprocess.run([sys.executable,
            str(resume/'recovered_q021/export_original_worker_port.py'),
            '--source-topic',str(work/'shared-source'),'--config',str(settings),
            '--out',str(port)],cwd=repo,env=env,stdout=stream,stderr=subprocess.STDOUT)
    state['progress']['port32']=dict(returncode=exported.returncode,
        sha256=digest(port) if port.exists() else None)
    if exported.returncode==0:
        fixed_dir=out/'fixed-g'
        design_dir=out/'lambda-design'
        start('fixed-g',current/'fixed_m3_refinement_pipeline.py',
              ['--repo',repo,'--source-run',source,'--port32',port,'--outdir',fixed_dir],fixed_dir)
        start('lambda-design',current/'material_design_continue.py',
              ['--repo',repo,'--work',work,'--source-run',source,'--port32',port,
               '--outdir',design_dir],design_dir)
    else:
        state['progress']['port32']['error']='Original M32 exporter failed; true-tail still continues'
    with (out/'mpmath-install.log').open('x') as stream:
        installed=subprocess.run([sys.executable,'-m','pip','install','--disable-pip-version-check',
            '--no-cache-dir','mpmath==1.3.0'],env=env,stdout=stream,stderr=subprocess.STDOUT)
    state['progress']['cut_audit_dependency_ready']=installed.returncode==0
    state['status']='independent_actual_continuations_running'
    save()
    while True:
        refresh()
        if audit_process is not None and audit_process.poll() is not None:
            audit_stream.close()
            row=dict(packet=audit_packet.name,packet_sha256=digest(audit_packet),
                     returncode=audit_process.returncode)
            if audit_path.exists():
                check=json.loads(audit_path.read_text())
                row.update(output_sha256=digest(audit_path),status=check['status'],
                    branches=check['branches'],normalized_Darboux=check['normalized_Darboux'],
                    continuous_turning=check['continuous_turning'],
                    unique_turning_mean_bracket=check['unique_turning_mean_bracket'],
                    bridge_tail_trace=check.get('bridge_tail_trace'))
            if audit_process.returncode:
                row['last_log']=audit_path.with_suffix('.log').read_text(errors='replace')[-2000:]
            state['stages'].append(row)
            audit_process=None
        if installed.returncode==0 and audit_process is None:
            for packet in sorted((tail_dir/'actual').glob('tail_*.json.gz')):
                if packet.name in audit_seen:
                    continue
                try:
                    with gzip.open(packet,'rt') as stream:
                        data=json.load(stream)
                    accepted=data.get('response',{}).get('converged') is True
                except (OSError,ValueError):
                    continue
                if not accepted:
                    audit_seen.add(packet.name)
                    continue
                audit_seen.add(packet.name)
                audit_packet=packet
                audit_path=out/('cut-'+packet.name.replace('.json.gz','.json'))
                audit_stream=audit_path.with_suffix('.log').open('x')
                audit_process=subprocess.Popen([sys.executable,
                    str(current/'seam_cut_pair_audit.py'),'--tail-response',str(packet),
                    '--source-run',str(source),'--physical',str(source.parent/'physical.npz'),
                    '--source-port',str(work/'m24-linear-port.json'),
                    '--short-bridge-source',str(work/'runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py'),
                    '--out',str(audit_path)],cwd=repo,env=env,stdout=audit_stream,stderr=subprocess.STDOUT)
                break
        save()
        if all(p.poll() is not None for p in processes.values()) and audit_process is None:
            break
        time.sleep(15)
    state['status']='all_declared_continuations_returned'
    refresh()
    return 0 if exported.returncode==0 and all(p.returncode==0 for p in processes.values()) else 2


if __name__=='__main__':
    sys.exit(main())
