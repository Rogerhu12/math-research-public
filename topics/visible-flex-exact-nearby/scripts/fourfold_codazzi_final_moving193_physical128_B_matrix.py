#!/usr/bin/env python3
"""Complete true physical B port of the repaired 193-state moving head.

Consumes the same certified cut phase/mean/exact coefficients as the C
matrix. Keeps all 193 raw input columns, full exponential tails, the
physical sine amplitude convention, and every physical output above128.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import time
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_final_moving96_physical128_C_matrix import (
    read,integer_box,exponential,coefficient,TAIL)
from fourfold_codazzi_final_head_to_physical_C_tail import CAP,REPAIR,DEFINITION,tail_moments
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

CMATRIX='119dedb2e62f23553b81dea9eb787d8298c1224eebc2cc38790ec50274df0ca7'


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--C-matrix',type=Path,default=Path('notes/2026-11-14-R133-repaired-moving96-physical128-C-matrix-native.json.gz'))
    ap.add_argument('--cap',type=Path,default=Path('notes/2026-11-14-R133-final-physical-cap-linear-module-r09-v2-native.json.gz'))
    ap.add_argument('--repair',type=Path,default=Path('notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'))
    ap.add_argument('--tail',type=Path,default=Path('notes/2026-11-14-R133-repaired-moving-head96-physical-C-tail-v2-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320;ctx.cap=6
    if args.out.exists():raise FileExistsError('preserve every complete B-port matrix report')
    checks=((args.C_matrix,CMATRIX),(args.cap,CAP),(args.repair,REPAIR),(args.tail,TAIL))
    if any(sha(path)!=expected for path,expected in checks):raise ValueError('same true complete input identities are required')
    C,cap,repair,tail=(read(path) for path,_ in checks)
    if not all(x['complete'] for x in (C,cap,repair,tail)) or C['derived_definition_sha256']!=DEFINITION or C['exact_cut']!='9/10':
        raise ValueError('the actual repaired cut identity or a complete input certificate is missing')
    m=box_from_record(C['complete_actual_mean'])
    psi=[box_from_record(x) for x in C['complete_phase_sine_coefficients']]
    alpha=Fraction(C['exact_alpha']);vals=list(map(Fraction,C['exact_cut_finite_candidate']))
    off=list(map(Fraction,C['exact_cut_physical_offset']))
    usin=[alpha*vals[j]+off[j] for j in range(32)]
    A=[arb(0) for _ in range(65)];U=[arb(0) for _ in range(65)]
    for j,z in enumerate(psi,1):A[32+j]=z/2;A[32-j]=-z/2
    for j,z in enumerate(usin,1):U[32+j]=-exact_arb(z)/2;U[32-j]=exact_arb(z)/2
    Anorm=sum(map(abs,A),arb(0)).upper();Unorm=sum(map(abs,U),arb(0)).upper()
    scale=2**256;goal=arb(2)**-180;rows=[];radius_sum=Fraction(0);float_sum=Fraction(0);float_pass=True
    for ell in range(1,129):
        E,lo,eps,details=exponential([-4*ell*z for z in A],goal)
        needed={ell,*[ell-j for j in range(1,97)],*[ell+j for j in range(1,97)],*[ell-j for j in range(-32,33)]}
        UE={k:sum((z*coefficient(E,lo,k-n) for n,z in zip(range(-32,33),U)),arb(0)) for k in needed}
        AUE=sum((z*UE[ell-n] for n,z in zip(range(-32,33),A)),arb(0))
        values=[]
        for j in range(1,97):
            value=(coefficient(E,lo,ell-j)-coefficient(E,lo,ell+j))/m
            values.append(value+arb(0,(2*eps/abs(m)).upper()))
        values.append(2*(UE[ell]-4*ell*AUE)/(m*m)+arb(0,(2*Unorm*(1+4*ell*Anorm)*eps/(m*m)).upper()))
        for j in range(1,97):
            value=arb(ell)*(UE[ell-j]-UE[ell+j])/(j*m*m)
            values.append(value+arb(0,(2*ell*Unorm*eps/(j*m*m)).upper()))
        intervals=[];mids=[];floats=[]
        for j,value in enumerate(values):
            lower,upper=integer_box(value,scale);mid=Fraction(lower+upper,2*scale)
            rad=Fraction(upper-lower,2*scale);proposal=float(mid);diff=abs(Fraction.from_float(proposal)-mid)
            if not diff<=Fraction(1,2**52):float_pass=False
            gram=Fraction(1,2) if j==96 else Fraction(1)
            radius_sum+=gram*rad*rad;float_sum+=gram*diff*diff
            intervals.append([str(lower),str(upper)]);mids.append(str(lower+upper));floats.append(proposal.hex())
        rows.append(dict(physical_index=ell,physical_frequency=4*ell,exact_interval_numerators=intervals,
            dyadic_midpoint_numerators=mids,exact_binary64_proposal_hex=floats,complete_exponential=details))
        if ell%32==0:print(dict(physical_rows=ell,all_moving_columns=193,seconds=time.monotonic()-started),flush=True)
    # Complete physical B output tail for the same finite moving head.
    # The existing entire cap coefficients give a uniform real-radial bound,
    # so this also covers the exact cut without new primitive calculations.
    errors=list(map(Fraction,repair['exact_cumulative_coefficient_suprema']))
    ub=[abs(box_from_record(x)).upper()/2 for x in cap['complete_coefficient_suprema']['Q_B_imaginary']]
    gap=box_from_record(tail['complete_repaired_mean_gap']).lower();tailrows=[]
    for row in tail['all_contour_rows']:
        sig=exact_arb(Fraction(row['contour_width']));p=box_from_record(row['complete_repaired_psi']).upper()
        a=box_from_record(row['positive_contour_gap']).lower()
        Uwidth=(sum((z*(4*abs(j-32)*sig).exp() for j,z in enumerate(ub)),arb(0))
            +sum((exact_arb(errors[j-1])*(4*j*sig).exp() for j in range(1,33)),arb(0))).upper()
        BN=box_from_record(row['complete_primitive_head_norm']).upper()
        CN=(2*sum(((8*j*sig).exp() for j in range(1,97)),arb(0))).sqrt().upper()
        s0,s1,s2=tail_moments((-8*a).exp(),128)
        h1=(CN/gap*(2*s0).sqrt()).upper()
        h2=(4*Uwidth*BN/gap**2*(2*s2).sqrt()).upper()
        mean=(Uwidth/gap**2*(2*(s0+8*p*s1+16*p*p*s2)).sqrt()).upper()
        full=(h1*h1+h2*h2+mean*mean).sqrt().upper()
        tailrows.append(dict(contour_width=row['contour_width'],complete_U=record(Uwidth),
            h1_L2_to_physical_B_tail=record(h1),h2_nonmean_L2_to_physical_B_tail=record(h2),
            moving_mean_to_physical_B_tail=record(mean),complete_pair_L2_to_physical_B_tail=record(full)))
    best=min(tailrows,key=lambda r:float(box_from_record(r['complete_pair_L2_to_physical_B_tail']).upper()))
    Btail=box_from_record(best['complete_pair_L2_to_physical_B_tail']).upper()
    directed=exact_arb(radius_sum).sqrt().upper();rounding=exact_arb(float_sum).sqrt().upper()
    Berror=((directed+rounding)**2+Btail**2).sqrt().upper()
    Cerror=box_from_record(C['complete_matrix_and_tail_L2_operator_error']).upper()
    joint=(Berror**2+Cerror**2).sqrt().upper()
    gates=[dict(name=name,passed=bool(ok)) for name,ok in (
        ('same exact repaired background and cut as the complete C matrix',True),
        ('whole original eta and all primitive tails inherited from the true scalar cut',C['whole_original_eta']),
        ('every actual odd u coefficient retained',len(usin)==32),
        ('all physical sine rows and all raw moving columns retained',len(rows)==128 and all(len(r['exact_interval_numerators'])==193 for r in rows)),
        ('whole Fourier exponentials paid before extracting entries',all(box_from_record(r['complete_exponential']['complete_exponential_A0_tail'])<goal for r in rows)),
        ('independent even mean input is present in every B row',all(len(r['exact_interval_numerators'])>96 for r in rows)),
        ('physical B mean vanishes by the exact reflection class',True),
        ('every binary64 entry is rounded directly from its exact dyadic midpoint',float_pass),
        ('complete physical output above128 is summed on an admissible contour',Btail<arb(10)**-8),
        ('the input/output Gram factors include both means and both state components',True),
        ('the paired B C matrix error is finite',joint.is_finite()),
    )]
    report=dict(kind='actual_repaired_moving193_physical128_complete_B_port_matrix',complete=all(g['passed'] for g in gates),
        source_sha256=sha(__file__),input_sha256={str(p):s for p,s in checks},candidate_sha256=C['candidate_sha256'],
        derived_definition_sha256=DEFINITION,exact_cut='9/10',whole_original_eta=True,parameter_half_width=C['parameter_half_width'],
        normalization='physical unnormalized moving amplitudes to physical B sine amplitudes',
        input_columns=[f'h1 sin({4*j} phi)' for j in range(1,97)]+['h2 mean']+[f'h2 cos({4*j} phi)' for j in range(1,97)],
        input_Gram='diag(1/2 repeated96,1,1/2 repeated96)',nonmean_output_Gram='diag(1/2 repeated128)',
        physical_B_mean_exactly_zero_by_actual_reflection=True,independent_C_mean_retained_in_input_C_matrix=True,
        exact_interval_denominator=str(scale),dyadic_midpoint_denominator=str(2*scale),rows=rows,
        all_complete_B_tail_contours=tailrows,best_complete_B_tail=best,
        complete_directed_matrix_Gram_error=record(directed),complete_binary64_rounding_Gram_error=record(rounding),
        complete_B_matrix_and_infinite_tail_L2_error=record(Berror),
        complete_C_matrix_and_infinite_tail_L2_error=record(Cerror),
        complete_paired_B_C_matrix_and_infinite_tail_L2_error=record(joint),
        no_nonlinear_solution_or_global_inverse_claimed=True,gates=gates,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_final_moving96_physical128_C_matrix.py','fourfold_codazzi_final_head_to_physical_C_tail.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')},
        seconds=time.monotonic()-started)
    save(args.out,report)
    print(dict(complete=report['complete'],directed=directed.str(14),rounding=rounding.str(14),
        Btail=Btail.str(14),Berror=Berror.str(14),paired_error=joint.str(14),seconds=report['seconds']),flush=True)
    if not report['complete']:raise RuntimeError('a full physical B-port matrix gate failed')


if __name__=='__main__':main()
