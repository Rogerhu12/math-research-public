#!/usr/bin/env python3
"""Archive an original successful affine-inner prefix without accepting it.

Complete raw nodes, states, parameters, cubic coefficients and RMS values
are checked and copied byte-for-byte. The original full true-H tail and
physical boundary gates remain pending. No Newton or physical audit runs.
"""
from __future__ import annotations
import argparse
import datetime
import gzip
import hashlib
import io
import json
from pathlib import Path


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raw', type=Path, required=True)
    parser.add_argument('--warm-tail', type=Path, required=True)
    parser.add_argument('--launch-plan', type=Path, required=True)
    parser.add_argument('--archive-topic', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, required=True)
    args = parser.parse_args()
    import numpy as np
    raw = read(args.raw)
    if (raw.get('solver_success') or raw.get('status') != 0 or
            raw.get('physical_surface') is not False or
            not raw['provenance'].get('affine_inner_success') or
            not raw['provenance'].get('actual_nonlinear_coupling_pending')):
        raise ValueError('Only an explicitly pending successful affine-inner state applies')
    if raw['writer_sha256'] != sha((Path(__file__).parent/'root_raw_collocation.py').read_bytes()):
        raise ValueError('The original raw writer identity differs')
    if set(raw['arrays']) != {'x', 'y', 'p', 'cubic', 'rms'}:
        raise ValueError('The complete original raw array set is required')
    files, arrays = {args.raw}, {}
    for name, metadata in raw['arrays'].items():
        if metadata['dtype'] != 'float64':
            raise ValueError('Unexpected original raw dtype')
        blocks, end = [], 0
        for chunk in metadata['chunks']:
            if chunk['first'] != end or Path(chunk['file']).name != chunk['file']:
                raise ValueError('Original chunk coverage or filename differs')
            path = args.raw.parent/chunk['file']
            data = path.read_bytes()
            if sha(data) != chunk['sha256']:
                raise ValueError('An original complete raw chunk checksum differs')
            block = np.load(io.BytesIO(gzip.decompress(data)), allow_pickle=False)
            if (block.dtype != np.float64 or block.shape != (chunk['count'],)
                    or not np.isfinite(block).all()):
                raise ValueError('An original complete raw chunk is invalid')
            blocks.append(block)
            end += len(block)
            files.add(path)
        if end != int(np.prod(metadata['shape'])):
            raise ValueError('The original raw array is not fully covered')
        arrays[name] = np.concatenate(blocks).reshape(metadata['shape'])
    modes, nodes = int(raw['identity']['modes']), len(arrays['x'])
    if (arrays['y'].shape != (3*modes+1, nodes) or
            arrays['p'].shape != (modes+3,) or
            arrays['cubic'].shape != (4, nodes-1, 3*modes+1) or
            arrays['rms'].shape != (nodes-1,) or
            not np.all(np.diff(arrays['x']) > 0) or
            not np.array_equal(arrays['p'], raw['parameter_state'])):
        raise ValueError('The complete original augmented field is inconsistent')
    rms = float(np.max(arrays['rms']))
    if rms > raw['identity']['tol']:
        raise ValueError('The original full RMS gate has not passed')
    packet = read(args.warm_tail)
    response = packet['response']
    if (not response.get('converged') or not packet['request'].get('jacobian') or
            response['residual'] > packet['config']['solveTolerance']):
        raise ValueError('The prior true tail must be converged with its full Jacobian')
    snapshot = response.get('fullFlowTangentSnapshot')
    if not snapshot or not snapshot['roundtrip']['allBaseAndFlowValuesBitwiseEqual']:
        raise ValueError('The prior full-flow snapshot is required for faithful recovery')
    # The prior packet is a warm-state recovery input, not the final current-H response.
    full_H = -float(raw['identity']['gauge'])*arrays['y'][2*modes+1:, -1]
    entries = []
    for path in sorted(files):
        data = path.read_bytes()
        destination = args.archive_topic/'notes'/path.name
        if len(data) >= 5_000_000:
            raise ValueError('An original archive piece exceeds the repository limit')
        reused = destination.exists()
        if reused:
            if destination.read_bytes() != data:
                raise ValueError('An existing original archive piece differs')
        else:
            with destination.open('xb') as stream:
                stream.write(data)
        entries.append(dict(file='notes/'+path.name, bytes=len(data), sha256=sha(data),
                            reused_existing_archival_bytes=reused))
    result = dict(scope=__doc__, created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_file=str(Path(__file__)), source_sha256=sha(Path(__file__).read_bytes()),
        raw_file=str(args.raw), raw_sha256=sha(args.raw.read_bytes()),
        modes=modes, nodes=nodes, angular=raw['identity']['angular'],
        complete_raw_array_hashes_shapes_and_coverage_verified=True,
        original_inner_RMS=rms, original_RMS_tolerance=raw['identity']['tol'],
        full_current_H=full_H.tolist(), original_raw_identity=raw['identity'],
        original_pending_provenance=raw['provenance'],
        prior_warm_tail=dict(file=str(args.warm_tail), sha256=sha(args.warm_tail.read_bytes()),
            full_flow_snapshot=snapshot, represents_current_prefix_H=False,
            full_H_difference=float(np.max(abs(full_H-np.asarray(packet['request']['height']))))),
        launch_plan=dict(file=str(args.launch_plan), sha256=sha(args.launch_plan.read_bytes())),
        solver_success=False, actual_nonlinear_coupling_pending=True,
        actual_final_true_H_and_physical_boundary_and_audit_required=True,
        complete_job_exit_observed=False, original_live_job_not_interrupted=True,
        files=entries, total_bytes=sum(e['bytes'] for e in entries),
        new_bytes=sum(e['bytes'] for e in entries if not e['reused_existing_archival_bytes']),
        physical_surface_or_new_accepted_BVP_claim=False)
    if args.manifest.exists():
        raise ValueError('Use a fresh archive manifest')
    args.manifest.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(manifest=str(args.manifest), sha256=sha(args.manifest.read_bytes()),
        nodes=nodes, RMS=rms, files=len(entries), total_bytes=result['total_bytes'])), flush=True)


if __name__ == '__main__':
    main()
