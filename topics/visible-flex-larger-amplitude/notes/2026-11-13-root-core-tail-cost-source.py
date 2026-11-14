#!/usr/bin/env python3
"""Diagnose the finite core-tail control cost without any geometry constraints.

Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
Consumes the completed fine32/coarse-six proxy unchanged. This small LP only
identifies a useful direction for subsequent complete geometric screening.
It is floating design evidence, neither a no-solution proof nor a new field.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
import numpy as np
from scipy.optimize import linprog


def read(p):
    raw = Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--proxy', type=Path, required=True)
    p.add_argument('--proxy-resource', type=Path, required=True)
    p.add_argument('--fine', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Keep the earlier actual diagnostic unchanged')
    start = time.monotonic()
    proxy, result, fine = map(read, (a.proxy, a.proxy_resource, a.fine))
    meta = proxy['full_core_tail_proxy_adapter']
    if (result['exitcode'] != 0 or result.get('termination_signal') is not None
            or sha(a.fine) != meta['accepted_fine_core_sha256']
            or not fine['solver_success'] or fine['audit_pending']
            or not meta['tail_proxy_core_centre_is_fine32']
            or not meta['geometric_row_centre_remains_original_coarse28']):
        raise ValueError('The original accepted fine core and completed proxy are required')
    core = np.array(fine['core']['coefficients'])
    modes = np.array(meta['actual_physical_frequencies'])
    slopes = np.array(meta['normalized_complete_core_slopes'])
    names = meta['complete_control_order']
    if names != ['actual_q1', 'actual_q4', 'actual_c6', 'vu',
                 'descending_turn_curvature', 'start_acceleration']:
        raise ValueError('Exactly the six original actual columns are required')
    if slopes.shape != (32, 6) or not np.all(slopes[28:] == 0):
        raise ValueError('The four actual fine baseline modes must stay present with zero increments')
    cutoffs = [16, 24, 32, 40, 48]
    tails = {k: sum(Fraction.from_float(abs(float(c))) * (int(m)**2 - 1)
                   for c, m in zip(core, modes) if m >= k) for k in cutoffs}
    ix = np.flatnonzero(modes >= min(cutoffs))
    scale = float(max(tails.values()))
    weights = modes[ix]**2 - 1
    centre, derivative = weights*core[ix]/scale, weights[:, None]*slopes[ix]/scale
    nz = len(ix)
    # Columns: six normalized controls, positive auxiliaries, common factor.
    pos = np.column_stack((derivative, -np.eye(nz), np.zeros(nz)))
    neg = np.column_stack((-derivative, -np.eye(nz), np.zeros(nz)))
    tailrows = np.array([np.r_[np.zeros(6), modes[ix] >= k, -float(tails[k])/scale]
                         for k in cutoffs], dtype=float)
    matrix = np.vstack((pos, neg, tailrows))
    rhs = np.r_[-centre, centre, np.zeros(len(cutoffs))]
    objective = np.r_[np.zeros(6+nz), 1.]
    rows = []
    for q in (0., .25, .5, 1., 2., 4., 6., 8., 16.):
        bounds = [(q, q)] + [(-256., 256.)]*4 + [(-32., 0.)] + [(0., None)]*(nz+1)
        fit = linprog(objective, A_ub=matrix, b_ub=rhs, bounds=bounds, method='highs',
                      options={'primal_feasibility_tolerance': 1e-9,
                               'dual_feasibility_tolerance': 1e-9})
        row = {'q1_factor': q, 'q1_increment': q*.001, 'success': bool(fit.success),
               'status': int(fit.status), 'message': fit.message}
        if fit.success:
            x = fit.x[:6]
            predicted = core + slopes@x
            ratios = {str(k): float(sum(Fraction.from_float(abs(float(c)))*(int(m)**2-1)
                                       for c, m in zip(predicted, modes) if m >= k)/tails[k])
                      for k in cutoffs}
            row.update(minimum_floating_multiplier=float(fit.x[-1]),
                       normalized_steps=x.tolist(),
                       physical_steps={r['name']:r['step']*v for r, v in zip(proxy['directions'], x)},
                       exact_binary_tail_ratios=ratios,
                       predicted_fine_complete_core=predicted.tolist(),
                       maximum_float_LP_row_violation=float(max(matrix@fit.x-rhs)))
            if max(ratios.values()) > fit.x[-1] + 1e-6:
                raise ArithmeticError('The actual binary core did not replay the tail inequalities')
        rows.append(row)
        print(json.dumps({k:v for k,v in row.items() if k in
                          ('q1_increment','success','minimum_floating_multiplier')}), flush=True)
    out = {'schema': 'fine32-coarse-six-core-tail-only-cost-diagnostic-v1',
           'source_sha256': sha(__file__),
           'inputs': {k:{'path':str(v),'sha256':sha(v)} for k,v in
                      [('proxy',a.proxy),('proxy_resource',a.proxy_resource),('fine',a.fine)]},
           'cutoffs':cutoffs,'physical_control_order':names,'scenarios':rows,
           'geometry_rows_deliberately_absent_from_diagnostic': True,
           'original_complete_geometry_LP_unchanged': True,
           'floating_design_evidence_only': True,'no_new_ODE_or_field': True,
           'no_certified_infeasibility_or_new_BVP': True,
           'elapsed_seconds':time.monotonic()-start,
           'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    a.out.write_text(json.dumps(out,indent=2)+'\n')


if __name__ == '__main__':
    main()
