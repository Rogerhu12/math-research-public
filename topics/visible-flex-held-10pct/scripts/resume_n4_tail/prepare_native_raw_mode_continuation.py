#!/usr/bin/env python3
"""Prepare one mode increase from a completed actual raw n4 checkpoint.

Metadata and source preparation only. The native C++/CLI, parallel adapter,
original nonlinear solver and numerical gates are reused byte for byte.
The new manifest declares the new runtime M; prior M20 fixture comparisons
are provenance, not a claim that the new M has already been evaluated.
q and all raw controls remain unknowns, so this is not a fixed-all-parameters
README item5 refinement certificate.
"""
import argparse
import copy
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def verify(item):
    if ref(item['path'])['sha256'] != item['sha256']:
        raise ValueError('Bound source changed: ' + item['path'])


def load(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def save(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')
    return ref(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('workspace', 'checkpoint', 'previous-manifest', 'manifest-directory', 'run-directory'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--modes', type=int, required=True)
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    topic = workspace / 'math-research-public/topics/visible-flex-held-10pct'
    checkpoint = args.checkpoint.resolve()
    cp = load(checkpoint)
    summary_path = checkpoint.with_name(checkpoint.name.removesuffix('.json.gz')+'-summary.json')
    summary = load(summary_path)
    if (summary['status'] != 'completed' or not summary['solver_success'] or
            not summary['complete_metric_pass'] or not cp['solver_success'] or
            not cp['complete_metric_pass'] or not cp['config']['actual_nonlinear_tail'] or
            not cp['tail_seam']['tail_converged'] or
            summary['physical_profile'] != cp['physical_profile'] or
            summary['parameters'] != cp['parameters'] or
            summary['summary'] != cp['summary']):
        raise ValueError('A genuinely completed actual finite prefix is required')
    oldM = cp['config']['modes']
    if not oldM < args.modes <= len(cp['physical_port']['modes']):
        raise ValueError('Mode increase must retain old modes and use the actual existing physical port')
    if cp['config']['base_mode'] != 4 or cp['raw_control_anchor_modes'] > oldM:
        raise ValueError('Unexpected n4/raw anchor definition')
    chunks = []
    for row in cp['pp_coefficient_chunks']:
        p = checkpoint.parent / row['file']
        if ref(p)['sha256'] != row['sha256']:
            raise ValueError('Input coefficient chunk changed')
        chunks.append(ref(p))
    last_tail = checkpoint.parent / cp['tail_seam']['tail_record']
    tail = load(last_tail)
    if (not tail['response']['converged'] or not tail['request']['jacobian'] or
            not tail['request']['audit'] or not tail['response']['residual'] < 2e-9 or
            tail['response']['checkpoint']['parameters']['modes'] != oldM or
            tail['response']['jets'] != cp['tail_seam']['tail_jets']):
        raise ValueError('Complete final actual tail/Jacobian/audit source differs')
    old = load(args.previous_manifest)
    if old['fixed_scope']['M'] != oldM:
        raise ValueError('The previous declared scope has another M')
    for item in [*old['original_sources'], *old['owned_sources'],
                 *old['native_files'].values(), *old['runtime_libraries']]:
        verify(item)
    for key in ('wrapper', 'python', 'plan', 'equivalence_record'):
        verify(old['execution_provider'][key])
    args.manifest_directory.mkdir(parents=True, exist_ok=False)
    args.run_directory.mkdir(parents=True, exist_ok=False)
    manifest = copy.deepcopy(old)
    manifest['fixed_scope']['M'] = args.modes
    manifest['physical_source_input'] = ref(last_tail)
    manifest['declared_runtime_mode_continuation'] = dict(
        source=ref(__file__), previous_manifest=ref(args.previous_manifest),
        original_mode_count=oldM, new_mode_count=args.modes,
        unchanged_native_source_binary_and_runtime=True,
        unchanged_original_solver_and_gates=True,
        current_completed_prefix=ref(checkpoint), current_completed_prefix_chunks=chunks,
        current_actual_tail=ref(last_tail),
        previous_fixture_scope='The historical three fixtures certify their original M20 inputs only.',
        new_model_or_nonlinear_evaluation_by_preparation=False)
    manifest_path = args.manifest_directory / 'manifest.json'
    manifest_ref = save(manifest_path, manifest)
    audit_view = dict(scope='Schema view of the already completed actual prefix audit; no reevaluation.',
        source=ref(__file__), input_checkpoint=ref(checkpoint), input_chunks=chunks,
        completed_original_summary=ref(summary_path), final_actual_tail=ref(last_tail),
        success=True, nodes=cp['nodes'], physical_profile=cp['physical_profile'],
        parameters=cp['parameters'], summary=cp['summary'])
    audit_path = args.run_directory / 'input-actual-audit-view.json'
    audit_ref = save(audit_path, audit_view)
    out = args.run_directory.resolve() / 'seed'
    arguments = [
        '--prefix-loader-dir', str(workspace/'n4_work'),
        '--source-topic', str(workspace/'n4_work/bundle/topics/visible-flexible-closed-surface'),
        '--tail-source', manifest['source_topic'],
        '--sparse-helper', str(workspace/'publication/topics/visible-flex-held-10pct/scripts/nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'),
        '--checkpoint', str(checkpoint), '--input-audit', str(audit_path.resolve()),
        '--config', str(workspace/'transfer_work/n4-thicker-cut/w016-config.json'),
        '--out', str(out), '--modes', str(args.modes), '--angular', str(64*args.modes),
        '--quadrature', '512', '--steps', '16', '--parts', '32',
        '--tol', '1e-8', '--bc-tol', '1e-8', '--physical-bc-tol', '1e-10',
        '--max-nodes', '6000', '--node-heap', '1536',
        '--tail-initial', str(last_tail.resolve()), '--scales', '1']
    if 512 <= 4*args.modes*4:
        raise ValueError('The unchanged original Fourier guard would reject this mode count')
    arguments_path = args.run_directory / 'original-arguments.json'
    arguments_ref = save(arguments_path, arguments)
    runner = topic/'scripts/resume_n4_tail/run_observed_raw_actual_tail.py'
    command = [sys.executable, '-u', str(runner), '--prepare',
        '--original-driver', str(topic/'scripts/resume_n4_tail/couple_raw_actual_tail.py'),
        '--arguments', str(arguments_path.resolve()), '--directory', str(args.run_directory.resolve()),
        '--manifest', str(manifest_path.resolve()),
        '--observer', str(topic/'scripts/resume_n4/observe_command_live.py'), '--cwd', str(workspace)]
    result = subprocess.run(command, capture_output=True, text=True)
    stdout = args.run_directory/'preparation-child.stdout'
    stderr = args.run_directory/'preparation-child.stderr'
    with stdout.open('x') as stream:stream.write(result.stdout)
    with stderr.open('x') as stream:stream.write(result.stderr)
    record = dict(scope=__doc__, source=ref(__file__), command=sys.argv,
        previous_manifest=ref(args.previous_manifest), new_manifest=manifest_ref,
        input_checkpoint=ref(checkpoint), input_chunks=chunks, input_summary=ref(summary_path),
        actual_tail=ref(last_tail), audit_schema_view=audit_ref,
        original_arguments=arguments_ref, preparation_child_command=command,
        preparation_child_returncode=result.returncode,
        preparation_child_stdout=ref(stdout), preparation_child_stderr=ref(stderr),
        q_and_all_controls_remain_unknowns=True, original_math_evaluations=0)
    if result.returncode == 0:
        record['observed_plan'] = ref(args.run_directory/'observed-plan.json')
    output = save(args.manifest_directory/'preparation.json', record)
    print(json.dumps(dict(preparation=output, returncode=result.returncode,
                          plan=record.get('observed_plan'))), flush=True)
    if result.returncode:
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)


if __name__ == '__main__':
    main()
