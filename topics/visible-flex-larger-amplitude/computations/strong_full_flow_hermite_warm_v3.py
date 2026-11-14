#!/usr/bin/env python3
"""Make an explicitly unaccepted full-shooting cubic-Hermite initial guess.

Two genuinely accepted prefixes, their exact full-H audited tail packets and
same-identity full-flow snapshots are required. The target complete H comes
from an identified, completed original warm screen, not a hand-entered scalar.
The default path is near collinear and stays in the observed alpha interval
[-1,2]. An off-axis projection is available only as an explicitly selected
new heuristic with a supplied small bound. It is not validated by the earlier
collinear diagnostic. No ODE, Node, residual, Jacobian, Newton or acceptance
operation occurs here. Every new worker must apply all original solve gates.
"""
from __future__ import annotations

import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
import datetime
import gzip
import hashlib
import io
import json
from pathlib import Path
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
DIAGNOSTIC_SHA = 'db44242a7cd0098cd9779950c0d9f27551d7ce86b21bad05ab2962a14747b491'
WORKER_SHA = '2a0a93902999f244a838effd4ae09930f456f0a97393416bacb1554c075c1653'
IO_KEYS = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('previous-primary', 'previous-raw', 'previous-packet', 'previous-flow',
                 'current-primary', 'current-raw', 'current-packet', 'current-flow',
                 'target-screen', 'original-predictor', 'out', 'report'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--allow-projected-direction', action='store_true')
    parser.add_argument('--max-orthogonal-relative', type=float)
    parser.add_argument('--previous-flow-packet', type=Path)
    parser.add_argument('--current-flow-packet', type=Path)
    args = parser.parse_args()
    start = time.monotonic()
    if args.out.exists() or args.report.exists() or args.out.suffix != '.gz':
        raise ValueError('Require fresh report and .json.gz warm output paths')
    if sha(HERE/'strong_full_flow_secant_offline_diagnostic.py') != DIAGNOSTIC_SHA:
        raise ValueError('The frozen numerical graph/transport reader changed')
    if sha(HERE/'strong_full_tangent_tail_worker.mjs') != WORKER_SHA:
        raise ValueError('The frozen full-flow storage worker changed')
    import strong_full_flow_secant_offline_diagnostic as kernel
    if sha(args.original_predictor) != kernel.PREDICTOR_SHA:
        raise ValueError('The frozen original tangent formula changed')
    if args.allow_projected_direction:
        if args.max_orthogonal_relative is None or not 1e-8 < args.max_orthogonal_relative <= .01:
            raise ValueError('An explicit projected heuristic needs a bound in (1e-8,.01]')
        direction_limit = args.max_orthogonal_relative
    else:
        if args.max_orthogonal_relative is not None:
            raise ValueError('A custom direction bound needs the explicit projected heuristic flag')
        direction_limit = 1e-8
    checks, inputs, factory_probes = {}, {}, {}

    def check(name, passed):
        if not passed:
            raise ValueError('Warm-input identity check failed: '+name)
        checks[name] = True

    def accepted(label):
        primary_path = getattr(args, label+'_primary')
        raw_path = getattr(args, label+'_raw')
        packet_path = getattr(args, label+'_packet')
        flow_path = getattr(args, label+'_flow')
        flow_packet_path = getattr(args, label+'_flow_packet') or packet_path
        primary, raw, packet = map(read, (primary_path, raw_path, packet_path))
        flow_packet = read(flow_packet_path)
        for path in (primary_path, raw_path, packet_path, flow_packet_path):
            inputs[str(path)] = sha(path)
        response, request = packet['response'], packet['request']
        check(label+'_original_actual_acceptance', primary.get('solver_success') and
            not primary.get('audit_pending', True) and primary['config'].get('actual_nonlinear_tail') and
            primary['max_rms_collocation_residual'] <= primary['config']['tol'] and
            primary['summary']['physical_bc_max'] <= primary['actual_tail']['actual_physical_bc_tolerance'])
        check(label+'_accepted_raw_identity', raw.get('solver_success') and
            sha(raw_path) == primary['raw_collocation_checkpoint']['sha256'] and
            Path(primary['raw_collocation_checkpoint']['file']).name == raw_path.name and
            raw['identity']['profile'] == primary['frozen_profile'])
        check(label+'_original_audited_tail', request.get('jacobian') and request.get('audit') and
            response.get('converged') and response.get('audit') and
            np.isfinite(response['residual']) and response['residual'] <= packet['config']['solveTolerance'] and
            packet['source_sha256'] == primary['actual_tail']['source_sha256'] and
            response['audit'] == primary['actual_tail']['audit'] and
            Path(primary['actual_tail']['final_response']).name == packet_path.name)
        modes = int(primary['modes'])
        metadata = raw['arrays']['y']
        blocks, end = [], 0
        for part in metadata['chunks']:
            path = raw_path.parent/part['file']
            check(label+'_raw_y_chunk_'+str(end), Path(part['file']).name == part['file'] and
                  part['first'] == end and sha(path) == part['sha256'])
            value = np.load(io.BytesIO(gzip.decompress(path.read_bytes())), allow_pickle=False)
            check(label+'_raw_y_values_'+str(end), value.dtype == np.float64 and
                  value.shape == (part['count'],) and np.isfinite(value).all())
            inputs[str(path)] = part['sha256']
            blocks.append(value)
            end += len(value)
        check(label+'_raw_y_coverage', metadata['dtype'] == 'float64' and
              end == int(np.prod(metadata['shape'])) and metadata['shape'][0] == 3*modes+1)
        values = np.concatenate(blocks).reshape(metadata['shape'])
        actual_H = -float(primary['gauge_amplitude'])*values[2*modes+1:, -1]
        check(label+'_true_complete_H', actual_H.tobytes() == np.asarray(request['height'], dtype=np.float64).tobytes())
        flow = kernel.snapshot(flow_path, inputs, check, label+'_snapshot')
        stored, identity, states, height, far, radius, flows = flow
        checkpoint = response['checkpoint']
        raw_indices = np.asarray(identity['rawNode'], dtype=np.float64)
        integer_indices = raw_indices.astype(np.int64)
        check(label+'_raw_node_indices_are_exact_integers',
            np.array_equal(raw_indices, integer_indices) and raw_indices[0] == 0 and
            raw_indices[-1] == len(states)-1 and np.all(np.diff(raw_indices) > 0))
        flow_response = flow_packet['response']
        flow_checkpoint = flow_response['checkpoint']
        flow_pointer = flow_response.get('fullFlowTangentSnapshot') or {}
        probe = flow_pointer.get('roundtrip', {}).get('originalFactoryPredictorCheck')
        check(label+'_optional_original_factory_probe_not_failed',
            probe is None or probe.get('allStateValuesBitwiseEqual') is True)
        factory_probes[label] = dict(recorded=probe is not None,
            recorded_check_passed=(probe.get('allStateValuesBitwiseEqual') if probe is not None else None),
            frozen_worker_rule='Additional original-factory probe is recorded only for call===1 && tangentPredictor; complete base/flow bit roundtrip is mandatory for every snapshot.')
        check(label+'_full_flow_owned_by_actual_audited_packet',
            flow_packet['request'].get('jacobian') and flow_packet['request'].get('audit') and
            flow_response.get('converged') and flow_response.get('audit') and
            np.isfinite(flow_response['residual']) and
            flow_response['residual'] <= flow_packet['config']['solveTolerance'] and
            flow_pointer.get('manifestSha256') == sha(flow_path) and
            flow_pointer.get('roundtrip', {}).get('allBaseAndFlowValuesBitwiseEqual') and
            np.asarray(flow_packet['request']['height'], dtype=np.float64).tobytes() == actual_H.tobytes() and
            np.array_equal(np.asarray(flow_checkpoint['states'], dtype=np.float64), states) and
            flow_checkpoint['rawNode'] == identity['rawNode'] and
            {k:v for k,v in flow_checkpoint['parameters'].items() if k not in IO_KEYS} == identity['parameters'])
        check(label+'_flow_belongs_to_same_accepted_state',
            np.array_equal(states, np.asarray(checkpoint['states'], dtype=np.float64)) and
            height.tobytes() == actual_H.tobytes() and
            checkpoint['rawNode'] == identity['rawNode'] and
            np.array_equal(states[integer_indices], np.asarray(checkpoint['rawStates'], dtype=np.float64)) and
            {k:v for k,v in checkpoint['parameters'].items() if k not in IO_KEYS} == identity['parameters'])
        check(label+'_full_height_jacobian', len(response['heightJetJacobian']) == (3*modes+2)*modes and
            np.isfinite(np.asarray(response['heightJetJacobian'], dtype=np.float64)).all())
        return primary, packet, flow, flow_packet

    previous_primary, previous_packet, previous, previous_flow_packet = accepted('previous')
    current_primary, current_packet, current, current_flow_packet = accepted('current')
    ma, ia, sa, ha, far, radius, fa = previous
    mb, ib, sb, hb, farb, radiusb, fb = current
    check('all_complete_tail_physical_and_numerical_identities_match',
        ma['identityCanonical'] == mb['identityCanonical'] and radius == radiusb and
        np.array_equal(far, farb) and sa.shape == sb.shape and
        previous_flow_packet['source_sha256'] == current_flow_packet['source_sha256'])
    screen = read(args.target_screen)
    inputs[str(args.target_screen)] = sha(args.target_screen)
    check('target_is_completed_original_unsolved_warm_screen', screen.get('finished') and
        screen.get('nonlinear_solution') is False and screen.get('true_new_H_tail_evaluated') is False and
        screen.get('finite_domain_passed') and screen.get('worker_start_attempts') == 0)
    check('target_same_current_accepted_reference',
        Path(screen['actual_reference']).name == args.current_primary.name and
        any(Path(k).name == args.current_primary.name and v == sha(args.current_primary)
            for k,v in screen['source_sha256'].items()) and
        any(Path(k).name == args.current_raw.name and v == sha(args.current_raw)
            for k,v in screen['source_sha256'].items()))
    target = np.asarray(screen['complete_warm_H'], dtype=np.float64)
    check('target_retains_complete_finite_H', target.shape == hb.shape and np.isfinite(target).all())
    dh, dn = hb-ha, target-hb
    check('distinct_accepted_and_target_H', float(dh@dh) > 0 and float(dn@dn) > 0)
    alpha = float(dh@dn/(dh@dh))
    orthogonal = dn-alpha*dh
    relative = float(np.linalg.norm(orthogonal)/np.linalg.norm(dn))
    weights = (2*np.arange(1, len(hb)+1, dtype=np.float64))**2
    weighted_relative = float(np.linalg.norm(weights*orthogonal)/np.linalg.norm(weights*dn))
    applicability = dict(alpha=alpha, declared_alpha_interval=[-1., 2.],
        alpha_comparison_roundoff_slack=2e-12,
        orthogonal_relative_l2=relative, frequency_squared_orthogonal_relative_l2=weighted_relative,
        declared_orthogonal_limit=direction_limit,
        mode=('explicit_projected_cubic_heuristic' if args.allow_projected_direction else 'near_collinear_cubic'),
        previous_delta_H_max=float(np.max(abs(dh))), target_delta_H_max=float(np.max(abs(dn))),
        existing_collinear_diagnostic_does_not_validate_new_projected_direction=bool(args.allow_projected_direction),
        practical_initial_guess_applicability_checks_only=True)
    applicable = (-1.-2e-12 <= alpha <= 2.+2e-12 and
                  relative <= direction_limit and weighted_relative <= direction_limit)
    report = dict(scope=__doc__, schema='full-flow-hermite-warm-input-v1',
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_sha256={str(Path(__file__)):sha(__file__),
            str(HERE/'strong_full_flow_secant_offline_diagnostic.py'):DIAGNOSTIC_SHA,
            str(args.original_predictor):kernel.PREDICTOR_SHA,
            str(HERE/'strong_full_tangent_tail_worker.mjs'):WORKER_SHA},
        input_sha256=inputs, checks=checks, applicability=applicability, applicable=applicable,
        original_factory_probe_recording=factory_probes,
        all_MJS_unchanged=True, original_solve_and_every_acceptance_gate_unchanged=True,
        new_target_accepted=False, ODE_Node_Newton_residual_calls=0)
    if not applicable:
        report.update(output_written=False,
            decision='Use the unchanged original warm method or choose a separately reviewed smaller direction; this is not rejection of the mathematical candidate.')
    else:
        ga, ta, cona, bera = kernel.graph_transport(fa, far)
        gb, tb, conb, berb = kernel.graph_transport(fb, far)
        check('finite_numerical_graph_inverse_residual', np.isfinite([cona,conb,bera,berb]).all() and
              max(bera,berb) < 5e-11)
        r4, modes = radius**4, len(hb)
        linear = sb+kernel.direction(gb, tb, target/r4-sb[0,:modes])
        linear[0,:modes] = target/r4
        v0 = kernel.direction(ga, ta, dh/r4)
        v1 = kernel.direction(gb, tb, dh/r4)
        delta = sb-sa
        a2 = (v0-delta)+2*(v1-delta)
        a3 = (v0-delta)+(v1-delta)
        correction = alpha**2*a2+alpha**3*a3
        predicted = linear+correction
        predicted[0,:modes] = target/r4
        check('complete_predicted_states_finite', predicted.shape == sb.shape and np.isfinite(predicted).all())
        check('direct_target_Dirichlet_Q_bits_preserved',
              np.array_equal(predicted[0,:modes].view(np.uint64), (target/r4).view(np.uint64)))
        checkpoint = dict(parameters=current_packet['response']['checkpoint']['parameters'],
            states=predicted.tolist(), rawNode=current_packet['response']['checkpoint']['rawNode'],
            rawStates=predicted[np.asarray(ib['rawNode'], dtype=np.int64)].tolist(), cutHeight=target.tolist(),
            scope='Unaccepted cubic-Hermite initial guess only. No residual/Jacobian/positivity/audit result belongs to these states; the original full solver must evaluate them.')
        payload = dict(status='cubic-hermite-full-flow-warm-only', new_target_accepted=False,
            checkpoint=checkpoint, provenance=dict(
                source_sha256=report['source_sha256'], input_sha256=inputs,
                applicability=applicability, full_tail_identity_sha256=ma['identitySha256'],
                formula='Original current tangent plus alpha^2*((v0-d)+2*(v1-d)) + alpha^3*((v0-d)+(v1-d)), d=current_state-previous_state. The current tangent includes any declared orthogonal component.',
                complete_original_nonlinear_solve_Jacobian_positivity_line_search_RMS_BC_audit_required=True,
                no_flow_Jacobian_snapshot_assigned_to_this_unaccepted_state=True))
        data = gzip.compress(json.dumps(payload, separators=(',',':'), allow_nan=False).encode(), mtime=0)
        if len(data) >= 5_000_000:
            raise ValueError('The fresh warm checkpoint exceeds the repository file cap')
        with args.out.open('xb') as stream:
            stream.write(data)
        roundtrip = read(args.out)
        restored = np.asarray(roundtrip['checkpoint']['states'], dtype=np.float64)
        check('all_predicted_state_bits_survive_JSON_roundtrip',
              np.array_equal(restored.view(np.uint64), predicted.view(np.uint64)))
        report.update(output_written=True, output=dict(file=str(args.out), sha256=sha(args.out), bytes=len(data)),
            complete_state_shape=list(predicted.shape), complete_height=target.tolist(),
            numerical_graph_checks=dict(previous_max_condition=cona, current_max_condition=conb,
                previous_normalized_inverse_residual=bera, current_normalized_inverse_residual=berb,
                no_interval_inverse_certificate=True),
            change_from_original_linear_guess=kernel.stats(predicted, linear),
            no_response_or_flow_snapshot_fabricated=True)
    report['checks'] = checks
    report['elapsed_seconds'] = time.monotonic()-start
    report['command'] = sys.argv
    with args.report.open('x') as stream:
        json.dump(report, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(report=str(args.report), report_sha256=sha(args.report),
        applicable=applicable, output_written=report['output_written'],
        elapsed_seconds=report['elapsed_seconds'], checks=len(checks))), flush=True)


if __name__ == '__main__':
    main()
