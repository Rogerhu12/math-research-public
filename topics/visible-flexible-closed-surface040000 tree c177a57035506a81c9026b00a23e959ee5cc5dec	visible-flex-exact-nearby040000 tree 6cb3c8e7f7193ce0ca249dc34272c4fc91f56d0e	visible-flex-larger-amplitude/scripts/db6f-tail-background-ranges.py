#!/usr/bin/env python3
"""Sequentially produce only the independently budgeted background ranges.

This is an execution ledger, not another interval algorithm. Each child
packet retains its own full settings, source hashes and exact coverage.
"""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--plan',type=Path,required=True)
    ap.add_argument('--setting',type=int,default=1)
    ap.add_argument('--raw-cell',type=int,default=0)
    ap.add_argument('--manifest',type=Path,required=True)
    ap.add_argument('--primitive',type=Path,required=True)
    ap.add_argument('--calibrations',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--w-width',type=float,default=4e-9)
    ap.add_argument('--max-depth',type=int,default=10)
    args=ap.parse_args()
    producer=Path(__file__).with_name('db6f-tail-background-packet-phase.py')
    plan=json.loads(args.plan.read_text())
    ranges=plan['settings'][args.setting]['raw_cells'][str(args.raw_cell)]['span_ranges']
    if not ranges or any(not (isinstance(a,int) and isinstance(b,int) and 0<=a<b) for a,b in ranges):
        raise ValueError('invalid planned span ranges')
    if any(b>c for (a,b),(c,d) in zip(ranges[:-1],ranges[1:])):
        raise ValueError('planned ranges overlap or are unordered')
    target=Path(str(args.out_prefix)+'.json')
    if target.exists():raise FileExistsError(target)
    report={'status':'sequential-background-production-ledger','finished':False,
            'script_sha256':sha(__file__),'producer_sha256':sha(producer),
            'plan_file':str(args.plan),'plan_sha256':sha(args.plan),
            'settings':{k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
            'span_ranges':ranges,'children':[]}
    start=time.time()
    target.write_text(json.dumps(report,indent=2)+'\n')
    for k,(a,b) in enumerate(ranges):
        prefix=Path(str(args.out_prefix)+f'-r{k:02d}')
        command=[sys.executable,str(producer),'--manifest',str(args.manifest),
                 '--primitive',str(args.primitive),'--calibrations',str(args.calibrations),
                 '--out-prefix',str(prefix),'--span-start',str(a),'--span-stop',str(b),
                 '--w-width',str(args.w_width),'--wr-width','1e300',
                 '--radial-residual','1e-8','--max-depth',str(args.max_depth)]
        began=time.time()
        with Path(str(prefix)+'.log').open('w') as log:
            process=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT)
        child={'range':[a,b],'return_code':process.returncode,
               'elapsed_seconds':time.time()-began,'packet_file':str(prefix)+'.json'}
        if process.returncode==0:
            data=json.loads(Path(child['packet_file']).read_text())
            child.update(packet_sha256=sha(child['packet_file']),finished=data.get('finished'),
                         rows=data['rows'],unmet_tolerance_rows=data['unmet_tolerance_rows'],
                         maximum_w_total_uncertainty=data['maximum_w_total_uncertainty'])
        report['children'].append(child)
        report['elapsed_seconds']=time.time()-start
        report['maximum_child_resident_bytes']=int(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)*1024
        target.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(child),flush=True)
        if process.returncode!=0:raise RuntimeError('child background production failed')
    report['finished']=all(c.get('finished') for c in report['children'])
    report['rows']=sum(c['rows'] for c in report['children'])
    report['unmet_tolerance_rows']=sum(c['unmet_tolerance_rows'] for c in report['children'])
    report['maximum_w_total_uncertainty']=max(c['maximum_w_total_uncertainty'] for c in report['children'])
    target.write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':main()
