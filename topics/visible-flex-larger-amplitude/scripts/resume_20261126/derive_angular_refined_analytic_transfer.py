#!/usr/bin/env python3
"""Complete source-only construction of the independent-target N history bridge."""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PARENT_SHA='0d2a5e9c9f5651e149d53da859ac42ced1c3b44709f9a5a3416a82c8d8702608'
OLD_MEMORY='4d92ca2387523a76bbea0a3444e0665c306369dd0351c3354c998a09884e043b'
PARENTS={
    'cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5': dict(
        report_schema='complete-R711-reference-centred-C1-material-envelope-fixed-normal-plane-SO3-QP-v1',
        reader_sha256='104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7',
        reader_relative='scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py',
        operator_sha256='a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd',
        operator_schema='complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1',
        memory_sha256='c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152'),
    '95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9': dict(
        report_schema='complete-R711-reference-centred-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1',
        reader_sha256='f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470',
        reader_relative='scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py',
        operator_sha256='d5da5e3db88a03cc0afdc00e3a6bc74e425aa3f1b730ea7f66ac278f93d8e6eb',
        operator_schema='complete-R711-reference-centred-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1',memory_sha256=OLD_MEMORY),
    '0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51': dict(
        report_schema='complete-R711-reference-centred-analytic-J3-independent-chart-material-envelope-fixed-normal-plane-SO3-QP-v1',
        reader_sha256='c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e',
        reader_relative='scripts/resume_20261126/read_reference_centred_analytic_j3_material_envelope_so3_report.py',
        operator_sha256='04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e',
        operator_schema='complete-R711-reference-centred-analytic-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1',memory_sha256=OLD_MEMORY)}


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def body(text,name):
    n=next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name==name)
    return '\n'.join(text.splitlines()[n.lineno-1:n.end_lineno])+'\n'


def assign(text,name,value):
    n=next(n for n in ast.parse(text).body if isinstance(n,ast.Assign)
        and len(n.targets)==1 and isinstance(n.targets[0],ast.Name) and n.targets[0].id==name)
    lines=text.splitlines(keepends=True)
    return ''.join(lines[:n.lineno-1])+name+' = '+repr(value)+'\n'+''.join(lines[n.end_lineno:])


def once(text,old,new,count=1):
    if text.count(old)!=count:
        raise ValueError('Exact original source change missing or repeated '+old[:100]+' '+str(text.count(old)))
    return text.replace(old,new)


def derive(parent,additions,generated):
    if sha(parent)!=PARENT_SHA:
        raise ValueError('Use the complete actual analytic-J3 terminal/independent bridge')
    result=assign(parent,'SCHEMA','strict-N2048-to-N4096-independent-chart-analytic-J3-material-history-transfer-v1')
    result=assign(result,'CURRENT_MEMORY_SOURCE_SHA256',sha((generated/'angular_refined_independent_chart_memory.py').read_text()))
    result=assign(result,'ANALYTIC_BINDING_SOURCE_SHA256',sha((generated/'angular_refined_analytic_source_binding.py').read_text()))
    result=assign(result,'PARENT_FAMILIES',PARENTS)
    result=once(result,"HISTORY_SOURCE_SHA256 =", "ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256 = '"+OLD_MEMORY+"'\nHISTORY_SOURCE_SHA256 =")
    result=once(result,"Path(__file__).with_name('analytic_j3_source_and_report_binding.py')",
        "Path(__file__).with_name('angular_refined_analytic_source_binding.py')")
    new_requested='''def requested_parent_memory(args):
    """Select the N4096 loader without pretending an N2048 parent used it."""
    selected=None
    for filename in getattr(args,'material_envelope_parent_report',[]):
        record,raw=_record_bytes(filename)
        value=json.loads(raw)
        family=_parent_family(value.get('source_sha256'),value)
        if family['memory_sha256']!=ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256:
            raise ValueError('An actual N parent must have the same complete independent fixed target')
        selected=CURRENT_MEMORY_SOURCE_SHA256
        _same_bytes(record)
    return selected
'''
    result=once(result,body(result,'requested_parent_memory'),new_requested)
    result=once(result,'        unchanged_complete_memory_source_sha256=MEMORY_SOURCE_SHA256,',
        '        original_complete_legacy_memory_source_sha256=MEMORY_SOURCE_SHA256,\n'
        '        actual_N2048_independent_target_memory_source_sha256=ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256,\n'
        '        reference_full_N=2048,current_full_N=4096,\n'
        '        all_old_literal_angles_copied_to_even_columns=True,\n'
        '        all_original_tagged_history_decoded_with_original_N=True,\n'
        '        finite_angular_objective_changed=True,radial_refinement_performed=False,')
    result=once(result,'        strict_terminal_transfer_memory_source_sha256=MEMORY_SOURCE_SHA256,',
        '        strict_terminal_transfer_memory_source_sha256=CURRENT_MEMORY_SOURCE_SHA256,')
    result=once(result,'        original_memory_math_history_scans_and_rows_unchanged=True,',
        '        original_memory_math_and_rows_retained_with_declared_N_history_resolution=True,')
    result=once(result,'        all_original_reference_base_chart_carrier_and_envelope_policy_must_match=True,',
        '        all_fixed_reference_chart_seed_carrier_and_envelope_cap_must_match=True,')
    result=once(result,"        changed_model_fields='strict terminal transfer only: complete source/schema, full explicitly bound C1/detached/adjacent/analytic-J3 policies, and calibration source/endpoint source',",
        "        changed_model_fields='complete declared finite observer plus exact source/schema/dependent identities and bound matrix policies; every fixed field/target/free parameter equal',")
    result=once(result,'    actual_memory_sha=sha(memory.__file__)\n',
        "    actual_memory_sha=sha(memory.__file__)\n"
        "    if (actual_memory_sha!=CURRENT_MEMORY_SOURCE_SHA256 or q.full_N!=4096 or q.N!=1025\n"
        "            or q.base.reference_full_N!=2048):\n"
        "        raise ValueError('Use the actual complete independent target with its refined observer')\n")
    result=once(result,"        if family['memory_sha256']!=actual_memory_sha:\n            raise ValueError('The captured complete parent changed the selected memory family')",
        "        if family['memory_sha256']!=ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256:\n            raise ValueError('The captured N2048 parent changed its original independent-target memory')")
    result=once(result,"or payload.get('N') != q.full_N or payload.get('J') != q.J",
        "or payload.get('N') != 2048 or payload.get('J') != q.J")
    result=once(result,"                or payload.get('fixed_scalar_metric',{}).get('identity_sha256') != q.context.scalar_identity\n                or payload.get('representation',{}).get('base_complete_model') != q.base.model):",
        "                or payload.get('fixed_scalar_metric',{}).get('identity_sha256') != q.context.scalar_identity):")
    result=once(result,"        memory.validate_report_metadata(actual,model_identity=payload['model_identity_sha256'],\n            carrier_sha256=current_carrier_sha)\n        if actual.get('definition') != expected_policy:\n            raise ValueError('Do not reset or change the complete envelope policy/near-active cap during transfer')",
        "        _original_memory().validate_report_metadata(actual,model_identity=payload['model_identity_sha256'],\n            carrier_sha256=current_carrier_sha)\n        _policy_inclusion(actual.get('definition'),expected_policy)\n"
        "        inbound=_complete_input_reports(payload,current_carrier_sha256=current_carrier_sha)\n"
        "        for item in inbound:\n"
        "            if (item['kind']=='complete_preparation' and\n"
        "                    item['payload'].get('reference_definition')!=preparation['reference_definition']):\n"
        "                raise ValueError('Every original history preparation must retain the exact same fixed reference')")
    result=once(result,"            model_binding=model_binding,family=family,",
        "            model_binding=model_binding,family=family,inbound=inbound,")
    result=once(result,"    for path in paths:\n        if path not in manifest:\n            manifest.append(path)",
        "    for parent in parents:\n"
        "        for item in parent['inbound']:\n"
        "            path=Path(item['record']['path']).resolve()\n"
        "            if item['kind']!='complete_preparation' and path not in manifest:manifest.append(path)\n"
        "    for path in paths:\n        if path not in manifest:\n            manifest.append(path)")
    old_grid="""        if (old['implicit_grid'] != envelope.metadata()['implicit_grid']
                or old['historical_address_binding']['origin_carrier']['record']['sha256']
                    != envelope.metadata()['historical_address_binding']['origin_carrier']['record']['sha256']):
            raise ValueError('Keep the entire actual old/current material grid and angle-word union')
        locations = history.Locations(q.J,q.P,q.full_N)
        locations.walk(payload,path=('complete_source_bound_envelope_parent',))"""
    new_grid="""        inclusion=_grid_inclusion(old,envelope.metadata())
        locations = history.Locations(q.J,q.P,2048)
        for item in parent['inbound']:
            if item['kind']!='complete_preparation':
                locations.walk(item['payload'],path=('complete_original_input_history',item['record']['sha256']))
        locations.walk(payload,path=('complete_source_bound_envelope_parent',))"""
    result=once(result,old_grid,new_grid)
    result=once(result,"            actual_complete_walker_role_fingerprints=fingerprints,",
        "            actual_complete_walker_role_fingerprints=fingerprints,\n"
        "            complete_original_role_arrays=copy.deepcopy(old_arrays),\n"
        "            complete_original_typed_rows=copy.deepcopy(rows),\n"
        "            complete_grid_inclusion=inclusion,\n"
        "            complete_inbound_history_records=[dict(record=v['record'],kind=v['kind']) for v in parent['inbound']],\n"
        "            inherited_prior_transfer_metadata=copy.deepcopy(payload.get('material_envelope_transfer')),")
    result=once(result,"                typed_core_sha256=key,actual_new_field_value_inherited=False)",
        "                typed_core_sha256=key,actual_new_field_value_inherited=False,\n"
        "                complete_original_typed_row=copy.deepcopy(row))")
    result=once(result,"            actual_origin_model_identity_sha256=q.identity,",
        "            reference_full_N=2048,current_full_N=4096,\n            actual_origin_model_identity_sha256=q.identity,")
    result=once(result,"        actual_current_driver_sha256=caller_record['sha256'],\n        actual_current_model_identity_sha256=q.identity,",
        "        actual_current_driver_sha256=caller_record['sha256'],\n"
        "        actual_current_driver_source=copy.deepcopy(caller_record),\n"
        "        reference_full_N=2048,current_full_N=4096,\n"
        "        actual_current_model_identity_sha256=q.identity,")
    result=once(result,"                or str(saved['base_so3_model_identity_sha256'].item()) != q.base.identity",
        "                or str(saved['base_so3_model_identity_sha256'].item()) != payload['representation']['base_model_identity_sha256']")
    result=once(result,"int(saved['working_full_angles'].item()) != q.full_N",
        "int(saved['working_full_angles'].item()) != 2048")
    result=once(result,"        actual_full_free_variable_count=q.free_size,",
        "        actual_full_free_variable_count=q.free_size,\n"
        "        source_current_full_N=2048,current_full_N=4096,reference_full_N=2048,")
    result=once(result,"            or value.get('actual_full_free_variable_count') != report['original_variables']",
        "            or value.get('actual_full_free_variable_count') != report['original_variables']\n"
        "            or value.get('source_current_full_N')!=2048 or value.get('current_full_N')!=4096\n"
        "            or value.get('reference_full_N')!=2048")
    result=once(result,"            or actual_memory_sha not in (MEMORY_SOURCE_SHA256,CURRENT_MEMORY_SOURCE_SHA256)\n            or envelope.get('source_sha256') != actual_memory_sha):",
        "            or actual_memory_sha!=CURRENT_MEMORY_SOURCE_SHA256\n"
        "            or value.get('reference_full_N')!=2048 or value.get('current_full_N')!=4096\n"
        "            or envelope.get('source_sha256') != actual_memory_sha):")
    result=once(result,"    known_reports = {}\n",
        "    _reread_transfer_parents(value,model,envelope,caller_source_sha256,carrier_sha256)\n    known_reports = {}\n")
    result=once(result,"                !=CURRENT_MEMORY_SOURCE_SHA256 for p in parents):",
        "                !=ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256 for p in parents):")
    result=once(result,"                or family['memory_sha256']!=actual_memory_sha",
        "                or family['memory_sha256']!=ORIGINAL_CURRENT_MEMORY_SOURCE_SHA256")
    start=result.index("        origin=parent.get('inherited_prior_independent_branch_origin')",result.index('def validate_metadata('))
    end=result.index("        _digest(parent.get('actual_model_identity_sha256'))",start)
    result=result[:start]+"""        inherited=parent.get('inherited_prior_transfer_metadata')
        if not isinstance(inherited,dict):
            raise ValueError('Keep the entire prior terminal lineage, including unresolved peer obligations')
        if parent.get('inherited_prior_independent_branch_origin')!=inherited.get('independent_branch_origin'):
            raise ValueError('The complete prior independent origin must not be rewritten for the current N')
"""+result[end:]
    result=once(result,"binding.get('full_base_reference_chart_profile_and_partition_equal')",
        "binding.get('full_fixed_reference_chart_profile_seed_mesh_Q_gamma_partition_and_free_layout_equal')")
    result=once(result,"binding.get('only_explicit_source_schema_and_matrix_working_policy_fields_changed')",
        "binding.get('only_explicit_observation_source_schema_and_matrix_working_policy_fields_changed')")
    result=once(result,"            _digest(origin.get('first_discovered_source_full_point_sha256'))",
        "            old_row=source['complete_original_typed_rows'][origin['source_row_ordinal']]\n"
        "            if origin.get('complete_original_typed_row')!=old_row or _typed_key(old_row)!=_typed_key(row):\n"
        "                raise ValueError('Keep every original full typed row and its prior discovery lineage')\n"
        "            _digest(origin.get('first_discovered_source_full_point_sha256'))")
    result=once(result,"        continuous_certificate=False)\n",
        "        reference_full_N=2048,current_full_N=4096,\n"
        "        all_original_literal_angles_and_fixed_target_retained=True,\n"
        "        radial_refinement_performed=False,continuous_certificate=False)\n")
    result+='\n\n'+'\n\n'.join(body(additions,n.name).rstrip() for n in ast.parse(additions).body if isinstance(n,ast.FunctionDef))+'\n'
    ast.parse(result);compile(result,'angular_refined_analytic_history_transfer.py','exec')
    if len(result.encode())>=100000:
        raise ValueError('Keep the entire transfer below 100KB')
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--parent-source',type=Path,required=True)
    p.add_argument('--additions-source',type=Path,required=True)
    p.add_argument('--generated-directory',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    value=derive(a.parent_source.read_text(),a.additions_source.read_text(),a.generated_directory)
    a.output.write_text(value)
    print(json.dumps(dict(bytes=len(value.encode()),sha256=sha(value))))


if __name__=='__main__':
    main()
