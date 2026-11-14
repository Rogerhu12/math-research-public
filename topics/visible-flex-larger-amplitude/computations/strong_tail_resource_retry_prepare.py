#!/usr/bin/env python3
"""Freeze a completed all-cache failure and prepare a resource-only tail retry.

No Node/ODE/Jacobian is executed here. The original prepare-only guards still
run. This entry requires every stage of the authentic accepted state to have
been hit, with no new cache entry, in the already completed prior attempt.
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
    parser.add_argument('--node-heap', type=int, required=True)
    parser.add_argument('--resource-probe', required=True)
    parser.add_argument('--formal-tool-exit', type=int, required=True)
    args = parser.parse_args()
    os.chdir(HERE.parent)
    sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    read = lambda p: json.loads(Path(p).read_text())
    old, new = args.previous_prefix, args.next_prefix
    plan, summary, resource = (read(old+s) for s in
        ('-command-plan.json', '-summary.json', '-resource.json'))
    if args.formal_tool_exit != 1 or resource['exitcode'] != 1 or summary.get('tail_converged'):
        raise ValueError('Requires a formally completed unsuccessful attempt')
    if Path(new+'-command-plan.json').exists():
        raise ValueError('The next prefix must be fresh')
    recovery = plan['accepted_iteration_recovery']
    if sha(recovery['path']) != recovery['sha256']:
        raise ValueError('Authentic accepted recovery changed')
    for path, digest in plan['source_sha256'].items():
        if sha(path) != digest:
            raise ValueError('Retained numerical source changed: '+path)
    probe = read(args.resource_probe)
    if (probe['exitcode'] != 0 or not probe['exact_recorded_cache_runtime_matches']
            or probe['physical_evaluations'] != 0):
        raise ValueError('Resource utility/runtime check did not pass')
    argv = plan['run_argv']
    young = int(argv[argv.index('--node-young-semi-space')+1])
    expected_options = f'--max-old-space-size={args.node_heap} --max-semi-space-size={young}'
    if probe['NODE_OPTIONS'] != expected_options:
        raise ValueError('Resource utility does not match proposed settings')
    source_topic = argv[argv.index('--source-topic')+1]
    binding_file = old+'-completed-J-cache-binding.json'
    binding_argv = [sys.executable, str(HERE/'strong_exact_stage_resume_binding.py'),
        '--checkpoint', recovery['path'],
        '--seed', old+'-initial-call000001-initial-seed.json.gz',
        '--trace', old+'-trace.jsonl', '--plan', old+'-plan.json',
        '--source-topic', source_topic, '--out', binding_file]
    checked = subprocess.run(binding_argv, capture_output=True, text=True)
    if checked.returncode:
        raise RuntimeError(checked.stdout+checked.stderr)
    binding = read(binding_file)
    if (not binding['passed'] or binding['newly_completed_stages'] != 0
            or binding['checked_stages'] != binding['full_stage_count']
            or [r['stage'] for r in binding['checks']] != list(range(binding['full_stage_count']))):
        raise ValueError('Requires all original stage keys hit with no new entry')
    own = {str(HERE/p): sha(HERE/p) for p in
        (Path(__file__).name, 'strong_exact_stage_resume_binding.py')}
    actions_file = old+'-resource-retry-storage-actions.json'
    Path(actions_file).write_text(json.dumps(dict(source_sha256_at_start=own,
        binding_command=binding_argv, binding_exit=checked.returncode,
        stdout=checked.stdout, stderr=checked.stderr), indent=2)+'\n')
    files, compressed = [], []
    for suffix in ('.log', '-events.jsonl', '-trace.jsonl'):
        original = Path(old+suffix)
        target = Path(str(original)+'.gz')
        payload = gzip.compress(original.read_bytes(), compresslevel=6, mtime=0)
        if target.exists() and target.read_bytes() != payload:
            raise ValueError('Existing compressed evidence differs')
        if not target.exists():
            target.write_bytes(payload)
        files.append(target)
        compressed.append(dict(source=str(original), source_sha256=sha(original),
            compressed=str(target), compressed_sha256=sha(target),
            byte_exact_decompression=gzip.decompress(payload) == original.read_bytes()))
    suffixes = ('-command-plan.json','-plan.json','-summary.json','-resource.json',
        '-ready.json','-config.json','-response_adapter.json',
        '-response_exact-raw-adapter.json','-response_exact-stage-adapter.json',
        '-response_Node-limits-spawn.json','-response_Node-limits-ready.json',
        '-response_Node-resource-intent.json','-response_Node-resource-observed.json',
        '-initial-call000001-initial-seed.json.gz','-iteration.json.gz',
        '-completed-J-cache-binding.json','-resource-retry-storage-actions.json')
    files += [Path(old+s) for s in suffixes]
    note = dict(scope=__doc__, formal_tool_poll_exit=args.formal_tool_exit,
        worker_returncode_before_close=summary['worker_returncode_before_close'],
        worker_returncode_after_close=summary['worker_returncode_after_close'],
        cause='unknown', error=summary.get('error'), resource=resource,
        authentic_recovery_unchanged=recovery, full_stage_cache_keys_checked=binding['checked_stages'],
        no_new_cache_entries=True, no_final_audited_response=True,
        stored_or_recomputed_norm_alone_is_not_acceptance=True,
        next_change_only_Node_old_heap_MiB=args.node_heap,
        original_full_Jacobian_and_audit_still_required=True, compressed_evidence=compressed)
    note_file = Path(old+'-failed-note.json')
    note_file.write_text(json.dumps(note, indent=2)+'\n')
    files += [note_file, Path(args.resource_probe), Path(__file__).resolve()]

    def manifest(path, scope, paths):
        rows = [dict(path=str(p.relative_to(HERE.parent) if p.is_absolute() else p),
            bytes=p.stat().st_size, sha256=sha(p)) for p in paths]
        path.write_text(json.dumps(dict(scope=scope, files=rows), indent=2)+'\n')
        return dict(file=str(path), sha256=sha(path), files=len(rows), bytes=sum(r['bytes'] for r in rows))

    failed = manifest(Path(old+'-failed-stable-files.json'), note['scope'], files)
    next_argv = [v.replace(old,new) for v in argv]
    old_heap = int(next_argv[next_argv.index('--node-heap')+1])
    next_argv[next_argv.index('--node-heap')+1] = str(args.node_heap)
    if next_argv[next_argv.index('--iteration-checkpoint')+1] != recovery['path']:
        raise ValueError('Recovery path must remain exact')
    plan.update(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        status='prepared-resource-only-recovery-final-J-and-audit-not-run', run_argv=next_argv,
        resource_argv=[sys.executable,str(HERE/'strong_resource_run.py'),'--out',new+'-resource.json','--']+next_argv,
        stdout_log=new+'.log', prior_attempt=dict(prefix=old, formal_exit=1,
            observed_Node_exit=summary['worker_returncode_after_close'], cause='unknown',
            wall_seconds=resource['wall_seconds'], peak_rss_kib=resource['peak_rss_kib'],
            current_state_completed_Jacobian_stages=binding['checked_stages']),
        reason='Resource-only old-heap reduction; exact accepted state, all 576 cached maps, complete final Jacobian and original audit remain unchanged.',
        observed_available_bytes_before_prepare=os.statvfs('.').f_bavail*os.statvfs('.').f_frsize,
        storage_orchestration_source_sha256=own,
        resource_settings_same_as_prior_r4=False,
        supported_runtime_probe=dict(file=args.resource_probe, sha256=sha(args.resource_probe),
            actual_total_heap_limit_bytes=probe['probe']['heap']['heap_size_limit'],
            no_predicted_worker_RSS_or_cause_claim=True))
    plan['resource_change_only'].update(Node_old_heap_MiB=args.node_heap,
        previous_Node_old_heap_MiB=old_heap)
    plan['new_completed_stage_cache'].update(newly_completed_in_immediately_prior_attempt=0)
    plan['read_only_resource_observation']['prior_production_spawn_and_ready_files'] = [
        old+'-response_Node-limits-spawn.json',old+'-response_Node-limits-ready.json']
    plan_path = Path(new+'-command-plan.json')
    with plan_path.open('x') as stream:
        json.dump(plan,stream,indent=2);stream.write('\n')
    with Path(new+'-prepare.log').open('x') as log:
        prepared = subprocess.run(next_argv+['--prepare-only'],
            env={**os.environ,**plan['environment']},stdout=log,stderr=subprocess.STDOUT)
    if prepared.returncode:
        raise RuntimeError('Original prepare-only guards failed')
    next_files = [Path(new+s) for s in ('-command-plan.json','-plan.json','-config.json',
        '-prepare.log','-limit-observer-entry.json')]+[Path(args.resource_probe),Path(__file__).resolve()]
    ready = manifest(Path(new+'-prepared-stable-files.json'),
        'Prepared resource-only retry; no numerical attempt has started.',next_files)
    print(json.dumps(dict(failed=failed,prepared=ready,actual_prepare_exit=prepared.returncode,
        old_heap_MiB=old_heap,new_heap_MiB=args.node_heap,
        current_state_complete_stages=binding['checked_stages'],next_plan_sha256=sha(plan_path))),flush=True)


if __name__ == '__main__':
    main()
