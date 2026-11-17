#!/usr/bin/env python3
"""True fixed-metric BVP refinement on all saved nodes and their midpoints.

The original saved-mesh initializer checks physical metric, chart, cut and
gauge before any refinement. This wrapper only enriches its initial mesh
and evaluates the saved represented nonmean field at the new nodes. The
original nonlinear BVP, actual-DN outer iteration, root guards and all
acceptance tests subsequently run unchanged. No midpoint postprocessing is
reported as a new solve.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly

parser = argparse.ArgumentParser(add_help=False, allow_abbrev=False)
parser.add_argument('--source-topic', type=Path, required=True)
parser.add_argument('--short-bridge', type=Path, required=True)
parser.add_argument('--restart-bisections', type=int, default=1)
args, rest = parser.parse_known_args()
if args.restart_bisections < 1:
    raise ValueError('At least one initial-mesh bisection is required')
if '--fixed' not in rest:
    raise ValueError('Radial refinement requires the fixed physical metric')
if '--preserve-restart-mesh' not in rest:
    rest.append('--preserve-restart-mesh')
source = args.source_topic.resolve()
sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

coupler_path = source/'scripts/db6f-prefix-coupled.py'
flat_path = source/'scripts/db6f-prefix-flat-profile.py'
preserve_path = source/'scripts/db6f-prefix-preserve-restart.py'
coupler = module('radial_refine_original_m3_coupler', coupler_path)
flat = module('radial_refine_original_flat', flat_path)
flat.install(coupler.adaptive)
bridge = module('radial_refine_original_short_bridge', args.short_bridge.resolve())
original_install = coupler.adaptive.old.install_source

def install(root):
    original_install(root)
    bridge.install()

coupler.adaptive.old.install_source = install
original_module = coupler.module

def load_with_refined_initializer(name, path):
    loaded = original_module(name, path)
    if name != 'db6f_preserve_restart':
        return loaded
    original_restart = loaded.restart

    def restart(obj, checkpoint, chart, merge_tolerance=2e-13):
        from curve_stable_prefix_bvp import load_checkpoint
        x0, _, parameters, info = original_restart(obj, checkpoint, chart, merge_tolerance)
        x = x0.copy()
        for _ in range(args.restart_bisections):
            x = np.sort(np.r_[x, (x[:-1]+x[1:])/2])
        if not np.all(np.diff(x) > 0):
            raise ValueError('Bisection produced coincident numerical nodes')
        if not np.all(np.isin(x0, x)):
            raise AssertionError('An original mesh anchor was lost')
        record = load_checkpoint(checkpoint)
        old_modes = record['config']['modes']
        physical, _ = obj.chart(x, parameters[0])
        old_pp = PPoly.construct_fast(np.asarray(record['pp_coefficients']),
                                     np.asarray(record['mesh'], float),
                                     extrapolate=True, axis=1)
        old_values = old_pp(physical)
        y = np.zeros((obj.n, len(x)))
        ratio = record['gauge_amplitude']/obj.q
        y[0] = ratio*old_values[0]
        y[1:old_modes+1] = ratio*old_values[1:old_modes+1]
        y[obj.M+1:obj.M+old_modes+1] = ratio*old_values[old_modes+1:2*old_modes+1]
        y[2*obj.M+1:2*obj.M+old_modes+1] = ratio*old_values[2*old_modes+1:3*old_modes+1]
        correction = obj.initial(parameters)-y[:, 0]
        flow = obj.flow(parameters[0])
        cutoff = (flow.Tu if flow.direction == 'outward' else flow.Td)/2
        if not cutoff > 0:
            raise ValueError('Invalid inlet correction interval')
        y += correction[:, None]*np.maximum(0, 1-physical/cutoff)[None, :]**3
        info.update(method='original-checked-saved-mesh-plus-all-midpoints-true-BVP',
                    original_checked_nodes=len(x0), new_nodes=len(x),
                    restart_bisections=args.restart_bisections,
                    all_original_anchors_retained=True,
                    minimum_numerical_span=float(np.diff(x).min()),
                    maximum_numerical_span=float(np.diff(x).max()),
                    initializer_wrapper_sha256=sha(__file__),
                    original_initializer_sha256=sha(preserve_path),
                    scope=__doc__)
        print(json.dumps(dict(event='radial_initial_mesh', **info)), flush=True)
        return x, y, parameters, info

    loaded.restart = restart
    return loaded

coupler.module = load_with_refined_initializer
sys.argv = [sys.argv[0], '--source-root', str(source/'repro/source-root')]+rest
out = Path(rest[rest.index('--out-prefix')+1])
out.parent.mkdir(parents=True, exist_ok=True)
record = dict(scope=__doc__, command=sys.argv, restart_bisections=args.restart_bisections,
              source_topic=str(source), source_hashes={str(path):sha(path) for path in
                  [Path(__file__), coupler_path, flat_path, preserve_path, args.short_bridge]})
record_path = out.with_name(out.name+'-wrapper-record.json')
record_path.write_text(json.dumps(record, indent=2)+'\n')
started = time.monotonic()
try:
    coupler.main()
    record['returned'] = True
finally:
    record['seconds'] = time.monotonic()-started
    record_path.write_text(json.dumps(record, indent=2)+'\n')
