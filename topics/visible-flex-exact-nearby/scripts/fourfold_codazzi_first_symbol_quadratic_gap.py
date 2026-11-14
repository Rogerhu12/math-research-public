#!/usr/bin/env python3
"""Certify the four-root arithmetic after a specified first scalar phase.

Only the completed explicit-family finite-part native is consumed.
The full scalar return coefficient and root matching remain separate.
All new integer and directed arithmetic runs only in public Actions.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import platform
import time
import flint
from flint import arb, ctx

PUBLIC = "Rogerhu12/math-research-public"
INPUT_SHA = "06070fd3b4bd7a3e4ba17d99821c0f6ad06393863bf538f9a8157b6187e60dbb"
A = 5831714953207175
B = 21212218271020390
PREFIX = (0,3,1,1,1,3,7,1,3,1,1,1,2,2,1,15,5,4,8)
N0 = 2**34
FIRST = 97

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def exact(x):
    x = Fraction(x)
    return arb(x.numerator)/x.denominator

def box(r):
    return arb(r["lower"]).lower().union(arb(r["upper"]).upper())

def record(x):
    x = arb(x)
    if not x.is_finite():
        raise ArithmeticError("nonfinite directed arithmetic")
    return dict(ball=x.str(70), lower=x.lower().str(70), upper=x.upper().str(70))

def save(path, doc):
    path = Path(path)
    raw = (json.dumps(doc, indent=2, allow_nan=False)+"\n").encode()
    if path.suffix == ".gz":
        raw = gzip.compress(raw, mtime=0)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".partial")
    temporary.write_bytes(raw)
    temporary.replace(path)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--topic", type=Path, required=True)
    p.add_argument("--coefficient", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != PUBLIC):
        raise RuntimeError("mathematics runs only in this public repository Actions")
    if platform.python_version() != "3.12.14" or flint.__version__ != "0.9.0":
        raise RuntimeError("the pinned directed arithmetic runtime is required")
    if args.out.exists():
        raise FileExistsError("preserve every original arithmetic outcome")
    ctx.prec = 320
    start = time.monotonic()
    doc = dict(
        kind="actual_complete_quadratic_norm_gap_for_selected_finite_part_scalar",
        complete=False, arithmetic_gap_complete=False, failure=None,
        public_repository=PUBLIC, public_run_id=os.environ["GITHUB_RUN_ID"],
        public_run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__), coefficient_input_sha256=sha(args.coefficient),
        bits=320, gates=[], candidates=[], convergence_records=[],
        exact_rho=dict(A=str(A), B=str(B), radical="sqrt(5)"),
        first_retained_high_index=FIRST, exact_high_norm_cutoff=str(N0),
        exact_small_gap_candidate_constant="65",
        coefficient_is_minus_one_quarter_of_selected_finite_part_only=True,
        actual_full_return_beta_identification_proved=False,
        actual_root_finite_coefficient_or_strong_remainder_paid=False,
        original_scalar_germs_or_finite_part_integrals_recomputed=0,
        original_phase_or_root_Newton_steps_recomputed=0)

    def checkpoint(stage):
        doc.update(stage=stage, seconds=time.monotonic()-start)
        save(args.out, doc)

    def gate(name, value):
        ok = bool(value)
        doc["gates"].append(dict(name=name, passed=ok))
        if not ok:
            raise ArithmeticError(name)

    checkpoint("started")
    try:
        raw = args.coefficient.read_bytes()
        original = json.loads(gzip.decompress(raw))
        gate("the completed actual selected-parameter finite part is consumed unchanged",
            sha(args.coefficient) == INPUT_SHA
            and original["complete"] and original["transfer_enclosure_complete"]
            and str(original["public_run_id"]) == "43597209022"
            and original["source_sha256"] == "de12b8129caeb8c51857f6b44a152c7a91e1facbdc553d2bd4f4ea320a38406a"
            and original["actual_affine_parameter"] == "eta_0"
            and original["exact_affine_offset"] == "0"
            and original["full193_direction_and_independent_even_mean_retained"]
            and len(original["rows"]) == 3146
            and all(g["passed"] for g in original["gates"]))
        beta = box(original["minus_quarter_of_selected_finite_part_with_no_full_return_identification"])
        pi, sqrt5 = arb.pi(), arb(5).sqrt()
        b_interval = beta/(2*pi)
        rho = (A+sqrt5)/B
        gate("the full coefficient interval has the declared M four bound", abs(b_interval) < 4)

        pp, pv, qq, qv = 0, 1, 1, 0
        for partial in PREFIX:
            pp, pv = pv, partial*pv+pp
            qq, qv = qv, partial*qv+qq
        determinant = pv*qq-pp*qv
        A0 = pv*qq+pp*qv+2*pp*qq-2*pv*qv
        B0 = 2*(qq*qq+qv*qq-qv*qv)
        gate("the exact unimodular continued fraction is the specified quadratic target",
            abs(determinant) == 1 and determinant*A0 == A and determinant*B0 == B
            and max(PREFIX[1:]) == 15)
        gate("the primitive integer quadratic form has exactly discriminant five",
            B % 2 == 0 and (A*A-5) % (2*B) == 0)
        a = B//2
        c = (A*A-5)//(2*B)
        gate("the exact positive quadratic leading coefficient is below two to fifty four",
            a > 0 and a < 2**54 and A*A-4*a*c == 5)
        norm_interval = 16*sqrt5*b_interval
        gate("the entire limiting norm interval lies inside the checked integer range",
            abs(norm_interval) < 512)
        norm_distances = [(k, abs(norm_interval-k).lower()) for k in range(-512,513)]
        nearest_integer, mu_actual = min(norm_distances, key=lambda z: z[1])
        gate("the full limiting norm interval is more than one eighth from every integer",
            mu_actual > exact(Fraction(1,8)))
        mu = exact(Fraction(1,8))
        d_high_ball = mu/(64*sqrt5)
        d_high = d_high_ball.lower()
        gate("the exact high cutoff pays the full quadratic correction uniformly",
            arb(N0*N0) >= 64*a*(4+d_high_ball.upper())**2/mu)
        doc.update(
            coefficient_interval=record(beta), phase_coefficient_interval=record(b_interval),
            exact_integer_polynomial=dict(a=str(a), b=str(-A), c=str(c), discriminant="5"),
            exact_prefix=list(PREFIX), exact_prefix_determinant=determinant,
            limiting_norm_interval=record(norm_interval),
            closest_limiting_integer=nearest_integer,
            actual_limiting_integer_distance_lower=record(mu_actual),
            selected_limiting_distance_lower="1/8",
            high_distance_times_abs_n_lower=record(d_high))

        # Complete exact convergent basis cover; the infinite tail is all ones.
        convergents = []
        pp, pv, qq, qv = 0, 1, 1, 0
        index = 0
        while True:
            partial = PREFIX[index] if index < len(PREFIX) else 1
            pp, pv = pv, partial*pv+pp
            qq, qv = qv, partial*qv+qq
            convergents.append((pv,qv,partial))
            if qv >= 4*N0:
                break
            index += 1
            if index > 4096:
                raise ArithmeticError("exact continued fraction cover unexpectedly incomplete")
        gate("the exact convergent cover reaches the complete finite denominator cutoff",
            convergents[0][:2] == (0,1) and convergents[-1][1] >= 4*N0
            and all(convergents[k][1] < convergents[k+1][1]
                    for k in range(len(convergents)-1)))
        finite_min = arb(1)/16
        worst = None
        seen = set()
        residues = {str(k):0 for k in range(4)}
        for k in range(len(convergents)-1):
            pk,qk,_ = convergents[k]
            pprev,qprev = convergents[k-1][:2] if k else (1,0)
            pnext,qnext,anext = convergents[k+1]
            if abs(pk*qprev-pprev*qk) != 1 or qnext != anext*qk+qprev:
                raise ArithmeticError("a true continued fraction basis lost unimodularity")
            count = 0
            for v in range(-66,67):
                for u0 in range(-66,anext+68):
                    N = u0*qk+v*qprev
                    if not (4*FIRST <= N < 4*N0 and N % 4 == 0 and qk <= N < qnext):
                        continue
                    P = u0*pk+v*pprev
                    if (P,N) in seen:
                        raise ArithmeticError("a finite candidate was repeated")
                    seen.add((P,N))
                    n = N//4
                    u_phase = n*(arb(P)/4-n*rho)
                    distance = abs(b_interval-u_phase).lower()
                    norm_integer = a*P*P-A*P*N+c*N*N
                    # This exact polynomial identity is also checked in the
                    # actual directed environment for every retained pair.
                    identity = 16*sqrt5*u_phase+16*a*u_phase*u_phase/(n*n)
                    if not identity.contains(arb(norm_integer)):
                        raise ArithmeticError("the integer norm and its directed identity disagree")
                    item = dict(convergent_index=k, basis_u=u0, basis_v=v,
                        exact_P=str(P), exact_N=str(N), index_n=n, fourth_root_residue=P%4,
                        coefficient_resonance_u=record(u_phase),
                        full_coefficient_distance_lower=record(distance),
                        exact_quadratic_norm=str(norm_integer))
                    doc["candidates"].append(item)
                    count += 1
                    residues[str(P%4)] += 1
                    if not distance > 0:
                        doc["unseparated_candidate"] = item
                        raise ArithmeticError("the actual full coefficient interval contains an unresolved finite divisor")
                    if distance < finite_min:
                        finite_min = distance
                        worst = item
            doc["convergence_records"].append(dict(index=k,p=str(pk),q=str(qk),
                previous_p=str(pprev),previous_q=str(qprev),next_q=str(qnext),
                next_partial=anext,full_basis_u_range=[-66,anext+67],
                full_basis_v_range=[-66,66],retained_candidates=count))
            checkpoint("complete-convergent-prefix")
        gate("all retained finite divisor intervals have a strictly positive directed separation",
            finite_min > 0 and len(seen) == len(doc["candidates"]))
        common = min(arb(1)/16,finite_min,d_high).lower()
        exponent = None
        for power in range(1,2049):
            if exact(Fraction(1,2**power)) < common:
                exponent = power
                break
        gate("an explicit rational uniform gap survives all four roots and every high integer",
            exponent is not None)
        epsilon = Fraction(1,2**exponent)
        doc.update(complete=True, arithmetic_gap_complete=True,
            complete_finite_candidates=len(seen), candidate_counts_by_fourth_root=residues,
            complete_finite_distance_times_abs_n_lower=record(finite_min),
            worst_finite_candidate=worst,
            complete_common_distance_times_abs_n_lower=record(common),
            exact_uniform_distance_times_abs_n_lower=str(epsilon),
            exact_uniform_complex_gap_times_abs_n_lower=str(4*epsilon),
            exact_scalar_inverse_one_derivative_constant=str(1/(4*epsilon)),
            explicit_gap_covers_every_abs_index_at_least=FIRST,
            exact_finite_denominator_interval=[str(4*FIRST),str(4*N0)],
            infinite_tail_proved_by_integer_norm=True,
            finite_cover_proved_by_complete_convergent_basis=True,
            all_fourth_roots_and_both_signs_of_frequency_covered=True,
            low193_head_and_mean_retained=True)
        checkpoint("complete")
        print(json.dumps(dict(complete=True,candidates=len(seen),
            complex_gap_times_index=str(4*epsilon),
            scalar_inverse_constant=str(1/(4*epsilon)),
            full_return_beta_identified=False)),flush=True)
    except BaseException as exc:
        doc["failure"] = dict(type=type(exc).__name__,message=str(exc))
        checkpoint("failed-prefix-preserved")
        raise

if __name__ == "__main__":
    main()
