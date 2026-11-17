#!/usr/bin/env python3
"""Keep named residual/Jacobian evidence, identities and scalar resource data."""
import argparse
import json
from pathlib import Path
from record_fixed_actual import load, scalar_tree, sha


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('locator', 'jacobian', 'locator-resource', 'jacobian-resource', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    a = p.parse_args()
    loc, jac = load(a.locator), load(a.jacobian)
    if loc['inputAccepted'] or jac['statesChanged'] or jac['originalSolverInvoked']:
        raise ValueError('Read-only failure diagnosis only')
    if not loc['input_sha256'] == jac['input_sha256']:
        raise ValueError('Different complete finite states')
    if not loc['replayNormalizedResidual'] == loc['inputLastIteration']['norm'] == jac['fullStateStoppingResidual']:
        raise ValueError('Stopping-state replay mismatch')
    if loc['originalGate'] != jac['originalGate'] or jac['originalGate'] != 2e-9:
        raise ValueError('Original gate mismatch')
    if jac['locator_sha256'] != sha(a.locator):
        raise ValueError('Jacobian probe used another locator')
    resources = {key: load(path) for key, path in
                 (('locator', a.locator_resource), ('jacobian', a.jacobian_resource))}
    if any(r['status'] != 'observed_terminal' or r['child_returncode'] != 0
           for r in resources.values()):
        raise ValueError('Both read-only processes need successful observed terminals')
    for path, digest in jac['source_sha256'].items():
        if sha(path) != digest:
            raise ValueError('Execution source changed: ' + path)
    rows = jac['selectedRows']
    largest = max(rows, key=lambda r: r['oneInputUlpLinearizedOutputMaxOverOriginalGate'])
    largest_diagonal = max(rows, key=lambda r: abs(r['diagonalAnalyticDerivative']))
    result = dict(
        scope='Read-only original full-Jacobian residual replay and selected local analytic sensitivities for one complete failed .5H tail. ULP derivative scales motivate a discretization experiment; they are not nonlinear rounding bounds, an impossibility result, or an accepted tail.',
        collector_sha256=sha(__file__), input=loc['input'],
        input_sha256=loc['input_sha256'], input_failure=loc['inputFailure'],
        last_original_iteration=loc['inputLastIteration'],
        original_gate=loc['originalGate'], exact_full_replay=loc['replayNormalizedResidual'],
        modes=jac['modes'], spacing=jac['spacing'], quadrature=jac['quadrature'],
        parts=jac['parts'], steps=jac['steps'], stages=jac['stages'],
        primary_residual_row=loc['largestResidual'][0],
        secondary_residual_row=loc['largestResidual'][1],
        lowest_A_row=loc['lowestA'][0], minA=loc['minA'], minD=loc['minD'],
        far_robin_residual_max=loc['endResidualMax'],
        local_jacobian_selected_count=len(rows),
        largest_named_input_ulp_sensitivity=largest,
        largest_named_diagonal_sensitivity=largest_diagonal,
        all_named_ulp_scales_below_original_gate=all(
            r['oneInputUlpLinearizedOutputMaxOverOriginalGate'] < 1 for r in rows),
        states_changed=False, new_solver_invoked=False,
        source_sha256=jac['source_sha256'],
        run_summary_sha256=jac['run_summary_sha256'],
        full_locator_sha256=sha(a.locator), full_jacobian_diagnostic_sha256=sha(a.jacobian),
        actual_commands={key: value['command'] for key, value in resources.items()},
        observed_resources={key: scalar_tree(value) for key, value in resources.items()},
        resource_hashes=dict(locator=sha(a.locator_resource), jacobian=sha(a.jacobian_resource)),
        scope_of_jacobian='Analytic derivative at the saved state, using the original full-Jacobian flow path. Multiplication by an input ULP is linearized sensitivity only. Mixed-unit row sums are not invariant condition numbers.',
        data_policy='Only two named residual rows, the minimum-A row, two named Jacobian diagnostics and scalar provenance are retained. Complete states, all selected rows and matrices remain scratch-only.')
    a.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    if a.out.stat().st_size >= 100000:
        raise ValueError('Compact record exceeds 100 KB')
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out))))


if __name__ == '__main__':
    main()
