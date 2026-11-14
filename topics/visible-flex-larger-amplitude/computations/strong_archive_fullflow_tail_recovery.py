#!/usr/bin/env python3
"""Archive a genuine converged finite-tail response as recovery data only.

The complete response, full height Jacobian and all original full-flow
sidecars are retained exactly. This does not accept the associated prefix,
infer a physical audit when absent, or claim an infinite closed surface.
The live coupled job is neither changed nor restarted.
"""
from __future__ import annotations

import argparse
import datetime
import gzip
import hashlib
import json
import math
from pathlib import Path


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def checked(path, expected):
    data = Path(path).read_bytes()
    if sha(data) != expected:
        raise ValueError('Original complete recovery bytes differ: '+str(path))
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--packet', type=Path, required=True)
    parser.add_argument('--launch-plan', type=Path, required=True)
    parser.add_argument('--archive-topic', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, required=True)
    args = parser.parse_args()
    import numpy as np
    packet = read(args.packet)
    request, response = packet['request'], packet['response']
    modes = len(request['height'])
    if (not request.get('jacobian') or not response.get('converged') or
            not math.isfinite(response['residual']) or
            response['residual'] > packet['config']['solveTolerance']):
        raise ValueError('The original full-J nonlinear tail did not converge')
    jac = np.asarray(response['heightJetJacobian'], dtype=np.float64)
    checkpoint = response['checkpoint']
    states = np.asarray(checkpoint['states'], dtype=np.float64)
    height = np.asarray(request['height'], dtype=np.float64)
    if (modes < 1 or jac.shape != ((3*modes+2)*modes,) or not np.isfinite(jac).all() or
            states.ndim != 2 or states.shape[1] != 2*modes or not np.isfinite(states).all() or
            not np.isfinite(height).all() or
            not np.array_equal(states[np.asarray(checkpoint['rawNode'], dtype=int)],
                               np.asarray(checkpoint['rawStates'], dtype=np.float64)) or
            height.tobytes() != np.asarray(checkpoint['cutHeight'], dtype=np.float64).tobytes()):
        raise ValueError('The complete current-H/Jacobian/state identity differs')
    snapshot = response.get('fullFlowTangentSnapshot')
    if (not snapshot or response.get('fullFlowTangentStorageError') is not None or
            not snapshot['roundtrip'].get('allBaseAndFlowValuesBitwiseEqual') or
            not snapshot['roundtrip']['originalFactoryPredictorCheck'].get('allStateValuesBitwiseEqual')):
        raise ValueError('The original full-flow/base/predictor roundtrip is missing')
    manifest_path = Path(snapshot['manifestPath'])
    if not manifest_path.is_file():
        manifest_path = args.packet.parent/manifest_path.name
    checked(manifest_path, snapshot['manifestSha256'])
    stored = read(manifest_path)
    dimensions = stored['dimensions']
    if (not stored.get('complete') or not stored.get('allStageFlowJacobiansRetained') or
            not stored.get('allBaseStatesAndHeightsRetained') or
            dimensions['modes'] != modes or dimensions['stateDimension'] != 2*modes or
            dimensions['nodes'] != states.shape[0] or dimensions['stages']+1 != states.shape[0]):
        raise ValueError('The full shooting-flow dimensions differ')
    files = {args.packet, manifest_path}
    stage_end = flow_bytes = 0
    for index, item in enumerate([stored['base'], *stored['chunks']]):
        if Path(item['file']).name != item['file']:
            raise ValueError('The original sidecar name is not a basename')
        path = manifest_path.parent/item['file']
        data = checked(path, item['sha256'])
        raw = gzip.decompress(data)
        if (len(data) != item['bytes'] or len(raw) != item['rawBytes'] or
                sha(raw) != item['rawSha256'] or
                not np.isfinite(np.frombuffer(raw, dtype='<f8')).all()):
            raise ValueError('A complete original sidecar failed its raw/compressed gate')
        if index:
            if (item['firstStage'] != stage_end or
                    item['shape'] != [item['stageCount'], 2*modes, 2*modes]):
                raise ValueError('The full-flow sidecars do not cover the stages in order')
            stage_end += item['stageCount']
            flow_bytes += len(raw)
        files.add(path)
    if stage_end != dimensions['stages'] or flow_bytes != stored['rawFlowBytes']:
        raise ValueError('The full original stage flow matrices are not covered')
    entries = []
    for path in sorted(files):
        data = path.read_bytes()
        if len(data) >= 5_000_000:
            raise ValueError('A recovery file exceeds the fixed repository cap')
        target = args.archive_topic/'notes'/path.name
        if target.exists():
            if target.read_bytes() != data:
                raise ValueError('An existing immutable recovery file differs')
        else:
            with target.open('xb') as stream:
                stream.write(data)
        entries.append(dict(file='notes/'+path.name, sha256=sha(data), bytes=len(data)))
    result = dict(scope=__doc__, created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        archiver_source_sha256=sha(Path(__file__).read_bytes()),
        packet=dict(file=str(args.packet), sha256=sha(args.packet.read_bytes())),
        launch_plan=dict(file=str(args.launch_plan), sha256=sha(args.launch_plan.read_bytes())),
        full_height=height.tolist(), modes=modes, residual=response['residual'],
        tolerance=packet['config']['solveTolerance'], history=response.get('history'),
        full_height_jacobian_entries=int(jac.size), full_state_shape=list(states.shape),
        complete_snapshot=snapshot, actual_request_audit=bool(request.get('audit')),
        original_physical_tail_audit_present=response.get('audit') is not None,
        all_compressed_and_raw_sidecar_hashes_verified=True,
        all_original_stages_preserved=True, original_live_coupled_job_unchanged=True,
        coupled_prefix_or_closed_family_accepted=False,
        full_original_prefix_RMS_true_H_physical_BC_and_audit_gates_still_required=True,
        files=entries, total_bytes=sum(item['bytes'] for item in entries))
    with args.manifest.open('x') as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(manifest=str(args.manifest), manifest_sha256=sha(args.manifest.read_bytes()),
        files=len(entries), total_bytes=result['total_bytes'], residual=response['residual'])), flush=True)


if __name__ == '__main__':
    main()
