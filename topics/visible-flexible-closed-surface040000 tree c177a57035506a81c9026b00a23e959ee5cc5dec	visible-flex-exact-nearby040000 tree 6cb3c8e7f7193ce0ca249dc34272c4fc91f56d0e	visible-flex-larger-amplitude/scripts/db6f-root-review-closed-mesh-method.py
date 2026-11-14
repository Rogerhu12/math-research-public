#!/usr/bin/env python3
"""Record root's independent source review; verify the half-angle identity.

This is a proof/source review, not a run on an exported mesh. The polynomial
identity uses exact integer coefficients and no symbolic algebra dependency.
"""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def add(*items):
    result = {}
    for item in items:
        for exponent, coefficient in item.items():
            result[exponent] = result.get(exponent, 0) + coefficient
    return {key: value for key, value in result.items() if value}


def scale(item, coefficient):
    return {key: coefficient*value for key, value in item.items() if coefficient*value}


def mul(a, b):
    result = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            key = tuple(x+y for x, y in zip(ka, kb))
            result[key] = result.get(key, 0)+va*vb
    return {key: value for key, value in result.items() if value}


def half_angle_identity():
    one = {(0, 0, 0): 1}
    x, y, z = ({(1, 0, 0): 1}, {(0, 1, 0): 1}, {(0, 0, 1): 1})
    xx, yy, zz = mul(x, x), mul(y, y), mul(z, z)
    gram = add(one, scale(mul(mul(x, y), z), 2),
               scale(xx, -1), scale(yy, -1), scale(zz, -1))
    total = add(one, x, y, z)
    total2 = mul(total, total)
    denominator = mul(mul(add(one, scale(xx, -1)),
                          add(one, scale(yy, -1))), add(one, scale(zz, -1)))
    # Pairs represent a+i*T*b with T^2 = gram.
    real, imaginary = one, {}
    for factor in (add(y, scale(mul(x, z), -1)),
                   add(z, scale(mul(x, y), -1)),
                   add(x, scale(mul(y, z), -1))):
        real, imaginary = (add(mul(real, factor), scale(mul(gram, imaginary), -1)),
                           add(real, mul(imaginary, factor)))
    re = add(mul(add(total2, gram), real),
             mul(denominator, add(total2, scale(gram, -1))))
    im = add(mul(add(total2, gram), imaginary),
             scale(mul(denominator, total), 2))
    if re or im:
        raise ArithmeticError('Half-angle polynomial identity failed')


def main():
    validator = ROOT/'scripts/db6f-audit-closed-mesh.py'
    proof = ROOT/'notes/2026-11-09-db6f-closed-mesh-radial-validation-proof.md'
    backend = ROOT/'scripts/db6f-audit-continuous-hermite.py'
    ast.parse(validator.read_text())
    half_angle_identity()
    sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    report = dict(
        status='PASS-independent-proof-and-static-implementation-review',
        scope='Conditional radial PL embedding lemma and validator source only; '
              'no actual PLY is run in this review.',
        validator_sha256=sha(validator), proof_sha256=sha(proof),
        interval_backend_sha256=sha(backend), review_script_sha256=sha(Path(__file__)),
        review_checks=dict(
            triangulated_closed_oriented_manifold=True,
            halfedge_rotation_and_connectedness=True,
            positive_face_edge_and_vertex_local_degree=True,
            spherical_area_half_angle_polynomial_identity=True,
            rational_degree_isolation=True, exact_fraction_accumulation=True,
            strict_binary_input_and_size_contract=True),
        actual_mesh_validated_here=False,
        continuous_metric_or_reach_certified_here=False,
        fixed_g_convergence_gate_5_paid=False)
    output = ROOT/'notes/2026-11-09-db6f-root-review-closed-mesh-method.json'
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
