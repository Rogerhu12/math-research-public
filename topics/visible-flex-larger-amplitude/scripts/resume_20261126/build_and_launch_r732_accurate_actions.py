#!/usr/bin/env python3
"""Materialize complete R732 science sources, then execute one accurate entry.

The complete accurate target is run through the unchanged published exception
capture wrapper. All original target arguments, domains, budgets, source guards,
exit semantics and failure reports remain. Source materialization does not call
a scientific field, root, derivative, numerical fixture or separate preflight.
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
SCHEMA = 'actual-complete-R732-accurate-source-build-and-entry-v1'
BUILDER = {
  "role": "complete_source_builder",
  "name": "reproduce_r732_R729_complete_sources.mjs",
  "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_r732_R729_complete_sources.mjs",
  "bytes": 53259,
  "sha256": "f250982e3abe4b01e9e6c49211fb3d7bf066b8d84df91a7f5e5fb32b57782da3",
  "git_blob_sha": "7148f6aba2456e391a94b7cf0ccb3f2c0f929a77"
}
ACCURATE_BUILDER = {
  "role": "normal build reproducer of four complete original-source-guarded runtimes from four current main R722 parents with all exact reversible replacements",
  "name": "reproduce_R732_accurate_normal_geometry_sources.mjs",
  "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_R732_accurate_normal_geometry_sources.mjs",
  "bytes": 69694,
  "sha256": "f001de2154b6efae895c2eec744958762a9f6f44a4b36ed15e89c2afbd238c3c",
  "git_blob_sha": "d4fa267ddaf6e2667e68c423a6644dc42afc81f8"
}
ENTRIES = {
  "normal": {
    "role": "complete unrestricted 32-stage same-field normal and sixjet runner",
    "name": "fixed_fejer_r732_complete_normal_root_and_sixjet_fees.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r732_complete_normal_root_and_sixjet_fees.py",
    "bytes": 50881,
    "sha256": "fdce285c71f82da4bb017f9afb37ae61c332ebe754a17ef8e4972f83c9483291",
    "git_blob_sha": "3be261585182f34e03a5a63f1985ecd6f6052e78"
  },
  "geometry": {
    "role": "complete quantitative fixed-target Gram, curvature and positive support evaluation for every actual closed angular and radial leaf",
    "name": "fixed_fejer_r732_continuous_gram_curvature_support.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r732_continuous_gram_curvature_support.py",
    "bytes": 46699,
    "sha256": "2dca8226150e8b2f5ab75e8435f9660ade1e4540674cb2bf93dae5c78a7e6467",
    "git_blob_sha": "57b539979492cae372dc0fcbb94ffec6133693e9"
  }
}
CAPTURE = {
  "bytes": 14448,
  "sha256": "16c18a231f19718594dba5abb8cb72e67c7eda3f2974aa061d2bcf72cfc57f5e",
  "git_blob_sha": "2584e65a5306ca8aae5c6478e8a0c1551dac81b1",
  "name": "capture_complete_accurate_fee_exception.py",
  "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/capture_complete_accurate_fee_exception.py"
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
        raise ValueError('Forward the complete capture argv, including the one original target --repo and every original target argument')
    repo = Path(original[indices[0]+1]).resolve(strict=True)
    target = ENTRIES[args.entry]
    expected_prefix = ['--target-script', str(repo/target['path']),
        '--target-sha256', target['sha256'], '--target-bytes', str(target['bytes']),
        '--diagnostic-directory']
    if (len(original) < 9 or original[:7] != expected_prefix or original[8] != '--'):
        raise ValueError('Keep the complete original capture prefix for the exact current accurate target')
    original_target = original[9:]
    if original_target.count('--repo') != 1:
        raise ValueError('Keep the complete original accurate target arguments')
    record = args.build_record.resolve()
    if record == repo or repo in record.parents:
        raise ValueError('Build execution metadata stays outside the source repository')
    materialization = record.with_name(record.name+'.materialization.json')
    accurate_materialization=record.with_name(record.name+'.accurate-materialization.json')
    if record.exists() or materialization.exists() or accurate_materialization.exists():
        raise FileExistsError('Keep each complete build execution in its own fresh metadata files')
    record.parent.mkdir(parents=True, exist_ok=True)
    builder = repo/BUILDER['path']
    builder_record = whole_file(builder, BUILDER)
    accurate_builder=repo/ACCURATE_BUILDER["path"]
    accurate_builder_record=whole_file(accurate_builder,ACCURATE_BUILDER)
    node = shutil.which('node')
    if node is None:
        raise RuntimeError('Node.js is required to materialize the complete pinned source files')
    entry = repo/CAPTURE['path']
    source_commit = subprocess.check_output(
        ['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
    command = [sys.executable, '-u', str(entry), *original]
    build_command = [node, str(builder), '--source-repository', str(repo),
        '--output-repository', str(repo), '--record', str(materialization)]
    accurate_build_command=[node,str(accurate_builder),'--source-repository',str(repo),
        '--output-repository',str(repo),'--record',str(accurate_materialization)]
    value = dict(schema=SCHEMA, complete=False, phase='complete-source-materialization-start',
        wrapper_source=file_record(__file__), wrapper_argv=list(sys.argv),
        python_version=sys.version, node_executable=node,
        source_commit=source_commit, workflow_trigger_commit=os.environ.get('GITHUB_SHA'),
        github_run_id=os.environ.get('GITHUB_RUN_ID'), github_run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
        complete_source_builder=builder_record, build_command=build_command,
        complete_accurate_source_builder=accurate_builder_record,
        accurate_build_command=accurate_build_command,
        original_entry_kind=args.entry, original_entry_source=CAPTURE,
        complete_accurate_target_source=target,
        complete_original_accurate_target_arguments=original_target,
        original_accurate_target_argument_count=len(original_target),
        original_accurate_target_arguments_changed=False,
        original_exception_capture_source_unchanged=True,
        original_complete_entry_arguments=original,
        complete_original_exception_capture_command=command,
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
        paid=subprocess.run(accurate_build_command,cwd=repo,check=False)
        value['accurate_builder_returncode']=paid.returncode
        if paid.returncode:
            raise RuntimeError('Complete accurate source build returned '+str(paid.returncode))
        accurate_value=json.loads(accurate_materialization.read_text(encoding='utf-8'))
        if (accurate_value.get('schema')!='complete-R732-accurate-source-text-reconstruction-v1'
                or accurate_value.get('complete') is not True or accurate_value.get('direction')!='forward'
                or [row['role'] for row in accurate_value['complete_sources']]!=['normal','leaf','geometry','bridge']
                or accurate_value.get('complete_source_count')!=4):
            raise ValueError('The complete R732 accurate source materialization record differs')
        value['complete_accurate_materialization_record']=file_record(accurate_materialization)
        value['complete_accurate_materialization']=accurate_value
        value['generated_sources_complete'] = True
        value['actual_original_entry_source'] = whole_file(entry, CAPTURE)
        value['actual_complete_accurate_target_source'] = whole_file(repo/target['path'], target)
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
