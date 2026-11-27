#!/usr/bin/env python3
"""Complete stdlib reconstruction of the run08 consumed-projection repair.

The parent is the entire published 8c1e source. This script performs no field,
root or integral calculation and imports no numerical library. The scientific
body remains in the complete derived file and is guarded by public Actions.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PARENT_SHA256 = '8c1e2d8f71bb08b33f99f9c187dbed2994776fc64b7114e1cea921a4fecff449'
DERIVED_SHA256 = '6cc95526e5305fa0265b96f66d322bbba612b8702d5ebcc5ec48a9fb29639d19'
DERIVED_BYTES = 53529
PATCHES = [
  {
    "start": 10,
    "end": 13,
    "expected": "This complete derivative binds current run08 evidence by actual run/attempt,\nwhole returned file identities and the same pinned preparation source; it\ndoes not inherit run07 current carrier/report words or change old mathematics.\n",
    "replacement": "This complete revision binds the real run08 warm/node/scalar/reference bytes,\nthen separately verifies the entire consumed mesh, fixed chart and scalar\nprojection against the original historical definition. Whole warm/H equality\nis neither required nor claimed. The old complete carrier and all 2397-leaf\narithmetic remain mandatory; this is not a substitute old-address packet.\n"
  },
  {
    "start": 17,
    "end": 17,
    "expected": "",
    "replacement": "import ast\nimport gzip\n"
  },
  {
    "start": 28,
    "end": 30,
    "expected": "SCHEMA = 'actual-run05-carrier-reconstruction-for-run08-by-recorded-leaf-count-v1'\nPARENT_COMPLETE_SOURCE_SHA256 = 'ef67425800ae9de626a7f8f48fd89deb125fbf0e4d6af72cf79741d1e254664e'\n",
    "replacement": "SCHEMA = 'actual-run05-carrier-reconstruction-from-current-consumed-projection-v2'\nPARENT_COMPLETE_SOURCE_SHA256 = '8c1e2d8f71bb08b33f99f9c187dbed2994776fc64b7114e1cea921a4fecff449'\n"
  },
  {
    "start": 107,
    "end": 108,
    "expected": "            or metrics.get('original_warm') != WARM_SHA\n",
    "replacement": "            or (historical and metrics.get('original_warm') != WARM_SHA)\n"
  },
  {
    "start": 112,
    "end": 112,
    "expected": "",
    "replacement": "    for key in ('original_warm','node','scalar_input','carrier','reference','model','fixed_profile'):\n        _digest(metrics.get(key),'public metric '+key)\n"
  },
  {
    "start": 190,
    "end": 191,
    "expected": "        current_reported_scalar_tolerance_reached=metrics['scalar_tolerance_reached'])\n",
    "replacement": "        current_reported_scalar_tolerance_reached=metrics['scalar_tolerance_reached'],\n        actual_current_warm_bundle_sha256=metrics['original_warm'])\n"
  },
  {
    "start": 194,
    "end": 194,
    "expected": "",
    "replacement": "\nCOMPATIBILITY_SCHEMA = 'actual-current-reference-projection-compatible-with-run05-v2'\nORIGIN_ENVELOPE_SOURCE_SHA256 = 'c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152'\nORIGIN_MESH_SHA256 = 'eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262'\nORIGIN_CHART_SHA256 = '90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e'\nWARM_RECIPE_SHA256 = '561308ca74186ac8eeb302dc786b633f2f643a1f98896d0685691d06eec556a4'\nWARM_CONTROLLER_SOURCE_SHA256 = '067b3f2e14145a6f88b2d171c555f1174f0505b45a5aaf670c3ec2610f7c286d'\nOLD_CARRIER_BYTES = 227202\nWARM_MEMBERS = ('mesh','qjets','a_stages','radius','Hcap','width','fixed_core_first3',\n                'circle_projection','a_stage_absolute_error','stage_time_absolute_error')\nCONSUMED_WARM_PROJECTION = ('mesh','width','radius','qjets[0,0,1:161]','fixed_core_first3')\nCURRENT_RECORD_KEYS = ('current_warm_bundle','current_node_report','current_scalar_input',\n                       'current_carrier','current_preparation_report','current_reference_bundle')\n\n\ndef _digest(value, name):\n    if (not isinstance(value,str) or len(value)!=64\n            or any(c not in '0123456789abcdef' for c in value)):\n        raise ValueError('A complete actual SHA256 is required: '+name)\n    return value\n\n\ndef _valid_record(value, name, *, reread=False):\n    if (not isinstance(value,dict) or set(value)!=set(('path','sha256','bytes'))\n            or not isinstance(value['path'],str) or not Path(value['path']).is_absolute()\n            or type(value['bytes']) is not int or value['bytes']<=0):\n        raise ValueError('Keep a complete actual file record: '+name)\n    _digest(value['sha256'],name)\n    if reread and record(value['path'])!=value:\n        raise ValueError('The bound complete file changed: '+name)\n    return value\n\n\ndef _bound_json(value, name):\n    _valid_record(value,name)\n    raw=Path(value['path']).read_bytes()\n    if len(raw)!=value['bytes'] or hashlib.sha256(raw).hexdigest()!=value['sha256']:\n        raise ValueError('The complete JSON snapshot changed: '+name)\n    return json.loads(raw)\n\n\ndef _public_blocks(value):\n    _valid_record(value,'public evidence')\n    raw=Path(value['path']).read_bytes()\n    if len(raw)!=value['bytes'] or hashlib.sha256(raw).hexdigest()!=value['sha256']:\n        raise ValueError('The full public volume changed during binding')\n    return [json.loads(block) for block in\n            re.findall(r'\\x60\\x60\\x60json\\s*\\n(.*?)\\n\\x60\\x60\\x60',raw.decode(),flags=re.S)]\n\n\ndef bind_actual_warm_return(args, current, identity):\n    \"\"\"Bind this run's entire real warm output, not the old warm digest.\"\"\"\n    blocks=_public_blocks(identity['actual_complete_public_volume'])\n    matches=[value for value in blocks if value.get('name')=='warm']\n    if len(matches)!=1:\n        raise ValueError('The actual complete current warm return must occur once')\n    value=matches[0]; metrics=value.get('metrics',{})\n    source={entry['role']:entry for entry in value.get('input_files',[])}\n    if (value.get('state')!='completed' or value.get('returncode')!=0\n            or value.get('source_sha256')!=WARM_CONTROLLER_SOURCE_SHA256\n            or source.get('recipe',{}).get('sha256')!=WARM_RECIPE_SHA256\n            or source.get('hold_warm',{}).get('sha256')!=WARM_SOURCE_SHA\n            or metrics.get('old_optimization_directions_started')!=0\n            or [metrics.get(k) for k in ('M','J','cells')]!=[160,923,922]\n            or metrics.get('hold_bundle_sha256')!=current['original_warm']\n            or metrics.get('hold_report_sha256')!=current['node']\n            or metrics.get('scalar_input_sha256')!=current['scalar_input']):\n        raise ValueError('The current warm/node/scalar must be its actual complete producer return')\n    outputs={Path(v['path']).name:v for v in value['outputs']}\n    root=Path(os.environ['RUNNER_TEMP'])/(\n        'visible-larger-research-'+identity['actual_run_id']+'-'+identity['actual_run_attempt'])/'research/fullclosed_solver/data'\n    actual={}\n    for key,argument,basename,metric in (\n            ('current_warm_bundle',args.warm_bundle,'fullclosed-hold-warm.npz','original_warm'),\n            ('current_node_report',args.node_report,'fullclosed-hold-warm.json','node'),\n            ('current_scalar_input',args.scalar_input,'pulse-a5-complete-base.json.gz','scalar_input')):\n        bound=record(argument);expected=(root/basename).resolve();output=outputs.get(basename)\n        if (Path(argument).resolve()!=expected or not isinstance(output,dict)\n                or Path(output['path']).resolve()!=expected\n                or bound['sha256']!=current[metric] or bound['sha256']!=output.get('sha256')\n                or bound['bytes']!=output.get('bytes')):\n            raise ValueError('Current source input differs from the real full warm output: '+key)\n        actual[key]=bound\n    return dict(actual_files=actual,actual_warm_recipe_sha256=WARM_RECIPE_SHA256,\n        actual_warm_producer_sha256=WARM_SOURCE_SHA,\n        actual_warm_source_commit=value['source_commit'],\n        actual_complete_public_volume=identity['actual_complete_public_volume'],\n        historical_warm_digest_requirement_applied_to_current=False,\n        old_warm_bundle_recreated_or_relabelled=False)\n\n\ndef verify_projection_origin(repo):\n    \"\"\"Read only the fixed origin constants from the entire original policy source.\"\"\"\n    path=Path(repo)/TOPIC/'scripts/resume_20261126/complete_material_envelope_memory.py'\n    if sha(path)!=ORIGIN_ENVELOPE_SOURCE_SHA256:\n        raise ValueError('The published whole original envelope input definition changed')\n    tree=ast.parse(path.read_text())\n    names={'ORIGIN_CARRIER_SHA','ORIGIN_CARRIER_BYTES','ORIGIN_WARM_SHA',\n           'ORIGIN_PARAMETERS_SHA','ORIGIN_MESH_SHA','ORIGIN_CHART_SHA'}\n    values={}\n    for statement in tree.body:\n        if isinstance(statement,ast.Assign):\n            for target in statement.targets:\n                if isinstance(target,ast.Name) and target.id in names:\n                    if target.id in values:\n                        raise ValueError('The original complete envelope has duplicate origin constants')\n                    values[target.id]=ast.literal_eval(statement.value)\n    expected=dict(ORIGIN_CARRIER_SHA=OLD_CARRIER_SHA,ORIGIN_CARRIER_BYTES=OLD_CARRIER_BYTES,\n        ORIGIN_WARM_SHA=WARM_SHA,ORIGIN_PARAMETERS_SHA=PARAMETERS_SHA,\n        ORIGIN_MESH_SHA=ORIGIN_MESH_SHA256,ORIGIN_CHART_SHA=ORIGIN_CHART_SHA256)\n    if values!=expected:\n        raise ValueError('Do not change the complete historical mesh/chart/carrier definition')\n    return record(path)\n\n\ndef validate_current_input_compatibility(value, *, actual_model, current_carrier,\n        current_preparation_report, current_reference_bundle, current_node_report,\n        current_scalar_input):\n    \"\"\"Pure stdlib, complete-file validation; no numerical field construction.\n\n    Consumer arguments are its actual file_record dictionaries. The producer's\n    full current warm, node, scalar, reference and preparation files are rehashed;\n    no true flag or matching shape substitutes for those recorded whole bytes.\n    \"\"\"\n    if (not isinstance(value,dict) or value.get('schema')!=COMPATIBILITY_SCHEMA\n            or value.get('producer_source_sha256')!=sha(__file__)\n            or value.get('origin_envelope_source_sha256')!=ORIGIN_ENVELOPE_SOURCE_SHA256\n            or value.get('historical_warm_bundle_sha256')!=WARM_SHA\n            or value.get('complete_scalar_parameters_sha256')!=PARAMETERS_SHA\n            or canonical(value.get('complete_scalar_parameters'))!=PARAMETERS_SHA\n            or value.get('current_mesh_sha256')!=ORIGIN_MESH_SHA256\n            or value.get('historical_mesh_sha256')!=ORIGIN_MESH_SHA256\n            or value.get('current_fixed_chart_core_sha256')!=ORIGIN_CHART_SHA256\n            or value.get('historical_fixed_chart_core_sha256')!=ORIGIN_CHART_SHA256\n            or value.get('exact_node_recipe_source_sha256')!=WARM_SOURCE_SHA\n            or value.get('consumed_warm_projection')!=list(CONSUMED_WARM_PROJECTION)\n            or value.get('literal_width_hex')!=float(.05).hex()):\n        raise ValueError('The current input projection is not the entire fixed historical mathematical input')\n    supplied=dict(current_carrier=current_carrier,current_preparation_report=current_preparation_report,\n        current_reference_bundle=current_reference_bundle,current_node_report=current_node_report,\n        current_scalar_input=current_scalar_input)\n    for key in CURRENT_RECORD_KEYS:\n        _valid_record(value.get(key),key,reread=True)\n        if key in supplied and value[key]!=supplied[key]:\n            raise ValueError('Consumer current file differs from the producer binding: '+key)\n    for key in ('historical_carrier','historical_public_return','current_public_return','origin_envelope_source'):\n        _valid_record(value.get(key),key,reread=True)\n    if (value['historical_carrier']['sha256']!=OLD_CARRIER_SHA\n            or value['historical_carrier']['bytes']!=OLD_CARRIER_BYTES\n            or value['historical_public_return']['sha256']!=OLD_RECORD_SHA\n            or value['origin_envelope_source']['sha256']!=ORIGIN_ENVELOPE_SOURCE_SHA256\n            or value.get('actual_current_model_identity_sha256')!=canonical(actual_model)\n            or actual_model.get('source_sha256')!=REFERENCE_SHA\n            or actual_model.get('M')!=160 or actual_model.get('J')!=923\n            or actual_model.get('original_warm_bundle_sha256')!=value['current_warm_bundle']['sha256']\n            or actual_model.get('symbolic_node_report_sha256')!=current_node_report['sha256']\n            or actual_model.get('scalar_input_sha256')!=current_scalar_input['sha256']\n            or actual_model.get('observation_carrier_sha256')!=current_carrier['sha256']\n            or actual_model.get('original_scalar_parameters_identity_sha256')!=PARAMETERS_SHA\n            or actual_model.get('mesh_sha256')!=ORIGIN_MESH_SHA256\n            or actual_model.get('fixed_chart_core_sha256')!=ORIGIN_CHART_SHA256\n            or actual_model.get('fixed_core_first3')!=value.get('fixed_core_first3_hex')\n            or actual_model.get('fixed_scalar_metric_identity_sha256')!=value.get('actual_current_fixed_scalar_identity_sha256')\n            or canonical(actual_model.get('fixed_scalar_profile_definition'))!=value.get('actual_current_fixed_scalar_identity_sha256')):\n        raise ValueError('Full current model/files and original scalar/domain/chart must agree')\n    preparation=_bound_json(current_preparation_report,'actual current preparation')\n    expected_solver=dict(reference_bundle=current_reference_bundle,carrier=current_carrier,\n        node_report=current_node_report,scalar_input=current_scalar_input)\n    if (preparation.get('schema')!='R690-independent-axisymmetric-SO3-preparation-v1'\n            or preparation.get('source_sha256')!=REFERENCE_SHA or preparation.get('complete') is not True\n            or preparation.get('reference_definition')!=actual_model\n            or preparation.get('reference_model_identity_sha256')!=canonical(actual_model)\n            or preparation.get('input_for_solver')!=expected_solver\n            or preparation.get('old_warm_bundle')!=value['current_warm_bundle']\n            or preparation.get('old_warm_node_report')!=current_node_report\n            or [preparation.get(k) for k in ('M','J','P','N')]!=[160,923,7377,2048]):\n        raise ValueError('Use the complete actual preparation, not independently assembled hashes')\n    node=_bound_json(current_node_report,'actual current exact-node report')\n    definitions=[[str(F(item['S_coefficient'])),str(F(item['constant']))]\n                 for item in node['true_scalar_nodes']]\n    if (node.get('source_sha256')!=WARM_SOURCE_SHA\n            or node.get('schema')!='fullclosed-hold-real-pulse-warm-v1'\n            or node.get('bundle_sha256')!=value['current_warm_bundle']['sha256']\n            or node.get('input_sha256')!=current_scalar_input['sha256']\n            or node.get('exact_core_affine') is not True\n            or node.get('M')!=160 or node.get('J')!=923 or len(definitions)!=923\n            or canonical(definitions)!=value.get('exact_symbolic_nodes_sha256')\n            or node.get('width_carrier')!=float(.05)\n            or node.get('width_exact')!=str(F(.05))):\n        raise ValueError('The full current symbolic mesh source differs from the verified original recipe')\n    for key in ('same_complete_scalar_formula_verified','same_complete_fixed_material_chart_verified',\n                'same_complete_symbolic_domain_verified','full_original_carrier_sha_verified',\n                'actual_current_warm_return_bound','all_original_carrier_members_reconstructed'):\n        if value.get(key) is not True:\n            raise ValueError('A complete reconstruction obligation is unpaid: '+key)\n    for key in ('historical_whole_warm_recreated','historical_whole_warm_or_height_equality_claimed',\n                'old_metric_or_geometry_values_inherited','current_files_relabelled_as_historical'):\n        if value.get(key) is not False:\n            raise ValueError('Current bytes or scientific conclusions were relabelled: '+key)\n    # Actual scalar-file bytes and all exact projected values are checked here,\n    # independently of the input model's recorded parameter digest.\n    raw=Path(current_scalar_input['path']).read_bytes()\n    if len(raw)!=current_scalar_input['bytes'] or hashlib.sha256(raw).hexdigest()!=current_scalar_input['sha256']:\n        raise ValueError('The current complete scalar snapshot changed')\n    scalar=json.loads(gzip.decompress(raw) if raw[:2]==b'\\x1f\\x8b' else raw)\n    parameters=dict(analytic_extension_origin=scalar['analytic_extension_origin'],\n        geometry=scalar['fixed_scalar_profile']['geometry'])\n    if parameters!=value['complete_scalar_parameters'] or canonical(parameters)!=PARAMETERS_SHA:\n        raise ValueError('The actual current scalar has a different complete mathematical projection')\n    # Public evidence is matched independently to the actual current files.\n    blocks=_public_blocks(value['current_public_return'])\n    prepares=[v for v in blocks if v.get('step_id')==CURRENT_STEP]\n    warms=[v for v in blocks if v.get('name')=='warm']\n    if len(prepares)!=1 or len(warms)!=1:\n        raise ValueError('The whole actual current warm and preparation returns are required')\n    step=prepares[0]; metrics=step.get('metrics',{}).get(OLD_METRIC_KEY,{})\n    warm=warms[0]; wm=warm.get('metrics',{})\n    outputs={Path(item['path']).name:item for item in step.get('outputs',[])}\n    for key,filename,metric in (('current_carrier','observations.npz','carrier'),\n            ('current_reference_bundle','reference.npz','reference'),\n            ('current_preparation_report','report.json',None)):\n        if outputs.get(filename)!=value[key] or (metric is not None and metrics.get(metric)!=value[key]['sha256']):\n            raise ValueError('Public actual preparation output differs from the whole current file: '+key)\n    if (step.get('state')!='completed' or step.get('returncode')!=0\n            or step.get('source_sha256')!=REFERENCE_SHA or metrics.get('complete') is not True\n            or metrics.get('model')!=canonical(actual_model)\n            or metrics.get('original_warm')!=value['current_warm_bundle']['sha256']\n            or metrics.get('node')!=current_node_report['sha256']\n            or metrics.get('scalar_input')!=current_scalar_input['sha256']\n            or metrics.get('scalar_parameters')!=PARAMETERS_SHA\n            or warm.get('state')!='completed' or warm.get('returncode')!=0\n            or warm.get('source_sha256')!=WARM_CONTROLLER_SOURCE_SHA256\n            or wm.get('hold_bundle_sha256')!=value['current_warm_bundle']['sha256']\n            or wm.get('hold_report_sha256')!=current_node_report['sha256']\n            or wm.get('scalar_input_sha256')!=current_scalar_input['sha256']):\n        raise ValueError('Current mathematical projection is not bound to its genuine complete public inputs')\n    return dict(schema=COMPATIBILITY_SCHEMA,producer_source_sha256=sha(__file__),\n        compatibility_identity_sha256=canonical(value),\n        actual_current_model_identity_sha256=canonical(actual_model),\n        actual_current_warm_bundle_sha256=value['current_warm_bundle']['sha256'],\n        historical_warm_bundle_sha256=WARM_SHA,\n        current_and_historical_whole_warm_equal=value['current_warm_bundle']['sha256']==WARM_SHA,\n        historical_whole_warm_or_height_equality_claimed=False,\n        complete_scalar_parameters_sha256=PARAMETERS_SHA,current_mesh_sha256=ORIGIN_MESH_SHA256,\n        current_fixed_chart_core_sha256=ORIGIN_CHART_SHA256,\n        exact_symbolic_nodes_sha256=value['exact_symbolic_nodes_sha256'],\n        historical_carrier_sha256=OLD_CARRIER_SHA,historical_carrier_bytes=OLD_CARRIER_BYTES,\n        whole_old_carrier_and_full_current_input_bytes_rechecked=True,\n        same_complete_scalar_formula_and_fixed_chart=True,\n        scientific_certificates_inherited=False)\n\n\n"
  },
  {
    "start": 307,
    "end": 307,
    "expected": "",
    "replacement": "    warm_return = bind_actual_warm_return(args,current,current_identity)\n    report['actual_current_warm_public_binding'] = warm_return\n    origin_source = verify_projection_origin(repo)\n"
  },
  {
    "start": 310,
    "end": 311,
    "expected": "            (args.warm_bundle,WARM_SHA),\n",
    "replacement": "            (args.warm_bundle,current['original_warm']),\n"
  },
  {
    "start": 325,
    "end": 326,
    "expected": "            or current_model.get('original_warm_bundle_sha256') != WARM_SHA\n",
    "replacement": "            or current_model.get('original_warm_bundle_sha256') != current['original_warm']\n"
  },
  {
    "start": 334,
    "end": 335,
    "expected": "            or node.get('bundle_sha256') != WARM_SHA\n",
    "replacement": "            or node.get('bundle_sha256') != current['original_warm']\n"
  },
  {
    "start": 341,
    "end": 341,
    "expected": "",
    "replacement": "    if set(warm)!=set(WARM_MEMBERS):\n        raise ValueError('Keep all ten actual original warm-producer members')\n"
  },
  {
    "start": 346,
    "end": 348,
    "expected": "    if not np.array_equal(core[:3],warm['fixed_core_first3']):\n        raise ValueError('Original first-three core words changed')\n",
    "replacement": "    if (str(mesh.dtype)!='float64' or str(core.dtype)!='float64'\n            or str(warm['qjets'].dtype)!='float64'\n            or str(warm['fixed_core_first3'].dtype)!='float64'\n            or warm['fixed_core_first3'].shape!=(3,)\n            or core.shape!=(160,) or not np.isfinite(core).all()\n            or not np.array_equal(core[:3],warm['fixed_core_first3'])):\n        raise ValueError('Keep the complete real fixed-core projection and original first three words')\n    if (ref.array_sha(mesh)!=ORIGIN_MESH_SHA256 or ref.array_sha(core)!=ORIGIN_CHART_SHA256\n            or current_model.get('mesh_sha256')!=ORIGIN_MESH_SHA256\n            or current_model.get('fixed_chart_core_sha256')!=ORIGIN_CHART_SHA256\n            or current_model.get('fixed_core_first3')!=[float(v).hex() for v in core[:3]]):\n        raise ValueError('The actual whole mesh or complete fixed material chart differs from historical input')\n    report['actual_warm_member_records'] = {key:array_record(ref,warm[key]) for key in WARM_MEMBERS}\n    report['current_consumed_projection'] = dict(\n        mesh_sha256=ref.array_sha(mesh),fixed_chart_core_sha256=ref.array_sha(core),\n        fixed_core_first3_hex=[float(v).hex() for v in core[:3]],\n        consumed_projection=list(CONSUMED_WARM_PROJECTION),\n        current_complete_warm_sha256=current['original_warm'],\n        historical_complete_warm_sha256=WARM_SHA,\n        current_and_historical_whole_warm_equal=current['original_warm']==WARM_SHA,\n        whole_warm_or_height_equality_inferred=False)\n"
  },
  {
    "start": 354,
    "end": 355,
    "expected": "        raise ValueError('The unchanged complete warm does not fit the exact scalar')\n",
    "replacement": "        raise ValueError('The actual consumed warm endpoints do not fit the exact scalar')\n    if any(warm[key].shape!=() or str(warm[key].dtype)!='float64'\n            or not np.isfinite(warm[key]).all() for key in ('width','radius','Hcap')):\n        raise ValueError('Keep the genuine scalar carrier words in the complete warm input')\n"
  },
  {
    "start": 391,
    "end": 392,
    "expected": "        common_full_warm_bundle_sha256=WARM_SHA,\n",
    "replacement": "        historical_full_warm_bundle_sha256=WARM_SHA,\n        current_actual_full_warm_bundle_sha256=current['original_warm'],\n        whole_warm_or_height_equality_claimed=False,\n        actual_current_projection=report['current_consumed_projection'],\n        original_envelope_input_source=origin_source,\n"
  },
  {
    "start": 480,
    "end": 480,
    "expected": "",
    "replacement": "    compatibility = dict(schema=COMPATIBILITY_SCHEMA,producer_source_sha256=sha(__file__),\n        origin_envelope_source_sha256=ORIGIN_ENVELOPE_SOURCE_SHA256,\n        origin_envelope_source=origin_source,\n        current_warm_bundle=record(args.warm_bundle),\n        current_node_report=record(args.node_report),current_scalar_input=record(args.scalar_input),\n        current_carrier=record(args.current_carrier),current_preparation_report=record(args.current_reference_report),\n        current_reference_bundle=current_identity['actual_reference_output'],\n        historical_carrier=actual,historical_public_return=record(args.historical_public_record),\n        current_public_return=current_identity['actual_complete_public_volume'],\n        historical_warm_bundle_sha256=WARM_SHA,\n        actual_current_model_identity_sha256=canonical(current_model),\n        actual_current_fixed_scalar_identity_sha256=current_model['fixed_scalar_metric_identity_sha256'],\n        complete_scalar_parameters=projected,complete_scalar_parameters_sha256=canonical(projected),\n        historical_mesh_sha256=ORIGIN_MESH_SHA256,current_mesh_sha256=ref.array_sha(mesh),\n        historical_fixed_chart_core_sha256=ORIGIN_CHART_SHA256,\n        current_fixed_chart_core_sha256=ref.array_sha(core),\n        fixed_core_first3_hex=[float(v).hex() for v in core[:3]],\n        exact_symbolic_nodes_sha256=canonical([[str(a),str(b)] for a,b in definitions]),\n        exact_node_recipe_source_sha256=WARM_SOURCE_SHA,literal_width_hex=width.hex(),\n        consumed_warm_projection=list(CONSUMED_WARM_PROJECTION),\n        same_complete_scalar_formula_verified=True,same_complete_fixed_material_chart_verified=True,\n        same_complete_symbolic_domain_verified=True,full_original_carrier_sha_verified=True,\n        actual_current_warm_return_bound=True,all_original_carrier_members_reconstructed=True,\n        historical_whole_warm_recreated=False,historical_whole_warm_or_height_equality_claimed=False,\n        old_metric_or_geometry_values_inherited=False,current_files_relabelled_as_historical=False)\n    validation = validate_current_input_compatibility(compatibility,actual_model=current_model,\n        current_carrier=record(args.current_carrier),current_preparation_report=record(args.current_reference_report),\n        current_reference_bundle=current_identity['actual_reference_output'],\n        current_node_report=record(args.node_report),current_scalar_input=record(args.scalar_input))\n    report['current_input_compatibility'] = compatibility\n    report['current_input_compatibility_validation'] = validation\n"
  },
  {
    "start": 481,
    "end": 481,
    "expected": "",
    "replacement": "        current_input_compatibility=compatibility,\n        current_input_compatibility_identity_sha256=canonical(compatibility),\n"
  }
]


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def section(source, start, end):
    first=source.index(start)
    return source[first:source.index(end,first+len(start))]


def derive(source):
    if digest(source.encode())!=PARENT_SHA256:
        raise ValueError('The complete published parent source changed')
    rows=source.splitlines(keepends=True)
    result=[];cursor=0
    for patch in PATCHES:
        low,high=patch['start'],patch['end']
        if not cursor<=low<=high<=len(rows) or ''.join(rows[low:high])!=patch['expected']:
            raise ValueError('The exact complete parent patch does not match')
        result.extend((''.join(rows[cursor:low]),patch['replacement']))
        cursor=high
    result.append(''.join(rows[cursor:]))
    output=''.join(result)
    raw=output.encode()
    if len(raw)!=DERIVED_BYTES or digest(raw)!=DERIVED_SHA256:
        raise ValueError('The complete derived file has the wrong identity')
    for first,last in (
            ('def exact_node_definitions(','def counted_tail_class('),
            ('def counted_tail_class(','def compare_member('),
            ('def compare_member(','def execute(')):
        if section(source,first,last)!=section(output,first,last):
            raise ValueError('A complete original numerical kernel changed')
    first="    deep_module = modules['deep_scalar']"
    old_end="    report['material_envelope_binding'] = dict(schema=BINDING_SCHEMA,"
    new_end="    compatibility = dict(schema=COMPATIBILITY_SCHEMA,producer_source_sha256=sha(__file__),"
    if section(source,first,old_end)!=section(output,first,new_end):
        raise ValueError('The full leaf/radius/plan/observation/save/SHA/math body changed')
    tree=ast.parse(output)
    compile(tree,'restore_actual_run05_carrier_for_compatible_current_run08.py','exec')
    return output


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parent',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--verify-existing',action='store_true')
    args=parser.parse_args()
    parent=args.parent.read_bytes()
    if digest(parent)!=PARENT_SHA256:
        raise ValueError('Use the complete actual 8c1e parent bytes')
    output=derive(parent.decode())
    if args.verify_existing:
        if args.out.read_bytes()!=output.encode():
            raise ValueError('The entire existing output does not match the derivation')
    else:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        if args.out.exists():
            raise FileExistsError('Do not overwrite an existing source revision')
        args.out.write_bytes(output.encode())
    print(json.dumps(dict(parent_sha256=PARENT_SHA256,derived_sha256=DERIVED_SHA256,
        derived_bytes=DERIVED_BYTES,complete_source_derived=True,
        AST_and_compile_completed=True,scientific_code_executed=False)))


if __name__=='__main__':
    main()
