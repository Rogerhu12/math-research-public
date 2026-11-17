#!/usr/bin/env python3
"""Regenerate the beta8 m=2 port, angular chart and seed commands in scratch.

Only immutable, hash-checked source is restored. No H vector, linear DN array
or numerical checkpoint is stored in the repository. This prepares a finite
calculation; it supplies no infinite-tail or global geometry certificate.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,hashlib,importlib.util,json,shlex,shutil,subprocess,sys
from pathlib import Path

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec);sys.modules[name]=value
    spec.loader.exec_module(value);return value
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--dest',type=Path,required=True)
    parser.add_argument('--manifest',type=Path,default=Path(__file__).with_name('coupling_recovery_manifest.json'))
    parser.add_argument('--run-seed',action='store_true')
    a=parser.parse_args();repo=a.repo.resolve();dest=a.dest.resolve()
    if dest==repo or repo in dest.parents:raise ValueError('Regenerated data must stay outside the repository')
    dest.mkdir(parents=True,exist_ok=False)
    recovery=dest/'recovery';manifest=json.loads(a.manifest.read_text())
    for row in manifest['files']:
        data=subprocess.check_output(['git','-C',str(repo),'show',row['revision']+':'+row['path']])
        if len(data)!=row['bytes']or hashlib.sha256(data).hexdigest()!=row['sha256']:
            raise RuntimeError('Immutable source checksum mismatch: '+row['path'])
        target=recovery/row['target'];target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    source=recovery/'bundle/topics/visible-flexible-closed-surface'
    comp=recovery/'bundle/topics/visible-flex-larger-amplitude/computations'
    (source/'source-origin.json').write_text(json.dumps({'source_revision':manifest['source_revision'],'scope':'Individually SHA256-verified immutable files.'},indent=2)+'\n')
    helper=recovery/'coupling_helpers';config=json.loads((helper/'hybrid_raised_valley_m8_config.json').read_text())
    pad=config.pop('valleyControlsPadTo',len(config['valleyControls']))
    config['valleyControls'] += [0]*max(0,pad-len(config['valleyControls']))
    config_path=dest/'tail-config.json';config_path.write_text(json.dumps(config,indent=2)+'\n')
    shutil.copyfile(helper/'hybrid_outer_factory.mjs',dest/'hybrid_outer_factory.mjs')
    worker=dest/'hybrid_tail_worker.mjs'
    subprocess.run([sys.executable,str(helper/'make_hybrid_worker.py'),str(source),str(worker)],check=True)
    env=dict(os.environ,VISIBLE_FLEX_SOURCE_TOPIC=str(source),
             VISIBLE_FLEX_SOURCE_ROOT=str(source/'repro/source-root'),
             CLOSING_TAIL_CACHE=str(source/'repro/source-root/topics/large-amplitude-twist-flex/scripts'))
    proc=subprocess.Popen(['node',str(worker),str(config_path)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,env=env)
    line=proc.stdout.readline()
    if not line:raise RuntimeError('Actual tail worker did not initialize')
    ready=json.loads(line)
    proc.stdin.write('{"stop":true}\n');proc.stdin.flush();proc.stdin.close();proc.wait(timeout=30)
    if proc.returncode:raise RuntimeError('Actual tail worker did not stop cleanly')
    physical_keys=('rCut','wCut','width','curvatureBound','orientation','prefixR','prefixEnd',
                   'prefixReturnStart','protectCell','slopeCap','capTransition','calibrationSteps',
                   'warpSteps','cuspAwareQuadrature','quadratureTolerance','capMode','valleyControls',
                   'pulseCaps','valleyCaps','maxCachedBetas','warpWeightLevels','spacing','outerCellDesign','constructor')
    cut_keys=('radius','backgroundSlope','backgroundSecond','E','Ep')
    port=dict(scope='Regenerated actual beta8 m=2 finite linear DN; used only for initialization and validation.',
              parameters={key:ready['parameters'][key]for key in physical_keys},
              cut={key:ready['cut'][key]for key in cut_keys},
              modes=list(range(2,2*config['modes']+1,2)),linearSlope=ready['linearSlope'])
    port_path=dest/'physical-port.json';port_path.write_text(json.dumps(port,indent=2)+'\n')
    sweep=module('coupled_runtime_smallcut',helper/'smallcut_prefix_sweep.py')
    cfg=dict(direction='outward',vu=.55,vd=.6,delta=.1718,ramp=.4,ramp_eta=.05,ramp_law='flat',cycles=1,
             prefix_bridge=dict(kind='turn_plateau_v1',curvature=4.,peak_fraction=.2))
    sweep.prepare(source,comp,port_path,cfg,dest)
    # A fresh finite-linear-DN seed is an initialization alternative. The
    # historical accepted run used a relaxed q=.002 seed; its exact command
    # and source/output hashes are retained in coupling_completed_seed.json.
    seed=[sys.executable,'-u',str(comp/'numerical-m2-prefix.py'),'--source-topic',str(source),
          '--profile',str(dest/'profile.json'),'--chart',str(dest/'chart.json'),'--port',str(port_path),
          '--out-prefix',str(dest/'linear-seed'),'--amplitude','.0002','--warp-reference','.0002',
          '--modes','8','--angular','256','--audit-angular','512','--nodes','301','--max-nodes','1800',
          '--tol','3e-7','--bc-tol','1e-7','--physical-bc-tol','2e-9']
    coupled=[sys.executable,'-u',str(Path(__file__).with_name('couple_smallcut.py').resolve()),
             '--source-topic',str(source),'--prefix-driver',str(comp/'numerical-m2-prefix.py'),
             '--coupler-source',str(source/'scripts/db6f-prefix-coupled.py'),'--worker',str(worker),
             '--profile',str(dest/'profile.json'),'--chart',str(dest/'chart.json'),'--port',str(port_path),
             '--tail-config',str(config_path),'--restart',str(dest/'linear-seed.json.gz'),
             '--out',str(dest/'coupled-q0002'),'--amplitude','.0002','--modes','8','--nodes','301',
             '--max-nodes','1800','--tol','3e-7','--warmup-scales','.1','1','--relax-linear']
    report=dict(scope=__doc__,source_manifest_sha256=sha(a.manifest),worker_sha256=sha(worker),
                factory_sha256=sha(dest/'hybrid_outer_factory.mjs'),commands=dict(seed=seed,coupled=coupled),
                regenerated_files={name:sha(dest/name)for name in ['physical-port.json','profile.json','chart.json','tail-config.json']},
                seed_status='not run')
    if a.run_seed:
        with (dest/'linear-seed.log').open('w')as log:result=subprocess.run(seed,stdout=log,stderr=subprocess.STDOUT)
        summary_path=dest/'linear-seed-summary.json'
        summary=json.loads(summary_path.read_text())if summary_path.exists()else{}
        report['seed_status']=dict(exit_code=result.returncode,success=bool(summary.get('solver_success')),
                                  metric_l1=summary.get('summary',{}).get('metric_l1'))
    (dest/'runtime-preparation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(event='prepared',destination=str(dest),linear_seed_command=shlex.join(seed),
                          actual_coupled_command=shlex.join(coupled),seed_status=report['seed_status'])),flush=True)
if __name__=='__main__':main()
