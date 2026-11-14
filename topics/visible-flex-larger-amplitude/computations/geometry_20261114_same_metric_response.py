#!/usr/bin/env python3
"""Full original boundary response at fixed scalar metric, K=k=0.

Use the original boundary-response CLI with --accepted pointing to the
genuinely accepted complete parent field and --prepared to its v4 initial
guess.  Every core is released and no active scalar control is introduced.
All field/tail rows, original FD levels, contractions and 5e-5 threshold
remain in the original complete response calculation.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import json
from pathlib import Path
import sys
import numpy as np

import geometry_20261114_full_dn_response as original
from geometry_20261114_lifted_modes_profile import field_spec, sha
from geometry_20261114_same_metric_profile import SCHEMA, freeze_spec, reconstruct_profile

HERE = Path(__file__).resolve().parent


def path(name):
    return Path(sys.argv[sys.argv.index(name) + 1])


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run numerical boundary responses in the public repository's Actions")
    parent, prepared = original.read(path("--accepted")), original.read(path("--prepared"))
    M, N = int(prepared["M"]), int(prepared["N"])
    expected = freeze_spec(parent, M, sha(path("--accepted")))
    if (prepared["complete_scalar_profile"] != expected
            or prepared.get("field_representation") != field_spec(M, N)
            or prepared.get("active_scalar_parameters") != 0 or prepared.get("fixed_core_modes") != 0
            or prepared.get("parent_binding", {}).get("parent_sha256") != sha(path("--accepted"))):
        raise ValueError("Use the actually bound same-metric complete prepared field")
    frozen = reconstruct_profile(expected)
    constructor = original.original.native.outward.FullCoreProbe
    boundary_constructor = original.FullDNBoundary
    def probe(core, source_M, source_N, velocity, length, k0):
        if (int(source_M), int(source_N)) != (int(parent["M"]), int(parent["N"])):
            raise ValueError("The complete accepted parent identity changed")
        return constructor(np.pad(np.asarray(core), (0, M - source_M)), M, N, velocity, length, k0)
    def profile(source, port, peak, source_modes):
        if (int(source_modes) != int(parent["M"])
                or port != expected["complete_original_port"]
                or peak != expected["frozen_design_scalar_profile"]["peak_curvature"]):
            raise ValueError("Do not replace the frozen scalar/tail metric")
        return frozen
    def boundary(profile, unused_old_three_targets, *args, **kwargs):
        # K=0 is the explicit R240 refinement problem; old low-core design
        # constraints must not survive merely because the original setup
        # passes its usual three-coefficient argument.
        return boundary_constructor(profile, np.empty(0), *args, **kwargs)
    original.original.native.outward.FullCoreProbe = probe
    original.CompleteProfile = profile
    original.FullDNBoundary = boundary
    original.__file__ = __file__
    result = original.main()
    output = path("--out") / "response-check.json"
    report = json.loads(output.read_text())
    report["same_metric_implementation"] = dict(
        scalar_schema=SCHEMA, canonical_scalar_identity_sha256=expected["canonical_scalar_identity_sha256"],
        parent_sha256=sha(path("--accepted")), field_modes=M, angular_quadrature=N,
        tail_modes=M, fixed_core_modes=0, active_scalar_parameters=0,
        state_dimension=4 * M + 2, left_rows=3 * M + 2, right_rows=M,
        frozen_design_parameters=expected["frozen_design_parameters"],
        adapter_source_sha256=sha(__file__),
        scalar_profile_source_sha256=sha(HERE / "geometry_20261114_same_metric_profile.py"),
        original_response_source_sha256=sha(HERE / "geometry_20261114_full_dn_response.py"))
    output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    return result


if __name__ == "__main__":
    raise SystemExit(main())
