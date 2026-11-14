#!/usr/bin/env python3
"""Build hash-bound validated radial primitive tables for a fixed source."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time

from db6f_tail_interval_elementary import I
from db6f_tail_interval_source_stable import FrozenSource
from db6f_tail_background_primitive import build_profile, strong_profile_anchors


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ['checkpoint','calibrations','alpha','cell-zero-A','inner-A','outer-B','out']:
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--depth',type=int,default=8)
    ap.add_argument('--order',type=int,default=8)
    ap.add_argument('--density',type=float,default=1e-10)
    ap.add_argument('--only-cell',type=int)
    ap.add_argument('--only-segment',type=int)
    args=ap.parse_args()
    raw=args.checkpoint.read_bytes()
    data=json.loads(gzip.decompress(raw) if args.checkpoint.suffix=='.gz' else raw)
    rr=data.get('response',data);cp=rr.get('checkpoint',rr);p=cp['parameters']
    cal=json.loads(args.calibrations.read_text());al=json.loads(args.alpha.read_text())
    az=json.loads(args.cell_zero_A.read_text());ai=json.loads(args.inner_A.read_text());bo=json.loads(args.outer_B.read_text())
    for report in [az,ai,bo]:
        if report['checkpointSHA256']!=sha(args.checkpoint) or report.get('calibrationsSHA256',report.get('calibrationTableSHA256'))!=sha(args.calibrations):
            raise ValueError('integral source binding mismatch')
    if al['inputs']['checkpoint']['sha256']!=sha(args.checkpoint) or al['inputs']['calibrations']['sha256']!=sha(args.calibrations):
        raise ValueError('alpha source binding mismatch')
    av=al['exactRadialAlpha'];alpha=I(av[0],av[1])
    model=FrozenSource(p,cal)
    anchors=strong_profile_anchors(p,av,az,ai,bo,args.depth)
    report={'status':'validated-source-radial-primitive-pending-independent-review',
            'scope':__doc__,'settings':{k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
            'inputs':{k:{'file':str(v),'sha256':sha(v)} for k,v in vars(args).items() if isinstance(v,Path) and k!='out'},
            'sources':{name:sha(Path(__file__).with_name(name)) for name in [Path(__file__).name,'db6f_tail_background_primitive.py','db6f_tail_interval_source.py','db6f_tail_interval_source_stable.py','db6f_tail_interval_elementary.py','db6f-audit-continuous-hermite.py']},
            'sourceModelModule':'db6f_tail_interval_source_stable.py',
            'parameters':p,'alpha':av,'profiles':[],'finished':False}
    start=time.time()
    for n in range(args.depth):
        if args.only_cell is not None and n!=args.only_cell:continue
        for j in range(9):
            if args.only_segment is not None and j!=args.only_segment:continue
            value=build_profile(model,alpha,n,j,anchors[(n,j)],order=args.order,density=args.density)
            report['profiles'].append(value)
            report['seconds']=time.time()-start
            payload=json.dumps(report,separators=(',',':')).encode()
            args.out.write_bytes(gzip.compress(payload,mtime=0) if args.out.suffix=='.gz' else payload+b'\n')
            print(json.dumps({k:value[k] for k in ['n','segment','boxesEvaluated','analyticLeaves','rangeLeaves']}),flush=True)
    report['finished']=True;report['seconds']=time.time()-start
    payload=json.dumps(report,separators=(',',':')).encode()
    args.out.write_bytes(gzip.compress(payload,mtime=0) if args.out.suffix=='.gz' else payload+b'\n')
    if args.out.stat().st_size>=5000000:raise ValueError('primitive table exceeds the per-file limit; split it by cell')
    print(json.dumps({'finished':True,'profiles':len(report['profiles']),'seconds':report['seconds'],'bytes':args.out.stat().st_size}))


if __name__=='__main__':main()
