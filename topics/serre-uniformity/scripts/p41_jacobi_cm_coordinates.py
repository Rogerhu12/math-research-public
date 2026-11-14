#!/usr/bin/env python3
"""R89: generate the actual signed CM coordinates, with PARI/GP 2.19.

The finite quadratic-form enumeration uses only Python integers. PARI builds
the actual star-plus, new, Fricke-plus modular-symbol space and projects the
intersection functionals onto it. No approximate periods or heights occur.
"""

import argparse
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
import tempfile


def positive_divisors(n):
    out = []
    for d in range(1, math.isqrt(n)+1):
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
    return out


def enumerate_coefficients(matrices):
    """RSST Theorem 4.15, k=2, Delta0=-43; free paths go from g0 to g∞."""
    level, auxiliary, auxiliary_root = 1681, -43, 1219
    assert (auxiliary_root**2-auxiliary) % (4*level) == 0
    legendre = [0 if a == 0 else (1 if pow(a, 21, 43) == 1 else -1)
                for a in range(43)]
    linear = []
    for a, b, c, d in matrices:
        assert a*d-b*c == 1
        linear.append((d*d, -d*c, c*c, -2*d*b, d*a+b*c, -2*c*a))
    output = []
    for delta, r in ((-4, 756), (-8, 142), (-3*level, level), (-7*level, level)):
        assert (r*r-delta) % (4*level) == 0
        target = r*auxiliary_root % (2*level)
        discriminant = delta*auxiliary
        assert math.isqrt(discriminant)**2 != discriminant
        values = [0]*len(matrices)
        total, hits = 0, 0
        for b in range(-math.isqrt(discriminant), math.isqrt(discriminant)+1):
            if (discriminant-b*b) % 4:
                continue
            n = (discriminant-b*b)//4
            if n <= 0:
                continue
            for a in positive_divisors(n):
                c = -n//a
                total += 1
                chi = legendre[a % 43] if a % 43 else legendre[c % 43]
                if not chi:
                    continue
                for i, (l1, l2, l3, l4, l5, l6) in enumerate(linear):
                    A = l1*a+l2*b+l3*c
                    if A % level:
                        continue
                    B = (l4*a+l5*b+l6*c) % (2*level)
                    # Q and -Q have opposite genus characters and intersection
                    # numbers. At r=level both conditions hold; count both.
                    count = int(B == target)+int(B == -target % (2*level))
                    values[i] -= count*chi
                    hits += count
        assert values[-2:] == [0, 0]
        output.append({"delta": delta, "r": r, "product_discriminant": discriminant,
                       "positive_a_forms": total, "hits": hits,
                       "nonzero_paths": sum(v != 0 for v in values), "values": values})
    return output


def gp_polynomial(item, name):
    coefficients = item[f"{name}_numerator_descending"]
    degree = len(coefficients)-1
    terms = "+".join(f"({n})*x^{degree-i}" for i, n in enumerate(coefficients))
    return f"({terms})/{item[f'{name}_denominator']}"


def run_gp(gp, source, work, function):
    command = f"read({json.dumps(str(source))});\n{function}({json.dumps(str(work))});\nquit;\n"
    result = subprocess.run([gp, "-q", "-f", "-s", "536870912"], input=command, text=True,
                            capture_output=True, timeout=180, check=True)
    if "***" in result.stderr:
        raise RuntimeError(result.stderr)
    print(result.stdout.strip(), flush=True)


def main():
    script = Path(__file__).resolve()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gp", default=shutil.which("gp") or "/tmp/pari-2.19.0/gp")
    parser.add_argument("--output", type=Path,
                        default=script.with_name("data")/"p41_jacobi_cm_certificate.json")
    args = parser.parse_args()
    data_dir = script.with_name("data")
    inert_path = data_dir/"p41_inert_cm_certificate.json"
    split_path = data_dir/"p41_cm_ratio_certificate.json"
    inert = json.loads(inert_path.read_text())
    split = json.loads(split_path.read_text())
    with tempfile.TemporaryDirectory(prefix="serre-p41-jacobi-") as temp:
        work = Path(temp)
        run_gp(args.gp, script.with_suffix(".gp"), work, "p41_jacobi_setup")
        matrices = json.loads((work/"paths.json").read_text())
        coefficients = enumerate_coefficients(matrices)
        for row in coefficients:
            print(f"Delta={row['delta']}, r={row['r']}: {row['positive_a_forms']} forms, "
                  f"{row['hits']} signed hits, {row['nonzero_paths']} nonzero paths.", flush=True)
        (work/"rows.gp").write_text(json.dumps([item["values"] for item in coefficients])+"\n")
        reference = []
        for left, right in zip(inert["fields"], split["fields"]):
            assert left["factor_descending"] == right["factor_descending"]
            reference.append("["+json.dumps(left["factor_descending"])+","+
                             ",".join([gp_polynomial(left, "kappa"), gp_polynomial(left, "root3"),
                                       gp_polynomial(left, "root7"), gp_polynomial(right, "root")])+"]")
        (work/"reference.gp").write_text("["+",".join(reference)+"]\n")
        run_gp(args.gp, script.with_suffix(".gp"), work, "p41_jacobi_project")
        projection = json.loads((work/"projection.json").read_text())
    fields = []
    for item in projection.pop("field_data"):
        field = {"factor_descending": item[0]}
        names = ("jacobi8_ratio", "jacobi3p2_ratio", "jacobi7p2_ratio", "s8", "r3", "r7", "xiG")
        for name, (denominator, numerator) in zip(names, item[1:8]):
            field[f"{name}_denominator"] = denominator
            field[f"{name}_numerator_descending"] = numerator
        field["signs_relative_R85_R79_r3_r7_s8"] = item[8]
        fields.append(field)
    result = {
        "result": "R89", "level": 1681, "weight": 2, "star": 1, "fricke": 1,
        "new": True, "auxiliary_discriminant": -43, "auxiliary_root": 1219,
        "reference_CM_pair": [-4, 756], "actual_point_signs": True,
        "inert_reference": inert_path.name,
        "inert_reference_sha256": hashlib.sha256(inert_path.read_bytes()).hexdigest(),
        "split_reference": split_path.name,
        "split_reference_sha256": hashlib.sha256(split_path.read_bytes()).hexdigest(),
        "generator_path_count": 289, "free_path_count": 287, "elliptic_zero_path_count": 2,
        "path_matrices": matrices, "raw_coefficients": coefficients,
        **projection, "fields": fields,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, separators=(",", ":"))+"\n")
    print(f"Saved {args.output}; SHA256 {hashlib.sha256(args.output.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
