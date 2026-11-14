#!/usr/bin/env python3
"""Archive one actually accepted finite BVP and its original full-flow tail.

This copies immutable original bytes after checking the owned exit status,
physical acceptance gates, complete raw H, tail source identity and every
binary chunk. It never runs Newton, changes a field or upgrades finite data
to an infinite closure, held, embedding or reach certificate.

An optional prior pending raw package can supply identical compressed array
payloads. Only the target's exact original gzip header/trailer is then stored
in a replay recipe, after complete byte-for-byte reconstruction. The original
accepted primary/raw metadata and every original target SHA remain intact.
"""
from __future__ import annotations

import argparse
import datetime
import gzip
import hashlib
import io
import json
from pathlib import Path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def checked_bytes(path, expected):
    data = Path(path).read_bytes()
    if digest(data) != expected:
        raise ValueError('Original file checksum differs: '+str(path))
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--actual-prefix', type=Path, required=True)
    parser.add_argument('--archive-topic', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--reuse-pending-raw', type=Path)
    options = parser.parse_args()
    import numpy as np
    prefix = options.actual_prefix
    primary_path = Path(str(prefix)+'.json.gz')
    primary = read(primary_path)
    resource_path = Path(str(prefix)+'-resource.json')
    resource = read(resource_path)
    if (resource.get('exitcode') != 0 or not resource.get('wait4_observed')
            or not primary.get('solver_success') or primary.get('audit_pending', True)
            or not primary['config'].get('actual_nonlinear_tail')):
        raise ValueError('The original owned actual acceptance did not complete')
    if (primary['max_rms_collocation_residual'] > primary['config']['tol']
            or primary['summary']['physical_bc_max'] >
            primary['actual_tail']['actual_physical_bc_tolerance']):
        raise ValueError('Original actual RMS or physical boundary gate failed')
    raw_path = Path(primary['raw_collocation_checkpoint']['file'])
    checked_bytes(raw_path, primary['raw_collocation_checkpoint']['sha256'])
    raw = read(raw_path)
    if not raw.get('solver_success') or raw.get('physical_surface') is not False:
        raise ValueError('The complete accepted raw checkpoint is required')
    files = {primary_path, resource_path, raw_path}
    arrays, raw_chunks = {}, []
    for name, metadata in raw['arrays'].items():
        if metadata['dtype'] != 'float64':
            raise ValueError('Unexpected raw dtype')
        blocks, end = [], 0
        for chunk in metadata['chunks']:
            if chunk['first'] != end or Path(chunk['file']).name != chunk['file']:
                raise ValueError('Raw chunk coverage or filename differs')
            path = raw_path.parent/chunk['file']
            block = np.load(io.BytesIO(gzip.decompress(checked_bytes(path, chunk['sha256']))),
                            allow_pickle=False)
            if block.shape != (chunk['count'],) or block.dtype != np.float64:
                raise ValueError('Raw chunk shape or dtype differs')
            if not np.isfinite(block).all():
                raise ValueError('A raw chunk is nonfinite')
            blocks.append(block)
            end += len(block)
            files.add(path)
            raw_chunks.append((name, chunk, path))
        if end != int(np.prod(metadata['shape'])):
            raise ValueError('Raw chunks do not cover the full array')
        arrays[name] = np.concatenate(blocks).reshape(metadata['shape'])
    modes, nodes = int(primary['modes']), int(primary['nodes'])
    if (arrays['y'].shape != (3*modes+1, nodes) or
            arrays['p'].shape not in ((modes,), (modes+3,)) or
            not np.array_equal(arrays['p'], primary['parameters'])):
        raise ValueError('Accepted full field or parameter copies differ')
    raw_reuse, prior_raw_comparison = [], None
    if options.reuse_pending_raw:
        import strong_gzip_chunk_recovery as gzip_recovery
        prior_path = options.reuse_pending_raw
        prior_data = prior_path.read_bytes()
        prior = read(prior_path)
        archived_prior = options.archive_topic/'notes'/prior_path.name
        if (not archived_prior.is_file() or archived_prior.read_bytes() != prior_data or
                not prior['provenance'].get('affine_inner_success') or
                not prior['provenance'].get('actual_nonlinear_coupling_pending')):
            raise ValueError('The explicitly prior pending raw archive must be complete and exact')
        prior_chunks = {(name, chunk['first'], chunk['count']):chunk
            for name, metadata in prior['arrays'].items() for chunk in metadata['chunks']}
        comparisons = []
        for name, chunk, path in raw_chunks:
            item = prior_chunks.get((name, chunk['first'], chunk['count']))
            shape_same = (name in prior['arrays'] and
                prior['arrays'][name]['shape'] == raw['arrays'][name]['shape'] and
                prior['arrays'][name]['dtype'] == raw['arrays'][name]['dtype'])
            row = dict(array=name, target_file=path.name, shape_and_chunk_layout_same=bool(item and shape_same),
                       original_uncompressed_bytes_equal=False, original_deflate_bytes_equal=False,
                       exact_original_gzip_payload_reused=False)
            if item and shape_same:
                if Path(item['file']).name != item['file']:
                    raise ValueError('Unexpected prior original raw chunk filename')
                source = options.archive_topic/'notes'/item['file']
                data = checked_bytes(source, item['sha256'])
                target_data = checked_bytes(path, chunk['sha256'])
                old_parts, new_parts = gzip_recovery.split_member(data), gzip_recovery.split_member(target_data)
                row['source_file'] = 'notes/'+item['file']
                row['original_uncompressed_bytes_equal'] = old_parts[3] == new_parts[3]
                row['original_deflate_bytes_equal'] = old_parts[1] == new_parts[1]
                recipe = gzip_recovery.make_recipe(data, target_data, 'notes/'+item['file'], path.name)
                if recipe is not None:
                    raw_reuse.append(recipe)
                    files.remove(path)
                    row['exact_original_gzip_payload_reused'] = True
            comparisons.append(row)
        prior_raw_comparison = dict(file='notes/'+prior_path.name, sha256=digest(prior_data),
            all_complete_original_array_chunks_equal=all(row['original_uncompressed_bytes_equal'] for row in comparisons),
            reused_original_gzip_chunks=len(raw_reuse), comparisons=comparisons)
    tail_path = Path(primary['actual_tail']['final_response'])
    packet = read(tail_path)
    request, response = packet['request'], packet['response']
    height = -float(primary['gauge_amplitude'])*arrays['y'][2*modes+1:, -1]
    if np.asarray(request['height'], dtype=np.float64).tobytes() != height.tobytes():
        raise ValueError('The final tail was not evaluated at the complete actual H')
    if (not request.get('jacobian') or not request.get('audit') or
            not response.get('converged') or not response.get('audit') or
            response['residual'] > packet['config']['solveTolerance'] or
            packet['source_sha256'] != primary['actual_tail']['source_sha256'] or
            response['audit'] != primary['actual_tail']['audit']):
        raise ValueError('The final original tail gates or source binding differ')
    jacobian = np.asarray(response['heightJetJacobian'], dtype=np.float64)
    if jacobian.shape != ((3*modes+2)*modes,) or not np.isfinite(jacobian).all():
        raise ValueError('The complete original height Jacobian is missing')
    files.add(tail_path)
    origin = packet.get('exact_audited_tail_io_adapter', {}).get('origin')
    if origin:
        origin_path = Path(origin['packet'])
        if not origin_path.is_file():
            origin_path = tail_path.parent/origin_path.name
        checked_bytes(origin_path, origin['sha256'])
        files.add(origin_path)
    end = 0
    for chunk in primary['pp_coefficient_chunks']:
        if chunk['state_first'] != end or Path(chunk['file']).name != chunk['file']:
            raise ValueError('Physical polynomial coverage differs')
        path = primary_path.parent/chunk['file']
        data = checked_bytes(path, chunk['sha256'])
        if len(data) != chunk['bytes']:
            raise ValueError('Physical polynomial byte count differs')
        files.add(path)
        end = chunk['state_last_exclusive']
    if end != 3*modes+1:
        raise ValueError('The physical polynomial does not retain every state')

    snapshot = response.get('fullFlowTangentSnapshot')
    if (not snapshot or response.get('fullFlowTangentStorageError') is not None or
            not snapshot['roundtrip'].get('allBaseAndFlowValuesBitwiseEqual')):
        raise ValueError('The original converged full-flow storage roundtrip is missing')
    snapshot_path = Path(snapshot['manifestPath'])
    if not snapshot_path.is_file():
        snapshot_path = tail_path.parent/snapshot_path.name
    checked_bytes(snapshot_path, snapshot['manifestSha256'])
    stored = read(snapshot_path)
    dimensions = stored['dimensions']
    if (not stored.get('complete') or dimensions['modes'] != modes or
            dimensions['stateDimension'] != 2*modes or
            dimensions['nodes'] != dimensions['stages']+1 or
            not stored.get('allStageFlowJacobiansRetained') or
            not stored.get('allBaseStatesAndHeightsRetained')):
        raise ValueError('Incomplete full-flow snapshot')
    files.add(snapshot_path)
    stage_end, raw_flow_bytes = 0, 0
    for index, item in enumerate([stored['base'], *stored['chunks']]):
        if Path(item['file']).name != item['file']:
            raise ValueError('A full-flow sidecar filename differs')
        path = snapshot_path.parent/item['file']
        data = checked_bytes(path, item['sha256'])
        uncompressed = gzip.decompress(data)
        if (len(data) != item['bytes'] or len(uncompressed) != item['rawBytes'] or
                digest(uncompressed) != item['rawSha256'] or
                not np.isfinite(np.frombuffer(uncompressed, dtype='<f8')).all()):
            raise ValueError('Full-flow compressed/raw binary identity differs')
        if index:
            if (item['firstStage'] != stage_end or
                    item['shape'] != [item['stageCount'], 2*modes, 2*modes]):
                raise ValueError('Full-flow stage coverage differs')
            stage_end += item['stageCount']
            raw_flow_bytes += len(uncompressed)
        files.add(path)
    if stage_end != dimensions['stages'] or raw_flow_bytes != stored['rawFlowBytes']:
        raise ValueError('The complete flow matrices were not covered')

    suffixes = ('-ownership.json', '-base-profile.json', '-config.json',
        '-actual-three-control-adapter.json', '-disk-adapter.json', '-domain-observer.json',
        '-fresh-physical-merit-adapter.json', '-prefix-cache-summary.json',
        '-tail-response_adapter.json', '-tail-response_exact-raw-adapter.json',
        '-tail-response_exact-stage-adapter.json', '-tail-response_full-tangent-adapter.json',
        '-tail-response_Node-resource-intent.json', '-tail-response_Node-resource-observed.json')
    for suffix in suffixes:
        path = Path(str(prefix)+suffix)
        if path.is_file():
            files.add(path)
    # Exact-audited-H reuse creates separately named original live generations.
    # Retain their source/resource/config bindings without copying extra raw
    # Newton states or every historical response/snapshot.
    for suffix in ('_adapter.json', '_exact-raw-adapter.json', '_exact-stage-adapter.json',
                   '_full-tangent-adapter.json', '_Node-resource-intent.json',
                   '_Node-resource-observed.json', '-config.json'):
        files.update(prefix.parent.glob(prefix.name+'-tail-response-live-*'+suffix))
    for suffix in ('_recorded-adapter.json',):
        files.update(prefix.parent.glob(prefix.name+'-tail-response'+suffix))
    target = options.archive_topic/'notes'
    target.mkdir(parents=True, exist_ok=True)
    entries = []

    def put(name, data, original_file=None):
        path = target/name
        if len(data) >= 5_000_000:
            raise ValueError('A single archive file exceeds the fixed repository limit')
        reused = path.exists()
        if reused:
            if path.read_bytes() != data:
                raise ValueError('An existing immutable archive file differs: '+str(path))
        else:
            with path.open('xb') as stream:
                stream.write(data)
        entries.append(dict(file='notes/'+name, bytes=len(data), sha256=digest(data),
                            reused_existing_archival_bytes=reused, original_file=original_file))

    for path in sorted(files):
        data = path.read_bytes()
        if path.suffix == '.json' and len(data) > 1_000_000:
            put(path.name+'.gz', gzip.compress(data, mtime=0), str(path))
        else:
            put(path.name, data)
    for suffix in ('-stdout.log', '-tail-trace.jsonl', '-tail-trials.jsonl',
                   '-disk-events.jsonl', '-iterate-ledger.jsonl',
                   '-prefix-cache-events.jsonl', '-summary.json'):
        path = Path(str(prefix)+suffix)
        if path.is_file():
            put(path.name+'.gz', gzip.compress(path.read_bytes(), mtime=0), str(path))
    for pattern in ('-tail-response-live-*-trace.jsonl', '-tail-response-live-*-trials.jsonl',
                    '-tail-response_dispatch.jsonl'):
        for path in sorted(prefix.parent.glob(prefix.name+pattern)):
            put(path.name+'.gz', gzip.compress(path.read_bytes(), mtime=0), str(path))
    ready_name = prefix.name+'-accepted-ready-extracted.json'
    put(ready_name, (json.dumps(primary['actual_tail']['ready'], indent=2, allow_nan=False)+'\n').encode(),
        str(primary_path)+' :: actual_tail.ready (explicit fresh extraction)')
    recipe_summary = None
    if raw_reuse:
        helper = Path(__file__).parent/'strong_gzip_chunk_recovery.py'
        recipe_name = prefix.name+'-exact-raw-gzip-recovery.json'
        recipe = dict(schema=gzip_recovery.SCHEMA, helper_sha256=digest(helper.read_bytes()),
            helper_file='computations/'+helper.name,
            original_accepted_raw_file='notes/'+raw_path.name,
            original_accepted_raw_sha256=digest(raw_path.read_bytes()),
            chunks=raw_reuse, all_original_target_bytes_reconstructed_in_memory=True,
            original_raw_metadata_and_primary_bytes_unchanged=True,
            source_pending_raw=prior_raw_comparison,
            usage='Run the unchanged helper with --recipe, --archive-topic, --output-directory and a fresh --report before consuming the original raw. Copy all other archived original files normally.')
        recipe_bytes = (json.dumps(recipe, indent=2, allow_nan=False)+'\n').encode()
        put(recipe_name, recipe_bytes, 'Exact original gzip headers/trailers plus hash-bound shared original DEFLATE payloads')
        recipe_summary = dict(file='notes/'+recipe_name, sha256=digest(recipe_bytes),
            helper_file='computations/'+helper.name, helper_sha256=recipe['helper_sha256'],
            chunks=len(raw_reuse), raw_target_bytes_not_duplicated=sum(row['target_bytes'] for row in raw_reuse),
            exact_original_chunks_require_reconstruction=True)
    result = dict(scope=__doc__, created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_file=str(Path(__file__)), source_sha256=digest(Path(__file__).read_bytes()),
        original_owned_exitcode=0, original_actual_acceptance_complete=True,
        complete_H_bitwise_equal=True, original_full_J_entries=len(jacobian),
        primary_file=str(primary_path), primary_sha256=digest(primary_path.read_bytes()),
        raw_file=str(raw_path), raw_sha256=digest(raw_path.read_bytes()),
        final_tail_file=str(tail_path), final_tail_sha256=digest(tail_path.read_bytes()),
        modes=modes, nodes=nodes, angular=primary['config']['angular'],
        gauge=primary['gauge_amplitude'], actual_q=primary['actual_primary_amplitude'],
        full_core=primary['core'], physical_profile=primary['frozen_profile'],
        physical_summary=primary['summary'], meridian_length=primary['meridian_length'],
        original_RMS=primary['max_rms_collocation_residual'], original_RMS_tolerance=primary['config']['tol'],
        true_physical_BC=primary['summary']['physical_bc_max'],
        true_physical_BC_tolerance=primary['actual_tail']['actual_physical_bc_tolerance'],
        tail_residual=response['residual'], tail_tolerance=packet['config']['solveTolerance'],
        original_tail_audit=response['audit'], full_flow_snapshot=snapshot,
        all_compressed_and_raw_flow_hashes_verified=True,
        complete_original_accepted_raw_content_retained=True,
        no_inner_or_iterate_array_duplicates_copied_in_this_package=True,
        prior_pending_raw_comparison=prior_raw_comparison,
        exact_original_raw_gzip_recovery=recipe_summary,
        ready_extraction=dict(file='notes/'+ready_name, origin='actual_tail.ready of this primary'),
        resources=resource, files=entries, total_bytes=sum(e['bytes'] for e in entries),
        new_bytes=sum(e['bytes'] for e in entries if not e['reused_existing_archival_bytes']),
        infinite_closure_or_closed_held_or_reach_claim=False)
    if options.manifest.exists():
        raise ValueError('Use a fresh accepted archive manifest')
    options.manifest.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(manifest=str(options.manifest), sha256=digest(options.manifest.read_bytes()),
        files=len(entries), total_bytes=result['total_bytes'], new_bytes=result['new_bytes'])), flush=True)


if __name__ == '__main__':
    main()
