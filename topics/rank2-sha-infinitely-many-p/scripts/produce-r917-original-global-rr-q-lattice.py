#!/usr/bin/env sage-python
"""R917: the complete original global M2 / S RR lattice from exact q jets.

Mathematics runs only in the public repository Actions.  The input rows come
from the persistent complete PARI M2(867) space, never from guessed q series.
No coefficient output file is created.  This context has no degree48
function-field elements or closed-point evaluator.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical producer only in the public repository Actions.")

import argparse
import hashlib
import json
import time
from pathlib import Path
from sage.all import QQ, ZZ, GF, PowerSeriesRing, matrix, diagonal_matrix
from sage.env import SAGE_VERSION
from original_pari_m2_basis import PariOriginalM2Basis
import original_pari_m2_basis

STARTED = time.monotonic()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def matrix_digest(M):
    return digest([[str(x) for x in row] for row in M.rows()])


def progress(stage, **kw):
    print("RANK2_R917_STAGE " + canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **kw)), flush=True)


def assert_integral_at(M, prime):
    assert all(ZZ(x.denominator()) % prime for x in M.list())


def reduce_at(M, k):
    p = ZZ(k.characteristic())
    assert_integral_at(M, p)
    return matrix(k, M.nrows(), M.ncols(),
                  [k(x.numerator())/k(x.denominator()) for x in M.list()])


def saturate_original_rows(original, prime):
    """Exact Z_(prime)-saturation in the same QQ row space, with full transform."""
    p = ZZ(prime)
    assert p.is_prime()
    assert original.base_ring() is QQ
    r, length = original.nrows(), original.ncols()
    assert 0 < r <= length
    columns = tuple(original.pivots())
    assert len(columns) == r
    scales = []
    for row in original.rows():
        nonzero = [x for x in row if x]
        assert nonzero
        v = min(int(x.valuation(p)) for x in nonzero)
        scales.append(QQ(p)**(-v))
    transform = diagonal_matrix(QQ, scales)
    current = transform*original
    assert_integral_at(current, p)
    determinant = current.matrix_from_columns(columns).determinant()
    assert determinant
    current_index = int(determinant.valuation(p))
    assert current_index >= 0
    initial_index = current_index
    k = GF(p)
    steps = []
    progress("original full rational rows made prime-integral",
             prime=int(p), rows=r, coefficients=length,
             fixed_minor_columns=list(columns),
             fixed_minor_initial_valuation=initial_index)

    while True:
        reduced = reduce_at(current, k)
        rank = int(reduced.rank())
        if rank == r:
            break
        kernel = reduced.left_kernel().basis_matrix().echelon_form()
        d = int(kernel.nrows())
        assert d == r-rank and d > 0
        assert kernel*reduced == 0
        pivots = tuple(kernel.pivots())
        assert len(pivots) == d
        complement = [j for j in range(r) if j not in set(pivots)]
        rows = [[QQ(1 if j == i else 0) for j in range(r)]
                for i in complement]
        rows.extend([[QQ(ZZ(x)) for x in row] for row in kernel.rows()])
        U = matrix(QQ, rows)
        assert U.nrows() == r and U.ncols() == r
        udet = U.determinant()
        assert udet and udet.valuation(p) == 0
        divided = diagonal_matrix(QQ, [QQ.one()]*(r-d)+[QQ(1)/p]*d)*U
        current = divided*current
        transform = divided*transform
        assert_integral_at(current, p)
        determinant = current.matrix_from_columns(columns).determinant()
        assert determinant
        next_index = int(determinant.valuation(p))
        assert 0 <= next_index == current_index-d
        steps.append({"previous_rank":rank, "kernel_dimension":d,
                      "fixed_minor_valuation_before":current_index,
                      "fixed_minor_valuation_after":next_index})
        current_index = next_index
        assert len(steps) <= initial_index
        progress("exact original local saturation step",
                 prime=int(p), step=len(steps), **steps[-1])

    assert transform*original == current
    reduced = reduce_at(current, k)
    assert reduced.rank() == r
    assert int(current.matrix_from_columns(columns).determinant().valuation(p)) == current_index
    record = {
        "prime":int(p), "dimension":r, "jet_coefficients":length,
        "fixed_minor_columns":list(columns),
        "initial_minor_valuation":initial_index,
        "final_minor_valuation":current_index,
        "strict_saturation_steps":steps,
        "total_index_descent":initial_index-current_index,
        "full_rational_transform_verified":True,
        "all_final_denominators_prime_units":True,
        "full_reduced_rank":r,
        "input_rational_rows_sha256":matrix_digest(original),
        "saturated_rational_rows_sha256":matrix_digest(current),
        "rational_basis_transform_sha256":matrix_digest(transform),
        "complete_reduced_rows_sha256":matrix_digest(reduced),
    }
    return current, transform, reduced, record


def original_denominator(k, precision):
    ring = PowerSeriesRing(k, "Q", default_prec=precision)
    coefficients = [k.one()]
    for n in range(1, precision):
        value = 12*sum(ZZ(n).divisors())
        if n % 3 == 0:
            value -= 36*sum(ZZ(n//3).divisors())
        coefficients.append(k(value))
    S = ring(coefficients).add_bigoh(precision)
    assert S[0] == 1
    return ring, S


def build_original_global_rr_q_lattice(prime=29, q_precision=205):
    prime, q_precision = int(prime), int(q_precision)
    assert prime in (29, 41)
    assert q_precision >= 205
    owner = PariOriginalM2Basis(progress)
    owner.ensure_precision(q_precision)
    full_rows = matrix(QQ, owner.columns)
    assert full_rows.nrows() == 120 and full_rows.ncols() == q_precision
    exact_rows = full_rows[:, :205]
    progress("start exact local saturation of the complete original M2",
             prime=prime, dimension=120, jet_coefficients=205)
    saturated, transform, reduced, saturation = saturate_original_rows(exact_rows, prime)
    k = GF(prime)
    full_saturated = transform*full_rows
    assert full_saturated[:, :205] == saturated
    assert_integral_at(full_saturated, ZZ(prime))
    full_reduced = reduce_at(full_saturated, k)
    assert full_reduced[:, :205] == reduced
    ring, S = original_denominator(k, q_precision)
    Sinv = 1/S
    rr_rows = []
    for row in full_reduced.rows():
        rr = (ring(list(row)).add_bigoh(q_precision)*Sinv).add_bigoh(q_precision)
        rr_rows.append([k(rr[j]) for j in range(q_precision)])
    rr_jets = matrix(k, rr_rows)
    assert rr_jets[:, :205].rank() == 120
    progress("complete original global RR q lattice certified",
             prime=prime, original_divisor_degree=204,
             complete_dimension=120, complete_sturm_rank=120,
             q_precision=q_precision)

    context = {
        "kind":"rank2_original_global_rr_q_lattice_context",
        "prime":prime, "constants":k, "weight":2,
        "original_divisor":"D_S = div(dT/T) + all 36 cusps",
        "original_denominator_q_series":S,
        "rational_source_owner":owner,
        "rational_source_forms":owner.forms,
        "rational_basis_transform":transform,
        "global_modular_form_jets":full_reduced,
        "original_rr_jets":rr_jets,
        "q_precision":q_precision,
        "function_field_context_available":False,
        "closed_point_evaluator_available":False,
    }
    result = {
        "kind":"rank2_original_global_rr_q_lattice",
        "status":"exact_global_space_and_integral_lattice_only",
        "certified_original_global_rr_space":True,
        "existing_function_field_frontend_certified":False,
        "original_shadow_computed":False,
        "level":867, "weight":2, "prime":prime,
        "genus":85, "all_geometric_cusps":36,
        "original_divisor_degree":204,
        "complete_dimension":120, "complete_sturm_rank":120,
        "jet_precision":q_precision,
        "original_denominator":"S=(3*E2(Q^3)-E2(Q))/2; constant 1",
        "full_original_rr_jets_sha256":matrix_digest(rr_jets),
        "original_S_jets_sha256":digest([int(S[j]) for j in range(q_precision)]),
        "saturation":saturation,
        "rational_source_provenance":owner.provenance,
        "scope":(
            "The complete original global L(D_S), from the same authenticated "
            "rational modular-form space and exact local saturation. "
            "No degree48 basis coordinates, original T/U/V evaluation, "
            "closed-point divisor, or Frobenius shadow is certified."),
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID", os.environ.get("GITHUB_RUN_ID")),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "sage_version":SAGE_VERSION,
        "image":os.environ.get("RANK2_IMAGE"),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{
            "original_pari_m2_basis.py":hashlib.sha256(
                Path(original_pari_m2_basis.__file__).read_bytes()).hexdigest()},
        "readme_blobs":{
            "README.md":os.environ.get("RANK2_ROOT_README_SHA"),
            "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    return context, result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    parser.add_argument("--q-precision", type=int, default=205)
    args = parser.parse_args()
    context, result = build_original_global_rr_q_lattice(args.prime, args.q_precision)
    globals()["ORIGINAL_RR_Q_LATTICE_CONTEXT"] = context
    payload = canonical(result)
    print("RANK2_R917_RESULT " + payload, flush=True)
    print("RANK2_R917_SHA256 " + hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        progress("failed", exception_type=type(exc).__name__, message=str(exc))
        raise
