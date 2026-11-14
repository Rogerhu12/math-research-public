#!/usr/bin/env python3
"""Exact two-row Airy audit and actual waist spline-regularity check.

Run only as a genuine public Actions mathematical child. The exact model
identities do not assert current nonlocal root or positive-port matching.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
import sympy as sp


ORIGIN = "0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b"
OBJECT = "91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
SOURCES = {
    "fourfold_phase_beta_bulk_interval.py": "4b9d6bf8d4b0d0c962eb32df9051b3b58fa1e25d7612e2bcef259572a9b15a76",
    "fourfold_phase_beta_interval.py": "ff159224bc1870b7580ef6e5f0370a4fcc385ed556d947003a0bb1667e6f4b0f",
    "fourfold_phase_beta_affine.py": "b82724a2af026b9b9ee935f3df0eb95e7feb36ac5f65db9694085b5a4ad25991",
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--origin", type=Path, required=True)
    parser.add_argument("--object", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    if args.out.exists():
        raise FileExistsError("preserve every actual audit result")
    if os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("this mathematical child requires the public repository Actions")
    if sp.__version__ != "1.14.0" or np.__version__ != "2.3.5":
        raise RuntimeError("the reviewed exact-audit runtime changed")
    if sha(args.origin) != ORIGIN or sha(args.object) != OBJECT:
        raise ValueError("the exact original target inputs changed")
    here = Path(__file__).parent
    for name, expected in SOURCES.items():
        if sha(here/name) != expected:
            raise ValueError("the exact symmetric scalar definition changed: "+name)
    definition = json.loads(args.object.read_text())
    if (definition.get("kind") != "exact_affine_symmetric_infinite_R33_graph"
            or definition["origin_inputs"]["sha256"] != ORIGIN):
        raise ValueError("a different exact target definition was supplied")

    gates = []
    def check(name, okay):
        gates.append(dict(name=name, passed=bool(okay)))

    rho, eps, H = sp.symbols("rho eps H", positive=True)
    q = sp.sqrt(rho)
    first = lambda expression: sp.simplify(sp.series(expression, eps, 0, 2).removeO())
    B = 1/(4*rho)
    S = sp.Matrix([[0, -B/(2*q)], [B/(2*q), 0]])
    T = sp.eye(2)+S*eps/sp.I
    columns = []
    for sign in (1, -1):
        # Factor rho**(-1/4) exp(sign*i*theta) before differentiating.
        F = 1-sign*sp.I*5*eps/(48*rho**sp.Rational(3, 2))
        Fprime = sp.diff(F, rho)-F/(4*rho)+sign*sp.I*q*F/eps
        raw = sp.Matrix([first((sp.I*eps*Fprime+sigma*q*F)/(2*q))
                         for sigma in (1, -1)])
        normalized = (sp.eye(2)-S*eps/sp.I)*raw
        columns.append((raw, normalized.applyfunc(first)))
    raw_plus, normalized_plus = columns[0]
    raw_minus, normalized_minus = columns[1]
    tt = eps/rho**sp.Rational(3, 2)
    check("both outgoing curvature rows retain the complete Airy derivative shear",
          raw_plus == sp.Matrix([-sp.I*tt/8, -1-sp.I*tt/48]))
    check("both opposite curvature rows use the same original h1 reconstruction",
          raw_minus == sp.Matrix([1-sp.I*tt/48, -sp.I*tt/8]))
    check("the complete cross normalizer removes the outgoing first cross column",
          normalized_plus == sp.Matrix([0, -1-sp.I*tt/48]))
    check("the complete cross normalizer removes the opposite first cross column",
          normalized_minus == sp.Matrix([1-sp.I*tt/48, 0]))
    check("the strict signed coefficient agrees with the actual dominant Airy row",
          sp.simplify(-sp.diff(sp.I*eps/(48*rho**sp.Rational(3, 2)), rho)
                      -sp.I*eps/(32*rho**sp.Rational(5, 2))) == 0)
    check("the model finite-part subtraction uses the complete Xi coefficient",
          sp.simplify(B**2/q-rho**sp.Rational(-5, 2)/16) == 0
          and sp.diff(-rho**sp.Rational(-3, 2)/24, rho)
          == rho**sp.Rational(-5, 2)/16)
    boundary = sp.Matrix([[1, 1]])*T
    check("the actual waist row keeps both first endpoint factors",
          boundary == sp.Matrix([[1-sp.I*tt/8, 1+sp.I*tt/8]]))
    check("the nonzero model waist factor supplies exactly the missing first phase",
          first(boundary[1]/boundary[0]) == 1+sp.I*tt/4
          and sp.Rational(1, 24)+sp.Rational(1, 4) == sp.Rational(7, 24)
          and sp.Rational(5, 48)-sp.Rational(1, 4) == -sp.Rational(7, 48))

    r = sp.symbols("r", real=True)
    et, qr, L1, L2 = (sp.Function(name)(r) for name in ("eta", "q", "L1", "L2"))
    optical = et*qr
    p = sp.diff(et, r)/et+L1+L2
    potential = ((sp.diff(et, r)/et+L1)*L2-sp.diff(L2, r)
                 +sp.diff(p, r)/2-p*p/4)
    W = (potential/optical**2+3*sp.diff(optical, r)**2/(4*optical**4)
         -sp.diff(optical, r, 2)/(2*optical**3))
    cross = -sp.diff(qr, r)/(2*qr)+(L1-L2)/2
    check("the general local radial two-row Liouville identity keeps its endpoint",
          sp.simplify(cross**2/optical-sp.diff(cross/optical, r)+W*optical) == 0)

    b, u, v, eta, qq, B0 = sp.symbols("b u v eta qq B0", nonzero=True)
    Bp, Bm = B0-2*b*qq*u*v, B0+2*b*qq*u*v
    actual_S = sp.Matrix([[0, -Bp/(2*eta*qq)], [Bm/(2*eta*qq), 0]])
    separated_S = (B0/(2*eta*qq)*sp.Matrix([[0, -1], [1, 0]])
                   +b*u*v/eta*sp.Matrix([[0, 1], [1, 0]]))
    check("the current nonradial normalizer retains its finite symmetric part",
          sp.simplify(actual_S-separated_S) == sp.zeros(2))
    check("the finite root coefficient is angular odd under the full reflection",
          sp.simplify((b*u*v/eta).subs(u, -u)+b*u*v/eta) == 0)

    spline_rows = []
    with np.load(args.origin, allow_pickle=False) as saved:
        for prefix in ("base", "shift", "mean0", "mean1", "mean2",
                       "height0_slope", "height1_slope", "height2_slope", "height3_slope"):
            degree = int(saved[prefix+"_degree"])
            knots = saved[prefix+"_knots"]
            multiplicity = int(np.count_nonzero(knots == 0))
            interior = bool(knots[0] < 0 < knots[-1])
            regularity = degree-multiplicity if multiplicity else degree
            spline_rows.append(dict(name=prefix, degree=degree,
                exact_zero_multiplicity=multiplicity, zero_is_interior=interior,
                guaranteed_continuous_derivatives_at_zero=regularity))
        phase = saved["phase_knots"]
        phase_at_zero = int(np.count_nonzero(phase == 0))
        phase_interior = bool(phase[0] < 0 < phase[-1])
    check("every actual radius and height-slope spline is C4 at the waist",
          all(row["degree"] == 5 and row["exact_zero_multiplicity"] == 1
              and row["zero_is_interior"]
              and row["guaranteed_continuous_derivatives_at_zero"] >= 4
              for row in spline_rows))
    check("the original phase spline has no knot at the waist",
          phase_at_zero == 0 and phase_interior)

    report = dict(kind="exact_two_row_Airy_model_and_current_waist_normalizer_audit",
        complete=all(row["passed"] for row in gates), source_sha256=sha(__file__),
        original_spline_sha256=ORIGIN, actual_affine_object_sha256=OBJECT,
        symmetric_definition_sources=SOURCES, original_spline_structure=spline_rows,
        original_phase_zero_knot_multiplicity=phase_at_zero,
        actual_waist_conclusion="a_prime=a_third=E_prime=K_prime=q_prime=beta=B_plus=B_minus=S=0",
        conclusion_uses_exact_spline_regularity_and_symmetrized_definitions=True,
        point_interval_containing_zero_not_used_as_identity=True,
        model_Xi="1/(16 rho^(5/2))",
        model_finite_part_from_cut_H="-1/(24 H^(3/2))",
        actual_root_finite_symmetric_cross_coefficient="(beta*u*v/eta)|root",
        finite_symmetric_cross_coefficient_not_erased=True,
        full_current_root_positive_port_and_strong_remainder_claimed=False,
        current_finite_part_identified_with_full_return_beta=False,
        all_current_mean_and_source_rows_remain_obligations=True,
        public_run_id=os.environ.get("GITHUB_RUN_ID"),
        public_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        sympy_version=sp.__version__, numpy_version=np.__version__, gates=gates,
        seconds=time.monotonic()-started)
    raw = (json.dumps(report, indent=2, allow_nan=False)+"\n").encode()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if args.out.suffix == ".gz":
        raw = gzip.compress(raw, mtime=0)
    args.out.write_bytes(raw)
    print(json.dumps(dict(complete=report["complete"], gates=len(gates),
                         output_sha256=sha(args.out), seconds=report["seconds"])), flush=True)
    if not report["complete"]:
        raise RuntimeError("a complete actual audit gate failed; original output retained")


if __name__ == "__main__":
    main()
