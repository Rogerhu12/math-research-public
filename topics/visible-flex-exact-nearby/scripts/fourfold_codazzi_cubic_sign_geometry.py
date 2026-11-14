#!/usr/bin/env python3
"""Whole-circle geometry of the same certified cubic-residual Cauchy branch.

The full finite BC function is only an error centre.  The independently
proved true C0 error is added on every closed radial/angular box before
testing either sign or reconstructing the second fundamental form.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_sharded_candidate import ShardedExactCandidate
from fourfold_codazzi_linear_degeneracy_v2 import read_json,upper,lower,propagate
from fourfold_codazzi_cleared_polynomial_residual import actual_ball,parameter
from fourfold_phase_codazzi_continuation_validate import angular_cells_taylor,maxabs
from fourfold_phase_beta_bulk_box import DirectedFFT
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_two_jet_newton_source import Box,arb_box,record,save,sha,range_record


def check_bound_files(data):
    for path,h in data.get('inputs',{}).items():
        if sha(path)!=h:raise ValueError('bound input changed: '+path)
    for name,h in data.get('dependencies',{}).items():
        if sha(Path(__file__).with_name(name))!=h:
            raise ValueError('bound dependency changed: '+name)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native',type=Path,default=Path('notes/2026-11-13-Codazzi-cubic-cleared-r02-n1024-v1-native.json.gz'))
    ap.add_argument('--continuation',type=Path,default=Path('notes/2026-11-13-R131-cubic-cleared-r01-v1-C0-native.json.gz'))
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-codazzi-dense-r02-n1024-candidate-shards.json'))
    ap.add_argument('--angles',type=int,default=4096)
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits;ctx.cap=4;tick=time.monotonic()
    if args.out.exists():raise FileExistsError('a fresh complete geometry report is required')
    if args.angles<2048 or args.angles&(args.angles-1):
        raise ValueError('a complete power-of-two closed angular cover is required')
    native=read_json(args.native);certificate=read_json(args.continuation)
    if (native.get('kind')!='actual_complete_Codazzi_cubic_target_cleared_polynomial_residual'
        or not native.get('complete') or native.get('failure') is not None
        or native['covered_interval']!=native['exact_requested_interval']
        or not native['whole_affine_parameter_interval'] or not native['whole_real_angular_circle']
        or native['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cubic_cleared_residual.py'))):
        raise ValueError('the complete same actual cubic native is required')
    if (certificate.get('kind')!='R131_true_C0_prefix_from_complete_cubic_cleared_residual'
        or not certificate.get('complete') or not certificate.get('continuation_certified')
        or not certificate['whole_affine_parameter_interval'] or not certificate['whole_real_angular_circle']
        or not certificate['barrier']['passed']
        or certificate['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cubic_C0_prefix.py'))
        or certificate['inputs'].get(str(args.native))!=sha(args.native)):
        raise ValueError('the same actually proved C0 prefix is required')
    check_bound_files(native);check_bound_files(certificate)
    for key in ('object_sha256','candidate_sha256','exact_center_parameter','parameter_half_width'):
        if native[key]!=certificate[key]:raise ValueError('true continuation identity changed: '+key)
    if sha(args.candidate)!=native['candidate_manifest_sha256']:
        raise ValueError('the complete finite candidate manifest differs')
    original_left,original_right=map(Fraction,native['exact_requested_interval'])
    left,right=map(Fraction,certificate['exact_requested_interval'])
    if left!=original_left or left!=0 or not 0<right<=original_right:
        raise ValueError('geometry must use the proved same-waist prefix')
    selected=[]
    for item in native['rows']:
        lo,hi=map(Fraction,item['interval'])
        if lo>=right:break
        row=dict(item);row['native_interval']=item['interval']
        row['interval']=[str(lo),str(min(hi,right))];selected.append(row)
    initial=certificate['initial_actual_weighted_derivative']
    if not initial['whole_parameter_interval'] or not initial['whole_real_angular_circle']:
        raise ValueError('the independent whole-waist gradient is missing')
    barrier=propagate(dict(initial_error=native['actual_initial_error'],rows=selected,
        exact_requested_interval=['0',str(right)]),upper(initial['weighted_gradient_upper']),
        exact_arb(Fraction(certificate['tube'])))
    if not barrier['passed'] or barrier!=certificate['barrier']:
        raise ValueError('the independent complete actual C0 replay differs')
    target=SimpleNamespace(product_grid=2048,polynomial_fft=DirectedFFT())
    candidate=ShardedExactCandidate(args.candidate,target)
    if (candidate.original_payload_sha256!=native['candidate_sha256']
        or candidate.metadata['object_sha256']!=native['object_sha256']
        or parameter(candidate.metadata['exact_center_parameter'])!=parameter(native['exact_center_parameter'])):
        raise ValueError('the entire recovered finite object differs')
    turnX=turnY=turnN=horizontal=displacement=curvature=arb(0)
    amin=emin=None;cursor=Fraction(0);minimum_sign=None;rows=[]
    all_signs=True
    for index,(item,error) in enumerate(zip(selected,barrier['rows'])):
        lo,hi=map(Fraction,item['interval']);gl,gr=map(Fraction,item['actual_scalar_germ'])
        if lo!=cursor or not gl<=lo<hi<=gr or item['interval']!=error['interval']:
            raise ValueError('the full true radial/germ/error cover differs')
        coefficients={k:actual_ball(v) for k,v in item['true_target_coefficients'].items()}
        if not coefficients['K']<0 or not all(coefficients[k]>0 for k in ('k','a','E')):
            raise ValueError('the true target chart is not strictly valid')
        polynomials=candidate.polynomials(item['piece'],lo,hi)
        B,C=(angular_cells_taylor(polynomials[k],args.angles) for k in ('B','C'))
        if not np.all(C.hi<0):raise ValueError('the full candidate negative denominator is missing')
        k=arb_box(coefficients['k']);P,Q=(B+k)/C,(B-k)/C
        e0=upper(error['C0_final']);fee=arb_box(e0)
        p=P+Box(-fee.hi,fee.hi);q=Q+Box(-fee.hi,fee.hi)
        sign=arb(float(min(np.min(-p.hi),np.min(q.lo)))).lower()
        gap=lower(error['actual_gap_lower']);M=upper(error['actual_M'])
        ku=coefficients['k'].upper();e=coefficients['E'].sqrt().upper()
        if not gap>0:raise ValueError('the true p,q gap is unresolved')
        opposite=bool(sign>0);all_signs=all_signs and opposite
        # Both formulas are rigorous. The sign-sensitive one is used only
        # after every angular cell on this exact radial box has passed.
        if opposite:A=(ku*M).upper();Bm=ku
        else:A=(2*ku*M*M/gap).upper();Bm=(2*ku*M/gap).upper()
        Cm=(2*ku/gap).upper();h=exact_arb(hi-lo)
        horizontal=(horizontal+min(h*e,h*e*turnX+h*h*e*e*A/2)).upper()
        displacement=(displacement+h*e).upper()
        turnX=(turnX+h*e*A).upper();turnY=(turnY+h*e*Bm).upper()
        turnN=(turnN+h*e*(A*A+Bm*Bm).sqrt()).upper()
        curvature=max(curvature,max(A,Cm)+Bm).upper()
        al=coefficients['a'].lower();el=coefficients['E'].sqrt().lower()
        amin=al if amin is None else min(amin,al).lower()
        emin=el if emin is None else min(emin,el).lower()
        minimum_sign=sign if minimum_sign is None else min(minimum_sign,sign).lower()
        rows.append(dict(native_row=index,piece=item['piece'],interval=item['interval'],
            original_native_interval=item['native_interval'],actual_scalar_germ=item['actual_scalar_germ'],
            complete_candidate_B_range=range_record(B),complete_candidate_C_range=range_record(C),
            true_p_range=range_record(p),true_q_range=range_record(q),
            actual_error=record(e0),actual_sign_lower=record(sign),opposite_signs_proved=opposite,
            actual_gap_lower=record(gap),actual_absolute_Riemann_upper=record(M),
            A_absolute_upper=record(A),B_absolute_upper=record(Bm),C_absolute_upper=record(Cm),
            integrated_X_turn=record(turnX),integrated_Y_turn=record(turnY),
            integrated_horizontal_displacement=record(horizontal)))
        cursor=hi
        if index%20==0:print(dict(row=index,right=str(hi),sign=sign.str(10),opposite=opposite),flush=True)
    if cursor!=right or len(rows)!=len(barrier['rows']):raise ValueError('incomplete true geometry interval')
    support=arb(1)/2;radius=arb(13)/10
    horizontal_normal=(turnY+turnX*turnX/2).upper()
    rlo=(support-horizontal).lower();rhi=(radius+horizontal).upper()
    angular=(support-horizontal-radius*turnY).lower()
    normal=(support-horizontal-radius*horizontal_normal).lower()
    phi=(amin*angular/(rhi*rhi)).lower();jac=(emin*amin*normal/(rhi*rhi)).lower()
    vertical=(1-turnX*turnX/2).lower()
    values=dict(minimum_actual_opposite_sign=minimum_sign,
        actual_principal_curvature_upper=curvature,displacement_upper=displacement,
        X_turn_upper=turnX,Y_turn_upper=turnY,normal_turn_upper=turnN,
        horizontal_displacement_upper=horizontal,horizontal_normal_change_upper=horizontal_normal,
        horizontal_radius_lower=rlo,horizontal_radius_upper=rhi,
        angular_numerator_lower=angular,horizontal_normal_support_lower=normal,
        argument_theta_lower=phi,cylindrical_Jacobian_lower=jac,vertical_tangent_lower=vertical)
    gates=dict(nonzero_horizontal_radius=bool(rlo>0),positive_argument_derivative=bool(phi>0),
        positive_cylindrical_Jacobian=bool(jac>0),positive_vertical_tangent=bool(vertical>0))
    dependencies=('fourfold_codazzi_sharded_candidate.py','fourfold_codazzi_linear_degeneracy_v2.py',
        'fourfold_codazzi_cleared_polynomial_residual.py','fourfold_phase_codazzi_continuation_validate.py',
        'fourfold_phase_beta_bulk_box.py','fourfold_phase_beta_bulk_interval.py',
        'fourfold_phase_two_jet_newton_source.py','fourfold_phase_newton_source_centered.py')
    out=dict(kind='actual_same_Codazzi_cubic_prefix_sign_and_complete_geometry',
        complete=True,continuation_certified=True,embedding_certified=all(gates.values()),
        closed_surface_complete=False,source_sha256=sha(__file__),bits=args.bits,
        inputs={str(p):sha(p) for p in (args.native,args.continuation,args.candidate)},
        verified_native_inputs=native['inputs'],verified_native_dependencies=native['dependencies'],
        full_C0_barrier_independently_replayed=True,object_sha256=native['object_sha256'],
        candidate_sha256=native['candidate_sha256'],exact_center_parameter=native['exact_center_parameter'],
        parameter_half_width=native['parameter_half_width'],whole_affine_parameter_interval=True,
        whole_real_angular_circle=True,exact_positive_interval=['0',str(right)],
        reflected_interval=[str(-right),str(right)],closed_angle_cells=args.angles,
        finite_candidate_degree=candidate.degree,all_radial_rows_retained=True,
        all_actual_opposite_signs_proved=all_signs,rows=rows,geometry_gates=gates,
        bounds={k:record(v) for k,v in values.items()},
        dependencies={name:sha(Path(__file__).with_name(name)) for name in dependencies},
        geometry_theorems={str(p):sha(p) for p in (
            Path('results/R123-separated-correction-budgets-and-normal-Hessian.md'),
            Path('results/R126-exact-Codazzi-reconstruction-and-continuation.md'),
            Path('results/R128-quantitative-embedding-of-the-exact-waist-annulus.md'))},
        wall_seconds=time.monotonic()-tick,
        scope='The same true Cauchy branch and original metric on the stated reflected annulus. Every candidate field is enlarged by its proved true error before using its sign. Geometry uses the actual orthonormal frame, the entire angular circle, the true parameter box and the original complete waist. No complete closed surface, same-metric flex, held displacement or reach is asserted.')
    save(args.out,out)
    print(dict(complete=True,embedding_certified=out['embedding_certified'],
        all_opposite_signs=all_signs,rows=len(rows),bounds={k:v.str(13) for k,v in values.items()},
        wall_seconds=out['wall_seconds']),flush=True)


if __name__=='__main__':main()
