#!/usr/bin/env python3
"""Exact frozen-target warp bounds on the final requested common-cut width.

Uses the existing Fraction clamped spline definition, not rounded SciPy PP
coefficients. This supplies rho/b constants; it does not bound a or the new
bridge rescaling, and does not inspect or alter a nonlinear solver.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

HERE=Path(__file__).resolve().parent


def identity(path):
    path=Path(path).resolve(); data=path.read_bytes()
    return dict(path=str(path),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())


def bernstein_range(poly):
    n=len(poly)-1
    values=[sum((poly[j]*Q(math.comb(k,j),math.comb(n,j)) for j in range(k+1)),Q(0))
            for k in range(n+1)]
    return min(values),max(values)


def row(v): return dict(exact=str(v),float=float(v))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--checkpoint',type=Path,required=True)
    ap.add_argument('--width',type=float,default=.15)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists(): raise FileExistsError(args.out)
    start=time.monotonic()
    cp=json.loads(gzip.decompress(args.checkpoint.read_bytes()))
    path=HERE/'78718-prefix-metric-supplier-storage-v1.py'
    spec=importlib.util.spec_from_file_location('warp_target_math',path)
    source=importlib.util.module_from_spec(spec);sys.modules[spec.name]=source;spec.loader.exec_module(source)
    knots,coeff=source.exact_clamped_spline(cp['chart'])
    end=Q.from_float(float(cp['meridian_length']))
    width=Q.from_float(args.width)
    if not 0<width<end: raise ValueError('Invalid window')
    # Original np.searchsorted uses this binary subtraction. Cover its exact
    # dyadic value and one further downward ulp, without assuming width=3/20.
    threshold=float(cp['meridian_length'])-args.width
    left=Q.from_float(math.nextafter(threshold,-math.inf))
    if left<Q(3,4)*end: raise ValueError('Window reaches pre-cutoff regime')
    warp=8*Q.from_float(float(cp['warp_reference_q']))
    cuts=sorted(set([left/end,Q(1)]+[x for x in knots if left/end<x<1]))
    maximum_e=Q(0); maximum_ep=Q(0); pieces=[]
    for l,r in zip(cuts,cuts[1:]):
        j=max(i for i,x in enumerate(knots[:-1]) if x<=l)
        h=source.compose(coeff[j],[-knots[j],Q(1)])
        cutoff=source.compose([Q(1),Q(0),Q(0),Q(-10),Q(15),Q(-6)],[Q(-3),Q(4)])
        e=source.scale(source.mul(h,cutoff),warp)
        ep=source.scale(source.der(e),1/end)
        for v in range(8):
            a=l+(r-l)*Q(v,8); b=l+(r-l)*Q(v+1,8)
            er=bernstein_range(source.compose(e,[a,b-a]))
            dr=bernstein_range(source.compose(ep,[a,b-a]))
            ee=max(map(abs,er)); dd=max(map(abs,dr))
            maximum_e=max(maximum_e,ee); maximum_ep=max(maximum_ep,dd)
            pieces.append(dict(left_normalized_exact=str(a),right_normalized_exact=str(b),
                               e_min_exact=str(er[0]),e_max_exact=str(er[1]),
                               ep_min_exact=str(dr[0]),ep_max_exact=str(dr[1])))
    if not maximum_e<1: raise ValueError('No positive target chart lower bound')
    rho=1-maximum_e
    bupper=maximum_ep/(3*rho)
    def ceil_grid(x,n=12):
        scale=10**n; k=(x.numerator*scale+x.denominator-1)//x.denominator
        return Q(k,scale)
    esafe=ceil_grid(maximum_e); epsafe=ceil_grid(maximum_ep); bsafe=ceil_grid(bupper)
    report=dict(schema='78718-common-cut-exact-warp-bounds-v1',scope=__doc__,
                input=identity(args.checkpoint),supplier=identity(path),script=identity(__file__),
                checkpoint_status=cp.get('status'),checkpoint_solver_success=cp.get('solver_success'),
                target_chart_definition='exact_clamped_spline(chart) times original quintic cutoff',
                end_exact=str(end),requested_width_exact=str(width),covered_left_exact=str(left),
                covered_width_exact=str(end-left),panels=len(pieces),panel_bounds=pieces,
                absolute_e_upper=row(maximum_e),absolute_ep_upper=row(maximum_ep),
                rho_lower=row(rho),convective_b_absolute_upper=row(bupper),
                simple_safe_e_upper_exact=str(esafe),simple_safe_ep_upper_exact=str(epsafe),
                simple_safe_rho_lower_exact=str(1-esafe),simple_safe_b_upper_exact=str(bsafe),
                radius_or_radial_rescaling_bound=False,geometry_candidate_generated=False,
                BVP_calls=0,tail_calls=0,seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(output=identity(args.out),panels=len(pieces),
                         e_upper=float(maximum_e),ep_upper=float(maximum_ep),
                         rho_lower=float(rho),b_upper=float(bupper),
                         safe_e_upper=str(esafe),safe_ep_upper=str(epsafe),
                         safe_rho_lower=str(1-esafe),safe_b_upper=str(bsafe),
                         seconds=report['seconds']),sort_keys=True))


if __name__=='__main__': main()
