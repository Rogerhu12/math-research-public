#!/usr/bin/env python3
"""Exact-rational continuous-position bounds from completed R68 panel records.

No source, ODE, interval-library or nonlinear evaluation is repeated. Logarithms
of exact dyadic frame ratios use a proved positive atanh series remainder;
each resulting upper bound is rounded upward to the fixed 2^-128 grid.
The input's diagonal integrals plus frame jumps are kept as exact dyadics.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import re
import resource
import time
from decimal import Decimal, localcontext, ROUND_CEILING


def digest(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda:f.read(1048576),b''):
            h.update(chunk)
    return h.hexdigest()


def endpoint(value):
    m=int(value['mantissa']); e=int(value['binary_exponent'])
    return Q(m*(1<<e)) if e>=0 else Q(m,1<<(-e))


def upper(value):
    return endpoint(value['upper'])


def ceil_grid(value,bits=128):
    n=value.numerator*(1<<bits); d=value.denominator
    return Q(-((-n)//d),1<<bits)


def series_log_upper(value):
    if not 1<=value<=2:
        raise ValueError('The normalized log argument must lie in[1,2]')
    z=(value-1)/(value+1); zz=z*z; power=z; result=Q(0)
    for k in range(8):
        result+=power/(2*k+1)
        power*=zz
    # The remaining denominators are at least17, and 0<=z<=1/3.
    result+=power/(17*(1-zz))
    return ceil_grid(2*result)


LOG2_UPPER=series_log_upper(Q(2))


def log_upper(value):
    if value<1:
        raise ValueError('Use the positive reciprocal for a negative log')
    k=value.numerator.bit_length()-value.denominator.bit_length()
    power=Q(1<<k) if k>=0 else Q(1,1<<(-k))
    if value<power:
        k-=1;power/=2
    normalized=value/power
    assert k>=0 and 1<=normalized<2
    return ceil_grid(k*LOG2_UPPER+series_log_upper(normalized))


def positive_pair(value):
    return (log_upper(value),Q(0)) if value>=1 else (Q(0),log_upper(1/value))


def record(value):
    d=value.denominator
    if d&(d-1):
        raise ValueError('Every returned bound must be exactly dyadic')
    with localcontext() as c:
        c.prec=35;c.rounding=ROUND_CEILING
        display=str(Decimal(value.numerator)/Decimal(value.denominator))
    return dict(mantissa=str(value.numerator),binary_exponent=-(d.bit_length()-1),
                decimal_upper=display)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--rss-kib',type=int,default=30720)
    args=ap.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('Use a fresh exact postprocessing result')
    data=json.loads(args.input.read_text())
    if data['cells']!=[11,10] or not all(data['gates'].values()):
        raise ValueError('Require the original complete and successful R68 panel stream')
    inputs={str(args.input):digest(args.input)}
    first=previous=blo=bhi=None
    forward=inverse=positive_forward=positive_inverse=phase=Q(0)
    max_forward=max_inverse=Q(0);loc_f=loc_i=None;count=0
    derivation=hashlib.sha256();cell_rows=[]
    files=[v for v in data['files'] if v['path'].endswith('-panels.jsonl.gz')]
    if len(files)!=18:raise ValueError('All18 exact panel packets are required')
    for packet_index,packet in enumerate(files):
        path=Path(packet['path'])
        if digest(path)!=packet['sha256']:raise ValueError('A completed panel packet changed')
        inputs[str(path)]=packet['sha256']
        match=re.search(r'-cell(\d+)-seg(\d+)-panels',path.name)
        cell,segment=map(int,match.groups());panel_count=0
        with gzip.open(path,'rt') as stream:
            for line in stream:
                row=json.loads(line);b=upper(row['chosen_frame'])
                if endpoint(row['chosen_frame']['lower'])!=b or b<=0:
                    raise ValueError('The chosen frame is not one exact positive dyadic')
                nf=upper(row['new_forward_with_jump']);ni=upper(row['new_backward_with_jump'])
                g=upper(row['new_phase']);assert g>=0
                if first is None:
                    first=b;first_plus,first_minus=positive_pair(b)
                    blo=bhi=b
                plus,minus=positive_pair(b)
                jf,ji=(Q(0),Q(0)) if previous is None else positive_pair(previous/b)
                # R68(68.7) bounds every partial panel and its entering jump.
                pf=max(nf,jf);pi=max(ni,ji)
                f=forward+pf+first_minus+plus
                i=inverse+pi+minus+first_plus
                location=dict(cell=cell,segment=segment,panel=row['index'])
                if f>max_forward:max_forward=f;loc_f=location
                if i>max_inverse:max_inverse=i;loc_i=location
                positive_forward+=max(Q(0),nf,jf)
                positive_inverse+=max(Q(0),ni,ji)
                forward+=nf;inverse+=ni;phase+=g
                blo=min(blo,b);bhi=max(bhi,b);previous=b
                count+=1;panel_count+=1
                derivation.update((json.dumps(dict(location=location,forward=record(forward),
                    inverse=record(inverse),prefix_forward=record(f),prefix_inverse=record(i)),
                    sort_keys=True,separators=(',',':'))+'\n').encode())
                if count%128==0 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>args.rss_kib:
                    raise MemoryError('The observed standard-library RSS guard failed')
        if panel_count!=packet['panels']:raise ValueError('A complete original packet was truncated')
        if segment==8:
            endpoint_record=data['rows'][len(cell_rows)]
            assert endpoint_record['cell']==cell
            if not phase<=upper(endpoint_record['budgets']['new']['cumulative_phase_upper']):
                raise ArithmeticError('The exact full phase sum exceeds its existing certified bound')
            global_endpoint_cost=positive_pair(1/blo)[0] if blo<1 else Q(0)
            global_endpoint_cost+=positive_pair(bhi)[0] if bhi>1 else Q(0)
            cell_rows.append(dict(cell=cell,cumulative_panels=count,
                all_positions_from_cut_log_prefactor=record(max_forward),
                all_positions_to_cut_log_prefactor=record(max_inverse),
                all_position_pairs_forward_log_prefactor=record(positive_forward+global_endpoint_cost),
                all_position_pairs_inverse_log_prefactor=record(positive_inverse+global_endpoint_cost),
                maximum_forward_location=loc_f,maximum_inverse_location=loc_i,
                minimum_frame=record(blo),maximum_frame=record(bhi),
                exact_sum_of_certified_panel_phases=record(phase),
                certified_phase_upper=endpoint_record['budgets']['new']['cumulative_phase_upper']))
            print(json.dumps(dict(event='complete_continuous_frame_cell',cell=cell,panels=count,
                forward=record(max_forward)['decimal_upper'],inverse=record(max_inverse)['decimal_upper'])),flush=True)
    result=dict(scope=__doc__,input_sha256=inputs,source_sha256=digest(Path(__file__)),
        panels=count,rows=cell_rows,atanh_terms=8,log_grid_bits=128,log2_upper=record(LOG2_UPPER),
        derivation_rows_sha256=derivation.hexdigest(),
        intermediate_policy='Each exact prefix row is deterministically reproduced by this script; primary input packets and the complete maxima are retained.',
        gates=dict(all_original_panels_consumed=count==data['panels']==10793,
            complete_continuous_partial_panels=True,both_endpoint_factors=True,
            every_source_packet_hash_checked=True,no_new_source_ODE_or_mean_evaluation=True,
            positive_log_remainders_and_upward_rounding=True),
        nonlinear_source_or_Schur_inverse_paid=False,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if not all(result['gates'].values()):raise ArithmeticError('A required complete-coverage gate failed')
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>args.rss_kib:
        raise MemoryError('The final observed RSS guard failed')
    print(json.dumps(dict(event='continuous_frame_complete',panels=count,seconds=time.monotonic()-started,
        peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
