#!/usr/bin/env python3
"""R291 exact certificates, starting with the original R288 theta coefficients."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

checks = []


def require(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def mod(x, p):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, p) % p


def power_series(exponent, length):
    """Coefficients of (1-q)^exponent, over Q."""
    out = [F(1)]
    for n in range(1, length):
        out.append(-out[-1] * (exponent-n+1) / n)
    return out


def multiply(a, b, length, p):
    return [sum(a[j]*b[n-j] for j in range(n+1)
                if j < len(a) and n-j < len(b)) % p
            for n in range(length)]


payload = {"primes": {}}
for p in (5, 11, 23):
    r = (p+1)//3
    length = 2*r-1
    z = [F(0), F(1, 6)]
    for n in range(1, p-1):
        z.append(z[-1] * F(n*(3*n+1), (n+1)*(3*n+2)))
    h = [F(1)]
    for j in range(r-1):
        h.append(h[-1] * F((3*j+2)*(3*j+1),
                           3*(j+1)*(3*j+4)))
    a0 = p*z[r]
    a = mod(a0, p)
    require(f"p={p}: original first bad-band residue is a unit", a != 0)
    A = [mod(a0*h[n], p) if n < r else 0 for n in range(length)]
    Uq = [z[r+n] - (z[r]*h[n] if n < r else 0)
          for n in range(length)]
    require(f"p={p}: the whole original allowed U-window is integral",
            all(x.denominator % p for x in Uq))
    U = [mod(x, p) for x in Uq]
    require(f"p={p}: original constant and top Dixon coefficient",
            U[0] == 0 and mod(h[-1], p) == 1)

    B = [mod(F((-1)**j*comb(r-1, j)-1, 3*j+2), p)
         for j in range(r-1)]
    require(f"p={p}: B at one vanishes exactly", sum(B) % p == 0)
    require(f"p={p}: complete polynomial differential and Cartier term",
            all(((3*j+2)*B[j] - ((-1)**j*comb(r-1, j)-1)) % p == 0
                for j in range(r-1))
            and ((-1)**(r-1)-1) % p == (-2) % p)
    require(f"p={p}: actual B-degree and leading coefficient",
            (not any(B)) if p == 5 else B[-1] == mod(F(5, 9), p))

    T = [mod(2*a0*h[j]*F(18*j*j+30*j+11,
                         27*(j+1)*(3*j+4)), p)
         for j in range(r-1)]
    T.append(mod(2*a0*F(2*r-1, 3)*h[-1], p))
    force_left = [0] + [(9*t) % p for t in T]
    force_right = [0]*(r+1)
    for j in range(r):
        force_right[j] += A[j]
        force_right[j+1] += A[j]
    force_right[0] += a
    force_right[r] -= a
    for j in range(r+1):
        force_right[j] -= 2*a*(-1)**j*comb(r, j)
    require(f"p={p}: full forcing compression including top coefficient",
            force_left == [x % p for x in force_right])

    v2 = [mod(x, p) for x in power_series(F(2, 3), length)]
    first_row = [((1+3*n)*U[n]+A[n]) % p for n in range(length)]
    left = multiply(v2, first_row, length, p)
    right = [1] + [mod(F(2, 3*n), p) for n in range(1, length)]
    for j, coefficient in enumerate(B):
        vp = power_series(F(j)+F(2, 3), length)
        right = [(right[n]+coefficient*mod(vp[n], p)) % p
                 for n in range(length)]
    right = [(a*x) % p for x in right]
    require(f"p={p}: first integral on every original integral coefficient",
            left == right)
    require(f"p={p}: first resonance is exactly the excluded q^p boundary",
            all((1+3*n) % p for n in range(length))
            and (1+3*length) == 2*p and r+length == p)
    payload["primes"][str(p)] = {
        "r": r, "window_length": length, "a0_mod_p": a,
        "U_mod_p": U, "B_coefficient_at_V_power_3j_plus_2": B,
        "first_integral_common_coefficients": left,
        "cartier_beta_coefficient_of_dv": (-2) % p,
    }

payload.update(status="PASS", number_of_checks=len(checks), checks=checks)
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n")
print(json.dumps({"status": "PASS", "checks": len(checks),
                  "output": str(output)}))
