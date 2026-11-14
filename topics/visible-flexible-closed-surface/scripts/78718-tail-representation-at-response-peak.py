#!/usr/bin/env python3
"""Floating same-point source versus explicit-XYZ metric comparison.

The finite map is the existing IntegratedTail definition evaluated by its
long-double reader.  Its exporter must have consumed exactly the response
packet diagnosed by 78718-tail-response-diagnostic.mjs.  The common-angle
normalized Gram difference is invariant under ambient rotations, so no
positional gauge matching is assumed.  This is one radius, not a continuous
certificate or an estimate of all interpolation errors on the tail.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import time

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('tail_peak_representation', HERE/'db6f_tail_integrated.py')
reader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reader)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def op(a):
    return (np.abs(a[:, 0]+a[:, 2])+np.sqrt((a[:, 0]-a[:, 2])**2+4*a[:, 1]**2))/2


def run(args):
    started = time.monotonic()
    if args.out.exists():
        raise ValueError('fresh output path required')
    report = json.loads(args.diagnostic.read_text())
    peak_path = Path(report['peakMetricData']['path'])
    if sha(peak_path) != report['peakMetricData']['sha256']:
        raise ValueError('peak data hash mismatch')
    peak = json.loads(gzip.decompress(peak_path.read_bytes()))
    meta = json.loads(args.manifest.read_text())
    if meta['inputSHA256'] != report['packet']['sha256'] or peak['packet_sha256'] != report['packet']['sha256']:
        raise ValueError('manifest and diagnostic do not originate in the same response packet')
    tail = reader.IntegratedTail(args.manifest)
    count = int(peak['angularNodes'])
    theta = np.arange(count, dtype=np.longdouble)*(2*np.arccos(np.longdouble(-1))/count)
    g = peak['geometry']
    r, w, E = (np.longdouble(g[k]) for k in ('r', 'w', 'E'))
    _, vr, vt, _, _, _ = tail.perturbation_jets(r, theta)
    fr = vr+np.stack([np.cos(theta), np.sin(theta), np.full(count, w)], axis=-1)
    ft = vt+np.stack([-r*np.sin(theta), r*np.cos(theta), np.zeros(count)], axis=-1)
    actual = np.stack([np.sum(fr*fr, axis=-1)/E-1,
                       np.sum(fr*ft, axis=-1)/(r*np.sqrt(E)),
                       np.sum(ft*ft, axis=-1)/(r*r)-1], axis=-1)
    source = np.asarray(peak['source_metric'], dtype=np.longdouble)
    if source.shape != actual.shape:
        raise ValueError('common-angle metric shapes differ')
    native_count = int(peak['nativeAngularNodes'])
    if count % native_count:
        raise ValueError('source angle grids are not nested')
    stride = count//native_count
    native_source = np.asarray(peak['source_metric_native'], dtype=np.longdouble)
    native_actual = actual[::stride]
    if native_source.shape != native_actual.shape:
        raise ValueError('native source metric shape differs')
    native_delta = native_actual-native_source
    angular_change = source[::stride]-native_source
    delta = actual-source
    actual_op, source_op, difference_op = op(actual), op(source), op(delta)
    worst = int(np.argmax(difference_op))
    output = dict(status='floating-common-point-XYZ-versus-source-metric', scope=__doc__,
                  script_sha256=sha(__file__), reader_sha256=sha(HERE/'db6f_tail_integrated.py'),
                  manifest=str(args.manifest), manifest_sha256=sha(args.manifest),
                  diagnostic=str(args.diagnostic), diagnostic_sha256=sha(args.diagnostic),
                  packet_sha256=report['packet']['sha256'], peak_data_sha256=sha(peak_path),
                  radius=float(r), source_stage=peak['stage'], source_x=peak['x'], angular_nodes=count,
                  source_operator_sample_max=float(np.max(source_op)),
                  finite_operator_sample_max=float(np.max(actual_op)),
                  metric_difference_operator_sample_max=float(np.max(difference_op)),
                  native_angular_nodes=native_count,
                  source_native_operator_sample_max=float(np.max(op(native_source))),
                  finite_at_native_operator_sample_max=float(np.max(op(native_actual))),
                  native_metric_difference_operator_sample_max=float(np.max(op(native_delta))),
                  source_angular_refinement_common_angle_change_max=float(np.max(op(angular_change))),
                  rr_difference_sample_max=float(np.max(np.abs(delta[:, 0]))),
                  rt_difference_sample_max=float(np.max(np.abs(delta[:, 1]))),
                  tt_difference_sample_max=float(np.max(np.abs(delta[:, 2]))),
                  worst_difference_angle_index=worst,
                  worst_difference_theta=float(theta[worst]),
                  exporter_source_metric_sample_max=meta['totals'].get('sourceMetric'),
                  exporter_finite_metric_sample_max=meta['totals'].get('metric'),
                  exporter_position_deviation_sample_max=meta['totals'].get('maxIntegratedPositionDeviation'),
                  actual_ode_calls=0, actual_dn_calls=0,
                  continuous_bound=False, whole_tail_covered=False,
                  seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
    print(json.dumps({k: output[k] for k in ('radius', 'angular_nodes', 'source_operator_sample_max',
                                           'finite_operator_sample_max', 'metric_difference_operator_sample_max',
                                           'seconds')}, separators=(',', ':')))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('manifest', 'diagnostic', 'out'):
        ap.add_argument('--'+name, type=Path, required=True)
    run(ap.parse_args())
