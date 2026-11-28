#!/usr/bin/env python3
"""Exact original FullHold Hermite coefficients, R734 width and cooperative prefix.

Scientific execution takes place on the public project runner. The full row
ledger stays there. Only the complete small conclusion and content identities
are reported. Polynomial vectors are in increasing powers of local u.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import gzip
import importlib.util
import json
from math import comb
import os
from pathlib import Path
import subprocess

TOPIC = "topics/visible-flex-larger-amplitude"
MAKER = "scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py"
MAKER_SHA = "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60"
TARGET = "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9"
PREDICATES = ("a>0", "a_ss>0", "a_s>=0", "a*a_sss+3*a_s*a_ss>=0", "1-Rplus^2*a_s^2>0")
STRICT = (True, True, False, False, True)
RPLUS = Q(25, 4) + Q(553, 2**53)
RMINUS = Q(1, 4) - Q(553, 2**53)
BISECTIONS = 48


def json_bytes(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def ident(data):
    return {"bytes": len(data), "sha256": sha256(data).hexdigest()}


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def derivative(p):
    return trim([i*p[i] for i in range(1, len(p))])


def scale(p, s):
    return trim([s*x for x in p])


def add(p, q):
    r = [Q(0)] * max(len(p), len(q))
    for seq in (p, q):
        for i, x in enumerate(seq):
            r[i] += x
    return trim(r)


def times(p, q):
    if not p or not q:
        return []
    r = [Q(0)] * (len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return trim(r)


def divide(p, q):
    if not q:
        raise ZeroDivisionError("zero polynomial divisor")
    p = trim(p)
    quotient = [Q(0)] * max(0, len(p)-len(q)+1)
    while len(p) >= len(q):
        i, lead = len(p)-len(q), p[-1]/q[-1]
        quotient[i] = lead
        for j, y in enumerate(q):
            p[i+j] -= lead*y
        p = trim(p)
    return trim(quotient), p


def normalized(p):
    return scale(p, Q(1)/abs(p[-1])) if p else []


def gcd(p, q):
    while q:
        p, q = q, normalized(divide(p, q)[1])
    return scale(p, Q(1)/p[-1]) if p else []


def quotient(p, q):
    result, rem = divide(p, q)
    if rem:
        raise ArithmeticError("inexact square-free quotient")
    return result


def sign(x):
    return (x > 0) - (x < 0)


def side(p, right):
    """Sign just right of zero or just left of one, even for endpoint roots."""
    if not right:
        return next((sign(x) for x in p if x), 0)
    order = 0
    while p:
        value = sum(p, Q(0))
        if value:
            return (-1)**order * sign(value)
        p, order = derivative(p), order+1
    return 0


def inner_roots(p):
    """Number of distinct real roots strictly inside (0,1), via Sturm."""
    if len(p) < 2:
        return 0
    chain = [normalized(p), normalized(derivative(p))]
    while True:
        rem = divide(chain[-2], chain[-1])[1]
        if not rem:
            break
        chain.append(normalized(scale(rem, -1)))
    def variation(right):
        seq = [side(f, right) for f in chain]
        seq = [x for x in seq if x]
        return sum(x != y for x, y in zip(seq, seq[1:]))
    return variation(False) - variation(True)


def odd_roots(p):
    """Yun factors of odd multiplicity, with strictly interior Sturm counts."""
    common = gcd(p, derivative(p))
    part = quotient(p, common)
    counts = []
    multiplicity = 1
    while len(part) > 1:
        both = gcd(part, common)
        if multiplicity % 2:
            factor = quotient(part, both)
            counts.append([multiplicity, inner_roots(factor)])
        part, common = both, quotient(common, both)
        multiplicity += 1
    return counts


def bernstein(p):
    n = len(p)-1
    if n < 0:
        return [Q(0)]
    return [sum((p[j]*Q(comb(k, j), comb(n, j)) for j in range(k+1)), Q(0))
            for k in range(n+1)]


def decide(p, strict):
    """Closed-cell universal sign; endpoints, repeated and zero roots included."""
    b = bernstein(p)
    low, high = min(b), max(b)
    record = {"bernstein_lower": str(low), "bernstein_upper": str(high),
              "left_value": str(b[0]), "right_value": str(b[-1])}
    if b[0] < 0 or b[-1] < 0 or (strict and (b[0] == 0 or b[-1] == 0)):
        ok, how = False, "endpoint"
    elif low >= 0:
        # All internal Bernstein basis functions are positive on the open cell.
        ok, how = True, "Bernstein hull and both actual endpoint signs"
    elif side(p, False) < 0 or side(p, True) < 0:
        ok, how = False, "negative exact one-sided sign"
    elif strict:
        n = inner_roots(p)
        ok, how = n == 0, "Sturm distinct roots in (0,1)"
        record["interior_roots"] = n
    else:
        counts = odd_roots(p)
        ok, how = not any(n for _, n in counts), "Yun odd-multiplicity factors and Sturm"
        record["odd_multiplicity_root_counts"] = counts
    record.update(holds=ok, proof=how)
    return record


def predicates(co, w):
    ap = scale(derivative(co), Q(1)/w)
    app = scale(derivative(ap), Q(1)/w)
    appp = scale(derivative(app), Q(1)/w)
    cooperation = add(times(co, appp), scale(times(ap, app), 3))
    margin = add([Q(1)], scale(times(ap, ap), -RPLUS**2))
    return [trim(co), app, ap, cooperation, margin]


def restriction(p, t):
    return trim([v*t**i for i, v in enumerate(p)])


def verdicts(polys, t):
    return [decide(restriction(p, t), strict) for p, strict in zip(polys, STRICT)]


def prefix_frontier(polys, x, w):
    at_start = verdicts(polys, Q(0))
    if not all(v["holds"] for v in at_start):
        return {"lower": str(x), "upper": str(x), "right_piece_left_endpoint_valid": False,
                "failed_at_upper": [s for s, v in zip(PREDICATES, at_start) if not v["holds"]],
                "upper_decisions": at_start, "domain_note": "preceding pieces end at x; right-hand data already fail at x"}
    lo, hi = Q(0), Q(1)
    for _ in range(BISECTIONS):
        mid = (lo+hi)/2
        if all(v["holds"] for v in verdicts(polys, mid)):
            lo = mid
        else:
            hi = mid
    lower, upper = verdicts(polys, lo), verdicts(polys, hi)
    return {"lower": str(x+w*lo), "upper": str(x+w*hi),
            "local_lower": str(lo), "local_upper": str(hi),
            "right_piece_left_endpoint_valid": True, "bisections": BISECTIONS,
            "failed_at_upper": [s for s,v in zip(PREDICATES, upper) if not v["holds"]],
            "lower_decisions": lower, "upper_decisions": upper,
            "domain_note": "every predicate holds throughout the closed lower prefix; some predicate fails somewhere in the closed upper prefix. No inclusion claim at the unknown supremum."}


def binary_value(v):
    x = float(v)
    return {"binary64_hex": x.hex(), "exact": str(Q.from_float(x))}


def knot_data(knot):
    return {key: binary_value(knot[key]) for key in ("s", "a", "ap", "app")}


def recover(repo, work):
    path = repo / TOPIC / MAKER
    if sha256(path.read_bytes()).hexdigest() != MAKER_SHA:
        raise ValueError("fixed scalar maker source differs")
    spec = importlib.util.spec_from_file_location("fixed_r690_scalar_source", path)
    maker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(maker)
    maker.require_actions()
    paths = maker._source_paths(repo)
    # Partial historical fetch acquires commit/tree metadata. git show in the
    # original restoration then fetches the one actual named original blob.
    subprocess.run(["git","fetch","--no-tags","--depth=1","--filter=blob:none","origin",
                    maker.ACCEPTED_COMMIT], cwd=repo, check=True)
    record = maker._restore_accepted(repo, work / "original-accepted099.json.gz")
    original = maker._read_json_bytes(gzip.decompress(Path(record["path"]).read_bytes()))
    parameters = maker.scalar_projection(original)
    data = {"analytic_extension_origin": parameters["analytic_extension_origin"],
            "fixed_scalar_profile": {"geometry": parameters["geometry"]}}
    # The bytes are exactly those emitted by the original fixed-input maker.
    fixed_path = work / "fixed-scalar-input.json"
    maker.write_json(fixed_path, data)
    scalar = maker._load("r734_exact_fullhold", paths["scalar"])
    full = scalar.FullHold(data, paths["integer"], paths["hold"], panels=maker.PANELS)
    recipe = maker.mathematical_target_recipe()
    if maker.canonical(recipe) != TARGET:
        raise ValueError("original full fixed target identity differs")
    binding = {"maker": {"path": TOPIC+"/"+MAKER, "sha256": MAKER_SHA},
               "source_pins": maker.SOURCE_PINS, "panels": maker.PANELS,
               "historic_source": recipe["scalar_parameter_origin"],
               "complete_scalar_projection_sha256": maker.canonical(parameters),
               "fixed_scalar_input": ident(fixed_path.read_bytes()),
               "full_target_sha256": TARGET, "actual_fullhold_source_sha256": full.source_sha,
               "old_end": str(full.x[-1]), "S_lower": str(Q(full.S[0], full.h.S)),
               "S_upper": str(Q(full.S[1], full.h.S)), "out": str(full.out),
               "unchanged_prefix_end_lower": str(Q(full.S[0], full.h.S)-full.out/4)}
    if not full.x[-1] < Q(full.S[0], full.h.S)-full.out/4:
        raise ArithmeticError("old pieces are not all within the R690 unchanged prefix")
    return full, parameters, binding


def calculate(repo, work, summary_path):
    if (os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"
            or os.environ.get("GITHUB_ACTIONS") != "true"):
        raise RuntimeError("public project Actions required")
    work.mkdir(parents=True, exist_ok=True)
    full, parameters, binding = recover(repo, work)
    knots = parameters["geometry"]["knots"]
    law = parameters["geometry"]["initial_law"]
    k0 = Q.from_float(float(law["k0"]))
    x, coeff = full.x, full.coefficients
    if len(x) != 416 or len(coeff) != 415 or len(knots) != 416:
        raise ValueError("the original 416 knots and 415 pieces are required")
    width = x[1]-x[0]
    first = coeff[0]
    b3 = sum((j*(j-1)*(j-2)*abs(first[j]) for j in range(3,6)), Q(0))/width**3
    terms = [width, Q(1,200), k0/(2*(1+b3)), 1/(25*(4+7*b3/(2*k0)))]
    core_jet = [first[0], first[1]/width, 2*first[2]/width**2]
    core_match = core_jet == [1, 0, k0]
    core = {"physical_width": str(width), "first_two_knots": list(map(knot_data,knots[:2])),
            "initial_law": {k:binary_value(law[k]) for k in ("length","velocity","k0")},
            "first_fullhold_coefficients": list(map(str, first)), "physical_core_jet": list(map(str, core_jet)),
            "k0_matches_2c2_over_w2": core_jet[2] == k0, "complete_core_jet_matches": core_match,
            "B3": str(b3), "width_terms_w_1over200_k0term_driftterm": list(map(str,terms)),
            "Tstar": str(min(terms)) if core_match else None,
            "Tstar_approx": float(min(terms)) if core_match else None,
            "Tstar_applies_to_two_sided_core_only": True, "core_formula_uses_actual_Fractions": True}
    raw = {"binding": binding, "core": core, "knot_words": list(map(knot_data, knots)),
           "cn_convention": "Exact Fraction c_j multiplying u^j; u=(s-x_i)/(x_{i+1}-x_i); no coefficient binary64 rounding in the target.",
           "Rplus": str(RPLUS), "Rminus": str(RMINUS), "predicate_order": PREDICATES, "rows":[]}
    columns = [[] for _ in PREDICATES]
    first_failure = None
    frontier = None
    joints_ok = True
    fractions_only = True
    for i,(left,right,co) in enumerate(zip(x,x[1:],coeff)):
        w = right-left
        p = predicates(co, w)
        ds = [decide(poly, strict) for poly, strict in zip(p, STRICT)]
        status = [v["holds"] for v in ds]
        for col, yes in zip(columns,status):
            col.append("1" if yes else "0")
        if first_failure is None and not all(status):
            first_failure = i
            frontier = prefix_frontier(p,left,w)
        actual = [[vec[0] if vec else Q(0), sum(vec,Q(0))] for vec in [p[0],p[2],p[1]]]
        expected = [[Q(float(knots[i][key])), Q(float(knots[i+1][key]))]
                    for key in ("a","ap","app")]
        if i == 0:
            for pair, value in zip(expected, [Q(1),Q(0),k0]):
                pair[0] = value
        residuals = [[a-b for a,b in zip(aa,bb)] for aa,bb in zip(actual,expected)]
        joints_ok = joints_ok and all(v == 0 for pair in residuals for v in pair)
        fractions_only = fractions_only and all(isinstance(v,Q) for v in co)
        raw["rows"].append({"index":i, "domain":[str(left),str(right)], "width":str(w),
            "coefficients":list(map(str,co)), "rounded_display_only":[float(v).hex() for v in co],
            "knot_indices":[i,i+1], "physical_endpoint_jet_residuals":[list(map(str,z)) for z in residuals],
            "predicate_powers":[list(map(str,vec)) for vec in p], "decisions":ds})
    if first_failure is None:
        frontier = {"lower":str(x[-1]), "upper":str(x[-1]), "whole_old_domain_valid":True}
    raw["frontier"] = frontier
    raw_path = work / "all-415-exact-rows.json"
    raw_body = json_bytes(raw)
    raw_path.write_bytes(raw_body)
    n = 415 if first_failure is None else first_failure
    compact_frontier = {k:v for k,v in frontier.items() if k not in ("lower_decisions","upper_decisions")}
    # Both bounds of the frontier are exact Fractions. Rounded displays are ancillary.
    compact_frontier["approximate_endpoints"] = [float(Q(frontier[k])) for k in ("lower","upper")]
    conclusion = {"schema":"r734-complete-original-Hermite-cooperative-prefix-v1",
        "repository":os.environ["GITHUB_REPOSITORY"], "run":os.environ["GITHUB_RUN_ID"],
        "attempt":os.environ["GITHUB_RUN_ATTEMPT"], "trigger_commit":os.environ["GITHUB_SHA"],
        "source_commit":subprocess.check_output(["git","rev-parse","HEAD"],cwd=repo,text=True).strip(),
        "script":ident(Path(__file__).read_bytes()), "rules_read_commit":os.environ["R734_RULES_COMMIT"],
        "binding":binding, "Rplus":str(RPLUS),"Rminus":str(RMINUS),
        "core":core,"original_pieces_examined":len(coeff),"original_knots_examined":len(knots),
        "all_source_coefficients_are_Fractions":fractions_only,"all_physical_endpoint_jets_match":joints_ok,
        "all_415_rows":ident(raw_body), "row_identity":"all_415_rows SHA-256 and zero-based rows[i]; each row contains its exact domain, all six exact power coefficients, binary64 display, knot indices, physical endpoint jet residuals, and the exact whole-cell Bernstein bounds and classification of all five predicates",
        "predicate_order":PREDICATES,"cell_status_columns":["".join(c) for c in columns],
        "status_legend":"column string character i is 1 = proved throughout closed piece i, 0 = disproved on that piece; each side takes its own one-sided third derivative at a knot. No unresolved signs.",
        "complete_core_prefix_piece_count":n, "whole_piece_prefix_end":str(x[n]),
        "first_failing_piece_zero_based":first_failure, "cooperative_frontier":compact_frontier,
        "scope":"All 415 original Hermite pieces through the original analytic origin only. Tstar is the local R734 core bound. Cooperative sign continuation is separate; it supplies neither a normal-ball certificate on that longer band nor a full closed isometric family.",
        "physical_F":0,"Jacobian":0,"normal_roots":0,"raw_uploaded":False}
    if first_failure is not None:
        row=raw["rows"][first_failure]
        conclusion["first_failing_whole_piece"]={"index":first_failure, "domain":row["domain"],
            "failed_predicates":[PREDICATES[j] for j,d in enumerate(row["decisions"]) if not d["holds"]],
            "failure_proofs":[d for d in row["decisions"] if not d["holds"]]}
    body = json_bytes(conclusion)
    summary_path.write_bytes(body)
    print(json.dumps({"raw_runner_only":ident(raw_body),"complete_logical_conclusion":ident(body),
                      "Tstar":core["Tstar"],"whole_prefix_count":n,"frontier":compact_frontier}),flush=True)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",required=True,type=Path)
    parser.add_argument("--work",required=True,type=Path)
    parser.add_argument("--summary",required=True,type=Path)
    args=parser.parse_args()
    calculate(args.repo.resolve(), args.work.resolve(), args.summary.resolve())
