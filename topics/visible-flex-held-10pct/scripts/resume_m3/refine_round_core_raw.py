#!/usr/bin/env python3
"""Refine a completed raw-core actual state with its physical g frozen.

The old raw control functions are mathematically unchanged when zero slots
are appended.  The actual BVP still solves every new mode and the true tail.
Only a subsequent full audit can establish an improvement in metric error.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from couple_m3_smallcut_secant import accepted_anchor


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('source-topic','short-bridge','sparse-helper','linear-port','prefix-restart','tail-restart','outdir'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--modes',type=int,required=True)
    p.add_argument('--angular',type=int)
    p.add_argument('--nodes',type=int)
    p.add_argument('--max-nodes',type=int,default=6000)
    a=p.parse_args();rec=json.load(gzip.open(a.prefix_restart,'rt'));accepted_anchor(rec,a.prefix_restart)
    if rec.get('core_control_path')!='raw-mean-primary-compact-v1':
        raise ValueError('Expected an actual raw-core state')
    if a.modes<=rec['config']['modes']:raise ValueError('Increase actual mode resolution')
    angular=a.angular or max(rec['config']['angular'],32*a.modes)
    if angular<rec['config']['angular']:raise ValueError('Do not reduce angular quadrature')
    cfg=dict(rec['tail_config']);cfg['modes']=a.modes
    need=4*a.modes*cfg['spacing'];N=1
    while N<=need:N*=2
    cfg['quadrature']=max(cfg['quadrature'],N)
    for k in ('initialCheckpoint','secantCheckpoint','designInitialCheckpoint','traceFile','geometricAmplitudePredictor'):
        cfg.pop(k,None)
    out=a.outdir.resolve();out.mkdir(parents=True,exist_ok=True)
    cfg['initialCheckpoint']=str(a.tail_restart.resolve());cfg['traceFile']=str(out/'worker-trace.jsonl')
    config=out/'config.json';profile=out/'profile.json';chart=out/'chart.json'
    config.write_text(json.dumps(cfg,indent=2)+'\n');profile.write_text(json.dumps(rec['frozen_profile'],indent=2)+'\n')
    chart.write_text(json.dumps(rec['chart'],indent=2)+'\n')
    port=json.loads(a.linear_port.read_text())
    expected_cut=dict(port['cut']);expected_cut['_prefix_bridge']=rec['frozen_profile']['prefix_bridge']
    if port['parameters']!=rec['physical_tail_parameters'] or expected_cut!=rec['physical_tail_cut']:
        raise ValueError('The new literal actual port must preserve the same physical g')
    if len(port['linearSlope'])<a.modes:raise ValueError('The actual new-mode port is incomplete')
    # The worker's physical port omits this prefix-only constructor selector.
    # Preserve the accepted selector in a separate prefix port, without
    # modifying a single numerical cut jet from the new actual worker.
    port['cut']=expected_cut;prefix_port=out/'prefix-port.json'
    prefix_port.write_text(json.dumps(port,indent=2)+'\n')
    settings=rec['core_round_settings'];wrapper=Path(__file__).with_name('couple_m3_round_core_raw_fixed.py')
    command=[sys.executable,str(wrapper),'--source-topic',str(a.source_topic.resolve()),
      '--short-bridge',str(a.short_bridge.resolve()),'--homotopy',str(settings['homotopy']),
      '--round-halfwidth',str(settings['halfwidth']),'--round-transition',str(settings['transition']),
      '--control-transition',str(settings['control_transition']),'--profile',str(profile),
      '--chart',str(chart),'--linear-port',str(prefix_port),'--tail-config',str(config),
      '--out-prefix',str(out/'seed'),'--restart',str(a.prefix_restart.resolve()),
      '--amplitude',str(rec['actual_primary_amplitude']),'--warp-reference',str(rec['warp_reference_q']),
      '--modes',str(a.modes),'--angular',str(angular),'--audit-angular',str(2*angular),
      '--nodes',str(a.nodes or rec['nodes']),'--max-nodes',str(a.max_nodes),
      '--tol',str(rec['config']['tol']),'--bc-tol',str(rec['config']['bc_tol']),
      '--physical-bc-tol',str(rec['config']['physical_bc_tol']),
      '--node-heap','3072','--warmup-scales','1','--lagged-tail','--fixed']
    record=dict(scope=__doc__,command=command,physical_g_frozen=True,
      old_modes=rec['config']['modes'],new_modes=a.modes,old_angular=rec['config']['angular'],new_angular=angular,
      old_tail_quadrature=rec['tail_config']['quadrature'],new_tail_quadrature=cfg['quadrature'],
      core_round_settings=settings,core_control_path=rec['core_control_path'],
      frozen_profile=rec['frozen_profile'],unchanged_tail_gate=cfg['solveTolerance'],
      prefix_port_sha256=hashlib.sha256(prefix_port.read_bytes()).hexdigest(),
      source_sha256={str(f.resolve()):hashlib.sha256(f.read_bytes()).hexdigest() for f in [Path(__file__),wrapper]},
      inputs={str(f.resolve()):hashlib.sha256(f.read_bytes()).hexdigest() for f in
       (a.prefix_restart,a.tail_restart,a.linear_port,a.short_bridge,a.sparse_helper)})
    record_file=out/'continuation-command.json';record_file.write_text(json.dumps(record,indent=2)+'\n')
    env=dict(os.environ);env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
      VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(a.sparse_helper.resolve()),VISIBLE_FLEX_SPARSE_TRACE=str(out/'linear-trace.jsonl'))
    result=subprocess.run(command,env=env);record['returncode']=result.returncode
    record_file.write_text(json.dumps(record,indent=2)+'\n');raise SystemExit(result.returncode)


if __name__=='__main__':main()
