#!/usr/bin/env python3
"""Rebuild the actual CM(-28) supersingular F2 height and independent audit."""
import argparse
from pathlib import Path
import subprocess
import sys

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--script-dir',type=Path,required=True)
p.add_argument('--work-dir',type=Path,required=True)
a=p.parse_args();s=a.script_dir.resolve();w=a.work_dir.resolve();w.mkdir(parents=True,exist_ok=True)
d=s/'data';support=w/'SS_j10_05_actual_T2_support47.json.gz'
center=w/'SS_j10_05_actual_F2_connections47.json.gz'
poly=w/'SS_j10_05_actual_CM_anchored_F2_polynomial47.json.gz'
anchor=d/'p41_CM28_SS_anchor47.json.gz'
def run(name,args):
    subprocess.run([sys.executable,'-u',str(s/name)]+[str(x) for x in args],check=True)
run('p41_CM28_SS_T2_support47.py',['--script-dir',s,'--work-dir',w/'support','--output',support])
run('p41_CM28_SS_F2_connections47.py',['--script-dir',s,'--recovery-dir',d,'--disk-id','SS_j10_05',
    '--result-id','R318','--t2-support',support,'--work-dir',w/'connections','--output',center])
run('p41_CM28_SS_F2_polynomial47.py',['--script-dir',s,'--disk-id','SS_j10_05','--result-id','R318',
    '--center',center,'--anchor',anchor,'--tiny',d/'p41_all129_second_kind_tiny47_complete.json.gz',
    '--work-dir',w/'polynomial','--output',poly])
run('verify_CM28_SS_F2_anchor47.py',['--script-dir',s,'--center',center,'--polynomial',poly,'--anchor',anchor,
    '--support',support,'--connection-source',s/'p41_CM28_SS_F2_connections47.py',
    '--polynomial-source',s/'p41_CM28_SS_F2_polynomial47.py',
    '--output',w/'SS_j10_05-CM-F2-independent-audit.json'])
