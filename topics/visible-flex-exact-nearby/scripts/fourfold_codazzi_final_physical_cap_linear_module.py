#!/usr/bin/env python3
"""Actual ac1 continuous all-mode physical cap Jacobi module.

The centre is evaluated in its true moving angle.  A full analytic inverse
of theta=phi+psi bounds the *physical* multiplication coefficients.  The
reference Green is the true rotational two-ended q_M Green, not a radial
collocation inverse.  Unknown modes, both means, ordinary/divergence
sources and independent physical jumps are retained.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

from flint import arb, ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_current_positive_complete_coefficients import (
    CURRENT_SHA, OBJECT_SHA, checked_cap, convolution, dyadic, full_fields,
    literal_coordinates, polynomial_values,
)
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha


def upper(z):
    return abs(z).upper()


def nonnegative_max(a, b):
    return max(a.upper(), b.upper()).upper()


def norm_envelope(values, start, width):
    return sum((x * (4 * abs(k) * width).exp()
                for k, x in zip(range(start, start+len(values)), values)), arb(0)).upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--cap-cache',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    ap.add_argument('--left',type=Fraction,default=Fraction(9,10))
    ap.add_argument('--inverse-width',type=Fraction,default=Fraction(1,64))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(1,10**9))
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args(); started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve each complete cap attempt')
    if not Fraction(239,1000)<=args.left<Fraction(25,8) or args.bits<256:
        raise ValueError('invalid true positive cap domain or precision')
    if not Fraction(0)<args.inverse_width<=Fraction(1,16):
        raise ValueError('invalid declared analytic inversion radius')
    ctx.prec=args.bits;ctx.cap=6
    if sha(args.candidate)!=CURRENT_SHA or sha(args.object)!=OBJECT_SHA:
        raise ValueError('this report belongs only to the actual final ac1 centre')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    if meta['object_sha256']!=OBJECT_SHA or meta['coordinates']!=literal_coordinates():
        raise ValueError('physical and moving candidate coordinates cannot be interchanged')
    modes=int(meta['modes']);alpha=exact_arb(dyadic(meta['amplitude']))
    if modes!=32 or Fraction(meta['exact_float_nu'])!=Fraction(-2572625729470897,72057594037927936):
        raise ValueError('the exact complete current centre identity changed')
    cap=checked_cap(args.cap_cache,args.object,args.half_width)
    nodes=list(map(dyadic,saved['radial_nodes']))
    entry=cap['true_R74_entrance']
    radius=box_from_record(entry['radius']);omega=box_from_record(entry['normalized_omega'])
    initial=1/(1+(radius/(4*omega))**2).sqrt()
    fee=box_from_record(cap['Jacobi']['full_frequency_interval']['complete_true_tail_fee']).upper()
    qlo=(initial.lower()-fee).lower();qhi=(initial.upper()+fee).upper()
    slack=arb(2)**-128; reference=[]
    if not qlo>0:raise ValueError('the complete actual rotational outer line is not positive')
    for index in reversed(range(len(cap['rows']))):
        native=cap['rows'][index]
        lo,hi=map(Fraction,native['interval'])
        if hi<=args.left:continue
        c={k:box_from_record(v) for k,v in native['coefficients'].items()}
        ell,gamma,beta=c['lambda_ref'],c['gamma'],c['beta']
        lin=-beta*(ell-1)/(4*gamma)
        bl=min(arb(0),lin.lower());bu=max(arb(0),lin.upper())
        elllo,ellhi=ell.lower(),ell.upper()
        lo_root=(2*elllo/((bl*bl+4*elllo).sqrt()-bl)).lower()
        hi_root=((bu+(bu*bu+4*ellhi).sqrt())/2).upper()
        qlo=min(qlo,lo_root).lower();qhi=max(qhi,hi_root).upper()
        ql=(qlo*(1-slack)).lower();qu=(qhi*(1+slack)).upper()
        face_lo=(elllo+bl*ql-ql*ql).lower()
        face_hi=(qu*qu-bu*qu-ellhi).lower()
        sd=(gamma*ql+min(arb(0),(-2*beta).lower())/4).lower()
        sc=(gamma*ql+min(arb(0),(beta*(ell+1)).lower())/4).lower()
        reference.append(dict(native_index=index,left=max(lo,args.left),right=hi,
            c=c,q_lower=ql,q_upper=qu,D_rate=sd,C_rate=sc,
            lower_face=face_lo,upper_face=face_hi,
            T=(gamma.upper()/sc).upper() if sc>0 else arb('inf'),
            KD=((gamma.upper()+qu*upper(beta)/4)/sd).upper() if sd>0 else arb('inf'),
            KC=(upper(beta)/(4*sc)).upper() if sc>0 else arb('inf')))
    reference.reverse();cursor=args.left
    for row in reference:
        if row['left']!=cursor or row['right']<=cursor:raise ValueError('the true cap suffix has a gap')
        cursor=row['right']
    if cursor!=Fraction(25,8):raise ValueError('the actual cap does not reach the true outer port')
    rates_pass=all(row['D_rate']>0 and row['C_rate']>0 and row['c']['beta']<0
                   and row['lower_face']>0 and row['upper_face']>0 for row in reference)
    if not rates_pass:
        save(args.out,dict(kind='actual_final_physical_cap_linear_module_v1',complete=False,
            source_sha256=sha(__file__),failure='one of the actual all-mode Green faces/rates failed',
            left=str(args.left),reference_rows=[dict(native_index=r['native_index'],
            interval=[str(r['left']),str(r['right'])],
            bounds={k:record(r[k]) for k in ('D_rate','C_rate','lower_face','upper_face')}) for r in reference]))
        print(dict(complete=False,reason='reference rates'),flush=True);return

    # Enclose every actual finite coefficient on every true radial intersection.
    # Maxima are taken coefficientwise before the l1 sum, exactly matching X_sigma.
    qb=[arb(0) for _ in range(2*modes+1)]
    qc=[arb(0) for _ in range(4*modes+1)]
    psi=[arb(0) for _ in range(2*modes+1)]
    psip=[arb(0) for _ in range(2*modes+1)]
    cover=[];minimum_mean=None;physical_jmin=None;physical_jmax=arb(0)
    for row in reference:
        lo,hi=row['left'],row['right'];c=row['c'];s=1/c['Cref'];K=c['K']
        cuts=[lo,*[r for r in nodes if lo<r<hi],hi]
        for left,right in zip(cuts[:-1],cuts[1:]):
            piece=bisect_right(nodes,left)-1
            vals=polynomial_values(saved,nodes,piece,left,right)
            ui,dv=full_fields(vals,modes,alpha,arb(0))
            mean=s+dv[modes]
            if not mean<0:raise ValueError('the same current moving mean is not negative')
            mg=(-mean).lower()
            minimum_mean=mg if minimum_mean is None else min(minimum_mean,mg).lower()
            u2=[-x for x in convolution(ui,ui)];dv2=convolution(dv,dv)
            Qc=[]
            for k in range(-2*modes,2*modes+1):
                vlin=dv[k+modes] if -modes<=k<=modes else arb(0)
                Qc.append(-u2[k+2*modes]-K*(2*s*vlin+dv2[k+2*modes]))
            for i,z in enumerate(ui):qb[i]=nonnegative_max(qb[i],upper(2*z))
            for i,z in enumerate(Qc):qc[i]=nonnegative_max(qc[i],upper(z))
            ratio_ne=arb(0)
            for k in range(-modes,modes+1):
                if not k:continue
                z=upper(dv[k+modes]/mean)
                psi[k+modes]=nonnegative_max(psi[k+modes],z/(4*abs(k)))
                psip[k+modes]=nonnegative_max(psip[k+modes],z)
                ratio_ne+=z
            jlo=(1-ratio_ne).lower();jhi=(1+ratio_ne).upper()
            physical_jmin=jlo if physical_jmin is None else min(physical_jmin,jlo).lower()
            physical_jmax=max(physical_jmax,jhi).upper()
            cover.append(dict(native_index=row['native_index'],candidate_piece=piece,
                interval=[str(left),str(right)],actual_scalar_germ=cap['rows'][row['native_index']]['actual_scalar_germ']))
        if len(cover)%400<10:print(dict(complete_radial_intersections=len(cover),at=str(hi)),flush=True)
    width=exact_arb(args.inverse_width)
    inversion_displacement=norm_envelope(psi,-modes,2*width)
    inversion_lip=norm_envelope(psip,-modes,2*width)
    DB=norm_envelope(qb,-modes,2*width);DC=norm_envelope(qc,-2*modes,2*width)
    actual_multiplication=max(DB,DC).upper()
    inverse_pass=bool(inversion_displacement<width and inversion_lip<1 and physical_jmin>0)
    qplus=max(r['q_upper'] for r in reference).upper()
    sd=min(r['D_rate'] for r in reference).lower();sc=min(r['C_rate'] for r in reference).lower()
    T=max(r['T'] for r in reference).upper()
    KD=max(r['KD'] for r in reference).upper();KC=max(r['KC'] for r in reference).upper()
    ellmin=min(r['c']['lambda_ref'].lower() for r in reference).lower()
    betamin=min((-r['c']['beta']).lower() for r in reference).lower()
    Kmean=(1/(1+ellmin)).upper();Cq=(T*KD+KC).upper();Bq=(KD+qplus*Cq).upper()
    KG=(Bq+max(Cq,Kmean)).upper()
    HD=(1+(1+qplus)*T).upper();HC=(1+qplus).upper()
    # The rotational reference may retain the original genuine linear tail
    # while the current true exterior uses the newly installed long profile.
    # Compare both to the same q_*; never identify these two lines for free.
    q_comparison=(fee+arb(2)**-512).upper()
    if not q_comparison<arb(2)**-500:
        raise ValueError('the explicit old/current exterior multiplier comparison failed')
    Ld=(exact_arb(Fraction(5898255,10**12))+q_comparison).upper()
    L0=exact_arb(Fraction(7372818,10**13))
    bulk=(KG*actual_multiplication).upper()
    outer=(HD*Ld+L0).upper();chi=(bulk+outer).upper()
    AD=(1/(8*sd)).sqrt().upper();AC=(1/(8*sc)).sqrt().upper()
    B0=(1/(4*betamin)).sqrt().upper();C0=(1/(2*betamin*(1+ellmin))).sqrt().upper()
    FB=((1+qplus*T)*AD+B0+T*AD).upper()
    FC=((1+qplus*T)*qplus*AD+qplus*AC+T*qplus*AD+AC+C0).upper()
    divB=(HD/sd).upper();divC=(HD*qplus/sd+HC/sc).upper()
    # Divergence sources have mean zero. Ordinary sources retain both means.
    jumpB=max(HD,arb(1)).upper();jumpC=max(HD*qplus+HC,arb(1)).upper()
    passed=bool(inverse_pass and chi<1)
    bounds=dict(physical_inverse_displacement_Awidth=inversion_displacement,
        physical_inverse_contraction=inversion_lip,physical_theta_jacobian_lower=physical_jmin,
        physical_theta_jacobian_upper=physical_jmax,minimum_mean_abs=minimum_mean,
        complete_physical_Q_B_Awidth=DB,complete_physical_Q_C_Awidth=DC,
        actual_full_multiplication_norm=actual_multiplication,q_upper=qplus,
        D_rate_per_M=sd,C_rate_per_M=sc,triangular_coupling=T,K_D=KD,K_C=KC,
        mean_Q_kernel=Kmean,complete_module_Q_kernel=KG,
        inner_C_port=HC,outer_nonzero_d_port=HD,outer_Bmean_port=arb(1),outer_Cmean_port=arb(1),
        true_outer_DN_L2_derivative=Ld,true_outer_mean_derivative=L0,
        historical_to_current_outer_q_comparison=q_comparison,
        bulk_feedback=bulk,true_outer_feedback=outer,complete_feedback=chi,
        ordinary_L2rL2_B_source=FB,ordinary_L2rL2_C_source=FC,
        divergence_module_B_source=divB,divergence_module_C_source=divC,
        physical_B_jump_l1_source=jumpB,physical_C_jump_l1_source=jumpC)
    if passed:
        inverse=(1/(1-chi)).upper();bounds['full_resolvent']=inverse
        for k in ('inner_C_port','outer_nonzero_d_port','outer_Bmean_port','outer_Cmean_port',
                  'ordinary_L2rL2_B_source','ordinary_L2rL2_C_source',
                  'divergence_module_B_source','divergence_module_C_source',
                  'physical_B_jump_l1_source','physical_C_jump_l1_source'):
            bounds['closed_'+k]=(bounds[k]*inverse).upper()
    encoded=json.dumps(cover,sort_keys=True,separators=(',',':')).encode()
    report=dict(kind='actual_final_physical_cap_linear_module_v1',complete=passed,
        source_sha256=sha(__file__),candidate_sha256=sha(args.candidate),object_sha256=sha(args.object),
        cap_cache_sha256=sha(args.cap_cache),candidate_coordinate_identity=meta['coordinates'],
        exact_alpha=str(dyadic(meta['amplitude'])),exact_nu=meta['exact_float_nu'],
        exact_eta_center=cap['exact_center_parameter'],parameter_half_width=str(args.half_width),
        whole_original_eta=True,complete_primitive_tail=True,complete_unknown_Fourier_modes=True,
        exact_interval=[str(args.left),'25/8'],inverse_analytic_width=str(args.inverse_width),
        candidate_modes=modes,native_reference_rows=len(reference),complete_closed_intersections=len(cover),
        actual_closed_cover_sha256=hashlib.sha256(encoded).hexdigest(),closed_cover=cover,
        reference_rows=[dict(native_index=r['native_index'],interval=[str(r['left']),str(r['right'])],
            bounds={k:record(r[k]) for k in ('q_lower','q_upper','D_rate','C_rate','lower_face','upper_face','T','KD','KC')}) for r in reference],
        complete_coefficient_suprema=dict(Q_B_imaginary=[record(x) for x in qb],
            Q_C_real=[record(x) for x in qc],psi=[record(x) for x in psi],psi_phi=[record(x) for x in psip]),
        bounds={k:record(v) for k,v in bounds.items()},
        full_reference_modes='every physical M in 4N; no finite angular cutoff',
        state_norm='sum of the two l2_m(C_r) norms in physical theta, including both means',
        exact_Q_derivatives='Q_B=2u; Q_C=ell-u^2-Kv^2, composed with the actual inverse phi(theta)',
        unknown_is_physical_Codazzi_Jacobi=True,
        moving_residual_sensitive_operator_bridge_still_required=True,
        cap_internal_same_physical_angle_jump_sources_independent=True,
        actual_nonlinear_exterior_derivative_closed=passed,
        original_nonlinear_solution_exists=False,negative_return_inverse=False,
        complete_whole_body_inverse=False,
        source_and_theorem_sha256={
            str(Path(__file__).with_name(name)):sha(Path(__file__).with_name(name)) for name in (
                'fourfold_codazzi_current_positive_complete_coefficients.py',
                'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_rotational_cap_jacobi.py',
                'fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')},
        input_theorem_sha256={name:sha(Path('results')/name) for name in (
            'R133-supplement-full-Codazzi-source-contact-on-actual-cap.md',
            'R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md')},
        seconds=time.monotonic()-started)
    save(args.out,report)
    print(dict(complete=passed,intersections=len(cover),DB=DB.str(14),DC=DC.str(14),
        KG=KG.str(14),feedback=chi.str(14),seconds=report['seconds']),flush=True)


if __name__=='__main__':main()
