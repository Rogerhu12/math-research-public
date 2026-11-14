#!/usr/bin/env python3
"""Exact positivity bounds for a support reference read from a saved warm.

Only the reference-coordinate data are constructed; no new geometric map or
solver is produced. The physical metric is not changed.
"""
from fractions import Fraction as Q
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent


def identity(p):
    p=Path(p).resolve();raw=p.read_bytes()
    return dict(path=str(p),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def bernstein_range(poly):
    n=len(poly)-1
    values=[sum((poly[j]*Q(math.comb(k,j),math.comb(n,j)) for j in range(k+1)),Q(0))
            for k in range(n+1)]
    return min(values),max(values)


def bounded(x,digits=12):
    p=10**digits
    return Q(x.numerator*p//x.denominator,p),Q(-((-x.numerator*p)//x.denominator),p)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--checkpoint',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    if args.out.exists(): raise FileExistsError(args.out)
    cp=json.loads(gzip.decompress(args.checkpoint.read_bytes()))
    M=cp['config']['modes'];m=cp['config']['base_mode']
    cs=[float(cp['actual_primary_amplitude'])]+[float(a)*float(b) for a,b in
       zip(cp['parameters'][1:],cp['central_correction_scales'])]
    if len(cs)!=M: raise ValueError('Incomplete reference support coefficients')
    c=[Q.from_float(v) for v in cs]
    qref=Q.from_float(float(cp['warp_reference_q']))
    radius=sum((Q((m*(j+1))**2-1)*abs(v) for j,v in enumerate(c)),Q(0))
    arc_delta=sum((Q((m*(j+1))**2-1,m*(j+1))*abs(v-(qref if j==0 else 0))
                  for j,v in enumerate(c)),Q(0))
    rho_delta=sum((Q((m*(j+1))**2-1)*abs(v-(qref if j==0 else 0))
                  for j,v in enumerate(c)),Q(0))
    path=HERE/'78718-prefix-metric-supplier-storage-v1.py'
    spec=importlib.util.spec_from_file_location('support_reference_target_math',path)
    source=importlib.util.module_from_spec(spec);sys.modules[spec.name]=source;spec.loader.exec_module(source)
    knots,coefs=source.exact_clamped_spline(cp['chart'])
    cuts=sorted(set(knots+[Q(0),Q(3,4),Q(1)]))
    ranges=[];lower=Q(1);upper=Q(0)
    for left,right in zip(cuts,cuts[1:]):
        j=max(i for i,v in enumerate(knots[:-1]) if v<=left)
        poly=source.compose(coefs[j],[-knots[j],Q(1)])
        if left>=Q(3,4):
            cutoff=source.compose([Q(1),Q(0),Q(0),Q(-10),Q(15),Q(-6)],[Q(-3),Q(4)])
            poly=source.mul(poly,cutoff)
        for k in range(8):
            a=left+(right-left)*Q(k,8);b=left+(right-left)*Q(k+1,8)
            lo,hi=bernstein_range(source.compose(poly,[a,b-a]))
            lower=min(lower,lo);upper=max(upper,hi)
            ranges.append((a,b,lo,hi))
    magnitude=max(abs(lower),abs(upper))
    chart_rho=1-magnitude*radius
    assert 1-radius>Q(19,100) and chart_rho>0
    row=lambda x:dict(exact=str(x),display=float(x))
    lo,hi=bounded(magnitude)
    chart_lo,_=bounded(chart_rho)
    reference_lo,_=bounded(1-radius)
    _,arc_hi=bounded(magnitude*arc_delta)
    _,rho_hi=bounded(magnitude*rho_delta)
    report=dict(scope=__doc__,input=identity(args.checkpoint),script=identity(__file__),
                supplier=identity(path),status=cp.get('status'),solver_success=cp.get('solver_success'),
                reference_definition='c1=stored actual_primary_amplitude; cj>=2=binary64 product of stored parameter and its stored scale, then treated as exact dyadics',
                M=M,m=m,reference_coefficients_exact=[str(v) for v in c],
                reference_rho_triangle_lower=row(1-radius),
                high_support_l1=row(sum(map(abs,c[1:]),Q(0))),
                chart_chi_lower=row(lower),chart_chi_upper=row(upper),
                chart_chi_abs_upper=row(magnitude),full_chart_rho_lower=row(chart_rho),
                exact_bernstein_panels=len(ranges),
                simple_reference_rho_lower_exact=str(reference_lo),
                simple_chi_abs_upper_exact=str(hi),
                simple_full_chart_rho_lower_exact=str(chart_lo),
                simple_change_from_original_angle_upper_exact=str(arc_hi),
                simple_change_from_original_rho_upper_exact=str(rho_hi),
                BVP_calls=0,tail_calls=0,new_surface=False)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out.resolve()),bytes=args.out.stat().st_size,
                         reference_rho_lower=str(reference_lo),chi_abs_upper=str(hi),
                         full_chart_rho_lower=str(chart_lo),
                         angle_change_upper=str(arc_hi),rho_change_upper=str(rho_hi),
                         panels=len(ranges))))


if __name__=='__main__': main()
