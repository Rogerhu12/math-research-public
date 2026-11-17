"""Run the complete basis-only audit in a user-selected scratch directory."""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path
import numpy as np
import mpmath


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--scratch',type=Path,required=True)
    args=p.parse_args();source=Path(__file__).resolve().parent
    out=args.scratch.resolve();out.mkdir(parents=True,exist_ok=True)
    reference=out/'reference';env=dict(os.environ)
    for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):env[key]='1'
    commands=[
        ('recover',[source/'recover_reference_sources.py','--repo',args.repo.resolve(),'--out',reference]),
        ('old-wide',[reference/'old_basis_fundamental_locked.py','--source',reference,'--out',out/'old-wide.json']),
        ('old-narrow',[reference/'old_basis_fundamental_locked_narrow.py','--source',reference,'--out',out/'old-narrow.json']),
        ('core-api',[source/'audit_uniform_core.py','--reference-core',reference/'plateau_core.py','--out',out/'core-api.json']),
        ('small-step',[source/'audit_small_parameter_steps.py','--reference-core',reference/'plateau_core.py','--out',out/'small-step.json']),
        ('comparison',[source/'compare_complement_controls.py','--reference-core',reference/'plateau_core.py',
            '--old-diagnostics',out/'old-wide.json',out/'old-narrow.json','--direction-input',source/'actual_direction_input.json',
            '--out',out/'comparison.json'])]
    runs=[]
    for name,argv in commands:
        start=time.monotonic();cmd=[sys.executable]+[str(x)for x in argv]
        log=out/(name+'.log')
        with log.open('wb') as handle:
            completed=subprocess.run(cmd,env=env,stdout=handle,stderr=subprocess.STDOUT)
        runs.append(dict(stage=name,command=cmd,returncode=completed.returncode,
                         elapsed_seconds=time.monotonic()-start,log_sha256=hashlib.sha256(log.read_bytes()).hexdigest()))
        print(json.dumps(runs[-1]),flush=True)
        if completed.returncode:raise RuntimeError('Audit stage failed; see '+str(log))
    report=dict(scope='Empty-reference restoration and actual audit execution; no BVP or surface is solved.',
        python=sys.version,numpy=np.__version__,mpmath=mpmath.__version__,runs=runs,
        output_sha256={name:hashlib.sha256((out/name).read_bytes()).hexdigest() for name in
            ('old-wide.json','old-narrow.json','core-api.json','small-step.json','comparison.json')})
    (out/'completed.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':main()
