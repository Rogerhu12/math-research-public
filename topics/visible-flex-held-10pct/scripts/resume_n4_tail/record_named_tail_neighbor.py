#!/usr/bin/env python3
"""Record one prescribed interior binary64 neighbor and its original DN result.

This reads completed output only.  It never evaluates a tail or promotes the
two affected local rows to a nonlinear-tail acceptance.  The original solver,
its full residual, height-jet Jacobian and audit are the sole finite outcome.
"""
import argparse
import hashlib
import math
from pathlib import Path
import struct
import json

from record_fixed_actual import load, scalar_tree, sha
from record_tail_initialization import numeric_identity, finite_entries


def identity(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('input', 'diagnostic', 'summary', 'output', 'resource', 'log',
                'baseline-record', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    a = p.parse_args()
    before, after = load(a.input), load(a.output)
    diagnostic, summary = load(a.diagnostic), load(a.summary)
    resource, baseline = load(a.resource), load(a.baseline_record)
    if resource['status'] != 'observed_terminal' or resource['child_returncode'] != 0:
        raise ValueError('The original process must have an observed clean terminal')
    if not before['response'].get('failed'):
        raise ValueError('Expected the complete diagnosed failed original solve')
    if summary['input_sha256'] != sha(a.input) or diagnostic['input_sha256'] != sha(a.input):
        raise ValueError('Diagnostic/initializer input identity mismatch')
    if summary['diagnostic_sha256'] != sha(a.diagnostic):
        raise ValueError('Named diagnostic identity mismatch')
    if summary['output_record_sha256'] != sha(a.output):
        raise ValueError('Original output identity mismatch')
    if not any(row['sha256'] == sha(a.input) for row in baseline['tail_responses'].values()):
        raise ValueError('The preceding terminal record does not bind this failed state')
    if numeric_identity(before['config']) != numeric_identity(after['config']):
        raise ValueError('The complete physical or numerical configuration changed')
    if not summary['originalGate'] == before['config']['solveTolerance'] == 2e-9:
        raise ValueError('The original 2e-9 residual gate changed')
    initial_norm = before['response']['lastIteration']['norm']
    if not summary['originalFullReplayResidual'] == diagnostic['replayNormalizedResidual'] == initial_norm:
        raise ValueError('Original complete stopping replay is not identical')
    for path, digest in summary['source_sha256'].items():
        if sha(path) != digest:
            raise ValueError('A bound execution source changed: ' + path)
    for path, digest in diagnostic['source_sha256'].items():
        if summary['source_sha256'].get(path) != digest:
            raise ValueError('A bound shared/periodic/native source was omitted')
    if after['execution_source_sha256'] != summary['source_sha256']:
        raise ValueError('Output execution source provenance differs')
    if after['source_sha256'] != before['source_sha256']:
        raise ValueError('The inherited native worker source bindings changed')
    if not after['request']['jacobian'] or not after['request']['audit']:
        raise ValueError('Original full Jacobian and audit were not requested')
    height = before['response']['checkpoint']['cutHeight']
    if numeric_identity(height) != numeric_identity(before['request']['height']):
        raise ValueError('The failed checkpoint and its original request disagree')
    if numeric_identity(height) != numeric_identity(after['request']['height']):
        raise ValueError('A physical cut-height component changed')
    peak, candidate = diagnostic['largestResidual'][0], summary['candidate']
    for key, expected in [('stage', peak['stage']), ('component', peak['component']),
                          ('oldValue', peak['stateValue']), ('newValue', peak['flowValue'])]:
        if candidate[key] != expected:
            raise ValueError('The candidate differs from the prescribed original flow value')
    if math.nextafter(candidate['oldValue'], candidate['newValue']) != candidate['newValue']:
        raise ValueError('The prescribed change is not exactly one binary64 neighbor')
    if candidate['absoluteChange'] != candidate['newValue'] - candidate['oldValue']:
        raise ValueError('Candidate signed difference mismatch')
    states = before['response']['checkpoint']['states']
    if not 0 < candidate['stage'] < len(states) - 1:
        raise ValueError('Only a free interior node may change in this initializer')
    if states[candidate['stage']][candidate['component']] != candidate['oldValue']:
        raise ValueError('The named starting coordinate differs')
    expected_rows = [candidate['stage'] - 1, candidate['stage']]
    if any([row['stage'] for row in summary[key]] != expected_rows for key in
           ('affectedStagesBefore', 'affectedStagesAfter')):
        raise ValueError('The two original affected residual rows were not both checked')
    response = after['response']
    accepted = bool(response.get('converged') and not response.get('failed'))
    if accepted != summary['originalSolverConverged']:
        raise ValueError('Reported acceptance differs from the original returned result')
    M = before['config']['modes']
    entries = None
    if accepted:
        if not response['residual'] == summary['finalResidual'] < 2e-9:
            raise ValueError('Original complete nonlinear residual did not pass')
        if not response.get('audit') or response['audit'] != summary['audit']:
            raise ValueError('The complete original returned audit is missing or differs')
        entries = finite_entries(response['heightJetJacobian'])
        if entries != (3 * M + 2) * M:
            raise ValueError('The original height-jet Jacobian dimensions or entries differ')
    elif not response.get('failed'):
        if (response.get('converged') is not False or
                not math.isfinite(response.get('residual', math.nan)) or
                response['residual'] != summary.get('finalResidual')):
            raise ValueError('Expected original acceptance, nonconvergence, or recorded failure')
    checkpoint = response.get('checkpoint')
    if checkpoint and numeric_identity(checkpoint['cutHeight']) != numeric_identity(height):
        raise ValueError('The output checkpoint cut height changed')
    history = response.get('history') or []
    iteration_log = []
    for line in a.log.read_text().splitlines():
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if row.get('event') == 'original_solve_iteration' and not row.get('phase'):
            iteration_log.append({k: v for k, v in row.items() if k != 'event'})
    if not iteration_log:
        raise ValueError('The original solver complete-residual progress is missing')
    last = history[-1] if history else response.get('lastIteration')
    if last and iteration_log[-1]['norm'] != last['norm']:
        raise ValueError('Last original full-residual log disagrees with the returned state')
    result = dict(
        scope='One prescribed free interior one-ULP initial value, followed by the original complete finite nonlinear DN solve, original Jacobian calculation and original audit. Local row improvements and process exit alone are not acceptance. This record supplies no coupled prefix, full target-height acceptance, exact arc, closure or continuous certificate.',
        collector=identity(__file__),
        collector_helpers={name: sha(Path(__file__).with_name(name)) for name in
                           ('record_fixed_actual.py', 'record_tail_initialization.py')},
        command=summary['command'], input=identity(a.input),
        diagnostic=identity(a.diagnostic), output=identity(a.output),
        preceding_terminal=identity(a.baseline_record),
        unabridged_summary=identity(a.summary), source_sha256=summary['source_sha256'],
        original_configuration_and_all_cut_heights_bitwise_unchanged=True,
        original_discretization={k: before['config'][k] for k in
            ('modes', 'spacing', 'quadrature', 'depth', 'shootingParts', 'steps',
             'auditSteps', 'maxIterations', 'solveTolerance') if k in before['config']},
        complete_cut_height_count=len(height),
        complete_cut_height_float64_le_sha256=hashlib.sha256(
            struct.pack('<' + 'd' * len(height), *height)).hexdigest(),
        original_stopping_full_replay_residual=initial_norm,
        prescribed_candidate=candidate, initialization_boundary_nodes_unchanged=True,
        affected_original_rows_before=summary['affectedStagesBefore'],
        affected_original_rows_after=summary['affectedStagesAfter'],
        original_solver_invoked=True, original_solver_accepted=accepted,
        original_outcome=('accepted' if accepted else 'exception' if response.get('failed')
                          else 'returned_not_converged'),
        original_solver_error=response.get('failed'), final_residual=response.get('residual'),
        first_original_iteration=iteration_log[0],
        last_original_iteration=last,
        original_full_residual_iteration_count=len(iteration_log),
        original_height_jet_jacobian_finite_entries=entries,
        original_audit_diagnostics=scalar_tree(response.get('audit') or {}),
        audit_scope='The unchanged original audit output is retained as diagnostics; no new full-domain tensor bound or extra acceptance test is inferred.',
        solver_minA=summary.get('minA'), solver_minD=summary.get('minD'),
        complete_original_state_saved=bool(checkpoint),
        state_node_count=len(checkpoint['states']) if checkpoint else None,
        process_resource=scalar_tree(resource), process_resource_sha256=sha(a.resource),
        execution_log_sha256=sha(a.log),
        resource_scope='RUSAGE_CHILDREN and sampled namespace RSS keep their original semantics; neither establishes a whole-host process-tree peak.',
        coupled_prefix_solved=False,
        data_policy='Only prescribed coordinates, small numerical parameters, scalar diagnostics and hashes are published; complete states and fields remain scratch-only.')
    a.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    if a.out.stat().st_size >= 100000:
        raise ValueError('Compact record must stay below 100 KB')
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out), accepted=accepted)))


if __name__ == '__main__':
    main()
