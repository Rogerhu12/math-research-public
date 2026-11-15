#!/usr/bin/env python3
"""Public Actions driver for the eight fixed original inert Gaussian source transports."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO / "topics/serre-uniformity"
REQUEST = TOPIC / "notes/sigma-inert-Gaussian-source-transport-request.json"
RESULT = "fixed-inert-Gaussian-rayclass-source-transport"
FINAL = "fixed-inert-Gaussian-source-transport.json"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Original inert Gaussian new arithmetic belongs to the public repository Actions.")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save(path, data):
    path = Path(path)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(data, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()


def spec(path):
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def inside(relative):
    p = Path(relative)
    assert not p.is_absolute() and ".." not in p.parts
    return REPO / p


def check_sources(item):
    assert item["result"] == RESULT and item["scope"] == "eight_fixed_source_transports"
    assert item["image"] == "sagemath/sagemath:10.6"
    assert item["sage_version"] == "10.6"
    assert item["budget_minutes"] == 30
    for key in ("core", "wrapper", "proof", "method", "workflow", "upstream_core", "upstream_proof", "harmonic_proof"):
        assert sha(inside(item[key])) == item[key + "_sha256"]
    assert inside(item["wrapper"]).resolve() == Path(__file__).resolve()


def manifest(out):
    artifact = "serre-global-" + RESULT + "-" + os.environ["GITHUB_RUN_ID"] + "-" + os.environ["GITHUB_RUN_ATTEMPT"]
    rows = [dict(spec(p), included_in_git=False, artifact=artifact)
            for p in sorted(out.iterdir()) if p.is_file() and p.name not in (MANIFEST, REFERENCE)]
    save(out / MANIFEST, {"result": RESULT, "files": rows, "artifact": artifact,
        "retention_days": 1, "automatic_git_or_release_publication": False})
    save(out / REFERENCE, {"result": RESULT, "manifest": spec(out / MANIFEST),
        "artifact": artifact, "file_count": len(rows), "raw_output_in_git_or_release": False})


def parse_log(text, item):
    matches = re.findall(r"^EXECUTION_METADATA=(.*)$", text, re.M)
    assert len(matches) == 1
    meta = json.loads(matches[0])
    for key, env in (("run_id", "GITHUB_RUN_ID"), ("run_attempt", "GITHUB_RUN_ATTEMPT"),
                     ("source_commit", "GITHUB_SHA"), ("repository", "GITHUB_REPOSITORY")):
        assert str(meta[key]) == os.environ[env]
    assert meta["github_actions"] == "true" and meta["source_sha256"] == item["core_sha256"]
    assert re.findall(r"^SAGE_VERSION=(.*)$", text, re.M) == [item["sage_version"]]
    start = re.search(r"^\{", text, re.M)
    assert start is not None
    result, used = json.JSONDecoder().raw_decode(text[start.start():])
    assert result["result"] == RESULT and result["source_sha256"] == item["core_sha256"]
    assert result["R812_upstream_source_sha256"] == item["upstream_core_sha256"]
    digest = hashlib.sha256(canonical(result)).hexdigest()
    assert re.findall(r"^RESULT_SHA256=([0-9a-f]{64})$", text, re.M) == [digest]
    assert result["all_fixed_character_and_parity_checks_passed"] is True
    names = ["S", "F", "H", "R", "J", "G"]
    assert result["original_basis"] == names
    labels = [{"form": f, "level": level, "oldform_exponent": d}
              for f, level, d in [("F3",36,1),("F3",36,2),("F3",36,4),
                                  ("F7",36,1),("F7",36,2),("F7",36,4),
                                  ("G1",144,1),("G5",144,1)]]
    def coordinates(row):
        assert len(row) == 24
        assert all(isinstance(q, str) and re.fullmatch(r"-?\d+(?:/[1-9]\d*)?", q) for q in row)
    def certificate(cert):
        assert isinstance(cert["zero"], bool)
        assert int(cert["power_basis_denominator"]) > 0
        assert cert["zero"] == (int(cert["integral_norm"]) == 0)
        assert (cert["integral_norm_factors"] is None) == cert["zero"]
        coordinates(cert["power_basis_coordinates"])
    channels = result["source_channels"]
    assert len(channels) == 8
    for row, label in zip(channels, labels):
        assert all(row[k] == value for k, value in label.items())
        assert row["primitive_convention"] == "J_nu(t)=J_form(t^d)/d; theta_t J_nu=f_nu"
        certificate(row["FG"])
        certificate(row["HJ"])
    for key in ("source_basis_det", "transport_matrix_det"):
        certificate(result[key])
        assert result[key]["zero"] is False
    assert 0 <= result["normalization_pivot"] < 6
    matrix_specs = [
        ("Uhat_matrix", names, [{"theta_characteristic_r": r, "section": "Psi"} for r in range(6)]),
        ("source_basis_matrix", [{"theta_first_r": r, "theta_second_s": s}
                                  for r in range(4) for s in (1,2)], labels),
        ("transport_matrix", [{"original_even": names[a], "original_odd": names[b]}
                               for a in range(4) for b in (4,5)], labels),
    ]
    for key, rows, columns in matrix_specs:
        obj = result[key]
        assert obj["row_labels"] == rows and obj["column_labels"] == columns
        entries = obj["entries_in_power_basis"]
        assert len(entries) == len(rows)
        for row in entries:
            assert len(row) == len(columns)
            for entry in row:
                coordinates(entry)
    return meta, result, digest


def compute(item, out):
    guard()
    out.mkdir(parents=True, exist_ok=True)
    check_sources(item)
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    assert source == os.environ["GITHUB_SHA"]
    save(out / "public-actions-input.json", {"result": RESULT, "source_commit": source,
        "source_repository": os.environ["GITHUB_REPOSITORY"], "job": item,
        "request_sha256": sha(REQUEST), "root_readme_sha256": sha(REPO / "README.md"),
        "topic_readme_sha256": sha(TOPIC / "README.md"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "fixed_eight_source_transport_only": True, "prime_scan_or_high_sigma_jet": False,
        "previous_six_Frobenius_cases_recomputed": False,
        "necessary_R812_basis_restored_because_prior_full_U_was_not_serialized": True})
    started = time.monotonic()
    log = out / "public-actions-run.log"
    name = "serre-inert-Gaussian-source-" + os.environ["GITHUB_RUN_ID"] + "-" + os.environ["GITHUB_RUN_ATTEMPT"]
    error, code, parsed = None, 1, None
    try:
        subprocess.run(["docker", "pull", item["image"]], check=True)
        info = json.loads(subprocess.check_output(["docker", "image", "inspect", item["image"]], text=True))[0]
        digests = [d for d in info["RepoDigests"] if d.startswith("sagemath/sagemath@sha256:")]
        assert len(digests) == 1 and info["Os"] == "linux" and info["Architecture"] == "amd64"
        fixed_image = digests[0]
        save(out / "runtime-image-receipt.json", {"requested_image": item["image"],
            "executed_image": fixed_image, "image_id": info["Id"],
            "architecture": info["Architecture"], "os": info["Os"],
            "image_created": info["Created"], "sage_version_required": item["sage_version"],
            "official_versioned_image": True})
        command = ["docker", "run", "--rm", "--name", name, "--network=none",
            "--mount", "type=bind,src=" + str(REPO) + ",dst=/workspace/serre-source,readonly",
            "--workdir", "/workspace/serre-source", "--env", "PYTHONDONTWRITEBYTECODE=1",
            "--env", "PYTHONUNBUFFERED=1"]
        for key in ("GITHUB_ACTIONS", "GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT",
                    "GITHUB_SHA", "GITHUB_REF", "GITHUB_WORKFLOW", "GITHUB_EVENT_NAME"):
            command.extend(["--env", key + "=" + os.environ[key]])
        command.extend(["--entrypoint", "/usr/bin/sage", fixed_image, "-python",
                        "/workspace/serre-source/" + item["core"]])
        with log.open("w", encoding="utf-8") as stream:
            proc = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT,
                                  timeout=item["budget_minutes"] * 60)
            code = proc.returncode
        text = log.read_text(encoding="utf-8")
        print(text, flush=True)
        assert code == 0, "Mathematical core did not complete"
        meta, result, digest = parse_log(text, item)
        save(out / FINAL, result)
        parsed = result
        save(out / "core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": item["core_sha256"], "proof_sha256": item["proof_sha256"],
            "metadata": meta, "canonical_result_sha256": digest,
            "result_file": spec(out / FINAL), "all_fixed_character_and_parity_checks_passed": True,
            "complete_exact_Uhat_and_two_eight_by_eight_matrices_saved": True,
            "source_channel_count": len(result["source_channels"]),
            "elapsed_seconds": time.monotonic() - started})
    except Exception as exc:
        error = type(exc).__name__ + ": " + str(exc)
        if isinstance(exc, subprocess.TimeoutExpired):
            subprocess.run(["docker", "rm", "-f", name], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            code = 124
        elif code == 0:
            code = 1
        if log.exists():
            print(log.read_text(encoding="utf-8"), flush=True)
    complete = code == 0 and parsed is not None
    save(out / "run-receipt.json", {"result": RESULT, "complete": complete,
        "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"], "process_exit_code": code,
        "error": error, "execution_environment": "public-repository-github-actions",
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "elapsed_seconds": time.monotonic() - started,
        "eight_fixed_transports_computed": complete,
        "all_FG_or_HJ_entries_nonzero_required_for_success": False,
        "unknown_scaled_CM_values_or_their_combination_computed": False,
        "primitive_Legendre_same_h_or_main_uniformity_claimed": False})
    manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    guard()
    check_sources(item)
    initial, run, core = (read(out / n) for n in ("public-actions-input.json", "run-receipt.json", "core-receipt.json"))
    assert initial["job"] == item and initial["source_commit"] == run["source_commit"] == os.environ["GITHUB_SHA"]
    assert run["complete"] is True and run["process_exit_code"] == 0 and core["complete"] is True
    assert core["source_sha256"] == item["core_sha256"] and core["proof_sha256"] == item["proof_sha256"]
    assert run["unknown_scaled_CM_values_or_their_combination_computed"] is False
    meta, result, digest = parse_log((out / "public-actions-run.log").read_text(encoding="utf-8"), item)
    assert result == read(out / FINAL) and core["metadata"] == meta
    assert core["canonical_result_sha256"] == digest and core["result_file"] == spec(out / FINAL)
    reference = read(out / REFERENCE)
    assert reference["manifest"] == spec(out / MANIFEST)
    inventory = read(out / MANIFEST)
    assert inventory["result"] == RESULT and reference["file_count"] == len(inventory["files"])
    names = set()
    for row in inventory["files"]:
        name = row["file"]
        assert Path(name).name == name and name not in names
        names.add(name)
        assert row["bytes"] == (out / name).stat().st_size and row["sha256"] == sha(out / name)
        assert row["included_in_git"] is False
    assert names == {p.name for p in out.iterdir() if p.is_file() and p.name not in (MANIFEST, REFERENCE)}
    print(json.dumps({"result": RESULT, "complete": True,
        "source_channel_count": len(result["source_channels"]),
        "zero_FG_channels": [i for i,c in enumerate(result["source_channels"]) if c["FG"]["zero"]],
        "zero_HJ_channels": [i for i,c in enumerate(result["source_channels"]) if c["HJ"]["zero"]],
        "complete_exact_matrices_saved": True,
        "canonical_result_sha256": digest,
        "unknown_CM_value_nonzero_same_h_or_main_uniformity_claimed": False}), flush=True)
    return 0


def main():
    guard()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["compute", "verify"])
    args = parser.parse_args()
    request = read(REQUEST)
    assert request["session"] == "serre-public-astra-20261115"
    out = Path(os.environ["RUNNER_TEMP"]) / "serre-global" / RESULT / "output"
    return compute(request["job"], out) if args.mode == "compute" else verify(request["job"], out)


if __name__ == "__main__":
    sys.exit(main())

