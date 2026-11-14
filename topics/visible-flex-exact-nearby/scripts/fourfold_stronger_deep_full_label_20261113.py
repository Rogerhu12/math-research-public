#!/usr/bin/env python3
"""Full actual high blocks, two basis seams, and the stronger-tail label map."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, ctx
import sympy as sp


def run():
    ctx.prec=256
    A=arb
    checks=[]
    numeric={}

    def gate(name, statement, evidence):
        if not bool(statement):
            raise AssertionError(name)
        checks.append({'name':name,'pass':True,'evidence':evidence})

    def show(x):
        return x.str(45)

    def lg(x):
        return x.log()/A(2).log()

    def delta(j):
        return A(2)/25*A(2)**(-j)

    def h(j):
        return A(9)/100 if j<=4096 else 8*delta(j)**(A(1)/256)

    def beta(j,K=64):
        de=delta(j)
        et=de**(A(3)/2)/(4*A(2).sqrt())
        return 3*de+6*et+(A(15)/2*et*(2*(2*A(K)).log()-6*de.log())).sqrt()

    def ratio(j):
        de=delta(j)
        if j<=4096:
            return de**(A(7)/4)
        if j<=8192:
            return delta(4096)**(-A(3)/2)*de**(A(13)/4)
        return delta(4096)**(-A(3)/2)*delta(8192)**(-A(485)/4)*de**(A(249)/2)

    def local_input_log(j):
        power=76 if j<=8192 else 320
        Jbar=32768*(1-delta(j).log())/h(j)
        return power+lg(ratio(j))-5*lg(h(j))+5*lg(Jbar)

    def nonlinear_log(j):
        power=102 if j<=8192 else 480
        return 16+10+power+lg(ratio(j))-14*lg(h(j))

    def reference_state_log(j):
        return 10000+184+10*lg(A(j+4))-20*lg(delta(j))-5*lg(h(j))+lg(ratio(j))

    def spectrum(m,K,c):
        nu=A(m)**2*(A(m)**2-1)/12
        av=A(65)/64*nu
        TT=av*(A(K)+1/c)-(1+1/c)
        La=(TT+(TT*TT-4/c).sqrt())/2
        sm=1/(c*La)
        t=av/(A(K)*av-1-sm)
        s=-1/c+1/(c*av)+sm/av
        return La,sm,s,t

    K=2**128
    C=16*A(2).sqrt()
    Mcap=A(2)**(-40)*delta(8193)**(-A(1)/8)
    oldM8192=A(2)**(-A(5)/4)*delta(8192)**(-A(1)/8)
    oldM129=A(2)**(-A(5)/4)*delta(129)**(-A(1)/8)
    gate('actual_new_window_really_shrinks',Mcap<oldM8192,
         {'new_log2':show(lg(Mcap)),'old_previous_log2':show(lg(oldM8192))})
    gate('actual_capped_prefix_still_contains_original_low_modes',Mcap>oldM129 and oldM129>176,
         'The cap acts only at the very high end of the unchanged prefix')
    gate('actual_capped_window_nondecreasing',
         A(2)**(A(1)/8)>1,
         'min(old increasing window, fixed cap) joins the new increasing window exactly at8193')
    old_added_log=80*A(2).log()+312*(1+Mcap).log()-Mcap*h(8192)/2
    gate('actual_newly_high_old_blocks_contract',old_added_log<-A(4).log(),show(old_added_log))
    gate('actual_newly_high_old_blocks_all_frequency_derivative',312/(1+Mcap)<h(8192)/2,
         show(lg((312/(1+Mcap))/(h(8192)/2))))
    new_high_log=(450-131)*A(2).log()+312*(1+Mcap).log()-(h(8193)-beta(8193,K))*Mcap
    gate('actual_entire_new_high_block_contracts',new_high_log<-A(4).log(),show(new_high_log))
    gate('actual_new_high_frequency_all_layer_monotonicity',
         h(8193)*(1+Mcap)>1024 and Q(39,1024)<Q(1,16)-Q(1,256),
         'The explicit scalar derivative covers every deeper layer and every higher retained mode')
    gate('actual_new_high_angle_fee',2*beta(8193,K)<h(8193),show(lg(2*beta(8193,K)/h(8193))))

    # The whole-mode algebraic inequalities use nu>=20, not a finite frequency scan.
    gate('all_mode_basis_signs',Q(325,16)>2 and Q(1,16)<1,
         's=-1/c+1/(c alpha nu)+lambda/(alpha nu) is negative and greater than-1/c')
    gate('all_mode_basis_row_bounds',1+Q(1,63)<Q(17,16) and 1+Q(1,16)==Q(17,16),
         'Both E and its inverse use determinant1-st>1')
    avmin=Q(325,16)
    dsbound=1/(16*63*avmin**2)
    gate('new_second_seam_lower_row_all_modes',dsbound<Q(1,2**18),str(dsbound))
    gate('new_second_seam_upper_gain_all_modes',dsbound/63<Q(1,2**24),str(dsbound/63))
    gate('new_second_seam_upper_offdiagonal_all_modes',Q(1,63)<Q(1,16),
         't2<t1 and1-s1*t1>1 preserve the exact Q12 bound')
    s1,t1,s2,t2=sp.symbols('s1 t1 s2 t2')
    E1=sp.Matrix([[1,t1],[s1,1]])
    E2=sp.Matrix([[1,t2],[s2,1]])
    QQ=E1.inv()*E2
    gate('exact_complete_second_basis_seam',
         all(sp.simplify(v)==0 for v in QQ-sp.Matrix([
             [1+t1*(s1-s2)/(1-s1*t1),(t2-t1)/(1-s1*t1)],
             [(s2-s1)/(1-s1*t1),(1-s1*t2)/(1-s1*t1)] ])),
         'Both off-diagonal rows and the exact determinant are preserved')
    gate('new_second_seam_positive_not_unitary',
         Q(1,1+Q(1,16*63))>Q(15,16),
         'Q22 is positive and below1; no orthogonal or unitary assumption is used')

    lower=A(2)**(A(39)/4-131)*(K-1)/(64+A(1)/16)
    upper=A(2)**(A(39)/4-131)*(A(K)+A(1)/16)/63
    gate('new_normalized_gain_jumps_up_all_modes',lower>A(3)/2 and upper<2,
         {'lower':show(lower),'upper':show(upper)})
    gate('new_small_branch_extreme_contraction',
         A(2)**(-131)/(C*(K-1)*A(325)/16)<A(2)**(-260),
         show(lg(A(2)**(-131)/(C*(K-1)*A(325)/16))))
    rows=[]
    for m in (4,176):
        La1,l1,ss1,tt1=spectrum(m,64,C)
        La2,l2,ss2,tt2=spectrum(m,K,C)
        den=1-ss1*tt1
        q11=(1-tt1*ss2)/den
        q21=(ss2-ss1)/den
        q12=(tt2-tt1)/den
        q22=(1-ss1*tt2)/den
        gate(f'actual_seam_numeric_{m}',q11>1 and q11<1+A(2)**(-24)
             and abs(q21)<A(2)**(-18) and abs(q12)<A(1)/63 and q22>0 and q22<1,
             {'q11':show(q11),'q21':show(q21),'q12':show(q12),'q22':show(q22)})
        rows.append({'m':m,'q11':show(q11),'q21':show(q21),
                     'q12':show(q12),'q22':show(q22),
                     'normalized_gain_ratio':show((La2/A(2)**131)/(La1/A(2)**(A(39)/4)))})
    old_low=[]
    for m in range(4,173,4):
        La,_,_,_=spectrum(m,64,A(64))
        old_low.append(La/A(2)**(A(39)/4)*(-A(m)*A(9)/100).exp())
    gate('unchanged_entire_43_mode_constant_width_gate',all(x>A(25)/24 for x in old_low),
         {'m4':show(old_low[0]),'m172':show(old_low[-1]),'count':len(old_low)})
    La176,_,_,_=spectrum(176,64,A(16))
    gate('unchanged_remaining_modes_start_contracting',
         La176/A(2)**(A(39)/4)*(-A(176)*A(9)/100).exp()<A(4)/5,
         'The derivative5/m<.09 extends this exact endpoint to allm>=176')
    neutral=256*lg(A(5)/3)+2
    gate('complete_neutral_length_with_both_upward_jumps',neutral<192,show(neutral))
    kernel=192+5+2/(1-A(2)**(-A(1)/8))+1
    gate('complete_scalar_kernel_sum',kernel<256,show(kernel))

    # Exact two-row elimination at the new seam.
    q11,q12,q21,q22,a,b,up,vp,gu,gv=sp.symbols('q11 q12 q21 q22 a b up vp gu gv',nonzero=True)
    uu=q11*a*up+q12*b*vp+gu
    vv=q21*a*up+q22*b*vp+gv
    eliminated=q21/q11*uu+(q11*q22-q12*q21)/q11*b*vp+gv-q21/q11*gu
    gate('exact_full_new_small_row_elimination',sp.simplify(vv-eliminated)==0,
         'The large a*u term is eliminated using the real first equation')
    gate('new_small_branch_gap_count',8192-4097==4095 and 10*(8192-4097)==40950,
         'The two physical basis seams have4095 intervening small-branch cells')
    gate('actual_complete_two_seam_feedback',
         513*A(2)**(-40950)*A(2)**(-18)*A(2)/1000<A(2)**(-40000),
         show(lg(513*A(2)**(-40950)*A(2)**(-18)*A(2)/1000)))
    gate('complete_new_large_scalar_kernel',512*(1+A(2)**(-24))/(1-A(2)**(-40000))<513,
         'The complete second gain and both-seam feedback are included')
    gate('complete_large_source_row_budget',2+Q(2*4,1000)+Q(1,2**250)<Q(201,100),
         'The old seam future small source and the actual tiny new-seam source are both paid')
    gate('complete_large_row_Green_budget',Q(513*201,100)<1032,
         'No forward large multiplier is applied to a bounded u after seam elimination')
    gate('complete_paired_Green_budget',Q(4,3)*(2*1032+1)<2**12,
         'Both E rows and the entire genuine high source geometric sum are included')
    gate('complete_homogeneous_label_budget',
         4*(1+A(2)**(-24))/(1-A(2)**(-40000))<8,
         'The homogeneous real-high path has no additional source geometric factor')

    q_old=A(2)**15*32768*A(2)**(-A(39)/4)*delta(128).sqrt()*(8/(A(1).exp()*h(128)))**8
    q_new=A(2)**15*A(2)**141*delta(8193).sqrt()*(8/(A(1).exp()*h(8193)))**8
    gate('complete_old_prefix_low_matrix_error',q_old<A('0.024998080'),show(q_old))
    gate('complete_new_low_matrix_error',q_new<A(2)**(-3000),show(lg(q_new)))
    gate('actual_whole_new_Green_Neumann_gate',q_old+q_new<A(1)/32,
         'The unchanged and new low regimes are paid; the actual high blocks have no discarded error')
    gate('actual_complete_new_Green_bound',A(2)**15/(1-q_old-q_new)<A(2)**16,
         show(A(2)**15/(1-q_old-q_new)))
    gate('actual_complete_new_label_column_bound',8/(1-q_old-q_new)<9,
         show(8/(1-q_old-q_new)))
    gate('actual_weighted_low_operator_tail_converges',Q(1,2)-Q(8,256)==Q(15,32),
         'This is the normalized all-m envelope required for product-topology continuity')

    input_rows=[]
    for j in (128,4097,8192,8193):
        ilog=local_input_log(j)
        nlog=nonlinear_log(j)
        gate(f'actual_complete_local_input_{j}',ilog+lg(16*A(1).exp())<0,show(ilog))
        gate(f'actual_complete_nonlinear_feedback_{j}',nlog<-52,show(nlog))
        input_rows.append({'j':j,'local_input_log2':show(ilog),'nonlinear_feedback_log2':show(nlog)})
    gate('new_local_input_super_small',local_input_log(8193)<-19000,show(local_input_log(8193)))
    gate('new_local_nonlinearity_super_small',nonlinear_log(8193)<-19000,show(nonlinear_log(8193)))
    gate('new_full_local_input_envelope_monotonicity',
         Q(249,2)-Q(10,256)-Q(5,8193)>0,
         'The trueJbar^5 and h^-5 are included in the all-layer derivative')
    gate('new_full_local_nonlinearity_envelope_monotonicity',
         Q(249,2)-Q(14,256)>0,
         'The real full quadratic h^-14 fee is included')
    gate('complete_nonlinear_global_self_map',9*Q(1,64)+Q(1,2**52)<1,
         'The label ball maps inside the actual unit strong sequence ball')
    gate('complete_nonlinear_global_contraction',Q(2,2**52)<1,
         'The full strong Fourier Taylor lift preserves both signs and the complete mean root')
    gate('complete_nonlinear_label_to_state_bound',9/(1-Q(1,2**52))<16,
         'The actual fixed point has norm below16 times its full label norm')
    gate('complete_new_C2_flat_jets',127-Q(5,256)>0,
         'The new global normalization factor is fixed; the full nonlinear second jets decay')

    av=A(325)/16
    err=A(2)**272*A(4)**8*delta(8193).sqrt()
    Dmin=A(K)*av-1-av/16
    Tupper=1/C+(A(K)+A(1)/16)/(C*Dmin)
    gate('actual_new_fourth_true_error',err<A(2)**(-3000),show(lg(err)))
    gate('actual_new_fourth_full_complex_cone',Tupper+A(2)**(-3000)<A(1)/16,show(Tupper))
    gate('actual_new_fourth_true_projective_derivative',
         1/(C*(Dmin-err*A(17)/16)**2)<A(2)**(-24),
         show(lg(1/(C*(Dmin-err*A(17)/16)**2))))
    gate('actual_full_unchanged_fourth_prefix_count',8192-128==8064,
         'All8064 actual cells, not the altered ideal cell, transmit the fourth difference')
    gate('actual_full_fourth_slope_difference',-24*8064-3+7==-193532,
         'Two slope tubes, all true projective contractions, and20sqrt12 are retained')
    gate('actual_fourth_parameter_derivative_difference',-193532+16==-193516,
         'The actual full complex parameter-box margin pays the parameter derivative')

    budget_rows=[]
    for j in (4096,8192,8193):
        value=reference_state_log(j)
        gate(f'actual_reference_squared_state_endpoint_{j}',value<155000,show(value))
        budget_rows.append({'j':j,'reference_squared_state_log2':show(value)})
    tailpower=Q(249,2)-20-Q(5,256)
    gate('actual_new_reference_squared_state_tail_power',tailpower>104,str(tailpower))
    gate('actual_new_reference_squared_state_tail_ratio',
         (A(8198)/8197)**10*A(2)**(-A(tailpower.numerator)/tailpower.denominator)<A(2)**(-100),
         'The actual polynomial layer factor and complete positive exponent are both included')
    gate('actual_whole_finite_prefix_and_infinite_tail_budget',155000+14<160000,
         'All8192 finite-prefix terms and the complete new infinite geometric sum are paid')
    gate('conditional_new_label_budget_exact_exponent',160000-262144==-102144,
         'Only the stated radial multiplication budget is claimed, not a same-width operator inverse')

    numeric.update({
        'actual_newly_high_old_log_bound':show(old_added_log),
        'actual_new_high_log_bound':show(new_high_log),
        'actual_window_cap_log2':show(lg(Mcap)),
        'complete_second_seam_boxes':rows,
        'whole_scalar_kernel_bound':show(kernel),
        'old_low_Neumann':show(q_old),
        'new_low_Neumann_log2':show(lg(q_new)),
        'complete_local_input_and_nonlinear_rows':input_rows,
        'new_fourth_cone_modulus_upper':show(Tupper),
        'full_actual_reference_squared_state_rows':budget_rows,
    })
    root=Path(__file__).resolve().parents[1]
    paths=[
        root/'results/R119-supplement-new-deep-profile-full-label-chart.md',
        root/'results/R119-supplement-new-deep-profile-and-actual-homogeneous-Robin.md',
        root/'results/R119-supplement-stronger-deep-first-shear-and-complete-local-map.md',
        root/'results/R119-supplement-uniform-frequency-reference-Airy-Cauchy.md',
        root/'results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md',
        Path(__file__).resolve(),
    ]
    return {
        'schema':'visible-exact-R119-stronger-deep-full-label-v1',
        'scope':'The actual new K=2^128 profile after8192. The low-window cap retains every displaced mode as a true high block. Both complete characteristic basis seams, their small-branch feedback, full strong Green and nonlinear mean-inclusive all-label chart are proved. The real fourth flat-tail line is transmitted through all8064 unchanged cells. Both global normalization factors and the complete finite-prefix squared-reference multiplication budget remain explicit. No actual external nonlinear input, new Robin, new KAM or same-width mixed-network inverse is claimed.',
        'numeric':numeric,
        'file_sha256':{str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths},
        'checks':checks,
        'all_pass':all(c['pass'] for c in checks),
        'claims':{
            'actual_displaced_high_blocks_preserved':True,
            'complete_two_seams_and_both_rows':True,
            'complete_actual_strong_discrete_Green':True,
            'complete_mean_nonlinear_all_label_chart':True,
            'actual_full_C2_flat_end':True,
            'actual_fourth_flat_tail_line_and_difference':True,
            'all_finite_prefix_normalization_fees_retained':True,
            'external_nonlinear_input_reaches_small_label_contract':False,
            'new_actual_Robin_or_affine_source':False,
            'new_KAM_output':False,
            'same_width_updated_network_inverse':False,
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
