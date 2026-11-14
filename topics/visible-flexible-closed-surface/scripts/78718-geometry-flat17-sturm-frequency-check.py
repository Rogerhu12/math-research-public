#!/usr/bin/env python3
"""Author exact checks of Sturm scaling and actual flat17 frequency constants.
No PDE solver, candidate optimization, or independent audit is performed.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import sympy as s

TOPIC = Path(__file__).resolve().parent.parent
PROOF = TOPIC / "notes/2026-11-10-78718-geometry-flat17-sturm-frequency-provider-v1.md"
PROOF_SHA = "68962bac35e0a6969ce159b17e0b7754698cffc816248ddfb596c35a7a93f5db"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if sha(PROOF) != PROOF_SHA:
        raise ValueError("Frozen proof identity mismatch")
    a, c, q, p, x, y, xu, yu, f1, f2 = s.symbols("a c q p x y xu yu f1 f2")
    alpha = p / a
    ps = c * q / a * p**3
    alphas = ps / a - p * c / a**2
    d1 = -c / a * (1 - q * p**2)
    d2 = 3 * c * q / a * p**2
    h = 1 / (a**2 * p)
    v = a**2 * q * p**4
    xs = -q * p**3 * yu + f1 / alpha
    ys = -h * xu + f2 / p**3
    symbolic = {}

    def zero(name, expr):
        value = s.cancel(expr)
        if value != 0:
            raise AssertionError((name, str(value)))
        symbolic[name] = True

    zero("d1_is_alpha_log_derivative", alphas / alpha - d1)
    zero("d2_is_triple_p_log_derivative", 3 * ps / p - d2)
    zero("beta_equation", alphas * x + alpha * xs
         - (-alpha * q * p**3 * yu + d1 * alpha * x + f1))
    zero("pi_equation", 3 * p**2 * ps * y + p**3 * ys
         - (-alpha**2 * xu + d2 * p**3 * y + f2))
    zero("sturm_x_source", xs / h + v * yu - a**3 * f1)
    zero("sturm_y_source", ys / h + xu - a**2 / p**2 * f2)
    jj, vv = s.symbols("jj vv", real=True)
    mat = -s.I * jj * s.Matrix([[0, vv], [1, 0]])
    flux = s.Matrix([[0, 1], [1, 0]])
    defect = mat.conjugate().T * flux + flux * mat
    for row in range(2):
        for col in range(2):
            zero(f"flux_{row}_{col}", defect[row, col])
    zero("zero_trace", s.trace(mat))
    aa, ab, bb, bc = s.symbols("aa ab bb bc")
    scat = s.Matrix([[-bc / ab, 1 / ab], [1 / ab, bb / ab]])
    adj = s.Matrix([[-bb / aa, 1 / aa], [1 / aa, bc / aa]])
    gram = adj * scat
    zero("scattering_gram_01", gram[0, 1])
    zero("scattering_gram_10", gram[1, 0])
    zero("scattering_gram_00", gram[0, 0] - (1 + bb * bc) / (aa * ab))
    zero("scattering_gram_11", gram[1, 1] - (1 + bb * bc) / (aa * ab))

    A, P = F(43, 40), F(51, 50)
    eps, eta = F.from_float(.4), F.from_float(.05)
    vu, vd = F.from_float(.17), F.from_float(.18)
    delta = F.from_float(.07254443456654512)
    accel = F(181, 1000)**2 * F(601, 1000) / (
        F(9, 125) * F(399, 1000) * F(949, 1000))
    z, cutoff = F(3, 4), 18
    exp_upper = sum((z**k / F(factorial(k)) for k in range(cutoff + 1)), F(0))
    exp_upper += (z**(cutoff + 1) / F(factorial(cutoff + 1))) / (
        1 - z / F(cutoff + 2))
    rational = {
        "actual_eps": F(399, 1000) < eps < F(401, 1000),
        "actual_eta": F(49, 1000) < eta < F(51, 1000),
        "actual_vu": F(169, 1000) < vu < F(181, 1000),
        "actual_vd": F(179, 1000) < vd < F(181, 1000),
        "actual_delta": F(9, 125) < delta < F(3, 40),
        "acceleration": accel < F(3, 4),
        "background_p": P**2 * (1 - F(181, 1000)**2) > 1,
        "period": F(3, 40) / F(599, 1000) * (F(1000, 169) + F(1000, 179)) < F(3, 2),
        "omega_factor": A**3 * P**4 < F(27, 20),
        "a_cubed": A**3 < F(5, 4),
        "p_fourth": P**4 < F(11, 10),
        "H_lower": A**2 * P < F(6, 5),
        "coordinate_factor": A * P**3 < F(23, 20),
        "central_physical_width": F(399, 1000) * F(9, 125) / F(601, 1000) * F(2000, 181) > F(1, 2),
        "sqrt_a_cubed": F(5, 4) < F(81, 64),
        "sqrt_omega": F(27, 20) < F(36, 25),
        "S_upper": F(161, 80) < F(9, 4),
        "exponential": exp_upper < F(11, 5),
        "full_sturm_constant_17": F(3, 2) * F(99, 80) * F(161, 80)**2 * F(11, 5) < 17,
        "full_physical_constant_20": F(17) * F(23, 20) < 20,
        "outer_constant_6": F(3, 2) * F(6, 5) * F(3, 2) * F(11, 5) < 6,
        "negative_action": F(3, 40) * F(401, 599) < F(81, 1600),
        "l2_coordinate": A**2 * P**7 < F(36, 25),
    }
    if not all(rational.values()):
        raise AssertionError([name for name, value in rational.items() if not value])
    report = {
        "scope": __doc__.strip(),
        "proof": str(PROOF.relative_to(TOPIC)),
        "proof_sha256": PROOF_SHA,
        "checker_sha256": sha(Path(__file__).resolve()),
        "symbolic_checks": symbolic,
        "rational_checks": rational,
        "symbolic_count": len(symbolic),
        "rational_count": len(rational),
        "exp_three_quarters_upper": str(exp_upper),
        "pde_runs": 0,
        "new_candidate_runs": 0,
        "passed": True,
    }
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "passed": True, "symbolic_count": len(symbolic),
        "rational_count": len(rational), "pde_runs": 0,
        "report_bytes": args.out.stat().st_size,
        "report_sha256": sha(args.out),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

