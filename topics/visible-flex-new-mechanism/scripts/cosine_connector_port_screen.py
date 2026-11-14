#!/usr/bin/env python3
"""Continuous necessary port screens for frozen cosine or elliptic flat cores.

The generic interval interface separates necessary OUTER cap-height intervals
from SUFFICIENT intervals for the chord inequalities alone.  It also checks
the directional outward-turn condition on entire angular/direction cells.
Actual geometric screens run only in the public repository's Actions.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from decimal import Decimal as D
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path

from folded_reference_geometry import I, PI, DOWN, UP, sincos
from star_core_geometry import square, clipped, unit_enclosures
from space_star_lift_design import rational_interval


def exact(value):
    return Q.from_float(value) if isinstance(value, float) else Q(value)


def ii(value):
    return rational_interval(exact(value))


def dot2(a, b):
    return a[0]*b[0]+a[1]*b[1]


def sqrt_nonnegative(value):
    return I(max(D(0), value.lo), max(D(0), value.hi)).sqrt()


def meet(left, right):
    lo, hi = max(left.lo, right.lo), min(left.hi, right.hi)
    if lo > hi:
        raise ValueError('inconsistent continuous intervals for the same exact quantity')
    return I(lo, hi)


@dataclass
class PortCell:
    side: int
    index: int
    position: list
    outward_velocity: list
    theta: I


class PortBoxes:
    def __init__(self, cells, support, identity_sha256, diameter_lower, metadata):
        self.cells = cells
        self.support = support
        self.identity_sha256 = identity_sha256
        self.diameter_lower = diameter_lower
        self.metadata = metadata


def ellipse_port_boxes(core, angular_nodes=512, progress=None):
    """Interval provider only; the physical ellipse evaluator belongs elsewhere.

    Consume EllipticCylinderPort's exact radii/width and physical identity.
    Both outward ports are included; the core itself is centered at z=0.
    """
    n = int(angular_nodes)
    if n < 16:
        raise ValueError('at least sixteen angular cells required')
    A, B, w = ii(core.A_exact), ii(core.B_exact), ii(core.width_exact)
    if core.A_exact < core.B_exact or B.lo <= 0 or w.lo <= 0:
        raise ValueError('need major>=minor>0 and positive width')
    vertices, angular_cells = unit_enclosures(n)
    step = 2*PI/n
    speeds = [sqrt_nonnegative(square(A)*square(s)+square(B)*square(c)) for s, c in vertices]
    increments = []
    for j, (s, c) in enumerate(angular_cells):
        speed = sqrt_nonnegative(square(A)*square(s)+square(B)*square(c))
        if speed.lo <= 0:
            raise ValueError('ellipse speed interval positivity unresolved')
        difference = square(A)-square(B)
        Qp = 2*difference*s*c
        Qpp = 2*difference*(square(c)-square(s))
        speed_second = Qpp/(2*speed)-square(Qp)/(4*speed**3)
        error = (I(speed_second.abs_upper())*step**3/12).hi
        trap = step*(speeds[j]+speeds[(j+1) % n])/2
        increment = meet(trap+I(-error, error), step*speed)
        if increment.lo <= 0:
            raise ValueError('ellipse arclength increment positivity unresolved')
        increments.append(increment)
    prefix = [I(0)]
    for increment in increments:
        prefix.append(prefix[-1]+increment)
    period = prefix[-1]
    suffix = [I(0)]*(n+1)
    for j in range(n-1, -1, -1):
        suffix[j] = suffix[j+1]+increments[j]
    prefix = [meet(value, period-suffix[j]) for j, value in enumerate(prefix)]
    prefix[0], prefix[-1] = I(0), period
    cells = []
    for j, (s, c) in enumerate(angular_cells):
        angle = 2*PI*I(prefix[j].lo, prefix[j+1].hi)/period
        for side in [-1, 1]:
            cells.append(PortCell(side, j, [A*c, B*s, side*w],
                                  [I(0), I(0), I(side)], angle))
    if progress:
        progress({'stage': 'ellipse_continuous_port_boxes', 'angular_cells': n})

    def support(direction):
        return sqrt_nonnegative(square(A)*square(direction[0])+square(B)*square(direction[1]))

    return PortBoxes(cells, support, core.identity_sha256, 2*A,
                     {'provider': 'exact-ellipse-interval-port-v1', 'angular_cells': n,
                      'physical_identity': core.identity, 'period_enclosure': period.json(),
                      'material_angle_is_interval_arclength_not_float_inverse': True,
                      'boundary_projection_lies_in_domain': True,
                      'outward_horizontal_velocity_identically_zero': True,
                      'fold': 2})


def cosine_port_boxes(report, angular_nodes=1024, progress=None):
    # Optional branch only. The ellipse lane does not depend on an unpublished
    # general cosine-ribbon embedding engine or its verification adapters.
    from cosine_core_embedding import FrozenRibbon, Cell, norm, rotate
    from space_star_flat_core import cross
    from space_star_cosine_verify import moving_frame_jets
    from cosine_rectifying_core import exact_rational
    ribbon = FrozenRibbon(report, angular_nodes, progress=progress)
    identity = ribbon.identity
    a, b = ii(identity['a']), ii(identity['b'])
    heights = [ii(exact_rational(x)) for x in identity['height_coefficients']]
    offset = ii(exact_rational(identity['height_offset']))
    _, angular_cells = unit_enclosures(angular_nodes)
    leaves = sorted((node for node in ribbon.nodes if node.left is None), key=lambda node: node.begin)
    cells = []
    for node, (ss, cc) in zip(leaves, angular_cells):
        _, v1, v2, _, _ = moving_frame_jets(ss, cc, a, b, heights, offset)
        speed = norm(v1); cross12 = cross(v1, v2)
        omega = meet(norm(cross12), I((ribbon.kappa_lower*I(speed.lo)**3).lo,
                                      (ribbon.curvature*I(speed.hi)**3).hi))
        if omega.lo <= 0:
            raise ValueError('continuous binormal positivity unresolved')
        binormal = rotate([clipped(component/omega) for component in cross12], ss, cc)
        for side in [-1, 1]:
            position, _, material, _ = ribbon.bounds(Cell(node.index, side*ribbon.width, side*ribbon.width))
            theta = 2*PI*material/ribbon.period
            cells.append(PortCell(side, node.begin, position,
                                  [side*x for x in binormal], theta))

    def support(direction):
        values = [dot2(direction, node.position[:2]) for node in leaves]
        return I(max(value.lo for value in values), max(value.hi for value in values))

    # Two C3-related tip points have the same height and planar separation
    # sqrt(3)*(1+a+b), even if the tip is not the farthest point of the curve.
    diameter_lower = I(3).sqrt()*(1+a+b)
    return PortBoxes(cells, support, ribbon.digest, diameter_lower,
                     {'provider': 'frozen-cosine-interval-port-v1', 'angular_cells': angular_nodes,
                      'physical_identity': identity, 'period_enclosure': ribbon.period.json(),
                      'material_angle_is_interval_arclength_not_float_inverse': True,
                      'boundary_projection_lies_in_domain': False,
                      'outward_horizontal_velocity_identically_zero': False,
                      'fold': 3})


def cap_chord_height_screen(boxes, length, cut_radius, phase='0', cap_height_interval=None):
    """All-angle chord constraints; OUTER and INNER height bounds stay distinct."""
    L, radius, phase_i = ii(length), ii(cut_radius), ii(phase)
    if L.lo <= 0 or radius.lo <= 0:
        raise ValueError('positive physical length and circle radius required')
    L2 = square(L)
    rows = []
    for side in [-1, 1]:
        outer_lo, outer_hi = D('-Infinity'), D('Infinity')
        inner_lo, inner_hi = D('-Infinity'), D('Infinity')
        inner_resolved = True; strict_horizontal = []
        maximum_lower, maximum_upper = D(0), D(0)
        for cell in (item for item in boxes.cells if item.side == side):
            sn, cs = sincos(cell.theta+phase_i)
            dx, dy = cell.position[0]-radius*cs, cell.position[1]-radius*sn
            distance2 = square(dx)+square(dy)
            maximum_lower = max(maximum_lower, distance2.lo)
            maximum_upper = max(maximum_upper, distance2.hi)
            if distance2.lo > L2.hi:
                strict_horizontal.append(cell.index)
                inner_resolved = False
                continue
            qmax = sqrt_nonnegative(I(max(D(0), UP.subtract(L2.hi, distance2.lo)))).hi
            z = cell.position[2]
            lower = (I(z.lo)-I(qmax)).lo
            upper = (I(z.hi)+I(qmax)).hi
            outer_lo, outer_hi = max(outer_lo, lower), min(outer_hi, upper)
            if distance2.hi > L2.lo:
                inner_resolved = False
            else:
                qmin = max(D(0), sqrt_nonnegative(I(max(D(0), DOWN.subtract(L2.lo, distance2.hi)))).lo)
                inner_lo = max(inner_lo, (I(z.hi)-I(qmin)).hi)
                inner_hi = min(inner_hi, (I(z.lo)+I(qmin)).lo)
        if cap_height_interval is not None:
            allowed = cap_height_interval if isinstance(cap_height_interval, I) else I(*cap_height_interval)
            outer_lo, outer_hi = max(outer_lo, allowed.lo), min(outer_hi, allowed.hi)
            inner_lo, inner_hi = max(inner_lo, allowed.lo), min(inner_hi, allowed.hi)
        excluded = bool(strict_horizontal or outer_lo > outer_hi)
        inner_nonempty = inner_resolved and inner_lo <= inner_hi and not excluded
        rows.append({'side': side, 'strict_horizontal_failure_cells': strict_horizontal[:8],
                     'strict_horizontal_failure_cell_count': len(strict_horizontal),
                     'necessary_outer_height_interval': {'lower': str(outer_lo), 'upper': str(outer_hi)},
                     'necessary_outer_interval_empty': bool(outer_lo > outer_hi),
                     'fixed_circle_port_and_length_excluded': excluded,
                     'sufficient_height_interval_for_all_chord_inequalities':
                         {'lower': str(inner_lo), 'upper': str(inner_hi)} if inner_nonempty else None,
                     'sufficient_interval_unresolved_is_not_exclusion': not inner_nonempty and not excluded,
                     'maximum_horizontal_chord_squared_enclosure':
                         {'lower': str(maximum_lower), 'upper': str(maximum_upper)},
                     'continuous_all_material_angles_covered': True,
                     'a_surface_connector_has_not_been_constructed': True})
    return {'length': str(exact(length)), 'cut_radius': str(exact(cut_radius)),
            'tail_material_phase': str(exact(phase)), 'sides': rows,
            'any_side_strictly_excluded': any(row['fixed_circle_port_and_length_excluded'] for row in rows)}


def positive_turn_displacement(component):
    """g(b_+) = 1-sqrt(1-b_+^2), with 0<=b_+<=1 and directed bounds."""
    lo = min(D(1), max(D(0), component.lo))
    hi = min(D(1), max(D(0), component.hi))
    root_lo = sqrt_nonnegative(1-square(I(lo)))
    root_hi = sqrt_nonnegative(1-square(I(hi)))
    return I(max(D(0), (1-root_lo).lo), min(D(1), (1-root_hi).hi))


def all_direction_turn_screen(boxes, tau, padding='0', direction_cells=24, progress=None):
    """R25 generalized to all boundary points and all direction cells.

    For e.V>0 a unit-speed material geodesic must move outward at least
    tau*(1-sqrt(1-(e.V)^2)) before becoming non-outward. For e.V<=0 only
    the original projection envelope is required. The envelope is K+B_p.
    This is a necessary screen for an EXACT isometric target. A small C0
    metric residual does not by itself make numerical radial lines geodesic.
    """
    reach, pad = ii(tau), ii(padding)
    if reach.lo <= 0 or pad.lo < 0:
        raise ValueError('positive assumed reach and nonnegative projection padding required')
    if (boxes.metadata.get('boundary_projection_lies_in_domain') and
            boxes.metadata.get('outward_horizontal_velocity_identically_zero')):
        return {'continuous_all_material_angles_and_directions_passed': True,
                'proof': 'boundary lies in K and every outward velocity is vertical; g((e.V)_+)=0 identically',
                'strict_violation': False, 'checked_direction_cells': 0,
                'assumes_exact_unit_speed_material_geodesics_of_target_metric': True,
                'approximate_R28_material_curves_are_not_automatically_geodesics': True,
                'projection_envelope_is_still_a_required_future_connector_assumption': True}
    _, directions = unit_enclosures(int(direction_cells))
    failures = []; unresolved = 0; checked = 0; worst_upper = D('-Infinity')
    for j, (ss, cc) in enumerate(directions):
        direction = [cc, ss]
        support = boxes.support(direction)
        for cell in boxes.cells:
            b = clipped(dot2(direction, cell.outward_velocity[:2]))
            gap = dot2(direction, cell.position[:2])+reach*positive_turn_displacement(b)-support-pad
            worst_upper = max(worst_upper, gap.hi); checked += 1
            if gap.lo > 0:
                failures.append({'side': cell.side, 'angular_cell': cell.index,
                                 'direction_cell': j, 'strict_excess_lower': str(gap.lo)})
            elif gap.hi > 0:
                unresolved += 1
        if progress:
            progress({'stage': 'all_direction_turn_screen', 'completed_direction_cells': j+1,
                      'direction_cells': len(directions), 'strict_failures_so_far': len(failures)})
    return {'assumed_reach': str(exact(tau)), 'projection_padding': str(exact(padding)),
            'continuous_all_material_angles_and_directions_passed': not failures and unresolved == 0,
            'strict_violation': bool(failures), 'strict_violation_count': len(failures),
            'strict_witnesses': failures[:12], 'unresolved_cell_pairs': unresolved,
            'checked_cell_pairs': checked, 'checked_direction_cells': len(directions),
            'maximum_excess_upper': str(worst_upper),
            'direction_cells_cover_the_whole_angle_circle': True,
            'assumes_exact_unit_speed_material_geodesics_of_target_metric': True,
            'approximate_R28_material_curves_are_not_automatically_geodesics': True,
            'projection_envelope_is_still_a_required_future_connector_assumption': True,
            'unresolved_interval_is_not_strict_failure': True}


def developer_check():
    # Use the new ellipse interface with a circle, not any research candidate.
    from ellipse_frame_port import EllipticCylinderPort
    core = EllipticCylinderPort('1', '1', '1/10')
    boxes = ellipse_port_boxes(core, 64)
    passing = cap_chord_height_screen(boxes, '1/2', '4/5')
    failing = cap_chord_height_screen(boxes, '1/20', '4/5')
    support = all_direction_turn_screen(boxes, '1/20', '0', 16)
    g0, g1 = positive_turn_displacement(I(-1, 0)), positive_turn_displacement(I(1))
    passed = (not passing['any_side_strictly_excluded']
              and all(row['sufficient_height_interval_for_all_chord_inequalities'] is not None
                      for row in passing['sides'])
              and failing['any_side_strictly_excluded']
              and support['continuous_all_material_angles_and_directions_passed']
              and g0.lo == 0 and g0.hi < D('1e-40') and g1.lo > D('.999999999999'))
    return {'schema': 'continuous-port-screen-development-v1', 'passed': bool(passed),
            'artificial_circle_only': True, 'research_candidate_evaluated': False,
            'passing_chord_case': passing, 'failing_chord_case': failing,
            'exact_vertical_support_case': support}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--cosine-report', type=Path)
    parser.add_argument('--ellipse-major', default='1'); parser.add_argument('--ellipse-minor', default='.28')
    parser.add_argument('--half-width', default='.02')
    parser.add_argument('--angular-nodes', type=int, default=1024)
    parser.add_argument('--direction-cells', type=int, default=24)
    parser.add_argument('--length', default='.9'); parser.add_argument('--cut-radius', default='.22')
    parser.add_argument('--phase', default='0'); parser.add_argument('--height-max')
    parser.add_argument('--reach-ratio', default='.03'); parser.add_argument('--planned-tau')
    parser.add_argument('--padding', default='0'); parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.check_only:
        report = developer_check()
    else:
        if (os.environ.get('GITHUB_ACTIONS') != 'true' or
                os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
            parser.error('real necessary screens run only in the public repository Actions')
        progress = lambda row: print(json.dumps(row), flush=True)
        if args.cosine_report:
            repository = Path(__file__).resolve().parents[3]
            allowed = [repository/'topics'/'visible-flex-new-mechanism'/'notes']
            if os.environ.get('RUNNER_TEMP'):
                allowed.append(Path(os.environ['RUNNER_TEMP']))
            if not any(args.cosine_report.resolve().is_relative_to(root.resolve()) for root in allowed):
                parser.error('cosine report must be a public topic note or this Actions run temporary output')
            raw = args.cosine_report.read_bytes()
            boxes = cosine_port_boxes(json.loads(raw), args.angular_nodes, progress)
            input_source = {'path': str(args.cosine_report), 'sha256': hashlib.sha256(raw).hexdigest()}
        else:
            from ellipse_frame_port import EllipticCylinderPort
            core = EllipticCylinderPort(args.ellipse_major, args.ellipse_minor, args.half_width)
            boxes = ellipse_port_boxes(core, args.angular_nodes, progress)
            input_source = {'physical_identity': core.identity}
        necessary_tau = ii(args.reach_ratio)*I(boxes.diameter_lower.lo)
        tau = args.planned_tau if args.planned_tau is not None else str(necessary_tau.lo)
        height = None if args.height_max is None else I(ii(args.height_max).hi.copy_negate(), ii(args.height_max).hi)
        chord = cap_chord_height_screen(boxes, args.length, args.cut_radius, args.phase, height)
        turn = all_direction_turn_screen(boxes, tau, args.padding, args.direction_cells, progress)
        report = {'schema': 'continuous-core-port-necessary-screen-v1',
                  'physical_identity_sha256': boxes.identity_sha256, 'input_source': input_source,
                  'provider': boxes.metadata, 'diameter_lower_enclosure': boxes.diameter_lower.json(),
                  'necessary_reach_from_topic_ratio_enclosure': necessary_tau.json(),
                  'support_tau_kind': 'planned-extra-target' if args.planned_tau else 'necessary-from-diameter-lower',
                  'chord_height_screen': chord, 'directional_turn_screen': turn,
                  'planned_tau_failure_is_not_unconditional_topic_exclusion': args.planned_tau is not None,
                  'passing_necessary_screens_does_not_construct_a_connector': True,
                  'complete_surface_embedded': False, 'reach_lower_certified': False, 'task_complete': False}
    report['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'out': str(args.out), 'development_passed': report.get('passed'),
                      'task_complete': False}), flush=True)
    if args.check_only and not report['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
