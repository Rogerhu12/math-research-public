#!/usr/bin/env python3
"""Complete q=11 search over every degree-three minimal polar divisor.

The mathematical domain is proved in the companion note. It has two disjoint
parts: one chosen branch above each Y-place, and one whole three-point fibre.
All multiplicities are retained. No particular polar divisor is guessed.

Only the named public Actions repository may execute this module. The result
is a finite q=11 section computation, not a claim about an ordinary prime,
the original weighted 27 pairs, or infinitely many primes.
"""

import hashlib
import itertools
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path
import sys
import time

if os.environ.get("GITHUB_ACTIONS") != "true" or \
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("Mathematical execution requires the named public GitHub Actions repository.")

from flint import nmod_poly

Q = 11

# Complete negative domains already executed publicly. Reuse them, do not rerun.
PAID_NEGATIVE_PAIRS = {
    ((10, 1, 10, 1), (9, 8, 1)): {
        "run": 45934797848, "job": 140295406866,
        "source": "1ac50c6e0283c6878c77c8fc9e357fc1b17a8ee1",
        "request_id": "rank2-20261127-original-q11-fixed-kernel-section",
        "script": "topics/rank2-sha-infinitely-many-p/scripts/check-original-q11-kernel-section.py",
        "script_sha256": "989df72755256fa401e0aa3826c00721a9a2f7d6655af374576b09c87fb985b3",
        "stdout_sha256": "0e8db179dcb5a5d485b1745616861e3f12a2beee56dd7ae48b6636e0d04022a5", "stdout_bytes": 848,
        "enumeration_sha256": "9a44261254fa0abc60c980ca7ca8cdc5745b2e98f56f105908220abd5dd7a78e"},
    ((10, 3, 8, 1), (2, 1, 4)): {
        "run": 45936278912, "job": 140300111547,
        "source": "89a464233e4d50471eb795622a80ea05af09a43e",
        "request_id": "rank2-20261127-original-q11-six-torsion-pole",
        "script": "topics/rank2-sha-infinitely-many-p/scripts/check-original-q11-six-torsion-pole.py",
        "script_sha256": "a1566e8b5b5591c17a0feddfcf33b65bb226f19690424a2df68306e28c6d78c1",
        "stdout_sha256": "73cadc36965119047f0d228ccea05c211a60bd1558ac3bd9706eae480cb17f12", "stdout_bytes": 952,
        "enumeration_sha256": "d7d80797ddf5a122b9e55edb3b35d2dae57822bba77edbb9a8e041c3c16bf36e"},
    ((10, 9, 2, 1), (3, 0, 4)): {
        "run": 45941789126, "job": 140317511374,
        "source": "5bcbf6061bc111254d1f75c732ab40e55d4bb1ef",
        "request_id": "2026-11-27-original-q11-delta-image-polar-divisor",
        "script": "topics/rank2-sha-infinitely-many-p/scripts/check-original-q11-delta-image-pole.py",
        "script_sha256": "b70ed972bb7105547b4229b1ca121af04f37292b3466c5e30ec69496bcb59081",
        "stdout_sha256": "de64c4bded5a81bac81b32c913580743ca449c776bb2b2c3140c2ffc86d7164c", "stdout_bytes": 998,
        "enumeration_sha256": "61905c08fa3ec8e1bc28f283ee54e4b7abc3e1c7c8e0522030573ef530f40355"},
}


class ReceiptReadError(Exception):
    """Missing or mismatched original public evidence is an execution error."""


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def receipt_api_get(path, want_redirect=False):
    api = "https://api.github.com/repos/Rogerhu12/math-research-public"
    token = os.environ.get("RANK2_ACTIONS_READ_TOKEN", "")
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "rank2-q11-complete-polar-divisors-receipt-reader",
        "Accept-Encoding": "identity",
    }
    if token:
        headers["Authorization"] = "Bearer " + token
    request = urllib.request.Request(api + path, headers=headers, method="GET")
    opener = urllib.request.build_opener(NoRedirect())
    try:
        response = opener.open(request, timeout=30)
    except urllib.error.HTTPError as exc:
        code, location = exc.code, exc.headers.get("Location")
        exc.close()
        if code == 302 and want_redirect and location:
            if not location.startswith("https://"):
                raise ReceiptReadError("The original log redirect is not HTTPS.")
            return location
        raise ReceiptReadError("The original public receipt API returned HTTP " + str(code))
    if want_redirect:
        response.close()
        raise ReceiptReadError("The original job log endpoint did not return a redirect.")
    with response:
        data = response.read(2000001)
    if len(data) > 2000000:
        raise ReceiptReadError("An original API metadata response exceeded its byte bound.")
    return json.loads(data)


def read_paid_result(binding):
    run_id, job_id = binding["run"], binding["job"]
    run = receipt_api_get("/actions/runs/" + str(run_id))
    job = receipt_api_get("/actions/jobs/" + str(job_id))
    if run.get("id") != run_id or run.get("head_sha") != binding["source"] or \
            job.get("id") != job_id or job.get("run_id") != run_id or \
            job.get("head_sha") != binding["source"]:
        raise ReceiptReadError("The original run/job/source identity does not match.")
    for metadata in (run, job):
        if metadata.get("status") != "completed" or metadata.get("conclusion") != "success":
            raise ReceiptReadError("The original public job is not completed successfully.")

    location = receipt_api_get("/actions/jobs/" + str(job_id) + "/logs", want_redirect=True)
    # A new unauthenticated request prevents forwarding the API token to storage.
    request = urllib.request.Request(location, headers={
        "User-Agent": "rank2-q11-complete-polar-divisors-receipt-reader",
        "Accept-Encoding": "identity"}, method="GET")
    with urllib.request.urlopen(request, timeout=30) as response:
        raw_log = response.read(2000001)
    if len(raw_log) > 2000000:
        raise ReceiptReadError("An original compact job log exceeded its byte bound.")
    pattern = re.compile(
        rb"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z "
        rb"(RANK2_EXACT_STDOUT|RANK2_PUBLIC_EXACT_CHECK) (.*)$")
    stdout_records, receipt_records = [], []
    for line in raw_log.splitlines():
        match = pattern.fullmatch(line)
        if match is None:
            continue
        tag, payload = match.groups()
        record = json.loads(payload)
        if tag == b"RANK2_EXACT_STDOUT" and record.get("script") == binding["script"]:
            stdout_records.append(record)
        if tag == b"RANK2_PUBLIC_EXACT_CHECK" and record.get("request_id") == binding["request_id"]:
            receipt_records.append(record)
    if len(stdout_records) != 1 or len(receipt_records) != 1:
        raise ReceiptReadError("The original timestamped stdout/receipt is missing or ambiguous.")
    receipt = receipt_records[0]
    if receipt.get("run_id") != run_id or receipt.get("source_commit") != binding["source"] or \
            receipt.get("outputs_persisted") is not False:
        raise ReceiptReadError("The original complete-check receipt has a mismatched identity.")
    checks = [item for item in receipt.get("checks", [])
              if item.get("script") == binding["script"]]
    if len(checks) != 1:
        raise ReceiptReadError("The original exact script check is missing or ambiguous.")
    check = checks[0]
    if check.get("script_sha256") != binding["script_sha256"] or \
            check.get("sha256") != binding["stdout_sha256"] or \
            check.get("stdout_bytes") != binding["stdout_bytes"] or \
            check.get("exit_code") != 0 or check.get("args") != [] or \
            check.get("engine") != "python3":
        raise ReceiptReadError("The original script/stdout hash, arguments, or exit status differs.")
    result = stdout_records[0]["result"]
    raw = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if len(raw) != binding["stdout_bytes"] or \
            hashlib.sha256(raw).hexdigest() != binding["stdout_sha256"]:
        raise ReceiptReadError("The live original stdout does not match its immutable hash.")
    return result


def paid_receipts():
    """Read original public receipts live; never cache their computed output."""
    out = []
    for (h_tuple, _), binding in PAID_NEGATIVE_PAIRS.items():
        result = read_paid_result(binding)
        if result["source_sha256"] != binding["script_sha256"] or \
                result["enumeration_sha256"] != binding["enumeration_sha256"] or \
                tuple(result["H"]) != h_tuple:
            raise ReceiptReadError("A reused record has the wrong original source or divisor.")
        if result["field"] != Q or result["full_pair_count"] != 2662 or \
                result["m_count"] != 242 or result["solution_count_mod_sign"] != 0 or \
                result["solutions"] or not result["representatives_complete"] or \
                result["mathematical_status"] not in {
                    "NO_SOLUTION_WITH_THIS_FIXED_DIVISOR",
                    "NO_SOLUTION_WITH_THIS_TRIPLE_POLE_DIVISOR"}:
            raise ReceiptReadError("A reused record does not certify the full negative domain.")
        out.append(dict(binding, original_log_consumed_live=True))
    os.environ.pop("RANK2_ACTIONS_READ_TOKEN", None)
    return out


def poly(a):
    return nmod_poly(list(a), Q)


def enc(a):
    return [int(c) for c in a]


def ev(a, x):
    out = 0
    for c in reversed(enc(a)):
        out = (out * x + c) % Q
    return out


def exact(a, b):
    c, r = divmod(a, b)
    if not r.is_zero():
        raise ArithmeticError("A proved exact polynomial division has a remainder.")
    return c


def invmod(a, modulus):
    r0, r1 = modulus, a % modulus
    s0, s1 = poly([]), poly([1])
    while not r1.is_zero():
        c, rr = divmod(r0, r1)
        r0, r1 = r1, rr
        s0, s1 = s1, s0 - c * s1
    if r0.degree() != 0:
        raise ArithmeticError("A stated quotient-ring unit is not invertible.")
    return (s0 * pow(int(r0[0]), Q - 2, Q)) % modulus


def scalar_solutions(r0, r1):
    """All b in F_11 with r0-b*r1=0, including the zero-polynomial case."""
    if r1.is_zero():
        return list(range(Q)) if r0.is_zero() else []
    for i, ci in enumerate(enc(r1)):
        if ci:
            b = int(r0[i]) * pow(ci, Q - 2, Q) % Q
            return [b] if (r0 - b * r1).is_zero() else []
    raise ArithmeticError("Unreachable nonzero-polynomial case.")


def ring_add(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def ring_scale(a, c):
    return tuple(c * z for z in a)


def ring_times_poly(a, h):
    return tuple(z * h for z in a)


def ring_mul(a, b, f):
    out = [poly([]), poly([]), poly([])]
    for i in range(3):
        for j in range(3):
            term = a[i] * b[j]
            k = i + j
            if k >= 3:
                term *= f
                k -= 3
            out[k] += term
    return tuple(out)


def original_identity(xnum, wnum, H2, f, t):
    xt = (xnum[0] + t * H2, xnum[1], xnum[2])
    xcube = ring_mul(ring_mul(xnum, xnum, f), xnum, f)
    value = ring_add(
        ring_add(ring_scale(ring_mul(wnum, wnum, f), -3),
                 ring_scale(xcube, -4)),
        ring_scale(ring_times_poly(ring_mul(xt, xt, f), H2), -1))
    return all(z.is_zero() for z in value)


def normnum(A, B, C, f):
    return A**3 + B**3 * f + C**3 * f**2 - 3 * A * B * C * f


def update_hash(h, item):
    h.update(json.dumps(item, sort_keys=True, separators=(",", ":")).encode())
    h.update(b"\n")


def all_single_branch_pairs(f):
    """All H monic of degree 3 and J of degree <3 with H | J^3-f and Hf coprime."""
    pairs = set()
    j_count = 0
    for coeffs in itertools.product(range(Q), repeat=3):
        j_count += 1
        J = poly(coeffs)
        residue = J**3 - f
        if residue.degree() < 3:
            continue
        _, factors = residue.factor(algorithm="berlekamp")
        factors = sorted(factors, key=lambda fe: (fe[0].degree(), enc(fe[0])))
        for exponents in itertools.product(*(range(int(e) + 1) for _, e in factors)):
            if sum(int(e) * fac.degree()
                   for e, (fac, _) in zip(exponents, factors)) != 3:
                continue
            H = poly([1])
            for e, (fac, _) in zip(exponents, factors):
                H *= fac**int(e)
            if ev(H, 0) == 0 or ev(H, Q - 1) == 0:
                continue
            if H.degree() != 3 or int(H[3]) != 1 or not (residue % H).is_zero():
                raise ArithmeticError("Incorrect complete divisor enumeration.")
            pairs.add((tuple(enc(H)), tuple(enc(J))))
    if j_count != Q**3:
        raise ArithmeticError("The J domain was not completely enumerated.")
    return sorted(pairs), j_count


def main():
    started = time.monotonic()
    consumed_receipts = paid_receipts()
    y = poly([0, 1])
    f = y * (y + 1)
    t = -pow(27, Q - 2, Q) * y
    inv3 = pow(3, Q - 2, Q)
    inv12 = pow(12, Q - 2, Q)
    inv9 = pow(9, Q - 2, Q)

    enumeration_hash = hashlib.sha256()
    solution_hash = hashlib.sha256()
    records = []
    counts = {
        "J_polynomials_enumerated": 0,
        "single_branch_H_J_pairs": 0,
        "single_branch_paid_negative_domains_reused": 0,
        "single_branch_paid_logical_m_b_pairs": 0,
        "single_branch_logical_m_b_pairs": 0,
        "single_branch_m_exact_pole": 0,
        "single_branch_after_required_m_divisibility": 0,
        "single_branch_after_N_degree": 0,
        "single_branch_solutions": 0,
        "whole_fibres": 0,
        "whole_fibre_logical_B_C_pairs": 0,
        "whole_fibre_after_required_m_divisibility": 0,
        "whole_fibre_after_N_degree": 0,
        "whole_fibre_after_exact_three_poles": 0,
        "whole_fibre_solutions": 0,
    }

    def keep(kind, H, J, m, nnum, nden, xnum, wnum):
        H2, H3 = H**2, H**3
        if not original_identity(xnum, wnum, H2, f, t):
            raise ArithmeticError("A scalar candidate fails the original cubic-ring identity.")
        bounds_x = (2 * H.degree(), 2 * H.degree(), 2 * H.degree() - 1)
        bounds_w = (3 * H.degree() + 1, 3 * H.degree(), 3 * H.degree() - 1)
        if any(z.degree() > bound for z, bound in zip(xnum, bounds_x)):
            raise ArithmeticError("A returned x violates the original infinity bound.")
        if any(z.degree() > bound for z, bound in zip(wnum, bounds_w)):
            raise ArithmeticError("A returned W violates the original infinity bound.")
        vals = {}
        for label, at in (("T", 0), ("minus_T", Q - 1)):
            hx = ev(H2, at)
            hw = ev(H3, at)
            vals[label] = {
                "x": ev(xnum[0], at) * pow(hx, Q - 2, Q) % Q,
                "W": ev(wnum[0], at) * pow(hw, Q - 2, Q) % Q,
                "M": ev(m, at) * pow(ev(H, at), Q - 2, Q) % Q,
                "N": ev(nnum, at) * pow(ev(nden, at), Q - 2, Q) % Q,
            }
        if vals["T"] != {"x": (-inv3) % Q, "W": inv9,
                         "M": Q - 1, "N": (-2 * inv9) % Q}:
            raise ArithmeticError("The actual I9 endpoint has the wrong orientation.")
        if vals["minus_T"] != {"x": (-inv9) % Q, "W": 0,
                               "M": inv3, "N": pow(27, Q - 2, Q)}:
            raise ArithmeticError("The actual I3 endpoint has the wrong orientation.")
        item = {
            "polar_case": kind,
            "H": enc(H), "J": None if J is None else enc(J),
            "m": enc(m), "M_denominator": enc(H),
            "N_numerator": enc(nnum), "N_denominator": enc(nden),
            "x_numerator_basis_1_X_X2": [enc(z) for z in xnum],
            "x_denominator": enc(H2),
            "W_numerator_basis_1_X_X2": [enc(z) for z in wnum],
            "W_denominator": enc(H3),
            "original_base": "Y^2+Y=X^3; t=-Y/27",
            "original_y_return": "(delta*W-x-t)/2; delta^2=-3",
            "original_identity_zero": [True, True, True],
            "Q_intersection_O": 3,
            "I9_component": 0,
            "I3_component_in_R1027_orientation": 1,
            "height": {"numerator": 22, "denominator": 3},
            "endpoints": vals,
        }
        update_hash(solution_hash, item)
        if len(records) < 8:
            records.append(item)

    pairs, counts["J_polynomials_enumerated"] = all_single_branch_pairs(f)
    counts["single_branch_H_J_pairs"] = len(pairs)
    for h_tuple, j_tuple in pairs:
        counts["single_branch_logical_m_b_pairs"] += Q**3
        paid = PAID_NEGATIVE_PAIRS.get((h_tuple, j_tuple))
        if paid is not None:
            counts["single_branch_paid_negative_domains_reused"] += 1
            counts["single_branch_paid_logical_m_b_pairs"] += Q**3
            update_hash(enumeration_hash, {
                "case": "paid_negative_reused", "H": h_tuple, "J": j_tuple,
                "binding": paid})
            continue
        H, J = poly(h_tuple), poly(j_tuple)
        H2, H3, H4, H6 = H**2, H**3, H**4, H**6
        J2 = (J - (J**3 - f) * invmod(3 * J**2, H2)) % H2
        if not (J2**3 - f).is_zero() and not ((J2**3 - f) % H2).is_zero():
            raise ArithmeticError("The full repeated-root Hensel lift failed.")
        ji = invmod(J2, H2)
        ji2 = ji**2 % H2
        m0 = (-ev(H, 0)) % Q
        target = ev(H, Q - 1) * inv3 % Q
        update_hash(enumeration_hash, {"case": "one_branch", "H": h_tuple, "J": j_tuple})
        for m2, m3 in itertools.product(range(Q), repeat=2):
            m1 = (m0 + m2 - m3 - target) % Q
            m = poly([m0, m1, m2, m3])
            if m.gcd(H).degree() != 0:
                update_hash(enumeration_hash, [m0, m1, m2, m3, "not_exact_degree_three"])
                continue
            counts["single_branch_m_exact_pole"] += 1
            A = -(H2 + 3 * m**2) * inv12
            B0 = A * ji % H2
            C = A * ji2 % H2
            K20 = exact(6 * (A**2 - B0 * C * f) - t * H4, H2)
            linear = 6 * C * f
            choices = scalar_solutions(K20 % m, linear % m)
            counts["single_branch_after_required_m_divisibility"] += len(choices)
            update_hash(enumeration_hash, [m0, m1, m2, m3, choices])
            for b in choices:
                B = B0 + b * H2
                n = exact(K20 - b * linear, 3 * m)
                if n.degree() > 4:
                    continue
                counts["single_branch_after_N_degree"] += 1
                E = normnum(A, B, C, f)
                if not (4 * E + t**2 * H6 + 3 * n**2 * H4).is_zero():
                    continue
                xnum = (A, B, C)
                wnum = (m * A + n * H2, m * B, m * C)
                keep("one_branch_above_each_Y_place", H, J, m, n, H, xnum, wnum)
                counts["single_branch_solutions"] += 1

    # The second case is a whole fibre, not a repeated one-branch divisor.
    for c in range(Q):
        if c in (0, Q - 1):
            continue
        H = y - c
        H2, H3, H4, H6 = H**2, H**3, H**4, H**6
        m = poly([c, (4 * c + 1) * inv3 % Q])
        A = -(H2 + 3 * m**2) * inv12
        counts["whole_fibres"] += 1
        counts["whole_fibre_logical_B_C_pairs"] += Q**5
        update_hash(enumeration_hash, {"case": "whole_fibre", "c": c, "m": enc(m)})
        for c0, c1, b1, b2 in itertools.product(range(Q), repeat=4):
            C = poly([c0, c1])
            Bh = poly([0, b1, b2])
            K0 = 6 * (A**2 - Bh * C * f) - t * H4
            linear = 6 * C * f
            choices = scalar_solutions(K0 % m, linear % m)
            counts["whole_fibre_after_required_m_divisibility"] += len(choices)
            update_hash(enumeration_hash, [c0, c1, b1, b2, choices])
            for b0 in choices:
                B = Bh + b0
                k = exact(K0 - b0 * linear, 3 * m)
                if k.degree() > 4:
                    continue
                counts["whole_fibre_after_N_degree"] += 1
                E = normnum(A, B, C, f)
                if (E % H).is_zero():
                    continue
                counts["whole_fibre_after_exact_three_poles"] += 1
                if not (4 * E + t**2 * H6 + 3 * k**2).is_zero():
                    continue
                xnum = (A, B, C)
                wnum = (m * A + k, m * B, m * C)
                keep("whole_three_point_fibre", H, None, m, k, H3, xnum, wnum)
                counts["whole_fibre_solutions"] += 1

    if counts["single_branch_paid_negative_domains_reused"] != len(PAID_NEGATIVE_PAIRS):
        raise ArithmeticError("An exact previously paid negative domain was not recovered.")
    if counts["whole_fibres"] != Q - 2:
        raise ArithmeticError("The complete whole-fibre domain was not traversed.")
    if counts["single_branch_logical_m_b_pairs"] != len(pairs) * Q**3:
        raise ArithmeticError("The complete one-branch parameter domain was not traversed.")
    if counts["whole_fibre_logical_B_C_pairs"] != (Q - 2) * Q**5:
        raise ArithmeticError("The complete whole-fibre parameter domain was not traversed.")

    number = counts["single_branch_solutions"] + counts["whole_fibre_solutions"]
    result = {
        "status": "COMPLETE_ALL_DEGREE_THREE_POLAR_DIVISORS",
        "mathematical_status": (
            "ACTUAL_ORIGINAL_HEIGHT_22_OVER_3_SECTION_FOUND" if number else
            "NO_ANTI_SECTION_WITH_THE_STATED_HEIGHT_AND_ENDPOINTS"),
        "q": Q,
        "normalized_I3_orientation": 1,
        "opposite_orientation": "Obtained exactly by W,M,N -> -W,-M,-N.",
        "counts": counts,
        "paid_negative_receipts_reused": consumed_receipts,
        "enumeration_sha256": enumeration_hash.hexdigest(),
        "exact_solution_sha256": solution_hash.hexdigest(),
        "normalized_solution_count": number,
        "representatives": records,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.monotonic() - started,
        "scope": {
            "all_degree_three_effective_D_disjoint_T_minusT_O": True,
            "all_repeated_multiplicities_and_whole_tau_orbits": True,
            "assumes_Tate_at_q11": False,
            "original_27_weighted_pairs_nonzero": False,
            "ordinary_p_local_comparison_paid": False,
            "infinitely_many_p": False,
        },
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        error = {"status": "EXECUTION_ERROR", "error_type": type(exc).__name__, "message": str(exc)}
        print(json.dumps(error, sort_keys=True, separators=(",", ":")), file=sys.stderr)
        raise
