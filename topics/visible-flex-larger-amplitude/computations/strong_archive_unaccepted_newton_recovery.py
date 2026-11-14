#!/usr/bin/env python3
"""Copy a complete original inner-Newton recovery point without accepting it.

This checks every original raw array and source hash, and binds an already
converged full-J tail snapshot as a prior warm input.  No residual, RMS, new-H
tail solve, physical audit or nonlinear acceptance is performed.  The prior
tail is explicitly not asserted to represent the current raw cut height.
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
    value = Path(path).read_bytes()
    return json.loads(gzip.decompress(value) if str(path).endswith('.gz') else value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raw', type=Path, required=True)
    parser.add_argument('--prior-tail', type=Path, required=True)
    parser.add_argument('--tail-config', type=Path, required=True)
    parser.add_argument('--archive-topic', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, required=True)
    options = parser.parse_args()
    import numpy as np
    raw = read(options.raw)
    identity, provenance = raw['identity'], raw['provenance']
    if (raw.get('solver_success') is not False or raw.get('physical_surface') is not False
            or raw.get('status') != 1 or provenance.get('phase') != 'accepted-newton'
            or not provenance.get('actual_coupled_acceptance_pending')
            or not provenance.get('rms_not_evaluated')):
        raise ValueError('Only a complete explicitly unaccepted original Newton step applies')
    original_writer = Path(__file__).parent/'root_raw_collocation.py'
    if raw['writer_sha256'] != sha(original_writer.read_bytes()):
        raise ValueError('The original complete raw writer identity differs')
    for name, expected in provenance['source_sha256'].items():
        if sha(Path(name).read_bytes()) != expected:
            raise ValueError('An original source or accepted input differs: '+name)
    if sha(options.tail_config.read_bytes()) != identity['coupling_context']['tail_config_sha256']:
        raise ValueError('The original actual tail configuration differs')
    if set(raw['arrays']) != {'x', 'y', 'p', 'cubic', 'rms'}:
        raise ValueError('Every original raw array is required, including the explicit empty RMS')
    files, arrays = {options.raw}, {}
    for name, metadata in raw['arrays'].items():
        if metadata['dtype'] != 'float64':
            raise ValueError('Unexpected original raw array dtype')
        blocks, end = [], 0
        for item in metadata['chunks']:
            if item['first'] != end or Path(item['file']).name != item['file']:
                raise ValueError('Original raw chunk coverage or filename differs')
            path = options.raw.parent/item['file']
            data = path.read_bytes()
            if sha(data) != item['sha256']:
                raise ValueError('An original raw chunk checksum differs')
            values = np.load(io.BytesIO(gzip.decompress(data)), allow_pickle=False)
            if (values.dtype != np.float64 or values.shape != (item['count'],)
                    or not np.isfinite(values).all()):
                raise ValueError('An original raw chunk shape or value differs')
            blocks.append(values)
            end += values.size
            files.add(path)
        if end != int(np.prod(metadata['shape'])):
            raise ValueError('The original complete raw array is not covered')
        arrays[name] = (np.concatenate(blocks) if blocks else np.empty(0, dtype=np.float64)).reshape(metadata['shape'])
    modes, nodes = int(identity['modes']), len(arrays['x'])
    if (arrays['y'].shape != (3*modes+1, nodes) or arrays['p'].shape != (modes+3,)
            or arrays['cubic'].shape != (4, nodes-1, 3*modes+1)
            or arrays['rms'].shape != (0,) or not np.all(np.diff(arrays['x']) > 0)
            or arrays['p'].tobytes() != np.asarray(raw['parameter_state'], dtype=np.float64).tobytes()):
        raise ValueError('Original complete unaccepted field layout differs')
    packet = read(options.prior_tail)
    response, request = packet['response'], packet['request']
    if (not response.get('converged') or not request.get('jacobian')
            or response['residual'] > packet['config']['solveTolerance']):
        raise ValueError('The prior original full-J tail did not converge')
    jacobian = np.asarray(response['heightJetJacobian'], dtype=np.float64)
    if jacobian.shape != ((3*modes+2)*modes,) or not np.isfinite(jacobian).all():
        raise ValueError('The prior original full height Jacobian is incomplete')
    snapshot = response.get('fullFlowTangentSnapshot')
    if not snapshot or not snapshot['roundtrip'].get('allBaseAndFlowValuesBitwiseEqual'):
        raise ValueError('The complete original full-flow snapshot is missing')
    snapshot_path = Path(snapshot['manifestPath'])
    if not snapshot_path.is_file():
        snapshot_path = options.prior_tail.parent/snapshot_path.name
    if sha(snapshot_path.read_bytes()) != snapshot['manifestSha256']:
        raise ValueError('The prior original full-flow snapshot checksum differs')
    stored = read(snapshot_path)
    for item in [stored['base'], *stored['chunks']]:
        path = snapshot_path.parent/item['file']
        if sha(path.read_bytes()) != item['sha256']:
            raise ValueError('A prior complete full-flow sidecar differs')
    current_height = -float(identity['gauge'])*arrays['y'][2*modes+1:, -1]
    entries = []
    for path in sorted(files):
        data = path.read_bytes()
        if len(data) >= 5_000_000:
            raise ValueError('A complete original archive piece exceeds the repository cap')
        target = options.archive_topic/'notes'/path.name
        if target.exists():
            if target.read_bytes() != data:
                raise ValueError('An existing immutable original archive piece differs')
        else:
            with target.open('xb') as stream:
                stream.write(data)
        entries.append(dict(file='notes/'+path.name, sha256=sha(data), bytes=len(data)))
    result = dict(scope=__doc__, created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_file=str(Path(__file__)), source_sha256=sha(Path(__file__).read_bytes()),
        original_raw_file=str(options.raw), original_raw_sha256=sha(options.raw.read_bytes()),
        modes=modes, angular=int(identity['angular']), gauge=float(identity['gauge']), nodes=nodes,
        original_inner_iteration=raw['niter'], original_inner_provenance=provenance,
        original_complete_identity=identity,
        every_original_raw_source_and_input_hash_checked=True,
        every_original_raw_array_hash_shape_coverage_and_finite_value_checked=True,
        complete_current_H=current_height.tolist(),
        prior_warm_tail=dict(file=str(options.prior_tail), sha256=sha(options.prior_tail.read_bytes()),
            represents_current_raw_H=False, complete_H_difference_max=float(np.max(abs(current_height-np.asarray(request['height'])))),
            prior_full_J_entries=int(jacobian.size), prior_full_flow_snapshot=snapshot),
        original_tail_config=dict(file=str(options.tail_config), sha256=sha(options.tail_config.read_bytes())),
        solver_success=False, physical_surface=False, original_RMS_evaluated=False,
        original_full_current_H_tail_and_physical_boundary_and_final_audit_required=True,
        numerical_solver_or_Node_started=False, current_original_job_changed=False,
        files=entries, total_bytes=sum(item['bytes'] for item in entries))
    with options.manifest.open('x') as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(manifest=str(options.manifest), sha256=sha(options.manifest.read_bytes()),
        files=len(entries), bytes=result['total_bytes'], nodes=nodes,
        original_inner_iteration=raw['niter'], accepted_nonlinear_BVP=False)), flush=True)


if __name__ == '__main__':
    main()
