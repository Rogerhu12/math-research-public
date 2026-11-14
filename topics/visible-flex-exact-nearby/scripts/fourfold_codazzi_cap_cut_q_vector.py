#!/usr/bin/env python3
"""Actual q_m(3/2) vector and full 663-cell directed Riccati comparison.

The floating vector is saved first for a finite cut-body probe. The separate
native report retains the true R74 regular fee, full parameter interval,
all primitive tails, and all closed body/graft cells. It does not discard
the higher-mode invariant interval or the nonlinear cap correction.
"""
from __future__ import annotations
import argparse,gzip,json,time
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.sparse import diags
from flint import arb,ctx
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_codazzi_rotational_cap_jacobi import box_from_record,logistic_flow
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha


def read(path):return json.loads(gzip.decompress(Path(path).read_bytes()))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--reference',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    ap.add_argument('--screening',type=Path,default=Path('notes/2026-11-13-R133-cap-analytic-screening-r15-mu3halves-native.json.gz'))
    ap.add_argument('--modes',type=int,default=256)
    ap.add_argument('--floating',type=Path,required=True);ap.add_argument('--native',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320;ctx.cap=6
    if args.floating.exists() or args.native.exists():raise FileExistsError('preserve each actual q-vector attempt')
    if args.modes<1:raise ValueError('positive complete mode count required')
    ref,screen=read(args.reference),read(args.screening)
    if (not ref['complete'] or not ref['cap_linear_reference_certified']
        or not screen['complete'] or not screen['curvature_screening_certified']
        or screen['exact_requested_interval']!=['3/2','25/8']
        or screen['inputs'].get(str(args.reference))!=sha(args.reference)
        or ref['object_sha256']!=sha(args.object)
        or ref['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_rotational_cap_jacobi_v2.py'))):
        raise ValueError('the complete real cap reference identity is required')
    geometry,definition=load_exact_object(args.object,512)
    body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,args.object)
    @lru_cache(maxsize=32768)
    def target(r):
        t=body.point(float(r)) if r<=3 else graft.point(float(r))
        return t['gamma'],t['beta'],t['lambda_ref']
    physical=4*np.arange(1,args.modes+1,dtype=float)
    initial=1/np.sqrt(1+(graft.a_endpoint/(4*graft.omega))**2)
    calls=0;lastprint=time.monotonic()
    def rhs(r,q):
        nonlocal calls,lastprint
        gamma,beta,ell=target(float(r));calls+=1
        if time.monotonic()-lastprint>20:
            print(dict(stage='floating_true_cap_Riccati',radius=float(r),rhs_calls=calls),flush=True);lastprint=time.monotonic()
        return physical*gamma*(q*q-ell)+beta*(ell-1)*q
    def jac(r,q):
        gamma,beta,ell=target(float(r))
        return diags(2*physical*gamma*q+beta*(ell-1),format='csc')
    sol=solve_ivp(rhs,(25/8,3/2),np.full(args.modes,initial),method='Radau',jac=jac,
        rtol=2e-11,atol=2e-13,max_step=.005)
    valid=bool(sol.success and sol.t[-1]==1.5 and np.all(np.isfinite(sol.y)) and np.all(sol.y[:,-1]>0))
    floating=dict(kind='floating_actual_cap_cut_regular_q_vector',complete=True,success=valid,
        certified=False,source_sha256=sha(__file__),object_sha256=sha(args.object),
        reference_sha256=sha(args.reference),left='3/2',right='25/8',modes=args.modes,
        physical_frequencies=physical.astype(int).tolist(),q_values=sol.y[:,-1].tolist(),
        initial_qstar=float(initial),actual_omega_center=float(graft.omega),actual_aR_center=float(graft.a_endpoint),
        method='Radau with full diagonal Jacobian',rtol=2e-11,atol=2e-13,maximum_step=.005,
        successful_radial_steps=len(sol.t)-1,rhs_calls=calls,solver_message=sol.message,
        exact_center_parameter=ref['exact_center_parameter'],primitive_nodes=512,
        nonzero_true_tail_fee_paid_only_by_separate_directed_report=True,
        actual_nonlinear_cap_B_and_C_mean_correction_not_deleted=True,
        wall_seconds=time.monotonic()-started)
    args.floating.write_text(json.dumps(floating,indent=2,allow_nan=False)+'\n')
    print(dict(stage='floating_vector_saved',success=valid,path=str(args.floating),
        q4=float(sol.y[0,-1]),q_last=float(sol.y[-1,-1]),wall_seconds=time.monotonic()-started),flush=True)
    if not valid:raise ValueError('floating actual cap q vector did not reach 3/2')
    # Parse each real closed cell once; no coefficient recomputation or
    # replacement of an original scalar germ is involved.
    selected=[];cursor=Fraction(3,2)
    for chosen in screen['rows']:
        nr=ref['rows'][chosen['native_index']];lo,hi=map(Fraction,chosen['interval'])
        nl,nh=map(Fraction,nr['interval']);gl,gh=map(Fraction,nr['actual_scalar_germ'])
        if lo!=cursor or not gl<=nl<=lo<hi<=nh<=gh:raise ValueError('the complete 663-cell cover differs')
        coeff={k:box_from_record(nr['coefficients'][k]) for k in ('gamma','beta','lambda_ref')}
        gamma,beta,ell=(coeff[k] for k in ('gamma','beta','lambda_ref'));linear=-beta*(ell-1)
        if not gamma>0 or not ell>0:raise ValueError('true positive scalar chart lost')
        selected.append((exact_arb(hi-lo),(gamma.lower()*ell.lower()).lower(),
            (gamma.upper()*ell.upper()).upper(),linear.lower(),linear.upper(),gamma.lower(),gamma.upper()))
        cursor=hi
    if cursor!=Fraction(25,8) or len(selected)!=663:raise ValueError('wrong complete actual cut interval')
    entry=ref['true_R74_entrance'];aa=box_from_record(entry['radius']);omega=box_from_record(entry['normalized_omega'])
    base=1/(1+(aa/(4*omega))**2).sqrt();long=exact_arb(Fraction(2**24)-Fraction(25,8))
    entries=[];failure=None;native_started=time.monotonic()
    try:
        for jj in range(1,args.modes+1):
            M=4*jj;fee=arb(0) if jj==1 else (arb(2)**42*(-2*M*omega.lower()*long).exp()).upper()
            low=(base.lower()-fee).lower();high=(base.upper()+fee).upper()
            for h,al,au,bl,bu,gl,gu in reversed(selected):
                low=logistic_flow(low,(M*al).lower(),bl,(M*gu).upper(),h).lower()
                high=logistic_flow(high,(M*au).upper(),bu,(M*gl).lower(),h).upper()
                if not 0<low<=high:raise ValueError('a full finite-mode Riccati enclosure failed')
            qfloat=arb(float(sol.y[jj-1,-1]))
            entries.append(dict(physical_frequency=M,q_lower=record(low),q_upper=record(high),
                width_upper=record((high-low).upper()),true_R74_regular_fee=record(fee),
                fourth_mode_fee_exactly_zero=jj==1,floating_value=float(sol.y[jj-1,-1]),
                floating_value_inside_directed_box=bool(qfloat>low and qfloat<high)))
            if jj%16==0 or jj==args.modes:
                print(dict(stage='directed_true_Riccati',completed_modes=jj,total_modes=args.modes,
                    last_q_interval=[float(low),float(high)],native_wall=time.monotonic()-native_started),flush=True)
    except Exception as exc:failure=dict(type=type(exc).__name__,message=str(exc))
    complete=bool(failure is None and len(entries)==args.modes)
    result=dict(kind='actual_cap_cut_full_finite_q_vector_and_all_frequency_interval',complete=complete,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.object,args.reference,args.screening,args.floating)},
        object_sha256=ref['object_sha256'],exact_center_parameter=ref['exact_center_parameter'],
        parameter_half_width=ref['parameter_half_width'],whole_affine_parameter_interval=True,
        whole_real_angular_circle=True,complete_primitive_tail=True,left='3/2',right='25/8',
        exact_closed_boxes=663,modes=args.modes,entries=entries,failure=failure,
        entire_finite_vector_certified=complete,
        all_floating_values_inside_directed_boxes=complete and all(v['floating_value_inside_directed_box'] for v in entries),
        full_frequency_invariant_interval=ref['Jacobi']['full_frequency_interval'],
        all_frequencies_beyond_finite_vector_retained=True,
        original_mean_B_and_C_rows_retained=True,
        actual_nonlinear_cap_error_still_required=dict(B_plus_q_c_A0='1.663187e-8',C_mean_abs='4.636375e-9',
            source='results/R133-supplement-universal-small-inner-periodic-cap.md'),
        no_compact_nu_dependence_after_support_endpoint='The compact metric bump vanishes for r>=.18, so this entire true cap is independent of that nu.',
        native_wall_seconds=time.monotonic()-native_started,wall_seconds=time.monotonic()-started,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_codazzi_rotational_cap_jacobi_v2.py',
            'fourfold_codazzi_rotational_cap_jacobi_probe.py','fourfold_phase_codazzi_rotational_reference_probe.py',
            'fourfold_phase_symmetric_geometry.py','fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')})
    save(args.native,result)
    print(dict(stage='directed_vector_saved',complete=complete,path=str(args.native),failure=failure,
        all_floating_values_inside=result['all_floating_values_inside_directed_boxes']),flush=True)
    if not complete:raise ValueError('complete directed q-vector gate failed; original partial report saved')


if __name__=='__main__':main()
