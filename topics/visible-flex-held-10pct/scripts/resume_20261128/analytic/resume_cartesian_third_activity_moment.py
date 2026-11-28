#!/usr/bin/env python3
"""Continue one actual interrupted prefix moment from its exact saved interval.

The saved core interval and first 640 actual radial contributions are never
reevaluated. The unchanged original MomentVerifier supplies every remaining
span. Preparation is metadata/Fraction work only; execution requires the
original actual source loader, full grid and exact field-extraction identities.
This entry deliberately accepts only the actual original, no-cut, parts=1 run.
"""
from fractions import Fraction as Q
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
GEO = HERE.parent/'geometry'
SCRIPTS = HERE.parents[1]
REPO = SCRIPTS.parents[2]
ORIGINAL = HERE/'cartesian_third_activity_moment.py'
ORIGINAL_SHA = 'fef214b4b49efb77e4493886431ec125553f842be7a13c3dadd357c0a9a9002e'
SCHEMA = 'actual-original-cartesian-third-moment-partial-sum-resume-v1'


def sha(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            value.update(block)
    return value.hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def verify(record):
    if sha(record['path']) != record['sha256']:
        raise ValueError('A bound actual input changed: '+record['path'])
    return Path(record['path'])


def read_json(path):
    def reject(value):
        raise ValueError('Nonfinite JSON constant: '+value)
    return json.loads(Path(path).read_bytes(), parse_constant=reject)


def save(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.tmp')
    with temporary.open('w') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def output(path):
    path = Path(path).resolve()
    if path == REPO or REPO in path.parents:
        raise ValueError('Keep complete interval data outside Git')
    path.mkdir(parents=True, exist_ok=False)
    return path


def interval_record(values):
    if (not isinstance(values, list) or len(values) != 2
            or not all(type(v) is float and math.isfinite(v) for v in values)
            or values[0] > values[1]):
        raise ValueError('Require the actual finite ordered binary64 interval endpoints')
    return dict(display=values, binary64_hex=[v.hex() for v in values],
                exact_binary_fractions=[str(Q.from_float(v)) for v in values])


def preparation(args):
    out = output(args.outdir)
    terminal_path = args.terminal_record.resolve()
    terminal = read_json(terminal_path)
    if (terminal.get('observed_child_returncode') != -9
            or terminal.get('observed_parent_returncode') != 247
            or terminal.get('actual_process_return_observed') is not True
            or terminal.get('prefix_flux_certified') is not False
            or terminal.get('specific_kill_cause_established') is not False):
        raise ValueError('Require the actual observed original signal9 terminal record')
    process_path = verify(terminal['actual_process'])
    partial_path = verify(terminal['actual_partial_summary'])
    verify(terminal['actual_console'])
    if (verify(terminal['original_entry']).resolve() != ORIGINAL.resolve()
            or terminal['original_entry']['sha256'] != ORIGINAL_SHA):
        raise ValueError('The actual interrupted moment source identity differs')
    process, partial = read_json(process_path), read_json(partial_path)
    if (process.get('returncode') != -9 or process.get('actual_process_return_observed') is not True
            or process.get('source_sha256') != ORIGINAL_SHA
            or partial.get('source_sha256') != ORIGINAL_SHA
            or partial.get('status') != 'continuous_prefix_and_core_moment_running'
            or partial.get('source_kind') != 'actual_original_R53_design'
            or partial.get('core_flux_certified') is not True
            or partial.get('prefix_flux_certified') is not False
            or partial.get('complete_cut_correction_included') is not False):
        raise ValueError('Require the actual saved original no-cut prefix/core interval state')
    command = process['command']
    if ('--radial-parts' not in command or command[command.index('--radial-parts')+1] != '1'
            or '--bundle' in command or '--coupling-summary' in command):
        raise ValueError('This honest resume entry retains the original parts=1, no-cut source')
    table_path = verify(partial['tables'])
    if (verify(terminal['source_tables']).resolve() != table_path.resolve()
            or partial['tables']['sha256'] != process['tables_sha256']):
        raise ValueError('The actual process and saved moment table identity differ')
    table = read_json(table_path)
    if (table.get('status') != 'complete_angular_three_jet_interval_tables'
            or table.get('source_run_sha256') != partial['source_run_sha256']
            or table.get('defining_jets') != partial['defining_jets']
            or table.get('angular_tables') != partial['angular_tables']):
        raise ValueError('The saved cumulative moment and actual complete table differ')
    for path, digest in partial['source_hashes'].items():
        verify(dict(path=path, sha256=digest))
    for key in ('defining_jets', 'angular_tables', 'physical_file'):
        verify(partial[key])
    run_path = verify(dict(path=partial['source_run'], sha256=partial['source_run_sha256']))
    grid_path = verify(terminal['exact_prefix_grid_binding'])
    grid_record = read_json(grid_path)
    if (grid_record.get('status') != 'exact_durable_metric_frontier_prepared_not_executed'
            or grid_record['table_report'] != partial['tables']
            or grid_record['source_run'] != ref(run_path)
            or grid_record['defining_jets'] != partial['defining_jets']
            or grid_record['angular_tables'] != partial['angular_tables']
            or grid_record['physical_file'] != partial['physical_file']):
        raise ValueError('The exact partition binding is for a different actual field')
    verify(grid_record['entry'])
    grid = [Q(value) for value in grid_record['exact_initial_grid']]
    if (len(grid) < 2 or grid[0] != 0 or any(r <= l for l, r in zip(grid[:-1],grid[1:]))
            or [str(grid[0]),str(grid[-1])] != partial['full_prefix_radial_domain_exact']):
        raise ValueError('The full unchanged actual moment domain is not exactly partitioned')
    count = partial['completed_radial_leaves']
    if (type(count) is not int or not 0 < count < len(grid)-1
            or count != terminal['complete_preserved_radial_intervals']
            or [str(grid[0]),str(grid[count])] != terminal['exact_preserved_radial_range']):
        raise ValueError('The saved actual cumulative interval count is not bound to this grid')
    total = interval_record(partial['current_prefix_flux_interval'])
    core = interval_record(partial['core_flux']['real_m3_boundary_flux_interval'])
    if (total['display'] != terminal['preserved_partial_sum']
            or partial['core_flux'] != terminal['complete_core_result_retained']):
        raise ValueError('The actual terminal and saved prefix/core intervals differ')
    record = dict(schema=SCHEMA, status='actual_partial_sum_exact_resume_prepared_not_executed',
        entry=ref(__file__), original_entry=ref(ORIGINAL), terminal_record=ref(terminal_path),
        actual_process=ref(process_path), actual_partial_summary=ref(partial_path),
        actual_console=terminal['actual_console'], table_report=partial['tables'],
        defining_jets=partial['defining_jets'], angular_tables=partial['angular_tables'],
        source_run=ref(run_path), physical_file=partial['physical_file'],
        bound_source_hashes=partial['source_hashes'], exact_grid_binding=ref(grid_path),
        exact_grid_binding_entry=grid_record['entry'], exact_grid=[str(x) for x in grid],
        radial_parts=1, total_original_base_intervals=len(grid)-1,
        inherited_completed_base_intervals=count, remaining_base_intervals=len(grid)-1-count,
        exact_inherited_radial_range=[str(grid[0]),str(grid[count])],
        exact_remaining_radial_range=[str(grid[count]),str(grid[-1])],
        inherited_partial_sum=total, inherited_core_moment=core,
        original_field_extraction=partial['field_extraction'],
        source_kind=partial['source_kind'], complete_cut_correction_included=False,
        inherited_core_recomputed=False, inherited_prefix_intervals_to_recompute=0,
        original_prefix_span_calls=0, original_model_loaded=False,
        prefix_flux_certified=False, core_flux_certified=True, complete_tail_moment_certified=False,
        whole_active_coefficient_certified=False, whole_surface=False,
        full_J_assembled=False, nonlinear_solver_invoked=False,
        specific_parent_kill_cause_established=False,
        numerical_interval_endpoints_preserved_without_reconversion_through_decimal_or_midpoint=True)
    save(out/'prepared.json', record)
    print(json.dumps({key:record[key] for key in ('status','inherited_completed_base_intervals',
        'remaining_base_intervals','exact_inherited_radial_range','inherited_partial_sum')}), flush=True)


def execution(args):
    prepared_path = args.execute_prepared.resolve()
    prepared = read_json(prepared_path)
    if (prepared.get('schema') != SCHEMA
            or prepared.get('status') != 'actual_partial_sum_exact_resume_prepared_not_executed'
            or verify(prepared['entry']).resolve() != Path(__file__).resolve()):
        raise ValueError('Require this frozen exact partial-sum preparation')
    for key in ('original_entry','terminal_record','actual_process','actual_partial_summary',
                'actual_console','table_report','defining_jets','angular_tables','source_run',
                'physical_file','exact_grid_binding','exact_grid_binding_entry'):
        verify(prepared[key])
    for path, digest in prepared['bound_source_hashes'].items():
        verify(dict(path=path, sha256=digest))
    if prepared['radial_parts'] != 1 or prepared['complete_cut_correction_included'] is not False:
        raise ValueError('The original numerical partition or no-cut field changed')
    grid = [Q(value) for value in prepared['exact_grid']]
    start = prepared['inherited_completed_base_intervals']
    partial = read_json(prepared['actual_partial_summary']['path'])
    out = output(args.outdir)
    begun = time.monotonic()
    report = dict(partial)
    report.update(schema=SCHEMA, status='continuous_prefix_moment_resuming_from_actual_sum',
        resume_entry=ref(__file__), preparation=ref(prepared_path),
        inherited_partial_summary=prepared['actual_partial_summary'],
        inherited_completed_base_intervals=start,
        exact_inherited_radial_range=prepared['exact_inherited_radial_range'],
        inherited_partial_sum=prepared['inherited_partial_sum'],
        inherited_core_moment=prepared['inherited_core_moment'],
        inherited_prefix_per_leaf_records_available=False,
        inherited_prefix_and_core_values_recomputed=False,
        new_prefix_span_calls=0, new_completed_base_intervals=0,
        completed_radial_leaves=start, prefix_flux_certified=False, seconds=0.,
        original_J_or_BVP_invoked=False, specific_parent_kill_cause_established=False)
    report['source_hashes'] = dict(report['source_hashes'])
    report['source_hashes'][str(Path(__file__).resolve())] = sha(__file__)
    save(out/'summary.json', report)
    try:
        sys.path[:0] = [str(HERE),str(GEO)]
        import cartesian_third_activity_moment as original
        original.coupled.check_reviewed_algebra()
        verifier = original.metric.NewMetric(prepared['table_report']['path'])
        moment = original.MomentVerifier(verifier, False)
        if (moment.grid != grid or moment.extraction != prepared['original_field_extraction']
                or verifier.record['source_run_sha256'] != partial['source_run_sha256']
                or verifier.N != partial['angular_boxes_per_sector']
                or verifier.record['mean_nodes'] != partial['mean_nodes']):
            raise ValueError('The complete actual original grid/field/mean identity changed')
        def restore(record):
            endpoints = [float.fromhex(value) for value in record['binary64_hex']]
            if interval_record(endpoints) != record:
                raise ValueError('The inherited binary64 interval identity changed')
            value = original.I(*endpoints)
            if [float(x).hex() for x in value.x] != record['binary64_hex']:
                raise AssertionError('Original interval construction changed a saved endpoint')
            return value
        total = restore(prepared['inherited_partial_sum'])
        core = restore(prepared['inherited_core_moment'])
        leaf_path = out/'continued-prefix-moment-leaves.jsonl'
        with leaf_path.open('xb', buffering=0) as leaves:
            for index in range(start,len(grid)-1):
                left, right = grid[index:index+2]
                value, row = moment.prefix_span(left, right)
                report['new_prefix_span_calls'] += 1
                total += value
                cumulative = interval_record(original.display(total))
                payload = dict(original_base_index=index, **row,
                    cumulative_completed_base_intervals=index+1,
                    cumulative_full_prefix_partial_sum=cumulative)
                encoded = (json.dumps(payload, allow_nan=False)+'\n').encode()
                if leaves.write(encoded) != len(encoded):
                    raise IOError('A new complete moment journal row was not written in full')
                os.fsync(leaves.fileno())
                report.update(completed_radial_leaves=index+1,
                    new_completed_base_intervals=index+1-start,
                    current_prefix_flux_interval=original.display(total),
                    current_prefix_flux_binary64=cumulative,
                    exact_current_radial_coverage=[str(grid[0]),str(right)],
                    continued_leaf_bytes=leaves.tell(), seconds=time.monotonic()-begun)
                # Commit every complete new span; a killed process no longer
                # loses the last sixteen cumulative contributions.
                save(out/'summary.json', report)
                if (index+1-start) % 16 == 0:
                    print(json.dumps(dict(stage='resumed_continuous_third_flux',
                        inherited=start, completed=index+1, new_completed=index+1-start,
                        interval=original.display(total), seconds=report['seconds'])), flush=True)
        lines = leaf_path.read_bytes().splitlines(keepends=True)
        if len(lines) != len(grid)-1-start:
            raise AssertionError('The remaining actual moment intervals were not all journaled')
        cursor = grid[start]
        for index, line in enumerate(lines,start):
            if not line.endswith(b'\n'):
                raise AssertionError('A new completed moment row is truncated')
            row = json.loads(line)
            if (row['original_base_index'] != index
                    or row['radial_exact'] != [str(cursor),str(grid[index+1])]
                    or row['cumulative_completed_base_intervals'] != index+1):
                raise AssertionError('Remaining actual moment coverage has a gap or overlap')
            cursor = grid[index+1]
        if (cursor != grid[-1] or report['completed_radial_leaves'] != len(grid)-1
                or row['cumulative_full_prefix_partial_sum'] != interval_record(original.display(total))):
            raise AssertionError('The final same-field cumulative interval identity failed')
        candidates = []
        for length in (Q(1,200),Q(1,100)):
            value = total+original.I.rational(length)*core
            candidates.append(dict(total_inserted_cylinder_length_exact=str(length),
                prefix_plus_cylinder_real_coefficient_interval=original.display(value),
                tail_coefficient_not_included=True, whole_activity_nonzero_certified=False))
        report.update(status='continuous_actual_prefix_and_core_third_flux_enclosed',
            prefix_flux_certified=True, core_flux_certified=True,
            real_prefix_flux_interval=original.display(total),
            real_prefix_flux_separated_from_zero=original.separate_from_zero(total),
            complete_prefix_domain_covered_once=True, radial_leaves=len(grid)-1,
            all_actual_shared_jet_and_repair_joins_retained=True,
            continued_prefix_leaves=ref(leaf_path),
            full_prefix_coverage_evidence=dict(inherited_actual_cumulative_record=prepared['actual_partial_summary'],
                inherited_exact_range=prepared['exact_inherited_radial_range'],
                new_exact_range=prepared['exact_remaining_radial_range'],
                new_complete_leaf_journal=ref(leaf_path),
                original_inherited_per_leaf_list_invented=False),
            candidate_total_cylinder_lengths=candidates,
            tail_bound_available_only_after_actual_same_field_geometry=partial.get(
                'tail_bound_available_only_after_actual_same_field_geometry',
                '4*pi*Z*r_star^5/5, requiring complete injective planar projection, radius identity r=R, |z|<=Z and r_xy<=r_star'),
            complete_tail_moment_certified=False, whole_active_coefficient_certified=False,
            actual_short_cylinder_length_selected=False, euclidean_noncongruence_certified=False,
            complete_surface=False, mathematical_completion=False,
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            seconds=time.monotonic()-begun)
        save(out/'summary.json', report)
        print(json.dumps({key:report[key] for key in ('status','real_prefix_flux_interval',
            'radial_leaves','new_prefix_span_calls','seconds')}), flush=True)
    except Exception as error:
        (out/'exception.txt').write_text(traceback.format_exc())
        report.update(status='moment_interval_resume_execution_failed', error=repr(error),
            prefix_flux_certified=False, seconds=time.monotonic()-begun)
        save(out/'summary.json', report)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--terminal-record',type=Path)
    group.add_argument('--execute-prepared',type=Path)
    parser.add_argument('--outdir',type=Path,required=True)
    args = parser.parse_args()
    if args.terminal_record is not None:
        preparation(args)
    else:
        execution(args)


if __name__ == '__main__':
    main()
