#!/usr/bin/env python3
"""Independent frozen-source and read-only-check closure; no solver imports."""
import argparse
import ast
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / "notes"
AUTHOR = "2026-11-09-db6f-prefix-newton-release-lu"
REVIEW = "2026-11-09-db6f-tail-review-newton-release-lu"


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def read(path):
    return json.loads(Path(path).read_text())


def ident(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verified(row):
    actual = ident(row["path"])
    require(actual == {k: row[k] for k in actual}, "Changed frozen source")
    return actual


def function(tree, name):
    found = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == name]
    require(len(found) == 1, "Missing unique function " + name)
    return found[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(args.out.resolve().parent == NOTES and not args.out.exists(), "Invalid occupied output")
    pub_path = NOTES / (AUTHOR + "-publication.json")
    require(ident(pub_path)["sha256"] == "59e915d98e058adbdaf8682b6c3cfaed8cd07045a5a2d271686974a90ecdd29d",
            "Author publication changed")
    publication = read(pub_path)
    require(publication["file_count"] == len(publication["files"]) == 7, "Wrong publication extent")
    files = [verified(row) for row in publication["files"]]
    require(sum(row["bytes"] for row in files) == publication["total_bytes"] == 52348, "Wrong byte total")
    ledger_path = NOTES / (AUTHOR + "-sources.json")
    sources = [verified(row) for row in read(ledger_path)["files"]]
    require(len(sources) == 13 and len({row["path"] for row in sources}) == 13, "Wrong source extent")

    original_protocol = NOTES / (AUTHOR + "-protocol.json")
    replay = NOTES / (REVIEW + "-protocol-replay.json")
    require(original_protocol.read_bytes() == replay.read_bytes(), "Independent author replay is not byte-identical")
    require(ident(replay)["sha256"] == "1cfe353071f1c823e507285e81e41559d84094f8af2a03aa2afe0d2f6715c40e",
            "Author protocol differs")
    protocol = read(replay)
    require(protocol["status"] == "PURE_LIFETIME_PROTOCOL_PASS" and len(protocol["cases"]) == 10
            and all(row["passed"] is True for row in protocol["cases"]), "Protocol replay did not pass")
    own_protocol = NOTES / (REVIEW + "-lifetime-check.json")
    require(ident(own_protocol)["sha256"] == "53ca99e44b658a0758aa871a787e931fa1ef8ad350b57ff7bcfc304fe95a42a7",
            "Independent lifetime check differs")
    own = read(own_protocol)
    require(own["protocol_case_count"] == 9 and own["real_splu_calls"] == 0
            and own["original_or_derived_Newton_calls"] == 0, "Independent scope changed")
    verified(own["checker"])
    negative_path = NOTES / (REVIEW + "-negative-gate.json")
    require(ident(negative_path)["sha256"] == "303d36428b070382fb5a386b5ba3fe5f2f33af5f6d0ad1534317308029b7db09",
            "Normal negative gate output differs")
    negative = read(negative_path)
    require(negative["status"] == "NOT_SELECTED" and negative["ready"] is False
            and negative["solver_calls"] == negative["install_calls"] == 0
            and negative["runtime_unchanged"] is True
            and negative["reason"] == "Original domain-aware Newton is not installed; refusing selection",
            "Read-only fresh process gate did not reject the uninstalled identity")

    selector_path = HERE / "db6f-prefix-select-domain-newton-release-lu.py"
    selector = ast.parse(selector_path.read_text())
    choose = function(selector, "select_newton")
    assignment = "derived.STATS = original.STATS"
    alias = [i for i, node in enumerate(choose.body)
             if isinstance(node, ast.Assign) and ast.unparse(node) == assignment]
    pointer = [i for i, node in enumerate(choose.body)
               if isinstance(node, ast.Assign) and ast.unparse(node) == "bvp.solve_newton = derived.solve_newton"]
    require(len(alias) == len(pointer) == 1 and alias[0] < pointer[0], "STATS alias is not set before selection")
    first_executable = choose.body[1] if ast.get_docstring(choose) is not None else choose.body[0]
    require(ast.unparse(first_executable) == "info = original_runtime_gate(original, bvp)",
            "Selection does not first require the installed original identity")
    require(not any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                    and node.func.id in ("select_newton", "install", "solve_newton")
                    for node in ast.walk(function(selector, "main"))),
            "Read-only CLI unexpectedly calls a mutation or solver")
    constants = {node.targets[0].id: node.value for node in selector.body
                 if isinstance(node, ast.Assign) and len(node.targets) == 1
                 and isinstance(node.targets[0], ast.Name)}
    scipy_source = next(row for row in sources if row["path"].endswith("/scipy/integrate/_bvp.py"))
    require(ast.literal_eval(constants["BVP_SHA"]) == scipy_source["sha256"], "SciPy source gate differs")
    require(ast.literal_eval(constants["PARAMETERS"]) ==
            ["n", "m", "h", "col_fun", "bc", "jac", "y", "p", "B", "bvp_tol", "bc_tol"],
            "Original function signature gate differs")

    n, k = 43, 14
    counts = []
    # Exact coefficients of m and the constant term independently establish
    # 2(m-1)n^2+(m-1)nk+2n(n+k)+(n+k)k = (2n+k)(nm+k).
    require((2*n*n+n*k, -2*n*n-n*k+2*n*(n+k)+(n+k)*k) ==
            ((2*n+k)*n, (2*n+k)*k), "Global Jacobian count identity failed")
    for m, expected in ((5047, 21703500), (6500, 27951400)):
        count = 2*(m-1)*n*n + (m-1)*n*k + 2*n*(n+k) + (n+k)*k
        require(count == expected == 100*(43*m+14), "Global Jacobian scalar count differs")
        counts.append({"nodes": m, "structural_entries": count, "one_float64_values_array_bytes": 8*count})
    old_wrapper = HERE / "db6f-root-true-m14-resource-limited.py"
    new_wrapper = HERE / "db6f-root-true-m14-resource-limited-4g.py"
    require(old_wrapper.read_bytes().replace(b"CAP=3*1024*1024*1024", b"CAP=4*1024*1024*1024", 1)
            == new_wrapper.read_bytes(), "4GiB resource wrapper differs beyond the cap constant")
    observed_path = NOTES / "2026-11-09-db6f-root-spectral-true-m14q512-01-final-observed.json"
    observed = read(observed_path)
    require(observed["actual_exit_code"] == observed["guard_child_exit_code"] == 2
            and observed["tool_receipt"] == "55ec10", "Closed attempt01 receipt differs")
    require(observed["new_prefix_checkpoint_exists"] is False and observed["new_coefficients_exist"] is False
            and observed["final_seam_exists"] is False, "Closed attempt01 was misclassified")
    closed = read(NOTES / "2026-11-09-db6f-prefix-spectral-true-m14q512-01-reproduction.json")
    require(closed["error_type"] == "FileNotFoundError" and len(closed["spectral_coordinate_calls"]) == 1
            and closed["spectral_coordinate_calls"][0]["error"] == "MemoryError((21703500,), dtype('float64'))",
            "Closed primary/secondary failure distinction differs")
    cgroup_path = Path("/sys/fs/cgroup/memory.max")
    cgroup_snapshot = cgroup_path.read_text().strip()

    report = {
        "status": "PASS_FULL_LU_FUNCTION_BATCH_SOURCE_AND_READONLY_CLOSURE",
        "scope": "Source identities, exact integer counts and detached fake protocol outputs only. select_newton, original install and all real solvers remain uncalled by this review.",
        "checker": ident(__file__), "author_publication": ident(pub_path), "author_files": files,
        "author_sources": sources, "source_count": len(sources),
        "independent_author_protocol_replay": ident(replay), "byte_identical_protocol_replay": True,
        "independent_other_lifetime_protocol": ident(own_protocol), "negative_normal_gate": ident(negative_path),
        "original_STATS_alias_before_pointer_change": True, "separate_new_runtime_identity": True,
        "original_uninstalled_negative_gate_rejects": True, "old_true_M14_gate_must_not_be_reused": True,
        "integer_global_jacobian_counts": counts,
        "known_values_shape_is_not_saved_mesh_or_refresh_index": True,
        "root_closed_attempt01_observation": ident(observed_path),
        "resource_wrapper_difference_only_3_to_4_GiB": True,
        "cgroup_memory_max_observed_this_check": {"path": str(cgroup_path), "value": cgroup_snapshot},
        "actual_newton_calls": 0, "actual_BVP_calls": 0, "actual_DN_RK_root_calls": 0,
        "actual_sparse_LU_calls": 0, "actual_install_calls": 0,
        "active_attempt02_outputs_read": False, "memory_sufficiency_or_candidate_success_claimed": False,
    }
    data = (json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode()
    require(len(data) < 100_000, "Oversize report")
    with args.out.open("xb") as handle:
        handle.write(data)
    print(json.dumps({"status": report["status"], "report": ident(args.out),
                      "sources": len(sources), "author_protocol_replay_identical": True,
                      "newton_calls": 0, "installation_calls": 0}))


if __name__ == "__main__":
    main()
