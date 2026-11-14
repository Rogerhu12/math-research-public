#!/usr/bin/env python3
"""Feed the new full base energy into actual higher/source/strong scattering.

The former density identity gains one angular order. Only its complete
zeroth-order height and density columns are replaced. Cauchy and ordinary
source costs are kept separate in the original full WKB residual identity.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked
from fourfold_negative_root_physical_graph_operator import mult
from fourfold_actual_relative_ray_real_jets import complete_comparisons
from fourfold_strict_windowed_density_R46 import frame


def up(v):return stored(v).upper()
def lo(v):return stored(v).lower()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--energy',type=Path,default=Path('notes/2026-11-13-R46-unshifted-half-density-energy.json'))
    p.add_argument('--jets',type=Path,default=Path('notes/2026-11-13-R106-full-relative-real-log-jets-refined.json.gz'))
    p.add_argument('--density',type=Path,default=Path('notes/2026-11-13-R46-complete-density-transport-bootstrap.json'))
    p.add_argument('--base',type=Path,default=Path('notes/2026-11-13-R46-strict-two-base-four-thirds.json'))
    p.add_argument('--root-cut',type=Path,default=Path('notes/2026-11-13-actual-root-cut-true-strong-rebudget.json'))
    p.add_argument('--scale',type=int,default=1048576)
    p.add_argument('--bits',type=int,default=384)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('fresh complete strict/scattering report required')
    ctx.prec=a.bits;tick=time.monotonic()
    e=checked(a.energy,'fourfold_strict_unshifted_half_density_energy.py')
    j=checked(a.jets,'fourfold_actual_relative_ray_log_jets_refine.py')
    d=checked(a.density,'fourfold_strict_density_transport_bootstrap.py')
    b=checked(a.base,'fourfold_strict_base_four_thirds.py')
    root=checked(a.root_cut,'fourfold_actual_root_cut_strong_rebudget.py')
    if any(z['identity']!=d['identity'] for z in (e,j,b,root)):
        raise ValueError('same original actual strict family required')
    if e['inputs'].get(str(a.density))!=sha(a.density):
        raise ValueError('new base energy has another original density realization')
    for row in (e,j,b,root):
        for path in set(row['inputs']).intersection(d['inputs']):
            if row['inputs'][path]!=d['inputs'][path]:raise ValueError('complete shared field differs')
    if not j['all_pairs_of_strict_times_and_both_directions'] or not j['entire_original_real_parameter_box']:
        raise ValueError('all true relative times and full parameters are needed')
    N=a.scale
    if N!=b['scale'] or N!=root['scale']:raise ValueError('same full comparison scale required')
    er=next(z for z in e['rows'] if z['scale']==N)
    dr=next(z for z in d['rows'] if z['scale']==N)
    H=[arb(0),up(j['accepted_relative_first_derivative'])]+[
        up(z['accepted_complete_relative_derivative']) for z in j['accepted_real_derivative_bounds']]
    if [z['order'] for z in j['accepted_real_derivative_bounds']]!=[2,3,4]:
        raise ValueError('the actual complete four real derivatives are required')
    _,D=complete_comparisons(N,H[1],H,1)
    fw=lo(d['field_strip']);Q=up(d['complete_integrated_kappa_modulus'])
    mp=up(e['bounds']['old_m_modulus']);rp=up(e['bounds']['old_sqrtmu_modulus'])
    # T was retained in the native frame proof; recover its separate complete
    # modulus from the original field input, never divide a product bound.
    fp=Path('notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz')
    f=checked(fp,'fourfold_strict_actual_wkb_fields.py')
    if d['inputs'].get(str(fp))!=sha(fp) or e['inputs'].get(str(fp))!=sha(fp):
        raise ValueError('same actual complete 215 native fields required')
    tp=max(up(z['complete_complex_field_moduli']['T']) for z in f['cells'])
    if len(f['cells'])!=215:raise ValueError('the full true closed cover is missing')
    cN=((1+arb(N)**-2).sqrt()/4).upper()
    meanC=up(er['old_density_base_mean_initial']);meanS=up(er['old_density_base_mean_source'])
    yC0=up(er['old_density_base_y_initial']);yS0=up(er['old_density_base_y_source'])
    Mm=mult(N,1,mp,fw);Mr=mult(N,1,rp,fw);Mt=mult(N,1,tp,fw)
    Mm2=mult(N,2,mp,fw);Mr2=mult(N,2,rp,fw);Kunit=mult(N,1,arb(1),fw)
    FY=((4*arb(N)*Mr2+Mm*(1+Mt*Mt).sqrt())/arb(2).sqrt()).upper()
    yC1=(D[1]*FY+D[1]*Kunit*Q*(meanC/arb(2).sqrt()+cN*yC0)).upper()
    yS1=(D[1]*Mm/arb(2).sqrt()+D[1]*Kunit*Q*(meanS/arb(2).sqrt()+cN*yS0)).upper()
    def physical(mean,y1,y0):
        u=Mm2*(mean+arb(2).sqrt()*cN*y1)
        p=arb(2).sqrt()*Mr*y1+Mt*Mm*(mean+arb(2).sqrt()*cN*y0)
        return (u*u+p*p).sqrt().upper()
    C15=physical(meanC,yC1,yC0);S15=physical(meanS,yS1,yS0)
    old15=next(z for z in dr['derivative_rows'] if z['half_integer']=='3/2')
    C15=min(C15,up(old15['full_physical_Cauchy'])).upper()
    S15=min(S15,up(old15['positive_ordinary_physical_source'])).upper()
    C05=up(er['full_physical_Cauchy_positive_half'])
    S05=up(er['full_physical_L1L2_source_to_positive_half'])
    # Negative source injection H_N^-1 -> P_N^-1/2 has norm one.
    # Its exact Cauchy bound is C05, so interpolate it with S05 for t=0.
    Szero=(C05*S05).sqrt().upper()
    def interpolate(t,positive_source=False):
        t=Fraction(t)
        if t==0:return Szero if positive_source else C05
        if not Fraction(1,2)<=t<=Fraction(3,2):raise ValueError('unpaid physical index')
        theta=t-Fraction(1,2)
        low=S05 if positive_source else C05;high=S15 if positive_source else C15
        return (low**exact_arb(1-theta)*high**exact_arb(theta)).upper()
    strong=[]
    for row in b['rows']:
        s=Fraction(row['input_order']);t=Fraction(row['output_order'])
        C=interpolate(t);S=interpolate(t,True)
        I=up(row['inverse_frame']);F=up(row['frame'])
        defect=up(row['complete_initial_defect']);residual=up(row['complete_residual'])
        correction=(I*(C*(defect+F)+S*residual)+1).upper()
        rest=(4*(2*up(row['full_cross_cone_and_mean_output'])+up(row['full_remaining_momentum'])
                 +up(row['full_Q'])*up(row['full_ordering']))).upper()
        total=(correction+rest).upper()
        strong.append(dict(input_order=str(s),output_order=str(t),
            full_physical_Cauchy=record(C),full_physical_ordinary_source=record(S),
            unchanged_full_initial_defect=record(defect),unchanged_complete_residual=record(residual),
            unchanged_full_frame=record(F),unchanged_full_inverse_frame=record(I),
            complete_source_and_mean_correction=record(correction),
            unchanged_complete_cross_mean_momentum_and_ordering=record(rest),
            full_strict_four_thirds=record(total),
            previous_full_strict_four_thirds=row['full_strict_four_thirds']))
    Cbase=up(e['best_complete_original_base_amplitude'])
    srcbase=min(up(z['same_full_original_L1_HNminus_half_source_to_L2_amplitude'])
                for z in e['rows'] if z['scale']<=N).upper()
    _,I1=frame(N,Fraction(1),mp,rp*rp,tp,fw)
    src1=(I1*interpolate(1,True)).upper()
    rt=root['bounds'];K=up(rt['root_to_physical_cut_window_two'])
    Rkp=up(rt['purified_root_cut_full_four_thirds'])
    model=up(rt['purified_root_cut_same_model_window_two'])
    W=up(rt['strict_same_model_window_two']);ik=up(rt['unchanged_reciprocal_true_flux_factor'])
    shared=(Rkp*Cbase*K+model*W*Rkp).upper()
    RT={row['input_order']:(ik*(shared+model*up(row['full_strict_four_thirds'])*K)).upper()
        for row in strong}
    RS=(3*max(RT.values())).upper()
    raw0={k:up(v) for k,v in root['full_negative_near_endpoint_raw_base_columns'].items()}
    raw1={k:up(v) for k,v in root['full_negative_near_endpoint_raw_HN1_columns'].items()}
    raw0['strict_core']=(up(rt['physical_cut_to_root_base'])*srcbase).upper()
    raw1['strict_core']=(up(rt['physical_cut_to_root_window_two'])*src1).upper()
    affine={k:(arb(2).sqrt()*v).upper() for k,v in raw0.items()}
    affine['negative_five_space_direct_sum']=(affine['strict_core']**2+
        2*affine['either_canonical_root']**2+2*affine['either_tilted_graph']**2).sqrt().upper()
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('both full physical first higher Cauchy and source constants improve',
         C15<up(old15['full_physical_Cauchy']) and S15<up(old15['positive_ordinary_physical_source']))
    gate('both actual complete strong windows improve',
         all(up(z['full_strict_four_thirds'])<up(z['previous_full_strict_four_thirds']) for z in strong))
    gate('the actual complete scattering error improves',RS<up(rt['complete_actual_strong_scattering_error_both_windows']))
    gate('the strict ordinary base and H1 raw columns improve',
         raw0['strict_core']<up(root['full_negative_near_endpoint_raw_base_columns']['strict_core'])
         and raw1['strict_core']<up(root['full_negative_near_endpoint_raw_HN1_columns']['strict_core']))
    out=dict(kind='actual_strict_half_density_bootstrap_and_complete_strong_scattering',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,identity=d['identity'],scale=N,
        actual_parameter_scope=root['actual_parameter_scope'],entire_original_real_parameter_box_for_local_estimates=True,
        inputs={str(p):sha(p) for p in (a.energy,a.jets,a.density,a.base,a.root_cut,fp)},
        native_cells_recomputed=0,all_original_215_closed_cells_and_550_true_relative_times_retained=True,
        exact_physical_interval=d['exact_physical_interval'],
        original_density_equations_and_first_phase_unchanged=True,
        complete_old_density_potential_retained_only_in_the_lower_order_bootstrap=True,
        source_and_Cauchy_costs_not_identified=True,
        strong_error_identity='I_t*(C_t*(initial_defect+mean_frame)+S_t*ordinary_residual)+1+all_original_cross_mean_momentum_ordering_terms',
        full_actual_scattering_identity='R_S=3 max_s kappa^-1*(R_Kp*C0*K2+M2*R_strict_s*K2+M2*W2*R_Kp)',
        bounds={k:record(v) for k,v in dict(
            physical_Cauchy_half=C05,physical_ordinary_source_half=S05,
            complete_density_transport_order_one=D[1],full_angular_antiderivative_gain=cN,
            full_integrated_density_potential=Q,complete_old_density_initial_order_one=FY,
            complete_density_homogeneous_order_one=yC1,complete_density_ordinary_source_order_one=yS1,
            physical_Cauchy_three_halves=C15,physical_ordinary_source_three_halves=S15,
            physical_ordinary_source_zero=Szero,
            complete_original_base_amplitude_Cauchy=Cbase,
            strict_complete_L1_HNminus_half_to_base_amplitude=srcbase,
            strict_complete_L1_HNhalf_to_HN1_amplitude=src1,
            complete_negative_transfer_error_forward=RT['0'],complete_negative_transfer_error_opposite=RT['-4/3'],
            complete_actual_strong_scattering_error_both_windows=RS).items()},
        strict_strong_rows=strong,
        full_negative_near_endpoint_raw_base_columns={k:record(v) for k,v in raw0.items()},
        full_negative_near_endpoint_raw_HN1_columns={k:record(v) for k,v in raw1.items()},
        full_negative_original_affine_base_columns={k:record(v) for k,v in affine.items()},
        complete_base_physical_source_units=root['complete_base_physical_source_units'],
        complete_stronger_physical_source_units=root['complete_stronger_physical_source_units'],
        source_partition=root['source_partition'],exact_source_reflection=root['exact_source_reflection'],
        original_mean_matrices_both_regular_ports_and_every_head_path_retained=True,
        exact_actual_scattering_is_still_onto_unitary=True,
        full_returned_Rstar_recomputed=False,finite_head_inverse_proved=False,full_feedback_inverse_proved=False,
        new_nu_body_or_deep_tail_transfer_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py','fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_negative_root_physical_graph_operator.py','fourfold_actual_relative_ray_real_jets.py',
            'fourfold_strict_windowed_density_R46.py')},gates=gates,seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,physical_C15=C15.str(12),physical_S15=S15.str(12),
        Rstrict=[z['full_strict_four_thirds']['ball'] for z in strong],RS=RS.str(12),
        core_raw0=raw0['strict_core'].str(12),core_raw1=raw1['strict_core'].str(12),
        out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
