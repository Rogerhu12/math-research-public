#!/usr/bin/env python3
"""Reconstruct the selected adaptive-tail q=.002 coupled finite seed.

The source bundle must first be restored from the recorded source manifests.
All regenerated arrays/checkpoints/ports are written only into --output.
"""
import argparse,json,shutil,subprocess,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
for k in ('repo','source-topic','prefix-recovery','output'):p.add_argument('--'+k,type=Path,required=True)
p.add_argument('--continue-amplitudes',nargs='*',type=float,default=[])
a=p.parse_args();here=Path(__file__).resolve().parent;out=a.output.resolve();out.mkdir(parents=True,exist_ok=False)
source=a.source_topic.resolve();recovery=a.prefix_recovery.resolve();driver=recovery/'bundle/topics/visible-flex-larger-amplitude/computations/numerical-m2-prefix.py'
factory=out/'hybrid_outer_factory.mjs';shutil.copy2(here/'hybrid_outer_factory.mjs',factory)
config=out/'physical_config.json';shutil.copy2(here/'physical_config.json',config)
worker=out/'tail_worker.mjs';port=out/'worker_port8.json';prefix=out/'prefix_p20';tail=out/'actual_q002_direction_seed';coupled=out/'coupled_q002'
commands=[]
def run(command):
 command=[str(x)for x in command];commands.append(command)
 (out/'commands.json').write_text(json.dumps(commands,indent=2)+'\n')
 print(json.dumps({'command':command}),flush=True);subprocess.run(command,check=True)
py=sys.executable
run([py,here/'make_hybrid_worker.py',source,worker])
run([py,here/'export_hybrid_ready_port.py','--source-topic',source,'--worker',worker,'--config',config,'--out',port,'--constructor','finite_preserved_pulses_v1'])
run([py,here/'smallcut_prefix_sweep.py','--repo',a.repo.resolve(),'--recovery',recovery,'--output',prefix,'--radius','.30','--port',port,'--curvature','4','--peak-fraction','.2','--stages','.002:8','--tol','1e-6','--max-nodes','4000','--stage-timeout','600'])
seed=prefix/'q002-m8.json.gz'
if not seed.exists():raise RuntimeError('Linear-port prefix did not produce a successful seed')
run([py,here/'continue_tail.py','--source-topic',source,'--config',config,'--height-trace',prefix/'q002-m8-H.json','--out',tail,'--lambdas=-.5,-1','--worker-path',worker,'--audit','--stop-on-failure'])
td=json.loads((tail/'summary.json').read_text());last=td['runs'][-1]
if not last['converged'] or last['lam']!=-1:raise RuntimeError('True nonlinear full-vector tail seed did not converge')
c=json.loads(config.read_text());c['initialCheckpoint']=str(tail/last['response_file']);seed_config=out/'coupled_seed_config.json';seed_config.write_text(json.dumps(c,indent=2)+'\n')
base=[py,here/'couple_smallcut.py','--source-topic',source,'--prefix-driver',driver,'--coupler-source',here/'db6f-prefix-coupled.py','--worker',worker,'--profile',prefix/'profile.json','--chart',prefix/'chart.json','--port',port,'--tail-config',seed_config,'--restart',seed,'--out',coupled,'--amplitude','.002','--modes','8','--nodes','601','--max-nodes','4000','--tol','1e-6','--warmup-scales','1','--inner-verbose','1']
run(base)
d=json.loads((coupled/'summary.json').read_text())
if not d['solver_success']:raise RuntimeError('True coupled prefix/tail solve was not accepted')
response=coupled/d['tail_seam']['tail_record']
run([py,here/'smallcut_endpoint.py','--recovery',recovery,'--checkpoint',coupled/'prefix.json.gz','--port',port,'--output',coupled/'prefix-endpoint','--angular','512'])
for step,label in [('0.0001','main'),('0.00005','half-step')]:
 endpoint=coupled/('tail-endpoint-'+label+'.json')
 run(['node',here/'export_cut_cartesian.mjs',source,factory,response,endpoint,'512',step])
 run([py,here/'compare_cut_cartesian.py',coupled/'prefix-endpoint.npz',endpoint,coupled/('cartesian-seam-'+label+'.json')])
run([py,here/'audit_prefix_envelope.py','--recovery',recovery,'--checkpoint',coupled/'prefix.json.gz','--port',port,'--output',coupled/'prefix-envelope.json'])
run(['node',here/'audit_finite_tail_geometry.mjs',source,factory,response,coupled/'prefix-endpoint.json',coupled/'finite-tail-geometry.json','128','4'])
if a.continue_amplitudes:
 run([py,here/'continue_smallcut_coupled.py','--source-topic',source,'--prefix-driver',driver,'--coupler-source',here/'db6f-prefix-coupled.py','--worker',worker,'--profile',prefix/'profile.json','--chart',prefix/'chart.json','--port',port,'--tail-config',config,'--restart',coupled/'prefix.json.gz','--tail-state',response,'--out',out/'coupled_continuation','--amplitudes',*a.continue_amplitudes,'--modes','8','--nodes','601','--max-nodes','4000','--tol','1e-6','--inner-verbose','1'])
