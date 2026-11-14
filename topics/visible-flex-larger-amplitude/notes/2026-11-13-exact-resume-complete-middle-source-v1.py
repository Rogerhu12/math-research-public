#!/usr/bin/env python3
"""Exact complete high-source mass from all46 paid low-centre field caps.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The full mean, numerator zero coefficient and complete inverse are retained.
This is a source bound, not a full middle/high or outer fixed point.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ex(v):return F(int(v['numerator']),int(v['denominator']))
def rec(v):return dict(numerator=str(v.numerator),denominator=str(v.denominator),display_only=float(v))


def conv(a,b):
    out={}
    for m,x in a.items():
        for n,y in b.items():out[m+n]=out.get(m+n,F(0))+x*y
    return out


def add(a,b):
    out=dict(a)
    for m,x in b.items():out[m]=out.get(m,F(0))+x
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--spectral',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--inverse-degree',type=int,default=6)
    ap.add_argument('--rss-kib',type=int,default=98304)
    a=ap.parse_args();start=time.monotonic()
    if a.inverse_degree!=6:raise ValueError('This actual recipe fixes the complete degree6 inverse polynomial')
    packet=Path(str(a.out_prefix)+'.json.gz');summary=Path(str(a.out_prefix)+'-summary.json')
    if packet.exists() or summary.exists():raise FileExistsError('Use fresh complete source output')
    s=json.loads(a.spectral.read_text())
    if not s['all_gates'] or not all(s['gates'].values()) or [r['mode'] for r in s['field_caps']]!=list(range(2,93,2)):
        raise ValueError('All original46 field caps and gates are required')
    C=F(10);V0=F(2)**-40
    if not ex(s['final_field_norm'])<C:raise ArithmeticError('The complete actual centre bound changed')
    # Each signed coefficient is bounded by its entire paid pair cap.
    # Duplicating the cap at both signs is conservative and requires no parity assertion.
    coeff={sign*r['mode']:ex(r['upper']) for r in s['field_caps'] for sign in (-1,1)}
    total=sum(coeff.values(),F(0))
    if not total<2*C:raise ArithmeticError('Actual signed coefficient overestimate is inconsistent')
    leading={m:F(5,4)*V0*x for m,x in coeff.items()}
    leading[0]=4*C*C*V0*V0
    numerator={m:F(23,18)*x for m,x in conv(coeff,coeff).items()}
    numerator=add(numerator,{m:10*C*C*V0*x for m,x in coeff.items()})
    numerator[0]=numerator.get(0,F(0))+16*C**4*V0*V0
    L=sum(leading.values(),F(0));Q=sum(numerator.values(),F(0))
    if not 0<L<1:raise ArithmeticError('The full geometric inverse domain is unpaid')
    inverse={0:F(1)};term={0:F(1)}
    for k in range(1,7):
        term=conv(term,leading);inverse=add(inverse,term)
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Owned source consumer RSS limit')
    poly=conv(numerator,inverse)
    remainder=Q*L**7/(1-L)
    pair=[dict(mode=m,polynomial_pair_mass=rec(poly.get(m,F(0))+poly.get(-m,F(0))))
          for m in range(2,max(abs(m) for m in poly)+1,2)]
    middle_poly=sum((ex(r['polynomial_pair_mass']) for r in pair if 94<=r['mode']<=5758),F(0))
    near_poly=sum((ex(r['polynomial_pair_mass']) for r in pair if 94<=r['mode']<=184),F(0))
    rest_poly=sum((ex(r['polynomial_pair_mass']) for r in pair if 186<=r['mode']<=5758),F(0))
    high_poly=sum((ex(r['polynomial_pair_mass']) for r in pair if r['mode']>=5760),F(0))
    full=middle_poly+remainder
    gates=dict(all46_original_caps=True,complete_centre_below10=True,
               signed_majorant_total_below20=total<20,complete_inverse_domain=L<1,
               exact_polynomial_support_to736=max(abs(m) for m in poly)==736,
               numerator_zero_coefficient_retained=0 in numerator,
               complete_mean_terms_retained=True,shared_inverse_tail_retained=True,
               all_modes94_to5758_included=True,all_modes5760_and_above_included=True,
               physical_mean_domain_10V0_below_one_over64=10*V0<F(1,64))
    if not all(gates.values()):raise ArithmeticError('An exact complete source gate failed')
    result=dict(schema='visible-flex-complete-high-source-from46-caps-v1',
        author='exact_closure (GPT-6 Astra Pro; AI-assisted)',
        status='Proved complete source mass bounds for the same R101 low46 centre',
        all_gates=True,gates=gates,constant_strip='18/125',source_units='c_bg V_I^2 in source-x; signed Fourier weak mass',
        fixed_centre_bound='10',fixed_V_upper='2^-40',coefficient_duplication='Each signed coefficient receives its entire pair cap; no real-parity equality is assumed',
        signed_field_majorant_total=rec(total),complete_leading_norm_upper=rec(L),complete_numerator_norm_upper=rec(Q),
        inverse_polynomial_degree=6,shared_complete_inverse_tail=rec(remainder),polynomial_pair_rows=pair,
        complete_middle_shared_mass=rec(full),near_polynomial_mass=rec(near_poly),rest_polynomial_mass=rec(rest_poly),
        complete_infinite_high_shared_mass=rec(high_poly+remainder),
        tail_mass_must_be_paid_once_across_any_joint_partition=True,
        formula='A_m=a_|m| at each sign; L=(5/4)V0 A+4 C0^2 V0^2 delta0; B=(23/18)A*A+10 C0^2 V0 A+16 C0^4 V0^2 delta0; polynomial=B*sum(k=0..6)L^k; shared remainder=||B|| ||L||^7/(1-||L||)',
        physical_source_changed=False,full_middle_kernel_paid=False,nonlinear_fixed_point_claimed=False,
        input_hashes={str(a.spectral):sha(a.spectral)},source_sha256=sha(__file__),
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with packet.open('wb') as raw:
      with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0,compresslevel=9) as packed:
        packed.write((json.dumps(result,separators=(',',':'))+'\n').encode())
    if packet.stat().st_size>=5_000_000:raise ArithmeticError('The compressed complete source exceeded the repository limit')
    brief={k:v for k,v in result.items() if k!='polynomial_pair_rows'}
    brief['primary_packet']={'path':str(packet),'bytes':packet.stat().st_size,'sha256':sha(packet)}
    summary.write_text(json.dumps(brief,indent=2)+'\n')
    print(json.dumps(dict(all_gates=True,complete_middle_shared_mass=float(full),
        complete_infinite_high_shared_mass=float(high_poly+remainder),
        shared_tail=float(remainder),elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
