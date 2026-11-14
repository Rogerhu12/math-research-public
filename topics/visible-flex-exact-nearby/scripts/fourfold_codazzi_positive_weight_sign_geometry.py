#!/usr/bin/env python3
"""Complete same-branch geometry from checked positive-weight C0 certificates.

All original saved complete rows and their true unweighted C0 barrier are replayed
without resetting the actual error. The true Riemann field, including its
proved error, is reconstructed on every closed angular/radial cell before
bounding the second form and integrating the original physical frame.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_sharded_candidate import ShardedExactCandidate
from fourfold_codazzi_linear_degeneracy_v2 import read_json,upper,lower
from fourfold_codazzi_positive_weight_batched_piece_C0_v3 import checked_parts as checked_v3,actual_initial
from fourfold_codazzi_positive_weight_saved_row_C0_v4 import checked_parts as checked_v4
from fourfold_codazzi_positive_weight_cubic_C0 import propagate
from fourfold_codazzi_cleared_polynomial_residual import actual_ball,parameter
from fourfold_codazzi_cubic_sign_geometry import check_bound_files
from fourfold_phase_codazzi_continuation_validate import angular_cells_taylor,maxabs
from fourfold_phase_beta_bulk_box import DirectedFFT
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_two_jet_newton_source import Box,arb_box,record,save,sha,range_record


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native',type=Path,default=Path('notes/2026-11-13-Codazzi-cubic-cleared-r02-n1024-v1-native.json.gz'))
    ap.add_argument('--continuation',type=Path,required=True)
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-codazzi-dense-r02-n1024-candidate-shards.json'))
    ap.add_argument('--initial',type=Path,default=Path('notes/2026-11-13-R131-C0-only-r005-native.json.gz'))
    ap.add_argument('--angles',type=int,default=4096)
    ap.add_argument('--bits',type=int,default=256)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits;ctx.cap=4;tick=time.monotonic()
    if args.out.exists():raise FileExistsError('a fresh complete weighted geometry report is required')
    if args.angles<2048 or args.angles&(args.angles-1):
        raise ValueError('a complete power-of-two closed angular cover is required')
    native=read_json(args.native);certificate=read_json(args.continuation)
    if (native.get('kind')!='actual_complete_Codazzi_cubic_target_cleared_polynomial_residual'
        or not native.get('complete') or native.get('failure') is not None
        or native['covered_interval']!=native['exact_requested_interval']
        or not native['whole_affine_parameter_interval'] or not native['whole_real_angular_circle']
        or native['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cubic_cleared_residual.py'))):
        raise ValueError('the complete original actual target native is required')
    consumers={
        'R131_true_C0_continuation_from_checked_complete_cubic_weight_pieces_v3':
            ('fourfold_codazzi_positive_weight_batched_piece_C0_v3.py',checked_v3),
        'R131_true_C0_continuation_from_complete_union_of_saved_weight_rows_v4':
            ('fourfold_codazzi_positive_weight_saved_row_C0_v4.py',checked_v4),
    }
    consumer=consumers.get(certificate.get('kind'))
    if consumer is None:raise ValueError('unrecognized actually proved positive-weight consumer')
    consumer_name,part_checker=consumer
    if (not certificate.get('original_native_reports_unchanged')
        or not certificate.get('complete') or not certificate.get('continuation_certified')
        or not certificate['whole_affine_parameter_interval'] or not certificate['whole_real_angular_circle']
        or not certificate['final_bootstrap_is_unweighted'] or certificate['uses_candidate_C1_error_barrier']
        or certificate['source_sha256']!=sha(Path(__file__).with_name(consumer_name))
        or certificate['bits']!=args.bits
        or certificate['inputs'].get(str(args.initial))!=sha(args.initial)):
        raise ValueError('the same actually proved complete positive-weight continuation is required')
    check_bound_files(native);check_bound_files(certificate)
    for key in ('object_sha256','exact_center_parameter','parameter_half_width'):
        if native[key]!=certificate[key]:raise ValueError('true continuation identity changed: '+key)
    if (native['candidate_sha256']!=certificate['full_BC_candidate_sha256']
        or sha(args.candidate)!=native['candidate_manifest_sha256']):
        raise ValueError('the full original candidate identity changed')
    left,right=map(Fraction,certificate['exact_requested_interval'])
    original_left,original_right=map(Fraction,native['exact_requested_interval'])
    if left!=0 or original_left!=0 or not 0<right<=original_right:
        raise ValueError('the same original waist and proved prefix are required')
    paths=[Path(x['path']) for x in certificate['complete_parts']]
    audits=[Path(x) for x in certificate.get('interruption_audits',[])]
    if part_checker is checked_v4:
        if (not certificate['interrupted_reports_remain_incomplete']
            or not certificate['all_saved_rows_reconstructed_against_full_exact_original_partition']):
            raise ValueError('the explicit complete saved-row union contract is missing')
        data,parts,verified_inputs,verified_deps,producers=part_checker(paths,right,audits)
    else:
        if audits:raise ValueError('the original complete-piece consumer cannot contain interrupted inputs')
        data,parts,verified_inputs,verified_deps,producers=part_checker(paths,right)
    if (parts!=certificate['complete_parts']
        or verified_inputs!=certificate['verified_native_inputs']
        or verified_deps!=certificate['verified_native_dependencies']
        or producers!=certificate['checked_original_piece_producers']
        or len(data['rows'])!=certificate['complete_rows']
        or verified_inputs.get(str(args.native))!=sha(args.native)
        or verified_inputs.get(str(args.candidate))!=sha(args.candidate)):
        raise ValueError('the complete original piece chain or producer identities changed')
    initial=actual_initial(args.initial,data)
    if initial!=certificate['initial_actual_weighted_derivative']:
        raise ValueError('the independent true initial gradient changed')
    tube=certificate['best_certified_tube']
    if tube not in certificate['passed_tubes'] or tube not in data['tubes']:
        raise ValueError('the selected actual error tube was not certified')
    barrier=propagate(data,upper(initial['weighted_gradient_upper']),tube)
    if not barrier['passed'] or barrier!=certificate['tube_results'][tube]:
        raise ValueError('the full original weighted barrier replay differs')
    selected=[]
    for item in data['rows']:
        index=item['native_row']
        if not isinstance(index,int) or not 0<=index<len(native['rows']):
            raise ValueError('an original coefficient row is missing')
        original=native['rows'][index]
        lo,hi=map(Fraction,item['interval']);nl,nh=map(Fraction,original['interval'])
        gl,gh=map(Fraction,item['actual_scalar_germ']);ol,oh=map(Fraction,original['actual_scalar_germ'])
        if not (gl<=lo<hi<=gh and ol<=nl<=lo<hi<=nh<=oh):
            raise ValueError('the common true weight/coefficient/germ cover changed')
        row=dict(original);row['native_interval']=original['interval']
        row['interval']=item['interval'];row['original_native_row']=index
        selected.append(row)
    if len(selected)!=len(barrier['rows']):raise ValueError('full original weighted rows differ')
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
        e0=upper(error['actual_unweighted_C0']);fee=arb_box(e0)
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
        Cm=(2*ku/gap).upper()
        # Reconstruct the complete true second form separately on every
        # closed angular cell. The global certified gap is an independent
        # valid lower bound, intersected with the same true q-p enclosure.
        denominator=q-p
        denominator=Box(np.maximum(denominator.lo,arb_box(gap).lo),denominator.hi)
        if np.any(denominator.lo<=0) or np.any(denominator.lo>denominator.hi):
            raise ValueError('the true pointwise Riemann denominator is inconsistent')
        actual_A=-2*k*p*q/denominator
        actual_B=-k*(p+q)/denominator
        actual_C=-2*k/denominator
        direct_A=maxabs(actual_A).upper();direct_B=maxabs(actual_B).upper()
        direct_C=maxabs(actual_C).upper()
        A=min(A,direct_A).upper();Bm=min(Bm,direct_B).upper();Cm=min(Cm,direct_C).upper()
        h=exact_arb(hi-lo)
        horizontal=(horizontal+min(h*e,h*e*turnX+h*h*e*e*A/2)).upper()
        displacement=(displacement+h*e).upper()
        turnX=(turnX+h*e*A).upper();turnY=(turnY+h*e*Bm).upper()
        turnN=(turnN+h*e*(A*A+Bm*Bm).sqrt()).upper()
        curvature=max(curvature,max(A,Cm)+Bm).upper()
        al=coefficients['a'].lower();el=coefficients['E'].sqrt().lower()
        amin=al if amin is None else min(amin,al).lower()
        emin=el if emin is None else min(emin,el).lower()
        minimum_sign=sign if minimum_sign is None else min(minimum_sign,sign).lower()
        rows.append(dict(comparison_row=index,original_native_row=item['original_native_row'],
            piece=item['piece'],interval=item['interval'],
            original_native_interval=item['native_interval'],actual_scalar_germ=item['actual_scalar_germ'],
            complete_candidate_B_range=range_record(B),complete_candidate_C_range=range_record(C),
            true_p_range=range_record(p),true_q_range=range_record(q),
            direct_actual_A_range=range_record(actual_A),direct_actual_B_range=range_record(actual_B),
            direct_actual_C_range=range_record(actual_C),
            direct_A_absolute_upper=record(direct_A),direct_B_absolute_upper=record(direct_B),
            direct_C_absolute_upper=record(direct_C),
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
    dependencies=('fourfold_codazzi_cubic_sign_geometry.py','fourfold_codazzi_sharded_candidate.py',
        'fourfold_codazzi_positive_weight_batched_piece_C0_v3.py',
        'fourfold_codazzi_positive_weight_saved_row_C0_v4.py','fourfold_codazzi_positive_weight_cubic_C0.py',
        'fourfold_codazzi_linear_degeneracy_v2.py','fourfold_codazzi_cleared_polynomial_residual.py',
        'fourfold_phase_codazzi_continuation_validate.py','fourfold_phase_beta_bulk_box.py',
        'fourfold_phase_beta_bulk_interval.py','fourfold_phase_two_jet_newton_source.py',
        'fourfold_phase_newton_source_centered.py')
    out=dict(kind='actual_same_Codazzi_positive_weight_complete_sign_and_pointwise_frame_geometry',
        complete=True,continuation_certified=True,embedding_certified=all(gates.values()),
        closed_surface_complete=False,source_sha256=sha(__file__),bits=args.bits,
        inputs={str(p):sha(p) for p in [args.native,args.continuation,args.candidate,args.initial]+paths+audits},
        verified_native_inputs=verified_inputs,verified_native_dependencies=verified_deps,
        checked_original_piece_producers=producers,complete_parts=parts,
        original_continuation_consumer=consumer_name,interruption_audits=list(map(str,audits)),
        full_unweighted_C0_from_all_original_weight_pieces_independently_replayed=True,
        certified_tube=tube,object_sha256=native['object_sha256'],
        candidate_sha256=native['candidate_sha256'],exact_center_parameter=native['exact_center_parameter'],
        parameter_half_width=native['parameter_half_width'],whole_affine_parameter_interval=True,
        whole_real_angular_circle=True,exact_positive_interval=['0',str(right)],
        reflected_interval=[str(-right),str(right)],closed_angle_cells=args.angles,
        finite_candidate_degree=candidate.degree,all_radial_rows_retained=True,
        whole_true_pointwise_Riemann_reconstruction_before_frame_bounds=True,
        all_actual_opposite_signs_proved=all_signs,rows=rows,geometry_gates=gates,
        bounds={k:record(v) for k,v in values.items()},
        dependencies={name:sha(Path(__file__).with_name(name)) for name in dependencies},
        geometry_theorems={str(p):sha(p) for p in (
            Path('results/R123-separated-correction-budgets-and-normal-Hessian.md'),
            Path('results/R126-exact-Codazzi-reconstruction-and-continuation.md'),
            Path('results/R128-quantitative-embedding-of-the-exact-waist-annulus.md'))},
        wall_seconds=time.monotonic()-tick,
        scope='The original exact metric and same-waist Cauchy solution on the explicitly certified reflected interval. All full finite fields are enlarged by the proved unweighted true error before nonlinear curvature reconstruction. No complete closed surface, held displacement, ambient-quotient motion or global reach follows.')
    save(args.out,out)
    print(dict(complete=True,embedding_certified=out['embedding_certified'],
        all_opposite_signs=all_signs,rows=len(rows),bounds={k:v.str(13) for k,v in values.items()},
        wall_seconds=out['wall_seconds']),flush=True)


if __name__=='__main__':main()
