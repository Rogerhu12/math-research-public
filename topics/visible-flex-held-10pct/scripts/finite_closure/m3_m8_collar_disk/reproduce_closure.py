#!/usr/bin/env python3
"""Rebuild the finite C2 tail/collar/disk audit from an accepted fixed-g pair.

This consumes regenerated solver checkpoints; it does not store them or rerun
the BVP. Restore the 74-source closure first. All outputs go to --outdir.
"""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--source-topic',type=Path,required=True)
p.add_argument('--short-bridge',type=Path,required=True)
p.add_argument('--prefix-checkpoint',type=Path,required=True)
p.add_argument('--tail-checkpoint',type=Path,required=True)
p.add_argument('--port',type=Path,required=True)
p.add_argument('--outdir',type=Path,required=True)
a=p.parse_args();here=Path(__file__).resolve().parent
out=a.outdir.resolve();out.mkdir(parents=True,exist_ok=False)
source=a.source_topic.resolve()
record={'scope':__doc__,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'commands':[],'completed':False}
def run(cmd):
    cmd=[str(z) for z in cmd]
    record['commands'].append(cmd)
    (out/'replay_execution.json').write_text(json.dumps(record,indent=2)+'\n')
    subprocess.run(cmd,check=True)
py=sys.executable
run([py,here/'m3_prefix_endpoint.py','--source-topic',source,
     '--short-bridge',a.short_bridge.resolve(),'--checkpoint',a.prefix_checkpoint.resolve(),
     '--port',a.port.resolve(),'--output',out/'prefix-endpoint','--angular','512'])
run([py,here/'prepare_finite_tail.py','--source-topic',source,
     '--checkpoint',a.tail_checkpoint.resolve(),'--outdir',out/'finite',
     '--steps','32','--angular','256','--degree','96','--audit-angular','128',
     '--background-curvature','8.001'])
run([py,source/'scripts/db6f-tail-collar-exact-check.py',out/'finite/tail-collar.json',out/'finite/tail-collar-exact.json'])
run(['node',here/'dump_background_constants.mjs',source,a.tail_checkpoint.resolve(),out/'background-constants.json'])
run([py,here/'certify_background_integrals_v2.py','--input',out/'background-constants.json',
     '--out',out/'background-interval.json','--panels','64'])
run([py,here/'check_background_analytic_gates.py','--constants',out/'background-constants.json',
     '--integrals',out/'background-interval.json','--out',out/'background-gates.json'])
run([py,here/'audit_collar_and_disk.py','--manifest',out/'finite/tail-manifest.json',
     '--collar-exact',out/'finite/tail-collar-exact.json','--prefix-endpoint',out/'prefix-endpoint.json',
     '--background',out/'background-interval.json','--reader',source/'scripts/db6f_tail_integrated.py',
     '--out',out/'collar-disk-scalar.json'])
record['completed']=True
record['output_sha256']={str(q.relative_to(out)):hashlib.sha256(q.read_bytes()).hexdigest()for q in
    [out/'finite/tail-manifest.json',out/'finite/tail-collar-exact.json',out/'prefix-endpoint.json',
     out/'background-interval.json',out/'background-gates.json',out/'collar-disk-scalar.json']}
(out/'replay_execution.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'completed':True,'outdir':str(out)}))
