#!/usr/bin/env python3
"""Rebuild the actual SS_j9_11 F2 connections, CM-anchored polynomial and audit."""
import argparse
from pathlib import Path
import subprocess
import sys

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--script-dir',type=Path,required=True)
p.add_argument('--work-dir',type=Path,required=True)
a=p.parse_args();s=a.script_dir.resolve();w=a.work_dir.resolve();w.mkdir(parents=True,exist_ok=True)
d=s/'data';center=w/'SS_j9_11_actual_F2_connections47.json.gz'
poly=w/'SS_j9_11_actual_CM_anchored_F2_polynomial47.json.gz'
anchor=d/'p41_CM27_SS_anchor47.json.gz'
def run(name,args):
    subprocess.run([sys.executable,'-u',str(s/name)]+[str(x) for x in args],check=True)
run('p41_CM27_SS_F2_connections47.py',['--script-dir',s,'--recovery-dir',d,'--disk-id','SS_j9_11',
    '--result-id','R313','--work-dir',w/'connections','--output',center])
run('p41_CM27_SS_F2_polynomial47.py',['--script-dir',s,'--disk-id','SS_j9_11','--result-id','R313',
    '--center',center,'--anchor',anchor,'--tiny',d/'p41_all129_second_kind_tiny47_complete.json.gz',
    '--work-dir',w/'polynomial','--output',poly])
run('verify_CM27_SS_F2_anchor47.py',['--script-dir',s,'--center',center,'--polynomial',poly,'--anchor',anchor,
    '--connection-source',s/'p41_CM27_SS_F2_connections47.py','--polynomial-source',s/'p41_CM27_SS_F2_polynomial47.py',
    '--output',w/'SS_j9_11-CM-F2-independent-audit.json'])
