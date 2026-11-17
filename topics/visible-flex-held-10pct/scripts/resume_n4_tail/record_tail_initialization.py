#!/usr/bin/env python3
"""Bind one completed local-tail initialization to its unchanged original solve.

This collector records source and whole-state identities, small selected
coordinate changes, and scalar outcomes.  It neither runs a solver nor treats
a local residual decrease as an accepted nonlinear tail.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import struct
from record_fixed_actual import load, scalar_tree, sha


def numeric_identity(value):
    """Canonical recursive identity preserving every binary64 numeric value."""
    if value is None or isinstance(value, (str, bool)):
        return value
    if isinstance(value, (int, float)):
        return ('binary64', struct.pack('<d', value).hex())
    if isinstance(value, list):
        return [numeric_identity(v) for v in value]
    if isinstance(value, dict):
        return {k: numeric_identity(value[k]) for k in sorted(value)}
    raise TypeError(type(value))


def finite_entries(value):
    if isinstance(value, list):
        return sum(finite_entries(v) for v in value)
    if isinstance(value, dict):
        return sum(finite_entries(v) for v in value.values())
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if not math.isfinite(value):
            raise ValueError('Non-finite analytic Jacobian entry')
        return 1
    raise ValueError('Expected numeric full-Jacobian entries')


def identity(path):
    return dict(path=str(path.resolve()), sha256=sha(path))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('input', 'summary', 'output', 'resource', 'log', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    a = p.parse_args()
    before, after = load(a.input), load(a.output)
    summary, resource = load(a.summary), load(a.resource)
    if resource['status'] != 'observed_terminal':
        raise ValueError('An observed process terminal is required')
    if summary['input_sha256'] != sha(a.input):
        raise ValueError('Initializer summary belongs to another input')
    if summary['output_record_sha256'] != sha(a.output):
        raise ValueError('Initializer summary belongs to another output')
    if not before['response'].get('failed'):
        raise ValueError('Original input must be a complete failed solve')
    if not summary['all_physical_and_solver_parameters_unchanged']:
        raise ValueError('This collector is restricted to state initialization')
    if numeric_identity(before['config']) != numeric_identity(after['config']):
        raise ValueError('Physical or numerical configuration changed')
    old_height = before['response']['checkpoint']['cutHeight']
    if numeric_identity(old_height) != numeric_identity(after['request']['height']):
        raise ValueError('The complete requested physical height changed')
    if not after['request']['jacobian'] or not after['request']['audit']:
        raise ValueError('The original full Jacobian and audit must be requested')
    if not summary['original_gate'] == before['config']['solveTolerance'] == 2e-9:
        raise ValueError('This branch retains the original 2e-9 gate')
    if summary['before']['norm'] != before['response']['lastIteration']['norm']:
        raise ValueError('Full replay does not match the recorded stopping state')
    for name, digest in summary['source_sha256'].items():
        if sha(name) != digest:
            raise ValueError('Recorded execution source changed: ' + name)
    if after['execution_source_sha256'] != summary['source_sha256']:
        raise ValueError('Output execution source bindings disagree')
    response = after.get('response')
    accepted = bool(response and response.get('converged') and not response.get('failed'))
    invoked = summary['original_solver_invoked']
    jacobian_entries = None
    if accepted:
        if not invoked or not summary['original_solver_converged']:
            raise ValueError('Acceptance must come from the unchanged original solver')
        if not response['residual'] < summary['original_gate']:
            raise ValueError('The original finite residual gate did not pass')
        if response['residual'] != summary['final_residual']:
            raise ValueError('Final residual identity mismatch')
        if not response['audit']:
            raise ValueError('The complete original audit is missing')
        jacobian_entries = finite_entries(response['heightJetJacobian'])
        if jacobian_entries == 0:
            raise ValueError('Empty analytic Jacobian')
    if invoked and not accepted and not response.get('failed'):
        raise ValueError('Expected either the original acceptance or a recorded failure')
    if response and response.get('checkpoint'):
        if numeric_identity(response['checkpoint']['cutHeight']) != numeric_identity(old_height):
            raise ValueError('Output checkpoint changed the requested height')
    history = (response or {}).get('history') or []
    finite_cfg = {k: before['config'][k] for k in
                  ('modes', 'spacing', 'quadrature', 'depth', 'shootingParts',
                   'steps', 'auditSteps', 'maxIterations', 'solveTolerance')
                  if k in before['config']}
    selected = summary.get('selected')
    passes = []
    for row in summary.get('passes', []):
        passes.append({k: row[k] for k in
                       ('pass', 'before_norm', 'peak', 'local_trial_count', 'selected')
                       if k in row})
    result = dict(
        scope='A completed declared internal-state initializer followed, only after strict complete residual improvement, by the unchanged original finite nonlinear DN solve and audit. A local decrease, process exit code, or saved failed checkpoint is not acceptance. No coupled prefix, exact circular arc, continuous certificate, closure or reach is inferred.',
        collector_sha256=sha(__file__), command=summary['command'],
        input=identity(a.input), output=identity(a.output),
        unabridged_scratch_summary=identity(a.summary),
        source_sha256=summary['source_sha256'],
        original_discretization=finite_cfg,
        original_configuration_and_all_cut_heights_bitwise_unchanged=True,
        cut_height_count=len(old_height),
        cut_height_float64_le_sha256=hashlib.sha256(
            struct.pack('<' + 'd' * len(old_height), *old_height)).hexdigest(),
        baseline=summary['before'],
        prescribed_alpha_candidates=summary['alphas'],
        prescribed_beta_candidates=summary['betas'],
        selected_single_pass=selected, selected_passes=passes,
        local_trial_count=summary.get('local_trial_count'),
        local_sequence_stopped=summary.get('stopped'),
        complete_candidate_replay=summary['full_candidate_replay'],
        original_solver_invoked=invoked, original_solver_accepted=accepted,
        original_solver_error=(response or {}).get('failed'),
        last_original_iteration=((history[-1] if history else None) or
                                 (response or {}).get('lastIteration')),
        final_residual=(response or {}).get('residual'),
        original_audit=scalar_tree((response or {}).get('audit') or {}),
        full_analytic_jacobian_finite_entries=jacobian_entries,
        complete_original_state_saved=bool((response or {}).get('checkpoint')),
        state_stage_count=len(((response or {}).get('checkpoint') or {}).get('states', [])),
        process_resource=scalar_tree(resource), process_resource_sha256=sha(a.resource),
        resource_scope='RUSAGE_CHILDREN and sampled namespace process observations retain their own semantics; neither is a whole-host process-tree peak or an OOM diagnosis.',
        execution_log_sha256=sha(a.log), seconds=summary['seconds'],
        coupled_prefix_solved=False,
        data_policy='Only selected coordinates, scalar outcomes, small solver parameters and hashes are retained. Full states, complete trial tables and meshes remain scratch-only.')
    a.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    if a.out.stat().st_size >= 100000:
        raise ValueError('Compact record must stay below 100 KB')
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out),
                          original_solver_accepted=accepted)))


if __name__ == '__main__':
    main()
