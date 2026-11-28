#!/usr/bin/env python3
"""Materialize complete pinned halfwave working-Horner sources, then run the original full entry.

This standard-library wrapper performs source construction only before launching
the complete scientific launcher or complete pure reader. It does not import
generated scientific code, execute fragments, evaluate fields, or change argv.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import traceback

TOPIC = 'topics/visible-flex-larger-amplitude'
SCHEMA = 'actual-complete-R729-native-horner-source-build-and-entry-v1'
BUILDER = {
  "role": "whole checked source builder",
  "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/reproduce_halfwave_R729_native_horner_complete_sources.mjs",
  "name": "reproduce_halfwave_R729_native_horner_complete_sources.mjs",
  "bytes": 6196,
  "sha256": "b7b5f5f9722f79e93cecb5b2effae235d32ba1fb8defafc20e2a423f5f540a0e",
  "git_blob_sha": "fc844333391db00c36793d75baa739daaea20c45"
}
ENTRIES = {
  "science": {
    "role": "launcher",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_h33_native_actions.py",
    "name": "launch_fixed_fejer_h33_native_actions.py",
    "bytes": 22355,
    "sha256": "05de0351895cc62aac673bcf9595bc64505f2d3e6a7b035840aa3120bbe1cd67",
    "git_blob_sha": "6d064dc3f3b305d94c16760216d6916b2271d865"
  },
  "pure": {
    "role": "reader",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_h33_native_report.py",
    "name": "read_fixed_fejer_h33_native_report.py",
    "bytes": 94539,
    "sha256": "2ae72a028572e41aac288ca4786978db53c54b955751efde7e116b12e43d9683",
    "git_blob_sha": "6e6492679a679476c023b60791aaa2c7343d0acf"
  }
}

def file_record(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return dict(path=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
        git_blob_sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest())


def whole_file(path, expected):
    actual = file_record(path)
    if any(actual[key] != expected[key] for key in ('bytes', 'sha256', 'git_blob_sha')):
        raise ValueError('Complete source differs: '+str(path))
    return actual


def save(path, value):
    temporary = path.with_name(path.name+'.writing-'+str(os.getpid()))
    with temporary.open('x', encoding='utf-8', newline='\n') as handle:
        json.dump(value, handle, indent=2, allow_nan=False)
        handle.write('\n')
    os.replace(temporary, path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--entry', choices=sorted(ENTRIES), required=True)
    parser.add_argument('--build-record', type=Path, required=True)
    parser.add_argument('original_arguments', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    original = list(args.original_arguments)
    if original and original[0] == '--':
        original.pop(0)
    indices = [i for i, item in enumerate(original) if item == '--repo']
    if len(indices) != 1 or indices[0]+1 >= len(original):
        raise ValueError('Forward the one original --repo argument and every original entry argument')
    repo = Path(original[indices[0]+1]).resolve(strict=True)
    record = args.build_record.resolve()
    if record == repo or repo in record.parents:
        raise ValueError('Build execution metadata stays outside the source repository')
    materialization = record.with_name(record.name+'.materialization.json')
    if record.exists() or materialization.exists():
        raise FileExistsError('Keep each complete build execution in its own fresh metadata files')
    record.parent.mkdir(parents=True, exist_ok=True)
    builder = repo/BUILDER['path']
    builder_record = whole_file(builder, BUILDER)
    node = shutil.which('node')
    if node is None:
        raise RuntimeError('Node.js is required to materialize the complete pinned source files')
    entry = repo/ENTRIES[args.entry]['path']
    source_commit = subprocess.check_output(
        ['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
    command = [sys.executable, '-u', str(entry), *original]
    build_command = [node, str(builder), '--source-repository', str(repo),
        '--output-repository', str(repo), '--record', str(materialization)]
    value = dict(schema=SCHEMA, complete=False, phase='complete-source-materialization-start',
        wrapper_source=file_record(__file__), wrapper_argv=list(sys.argv),
        python_version=sys.version, node_executable=node,
        source_commit=source_commit, workflow_trigger_commit=os.environ.get('GITHUB_SHA'),
        github_run_id=os.environ.get('GITHUB_RUN_ID'), github_run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
        complete_source_builder=builder_record, build_command=build_command,
        original_entry_kind=args.entry, original_entry_source=ENTRIES[args.entry],
        original_complete_entry_arguments=original,
        complete_original_scientific_or_pure_command=command,
        original_entry_argument_count=len(original), original_entry_arguments_changed=False,
        scientific_role_count=140, current_complete_runtime_source_count=23,
        build_wrapper_is_a_scientific_source_role=False,
        generated_source_files_claimed_tracked_at_HEAD=False,
        all_original_method_guards_retained=True, explicit_complete_method_replacements=True,
        scientific_evaluation_performed_by_builder=False,
        extra_scientific_preflight_or_fixture=False, extra_scientific_timeout=None,
        generated_sources_complete=False, child_started=False, child_returncode=None,
        mathematical_success_or_certificate_claimed=False)
    save(record, value)
    try:
        built = subprocess.run(build_command, cwd=repo, check=False)
        value['builder_returncode'] = built.returncode
        if built.returncode != 0:
            raise RuntimeError('Complete source build returned '+str(built.returncode))
        built_value = json.loads(materialization.read_text(encoding='utf-8'))
        if (built_value.get('schema') != 'actual-complete-R729-native-horner-source-materialization-v1'
                or built_value.get('complete') is not True
                or built_value.get('direction') != 'forward'
                or built_value.get('complete_source_file_count') != 17):
            raise ValueError('The full seventeen-source materialization record is incomplete')
        value['complete_materialization_record'] = file_record(materialization)
        value['complete_materialization'] = built_value
        value['node_version'] = built_value['node_version']
        value['generated_sources_complete'] = True
        value['actual_original_entry_source'] = whole_file(entry, ENTRIES[args.entry])
        value['phase'] = 'original-complete-entry-start'
        value['child_started'] = True
        save(record, value)
        child = subprocess.run(command, cwd=repo, check=False)
        value['child_returncode'] = child.returncode
        value['phase'] = 'original-complete-entry-returned'
        value['complete'] = True
        value['successful_process_return'] = child.returncode == 0
        save(record, value)
        return child.returncode if child.returncode >= 0 else 128-child.returncode
    except Exception as exc:
        value['phase'] = 'source-build-or-entry-error'
        value['error'] = dict(type=type(exc).__name__, message=str(exc))
        save(record, value)
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
