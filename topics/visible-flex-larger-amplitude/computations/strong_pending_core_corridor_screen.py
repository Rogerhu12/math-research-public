#!/usr/bin/env python3
"""Exact finite planar-budget check on an explicitly unaccepted raw core.

No source is relabeled as converged. Two artificial planar continuations keep
all c6+ coefficients of the raw iterate fixed: the old R40 c4 slope, or an
affine return to the canonical c4 at the landing q. A failure is a failure of
that finite planar budget only, not nonexistence or failure of a real surface.
No NumPy, physical RHS, Jacobian, tail, geometry or BVP is evaluated.
"""
from __future__ import annotations
import argparse
import array
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path
import resource
import time

import strong_core_corridor_refresh as certificate
import strong_actual_checkpoint_step_scale as raw_arrays


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);b=path.read_bytes()
    return json.loads(gzip.decompress(b) if path.suffix=='.gz' else b)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raw',type=Path,required=True)
    parser.add_argument('--reference',type=Path,required=True)
    parser.add_argument('--landing-q',default='.402')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    begin=time.monotonic()
    raw,reference=read(args.raw),read(args.reference)
    ident=raw['identity'];M=ident['modes'];q=ident['gauge'];piece_hashes={}
    p=raw_arrays.read_vector(args.raw,raw,'p',piece_hashes)
    if p.tobytes()!=array.array('d',raw['parameter_state']).tobytes():
        raise ValueError('The raw manifest parameter copy differs from its hash-checked complete array')
    if (raw.get('solver_success') is not False or raw.get('physical_surface') is not False
            or raw['provenance'].get('phase')!='accepted-newton'
            or not raw['provenance'].get('actual_coupled_acceptance_pending')
            or ident['coupling_context']['baseline_sha256']!=sha(args.reference)
            or len(p)!=M+3 or len(reference['central_correction_scales'])!=M-1
            or reference['gauge_amplitude']!=q):
        raise ValueError('Require the explicitly pending complete all-core+geometry raw and linked reference')
    # These are the same binary64 coefficient operations as actual_coefficients.
    floats=[q*math.exp(float(p[0]))]+[a*b for a,b in zip(p[1:M],reference['central_correction_scales'])]
    floats[1]+=ident['reference_coefficients'][1]
    c=[F.from_float(value) for value in floats]
    target=F(args.landing_q)
    if not target>c[0]:raise ValueError('Use an increasing artificial primary amplitude')
    lo,hi=F('0.7071067811865475'),F('0.7071067811865476')
    if not lo**2<F(1,2)<hi**2:raise AssertionError('Inverse sqrt2 rational enclosure failed')
    mid=(lo+hi)/2
    odd=sum(value for j,value in enumerate(c,1) if j>=3 and j%2)
    k0=F.from_float(ident['profile']['start_acceleration'])
    rows=[]
    paths=[('old_R40_slope',c[1]-(target-c[0])*mid/10,(target-c[0])*(hi-lo)/20),
           ('affine_to_canonical_landing_c4',-target*mid/10,target*(hi-lo)/20)]
    for name,landing_c4,landing_error in paths:
        endpoints=[]
        slope=(landing_c4-c[1])/(target-c[0]);slope_error=landing_error/(target-c[0])
        for at,c4,error in ((c[0],c[1],F(0)),(target,landing_c4,landing_error)):
            current=list(c);current[0],current[1]=at,c4
            gap=2*(at+odd);required=F(3,20)*gap
            polynomial=certificate.chebyshev_power([1-required-15*error]+
                [-(4*j*j-1)*value for j,value in enumerate(current,1)])
            result=certificate.positive_certificate(polynomial,12)
            short_axis=1-sum((4*j*j-1)*value*(-1)**j for j,value in enumerate(current,1))+15*error
            product=k0*gap*short_axis
            endpoints.append(dict(q=certificate.rec(at),c4_midpoint=certificate.rec(c4),
                c4_error=certificate.rec(error),axial_core_gap=certificate.rec(gap),
                future_full_D_budget=certificate.rec(5*gap),required_core_rho=certificate.rec(required),
                short_axis_rho_upper=certificate.rec(short_axis),
                R7_product_upper=certificate.rec(product),R7_less_than_one=product<1,
                radius_surplus_certificate=result))
        derivative_lower=3-15*(slope+slope_error)
        rows.append(dict(name=name,core_c4_slope_mid=certificate.rec(slope),
            core_c4_slope_error=certificate.rec(slope_error),endpoints=endpoints,
            artificial_planar_radius_corridor_certified=all(e['radius_surplus_certificate']['certified_positive'] for e in endpoints),
            short_axis_rho_derivative_lower=certificate.rec(derivative_lower),
            R7_endpoint_monotonicity_requirements=bool(derivative_lower>0 and c[0]+odd>0
                and 1-sum((4*j*j-1)*value*(-1)**j for j,value in enumerate(c,1))>0)))
    source_hashes={str(p):sha(p) for p in (args.raw,args.reference,Path(__file__),Path(certificate.__file__),
        Path(__file__).parent/'strong_actual_augmented_core.py',Path(raw_arrays.__file__))}
    source_hashes.update(piece_hashes)
    output=dict(scope=__doc__,finished=True,source_sha256=source_hashes,
        source_solver_success=False,source_physical_surface=False,actual_coupled_acceptance_pending=True,
        complete_raw_core_binary64=floats,complete_raw_core_exact=[certificate.rec(x) for x in c],
        frozen_higher_mode_count=M-2,representation_gauge=q,actual_primary_amplitude=floats[0],
        artificial_paths=rows,seconds=time.monotonic()-begin,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        physical_RHS_evaluations=0,Jacobian_evaluations=0,Node_workers=0,BVP_solves=0,
        limitations=['Input is an unaccepted actual-inner iterate, not a converged or audited surface.',
            'All high coefficients are artificially frozen; a true later BVP can change all of them.',
            'The exact statements concern only the finite support curves defined by the displayed binary64 coefficients.',
            'D<=5d is a future whole-surface budget, not its measured diameter.',
            'A negative witness rejects this rho>=.15d sufficient budget for this artificial path, not actual reach or existence.',
            'No closed held amplitude, exact isometry, continuous surface reach or topic completion follows.'])
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(event='pending_core_planar_budget_checked',file=str(args.out),
        source_solver_success=False,actual_primary=floats[0],seconds=output['seconds'],peak_rss_kib=output['peak_rss_kib'],
        paths=[dict(name=row['name'],radius=row['artificial_planar_radius_corridor_certified'],
            R7=row['endpoints'][-1]['R7_product_upper']['decimal_display'],
            negative_count=len(row['endpoints'][-1]['radius_surplus_certificate']['nonpositive_witnesses'])) for row in rows])),flush=True)


if __name__=='__main__':main()
