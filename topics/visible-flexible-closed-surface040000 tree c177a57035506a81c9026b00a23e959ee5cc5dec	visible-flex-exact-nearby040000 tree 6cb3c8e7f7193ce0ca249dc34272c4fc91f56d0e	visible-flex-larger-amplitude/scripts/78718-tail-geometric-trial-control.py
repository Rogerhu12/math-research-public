"""Classify a completed geometric-trial failure for the existing H controller.

This controls whether a numerical failure may request a smaller H increment.
It neither accepts a DN response nor changes its equations or success test.
Original trace rows are kept verbatim; geometric construction failures are
never relabelled as residual/ODE evaluation failures.
"""


def classify_failure(record, call, rows, original, max_iterations=36):
    unchanged = original.classify_original_failure(record, call, rows, max_iterations)
    if unchanged is not None:
        return unchanged
    response, request = record['response'], record['request']
    if (request['jacobian'] is not False or request['audit'] is not False
            or max_iterations != 36 or not isinstance(rows, list)):
        return None
    checkpoint = response.get('checkpoint')
    if not isinstance(checkpoint, dict):
        return None
    depth = checkpoint.get('parameters', {}).get('depth')
    if not original.int_value(depth):
        return None
    known_causes = original.KNOWN_MOMENTUM_ERRORS | {
        'Error: initial full mean root failed',
        'Error: initial mean iteration limit',
        'Error: Geometric seeded full mean root failed',
        'Error: Geometric seeded mean iteration limit',
        'Error: Geometric retraction Gram matrix is not SPD',
    }
    geometric_rows = 0
    for row in rows:
        if (not isinstance(row, dict) or not original.int_value(row.get('call'))
                or row['call'] != call or not original.int_value(row.get('iteration'))
                or not original.int_value(row.get('trial'))
                or not 0 <= row['iteration'] < max_iterations
                or not 0 <= row['trial'] < 10
                or not original.number(row.get('step'))
                or row['step'] != 2.0 ** (-row['trial'])
                or not original.number(row.get('baseNorm')) or row['baseNorm'] < 0):
            return None
        kind = row.get('kind')
        if kind == 'geometric-trial-construction-rejection':
            node, cause = row.get('node'), row.get('cause')
            if (row.get('phase') != 'trial-construction'
                    or not original.int_value(node) or not 0 <= node <= depth
                    or cause not in known_causes
                    or row.get('error') not in {
                        f'Error: Geometric retraction preparation at node {node}: {cause}',
                        f'Error: Geometric retraction trial at node {node}: {cause}'}):
                return None
            geometric_rows += 1
        elif kind in ('momentum-guard-rejection', 'momentum-root-solver-rejection'):
            if row.get('error') not in original.KNOWN_MOMENTUM_ERRORS:
                return None
        elif kind in ('accepted', 'residual-not-decreasing'):
            if (not original.number(row.get('trialNorm')) or row['trialNorm'] < 0
                    or ((row['trialNorm'] < row['baseNorm']) != (kind == 'accepted'))):
                return None
        else:
            return None
    if not geometric_rows:
        return None
    if 'failed' not in response:
        history = response.get('history')
        if (response.get('converged') is not False or not isinstance(history, list)
                or len(history) != max_iterations):
            return None
        for iteration, saved in enumerate(history):
            if (not isinstance(saved, dict) or not original.int_value(saved.get('iteration'))
                    or saved['iteration'] != iteration or not original.number(saved.get('norm'))
                    or saved['norm'] < 0 or not original.number(saved.get('step'))):
                return None
        if not original.complete_trial_groups(rows, max_iterations, history=history):
            return None
        groups, kind = max_iterations, 'geometric-trial-complete-nonconvergence'
    else:
        if set(response) != {'failed', 'lastIteration', 'checkpoint'}:
            return None
        last = response['lastIteration']
        if (not isinstance(last, dict) or not original.int_value(last.get('iteration'))
                or not 0 <= last['iteration'] < max_iterations
                or not original.number(last.get('norm'))):
            return None
        prefix = 'Error: multiple-shooting line search failed at '
        failure = response['failed']
        if not isinstance(failure, str) or not failure.startswith(prefix):
            return None
        try:
            if float(failure[len(prefix):]) != last['norm']:
                return None
        except ValueError:
            return None
        groups = last['iteration'] + 1
        if not original.complete_trial_groups(rows, groups, failed_last=True,
                                               last_norm=last['norm']):
            return None
        kind = 'geometric-trial-known-ten-trial-rejection'
    return {'kind': kind, 'trial_rows': len(rows), 'iteration_groups': groups,
            'geometric_construction_rejection_rows': geometric_rows,
            'closed_call_trial_rows_sha256': original.digest(rows),
            'scope': 'Numerical H subdivision only; no assertion that the original ODE or geometric problem has no solution.'}
