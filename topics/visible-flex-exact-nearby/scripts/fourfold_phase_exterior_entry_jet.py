#!/usr/bin/env python3
"""Exact-family physical entry jets for a C4 exterior graft at material r=3.

These are jets of the complete weighted scalar splines, including the exact
height antiderivative.  No derivative of a rounded physical export is used.
Coefficients are Taylor coefficients, hence include division by j factorial.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import time

from flint import arb,acb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_parameter_germ import ParameterGermBulkTarget,provenance,sha
from fourfold_phase_beta_interval import ball_record


def entry_germs(target,cut=Fraction(3)):
    knots=sorted({abs(Fraction.from_float(float(x)))
                  for key,values in target.frozen.items() if key.endswith('_knots') for x in values})
    left=max(x for x in knots if x<cut)
    target.set_cell(left,cut)
    old,ctx.cap=ctx.cap,8
    beta,gamma,radius,height=target.scalars(acb(exact_arb(cut)),1)
    log_radius=radius.log()
    slope_ratio=height.derivative()/(radius*radius)
    def real_coeff(value,j):
        coefficient=value[j]
        if not coefficient.imag.contains(0):
            raise ValueError('a physical entry coefficient lost its real structure')
        return coefficient.real
    result=dict(cut=cut,last_common_span=(left,cut),
        beta=[[real_coeff(value,j) for j in range(5)] for value in beta],
        gamma=[[real_coeff(value,j) for j in range(5)] for value in gamma],
        radius=[real_coeff(radius,j) for j in range(5)],
        height=[real_coeff(height,j) for j in range(5)],
        log_radius=[real_coeff(log_radius,j) for j in range(5)],
        slope_ratio=[real_coeff(slope_ratio,j) for j in range(4)])
    ctx.cap=old
    if not result['radius'][0]>0 or not result['slope_ratio'][0]>0:
        raise ValueError('entry radius and vertical slope ratio must be positive')
    return result


def serializable_entry(entry):
    out=dict(cut=str(entry['cut']),last_common_span=list(map(str,entry['last_common_span'])),
             coefficient_convention='coefficient j = physical radial derivative of order j / j!')
    for key in ('beta','gamma'):
        out[key]=[[ball_record(v) for v in row] for row in entry[key]]
    for key in ('radius','height','log_radius','slope_ratio'):
        out[key]=[ball_record(v) for v in entry[key]]
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--center-object',type=Path,required=True)
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,2000000))
    ap.add_argument('--bits',type=int,default=192)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits;ctx.cap=8;started=time.monotonic()
    target=ParameterGermBulkTarget(args.center_object,args.half_width,256,512,
                                  arb('.003'),arb('.0025'),arb('.32'))
    entry=entry_germs(target)
    identity=provenance(target,args.center_object);identity.pop('dependency_sha256')
    here=Path(__file__).parent
    report=dict(kind='actual_affine_C4_exterior_entry_scalar_jets',complete=True,**identity,
        bits=args.bits,entry=serializable_entry(entry),
        dependency_sha256={name:sha(here/name) for name in (
            'fourfold_phase_beta_parameter_germ.py','fourfold_phase_beta_parameter_root.py',
            'fourfold_phase_beta_affine.py','fourfold_phase_beta_interval.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_beta_bulk_box.py',
            'fourfold_phase_beta_combine.py')},
        elapsed_seconds=time.monotonic()-started,
        scope=['Exact-family scalar jets only, before any proposed exterior is constructed.',
               'All coefficients are enclosed over the full shared parameter interval.',
               'No outside positive-domain, isometry, or flat-held-cap claim is made by this file.'])
    report['source_sha256']=sha(__file__)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(log_radius=[v.str(14) for v in entry['log_radius']],
                         slope_ratio=[v.str(14) for v in entry['slope_ratio']],
                         height=entry['height'][0].str(14),
                         elapsed_seconds=report['elapsed_seconds']),indent=2),flush=True)


if __name__=='__main__':main()
