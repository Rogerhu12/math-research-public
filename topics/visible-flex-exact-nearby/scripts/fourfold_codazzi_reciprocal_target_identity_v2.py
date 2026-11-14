#!/usr/bin/env python3
"""Compare the stable new target jets with the full unscaled metric identity.

This is a necessary implementation check of the new radius cancellation and
compact metric transformation. It is not an existence or inverse certificate.
"""
from __future__ import annotations
import argparse,math,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_cubic_target_jets import CubicCodazziTarget,series_sqrt
from fourfold_codazzi_high_target_jets import series_mul,series_inv,series_dr
from fourfold_codazzi_reciprocal_compact_target_jets import (
    ReciprocalCompactTargetJets,bump_series,exponential,scale,add,power)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha


def direct_jets(original,r,nu):
    a=[original['a' if j==0 else 'a'+str(j)]/math.factorial(j) for j in range(6)]
    E=[original['E' if j==0 else 'E'+str(j)]/math.factorial(j) for j in range(5)]
    factor=exponential(scale(bump_series(r,r,exact_arb(r)),exact_arb(nu)))
    En=series_mul(E,factor);ia=series_inv(a);ie=series_inv(En)
    ap=series_dr(a);app=series_dr(ap);Ep=series_dr(En)
    curvature=add(scale(series_mul(series_mul(app,ia),ie),-1),
        scale(series_mul(series_mul(series_mul(ap,Ep),ia),power(ie,2)),arb(1)/2))
    gamma=series_mul(series_sqrt(En),ia)
    beta=series_mul(ap,ia)
    gap=add(En,scale(series_mul(ap,ap),-1))
    if not gap[0]>0:raise ValueError('the independent unscaled chart gap is unresolved')
    reciprocal=scale(series_mul(series_mul(a,series_sqrt(En)),series_inv(series_sqrt(gap))),-1)
    out={}
    for name,values in (('gamma',gamma),('beta',beta),('K',curvature),('s',reciprocal)):
        for j in range(4):out[name+(str(j) if j else '')]=math.factorial(j)*values[j]
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--nu',type=Fraction,default=Fraction(-8203900476603349,288230376151711744))
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    if args.out.exists():raise FileExistsError('retain the original identity report')
    ctx.prec=192;ctx.cap=6;start=time.monotonic()
    stable=ReciprocalCompactTargetJets(args.object,Fraction(0),512)
    direct=CubicCodazziTarget(args.object,Fraction(0),512,1024)
    rows=[];failure=None
    for r in (Fraction(0),Fraction(3,40),Fraction(23,200),Fraction(17,100),Fraction(2,5),Fraction(3,2)):
        old=direct.coefficients(r,r)
        for nu in (Fraction(0),args.nu):
            try:
                calculated,germ=stable.coefficients(r,r,nu);independent=direct_jets(old,r,nu)
                checks={name:dict(overlap=bool(value.overlaps(independent[name])),
                    stable=record(value),unscaled=record(independent[name]))
                    for name,value in calculated.items() if name in independent}
                row=dict(radius=str(r),nu=str(nu),germ=list(map(str,germ)),checks=checks)
                rows.append(row)
                if not all(v['overlap'] for v in checks.values()):
                    raise ValueError('the actual direct and cancelled target jets disagree')
            except Exception as error:
                failure=dict(radius=str(r),nu=str(nu),error_type=type(error).__name__,message=str(error));break
        if failure is not None:break
    report=dict(kind='complete_new_compact_metric_target_identity',complete=failure is None,
        failure=failure,object_sha256=sha(args.object),source_sha256=sha(__file__),
        stable_provider_sha256=sha(Path(__file__).with_name('fourfold_codazzi_reciprocal_compact_target_jets.py')),
        unscaled_provider_sha256=sha(Path(__file__).with_name('fourfold_codazzi_cubic_target_jets.py')),
        exact_original_parameter_half_width='0',complete_infinite_primitive=True,
        coefficients_per_point=16,rows=rows,nonlinear_existence_proved=False,
        wall_seconds=time.monotonic()-start)
    save(args.out,report)
    print(dict(complete=report['complete'],failure=failure,rows=len(rows),wall_seconds=report['wall_seconds']))
    if failure is not None:raise SystemExit(2)


if __name__=='__main__':main()
