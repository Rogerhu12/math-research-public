#!/usr/bin/env python3
"""Independent Cartesian and rational checks for the explicit disk theorem.

No author module, candidate checkpoint, integration, mesh, BVP or RK is used.
The proof of reach with a boundary is reviewed in the accompanying full text;
these finite checks do not replace its nearest-point argument.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import sympy as S

TOPIC = Path(__file__).resolve().parent.parent
NOTES = TOPIC / 'notes'
STEM = '2026-11-09-db6f-audit-explicit-three-cylinder-flat-branch'
EXPECTED = {
    'notes/' + STEM + '.md': 'ec4c52b1abafb44b300ae20956bc1308c9b522b62a9cff1a70208a65326117ee',
    'notes/' + STEM + '.json': '4f69b9e47ec6cbe6e1eba678526420376519c99ef72839420b9da86613826807',
    'scripts/db6f-audit-explicit-three-cylinder-flat-branch.py':
        '0288ff3d7e6d1c0fddfb68d910e5ecd073caf8448f2b0dd8433a063386234c32',
}


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def exact(value):
    value = Q(value)
    return {'numerator': value.numerator, 'denominator': value.denominator}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists(), 'Fresh report path required'
    bindings = []
    for relative, expected in EXPECTED.items():
        item = identity(TOPIC / relative)
        assert item['sha256'] == expected, relative
        bindings.append(item)
    author = json.loads((NOTES / (STEM + '.json')).read_text())
    for row in author['sources']:
        item = identity(TOPIC / row['path'])
        assert item['sha256'] == row['sha256'] and item['bytes'] == row['bytes']
        bindings.append(item)

    # Work in Cartesian coordinates with two independent unit-circle identities.
    # This is different from the author's meridian/polar implementation.
    c, s, u, v, k = S.symbols('c s u v k', real=True)
    ring = S.groebner([c*c+s*s-1, u*u+v*v-1], c, s, u, v, k)
    jac = S.Matrix([[1+(c-1)*u*u, (c-1)*u*v],
                    [(c-1)*u*v, 1+(c-1)*v*v],
                    [-s*u, -s*v]])
    normal = S.Matrix([-s*u, -s*v, -c])
    n = [u, v]
    zeros = {}

    def zero(name, expression):
        remainder = ring.reduce(S.expand(expression))[1]
        assert remainder == 0, name
        zeros[name] = '0'

    gram = jac.T * jac - S.eye(2)
    for i in range(2):
        for j in range(2):
            zero(f'Cartesian_metric_{i}{j}', gram[i, j])
    zero('inward_normal_unit', normal.dot(normal)-1)
    for i in range(2):
        zero(f'Cartesian_normal_tangent_{i}', normal.dot(jac[:, i]))
        for j in range(2):
            acceleration = k * n[i] * n[j] * normal
            zero(f'Cartesian_second_form_{i}{j}',
                 acceleration.dot(normal)-k*n[i]*n[j])
    second = S.Matrix([[k*u*u, k*u*v], [k*u*v, k*v*v]])
    zero('Cartesian_Gauss_rank_one', second.det())
    zero('Cartesian_shape_trace_k', S.trace(second)-k)

    x, y = S.symbols('x y', real=True)
    curvature = S.Function('curvature')(u*x+v*y)
    tensor = [[curvature*n[i]*n[j] for j in range(2)] for i in range(2)]
    for j in range(2):
        residual = S.diff(tensor[1][j], x)-S.diff(tensor[0][j], y)
        assert S.simplify(residual) == 0
        zeros[f'Cartesian_Codazzi_column_{j}'] = '0'

    # Inverse variable t=ell/(s-a) is >=1.  Its peak is t=2.
    t = S.symbols('t', positive=True)
    shape = t*t*S.exp(1-t)
    assert S.simplify(S.diff(shape, t)-t*(2-t)*S.exp(1-t)) == 0
    assert S.simplify(shape.subs(t, 2)-4/S.E) == 0
    zeros['inverse_variable_curvature_derivative'] = '0'
    zeros['inverse_variable_curvature_peak'] = '0'

    a, length, diameter = Q(579, 1000), Q(421, 1000), Q(2)
    gates = []

    def gt(name, left, right):
        left, right = Q(left), Q(right)
        assert left > right, name
        gates.append({'name': name, 'left': exact(left), 'right': exact(right),
                      'relation': '>', 'passed': True})

    gt('caps_are_disjoint_on_disk', 2*a, 1)
    gt('activity_has_positive_width', 1, a)
    gt('strict_exponential_upper', Q(11, 4), Q(8, 3)+Q(1, 24)/(1-Q(1, 5)))
    gt('cube_gives_exp_minus_one_third', Q(10, 7)**3, Q(11, 4))
    # Lower sums over [1/3,1/2], [1/2,3/4], [3/4,1].
    intervals = [(Q(1, 3), Q(1, 2), Q(16, 121)),
                 (Q(1, 2), Q(3, 4), Q(4, 11)),
                 (Q(3, 4), Q(1), Q(7, 10))]
    lower = length * sum((right-left)*value*Q(5, 6)
                         for left, right, value in intervals)
    gt('Hausdorff_witness_height', lower, Q(1, 10))
    gt('held_ratio_uses_whole_initial_diameter', lower/diameter, Q(1, 20))
    gt('fixed_material_disk_diameter', 2*a, diameter/5)
    reach = Q(1, 4)/(Q(3, 2)/length)
    assert reach == Q(421, 6000)
    gt('boundary_inclusive_reach_radius', reach, Q(3, 100)*diameter)
    gt('boundary_inclusive_reach_ratio', reach/diameter, Q(3, 100))
    # Independent contradiction form of the plane-separation bound:
    # eps<=1/40 and h>1/10 would force |u|^2<1 for a unit plane normal.
    epsilon, height = Q(1, 40), Q(1, 10)
    unit_normal_upper = (epsilon/a)**2 + (epsilon*(2+1/a)/height)**2
    gt('unit_plane_normal_contradiction', 1, unit_normal_upper)
    gt('quotient_distance_ratio_positive', epsilon/diameter, 0)
    weak_height = Q(47, 500)-length/8
    assert weak_height == Q(331, 8000)
    gt('weak_branch_above_original_core_top', weak_height, Q(1, 100))
    gt('flat_ring_has_positive_width', a, Q(577, 1000))
    gt('flat_ring_above_zero', Q(47, 500), 0)

    recorded = author['rational']['held_strict_lower']
    assert lower == Q(recorded['numerator'], recorded['denominator'])
    recorded = author['rational']['reach_strict_lower']
    assert reach == Q(recorded['numerator'], recorded['denominator'])
    proof = (NOTES / (STEM+'.md')).read_text()
    assert proof.count('-sin(') == 1

    unique = {item['path']: item for item in bindings}
    report = {
        'status': 'PASS_INDEPENDENT_CARTESIAN_AND_RATIONAL_DISK_CHECKS',
        'scope': 'Explicit embedded disk with boundary only; no closed surface or G5.',
        'checker': identity(__file__),
        'source_bindings': sorted(unique.values(), key=lambda item: item['path']),
        'Cartesian_and_inverse_variable_identities': zeros,
        'symbolic_identity_count': len(zeros),
        'independent_rational_gates': gates,
        'rational_gate_count': len(gates),
        'same_exact_author_held_and_reach_bounds': True,
        'held_strict_lower': exact(lower),
        'reach_strict_lower': exact(reach),
        'plane_normal_squared_upper_under_false_epsilon_assumption': exact(unit_normal_upper),
        'known_proof_typography_correction': 'Equation (8): insert a backslash before the one bare sin.',
        'author_module_imports': 0,
        'integration_mesh_BVP_tail_RK_calls': 0,
        'main_candidate_data_read': False,
        'global_reach_argument_requires_full_text_review': True,
        'closed_surface_constructed': False,
        'G5_completed': False,
    }
    with args.out.open('x') as output:
        output.write(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'identities': len(zeros),
                      'rational_gates': len(gates), 'output': identity(args.out)}))


if __name__ == '__main__':
    main()
