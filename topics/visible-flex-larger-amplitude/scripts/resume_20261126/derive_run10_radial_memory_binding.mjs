// Complete literal source derivation only. This module does not import scientific Python.
import crypto from 'node:crypto';
const identity = text => ({bytes:Buffer.byteLength(text,'utf8'),sha256:crypto.createHash('sha256').update(text,'utf8').digest('hex')});
const same = (a,b) => a.bytes===b.bytes && a.sha256===b.sha256;
export const SPECS = [
 {
  "role": "radial_addresses",
  "parent": {
   "path": "scripts/resume_20261126/radial_material_address_transfer.py",
   "bytes": 22097,
   "sha256": "6c77349921ccfdfa765e720a330e584abba96d65c4566d9a4286df072428e716",
   "git_blob_sha": "674d073938d100b2d5a7a13380e465d0f0cb2943"
  },
  "output": {
   "name": "run10_radial_material_address_transfer.py",
   "bytes": 22097,
   "sha256": "e27e2f333e2a24279af84d6e015835420355b2fb446dbd56b99e99e68d40374b"
  },
  "patches": [
   {
    "old": "d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75",
    "new": "081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5",
    "count": 1
   },
   {
    "old": "public09",
    "new": "public10",
    "count": 1
   }
  ]
 },
 {
  "role": "independent_envelope_memory",
  "parent": {
   "path": "scripts/resume_20261126/radial_refined_public_reference_memory.py",
   "bytes": 59239,
   "sha256": "6d8184f921e93265284c1a5396b9349d3adefd9cfbd7531cf2f4a682b33ad33a",
   "git_blob_sha": "e4e48e2eff8cec3dfbbcf47b64ce2626ecf6c161"
  },
  "output": {
   "name": "run10_radial_refined_material_memory.py",
   "bytes": 59245,
   "sha256": "043d451e34890c522de17be687306898f2f18ec8451d1814ab75730eea687071"
  },
  "patches": [
   {
    "old": "d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75",
    "new": "081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5",
    "count": 1
   },
   {
    "old": "9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18",
    "new": "fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a",
    "count": 1
   },
   {
    "old": "306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a",
    "new": "9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209",
    "count": 2
   },
   {
    "old": "45943410994",
    "new": "45972294636",
    "count": 2
   },
   {
    "old": "20261127-09",
    "new": "20261127-10",
    "count": 1
   },
   {
    "old": "public09",
    "new": "public10",
    "count": 10
   },
   {
    "old": "run09",
    "new": "run10",
    "count": 8
   },
   {
    "old": "6c77349921ccfdfa765e720a330e584abba96d65c4566d9a4286df072428e716",
    "new": "e27e2f333e2a24279af84d6e015835420355b2fb446dbd56b99e99e68d40374b",
    "count": 1
   },
   {
    "old": "radial_material_address_transfer.py",
    "new": "run10_radial_material_address_transfer.py",
    "count": 1
   }
  ]
 },
 {
  "role": "analytic_J3_binding",
  "parent": {
   "path": "scripts/resume_20261126/radial_refined_public_reference_source_binding.py",
   "bytes": 47609,
   "sha256": "5b50b02aea139b81e7e1ed3cbf37c4ad8870d182c63d48bf648fb197e1cf3734",
   "git_blob_sha": "ce4a685002b4c11163ca01abd28591dd098698f3"
  },
  "output": {
   "name": "run10_radial_source_and_report_binding.py",
   "bytes": 48958,
   "sha256": "7536c4b1fb9085fe03a00be5da4073065b7abb98a3b2ee7b3d14833c478af415"
  },
  "patches": [
   {
    "old": "def _pure(path,expected,constants,functions):\n    path=Path(path).resolve()\n    raw=path.read_bytes()\n    if len(raw)>=100000 or hashlib.sha256(raw).hexdigest()!=expected:\n        raise ValueError('Bind the whole independently declared small source: '+path.name)\n    tree=ast.parse(raw)\n    body=[];seen_names=set();seen_functions=set()\n    for node in tree.body:\n        if (isinstance(node,ast.Assign) and len(node.targets)==1\n                and isinstance(node.targets[0],ast.Name) and node.targets[0].id in constants):\n            ast.literal_eval(node.value)\n            body.append(node);seen_names.add(node.targets[0].id)\n        if isinstance(node,ast.FunctionDef) and node.name in functions:\n            body.append(node);seen_functions.add(node.name)\n    if seen_names!=set(constants) or seen_functions!=set(functions):\n        raise ValueError('The full source-bound pure interface changed: '+path.name)\n    namespace=dict(Path=Path,hashlib=hashlib,json=json,math=math,__file__=str(path))\n    exec(compile(ast.Module(body=body,type_ignores=[]),'<complete bound pure analytic J3>','exec'),namespace)\n    if sha(path)!=expected:\n        raise ValueError('Source bytes changed during pure extraction')\n    return namespace\n\n",
    "new": "def _pure(path,expected,constants,functions):\n    path=Path(path).resolve()\n    raw=path.read_bytes()\n    if len(raw)>=100000 or hashlib.sha256(raw).hexdigest()!=expected:\n        raise ValueError('Bind the whole independently declared small source: '+path.name)\n    tree=ast.parse(raw)\n    body=[];seen_names=set();seen_functions=set()\n    for node in tree.body:\n        if (isinstance(node,ast.Assign) and len(node.targets)==1\n                and isinstance(node.targets[0],ast.Name) and node.targets[0].id in constants):\n            ast.literal_eval(node.value)\n            body.append(node);seen_names.add(node.targets[0].id)\n        if isinstance(node,ast.FunctionDef) and node.name in functions:\n            body.append(node);seen_functions.add(node.name)\n    if seen_names!=set(constants) or seen_functions!=set(functions):\n        raise ValueError('The full source-bound pure interface changed: '+path.name)\n    namespace=dict(Path=Path,hashlib=hashlib,json=json,math=math,ast=ast,textwrap=textwrap,__file__=str(path))\n    exec(compile(ast.Module(body=body,type_ignores=[]),'<complete bound pure analytic J3>','exec'),namespace)\n    if sha(path)!=expected:\n        raise ValueError('Source bytes changed during pure extraction')\n    return namespace\n\n",
    "count": 1
   },
   {
    "old": "def _policies(directory):\n    directory=Path(directory).resolve()\n    result={}\n    for role,key in POLICY_KEYS.items():\n        name,digest=SOURCE_BINDINGS[role]\n        functions={'sha','definition'}\n        if role in ('analytic_J3','analytic_frame'):\n            functions|={'canonical','_copy','_digest','_counts','validate_metadata'}\n        namespace=_pure(directory/name,digest,POLICY_CONSTANTS[role],functions)\n        result[key]=namespace['definition']()\n        if role in ('analytic_J3','analytic_frame'):\n            result['actual_validator' if role=='analytic_J3' else 'frame_actual_validator']=namespace['validate_metadata']\n    return result\n\n",
    "new": "def _policies(directory):\n    directory=Path(directory).resolve()\n    result={}\n    for role,key in POLICY_KEYS.items():\n        name,digest=SOURCE_BINDINGS[role]\n        functions={'sha','definition'}\n        if role in ('analytic_J3','analytic_frame','frame_C1'):\n            functions|={'canonical','_ast_value','complete_method_ast'}\n        if role in ('analytic_J3','analytic_frame','closure_values'):\n            functions|={'canonical','_copy','_digest','_counts','validate_metadata'}\n        namespace=_pure(directory/name,digest,POLICY_CONSTANTS[role],functions)\n        result[key]=namespace['definition']()\n        if role in ('analytic_J3','analytic_frame','closure_values'):\n            validator_key={'analytic_J3':'actual_validator',\n                'analytic_frame':'frame_actual_validator',\n                'closure_values':'closure_actual_validator'}[role]\n            result[validator_key]=namespace['validate_metadata']\n    return result\n",
    "count": 1
   },
   {
    "old": "def read_actual(report,*,roles,source_directory):\n    \"\"\"Validate every actual new snapshot and full metadata at its OWN point.\"\"\"\n    model=report['representation']\n    policies=validate_current_model(model,roles=roles,source_directory=source_directory)\n    expected=policies['analytic_stage_jacobian']\n    if (report.get('analytic_stage_jacobian_definition')!=expected\n            or report.get('analytic_stage_jacobian_source',{}).get('sha256')!=roles['analytic_J3']\n            or report.get('analytic_stage_J3_full_original_residual_and_chain_retained') is not True\n            or report.get('analytic_stage_J3_speedup_or_rounding_certified') is not False):\n        raise ValueError('Bind the complete declared analytic partial without inherited success or speed')\n    frame_expected=policies['analytic_normal_frame']\n    if (report.get('analytic_normal_frame_definition')!=frame_expected\n            or report.get('analytic_normal_frame_source',{}).get('sha256')!=roles['analytic_frame']\n            or report.get('analytic_normal_frame_full_six_columns_and_active_graph_retained') is not True\n            or report.get('analytic_normal_frame_speedup_or_rounding_certified') is not False):\n        raise ValueError('Bind the complete six-control derivative without borrowing a cost or certificate')\n    frame_validator=policies['frame_actual_validator']\n    validator=policies['actual_validator']\n    count=0\n    metadata_count=0\n    def visit(value):\n        nonlocal count,metadata_count\n        if isinstance(value,dict):\n            if value.get('schema')==ROOT_SNAPSHOT_SCHEMA:\n                if (value.get('operator_schema')!=OPERATOR_SCHEMA\n                        or value.get('operator_source_sha256')!=roles['endpoint']\n                        or value.get('model_identity_sha256')!=canonical(model)):\n                    raise ValueError('An analytic matrix snapshot belongs to another actual field')\n                validator(value.get('analytic_stage_jacobian'),model=model,source_by_role=roles,\n                    current_full_point_sha256=value.get('current_full_point_sha256'))\n                frame_validator(value.get('analytic_normal_frame'),model=model,source_by_role=roles,\n                    current_full_point_sha256=value.get('current_full_point_sha256'))\n                count+=1\n            elif value.get('schema')==OPERATOR_SCHEMA and 'model' in value:\n                if value['model']!=model or value.get('model_identity_sha256')!=canonical(model):\n                    raise ValueError('A full matrix metadata record belongs to another actual field')\n                validator(value.get('analytic_stage_jacobian'),model=model,source_by_role=roles,\n                    current_full_point_sha256=value.get('current_full_point_sha256'))\n                frame_validator(value.get('analytic_normal_frame'),model=model,source_by_role=roles,\n                    current_full_point_sha256=value.get('current_full_point_sha256'))\n                metadata_count+=1\n            for child in value.values():\n                visit(child)\n        elif isinstance(value,list):\n            for child in value:\n                visit(child)\n    visit(report)\n    latest=report.get('latest_operator_metadata')\n    actual=None\n    frame_actual=None\n    if latest:\n        if latest.get('schema')!=OPERATOR_SCHEMA or latest.get('model')!=model:\n            raise ValueError('Do not substitute another latest operator record')\n        actual=validator(latest.get('analytic_stage_jacobian'),model=model,source_by_role=roles,\n            current_full_point_sha256=latest.get('current_full_point_sha256'))\n        frame_actual=frame_validator(latest.get('analytic_normal_frame'),model=model,source_by_role=roles,\n            current_full_point_sha256=latest.get('current_full_point_sha256'))\n    elif report.get('complete') is True:\n        raise ValueError('A complete budget must retain its own actual local-matrix counters')\n    return dict(schema=SCHEMA,source_sha256=sha(__file__),\n        actual_analytic_source_sha256=roles['analytic_J3'],\n        actual_operator_source_sha256=roles['endpoint'],\n        actual_model_identity_sha256=canonical(model),\n        definition=expected,definition_identity_sha256=canonical(expected),\n        actual_bound_snapshot_count=count,actual_bound_full_metadata_count=metadata_count,\n        latest_actual_diagnostics=actual,\n        radial_refinement=radial_refinement_binding(report,roles=roles,source_directory=source_directory),\n        analytic_normal_frame=dict(source_sha256=roles['analytic_frame'],\n            actual_operator_source_sha256=roles['endpoint'],\n            actual_model_identity_sha256=canonical(model),definition=frame_expected,\n            definition_identity_sha256=canonical(frame_expected),\n            actual_bound_snapshot_count=count,actual_bound_full_metadata_count=metadata_count,\n            latest_actual_diagnostics=frame_actual,snapshot_values_backfilled_from_latest=False,\n            full_six_columns_and_all_upstream_J_retained=True,\n            current_scientific_values_recomputed=False),\n        snapshot_values_backfilled_from_latest=False,\n        original_full_stage_residual_domain_Armijo_and_all_upstream_J_retained=True,\n        local_J3_is_not_an_endpoint_root_or_geometry_certificate=True,\n        every_matrix_request_is_a_complete_three_by_three_batch=True,\n        source_or_binding_failures_silently_fallback=False,\n        current_scientific_values_recomputed=False)\n\n\n",
    "new": "def read_actual(report,*,roles,source_directory):\n    \"\"\"Validate every actual snapshot and full metadata at its OWN point.\"\"\"\n    model=report['representation']\n    policies=validate_current_model(model,roles=roles,source_directory=source_directory)\n    expected=policies['analytic_stage_jacobian']\n    if (report.get('analytic_stage_jacobian_definition')!=expected\n            or report.get('analytic_stage_jacobian_source',{}).get('sha256')!=roles['analytic_J3']\n            or report.get('analytic_stage_J3_full_original_residual_and_chain_retained') is not True\n            or report.get('analytic_stage_J3_speedup_or_rounding_certified') is not False):\n        raise ValueError('Bind the complete analytic partial without inherited success or speed')\n    frame_expected=policies['analytic_normal_frame']\n    if (report.get('analytic_normal_frame_definition')!=frame_expected\n            or report.get('analytic_normal_frame_source',{}).get('sha256')!=roles['analytic_frame']\n            or report.get('analytic_normal_frame_full_six_columns_and_active_graph_retained') is not True\n            or report.get('analytic_normal_frame_speedup_or_rounding_certified') is not False):\n        raise ValueError('Bind the full six-control derivative and actual upstream graph')\n    closure_expected=policies['detached_closure_value_reuse']\n    if (report.get('detached_closure_value_reuse_definition')!=closure_expected\n            or report.get('detached_closure_value_source',{}).get('sha256')!=roles['closure_values']\n            or report.get('closure_value_all_final_original_equation_checks_retained') is not True\n            or report.get('closure_value_active_J_and_transpose_use_original') is not True\n            or report.get('closure_value_speedup_rounding_or_root_certificate') is not False):\n        raise ValueError('A value cache cannot replace any stage, active derivative or original final check')\n    validators=(('analytic_stage_jacobian',policies['actual_validator']),\n        ('analytic_normal_frame',policies['frame_actual_validator']),\n        ('detached_closure_value_reuse',policies['closure_actual_validator']))\n    count=0\n    metadata_count=0\n    def validate_at_own_point(value):\n        for key,validator in validators:\n            validator(value.get(key),model=model,source_by_role=roles,\n                current_full_point_sha256=value.get('current_full_point_sha256'))\n    def visit(value):\n        nonlocal count,metadata_count\n        if isinstance(value,dict):\n            if value.get('schema')==ROOT_SNAPSHOT_SCHEMA:\n                if (value.get('operator_schema')!=OPERATOR_SCHEMA\n                        or value.get('operator_source_sha256')!=roles['endpoint']\n                        or value.get('model_identity_sha256')!=canonical(model)):\n                    raise ValueError('A complete snapshot belongs to another actual field')\n                validate_at_own_point(value);count+=1\n            elif value.get('schema')==OPERATOR_SCHEMA and 'model' in value:\n                if value['model']!=model or value.get('model_identity_sha256')!=canonical(model):\n                    raise ValueError('A full metadata record belongs to another actual field')\n                validate_at_own_point(value);metadata_count+=1\n            for child in value.values():visit(child)\n        elif isinstance(value,list):\n            for child in value:visit(child)\n    visit(report)\n    latest=report.get('latest_operator_metadata')\n    actuals={key:None for key,_ in validators}\n    if latest:\n        if latest.get('schema')!=OPERATOR_SCHEMA or latest.get('model')!=model:\n            raise ValueError('Do not substitute another latest operator record')\n        for key,validator in validators:\n            actuals[key]=validator(latest.get(key),model=model,source_by_role=roles,\n                current_full_point_sha256=latest.get('current_full_point_sha256'))\n    elif report.get('complete') is True:\n        raise ValueError('A complete budget must retain its actual full numerical-policy metadata')\n    def summary(role,key,definition):\n        return dict(source_sha256=roles[role],actual_operator_source_sha256=roles['endpoint'],\n            actual_model_identity_sha256=canonical(model),definition=definition,\n            definition_identity_sha256=canonical(definition),\n            actual_bound_snapshot_count=count,actual_bound_full_metadata_count=metadata_count,\n            latest_actual_diagnostics=actuals[key],snapshot_values_backfilled_from_latest=False,\n            current_scientific_values_recomputed=False)\n    frame=summary('analytic_frame','analytic_normal_frame',frame_expected)\n    frame['full_six_columns_and_all_upstream_J_retained']=True\n    closure=summary('closure_values','detached_closure_value_reuse',closure_expected)\n    closure.update(all_stage_and_chain_final_equations_reread_by_original_formula=True,\n        active_J_and_transpose_bypass_cache=True,\n        mutable_progress_file_not_consumed_as_immutable_evidence=True,\n        speedup_root_or_geometry_certificate_inferred=False)\n    return dict(schema=SCHEMA,source_sha256=sha(__file__),\n        actual_analytic_source_sha256=roles['analytic_J3'],\n        actual_operator_source_sha256=roles['endpoint'],\n        actual_model_identity_sha256=canonical(model),\n        definition=expected,definition_identity_sha256=canonical(expected),\n        actual_bound_snapshot_count=count,actual_bound_full_metadata_count=metadata_count,\n        latest_actual_diagnostics=actuals['analytic_stage_jacobian'],\n        analytic_normal_frame=frame,detached_closure_value_reuse=closure,\n        snapshot_values_backfilled_from_latest=False,\n        original_full_stage_residual_domain_Armijo_and_all_upstream_J_retained=True,\n        local_J3_is_not_an_endpoint_root_or_geometry_certificate=True,\n        every_matrix_request_is_a_complete_three_by_three_batch=True,\n        source_or_binding_failures_silently_fallback=False,current_scientific_values_recomputed=False)\n",
    "count": 1
   },
   {
    "old": "import sys\n",
    "new": "import sys\nimport textwrap\n",
    "count": 1
   },
   {
    "old": "POLICY_KEYS = {'analytic_J3': 'analytic_stage_jacobian', 'frame_C1': 'normal_frame_C1_reuse', 'stage_matrices': 'detached_stage_matrix_reuse', 'adjacent_matrices': 'adjacent_normal_frame_matrices', 'analytic_frame': 'analytic_normal_frame'}",
    "new": "POLICY_KEYS = {\"analytic_J3\": \"analytic_stage_jacobian\", \"frame_C1\": \"normal_frame_C1_reuse\", \"stage_matrices\": \"detached_stage_matrix_reuse\", \"adjacent_matrices\": \"adjacent_normal_frame_matrices\", \"analytic_frame\": \"analytic_normal_frame\", \"closure_values\": \"detached_closure_value_reuse\"}",
    "count": 1
   },
   {
    "old": "POLICY_CONSTANTS = {'analytic_J3': {'BASE_SOURCE_SHA256', 'COUNTER_KEYS', 'ENDPOINT_SCHEMA', 'METHOD_AST', 'OBSERVED_COUNTER_KEYS', 'PARENT_NORMAL_SOURCE_SHA256', 'SCHEMA'}, 'frame_C1': {'ANALYTIC_STAGE_SOURCE_SHA256', 'METHOD_AST', 'ORIGINAL_CENTERED_SOURCE', 'SCHEMA'}, 'stage_matrices': {'ANALYTIC_STAGE_SOURCE_SHA256', 'BASE_SOURCE_SHA256', 'FRAME_C1_SOURCE_SHA256', 'ORIGINAL_C1_OPERATOR_SOURCE_SHA256', 'PHASES', 'SCHEMA'}, 'adjacent_matrices': {'ANALYTIC_STAGE_SOURCE_SHA256', 'BASE_SOURCE_SHA256', 'FRAME_C1_SOURCE_SHA256', 'PARENT_OPERATOR_SOURCE_SHA256', 'SCHEMA', 'STAGE_MATRIX_SOURCE_SHA256'}, 'analytic_frame': {'BASE_SOURCE_SHA256', 'COUNTER_KEYS', 'ENDPOINT_SCHEMA', 'METHOD_AST', 'OBSERVED_COUNTER_KEYS', 'ORIGINAL_FRAME_AST_SHA256', 'PARENT_NORMAL_SOURCE_SHA256', 'SCHEMA'}}",
    "new": "POLICY_CONSTANTS = {\"analytic_J3\": {\"BASE_SOURCE_SHA256\", \"COUNTER_KEYS\", \"ENDPOINT_SCHEMA\", \"METHOD_AST\", \"OBSERVED_COUNTER_KEYS\", \"PARENT_NORMAL_SOURCE_SHA256\", \"SCHEMA\", \"METHOD_SOURCE_OVERRIDES\", \"CLOSURE_VALUE_SOURCE_SHA256\"}, \"frame_C1\": {\"ANALYTIC_STAGE_SOURCE_SHA256\", \"METHOD_AST\", \"ORIGINAL_CENTERED_SOURCE\", \"SCHEMA\", \"METHOD_SOURCE_OVERRIDES\", \"CLOSURE_VALUE_SOURCE_SHA256\"}, \"stage_matrices\": {\"ANALYTIC_STAGE_SOURCE_SHA256\", \"BASE_SOURCE_SHA256\", \"FRAME_C1_SOURCE_SHA256\", \"ORIGINAL_C1_OPERATOR_SOURCE_SHA256\", \"PHASES\", \"SCHEMA\"}, \"adjacent_matrices\": {\"ANALYTIC_STAGE_SOURCE_SHA256\", \"BASE_SOURCE_SHA256\", \"FRAME_C1_SOURCE_SHA256\", \"PARENT_OPERATOR_SOURCE_SHA256\", \"SCHEMA\", \"STAGE_MATRIX_SOURCE_SHA256\"}, \"analytic_frame\": {\"BASE_SOURCE_SHA256\", \"COUNTER_KEYS\", \"ENDPOINT_SCHEMA\", \"METHOD_AST\", \"OBSERVED_COUNTER_KEYS\", \"ORIGINAL_FRAME_AST_SHA256\", \"PARENT_NORMAL_SOURCE_SHA256\", \"SCHEMA\", \"METHOD_SOURCE_OVERRIDES\", \"CLOSURE_VALUE_SOURCE_SHA256\"}, \"closure_values\": {\"COUNTER_KEYS\", \"SCHEMA\", \"DEFINITION_SCHEMA\", \"ENDPOINT_SCHEMA\", \"NORMAL_PARENT_SHA256\", \"BASE_SOURCE_SHA256\", \"TORCH_VERSION\"}}",
    "count": 1
   },
   {
    "old": "SOURCE_BINDINGS = {\"analytic_J3\":[\"radial_refined_public_reference_stage_jacobian.py\",\"0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9\"],\"analytic_frame\":[\"radial_refined_public_reference_normal_frame.py\",\"8fb0f326356d8e94337d51bfba85068c5872453df8f08e6619f241dfe7f715ce\"],\"frame_C1\":[\"radial_refined_public_reference_frame_c1.py\",\"bd1f11970897ec217edad05fd4a89eac2e5a4279508f15eb36e3d50959a38d8e\"],\"stage_matrices\":[\"radial_refined_public_reference_stage_matrices.py\",\"fab35a0c45681b352c5087297c7c47e8156674bce5616680952d0abcc253d387\"],\"adjacent_matrices\":[\"radial_refined_public_reference_adjacent_matrices.py\",\"3a156cc80399c3f7c3f59ed8b01a24038e3dcdc1c7d6ac2144c140d526e656d4\"],\"reference_calibration\":[\"radial_refined_public_reference_calibration.py\",\"c4a0160f769c5d97a102785cd8fd64cc527f2e236946901bdf0bc0a58621a178\"],\"endpoint\":[\"so3_radial_refined_public_reference_normal_lift.py\",\"8591b957da548e28efb42d456f55879b5d75fa950a686aab600c2d3b00a887c5\"]}",
    "new": "SOURCE_BINDINGS = {\"analytic_J3\":[\"run10_radial_analytic_stage_jacobian.py\",\"7bbc3384dae0f791992835ceacdbc78ace50101ef9b5291b67d72ea2afd9425b\"],\"analytic_frame\":[\"run10_radial_analytic_normal_frame.py\",\"945b66100801058d311f215c9453efa35a9cbb3edf031dc1b10da0140f9567f2\"],\"frame_C1\":[\"run10_radial_normal_frame_c1.py\",\"976f638b104c0b95233c9238eec3440baf6b31910f1a943fea99f114f2ccdbe2\"],\"stage_matrices\":[\"run10_radial_detached_stage_matrices.py\",\"404ecb970b37b37fd00863c52564ac1ec784c902d7f5123cc5317d77976336c9\"],\"adjacent_matrices\":[\"run10_radial_adjacent_normal_matrices.py\",\"7477da02b225834cc1f0dae147d0bca53a3b40398ee04cdf0dfc7f0217483a37\"],\"reference_calibration\":[\"run10_radial_reference_calibration.py\",\"cb440bfe32830f5a479e466fec8439e9bde88bfbb4160e534f899f999bac573b\"],\"endpoint\":[\"so3_run10_radial_refined_closure_normal_lift.py\",\"ffbbddc9047b36cd308ed79df7ad4669185f61e71d85caef9a14f37b8292a40c\"],\"closure_values\":[\"run10_radial_detached_closure_values.py\",\"61368668228dc9a90b24c4e88a692c5759214add2b733fe10a882acb2ce8f6eb\"]}",
    "count": 1
   },
   {
    "old": "SCHEMA = 'complete-public09-radial-refined-analytic-frame-source-model-binding-v1'",
    "new": "SCHEMA = 'complete-run10-radial-refined-closure-values-source-model-binding-v1'",
    "count": 1
   },
   {
    "old": "OPERATOR_SCHEMA = 'complete-radial-refined-public-reference-analytic-frame-normal-plane-SO3-v1'",
    "new": "OPERATOR_SCHEMA = 'complete-run10-radial-refined-detached-closure-values-analytic-frame-normal-layer-v1'",
    "count": 1
   },
   {
    "old": "ROOT_SNAPSHOT_SCHEMA = 'actual-radial-refined-public-reference-analytic-frame-snapshot-v1'",
    "new": "ROOT_SNAPSHOT_SCHEMA = 'actual-run10-radial-refined-closure-values-normal-snapshot-v1'",
    "count": 1
   },
   {
    "old": "def _validate_original_parent_model(old,directory):\n    if (old.get('source_sha256')!='3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc'\n            or old.get('schema')!='complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'):\n        raise ValueError('Use the complete actual public09 M160/J923 analytic-frame model')\n    original=_bound_module(Path(directory)/'run09_public_reference_analytic_frame_binding.py',\n        '15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592')\n    roles={role:record[1] for role,record in original.SOURCE_BINDINGS.items()}\n    original.validate_current_model(old,roles=roles,source_directory=directory)\n    return tuple(original.POLICY_KEYS.values())\n\n",
    "new": "def _validate_original_parent_model(old,directory):\n    if (old.get('source_sha256')!='6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4'\n            or old.get('schema')!='complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1'):\n        raise ValueError('Use the complete actual run10 M160/J923 detached-closure model')\n    original=_bound_module(Path(directory)/'run10_detached_closure_value_binding.py',\n        'dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1')\n    roles={role:record[1] for role,record in original.SOURCE_BINDINGS.items()}\n    original.validate_current_model(old,roles=roles,source_directory=directory)\n    return tuple(original.POLICY_KEYS.values())\n\n",
    "count": 1
   },
   {
    "old": "def bind_actual_run09_input(path, *, current_files=None):\n    \"\"\"Read only the genuinely returned whole input binding and all six inputs.\n\n    The old/current carrier reconstruction is never rerun here. The complete\n    source-bound memory separately rechecks its public snapshots, full chart,\n    original P0 and actual carrier arrays before the first physical field.\n    \"\"\"\n    path=Path(path).resolve()\n    raw=path.read_bytes()\n    record=dict(path=str(path),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw))\n    if (record['sha256']!=ACTUAL_RUN09_BINDING_SHA256\n            or record['bytes']!=ACTUAL_RUN09_BINDING_BYTES):\n        raise ValueError('Use the whole actually returned run09 input binding, not a relabelled current file')\n    payload=json.loads(raw)\n    target=payload.get('fixed_target_definition',{})\n    evidence=target.get('complete_public_input_evidence',{})\n    if (payload.get('schema')!='material-envelope-actual-public-run09-fixed-target-binding-v1'\n            or payload.get('producer',{}).get('source_sha256')!=ACTUAL_RUN09_PRODUCER_SOURCE\n            or payload.get('fixed_target_definition_identity_sha256')!=ACTUAL_RUN09_TARGET_IDENTITY\n            or canonical(target)!=ACTUAL_RUN09_TARGET_IDENTITY\n            or target.get('schema')!='independently-frozen-actual-public-run09-scalar-and-material-chart-v1'\n            or target.get('definition_source_sha256')!=ACTUAL_RUN09_PRODUCER_SOURCE\n            or target.get('public_input_binding_source_sha256')!=ACTUAL_RUN09_PUBLIC_INPUT_SOURCE\n            or target.get('current_reference_model_identity_sha256')!=ACTUAL_RUN09_MODEL_IDENTITY\n            or canonical(target.get('complete_current_reference_model'))!=ACTUAL_RUN09_MODEL_IDENTITY\n            or target.get('fixed_chart_core_array_record',{}).get('sha256')!=ACTUAL_RUN09_CHART_IDENTITY\n            or target.get('same_original_fixed_chart') is not True\n            or target.get('same_mathematical_g_claimed') is not False\n            or evidence.get('actual_run_id')!='45943410994'\n            or evidence.get('actual_run_attempt')!='1'\n            or evidence.get('actual_reference_step_id')!='independent-axisymmetric-R690-reference-prepare-v2-first-20261127-09'\n            or canonical(evidence)!=target.get('complete_public_input_evidence_identity_sha256')):\n        raise ValueError('The complete returned run09 target/evidence/source identity changed')\n    files=evidence.get('current_files')\n    expected={'current_warm_bundle','current_node_report','current_scalar_input',\n        'current_carrier','current_preparation_report','current_reference_bundle'}\n    if not isinstance(files,dict) or set(files)!=expected:\n        raise ValueError('Every one of the six actual run09 input records is required')\n    supplied={} if current_files is None else current_files\n    if not isinstance(supplied,dict) or not set(supplied)<=expected:\n        raise ValueError('Only explicit original complete input roles can be matched')\n    for role,declared in files.items():\n        source=Path(declared['path']).resolve()\n        data=source.read_bytes()\n        actual=dict(path=str(source),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))\n        if actual!=declared or (role in supplied and Path(supplied[role]).resolve()!=source):\n            raise ValueError('The current entry input is not its whole actual run09 file: '+role)\n    if path.read_bytes()!=raw:\n        raise ValueError('The immutable actual input binding changed while being consumed')\n    return dict(schema='actual-run09-returned-input-entry-binding-v1',\n        source_sha256=sha(__file__),actual_binding_file=record,\n        actual_input_producer_source_sha256=ACTUAL_RUN09_PRODUCER_SOURCE,\n        actual_public_input_binding_source_sha256=ACTUAL_RUN09_PUBLIC_INPUT_SOURCE,\n        actual_run_id='45943410994',actual_run_attempt='1',\n        actual_reference_step_id=evidence['actual_reference_step_id'],\n        actual_reference_model_identity_sha256=ACTUAL_RUN09_MODEL_IDENTITY,\n        actual_fixed_target_definition_identity_sha256=ACTUAL_RUN09_TARGET_IDENTITY,\n        actual_fixed_chart_core_sha256=ACTUAL_RUN09_CHART_IDENTITY,\n        complete_current_input_files=copy.deepcopy(files),\n        all_six_current_whole_files_reread=True,\n        complete_memory_public_snapshot_and_array_validation_still_required=True,\n        same_original_fixed_chart=True,same_mathematical_g_claimed=False,\n        not_claimed_metric_relation_is_not_a_claim_of_mathematical_inequality=True,\n        physical_values_roots_or_certificates_inherited=False)\n",
    "new": "def bind_actual_run10_input(path, *, current_files=None):\n    \"\"\"Read only the genuinely returned whole input binding and all six inputs.\n\n    The old/current carrier reconstruction is never rerun here. The complete\n    source-bound memory separately rechecks its public snapshots, full chart,\n    original P0 and actual carrier arrays before the first physical field.\n    \"\"\"\n    path=Path(path).resolve()\n    raw=path.read_bytes()\n    record=dict(path=str(path),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw))\n    if (record['sha256']!=ACTUAL_RUN10_BINDING_SHA256\n            or record['bytes']!=ACTUAL_RUN10_BINDING_BYTES):\n        raise ValueError('Use the whole actually returned run10 input binding, not a relabelled current file')\n    payload=json.loads(raw)\n    target=payload.get('fixed_target_definition',{})\n    evidence=target.get('complete_public_input_evidence',{})\n    if (payload.get('schema')!='material-envelope-actual-public-run10-fixed-target-binding-v1'\n            or payload.get('producer',{}).get('source_sha256')!=ACTUAL_RUN10_PRODUCER_SOURCE\n            or payload.get('fixed_target_definition_identity_sha256')!=ACTUAL_RUN10_TARGET_IDENTITY\n            or canonical(target)!=ACTUAL_RUN10_TARGET_IDENTITY\n            or target.get('schema')!='independently-frozen-actual-public-run10-scalar-and-material-chart-v1'\n            or target.get('definition_source_sha256')!=ACTUAL_RUN10_PRODUCER_SOURCE\n            or target.get('public_input_binding_source_sha256')!=ACTUAL_RUN10_PUBLIC_INPUT_SOURCE\n            or target.get('current_reference_model_identity_sha256')!=ACTUAL_RUN10_MODEL_IDENTITY\n            or canonical(target.get('complete_current_reference_model'))!=ACTUAL_RUN10_MODEL_IDENTITY\n            or target.get('fixed_chart_core_array_record',{}).get('sha256')!=ACTUAL_RUN10_CHART_IDENTITY\n            or target.get('same_original_fixed_chart') is not True\n            or target.get('same_mathematical_g_claimed') is not False\n            or evidence.get('actual_run_id')!='45972294636'\n            or evidence.get('actual_run_attempt')!='1'\n            or evidence.get('actual_reference_step_id')!='independent-axisymmetric-R690-reference-prepare-v2-first-20261127-10'\n            or canonical(evidence)!=target.get('complete_public_input_evidence_identity_sha256')):\n        raise ValueError('The complete returned run10 target/evidence/source identity changed')\n    files=evidence.get('current_files')\n    expected={'current_warm_bundle','current_node_report','current_scalar_input',\n        'current_carrier','current_preparation_report','current_reference_bundle'}\n    if not isinstance(files,dict) or set(files)!=expected:\n        raise ValueError('Every one of the six actual run10 input records is required')\n    supplied={} if current_files is None else current_files\n    if not isinstance(supplied,dict) or not set(supplied)<=expected:\n        raise ValueError('Only explicit original complete input roles can be matched')\n    for role,declared in files.items():\n        source=Path(declared['path']).resolve()\n        data=source.read_bytes()\n        actual=dict(path=str(source),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))\n        if actual!=declared or (role in supplied and Path(supplied[role]).resolve()!=source):\n            raise ValueError('The current entry input is not its whole actual run10 file: '+role)\n    if path.read_bytes()!=raw:\n        raise ValueError('The immutable actual input binding changed while being consumed')\n    return dict(schema='actual-run10-returned-input-entry-binding-v1',\n        source_sha256=sha(__file__),actual_binding_file=record,\n        actual_input_producer_source_sha256=ACTUAL_RUN10_PRODUCER_SOURCE,\n        actual_public_input_binding_source_sha256=ACTUAL_RUN10_PUBLIC_INPUT_SOURCE,\n        actual_run_id='45972294636',actual_run_attempt='1',\n        actual_reference_step_id=evidence['actual_reference_step_id'],\n        actual_reference_model_identity_sha256=ACTUAL_RUN10_MODEL_IDENTITY,\n        actual_fixed_target_definition_identity_sha256=ACTUAL_RUN10_TARGET_IDENTITY,\n        actual_fixed_chart_core_sha256=ACTUAL_RUN10_CHART_IDENTITY,\n        complete_current_input_files=copy.deepcopy(files),\n        all_six_current_whole_files_reread=True,\n        complete_memory_public_snapshot_and_array_validation_still_required=True,\n        same_original_fixed_chart=True,same_mathematical_g_claimed=False,\n        not_claimed_metric_relation_is_not_a_claim_of_mathematical_inequality=True,\n        physical_values_roots_or_certificates_inherited=False)\n",
    "count": 1
   },
   {
    "old": "d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75",
    "new": "081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5",
    "count": 1
   },
   {
    "old": "9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18",
    "new": "fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a",
    "count": 1
   },
   {
    "old": "306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a",
    "new": "9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209",
    "count": 1
   },
   {
    "old": "public09",
    "new": "public10",
    "count": 4
   },
   {
    "old": "run09",
    "new": "run10",
    "count": 3
   },
   {
    "old": "RUN09",
    "new": "RUN10",
    "count": 10
   },
   {
    "old": "2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d",
    "new": "4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf",
    "count": 1
   },
   {
    "old": "430906",
    "new": "430908",
    "count": 1
   },
   {
    "old": "7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a",
    "new": "e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049",
    "count": 1
   },
   {
    "old": "        analytic_normal_frame=frame,detached_closure_value_reuse=closure,\n",
    "new": "        analytic_normal_frame=frame,detached_closure_value_reuse=closure,\n        radial_refinement=radial_refinement_binding(report,roles=roles,source_directory=source_directory),\n",
    "count": 1
   }
  ]
 }
];

export function build(read) {
  const output=new Map();
  for(const spec of SPECS) {
    const parent=read(spec.parent.path);
    if(typeof parent!=='string'||!same(identity(parent),spec.parent))throw new Error('Whole construction parent differs: '+spec.parent.path);
    let value=parent;
    for(const patch of spec.patches) {
      const count=value.split(patch.old).length-1;
      if(count!==patch.count)throw new Error('Exact patch count differs: '+spec.output.name+' '+count+' != '+patch.count);
      value=value.split(patch.old).join(patch.new);
    }
    if(!same(identity(value),spec.output))throw new Error('Whole derived source differs: '+spec.output.name);
    if(spec.output.bytes>=100000)throw new Error('Complete source exceeds the integration ceiling');
    output.set(spec.output.name,value);
  }
  return output;
}
