#!/usr/bin/env python3
"""R987/R993/R992/R1004 public entry: complete direct22 CM and exact13 torsion boundaries.

All 24 full fibers for BOTH operators are reconstructed from the unchanged
canonical norm7/norm19 formulas.  The two extra fibers, every mass column,
commutation, conjugate inverses, twelfth powers, and the exact existing full22
hash are checked before the new thirteen-local consumer is called.  Nothing
is read from generated mathematical output; no degree390 producer is run.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time


HERE = Path(__file__).resolve().parent
SOURCE_PINS = {
    "check-r464-degree102-cm7-exact.py": "b3e11a9da1b28a7623d86acf944262ab23c2d1969b1f0183030a4d1c96b5f1ff",
    "check-r466-fixed-two-division-source.py": "effd6f1526421cfcb9da3bd7769eed258374fa0addf337313d0315cb3ef08245",
    "check-r480-actual-input-cm19.py": "3d4d9a05872cdde0f24ff756ec79407417afa943eabf6f71f4e48d32f91f9c45",
}


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def initialize():
    global D7, D19
    D7 = module("r987_actual_norm7", HERE / "check-r464-degree102-cm7-exact.py")
    D19 = module("r987_actual_norm19", HERE / "check-r480-actual-input-cm19.py")


def fiber_task(task):
    norm, value = task
    Q = D19.H["Q"]
    if norm == 7:
        target, raw = D7.exact_fiber_row((130, 2, value))
        row = [(Q(c[0]), Q(c[1])) for c in raw]
    elif norm == 19:
        target, row = D19.fiber((130, 2, value))
    else:
        raise ValueError(norm)
    assert target == value and len(row) == 22
    return norm, value, row


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematical execution requires the named public Actions repository")
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    assert 1 <= args.workers <= 4
    started = time.monotonic()
    for name, expected in SOURCE_PINS.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected
    initialize()
    H = D19.H
    Q, Mat = H["Q"], H["Mat"]
    km, ka, ks, K = H["km"], H["ka"], H["ks"], H["fq"]
    values = list(range(1, 25))
    tasks = [(norm, value) for norm in (7, 19) for value in values]
    rows = {7: {}, 19: {}}
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers,
                                                initializer=initialize) as pool:
        for norm, value, row in pool.map(fiber_task, tasks):
            rows[norm][value] = row
    V = Mat([[Q(a**(3*j)) for j in range(22)] for a in values[:22]])
    inverse = V.inv()
    matrices = []
    for norm in (7, 19):
        B = tuple(inverse*Mat([[rows[norm][a][j][part] for j in range(22)]
                              for a in values[:22]]) for part in (0, 1))
        for a in values:
            ev = Mat([[Q(a**(3*j)) for j in range(22)]])
            for part in (0, 1):
                assert ev*B[part] == Mat([[rows[norm][a][j][part] for j in range(22)]])
        matrices.append(B)
    I = H["identity"](22)
    for B in matrices:
        assert km(B, (B[0], -B[1])) == I
        value = I
        for j in range(12):
            value = km(value, B)
        assert value == I
    assert km(matrices[0], matrices[1]) == km(matrices[1], matrices[0])
    full_hash = digest({"N7": H["serialize_matrix"](matrices[0]),
                        "N19": H["serialize_matrix"](matrices[1])})
    assert full_hash == "aed9d071b6bf9b8b2751b253883fc2664e2dd19724edec8383c5a7f3e4017113"
    context = {"H": H, "B7": matrices[0], "B19": matrices[1],
               "dimension": 22, "degree": 130, "offset": 2,
               "construction_origin": "direct_complete_24_fibers_each",
               "canonical_complete_matrix_sha256": full_hash}
    print("R987 direct complete22 matrices returned every column and both extra fibers; hash="+full_hash,
          file=sys.stderr, flush=True)
    helper = module("r987_actual_thirteen_pair", HERE / "check-original-thirteen-torsion-forced-pair.py")
    pair = helper.check_original_thirteen_torsion_pair(context)
    boundary_helper = module("r993_actual_thirteen_boundary", HERE / "check-original-thirteen-boundary-weights.py")
    boundary = boundary_helper.check_original_thirteen_boundary_weights(context)
    zero_helper = module("r992_actual_thirteen_zero", HERE / "check-original-thirteen-inert-zero-source.py")
    zero_source = zero_helper.check_original_thirteen_inert_zero_source(context)
    sixth_helper = module("r1004_actual_thirteen_sixth", HERE / "check-original-thirteen-full-sixth-jet.py")
    sixth = sixth_helper.check_original_thirteen_full_sixth_jet(context)
    source_files = [Path(__file__).name, "check-original-thirteen-torsion-forced-pair.py",
                    "check-original-thirteen-boundary-weights.py",
                    "check-original-thirteen-inert-zero-source.py",
                    "check-original-thirteen-full-sixth-jet.py", *SOURCE_PINS]
    metadata = [{"path": name, "bytes": (HERE/name).stat().st_size,
                 "sha256": hashlib.sha256((HERE/name).read_bytes()).hexdigest()}
                for name in source_files]
    result = {"status": "PASS", "format": "R987/R993 complete direct22, actual13 pair and full boundary weights",
              "workers": args.workers, "source_files": metadata,
              "source_manifest_sha256": digest(metadata),
              "full_operator_basis": "sigma^130*x^2*X^j, j=0,...,21, X=x^3",
              "complete_fiber_values_each": values,
              "number_of_complete_fibers": 48,
              "all_twenty_two_columns_including_mass": True,
              "two_extra_full_fibers_each_returned": True,
              "full_conjugate_inverse_commutation_twelfth_powers": True,
              "canonical_complete_matrix_sha256": full_hash,
              "actual_thirteen_torsion_pair": pair,
              "actual_thirteen_boundary_weights": boundary,
              "actual_thirteen_inert_zero_source": zero_source,
              "actual_thirteen_full_sixth_jet": sixth,
              "elapsed_seconds": time.monotonic()-started}
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

