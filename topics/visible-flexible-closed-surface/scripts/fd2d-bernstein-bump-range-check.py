#!/usr/bin/env python3
"""Actual current-input range check; no nonlinear or actual-body solve."""
import argparse
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
import json
import resource
import time

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import aq,bound_record
from fd2d_gc_r136_arb_profile import R136ArbProfile
from fd2d_gc_r136_bernstein_bumps import BernsteinBumpProfile,exact_bump_range


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--profile',type=Path,required=True)
    ap.add_argument('--profile-sha256',required=True);ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic()
    old=R136ArbProfile.from_packet(args.profile,expected_sha256=args.profile_sha256)
    new=BernsteinBumpProfile.from_packet(args.profile,expected_sha256=args.profile_sha256)
    if old.input_binding_sha256!=new.input_binding_sha256:raise AssertionError('The target binding changed')
    checks=0
    for left,right in new.supports:
        width=right-left
        for t in (F(0),F(1,8),F(1,2),F(7,8),F(1)):
            lo=max(F(0),t-F(1,16));hi=min(F(1),t+F(1,16))
            for d in range(4):
                value=F(0)
                for k in range(d+1):
                    j=d-k
                    scale=comb(d,k)*factorial(5)//factorial(5-k)
                    scale*=((-1)**j)*factorial(5)//factorial(5-j)
                    value+=scale*t**(5-k)*(1-t)**(5-j)
                value*=F(1024)/width**d
                box=exact_bump_range(left+width*lo,left+width*hi,left,right,d)
                if not box.contains(aq(value)):raise AssertionError(('Exact derivative escaped',d,str(t)))
                checks+=1
    rows=[];lo,hi=F(17,20),F(1468,1000)
    for j in range(80):
        x=lo+(hi-lo)*j/80;y=lo+(hi-lo)*(j+1)/80
        a=old.physical_box(x,y);b=new.physical_box(x,y)
        rows.append(dict(start_exact=str(x),stop_exact=str(y),start=float(x),stop=float(y),
            old_K=bound_record(a['K']),new_K=bound_record(b['K']),
            sign='positive' if b['K']>0 else 'negative' if b['K']<0 else 'unresolved',
            old_a_ss_width=float(a['a_ss'].upper()-a['a_ss'].lower()),
            new_a_ss_width=float(b['a_ss'].upper()-b['a_ss'].lower()),
            old_a_sss_width=float(a['a_sss'].upper()-a['a_sss'].lower()),
            new_a_sss_width=float(b['a_sss'].upper()-b['a_sss'].lower())))
    segments=[]
    for r in rows:
        if segments and segments[-1]['sign']==r['sign']:
            s=segments[-1];s['stop']=r['stop'];s['stop_exact']=r['stop_exact']
            s['K_lower']=min(s['K_lower'],r['new_K']['lower_display'])
            s['K_upper']=max(s['K_upper'],r['new_K']['upper_display'])
        else:segments.append({**{k:r[k] for k in ('start','stop','start_exact','stop_exact','sign')},
                              'K_lower':r['new_K']['lower_display'],'K_upper':r['new_K']['upper_display']})
    report=dict(schema='fd2d-R171-Bernstein-bump-actual-range-check-v1',passed=True,
        source=identity(__file__),evaluation_source=identity(Path(__file__).with_name('fd2d_gc_r136_bernstein_bumps.py')),
        original_packet=identity(args.profile),target_binding_unchanged=new.input_binding_sha256,
        exact_scalar_derivative_checks=checks,continuous_late_boxes=rows,sign_segments=segments,
        analytic_target_and_all_derivatives_unchanged=True,
        runtime_or_surface_error_bound=False,whole_F_J_BVP_frame_body_run=False,
        seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out=Path(str(args.out_prefix)+'-report.json')
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed=True,checks=checks,segments=segments,seconds=report['seconds'],
                         peak_rss_kib=report['peak_rss_kib'],report=identity(out))))


if __name__=='__main__':main()
