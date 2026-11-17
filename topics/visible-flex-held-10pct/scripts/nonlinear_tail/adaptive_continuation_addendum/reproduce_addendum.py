#!/usr/bin/env python3
"""Reproduce finite continuation and the frozen-q004-metric M12 comparison.

Requires the recovered source and q=.002 seed from the adjacent seed package.
All regenerated ports and coefficient/checkpoint arrays stay in --output.
"""
import argparse,json,subprocess,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
for k in ('seed-package','seed-run','source-topic','prefix-recovery','output'):p.add_argument('--'+k,type=Path,required=True)
a=p.parse_args();pkg=a.seed_package.resolve();seed=a.seed_run.resolve();source=a.source_topic.resolve();out=a.output.resolve();out.mkdir(parents=True,exist_ok=False)
driver=a.prefix_recovery.resolve()/'bundle/topics/visible-flex-larger-amplitude/computations/numerical-m2-prefix.py'
worker=seed/'tail_worker.mjs';factory=seed/'hybrid_outer_factory.mjs';port=seed/'worker_port8.json';config=seed/'physical_config.json';profile=seed/'prefix_p20/profile.json';chart=seed/'prefix_p20/chart.json'
py=sys.executable;commands=[]
def run(cmd):
 cmd=list(map(str,cmd));commands.append(cmd);(out/'commands.json').write_text(json.dumps(commands,indent=2)+'\n');print(json.dumps({'command':cmd}),flush=True);subprocess.run(cmd,check=True)
def tail_record(case):
 d=json.loads((case/'summary.json').read_text())
 if not d['solver_success']:raise RuntimeError('An accepted coupled pair is required: '+str(case))
 return case/d['tail_seam']['tail_record']
def continuation(restart_case,amplitudes,tol,destination):
 run([py,pkg/'continue_smallcut_coupled.py','--source-topic',source,'--prefix-driver',driver,'--coupler-source',pkg/'db6f-prefix-coupled.py','--worker',worker,'--profile',profile,'--chart',chart,'--port',port,'--tail-config',config,'--restart',restart_case/'prefix.json.gz','--tail-state',tail_record(restart_case),'--out',destination,'--amplitudes',*amplitudes,'--modes','8','--nodes','601','--max-nodes','4000'if tol==1e-6 else'2500','--tol',tol,'--inner-verbose','2'])
first=out/'continuation_tol1e-6';continuation(seed/'coupled_q002',[.004,.006],1e-6,first)
q4=first/'q0p004-m8';tail_record(q4)
continuation(q4,[.006,.008],3e-6,out/'continuation_tol3e-6')
port32=out/'port32_s1024_canonical.json'
run(['node',Path(__file__).with_name('hybrid_linear_port.mjs'),source,factory,config,port32,'1024','32',port])
summary=json.loads((q4/'summary.json').read_text());fixed_profile=out/'q004-frozen-profile.json';fixed_profile.write_text(json.dumps(summary['frozen_profile'],indent=2)+'\n')
c=json.loads(config.read_text());c.update(modes=12,quadrature=256,steps=64,auditSteps=64,linearSteps=1024,initialCheckpoint=str(tail_record(q4)))
fixed_config=out/'fixed_q004_m12_s64_config.json';fixed_config.write_text(json.dumps(c,indent=2)+'\n')
run([py,pkg/'couple_smallcut.py','--source-topic',source,'--prefix-driver',driver,'--coupler-source',pkg/'db6f-prefix-coupled.py','--worker',worker,'--profile',fixed_profile,'--chart',chart,'--port',port32,'--tail-config',fixed_config,'--restart',q4/'prefix.json.gz','--out',out/'fixed_q004_m12_s64','--amplitude','.004','--warp-reference','.004','--modes','12','--angular','384','--audit-angular','768','--nodes','701','--max-nodes','4000','--tol','3e-7','--warmup-scales','1','--inner-verbose','2','--fixed'])
