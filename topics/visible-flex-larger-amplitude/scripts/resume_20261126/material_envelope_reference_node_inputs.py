#!/usr/bin/env python3
"""Source-closed complete fixed-reference node inputs for the material envelope.

This restores only actual immutable mean/radial-plan inputs and calls the
unchanged provider to obtain NEW actual four-jet words. It does not assert
that unrecorded old outer-field cache words were immutable or identical.
No outer F/J/normal root or new mean root is computed by this module.
All actual array reads and provider evaluation require public Actions.
"""
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
from types import SimpleNamespace

SCHEMA = 'complete-material-envelope-immutable-reference-node-inputs-v1'
PLAN_SCHEMA = 'complete-material-envelope-reference-node-query-plan-v1'
WORK_SCHEMA = 'actual-fixed-reference-four-jet-node-packet-v1'
TOPIC = 'topics/visible-flex-larger-amplitude'
PINS = {
    'schedule': ('all_recorded_material_envelope_seed_fees.py',
        '3feff893d09257748d153f0423e75d64eafe75777933ba85ee67611ce61cad6d'),
    'accurate': ('reference_centred_c1_material_envelope_accurate_mean_residuals.py',
        'ce686a593cd81167167adfda966b423e2d95f1c9ce708f5d7252089baed24f1d'),
    'fees': ('reference_centred_c1_material_envelope_seed_angular_jet_error_bounds.py',
        '2859943d522cd764b686112acd0acdb065dc6a893625f4a8e237641caf041d36'),
    'provider': ('supported_smooth_triangle_meridian_reference.py',
        '0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b'),
    'mean_kernel': ('supported_smooth_triangle_seed_mean_jets.py',
        'f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917'),
    'reference': ('so3_axisymmetric_reference.py',
        '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'),
    'memory': ('complete_material_envelope_memory.py',
        'c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152'),
    'history': ('../resume_20261120/launch_refinement_from_full_report.py',
        '4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60'),
}
VECTOR_KEYS = ('v','v_phi','v_phiphi','d','d_phi','d_phiphi','w','w_phi','w_phiphi')
SCALAR_KEYS = ('lambda','lambda_phi','lambda_phiphi','profile_moment',
    'profile_moment_first_derivative','profile_moment_second_derivative')
FIELD_MAP = {'T':'T0','Tp':'T0_phi','Tpp':'T0_phiphi','Ts':'T0_s'}
INPUT_KEYS = ('reference_bundle','carrier','node_report','scalar_input','preparation_report')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Complete actual reference nodes require public repository Actions')


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


def capture(path, expected=None):
    path = Path(path).resolve()
    data = path.read_bytes()
    record = dict(path=str(path),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))
    if expected is not None and record != expected:
        raise ValueError('A complete immutable JSON input changed: '+str(path))
    value = json.loads(data)
    if file_record(path) != record:
        raise ValueError('The captured actual bytes changed during parsing')
    return value, record


def load(name, path, digest):
    if sha(path) != digest:
        raise ValueError('The complete node source changed: '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    if sha(module.__file__) != digest:
        raise ValueError('The actual loaded complete source changed')
    return module


def array_sha(value):
    import numpy as np
    a = np.ascontiguousarray(value)
    h = hashlib.sha256()
    h.update(str(a.dtype).encode())
    h.update(json.dumps(list(a.shape)).encode())
    h.update(a.tobytes())
    return h.hexdigest()


def array_record(value):
    return dict(dtype=str(value.dtype),shape=list(value.shape),sha256=array_sha(value))


def readonly(value):
    import numpy as np
    result = np.array(value,copy=True)
    result.setflags(write=False)
    return result


def write_json(path, value, *, fresh=False):
    path = Path(path)
    if fresh and path.exists():
        raise FileExistsError('Do not overwrite an immutable node record: '+str(path))
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary = path.with_name(path.name+'.partial')
    if temporary.exists():
        raise FileExistsError('An uncommitted node output requires explicit recovery: '+str(temporary))
    temporary.write_text(json.dumps(value,sort_keys=True,indent=2,allow_nan=False)+'\n')
    temporary.replace(path)


def save_arrays(path, arrays):
    import numpy as np
    path = Path(path)
    if path.exists() or path.with_name(path.name+'.partial').exists():
        raise FileExistsError('Use a fresh immutable node-array packet')
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary = path.with_name(path.name+'.partial')
    with temporary.open('xb') as stream:
        np.savez(stream,**arrays)
    temporary.replace(path)
    return file_record(path)


def checked_arrays(record):
    import numpy as np
    if file_record(record['path']) != record:
        raise ValueError('The complete actual array input is absent or changed')
    with np.load(record['path'],allow_pickle=False) as data:
        arrays = {key:readonly(data[key]) for key in data.files}
    if file_record(record['path']) != record:
        raise ValueError('The complete array input changed during its actual read')
    return arrays


def finite_array(value, *, shape=None, integer=False):
    import numpy as np
    expected = np.dtype('int64' if integer else 'float64')
    if (value.dtype != expected or (shape is not None and value.shape != shape)
            or not np.isfinite(value).all()):
        raise ValueError('Keep the complete finite actual array dtype and shape')
    return value


def _key(location):
    cell,u,phi = location
    if (isinstance(cell,bool) or int(cell) != cell or not 0 <= int(cell) < 922
            or not math.isfinite(float(u)) or not 0 <= float(u) <= 1
            or not math.isfinite(float(phi))):
        raise ValueError('Invalid literal original material address')
    return int(cell),float(u).hex(),float(phi).hex()


class BoundReferenceInputs:
    """Bind the full actual report and restore only its immutable seed inputs."""
    def __init__(self, args):
        require_actions()
        import numpy as np
        self.args = args
        self.repo = Path(args.repo).resolve()
        directory = self.repo/TOPIC/'scripts/resume_20261126'
        self.paths = {key:directory/name for key,(name,digest) in PINS.items()}
        self.modules = {key:load('_immutable_seed_nodes_'+key,self.paths[key],digest)
            for key,(name,digest) in PINS.items()}
        scheduler = self.modules['schedule']
        schedule_args = SimpleNamespace(**vars(args))
        schedule_args.per_batch_seconds = 60.
        schedule_args.width_goal = '1/100000000'
        paths = scheduler.source_paths(self.repo)
        self.recorded, self.input_paths = scheduler.bind_actual(schedule_args,paths)
        self.raw, self.report_record = capture(args.report,self.recorded['actual_report'])
        self.seed = self.raw['supported_unit_seed_definition']
        self.seed_identity = self.raw['supported_unit_seed_identity_sha256']
        self.envelope = self.raw['material_envelope']
        self.modules['memory'].validate_report_metadata(self.envelope,
            model_identity=self.raw['model_identity_sha256'],
            carrier_sha256=self.raw['observation_carrier_sha256'])
        if canonical(self.seed) != self.seed_identity:
            raise ValueError('The complete actual fixed seed changed')
        self.input_records = [copy.deepcopy(self.report_record)]
        self.input_records += list(copy.deepcopy(self.recorded['complete_input_records']).values())
        self.input_records += [copy.deepcopy(row['actual_raw_batch']) for row in self.recorded['schedule']]
        self.actual = None
        if self.recorded['schedule']:
            actual_args = SimpleNamespace(**vars(args))
            actual_args.batch_index, actual_args.batch_arrays = 0,None
            self.actual = self.modules['accurate'].ActualMeanBatch(actual_args)
            self.context = self.actual.context
        else:
            self.context = self.modules['reference'].AxisymmetricReferenceContext.from_files(
                repo=self.repo,**self.input_paths,panels=args.panels)
        c = self.context
        if (self.seed['complete_axisymmetric_reference_model'] != c.model
                or self.seed['initial_reference_bundle_sha256'] != self.recorded['complete_input_records']['reference_bundle']['sha256']
                or self.seed['initial_reference_model_identity_sha256'] != c.identity
                or self.seed['fixed_scalar_metric_identity_sha256'] != c.scalar_identity
                or self.seed['fixed_scalar_profile_definition'] != c.scalar_definition
                or self.seed['fixed_chart_core_sha256'] != c.model['fixed_chart_core_sha256']
                or self.seed['initial_height_hex'] != float(c.height).hex()):
            raise ValueError('Keep the complete actual fixed seed/reference/scalar/chart/H')
        self.observations, prepared = c.create_problem(N=2048,stage_block=64)
        provider = self.modules['provider']
        work = self.seed['working_definition']
        parameters = provider.SeedParameters(
            support_intervals=tuple(tuple(v) for v in self.seed['exact_relative_support_intervals']),
            relative_boundary_total_length=self.seed['exact_relative_boundary_total_length'],
            profile_delta=self.seed['exact_profile_delta'],
            radial_quadrature_order=work['radial_quadrature_order'],
            profile_quadrature_order=work['profile_quadrature_order'],
            mean_maxiter=work['mean_maxiter'],mean_tolerance=float.fromhex(work['mean_physical_tolerance_hex']),
            scalar_iterations=work['scalar_iterations'],mean_backtracks=work['mean_backtracks'],
            mean_armijo=float.fromhex(work['mean_armijo_hex']))
        self.provider = provider.SupportedUnitMeridianJet(self.observations,prepared,
            expected_bundle_sha256=self.recorded['complete_input_records']['reference_bundle']['sha256'],
            seed_parameters=parameters,mean_kernel_module=self.modules['mean_kernel'],cache_directory=None)
        for name in ('evaluate','_scalar','_chart','_means','_radial'):
            if sha(getattr(self.provider,name).__func__.__code__.co_filename)!=PINS['provider'][1]:
                raise ValueError('The actual complete provider method body changed: '+name)
        if self.provider.model != self.seed or self.provider.model_identity != self.seed_identity:
            raise ValueError('The unchanged working provider is not the actual complete seed')
        latest = self.raw.get('latest_operator_metadata')
        self.seed_metadata = None if latest is None else latest['base_complete_metadata']['fixed_supported_unit_seed']
        self.mean_by_angle = {}
        self.restore_mean_inputs()
        self.plan_restoration = self.restore_radial_plan()
        self.grid, self.explicit, self.history_binding = self.complete_material_addresses()
        self.groups, self.query_definition = self.query_groups()
        self._seal_input_records()
        self.binding = dict(schema=SCHEMA,source_sha256=sha(__file__),
            complete_source_sha256_by_role={k:v[1] for k,v in PINS.items()},
            actual_report=self.report_record,
            actual_outer_driver_sha256=self.raw['source_sha256'],
            actual_outer_model_identity_sha256=self.raw['model_identity_sha256'],
            complete_seed_model=self.seed,supported_unit_seed_identity_sha256=self.seed_identity,
            fixed_scalar_metric_identity_sha256=c.scalar_identity,
            material_envelope_definition_identity_sha256=self.envelope['definition_identity_sha256'],
            complete_recorded_batch_binding=self.recorded,
            complete_input_records=self.input_records,
            restored_radial_plan=self.plan_restoration,
            restored_complete_mean_angle_count=len(self.mean_by_angle),
            no_mean_or_outer_normal_roots_recomputed=True,
            working_value_scope='fresh actual unchanged-provider evaluate calls from report-bound read-only seed inputs; old unrecorded outer node words are not asserted identical',
            old_outer_node_word_association_certified=False,
            history_binding=self.history_binding,complete_query_plan=self.query_definition,
            exact_reference_point_formula='s=lambda*S+eta; lambda,eta from exact original nodes and literal binary64 u',
            complete_field_certificate=False)
        self.identity = canonical(self.binding)
        self.recheck()

    def _add_input(self, record):
        if file_record(record['path']) != record:
            raise ValueError('A full source-bound actual input changed')
        self.input_records.append(copy.deepcopy(record))

    def _seal_input_records(self):
        result = {}
        for item in self.input_records:
            path = item['path']
            if path in result and result[path] != item:
                raise ValueError('The same actual path changed identity inside the input closure')
            result[path] = item
            p = Path(path).resolve()
            if p == self.args.outdir or self.args.outdir in p.parents:
                raise ValueError('The complete output namespace must be disjoint from every immutable input')
        self.input_records = [result[key] for key in sorted(result)]

    def recheck(self):
        for record in self.input_records:
            if file_record(record['path']) != record:
                raise ValueError('An actual node input changed after binding: '+record['path'])

    def restore_mean_inputs(self):
        import numpy as np
        for row in self.recorded['schedule']:
            batch = row['actual_complete_batch_metadata']
            values = checked_arrays(row['actual_raw_batch'])
            count = row['literal_angle_count']
            if str(values['seed_model_identity'].item()) != self.seed_identity:
                raise ValueError('Actual mean arrays belong to another seed')
            phi = finite_array(values['phi'],shape=(count,))
            if [float(v).hex() for v in phi] != batch['literal_angle_hex']:
                raise ValueError('Retain the entire actual mean angle order')
            for key in VECTOR_KEYS+SCALAR_KEYS:
                finite_array(values[key],shape=(count,3) if key in VECTOR_KEYS else (count,))
            for index,word in enumerate(batch['literal_angle_hex']):
                if word in self.mean_by_angle:
                    raise ValueError('Duplicate actual completed mean angle')
                self.mean_by_angle[word] = dict(batch_index=row['batch_index'],angle_index=index,
                    actual_raw_batch=row['actual_raw_batch'],
                    actual_words={key:([float(v).hex() for v in values[key][index]]
                        if key in VECTOR_KEYS else float(values[key][index]).hex())
                        for key in VECTOR_KEYS+SCALAR_KEYS})
                self.provider._mean_cache[word] = {key:readonly(values[key][index])
                    for key in VECTOR_KEYS+SCALAR_KEYS[:3]}
        if len(self.provider._mean_cache) != self.recorded['actual_recorded_literal_angles']:
            raise ValueError('A complete recorded mean angle was dropped')
        # These are imported immutable inputs. Original actual new-root counters
        # remain zero and old batch/elapsed records are not relabelled as new work.
        if any(self.provider.counts[key] for key in ('new_mean_angles','mean_batches','completed_mean_angles')):
            raise ValueError('Restoring actual input words must not execute a new mean root')

    def restore_radial_plan(self):
        import numpy as np
        record = None if self.seed_metadata is None else self.seed_metadata.get('radial_plan')
        if record is None:
            if self.mean_by_angle:
                raise ValueError('Completed actual means require their full original radial plan')
            return dict(complete=False,reason='no actual complete radial plan in the source report')
        if (record.get('source_sha256') != PINS['provider'][1]
                or record.get('seed_model_identity_sha256') != self.seed_identity
                or record.get('complete_domain') is not True
                or record.get('original_cell_count') != 922
                or record.get('no_scalar_tail_or_radial_piece_dropped') is not True):
            raise ValueError('Keep the complete same-source, same-seed radial plan')
        for key in ('runner_raw_arrays','runner_raw_description'):
            self._add_input(record[key])
        description,_ = capture(record['runner_raw_description']['path'],record['runner_raw_description'])
        plain = {k:v for k,v in record.items() if k not in ('runner_raw_arrays','runner_raw_description')}
        if {k:v for k,v in description.items() if k not in ('pieces','nodes')} != plain:
            raise ValueError('The complete plan description differs from the actual report snapshot')
        if (canonical(description['pieces']) != record['pieces_identity_sha256']
                or canonical(description['nodes']) != record['nodes_identity_sha256']
                or len(description['pieces']) != record['exact_piece_count']):
            raise ValueError('The complete actual plan piece/node descriptions changed')
        data = checked_arrays(record['runner_raw_arrays'])
        keys = ('boundary_values','boundary_weights','boundary_chi','outside_values','outside_weights','base_gauss_u','base_gauss_w')
        if set(data) != set(keys)|{'model_identity','central_length','outside_integrals'}:
            raise ValueError('Retain the exact complete original radial-plan array schema')
        if str(data['model_identity'].item()) != self.seed_identity:
            raise ValueError('The complete radial-plan arrays name another seed')
        B,O = record['complete_positive_boundary_node_count'],record['complete_positive_complement_node_count']
        Q = self.seed['working_definition']['radial_quadrature_order']
        shapes = dict(boundary_values=(B,4),boundary_weights=(B,),boundary_chi=(B,),
            outside_values=(O,4),outside_weights=(O,),base_gauss_u=(Q,),base_gauss_w=(Q,))
        for key in keys:
            finite_array(data[key],shape=shapes[key])
            if array_record(data[key]) != record['arrays'][key]:
                raise ValueError('Actual radial-plan array words changed: '+key)
        finite_array(data['central_length'],shape=())
        finite_array(data['outside_integrals'],shape=(2,))
        if (float(data['central_length']).hex() != record['central_length_carrier_hex']
                or [float(v).hex() for v in data['outside_integrals']] != [record['outside_horizontal_integral_carrier_hex'],record['outside_vertical_integral_carrier_hex']]
                or float(data['central_length']) <= 0
                or np.any(data['boundary_weights'] <= 0) or np.any(data['outside_weights'] <= 0)
                or np.any(data['base_gauss_w'] <= 0) or np.any(data['base_gauss_u'] <= 0)
                or np.any(data['base_gauss_u'] >= 1) or np.any(data['boundary_chi'] < 0)
                or np.any(data['boundary_chi'] > 1)):
            raise ValueError('The complete original positive plan has inconsistent actual scalar words')
        self.provider._plan = dict(arrays={key:data[key] for key in keys},
            central_length=float(data['central_length']),outside_horizontal=float(data['outside_integrals'][0]),
            outside_vertical=float(data['outside_integrals'][1]),record=copy.deepcopy(record))
        return dict(complete=True,actual_report_record=record,
            actual_description_piece_count=len(description['pieces']),actual_description_node_count=len(description['nodes']),
            full_actual_plan_arrays_actually_read=True,new_plan_integrals_or_mean_roots_computed=False)

    def complete_material_addresses(self):
        memory,history = self.modules['memory'],self.modules['history']
        preparation,preparation_record = capture(self.input_paths['preparation_report'])
        if preparation_record != self.recorded['complete_input_records']['preparation_report']:
            raise ValueError('The complete actual preparation changed')
        current = memory.read_carrier(self.input_paths['carrier'],self.raw['observation_carrier_sha256'])
        hb = self.envelope['historical_address_binding']
        current_record = hb['current_carrier']['record']
        if current['metadata'] != hb['current_carrier'] or current['record'] != current_record:
            raise ValueError('The actual current full carrier changed')
        old_record = hb['origin_carrier']['record']
        old = memory.read_carrier(old_record['path'],old_record['sha256'])
        if old['metadata'] != hb['origin_carrier'] or old['record'] != old_record:
            raise ValueError('The actual original full carrier changed')
        self._add_input(old_record)
        binding = hb['actual_path_binding']
        if 'binding_file' in binding:
            self._add_input(binding['binding_file'])
            payload,_ = capture(binding['binding_file']['path'],binding['binding_file'])
            checked = memory.validate_public_binding(payload,current_input=current['record'])
            if dict(checked,binding_file=binding['binding_file']) != binding:
                raise ValueError('The complete carrier path binding changed')
        original,origin = memory._original_p0(self.args,preparation,history,old_record['path'])
        if origin != hb['original_p0']:
            raise ValueError('All eleven actual original payloads/roles/protected points are required')
        self._add_input(preparation['complete_supplied_location_provenance'])
        points = history.Locations(923,7377,2048)
        points.walk(original.arrays(),path=('complete_actual_original_p0',))
        locations,_ = capture(preparation['new_locations']['path'],preparation['new_locations'])
        self._add_input(preparation['new_locations'])
        if (locations['carrier_sha256'] != current_record['sha256']
                or locations['reference_bundle_sha256'] != self.raw['bundle_sha256']
                or locations['N'] != 2048
                or locations['complete_supplied_provenance'] != preparation['complete_supplied_location_provenance']):
            raise ValueError('Keep the complete actual prepared locations and provenance')
        points.walk(locations,path=('complete_actual_current_prepared_locations',))
        sources = self.raw['history']['sources']
        if sources[:2] != [preparation_record,preparation['new_locations']]:
            raise ValueError('The declared complete history prefix changed')
        for record in sources[2:]:
            payload,_ = capture(record['path'],record)
            self._add_input(record)
            if payload.get('carrier_sha256',payload.get('observation_carrier_sha256')) != current_record['sha256']:
                raise ValueError('An explicit source names another actual carrier')
            if memory._indexed_grid(payload) and int(payload.get('N',payload.get('full_angles',payload.get('full_N',-1)))) != 2048:
                raise ValueError('Do not reinterpret an actual indexed historical angle')
            if payload.get('schema') == 'deep-valley-same-symbolic-location-transfer-v1':
                payload = {key:payload[key] for key in memory.ORIGIN_P0}
            points.walk(payload,path=('explicit_complete_history',Path(record['path']).name))
        points.resolve_grid(self.input_paths['carrier'])
        arrays = points.arrays()
        initial = {_key(v) for key in ('curvature_points','radius_points') for v in arrays[key]}
        expected = self.envelope['known_explicit_history']
        if (len(initial) != expected['initial_unique_locations']
                or canonical(sorted(initial)) != expected['initial_binary_locations_sha256']):
            raise ValueError('The complete known explicit initial envelope differs')
        radial = set(current['radial_words']) | set(old['radial_words'])
        phi = tuple(float(v).hex() for v in self.observations.phi)
        formula = tuple(float(math.pi*j/1024).hex() for j in range(513))
        grid = self.envelope['implicit_grid']
        if (phi != formula or array_sha(self.observations.phi) != grid['actual_phi_sha256']
                or canonical(sorted(radial)) != grid['union_radial_words_sha256']
                or len(radial)*len(phi) != grid['unique_implicit_material_locations']):
            raise ValueError('The complete actual radial and angular envelope words changed')
        points.walk(self.raw,path=('complete_actual_source_report',))
        points.resolve_grid(self.input_paths['carrier'])
        all_arrays = points.arrays()
        all_explicit = {_key(v) for key in ('curvature_points','radius_points','protected_curvature_points') for v in all_arrays[key]}
        for row in self.envelope['actual_separation_memory']['rows']:
            for location in (row['location'],None if row['partner'] is None else row['partner'].get('location')):
                if location is not None:
                    all_explicit.add(memory._point_key(location))
        if any(v not in initial and not ((v[0],v[1]) in radial and v[2] in phi) for v in all_explicit):
            raise ValueError('An actual new address escaped the complete source-closed material envelope')
        return dict(radial=sorted(radial),phi=list(phi)),sorted(all_explicit),dict(
            actual_old_and_current_complete_arrays_read=True,
            original_eleven_payloads=origin,known_explicit_initial_count=len(initial),
            known_explicit_initial_binary_sha256=canonical(sorted(initial)),
            complete_actual_explicit_count=len(all_explicit),complete_actual_explicit_binary_sha256=canonical(sorted(all_explicit)),
            actual_separation_memory_count=self.envelope['actual_separation_memory']['count'],
            unknown_old_protected_order_reconstructed=False,
            complete_old_current_grid_permanent_query_responsibility=True)

    def query_groups(self):
        import numpy as np
        c = self.context
        needed = list(self.grid['phi'])
        seen = set(needed)
        for word in [v[2] for v in self.explicit]+list(self.mean_by_angle):
            if word not in seen:
                needed.append(word);seen.add(word)
        order = int(self.raw['latest_operator_metadata']['base_complete_metadata']['working_integration_order'])
        if order != self.seed['working_definition']['radial_quadrature_order']:
            raise ValueError('This complete node plan requires the actual original and provider radial rules to agree in order')
        saved = c.data
        expected_cells = np.repeat(np.arange(c.J-1,dtype=np.int64),order)
        count = len(expected_cells)
        cells = finite_array(saved['cached_scalar_cells'][:count],shape=(count,),integer=True)
        local = finite_array(saved['cached_scalar_local'][:count],shape=(count,))
        if (not np.array_equal(cells,expected_cells) or np.any(local <= 0) or np.any(local >= 1)
                or not np.array_equal(local,np.tile(local[:order],c.J-1))):
            raise ValueError('The actual reference preparation must retain the entire first complete Gauss query')
        if self.provider._plan is None:
            actual_gu_equal = None
        else:
            gu = self.provider._plan['arrays']['base_gauss_u']
            actual_gu_equal = gu.tobytes() == local[:order].tobytes()
            if not actual_gu_equal:
                raise ValueError('The two actually recorded complete radial query word sets differ; require an explicit expanded plan')
        integration = [(int(j),float(u).hex()) for j,u in zip(cells,local)]
        groups = [dict(kind='whole_old_current_material_grid',radial=self.grid['radial'],phi=self.grid['phi']),
            dict(kind='whole_original_meridian_integration_at_every_required_angle',radial=integration,phi=needed)]
        radial_grid,radial_integration = set(self.grid['radial']),set(integration)
        explicit_by_angle = {}
        for j,u,p in self.explicit:
            if ((j,u) in radial_grid and p in set(self.grid['phi'])) or (j,u) in radial_integration:
                continue
            explicit_by_angle.setdefault(p,[]).append((j,u))
        for word in sorted(explicit_by_angle):
            groups.append(dict(kind='complete_explicit_material_locations',radial=sorted(set(explicit_by_angle[word])),phi=[word]))
        records=[]
        for index,group in enumerate(groups):
            group['group_index']=index
            group['identity_sha256']=canonical({k:group[k] for k in ('kind','radial','phi')})
            group['point_count']=len(group['radial'])*len(group['phi'])
            records.append(dict(group_index=index,kind=group['kind'],identity_sha256=group['identity_sha256'],
                radial_count=len(group['radial']),angular_count=len(group['phi']),point_count=group['point_count'],
                radial_words_sha256=canonical(group['radial']),literal_angle_words_sha256=canonical(group['phi'])))
        missing=[word for word in needed if word not in self.mean_by_angle]
        definition=dict(schema=PLAN_SCHEMA,source_sha256=sha(__file__),groups=records,
            planned_points_with_explicit_group_multiplicity=sum(v['point_count'] for v in records),
            required_literal_angles=len(needed),ordered_required_literal_angle_words_sha256=canonical(needed),
            actual_recorded_complete_mean_angles=len(self.mean_by_angle),missing_completed_mean_angles=missing,
            complete_old_current_grid=True,complete_explicit_and_typed_partner_locations=True,
            complete_original_integral_at_every_required_angle=True,
            actual_reference_integration_query=dict(order=order,cells=array_record(cells),local=array_record(local),
                scalar_cache_prefix_in_original_preparation_actually_checked=True,
                actual_reference_and_provider_gauss_words_equal=actual_gu_equal,
                old_outer_internal_leggauss_words_independently_recorded=False),
            angle_subset_used=False,missing_mean_angles_dropped=False,
            old_outer_working_node_word_identity_claimed=False)
        return groups,definition

    def chunks(self, radial_block, angle_block):
        serial=0
        for group in self.groups:
            for a in range(0,len(group['phi']),angle_block):
                for r in range(0,len(group['radial']),radial_block):
                    value=dict(serial=serial,group_index=group['group_index'],group_identity_sha256=group['identity_sha256'],
                        kind=group['kind'],radial_start=r,angle_start=a,
                        radial=group['radial'][r:r+radial_block],phi=group['phi'][a:a+angle_block])
                    value['identity_sha256']=canonical(value)
                    yield value
                    serial+=1

    def evaluate(self, chunk):
        require_actions()
        import numpy as np
        if self.provider._plan is None:
            raise ValueError('No complete actual radial plan exists; do not compute a substitute plan')
        if any(word not in self.mean_by_angle for word in chunk['phi']):
            raise ValueError('A required actual completed mean angle is absent; no new root is silently computed')
        cells=np.asarray([v[0] for v in chunk['radial']],dtype=np.int64)
        local=np.asarray([float.fromhex(v[1]) for v in chunk['radial']],dtype=float)
        phi=np.asarray([float.fromhex(v) for v in chunk['phi']],dtype=float)
        before=dict(self.provider.counts)
        actual=self.provider.evaluate(cells,local,phi)
        after=dict(self.provider.counts)
        if any(after[key] != before[key] for key in ('new_mean_angles','mean_batches','completed_mean_angles')):
            raise ValueError('The node producer unexpectedly computed a new mean root')
        shape=(len(cells),len(phi),3)
        values={name:readonly(finite_array(actual[key],shape=shape)) for name,key in FIELD_MAP.items()}
        radial=self.provider._radial(cells,local)
        widths=self.context.mesh[cells+1]-self.context.mesh[cells]
        s=self.context.mesh[cells]+widths*local
        arrays=dict(cells=cells,local=local,phi=phi,working_mesh_width=widths,working_s=s,
            **values,working_original_scalar_jets=radial['values'],working_region_tags=radial['kinds'],
            working_chi=radial['chi'],working_chi_s=radial['chi_s'],working_profile=radial['profile'],working_profile_s=radial['profile_s'],
            working_theta=actual['theta_parent'],working_rho=actual['rho_parent'],working_rho_phi=actual['rho_phi_parent'])
        records={key:array_record(value) for key,value in arrays.items()}
        return arrays,dict(schema=WORK_SCHEMA,source_sha256=sha(__file__),
            binding_identity_sha256=self.identity,chunk=chunk,actual_provider_sha256=PINS['provider'][1],
            supported_unit_seed_identity_sha256=self.seed_identity,
            actual_report=self.report_record,array_records=records,
            actual_provider_metadata=actual['metadata'],
            actual_provider_counts_before=before,actual_provider_counts_after=after,
            actual_provider_count_delta={key:after[key]-before[key] for key in before},
            immutable_mean_inputs=[dict(literal_phi_hex=word,**self.mean_by_angle[word]) for word in chunk['phi']],
            actual_values_computed_in_this_new_producer=True,
            actual_node_execution=dict(repository=os.environ['GITHUB_REPOSITORY'],
                run_id=os.environ.get('GITHUB_RUN_ID'),run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
                trigger_commit=os.environ.get('GITHUB_SHA'),python_version=sys.version,
                numpy_version=np.__version__),
            old_outer_unrecorded_working_words_asserted_identical=False,
            current_outer_F_J_and_normal_roots_recomputed=False,
            exact_scalar_and_mesh_carrier_are_distinct=True)

    def exact_point(self, cell, local_word):
        u=F(float.fromhex(local_word))
        return tuple((1-u)*a+u*b for a,b in zip(self.context.nodes[int(cell)],self.context.nodes[int(cell)+1]))
