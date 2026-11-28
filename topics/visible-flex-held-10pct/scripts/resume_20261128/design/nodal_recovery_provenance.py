"""Bind a real unaccepted nodal recovery through every prior restart link.

An original two-source initializer is provenance, not the field to replay.
The returned initializer is the latest requested full nodal checkpoint of
the closed original target run. Each intermediate run, checkpoint journal,
literal-restoration record, source and input hash is checked. No accepted
run or predictor record is fabricated and no completed Newton path is rerun.
"""
import hashlib
import json
from pathlib import Path

import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def option(run, flag):
    command = run['command']
    if command.count(flag) != 1:
        raise ValueError('The actual original command has no unique '+flag)
    return command[command.index(flag)+1]


def _hashes(record):
    for filename, expected in record.items():
        if sha(filename) != expected:
            raise ValueError('A bound original input or source changed: '+filename)


def _checkpoint(run_path, node_path, *, latest):
    pointer_path = run_path.parent/'latest-unaccepted-nodal-checkpoint.json'
    if latest:
        row = json.loads(pointer_path.read_text())
    else:
        rows = [json.loads(line) for line in
                (run_path.parent/'nodal-checkpoints.jsonl').read_text().splitlines()]
        matches = [row for row in rows if run_path.parent/row['file'] == node_path]
        if len(matches) != 1:
            raise ValueError('The prior raw input is not a unique actual complete nodal checkpoint')
        row = matches[0]
    if (run_path.parent/row['file'] != node_path or sha(node_path) != row['sha256']
            or row['accepted_bvp'] is not False or row['before_full_J_assembly'] is not True):
        raise ValueError('The actual unaccepted full nodal checkpoint changed')
    _hashes(row['original_source_hashes'])
    return row, pointer_path


def recover(first_initializer, run_path, node_path):
    run_path, node_path = Path(run_path).resolve(), Path(node_path).resolve()
    first = dict(first_initializer)
    initial = dict(first['result'])
    original_raw = Path(initial['initial_raw']).resolve()
    source = json.loads(Path(first['right_run']).read_text())
    expected_core = dict(source['core_settings'], homotopy=first['target_lambda'])
    comparable = ('physical_profile', 'physical_tail_parameters', 'physical_tail_cut',
                  'angular_chart', 'gauge_q', 'warp_reference', 'gates')
    latest, pointer_path = _checkpoint(run_path, node_path, latest=True)
    if (latest['parameters'] != first['modes']
            or latest['state_components'] != 3*first['modes']+1):
        raise ValueError('The requested full nodal target dimensions differ')
    with np.load(node_path, allow_pickle=False) as raw:
        x, y, p, scale = (raw[key].copy() for key in ('x', 'y', 'p', 'pscale'))
    M = first['modes']
    if (x.ndim != 1 or len(x) != latest['nodes'] or x[0] != 0 or x[-1] != 1
            or np.any(np.diff(x) <= 0) or y.shape != (3*M+1, len(x))
            or p.shape != (M,) or scale.shape != (M-1,)
            or np.any(scale <= 0) or not all(np.all(np.isfinite(v)) for v in (x,y,p,scale))):
        raise ValueError('The requested actual full nodal arrays fail their representation contract')
    links, visited = [], set()
    current = run_path
    for depth in range(32):
        if current in visited:
            raise ValueError('A cycle appeared in the actual nodal recovery provenance')
        visited.add(current)
        run = json.loads(current.read_text())
        if (run.get('solver_success') is True or run['fixed_metric_refinement'] is not False
                or run['actual_tail_requested'] is not False
                or run['modes'] != M or run['angular'] != first['angular']
                or run['core_settings'] != expected_core
                or not all(run[key] == source[key] for key in comparable)
                or not np.array_equal(np.asarray(run['parameter_scales']), scale)):
            raise ValueError('A recovered run differs from the bound original target equation')
        for group in ('inputs', 'source_hashes'):
            _hashes(run[group])
        if sha(option(run, '--port')) != initial['port_sha256']:
            raise ValueError('The recovered original physical port changed')
        raw_path = Path(option(run, '--raw-restart')).resolve()
        row = dict(run=str(current), run_sha256=sha(current),
                   actual_raw_input=str(raw_path), actual_raw_input_sha256=sha(raw_path))
        trace = current.parent.parent.with_name(current.parent.parent.name+'-dispatch-execution.jsonl')
        if not trace.is_file():
            raise ValueError('The prior actual execution source binding is unavailable')
        trace_rows = [json.loads(line) for line in trace.read_text().splitlines()]
        begin = [entry for entry in trace_rows if entry.get('event') == 'execution_begin']
        if len(begin) != 1:
            raise ValueError('The prior execution has no unique source binding')
        _hashes(begin[0]['source_hashes'])
        row.update(prior_execution_trace=str(trace), prior_execution_trace_sha256=sha(trace))
        links.append(row)
        if raw_path == original_raw:
            if row['actual_raw_input_sha256'] != initial['initial_raw_sha256']:
                raise ValueError('The original complete two-source initializer changed')
            break
        literal_path = current.parent/'literal-full-design-nodal-restart.json'
        literal = json.loads(literal_path.read_text())
        if (Path(literal['checkpoint']).resolve() != raw_path
                or literal['checkpoint_sha256'] != sha(raw_path)
                or literal['all_complete_nodal_arrays_restored_bitwise'] is not True
                or literal['accepted_bvp'] is not False):
            raise ValueError('A prior literal nodal recovery link is not bound to the actual raw input')
        parent_run = raw_path.parent/'run.json'
        prior_node, _ = _checkpoint(parent_run, raw_path, latest=False)
        row.update(literal_record=str(literal_path), literal_record_sha256=sha(literal_path),
                   prior_checkpoint_ordinal=prior_node['checkpoint_ordinal'])
        current = parent_run
    else:
        raise ValueError('Actual nodal recovery provenance exceeds the explicit depth limit')
    first['prior_two_source_initializer_result'] = initial
    first['result'] = dict(initial, initial_raw=str(node_path), initial_raw_sha256=sha(node_path))
    first.update(record_kind='unaccepted_complete_nodal_recovery_after_engineering_interrupt',
        prior_unaccepted_run=str(run_path), prior_unaccepted_run_sha256=sha(run_path),
        nodal_pointer=str(pointer_path), nodal_pointer_sha256=sha(pointer_path),
        recovered_checkpoint_ordinal=latest['checkpoint_ordinal'],
        recovered_nodes=len(x), complete_prior_restart_links=links,
        literal_complete_nodal_checkpoint=True,
        original_two_source_field_replayed=False,
        mathematical_failure_inferred=False)
    return first
