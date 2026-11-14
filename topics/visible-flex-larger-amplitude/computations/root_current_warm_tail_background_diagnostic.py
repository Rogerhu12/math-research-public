#!/usr/bin/env python3
"""Reuse saved frozen-background heights with a completed current warm screen.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This is a floating background-size diagnostic.  It pays neither the changed-H
nonlinear tail mean nor the remaining cap, continuous errors or closed D.
No factory, ODE, new field, worker or variational solve is started.
"""
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path

BACKGROUND_SHA = '12d50025e0ee39087ab42a7af4e1f54f5ae7662fd32058516386f88689301240'
FIXED_SHA = 'cd2392da6fdc8676a563ef6a18037fe43ea1519288ae39e811d6ac7a55bbcdfa'
ORIGINAL_SHA = '917d859e8a73fa663db1839e354909ae4f174bad1895f8717c20705cdd702aaf'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--plan', type=Path, required=True)
    p.add_argument('--case', required=True)
    p.add_argument('--background', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError(a.out)
    plan, background = read(a.plan), read(a.background)
    if Path.cwd() != Path(plan['cwd']) or sha(a.background) != BACKGROUND_SHA:
        raise ValueError('The current path or original saved background changed')
    rows = [r for r in plan['candidates'] if r['name'] == a.case]
    if len(rows) != 1:
        raise ValueError('Select one actually completed finite warm field')
    row = rows[0]
    screen, owned = read(row['report']), read(row['resource'])
    command = row['command'][row['command'].index('--') + 1:]
    if not (owned['wait4_observed'] and owned['exitcode'] == 0
            and owned['termination_signal'] is None and owned['command'] == command
            and screen['finished'] and screen['finite_domain_passed']
            and screen['worker_start_attempts'] == 0 and not screen['nonlinear_solution']):
        raise ValueError('An uncompleted warm cannot supply the prefix height')
    if not (background['all_checks'] and all(background['checks'].values())
            and background['complete_head_profile_count'] == 1440
            and len(background['rows']) == 1440 and len(background['endpoints']) == 1441):
        raise ValueError('The complete original same-tail background is required')
    config = Path(command[command.index('--tail-config') + 1])
    matches = [(key, value) for key, value in background['input_sha256'].items()
               if Path(key).name == config.name]
    if len(matches) != 1 or matches[0][1] != sha(config):
        raise ValueError('The finite warm must retain this exact frozen-tail configuration')
    reference = Path(screen['actual_reference'])
    fixed = read(reference)
    view = fixed['frozen_design_view']
    if not (sha(reference) == FIXED_SHA
            and ORIGINAL_SHA in view['source_sha256'].values()
            and view['physical_quintics_unchanged'] and view['eight_physical_data_unchanged']
            and view['raw_x_y_cubic_unchanged'] and view['complete_H_bitwise_equal']):
        raise ValueError('Keep the actual accepted-A fixed-view identity bridge')
    geometry = screen['geometry_fields']
    height = float(geometry['height_abs_max_sample'])
    prefix_size = float(geometry['twice_radius_max_sample'])
    curvature = float(geometry['kappa_abs_max_sample'])
    if (not all(math.isfinite(x) and x > 0 for x in (height, prefix_size, curvature))
            or geometry['mean_quadrature']['angular'] != 1552
            or len(geometry['actual_core']) != 32):
        raise ValueError('Require the actual complete-mean current-M32 screen')
    endpoint = max((2 * math.hypot(r['radius'], height + r['background_height_from_cut']), i)
                   for i, r in enumerate(background['endpoints']))
    rectangle = max((2 * math.hypot(r['outer_radius'], height + r['cumulative_height_after']), i)
                    for i, r in enumerate(background['rows']))
    combined_size = max(prefix_size, rectangle[0])
    out = dict(schema='current-warm-plus-saved-frozen-background-size-diagnostic-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)', scope=__doc__,
        source_sha256=sha(__file__), input_sha256={str(path): sha(path) for path in
            (a.plan, a.background, Path(row['report']), Path(row['resource']), config, reference)},
        case=a.case, prefix_height_abs_max_sample=height,
        prefix_size_twice_norm_sample=prefix_size, prefix_raw_cubic_curvature_sample=curvature,
        frozen_background_endpoint_size_sample=endpoint[0], endpoint_argmax=endpoint[1],
        frozen_background_floating_rectangle_size_diagnostic=rectangle[0], rectangle_argmax=rectangle[1],
        maximum_prefix_and_background_size_diagnostic=combined_size,
        prefix_curvature_times_combined_size_diagnostic=curvature * combined_size,
        full_profile_count=1440, complete_mean_angular=1552,
        original_same_tail_configuration_unchanged=True,
        changed_H_nonlinear_tail_mean_not_evaluated=True,
        endpoint_prefix_height_anchor_is_finite_maximum_not_exact_cut_mean=True,
        exact_closed_surface_diameter_reach_or_Hausdorff_certified=False,
        no_new_factory_ODE_Node_Jacobian_or_field=True)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(dict(out=str(a.out), sha256=sha(a.out),
        combined_size_diagnostic=combined_size, curvature_size_diagnostic=curvature * combined_size)), flush=True)


if __name__ == '__main__':
    main()
