#!/usr/bin/env python3
"""Full actual strict energy in the unshifted two-row density frame.

Uses only the already proved 215-cell full fields.  The exact first-order
system has log(mu) first derivatives and the original d, not Fcal/mu.
Every mean and ordinary source is kept.  The original amplitude frame is
recovered, with its shear and full mean, using actual first angular jets.
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


def up(v):return stored(v).upper()
def lo(v):return stored(v).lower()


def half_multiplier(M,D,N):
    """Complete H_N^+/-1/2 multiplier via the exact two-row H1 majorant."""
    d=D/N
    one=((d*d+4*M*M).sqrt()+d)/2
    return (M*one).sqrt().upper()


def triangular_norm(a,c,d):
    """Operator norm of [[a,0],[c,d]], also of [[d,0],[c,a]]."""
    trace=a*a+c*c+d*d
    disc=((a*a+c*c-d*d)**2+4*c*c*d*d).sqrt()
    return ((trace+disc)/2).sqrt().upper()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--fields',type=Path,default=Path('notes/2026-11-13-R46-native-WKB-full-strict-fields-v2.json.gz'))
    p.add_argument('--old-density',type=Path,default=Path('notes/2026-11-13-R46-complete-density-transport-bootstrap.json'))
    p.add_argument('--old-word',type=Path,default=Path('notes/2026-11-13-actual-central-strong-word.json'))
    p.add_argument('--height-weight',type=Fraction,default=Fraction(9))
    p.add_argument('--scales',type=int,nargs='+',default=[1,4,16,64,256,1024,4096,65536,1048576])
    p.add_argument('--bits',type=int,default=384)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists() or a.height_weight<=0 or min(a.scales)<1:
        raise ValueError('fresh report and positive fixed height/norm weights required')
    ctx.prec=a.bits;tick=time.monotonic()
    f=checked(a.fields,'fourfold_strict_actual_wkb_fields.py')
    old=checked(a.old_density,'fourfold_strict_density_transport_bootstrap.py')
    word=checked(a.old_word,'fourfold_actual_central_strong_word.py')
    if f['identity']!=old['identity'] or f['identity']!=word['identity']:
        raise ValueError('same original full actual strict family required')
    if old['inputs'].get(str(a.fields))!=sha(a.fields):
        raise ValueError('the original density proof uses another native field')
    if not f['mean_retained'] or len(f['cells'])!=215:
        raise ValueError('the original full 215 closed cells and mean are required')
    lam=exact_arb(a.height_weight);rootlam=lam.sqrt()
    ell=chi=A=B=arb(0);mulo=None;muhi=arb(0);meanw=meany=arb(0)
    # Complete actual multiplier pairs (zeroth and first x derivative, x=4theta).
    m0=m1=r0=r1=tm0=tm1=arb(0)
    cursor=Fraction(0);cells=[]
    for i,c in enumerate(f['cells']):
        left,right=Fraction(c['left']),Fraction(c['right'])
        if left!=cursor or not left<right:raise ValueError('full strict closed cover gap')
        cursor=right;h=2*exact_arb(right-left)
        M={k:up(v) for k,v in c['complete_complex_field_moduli'].items()}
        D=c['complete_complex_first_derivative_moduli'];e=c['energy']
        ml=lo(c['geometry']['mu_modulus_lower'])
        if not ml>0:raise ValueError('the real positive density loses its certified gap')
        m=up(c['geometry']['m_modulus_upper']);rr=M['mu'].sqrt()
        xchi=max(arb(0),up(e['first_characteristic_rate_forward']),up(e['first_characteristic_rate_backward']))
        xell=(M['Lr']+M['v']*M['Ltheta']).upper()
        aa=(M['nu']/ml.sqrt()).upper();bb=(M['d']/ml.sqrt()).upper()
        cross=(rootlam*aa+bb/rootlam).upper()
        rate=(xchi+xell+cross).upper()
        ell+=h*xell;chi+=h*xchi;A+=h*aa;B+=h*bb
        mulo=ml if mulo is None else min(mulo,ml);muhi=max(muhi,M['mu'])
        meanw=max(meanw,rr/rootlam)
        # old y=(w_theta +/- zeta)/2, w=sqrt(mu)u, zeta=(p+Tu)/sqrt(mu).
        aaold=rr*M['Ltheta']/2;bbold=M['T']/ml.sqrt()
        meany=max(meany,((1+(aaold*aaold+bbold*bbold)/lam)/2).sqrt())
        mx=m*M['Ltheta']/8;rx=rr*M['Ltheta']/8
        tx=up(D['T']['angular'])/4
        m0=max(m0,m);m1=max(m1,mx);r0=max(r0,rr);r1=max(r1,rx)
        tm0=max(tm0,m*M['T']);tm1=max(tm1,m*tx+mx*M['T'])
        cells.append(dict(cell=i,left=str(left),right=str(right),
            real_transport_diagonal_bound=record(xchi),
            true_log_density_material_derivative_bound=record(xell),
            ordinary_height_coupling_bound=record(cross),
            full_squared_energy_rate=record(rate),
            both_reflected_halves_log_contribution=record((h*rate/2).upper())))
    if str(cursor)!=old['exact_physical_interval'][1]:
        raise ValueError('the original actual full strict endpoint differs')
    logarithm=((chi+ell+rootlam*A+B/rootlam)/2).upper()
    growth=logarithm.exp().upper();mulo=mulo.lower();muhi=muhi.upper()
    raw_source=(growth/mulo.sqrt()).upper()
    rows=[]
    for N in a.scales:
        low=min(lam,16*arb(N)**2*mulo,1/muhi).lower()
        high=max(lam,16*arb(N)**2*muhi,1/mulo).upper()
        if not low>0:raise ValueError('the full physical energy comparison is not positive')
        physical=(growth*(high/low).sqrt()).upper()
        physical_source_half=(raw_source/low.sqrt()).upper()
        mm=half_multiplier(m0,m1,N);mr=half_multiplier(r0,r1,N)
        mtm=half_multiplier(tm0,tm1,N)
        frame=triangular_norm(mm,mtm,(4*arb(N)).sqrt()*mr)
        amplitude=(frame*physical*frame).upper()
        amplitude_source=(frame*physical).upper()
        initial=(growth*high.sqrt()).upper()
        rows.append(dict(scale=N,energy_comparison_lower=record(low),energy_comparison_upper=record(high),
            full_physical_Cauchy_positive_half=record(physical),
            full_physical_Cauchy_flux_dual_negative_half=record(physical),
            full_physical_Cauchy_all_between_minus_half_and_half=record(physical),
            full_physical_L1L2_source_to_positive_half=record(physical_source_half),
            full_physical_L1_HNminus_half_source_to_zero=record(physical),
            exact_old_m_half_multiplier=record(mm),exact_old_sqrtmu_half_multiplier=record(mr),
            exact_old_combined_Tm_half_multiplier=record(mtm),
            full_original_normal_frame_and_inverse_at_base=record(frame),
            same_full_original_L2_amplitude_and_inverse=record(amplitude),
            same_full_original_L1_HNminus_half_source_to_L2_amplitude=record(amplitude_source),
            old_density_base_mean_initial=record((meanw*initial).upper()),
            old_density_base_y_initial=record((meany*initial).upper()),
            old_density_base_mean_source=record((meanw*raw_source).upper()),
            old_density_base_y_source=record((meany*raw_source).upper())))
    best=min(rows,key=lambda z:up(z['same_full_original_L2_amplitude_and_inverse']))
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('the new full real energy exponent is smaller',logarithm<up(old['full_base_energy_log']))
    gate('the actual complete L2 amplitude propagation improves',
         up(best['same_full_original_L2_amplitude_and_inverse'])<up(word['norms']['true_strict_L2_amplitude']))
    gate('the complete old density mean and derivative-zero conversions improve',
         meanw<up(old['base_mean_w_conversion']) and meany<up(old['base_density_conversion']))
    gate('all declared exact source/field coverage is complete',len(cells)==215 and cursor>0)
    out=dict(kind='actual_complete_strict_unshifted_half_density_energy_and_original_base_frame',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(p):sha(p) for p in (a.fields,a.old_density,a.old_word)},identity=f['identity'],
        actual_parameter_scope='The entire original exact real affine parameter interval, hence the selected R101 p_infinity.',
        entire_original_real_parameter_box=True,native_cells_recomputed=0,
        exact_physical_interval=old['exact_physical_interval'],positive_cells=215,
        exact_fixed_height_weight=str(a.height_weight),
        exact_state='Y_sigma=(sqrt(mu)*u_theta+sigma*p/sqrt(mu))/sqrt(2); original p=a*u_r+b*u_theta',
        exact_transport='d_r Y_sigma+d_theta[(v-sigma*nu)Y_sigma]=[ell_r+(v+sigma*nu)ell_theta]Y_-sigma/2+sigma*(f-d*u)/sqrt(2*mu)',
        exact_height='u_r=nu*(Y_plus-Y_minus)/sqrt(2*mu)-v*u_theta',
        exact_energy='int(lambda*abs(u)^2+mu*abs(u_theta)^2+abs(p)^2/mu); lambda is constant positive',
        exact_Hermitian_wave_cross='ell_r+v*ell_theta; the two signed nu*ell_theta terms cancel exactly',
        exact_Hermitian_height_cross='(lambda*nu-d)/sqrt(2*lambda*mu) * (1,-1)',
        no_Fcal_or_second_density_derivative_in_the_new_energy=True,
        ordinary_source='original physical scalar f in dr; no weak load is renamed',
        mean_height_flux_all_head_paths_and_full_old_shear_retained=True,
        true_original_subintervals_and_both_time_directions=True,
        all_fractional_base_orders_use_the_actual_flux_dual_and_interpolation=True,
        full_Ltwo_amplitude_is_independent_of_the_auxiliary_comparison_scale=True,
        exact_physical_frequency='theta derivative is 4*n; Lambda=max(1,4*abs(n)), including mean one',
        complete_original_frame='Hadamard followed by [[m Lambda^-1/2,0],[-Tm Lambda^-1/2,i sqrt(mu) Lambda^1/2]], with all mean entries',
        bounds={k:record(v.upper()) for k,v in dict(
            integrated_transport_diagonal=chi,integrated_material_log_density=ell,
            integrated_nu_over_sqrtmu=A,integrated_d_over_sqrtmu=B,
            full_energy_logarithm=logarithm,full_energy_Cauchy_growth=growth,
            full_L1L2_source_to_energy=raw_source,full_mu_lower=mulo,full_mu_upper=muhi,
            old_density_mean_conversion=meanw,old_density_y_conversion=meany,
            old_m_modulus=m0,old_m_first_x_derivative=m1,
            old_sqrtmu_modulus=r0,old_sqrtmu_first_x_derivative=r1,
            old_Tm_modulus=tm0,old_Tm_first_x_derivative=tm1,
            prior_energy_logarithm=up(old['full_base_energy_log']),
            prior_true_strict_base_amplitude=up(word['norms']['true_strict_L2_amplitude'])).items()},
        cells=cells,rows=rows,best_base_amplitude_scale=best['scale'],
        best_complete_original_base_amplitude=best['same_full_original_L2_amplitude_and_inverse'],
        source_scale_embedding='For a comparison scale M<=N, H_N^(-1/2) embeds into H_M^(-1/2) with norm one; output amplitude L2 is the same space.',
        higher_density_bootstrap_reconsumed=False,full_strong_R46_remainder_recomputed=False,
        full_returned_Rstar_recomputed=False,finite_head_inverse_proved=False,
        full_feedback_inverse_proved=False,new_nu_body_or_deep_tail_transfer_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py','fourfold_negative_canonical_cancellation_chart.py')},
        gates=gates,seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,energy_log=logarithm.str(12),energy_growth=growth.str(12),
        best_scale=best['scale'],amplitude=best['same_full_original_L2_amplitude_and_inverse']['ball'],
        out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
