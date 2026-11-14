#!/usr/bin/env python3
"""Rebuild actual CM7 T3 branches, F3 height, and its independent audit."""
import argparse
from pathlib import Path
import subprocess
import sys
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--script-dir',type=Path,required=True)
p.add_argument('--work-dir',type=Path,required=True)
a=p.parse_args();s=a.script_dir.resolve();d=s/'data';w=a.work_dir.resolve();w.mkdir(parents=True,exist_ok=True)
br=w/'p41_CM7_actual_T3_branches47.json.gz';poly=w/'SS_j9_19_actual_CM_F3_polynomial47.json.gz'
anchor=d/'p41_basic_three_SS_CM_anchors47.json.gz'
def run(name,args):subprocess.run([sys.executable,'-u',str(s/name)]+[str(x) for x in args],check=True)
run('p41_CM7_T3_actual_branches47.py',['--script-dir',s,'--cm-anchors',anchor,'--output',br])
common=['--script-dir',s,'--branches',br,'--f2-branches',d/'p41_CM7_actual_T2_local_branches47.json.gz',
    '--f2-polynomial',d/'SS_j9_19_actual_CM_Laurent_F2_polynomial47.json.gz',
    '--f2-audit',d/'SS_j9_19-CM-F2-Laurent-independent-audit.json',
    '--reference-connections',d/'ORD_j39_actual_F3_CM_anchored_connections47.json.gz','--cm-anchors',anchor]
run('p41_CM7_F3_polynomial47.py',common+['--work-dir',w/'polynomial','--output',poly])
run('verify_CM7_F3_actual47.py',common+['--polynomial',poly,'--output',w/'SS_j9_19-CM-F3-independent-audit.json'])
