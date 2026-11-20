#!/usr/bin/env python3
"""One command for the documented scratch recovery and a declared full solve.

Example (all raw products stay outside the repository):
python reproduce_and_solve.py --repo REPO --work SCRATCH --implementation BATCHED

This command does not reproduce the old continuous certificates. Completed
recovery outputs are reused only after their exact recorded hashes are checked.
Each new nonlinear budget has a fresh output directory and explicit limits.
"""
import argparse
import os
from pathlib import Path
import subprocess
import sys

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--work',type=Path,required=True)
    p.add_argument('--implementation',type=Path)
    p.add_argument('--directions',type=int,default=1)
    p.add_argument('--maxiter',type=int,default=128)
    p.add_argument('--damping',type=float,default=.001)
    p.add_argument('--solver-output',type=Path)
    a=p.parse_args();here=Path(__file__).resolve().parent
    env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    for name in ('rebuild_fullclosed.py','rebuild_closed_warm.py'):
        subprocess.run([sys.executable,'-u',str(here/name),'--repo',str(a.repo),'--work',str(a.work)],env=env,check=True)
    if a.implementation:
        output=a.solver_output or a.work/'first-direction'
        operator=a.repo/'topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py'
        subprocess.run([sys.executable,'-u',str(here/'fullclosed_lm.py'),'--operator',str(operator),
            '--implementation',str(a.implementation),'--bundle',str(a.work/'data/fullclosed-mode-damped-warm.npz'),
            '--outdir',str(output),'--max-directions',str(a.directions),'--maxiter',str(a.maxiter),
            '--damping',str(a.damping)],env=env,check=True)

if __name__=='__main__':main()
