#!/usr/bin/env python3
"""R739: reuse completed p47 fibers and p41 integer traces for exact local algebra.

This program never enumerates finite-field fibers, lattice points, or DFTs.
The two retained certificates fix the original generators and character labels.
A nonzero exact cyclotomic norm supplies a sufficient finite p-adic precision.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import time
import traceback
from p41_public_actions_recovery import REPO, TOPIC, publish

HERE = Path(__file__).resolve().parent
RESULT = "R739-reused-cyclotomic-valuations"
REQUEST = TOPIC / "notes/R739-cyclotomic-reuse-request.json"
WORKFLOW = REPO / ".github/workflows/serre-R739-cyclotomic-reuse.yml"
FINAL = "R739-reused-exact-valuations.json"
AUDIT = "R739-cyclotomic-integer-audit.json.gz"
SESSION = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "R739-cyclotomic-session.json"

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read(path):
    return json.loads(Path(path).read_text())

def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".next")
    temporary.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")
    temporary.replace(path)

def archive(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as raw:
        with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as stream:
            stream.write(data)

def valuation(n, p):
    n = abs(int(n))
    assert n != 0
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result

def remainder(coefficients, monic):
    coefficients = [int(x) for x in coefficients]
    monic = [int(x) for x in monic]
    degree = len(monic)-1
    assert degree >= 1 and monic[-1] == 1
    coefficients += [0] * max(0, degree-len(coefficients))
    for i in range(len(coefficients)-1, degree-1, -1):
        leading = coefficients[i]
        for j in range(degree+1):
            coefficients[i-degree+j] -= leading*monic[j]
        assert coefficients[i] == 0
    return coefficients[:degree]

def bareiss(matrix):
    work = [row[:] for row in matrix]
    degree = len(work)
    assert degree and all(len(row) == degree for row in work)
    sign, previous, pivots = 1, 1, []
    for k in range(degree-1):
        row = next((j for j in range(k, degree) if work[j][k]), None)
        if row is None:
            return 0, pivots
        if row != k:
            work[k], work[row] = work[row], work[k]
            sign = -sign
        pivot = work[k][k]
        pivots.append({"step": k, "row": row, "pivot": str(pivot),
                       "exact_divisor": str(previous)})
        for i in range(k+1, degree):
            for j in range(k+1, degree):
                numerator = work[i][j]*pivot-work[i][k]*work[k][j]
                quotient, residue = divmod(numerator, previous)
                assert residue == 0
                work[i][j] = quotient
        for i in range(k+1, degree):
            work[i][k] = 0
        previous = pivot
    return sign*work[-1][-1], pivots

def modular_determinant(matrix, prime):
    work = [[x % prime for x in row] for row in matrix]
    answer = 1
    for k in range(len(work)):
        row = next((j for j in range(k, len(work)) if work[j][k]), None)
        if row is None:
            return 0
        if row != k:
            work[k], work[row] = work[row], work[k]
            answer = -answer
        pivot = work[k][k]
        answer = answer*pivot % prime
        inverse = pow(pivot, -1, prime)
        for i in range(k+1, len(work)):
            factor = work[i][k]*inverse % prime
            for j in range(k, len(work)):
                work[i][j] = (work[i][j]-factor*work[k][j]) % prime
    return answer % prime

def cyclotomic_norm(coefficients, cyclotomic, prime):
    reduced = remainder(coefficients, cyclotomic)
    degree = len(cyclotomic)-1
    columns = [remainder([0]*j+reduced, cyclotomic) for j in range(degree)]
    matrix = [[columns[j][i] for j in range(degree)] for i in range(degree)]
    determinant, pivots = bareiss(matrix)
    assert determinant != 0, "Unexpected zero conflicts with the retained nonzero conjugate"
    modular_checks = []
    for auxiliary in (1000000007, 1000000009):
        check = modular_determinant(matrix, auxiliary)
        assert check == determinant % auxiliary
        modular_checks.append({"prime": auxiliary, "determinant_mod_prime": check})
    norm_valuation = valuation(determinant, prime)
    audit = {"cyclotomic_coefficients_ascending": [str(x) for x in cyclotomic],
             "input_coefficients_ascending": [str(x) for x in coefficients],
             "remainder_coefficients_ascending": [str(x) for x in reduced],
             "multiplication_matrix_rows": [[str(x) for x in row] for row in matrix],
             "bareiss_pivots": pivots, "exact_norm": str(determinant),
             "valuation_exact_norm": norm_valuation,
             "modular_determinant_checks": modular_checks}
    return reduced, norm_valuation, audit

def mul(u, v, modulus, basis):
    a, b, c, d = u[0], u[1], v[0], v[1]
    if basis == "sqrt_minus_three":
        return ((a*c-3*b*d) % modulus, (a*d+b*c) % modulus)
    assert basis == "zeta"
    return ((a*c-b*d) % modulus, (a*d+b*c-b*d) % modulus)

def power(u, exponent, modulus, basis):
    assert exponent >= 0
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = mul(result, u, modulus, basis)
        u = mul(u, u, modulus, basis)
        exponent >>= 1
    return result

def polynomial_value(coefficients, argument, modulus, basis):
    result = (0, 0)
    for coefficient in reversed(coefficients):
        result = mul(result, argument, modulus, basis)
        result = ((result[0]+int(coefficient)) % modulus, result[1])
    return result

def lift_retained_teich(old, old_digits, digits, p, order, basis):
    assert digits >= old_digits
    old = tuple(int(x) for x in old)
    old_modulus, modulus = p**old_digits, p**digits
    assert power(old, order, old_modulus, basis) == (1, 0)
    iterations = (digits-old_digits+1)//2
    lifted = power(old, p**(2*iterations), modulus, basis)
    assert tuple(x % old_modulus for x in lifted) == old
    assert power(lifted, order, modulus, basis) == (1, 0)
    factors = [q for q in range(2, order+1)
               if order % q == 0 and all(q % r for r in range(2, math.isqrt(q)+1))]
    assert all(power(lifted, order//q, modulus, basis) != (1, 0) for q in factors)
    conjugate = ((lifted[0], -lifted[1]) if basis == "sqrt_minus_three"
                 else (lifted[0]-lifted[1], -lifted[1]))
    assert power(lifted, p, modulus, basis) == tuple(x % modulus for x in conjugate)
    return lifted, modulus, iterations

def inputs_and_configuration(request):
    assert request["result"] == RESULT
    assert request["arithmetic_sha256"] == sha(__file__)
    assert request["workflow_sha256"] == sha(WORKFLOW)
    assert request["completed_results_must_be_reused"]
    objects = {}
    for label, item in request["inputs"].items():
        path = REPO / item["path"]
        assert sha(path) == item["sha256"], label
        raw = gzip.decompress(path.read_bytes()) if path.suffix == ".gz" else path.read_bytes()
        objects[label] = json.loads(raw)
    cfg = {"result": RESULT, "arithmetic_sha256": sha(__file__),
           "workflow_sha256": sha(WORKFLOW), "inputs": request["inputs"],
           "p47_character_h": 7, "p41_character_h": 37,
           "new_fiber_enumerations": 0, "new_lattice_terms": 0, "new_DFTs": 0}
    return objects, cfg

def calculate(out, cfg, old):
    checkpoint, receipt47, fibers = (old["p47_checkpoint"], old["p47_receipt"],
                                     old["p47_fibers"])
    assert checkpoint["complete"] and checkpoint["completed_through_a"] == 46
    assert checkpoint["receipt_sha256"] == cfg["inputs"]["p47_receipt"]["sha256"]
    assert receipt47["complete"] and receipt47["N_h_mod_p4"] == [0, 0]
    assert receipt47["valuation_exact"] is None and receipt47["valuation_lower_bound"] == 4
    assert receipt47["all_conjugation_count_checks_passed"]
    assert receipt47["original_split_vector_preserved"]
    original47 = receipt47["configuration"]
    assert original47 == checkpoint["configuration"] == fibers["configuration"]
    assert (original47["prime"], original47["h"], original47["digits"]) == (47, 7, 4)
    assert original47["theta_direction"] == "theta_h(y)=[y]^(-h*(p-1))"
    assert original47["fiber_summand"] == "theta_h(y)^(-1)"
    assert original47["torus"] == "[[a,-1],[1,a+1]] and identity"
    counts = [int(x) for x in checkpoint["counts"]]
    assert len(counts) == 48 and counts == fibers["total_character_counts"]
    assert all(counts[j] == counts[-j % 48] for j in range(48))
    assert fibers["field_elements"] == 47**2-1 and len(fibers["rows"]) == 47
    # Only sum retained counts for an audit; no finite-field elements are generated.
    assert [sum(row["character_counts"][j] for row in fibers["rows"])
            for j in range(48)] == counts
    q47 = [0]*48
    q47[0] = 46
    for j, count in enumerate(counts):
        q47[7*j % 48] -= count
    phi48 = [0]*17
    phi48[0], phi48[8], phi48[16] = 1, -1, 1
    reduced47, bound47, audit47 = cyclotomic_norm(q47, phi48, 47)
    digits47 = max(5, bound47+1)
    eta, modulus47, iterations47 = lift_retained_teich(
        fibers["teichmuller_generator_mod_p4"], 4, digits47, 47, 48, "sqrt_minus_three")
    assert [x % 47 for x in eta] == fibers["norm_one_generator_mod_p"]
    value47 = polynomial_value(reduced47, eta, modulus47, "sqrt_minus_three")
    assert value47 == polynomial_value(q47, eta, modulus47, "sqrt_minus_three")
    assert value47[1] == 0 and value47[0] != 0
    v47 = valuation(value47[0], 47)
    assert 4 <= v47 <= bound47 < digits47
    result47 = {"prime": 47, "h": 7, "valuation_N_h": v47,
                "valuation_parity": v47 % 2, "leading_unit_mod_p": value47[0]//47**v47 % 47,
                "digits": digits47, "modulus": str(modulus47),
                "teichmuller_generator": [str(x) for x in eta],
                "teichmuller_extra_frobenius_squared_iterations": iterations47,
                "N_h_mod_p_to_digits": [str(x) for x in value47],
                "valuation_exact_norm": bound47,
                "same_original_generator_and_torus": True,
                "previous_v_at_least_four_preserved": True,
                "parity_assumed": False}

    polynomial, receipt41 = old["p41_polynomial"], old["p41_receipt"]
    assert receipt41["complete"] and receipt41["all_trace_roundings_unique"]
    assert receipt41["all_rows_covered"]
    assert polynomial["integer_trace_uniqueness_verified"]
    assert not polynomial["P_exactly_zero"]
    assert polynomial["configuration"] == receipt41["configuration"]
    original41 = receipt41["configuration"]
    assert original41["prime"] == 41 and original41["n"] == 42
    assert original41["finite_field"]["gamma"] == [7, 30]
    assert original41["finite_field"]["gamma_to_n_over_3"] == [0, 1]
    assert int(original41["D"]) == 2**37*3**26*41**5
    assert receipt41["padic_result"]["padic_digits"] == 6
    assert receipt41["padic_result"]["valuation_integer_numerator"] == 3
    assert receipt41["padic_result"]["valuation_P"] == -2
    coefficients41 = [int(x) for x in polynomial["coefficients_ascending"]]
    phi42 = [int(x) for x in polynomial["cyclotomic_coefficients_ascending"]]
    assert len(coefficients41) == 42 and len(phi42) == 13 and phi42[-1] == 1
    reduced41, bound41, audit41 = cyclotomic_norm(coefficients41, phi42, 41)
    assert reduced41 == [int(x) for x in polynomial["remainder_coefficients_ascending"]] + (
        [0]*max(0, len(reduced41)-len(polynomial["remainder_coefficients_ascending"])))
    digits41 = max(6, bound41+1)
    gamma, modulus41, iterations41 = lift_retained_teich(
        receipt41["padic_result"]["teichmueller_lift"], 6, digits41, 41, 42, "zeta")
    assert [x % 41 for x in gamma] == [7, 30]
    argument37 = power(gamma, 37, modulus41, "zeta")
    assert math.gcd(37, 42) == 1 and 37 % 6 == 1
    assert power(argument37, 14, modulus41, "zeta") == (0, 1)
    value41 = polynomial_value(reduced41, argument37, modulus41, "zeta")
    assert value41 == polynomial_value(coefficients41, argument37, modulus41, "zeta")
    assert value41[1] == 0 and value41[0] != 0
    numerator_v = valuation(value41[0], 41)
    assert numerator_v <= bound41 < digits41
    p_v = numerator_v-5
    denominator_unit = 42*2**37*3**26
    p_leading = (value41[0]//41**numerator_v)*pow(denominator_unit, -1, 41) % 41
    # R727: P_36(x)=P_4(x)=19/9 at x^2=-1/3, hence N_37 is a unit.
    n37_mod41 = -pow(19*pow(9, -1, 41) % 41, 2, 41) % 41
    assert n37_mod41 != 0
    result41 = {"prime": 41, "h": 37, "valuation_integer_numerator": numerator_v,
                "valuation_P_h": p_v, "valuation_P_parity": p_v % 2,
                "normalized_P_leading_mod_p": p_leading,
                "twice_valuation_M2_h": p_v,
                "valuation_M2_h_as_rational": [p_v//math.gcd(abs(p_v), 2),
                                               2//math.gcd(abs(p_v), 2)],
                "N_h_mod_p": n37_mod41, "N_h_is_unit_by_R727": True,
                "digits": digits41, "modulus": str(modulus41),
                "original_teichmuller_generator": [str(x) for x in gamma],
                "actual_h37_argument": [str(x) for x in argument37],
                "teichmuller_extra_frobenius_squared_iterations": iterations41,
                "integer_polynomial_value": [str(x) for x in value41],
                "valuation_exact_norm_of_integer_numerator": bound41,
                "same_original_tame_direction": True,
                "h1_value_recomputed": False, "parity_assumed": False}
    audit = {"configuration": cfg, "p47": audit47, "p41": audit41,
             "precision_reason": "Each selected valuation of a nonzero cyclotomic integer is at most the p-valuation of its exact integral norm; p is unramified and all local valuations are nonnegative.",
             "new_fiber_enumerations": 0, "new_lattice_terms": 0, "new_DFTs": 0}
    archive(out / AUDIT, (json.dumps(audit, sort_keys=True, separators=(",", ":"))+"\n").encode())
    result = {"configuration": cfg, "complete": True, "p47": result47, "p41": result41,
              "all_input_hashes_verified": True,
              "new_fiber_enumerations": 0, "new_lattice_terms": 0, "new_DFTs": 0,
              "parity_inferred_from_mod_p_square": False,
              "height_or_Serre_exclusion_claimed": False,
              "artifacts": [{"file": AUDIT, "sha256": sha(out / AUDIT)}]}
    save(out / FINAL, result)
    return result

def check_readmes(out, source):
    fetch = subprocess.run(["git", "fetch", "--depth=1", "--filter=blob:none", "origin", "main"],
                           cwd=REPO, text=True, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT, timeout=120)
    record = {"source_commit": source, "fetch_exit_code": fetch.returncode,
              "fetch_log": fetch.stdout}
    save(out / "R739-readme-check.json", record)
    if fetch.returncode:
        raise RuntimeError("Could not refresh the public README rules")
    diff = subprocess.run(["git", "diff", source, "origin/main", "--", "README.md",
                           "topics/serre-uniformity/README.md"], cwd=REPO, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
    record.update(checked_main_commit=subprocess.check_output(
        ["git", "rev-parse", "origin/main"], cwd=REPO, text=True).strip(),
        diff_exit_code=diff.returncode, readmes_changed=bool(diff.stdout.strip()))
    save(out / "R739-readme-check.json", record)
    if diff.returncode or diff.stdout.strip():
        (out / "R739-readme-rules.diff").write_text(diff.stdout)
        raise RuntimeError("README changed; preserve inputs for rule review")

def reused_complete(out, cfg):
    base = TOPIC / "computations" / RESULT
    for path in sorted(base.glob("*/"+FINAL)):
        prior = read(path)
        if not prior.get("complete") or prior.get("configuration") != cfg:
            continue
        assert prior["all_input_hashes_verified"]
        assert prior["new_fiber_enumerations"] == prior["new_lattice_terms"] == prior["new_DFTs"] == 0
        manifest = read(path.parent / "files-manifest.json")
        record = next(x for x in manifest["files"] if x["file"] == FINAL)
        assert record["sha256"] == sha(path)
        for item in prior["artifacts"]:
            artifact = path.parent / item["file"]
            assert sha(artifact) == item["sha256"]
            shutil.copyfile(artifact, out / item["file"])
        shutil.copyfile(path, out / FINAL)
        return {"path": str(path.relative_to(REPO)), "receipt_sha256": sha(path)}
    return None

def run():
    started = time.monotonic()
    out = Path(os.environ["RUNNER_TEMP"]) / "R739-cyclotomic-output"
    out.mkdir(parents=True, exist_ok=True)
    source = os.environ["GITHUB_SHA"]
    save(SESSION, {"output": str(out), "result": RESULT})
    receipt = {"result": RESULT, "complete": False, "source_commit": source,
               "execution_environment": "public-repository-github-actions",
               "height_or_Serre_exclusion_claimed": False}
    source_input = {"result": RESULT, "source_commit": source,
                    "source_repository": "Rogerhu12/math-research-public", "sources": []}
    save(out / "run-receipt.json", receipt)
    save(out / "public-actions-input.json", source_input)
    try:
        request = read(REQUEST)
        source_input.update(request=request, request_sha256=sha(REQUEST))
        save(out / "public-actions-input.json", source_input)
        paths = [Path(__file__), REQUEST, WORKFLOW, HERE / "p41_public_actions_recovery.py",
                 REPO / "README.md", TOPIC / "README.md"]
        paths += [REPO / item["path"] for item in request["inputs"].values()]
        for path in paths:
            relative = str(path.relative_to(REPO))
            target = out / "sources" / (relative+".gz")
            archive(target, path.read_bytes())
            source_input["sources"].append({"path": relative, "sha256": sha(path),
                                           "archive": str(target.relative_to(out)),
                                           "archive_sha256": sha(target)})
            save(out / "public-actions-input.json", source_input)
        objects, cfg = inputs_and_configuration(request)
        old = reused_complete(out, cfg)
        if old is None:
            check_readmes(out, source)
            result = calculate(out, cfg, objects)
            receipt.update(status="COMPLETED_REUSED_INPUT_EXACT_ALGEBRA")
        else:
            result = read(out / FINAL)
            receipt.update(status="REUSED_COMPLETE", previous_complete=old)
        receipt.update(complete=True, core_receipt_sha256=sha(out / FINAL),
                       completed_results_recomputed=False, p47=result["p47"], p41=result["p41"],
                       runtime_seconds=time.monotonic()-started)
        save(out / "run-receipt.json", receipt)
        print(json.dumps(receipt), flush=True)
    except BaseException:
        (out / "R739-reuse-failure.txt").write_text(traceback.format_exc())
        save(out / "run-receipt.json", receipt)
        raise

def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Formal computation is restricted to the public repository Actions.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=["run", "publish", "verify"])
    args = parser.parse_args()
    if args.phase == "run":
        run()
        return
    out = Path(read(SESSION)["output"])
    if args.phase == "publish":
        raise SystemExit(publish({"result": RESULT}, out, "serre-cartier"))
    receipt, core = read(out / "run-receipt.json"), read(out / FINAL)
    assert receipt["complete"] and core["complete"]
    assert sha(out / FINAL) == receipt["core_receipt_sha256"]
    _, cfg = inputs_and_configuration(read(REQUEST))
    assert core["configuration"] == cfg and core["all_input_hashes_verified"]
    for item in core["artifacts"]:
        assert sha(out / item["file"]) == item["sha256"]
    assert core["new_fiber_enumerations"] == core["new_lattice_terms"] == core["new_DFTs"] == 0
    assert not core["parity_inferred_from_mod_p_square"]
    assert not core["height_or_Serre_exclusion_claimed"]
    print("RETAINED_CERTIFICATES_AND_EXACT_LOCAL_VALUATIONS_VERIFIED")

if __name__ == "__main__":
    main()
