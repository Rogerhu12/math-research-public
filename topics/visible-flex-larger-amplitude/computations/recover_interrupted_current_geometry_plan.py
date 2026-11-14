#!/usr/bin/env python3
"""Preserve an interrupted driver and resume only its unfinished actual fields.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only output-path tokens change for already started but uncompleted fields.
No mathematical input, numerical rule, successful field, or acceptance gate
is modified.  An unavailable tool session is not an observed child exit code.
"""
import argparse
import copy
import datetime
import hashlib
import json
from pathlib import Path
from root_geometry_execute_plan import inspect_complete


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def fresh(path, value):
    if path.exists():
        raise FileExistsError(path)
    path.write_text(json.dumps(value, indent=2) + '\n')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--plan', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--receipt', type=Path, required=True)
    p.add_argument('--suffix', required=True)
    p.add_argument('--lost-session', type=int, action='append', required=True)
    a = p.parse_args()
    original = read(a.plan)
    if (Path.cwd() != Path(original['cwd']) or original['modes'] != 32
            or original['baseline_only'] or len(original['candidates']) != 19):
        raise ValueError('Keep the original complete current-M32 plan')
    for path, wanted in original['source_and_input_sha256'].items():
        if sha(path) != wanted:
            raise ValueError('An original mathematical source/input changed: ' + path)
    result = copy.deepcopy(original)
    cases = []
    for source, target in zip(original['candidates'], result['candidates']):
        prefix = source['command'][source['command'].index('--out-prefix') + 1]
        prior = sorted(Path(prefix).parent.glob(Path(prefix).name + '-*'))
        record = dict(name=source['name'], original_prefix=prefix,
            original_command=source['command'], original_small_or_partial_files=[
                dict(path=str(f), sha256=sha(f), bytes=f.stat().st_size)
                for f in prior if f.is_file()])
        resource = Path(source['resource'])
        if resource.exists():
            owned = read(resource)
            if not (owned['wait4_observed'] and owned['exitcode'] == 0
                    and owned['termination_signal'] is None):
                raise ValueError('A recorded actual failed result needs a separate explicit recovery: ' + source['name'])
            record.update(inspect_complete(source))
            record['recovery_action'] = 'reuse_original_completed_field_verbatim'
            if source != target:
                raise ValueError('A completed original command changed')
        elif prior:
            newprefix = prefix + '-' + a.suffix
            if list(Path(newprefix).parent.glob(Path(newprefix).name + '-*')):
                raise FileExistsError(newprefix)
            edits = []
            for i, value in enumerate(target['command']):
                if value.startswith(prefix):
                    changed = newprefix + value[len(prefix):]
                    target['command'][i] = changed
                    edits.append(dict(index=i, before=value, after=changed))
            for key in ('report', 'field', 'resource', 'log'):
                if not source[key].startswith(prefix):
                    raise ValueError('Unexpected output-path schema')
                target[key] = newprefix + source[key][len(prefix):]
            reverse = list(target['command'])
            for edit in edits:
                if reverse[edit['index']] != edit['after']:
                    raise ValueError('Unlisted command change')
                reverse[edit['index']] = edit['before']
            if reverse != source['command']:
                raise ValueError('Only exact output-prefix substitutions are allowed')
            for key in source:
                if key not in ('command', 'report', 'field', 'resource', 'log') and source[key] != target[key]:
                    raise ValueError('A mathematical field parameter changed')
            record.update(recovery_action='repeat_only_uncompleted_field_with_fresh_output_prefix',
                replacement_prefix=newprefix, exact_output_token_edits=edits,
                original_child_exitcode_observed=False, original_termination_signal_unknown=True,
                original_partial_files_untouched=True)
        else:
            record.update(recovery_action='execute_original_unstarted_command_verbatim',
                original_child_exitcode_observed=False)
        cases.append(record)
    if cases[0]['recovery_action'] != 'reuse_original_completed_field_verbatim':
        raise ValueError('The unique completed baseline must be reused')
    receipt = dict(schema='current-M32-geometry-tool-session-interruption-recovery-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)', source_sha256=sha(__file__),
        observed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        original_plan=dict(path=str(a.plan), sha256=sha(a.plan)),
        unavailable_tool_sessions=a.lost_session, observation='write_stdin returned Unknown process id',
        no_child_exit_or_signal_inferred_from_tool_error=True, cases=cases,
        complete_original_fields_recomputed=False, same_all_mathematical_commands_and_inputs=True,
        same_3767_by_768_grid_and_mean1552=True, numerical_settings_or_acceptance_gates_changed=False)
    fresh(a.receipt, receipt)
    result['io_only_interruption_recovery'] = dict(receipt=str(a.receipt), sha256=sha(a.receipt),
        original_plan=str(a.plan), original_plan_sha256=sha(a.plan),
        mathematical_inputs_and_successful_commands_unchanged=True)
    fresh(a.out, result)
    print(json.dumps(dict(plan=str(a.out), plan_sha256=sha(a.out), receipt_sha256=sha(a.receipt),
        completed=[r['name'] for r in cases if r['recovery_action'].startswith('reuse_')],
        incomplete=[r['name'] for r in cases if not r['recovery_action'].startswith('reuse_')])), flush=True)


if __name__ == '__main__':
    main()
