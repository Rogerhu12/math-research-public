#!/usr/bin/env python3
"""Assemble exact same-field complete prefix receipts, allowing different proven enclosures."""
import argparse
import gzip
import hashlib
import io
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np


# Hashes of the exact published source manifests, using compact sorted-key JSON.
SOURCE_MANIFESTS = {
    "production": "7b3e549a381b1e92efbea4cb7c9746c6fecd8848937caf93b588a3a8f2e77cda",
    "hull": "b79c13563317b99f90ed2076c7cb09cba14d9efd474dc6be0c2ed96fcc845189",
    "four": "0f1148695f6a5a449503e278c5ed1487349dccf1db6249f0916516b4caabf7b3",
    "sixteen": "884b3ed5037b612e4e446322761dd070b1d29c362a53568e3c2dcf5a15911325"
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read(path):
    return json.loads(path.read_bytes())


def verify_cover(intervals, left, right):
    cursor = left
    for lo, hi in sorted(intervals):
        require(left <= lo <= cursor and lo < hi <= right, 'Invalid envelope or interior gap')
        cursor = max(cursor, hi)
    require(cursor == right, 'Incomplete interval cover')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('scripts', 'input', 'forward', 'reverse', 'initial', 'four', 'sixteen', 'out'):
        ap.add_argument('--' + name, type=Path, required=True)
    ap.add_argument('--progress', action='store_true', help='Verify available complete receipts and print partial counts without writing a file')
    a = ap.parse_args()
    notes = a.scripts.parent / 'notes'
    raw = a.input / 'm12-prefix-data.npz.gz'
    field = a.input / 'h2-c2-m48-g12-04r1'
    grid = a.input / 'h2-c2-m48-g12-04'
    inputs = {
        'data_sha256': raw, 'field_sha256': field / 'result.json.field.npz',
        'solver_result_sha256': field / 'result.json', 'grid_sha256': grid / 'grid.json',
        'correction_bounds_sha256': field / 'correction-bounds.json',
        'query_report_sha256': grid / 'exact-tail-queries.json',
        'query_cache_sha256': grid / 'exact-tail-queries.json.npz',
        'meta_sha256': notes / '2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json',
        'bridge_sha256': notes / '2026-11-09-db6f-root-exact-bridge-m12.json',
    }
    ids = {name: sha(path) for name, path in inputs.items()}
    require(ids['field_sha256'] == '5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8',
            'Expected original G12/M48 field')
    require(not a.out.exists(), 'Use a new output file')
    config = read(inputs['meta_sha256'])['frozen_profile']
    bridge = read(inputs['bridge_sha256'])
    offset = sum(F(config['delta']) / (F(config[v]) * (1 - F(config['ramp']))) for v in ('vu','vd'))
    s_lo = offset + F(bridge['exact_L']['lo'])
    s_hi = offset + F(bridge['exact_L']['hi'])
    with np.load(io.BytesIO(gzip.decompress(raw.read_bytes())), allow_pickle=False) as data:
        end = F(float(data['mesh'][-1]))
    length = F(.6) - F(.15)
    k_lo, k_hi = [end * (s + length) / s for s in (s_hi, s_lo)]
    with np.load(inputs['field_sha256'], allow_pickle=False) as data:
        z_knots = sorted(set(F(float(x)) for x in data['unit_knots']))
    bounds = [
        (max(F(0), lo * k_lo), min(end, hi * k_hi))
        for lo, hi in zip(z_knots, z_knots[1:]) if lo * k_lo < end
    ]
    require(len(bounds) == 158, 'Unexpected original prefix knot partition')
    verify_cover(bounds, F(0), end)
    target = F(1, 500000000)
    rows = []
    reports = {}
    source_versions = {}

    def inspect(path, index, schema):
        if a.progress and not path.exists():
            return
        if path not in reports:
            reports[path] = read(path)
        d = reports[path]
        for key, expected in ids.items():
            if schema == 'sixteen' and key in ('query_report_sha256', 'query_cache_sha256'):
                continue  # Original W16 has neither common-cut nor tail terms.
            actual_key = 'result_sha256' if schema == 'sixteen' and key == 'solver_result_sha256' else key
            require(d[actual_key] == expected, f'Input identity mismatch: {actual_key}')
        require(d['actual_original_X_plus_C_plus_saved_W'], 'Map identity missing')
        if schema == 'sixteen':
            require(index == 16 and d['actual_W_element'] == 16 and d['complete_selected_W_element']
                    and d['same_original_exact_g'] and d['analytic_common_refinement_complete_on_actual_intersections']
                    and d['complete_interval_jet_remainders_paid'] and d['all_angles_by_original_D3_and_reflection_symmetry'],
                    'Incomplete original W16 receipt')
            envelope = d['outer_native_W_envelope']
            leaves = d['rows']
            segments = [tuple(map(F, leaf['native_interval'])) for leaf in leaves]
            maximum = max(F(leaf['relative_metric_upper_exact']) for leaf in leaves)
            source_versions[schema] = {k:d[k] for k in ('script_sha256','interval_kernel_sha256','central_interval_sha256')}
        else:
            require(d['original_exact_g_retained'] and not d['Q_source_regularization_included']
                    and d['all_angles_by_verified_D3_and_reflection'] and d['below_B']
                    and F(d['requested_B_exact']) == target, 'Metric, angular cover or threshold changed')
            if schema == 'four':
                require(d['all_source_chart_target_C_W_actual_intersections_covered']
                        and d['complete_real_interval_jet_remainders_paid'], 'Four-region receipt incomplete')
                summary = next(r for r in d['elements'] if r['element'] == index)
            else:
                require(d['complete_actual_element_prefix_intersection'] and d['element']['element'] == index,
                        'Element receipt incomplete')
                summary = d['element']
            leaves = [r for r in d['all_intersections'] if r['element'] == index]
            require(len(leaves) == summary['intersection_leaves'], 'Leaf count mismatch')
            envelope = summary['native_outer_envelope']
            segments = [tuple(map(F, leaf['native_outer_interval'])) for leaf in leaves]
            maximum = max(F(leaf['relative_metric_upper']['upper_exact']) for leaf in leaves)
            require(source_versions.setdefault(schema, d['frozen_sources']) == d['frozen_sources'], 'Kernel drift')
        manifest = json.dumps(source_versions[schema], sort_keys=True, separators=(',',':')).encode()
        require(hashlib.sha256(manifest).hexdigest() == SOURCE_MANIFESTS[schema], 'Unexpected source-file version')
        require(tuple(map(F,envelope)) == bounds[index], 'Envelope differs from independently recovered actual W knot')
        verify_cover(segments, *bounds[index])
        require(0 <= maximum <= target, 'Actual leaf certificate misses tolerance')
        rows.append({'element':index, 'leaves':len(leaves), 'upper_exact':str(maximum),
                     'native_outer_envelope':envelope, 'receipt':path.name, 'receipt_sha256':sha(path), 'source':schema})
        if schema != 'four':
            del reports[path]

    for index in range(len(bounds)):
        if index == 16:
            inspect(a.sixteen, index, 'sixteen')
        elif index in (70,125,153,157):
            inspect(a.four, index, 'four')
        else:
            base, kind = (a.initial,'production') if index < 16 else ((a.forward,'hull') if index < 80 else (a.reverse,'hull'))
            inspect(base / f'element-{index:04d}.json', index, kind)
    if a.progress:
        print(json.dumps({'active_partial_diagnostic':True, 'complete_elements':len(rows),
                          'intersection_leaves':sum(r['leaves'] for r in rows),
                          'verified_elements':[r['element'] for r in rows],
                          'maximum_upper_exact':str(max(F(r['upper_exact']) for r in rows))}))
        return
    worst = max(rows, key=lambda row:F(row['upper_exact']))
    out = {'schema':'2ecf-original-M12-composed-complete-prefix-total-Gram-v1', **ids,
           'complete_original_prefix':True,'whole_surface_complete':False,'native_domain':['0',str(end)],
           'common_q_endpoint_interval':list(map(str,(s_lo,s_hi))),
           'common_z_endpoint_interval':list(map(str,(s_lo/(s_lo+length),s_hi/(s_hi+length)))),
           'complete_elements':len(rows),'complete_intersection_leaves':sum(r['leaves'] for r in rows),
           'maximum_relative_metric_upper_exact':worst['upper_exact'],'worst_element':worst['element'],
           'requested_B_exact':str(target),'all_elements_below_B':True,'sources':source_versions,'elements':rows}
    a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('sources','elements')}))


if __name__ == '__main__':
    main()
