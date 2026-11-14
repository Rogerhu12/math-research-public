#!/usr/bin/env python3
"""Metadata only: record exact planned argv and genuine numerical_recovery tool returns.

This program never executes a command or mathematical backend. The caller runs
the returned exec command through its own actual tool and supplies that actual
return to complete/unavailable. A recorded natural exit is not a certificate.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shlex

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent / 'notes'
ACTOR = '/root/numerical_recovery'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identity(path):
    path = Path(path).resolve()
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            digest.update(block)
    return {'path': str(path), 'bytes': path.stat().st_size, 'sha256': digest.hexdigest()}


def verify(row):
    actual = identity(row['path'])
    require(all(actual[key] == row[key] for key in actual), 'Changed bound input: ' + row['path'])


def inventory(root):
    root = Path(root)
    return [identity(path) for path in sorted(root.rglob('*')) if path.is_file()]


def write(path, value):
    raw = (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    require(len(raw) < 1_000_000, 'Split a large metadata observation explicitly')
    with Path(path).open('xb') as stream:
        stream.write(raw)
    return identity(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--phase', choices=('prepare', 'complete', 'unavailable'), required=True)
    parser.add_argument('--record-prefix', type=Path, required=True)
    parser.add_argument('--plan', type=Path)
    parser.add_argument('--plan-sha256')
    parser.add_argument('--stage')
    parser.add_argument('--tool-result-json')
    parser.add_argument('--tool-session-id', type=int)
    args = parser.parse_args()
    prefix = args.record_prefix.resolve()
    require(prefix.parent == NOTES.resolve(), 'Record prefix must be immediate current notes')
    invocation = Path(str(prefix) + '-invocation.json')
    now = datetime.now(timezone.utc).isoformat()
    if args.phase == 'prepare':
        require(args.plan is not None and args.plan_sha256 and args.stage,
                'Prepare requires a bound plan and stage')
        require(not list(prefix.parent.glob(prefix.name + '*')), 'This invocation stem is already used')
        plan_row = identity(args.plan)
        require(plan_row['sha256'] == args.plan_sha256, 'Wrong reviewed actual success plan')
        plan = json.loads(args.plan.read_text())
        require(plan['plan_ready'] is True and plan['complete_final_audit_replayed'] is True
                and plan['actual_solver_calls'] == plan['actual_production_calls'] == 0,
                'Not an actual-success-bound pure plan')
        for row in plan['preexisting_bindings']:
            verify(row)
        matches = [row for row in plan['commands'] if row['id'] == args.stage]
        require(len(matches) == 1, 'Stage is absent or ambiguous')
        stage = matches[0]
        require(all(type(value) is str for value in stage['argv']), 'Nonliteral command argv')
        require(all(not Path(path).exists() for path in stage['expected_output_paths']),
                'Refusing to replace an existing expected output')
        run = Path(plan['production_directory'])
        require(run.parent.resolve() == NOTES.resolve(), 'Wrong production directory parent')
        run.mkdir(exist_ok=True)
        log = Path(str(prefix) + '-stdout.log')
        command = 'exec env ' + shlex.join([name + '=' + value for name, value in plan['environment'].items()]
                                         + stage['argv']) + ' > ' + shlex.quote(str(log)) + ' 2>&1'
        report = {'schema': '78718-production-stage-invocation-v1',
                  'observer': ACTOR, 'recorded_utc': now, 'recorder_source': identity(__file__),
                  'plan': plan_row, 'stage': stage, 'cwd': stage['cwd'],
                  'environment_overrides': plan['environment'],
                  'production_directory': str(run), 'files_before': inventory(run),
                  'preexisting_input_binding_count_verified': len(plan['preexisting_bindings']),
                  'stdout_log': str(log), 'execution_command': command,
                  'actual_command_started_by_this_program': False}
        row = write(invocation, report)
        print(json.dumps({'status': 'INVOCATION_RECORDED_COMMAND_NOT_EXECUTED', 'invocation': row,
                          'execution_request': {'cmd': command, 'workdir': stage['cwd']}}))
        return 0
    require(args.tool_result_json is not None, 'Require the caller actual tool return')
    prepared = json.loads(invocation.read_text())
    verify(prepared['recorder_source'])
    verify(prepared['plan'])
    result = json.loads(args.tool_result_json)
    require(type(result) is dict, 'Tool return must be an object')
    report = {'schema': '78718-production-stage-tool-observation-v1',
              'observer': ACTOR, 'recorded_utc': now, 'recorder_source': identity(__file__),
              'invocation': identity(invocation), 'plan': prepared['plan'],
              'stage_id': prepared['stage']['id'], 'tool_session_id': args.tool_session_id,
              'tool_return_metadata': {key: value for key, value in result.items() if key != 'output'},
              'files_after': inventory(prepared['production_directory']),
              'stdout_log': identity(prepared['stdout_log']) if Path(prepared['stdout_log']).exists() else None}
    if args.phase == 'complete':
        require(type(result.get('exit_code')) is int and result.get('session_id') is None
                and type(result.get('chunk_id')) is str and result['chunk_id'],
                'A completion requires a real finished tool return')
        report.update(status='observed-process-completed', actual_exit_code=result['exit_code'],
                      tool_receipt=result['chunk_id'])
        report['expected_outputs_present'] = all(Path(path).is_file()
                                                 for path in prepared['stage']['expected_output_paths'])
        report['all_production_files_below_5000000'] = all(row['bytes'] < 5_000_000
                                                         for row in report['files_after'])
        out = Path(str(prefix) + '-observed-exit.json')
    else:
        require('exit_code' not in result and 'tool_error' in result,
                'Unavailability cannot invent a process exit')
        report['status'] = 'tool-session-unavailable-process-outcome-unknown'
        out = Path(str(prefix) + '-unavailable.json')
    row = write(out, report)
    print(json.dumps({'status': report['status'], 'stage_id': report['stage_id'],
                      'actual_exit_code': report.get('actual_exit_code'),
                      'file_count': len(report['files_after']), 'observation': row}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
