#!/usr/bin/env sage-python
"""R922: certify the same original middle coordinate, without claiming RR completion."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical producer only in the public repository Actions.")

import argparse
import hashlib
import importlib.util
import json
import time
from pathlib import Path
from sage.all import set_random_seed
from sage.env import SAGE_VERSION
import original_rr_primitive_algebra as algebra

HERE = Path(__file__).resolve().parent
GEOMETRY_PATH = HERE / "produce-r919-original-shadow-rr-tate19-geometry-first.py"
_SPEC = importlib.util.spec_from_file_location("r922_original_geometry", GEOMETRY_PATH)
geometry = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(geometry)
base = geometry.base
STARTED = time.monotonic()
SEED = 20261116


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    args = parser.parse_args()
    set_random_seed(SEED)
    terms, phi_hash = base.hecke17_level3()
    algebra.universal_linear_remainder(args.prime, terms, base.progress)
    fields = geometry.make_atkin_fields(args.prime, terms)
    B, T, V = fields["field"], fields["T"], fields["V"]
    U, certificate = algebra.recover_original_middle(
        args.prime, terms, B, T, V, base.evaluate_phi, base.progress)
    assert fields["W"](U) == B(729)/U
    assert fields["W3"](U) == B(729)/U
    base.progress("r922: same original U and both full Atkin identities certified")
    dependencies = [
        GEOMETRY_PATH, HERE / "original_rr_primitive_algebra.py",
        HERE / "original_rr_fraction_free_algebra.py",
        HERE / "produce-original-shadow-rr-eta48.py"]
    result = {
        "kind":"rank2_original_middle_coordinate_certificate",
        "status":"exact_original_U_only",
        "prime":args.prime, "field_model":"original eta48",
        "function_field_degree":48,
        "phi17_integer_terms_sha256":phi_hash,
        "direct_tate_certificate":fields["direct_tate_certificate"],
        "separability":fields["algebra_certificate"]["separability"],
        "middle_coordinate_certificate":certificate,
        "both_original_U_Atkin_identities":True,
        "original_coordinates_sha256":base.hash_functions([T, U, V]),
        "original_U_sha256":base.hash_functions([U]),
        "rr_normalization_or_basis_claimed":False,
        "scope":"The same original U only, with both full Phi17 identities, original eta48 branch, and both absolute Atkin identities. All RR and shadow gates remain separate.",
        "seed":SEED, "sage_version":SAGE_VERSION,
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID"),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{
            p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
        "readme_blobs":{
            "README.md":os.environ.get("RANK2_ROOT_README_SHA"),
            "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "elapsed_seconds":time.monotonic()-STARTED}
    payload = base.canonical(result)
    print("RANK2_ORIGINAL_U_RESULT "+payload, flush=True)
    print("RANK2_ORIGINAL_U_SHA256 "+
          hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = base.CURRENT_STAGE
        base.progress("failed", failed_stage=failed,
                      exception_type=type(exc).__name__, message=str(exc))
        raise
