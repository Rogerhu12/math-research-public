#!/usr/bin/env python3
"""R94: compute the complete 53-direction Chow--Heegner translation at p=41.

PARI constructs the actual modular-symbol spaces. All CM coefficient sums,
the finite commuting-involution correspondence, and the stored certificate
use exact integers/rationals. This does not compute auxiliary local heights.
"""

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
import tempfile

from p41_jacobi_cm_coordinates import positive_divisors, gp_polynomial

P, LEVEL, AUXILIARY, AUXILIARY_ROOT = 41, 1681, -43, 1219


def legendre(a, p=P):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p-1)//2, p) == 1 else -1)


def squarefree(n):
    return all(n % (d*d) for d in range(2, math.isqrt(n)+1))


def hurwitz_degree(discriminant):
    """All reduced positive forms, including imprimitive ones, with weight 1/u."""
    assert discriminant < 0 and discriminant % 4 in (0, 1)
    result = Fraction(0)
    for a in range(1, math.isqrt((-discriminant)//3)+1):
        for b in range(-a, a+1):
            if (b*b-discriminant) % (4*a):
                continue
            c = (b*b-discriminant)//(4*a)
            if a > c or ((abs(b) == a or a == c) and b < 0):
                continue
            units = 3 if a == b == c else 2 if b == 0 and a == c else 1
            result += Fraction(1, units)
    return result


def add_degree_metadata(metadata, traces):
    for record, trace in zip(metadata, traces[1:]):
        valency = sum(positive_divisors(record["n"]))
        divisor_degree = 2*valency-2*trace
        common = math.gcd(54, trace)
        a, b = 54//common, -trace//common
        cm_degree = 2*sum((hurwitz_degree(D) for D in record["positive_trace_discriminants"]), Fraction(0))
        cm_degree += (22 if record["trace_zero_inert"] else 20)*hurwitz_degree(-4*record["n"])
        cusp_coefficient = (divisor_degree-cm_degree)/20
        assert cusp_coefficient.denominator == 1 and cusp_coefficient >= 0
        assert 54*b+a*trace == 0
        assert a*divisor_degree-b*106 == 2*(a*valency+b)
        record.update({"hecke_degree": valency, "trace": trace,
                       "diagonal_divisor_degree": divisor_degree,
                       "weighted_CM_degree": [cm_degree.numerator, cm_degree.denominator],
                       "cusp_divisor_coefficient": int(cusp_coefficient),
                       "F_Tn_coefficient": a, "F_identity_coefficient": b,
                       "G_multiplier": 2, "xi_nu_coefficient": 2*a,
                       "xi_KD_coefficient": -2*b,
                       "F_correspondence_valency": a*valency+b})


def hecke_indices():
    # n=43 alone would violate RSST's nonsquare condition with Delta0=-43.
    return [n for n in range(1, 92) if n % P and n != 43 and squarefree(n)]


def involution_correspondence():
    nonsquares = [d for d in range(1, P) if legendre(d) == -1]
    necklaces = [(a, d) for a in range(P) for d in nonsquares]
    all_pairs = [(a, b) for a in range(P+1) for b in range(a+1, P+1)]
    pair_index = {pair: i for i, pair in enumerate(all_pairs)}
    masks, neighbors = [], []
    for a, d in necklaces:
        pairs = {(a, P)}
        for x in range(P):
            if x != a:
                y = (a+d*pow((x-a) % P, -1, P)) % P
                if x < y:
                    pairs.add((x, y))
        assert len(pairs) == 21
        masks.append(sum(1 << pair_index[pair] for pair in pairs))
        neighbors.append([j for j, (b, e) in enumerate(necklaces)
                          if (a, d) != (b, e) and (d+e-(a-b)**2) % P == 0])
        assert len(neighbors[-1]) == 21
    adjacency = [sum(1 << j for j in row) for row in neighbors]
    for i in range(len(necklaces)):
        for j in range(i, len(necklaces)):
            assert ((adjacency[i] & adjacency[j]).bit_count()+
                    (masks[i] & masks[j]).bit_count()) == (P+1 if i == j else 1)
    weights = [0]*len(all_pairs)
    for i, (a, d) in enumerate(necklaces):
        if a == 0:
            for j in [i]+neighbors[i]:
                mask = masks[j]
                while mask:
                    low = mask & -mask
                    weights[low.bit_length()-1] += 2
                    mask -= low
    output = [[a, b, weight] for (a, b), weight in zip(all_pairs, weights) if weight]
    assert len(output) == 841 and sum(x[2] for x in output) == 18480
    assert weights[pair_index[(0, P)]] == 80
    return output


def paths_from_infinity(x):
    if x is None:
        return []
    n, d = x.numerator, x.denominator
    pp, pq, qp, qq = 0, 1, 1, 0
    output, previous = [], None
    while d:
        a = n//d
        n, d = d, n-a*d
        h, k = a*pq+pp, a*qq+qp
        current = Fraction(h, k)
        output.append((previous, current))
        previous = current
        pp, pq, qp, qq = pq, h, qq, k
    assert previous == x
    return output


def contract_paths(matrices):
    edge_index, edges, rows = {}, [], []

    def add_edge(start, end, coefficient, row):
        if start == end:
            return
        if end is not None and (start is None or end < start):
            start, end, coefficient = end, start, -coefficient
        key = (start, end)
        if key not in edge_index:
            A, C = (1, 0) if end is None else (end.numerator, end.denominator)
            B, D = (1, 0) if start is None else (start.numerator, start.denominator)
            determinant = A*D-B*C
            assert abs(determinant) == 1
            if determinant == -1:
                B, D = -B, -D
            edge_index[key] = len(edges)
            edges.append([A, B, C, D])
        index = edge_index[key]
        row[index] = row.get(index, 0)+coefficient

    for A, B, C, D in matrices:
        row = {}
        start = None if D == 0 else Fraction(P*B, D)
        end = None if C == 0 else Fraction(P*A, C)
        for coefficient, point in ((-1, start), (1, end)):
            for left, right in paths_from_infinity(point):
                add_edge(left, right, coefficient, row)
        rows.append([[i, c] for i, c in sorted(row.items()) if c])
    assert len(edges) == 970 and sum(abs(c) for row in rows for _, c in row) == 1403
    return edges, rows


def indefinite_forms(discriminant):
    assert discriminant > 0 and math.isqrt(discriminant)**2 != discriminant
    for b in range(-math.isqrt(discriminant), math.isqrt(discriminant)+1):
        if (discriminant-b*b) % 4:
            continue
        n = (discriminant-b*b)//4
        if n <= 0:
            continue
        for a in positive_divisors(n):
            c = -n//a
            chi = legendre(a, 43) if a % 43 else legendre(c, 43)
            yield a, b, c, chi


def contracted_coefficient(D, edges, rows):
    assert D < 0 and D % 4 in (0, 1) and legendre(D) == -1
    modulus, target = 2*P, P*(D % 2)
    linear = [((-2*d*b) % modulus, (d*a+b*c) % modulus, (-2*c*a) % modulus)
              for a, b, c, d in edges]
    values = [0]*len(edges)
    forms = 0
    for a, b, c, chi in indefinite_forms(AUXILIARY*D):
        forms += 1
        if chi:
            a, b, c = a % modulus, b % modulus, c % modulus
            for i, (l1, l2, l3) in enumerate(linear):
                if (l1*a+l2*b+l3*c-target) % modulus == 0:
                    values[i] -= 2*chi
    result = [sum(c*values[i] for i, c in row) for row in rows]
    assert result[-2:] == [0, 0]
    return result, forms


def direct_coefficient(D, r, matrices):
    assert (r*r-D) % (4*LEVEL) == 0
    target = r*AUXILIARY_ROOT % (2*LEVEL)
    linear = [(d*d, -d*c, c*c, -2*d*b, d*a+b*c, -2*c*a)
              for a, b, c, d in matrices]
    values = [0]*len(matrices)
    forms = 0
    for a, b, c, chi in indefinite_forms(AUXILIARY*D):
        forms += 1
        if chi:
            for i, (l1, l2, l3, l4, l5, l6) in enumerate(linear):
                if (l1*a+l2*b+l3*c) % LEVEL:
                    continue
                B = (l4*a+l5*b+l6*c) % (2*LEVEL)
                values[i] -= chi*(int(B == target)+int(B == -target % (2*LEVEL)))
    assert values[-2:] == [0, 0]
    return values, forms


def raw_translation_rows(indices, matrices):
    edges, path_rows = contract_paths(matrices)
    inert_targets = {-3}
    split_targets = {}
    for n in indices[1:]:
        for t in range(1, math.isqrt(4*n)+1):
            D = t*t-4*n
            if D < 0 and legendre(D) == -1:
                inert_targets.add(D)
        D = -4*n
        if legendre(D) == -1:
            inert_targets.add(D)
        else:
            split_targets[D] = next(r for r in range(2*LEVEL) if (r*r-D) % (4*LEVEL) == 0)
    assert len(inert_targets) == 90 and len(split_targets) == 25
    inert, split, counts = {}, {}, []
    for i, D in enumerate(sorted(inert_targets), 1):
        inert[D], count = contracted_coefficient(D, edges, path_rows)
        counts.append([D, LEVEL if D % 2 else 0, count, "contracted"])
        if i % 15 == 0:
            print(f"R94: contracted CM coefficients {i}/{len(inert_targets)}.", flush=True)
    for D, r in sorted(split_targets.items()):
        split[D], count = direct_coefficient(D, r, matrices)
        counts.append([D, r, count, "direct"])
    reference, reference_count = direct_coefficient(-4, 756, matrices)
    rows = [reference, inert[-3]]
    metadata = []
    for n in indices[1:]:
        positive = [0]*289
        discriminants = []
        for t in range(1, math.isqrt(4*n)+1):
            D = t*t-4*n
            if D < 0 and legendre(D) == -1:
                discriminants.append(D)
                positive = [a+2*b for a, b in zip(positive, inert[D])]
        at_zero = -4*n
        if legendre(at_zero) == -1:
            rows.extend([positive, inert[at_zero], [0]*289])
        else:
            rows.extend([positive, [0]*289, split[at_zero]])
        metadata.append({"n": n, "positive_trace_discriminants": discriminants,
                         "trace_zero_inert": legendre(at_zero) == -1})
    assert len(rows) == 161
    return rows, metadata, counts


def run_stage(gp, source, work, function):
    command = f"read({json.dumps(str(source))});\n{function}({json.dumps(str(work))});\nquit;\n"
    result = subprocess.run([gp, "-q", "-f", "-s", "536870912"], input=command,
                            capture_output=True, text=True, timeout=600, check=True)
    if "***" in result.stderr:
        raise RuntimeError(result.stderr)
    print(result.stdout.strip(), flush=True)


def main():
    script = Path(__file__).resolve()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gp", default=shutil.which("gp") or "/tmp/pari-2.19.0/gp")
    parser.add_argument("--output", type=Path,
                        default=script.with_name("data")/"p41_full_chow_heegner_certificate.json.gz")
    args = parser.parse_args()
    data_dir = script.with_name("data")
    references = {}
    for key, name in (("jacobi", "p41_jacobi_cm_certificate.json"),
                      ("inert", "p41_inert_cm_certificate.json"),
                      ("hecke", "p41_cm_ratio_certificate.json")):
        file = data_dir/name
        references[key] = (file, json.loads(file.read_text()))
    weights = involution_correspondence()
    indices = hecke_indices()
    assert len(indices) == 54
    with tempfile.TemporaryDirectory(prefix="serre-p41-chow-") as temp:
        work = Path(temp)
        (work/"Sweights.gp").write_text(json.dumps(weights)+"\n")
        (work/"indices.gp").write_text(json.dumps(indices)+"\n")
        prior = references["jacobi"][1]
        reference = [json.dumps(references["hecke"][1]["six_times_hecke_matrix"]),
                     json.dumps(references["inert"][1]["polarization_row_exact"]),
                     "["+",".join(gp_polynomial(f, "xiG") for f in prior["fields"])+"]",
                     "["+",".join(gp_polynomial(f, "r3") for f in prior["fields"])+"]"]
        (work/"reference.gp").write_text("["+",".join(reference)+"]\n")
        run_stage(args.gp, script.with_name("p41_jacobi_cm_coordinates.gp"), work, "p41_jacobi_setup")
        run_stage(args.gp, script.with_suffix(".gp"), work, "p41_chow_setup")
        matrices = json.loads((work/"paths.json").read_text())
        assert matrices == prior["path_matrices"]
        rows, metadata, counts = raw_translation_rows(indices, matrices)
        assert rows[0] == prior["raw_coefficients"][0]["values"]
        assert rows[1] == prior["raw_coefficients"][2]["values"]
        (work/"chow_rows.gp").write_text(json.dumps(rows)+"\n")
        run_stage(args.gp, script.with_suffix(".gp"), work, "p41_chow_project")
        source = json.loads((work/"source.json").read_text())
        projection = json.loads((work/"chow_projection.json").read_text())
    fields = []
    for item in projection.pop("field_data"):
        fields.append({"factor_descending": item[0], "S": item[1],
                       "raw_ratios": item[2], "directions": item[3]})
    add_degree_metadata(metadata, source["hecke_traces"])
    result = {"result": "R94", "p": P, "level": LEVEL, "d": 20, "genus": 54,
              "canonical_divisor_degree": 106,
              "canonical_KD_B4_U3_coefficients": [[-10, 1], [-2, 3]],
              "auxiliary_discriminant": AUXILIARY, "auxiliary_root": AUXILIARY_ROOT,
              "actual_full_trace_zero_Hecke_space": True, "indices": indices,
              "S_pair_weights": weights, "raw_translation_rows": rows,
              "row_metadata": metadata, "coefficient_enumeration_counts": counts,
              **source, **projection, "fields": fields}
    for key, (file, _) in references.items():
        result[f"{key}_reference"] = file.name
        result[f"{key}_reference_sha256"] = hashlib.sha256(file.read_bytes()).hexdigest()
    encoded = (json.dumps(result, separators=(",", ":"), sort_keys=True)+"\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(gzip.compress(encoded, mtime=0))
    print(f"Saved {args.output}: {len(encoded)} raw bytes, {args.output.stat().st_size} compressed bytes.")
    print("SHA256", hashlib.sha256(args.output.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
