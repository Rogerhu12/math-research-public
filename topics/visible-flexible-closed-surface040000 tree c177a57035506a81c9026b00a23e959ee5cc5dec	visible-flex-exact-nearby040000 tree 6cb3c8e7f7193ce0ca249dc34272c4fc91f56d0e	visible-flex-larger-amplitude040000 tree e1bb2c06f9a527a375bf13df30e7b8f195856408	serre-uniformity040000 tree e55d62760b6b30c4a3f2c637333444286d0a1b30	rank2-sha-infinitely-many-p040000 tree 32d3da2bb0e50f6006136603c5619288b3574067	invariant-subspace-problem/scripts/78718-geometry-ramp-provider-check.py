#!/usr/bin/env python3
"""Author-side exact algebra and rational gates for the ramp provider.
This is not a PDE run, an embedding/reach certificate, or an independent audit.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sympy as sy

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
PROOF = TOPIC / "notes/2026-11-10-78718-geometry-ramp-analytic-provider-v1.md"
PROOF_SHA = "bb727afa2bc5ba13d1005df5d806757f69332d35c6ea172cfb7ac781a19d2402"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if sha(PROOF) != PROOF_SHA:
        raise ValueError("Frozen proof identity mismatch")
    a, ap, q, b, p, bu, pu, qs = sy.symbols(
        "a ap q b p bu pu qs", nonzero=True
    )
    mu = ap / a
    bs = (b * bu - q * p * pu) / a - mu * b * (1 + b**2 - q * p**2)
    ps = (b * pu - p * bu) / a - mu * p * (b**2 - q * p**2)
    ell = (b**2 - q * p**2) / (a * p)
    m = b / p
    c = a / p

    def dr(f):
        return (sy.diff(f, a) * ap + sy.diff(f, ap) * q / a
                + sy.diff(f, b) * bs + sy.diff(f, p) * ps
                + sy.diff(f, q) * qs)

    def du(f):
        return sy.diff(f, b) * bu + sy.diff(f, p) * pu

    checks = {}

    def check_zero(name, expression):
        result = sy.cancel(expression)
        if result != 0:
            raise AssertionError((name, str(result)))
        checks[name] = True

    check_zero("gauss", ell * c - m**2 + q)
    check_zero("codazzi_M", dr(m) - du(ell) + mu * m)
    check_zero("codazzi_C", dr(c) - du(m) - mu * c - a * ap * ell)
    os = sy.Matrix([[0, 0, -ell], [0, 0, -m / a], [ell, m / a, 0]])
    ou = sy.Matrix([[0, -ap, -m], [ap, 0, -c / a], [m, c / a, 0]])
    curvature = os.applyfunc(du) - ou.applyfunc(dr) + ou * os - os * ou
    for i in range(3):
        for j in range(3):
            check_zero(f"frame_curvature_{i}_{j}", curvature[i, j])
    check_zero("rotational_background_b", bs.subs({b: 0, bu: 0, pu: 0}))
    check_zero(
        "rotational_background_p",
        ps.subs({b: 0, bu: 0, pu: 0}) - mu * q * p**3,
    )
    pb = (1 - ap**2) ** sy.Rational(-1, 2)
    if sy.simplify(sy.diff(pb, ap) * q / a - mu * q * pb**3) != 0:
        raise AssertionError("Rotational background derivative failed")
    checks["rotational_background_derivative"] = True

    eps = F.from_float(0.4)
    eta = F.from_float(0.05)
    vu = F.from_float(0.17)
    vd = F.from_float(0.18)
    delta = F.from_float(0.07254443456654512)
    acceleration_bound = (
        F(181, 1000)**2 * F(601, 1000)
        / (F(9, 125) * F(399, 1000) * F(949, 1000))
    )
    rational = {
        "eps_lower": F(399, 1000) < eps,
        "eps_upper": eps < F(401, 1000),
        "eta_lower": F(49, 1000) < eta,
        "eta_upper": eta < F(51, 1000),
        "vu_bounds": 0 < vu < F(181, 1000),
        "vd_bounds": 0 < vd < F(181, 1000),
        "delta_lower": F(9, 125) < delta,
        "delta_upper": delta < F(3, 40),
        "acceleration_upper": acceleration_bound < F(3, 4),
        "Q_upper": F(43, 40) * F(3, 4) < 1,
        "mu_upper": F(181, 1000) < F(1, 5),
        "rouche_margin": F(1, 8) + F(1, 4) < F(1, 2),
    }
    for name, value in rational.items():
        if not value:
            raise AssertionError(name)
    report = {
        "scope": __doc__.strip(),
        "proof": str(PROOF.relative_to(TOPIC)),
        "proof_sha256": PROOF_SHA,
        "checker_sha256": sha(Path(__file__).resolve()),
        "symbolic_checks": checks,
        "rational_checks": rational,
        "symbolic_count": len(checks),
        "rational_count": len(rational),
        "acceleration_upper_exact": str(acceleration_bound),
        "pde_runs": 0,
        "geometric_candidate_runs": 0,
        "passed": True,
    }
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "passed": True,
        "symbolic_count": len(checks),
        "rational_count": len(rational),
        "pde_runs": 0,
        "report_bytes": args.out.stat().st_size,
        "report_sha256": sha(args.out),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

