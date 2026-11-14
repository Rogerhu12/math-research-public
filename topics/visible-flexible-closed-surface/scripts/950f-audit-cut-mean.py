#!/usr/bin/env python3
"""Independent exact arithmetic checks for the regular-cut mean lemma.

The analytic proof is audited separately.  These checks certify the stored
finite Fourier trace's coefficient sizes, not an exact numerical isometry.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def number(q):
    return {"numerator": str(q.numerator), "denominator": str(q.denominator),
            "display": float(q)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("geometry", type=Path)
    parser.add_argument("proof", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit("Refusing to overwrite an earlier audit record")
    data = json.loads(args.geometry.read_text())
    cut = data["cut"]
    h = [F.from_float(float(x)) for x in cut["height"]]
    slope = [F.from_float(float(x)) for x in cut["height_s"]]
    v = sum((3*j*abs(x) for j, x in enumerate(h, 1)), F(0))
    w = sum(((3*j)**2*abs(x) for j, x in enumerate(h, 1)), F(0))
    u0 = sum(map(abs, slope), F(0))
    mean = F.from_float(float(cut["mean_height_s"]))
    assert F(2, 5) <= mean <= F(1, 2)
    assert v <= F(1, 200) and w <= F(1, 50) and u0 <= F(1, 50)
    a = F(3, 5)
    alpha_abs_lower = F(447, 500)
    assert alpha_abs_lower**2 < F(4, 5)
    u_min, u_max = F(19, 50), F(13, 25)
    q_floor = 1-u_max**2-(F(1, 200)/a)**2
    eta_floor = alpha_abs_lower*u_min-F(1, 50)/a
    second_denominator_ceiling = F(1, 50)-a*alpha_abs_lower*u_min
    assert q_floor > F(1459, 2000)
    assert eta_floor > F(153, 500)
    assert second_denominator_ceiling < -F(919, 5000)
    # Also show that the very small difference between the stored binary64
    # cut geometry and the displayed rational background cannot affect the
    # stated coarse inequalities. This is not a solver error enclosure.
    a_low, a_high = F(599999, 1000000), F(600001, 1000000)
    e_low, e_high = F(124999, 100000), F(125001, 100000)
    stored_a = F.from_float(float(cut["cut"]["radius"]))
    stored_e = F.from_float(float(cut["E"]))
    assert a_low <= stored_a <= a_high and e_low <= stored_e <= e_high
    assert alpha_abs_lower**2 < 1/e_high
    robust_q = 1-u_max**2-(F(1, 200)/a_low)**2
    robust_eta = alpha_abs_lower*u_min-F(1, 50)/a_low
    robust_denominator = F(1, 50)-a_low*alpha_abs_lower*u_min
    assert robust_q > F(1459, 2000)
    assert robust_eta > F(153, 500)
    assert robust_denominator < -F(919, 5000)
    report = {
        "scope": "Exact Fraction checks of the conditional regular-cut lemma's coarse domain and the stored finite Fourier trace. No existence, exact numerical isometry, C2 gluing, or infinite-tail assertion.",
        "status": "PASS",
        "sources": {str(p.resolve()): digest(p) for p in
                    [Path(__file__), args.geometry, args.proof]},
        "modes": len(h),
        "finite_fourier_size_bounds": {
            "v": number(v), "w": number(w), "u0": number(u0),
            "mean_u": number(mean)},
        "coarse_domain_exact_bounds": {
            "Q_lower": number(q_floor), "H_derivative_lower": number(eta_floor),
            "second_jet_denominator_upper": number(second_denominator_ceiling)},
        "robust_binary_geometry_neighborhood": {
            "radius_interval": [number(a_low), number(a_high)],
            "E_interval": [number(e_low), number(e_high)],
            "Q_lower": number(robust_q),
            "H_derivative_lower": number(robust_eta),
            "second_jet_denominator_upper": number(robust_denominator)},
    }
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": report["status"], "modes": len(h),
                      "v": float(v), "w": float(w), "u0": float(u0),
                      "eta_lower": float(eta_floor)}))


if __name__ == "__main__":
    main()
