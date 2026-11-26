#!/usr/bin/env python3
"""Fingerprint complete existing SO3 history with the exact published walker.

This is a pure report/address reader. It reads JSON and the two existing
observation-coordinate NPY vectors through the original stdlib implementation.
It reads the existing first 606 checkpoint words for the full initial-point
hash, without evaluating that field. It never imports a scientific model,
calls F/J/root/scan, or publishes address/field arrays. Public Actions only. A matching digest compares
the actual consumed location words; it does not prove equality of fields,
targets, geometry values or continuous certificates.
"""
import argparse
import ast
import copy
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import struct
import zipfile

SCHEMA = 'complete-existing-SO3-history-and-initial-point-fingerprints-v2'
TOPIC = 'topics/visible-flex-larger-amplitude'
HISTORY_PATH = 'scripts/resume_20261120/launch_refinement_from_full_report.py'
HISTORY_SHA = '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'
PREPARATION_PATH = 'scripts/resume_20261126/so3_axisymmetric_reference.py'
PREPARATION_SHA = '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'
PREPARATION_SCHEMA = 'R690-independent-axisymmetric-SO3-preparation-v1'
LOCATION_SCHEMA = 'independent-axisymmetric-SO3-literal-position-input-v1'
INITIAL_DRIVER_SHA = '606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9'
INITIAL_MERIDIAN_PATH = 'scripts/resume_20261126/so3_axisymmetric_meridian_operator.py'
INITIAL_MERIDIAN_SHA = '7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf'
DRIVERS = {
    '606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9':
        'fullclosed_axisymmetric_so3_qp.py',
    '359ffc94df1b33485c2cda4de0f5662ef7bc802c588f583a023fcd5723a7872d':
        'fullclosed_axisymmetric_so3_separation_soc.py',
    '7b7cc0c9b27a0339debab0319c6854323dfc6c21f3e92c64946cbffc70824c7d':
        'fullclosed_angular_unit_qp.py',
    '9649ed99b614c468258646145948d7c06feb356c72806c73727728ea498ed88e':
        'fullclosed_zero_moment_continuation_so3_qp.py',
    '34c9273aad6ccc3299c8b64ac250a37b3ae758eec34945ef00a4b14a3acaf1b3':
        'fullclosed_zero_moment_height_so3_qp.py',
    '5134d34d4f4393fc57d86eed329bd107b631b693668d1d04d602af5f286dc3f5':
        'fullclosed_zero_gamma_kkt_so3_qp.py',
}


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Read actual existing coordinate arrays only in the public Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def read_json(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ValueError('Every manifest or report must be a complete JSON object')
    return value, dict(path=str(path), sha256=hashlib.sha256(raw).hexdigest(),
        bytes=len(raw))


def literal_assignments(path):
    """Read literal declarations, never execute a scientific source module."""
    tree = ast.parse(Path(path).read_text())
    result = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and target.id in (
                    'SCHEMA', 'PREPARATION_SCHEMA', 'SOURCE_PINS'):
                if target.id in result:
                    raise ValueError('Ambiguous repeated source declaration')
                result[target.id] = ast.literal_eval(node.value)
    return result


def checked_source(topic, relative, expected, cache):
    path = (topic / relative).resolve()
    if topic.resolve() not in path.parents:
        raise ValueError('A source role escaped the declared public topic')
    actual = sha(path)
    if actual != expected:
        raise ValueError('Changed complete published source: '+relative)
    cache[relative] = dict(repo_relative_path=TOPIC+'/'+relative,
        sha256=actual, bytes=path.stat().st_size)
    return path


def checked_roles(topic, declarations, report, cache):
    pins = declarations.get('SOURCE_PINS')
    if not isinstance(pins, dict) or not pins:
        raise ValueError('Require the complete literal source-role declaration')
    expected = {}
    for role, pair in pins.items():
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            raise ValueError('Malformed complete source-role declaration')
        relative, digest = pair
        checked_source(topic, relative, digest, cache)
        expected[role] = digest
    if report.get('source_sha256_by_role') != expected:
        raise ValueError('The actual report differs from its complete source-role map')


def bind_preparation(args, topic, cache):
    path = checked_source(topic, PREPARATION_PATH, PREPARATION_SHA, cache)
    declarations = literal_assignments(path)
    report, evidence = read_json(args.preparation_report)
    if (report.get('schema') != PREPARATION_SCHEMA
            or declarations.get('PREPARATION_SCHEMA') != PREPARATION_SCHEMA
            or report.get('source_sha256') != PREPARATION_SHA
            or report.get('complete') is not True):
        raise ValueError('Need the actual completed independent reference preparation')
    checked_roles(topic, declarations, report, cache)
    if (report.get('M') != 160 or report.get('J') != 923
            or report.get('P') != 7377 or report.get('N') != 2048):
        raise ValueError('Keep the complete original reference observation domain')
    reference, carrier = record(args.reference_bundle), record(args.carrier)
    inputs = report['input_for_solver']
    if (inputs['reference_bundle']['sha256'] != reference['sha256']
            or inputs['carrier']['sha256'] != carrier['sha256']):
        raise ValueError('Actual reference or carrier bytes changed')
    definition = report['reference_definition']
    profile = report['fixed_scalar_metric_identity_sha256']
    if (canonical(definition) != report['reference_model_identity_sha256']
            or definition['source_sha256'] != PREPARATION_SHA
            or definition['fixed_scalar_metric_identity_sha256'] != profile
            or canonical(definition['fixed_scalar_profile_definition']) != profile
            or definition['observation_carrier_sha256'] != carrier['sha256']
            or definition['M'] != report['M'] or definition['J'] != report['J']):
        raise ValueError('The exact actual reference/profile definition is inconsistent')
    if (report.get('historical_nonlinear_directions_replayed') is not False
            or report.get('optimized_old_q_field_read_as_T0') is not False):
        raise ValueError('Require the actual complete independent preparation')
    return report, evidence, reference, carrier


def indexed_grid(value):
    # Literal function body of all_locations in complete driver 606e.
    if isinstance(value, dict):
        if 'stage' in value and 'angle' in value and 'phi' not in value:
            return True
        return any(indexed_grid(item) for item in value.values())
    if isinstance(value, list):
        if value and isinstance(value[0], str) and value[0] in ('grid', 'grid_radius'):
            return True
        return any(indexed_grid(item) for item in value)
    return False


def bind_manifest(path, payload, evidence, prep, prep_record, reference, carrier,
                  topic, cache):
    declared = payload.get('carrier_sha256', payload.get('observation_carrier_sha256'))
    if declared != carrier['sha256']:
        raise ValueError('Every supplied history must bind the same actual carrier')
    if indexed_grid(payload):
        value = payload.get('N', payload.get('full_angles', payload.get('full_N')))
        if value is None or int(value) != prep['N']:
            raise ValueError('Never reinterpret tagged grid indices under another N')
    if payload.get('schema') == LOCATION_SCHEMA:
        if (evidence['sha256'] != prep['new_locations']['sha256']
                or payload.get('reference_bundle_sha256') != reference['sha256']
                or payload.get('N') != prep['N'] or payload.get('J') != prep['J']
                or payload.get('P') != prep['P']):
            raise ValueError('Use the exact complete prepared location manifest')
        return dict(kind='complete-prepared-location-manifest',
            schema=payload['schema'], source_sha256=PREPARATION_SHA,
            model_identity_sha256=prep['reference_model_identity_sha256'],
            fixed_scalar_metric_identity_sha256=prep['fixed_scalar_metric_identity_sha256'],
            scientific_report_complete=None, final_bundle_sha256=None,
            numerical_values_or_certificates_inherited=False)
    source = payload.get('source_sha256')
    if source not in DRIVERS:
        raise ValueError('No complete published driver binding for supplied history')
    relative = 'scripts/resume_20261126/'+DRIVERS[source]
    source_path = checked_source(topic, relative, source, cache)
    declarations = literal_assignments(source_path)
    if payload.get('schema') != declarations.get('SCHEMA'):
        raise ValueError('Actual complete report schema/source pair changed')
    checked_roles(topic, declarations, payload, cache)
    if (payload.get('M') != prep['M'] or payload.get('J') != prep['J']
            or payload.get('N') != prep['N']
            or payload.get('all_full_rows') != 3*prep['P']*prep['N']
            or payload.get('bundle_sha256') != reference['sha256']
            or payload.get('independent_preparation_report',{}).get('sha256')
                != prep_record['sha256']):
        raise ValueError('Actual history changed reference or complete observation domain')
    profile = payload['fixed_scalar_metric']
    if (profile.get('identity_sha256') != prep['fixed_scalar_metric_identity_sha256']
            or profile.get('exact_profile_definition') !=
                prep['reference_definition']['fixed_scalar_profile_definition']
            or profile.get('target_fixed_before_first_direction') is not True
            or profile.get('target_recomputed_from_current_field') is not False):
        raise ValueError('Actual history is not bound to this same fixed profile')
    binding = payload['independent_reference_binding']
    if (binding.get('reference_model_identity_sha256') != prep['reference_model_identity_sha256']
            or binding.get('fixed_scalar_metric_identity_sha256') != profile['identity_sha256']
            or binding.get('new_locations',{}).get('sha256') != prep['new_locations']['sha256']):
        raise ValueError('Actual complete history lost its independent reference binding')
    representation = payload['representation']
    if canonical(representation) != payload['model_identity_sha256']:
        raise ValueError('Actual complete scientific representation identity changed')
    # Failure reports are intentional input: they can contain selected or trial
    # addresses even when they never produce a final field. No success is invented.
    if not isinstance(payload.get('complete'), bool):
        raise ValueError('An actual scientific report must explicitly declare complete')
    return dict(kind='complete-actual-scientific-report', schema=payload['schema'],
        source_sha256=source, source_commit=payload.get('source_commit'),
        model_identity_sha256=payload['model_identity_sha256'],
        fixed_scalar_metric_identity_sha256=profile['identity_sha256'],
        scientific_report_complete=payload['complete'],
        final_bundle_sha256=payload.get('final_bundle_sha256'),
        numerical_values_or_certificates_inherited=False)


def load_walker(path):
    name = '_complete_published_SO3_location_fingerprint_walker'
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    for method in ('walk','put','grid','angle','tagged','resolve_grid','arrays'):
        actual = Path(getattr(module.Locations, method).__code__.co_filename).resolve()
        if actual != path.resolve() or sha(actual) != HISTORY_SHA:
            raise ValueError('Use the actual complete published walker implementation')
    if sha(Path(module.npy_vector.__code__.co_filename)) != HISTORY_SHA:
        raise ValueError('The exact stdlib coordinate reader changed')
    return module


def fingerprint(locations):
    arrays = locations.arrays()
    values = {}
    for key in ('curvature_points','radius_points','protected_curvature_points'):
        words = []
        for cell, u, phi in arrays[key]:
            if (isinstance(cell, bool) or int(cell) != cell
                    or not math.isfinite(float(u)) or not math.isfinite(float(phi))):
                raise ValueError('Invalid consumed location word')
            words.append([int(cell), float(u).hex(), float(phi).hex()])
        words.sort()
        values[key] = dict(count=len(words), sha256=canonical(words))
    return dict(curvature_count=values['curvature_points']['count'],
        radius_count=values['radius_points']['count'],
        protected_curvature_count=values['protected_curvature_points']['count'],
        curvature_sha256=values['curvature_points']['sha256'],
        radius_sha256=values['radius_points']['sha256'],
        protected_curvature_sha256=values['protected_curvature_points']['sha256'],
        combined_sha256=canonical(values),
        pending_grid_count=len(locations.pending),
        recorded_position_occurrences=locations.occurrences,
        canonical_word_encoding='sorted [integer cell, float(u).hex(), float(phi).hex()] JSON',
        dictionary_semantics='unchanged 4d9 numeric tuple identity; surviving signed-zero words retained',
        address_arrays_published=False)


def npy_member(archive, name):
    """Read a literal non-object NPY member; no scientific array library."""
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
    header = ast.literal_eval(raw[start:end].decode(
        'utf-8' if version == (3, 0) else 'latin1'))
    if (not isinstance(header, dict)
            or set(header) != {'descr', 'fortran_order', 'shape'}
            or header['fortran_order'] is not False
            or not isinstance(header['shape'], tuple)
            or any(isinstance(v, bool) or not isinstance(v, int) or v < 0
                for v in header['shape'])):
        raise ValueError('Require the actual complete C-order literal array')
    descriptor, shape, data = header['descr'], header['shape'], raw[end:]
    if descriptor in ('<f8', '<i8'):
        width = 8
    elif (isinstance(descriptor, str) and descriptor.startswith('<U')
            and descriptor[2:].isdigit()):
        width = 4*int(descriptor[2:])
    else:
        raise ValueError('No object arrays or changed actual binary64 dtype')
    count = math.prod(shape)
    if len(data) != width*count:
        raise ValueError('The entire literal NPY shape and bytes must agree')
    return descriptor, shape, data


def float_member(archive, name, shape):
    descriptor, actual_shape, data = npy_member(archive, name)
    if descriptor != '<f8' or actual_shape != tuple(shape):
        raise ValueError('The exact bound float64 array changed: '+name)
    if any(not math.isfinite(v) for (v,) in struct.iter_unpack('<d', data)):
        raise ValueError('The saved complete point must contain finite words')
    return data


def text_member(archive, name):
    descriptor, shape, data = npy_member(archive, name)
    if shape != () or not descriptor.startswith('<U'):
        raise ValueError('Require an actual scalar Unicode NPY member')
    return data.decode('utf-32-le').rstrip('\0')


def integer_member(archive, name):
    descriptor, shape, data = npy_member(archive, name)
    if descriptor != '<i8' or shape != ():
        raise ValueError('Require the actual scalar int64 member')
    return struct.unpack('<q', data)[0]


def exact_array_sha(shape, chunks):
    # Literal 7f26 array_sha convention on the bound little-endian Actions
    # carrier: dtype string, JSON shape with ordinary spacing, then all bytes.
    value = hashlib.sha256(b'float64')
    value.update(json.dumps(list(shape)).encode())
    for chunk in chunks:
        value.update(chunk)
    return value.hexdigest()


def read_initial_point(args, prep, reference, carrier, topic, sources,
                       complete_inputs):
    report, report_record = read_json(args.initial_point_report)
    if report_record['sha256'] not in complete_inputs:
        raise ValueError('The initial scientific report must be a supplied complete manifest')
    if (report.get('source_sha256') != INITIAL_DRIVER_SHA
            or report.get('restart') is not None
            or report.get('new_unit_meridian_seed_changes_physical_field') is not True
            or report.get('complete') is not True):
        raise ValueError('Read the actual independent first 606 point, not a restarted point')
    # bind_manifest already checked this exact full report and every source
    # role in the manifest walk; retain a direct explicit initial-source guard.
    meridian_path = checked_source(topic, INITIAL_MERIDIAN_PATH,
        INITIAL_MERIDIAN_SHA, sources)
    meridian_schema = literal_assignments(meridian_path)['SCHEMA']
    model = report['representation']
    if (model['source_sha256'] != INITIAL_MERIDIAN_SHA
            or model['schema'] != meridian_schema
            or model['complete_axisymmetric_reference_model'] != prep['reference_definition']
            or model['initial_reference_bundle_sha256'] != reference['sha256']
            or model['fixed_scalar_metric_identity_sha256'] != prep['fixed_scalar_metric_identity_sha256']
            or report['observation_carrier_sha256'] != carrier['sha256']):
        raise ValueError('The initial complete point changed its actual full model')
    bundle = record(args.initial_point_bundle)
    declared_bundle = report['initial_new_bundle']
    if (bundle['sha256'] != declared_bundle['sha256']
            or bundle['bytes'] != declared_bundle['bytes']):
        raise ValueError('Use the existing actual initial-new-field bundle bytes')
    M, J, K = prep['M'], prep['J'], 3
    n = 3*M+2
    zero_slots = [0, 3*(J-1), 3*(J-1)+1]
    if model['omega_basis']['fixed_zero_radial_slots'] != zero_slots:
        raise ValueError('The complete 7f radial free mask changed')
    with zipfile.ZipFile(args.reference_bundle) as reference_archive:
        reference_model = json.loads(text_member(reference_archive, 'reference_model_json'))
        if (reference_model != prep['reference_definition']
                or text_member(reference_archive, 'reference_model_identity_sha256')
                    != prep['reference_model_identity_sha256']):
            raise ValueError('The actual reference bundle lost its complete definition')
        reference_core = float_member(reference_archive, 'initial_core', (M,))
        reference_height = float_member(reference_archive, 'initial_height', ())
        reference_mesh = float_member(reference_archive, 'mesh', (J,))
    with zipfile.ZipFile(args.initial_point_bundle) as archive:
        if (text_member(archive, 'schema') != meridian_schema
                or text_member(archive, 'so3_model_identity_sha256') != report['model_identity_sha256']
                or json.loads(text_member(archive, 'so3_model_json')) != model
                or text_member(archive, 'initial_reference_bundle_sha256') != reference['sha256']
                or text_member(archive, 'fixed_scalar_metric_identity_sha256')
                    != prep['fixed_scalar_metric_identity_sha256']
                or integer_member(archive, 'working_integration_order')
                    != report['working_evaluation']['integration_order']
                or integer_member(archive, 'working_full_angles') != prep['N']):
            raise ValueError('The complete actual initial checkpoint model or working settings changed')
        core = float_member(archive, 'core', (M,))
        omega = float_member(archive, 'omega_jets', (J, 3, n))
        height = float_member(archive, 'Hcap', ())
        fixed_chart = float_member(archive, 'fixed_chart_core', (M,))
        mesh = float_member(archive, 'mesh', (J,))
    if (core != reference_core or fixed_chart != reference_core
            or height != reference_height or mesh != reference_mesh
            or any(omega)):
        raise ValueError('Saved first point is not the complete actual q.initial word vector')
    core_sha = exact_array_sha((M,), [core])
    mesh_sha = exact_array_sha((J,), [mesh])
    if (core_sha != model['fixed_chart_core_sha256']
            or core_sha != prep['reference_definition']['fixed_chart_core_sha256']
            or mesh_sha != model['mesh_sha256']
            or mesh_sha != prep['reference_definition']['mesh_sha256']):
        raise ValueError('Complete literal core/chart/mesh array identities changed')
    first3 = [struct.unpack('<d', core[8*i:8*(i+1)])[0].hex() for i in range(K)]
    if first3 != model['fixed_core_first3']:
        raise ValueError('Retain all three original fixed core words')
    radial_free = [i for i in range(3*J) if i not in zero_slots]
    free_count = (M-K)+len(radial_free)*n+1
    if free_count != report['original_variables']:
        raise ValueError('Do not omit any complete free coordinate')
    row_bytes = n*8
    point_chunks = [core[8*K:]]+[omega[i*row_bytes:(i+1)*row_bytes]
        for i in radial_free]+[height]
    height_value = struct.unpack('<d', height)[0]
    return dict(schema='actual-existing-606-initial-complete-point-bytes-v1',
        report=report_record, bundle=bundle,
        source_driver_sha256=INITIAL_DRIVER_SHA,
        source_meridian_sha256=INITIAL_MERIDIAN_SHA,
        model_identity_sha256=report['model_identity_sha256'],
        fixed_scalar_metric_identity_sha256=prep['fixed_scalar_metric_identity_sha256'],
        complete_point_array_sha256=exact_array_sha((free_count,), point_chunks),
        original_variables=free_count, free_core_variables=M-K,
        free_rotation_variables=len(radial_free)*n, free_height_variables=1,
        core_array_sha256=core_sha, fixed_chart_core_array_sha256=core_sha,
        omega_full_array_sha256=exact_array_sha((J, 3, n), [omega]),
        mesh_array_sha256=mesh_sha, height_binary64_hex=height_value.hex(),
        exact_point_encoding='7f26: float64 dtype + JSON [all free variables] + core[3:], full radial-free omega rows, H bytes',
        actual_existing_initial_bundle_read=True,
        actual_existing_reference_core_height_mesh_read=True,
        saved_initial_core_equals_fixed_chart_by_bytes=True,
        saved_initial_omega_all_positive_zero_words=True,
        saved_initial_height_equals_actual_prepared_height_by_bytes=True,
        scientific_model_imported=False, initial_field_recomputed=False,
        new_geometry_or_metric_certificate_claimed=False,
        same_final_point_claimed=False,
        original_scalar_parameters_identity_sha256=prep['reference_definition'][
            'original_scalar_parameters_identity_sha256'],
        original_warm_bundle_sha256=prep['reference_definition']['original_warm_bundle_sha256'],
        exact_scalar_profile_definition_sha256=canonical(
            prep['reference_definition']['fixed_scalar_profile_definition']))



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo','preparation-report','reference-bundle','carrier','initial-point-report',
                'initial-point-bundle','output'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--manifest', type=Path, action='append', required=True)
    args = parser.parse_args()
    require_actions()
    args.repo = args.repo.resolve()
    args.output = args.output.resolve()
    if args.output.exists() or args.output == args.repo or args.repo in args.output.parents:
        raise ValueError('Use one fresh pure output outside the repository')
    topic = args.repo/TOPIC
    sources = {}
    prep, prep_record, reference, carrier = bind_preparation(args, topic, sources)
    walker_path = checked_source(topic, HISTORY_PATH, HISTORY_SHA, sources)
    history = load_walker(walker_path)
    union = history.Locations(prep['J'], prep['P'], prep['N'])
    entries, all_records = [], [prep_record, reference, carrier]
    prepared_supplied = False
    for index, path in enumerate(args.manifest):
        payload, evidence = read_json(path)
        binding = bind_manifest(path, payload, evidence, prep, prep_record,
            reference, carrier, topic, sources)
        prepared_supplied |= evidence['sha256'] == prep['new_locations']['sha256']
        individual = history.Locations(prep['J'], prep['P'], prep['N'])
        origin = ('explicit_complete_history', path.name)
        individual.walk(payload, path=origin)
        resolved = individual.resolve_grid(args.carrier)
        union.walk(payload, path=origin)
        prefix = copy.deepcopy(union)
        prefix_resolved = prefix.resolve_grid(args.carrier)
        entries.append(dict(index=index, label=path.parent.name+'/'+path.name,
            input=evidence, binding=binding,
            resolved_grid_positions=resolved,
            prefix_resolved_grid_positions=prefix_resolved,
            consumed=fingerprint(individual), prefix_union=fingerprint(prefix)))
        all_records.append(evidence)
    if not prepared_supplied:
        raise ValueError('Retain the entire prepared history as an explicit manifest')
    initial_point = read_initial_point(args, prep, reference, carrier, topic, sources,
        {entry['input']['sha256'] for entry in entries})
    all_records.extend((initial_point['report'], initial_point['bundle']))
    exact_resolved = union.resolve_grid(args.carrier)
    final = fingerprint(union)
    if not final['curvature_count'] or not final['radius_count']:
        raise ValueError('The complete supplied history union cannot be empty')
    for old in all_records:
        if sha(old['path']) != old['sha256']:
            raise ValueError('An actual input changed during the pure read')
    result = dict(schema=SCHEMA, source_sha256=sha(__file__),
        execution=dict(repository=os.environ['GITHUB_REPOSITORY'],
            run_id=os.environ.get('GITHUB_RUN_ID'),
            run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT')),
        complete=True, preparation_report=prep_record,
        actual_reference=reference, actual_carrier=carrier,
        M=prep['M'], J=prep['J'], P=prep['P'], N=prep['N'],
        reference_model_identity_sha256=prep['reference_model_identity_sha256'],
        fixed_scalar_metric_identity_sha256=prep['fixed_scalar_metric_identity_sha256'],
        exact_fixed_profile_definition_sha256=canonical(
            prep['reference_definition']['fixed_scalar_profile_definition']),
        fixed_chart_core_sha256=prep['reference_definition']['fixed_chart_core_sha256'],
        numerical_mesh_array_sha256=prep['reference_definition']['mesh_sha256'],
        original_scalar_parameters_identity_sha256=prep['reference_definition'][
            'original_scalar_parameters_identity_sha256'],
        original_warm_bundle_sha256=prep['reference_definition']['original_warm_bundle_sha256'],
        initial_complete_point=initial_point,
        initial_prepared_history_sha256=prep['new_locations']['sha256'],
        actual_complete_sources=sources, entries=entries,
        exact_solver_order_union=final,
        exact_solver_order_resolved_grid_positions=exact_resolved,
        each_prefix_walks_all_inputs_before_one_grid_resolution=True,
        complete_scope='Every supplied complete report/manifest through unchanged 4d9 walker',
        unspecified_or_future_reports_claimed_included=False,
        final_memory_alone_substituted_for_complete_report=False,
        field_arrays_read_for_word_hash_only=True,
        field_values_recomputed=False, scientific_model_modules_imported=False,
        existing_coordinate_arrays_read=['observation_cells','observation_u'],
        field_evaluations=0, J_evaluations=0, Jtranspose_evaluations=0,
        root_solves=0, geometry_scans=0, QP_solves=0,
        raw_location_tables_written=False, raw_report_contents_written=False,
        matching_address_hash_proves_same_field=False,
        matching_address_hash_proves_same_target=False,
        matching_address_hash_proves_continuous_certificate=False,
        comparison_scope='Actual consumed address words/protected roles and the actual first full free-point bytes; model/profile identities are reported separately; equal bytes alone do not certify a field')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_name(args.output.name+'.partial')
    temporary.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    temporary.replace(args.output)
    print(json.dumps(dict(event='complete_history_fingerprints_read',
        output=record(args.output), input_count=len(entries),
        union=final, source_sha256=result['source_sha256'],
        field_evaluations=0, J_evaluations=0, root_solves=0),
        separators=(',', ':'), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
