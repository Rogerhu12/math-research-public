#!/usr/bin/env python3
"""Intersect new all213 canonical auxiliary caps with the SAME R100 input.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Keeps the original six product axes, transverse shared1/32 l1 ball,
true46 lift columns, original q strip, V'=257/256 Vs and all true far.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def ex(v):
    if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
    return F(int(v['numerator']),int(v['denominator']))


def up(x,bits=160):
    x=F(x)
    if x<0:raise ArithmeticError('Positive bounds only')
    if not x:return x
    e=x.numerator.bit_length()-x.denominator.bit_length()-bits+1;unit=F(2)**e;y=x/unit
    ans=((y.numerator+y.denominator-1)//y.denominator)*unit
    if ans<x:raise ArithmeticError('Outward rounding went inward')
    return ans


def pack(x):
    x=up(x);d=x.denominator
    if d&(d-1):raise ArithmeticError('Dyadic output required')
    return [str(x.numerator),-(d.bit_length()-1)]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('original','bootstrap','bootstrap-resource','out'):p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('Keep the exact original bridge immutable')
    old=read(a.original);boot=read(a.bootstrap);usage=read(a.bootstrap_resource)
    if sha(a.original)!='28161832153c4f0b3e632f4c4fba2741b9b90d198a4d75ff5761a18a72c8fa8f':raise ArithmeticError('Original all213 actual R100 input required')
    if not(old['all_gates'] and boot['all_gates'] and all(boot['gates'].values()) and boot['schema']=='inner-r74-all213-canonical-modal-finite-bootstrap-v1'
           and boot['cells']==old['cells']==list(range(12,225)) and boot['modes']==old['modes']==list(range(2,93,2))
           and usage['exitcode']==0 and usage['termination_signal'] is None):raise ArithmeticError('Same complete actual bootstrap required')
    provenance=[]
    for n,(row,br) in enumerate(zip(old['rows'],boot['rows'])):
        if not row['cell']==br['cell']==n+12:raise ArithmeticError('Canonical source order changed')
        ratio=ex(br['reference_x_upper'])/ex(row['R100_Xbar'])
        factors=list(map(ex,row['decay_pair_factors']));linear=list(map(ex,row['Cs_linear_pair_caps']))
        errors=[min(ex(row['Cs_correction_pair_caps'][j]),up(ratio*ex(br['final_correction_pair_caps_over_reference'][j])*factors[j])) for j in range(46)]
        complete=[min(ex(row['Cs_complete_pair_caps'][j]),up(ratio*ex(br['final_complete_pair_caps_over_reference'][j])*factors[j]),up(linear[j]+errors[j])) for j in range(46)]
        error_common=min(ex(row['Cs_correction_common_cap']),up(ratio*ex(br['final_correction_common_cap_over_reference'])*factors[0]),up(sum(errors,F(0))))
        cs_common=min(ex(row['Cs_common_cap']),up(ratio*ex(br['final_complete_common_cap_over_reference'])*factors[0]),up(sum(complete,F(0))),up(sum(linear,F(0))+error_common))
        lam=list(map(ex,row['Lambda_pair_caps_at_radius1over32']));lam_common=ex(row['Lambda_common_cap_at_radius1over32'])
        base=[up(c+l) for c,l in zip(complete,lam)];common=min(up(cs_common+lam_common),up(sum(base,F(0))))
        if not(cs_common>0 and error_common>0 and all(x>0 for x in complete) and common<=ex(row['Cs_plus_Lambda_common_cap'])):raise ArithmeticError('Same-field intersection failed')
        provenance.append(dict(cell=12+n,old_Cs_common=row['Cs_common_cap'],new_Cs_common=pack(cs_common),bootstrap_reference_x_upper=br['reference_x_upper'],canonical_to_physical_ratio=dict(numerator=str(ratio.numerator),denominator=str(ratio.denominator))))
        row.update(Cs_correction_pair_caps=list(map(pack,errors)),Cs_complete_pair_caps=list(map(pack,complete)),Cs_common_cap=pack(cs_common),Cs_correction_common_cap=pack(error_common),
            Cs_plus_Lambda_pair_caps=list(map(pack,base)),Cs_plus_Lambda_common_cap=pack(common),Cs_provenance='Intersection with actual all213 canonical modal finite bootstrap, same existing auxiliary family')
    old.update(source_sha256=sha(__file__),all_gates=True,canonical_bootstrap_applied=True,canonical_bootstrap_provenance=provenance,
        fresh_input_identities={k:dict(path=str(getattr(a,k)),sha256=sha(getattr(a,k))) for k in ('original','bootstrap','bootstrap_resource')},
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    old['gates'].update(all213_same_reference_canonical_intersections=True,all_original_transverse_columns_unchanged=True,all_original_common_l1_budgets_unchanged=True)
    raw=(json.dumps(old,separators=(',',':'))+'\n').encode();a.out.write_bytes(gzip.compress(raw,mtime=0))
    if a.out.stat().st_size>=5_000_000:raise ArithmeticError('Split the complete modal transfer')
    print(json.dumps(dict(all_gates=True,path=str(a.out),sha256=sha(a.out),bytes=a.out.stat().st_size,elapsed_seconds=old['elapsed_seconds'],peak_rss_kib=old['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
