#!/usr/bin/env python3
"""Full actual positive-cap contact and original-frame two-sided 4/3 remainder.

Consumes the same exact two-sided canonical chart, new complete grounded
density first jets, and the old full uncompressed cap/Robin realization.
All root modes, regular mean and contact, complete Ai cutoff and sources are
retained. The result is an L2 two-sided smoothing statement, not a paid full
high-Sobolev or weighted returned inverse.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--chart',type=Path,default=Path('notes/2026-11-13-root-twosided-canonical-domain.json'))
    p.add_argument('--density-jets',type=Path,default=Path('notes/2026-11-13-root-full-grounded-density-first-jets.json.gz'))
    p.add_argument('--potential',type=Path,default=Path('notes/2026-11-13-negative-root-complete-potential-density.json'))
    p.add_argument('--whole-cap',type=Path,default=Path('notes/2026-11-12-actual-full-weak-source-budget.json'))
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('new full-cap/Airy report required')
    ctx.prec=a.bits;tick=time.monotonic()
    chart=checked(a.chart,'fourfold_root_twosided_canonical_domain.py')
    jets=checked(a.density_jets,'fourfold_root_full_grounded_density_first_jets.py')
    pot=checked(a.potential,'fourfold_negative_root_complete_potential_density.py')
    whole=read(a.whole_cap)
    if (not whole['proved'] or whole['source_sha256']!=sha(Path(__file__).with_name('fourfold_phase_full_weak_source_budget.py'))):
        raise ValueError('the original proved full-cap realization changed')
    for name,h in whole['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=h:raise ValueError('full-cap dependency changed '+name)
    for name,h in whole['input_sha256'].items():
        if sha(name)!=h:raise ValueError('full-cap input changed '+name)
    for name in ('object','root_certificate'):
        if sha(jets[name+'_path'])!=jets[name+'_sha256']:
            raise ValueError('complete native density input changed '+name)
    if sha(pot['input_path'])!=pot['input_sha256']:
        raise ValueError('complete true seven-field input changed')
    for key in ('center_object_sha256','origin_inputs_sha256','direction_sha256',
                'exact_center_parameter','exact_parameter_interval'):
        if not chart['identity'][key]==jets['identity'][key]==pot['identity'][key]:
            raise ValueError('actual whole family differs '+key)
    for key in ('origin_inputs_sha256','direction_sha256'):
        if whole[key]!=chart['identity'][key]:raise ValueError('whole-cap origin or direction differs')
    lo,hi=map(Fraction,chart['identity']['exact_parameter_interval'])
    wlo,whi=map(Fraction,whole['exact_parameter_interval'])
    if not wlo<=lo<hi<=whi:raise ValueError('whole cap does not contain the actual full parameter box')
    R=exact_arb(Fraction(pot['rho_radius']))
    S1=exact_arb(Fraction(pot['physical_characteristic_start_strip']))
    H=exact_arb(Fraction(chart['canonical_real_half_height']))
    sigma=exact_arb(Fraction(chart['canonical_complex_angle_strip']))
    M={k:stored(v).upper() for k,v in pot['complete_moduli'].items()}
    C,Q,e=M['C'],M['q'],M['Delta_minus_one'];CR=C*R
    J={k:stored(v).upper() for k,v in jets['complete_moduli'].items()}
    inv={k:stored(v).upper() for k,v in chart['inverse_path_bounds'].items()}
    Delta_theta=(2*e/S1).upper()
    Delta_rho=(3*C*CR.exp()+Q*Delta_theta).upper()
    Lrho=(J['log_Ucal_rho']/2+Delta_rho/(3*(1-e))).upper()
    Ltheta=(J['log_Ucal_theta']/2+Delta_theta/(3*(1-e))).upper()
    Ly=(Lrho*inv['inverse_rho_xi']+Ltheta*inv['inverse_theta_xi']).upper()
    Lphi=(Lrho*inv['inverse_rho_phi']+Ltheta*inv['inverse_theta_phi']).upper()
    G=((Ly*Ly+H*Lphi*Lphi).sqrt()/2).upper()
    absorb=(1-G*H).lower()
    Ereg=stored(whole['constants']['regular_mean_extension_energy']).upper()
    Egrad=max((1/H).upper(),arb(13)/12)
    Eall=(Egrad.sqrt()+G*(H/3).sqrt())**2
    qlo=stored(chart['actual_quarter_circle_frequency'][0]).lower()
    qhi=stored(chart['actual_quarter_circle_frequency'][1]).upper()
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('complete canonical chart and native density cover the same physical bidisk',
         Fraction(pot['rho_radius'])<=Fraction(jets['rho_radius']) and
         Fraction(pot['physical_characteristic_start_strip'])<=Fraction(jets['physical_angle_strip']))
    gate('the same full positive canonical collar is present',H>0 and sigma>0 and all(g['passed'] for g in chart['gates']))
    gate('the complete canonical height gradient is absorbable on this collar',absorb>arb(9)/10)
    gate('the true full cap includes regular mean and nonnegative infinite-tail Robin',Ereg>0 and wlo<=lo<hi<=whi)
    gate('actual quarter-circle physical frequency retained',qlo>4 and qhi>=qlo)
    def contact(E,mu):
        Ta=(E.sqrt()+G*(2*H).sqrt()*mu)/absorb
        Tr=Ereg.sqrt()/absorb
        Cw=(Ta*Ta+Tr*Tr).sqrt()
        Cs=((4+H*H)*Cw*Cw+4+2*H).sqrt()
        return {k:record(v.upper()) for k,v in dict(
            root_extension_energy=E,root_L2_trace_factor=mu,
            root_gradient=Ta,regular_gradient=Tr,full_weak_contact=Cw,
            full_ordinary_contact=Cs).items()}
    all_contact=contact(Eall,arb(1))
    high=[]
    for N in (0,64,256,65536,1048576):
        freq=qlo*(N+1)
        d=max(arb(1),(1/(H*freq**(arb(2)/3))).upper())
        EN=((d+arb(1)/12).sqrt()+G/(arb(3).sqrt()*freq**(arb(2)/3)))**2
        mu=(1+freq*freq)**(-arb(1)/6)
        high.append(dict(actual_quarter_mode_cutoff=N,actual_frequency_lower=record(freq),**contact(EN,mu)))
    Cs=stored(all_contact['full_ordinary_contact']).upper()
    Cw=stored(all_contact['full_weak_contact']).upper()
    V=stored(chart['complete_potential_modulus']).upper()
    Vphi=(V/sigma).upper()
    Vmult=(V**(arb(1)/3)*(V+Vphi)**(arb(2)/3)).upper()
    ai0=1/(arb(3)**(arb(2)/3)*(arb(2)/3).gamma())
    aip=1/(arb(3)**(arb(1)/3)*(arb(1)/3).gamma())
    cA=aip/ai0;c=1/cA.sqrt();pi=arb.pi()
    # Whole positive-axis L2 Ai identity: integral Ai(z)^2 dz=Ai'(0)^2.
    ratio=(1+qlo**(-2))**(arb(1)/3)
    potential_source=(2*c*ratio*Vmult*aip).upper()
    # C2 quintic cutoff equals one before H/2 and zero at and after H.
    chi1=(arb(15)/(4*H)).upper();chi2=(24/(H*H)).upper()
    inner=H/2;decay=(inner**(arb(3)/2)/3).lower()
    airy_split=arb(2)/3
    # Ai and Ai' <= 3/4 (1+z)^1/4 exp(-2 z^(3/2)/3).
    # Split one half of the squared exponential at the start of the cutoff.
    Msplit=(arb(9)/16*(arb(2)/3*(airy_split**(-arb(2)/3)*(arb(2)/3).gamma())
                      +arb(2)/3/airy_split)).sqrt().upper()
    critical=(arb(2)/3/decay).upper()
    # Use the exact unrestricted maximum, not evaluation at a rounded
    # critical-point endpoint (which need not be an upper bound).
    derivative_frequency=((arb(2)/3/decay)**(arb(2)/3)*(-arb(2)/3).exp()).upper()
    height_frequency=(-decay*qlo).exp().upper()
    cutoff_first=(4*c*ratio*chi1*Msplit*derivative_frequency).upper()
    cutoff_second=(2*c*ratio*chi2*Msplit*height_frequency).upper()
    F=(potential_source+cutoff_first+cutoff_second).upper()
    # The complete R39 inverse, including its separate exact mean columns.
    Nnonzero=(pi*ai0/c*(1+qlo**(-2))**(arb(1)/6)).upper()
    Nmean=(pi/(2*c)).upper()
    Nregular=((pi*cA).sqrt()/2).upper()
    Nwave=max(Nnonzero,Nmean,Nregular)
    finite_fee=arb(2) # zero trial on the actual root mean and regular input slots
    Rfour=(finite_fee+2*Nwave*Cs*F).upper()
    source_gain=(2*Nwave*Cs).upper()
    weak_gain=(2*Nwave*Cw).upper()
    gate('the complete real-axis Airy and cutoff budgets are finite',
         all(v.is_finite() and v>0 for v in (ai0,aip,c,Msplit,F,Rfour)))
    gate('both actual finite input slots are retained with their full outputs',finite_fee==2 and Nmean>0 and Nregular>0)
    out=dict(kind='actual_exact_positive_full_cap_contact_and_Airy_four_thirds',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(q):sha(q) for q in (a.chart,a.density_jets,a.potential,a.whole_cap)},
        identity=chart['identity'],whole_cap_parameter_interval=whole['exact_parameter_interval'],
        actual_canonical_positive_height=chart['canonical_real_half_height'],
        actual_canonical_angle_strip=chart['canonical_complex_angle_strip'],
        actual_quarter_circle_frequency=chart['actual_quarter_circle_frequency'],
        exact_operator='P_plus=-d_y^2-y*d_phi^2-V(-y,phi)',
        exact_height='w=tau U, tau=alpha_c^(-1/2), log alpha_c=(log Ucal)/2-(log Delta)/3',
        exact_Delta_first_radial_identity='Delta_rho+q Delta_theta=(3/(2rho))*((F_plus+F_minus)/2-Delta), with the removable rho=0 value',
        complete_height_gradient={k:record(v) for k,v in dict(
            Delta_theta=Delta_theta,Delta_rho=Delta_rho,
            log_alpha_physical_rho=Lrho,log_alpha_physical_theta=Ltheta,
            log_alpha_canonical_y=Ly,log_alpha_canonical_phi=Lphi,
            log_tau_C0_gradient=G,height_absorption=absorb,
            all_root_extension_energy=Eall,regular_mean_extension_energy=Ereg).items()},
        all_root_and_regular_contact=all_contact,high_root_and_regular_contact=high,
        contact_spaces='X=H_phi^(1/3) direct-sum C_regular; ordinary source=L2_y H_phi^(-2/3); weak source norm=||(F_y,F_phi/sqrt(y))||L2; full output=Xstar',
        exact_grounded_source='f_ground=(J_plus/tau)*(f-grad(log tau) dot F) composed with Psi_plus; F_ground=(J_plus/tau)*DPsi_plus^(-1)*F composed with Psi_plus',
        exact_Airy_trial='2 i c lambda^(-1/3) Ai(y lambda^(2/3)) chi(y) on every nonzero actual root frequency; zero on root mean and regular input',
        exact_complete_residual='-chi V(-y,phi) U - 2 chi_prime U_y - chi_second U; no principal error term is present',
        physical_frequency_weight='L=diag((1+|q*n|^2)^(1/2),1_regular); mean weight=1',
        complete_Airy_source={k:record(v) for k,v in dict(
            Ai_zero=ai0,minus_Aiprime_zero=aip,c_A=cA,c=c,
            potential_modulus=V,potential_phi_derivative=Vphi,
            potential_Hminus_two_thirds_multiplier=Vmult,
            physical_frequency_ratio=ratio,cutoff_first_derivative=chi1,
            cutoff_second_derivative=chi2,cutoff_exponential_rate=decay,
            split_positive_Airy_L2_majorant=Msplit,
            first_cutoff_frequency_critical=critical,
            full_first_cutoff_frequency_maximum=derivative_frequency,
            complete_potential_source=potential_source,
            complete_first_cutoff_source=cutoff_first,
            complete_second_cutoff_source=cutoff_second,
            full_trial_residual_times_L_four_thirds=F).items()},
        complete_original_frame={k:record(v) for k,v in dict(
            nonzero_contact_to_one_wave=Nnonzero,mean_contact_to_one_wave=Nmean,
            regular_contact_to_one_wave=Nregular,all_slots_contact_to_one_wave=Nwave,
            finite_mean_and_regular_comparison_fee=finite_fee,
            exact_full_unitary_norm=arb(1),
            right_and_left_full_four_thirds_remainder=Rfour,
            complete_local_ordinary_source_to_affine_outgoing=source_gain,
            complete_local_weak_source_to_affine_outgoing=weak_gain).items()},
        full_augmented_regular_and_root_mean_retained=True,
        actual_full_uncompressed_cap_and_nonzero_infinite_tail_fee_retained=True,
        positive_negative_frequency_crossings_and_all_output_modes_retained=True,
        true_root_height_shear_and_Piola_density_retained=True,
        proved_smoothing_window='R_cap+I: H^s -> H^(s+4/3), -4/3<=s<=0, in the full original R39 root Airy frame plus the balanced regular slot; the same constant controls both endpoints',
        full_higher_Sobolev_window_proved=False,weighted_same_width_bound_proved=False,
        final_regular_mean_compatibility_solved=False,full_returned_Rstar_proved=False,
        gates=gates,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_negative_canonical_cancellation_chart.py','fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py')},
        scope='Actual full-cap source/contact on the same exact canonical collar, and complete original-frame L2 right/left 4/3 Ai reflection remainder, with the root mean and regular scalar input/output retained. It does not solve the final regular compatibility equations or claim weighted/high-Sobolev full returned inverse.',
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),height=out['complete_height_gradient'],
        contact=all_contact,Airy_source=out['complete_Airy_source'],frame=out['complete_original_frame']),flush=True)


if __name__=='__main__':main()
