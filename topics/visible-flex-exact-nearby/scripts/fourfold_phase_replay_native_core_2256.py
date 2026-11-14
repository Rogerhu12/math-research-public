#!/usr/bin/env python3
"""Replay the five genuinely completed native computations after executor loss.

No certificate is reconstructed from the observed receipt. Each mathematical
entry reads its complete saved inputs and writes a new complete report.
"""
from __future__ import annotations
import argparse
import os
from pathlib import Path
import subprocess
import sys

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out-dir',type=Path,default=Path('notes/native_core_20261112_replayed'))
    ap.add_argument('--cover-root',type=Path,default=Path('data/core_uniform_flow_ci/43307149760'))
    args=ap.parse_args()
    os.chdir(Path(__file__).resolve().parents[1])
    args.out_dir.mkdir(parents=True,exist_ok=True)
    env=os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',
               PYTHONDONTWRITEBYTECODE='1')
    out=lambda name:str(args.out_dir/name)
    commands=[
        ['fourfold_phase_low_block_dihedral.py','--height-order','0','--bits','256',
         '--out',out('finite_low_dihedral.json')],
        ['fourfold_phase_core_even_collect.py','--cover-root',str(args.cover_root),
         '--bits','256','--out',out('complete_uniform_even_core.json')],
        ['fourfold_phase_family_interface_fourier.py','--half-width','1/1000000000',
         '--bits','192','--primitive-nodes','512','--angles','2048','--keep','512',
         '--normalized-strip','1/16','--out',out('family_quarter_cut.json')],
        ['fourfold_phase_interface_strong_grams.py','--interface',out('family_quarter_cut.json'),
         '--modes','4','--output-cutoffs','4,16,64,256','--bits','256',
         '--out',out('family_quarter_cut_strong_Grams.json')],
        ['fourfold_phase_even_low_paid_core.py','--core',out('complete_uniform_even_core.json'),
         '--interface',out('family_quarter_cut.json'),'--old-sector',out('finite_low_dihedral.json'),
         '--bits','256','--out',out('actual_even_low_paid_core.json')]]
    for command in commands:
        subprocess.run([sys.executable,str(Path('scripts')/command[0]),*command[1:]],
                       env=env,check=True)
if __name__=='__main__':
    main()
