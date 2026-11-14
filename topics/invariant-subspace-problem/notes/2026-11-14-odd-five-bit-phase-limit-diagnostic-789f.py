#!/usr/bin/env python3
"""One exact S3 block; no sampling and no general phase claim."""
import json
import time
import sympy as sp


def main():
    started = time.monotonic()
    x = sp.symbols("x", positive=True)  # x=r^2
    clean = lambda matrix: matrix.applyfunc(sp.cancel)
    # Full S3-invariant H_1 in coordinates (head0/r, r*head1, pool).
    # Physical metric is M; these are not Euclidean coordinates.
    m = sp.diag(1 / x, x, 3)
    f1 = sp.Matrix([
        [3 + 1/x, x, 3*x],
        [1/x, 3 + x, 3/x],
        [1, 1, 4 + x + 1/x],
    ])
    f2 = sp.Matrix([
        [3 + 3/x, 3*x, 6*x + 3],
        [3/x, 3 + 3*x, 3 + 6/x],
        [2 + 1/x, x + 2, 4 + 4*x + 4/x],
    ])
    e = sp.Matrix([[1, 0], [0, 1], [-sp.Rational(1, 3), -sp.Rational(1, 3)]])
    h = e.T * m * e
    assert m*f1 == f1.T*m and m*f2 == f2.T*m
    g1h = clean(e.T * m * f1.inv(method="DM") * e)
    g2h = clean(e.T * m * f2.inv(method="DM") * e)
    # The upper invariant primitive line has Gram hu and true Gamma_1=1.
    hu = 3 * (x + 1/x + 4)
    bridge = sp.Matrix([3*(1/x - 1), 3*(x - 1)])
    q = clean(bridge.T * g2h / hu)
    qh = clean(q.T * hu * q)
    innovation = clean(g1h.inv(method="DM")*g2h - 2*h.inv()*g1h - h.inv()*qh)
    kh = clean(qh + innovation.T*h*g2h.inv(method="DM")*h*innovation)
    kop = clean(h.inv()*kh)
    trace = sp.factor(sp.trace(kop))
    determinant = sp.factor(kop.det())
    trace_limit = sp.limit(trace, x, sp.oo)
    determinant_limit = sp.limit(determinant, x, sp.oo)
    assert trace_limit == sp.Rational(2, 3)
    assert determinant_limit == sp.Rational(1, 9)
    print(json.dumps({
        "status": "exact_diagnostic_only",
        "seconds": time.monotonic() - started,
        "parameter": "x=r^2, weights=(r,r^-1,1,1,1)",
        "block": "full S3 invariant upper line / lower two-dimensional primitive source",
        "trace": str(trace),
        "determinant": str(determinant),
        "trace_limit": str(trace_limit),
        "determinant_limit": str(determinant_limit),
        "both_eigenvalue_limits": "1/3",
        "general_phase_bound_proved": False,
    }, indent=2))


if __name__ == "__main__":
    main()
