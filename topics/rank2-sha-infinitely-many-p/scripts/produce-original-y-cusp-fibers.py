#!/usr/bin/env sage-python
"""Read every original Y cusp, including all six length-289 branches."""
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
from section_quotient_algebra import canonical, digest
from original_section_ring_embedding import build_original_y_section_basis
from original_ys_cusp_fibers import build_original_ys_cusp_fibers
import original_section_ring_embedding
import original_ys_cusp_fibers
import finite_section_frobenius

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
CURRENT_STAGE = "initialization"


def progress(stage, **record):
    global CURRENT_STAGE
    CURRENT_STAGE = stage
    print("RANK2_Y_CUSPS_STAGE "+canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **record)), flush=True)


def emit(name, receipt):
    payload = canonical(receipt)
    print(name+"_RESULT "+payload, flush=True)
    print(name+"_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


def build_original_y_cusp_fibers(prime=29, q_precision=2453, batch_size=64):
    path = HERE/"produce-original-y-affine-normalization.py"
    spec = importlib.util.spec_from_file_location("original_y_cusps_normalization", str(path))
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    progress("original complete normalization and both charts start",
             prime=int(prime), q_precision=int(q_precision))
    affine, normalization_receipt = source.build_original_y_affine_normalization(
        prime=prime, q_precision=q_precision, batch_size=batch_size)
    emit("RANK2_Y_AFFINE", normalization_receipt)
    sections, sections_receipt = build_original_y_section_basis(
        affine, constants=None, progress=progress)
    context, fiber_receipt = build_original_ys_cusp_fibers(
        affine, sections, progress=progress, batch_size=batch_size)
    dependencies = [path, Path(original_section_ring_embedding.__file__),
                    Path(original_ys_cusp_fibers.__file__),
                    Path(finite_section_frobenius.__file__),
                    HERE/"original_affine_multiplication.py",
                    HERE/"produce-original-y-colon-apery.py",
                    HERE/"section_quotient_algebra.py"]
    receipt = {
        "kind":"rank2_original_Y_complete_cusp_fibers_pipeline",
        "status":"same_original_two_chart_normalization_and_all_six_thick_cusp_fibers",
        "prime":int(prime), "level":3468, "q_precision":int(q_precision),
        "batch_size":int(batch_size),
        "complete_original_normalization_receipt_sha256":digest(normalization_receipt),
        "same_original_666_section_embedding":sections_receipt,
        "complete_original_cusp_fibers":fiber_receipt,
        "all_original_cusp_scheme_data_retained_in_process":True,
        "large_intersection_divisors_computed":False,
        "original_shadow_computed":False,
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID", os.environ.get("GITHUB_RUN_ID")),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "image":os.environ.get("RANK2_IMAGE"), "sage_version":SAGE_VERSION,
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
        "readme_blobs":{"root":os.environ.get("RANK2_ROOT_README_SHA"),
                        "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    context["complete_pipeline_receipt"] = receipt
    return context, receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    parser.add_argument("--q-precision", type=int, default=2453)
    parser.add_argument("--batch-size", type=int, default=64)
    args = parser.parse_args()
    context, receipt = build_original_y_cusp_fibers(
        args.prime, args.q_precision, args.batch_size)
    globals()["ORIGINAL_Y_COMPLETE_CUSP_FIBERS_CONTEXT"] = context
    emit("RANK2_Y_CUSPS", receipt)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = CURRENT_STAGE
        progress("failed", failed_stage=failed,
                 exception_type=type(exc).__name__, message=str(exc))
        raise
