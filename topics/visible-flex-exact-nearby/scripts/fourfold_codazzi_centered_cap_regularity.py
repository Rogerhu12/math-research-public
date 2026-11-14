#!/usr/bin/env python3
"""Consume a complete nonzero-centre cap contraction and all angular inputs.

All exact dyadic radial interface point sources must already be paid.
One explicit residual-based smaller radius may sharpen the already certified
ball. All attempts and strict gates are retained. Angular regularity follows
from the true translation/Neumann argument, not from finite output spectra.
"""
from __future__ import annotations
import argparse,gzip,json
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,save,sha


def read(path):return json.loads(gzip.decompress(Path(path).read_bytes()))


def exact(value):
    q=Fraction(value);return arb(q.numerator)/q.denominator


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native',type=Path,default=Path('notes/2026-11-13-R133-centered-cap-r1-v4-jumps-native.json.gz'))
    ap.add_argument('--kernels',type=Path,default=Path('notes/2026-11-13-R133-A0-driven-cap-r1-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve completed regularity budgets and real failures')
    native,kernels=read(args.native),read(args.kernels)
    producer=Path(__file__).with_name('fourfold_codazzi_centered_cap_interface_jumps.py')
    if (native['kind']!='actual_complete_nonzero_centred_cap_with_all_exact_interface_jumps'
        or not native['complete'] or not native['nonzero_centred_contraction_certified']
        or not native['actual_driven_cap_exists'] or not native['actual_solution_radially_continuous']
        or native['source_sha256']!=sha(producer)
        or native['inputs'][str(args.kernels)]!=sha(args.kernels)):
        raise ValueError('a complete actual nonzero-centred contraction is required')
    for doc in (native,kernels):
        if not all(doc[k] for k in ('whole_affine_parameter_interval','whole_real_angular_circle','complete_primitive_tail')):
            raise ValueError('complete true target scope changed')
        for name,h in doc.get('dependencies',{}).items():
            if sha(Path(__file__).with_name(name))!=h:raise ValueError('frozen dependency changed: '+name)
    for path,h in native['inputs'].items():
        if sha(path)!=h:raise ValueError('a complete residual input changed: '+path)
    for key in ('object_sha256','exact_center_parameter','parameter_half_width','exact_requested_interval'):
        if native[key]!=kernels[key]:raise ValueError('native and Green kernels have different identities')
    b={k:box_from_record(v) for k,v in native['bounds'].items()}
    c={k:box_from_record(v) for k,v in kernels['constants'].items()}
    Bn,Cn,eps=(b[k].upper() for k in ('centre_B_global_A0','centre_c_global_A0','fixed_point_residual_upper'))
    Cstar=c['reference_C_abs_lower'].lower();L=max(arb(1),c['ell_upper']).upper();G=c['complete_pair_nonlinear_kernel'].upper()
    old_radius=exact(native['exact_correction_radius'])
    relative=native['full_DQ_bound_kind']=='relative'
    if relative:Br,Cr=(b[k].upper() for k in ('centre_B_relative_A0','centre_c_relative_A0'))
    def budget(rho):
        if relative:
            br=(Br+rho/Cstar).upper();cr=(Cr+rho/Cstar).upper();dr=(1-cr).lower();d=(Cstar*dr).lower()
            if not d>0:return dict(passed=False,radius=record(rho),failure='actual relative denominator')
            DB=(2*br/dr).upper();DC=(2*L*cr/dr+(br*br+L*cr*cr)/(dr*dr)).upper()
        else:
            d=(Cstar-Cn-rho).lower()
            if not d>0:return dict(passed=False,radius=record(rho),failure='actual denominator')
            Bplus=(Bn+rho).upper();Cplus=(Cn+rho).upper()
            DB=(2*Bplus/d).upper();DC=(2*L*Cplus/d+(Bplus*Bplus+L*Cplus*Cplus)/(d*d)).upper()
        lam=(G*max(DB,DC)).upper();image=(eps+lam*rho).upper()
        passed=bool(lam<1 and image<rho)
        return dict(passed=passed,radius=record(rho),actual_C_abs_lower=record(d),
            full_Q_B_derivative=record(DB),full_Q_c_derivative=record(DC),
            contraction=record(lam),image=record(image),image_margin=record((rho-image).lower()),
            contraction_margin=record((1-lam).lower()))
    original=budget(old_radius)
    if not original['passed']:raise ValueError('the already successful complete contraction does not reproduce')
    zero_budget=budget(arb(0))
    if 'contraction' not in zero_budget:raise ValueError('zero-radius full derivative denominator failed')
    lam0=box_from_record(zero_budget['contraction']).upper()
    attempted=None;chosen=original
    if lam0<1:
        trial=(2*eps/(1-lam0)).upper()
        if 0<trial<old_radius:
            attempted=budget(trial)
            if attempted['passed']:chosen=attempted
    rho=box_from_record(chosen['radius']).upper();d=box_from_record(chosen['actual_C_abs_lower']).lower()
    lam=box_from_record(chosen['contraction']).upper();actual_error=(eps/(1-lam)).upper()
    if not actual_error<rho:raise ValueError('actual a-posteriori error is not inside the selected strict ball')
    port=kernels['actual_finite_inner_port']
    if (not port['all_nonzero_boundary_modes_present'] or not port['omitted_boundary_modes_exactly_zero']
        or port['sha256']!=sha(port['path']) or native['inputs'][port['path']]!=port['sha256']
        or port['exact_cut']!=native['exact_requested_interval'][0]):
        raise ValueError('the complete actual finite input trace changed')
    coeff=list(map(box_from_record,port['exact_dyadic_cosine_coefficient_enclosures']))
    if len(coeff)!=port['modes']:raise ValueError('the physical input list is incomplete')
    Hc=c['boundary_c_factor'].upper();Hd=c['boundary_d_factor'].upper()
    eD=exact(native['outer_nonzero_d_A2_budget'])
    norms=[sum((arb(4*(j+1))**order*abs(v) for j,v in enumerate(coeff)),arb(0)).upper() for order in (1,2)]
    H1=(Hc*norms[0]+Hd*eD).upper();H2=(Hc*norms[1]+Hd*eD).upper()
    S=(Bn+Cn+rho).upper();J2=(L*(2/d+4*S/(d*d)+2*S*S/(d*d*d))).upper()
    first=(H1/(1-lam)).upper();second=((H2+G*J2*first*first)/(1-lam)).upper()
    full_X2=(S+2*first+second).upper()
    report=dict(kind='actual_nonzero_centred_cap_strong_translation_regularization_v1',complete=True,
        source_sha256=sha(__file__),input_sha256=sha(args.native),kernels_sha256=sha(args.kernels),
        object_sha256=native['object_sha256'],exact_center_parameter=native['exact_center_parameter'],
        parameter_half_width=native['parameter_half_width'],exact_requested_interval=native['exact_requested_interval'],
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,complete_primitive_tail=True,
        original_strict_ball=original,one_explicit_smaller_radius_attempt=attempted,chosen_strict_ball=chosen,
        smaller_radius_formula='2*complete_residual/(1-zero_radius_full_DQ_bound); only used if its full actual gates pass',
        bounds={k:record(v) for k,v in dict(complete_residual=eps,complete_pair_X0=S,
            actual_correction_X0=actual_error,true_C_abs_lower=((Cstar*(1-Cr)-actual_error) if relative else (Cstar-Cn-actual_error)).lower(),
            zero_radius_full_DQ_bound=lam0,full_second_nonlinearity_derivative=J2,
            exact_inner_C_theta_A0=norms[0],exact_inner_C_thetatheta_A0=norms[1],
            differentiated_boundary_H1=H1,differentiated_boundary_H2=H2,
            full_theta_derivative_X0=first,full_second_theta_derivative_X0=second,
            full_inhomogeneous_X2=full_X2).items()},
        all_exact_radial_interface_point_sources_paid=True,solution_radially_continuous=True,
        full_DQ_bound_kind=native['full_DQ_bound_kind'],
        all_physical_Fourier_modes_retained=True,means_retained_with_exact_zero_angular_derivatives=True,
        outer_d_regularization_paid_by_its_inhomogeneous_A2_budget=True,
        finite_output_regularization_not_assumed=True,
        nonlinear_regular_tail_matched=False,body_matched=False,periodic_frame_holonomy_proved=False,closed_surface_complete=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_centered_cap_interface_jumps.py','fourfold_codazzi_cap_A0_translation_budget.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_metric_defect.py')})
    save(args.out,report)
    print(dict(error=actual_error.str(14),chosen_radius=rho.str(14),contraction=lam.str(14),
        theta=first.str(14),thetatheta=second.str(14),complete_X2=full_X2.str(14)),flush=True)


if __name__=='__main__':main()
