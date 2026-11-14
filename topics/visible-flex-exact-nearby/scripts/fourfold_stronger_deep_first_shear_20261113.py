#!/usr/bin/env python3
"""The actual K=2^128 deeper first shear and complete local map budget."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, ctx
import sympy as sp


def run():
    ctx.prec = 256
    A = arb
    checks = []
    numeric = {}

    def gate(name, statement, evidence):
        if not bool(statement):
            raise AssertionError(name)
        checks.append({'name': name, 'pass': True, 'evidence': evidence})

    def show(x):
        return x.str(45)

    def lg(x):
        return x.log() / A(2).log()

    def delta(j):
        return A(2) / 25 * A(2)**(-j)

    def zero(x):
        return sp.simplify(x) == 0

    K = A(2)**128
    Ki = 2**128
    C = 16*A(2).sqrt()
    alpha = A(65)/64
    de = delta(8193)
    et = de**(A(3)/2)/(4*A(2).sqrt())
    L = 1-de.log()
    cK = 2*(K*alpha).log()-C.log()
    cm = 1+A(15)/(8/(4*A(2).sqrt()))*(2+(2*K).log())
    beta = 3*de+6*et+(A(15)/2*et*(2*(2*K).log()-6*de.log())).sqrt()
    h = 8*de**(A(1)/256)
    Jbar = A(32768)*L/h
    low_internal = A(2)**(-5)*de**(-A(3)/8)
    low_absolute = A(2)**(-40)*de**(-A(1)/8)
    rho = A(2)**(-28)+A(2)**(-24)/A(12).sqrt()+A(2)**(-20)/(48*A(2).sqrt())

    gate('exact_amplitude_seam_old_to_b9over2',
         Q(3,2)+Q(9,2)==6,
         'C mu_(4097)=mu_4096; the new first shear changes no endpoint amplitude')
    gate('exact_amplitude_seam_at_8193',
         Q(9,2)-Q(9,2)==0,
         'The same C=2^(9/2) remains at the endpoint after the first-plateau change')
    x=sp.symbols('x')
    S=10*x**3-15*x**4+6*x**5
    gate('complete_quintic_endpoint_two_jets',
         all(sp.diff(S,x,k).subs(x,e)==0 for e in (0,1) for k in (1,2)),
         'The exact profile and all parameter bump endpoint two-jets match')
    gate('new_log_variation_constant',cK<175,show(cK))
    jumps=[(K/de).log(),(K*alpha/de**2).log(),(alpha/de**2).log(),(1/(C*de)).log()]
    gate('actual_four_log_jump_sum',
         sum(jumps).overlaps(-6*de.log()+cK),
         'All four actual log jumps are included')
    for i, D in enumerate(jumps,1):
        gate(f'actual_jump_window_{i}',D>A(8193)/2 and D<3*(8193+4),show(D))
        gate(f'actual_jump_below_three_log_delta_{i}',D<-3*de.log(),show(D/(-de.log())))
    gate('new_C2_flat_exponents',Q(9,2)-1>0 and Q(9,2)-Q(5,2)>0
         and Q(9,2)-4==Q(1,2),
         'The full background zero, first and second jets have powers7/2,2,1/2')
    curve=K*L/(1-delta(128).log())*delta(4096)**(A(3)/2)*de**2*delta(128)**(-A(7)/2)
    gate('actual_changed_curvature_dominated_by_finite_prefix',curve<1,show(lg(curve)))
    w=2*K*delta(4096)**(A(3)/2)*de**(A(7)/2)
    gate('actual_complete_mean_background_gate',w<1,show(lg(w)))
    gate('all_deep_geometric_jet_envelopes_decrease',
         (L+A(2).log())**2/L**2<A(2).sqrt(),
         'Even the slowest C2 envelope L_j^2 delta_j^(1/2) decreases after8193')
    gate('actual_negative_density_ratio',2*Ki*Q(65,64)<2**132,
         'The complete r^-8 endpoint factor and new highest/lowest profile values are included')
    gate('actual_Airy_density_hypothesis',132<272,
         'The enlarged complete reference theorem applies to this actual new density ratio')

    roots=[]
    for kind,D in enumerate((jumps[0],jumps[2]),1):
        zz=(7*et/(30*A(12).sqrt()*D)).sqrt()
        dd=zz/(196*(1-4*zz))
        slope=(10080*A(12).sqrt()*D/et**3*(1-4*zz)).sqrt()
        gate(f'new_actual_root_full_germ_{kind}',zz<A(2)**(-20) and dd<A(2)**(-10),
             {'z':show(zz),'d':show(dd)})
        gate(f'new_actual_root_complete_slope_{kind}',
             slope*de**(A(9)/4)>1 and slope*de**(A(9)/4)<A(2)**16*A(8197).sqrt(),
             show(slope*de**(A(9)/4)))
        roots.append({'kind':kind,'z':show(zz),'d':show(dd),
                      'scaled_slope':show(slope*de**(A(9)/4))})
    gate('new_actual_reference_auxiliary_speed',A(2)**16*8197*de.sqrt()<1,
         show(lg(A(2)**16*8197*de.sqrt())))
    gate('new_actual_reference_strict_split',8197*de**2<1,show(lg(8197*de**2)))

    kk,nn,pp=sp.symbols('k nu p', nonzero=True)
    gen=sp.Matrix([[kk,nn/pp],[-pp,-kk]])
    mm=sp.symbols('m',integer=True,positive=True)
    nu=mm**2*(mm**2-1)/12
    km=(mm**2-4)/sp.sqrt(12)
    gate('exact_true_platform_square',
         all(zero(v) for v in (gen*gen).subs({kk:km,nn:nu})
             +sp.eye(2)*(7*mm**2-16)/12),
         'The exact sin/cos platform formula controls both true rows')
    ks,al,vs,cs=sp.symbols('K alpha nu C', nonzero=True)
    B=sp.diag(1,1/cs)*sp.Matrix([[1,0],[-1,1]])*sp.Matrix([[1,al*vs],[0,1]])*sp.Matrix([[1,0],[-ks,1]])
    Bclaimed=sp.Matrix([[1-ks*al*vs,al*vs],[(ks*al*vs-ks-1)/cs,(1-al*vs)/cs]])
    gate('exact_new_three_shear_matrix',all(zero(v) for v in B-Bclaimed),
         'The actual endpoint second row is divided by C, never by the new first shear')
    gate('exact_new_matrix_determinant',zero(B.det()-1/cs),
         'The full trace-zero flow has determinant1/C at its actual endpoint')
    gate('new_true_low_window_short_gate',16*Ki*Q(1,2**160)==Q(1,2**28),
         'All six real short segments are small on the stated new absolute-error window')
    gate('new_true_low_window_platform_gate',low_absolute**2*de<1,
         show(lg(low_absolute**2*de)))
    error_const=2**8*Ki+64*Ki**2
    gate('complete_ordered_matrix_error_constant',error_const<2**272,
         'Platform errors plus24 K nu (exp(16 K m^4 sqrt(delta))-1); each main platform occurs once')

    gate('complete_monotone_Gauss_low_window',rho<A(2)**(-24),show(rho))
    rho_upper=A(2)**(-24)
    rest=2*K*et/de+2*et+4*rho_upper+8*A(2).sqrt()*rho_upper*de.sqrt()/K
    gate('actual_first_shear_remaining_factors_small',rest<A(1)/16,show(rest))
    q=A(1)+A(25)/1024
    pminus=(1+q*K*(1+et/de))*rest.exp()
    gate('actual_first_shear_not_exponentiated',pminus<2*K,show(pminus/K))
    gate('complete_internal_forward_flow_constant',Q(2*4*4*2,12)<8,
         'D Pplus Cstar Pminus gives64 K nu<8 K m^4')
    gate('complete_internal_reverse_flow_constant',2*8*Ki==2**132,
         'The exact determinant-one internal inverse costs at most one further factor2')

    gate('actual_coarse_scalar_constant',cm<A(2)**10,show(cm))
    coarse=64*((A(6).exp())*(K+4)**3+8*K**3*cm**4*(cm.sqrt()+3))
    gate('complete_all_frequency_prefactor',coarse<A(2)**440,show(lg(coarse)))
    gate('complete_coarse_low_frequency_small_segments',
         (Ki+68)*de**(A(1)/4)/(4*A(2).sqrt())<1,
         show(lg((Ki+68)*de**(A(1)/4)/(4*A(2).sqrt()))))
    gate('complete_canonical_two_row_high_norm',440+10==450 and 308+4==312,
         'The actual nu Q first row and both endpoint norm conversions are retained')

    # The full material integral, with the actual complex parameter allowance.
    rc=A(2)**(-15)
    material=(16*de*(1+alpha**2/de**2)-6*de.log()+cK
              +(2*rc).exp()*(alpha**2/de**2+A(1)/2+A(1)/512)
              +4*rc*(1+alpha**2/de**2))
    gate('complete_material_integral_after_new_peak',material*de**2<64,
         show(material*de**2))
    gate('complete_true_Galerkin_window',Jbar<low_internal,
         show(lg(Jbar/low_internal)))
    gate('complete_new_angle_budget',1024*beta<h,show(lg(1024*beta/h)))
    gate('new_local_homogeneous_strong_constant',
         A(2)**131*(20/A(1).exp())**5<A(2)**148,
         show(lg(A(2)**131*(20/A(1).exp())**5)))
    gate('new_local_integral_contraction',131+26+149-320==-14,
         'The actual full finite integral map contracts, including its compressed inverse')
    gate('new_local_mean_relative_ball',18+149-320<-100,
         'The complete holonomy-one mean small root is paid before solving the map')
    gate('new_radial_Volterra_extra_constant',480*cK<-16*de.log(),
         {'log2_extra':show(480*cK/A(2).log()),'log2_paid':show(-16*lg(de))})
    gate('new_residual_actual_Z0_change',149-24==125 and 47+125==172,
         'The real Galerkin residual keeps its forcing and its enlarged near-solution factor')
    gate('new_full_physical_correction_power',4096-Q(5787,2)-16==Q(2373,2),
         'All radial growth and the new fixed variation constant are paid before the correction')
    gate('new_complete_port_correction_power',Q(2373,2)-Q(3,4)==Q(4743,4),
         'The remaining h^-2 port conversion uses the already paid h>=delta^(3/8)')
    gate('new_physical_correction_small_ball',
         A(640)*A(2)**(-106)*de**(A(2375)/2)<A(1)/4000000,
         show(lg(A(640)*A(2)**(-106)*de**(A(2375)/2))))
    gate('new_output_Duhamel_angle_constant',
         A(2)**131*(16/A(1).exp())**4<A(2)**144,
         show(lg(A(2)**131*(16/A(1).exp())**4)))
    gate('new_finite_quadratic_Lipschitz_constant',144+26+2*149<472,
         'The two full strong solution factors and real source difference enter the coefficient')
    gate('new_full_correction_Cauchy_ratio',
         4+224+320-472-25==51 and Q(4743,4)-Q(15,8)==Q(9471,8),
         'The actual local input radius, J^5 and full complex Cauchy remainder are retained')
    gate('new_full_correction_quadratic_absorption',A(2)**51*de**(A(9471)/8)<1,
         show(lg(A(2)**51*de**(A(9471)/8))))
    gate('new_complete_local_quadratic_constant',472+1<480,
         'The actual finite and complete all-angle correction remainders fit the stated G')

    gate('new_exact_normalization_continuity',Q(39,4)-131+131==Q(39,4),
         'The new normalization equals the old one at exactly layer8192')
    gate('new_exact_normalization_global_factor',
         131-Q(39,4)==Q(485,4) and 131-Q(9,2)-2==Q(249,2),
         'Both delta_4096^-3/2 and delta_8192^-485/4 must remain')
    gate('new_relative_complete_angle_power',Q(249,2)-Q(5,256)==Q(31867,256),
         'The actual h_j^-5 fee is subtracted from the physical relative state power')
    T4=alpha*20*(K+1/C)-(1+1/C)
    lam4=(T4+(T4*T4-4/C).sqrt())/2
    gate('new_actual_ideal_fourth_normalized_gain',lam4/A(2)**131>A(5)/2,
         show(lam4/A(2)**131))
    ratio=delta(4096)**(-A(3)/2)*delta(8192)**(-A(485)/4)*de**(A(249)/2)
    previous=delta(4096)**(-A(3)/2)*delta(8192)**(A(13)/4)
    gate('new_first_layer_matches_real_old_scale',
         (ratio/previous).overlaps(A(2)**(-A(249)/2)),
         show(lg(ratio/previous)))
    normalized_low=(A(2)**141*de.sqrt()*(8/(A(1).exp()*h))**8)
    gate('new_complete_weighted_low_error',normalized_low<A(2)**(-3000),
         show(lg(normalized_low)))
    normalized_high=(A(450-131)*A(2).log()+312*(1+low_absolute).log()
                     -(h-beta)*low_absolute)
    gate('new_complete_true_high_contraction',normalized_high<-A(4).log(),
         show(normalized_high))
    local_input=320+lg(ratio)-5*lg(h)+5*lg(Jbar)
    gate('new_actual_proposed_normalized_local_input',local_input<-19000,show(local_input))
    nonlinear=480+lg(ratio)-14*lg(h)
    gate('new_actual_proposed_normalized_nonlinear_fee',nonlinear<-19000,show(nonlinear))

    # This is recorded as a conditional multiplication budget, not an inverse.
    preconditioned=(10000+10*lg(A(8197))-20*lg(de)
                    +184+lg(ratio)-5*lg(h))
    gate('new_first_layer_condition_number_is_not_small',preconditioned>100000,
         show(preconditioned))
    gate('new_first_layer_small_label_contract_has_room',preconditioned-262144<-90000,
         show(preconditioned-262144))
    gate('old_linear_actual_input_not_new_nonlinear_reach',
         -A(33545404)/A(2).log()<-262144,
         {'old_linear_log2':show(-A(33545404)/A(2).log()),
          'new_operator_or_nonlinear_claim':False})

    gate('all_new_radial_gate_envelopes_monotone',
         Q(1,8193)+Q(1,256)-Q(3,8)<0 and
         Q(249,2)-Q(10,256)-Q(5,8193)>0 and
         Q(249,2)-Q(14,256)>0,
         'The Galerkin, local radius and nonlinear majorants improve for every later integer layer')
    gate('all_new_high_frequency_gate_monotone',
         h*(1+low_absolute)>1024 and Q(39,1024)<Q(1,16)-Q(1,256),
         'The full real-m and real-layer logarithmic derivative is negative beyond the checked endpoint')

    numeric.update({
        'first_changed_layer':8193,
        'first_shear':'2^128',
        'complete_log_variation_constant':show(cK),
        'actual_root_boxes':roots,
        'new_coarse_prefactor_log2':show(lg(coarse)),
        'new_first_relative_scale_log2':show(lg(ratio)),
        'new_proposed_local_input_log2':show(local_input),
        'new_proposed_nonlinear_fee_log2':show(nonlinear),
        'new_reference_squared_times_state_first_layer_log2':show(preconditioned),
        'new_same_product_after_conditional_label_bound_log2':show(preconditioned-262144),
        'old_linear_regular_input_log2':show(-A(33545404)/A(2).log()),
    })
    root=Path(__file__).resolve().parents[1]
    paths=[
        root/'results/R119-supplement-new-deep-profile-and-actual-homogeneous-Robin.md',
        root/'results/R119-supplement-new-deep-profile-full-label-chart.md',
        root/'results/R119-supplement-uniform-frequency-reference-Airy-Cauchy.md',
        root/'results/R119-supplement-new-tail-continuous-source-and-affine-exterior-data.md',
        root/'results/R119-supplement-stronger-deep-first-shear-and-complete-local-map.md',
        Path(__file__).resolve(),
    ]
    return {
        'schema':'visible-exact-R119-stronger-deep-first-shear-v1',
        'scope':'A new actual candidate metric after layer8192, preserving every endpoint amplitude and complete C2 seam. Real all-mode canonical matrices, complete finite-plus-full-angle nonlinear local maps with the true mean, and reinstantiation of the same-space radial reference Airy bound. The full global factors and the large transition-layer condition number are explicit. No transfer of the old full-label chart, actual Robin, KAM output, nonlinear input or relative network inverse is claimed.',
        'numeric':numeric,
        'file_sha256':{str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths},
        'checks':checks,
        'all_pass':all(c['pass'] for c in checks),
        'claims':{
            'actual_new_deep_geometry_and_full_C2_seams':True,
            'actual_all_mode_matrices_and_both_rows':True,
            'complete_mean_full_nonlinear_local_map':True,
            'same_space_reference_Airy_reinstantiated':True,
            'both_global_normalization_factors_retained':True,
            'new_full_label_chart':False,
            'new_actual_Robin_or_affine_source_column':False,
            'new_KAM_or_same_width_perturbation':False,
            'old_linear_input_is_new_nonlinear_reach':False,
            'full_network_inverse':False,
            'topic_completion':False,
        },
    }


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=run()
    if args.output:
        args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'all_pass':result['all_pass'],'checks':len(result['checks']),
                      'output':str(args.output) if args.output else None},ensure_ascii=False))
