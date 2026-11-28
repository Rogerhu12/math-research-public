"""Read actual paid R643 displays; return exact rational precision requirements, never invented errors."""
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import r658_actual_finite_M25_germ_component_20261128 as germ


PRODUCER_SHA = 'e7b204d7cedde08e0ccf2ce465a1ec09f455d8d64e74b39fe2490421f6ce3757'
if hashlib.sha256(Path(germ.__file__).read_bytes()).hexdigest()!=PRODUCER_SHA:
    raise ValueError('published actual finite-germ proof interface differs')


def original_observation(interval):
    lower,upper=interval['lo'],interval['hi']
    center=math.nextafter(lower,math.inf)
    if not math.isfinite(center) or math.nextafter(center,math.inf)!=upper:
        raise ValueError('expected the two outward neighbors emitted by the original R643 observer')
    return center


def exact_half(value):
    half=Fraction.from_float(abs(value))/2
    return {'numerator':str(half.numerator),'denominator':str(half.denominator)}


def _threshold_rows(component,contract):
    germ.public_only()
    if (germ.sha(germ.canonical(contract))!=germ.CONTRACT or component.get('schema')!=germ.SCHEMA
            or component.get('source_contract_sha256')!=germ.CONTRACT):
        raise ValueError('the actual source component and its original contract are required')
    rows={}
    for j in germ.MODES:
        old=contract['old_germ_normalizations'][str(j)]
        D=original_observation(old['display_log'])
        c=original_observation(old['core_A_abs'])
        if D<1027 or c<1.70:
            raise ValueError('the reported R643 display or core observation no longer identifies this bound')
        d=math.floor(D)
        rows[str(j)]={'chosen_common_binary64_display_hex':D.hex(),
            'observed_abs_core_A_hex':c.hex(),
            'sufficient_absolute_error_radius_for_finite_abs_core_A':exact_half(c),
            'proved_log_upper_truncation_core_A_in_chosen_gauge':-2080-d,
            'proved_log_upper_truncation_core_C_in_chosen_gauge':-2090-d,
            'proved_log_upper_difference_tail_0_to_3_over_W_108_through_alpha26_in_chosen_gauge':-1000-d,
            'proved_log_upper_omitted_true_tail_0_to_3_over_W_alpha26_onward_in_chosen_gauge':-1000-d,
            'finite_denominator_accuracy_verified_by_this_consumer':False}
    return {'schema':'R658-actual-display-and-relative-denominator-precision-v1',
        'original_component':component,'same_actual_mode_precision_requirements':rows,
        'if_each_finite_denominator_threshold_is_independently_met_normalized_log_upper':-2000,
        'conditional_bound_domains':['difference_108_le_u_le_alpha26_radial_orders0to3_over_W',
            'omitted_true_remainder_u_ge_alpha26_radial_orders0to3_over_W',
            'difference_original_mouth_to_rim_radial_orders0to2_after_actual_cutoff'],
        'seven_source_rows_preserved':component['seven_original_source_rows'],
        'source_ODE_roundoff_or_global_motion_certified':False}


def paid_0d9a_thresholds(literal_contract,paid_receipt):
    component=germ.paid_0d9a_component(literal_contract,paid_receipt)
    return _threshold_rows(component,json.loads(literal_contract))


def live_thresholds(existing_tail,response,paid_receipt):
    component=germ.actual_tail_component(existing_tail,response,paid_receipt)
    result=_threshold_rows(component,existing_tail.contract)
    forced=existing_tail.model.old.old.forced
    C_h,C_p=(float(value) for value in forced.raw_core_C)
    if not all(math.isfinite(v) for v in (C_h,C_p)) or C_h==0:
        raise ValueError('the actual already-generated forced core C pair is unavailable')
    result['additional_forced_boundary_observation']={
        'actual_force_background_gain_hex':float(forced.par.gain_height).hex(),
        'actual_forced_j4_homogeneous_core_C_hex':C_h.hex(),
        'actual_forced_j4_particular_core_C_hex':C_p.hex(),
        'actual_force_display_hex':float(forced.flat.display_log).hex(),
        'actual_paid_tail_multiplier_hex':float(forced.tail_multiplier).hex(),
        'sufficient_absolute_error_radius_for_finite_abs_force_core_C':exact_half(C_h),
        'subsequent_actual_particular_source_variation_and_core_back_still_required':True,
        'positive_true_denominator_certified_by_this_observation':False}
    return result
