#!/usr/bin/env python3
"""Pure complete-report binding for the actual missing-angle geometry.

This module loads explicitly selected standard-library-only functions
from the exact complete geometry and numerical-selector sources. It does not import that scientific
module, construct a field, or evaluate a root, derivative or quadrature.
The original complete pure geometry/envelope checks remain in the caller.
"""
import ast
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

SCHEMA = 'actual-fixed-fejer-r725-dk-cache-report-binding-v1'
ROLE = 'batched_geometry_binding'
GEOMETRY_NAME = 'so3_fixed_fejer_r725_dk_cache_geometry.py'
GEOMETRY_SHA256 = 'a609fd96e1b19f14c9050a03a93967b70bbcf38747457f604496154edd364ced'
GEOMETRY_BYTES = 88422
GEOMETRY_SCHEMA = 'complete-fixed-fejer-r725-dk-cache-world-geometry-v1'
CONSTANT_NAMES = (
    'MISSING_ANGLE_BATCH_SCHEMA',
    'MISSING_ANGLE_BATCH_PARENT_GEOMETRY_SHA256',
    'ENDPOINT_SOURCE_SHA256',
)
FUNCTION_NAMES = (
    'missing_angle_batch_policy',
    'validate_missing_angle_batches',
)


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def _sha_word(value):
    return (isinstance(value, str) and len(value) == 64
        and all(character in '0123456789abcdef' for character in value))


def _selected_geometry(path):
    """Compile the original selected pure bodies, not the scientific module."""
    path = Path(path).resolve()
    raw = path.read_bytes()
    if (path.name != GEOMETRY_NAME or len(raw) != GEOMETRY_BYTES
            or hashlib.sha256(raw).hexdigest() != GEOMETRY_SHA256):
        raise ValueError('Keep the exact entire new missing-angle geometry source')
    tree = ast.parse(raw.decode('utf-8'), filename=str(path))
    constants = {}
    functions = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            names = [target.id for target in node.targets if isinstance(target, ast.Name)]
            wanted = [name for name in names if name in CONSTANT_NAMES]
            if wanted:
                if len(node.targets) != 1 or len(wanted) != 1 or len(names) != 1:
                    raise ValueError('Use one literal binding per selected complete constant')
                name = wanted[0]
                if name in constants:
                    raise ValueError('Repeated selected geometry constant: '+name)
                value = ast.literal_eval(node.value)
                if not isinstance(value, str):
                    raise ValueError('The complete selected geometry constants are literal strings')
                constants[name] = (node, value)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in FUNCTION_NAMES:
            if (not isinstance(node, ast.FunctionDef) or node.decorator_list
                    or node.name in functions):
                raise ValueError('Keep one undecorated complete original pure function: '+node.name)
            functions[node.name] = node
    if set(constants) != set(CONSTANT_NAMES) or set(functions) != set(FUNCTION_NAMES):
        raise ValueError('Do not omit any original pure batching function or constant')
    if (constants['MISSING_ANGLE_BATCH_SCHEMA'][1]
            != 'complete-literal-missing-angle-normal-root-batching-v1'
            or not _sha_word(constants['MISSING_ANGLE_BATCH_PARENT_GEOMETRY_SHA256'][1])
            or not _sha_word(constants['ENDPOINT_SOURCE_SHA256'][1])):
        raise ValueError('The selected pure source identity contract differs')
    selected = [constants[name][0] for name in CONSTANT_NAMES]
    selected += [functions[name] for name in FUNCTION_NAMES]
    namespace = dict(__file__=str(path), sha=sha, canonical=canonical, math=math)
    module = ast.Module(body=selected, type_ignores=[])
    exec(compile(module, str(path), 'exec'), namespace)
    for name in FUNCTION_NAMES:
        function = namespace[name]
        if (Path(function.__code__.co_filename).resolve() != path
                or sha(function.__code__.co_filename) != GEOMETRY_SHA256):
            raise ValueError('The actual pure batching function lost its whole-source binding')
    if path.read_bytes() != raw:
        raise ValueError('The complete geometry source changed during pure binding')
    return path, namespace


CURVATURE_SELECTOR_NAME = 'fullclosed_point_inequalities_v2_r725_curvature_cache.py'
CURVATURE_SELECTOR_SHA256 = 'c378e098013b6d15fc51fe6cafda0415dfaecc331a81d7655c94ef97a11e294b'
CURVATURE_SELECTOR_BYTES = 35982
CURVATURE_CONSTANT_NAMES = ('_CURVATURE_CACHE_SCHEMA','_CURVATURE_CACHE_LIMIT',
    '_CURVATURE_CACHE_NORMAL_SHA256','_CURVATURE_CACHE_MERIDIAN_SHA256')
CURVATURE_FUNCTION_NAMES = ('_curvature_cache_sha',
    'complete_curvature_pullback_cache_definition',
    'validate_complete_curvature_pullback_cache')


def _selected_curvature_selector(path):
    """Read the complete selector; compile only its three original pure functions."""
    path = Path(path).resolve()
    raw = path.read_bytes()
    if (path.name != CURVATURE_SELECTOR_NAME or len(raw) != CURVATURE_SELECTOR_BYTES
            or hashlib.sha256(raw).hexdigest() != CURVATURE_SELECTOR_SHA256):
        raise ValueError('Keep the whole exact halfwave numerical-pullback selector')
    tree = ast.parse(raw.decode('utf-8'), filename=str(path))
    constants, functions = {}, {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            names = [item.id for item in node.targets if isinstance(item, ast.Name)]
            selected = [name for name in names if name in CURVATURE_CONSTANT_NAMES]
            if selected:
                if (len(node.targets) != 1 or len(names) != 1 or len(selected) != 1
                        or selected[0] in constants):
                    raise ValueError('Keep each complete pure selector constant exactly once')
                constants[selected[0]] = node
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in CURVATURE_FUNCTION_NAMES:
            if (not isinstance(node, ast.FunctionDef) or node.decorator_list
                    or node.name in functions):
                raise ValueError('Keep each original undecorated pure selector function')
            functions[node.name] = node
    if set(constants) != set(CURVATURE_CONSTANT_NAMES) or set(functions) != set(CURVATURE_FUNCTION_NAMES):
        raise ValueError('Do not drop any complete pure numerical-cache definition or validator')
    # The only nonliteral selected constant is the original 64*1024*1024.
    # Its entire source is already hard bound above; no scientific body is selected.
    nodes = [constants[name] for name in CURVATURE_CONSTANT_NAMES]
    nodes += [functions[name] for name in CURVATURE_FUNCTION_NAMES]
    namespace = dict(__file__=str(path), Path=Path, hashlib=hashlib)
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), 'exec'), namespace)
    if (namespace['_CURVATURE_CACHE_SCHEMA'] != 'complete-same-point-returned-curvature-pullback-cache-v1'
            or namespace['_CURVATURE_CACHE_LIMIT'] != 64*1024*1024
            or not _sha_word(namespace['_CURVATURE_CACHE_NORMAL_SHA256'])
            or not _sha_word(namespace['_CURVATURE_CACHE_MERIDIAN_SHA256'])):
        raise ValueError('The original whole numerical-cache source policy differs')
    for name in CURVATURE_FUNCTION_NAMES:
        if (Path(namespace[name].__code__.co_filename).resolve() != path
                or sha(namespace[name].__code__.co_filename) != CURVATURE_SELECTOR_SHA256):
            raise ValueError('The actual pure selector function lost its complete-source identity')
    if path.read_bytes() != raw:
        raise ValueError('The entire numerical selector changed during pure binding')
    return path, namespace


def _complete_curvature_cache_scopes(report, roles, geometry_path, identity):
    path, pure = _selected_curvature_selector(
        geometry_path.parent.parent/'resume_20261120'/CURVATURE_SELECTOR_NAME)
    policy = pure['complete_curvature_pullback_cache_definition']()
    if (roles.get('geometry_selector') != CURVATURE_SELECTOR_SHA256
            or policy.get('source_sha256') != CURVATURE_SELECTOR_SHA256
            or policy.get('old_source_normal_sha256') != roles.get('endpoint')
            or policy.get('old_source_meridian_helper_sha256') != roles.get('detached_meridian_values')):
        raise ValueError('Use the declared complete current normal, helper and selector source family')
    scopes = []
    for field, phase in (('metric_directions','metric'),('restoration_directions','restoration')):
        directions = report.get(field, [])
        if not isinstance(directions, list):
            raise ValueError('Retain the original complete direction list')
        for ordinal, direction in enumerate(directions):
            if not isinstance(direction, dict) or direction.get('phase') != phase:
                raise ValueError('Each returned cache scope belongs to its actual scientific direction')
            rows = direction.get('complete_selected_inequalities')
            start = direction.get('starting_geometry')
            if not isinstance(rows, dict) or not isinstance(start, dict):
                raise ValueError('Every recorded direction retains its original rows and starting geometry')
            point = rows.get('current_full_point_sha256')
            prefix = rows.get('original_selection_metadata')
            if (not _sha_word(point) or start.get('current_full_point_sha256') != point
                    or start.get('actual_model_identity_sha256') != identity
                    or not isinstance(prefix, dict)
                    or rows.get('original_selector_source_sha256') != CURVATURE_SELECTOR_SHA256):
                raise ValueError('A returned numerical cache may not use the report latest point in place of its own point')
            count = rows.get('original_prefix_rows')
            if (type(count) is not int or not 0 <= count <= 192
                    or prefix.get('selected_rows') != count
                    or not isinstance(prefix.get('rows'), list) or len(prefix['rows']) != count
                    or not isinstance(rows.get('rows'), list) or len(rows['rows']) < count):
                raise ValueError('The cache must retain every original selected prefix row in its actual order')
            source = rows.get('source_binding')
            if (not isinstance(source, dict)
                    or source.get('source_sha256') != GEOMETRY_SHA256
                    or source.get('actual_model_identity_sha256') != identity
                    or source.get('current_selector_source_sha256') != CURVATURE_SELECTOR_SHA256
                    or source.get('complete_curvature_pullback_cache_policy') != policy):
                raise ValueError('The full row builder must bind this actual complete selector policy')
            checked = pure['validate_complete_curvature_pullback_cache'](
                prefix.get('complete_curvature_pullback_cache'), selected_rows=count,
                current_full_point_sha256=point, model_identity_sha256=identity)
            scopes.append(dict(direction_list=field, ordinal=ordinal,
                direction_index=direction.get('index'), direction_serial=direction.get('serial'),
                current_full_point_sha256=point, original_prefix_rows=count,
                complete_original_prefix_row_metadata_sha256=canonical(prefix['rows']),
                actual_complete_cache_record=checked))
    return dict(schema='actual-complete-halfwave-curvature-pullback-cache-binding-v1',
        selector_source=dict(path=str(path), bytes=CURVATURE_SELECTOR_BYTES,
            sha256=CURVATURE_SELECTOR_SHA256),
        actual_model_identity_sha256=identity, policy=policy,
        policy_identity_sha256=canonical(policy), scopes=scopes,
        complete_actual_direction_scopes=len(scopes),
        every_recorded_direction_own_point_used=True,
        logical_requests_not_counted_as_actual_point_vjp_executions=True,
        original_complete_direction_and_row_validators_still_required=True,
        missing_future_direction_or_final_values_created=False,
        field_root_derivative_or_quadrature_evaluations=0,
        scientific_module_imported=False,
        independent_scientific_admission_gate_created=False)


def bind_report(report, *, source_by_role, geometry_source):
    """Return (static complete binding, full_geometry_check) without science.

    The caller keeps its original material-envelope and geometric validators.
    The closure is applied to each actual original complete or partial scan,
    with that scan's own full-point SHA rather than the report's latest point.
    """
    if not isinstance(report, dict) or not isinstance(source_by_role, dict):
        raise ValueError('Use the complete actual report and complete source-role map')
    roles = dict(source_by_role)
    if report.get('source_sha256_by_role') != roles:
        raise ValueError('The complete actual source-role map cannot be replaced by a projection')
    own_path = Path(__file__).resolve()
    own_sha = sha(own_path)
    if roles.get(ROLE) != own_sha or roles.get('geometry') != GEOMETRY_SHA256:
        raise ValueError('Bind both this full pure module and the entire actual geometry')
    path, pure = _selected_geometry(geometry_source)
    policy = pure['missing_angle_batch_policy']()
    if (policy.get('source_sha256') != GEOMETRY_SHA256
            or policy.get('operator_source_sha256') != pure['ENDPOINT_SOURCE_SHA256']
            or policy.get('parent_geometry_source_sha256')
                != pure['MISSING_ANGLE_BATCH_PARENT_GEOMETRY_SHA256']
            or roles.get('endpoint') != pure['ENDPOINT_SOURCE_SHA256']):
        raise ValueError('Keep the actual whole normal source in the complete geometry policy')
    model = report.get('representation')
    identity = report.get('model_identity_sha256')
    if (not isinstance(model, dict) or not _sha_word(identity)
            or canonical(model) != identity
            or model.get('source_sha256') != roles['endpoint']):
        raise ValueError('The complete actual representation must match its own model identity')
    working = report.get('working_evaluation')
    nodes = model.get('exact_normal_step_nodes')
    if (not isinstance(working, dict) or not isinstance(nodes, list)
            or len(nodes) < 2 or any(not isinstance(value, str) for value in nodes)):
        raise ValueError('Keep the whole exact normal partition and working evaluation')
    exact = [Fraction(value) for value in nodes]
    if (exact[0] != 0 or exact[-1] != 1
            or any(left >= right for left, right in zip(exact, exact[1:]))
            or [str(value) for value in exact] != nodes
            or working.get('exact_normal_step_nodes') != nodes):
        raise ValueError('The complete declared normal partition must be the same exact ordered nodes')
    stage_count = len(nodes)-1
    angle_block = working.get('angle_block')
    if (type(working.get('normal_stage_count')) is not int
            or working['normal_stage_count'] != stage_count
            or type(angle_block) is not int or angle_block < 1):
        raise ValueError('Match actual stages to node count minus one and retain the whole angle block')
    if (not _sha_word(roles.get('detached_meridian_values'))
            or not isinstance(model.get('detached_meridian_value_reuse'), dict)
            or model['detached_meridian_value_reuse'].get('source_sha256')
                != roles['detached_meridian_values']):
        raise ValueError('Retain the actual complete detached-meridian source in this same model')
    policy_identity = canonical(policy)
    curvature_cache = _complete_curvature_cache_scopes(report, roles, path, identity)
    binding = dict(schema=SCHEMA, source_sha256=own_sha,
        geometry_source=dict(path=str(path), bytes=GEOMETRY_BYTES, sha256=GEOMETRY_SHA256),
        geometry_schema=GEOMETRY_SCHEMA,
        complete_geometry_parent_sha256=pure['MISSING_ANGLE_BATCH_PARENT_GEOMETRY_SHA256'],
        actual_operator_source_sha256=roles['endpoint'],
        actual_detached_meridian_source_sha256=roles['detached_meridian_values'],
        actual_model_identity_sha256=identity,
        exact_normal_step_nodes=list(nodes), normal_stage_count=stage_count,
        angle_block=angle_block, policy=policy, policy_identity_sha256=policy_identity,
        complete_curvature_pullback_cache=curvature_cache,
        original_complete_geometric_validator_required=True,
        individual_scan_own_point_required=True,
        partial_scans_not_promoted=True,
        working_singleton_word_equality_claimed=False,
        field_root_derivative_or_quadrature_evaluations=0,
        scientific_module_imported=False,
        independent_scientific_admission_gate_created=False)

    def full_geometry_check(value):
        if value is None:
            return None
        if (not isinstance(value, dict) or value.get('schema') != GEOMETRY_SCHEMA
                or value.get('actual_model_identity_sha256') != identity
                or type(value.get('complete')) is not bool):
            raise ValueError('Use an actual complete or partial scan from this whole geometry and model')
        complete = value['complete']
        point = value.get('current_full_point_sha256')
        if ((point is not None and not _sha_word(point)) or (complete and point is None)):
            raise ValueError('Every actual completed scan has its own complete point word identity')
        record = value.get('missing_angle_root_batches')
        if (not isinstance(record, dict)
                or record.get('original_angle_block') != angle_block
                or record.get('normal_stage_count') != stage_count):
            raise ValueError('The scan cannot change its report angle block or complete normal stage count')
        source = value.get('source_binding')
        if complete and not isinstance(source, dict):
            raise ValueError('Keep the complete actual geometry source binding on a successful scan')
        if source is not None:
            if (not isinstance(source, dict) or source.get('schema') != GEOMETRY_SCHEMA
                    or source.get('source_sha256') != GEOMETRY_SHA256
                    or source.get('operator_source_sha256') != roles['endpoint']
                    or source.get('actual_model_identity_sha256') != identity
                    or source.get('missing_angle_root_batch_policy') != policy
                    or source.get('current_selector_source_sha256') != CURVATURE_SELECTOR_SHA256
                    or source.get('complete_curvature_pullback_cache_policy') != curvature_cache['policy']
                    or source.get('detached_meridian_value_source_sha256')
                        != roles['detached_meridian_values']):
                raise ValueError('The actual scan source/policy must be this same complete report family')
        checked = pure['validate_missing_angle_batches'](record,
            model_identity=identity, point_sha256=point, geometry_complete=complete)
        if (not isinstance(checked, dict)
                or checked.get('actual_model_identity_sha256') != identity
                or checked.get('current_full_point_sha256') != point
                or checked.get('policy_identity_sha256') != policy_identity):
            raise ValueError('Keep the original pure validator result at its own actual point')
        if complete and (
                type(value.get('permanent_unique_locations_read')) is not int
                or checked['original_union_location_count'] != value['permanent_unique_locations_read']
                or checked['original_point_reads_completed'] != value['permanent_unique_locations_read']
                or value.get('all_permanent_curvature_and_radius_locations_read') is not True):
            raise ValueError('The complete batch record and original point loop must cover the same whole union')
        return dict(checked, geometry_complete=complete,
            geometry_source_sha256=GEOMETRY_SHA256,
            pure_binding_source_sha256=own_sha)

    return binding, full_geometry_check
