#!/usr/bin/env python3
"""The complete new root-anchored drift budget on [r_star,r_star+1/100].

New scientific evaluation is restricted to this repository's public Actions.
Only the already complete positive/germ scalar rows and complete X result
are read.  The two new saved bounds are the local drift-derivative integral
and its exponential.  No candidate, old target, flow ODE, or capacity ODE
is evaluated, and no coefficient/partition array is published.
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


KIND = 'R138_true_root_anchored_local_drift_budget_v1'
BITS = 320
LENGTH = Fraction(1, 100)
CLOSE_TO_ONE = Fraction(101, 100)
POSITIVE_SHA = 'ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d'
GERM_SHA = '397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864'
CANDIDATE_SHA = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
OBJECT_SHA = '91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848'
REPAIR_SHA = '440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
X_SHA = '1259c3687cea0af523dd52055e88d5ee9a7b77094c218101835b6c38dfbbc7ec'
X_EXECUTION_SHA = '999555eafb3c443266f1a8fed98056c9d4f448c0131ef5ffff93941b35040c92'
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
        'new local drift uses exactly the same actual Qrepair as X')
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

    cutoff = ROOT_HI+LENGTH
    require(cutoff < RIGHT, 'fixed new complete root interval is inside the original cap')
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
        'whole original cap and the whole padded new root interval are both complete')
    partition = [[str(l),str(r),index,piece] for l,r,index,piece in pieces]
    partition_sha = hashlib.sha256(json.dumps(partition,separators=(',',':')).encode()).hexdigest()
    interface_sha = hashlib.sha256(json.dumps(original_interfaces,sort_keys=True,
                                            separators=(',',':')).encode()).hexdigest()
    require(interface_sha == xid['original_positive_interface_metadata_sha256'],
            'all original candidate/intrinsic interface metadata agree with X')
    return dict(positive=positive,germ=germ,old_x=old_x,execution=execution,
                pieces=pieces,cutoff=cutoff,partition_sha=partition_sha,
                interface_sha=interface_sha,original_interfaces=len(original_interfaces))


def run(args):
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
        and os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public',
        'new science runs only in this repository public Actions')
    require(not args.output.exists(), 'preserve every previous result or failed prefix')
    admitted = admit_inputs(args)
    from flint import arb, ctx
    ctx.prec = BITS
    began = time.monotonic()
    args.output.parent.mkdir(parents=True, exist_ok=True)

    def rat(value):
        value = Fraction(value)
        return arb(value.numerator)/value.denominator

    def old_ball(record):
        require('lower' in record and 'upper' in record, 'whole old signed scalar endpoints')
        value = arb(record['lower']).lower().union(arb(record['upper']).upper())
        require(value.is_finite(), 'finite whole old scalar enclosure')
        return value

    def unpack(record):
        require(record.get('kind') == 'complete_decimal_ball_v1', 'complete saved scalar kind')
        exponent = int(record['decimal_exponent'])
        scale = rat(10**exponent) if exponent >= 0 else rat(Fraction(1,10**(-exponent)))
        mid = rat(int(record['midpoint_integer']))*scale
        radius = rat(int(record['radius_integer']))*scale
        require(radius >= 0, 'nonnegative whole saved scalar radius')
        return (mid-radius).lower().union((mid+radius).upper())

    def recorded(value):
        require(value.is_finite(), 'finite complete new scalar upper')
        mid,radius,exponent = value.mid_rad_10exp(75)
        result = dict(kind='complete_decimal_ball_v1',mathematical_direction='upper',
                      midpoint_integer=str(int(mid)),radius_integer=str(int(radius)),
                      decimal_exponent=str(int(exponent)))
        require(int(radius) >= 0 and unpack(result).contains(value),
                'saved whole new scalar contains its complete directed value')
        return result

    old_x = admitted['old_x']
    old_integral = old_x['new_scalar_integrals']['drift_derivative_integral']
    old_gamma = old_x['complete_derived_energy_bounds']['Gamma']
    require(unpack(old_integral).lower() > 0 and unpack(old_gamma).lower() > 1,
            'complete old drift upper records are retained without reevaluation')
    identity = dict(kind=KIND,source_sha256=digest(__file__),arithmetic_bits=BITS,
        original_positive_sha256=POSITIVE_SHA,original_germ_sha256=GERM_SHA,
        original_candidate_sha256=CANDIDATE_SHA,intrinsic_object_sha256=OBJECT_SHA,
        exact_repair_definition_sha256=REPAIR_SHA,
        exact_alpha=str(ALPHA),exact_eta=str(ETA),exact_nu=str(NU),
        exact_true_root_interval=[str(ROOT_LO),str(ROOT_HI)],
        actual_local_interval='[r_star,r_star+1/100]',fixed_local_length=str(LENGTH),
        conservative_integration_interval=[str(ROOT_LO),str(admitted['cutoff'])],
        exact_flow_initial_condition='psi(r_star,xi)=xi',moving_period='2*pi',
        original_positive_rows=4650,original_positive_interfaces=admitted['original_interfaces'],
        original_positive_interface_metadata_sha256=admitted['interface_sha'],
        complete_new_partition_sha256=admitted['partition_sha'],
        full_pair_repair_A0=str(REPAIR),
        old_X_sha256=X_SHA,old_X_execution_sha256=X_EXECUTION_SHA,
        fixed_close_to_one_threshold=str(CLOSE_TO_ONE))
    doc = dict(identity=identity,complete=False,proved=False,failure=None,
        stage='prepared-complete-new-local-drift-integral',
        expected_common_cells=len(admitted['pieces']),completed_common_cells=0,
        completed_positive_rows=0,current_exact_right=str(ROOT_LO),
        integral_prefix=recorded(arb(0)),complete_drift_integral=None,
        complete_local_Gamma=None,saved_record_count=0,
        old_scientific_targets_called=0,old_geometry_ODE_calls=0,
        old_candidate_targets_called=0,old_X_targets_recomputed=0,
        new_flow_ODE_calls=0,new_capacity_ODE_calls=0,published_arrays=0,
        whole_original_references=dict(
            physical_budget=dict(complete_result_sha256=X_SHA,
                complete_execution_sha256=X_EXECUTION_SHA,run_id='44737045152',run_attempt='1',
                whole_result_admitted=True,whole_execution_admitted=True,
                original_identity=old_x['identity'],original_scope=old_x['scope'],
                complete_original_D0_record=old_integral,complete_original_Gamma_record=old_gamma)),
        scope=dict(same_actual_Qrepair_and_complete_independent_mean=True,
            same_full_moving_angular_circle=True,original_all_interfaces_preserved=True,
            true_root_not_replaced_by_interval_endpoint=True,
            root_anchored_auxiliary_flow=True,root_receiver_density_transfer_required=False,
            physical_Theta_and_H_mean_retained=True,one_local_sqrt_Gamma_in_energy=True,
            complete_new_local_drift_integral_proved=False,
            complete_new_local_Gamma_proved=False,local_Gamma_below_101_over_100=False,
            actual_flow_integrated=False,localized_capacity_Gram_paid=False,
            new_spectral_body_budget_paid=False,root_boundary_form_paid=False,
            actual_positive_boundary_problem_singular=False,
            positive_inverse_proved=False,final_topic_complete=False),
        strict_comparisons=None,seconds=time.monotonic()-began)
    save(args.output,doc)
    total = unpack(json.loads(args.output.read_text())['integral_prefix']).upper()
    eps = rat(REPAIR)
    positive,germ = admitted['positive'],admitted['germ']
    for index,(left,right,row_index,piece) in enumerate(admitted['pieces']):
        if row_index < 0:
            intrinsic = germ['complex_intrinsic_coefficients']
            beta = abs(old_ball(intrinsic['beta']['real'])).upper()
            curvature = abs(old_ball(intrinsic['K']['real'])).upper()
            u = old_ball(germ['moving_U_derivative_Astrip'][0]).upper()
            v = old_ball(germ['moving_v_derivative_Astrip'][0]).upper()
            original_drift = (beta*(u*u+curvature*v*v)).upper()
        else:
            row = positive['rows'][row_index]
            beta = abs(old_ball(row['intrinsic']['beta'])).upper()
            curvature = abs(old_ball(row['intrinsic']['K'])).upper()
            u = old_ball(row['bounds']['U_A0']).upper()
            v = old_ball(row['bounds']['V_A0']).upper()
            original_drift = old_ball(row['bounds']['drift_phi_A0']).upper()
        require(u >= 0 and v >= 0 and beta >= 0 and curvature >= 0 and original_drift >= 0,
                'complete nonnegative original Wiener bounds on the whole source cell')
        # The paid repair is a complete pair bound ||e_u||A0+||e_v||A0 <= eps.
        # These are exactly X's original repair/background definitions, now
        # integrated only over the independently fixed complete root interval.
        delta_S = (max(arb(1),curvature)*(2*(u+v)*eps+eps*eps)).upper()
        repaired_drift = (original_drift+2*beta*delta_S).upper()
        contribution = (rat(right-left)*repaired_drift).upper()
        require(contribution.is_finite() and contribution >= 0,
                'whole-cell nonnegative local drift-integral contribution')
        total = (total+contribution).upper()
        doc['completed_common_cells'] = index+1
        doc['completed_positive_rows'] += int(row_index >= 0)
        doc['current_exact_right'] = str(right)
        doc['integral_prefix'] = recorded(total)
        doc['stage'] = 'complete-original-cell-prefix'
        doc['seconds'] = time.monotonic()-began
        save(args.output,doc)
        total = unpack(json.loads(args.output.read_text())['integral_prefix']).upper()
        if (index+1) % 32 == 0 or index+1 == len(admitted['pieces']):
            print(json.dumps(dict(completed_common_cells=index+1,
                                  current_exact_right=str(right))),flush=True)

    require(doc['completed_common_cells'] == doc['expected_common_cells']
        and Fraction(doc['current_exact_right']) == admitted['cutoff'],
        'complete original root interval, no partial prefix promoted to a conclusion')
    doc['complete_drift_integral'] = doc['integral_prefix']
    doc['saved_record_count'] = 1
    doc['stage'] = 'complete-local-drift-integral-saved-before-exponential'
    save(args.output,doc)
    saved_D = unpack(json.loads(args.output.read_text())['complete_drift_integral']).upper()
    doc['complete_local_Gamma'] = recorded(saved_D.exp().upper())
    doc['saved_record_count'] = 2
    doc['stage'] = 'complete-local-Gamma-saved-before-comparisons'
    save(args.output,doc)
    final = json.loads(args.output.read_text())
    saved_Gamma = unpack(final['complete_local_Gamma'])
    close_gate = bool(saved_Gamma.upper() < rat(CLOSE_TO_ONE))
    smaller_old = bool(saved_Gamma.upper() < unpack(old_gamma).lower())
    doc['strict_comparisons'] = dict(
        local_Gamma_below_101_over_100=close_gate,
        local_Gamma_strictly_below_original_saved_Gamma=smaller_old,
        fixed_close_to_one_threshold=str(CLOSE_TO_ONE),
        complete_new_saved_upper_used=True,complete_old_saved_lower_used=True,
        false_comparison_does_not_negate_complete_local_bound=True)
    doc['scope']['complete_new_local_drift_integral_proved'] = True
    doc['scope']['complete_new_local_Gamma_proved'] = True
    doc['scope']['local_Gamma_below_101_over_100'] = close_gate
    doc.update(complete=True,proved=True,stage='complete-root-anchored-local-drift-budget',
               seconds=time.monotonic()-began)
    save(args.output,doc)
    print(json.dumps(dict(complete=True,proved=True,
        completed_common_cells=doc['completed_common_cells'],saved_record_count=2,
        local_Gamma_below_101_over_100=close_gate,output=str(args.output))),flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('positive','germ','physical','physical_execution','output'):
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
                document['stage'] = 'unfinished-new-local-drift-prefix'
                save(args.output,document)
        raise


if __name__ == '__main__':
    main()
