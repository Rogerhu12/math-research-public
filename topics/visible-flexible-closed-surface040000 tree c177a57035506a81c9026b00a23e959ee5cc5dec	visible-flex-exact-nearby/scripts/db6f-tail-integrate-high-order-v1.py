#!/usr/bin/env python3
"""Validated Taylor/range integration of the frozen finite source A and B.

On a verified single analytic branch, normalized interval derivatives give
the integral Taylor remainder. Cap or abs crossings are subdivided and
eventually integrated by a plain interval range. Acceptance tolerances only
control work; the returned interval remains the actual certificate.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from db6f_tail_interval_elementary import I, qbounds
from db6f_tail_interval_source import FrozenSource, Jet


def integral_sum(values):
    if not values:return I(0)
    lo=np.array([float(x.lo) for x in values]);hi=np.array([float(x.hi) for x in values])
    if not np.all(np.isfinite(lo)) or not np.all(np.isfinite(hi)) or not np.all(lo<=hi):
        raise ArithmeticError('a nonfinite or reversed enclosure cannot enter a certificate')
    while len(lo)>1:
        if len(lo)%2:lo=np.r_[lo,0.];hi=np.r_[hi,0.]
        v=I(lo[::2],hi[::2])+I(lo[1::2],hi[1::2]);lo,hi=v.lo,v.hi
    return I(lo[0],hi[0])


def integrate(model,n,j,which,order,initial,tolerance,min_width,batch):
    if initial&(initial-1):raise ValueError('initial partition count must be a power of two')
    pending=[(k/initial,(k+1)/initial) for k in range(initial)]
    saved=[];analytic_count=range_count=evaluated=0;max_depth=0
    for depth in range(50):
        if not pending:break
        nxt=[]
        for start in range(0,len(pending),batch):
            block=pending[start:start+batch]
            lo=np.array([a for a,b in block]);hi=np.array([b for a,b in block]);width=hi-lo;mid=(lo+hi)/2
            if not np.all(width==width[0]):raise ValueError('breadth-first cells must have equal exact dyadic width')
            h=Q(float(width[0]))/2
            rr=model.evaluate(n,j,Jet.variable(I(lo,hi),order))
            pp=model.evaluate(n,j,Jet.variable(I(mid),order))
            valid=rr['valid'+which]&pp['valid'+which]
            f,point=rr[which],pp[which]
            polynomial=I(np.zeros(len(block)))
            for k in range(0,order,2):
                polynomial=polynomial+point.c[k]*qbounds(2*h**(k+1)/(k+1))
            remainder=f.c[order]*qbounds(2*h**(order+1)/(order+1))
            taylor=polynomial+remainder
            plain=f.c[0]*I(width)
            budget=tolerance*width
            remainder_bound=remainder.abs().hi
            plain_width=plain.hi-plain.lo
            accept_taylor=valid&(remainder_bound<=budget)
            accept_range=(~valid)&((plain_width<=budget)|(width<=min_width))
            for k,(a,b) in enumerate(block):
                if accept_taylor[k]:
                    saved.append(taylor[k]);analytic_count+=1
                elif accept_range[k]:
                    saved.append(plain[k]);range_count+=1
                elif width[k]<=min_width:
                    # A remainder can be wide because of interval dependency
                    # or parameter uncertainty. A direct range stays valid.
                    saved.append(plain[k]);range_count+=1
                else:
                    m=(a+b)/2;nxt.extend([(a,m),(m,b)])
            evaluated+=len(block);max_depth=depth
        pending=nxt
    if pending:raise RuntimeError('adaptive integration did not terminate')
    ans=integral_sum(saved)
    return ans,{'cell':n,'segment':j,'integrand':which,'interval':[float(ans.lo),float(ans.hi)],
                'width':float(ans.hi-ans.lo),'analyticLeaves':analytic_count,'rangeLeaves':range_count,
                'evaluatedBoxes':evaluated,'maximumExtraDepth':max_depth}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('checkpoint');ap.add_argument('calibrations');ap.add_argument('out')
    ap.add_argument('--integrands',default='A,B')
    ap.add_argument('--a-cells',default='0')
    ap.add_argument('--b-cells',default='0:16')
    ap.add_argument('--segments',default='0:9')
    ap.add_argument('--order',type=int,default=12)
    ap.add_argument('--initial',type=int,default=16)
    ap.add_argument('--a-tolerance',type=float,default=1e-16)
    ap.add_argument('--b-tolerance',type=float,default=1e-20)
    ap.add_argument('--minimum-width',type=float,default=2**-44)
    ap.add_argument('--batch',type=int,default=128)
    args=ap.parse_args()
    if args.order<2 or args.order%2:raise ValueError('positive even Taylor order required')
    if args.minimum_width<2**-48:raise ValueError('dyadic midpoints must remain exactly representable')
    def indices(s):
        if ':' in s:
            a,b=s.split(':');return list(range(int(a),int(b)))
        return [int(x) for x in s.split(',') if x]
    cp_path=Path(args.checkpoint)
    obj=json.load(gzip.open(cp_path,'rt') if cp_path.suffix=='.gz' else cp_path.open())
    response=obj.get('response',obj);cp=response.get('checkpoint',response)
    frozen=json.loads(Path(args.calibrations).read_text());model=FrozenSource(cp['parameters'],frozen)
    report={'status':'validated-frozen-source-high-order-integrals-pending-independent-review',
            'scope':__doc__,'checkpointSHA256':hashlib.sha256(cp_path.read_bytes()).hexdigest(),
            'calibrationsSHA256':hashlib.sha256(Path(args.calibrations).read_bytes()).hexdigest(),
            'sourceHashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),
                            Path(__file__).with_name('db6f_tail_interval_source.py'),
                            Path(__file__).with_name('db6f_tail_interval_elementary.py'),
                            Path(__file__).with_name('db6f-audit-continuous-hermite.py')]},
            'settings':vars(args),'rows':[],'totals':{},'finished':False}
    saved={};started=time.time()
    for which in args.integrands.split(','):
        cells=indices(args.a_cells if which=='A' else args.b_cells)
        saved[which]=[]
        for n in cells:
            for j in indices(args.segments):
                value,row=integrate(model,n,j,which,args.order,args.initial,
                                    args.a_tolerance if which=='A' else args.b_tolerance,args.minimum_width,args.batch)
                saved[which].append(value);report['rows'].append(row)
                total=integral_sum(saved[which]);report['totals'][which]=[float(total.lo),float(total.hi)]
                report['seconds']=time.time()-started
                Path(args.out).write_text(json.dumps(report,indent=2)+'\n')
                print(json.dumps(row),flush=True)
    report['finished']=True;report['seconds']=time.time()-started
    Path(args.out).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'finished':True,'totals':report['totals'],'seconds':report['seconds']}))


if __name__=='__main__':main()
