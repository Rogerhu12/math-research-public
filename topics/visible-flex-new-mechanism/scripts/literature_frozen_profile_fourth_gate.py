#!/usr/bin/env python3
"""Profile-only refinement of the frozen first full-fourth evaluation.

No geometry, compiler, spectral refit, or optimization is performed.  Actual
profile integrals are restricted to this public repository's GitHub Actions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time
from types import SimpleNamespace

import numpy as np

import literature_full_fourth_evaluate as full
import literature_range_numeric_engine as engine

LD, CD = engine.LD, engine.CD


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def pair(value):
    return [float(np.real(value)), float(np.imag(value))]


def validate_profile_identity(definition):
    copied = dict(definition)
    expected = copied.pop('profile_identity_sha256')
    encoded = json.dumps(copied, sort_keys=True, separators=(',', ':'), allow_nan=False)
    actual = hashlib.sha256(encoded.encode()).hexdigest()
    if actual != expected:
        raise ValueError('frozen profile canonical identity mismatch')
    return actual


def profile_level(definition, n, deadline):
    # An empty atom table asks the already-frozen implementation only for
    # its 17 panels, five analytic input jets, and true right primitive.
    table = full.ProfileTable(SimpleNamespace(atoms=[], ids={}), definition, n, deadline)
    x, w = table.nodes, table.weights
    q, q1, q2, q3 = table.qjets[:4]
    Q = 1 + x * x
    density = Q * q2 * q2 + 2 * q1 * q1
    negative_tail, negative_total = table.primitive(density)
    J, J_total = -negative_tail, -negative_total
    local_L = x * Q * q2 * q2 - 2 * Q * q1 * q2
    a = x * q2 - q1
    F = Q * q2 - 2 * q
    B = F * F / 2 - 2 * Q * a * a - Q * Q * a * q3
    V = -(Q * q1 * q1 + x * J) / 8
    V_prime = (local_L - J) / 8
    V_second = a * (a + Q * q3) / 4
    # All products here are ordinary complex products, never Hermitian ones.
    E_sobolev = w @ (Q * V_second * V_second / 4 + V_prime * V_prime / 2)
    YV_u_T = (x * V_second - V_prime) / 2
    YV_u_B = V - x * V_prime + x * x * V_second / 2
    actual_energy_density = (YV_u_T * YV_u_T + YV_u_B * YV_u_B) / (x * x)
    E_direct = w @ actual_energy_density
    T_direct = w @ (B * V_second) / 32
    F_direct = E_direct + 2 * T_direct
    square_density = (
        2 * Q * q2 * q2 * (
            (q - x * q1 + (x * x - 1) * q2 / 6) ** 2
            + (q1 - x * q2 / 3) ** 2
        )
        + Q ** 3 * q2 ** 4 / 36
        + 4 * q1 * q1 * (q - x * q1 / 3) ** 2
        + 2 * (x * x + 3) * q1 ** 4 / 9
    )
    F_local = w @ square_density / 128
    left = LD(definition['physical_interval'][0])
    boundary_correction = J_total * J_total / (256 * left)
    sobolev_boundary_correction = -left * J_total * J_total / 128
    energy_boundary_correction = J_total * J_total * (left / 128 + 1 / (256 * left))
    localization_error = F_direct - F_local - boundary_correction
    direct_scale = w @ (
        abs(actual_energy_density) + abs(B * V_second / 16)
    )
    local_scale = w @ abs(square_density) / 128
    positive_tail_scale = w @ (Q * abs(q2) ** 2 + 2 * abs(q1) ** 2)
    return dict(
        quadrature_n=n, total_profile_nodes=len(x),
        profile_moments=table.complex_moments(),
        J_total=pair(J_total),
        J_total_relative=float(abs(J_total) / max(LD('1e-100'), positive_tail_scale)),
        E_direct_physical_Yu_square=pair(E_direct),
        E_sobolev_form_before_boundary=pair(E_sobolev), T_direct=pair(T_direct),
        F_direct_on_frozen_finite_interval=pair(F_direct),
        F_sobolev_form_before_boundary=pair(E_sobolev + 2 * T_direct),
        F_local_ordinary_complex_polynomial=pair(F_local),
        exact_off_constraint_boundary_correction=pair(boundary_correction),
        exact_sobolev_to_local_boundary_correction=pair(sobolev_boundary_correction),
        exact_physical_energy_minus_sobolev_boundary=pair(energy_boundary_correction),
        physical_energy_boundary_residual=pair(E_direct - E_sobolev - energy_boundary_correction),
        sobolev_localization_residual=pair(E_sobolev + 2 * T_direct - F_local - sobolev_boundary_correction),
        localization_residual=pair(localization_error),
        localization_relative_to_direct_absolute_sum=float(
            abs(localization_error) / max(LD('1e-100'), direct_scale)
        ),
        direct_absolute_term_sum=float(direct_scale),
        local_absolute_density_integral=float(local_scale),
        function_values_are_not_interval_enclosures=True,
        profile_refit=False, geometry_evaluated=False,
        exact_quadratic_tail_zero_certified=False,
        exact_first_constant_fourth_gate_certified=False,
        all_constant_states_or_fourth_periods_evaluated=False,
    )


def toy_check():
    # A differential-polynomial boundary identity, not a profile integral.
    import sympy as sp
    x, J, q1, q2, q3 = sp.symbols('x J q1 q2 q3')
    Q = 1 + x * x
    Jp = -Q * q2 * q2 - 2 * q1 * q1
    derivative = lambda z: sp.diff(z, x) + sp.diff(z, J) * Jp + sp.diff(z, q1) * q2 + sp.diff(z, q2) * q3
    A = Q * (2 * q1 * q2 - x * q2 * q2)
    rhs = derivative(x * J * J + 2 * J * Q * q1 * q1) + 2 * Q * Q * q1 * q1 * q2 * q2 + 4 * Q * q1 ** 4
    assert sp.expand(J * J + 2 * J * A - rhs) == 0
    v, v1, v2 = sp.symbols('v v1 v2')
    dv = lambda z: sp.diff(z, x) + sp.diff(z, v) * v1 + sp.diff(z, v1) * v2
    physical = ((x * v2 - v1) ** 2 / 4 + (v - x * v1 + x * x * v2 / 2) ** 2) / (x * x)
    sobolev = Q * v2 * v2 / 4 + v1 * v1 / 2
    energy_boundary = v * v1 - v * v / x - (x / 2 + 1 / (4 * x)) * v1 * v1
    assert sp.cancel(physical - sobolev - dv(energy_boundary)) == 0
    sample = {'kind': 'artificial identity-only object', 'value': 1}
    encoded = json.dumps(sample, sort_keys=True, separators=(',', ':'), allow_nan=False)
    sample['profile_identity_sha256'] = hashlib.sha256(encoded.encode()).hexdigest()
    assert validate_profile_identity(sample) == sample['profile_identity_sha256']
    return dict(schema='frozen-profile-fourth-gate-toy-v1',
        exact_tail_boundary_identity=True, exact_physical_energy_boundary_identity=True,
        synthetic_identity_binding=True,
        profile_or_geometry_integrals_evaluated=False,
        source_sha256=sha(__file__))


def run(args):
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise RuntimeError('actual profile integration is authorized only in this public repository Actions')
    if sha(args.input) != args.input_sha256:
        raise ValueError('actual full-fourth output SHA mismatch')
    original = json.loads(args.input.read_text())
    if original.get('schema') != 'R45-full-fourth-function-evaluation-v1' or original.get('completion') != 'complete':
        raise ValueError('expected the completed frozen first full-fourth evaluation')
    if original['runner_sha256'] != sha(full.__file__):
        raise ValueError('frozen profile producer source has changed')
    if original['source_hashes']['literature_range_numeric_engine.py'] != sha(engine.__file__):
        raise ValueError('frozen Gauss/primitive source has changed')
    definition = original['profile_definition']
    identity = validate_profile_identity(definition)
    if definition.get('kind') != 'R52-even-four-mode-overlapping-eight-packet-profile':
        raise ValueError('this diagnostic is for the original R52 frozen profile')
    if definition['physical_interval'][0] <= 0:
        raise ValueError('the first standard-state physical interval must be positive')
    start = time.monotonic()
    deadline = start + args.max_seconds
    levels = []
    for n in args.nodes:
        if time.monotonic() > deadline:
            raise TimeoutError('profile-only diagnostic budget exceeded')
        levels.append(profile_level(definition, n, deadline))
    return dict(
        schema='frozen-R52-profile-fourth-local-gate-v1', completion='complete',
        input_sha256=args.input_sha256, input_source=original['github'],
        profile_identity_sha256=identity,
        geometry_identity_sha256_for_reference_only=original['geometry_identity_sha256'],
        unchanged_profile_definition=definition,
        source_sha256=sha(__file__),
        imported_source_hashes={
            'literature_full_fourth_evaluate.py': sha(full.__file__),
            'literature_range_numeric_engine.py': sha(engine.__file__),
        },
        github={k: os.environ.get(k) for k in ('GITHUB_REPOSITORY', 'GITHUB_RUN_ID', 'GITHUB_RUN_ATTEMPT', 'GITHUB_SHA')},
        elapsed_seconds=time.monotonic() - start, validation=levels,
        profile_or_geometry_refit=False, geometry_evaluated=False,
        full_formal_compilation_performed=False,
        R53_fourth_leading_gate_claimed=False,
        exact_fixed_target_family_constructed=False, task_complete=False,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path)
    parser.add_argument('--input-sha256')
    parser.add_argument('--nodes', nargs='+', type=int, default=[256, 512])
    parser.add_argument('--max-seconds', type=float, default=120)
    parser.add_argument('--toy-only', action='store_true')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if not args.toy_only and (args.input is None or args.input_sha256 is None):
        parser.error('--input and --input-sha256 are required for actual evaluation')
    if any(n < 4 for n in args.nodes) or args.max_seconds <= 0:
        parser.error('nodes must be at least 4 and budget must be positive')
    result = toy_check() if args.toy_only else run(args)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + '\n')


if __name__ == '__main__':
    main()
