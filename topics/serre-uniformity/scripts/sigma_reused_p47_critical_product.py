#!/usr/bin/env python3
"""Convert seven products from the retained R702 p47 ordinary derivatives."""
import os

if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("This fixed consumer runs only in the public repository GitHub Actions.")

import hashlib
import json
from math import factorial, prod
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[3]
TOPIC = REPO / "topics/serre-uniformity"
REQUEST = TOPIC / "notes/sigma-reused-p47-critical-product-request.json"
RESULT = "reused-R702-p47-seven-critical-products"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def git_blob(path):
    data = Path(path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()


def main():
    request = json.loads(REQUEST.read_text(encoding="utf-8"))
    job = request["job"]
    assert job["result"] == RESULT and job["prime"] == 47
    assert job["scope"] == "seven_products_from_existing_A_only"
    assert Path(__file__).resolve() == REPO / job["core"]
    for key in ("core", "wrapper", "workflow", "upstream_data", "upstream_formula"):
        relative = Path(job[key])
        assert not relative.is_absolute() and ".." not in relative.parts
        assert git_blob(REPO / relative) == job[key + "_git_blob"]
    upstream_path = REPO / job["upstream_data"]
    upstream = json.loads(upstream_path.read_text(encoding="utf-8"))
    assert upstream["prime"] == 47
    assert upstream["result"] == "R702-independent-Bell-check"
    assert upstream["ordinary_derivatives_used"] is True
    assert upstream["division_by_p_used"] is False
    assert upstream["source_sha256"] == job["upstream_arithmetic_sha256"]
    rows = upstream["every_allowed_t_checked"]
    assert [row["t"] for row in rows] == list(range(2, 45, 3))
    p = upstream["prime"]
    A = {row["t"]: row["A_t"] for row in rows}
    assert all(type(value) is int and 0 <= value < p for value in A.values())
    N = (p - 5) // 6
    common = pow(2, (p - 7) // 2, p)
    products = []
    for i in range(N):
        j = N - 1 - i
        m1, m2 = 6 * i + 4, 6 * j + 1
        h = 6 * i + 7
        assert m1 + m2 == p - 6 and m1 + 1 == h - 2 and m2 + 1 == p - h - 2
        assert 0 <= m1 < p and 0 <= m2 < p
        q_h = prod(h + offset for offset in range(-2, 3)) % p
        direct = (pow(2, m1 // 2 + (m2 - 1) // 2, p)
                  * A[m1 + 1] * A[m2 + 1]
                  * pow((factorial(m1) * factorial(m2)) % p, -1, p)) % p
        wilson = common * q_h * A[m1 + 1] * A[m2 + 1] % p
        assert direct == wilson
        products.append({"i": i, "j": j, "h": h,
            "first_A_index": m1 + 1, "second_A_index": m2 + 1,
            "first_retained_A": A[m1 + 1], "second_retained_A": A[m2 + 1],
            "Q_h_mod_p": q_h, "f_i_g_j": wilson,
            "factorial_formula_checked": True, "alternating_sign": (-1) ** j})
    alternating = sum(row["alternating_sign"] * row["f_i_g_j"] for row in products) % p
    output = {"result": RESULT, "prime": p, "N": N, "source_sha256": digest(__file__),
        "source_commit": os.environ["GITHUB_SHA"], "run_id": os.environ["GITHUB_RUN_ID"],
        "run_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "repository": os.environ["GITHUB_REPOSITORY"],
        "upstream_file": job["upstream_data"], "upstream_git_blob": git_blob(upstream_path),
        "upstream_file_sha256": digest(upstream_path),
        "upstream_arithmetic_sha256": upstream["source_sha256"],
        "formula_file": job["upstream_formula"],
        "formula_git_blob": job["upstream_formula_git_blob"],
        "common_Wilson_multiplier": common, "products": products,
        "alternating_critical_convolution": alternating,
        "alternating_critical_convolution_nonzero": alternating != 0,
        "B_from_existing_source": upstream["B"],
        "original_apolar_scale": pow(6 * upstream["B"], 5, p),
        "new_A_or_f_or_g_series_generated": False, "new_primes": [],
        "primitive_or_Legendre_weights_computed": False,
        "all_inert_primes_nonzero_claimed": False}
    destination = Path(sys.argv[1])
    destination.write_text(json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True, indent=2))
    print("RESULT_SHA256=" + hashlib.sha256(canonical(output)).hexdigest())


if __name__ == "__main__":
    main()
