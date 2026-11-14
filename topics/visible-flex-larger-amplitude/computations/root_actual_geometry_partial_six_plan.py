#!/usr/bin/env python3
"""Plan only the six genuinely recovered q122 warm directions.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The original eight-column producer failed. Its six completed external full
vectors and measured per-column half checks are real, but combination half
vectors and combination matrix residuals were not saved. This entry preserves
that distinction while passing only the available six directions to the
original actual-input, complete-mean geometry planner. No missing frontload
or vd direction is generated or declared passed.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
ORIGINAL_SHA='a6c537cea001d5fcc4104164bee5194620913b9a53bfa1fad0ccf6800ddfcb34'
RESPONSE_SHA='2e848e2b59507a4bec44546a4916fb54e461b59713c0b37a968313669dc97f30'


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(add_help=False)
    p.add_argument('--response-data',type=Path,required=True)
    p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--neutral-controls',nargs='+',required=True)
    a,_=p.parse_known_args()
    original=HERE/'root_actual_geometry_fullmean_initial_laws_plan.py'
    if sha(original)!=ORIGINAL_SHA or sha(a.response_data)!=RESPONSE_SHA:
        raise ValueError('Frozen planner or real partial-six response changed')
    d=json.loads(a.response_data.read_text())
    if (a.neutral_controls!=['vu','descending_turn_curvature','start_acceleration'] or
        d.get('partial_recovery') is not True or d.get('finished') is not True or
        d.get('original_eight_control_job_finished') is not False or d.get('original_eight_control_job_exitcode')!=1 or
        d.get('all_six_original_external_full_and_half_gates_observed') is not True or
        d.get('unavailable_fields')!=['initial_speed_frontload','vd'] or
        d.get('fields')!=['delta','boost_length','boost_speed','vu','descending_turn_curvature','start_acceleration']):
        raise ValueError('Only the observed six-column design recovery is permitted')
    rows=d['prescribed_low_core_responses']+d['additional_core_held_directions']
    if len(rows)!=6 or any(r.get('original_combined_half_vector_was_not_saved') is not True or r.get('equation_relative_backward_error') is not None for r in rows):
        raise ValueError('Unsaved combination checks must remain explicitly unknown')
    spec=importlib.util.spec_from_file_location('frozen_complete_mean_six_plan',original)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
    module.main()
    path=Path(str(a.out_prefix)+'-plan.json');plan=json.loads(path.read_text())
    if len(plan['directions'])!=6 or len(plan['candidates'])!=13 or plan['candidates'][0]['name']!='baseline':
        raise ArithmeticError('The original six-control plan changed dimension')
    plan['partial_control_response_scope']=dict(scope=__doc__,response_sha256=RESPONSE_SHA,
        original_eight_control_job_exitcode=1,unavailable_fields=d['unavailable_fields'],
        all_six_original_external_full_and_half_gates_observed=True,
        combined_direct_half_vectors_or_matrix_residuals_observed=False,
        numerical_combination_perturbation_estimates=[{k:v for k,v in r.items() if 'perturbation_bound' in k or k in ('direction','external_field')} for r in rows],
        local_unsolved_warm_design_only=True,original_new_BVP_gates_unchanged=True)
    plan['source_and_input_sha256'][str(Path(__file__))]=sha(__file__)
    plan['limitations'].append('Six recovered full directions only; missing frontload/vd and unrecorded direct combination checks are not supplied by this plan.')
    temp=path.with_name(path.name+'.partial-six.tmp');temp.write_text(json.dumps(plan,indent=2)+'\n');temp.replace(path)
    print(json.dumps({'event':'partial_six_fullmean_plan_frozen','plan':str(path),'sha256':sha(path),'directions':6,'new_fields_to_run':12,'baseline_must_be_reused':True}),flush=True)


if __name__=='__main__':main()
