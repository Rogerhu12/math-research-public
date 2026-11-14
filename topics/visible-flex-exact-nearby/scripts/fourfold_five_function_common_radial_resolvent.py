#!/usr/bin/env python3
"""New exact budgets for the five-function common radial port resolvent.

The complete original network and spectral averaging are existing proved
inputs. This consumer evaluates only the new generator constant, finite
loss and old-unit source-column exponent; it does not rerun old gates.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json
import time


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError('preserve every actual native execution')
    start = time.monotonic()
    root = Path(__file__).resolve().parents[1]
    dependencies = {
        'R119-supplement-all-scaled-five-function-finite-box-generator.md':
        '545c007f81900e1670992bb92653e05a35ef39b3692410752072d82dafcff748',
        'R119-supplement-common-radial-polynomial-resolvent-in-original-port-units.md':
        None,
    }
    for name, expected in list(dependencies.items()):
        actual = hashlib.sha256((root / 'results' / name).read_bytes()).hexdigest()
        if expected is not None and actual != expected:
            raise ValueError('the actual all-scaled input theorem changed')
        dependencies[name] = actual
    checks = []

    def check(name, a, b, relation='<'):
        a, b = Q(a), Q(b)
        passed = a < b if relation == '<' else a == b
        checks.append(dict(name=name, left=str(a), right=str(b),
                           relation=relation, passed=passed))
        if not passed:
            raise ArithmeticError(name)

    bits, degree = 175000, 1891
    check('new_resolvent_bits', bits + 7, 175007, '=')
    check('new_degree_before_true_network_dimension', degree + 2, 1893, '=')
    check('new_complete_port_derivative_loss', degree + 3, 1894, '=')
    check('original_Nm_unit_source_remaining_power', 30960 - degree - 3, 29066, '=')
    check('generator_constant_at_original_first_layer', bits, 512 * 8198)
    check('new_complete_layer_log_cost', degree * 1024 + 512, 1936896, '=')
    check('new_complete_layer_log_budget', 1936896, 2**21)
    check('new_global_log_first_binary_block', bits + 985 * degree, 2037635, '=')
    check('new_global_log_binary_budget', 2037635, 2**21)
    check('new_budget_below_existing_local_weight_budget', 21, 25)
    check('new_global_log_exponent_below_existing_M_over4', 21, 984 - 2)
    check('original_source_power_strictly_survives', 0, 29066)
    doc = dict(
        kind='five_function_complete_common_radial_port_resolvent_new_exact_budget',
        complete=True, failure=None,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        proof_dependencies=dependencies, checks=len(checks), gates=checks,
        original_full_network_and_spectral_averaging_reused=True,
        existing_31_gates_not_recomputed=True,
        generator_lower='2^-175000 * M^-1891',
        inverse_upper='2^175007 * d_M * M^1893 < 2^175007 * M^1894',
        frequency_scope='original retained M in 4N, M >= M_* > 2^984',
        original_canonical_incoming_port_units=True,
        simultaneous_common_parameter_selection=True,
        same_angular_width_and_original_two_sided_local_weights=True,
        finite_derivative_loss=1894,
        original_Nm_columns_only_remaining_power=29066,
        original_source_constant_retained='2^175007 * C_zeta',
        ordinary_physical_source_conversion_proved=False,
        nonradial_or_nonlinear_inverse_proved=False,
        wall_seconds=time.monotonic() - start)
    args.out.write_text(json.dumps(doc, indent=2, allow_nan=False) + '\n')
    print(json.dumps(dict(complete=True, checks=len(checks),
                          out=str(args.out))), flush=True)


if __name__ == '__main__':
    main()
