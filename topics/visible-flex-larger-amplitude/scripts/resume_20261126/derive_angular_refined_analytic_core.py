#!/usr/bin/env python3
"""Complete source-only construction of the analytic-J3 N4096 core.

No numerical module is imported or executed.  The original N2048 reference,
fixed scalar/chart/seed, radial mesh and all 32 normal stages are retained.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PINS = {
    'analytic_normal_stage_jacobian.py': '64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d',
    'analytic_j3_normal_frame_c1_reuse.py': '8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8',
    'analytic_j3_detached_normal_stage_matrix_reuse.py': '5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1',
    'analytic_j3_adjacent_normal_frame_matrices.py': '8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787',
    'reference_centred_analytic_j3_smooth_triangle_calibration.py': '4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d',
    'so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py': '04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e',
    'immutable_analytic_normal_root_packets_v2.py': '1e0656b19de4eb78937a9f8305569d7c1cce59f48614fb7a279738942bcd622e',
}
REUSED = {
    'angular_observation_refinement.py': '8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3',
    'so3_angular_refined_smooth_triangle_meridian_operator.py': '1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529',
    'angular_refined_smooth_triangle_literal_zero_moment_input.py': 'a4a53ff3ff92bb4fdbf8db2da048c717437d945423932e2b3d69cfc1cc06035d',
}
BASE_SCHEMA = 'complete-angular-refined-supported-smooth-triangle-reference-so3-meridian-v1'
NORMAL_SCHEMA = 'complete-angular-refined-reference-centred-analytic-J3-fixed-normal-plane-SO3-v1'
SNAPSHOT_SCHEMA = 'actual-angular-refined-analytic-J3-normal-current-point-snapshot-v1'
OLD_NORMAL_SCHEMA = 'complete-R711-reference-centred-analytic-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'
OLD_BASE = '6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'
OLD_BINDER = '307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7'
NAMES = {
    'analytic_normal_stage_jacobian.py': 'angular_refined_analytic_normal_stage_jacobian.py',
    'analytic_j3_normal_frame_c1_reuse.py': 'angular_refined_analytic_frame_c1.py',
    'analytic_j3_detached_normal_stage_matrix_reuse.py': 'angular_refined_analytic_stage_matrices.py',
    'analytic_j3_adjacent_normal_frame_matrices.py': 'angular_refined_analytic_adjacent_matrices.py',
    'reference_centred_analytic_j3_smooth_triangle_calibration.py': 'angular_refined_analytic_calibration.py',
    'so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py': 'so3_angular_refined_analytic_normal_lift.py',
    'immutable_analytic_normal_root_packets_v2.py': 'immutable_angular_refined_analytic_root_packets.py',
}


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def methods(text):
    return {(c.name, n.name): ast.dump(n, include_attributes=False)
        for c in ast.parse(text).body if isinstance(c, ast.ClassDef)
        for n in c.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}


def swap(text, old, new):
    if old not in text:
        raise ValueError('Missing exact complete-source literal: '+old)
    return text.replace(old, new)


def assignment(text, name, expression):
    node = next(n for n in ast.parse(text).body if isinstance(n, ast.Assign)
        and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)
        and n.targets[0].id == name)
    lines = text.splitlines(keepends=True)
    return ''.join(lines[:node.lineno-1])+name+' = '+expression+'\n'+''.join(lines[node.end_lineno:])


def derive(parent_directory, observation_directory):
    old = {}
    for name, digest in PINS.items():
        old[name] = (parent_directory/name).read_text()
        if sha(old[name]) != digest:
            raise ValueError('Changed complete analytic-J3 parent: '+name)
    result = {}
    for name, digest in REUSED.items():
        value = (observation_directory/name).read_text()
        if sha(value) != digest:
            raise ValueError('Changed complete generic observer/base/input source: '+name)
        result[name] = value
    substitutions = {
        OLD_BASE: REUSED['so3_angular_refined_smooth_triangle_meridian_operator.py'],
        OLD_BINDER: REUSED['angular_refined_smooth_triangle_literal_zero_moment_input.py'],
        OLD_NORMAL_SCHEMA: NORMAL_SCHEMA,
        'complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1': BASE_SCHEMA,
        'supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1': 'angular-refined-supported-smooth-triangle-literal-Q-input-v1',
        'actual-reference-centred-analytic-J3-normal-current-point-snapshot-v1': SNAPSHOT_SCHEMA,
    }
    for old_name in tuple(PINS)[:-1]:
        text = old[old_name]
        for before, after in substitutions.items():
            if before in text:
                text = text.replace(before, after)
        result[NAMES[old_name]] = text
        substitutions[PINS[old_name]] = sha(text)
        # Every function and class method is retained. Only complete source,
        # endpoint schema and base/input identity literals have changed.
        before_tree, after_tree = ast.parse(old[old_name]), ast.parse(text)
        before = {n.name: ast.dump(n, include_attributes=False) for n in before_tree.body
            if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
        after = {n.name: ast.dump(n, include_attributes=False) for n in after_tree.body
            if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
        if before != after:
            raise ValueError('An original complete analytic/root/cache method changed: '+old_name)
    packet = old['immutable_analytic_normal_root_packets_v2.py']
    packet = swap(packet, 'immutable-current-analytic-normal-chain-root-packets-with-entry-binding-v2',
        'immutable-angular-refined-analytic-normal-chain-root-packets-with-entry-binding-v1')
    marker = 'NORMALS = {\n'
    if packet.count(marker) != 1:
        raise ValueError('The whole actual packet registry changed')
    entry = dict(schema=NORMAL_SCHEMA,
        base=REUSED['so3_angular_refined_smooth_triangle_meridian_operator.py'],
        adjacent=sha(result[NAMES['analytic_j3_adjacent_normal_frame_matrices.py']]),
        calibration=sha(result[NAMES['reference_centred_analytic_j3_smooth_triangle_calibration.py']]),
        analytic=sha(result[NAMES['analytic_normal_stage_jacobian.py']]))
    normal_sha = sha(result[NAMES['so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py']])
    packet = packet.replace(marker, marker+'    '+repr(normal_sha)+': '+repr(entry)+',\n', 1)
    result[NAMES['immutable_analytic_normal_root_packets_v2.py']] = packet
    if methods(packet) != methods(old['immutable_analytic_normal_root_packets_v2.py']):
        raise ValueError('Immutable packet recording must not change any original class method')
    for name, text in result.items():
        ast.parse(text); compile(text, name, 'exec')
        if len(text.encode()) >= 100000:
            raise ValueError('Keep each complete source below 100KB: '+name)
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--parent-directory', type=Path, required=True)
    p.add_argument('--observation-directory', type=Path, required=True)
    p.add_argument('--output-directory', type=Path, required=True)
    a = p.parse_args()
    result = derive(a.parent_directory, a.observation_directory)
    a.output_directory.mkdir(parents=True, exist_ok=True)
    for name, value in result.items():
        (a.output_directory/name).write_text(value)
    print(json.dumps({n: dict(sha256=sha(v), bytes=len(v.encode())) for n,v in result.items()}, sort_keys=True))


if __name__ == '__main__':
    main()
