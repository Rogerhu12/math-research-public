#!/usr/bin/env python3
"""Real cooperative-comparison bounds for finite even frequency bands.

In (Q,Xi/nu), absolute values are dominated by [[d,nu*a],[b0,d]],
d=(m^2-4)r_x/r, a,b0>0. Every entry increases with m. The scalar diagonal
integrates to (r_out/r_in)^(m^2-4). Positive Peano--Baker bounds cover each
band by its upper frequency. The infinite remainder uses R22's energy bound.
This bounds propagation of the true deep high trace, not head-generated source.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb,ctx
from closure_real_head_source_enclosure import RealHead,exact_q,power2,ball_record
from closure_real_linear_head_enclosure import PositiveKernels,eye,matrix_record


def mm_upper(a,b):
    return [[(a[i][0]*b[0][j]+a[i][1]*b[1][j]).upper() for j in range(2)] for i in range(2)]


def scale_upper(a,s):
    return [[(x*s).upper() for x in row] for row in a]


def positive_peano(A,B):
    A=A.upper();B=B.upper();p=(A*B).upper()
    if not 0<=p<1:raise ArithmeticError('Positive Peano product must be <1')
    even=p*p/(4*(1-p));odd=p*p/(12*(1-p))
    diagonal=(1+p+even).upper();extra=(1+p/2+odd).upper()
    return [[diagonal,(A*extra).upper()],[(B*extra).upper(),diagonal]],p


def panel_kernels(kernels,n,j,max_mode,cap):
    nu=arb(max_mode*max_mode*(max_mode*max_mode-1))/12
    stack=[(Q(0),Q(1),0)]
    while stack:
        lo,hi,level=stack.pop()
        kernel=kernels.kernels(n,j,lo,hi)
        a=kernel['r']**(-8)*kernel['coreA'];b=kernel['r']**6*kernel['coreB']
        if (nu*a).upper()*b.upper()>cap:
            if level>=30:raise ArithmeticError('Positive-comparison panel subdivision limit')
            mid=(lo+hi)/2
            stack.append((mid,hi,level+1));stack.append((lo,mid,level+1))
        else:yield a,b


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ready',type=Path,required=True)
    parser.add_argument('--source-ledger',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--bands',default='94:96,98:104,106:112,114:128,130:192,194:256,258:512,514:1024,1026:2048')
    parser.add_argument('--start',type=int,default=12)
    parser.add_argument('--far',type=int,default=225)
    parser.add_argument('--far-strip',type=int,default=38)
    parser.add_argument('--out-strip',type=int,default=1)
    parser.add_argument('--far-low-log2-bound',type=int,default=-2200)
    parser.add_argument('--product-cap',default='1/4')
    parser.add_argument('--precision',type=int,default=192)
    args=parser.parse_args();ctx.prec=args.precision;started=time.monotonic()
    if args.start!=12 or args.far!=225:raise ValueError('The R18/R22 interface is currently 225 to12')
    if args.far_low_log2_bound>-1947:raise ValueError('Respect the R18 low-height domain')
    bands=[tuple(map(int,pair.split(':'))) for pair in args.bands.split(',')]
    expected=94
    for lo,hi in bands:
        if lo!=expected or lo%2 or hi%2 or hi<lo:raise ValueError('Cover contiguous even frequencies starting at94')
        expected=hi+2
    cap=exact_q(Q(args.product_cap))
    if not 0<cap<1:raise ValueError('Require 0<product-cap<1')
    raw=args.ready.read_bytes();ready=json.loads(raw)
    ledger_raw=args.source_ledger.read_bytes();ledger=json.loads(ledger_raw)
    if not all(ledger['checks'].values()) or hashlib.sha256(raw).hexdigest() not in ledger['input_hashes'].values():
        raise ValueError('The ready source has not paid the R22 finite parameter ledger')
    head=RealHead(ready,start=12,far=159,exact_through=23)
    kernels=PositiveKernels(head,225,bands[-1][1]);counts=0;rows=[]
    totals=[eye() for _ in bands]
    nus=[arb(hi*hi*(hi*hi-1))/12 for _,hi in bands]
    for n in range(224,11,-1):
        if n<224:
            for matrix in totals:
                matrix[1]=[(x/head.rho).upper() for x in matrix[1]]
        cell=[eye() for _ in bands];panels=0
        for j in range(9):
            for a,b in panel_kernels(kernels,n,j,bands[-1][1],cap):
                panels+=1
                for i,nu in enumerate(nus):
                    P,_=positive_peano(nu*a,b)
                    cell[i]=mm_upper(P,cell[i])
        rin=kernels.radius_point(n,0,Q(0));rout=kernels.radius_point(n,8,Q(1))
        ratio=(rout.upper()/rin.lower()).upper()
        if ratio<1:raise ArithmeticError('An outward radius-ratio upper bound was lost')
        for i,(_,hi) in enumerate(bands):
            cell[i]=scale_upper(cell[i],(ratio**(hi*hi-4)).upper())
            totals[i]=mm_upper(cell[i],totals[i])
        rows.append(dict(cell=n,panels=panels,positive_cell_matrices=[matrix_record(M) for M in cell]))
        counts+=panels
        if n%16==0 or n==12:
            print(json.dumps(dict(event='cell',cell=n,panels=counts,
                seconds=time.monotonic()-started,RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        kernels.release_cell(n)
    delta=head.d0*power2(-224)
    far_high=(head.eps/head.rc**3*(arb(11)*delta.log()/2).exp()
              *power2(1967+2*args.far_low_log2_bound))
    gap=args.far_strip-args.out_strip
    if gap<=4:raise ValueError('The infinite energy window needs a strip gap >4')
    outputs=[];operator_max=arb(0)
    for (lo,hi),matrix in zip(bands,totals):
        # The last cell uses mu12; the physical node12 raw port uses mu11.
        final=[matrix[0],[(x/head.rho).upper() for x in matrix[1]]]
        norm=(final[0][0]+final[1][0]).union(final[0][1]+final[1][1]).upper()
        weighted=(norm*(-arb(gap*lo)).exp()).upper()
        operator_max=operator_max.union(weighted).upper()
        outputs.append(dict(first_mode=lo,last_mode=hi,
            raw_balanced_operator_bound=ball_record(norm),
            log2_raw_balanced_operator_bound=ball_record(norm.log()/head.log2),
            weighted_operator_bound=ball_record(weighted),
            log2_deep_high_response_bound=ball_record((weighted*far_high).log()/head.log2)))
    energy=sum(3*n+32 for n in range(12,225));conversion=(224+18)//2
    first_infinite=bands[-1][1]+2;net=gap-4
    if not 4<net*first_infinite:raise ArithmeticError('The infinite envelope is not decreasing')
    infinite_log=(energy+conversion)*head.log2+4*arb(first_infinite).log()-net*first_infinite
    infinite=infinite_log.exp().upper();operator_max=operator_max.union(infinite).upper()
    bound=operator_max*far_high
    result=dict(status='Validated real exact-LINEAR propagation of the full j>46 deep trace, conditional on the specified full low46 R18 ball',
        far_strip=args.far_strip,out_strip=args.out_strip,
        all_46_low_height_l1_log2_bound=args.far_low_log2_bound,
        physical_far_high_bound=ball_record(far_high),
        bands=outputs,infinite_window=dict(first_mode=first_infinite,
            energy_log2=energy,conversion_log2=conversion,net_angular_gap=net,
            monotonicity_paid=True,weighted_operator_bound=ball_record(infinite),
            log2_deep_high_response_bound=ball_record((infinite*far_high).log()/head.log2)),
        weighted_operator_bound=ball_record(operator_max),
        complete_high_response_bound=ball_record(bound),
        log2_complete_high_response_bound=ball_record(bound.log()/head.log2),
        panel_count=counts,cell_rows=rows,scalar_integrals=kernels.integral_count,
        source_integrals=head.integral_count,elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        input_hashes={str(args.ready):hashlib.sha256(raw).hexdigest(),str(args.source_ledger):hashlib.sha256(ledger_raw).hexdigest()},
        source_hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in
            ['closure_positive_linear_band_enclosure.py','closure_real_linear_head_enclosure.py','closure_real_head_source_enclosure.py']},
        limits=['All original low46 deep heights are retained in the hypothesis; no free parameter is omitted or set to zero.',
            'The image norm is raw balanced (Q,Xi/nu) at the endpoint, not R23 whole-cell X.',
            'Head-generated nonlinear source and nonlinear feedback are not included.',
            'The stated smaller low-height ball/strip must be paid by the actual coupled reference and correction.'])
    output=Path(str(args.out_prefix)+'.json.gz')
    encoded=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(encoded)>=5_000_000:raise ArithmeticError('Repository file cap exceeded')
    output.write_bytes(encoded)
    summary={k:v for k,v in result.items() if k not in ('cell_rows','input_hashes')}
    summary.update(output=str(output),output_bytes=len(encoded),output_sha256=hashlib.sha256(encoded).hexdigest())
    Path(str(args.out_prefix)+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(output=str(output),log2_complete_high_response=summary['log2_complete_high_response_bound']['display'],
        panels=counts,seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
