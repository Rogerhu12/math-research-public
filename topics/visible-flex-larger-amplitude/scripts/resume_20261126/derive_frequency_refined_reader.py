#!/usr/bin/env python3
"""Pure text derivation of the complete M-only refined normal report reader.

This program reads source text and writes source text only.  It does not
import a scientific provider or consume a numerical report/checkpoint.
"""
import argparse
import ast
import difflib
import hashlib
import json
from pathlib import Path

PARENT_SHA = 'c0cc0011498154a171e401d9874d34f060242180d341d6d2ea2b85eb963455dd'
DRIVER_SHA = '6a900861c01d0967dc585dd84797cc2428b62bd4a5969d594a68387c7a0175be'
REPORT_SCHEMA = 'complete-R711-reference-centred-adjacent-frame-frequency-refined-material-envelope-SO3-QP-v1'
OPERATOR_SCHEMA = 'complete-R711-reference-centred-adjacent-frame-frequency-refined-SO3-fixed-normal-plane-six-control-layer-v1'
READER_NAME = 'read_frequency_refined_material_envelope_so3_report.py'

FREQUENCY_BINDING = '''def frequency_binding(topic,report,model,roles,driver):
    relative,expected=load_pins(driver)['frequency_layout']
    path=topic/relative
    if (sha(path)!=expected or roles['frequency_layout']!=expected
            or report.get('frequency_layout_source',{}).get('sha256')!=expected):
        raise ValueError('Keep the complete independent frequency-layout source')
    spec=importlib.util.spec_from_file_location('_pure_frequency_layout_'+expected,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    if sha(module.validate_report.__code__.co_filename)!=expected:
        raise ValueError('The complete layout validator changed')
    result=module.validate_report(report,expected_layout_source_sha256=expected)
    value=report['frequency_refinement'];restart=report.get('restart')
    if (value.get('source_sha256')!=roles['envelope_transfer']
            or report.get('exact_trial_function_inclusion_is_not_floating_baseline_equivalence') is not True
            or report.get('coarse_baseline_statistics_are_not_new_initial_values') is not True
            or report.get('exact_selected_field_inclusion_requires_compatible_implicit_branch') is not True
            or report.get('computed_coarse_and_fine_field_equality_claimed') is not False):
        raise ValueError('Keep exact function inclusion separate from a new floating field read')
    mode=report['material_envelope_transfer']['current_invocation_memory_mode']
    if restart is None:
        if (mode!='frequency-refinement' or value['mode']!='actual-complete-parent-zero-inclusion'
                or report.get('prior_envelope_final_variable_seed')!=value
                or report.get('new_zero_closure_seed_changes_physical_field') is not None):
            raise ValueError('A first refined point needs its complete real coarse-variable seed')
    elif (mode!='same-source-restart' or value['mode']!='same-source-complete-restart'
            or value['parent_report']!=restart['report'] or value['parent_checkpoint']!=restart['checkpoint']
            or value['parent_driver_source_sha256']!=DRIVER_SHA
            or value['parent_model_identity_sha256']!=canonical(model)
            or value['parent_norm_identity_sha256']!=report['coordinate_norm']['norm_identity_sha256']
            or report.get('prior_envelope_final_variable_seed') is not None
            or report.get('new_zero_closure_seed_changes_physical_field') is not False):
        raise ValueError('A fine restart retains the actual whole current model, norm and final point')
    return result


'''


def sha(value):
    return hashlib.sha256(value).hexdigest()


def replace_once(text,old,new):
    if text.count(old)!=1:
        raise ValueError('Expected one complete literal source fragment: '+repr(old[:90]))
    return text.replace(old,new)


def derive(parent,driver):
    if sha(parent.encode())!=PARENT_SHA or sha(driver.encode())!=DRIVER_SHA:
        raise ValueError('Use the exact complete parent reader and refined scientific source')
    parsed=ast.parse(driver)
    schemas=[ast.literal_eval(n.value) for n in parsed.body if isinstance(n,ast.Assign)
        and len(n.targets)==1 and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='SCHEMA']
    if schemas!=[REPORT_SCHEMA]:raise ValueError('The actual complete driver schema differs')
    text=parent
    for old,new in (
        ("DRIVER_SHA = '91c86a4fed296cda92a9ac522dace21fb7e0ab603c288226b5cc8e7c3b8f44b6'","DRIVER_SHA = "+repr(DRIVER_SHA)),
        ("REPORT_SCHEMA = 'complete-R711-reference-centred-adjacent-frame-material-envelope-fixed-normal-plane-SO3-QP-v1'","REPORT_SCHEMA = "+repr(REPORT_SCHEMA)),
        ("OPERATOR_SCHEMA = 'complete-R711-reference-centred-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'","OPERATOR_SCHEMA = "+repr(OPERATOR_SCHEMA)),
        ("driver = topic/'scripts/resume_20261126/fullclosed_reference_centred_adjacent_frame_material_envelope_so3_qp.py'","driver = topic/'scripts/resume_20261126/fullclosed_frequency_refined_material_envelope_so3_qp.py'"),
        ("value.get('schema') != 'supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'","value.get('schema') != 'frequency-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'"),
        ("!= 'supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'","!= 'frequency-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'"),
        ("path = topic/'scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py'","path = topic/'scripts/resume_20261126/frequency_refined_smooth_triangle_literal_zero_moment_input.py'"),
        ("base.get('schema') != 'complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1'","base.get('schema') != 'complete-R711-frequency-refined-frozen-reference-so3-meridian-with-core-lift-v1'"),
        ("'all_original_outer_free_variables_and_norm_layout_unchanged'","'all_original_outer_free_variables_retained_and_new_modes_added',\n                    'frozen_reference_layout_unchanged','current_norm_layout_changed'"),
        ("schema='actual-complete-R711-reference-centred-adjacent-frame-material-envelope-normal-plane-SO3-scalar-readout-v1'","schema='actual-complete-R711-reference-centred-frequency-refined-material-envelope-normal-plane-SO3-scalar-readout-v1'"),
    ):text=replace_once(text,old,new)
    text=replace_once(text,
        "    raw_transfer=report['material_envelope_transfer']\n    if raw_transfer.get('current_invocation_memory_mode')=='explicit-independent-branch':\n        original=model['reference_centering_definition']['original_reference_point_sha256']\n        if (report.get('initial_full_variable_point_sha256')!=original\n                or report.get('actual_reference_initial_full_point_sha256')!=original\n                or report.get('prior_envelope_final_variable_seed') is not None):\n            raise ValueError('The independent branch must really start from its complete original reference point')\n",
        "    # The independent M-only entry uses an actual coarse final or its own fine restart.\n    # The complete source-bound transfer and layout validators check those two cases.\n")
    text=replace_once(text,
        "            or value.get('original_reference_point_sha256') != report['actual_reference_initial_full_point_sha256']",
        "            or value.get('frozen_reference_M') != report['reference_M']\n            or value.get('current_M') != report['current_M']\n            or value.get('reference_point_coordinate_layout') != 'new M320 zero embedding of the frozen M160 core/H with all omega zero'\n            or value.get('current_layout_reference_point_is_old_layout_byte_identical') is not False\n            or value.get('frozen_seed_and_original_reference_core_H_unchanged') is not True\n            or value.get('original_reference_point_sha256') != report['actual_reference_initial_full_point_sha256']")
    text=replace_once(text,'def read_report(repo, report_path, *, verify_final_bundle=False):',
        FREQUENCY_BINDING+'def read_report(repo, report_path, *, verify_final_bundle=False):')
    text=replace_once(text,
        '    transfer_binding,prior_final_seed = transferred_envelope_binding(topic,report,model,roles,driver)',
        '    transfer_binding,prior_final_seed = transferred_envelope_binding(topic,report,model,roles,driver)\n    frequency = frequency_binding(topic,report,model,roles,driver)')
    text=replace_once(text,
        '        prior_envelope_final_variable_seed=prior_final_seed,',
        '        prior_envelope_final_variable_seed=prior_final_seed,\n        reference_M=report[\'reference_M\'],current_M=report[\'current_M\'],\n        frequency_layout=frequency,frequency_refinement=report[\'frequency_refinement\'],\n        complete_parent_model_binding_checked_by_source_bound_transfer=True,\n        old_norm_or_damping_equivalence_inherited=False,')
    text=replace_once(text,'"""Pure complete R715 reference-centred R711 normal-chain attribution.',
        '"""Pure complete M160 -> M320 fixed-reference normal-chain attribution.')
    tree=ast.parse(text)
    compile(text,READER_NAME,'exec')
    old={n.name:ast.dump(n,include_attributes=False) for n in ast.parse(parent).body if isinstance(n,ast.FunctionDef)}
    new={n.name:ast.dump(n,include_attributes=False) for n in tree.body if isinstance(n,ast.FunctionDef)}
    changed={name for name in old if old[name]!=new[name]}
    expected={'transferred_envelope_binding','centering_binding','bind_literal_input','supported_seed_binding','read_report'}
    if changed!=expected or set(new)-set(old)!={'frequency_binding'}:
        raise ValueError('Unexpected change outside the complete source/layout binding interface')
    for n in ast.walk(tree):
        if isinstance(n,ast.Dict):
            keys=[v.value for v in n.keys if isinstance(v,ast.Constant) and isinstance(v.value,str)]
            if len(keys)!=len(set(keys)):raise ValueError('Duplicate literal dict key')
        if isinstance(n,ast.Call):
            keys=[v.arg for v in n.keywords if v.arg is not None]
            if len(keys)!=len(set(keys)):raise ValueError('Duplicate keyword')
    if len(text.encode())>=100000:raise ValueError('Keep the complete source below the public small-source limit')
    return text,dict(parent_reader_sha256=PARENT_SHA,actual_driver_sha256=DRIVER_SHA,
        bytes=len(text.encode()),sha256=sha(text.encode()),
        changed_existing_functions=sorted(changed),new_functions=['frequency_binding'],
        unchanged_complete_function_count=len(old)-len(changed),scientific_execution=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--parent-reader',type=Path,required=True)
    p.add_argument('--driver',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    p.add_argument('--verify-existing',action='store_true')
    a=p.parse_args()
    parent=a.parent_reader.read_text();driver=a.driver.read_text()
    output,record=derive(parent,driver)
    target=a.outdir/READER_NAME
    if a.verify_existing:
        if target.read_text()!=output:raise ValueError('The full generated reader differs')
    else:
        a.outdir.mkdir(parents=True,exist_ok=True)
        target.write_text(output)
        (a.outdir/'reader.diff').write_text(''.join(difflib.unified_diff(parent.splitlines(True),output.splitlines(True),
            fromfile='complete-c0cc-parent-reader.py',tofile=READER_NAME)))
        (a.outdir/'reader-source-lock.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,sort_keys=True))


if __name__=='__main__':main()
