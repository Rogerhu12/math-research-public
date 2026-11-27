#!/usr/bin/env python3
"""Host provenance for the unchanged original shadow with faithful complete native rows.

Only the existing public PASS reader receives the workflow read token.  The
mathematical process is offline, has a read-only source mount, and writes no
recomputable data file.  This launcher performs no mathematics.
"""
import argparse
import hashlib
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path
from original_shadow_receipt_tools import canonical, digest, add_pinned_arguments, pinned_request

REPOSITORY = "Rogerhu12/math-research-public"
IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
TOPIC = Path("topics/rank2-sha-infinitely-many-p")
REQUEST = TOPIC/"ci/original-scalar-filtration-shadow-request.json"
WORKFLOW = Path(".github/workflows/rank2-sha-original-triangular-artinian-shadow.yml")
HERE = Path(__file__).resolve().parent


def progress(stage, **kw):
    print("RANK2_TRIANGULAR_ARTINIAN_HOST "+canonical(dict(stage=stage, **kw)),
          file=sys.stderr, flush=True)


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def request_arguments(root):
    raw = (root/REQUEST).read_bytes()
    assert len(raw) <= 32768
    obj = json.loads(raw)
    assert set(obj) == {"schema", "prime", "first", "packet", "phase", "trace_method",
                        "q_precision", "batch_size", "kernel_method", "linear_algebra", "run_api_preflight",
                        "source_sha256", "workflow_sha256"}
    assert obj["schema"] == "rank2-original-triangular-artinian-request/v13"
    assert type(obj["prime"]) is int and obj["prime"] in (29, 41)
    cli = ["--prime", str(obj["prime"])]
    keys = ("job", "run", "run_head", "source", "result_sha256")
    for stem in ("first", "packet"):
        pin = obj[stem]
        assert isinstance(pin, dict) and set(pin) == set(keys)
        for key in keys:
            if key in ("job", "run"):
                assert type(pin[key]) is int and pin[key] > 0
            else:
                assert isinstance(pin[key], str)
            cli += ["--"+stem+"-"+key.replace("_", "-"), str(pin[key])]
        assert pin["source"] == pin["run_head"]
    parser = argparse.ArgumentParser(add_help=False, allow_abbrev=False)
    add_pinned_arguments(parser)
    checked = pinned_request(parser.parse_args(cli))
    assert obj["phase"] == "shadow"
    assert obj["linear_algebra"] == "complete-scalar-filtration-native-original-shadow-v13"
    assert type(obj["run_api_preflight"]) is bool
    assert obj["trace_method"] in ("artinian",)
    assert type(obj["q_precision"]) is int and obj["q_precision"] >= 2453
    assert type(obj["batch_size"]) is int and obj["batch_size"] > 0
    assert obj["kernel_method"] in ("minimal", "hermite")
    extra = ["--phase", obj["phase"], "--trace-method", obj["trace_method"],
             "--q-precision", str(obj["q_precision"]),
             "--batch-size", str(obj["batch_size"]), "--kernel-method", obj["kernel_method"]]
    if obj["run_api_preflight"]:
        extra.append("--run-api-preflight")
    checked.update({key:obj[key] for key in ("phase", "trace_method", "q_precision", "batch_size", "kernel_method", "linear_algebra", "run_api_preflight")})
    expected_sources = obj["source_sha256"]
    assert isinstance(expected_sources, dict) and len(expected_sources) == 65
    assert all(isinstance(k, str) and isinstance(v, str) and len(v) == 64
               and set(v) <= set("0123456789abcdef")
               for k, v in expected_sources.items())
    workflow_hash = obj["workflow_sha256"]
    assert isinstance(workflow_hash, str) and len(workflow_hash) == 64
    assert set(workflow_hash) <= set("0123456789abcdef")
    return cli, checked, hashlib.sha256(raw).hexdigest(), extra, expected_sources, workflow_hash


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise SystemExit("Use only the public repository Actions host.")
    root = Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    assert HERE == root/TOPIC/"scripts"
    source = git(root, "rev-parse", "HEAD")
    assert source == os.environ["GITHUB_SHA"] and len(source) == 40
    run, attempt = os.environ["GITHUB_RUN_ID"], os.environ["GITHUB_RUN_ATTEMPT"]
    assert run.isdecimal() and attempt.isdecimal()
    cli, request, request_hash, extra, expected_sources, workflow_hash = request_arguments(root)
    names = (
        "launch-original-triangular-artinian-shadow.py",
        "produce-original-triangular-artinian-shadow.py",
        "produce-original-linear-fiber-artinian-shadow.py",
        "original_linear_fiber_frobenius.py",
        "original_pair_reset_row_reduction.py", "original_quadratic_norm_field.py",
        "original_triangular_artinian_values.py", "original_triangular_preimage_tools.py",
        "original_polynomial_row_reduction.py", "original_degree_bounded_row_reduction.py",
        "original_ys_equation_transport.py", "original_ys_geometry_transport.py",
        "original_full_w_basis_transport.py", "original_w_ideal_transport.py",
        "original_miller_batch_units.py",
        "original_ys_integral_image_tools.py",
        "original_ys_scalar_colon_tools.py",
        "launch-original-artinian-shadow.py", "produce-original-artinian-shadow.py",
        "produce-original-cube-section-fractions.py", "original_cube_compact_sections.py",
        "original_ys_artinian_norm_tools.py", "original_ys_exact_reuse.py", "original_ys_fraction_bridge.py", "original_ys_artinian_shadow_consumer.py",
        "original_affine_fast_operations.py", "original_section_ring_embedding.py",
        "original_ys_divisor_ideal_tools.py", "original_ys_closed_point_tools.py",
        "original_ys_local_value_tools.py", "original_shadow_relative_six_tools.py",
        "original_shadow_coefficient_tools.py", "original_shadow_tate_trace_tools.py",
        "original_affine_multiplication.py", "produce-original-y-affine-normalization.py",
        "produce-original-y-colon-apery.py", "produce-original-y-global-section-and-ys.py",
        "produce-original-tuv-section-fractions.py",
        "produce-original-map-section-fractions.py", "section_quotient_algebra.py",
        "read-original-shadow-pass-receipts.py", "original_shadow_receipt_tools.py",
        "produce-original-shadow-local-input.py", "original_good_prime_germ_tools.py",
        "check-r873-original-cm-petersson-degree.py", "original_low_weight_cm_tools.py",
        "produce-r917-original-global-rr-q-lattice.py", "original_pari_m2_basis.py",
        "original_shadow_coordinate_tools.py")
    names = names + ("launch-original-projector-artinian-shadow.py",
                     "produce-original-projector-artinian-shadow.py",
                     "original_projector_hermite.py")
    names = names + ("launch-original-native-row-artinian-shadow.py",
                     "produce-original-native-row-artinian-shadow.py",
                     "original_native_pair_reset.py",
                     "original_native_polynomial_rows.pyx")
    names = names + ("launch-original-complete-quadratic-shadow.py",
                     "produce-original-complete-quadratic-shadow.py",
                     "original_complete_quadratic_returns.py",
                     "original_complete_quadratic_polynomials.pyx")
    names = names + (
        "launch-original-scalar-filtration-shadow.py",
        "produce-original-scalar-filtration-shadow.py",
        "original_native_complete_return_binding.py",
        "original_current_idempotent_square.py",
        "original_scalar_base_divisor_support.py",
    )
    assert len(names) == len(set(names)) == 65
    assert set(expected_sources) == set(names)
    files = [TOPIC/"scripts"/name for name in names]+[
        REQUEST, WORKFLOW, Path("README.md"), TOPIC/"README.md"]
    assert not git(root, "status", "--porcelain", "--", *map(str, files))
    hashes = {str(p):hashlib.sha256((root/p).read_bytes()).hexdigest() for p in files}
    for name, expected in expected_sources.items():
        assert hashes[str(TOPIC/"scripts"/name)] == expected, "Pinned source changed: "+name
    assert hashes[str(WORKFLOW)] == workflow_hash
    readmes = {"root":git(root, "rev-parse", "HEAD:README.md"),
               "topic":git(root, "rev-parse", "HEAD:"+str(TOPIC/"README.md"))}
    manifest = dict(source=source, run_id=run, run_attempt=attempt, image=IMAGE,
                    parameters=request, request_sha256=request_hash,
                    source_file_sha256=hashes, readme_blobs=readmes,
                    mathematical_scope="same original two-chart integral consumer: "+request["phase"]+"",
                    token_location="host public PASS reader only", source_mount="read-only",
                    Sage_network_mode="none", recomputable_data_file_written=False,
                    all_65_code_sources_match_fixed_request=True,
                    actual_workflow_matches_fixed_request=True)
    progress("pinned original PASS request and source checked", **manifest)
    progress("host manifest digest", sha256=digest(manifest))
    host_env = os.environ.copy()
    host_env["PYTHONDONTWRITEBYTECODE"] = "1"
    clean_env = {key:value for key, value in host_env.items()
                 if key not in ("GH_TOKEN", "GITHUB_TOKEN", "RANK2_GITHUB_TOKEN",
                                "RANK2_ACTIONS_READ_TOKEN", "RANK2_GITHUB_PAT")}
    container = "rank2-triangular-artinian-shadow-"+run+"-"+attempt
    values = {
        "GITHUB_ACTIONS":"true", "GITHUB_REPOSITORY":REPOSITORY,
        "RANK2_SOURCE_SHA":source, "RANK2_RUN_ID":run,
        "RANK2_RUN_ATTEMPT":attempt, "RANK2_IMAGE":IMAGE,
        "RANK2_LINEAR_ALGEBRA":request["linear_algebra"],
        "RANK2_ROOT_README_SHA":readmes["root"],
        "RANK2_TOPIC_README_SHA":readmes["topic"],
        "PYTHONDONTWRITEBYTECODE":"1", "PYTHONUNBUFFERED":"1", "OMP_NUM_THREADS":"4"}
    command = ["docker", "run", "--rm", "--init", "--network", "none",
               "--name", container, "-i"]
    for key, value in values.items():
        command += ["-e", key+"="+value]
    command += ["-v", str(root)+":/work:ro", "-w", "/work",
                "--entrypoint", "/usr/bin/sage", IMAGE, "-python",
                str(TOPIC/"scripts/produce-original-scalar-filtration-shadow.py"), *cli, *extra]
    reader, sage, success = None, None, False
    started = time.monotonic()

    def interrupted(signum, frame):
        raise InterruptedError("Public host pipeline interrupted by signal "+str(signum))

    old = {s:signal.signal(s, interrupted) for s in (signal.SIGTERM, signal.SIGINT)}
    try:
        reader = subprocess.Popen([sys.executable, str(HERE/"read-original-shadow-pass-receipts.py"), *cli],
                                  cwd=root, env=host_env, stdout=subprocess.PIPE)
        sage = subprocess.Popen(command, cwd=root, env=clean_env, stdin=reader.stdout)
        reader.stdout.close()
        reader_returncode = reader.wait(timeout=600)
        progress("original PASS reader exited", returncode=reader_returncode)
        assert reader_returncode == 0, "Both true original PASS receipts are required."
        remaining = 21000-(time.monotonic()-started)
        assert remaining > 0
        sage_returncode = sage.wait(timeout=remaining)
        progress("offline complete original source solver exited", returncode=sage_returncode)
        assert sage_returncode == 0, "The offline original integral consumer failed with return code "+str(sage_returncode)
        success = True
        progress("both original authentication and requested original integral consumer gates succeeded",
                 source=source, run_id=run, elapsed_seconds=time.monotonic()-started)
    finally:
        if not success:
            progress("pipeline incomplete; no mathematical PASS is asserted", source=source, run_id=run)
            for child in (reader, sage):
                if child is not None and child.poll() is None:
                    child.terminate()
            subprocess.run(["docker", "rm", "-f", container], env=clean_env,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           timeout=30, check=False)
            for child in (reader, sage):
                if child is not None:
                    try:
                        child.wait(timeout=15)
                    except subprocess.TimeoutExpired:
                        child.kill()
                        child.wait(timeout=15)
        for sig, handler in old.items():
            signal.signal(sig, handler)


if __name__ == "__main__":
    main()
