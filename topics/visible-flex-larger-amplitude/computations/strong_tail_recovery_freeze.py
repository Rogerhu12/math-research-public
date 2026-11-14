#!/usr/bin/env python3
"""Freeze one failed resumed tail attempt and prepare the identical next attempt.

Storage/orchestration only.  The actual accepted recovery state, numerical
sources, stage-cache identity, mathematical settings and all final gates are
unchanged.  The previous process must already have been formally polled.
This never starts a Node worker or deletes a primary/cache file.  It invokes
the existing exact archive, input-binding and prepare-only guards in sequence.
"""
import argparse
import datetime
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous-prefix', required=True)
    parser.add_argument('--next-prefix', required=True)
    parser.add_argument('--delta-prefix', required=True)
    parser.add_argument('--formal-tool-exit', type=int, required=True)
    args = parser.parse_args()
    root = HERE.parent
    os.chdir(root)
    old, new = args.previous_prefix, args.next_prefix
    sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    read = lambda p: json.loads(Path(p).read_text())
    plan, summary, resource = (read(old+s) for s in ('-command-plan.json', '-summary.json', '-resource.json'))
    if args.formal_tool_exit != 1 or resource['exitcode'] != 1 or summary.get('tail_converged'):
        raise ValueError('This helper requires an already polled unsuccessful resumed attempt')
    if Path(new+'-command-plan.json').exists():
        raise ValueError('Use a fresh next-attempt prefix')
    recovery = plan['accepted_iteration_recovery']
    if sha(recovery['path']) != recovery['sha256']:
        raise ValueError('The authentic accepted recovery changed')
    for path, digest in plan['source_sha256'].items():
        if sha(path) != digest:
            raise ValueError('A retained numerical source changed: '+path)
    helper_hashes = {str(HERE/name):sha(HERE/name) for name in (
        Path(__file__).name, 'strong_exact_stage_cache_delta.py',
        'strong_exact_stage_cache_archive.py', 'strong_exact_stage_resume_binding.py')}
    actions = []

    def run(command):
        completed = subprocess.run(command, capture_output=True, text=True)
        actions.append(dict(command=command, exitcode=completed.returncode,
            stdout=completed.stdout, stderr=completed.stderr))
        if completed.returncode:
            raise RuntimeError('Storage verification failed: '+repr(actions[-1]))
        return completed

    argv = plan['run_argv']
    source_topic = argv[argv.index('--source-topic')+1]
    cache = argv[argv.index('--cache-directory')+1]
    seed = old+'-initial-call000001-initial-seed.json.gz'
    marker = json.loads(gzip.decompress(Path(seed).read_bytes()))['checkpoint']['exactInitialSeed']
    identity = marker['stageIdentitySHA']
    delta = args.delta_prefix+'.json'
    command = [sys.executable, str(HERE/'strong_exact_stage_cache_delta.py'),
        '--cache-root', str(Path(cache)/identity), '--out-prefix', args.delta_prefix]
    for previous in plan['new_completed_stage_cache']['manifests']:
        command += ['--previous-manifest', previous]
    run(command)
    delta_record = read(delta)
    run([sys.executable, str(HERE/'strong_exact_stage_cache_archive.py'), 'restore',
        '--manifest', delta, '--cache-parent', cache])
    binding_file = old+'-completed-J-cache-binding.json'
    run([sys.executable, str(HERE/'strong_exact_stage_resume_binding.py'),
        '--checkpoint', recovery['path'], '--seed', seed, '--trace', old+'-trace.jsonl',
        '--plan', old+'-plan.json', '--source-topic', source_topic, '--out', binding_file])
    binding = read(binding_file)
    if not binding['passed'] or binding['newly_completed_stages'] != delta_record['stage_files']:
        raise ValueError('The new immutable stages do not match the actual resumed evaluation')
    total, added = binding['checked_stages'], binding['newly_completed_stages']
    indices = [row['stage'] for row in binding['checks']]
    if indices != list(range(total)):
        raise ValueError('Unexpected initial evaluation stage order')
    actions_path = Path(old+'-storage-actions.json')
    actions_path.write_text(json.dumps(dict(source_sha256_at_start=helper_hashes, actions=actions), indent=2)+'\n')
    files, compressed = [], []
    for suffix in ('.log', '-events.jsonl', '-trace.jsonl'):
        original = Path(old+suffix)
        target = Path(str(original)+'.gz')
        data = gzip.compress(original.read_bytes(), compresslevel=6, mtime=0)
        if target.exists() and target.read_bytes() != data:
            raise ValueError('Previously compressed terminal bytes differ')
        if not target.exists():
            target.write_bytes(data)
        files.append(target)
        compressed.append(dict(source=str(original), source_sha256=sha(original),
            compressed=str(target), compressed_sha256=sha(target),
            byte_exact_decompression=gzip.decompress(target.read_bytes()) == original.read_bytes()))
    suffixes = ('-summary.json','-resource.json','-ready.json','-config.json',
        '-response_adapter.json','-response_exact-raw-adapter.json','-response_exact-stage-adapter.json',
        '-response_Node-limits-spawn.json','-response_Node-limits-ready.json',
        '-response_Node-resource-intent.json','-response_Node-resource-observed.json',
        '-initial-call000001-initial-seed.json.gz','-completed-J-cache-binding.json','-storage-actions.json')
    files += [Path(old+s) for s in suffixes]
    files += [Path(delta), *[Path(row['path']) for row in delta_record['archives']],
        Path(__file__).resolve(), HERE/'strong_exact_stage_resume_binding.py']
    cause = ('reported ENOSPC during cache storage' if 'ENOSPC' in summary.get('error','') else 'unknown')
    note = dict(scope=__doc__, formal_tool_poll_exit=args.formal_tool_exit,
        worker_returncode_before_close=summary['worker_returncode_before_close'],
        worker_returncode_after_close=summary['worker_returncode_after_close'],
        cause=cause, error=summary.get('error'), resource=resource,
        unchanged_authentic_recovery=recovery, new_complete_stages=added,
        current_state_complete_stages=total, remaining_stages=binding['full_stage_count']-total,
        no_new_accepted_state_claim=True, no_final_tail_acceptance=True,
        full_Jacobian_and_original_audit_still_required=True,
        original_archive_restore_and_full_input_binding_passed=True,
        cache_delta_manifest=delta, cache_delta_sha256=sha(delta), compressed_evidence=compressed)
    note_path = Path(old+'-failed-note.json')
    note_path.write_text(json.dumps(note, indent=2)+'\n')
    files.append(note_path)

    def manifest(path, scope, paths):
        rows = [dict(path=str(p.relative_to(root) if p.is_absolute() else p),
            bytes=p.stat().st_size, sha256=sha(p)) for p in paths]
        path.write_text(json.dumps(dict(scope=scope, files=rows), indent=2)+'\n')
        return dict(file=str(path), sha256=sha(path), files=len(rows), bytes=sum(r['bytes'] for r in rows))

    failed = manifest(Path(old+'-failed-stable-files.json'), note['scope'], files)
    next_argv = [value.replace(old,new) for value in argv]
    if next_argv[next_argv.index('--iteration-checkpoint')+1] != recovery['path']:
        raise ValueError('The next attempt must preserve the same actual accepted state')
    plan.update(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        status='prepared-identical-recovery-final-J-and-audit-not-run', run_argv=next_argv,
        resource_argv=[sys.executable,str(HERE/'strong_resource_run.py'),'--out',new+'-resource.json','--']+next_argv,
        stdout_log=new+'.log', prior_attempt=dict(prefix=old, formal_exit=1,
            observed_Node_exit=summary['worker_returncode_after_close'], cause=cause,
            wall_seconds=resource['wall_seconds'], peak_rss_kib=resource['peak_rss_kib'],
            actual_additional_accepted_trial=False, current_state_completed_Jacobian_stages=total),
        reason='Continue from the unchanged authentic accepted state with all newly verified exact stage maps; every original final gate remains.',
        observed_available_bytes_before_prepare=os.statvfs(root).f_bavail*os.statvfs(root).f_frsize,
        storage_orchestration_source_sha256=helper_hashes)
    plan['new_completed_stage_cache']['manifests'].append(delta)
    plan['new_completed_stage_cache'].update(stages_for_this_full_state=total,
        remaining_stages=binding['full_stage_count']-total, newly_completed_in_immediately_prior_attempt=added,
        archive_original_restore_formal_exit=0)
    plan['read_only_resource_observation']['prior_production_spawn_and_ready_files'] = [
        old+'-response_Node-limits-spawn.json', old+'-response_Node-limits-ready.json']
    plan_path = Path(new+'-command-plan.json')
    with plan_path.open('x') as stream:
        json.dump(plan,stream,indent=2);stream.write('\n')
    with Path(new+'-prepare.log').open('x') as log:
        prepared = subprocess.run(next_argv+['--prepare-only'],
            env={**os.environ, **plan['environment']}, stdout=log, stderr=subprocess.STDOUT)
    if prepared.returncode:
        raise RuntimeError('The next original prepare-only guard did not pass')
    prepared_files = [Path(new+s) for s in ('-command-plan.json','-plan.json','-config.json',
        '-prepare.log','-limit-observer-entry.json')]+[Path(__file__).resolve()]
    prepared_manifest = manifest(Path(new+'-prepared-stable-files.json'),
        'Prepared only; the next numerical attempt has not started.', prepared_files)
    print(json.dumps(dict(failed=failed, prepared=prepared_manifest, actual_prepare_exit=prepared.returncode,
        current_state_complete_stages=total, new_stage_count=added,
        remaining_stage_count=binding['full_stage_count']-total, next_plan_sha256=sha(plan_path))), flush=True)


if __name__ == '__main__':
    main()
