#!/usr/bin/env python3
"""Transfer the complete regular Hs graph to the exact repaired M32 endpoint.

The already proved fixed-physical-angle cap change and exact 65 right
offsets are consumed. No original endpoint field, cap matrix, nonlinear
long solve, or target primitive is recomputed. All mean, head and affine
outer columns remain present in the new exact-reference certificate.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

ORIGINAL='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
REPAIR_NATIVE='6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc'
CAP_BACKGROUND='35db98d4124d50ef3bd69f3ec3aa6906289e3f6083c3ba91c8197da7547830ff'
OUTER_NATIVE='b62e06091e0d46198b80f0442da3627fe0ea79d23500bf823a9a96ee2f95e117'
OUTER_SOURCE='b0a276bc9453c8ea67103f0cf05a1ab7cdfe62f7b2772bfba6b27697d73a3185'
CAP_SOURCE='a24c26c793e01ad0b8e686786d0b7c1f9d3f5c6de0af00a8cb0283f2369478be'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data=Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if data[:2]==b'\x1f\x8b' else data)


def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    data=(json.dumps(doc,ensure_ascii=False,separators=(',',':'))+'\n').encode()
    if path.suffix=='.gz':data=gzip.compress(data,mtime=0)
    temporary=path.with_suffix(path.suffix+'.partial');temporary.write_bytes(data);temporary.replace(path)


def exact(value):
    value=Fraction(value);return arb(value.numerator)/value.denominator


def interval(value):return arb(value['lower']).lower().union(arb(value['upper']).upper())


def record(value):
    value=arb(value)
    if not value.is_finite():raise ArithmeticError('a repaired complete regular port is nonfinite')
    return dict(ball=value.str(80),lower=value.lower().str(80),upper=value.upper().str(80))


def nonnegative(value):
    value=arb(value).upper()
    if not value>=0 or not value.is_finite():raise ValueError('invalid complete outer coefficient upper bound')
    return value


def nonlinear_row(z,b):
    eps=exact(Fraction(1,2**512))
    rf=10*(z+b);F=rf+b;kap=36*4096*F
    if not kap<1:raise ValueError('the genuine complete long graph contraction is lost')
    jf=9/(1-kap);jb=(eps+kap)/(1-kap)
    return dict(rf=rf,F=F,kap=kap,jf=jf,jb=jb,
        T=eps+4*16384*F*jf,C=4*2048*F*jf,
        U=eps+4*16384*F*(1+jb),V=4*2048*F*(1+jb),
        image=9*z+eps*b+9*4096*F*F)


def run(a,doc):
    def gate(name,ok,**data):
        doc['gates'].append(dict(name=name,passed=bool(ok),**data))
        if not ok:raise ValueError('repaired complete outer gate failed: '+name)
    repair,cap,old=read(a.repair),read(a.cap_background),read(a.old_outer)
    gate('exact_original_repair_physical_cap_and_complete_Hs_native_bytes',
        sha(a.repair)==REPAIR_NATIVE and sha(a.cap_background)==CAP_BACKGROUND
        and sha(a.old_outer)==OUTER_NATIVE
        and sha(Path(__file__).with_name('fourfold_codazzi_final_regular_Hs_Riccati.mjs'))==OUTER_SOURCE
        and sha(Path(__file__).with_name('fourfold_codazzi_continuous_cap_residual_conjugation.py'))==CAP_SOURCE)
    gate('complete_exact_M32_repair_and_all65_right_offsets',
        repair.get('complete') and repair.get('candidate_sha256')==ORIGINAL
        and repair.get('derived_definition_sha256')==REPAIR
        and repair.get('exact_interface_count')==6143
        and repair.get('corrected_value_and_all_angular_derivatives_continuous')
        and repair['definition']['modes']==32
        and repair['definition']['offsets_independent_of_eta_and_nu']
        and len(repair.get('exact_right_physical_offset',[]))==65
        and len(repair.get('gates',[]))==6 and all(x['passed'] for x in repair['gates']))
    gate('actual_fixed_physical_angle_change_includes_infinite_tail_and_mean',
        cap.get('complete') and cap.get('source_sha256')==CAP_SOURCE
        and cap.get('original_candidate_sha256')==ORIGINAL
        and cap.get('derived_definition_sha256')==REPAIR
        and cap.get('repair_input_sha256')==REPAIR_NATIVE
        and cap.get('real_continuous_repaired_centre')
        and cap.get('unknown_Fourier_tail_truncated') is False
        and cap.get('bare_composition_minus_identity_used') is False
        and cap.get('whole_original_eta_for_background_transfer')
        and cap.get('background_parameter_half_width')=='1/1000000000'
        and len(cap.get('gates',[]))==6 and all(x['passed'] for x in cap['gates']))
    gate('same_original_complete_nonlinear_Hs_graph_and_all33_gates',
        old.get('complete') and old.get('candidate_sha256')==ORIGINAL
        and len(old.get('gates',[]))==33 and all(x['passed'] for x in old['gates'])
        and old['permissions']['full_nonlinear_DN_derivative_Hs']
        and old['permissions']['all_0_to_1_orders_by_interpolation'])
    offsets=list(map(Fraction,repair['exact_right_physical_offset']))
    mean_e=exact(abs(offsets[32]))
    gate('same_exact_independent_right_mean',offsets[32]==Fraction(repair['exact_right_mean_offset']))
    sigma=exact(Fraction(1,8))
    eu=sum((exact(abs(offsets[j-1]))*(4*j*sigma).exp() for j in range(1,33)),arb(0)).upper()
    ev=sum((exact(abs(offsets[32+j]))*(4*j*sigma).exp() for j in range(1,33)),arb(0)).upper()
    old_mlo=exact('5.84461145233');old_mhi=arb(7)
    mlo=(old_mlo-mean_e).lower();mhi=(old_mhi+mean_e).upper()
    gate('repaired_endpoint_mean_and_true_Riccati_terminal_invariant',
        mlo>exact('5.8') and (1-exact(Fraction(1,2*800000**2)))/mhi>exact(Fraction(1,8))
        and 1/mlo<exact(Fraction(1,5)))
    Us0=exact('0.000000001643190');Vs0=exact('0.000000009603792');P0=exact('0.00000000001480385')
    psi_change=((ev+mean_e*Vs0/old_mlo)/(4*mlo)).upper()
    Us=(Us0+eu).upper();Vs=(Vs0+ev).upper();P=(P0+psi_change).upper()
    dC=nonnegative(interval(cap['bounds']['outer_full_C_change_A_1over64']))
    Z=nonnegative(interval(cap['bounds']['corrected_outer_Z_A0']))
    Z1=(exact(old['background']['Z_phi_A0'])+64*dC).upper()
    gate('complete_repaired_physical_Z_and_its_derivative_include_all_modes',
        Z<exact(Fraction(1,10**12)) and dC>=0 and Z1>0)
    eps=exact(Fraction(1,2**512));rb=exact(Fraction(1,2**60));B1=16*rb
    rZw=exact(old['background']['wider_Z_radius']);rBw=exact(old['background']['wider_fB_radius'])
    rhoZ=exact(old['background']['Cauchy_Z_radius']);rhoB=exact(old['background']['Cauchy_fB_radius'])
    gate('repaired_input_inside_the_same_genuine_complete_complex_domains',
        Z+rhoZ<rZw and rb+rhoB<rBw)
    wide=nonlinear_row(rZw,rBw);small=nonlinear_row(exact(Fraction(1,10**12)),rb)
    gate('same_complete_wide_long_fixed_point_and_holonomy_small_root',
        2*wide['F']<exact(Fraction(1,2**25)) and 6*wide['F']<exact(Fraction(1,2**20))
        and wide['kap']<exact(Fraction(1,1000)) and wide['image']<wide['rf'])
    Xi=(Z1/rhoZ+B1/rhoB).upper()
    T1=(small['T']+Xi*wide['T']).upper();U1=(small['U']+Xi*wide['U']).upper()
    dn={name:exact(old['actual_DN'][name]) for name in (
        'Z_to_d_L2','Z_to_d_H1','Z_to_d_Hone_sixth',
        'fB_to_d_L2','fB_to_d_H1','fB_to_d_Hone_sixth','Z_to_mean','fB_to_mean')}
    gate('repaired_complete_nonlinear_L2_DN_and_independent_mean_columns',
        small['T']<dn['Z_to_d_L2'] and small['C']<dn['Z_to_mean']
        and small['U']<dn['fB_to_d_L2'] and small['V']<dn['fB_to_mean'])
    gate('repaired_translation_commutator_pays_full_H1_DN',
        T1<dn['Z_to_d_H1'] and U1<dn['fB_to_d_H1'])
    gate('same_operator_complete_Hone_sixth_interpolation',
        dn['Z_to_d_L2']**5*dn['Z_to_d_H1']<dn['Z_to_d_Hone_sixth']**6
        and dn['fB_to_d_L2']**5*dn['fB_to_d_H1']<dn['fB_to_d_Hone_sixth']**6)
    qmin=exact('0.9999999999993')
    gate('complete_physical_curvature_graph_inverses',
        1/(qmin-dn['Z_to_d_H1'])<exact('1.000251')
        and 1/(qmin-dn['Z_to_d_Hone_sixth'])<exact('1.0000112'))
    e1=(P/sigma).upper();e2=(2*P/(4*sigma*sigma)).upper();e3=(6*P/(16*sigma**3)).upper()
    gate('actual_repaired_angle_orientation',e1<exact(Fraction(1,4)))
    pi_upper=exact(Fraction(22,7))
    K0=(e2/(1-e1)+(1+pi_upper)*e1).upper()
    K1=(e3/(3*(1-e1))+e2*e2/(2*(1-e1)**2)+(2+pi_upper)*e1+e1*e1).upper()
    Kh=(K0+4*K1).upper();comp=(1/(1-e1)).upper()
    gate('complete_Hilbert_conjugation_without_same_order_composition_subtraction',Kh<1)
    mg=exact('5.8');uA=(9*Us).upper();wA=(9*Vs).upper()
    uphi=(136*Us).upper();vphi=(136*Vs).upper();vA=(mhi+wA).upper()
    gate('complete_repaired_Bone_multiplier_and_reciprocal_gap',mlo-wA>mg)
    C0=dn['Z_to_mean'];T1p=dn['Z_to_d_H1'];Tsix=dn['Z_to_d_Hone_sixth'];Usix=dn['fB_to_d_Hone_sixth']
    f1=comp*(1+T1p);g1=comp*(1+C0)
    a1=vA*f1+vA*(uA+uphi/4)*g1
    a2=(vA*vA+vphi*vA/4)*g1
    gate('actual_full_Hs_moving_graph_lift_on_all_0_to_1_orders',a1*a1+a2*a2<2500)
    chi=(1+vA/mg)/(4*mg)
    recovery=(comp*(1+vphi*chi)/(mg*mg)).upper()
    gate('actual_complete_Hs_physical_recovery',recovery<exact(Fraction(3,100)))
    E2=(wA*(2*mhi+wA)+vphi*vA/4)*g1
    lead_inverse=comp*(1+e1)/(mg*mg)
    chart_inverse=(lead_inverse/(1-lead_inverse*E2)).upper()
    gate('complete_nonmean_even_chart_is_onto_and_includes_true_mean_output',
        lead_inverse*E2<exact(Fraction(1,10**6)) and chart_inverse<exact(Fraction(3,100)))
    mean_map=(mhi*mhi*C0*exact(Fraction(3,100))).upper()
    gate('independent_repaired_moving_mean_not_deleted',mean_map<exact('0.000001084'))
    def row_defect(T):
        f=comp*(1+T);g=comp*(1+C0)
        leading=mhi*(comp*(T+eps+C0)+Kh*f)
        error=wA*f+(vA*(uA+uphi/4)+(wA*(2*mhi+wA)+vphi*vA/4)/mg)*g
        return ((leading+error)*exact(Fraction(3,100))).upper()
    defect1=row_defect(T1p);defect6=row_defect(Tsix)
    gate('complete_repaired_H1_and_Hone_sixth_Robin_rows',
        defect1<exact('0.000053') and defect6<exact('0.0000026'))
    # Use the same explicitly widened rational budget only after proving
    # the new exact-input bound. No old numerical permission is inherited.
    E6=exact('0.0000026');feedback=(exact(Fraction(17,2))*E6).upper()
    reflection=(feedback/(1-feedback)).upper()
    gate('actual_complete_repaired_high_outer_Riccati_graph',reflection<exact('0.0000222'))
    head=(9*E6/(1-feedback)).upper()
    gate('all_low96_to_high_outer_columns_retained',
        arb(385)<arb(3)**6 and head<exact('0.0000235'))
    B2=vA*vA+vphi*vA/4
    affine_mean=vA*(uA+uphi/4)+B2/mg+E6*B2
    affine_B=vA*comp
    affine_f=affine_B*Usix+affine_mean*dn['fB_to_mean']
    afactor=3/(1-feedback)
    fB_port=(afactor*affine_f).upper();Robin_port=(afactor*affine_B).upper()
    mean_port=(afactor*affine_mean).upper()
    gate('independent_outer_height_Robin_and_mean_source_columns',
        fB_port<exact('0.000030') and Robin_port<22 and mean_port<26)
    mean_affine=(mhi*mhi*(1+C0*exact(Fraction(3,100))*B2)).upper()
    gate('complete_affine_mean_and_height_to_mean_outputs',
        mean_affine<50 and mean_affine*dn['fB_to_mean']<exact('0.0000041'))
    bounds=dict(right_eu_Aone_eighth=eu,right_ev_nonmean_Aone_eighth=ev,right_mean_change=mean_e,
        corrected_endpoint_mean_absolute_lower=mlo,corrected_endpoint_mean_absolute_upper=mhi,
        corrected_outer_physical_Z_A0=Z,corrected_outer_physical_Z_theta_A0=Z1,
        actual_fixed_physical_C_change_Aone_sixtyfourth=dC,actual_angle_change_Aone_eighth=psi_change,
        corrected_moving_U_Aone_eighth=Us,corrected_moving_Vnonmean_Aone_eighth=Vs,
        corrected_angle_displacement_Aone_eighth=P,actual_translation_Cauchy_size=Xi,
        complete_Hilbert_conjugation_Hs=Kh,complete_angle_composition_Hs=comp,
        actual_complete_Z_DN_H1=T1,actual_complete_fB_DN_H1=U1,
        complete_moving_Hs_recovery=recovery,complete_even_nonmean_chart_inverse=chart_inverse,
        true_moving_mean_rank=mean_map,complete_Robin_H1=defect1,complete_Robin_Hone_sixth=defect6,
        complete_high_outer_feedback=reflection,complete_low_to_high_outer_source=head,
        independent_fB_outer_source=fB_port,ordinary_Robin_outer_source=Robin_port,
        independent_mean_outer_source=mean_port,independent_mean_to_mean=mean_affine,
        independent_fB_to_mean=(mean_affine*dn['fB_to_mean']).upper(),
        actual_reference_outer_p_lower=((1-exact(Fraction(1,2*800000**2)))/mhi).lower(),
        actual_reference_outer_p_upper=(1/mlo).upper())
    doc.update(complete=True,original_candidate_sha256=ORIGINAL,derived_definition_sha256=REPAIR,
        exact_affine_parameter_offset='0',whole_original_eta_claimed=False,
        physical_parameter='fixed original physical eta0 and nu',
        bounds={name:record(value) for name,value in bounds.items()},
        actual_DN={name:record(value) for name,value in dn.items()},
        exact_reference=dict(outer_backward_equals_actual_q_over_repaired_mean=True,
            p_final='q_star/(-m_repaired(R)), frequency independent',
            g_final='the genuine forward solution from r_star; arbitrary positive value allowed here',
            p_terminal_invariant=['1/8','1/5']),
        full_Hone_sixth_Riccati_graph_proved=True,full_nonlinear_DN_Hs_derivative_proved=True,
        independent_even_mean_and_all_head_and_affine_outer_columns_retained=True,
        all_fourier_modes_including_infinite_physical_tail_retained=True,
        physical_H7_over6_nonlinear_exterior_graph_claimed=False,
        unknown_Fourier_correction_assigned_M32_band=False,
        no_original_endpoint_or_cap_matrix_or_target_recomputation=True,
        complete_positive_body_inverse_proved=False,complete_infinite_BVP_inverse_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('repair','cap-background','old-outer','out'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every complete or failed repaired outer graph attempt')
    document=dict(kind='actual_exact_M32_repair_complete_Hs_regular_and_Riccati_outer_graph_v1',
        complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in ('repair','cap-background','old-outer')})
    try:run(a,document)
    except BaseException as error:
        document['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:document['seconds']=time.monotonic()-started;save(a.out,document)
    print(json.dumps(dict(complete=True,gates=len(document['gates']),seconds=document['seconds'],
        complete_high_outer_feedback=document['bounds']['complete_high_outer_feedback']['upper'])),flush=True)


if __name__=='__main__':main()
