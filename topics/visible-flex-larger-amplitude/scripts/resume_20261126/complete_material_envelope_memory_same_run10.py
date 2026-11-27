#!/usr/bin/env python3
"""Complete material envelope for an exactly reconstructed run10 fixed reference.

The complete original run10 target and finite reference words are retained only
through the explicit whole-input reconstruction bridge. Current runner files and
execution are separately recorded, never relabelled as the origin. No prior field
values or certificates are inherited. Complete old/current material addresses and
all unknown later source-bound history obligations remain required.

The full old/current material grids are implicit permanent nonlinear memory.
Known historical roles and protected rows are retained explicitly. Unknown old
roles/order are NOT reconstructed: every implicit point is potentially protected,
and a new typed separation policy is declared. This module's validators use only
the standard library. Actual carrier reads/history assembly require public Actions.
"""
import ast
import copy
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import sys
import zipfile

SCHEMA = 'complete-same-run10-reconstructed-reference-material-envelope-memory-v1'
SCAN_SCHEMA = 'complete-same-run10-reconstructed-reference-material-envelope-scan-v1'
DEFINITION_SCHEMA = 'literal-old-current-grid-same-run10-reconstructed-reference-policy-v1'
BINDING_SCHEMA = 'complete-same-run10-frozen-reference-input-bridge-v1'
RESTORER_SHA = '5989b2b299d9b6a9bbc2c6bd2ee87f04eb5288ead69bcc4ec6bbb9497b9e40f6'
REFERENCE_BINDING_NAME = 'same_run10_frozen_reference_input_binding.py'
REFERENCE_BINDING_SHA = '5aee3276dc2c70a3adc52dda618494a8ef458f4b1496c34a5c2640c00a5735b0'
PREPARATION_SCHEMA = 'complete-reconstructed-run10-reference-preparation-v1'
HISTORY_SHA = '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
PREPARATION_SHA = '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'
ORIGIN_CARRIER_SHA = 'dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0'
ORIGIN_CARRIER_BYTES = 227202
ORIGIN_WARM_SHA = '3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c'
ORIGIN_PARAMETERS_SHA = 'e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa'
ORIGIN_MESH_SHA = 'eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262'
ORIGIN_CHART_SHA = '90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e'
CURRENT_FIXED_CHART_SHA = '90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e'
CURRENT_REFERENCE_MODEL_SHA = '081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5'
FIXED_TARGET_SCHEMA = 'independently-frozen-actual-public-run10-scalar-and-material-chart-v1'
ORIGIN_P0 = {
    'curvature_points': {'count': 1250, 'sha256': '0d18c105c0899f463979a1a99b28c7c74cc26dd3f3132ad58bae8803374ba9a8'},
    'radius_points': {'count': 208, 'sha256': '1758d6f5c7376dacf573d8495f576e62d06277f0b3be158e7b7b444def79d471'},
    'protected_curvature_points': {'count': 18, 'sha256': '4959a1e7725524fee90517420406f6d3c1e1d12c1ca2255967d5b6056b43872a'},
}
SEED_NAMES = ('legacy_memory','restore_grid','restore_local','witness_positive','witness_lowphi',
    'full13_curvature','full13_radius','r17_grid','r17_local','r17_fixed','continue_union')
FAMILIES = ('reach','body_diameter','distance_plus','distance_minus','cap_diameter','height_floor')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Actual envelope/history consumption requires public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def _digest(value, label):
    if not isinstance(value, str) or len(value) != 64 or any(c not in '0123456789abcdef' for c in value):
        raise ValueError('Missing actual SHA256: '+label)
    return value


def definition(near_active_rows=32):
    if isinstance(near_active_rows, bool) or int(near_active_rows) != near_active_rows or near_active_rows < 1:
        raise ValueError('At least one explicit new near-active working row is required')
    return dict(schema=DEFINITION_SCHEMA, source_sha256=sha(__file__),
        exact_binary64_material_locations=True,
        historical_origin_carrier_sha256=ORIGIN_CARRIER_SHA,
        old_and_current_complete_grid_union=True,
        implicit_grid_permanently_has_both_curvature_branches=True,
        implicit_grid_permanently_has_radius_and_both_witness_signs=True,
        scalar_cap_and_height_rows_retained=True,
        all_implicit_locations_potentially_protected=True,
        entire_envelope_including_explicit_p0_potentially_protected=True,
        unknown_historical_protected_flags_or_order_reconstructed=False,
        unknown_historical_role_promotions_reconstructed=False,
        known_explicit_protected_prefix_preserved=True,
        original_192_selector_retained_on_known_explicit_memory=True,
        additional_current_near_active_rows=int(near_active_rows),
        discovered_typed_separation_rows_have_no_eviction_or_count_cap=True,
        new_typed_rows_use_complete_current_parameter_pullback=True,
        original_nonlinear_acceptance_thresholds_unchanged=True,
        original_full_free_space_norm_and_objective_formula_unchanged=True,
        historical_fixed_chart_sha256=ORIGIN_CHART_SHA,
        independent_fixed_chart_sha256=CURRENT_FIXED_CHART_SHA,
        origin_actual_public_input_run_id='45972294636',origin_actual_public_input_run_attempt='1',
        original_target_statement_about_pre_run10_history_is_unchanged=True,
        same_mathematical_g_scope='original run10 fixed target; not an assertion about every earlier target',
        same_finite_reference_words_as_origin_run10_verified=True,
        current_execution_and_full_input_provenance_are_separate=True,
        complete_independent_fixed_target_schema=FIXED_TARGET_SCHEMA,
        complete_target_definition_and_actual_current_files_required=True,
        target_fixed_before_any_current_field_evaluation=True,
        historical_angles_reinterpreted_as_new_fixed_chart_phi0=True,
        same_historical_physical_points_claimed=False,
        same_original_fixed_chart=True,same_mathematical_g_claimed=True,
        old_values_or_scientific_certificates_inherited=False,
        unresolved_parallel_history_remains_an_explicit_obligation=True,
        full_grid_coverage_is_not_a_continuous_geometry_certificate=True)


def npy_member(archive, name):
    raw = archive.read(name+'.npy')
    if raw[:6] != b'\x93NUMPY' or len(raw) < 10:
        raise ValueError('Not a complete literal NPY member: '+name)
    version = tuple(raw[6:8])
    if version == (1, 0):
        length, start = struct.unpack('<H', raw[8:10])[0], 10
    elif version in ((2, 0), (3, 0)):
        if len(raw) < 12:
            raise ValueError('Truncated NPY header')
        length, start = struct.unpack('<I', raw[8:12])[0], 12
    else:
        raise ValueError('Unsupported NPY version')
    end = start+length
    if end > len(raw):
        raise ValueError('Truncated NPY header payload')
    header = ast.literal_eval(raw[start:end].decode('utf-8' if version == (3, 0) else 'latin1'))
    if (not isinstance(header, dict) or set(header) != {'descr', 'fortran_order', 'shape'}
            or header['fortran_order'] is not False or not isinstance(header['shape'], tuple)
            or any(isinstance(v, bool) or not isinstance(v, int) or v < 0 for v in header['shape'])):
        raise ValueError('Require the complete C-order literal array')
    descriptor, shape, data = header['descr'], header['shape'], raw[end:]
    if descriptor in ('<f8', '<i8'):
        width = 8
    elif isinstance(descriptor, str) and descriptor.startswith('<U') and descriptor[2:].isdigit():
        width = 4*int(descriptor[2:])
    else:
        raise ValueError('No object arrays or changed binary64 dtype')
    if len(data) != width*math.prod(shape):
        raise ValueError('Complete NPY shape and payload differ')
    return descriptor, shape, data


def _array_sha(dtype, shape, data):
    h = hashlib.sha256(dtype.encode())
    h.update(json.dumps(list(shape)).encode())
    h.update(data)
    return h.hexdigest()


def _member(archive, name, dtype, shape):
    d, s, b = npy_member(archive, name)
    if d != dtype or s != tuple(shape):
        raise ValueError('Changed complete carrier member: '+name)
    code = '<d' if dtype == '<f8' else '<q'
    values = tuple(v for (v,) in struct.iter_unpack(code, b))
    if dtype == '<f8' and not all(math.isfinite(v) for v in values):
        raise ValueError('Nonfinite actual carrier word')
    return values, b


def read_carrier(path, expected_sha=None):
    require_actions()
    before = file_record(path)
    if expected_sha is not None and before['sha256'] != expected_sha:
        raise ValueError('Actual whole carrier differs from its declared source')
    with zipfile.ZipFile(path) as archive:
        cells, cb = _member(archive, 'observation_cells', '<i8', (7377,))
        local, ub = _member(archive, 'observation_u', '<f8', (7377,))
        gauss, gb = _member(archive, 'observation_gauss_unit_nodes', '<f8', (6,))
        mesh, mb = _member(archive, 'mesh', '<f8', (923,))
        legacy, _ = _member(archive, 'observation_legacy_count', '<i8', ())
        order, _ = _member(archive, 'observation_order', '<i8', ())
    if legacy != (1845,) or order != (6,) or len(set(v.hex() for v in gauss)) != 6:
        raise ValueError('Retain all original legacy and six Gauss carrier entries')
    if any(not 0 < v < 1 for v in gauss) or any(a >= b for a, b in zip(mesh, mesh[1:])):
        raise ValueError('Invalid actual full material carrier')
    expected = []
    for j in range(923):
        expected.append((min(j, 921), 1. if j == 922 else 0.))
        if j < 922:
            expected.append((j, .5))
    expected.extend((j, value) for j in range(922) for value in gauss)
    words = [(c, u.hex()) for c, u in zip(cells, local)]
    if words != [(c, u.hex()) for c, u in expected]:
        raise ValueError('The entire actual plan differs from the complete original unsplit plan')
    after = file_record(path)
    if before != after:
        raise ValueError('Carrier changed while its complete literal addresses were read')
    return dict(record=before, cells=cells, local=local, cell_bytes=cb, local_bytes=ub,
        radial_words=words, mesh_sha256=_array_sha('float64',(923,),mb),
        metadata=dict(record=before, complete_radial_entry_count=7377,
            complete_unique_radial_entry_count=len(set(words)), legacy_count=1845,
            cells_sha256=_array_sha('int64',(7377,),cb),
            local_u_sha256=_array_sha('float64',(7377,),ub),
            radial_words_sha256=canonical(words),
            gauss_unit_nodes_binary64_hex=[v.hex() for v in gauss],
            gauss_unit_nodes_sha256=_array_sha('float64',(6,),gb),
            full_plan_closed_form_checked=True))


def validate_public_binding(payload, *, current_input):
    if not isinstance(payload, dict) or payload.get('schema') != BINDING_SCHEMA:
        raise ValueError('Use the explicit complete carrier path binding')
    old, current = payload.get('origin_carrier', {}), payload.get('current_carrier', {})
    if old.get('sha256') != ORIGIN_CARRIER_SHA or old.get('bytes') != ORIGIN_CARRIER_BYTES:
        raise ValueError('The actual historical whole carrier is required')
    if current.get('sha256') != current_input['sha256'] or current.get('bytes') != current_input['bytes']:
        raise ValueError('The path binding names another current carrier')
    for value in (old, current):
        if not isinstance(value.get('path'), str) or not value['path']:
            raise ValueError('An actual runner path is required, not an invented blob address')
    producer = payload.get('producer', {})
    _digest(producer.get('source_sha256'), 'binding producer')
    if (producer.get('source_sha256') != RESTORER_SHA
            or not isinstance(producer.get('source_commit'), str)
            or len(producer['source_commit']) != 40
            or not producer.get('reconstruction_scope')
            or payload.get('original_full_carrier_sha_verified') is not True
            or payload.get('consumer_must_rehash_and_read_complete_arrays') is not True
            or payload.get('surface_history_values_or_certificates_inherited') is not False):
        raise ValueError('The carrier reconstruction evidence is incomplete')
    return copy.deepcopy(payload)


def _read_bound_json(record):
    path = Path(record['path'])
    raw = path.read_bytes()
    if len(raw) != record['bytes'] or hashlib.sha256(raw).hexdigest() != record['sha256']:
        raise ValueError('Complete provided history bytes differ: '+str(path))
    value = json.loads(raw)
    if sha(path) != record['sha256']:
        raise ValueError('History changed during its actual read')
    return value



def _validate_independent_target_binding(binding, *, actual_model=None, current_carrier=None,
        current_preparation_report=None, current_reference_bundle=None,
        current_node_report=None, current_scalar_input=None):
    """Consume the whole new bridge; preserve the original target as origin evidence."""
    path=Path(__file__).with_name(REFERENCE_BINDING_NAME)
    if sha(path)!=REFERENCE_BINDING_SHA:
        raise ValueError('Use the complete explicit same-reference binding source')
    name='_same_run10_memory_bridge_'+REFERENCE_BINDING_SHA
    if name not in sys.modules:
        spec=importlib.util.spec_from_file_location(name,path)
        if spec is None or spec.loader is None:
            raise ValueError('The complete same-reference bridge cannot be loaded')
        module=importlib.util.module_from_spec(spec)
        sys.modules[name]=module
        spec.loader.exec_module(module)
    module=sys.modules[name]
    if (sha(module.__file__)!=REFERENCE_BINDING_SHA
            or sha(module.validate_bridge.__code__.co_filename)!=REFERENCE_BINDING_SHA):
        raise ValueError('The actual whole bridge validator differs')
    supplied={key:item for key,item in dict(current_carrier=current_carrier,
        current_preparation_report=current_preparation_report,
        current_reference_bundle=current_reference_bundle,current_node_report=current_node_report,
        current_scalar_input=current_scalar_input).items() if item is not None}
    result=module.validate_bridge(binding,expected_producer_source_sha256=RESTORER_SHA,
        current_files=supplied)
    target=binding['fixed_target_definition']
    if (actual_model is not None and target['complete_current_reference_model']!=actual_model):
        raise ValueError('The caller uses a different complete frozen reference model')
    if (result.get('source_sha256')!=REFERENCE_BINDING_SHA
            or result.get('producer_source_sha256')!=RESTORER_SHA
            or result.get('fixed_target_definition_identity_sha256')!=canonical(target)
            or result.get('actual_current_model_identity_sha256')!=CURRENT_REFERENCE_MODEL_SHA
            or result.get('current_fixed_chart_core_sha256')!=CURRENT_FIXED_CHART_SHA
            or result.get('origin_actual_run_id')!='45972294636'
            or result.get('same_mathematical_g_as_origin_run10_verified') is not True
            or result.get('same_finite_reference_words_as_origin_run10_verified') is not True
            or result.get('current_provenance_is_not_origin_provenance') is not True
            or result.get('original_target_claim_about_pre_run10_history_rewritten') is not False
            or result.get('scientific_certificates_inherited') is not False):
        raise ValueError('The complete original definition and actual new input bridge disagree')
    return result

def _point_key(value):
    c, u, p = int(value['cell']), float(value['u']), float(value['phi'])
    if (isinstance(value['cell'], bool) or c != value['cell'] or not 0 <= c < 922
            or not 0 <= u <= 1 or not math.isfinite(u) or not math.isfinite(p)):
        raise ValueError('Invalid actual literal material point')
    return c, u.hex(), p.hex()


def _fingerprint(arrays):
    return {key: dict(count=len(arrays[key]), sha256=canonical(sorted(
        [int(c),float(u).hex(),float(p).hex()] for c,u,p in arrays[key]))) for key in ORIGIN_P0}


def _original_p0(args, preparation, history, old_path):
    provenance = _read_bound_json(preparation['complete_supplied_location_provenance'])
    if (provenance.get('schema') != 'independent-axisymmetric-SO3-complete-supplied-history-v1'
            or provenance.get('actual_carrier_sha256') != sha(args.carrier)
            or provenance.get('actual_reference_bundle_sha256') != sha(args.reference_bundle)):
        raise ValueError('Use the actual complete current supplied-history provenance')
    packages = [v for v in provenance['ordered_inputs']
        if v.get('kind') == 'complete-published-a04-historical-package']
    if len(packages) != 1:
        raise ValueError('The one complete ordered eleven-payload origin is required')
    item = packages[0]
    package = item['original_payload']
    seeds = package['seeds']
    if (package.get('schema') != 'a04-historical-location-parameters-v1'
            or tuple(seeds) != SEED_NAMES or item.get('exact_original_node_scalar_grid_binding') is not True
            or item['original_topology'] != package['topology']
            or tuple(v['name'] for v in item['ordered_records']) != SEED_NAMES):
        raise ValueError('The complete source-verified ordered eleven payloads changed')
    result = history.Locations(923, 7377, 2048)
    for name, summary in zip(SEED_NAMES, item['ordered_records']):
        record = seeds[name]
        value = record['payload']
        if (canonical(value) != summary['original_payload_identity_sha256']
                or canonical(record) != summary['original_record_identity_sha256']
                or record['historical_source_sha256'] != summary['historical_source_sha256']
                or summary.get('full_payload_and_order_retained') is not True
                or summary.get('capacity_used_to_drop_positions') is not False):
            raise ValueError('Incomplete actual original payload or role provenance')
        for key, role in (('curvature_locations','curvature'),('radius_locations','radius'),
                          ('grid_curvature_locations','curvature'),('grid_radius_locations','radius')):
            for stage, angle in value.get(key, []):
                if name == 'legacy_memory' and not 0 <= int(stage) < 1845:
                    raise ValueError('The original legacy prefix changed')
                result.grid(stage, result.angle(angle), role, False, 'complete_old_p0.'+name+'.'+key)
        role = 'radius' if name == 'full13_radius' else ('curvature' if name in
            ('full13_curvature','witness_positive','witness_lowphi') else None)
        result.walk(value, path=('complete_old_p0',name,'payload'), role=role)
    result.resolve_grid(old_path)
    arrays = result.arrays()
    fingerprints = _fingerprint(arrays)
    if fingerprints != ORIGIN_P0:
        raise ValueError('Full original P0 word sets/roles/protected set were not actually reproduced')
    return result, dict(complete_supplied_provenance=copy.deepcopy(preparation['complete_supplied_location_provenance']),
        original_payload_count=11, ordered_payload_names=list(SEED_NAMES),
        original_p0_fingerprints=fingerprints, original_p0_combined_sha256=canonical(fingerprints),
        all_eleven_complete_payloads_consumed=True, actual_old_carrier_used_for_indexed_points=True)


def _indexed_grid(value):
    if isinstance(value, dict):
        return ('stage' in value and 'angle' in value and 'phi' not in value) or any(_indexed_grid(v) for v in value.values())
    if isinstance(value, list):
        return (bool(value) and isinstance(value[0],str) and value[0] in ('grid','grid_radius')) or any(_indexed_grid(v) for v in value)
    return False


def load_memory(args, preparation, q, history, *, restart=None, source_report_path=None):
    require_actions()
    if sha(history.Locations.walk.__code__.co_filename) != HISTORY_SHA:
        raise ValueError('Retain the complete original location walker')
    actual_model = preparation.get('reference_definition', {})
    if (preparation.get('schema') != PREPARATION_SCHEMA
            or preparation.get('source_sha256') != RESTORER_SHA or preparation.get('complete') is not True
            or canonical(actual_model) != preparation.get('reference_model_identity_sha256')
            or q.base.model.get('complete_axisymmetric_reference_model') != actual_model
            or actual_model.get('original_scalar_parameters_identity_sha256') != ORIGIN_PARAMETERS_SHA
            or int(preparation['N']) != 2048 or q.full_N != 2048 or q.N != 513
            or q.J != 923 or q.P != 7377):
        raise ValueError('Use the actual complete independently frozen reference and full material chart')
    current = read_carrier(args.carrier)
    binding_path = getattr(args, 'material_envelope_binding', None)
    if binding_path is None:
        raise ValueError('The independent new target requires its complete explicit path binding')
    binding_record = file_record(binding_path)
    binding = validate_public_binding(_read_bound_json(binding_record), current_input=current['record'])
    if file_record(binding['current_carrier']['path']) != current['record']:
        raise ValueError('Binding path is not the same actual current file')
    old = read_carrier(binding['origin_carrier']['path'], ORIGIN_CARRIER_SHA)
    if old['record'] != binding['origin_carrier']:
        raise ValueError('Actual original file record changed')
    binding = dict(binding, binding_file=binding_record)
    independent_target_validation = _validate_independent_target_binding(binding,
        actual_model=actual_model,current_carrier=current['record'],
        current_preparation_report=file_record(args.preparation_report),
        current_reference_bundle=file_record(args.reference_bundle),
        current_node_report=file_record(args.node_report),current_scalar_input=file_record(args.scalar_input))
    if (old['record']['bytes'] != ORIGIN_CARRIER_BYTES
            or old['mesh_sha256'] != ORIGIN_MESH_SHA or current['mesh_sha256'] != ORIGIN_MESH_SHA
            or q.observation_cells.tobytes() != current['cell_bytes']
            or q.observation_u.tobytes() != current['local_bytes']):
        raise ValueError('Complete actual mesh/current material words differ from the bound field')
    phi = [float(v) for v in q.phi]
    expected_phi = [math.pi*j/1024 for j in range(513)]
    if [v.hex() for v in phi] != [v.hex() for v in expected_phi]:
        raise ValueError('Use every literal quarter-angle word of the actual original formula')
    chart = q.base.context.core
    target = binding['fixed_target_definition']
    if (str(chart.dtype) != 'float64' or list(chart.shape) != [160]
            or _array_sha('float64',(160,),chart.tobytes()) != CURRENT_FIXED_CHART_SHA
            or [float(v).hex() for v in chart] != target['fixed_chart_core_binary64_hex']
            or target['complete_current_reference_model'] != actual_model
            or target['current_reference_model_identity_sha256'] != canonical(actual_model)):
        raise ValueError('The complete current chart differs from the independently frozen target')
    original, origin_record = _original_p0(args, preparation, history, old['record']['path'])
    points = history.Locations(q.J, q.P, q.full_N)
    points.walk(original.arrays(), path=('complete_actual_original_p0',))
    sources = [file_record(args.preparation_report)]
    # The complete current original history is a required input in its own
    # right; its inclusion does not depend on a caller repeating --manifest.
    prepared_locations = _read_bound_json(preparation['new_locations'])
    if (prepared_locations.get('schema') != 'independent-axisymmetric-SO3-literal-position-input-v1'
            or prepared_locations.get('carrier_sha256') != current['record']['sha256']
            or prepared_locations.get('reference_bundle_sha256') != sha(args.reference_bundle)
            or prepared_locations.get('N') != q.full_N
            or prepared_locations.get('complete_supplied_provenance') != preparation['complete_supplied_location_provenance']):
        raise ValueError('The complete actual prepared location input is required')
    points.walk(prepared_locations,path=('complete_actual_current_prepared_locations',))
    sources.append(copy.deepcopy(preparation['new_locations']))
    if restart is not None:
        if int(restart['N']) != q.full_N or source_report_path is None:
            raise ValueError('Bind the entire actual same-grid restart report')
        points.walk(restart, path=('complete_actual_new_policy_restart',))
        sources.append(file_record(source_report_path))
    for path in args.manifest:
        before = file_record(path)
        payload = _read_bound_json(before)
        if payload.get('carrier_sha256',payload.get('observation_carrier_sha256')) != current['record']['sha256']:
            raise ValueError('Explicit current-history manifests must bind the actual current carrier')
        if _indexed_grid(payload) and int(payload.get('N',payload.get('full_angles',payload.get('full_N',-1)))) != q.full_N:
            raise ValueError('Do not reinterpret a tagged historical angle')
        if payload.get('schema') == 'deep-valley-same-symbolic-location-transfer-v1':
            payload = {key:payload[key] for key in ORIGIN_P0}
        points.walk(payload, path=('explicit_complete_history',Path(path).name))
        sources.append(before)
    before = points.summary()
    resolved = points.resolve_grid(args.carrier)
    arrays = points.arrays()
    protected = {(int(c),float(u).hex(),float(p).hex()) for c,u,p in arrays['protected_curvature_points']}
    witnesses = [dict(cell=int(c),u=float(u),phi=float(p),protected=(int(c),float(u).hex(),float(p).hex()) in protected)
        for c,u,p in arrays['curvature_points']]
    radii = [dict(cell=int(c),u=float(u),phi=float(p)) for c,u,p in arrays['radius_points']]
    record = dict(sources=sources, before=before, resolved_grid_positions=resolved, after=points.summary(),
        original_history=origin_record, exact_binary_identity=True, old_values_or_certificates_inherited=False,
        new_locations_use='fixed initial-reference material chart phi0, never current internal phi_c',
        legacy_angle_reinterpretation='literal historical angles retained as material phi0; no same physical point assertion',
        independent_fixed_target_validation=independent_target_validation)
    envelope = MaterialEnvelope(q, current, old, phi, binding, origin_record,
        witnesses, radii, int(getattr(args,'envelope_near_active_rows',32)))
    if restart is not None:
        envelope.restore(restart.get('material_envelope'))
    return witnesses, radii, record, envelope


class MaterialEnvelope:
    def __init__(self, q, current, old, phi, binding, origin_record, witnesses, radii, near_active_rows):
        require_actions()
        self.definition = definition(near_active_rows)
        self.identity = canonical(self.definition)
        self.model_identity = q.identity
        self.current_sha = current['record']['sha256']
        self.current_radial = set(current['radial_words'])
        self.origin_radial = set(old['radial_words'])
        self.radial_union = self.current_radial | self.origin_radial
        self.phi_hex = {v.hex() for v in phi}
        self.extra_words = sorted(self.origin_radial-self.current_radial)
        self.extra_cells = tuple(c for c,u in self.extra_words)
        self.extra_u = tuple(float.fromhex(u) for c,u in self.extra_words)
        self.explicit = {_point_key(v):copy.deepcopy(v) for v in list(witnesses)+list(radii)}
        self._separation = {}
        self._counters = dict(scan_attempts=0,complete_scans=0,incomplete_scans=0,
            discovered_typed_constraints=0,working_row_builds=0,appended_rows_total=0)
        phi_bytes = b''.join(struct.pack('<d',v) for v in phi)
        self._fixed = dict(schema=SCHEMA,source_sha256=sha(__file__),definition=self.definition,
            definition_identity_sha256=self.identity,actual_model_identity_sha256=q.identity,
            current_carrier_sha256=self.current_sha,
            independent_fixed_target_definition_identity_sha256=binding['fixed_target_definition_identity_sha256'],
            same_original_fixed_chart=True,same_mathematical_g_claimed=True,
            historical_address_binding=dict(complete=True,origin_carrier=old['metadata'],
                current_carrier=current['metadata'],actual_path_binding=binding,
                original_p0=origin_record,old_and_current_entire_arrays_actually_read=True,
                old_current_radial_word_sets_equal=self.origin_radial==self.current_radial),
            implicit_grid=dict(current_radial_entry_count=len(current['radial_words']),
                current_unique_radial_count=len(self.current_radial),origin_unique_radial_count=len(self.origin_radial),
                extra_historical_radial_count=len(self.extra_words),union_unique_radial_count=len(self.radial_union),
                angular_count=len(phi),full_angular_count=q.full_N,
                actual_phi_sha256=_array_sha('float64',(len(phi),),phi_bytes),
                phi_formula='binary64 pi * integer j / 1024, j=0,...,512',
                union_radial_words_sha256=canonical(sorted(self.radial_union)),
                extra_radial_words_sha256=canonical(self.extra_words),
                unique_implicit_material_locations=len(self.radial_union)*len(phi)),
            potentially_protected_policy='entire E including explicit P0 and implicit grids, all typed families; known explicit protected prefix retains original roles; unknown old role promotions and order are not reconstructed',
            known_explicit_history=dict(initial_unique_locations=len(self.explicit),
                initial_binary_locations_sha256=canonical(sorted(self.explicit)),
                complete_original_p0_preserved=True,complete_eleven_payloads_preserved=True),
            unknown_old_individual_protected_labels_or_order_reconstructed=False,
            same_continuous_field_certificate_inherited=False,
            continuous_geometry_certified=False,continuous_metric_certified=False)

    def contains(self, location):
        key = _point_key(location)
        return key in self.explicit or ((key[0],key[1]) in self.radial_union and key[2] in self.phi_hex)

    def admit_explicit(self, values):
        for value in values:
            key = _point_key(value)
            if not self.contains(value):
                raise ValueError('An unbound material point was introduced outside the complete envelope')
            if key in self.explicit:
                self.explicit[key]['protected'] = bool(self.explicit[key].get('protected',False) or value.get('protected',False))

    def _separate(self, family, location, *, partner=None, branch=None, sign=None, token=None):
        if family not in FAMILIES:
            raise ValueError('Unknown full-envelope physical family')
        if location is not None and not self.contains(location):
            raise ValueError('A newly separated address escaped the bound complete envelope')
        if partner is not None and partner.get('location') is not None and not self.contains(partner['location']):
            raise ValueError('A diameter partner escaped the complete material envelope')
        if location is not None:
            location = dict(cell=int(location['cell']),u=float(location['u']),phi=float(location['phi']))
        if partner is not None:
            partner = copy.deepcopy(partner)
            if partner.get('location') is not None:
                v = partner['location']
                partner['location'] = dict(cell=int(v['cell']),u=float(v['u']),phi=float(v['phi']))
        row = dict(family=family,location=location,partner=partner,branch=branch,sign=sign)
        key = canonical(row)
        if key not in self._separation:
            row.update(first_discovered_current_full_point_sha256=token,origin='actual complete envelope nonlinear scan')
            self._separation[key] = row
            self._counters['discovered_typed_constraints'] += 1

    def observe_scan(self, result, *, extra_complete, explicit_complete, full_current_complete):
        self._counters['scan_attempts'] += 1
        complete = bool(result.get('complete') and extra_complete and explicit_complete and full_current_complete)
        self._counters['complete_scans' if complete else 'incomplete_scans'] += 1
        if result.get('complete') and not complete:
            raise ValueError('A complete screen cannot omit historical envelope work')
        token = result.get('current_full_point_sha256')
        if complete:
            _digest(token,'actual complete scan point')
            diameter = float(result['diameter_point_lower'])
            height = float(result['current_height'])
            radius = float(result['maximum_radius'])
            if diameter == 2.:
                partner = dict(kind='constant_core_diameter',value=2.)
            elif diameter == 2*abs(height):
                partner = dict(kind='cap_height_diameter',sign=(1 if height >= 0 else -1))
            elif diameter == 2*radius:
                partner = dict(kind='actual_radius_diameter',location=copy.deepcopy(result['farthest']))
            else:
                raise ValueError('The actual lower-diameter branch was not preserved')
            if float(result['reach_physical_g']) > 0:
                # Both physical principal branches and both signed inequalities
                # at the actually separated point remain permanently available.
                for branch in (0,1):
                    for sign in (-1,1):
                        self._separate('reach',result['worst'],partner=partner,branch=branch,sign=sign,token=token)
            amplitude = result['amplitude']
            worsts = amplitude['worst_by_family']
            for family in FAMILIES[1:]:
                if float(amplitude[family]) > 0:
                    location = None if family in ('cap_diameter','height_floor') else worsts[family]['location']
                    self._separate(family,location,token=token)
        scope = dict(schema=SCAN_SCHEMA,source_sha256=sha(__file__),definition=copy.deepcopy(self.definition),definition_identity_sha256=self.identity,
            actual_model_identity_sha256=self.model_identity,current_carrier_sha256=self.current_sha,
            current_full_point_sha256=token,complete=complete,
            current_grid_complete=bool(full_current_complete),historical_extra_grid_complete=bool(extra_complete),
            all_explicit_locations_read=bool(explicit_complete),
            every_implicit_location_all_six_jets_read=bool(full_current_complete and extra_complete),
            both_principal_curvatures_read=complete,both_witness_signs_read=complete,
            historical_address_binding_complete=True,
            implicit_grid=copy.deepcopy(self._fixed['implicit_grid']),
            actual_separation_memory_count=len(self._separation),
            actual_separation_memory_sha256=canonical(self.separation_rows()),
            no_unknown_historical_protected_order_claimed=True,
            continuous_geometry_certified=False)
        return scope

    def separation_rows(self):
        return copy.deepcopy(list(self._separation.values()))

    def rows_built(self, count):
        self._counters['working_row_builds'] += 1
        self._counters['appended_rows_total'] += int(count)

    def metadata(self):
        return copy.deepcopy(dict(self._fixed,actual_separation_memory=dict(
            count=len(self._separation),sha256=canonical(self.separation_rows()),rows=self.separation_rows(),
            eviction_or_working_row_cap=False),counters=self._counters,
            counter_scope='current process; discovered_typed_constraints includes restored permanent entries'))

    def restore(self, value):
        validate_report_metadata(value,model_identity=self.model_identity,carrier_sha256=self.current_sha)
        if value['definition'] != self.definition or value['implicit_grid'] != self._fixed['implicit_grid']:
            raise ValueError('A restart must retain the exact complete material envelope policy and words')
        for item in value['actual_separation_memory']['rows']:
            self._separate(item['family'],item['location'],partner=item['partner'],branch=item['branch'],
                sign=item['sign'],token=item['first_discovered_current_full_point_sha256'])


def _validate_grid(grid):
    if not isinstance(grid,dict):
        raise ValueError('Missing complete material grid coverage')
    for key in ('current_radial_entry_count','current_unique_radial_count','origin_unique_radial_count',
                'extra_historical_radial_count','union_unique_radial_count','angular_count',
                'full_angular_count','unique_implicit_material_locations'):
        value = grid.get(key)
        if isinstance(value,bool) or not isinstance(value,int) or value < 0:
            raise ValueError('Invalid actual grid count '+key)
    if (grid['current_radial_entry_count'] != 7377 or grid['angular_count'] != 513
            or grid['full_angular_count'] != 2048
            or grid['union_unique_radial_count'] != grid['current_unique_radial_count']+grid['extra_historical_radial_count']
            or grid['unique_implicit_material_locations'] != grid['union_unique_radial_count']*513):
        raise ValueError('Incomplete old/current grid union accounting')
    for key in ('actual_phi_sha256','union_radial_words_sha256','extra_radial_words_sha256'):
        _digest(grid.get(key),key)


def validate_scan_metadata(value, *, model_identity, carrier_sha256):
    if (not isinstance(value,dict) or value.get('schema') != SCAN_SCHEMA
            or value.get('source_sha256') != sha(__file__)
            or value.get('actual_model_identity_sha256') != model_identity
            or value.get('current_carrier_sha256') != carrier_sha256
            or value.get('historical_address_binding_complete') is not True
            or value.get('continuous_geometry_certified') is not False):
        raise ValueError('The actual scan is not bound to this complete envelope consumer')
    _digest(value.get('definition_identity_sha256'),'envelope policy')
    policy = value.get('definition',{})
    if (policy != definition(policy.get('additional_current_near_active_rows',-1))
            or canonical(policy) != value['definition_identity_sha256']):
        raise ValueError('The actual complete scan policy changed')
    _validate_grid(value.get('implicit_grid'))
    if not isinstance(value.get('complete'),bool):
        raise ValueError('The actual envelope scan completion must be explicit')
    flags = ('current_grid_complete','historical_extra_grid_complete','all_explicit_locations_read',
        'every_implicit_location_all_six_jets_read','both_principal_curvatures_read','both_witness_signs_read')
    if any(not isinstance(value.get(key),bool) for key in flags):
        raise ValueError('Do not invent missing envelope coverage flags')
    if value['complete']:
        _digest(value.get('current_full_point_sha256'),'complete envelope scan point')
        if not all(value[key] for key in flags):
            raise ValueError('A complete scan omitted some permanent nonlinear constraints')
    _digest(value.get('actual_separation_memory_sha256'),'separation memory')
    if not isinstance(value.get('actual_separation_memory_count'),int) or value['actual_separation_memory_count'] < 0:
        raise ValueError('Invalid actual separation memory count')
    return copy.deepcopy(value)


def validate_report_metadata(value, *, model_identity, carrier_sha256):
    if (not isinstance(value,dict) or value.get('schema') != SCHEMA
            or value.get('source_sha256') != sha(__file__)
            or value.get('actual_model_identity_sha256') != model_identity
            or value.get('current_carrier_sha256') != carrier_sha256
            or value.get('continuous_geometry_certified') is not False
            or value.get('continuous_metric_certified') is not False):
        raise ValueError('Use the complete actual new-envelope report')
    policy = value.get('definition',{})
    if policy != definition(policy.get('additional_current_near_active_rows',-1)):
        raise ValueError('The complete declared envelope policy changed')
    if canonical(policy) != value.get('definition_identity_sha256'):
        raise ValueError('Envelope policy identity mismatch')
    _validate_grid(value.get('implicit_grid'))
    bound = value.get('historical_address_binding',{})
    origin = bound.get('origin_carrier',{}).get('record',{})
    current = bound.get('current_carrier',{}).get('record',{})
    p0 = bound.get('original_p0',{})
    if (bound.get('complete') is not True or bound.get('old_and_current_entire_arrays_actually_read') is not True
            or origin.get('sha256') != ORIGIN_CARRIER_SHA or origin.get('bytes') != ORIGIN_CARRIER_BYTES
            or current.get('sha256') != carrier_sha256
            or p0.get('original_p0_fingerprints') != ORIGIN_P0
            or p0.get('original_p0_combined_sha256') != canonical(ORIGIN_P0)
            or p0.get('all_eleven_complete_payloads_consumed') is not True
            or p0.get('actual_old_carrier_used_for_indexed_points') is not True):
        raise ValueError('Original complete historical input and current array binding are unpaid')
    path_binding=bound.get('actual_path_binding',{})
    if path_binding.get('identical_whole_file_directly_read') is True:
        raise ValueError('A direct historical carrier is not the independently frozen new target')
    verified_path_binding=validate_public_binding(path_binding,current_input=current)
    independent_target_validation=_validate_independent_target_binding(
        verified_path_binding,current_carrier=current)
    if (value.get('independent_fixed_target_definition_identity_sha256')
                !=independent_target_validation['fixed_target_definition_identity_sha256']
            or value.get('same_original_fixed_chart') is not True
            or value.get('same_mathematical_g_claimed') is not True):
        raise ValueError('The report does not retain its complete independent fixed target')
    memory = value.get('actual_separation_memory',{})
    rows = memory.get('rows')
    if (not isinstance(rows,list) or memory.get('count') != len(rows)
            or memory.get('sha256') != canonical(rows) or memory.get('eviction_or_working_row_cap') is not False):
        raise ValueError('The entire uncapped typed memory must be retained')
    for row in rows:
        if row.get('family') not in FAMILIES:
            raise ValueError('Unknown retained typed family')
        if row.get('location') is not None:
            _point_key(row['location'])
        if row['family'] == 'reach':
            partner = row.get('partner',{})
            if (row.get('location') is None or row.get('branch') not in (0,1)
                    or isinstance(row.get('branch'),bool) or row.get('sign') not in (-1,1)
                    or isinstance(row.get('sign'),bool) or not isinstance(partner,dict)):
                raise ValueError('Incomplete retained signed curvature branch')
            kind = partner.get('kind')
            if kind == 'actual_radius_diameter':
                _point_key(partner.get('location',{}))
            elif kind == 'cap_height_diameter':
                if partner.get('sign') not in (-1,1) or isinstance(partner.get('sign'),bool):
                    raise ValueError('Retain the actual signed cap diameter branch')
            elif kind == 'constant_core_diameter':
                if partner.get('value') != 2.:
                    raise ValueError('Changed fixed-core diameter lower bound')
            else:
                raise ValueError('Unknown actual diameter partner')
        elif (row.get('partner') is not None or row.get('branch') is not None or row.get('sign') is not None
                or (row['family'] in ('cap_diameter','height_floor')) != (row.get('location') is None)):
            raise ValueError('The retained amplitude family/point contract changed')
        _digest(row.get('first_discovered_current_full_point_sha256'),'typed memory source point')
    if value.get('unknown_old_individual_protected_labels_or_order_reconstructed') is not False:
        raise ValueError('Unknown historical labels must not be fabricated')
    counters = value.get('counters',{})
    for key in ('scan_attempts','complete_scans','incomplete_scans','discovered_typed_constraints',
                'working_row_builds','appended_rows_total'):
        if isinstance(counters.get(key),bool) or not isinstance(counters.get(key),int) or counters[key]<0:
            raise ValueError('Missing actual envelope counter '+key)
    if counters['scan_attempts'] != counters['complete_scans']+counters['incomplete_scans']:
        raise ValueError('Actual complete/partial envelope read accounting changed')
    return dict(schema=SCHEMA,source_sha256=sha(__file__),definition_identity_sha256=canonical(policy),
        actual_model_identity_sha256=model_identity,current_carrier_sha256=carrier_sha256,
        historical_origin_carrier_sha256=ORIGIN_CARRIER_SHA,
        implicit_grid=copy.deepcopy(value['implicit_grid']),
        original_p0_fingerprints=copy.deepcopy(ORIGIN_P0),
        actual_separation_memory_count=len(rows),actual_separation_memory_sha256=canonical(rows),
        independent_fixed_target_validation=independent_target_validation,
        counters=copy.deepcopy(counters),all_old_current_locations_in_permanent_nonlinear_responsibility=True,
        unknown_historical_protected_order_reconstructed=False,continuous_geometry_certified=False)
