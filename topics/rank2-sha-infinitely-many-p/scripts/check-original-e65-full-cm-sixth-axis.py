#!/usr/bin/env python3
"""Original E65: all 66 CM7/CM19 columns, same-job E89, and sixth actual jet.

Public Rogerhu12/math-research-public Actions only; python-flint==0.9.0.
No generated file is read or written.  All source coefficients are rebuilt
from original complete characteristic-zero fibers.  R959 supplies the full
bad-place identification and the absolute eigenvalues; this program does not
infer that character from two eigenvalues.
"""
from __future__ import annotations
import argparse
import concurrent.futures
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time
from flint import fmpq as Q, fmpq_mat as Mat

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[3]
PREFIX = "topics/rank2-sha-infinitely-many-p/"
START = time.monotonic()
DEGREE, OFFSET, DIMENSION = 390, 0, 66
SOURCE_PINS = {
    "check-r480-actual-input-cm19.py": "3d4d9a05872cdde0f24ff756ec79407417afa943eabf6f71f4e48d32f91f9c45",
    "check-r466-fixed-two-division-source.py": "effd6f1526421cfcb9da3bd7769eed258374fa0addf337313d0315cb3ef08245",
    "check-r464-degree102-cm7-exact.py": "b3e11a9da1b28a7623d86acf944262ab23c2d1969b1f0183030a4d1c96b5f1ff",
    "check-r943-original-degree178-fifth-axis.py": "c4226727954c4f5fc8477bb17987a49242ef73103049ff7de8e004d442698ec6",
    "check-r943-degree178-full-cm-source.py": "b5c2e3f6781e1a788e2d3fd749f10e2ecab9e6c58e2950aecc9acf727f237e67",
    "check-r732-original-type-five-cm13.py": "d1b3c2f851e9ec6b6d6b6655141e36b4bb1108a30e57ff8365b5f583d880e469",
    "original_e65_local_schwartz.py": "b13ad04a3b12dd28e4e749a9b92f9bd3fcfe6bc976201f1057a5a58cf8c765d5"
}
SOURCE_FILES = [
    PREFIX + "scripts/check-original-e65-full-cm-sixth-axis.py",
    PREFIX + "scripts/original_e65_local_schwartz.py",
    *[PREFIX + "scripts/" + name for name in SOURCE_PINS
      if name != "original_e65_local_schwartz.py"],
    PREFIX + "ci/e65-full-cm-source-request.json",
    ".github/workflows/rank2-sha-e65-full-cm-source.yml",
]
assert len(SOURCE_FILES) == len(set(SOURCE_FILES)) == 10


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


D7 = module("original_e65_cm7", HERE / "check-r464-degree102-cm7-exact.py")
D19 = module("original_e65_cm19", HERE / "check-r480-actual-input-cm19.py")
LOCAL = module("original_e65_local", HERE / "original_e65_local_schwartz.py")
H = D19.H
ZERO, ONE = H["fq"](0), H["fq"](1)
omega = H["fq"](Q(-1,2), Q(1,2))
TARGET7, TARGET19 = H["fp"](omega, 2), H["fq"](-1)


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",",":")).encode()).hexdigest()


def full_fiber(task):
    norm, target = task
    if norm == 7:
        a, raw = D7.exact_fiber_row((DEGREE, OFFSET, target))
        row = [(Q(x[0]), Q(x[1])) for x in raw]
    elif norm == 19:
        a, row = D19.fiber((DEGREE, OFFSET, target))
    else:
        raise ValueError(norm)
    assert a == target and len(row) == DIMENSION
    print("R959 entire degree390 CM{} fiber {} / {} elapsed {:.3f}s".format(
        norm, target, DIMENSION+2, time.monotonic()-START), file=sys.stderr, flush=True)
    return a, row


def complete_matrix(norm, workers):
    targets = list(range(1, DIMENSION + 3))
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        rows = dict(pool.map(full_fiber, [(norm, a) for a in targets]))
    V = Mat([[Q(a**(3*j)) for j in range(DIMENSION)]
             for a in targets[:DIMENSION]])
    inverse = V.inv()
    matrices = tuple(inverse * Mat([[rows[a][j][part] for j in range(DIMENSION)]
                                   for a in targets[:DIMENSION]])
                     for part in (0, 1))
    for part in (0, 1):
        assert V * matrices[part] == Mat([
            [rows[a][j][part] for j in range(DIMENSION)]
            for a in targets[:DIMENSION]])
    for a in targets[DIMENSION:]:
        evaluation = Mat([[Q(a**(3*j)) for j in range(DIMENSION)]])
        for part in (0, 1):
            assert evaluation * matrices[part] == Mat([[rows[a][j][part]
                                                       for j in range(DIMENSION)]])
    print("R959 complete CM{} matrix returned all {} original columns and two extra full fibers".format(
        norm, DIMENSION), file=sys.stderr, flush=True)
    return matrices


def full_quadratic_nullspace(operators):
    """Whole Q(delta)-kernel via its faithful doubled rational matrix.

    No columns, imaginary coordinates or zero rows are discarded.  Every
    returned rational kernel vector and both quadratic operators are multiplied
    back before the one-dimensional target line is normalized.
    """
    n = operators[0][0].ncols()
    rows = []
    for real, imag in operators:
        assert real.nrows() == imag.nrows() and real.ncols() == imag.ncols() == n
        rows.extend([[real[i,j] for j in range(n)] +
                     [-3*imag[i,j] for j in range(n)]
                     for i in range(real.nrows())])
        rows.extend([[imag[i,j] for j in range(n)] +
                     [real[i,j] for j in range(n)]
                     for i in range(real.nrows())])
    full = Mat(rows)
    reduced, rank = full.rref()
    pivots = [next(j for j in range(2*n) if reduced[i,j])
              for i in range(rank)]
    assert pivots == sorted(set(pivots))
    free = [j for j in range(2*n) if j not in pivots]
    basis = []
    for column in free:
        v = [Q(0)]*(2*n)
        v[column] = Q(1)
        for i, pivot in enumerate(pivots):
            v[pivot] = -reduced[i,column]
        assert full * Mat([[x] for x in v]) == Mat(full.nrows(), 1)
        vector = [(v[j], v[n+j]) for j in range(n)]
        pair = (Mat([[x[0]] for x in vector]), Mat([[x[1]] for x in vector]))
        for operator in operators:
            assert H["km"](operator, pair) == (Mat(operator[0].nrows(),1),
                                                Mat(operator[0].nrows(),1))
        basis.append(vector)
    assert len(free) % 2 == 0
    return basis, {
        "complete_rational_shape":[full.nrows(),full.ncols()],
        "complete_rational_rank":rank,
        "complete_quadratic_kernel_dimension":len(free)//2,
        "all_rational_kernel_vectors_multiplied_back":True,
        "all_quadratic_operator_rows_multiplied_back":True,
        "whole_kernel_basis_sha256":canonical_hash([
            [[str(a),str(b)] for a,b in v] for v in basis])}


def construct_complete_source(workers):
    # The original CM19 sigma-leading-constant anchor, with no rephasing.
    for target in (1, DIMENSION+2):
        _, anchor = D19.fiber((4, 2, target))
        assert anchor == [H["fq"](-1)]
    A7 = complete_matrix(7, workers)
    A19 = complete_matrix(19, workers)
    identity = D19.identity(DIMENSION)
    assert H["km"](A7, A19) == H["km"](A19, A7)
    assert H["km"](A7, (A7[0], -A7[1])) == identity
    assert H["km"](A19, (A19[0], -A19[1])) == identity
    E7 = H["ka"](A7, H["ks"](identity, H["fn"](TARGET7)))
    E19 = H["ka"](A19, H["ks"](identity, H["fn"](TARGET19)))
    kernel, kernel_receipt = full_quadratic_nullspace((E7,E19))
    report = {
        "degree":DEGREE,
        "charge":195,
        "basis":"sigma^390*(1,X,...,X^65), X=x^3",
        "all_original_columns":DIMENSION,
        "full_targets_per_operator":list(range(1,DIMENSION+3)),
        "normalization":"[gamma]_*[bar_gamma]^*/gamma, original sigma carrier",
        "absolute_target_eigenvalues_Qdelta":[
            [str(x) for x in TARGET7], [str(x) for x in TARGET19]],
        "both_complete_operators_commute":True,
        "both_complete_conjugate_inverses_return":True,
        "CM19_original_Theta_squared_anchor_returned":True,
        "kernel":kernel_receipt,
        "canonical_complete_matrix_sha256":canonical_hash({
            "N7":H["serialize_matrix"](A7), "N19":H["serialize_matrix"](A19)})}
    print("R959_SOURCE_STAGE " + json.dumps(report, sort_keys=True, separators=(",",":")),
          file=sys.stderr, flush=True)
    assert kernel_receipt["complete_quadratic_kernel_dimension"] == 1, (
        "Actual complete target eigenspace needs further separation; no arbitrary line was selected")
    v = kernel[0]
    lead = max(i for i,x in enumerate(v) if x != ZERO)
    v = [H["fm"](x,H["fi"](v[lead])) for x in v]
    # Both rational vectors form the same complete K-line.
    for other in kernel:
        scalar = other[lead]
        assert other == [H["fm"](scalar,x) for x in v]
    assert lead == DIMENSION-2, "Actual first positive order is not six"
    assert v[-1] == ZERO and v[-2] == ONE
    assert all(b == 0 for a,b in v), "The identified full line is not rational"
    pair = (Mat([[a] for a,b in v]), Mat([[b] for a,b in v]))
    assert H["km"](A7,pair) == H["ks"](pair,TARGET7)
    assert H["km"](A19,pair) == H["ks"](pair,TARGET19)
    coefficients = [Fraction(str(a)) for a,b in v[:-1]]
    assert len(coefficients) == 65 and coefficients[-1] == 1
    denominator = math.lcm(*(x.denominator for x in coefficients))
    report.update({
        "status":"PASS",
        "source_origin_order":DEGREE-6*lead,
        "complete_original_mass_column_zero":True,
        "source_rational":True,
        "whole_source_returned_under_both_original_operators":True,
        "source_denominator":str(denominator),
        "source_polynomial_X_ascending_sha256":
            canonical_hash([str(x) for x in coefficients]),
        "output_coefficients_embedded_in_code":False})
    return coefficients, report


def sixth_actual_jet(coefficients):
    # Import executes the pinned complete E89 CM7/CM13 producer in THIS job.
    # The 29 source coefficients are consumed only from its in-memory result.
    old = module("original_e65_actual_five_sources",
                 HERE / "check-r943-original-degree178-fifth-axis.py")
    assert len(old.SOURCE_ASC) == 29 and old.SOURCE_ASC[-1] == 1
    # The existing routine constructs the actual five full-source jets at its
    # declared series length.  Its old local b5 return is deliberately unused:
    # both the five-column minor and six-column determinant are formed below.
    old.N = 6
    five, _, _ = old.source_jets()
    assert len(five) == 5 and all(len(jet) == 6 for name,jet in five)
    W = [Fraction(1), Fraction(-1,7)] + [Fraction(0)]*4
    for n in range(2,6):
        W[n] = sum(W[i]*W[n-i] for i in range(1,n))/((6*n+1)*(n-1))
    log_sigma = [Fraction(0)] + [
        -W[n]/(6*n*(6*n-1)) for n in range(1,6)]
    argument = old.smul([Fraction(0),Fraction(1)],old.spow(W,-3))
    sixth = old.smul(old.sexp([390*x for x in log_sigma]),
                     old.smul(old.spow(W,192),
                              old.compose(list(reversed(coefficients)),argument)))
    assert len(sixth) == 6 and sixth[0] == 1
    all_jets = five + [("Z390",sixth)]
    b5 = old.determinant([list(reversed(jet[:5])) for name,jet in five])
    b6 = old.determinant([list(reversed(jet)) for name,jet in all_jets])
    assert b5, "Same-job old five actual jets failed their original independence"
    return {
        "status":"PASS" if b6 else "SIX_ACTUAL_JETS_DEPENDENT",
        "same_job_old_E89_full_CM_rebuilt":True,
        "old_E89_CM_matrix_sha256":
            "6ee0222d90db6add172d6d6e650a2f8186b1776072661594a242b4e65c78d665",
        "old_E89_source_polynomial_sha256":
            canonical_hash([str(x) for x in old.SOURCE_ASC]),
        "source_names":[name for name,jet in all_jets],
        "source_charges":[17,36,68,33,89,195],
        "physical_rows_order":"[w^6,w^5,w^4,w^3,w^2,w] of each full source",
        "jets_F_divided_by_w_ascending":
            {name:[str(x) for x in jet] for name,jet in all_jets},
        "same_job_actual_B5_determinant":str(b5),
        "same_job_actual_B6_determinant":str(b6),
        "actual_B6_nonzero":bool(b6),
        "permanent_source_relations_removed_by_actual_CM_identification":True,
        "all_source_coefficients_generated_in_same_job":True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers",type=int,default=4)
    args = parser.parse_args()
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    request_path = ROOT / (PREFIX + "ci/e65-full-cm-source-request.json")
    request = json.loads(request_path.read_text())
    assert request["schema"] == "rank2-original-e65-full-cm-sixth-axis/v1"
    assert request["degree"] == DEGREE and request["workers"] == args.workers
    assert request["python_flint_version"] == "0.9.0"
    assert request["complete_CM_norms"] == [7,19]
    assert request["same_job_complete_E89_rebuild"] is True
    assert request["whole_five_plus_one_actual_jets"] is True
    import flint
    assert flint.__version__ == "0.9.0"
    hashes = {name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
              for name in SOURCE_FILES}
    for name,digest in SOURCE_PINS.items():
        assert hashes[PREFIX+"scripts/"+name] == digest, name
    manifest = {
        "schema":"rank2-original-e65-source-manifest/v1",
        "source_commit":os.environ["GITHUB_SHA"],
        "run_id":int(os.environ["GITHUB_RUN_ID"]),
        "request":request,
        "source_count":len(hashes),
        "source_sha256":hashes}
    print("R959_SOURCE_MANIFEST " + json.dumps(manifest,sort_keys=True,separators=(",",":")),
          file=sys.stderr,flush=True)
    local = LOCAL.check_original_e65_local_schwartz()
    print("R959 all original local Schwartz checks passed",file=sys.stderr,flush=True)
    coefficients, source = construct_complete_source(args.workers)
    jets = sixth_actual_jet(coefficients)
    result = {
        "schema":"rank2-original-e65-full-cm-sixth-axis-result/v1",
        "status":"PASS" if jets["actual_B6_nonzero"] else "SOURCE_PASS_SIX_JETS_DEPENDENT",
        "curve":"y^2=x^3+65",
        "full_local_Schwartz":local,
        "actual_source":source,
        "actual_six_jets":jets,
        "source_manifest_sha256":canonical_hash(manifest),
        "elapsed_seconds":time.monotonic()-START,
        "ordinary_infinite_prime_nonvanishing_proved":False,
        "inert_infinite_prime_nonvanishing_proved":False,
        "global_deep_kernel_proved":False,
        "output_files":False,
        "scope":"Original full E65 source and the six actual low jets; no transfer of central zero to products."}
    encoded = json.dumps(result,sort_keys=True,separators=(",",":"))
    print(encoded,flush=True)
    if request["require_sixth_jet_independence"]:
        assert jets["actual_B6_nonzero"], "Actual sixth low-jet independence failed"


if __name__ == "__main__":
    main()
