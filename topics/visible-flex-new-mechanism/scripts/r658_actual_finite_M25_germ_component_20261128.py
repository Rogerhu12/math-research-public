#!/usr/bin/env python3
"""Attach the exact M25 truncation component to an existing R643 source/response receipt.

Only proved same-field finite denominators and field bounds can consume the quotient.
The original floating observation intervals and all seven error rows are preserved.
No transfer ODE, root, FFT, field or Jacobian is evaluated.
"""
import hashlib
import json
import os
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFINITION = HERE.parent/'computations/r618-actual397-frozen-field-definition-20261127.json'
DEFINITION_SHA = '12b2113d13bcc20f8c4813c4aac6e8fef6859eb4de7a1271f44770ca793bc952'
CONTRACT = '56ec2a5f44fc05c844390d54395a890fd32e84fef60364483ef8532ea830cbfb'
TARGET = '86da8c603f3d7ed9eb928481f0afe492f10bb209c94bf0ccaf8070c1aa1cd6c5'
MODEL = '0394f785ff395a38929d5ef82749fe8523cf24e8719ecdc907759ab1664d122b'
SEED = '19519575f7b4a8100cf9813851c258188ad4a0063edad05eb1b5b332b83f2cc7'
SEED_FINAL = '1fb5abfdf70e6c8154938b07ec5bd3353b68735c0dd5fd49f704204e65bd024e'
Q0D9A = '0d9a753f09f33fadd88b838c4dd3eddccb2830567050d391d0824e2ab54e7e16'
TAIL0D9A = '7287b7059726904309c7ca2b415830e64f6916efa9a3f4f08ae219eeed1924cb'
SCHEMA = 'R658-same-actual-M25-exact-truncation-component-v1'
ERROR = 'finite_M_to_true_infinite_germs'
MODES = tuple(range(2,23,2))


def public_only():
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        raise RuntimeError('scientific source-error consumption belongs to the public Actions repository')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()


def _signed_component(contract, paid, response_sha):
    raw = DEFINITION.read_bytes()
    if sha(raw)!=DEFINITION_SHA:
        raise ValueError('fixed 86da mathematical field literal differs')
    definition = json.loads(raw)
    tail = definition['accurate_inner_tail_definition']
    params = definition['all_literal_parameters']
    errors = contract['source_error_accounting']
    if (sha(canonical(contract))!=CONTRACT or tail['all_original_even_germs']!=list(MODES)
            or tail['phase']!=0 or params['original_reconstruction_arguments']['M']!=25
            or params['profile_overrides']!={'R':.85,'log_suppression':6.,'core_scale':.5}
            or contract['target_sha256']!=TARGET or contract['original_inner_phase']!=0
            or set(contract['old_germ_normalizations'])!={str(j) for j in MODES}
            or sha(canonical(tail))!=contract['true_inner_definition_sha256']
            or paid['joint_model_sha256']!=MODEL or paid['same_target_sha256']!=TARGET
            or paid['actual_response_sha256']!=response_sha or paid['fixed_seed_response_sha256']!=SEED
            or paid['fixed_seed_paid_FINAL_sha256']!=SEED_FINAL
            or paid['old_source_error_accounting']!=errors or len(errors)!=7
            or ERROR not in errors):
        raise ValueError('the original field, M25 finite problem, actual response or source ledger differs')
    return {'schema':SCHEMA,'definition_sha256':DEFINITION_SHA,'source_contract_sha256':CONTRACT,
        'same_target_sha256':TARGET,'joint_model_sha256':MODEL,'actual_response_sha256':response_sha,
        'consumed_R643_tail_receipt_sha256':sha(canonical(paid)), 'modes':list(MODES),
        'first_peak':17,'finite_M':25,'zero_terminal_peak':26,'source_phase':0,
        'strict_upper_bounds_as_exp_of_integer':{
            'rho18_difference':-3860,'balanced_Cauchy_difference_at_alpha17':-4060,
            'balanced_unscaled_difference_all_2p5_through_109':-2130,
            'unscaled_radial_0_through_3_difference_over_W_108_through_alpha26':-1000,
            'unscaled_true_radial_0_through_3_remainder_over_W_beyond_alpha26':-1000,
            'unscaled_body_C_and_core_C_difference':-2090,
            'unscaled_body_A_and_core_A_difference':-2080},
        'exact_source_error_row':ERROR, 'seven_original_source_rows':errors,
        'remaining_normalized_transfer_requires_exact_finite_denominator_and_upper_bounds':True,
        'finite_Cauchy_numerical_error_or_dense_ODE_error_included':False,
        'rigorous_field_curvature_reach_or_global_motion_qualified':False}


def paid_0d9a_component(literal_contract, actual_paid_tail):
    """Use the two previously emitted public literals without rebuilding the source field."""
    public_only()
    if sha(literal_contract.encode())!=CONTRACT or sha(canonical(actual_paid_tail))!=TAIL0D9A:
        raise ValueError('expected the R643 original source contract and second actual acceptance receipt')
    return _signed_component(json.loads(literal_contract),actual_paid_tail,Q0D9A)


def actual_tail_component(existing_tail, response, paid_receipt):
    """Consume an existing in-memory R643 model, any actual response and its own paid bound."""
    public_only()
    import sys
    module = sys.modules.get(type(existing_tail).__module__)
    if (module is None or type(existing_tail).__name__!='CompleteMeanTail'
            or Path(module.__file__).resolve()!=HERE/'r643_complete_mean_tail_bounds_20261128.py'
            or sha(Path(module.__file__).read_bytes())!='4cc0d0430efb6815806a6a1ba04a58067c5c5dc7e3efcb124aae9547c184c47a'
            or existing_tail.contract_sha!=CONTRACT or existing_tail.joint.guard()!=existing_tail.provenance
            or module.paid.CurrentModelTailAnchor._snapshot(existing_tail)!=existing_tail.source_snapshot):
        raise ValueError('same existing R643 tail object and paid source snapshot are required')
    checked = existing_tail.joint._check(response)
    return _signed_component(existing_tail.contract,paid_receipt,sha(canonical(checked.tolist())))


def exact_endpoint(value):
    """Exact rational string or integer; outward binary64 endpoints can use as_integer_ratio()."""
    if type(value) not in (str,int):
        raise TypeError('supply a proved rational endpoint, including its exact binary64 ratio when applicable')
    result=Fraction(value)
    if result<0:
        raise ValueError('nonnegative analytic majorant required')
    return result


def normalized_homogeneous_component(component, finite):
    """Pay (7) for one actual linear functional on its continuous cell using independent finite bounds.

    finite['raw_difference_upper'] must enclose that actual functional on its cell, after
    all ODE/cutoff/derivative operations prescribed in R658. No sampled bounds enter here.
    """
    public_only()
    if (component.get('schema')!=SCHEMA or component.get('definition_sha256')!=DEFINITION_SHA
            or component.get('source_contract_sha256')!=CONTRACT or component.get('same_target_sha256')!=TARGET
            or finite.get('same_target_sha256')!=TARGET or finite.get('source_contract_sha256')!=CONTRACT
            or finite.get('actual_response_sha256')!=component.get('actual_response_sha256')
            or finite.get('mode') not in MODES or not finite.get('actual_linear_functional')
            or not finite.get('actual_continuous_cell')
            or finite.get('coordinate_gauge')!='unscaled_y_at_alpha17_equals_one'
            or finite.get('finite_M')!=25 or finite.get('zero_terminal_peak')!=26
            or finite.get('enclosure_status')!='verified_exact_finite_field_over_entire_cell'
            or not finite.get('denominator_proof') or not finite.get('finite_functional_bound_proof')
            or not finite.get('raw_difference_proof')):
        raise ValueError('independent exact finite-source and continuous-functional evidence is required')
    lower = exact_endpoint(finite['finite_abs_Acore_lower'])
    absolute = exact_endpoint(finite['finite_raw_functional_abs_upper'])
    difference = exact_endpoint(finite['raw_difference_upper'])
    # e > 8/3, hence this positive exact rational exceeds e**(-2080).
    # The default binary64 exponential would lose this entire contribution.
    dA = Fraction(3,8)**2080
    if lower<=dA:
        raise ArithmeticError('finite core-A lower bound does not separate the true denominator')
    result=(difference+absolute*dA/lower)/(lower-dA)
    return {'actual_response_sha256':component['actual_response_sha256'],'mode':finite['mode'],
        'actual_linear_functional':finite['actual_linear_functional'],
        'actual_continuous_cell':finite['actual_continuous_cell'],
        'strictly_positive_denominator_and_exact_rational_arithmetic':True,
        'upper_numerator':str(result.numerator),'upper_denominator':str(result.denominator),
        'source_evidence':finite,'seven_original_source_rows':component['seven_original_source_rows'],
        'only_this_normalized_homogeneous_truncation_component_paid':True}
