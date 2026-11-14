#!/usr/bin/env python3
"""Locate saved warm curvature peaks and actual meridian-chart length changes.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only complete saved field chunks and the two actual physical knot vectors are
read. This computes numerical diagnostics, not a new geometry field, ODE,
Jacobian or a nonlinear-impossibility certificate.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np
from root_neck_chart import NeckChart


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def jets(chart, t):
    value, first = chart.evaluate(np.array([t]))
    j = int(np.clip(np.searchsorted(chart.t, t, side='right')-1, 0, len(chart.h)-1))
    u = (t-chart.t[j])/chart.h[j]
    r, v, w = chart.r[j], chart.v[j], chart.v[j+1]
    c3, c4, c5 = 10*r-6*v-4*w, -15*r+8*v+7*w, 6*r-3*v-3*w
    second = (6*c3*u+12*c4*u*u+20*c5*u**3)/chart.h[j]
    return dict(segment=j, numerical_t=float(t), physical_s=float(value[0]),
                first=float(first[0]), second=float(second))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('report','baseline','chart-proof','out'):
        p.add_argument('--'+key, type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Fresh saved-field diagnostic required')
    report, baseline, proof = map(read, (a.report, a.baseline, a.chart_proof))
    if (not report['finite_domain_passed'] or report['nonlinear_solution']
            or not baseline['solver_success'] or baseline['audit_pending']
            or sha(a.baseline) != report['explicit_coarse_increment_warm']['current_reference_sha256']):
        raise ValueError('Actual unsolved complete field and accepted fine baseline required')
    field_path = Path(report['geometry_fields']['file'])
    grid_path = Path(report['geometry_fields']['grid_file'])
    if sha(field_path) != report['geometry_fields']['sha256']:
        raise ValueError('Complete field manifest identity differs')
    field, grid = read(field_path), read(grid_path)
    if not field['complete'] or field['shape'] != [3764,768,3]:
        raise ValueError('The original complete common grid is required')
    knots = np.asarray(proof['original_numerical_knots'])
    old_knots = np.asarray(baseline['numerical_meridian_chart']['reference_t'])
    if knots.tobytes() != old_knots.tobytes():
        raise ValueError('The actual material meridian knots differ')
    old = NeckChart(knots, baseline['numerical_meridian_chart']['physical_s'])
    new = NeckChart(knots, proof['actual_physical_breaks'])
    lengths_old, lengths_new = np.diff(old.s), np.diff(new.s)
    rows = [dict(segment=i, numerical_interval=knots[i:i+2].tolist(),
        original_physical_interval=old.s[i:i+2].tolist(),
        warm_physical_interval=new.s[i:i+2].tolist(),
        original_length=float(lengths_old[i]), warm_length=float(lengths_new[i]),
        warm_length_over_original=float(lengths_new[i]/lengths_old[i]),
        old_secant=float(old.r[i]), warm_secant=float(new.r[i]),
        old_endpoint_slopes=old.v[i:i+2].tolist(), warm_endpoint_slopes=new.v[i:i+2].tolist())
        for i in range(len(lengths_old))]
    peaks = []
    cursor = 0
    for chunk in field['chunks']:
        path = field_path.with_name(chunk['file'])
        if sha(path) != chunk['sha256'] or chunk['start'] != cursor:
            raise ValueError('A complete saved chunk changed or coverage has a gap')
        with gzip.open(path, 'rb') as stream:
            values = np.load(stream, allow_pickle=False)
        if values.shape != (chunk['end']-cursor,768,3) or not np.isfinite(values).all():
            raise ValueError('Complete finite field values required')
        magnitudes = np.max(abs(values[:,:,:2]), axis=(1,2))
        for local in np.argsort(magnitudes)[-12:]:
            local = int(local)
            angle, component = map(int, np.unravel_index(abs(values[local,:,:2]).argmax(), (768,2)))
            radial = cursor+local
            t = float(grid['numerical_t'][radial])
            old_jets, new_jets = jets(old,t), jets(new,t)
            peaks.append(dict(radial_index=radial, angular_index=angle,
                material_eta=float(angle*2*np.pi/768), principal_component=component,
                signed_curvature=float(values[local,angle,component]),
                absolute_curvature=float(magnitudes[local]),
                twice_radius_at_same_point=float(values[local,angle,2]),
                original_chart=old_jets, warm_chart=new_jets,
                old_over_warm_chart_first=float(old_jets['first']/new_jets['first'])))
        cursor = chunk['end']
    if cursor != 3764:
        raise ValueError('The complete original radial grid was not read')
    peaks.sort(key=lambda z:z['absolute_curvature'], reverse=True)
    peaks = peaks[:20]
    if peaks[0]['absolute_curvature'] != report['geometry_fields']['kappa_abs_max_sample']:
        raise ValueError('Saved peak does not reproduce the completed full-field summary')
    out = dict(schema='saved-fine-warm-chart-length-and-curvature-diagnostic-v1',
        scope=__doc__, source_sha256=sha(__file__),
        input_sha256={str(q):sha(q) for q in (a.report,a.baseline,a.chart_proof,field_path,grid_path)},
        chart_source_sha256=sha(Path(__file__).with_name('root_neck_chart.py')),
        all_complete_chunks_read=len(field['chunks']), original_raw_nodes=baseline['nodes'],
        complete_grid_shape=field['shape'], all22_segment_rows=rows,
        minimum_length_ratio=float(np.min(lengths_new/lengths_old)),
        maximum_length_ratio=float(np.max(lengths_new/lengths_old)),
        original_chart_common_slope_scale=float(old.slope_scale),
        warm_chart_common_slope_scale=float(new.slope_scale),
        original_minimum_Bernstein_control=float(old.bernstein_min),
        warm_minimum_Bernstein_control=float(new.bernstein_min),
        largest_saved_radial_peaks=peaks,
        full_geometry_evaluations=0, ODE_Node_Jacobian_calls=0,
        nonlinear_causation_or_nonexistence_proved=False)
    a.out.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(dict(event='actual_saved_fine_warm_chart_extrema_finished',
        path=str(a.out), sha256=sha(a.out), minimum_length_ratio=out['minimum_length_ratio'],
        maximum=peaks[0])), flush=True)


if __name__ == '__main__':
    main()
