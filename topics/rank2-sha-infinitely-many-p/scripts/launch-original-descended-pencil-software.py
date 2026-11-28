#!/usr/bin/env python3
"""Verify the fixed public software request and bind the original descended-pencil checker to one run."""
import ast
from contextlib import redirect_stderr, redirect_stdout
from hashlib import sha256
from io import StringIO
import json
import os
from pathlib import Path
import re
import runpy
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
ROOT = TOPIC.parents[1]
REQUEST = TOPIC / "ci" / "original-descended-pencil-software-request.json"
WORKFLOW = ROOT / ".github/workflows/rank2-sha-original-descended-pencil-software.yml"
REQUEST_SHA = "634d6687d16aa7bf95d1f2818c29ff481b96ba529744f73c9008857f2f6cd0c2"
MANIFEST_SHA = "cd143ac54ad6fe394eba6a6c66009c3e0c7666eb6ff0c8d76807dbbbfd9bba9d"
IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
REPOSITORY = "Rogerhu12/math-research-public"
CHECKS = (("check-original-descended-pencil.py", "RANK2_DESCENDED_PENCIL_SOFTWARE"),)
PREFIX = "RANK2_DESCENDED_PENCIL_PUBLIC_SOFTWARE"
THREADS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")
CREDENTIALS = ("GITHUB_TOKEN", "GH_TOKEN", "ACTIONS_RUNTIME_TOKEN", "ACTIONS_ID_TOKEN_REQUEST_TOKEN")
GIB = 1024 ** 3


def encode(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()


def digest(data):
    return sha256(data).hexdigest()


def require(test, message):
    if not test:
        raise RuntimeError(message)


def emit(marker, data):
    raw = encode(data)
    print(marker + "_RESULT " + raw.decode(), flush=True)
    print(marker + "_SHA256 " + digest(raw), flush=True)


def source_binding():
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY") == REPOSITORY, "Public research Actions required")
    raw = REQUEST.read_bytes()
    require(digest(raw) == REQUEST_SHA, "Changed fixed software request")
    request = json.loads(raw)
    pins = request["source_sha256"]
    require(request["source_files"] == sorted(pins) and len(pins) == 40 and
            request["source_manifest_sha256"] == MANIFEST_SHA == digest(encode(pins)) and
            request["checks"] == [name for name, _ in CHECKS], "Changed fixed source manifest")
    actual = {}
    for name, expected in pins.items():
        require(Path(name).name == name, "Expected a source basename")
        data = (HERE / name).read_bytes()
        actual[name] = digest(data)
        require(actual[name] == expected, "Changed software input " + name)
        if name.endswith(".py"):
            ast.parse(data, filename=name)
    source = os.environ["RANK2_SOURCE_SHA"]
    run = os.environ["RANK2_RUN_ID"]
    attempt = os.environ["RANK2_RUN_ATTEMPT"]
    require(re.fullmatch("[0-9a-f]{40}", source) and run.isdecimal() and attempt.isdecimal() and
            os.environ["RANK2_IMAGE"] == IMAGE, "Incomplete source, run, or image identity")
    return dict(request_id=request["request_id"], request_sha256=digest(raw),
                run_id=run, run_attempt=attempt, repository=REPOSITORY, source=source,
                root_readme_blob=os.environ["RANK2_ROOT_README_SHA"],
                topic_readme_blob=os.environ["RANK2_TOPIC_README_SHA"],
                image=IMAGE, source_file_sha256=actual, source_manifest_sha256=digest(encode(actual)),
                launcher_sha256=digest(Path(__file__).read_bytes()),
                workflow_sha256=digest(WORKFLOW.read_bytes()))


def validate_pencil(receipt):
    require(receipt["status"] == "all_descended_pencil_small_software_checks_completed" and
            receipt["physical_rank306_geometry_executed"] is False and
            receipt["original_level1156_lattice_executed"] is False, "Changed fixture or production scope")
    src = receipt["actual_small_modular_lattice"]
    require((src["level"], src["full_rational_dimension"], src["faithful_jets"], src["high_jets"]) == (4,2,2,48) and
            src["complete_saturation"]["full_reduced_rank"] == 2 and
            src["complete_saturation"]["full_rational_transform_verified"] is True, "Incomplete actual modular source")
    frames = receipt["physical_modular_frames"]
    require((frames["true_modular_input_columns"],frames["true_complete_weight_two_rank"],
             frames["matched_both_global_frames_through_order"],frames["normalized_branch_coefficients"]) == (48,2,41,44)
            and all(re.fullmatch("[0-9a-f]{64}",frames[k]) for k in
                    ("full_returned_weight_two_jets_sha256","actual_basis_change_sha256")),
            "The true level-four lattice did not return both physical modular frames")
    high = receipt["actual_high_source_fixtures"]
    require(high["wrong_original_embedding_rejected"] is True and
            [(g["original_artin"],g["original_embedding"],g["actual_denominator_order"],
              g["actual_numerator_order"],g["high_source_coefficients_used"],g["actual_normalized_germ_coefficients"])
             for g in high["actual_sources"]] == [(0,0,3,2,1486,1483),(1,2,612,611,2095,1483)],
            "Missing high-section source, normalized window, or Artin rejection")
    cases = receipt["scalar_cases"]
    require([r["field_degree"] for r in cases] == [1,2], "Both actual coefficient fields are required")
    for row in cases:
        graph, pencil = row["complete_g3"], row["real_pencil"]
        require(graph["actual_complete_kernel_dimension"] == 2 and graph["true_equation_coefficients"] == 6 and
                graph["both_projections_injective"] is True and graph["full_kernel_proof"]["original_rank"] == 6 and
                graph["full_kernel_proof"]["every_original_kernel_row_verified"] is True and
                (pencil["actual_independent_multiplier_rank"],pencil["full_product_rows"],
                 pencil["true_product_coefficients"],pencil["whole_base_divisor_length"]) == (4,6,4,0) and
                row["actual_original_coordinate_receipt"]["actual_W8_inputs"] == 8 and
                (row["actual_repeated_pencil_rank"],row["actual_ramified_pole_order"]) == (3,3) and
                row["short_germ_rejected"] is True, "Incomplete full source or pencil certificate")
        require([(r["positive"],r["negative"]) for r in row["physical_charts"]] == [(8,7),(8,5)] and
                all(r["wrong_physical_paired_image_rejected"] is True and
                    re.fullmatch("[0-9a-f]{64}",r["post_ideal_identity"]) for r in row["physical_charts"]),
                "Missing genuine finite, reciprocal, or rejected physical image")
    rect = receipt["rectangular_cases"]
    require(len(rect) == 2 and all((r["full_source_rows"],r["returned_rank"],r["actual_deleted_zero_rows"]) == (4,2,2) and
                r["changed_syzygy_rejected"] is True and r["excessive_attached_degree_rejected"] is True and
                r["original_row_comparison"] is True for r in rect), "Incomplete physical rectangular return")
    binding = receipt["source_binding"]
    require(binding["reversible_new_call_sites"] == 1 and binding["mathematical_instances_by_binding"] == 0 and
            binding["general_zero_pole_method_and_full_paired_graph_unchanged"] is True and
            binding["original_scalar_support_runner_and_all_remaining_calls_preserved"] is True and
            (receipt["actual_selector_sessions"],receipt["actual_selected_original_endpoint_calls"]) == (1,0),
            "The real original selector failed or unexpectedly executed geometry")


def unique_line(lines, prefix):
    marker = prefix.encode() + b" "
    matches = [line[len(marker):] for line in lines if line.startswith(marker)]
    require(len(matches) == 1, "Missing or duplicated line " + prefix)
    return matches[0]


def receipt_from(stream, prefix):
    lines = stream.splitlines()
    body = unique_line(lines, prefix + "_RESULT")
    reported = unique_line(lines, prefix + "_SHA256")
    require(reported == digest(body).encode(), "Unbound complete result " + prefix)
    result = json.loads(body)
    require(body == encode(result), "Non-canonical full result " + prefix)
    return result, digest(body), len(body)


def checker_record(name, marker, stream):
    receipt, hashed, size = receipt_from(stream, marker)
    require(name == CHECKS[0][0], "Unreviewed checker path")
    validate_pencil(receipt)
    return dict(check_script=name, fixture_result=receipt, fixture_result_sha256=hashed,
                fixture_result_bytes=size, checker_output_bytes=len(stream), checker_output_sha256=digest(stream))


def execute():
    binding = source_binding()
    # Sage 10.6 sage-env resets OPENBLAS_NUM_THREADS to 1. Restore the
    # already inspected four-thread request before importing the fixture.
    # Record only this allowlist; never print values of credential variables.
    before = dict(thread_counts={t: os.environ.get(t) for t in THREADS},
                  credential_keys_present={t: t in os.environ for t in CREDENTIALS},
                  numpy_preloaded="numpy" in sys.modules)
    print(PREFIX + "_RUNTIME_BEFORE " + encode(before).decode(), flush=True)
    require(not before["numpy_preloaded"] and
            not any(before["credential_keys_present"].values()),
            "The numerical backend was already loaded or host credentials entered the container")
    for thread in THREADS:
        os.environ[thread] = "4"
    runtime = dict(before=before, thread_counts={t: os.environ.get(t) for t in THREADS},
                   numpy_preloaded="numpy" in sys.modules,
                   credential_keys_present={t: t in os.environ for t in CREDENTIALS})
    require(all(os.environ.get(t) == "4" for t in THREADS) and
            all(t not in os.environ for t in CREDENTIALS), "Incorrect isolated execution environment")
    emit(PREFIX + "_RUNTIME", runtime)
    print(PREFIX + "_SELECTOR " + encode(binding).decode(), flush=True)
    records = []
    started = time.monotonic()
    for name, marker in CHECKS:
        output = StringIO()
        try:
            with redirect_stdout(output), redirect_stderr(output):
                runpy.run_path(str(HERE / name), run_name="__main__")
        finally:
            data = output.getvalue().encode("utf-8")
            print(PREFIX + "_BEGIN " + name, flush=True)
            sys.stdout.buffer.write(data)
            sys.stdout.buffer.flush()
            print(PREFIX + "_END " + name, flush=True)
        require(data.endswith(b"\n"), "Incomplete checker output")
        records.append(checker_record(name, marker, data))
    require(binding == source_binding(), "Software sources changed within the descended-pencil execution")
    emit(PREFIX + "_PUBLIC", dict(binding=binding, runtime=runtime, checkers=records, status="PASS",
        elapsed_seconds=time.monotonic() - started, same_container=True, time_budget_seconds=420,
        cpu_limit=4, memory_limit_gib=16, swap_inclusive_limit_gib=16,
        original_rank306_geometry_executed=False, heavy_producer_executed=False))


def host_contract():
    binding = source_binding()
    container = json.load(sys.stdin)[0]
    config, host = container["Config"], container["HostConfig"]
    names = dict(item.split("=", 1) for item in config["Env"])
    launches = ["-python", str(Path(__file__).resolve().relative_to(ROOT)), "--execute"]
    require(config["Image"] == IMAGE and config["Entrypoint"] == ["/usr/bin/sage"] and
            config["Cmd"] == launches and config["WorkingDir"] == "/work" and not config["Tty"] and
            host["NetworkMode"] == "none" and host["Init"] is True and
            host["NanoCpus"] == 4_000_000_000 and host["Memory"] == host["MemorySwap"] == 16 * GIB,
            "Unexpected Docker execution or resource configuration")
    mounts = [m for m in container["Mounts"] if m["Destination"] == "/work"]
    require(len(mounts) == 1 and mounts[0]["Type"] == "bind" and mounts[0]["RW"] is False and
            Path(mounts[0]["Source"]).resolve() == ROOT and
            not any(m["Destination"].startswith("/work/") for m in container["Mounts"]),
            "Expected the complete read-only source checkout")
    fixed_env = ("GITHUB_ACTIONS", "GITHUB_REPOSITORY", "RANK2_SOURCE_SHA", "RANK2_RUN_ID",
                 "RANK2_RUN_ATTEMPT", "RANK2_ROOT_README_SHA", "RANK2_TOPIC_README_SHA", "RANK2_IMAGE")
    require(all(names.get(t) == os.environ[t] for t in fixed_env) and
            all(names.get(t) == "4" for t in THREADS) and
            all(t not in names for t in CREDENTIALS), "Unexpected container provenance or credentials")
    require(container["Id"] == os.environ["RANK2_DOCKER_ID"], "Docker container identity changed")
    emit(PREFIX + "_CONTRACT", dict(docker_id=container["Id"], binding=binding,
        actual_nano_cpus=host["NanoCpus"], actual_memory_bytes=host["Memory"],
        actual_memory_swap_bytes=host["MemorySwap"], actual_network=host["NetworkMode"],
        source_mount_read_only=True, host_credentials_absent=True, thread_counts={t: names[t] for t in THREADS},
        actual_entrypoint=config["Entrypoint"], actual_arguments=config["Cmd"], software_timeout_seconds=420))


def host_after():
    # The raw complete attached stream is preserved even if the checker aborts.
    stream = sys.stdin.buffer.read()
    sys.stdout.buffer.write(stream)
    sys.stdout.buffer.flush()
    envelope, hashed, size = receipt_from(stream, PREFIX + "_PUBLIC")
    binding = source_binding()
    require(unique_line(stream.splitlines(), PREFIX + "_SELECTOR") == encode(binding) and
            envelope["binding"] == binding and envelope["status"] == "PASS" and
            envelope["original_rank306_geometry_executed"] is False and
            envelope["heavy_producer_executed"] is False and envelope["same_container"] is True and
            (envelope["time_budget_seconds"], envelope["cpu_limit"], envelope["memory_limit_gib"],
             envelope["swap_inclusive_limit_gib"]) == (420, 4, 16, 16),
            "Host and container returned different source or resource bindings")
    runtime, runtime_hash, runtime_bytes = receipt_from(stream, PREFIX + "_RUNTIME")
    require(runtime == envelope["runtime"] and
            unique_line(stream.splitlines(), PREFIX + "_RUNTIME_BEFORE") == encode(runtime["before"]) and
            runtime["numpy_preloaded"] is False and runtime["before"]["numpy_preloaded"] is False and
            not any(runtime["credential_keys_present"].values()) and
            not any(runtime["before"]["credential_keys_present"].values()) and
            runtime["thread_counts"] == {t: "4" for t in THREADS},
            "The actual before-import thread restoration or credential boundary changed")
    rows = []
    for name, marker in CHECKS:
        begin = (PREFIX + "_BEGIN " + name + "\n").encode()
        end = (PREFIX + "_END " + name + "\n").encode()
        require(stream.count(begin) == stream.count(end) == 1, "Changed checker output boundaries")
        entry = checker_record(name, marker, stream.split(begin, 1)[1].split(end, 1)[0])
        require(receipt_from(stream, marker)[1] == entry["fixture_result_sha256"],
                "Unexpected duplicate or unbound checker receipt")
        rows.append(entry)
    require(rows == envelope["checkers"], "Independent full host outputs and combined envelope differ")
    docker_id = os.environ["RANK2_DOCKER_ID"]
    status = subprocess.check_output(["docker", "wait", docker_id], text=True, timeout=20).strip()
    require(status == "0", "The inspected Docker container did not exit successfully")
    emit(PREFIX + "_HOST", dict(status="PASS", docker_id=docker_id, container_exit_code=int(status),
        source=binding["source"], run_id=binding["run_id"], run_attempt=binding["run_attempt"],
        complete_attached_stream_bytes=len(stream), complete_attached_stream_sha256=digest(stream),
        runtime_result_bytes=runtime_bytes, runtime_result_sha256=runtime_hash,
        public_result_bytes=size, public_result_sha256=hashed, verified_source_count=len(binding["source_file_sha256"]),
        complete_fixture_result_sha256=[r["fixture_result_sha256"] for r in rows],
        complete_checker_output_sha256=[r["checker_output_sha256"] for r in rows]))


if __name__ == "__main__":
    commands = {"--host-contract": host_contract, "--host-after": host_after, "--execute": execute}
    require(len(sys.argv) == 2 and sys.argv[1] in commands, "Select one fixed software-check stage")
    commands[sys.argv[1]]()
