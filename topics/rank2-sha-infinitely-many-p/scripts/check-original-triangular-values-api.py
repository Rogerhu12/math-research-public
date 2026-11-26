#!/usr/bin/env sage-python
"""Public tiny API gate for complete paired graphs and affine source lifts.

This constructs only a specified quadratic finite-field fixture and tiny
matrices. It does not build original maps, a normalization, a divisor,
a norm, a closed point, an intersection, or a shadow.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import ast
import hashlib
import json
import time
from pathlib import Path
from sage.all import GF, PolynomialRing
from sage.env import SAGE_VERSION
from original_ys_divisor_ideal_tools import canonical, digest, field_description
from original_triangular_artinian_values import (
    triangular_value_preflight, SOURCE_DEPENDENCIES)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TOPIC = HERE.parent
REQUEST = TOPIC/"ci/original-triangular-values-api-request.json"
WORKFLOW = ROOT/".github/workflows/rank2-sha-triangular-values-api.yml"
IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
STARTED = time.monotonic()
SOURCE_FILES = tuple(dict.fromkeys((
    "check-original-triangular-values-api.py",
) + SOURCE_DEPENDENCIES))


def progress(stage, **record):
    print("RANK2_TRIANGULAR_VALUE_API_STAGE "+canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **record)), flush=True)


def main():
    raw = REQUEST.read_bytes()
    assert len(raw) <= 4096
    request = json.loads(raw)
    assert request == {
        "schema":"rank2-original-triangular-values-api/v1",
        "prime":29, "extension_degree":2,
        "modulus_ascending":[-2, 0, 1],
        "checks":["complete-paired-graph",
                  "complete-affine-source-augmentation"],
        "original_geometry":False,
    }
    assert SAGE_VERSION == "10.6"
    source = os.environ["RANK2_SOURCE_SHA"]
    assert len(source) == 40 and all(c in "0123456789abcdef" for c in source)
    assert os.environ["RANK2_IMAGE"] == IMAGE
    assert os.environ["RANK2_RUN_ID"].isdecimal()
    assert os.environ["RANK2_RUN_ATTEMPT"].isdecimal()
    for key in ("RANK2_ROOT_README_SHA", "RANK2_TOPIC_README_SHA"):
        assert len(os.environ[key]) == 40
    for name in SOURCE_FILES:
        ast.parse((HERE/name).read_text(encoding="utf-8"), filename=name)
    files = [HERE/name for name in SOURCE_FILES]+[
        REQUEST, WORKFLOW, ROOT/"README.md", TOPIC/"README.md"]
    manifest = {
        "source":source, "run_id":os.environ["RANK2_RUN_ID"],
        "run_attempt":os.environ["RANK2_RUN_ATTEMPT"],
        "image":IMAGE, "sage_version":SAGE_VERSION,
        "request":request, "request_sha256":hashlib.sha256(raw).hexdigest(),
        "source_sha256":{
            str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest()
            for path in files},
        "readme_blobs":{"root":os.environ["RANK2_ROOT_README_SHA"],
                        "topic":os.environ["RANK2_TOPIC_README_SHA"]},
        "source_mount_read_only":True, "Sage_network_mode":"none",
        "small_algorithm_fixture_only":True,
    }
    progress("source manifest and all source ASTs checked", manifest=manifest,
             manifest_sha256=digest(manifest))
    fp = GF(request["prime"])
    modulus_ring = PolynomialRing(fp, "r942_api_modulus")
    modulus = modulus_ring(request["modulus_ascending"])
    assert modulus.degree() == 2 and modulus.is_irreducible()
    k = GF(request["prime"]**request["extension_degree"],
           name="r942_api_a", modulus=modulus)
    assert k.degree() == 2 and k.gen()**2 == k(2)
    checked = triangular_value_preflight(k, progress=progress)
    assert checked["status"] == "complete_paired_graph_and_affine_augmentation_preflight_passed"
    result = {
        "kind":"rank2_R942_complete_graph_and_affine_API_preflight",
        "status":"complete_graph_and_affine_algorithm_API_gates_passed",
        "source":source, "run_id":os.environ["RANK2_RUN_ID"],
        "run_attempt":os.environ["RANK2_RUN_ATTEMPT"],
        "manifest_sha256":digest(manifest), "image":IMAGE,
        "sage_version":SAGE_VERSION, "test_constants":field_description(k),
        "constant_field_is_specified_algorithm_fixture":True,
        "complete_graph_and_affine_preimages":checked,
        "all_source_ASTs_checked":True,
        "source_file_count":len(SOURCE_FILES),
        "original_maps_recomputed":False,
        "original_normalization_recomputed":False,
        "original_divisors_norms_intersections_or_shadow_claimed":False,
        "coefficient_or_data_file_written":False,
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    payload = canonical(result)
    print("RANK2_TRIANGULAR_VALUE_API_RESULT "+payload, flush=True)
    print("RANK2_TRIANGULAR_VALUE_API_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    main()
