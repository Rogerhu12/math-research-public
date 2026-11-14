#!/usr/bin/env python3
"""Prepare a fresh current-A warm with an actually verified chart-order bridge.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The original failed command, all physical controls, common samples and original
raw-node domain gates remain recorded. Only the explicitly identified finite
geometry entry and output paths change. This preparation computes no field.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PINS = {
    'root_actual_geometry_field_anchor.py':
        'da6726c130503113a9483da2365cea70e59f22f26e09eb19b08ba57632229a77',
    'root_actual_current_geometry_exact_chart_order.py':
        '2a5ddc83127566cdf88d3709ec328235379b5083b6c069d51927b3defc0eb1a2',
    'root_actual_warm_chart_orientation_probe.py':
        'cd9aedc0edc0b3d13dcc4bd4724c386b0f5ddb847fa0317f9e4b16c559e88868',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def physical_command(command):
    """Keep every original option except the three pure output destinations."""
    result = command[:1] + command[2:]
    for flag in ('--out-prefix', '--inspect-warm-output', '--geometry-array'):
        at = result.index(flag)
        del result[at:at+2]
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--plan', type=Path, required=True)
    ap.add_argument('--case', default='combined')
    ap.add_argument('--probe', type=Path, required=True)
    ap.add_argument('--probe-resource', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    args = ap.parse_args()
    for name, wanted in PINS.items():
        if sha(HERE/name) != wanted:
            raise ValueError('A frozen chart entry changed: '+name)
    plan, probe, probe_owned = read(args.plan), read(args.probe), read(args.probe_resource)
    if Path.cwd() != Path(plan['cwd']):
        raise ValueError('Retain the actual plan cwd')
    for name, wanted in plan['source_and_input_sha256'].items():
        if sha(name) != wanted:
            raise ValueError('A prepared current input changed: '+name)
    choices = [r for r in plan['candidates'] if r['name'] == args.case]
    if len(choices) != 1:
        raise ValueError('Select exactly one existing current candidate')
    row = copy.deepcopy(choices[0])
    command = row['command']
    original_child = command[command.index('--')+1:]
    failed, failed_owned = read(row['report']), read(row['resource'])
    if not (failed_owned['exitcode'] == 1 and failed_owned['wait4_observed']
            and failed_owned['termination_signal'] is None
            and failed_owned['command'] == original_child
            and failed['inspection_error'] == "ValueError('The physical chart lost orientation')"
            and not failed['finite_domain_passed']
            and Path(original_child[1]) == HERE/'root_actual_geometry_field_anchor.py'):
        raise ValueError('Retain the actual original native float-order rejection')
    if not (probe_owned['exitcode'] == 0 and probe_owned['wait4_observed']
            and probe_owned['termination_signal'] is None
            and Path(probe_owned['command'][1]) == HERE/'root_actual_warm_chart_orientation_probe.py'
            and physical_command(original_child) == physical_command(probe_owned['command'])
            and probe['physical_profile'] == failed['warm_profile']
            and probe['raw_strict_increase']
            and probe['all_exact_binary_polynomial_piece_derivatives_positive']
            and probe['all_actual_raw_nodes_retained']
            and probe['raw_nodes'] == 2590 and probe['common_grid_nodes'] == 3767
            and probe['grid_nonpositive_spacings']
            and all(r['displayed_ds'] == 0 and r['same_piece_strict_positive_exact_ds']
                    for r in probe['grid_nonpositive_spacings'])):
        raise ValueError('The same physical candidate lacks its actual exact chart probe')
    prefix = str(args.out_prefix)
    out = Path(prefix+'-plan.json')
    if list(args.out_prefix.parent.glob(args.out_prefix.name+'*')):
        raise FileExistsError('Use a completely fresh exact-chart output prefix')
    old_paths = [args.plan, Path(row['report']), Path(row['resource']),
                 args.probe, args.probe_resource, Path(__file__)]
    old_paths.extend(HERE/name for name in PINS)
    for flag, value in (
            ('--out', prefix+'-resource.json'), ('--heartbeat', prefix+'-heartbeat.json'),
            ('--ownership', prefix+'-ownership.json'),
            ('--task-prefix', 'current-A-combined-exact-chart-'+args.out_prefix.name),
            ('--out-prefix', prefix), ('--inspect-warm-output', prefix+'-screen.json'),
            ('--geometry-array', prefix+'-field.json')):
        command[command.index(flag)+1] = value
    command[command.index('--')+2] = str(HERE/'root_actual_current_geometry_exact_chart_order.py')
    row.update(report=prefix+'-screen.json', resource=prefix+'-resource.json',
               field=prefix+'-field.json', log=prefix+'-log.txt',
               exact_chart_order_entry=True)
    plan['candidates'] = [row]
    plan['source_and_input_sha256'].update({str(p): sha(p) for p in old_paths})
    plan['actual_current_combined_exact_chart_plan'] = dict(
        source_sha256=sha(__file__), original_plan=str(args.plan),
        original_plan_sha256=sha(args.plan), original_failed_case=choices[0],
        actual_probe=str(args.probe), actual_probe_sha256=sha(args.probe),
        exact_geometry_entry_sha256=PINS['root_actual_current_geometry_exact_chart_order.py'],
        complete_physical_command_preserved=True, samples_and_mean_unchanged=True,
        actual_raw_float_strict_gate_preserved=True,
        exact_all_adjacent_sample_order_to_be_verified_by_producer=True,
        no_new_solution_or_continuous_geometry_claimed=True)
    out.write_text(json.dumps(plan, indent=2)+'\n')
    print(json.dumps(dict(plan=str(out), sha256=sha(out),
        same_physical_candidate=True, actual_displayed_ties=len(probe['grid_nonpositive_spacings']))),
        flush=True)


if __name__ == '__main__':
    main()
