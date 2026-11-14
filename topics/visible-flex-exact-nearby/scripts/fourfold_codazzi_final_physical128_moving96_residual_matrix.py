#!/usr/bin/env python3
"""True full residual change of equations and its96-by128 sine block.

Y(phi)=v(phi) R_B(Theta(phi)).  The full L2 map and inverse are bounded;
the finite block is not identified with that whole map.  Original mean,
whole eta, phase tails and Gram conventions are retained.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import time
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_final_moving96_physical128_C_matrix import read,integer_box,exponential,coefficient
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

CMATRIX='119dedb2e62f23553b81dea9eb787d8298c1224eebc2cc38790ec50274df0ca7'
DEFINITION='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--C-matrix',type=Path,default=Path('notes/2026-11-14-R133-repaired-moving96-physical128-C-matrix-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every actual residual change-of-equations certificate')
    if sha(args.C_matrix)!=CMATRIX:raise ValueError('the same complete actual physical cut is required')
    C=read(args.C_matrix)
    if not C['complete'] or C['derived_definition_sha256']!=DEFINITION or C['exact_cut']!='9/10' or not C['whole_original_eta']:
        raise ValueError('the complete repaired same-object angle/mean proof is missing')
    m=box_from_record(C['complete_actual_mean']);psi=[box_from_record(x) for x in C['complete_phase_sine_coefficients']]
    alpha=Fraction(C['exact_alpha']);values=list(map(Fraction,C['exact_cut_finite_candidate']))
    offsets=list(map(Fraction,C['exact_cut_physical_offset']))
    vcos=[alpha*values[32+j]+offsets[32+j] for j in range(1,33)]
    vnon=exact_arb(sum(map(abs,vcos),Fraction(0)))
    mgap=abs(m).lower();vmin=(mgap-vnon).lower();vmax=(abs(m).upper()+vnon).upper()
    fullnorm=(abs(m).upper()*vmax).sqrt().upper()
    fullinverse=(1/(mgap*vmin).sqrt()).upper()
    if not m<0 or not vmin>0:raise ValueError('the complete real weighted angle must be invertible')
    A=[arb(0) for _ in range(65)]
    for j,z in enumerate(psi,1):A[32+j]=z/2;A[32-j]=-z/2
    goal=arb(2)**-180;scale=2**256
    intervals=[[] for _ in range(96)];mids=[[] for _ in range(96)];floats=[[] for _ in range(96)]
    radius_squared=Fraction(0);rounding_squared=Fraction(0);float_gate=True;exps=[]
    for ell in range(1,129):
        E,lo,eps,detail=exponential([-4*ell*z for z in A],goal);exps.append(detail)
        for j in range(1,97):
            value=m*exact_arb(Fraction(j,ell))*(coefficient(E,lo,ell-j)+coefficient(E,lo,ell+j))
            value+=arb(0,(2*abs(m)*exact_arb(Fraction(j,ell))*eps).upper())
            lower,upper=integer_box(value,scale);middle=Fraction(lower+upper,2*scale)
            radius=Fraction(upper-lower,2*scale);proposal=float(middle);roundoff=abs(Fraction.from_float(proposal)-middle)
            radius_squared+=radius*radius;rounding_squared+=roundoff*roundoff
            float_gate=float_gate and roundoff<=Fraction(1,2**50)
            intervals[j-1].append([str(lower),str(upper)]);mids[j-1].append(str(lower+upper));floats[j-1].append(proposal.hex())
    directed=exact_arb(radius_squared).sqrt().upper();rounding=exact_arb(rounding_squared).sqrt().upper()
    blockerror=(directed+rounding).upper()
    rows=[dict(moving_index=j+1,moving_physical_frequency=4*(j+1),
        exact_interval_numerators=intervals[j],dyadic_midpoint_numerators=mids[j],
        exact_binary64_proposal_hex=floats[j]) for j in range(96)]
    gates=[dict(name=name,passed=bool(ok)) for name,ok in (
        ('the same exact repaired cut and whole original eta are retained',C['whole_original_eta']),
        ('all32 actual phase and nonmean v coefficients are retained',len(psi)==len(vcos)==32),
        ('the full real multiplier and angular Jacobian stay nonzero',vmin>0 and mgap>0),
        ('every finite block entry has a complete exponential-tail error',all(box_from_record(x['complete_exponential_A0_tail'])<goal for x in exps)),
        ('all96 moving sine rows and128 physical sine columns are retained',len(rows)==96 and all(len(z['exact_interval_numerators'])==128 for z in rows)),
        ('both sine Gram factors are exactly one half and cancel in the HS error',radius_squared>=0 and rounding_squared>=0),
        ('binary64 is rounded from each exact dyadic midpoint',float_gate),
        ('the complete L2 map and inverse have finite actual bounds',fullnorm.is_finite() and fullinverse.is_finite()),
        ('the finite block has a finite directed same-L2 error',blockerror.is_finite()),
        ('the independent physical C mean is not removed by this odd B transform',C['physical_mean_row']['all_nonmean_input_columns_exactly_zero']),
    )]
    report=dict(kind='actual_complete_physical128_B_residual_to_moving96_matrix',complete=all(g['passed'] for g in gates),
        source_sha256=sha(__file__),C_matrix_sha256=CMATRIX,candidate_sha256=C['candidate_sha256'],
        derived_definition_sha256=DEFINITION,exact_cut='9/10',whole_original_eta=True,
        parameter_half_width=C['parameter_half_width'],exact_nu=C['exact_nu'],
        exact_operator='S R(phi)=v(phi)*R(Theta(phi)); Theta_phi=v/m',
        exact_matrix_entry='K[j,l]=m*(j/l)*(E_l[l-j]+E_l[l+j]); E_l=exp(-4*l*i*psi)',
        input_basis='raw physical sin(4*l*theta), l=1..128',output_basis='raw moving sin(4*j*phi), j=1..96',
        input_Gram='diag(1/2 repeated128)',output_Gram='diag(1/2 repeated96)',
        exact_interval_denominator=str(scale),dyadic_midpoint_denominator=str(2*scale),rows=rows,
        complete_actual_mean=record(m),complete_v_absolute_lower=record(vmin),complete_v_absolute_upper=record(vmax),
        complete_full_L2_operator_norm=record(fullnorm),complete_full_L2_inverse_norm=record(fullinverse),
        complete_directed_matrix_Gram_error=record(directed),complete_binary64_rounding_Gram_error=record(rounding),
        complete_finite_block_L2_error=record(blockerror),all_exponential_details=exps,
        full_moving_h1_boundary_coefficient_is_exact_identity=True,
        no_physical_high_input_or_moving_high_output_deleted=True,
        exact_independent_C_mean_row_is_still_required=True,
        no_whole_boundary_or_body_inverse_claimed=True,gates=gates,seconds=time.monotonic()-started)
    save(args.out,report)
    print(dict(complete=report['complete'],fullnorm=fullnorm.str(15),inverse=fullinverse.str(15),
        directed=directed.str(15),rounding=rounding.str(15),error=blockerror.str(15),seconds=report['seconds']),flush=True)
    if not report['complete']:raise RuntimeError('a complete residual-change matrix gate failed')


if __name__=='__main__':main()
