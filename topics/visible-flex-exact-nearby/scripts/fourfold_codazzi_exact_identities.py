#!/usr/bin/env python3
"""Exact symbolic checks for R126; no numerical continuum gate is asserted."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    checks = {}

    def check(name, expression):
        entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
        values = [s.factor(x) for x in entries]
        checks[name] = all(x == 0 for x in values)
        if not checks[name]:
            raise ArithmeticError((name, values))

    A, B, C, K, a, ap, app, At, Bt, Bs, Cs, h = s.symbols(
        "A B C K a ap app At Bt Bs Cs h", nonzero=True
    )
    M = s.Matrix([[0, 0, -A], [0, 0, -B], [A, B, 0]])
    N = s.Matrix([[0, -ap, -a*B], [ap, 0, -a*C], [a*B, a*C, 0]])
    Mt = s.Matrix([[0, 0, -At], [0, 0, -Bt], [At, Bt, 0]])
    Ns = s.Matrix([[0, -app, -ap*B-a*Bs],
                   [app, 0, -ap*C-a*Cs],
                   [ap*B+a*Bs, ap*C+a*Cs, 0]])
    flat = Mt-Ns+N*M-M*N
    check("frame_radial_generator_is_skew", M+M.T)
    check("frame_angular_generator_is_skew", N+N.T)
    check("complete_frame_flatness", flat.subs({
        Bs: At/a-2*ap*B/a, Cs: Bt/a+ap*(A-C)/a,
        app: -a*(A*C-B*B),
    }, simultaneous=True))

    L = s.Matrix([[2*B/C, -(K+B*B)/(C*C)], [1, 0]])/a
    H = s.Matrix([[1, -B/C], [-B/C, (B*B-K)/(C*C)]])
    check("actual_symmetrizer", H*L-(H*L).T)
    check("symmetrizer_determinant", H.det()+K/(C*C))
    lam = s.symbols("lambda")
    check("principal_characteristic_polynomial",
          (lam*s.eye(2)-L).det()-((lam-B/(a*C))**2+K/(a*a*C*C)))
    Ctheta = s.symbols("Ctheta")
    utheta = s.Matrix([Bt, Ctheta])
    forcing = s.Matrix([-2*h*B, h*((K+B*B)/C-C)])
    jac = (L*utheta+forcing).jacobian([B, C])
    expected_jac = s.Matrix([
        [2*Bt/(a*C)-2*B*Ctheta/(a*C*C)-2*h,
         -2*B*Bt/(a*C*C)+2*(K+B*B)*Ctheta/(a*C**3)],
        [2*h*B/C, -h*((K+B*B)/(C*C)+1)],
    ])
    check("complete_linearized_lower_order_matrix", jac-expected_jac)

    k, kp, gamma, beta = s.symbols("k kp gamma beta", nonzero=True)
    p = (B+k)/C
    q = (B-k)/C
    Ar = (B*B-k*k)/C
    Br = gamma*(s.diff(Ar, B)*Bt+s.diff(Ar, C)*Ctheta)-2*beta*B
    Cr = gamma*Bt+beta*(Ar-C)
    pr = s.diff(p, B)*Br+s.diff(p, C)*Cr+s.diff(p, k)*kp
    qr = s.diff(q, B)*Br+s.diff(q, C)*Cr+s.diff(q, k)*kp
    pt = s.diff(p, B)*Bt+s.diff(p, C)*Ctheta
    qt = s.diff(q, B)*Bt+s.diff(q, C)*Ctheta
    check("first_complete_Riemann_equation",
          pr-(gamma*q*pt-beta*q*(1+p*p)+kp/(2*k)*(p-q)))
    check("second_complete_Riemann_equation",
          qr-(gamma*p*qt-beta*p*(1+q*q)-kp/(2*k)*(p-q)))
    check("inverse_C", 2*k/(p-q)-C)
    check("inverse_B", k*(p+q)/(p-q)-B)
    check("inverse_A", C*p*q-Ar)

    P, Q, kap = s.symbols("P Q kappa")
    f = -beta*Q*(1+P*P)+kap*(P-Q)
    g = -beta*P*(1+Q*Q)-kap*(P-Q)
    check("forcing_jacobian",
          s.Matrix([f, g]).jacobian([P, Q])-s.Matrix([
              [-2*beta*P*Q+kap, -beta*(1+P*P)-kap],
              [-beta*(1+Q*Q)-kap, -2*beta*P*Q+kap],
          ]))
    check("first_forcing_Hessian",
          s.hessian(f, [P, Q])-s.Matrix([[-2*beta*Q, -2*beta*P],
                                        [-2*beta*P, 0]]))
    check("second_forcing_Hessian",
          s.hessian(g, [P, Q])-s.Matrix([[0, -2*beta*Q],
                                        [-2*beta*Q, -2*beta*P]]))
    report = {
        "kind": "R126_exact_symbolic_Gauss_Codazzi_identities",
        "complete": all(checks.values()),
        "checks": checks,
        "check_count": len(checks),
        "sympy_version": s.__version__,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Exact rational symbolic identities only; no finite angular truncation.",
        "continuation_numerical_gates_paid": False,
        "closed_surface_or_flex_completion_claimed": False,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"complete": report["complete"], "check_count": len(checks),
                      "out": str(args.out)}))


if __name__ == "__main__":
    main()
