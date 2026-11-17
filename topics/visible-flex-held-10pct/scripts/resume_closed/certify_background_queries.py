#!/usr/bin/env python3
"""Certify true-background partial integrals and inverse queries at actual R.

Numerical factory inverses only propose a cell, piece and center.  The
reported enclosure is certified from the unchanged R27 true integrals,
strict positive radial speed, and two outward inverse inequalities.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import heapq
import json
import math
import subprocess
import time

from certify_background_sharp import Background, lower, upper, interval, q, bound, mp, iv


def rational(v):
    x=Fraction(v)
    return iv.mpf(x.numerator)/x.denominator


def saved_interval(row):
    lo,hi=rational(row['lower_exact']),rational(row['upper_exact'])
    return interval(lower(lo),upper(hi))


def absolute_upper(v):
    return max(abs(lower(v)),abs(upper(v)))


def integrate_range(piece,left,right,tolerance,max_panels=65536):
    if left==right:
        return [iv.mpf(0)]*4,dict(panels=0,maximum_depth=0)
    assert 0<=left<right<=1
    # Initial endpoints are binary64, or zero/one; they have at most 53
    # significant binary digits.  At most 100 bisections keep midpoint
    # arithmetic exact in the 90-digit scalar context.
    assert all(x._mpf_[3]<=53 for x in [left,right])
    serial=0
    first=piece.panel(left,right)
    error=max(upper(v)-lower(v) for v in first)
    heap=[(-error,serial,left,right,first,0)]
    while True:
        largest=-heap[0][0]
        if (largest<=tolerance and (len(heap)%32==0 or largest*len(heap)<=tolerance)) or len(heap)>=max_panels:
            total=[sum((v[4][j] for v in heap),iv.mpf(0)) for j in range(4)]
            if max(upper(v)-lower(v) for v in total)<=tolerance:
                return total,dict(panels=len(heap),maximum_depth=max(v[5]for v in heap))
            if len(heap)>=max_panels:
                raise ArithmeticError('partial-integral panel cap')
        _,_,left,right,_,depth=heapq.heappop(heap)
        assert depth<100
        mid=(left+right)/2
        for lo,hi in [(left,mid),(mid,right)]:
            vals=piece.panel(lo,hi)
            error=max(upper(v)-lower(v) for v in vals)
            serial+=1
            heapq.heappush(heap,(-error,serial,lo,hi,vals,depth+1))


class TrueBackgroundQueries:
    def __init__(self,constants,certificate,piece_width='1e-18'):
        self.bg=Background(constants,certificate['cells'])
        self.cert=certificate
        self.normalization=saved_interval(certificate['positive_exact_normalization'])
        self.tolerance=mp.mpf(piece_width)
        self.pieces={}
        self.starts={}
        self.partial_cache={}
        self.integration_calls=[]
        bg=self.bg
        Y160=6*bg.delta0*bg.two**(-160)+6*bg.eta0*bg.two**(-240)/(1-bg.eta_ratio)
        self.rdeep=bg.aa*iv.exp(Y160/bg.sqrt12)

    def cell_start(self,n):
        if n not in self.starts:
            assert 0<=n<self.cert['cells']
            sums=[iv.mpf(0),iv.mpf(0)]
            for row in self.cert['cell_integrals'][n+1:]:
                sums=[a+saved_interval(row[k])for a,k in zip(sums,['A','B'])]
            for j,key in enumerate(['A','B']):
                rem=saved_interval(self.cert['analytic_deep_remainder'][key])
                sums[j]+=interval(0,upper(rem))
            value=self.rdeep+sums[0]+self.normalization*sums[1]
            if n==0:
                known=saved_interval(self.cert['cell0_inner_radius'])
                value=interval(max(lower(value),lower(known)),min(upper(value),upper(known)))
            self.starts[n]=value
        return self.starts[n]

    def piece(self,n,j):
        if n not in self.pieces:
            self.pieces[n]=list(self.bg.pieces(n))
        return self.pieces[n][j]

    def partial(self,n,j,x):
        key=(n,j,float(x))
        if key not in self.partial_cache:
            vals,stats=integrate_range(self.piece(n,j),mp.mpf(0),mp.mpf(float(x)),self.tolerance)
            self.partial_cache[key]=vals
            self.integration_calls.append(dict(cell=n,segment=j,x=float(x),**stats))
        return self.partial_cache[key]

    def radius_at(self,n,j,x):
        value=self.cell_start(n)
        for k in range(j):
            vals=self.partial(n,k,1.)
            value+=vals[0]+self.normalization*vals[1]
        vals=self.partial(n,j,x)
        return value+vals[0]+self.normalization*vals[1]

    def differential(self,n,j,domain):
        piece=self.piece(n,j)
        w,vals=piece.evaluate(domain,4)
        E=1+w.c[0]*w.c[0]
        if vals[0] is None:
            A=abs(w.c[1])/(8*E*iv.sqrt(E))
            sign=iv.mpf(1) if lower(w.c[1])>=0 else iv.mpf(-1) if upper(w.c[1])<=0 else interval(-1,1)
            Ax=sign*(2*w.c[2]/(E*iv.sqrt(E))-3*w.c[0]*w.c[1]*w.c[1]/(E*E*iv.sqrt(E)))/8
        else:
            A,Ax=vals[0].c[0],vals[0].c[1]
        speed=A+self.normalization*vals[1].c[0]
        assert lower(speed)>0
        speed_x=Ax+self.normalization*vals[1].c[1]
        wr=w.c[1]/speed
        wrr=(2*w.c[2]*speed-w.c[1]*speed_x)/(speed*speed*speed)
        return dict(w=w.c[0],wR=wr,wRR=wrr,speed=speed)

    def certify(self,radius,proposal):
        n,j=int(proposal['cell']),int(proposal['segment'])
        x0=mp.mpf(proposal['x'])
        assert 0<x0<1
        target=q(radius)
        at0=self.radius_at(n,j,x0)
        residual=at0-target
        trial=mp.mpf('1e-6')
        trial=min(trial,x0/2,(1-x0)/2)
        trial_domain=interval(x0-trial,x0+trial)
        gate=self.differential(n,j,trial_domain)
        # 2*error/speed_min yields strict inequalities even at interval ends.
        h=2*absolute_upper(residual)/lower(gate['speed'])
        h=mp.mpf(math.nextafter(float(h),math.inf))
        assert 0<h<trial
        assert x0._mpf_[2]>=-128 and h._mpf_[2]>=-128
        domain=interval(x0-h,x0+h)
        assert lower(domain)>=lower(trial_domain) and upper(domain)<=upper(trial_domain)
        exact=self.differential(n,j,domain)
        speed_lower=lower(exact['speed'])
        # These two scalar computations are converted to outward intervals
        # before their sign is accepted.  The 90-digit scalar value is never
        # itself used as a certified rounding direction.
        left_bound=at0-iv.mpf(speed_lower)*iv.mpf(h)
        right_bound=at0+iv.mpf(speed_lower)*iv.mpf(h)
        assert upper(left_bound)<lower(target)
        assert lower(right_bound)>upper(target)
        # Retain the physical radial dependency.  Direct range evaluation of
        # the cap formula at a tiny x interval can lose cancellations; the
        # mean-value theorem in R uses the already certified inverse box.
        w_at0=self.piece(n,j).evaluate(iv.mpf(x0),0)[0].c[0]
        propagated=w_at0+exact['wR']*(target-at0)
        exact['w']=interval(max(lower(exact['w']),lower(propagated)),
                            min(upper(exact['w']),upper(propagated)))
        errors={name:absolute_upper(exact[key]-q(proposal[name]))for name,key in [('w','w'),('wr','wR')]}
        return dict(radius=radius,cell=n,segment=j,numerical_center=float(x0),
                    center_true_radius=bound(at0),center_radius_minus_target=bound(residual),
                    exact_w_at_proposed_parameter=bound(w_at0),
                    exact_inverse_parameter_interval=bound(domain),
                    inverse_left_radius_upper=bound(left_bound),inverse_right_radius_lower=bound(right_bound),
                    true_w=bound(exact['w']),true_wR=bound(exact['wR']),true_wRR=bound(exact['wRR']),
                    positive_radial_speed=bound(exact['speed']),
                    numerical_query_absolute_error_upper={k:math.nextafter(float(v),math.inf)for k,v in errors.items()},
                    inverse_bracket_strict=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ['constants','certificate','source-topic','checkpoint','out']:
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--radii',required=True)
    parser.add_argument('--piece-width',default='1e-18')
    args=parser.parse_args()
    started=time.monotonic()
    constants=json.loads(args.constants.read_text())
    certificate=json.loads(args.certificate.read_text())
    assert certificate['input_sha256']==hashlib.sha256(args.constants.read_bytes()).hexdigest()
    radii=[float(x)for x in args.radii.split(',')]
    server=Path(__file__).with_name('background_metric_query.mjs')
    proc=subprocess.Popen(['node',str(server),str(args.source_topic),str(args.checkpoint)],
                          stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1)
    try:
        info=json.loads(proc.stdout.readline());assert info.get('ready')
        proc.stdin.write(json.dumps(dict(radii=radii))+'\n');proc.stdin.flush()
        reply=json.loads(proc.stdout.readline());assert 'error'not in reply,reply
    finally:
        proc.stdin.close();proc.wait(timeout=30)
    exact=TrueBackgroundQueries(constants,certificate,args.piece_width)
    rows=[]
    for radius,proposal in zip(radii,reply['rows']):
        row=exact.certify(radius,proposal)
        row['numerical_proposal']=proposal
        rows.append(row)
        print(json.dumps(dict(radius=radius,error_upper=row['numerical_query_absolute_error_upper'],
                              inverse_width=row['exact_inverse_parameter_interval']['upper']-row['exact_inverse_parameter_interval']['lower'])),flush=True)
    sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
    output=dict(scope=__doc__,source_sha256=sha(Path(__file__)),
                sharp_source_sha256=sha(Path(__file__).with_name('certify_background_sharp.py')),
                inputs={str(p.resolve()):sha(p)for p in [args.constants,args.certificate,args.checkpoint,server]},
                command=__import__('sys').argv,interval_precision=iv.dps,piece_width=args.piece_width,
                numerical_factory=info,rows=rows,integration_calls=exact.integration_calls,
                whole_radial_metric_certified=False,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(output,indent=2)+'\n')


if __name__=='__main__':
    main()
