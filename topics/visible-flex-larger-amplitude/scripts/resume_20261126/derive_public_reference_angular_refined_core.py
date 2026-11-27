#!/usr/bin/env python3
"""Complete source-only N4096 core for the actual public-reference analytic-frame family.

No numerical module is imported or executed.  The original N2048 reference,
fixed scalar/chart/seed, radial mesh and all 32 normal stages are retained.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

PINS = {'analytic_frame_local_stage_jacobian.py': '894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866',
 'analytic_normal_frame_jets.py': '4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8',
 'analytic_frame_c1_reuse.py': 'f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb',
 'analytic_frame_detached_normal_stage_matrix_reuse.py': 'fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255',
 'analytic_frame_adjacent_normal_matrices.py': '3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695',
 'reference_centred_analytic_frame_smooth_triangle_calibration.py': 'fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0',
 'so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py': '3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc',
 'immutable_analytic_frame_normal_root_packets.py': '094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0'}
REUSED = {
    'angular_observation_refinement.py': '8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3',
    'so3_angular_refined_smooth_triangle_meridian_operator.py': '1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529',
    'angular_refined_smooth_triangle_literal_zero_moment_input.py': 'a4a53ff3ff92bb4fdbf8db2da048c717437d945423932e2b3d69cfc1cc06035d',
}
BASE_SCHEMA = 'complete-angular-refined-supported-smooth-triangle-reference-so3-meridian-v1'
NORMAL_SCHEMA = 'complete-angular-refined-public-reference-analytic-frame-normal-plane-SO3-v1'
SNAPSHOT_SCHEMA = 'actual-angular-refined-public-reference-analytic-frame-snapshot-v1'
OLD_NORMAL_SCHEMA = 'complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1'
OLD_BASE = '6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865'
OLD_BINDER = '307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7'
NAMES = {'analytic_frame_local_stage_jacobian.py': 'angular_refined_public_reference_stage_jacobian.py',
 'analytic_normal_frame_jets.py': 'angular_refined_public_reference_normal_frame.py',
 'analytic_frame_c1_reuse.py': 'angular_refined_public_reference_frame_c1.py',
 'analytic_frame_detached_normal_stage_matrix_reuse.py': 'angular_refined_public_reference_stage_matrices.py',
 'analytic_frame_adjacent_normal_matrices.py': 'angular_refined_public_reference_adjacent_matrices.py',
 'reference_centred_analytic_frame_smooth_triangle_calibration.py': 'angular_refined_public_reference_calibration.py',
 'so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py': 'so3_angular_refined_public_reference_normal_lift.py',
 'immutable_analytic_frame_normal_root_packets.py': 'immutable_angular_refined_public_reference_root_packets.py'}


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
        'actual-reference-centred-analytic-frame-normal-current-point-snapshot-v1': SNAPSHOT_SCHEMA,
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
    packet = old['immutable_analytic_frame_normal_root_packets.py']
    packet = swap(packet, 'immutable-current-analytic-full-frame-normal-root-packets-v1',
        'immutable-angular-refined-public-reference-analytic-frame-root-packets-v1')
    marker = 'NORMALS = {\n'
    if packet.count(marker) != 1:
        raise ValueError('The whole actual packet registry changed')
    entry = dict(schema=NORMAL_SCHEMA,
        base=REUSED['so3_angular_refined_smooth_triangle_meridian_operator.py'],
        adjacent=sha(result[NAMES['analytic_frame_adjacent_normal_matrices.py']]),
        calibration=sha(result[NAMES['reference_centred_analytic_frame_smooth_triangle_calibration.py']]),
        analytic=sha(result[NAMES['analytic_frame_local_stage_jacobian.py']]),
        analytic_frame=sha(result[NAMES['analytic_normal_frame_jets.py']]))
    normal_sha = sha(result[NAMES['so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py']])
    packet = packet.replace(marker, marker+'    '+repr(normal_sha)+': '+repr(entry)+',\n', 1)
    result[NAMES['immutable_analytic_frame_normal_root_packets.py']] = packet
    if methods(packet) != methods(old['immutable_analytic_frame_normal_root_packets.py']):
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
