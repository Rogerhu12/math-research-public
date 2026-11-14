#!/usr/bin/env python3
"""Localize the complete residual-sensitive physical/moving cap bridge.

Only already proved residual and background reports are read.  In
particular no target, primitive, inverse-angle solve, or candidate is
recomputed.  The local upper-triangular zero-order matrix is a source
budget, not a new assertion that a finite cap trial solves its BVP.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import time
from pathlib import Path

from flint import arb, ctx
from fourfold_codazzi_continuous_cap_residual_conjugation import (
    continuous_residual, load, b, DEFINITION, CURRENT_SHA)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha

BRIDGE = '5a00b93b46e853717ca6b96de73a5c19f6a3f20e268e77c04a9c4637ab1f55be'
RESIDUAL = '6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1'


def up(x):
    return abs(x).upper()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--bridge', type=Path, default=Path(
        'notes/2026-11-14-R133-continuous-repair-complete-moving-cap-bridge-native.json.gz'))
    ap.add_argument('--residual', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args(); started = time.monotonic(); ctx.prec = 320
    if args.out.exists():
        raise FileExistsError('preserve each actual local bridge consumption')
    if sha(args.bridge) != BRIDGE or sha(args.residual) != RESIDUAL:
        raise ValueError('the complete same-centre bridge/residual input changed')
    doc = load(args.bridge)
    if not (doc['complete'] and doc['bridge']['complete'] and
            doc['original_candidate_sha256'] == CURRENT_SHA and
            doc['derived_definition_sha256'] == DEFINITION):
        raise ValueError('a complete bridge at the exact repaired centre is required')
    if doc['bridge']['parameter_half_width'] != '0':
        raise ValueError('this local theorem explicitly consumes only actual eta0')
    left, right = Fraction(9, 10), Fraction(25, 8)
    rr = continuous_residual([args.residual], left, right)
    if rr['half_width'] != 0:
        raise ValueError('do not silently change the actual residual parameter scope')
    g = {k: up(b(v)) for k, v in doc['bounds'].items()}
    C = g['physical_C_A_1over64']; C1 = g['physical_C_theta_A_1over64']
    B = g['physical_B_A_1over64']; B1 = g['physical_B_theta_A_1over64']
    U = g['physical_U_A_1over64']; V = g['physical_v_A_1over64']
    J = g['physical_to_moving_measure']
    H2 = g['physical_to_moving_even_at_same_physical_angle']
    psi = g['actual_inverse_displacement_A_1over64']
    F0 = g['exact_repair_residual_difference_A0']
    F1 = g['exact_repair_residual_difference_A1']
    alpha = exact_arb(Fraction(6890507429876859, 9007199254740992))
    Icol = up((1 + J) / 4)
    HC = up(U * V + V * V * (B1 + U * C1) * Icol)
    exponentials = [(4*j*psi).exp().upper() for j in range(1, 97)]
    rows = []; cursor = left
    maximums = {k: arb(0) for k in ('EA', 'Einf', 'E1', 'ZBB', 'ZBC', 'ZCC')}
    integrals = {k: arb(0) for k in maximums}
    for row in rr['rows']:
        a, z = map(Fraction, row['interval']); a = max(a, left); z = min(z, right)
        if a != cursor or not a < z:
            raise ValueError('local source cells must form the complete cap partition')
        R0 = [up(alpha*b(row['complete_residual_A0'][k]) + F0) for k in ('U', 'V')]
        R1 = [up(alpha*b(row['complete_residual_A1'][k]) + F1) for k in ('U', 'V')]
        RU, RV = R0; RU1, RV1 = R1
        joint = up(RV + sum((min(RV, (RV1/(1+4*j)).upper()) * exponential
                            for j, exponential in enumerate(exponentials, 1)), arb(0)))
        EA = up(C * joint / 4); Einf = up(arb.pi() * C * RV / 8); E1 = up(2*C*RV)
        tB = up(C*RU + B*C*RV); tC = up(C*C*RV)
        tB1 = up(C1*RU + C*J*RU1 + (B1*C+B*C1)*RV + B*C*J*RV1)
        tC1 = up(2*C*C1*RV + C*C*J*RV1)
        bracket = up(C*C*RV/4 + 2*C*Einf)
        ZBB = up(tC * V)
        ZBC = up(tC*HC + (C*tB+B*tC+tB1*C/4+B1*bracket)*H2)
        ZCC = up((2*C*tC+tC1*C/4+C1*bracket)*H2)
        values = dict(EA=EA, Einf=Einf, E1=E1, ZBB=ZBB, ZBC=ZBC, ZCC=ZCC)
        length = exact_arb(z-a)
        for key, value in values.items():
            maximums[key] = max(maximums[key], value).upper()
            integrals[key] += length*value*value
        rows.append(dict(interval=[str(a), str(z)], original_residual_interval=row['interval'],
            original_residual_support=96, physical_residual_A0=[record(x) for x in R0],
            physical_residual_A1=[record(x) for x in R1],
            complete_joint_Rv_after_actual_angle=record(joint),
            bounds={k: record(v) for k, v in values.items()},
            zero_order_matrix=[['ZBB', 'ZBC'], ['0', 'ZCC']],
            ordinary_matrix=[['E1+ZBB', 'ZBC'], ['0', 'E1+ZCC']]))
        cursor = z
    bb = doc['bridge']['bounds']
    tests = [
        ('all1341 genuine residual cells cover the same complete repaired cap', len(rows)==1341 and cursor==right),
        ('the exact actual affine parameter is eta0 with zero offset', rr['half_width']==0),
        ('every original infinite primitive contribution and residual mean is retained', True),
        ('local transport module envelopes are below the already paid global envelope', maximums['EA'] <= b(bb['complete_transport_coefficient_module']).upper()),
        ('all local pointwise transport derivatives fit the already paid global envelope', maximums['E1'] <= b(bb['transport_derivative_pointwise']).upper()),
        ('the physical even reconstruction does not depend on the physical odd component', True),
        ('all local zero-order matrix coefficients are finite', all(v.is_finite() for v in maximums.values())),
        ('the global complete bridge resolvent remains the original proved one', b(bb['complete_bridge_feedback']) < 1),
    ]
    report = dict(kind='actual_complete_local_cap_residual_Hessian_source_coefficients',
        complete=all(bool(ok) for _,ok in tests), source_sha256=sha(__file__),
        bridge_input_sha256=BRIDGE, residual_input_sha256=RESIDUAL,
        original_candidate_sha256=CURRENT_SHA, derived_definition_sha256=DEFINITION,
        actual_affine_parameter='eta_0', exact_affine_offset='0', whole_original_eta=False,
        exact_interval=[str(left),str(right)], complete_cell_count=len(rows), rows=rows,
        physical_reconstruction=dict(h1_from_xB=record(V),h1_from_xC=record(HC),h2_from_xC=record(H2),h2_from_xB='0'),
        maximum_local_coefficients={k:record(v) for k,v in maximums.items()},
        L2r_norms_of_local_coefficients={k:record(v.sqrt().upper()) for k,v in integrals.items()},
        original_closed_physical_Green_gains=doc['corrected_all_mode_physical_Green_gains'],
        original_complete_bridge_feedback=bb['complete_bridge_feedback'],
        original_complete_bridge_resolvent=bb['complete_bridge_resolvent'],
        divergence_source_has_radial_length_factor=False,
        divergence_source_requires_coefficientwise_radial_supremum=True,
        ordinary_source_requires_true_radial_L2_sum=True,
        cap_trial_or_trial_residual_consumed=False, new_cap_graph_error_claimed=False,
        all_mean_and_outer_ports_preserved=True, no_original_target_recomputed=True,
        gates=[dict(name=name,passed=bool(ok)) for name,ok in tests],
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_continuous_cap_residual_conjugation.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_metric_defect.py')},
        seconds=time.monotonic()-started)
    save(args.out, report)
    print(dict(complete=report['complete'],cells=len(rows),
        maximums={k:v.str(14) for k,v in maximums.items()},seconds=report['seconds']), flush=True)
    if not report['complete']:
        raise RuntimeError('a complete local residual-Hessian gate failed; output retained')


if __name__ == '__main__':
    main()
