#!/usr/bin/env python3
"""Resume the interrupted, hash-bound ORIGINAL Cartesian metric coverage.

Only newline-terminated actual accepted leaves are inherited, byte for byte.
Their exact dyadic positions reconstruct the original depth-first frontier;
no accepted enclosure is recomputed. The original NewMetric.enclose, target,
depth limit and cell limit are unchanged. Preparation builds no metric model
and evaluates no interval. Actual execution still passes the original loader.
"""
from bisect import bisect_right
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
SCRIPTS = HERE.parents[1]
REPO = SCRIPTS.parents[2]
ORIGINAL = HERE / 'cartesian_prefix_metric.py'
ORIGINAL_SHA = '935dc0ec201161396e11d25ace0de29e456e2c713618b1469cb78d1cea004ab3'
SCHEMA = 'actual-original-cartesian-metric-durable-leaf-resume-v1'
TARGET = float('9.9e-7')
MAX_CELLS = 150000
MAX_DEPTH = 28
META = ('radius_lower', 'rho_lower', 'point_operator', 'radial_first',
        'radial_second', 'angular_second', 'radial_taylor_upper',
        'angular_interpolation_upper')


def sha(path):
    result = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            result.update(block)
    return result.hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def verify(record):
    if sha(record['path']) != record['sha256']:
        raise ValueError('A bound actual input changed: ' + record['path'])
    return Path(record['path'])


def read_json(path):
    def reject(value):
        raise ValueError('Nonfinite JSON constant: ' + value)
    return json.loads(Path(path).read_bytes(), parse_constant=reject)


def save(path, value):
    path = Path(path)
    temp = path.with_name(path.name + '.tmp')
    with temp.open('w') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)


def output_directory(path):
    path = Path(path).resolve()
    if path == REPO or REPO in path.parents:
        raise ValueError('Keep complete certificate arrays outside Git')
    path.mkdir(parents=True, exist_ok=False)
    return path


def original_grid(summary, table, run):
    """Reconstruct ONLY the literal partition; actual execution checks NewMetric."""
    import numpy as np
    definition = summary['exact_target_definition']
    entry, end = Q(definition['prefix_end_exact']), Q(definition['end_exact'])
    phase = definition['bridge_phase']
    patch = Q(definition['patch_length_exact'])
    if patch != Q(1, 1000):
        raise ValueError('The original exact target patch changed')
    spec = run['frozen_profile']['multistage_flat']
    eta = Q(spec['eta'])
    reference = [tuple(map(Q, row)) for name in ('up', 'down') for row in spec[name]]
    total = sum((row[2] for row in reference), Q(0))
    if total <= 0 or not 0 < eta < Q(1, 2):
        raise ValueError('Invalid original exact profile partition')
    duration, cursor = entry / total, Q(0)
    points = [Q(0), entry, end, end-patch,
              entry+Q(phase['L1']), entry+Q(phase['L1'])+Q(phase['L2'])]
    for v0, v1, length in reference:
        if length <= 0:
            raise ValueError('Nonpositive original profile piece')
        zones = (Q(0), Q(1)) if v0 == v1 else (Q(0), eta, 1-eta, Q(1))
        points.extend(duration*(cursor+length*z) for z in zones)
        cursor += length
    with np.load(table['defining_jets']['path'], allow_pickle=False) as data:
        knots = data['knots'].copy()
        center = data['center_width'].copy()
    if (knots.ndim != 1 or not np.all(np.isfinite(knots))
            or np.any(np.diff(knots) <= 0) or not np.isfinite(center).all()):
        raise ValueError('The actual common Cartesian partition is invalid')
    knots = [Q.from_float(float(x)) for x in knots]
    if knots[0] != 0 or knots[-1] != end:
        raise ValueError('The actual defining field and recorded target differ')
    grid = sorted(set(points+knots+[Q.from_float(float(center))]))
    if grid[0] != 0 or grid[-1] != end or len(grid)-1 != summary['initial_radial_cells']:
        raise ValueError('The reconstructed original complete partition differs')
    return grid


def complete_rows(data):
    """A trailing fragment, even parseable JSON, is not a completed journal row."""
    cut = data.rfind(b'\n')+1
    prefix, fragment = data[:cut], data[cut:]
    rows = []
    cursor = Q(0)
    for number, line in enumerate(prefix.splitlines(keepends=True), 1):
        if not line.endswith(b'\n'):
            raise ValueError('Interior journal row is not newline terminated')
        row = json.loads(line, parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))
        left, right = Q(row['left']), Q(row['right'])
        if str(left) != row['left'] or str(right) != row['right']:
            raise ValueError('The actual journal must retain canonical exact Fractions')
        if left != cursor or not left < right:
            raise ValueError('A completed actual leaf overlaps, leaves a gap, or reverses')
        values = [row['bound']]+[row[key] for key in META]
        if not all(type(value) in (int, float) and math.isfinite(value) for value in values):
            raise ValueError('A completed actual leaf has a nonfinite certificate value')
        if (not 0 <= row['bound'] <= TARGET or row['radius_lower'] <= 0
                or row['rho_lower'] <= 0 or any(row[key] < 0 for key in META[2:])):
            raise ValueError('An inherited leaf did not pass the original metric/domain gates')
        rows.append(row)
        cursor = right
    if not rows:
        raise ValueError('No complete actual accepted leaves were preserved')
    return rows, prefix, fragment


def frontier(grid, rows):
    """Replay only exact subdivision identities, never a numerical enclosure."""
    pending = [(l, r, 0) for l, r in zip(grid[:-1], grid[1:])][::-1]
    splits = 0
    for row in rows:
        left, right = Q(row['left']), Q(row['right'])
        base = bisect_right(grid, left)-1
        if not 0 <= base < len(grid)-1 or right > grid[base+1]:
            raise ValueError('A durable leaf crosses an original exact partition join')
        ratio = (grid[base+1]-grid[base])/(right-left)
        index = (left-grid[base])/(right-left)
        if (ratio.denominator != 1 or ratio <= 0
                or ratio.numerator & (ratio.numerator-1)
                or index.denominator != 1 or not 0 <= index < ratio
                or ratio.numerator.bit_length()-1 > MAX_DEPTH):
            raise ValueError('A durable leaf is not an original depth-limited dyadic cell')
        while True:
            if not pending:
                raise ValueError('The actual journal extends beyond the target domain')
            l, r, depth = pending.pop()
            if l != left or right > r:
                raise ValueError('Completed leaves do not follow the original DFS order')
            if r == right:
                break
            middle = (l+r)/2
            if right > middle or depth >= MAX_DEPTH:
                raise ValueError('An inherited dyadic leaf cannot be reached by the original split')
            pending.extend([(middle, r, depth+1), (l, middle, depth+1)])
            splits += 1
    cursor = Q(rows[-1]['right'])
    for left, right, depth in reversed(pending):
        if left != cursor or not left < right or not 0 <= depth <= MAX_DEPTH:
            raise AssertionError('The exact remaining frontier is not a single complete cover')
        cursor = right
    if cursor != grid[-1]:
        raise AssertionError('The remaining frontier does not end at the true target endpoint')
    return pending, splits


def accumulated(rows):
    result = dict(accepted=len(rows), peak=0., radius_lower=None, rho_lower=None)
    for row in rows:
        if row['bound'] > result['peak']:
            result.update(peak=row['bound'], peak_interval=[float(Q(row['left'])), float(Q(row['right']))],
                          peak_details={key:row[key] for key in META})
        for key in ('radius_lower', 'rho_lower'):
            result[key] = row[key] if result[key] is None else min(result[key], row[key])
    return result


def stack_json(pending):
    return [dict(left=str(l), right=str(r), depth=d) for l, r, d in pending]


def prepare(args):
    out = output_directory(args.outdir)
    summary_path, terminal_path = args.partial_summary.resolve(), args.termination_record.resolve()
    summary, terminal = read_json(summary_path), read_json(terminal_path)
    if (summary.get('status') != 'continuous_metric_running'
            or summary.get('metric_certified') is not False
            or summary.get('whole_surface') is not False or summary['target'] != TARGET):
        raise ValueError('Require the actual interrupted original metric report with its original target')
    if (terminal.get('observed_returncode') != 137
            or terminal.get('complete_metric_certified') is not False
            or terminal.get('specific_kill_cause_established') is not False):
        raise ValueError('Require the observed original exit137 record, without an invented cause')
    if (verify(terminal['partial_summary']).resolve() != summary_path
            or verify(terminal['source']).resolve() != ORIGINAL.resolve()
            or terminal['source']['sha256'] != ORIGINAL_SHA
            or summary['source_hashes'].get(str(ORIGINAL.resolve())) != ORIGINAL_SHA):
        raise ValueError('The terminal record does not bind this actual original execution')
    verify(terminal['console'])
    shell = terminal['observed_shell_message']
    if '--target 9.9e-7 --max-cells 150000' not in shell:
        raise ValueError('The actual original target and cell cap are not bound by its command')
    leaves_path = verify(terminal['actual_leaves']).resolve()
    table_path = Path(summary['table_report']).resolve()
    if sha(table_path) != summary['table_report_sha256']:
        raise ValueError('The original actual table report changed')
    table = read_json(table_path)
    if (table.get('status') != 'complete_angular_three_jet_interval_tables'
            or table.get('right_sector_endpoint_gram_equals_left_exactly') is not True
            or table['source_run_sha256'] != summary['source_run_sha256']
            or table['defining_jets'] != summary['defining_jets']
            or table['angular_boxes_per_sector'] != summary['angular_boxes_per_sector']):
        raise ValueError('The original partial metric and complete actual table disagree')
    bound = dict(summary['source_hashes'])
    for path, digest in table['source_hashes'].items():
        if path in bound and bound[path] != digest:
            raise ValueError('The bound source identities disagree')
        bound[path] = digest
    for path, digest in bound.items():
        verify(dict(path=path, sha256=digest))
    for name in ('defining_jets', 'angular_tables'):
        verify(table[name])
    run_path = verify(dict(path=table['source_run'], sha256=table['source_run_sha256']))
    run = read_json(run_path)
    physical = dict(path=str(run_path.parent/'physical.npz'), sha256=table['physical_sha256'])
    verify(physical)
    grid = original_grid(summary, table, run)
    data = leaves_path.read_bytes()
    rows, prefix, fragment = complete_rows(data)
    pending, splits = frontier(grid, rows)
    if not pending:
        raise ValueError('No unresolved exact radial interval remains; do not rerun coverage')
    inherited = accumulated(rows)
    if len(rows) >= summary['accepted']:
        snapshot = accumulated(rows[:summary['accepted']])
        for key in ('peak', 'radius_lower', 'rho_lower', 'peak_interval', 'peak_details'):
            if snapshot.get(key) != summary.get(key):
                raise ValueError('The earlier report snapshot disagrees with its durable actual leaves')
    record = dict(schema=SCHEMA, status='exact_durable_metric_frontier_prepared_not_executed',
        entry=ref(__file__), original_source=ref(ORIGINAL), partial_summary=ref(summary_path),
        termination_record=ref(terminal_path), actual_leaves=ref(leaves_path),
        original_console=terminal['console'], table_report=ref(table_path), source_run=ref(run_path),
        physical_file=physical, defining_jets=table['defining_jets'], angular_tables=table['angular_tables'],
        bound_source_hashes=bound, target=TARGET, max_cells=MAX_CELLS, max_depth=MAX_DEPTH,
        exact_target_definition=summary['exact_target_definition'],
        exact_initial_grid=[str(x) for x in grid], original_initial_cells=len(grid)-1,
        complete_durable_leaves=len(rows), inherited_accumulated=inherited,
        inherited_prefix_bytes=len(prefix), inherited_prefix_sha256=hashlib.sha256(prefix).hexdigest(),
        trailing_incomplete_fragment_bytes=len(fragment),
        trailing_incomplete_fragment_sha256=hashlib.sha256(fragment).hexdigest(),
        trailing_fragment_is_never_an_accepted_leaf=True,
        source_last_reported_counters={key:summary[key] for key in ('accepted', 'splits', 'attempts', 'seconds')},
        minimum_subdivision_splits_implied_by_durable_leaves=splits,
        reconstructed_traversal_events=len(rows)+splits,
        reconstructed_counts_are_not_claimed_actual_process_totals=True,
        exact_covered_prefix=['0', rows[-1]['right']], exact_remaining_stack=stack_json(pending),
        remaining_frontier_cells=len(pending), completed_and_remaining_cover_once_without_gaps=True,
        original_leaf_values_and_original_depths_preserved=True,
        original_model_loaded=False, original_enclose_calls=0, full_J_assembled=False,
        nonlinear_solver_invoked=False, metric_certified=False, whole_surface=False,
        original_exit137_observed=True, specific_kill_cause_established=False,
        original_accepted_leaves_to_recompute=0, original_bound_sources_modified=False)
    save(out/'prepared.json', record)
    print(json.dumps({key:record[key] for key in ('status', 'complete_durable_leaves',
        'remaining_frontier_cells', 'exact_covered_prefix', 'inherited_prefix_sha256')}), flush=True)


def execute(args):
    preparation_path = args.execute_prepared.resolve()
    prepared = read_json(preparation_path)
    if prepared.get('schema') != SCHEMA or prepared.get('status') != 'exact_durable_metric_frontier_prepared_not_executed':
        raise ValueError('Require the exact completed preparation record')
    if verify(prepared['entry']).resolve() != Path(__file__).resolve():
        raise ValueError('This is not the frozen prepared resume entry')
    for name in ('original_source', 'partial_summary', 'termination_record', 'actual_leaves',
                 'original_console', 'table_report', 'source_run', 'physical_file',
                 'defining_jets', 'angular_tables'):
        verify(prepared[name])
    for path, digest in prepared['bound_source_hashes'].items():
        verify(dict(path=path, sha256=digest))
    if (prepared['target'], prepared['max_cells'], prepared['max_depth']) != (TARGET, MAX_CELLS, MAX_DEPTH):
        raise ValueError('The original numerical acceptance gates changed')
    grid = list(map(Q, prepared['exact_initial_grid']))
    rows, prefix, fragment = complete_rows(Path(prepared['actual_leaves']['path']).read_bytes())
    pending, splits = frontier(grid, rows)
    if (stack_json(pending) != prepared['exact_remaining_stack']
            or len(rows) != prepared['complete_durable_leaves']
            or hashlib.sha256(prefix).hexdigest() != prepared['inherited_prefix_sha256']
            or accumulated(rows) != prepared['inherited_accumulated']):
        raise ValueError('The actual durable frontier changed after preparation')
    out = output_directory(args.outdir)
    started = time.monotonic()
    report = read_json(prepared['partial_summary']['path'])
    report.update(schema=SCHEMA, status='continuous_metric_resuming', resume_entry=ref(__file__),
        preparation=ref(preparation_path), actual_parent_termination=prepared['termination_record'],
        inherited_actual_leaves=prepared['actual_leaves'], inherited_complete_leaves=len(rows),
        inherited_prefix_bytes=len(prefix), inherited_prefix_sha256=prepared['inherited_prefix_sha256'],
        trailing_incomplete_fragment_bytes=len(fragment), original_accepted_leaves_recomputed=0,
        source_last_reported_counters=prepared['source_last_reported_counters'],
        minimum_subdivision_splits_implied_by_durable_leaves=splits,
        reconstructed_traversal_events=len(rows)+splits,
        reconstructed_counts_are_not_claimed_actual_process_totals=True,
        new_enclosure_attempts=0, new_accepted_leaves=0, new_splits=0,
        attempts=len(rows)+splits, splits=splits, metric_certified=False, whole_surface=False,
        specific_parent_kill_cause_established=False, full_J_assembled=False,
        all_original_numeric_gates_unchanged=True, **accumulated(rows))
    report['source_hashes'] = dict(report['source_hashes'], **{str(Path(__file__).resolve()):sha(__file__)})
    save(out/'summary.json', report)
    try:
        import cartesian_prefix_metric as original
        verifier = original.NewMetric(prepared['table_report']['path'])
        if (verifier.grid != grid or verifier.target.definition != prepared['exact_target_definition']
                or verifier.N != report['angular_boxes_per_sector']
                or verifier.record['source_run_sha256'] != report['source_run_sha256']):
            raise ValueError('The unchanged actual original loader disagrees with the prepared partition/source')
        leaf_path = out/'complete-leaves.jsonl'
        with leaf_path.open('xb') as stream:
            stream.write(prefix)
            stream.flush()
            os.fsync(stream.fileno())
        if sha(leaf_path) != prepared['inherited_prefix_sha256']:
            raise IOError('The inherited complete prefix bytes were not preserved')
        if fragment:
            (out/'excluded-uncompleted-parent-fragment.bin').write_bytes(fragment)
        save(out/'remaining-stack.json', dict(exact_pending_stack=stack_json(pending),
            completed_leaves=report['accepted'], first_remaining_left=str(pending[-1][0])))
        with leaf_path.open('ab', buffering=0) as leaves:
            while pending:
                left, right, depth = pending.pop()
                report['attempts'] += 1
                report['new_enclosure_attempts'] += 1
                upper, meta = verifier.enclose(left, right)
                if upper <= TARGET:
                    row = dict(left=str(left), right=str(right), bound=upper, **meta)
                    leaves.write((json.dumps(row, allow_nan=False)+'\n').encode())
                    os.fsync(leaves.fileno())
                    report['accepted'] += 1
                    report['new_accepted_leaves'] += 1
                    if upper > report['peak']:
                        report.update(peak=upper, peak_interval=[float(left),float(right)], peak_details=meta)
                    for key in ('radius_lower', 'rho_lower'):
                        report[key] = min(report[key], meta[key])
                else:
                    if depth >= MAX_DEPTH or report['accepted']+len(pending) >= MAX_CELLS:
                        report.update(status='continuous_metric_unresolved', remaining=len(pending)+1,
                            unresolved_interval=[float(left),float(right)], unresolved_details=meta,
                            unresolved_depth=depth, last_bound=upper)
                        pending.append((left, right, depth))
                        break
                    middle = (left+right)/2
                    pending.extend([(middle,right,depth+1),(left,middle,depth+1)])
                    report['splits'] += 1
                    report['new_splits'] += 1
                save(out/'remaining-stack.json', dict(exact_pending_stack=stack_json(pending),
                    completed_leaves=report['accepted'], new_enclosure_attempts=report['new_enclosure_attempts']))
                if report['new_enclosure_attempts'] % 50 == 0:
                    report.update(seconds=time.monotonic()-started, remaining=len(pending))
                    save(out/'summary.json', report)
                    print(json.dumps(dict(stage='resumed_original_continuous_metric',
                        accepted=report['accepted'], new_attempts=report['new_enclosure_attempts'],
                        new_splits=report['new_splits'], remaining=len(pending),
                        s=float(right), peak=report['peak'], seconds=report['seconds'])), flush=True)
            else:
                all_rows, all_bytes, remainder = complete_rows(leaf_path.read_bytes())
                final_pending, final_splits = frontier(grid, all_rows)
                if (remainder or final_pending or len(all_rows) != report['accepted']
                        or all_bytes[:len(prefix)] != prefix
                        or accumulated(all_rows) != {key:report[key] for key in accumulated(all_rows)}):
                    raise AssertionError('Final exact actual leaf coverage or byte inheritance failed')
                report.update(status='continuous_new_cartesian_prefix_metric_certified', metric_certified=True,
                    full_radial_range=[str(grid[0]),str(grid[-1])],
                    full_angular_range='[0,2*pi], by exact threefold covariance', all_phase_prefix_metric=True,
                    phase_reason='Rotation and material-angle translation preserve the frozen radial target metric',
                    complete_actual_leaf_cover_verified_once=True, inherited_prefix_bytes_equal=True,
                    final_splits_implied_by_complete_leaf_tree=final_splits)
        report.update(seconds=time.monotonic()-started, complete_leaves_sha256=sha(leaf_path),
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save(out/'summary.json', report)
        print(json.dumps({key:report[key] for key in ('status','accepted','new_enclosure_attempts',
            'new_accepted_leaves','new_splits','peak','seconds')}), flush=True)
    except Exception as error:
        (out/'exception.txt').write_text(traceback.format_exc())
        report.update(status='continuous_metric_resume_execution_failed', metric_certified=False,
            error=repr(error), seconds=time.monotonic()-started)
        save(out/'summary.json', report)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--partial-summary', type=Path)
    group.add_argument('--execute-prepared', type=Path)
    parser.add_argument('--termination-record', type=Path)
    parser.add_argument('--outdir', type=Path, required=True)
    args = parser.parse_args()
    if args.partial_summary is not None:
        if args.termination_record is None:
            parser.error('--partial-summary requires --termination-record')
        prepare(args)
    else:
        if args.termination_record is not None:
            parser.error('The frozen preparation already binds the actual terminal record')
        execute(args)


if __name__ == '__main__':
    main()
