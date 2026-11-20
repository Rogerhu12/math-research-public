#!/usr/bin/env python3
"""Full-domain scheduling/checkpoints for the frozen R674 tight Gram kernel.

No new interval formula, scalar cache, field, metric or solver step is added.
Each successful call covers one complete original cell with all physical
pieces and angles.  Missing or unreturned calls never contribute a zero.
All scientific execution, including report reuse, belongs in public Actions.
"""
import argparse
from fractions import Fraction as F
import gc
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import resource
import sys
import time

import numpy as np


SCHEMA = 'R674-full-domain-adaptive-tight-Gram-v1'
RAW_SCHEMA = 'R674-full-domain-adaptive-tight-Gram-cell-v1'
KERNEL_SCHEMA = 'R674-reference-tail-cancellation-preserving-relative-Gram-v1'
KERNEL_SHA = 'fd4cd58045e16a969c8c1be48468ab4c1a7be929ef9b95e2a9a24ca546176b2d'
PROFILE_SHA = 'f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225'
FACTORY_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
LEGACY_SHA = '5bbf821f45fec3a8ecd29ebd64dce8058bb302f7d53416b50158cca743065a13'
README_TARGET = F(1, 1000000)


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(value):
    raw = json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def file_identity(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def read_json(path):
    result = json.loads(Path(path).read_text())
    if not isinstance(result, dict):
        raise ValueError('Expected a JSON object: '+str(path))
    return result


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name+'.partial')
    tmp.write_text(json.dumps(value, separators=(',', ':'), allow_nan=False)+'\n')
    tmp.replace(path)


def finite_fraction(value):
    if isinstance(value, bool) or value is None:
        raise ValueError('A finite numerical bound is required')
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('Nonfinite bound')
    return F(value)


def pair(value):
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError('Expected an exact affine-in-S pair')
    return tuple(F(item) for item in value)


def spec_key(spec):
    return tuple(spec.get(key) for key in ('angles', 'radial_subdivisions', 'scalar_degree', 'panels'))


def levels(text, M, panels):
    if text == 'auto':
        Q = 2048
        while Q < 9*M:
            Q *= 2
        values = [(Q*2**j, 2**j, n, panels) for j, n in enumerate((5, 5, 6, 7, 8))]
    else:
        values = []
        for item in text.split(','):
            data = [int(v) for v in item.split(':')]
            if len(data) == 3:
                data.append(panels)
            if len(data) != 4:
                raise ValueError('Use Q:radial:degree[:panels], separated by commas')
            values.append(tuple(data))
    if not values:
        raise ValueError('A nonempty declared refinement plan is required')
    for Q, radial, degree, p in values:
        if Q < 2 or Q & (Q-1) or radial < 1 or radial & (radial-1) or not 3 <= degree <= 8 or p < 1:
            raise ValueError('Dyadic Q/radial, degree 3..8 and positive panels are required')
    result = [dict(angles=q, radial_subdivisions=r, scalar_degree=n, panels=p) for q, r, n, p in values]
    if len({spec_key(value) for value in result}) != len(result):
        raise ValueError('Do not repeat an identical mathematical call configuration')
    return result


def load_kernel(repo):
    path = Path(repo).resolve()/'topics/visible-flex-larger-amplitude/scripts/resume_20261120/exact_reference_tail_relative_gram_interval.py'
    if sha(path) != KERNEL_SHA:
        raise ValueError('The declared complete-cell tight Gram source changed')
    name = '_full_domain_tight_Gram_kernel_'+KERNEL_SHA[:16]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module, path


def actual_definition(args):
    inputs = {key: file_identity(getattr(args, key)) for key in ('bundle', 'node_report', 'scalar_input')}
    if args.reference_carrier is not None:
        inputs['reference_carrier'] = file_identity(args.reference_carrier)
    node = read_json(args.node_report)
    nodes = [pair([v['S_coefficient'], v['constant']]) for v in node['true_scalar_nodes']]
    with np.load(args.bundle, allow_pickle=False) as data:
        encoded = data['reference_tail_model_json'].item()
        model = json.loads(encoded.decode() if isinstance(encoded, bytes) else str(encoded))
        lam = finite_fraction(data['reference_tail_lambda'].item())
        tags = [finite_fraction(data[key].item()) for key in ('exact_tail_lambda',) if key in data.files]
    if (model.get('schema') != 'R671-exact-reference-tail-lift-v1'
            or model.get('source_sha256') != FACTORY_SHA
            or model.get('node_report_sha256') != inputs['node_report']['sha256']
            or model.get('scalar_input_sha256') != inputs['scalar_input']['sha256']
            or finite_fraction(model.get('lambda_value')) != lam or not 0 <= lam <= 1
            or any(value != lam for value in tags)
            or not isinstance(model.get('M'), int) or model['M'] < 1
            or len(nodes) < 2 or nodes[0] != (F(0), F(0)) or nodes[-1] != (F(1), F(0))):
        raise ValueError('The actual bundle/node/scalar must have one canonical R671 definition')
    binding = dict(bundle_sha256=inputs['bundle']['sha256'], node_report_sha256=inputs['node_report']['sha256'],
        scalar_input_sha256=inputs['scalar_input']['sha256'], model_identity_sha256=canonical_sha(model),
        J=len(nodes), M=model['M'])
    return inputs, binding, model, nodes


def check_kernel_report(report, binding, model):
    sources = report.get('source_inputs', {})
    if (report.get('schema') != KERNEL_SCHEMA or report.get('source_sha256') != KERNEL_SHA
            or report.get('reference_interval_source_sha256') != PROFILE_SHA
            or report.get('legacy_Gram_source_sha256') != LEGACY_SHA
            or report.get('model_definition') != model
            or report.get('model_identity_sha256') != binding['model_identity_sha256']
            or report.get('J') != binding['J'] or report.get('M') != binding['M']
            or any(sources.get(key, {}).get('sha256') != binding[key+'_sha256']
                   for key in ('bundle', 'node_report', 'scalar_input'))):
        raise ValueError('Seed report differs from the actual field or frozen complete-cell source')


def check_row(row, cell, nodes):
    if (not isinstance(row, dict) or row.get('cell') != cell or not 0 <= cell < len(nodes)-1
            or pair(row.get('symbolic_left')) != nodes[cell] or pair(row.get('symbolic_right')) != nodes[cell+1]
            or row.get('all_radial_and_angular_points_covered') is not True
            or row.get('strict_under_stated_IEEE_arithmetic') is not True
            or row.get('old_candidate_bounds_inherited') is not False):
        raise ValueError('Returned row is not a complete current-field original-cell enclosure')
    upper = finite_fraction(row.get('continuous_relative_gram_operator_upper'))
    lower = finite_fraction(row.get('actual_supremum_lower'))
    if (not 0 <= lower <= upper or finite_fraction(row.get('minimum_a_lower')) <= 0
            or finite_fraction(row.get('minimum_rho_lower')) <= 0):
        raise ValueError('Invalid cell bounds or unpaid target-metric positivity')
    return upper, lower


def address(row, spec, which):
    value = row.get('worst' if which == 'upper' else 'actual_lower_witness')
    if not isinstance(value, dict):
        return None
    result = dict(value, angles=spec['angles'], radial_subdivisions=spec['radial_subdivisions'])
    part, sub = value.get('piece'), value.get('radial_subcell')
    pieces = row.get('scalar_pieces', [])
    physical = next((p for p in pieces if p.get('piece') == part and p.get('radial_subcell') == sub), None)
    if physical is not None and 'symbolic_left' in physical:
        left, right = pair(physical['symbolic_left']), pair(physical['symbolic_right'])
    elif isinstance(part, int) and 0 <= part < len(pieces) and 'left' in pieces[part]:
        left0, right0 = pair(pieces[part]['left']), pair(pieces[part]['right'])
        r = spec['radial_subdivisions']
        left = tuple(a+(b-a)*F(sub, r) for a, b in zip(left0, right0))
        right = tuple(a+(b-a)*F(sub+1, r) for a, b in zip(left0, right0))
    else:
        left, right = None, None
    if left is not None:
        result.update(symbolic_left=[str(v) for v in left], symbolic_right=[str(v) for v in right])
        if which == 'lower':
            point = left if value.get('endpoint') == 0 else right
            result['exact_witness_s'] = [str(v) for v in point]
    if isinstance(value.get('angle_grid_index'), int):
        result['angle_center_pi_coefficient_exact'] = str(F(2*value['angle_grid_index'], spec['angles']))
        if which == 'upper':
            result['closed_arc_halfwidth_pi_coefficient_exact'] = str(F(1, spec['angles']))
    return result


def diagnostic(row, spec):
    names = ('maximum_component_absolute_upper', 'minimum_a_lower', 'minimum_rho_lower',
        'scalar_remainder_relative_gram_upper', 'scalar_target_remainder_relative_gram_upper',
        'new_physical_scalar_gram_fee_component_upper', 'angular_padding_operator_upper',
        'nonlinear_angular_fourth_order_padding_upper', 'numerator_coefficient_interval_width_upper',
        'reference_lift_active', 'maximum_numerator_degree')
    result = {key: row[key] for key in names if key in row}
    fees = row.get('new_physical_scalar_gram_fee_component_upper')
    if isinstance(fees, list) and len(fees) == 3:
        e, m, g = [finite_fraction(value) for value in fees]
        result['physical_scalar_fee_operator_upper_by_row_sum_exact'] = str(max(e, g)+m)
    result['worst_upper_location'] = address(row, spec, 'upper')
    result['actual_lower_witness_location'] = address(row, spec, 'lower')
    result['scope'] = ('Scalar Gram fees are relative-matrix budgets; nonlinear fourth-order padding and coefficient width '
                       'are unnormalized numerator diagnostics, not an additive decomposition of actual error')
    return result


class Schedule:
    def __init__(self, args, kernel_path, inputs, binding, model, nodes, plan):
        self.args, self.kernel_path = args, kernel_path
        self.inputs, self.binding, self.model, self.nodes, self.plan = inputs, binding, model, nodes, plan
        self.source_sha = sha(__file__)
        self.target = F(args.target)
        self.started = time.monotonic()
        self.calls, self.setups, self.imports = [], [], []
        self.best = {}
        self.current = None
        self.status = 'running'
        self.stop_reason = None
        self.reader_metadata = None
        self.directory = args.records_directory or args.out.with_name(args.out.stem+'-cells')
        self.directory = self.directory.resolve()
        self.directory.mkdir(parents=True, exist_ok=True)
        self.loaded_reports = {}

    def add_bound(self, row, spec, reference):
        cell = row['cell']
        upper, lower = check_row(row, cell, self.nodes)
        detail = diagnostic(row, spec)
        old = self.best.get(cell)
        if old is None:
            self.best[cell] = dict(upper=upper, lower=lower, upper_source=reference, lower_source=reference,
                upper_configuration=spec, lower_configuration=spec,
                upper_diagnostics=detail, lower_witness=detail['actual_lower_witness_location'],
                consistent=True)
            return
        if upper < old['upper']:
            old.update(upper=upper, upper_source=reference, upper_configuration=spec, upper_diagnostics=detail)
        if lower > old['lower']:
            old.update(lower=lower, lower_source=reference, lower_configuration=spec,
                       lower_witness=detail['actual_lower_witness_location'])
        old['consistent'] = bool(old['consistent'] and old['lower'] <= old['upper'])

    def load_reference(self, reference, configuration=None):
        path = Path(reference['path']).resolve()
        key = (str(path), reference['sha256'])
        if key not in self.loaded_reports:
            if sha(path) != reference['sha256']:
                raise ValueError('Prior raw output bytes changed: '+str(path))
            self.loaded_reports[key] = read_json(path)
        source = self.loaded_reports[key]
        if reference['kind'] == 'kernel_report':
            check_kernel_report(source, self.binding, self.model)
            if source.get('execution', {}).get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
                raise ValueError('Prior mathematical report does not identify public Actions')
            row = source['records'][reference['row_index']]
        elif reference['kind'] == 'cell_return':
            if (source.get('schema') != RAW_SCHEMA or source.get('dispatcher_source_sha256') != self.source_sha
                    or source.get('kernel_source_sha256') != KERNEL_SHA or source.get('field_binding') != self.binding
                    or source.get('state') != 'returned'
                    or source.get('execution', {}).get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
                raise ValueError('Prior cell return does not bind the same source and field')
            if configuration is not None and source.get('configuration') != configuration:
                raise ValueError('The recorded call parameters differ from the actual returned raw file')
            row = source['record']
        else:
            raise ValueError('Unknown raw return reference')
        return row

    def import_seed(self, path):
        record = file_identity(path)
        source = read_json(path)
        check_kernel_report(source, self.binding, self.model)
        rows = source.get('records', [])
        if source.get('covered_cells') != [row.get('cell') for row in rows]:
            raise ValueError('Seed report complete-return list differs from its actual rows')
        spec = dict(angles=int(source['angles']), radial_subdivisions=int(source['radial_subdivisions_per_joint_piece']),
            scalar_degree=int(source['scalar_taylor_degree']),
            panels=(source.get('fullhold') or {}).get('simpson_panels_per_ramp'))
        added = []
        for index, row in enumerate(rows):
            ref = dict(kind='kernel_report', path=record['path'], sha256=record['sha256'], row_index=index)
            actual_row = self.load_reference(ref, spec)
            self.add_bound(actual_row, spec, ref)
            call = dict(cell=actual_row['cell'], configuration=spec, state='returned', output=ref,
                        origin='explicit_same-field_fd4_seed', original_call_seconds=actual_row.get('seconds'))
            self.calls.append(call); added.append(actual_row['cell'])
        self.reader_metadata = {key:value for key, value in source.items()
            if key not in ('records', 'covered_cells', 'requested_cells')}
        self.imports.append(dict(**record, kind='fd4_returned_cells', cells=added,
            previous_complete_scope=source.get('complete_scope'), field_values_recomputed=False))

    def import_resume(self, path):
        record = file_identity(path)
        source = read_json(path)
        if (source.get('schema') != SCHEMA or source.get('source_sha256') != self.source_sha
                or source.get('kernel_source_sha256') != KERNEL_SHA or source.get('field_binding') != self.binding):
            raise ValueError('Resume checkpoint belongs to a different source or actual field')
        for previous in source.get('calls', []):
            call = dict(previous)
            if call.get('state') == 'returned':
                row = self.load_reference(call['output'], call['configuration'])
                self.add_bound(row, call['configuration'], call['output'])
            elif call.get('state') == 'running':
                call.update(state='unreturned', consequence='No bound consumed; no zero value and no assumed elapsed cost')
            self.calls.append(call)
        for previous in source.get('reader_setups', []):
            setup = dict(previous)
            if setup.get('state') == 'running':
                setup.update(state='unreturned', consequence='No cell bound from this setup was assumed')
            self.setups.append(setup)
        self.reader_metadata = source.get('last_reader_metadata')
        self.imports.append(dict(**record, kind='same-field_checkpoint',
            prior_status=source.get('status'), prior_seconds=source.get('seconds'),
            completed_raw_files_rechecked=True, geometric_field_recomputed=False))

    def classification(self, cell):
        value = self.best.get(cell)
        if value is None:
            return 'unpaid_no_return'
        if not value['consistent']:
            return 'inconsistent_returned_bounds'
        if value['upper'] <= self.target:
            return 'requested_bound_paid'
        if value['lower'] > self.target:
            return 'current_candidate_proved_above_target'
        return 'enclosure_unresolved'

    def eligible(self, cell, spec, initial):
        state = self.classification(cell)
        if state not in ('unpaid_no_return', 'enclosure_unresolved'):
            return False
        if initial and cell in self.best:
            return False  # Already paid complete cover is not rerun as a coarse pass.
        for call in self.calls:
            if call.get('cell') != cell:
                continue
            old = call.get('configuration', {})
            if spec_key(old) == spec_key(spec):
                return False  # Even a failed/unreturned call is not silently repeated.
            if call.get('state') == 'returned' and all(old.get(k) is not None and old[k] >= spec[k]
                    for k in ('angles', 'radial_subdivisions', 'scalar_degree', 'panels')):
                return False  # Scheduling choice only; no assertion that bounds are monotone.
        return True

    def budget_hit(self):
        return self.args.budget_seconds > 0 and time.monotonic()-self.started >= self.args.budget_seconds

    def snapshot(self):
        valid = {cell: value for cell, value in self.best.items() if value['consistent']}
        expected = list(range(self.binding['J']-1))
        complete = sorted(valid) == expected
        upper = max((value['upper'] for value in valid.values()), default=None)
        lower = max((value['lower'] for value in valid.values()), default=None)
        records, groups = [], {}
        for cell in expected:
            state = self.classification(cell)
            groups.setdefault(state, []).append(cell)
            value = self.best.get(cell)
            record = dict(cell=cell, state=state)
            if value is not None:
                record.update(upper_exact=str(value['upper']), lower_exact=str(value['lower']),
                    upper=float(value['upper']), lower=float(value['lower']),
                    upper_source=value['upper_source'], lower_source=value['lower_source'],
                    upper_configuration=value['upper_configuration'], lower_configuration=value['lower_configuration'],
                    upper_diagnostics=value['upper_diagnostics'], actual_lower_witness=value['lower_witness'])
            records.append(record)
        eligible_records = [row for row in records if row['cell'] in valid]
        upper_top = sorted(eligible_records, key=lambda row: F(row['upper_exact']), reverse=True)[:self.args.bottlenecks]
        lower_top = sorted(eligible_records, key=lambda row: F(row['lower_exact']), reverse=True)[:self.args.bottlenecks]
        unresolved = [row for row in eligible_records if row['state'] == 'enclosure_unresolved']
        gap_top = sorted(unresolved, key=lambda row: F(row['upper_exact'])-F(row['lower_exact']),
                         reverse=True)[:self.args.bottlenecks]
        summary = dict(complete_scope=complete, covered_cells=sorted(valid), expected_cells=expected,
            covered_relative_gram_operator_upper=None if upper is None else float(upper),
            covered_relative_gram_operator_upper_exact=None if upper is None else str(upper),
            covered_actual_supremum_lower=None if lower is None else float(lower),
            covered_actual_supremum_lower_exact=None if lower is None else str(lower),
            complete_relative_gram_operator_upper=float(upper) if complete else None,
            complete_relative_gram_operator_upper_exact=str(upper) if complete else None,
            requested_target_certified=bool(complete and upper <= self.target),
            metric_certified=bool(complete and upper <= README_TARGET),
            all_t_metric_certified=bool(complete and upper <= README_TARGET),
            current_candidate_proved_above_requested_target=bool(lower is not None and lower > self.target),
            current_candidate_proved_above_README_target=bool(lower is not None and lower > README_TARGET),
            states=groups, state_counts={key:len(value) for key, value in groups.items()}, records=records,
            bottlenecks=dict(highest_upper=upper_top, highest_strict_lower=lower_top, largest_unresolved_gap=gap_top),
            lower_bound_scope='Maximum of rigorous norm lower endpoints at actual exact radial/angle witness points; a lower bound on the true supremum, never an average or the lower endpoint of an upper-bound formula')
        return summary

    def write(self):
        summary = self.snapshot()
        result = dict(schema=SCHEMA, source_sha256=self.source_sha, kernel_source_sha256=KERNEL_SHA,
            reference_interval_source_sha256=PROFILE_SHA, legacy_Gram_source_sha256=LEGACY_SHA,
            execution={key: os.environ.get(key) for key in ('GITHUB_REPOSITORY','GITHUB_RUN_ID',
                'GITHUB_RUN_ATTEMPT','GITHUB_WORKFLOW','GITHUB_SHA')},
            source_inputs=dict(self.inputs, adaptive_source=file_identity(__file__), kernel_source=file_identity(self.kernel_path)),
            field_binding=self.binding, model_definition=self.model,
            requested_target_exact=str(self.target), README_target_exact=str(README_TARGET),
            requested_levels=self.args.levels, refinement_plan=self.plan,
            budget_seconds=self.args.budget_seconds, records_directory=str(self.directory),
            imported_reports=self.imports, calls=self.calls, reader_setups=self.setups,
            last_reader_metadata=self.reader_metadata, current=self.current,
            status=self.status, stop_reason=self.stop_reason, **summary,
            cap_relative_gram_upper_exact='0', cap_metrics_exact_and_reflection_preserves_gram=True,
            phase_scope='R248 angle conjugacy is an isometry of the same activity g; ambient rotations preserve Gram and full-angle bounds cover every phase',
            cap_metric_scope='Unmarked flat caps use their flat metric; any R661 fixed marker graphs use their own common induced metric. No claim that nonzero graphs preserve the old flat cap metric',
            common_activity_metric_changed=False, field_or_coordinates_changed=False,
            original_free_modes_discarded=False, scalar_cache_added=False, interval_formula_changed=False,
            embedding_certified=False, reach_certified=False, fixed_metric_refinement_certified=False,
            mesh_frequency_refinement_convergence_claimed=False, topic_completion_certified=False,
            raw_outputs_policy='Runner-local complete per-cell rows and immutable raw report references; publish source, parameters, run, hashes and compact bottlenecks only',
            seconds=time.monotonic()-self.started,
            process_peak_rss_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        atomic_json(self.args.out, result)
        return result

    def run(self, kernel):
        self.write()
        for level, spec in enumerate(self.plan):
            pending = [cell for cell in range(self.binding['J']-1) if self.eligible(cell, spec, level == 0)]
            if not pending:
                continue
            if self.budget_hit():
                self.stop_reason = 'Budget reached before admitting a new reader/cell; all prior returns retained'
                break
            setup = dict(level=level, configuration=spec, state='running', admitted_cells=pending,
                         historical_elapsed_cost_assumed=False)
            self.setups.append(setup)
            self.current = dict(kind='reader_initialization', level=level, configuration=spec)
            self.write(); begin = time.monotonic()
            try:
                reader = kernel.make_reader(repo=self.args.repo, bundle=self.args.bundle,
                    node_report=self.args.node_report, scalar_input=self.args.scalar_input,
                    reference_carrier=self.args.reference_carrier, angles=spec['angles'],
                    radial_subdivisions=spec['radial_subdivisions'], scalar_degree=spec['scalar_degree'], panels=spec['panels'])
                metadata = reader.metadata()
                check_kernel_report(metadata, self.binding, self.model)
                self.reader_metadata = metadata
                setup.update(state='returned', seconds=time.monotonic()-begin,
                    model_identity_sha256=metadata['model_identity_sha256'])
            except Exception as error:
                setup.update(state='failed', seconds=time.monotonic()-begin,
                    error_type=type(error).__name__, error=str(error), contribution='No cell bounds')
                self.current = None; self.write()
                print(json.dumps(dict(event='adaptive_Gram_reader_failed', **setup)), flush=True)
                if isinstance(error, MemoryError):
                    self.stop_reason = 'An actual reader allocation failed; no wider level admitted in this invocation'
                    break
                continue
            for cell in pending:
                if self.budget_hit():
                    self.stop_reason = 'Budget reached after the current call naturally returned; no live task abandoned'
                    break
                number = len(self.calls)
                path = self.directory/('return-'+str(number).zfill(6)+'-cell-'+str(cell).zfill(5)+'.json')
                if path.exists():
                    raise FileExistsError('Preserve a previous raw cell output: '+str(path))
                call = dict(cell=cell, level=level, configuration=spec, state='running',
                    planned_raw_output=str(path), original_call_seconds=None)
                self.calls.append(call)
                self.current = dict(kind='complete_cell', call_index=number, cell=cell, level=level, configuration=spec)
                self.write(); begin = time.monotonic()
                try:
                    row = reader.certify(cell)
                    check_row(row, cell, self.nodes)
                    raw = dict(schema=RAW_SCHEMA, dispatcher_source_sha256=self.source_sha,
                        kernel_source_sha256=KERNEL_SHA, field_binding=self.binding, configuration=spec,
                        execution={key: os.environ.get(key) for key in ('GITHUB_REPOSITORY','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT')},
                        state='returned', record=row, call_seconds=time.monotonic()-begin)
                    atomic_json(path, raw)
                    ref = dict(kind='cell_return', path=str(path), sha256=sha(path))
                    self.add_bound(row, spec, ref)
                    call.update(state='returned', output=ref, original_call_seconds=raw['call_seconds'])
                except Exception as error:
                    call.update(state='failed', original_call_seconds=time.monotonic()-begin,
                        error_type=type(error).__name__, error=str(error), contribution='No new cell bound')
                self.current = None
                result = self.write()
                current = self.best.get(cell)
                print(json.dumps(dict(event='adaptive_Gram_cell_return', cell=cell, level=level,
                    call_state=call['state'], mathematical_state=self.classification(cell),
                    upper=None if current is None else float(current['upper']),
                    strict_lower=None if current is None else float(current['lower']),
                    call_seconds=call['original_call_seconds'], total_seconds=result['seconds'],
                    complete_scope=result['complete_scope'], metric_certified=result['metric_certified'])), flush=True)
                if call.get('error_type') == 'MemoryError':
                    self.stop_reason = 'An actual cell allocation failed; no wider level admitted in this invocation'
                    break
            self.reader_metadata = reader.metadata()
            del reader; gc.collect()
            self.current = None; self.write()
            if self.stop_reason:
                break
        self.current = None
        final = self.snapshot()
        if self.stop_reason:
            self.status = 'checkpoint_unfinished'
        elif final['requested_target_certified']:
            self.status = 'complete_requested_bound_certified'
        elif final['complete_scope'] and final['current_candidate_proved_above_requested_target']:
            self.status = 'complete_current_candidate_proved_above_target'
        elif final['complete_scope']:
            self.status = 'complete_cover_target_unresolved'
        else:
            self.status = 'declared_plan_returned_with_unpaid_domain'
        result = self.write()
        print(json.dumps(dict(event='adaptive_Gram_checkpoint', report=str(self.args.out.resolve()),
            report_sha256=sha(self.args.out), bundle_sha256=self.binding['bundle_sha256'], status=self.status,
            complete_scope=result['complete_scope'], upper=result['complete_relative_gram_operator_upper'],
            covered_strict_lower=result['covered_actual_supremum_lower'], state_counts=result['state_counts'],
            metric_certified=result['metric_certified'], seconds=result['seconds'])), flush=True)


def main():
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Execute scientific scheduling and report consumption only in the public repository Actions')
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo','bundle','node-report','scalar-input','out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--reference-carrier', type=Path)
    parser.add_argument('--records-directory', type=Path)
    parser.add_argument('--seed-report', action='append', type=Path, default=[])
    parser.add_argument('--resume', type=Path)
    parser.add_argument('--levels', default='auto', help='auto or Q:r:n[:panels],...; only unresolved cells enter later levels')
    parser.add_argument('--panels', type=int, default=128)
    parser.add_argument('--target', default='1/1000000', help='Exact positive rational; README metric flag always uses 1/1000000')
    parser.add_argument('--budget-seconds', type=float, default=0., help='0: no extra dispatcher budget; stop admitting calls only after a natural return')
    parser.add_argument('--bottlenecks', type=int, default=16)
    args = parser.parse_args()
    args.out = args.out.resolve()
    if args.out.exists():
        raise FileExistsError('Use a fresh output; prior checkpoints may enter via --resume')
    if F(args.target) <= 0 or args.panels < 1 or args.budget_seconds < 0 or not math.isfinite(args.budget_seconds) or args.bottlenecks < 1:
        raise ValueError('Invalid exact target, panels, budget or bottleneck count')
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    kernel, path = load_kernel(args.repo)
    inputs, binding, model, nodes = actual_definition(args)
    plan = levels(args.levels, binding['M'], args.panels)
    work = Schedule(args, path, inputs, binding, model, nodes, plan)
    if args.resume is not None:
        work.import_resume(args.resume)
    for source in args.seed_report:
        work.import_seed(source)
    work.run(kernel)


if __name__ == '__main__':
    main()
