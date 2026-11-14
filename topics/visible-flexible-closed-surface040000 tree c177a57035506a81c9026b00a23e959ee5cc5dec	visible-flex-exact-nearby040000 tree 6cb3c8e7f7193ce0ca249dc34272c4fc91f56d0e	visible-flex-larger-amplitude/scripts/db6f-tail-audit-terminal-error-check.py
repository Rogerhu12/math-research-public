#!/usr/bin/env python3
"""Independent scalar/hash audit of the already observed genuine M12 negative replay.

This does not import the terminal gate, run its candidate branch, or create a
candidate.  It is a reproducible check of a closed negative replay and of the
exact comparison lemma.  The code review of the candidate branch is separate.
"""
import argparse
import ast
from fractions import Fraction
import hashlib
import json
from pathlib import Path


TOPIC = Path(__file__).resolve().parents[1]
STEM = "2026-11-09-db6f-"
SOURCE_SHA = "1be7add52ec2c06653a2a64baa8653e675559a55551cf22603d14a80f9cfb234"
METHOD_SHA = "06dc6928cd0581ec7e0ccde947ab9de2dc9adff351d3598cd31703fad8b7fb5a"
REPLAY_SHA = "3f75f6668aaf0c90dbca169e353a6eb9d8df38de8e01b24acf0bafcd7daaa213"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def binding(path, expected):
    value = digest(path)
    require(value == expected, "Changed frozen file: " + str(path))
    return {"file": str(path), "sha256": value, "bytes": path.stat().st_size}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(not args.out.exists(), "Refusing to overwrite an existing audit")
    source = TOPIC / "scripts/db6f-audit-terminal-error-gate.py"
    method = TOPIC / "notes" / (STEM + "audit-terminal-error-gate-method.md")
    author = TOPIC / "notes" / (STEM + "audit-terminal-error-m12-negative.json")
    replay = TOPIC / "notes" / (STEM + "tail-review-terminal-error-m12-negative.json")
    inputs = {"source": binding(source, SOURCE_SHA), "method": binding(method, METHOD_SHA),
              "author_negative": binding(author, REPLAY_SHA), "independent_negative": binding(replay, REPLAY_SHA)}
    require(author.read_bytes() == replay.read_bytes(), "Negative replay differs from author output")
    data = json.loads(replay.read_text())
    require(data["status"] == "EXPECTED_REJECTION" and data["test_only"] is True,
            "Not the genuine closed negative test")
    for key in ("certificate_issued", "candidate_binding_branch_executed", "future_candidate_was_created",
                "numerical_backends_imported", "radial_grid_evaluated", "metric_curvature_recomputed",
                "packet_or_manifest_generated", "fixed_g_convergence_gate_5_paid",
                "independent_final_full_pipeline_verified", "infinite_solution_existence_proved", "README_complete"):
        require(data[key] is False, "Unexpected positive claim: " + key)
    require(data["actual_new_root_flow_solver_calls"] == 0, "Unexpected numerical solve")
    require(data["script_sha256"] == SOURCE_SHA, "Replay is not from the frozen source")

    # Inspect the imports without executing the reviewed source.
    tree = ast.parse(source.read_text())
    modules = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            modules.append(node.module)
    require(set(modules) <= {"__future__", "argparse", "fractions", "gzip", "hashlib", "json", "pathlib"},
            "Unexpected backend or dependency import")

    # These constants and the old upper are independently fixed here; no gate
    # function or its own scalar routine is imported or called.
    B = Fraction(1, 500000000)
    F = Fraction(195883, 20000)
    L = Fraction(370012576184137, 18889465931478580854784)
    U = Fraction(38493756262750339563330485335957988971213899,
                 1496577676626844588240573268701473812127674924007424)
    margin = Fraction(61863470598928509, 23058430092136939520000000000000)
    require(B == Fraction("0.000000002") and F == Fraction("9.79415"), "Threshold/factor normalization")
    require(L - F * B == margin > 0, "Strict factor threshold margin")
    require(L > Fraction("0.0000000195883") > B and U > B, "Genuine M12 must fail the terminal bound")
    require(L - F * U < 0, "Genuine M12 must fail the factor comparison against its own old upper")
    expected = {"threshold_exact": B, "tested_whole_upper_exact": U,
                "old_M12_lower_exact": L, "strict_decrease_factor_exact": F,
                "strict_decrease_margin_exact": L - F * U,
                "fixed_threshold_factor_margin_exact": margin}
    for key, value in expected.items():
        require(Fraction(data["scalar"][key]) == value, "Scalar mismatch: " + key)
    require(data["scalar"]["terminal_metric_gate_passed"] is False and
            data["scalar"]["strict_actual_decrease_gate_passed"] is False,
            "Negative scalar test was not rejected")

    files = data["checked_files"]
    require(len(files) == 48 and len({row["file"] for row in files}) == 48, "Changed closed input inventory")
    total_bytes = 0
    for row in files:
        path = Path(row["file"])
        require(path.stat().st_size == row["bytes"] and digest(path) == row["sha256"],
                "Closed replay dependency changed: " + str(path))
        total_bytes += row["bytes"]
    report = {
        "status": "PASS-independent-closed-negative-scalar-and-hash-check",
        "script_sha256": digest(Path(__file__)), "inputs": inputs,
        "independent_negative_byte_identical_to_author": True,
        "closed_replay_dependencies_rehashed": len(files), "dependency_bytes_rehashed": total_bytes,
        "source_imports": sorted(modules),
        "exact_scalar_reconstruction": {key: str(value) for key, value in expected.items()},
        "conditional_lemma": "If 0<=E_new<=U_new<=B and E_old>=L, then E_old>F*E_new; no division by E_new is used.",
        "actual_old_M12_error_strictly_exceeds_B": True,
        "new_candidate_branch_executed": False, "root_flow_solver_calls": 0,
        "new_metric_curvature_or_partition_verification": False,
        "candidate_certificate_issued": False, "README_complete": False,
        "scope": "Pure metadata, source-import AST and exact scalar audit. It does not replace the separate full code review or any continuous input certificate."
    }
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"status": report["status"], "dependencies": len(files), "candidate_certificate_issued": False}))


if __name__ == "__main__":
    main()
