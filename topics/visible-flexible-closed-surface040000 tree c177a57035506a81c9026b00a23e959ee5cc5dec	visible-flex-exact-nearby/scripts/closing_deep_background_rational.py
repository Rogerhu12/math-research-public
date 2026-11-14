"""Exact-rational conservative bound for the default N=160 infinite background.

Inputs are exact decimals: r_c=1/4, w_cut=1/2, delta0=3/500,
R=64, a=11/4, c_n=(1/20)2^(-n/2). Calibration existence is
R28 section 1, whose Git blob is recorded in the accompanying note.
This certifies the unwarped rotational background only.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sys


def run():
    delta0, wc, rc, R, N = F(3, 500), F(1, 2), F(1, 4), 64, 160
    eta0 = delta0 / 20
    # 2^(-3/2) < 3/8, since sqrt(2)>4/3.
    assert F(4, 3) ** 2 < 2
    total_log_upper = 6 * delta0 + 6 * eta0 * F(8, 5)
    # sqrt(12)>3 and 2^(11/4)>6; exp(x)<=1/(1-x) for 0<=x<1.
    assert 3 ** 2 < 12 and 6 ** 4 < 2 ** 11
    assert 7 * total_log_upper / 3 < F(1, 10)
    W = wc * R / (6 * delta0) * F(10, 9) / 2 ** (7 * N // 4)
    # log 2 < 7/10: a lower Taylor polynomial for exp(7/10) exceeds 2.
    def exp_partial(x, degree):
        term = total = F(1)
        for k in range(1, degree + 1):
            term *= x / k
            total += term
        return total
    assert exp_partial(F(7, 10), 4) > 2
    # log(500/3)<6, by an exact lower Taylor polynomial.
    assert exp_partial(F(6), 5) > F(500, 3)
    H = (2 * N + 7) * F(7, 10) + 12
    assert H < 241
    eta = eta0 / 2 ** (3 * N // 2)
    # sqrt(12)<7/2 and max S'=15/8.
    assert F(7, 2) ** 2 > 12
    B = F(7, 2) * W * F(15, 8) * 241 / (eta * rc) + 7 * W / rc
    assert B < F(1, 50)
    angular = W / rc
    assert angular < F(1, 10 ** 79)
    # The first term decreases for every n>=160. 2^(1/4)>7/6.
    assert F(7, 6) ** 4 < 2
    monotone_ratio_upper = (H + F(7, 5)) / H * F(6, 7)
    assert monotone_ratio_upper < 1
    # R28 calibration bound at n=80, monotone thereafter.
    cn = F(1, 20) / 2 ** 40
    dn = delta0 / 2 ** 80
    calibration_bound = 792 * (384 * cn + 36 * dn * dn) / (1 - 384 * cn)
    assert calibration_bound < F(1, 10 ** 7) < 33
    # Remaining radial distance: exp(x)-1<=2x for x<=1/2.
    log_radius_upper = total_log_upper / (3 * 2 ** N)
    assert log_radius_upper < F(1, 2)
    radial_extent = 2 * rc * log_radius_upper
    remaining_height = W * radial_extent
    assert remaining_height < F(1, 10 ** 131)

    def show(x):
        return {"numerator": str(x.numerator), "denominator": str(x.denominator), "approx": float(x)}

    return {
        "scope": "Exact-rational bound for the unchanged n>=160 rotational background; not the finite warp or nonrotational surface.",
        "source_r28_blob": "cf9881e3ae2c2797a61213ab099dbec239be5f0d",
        "parameters": {"rCuff": "1/4", "wCut": "1/2", "delta0": "3/500", "R": 64, "a": "11/4", "N": 160},
        "W160_upper": show(W), "meridian_curvature_upper": show(B),
        "angular_curvature_upper": show(angular), "strict_meridian_bound": "1/50",
        "calibration_B80_upper": show(calibration_bound),
        "first_term_step_ratio_upper": show(monotone_ratio_upper),
        "remaining_height_upper": show(remaining_height),
        "conclusion": "Every exact bracket-root selection from R28 gives |kappa_mer|<0.02 in all unwarped cells n>=160, and w,w_r tend to zero, so the rotational background closes C2 onto the flat disk."
    }


if __name__ == "__main__":
    result = run()
    text = json.dumps(result, indent=2) + "\n"
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(text)
    print(text)
