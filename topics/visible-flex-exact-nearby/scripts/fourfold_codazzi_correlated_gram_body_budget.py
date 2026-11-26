#!/usr/bin/env python3
"""Complete CV correlated Gram maximum and optimal root necessary screen.

Same-v four-vertex values on all4651 closed cells replace the old SG box.
The old SG result and X/Y/GB/RS are read unchanged, never recomputed.
Four changed body bounds and the R143 OC.5 diagnostic are saved whole;
the allowance is conditional on all body gates. Science is public Actions only.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import time


KIND = 'R143_complete_correlated_Gram_body_budget_v1'
BITS = 320
POSITIVE_SHA = 'ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d'
GERM_SHA = '397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864'
CANDIDATE_SHA = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
OBJECT_SHA = '91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
REPAIR_SHA = '440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
X_SHA = '1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec'
X_EXECUTION_SHA = '999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92'
Y_SHA = '19b489ce0b8b85d4223ea334f7e2397188755d42605bf7613d2023ac69cb2cf3'
Y_EXECUTION_SHA = '2e4cea611a229dbf894bae1fb2478ebc2219f9c0282a84cae1abd32ceb54f084'
GB_SHA = '5b5f374fb68e66ce25725195a9d574940e5ee7e9b273b6b55da90ada261ec492'
GB_EXECUTION_SHA = '9bc00f39ab9656ef3e3afbc64f3df20d8340bbe85b92be4bc17141a80f28a18f'
RS_SHA = 'e1b27ffa5759b9b55bc785ef17d362a67f1d370d5ae26e68b422922d9a0229d8'
RS_EXECUTION_SHA = 'ba15b1060c40e965b27cc325c7696a35202dbf54c83817dbfb508750acdf8f1c'
SG_SHA = '24c5923eb7a0b34c566c785ec11e33e7881b3ce6c35613a60cb9532238cf1b5e'
SG_EXECUTION_SHA = 'ce2787cd11267f3d47dcbab8f2dd76851ca64ebec09a72767bac313235f7438a'
ETA = Fraction(-7789843107295549, 4611686018427387904)
NU = Fraction(-2572625729470897, 72057594037927936)
ALPHA = Fraction(6890507429876859, 9007199254740992)
ROOT_LO = Fraction(1191984371497, 5000000000000)
ROOT_HI = Fraction(2383968743003, 10000000000000)
BODY_LEFT = Fraction(1192029371497, 5000000000000)
RIGHT = Fraction(25, 8)
REPAIR = Fraction(4, 10**18)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path, expected):
    raw = Path(path).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == expected,
            'whole original input identity: ' + Path(path).name)
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def save(path, document):
    raw = (json.dumps(document, ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode()
    temporary = Path(str(path)+'.partial')
    temporary.write_bytes(raw)
    temporary.replace(path)
    require(path.read_bytes() == raw, 'whole new scalar result exact byte readback')


def admit_inputs(args):
    """Pure restoration/metadata admission; no scientific module is imported."""
    positive = read(args.positive, POSITIVE_SHA)
    germ = read(args.germ, GERM_SHA)
    old_x = read(args.physical, X_SHA)
    execution = read(args.physical_execution, X_EXECUTION_SHA)
    require(positive.get('complete') is True
        and positive.get('coefficient_cover_complete') is True
        and positive.get('failure') is None
        and len(positive['rows']) == 4650
        and positive['identity']['candidate_sha256'] == CANDIDATE_SHA
        and positive['identity']['object_sha256'] == OBJECT_SHA
        and Fraction(positive['identity']['actual_alpha']) == ALPHA
        and Fraction(positive['identity']['actual_nu']) == NU
        and Fraction(positive['identity']['exact_eta_center']) == ETA
        and positive['whole_original_eta'] is True,
        'same complete original positive coefficient cover and fixed centre')
    require(germ.get('complete') is True and germ.get('proved') is True
        and germ.get('failure') is None
        and germ['candidate_sha256'] == CANDIDATE_SHA
        and germ['object_sha256'] == OBJECT_SHA
        and Fraction(germ['exact_amplitude']) == ALPHA
        and Fraction(germ['actual_fixed_nu']) == NU
        and Fraction(germ['exact_center_parameter']) == ETA
        and germ['whole_affine_parameter_interval'] is True
        and tuple(map(Fraction,germ['root_interval'])) == (ROOT_LO,ROOT_HI)
        and germ['actual_candidate_piece'] == 2549
        and germ['compact_bump_identically_zero_on_entire_actual_germ'] is True,
        'same complete true-root germ and independent moving mean')
    radial = tuple(map(Fraction,germ['complex_radial_rectangle']['real_interval']))
    scalar = tuple(map(Fraction,germ['original_scalar_germ']))
    require(radial[0] <= ROOT_LO < ROOT_HI < BODY_LEFT <= radial[1]
        and scalar[0] <= ROOT_LO < BODY_LEFT <= scalar[1],
        'entire uncertain-root collar is inside both original germ domains')
    require(old_x.get('complete') is True and old_x.get('proved') is True
        and old_x.get('failure') is None
        and old_x['completed_closed_cells'] == 4651,
        'whole completed original physical budget')
    xid = old_x['identity']
    require(xid['original_positive_sha256'] == POSITIVE_SHA
        and xid['original_germ_sha256'] == GERM_SHA
        and xid['original_candidate_sha256'] == CANDIDATE_SHA
        and xid['intrinsic_object_sha256'] == OBJECT_SHA
        and xid['exact_repair_definition_sha256'] == REPAIR_SHA
        and Fraction(xid['exact_alpha']) == ALPHA
        and Fraction(xid['exact_eta']) == ETA and Fraction(xid['exact_nu']) == NU
        and xid['exact_true_root_interval'] == [str(ROOT_LO),str(ROOT_HI)]
        and xid['fixed_point'] == '(0,0,1/2)'
        and Fraction(xid['full_repair_A0']) == REPAIR,
        'new spectral budget uses exactly the same actual Qrepair as X')
    for key in ('same_fixed_eta_nu_and_Qrepair', 'full_real_angular_circle',
                'true_root_not_replaced_by_interval_endpoint', 'complete_means_retained',
                'complete_original_interfaces_retained', 'actual_DF_not_WVC_hybrid'):
        require(old_x['scope'][key] is True, 'whole original physical qualification: '+key)
    require(old_x['scope']['full_positive_inverse_proved'] is False
        and old_x['scope']['final_topic_complete'] is False,
        'the completed original budget is not relabeled as a whole inverse')
    for key in ('old_scientific_target_calls', 'old_primitive_calls',
                'old_geometry_ODE_calls', 'published_Fourier_or_frame_arrays'):
        require(old_x[key] == 0, 'original X no-recomputation qualification')
    require(execution.get('complete') is True
        and execution.get('failure') is None
        and str(execution.get('run_id')) == '44737045152'
        and str(execution.get('run_attempt')) == '1'
        and execution.get('actual_child_returncode') == 0
        and execution.get('original_scientific_complete') is True
        and execution.get('original_scientific_failure') is None
        and execution.get('old_completed_targets_recomputed') == 0
        and execution.get('old_numerical_producers_called') == 0
        and execution.get('scientific_children') == 1
        and any(row.get('sha256') == X_SHA for row in execution.get('scientific_files',[])),
        'whole original X execution binds its exact complete scientific result')

    cutoff = RIGHT
    pieces = [(ROOT_LO,BODY_LEFT,-1,2549)]
    original_interfaces = []
    endpoint = BODY_LEFT
    for index,row in enumerate(positive['rows']):
        left,right = map(Fraction,row['interval'])
        require(left == endpoint and left < right,
                'all 4650 original closed rows form their complete exact ordered cover')
        require(row['fields_are_moving_phi_not_physical_theta'] is True
            and row['complete_primitive_intermediate_retained'] is True
            and row['complete_mean_column_retained'] is True,
            'each original row keeps the actual moving angle, primitive and full mean')
        endpoint = right
        if row['right_interface'] is not None:
            original_interfaces.append(row['right_interface'])
        if left < cutoff:
            pieces.append((left,min(right,cutoff),index,row['candidate_piece']))
    require(endpoint == RIGHT and len(original_interfaces) == 3594
        and pieces[0][0] == ROOT_LO and pieces[-1][1] == cutoff
        and all(pieces[j][1] == pieces[j+1][0] for j in range(len(pieces)-1)),
        'whole original cap including the entire uncertain-root germ is complete')
    partition = [[str(l),str(r),index,piece] for l,r,index,piece in pieces]
    partition_sha = hashlib.sha256(json.dumps(partition,separators=(',',':')).encode()).hexdigest()
    interface_sha = hashlib.sha256(json.dumps(original_interfaces,sort_keys=True,
                                            separators=(',',':')).encode()).hexdigest()
    require(interface_sha == xid['original_positive_interface_metadata_sha256'],
            'all original candidate/intrinsic interface metadata agree with X')
    return dict(positive=positive,germ=germ,old_x=old_x,execution=execution,
                pieces=pieces,cutoff=cutoff,partition_sha=partition_sha,
                interface_sha=interface_sha,original_interfaces=len(original_interfaces))


def admit_saved_budgets(args, admitted):
    """Whole prior-result admission only; all prior targets remain read-only."""
    old_x = admitted['old_x']
    old_y = read(args.composed,Y_SHA)
    old_gb = read(args.body_budget,GB_SHA)
    old_rs = read(args.root_screen,RS_SHA)
    records = (
        ('composed',old_y,read(args.composed_execution,Y_EXECUTION_SHA),
         '44740320925',Y_SHA,Y_EXECUTION_SHA),
        ('body_budget',old_gb,read(args.body_execution,GB_EXECUTION_SHA),
         '44745355257',GB_SHA,GB_EXECUTION_SHA),
        ('root_screen',old_rs,read(args.screen_execution,RS_EXECUTION_SHA),
         '44758362539',RS_SHA,RS_EXECUTION_SHA))
    for name,result,execution,run_id,native,exec_sha in records:
        require(result.get('complete') is True and result.get('proved') is True
            and result.get('failure') is None,
            'complete whole prior scientific result: '+name)
        require(execution.get('complete') is True and execution.get('failure') is None
            and str(execution.get('run_id')) == run_id
            and str(execution.get('run_attempt')) == '1'
            and execution.get('actual_child_returncode') == 0
            and execution.get('original_scientific_complete') is True
            and execution.get('original_scientific_failure') is None
            and execution.get('old_completed_targets_recomputed') == 0
            and execution.get('old_numerical_producers_called') == 0
            and execution.get('scientific_children') == 1
            and any(item.get('sha256') == native for item in execution.get('scientific_files',[])),
            'complete whole prior execution: '+name)
    require(old_y['completed_closed_cells'] == 4651
        and old_y['prior_complete_budget']['sha256'] == X_SHA
        and old_y['prior_complete_budget']['execution_sha256'] == X_EXECUTION_SHA
        and old_y['prior_complete_budget']['whole_original_scope_and_false_gates_retained'] is True
        and old_y['identity']['prior_complete_budget_sha256'] == X_SHA
        and old_y['identity']['prior_complete_execution_sha256'] == X_EXECUTION_SHA,
        'same complete X reference and its original outcomes retained by completed Y')
    for key in ('same_fixed_eta_nu_and_Qrepair','full_real_angular_circle',
                'true_root_not_replaced_by_interval_endpoint','complete_means_retained',
                'complete_original_interfaces_retained','actual_DF_not_WVC_hybrid',
                'complete_prior_X_outcome_preserved'):
        require(old_y['scope'][key] is True, 'original Y scope unchanged: '+key)
    for key in ('old_scientific_target_calls','old_primitive_calls','old_geometry_ODE_calls',
                'old_frame_propagation_steps','old_energy_constant_targets_recomputed',
                'published_Fourier_or_frame_arrays'):
        require(old_y[key] == 0, 'original Y no-recomputation scope')
    require(old_gb['saved_record_count'] == 6 and old_gb['actual_returncode'] == 0
        and old_gb['identity']['completed_X_budget_sha256'] == X_SHA
        and old_gb['identity']['completed_X_execution_sha256'] == X_EXECUTION_SHA
        and old_gb['identity']['completed_Y_budget_sha256'] == Y_SHA
        and old_gb['identity']['completed_Y_execution_sha256'] == Y_EXECUTION_SHA
        and old_gb['body_only_sufficient_comparison']['all_body_gates_pass'] is True
        and old_gb['scope']['new_body_Hhalf_bounds_proved'] is True
        and old_gb['scope']['root_Htwo_thirds_path_changed'] is False
        and old_gb['scope']['whole_environment_zero_mode_retained'] is True
        and old_gb['scope']['actual_DF_not_WVC_hybrid'] is True,
        'same completed original GB body budget and unchanged root-source path')
    require(old_rs['completed_common_cells'] == old_rs['expected_common_cells'] == 327
        and old_rs['completed_subcells'] == old_rs['expected_subcells'] == 10464
        and old_rs['identity']['old_X_sha256'] == X_SHA
        and old_rs['identity']['old_GB_sha256'] == GB_SHA
        and old_rs['identity']['original_positive_sha256'] == POSITIVE_SHA
        and old_rs['identity']['original_germ_sha256'] == GERM_SHA
        and old_rs['scope']['same_actual_Qrepair_and_original_full_high'] is True
        and old_rs['scope']['exact_independent_mean_and_original_all_interfaces_retained'] is True
        and old_rs['scope']['complete_integral_target_proved'] is True
        and old_rs['scope']['actual_positive_boundary_problem_singular'] is False
        and old_rs['scope']['positive_inverse_proved'] is False,
        'same completed whole RS necessary screen, never reevaluate its integral')
    old_sg = read(args.old_spectral,SG_SHA)
    sg_execution = read(args.old_spectral_execution,SG_EXECUTION_SHA)
    require(old_sg.get('complete') is True and old_sg.get('proved') is True
        and old_sg.get('failure') is None
        and old_sg['completed_closed_cells'] == 4651
        and old_sg['saved_record_count'] == 5
        and old_sg['identity']['original_positive_sha256'] == POSITIVE_SHA
        and old_sg['identity']['original_germ_sha256'] == GERM_SHA
        and old_sg['identity']['exact_repair_definition_sha256'] == REPAIR_SHA
        and old_sg['identity']['old_X_sha256'] == X_SHA
        and old_sg['identity']['old_Y_sha256'] == Y_SHA
        and old_sg['identity']['old_GB_sha256'] == GB_SHA
        and old_sg['identity']['old_RS_sha256'] == RS_SHA
        and old_sg['scope']['complete_whole_spectral_constant_proved'] is True
        and old_sg['scope']['complete_four_new_upper_bounds_proved'] is True
        and old_sg['scope']['positive_inverse_proved'] is False,
        'complete original SG upper, preserving its original success and scope')
    require(sg_execution.get('complete') is True and sg_execution.get('failure') is None
        and str(sg_execution.get('run_id')) == '44767124478'
        and str(sg_execution.get('run_attempt')) == '1'
        and sg_execution.get('actual_child_returncode') == 0
        and sg_execution.get('original_scientific_complete') is True
        and sg_execution.get('original_scientific_failure') is None
        and sg_execution.get('old_completed_targets_recomputed') == 0
        and sg_execution.get('old_numerical_producers_called') == 0
        and sg_execution.get('scientific_children') == 1
        and any(item.get('sha256') == SG_SHA for item in sg_execution.get('scientific_files',[])),
        'whole original SG execution binds its exact complete scientific result')
    records = records + (('old_spectral',old_sg,sg_execution,'44767124478',SG_SHA,SG_EXECUTION_SHA),)
    return old_y,old_gb,old_rs,old_sg,records


def run(args):
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
        and os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public',
        'new science runs only in this repository public Actions')
    require(not args.output.exists(), 'preserve every previous result or failed prefix')
    admitted = admit_inputs(args)
    old_y,old_gb,old_rs,old_sg,prior_records = admit_saved_budgets(args,admitted)
    from flint import arb,ctx
    ctx.prec = BITS
    began = time.monotonic()
    args.output.parent.mkdir(parents=True,exist_ok=True)

    def rat(value):
        value = Fraction(value)
        return arb(value.numerator)/value.denominator

    def old_ball(record):
        require('lower' in record and 'upper' in record, 'whole original signed endpoints')
        value = arb(record['lower']).lower().union(arb(record['upper']).upper())
        require(value.is_finite(), 'finite whole original scalar')
        return value

    def unpack(record):
        require(record.get('kind') == 'complete_decimal_ball_v1', 'complete decimal record kind')
        exponent = int(record['decimal_exponent'])
        scale = rat(10**exponent) if exponent >= 0 else rat(Fraction(1,10**(-exponent)))
        mid,radius = rat(int(record['midpoint_integer']))*scale,rat(int(record['radius_integer']))*scale
        require(radius >= 0, 'nonnegative complete saved radius')
        return (mid-radius).lower().union((mid+radius).upper())

    def recorded(value,direction='upper'):
        require(value.is_finite() and direction in ('upper','lower'), 'finite new directed scalar')
        mid,radius,exponent = value.mid_rad_10exp(75)
        record = dict(kind='complete_decimal_ball_v1',mathematical_direction=direction,
                      midpoint_integer=str(int(mid)),radius_integer=str(int(radius)),
                      decimal_exponent=str(int(exponent)))
        require(int(radius) >= 0 and unpack(record).contains(value),
                'complete saved scalar contains its original directed value')
        return record

    old_x = admitted['old_x']
    xs,xd = old_x['new_scalar_suprema'],old_x['complete_derived_energy_bounds']
    ys,yd = old_y['new_scalar_suprema'],old_y['complete_derived_energy_bounds']
    old_records = dict(C_E=xs['C_E'],C_H=xs['C_H'],A_Theta=xs['A_Theta'],
        Gamma=xd['Gamma'],h_B=xd['h_B'],E_0=ys['E_0'],E_1=ys['E_1'],
        h_E=yd['h_E'],r_E=yd['r_E'],r_B=yd['r_B'],
        w_B=old_gb['new_records']['wB_half_upper'],
        a_BB=old_gb['new_records']['aBB_upper'],
        RS_test_integral=old_rs['complete_test_integral'],
        old_C_spectral_upper=old_sg['new_records']['C_spectral_upper'])
    old = {name:unpack(value).upper() for name,value in old_records.items()}
    require(all(value > 0 for value in old.values()), 'complete positive old scalar inputs')
    require(unpack(old_records['RS_test_integral']).upper() < rat(125)
        and unpack(old_records['E_0']).lower() > rat(Fraction(693,500000))
        and unpack(old_records['E_1']).lower() > rat(Fraction(2719,1000))
        and unpack(old_records['h_E']).lower() > rat(Fraction(1869,10**6))
        and unpack(old_records['Gamma']).lower() > rat(Fraction(11839,10000))
        and unpack(old_records['A_Theta']).lower() > rat(Fraction(15794,10000))**2,
        'whole saved original records prove all RN necessary-screen premises')
    references = dict(physical_budget=dict(complete_result_sha256=X_SHA,
        complete_execution_sha256=X_EXECUTION_SHA,run_id='44737045152',run_attempt='1',
        whole_result_admitted=True,whole_execution_admitted=True,
        original_identity=old_x['identity'],original_scope=old_x['scope'],
        original_comparison=old_x['body_only_sufficient_comparison']))
    for name,result,execution,run_id,native,exec_sha in prior_records:
        references[name] = dict(complete_result_sha256=native,complete_execution_sha256=exec_sha,
            run_id=run_id,run_attempt='1',whole_result_admitted=True,whole_execution_admitted=True,
            original_identity=result['identity'],original_scope=result['scope'],
            original_comparison=result.get('body_only_sufficient_comparison',result.get('strict_gates')))
    identity = dict(kind=KIND,source_sha256=digest(__file__),arithmetic_bits=BITS,
        original_positive_sha256=POSITIVE_SHA,original_germ_sha256=GERM_SHA,
        original_candidate_sha256=CANDIDATE_SHA,intrinsic_object_sha256=OBJECT_SHA,
        exact_repair_definition_sha256=REPAIR_SHA,exact_alpha=str(ALPHA),
        exact_eta=str(ETA),exact_nu=str(NU),fixed_point='(0,0,1/2)',
        exact_true_root_interval=[str(ROOT_LO),str(ROOT_HI)],
        actual_spectral_domain='[r_star,25/8] x full original moving circle',
        conservative_radial_cover=[str(ROOT_LO),str(RIGHT)],
        original_positive_rows=4650,original_positive_interfaces=admitted['original_interfaces'],
        original_positive_interface_metadata_sha256=admitted['interface_sha'],
        complete_new_partition_sha256=admitted['partition_sha'],
        full_pair_repair_A0=str(REPAIR),support_lower='2/5',
        original_body_drift_anchor='psi(25/8)=identity',
        intended_root_receiver='independent true-root-anchored RA flow',
        old_X_sha256=X_SHA,old_X_execution_sha256=X_EXECUTION_SHA,
        old_Y_sha256=Y_SHA,old_Y_execution_sha256=Y_EXECUTION_SHA,
        old_GB_sha256=GB_SHA,old_GB_execution_sha256=GB_EXECUTION_SHA,
        old_RS_sha256=RS_SHA,old_RS_execution_sha256=RS_EXECUTION_SHA,
        old_SG_sha256=SG_SHA,old_SG_execution_sha256=SG_EXECUTION_SHA,
        complete_cell_majorant='CV.5 same-v four vertices; never SG.12',
        new_root_screen='R143 OC.5 optimized nonnegative direction')
    doc = dict(identity=identity,complete=False,proved=False,failure=None,
        stage='prepared-complete-new-correlated-gram-maximum',
        expected_closed_cells=4651,completed_closed_cells=0,
        current_exact_right=str(ROOT_LO),spectral_max_prefix=recorded(arb(0)),
        new_records={},saved_record_count=0,
        old_scientific_targets_called=0,old_CE_targets_recomputed=0,
        old_geometry_ODE_calls=0,old_residual_targets_recomputed=0,
        old_Gamma_and_root_trace_targets_recomputed=0,
        old_wB_aBB_targets_recomputed=0,old_RS_targets_recomputed=0,
        new_drift_or_capacity_ODE_calls=0,published_arrays=0,
        whole_original_references=references,reused_complete_scalar_records=old_records,
        body_only_sufficient_comparison=None,root_anchor_necessary_screen=None,
        conditional_root_allowance=None,
        scope=dict(same_actual_Qrepair_and_complete_mean=True,
            original_true_root_and_all_interfaces_retained=True,
            original_body_drift_and_environment_zero_mode_retained=True,
            original_H_source_and_root_Htwo_thirds_path_retained=True,
            complete_whole_spectral_constant_proved=False,
            complete_five_new_upper_bounds_proved=False,
            optimized_root_budget_certifiably_excluded=False,
            conditional_new_root_allowance_proved=False,
            root_anchored_receiver_necessary_conditions_pass=False,
            any_necessary_condition_certifiably_violated=False,
            original_Gamma_root_receiver_route_not_reopened=True,
            actual_local_root_drift_not_recomputed=True,
            actual_capacity_or_finite_receiver_Gram_paid=False,
            root_boundary_form_paid=False,positive_inverse_proved=False,
            actual_positive_boundary_problem_singular=False,final_topic_complete=False),
        seconds=time.monotonic()-began)
    save(args.output,doc)
    maximum = unpack(json.loads(args.output.read_text())['spectral_max_prefix']).upper()
    eps,sigma = rat(REPAIR),rat(Fraction(2,5))
    positive,germ = admitted['positive'],admitted['germ']
    for index,(left,right,row_index,piece) in enumerate(admitted['pieces']):
        if row_index < 0:
            intrinsic = germ['complex_intrinsic_coefficients']
            gamma = old_ball(intrinsic['gamma']['real'])
            curvature = old_ball(intrinsic['K']['real'])
            mean = old_ball(germ['moving_mean_v']['real'])
            m_hi = old_ball(germ['moving_mean_v']['modulus_upper']).upper()
            u = old_ball(germ['moving_U_derivative_Astrip'][0]).upper()
            v = old_ball(germ['moving_v_derivative_Astrip'][0]).upper()
            v_gap = old_ball(germ['angle_inverse']['bounds']['v_gap']).lower()
            k_lo = arb(0)
        else:
            row = positive['rows'][row_index]
            gamma = old_ball(row['intrinsic']['gamma'])
            curvature = old_ball(row['intrinsic']['K'])
            mean = old_ball(row['bounds']['mean_v'])
            m_hi = abs(mean).upper()
            u = old_ball(row['bounds']['U_A0']).upper()
            v = old_ball(row['bounds']['V_A0']).upper()
            v_gap = old_ball(row['bounds']['real_physical_inverse_gap']).lower()
            k_lo = curvature.lower()
            require(k_lo > 0, 'original body curvature retains its whole-cell positive sign')
        require(gamma.lower() > 0 and mean.upper() < 0 and u >= 0 and v > 0,
                'whole original signed gamma/mean and Wiener bounds')
        # Same paid Qrepair fees as X/SG.10.  Intrinsic gamma and K are unchanged.
        u,v = (u+eps).upper(),(v+eps).upper()
        m_lo,m_hi = ((-mean).lower()-eps).lower(),(m_hi+eps).upper()
        v_gap = (v_gap-eps).lower()
        require(m_lo > 0 and v_gap > 0, 'complete repaired denominators remain positive')
        k_hi = abs(curvature).upper()
        eta_lo,eta_hi = (gamma.lower()*m_lo).lower(),(gamma.upper()*m_hi).upper()
        require(eta_lo > 0 and eta_hi >= eta_lo, 'complete actual eta interval')
        require(v >= v_gap, 'complete correlated same-v closed interval')
        local_values = []
        for eta in (eta_lo,eta_hi):
            reciprocal = 1/eta
            for speed in (v_gap,v):
                # CV.5: the SAME speed occurs in both diagonal terms,
                # kappa and denominator. A nonnegative sum avoids cancellation.
                # Use whole Arb expressions at the directed endpoint; do not
                # independently round kappa in its opposing appearances.
                kappa = k_hi*speed*speed
                big_m = 1+u*u+kappa
                discriminant = ((1+u*u-kappa)**2+4*u*u*kappa).sqrt()
                value = ((big_m*(eta+reciprocal)
                         +discriminant*abs(eta-reciprocal))/(2*sigma*speed)).upper()
                require(value.is_finite() and value > 0,
                        'complete correlated four-vertex spectral upper')
                local_values.append(value)
        maximum = max(maximum,*local_values).upper()
        doc['completed_closed_cells'] = index+1
        doc['current_exact_right'] = str(right)
        if (index+1) % 64 == 0 or index+1 == len(admitted['pieces']):
            doc['spectral_max_prefix'] = recorded(maximum)
            doc['stage'] = 'complete-original-cell-spectral-prefix'
            doc['seconds'] = time.monotonic()-began
            save(args.output,doc)
            maximum = unpack(json.loads(args.output.read_text())['spectral_max_prefix']).upper()
            print(json.dumps(dict(completed_closed_cells=index+1,
                                  current_exact_right=str(right))),flush=True)
    require(doc['completed_closed_cells'] == doc['expected_closed_cells'] == len(admitted['pieces'])
        and Fraction(doc['current_exact_right']) == RIGHT,
        'all4651 new spectral cells completed, never substitute old CE for missing cells')

    def emit(name,value,direction='upper'):
        require(name not in doc['new_records'], 'a new scalar is emitted only once')
        doc['new_records'][name] = recorded(value,direction)
        doc['saved_record_count'] = len(doc['new_records'])
        doc['stage'] = 'saved-new-spectral-scalar-'+name
        doc['seconds'] = time.monotonic()-began
        save(args.output,doc)
        saved = json.loads(args.output.read_text())['new_records'][name]
        require(unpack(saved).contains(value), 'new scalar whole saved containment after disk readback')
        return unpack(saved).upper() if direction == 'upper' else unpack(saved).lower()

    # Intersect two complete independent upper bounds only after every new cell.
    c_sp = emit('C_correlated_upper',min(maximum,old['old_C_spectral_upper']).upper())
    w_e = emit('wE_correlated_upper',(rat(Fraction(5,2))*old['Gamma']
        *old['A_Theta'].sqrt()*(c_sp.sqrt()+old['C_H'].sqrt()*old['h_E'])).upper())
    a_ee = emit('aEE_correlated_upper',(old['E_0']*w_e*w_e
        +old['E_1']*w_e*old['h_E']).upper())
    a_eb = emit('aEB_correlated_upper',(2*old['E_0']*w_e*old['w_B']
        +old['E_1']*(w_e*old['h_B']+old['w_B']*old['h_E'])).upper())
    final = json.loads(args.output.read_text())['new_records']
    # R143 OC.5: lower endpoints make this an upper for the most favorable
    # necessary scalar. It excludes only this nonnegative-cost budget.
    aee_lo = unpack(final['aEE_correlated_upper']).lower()
    aeb_lo = unpack(final['aEB_correlated_upper']).lower()
    abb_lo = unpack(old_records['a_BB']).lower()
    favorable_d = (1-abb_lo).upper()
    require(aee_lo >= 0 and aeb_lo >= 0 and abb_lo >= 0
        and unpack(old_records['a_BB']).upper() < 1 and favorable_d > 0,
        'complete original positive B margin and nonnegative selected costs')
    emit('optimized_root_necessary_upper',(rat(Fraction(23,30))-aee_lo
        -aeb_lo*aeb_lo/(4*favorable_d)).upper())
    final = json.loads(args.output.read_text())['new_records']
    optimized_excluded = bool(unpack(final['optimized_root_necessary_upper']).upper() <= 0)
    a = 2-a_ee
    d = 1-old['a_BB']
    c = a_eb/2
    a_lower,d_lower,c_upper = a.lower(),d.lower(),c.upper()
    gate_a,gate_d = bool(a_lower > 0),bool(d_lower > 0)
    determinant_lower = (a_lower*d_lower-c_upper*c_upper).lower()
    gate_det = bool(determinant_lower > 0)
    body_all = gate_a and gate_d and gate_det
    doc['body_only_sufficient_comparison'] = dict(E_coefficient_less_than_2=gate_a,
        B_coefficient_less_than_1=gate_d,cross_discriminant_positive=gate_det,
        all_body_gates_pass=body_all,comparison_uses_complete_saved_upper_endpoints=True,
        root_constant_for_this_diagnostic='0; actual root receiver still independent',
        false_is_not_a_singularity_claim=True)
    if body_all:
        denominator_upper = (2*(d.upper()*old['r_E']**2
            +2*c_upper*old['r_E']*old['r_B']+a.upper()*old['r_B']**2)).upper()
        require(denominator_upper > 0, 'whole positive new root-allowance denominator')
        allowance = emit('root_allowance_correlated_lower',
            (determinant_lower/denominator_upper).lower(),'lower')
        require(allowance > 0, 'complete saved new lower allowance remains positive')
        doc['conditional_root_allowance'] = dict(applicable=True,
            source_record='root_allowance_correlated_lower',complete_saved_lower_used=True,
            exact_original_root_source_vector_retained=True,
            half_body_margin_proved=True,actual_root_cost_paid=False)
        doc['scope']['conditional_new_root_allowance_proved'] = True
    else:
        doc['conditional_root_allowance'] = dict(applicable=False,
            reason='the complete new body-only three-gate condition did not pass',
            no_conditional_lower_record_created=True,actual_root_cost_paid=False)
    final = json.loads(args.output.read_text())['new_records']
    thresholds = {'C_correlated_upper':Fraction(23),'wE_correlated_upper':Fraction(22),
                  'aEE_correlated_upper':Fraction(23,30)}
    passed = {name:bool(unpack(final[name]).upper() < rat(threshold))
              for name,threshold in thresholds.items()}
    violated = {name:bool(unpack(final[name]).lower() >= rat(threshold))
                for name,threshold in thresholds.items()}
    doc['root_anchor_necessary_screen'] = dict(
        exact_thresholds={name:str(value) for name,value in thresholds.items()},
        complete_saved_upper_comparisons=passed,complete_saved_lower_violations=violated,
        all_necessary_conditions_pass=all(passed.values()),
        at_least_one_necessary_condition_certifiably_violated=any(violated.values()),
        complete_old_RS_ball_below_125=True,
        complete_RN14_root_EE_strictly_greater_than_37_over_30=True,
        optimized_test_record='optimized_root_necessary_upper',
        optimized_nonnegative_direction_budget_certifiably_excluded=optimized_excluded,
        positive_optimized_upper_means_only_not_excluded=True,
        no_new_local_Gamma_value_assumed=True,
        passing_necessary_screen_is_not_a_sufficient_root_gate=True,
        no_actual_BVP_singularity_inferred=True)
    doc['scope']['complete_whole_spectral_constant_proved'] = True
    doc['scope']['complete_five_new_upper_bounds_proved'] = True
    doc['scope']['optimized_root_budget_certifiably_excluded'] = optimized_excluded
    doc['scope']['root_anchored_receiver_necessary_conditions_pass'] = all(passed.values())
    doc['scope']['any_necessary_condition_certifiably_violated'] = any(violated.values())
    doc.update(complete=True,proved=True,stage='complete-correlated-gram-body-budget',
               seconds=time.monotonic()-began)
    save(args.output,doc)
    print(json.dumps(dict(complete=True,proved=True,completed_closed_cells=4651,
        saved_record_count=doc['saved_record_count'],all_body_gates_pass=body_all,
        root_anchor_necessary_conditions_pass=all(passed.values()),output=str(args.output))),flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('positive','germ','physical','physical_execution','composed','composed_execution',
                 'body_budget','body_execution','root_screen','screen_execution',
                 'old_spectral','old_spectral_execution','output'):
        parser.add_argument('--'+name.replace('_','-'),type=Path,required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError('preserve the previous complete result or unfinished prefix')
    try:
        run(args)
    except Exception as exc:
        if args.output.exists():
            document = json.loads(args.output.read_text())
            if not document.get('complete'):
                document['failure'] = dict(type=type(exc).__name__,message=str(exc))
                document['stage'] = 'unfinished-new-correlated-gram-body-prefix'
                save(args.output,document)
        raise


if __name__ == '__main__':
    main()


