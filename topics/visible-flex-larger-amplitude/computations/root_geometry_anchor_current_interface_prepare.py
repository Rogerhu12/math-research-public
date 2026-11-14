#!/usr/bin/env python3
"""Prepare source identities and units for a future actual M32 nine-control model.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
No future accepted package, response value, geometry field or numerical grid is
created. This checks the reversible adapters and existing physical API only.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import ast
import hashlib
import importlib
import json
from pathlib import Path
import resource
import time

from root_geometry_anchor_current_interfaces import (
    CONTROL_NAMES,RESPONSE_FIELDS,HERE,FROZEN,build,sha,check_sources)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--response-source',type=Path,required=True)
    a=p.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('A fresh source-only preparation record is required')
    check_sources()
    plan_ns,plan_prov=build('plan',HERE/'root_actual_geometry_anchor_current_plan.py')
    combo_ns,combo_prov=build('combined',HERE/'root_geometry_anchor_current_combined_plan.py')
    import root_geometry_minimax_initial_laws_controls as algorithm
    import root_geometry_anchor_current_reader as reader
    from strong_frontload_anchor_loader_adapter import build as build_provider
    namespace,provider_prov=build_provider('geometry',HERE/'root_actual_geometry_field_anchor.py')
    unused_entry,unused_main,field_preparation=namespace['prepare_entry']()
    response_source=a.response_source.read_text()
    provider_source=(HERE/'alternative-neck-provider.py').read_text()
    flat_source=(HERE/'alternative-neck-flatturn.py').read_text()
    checks={
        'all_original_source_hashes_match':True,
        'plan_reversal_exact':plan_prov['exact_reverse_recovers_original_source'],
        'combined_reversal_exact':combo_prov['exact_reverse_recovers_original_source'],
        'original_current_minimax_accepts_nine_controls':algorithm.valid_controls(list(CONTROL_NAMES)),
        'original_combined_validator_accepts_nine_controls':combo_ns['valid_controls'](list(CONTROL_NAMES)),
        'original_plan_validator_accepts_nine_controls':plan_ns['valid_controls'](list(CONTROL_NAMES)),
        'fresh_plan_default_neutrals_are_complete_six':tuple(plan_ns['DEFAULT_NEUTRALS'])==CONTROL_NAMES[3:],
        'reader_import_has_no_field_execution':callable(reader.verify),
        'same_corrected_provider_explicit':provider_prov['current_anchor_hook_sha256']==FROZEN['strong_monotone_initial_speed_anchor.py'],
        'geometry_original_mean_and_formulas_unchanged':not provider_prov['mathematical_geometry_mean_quintic_and_acceptance_formulas_changed'],
        'original_Ksync_provider_key_exists':"Ksync=float(cfg.get('descending_sync_curvature',8.))" in provider_source,
        'original_Ksync_controls_sync_turn':"sync=fl.turn(-math.asin(vd),-math.asin(vl),Ksync)" in provider_source,
        'original_turn_length_formula':"eps=.08;L=abs(p1-p0)/(K*(1-eps))" in flat_source,
        'original_response_fullstep_formula':"width=2e-6*max(.1,abs(original))" in response_source,
        'original_response_halfstep_formula':"for step in (width,width/2):" in response_source,
        'original_Ksync_response_whitelist':"'descending_sync_curvature','coast_outward','loop_ratio'" in response_source,
        'original_core_held_exchange_uses_full_primary_columns':"combined=source+Z@du" in response_source,
        'original_neutral_physical_unit_is_one':"physical_profile_derivative={field:1." in response_source,
    }
    if not all(checks.values()):raise ArithmeticError([k for k,v in checks.items() if not v])
    sources={str(HERE/name):sha(HERE/name) for name in FROZEN}
    for name in ('root_geometry_anchor_current_interfaces.py','root_actual_geometry_anchor_current_plan.py',
                 'root_geometry_anchor_current_reader.py','root_geometry_anchor_current_combined_plan.py',
                 'root_geometry_anchor_current_interface_prepare.py','alternative-neck-provider.py','alternative-neck-flatturn.py'):
        path=HERE/name;ast.parse(path.read_text());sources[str(path)]=sha(path)
    sources[str(a.response_source)]=sha(a.response_source)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    result=dict(schema='current-M32-nine-control-geometry-source-only-preparation-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        all_source_only_gates=True,gate_count=len(checks),gates=checks,source_sha256_map=sources,
        plan_adapter=plan_prov,combined_adapter=combo_prov,provider_adapter=provider_prov,
        unchanged_field_source_preparation=field_preparation,
        design_controls=list(CONTROL_NAMES),external_response_fields=list(RESPONSE_FIELDS),
        suggested_geometry_steps=[.001,3e-5,2e-6,.0002,.0025,.002,.01,.001,.002],
        geometry_step_suggestions_are_not_executed_fields_or_response_forcing_steps=True,
        synchronization_control=dict(key='descending_sync_curvature',unit='physical phase radians per meridian length',
            turn_length='abs(asin(loop_speed)-asin(vd))/(Ksync*(1-eps)); original eps=.08',
            fixed_vd_loop_speed_length_derivative='-Lsync/Ksync',
            original_external_fullstep='2e-6*max(.1,abs(current Ksync))',original_external_halfstep='fullstep/2',
            if_current_Ksync_equals_2=dict(fullstep=4e-6,halfstep=2e-6,suggested_geometry_step=.002),
            core_held_definition='dKsync=1; delta, boost_length and boost_speed adjusted by the same current full-J 3x3 exchange so the three prescribed core coefficients have zero first derivative.',
            higher_core_modes_and_all_shooting_state_derivatives_retained=True,
            sign_or_usefulness_not_predicted_without_actual_current_response=True),
        execution_contract=dict(actual_baseline_owned_accepted_required_before_plan=True,
            same_fixed_view_SHA_for_current_quintic_audit=True,unique_baseline_plan_reused_verbatim=True,
            modes=32,mean_angular=1552,geometry_angular_minimum=768,
            every_current_raw_node_and_current_quintic_witness_retained=True,
            full_response_all_nine_columns_required=True,original_partial_eight_response_not_accepted=True,
            planned_fields_after_response=19,all_five_finite_minimax_row_families_retained=True,
            no_extra_fine_modes_zeroed=True,no_coarse_or_stale_fields_imported=True,
            original_strict_field_domain_and_chart_gates_retained=True),
        actual_geometry_fields_generated=0,accepted_inputs_fabricated=0,new_ODE_Node_Jacobian_calls=0,
        seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),gates=len(checks),geometry_fields=0,
                         seconds=result['seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
