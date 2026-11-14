#!/usr/bin/env python3
"""Exact finite-field and PARI/GP certificate for R99; no optional packages.

Run with --write to regenerate the adjacent JSON, or --check to compare it.
The GP computation uses exact modular-form and number-field arithmetic.
No class group, GRH, floating-point recognition, or cached eigenform data is used.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True

PRIMES = (11, 13, 23, 37, 47, 59, 61, 71, 73, 83, 97)
DEFAULT_CERTIFICATE = Path(__file__).with_name("r99_d3_multifrey_certificate.json")


def legendre(a: int, q: int) -> int:
    z = pow(a % q, (q - 1) // 2, q)
    return -1 if z == q - 1 else z


def trace(q: int, a2: int, a4: int, a6: int = 0) -> int:
    return -sum(legendre(x**3 + a2*x*x + a4*x + a6, q)
                for x in range(q))


def finite_field_data() -> list[dict]:
    rows = []
    for q in PRIMES:
        assert all(q % t for t in range(2, math.isqrt(q) + 1))
        roots = [t for t in range(q) if t*t % q == 3]
        assert len(roots) == 2
        inv2, inv4 = pow(2, -1, q), pow(4, -1, q)
        ta = trace(q, 0, -1)
        allowed = []
        for a, b in [(a, 1) for a in range(q)] + [(1, 0)]:
            quartic = a**4 - 18*a*a*b*b - 27*b**4
            T = quartic * inv4 % q
            if not T:
                continue
            X = (T + 9*a*a*b*b) % q
            W = a*b*(a**4 + 27*b**4)*inv4 % q
            assert (X**3 - 27*W*W - T**3) % q == 0
            te = trace(q, 0, -4*X, -16*W)
            teminus = trace(q, 0, -4*X, 16*W)
            assert (te == ta) == (teminus == ta)
            if te != ta:
                continue
            h = (a*a + 3*b*b)*inv2 % q
            tb = [trace(q, 4*a, 2*(a*a + r*h)) for r in roots]
            assert tb[0]**2 == tb[1]**2
            allowed.append([a, b, tb[0]])
        squares = sorted({t*t for _, _, t in allowed})
        tb0 = trace(q, 4, 2 + roots[0])
        tc0 = legendre(1 + roots[0], q)*tb0
        assert [1, 0, tb0] in allowed
        assert tb0**2 in squares
        rows.append({"q": q, "sqrt3": roots[0], "trace_A": ta,
                     "trace_squares_B": squares,
                     "projective_representatives": allowed,
                     "trace_B0": tb0, "trace_C0": tc0})
    return rows


def gp_program(rows: list[dict]) -> str:
    checks = [[r["q"], r["trace_squares_B"]] for r in rows]
    return r'''
default(parisizemax,400000000);
''' + "checks=" + json.dumps(checks) + ";\n" + r'''
print("VERSION|",version());
M=mfinit([768,2,12],0); E=mfeigenbasis(M);
print("SPACE|",mfdim(M),"|",#E);
for(j=1,#E, my(f=E[j], P=mfparams(f)[4], c=mfcoefs(f,97), g=0, ds=vector(#checks)); for(i=1,#checks,my(q=checks[i][1],S=checks[i][2],a=c[q+1],v=q); for(k=1,#S,v*=norm(Mod(lift(a^2-S[k]),P))); ds[i]=v; g=gcd(g,v); print("COEF|",j,"|",q,"|",lift(a))); print("FORM|",j,"|",P,"|",mfisCM(f),"|",g,"|",ds));
K=nfinit(y^2-3); r=Mod(y,y^2-3); u=1+r; P2=idealprimedec(K,2)[1];
print("CHI_DISC|",nfdisc(x^4-2*x^2-2));
print("CHI_HILBERT|",[nfhilbert(K,u,r,P2),nfhilbert(K,u,1+2*r,P2),nfhilbert(K,u,-1,P2)]);
print("IRRED_UNIT|",norm((2+r)^12-1));
print("IRRED_RESULTANT|",polresultant(x^2-2*x+3,x^12-1));
B0=ellinit([0,4,0,2+r,0],K);
print("B0_J|",lift(B0.j)); print("B0_J_POLY|",minpoly(B0.j));
for(i=1,4,my(d=[1,-1,2,-2][i],C=ellinit([0,4*u*d,0,u^2*(2+r)*d^2,0],K),R=elllocalred(C,P2),Cmin=ellchangecurve(C,R[3])); print("C0_LOCAL|",d,"|",R[1],"|",R[2],"|",idealval(K,Cmin.disc,P2),"|",R[4]));
for(i=1,3,my(a=[1,5,7][i],b=3,h=(a^2+3*b^2)/2,C=ellinit([0,4*a*u,0,2*u^2*(a^2+r*h),0],K),R=elllocalred(C,P2),Cmin=ellchangecurve(C,R[3])); print("ACTUAL_LOCAL_SAMPLE|",a,"|",b,"|",R[1],"|",R[2],"|",idealval(K,Cmin.disc,P2)));
quit
'''


def gp_data(gp: str, rows: list[dict]) -> dict:
    proc = subprocess.run([gp, "-fq"], input=gp_program(rows), text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          check=False)
    errors = [line for line in proc.stderr.splitlines()
              if "***" in line and "Warning:" not in line]
    if proc.returncode or errors:
        raise RuntimeError("PARI/GP failed:\n" + proc.stdout + proc.stderr)
    data = {"forms": [], "C0_at_P2": [], "local_samples": []}
    coefs = {}
    for raw in proc.stdout.splitlines():
        fields = raw.strip().split("|")
        key = fields[0]
        if key == "VERSION":
            # The exact data below, rather than the installed version, is compared.
            data["pari_version_used"] = json.loads(fields[1])
        elif key == "SPACE":
            data["dimension"], data["orbit_count"] = map(int, fields[1:])
        elif key == "COEF":
            j, q = map(int, fields[1:3])
            coefs.setdefault(j, {})[str(q)] = fields[3]
        elif key == "FORM":
            j = int(fields[1])
            data["forms"].append({"index": j, "coefficient_polynomial": fields[2],
                                  "CM_discriminant": int(fields[3]),
                                  "gcd_Dq": int(fields[4]),
                                  "Dq_in_prime_order": json.loads(fields[5]),
                                  "coefficients": coefs[j]})
        elif key in ("CHI_DISC", "IRRED_UNIT", "IRRED_RESULTANT"):
            data[key.lower()] = int(fields[1])
        elif key == "CHI_HILBERT":
            data[key.lower()] = json.loads(fields[1])
        elif key in ("B0_J", "B0_J_POLY"):
            data[key.lower()] = fields[1]
        elif key == "C0_LOCAL":
            data["C0_at_P2"].append(dict(zip(
                ("d", "conductor_exponent", "pari_kodaira_code",
                 "minimal_discriminant_valuation", "tamagawa"),
                map(int, fields[1:]))))
        elif key == "ACTUAL_LOCAL_SAMPLE":
            data["local_samples"].append(list(map(int, fields[1:])))
        elif raw.strip():
            raise RuntimeError("Unexpected GP output: " + raw)
    assert (data["dimension"], data["orbit_count"]) == (28, 10)
    assert [f["gcd_Dq"] for f in data["forms"]] == [
        2**12, 0, 0, 2**12, 0, 0, 2**24, 2**24, 2**24, 2**28]
    assert [f["CM_discriminant"] for f in data["forms"]] == [
        -8, 0, 0, -8, 0, 0, -8, -24, -24, -3]
    assert data["chi_disc"] == -4608
    assert data["chi_hilbert"] == [-1, 1, -1]
    assert data["irred_unit"] == -7300800
    assert data["irred_resultant"] == 530784
    for row in data["C0_at_P2"]:
        assert (row["conductor_exponent"], row["pari_kodaira_code"],
                row["minimal_discriminant_valuation"]) == (12, -6, 18)
    assert data["local_samples"] == [
        [1,3,12,2,12], [5,3,12,2,12], [7,3,12,2,12]]
    # Identify each rational twist by two exact split-prime coefficients.
    twists = []
    for d in (1, -1, 2, -2):
        wanted = {str(q): str(legendre(d,q)*next(
            r["trace_C0"] for r in rows if r["q"] == q)) for q in (11,13)}
        matches = [f["index"] for f in data["forms"] if all(
            f["coefficients"][q] == a for q,a in wanted.items())]
        assert len(matches) == 1
        twists.append({"d": d, "orbit_index": matches[0]})
    assert twists == [{"d":1,"orbit_index":5}, {"d":-1,"orbit_index":3},
                      {"d":2,"orbit_index":2}, {"d":-2,"orbit_index":6}]
    data["twist_identification"] = twists
    return data


def build_certificate(gp: str) -> dict:
    rows = finite_field_data()
    return {"schema": "R99-d3-multifrey-v1", "level": 768,
            "weight": 2, "nebentypus_Kronecker_discriminant": 12,
            "definition_Dq": "q * product_s Norm(a_q(f)^2-s)",
            "finite_fields": rows, "exact_pari": gp_data(gp, rows)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gp", default=shutil.which("gp"))
    ap.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    modes = ap.add_mutually_exclusive_group()
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    ap.add_argument("--finite-only", action="store_true")
    args = ap.parse_args()
    if args.finite_only:
        print(json.dumps(finite_field_data(), ensure_ascii=False, indent=2))
        return
    if not args.gp:
        ap.error("PARI/GP is required; supply --gp /path/to/gp")
    result = build_certificate(args.gp)
    if args.write:
        args.certificate.write_text(json.dumps(result, ensure_ascii=False,
                                              indent=2) + "\n")
        print("Wrote", args.certificate)
    else:
        saved = json.loads(args.certificate.read_text())
        saved["exact_pari"]["pari_version_used"] = result["exact_pari"]["pari_version_used"]
        assert result == saved, "Recomputed certificate differs"
        print("R99: all finite-field, modular-form, conductor and twist data match")
    print("dimension 28; 10 orbits; 6 excluded for every p>37; 4 fixed non-CM twists remain")


if __name__ == "__main__":
    main()
