#!/usr/bin/env python3
"""Read-only source/metadata checks for the frozen next-mode interface v2.

No solver module is imported.  No future checkpoint/configuration or mock
response is constructed.  This checks source identity and static dimensions,
not the success or acceptance of a future M15/M16 computation.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import shlex

TOPIC = Path(__file__).resolve().parents[1]
REPO = TOPIC.parents[1]
P = "notes/2026-11-09-db6f-prefix-m15-to-next-mode-interface"
PINS = {
    P + ".md": "9d9074821c88cfefab9b4762fddb0168efe0d058c120ce99fdcfffc459d3aa42",
    P + "-sources.json": "dc7cda84e6d70706d62cb1f5c23e4dce5e1ec57d001c3fc15243203f479d2d67",
    P + "-v2.md": "8e14cd3142f7e09f4721e568299d76be0c5febf2fccd65edce18f470f659c769",
    P + "-v2-sources.json": "040c85e07ba4163fa811fa938fdd1660cc91fac04ee7eac92e1cdb9c4c38c9a5",
}


def require(value, message):
    if not value:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def binding(path):
    return {"path": str(path.relative_to(REPO)), "sha256": sha(path), "bytes": path.stat().st_size}


def command(text, first):
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if line.strip().startswith(first))
    out = []
    for line in lines[start:]:
        if not line.startswith("    "):
            break
        continuation = line.rstrip().endswith("\\")
        out.append(line.strip().removesuffix("\\"))
        if not continuation:
            break
    return shlex.split(" ".join(out))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    out = args.out.resolve()
    require(out.is_relative_to(TOPIC) and not out.exists(), "New own-topic output required")
    method_bindings = []
    for rel, expected in PINS.items():
        path = TOPIC / rel
        require(sha(path) == expected, "Frozen method/ledger changed: " + rel)
        method_bindings.append(binding(path))
    old = json.loads((TOPIC / (P + "-sources.json")).read_text())
    new = json.loads((TOPIC / (P + "-v2-sources.json")).read_text())
    require(len(old["source_bindings"]) == 19 and len(new["source_bindings"]) == 29, "Source counts")
    current = {row["path"]: row for row in new["source_bindings"]}
    require(len(current) == 29, "Repeated source identity")
    for row in old["source_bindings"]:
        require(current[row["path"]] == row, "Changed original source binding")
    checked = []
    for row in new["source_bindings"]:
        path = (REPO / row["path"]).resolve()
        require(path.is_relative_to(TOPIC), "Binding leaves topic")
        got = binding(path)
        require(got == row, "Source bytes/hash changed: " + row["path"])
        checked.append(got)
    for row in new["frozen_v1_bindings"]:
        require(binding((REPO / row["path"]).resolve()) == row, "Changed frozen v1")
    require(binding(TOPIC / (P + "-v2.md")) == new["v2_note"], "v2 note identity")

    cache = TOPIC / "repro/source-root/topics/large-amplitude-twist-flex/scripts"
    dependencies = json.loads((TOPIC / "notes/closing_tail_dependency_blobs.json").read_text())
    require(len(dependencies) == 9, "Closing loader dependency count")
    blob_checks = []
    for name, expected in dependencies.items():
        data = (cache / name).read_bytes()
        actual = hashlib.sha1(("blob " + str(len(data)) + "\0").encode() + data).hexdigest()
        require(actual == expected, "Frozen cache Git-blob mismatch: " + name)
        blob_checks.append({"name": name, "git_blob_sha1": actual})
    require({row["name"]: row["git_blob_sha1"] for row in new["cache_blob_checks"]} == dependencies,
            "Author cache ledger disagrees")

    old_text = (TOPIC / (P + ".md")).read_text()
    text = (TOPIC / (P + "-v2.md")).read_text()
    coupled = command(text, "python scripts/db6f-prefix-flat-coupled.py")
    require(coupled == command(old_text, "python scripts/db6f-prefix-flat-coupled.py"), "Main coupled argv changed")
    affine = command(text, "python scripts/db6f-prefix-affine-lift.py")
    require(affine == command(old_text, "python scripts/db6f-prefix-affine-lift.py"), "Auxiliary affine argv changed")
    raw = command(text, "VISIBLE_FLEX_SOURCE_ROOT=")
    old_raw = command(old_text, "VISIBLE_FLEX_SOURCE_ROOT=")
    cache_args = [arg for arg in raw if arg.startswith("CLOSING_TAIL_CACHE=")]
    require(len(cache_args) == 1 and cache_args[0].split("=", 1)[1] == str(cache), "Explicit verified raw-lift cache")
    require([arg for arg in raw if not arg.startswith("CLOSING_TAIL_CACHE=")] == old_raw, "Other raw-lift command changed")
    parser_tree = ast.parse((TOPIC / "scripts/db6f-prefix-coupled.py").read_text())
    allowed = set()
    for node in ast.walk(parser_tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "add_argument":
            allowed.update(arg.value for arg in node.args if isinstance(arg, ast.Constant) and isinstance(arg.value, str))
    require(all(arg in allowed for arg in coupled if arg.startswith("--")), "Unknown coupled argument")
    wi = coupled.index("--warmup-scales")
    require(coupled[wi + 1] == "--lagged-tail", "The original warmup list must be empty")
    expected_values = {"--source-root": "repro/source-root", "--amplitude": ".1", "--warp-reference": ".1",
                       "--modes": "16", "--angular": "512", "--audit-angular": "1024", "--nodes": "1601",
                       "--max-nodes": "4500", "--tol": "2e-9", "--bc-tol": "1e-8",
                       "--physical-bc-tol": "2e-11", "--node-heap": "1536"}
    for key, value in expected_values.items():
        require(coupled[coupled.index(key) + 1] == value, "Changed numerical/physical argument: " + key)
    require("--fixed" in coupled and "--preserve-restart-mesh" in coupled, "Fixed-metric saved-mesh flags")

    port = json.loads((TOPIC / "notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json").read_text())
    require(len(port["linearSlope"]) == 96 and port["linearSlope"][15] == 205.94394394816572, "Physical linear d16")
    M, depth, parts, profiles = 16, 12, 8, 9
    expected = {"prefix_slots": 3 * M + 1, "tail_shape": [depth * profiles * parts + 1, 2 * M],
                "raw_shape": [depth + 1, 2 * M], "height_jet_jacobian_entries": (3 * M + 2) * M}
    require(new["derived_expected_M16_schema"] == expected, "Derived static dimensions")
    require(512 > 4 * M * 3, "Original momentum-engine angular condition")
    # Source facts are read, not executed.  Their interpretation is in the audit.
    source_facts = {
        "scripts/950f-tail-warm-remesh.mjs": ["to[M+j]=v[oldM+j]", "Math.abs(z-nearest)<1e-12"],
        "scripts/db6f-prefix-tail-shared-client.py": ["CLOSING_TAIL_CACHE=str(source_root/", "and not audit"],
        "scripts/db6f-prefix-tail-shared-worker.mjs": ["cfg.correctInitialBoundary!==false", "v/r4-initial[0][j]"],
        "scripts/db6f-prefix-tail-shared-core.mjs": ["new Float64Array((3*M+2)*M)", "columns:'physical cut height Fourier coefficients'"],
        "scripts/db6f-prefix-tail-raw-lift.mjs": ["factor=i===0?cell.portRatio:1", "UNSOLVED warm guess"],
        "scripts/db6f-prefix-affine-lift.py": ["actual_nonlinear_tail=False", "if audit:raise RuntimeError"],
    }
    for rel, snippets in source_facts.items():
        value = (TOPIC / rel).read_text()
        require(all(snippet in value for snippet in snippets), "Static source clause changed: " + rel)
    supplementary = ["scripts/closing_weighted_tail.mjs", "scripts/closing_recalibrated_tail.mjs",
                     "scripts/db6f-prefix-flat-profile.py", "scripts/950f-prefix-adaptive-chart-bvp-v2.py",
                     "scripts/950f-prefix-warped-bvp.py", "notes/fixed_metric_mode3_bvp.py",
                     "notes/fixed_metric_mode3_flow.py",
                     "repro/source-root/topics/large-amplitude-twist-flex/scripts/curve_stable_prefix_bvp.py"]
    result = {"status": "PASS-static-next-mode-interface-v2-after-explicit-cache-fix",
              "script_sha256": sha(Path(__file__).resolve()), "method_bindings": method_bindings,
              "all_source_bindings": checked, "supplementary_read_source_bindings": [binding(TOPIC / p) for p in supplementary],
              "cache_blob_checks": blob_checks, "original_19_sources_unchanged": True,
              "ordinary_coupled_and_affine_commands_unchanged": True, "raw_lift_only_command_addition_is_cache": True,
              "all_coupled_flags_exist_in_original_parser": True, "empty_original_warmup_list": True,
              "static_expected_M16_schema_not_a_candidate": expected,
              "physical_linear_d16": port["linearSlope"][15], "linear_port_length": len(port["linearSlope"]),
              "momentum_quadrature_guard": {"N": 512, "required_strict_lower": 4 * M * 3},
              "future_baseline_or_response_read": False, "future_fixture_or_config_created": False,
              "solver_modules_imported": False, "solver_root_flow_or_export_calls": 0,
              "success_or_error_certificate_for_future_M16": False, "README_complete": False}
    with out.open("x") as handle:
        handle.write(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps({"status": result["status"], "sha256": sha(out), "source_bindings_checked": len(checked),
                      "cache_blobs_checked": len(blob_checks), "solver_calls": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
