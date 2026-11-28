#!/usr/bin/env python3
"""Construct an explicitly unaccepted complete state from actual E call 0027.

All downstream unknowns are retained except one literal one-ULP change at
node 86/Pi harmonic 12. Native inputs omit node zero: this entry explicitly
sets its Q to the unchanged requested target and its Pi to the actual call
0027 stage-zero flow. It does not claim that these are the lost old node-zero
bits. Only stage 85 then has a changed native input. That entire original
stage is recomputed by the unchanged production executable, with all its
frozen coefficients, trigonometric tables, steps, root rules and state.

Unchanged stages use their actual old output only after every complete stage
block and all mathematical header bytes compare exactly. The full original
discrete norm, including node zero and both boundaries, is then recomputed.
This supplies an initial guess, never an accepted solver response. A later
original full fresh Jacobian, complete height Jacobian and audit remain due.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
import copy
import gzip
import hashlib
import json
import math
from pathlib import Path
import platform
import struct
import subprocess
import time

import numpy as np


CPP_SHA = 'e5a7d3b0a1021aae54fabcd3c5baae0558cab4246b4a10cfdeb31b6d275a8ddf'
HEADER_SHA = '88d7b9bc6c92a3d73ca33b2152e8bac078b6c9b3f90167f5e0a3409dd01f8356'
EXE_SHA = '1b47ed47e70e35a08f11173b1f17a5d1c2ee046f59f54f235ee5fa56de07af94'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=digest(path.read_bytes()))


def checked(item):
    if ref(item['path']) != item:
        raise ValueError('Actual bound input changed: '+item['path'])
    return Path(item['path'])


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def save(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')


def parse_output(raw, M, count, with_jac, token):
    expected = b'VFN4OUT1'+struct.pack('<4i', 1, M, count, int(with_jac))+token.encode()
    if raw[:88] != expected:
        raise ValueError('Original native output header differs')
    K, offset = 2*M, 88
    states, tangents, diagnostics = [], [], []
    for n in range(count):
        index, status = struct.unpack_from('<2i', raw, offset)
        offset += 8
        if index != n or status != 0:
            raise ValueError('A native stage is absent or unsuccessful')
        states.append(np.frombuffer(raw, dtype='<f8', count=K+2, offset=offset).copy())
        offset += 8*(K+2)
        if with_jac:
            tangents.append(np.frombuffer(raw, dtype='<f8', count=(K+2)*K,
                offset=offset).copy().reshape(K+2, K))
            offset += 8*(K+2)*K
        values = struct.unpack_from('<3Q5d', raw, offset)
        offset += 64
        names = ('root_calls', 'root_updates', 'root_fallbacks', 'minA', 'minD',
                 'max_root_relative_residual', 'min_literal_Jacobian_pivot', 'kernel_seconds')
        row = dict(zip(names, values))
        if (not all(math.isfinite(row[k]) for k in
                    ('minA', 'minD', 'max_root_relative_residual', 'kernel_seconds'))
                or row['minA'] <= 0 or row['minD'] <= 0):
            raise ValueError('An actual native domain diagnostic is not valid')
        if with_jac and (not math.isfinite(row['min_literal_Jacobian_pivot'])
                         or row['min_literal_Jacobian_pivot'] <= 0):
            raise ValueError('The complete original tangent has no valid pivot')
        if not math.isfinite(row['min_literal_Jacobian_pivot']):
            row['min_literal_Jacobian_pivot'] = None  # No tangent was requested.
        diagnostics.append(row)
    if offset != len(raw):
        raise ValueError('Original native output extent differs')
    states = np.asarray(states)
    if not np.all(np.isfinite(states)) or (with_jac and not np.all(np.isfinite(tangents))):
        raise ValueError('An actual complete native state/tangent is not finite')
    return states, np.asarray(tangents) if with_jac else None, diagnostics


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--attempt', type=Path, required=True)
    ap.add_argument('--outdir', type=Path, required=True)
    args = ap.parse_args()
    attempt, out = args.attempt.resolve(), args.outdir.resolve()
    repo = Path(__file__).resolve().parents[5]
    if out == repo or repo in out.parents:
        raise ValueError('Keep full candidate fields outside the repository')
    out.mkdir(parents=True, exist_ok=False)
    if os.environ.get('LD_PRELOAD') or os.environ.get('LD_LIBRARY_PATH'):
        raise ValueError('Unreviewed dynamic-loader overrides')

    runs = attempt/'native-runs'
    record_path, jac_path = runs/'0027-state-record.json', runs/'0024-jac-record.json'
    record, jac_record = read(record_path), read(jac_path)
    for value, flag in ((record, False), (jac_record, True)):
        if (value.get('status') != 'complete' or value.get('returncode') != 0
                or value.get('withJac') is not flag or value.get('returned_flow_count') != 1152):
            raise ValueError('Use the actual complete E trial and previous full J')
        for key in ('manifest', 'static_metadata', 'input', 'output'):
            checked(value[key])
    if record['manifest'] != jac_record['manifest'] or record['static_metadata'] != jac_record['static_metadata']:
        raise ValueError('The old actual state and tangent do not share the native definition')
    manifest = read(record['manifest']['path'])
    bindings = [*manifest['owned_sources'], *manifest['native_files'].values(), *manifest['runtime_libraries']]
    for item in bindings:
        checked(item)
    for name, expected in (('cpp', CPP_SHA), ('header', HEADER_SHA), ('executable', EXE_SHA)):
        if manifest['native_files'][name]['sha256'] != expected:
            raise ValueError('This audited production stage kernel changed: '+name)
    meta = read(record['static_metadata']['path'])
    cfg_path = attempt/'tail-settings.json'
    cfg = read(cfg_path)
    initial_path = Path(cfg['initialCheckpoint'])
    old_initial = read(initial_path)
    cp_parameters = copy.deepcopy(old_initial['checkpoint']['parameters'])
    raw_nodes = old_initial['checkpoint']['rawNode']
    background_path = attempt/'predictor/original-tangent-scales.json'
    bg = read(background_path)
    reference_path = attempt.parent/'height-reference.json'
    reference = read(reference_path)
    H = np.asarray(reference['candidate_H'], dtype='<f8')
    target = np.asarray(bg['desiredTarget'], dtype='<f8')
    M, S, K = bg['M'], bg['depth'], bg['K']
    if (M != 24 or S != 1152 or K != 48 or cfg['modes'] != M
            or cfg['spacing'] != 3 or cfg['quadrature'] != 512
            or len(meta['stages']) != S or H.shape != (M,)
            or target.shape != (M,) or cp_parameters['modes'] != M
            or cp_parameters['depth'] != S or cp_parameters['spacing'] != 3
            or not np.all(np.isfinite(H)) or not np.all(np.isfinite(target))
            or not np.array_equal(old_initial['checkpoint']['cutHeight'], H)
            or any(type(n) is not int or not 0 <= n <= S for n in raw_nodes)):
        raise ValueError('The original complete physical dimensions or height differ')
    if (H/float(bg['r4'])).tobytes() != target.tobytes():
        raise ValueError('The original literal full-height target is different')
    scales = np.empty(S+1)
    scales[0] = max(1e-250, *map(abs, target))
    for n in range(S):
        scales[n+1] = float(scales[n])/abs(bg['gains0'][n])
    if not np.all(np.isfinite(scales)) or not np.all(scales > 0):
        raise ValueError('The original full-height scales are not complete')

    wire = checked(record['input']).read_bytes()
    header_bytes = meta['counts']['headerBytes']
    if wire[:8] != b'VFN4LD01' or struct.unpack_from('<9i', wire, 8) != (1,M,512,3,512,30,20,S,0):
        raise ValueError('The actual state-only kernel header changed')
    token = digest(wire[:44]+wire[108:])
    if token != record['payload_token'] or wire[44:108] != token.encode():
        raise ValueError('The original complete input token differs')
    original_states = np.empty((S+1, K))
    original_states[0] = np.nan  # Node zero was not recorded by the native wire.
    for n, row in enumerate(meta['stages']):
        if row['stage'] != n:
            raise ValueError('Original stage order differs')
        original_states[n+1] = np.frombuffer(wire, dtype='<f8', count=K, offset=row['initialOffset'])
        if np.frombuffer(wire, dtype='<f8', count=2, offset=row['initialOffset']+8*K).tobytes() != bytes(16):
            raise ValueError('Original per-stage means are not literal positive zeros')
    raw_flows, _, old_diagnostics = parse_output(checked(record['output']).read_bytes(), M, S, False, token)
    _, old_J, _ = parse_output(checked(jac_record['output']).read_bytes(), M, S, True, jac_record['payload_token'])
    flows = raw_flows[:, :K].copy()
    for n in range(S):
        if bg['portRatios'][n] != meta['stages'][n]['portRatio']:
            raise ValueError('Original physical port conversion differs')
        flows[n, M:] /= bg['portRatios'][n]
        if old_diagnostics[n]['root_calls'] != 4*meta['stages'][n]['nsteps']:
            raise ValueError('Original roots do not cover the complete stage grid')

    node, component, changed_stage = 86, 27, 85
    candidate = original_states.copy()
    candidate[0, :M] = target
    candidate[0, M:] = flows[0, M:]
    before, after = float(candidate[node, component]), float(flows[node, component])
    if after != np.nextafter(before, math.inf) or after-before != abs(np.spacing(before)):
        raise ValueError('The recorded residual is not precisely the declared upward one ULP')
    candidate[node, component] = after
    if np.count_nonzero(candidate[1:] != original_states[1:]) != 1:
        raise ValueError('A different downstream unknown changed')
    J85 = old_J[changed_stage, :K].copy()
    J85[M:] /= bg['portRatios'][changed_stage]
    effect = J85[:,component]*(after-before)
    predicted = flows[changed_stage]-candidate[changed_stage]+effect
    other = np.abs((flows-candidate[:-1])/scales[:-1,None])
    other[changed_stage] = 0
    deep = candidate[-1,M:]-np.asarray(bg['deepGraph'])*candidate[-1,:M]
    feasibility = dict(node0_Q_norm=float(np.max(other[0,:M])), node0_Pi_norm=float(np.max(other[0,M:])),
        other_complete_flow_rows_norm=float(np.max(other)),
        deep_norm=float(np.max(np.abs(deep)/scales[-1])),
        unchanged_height_boundary_norm=float(np.max(np.abs(candidate[0,:M]-target)/scales[0])),
        previous_true_J_neighbor_effect_norm=float(np.max(np.abs(effect)/scales[changed_stage])),
        previous_true_J_neighbor_predicted_norm=float(np.max(np.abs(predicted)/scales[changed_stage])),
        previous_J_is_prediction_only=True)
    if max(feasibility[k] for k in ('node0_Q_norm', 'node0_Pi_norm', 'other_complete_flow_rows_norm',
            'deep_norm', 'unchanged_height_boundary_norm', 'previous_true_J_neighbor_predicted_norm')) >= cfg['solveTolerance']:
        raise ValueError('The explicit candidate does not have the anticipated original residual margin')

    candidate_wire = bytearray(wire)
    location = meta['stages'][changed_stage]['initialOffset']+8*component
    struct.pack_into('<d', candidate_wire, location, after)
    candidate_token = digest(candidate_wire[:44]+candidate_wire[108:])
    candidate_wire[44:108] = candidate_token.encode()
    # These are exactly the VFConfig bytes used by vf_run_stage. Global batch
    # count and opaque echo token are transport fields; withJac stays bound.
    header_math = wire[:36]+wire[40:44]+wire[108:header_bytes]
    context = canonical(dict(manifest=record['manifest'], metadata=record['static_metadata'],
        all_source_kernel_runtime_bindings=bindings, mode=1, callbacks=None, withJac=False,
        required_rounding='FE_TONEAREST and x87 64-significand, checked inside vf_run_stage'))
    equal_rows = []
    for n, row in enumerate(meta['stages']):
        start, size = row['blockOffset'], row['blockLength']
        old_block, new_block = wire[start:start+size], candidate_wire[start:start+size]
        same = old_block == new_block
        if same != (n != changed_stage):
            raise ValueError('Unexpected complete stage dependency change')
        key_material = context+header_math+canonical(row)
        equal_rows.append(dict(stage=n, complete_block_bytes=size, identical=same,
            original_complete_key=digest(key_material+old_block),
            candidate_complete_key=digest(key_material+new_block)))
    source_row = meta['stages'][changed_stage]
    start, size = source_row['blockOffset'], source_row['blockLength']
    single = bytearray(wire[:header_bytes])+candidate_wire[start:start+size]
    struct.pack_into('<i', single, 36, 1)
    single_token = digest(single[:44]+single[108:])
    single[44:108] = single_token.encode()
    if single[:36]+single[40:44]+single[108:header_bytes] != header_math:
        raise ValueError('The single-stage request changes a mathematical header field')
    single_path, single_output = out/'original-stage85-input.bin', out/'original-stage85-output.bin'
    single_path.write_bytes(single)
    preflight = dict(scope=__doc__, source=ref(__file__), original_trial=ref(record_path),
        previous_true_J=ref(jac_path), native_manifest=record['manifest'], native_metadata=record['static_metadata'],
        current_config=ref(cfg_path), original_unaccepted_predictor=ref(initial_path),
        full_height_reference=ref(reference_path), original_scales_metadata=ref(background_path),
        original_native_input=record['input'], original_native_output=record['output'],
        all_source_kernel_runtime_bindings=bindings, feasibility=feasibility,
        requested_height_count=M, full_height_f64le_sha256=digest(H.tobytes()),
        original_native_input_omits_node0=True,
        node0_definition='New unaccepted Q=original desiredTarget; Pi=actual call0027 normalized stage0 output',
        old_node0_preservation_claimed=False, complete_unknown_count=int(candidate.size),
        retained_downstream_unknown_count=int(candidate[1:].size-1),
        changed_node=node, changed_component=component, physical_harmonic=12,
        before=before, after=after, exact_delta_hex=(after-before).hex(),
        complete_original_stage_dependencies=equal_rows,
        recomputed_stage=changed_stage, stages_to_reuse=S-1,
        stage_independence_source_fact='vf_run_stage constructs a new Engine for each VFStage; no cross-stage mutable state. CLI loop index is only output identification. kernel_seconds is timing metadata, not a field value.',
        single_original_stage_request=ref(single_path), fresh_native_J_requested=False,
        candidate_full_batch_input_sha256=digest(candidate_wire),
        candidate_full_state_f64le_sha256=digest(candidate.astype('<f8').tobytes()),
        original_equations_or_acceptance_tolerance_changed=False, accepted_field=False)
    save(out/'preflight.json', preflight)
    for item in bindings:
        checked(item)
    command = [manifest['native_files']['executable']['path'], str(single_path), str(single_output)]
    begin = time.monotonic()
    completed = subprocess.run(command, capture_output=True)
    elapsed = time.monotonic()-begin
    (out/'original-stage85-stdout.txt').write_bytes(completed.stdout)
    (out/'original-stage85-stderr.txt').write_bytes(completed.stderr)
    if completed.returncode != 0:
        save(out/'summary.json', dict(status='original_changed_stage_failed', returncode=completed.returncode,
            preflight=ref(out/'preflight.json'), command=command, elapsed_seconds=elapsed,
            accepted_field=False, original_full_request_returned=False))
        raise RuntimeError('The original affected native stage did not complete')
    fresh, _, fresh_diags = parse_output(single_output.read_bytes(), M, 1, False, single_token)
    if fresh_diags[0]['root_calls'] != 4*source_row['nsteps']:
        raise ValueError('The original changed stage did not pay every root/grid point')
    new_flows = flows.copy()
    new_flows[changed_stage] = fresh[0,:K]
    new_flows[changed_stage,M:] /= bg['portRatios'][changed_stage]
    residuals = new_flows-candidate[:-1]
    normalized = np.abs(residuals)/scales[:-1,None]
    index = np.unravel_index(np.argmax(normalized), normalized.shape)
    deep_norm = float(np.max(np.abs(deep)/scales[-1]))
    height_norm = float(np.max(np.abs(candidate[0,:M]-target)/scales[0]))
    norm = max(float(np.max(normalized)), deep_norm, height_norm)
    cp = dict(parameters=cp_parameters, states=candidate.tolist(), rawNode=raw_nodes,
        rawStates=[candidate[n].tolist() for n in raw_nodes], cutHeight=H.tolist(),
        scope='UNACCEPTED complete initializer: genuine native trial downstream states, one ULP repair, explicitly new node0. Original full fresh J, full height Jacobian and audit still required.')
    initializer_path = out/'unaccepted-complete-ulp-initializer.json.gz'
    initializer_path.write_bytes(gzip.compress(canonical(dict(checkpoint=cp, accepted=False,
        original_full_request_returned=False, initializer_kind='explicit-node0-and-one-ULP-input',
        preflight=ref(out/'preflight.json'))), mtime=0))
    domains = old_diagnostics[:]
    domains[changed_stage] = fresh_diags[0]
    for item in [record['input'], record['output'], record['manifest'], record['static_metadata'],
                 jac_record['input'], jac_record['output'], *bindings]:
        checked(item)
    report = dict(status='explicit_unaccepted_complete_ulp_initializer_evaluated', scope=__doc__,
        preflight=ref(out/'preflight.json'), source=ref(__file__), initializer=ref(initializer_path),
        actual_original_single_stage=dict(command=command, returncode=completed.returncode,
            input=ref(single_path), output=ref(single_output), diagnostics=fresh_diags[0],
            process_wall_seconds=elapsed, native_stage_count=1, original_global_stage=changed_stage,
            withJac=False, original_production_executable_unchanged=True),
        exact_reuse_stage_count=S-1, new_native_stage_count=1,
        complete_original_residual=dict(norm=norm, tolerance=cfg['solveTolerance'],
            candidate_state_residual_passed=norm<cfg['solveTolerance'],
            interior_and_node0_flow_rows=S*K, deep_rows=M, physical_height_rows=M,
            total_rows=S*K+2*M, node0_Q_norm=float(np.max(normalized[0,:M])),
            node0_Pi_norm=float(np.max(normalized[0,M:])), deep_norm=deep_norm,
            physical_height_norm=height_norm, changed_neighbor85_norm=float(np.max(normalized[changed_stage])),
            repaired_row86_norm=float(np.max(normalized[node])),
            maximizing_flow_row=dict(stage=int(index[0]), component=int(index[1]),
                variable='Q' if index[1]<M else 'Pi', harmonic=3*(int(index[1])%M+1),
                absolute_residual=float(residuals[index]), original_scale=float(scales[index[0]]))),
        complete_original_stage_domain=dict(minA=min(v['minA'] for v in domains),
            minD=min(v['minD'] for v in domains), all_actual_original_root_guards_passed=True),
        requested_height_f64le_sha256=digest(H.tobytes()), complete_unknown_count=int(candidate.size),
        full_state_f64le_sha256=digest(candidate.astype('<f8').tobytes()),
        accepted_field=False, original_solver_convergence_claimed=False,
        original_full_request_returned=False, fresh_full_J_returned=False,
        full_height_J_returned=False, full_audit_returned=False, complete_surface=False,
        reused_timing_diagnostics_are_prior_actual_timings=True,
        producer_runtime=dict(python=platform.python_version(), numpy=np.__version__, machine=platform.machine()))
    save(out/'summary.json', report)
    print(json.dumps(dict(summary=ref(out/'summary.json'), initializer=report['initializer'],
        actual_stage_seconds=elapsed, original_complete_norm=norm,
        candidate_state_residual_passed=report['complete_original_residual']['candidate_state_residual_passed'],
        accepted_field=False), indent=2), flush=True)


if __name__ == '__main__':
    main()
