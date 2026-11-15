#!/usr/bin/env python3
"""A fourth, independent odd C2 zero-jet shape on the second original support.

This is a new scalar family, not a new solution of a previously fixed g.
All three resonance equations, all 112 tail rows and all original physical
domain/final checks remain.  The full design derivative has shape 3 by 4.
The old square physical-circle check uses a transparent fixed-theta view
with the original three active p coordinates; theta is still present in
every scalar jet.  No additional core target or tail mode is introduced.
All numerical evaluation, including descriptor/domain work, is Actions-only.
"""
from __future__ import annotations

import os
if (os.environ.get('GITHUB_ACTIONS') != 'true'
        or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
    raise RuntimeError('This new scalar/model family may only be imported in public Actions')
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np

import geometry_20261114_small_core_resonance as base
from geometry_20261114_full_dn_augmented import AugmentedFlow
from geometry_20261114_physical_test_boundary import PhysicalTestBoundary
from geometry_20261114_lifted_modes_profile import scalar_spec as old_scalar_spec, field_spec
from geometry_20261114_full_prefix_operator import (
    export_scalar_descriptor as old_descriptor, ScalarExpression as OldExpression,
    Q, canonical_sha, encoded)

HERE = Path(__file__).resolve().parent
SCHEMA = 'R259-four-control-circle-full-three-resonance-family-v1'
SCALAR_SCHEMA = 'complete-prefix-three-even-plus-second-support-odd-control-v1'
DESCRIPTOR_SCHEMA = 'complete-four-control-scalar-real-expression-v1'
SUPPORT_INDEX = 1
original, EXPECTED, write = base.original, base.EXPECTED, base.write
CompleteResidual = base.CompleteResidual
SOURCE_PINS = {
    'geometry_20261114_small_core_resonance.py': '3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5',
    'geometry_20261114_full_scalar_profile.py': '8ff23e31a58d0f8b087929d69ac8d6f9b6f2777615e50eef5ebe40ed7b6bed6b',
    'geometry_20261114_prefix_controls_profile.py': 'f019e6b33c8e1776d5cca87c22efadd0f999766b894be855efb53ad10b4d6a24',
    'geometry_20261114_lifted_modes_profile.py': '13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5',
    'geometry_20261114_full_prefix_operator.py': 'a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703',
    'geometry_20261114_full_dn_augmented.py': 'f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e',
    'geometry_20261114_physical_test_boundary.py': '3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681',
}


def checked_sources():
    found = {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in SOURCE_PINS}
    if found != SOURCE_PINS:
        raise ValueError('The original scalar, circle or physical boundary source differs')
    return {**found, Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


class OddBump:
    """w^2 P(x)(2x-1), P=64x^3(1-x)^3, with the original stored w."""
    def __init__(self, original_bump):
        self.left, self.right, self.width = (float(getattr(original_bump, name))
                                             for name in ('left', 'right', 'width'))
        if not all(math.isfinite(v) for v in (self.left, self.right, self.width)) or self.width <= 0:
            raise ValueError('The added control must retain an actual finite positive original support')

    def jet(self, s):
        x = (float(s)-self.left)/self.width
        if x <= 0 or x >= 1:
            return np.zeros(3)
        P = 64*x**3*(1-x)**3
        dP = 64*(3*x**2-12*x**3+15*x**4-6*x**5)
        ddP = 64*(6*x-36*x**2+60*x**3-30*x**4)
        return np.asarray([self.width**2*P*(2*x-1),
            self.width*(dP*(2*x-1)+2*P), ddP*(2*x-1)+4*dP])


class FourControlProfile:
    def __init__(self, original_three):
        if original_three.parameter_count != 3 or len(original_three.bumps) != 3:
            raise ValueError('Keep the exact three original supports before adding the odd control')
        self.original_three = original_three
        self.odd = OddBump(original_three.bumps[SUPPORT_INDEX])
        self.parameter_count = 4
        self.bumps = [*original_three.bumps, self.odd]

    def __getattr__(self, name):
        return getattr(self.original_three, name)

    def base_jet(self, s):
        return self.original_three.base_jet(s)

    def control_jets(self, s):
        return np.column_stack((self.original_three.control_jets(s), self.odd.jet(s)))

    def profile(self, s, parameters=None):
        p = np.zeros(4) if parameters is None else np.asarray(parameters)
        if p.shape != (4,):
            raise ValueError('The new family must consume p1,p2,p3,theta together')
        jet = self.original_three.base_jet(s)+self.original_three.control_jets(s)@p[:3]
        if p[3] != 0:
            jet = jet+p[3]*self.odd.jet(s)
        if not np.all(np.isfinite(jet)) or jet[0] <= 0 or abs(jet[1]) >= 1:
            raise FloatingPointError("The actual four-control scalar metric left a>0, |a'|<1")
        return tuple(jet)

    def description(self):
        result = dict(self.original_three.description())
        original_polynomial = result.pop('control_polynomial')
        original_profile_source = result['profile_source_sha256']
        result.update(scope=__doc__, scalar_schema=SCALAR_SCHEMA, scalar_parameters=4,
            control_scheme='original-three-even-plus-second-original-support-odd-v1',
            original_three_control_polynomial=original_polynomial,
            original_three_profile_source_sha256=original_profile_source,
            profile_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            original_three_parameter_source=type(self.original_three).__name__,
            original_three_supports_retained=True, odd_control_support_index=SUPPORT_INDEX,
            control_supports=[[b.left,b.right] for b in self.bumps],
            control_supports_binary64=[[b.left,b.right] for b in self.bumps],
            control_definition='three original even bumps plus theta*b2(x)*(2*x-1)',
            added_control_formula='stored_width^2*64*x^3*(1-x)^3*(2*x-1), zero for x<=0 or x>=1',
            zero_theta_is_original_family_mathematically=True,
            response_rank_improvement_or_root_existence_claimed=False,
            design_family_is_a_new_g_family=True,
            four_active_parameters_are_not_the_original_square_full_DN_system=True,
            final_circle_check_fixes_theta_and_keeps_three_active_parameters=True)
        result.pop('left_boundary_rows', None)
        result.pop('right_boundary_rows', None)
        return result


class ThetaFrozenProfile:
    """Exactly the same new scalar formula, with theta held at its current value."""
    def __init__(self, designed, theta):
        self.designed_four = designed
        self.theta = float(theta)
        if not math.isfinite(self.theta):
            raise ValueError('Freeze an actual finite fourth coefficient')
        self.parameter_count = 3
        self.bumps = designed.original_three.bumps

    def __getattr__(self, name):
        return getattr(self.designed_four.original_three, name)

    def base_jet(self, s):
        value = self.designed_four.original_three.base_jet(s)
        return value if self.theta == 0 else value+self.theta*self.designed_four.odd.jet(s)

    def control_jets(self, s):
        return self.designed_four.original_three.control_jets(s)

    def profile(self, s, parameters=None):
        p = np.zeros(3) if parameters is None else np.asarray(parameters)
        if p.shape != (3,):
            raise ValueError('The square final check retains its three original active p coordinates')
        return self.designed_four.profile(s, np.r_[p,self.theta])


def setup(accepted, prepared, anchor, angles=4096, workers=1):
    old, original_flow, original_boundary = base.setup(accepted, prepared, anchor, angles, workers)
    return FourControlProfile(old), original_flow, original_boundary


def scalar_spec(profile, port, parameters, accepted_sha256):
    if not isinstance(profile, FourControlProfile):
        raise TypeError('Use the actual four-control profile for the new scalar identity')
    p = np.asarray(parameters, float)
    if p.shape != (4,) or not np.all(np.isfinite(p)):
        raise ValueError('Freeze the complete actual four-parameter scalar')
    old = old_scalar_spec(profile.original_three, port, p[:3], accepted_sha256)
    return dict(schema=SCALAR_SCHEMA, original_three_parameter_specification=old,
        frozen_design_parameters=p.tolist(), odd_control_support_index=SUPPORT_INDEX,
        odd_control=dict(left=profile.odd.left, right=profile.odd.right, stored_width=profile.odd.width,
            normalized_formula='64*x^3*(1-x)^3*(2*x-1)', width_prefactor_power=2,
            zero_extension=True, scalar_zero_jet_order=2,
            mathematical_support_uses_left_plus_stored_width=True),
        profile_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        complete_scalar_source_sha256=checked_sources(),
        field_modes=profile.M, tail_modes=profile.tail_modes,
        fixed_core_targets_count=3, native_right_rows=profile.M,
        new_scalar_family_not_a_same_g_refinement=True,
        canonical_material_metric='ds^2+a(s;p1,p2,p3,theta)^2*dtheta_material^2')


def export_scalar_descriptor(profile, specification):
    if specification.get('schema') != SCALAR_SCHEMA:
        raise ValueError('Do not relabel the new four-control scalar as an old v3 metric')
    p = specification['frozen_design_parameters']
    rebuilt = scalar_spec(profile, specification['original_three_parameter_specification']['complete_original_port'],
                          p, specification['original_three_parameter_specification']['accepted_prefix_sha256'])
    if rebuilt != specification:
        raise ValueError('The complete current four-control scalar identity differs')
    old = old_descriptor(profile.original_three, specification['original_three_parameter_specification'],
                         origin='unspecified-runtime-object')
    odd = specification['odd_control']
    expression = dict(base_three_parameter_expression=old['mathematical_expression'],
        base_three_parameter_identity_sha256=old['mathematical_identity_sha256'],
        odd_control_support_index=SUPPORT_INDEX, theta=encoded(p[3]),
        odd_control=encoded({k:odd[k] for k in ('left','right','stored_width')}),
        added_radius_formula='theta*w^2*64*x^3*(1-x)^3*(2*x-1), zero extension',
        added_returned_ap_formula='theta*w*(Pprime(x)*(2*x-1)+2*P(x))',
        added_returned_app_formula='theta*(Psecond(x)*(2*x-1)+4*Pprime(x))',
        source_sha256=specification['profile_source_sha256'],
        original_finite_Gauss_radius_and_independent_ap_app_retained=True)
    return dict(schema=DESCRIPTOR_SCHEMA, full_specification_sha256=canonical_sha(specification),
        mathematical_expression=expression, mathematical_identity_sha256=canonical_sha(expression),
        base_three_parameter_descriptor=old,
        new_metric_family=True, old_scalar_domain_certificate_reused=False,
        literal_floating_evaluator_error_verified=False,
        original_global_scalar_C2_interfaces_verified_here=False,
        added_control_alone_has_exact_declared_zero_012_jets=True)


class ScalarExpression:
    def __init__(self, specification, descriptor, primitive):
        if (descriptor.get('schema') != DESCRIPTOR_SCHEMA
                or descriptor['full_specification_sha256'] != canonical_sha(specification)
                or descriptor['mathematical_identity_sha256'] != canonical_sha(descriptor['mathematical_expression'])):
            raise ValueError('Bind the complete new expression, including theta and its fourth shape')
        self.base = OldExpression(specification['original_three_parameter_specification'],
                                  descriptor['base_three_parameter_descriptor'], primitive)
        self.theta = Q(float(specification['frozen_design_parameters'][3]))
        control = self.base.controls[SUPPORT_INDEX]
        self.left, self.width = control['left'], control['stored_width']
        self.breakpoints = self.base.breakpoints
        self.b = self.base.b

    def branch(self, middle):
        return self.base.branch(middle)

    def value(self, s, branch, middle):
        value = self.base.value(s, branch, middle)
        if self.theta and self.left < middle < self.left+self.width:
            u = (s-self.b(self.left))/self.b(self.width)
            value += self.b(self.theta)*self.b(self.width)**2*64*u**3*(1-u)**3*(2*u-1)
        return value

    def returned_ap(self, s, branch, middle):
        value = base.returned_ap(self.base, s, branch, middle)
        if self.theta and self.left < middle < self.left+self.width:
            u = (s-self.b(self.left))/self.b(self.width)
            P = 64*u**3*(1-u)**3
            dP = 64*(3*u**2-12*u**3+15*u**4-6*u**5)
            value += self.b(self.theta)*self.b(self.width)*(dP*(2*u-1)+2*P)
        return value


def scalar_domain(profile, specification, output, bits, maximum_depth):
    """Fresh whole-interval a and independently returned ap for this actual new g."""
    import geometry_20261114_direct_operator_cell as primitive
    primitive.ctx.prec = bits
    descriptor = export_scalar_descriptor(profile, specification)
    expression = ScalarExpression(specification, descriptor, primitive)
    rows, failed, totals = [], [], dict(leaf_count=0, split_cells=0)

    def visit(left, right, depth):
        middle = (left+right)/2
        branch = expression.branch(middle)
        interval = primitive.arb(str(middle), str((right-left)/2))
        radius = expression.value(interval, branch, middle)
        speed = expression.returned_ap(interval, branch, middle)
        good = bool(radius.is_finite() and speed.is_finite()
            and radius.lower() > 0 and speed.abs_upper() < 1)
        bad = bool(radius.is_finite() and speed.is_finite()
            and (radius.upper() <= 0 or speed.lower() >= 1 or speed.upper() <= -1))
        if not good and not bad and depth < maximum_depth:
            totals['split_cells'] += 1
            visit(left, middle, depth+1)
            visit(middle, right, depth+1)
            return
        totals['leaf_count'] += 1
        row = dict(interval=[str(left),str(right)], branch=list(branch), depth=depth,
            radius_enclosure=primitive.ball_record(radius), returned_ap_enclosure=primitive.ball_record(speed),
            strict_positive_radius_and_abs_ap_lt_one=good, definite_scalar_domain_failure=bad)
        rows.append(row)
        if not good:
            failed.append(row)

    for left,right in zip(expression.breakpoints[:-1],expression.breakpoints[1:]):
        visit(left,right,0)
    report = dict(schema='R259-four-control-complete-declared-scalar-domain-enclosure-v1',
        descriptor=descriptor, covered_interval=[str(expression.breakpoints[0]),str(expression.breakpoints[-1])],
        bits=bits, maximum_depth=maximum_depth, **totals,
        complete_declared_real_expression_domain_certified=not failed,
        unresolved_leaf_count=len(failed), leaves=rows,
        fresh_new_four_control_identity=descriptor['mathematical_identity_sha256'],
        old_scalar_domain_certificate_reused=False, source_returned_ap_used=True,
        returned_ap_identified_with_derivative_of_finite_Gauss_a=False,
        exact_prefix_scalar_and_complete_stored_finite_Gauss_expression=True,
        literal_binary64_evaluation_roundoff_enclosed=False,
        exact_scalar_derivative_compatibility_or_C2_interface_certificate=False,
        source_circle_R_and_full_Frenet_domain_covered_by_this_scalar_bound=False)
    write(Path(output)/'complete-scalar-domain.json.gz',report)
    return {k:v for k,v in report.items() if k not in ('leaves','descriptor')}


class CircleReference:
    def __init__(self, profile, mesh, true_slope_jacobian, target, height_sign, cut_scale):
        self.profile = profile
        self.x = np.asarray(mesh, float)
        self.h = np.diff(self.x)
        self.mid = .5*(self.x[:-1]+self.x[1:])
        self.base = np.asarray([profile.base_jet(s) for s in self.x])[:, :2]
        self.base_mid = np.asarray([profile.base_jet(s) for s in self.mid])[:, :2]
        self.controls = np.asarray([profile.control_jets(s) for s in self.x])[:, :2]
        self.controls_mid = np.asarray([profile.control_jets(s) for s in self.mid])[:, :2]
        self.J = np.asarray(true_slope_jacobian)
        self.target = np.asarray(target)
        self.eh, self.gamma = height_sign, cut_scale
        self.M = profile.M
        if self.J.shape != (self.M, self.M) or self.target.shape != (3,):
            raise ValueError("Retain all native slope rows and exactly the declared three target entries")
        self.offdiagonal = self.J.copy()
        np.fill_diagonal(self.offdiagonal, 0.)
        self.exactly_diagonal = bool(np.count_nonzero(self.offdiagonal) == 0)
        self.frequency = np.array([2., 4., 6.])

    def matrix(self, ratio, radius, speed, vertical):
        k2 = self.frequency**2
        answer = np.empty((len(radius), 3, 2, 2), dtype=np.result_type(radius, speed))
        answer[:, :, 0, 0] = ratio[:, None]*(1-k2)
        answer[:, :, 0, 1] = -vertical[:, None]*k2/radius[:, None]
        answer[:, :, 1, 0] = (speed*ratio/vertical)[:, None]*(k2-1)
        answer[:, :, 1, 1] = ratio[:, None]*k2
        return answer

    def evaluate(self, parameters):
        parameters = np.asarray(parameters)
        if parameters.shape != (4,):
            raise ValueError("Consume all three original controls and the new odd theta control")
        nodes = self.base+np.einsum("mjk,k->mj", self.controls[:, :, :3], parameters[:3])
        middle = self.base_mid+np.einsum("mjk,k->mj", self.controls_mid[:, :, :3], parameters[:3])
        if parameters[3] != 0:
            nodes = nodes+parameters[3]*self.controls[:, :, 3]
            middle = middle+parameters[3]*self.controls_mid[:, :, 3]
        real = np.isrealobj(parameters)
        if real and (np.any(~np.isfinite(nodes)) or np.any(~np.isfinite(middle))
                or np.min(nodes[:, 0]) <= 0 or np.min(middle[:, 0]) <= 0
                or np.max(abs(nodes[:, 1])) >= 1 or np.max(abs(middle[:, 1])) >= 1):
            raise FloatingPointError("Original node/mid scalar domain failed; no interval claim is made by this test")
        q, qm = nodes[:, 1]/nodes[:, 0], middle[:, 1]/middle[:, 0]
        h = self.h
        left = -1-h*(q[:-1]+2*qm)/6-h*h*qm*q[:-1]/12
        right = 1-h*(q[1:]+2*qm)/6+h*h*qm*q[1:]/12
        if np.any(right == 0) or np.any(~np.isfinite(right)):
            raise FloatingPointError("The original circle radius cell cannot be eliminated")
        radius = np.empty(len(self.x), dtype=np.result_type(parameters, float))
        radius[0] = 1.
        for j in range(len(h)):
            radius[j+1] = -left[j]*radius[j]/right[j]
        radius_mid = .5*(radius[:-1]+radius[1:])-h*(q[1:]*radius[1:]-q[:-1]*radius[:-1])/8
        speed, speed_mid = q*radius, qm*radius_mid
        margin, margin_mid = 1-speed*speed, 1-speed_mid*speed_mid
        if real and (np.any(~np.isfinite(radius)) or np.any(~np.isfinite(radius_mid))
                or np.min(radius) <= 0 or np.min(radius_mid) <= 0
                or np.min(margin) <= 0 or np.min(margin_mid) <= 0):
            raise FloatingPointError("The actual source circle left R>0 or 1-(ap*R/a)^2>0")
        vertical, vertical_mid = np.sqrt(margin), np.sqrt(margin_mid)
        height = np.r_[0., np.cumsum(h*(vertical[:-1]+vertical[1:]+4*vertical_mid)/6)]
        B = self.matrix(q, radius, speed, vertical)
        Bm = self.matrix(qm, radius_mid, speed_mid, vertical_mid)
        identity = np.eye(2)
        hh = h[:, None, None, None]
        L = -identity-hh*(B[:-1]+2*Bm)/6-hh*hh*(Bm@B[:-1])/12
        R = identity-hh*(B[1:]+2*Bm)/6+hh*hh*(Bm@B[1:])/12
        modes = np.zeros((len(self.x), 3, 2), dtype=radius.dtype)
        modes[0, :, 0] = 1.
        for j in range(len(h)):
            rhs = np.einsum("kij,kj->ki", L[j], modes[j])
            modes[j+1] = np.linalg.solve(R[j], -rhs[..., None])[..., 0]
        velocity = np.einsum("mkij,mkj->mki", B, modes)
        if np.any(~np.isfinite(modes)) or np.any(~np.isfinite(velocity)):
            raise FloatingPointError("The low-mode original transfer is nonfinite; use a two-end linear BVP instead")
        native = np.zeros(self.M, dtype=radius.dtype)
        native[:3] = self.eh*self.target*modes[-1, :, 1]
        full = -self.gamma*(self.J@native)
        full[:3] += self.target*velocity[-1, :, 1]
        unit_diagonal = velocity[-1, :, 1]-self.gamma*self.eh*np.diag(self.J)[:3]*modes[-1, :, 1]
        return dict(parameters=parameters, scalar_nodes=nodes, scalar_middle=middle,
            radius=radius, radius_mid=radius_mid, radius_rhs=speed,
            height=height, height_rhs=vertical, ratio=q, ratio_mid=qm,
            vertical_mid=vertical_mid, margin=margin, margin_mid=margin_mid,
            modes=modes, velocity=velocity, L=L, R=R, B=B, Bmid=Bm,
            radius_left=left, radius_right=right, full_right=full,
            native_first_order_height=native, low_right=full[:3],
            unit_diagonal_defect=unit_diagonal,
            equation=(unit_diagonal if self.exactly_diagonal else full[:3]))

    def jacobian(self, parameters):
        step = 1e-25
        columns = []
        for j in range(4):
            p = np.asarray(parameters, complex)
            p[j] += 1j*step
            columns.append(self.evaluate(p)["equation"].imag/step)
        return np.stack(columns, axis=1)

    def description(self, state):
        residual = (np.einsum("mkij,mkj->mki", state["L"], state["modes"][:-1])
            + np.einsum("mkij,mkj->mki", state["R"], state["modes"][1:]))
        conditions = np.linalg.cond(state["R"])
        J = self.jacobian(state["parameters"])
        singular = np.linalg.svd(J, compute_uv=False)
        levels = []
        for step in (2e-5, 1e-5, 5e-6):
            errors = []
            valid = True
            for j in range(4):
                d = np.zeros(4); d[j] = step
                try:
                    numerical = (self.evaluate(state["parameters"]+d)["equation"]
                        - self.evaluate(state["parameters"]-d)["equation"])/(2*step)
                    errors.append(float(np.max(abs(numerical-J[:, j])))/max(1., float(np.max(abs(J[:, j])))))
                except FloatingPointError:
                    valid = False
                    break
            levels.append(dict(step=step, valid=valid, maximum_relative_error=max(errors) if valid else None,
                relative_errors_by_parameter=errors, parameter_order=['p1','p2','p3','theta'],
                all_four_columns_checked=bool(valid and len(errors)==4)))
        return dict(parameters=state["parameters"].tolist(),
            full_first_order_native_height=state["native_first_order_height"].tolist(),
            complete_first_order_right_residual=state["full_right"].tolist(),
            unit_diagonal_defects=state["unit_diagonal_defect"].tolist(),
            low_equations_used=state["equation"].tolist(),
            low_equations_definition=("unit d_j; actual full J measured exactly diagonal" if self.exactly_diagonal
                else "full three low rows with actual off-diagonal J; free high-core Schur elimination unresolved"),
            source_target_first_three=self.target.tolist(), target_zero_indices=np.flatnonzero(self.target == 0).tolist(),
            three_unit_resonances_are_necessary_for_these_straight_targets=bool(
                self.exactly_diagonal and np.all(self.target != 0)),
            zero_tail_slope_J=dict(shape=list(self.J.shape),
                maximum_absolute_offdiagonal=float(np.max(abs(self.offdiagonal))),
                nonzero_offdiagonal_entries=int(np.count_nonzero(self.offdiagonal)),
                all_entries_consumed=True, exactly_diagonal_as_recorded=self.exactly_diagonal,
                ready_linear_graph_used=False),
            high_right_leak_max=float(np.max(abs(state["full_right"][3:]), initial=0)),
            high_free_core_Schur_elimination_computed=False,
            high_mode_nonresonance_proved=False,
            scalar_node_and_mid_minimum_radius=float(min(np.min(state["scalar_nodes"][:, 0]),
                np.min(state["scalar_middle"][:, 0]))),
            source_circle_node_and_mid_minimum_radius=float(min(state["radius"].min(), state["radius_mid"].min())),
            source_circle_node_and_mid_minimum_beta2=float(min(state["margin"].min(), state["margin_mid"].min())),
            actual_circle_R_minus_supplied_a_node_max=float(np.max(abs(state["radius"]-state["scalar_nodes"][:, 0]))),
            radius_cell_denominator_minimum_absolute=float(np.min(abs(state["radius_right"]))),
            low_two_by_two_right_condition_max_by_mode=conditions.max(axis=0).tolist(),
            low_mode_trajectory_max_by_mode=np.max(abs(state["modes"]), axis=(0, 2)).tolist(),
            low_original_collocation_tangent_residual_max=float(np.max(abs(residual))),
            three_by_four_parameter_jacobian=J.tolist(), singular_values=singular.tolist(),
            parameter_order=['p1','p2','p3','theta'], response_shape=[3,4],
            first_three_column_singular_values=np.linalg.svd(J[:, :3], compute_uv=False).tolist(),
            fourth_column_full_chain_response=J[:, 3].tolist(),
            four_parameter_columns_include_circle_radius_and_all_low_mode_transfers=True,
            added_function_independence_does_not_assert_response_rank=True,
            new_g_family_not_a_relabelled_old_fixed_metric=True,
            numerical_parameter_condition=float(singular[0]/singular[-1]) if singular[-1] else None,
            numerical_singular_values_are_not_a_transversality_proof=True,
            independent_real_parameter_difference_checks=levels,
            scalar_and_circle_queries_are_not_whole_interval_bounds=True)


def complete_reference_check(model, state, profile, flow, boundary, output, source, source_sha):
    """Fresh original FFT/node/mid/RMS checks at the actual new g, theta fixed.

    The original boundary is square only for k=K=3 with M=T=112.  We do not
    change K, discard a tail row or insert a fourth boundary condition.
    Holding the actual theta constant leaves the identical mathematical g
    and physical circle.  Floating scalar summation paths are read back,
    not assumed to be byte-identical to the separate collocation recurrence.
    """
    full_parameters = np.asarray(state["parameters"], float).copy()
    view = ThetaFrozenProfile(profile, full_parameters[3])
    old_boundary = boundary
    flow = AugmentedFlow(flow.q, view, flow.workers)
    flow.q.profile = view.profile
    boundary = PhysicalTestBoundary(view, np.zeros(3), flow.point_rhs, flow.point_jacobian,
        old_boundary.tail_map, height_sign=old_boundary.eh, radial_sign=old_boundary.er,
        angular=old_boundary.trace.N, physical_angles=old_boundary.physical_angles)
    state = dict(state, parameters=full_parameters[:3])
    physical_jets = flow.scalar_jets(model.x, np.repeat(full_parameters[:3, None], len(model.x), axis=1))
    same_scalar_readback = dict(
        full_four_parameters=full_parameters.tolist(), actual_frozen_theta=float(full_parameters[3]),
        square_check_active_parameter_count=3, original_fixed_core_target_count=3,
        original_tail_and_field_modes=flow.M,
        mathematical_new_scalar_function_identical=True,
        binary64_summation_paths_claimed_identical=False,
        actual_scalar_node_value_ap_max_difference=float(np.max(abs(physical_jets[:, :2]-state["scalar_nodes"]))),
        scalar_path_comparison_is_not_an_acceptance_gate=True)
    boundary.target = np.zeros(3)
    y = np.zeros((len(model.x), flow.dimension))
    y[:, 0] = state["radius"]
    y[:, boundary.iz] = state["height"]
    y[:, flow.parameter_slice] = state["parameters"]
    problem = CompleteResidual(model.x, flow, boundary)
    actual = problem.evaluate(problem.chart.pack(y), require_rms=True)
    if not actual["finite"]:
        write(output/"circle-original-domain.json", actual["report"])
        return dict(original_full_reference_finite=False, actual_domain=actual["report"],
                    frozen_theta_square_check=same_scalar_readback)
    derivative_checks = []
    for node in sorted(set((0, len(model.x)//2, len(model.x)-1))):
        R, q = state["radius"][node], state["ratio"][node]
        W = state["height_rhs"][node]
        for j, k in enumerate(model.frequency):
            U, H = state["modes"][node, j]
            tangent = ((1-k*k)*R-U)/k
            direction = np.zeros(flow.n)
            direction[j+1] = U
            direction[flow.M+1+j] = tangent
            direction[boundary.iz+j+1] = H
            expected = np.zeros(flow.n)
            expected[j+1], expected[boundary.iz+j+1] = state["velocity"][node, j]
            expected[flow.M+1+j] = q*(k*U+tangent)+k*W*H/R
            direct = flow.point_rhs(model.x[node], y[node, :flow.n].astype(complex)
                + 1j*1e-25*direction, state["parameters"]).imag/1e-25
            derivative_checks.append(dict(node=node, station=float(model.x[node]), mode=j+1,
                actual_full_FFT_direction_relative_error=float(np.max(abs(direct-expected)))/max(1., float(np.max(abs(expected)))),
                all_physical_rows_compared=True))
    specification = scalar_spec(profile, source["complete_scalar_profile"]["complete_original_port"],
        full_parameters, EXPECTED["accepted"])
    reference = dict(schema=SCHEMA, scope=__doc__, M=flow.M, N=flow.q.N,
        mesh=model.x.tolist(), states=actual["y"].tolist(), rhs=actual["f"].tolist(),
        complete_scalar_profile=specification, field_representation=field_spec(flow.M, flow.q.N),
        frozen_theta_square_check=same_scalar_readback, scalar_family_sha256=canonical_sha(specification),
        fixed_core_targets=[0., 0., 0.], original_large_core_targets_retained=False,
        source_prepared_sha256=source_sha, full_native_tail_at_nonzero_height_computed=False,
        success=False, new_coupled_finite_acceptance=False, complete_closed_surface=False,
        actual_original_residual_and_domain=actual["report"],
        original_full_FFT_tangent_checks=derivative_checks,
        low_three_unit_modes_UH=state["modes"].tolist(),
        low_three_unit_modes_rhs_UH=state["velocity"].tolist())
    write(output/"circle-reference.json.gz", reference)
    return dict(original_full_reference_finite=True, actual_domain=actual["report"],
        frozen_theta_square_check=same_scalar_readback, scalar_family_sha256=canonical_sha(specification),
        original_full_FFT_tangent_checks=derivative_checks,
        reference_file="circle-reference.json.gz", reference_sha256=original.sha(output/"circle-reference.json.gz"),
        reference_is_not_a_nonzero_parent=True)


def observed_model_class(trace, baseline):
    class ObservedCircleReference(CircleReference):
        def evaluate(self, parameters):
            values = np.asarray(parameters)
            real = bool(np.isrealobj(values))
            trace.counts['evaluation_attempts'] += 1
            trace.counts['real_evaluation_attempts' if real else 'complex_evaluation_attempts'] += 1
            index = trace.counts['evaluation_attempts']
            point = (dict(parameters=values.tolist()) if real else
                     dict(parameters_real=values.real.tolist(), parameters_imag=values.imag.tolist()))
            started = time.monotonic()
            try:
                answer = super().evaluate(parameters)
            except Exception as error:
                trace.counts['evaluation_exceptions'] += 1
                trace.emit(dict(kind='four_control_evaluate_exception', evaluation_index=index,
                    real_parameters=real, **point, exception=repr(error),
                    original_exception_class=type(error).__name__, seconds=time.monotonic()-started))
                raise
            trace.counts['evaluation_returns'] += 1
            if real:
                try:
                    payload = baseline.state_record(np, answer)
                except Exception as error:
                    # Observation must not change an original evaluate return.
                    payload = dict(observer_error=repr(error), original_evaluate_return_preserved=True)
                    trace.observer_errors.append(dict(evaluation_index=index, exception=repr(error)))
            else:
                payload = dict(equation_real=answer['equation'].real.tolist(),
                    equation_imag=answer['equation'].imag.tolist(),
                    original_complex_step_path=True,
                    original_real_domain_guard_is_not_applied_to_complex_probe=True)
            trace.emit(dict(kind='four_control_evaluate_return', evaluation_index=index,
                real_parameters=real, **point, returned=payload, seconds=time.monotonic()-started))
            return answer

        def jacobian(self, parameters):
            trace.counts['jacobian_attempts'] += 1
            index = trace.counts['jacobian_attempts']
            started = time.monotonic()
            try:
                answer = super().jacobian(parameters)
            except Exception as error:
                trace.emit(dict(kind='four_control_jacobian_exception', jacobian_index=index,
                    parameters=np.asarray(parameters).tolist(), exception=repr(error),
                    seconds=time.monotonic()-started))
                raise
            trace.counts['jacobian_returns'] += 1
            trace.emit(dict(kind='four_control_jacobian_return', jacobian_index=index,
                parameters=np.asarray(parameters).tolist(), current_full_three_by_four_jacobian=answer.tolist(),
                original_complex_step=1e-25, seconds=time.monotonic()-started))
            return answer

        def description(self, state):
            trace.counts['description_attempts'] += 1
            return super().description(state)
    return ObservedCircleReference


def zero_theta_reduction_readback(model, parameters, current_state=None, *, trace, baseline):
    """Read back theta=0 against the frozen three-control recurrence, not a gate."""
    p = np.asarray(parameters, float)
    original_model = baseline.observed_model_class(base, trace)(model.profile.original_three, model.x,
        model.J, model.target, model.eh, model.gamma)
    original_state = original_model.evaluate(p[:3])
    zero = np.r_[p[:3], 0.]
    new_state = current_state if p[3] == 0 and current_state is not None else model.evaluate(zero)
    rows = []
    for name, old in original_state.items():
        if name == 'parameters':
            continue
        a, b = np.ascontiguousarray(old), np.ascontiguousarray(new_state[name])
        rows.append(dict(array=name, shape=list(a.shape), dtype=str(a.dtype), order='C', bytes=a.nbytes,
            old_sha256=hashlib.sha256(a.tobytes()).hexdigest(),
            new_sha256=hashlib.sha256(b.tobytes()).hexdigest(),
            byte_identical=a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()))
    return dict(theta=0., original_three_parameters=p[:3].tolist(), arrays=rows,
        all_recorded_arrays_byte_identical=all(row['byte_identical'] for row in rows),
        exact_real_formula_reduces_to_original_three_control_family=True,
        comparison_reference_schema=base.SCHEMA, comparison_reference_evaluate_calls=1,
        original_reference_evaluation_included_in_call_trace=True,
        numerical_byte_identity_is_an_actual_readback_not_a_source_claim=True,
        comparison_is_not_a_candidate_or_final_acceptance_gate=True,
        no_original_parent_status_J_or_merit_reused=True)
