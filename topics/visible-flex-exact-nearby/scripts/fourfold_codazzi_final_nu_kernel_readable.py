#!/usr/bin/env python3
"""Readable directed bounds from the complete, actually executed ac1 nu kernel."""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx
from fourfold_codazzi_curvature_angle_energy_prefix import read
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record, save, sha

KIND = 'actual_final_complete_nu_5M_kernel_readable_bounds'
NATIVE = '281fa7c17d16b8f6823883df7ff61fc12f9c846c6b98bdd6951eed928d480848'
SOURCE = '09807e405455b58c043a5ff26b7ff5e4e1569a96c81ecd860125552bfba95a3b'
CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--native',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();ctx.prec=320
    if sha(a.native)!=NATIVE:raise ValueError('different actual complete native bytes')
    d=read(a.native)
    if (d.get('kind')!='actual_final_moving_full_nu_adjoint_5M_kernel_and_all_jumps'
        or not d.get('complete') or d.get('failure') is not None
        or d.get('source_sha256')!=SOURCE or d.get('actual_candidate_sha256')!=CANDIDATE
        or not d.get('whole_affine_parameter_interval')
        or not d.get('complete_original_primitive_tail')
        or d.get('complete_finite_kernel_support_index')!=160
        or d.get('actual_scalar_Schur_nonzero_proved') is not False):
        raise ValueError('the complete same-centre source contract changed')
    if len(d['rows'])!=1156 or len(d['jumps'])!=864:raise ValueError('incomplete rows or jumps')
    left=Fraction(1,20)
    for i,row in enumerate(d['rows']):
        x,y=map(Fraction,row['interval'])
        if row['common_row']!=i or x!=left or not x<y:raise ValueError('cover gap or changed row')
        left=y
    if left!=Fraction(9,50):raise ValueError('the full control support was not covered')
    ceilings={
        'unnormalized_full_parameter_source_L1L2_upper':'1.964956',
        'complete_G_weighted_L1L2_upper':'625.523019',
        'all_A_jumps_weighted_l1_L2_upper':'8.072489e-19',
        'true_continuous_adjoint_scalar_absolute_coefficient':'625.523019',
    }
    gates=[]
    for key,bound in ceilings.items():
        value=box_from_record(d['bounds'][key])
        passed=bool(value<arb(bound))
        gates.append(dict(name=key,actual=record(value),strict_upper=bound,passed=passed))
        if not passed:raise ValueError('directed final bound failed: '+key)
    out=dict(kind=KIND,source_sha256=sha(__file__),complete=True,
        inputs={str(a.native):NATIVE},candidate_sha256=CANDIDATE,
        complete_closed_radial_rows=1156,all_actual_A_jumps=864,
        whole_original_eta=True,complete_original_primitive_tail=True,
        exact_support=['1/20','9/50'],full_kernel_support_index=160,
        gate_count=len(gates),gates=gates,
        actual_adjoint_not_supplied=True,actual_nu_Schur_nonzero_proved=False,
        complete_BVP_inverse_proved=False)
    save(a.out,out)
    print(dict(complete=True,gates=len(gates),out=str(a.out)),flush=True)

if __name__=='__main__':main()
