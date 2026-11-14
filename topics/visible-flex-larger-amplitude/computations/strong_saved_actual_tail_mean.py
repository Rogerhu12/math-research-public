#!/usr/bin/env python3
"""Recover the accepted finite-tail mean from exact completed-stage cache bytes.

No tail factory, ODE, root, Newton, variational evaluation, or Git operation is
called. Each cache input and full J is checked against the saved accepted binary
full-flow snapshot. A compact sidecar saves the previously unique out/mean/min
bytes; together with the existing full-J chunks it reconstructs every original
cache file bit for bit. This is a finite numerical value, not a continuous or
infinite-tail certificate.
"""
import argparse
import base64
import gzip
import hashlib
import json
import math
import struct
from pathlib import Path


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def save(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != raw:
            raise FileExistsError(str(path))
    else:
        path.write_bytes(raw)


def tree(t):
    kind = t[0]
    if kind == 'object':
        return {k: tree(v) for k, v in t[1]}
    if kind == 'array':
        return [tree(v) for v in t[1]]
    if kind == 'f64le':
        return struct.unpack('<d', bytes.fromhex(t[1]))[0]
    if kind == 'null':
        return None
    if kind in ('string', 'boolean'):
        return t[1]
    raise ValueError('Unknown original typed identity')


def load_flow(path, check):
    path = Path(path)
    obj = read(path)
    check('complete original binary full-flow snapshot',
          obj['schema'] == 'full-shooting-flow-tangent-storage-v1' and
          obj['complete'] is True and obj['baseHadAudit'] is True)
    check('original strict solve tolerance',
          obj['convergedBaseResidual'] < obj['originalSolveTolerance'])
    check('typed full-flow identity checksum',
          sha(obj['identityCanonical'].encode()) == obj['identitySha256'])
    identity = tree(json.loads(obj['identityCanonical']))
    dims = obj['dimensions']
    K, stages = dims['stateDimension'], dims['stages']
    check('complete state dimensions', K == 2 * dims['modes'] and
          dims['nodes'] == stages + 1)
    base_raw = path.with_name(obj['base']['file']).read_bytes()
    check('binary base compressed checksum', sha(base_raw) == obj['base']['sha256'])
    seed = gzip.decompress(base_raw)
    check('binary base raw checksum', sha(seed) == obj['base']['rawSha256'] and
          len(seed) == obj['base']['rawBytes'])
    flow = bytearray()
    for row in obj['chunks']:
        raw = path.with_name(row['file']).read_bytes()
        check('full J compressed chunk checksum ' + row['file'], sha(raw) == row['sha256'])
        data = gzip.decompress(raw)
        check('full J raw chunk and coverage ' + row['file'],
              sha(data) == row['rawSha256'] and len(data) == row['rawBytes'] and
              row['firstStage'] * K * K * 8 == len(flow) and
              len(data) == row['stageCount'] * K * K * 8)
        flow.extend(data)
    check('all full J stages retained', len(flow) == stages * K * K * 8)
    return obj, identity, seed, flow


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--primary', type=Path, required=True)
    parser.add_argument('--owned-resource', type=Path, required=True)
    parser.add_argument('--tail', type=Path, required=True)
    parser.add_argument('--ready', type=Path, required=True)
    parser.add_argument('--flow-manifest', type=Path, required=True)
    parser.add_argument('--background', type=Path, required=True)
    parser.add_argument('--source-topic', type=Path, required=True)
    parser.add_argument('--runtime-computations', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    checks = []

    def check(name, condition):
        if not condition:
            raise ValueError(name)
        checks.append(name)

    primary, resource, packet, ready = [read(p) for p in
        (args.primary, args.owned_resource, args.tail, args.ready)]
    check('original whole BVP owned exit zero',
          resource['exitcode'] == 0 and resource['wait4_observed'] is True)
    check('original whole BVP acceptance', primary['solver_success'] is True and
          primary['audit_pending'] is False)
    check('original ready equality', primary['actual_tail']['ready'] == ready)
    response = packet['response']
    check('original final converged full audit', response['converged'] is True and
          response['residual'] < packet['config']['solveTolerance'] and
          isinstance(response['audit'], dict))
    check('original final tail source identity',
          packet['source_sha256'] == primary['actual_tail']['source_sha256'])
    flow, identity, seed, jacobians = load_flow(args.flow_manifest, check)
    check('original packet full-flow SHA',
          response['fullFlowTangentSnapshot']['manifestSha256'] ==
          sha(args.flow_manifest.read_bytes()))
    K, stages, M = [flow['dimensions'][key] for key in
                    ('stateDimension', 'stages', 'modes')]
    states_bytes = (stages + 1) * K * 8
    values = struct.unpack('<' + 'd' * ((stages + 1) * K), seed[:states_bytes])
    saved = response['checkpoint']['states']
    check('all original checkpoint states and binary zero convention',
          len(saved) == stages + 1 and all(len(v) == K for v in saved) and
          all(values[n*K+j] == saved[n][j] for n in range(stages+1) for j in range(K)))
    H = struct.unpack('<' + 'd' * M, seed[states_bytes:states_bytes + M*8])
    check('complete physical H equals final request', list(H) == packet['request']['height'])
    check('complete raw-node map', identity['rawNode'] == response['checkpoint']['rawNode'])
    storage = ready['exactStageStorage']
    cache = Path(storage['root'])
    cache_identity = (cache/'identity.txt').read_bytes()
    check('original exact stage complete identity SHA',
          cache.name == storage['identitySHA'] and cache_identity.endswith(b'\n') and
          sha(cache_identity[:-1]) == storage['identitySHA'])
    core_path = args.source_topic/'scripts/78718-tail-tangent-core.mjs'
    core = core_path.read_text()
    check('original tail core source pin', sha(core.encode()) ==
          identity['sourceSha256']['pinned-topic/scripts/78718-tail-tangent-core.mjs'])
    check('original mean reduction and state-input formulas',
          'meanHeightToCut:last.flows.reduce((sum,f)=>sum+f.meanHeight,0)' in core and
          'f=cellFlow(n,states[n+1],withJac);' in core and
          'meanHeight:f.state[K]+f.state[K+1]' in core)
    store_path = args.runtime_computations/'strong_exact_stage_flow_store.mjs'
    check('original cache-store source pin', sha(store_path.read_bytes()) ==
          identity['sourceSha256']['adapter/strong_exact_stage_flow_store.mjs'])
    background = read(args.background)
    check('same background fingerprint and alpha',
          background['original_geometry_manifest']['profileFingerprintAfter'] ==
          identity['physicalIdentity']['profileFingerprintAfter'] and
          background['original_geometry_manifest']['frozenWarpAlpha'] ==
          identity['physicalIdentity']['frozenWarpAlpha'])
    rows, compact, total, cell_totals = [], bytearray(), 0.0, {}
    exact_sum_terms = []
    for n in range(stages):
        state = seed[(n+1)*K*8:(n+2)*K*8]
        key = sha((storage['identitySHA'] + ':' + str(n) + ':true:').encode() + state)
        path = cache/(str(n).zfill(6) + '-' + key + '.bin')
        raw = path.read_bytes()
        check('stage magic ' + str(n), raw[:8] == b'VFXJAC01')
        length = struct.unpack('<I', raw[8:12])[0]
        header_bytes = raw[12:12+length]
        header = json.loads(header_bytes)
        payload = raw[12+length:]
        check('stage complete header and input bits ' + str(n),
              header['identitySHA'] == storage['identitySHA'] and header['stage'] == n and
              header['dimension'] == K and header['withJac'] is True and
              header['inputSHA'] == sha(state) and len(payload) == (K+K*K+3)*8)
        check('stage complete payload checksum ' + str(n),
              sha(payload) == header['payloadSHA256'])
        J = jacobians[n*K*K*8:(n+1)*K*K*8]
        check('stage full J bit-equal to accepted snapshot ' + str(n),
              payload[K*8:(K+K*K)*8] == J)
        kept = payload[:K*8] + payload[(K+K*K)*8:]
        compact.extend(kept)
        mean, minA, minD = struct.unpack('<ddd', payload[-24:])
        check('finite saved stage quantities ' + str(n),
              all(math.isfinite(v) for v in struct.unpack('<'+'d'*(K+3), kept)))
        total += mean
        exact_sum_terms.append(mean)
        layout = identity['stageLayout'][n]
        cell = int(layout['rawCell'])
        cell_totals[cell] = cell_totals.get(cell, 0.0) + mean
        rows.append({'stage': n, 'raw_cell': cell, 'raw_segment': int(layout['rawSegment']),
            'raw_left': layout['rawLeft'], 'raw_right': layout['rawRight'],
            'mean_height_increment': mean, 'minA': minA, 'minD': minD,
            'cache_file': str(path), 'cache_file_sha256': sha(raw),
            'header_utf8_base64': base64.b64encode(header_bytes).decode(),
            'input_sha256': header['inputSHA'], 'payload_sha256': header['payloadSHA256']})
    stem = args.out.name.removesuffix('.json.gz').removesuffix('.json')
    compact_path = args.out.with_name(stem+'-out-and-mean.f64le.gz')
    identity_path = args.out.with_name(stem+'-stage-identity.txt.gz')
    save(compact_path, gzip.compress(bytes(compact), mtime=0))
    save(identity_path, gzip.compress(cache_identity, mtime=0))
    reread = gzip.decompress(compact_path.read_bytes())
    for row in rows:
        n = row['stage']
        kept = reread[n*(K+3)*8:(n+1)*(K+3)*8]
        J = jacobians[n*K*K*8:(n+1)*K*K*8]
        payload = kept[:K*8] + J + kept[K*8:]
        head = base64.b64decode(row['header_utf8_base64'])
        restored = b'VFXJAC01'+struct.pack('<I', len(head))+head+payload
        check('compact exact reconstruction of original stage ' + str(n),
              sha(restored) == row['cache_file_sha256'])
    physical_depth = int(identity['parameters']['physicalDepth'])
    bg_same_cells = math.fsum(v['background_height_increment'] for v in
                             background['rows'] if v['cell'] < physical_depth)
    check('all physical cells and all numerical stages',
          sorted(cell_totals) == list(range(physical_depth)) and len(rows) == stages)
    inputs = {str(p): sha(p.read_bytes()) for p in
              (args.primary, args.owned_resource, args.tail, args.ready,
               args.flow_manifest, args.background, core_path, store_path)}
    result = {'schema': 'accepted-finite-tail-saved-mean-v1', 'finished': True,
        'source_sha256': sha(Path(__file__).read_bytes()), 'input_sha256': inputs,
        'complete_original_cache_identity_sha256': storage['identitySHA'],
        'original_fullflow_identity_sha256': flow['identitySha256'],
        'dimensions': flow['dimensions'], 'original_actual_tail_residual': response['residual'],
        'physical_depth': physical_depth, 'checks': checks, 'check_count': len(checks),
        'saved_original_meanHeightToCut_forward_sum': total,
        'saved_same_terms_fsum': math.fsum(exact_sum_terms),
        'sum_absolute_saved_stage_mean_increments': math.fsum(map(abs, exact_sum_terms)),
        'physical_cell_saved_means': cell_totals,
        'factory_background_height_over_same_cells': bg_same_cells,
        'cached_mean_minus_factory_background_includes_quadrature_difference': total-bg_same_cells,
        'original_factory_height_beyond_finite_depth': math.fsum(v['background_height_increment']
            for v in background['rows'] if v['cell'] >= physical_depth),
        'rows': rows,
        'compact_archive': {'file': compact_path.name, 'bytes': compact_path.stat().st_size,
            'raw_bytes': len(compact), 'sha256': sha(compact_path.read_bytes()),
            'raw_sha256': sha(bytes(compact)), 'shape': [stages, K+3],
            'layout': 'per stage: original out[K],meanHeight,minA,minD;Float64LE'},
        'stage_identity_archive': {'file': identity_path.name,
            'sha256': sha(identity_path.read_bytes()), 'raw_sha256': sha(cache_identity)},
        'existing_J_chunks_reused_without_duplication': flow['chunks'],
        'every_original_stage_file_reconstructs_bit_for_bit': True,
        'no_ODE_root_Newton_variational_or_factory_calls': True,
        'scope': __doc__,
        'limitations': ['The value is from the original accepted finite M32, depth8, steps12 tail.',
            'No new continuous radial error bound or infinite-tail/flat-cap certificate.',
            'Mean height alone does not bound the nonzero angular height modes or the full Cartesian frame.',
            'Factory background and cached stage total use different quadrature; their difference is not a certified pure nonlinear correction.',
            'No global diameter, Hausdorff distance, rigid-registration amplitude, or reach claim.']}
    raw = (json.dumps(result, separators=(',',':'))+'\n').encode()
    save(args.out, gzip.compress(raw, mtime=0) if str(args.out).endswith('.gz') else raw)
    print(json.dumps({'finished': True, 'checks': len(checks), 'stages': stages,
        'finite_actual_meanHeightToCut': total, 'factory_background_same_cells': bg_same_cells,
        'out': str(args.out), 'sha256': sha(args.out.read_bytes())}))


if __name__ == '__main__':
    main()
