#!/usr/bin/env python3
"""Publish only small public-topic JSON diagnostics using ordinary Git.

The token is read only from GITHUB_TOKEN, passed to a transient credential
helper through the child environment, and never written to disk. README
changes after any pull stop publication and leave the results as artifacts.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

TOPIC = "topics/visible-flex-new-mechanism"
REPOSITORY = "Rogerhu12/math-research-public"
READMES = ["README.md", f"{TOPIC}/README.md"]
SOURCE_FILES = READMES + [
    ".github/workflows/visible-new-mechanism-search.yml",
    ".github/workflows/visible-new-mechanism-continuation.yml",
    f"{TOPIC}/computations/request-continuation.json",
    f"{TOPIC}/scripts/eccentric_collar_search.py",
    f"{TOPIC}/scripts/literature_band_seed.py",
    f"{TOPIC}/scripts/literature_band_kernel.py",
    f"{TOPIC}/scripts/mixed_mode_gc_flow.py",
    f"{TOPIC}/scripts/publish_actions.py",
    f"{TOPIC}/notes/eccentric-search-design-002-curvature-seed.json",
]
MAX_FILE = 5_000_000
COMPRESS_AT = 1_000_000


class PublicationStopped(RuntimeError):
    pass


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n")


def git_environment(token: str) -> dict:
    env = os.environ.copy()
    # Disable inherited diagnostic traces before handling credentials.
    for key in list(env):
        if key.startswith("GIT_TRACE") or key.startswith("GIT_CONFIG_"):
            env.pop(key)
    env.pop("GIT_CURL_VERBOSE", None)
    env.update({
        "GIT_TERMINAL_PROMPT": "0",
        "GITHUB_TOKEN": token, "GIT_CONFIG_COUNT": "2",
        "GIT_CONFIG_KEY_0": "credential.helper", "GIT_CONFIG_VALUE_0": "",
        "GIT_CONFIG_KEY_1": "credential.helper",
        "GIT_CONFIG_VALUE_1": "!f() { printf '%s\\n' 'username=x-access-token' \"password=$GITHUB_TOKEN\"; }; f",
    })
    return env


def git(repo: Path, env: dict, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    result = subprocess.run(["git", *args], cwd=repo, env=env,
                            capture_output=True, text=True)
    if check and result.returncode:
        token = env.get("GITHUB_TOKEN", "")
        message = result.stderr.strip()
        if token:
            message = message.replace(token, "[redacted]")
        raise PublicationStopped(f"git {args[0]} failed: {message[:1200]}")
    return result


def committed_bytes(repo: Path, env: dict, commit: str, path: str) -> bytes:
    size = int(git(repo, env, "cat-file", "-s", f"{commit}:{path}").stdout)
    if size >= MAX_FILE:
        raise PublicationStopped(f"source exceeds the repository file limit: {path}")
    if path.endswith(".md") and size >= 100_000:
        raise PublicationStopped(f"source Markdown requires a bounded read: {path}")
    result = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=repo,
                            env=env, capture_output=True, check=True)
    return result.stdout


def collect_outputs(results: Path) -> tuple[dict[str, bytes], list[dict]]:
    payload, manifest = {}, []
    for path in sorted(results.rglob("*")):
        if path.is_symlink():
            raise PublicationStopped("result symlinks are not publishable")
        if not path.is_file() or path.name.startswith("publication-"):
            continue
        relative = path.relative_to(results)
        precompressed = path.name.endswith(".json.gz")
        if path.suffix != ".json" and not precompressed:
            # Logs, binary states, meshes and incidental files remain artifacts.
            continue
        # The repository limit applies to the stored file, after required gzip.
        # Bound raw JSON in memory separately; never send this data through an API tool.
        source_size = path.stat().st_size
        if precompressed and source_size >= MAX_FILE:
            raise PublicationStopped(f"compressed diagnostic is too large: {relative}")
        if not precompressed and source_size > 64_000_000:
            raise PublicationStopped(f"raw diagnostic exceeds the decoded JSON bound: {relative}")
        stored = path.read_bytes()
        if precompressed:
            # Preserve an explicitly hashed complete symbolic DAG already packed
            # by its producer, while validating its bounded decoded JSON.
            with gzip.GzipFile(fileobj=io.BytesIO(stored)) as stream:
                raw = stream.read(64_000_001)
            if len(raw) > 64_000_000:
                raise PublicationStopped(f"decoded diagnostic is too large: {relative}")
        else:
            raw = stored
        def reject_nonfinite(value):
            raise ValueError(f"nonfinite JSON constant in {relative}: {value}")
        json.loads(raw, parse_constant=reject_nonfinite)
        target = relative.as_posix()
        packed = stored if precompressed else raw
        if not precompressed and len(raw) > COMPRESS_AT:
            target += ".gz"
            packed = gzip.compress(raw, compresslevel=9, mtime=0)
        if len(packed) >= MAX_FILE:
            raise PublicationStopped(f"compressed diagnostic is too large: {relative}")
        if target in payload:
            raise PublicationStopped(f"duplicate output path: {target}")
        payload[target] = packed
        manifest.append({"path": target, "bytes": len(packed),
                         "sha256": sha256(packed), "raw_bytes": len(raw),
                         "raw_sha256": sha256(raw)})
    if not payload:
        raise PublicationStopped("no completed small JSON diagnostics to publish")
    return payload, manifest


def check_readme_delta(repo: Path, env: dict, before: str, after: str,
                       results: Path) -> None:
    changed = git(repo, env, "diff", "--name-only", before, after, "--", *READMES).stdout.strip()
    if not changed:
        return
    delta = git(repo, env, "diff", "--no-ext-diff", "--unified=3", before, after, "--", *READMES).stdout
    (results / "publication-README-change.diff").write_text(delta)
    raise PublicationStopped("README changed after pull; publication stopped. "
                             "Read the saved diff and apply the new rules before rerunning. "
                             f"Changed: {', '.join(changed.splitlines())}")


def pull_and_check(repo: Path, env: dict, results: Path) -> dict:
    before = git(repo, env, "rev-parse", "HEAD").stdout.strip()
    git(repo, env, "pull", "--rebase", "--no-autostash", "origin", "main")
    after = git(repo, env, "rev-parse", "HEAD").stdout.strip()
    check_readme_delta(repo, env, before, after, results)
    remote = git(repo, env, "rev-parse", "origin/main").stdout.strip()
    return {"before": before, "after": after, "remote_main": remote,
            "readmes_unchanged": True}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", required=True, type=Path)
    parser.add_argument("--lane", required=True,
                        choices=["eccentric", "seeds", "kernel", "core_folded", "second_order", "folded_bearing", "band_geometry", "band_newton", "inward", "codedesign", "inward_fixed", "ellipse_cont", "ellipse_phi", "inward_gc4", "star_core", "closed_design", "ruled_tail", "space_star", "closed_quartic", "star_lift", "space_refine", "warped_core", "warped_tube", "phase_shoot", "derivative_audit", "star_verify", "closed_branch", "global_profile", "warped_collar", "exact_D0", "cosine_core", "phase_D0", "physical_C", "cosine_endpoints", "cosine_feasible", "physical_root", "constant_h_exact", "ellipse_frame", "ellipse_audit", "ellipse_enriched", "zero_operator_exact", "ellipse_bent_tail", "zero_operator_instance", "third_order_exact", "fourth_order_exact", "fourth_sos_exact", "ellipse_saturated_heat", "overlap_fourth_exact", "range_numerator_exact", "full_range_compile", "natural_body_initial", "single_P_instance", "independent_height_solve", "full_fourth_evaluate", "fixed_height_primitive", "frozen_profile_gate", "entry_paired_audit", "recovery_development", "short_entry_development", "short_entry_audit", "p1_bulk_development", "p1_bulk_exact", "height_gate_development", "height_polytope_development", "height_polytope_audit", "higher_range_development", "p1_word_exact", "local_third_exact", "entry_single_q_development", "height_quartic_development", "linear_third_exact", "quartic_joint_development", "quartic_joint_audit", "closed_c1_endpoint", "full_phase_bridge_exact", "core_transport_development", "core_transport_initial_development", "core_transport_initial_audit", "full_phase_rational_dual", "pure_tail_period", "joint_resume", "localized_core_initial", "pure_tail_subleading", "multiple_pair_P1", "metric_epigraph", "pure_tail_next_reduce", "localized_leading_initial", "total_P1_blocks", "metric_epigraph_saved_trial", "pure_tail_action_compress", "pure_tail_c8_reduce", "fourth_character_transverse", "metric_epigraph_dense", "metric_epigraph_exchange", "pure_tail_c7_reduce", "c7_transverse_tail_probe", "curvature_epigraph_exchange", "local_fourth_quotient", "full_m8_tail_response_projection", "curvature_output_recovery", "constrained_static_fourth", "curvature_trial_diagnostics", "static_g_rational_dual", "static_m8_tail_quotient", "curvature_feasible_exchange", "constrained_static_m8_tail_quotient", "g_first_translation", "local_fourth_derivative_factors", "curvature_feasible_trial_diagnostics", "g_second_translation"])
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    repo, results = args.repo.resolve(), args.results.resolve()
    results.mkdir(parents=True, exist_ok=True)
    token = os.environ.get("GITHUB_TOKEN", "")
    env = git_environment(token)
    status = {"status": "not_published", "lane": args.lane,
              "at_utc": datetime.now(timezone.utc).isoformat()}
    try:
        if repo == results or repo in results.parents:
            raise PublicationStopped("results must remain outside the checkout until packaged")
        payload, manifest = collect_outputs(results)
        source = os.environ.get("GITHUB_SHA") or git(repo, env, "rev-parse", "HEAD").stdout.strip()
        if not re.fullmatch(r"[0-9a-f]{40}", source):
            raise PublicationStopped("invalid source commit")
        if not args.dry_run:
            if os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
                raise PublicationStopped("publisher is restricted to this public repository")
            if os.environ.get("GITHUB_REF") != "refs/heads/main":
                raise PublicationStopped("publication is restricted to main; keep other runs as artifacts")
            if not token:
                raise PublicationStopped("GITHUB_TOKEN is unavailable; artifacts are retained")
            origin = git(repo, env, "remote", "get-url", "origin").stdout.strip()
            if origin not in [f"https://github.com/{REPOSITORY}", f"https://github.com/{REPOSITORY}.git"]:
                raise PublicationStopped("unexpected origin; refusing to change its address")
        run_id = os.environ.get("GITHUB_RUN_ID", "dry-run")
        attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "1")
        if not args.dry_run and (not run_id.isdecimal() or not attempt.isdecimal()):
            raise PublicationStopped("run identifiers must be numeric")
        relative_dest = f"{TOPIC}/notes/actions-{run_id}-{attempt}-{args.lane}"
        receipt = {"schema": "visible-new-mechanism-actions-v1", "repository": REPOSITORY,
                   "source_commit": source, "run_id": run_id, "run_attempt": attempt,
                   "lane": args.lane, "destination": relative_dest,
                   "design_is_not_fixed_metric_refinement": args.lane in {"eccentric", "core_folded", "folded_bearing", "band_geometry", "inward", "codedesign", "ellipse_cont", "ellipse_phi", "star_core", "closed_design", "space_star", "closed_quartic", "star_lift", "warped_core", "phase_shoot", "closed_branch", "global_profile", "warped_collar", "cosine_core", "cosine_endpoints", "cosine_feasible", "physical_root", "ellipse_bent_tail", "zero_operator_instance", "ellipse_saturated_heat", "natural_body_initial", "single_P_instance", "independent_height_solve", "full_fourth_evaluate", "entry_paired_audit", "short_entry_audit", "height_polytope_audit", "quartic_joint_audit", "core_transport_initial_audit", "joint_resume", "localized_core_initial", "metric_epigraph", "localized_leading_initial", "metric_epigraph_dense", "metric_epigraph_exchange", "curvature_epigraph_exchange", "curvature_feasible_exchange"},
                   "diagnostic_without_new_surface_or_profile_design": args.lane in {"fixed_height_primitive", "frozen_profile_gate", "recovery_development", "short_entry_development", "p1_bulk_development", "p1_bulk_exact", "height_gate_development", "height_polytope_development", "higher_range_development", "p1_word_exact", "entry_single_q_development", "height_quartic_development", "linear_third_exact", "quartic_joint_development", "closed_c1_endpoint", "full_phase_bridge_exact", "core_transport_development", "core_transport_initial_development", "metric_epigraph_saved_trial", "curvature_output_recovery", "curvature_trial_diagnostics", "curvature_feasible_trial_diagnostics"},
                   "artificial_development_only": args.lane in {"recovery_development", "short_entry_development", "p1_bulk_development", "height_gate_development", "height_polytope_development", "higher_range_development", "entry_single_q_development", "height_quartic_development", "quartic_joint_development", "core_transport_development", "core_transport_initial_development"},
                   "complete_research_compilation_without_candidate_geometry": args.lane in {"p1_bulk_exact", "p1_word_exact", "local_third_exact", "linear_third_exact", "closed_c1_endpoint", "full_phase_bridge_exact", "full_phase_rational_dual", "pure_tail_period", "pure_tail_subleading", "multiple_pair_P1", "pure_tail_next_reduce", "total_P1_blocks", "pure_tail_action_compress", "pure_tail_c8_reduce", "fourth_character_transverse", "pure_tail_c7_reduce", "c7_transverse_tail_probe", "local_fourth_quotient", "full_m8_tail_response_projection", "constrained_static_fourth", "static_g_rational_dual", "static_m8_tail_quotient", "constrained_static_m8_tail_quotient", "g_first_translation", "local_fourth_derivative_factors", "g_second_translation"},
                   "exact_profile_witness_without_candidate_geometry": args.lane in {"local_third_exact", "full_phase_rational_dual", "multiple_pair_P1", "fourth_character_transverse"},
                   "task_complete": False, "source_files": {}, "outputs": manifest,
                   "pulls": [], "readmes_read_commit": source}
        script_root = f"{TOPIC}/scripts"
        script_sources = ([p.relative_to(repo).as_posix() for p in (repo / script_root).glob("*.py")]
                          if args.dry_run else
                          git(repo, env, "ls-tree", "-r", "--name-only", source, "--", script_root).stdout.splitlines())
        for path in sorted(set(SOURCE_FILES + script_sources)):
            content = (repo / path).read_bytes() if args.dry_run else committed_bytes(repo, env, source, path)
            receipt["source_files"][path] = {"sha256": sha256(content), "bytes": len(content)}
        request_path = f"{TOPIC}/computations/request.json"
        if (repo / request_path).is_file():
            content = (repo / request_path).read_bytes()
            receipt["source_files"][request_path] = {"sha256": sha256(content), "bytes": len(content)}
        if args.dry_run:
            receipt["dry_run_working_tree_sources"] = True
            write_json(results / "publication-receipt.json", receipt)
            status.update(status="dry_run_only", output_count=len(payload))
            print("Dry run: packaged diagnostics and source hashes; no Git mutation or publication.")
            return 0
        if git(repo, env, "status", "--porcelain", "--untracked-files=no").stdout.strip():
            raise PublicationStopped("tracked checkout changes exist before publication")
        if git(repo, env, "rev-parse", "HEAD").stdout.strip() != source:
            raise PublicationStopped("checkout HEAD is not the computation source commit")
        receipt["pulls"].append(pull_and_check(repo, env, results))
        receipt["readmes_read_commit"] = receipt["pulls"][-1]["remote_main"]
        destination = repo / relative_dest
        if destination.exists():
            raise PublicationStopped("unique run output directory already exists; refusing overwrite")
        destination.mkdir(parents=True)
        for path, content in payload.items():
            target = destination / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        def save_receipt():
            write_json(results / "publication-receipt.json", receipt)
            destination.mkdir(parents=True, exist_ok=True)
            write_json(destination / "receipt.json", receipt)
        save_receipt()
        git(repo, env, "config", "user.name", "github-actions[bot]")
        git(repo, env, "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
        git(repo, env, "add", "--sparse", "--", relative_dest)
        staged = git(repo, env, "diff", "--cached", "--name-only").stdout.splitlines()
        if not staged or any(not path.startswith(relative_dest + "/") for path in staged):
            raise PublicationStopped("staging contains files outside the unique output directory")
        git(repo, env, "commit", "-m", f"visible-new-mechanism: record {args.lane} Actions {run_id}/{attempt}")
        while True:
            pushed = git(repo, env, "push", "origin", "HEAD:main", check=False)
            if pushed.returncode == 0:
                status.update(status="published", destination=relative_dest,
                              commit=git(repo, env, "rev-parse", "HEAD").stdout.strip(),
                              source_commit=source, output_count=len(payload))
                print(f"Published {len(payload)} small JSON diagnostics to {relative_dest}.")
                return 0
            reason = (pushed.stdout + pushed.stderr).lower()
            advanced = any(marker in reason for marker in ["non-fast-forward", "fetch first", "remote contains work"])
            advanced = advanced or ("cannot lock ref" in reason and "but expected" in reason)
            if not advanced:
                raise PublicationStopped("push failed for a reason other than non-fast-forward; artifacts retained")
            print("Remote advanced; immediately pulling with rebase and checking both READMEs before retry.")
            receipt["pulls"].append(pull_and_check(repo, env, results))
            receipt["readmes_read_commit"] = receipt["pulls"][-1]["remote_main"]
            save_receipt()
            git(repo, env, "add", "--sparse", "--", f"{relative_dest}/receipt.json")
            git(repo, env, "commit", "--amend", "--no-edit")
    except (PublicationStopped, OSError, ValueError, subprocess.SubprocessError) as exc:
        message = str(exc)
        if token:
            message = message.replace(token, "[redacted]")
        status.update(status="stopped_without_publication", reason=message)
        print(f"Publication stopped: {message}", file=sys.stderr)
        return 1
    finally:
        write_json(results / "publication-status.json", status)


if __name__ == "__main__":
    raise SystemExit(main())
