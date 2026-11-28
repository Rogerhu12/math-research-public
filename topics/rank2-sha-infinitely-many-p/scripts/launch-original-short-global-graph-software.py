#!/usr/bin/env python3
"""Verify the fixed public software request and bind both original checkers to one run."""
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
REQUEST = TOPIC / "ci" / "original-short-global-graph-software-request.json"
WORKFLOW = ROOT / ".github/workflows/rank2-sha-original-short-global-graph-software.yml"
REQUEST_SHA = "03d325b63d505574486a1bb6034ea503db9094bae18513dd0db7dac3ca2c78f5"
MANIFEST_SHA = "d2f9ba0d1fcea025f7ddb592ef0abda68923e41adbca22103ae5f8cd819abe9a"
IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
REPOSITORY = "Rogerhu12/math-research-public"
CHECKS = (
    ("check-original-short-graph-multichain.py", "RANK2_SHORT_GRAPH_MULTICHAIN_SOFTWARE"),
    ("check-original-short-global-graph.py", "RANK2_SHORT_GLOBAL_GRAPH_SOFTWARE"),
)
PREFIX = "RANK2_SHORT_GRAPH_SOFTWARE"
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
    require(request["source_files"] == sorted(pins) and len(pins) == 43 and
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


def validate_multichain(receipt):
    manual = receipt["manual"]
    require(receipt["kind"] == "original_short_graph_multichain_software_only" and
            [row["field_degree"] for row in manual] == [1, 2, 2] and
            all(row["actual_chain_lengths"] == [0, 3, 2] and
                row["actual_zero_pivot_nonzero_tail"] is True and
                row["actual_complete_column_popov_return"] is True for row in manual) and
            manual[2]["actual_structure_constants"] == [22, 1] and
            manual[2]["actual_modulus_discriminant"] == 2 and
            manual[2]["actual_ground_field_products_and_inverses_returned"] is True,
            "Missing actual Popov, multichain, or non-binomial field return")
    admitted, declined = receipt["actual_prime_admissions"], receipt["actual_quadratic_original_pairs"]
    require(0 < admitted < 8 and 0 < declined < 8 and
            receipt["full_chart_comparisons"] == admitted + declined == 8 and
            receipt["actual_post_ideal_tamper_rejections"] == 2 and
            receipt["actual_proper_subgraph_rejections"] == 2 and
            receipt["production_geometry_claimed"] is False, "Missing whole ideal comparison or rejection")


def validate_global(receipt):
    graphs = receipt["actual_low_graphs"]
    # (constant degree, pole degree, window, full RR dimension, actual thick modulus degree)
    expected = [(1, 2, 2, 3, 4), (1, 4, 3, 3, 6), (1, 1, 2, 4, 3), (1, 1, 2, 4, 4),
                (2, 2, 2, 3, 4), (2, 4, 3, 3, 6), (2, 1, 2, 4, 3)]
    require(receipt["kind"] == "whole_short_thick_fibre_and_reversal_software_only" and
            len(graphs) == len(expected), "Missing actual small global graph")
    for row, (field, degree, window, dimension, precision) in zip(graphs, expected):
        weights = row["actual_original_paired_weights"]
        require(row["actual_constant_degree"] == field and row["true_projective_pole_degree"] == degree and
                row["actual_original_RR_dimension"] == dimension and
                row["actual_short_fibre_degree"] == precision and len(weights) == 2 and
                min(weights) >= 0 and max(weights) <= window and sum(weights) == 1 + degree,
                "A full two-chart model dimension, thick degree, or paired row weight changed")
    require(receipt["complete_chart_comparisons"] == 14 and
            receipt["truncated_thick_place_rejections"] == 2 and
            receipt["wrong_original_chart_rejections"] == 2 and
            receipt["actual_genuinely_quadratic_squared_fibre_comparisons"] == 1 and
            receipt["actual_both_complementary_projective_degrees_verified"] is True and
            receipt["explicit_quadratic_relation"] == "alpha^2=alpha+1/4 over F29" and
            receipt["original_rank306_geometry_executed"] is False, "Missing genuine reciprocal-chart check")


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
    if name == CHECKS[0][0]:
        validate_multichain(receipt)
    elif name == CHECKS[1][0]:
        validate_global(receipt)
    else:
        raise RuntimeError("Unreviewed checker path")
    return dict(check_script=name, fixture_result=receipt, fixture_result_sha256=hashed,
                fixture_result_bytes=size, checker_output_bytes=len(stream), checker_output_sha256=digest(stream))


def execute():
    binding = source_binding()
    require(all(os.environ.get(t) == "4" for t in THREADS) and
            all(t not in os.environ for t in CREDENTIALS), "Incorrect isolated execution environment")
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
    require(binding == source_binding(), "Software sources changed within the two-checker execution")
    emit(PREFIX + "_PUBLIC", dict(binding=binding, checkers=records, status="PASS",
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
    # The raw complete attached stream is preserved even if either checker aborts.
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
        public_result_bytes=size, public_result_sha256=hashed, verified_source_count=len(binding["source_file_sha256"]),
        complete_fixture_result_sha256=[r["fixture_result_sha256"] for r in rows],
        complete_checker_output_sha256=[r["checker_output_sha256"] for r in rows]))


if __name__ == "__main__":
    commands = {"--host-contract": host_contract, "--host-after": host_after, "--execute": execute}
    require(len(sys.argv) == 2 and sys.argv[1] in commands, "Select one fixed software-check stage")
    commands[sys.argv[1]]()
