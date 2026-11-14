#!/usr/bin/env python3
"""R59 moving-frame strip on a smaller exact affine-control box.

The already paid real infinite-primitive bounds remain those of R57's larger
box.  Only the explicit phase/mean box is narrowed, with exact rational
containment checked before outward binary64 interval arithmetic.  This does
not narrow or replace the true graph by rounded control coefficients.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import time

import numpy as np

from fourfold_phase_beta_affine import sha
from fourfold_phase_full_angle_time_domain import document
from fourfold_phase_core_N_interval import CoreNGate,ClosedSpanSplineBox
from fourfold_phase_root_interval import Box
from fourfold_phase_uniform_tail import derivative_coefficients
from fourfold_phase_modulus_characteristic_strip import hyperbolic_weights,strip_cell,write_report


def outward(value,upper):
    x=float(value);actual=Fraction.from_float(x)
    if upper and actual<value:x=math.nextafter(x,math.inf)
    if not upper and actual>value:x=math.nextafter(x,-math.inf)
    if upper and not Fraction.from_float(x)>=value:raise ValueError('upper rational conversion failed')
    if not upper and not Fraction.from_float(x)<=value:raise ValueError('lower rational conversion failed')
    return x


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,required=True)
    p.add_argument('--real-certificate',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_parameter_N_interval.json'))
    p.add_argument('--halfwidth',default='1/2000000');p.add_argument('--width',default='1/48')
    p.add_argument('--indices');p.add_argument('--out',type=Path,required=True);p.add_argument('--resume',action='store_true')
    args=p.parse_args();started=time.monotonic();obj=document(args.object)
    ip=Path(obj['origin_inputs']['path'])
    if sha(ip)!=obj['origin_inputs']['sha256']:raise ValueError('origin input hash differs')
    # Direction is binary NPZ; its exact bytes are the definition.
    dp=Path(obj['direction']['path'])
    if sha(dp)!=obj['direction']['sha256']:raise ValueError('direction input hash differs')
    real=document(args.real_certificate)
    if (not real.get('uniform_parameter_N_negative_proved') or real['status']!='complete'
        or real.get('failures') or real.get('pending')
        or real['origin_inputs_sha256']!=sha(ip) or real['frozen_direction_sha256']!=sha(dp)):
        raise ValueError('completed real R57 box certificate required')
    center=Fraction(int(obj['delta_fraction']['numerator']),int(obj['delta_fraction']['denominator']))
    half=Fraction(args.halfwidth);width=Fraction(args.width)
    if half<0 or not 0<width<Fraction(1,10):raise ValueError('invalid parameter or physical strip width')
    exact_lo,exact_hi=center-half,center+half
    low,high=outward(exact_lo,False),outward(exact_hi,True);physical_width=outward(width,True)
    old_lo,old_hi=map(Fraction.from_float,real['exact_parameter_interval'])
    if not old_lo<=Fraction.from_float(low)<=exact_lo<=exact_hi<=Fraction.from_float(high)<=old_hi:
        raise ValueError('the new independent parameter box leaves the paid real box')
    with np.load(ip,allow_pickle=False)as z:frozen={k:z[k].copy()for k in z.files}
    with np.load(dp,allow_pickle=False)as z:direction={k:z[k].copy()for k in z.files}
    if json.loads(str(direction['metadata']))['origin_inputs_sha256']!=sha(ip):raise ValueError('direction origin differs')
    gate=CoreNGate(frozen,real['quarter_nodes'],real['angular_nodes']);delta=Box(low,high)
    raw=Box(frozen['phase_coefficients'])+delta*direction['phase_direction_coefficients']
    phase=ClosedSpanSplineBox.__new__(ClosedSpanSplineBox);phase.states=[]
    knots,degree,lo,hi=frozen['phase_knots'],5,raw.lo,raw.hi
    for order in range(6):
        phase.states.append((knots,degree,lo,hi))
        if order<5:knots,degree,lo,hi=derivative_coefficients(knots,degree,lo,hi)
    gate.target.phase=phase
    gate.target.alpha=[Box(a)+delta*v for a,v in zip(frozen['alpha'],direction['alpha_direction'])]
    cells=sorted(real['rows'],key=lambda r:r['interval'][0])
    if (cells[0]['interval'][0]!=0 or cells[-1]['interval'][1]!=real['core'][1]
        or any(a['interval'][1]!=b['interval'][0]for a,b in zip(cells,cells[1:]))):
        raise ValueError('the original exact closed-cell cover has a gap')
    requested=list(range(len(cells)))if args.indices is None else list(map(int,args.indices.split(',')))
    if requested!=sorted(set(requested)) or any(i<0 or i>=len(cells)for i in requested):raise ValueError('invalid exact cell list')
    common=dict(kind='R59_moving_frame_on_smaller_exact_affine_independent_box',
        source_sha256=sha(__file__),target_center_object_sha256=sha(args.object),
        origin_inputs_sha256=sha(ip),frozen_direction_sha256=sha(dp),real_certificate_sha256=sha(args.real_certificate),
        exact_parameter_center=str(center),exact_requested_parameter_interval=list(map(str,(exact_lo,exact_hi))),
        exact_parameter_interval=[low,high],containing_real_parameter_interval=real['exact_parameter_interval'],
        rational_parameter_containment_checked=True,requested_physical_theta_strip=str(width),
        angular_strip_width=physical_width,exact_outward_physical_width=str(Fraction.from_float(physical_width)),
        radial_core=real['core'],requested_indices=requested,total_real_cells=len(cells),
        dependency_sha256={name:sha(Path(__file__).with_name(name))for name in
            ['fourfold_phase_modulus_characteristic_strip.py','fourfold_phase_core_N_interval.py',
             'fourfold_phase_root_interval.py','fourfold_phase_uniform_tail.py']},
        limitations=['Real X and N bounds are inherited from the containing R57 independent box',
            'Only explicit phase/mean interval inputs are narrowed, before exact symmetry/infinite R33',
            'Only theta is complex; no complex time or true flow conclusion',
            'A failed row remains a failed gate and cannot be omitted'])
    rows=[]
    if args.resume and args.out.exists():
        old=document(args.out)
        if any(old.get(k)!=v for k,v in common.items()):raise ValueError('resume identity changed')
        rows=old['cells']
        if [r['cell_index']for r in rows]!=requested[:len(rows)]:raise ValueError('non-prefix saved rows')
    weights=hyperbolic_weights(physical_width,gate.target.modes)
    def save():
        complete=len(rows)==len(requested);covered=complete and requested==list(range(len(cells)))
        doc=dict(**common,status='complete'if complete else'running',cells=rows,cell_count=len(rows),
            complete_radial_coverage=covered,all_passed=all(r['passed']for r in rows),
            proved_uniform_denominator_nonzero=bool(covered and all(r['passed']for r in rows)),
            elapsed_seconds=time.monotonic()-started)
        if rows:doc['minimum_Nraw_modulus_lower']=min(r['Nraw_modulus_lower']for r in rows)
        write_report(args.out,doc);return doc
    save()
    for i in requested[len(rows):]:
        beta,gamma,radius,_=gate.target.scalars(Box(*cells[i]['interval']))
        row=strip_cell(beta,gamma,radius,cells[i],physical_width,weights,gate);row['cell_index']=i;rows.append(row)
        if len(rows)%25==0:
            save();print(json.dumps(dict(covered=len(rows),failed=sum(not r['passed']for r in rows))),flush=True)
    result=save();print(json.dumps(dict(complete=True,covered=result['complete_radial_coverage'],
        proved=result['proved_uniform_denominator_nonzero'],failed=sum(not r['passed']for r in rows),sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()
