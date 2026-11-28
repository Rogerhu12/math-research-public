#!/usr/bin/env python3
"""R94: pay R87's literal binary64 window parameters using R91's pi bound.

All new arithmetic is exact Fraction. R91 already proves the window integral,
the mean-compensation inequality and the retained strict Machin bound. This
entry only substitutes the actual source's binary64 S,b,k and checks the same
core curvature ceiling. It does not certify finite Gaussian core evaluation,
produce a field, check a complete BVP or transfer any old geometry bound.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[2]
PRIOR = TOPIC/'notes/2026-11-28-analytic-core-mean-compensation-box.json'
PRIOR_SOURCE = HERE/'certify_core_mean_compensation_box.py'
PRIOR_SOURCE_SHA = '8278c20e4a06596133361f620954e7382682ce5734eda685b4619fe2e7d2780a'
CORE = TOPIC/'scripts/resume_transfer/material_flattened_support_core.py'
CORE_SHA = '1d655f2bdad53e1d320c1115a9873abe399a9b7ba930722c415d02dedb9b1f20'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path),sha256=sha(path))


def positive(value, description):
    if value <= 0:
        raise ArithmeticError(description+' is not positive')
    return str(value)


def certificate(config_path):
    previous = json.loads(PRIOR.read_text())['actual_record']
    if (sha(PRIOR_SOURCE) != PRIOR_SOURCE_SHA
            or previous['source_sha256'] != PRIOR_SOURCE_SHA
            or previous['status'] != 'proved_exact_scalar_core_budget'
            or sha(CORE) != CORE_SHA
            or previous['source_definitions'].get(str(CORE)) != CORE_SHA
            or previous['original_window']['integral'] != '1/2'):
        raise ValueError('The bound original R91 proof/record or exact R53 window definition changed')
    pi_lower = Q(previous['pi_lower_witness']['lower'])
    if pi_lower != Q(1231847548,392109375):
        raise ValueError('Use the already proved strict Machin lower bound')
    cfg = json.loads(Path(config_path).read_text())
    actual = {}
    for key in ('halfwidth','transition','target_curvature'):
        value = cfg[key]
        if type(value) not in (int,float) or not math.isfinite(value):
            raise ValueError('The real source window must have finite numerical parameters')
        actual[key] = Q.from_float(float(value))
    S,b,k = (actual[key] for key in ('halfwidth','transition','target_curvature'))
    if (cfg.get('curvature_blend') != 1
            or (S,b,k) != (Q.from_float(.675),Q.from_float(.3),Q(1,2))):
        raise ValueError('This consequence is for the literal R87 .675/.3/.5 parameters only')
    J = 2*S+b
    T_lower = 2*pi_lower/3
    beta_upper = (T_lower-k*J)/(T_lower-J)
    old_beta_upper = Q(897,314)
    target_curvature_upper = Q(3723,314)
    margins = dict(
        S_minus_27_over_40=str(S-Q(27,40)),
        b_minus_3_over_10=str(b-Q(3,10)),
        J_minus_33_over_20=positive(J-Q(33,20),'literal total protected window change'),
        actual_window_fit=positive(T_lower/2-S-b,'true period half-window fit'),
        actual_compensation_denominator=positive(T_lower-J,'true compensation denominator'),
        old_beta_ceiling_minus_new_upper=positive(old_beta_upper-beta_upper,'retained strict beta ceiling'),
        full_core_ceiling_minus_new_upper=positive(target_curvature_upper-(9+beta_upper),'retained full core ceiling'),
        original_support_curvature_above_k=positive(Q(9,17)-k,'nonnegative beta hypothesis'),
        complete_core_curvature_budget=positive(Q(123,10)-target_curvature_upper,'12.3 core margin'))
    return dict(schema='R94-literal-binary64-window-core-mean-consequence-v1',
        status='proved_exact_binary64_parameter_substitution',source=ref(__file__),
        source_configuration=ref(config_path),source_configuration_homotopy=cfg.get('homotopy'),
        inherited_R91_record=ref(PRIOR),inherited_R91_source=ref(PRIOR_SOURCE),
        unchanged_exact_core_source=ref(CORE),
        premise='The R53 exact true-integral core, curvature_blend=1, weighted support sum A<=8/9; only S,b,k are interpreted as their actual source binary64 rationals',
        actual_parameters_exact={key:str(value) for key,value in actual.items()},
        true_integral_window_exact=str(J),
        retained_pi_lower_strict=str(pi_lower),true_period_lower_strict=str(T_lower),
        exact_mean_compensation_upper_strict=str(beta_upper),
        retained_compensation_upper_strict=str(old_beta_upper),
        full_homotopy_interval=['0','1'],retained_weighted_support_sum_upper='8/9',
        retained_full_core_curvature_interval=['1/2',str(target_curvature_upper)],
        upper_endpoint_is_strict=True,exact_margins=margins,
        finite_Gauss_core_error_certified=False,actual_support_coefficients_validated=False,
        actual_lambda_one_field_produced=False,new_BVP_or_tail_solve_executed=False,
        original_numerical_source_or_gates_changed=False,
        whole_surface_geometry_or_metric_certified=False,readme_completion_claimed=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--core-config',type=Path,
        default=HERE.parent/'design/material_single_gentle_k050_lambda0.json')
    parser.add_argument('--out',type=Path,required=True)
    args = parser.parse_args()
    result = certificate(args.core_config.resolve())
    out = args.out.resolve()
    if out.exists() or out == TOPIC or TOPIC in out.parents:
        raise ValueError('Use a fresh scalar execution record outside the topic source tree')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(status=result['status'],output=ref(out),
        actual_parameters_exact=result['actual_parameters_exact'],
        true_integral_window_exact=result['true_integral_window_exact'],
        exact_mean_compensation_upper_strict=result['exact_mean_compensation_upper_strict'],
        retained_full_core_curvature_interval=result['retained_full_core_curvature_interval'],
        old_beta_ceiling_margin=result['exact_margins']['old_beta_ceiling_minus_new_upper'])),flush=True)


if __name__ == '__main__':
    main()
