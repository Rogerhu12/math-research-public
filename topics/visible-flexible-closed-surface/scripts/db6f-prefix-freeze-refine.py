#!/usr/bin/env python3
"""Freeze a completed coupled meridian metric and refine its actual tail solve.
The physical profile, full tail construction and phase range are unchanged.
Only Fourier order, numerical angular/radial resolution, and finite tail depth
change; actual support amplitude is an output of the same fixed-metric BVP.
"""
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--baseline',type=Path,required=True);p.add_argument('--out-prefix',type=Path,required=True);p.add_argument('--modes',type=int,required=True);p.add_argument('--depth',type=int,default=12);p.add_argument('--steps',type=int,default=32);p.add_argument('--shooting-parts',type=int,default=2);p.add_argument('--angular',type=int,default=512);p.add_argument('--tail-angular',type=int,default=512);p.add_argument('--tol',type=float,default=2e-9);p.add_argument('--bc-tol',type=float,default=1e-8);p.add_argument('--physical-bc-tol',type=float,default=2e-11);p.add_argument('--nodes',type=int,default=1001);p.add_argument('--max-nodes',type=int,default=6000);p.add_argument('--tail-tol',type=float,default=2e-9);p.add_argument('--node-heap',type=int,default=2048);p.add_argument('--shared-tail-engines',action='store_true');p.add_argument('--raw-lift-warm',action='store_true');p.add_argument('--lagged-tail',action='store_true');p.add_argument('--tail-initial-checkpoint',type=Path);p.add_argument('--preserve-restart-mesh',action='store_true');p.add_argument('--retain-tail-iterations',action='store_true');p.add_argument('--skip-warmup',action='store_true');a=p.parse_args()
if a.skip_warmup and not a.lagged_tail:raise ValueError('Skipping the warmup probe requires the original outer actual-DN solver')
S=Path(__file__).resolve().parent;N=S.parent/'notes';rec=json.loads(gzip.decompress(a.baseline.read_bytes()));assert rec['solver_success'] and rec['config']['actual_nonlinear_tail']
profile=a.out_prefix.with_name(a.out_prefix.name+'-frozen-profile.json');profile.write_text(json.dumps(rec['frozen_profile'],indent=2)+'\n')
tcfg=dict(rec['tail_config']);tailstate=a.tail_initial_checkpoint if a.tail_initial_checkpoint else a.baseline.parent/rec['tail_seam']['tail_record'];assert tailstate.exists()
tcfg.update(modes=a.modes,depth=a.depth,steps=a.steps,shootingParts=a.shooting_parts,quadrature=a.tail_angular,auditSteps=a.steps,maxIterations=36,solveTolerance=a.tail_tol,initialCheckpoint=str(tailstate.resolve()),sharedEngines=a.shared_tail_engines,traceFile=str(a.out_prefix.with_name(a.out_prefix.name+'-tail-trace.jsonl').resolve()))
if a.retain_tail_iterations:
 if not a.shared_tail_engines:raise ValueError('Iteration retention requires the shared worker')
 tcfg['iterationCheckpointFile']=str(a.out_prefix.with_name(a.out_prefix.name+'-tail-iteration.json.gz').resolve())
else:tcfg.pop('iterationCheckpointFile',None)
cfg=a.out_prefix.with_name(a.out_prefix.name+'-tail-config.json');cfg.write_text(json.dumps(tcfg,indent=2)+'\n')
warm_conversion=None
if a.raw_lift_warm:
 warm=a.out_prefix.with_name(a.out_prefix.name+'-raw-lift-warm.json.gz')
 warm_command=['node',str(S/'db6f-prefix-tail-raw-lift.mjs'),'--checkpoint',str(tailstate),'--config',str(cfg),'--out',str(warm)]
 wr=subprocess.run(warm_command,env=dict(os.environ,VISIBLE_FLEX_SOURCE_ROOT=str(a.source_root.resolve())),text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if wr.returncode:raise RuntimeError('Raw warm conversion failed: '+wr.stderr)
 warm_conversion=dict(command=warm_command,summary=json.loads(wr.stdout),sha256=hashlib.sha256(warm.read_bytes()).hexdigest())
 tcfg['initialCheckpoint']=str(warm.resolve());cfg.write_text(json.dumps(tcfg,indent=2)+'\n')
cmd=[sys.executable,str(S/'db6f-prefix-flat-coupled.py'),'--source-root',str(a.source_root),'--profile',str(profile),'--chart',str(N/'2026-11-09-950f-prefix-adaptive-chart.json'),'--linear-port',str(N/'2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json'),'--tail-config',str(cfg),'--out-prefix',str(a.out_prefix),'--restart',str(a.baseline),'--amplitude',str(rec['gauge_amplitude']),'--warp-reference',str(rec['warp_reference_q']),'--modes',str(a.modes),'--angular',str(a.angular),'--audit-angular',str(max(1024,64*a.modes)),'--nodes',str(a.nodes),'--max-nodes',str(a.max_nodes),'--tol',str(a.tol),'--bc-tol',str(a.bc_tol),'--physical-bc-tol',str(a.physical_bc_tol),'--node-heap',str(a.node_heap),'--fixed','--warmup-scales']+([] if a.skip_warmup else ['1'])
if a.lagged_tail:cmd.append('--lagged-tail')
if a.preserve_restart_mesh:cmd.append('--preserve-restart-mesh')
manifest=dict(scope=__doc__,driver_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),warmup_scales=[] if a.skip_warmup else [1],initial_tail_checkpoint=str(tailstate),initial_tail_sha256=hashlib.sha256(tailstate.read_bytes()).hexdigest(),warm_conversion=warm_conversion,shared_tail_engines=a.shared_tail_engines,baseline=str(a.baseline),baseline_sha256=hashlib.sha256(a.baseline.read_bytes()).hexdigest(),frozen_profile=rec['frozen_profile'],frozen_tail_parameters=rec['physical_tail_parameters'],baseline_amplitude=rec['actual_primary_amplitude'],command=cmd)
a.out_prefix.with_name(a.out_prefix.name+'-reproduction.json').write_text(json.dumps(manifest,indent=2)+'\n');start=time.time()
with a.out_prefix.with_name(a.out_prefix.name+'-run.log').open('w')as out:r=subprocess.run(cmd,stdout=out,stderr=subprocess.STDOUT)
manifest.update(exit_code=r.returncode,wall_seconds=time.time()-start);sf=a.out_prefix.with_name(a.out_prefix.name+'-summary.json')
if sf.exists():
 d=json.loads(sf.read_text());manifest.update(success=d.get('solver_success'),error=d.get('error'),actual_amplitude=d.get('actual_primary_amplitude'))
 if 'actual_primary_amplitude'in d:manifest['amplitude_difference']=d['actual_primary_amplitude']-rec['actual_primary_amplitude']
a.out_prefix.with_name(a.out_prefix.name+'-reproduction.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps({k:v for k,v in manifest.items()if k not in ('command','frozen_profile','frozen_tail_parameters')}),flush=True)
