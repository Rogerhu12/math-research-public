#!/usr/bin/env python3
"""Continue one actual interrupted prefix moment from its exact saved interval.

The saved core interval and all 976 actual radial contributions are never
reevaluated. The original 640-value record and 336 complete continuation
journal rows form one explicitly verified provenance chain. The unchanged original MomentVerifier supplies every remaining
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
PREVIOUS = HERE/'resume_cartesian_third_activity_moment.py'
PREVIOUS_SHA = 'd2824688e98cf51acfe60971b42ece3b1e13db97ad5efee4f19bb8b0e72e9436'
PREVIOUS_SCHEMA = 'actual-original-cartesian-third-moment-partial-sum-resume-v1'
SCHEMA = 'actual-original-cartesian-third-moment-partial-sum-resume-v2'


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
        raise ValueError('Require the actual observed resumed signal9 terminal record')
    process_path = verify(terminal['actual_process'])
    partial_path = verify(terminal['actual_partial_summary'])
    verify(terminal['actual_console'])
    previous_path = verify(terminal['previous_preparation'])
    process, partial = read_json(process_path), read_json(partial_path)
    previous = read_json(previous_path)
    if (verify(terminal['original_entry']).resolve() != ORIGINAL.resolve()
            or terminal['original_entry']['sha256'] != ORIGINAL_SHA
            or verify(terminal['resume_entry']).resolve() != PREVIOUS.resolve()
            or terminal['resume_entry']['sha256'] != PREVIOUS_SHA
            or previous.get('schema') != PREVIOUS_SCHEMA
            or previous.get('status') != 'actual_partial_sum_exact_resume_prepared_not_executed'
            or previous['entry'] != terminal['resume_entry']
            or previous['original_entry'] != terminal['original_entry']):
        raise ValueError('The actual original/resume/preparation source chain differs')
    history = {key:previous[key] for key in ('entry','original_entry','terminal_record',
        'actual_process','actual_partial_summary','actual_console','table_report',
        'defining_jets','angular_tables','source_run','physical_file','exact_grid_binding',
        'exact_grid_binding_entry')}
    for record in history.values():
        verify(record)
    for path, digest in previous['bound_source_hashes'].items():
        verify(dict(path=path, sha256=digest))
    if (process.get('returncode') != -9 or process.get('actual_child_return_observed') is not True
            or process.get('entry_sha256') != PREVIOUS_SHA
            or process.get('prepared_sha256') != sha(previous_path)
            or process.get('actual_summary') != ref(partial_path)
            or partial.get('schema') != PREVIOUS_SCHEMA
            or partial.get('source_sha256') != ORIGINAL_SHA
            or partial.get('resume_entry') != terminal['resume_entry']
            or partial.get('preparation') != ref(previous_path)
            or partial.get('status') != 'continuous_prefix_moment_resuming_from_actual_sum'
            or partial.get('core_flux_certified') is not True
            or partial.get('prefix_flux_certified') is not False
            or partial.get('complete_cut_correction_included') is not False
            or previous['radial_parts'] != 1
            or previous['source_kind'] != 'actual_original_R53_design'):
        raise ValueError('Require the actual interrupted same-field v1 continuation')
    command = process['command']
    if ('--execute-prepared' not in command
            or Path(command[command.index('--execute-prepared')+1]).resolve() != previous_path
            or '--bundle' in command or '--coupling-summary' in command):
        raise ValueError('The actual process did not consume its bound preparation')
    original_partial = read_json(previous['actual_partial_summary']['path'])
    for key in ('source_sha256','source_kind','tables','defining_jets','angular_tables',
                'source_run','source_run_sha256','physical_file','physical_sha256','mean_nodes',
                'modes','homotopy','angular_boxes_per_sector','field_extraction','core_flux',
                'complete_cut_correction_included','full_prefix_radial_domain_exact'):
        if partial[key] != original_partial[key]:
            raise ValueError('The same actual field/core identity changed: '+key)
    expected_sources = dict(previous['bound_source_hashes'])
    expected_sources[str(PREVIOUS.resolve())] = PREVIOUS_SHA
    if (partial['source_hashes'] != expected_sources
            or partial['inherited_partial_summary'] != previous['actual_partial_summary']
            or partial['inherited_partial_sum'] != previous['inherited_partial_sum']
            or partial['inherited_core_moment'] != previous['inherited_core_moment']
            or terminal['source_tables'] != previous['table_report']
            or terminal['exact_prefix_grid_binding'] != previous['exact_grid_binding']):
        raise ValueError('The original cumulative record or full source binding changed')
    for path, digest in expected_sources.items():
        verify(dict(path=path, sha256=digest))
    grid = [Q(value) for value in previous['exact_grid']]
    prior_count = previous['inherited_completed_base_intervals']
    count = partial['completed_radial_leaves']
    if (type(count) is not int or not prior_count < count < len(grid)-1
            or count != terminal['complete_preserved_radial_intervals']
            or partial['inherited_completed_base_intervals'] != prior_count
            or partial['new_completed_base_intervals'] != count-prior_count
            or partial['new_prefix_span_calls'] != count-prior_count
            or partial['exact_current_radial_coverage'] != [str(grid[0]),str(grid[count])]
            or terminal['exact_preserved_radial_range'] != partial['exact_current_radial_coverage']):
        raise ValueError('The actual continuation count/domain is inconsistent')
    leaf_path = verify(terminal['preserved_complete_leaf_journal'])
    raw = leaf_path.read_bytes()
    lines = raw.splitlines(keepends=True)
    if (len(lines) != count-prior_count or any(not line.endswith(b'\n') for line in lines)
            or len(raw) != partial['continued_leaf_bytes']
            or len(lines) != terminal['preserved_complete_leaf_journal_lines']
            or terminal['truncated_journal_tail_bytes'] != 0):
        raise ValueError('Require every actual complete journal row, without a truncated tail')
    cumulative = previous['inherited_partial_sum']
    for index, line in enumerate(lines,prior_count):
        row = json.loads(line)
        if (row['original_base_index'] != index
                or row['radial_exact'] != [str(grid[index]),str(grid[index+1])]
                or row['cumulative_completed_base_intervals'] != index+1
                or row['includes_full_finite_mean'] is not True
                or row['includes_core_lift_and_center'] is not True
                or row['sampled_maximum_substituted_for_continuous_bound'] is not False):
            raise ValueError('The durable original-grid coverage or full-field row contract differs')
        value = interval_record(row['full_circle_two_reflected_prefix_flux_interval'])
        next_sum = row['cumulative_full_prefix_partial_sum']
        if interval_record(next_sum['display']) != next_sum:
            raise ValueError('A saved cumulative binary64 identity differs')
        before = [Q(x) for x in cumulative['exact_binary_fractions']]
        increment = [Q(x) for x in value['exact_binary_fractions']]
        after = [Q(x) for x in next_sum['exact_binary_fractions']]
        if not (after[0] <= before[0]+increment[0] and after[1] >= before[1]+increment[1]):
            raise ValueError('A saved cumulative interval does not enclose its exact prior sum')
        cumulative = next_sum
    total = interval_record(partial['current_prefix_flux_interval'])
    if (cumulative != total or partial['current_prefix_flux_binary64'] != total
            or terminal['preserved_partial_sum_binary64'] != total
            or terminal['preserved_partial_sum'] != total['display']
            or partial['core_flux'] != terminal['complete_core_result_retained']):
        raise ValueError('The last durable journal and actual saved prefix/core intervals differ')
    record = dict(previous)
    record.update(schema=SCHEMA, entry=ref(__file__), terminal_record=ref(terminal_path),
        actual_process=ref(process_path), actual_partial_summary=ref(partial_path),
        actual_console=terminal['actual_console'], bound_source_hashes=expected_sources,
        inherited_resume_preparation=ref(previous_path), inherited_provenance_references=history,
        inherited_complete_leaf_journal=ref(leaf_path),
        inherited_journaled_complete_base_intervals=count-prior_count,
        inherited_original_unjournaled_base_intervals=prior_count,
        inherited_completed_base_intervals=count, remaining_base_intervals=len(grid)-1-count,
        exact_inherited_radial_range=[str(grid[0]),str(grid[count])],
        exact_remaining_radial_range=[str(grid[count]),str(grid[-1])],
        inherited_partial_sum=total, inherited_core_moment=previous['inherited_core_moment'],
        inherited_complete_rows_exactly_cover_once=True,
        inherited_cumulative_additions_enclosed_by_exact_fraction_checks=True,
        inherited_journal_tail_bytes_excluded=0)
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
    verify(prepared['inherited_resume_preparation'])
    verify(prepared['inherited_complete_leaf_journal'])
    for record in prepared['inherited_provenance_references'].values():
        verify(record)
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
        inherited_original_unjournaled_base_intervals=prepared['inherited_original_unjournaled_base_intervals'],
        inherited_complete_leaf_journals=[prepared['inherited_complete_leaf_journal']],
        inherited_resume_preparation=prepared['inherited_resume_preparation'],
        inherited_provenance_references=prepared['inherited_provenance_references'],
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
                inherited_complete_leaf_journals=[prepared['inherited_complete_leaf_journal']],
                inherited_resume_preparation=prepared['inherited_resume_preparation'],
                inherited_provenance_references=prepared['inherited_provenance_references'],
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
