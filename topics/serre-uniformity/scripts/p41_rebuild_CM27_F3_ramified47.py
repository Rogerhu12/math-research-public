#!/usr/bin/env python3
"""Rebuild the exact ramified CM27 F3 disk and its independent audit."""
import argparse,subprocess,sys
from pathlib import Path

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--script-dir',type=Path,required=True);ap.add_argument('--work-dir',type=Path,required=True);args=ap.parse_args();s=args.script_dir.resolve();d=s/'data';w=args.work_dir.resolve();w.mkdir(parents=True,exist_ok=True)
 def run(n,a):subprocess.run([sys.executable,'-u',str(s/n)]+[str(x) for x in a],check=True)
 anchor=d/'p41_CM27_SS_anchor47.json.gz';branches=w/'p41_CM27_actual_T3_ramified_branches47.json.gz';pol=w/'SS_j9_11_actual_CM_ramified_F3_polynomial47.json.gz'
 run('p41_CM27_T3_ramified_branches47.py',['--script-dir',s,'--v-anchor',anchor,'--output',branches])
 common=['--script-dir',s,'--branches',branches,'--reference-connections',d/'ORD_j39_actual_F3_CM_anchored_connections47.json.gz','--v-anchor',anchor,'--f2-polynomial',d/'SS_j9_11_actual_CM_anchored_F2_polynomial47.json.gz','--f2-audit',d/'SS_j9_11-CM-F2-independent-audit.json']
 run('p41_CM27_F3_ramified_polynomial47.py',common+['--work-dir',w/'moving-RR','--output',pol])
 run('verify_CM27_F3_ramified47.py',common+['--polynomial',pol,'--output',w/'SS_j9_11-CM-F3-ramified-independent-audit.json'])
if __name__=='__main__':main()
