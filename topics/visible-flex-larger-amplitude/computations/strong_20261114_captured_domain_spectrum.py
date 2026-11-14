#!/usr/bin/env python3
"""Diagnose original rejected trial inputs with the complete physical curve.

The original Flow and all retained modes are used to reproduce q_lat and the
Frenet radicand algebraically, without taking its rejected square root. Angular
low passes are explicitly diagnostic: they are not alternative numerical
states, solutions, inlet curves, or domain/acceptance tests. No BVP Jacobian,
tail worker, nonlinear solve or height integral is run.

Author: strong_amplitude (GPT-6 Astra Pro; AI-assisted), 2026-11-14.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import time
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--captured-domain', type=Path, action='append', required=True)
    parser.add_argument('--captured-out', type=Path, required=True)
    own, remaining = parser.parse_known_args()
    import strong_actual_warm_screen as warm
    import strong_20261114_loop_actual_bvp as entry
    original, old_argv = warm.inspect_warm, sys.argv
    done = False

    def inspect(obj, x, y, p, baseline_H, **unused):
        nonlocal done
        started = time.monotonic()
        rows = []
        for path in own.captured_domain:
            with np.load(path, allow_pickle=False) as packed:
                meta = json.loads(packed['metadata'].tobytes())
                s, Y, P = (packed[name].copy() for name in ('s', 'y', 'p'))
            for name, array in (('s', s), ('y', Y), ('p', P)):
                recorded = meta['arrays'][name]
                if (list(array.shape) != recorded['shape']
                        or array.dtype.str != recorded['dtype']
                        or hashlib.sha256(array.tobytes(order='C')).hexdigest() != recorded['C_order_bytes_sha256']):
                    raise ValueError('The actual captured callback array differs: ' + name)
            identity = meta['identity']
            if (obj.M != identity['M'] or obj.nt != identity['nt']
                    or obj.q != identity['q'] or obj.cfg != identity['cfg']
                    or obj.ref_coeff.tolist() != identity['ref_coeff']
                    or obj.ref_frequencies != identity['ref_frequencies']):
                raise ValueError('The original captured Flow identity differs')
            obj.select(P)
            flow = obj.flow()
            if flow.cfg != identity['actually_constructed_Flow_cfg']:
                raise ValueError('The exact captured physical profile was not reconstructed')
            N = flow.nt
            geo = flow.geo(s, N)
            a, ap, app = flow.profile(s)
            d = flow.values(obj.q*Y, flow.B1) + geo['p1']
            dd = flow.values(obj.q*Y, flow.B2) + geo['p2']

            def measure(first, second):
                speed = np.linalg.norm(first, axis=2)
                tangent = first/speed[:, :, None]
                normal = second - np.sum(second*tangent, axis=2)[:, :, None]*tangent
                qlat = a[:, None]*np.linalg.norm(normal, axis=2)/(speed*speed)
                margin = 1 - (ap[:, None]/qlat)**2
                gap = qlat - abs(ap)[:, None]
                i, j = np.unravel_index(np.argmin(margin), margin.shape)
                return dict(min_radicand=float(margin[i, j]), min_gap=float(gap.min()),
                    physical_s=float(s[i]), angle_index=int(j),
                    psi=float(2*np.pi*j/N), a=float(a[i]), ap=float(ap[i]),
                    q_lat=float(qlat[i, j]), minimum_angular_speed=float(speed.min()))

            full = measure(d, dd)
            text = meta['exception_repr']
            match = re.search(r'Adaptive Frenet domain failure: ([^\)\x27]+)', text)
            captured_margin = float(match.group(1)) if match else None
            if captured_margin is not None:
                full['captured_exception_radicand'] = captured_margin
                full['reproduction_absolute_difference'] = abs(full['min_radicand'] - captured_margin)
                if full['reproduction_absolute_difference'] > 2e-10:
                    raise ValueError('The original rejected radicand was not reproduced')
            spectrum_d = np.fft.fft(d, axis=1)
            spectrum_dd = np.fft.fft(dd, axis=1)
            frequencies = np.rint(np.fft.fftfreq(N)*N).astype(int)
            filtered = []
            for cutoff in (4, 8, 16, 24, 32, 48, 64, 65, 96, 128):
                mask = (abs(frequencies) <= cutoff)[None, :, None]
                first = np.fft.ifft(spectrum_d*mask, axis=1).real
                second = np.fft.ifft(spectrum_dd*mask, axis=1).real
                filtered.append(dict(material_psi_harmonic_cutoff=cutoff,
                    diagnostic_only=True, **measure(first, second)))
            rows.append(dict(file=str(path), sha256=sha(path),
                original_callback_index=meta['index'],
                original_exception=text, modes=obj.M, angular=N,
                actual_parameter_vector=P.tolist(),
                actual_physical_profile=dict(flow.cfg),
                original_full_curve=full, filtered_diagnostics=filtered,
                radial_points=len(s), physical_s_range=[float(s.min()), float(s.max())],
                source_hashes_at_capture=meta['source_sha256_at_start']))
            print(json.dumps(dict(event='captured_domain_spectrum',
                callback=meta['index'], original_margin=full['min_radicand'],
                reproduction_difference=full.get('reproduction_absolute_difference'))), flush=True)
        report = dict(scope=__doc__, source_sha256=sha(__file__),
            diagnostic_finished=True, finite_domain_passed=False,
            original_complete_rejected_states_reproduced=True,
            angular_filter_used_only_in_diagnostics=True,
            numerical_solver_and_mathematical_gates_changed=False,
            new_nonlinear_solution=False, full_RMS_and_fullmean_geometry_not_evaluated=True,
            tail_worker_started=False, rows=rows, seconds=time.monotonic()-started)
        own.captured_out.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')
        done = True
        return report

    warm.inspect_warm = inspect
    sys.argv = [old_argv[0], *remaining]
    try:
        entry.main()
    finally:
        warm.inspect_warm, sys.argv = original, old_argv
    if not done:
        raise RuntimeError('Actual captured-state diagnostic did not finish')


if __name__ == '__main__':
    main()
