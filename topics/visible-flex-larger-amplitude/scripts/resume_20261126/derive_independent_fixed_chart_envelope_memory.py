#!/usr/bin/env python3
"""Reproduce the complete independent fixed-chart envelope memory from its full parent.

Only UTF-8 text, SHA256, AST parsing and compilation are used here. This tool
does not import, execute or evaluate any scientific source or example.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PLAN = json.loads(r'''{
  "schema": "complete-independent-fixed-chart-memory-text-derivation-v1",
  "parent": {
    "path": "scripts/resume_20261126/complete_material_envelope_memory_compatible_current.py",
    "bytes": 45188,
    "sha256": "1e2ca9ec89d407d6d187ed60fe94406820f098dfca7c2b70c4f0645ea9bcdfa9"
  },
  "output": {
    "path": "scripts/resume_20261126/complete_material_envelope_memory_independent_chart.py",
    "bytes": 48544,
    "sha256": "4d92ca2387523a76bbea0a3444e0665c306369dd0351c3354c998a09884e043b"
  },
  "patches": [
    {
      "old": "\"\"\"Complete literal material envelope with an explicit new working-row policy.",
      "new": "\"\"\"Complete material envelope for the explicitly independent frozen run08 chart.\n\nThe target is defined by the entire current scalar/model/reference and all 160\nliteral fixed chart words before any field evaluation. The historical chart and\nits numerical values are not reused as the new target. Complete old/current\nmaterial address obligations are retained and interpreted in the new phi0 chart.",
      "count": 1
    },
    {
      "old": "SCHEMA = 'complete-material-envelope-memory-and-typed-policy-v1'",
      "new": "SCHEMA = 'complete-independent-fixed-chart-material-envelope-memory-and-typed-policy-v1'",
      "count": 1
    },
    {
      "old": "SCAN_SCHEMA = 'complete-material-envelope-same-point-scan-v1'",
      "new": "SCAN_SCHEMA = 'complete-independent-fixed-chart-material-envelope-same-point-scan-v1'",
      "count": 1
    },
    {
      "old": "DEFINITION_SCHEMA = 'literal-old-current-grid-envelope-new-working-policy-v1'",
      "new": "DEFINITION_SCHEMA = 'literal-old-current-grid-independent-fixed-chart-working-policy-v1'",
      "count": 1
    },
    {
      "old": "BINDING_SCHEMA = 'material-envelope-carrier-path-binding-v1'",
      "new": "BINDING_SCHEMA = 'material-envelope-independent-fixed-chart-binding-v1'",
      "count": 1
    },
    {
      "old": "6cc95526e5305fa0265b96f66d322bbba612b8702d5ebcc5ec48a9fb29639d19",
      "new": "105289ba7c454f671c8eae086b31a4ea01b06978101503cd0ef283320fc85361",
      "count": 1
    },
    {
      "old": "CURRENT_COMPATIBILITY_PRODUCER_NAME",
      "new": "INDEPENDENT_FIXED_TARGET_PRODUCER_NAME",
      "count": 2
    },
    {
      "old": "restore_actual_run05_carrier_for_compatible_current_run08.py",
      "new": "freeze_run08_fixed_chart_and_restore_run05_carrier.py",
      "count": 1
    },
    {
      "old": "ORIGIN_CHART_SHA = '90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e'\n",
      "new": "ORIGIN_CHART_SHA = '90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e'\nCURRENT_FIXED_CHART_SHA = '7c4c9b736c0c8081e9f00a131db5fb63af224aa64fb476c07c78c09b5288bb48'\nCURRENT_REFERENCE_MODEL_SHA = '492456a67601cac752dc8e5cb79c14eaccc7339b2d3206f0d570bb60b02c5c5e'\nFIXED_TARGET_SCHEMA = 'independent-run08-frozen-complete-scalar-and-material-chart-v1'\n",
      "count": 1
    },
    {
      "old": "        original_full_free_space_norm_and_objective_unchanged=True,\n",
      "new": "        original_full_free_space_norm_and_objective_formula_unchanged=True,\n        historical_fixed_chart_sha256=ORIGIN_CHART_SHA,\n        independent_fixed_chart_sha256=CURRENT_FIXED_CHART_SHA,\n        complete_independent_fixed_target_schema=FIXED_TARGET_SCHEMA,\n        complete_target_definition_and_actual_current_files_required=True,\n        target_fixed_before_any_current_field_evaluation=True,\n        historical_angles_reinterpreted_as_new_fixed_chart_phi0=True,\n        same_historical_physical_points_claimed=False,\n        same_original_fixed_chart=False,same_mathematical_g_claimed=False,\n        old_values_or_scientific_certificates_inherited=False,\n        unresolved_parallel_history_remains_an_explicit_obligation=True,\n",
      "count": 1
    },
    {
      "old": "def _validate_actual_current_binding(binding, *, actual_model=None, current_carrier=None,\n        current_preparation_report=None, current_reference_bundle=None,\n        current_node_report=None, current_scalar_input=None):\n    \"\"\"Verify the entire actual current projection with the whole pinned producer.\"\"\"\n    if not isinstance(binding,dict):\n        raise ValueError('The complete actual current path binding is required')\n    value=binding.get('current_input_compatibility')\n    if (not isinstance(value,dict)\n            or binding.get('current_input_compatibility_identity_sha256')!=canonical(value)\n            or value.get('producer_source_sha256')!=RESTORER_SHA\n            or binding.get('origin_carrier')!=value.get('historical_carrier')\n            or binding.get('current_carrier')!=value.get('current_carrier')):\n        raise ValueError('Current projection and whole old/current carrier evidence disagree')\n    records=dict(current_carrier=current_carrier,\n        current_preparation_report=current_preparation_report,\n        current_reference_bundle=current_reference_bundle,current_node_report=current_node_report,\n        current_scalar_input=current_scalar_input)\n    for key,actual in list(records.items()):\n        declared=value.get(key)\n        if not isinstance(declared,dict):\n            raise ValueError('Missing full current projection file record '+key)\n        if actual is None:\n            records[key]=copy.deepcopy(declared)\n        elif actual!=declared:\n            raise ValueError('The actual caller input differs from its full producer '+key)\n    preparation=_read_bound_json(records['current_preparation_report'])\n    model=preparation.get('reference_definition')\n    if (not isinstance(model,dict) or preparation.get('source_sha256')!=PREPARATION_SHA\n            or preparation.get('schema')!='R690-independent-axisymmetric-SO3-preparation-v1'\n            or preparation.get('complete') is not True\n            or preparation.get('reference_model_identity_sha256')!=canonical(model)\n            or (actual_model is not None and actual_model!=model)):\n        raise ValueError('Bind the same actual complete frozen reference model')\n    path=Path(__file__).with_name(INDEPENDENT_FIXED_TARGET_PRODUCER_NAME)\n    if sha(path)!=RESTORER_SHA:\n        raise ValueError('Use the complete current projection producer source')\n    module_name='_complete_run08_current_projection_'+RESTORER_SHA[:16]\n    spec=importlib.util.spec_from_file_location(module_name,path)\n    if spec is None or spec.loader is None:\n        raise ValueError('The full current projection source cannot be loaded')\n    module=importlib.util.module_from_spec(spec)\n    sys.modules[module_name]=module\n    spec.loader.exec_module(module)\n    if (sha(module.__file__)!=RESTORER_SHA\n            or sha(module.validate_current_input_compatibility.__code__.co_filename)!=RESTORER_SHA):\n        raise ValueError('The actual complete projection validator source differs')\n    result=module.validate_current_input_compatibility(value,actual_model=model,**records)\n    if (result.get('producer_source_sha256')!=RESTORER_SHA\n            or result.get('compatibility_identity_sha256')!=canonical(value)\n            or result.get('actual_current_model_identity_sha256')!=canonical(model)\n            or result.get('whole_old_carrier_and_full_current_input_bytes_rechecked') is not True\n            or result.get('same_complete_scalar_formula_and_fixed_chart') is not True\n            or result.get('scientific_certificates_inherited') is not False):\n        raise ValueError('The full actual projection validator did not return its binding')\n    return result\n",
      "new": "def _validate_independent_target_binding(binding, *, actual_model=None, current_carrier=None,\n        current_preparation_report=None, current_reference_bundle=None,\n        current_node_report=None, current_scalar_input=None):\n    \"\"\"Recheck the complete new target and actual files with its whole producer.\"\"\"\n    if not isinstance(binding,dict) or binding.get('schema')!=BINDING_SCHEMA:\n        raise ValueError('The complete independent fixed-target path binding is required')\n    value=binding.get('independent_fixed_target_binding')\n    target=binding.get('fixed_target_definition')\n    if (not isinstance(value,dict) or not isinstance(target,dict)\n            or binding.get('independent_fixed_target_binding_identity_sha256')!=canonical(value)\n            or binding.get('fixed_target_definition_identity_sha256')!=canonical(target)\n            or value.get('fixed_target_definition')!=target\n            or value.get('fixed_target_definition_identity_sha256')!=canonical(target)\n            or value.get('producer_source_sha256')!=RESTORER_SHA\n            or target.get('schema')!=FIXED_TARGET_SCHEMA\n            or target.get('definition_source_sha256')!=RESTORER_SHA\n            or target.get('current_reference_model_identity_sha256')!=CURRENT_REFERENCE_MODEL_SHA\n            or target.get('fixed_chart_core_array_record',{}).get('sha256')!=CURRENT_FIXED_CHART_SHA\n            or target.get('historical_original_chart_core_sha256')!=ORIGIN_CHART_SHA\n            or target.get('same_original_fixed_chart') is not False\n            or target.get('same_mathematical_g_claimed') is not False\n            or target.get('old_field_values_or_scientific_certificates_inherited') is not False\n            or binding.get('origin_carrier')!=value.get('historical_carrier')\n            or binding.get('current_carrier')!=value.get('current_carrier')):\n        raise ValueError('The full independent target, actual input and complete carrier evidence disagree')\n    records=dict(current_carrier=current_carrier,\n        current_preparation_report=current_preparation_report,\n        current_reference_bundle=current_reference_bundle,current_node_report=current_node_report,\n        current_scalar_input=current_scalar_input)\n    for key,actual in list(records.items()):\n        declared=value.get(key)\n        if not isinstance(declared,dict):\n            raise ValueError('Missing full independent-target input file record '+key)\n        if actual is None:\n            records[key]=copy.deepcopy(declared)\n        elif actual!=declared:\n            raise ValueError('The actual caller input differs from its full producer '+key)\n    preparation=_read_bound_json(records['current_preparation_report'])\n    model=preparation.get('reference_definition')\n    if (not isinstance(model,dict) or preparation.get('source_sha256')!=PREPARATION_SHA\n            or preparation.get('schema')!='R690-independent-axisymmetric-SO3-preparation-v1'\n            or preparation.get('complete') is not True\n            or preparation.get('reference_model_identity_sha256')!=canonical(model)\n            or canonical(model)!=CURRENT_REFERENCE_MODEL_SHA\n            or target.get('complete_current_reference_model')!=model\n            or target.get('complete_current_reference_bundle_sha256')!=records['current_reference_bundle']['sha256']\n            or (actual_model is not None and actual_model!=model)):\n        raise ValueError('Bind the actual complete new frozen reference model and target')\n    path=Path(__file__).with_name(INDEPENDENT_FIXED_TARGET_PRODUCER_NAME)\n    if sha(path)!=RESTORER_SHA:\n        raise ValueError('Use the whole independent fixed-target producer source')\n    module_name='_complete_run08_independent_fixed_target_'+RESTORER_SHA[:16]\n    spec=importlib.util.spec_from_file_location(module_name,path)\n    if spec is None or spec.loader is None:\n        raise ValueError('The full independent fixed-target source cannot be loaded')\n    module=importlib.util.module_from_spec(spec)\n    sys.modules[module_name]=module\n    spec.loader.exec_module(module)\n    if (sha(module.__file__)!=RESTORER_SHA\n            or sha(module.validate_independent_fixed_target_binding.__code__.co_filename)!=RESTORER_SHA):\n        raise ValueError('The actual complete independent target validator source differs')\n    result=module.validate_independent_fixed_target_binding(value,actual_model=model,**records)\n    if (result.get('producer_source_sha256')!=RESTORER_SHA\n            or result.get('independent_fixed_target_binding_identity_sha256')!=canonical(value)\n            or result.get('fixed_target_definition_identity_sha256')!=canonical(target)\n            or result.get('actual_current_model_identity_sha256')!=canonical(model)\n            or result.get('current_fixed_chart_core_sha256')!=CURRENT_FIXED_CHART_SHA\n            or result.get('whole_old_carrier_and_full_current_input_bytes_rechecked') is not True\n            or result.get('same_complete_scalar_formula') is not True\n            or result.get('complete_current_fixed_chart_verified') is not True\n            or result.get('all_historical_and_current_material_addresses_still_required') is not True\n            or result.get('same_original_fixed_chart') is not False\n            or result.get('same_mathematical_g_claimed') is not False\n            or result.get('scientific_certificates_inherited') is not False):\n        raise ValueError('The whole independent target validator did not return its exact binding')\n    return result\n",
      "count": 1
    },
    {
      "old": "_validate_actual_current_binding(",
      "new": "_validate_independent_target_binding(",
      "count": 2
    },
    {
      "old": "current_projection_validation",
      "new": "independent_target_validation",
      "count": 6
    },
    {
      "old": "current_input_compatibility_validation=",
      "new": "independent_fixed_target_validation=",
      "count": 2
    },
    {
      "old": "Use the actual complete compatible reference and full material chart",
      "new": "Use the actual complete independently frozen reference and full material chart",
      "count": 1
    },
    {
      "old": "    independent_target_validation = None\n    if binding_path is None:\n        if (current['record']['sha256'] != ORIGIN_CARRIER_SHA\n                or actual_model.get('original_warm_bundle_sha256') != ORIGIN_WARM_SHA):\n            raise ValueError('A differing current carrier needs the complete actual old-carrier path binding')\n        old = current\n        binding = dict(schema=BINDING_SCHEMA, origin_carrier=copy.deepcopy(current['record']),\n            current_carrier=copy.deepcopy(current['record']), identical_whole_file_directly_read=True)\n    else:\n        binding_record = file_record(binding_path)\n        binding = validate_public_binding(_read_bound_json(binding_record), current_input=current['record'])\n        if file_record(binding['current_carrier']['path']) != current['record']:\n            raise ValueError('Binding path is not the same actual current file')\n        old = read_carrier(binding['origin_carrier']['path'], ORIGIN_CARRIER_SHA)\n        if old['record'] != binding['origin_carrier']:\n            raise ValueError('Actual original file record changed')\n        binding = dict(binding, binding_file=binding_record)\n        independent_target_validation = _validate_independent_target_binding(binding,\n            actual_model=actual_model,current_carrier=current['record'],\n            current_preparation_report=file_record(args.preparation_report),\n            current_reference_bundle=file_record(args.reference_bundle),\n            current_node_report=file_record(args.node_report),current_scalar_input=file_record(args.scalar_input))\n",
      "new": "    if binding_path is None:\n        raise ValueError('The independent new target requires its complete explicit path binding')\n    binding_record = file_record(binding_path)\n    binding = validate_public_binding(_read_bound_json(binding_record), current_input=current['record'])\n    if file_record(binding['current_carrier']['path']) != current['record']:\n        raise ValueError('Binding path is not the same actual current file')\n    old = read_carrier(binding['origin_carrier']['path'], ORIGIN_CARRIER_SHA)\n    if old['record'] != binding['origin_carrier']:\n        raise ValueError('Actual original file record changed')\n    binding = dict(binding, binding_file=binding_record)\n    independent_target_validation = _validate_independent_target_binding(binding,\n        actual_model=actual_model,current_carrier=current['record'],\n        current_preparation_report=file_record(args.preparation_report),\n        current_reference_bundle=file_record(args.reference_bundle),\n        current_node_report=file_record(args.node_report),current_scalar_input=file_record(args.scalar_input))\n",
      "count": 1
    },
    {
      "old": "    chart = q.base.context.core\n    if (str(chart.dtype) != 'float64' or list(chart.shape) != [160]\n            or _array_sha('float64',(160,),chart.tobytes()) != ORIGIN_CHART_SHA):\n        raise ValueError('The fixed material chart differs from the original complete chart')\n",
      "new": "    chart = q.base.context.core\n    target = binding['fixed_target_definition']\n    if (str(chart.dtype) != 'float64' or list(chart.shape) != [160]\n            or _array_sha('float64',(160,),chart.tobytes()) != CURRENT_FIXED_CHART_SHA\n            or [float(v).hex() for v in chart] != target['fixed_chart_core_binary64_hex']\n            or target['complete_current_reference_model'] != actual_model\n            or target['current_reference_model_identity_sha256'] != canonical(actual_model)):\n        raise ValueError('The complete current chart differs from the independently frozen target')\n",
      "count": 1
    },
    {
      "old": "            current_carrier_sha256=self.current_sha,\n            historical_address_binding=",
      "new": "            current_carrier_sha256=self.current_sha,\n            independent_fixed_target_definition_identity_sha256=binding['fixed_target_definition_identity_sha256'],\n            same_original_fixed_chart=False,same_mathematical_g_claimed=False,\n            historical_address_binding=",
      "count": 1
    },
    {
      "old": "    path_binding=bound.get('actual_path_binding',{})\n    independent_target_validation=None\n    if path_binding.get('identical_whole_file_directly_read') is not True:\n        verified_path_binding=validate_public_binding(path_binding,current_input=current)\n        independent_target_validation=_validate_independent_target_binding(\n            verified_path_binding,current_carrier=current)\n    elif (current.get('sha256')!=ORIGIN_CARRIER_SHA\n            or origin!=current or path_binding.get('origin_carrier')!=origin\n            or path_binding.get('current_carrier')!=current):\n        raise ValueError('A direct historical whole-file case cannot represent different current input')\n",
      "new": "    path_binding=bound.get('actual_path_binding',{})\n    if path_binding.get('identical_whole_file_directly_read') is True:\n        raise ValueError('A direct historical carrier is not the independently frozen new target')\n    verified_path_binding=validate_public_binding(path_binding,current_input=current)\n    independent_target_validation=_validate_independent_target_binding(\n        verified_path_binding,current_carrier=current)\n    if (value.get('independent_fixed_target_definition_identity_sha256')\n                !=independent_target_validation['fixed_target_definition_identity_sha256']\n            or value.get('same_original_fixed_chart') is not False\n            or value.get('same_mathematical_g_claimed') is not False):\n        raise ValueError('The report does not retain its complete independent fixed target')\n",
      "count": 1
    }
  ]
}''')

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    args = parser.parse_args()
    topic = args.repo.resolve()/'topics/visible-flex-larger-amplitude'
    parent = PLAN['parent']
    raw = (topic/parent['path']).read_bytes()
    if len(raw)!=parent['bytes'] or digest(raw)!=parent['sha256']:
        raise ValueError('The complete published parent source differs')
    text = raw.decode('utf-8')
    for index, item in enumerate(PLAN['patches']):
        if text.count(item['old'])!=item['count']:
            raise ValueError('Complete exact replacement occurrence mismatch: '+str(index))
        text = text.replace(item['old'],item['new'])
    result = text.encode('utf-8')
    expected = PLAN['output']
    if len(result)!=expected['bytes'] or digest(result)!=expected['sha256']:
        raise ValueError('The full reproduced memory source differs')
    filename = Path(expected['path']).name
    ast.parse(text,filename=filename)
    compile(text,filename,'exec')
    args.outdir.mkdir(parents=True,exist_ok=True)
    target = args.outdir/filename
    target.write_bytes(result)
    print(json.dumps(dict(schema=PLAN['schema'],path=str(target),
        bytes=len(result),sha256=digest(result),whole_source_reproduced=True,
        scientific_imports_or_evaluations=False),sort_keys=True))

if __name__=='__main__':
    main()
