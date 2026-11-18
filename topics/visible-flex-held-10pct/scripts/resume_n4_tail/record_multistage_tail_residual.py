#!/usr/bin/env python3
"""Bind a completed full replay and its few named above-gate stage rows.

No numerical map is evaluated.  The displayed per-component ULP counts are
finite diagnostics, not an arithmetic error bound or an impossibility result.
"""
import argparse
import hashlib
import json
from pathlib import Path
from record_fixed_actual import load, scalar_tree, sha


def identity(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('input', 'locator', 'resource', 'log', 'run-summary',
                'terminal-record', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    a = p.parse_args()
    raw, located = load(a.input), load(a.locator)
    resource, run = load(a.resource), load(a.run_summary)
    terminal = load(a.terminal_record)
    if not raw['response'].get('failed') or located['inputAccepted']:
        raise ValueError('This is a read-only diagnosis of a complete failed solve')
    if located['input_sha256'] != sha(a.input) or terminal['output']['sha256'] != sha(a.input):
        raise ValueError('The preceding terminal and locator must bind the same complete state')
    if not located['replayNormalizedResidual'] == raw['response']['lastIteration']['norm'] == located['inputLastIteration']['norm']:
        raise ValueError('Original full replay does not reproduce its stopping value')
    if located['originalGate'] != raw['config']['solveTolerance'] or located['originalGate'] != 2e-9:
        raise ValueError('Original gate changed')
    if resource['status'] != 'observed_terminal' or resource['child_returncode'] != 0:
        raise ValueError('The full read-only process needs an observed successful terminal')
    sources = {**terminal['source_sha256'], **located['source_sha256']}
    topic = Path(resource['command'][-3]).resolve()
    for name, digest in run['periodic_engine_sha256'].items():
        sources[str(topic/'scripts/periodic-quadrature'/name)] = digest
    for path, digest in sources.items():
        if sha(path) != digest:
            raise ValueError('Execution source changed: ' + path)
    rows = located['largestResidual']
    if any(rows[i]['normalizedResidual'] < rows[i+1]['normalizedResidual']
           for i in range(len(rows)-1)):
        raise ValueError('The original retained stage ranking is not decreasing')
    above = [row for row in rows if row['normalizedResidual'] >= located['originalGate']]
    if len(above) == len(rows):
        raise ValueError('The retained rows do not bound the total above-gate stage count')
    if len({row['stage'] for row in above}) != len(above):
        raise ValueError('The locator must retain one maximum row per distinct stage')
    if located['endResidualMax'] >= located['originalGate']:
        raise ValueError('A separate far-boundary obstruction needs explicit treatment')
    groups = []
    for stage in sorted(row['stage'] for row in above):
        if not groups or stage != groups[-1][-1] + 1:
            groups.append([stage])
        else:
            groups[-1].append(stage)
    result = dict(
        scope=__doc__, collector=identity(__file__), helper=identity(Path(__file__).with_name('record_fixed_actual.py')),
        input=identity(a.input), preceding_terminal=identity(a.terminal_record),
        locator=identity(a.locator), full_replay=located['replayNormalizedResidual'],
        original_gate=located['originalGate'], last_original_iteration=located['inputLastIteration'],
        stages=located['stages'], modes=located['modes'], quadrature=located['quadrature'],
        shooting_parts=located['shootingParts'],
        above_gate_stage_count=len(above),
        above_gate_count_scope='Exactly this many stage maxima exceed the original gate: the retained list is descending and its next row is below the gate. More than one component in a named stage may exceed the gate; no total component count is asserted.',
        named_above_gate_rows={str(row['stage']): row for row in above},
        next_ranked_stage=rows[len(above)],
        peak_is_unique_among_stage_maxima=rows[0]['normalizedResidual'] > rows[1]['normalizedResidual'],
        adjacent_stage_groups=groups,
        dependency='A change to an interior node j changes its target residual row j and the preceding flow-input row j-1. Adjacent named peaks must not be treated as independent moves.',
        all_named_component_one_ulp_scales_below_gate=all(row['ulpDividedByScale'] < located['originalGate'] for row in above),
        ulp_scope='Finite binary64 component spacing and observed residual counts only. They do not identify a root/RK rounding error, prove a nonlinear perturbation bound, or establish a machine-precision lower bound.',
        lowest_A_row=located['lowestA'][0], minA=located['minA'], minD=located['minD'],
        far_robin_residual_max=located['endResidualMax'],
        source_sha256=sources, baseline_periodic_manifest=identity(a.run_summary),
        original_command=resource['command'], resource=scalar_tree(resource),
        resource_identity=identity(a.resource), log_sha256=sha(a.log),
        states_changed=False, new_solver_invoked=False,
        data_policy='Only the few specifically used above-gate scalar rows and identity hashes are retained; complete states, full sorted tables and matrices remain scratch-only.')
    a.out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    if a.out.stat().st_size >= 100000:
        raise ValueError('Compact record must stay below 100 KB')
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out),
                          above_gate_stage_count=len(above))))


if __name__ == '__main__':
    main()
