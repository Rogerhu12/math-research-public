#!/usr/bin/env python3
"""Exact arithmetic supporting R469, with no numerical L-values.

The polynomial is the actual R466 line, in the b=1 model.  Its first five
Taylor coefficients follow from x''=6*x^2 and (log sigma)''=-x.  The p=23
calculation is one exact certificate for this fixed curve, not a prime scan.
"""
from pathlib import Path
import json
from flint import fmpq as Q, fmpq_poly as Poly


def source_polynomial():
    X = Poly([0, 1])
    return (
        (X + 1) * (X**2 + 20*X - 8) * (7*X**2 - 4*X + 16)
        * (X**4 + 40*X**3 + 2112*X**2 + 3136*X + 1792)
        * (13*X**4 + 52*X**3 + 1536*X**2 + 1024*X + 256)
        * (X**8 + 1232*X**7 - 58688*X**6 - 49408*X**5
           - 439040*X**4 - 2111488*X**3 - 1949696*X**2
           - 851968*X - 32768) / 91
    )


def taylor_coefficients():
    n = 5
    P = source_polynomial()
    assert P.degree() == 21 and P[21] == 1
    x = [Q(1), Q(-1, 7)]
    for k in range(2, n):
        x.append(6*sum((x[i]*x[k-i] for i in range(1, k)), Q(0))
                 / ((6*k-2)*(6*k-3)-12))
    logarithm = [Q(0)] + [
        -136*x[k]/(6*k*(6*k-1)) for k in range(1, n)
    ]
    exponential = [Q(1)]
    for k in range(1, n):
        exponential.append(sum(
            (i*logarithm[i]*exponential[k-i] for i in range(1, k+1)),
            Q(0))/k)

    def mul(a, b):
        return [sum((a[i]*b[k-i] for i in range(k+1)), Q(0))
                for k in range(n)]

    def power(a, r):
        out = [Q(1)] + [Q(0)]*(n-1)
        while r:
            if r & 1:
                out = mul(out, a)
            a = mul(a, a)
            r //= 2
        return out

    alpha = [Q(0)]*(n+1)
    for j in range(21, -1, -1):
        shift = 22-j
        if shift > n:
            continue
        v = mul(exponential, power(x, 2+3*j))
        for k in range(n+1-shift):
            alpha[shift+k] += P[j]*v[k]
    return alpha


def residue(a, p):
    return int(a.numerator) % p * pow(int(a.denominator) % p, -1, p) % p


def main():
    alpha = taylor_coefficients()
    assert alpha[1] == 1
    assert alpha[2] == Q(135218, 105)
    assert alpha[3] == Q(21083507491, 1576575)
    assert alpha[4] == Q(1377083080404572, 9435801375)
    # Norm(f)=64*3*17^2; the roots of unity contribute precisely six.
    ray_degree = Q(64*3*17**2, 6)*Q(3, 4)*Q(2, 3)*Q(288, 289)
    assert ray_degree == 4608
    # h^2=-51*sqrt(3)/(408^2*pi^2).
    assert Q(136*51*3, 408**2) == Q(1, 8)
    assert Q(4*51, 408**2) == Q(1, 816)
    assert Q(2*4*51, 408**2) == Q(1, 408)
    assert Q(3, 408) == Q(1, 136)
    # D=2312; each source term has weight -1 and leading z-degree six.
    D = 2312
    assert D == 8*17**2 and D//17 == 136
    assert Q(-136, 6)+Q(2, 3)+21 == -1
    assert min(132-6*j for j in range(22)) == 6
    p = 23
    alpha24 = residue(alpha[4], p)
    pc = (-pow(4, -4, p)*70) % p
    derivative_over_p = alpha24*pow(136*pc % p, -1, p) % p
    assert (alpha24, pc, derivative_over_p) == (15, 15, 11)
    physical_alpha24 = pow(D, 3, p)*alpha24 % p
    physical_derivative_over_p = pow(D, -1, p)*derivative_over_p % p
    assert physical_alpha24 == physical_derivative_over_p == 22
    out = {
        "curve": "y^2=x^3+2312",
        "normalization": "F_1=sigma^136*x^2*P21(x^3;1), first z^6 coefficient 1",
        "source_polynomial": [str(c) for c in source_polynomial()],
        "alpha": {str(6*k): str(alpha[k]) for k in range(1, 6)},
        "primitive_ray_class_degree": str(ray_degree),
        "real_square_scale": 408,
        "CM_square_scale": 136,
        "single_inert_prime": {
            "p": p, "alpha24_mod_p": alpha24, "pc_mod_p": pc,
            "J136_derivative_div_p_mod_p": derivative_over_p,
            "physical_s24_mod_p": physical_alpha24,
            "physical_derivative_div_p_mod_p": physical_derivative_over_p,
        },
        "scope": "With the full R469 Selmer bridge: exact rank two and finite Sha[23^infinity]. No infinitely-many-p claim.",
    }
    Path(__file__).with_suffix(".json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2)+"\n")
    print("R469 exact source, period scales, ray degree, and p=23 certificate passed.")


if __name__ == "__main__":
    main()
