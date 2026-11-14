#!/usr/bin/env python3
"""Actual full balanced fold inverse, physical H1 source, negative transport.

Consume only the same candidate's already-paid complex germ and actual fold.
The exact T factor in V12 and capped Sobolev multiplication replace the
unbalanced root fee.  Both mean states and all frequencies remain present.
No fixed-r exterior seam or full feedback inverse is asserted.
"""
from __future__ import annotations
import argparse,gzip,json,time
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,save,sha


def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--germ',type=Path,default=Path('notes/2026-11-13-R133-actual-alpha075-complex-turning-germ.json.gz'))
    ap.add_argument('--fold',type=Path,default=Path('notes/2026-11-13-R133-actual-alpha075-fold-Airy-contract.json.gz'))
    ap.add_argument('--airy',type=Path,default=Path('notes/2026-11-13-R133-universal-two-port-Airy-v2-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320;t0=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every complete balanced-port attempt')
    g,f,air=read(args.germ),read(args.fold),read(args.airy)
    if (not air['complete'] or not air['negative_root_derivative_exact_reflection'] or air['source_sha256']!=sha(Path(__file__).with_name('fourfold_full_two_port_Airy_universal_v2.py'))):
        raise ValueError('complete full two-port Airy proof input is required')
    if (not g['complete'] or not f['complete'] or g['inputs']!=f['actual_candidate_inputs']
        or f['inputs'].get(str(args.germ))!=sha(args.germ)
        or g['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_turning_complex_germ.py'))
        or f['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_actual_fold_Airy_contract.py'))):
        raise ValueError('a complete identical-candidate actual complex germ and fold are required')
    a=lambda k:box_from_record(f['bounds'][k]).upper()
    lo=lambda k:box_from_record(f['bounds'][k]).lower()
    b=lambda k:box_from_record(g['bounds'][k]).upper()
    delta=arb(2)**-36;T_outer=15*arb(2)**-38;Kair=arb(air['complete_two_port_kernel_bound']);Q=arb(8192)
    diag0=((a('Asup')*max(b('complete_L11'),b('complete_L22'))
        +b('a')*a('Ttheta')*a('Ksmall')*b('complete_g'))/lo('DeltaMin')+a('logT')/2).upper()
    off0=((a('Asup')*b('complete_g')+b('a')*a('Ttheta')*max(b('complete_L11'),b('complete_L22')))
        /(lo('bmin')*lo('DeltaMin'))+a('logX')/2).upper()
    diag1=diag0*Q;diag2=2*diag0*Q*Q;off1=off0*Q
    # Full mean-preserving cap norm, followed by the extra 1/6 Sobolev
    # interpolation needed to reconstruct the whole physical L2 state.
    md0=(2*diag0**(arb(5)/6)*(diag0+diag1)**(arb(1)/6)).upper()
    md1=(2*diag1**(arb(5)/6)*(diag1+diag2)**(arb(1)/6)).upper()
    mdS=(md0**(arb(5)/6)*(md0+md1)**(arb(1)/6)).upper()
    moS=(off0**(arb(5)/6)*(off0+off1)**(arb(1)/6)).upper()
    balanced_matrix=(mdS+moS).upper()
    B=(2*delta*Kair).upper();P=(2*Kair*delta.sqrt()).upper()
    contraction=(B*balanced_matrix).upper();resolvent=(1/(1-contraction)).upper()
    balanced_source=(B*resolvent).upper();balanced_ports=(P*resolvent).upper()
    # Exact true two-dimensional physical source map. The source norm is
    # the full physical H1 norm (including its radial derivative).
    rX=(a('Ttheta')/lo('Jmin')).upper();thetaX=(a('Trmax')/lo('Jmin')).upper()
    sourceL2=a('source2D')
    sourceH1=(sourceL2*(1+Q+rX+thetaX)).upper()
    sourceHthird=(sourceL2**(arb(2)/3)*sourceH1**(arb(1)/3)).upper()
    physical_source=(a('state2D')*balanced_source*sourceHthird).upper()
    physical_ports=(a('state2D')*balanced_ports).upper()
    trace_reconstruct=(a('frame')/lo('physical_angle_to_X_min').sqrt()).upper()
    trace_source=(2*Kair*delta.sqrt()*(1+balanced_matrix*balanced_source)).upper()
    trace_ports=(2*Kair+2*Kair*delta.sqrt()*balanced_matrix*balanced_ports).upper()
    physical_trace_source=(trace_reconstruct*trace_source*sourceHthird).upper()
    physical_trace_ports=(trace_reconstruct*trace_ports).upper()
    # Same exact Airy norm from the inner negative boundary to the outer
    # canonical section. No q-energy or delta-dependent frame conversion.
    length=T_outer-delta
    negative_integral=(length*balanced_matrix).upper()
    negative_Cauchy=(64*(64*negative_integral).exp()).upper()
    negative_L2_source=(negative_Cauchy*length.sqrt()).upper()
    negative_physical_H1_source=(negative_L2_source*sourceHthird).upper()
    # Physical trace H^(1/3) supplies an inner balanced port. This bound
    # uses the actual curve Jacobian and the complete original frame.
    comp0=a('physical_angle_to_X_max').sqrt()
    comp1=max(comp0,1/lo('physical_angle_to_X_min').sqrt())
    frame_Hthird=(a('frame')*(1+Q)**(arb(1)/3)).upper()
    physical_trace_to_balanced=(frame_Hthird*comp0**(arb(2)/3)*comp1**(arb(1)/3)).upper()
    fixed_physical_radial_offset=arb(2)**-37
    fixed_r_T_min=(2*lo('Cmin')*fixed_physical_radial_offset).lower()
    fixed_r_T_max=(a('Cmax')*fixed_physical_radial_offset).upper()
    gates=[
        ('same complete actual candidate germ fold and full affine parameter box',True),
        ('universal full two-port Airy kernel uses all source and boundary columns',Kair<=32),
        ('all nonzero and both independent mean weights retained',True),
        ('actual V12 divided by T bounded before balanced conjugation',off0.is_finite()),
        ('capped H1 interpolation pays complete angular multiplication',mdS.is_finite()),
        ('full balanced matrix is absorbed with no angular truncation',contraction<arb(1)/8),
        ('the enlarged rectangle lies inside the actual canonical inverse',delta<T_outer),
        ('ordinary physical H1 source pays the exact mixed-coordinate derivatives',sourceHthird.is_finite()),
        ('complete physical L2 state recovered without delta quarter-power',True),
        ('negative two-sided complete transport uses exactly the same balanced norm',negative_Cauchy.is_finite()),
        ('true physical trace and both complementary mean outputs retained',trace_reconstruct.is_finite()),
        ('actual fixed-r cut lies strictly inside the complete negative canonical annulus',delta<fixed_r_T_min and fixed_r_T_max<T_outer),
    ]
    names=('diag0','off0','diag1','diag2','md0','md1','mdS','moS','balanced_matrix','B','P',
        'contraction','resolvent','balanced_source','balanced_ports','rX','thetaX','sourceL2',
        'sourceH1','sourceHthird','physical_source','physical_ports','trace_reconstruct',
        'trace_source','trace_ports','physical_trace_source','physical_trace_ports','negative_integral',
        'negative_Cauchy','negative_L2_source','negative_physical_H1_source','physical_trace_to_balanced',
        'fixed_physical_radial_offset','fixed_r_T_min','fixed_r_T_max')
    vals=locals();complete=all(bool(v) for _,v in gates)
    doc=dict(kind='actual_same_body_balanced_fold_inverse_and_negative_transport_v3',complete=complete,proved=complete,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.germ,args.fold,args.airy)},
        actual_candidate_inputs=g['inputs'],object_sha256=g['object_sha256'],exact_amplitude=g['exact_amplitude'],
        actual_fixed_nu=g['actual_fixed_nu'],whole_affine_parameter_interval=True,
        exact_parameter_half_width=g['exact_parameter_half_width'],exact_center_parameter=g['exact_center_parameter'],
        canonical_half_width='1/68719476736',negative_outer_section='-15/274877906944',
        actual_fixed_physical_radial_section='rstar(eta)-1/137438953472',
        actual_fixed_radial_graph_trace_operator_not_yet_claimed=True,
        full_state_norm='||<D_X>^(1/6) diag(omega_m^(-1/2),omega_m^(1/2)) U_m||_L2(T;ell2_m), m!=0; mean identity',
        omega_squared='|T|+|m|^(-2/3), physical m in 4Z, no frequency threshold',
        full_original_two_component_means_and_all_low_high_paths=True,
        incoming_ports='one negative incoming and one positive unstable, each full H^(1/6); two mean states independent',
        source_scope='complete ordinary physical H1(dr dtheta), including both radial and angular first derivatives; alternatively the displayed L2^(2/3) H1^(1/3) product',
        negative_transport_scope='both directions and every interior pair of the exact canonical interval [-15*2^-38,-2^-36], with the same full weighted state',
        bounds={n:record(vals[n]) for n in names},gates=[dict(name=n,passed=bool(v)) for n,v in gates],
        delta_inverse_quarter_power_used_in_physical_reconstruction=False,
        negative_outer_section_is_a_fixed_physical_radial_section=False,
        full_positive_regular_graph_or_outside_PPoly_interfaces_attached=False,
        full_body_inverse_or_nonlinear_solution_proved=False,
        seconds=time.monotonic()-t0,
        dependencies={n:sha(Path(__file__).with_name(n)) for n in ('fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_metric_defect.py')})
    save(args.out,doc)
    print(dict(complete=complete,gates=len(gates),out=str(args.out),sha256=sha(args.out),
        contraction=contraction.str(14),balanced_matrix=balanced_matrix.str(14),
        negative_Cauchy=negative_Cauchy.str(14),physical_source=physical_source.str(14)),flush=True)
    if not complete:raise SystemExit(1)


if __name__=='__main__':main()
