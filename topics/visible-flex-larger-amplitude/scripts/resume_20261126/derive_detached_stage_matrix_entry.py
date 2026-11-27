#!/usr/bin/env python3
"""Pure full-source derivation of the independent detached stage-matrix entry.

Only stdlib source parsing/construction is performed.  No numerical module
is imported, and no field, integral, matrix, root or scientific fixture runs.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import pprint


PARENTS = {
    'operator': ('so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py',
        'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'),
    'calibration': ('reference_centred_c1_smooth_triangle_calibration.py',
        '3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991'),
    'geometry': ('so3_reference_centred_c1_material_envelope_geometry.py',
        'bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f'),
    'driver': ('fullclosed_reference_centred_c1_material_envelope_so3_qp.py',
        'cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5'),
    'launcher': ('launch_reference_centred_c1_material_envelope_so3_actions.py',
        'b93af9809adaf42a3eee9328c6ca857156c38609f40db975a92c3bea5f5af991'),
    'reader': ('read_reference_centred_c1_material_envelope_so3_report.py',
        '104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7'),
}
FRAME_SOURCE_SHA = 'ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9'
STAGE_SOURCE_SHA = '375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59'
TRANSFER_SOURCE_SHA = 'd5e74a6ee160e7ee5a70f53fb96b497e2ff1eacef070757f32ccf8d9226da3eb'
EXPECTED = {'detached_normal_stage_matrix_reuse.py': '375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59',
 'fullclosed_reference_centred_stage_cached_material_envelope_so3_qp.py': '1d1530c3a613d5b0721470139bce338ba950eaf561f51f921b562fb774cbedb2',
 'launch_reference_centred_stage_cached_material_envelope_so3_actions.py': '0625733b252205e20e98c53b372bfaf27fdae5cd421c6b38551a9d538d1025e5',
 'read_reference_centred_stage_cached_material_envelope_so3_report.py': '954721008b83c8550b4e0016cf0ec5351e46572dcccccca96f20b180f3cb5f0b',
 'reference_centred_stage_cached_smooth_triangle_calibration.py': '803ff897445b390ec2ba96ed84a0c7598d49ff9756e38077556074d025cce15d',
 'so3_reference_centred_stage_cached_material_envelope_geometry.py': 'bdf212da59c48dfdee86160178e4b8f91177796f4a62fca7f4a1ce9510b9a9f5',
 'so3_reference_centred_stage_cached_smooth_triangle_normal_lift_operator.py': 'd461f660063bfa2aeecc724050d71c6ef98143b9129f7cfe34f22e4043488a7f',
 'transfer_material_envelope_memory.py': 'd5e74a6ee160e7ee5a70f53fb96b497e2ff1eacef070757f32ccf8d9226da3eb'}
NAMES = {
    'helper': 'detached_normal_stage_matrix_reuse.py',
    'transfer': 'transfer_material_envelope_memory.py',
    'calibration': 'reference_centred_stage_cached_smooth_triangle_calibration.py',
    'operator': 'so3_reference_centred_stage_cached_smooth_triangle_normal_lift_operator.py',
    'geometry': 'so3_reference_centred_stage_cached_material_envelope_geometry.py',
    'driver': 'fullclosed_reference_centred_stage_cached_material_envelope_so3_qp.py',
    'launcher': 'launch_reference_centred_stage_cached_material_envelope_so3_actions.py',
    'reader': 'read_reference_centred_stage_cached_material_envelope_so3_report.py',
}
SCHEMAS = {
    'operator': 'complete-R711-reference-centred-C1-stage-matrix-reuse-SO3-fixed-normal-plane-six-control-layer-v1',
    'geometry': 'complete-R715-stage-matrix-reuse-material-envelope-world-geometry-and-preserved-prefix-rows-v1',
    'driver': 'complete-R711-reference-centred-stage-matrix-reuse-material-envelope-fixed-normal-plane-SO3-QP-v1',
    'readout': 'actual-complete-R711-reference-centred-stage-matrix-reuse-material-envelope-normal-plane-SO3-scalar-readout-v1',
}


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def checked(path, expected):
    data = Path(path).read_bytes()
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError('The complete input source bytes differ: '+str(path))
    return data.decode()


def replace(text, old, new, count=1):
    if text.count(old) != count:
        raise ValueError('Counted full-source change differs: '+old[:120])
    return text.replace(old,new)


def literal(text, name):
    nodes = [node for node in ast.parse(text).body if isinstance(node,ast.Assign)
        and any(isinstance(target,ast.Name) and target.id == name for target in node.targets)]
    if len(nodes) != 1:
        raise ValueError('Exactly one literal assignment required: '+name)
    return ast.literal_eval(nodes[0].value)


def assign(text, name, value):
    nodes = [node for node in ast.parse(text).body if isinstance(node,ast.Assign)
        and any(isinstance(target,ast.Name) and target.id == name for target in node.targets)]
    if len(nodes) != 1:
        raise ValueError('Exactly one assignment required: '+name)
    node = nodes[0]
    lines = text.splitlines(keepends=True)
    lines[node.lineno-1:node.end_lineno] = [name+' = '+pprint.pformat(value,sort_dicts=False,width=110)+'\n']
    return ''.join(lines)


def methods(text, class_name):
    nodes = [node for node in ast.parse(text).body
        if isinstance(node,ast.ClassDef) and node.name == class_name]
    if len(nodes) != 1:
        raise ValueError('Exactly one complete class required: '+class_name)
    return {node.name:ast.dump(node,include_attributes=False) for node in nodes[0].body
        if isinstance(node,ast.FunctionDef)}


def functions(text):
    return {node.name:ast.dump(node,include_attributes=False) for node in ast.parse(text).body
        if isinstance(node,ast.FunctionDef)}


def assert_methods(parent, current, class_name, changed):
    old,new = methods(parent,class_name),methods(current,class_name)
    if set(old) != set(new) or {name for name in old if old[name] != new[name]} != set(changed):
        raise ValueError('The actual complete method difference set changed: '+class_name)
    return len(old)-len(changed)


def assert_functions(parent, current, changed, added=()):
    old,new = functions(parent),functions(current)
    if set(new)-set(old) != set(added) or set(old)-set(new):
        raise ValueError('The complete top-level function set changed')
    if {name for name in old if old[name] != new[name]} != set(changed):
        raise ValueError('The complete top-level function difference set changed')
    return len(old)-len(changed)


def add_explicit_final_seed_arguments(text):
    text = replace(text,"    p.add_argument('--material-envelope-parent-report', type=Path, action='append', default=[])\n",
        "    p.add_argument('--material-envelope-parent-report', type=Path, action='append', default=[])\n"
        "    p.add_argument('--material-envelope-seed-checkpoint', type=Path)\n"
        "    p.add_argument('--material-envelope-seed-report', type=Path)\n")
    return replace(text,'    a.material_envelope_parent_report = [path.resolve() for path in a.material_envelope_parent_report]\n',
        '    a.material_envelope_parent_report = [path.resolve() for path in a.material_envelope_parent_report]\n'
        '    if bool(a.material_envelope_seed_checkpoint) != bool(a.material_envelope_seed_report):\n'
        "        raise ValueError('An explicit old complete final variable seed requires both actual files')\n"
        '    if a.material_envelope_seed_checkpoint is not None:\n'
        '        a.material_envelope_seed_checkpoint = a.material_envelope_seed_checkpoint.resolve()\n'
        '        a.material_envelope_seed_report = a.material_envelope_seed_report.resolve()\n'
        '        if (a.restart_checkpoint is not None or a.seed_so3_checkpoint is not None\n'
        '                or a.material_envelope_seed_report not in a.material_envelope_parent_report):\n'
        "            raise ValueError('The explicit final belongs to a fully transferred prior envelope and cannot be mixed with another seed/restart')\n")


def output_check(text, name):
    if len(text.encode()) >= 100000:
        raise ValueError('Keep the complete small-source file below 100KB: '+name)
    tree = ast.parse(text,filename=name)
    compile(tree,name,'exec')
    for node in ast.walk(tree):
        if isinstance(node,ast.Dict):
            keys = [key.value for key in node.keys if isinstance(key,ast.Constant)
                and isinstance(key.value,(str,int,float,bool,bytes,type(None)))]
            if len(keys) != len(set(keys)):
                raise ValueError('Duplicate literal dictionary key: '+name)
        if isinstance(node,ast.Call):
            keys = [key.arg for key in node.keywords if key.arg is not None]
            if len(keys) != len(set(keys)):
                raise ValueError('Duplicate literal keyword: '+name)
    if not text.endswith('\n') or any(line.rstrip() != line for line in text.splitlines()):
        raise ValueError('Keep exact final newline and no trailing whitespace: '+name)


OPERATOR_GUARD = '''        if (stage_matrix_module is None
                or sha(stage_matrix_module.__file__) != STAGE_MATRIX_SOURCE_SHA256
                or sha(stage_matrix_module.definition.__code__.co_filename) != STAGE_MATRIX_SOURCE_SHA256
                or sha(stage_matrix_module.CompleteDetachedStageMatrices.__init__.__code__.co_filename)
                    != STAGE_MATRIX_SOURCE_SHA256):
            raise ValueError('Bind the complete independent detached stage-matrix helper')
'''

GEOMETRY_GUARD = '''        matrices = problem.stage_matrices
        matrix_policy = model.get('detached_stage_matrix_reuse')
        if (not isinstance(matrix_policy,dict) or matrix_policy != matrices.definition
                or matrix_policy.get('source_sha256') != STAGE_MATRIX_SOURCE_SHA256
                or sha(matrices.__init__.__func__.__code__.co_filename) != STAGE_MATRIX_SOURCE_SHA256
                or matrices.q is not problem or matrices.model_identity_sha256 != problem.identity
                or matrices.actual_operator_source_sha256 != ENDPOINT_SOURCE_SHA256
                or matrices.actual_calibration_source_sha256 != REFERENCE_CENTERING_SOURCE_SHA256
                or matrix_policy.get('original_Newton_matrix_evaluations_unchanged') is not True
                or matrix_policy.get('original_stage_equations_domain_solves_and_trace_retained') is not True
                or matrix_policy.get('original_active_residual_and_full_upstream_parameter_chain_retained') is not True
                or matrix_policy.get('matrices_shared_between_calls_or_points_or_batches') is not False
                or matrix_policy.get('active_input_graphs_accepted') is not False):
            raise ValueError('Detached matrix reuse cannot replace original stages or the complete active field chain')
'''

READER_ADDITION = '''
def read_detached_matrix_policy(path):
    """Read the whole pinned helper's explicitly selected pure stdlib interface."""
    tree = ast.parse(Path(path).read_text())
    names = {'SCHEMA','FRAME_C1_SOURCE_SHA256','ORIGINAL_C1_OPERATOR_SOURCE_SHA256',
        'BASE_SOURCE_SHA256','PHASES','NORMAL_COUNTER_KEYS'}
    wanted = {'sha','canonical','definition','_new_counts','_plain_copy','_valid_digest',
        '_finite_nonnegative','_validated_counts','validate_metadata'}
    body,seen_names,seen_functions = [],set(),set()
    for node in tree.body:
        if isinstance(node,ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0],ast.Name):
            name = node.targets[0].id
            if name in names:
                ast.literal_eval(node.value)
                body.append(node)
                seen_names.add(name)
        if isinstance(node,ast.FunctionDef) and node.name in wanted:
            body.append(node)
            seen_functions.add(node.name)
    if seen_names != names or seen_functions != wanted:
        raise ValueError('Keep the complete source-bound detached-matrix pure policy and validator')
    namespace = dict(Path=Path,hashlib=hashlib,json=json,math=math,__file__=str(path))
    exec(compile(ast.Module(body=body,type_ignores=[]),'<bound pure detached-matrix metadata>','exec'),namespace)
    return namespace['definition'](),namespace['validate_metadata']


def detached_matrix_binding(report,model,roles,path):
    if sha(path) != roles['stage_matrices']:
        raise ValueError('Bind the entire independently published detached-matrix helper')
    expected,validator = read_detached_matrix_policy(path)
    if (model.get('detached_stage_matrix_reuse') != expected
            or report.get('detached_stage_matrix_reuse_definition') != expected
            or report.get('detached_stage_matrix_source',{}).get('sha256') != roles['stage_matrices']
            or report.get('all_original_Newton_stage_equations_and_full_implicit_chain_retained') is not True
            or report.get('stage_matrix_cache_acceleration_or_rounding_certified') is not False):
        raise ValueError('Numerical matrix reuse must preserve the complete original stage and field contract')
    binding = dict(definition=expected,definition_identity_sha256=canonical(expected),
        source_sha256=roles['stage_matrices'],all_original_free_variables_and_stages_retained=True,
        original_Newton_matrices_unchanged=True,prior_uncached_run_required=False,
        numerical_matrix_origin_is_distinct_from_current_stage_root=True,
        acceleration_or_error_certificate=False)
    def read_metadata(value):
        if value is None or value == {}:
            return None
        if not isinstance(value,dict):
            raise ValueError('Keep the actual complete operator metadata or absence')
        return validator(value.get('detached_stage_matrix_reuse'),model=model,
            source_by_role=roles,current_full_point_sha256=value.get('current_full_point_sha256'))
    return binding,read_metadata


def transferred_envelope_binding(topic,report,model,roles,driver):
    relative,expected = load_pins(driver)['envelope_transfer']
    path = topic/relative
    if (sha(path) != expected or roles['envelope_transfer'] != expected
            or report.get('material_envelope_transfer_source',{}).get('sha256') != expected):
        raise ValueError('Keep the complete independent address/type transfer source')
    name = '_actual_complete_envelope_transfer_'+expected
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    for function in (module.definition,module.validate_metadata,module.validate_seed_metadata):
        if sha(function.__code__.co_filename) != expected:
            raise ValueError('Use the complete source-bound pure transfer policy and validator')
    if report.get('material_envelope_transfer_definition') != module.definition():
        raise ValueError('The actual transfer policy is not the complete declared source policy')
    transfer = module.validate_metadata(report.get('material_envelope_transfer'),model=model,
        envelope=report['material_envelope'],caller_source_sha256=DRIVER_SHA,
        carrier_sha256=report['observation_carrier_sha256'])
    seed = module.validate_seed_metadata(report.get('prior_envelope_final_variable_seed'),
        report=report,model=model,transfer=report['material_envelope_transfer'])
    return transfer,seed
'''


def derive(parents, helper, frame_source, transfer):
    result = {NAMES['helper']:helper,NAMES['transfer']:transfer}
    cal = assign(parents['calibration'],'ENDPOINT_SCHEMA',SCHEMAS['operator'])
    result[NAMES['calibration']] = cal
    op = assign(parents['operator'],'SCHEMA',SCHEMAS['operator'])
    op = replace(op,'from dataclasses import dataclass\n','from dataclasses import dataclass\nfrom contextlib import nullcontext\n')
    op = assign(op,'REFERENCE_CENTERING_SOURCE_SHA256',digest(cal))
    op = replace(op,"FRAME_C1_SOURCE_SHA256 = '"+FRAME_SOURCE_SHA+"'\n",
        "FRAME_C1_SOURCE_SHA256 = '"+FRAME_SOURCE_SHA+"'\nSTAGE_MATRIX_SOURCE_SHA256 = '"+digest(helper)+"'\n")
    op = replace(op,'reference_centering_module=None, frame_c1_module=None):',
        'reference_centering_module=None, frame_c1_module=None, stage_matrix_module=None):')
    op = replace(op,'        self.reference_calibration = reference_centering_module.FrozenReferenceCalibration(',
        OPERATOR_GUARD+'        self.reference_calibration = reference_centering_module.FrozenReferenceCalibration(')
    op = replace(op,'            normal_frame_C1_reuse=frame_c1_module.definition(),\n',
        '            normal_frame_C1_reuse=frame_c1_module.definition(),\n'
        '            detached_stage_matrix_reuse=stage_matrix_module.definition(),\n')
    op = replace(op,'        self.frame_c1 = frame_c1_module.NormalFrameC1Kernel(self)\n',
        '        self.frame_c1 = frame_c1_module.NormalFrameC1Kernel(self)\n'
        '        self.stage_matrices = stage_matrix_module.CompleteDetachedStageMatrices(self,frame_c1_module=frame_c1_module)\n')
    op = replace(op,'        with torch.no_grad(), self.frame_c1.value_scope(data,keys,order) as frame_values:\n',
        '        with torch.no_grad(), self.frame_c1.value_scope(data,keys,order) as frame_values, (\n'
        "                self.stage_matrices.scope(data,keys,order,'returned_value_J3')\n"
        '                if existing is None else nullcontext()) as stage_matrices:\n')
    op = replace(op,'                        matrix = self._stage_jacobian(eta,data,previous,frame,zero,tau)\n',
        '                        matrix = stage_matrices.scalar(eta,previous,frame,zero,tau,index-1)\n'
        "                        stage_record['returned_value_matrix_origin'] = json.loads(json.dumps(\n"
        '                            stage_matrices.last_request_record,allow_nan=False))\n')
    start = op.index('                for index in range(self.normal_stage_count):\n',op.index('    def _get_roots('))
    end = op.index('        return items\n',start)
    original = op[start:end]
    wrapped = ("                with self.stage_matrices.scope(subset,[keys[i] for i in needed],order,\n"
        "                        'complete_angular_J6_J9') as stage_matrices:\n"
        +''.join('    '+line if line.strip() else line for line in original.splitlines(keepends=True)))
    wrapped = replace(wrapped,
        '                            matrix = self._stage_jet_jacobian(eta,subset,previous,frame,zero,\n'
        '                                self.normal_step_carriers[index+1],order)\n',
        '                            matrix = stage_matrices.angular(eta,previous,frame,zero,\n'
        '                                self.normal_step_carriers[index+1],index,order)\n')
    op = op[:start]+wrapped+op[end:]
    op = replace(op,'            normal_frame_C1_reuse=self.frame_c1.metadata(),\n',
        '            normal_frame_C1_reuse=self.frame_c1.metadata(),\n'
        '            detached_stage_matrix_reuse=self.stage_matrices.metadata(),\n')
    result[NAMES['operator']] = op
    geometry = assign(parents['geometry'],'SCHEMA',SCHEMAS['geometry'])
    geometry = assign(geometry,'OPERATOR_SCHEMA',SCHEMAS['operator'])
    geometry = assign(geometry,'ENDPOINT_SOURCE_SHA256',digest(op))
    geometry = assign(geometry,'REFERENCE_CENTERING_SOURCE_SHA256',digest(cal))
    geometry = replace(geometry,'BASE_OPERATOR_SCHEMA = ',"STAGE_MATRIX_SOURCE_SHA256 = '"+digest(helper)+"'\nBASE_OPERATOR_SCHEMA = ")
    geometry = replace(geometry,"        self.operator_sha256 = model['source_sha256']\n",
        GEOMETRY_GUARD+"        self.operator_sha256 = model['source_sha256']\n")
    result[NAMES['geometry']] = geometry
    driver = assign(parents['driver'],'SCHEMA',SCHEMAS['driver'])
    pins = literal(driver,'SOURCE_PINS')
    for role,key in (('endpoint','operator'),('reference_calibration','calibration'),('geometry','geometry')):
        pins[role] = ('scripts/resume_20261126/'+NAMES[key],digest(result[NAMES[key]]))
    pins['stage_matrices'] = ('scripts/resume_20261126/'+NAMES['helper'],digest(helper))
    pins['envelope_transfer'] = ('scripts/resume_20261126/'+NAMES['transfer'],digest(transfer))
    for role,parent_key in (('envelope_parent_reader','reader'),('envelope_parent_driver','driver'),
            ('envelope_parent_endpoint','operator'),('envelope_parent_calibration','calibration'),
            ('envelope_parent_geometry','geometry')):
        pins[role] = ('scripts/resume_20261126/'+PARENTS[parent_key][0],PARENTS[parent_key][1])
    driver = assign(driver,'SOURCE_PINS',pins)
    driver = replace(driver,'def all_locations(args, preparation, q, history, restart=None, source_report_path=None, *, envelope_memory):\n'
        '    """Explicit new permanent-envelope policy with the original complete known-history walker."""\n'
        '    return envelope_memory.load_memory(args,preparation,q,history,\n'
        '        restart=restart,source_report_path=source_report_path)\n',
        'def all_locations(args, preparation, q, history, restart=None, source_report_path=None, *, envelope_memory, envelope_transfer):\n'
        '    """Preserve the actual prior complete envelope addresses and typed memory across the new model."""\n'
        '    return envelope_transfer.load_memory(args,preparation,q,history,\n'
        '        memory=envelope_memory,current_driver_source=__file__,\n'
        '        restart=restart,source_report_path=source_report_path)\n')
    driver = replace(driver,"    p.add_argument('--material-envelope-binding', type=Path)\n",
        "    p.add_argument('--material-envelope-binding', type=Path)\n"
        "    p.add_argument('--material-envelope-parent-report', type=Path, action='append', default=[])\n")
    driver = replace(driver,'    a.manifest = [path.resolve() for path in a.manifest]\n',
        '    a.material_envelope_parent_report = [path.resolve() for path in a.material_envelope_parent_report]\n'
        '    a.manifest = [path.resolve() for path in a.manifest]\n')
    driver = add_explicit_final_seed_arguments(driver)
    driver = replace(driver,'    envelope_memory = load(',
        "    envelope_transfer = load('_actual_complete_envelope_transfer',paths['envelope_transfer'])\n    envelope_memory = load(")
    driver = replace(driver,'    witnesses, radius_witnesses, history_record, envelope = all_locations(\n',
        '    witnesses, radius_witnesses, history_record, envelope, envelope_transfer_record = all_locations(\n')
    driver = replace(driver,'        envelope_memory=envelope_memory)\n',
        '        envelope_memory=envelope_memory,envelope_transfer=envelope_transfer)\n'
        '    prior_final_point,prior_final_seed = envelope_transfer.seed_from_complete_prior_final(\n'
        '        args,q,current_driver_source=__file__,transfer_record=envelope_transfer_record)\n'
        '    if prior_final_point is not None:\n'
        '        x = prior_final_point\n')
    driver = replace(driver,'    frame_c1 = load(',"    stage_matrices = load('_actual_complete_detached_stage_matrices',paths['stage_matrices'])\n    frame_c1 = load(")
    driver = replace(driver,'reference_centering_module=calibration,frame_c1_module=frame_c1)',
        'reference_centering_module=calibration,frame_c1_module=frame_c1,stage_matrix_module=stage_matrices)')
    driver = replace(driver,"        normal_frame_C1_source=file_record(paths['frame_C1']),\n",
        "        normal_frame_C1_source=file_record(paths['frame_C1']),\n"
        '        detached_stage_matrix_reuse_definition=q.stage_matrices.definition,\n'
        "        detached_stage_matrix_source=file_record(paths['stage_matrices']),\n"
        '        all_original_Newton_stage_equations_and_full_implicit_chain_retained=True,\n'
        '        stage_matrix_cache_acceleration_or_rounding_certified=False,\n')
    driver = replace(driver,'        material_envelope_definition=envelope.definition,\n',
        '        material_envelope_definition=envelope.definition,\n'
        '        material_envelope_transfer=envelope_transfer_record,\n'
        '        material_envelope_transfer_definition=envelope_transfer.definition(),\n'
        "        material_envelope_transfer_source=file_record(paths['envelope_transfer']),\n"
        '        explicit_prior_final_variable_seed_requested=args.material_envelope_seed_checkpoint is not None,\n'
        '        prior_envelope_final_variable_seed=prior_final_seed,\n'
        '        initial_full_variable_point_sha256=meridian.array_sha(x),\n')
    driver = replace(driver,literal(parents['operator'],'SCHEMA'),SCHEMAS['operator'],
        count=driver.count(literal(parents['operator'],'SCHEMA')))
    result[NAMES['driver']] = driver
    launcher = replace(parents['launcher'],PARENTS['driver'][0],NAMES['driver'])
    launcher = assign(launcher,'DRIVER_SHA',digest(driver))
    launcher = replace(launcher,"    p.add_argument('--material-envelope-binding', type=Path)\n",
        "    p.add_argument('--material-envelope-binding', type=Path)\n"
        "    p.add_argument('--material-envelope-parent-report', type=Path, action='append', default=[])\n")
    launcher = replace(launcher,'    a.manifest = [path.resolve() for path in a.manifest]\n',
        '    a.material_envelope_parent_report = [path.resolve() for path in a.material_envelope_parent_report]\n'
        '    a.manifest = [path.resolve() for path in a.manifest]\n')
    launcher = add_explicit_final_seed_arguments(launcher)
    launcher = replace(launcher,'        args.scalar_input, *args.manifest]\n',
        '        args.scalar_input, *args.manifest, *args.material_envelope_parent_report]\n'
        '    if args.material_envelope_seed_checkpoint is not None:\n'
        '        inputs.extend([args.material_envelope_seed_checkpoint,args.material_envelope_seed_report])\n'
        '    if args.material_envelope_binding is not None:\n'
        '        inputs.append(args.material_envelope_binding)\n')
    launcher = replace(launcher,"schema='public-actions-complete-R711-reference-centred-normal-plane-SO3-command-v1'",
        "schema='public-actions-complete-R711-stage-matrix-envelope-transfer-SO3-command-v1'")
    launcher = replace(launcher,'        full_variables_and_original_positive_rows_preserved=True,\n',
        '        full_variables_and_original_positive_rows_preserved=True,\n'
        '        detached_stage_matrix_reuse_declared=True,\n'
        '        original_Newton_matrices_and_all_stage_equations_retained=True,\n'
        '        old_envelope_transferred_as_addresses_and_types_only=True,\n'
        '        measured_cache_hit_rate_or_speedup_claimed=False,\n')
    result[NAMES['launcher']] = launcher
    reader = replace(parents['reader'],PARENTS['driver'][0],NAMES['driver'])
    reader = assign(reader,'DRIVER_SHA',digest(driver))
    reader = assign(reader,'REPORT_SCHEMA',SCHEMAS['driver'])
    reader = replace(reader,literal(parents['operator'],'SCHEMA'),SCHEMAS['operator'],
        count=reader.count(literal(parents['operator'],'SCHEMA')))
    reader = replace(reader,"'actual-complete-R711-reference-centred-C1-material-envelope-normal-plane-SO3-scalar-readout-v1'",
        repr(SCHEMAS['readout']))
    reader = replace(reader,'\ndef material_envelope_binding(',READER_ADDITION+'\n\ndef material_envelope_binding(')
    reader = replace(reader,"    frame_binding = frame_reuse_binding(report,model,roles,topic/load_pins(driver)['frame_C1'][0])\n",
        "    frame_binding = frame_reuse_binding(report,model,roles,topic/load_pins(driver)['frame_C1'][0])\n"
        "    matrix_binding,matrix_read = detached_matrix_binding(report,model,roles,topic/load_pins(driver)['stage_matrices'][0])\n")
    reader = replace(reader,'    envelope_binding,envelope_check,envelope_row_check = material_envelope_binding(topic,report,roles,driver)\n',
        '    envelope_binding,envelope_check,envelope_row_check = material_envelope_binding(topic,report,roles,driver)\n'
        '    transfer_binding,prior_final_seed = transferred_envelope_binding(topic,report,model,roles,driver)\n')
    reader = replace(reader,'        normal_frame_C1_binding=frame_binding,\n',
        '        normal_frame_C1_binding=frame_binding,\n'
        '        detached_stage_matrix_binding=matrix_binding,\n'
        '        detached_stage_matrix_diagnostics=matrix_read(metadata),\n')
    reader = replace(reader,'        material_envelope_binding=envelope_binding,\n',
        '        material_envelope_binding=envelope_binding,\n'
        '        material_envelope_transfer=transfer_binding,\n'
        '        prior_envelope_final_variable_seed=prior_final_seed,\n'
        "        initial_full_variable_point_sha256=report['initial_full_variable_point_sha256'],\n")
    result[NAMES['reader']] = reader
    verify(parents,result,frame_source)
    return result


def verify(parents,result,frame_source):
    for name,text in result.items():
        output_check(text,name)
    op=result[NAMES['operator']]
    invariant=assert_methods(parents['operator'],op,'ZeroClosureOperator',
        {'__init__','_run_chain','_get_roots','metadata'})
    old_methods,new_methods=methods(parents['operator'],'ZeroClosureOperator'),methods(op,'ZeroClosureOperator')
    for name in literal(frame_source,'METHOD_AST'):
        if old_methods[name] != new_methods[name]:
            raise ValueError('One of the original nine C1 mathematical methods changed: '+name)
    if assert_methods(parents['calibration'],result[NAMES['calibration']],
            'FrozenReferenceCalibration',set()) < 1:
        raise ValueError('Keep every calibration method unchanged')
    assert_methods(parents['geometry'],result[NAMES['geometry']],'GeometryScreen',{'__init__'})
    driver=result[NAMES['driver']]
    marker='    def save_report():\n'
    if driver[driver.index(marker):] != parents['driver'][parents['driver'].index(marker):]:
        raise ValueError('Keep the entire already-complete envelope save/PhaseI/QP/true-screen suffix')
    assert_functions(parents['driver'],driver,{'main','all_locations','parse_args'})
    assert_functions(parents['launcher'],result[NAMES['launcher']],{'main','parse_args'})
    assert_functions(parents['reader'],result[NAMES['reader']],{'read_report'},
        {'read_detached_matrix_policy','detached_matrix_binding','transferred_envelope_binding'})
    before=parents['geometry'][parents['geometry'].index('    def _set_x('):]
    after=result[NAMES['geometry']][result[NAMES['geometry']].index('    def _set_x('):]
    if before != after:
        raise ValueError('Keep every full grid, all historical points and complete row selection byte')
    if EXPECTED and {name:digest(text) for name,text in result.items()} != EXPECTED:
        raise ValueError('The published full-source derivation identity changed')
    return invariant


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parent-directory',type=Path,action='append',required=True)
    parser.add_argument('--stage-source',type=Path,required=True)
    parser.add_argument('--transfer-source',type=Path,required=True)
    parser.add_argument('--frame-source',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    parser.add_argument('--verify-existing',action='store_true')
    args=parser.parse_args()
    parents={}
    for key,(name,expected) in PARENTS.items():
        candidates=[directory/name for directory in args.parent_directory if (directory/name).is_file()]
        if len(candidates) != 1:
            raise ValueError('Provide exactly one complete source location: '+name)
        parents[key]=checked(candidates[0],expected)
    helper=checked(args.stage_source,STAGE_SOURCE_SHA)
    frame=checked(args.frame_source,FRAME_SOURCE_SHA)
    transfer=checked(args.transfer_source,TRANSFER_SOURCE_SHA)
    result=derive(parents,helper,frame,transfer)
    args.outdir.mkdir(parents=True,exist_ok=True)
    for name,text in result.items():
        path=args.outdir/name
        if args.verify_existing:
            if not path.is_file() or path.read_bytes() != text.encode():
                raise ValueError('Full existing source differs: '+str(path))
        else:
            path.write_text(text)
    print(json.dumps(dict(complete=True,scientific_modules_imported=False,
        scientific_execution=False,original_nine_method_AST_unchanged=True,
        outputs={name:dict(bytes=len(text.encode()),sha256=digest(text)) for name,text in result.items()}),indent=2))


if __name__ == '__main__':
    main()
