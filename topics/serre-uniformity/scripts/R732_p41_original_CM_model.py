#!/usr/bin/env python3
"""Exact p=41 input for the ORIGINAL R725/R732 CM model; public Actions only.

This computes the same b=r_0^6, not a convenient sextic twist.  It does not
claim to have computed the original X_1 -> C map, beta, or a height.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time

from flint import fmpq, fmpq_poly, fmpz_poly

P = 41
M = 7
D = 20
DEG = 280
FIBER = 40
X = fmpz_poly([0, 1])
FX = X**3 + 16
ONE = fmpq_poly([1])
U = fmpq_poly([0, 1])


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if path.suffix == ".gz":
        data = gzip.compress(data, mtime=0)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_bytes(data)
    tmp.replace(path)


def read(path):
    data = Path(path).read_bytes()
    if str(path).endswith(".gz"):
        data = gzip.decompress(data)
    return json.loads(data)


def enc(poly):
    return {"numerator": [str(c) for c in poly.numer().coeffs()],
            "denominator": str(poly.denom())}


def dec(item):
    return fmpq_poly([int(c) for c in item["numerator"]],
                     int(item["denominator"]))


def rational(q):
    return {"numerator": str(q.numer()), "denominator": str(q.denom())}


def valuation(q, prime=P):
    if q == 0:
        return None
    a, b = abs(int(q.numer())), int(q.denom())
    out = 0
    while a % prime == 0:
        out += 1
        a //= prime
    while b % prime == 0:
        out -= 1
        b //= prime
    return out


def check_eisenstein(poly):
    assert poly.leading_coefficient() == 1
    values = [valuation(poly[j]) for j in range(poly.degree())]
    assert values[0] == 1
    assert all(v is None or v >= 1 for v in values)
    return values


Q = {0: fmpz_poly([0]), 1: fmpz_poly([1]), 2: fmpz_poly([1]),
     3: 3*X**4 + 192*X,
     4: 2*(X**6 + 320*X**3 - 2048)}


def qdiv(n):
    """psi_n for odd n; psi_n/(2y) for even n, on y^2=x^3+16."""
    if n in Q:
        return Q[n]
    if n & 1:
        k = (n-1)//2
        left = qdiv(k+2)*qdiv(k)**3
        right = qdiv(k-1)*qdiv(k+1)**3
        if k & 1:
            right *= 16*FX**2
        else:
            left *= 16*FX**2
        value = left-right
    else:
        k = n//2
        value = qdiv(k)*(qdiv(k+2)*qdiv(k-1)**2 -
                        qdiv(k-2)*qdiv(k+1)**2)
    Q[n] = value
    return value


def torsion_modulus():
    psi = qdiv(P)
    assert psi.degree() == 840 and psi.leading_coefficient() == P
    assert all(psi[i] == 0 for i in range(psi.degree()+1) if i % 3)
    # psi_41(x)/x^840 = sum_j c_(840-3j)*(U/64)^j.
    raw = fmpq_poly([fmpq(psi[840-3*j], 64**j) for j in range(DEG+1)])
    modulus = raw / raw.leading_coefficient()
    assert modulus.degree() == DEG
    assert modulus.gcd(modulus.derivative()) == ONE
    check_eisenstein(modulus)
    return psi, raw, modulus


def cubic_part(poly, residue):
    assert all(poly[i] == 0 for i in range(poly.degree()+1)
               if i % 3 != residue)
    return fmpz_poly([poly[residue+3*j]
                     for j in range((poly.degree()-residue)//3+1)])


def reverse64(poly):
    deg = poly.degree()
    return fmpq_poly([poly[deg-j]*64**(deg-j) for j in range(deg+1)])


def multiple_ratio(n, modulus):
    """A(U)/B(U)=x([n]P)/x(P), with U=64/x(P)^3."""
    if n & 1:
        denx = qdiv(n)**2
        cross = 4*FX*qdiv(n-1)*qdiv(n+1)
    else:
        denx = 4*FX*qdiv(n)**2
        cross = qdiv(n-1)*qdiv(n+1)
    numx = X*denx-cross
    denx *= X
    residue = next(i % 3 for i, c in enumerate(numx.coeffs()) if c)
    at, bt = cubic_part(numx, residue), cubic_part(denx, residue)
    a, b = reverse64(at), reverse64(bt)
    difference = bt.degree()-at.degree()
    if difference >= 0:
        a *= U**difference
    else:
        b *= U**(-difference)
    return a % modulus, b % modulus


def mul(a, b, modulus):
    return (a*b) % modulus


def power(a, exponent, modulus):
    ans = ONE
    while exponent:
        if exponent & 1:
            ans = mul(ans, a, modulus)
        a = mul(a, a, modulus)
        exponent >>= 1
    return ans


def inv(a, modulus):
    g, s, t = a.xgcd(modulus)
    assert g == ONE
    assert s*a + t*modulus == ONE
    ans = s % modulus
    assert mul(a, ans, modulus) == ONE
    return ans


def field_trace(a, modulus):
    # Lagrange interpolation: trace(a)=[U^(DEG-1)](a P'(U) mod P).
    return mul(a, modulus.derivative(), modulus)[DEG-1]


def evaluate(poly, a, modulus):
    value = fmpq_poly([0])
    for c in reversed(poly.coeffs()):
        value = mul(value, a, modulus) + c
    return value


def compute(out):
    out.mkdir(parents=True, exist_ok=True)
    identity = {"p": P, "curve": [0, 0, 0, 0, 16],
                "coordinate": "U=64/x(P)^3", "torsion_degree": DEG,
                "original_b": "((w(P)-w(sqrt(-3)P))/2)^6",
                "source_sha256": sha(__file__), "python_flint": "0.9.0"}
    state_path = out/"p41-original-CM-state.json.gz"
    if state_path.exists():
        state = read(state_path)
        assert state["identity"] == identity
    else:
        state = {"identity": identity, "products_completed": 0,
                 "traces": [], "complete": False}
    started = time.monotonic()
    psi, raw, modulus = torsion_modulus()
    save(out/"p41-original-torsion-modulus.json.gz",
         {"identity": identity, "psi_41": enc(fmpq_poly(psi)),
          "raw_U_modulus": enc(raw), "monic_U_modulus": enc(modulus),
          "eisenstein_41_valuations": check_eisenstein(modulus)})
    if state["products_completed"]:
        wn, wd, rn, rd = [dec(state[k]) for k in ("wn", "wd", "rn", "rd")]
    else:
        wn = wd = rn = rd = ONE
    for n in range(state["products_completed"]+1, D+1):
        a, b = multiple_ratio(n, modulus)
        a2 = mul(a, a, modulus)
        a3 = mul(a2, a, modulus)
        b3 = power(b, 3, modulus)
        ub3 = mul(U, b3, modulus)
        wn = mul(wn, mul(a2, b, modulus), modulus)
        wd = mul(wd, 4*a3+ub3, modulus)
        rn = mul(rn, a3+ub3, modulus)
        rd = mul(rd, a3-2*ub3, modulus)
        state.update(products_completed=n, wn=enc(wn), wd=enc(wd),
                     rn=enc(rn), rd=enc(rd))
        save(state_path, state)
        print(json.dumps({"stage": "original-torsion-products", "n": n,
                          "seconds": time.monotonic()-started}), flush=True)
    if "original_b_in_U" in state:
        bvalue = dec(state["original_b_in_U"])
    else:
        w = mul(wn, inv(wd, modulus), modulus)
        r = mul(rn, inv(rd, modulus), modulus)
        antitrace = mul(w, ONE-((-3)**D)*power(r, 2, modulus), modulus)
        bvalue = mul(power(U, P-1, modulus),
                     power(antitrace, 6, modulus), modulus)/64
        state["original_b_in_U"] = enc(bvalue)
        save(state_path, state)
        print(json.dumps({"stage": "original-b", "seconds": time.monotonic()-started}),
              flush=True)
    # Every conjugate of b is represented exactly FIBER=40 times in Q[U]/P.
    traces = [fmpq(int(t["numerator"]), int(t["denominator"])) for t in state["traces"]]
    bpower = power(bvalue, len(traces), modulus)
    for k in range(len(traces)+1, M+1):
        bpower = mul(bpower, bvalue, modulus)
        traces.append(field_trace(bpower, modulus)/FIBER)
        state["traces"] = [rational(t) for t in traces]
        save(state_path, state)
        print(json.dumps({"stage": "exact-power-trace", "k": k,
                          "seconds": time.monotonic()-started}), flush=True)
    descending = [fmpq(1)]
    for k in range(1, M+1):
        ck = -sum((descending[k-i]*traces[i-1] for i in range(1, k+1)),
                  fmpq(0))/k
        descending.append(ck)
    minimal = fmpq_poly(list(reversed(descending)))
    assert minimal.degree() == M
    assert evaluate(minimal, bvalue, modulus).is_zero()
    eisenstein = check_eisenstein(minimal)
    discriminant = minimal.discriminant()
    assert valuation(discriminant) == M-1
    # Explicit inverse different in Q[b], for the original R728 Neron lattice.
    derivative_inverse = inv(minimal.derivative(), minimal)
    certificate = {
        "identity": identity, "complete": True,
        "original_b_not_a_replacement_twist": True,
        "minimal_polynomial_ascending": [rational(c) for c in minimal.coeffs()],
        "minimal_polynomial": enc(minimal),
        "eisenstein_41_valuations": eisenstein,
        "power_traces": [rational(t) for t in traces],
        "trace_fiber_multiplicity": FIBER,
        "exact_F_of_b_zero": True,
        "discriminant": rational(discriminant),
        "discriminant_41_valuation": valuation(discriminant),
        "inverse_different_generator": enc(derivative_inverse),
        "torsion_modulus_sha256": sha(out/"p41-original-torsion-modulus.json.gz"),
        "original_map_or_beta_computed": False,
        "seconds": time.monotonic()-started,
    }
    save(out/"p41-original-CM-model-certificate.json", certificate)
    state["complete"] = True
    save(state_path, state)
    save(out/"core-receipt.json", {
        "complete": True, "p": P, "model_degree": M,
        "certificate_sha256": sha(out/"p41-original-CM-model-certificate.json"),
        "state_sha256": sha(state_path), "source_sha256": sha(__file__),
        "original_map_or_beta_computed": False})
    return certificate


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Exact task computation is restricted to the public repository Actions.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        result = compute(args.output)
        print(json.dumps({"complete": True, "p": P, "degree": M,
                          "seconds": result["seconds"]}), flush=True)
        return 0
    except BaseException as error:
        save(args.output/"core-receipt.json", {
            "complete": False, "p": P, "source_sha256": sha(__file__),
            "error": type(error).__name__ + ": " + str(error),
            "original_map_or_beta_computed": False})
        raise


if __name__ == "__main__":
    sys.exit(main())
