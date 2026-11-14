#!/usr/bin/env python3
"""Check the original M15 affine-prefix restart without a BVP or tail solve.

Only the frozen original constructor, coordinate map, saved PPoly and inlet
initialization are evaluated. This is an initial-data check, not a DN, RK,
collocation or geometry audit. No subprocess is started.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'
OLD_STEM = '2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-from-affine'
DEFAULT_OUT = NOTES / '2026-11-09-db6f-prefix-final-m15-restart-check.json'


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def bind(path):
    path = Path(path).resolve()
    return dict(path=str(path), bytes=path.stat().st_size, sha256=sha(path))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def distance_to_grid(a, b):
    j = np.searchsorted(b, a)
    lo = b[np.maximum(0, j-1)]
    hi = b[np.minimum(len(b)-1, j)]
    return float(np.maximum(0, np.minimum(abs(a-lo), abs(a-hi))).max())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    binding_path = NOTES / (OLD_STEM + '-input-bindings.json')
    binding = read(binding_path)
    command = binding['command']
    for item in binding['bound_files']:
        if sha(item['path']) != item['sha256']:
            raise ValueError('Frozen old launch input changed: ' + item['path'])

    def option(name):
        return command[command.index(name)+1]

    expected = {'--amplitude': '.1', '--warp-reference': '.1', '--modes': '15',
                '--angular': '512', '--audit-angular': '1024', '--nodes': '1601',
                '--max-nodes': '4500', '--tol': '2e-9', '--bc-tol': '1e-8',
                '--physical-bc-tol': '2e-11', '--node-heap': '1536'}
    for key, value in expected.items():
        if option(key) != value:
            raise ValueError('Unexpected original option: ' + key)
    for flag in ['--fixed', '--warmup-scales', '--lagged-tail', '--preserve-restart-mesh']:
        if flag not in command:
            raise ValueError('Missing original flag: ' + flag)
    if command[command.index('--warmup-scales')+1] != '--lagged-tail':
        raise ValueError('Original warmup list is not empty')

    wrapper = Path(command[1])
    runner = load('db6f_final_m15_restart_original', wrapper).runner
    source_root = Path(option('--source-root'))
    runner.adaptive.old.install_source(source_root)
    from curve_stable_prefix_bvp import load_checkpoint
    cfg_path = Path(option('--profile'))
    chart_path = Path(option('--chart'))
    port_path = Path(option('--linear-port'))
    cp_path = Path(option('--restart'))
    cfg, chart, port = read(cfg_path), read(chart_path), read(port_path)
    port['_sha256'] = sha(port_path)
    rec = load_checkpoint(cp_path)
    if rec['config'].get('actual_nonlinear_tail') is not False:
        raise ValueError('Restart is not the explicitly UNSOLVED affine predictor')
    _, Base = runner.adaptive.build_classes(chart)

    class BVP(runner.TailMixin, Base):
        pass

    obj = BVP(cfg, port, .1, 15, 512, True, .1)
    obj.restart_remesh = 1601
    obj.bcweights = np.full(obj.M, 2e-11/1e-8)
    helper_path = HERE / 'db6f-prefix-preserve-restart.py'
    helper = load('db6f_final_m15_saved_restart', helper_path)
    x, y, par, info = helper.restart(obj, cp_path, chart)
    physical, derivative = obj.chart(x, par[0])
    old_mesh = np.asarray(rec['mesh'], float)
    flow = obj.flow(par[0])
    height = obj.bridge.sigma * obj.q * y[obj.iz:, -1]
    goal = np.asarray(rec['predicted_cut_height'], float)
    failed_path = NOTES / (OLD_STEM + '_tail_0001.json.gz')
    prior_request = np.asarray(read(failed_path)['request']['height'], float)
    if height.shape != (15,) or not np.all(np.isfinite(height)):
        raise ValueError('Invalid restarted physical height')
    if not np.array_equal(height, prior_request):
        raise ValueError('The original restart no longer reproduces its actual old DN request')
    if not np.all(np.diff(physical) > 0) or not np.all(derivative > 0):
        raise ValueError('Numerical-to-physical coordinate map is not increasing at nodes')
    if physical[0] != 0 or physical[-1] != flow.end:
        raise ValueError('Physical endpoints changed')
    if obj.q != rec['gauge_amplitude'] or obj.warp_q != rec['warp_reference_q']:
        raise ValueError('Frozen coordinate gauge changed')
    if obj.support_amplitude != rec['actual_primary_amplitude']:
        raise ValueError('Saved physical inlet support was not restored')
    delta = height-goal
    max_height_difference = float(abs(delta).max())
    if max_height_difference > 1e-18:
        raise ValueError('Unexpectedly large restart-to-affine physical height change')
    left = obj.initial(par)
    fixed_parameter_count = len(par)
    source_paths = {Path(item['path']).resolve() for item in binding['bound_files']}
    source_paths.update([Path(__file__).resolve(), binding_path, failed_path])
    source_paths.update(HERE / name for name in [
        '950f-prefix-adaptive-chart-bvp-v2.py', '950f-prefix-warped-bvp.py',
        '950f-tail-client-v3.py', 'db6f-prefix-flat-profile.py',
        '950f-prefix-flat-accel-screen.py'])
    for module in tuple(sys.modules.values()):
        filename = getattr(module, '__file__', None)
        if filename is not None:
            path = Path(filename).resolve()
            if path.suffix == '.py' and (path.is_relative_to(TOPIC) or path.is_relative_to(source_root)):
                source_paths.add(path)
    result = dict(
        status='RESTART_INPUTS_CHECKED_PREFIX_AND_TARGET_DN_STILL_UNSOLVED',
        scope=__doc__, solver_launches=0, tail_solver_constructed=False,
        source_prefix_status=rec.get('status'), source_actual_nonlinear_tail=False,
        original_command_binding=str(binding_path), original_command_binding_sha256=sha(binding_path),
        old_nodes=len(old_mesh), restart_nodes=len(x), same_node_count=len(old_mesh) == len(x),
        physical_mesh_bitwise_equal=bool(np.array_equal(old_mesh, physical)),
        physical_mesh_index_max_difference=(float(abs(physical-old_mesh).max())
                                            if len(old_mesh) == len(x) else None),
        old_to_restarted_mesh_max_distance=distance_to_grid(old_mesh, physical),
        restarted_to_old_mesh_max_distance=distance_to_grid(physical, old_mesh),
        numerical_minimum_span=float(np.diff(x).min()),
        physical_minimum_span=float(np.diff(physical).min()),
        physical_meridian_end=float(flow.end), chart_ds_dt_min=float(derivative.min()),
        restored_support_amplitude=float(obj.support_amplitude), gauge_amplitude=float(obj.q),
        warp_reference_q=float(obj.warp_q), bridge_sigma=float(obj.bridge.sigma),
        free_parameter_count=fixed_parameter_count, primary_support_parameter_is_free=True,
        parameters_max_difference=float(abs(par-np.asarray(rec['parameters'])).max()),
        inlet_coefficient_residual_max=float(abs(y[:, 0]-left).max()),
        restart_info=info, restarted_cut_height=height.tolist(),
        stored_affine_cut_height=goal.tolist(),
        restart_cut_height_bitwise_equals_old_actual_request=True,
        restart_cut_height_bitwise_equals_affine_target=bool(np.array_equal(height, goal)),
        restart_cut_height_max_absolute_difference=max_height_difference,
        nonzero_restart_cut_differences=int(np.count_nonzero(delta)),
        boundary_correction_required='Keep the original default linear warm correction, then solve the original true DN at this restarted height. Never overwrite the prefix endpoint or relabel the s=1 response.',
        all_bound_files=[bind(p) for p in sorted(source_paths)])
    raw = (json.dumps(result, indent=2, allow_nan=False)+'\n').encode()
    if len(raw) >= 1_000_000:
        raise ValueError('Unexpected large check report')
    args.out.write_bytes(raw)
    args.out.chmod(0o444)
    print(json.dumps(dict(status=result['status'], nodes=len(x),
        physical_mesh_max_difference=result['physical_mesh_index_max_difference'],
        cut_height_max_difference=max_height_difference,
        original_request_bitwise_reproduced=True, solver_launches=0,
        output=str(args.out), sha256=sha(args.out))))


if __name__ == '__main__':
    main()
