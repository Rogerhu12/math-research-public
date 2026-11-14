#!/usr/bin/env python3
"""Complete physical regular outer graph for the whole real Q0+delta*Z family.

Consume the completed exact193 endpoint and original full nonlinear graph.
Only new directed scalar transfer budgets are evaluated. No old target,
response, cap matrix or nonlinear exterior solve is rerun.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,sys,time
from fractions import Fraction
from pathlib import Path
import flint
from flint import arb,ctx

PUBLIC='Rogerhu12/math-research-public'
ORIGINAL='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR='440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
DIRECTION='6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04'
OUTER_NATIVE='b62e06091e0d46198b80f0442da3627fe0ea79d23500bf823a9a96ee2f95e117'
BASE_OUTER='75e7c0e1447306a97971ee05dcb68b8d357cb4fffa5c1a37335a6fc29a473424'
BASE_SOURCE='5d1e8a86aa268d4d98bc929264d706b418b88cb99518ca646d84258d3068ffbe'
ENDPOINT='8f6019cefaa96da64eadb3b19a98110dc81a0d5760a091e6fdffe538c971e606'
ENDPOINT_SOURCE='0e8904d935d83596040fede599ca60cbe7acdf5aba5249c8ddaa4ec3167a976f'

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
        if not ok:raise ValueError('whole real delta outer gate failed: '+name)
    old,base,endpoint=read(a.old_outer),read(a.repaired_outer),read(a.endpoint)
    gate('exact_original_complete_nonlinear_repaired_outer_and_full193_endpoint_bytes',
        sha(a.old_outer)==OUTER_NATIVE and sha(a.repaired_outer)==BASE_OUTER
        and sha(a.endpoint)==ENDPOINT
        and sha(Path(__file__).with_name('fourfold_codazzi_repaired_regular_Hs_outer.py'))==BASE_SOURCE
        and sha(Path(__file__).with_name('fourfold_codazzi_exact_right_Z_endpoint.py'))==ENDPOINT_SOURCE)
    gate('same_complete_original_nonlinear_graph_and_all33_gates',
        old.get('complete') and old.get('candidate_sha256')==ORIGINAL
        and len(old.get('gates',[]))==33 and all(x['passed'] for x in old['gates'])
        and old['permissions']['full_nonlinear_DN_derivative_Hs']
        and old['permissions']['all_0_to_1_orders_by_interpolation'])
    gate('same_complete_repaired_outer_with_all25_gates_and_true_mean',
        base.get('complete') and not base.get('failure')
        and base.get('source_sha256')==BASE_SOURCE
        and base.get('original_candidate_sha256')==ORIGINAL
        and base.get('derived_definition_sha256')==REPAIR
        and len(base.get('gates',[]))==25 and all(x['passed'] for x in base['gates'])
        and base.get('all_fourier_modes_including_infinite_physical_tail_retained')
        and base.get('independent_even_mean_and_all_head_and_affine_outer_columns_retained'))
    gate('same_actual_unscaled_full193_continuous_direction_and_all14_endpoint_gates',
        endpoint.get('complete') and not endpoint.get('failure')
        and endpoint.get('source_sha256')==ENDPOINT_SOURCE
        and endpoint.get('explicit_direction_definition_sha256')==DIRECTION
        and endpoint.get('original_complete_outer_native_sha256')==BASE_OUTER
        and endpoint.get('complete_mean_retained') and endpoint.get('physical_direction_unscaled_by_alpha')
        and len(endpoint.get('gates',[]))==14 and all(x['passed'] for x in endpoint['gates']))
    radius=Fraction(1,100000000);r=exact(radius)
    diagnostics=endpoint['complete_parameter_radius_diagnostics']
    selected=[x for x in diagnostics if Fraction(x['exact_parameter_radius'])==radius]
    if len(selected)!=1:raise ValueError('the whole real radius is absent from the original endpoint')
    diag=selected[0];w8=diag['width_budgets']['1/8'];w32=diag['width_budgets']['1/32']
    up=lambda x:nonnegative(interval(x))
    b0=base['bounds']
    mlo=interval(diag['true_mean_abs_lower']).lower()
    mhi=interval(diag['true_mean_abs_upper']).upper()
    eu=up(w8['delta_u_A0']);ev=up(w8['delta_v_nonmean_A0'])
    mean_e=up(w8['delta_mean_abs']);psi_change=up(w8['delta_angle_A0'])
    Us=up(w8['updated_moving_u_A0']);Vs=up(w8['updated_moving_v_nonmean_A0'])
    P=up(w8['updated_angle_A0']);sigma=exact(Fraction(1,8))
    gate('whole_real_parameter_ball_keeps_the_true_frequency_independent_terminal_invariant',
        mlo>exact('5.8') and (1-exact(Fraction(1,2*800000**2)))/mhi>exact(Fraction(1,8))
        and 1/mlo<exact(Fraction(1,5)))
    # Along every real homotopy from 0 to delta, the old A1/8 bound
    # gives the A1/32 first derivative with fee 16 > 32/3.
    V32=up(w32['updated_moving_v_nonmean_A0'])
    Vphi32=(16*up(b0['corrected_moving_Vnonmean_Aone_eighth'])
        +r*up(endpoint['norms']['1/32']['1']['v_nonmean'])).upper()
    w=(V32/mlo).upper();w1=(Vphi32/mlo).upper()
    psi_inverse=(up(w32['updated_angle_A0'])/(1-w)).upper()
    gate('complete_actual_inverse_angle_on_the_entire_homotopy_and_true_strip_margin',
        w<exact(Fraction(1,4)) and psi_inverse<exact(Fraction(1,64)))
    C=(1/(mlo*(1-w))).upper()
    C1=(w1/(mlo*(1-w)**3)).upper()
    eC=(r*up(endpoint['norms']['1/32']['0']['v_including_mean'])).upper()
    dC=((C*C+C1*C/4)*eC).upper()
    delta_Cmean=(mean_e/(interval(b0['corrected_endpoint_mean_absolute_lower']).lower()*mlo)).upper()
    Z=(up(b0['corrected_outer_physical_Z_A0'])+dC).upper()
    Z1=(up(b0['corrected_outer_physical_Z_theta_A0'])+64*dC).upper()
    gate('fixed_physical_angle_C_difference_retains_full_infinite_tail_and_exact_mean',
        C>0 and C1>=0 and dC>=0 and delta_Cmean>=0
        and Z<exact(Fraction(1,10**12)) and Z1>0)
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
    bounds.update(whole_real_delta_radius=r,whole_homotopy_Vnonmean_Aone_thirtysecond=V32,
        whole_homotopy_Vphi_Aone_thirtysecond=Vphi32,
        actual_inverse_angle_displacement_Aone_sixtyfourth=psi_inverse,
        whole_homotopy_physical_C_Aone_sixtyfourth=C,
        whole_homotopy_physical_Ctheta_Aone_sixtyfourth=C1,
        exact_physical_mean_change_bound=delta_Cmean,
        additional_full_physical_C_change_Aone_sixtyfourth=dC)
    doc.update(complete=True,original_candidate_sha256=ORIGINAL,
        derived_definition_sha256=REPAIR,explicit_direction_definition_sha256=DIRECTION,
        exact_real_delta_radius=str(radius),full_family='Q_delta=Q0+delta*Z',
        fixed_intrinsic_affine_offset='0',whole_original_eta_claimed=False,
        physical_parameter='fixed original physical eta0 and nu; full real delta family',
        bounds={name:record(value) for name,value in bounds.items()},
        actual_DN={name:record(value) for name,value in dn.items()},
        exact_reference=dict(outer_backward_equals_actual_q_over_delta_mean=True,
            p_final='q_star/(-m_delta(R)), frequency independent',
            g_final='the genuine forward solution from r_star; arbitrary positive value allowed here',
            p_terminal_invariant=['1/8','1/5']),
        full_Hone_sixth_Riccati_graph_proved=True,full_nonlinear_DN_Hs_derivative_proved=True,
        independent_even_mean_and_all_head_and_affine_outer_columns_retained=True,
        all_fourier_modes_including_infinite_physical_tail_retained=True,
        full_real_delta_outer_graph_proved=True,physical_H7_over6_nonlinear_exterior_graph_claimed=False,
        unknown_Fourier_correction_assigned_M96_band=False,
        no_original_endpoint_or_cap_matrix_or_target_recomputation=True,
        original_complete_endpoint_native_sha256=ENDPOINT,
        original_complete_repaired_outer_native_sha256=BASE_OUTER,
        complete_positive_body_inverse_proved=False,complete_infinite_BVP_inverse_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('old-outer','repaired-outer','endpoint','out'):
        p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!=PUBLIC:
        raise RuntimeError('all new mathematics must execute in the public repository Actions')
    if '.'.join(map(str,sys.version_info[:3]))!='3.12.14' or flint.__version__!='0.9.0':
        raise RuntimeError('the pinned directed arithmetic runtime changed')
    ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if a.out.exists():raise FileExistsError('preserve every actual full delta outer outcome')
    doc=dict(kind='actual_full_real_delta_complete_Hs_and_Riccati_outer_graph_v1',
        complete=False,failure=None,gates=[],source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(a,name.replace('-','_'))) for name in ('old-outer','repaired-outer','endpoint')},
        all_original_completed_computations_recomputed=0)
    try:run(a,doc)
    except BaseException as error:
        doc['failure']=dict(type=type(error).__name__,message=str(error));raise
    finally:doc['seconds']=time.monotonic()-started;save(a.out,doc)
    print(json.dumps(dict(complete=True,gates=len(doc['gates']),seconds=doc['seconds'],
        complete_high_outer_feedback=doc['bounds']['complete_high_outer_feedback']['upper'])),flush=True)


if __name__=='__main__':main()
