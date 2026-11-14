#!/usr/bin/env python3
"""Pair the actual signed root densities through one true common q-flow.

All field and H2 bounds come from the complete new Fourier native.  The
signed/common comparison is analytic and uses the already paid full nested
path margin; no data are sampled and no finite coefficient is substituted
for the full true potential.
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


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--native',type=Path,default=Path('notes/2026-11-13-actual-root-correlated-potential-v2.json'))
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():raise ValueError('new actual paired-root report required')
    ctx.prec=a.bits;tick=time.monotonic()
    d=checked(a.native,'fourfold_actual_root_correlated_potential_v2.py')
    if d['kind']!='actual_complete_root_correlated_first_order_potential_v2':
        raise ValueError('complete actual correlated native required')
    M={k:stored(v).upper() for k,v in d['complete_field_moduli'].items()}
    B={k:stored(v).upper() for k,v in d['complete_correlated_bounds'].items()}
    R=exact_arb(Fraction(d['rho_radius']))
    margin=stored(d['complete_characteristic_angle_margin']).lower()
    if not margin>0:raise ValueError('complete nested common/signed path margin missing')
    C,Cr,Ct,Q,K=M['C'],M['C_rho'],M['C_theta'],M['q'],M['kstar']
    C0=min(C,stored(d['complete_root_C0_modulus']).upper())
    # All paths and straight comparison segments are inside S-margin.
    Qtheta=(Q/margin).upper()
    Kb=(arb(2)/5*K*Ct*(Qtheta*R).exp()).upper()
    b=(Kb*R**(arb(5)/2)).upper()
    Fb=(Kb*b.exp()).upper()
    Db=(arb(3)/8*(C*R).exp()*Fb).upper()
    EZ=((C*R).exp()*(arb(2)/7*Cr+arb(4)/35*Q*Ct)
        +arb(4)/35*C0*C0*(C0*R).exp()).upper()
    Zmax=(1+arb(2)/5*R*C0+R*R*EZ).upper()
    ERcommon=(2*EZ+arb(4)/25*C0*C0+arb(4)/5*R*C0*EZ+R*R*EZ*EZ).upper()
    ERbranch=((2*b).exp()*(2*Zmax*Db*R.sqrt()
        +Db*Db*R**3+2*Zmax*Zmax*Kb*R.sqrt())).upper()
    ER=(ERcommon+ERbranch).upper()
    ratio=((Zmax+Db*R**(arb(5)/2))**2*(2*b).exp()).upper()
    EH=B['H_second_remainder']
    numerator2=(EH*ratio+C0*C0/5+(R*C0/4+arb(5)/16)*ER).upper()
    e=B['Delta_minus_one']
    V=(numerator2/(1-e)**(arb(4)/3)).upper()
    W=(V+5050).upper()
    L=exact_arb(Fraction(d['canonical_real_half_height']))
    halo=exact_arb(Fraction(d['canonical_complex_radial_halo']))
    eta=(W*L*L/2).upper()
    pos=(V*L*L/arb.pi()**2).upper()
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('same complete nested signed/common path margin is positive',margin>0)
    gate('both actual signed logarithmic comparisons are bounded with their full complex paths',b<arb(1)/8)
    gate('paired ratio second remainder improves independent signed-density bounds',ER<B['ratio_second_remainder'])
    gate('paired actual potential improves the complete preceding native bound',V<B['full_canonical_potential'])
    gate('all-frequency negative height Volterra including mean is a contraction',eta<1)
    gate('same finite positive-collar zero-two-trace form remains coercive',pos<1)
    out=dict(kind='actual_complete_root_potential_paired_through_common_characteristics',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(a.native):sha(a.native)},identity=d['identity'],root=d['root'],
        exact_canonical_domain=d['exact_complete_canonical_domain'],
        canonical_real_half_height=d['canonical_real_half_height'],
        canonical_complex_angle_strip=d['canonical_complex_angle_strip'],
        canonical_complex_radial_halo=d['canonical_complex_radial_halo'],
        actual_quarter_circle_frequency=d['actual_quarter_circle_frequency'],
        exact_common_reference='D0 f=C f, D0=partial_rho+q*partial_theta, f(0)=1',
        exact_common_ratio='Z=(3/2) integral_0^1 t^(1/2) exp(-integral_(t*rho)^rho C(s,Theta_s) ds) dt',
        exact_signed_comparison='F_sigma/f=exp(delta_I_sigma), |delta_I_sigma|<=Kb*|rho|^(5/2)',
        exact_Delta_comparison='Delta/f=Z+delta_Z, |delta_Z|<=Db*|rho|^(5/2)',
        exact_ratio='Delta^2/(F_plus*F_minus)=(Z+delta_Z)^2 exp(-delta_I_plus-delta_I_minus)',
        exact_Z_first_jet='Z=1-(2/5)*rho*C0+rho^2*E_Z',
        exact_potential_cancellation='N/rho^2=H2*ratio-C0^2/5+(rho*C0/4+5/16)*ratio_second_remainder',
        bounds={name:record(value) for name,value in dict(
            C0=C0,full_common_flow_angle_derivative=Qtheta,
            signed_common_logarithm_Kb=Kb,signed_common_logarithm_modulus=b,
            signed_common_exponential_remainder_coefficient=Fb,
            Delta_over_common_f_branch_remainder_coefficient=Db,
            common_ratio_second_remainder=EZ,common_ratio_modulus=Zmax,
            squared_common_ratio_second_remainder=ERcommon,
            true_signed_branch_ratio_second_remainder=ERbranch,
            complete_ratio_second_remainder=ER,complete_ratio_modulus=ratio,
            complete_H_second_remainder=EH,full_numerator_over_rho_squared=numerator2,
            full_canonical_potential=V,full_shifted_5050_residual=W,
            full_real_segment_radial_derivative=V/halo,
            full_negative_height_Volterra_norm=eta,
            full_negative_height_Volterra_resolvent=1/(1-eta),
            full_positive_finite_zero_two_trace_relative_fee=pos,
            full_positive_finite_zero_two_trace_coercivity=(1-pos).lower(),
            original_complete_potential_bound=B['previous_potential_bound'],
            complete_bound_improvement_factor=B['previous_potential_bound']/V).items()},
        potential_domain='entire paid two-sided fixed canonical product domain including radial halo',
        radial_derivative_domain='real xi in [-height,height], complete complex phi strip; no claim on radial halo boundary',
        complex_qtheta_scope='Cauchy on the original full field strip, restricted only to the common nested paths and their straight angular comparison segments, all with the recorded strict margin',
        all_modes_all_true_parameters_all_field_errors_retained=True,
        original_positive_negative_height_Piola_and_all_ports_unchanged=True,
        old_finite_positive_approximate_chart_used=False,
        full_returned_Rstar_recomputed=False,finite_head_inverse_proved=False,
        gates=gates,dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py')},
        scope='Complete same true root potential bound, sharpened by paired signed/common characteristic identities. Canonical product, physical source, density, height and every mean/regular port are those already paid for the exact old object. Complete return and finite-head inverses are not inferred.',
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),bounds=out['bounds'],seconds=out['seconds']),flush=True)


if __name__=='__main__':main()

