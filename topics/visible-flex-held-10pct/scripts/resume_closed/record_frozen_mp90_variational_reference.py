#!/usr/bin/env python3
"""Read-only terminal binding for the saved MP90 variational execution.

No evaluator, numerical library, nonlinear flow, root, derivative, tail or BVP
is imported or run. The exact decimal matrix entries are read only to check
shape, finiteness, serialization identity and the separately stored checkpoints.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[4]
RUN = WORK / 'closed_work/n4-mp90-variational-reference-v1'
EXPECTED = {
    'plan.json': 'd4f43809f46fd06a79ac8afce95431fa13a4009268fe3a59e035db01d0af82b4',
    'launch-command.json': '8f39eecc608d0ec0364c8a895082982ef6ff8e80d11f46bcf1dc8e3efa2dd1cc',
    'resource.json': '803d799873ccadfc95b937b935b91d660549a80d8381a4d130cd345e383e399f',
    'process.log': 'a5b2f3ad872a07a25fb7f2db5c4811e6e463e1d271d70e2aa352f3934701c2e1',
    'reference-summary.json': '07e09ac83186987a4622805b3a603efa7d4712e65d44c160ec29b115f646f550',
    'reference-raw.json.gz': '4ad1e37379b6ffb98ae173f1176e7e228a8d0658b21e6cb9bc6fa08148db4316',
}
STAGES = (43, 38, 175)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def load(path):
    path = Path(path)
    blob = path.read_bytes()
    return json.loads(gzip.decompress(blob) if path.suffix == '.gz' else blob)


def payload_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def check(item):
    if sha(item['path']) != item['sha256']:
        raise ValueError('Changed bound input/source: ' + item['path'])


def collect():
    for name, expected in EXPECTED.items():
        if sha(RUN / name) != expected:
            raise ValueError('Different observed execution: ' + name)
    plan = load(RUN / 'plan.json')
    identity = plan.pop('identity_sha256')
    assert payload_sha(plan) == identity
    plan['identity_sha256'] = identity
    assert plan['derivative_dps'] == 90 and plan['mpmath_version'] == '1.3.0'
    for mapping in (plan['source_sha256'], plan['mpmath_sources']):
        for path, digest in mapping.items():
            check(dict(path=path, sha256=digest))
    for key in ('source', 'capsule_summary', 'mp90_summary',
                'original_validated_float_baseline', 'coefficients', 'saved_mp90_raw'):
        check(plan[key])
    assert (len(plan['source_sha256']), len(plan['mpmath_sources'])) == (39, 87)
    launch = load(RUN / 'launch-command.json')
    resource = load(RUN / 'resource.json')
    summary = load(RUN / 'reference-summary.json')
    raw = load(RUN / 'reference-raw.json.gz')
    assert resource['status'] == 'observed_terminal' and resource['child_returncode'] == 0
    assert resource['command'] == launch['command']
    assert resource['command'][1:] == [plan['source']['path'], '--run-plan', str(RUN / 'plan.json')]
    assert launch['observer_command'][6] == '--'
    assert launch['observer_command'][7:] == launch['command']
    observer_path = launch['observer_command'][1]
    assert sha(observer_path) == resource['script_sha256']
    for obj in (launch, summary, raw):
        assert obj['plan'] == ref(RUN / 'plan.json')
    for obj in (summary, raw):
        assert obj['source'] == plan['source']
        assert obj['derivative_dps'] == 90
        assert obj['nonlinear_flow_or_root_invoked'] is False
    assert summary['raw'] == ref(RUN / 'reference-raw.json.gz')
    assert summary['original_MP_trajectory_rerun'] is False
    assert summary['whole_tail_or_DN_invoked'] is False
    assert summary['continuous_error_bound'] is False
    assert summary['native_comparison_performed'] is False
    assert raw['saved_trajectory_recomputed'] is False
    assert raw['mpmath_version'] == '1.3.0'
    assert raw['independent_derivative_evaluations'] is True
    assert [r['stage'] for r in raw['rows']] == list(STAGES)
    assert [r['stage'] for r in summary['named_results']] == list(STAGES)
    log = [json.loads(line) for line in (RUN / 'process.log').read_text().splitlines()]
    expected_log = []
    checkpoints = []
    results = []
    for row, reported, trajectory in zip(raw['rows'], summary['named_results'],
                                         plan['trajectories'], strict=True):
        assert row['saved_trajectory_identity'] == trajectory
        assert trajectory['original_roots'] == reported['derivative_sites'] == 64
        assert trajectory['original_RK_steps'] == 16 and trajectory['original_fallbacks'] == 0
        matrix = row['tangent42_by40']
        assert len(matrix) == 42 and all(len(r) == 40 for r in matrix)
        assert all(isinstance(v, str) for r in matrix for v in r)
        exact_stored = [[Fraction(v) for v in r] for r in matrix]
        assert row['tangent_serialization_sha256'] == payload_sha(matrix)
        assert reported['tangent_serialization_sha256'] == row['tangent_serialization_sha256']
        assert all(v == 0 for v in exact_stored[41])
        check(reported['stage_checkpoint'])
        checkpoint = load(reported['stage_checkpoint']['path'])
        assert checkpoint['row'] == row
        assert checkpoint['plan'] == summary['plan'] and checkpoint['source'] == summary['source']
        assert checkpoint['derivative_dps'] == 90
        assert checkpoint['nonlinear_flow_or_root_invoked'] is False
        stripped = {k: v for k, v in reported.items() if k != 'stage_checkpoint'}
        assert checkpoint['summary'] == stripped
        expected_log.extend(dict(stage=row['stage'], profile=0, step=step,
                                 derivative_sites=4*(step+1)) for step in range(16))
        expected_log.append(dict(event='independent_variational_stage_finished', **reported))
        checkpoints.append(reported['stage_checkpoint'])
        results.append(dict(**reported, stored_last_mean_row_exactly_zero=True,
                            saved_trajectory_identity=trajectory))
    expected_log.append(dict(summary=ref(RUN / 'reference-summary.json'),
                             raw=ref(RUN / 'reference-raw.json.gz')))
    assert log == expected_log
    capsule = load(plan['coefficients']['path'])
    assert capsule['root_rules']['floor'] == 0.1
    check(capsule['input'])
    original = load(capsule['input']['path'])
    assert 'projectionFloor' not in original['config']
    production_floor = original['response']['checkpoint']['parameters']['projectionFloor']
    assert production_floor == 0.05
    return dict(
        classification='Numerical evidence: completed finite independent variational readout.',
        collector=ref(__file__),
        collector_command=[sys.executable, str(Path(__file__).resolve()), '--output'],
        mathematical_run=dict(tool_session=72556, launch_chunk='27f51b',
                              terminal_chunk='25f90d', actual_exit_code=0),
        inputs={name: ref(RUN / name) for name in EXPECTED},
        observer=ref(observer_path), stage_checkpoints=checkpoints,
        original_capsule=plan['coefficients'], original_production_checkpoint=capsule['input'],
        source_checks=dict(research_sources=39, mpmath_python_sources=87,
                           source_manifest_identity=identity),
        original_command=resource['command'], observer_command=launch['observer_command'],
        observed_terminal={k: resource[k] for k in (
            'status', 'child_returncode', 'observed_utc', 'seconds', 'samples',
            'maximum_sampled_tree_rss_kib', 'child_rusage_maxrss_kib',
            'child_user_seconds', 'child_system_seconds')},
        calculation_seconds=summary['seconds'], derivative_dps=90, original_trajectory_dps=90,
        named_results=results, total_matrix_entries=3*42*40,
        trajectory_recomputed=False, nonlinear_flow_or_root_invoked=False,
        native_library_loaded=False, native_comparison_performed=False,
        whole_tail_or_DN_invoked=False, continuous_error_bound=False,
        domain_scope=dict(frozen_capsule_floor=0.1, production_checkpoint_floor=production_floor,
            production_floor_key='response.checkpoint.parameters.projectionFloor',
            config_has_projectionFloor=False,
            statement='The saved probe and this variational reference use capsule floor 0.1. '
                      'They do not establish an adaptor for the production floor 0.05.'),
        interpretation='Implicit-equation Jacobians at the saved approximate MP90 roots and '
            'variational RK along the saved approximate states. This is not differentiation of '
            'the finite root-stopping algorithm. Recorded linear residuals and LU pivots are '
            'finite arithmetic diagnostics, not a condition estimate or interval certificate.',
        data_policy='Complete matrices/checkpoints stay in scratch; only source, identities and compact scalars are published.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    record = collect()
    record['collector_command'].append(str(args.output.resolve()))
    with args.output.open('x') as stream:
        json.dump(record, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(record=ref(args.output), matrices=3, entries=3*42*40,
                          original_run_exit_code=0, new_mathematical_evaluation=False)))


if __name__ == '__main__':
    main()
