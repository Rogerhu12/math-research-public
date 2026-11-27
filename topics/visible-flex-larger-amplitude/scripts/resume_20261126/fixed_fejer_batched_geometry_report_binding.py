#!/usr/bin/env python3
"""Pure complete-report binding for the actual missing-angle geometry.

This module loads only two explicitly selected standard-library functions
from the exact complete geometry source. It does not import that scientific
module, construct a field, or evaluate a root, derivative or quadrature.
The original complete pure geometry/envelope checks remain in the caller.
"""
import ast
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

SCHEMA = 'actual-fixed-fejer-batched-geometry-report-binding-v1'
ROLE = 'batched_geometry_binding'
GEOMETRY_NAME = 'so3_fixed_fejer_batched_missing_angle_geometry.py'
GEOMETRY_SHA256 = '51b7a056baa6f81cac5d5acd5278d4258365f45bf5c98dd868cc520ecef7b898'
GEOMETRY_BYTES = 88163
GEOMETRY_SCHEMA = 'complete-fixed-fejer-batched-missing-angle-envelope-world-geometry-v1'
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
    binding = dict(schema=SCHEMA, source_sha256=own_sha,
        geometry_source=dict(path=str(path), bytes=GEOMETRY_BYTES, sha256=GEOMETRY_SHA256),
        geometry_schema=GEOMETRY_SCHEMA,
        complete_geometry_parent_sha256=pure['MISSING_ANGLE_BATCH_PARENT_GEOMETRY_SHA256'],
        actual_operator_source_sha256=roles['endpoint'],
        actual_detached_meridian_source_sha256=roles['detached_meridian_values'],
        actual_model_identity_sha256=identity,
        exact_normal_step_nodes=list(nodes), normal_stage_count=stage_count,
        angle_block=angle_block, policy=policy, policy_identity_sha256=policy_identity,
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
