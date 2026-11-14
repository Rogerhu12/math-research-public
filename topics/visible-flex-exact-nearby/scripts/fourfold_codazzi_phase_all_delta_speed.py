#!/usr/bin/env python3
"""Complete complex-parameter speed bounds from the proved scalar cache.

The explicit centre family is Q_delta=Qbar+delta Z, nu_delta=nu0+delta.
Its direction Z is arbitrary subject to explicitly supplied field norms;
this report does not identify it with an exact PDE response.  The exact
gamma*q cancellation prevents a false root-singular parameter charge.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import time
from pathlib import Path

from flint import arb, ctx
from fourfold_codazzi_phase_scalar_cache_jets import read, restrict_model
from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_metric_defect import record, save, sha

COVER = '94492bbafda1e5efb30b129e534171c9fc305524a2d972064e34e8894948bad3'
TCACHE = 'ab5e8156fbaf50c80e944a15d68858d29419229e7ae10665b432cd1af593587d'
JET_SOURCE = 'be012cec4863f809b6de67a880fe261d29518f02c2df563db776e4fa194849d8'


def up(x):
    return abs(x).upper()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cover', type=Path, default=Path('notes/2026-11-14-R133-complete-169-germ-phase-scalar-cover-native.json.gz'))
    ap.add_argument('--compact-T', type=Path, default=Path('notes/2026-11-14-R133-complete-scalar-derivative-and-compact-T-cache-native.json.gz'))
    ap.add_argument('--parameter-radius', default='1/1000000')
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args(); started = time.monotonic(); ctx.prec = 320
    if args.out.exists():
        raise FileExistsError('preserve every complete parameter budget')
    if sha(args.cover) != COVER or sha(args.compact_T) != TCACHE or sha(Path(__file__).with_name('fourfold_codazzi_phase_scalar_cache_jets.py')) != JET_SOURCE:
        raise ValueError('the full scalar derivative identities changed')
    cover, tc = read(args.cover), read(args.compact_T)
    if not (cover['complete'] and tc['complete'] and tc['compact_T_complete']):
        raise ValueError('the exact whole negative interval and full compact T cover are required')
    if cover['exact_affine_offset'] != '0' or tc['exact_affine_offset'] != '0':
        raise ValueError('this calculation is at the genuine eta0, offset zero')
    rho_exact = Fraction(args.parameter_radius)
    if not 0 < rho_exact <= Fraction(1, 1000000):
        raise ValueError('the explicit supported complex parameter radius is (0,10^-6]')
    rho = exact_arb(rho_exact); ca, cb = Fraction(1,20), Fraction(9,50)
    Trows = {tuple(map(Fraction,r['interval'])): r for r in tc['compact_T_models']}
    names = ['c_difference_m','c_difference_z','c_first_m','c_first_z',
             'c_second_m','c_second_z','c_third_m','c_third_z',
             'drift_beta_over4','drift_beta_Kabs_over4','drift_beta_Kdifference_over4',
             'drift_beta_Kfirst_over4','drift_beta_Ksecond_over4','drift_beta_Kthird_over4',
             'gamma_first','gamma_second','gamma_third']
    integrals = {n:arb(0) for n in names}; maxima = {n:arb(0) for n in names}
    ratio_max = arb(0); minimum_factor = arb(1); rows = []; used_T = 0
    zero_outside = True
    left, right = map(Fraction,cover['exact_complete_interval']); cursor = left
    for germ in cover['germs']:
        path = Path(germ['path'])
        if sha(path) != germ['sha256']:
            raise ValueError('a genuine scalar report changed')
        scalar = read(path)
        for row in scalar['rows']:
            a,b = map(Fraction,row['interval'])
            if a != cursor or not a < b:
                raise ValueError('the complete same scalar cells must remain a partition')
            val = {n:restrict_model(row,n,a,b,0)[2] for n in ('beta','K','gamma','q')}
            if not (val['K'] < 0 and val['gamma'] > 0 and val['q'] > 0):
                raise ValueError('complete negative type and positive scalar factors are required')
            in_support = ca <= a < b <= cb
            if (a < ca < b) or (a < cb < b):
                raise ValueError('a model may not straddle an exact compact support endpoint')
            if in_support:
                tr = Trows[(a,b)]
                if tr['scalar_native_sha256'] != germ['sha256']:
                    raise ValueError('the T quotient must use the exact same complete scalar identity')
                T = restrict_model(tr,'T',a,b,0)[2]
                t = real_interval((a-ca)/(cb-ca),(b-ca)/(cb-ca))
                W = min(arb(1), up(4096*t**6*(1-t)**6)).upper()
                wp = exact_arb(Fraction(24576)/(cb-ca))*t**5*(1-t)**5*(1-2*t)
                k = T*wp; kval = up(k); R = up(k/(-val['K'])); used_T += 1
            else:
                W = kval = R = arb(0)
            eta = up(rho*R)
            if not eta < 1:
                raise ValueError('the actual complete parameter disc crosses the square-root branch')
            sm = (1-eta).sqrt().lower(); sp = (1+eta).sqrt().upper()
            expfee = (rho*W).exp().upper(); K0 = up(val['K'])
            Kabs = up((K0+rho*kval)*expfee)
            Kdiff = up((kval+W*K0)*expfee)
            Kfirst = up((kval+W*(K0+rho*kval))*expfee)
            Ksecond = up((W*W*(K0+rho*kval)+2*W*kval)*expfee)
            Kthird = up((W**3*(K0+rho*kval)+3*W*W*kval)*expfee)
            gq = up(val['gamma']*val['q']); B = up(val['beta'])/4
            coeff = dict(
                c_difference_m=up(gq*R/(1+sm)), c_difference_z=up(gq*sp),
                c_first_m=up(gq*R/(2*sm)),
                c_first_z=up(gq*(sp+rho*R/(2*sm))),
                c_second_m=up(gq*R*R/(4*sm**3)),
                c_second_z=up(gq*(R/sm+rho*R*R/(4*sm**3))),
                c_third_m=up(gq*3*R**3/(8*sm**5)),
                c_third_z=up(gq*(3*R*R/(4*sm**3)+3*rho*R**3/(8*sm**5))),
                drift_beta_over4=up(B),drift_beta_Kabs_over4=up(B*Kabs),
                drift_beta_Kdifference_over4=up(B*Kdiff),
                drift_beta_Kfirst_over4=up(B*Kfirst),
                drift_beta_Ksecond_over4=up(B*Ksecond),
                drift_beta_Kthird_over4=up(B*Kthird))
            for j,name in enumerate(('gamma_first','gamma_second','gamma_third'),1):
                coeff[name] = up(val['gamma']*(rho*W/2).exp()*(W/2)**j)
            if not in_support:
                zero_outside = zero_outside and all(coeff[n] == 0 for n in (
                    'c_second_m','c_second_z','c_third_m','c_third_z'))
            length = exact_arb(b-a)
            for name in names:
                integrals[name] += length*coeff[name]
                maxima[name] = max(maxima[name],coeff[name]).upper()
            ratio_max = max(ratio_max,R).upper(); minimum_factor = min(minimum_factor,sm).lower()
            rows.append(dict(interval=row['interval'],actual_scalar_germ=row['actual_scalar_germ'],
                scalar_native_sha256=germ['sha256'],compact_support=in_support,
                complete_abs_k_over_q_squared=record(R),
                complete_squared_root_relative_margin=record((1-eta).lower()),
                complete_parameter_square_root_lower=record(sm),
                complete_optical_reference_gamma_q=record(gq),
                full_complex_disc_coefficients={n:record(coeff[n]) for n in names},
                complete_metric_parameter_coefficients={n:record(v) for n,v in dict(
                    W=W,abs_k=kval,abs_K_delta=Kabs,K_difference_over_delta=Kdiff,
                    K_first=Kfirst,K_second=Ksecond,K_third=Kthird).items()}))
            cursor = b
    nu0 = Fraction(cover['configuration']['exact_nu'])
    tests = [
        ('all626 complete scalar cells reach the exact true strict endpoint',len(rows)==626 and cursor==right),
        ('all220 compact T cells are consumed with exact same scalar identities',used_T==len(Trows)==220),
        ('the whole complex parameter disc avoids the actual square-root branch',rho*ratio_max<1),
        ('the entire real parameter interval remains inside the proved intrinsic nu box',Fraction(-1,25)<nu0-rho_exact<nu0+rho_exact<Fraction(-1,40)),
        ('all nonlinear optical parameter derivatives vanish off the true compact support',zero_outside),
        ('all full parameter coefficients and integrated norms are finite',all(x.is_finite() for x in integrals.values())),
        ('the actual affine parameter is eta0, with no unproved whole-eta extension',not cover['whole_original_eta'] and not tc['whole_original_eta']),
    ]
    report = dict(kind='actual_complete_complex_parameter_optical_speed_and_drift_budget',
        complete=all(bool(ok) for _,ok in tests),source_sha256=sha(__file__),
        cover_sha256=COVER,compact_T_input_sha256=TCACHE,scalar_derivative_source_sha256=JET_SOURCE,
        actual_affine_parameter='eta_0',exact_affine_offset='0',whole_original_eta=False,
        exact_nu=str(nu0),exact_parameter_disc_radius=str(rho_exact),
        exact_interval=[str(left),str(right)],exact_compact_support=['1/20','9/50'],
        actual_cells=len(rows),actual_compact_cells=used_T,rows=rows,
        maximum_complete_abs_k_over_q_squared=record(ratio_max),
        complete_relative_branch_margin=record((1-rho*ratio_max).lower()),
        complete_square_root_relative_lower=record(minimum_factor),
        integrated_full_complex_parameter_coefficients={n:record(v.upper()) for n,v in integrals.items()},
        maximum_full_complex_parameter_coefficients={n:record(v) for n,v in maxima.items()},
        exact_optical_identity='c_delta=-gamma_0*(m+delta*z)*sqrt(q_0^2-delta*T*w_prime)',
        explicit_centre_family_only=True,actual_PDE_solution_branch_assumed=False,
        response_direction_or_its_norms_consumed=False,full_phase_Schur_or_conjugacy_proved=False,
        genuine_mean_direction_z_retained=True,all_unknown_angular_modes_allowed=True,
        no_original_target_or_primitive_recomputed=True,
        gates=[dict(name=name,passed=bool(ok)) for name,ok in tests],seconds=time.monotonic()-started)
    save(args.out,report)
    print(dict(complete=report['complete'],cells=len(rows),compact_cells=used_T,
        ratio=ratio_max.str(16),branch_margin=(1-rho*ratio_max).str(16),
        integrated={n:integrals[n].str(14) for n in names[:8]},seconds=report['seconds']),flush=True)
    if not report['complete']:
        raise RuntimeError('an actual complete all-delta speed gate failed; output retained')


if __name__=='__main__':
    main()
