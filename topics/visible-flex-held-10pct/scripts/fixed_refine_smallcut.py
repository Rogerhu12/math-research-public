#!/usr/bin/env python3
"""Freeze a successful smallcut design profile and refine its Fourier/collocation mesh.
The physical metric, port, angular chart and warp reference stay fixed. The primary
support amplitude is a solved parameter; this remains an open finite-port prefix.
"""
import argparse,gzip,hashlib,json,subprocess,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--recovery',type=Path,required=True);p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--modes',type=int,default=20);p.add_argument('--tol',type=float,default=2e-8);p.add_argument('--nodes',type=int,default=701);p.add_argument('--max-nodes',type=int,default=6500);a=p.parse_args()
r=json.loads(gzip.decompress(a.checkpoint.read_bytes()))
if not r.get('solver_success'):raise SystemExit('Refinement requires a successful collocation checkpoint.')
port=json.loads(a.port.read_text());tagged_cut={**port['cut'],'_prefix_bridge':r['frozen_profile']['prefix_bridge']}
if r['physical_tail_parameters']!=port['parameters'] or r['physical_tail_cut']!=tagged_cut:raise SystemExit('Physical port differs from checkpoint.')
if a.modes>len(port['modes']):raise SystemExit('Port does not cover requested modes.')
a.output.mkdir(parents=True,exist_ok=True)
(a.output/'frozen-profile.json').write_text(json.dumps(r['frozen_profile'],indent=2)+'\n');(a.output/'chart.json').write_text(json.dumps(r['chart'],indent=2)+'\n')
source=a.recovery/'bundle/topics/visible-flexible-closed-surface';comp=a.recovery/'bundle/topics/visible-flex-larger-amplitude/computations'
cmd=[sys.executable,'-u',str(comp/'numerical-m2-prefix.py'),'--source-topic',str(source),'--profile',str(a.output/'frozen-profile.json'),'--chart',str(a.output/'chart.json'),'--port',str(a.port),'--out-prefix',str(a.output/'fixed'),'--amplitude',str(r['gauge_amplitude']),'--warp-reference',str(r['warp_reference_q']),'--modes',str(a.modes),'--angular',str(max(512,32*a.modes)),'--audit-angular',str(max(1024,64*a.modes)),'--nodes',str(a.nodes),'--max-nodes',str(a.max_nodes),'--tol',str(a.tol),'--bc-tol','1e-8','--physical-bc-tol','1e-10','--restart',str(a.checkpoint),'--fixed']
manifest=dict(scope=__doc__,seed_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),port_sha256=hashlib.sha256(a.port.read_bytes()).hexdigest(),command=cmd)
(a.output/'refinement_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
subprocess.run(cmd,check=True)
