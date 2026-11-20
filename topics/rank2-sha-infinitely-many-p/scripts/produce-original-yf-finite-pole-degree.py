#!/usr/bin/env sage-python
"""R927's two finite readings from the same full original section contexts.

All mathematics runs in one offline public Actions process.  The complete
original cube kernel, nonreduced DS, and all six thick Y cusp fibers remain
in memory.  Only proof receipts and hashes are emitted, never data files.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematics only in the public research Actions.")
if any(os.environ.get(key) for key in ("GH_TOKEN", "GITHUB_TOKEN", "RANK2_GITHUB_TOKEN")):
    raise SystemExit("Keep repository tokens outside the Sage process.")

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path
from sage.env import SAGE_VERSION
from section_quotient_algebra import canonical, digest
from original_shadow_receipt_tools import add_pinned_arguments, pinned_request, validate_envelope
from original_yF_finite_pole_degree import build_original_first_pole_degree

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
CURRENT_STAGE = "initialization"
DEPENDENCIES = (
    "launch-original-yf-finite-pole-degree.py", "produce-original-yf-finite-pole-degree.py",
    "original_yF_finite_pole_degree.py", "produce-original-cube-section-fractions.py",
    "produce-original-map-section-fractions.py", "produce-original-ds-section-algebra.py",
    "produce-original-y-cusp-fibers.py", "original_ys_cusp_fibers.py",
    "finite_section_frobenius.py", "original_section_ring_embedding.py",
    "produce-original-y-affine-normalization.py", "original_affine_multiplication.py",
    "produce-original-y-colon-apery.py", "produce-original-y-global-section-and-ys.py",
    "produce-original-tuv-section-fractions.py", "section_quotient_algebra.py",
    "read-original-shadow-pass-receipts.py", "original_shadow_receipt_tools.py",
    "produce-original-shadow-local-input.py", "original_good_prime_germ_tools.py",
    "check-r873-original-cm-petersson-degree.py", "original_low_weight_cm_tools.py",
    "produce-r917-original-global-rr-q-lattice.py", "original_pari_m2_basis.py",
    "original_shadow_coordinate_tools.py")


def progress(stage, **record):
    global CURRENT_STAGE
    CURRENT_STAGE = stage
    print("RANK2_YF_FINITE_DEGREE_STAGE "+canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **record)), flush=True)


def emit(name, receipt):
    payload = canonical(receipt)
    print(name+"_RESULT "+payload, flush=True)
    print(name+"_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


def load_source(name, alias):
    spec = importlib.util.spec_from_file_location(alias, str(HERE/name))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    add_pinned_arguments(parser)
    parser.add_argument("--q-precision", type=int, default=2453)
    parser.add_argument("--batch-size", type=int, default=64)
    args = parser.parse_args()
    assert args.prime == 29 and args.q_precision >= 2453 and args.batch_size > 0
    request = pinned_request(args)
    incoming = sys.stdin.buffer.read(2*1024*1024+1)
    assert len(incoming) <= 2*1024*1024
    envelope = json.loads(incoming.decode("utf-8"))
    reader_hash = hashlib.sha256((HERE/"read-original-shadow-pass-receipts.py").read_bytes()).hexdigest()
    first, packet = validate_envelope(envelope, request, reader_hash)
    progress("both original complete characteristic-zero PASS authenticated",
             public_pass_envelope_sha256=envelope["envelope_sha256"])

    cube_module = load_source("produce-original-cube-section-fractions.py", "yf_degree_original_cube")
    cube, cube_receipt = cube_module.build_original_cube_section_fractions(args.prime, first, packet)
    emit("RANK2_CUBE_SECTIONS", cube_receipt)
    progress("whole original nonreduced DS and every closed component start")
    ds_module = load_source("produce-original-ds-section-algebra.py", "yf_degree_original_ds")
    ds, ds_receipt = ds_module.build_original_ds_section_algebra(
        prime=args.prime, q_precision=817, max_unit_trials=64, batch_size=128,
        with_frobenius=True)
    emit("RANK2_SECTION_DS", ds_receipt)
    progress("same complete original normalization and all six thick cusp fibers start")
    cusp_module = load_source("produce-original-y-cusp-fibers.py", "yf_degree_original_cusps")
    cusp, cusp_receipt = cusp_module.build_original_y_cusp_fibers(
        prime=args.prime, q_precision=args.q_precision, batch_size=args.batch_size)
    emit("RANK2_Y_CUSPS", cusp_receipt)
    progress("all original 900 denominators on DS and the full infinity 289 factor start")
    degree, degree_receipt = build_original_first_pole_degree(
        cube, ds, cusp, progress=progress, cube_receipt=cube_receipt)
    assert degree["cube_context"] is cube and degree["DS_context"] is ds
    assert degree["cusp_context"] is cusp and degree["certificate"] is degree_receipt
    assert degree_receipt["status"] == "same_original_e_z_and_exact_yF_degree_read"
    assert all(degree[key] == degree_receipt[key] for key in ("e", "z", "dF"))
    assert degree_receipt["dF"] == 2160+9*(degree_receipt["e"]-degree_receipt["z"])
    emit("RANK2_YF_FINITE_DEGREE_READINGS", degree_receipt)
    receipt = {
        "kind":"rank2_original_yF_finite_pole_degree_pipeline",
        "status":"all_original_finite_pole_degree_gates_completed",
        "prime":args.prime, "base_level":867, "level":3468,
        "q_precision":args.q_precision, "batch_size":args.batch_size,
        "DS_q_precision":817, "DS_batch_size":128, "DS_maximum_unit_trials":64,
        "same_original_cube_receipt_sha256":digest(cube_receipt),
        "same_original_DS_receipt_sha256":digest(ds_receipt),
        "same_original_complete_cusp_receipt_sha256":digest(cusp_receipt),
        "complete_finite_pole_degree_readings":degree_receipt,
        "e":degree_receipt["e"], "z":degree_receipt["z"], "dF":degree_receipt["dF"],
        "original_consumer_branch":degree_receipt["original_consumer_branch"],
        "same_process_mixed_F_kernel_receipt_retained":True,
        "all_original_contexts_retained_in_same_offline_process":True,
        "all_900_original_RF_denominators_retained":True,
        "full_nonreduced_DS_and_length_289_infinity_factor_retained":True,
        "large_intersection_divisors_computed":False,
        "original_shadow_computed":False,
        "characteristic_zero_exact_pole_degree_claimed":False,
        "ordinary_nonvanishing_or_infinitely_many_p_claimed":False,
        "public_pass_envelope_sha256":envelope["envelope_sha256"],
        "authenticated_public_jobs":envelope["authentication"],
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID"),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "image":os.environ.get("RANK2_IMAGE"), "sage_version":SAGE_VERSION,
        "readme_blobs":{"root":os.environ.get("RANK2_ROOT_README_SHA"),
                        "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                             for name in DEPENDENCIES},
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    globals()["ORIGINAL_YF_FINITE_POLE_DEGREE_CONTEXT"] = {
        "cube":cube, "cube_receipt":cube_receipt, "DS":ds, "cusps":cusp,
        "finite_degree":degree, "certificate":receipt}
    emit("RANK2_YF_FINITE_DEGREE", receipt)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = CURRENT_STAGE
        progress("failed", failed_stage=failed,
                 exception_type=type(exc).__name__, message=str(exc))
        raise
