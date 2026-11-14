#!/usr/bin/env python3
"""Read every saved baseline chunk and retain its original witness identity.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
No geometry, Fourier response, BVP or tail is recomputed. All budgets here
are finite diagnostics and do not prove continuous curvature or amplitude.
"""
import os
for _k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import argparse
from fractions import Fraction
import gzip
import hashlib
import io
import json
from pathlib import Path
import resource
import time
import numpy as np


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p)
    b = p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix == '.gz' else b)


def rat(z):
    return Fraction(int(z['numerator']), int(z['denominator']))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for k in ('plan', 'witness-bridge', 'interior-audit', 'core-budget', 'out'):
        p.add_argument('--'+k, type=Path, required=True)
    a = p.parse_args()
    start = time.monotonic()
    if a.out.exists():
        raise FileExistsError('Fresh saved-state check required')
    plan, bridge, audit, core = map(read, (a.plan, a.witness_bridge,
                                         a.interior_audit, a.core_budget))
    gates = []
    def check(name, yes):
        if not yes:
            raise ArithmeticError(name)
        gates.append(name)
    check('one_actual_baseline_plan', plan['baseline_only'] and
          len(plan['candidates']) == 1 and plan['candidates'][0]['name'] == 'baseline')
    for path, wanted in plan['source_and_input_sha256'].items():
        check('frozen_plan_input:'+path, sha(path) == wanted)
    candidate = plan['candidates'][0]
    screen, used, grid, formal = map(read, (candidate['report'], candidate['field'],
                                          plan['grid'], candidate['resource']))
    g = screen['geometry_fields']
    check('observed_formal_zero', formal['exitcode'] == 0 and
          formal['termination_signal'] is None)
    check('no_new_numerical_solution', screen['finished'] and
          screen['nonlinear_solution'] is False and
          screen['true_new_H_tail_evaluated'] is False and screen['worker_start_attempts'] == 0)
    fixed = read(screen['actual_reference'])
    check('exact_baseline_all_core_and_profile',
          screen['actual_core'] == fixed['core']['coefficients'] and
          screen['warm_profile'] == fixed['frozen_profile'] and
          candidate['expected_profile'] == fixed['frozen_profile'])
    check('physical_identity_of_original_quintic_witness',
          bridge['all_checks_passed'] and
          bridge['all_physical_polynomials_metric_core_and_charts_identical'] and
          bridge['fixed_primary_sha256'] == sha(screen['actual_reference']) and
          bridge['original_audit_sha256'] == sha(a.interior_audit) and
          bridge['original_audit_input_sha256'] == audit['input_sha256'] and
          bridge['initial_laws_source_bridge']['all_checks_passed'])
    check('core_budget_same_actual_primary',
          core['current']['sha256'] == audit['input_sha256'] and
          core['retained_modes'] == fixed['modes'])
    command = candidate['command']
    tail_path = command[command.index('--actual-reference-tail')+1]
    tail = read(tail_path)
    H = np.asarray(screen['complete_warm_H'], dtype=np.float64)
    check('complete_current_H_unchanged_in_bits',
          screen['complete_H_change_max'] == 0 and
          H.tobytes() == np.asarray(tail['request']['height'], dtype=np.float64).tobytes())
    check('complete_actual_mean_and_common_grid',
          g['mean_quadrature']['angular'] == max(512, 16*(3*fixed['modes']+1)) == 1360 and
          g['mean_quadrature']['order'] == 6 and
          g['mean_quadrature']['mean_height_first_second_same_angular_rule'] and
          grid['angular'] == 768 and grid['original_raw_nodes'] == fixed['nodes'] and
          grid['all_original_raw_nodes_evaluated'] and
          sha(plan['grid']) == g['grid_sha256'])
    check('complete_chunk_manifest_identity', used == g['storage'] and
          used['complete'] and used['schema'] == 'complete-geometry-chunks-v1' and
          sha(candidate['field']) == g['sha256'])
    maxima = np.zeros(3)
    previous = 0
    point_count = 0
    checked_witnesses = []
    field_path = Path(candidate['field'])
    for part in used['chunks']:
        path = field_path.parent/part['file']
        check('chunk_integrity:'+part['file'], Path(part['file']).name == part['file'] and
              part['start'] == previous and part['end'] > previous and
              path.stat().st_size == part['bytes'] and sha(path) == part['sha256'])
        array = np.load(io.BytesIO(gzip.decompress(path.read_bytes())), allow_pickle=False)
        check('complete_chunk_shape:'+part['file'], array.dtype == np.float64 and
              array.shape == (part['end']-part['start'], 768, 3) and np.isfinite(array).all())
        maxima = np.maximum(maxima, np.max(np.abs(array), axis=(0,1)))
        for witness in g['known_reference_witness_samples']:
            j = witness['radial_index']
            if part['start'] <= j < part['end']:
                val = array[j-part['start'], witness['angular_index'], :]
                check('saved_witness_bits:'+str(j),
                      val.tobytes() == np.asarray(witness['components'], dtype=np.float64).tobytes())
                checked_witnesses.append(witness)
        point_count += array.shape[0]*array.shape[1]
        previous = part['end']
    check('complete_coverage_and_saved_extrema', previous == used['shape'][0] == len(grid['numerical_t']) and
          max(maxima[:2]) == g['kappa_abs_max_sample'] and maxima[2] == g['twice_radius_max_sample'] and
          len(checked_witnesses) == len(g['known_reference_witness_samples']) == 3)
    exact_gap = rat(core['gap_linear_coefficients'][0])
    kappa_quintic = audit['top']['kappa']['value']
    S = g['twice_radius_max_sample']
    kappa_budget = max(kappa_quintic, g['kappa_abs_max_sample'])
    report = dict(schema='actual-baseline-complete-saved-geometry-check-v1', scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)', all_gates=True,
        gate_count=len(gates), gates=gates, source_sha256=sha(__file__),
        input_sha256={str(p): sha(p) for p in (a.plan, a.witness_bridge, a.interior_audit,
            a.core_budget, Path(candidate['report']), field_path, Path(candidate['resource']))},
        original_audit_input_sha256=audit['input_sha256'], fixed_primary_sha256=sha(screen['actual_reference']),
        radial=used['shape'][0], angular=768, complete_mean=1360,
        raw_nodes=fixed['nodes'], finite_spatial_points=point_count,
        checked_chunks=len(used['chunks']), all_saved_field_bits_verified=True,
        raw_cubic_curvature_sample=g['kappa_abs_max_sample'],
        original_physical_quintic_curvature_sample=kappa_quintic,
        comparison_size_sample=S, comparison_size_semantics=g['twice_radius_semantics'],
        conservative_available_sample_kappa_times_size=kappa_budget*S,
        sample_margin_to_100_over_3=100/3-kappa_budget*S,
        exact_complete_core_gap={'numerator':str(exact_gap.numerator),'denominator':str(exact_gap.denominator)},
        complete_core_gap_divided_by_sample_size=float(exact_gap)/S,
        original_quintic_metric_fourier_l1_sample=audit['top']['metric_fourier_l1']['value'],
        original_quintic_flow_defect_sample=audit['top']['flow_defect']['value'],
        complete_H_unchanged_in_bits=True, field_chunks_only_in_scratch=True,
        original_metric_error_gap_remains=True, closed_surface_or_reach_or_amplitude_certified=False,
        elapsed_seconds=time.monotonic()-start, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'all_gates':True,'gates':len(gates),'path':str(a.out),'sha256':sha(a.out),
                      'S':S,'kappaS':kappa_budget*S,'gap_over_S':float(exact_gap)/S}),flush=True)


if __name__ == '__main__':
    main()
