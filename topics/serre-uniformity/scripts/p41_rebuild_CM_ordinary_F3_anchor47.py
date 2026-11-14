#!/usr/bin/env python3
"""Rebuild a nonhorizontal CM ordinary F3 disk from its exact CM anchor."""
import argparse
from pathlib import Path
import subprocess
import sys


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--disk-id',choices=['ORD_j39','ORD_j40'],required=True)
    ap.add_argument('--result-id',required=True)
    ap.add_argument('--work-dir',type=Path,required=True)
    ap.add_argument('--rebuild-support',action='store_true')
    args=ap.parse_args();scripts=args.script_dir.resolve();data=scripts/'data'
    work=args.work_dir.resolve();work.mkdir(parents=True,exist_ok=True);disk=args.disk_id
    recovery=work/'recovery-inputs'
    def link(source,target):
        source=source.resolve(strict=True);target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():assert target.resolve()==source
        else:target.symlink_to(source,target_is_directory=source.is_dir())
    for name in ['p41_rational_SS_second_kind_integrals47_complete.json.gz','p41_SS_second_kind_rhs47.json.gz']:
        link(data/name,recovery/name)
    link(data/'SS_second_kind_rhs47',recovery/'SS-second-kind-rhs')
    def run(name,argv):
        subprocess.run([sys.executable,'-u',str(scripts/name)]+[str(x) for x in argv],check=True)
    support=data/f'{disk}_actual_T3_support47.json.gz'
    if args.rebuild_support or not support.exists():
        support=work/f'{disk}_actual_T3_support47.json.gz'
        run('p41_ordinary_t3_quartic_support47.py',['--script-dir',scripts,'--ordinary-lifts',data/'p41_ordinary_point_lifts47.json.gz','--j',int(disk[5:]),'--output',support])
    connection=work/f'{disk}_actual_F3_CM_anchored_connections47.json.gz'
    polynomial=work/f'{disk}_actual_CM_anchored_F3_polynomial47.json.gz'
    fixed=data/'p41_T3_fixed_divisor47.json.gz'
    run('p41_CM_ordinary_F3_anchored_connection47.py',['--script-dir',scripts,'--recovery-dir',recovery,'--disk-id',disk,'--result-id',args.result_id,'--second-kind',data/f'{disk}_second_kind_complete47.json.gz','--t3-support',support,'--fixed-support',fixed,'--cm11-second',data/'ORD_j38_second_kind_complete47.json.gz','--work-dir',work/'connection','--output',connection])
    f2=data/f'{disk}_actual_canonical_F2_polynomial47.json.gz';f2audit=data/f'{disk}-CM-F2-independent-audit.json'
    run('p41_CM_ordinary_F3_anchored_polynomial47.py',['--script-dir',scripts,'--center',connection,'--disk-id',disk,'--result-id',args.result_id,'--abel',data/f'{disk}_Abel47.json.gz','--multiply',data/f'{disk}_multiply47.json.gz','--tiny',data/'p41_all129_second_kind_tiny47_complete.json.gz','--f2-polynomial',f2,'--f2-audit',f2audit,'--work-dir',work/'polynomial','--output',polynomial])
    run('verify_CM_ordinary_F3_anchor47.py',['--script-dir',scripts,'--connection',connection,'--polynomial',polynomial,'--support',support,'--f2-polynomial',f2,'--f2-audit',f2audit,'--cm-anchors',data/'p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz','--fixed-support',fixed,'--output',work/f'{disk}-CM-F3-independent-audit.json'])


if __name__=='__main__':main()
