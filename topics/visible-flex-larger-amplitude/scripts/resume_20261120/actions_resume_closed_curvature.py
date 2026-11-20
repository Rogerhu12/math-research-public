#!/usr/bin/env python3
"""Same-field R672 continuation with immutable complete-cell returns.

This producer calls the frozen 8ca81 R672 CurvatureReader.cell kernel.
It imports actual old checkpoints or its own raw-return journal; it does
not import curvature from another field or implement a new interval law.
All scientific execution is restricted to the authorized public Actions.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace

import numpy as np


SCHEMA = 'R672-complete-curvature-continuation-v1'
RAW_SCHEMA = 'R672-complete-curvature-continuation-cell-v1'
OLD_SCHEMA = 'fullclosed-complete-lowmode-sixjet-curvature-actions-v1'
KERNEL_SHA = '8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385'
FIRST_SHA = 'eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599'
REPOSITORY = 'Rogerhu12/math-research-public'
SOURCE_ROLES = ('geometry_source', 'interval_source', 'difference_source', 'transfer_source')


def digest_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for part in iter(lambda: stream.read(1 << 20), b''):
            h.update(part)
    return h.hexdigest()


def identity(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def read_json(path):
    data = json.loads(Path(path).read_text())
    if not isinstance(data, dict):
        raise ValueError('Expected a JSON object: '+str(path))
    return data


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(value, separators=(',', ':'), allow_nan=False)+'\n')
    temporary.replace(path)


def number(value):
    if isinstance(value, bool) or value is None:
        raise ValueError('Expected a finite recorded number')
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('Expected a finite recorded number')
    return F(value)


def event(**value):
    print(json.dumps(value, allow_nan=False), flush=True)


def load(path, expected, name):
    if sha(path) != expected:
        raise ValueError('Changed frozen mathematical source: '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def ranges(values):
    """Inclusive integer intervals; no per-cell numerical values."""
    result = []
    for value in sorted(set(values)):
        if result and value == result[-1][1]+1:
            result[-1][1] = value
        else:
            result.append([value, value])
    return result


def spec_key(spec):
    # radial_block is a memory batching parameter, not a new cover domain.
    return (spec['angles'], spec['radial_subdivisions'],
            spec['retained_angle_modes'], spec['taylor_degree'])


def row_spec(row, degree):
    return dict(angles=int(row['angles']),
        radial_subdivisions=int(row['radial_subdivisions_per_piece']),
        retained_angle_modes=int(row['retained_angle_modes']),
        taylor_degree=int(degree), radial_block=int(row['requested_radial_block']))


def check_spec(spec):
    Q, radial, modes, degree = spec_key(spec)
    if (Q < 4 or Q & (Q-1) or radial < 1 or radial & (radial-1)
            or modes < 1 or Q <= 4*modes or degree < 1 or spec['radial_block'] < 1):
        raise ValueError('Invalid recorded R672 complete-cell configuration')


def check_row(row, J, spec):
    if (not isinstance(row, dict) or not isinstance(row.get('cell'), int)
            or not 0 <= row['cell'] < J-1
            or row.get('all_original_points_covered') is not True
            or row.get('full_original_modes_and_complete_analytic_lift_paid') is not True
            or row.get('actual_first_form_used') is not True
            or row.get('sampled_a_used_as_geometry') is not False
            or row.get('strict_outward_arithmetic') is not True
            or not isinstance(row.get('exact_lift_pieces'), int) or row['exact_lift_pieces'] < 1
            or row_spec(row, spec['taylor_degree']) != spec):
        raise ValueError('A returned row does not bind a complete R672 cell and its actual configuration')
    check_spec(spec)
    unpaid = row.get('unpaid_immersion_boxes')
    if not isinstance(unpaid, int) or isinstance(unpaid, bool) or unpaid < 0:
        raise ValueError('Invalid unpaid-immersion count')
    paid = row.get('curvature_bound_certified')
    if paid is True:
        if (unpaid != 0 or number(row.get('curvature_upper')) < 0
                or number(row.get('minimum_E_lower')) <= 0
                or number(row.get('minimum_normal_squared_lower')) <= 0):
            raise ValueError('A claimed cell curvature bound has unpaid first form or invalid upper bound')
    elif paid is False:
        if unpaid == 0 or row.get('curvature_upper') is not None:
            raise ValueError('An unpaid cell cannot supply a curvature upper bound')
    else:
        raise ValueError('Missing literal curvature-bound status')
    if number(row.get('seconds')) < 0:
        raise ValueError('Invalid actual cell elapsed time')
    return paid


def same_execution(report):
    execution = report.get('execution', {})
    if execution.get('GITHUB_REPOSITORY') != REPOSITORY or not execution.get('GITHUB_RUN_ID'):
        raise ValueError('Returned evidence must identify the authorized public Actions execution')


def exact_box(value):
    return [str(number(value[key])) for key in ('lower_exact', 'upper_exact')]


def actual_inputs(args, paths):
    sources = {key: identity(paths[key]) for key in SOURCE_ROLES}
    sources.update(bundle=identity(args.bundle), node_report=identity(args.node_report))
    node = read_json(args.node_report)
    nodes = node.get('true_scalar_nodes', [])
    if len(nodes) < 2:
        raise ValueError('Need the actual complete symbolic node report')
    with np.load(args.bundle, allow_pickle=False) as data:
        shape = data['qjets'].shape
        mesh = data['mesh']
        if len(shape) != 3 or shape[0] != len(nodes) or shape[1] != 3 or (shape[2]-2) % 3:
            raise ValueError('Actual complete nodal carrier shape differs from the node report')
        if any(number(data[key].item()) != 0 for key in ('reference_tail_lambda', 'exact_tail_lambda')
               if key in data.files):
            raise ValueError('Frozen R672 is the original polynomial-lift field, not nonzero R671')
        if 'reference_tail_model_json' in data.files:
            encoded = data['reference_tail_model_json'].item()
            model = json.loads(encoded.decode() if isinstance(encoded, bytes) else str(encoded))
            if number(model.get('lambda_value')) != 0:
                raise ValueError('A nonzero reference-tail definition cannot use the old R672 geometry kernel')
        H, width, radius = [float(data[k]) for k in ('Hcap', 'width', 'radius')]
        if (node.get('S_carrier') != float(mesh[-1]) or node.get('radius_carrier') != radius
                or not np.isfinite([H, width, radius]).all() or min(H, width, radius) <= 0):
            raise ValueError('Actual node, endpoint, radius or height identity differs')
    scalar = node['scalar']
    metadata = dict(J=len(nodes), M=(shape[2]-2)//3,
        exact_S_box=exact_box(scalar['S']), exact_R_box=exact_box(scalar['R']),
        exact_width=str(F(width)), exact_H=str(F(H)), scalar_identity=scalar,
        original_polynomial_lift_only=True, R671_nonpolynomial_reference_lift_supported=False,
        normal_orientation='F_phi cross F_s',
        curvature='Absolute eigenvalues of actual Euclidean shape operator')
    first = identity(args.first_geometry_report) if args.first_geometry_report is not None else None
    if first is not None:
        report = read_json(args.first_geometry_report)
        same_execution(report)
        if (report.get('source_sha256') != FIRST_SHA or report.get('complete_scope') is not True
                or [row.get('cell') for row in report.get('records', [])] != list(range(len(nodes)-1))
                or any(report.get('source_inputs', {}).get(k, {}).get('sha256') != sources[k]['sha256']
                       for k in ('bundle', 'node_report'))):
            raise ValueError('Optional first-form lower bounds must bind this exact complete first-geometry report')
    binding = dict(source_sha256s={key: value['sha256'] for key, value in sources.items()},
        kernel_source_sha256=KERNEL_SHA, first_geometry_source_sha256=FIRST_SHA,
        first_geometry_report_sha256=None if first is None else first['sha256'],
        field_metadata=metadata)
    return sources, first, binding, metadata


def check_old(report, binding, metadata, degree):
    same_execution(report)
    if (report.get('schema') != OLD_SCHEMA or report.get('source_sha256') != KERNEL_SHA
            or report.get('first_geometry_source_sha256') != FIRST_SHA
            or any(report.get('source_inputs', {}).get(k, {}).get('sha256') != value
                   for k, value in binding['source_sha256s'].items())):
        raise ValueError('Old checkpoint differs from the actual bundle/node or frozen mathematical sources')
    old = report.get('metadata', {})
    for key, value in metadata.items():
        if old.get(key) != value:
            raise ValueError('Old checkpoint field metadata differs: '+key)
    if old.get('taylor_degree') != degree:
        raise ValueError('This minimal continuation retains the original complete Taylor degree')
    previous = old.get('optional_first_geometry')
    if (None if previous is None else previous.get('sha256')) != binding['first_geometry_report_sha256']:
        raise ValueError('Retain the same actual optional first-geometry report when importing this checkpoint')
    return old


class Continuation:
    def __init__(self, args, kernel, runtime, paths, sources, first, binding, metadata, execution, started):
        self.args, self.kernel, self.runtime, self.paths = args, kernel, runtime, paths
        self.sources, self.first, self.binding, self.metadata = sources, first, binding, metadata
        self.execution, self.started = execution, started
        self.producer_sha = sha(__file__)
        self.target = F(args.target)
        self.plan = [dict(angles=Q, radial_subdivisions=r, retained_angle_modes=m,
            taylor_degree=args.taylor_degree, radial_block=args.radial_block)
            for Q, r, m in kernel.parse_levels(args.levels)]
        if len({spec_key(s) for s in self.plan}) != len(self.plan):
            raise ValueError('Do not repeat the same complete-cell cover configuration')
        for spec in self.plan:
            check_spec(spec)
            if spec['retained_angle_modes'] > metadata['M']:
                raise ValueError('Retained low modes cannot exceed the actual full field bandwidth')
        self.directory = (args.records_directory or args.out.with_name(args.out.stem+'-cells')).resolve()
        if args.repo == self.directory or args.repo in self.directory.parents:
            raise ValueError('Immutable scientific cell returns must stay outside the repository')
        if self.directory == args.out or self.directory in args.out.parents:
            raise ValueError('Keep the mutable aggregate report outside its immutable cell-return directory')
        self.directory.mkdir(parents=True, exist_ok=True)
        self.J = metadata['J']
        self.expected = list(range(self.J-1))
        self.calls, self.imports, self.setups, self.sessions = [], [], [], []
        self.best, self.completed_keys, self.loaded = {}, set(), {}
        self.reused_bound_cells = set()
        self.current = None
        self.state, self.reason = 'running', None
        self.reader, self.base = None, None
        self.kernel_metadata = None
        self.maximum_transform_group_entries = 0
        self.carrier = identity(args.carrier) if args.carrier is not None else None
        self.lineage = None

    def key(self, cell, spec):
        return (int(cell), *spec_key(spec))

    def budget_hit(self):
        return self.args.budget_seconds > 0 and time.monotonic()-self.started >= self.args.budget_seconds

    def add_row(self, row, spec, reference):
        paid = check_row(row, self.J, spec)
        self.completed_keys.add(self.key(row['cell'], spec))
        if paid:
            old = self.best.get(row['cell'])
            if old is None or number(row['curvature_upper']) < number(old['record']['curvature_upper']):
                self.best[row['cell']] = dict(record=row, configuration=spec, source=reference)

    def snapshot_old(self, path):
        # Read/hash precisely the same immutable bytes, even if a producer
        # had atomically replaced the source file between other reads.
        path = Path(path).resolve()
        raw = path.read_bytes()
        digest = digest_bytes(raw)
        frozen = self.directory/('seed-'+digest+'.json')
        if frozen.exists():
            if sha(frozen) != digest:
                raise ValueError('A previous immutable seed snapshot changed')
        else:
            temporary = frozen.with_name(frozen.name+'.partial')
            temporary.write_bytes(raw)
            temporary.replace(frozen)
        return json.loads(raw), dict(path=str(frozen), sha256=digest, original_path=str(path), bytes=len(raw))

    def import_old(self, path):
        report, saved = self.snapshot_old(path)
        old_meta = check_old(report, self.binding, self.metadata, self.args.taylor_degree)
        if any(value.get('kind') == 'actual_8ca_checkpoint'
               and value.get('sha256') == saved['sha256'] for value in self.imports):
            return
        selected = report.get('selected_cells')
        if (not isinstance(selected, list) or selected != sorted(set(selected)) or not selected
                or any(not isinstance(i, int) or not 0 <= i < self.J-1 for i in selected)):
            raise ValueError('Old checkpoint has an invalid actual selected-cell scope')
        selected = set(selected)
        returned_best = {}
        imported = []
        for index, row in enumerate(report.get('attempts', [])):
            spec = row_spec(row, old_meta['taylor_degree'])
            check_row(row, self.J, spec)
            level = row.get('level')
            if (row['cell'] not in selected or not isinstance(level, int)
                    or not 0 <= level < len(report['levels'])
                    or list(report['levels'][level]) != list(spec_key(spec)[:3])):
                raise ValueError('Old attempt differs from its literal level or selected scope')
            reference = dict(kind='old_kernel_report', **saved, attempt_index=index)
            self.add_row(row, spec, reference)
            if row['curvature_bound_certified']:
                self.reused_bound_cells.add(row['cell'])
                before = returned_best.get(row['cell'])
                if before is None or number(row['curvature_upper']) < number(before['curvature_upper']):
                    returned_best[row['cell']] = row
            self.calls.append(dict(cell=row['cell'], configuration=spec, original_level=level,
                state='returned', output=reference, origin='actual_8ca_checkpoint',
                original_call_seconds=row['seconds']))
            imported.append(row['cell'])
        if (report.get('best') != {str(k): v for k, v in returned_best.items()}
                or report.get('covered_original_cells') != sorted(returned_best)):
            raise ValueError('Old aggregate does not agree with its complete returned attempts')
        self.loaded[(saved['path'], saved['sha256'])] = report
        self.imports.append(dict(kind='actual_8ca_checkpoint', **saved,
            returned_attempts=len(imported), covered_cell_ranges=ranges(returned_best),
            original_seconds=report.get('seconds'), original_complete_scope=report.get('complete_scope'),
            old_target_exact=report.get('target_exact'), numerical_fields_recomputed=False,
            original_beta_not_recorded_in_8ca_report=True,
            beta_scope='beta does not enter the R672 Euclidean shape-operator kernel'))

    def load_return(self, reference, spec):
        path = Path(reference['path']).resolve()
        key = (str(path), reference['sha256'])
        if key not in self.loaded:
            raw = path.read_bytes()
            if digest_bytes(raw) != reference['sha256']:
                raise ValueError('An immutable actual-return file changed: '+str(path))
            self.loaded[key] = json.loads(raw)
        report = self.loaded[key]
        if reference['kind'] == 'old_kernel_report':
            check_old(report, self.binding, self.metadata, self.args.taylor_degree)
            row = report['attempts'][reference['attempt_index']]
        elif reference['kind'] == 'cell_return':
            same_execution(report)
            if (report.get('schema') != RAW_SCHEMA or report.get('state') != 'returned'
                    or report.get('producer_source_sha256') != self.producer_sha
                    or report.get('kernel_source_sha256') != KERNEL_SHA
                    or report.get('field_binding') != self.binding
                    or report.get('configuration') != spec):
                raise ValueError('A raw return belongs to another field, producer or declared call')
            row = report['record']
        else:
            raise ValueError('Unknown returned-evidence format')
        check_row(row, self.J, spec)
        return row

    def import_resume(self, path):
        source = read_json(path)
        same_execution(source)
        if (source.get('schema') != SCHEMA or source.get('source_sha256') != self.producer_sha
                or source.get('kernel_source_sha256') != KERNEL_SHA or source.get('field_binding') != self.binding
                or source.get('taylor_degree') != self.args.taylor_degree):
            raise ValueError('Resume must retain this actual field, frozen kernel and producer')
        self.imports.extend(source.get('imports', []))
        self.sessions.extend(source.get('sessions', []))
        self.sessions.append(dict(kind='prior_invocation', report=identity(path),
            state=source.get('state'), seconds=source.get('seconds'), execution=source.get('execution')))
        for prior in source.get('calls', []):
            call = dict(prior)
            spec = call['configuration']
            if call.get('state') in ('running', 'failed') and call.get('planned_raw_output'):
                planned = Path(call['planned_raw_output'])
                if planned.is_file() and 'output' not in call:
                    reference = dict(kind='cell_return', **identity(planned))
                    row = self.load_return(reference, spec)
                    if row['cell'] != call['cell']:
                        raise ValueError('A recovered durable return belongs to a different cell')
                    call.update(state='returned', output=reference, original_call_seconds=row['seconds'],
                        recovery='Raw cell atomically returned before the parent checkpoint was updated')
                    call.pop('contribution', None)
                elif call.get('state') == 'running' and 'output' not in call:
                    call.update(state='unreturned', consequence='No bound or elapsed cell cost assumed')
            if call.get('state') == 'returned':
                row = self.load_return(call['output'], spec)
                if row['cell'] != call['cell']:
                    raise ValueError('Checkpoint row address differs from actual raw return')
                self.add_row(row, spec, call['output'])
                if row['curvature_bound_certified']:
                    self.reused_bound_cells.add(row['cell'])
            elif call.get('state') == 'failed':
                # A declared new resolution may be attempted, never a hidden
                # repeat of the identical failed call on ordinary resume.
                self.completed_keys.add(self.key(call['cell'], spec))
            self.calls.append(call)
        for prior in source.get('reader_setups', []):
            setup = dict(prior)
            if setup.get('state') == 'running':
                setup.update(state='unreturned', consequence='No new cell bounds were inferred')
            self.setups.append(setup)
        self.kernel_metadata = source.get('last_kernel_metadata')
        self.maximum_transform_group_entries = source.get('maximum_transform_group_entries', 0)

    def summary(self):
        valid = sorted(self.best)
        paid = [cell for cell in valid if number(self.best[cell]['record']['curvature_upper']) <= self.target]
        paid_set = set(paid)
        not_covered = [cell for cell in self.expected if cell not in self.best]
        above = [cell for cell in valid if cell not in paid_set]
        maximum = max((number(v['record']['curvature_upper']) for v in self.best.values()), default=None)
        maximum_paid = max((number(self.best[i]['record']['curvature_upper']) for i in paid), default=None)
        complete = valid == self.expected
        E = min((number(v['record']['minimum_E_lower']) for v in self.best.values()), default=None)
        W2 = min((number(v['record']['minimum_normal_squared_lower']) for v in self.best.values()), default=None)
        cuff = self.best.get(self.J-2)
        cuff_rho = None
        if cuff is not None:
            squared = number(cuff['record']['minimum_normal_squared_lower'])/F(self.metadata['exact_R_box'][1])**2
            unit = 1 << 80
            cuff_rho = F(math.isqrt(squared.numerator*unit*unit//squared.denominator), unit)
        marker = F(self.metadata['exact_H']) > 1 and F(self.metadata['exact_R_box'][0]) > F(9, 20)
        asfloat = lambda value: None if value is None else float(value)
        down = None if cuff_rho is None else float(cuff_rho)
        if down is not None and F(down) > cuff_rho:
            down = float(np.nextafter(down, -np.inf))
        return dict(covered_original_cells=valid, valid_cell_count=len(valid), expected_cell_count=self.J-1,
            target_paid_cell_count=len(paid), uncovered_cell_count=len(not_covered),
            remaining_above_target=sorted(not_covered+above), remaining_target_count=len(not_covered)+len(above),
            covered_scope_curvature_upper=asfloat(maximum),
            covered_scope_curvature_upper_exact=None if maximum is None else str(maximum),
            target_paid_scope_curvature_upper=asfloat(maximum_paid),
            target_paid_scope_curvature_upper_exact=None if maximum_paid is None else str(maximum_paid),
            covered_minimum_E_lower=asfloat(E), covered_minimum_normal_squared_lower=asfloat(W2),
            complete_selected_scope=complete, complete_scope=complete,
            continuous_curvature_upper=asfloat(maximum) if complete else None,
            continuous_curvature_upper_exact=str(maximum) if complete else None,
            target_certified=bool(complete and len(paid) == self.J-1),
            full_closed_immersion_certified=complete,
            flat_caps_curvature_upper=0., mirror_and_activity_phases_preserve_absolute_curvature=True,
            manifest_positions_covered_by_full_continuous_domain=complete,
            new_core_rho_lower=down, core_rho_lower_from_cuff_area=down,
            core_rho_lower_from_cuff_area_exact=None if cuff_rho is None else str(cuff_rho),
            conditional_four_p4_marker_curvature_upper=float(max(maximum, F(5))) if complete and marker else None,
            coverage_summary=dict(valid_cell_ranges=ranges(valid), target_paid_cell_ranges=ranges(paid),
                uncovered_cell_ranges=ranges(not_covered), valid_above_target_cell_ranges=ranges(above),
                scope='Ranges describe precisely returned continuous covers; no missing cell is assigned zero',
                compact_cross_job_resume_implemented=False),
            full_closed_embedding_certified=False, reach_certified=False, metric_certified=False,
            topic_completion_certified=False)

    def write(self):
        summary = self.summary()
        result = dict(schema=SCHEMA, source_sha256=self.producer_sha, kernel_source_sha256=KERNEL_SHA,
            first_geometry_source_sha256=FIRST_SHA, execution=self.execution,
            source_inputs=self.sources, field_binding=self.binding, metadata=self.metadata,
            optional_first_geometry_report=self.first, observation_carrier=self.carrier,
            supplied_location_manifests=self.lineage,
            producer_scope='Scheduling and same-field reuse only; every new complete-cell mathematical call is frozen R672 CurvatureReader.cell',
            original_polynomial_lift_only=True, R671_nonpolynomial_reference_lift_supported=False,
            target_exact=str(self.target), beta_exact=str(F(self.args.beta)),
            taylor_degree=self.args.taylor_degree, requested_radial_block=self.args.radial_block,
            requested_levels=self.args.levels, refinement_plan=self.plan,
            budget_seconds=self.args.budget_seconds, budget_scope='Stop new setup/cell admission; an admitted cell returns naturally',
            state=self.state, stop_reason=self.reason, current=self.current,
            imports=self.imports, sessions=self.sessions, reader_setups=self.setups, calls=self.calls,
            best={str(k): v['record'] for k, v in self.best.items()},
            best_sources={str(k): v['source'] for k, v in self.best.items()},
            last_kernel_metadata=self.kernel_metadata, records_directory=str(self.directory),
            maximum_transform_group_entries=self.maximum_transform_group_entries,
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            all_reported_input_hashes_actual=True, historical_candidate_hash_assumed=False,
            old_candidate_curvature_values_inherited=False,
            same_field_previously_returned_bounds_reused=bool(self.reused_bound_cells),
            same_field_previously_returned_bound_cell_count=len(self.reused_bound_cells),
            mathematical_kernel_modified=False, per_cell_raw_publication_allowed=False,
            raw_outputs_policy='Complete cell returns and attempts stay runner-local; publish source/parameters/actual hashes and compact covered-domain bounds only',
            seconds=time.monotonic()-self.started, **summary)
        write_json(self.args.out, result)
        return result

    def prepare_reader(self, spec):
        if self.reader is not None:
            self.reader.set_resolution(spec['angles'], spec['retained_angle_modes'])
            return
        setup = dict(configuration=spec, state='running')
        self.setups.append(setup)
        self.current = dict(kind='reader_setup', configuration=spec)
        self.write()
        begin = time.monotonic()
        try:
            a = SimpleNamespace(bundle=self.args.bundle, node_report=self.args.node_report,
                beta=self.args.beta, taylor_degree=self.args.taylor_degree,
                low_modes=spec['retained_angle_modes'],
                plan=[(spec['angles'], spec['radial_subdivisions'])])
            self.base = self.runtime.make_direct_reader(a, self.paths)
            self.reader = self.kernel.CurvatureReader(self.base, radial_block=self.args.radial_block,
                first_geometry_report=self.args.first_geometry_report)
            metadata = self.reader.metadata()
            for key, value in self.metadata.items():
                if metadata.get(key) != value:
                    raise ValueError('Actual reader differs from the declared current field: '+key)
            self.kernel_metadata = metadata
            setup.update(state='returned', seconds=time.monotonic()-begin)
        except BaseException as error:
            setup.update(state='failed' if isinstance(error, Exception) else 'unreturned',
                seconds=time.monotonic()-begin, error_type=type(error).__name__, error=str(error))
            raise
        finally:
            self.current = None
            self.write()

    def call(self, cell, spec, level, priority):
        number_id = len(self.calls)
        raw_path = self.directory/('return-'+str(number_id).zfill(6)+'-cell-'+str(cell).zfill(5)+'.json')
        if raw_path.exists():
            raise FileExistsError('Preserve the prior immutable cell return: '+str(raw_path))
        call = dict(cell=cell, configuration=spec, level=level, priority=priority,
            state='running', planned_raw_output=str(raw_path))
        self.calls.append(call)
        self.current = dict(kind='complete_cell', call_index=number_id, cell=cell, configuration=spec)
        self.write()
        begin = time.monotonic()
        try:
            row = self.reader.cell(cell, spec['radial_subdivisions'])
            row['level'] = level
            check_row(row, self.J, spec)
            raw = dict(schema=RAW_SCHEMA, producer_source_sha256=self.producer_sha,
                kernel_source_sha256=KERNEL_SHA, field_binding=self.binding,
                configuration=spec, execution=self.execution, state='returned', record=row,
                call_seconds=time.monotonic()-begin)
            write_json(raw_path, raw)
            reference = dict(kind='cell_return', **identity(raw_path))
            self.add_row(row, spec, reference)
            call.update(state='returned', output=reference, original_call_seconds=row['seconds'],
                observed_call_seconds=raw['call_seconds'])
            self.maximum_transform_group_entries = max(self.maximum_transform_group_entries,
                self.reader.maximum_transform_group_entries)
        except Exception as error:
            call.update(state='failed', observed_call_seconds=time.monotonic()-begin,
                error_type=type(error).__name__, error=str(error), contribution='No new bound consumed')
            self.completed_keys.add(self.key(cell, spec))
            raise
        finally:
            # A BaseException may leave state=running: resume distinguishes
            # a complete durable raw file from a genuinely unreturned cell.
            self.current = None
            result = self.write()
        event(event='R672_complete_cell_return', cell=cell, level=level, priority=priority,
            state=call['state'], curvature_upper=row['curvature_upper'],
            valid_cells=result['valid_cell_count'], target_paid=result['target_paid_cell_count'],
            covered_curvature_upper=result['covered_scope_curvature_upper'],
            complete_scope=result['complete_scope'], target_certified=result['target_certified'],
            call_seconds=call['observed_call_seconds'], seconds=result['seconds'])

    def pending(self, spec, coverage_only):
        out = []
        for cell in self.expected:
            value = self.best.get(cell)
            if value is not None and (coverage_only or number(value['record']['curvature_upper']) <= self.target):
                continue
            if self.key(cell, spec) not in self.completed_keys:
                out.append(cell)
        return out

    def finish(self):
        result = self.write()
        event(event='R672_continuation_checkpoint', state=self.state, report=str(self.args.out),
            report_sha256=sha(self.args.out), valid_cells=result['valid_cell_count'],
            target_paid=result['target_paid_cell_count'], complete_scope=result['complete_scope'],
            continuous_curvature_upper=result['continuous_curvature_upper'],
            target_certified=result['target_certified'], seconds=result['seconds'])
        return result

    def run(self):
        self.lineage = self.runtime.read_manifest_locations(self.args)
        self.write()
        try:
            # Complete previously uncovered domains first, at each declared
            # resolution if needed.  Target refinement follows only after
            # that coverage pass; no returned identical cover is rerun.
            for coverage_only in (True, False):
                priority = 'uncovered_first' if coverage_only else 'above_target_only'
                for level, spec in enumerate(self.plan):
                    pending = self.pending(spec, coverage_only)
                    if not pending:
                        continue
                    if self.budget_hit():
                        self.state, self.reason = 'budget_checkpoint', 'Budget reached before new setup/cell admission'
                        return self.finish()
                    self.prepare_reader(spec)
                    event(event='R672_continuation_level', priority=priority, level=level,
                        configuration=spec, pending=len(pending), seconds=time.monotonic()-self.started)
                    for cell in pending:
                        if self.budget_hit():
                            self.state, self.reason = 'budget_checkpoint', 'Budget reached after the previous complete cell naturally returned'
                            return self.finish()
                        self.call(cell, spec, level, priority)
            summary = self.summary()
            self.state = 'completed' if summary['target_certified'] else 'plan_exhausted'
            self.reason = ('Every original cell has an actual complete bound at or below the stated target'
                if summary['target_certified'] else 'No unattempted declared cover remains; unpaid or above-target cells stay explicit')
        except BaseException as error:
            self.state, self.reason = ('failed' if isinstance(error, Exception) else 'interrupted'), repr(error)
            self.write()
            if not isinstance(error, Exception):
                raise
            event(event='R672_continuation_failed', error_type=type(error).__name__, error=str(error))
        return self.finish()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'bundle', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    for name in ('node-report', 'carrier', 'first-geometry-report', 'records-directory', 'resume'):
        parser.add_argument('--'+name, type=Path)
    parser.add_argument('--manifest', type=Path, action='append', default=[])
    parser.add_argument('--seed-report', type=Path, action='append', default=[])
    parser.add_argument('--levels', default='256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96')
    parser.add_argument('--target', default='8.1')
    parser.add_argument('--taylor-degree', type=int, default=12)
    parser.add_argument('--radial-block', type=int, default=4)
    parser.add_argument('--beta', default='1/4')
    parser.add_argument('--budget-seconds', type=float, default=0.)
    args = parser.parse_args()
    if os.environ.get('GITHUB_ACTIONS', '').lower() != 'true' or os.environ.get('GITHUB_REPOSITORY') != REPOSITORY:
        raise SystemExit('Scientific curvature continuation runs only in the authorized public GitHub Actions.')
    started = time.monotonic()
    if (F(args.target) <= 0 or args.taylor_degree < 1 or args.radial_block < 1
            or not 0 < F(args.beta) <= 1 or not math.isfinite(args.budget_seconds) or args.budget_seconds < 0):
        raise ValueError('Invalid exact target, Taylor order, block size, beta or admission budget')
    args.repo, args.work, args.out = args.repo.resolve(), args.work.resolve(), args.out.resolve()
    if args.repo == args.out or args.repo in args.out.parents:
        raise ValueError('Scientific raw reports must stay outside the repository')
    if args.out.exists() and (args.resume is None or args.out != args.resume.resolve()):
        raise FileExistsError('Use a new output, or explicitly resume this same checkpoint')
    src = args.repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261120'
    kernel = load(src/'actions_closed_curvature.py', KERNEL_SHA, '_frozen_R672_curvature_kernel')
    runtime = load(src/'actions_closed_postprocess.py', FIRST_SHA, '_frozen_R670_curvature_context')
    execution = runtime.actions_context()
    args.command = 'curvature'
    runtime.common_paths(args)
    if args.first_geometry_report is not None:
        args.first_geometry_report = args.first_geometry_report.resolve()
    paths = runtime.source_paths(args.repo)
    sources, first, binding, metadata = actual_inputs(args, paths)
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    schedule = Continuation(args, kernel, runtime, paths, sources, first, binding, metadata, execution, started)
    if args.resume is not None:
        schedule.import_resume(args.resume.resolve())
    for path in args.seed_report:
        schedule.import_old(path)
    result = schedule.run()
    if result['state'] == 'failed':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
