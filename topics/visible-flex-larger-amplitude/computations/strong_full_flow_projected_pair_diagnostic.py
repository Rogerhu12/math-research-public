#!/usr/bin/env python3
"""Diagnose a projected two-point full-tail warm guess from real saved data.

AI-assisted research, strong_recovery, 2026-11-13.
Both base packets must be genuinely converged complete finite-tail/full-J
responses with bit-checked full-flow snapshots and one identical complete
tail identity. A base need not be an accepted coupled prefix; its actual audit
status is recorded. The comparison target, when present, must be a third real
complete tail response and its original unaccepted initial seed. The new
projected cubic is an offline heuristic, not an accepted solution or a
validated extension of the earlier collinear experiment. No ODE, Node, Newton,
residual evaluation, production mutation, or initial-checkpoint write occurs.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
KERNEL_SHA = 'db44242a7cd0098cd9779950c0d9f27551d7ce86b21bad05ab2962a14747b491'
WORKER_SHA = '2a0a93902999f244a838effd4ae09930f456f0a97393416bacb1554c075c1653'
IO = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('previous-packet', 'current-packet', 'original-predictor', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--reference-packet', type=Path)
    parser.add_argument('--initial-seed', type=Path)
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--max-orthogonal-relative', type=float, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    if args.out.exists() or not 1e-8 < args.max_orthogonal_relative <= .01:
        raise ValueError('Use a fresh output and an explicit projected bound in (1e-8,.01]')
    if args.prepare_only != (args.reference_packet is None and args.initial_seed is None):
        raise ValueError('Either prepare the two actual bases or give both actual target inputs')
    if not args.prepare_only and (args.reference_packet is None or args.initial_seed is None):
        raise ValueError('Both the original target seed and true target response are required')
    sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    if sha(HERE/'strong_full_flow_secant_offline_diagnostic.py') != KERNEL_SHA:
        raise ValueError('The frozen graph/transport reader changed')
    if sha(HERE/'strong_full_tangent_tail_worker.mjs') != WORKER_SHA:
        raise ValueError('The frozen storage worker changed')
    import strong_full_flow_secant_offline_diagnostic as kernel
    checks, inputs = {}, {}

    def check(name, condition):
        if not condition:
            raise ValueError('Full-tail offline identity failed: '+name)
        checks[name] = True

    check('original_predictor_source', sha(args.original_predictor) == kernel.PREDICTOR_SHA)
    inputs[str(args.original_predictor)] = kernel.PREDICTOR_SHA

    def packet(label, path):
        saved = kernel.read(path)
        inputs[str(path)] = sha(path)
        request, response = saved['request'], saved['response']
        modes = int(saved['config']['modes'])
        check(label+'_real_complete_converged_tail', request.get('jacobian') is True
              and response.get('converged') is True and not response.get('failed')
              and np.isfinite(response['residual'])
              and 0 <= response['residual'] <= saved['config']['solveTolerance']
              and modes == 32)
        jac = np.asarray(response['heightJetJacobian'], dtype=np.float64)
        check(label+'_complete_height_J', jac.size == (3*modes+2)*modes
              and np.isfinite(jac).all())
        pointer = response['fullFlowTangentSnapshot']
        flow_path = Path(pointer['manifestPath'])
        check(label+'_actual_full_flow_pointer', sha(flow_path) == pointer['manifestSha256']
              and pointer['roundtrip']['allBaseAndFlowValuesBitwiseEqual'] is True)
        flow = kernel.snapshot(flow_path, inputs, check, label)
        manifest, identity, states, height, far, radius, unused = flow
        cp = response['checkpoint']
        nodes = np.asarray(identity['rawNode'], dtype=np.int64)
        check(label+'_complete_checkpoint_and_H_match',
              np.asarray(request['height'], dtype=np.float64).tobytes() == height.tobytes()
              and np.asarray(cp['cutHeight'], dtype=np.float64).tobytes() == height.tobytes()
              and np.array_equal(np.asarray(cp['states'], dtype=np.float64), states)
              and cp['rawNode'] == identity['rawNode']
              and np.array_equal(np.asarray(cp['rawStates'], dtype=np.float64), states[nodes])
              and {k:v for k,v in cp['parameters'].items() if k not in IO} == identity['parameters']
              and manifest['convergedBaseResidual'] == response['residual'])
        return saved, flow

    previous_packet, previous = packet('previous', args.previous_packet)
    current_packet, current = packet('current', args.current_packet)
    ma, ia, sa, ha, far, radius, fa = previous
    mb, ib, sb, hb, farb, radiusb, fb = current
    check('complete_physical_source_stage_and_parameter_identity',
          ma['identityCanonical'] == mb['identityCanonical']
          and radius == radiusb and np.array_equal(far, farb) and sa.shape == sb.shape
          and previous_packet['source_sha256'] == current_packet['source_sha256'])
    check('distinct_real_base_heights', np.isfinite(ha).all() and np.isfinite(hb).all()
          and float((hb-ha)@(hb-ha)) > 0)
    report = dict(schema='projected-two-real-tail-offline-diagnostic-v1', scope=__doc__,
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_sha256={str(Path(__file__)):sha(__file__),
            str(HERE/'strong_full_flow_secant_offline_diagnostic.py'):KERNEL_SHA,
            str(HERE/'strong_full_tangent_tail_worker.mjs'):WORKER_SHA},
        input_sha256=inputs, checks=checks, dimensions=ma['dimensions'],
        complete_tail_identity_sha256=ma['identitySha256'], prepare_only=args.prepare_only,
        actual_base_audits=dict(previous=bool(previous_packet['response'].get('audit')),
                               current=bool(current_packet['response'].get('audit'))),
        base_complete_tail_residuals=[ma['convergedBaseResidual'], mb['convergedBaseResidual']],
        base_prefix_acceptance_not_inferred=True, original_solver_modified=False,
        new_initial_checkpoint_written=False, new_target_accepted=False,
        ODE_Node_Newton_residual_evaluations=0, rigorous_remainder_certified=False,
        existing_collinear_diagnostic_not_transferred=True)
    if not args.prepare_only:
        reference_packet, reference_flow = packet('reference', args.reference_packet)
        mr, ir, reference, target, farr, radiusr, unused = reference_flow
        check('reference_complete_same_tail_identity',
              mr['identityCanonical'] == ma['identityCanonical']
              and reference_packet['source_sha256'] == current_packet['source_sha256'])
        seed = kernel.read(args.initial_seed)
        inputs[str(args.initial_seed)] = sha(args.initial_seed)
        cp = seed['checkpoint']; original_seed = np.asarray(cp['states'], dtype=np.float64)
        indices = np.asarray(ib['rawNode'], dtype=np.int64)
        check('original_unaccepted_seed_full_identity', seed.get('numericalSolutionAccepted') is False
              and original_seed.shape == sb.shape and np.isfinite(original_seed).all()
              and np.asarray(cp['cutHeight'], dtype=np.float64).tobytes() == target.tobytes()
              and cp['rawNode'] == ib['rawNode']
              and np.array_equal(np.asarray(cp['rawStates'], dtype=np.float64), original_seed[indices])
              and {k:v for k,v in cp['parameters'].items() if k not in IO} == ib['parameters'])
        dh, dn = hb-ha, target-hb
        check('distinct_target_height', float(dn@dn) > 0)
        alpha = float(dh@dn/(dh@dh)); orthogonal = dn-alpha*dh
        weights = (2*np.arange(1, len(hb)+1, dtype=np.float64))**2
        relative = float(np.linalg.norm(orthogonal)/np.linalg.norm(dn))
        weighted_relative = float(np.linalg.norm(weights*orthogonal)/np.linalg.norm(weights*dn))
        applicable = (-1.-2e-12 <= alpha <= 2.+2e-12 and
                      max(relative, weighted_relative) <= args.max_orthogonal_relative)
        report['applicability'] = dict(alpha=alpha, declared_alpha_interval=[-1,2],
            orthogonal_relative=relative, frequency_squared_orthogonal_relative=weighted_relative,
            declared_orthogonal_limit=args.max_orthogonal_relative, applicable=applicable,
            earlier_step_H_max=float(np.max(abs(dh))), target_step_H_max=float(np.max(abs(dn))),
            numerical_design_bound_only=True)
        if applicable:
            ga, ta, ca, ba = kernel.graph_transport(fa, far)
            gb, tb, cb, bb = kernel.graph_transport(fb, far)
            check('finite_numerical_graph_inverse_checks', np.isfinite([ca,ba,cb,bb]).all()
                  and max(ba,bb) < 5e-11)
            r4, modes = radius**4, len(hb)
            whole_dq = target/r4-sb[0,:modes]
            linear = sb+kernel.direction(gb, tb, whole_dq)
            linear[0,:modes] = target/r4
            v0, v1 = kernel.direction(ga,ta,dh/r4), kernel.direction(gb,tb,dh/r4)
            delta = sb-sa
            correction = alpha**2*((v0-delta)+2*(v1-delta))+alpha**3*((v0-delta)+(v1-delta))
            cubic = linear+correction; cubic[0,:modes] = target/r4
            check('complete_predicted_state_and_Dirichlet_bits', np.isfinite(cubic).all()
                  and np.array_equal(cubic[0,:modes].view(np.uint64), (target/r4).view(np.uint64)))
            agreement = kernel.stats(linear, original_seed)
            check('original_seed_numerical_formula_agreement',
                  agreement['max_absolute'] < 1e-11*max(1.,float(np.max(abs(original_seed))))
                  and agreement['max_node_relative'] < 1e-10)
            first, predicted = kernel.stats(original_seed,reference), kernel.stats(cubic,reference)
            report.update(original_formula_numpy_agreement=agreement,
                original_archived_seed_error=first, projected_cubic_error=predicted,
                improvements={k:(first[k]/predicted[k] if predicted[k] else None) for k in
                    ('max_absolute','max_node_relative','rms_node_relative','cut_pi_max_absolute')},
                formula='Original current full tangent, including the complete orthogonal H component, plus alpha^2*((v0-d)+2*(v1-d))+alpha^3*((v0-d)+(v1-d)); d=current_state-previous_state.',
                numerical_graph_checks=dict(previous_condition=ca,current_condition=cb,
                    previous_inverse_backward=ba,current_inverse_backward=bb),
                far_linear_boundary_defects=dict(
                    original_seed=float(np.max(abs(original_seed[-1,modes:]-far*original_seed[-1,:modes]))),
                    projected_cubic=float(np.max(abs(cubic[-1,modes:]-far*cubic[-1,:modes])))),
                reference_residual=reference_packet['response']['residual'],
                reference_has_actual_audit=bool(reference_packet['response'].get('audit')))
        else:
            report['comparison_not_run_reason'] = 'Explicit projected trust condition failed; no mathematical nonexistence conclusion follows.'
    report['elapsed_seconds'] = time.monotonic()-started
    report['all_checks'] = True; report['command'] = sys.argv
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('x') as stream:
        json.dump(report, stream, indent=2, allow_nan=False); stream.write('\n')
    print(json.dumps(dict(out=str(args.out),sha256=sha(args.out),checks=len(checks),
        prepare_only=args.prepare_only,improvements=report.get('improvements'),
        applicability=report.get('applicability'),elapsed_seconds=report['elapsed_seconds'])), flush=True)


if __name__ == '__main__':
    main()
