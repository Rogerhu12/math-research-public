#!/usr/bin/env python3
"""Rebuild exact CM(-11) T3 branches, merged Laurent height, and independent audit."""
import argparse,subprocess,sys
from pathlib import Path

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--script-dir',type=Path,required=True);ap.add_argument('--work-dir',type=Path,required=True);ap.add_argument('--rebuild-support',action='store_true')
 args=ap.parse_args();scripts=args.script_dir.resolve();data=scripts/'data';work=args.work_dir.resolve();work.mkdir(parents=True,exist_ok=True)
 def run(name,argv):subprocess.run([sys.executable,'-u',str(scripts/name)]+[str(x) for x in argv],check=True)
 support=data/'ORD_j38_actual_T3_support47.json.gz'
 if args.rebuild_support or not support.exists():
  support=work/support.name;run('p41_ordinary_t3_split_support47.py',['--script-dir',scripts,'--ordinary-lifts',data/'p41_ordinary_point_lifts47.json.gz','--j',38,'--output',support])
 branches=work/'p41_CM11_actual_T3_local_branches47.json.gz';anchors=data/'p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz';connections=data/'ORD_j39_actual_F3_CM_anchored_connections47.json.gz'
 run('p41_CM11_T3_local_branches47.py',['--script-dir',scripts,'--support',support,'--cm-anchors',anchors,'--output',branches])
 polynomial=work/'ORD_j38_actual_CM_Laurent_F3_polynomial47.json.gz';f2=data/'ORD_j38_actual_canonical_F2_polynomial47.json.gz';audit=data/'ORD_j38-CM-F2-independent-audit.json'
 common=['--script-dir',scripts,'--branches',branches,'--reference-connections',connections,'--cm-anchors',anchors,'--f2-polynomial',f2,'--f2-audit',audit]
 run('p41_CM11_F3_Laurent_polynomial47.py',common+['--work-dir',work/'moving-RR','--output',polynomial])
 run('verify_CM11_F3_Laurent47.py',common+['--polynomial',polynomial,'--output',work/'ORD_j38-CM-F3-Laurent-independent-audit.json'])
if __name__=='__main__':main()
