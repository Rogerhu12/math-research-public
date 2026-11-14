#!/usr/bin/env python3
"""Exact original R727 finite toric norm at p=47,h=7, modulo 47^4.

For g_a=[[a,-1],[1,a+1]], D=a*a+a+1, the exact Weyl pairing is
  G(e_0,g_a e_0) = -sum theta_h(y)^(-1),
where (a+1)N(y)+Tr(y)=-a/D.  The identity contributes p-1.
We use theta_h(y)=[y]^(-h*(p-1)); hence the summand is
[y]^(h*(p-1)), with Teichmuller values in the unramified quadratic ring.
No mod-p square identity is lifted to higher precision.
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
import sys
import time
import traceback
from p41_public_actions_recovery import REPO, TOPIC, publish

HERE = Path(__file__).resolve().parent
REQUEST = TOPIC / "notes/R739-p47-h7-request.json"
WORKFLOW = REPO / ".github/workflows/serre-R739-p47-h7-norm.yml"
RESULT = "R739-original-finite-norm-p47-h7"
FINAL = "R739-p47-h7-exact-N.json"
ROWS = "R739-p47-h7-original-fibers.json.gz"
SESSION = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "R739-p47-h7-session.json"

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

def mul(u, v, modulus):
    return ((u[0]*v[0]-3*u[1]*v[1]) % modulus,
            (u[0]*v[1]+u[1]*v[0]) % modulus)

def power(u, exponent, modulus):
    answer = (1, 0)
    while exponent:
        if exponent & 1:
            answer = mul(answer, u, modulus)
        u = mul(u, u, modulus)
        exponent >>= 1
    return answer

def config(request):
    assert request["result"] == RESULT
    assert (request["prime"], request["h"], request["digits"]) == (47, 7, 4)
    assert request["arithmetic_sha256"] == sha(__file__)
    assert request["workflow_sha256"] == sha(WORKFLOW)
    return {"prime": 47, "h": 7, "digits": 4,
            "field_relation": "t^2=-3", "torus": "[[a,-1],[1,a+1]] and identity",
            "split_vector": "original e_0",
            "theta_direction": "theta_h(y)=[y]^(-h*(p-1))",
            "fiber_summand": "theta_h(y)^(-1)",
            "arithmetic_sha256": sha(__file__)}

def check_readmes(out, source):
    fetch = subprocess.run(["git", "fetch", "--depth=1", "--filter=blob:none",
                            "origin", "main"], cwd=REPO, text=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
    record = {"source_commit": source, "fetch_exit_code": fetch.returncode,
              "fetch_log": fetch.stdout}
    save(out / "R739-readme-check.json", record)
    if fetch.returncode:
        raise RuntimeError("Could not refresh public README rules")
    diff = subprocess.run(["git", "diff", source, "origin/main", "--",
                           "README.md", "topics/serre-uniformity/README.md"],
                          cwd=REPO, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, timeout=120)
    record.update(checked_main_commit=subprocess.check_output(
                    ["git", "rev-parse", "origin/main"], cwd=REPO, text=True).strip(),
                  diff_exit_code=diff.returncode, readmes_changed=bool(diff.stdout.strip()))
    save(out / "R739-readme-check.json", record)
    if diff.returncode or diff.stdout.strip():
        (out / "R739-readme-rules.diff").write_text(diff.stdout)
        raise RuntimeError("README changed; preserve inputs for rule review")

def reused_complete(out, cfg):
    base = TOPIC / "computations" / RESULT
    for prior in sorted(base.glob("*/" + FINAL)):
        receipt = read(prior)
        if receipt.get("configuration") != cfg or not receipt.get("complete"):
            continue
        manifest = read(prior.parent / "files-manifest.json")
        record = next(x for x in manifest["files"] if x["file"] == FINAL)
        assert record["sha256"] == sha(prior)
        for item in receipt["artifacts"]:
            old = prior.parent / item["file"]
            assert sha(old) == item["sha256"]
            shutil.copyfile(old, out / item["file"])
        shutil.copyfile(prior, out / FINAL)
        return {"public_path": str(prior.relative_to(REPO)),
                "receipt_sha256": sha(prior), "recomputed": False}
    return None

def exact_norm(out, cfg):
    p, h, digits = cfg["prime"], cfg["h"], cfg["digits"]
    n, modulus = p+1, p**digits
    assert math.gcd(h, n) == 1 and h % 6 == 1
    assert pow(p-3, (p-1)//2, p) == p-1
    factors = [q for q in range(2, n+1)
               if n % q == 0 and all(q % r for r in range(2, math.isqrt(q)+1))]
    generator = None
    for a in range(p):
        for b in range(p):
            trial = (a, b)
            if (a*a+3*b*b) % p != 1:
                continue
            if all(power(trial, n//q, p) != (1, 0) for q in factors):
                generator = trial
                break
        if generator is not None:
            break
    assert generator is not None
    log_table, current = {}, (1, 0)
    for j in range(n):
        assert current not in log_table
        log_table[current] = j
        current = mul(current, generator, p)
    assert current == (1, 0) and len(log_table) == n
    eta = power(generator, p**(2*digits), modulus)
    assert tuple(x % p for x in eta) == generator
    assert power(eta, n, modulus) == (1, 0)
    assert all(power(eta, n//q, modulus) != (1, 0) for q in factors)
    assert (eta[0]*eta[0]+3*eta[1]*eta[1]) % modulus == 1
    assert power(eta, p, modulus) == (eta[0], (-eta[1]) % modulus)
    weights = [power(eta, h*j, modulus) for j in range(n)]
    field_rows = []
    for u in range(p):
        for v in range(p):
            if u == v == 0:
                continue
            norm = (u*u+3*v*v) % p
            inverse = pow(norm, -1, p)
            quotient = ((u*u-3*v*v)*inverse % p, -2*u*v*inverse % p)
            j = log_table[quotient]
            assert quotient == power((u, v), p-1, p)
            assert tuple(z % p for z in weights[j]) == power((u, v), h*(p-1), p)
            field_rows.append((norm, 2*u % p, j))
    assert len(field_rows) == p*p-1
    counts, rows = [0]*n, []
    checkpoint = out / "R739-fiber-checkpoint.json"
    for a in range(p):
        determinant = (a*a+a+1) % p
        assert determinant
        r, s = (a+1) % p, -a*pow(determinant, -1, p) % p
        local = [0]*n
        for norm, trace, j in field_rows:
            if (r*norm+trace-s) % p == 0:
                local[j] += 1
        assert all(local[j] == local[(-j) % n] for j in range(n))
        counts = [u+v for u, v in zip(counts, local)]
        rows.append({"a": a, "determinant": determinant, "r": r, "s": s,
                     "fiber_size": sum(local), "character_counts": local})
        save(checkpoint, {"configuration": cfg, "complete": False,
                         "completed_through_a": a, "counts": counts, "rows": rows})
        if a % 10 == 0:
            print(json.dumps({"completed_through_a": a, "of": p-1}), flush=True)
    terms = [((counts[j]*weights[j][0]) % modulus,
              (counts[j]*weights[j][1]) % modulus) for j in range(n)]
    value = ((p-1-sum(t[0] for t in terms)) % modulus,
             -sum(t[1] for t in terms) % modulus)
    assert value[1] == 0
    assert value[0] % p == 0
    theta_on_sqrt_minus_three = weights[log_table[(p-1, 0)]]
    assert theta_on_sqrt_minus_three == (modulus-1, 0)
    raw = json.dumps({"configuration": cfg, "norm_one_generator_mod_p": generator,
                      "teichmuller_generator_mod_p4": eta, "modulus": modulus,
                      "field_elements": p*p-1, "rows": rows,
                      "total_character_counts": counts,
                      "theta_inverse_weights": weights,
                      "weighted_terms_mod_p4": terms}, sort_keys=True,
                     separators=(",", ":")).encode() + b"\n"
    archive(out / ROWS, raw)
    v = value[0]
    valuation = 0
    if v == 0:
        exact = None
        lower_bound = digits
        leading = None
    else:
        while v % p == 0:
            valuation += 1
            v //= p
        exact, lower_bound, leading = valuation, valuation, v % p
    result = {"configuration": cfg, "complete": True, "modulus": modulus,
              "N_h_mod_p4": list(value), "valuation_exact": exact,
              "valuation_lower_bound": lower_bound, "leading_unit_mod_p": leading,
              "parity_determined": exact is not None,
              "valuation_parity": None if exact is None else exact % 2,
              "teichmuller_order_verified": n,
              "original_torus_rows": p, "original_split_vector_preserved": True,
              "theta_on_sqrt_minus_three": list(theta_on_sqrt_minus_three),
              "all_conjugation_count_checks_passed": True,
              "legendre_check_used_only_mod_p": True,
              "legendre_P6_exact": "-47/9",
              "norm_valuation_inferred_from_mod_p_square": False,
              "artifacts": [{"file": ROWS, "sha256": sha(out / ROWS)}],
              "mathematical_completion_claimed": False}
    save(out / FINAL, result)
    save(checkpoint, {"configuration": cfg, "complete": True,
                     "completed_through_a": p-1, "counts": counts,
                     "receipt_sha256": sha(out / FINAL)})
    return result

def run():
    started = time.monotonic()
    out = Path(os.environ["RUNNER_TEMP"]) / "R739-p47-h7-output"
    out.mkdir(parents=True, exist_ok=True)
    source = os.environ["GITHUB_SHA"]
    save(SESSION, {"output": str(out), "result": RESULT})
    receipt = {"result": RESULT, "complete": False, "source_commit": source,
               "execution_environment": "public-repository-github-actions",
               "mathematical_completion_claimed": False}
    source_input = {"result": RESULT, "source_commit": source,
                    "source_repository": "Rogerhu12/math-research-public",
                    "sources": [], "mathematical_completion_claimed": False}
    save(out / "run-receipt.json", receipt)
    save(out / "public-actions-input.json", source_input)
    try:
        request = read(REQUEST)
        source_input.update(request=request, request_sha256=sha(REQUEST))
        save(out / "public-actions-input.json", source_input)
        for path in [Path(__file__), REQUEST, WORKFLOW,
                     HERE / "p41_public_actions_recovery.py",
                     REPO / "README.md", TOPIC / "README.md"]:
            relative = str(path.relative_to(REPO))
            target = out / "sources" / (relative + ".gz")
            archive(target, path.read_bytes())
            source_input["sources"].append({"path": relative, "sha256": sha(path),
                        "archive": str(target.relative_to(out)), "archive_sha256": sha(target)})
            save(out / "public-actions-input.json", source_input)
        cfg = config(request)
        old = reused_complete(out, cfg)
        if old is None:
            check_readmes(out, source)
            result = exact_norm(out, cfg)
            receipt.update(status="COMPLETED_EXACT_FINITE_NORM", completed_result_recomputed=False)
        else:
            result = read(out / FINAL)
            receipt.update(status="REUSED_COMPLETE", previous_complete=old,
                           completed_result_recomputed=False)
        receipt.update(complete=True, core_receipt_sha256=sha(out / FINAL),
                       N_h_mod_p4=result["N_h_mod_p4"],
                       valuation_exact=result["valuation_exact"],
                       valuation_lower_bound=result["valuation_lower_bound"],
                       runtime_seconds=time.monotonic()-started)
        save(out / "run-receipt.json", receipt)
        print(json.dumps(receipt), flush=True)
    except BaseException:
        (out / "R739-public-failure.txt").write_text(traceback.format_exc())
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
    session = read(SESSION)
    out = Path(session["output"])
    if args.phase == "publish":
        raise SystemExit(publish({"result": RESULT}, out, "serre-cartier"))
    receipt = read(out / "run-receipt.json")
    assert receipt["complete"]
    assert sha(out / FINAL) == receipt["core_receipt_sha256"]
    core = read(out / FINAL)
    assert core["complete"] and core["configuration"] == config(read(REQUEST))
    for item in core["artifacts"]:
        assert sha(out / item["file"]) == item["sha256"]
    assert core["original_split_vector_preserved"]
    assert core["all_conjugation_count_checks_passed"]
    assert not core["norm_valuation_inferred_from_mod_p_square"]
    print("ORIGINAL_FINITE_TORIC_NORM_VERIFIED")

if __name__ == "__main__":
    main()
