#!/usr/bin/env python3
"""Rebuild the genuine confluent basepoint F2 height and its integer audit."""
import argparse
from pathlib import Path
import subprocess
import sys


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--work-dir',type=Path,required=True)
    args=ap.parse_args();scripts=args.script_dir.resolve();work=args.work_dir.resolve()
    work.mkdir(parents=True,exist_ok=True);data=scripts/'data';here=Path(__file__).resolve().parent
    anchors=data/'p41_basic_three_SS_CM_anchors47.json.gz'
    reference=data/'SS_j9_11_actual_F2_connections47.json.gz'
    C=work/'SS_j0_10_actual_confluent_C_connection47.json.gz'
    F=work/'SS_j0_10_actual_confluent_F2_polynomial47.json.gz'
    audit=work/'SS_j0_10-confluent-F2-independent-audit.json'
    def run(name,arguments):
        subprocess.run([sys.executable,'-u',str(here/name),'--script-dir',str(scripts),
                        *[str(x) for x in arguments]],check=True)
    run('p41_basepoint_confluent_connection47.py',[
        '--cm-anchors',anchors,'--work-dir',work/'confluent','--output',C])
    run('p41_basepoint_F2_polynomial47.py',[
        '--confluent-connection',C,'--reference-connections',reference,'--cm-anchors',anchors,
        '--work-dir',work/'F2','--output',F])
    run('verify_basepoint_confluent_F2_47.py',[
        '--connection',C,'--polynomial',F,'--reference-connections',reference,
        '--cm-anchors',anchors,'--output',audit])
    print('PASS all actual basepoint construction and audit entries',flush=True)


if __name__=='__main__':main()
