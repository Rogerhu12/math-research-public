#!/usr/bin/env python3
"""Complete stdlib derivation of the explicit run08 independent fixed-chart input.

The entire prior 6cc producer is read and retained as a historical source.
No scientific module is imported or executed by this derivation script.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PARENT_SHA256 = '6cc95526e5305fa0265b96f66d322bbba612b8702d5ebcc5ec48a9fb29639d19'
DERIVED_SHA256 = '105289ba7c454f671c8eae086b31a4ea01b06978101503cd0ef283320fc85361'
DERIVED_BYTES = 61371
PATCHES = [
  {
    "start": 1,
    "end": 2,
    "expected": "\"\"\"Restore the actually observed run05 carrier, accepting only its full SHA.\n",
    "replacement": "\"\"\"Freeze the entire actual run08 chart as an independent target and restore old G.\n"
  },
  {
    "start": 3,
    "end": 15,
    "expected": "This is a new public-Actions input reconstruction, not a repeated surface\nsolve.  The old exact scalar computation is determined by its complete\nparameters and its genuinely recorded 2397 live leaves.  The original\ninteger/Fraction leaf arithmetic, heap priorities and tie order are kept.\nNo old scalar/node file is fabricated or relabelled.  Current actual files\nremain separately bound; their complete mathematical projection is checked.\nOnly a byte-identical old carrier authorizes the returned old address input.\nThis complete revision binds the real run08 warm/node/scalar/reference bytes,\nthen separately verifies the entire consumed mesh, fixed chart and scalar\nprojection against the original historical definition. Whole warm/H equality\nis neither required nor claimed. The old complete carrier and all 2397-leaf\narithmetic remain mandatory; this is not a substitute old-address packet.\n",
    "replacement": "The current 7c4c chart is a new fixed mathematical input, not the historical\n90e6 chart. Its complete 160 literal words, scalar/model/domain definition and\nwhole reference identity are saved before any new field evaluation. No old\ntarget/field/geometry identity or angle conjugacy is inherited.\n\nThe complete historical dc5 observation carrier is nevertheless reconstructed\nwith the original scalar parameters, observed 2397 leaves and all original\narray arithmetic, accepting only its whole SHA and 227202 bytes. That historical\ninput supplies all old material addresses, not old physical values. The new\nconsumer must retain P0 plus complete old/current grids and unresolved parallel\ntyped-history obligations. This is not a reduced address sample or a repair\nthat simply relabels the old chart constant.\n"
  },
  {
    "start": 29,
    "end": 29,
    "expected": "",
    "replacement": "import struct\n"
  },
  {
    "start": 32,
    "end": 35,
    "expected": "SCHEMA = 'actual-run05-carrier-reconstruction-from-current-consumed-projection-v2'\nPARENT_COMPLETE_SOURCE_SHA256 = '8c1e2d8f71bb08b33f99f9c187dbed2994776fc64b7114e1cea921a4fecff449'\nBINDING_SCHEMA = 'material-envelope-carrier-path-binding-v1'\n",
    "replacement": "SCHEMA = 'independent-run08-fixed-current-chart-and-complete-run05-carrier-input-v1'\nPARENT_COMPLETE_SOURCE_SHA256 = '6cc95526e5305fa0265b96f66d322bbba612b8702d5ebcc5ec48a9fb29639d19'\nBINDING_SCHEMA = 'material-envelope-independent-fixed-chart-binding-v1'\n"
  },
  {
    "start": 202,
    "end": 203,
    "expected": "COMPATIBILITY_SCHEMA = 'actual-current-reference-projection-compatible-with-run05-v2'\n",
    "replacement": "COMPATIBILITY_SCHEMA = 'independent-current-chart-and-historical-carrier-input-binding-v1'\n"
  },
  {
    "start": 216,
    "end": 216,
    "expected": "",
    "replacement": "\nCURRENT_CHART_SHA256 = '7c4c9b736c0c8081e9f00a131db5fb63af224aa64fb476c07c78c09b5288bb48'\nCURRENT_REFERENCE_SHA256 = 'eeb55084744c60a5ed2e2bbb4343b01c73028a6ab61b1216142e4b3bf57dd6b4'\nCURRENT_REFERENCE_MODEL_SHA256 = '492456a67601cac752dc8e5cb79c14eaccc7339b2d3206f0d570bb60b02c5c5e'\nTARGET_SCHEMA = 'independent-run08-frozen-complete-scalar-and-material-chart-v1'\n\n\ndef chart_words_record(words):\n    \"\"\"Canonical full 160 binary64 words; no truncated coefficient surrogate.\"\"\"\n    if not isinstance(words,list) or len(words)!=160:\n        raise ValueError('A complete 160-coefficient fixed chart is required')\n    values=[]\n    for word in words:\n        if not isinstance(word,str):\n            raise ValueError('The chart uses canonical literal binary64 hex strings')\n        value=float.fromhex(word)\n        if not math.isfinite(value) or value.hex()!=word:\n            raise ValueError('The chart word is not a canonical finite binary64 value')\n        values.append(value)\n    raw=b''.join(struct.pack('<d',value) for value in values)\n    digest=hashlib.sha256(b'float64')\n    digest.update(json.dumps([160]).encode())\n    digest.update(raw)\n    return dict(dtype='float64',shape=[160],sha256=digest.hexdigest(),\n        binary64_byte_order='little',all_words=len(values))\n\n\ndef fixed_target_definition(*, model, scalar_parameters, chart_words, node_definitions,\n                            reference_bundle):\n    if (canonical(model)!=CURRENT_REFERENCE_MODEL_SHA256\n            or model.get('fixed_chart_core_sha256')!=CURRENT_CHART_SHA256\n            or model.get('mesh_sha256')!=ORIGIN_MESH_SHA256\n            or model.get('original_scalar_parameters_identity_sha256')!=PARAMETERS_SHA\n            or canonical(scalar_parameters)!=PARAMETERS_SHA\n            or chart_words_record(chart_words)['sha256']!=CURRENT_CHART_SHA256\n            or [str(v) for v in chart_words[:3]]!=model.get('fixed_core_first3')\n            or reference_bundle.get('sha256')!=CURRENT_REFERENCE_SHA256\n            or len(node_definitions)!=923):\n        raise ValueError('Freeze this entire actual new chart target, not the historical chart')\n    return dict(schema=TARGET_SCHEMA,definition_source_sha256=sha(__file__),\n        complete_current_reference_model=model,\n        current_reference_model_identity_sha256=CURRENT_REFERENCE_MODEL_SHA256,\n        complete_current_reference_bundle_sha256=CURRENT_REFERENCE_SHA256,\n        complete_scalar_parameters=scalar_parameters,\n        complete_scalar_parameters_identity_sha256=PARAMETERS_SHA,\n        complete_current_fixed_scalar_profile_definition=model['fixed_scalar_profile_definition'],\n        current_fixed_scalar_metric_identity_sha256=model['fixed_scalar_metric_identity_sha256'],\n        fixed_chart_core_binary64_hex=list(chart_words),\n        fixed_chart_core_array_record=chart_words_record(chart_words),\n        exact_scalar_node_definitions=[list(v) for v in node_definitions],\n        exact_scalar_node_definitions_identity_sha256=canonical(node_definitions),\n        exact_node_recipe_source_sha256=WARM_SOURCE_SHA,\n        complete_literal_mesh_array_sha256=ORIGIN_MESH_SHA256,\n        exact_literal_width_hex=float(.05).hex(),\n        mathematical_target='ds^2+a_R690(s)^2*dTheta_current(phi0)^2',\n        fixed_chart='Theta_current is defined by all 160 literal coefficients in this definition',\n        original_complete_scalar_source_sha256=REFERENCE_SHA,\n        historical_original_chart_core_sha256=ORIGIN_CHART_SHA256,\n        same_original_fixed_chart=False,same_mathematical_g_claimed=False,\n        exact_old_to_new_chart_conjugacy_claimed=False,\n        target_fixed_before_any_field_or_direction=True,\n        current_free_core_does_not_redefine_target=True,\n        current_free_height_is_not_a_target_parameter=True,\n        old_and_current_literal_material_addresses_all_retained=True,\n        historical_angles_reinterpreted_as_new_fixed_chart_phi0=True,\n        same_historical_physical_points_claimed=False,\n        unknown_parallel_typed_priorities_reconstructed=False,\n        unresolved_parallel_history_remains_an_explicit_obligation=True,\n        original_branch_replaced_or_declared_finished=False,\n        old_field_values_or_scientific_certificates_inherited=False)\n\n\ndef validate_fixed_target_definition(value, *, actual_model, reference_bundle, node):\n    if not isinstance(value,dict):\n        raise ValueError('Keep the entire independent fixed-target definition')\n    definitions=[[str(F(v['S_coefficient'])),str(F(v['constant']))] for v in node['true_scalar_nodes']]\n    expected=fixed_target_definition(model=actual_model,\n        scalar_parameters=value.get('complete_scalar_parameters'),\n        chart_words=value.get('fixed_chart_core_binary64_hex'),\n        node_definitions=definitions,reference_bundle=reference_bundle)\n    if value!=expected:\n        raise ValueError('The complete new target definition differs from its actual files')\n    return dict(schema=TARGET_SCHEMA,definition_identity_sha256=canonical(value),\n        current_reference_model_identity_sha256=CURRENT_REFERENCE_MODEL_SHA256,\n        current_fixed_chart_core_sha256=CURRENT_CHART_SHA256,\n        historical_original_chart_core_sha256=ORIGIN_CHART_SHA256,\n        same_original_fixed_chart=False,same_mathematical_g_claimed=False,\n        old_values_or_certificates_inherited=False)\n\n\n"
  },
  {
    "start": 316,
    "end": 317,
    "expected": "def validate_current_input_compatibility(value, *, actual_model, current_carrier,\n",
    "replacement": "def validate_independent_fixed_target_binding(value, *, actual_model, current_carrier,\n"
  },
  {
    "start": 333,
    "end": 334,
    "expected": "            or value.get('current_fixed_chart_core_sha256')!=ORIGIN_CHART_SHA256\n",
    "replacement": "            or value.get('current_fixed_chart_core_sha256')!=CURRENT_CHART_SHA256\n"
  },
  {
    "start": 338,
    "end": 339,
    "expected": "        raise ValueError('The current input projection is not the entire fixed historical mathematical input')\n",
    "replacement": "        raise ValueError('The current projection is not the complete declared independent fixed-chart input')\n"
  },
  {
    "start": 354,
    "end": 354,
    "expected": "",
    "replacement": "            or canonical(actual_model)!=CURRENT_REFERENCE_MODEL_SHA256\n            or current_reference_bundle.get('sha256')!=CURRENT_REFERENCE_SHA256\n"
  },
  {
    "start": 361,
    "end": 362,
    "expected": "            or actual_model.get('fixed_chart_core_sha256')!=ORIGIN_CHART_SHA256\n",
    "replacement": "            or actual_model.get('fixed_chart_core_sha256')!=CURRENT_CHART_SHA256\n"
  },
  {
    "start": 365,
    "end": 366,
    "expected": "        raise ValueError('Full current model/files and original scalar/domain/chart must agree')\n",
    "replacement": "        raise ValueError('Full current model/files and declared new chart with original scalar/domain must agree')\n"
  },
  {
    "start": 391,
    "end": 392,
    "expected": "    for key in ('same_complete_scalar_formula_verified','same_complete_fixed_material_chart_verified',\n",
    "replacement": "    target=value.get('fixed_target_definition')\n    target_validation=validate_fixed_target_definition(target,actual_model=actual_model,\n        reference_bundle=current_reference_bundle,node=node)\n    if canonical(target)!=value.get('fixed_target_definition_identity_sha256'):\n        raise ValueError('The complete independent fixed target identity changed')\n    for key in ('same_complete_scalar_formula_verified','complete_current_fixed_material_chart_verified',\n"
  },
  {
    "start": 396,
    "end": 397,
    "expected": "    for key in ('historical_whole_warm_recreated','historical_whole_warm_or_height_equality_claimed',\n",
    "replacement": "    for key in ('same_original_fixed_chart','same_mathematical_g_claimed','exact_old_to_new_chart_conjugacy_claimed',\n                'historical_whole_warm_recreated','historical_whole_warm_or_height_equality_claimed',\n"
  },
  {
    "start": 438,
    "end": 439,
    "expected": "        compatibility_identity_sha256=canonical(value),\n",
    "replacement": "        independent_fixed_target_binding_identity_sha256=canonical(value),\n"
  },
  {
    "start": 445,
    "end": 446,
    "expected": "        current_fixed_chart_core_sha256=ORIGIN_CHART_SHA256,\n",
    "replacement": "        current_fixed_chart_core_sha256=CURRENT_CHART_SHA256,\n        historical_original_chart_core_sha256=ORIGIN_CHART_SHA256,\n        fixed_target_definition_identity_sha256=canonical(target),\n        independent_fixed_target=target_validation,\n        same_original_fixed_chart=False,same_mathematical_g_claimed=False,\n"
  },
  {
    "start": 449,
    "end": 450,
    "expected": "        same_complete_scalar_formula_and_fixed_chart=True,\n",
    "replacement": "        same_complete_scalar_formula=True,complete_current_fixed_chart_verified=True,\n        all_historical_and_current_material_addresses_still_required=True,\n"
  },
  {
    "start": 591,
    "end": 592,
    "expected": "            or current_model.get('source_sha256') != REFERENCE_SHA):\n",
    "replacement": "            or current_model.get('source_sha256') != REFERENCE_SHA\n            or canonical(current_model)!=CURRENT_REFERENCE_MODEL_SHA256\n            or current_identity['actual_reference_output']['sha256']!=CURRENT_REFERENCE_SHA256):\n"
  },
  {
    "start": 617,
    "end": 618,
    "expected": "    if (ref.array_sha(mesh)!=ORIGIN_MESH_SHA256 or ref.array_sha(core)!=ORIGIN_CHART_SHA256\n",
    "replacement": "    if (ref.array_sha(mesh)!=ORIGIN_MESH_SHA256 or ref.array_sha(core)!=CURRENT_CHART_SHA256\n"
  },
  {
    "start": 619,
    "end": 620,
    "expected": "            or current_model.get('fixed_chart_core_sha256')!=ORIGIN_CHART_SHA256\n",
    "replacement": "            or current_model.get('fixed_chart_core_sha256')!=CURRENT_CHART_SHA256\n"
  },
  {
    "start": 621,
    "end": 622,
    "expected": "        raise ValueError('The actual whole mesh or complete fixed material chart differs from historical input')\n",
    "replacement": "        raise ValueError('The actual whole mesh or entire new fixed chart differs from this independent input')\n"
  },
  {
    "start": 630,
    "end": 631,
    "expected": "        whole_warm_or_height_equality_inferred=False)\n",
    "replacement": "        whole_warm_or_height_equality_inferred=False,\n        historical_chart_core_sha256=ORIGIN_CHART_SHA256,\n        same_original_fixed_chart=False,same_mathematical_g_claimed=False)\n"
  },
  {
    "start": 770,
    "end": 770,
    "expected": "",
    "replacement": "    target=fixed_target_definition(model=current_model,scalar_parameters=projected,\n        chart_words=[float(v).hex() for v in core],\n        node_definitions=[[str(a),str(b)] for a,b in definitions],\n        reference_bundle=current_identity['actual_reference_output'])\n    target_path=args.outdir/'independent-fixed-target-definition.json'\n    target_path.write_text(json.dumps(target,sort_keys=True,separators=(',',':'),allow_nan=False)+'\\n')\n    report['independent_fixed_target_definition_file']=record(target_path)\n    report['independent_fixed_target_definition_identity_sha256']=canonical(target)\n"
  },
  {
    "start": 771,
    "end": 771,
    "expected": "",
    "replacement": "        fixed_target_definition=target,fixed_target_definition_identity_sha256=canonical(target),\n"
  },
  {
    "start": 790,
    "end": 791,
    "expected": "        same_complete_scalar_formula_verified=True,same_complete_fixed_material_chart_verified=True,\n",
    "replacement": "        same_complete_scalar_formula_verified=True,complete_current_fixed_material_chart_verified=True,\n        same_original_fixed_chart=False,same_mathematical_g_claimed=False,\n        exact_old_to_new_chart_conjugacy_claimed=False,\n"
  },
  {
    "start": 795,
    "end": 796,
    "expected": "    validation = validate_current_input_compatibility(compatibility,actual_model=current_model,\n",
    "replacement": "    validation = validate_independent_fixed_target_binding(compatibility,actual_model=current_model,\n"
  },
  {
    "start": 799,
    "end": 801,
    "expected": "    report['current_input_compatibility'] = compatibility\n    report['current_input_compatibility_validation'] = validation\n",
    "replacement": "    report['independent_fixed_target_binding'] = compatibility\n    report['independent_fixed_target_binding_validation'] = validation\n"
  },
  {
    "start": 802,
    "end": 804,
    "expected": "        current_input_compatibility=compatibility,\n        current_input_compatibility_identity_sha256=canonical(compatibility),\n",
    "replacement": "        independent_fixed_target_binding=compatibility,\n        independent_fixed_target_binding_identity_sha256=canonical(compatibility),\n        fixed_target_definition=target,fixed_target_definition_identity_sha256=canonical(target),\n"
  },
  {
    "start": 807,
    "end": 808,
    "expected": "            reconstruction_scope='Restore old actual carrier from complete exact parameters and recorded deterministic leaf count; accept only full original SHA'),\n",
    "replacement": "            reconstruction_scope='Independent complete current fixed chart; reconstruct full historical carrier only for its complete material-address responsibility, accepting only original whole SHA'),\n"
  },
  {
    "start": 821,
    "end": 821,
    "expected": "",
    "replacement": "        explicit_independent_new_fixed_material_chart=True,\n        same_original_fixed_chart=False,same_mathematical_g_claimed=False,\n        original_branch_replaced_or_declared_finished=False,\n"
  }
]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def section(source,start,end):
    p=source.index(start)
    return source[p:source.index(end,p+len(start))]


def derive(raw):
    if sha(raw)!=PARENT_SHA256:
        raise ValueError('Use the complete unchanged 6cc parent')
    source=raw.decode();rows=source.splitlines(keepends=True)
    parts=[];cursor=0
    for patch in PATCHES:
        low,high=patch['start'],patch['end']
        if not cursor<=low<=high<=len(rows) or ''.join(rows[low:high])!=patch['expected']:
            raise ValueError('Exact whole-parent edit mismatch')
        parts.extend((''.join(rows[cursor:low]),patch['replacement']))
        cursor=high
    parts.append(''.join(rows[cursor:]))
    result=''.join(parts)
    if sha(result.encode())!=DERIVED_SHA256 or len(result.encode())!=DERIVED_BYTES:
        raise ValueError('The complete derived producer identity changed')
    for a,b in (
        ('def exact_node_definitions(','def counted_tail_class('),
        ('def counted_tail_class(','def compare_member('),
        ('def compare_member(','def execute(')):
        if section(source,a,b)!=section(result,a,b):
            raise ValueError('An original numerical kernel changed')
    start="    deep_module = modules['deep_scalar']"
    old_end="    compatibility = dict(schema=COMPATIBILITY_SCHEMA,producer_source_sha256=sha(__file__),"
    new_end="    target=fixed_target_definition(model=current_model"
    if section(source,start,old_end)!=section(result,start,new_end):
        raise ValueError('The entire original carrier calculation/SHA gate changed')
    tree=ast.parse(result)
    compile(tree,'freeze_run08_fixed_chart_and_restore_run05_carrier.py','exec')
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--parent',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--verify-existing',action='store_true')
    a=p.parse_args()
    source=derive(a.parent.read_bytes())
    if a.verify_existing:
        if a.out.read_bytes()!=source.encode():
            raise ValueError('Entire existing file differs from the derivation')
    else:
        if a.out.exists():
            raise FileExistsError('Keep previous source revisions intact')
        a.out.parent.mkdir(parents=True,exist_ok=True)
        a.out.write_bytes(source.encode())
    print(json.dumps(dict(parent_sha256=PARENT_SHA256,derived_sha256=DERIVED_SHA256,
        bytes=DERIVED_BYTES,AST_and_compile_completed=True,
        scientific_code_executed=False,original_carrier_mathematics_unchanged=True)))


if __name__=='__main__':
    main()
