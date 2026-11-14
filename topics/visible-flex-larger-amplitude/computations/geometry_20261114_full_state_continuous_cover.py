#!/usr/bin/env python3
"""R241 spatial-cover consumer for an actual complete v3/v4 closed field.

The old v3 pair gates and all their margins are retained verbatim.  Only
the closed-bundle paths and field evaluator change: positions and normals
come directly from the complete SavedPrefix/actual-tail assembly, including
its full mean, the explicitly recorded inlet normal form and the SAME
recorded planar registration.  No old-A mesh, omitted-mean identity, new
fit, interpolation of display points or old geometry bound is substituted.

K, metric, slope, position and normal-error envelopes remain user-supplied
hypotheses.  Passing a numerical cover does not certify those envelopes,
the complete C2 immersion hypotheses, an exact isometry or topic completion.
This numerical entry runs only in this public repository's GitHub Actions.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
import os
from pathlib import Path

for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import numpy as np

from geometry_20261114_large_core_saved_prefix import actions_only, read, sha


HERE = Path(__file__).resolve().parent
GATE_SOURCE = HERE / "geometry_20261114_continuous_cover_budget_v3.py"
EXPECTED_SOURCES = {
    "geometry_20261114_continuous_cover_budget_v3.py":
        "3362fc35c09b98a8feb10706f2b126c9bc45e7d45a4294c928b4b72e59d2c7a1",
    "geometry_20261114_held_hausdorff_cover.py":
        "3ba8a0d02266d2b057862c0741dc0a6f65c1276514adab8e403852d69a55809c",
    "geometry_20261114_large_core_closed_assembly.py":
        "e70d27a92bf153e49e50016706db854b339d96d3414d7f4c00a5993e1f7609c0",
    "exact_20261114_refined_tail_adapter.py":
        "6b06db6c7c96078b9fabe403a0b3ade14f8b30b07a78b565ed299c77f840d937",
}


def check_hash_record(record, key, path, label):
    if record.get(key, {}).get("sha256") != sha(path):
        raise ValueError(label + " differs at " + key)


def same_definition(actual, stored, label):
    if actual != stored:
        keys = sorted(k for k in set(actual) | set(stored)
                      if actual.get(k) != stored.get(k))
        raise ValueError(label + " changed: " + ", ".join(keys))


def install_recorded_registration(saved, stored, angular):
    """Install the mesh's one recorded SE2 when its constructor requests it.

    The mathematical rotation is cos/sin of the stored binary64 angle,
    exactly as declared by the producer.  Its printed matrix is checked,
    not independently fitted or interpreted as another orthogonal matrix.
    """
    angle = float(stored["rotation_angle"])
    translation = np.asarray(stored["prefix_translation_to_subtract"], float)
    printed = np.asarray(stored["prefix_to_native_row_rotation"], float)
    if (not math.isfinite(angle) or translation.shape != (2,)
            or printed.shape != (2, 2) or not np.all(np.isfinite(translation))
            or not np.all(np.isfinite(printed))
            or int(stored["angular_samples"]) != angular):
        raise ValueError("Retain the complete assembly's finite planar registration")
    co, si = np.cos(angle), np.sin(angle)
    rotation = np.array([[co, -si], [si, co]])
    if not np.array_equal(rotation, printed):
        raise ValueError("Recorded rotation matrix differs from its declared angle evaluation")

    def use_recorded(prefix_points, native_points):
        if saved.registration is not None:
            raise ValueError("The single recorded registration has already been installed")
        if np.shape(prefix_points) != (angular, 2) or np.shape(native_points) != (angular, 2):
            raise ValueError("The constructor changed its complete native-cut sample grid")
        saved.rotation_to_native = rotation.copy()
        saved.translation_from_native = translation.copy()
        saved.registration = copy.deepcopy(stored)
        return saved.registration

    previous = saved.set_native_registration
    saved.set_native_registration = use_recorded
    return previous


def load_full_bundle(args):
    """Keep all original complete-tail acceptance/config/source/H bindings."""
    import geometry_20261114_large_core_closed_assembly as assembly_module
    import geometry_20261114_inlet_parity_normal_form as inlet
    from exact_20261114_true_tail_client import (
        DEFAULT_LEDGER, DEFAULT_STORED, REPO, public_asset)

    if not args.basename or Path(args.basename).name != args.basename:
        raise ValueError("--basename must be one file-name component")
    paths = {key: args.directory / (args.basename + suffix) for key, suffix in (
        ("plan", "-plan.json"), ("assembly", "-assembly.json"),
        ("mesh", "-phase0.ply.gz"), ("background", "-heights.json"),
        ("normals", "-normal-samples.npz"))}
    plan, assembly, background = map(read, (paths["plan"], paths["assembly"], paths["background"]))
    if not all(row.get("finished") is True for row in (plan, assembly, background)):
        raise ValueError("A completed plan, actual finite assembly and source background are required")
    check_hash_record(assembly["inputs"], "plan", paths["plan"], "Closed assembly")
    check_hash_record(assembly["inputs"], "heights", paths["background"], "Closed assembly")
    check_hash_record(background["inputs"], "plan", paths["plan"], "Background")
    check_hash_record(background["inputs"], "config", args.config, "Background")
    for key, path in (("checkpoint", args.checkpoint), ("port", args.port),
                      ("config", args.config), ("complete", args.complete),
                      ("actual_response", args.tail_response)):
        check_hash_record(plan["inputs"], key, path, "Closed plan")
    phase0 = [row for row in assembly["files"] if row.get("t") == 0]
    if len(phase0) != 1 or phase0[0]["sha256"] != sha(paths["mesh"]):
        raise ValueError("Use the assembly's exact single phase-zero mesh")
    if assembly["normal_samples"]["sha256"] != sha(paths["normals"]):
        raise ValueError("The complete assembly's normal packet differs")
    if (background["profile_fingerprint"] != plan["profile_fingerprint"]
            or background["cut"] != plan["cut"] or background["cuff"] != plan["cuff"]):
        raise ValueError("The source background and finite plan have different physical anchors")

    definition = assembly["large_core_prefix"]
    same_definition(plan["large_core_prefix"], definition, "Plan/assembly prefix definition")
    normalization = definition.get("inlet_normalization", {"enabled": False})
    if type(normalization.get("enabled")) is not bool:
        raise ValueError("The assembly must explicitly identify its inlet normalization")
    enabled = normalization["enabled"]
    for asset in (DEFAULT_LEDGER, DEFAULT_STORED):
        public_asset(asset.resolve().relative_to(REPO.resolve()), HERE.parent / "notes")

    previous_factory, previous_bundle = assembly_module.LargeCoreSavedPrefix, assembly_module._bundle
    assembly_module.LargeCoreSavedPrefix = lambda checkpoint: inlet.read_saved(checkpoint, normalize=enabled)
    assembly_module._bundle = None
    try:
        saved, tail, config = assembly_module.load_bundle(args)
        actual_binding = copy.deepcopy(assembly_module._bundle[3])
    finally:
        assembly_module.LargeCoreSavedPrefix = previous_factory
        assembly_module._bundle = previous_bundle
    same_definition(saved.definition, definition, "Complete physical/nodal/source definition")
    for key, value in actual_binding.items():
        if assembly["large_core_binding"].get(key) != value:
            raise ValueError("The actual accepted prefix/tail identity changed at " + key)
    if config["modes"] != saved.M or tail.N != config["quadrature"]:
        raise ValueError("Use this complete equal-mode field and its own actual tail")

    registered = copy.deepcopy(assembly["single_global_planar_registration"])
    previous_registration = install_recorded_registration(saved, registered, tail.N)
    previous_last = assembly_module._last_assembly
    try:
        A = assembly_module.LargeCoreAssembly(saved, tail, plan, background, None)
    finally:
        saved.set_native_registration = previous_registration
        assembly_module._last_assembly = previous_last
    if saved.registration != registered:
        raise AssertionError("The reconstructed field changed the recorded global registration")
    actual_mean = dict(prefix_cut_mean=A.prefix_cut_mean, tail_cut_small_mean=A.tail_cut_mean,
        single_upper_offset=A.offset, upper_cap_height=A.cap_height)
    for key, value in actual_mean.items():
        if value != assembly["mean_gauge"][key]:
            raise ValueError("The complete physical mean/gauge differs at " + key)
    if (A.L != plan["prefix_end"] or A.cut != plan["cut"] or A.cuff != plan["cuff"]
            or A.cap_height <= 0):
        raise ValueError("The exact same finite closed-map anchors are required")
    if assembly["core_and_hold_gauge"]["native_cap_rotation_axis_xy"] != [0., 0.]:
        raise ValueError("The existing spatial gates require the declared native cap axis (0,0)")
    bindings = dict(
        complete_checkpoint_sha256=sha(args.checkpoint), config_sha256=sha(args.config),
        actual_tail_response_sha256=sha(args.tail_response), complete_readout_sha256=sha(args.complete),
        original_port_sha256=sha(args.port),
        closed_bundle_sha256={key: sha(path) for key, path in paths.items()},
        actual_field_modes=saved.M, actual_tail_modes=config["modes"],
        actual_tail_angular=tail.N, complete_prefix_definition=copy.deepcopy(definition),
        inlet_normalization=copy.deepcopy(normalization),
        recorded_single_global_planar_registration=registered,
        same_recorded_registration_installed_without_new_fit=True,
        complete_mean_gauge=actual_mean, complete_z0_retained=True,
        actual_native_tail_and_full_cut_correction_retained=True,
        numerical_intermediate_tail_nodes_recomputed=False,
        original_numerical_sources_checked=actual_binding["verified_original_numerical_sources"],
        actual_complete_binding=actual_binding,
        all_source_envelopes_inherited=False, continuous_envelopes_certified=False,
        geometric_acceptance_created=False)
    return paths, plan, assembly, background, saved, A, bindings


def finite_points_normals(jets, kind, count, angular):
    points = np.asarray(jets["pos"], float)
    if points.shape != (count, angular, 3) or not np.all(np.isfinite(points)):
        raise ValueError("The complete field returned invalid positions")
    # Match the original assembly's conventions, including the inward tail.
    left, right = ("p1", "s1") if kind == "prefix" else ("s1", "p1")
    normals = np.cross(jets[left], jets[right])
    lengths = np.linalg.norm(normals, axis=2)
    if not np.all(np.isfinite(lengths)) or np.any(lengths <= 0):
        raise ValueError("The actual complete field is not regular at a queried center")
    return points, normals / lengths[:, :, None]


def direct_centers(args, A, descriptors, angles, N, stored_points):
    """Every active center is a direct evaluation in the recorded gauge."""
    theta = 2 * math.pi * angles / N
    cache = {}
    inverse = 0.
    for kind in ("prefix", "tail", "collar"):
        coordinates = sorted(set(row["coordinate"] for row in descriptors if row["kind"] == kind))
        for first in range(0, len(coordinates), args.normal_batch):
            at = np.asarray(coordinates[first:first + args.normal_batch])
            if kind == "prefix":
                jets, residual, _ = A.prefix_jets(at, theta)
                inverse = max(inverse, float(residual))
            else:
                jets = A.tail_jets(at, theta)
            points, normals = finite_points_normals(jets, kind, len(at), len(theta))
            for index, coordinate in enumerate(at):
                cache[(kind, float(coordinate))] = points[index], normals[index]
    count = len(descriptors) * len(theta)
    positions, normals = np.empty((count, 3)), np.empty((count, 3))
    discrepancy = {}
    for i, row in enumerate(descriptors):
        sl = slice(i * len(theta), (i + 1) * len(theta))
        positions[sl], normals[sl] = cache[(row["kind"], row["coordinate"])]
        positions[sl, 2] *= row["side"]
        normals[sl, 2] *= row["side"]
        gap = float(np.max(np.linalg.norm(positions[sl] - stored_points[sl], axis=1)))
        discrepancy[row["kind"]] = max(discrepancy.get(row["kind"], 0.), gap)
    return positions, dict(normals=normals, maximum_chart_inverse_residual=inverse,
        maximum_direct_center_mesh_difference=max(discrepancy.values()),
        direct_center_mesh_difference_by_piece=discrepancy)


def direct_normals_and_children(args, A, paths, descriptors, angles, N, points,
                               center_data, child_angles, ntheta, subdivision,
                               child_points, child_normals, child_position_error):
    normals = np.zeros_like(points)
    available = np.zeros(len(points), dtype=bool)
    info = dict(enabled=not args.disable_normal_cones,
        active_centers=len(center_data["normals"]), prefix_centers=0,
        maximum_chart_inverse_residual=center_data["maximum_chart_inverse_residual"],
        maximum_direct_center_mesh_difference=center_data["maximum_direct_center_mesh_difference"],
        direct_center_mesh_difference_by_piece=center_data["direct_center_mesh_difference_by_piece"],
        checked_existing_normals=0, maximum_existing_angle_difference=None,
        normal_packet_sha256=sha(paths["normals"]), angular_subdivision=subdivision,
        child_position_error=child_position_error,
        child_error_rule="The original conservative 3*position_error allowance is retained; each new position is now one direct complete-field evaluation.",
        complete_z0_and_recorded_single_SE2_used=True,
        display_positions_interpolated=False, omitted_mean_difference_identity_used=False,
        definition="Direct complete material-quintic/actual-tail six jets in the assembly's recorded global SE2; prefix and tail/collar centers, plus direct prefix angular children.")
    if not args.disable_normal_cones:
        normals[:-2] = center_data["normals"]
        available[:-2] = True
        coordinates = sorted(set(row["coordinate"] for row in descriptors if row["kind"] == "prefix"))
        children = {}
        for first in range(0, len(coordinates), args.normal_batch):
            at = np.asarray(coordinates[first:first + args.normal_batch])
            jets, residual, _ = A.prefix_jets(at, child_angles)
            info["maximum_chart_inverse_residual"] = max(info["maximum_chart_inverse_residual"], float(residual))
            positions, child_n = finite_points_normals(jets, "prefix", len(at), len(child_angles))
            for index, coordinate in enumerate(at):
                children[float(coordinate)] = (positions[index].reshape(ntheta, subdivision, 3),
                                               child_n[index].reshape(ntheta, subdivision, 3))
        for i, row in enumerate(descriptors):
            if row["kind"] != "prefix":
                continue
            sl = slice(i * ntheta, (i + 1) * ntheta)
            child_points[sl], child_normals[sl] = children[row["coordinate"]]
            child_points[sl, :, 2] *= row["side"]
            child_normals[sl, :, 2] *= row["side"]
            info["prefix_centers"] += ntheta
        with np.load(paths["normals"], allow_pickle=False) as packet:
            indices = packet["moving_source_indices"]
            old_normals = packet["moving_normal"]
        if indices.shape != (len(old_normals),) or old_normals.shape[1:] != (3,):
            raise ValueError("The assembly's moving normal packet has inconsistent dimensions")
        stored = {int(index): value for index, value in zip(indices, old_normals)}
        checked, counts = [], {}
        for i, row in enumerate(descriptors):
            for j, angle_index in enumerate(angles):
                index = int(row["source_ring"] * N + angle_index)
                if index not in stored:
                    continue
                value = stored[index]
                length = float(np.linalg.norm(value))
                if not math.isfinite(length) or length <= 0:
                    raise ValueError("A stored assembly normal is not finite and nonzero")
                value = value / length
                candidate = normals[i * ntheta + j]
                angle = math.atan2(float(np.linalg.norm(np.cross(candidate, value))),
                                   abs(float(np.dot(candidate, value))))
                checked.append(angle)
                counts[row["kind"]] = counts.get(row["kind"], 0) + 1
        if not checked:
            raise ValueError("No common actual-field normal is available for the bound packet check")
        info.update(checked_existing_normals=len(checked), checked_existing_normals_by_piece=counts,
                    maximum_existing_angle_difference=max(checked))
    normals[-2:] = [[0., 0., -1.], [0., 0., 1.]]
    available[-2:] = True
    return normals, available, info


def position_writer(paths, bindings):
    """Use the unchanged position-cover writer with this explicit bundle."""
    import geometry_20261114_held_hausdorff_cover as held

    def write(path, **kwargs):
        previous = held.bundle_paths
        held.bundle_paths = lambda directory: (paths["plan"], paths["assembly"], paths["mesh"])
        try:
            result = held.write_position_cover(path, **kwargs)
        finally:
            held.bundle_paths = previous
        result["complete_field_binding"] = bindings
        result["direct_complete_field_centers"] = True
        result["source_vertex_indices_role"] = (
            "Identifiers of corresponding material queries in the bound phase-zero mesh; "
            "the centers themselves are direct evaluations of the complete recorded field.")
        result["closed_bundle_files"] = {key: value.name for key, value in paths.items()}
        Path(path).write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
        return result

    return write


def replace_once(source, old, new):
    if source.count(old) != 1:
        raise ValueError("The frozen v3 source adapter anchor changed: " + old[:100])
    return source.replace(old, new)


def between_once(source, first, last, replacement):
    if source.count(first) != 1 or source.count(last) != 1:
        raise ValueError("The frozen v3 source block anchors changed")
    start, end = source.index(first), source.index(last)
    if end <= start:
        raise ValueError("The frozen v3 source block order changed")
    return source[:start] + replacement + source[end:]


def build_program(source):
    """Replace inputs/evaluation/provenance; preserve all spatial gate code."""
    first = source.index('"""')
    last = source.index('"""', first + 3) + 3
    source = source[:first] + '"""R241 cover of the actual complete v3/v4 finite closed field.\n\nDirect complete positions/normals, full mean, explicitly recorded inlet\nnormalization and the same recorded global SE2; original pair gates and\nmargins. All continuous error and geometry envelopes remain hypotheses.\n"""' + source[last:]
    source = replace_once(source, "    args = parser.parse_args()", """    parser.add_argument('--basename', default='surface')
    for key in ('config','tail-response','complete'):
        parser.add_argument('--'+key, type=Path, required=True)
    args = parser.parse_args()""")
    source = between_once(source,
        "    plan_path = args.directory/'refined-A-closed-plan.json'",
        "    N, upper = plan['angular'], plan['upper_rings']", """    paths, plan, assembly, background, saved, A, field_binding = load_full_bundle(args)
    plan_path, assembly_path, mesh_path, background_path = (paths[key] for key in ('plan','assembly','mesh','background'))
""")
    source = replace_once(source,
        "    points = rings[indices][:,angles].reshape(-1,3)", """    stored_center_points = rings[indices][:,angles].reshape(-1,3)
    points, center_data = direct_centers(args,A,descriptors,angles,N,stored_center_points)""")
    source = between_once(source, "    # F(s,new)=F(s,0)+G(s,new)-G(s,0)",
        "    # For p in cell i, the tangent projector differs", """    # Keep the original conservative child error margin.  The field is now
    # evaluated directly with its full mean and fixed recorded registration.
    child_position_error=3*position_error
    child_enclosure=child_h+child_position_error
    child_cone_sine=np.sin(np.minimum(math.pi/2,K*child_h+args.normal_angle_error))
    normal_vectors,normal_available,normal_info=direct_normals_and_children(
        args,A,paths,descriptors,angles,N,points,center_data,child_angles,ntheta,
        subdivision,child_points,child_normals,child_position_error)
""")
    source = replace_once(source,
        "and normal_info['maximum_same_radius_position_reconstruction_error'] <= 3*position_error)))",
        "))\n                         and normal_info['maximum_direct_center_mesh_difference'] <= 3*position_error)")
    source = replace_once(source,
        "schema='R37-R241-prefix-child-spatial-cover-budget-v3'",
        "schema='R37-R241-complete-full-state-spatial-cover-budget-v1'")
    source = replace_once(source,
        "input_sha256={str(p):sha(p) for p in (plan_path,assembly_path,mesh_path,background_path,args.checkpoint,args.port)},",
        "input_sha256={str(p):sha(p) for p in (plan_path,assembly_path,mesh_path,background_path,paths['normals'],args.checkpoint,args.port,args.config,args.tail_response,args.complete)},")
    source = replace_once(source,
        "new_points='True SavedPrefix/PPoly material-angle evaluations at the same radial nodes; original mean preserved by F(s,new)=F(s,0)+G(s,new)-G(s,0), with 3*position_error paid.',",
        "new_points='Direct complete SavedPrefix material-angle positions in the same recorded SE2, including full z0 and the assembly-declared inlet normal form; the conservative original 3*position_error margin is retained.',")
    source = replace_once(source,
        "'Child positions use an exact same-radius difference identity, not mesh interpolation; all three numerical expression evaluations require the supplied position-error bound.',",
        "'Every active center and prefix child is evaluated directly from the complete finite field in the same recorded gauge. Agreement with mesh samples does not prove the position or normal-error envelopes.',")
    source = replace_once(source,
        "    args.out.parent.mkdir(parents=True,exist_ok=True)\n    from geometry_20261114_held_hausdorff_cover import write_position_cover", """    result['complete_field_binding']=field_binding
    result['unchanged_spatial_gate_sources']=EXPECTED_SOURCES
    result['transformed_gate_program_sha256']=TRANSFORMED_PROGRAM_SHA256
    result['center_definition']='Direct complete-field positions, including full mean and the assembly-declared inlet normal form, in the same recorded SE2; no new fit or mesh interpolation.'
    result['closed_C2_inlet_normalization_enabled']=field_binding['inlet_normalization']['enabled']
    args.out.parent.mkdir(parents=True,exist_ok=True)
    write_position_cover=position_writer(paths,field_binding)""")
    return source


def main():
    actions_only()
    for name, digest in EXPECTED_SOURCES.items():
        if sha(HERE / name) != digest:
            raise ValueError("An original mathematical/input-writer source changed: " + name)
    program = build_program(GATE_SOURCE.read_text())
    namespace = dict(__name__="_complete_full_state_cover_v1", __file__=str(Path(__file__).resolve()),
        load_full_bundle=load_full_bundle, direct_centers=direct_centers,
        direct_normals_and_children=direct_normals_and_children,
        position_writer=position_writer, EXPECTED_SOURCES=EXPECTED_SOURCES,
        TRANSFORMED_PROGRAM_SHA256=hashlib.sha256(program.encode()).hexdigest())
    exec(compile(program, str(GATE_SOURCE) + "::<complete-field-input-adapter>", "exec"), namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()
