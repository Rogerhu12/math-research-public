#!/usr/bin/env python3
"""Replay the full finite closed-map construction from regenerated R21 outputs.

No BVP is solved. The R21 closure package supplies finite_closed_tail.py and
its separate, already proved background/collar construction. This wrapper is
a reproducible recipe for the individually executed computations recorded in
execution_record.json; it is not claimed as an additional clean rerun.
"""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys

p=argparse.ArgumentParser(description=__doc__)
for k in ['source-topic','short-bridge','prefix-checkpoint','tail-checkpoint','port',
          'closure-package','closure-output','outdir']:
    p.add_argument('--'+k,type=Path,required=True)
a=p.parse_args();here=Path(__file__).resolve().parent
source=a.source_topic.resolve();old=a.closure_output.resolve();dep=a.closure_package.resolve()
out=a.outdir.resolve();out.mkdir(parents=True,exist_ok=False);pre=out/'prefix'
reader=source/'scripts/db6f_tail_integrated.py';manifest=old/'finite/tail-manifest.json'
cap=dep/'finite_closed_tail.py';bg=old/'background-interval.json';cc=old/'collar-disk-scalar.json'
for x in [reader,manifest,cap,bg,cc]:
    if not x.is_file():raise FileNotFoundError(x)
record=dict(scope=__doc__,completed=False,commands=[],source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
def run(cmd):
    cmd=[str(z)for z in cmd];record['commands'].append(cmd)
    (out/'replay_execution.json').write_text(json.dumps(record,indent=2)+'\n')
    subprocess.run(cmd,check=True)
py=sys.executable
run([py,here/'audit_common_prefix.py','--source-topic',source,'--short-bridge',a.short_bridge.resolve(),
    '--checkpoint',a.prefix_checkpoint.resolve(),'--port',a.port.resolve(),'--tail-manifest',manifest,
    '--tail-reader',reader,'--cap-source',cap,'--outdir',pre,'--angular','512','--radial','1025'])
run([py,here/'bound_cut_lift.py','--prefix-data',pre/'prefix-shared-cartesian.npz',
    '--tail-manifest',manifest,'--tail-reader',reader,'--out',out/'cut-lift-all-angle-bounds.json'])
run([py,here/'certify_finite_tail_geometry.py','--manifest',manifest,'--reader',reader,
    '--background',bg,'--prefix-audit',pre/'prefix-common-audit.json','--out',out/'finite-tail-continuous-geometry.json'])
run([py,here/'certify_prefix_geometry.py','--data',pre/'prefix-shared-cartesian.npz',
    '--checkpoint',a.prefix_checkpoint.resolve(),'--prefix-audit',pre/'prefix-common-audit.json',
    '--cut-bounds',out/'cut-lift-all-angle-bounds.json','--out',out/'prefix-continuous-geometry.json',
    '--angular','512','--curvature','10','--support','.7','--radius','1.17'])
run([py,here/'combine_closed_geometry.py','--prefix-audit',pre/'prefix-common-audit.json',
    '--prefix-certificate',out/'prefix-continuous-geometry.json','--tail-certificate',out/'finite-tail-continuous-geometry.json',
    '--collar-certificate',cc,'--out',out/'closed-continuous-geometry.json'])
run([py,here/'closed_m3_map.py','--source-topic',source,'--short-bridge',a.short_bridge.resolve(),
    '--prefix-checkpoint',a.prefix_checkpoint.resolve(),'--tail-checkpoint',a.tail_checkpoint.resolve(),
    '--port',a.port.resolve(),'--tail-manifest',manifest,'--tail-reader',reader,'--cap-source',cap,
    '--out',out/'closed-phase-query.json'])
record['completed']=True
record['output_sha256']={str(x.relative_to(out)):hashlib.sha256(x.read_bytes()).hexdigest()for x in
    [pre/'prefix-common-audit.json',out/'cut-lift-all-angle-bounds.json',out/'finite-tail-continuous-geometry.json',
     out/'prefix-continuous-geometry.json',out/'closed-continuous-geometry.json',out/'closed-phase-query.json']}
(out/'replay_execution.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'completed':True,'outdir':str(out)}))
