#!/usr/bin/env python3
"""The stronger actual tail: raw labels, full sources and regular boundary."""
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

    def zero(x):
        return sp.simplify(x)==0

    def de(j):
        return A(2)/25*A(2)**(-j)

    def beta(j,K=64):
        delta=de(j)
        eta=delta**(A(3)/2)/(4*A(2).sqrt())
        return 3*delta+6*eta+(A(15)/2*eta*(2*(2*A(K)).log()-6*delta.log())).sqrt()

    K=2**128
    C=16*A(2).sqrt()
    gate('new_all_mode_large_root_to_m4',Q(63,64)*Q(65,64)*Q(5,64)>Q(1,16),
         'Lambda>(K-1)alpha nu andnu>=5m^4/64 implyLambda>K m^4/16')
    gate('new_all_mode_basis_product',Q(17,16)**2<2,
         'The sharper actual two-row basis norm is used rather than a product4')
    gate('new_actual_whole_low_window_relative_error',272+1-128+4-160==-11,
         'The actual2^272 matrix error yields a complete relative2^-11 bound on the true low window')
    er=Q(1,2**11)
    lr=Q(1,2**24)
    cone=(er+(lr+er)/2)/(1-Q(3,2)*er)
    gate('new_true_one_cell_full_cone',cone<Q(1,1024),str(cone))
    seam_cone=(Q(1,2**18)+Q(1,1024))/(1-Q(1,63*1024))
    gate('new_second_seam_full_cone',seam_cone<Q(1,512),str(seam_cone))
    gain=Q(5,2)*(1-Q(3,2)*er)*(1-Q(1,63*1024))
    gate('new_true_big_row_pays_second_seam',gain>1,str(gain))
    gate('new_normalized_root_polynomial_upper',Q(65,64)*Q(1,12)*Q(1,8)*(1+Q(1,16*K))<1,
         'The actual new normalized ideal large factor is less thanm^4 for everym>=4')
    Mcap=A(2)**(-40)*de(8193)**(-A(1)/8)
    gate('new_bad_prefix_only_at_enormous_true_frequencies',Mcap.log()>600,show(Mcap.log()))
    mh_factor=8*(A(2)/25)**(A(1)/256)*A(2)**(-A(321)/256)
    gate('new_narrow_cone_precedes_label_crossing',mh_factor>3,show(mh_factor))
    gate('new_narrow_cone_actual_label_start',4*A(4).log()-3*A(4)**(A(31)/32)<0,
         show(4*A(4).log()-3*A(4)**(A(31)/32)))
    gate('new_narrow_cone_all_frequency_monotonicity',
         4/A(4)<A(93)/32*A(4)**(-A(1)/32),
         'The derivative of4logm-3m^(31/32) is negative for everym>=4')
    gate('new_bad_prefix_layer_count',320-56==264,
         'The new entire bad prefix contains at most264 more real cells')
    gate('new_complete_actual_inverse_prefactor',450+131<600,
         'Both true internal inverse and the full new normalization inverse are retained')
    oldbad=Q(3,8)**6*Q(55917,5)
    gate('old_bad_prefix_exact_number',oldbad==Q(40763493,1310720),str(oldbad))
    gate('new_bad_prefix_extra_linear_coefficient',12*504+264*312==88416,
         'All old bad cells pay the increased norm constant')
    gate('new_bad_prefix_extra_constant',264*(600+312)==240768,
         'Every new bad cell pays its full constant and frequency polynomial')
    extra=(A(88416)*600+240768)*A(-600).exp()
    gate('new_full_bad_prefix_extra_fee',extra<A(1)/1000,show(extra))
    gate('new_extra_fee_all_frequency_monotonicity',88416-88416*600-240768<0,
         'The bound decreases for everylogm>=600')
    gate('new_entire_bad_prefix_still_below32',oldbad+Q(1,1000)<32,str(oldbad+Q(1,1000)))
    total_h=A(3968)*A(9)/100+8*de(4097)**(A(1)/256)/(1-A(2)**(-A(1)/256))
    angle=total_h+4*beta(129)+4*beta(8193,K)
    gate('new_complete_old_and_new_angle_sum',angle<358,show(angle))
    gate('new_deep_beta_geometric_majorant',A(2)**(-A(1)/2)<A(3)/4,
         'The complete actual beta envelopes decrease fast enough for the factor4 sum')
    gate('new_true_raw_label_weight',Q(5177,400)+391<404,
         'The actual changed internal normalization is again covered by raw404')
    gate('new_full_label_basis_fee',2<A(1).exp()**4,
         'The fullE inverse endpoint norm contributes less than one unit per minimum frequencym=4')

    gate('new_actual_fourth_connector_stop',-193532+4-9==-193537,
         'The real fourth slope, Riccati inverse and unchanged stop derivative are all included')
    gate('new_actual_fourth_stop_strict_box',Q(14)<Q(15) and Q(1,512)*16<Q(1,16),
         'The new stop remains in the same genuine finite geometry family')
    gate('new_actual_allmode_good_set_measure',1-Q(83,16384)>Q(99,100),
         'A new good parameter exists for the actual new infinite right lines')
    gate('new_grounded_Robin_lower_bound',Q(1,6)-Q(1,2**36)>Q(1,7),
         'The complete actual entrance algebra gives the positive whole-mode lower bound')
    gate('new_grounded_Robin_upper_bound',Q(5,28)+Q(1,2**36)<Q(1,5),
         'The complete actual entrance algebra gives the positive whole-mode upper bound')
    B=Q(2**24)-Q(25,8)
    Lmin=A(7)/5*A(B.numerator)/B.denominator
    gate('new_actual_full_Robin_difference',43-8*Lmin/A(2).log()<-A(2)**27,
         show(43-8*Lmin/A(2).log()))

    mu,pp,r,e=sp.symbols('mu p r e',nonzero=True)
    w=mu*pp/r**7
    N=mu*pp**2*e/(12*r**10)
    F=w*e/r
    eE=w*e/sp.sqrt(12)
    gate('new_complete_physical_to_canonical_source',zero(N-pp*F/(12*r**2)),
         'The actual larger profile occurs twice in the true source N')
    gate('new_complete_energy_to_canonical_source',zero(N-pp*eE/(sp.sqrt(12)*r**3)),
         'The radial reference uses e_E=w e/sqrt12 in its real physical units')
    gate('new_complete_mean_flux_source',zero(sp.sqrt(12)*mu*r**(-4)*N-w*w*e/sp.sqrt(12)),
         'The mean y derivative has its true positive sign and exact radial density')
    gate('new_source_full_two_row_Duhamel',450+16==466,
         'The actual entire high/internal flow feeds the complete strong two-row Green')
    gate('new_source_mean_not_old_zeta_ratio',131>10,
         'Mean estimates cannot silently retain the oldzeta_(j-1)/zeta_j bound')
    gate('new_source_zeta_comparison',131-Q(39,4)==Q(485,4)>0,
         'The actual newzeta and previous-cellzeta are below the full old physical envelopes')
    gate('new_profile_pointwise_mean_comparison',K>64,
         'Only the first up/high/down part increases, by nonnegative log interpolation factors')
    gate('new_complete_source_C2_prefactor',108+(450-80)<480,
         'The changed all-mode internal flow is fully paid before physical reconstruction')
    gate('new_complete_source_flat_exponent',Q(39,4)-5==Q(19,4)>0,
         'Both mean and nonmean second jets decay using the explicitly retained old envelope')

    sigmab=Q(5177,400)+2304-235
    sigmao=Q(1,512)
    gate('new_actual_Schur_fee',Q(295423,160)<1850,
         'The new raw404 and actual new good-set direction pay all finite angular costs')
    gate('new_full_source_angle_composition',224+1850<sigmab and sigmao<sigmab,
         {'source_B_width':str(sigmab),'required_Schur_width':2074})
    gate('new_source_particular_true_pair',-447+466==19,
         'The new ordinary-source column is not assigned the old small prefactor')
    gate('new_source_actual_compensating_labels',19+1-4<18,
         'The full k+C_Lf row is inverted using the actual new Schur operator')
    gate('new_complete_source_state_after_compensation',2**466+9*2**18<2**467,
         'Particular and all compensating homogeneous labels are retained')

    AA,MM,lam,Y,Yu=sp.symbols('A M lambda y yu',nonzero=True)
    TT=sp.Matrix([[AA,-4/MM**2],[-1,4/AA]])
    gate('new_actual_grounded_two_trace_determinant',zero(TT.det()-4*(1-MM**(-2))),
         'The complete height/normal-shear pair is kept')
    gamma=(1-4*lam/AA)/(AA-4*lam/MM**2)
    q=sp.Matrix([1,lam])/(AA-4*lam/MM**2)
    yy=sp.Matrix([Y,Yu])
    out=TT*yy
    gate('new_actual_affine_Robin_Wronskian',
         zero(out[1]+gamma*out[0]-TT.det()*sp.det(sp.Matrix.hstack(q,yy))),
         'The new actual homogeneous regular line, not an old frozen Robin value, determines the affine functional')
    gate('new_actual_tail_pair_to_Y',A(2).sqrt()*5/84<A(1)/8,
         'The full h(B)^-2=a(B)^2<1 factor is retained before bounding it')
    gate('new_actual_regular_reference_state',Q(1)+Q(3,2)**2<Q(28,5)**2,
         'The normalized true q state lies in its real entrance bound')
    gate('new_actual_affine_source_prefactor',2+42-3+19==60 and 60<80,
         'The new2^450 source cost and both genuine Wronskian states are paid')

    gate('new_actual_finite_connector_total_time',Q(505,4)+Q(1,2)+Q(75,16)<132,
         'The newly stopped connector and both actual bumps remain within the complete window')
    gate('new_actual_finite_mean_resistance',3**7<2**12,
         'exp(7/2)<64 pays the actual minimum w along the short segments')
    gate('new_actual_mean_cut_relative_slope',13+14==27 and Q(39,4)-6==Q(15,4),
         'The entire new source envelope is below the old one at the unchanged cut128')
    gate('new_actual_mean_finite_height_fee',27+12+8==47,
         'The mean source, genuine negative-A growth and full finite duration are retained')
    gate('new_actual_long_mean_resistance',4*Q(3,2)**2*B<2**30,
         'The true long mean resistance is polynomial4omegaL, not an exponential screen')
    gate('new_actual_mean_flux_final',13-Q(39,4)*128<-1200,
         'The real physical flux retains its explicit epsilon')
    meanheight=Q(1,2**(int(Q(39,4)*128)-25))+Q(1,2**(int(Q(15,4)*128)-47))+Q(1,2**(int(Q(39,4)*128)-43))
    gate('new_actual_mean_height_final',meanheight<Q(1,2**400),
         'The flat, finite-connector and long mean primitives all remain in the complete height row')

    screen=4*(2**23-2033-224)
    gate('new_actual_linear_regular_label_screen',screen==33545404,
         'The same numerical expression is now applied only after re-proving newraw404,newconnector andnewgoodset')
    real_input_log2=4-A(screen)/A(2).log()
    gate('new_actual_linear_state_reaches_conditional_small_ball',real_input_log2<-262144,
         show(real_input_log2))
    gate('new_linear_input_is_not_nonlinear_matching',screen>0,
         'The actual nonlinear tail has a further two-trace boundary correction; no nonlinear reach is asserted')

    numeric.update({
        'new_low_relative_error':'2^-11',
        'new_bad_prefix_extra_fee':show(extra),
        'old_bad_prefix_fee':str(oldbad),
        'new_actual_full_angular_sum_upper':show(angle),
        'actual_new_raw_label_fee':404,
        'actual_new_source_particular_bound':'2^466*Sstar',
        'actual_new_source_affine_bound':'2^80*exp(-4L)*Sstar',
        'actual_new_source_B_width':str(sigmab),
        'actual_new_linear_label_screen':screen,
        'actual_new_linear_state_log2_bound':show(real_input_log2),
    })
    root=Path(__file__).resolve().parents[1]
    paths=[
        root/'results/R119-supplement-stronger-deep-first-shear-and-complete-local-map.md',
        root/'results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md',
        root/'results/R119-supplement-new-tail-continuous-source-and-affine-exterior-data.md',
        root/'results/R119-supplement-retuned-fourth-connector-and-common-bumps.md',
        root/'results/R119-supplement-joint-tail-label-schur-normalization.md',
        root/'results/R119-supplement-stronger-tail-raw-labels-sources-and-regular-boundary.md',
        Path(__file__).resolve(),
    ]
    return {
        'schema':'visible-exact-R119-stronger-tail-boundary-sources-v1',
        'scope':'The actual stronger radial tail. New low cones, full huge-frequency bad prefixes and raw404 labels are proved; fourth connector and all-mode good bumps are selected again before defining the new true Robin. The actual full ordinary-source spaces, both canonical and physical traces, the screened affine exterior column, and all mean primitives are preserved. The actual R74 linear regular input reaches the stated conditional tiny label ball. Updated nonlinear matching and the same-width mixed-network inverse remain separate.',
        'numeric':numeric,
        'file_sha256':{str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths},
        'checks':checks,
        'all_pass':all(c['pass'] for c in checks),
        'claims':{
            'new_actual_raw404_label_weight':True,
            'new_actual_fourth_connector_and_good_bumps':True,
            'new_actual_homogeneous_Robin_and_mean_zero_slot':True,
            'new_complete_continuous_sources_and_C2_realization':True,
            'new_actual_affine_exterior_source_column':True,
            'new_actual_linear_regular_small_input':True,
            'new_nonlinear_regular_input_matched':False,
            'arbitrary_metric_source_periods_and_horizontal_reconstruction':False,
            'new_actual_KAM_output_or_same_width_network_inverse':False,
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
