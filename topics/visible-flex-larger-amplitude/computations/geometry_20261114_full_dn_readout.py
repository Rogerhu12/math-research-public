#!/usr/bin/env python3
"""Original physical C2 quintic readout on the complete frozen scalar profile.

Only the scalar-profile constructor is adapted to the serialized complete
AngleConnector/coast/finite-bridge formula and its solved control vector.
The original saved-RHS physical quintic, complete material-angle inversion,
first and second Cartesian derivatives and metric sampling remain intact.
These samples are not continuous reach bounds or a full closed assembly.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import sys
import geometry_20261114_material_quintic_readout as original
from geometry_20261114_full_scalar_profile import CompleteProfile, FrozenCompleteProfile

original_profile = original.base.fixed.FixedProfile


def exact_profile_formula(geometry):
    if geometry.get("schema") != "complete-controlled-scalar-profile-v1":
        return original_profile(geometry)
    # This metadata describes the already accepted input prefix. No new
    # nonlinear field is fabricated by reconstructing its scalar formula.
    source_metadata = dict(success=True, M=geometry["base_prefix_M"],
                           fixed_scalar_profile=dict(geometry=geometry["base_prefix_geometry"]),
                           mesh=[geometry["base_prefix_end"]])
    designed = CompleteProfile(source_metadata, geometry["complete_original_port"],
                               geometry["peak_curvature"], geometry["tail_modes"])
    return FrozenCompleteProfile(designed, geometry["frozen_design_parameters"])


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Evaluate the physical numerical readout in this public repository's Actions")
    original.base.fixed.FixedProfile = exact_profile_formula
    original.__doc__ = __doc__
    original.main()
    output = Path(sys.argv[sys.argv.index("--out") + 1])
    data = json.loads(output.read_text())
    data["complete_profile_readout_adapter_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    data["complete_scalar_profile_source_sha256"] = hashlib.sha256(Path(__file__).with_name(
        "geometry_20261114_full_scalar_profile.py").read_bytes()).hexdigest()
    output.write_text(json.dumps(data, indent=2) + "\n")


if __name__ == "__main__":
    main()
