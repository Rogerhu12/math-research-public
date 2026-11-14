#!/usr/bin/env python3
"""Exact Fraction witness for one CURRENT POSITIVE-MAJORANT two-cycle.

This is not a lower bound on the true physical operator.  It concerns
the explicitly chosen upper-budget polynomial, and is used to identify
the frequency aggregation that must be repaired.
"""
import argparse,gzip,hashlib,json,resource,time
from fractions import Fraction as F
from pathlib import Path


LOW_SHA='31c65d6c8053325502542c008720f880d7386cd39168be79ca466851e76bb7ee'
MIDDLE_SHA='07c428b0c1a1977985200172dbee0bf14ae57e5fd4ea97ddebdf9b671479b3e6'


def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()


def iter_array(path,key):
    needle='"'+key+'"';decoder=json.JSONDecoder();buf=''
    with gzip.open(path,'rt') as f:
        while True:
            more=f.read(65536)
            if not more:raise ValueError('Missing generated array '+key)
            buf+=more;at=buf.find(needle)
            if at>=0:
                tail=buf[at+len(needle):].lstrip()
                if tail.startswith(':') and tail[1:].lstrip().startswith('['):
                    buf=tail[1:].lstrip()[1:];break
            buf=buf[-256:]
        while True:
            buf=buf.lstrip()
            if buf.startswith(','):buf=buf[1:].lstrip()
            if buf.startswith(']'):return
            try:row,end=decoder.raw_decode(buf)
            except json.JSONDecodeError:
                more=f.read(65536)
                if not more:raise ValueError('Incomplete generated array')
                buf+=more;continue
            yield row;buf=buf[end:]


def dyadic(m,e):
    m=int(m);e=int(e)
    return F(m*(1<<e),1) if e>=0 else F(m,1<<(-e))


def rec(x):return dict(numerator=str(x.numerator),denominator=str(x.denominator))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('low','middle','out'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError('Use a fresh exact witness output')
    hashes={str(a.low):digest(a.low),str(a.middle):digest(a.middle)}
    if hashes[str(a.low)]!=LOW_SHA or hashes[str(a.middle)]!=MIDDLE_SHA:
        raise ValueError('This witness is tied to the two explicitly identified completed packages')
    corr=None
    for k,row in enumerate(iter_array(a.low,'corr')):
        if k==3:
            if len(row)!=213:raise ValueError('The old complete matrix row differs')
            corr=row[0];break
    if corr is None:raise ValueError('Missing output15/source12 positive coefficient')
    row=next(iter_array(a.middle,'gamma_rows'))
    if row['output_cell']!=12:raise ValueError('The first true causal output is not cell12')
    source=next(s for s in row['sources'] if s['source_cell']==15)
    gamma=source['gamma']
    if gamma['lower']!=gamma['upper']:raise ValueError('The chosen gamma coefficient must be one fixed dyadic upper')
    band=list(iter_array(a.middle,'bands'))[source['maximizing_band']]
    C=dyadic(*corr);H=dyadic(gamma['upper']['mantissa'],gamma['upper']['binary_exponent'])
    product=9*C*H
    checks=dict(two_selected_budget_coefficients_positive=C>0 and H>0,
                exact_two_cycle_product_above_one=product>1,
                positive_gap=product-1>0)
    result=dict(status='Exact obstruction only for the current scalar positive-budget polynomial; repair by retaining frequency support',
        checks=checks,low_entry=dict(family='corr',output_cell=15,source_cell=12,array_index=[3,0],compact= corr,
            actual_low_modal_witness=92,value=rec(C)),
        middle_entry=dict(output_cell=12,source_cell=15,array_row=0,maximizing_band=source['maximizing_band'],
            band=band,chosen_gamma=gamma,value=rec(H)),
        original428_cycle=['low(cell15)','middle(cell12)'],
        exact_product_9_H_corr=rec(product),exact_product_minus_one=rec(product-1),
        display_product=float(product),
        proof='The current budget has Phi_low15>=3*C*r_middle12 and Phi_middle12>=3*H*r_low15. Positive invariant radii would imply 1>=9*C*H>1. The same two inequalities rule out any positive weighted Lipschitz row bound below1 for this chosen majorant.',
        limitations=['These are coefficients of an upper-budget polynomial, not lower bounds on the exact PDE map.',
                     'The true auxiliary centre has frequencies <=92, so its quadratic linearization cannot couple a 258..512 perturbation directly to low output <=92. The full mean/inverse remainder is not zero.',
                     'No nonexistence of a physical solution, no altered g, and no discarded high mode are asserted.'],
        input_hashes=hashes,source_sha256=digest(Path(__file__)),
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(checks=checks,product=str(product),band=band,seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    if not all(checks.values()):raise SystemExit(1)


if __name__=='__main__':main()
