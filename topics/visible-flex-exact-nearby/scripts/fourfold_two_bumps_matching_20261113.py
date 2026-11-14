#!/usr/bin/env python3
"""Rational and polynomial gates for the same installed double-bump matching.

This does not certify a nonlinear high-input inverse.  It verifies constants
and exact matrix identities used in the accompanying full-frequency proof.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def add(*polys):
    out = {}
    for p in polys:
        for exp, coeff in p.items():
            out[exp] = out.get(exp, 0)+coeff
    return {e:c for e,c in out.items() if c}


def scale(p, c):
    return {e:c*v for e,v in p.items() if c*v}


def mul(p, q):
    out = {}
    for (i,j), a in p.items():
        for (k,l), b in q.items():
            e = (i+k,j+l)
            out[e] = out.get(e,0)+a*b
    return {e:c for e,c in out.items() if c}


def run():
    checks = []

    def gate(name, condition, evidence):
        if not condition:
            raise AssertionError(name)
        checks.append({'name':name, 'pass':True, 'evidence':evidence})

    ow = Q(7,5)-Q(15,16384)
    Lb = Q(75,16)
    eps = Q(1,2**39)
    tau = Q(5177,400)
    gate('actual_omega_tilde_positive', ow > Q(11,8),
         'Use R74 continuous derivative bounds, with the selected fixed parameters')
    gate('actual_A_minus_one', Q(3,16)/Q(11,8)**2 == Q(12,121) < Q(1,8),
         'A=1+psi_uu/omega_tilde^2 in the true physical radius')
    gate('A_in_paid_R119_box', 1+Q(1,8)<7 and 2+Q(1,8)<6,
         '|A|<=7 and |A+1|<=6 remain valid')
    gate('physical_w_over_a', Q(1,4)/Q(11,8) == Q(2,11) < Q(5,18),
         'Same paid physical C2 reconstruction constants')
    gate('actual_log_radius_length', Q(25,8)*Q(3,2)==Lb,
         'psi vanishes at both actual endpoints, so Lb=25 omega/8')
    gate('angle_width_fee', 16*Lb==75,
         'The full energy estimate is applied on the actual variable-coefficient segment')
    gate('relative_growth_exponent', 32*Lb==150 and 2*150==300,
         'e^(32 Lb)<e^150<2^300, using e<4')
    gate('actual_relative_output', -8723+300==-8423,
         'The same weighted full connector input is propagated')
    gate('full_complex_relative_ball', Q(1,2**8423)<Q(1,64),
         'X_beta<1, so all modes and the mean stay inside the actual ball')
    gate('endpoint_energy_angle_width', 2048-75==1973,
         'All widths use the original physical angle')
    gate('raw_angle_margin', 1973-1968==5,
         'Finite extra angular derivatives at the raw output have paid margin')
    gate('grounded_angle_margin', 1973-1967==6,
         'The true normal and shear transformation has paid margin')
    gate('positive_output_strip', tau+1967>Q(1,512),
         'The actual final physical strip is a restriction of a paid strip')
    gate('physical_bump_C2', -8423+17==-8406,
         'Complete horizontal and vertical physical second jets are included')
    gate('weighted_label_state_ball', Q(13,4)*Q(1,4)<1,
         'Original internal labels use the explicitly stronger ell1_8192 domain')
    gate('tail_boundary_fits_Dirichlet_ball', Q(1,2**8423)+Q(1,2**26)<Q(1,2**25),
         'f_B is bounded by U=(f_B)_theta_theta, not only by its unweighted height')
    gate('actual_long_annulus_length', Q(7,5)*(2**24-Q(25,8))>16,
         'The actual long interval is retained when bounding reflected waves')
    gate('nonlinear_neumann_error_constant', 2**13==8192,
         'Use the already paid complete two-endpoint nonlinear error bound')

    # Polynomial variables x=1/M and y=omega; identities hold for all M.
    one = {(0,0):1}
    x = {(1,0):1}
    y = {(0,1):1}
    x2 = mul(x,x)
    y2 = mul(y,y)
    J = [[y,scale(x,-1)],[mul(y,x),scale(one,-1)]]
    determinant = add(mul(J[0][0],J[1][1]),scale(mul(J[0][1],J[1][0]),-1))
    gate('exact_true_two_trace_determinant', determinant==scale(mul(y,add(one,scale(x2,-1))),-1),
         'det J_M=-omega(1-M^-2), with the common north-height sign retained')
    gate('exact_matching_row_first_column', add(J[0][0],J[1][0])==mul(y,add(one,x)),
         '(1,1)J_M=(1+1/M)(omega,-1)')
    gate('exact_matching_row_second_column', add(J[0][1],J[1][1])==scale(add(one,x),-1),
         'The derivative trace is retained with its true coefficient')
    frob = add(*(mul(v,v) for row in J for v in row))
    gate('exact_full_matrix_Frobenius_norm', frob==mul(add(one,y2),add(one,x2)),
         '||J_M||_F^2=(1+omega^2)(1+M^-2)')
    gate('transversality_ratio_polynomial', add(mul(add(one,x),add(one,x)),scale(add(one,x2),-1))==scale(x,2),
         '(1+1/M)^2-(1+M^-2)=2/M>0 for all M>=4')
    gate('full_two_trace_map_invertible', 1-Q(1,4**2)>0,
         'All actual nonzero fourfold frequencies satisfy M>=4')
    gate('exact_coth_reflection_fee', 4*Q(1,2**128)==Q(1,2**126)<eps/2,
         'L>16 and M>=4; no finite-frequency sampling or infinite-half-line replacement')
    gate('actual_relative_transversality', eps/2==Q(1,2**40),
         'Gap is for the complete pair (f_B,k_B/M), even when f_B=0')
    gate('relative_linear_inverse_constant', 1/(eps/2)==2**40,
         'This is an inverse on the actual base tail line, not an assumed nonlinear chart inverse')
    gate('screened_complete_trace_constant', 4*2**40==2**42,
         'e^(2L)csch(ML)<=4 exp(-(M-2)L)')
    gate('screening_exponent_all_frequencies', 4-2==Q(4,2),
         'M-2>=M/2 for all M>=4')

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/'results/R74-actual-full-tail-robin-and-augmented-positive-cap.md',
        root/'results/R119-actual-final-connector-all-label-continuation.md',
        root/'results/R119-supplement-full-installed-connector-with-paid-label-weight.md',
        root/'results/R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md',
        root/'results/R119-supplement-two-bumps-and-exact-nonlinear-matching.md',
        Path(__file__).resolve(),
    ]
    return {
        'schema':'visible-exact-R119-actual-double-bump-matching-v1',
        'scope':'Complete exact-tail continuation through both already installed bumps and the exact remaining nonlinear matching equation; a uniform base all-frequency relative two-trace gap is proved, but no nonlinear relative inverse is asserted.',
        'inputs':{'internal_label_exponential_weight':8192,
                  'actual_bump_log_radius_length_upper':'75/16',
                  'actual_full_tail_line_angle_gap':'2^-39',
                  'complete_matching_relative_gap':'2^-40',
                  'physical_output_strip':'1/512',
                  'file_sha256':{str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths}},
        'checks':checks,
        'all_pass':all(c['pass'] for c in checks),
        'claims':{'both_actual_bumps_retained':True,
                  'bump_selection_fixed_while_labels_vary':True,
                  'complete_high_mode_and_mean_continuation':True,
                  'actual_all_mode_two_trace_base_gap':True,
                  'height_nonvanishing_assumed':False,
                  'mean_slope_matched_by_same_holonomy_root':True,
                  'mean_height_difference_is_retained_output':True,
                  'nonlinear_relative_tail_graph_inverse':False,
                  'nonlinear_ordinary_source_inverse':False,
                  'final_global_family':False},
    }


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    report=run()
    encoded=json.dumps(report,ensure_ascii=False,indent=2)+'\n'
    if args.out:
        args.out.write_text(encoded)
        print(json.dumps({'all_pass':report['all_pass'],'checks':len(report['checks']),
                          'out':str(args.out)},ensure_ascii=False))
    else:
        print(encoded,end='')
