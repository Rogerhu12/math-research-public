#!/usr/bin/env python3
"""Freeze one complete v3 scalar metric across independent field refinements.

The original three design controls and all scalar formulas stay inside one
verbatim v3 specification.  Refinement has zero active scalar controls and
zero fixed inlet core modes.  New physical/tail mode counts do not rewrite
the old accepted source-prefix identity or refreeze an empty parameter list.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import geometry_20261114_lifted_modes_profile as design
from geometry_20261114_full_scalar_profile import FrozenCompleteProfile


HERE = Path(__file__).resolve().parent
SCHEMA = "frozen-complete-scalar-same-metric-refinement-v4"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_scalar_identity(specification):
    """Hash the same full v3 design data, independently of live field modes."""
    raw = json.dumps(specification, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=False, allow_nan=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _design_specification(geometry):
    schema = geometry.get("schema")
    if schema == design.SCHEMA:
        specification = geometry
    elif schema == SCHEMA:
        specification = geometry["frozen_design_scalar_profile"]
        if (geometry.get("active_scalar_parameters") != 0 or geometry.get("fixed_core_modes") != 0
                or geometry.get("canonical_scalar_identity_sha256") != canonical_scalar_identity(specification)
                or geometry.get("frozen_design_parameters") != specification.get("frozen_design_parameters")
                or geometry.get("complete_original_port") != specification.get("complete_original_port")
                or geometry.get("profile_source_sha256") != sha(__file__)
                or geometry.get("independent_modes_scalar_profile_sha256") != sha(design.__file__)):
            raise ValueError("The previously frozen complete scalar identity changed")
    else:
        raise ValueError("Freeze a genuinely accepted v3 full design or an existing v4 refinement")
    if (specification.get("schema") != design.SCHEMA
            or len(specification.get("frozen_design_parameters", [])) != 3
            or int(specification["tail_modes"]) != int(specification["field_modes"])):
        raise ValueError("Retain the original full v3 design and its three solved controls")
    return specification


def freeze_spec(parentactual, newM, parentSHA):
    """Serialize one fixed scalar; actual nonlinear acceptance is not created."""
    if (parentactual.get("success") is not True or parentactual.get("status") != 0
            or not parentactual.get("actual_tail")):
        raise ValueError("A genuine accepted complete full-DN parent is required")
    if (not isinstance(parentSHA, str) or len(parentSHA) != 64
            or any(c not in "0123456789abcdef" for c in parentSHA)):
        raise ValueError("Bind the actual parent checkpoint SHA256")
    geometry = parentactual["fixed_scalar_profile"]["geometry"]
    specification = _design_specification(geometry)
    M = int(newM)
    parent_M = int(parentactual["M"])
    if newM != M or M < parent_M or parent_M < int(specification["field_modes"]):
        raise ValueError("A field refinement must retain every parent and design mode")
    return dict(schema=SCHEMA,
        frozen_design_scalar_profile=copy.deepcopy(specification),
        frozen_design_parameters=copy.deepcopy(specification["frozen_design_parameters"]),
        complete_original_port=copy.deepcopy(specification["complete_original_port"]),
        canonical_scalar_identity_sha256=canonical_scalar_identity(specification),
        canonical_json="UTF-8 json.dumps(sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)",
        field_modes=M, tail_modes=M,
        active_scalar_parameters=0, fixed_core_modes=0,
        base_prefix_M=int(specification["base_prefix_M"]),
        design_field_modes=int(specification["field_modes"]),
        accepted_parent_sha256=parentSHA, parent_field_modes=parent_M,
        accepted_source_prefix_sha256=specification["accepted_prefix_sha256"],
        profile_source_sha256=sha(__file__),
        independent_modes_scalar_profile_sha256=sha(design.__file__),
        canonical_material_metric="The unchanged ds^2+a(s;p*)^2*dtheta^2 from frozen_design_scalar_profile",
        scalar_design_controls_remain_frozen=True,
        live_field_modes_do_not_change_metric=True,
        new_field_acceptance_created=False)


def reconstruct_profile(geometry):
    if geometry.get("schema") != SCHEMA:
        return design.reconstruct_profile(geometry)
    specification = _design_specification(geometry)
    M = int(geometry["field_modes"])
    if (int(geometry["tail_modes"]) != M or M < int(specification["field_modes"])
            or geometry.get("base_prefix_M") != int(specification["base_prefix_M"])
            or geometry.get("design_field_modes") != int(specification["field_modes"])):
        raise ValueError("The live field resolution is incompatible with the frozen design")
    original_frozen = design.reconstruct_profile(specification)
    # original_frozen.frozen_parameters are the three old p* values; the
    # empty active vector of a later refinement is intentionally never used.
    result = FrozenCompleteProfile(original_frozen.designed,
        specification["frozen_design_parameters"], field_modes=M)
    result.canonical_scalar_identity_sha256 = geometry["canonical_scalar_identity_sha256"]
    result.frozen_design_scalar_profile = copy.deepcopy(specification)
    result.same_metric_refinement_schema = SCHEMA
    return result
