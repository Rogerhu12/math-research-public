#!/usr/bin/env python3
"""Bind the existing map-consistency probe to a new recorded finite failure."""
import argparse
import json
from pathlib import Path
from record_fixed_actual import load, scalar_tree, sha


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('diagnostic', 'resource', 'terminal-record', 'source-topic', 'probe', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    a = p.parse_args()
    raw, resource, terminal = load(a.diagnostic), load(a.resource), load(a.terminal_record)
    input_path = Path(raw['input'])
    native = load(input_path)
    if resource['status'] != 'observed_terminal' or resource['child_returncode'] != 0:
        raise ValueError('The existing read-only probe needs an observed successful terminal')
    if not native['response'].get('failed') or terminal['accepted_tail_response_count']:
        raise ValueError('This record describes an original failed tail only')
    if raw['input_sha256'] != sha(input_path):
        raise ValueError('Diagnostic input identity mismatch')
    prior = terminal['tail_responses'][input_path.name]
    if prior['sha256'] != raw['input_sha256'] or prior['accepted']:
        raise ValueError('Published terminal and diagnostic refer to different states')
    if raw['normalized_variational_residual'] != native['response']['lastIteration']['norm']:
        raise ValueError('Original stopping path was not exactly replayed')
    if native['config']['solveTolerance'] != 2e-9 or raw['rhsEvaluation'] != 'split-linear-flux-v1':
        raise ValueError('Original split worker and gate required')
    for key in ('modes', 'quadrature', 'steps', 'shootingParts'):
        if raw[key] != native['config'][key]:
            raise ValueError('Discretization differs: ' + key)
    sources = {str(a.probe.resolve()): sha(a.probe)}
    for name, digest in native['source_sha256'].items():
        path = (a.source_topic / 'scripts' / name).resolve()
        if sha(path) != digest:
            raise ValueError('Original native source changed: ' + str(path))
        sources[str(path)] = digest
    for name, digest in terminal['periodic_engine_sha256'].items():
        path = (a.source_topic / 'scripts/periodic-quadrature' / name).resolve()
        if sha(path) != digest:
            raise ValueError('Periodic source changed: ' + str(path))
        sources[str(path)] = digest
    result = dict(
        scope='A new-state read-only application of the existing published split-worker map-consistency script. Both original stopping/full-Jacobian and original state-only line-search maps are evaluated at exactly the same saved failed state, without a Newton step, source edit or gate change.',
        collector_sha256=sha(__file__), prior_terminal_record_sha256=sha(a.terminal_record),
        input=str(input_path.resolve()), input_sha256=raw['input_sha256'],
        input_failure=native['response']['failed'], last_original_iteration=native['response']['lastIteration'],
        original_gate=native['config']['solveTolerance'],
        probe_sha256=sha(a.probe), source_sha256=sources,
        full_diagnostic_sha256=sha(a.diagnostic),
        original_discretization={k: native['config'][k] for k in
                                 ('modes', 'spacing', 'quadrature', 'depth', 'steps', 'shootingParts')},
        normalized_full_jacobian_residual=raw['normalized_variational_residual'],
        normalized_state_only_residual=raw['normalized_state_only_residual'],
        all_compared_state_outputs_have_zero_numeric_difference=(raw['max_map_difference']['normalized_map_difference'] == 0),
        residual_norms_numerically_identical=(raw['normalized_variational_residual'] == raw['normalized_state_only_residual']),
        largest_map_difference=raw['max_map_difference'],
        worst_full_jacobian_residual=raw['worst_variational_residual'],
        worst_state_only_residual=raw['worst_state_only_residual'],
        largest_stage_jacobian=raw['largest_stage_jacobian'],
        matrix_scope='An infinity norm of one mixed-unit local Jacobian is not a full BVP condition number. Zero numeric output difference does not assert bytewise equality of signed zero encodings.',
        states_changed=False, new_solver_invoked=False, accepted=False,
        actual_command=resource['command'], resource=scalar_tree(resource),
        resource_sha256=sha(a.resource),
        data_policy='The existing probe emits only named extrema. Full states and matrices remain scratch-only; only scalar diagnostics, original parameters and source/output hashes are recorded.')
    a.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    if a.out.stat().st_size >= 100000:
        raise ValueError('Compact record exceeds 100 KB')
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out),
                          identical=result['residual_norms_numerically_identical'])))


if __name__ == '__main__':
    main()
