#!/usr/bin/env python3
"""Apply the R56 complex-angle gate to the exact R57 independent control box."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_phase_characteristic_strip import strip_cell, hyperbolic_weights, total
from fourfold_phase_core_N_interval import CoreNGate, ClosedSpanSplineBox
from fourfold_phase_root_interval import Box
from fourfold_phase_uniform_tail import derivative_coefficients


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--direction',type=Path,required=True)
    ap.add_argument('--real-certificate',type=Path,required=True)
    ap.add_argument('--width',type=float,default=1/256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if not 0 < args.width <= .02:
        raise ValueError('invalid strip width')
    real=json.loads(args.real_certificate.read_text())
    if (real['kind']!='directed_uniform_real_parameter_N_tube_for_explicit_symmetric_R33_family'
        or real['status']!='complete' or not real['uniform_parameter_N_negative_proved']
        or real['failures'] or real['pending']):
        raise ValueError('need the completed R57 real independent-box certificate')
    sha=hashlib.sha256(args.inputs.read_bytes()).hexdigest()
    direction_sha=hashlib.sha256(args.direction.read_bytes()).hexdigest()
    if sha!=real['origin_inputs_sha256'] or direction_sha!=real['frozen_direction_sha256']:
        raise ValueError('different exact object or control box')
    with np.load(args.inputs,allow_pickle=False) as z:
        frozen={k:z[k].copy() for k in z.files}
    with np.load(args.direction,allow_pickle=False) as z:
        direction={k:z[k].copy() for k in z.files}
    if json.loads(str(direction['metadata']))['origin_inputs_sha256']!=sha:
        raise ValueError('direction origin mismatch')
    gate=CoreNGate(frozen,real['quarter_nodes'],real['angular_nodes'])
    delta=Box(*real['exact_parameter_interval'])
    raw=Box(frozen['phase_coefficients'])+delta*direction['phase_direction_coefficients']
    phase=ClosedSpanSplineBox.__new__(ClosedSpanSplineBox)
    phase.states=[]
    t,k,lo,hi=frozen['phase_knots'],5,raw.lo,raw.hi
    for order in range(6):
        phase.states.append((t,k,lo,hi))
        if order<5:
            t,k,lo,hi=derivative_coefficients(t,k,lo,hi)
    gate.target.phase=phase
    gate.target.alpha=[Box(a)+delta*d for a,d in
                       zip(frozen['alpha'],direction['alpha_direction'])]
    old=sorted(real['rows'],key=lambda r:r['interval'][0])
    if (old[0]['interval'][0]!=0 or old[-1]['interval'][1]!=real['core'][1]
        or any(a['interval'][1]!=b['interval'][0] for a,b in zip(old,old[1:]))):
        raise ValueError('radial coverage gap')
    weights=hyperbolic_weights(args.width,gate.target.modes)
    rows=[]
    for i,r in enumerate(old):
        beta,gamma,radius,slope=gate.target.scalars(Box(*r['interval']))
        row=strip_cell(beta,gamma,radius,
                       total(r['Fx_horizontal_upper'],r['Fx_z_abs_upper']),
                       -r['raw_minus_n_lower'],args.width,weights)
        row['radial_interval']=r['interval']
        rows.append(row)
        if (i+1)%100==0:
            print(json.dumps(dict(covered=i+1,total=len(old),
                                  failed=sum(not v['passed'] for v in rows))),flush=True)
    report=dict(kind='continuous_complex_angle_Nraw_gate_on_R57_independent_control_box',
        origin_inputs_sha256=sha,frozen_direction_sha256=direction_sha,
        real_certificate_sha256=hashlib.sha256(args.real_certificate.read_bytes()).hexdigest(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        dependency_sha256={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ['fourfold_phase_characteristic_strip.py','fourfold_phase_core_N_interval.py',
                         'fourfold_phase_root_interval.py','fourfold_phase_uniform_tail.py',
                         'fourfold_interval_scalar.py']},
        exact_parameter_interval=real['exact_parameter_interval'],radial_core=real['core'],
        angular_strip_width=args.width,cell_count=len(rows),cells=rows,
        all_passed=all(v['passed'] for v in rows),
        maximum_Nraw_real_part_upper=max(v['Nraw_real_part_upper'] for v in rows),
        limitations=['Real independent control box with the exact R57 endpoints; theta alone is complex',
                     'Rounded candidate membership must be proved separately by exact dyadic comparisons',
                     'No radial complex tube, moving-root certificate, validated return integration or conjugacy error is asserted'])
    if report['all_passed']:
        for key in ['drift_norm_upper','wave_factor_norm_upper',
                    'drift_theta_norm_upper','wave_factor_theta_norm_upper']:
            report['maximum_'+key]=max(v[key] for v in rows)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='cells'},indent=2),flush=True)
    if not report['all_passed']:
        raise SystemExit('preserved complex-strip failure')


if __name__=='__main__':
    main()
