#!/usr/bin/env sage-python
"""Certify the complete original Y normalization, including both charts.

The complete colon/Apéry producer and every true basis product run in one
public Actions process.  All coefficient objects stay in process.  This
stage does not certify large intersection divisors or a Frobenius shadow.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical producer only in public research Actions.")

import argparse
import hashlib
import importlib.util
import time
from pathlib import Path
from sage.env import SAGE_VERSION
from section_quotient_algebra import canonical
from original_affine_multiplication import build_original_affine_multiplication
import original_affine_multiplication

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
CURRENT_STAGE = "initialization"


def progress(stage, **kw):
    global CURRENT_STAGE
    CURRENT_STAGE = stage
    print("RANK2_Y_AFFINE_STAGE " + canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **kw)), flush=True)


def emit(name, receipt):
    payload = canonical(receipt)
    print(name+"_RESULT "+payload, flush=True)
    print(name+"_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


def build_original_y_affine_normalization(prime=29, q_precision=2453, batch_size=64):
    path = HERE/"produce-original-y-colon-apery.py"
    spec = importlib.util.spec_from_file_location("original_y_affine_apery", str(path))
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    progress("complete original pole spaces and module basis start", prime=int(prime),
             q_precision=int(q_precision))
    apery, apery_receipt = source.build_original_y_colon_apery(prime, q_precision)
    emit("RANK2_Y_APERY", apery_receipt)
    progress("every original basis multiplication start", module_rank=306,
             symmetric_pairs=46971)
    context, multiplication_receipt = build_original_affine_multiplication(
        apery, progress=progress, batch_size=batch_size)
    receipt = {
        "kind":"rank2_original_Y_complete_affine_normalization",
        "status":"original_complete_colon_apery_and_both_normalized_chart_multiplications",
        "prime":int(prime), "level":3468, "q_precision":int(q_precision),
        "batch_size":int(batch_size),
        "original_apery":apery_receipt,
        "complete_multiplication":multiplication_receipt,
        "large_intersection_divisors_computed":False,
        "infinity_fiber_closed_points_computed":False,
        "original_shadow_computed":False,
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID", os.environ.get("GITHUB_RUN_ID")),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "image":os.environ.get("RANK2_IMAGE"), "sage_version":SAGE_VERSION,
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{
            path.name:hashlib.sha256(path.read_bytes()).hexdigest(),
            "original_affine_multiplication.py":hashlib.sha256(
                Path(original_affine_multiplication.__file__).read_bytes()).hexdigest()},
        "readme_blobs":{"root":os.environ.get("RANK2_ROOT_README_SHA"),
                        "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    context["complete_normalization_receipt"] = receipt
    return context, receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    parser.add_argument("--q-precision", type=int, default=2453)
    parser.add_argument("--batch-size", type=int, default=64)
    args = parser.parse_args()
    context, receipt = build_original_y_affine_normalization(
        args.prime, args.q_precision, args.batch_size)
    globals()["ORIGINAL_Y_AFFINE_NORMALIZATION_CONTEXT"] = context
    emit("RANK2_Y_AFFINE", receipt)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = CURRENT_STAGE
        progress("failed", failed_stage=failed,
                 exception_type=type(exc).__name__, message=str(exc))
        raise
