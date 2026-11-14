#!/usr/bin/env python3
"""Pay every exact dyadic centre interface in the full cap Green residual.

The ambient algebra is l1 of the finite piecewise-continuous max norm.
The full fixed point U is continuous by its original Green integral equation;
the correction V has the opposite jumps to the exact stored polynomial centre.
"""
from __future__ import annotations
import argparse,gzip,json
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,save,sha


def read(path):return json.loads(gzip.decompress(Path(path).read_bytes()))


def exact(value):
    q=Fraction(value);return arb(q.numerator)/q.denominator


def dyadic(value):return Fraction.from_float(float(value))


PRODUCERS={
    'actual_complete_nonzero_centre_cap_residual_and_contraction_stable_joint_Taylor_v4':
        ('fourfold_codazzi_cap_centered_residual_v4.py','absolute',Fraction(1,500)),
    'actual_complete_nonzero_centre_cap_residual_and_relative_DQ_stable_joint_Taylor_v5':
        ('fourfold_codazzi_cap_centered_residual_v5.py','relative',Fraction(1,2000)),
}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native',type=Path,default=Path('notes/2026-11-13-R133-centered-cap-r1-v4-native.json.gz'))
    ap.add_argument('--kernels',type=Path,default=Path('notes/2026-11-13-R133-A0-driven-cap-r1-native.json.gz'))
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-R133-compact-metric-outer-mean-m64-candidate.npz.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve every complete interface attempt')
    native,kernels=read(args.native),read(args.kernels)
    if native['kind'] not in PRODUCERS:raise ValueError('unreviewed regular-residual producer')
    producer,bound_kind,rho_exact=PRODUCERS[native['kind']]
    if (not native['complete'] or native['source_sha256']!=sha(Path(__file__).with_name(producer))
        or native['inputs'].get(str(args.kernels))!=sha(args.kernels)
        or native['inputs'].get(str(args.candidate))!=sha(args.candidate)
        or not kernels['complete'] or not kernels['unweighted_nonzero_rates_positive']
        or not kernels['backward_mean_rates_positive']
        or kernels['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_cap_A0_translation_budget.py'))):
        raise ValueError('complete regular residual, centre, or all-mode Green identity changed')
    for doc in (native,kernels):
        if not all(doc[k] for k in ('whole_affine_parameter_interval','whole_real_angular_circle','complete_primitive_tail')):
            raise ValueError('complete target scope changed')
        for name,h in doc.get('dependencies',{}).items():
            if sha(Path(__file__).with_name(name))!=h:raise ValueError('frozen dependency changed: '+name)
    for path,h in native['inputs'].items():
        if sha(path)!=h:raise ValueError('complete regular-residual input changed: '+path)
    for key in ('object_sha256','exact_center_parameter','parameter_half_width','exact_requested_interval'):
        if native[key]!=kernels[key]:raise ValueError('target or interval identity changed: '+key)
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']));m=int(meta['modes'])
    if (m!=native['centre_all_modes'] or meta['object_sha256']!=native['object_sha256']
        or meta['coordinates']!='B=alpha*b; C=Cref_nu+alpha*c'):
        raise ValueError('wrong complete physical centre')
    left,right=map(Fraction,native['exact_requested_interval'])
    nodes=list(map(dyadic,saved['radial_nodes']));coef=saved['piece_coefficients']
    if (not nodes[0]<=left<right<=nodes[-1] or left<Fraction(18,100)
        or any(a>=b for a,b in zip(nodes[:-1],nodes[1:]))
        or coef.shape!=(4,len(nodes)-1,2*m+1) or not np.all(np.isfinite(coef))):
        raise ValueError('complete centre pieces or unchanged positive target missing')
    alpha=dyadic(meta['amplitude']);sums=[Fraction(0)]*(2*m+1);rows=[]
    largest=Fraction(0);nonzero_entries=0
    for j in range(1,len(nodes)-1):
        if not left<nodes[j]<right:continue
        h=nodes[j]-nodes[j-1];jumps=[]
        for k in range(2*m+1):
            previous=dyadic(coef[0,j-1,k])
            for value in coef[1:,j-1,k]:previous=previous*h+dyadic(value)
            # The reference Cref is the same continuous true radial function
            # on both sides. Its exact jump is zero; c retains its full mean.
            jump=alpha*(dyadic(coef[3,j,k])-previous)
            jumps.append(jump);sums[k]+=abs(jump)
            largest=max(largest,abs(jump));nonzero_entries+=int(jump!=0)
        JB=sum(map(abs,jumps[:m]),Fraction(0))
        JC=sum(map(abs,jumps[m+1:]),Fraction(0));J0=abs(jumps[m])
        rows.append(dict(join=str(nodes[j]),left_piece=j-1,right_piece=j,
            exact_B_nonzero_jump_A0=str(JB),exact_c_nonzero_jump_A0=str(JC),
            exact_c_mean_jump=str(J0),exact_B_mean_jump='0',
            nonzero_dyadic_jump_coefficients=sum(x!=0 for x in jumps)))
    JBq=sum(sums[:m],Fraction(0));JCq=sum(sums[m+1:],Fraction(0));J0q=sums[m]
    JB,JC,J0=map(exact,(JBq,JCq,J0q))
    b={k:box_from_record(v) for k,v in native['bounds'].items()}
    c={k:box_from_record(v) for k,v in kernels['constants'].items()}
    HD=c['boundary_d_factor'].upper();HC=c['boundary_c_factor'].upper();qp=c['q_upper'].upper()
    jump_fee=(HD*JB+(HD*qp+HC)*JC+J0).upper()
    eps=(b['fixed_point_residual_upper'].upper()+jump_fee).upper()
    Cstar=c['reference_C_abs_lower'].lower();L=max(arb(1),c['ell_upper']).upper()
    G=c['complete_pair_nonlinear_kernel'].upper();rho=exact(rho_exact)
    if not b['correction_radius'].contains(rho):raise ValueError('explicit radius no longer matches the native attempt')
    Bn=b['centre_B_global_A0'].upper();Cn=b['centre_c_global_A0'].upper()
    if bound_kind=='absolute':
        gap=(Cstar-Cn-rho).lower();bp=(Bn+rho).upper();cp=(Cn+rho).upper()
        if not gap>0:raise ValueError('actual complete absolute denominator failed')
        DB=(2*bp/gap).upper();DC=(2*L*cp/gap+(bp*bp+L*cp*cp)/(gap*gap)).upper()
    else:
        br=b['centre_B_relative_A0'].upper()+rho/Cstar
        cr=b['centre_c_relative_A0'].upper()+rho/Cstar;d=(1-cr).lower();gap=(Cstar*d).lower()
        if not d>0:raise ValueError('actual complete relative denominator failed')
        DB=(2*br/d).upper();DC=(2*L*cr/d+(br*br+L*cr*cr)/(d*d)).upper()
    lip=(G*max(DB,DC)).upper();image=(eps+lip*rho).upper();passed=bool(lip<1 and image<rho)
    bounds=dict(native['bounds']);bounds.update({k:record(v) for k,v in dict(
        regular_part_fixed_point_residual=b['fixed_point_residual_upper'],
        total_B_nonzero_jump_A0=JB,total_c_nonzero_jump_A0=JC,total_c_mean_jump=J0,
        full_interface_point_source_fee=jump_fee,fixed_point_residual_upper=eps,
        correction_radius=rho,actual_C_abs_lower=gap,full_Q_B_derivative=DB,full_Q_c_derivative=DC,
        full_contraction_factor=lip,closed_ball_image_upper=image,
        closed_ball_margin=(rho-image).lower(),contraction_margin=(1-lip).lower()).items()})
    inputs=dict(native['inputs']);inputs[str(args.native)]=sha(args.native)
    report=dict(kind='actual_complete_nonzero_centred_cap_with_all_exact_interface_jumps',complete=True,
        source_sha256=sha(__file__),regular_residual_kind=native['kind'],
        regular_residual_path=str(args.native),regular_residual_sha256=sha(args.native),
        inputs=inputs,object_sha256=native['object_sha256'],exact_center_parameter=native['exact_center_parameter'],
        parameter_half_width=native['parameter_half_width'],exact_requested_interval=native['exact_requested_interval'],
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,complete_primitive_tail=True,
        regular_closed_boxes=len(native['rows']),centre_all_modes=m,interior_exact_joins=len(rows),
        all_interfaces=rows,exact_sum_of_absolute_jumps_by_real_sine_cosine_coefficient=list(map(str,sums)),
        exact_largest_individual_jump=str(largest),nonzero_dyadic_jump_coefficients=nonzero_entries,
        centre_exactly_continuous=bool(nonzero_entries==0),
        ambient_norm='sum_m max_piece sup_closed_piece |f_m|; both interface traces retained; pair sum norm',
        correction_is_not_required_to_be_radially_continuous=True,
        full_DQ_bound_kind=bound_kind,exact_correction_radius=str(rho_exact),bounds=bounds,
        nonzero_centred_contraction_certified=passed,actual_driven_cap_exists=passed,
        actual_solution_radially_continuous=passed,
        original_integral_equation='U = H h + G_Q Q(U); every centre jump is subtracted in V by the exact Green residual identity',
        failure=None if passed else 'complete regular residual plus all interface point sources failed the strict ball gates',
        outer_nonzero_d_A2_budget=native['outer_nonzero_d_A2_budget'],
        outer_B_mean_budget=native['outer_B_mean_budget'],outer_c_mean_budget=native['outer_c_mean_budget'],
        inner_C_nonzero_exactly_the_complete_centre=True,mean_at_left_is_an_output=True,
        uncorrected_native_existence_flag_is_not_used=True,
        nonlinear_regular_tail_matched=False,body_matched=False,periodic_frame_holonomy_proved=False,closed_surface_complete=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            producer,'fourfold_codazzi_cap_A0_translation_budget.py','fourfold_codazzi_candidate_shards.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_metric_defect.py')})
    save(args.out,report)
    print(dict(passed=passed,interior_joins=len(rows),nonzero_jump_coefficients=nonzero_entries,
        jump_fee=jump_fee.str(16),complete_residual=eps.str(16),image=image.str(16),contraction=lip.str(16)),flush=True)


if __name__=='__main__':main()
