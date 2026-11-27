#!/usr/bin/env python3
"""Deterministic scalar/node inputs for one fixed noncircular R690 target.

The original accepted099 file is used only for its immutable scalar defining
parameters. No BVP, pulse field, old core, old warm qjets or old adaptive mesh
defines this target. The target chart is the exact binary rational result of
a specified round-to-nearest-even conversion of seven rational Fejer values.
All large generated arrays remain runner outputs. This module is importable
with the standard library; physical/scalar generation requires public Actions.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import gzip
import hashlib
import heapq
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import subprocess
import sys
import time

TOPIC = "topics/visible-flex-larger-amplitude"
REPOSITORY = "Rogerhu12/math-research-public"
PREPARATION_SCHEMA = "complete-fixed-fejer-r690-input-preparation-v1"
NODE_SCHEMA = "complete-fixed-fejer-r690-affine-nodes-v1"
DEFINITION_SCHEMA = "fixed-fejer-r690-scalar-and-chart-recipe-v1"
TARGET_SCHEMA = "fixed-rn64-fejer-R690-mathematical-target-v1"
ACCEPTED_COMMIT = "60321451c058c6a51da58c37ae5ec6f2d1145f74"
ACCEPTED_PATH = TOPIC + "/notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz"
ACCEPTED_SHA256 = "b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff"
ACCEPTED_BYTES = 2614352
SCALAR_PARAMETERS_SHA256 = "e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa"
M = 160
K = 3
PREFIX_NODES = 819
J = 923
REFERENCE_N = 2048
LEGACY_P = 1845
P = 7377
PANELS = 128
SOURCE_PINS = {
    "scalar": (
        "notes/2026-11-17-parallel-model-full-hold-oracle.py",
        "a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670"),
    "integer": (
        "notes/2026-11-17-parallel-inward-integral-enclosure.py",
        "babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0"),
    "integer_trigonometry": (
        "notes/2026-11-17-parallel-geometry-inward-chord-cover.py",
        "e480a2ca7ebd5911768cad04ef7b98319ff2cff1840cf71531eaf2b574b4211a"),
    "hold": (
        "scripts/parallel_20261117_negative_hold_profile_ivp.py",
        "ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1"),
    "deep_scalar": (
        "scripts/resume_20261126/deep_valley_tail_input.py",
        "e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2"),
}
NPZ_MEMBERS = (
    "mesh", "initial_core", "fixed_core_first3", "radius", "width", "M", "J")
OUTPUT_ROLES = ("fixed_input", "node_report", "scalar_input")


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Scientific input construction is restricted to this public repository Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def file_record(path):
    p = Path(path).resolve()
    return dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p))


def write_json(path, value):
    Path(path).write_text(
        json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n",
        encoding="utf-8")


def _no_constant(value):
    raise ValueError("Nonfinite JSON number: " + value)


def _read_json_bytes(raw):
    return json.loads(raw, parse_constant=_no_constant)


def _fraction_from_binary64(value, name):
    if type(value) not in (int, float) or not math.isfinite(float(value)):
        raise ValueError("Finite original binary scalar parameter required: " + name)
    return F.from_float(float(value))


def _nearest_integer_even(numerator, denominator):
    q, r = divmod(numerator, denominator)
    if 2*r > denominator or (2*r == denominator and q % 2):
        q += 1
    return q


def round_binary64(value):
    """Exact rational -> unique IEEE754 binary64 RN-even, without libm."""
    value = F(value)
    if value == 0:
        return struct.unpack(">d", struct.pack(">Q", 0))[0]
    negative = value < 0
    value = abs(value)
    n, d = value.numerator, value.denominator
    exponent = n.bit_length() - d.bit_length()
    if exponent >= 0:
        if n < (d << exponent):
            exponent -= 1
    elif (n << -exponent) < d:
        exponent -= 1
    if exponent > 1023:
        raise OverflowError("Finite binary64 parameter required")
    if exponent < -1022:
        mantissa = _nearest_integer_even(n << 1074, d)
        if mantissa > (1 << 52):
            raise ArithmeticError("Subnormal rounding crossed more than one binade")
        bits = mantissa
    else:
        shift = 52 - exponent
        if shift >= 0:
            mantissa = _nearest_integer_even(n << shift, d)
        else:
            mantissa = _nearest_integer_even(n, d << -shift)
        if mantissa == (1 << 53):
            mantissa >>= 1
            exponent += 1
        if exponent > 1023:
            raise OverflowError("Finite binary64 parameter required after rounding")
        if not (1 << 52) <= mantissa < (1 << 53):
            raise ArithmeticError("Invalid normal binary64 significand")
        bits = ((exponent + 1023) << 52) | (mantissa - (1 << 52))
    if negative:
        bits |= 1 << 63
    answer = struct.unpack(">d", struct.pack(">Q", bits))[0]
    if not math.isfinite(answer):
        raise ArithmeticError("Nonfinite generated parameter")
    return answer


def chart_recipe():
    """Pure short mathematical recipe; no stored output coefficient table."""
    return dict(
        schema="seven-mode-positive-fejer-RN64-chart-recipe-v1",
        reference_modes=M, fixed_core_modes=K,
        fejer_baseline="1/4", fejer_order=7,
        ideal_formula="c_m=3*(8-m)*(-1)^(m+1)/(16*(4*m^2-1)), 1<=m<=7",
        zero_tail_rule="c_m=+0 exactly for 8<=m<=160",
        target_coefficient_rule=(
            "Round each exact rational ideal coefficient once to IEEE754 binary64 "
            "round-to-nearest ties-to-even; the resulting binary rational is the exact target coefficient"),
        rounding_implementation="round_binary64: integer quotient/remainder and IEEE754 bit construction",
        support_function="p(phi)=1+sum_m c_m*cos(2*m*phi)",
        angular_density="rho0(phi)=1+sum_m (1-4*m^2)*c_m*cos(2*m*phi)",
        material_chart="Theta0(phi)=phi+sum_m (1-4*m^2)*c_m*sin(2*m*phi)/(2*m)",
        ideal_density="1/4+(3/4)*K_7(2*phi-pi), K_7(t)=|sum_{j=0}^7 exp(i*j*t)|^2/8",
        ideal_coefficients_are_not_the_exact_rounded_target=True,
        original_solved_core_words_used=False,
        current_free_core_does_not_change_the_frozen_chart=True,
        current_free_core_and_height_all_retained=True,
        reference_scalar_error_bound="abs(RN64(c_m)-c_m)<=2^-53 for 1<=m<=7",
        complete_density_rounding_error_bound="553/9007199254740992",
        strict_density_lower_bound="1/4-553/9007199254740992",
        strict_density_upper_bound="25/4+553/9007199254740992",
        support_function_rounding_error_bound="7/9007199254740992",
        axial_support_gap_rounding_error_bound="8/9007199254740992",
        full_surface_or_reach_certificate_claimed=False)


def mathematical_target_recipe():
    """The fixed g recipe; observer/mesh/work budgets are deliberately absent."""
    return dict(
        schema=TARGET_SCHEMA,
        complete_scalar_parameters_identity_sha256=SCALAR_PARAMETERS_SHA256,
        scalar_parameter_origin=dict(
            repository=REPOSITORY, commit=ACCEPTED_COMMIT,
            path=ACCEPTED_PATH, sha256=ACCEPTED_SHA256, bytes=ACCEPTED_BYTES,
            consumed_projection="analytic_extension_origin and fixed_scalar_profile.geometry only",
            extraction_origin_fallback="same as parallel_20261117_continue.py",
            original_field_arrays_or_core_consumed=False),
        exact_scalar_law=dict(
            base="complete original exact FullHold scalar on its entire domain",
            base_source_sha256=SOURCE_PINS["scalar"][1],
            integer_source_sha256=SOURCE_PINS["integer"][1],
            integer_trigonometry_source_sha256=SOURCE_PINS["integer_trigonometry"][1],
            hold_source_sha256=SOURCE_PINS["hold"][1],
            R690_source_sha256=SOURCE_PINS["deep_scalar"][1],
            R690_formula="complete R690 equations (3)-(5), including the untruncated infinite deep-valley tail",
            old_scalar_defining_projection_is_preserved=True,
            integration_budget_or_leaf_count_does_not_define_g=True),
        fixed_chart=chart_recipe(),
        metric="ds^2+a_R690(s)^2*dTheta0(phi)^2",
        exact_radial_domain="0<=s<=the original exact FullHold S",
        exact_angular_domain="phi in R/(2*pi*Z)",
        physical_phase_range="t in [0,1], alpha=pi*t/2, with the R248 inverse-Theta0 conjugacy",
        old_frozen_target_identity_inherited=False,
        same_mathematical_g_as_old_warm_selected_chart_claimed=False,
        old_field_values_or_certificates_inherited=False)


def node_recipe():
    """Exact rational prefix and exact affine-in-S tail; no adaptive BVP mesh."""
    return dict(
        schema="deterministic-923-node-affine-in-S-discretization-v1",
        prefix_nodes=PREFIX_NODES, prefix_domain=["0", "1"],
        mandatory_prefix_nodes=(
            "All original scalar geometry knot s words interpreted as exact binary rationals; "
            "0,1,analytic_extension_origin,FullHold.cut and FullHold.cut+FullHold.f when in [0,1]"),
        prefix_completion=(
            "Until 819 nodes: split the longest exact rational gap at its exact midpoint; "
            "equal lengths choose the leftmost gap"),
        tail_groups=[
            dict(left="1", right="cut+f+hold", intervals=4),
            dict(left="cut+f+hold", right="cut+f+hold+rise", intervals=8),
            dict(left="cut+f+hold+rise", right="S-width", intervals=64),
            dict(left="S-width", right="S-out", intervals=12),
            dict(left="S-out", right="S", intervals=16)],
        fixed_binary_parameters=dict(
            cut="binary64 literal 0.995 interpreted as an exact rational",
            f="binary64 literal 0.002 interpreted as an exact rational",
            hold="binary64 literal 0.02 interpreted as an exact rational",
            rise="binary64 literal 0.02 interpreted as an exact rational",
            out="binary64 literal 0.02 interpreted as an exact rational",
            width="binary64 literal 0.05 interpreted as an exact rational"),
        carrier_rule=(
            "For S-coefficient zero, RN-even64 of the exact rational constant. "
            "Otherwise RN-even64 of the midpoint of the same complete FullHold outward affine-time box."),
        original_adaptive_BVP_nodes_used=False,
        old_cell_and_u_imply_same_physical_point=False,
        old_known_addresses_require_explicit_new_target_interpretation=True,
        zero_tail_or_unvisited_scalar_domain_dropped=False,
        total_nodes=J, total_cells=J-1,
        legacy_node_and_midpoint_rows=LEGACY_P,
        current_six_Gauss_rows=P-LEGACY_P,
        current_total_rows=P)


def fixed_definition():
    target = mathematical_target_recipe()
    return dict(
        schema=DEFINITION_SCHEMA,
        definition_source_sha256=sha(__file__),
        mathematical_target_recipe=target,
        mathematical_target_identity_sha256=canonical(target),
        node_recipe=node_recipe(),
        finite_reference_layout=dict(
            reference_M=M, fixed_K=K, reference_J=J, reference_full_N=REFERENCE_N,
            reference_quarter_angles=REFERENCE_N//4+1, reference_P=P,
            legacy_P=LEGACY_P, observation_Gauss_order=6,
            initial_height_Gauss_order=8, full_scalar_panels=PANELS),
        source_sha256_by_role={key: value[1] for key, value in SOURCE_PINS.items()},
        initial_height_rule=(
            "The new complete reference constructor uses the original whole-cell "
            "eight-Gauss integral of normalized c; H remains a free variable and is not part of g"),
        fixed_input_npz_members=list(NPZ_MEMBERS),
        prior_same_field_or_same_finite_reference_claimed=False,
        elapsed_time_or_runner_identity_selects_target=False,
        source_produced_array_tables_are_not_repository_parameters=True)


def chart_coefficients():
    """Return 160 declared working/target words and exact generation evidence."""
    values = []
    details = []
    weighted = F(0)
    support_fee = F(0)
    gap_fee = F(0)
    theta_fee = F(0)
    for m in range(1, M+1):
        ideal = F(3*(8-m)*((-1)**(m+1)), 16*(4*m*m-1)) if m <= 7 else F(0)
        value = round_binary64(ideal)
        rounded = F.from_float(value)
        fee = abs(rounded-ideal)
        values.append(value)
        if m <= 7:
            if fee > F(1, 1 << 53):
                raise ArithmeticError("The exact parameter rounding exceeds its stated bound")
            weighted += (4*m*m-1)*fee
            support_fee += fee
            theta_fee += F(4*m*m-1, 2*m)*fee
            if m % 2:
                gap_fee += 2*fee
            details.append(dict(mode=m, ideal_rational=str(ideal),
                rounded_binary64_hex=value.hex(), rounded_exact_binary_rational=str(rounded),
                absolute_rounding_error_exact=str(fee)))
        elif value.hex() != "0x0.0p+0":
            raise ArithmeticError("The mathematical zero tail is positive exact zero")
    lo = F(1,4)-weighted
    hi = F(25,4)+weighted
    if lo <= 0:
        raise ArithmeticError("The source-defined chart density must be strictly positive")
    return values, dict(
        recipe=chart_recipe(), seven_parameter_roundings=details,
        exact_density_rounding_bound=str(weighted),
        exact_support_function_rounding_bound=str(support_fee),
        exact_axial_support_gap_rounding_bound=str(gap_fee),
        exact_Theta_rounding_bound=str(theta_fee),
        exact_density_lower_bound=str(lo), exact_density_upper_bound=str(hi),
        exact_core_curvature_upper_bound=str(1/lo),
        target_coefficients_are_exact_binary_rationals=True,
        ideal_rational_target_falsely_claimed=False,
        complete_zero_tail_count=M-7)


def scalar_projection(data):
    """Exactly the inherited defining projection, without using old core/state."""
    if not isinstance(data, dict) or data.get("success") is not True:
        raise ValueError("The fixed historical accepted input must retain its genuine source status")
    profile = data.get("fixed_scalar_profile", data.get("inherited_profile"))
    if not isinstance(profile, dict) or not isinstance(profile.get("geometry"), dict):
        raise ValueError("The complete original fixed scalar geometry is required")
    extension = data.get("extension_scalar", {})
    if not isinstance(extension, dict):
        raise ValueError("Malformed original extension metadata")
    if "analytic_extension_origin" in data:
        origin = float(data["analytic_extension_origin"])
    elif "start" in extension:
        origin = float(extension["start"])
    else:
        origin = float(data["mesh"][-1])
    if not math.isfinite(origin):
        raise ValueError("The original scalar origin must be finite")
    value = dict(analytic_extension_origin=origin, geometry=copy.deepcopy(profile["geometry"]))
    if canonical(value) != SCALAR_PARAMETERS_SHA256:
        raise ValueError("The direct accepted099 projection is not the complete fixed e640 scalar input")
    knots = value["geometry"].get("knots")
    if not isinstance(knots, list) or len(knots) < 2:
        raise ValueError("Retain every original scalar knot")
    xs = [_fraction_from_binary64(k["s"], "scalar knot s") for k in knots]
    if xs[0] != 0 or any(b <= a for a, b in zip(xs, xs[1:])):
        raise ValueError("The complete fixed scalar knots must be strictly increasing from zero")
    if xs[-1] != F.from_float(origin):
        raise ValueError("The original analytic origin is the last fixed scalar knot")
    return value


def exact_node_definitions(parameters):
    geometry = parameters["geometry"]
    origin = _fraction_from_binary64(parameters["analytic_extension_origin"], "origin")
    cut, f = F.from_float(.995), F.from_float(.002)
    hold = rise = out = F.from_float(.02)
    width = F.from_float(.05)
    points = {F(0), F(1), origin, cut, cut+f}
    for knot in geometry["knots"]:
        points.add(_fraction_from_binary64(knot["s"], "knot"))
    if any(x < 0 or x > 1 for x in points):
        raise ValueError("This fixed prefix recipe requires all original scalar knots in [0,1]")
    if len(points) > PREFIX_NODES:
        raise ValueError("The complete original knots cannot be truncated to fit the reference layout")
    ordered = sorted(points)
    heap = [(-(right-left), left, right) for left, right in zip(ordered, ordered[1:])]
    heapq.heapify(heap)
    while len(points) < PREFIX_NODES:
        negative_width, left, right = heapq.heappop(heap)
        if negative_width != left-right:
            raise ArithmeticError("Inconsistent exact prefix interval")
        middle = (left+right)/2
        if middle in points:
            raise ArithmeticError("Duplicate exact dyadic refinement point")
        points.add(middle)
        heapq.heappush(heap, (-(middle-left), left, middle))
        heapq.heappush(heap, (-(right-middle), middle, right))
    definitions = [(F(0), value) for value in sorted(points)]
    first_rise = cut+f+hold
    last_rise = first_rise+rise
    groups = [
        ((F(0),F(1)), (F(0),first_rise), 4),
        ((F(0),first_rise), (F(0),last_rise), 8),
        ((F(0),last_rise), (F(1),-width), 64),
        ((F(1),-width), (F(1),-out), 12),
        ((F(1),-out), (F(1),F(0)), 16)]
    for left, right, count in groups:
        if definitions[-1] != left:
            raise ArithmeticError("The complete exact mesh must concatenate")
        for j in range(1, count+1):
            t = F(j,count)
            definitions.append(((1-t)*left[0]+t*right[0], (1-t)*left[1]+t*right[1]))
    if (len(definitions) != J or definitions[0] != (F(0),F(0))
            or definitions[-1] != (F(1),F(0)) or len(set(definitions)) != J):
        raise ArithmeticError("The complete exact node domain/layout differs")
    return definitions


def _source_paths(repo):
    root = Path(repo).resolve()
    out = {}
    for role, (relative, expected) in SOURCE_PINS.items():
        path = root/TOPIC/relative
        if sha(path) != expected:
            raise ValueError("Changed complete fixed scalar source: " + role)
        out[role] = path
    return out


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError("Cannot load the complete source " + str(path))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _array_record(array):
    import numpy as np
    value = np.ascontiguousarray(array)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    payload = value.tobytes(order="C")
    h.update(payload)
    return dict(dtype=str(value.dtype), shape=list(value.shape),
        sha256=h.hexdigest(), payload_sha256=hashlib.sha256(payload).hexdigest(),
        payload_bytes=len(payload))


def _restore_accepted(repo, path):
    if path is not None:
        candidate = Path(path).resolve()
    else:
        raise ValueError("Internal restoration destination is required")
    if not candidate.exists():
        candidate.parent.mkdir(parents=True, exist_ok=True)
        with candidate.open("wb") as stream:
            subprocess.run(
                ["git", "-C", str(Path(repo).resolve()), "show", ACCEPTED_COMMIT+":"+ACCEPTED_PATH],
                stdout=stream, check=True)
    actual = file_record(candidate)
    if actual["sha256"] != ACCEPTED_SHA256 or actual["bytes"] != ACCEPTED_BYTES:
        raise ValueError("The complete original scalar-parameter source has changed")
    return actual


def _execution(repo):
    return dict(
        repository=os.environ["GITHUB_REPOSITORY"],
        run_id=os.environ["GITHUB_RUN_ID"],
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow=os.environ.get("GITHUB_WORKFLOW"),
        workflow_trigger_commit=os.environ.get("GITHUB_SHA"),
        actual_source_commit=subprocess.check_output(
            ["git","-C",str(Path(repo).resolve()),"rev-parse","HEAD"], text=True).strip())


def _construct_inputs(repo, accepted_prefix, outdir, panels, report):
    require_actions()
    import numpy as np
    if panels != PANELS:
        raise ValueError("The first complete deterministic input retains panels=128")
    paths = _source_paths(repo)
    source_records = {role:file_record(path) for role,path in paths.items()}
    source_records["input_constructor"] = file_record(__file__)
    report["source_records"] = copy.deepcopy(source_records)
    accepted = _restore_accepted(repo, accepted_prefix or outdir/"original-accepted099.json.gz")
    report["input_records"] = dict(original_accepted_scalar_parameter_source=accepted)
    raw = Path(accepted["path"]).read_bytes()
    if len(raw) != ACCEPTED_BYTES or hashlib.sha256(raw).hexdigest() != ACCEPTED_SHA256:
        raise ValueError("The captured original scalar input differs")
    original = _read_json_bytes(gzip.decompress(raw))
    parameters = scalar_projection(original)
    del original, raw
    report["complete_scalar_parameters"] = copy.deepcopy(parameters)
    report["complete_scalar_parameters_identity_sha256"] = canonical(parameters)
    scalar_value = dict(analytic_extension_origin=parameters["analytic_extension_origin"],
        fixed_scalar_profile=dict(geometry=copy.deepcopy(parameters["geometry"])))
    scalar_path = outdir/"fixed-scalar-input.json"
    write_json(scalar_path, scalar_value)
    report["outputs"]["scalar_input"] = file_record(scalar_path)

    scalar_module = _load("_complete_fixed_fejer_fullhold", paths["scalar"])
    full = scalar_module.FullHold(scalar_value, paths["integer"], paths["hold"], panels=panels)
    if sha(scalar_module.FullHold.__init__.__code__.co_filename) != SOURCE_PINS["scalar"][1]:
        raise ValueError("The actual complete scalar constructor source changed")
    definitions = exact_node_definitions(parameters)
    fixed = dict(cut=F.from_float(.995), f=F.from_float(.002), hold=F.from_float(.02),
        rise=F.from_float(.02), out=F.from_float(.02))
    if any(getattr(full,key) != value for key,value in fixed.items()):
        raise ValueError("The exact complete FullHold durations no longer match the fixed node recipe")
    scale = full.h.S
    boxes = [full.affine_time(a,b) for a,b in definitions]
    exact_gap_lower = []
    for left,right in zip(definitions, definitions[1:]):
        gap = full.affine_time(right[0]-left[0], right[1]-left[1])
        if gap[0] <= 0:
            raise ArithmeticError("The complete accurate affine mesh order was not established")
        exact_gap_lower.append(F(gap[0],scale))
    mesh_values = []
    mesh_fees = []
    for (a,b), box in zip(definitions,boxes):
        value = round_binary64(b if a == 0 else F(box[0]+box[1],2*scale))
        fee = max(abs(F.from_float(value)-F(box[0],scale)),
                  abs(F.from_float(value)-F(box[1],scale)))
        mesh_values.append(value)
        mesh_fees.append(fee)
    mesh = np.asarray(mesh_values,dtype="<f8")
    if (mesh.shape != (J,) or mesh[0] != 0 or not np.isfinite(mesh).all()
            or not np.all(np.diff(mesh)>0)):
        raise ArithmeticError("The actual complete binary64 mesh is not strictly increasing")
    core_values, chart_evidence = chart_coefficients()
    core = np.asarray(core_values,dtype="<f8")
    radius = round_binary64(F(full.R[0]+full.R[1],2*scale))
    radius_fee = max(abs(F.from_float(radius)-F(full.R[0],scale)),
                     abs(F.from_float(radius)-F(full.R[1],scale)))
    width = round_binary64(F.from_float(.05))
    if radius <= 0 or width <= 0:
        raise ArithmeticError("The complete scalar preparation carriers must remain positive")
    arrays = dict(mesh=mesh, initial_core=core, fixed_core_first3=core[:K].copy(),
        radius=np.asarray(radius,dtype="<f8"), width=np.asarray(width,dtype="<f8"),
        M=np.asarray(M,dtype="<i8"), J=np.asarray(J,dtype="<i8"))
    bundle = outdir/"fixed-reference-input.npz"
    np.savez_compressed(bundle, **arrays)
    report["outputs"]["fixed_input"] = file_record(bundle)
    records = {key:_array_record(value) for key,value in arrays.items()}

    definition = fixed_definition()
    target = mathematical_target_recipe()
    node = dict(
        schema=NODE_SCHEMA, source_sha256=sha(__file__),
        M=M, J=J, exact_core_affine=True,
        complete_scalar_parameters_identity_sha256=SCALAR_PARAMETERS_SHA256,
        fixed_definition_identity_sha256=canonical(definition),
        mathematical_target_identity_sha256=canonical(target),
        chart_recipe=chart_recipe(), chart_parameter_generation=chart_evidence,
        true_scalar_nodes=[dict(S_coefficient=str(a),constant=str(b)) for a,b in definitions],
        exact_node_recipe=node_recipe(),
        exact_scalar_node_definitions_identity_sha256=canonical([[str(a),str(b)] for a,b in definitions]),
        numerical_array_records=records,
        mesh_binary64_hex=[float(v).hex() for v in mesh],
        initial_core_binary64_hex=[float(v).hex() for v in core],
        fixed_core_first3_binary64_hex=[float(v).hex() for v in core[:K]],
        radius_binary64_hex=float(radius).hex(),
        width_binary64_hex=float(width).hex(),
        complete_FullHold_scalar_metadata=full.metadata(),
        mesh_carrier_absolute_error_exact=[str(value) for value in mesh_fees],
        maximum_mesh_carrier_absolute_error_exact=str(max(mesh_fees)),
        minimum_accurate_adjacent_node_gap_lower_exact=str(min(exact_gap_lower)),
        radius_carrier_absolute_error_exact=str(radius_fee),
        radius_role="FullHold preparation endpoint carrier; the downstream complete R690 constructor recomputes its own modified radius",
        full_domain_order_in_accurate_affine_coordinates_verified=True,
        old_warm_selected_core_or_mesh_consumed=False,
        old_same_physical_material_point_claimed=False,
        no_original_field_value_or_geometric_certificate_inherited=True)
    node_path = outdir/"fixed-affine-nodes.json"
    write_json(node_path,node)
    report["outputs"]["node_report"] = file_record(node_path)
    report.update(
        definition=definition, definition_identity_sha256=canonical(definition),
        mathematical_target_recipe=target, mathematical_target_identity_sha256=canonical(target),
        chart_recipe=chart_recipe(), chart_parameter_generation=chart_evidence,
        exact_scalar_node_definitions_identity_sha256=node["exact_scalar_node_definitions_identity_sha256"],
        numerical_array_records=records,
        complete_FullHold_scalar_metadata=full.metadata(),
        M=M,J=J,P=P,N=REFERENCE_N,fixed_K=K,initial_height_generated_here=False,
        original_scalar_parameters_verified=True,
        all_original_scalar_knots_retained=True,
        accurate_entire_radial_domain_retained=True,
        exact_mesh_order_verified=True,
        maximum_mesh_carrier_absolute_error_exact=str(max(mesh_fees)),
        maximum_core_rounding_error_exact=max(
            (row["absolute_rounding_error_exact"] for row in chart_evidence["seven_parameter_roundings"]),
            key=F),
        full_parameter_formula_not_generated_array_used_as_repository_input=True,
        old_chart_words_consumed=False,
        old_nonlinear_field_or_direction_used=False,
        current_free_core_and_height_reduced=False,
        BVP_or_pulse_solver_invoked=False,
        physical_field_evaluations=0,Jacobian_evaluations=0,normal_root_evaluations=0,
        R690_complete_tail_integrated_here=False,
        reference_initial_height_still_requires_complete_R690_constructor=True,
        geometry_or_metric_acceptance_claimed=False,
        old_literal_material_addresses=(
            "Their complete source/provenance remain required; if reused on this new target and new mesh, "
            "explicitly label reinterpretation and do not claim the same physical s or spatial point"),
        unknown_old_parallel_field_or_typed_history_reconstructed=False,
        original_branch_declared_finished=False)
    for role,item in source_records.items():
        if file_record(item["path"]) != item:
            raise ValueError("Complete source changed during input construction: " + role)
    if file_record(accepted["path"]) != accepted:
        raise ValueError("The complete original scalar input changed during construction")
    for role,item in report["outputs"].items():
        if file_record(item["path"]) != item:
            raise ValueError("A complete generated input changed: " + role)
    report["all_input_and_source_output_records_rechecked"] = True
    report["complete"] = True
    return report


def prepare_fixed_input(*, repo, accepted_prefix, outdir, panels=128):
    """Create the three whole stable mathematical files and one actual report."""
    require_actions()
    repo = Path(repo).resolve()
    outdir = Path(outdir).resolve()
    if outdir.exists() and any(outdir.iterdir()):
        raise ValueError("Use one fresh output directory for the complete fixed input")
    outdir.mkdir(parents=True,exist_ok=True)
    report = dict(schema=PREPARATION_SCHEMA,source_sha256=sha(__file__),
        complete=False,status="running",definition=fixed_definition(),
        definition_identity_sha256=canonical(fixed_definition()),
        mathematical_target_recipe=mathematical_target_recipe(),
        mathematical_target_identity_sha256=canonical(mathematical_target_recipe()),
        outputs={},source_records={},input_records={},execution=_execution(repo),
        all_input_and_source_output_records_rechecked=False,
        physical_field_evaluations=0,Jacobian_evaluations=0,normal_root_evaluations=0)
    path = outdir/"report.json"
    write_json(path,report)
    started = time.monotonic()
    try:
        _construct_inputs(repo,accepted_prefix,outdir,panels,report)
        report["status"] = "complete"
        report["seconds"] = time.monotonic()-started
        write_json(path,report)
        return report
    except Exception as exc:
        report.update(complete=False,status="failed",seconds=time.monotonic()-started,
            failure_type=type(exc).__name__,failure_reason=str(exc),
            all_input_and_source_output_records_rechecked=False)
        write_json(path,report)
        raise


def _bound_file(value,name):
    if (not isinstance(value,dict) or set(value)!={"path","bytes","sha256"}
            or not isinstance(value["path"],str) or not Path(value["path"]).is_absolute()
            or type(value["bytes"]) is not int or value["bytes"]<=0
            or not isinstance(value["sha256"],str) or len(value["sha256"])!=64):
        raise ValueError("Complete actual file record required: " + name)
    if file_record(value["path"]) != value:
        raise ValueError("Complete actual input changed: " + name)
    return value


def validate_preparation(value, *, actual_outputs=None):
    """Standard-library actual-file/source contract; no scalar/field/root calls."""
    if (not isinstance(value,dict) or value.get("schema")!=PREPARATION_SCHEMA
            or value.get("source_sha256")!=sha(__file__)
            or value.get("complete") is not True or value.get("status")!="complete"
            or value.get("all_input_and_source_output_records_rechecked") is not True
            or value.get("definition")!=fixed_definition()
            or value.get("definition_identity_sha256")!=canonical(fixed_definition())
            or value.get("mathematical_target_recipe")!=mathematical_target_recipe()
            or value.get("mathematical_target_identity_sha256")!=canonical(mathematical_target_recipe())):
        raise ValueError("Use the actual complete fixed-recipe preparation")
    outputs=value.get("outputs")
    if not isinstance(outputs,dict) or set(outputs)!=set(OUTPUT_ROLES):
        raise ValueError("All three full generated input files are required")
    for role,item in outputs.items():
        _bound_file(item,role)
    if actual_outputs is not None:
        if not isinstance(actual_outputs,dict) or set(actual_outputs)!=set(OUTPUT_ROLES):
            raise ValueError("Caller must provide all three actual inputs")
        for role,given in actual_outputs.items():
            candidate=given["path"] if isinstance(given,dict) else given
            if Path(candidate).resolve()!=Path(outputs[role]["path"]).resolve():
                raise ValueError("Caller selected a different full input "+role)
            if isinstance(given,dict) and given!=outputs[role]:
                raise ValueError("Caller input bytes differ "+role)
    for role,item in value["source_records"].items():
        _bound_file(item,"source "+role)
    if set(value["source_records"])!=set(SOURCE_PINS)|{"input_constructor"}:
        raise ValueError("The complete fixed source closure changed")
    for role,(_,expected) in SOURCE_PINS.items():
        if value["source_records"][role]["sha256"]!=expected:
            raise ValueError("A complete scalar source identity differs "+role)
    if value["source_records"]["input_constructor"]["sha256"]!=sha(__file__):
        raise ValueError("The real input constructor differs")
    original=_bound_file(value["input_records"]["original_accepted_scalar_parameter_source"],
        "original scalar-parameter source")
    if original["sha256"]!=ACCEPTED_SHA256 or original["bytes"]!=ACCEPTED_BYTES:
        raise ValueError("The fixed scalar origin changed")
    scalar=_read_json_bytes(Path(outputs["scalar_input"]["path"]).read_bytes())
    if set(scalar)!={"analytic_extension_origin","fixed_scalar_profile"}:
        raise ValueError("The scalar payload contains nondefining new state")
    if set(scalar["fixed_scalar_profile"])!={"geometry"}:
        raise ValueError("The scalar output must be the complete defining projection")
    parameters=dict(analytic_extension_origin=scalar["analytic_extension_origin"],
        geometry=scalar["fixed_scalar_profile"]["geometry"])
    if (canonical(parameters)!=SCALAR_PARAMETERS_SHA256
            or value.get("complete_scalar_parameters")!=parameters
            or value.get("complete_scalar_parameters_identity_sha256")!=SCALAR_PARAMETERS_SHA256):
        raise ValueError("The complete actual scalar projection differs")
    node=_read_json_bytes(Path(outputs["node_report"]["path"]).read_bytes())
    definitions=exact_node_definitions(parameters)
    words,evidence=chart_coefficients()
    if (node.get("schema")!=NODE_SCHEMA or node.get("source_sha256")!=sha(__file__)
            or node.get("M")!=M or node.get("J")!=J or node.get("exact_core_affine") is not True
            or node.get("chart_recipe")!=chart_recipe()
            or node.get("chart_parameter_generation")!=evidence
            or node.get("initial_core_binary64_hex")!=[v.hex() for v in words]
            or node.get("fixed_core_first3_binary64_hex")!=[v.hex() for v in words[:K]]
            or node.get("true_scalar_nodes")!=[dict(S_coefficient=str(a),constant=str(b)) for a,b in definitions]
            or node.get("fixed_definition_identity_sha256")!=value["definition_identity_sha256"]
            or node.get("mathematical_target_identity_sha256")!=value["mathematical_target_identity_sha256"]
            or node.get("complete_scalar_parameters_identity_sha256")!=SCALAR_PARAMETERS_SHA256
            or node.get("numerical_array_records")!=value.get("numerical_array_records")
            or node.get("exact_node_recipe")!=node_recipe()
            or node.get("exact_scalar_node_definitions_identity_sha256")!=canonical([[str(a),str(b)] for a,b in definitions])
            or value.get("exact_scalar_node_definitions_identity_sha256")!=node.get("exact_scalar_node_definitions_identity_sha256")):
        raise ValueError("The complete deterministic node/chart recipe differs")
    for role,item in outputs.items():
        _bound_file(item,role)
    for role,item in value["source_records"].items():
        _bound_file(item,"source final "+role)
    _bound_file(original,"original scalar-parameter source final")
    return dict(schema=PREPARATION_SCHEMA,source_sha256=sha(__file__),
        definition=copy.deepcopy(value["definition"]),
        definition_identity_sha256=value["definition_identity_sha256"],
        mathematical_target_recipe=copy.deepcopy(value["mathematical_target_recipe"]),
        mathematical_target_identity_sha256=value["mathematical_target_identity_sha256"],
        actual_input_records=copy.deepcopy(outputs),
        original_scalar_parameters_identity_sha256=SCALAR_PARAMETERS_SHA256,
        exact_scalar_node_definitions_identity_sha256=node["exact_scalar_node_definitions_identity_sha256"],
        chart_recipe=chart_recipe(),complete=True,
        completion_scope="complete source/parameter/actual-file binding only",
        actual_npz_members_revalidated_here=False,
        source_and_parameter_binding_complete=True,
        input_construction_complete=True,physical_field_read_or_certificate_claimed=False,
        old_mathematical_target_or_old_same_physical_points_claimed=False)


def read_preparation(path, *, actual_outputs=None):
    path=Path(path).resolve()
    before=file_record(path)
    value=_read_json_bytes(path.read_bytes())
    checked=validate_preparation(value,actual_outputs=actual_outputs)
    if file_record(path)!=before:
        raise ValueError("The complete preparation report changed during reading")
    checked["actual_preparation_report"]=before
    return value,checked


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--outdir",type=Path,required=True)
    parser.add_argument("--accepted-prefix",type=Path)
    parser.add_argument("--panels",type=int,default=128)
    args=parser.parse_args()
    value=prepare_fixed_input(repo=args.repo,accepted_prefix=args.accepted_prefix,
        outdir=args.outdir,panels=args.panels)
    result=dict(event="fixed_fejer_R690_input_prepared",
        report=file_record(args.outdir/"report.json"),complete=value["complete"],
        definition_identity_sha256=value["definition_identity_sha256"],
        mathematical_target_identity_sha256=value["mathematical_target_identity_sha256"],
        complete_scalar_parameters_identity_sha256=value["complete_scalar_parameters_identity_sha256"],
        M=value["M"],J=value["J"],P=value["P"],N=value["N"],
        source_sha256=value["source_sha256"],outputs=value["outputs"],
        BVP_or_pulse_solver_invoked=False,physical_field_evaluations=0,
        Jacobian_evaluations=0,normal_root_evaluations=0)
    print(json.dumps(result,sort_keys=True),flush=True)


if __name__ == "__main__":
    main()
