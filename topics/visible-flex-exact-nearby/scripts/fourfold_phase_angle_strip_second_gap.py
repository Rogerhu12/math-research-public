#!/usr/bin/env python3
"""Improve only the finite-phase harmonic P gate in a completed R59 scan.

The exact finite P and P_theta boundary grids receive a continuous second
derivative gap.  Every old passed row is retained, and each failed row is
recomputed on the identical parameter/radial cell; real infinite-primitive
inputs and all other moving-frame bounds remain the already paid values.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import time

import numpy as np
from fourfold_phase_beta_affine import sha
from fourfold_phase_full_angle_time_domain import document
from fourfold_phase_core_N_interval import CoreNGate,ClosedSpanSplineBox
from fourfold_phase_root_interval import Box,interval_dot,angular_grid
from fourfold_phase_uniform_tail import derivative_coefficients,weighted_sum_up,mul_up,power_up,down
from fourfold_phase_modulus_characteristic_strip import hyperbolic_weights,quotient_bounds,write_report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,required=True);p.add_argument('--old-scan',type=Path,required=True)
    p.add_argument('--real-certificate',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_parameter_N_interval.json'))
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();started=time.monotonic();obj=document(args.object);old=document(args.old_scan);real=document(args.real_certificate)
    ip,dp=Path(obj['origin_inputs']['path']),Path(obj['direction']['path'])
    if (old['status']!='complete' or not old['complete_radial_coverage']
        or old['target_center_object_sha256']!=sha(args.object)
        or old['origin_inputs_sha256']!=sha(ip) or old['frozen_direction_sha256']!=sha(dp)
        or old['real_certificate_sha256']!=sha(args.real_certificate)
        or not real.get('uniform_parameter_N_negative_proved')):
        raise ValueError('matching complete narrow-box scan and original real certificate required')
    if (sha(ip)!=obj['origin_inputs']['sha256'] or sha(dp)!=obj['direction']['sha256']
        or not old.get('rational_parameter_containment_checked')):
        raise ValueError('exact affine definition/parameter inclusion changed')
    old_rows=old['cells'];real_rows=sorted(real['rows'],key=lambda row:row['interval'][0])
    if (len(old_rows)!=len(real_rows)or any(r['cell_index']!=i or r['radial_interval']!=real_rows[i]['interval']
        for i,r in enumerate(old_rows))):raise ValueError('old scan does not give the exact complete original partition')
    with np.load(ip,allow_pickle=False)as z:frozen={k:z[k].copy()for k in z.files}
    with np.load(dp,allow_pickle=False)as z:direction={k:z[k].copy()for k in z.files}
    gate=CoreNGate(frozen,real['quarter_nodes'],real['angular_nodes'])
    delta=Box(*old['exact_parameter_interval']);raw=Box(frozen['phase_coefficients'])+delta*direction['phase_direction_coefficients']
    phase=ClosedSpanSplineBox.__new__(ClosedSpanSplineBox);phase.states=[]
    knots,degree,lo,hi=frozen['phase_knots'],5,raw.lo,raw.hi
    for order in range(6):
        phase.states.append((knots,degree,lo,hi))
        if order<5:knots,degree,lo,hi=derivative_coefficients(knots,degree,lo,hi)
    gate.target.phase=phase
    gate.target.alpha=[Box(a)+delta*v for a,v in zip(frozen['alpha'],direction['alpha_direction'])]
    nodes=real['angular_nodes'];sine,_=angular_grid(nodes);modes=np.arange(1,gate.target.modes+1)
    at=(np.arange(nodes)[:,None]*modes[None,:])%nodes
    sine_matrix=Box(sine.lo[at],sine.hi[at]);frequency=4*modes
    cosh_box,_=hyperbolic_weights(old['angular_strip_width'],gate.target.modes)
    gap=Box(float(gate.half_gap));rows=[]
    common={key:value for key,value in old.items()if key not in
        ['source_sha256','dependency_sha256','status','cells','cell_count','all_passed',
         'proved_uniform_denominator_nonzero','minimum_Nraw_modulus_lower','elapsed_seconds']}
    common.update(kind='R59_narrow_box_with_exact_finite_phase_second_order_angular_gap',
        source_sha256=sha(__file__),input_scan_sha256=sha(args.old_scan),input_scan_path=str(args.old_scan),
        dependency_sha256={name:sha(Path(__file__).with_name(name))for name in
            ['fourfold_phase_narrow_parameter_angle_strip.py','fourfold_phase_modulus_characteristic_strip.py',
             'fourfold_phase_core_N_interval.py','fourfold_phase_root_interval.py','fourfold_phase_uniform_tail.py']})
    def save():
        finished=len(rows)==len(old_rows);passed=finished and all(r['passed']for r in rows)
        doc=dict(**common,status='complete'if finished else'running',cells=rows,cell_count=len(rows),
            all_passed=all(r['passed']for r in rows),proved_uniform_denominator_nonzero=passed,
            minimum_Nraw_modulus_lower=min((r['Nraw_modulus_lower']for r in rows),default=0.),
            elapsed_seconds=time.monotonic()-started)
        write_report(args.out,doc);return doc
    save();changed=0
    for i,old_row in enumerate(old_rows):
        row=dict(old_row)
        if row['passed']:
            row['inherited_passed_input_cell']=True
        else:
            beta,_,_,_=gate.target.scalars(Box(*row['radial_interval']))
            P=Box(1)+interval_dot(gate.cosine,(beta[0]*frequency*cosh_box).reshape(-1,1))
            derivative=interval_dot(sine_matrix,(-beta[0]*(frequency**2)*cosh_box).reshape(-1,1))
            P2=float(weighted_sum_up(beta[0].abs_upper(),mul_up(power_up(frequency,3),cosh_box.hi)))
            linear=P-gap*Box(derivative.abs_upper())
            second=(Box(.5)*gap*gap*Box(P2))
            improved=float((linear-second).lo.min())
            Plower=max(row['P_real_part_lower'],improved)
            clo,zlo,Qlo,alo=[row[name]for name in
                ['cos_gamma_real_part_lower','Fx_z_real_part_lower','normal_component_modulus_lower','radius_lower']]
            positive=bool(Plower>0 and clo>0 and zlo>0 and Qlo>0 and alo>0)
            Dlo=float((Box(Plower)*clo*Qlo-Box(row['u_derivative_bounds'][0])*row['frame_projection_upper']).lo)if positive else 0.
            modulus=float((Box(alo)*alo*Dlo).lo)if positive and Dlo>0 else 0.
            oldmod=float(down(-row['old_second_order_Nraw_real_part_upper']))if row['old_second_order_Nraw_real_part_upper']<0 else 0.
            den=max(modulus,oldmod)
            row.update(P_real_part_lower=Plower,positive_multiplier_conditions=positive,
                moving_factor_modulus_lower=Dlo,moving_frame_Nraw_modulus_lower=modulus,
                Nraw_modulus_lower=den,passed=bool(den>0),
                finite_P_second_order_gap=dict(old_first_order_lower=old_row['P_real_part_lower'],
                    second_order_lower=improved,minimum_boundary_node_lower=float(P.lo.min()),
                    minimum_node_linear_gap_lower=float(linear.lo.min()),
                    P_second_derivative_upper=P2,quadratic_gap_upper=float(second.hi),
                    angular_nodes=nodes,half_gap_upper=float(gate.half_gap)))
            if den>0:
                n1,n2=row['Nraw_derivative_bounds'][1:]
                row['drift_derivative_bounds']=quotient_bounds(*row['Mraw_derivative_bounds'],n1,n2,den)
                row['wave_factor_derivative_bounds']=quotient_bounds(*row['G_derivative_bounds'],n1,n2,den)
            changed+=1
        rows.append(row)
        if len(rows)%25==0:
            save();print(json.dumps(dict(covered=len(rows),recomputed=changed,failed=sum(not r['passed']for r in rows))),flush=True)
    result=save();print(json.dumps(dict(complete=True,proved=result['proved_uniform_denominator_nonzero'],
        failed=sum(not r['passed']for r in rows),recomputed=changed,sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()
