#!/usr/bin/env python3
"""Materialize complete pinned R732 sources, then run the original full entry.

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
SCHEMA = 'actual-complete-R732-R729-source-build-and-entry-v1'
BUILDER = {
  "role": "complete_source_builder",
  "name": "reproduce_r732_R729_complete_sources.mjs",
  "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_r732_R729_complete_sources.mjs",
  "bytes": 53259,
  "sha256": "f250982e3abe4b01e9e6c49211fb3d7bf066b8d84df91a7f5e5fb32b57782da3",
  "git_blob_sha": "7148f6aba2456e391a94b7cf0ccb3f2c0f929a77"
}
ENTRIES = {
  "science": {
    "role": "launcher",
    "name": "launch_r732_R729_actions.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_r732_R729_actions.py",
    "bytes": 22292,
    "sha256": "670d9cef0ac9010dc9abf2d8bf4d0b864252d0d411efeee75c94b69e72a7fc3e",
    "git_blob_sha": "7ed44729d46c473fb2116d65b4dcd535921bf115"
  },
  "pure": {
    "role": "reader",
    "name": "read_r732_R729_report.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_r732_R729_report.py",
    "bytes": 95650,
    "sha256": "8f9789804b8413a30135f0300f227ffe48f99608f82048ed6a7a36456fcf4432",
    "git_blob_sha": "8cd0482c3990f7d96ab28381d11d64c41c75bd5e"
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
        scientific_role_count=139, current_complete_runtime_source_count=24,
        build_wrapper_is_a_scientific_source_role=False,
        generated_source_files_claimed_tracked_at_HEAD=False,
        original_source_and_method_guards_changed=False,
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
        if (built_value.get('schema') != 'actual-complete-R732-R729-source-materialization-v1'
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
