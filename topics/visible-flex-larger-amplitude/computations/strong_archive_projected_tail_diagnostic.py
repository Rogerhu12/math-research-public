#!/usr/bin/env python3
"""Retain an actual offline comparison with exact shared full-flow recovery.

AI-assisted research, strong_recovery, 2026-11-13.
The diagnostic and its original inputs keep their original bytes and hashes.
Only byte-identical gzip payloads may reuse the later accepted archive. The
unchanged gzip recovery helper reconstructs and reads back every such target.
No state, parameter, numerical result, acceptance status or diagnostic claim
is changed. A comparison against an unaudited full-J tail remains labelled so.
"""
from __future__ import annotations
import argparse
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DIAGNOSTIC_SHA = '097b6eb7f9ef9af2291515733382195b7ce9a78a8dd8fb468f7ed87d868f1123'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def new_json(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('diagnostic', 'owned-resource', 'accepted-archive',
                 'archive-topic', 'source-topic', 'out-prefix', 'manifest'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    import strong_gzip_chunk_recovery as recovery
    report, owned, accepted = map(read, (args.diagnostic, args.owned_resource, args.accepted_archive))
    if (owned.get('exitcode') != 0 or not owned.get('wait4_observed')
            or report.get('prepare_only') or not report.get('all_checks')
            or not report.get('checks') or not all(report['checks'].values())
            or report.get('original_solver_modified')
            or report.get('new_initial_checkpoint_written')
            or report.get('new_target_accepted')
            or report.get('ODE_Node_Newton_residual_evaluations') != 0
            or report.get('rigorous_remainder_certified')
            or accepted.get('original_owned_exitcode') != 0
            or not accepted.get('original_actual_acceptance_complete')):
        raise ValueError('The real diagnostic and later accepted archive are required')
    if sha((HERE/'strong_full_flow_projected_pair_diagnostic.py').read_bytes()) != DIAGNOSTIC_SHA:
        raise ValueError('The frozen diagnostic source changed')
    original_command = owned['command']
    if (original_command.count('--out') != 1 or
            Path(original_command[original_command.index('--out')+1]).resolve() != args.diagnostic.resolve()):
        raise ValueError('The actual owned exit belongs to another diagnostic output')

    # The final archive must already contain its complete original full-flow
    # files. It supplies storage bytes, never a new reference numerical value.
    candidates = {}
    for item in accepted['files']:
        path = args.archive_topic/item['file']
        data = path.read_bytes()
        if len(data) != item['bytes'] or sha(data) != item['sha256']:
            raise ValueError('An accepted archival input changed: '+str(path))
        if path.name.endswith('.f64le.gz'):
            raw = gzip.decompress(data)
            candidates.setdefault(sha(raw), []).append((item['file'], data))

    entries, bindings, recipes, external = [], [], [], []
    archived_names = set()

    def put(relative, data, origin):
        relative = Path(relative)
        if (len(relative.parts) != 2 or relative.parts[0] not in ('notes', 'computations')
                or relative.name in ('.', '..') or len(data) >= 5_000_000):
            raise ValueError('Invalid archival filename or oversized original file')
        destination = args.archive_topic/relative
        existed = destination.exists()
        if existed:
            if destination.read_bytes() != data:
                raise ValueError('An immutable archival file differs: '+str(destination))
        else:
            with destination.open('xb') as stream:
                stream.write(data)
        if str(relative) not in archived_names:
            entries.append(dict(file=str(relative), sha256=sha(data), bytes=len(data),
                original_file=origin, reused_existing_archival_bytes=existed))
            archived_names.add(str(relative))
        return str(relative)

    for original, expected in report['input_sha256'].items():
        path = Path(original)
        data = path.read_bytes()
        if sha(data) != expected:
            raise ValueError('An original diagnostic input changed: '+original)
        if path.resolve().is_relative_to(args.source_topic.resolve()):
            external.append(dict(original_file=original, sha256=expected,
                pinned_source_relative=str(path.resolve().relative_to(args.source_topic.resolve())),
                original_file_verified=True, copied_again=False))
            continue
        if path.parent.name != 'notes':
            raise ValueError('Unexpected diagnostic data location: '+original)
        relative = 'notes/'+path.name
        existing = args.archive_topic/relative
        recipe = None
        if not existing.exists() and path.name.endswith('.f64le.gz'):
            for source_name, source_bytes in candidates.get(sha(gzip.decompress(data)), []):
                recipe = recovery.make_recipe(source_bytes, data, source_name, path.name)
                if recipe is not None:
                    break
        if recipe is not None:
            recipes.append(recipe)
            binding = dict(original_file=original, original_sha256=expected,
                exact_original_target_requires_recovery=True, source_file=recipe['source_file'],
                source_sha256=recipe['source_sha256'], target_file=recipe['target_file'])
        else:
            put(relative, data, original)
            binding = dict(original_file=original, original_sha256=expected,
                archive_file=relative, exact_original_target_requires_recovery=False)
        bindings.append(binding)

    for original, expected in report['source_sha256'].items():
        path = Path(original); data = path.read_bytes()
        if sha(data) != expected or path.parent.name != 'computations':
            raise ValueError('A diagnostic source binding differs')
        put('computations/'+path.name, data, original)
    put('computations/'+Path(__file__).name, Path(__file__).read_bytes(), str(Path(__file__)))
    helper = HERE/'strong_gzip_chunk_recovery.py'
    put('computations/'+helper.name, helper.read_bytes(), str(helper))
    prefix = args.diagnostic.with_suffix('')
    for path in sorted(prefix.parent.glob(prefix.name+'*')):
        if path.is_file():
            put('notes/'+path.name, path.read_bytes(), str(path))

    recipe_identity = None
    if recipes:
        recipe_path = Path(str(args.out_prefix)+'-flow-recovery.json')
        replay_path = Path(str(args.out_prefix)+'-flow-recovery-readback.json')
        new_json(recipe_path, dict(schema=recovery.SCHEMA,
            helper_sha256=sha(helper.read_bytes()), chunks=recipes,
            exact_original_diagnostic_inputs=True,
            original_diagnostic_and_packets_unmodified=True,
            usage='Restore into the copied notes directory using the unchanged helper before rerunning the original diagnostic.'))
        subprocess.run([sys.executable, str(helper), '--recipe', str(recipe_path),
            '--archive-topic', str(args.archive_topic), '--output-directory', str(ROOT/'notes'),
            '--report', str(replay_path)], check=True)
        replay = read(replay_path)
        if (not replay.get('all_original_target_bytes_reconstructed_and_read_back')
                or not all(row['already_existed'] for row in replay['files'])):
            raise ValueError('The actual original full-flow targets were not verified in place')
        for path in (recipe_path, replay_path):
            put('notes/'+path.name, path.read_bytes(), str(path))
        recipe_identity = dict(file='notes/'+recipe_path.name,
            sha256=sha(recipe_path.read_bytes()), original_targets=len(recipes),
            target_bytes_not_duplicated=sum(row['target_bytes'] for row in recipes),
            complete_target_bytes_reconstructed_and_read_back=True,
            no_second_copy_of_targets_written=True,
            readback=dict(file='notes/'+replay_path.name, sha256=sha(replay_path.read_bytes())))

    manifest = dict(schema='actual-projected-tail-comparison-exact-archive-v1', scope=__doc__,
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        diagnostic=dict(file='notes/'+args.diagnostic.name, sha256=sha(args.diagnostic.read_bytes())),
        source_sha256=sha(Path(__file__).read_bytes()),
        original_diagnostic_owned_exitcode=0, original_identity_checks=len(report['checks']),
        accepted_archive=dict(file=str(args.accepted_archive), sha256=sha(args.accepted_archive.read_bytes())),
        diagnostic_input_bindings=bindings, pinned_external_source_inputs=external,
        full_flow_recovery=recipe_identity,
        actual_reference_has_audit=report['reference_has_actual_audit'],
        numerical_acceptance_or_error_claim_not_upgraded=True,
        no_new_ODE_Node_Newton_or_matrix_computation=True, files=entries,
        total_bytes=sum(row['bytes'] for row in entries),
        new_bytes=sum(row['bytes'] for row in entries if not row['reused_existing_archival_bytes']))
    new_json(args.manifest, manifest)
    print(json.dumps(dict(manifest=str(args.manifest),sha256=sha(args.manifest.read_bytes()),
        files=len(entries),new_bytes=manifest['new_bytes'],flow_recovery=recipe_identity)),flush=True)


if __name__ == '__main__':
    main()
