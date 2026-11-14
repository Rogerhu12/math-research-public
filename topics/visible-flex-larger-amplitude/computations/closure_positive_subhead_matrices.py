#!/usr/bin/env python3
"""Enclose actual positive cell matrices for a specified deep subhead band.

This exports only real-source cell matrices in balanced (Q, Xi/nu_m)
coordinates.  It makes no assertion about a full source Green operator or
the shallower omitted cells.  Consumers must insert the exact Xi interface
factor, Fourier strip changes and the actual position of every source.
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
from closure_real_head_source_enclosure import RealHead,exact_q,ball_record
from closure_real_linear_head_enclosure import PositiveKernels,eye,matrix_record
from closure_positive_linear_band_enclosure import panel_kernels,positive_peano,mm_upper,scale_upper


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['ready','source-ledger','out-prefix']:
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--bands',default='2050:4096,4098:8190')
    p.add_argument('--start',type=int,default=24)
    p.add_argument('--far',type=int,default=225)
    p.add_argument('--product-cap',default='1/4')
    p.add_argument('--precision',type=int,default=192)
    args=p.parse_args();ctx.prec=args.precision;started=time.monotonic()
    if not 12<=args.start<args.far<=225:
        raise ValueError('The certified source interface is confined to nodes12..225')
    bands=[tuple(map(int,pair.split(':'))) for pair in args.bands.split(',')]
    expected=bands[0][0]
    if expected<94:
        raise ValueError('This helper is for the high-frequency subhead')
    for lo,hi in bands:
        if lo!=expected or lo%2 or hi%2 or hi<lo:
            raise ValueError('Use contiguous inclusive even-frequency bands')
        expected=hi+2
    cap=exact_q(Q(args.product_cap))
    if not 0<cap<1:
        raise ValueError('Require a positive Peano product cap below1')
    raw=args.ready.read_bytes();ready=json.loads(raw)
    ledger_raw=args.source_ledger.read_bytes();ledger=json.loads(ledger_raw)
    if not all(ledger['checks'].values()) or hashlib.sha256(raw).hexdigest() not in ledger['input_hashes'].values():
        raise ValueError('The complete R22 source-parameter ledger does not certify this ready')
    # Keep the same physical radius source, including its original integration
    # anchors.  Selecting a subhead changes only the matrix output range.
    head=RealHead(ready,start=12,far=159,exact_through=23)
    kernels=PositiveKernels(head,args.far,bands[-1][1])
    nus=[arb(hi*hi*(hi*hi-1))/12 for _,hi in bands]
    rows=[];counts=0;max_product=arb(0)
    for n in range(args.far-1,args.start-1,-1):
        cell=[eye() for _ in bands];panels=0
        for j in range(9):
            for a,b in panel_kernels(kernels,n,j,bands[-1][1],cap):
                panels+=1
                for k,nu in enumerate(nus):
                    P,product=positive_peano(nu*a,b)
                    max_product=max(max_product.upper(),product.upper())
                    cell[k]=mm_upper(P,cell[k])
        rin=kernels.radius_point(n,0,Q(0));rout=kernels.radius_point(n,8,Q(1))
        ratio=(rout.upper()/rin.lower()).upper()
        if ratio<1:
            raise ArithmeticError('Lost the valid outward radius-ratio bound')
        for k,(_,hi) in enumerate(bands):
            cell[k]=scale_upper(cell[k],(ratio**(hi*hi-4)).upper())
        rows.append(dict(cell=n,panels=panels,r_inner=ball_record(rin),r_outer=ball_record(rout),
            positive_cell_matrices=[matrix_record(M) for M in cell]))
        counts+=panels
        kernels.release_cell(n)
        if n%32==0 or n==args.start:
            print(json.dumps(dict(event='cell',cell=n,panels=counts,seconds=time.monotonic()-started,
                RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    result=dict(status='Validated real positive cell-matrix envelopes on a specified subhead only',
        start_physical_node=args.start,far_physical_node=args.far,bands=[list(x) for x in bands],
        coordinates='(Q_m, Xi_m/nu_m), nu_m=m^2(m^2-1)/12; each matrix excludes intercell Xi rescaling',
        interface='For outward propagation from cell n to cell n-1, multiply the second coordinate by 1/rho, rho=2^(11/4).',
        band_envelope='Entries of the cooperative comparison increase with even m, so the upper frequency bounds every frequency in its band.',
        cell_rows=rows,product_cap=str(Q(args.product_cap)),maximum_panel_product=ball_record(max_product),
        panel_count=counts,scalar_integrals=kernels.integral_count,source_integrals=head.integral_count,
        input_hashes={str(args.ready):hashlib.sha256(raw).hexdigest(),str(args.source_ledger):hashlib.sha256(ledger_raw).hexdigest()},
        source_hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in
            ['closure_positive_subhead_matrices.py','closure_positive_linear_band_enclosure.py',
             'closure_real_linear_head_enclosure.py','closure_real_head_source_enclosure.py']},
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        limits=['No cells before start are represented, and no full-head Green or nonlinear matching claim is made.',
            'No density source is integrated here. A source consumer must preserve source/target order and the canonical-to-physical conversion.',
            'No endpoint estimate is promoted to a whole-cell state estimate without a separately paid partial-flow bound.'])
    encoded=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(encoded)>=5_000_000:
        raise ArithmeticError('Repository file cap exceeded')
    out=Path(str(args.out_prefix)+'.json.gz');out.write_bytes(encoded)
    summary={k:v for k,v in result.items() if k!='cell_rows'}
    summary.update(output=str(out),output_sha256=hashlib.sha256(encoded).hexdigest(),output_bytes=len(encoded))
    Path(str(args.out_prefix)+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(event='done',cells=len(rows),bands=result['bands'],panels=counts,
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'],output=str(out))),flush=True)


if __name__=='__main__':main()
