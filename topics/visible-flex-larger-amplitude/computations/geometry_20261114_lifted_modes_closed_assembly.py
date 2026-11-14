#!/usr/bin/env python3
"""Original actual-tail closed consumer for accepted independent-mode fields.

Only the v3 scalar/full-state reader and provenance dispatch are adapted.
Every actual-tail hash, full H/DN block, one SE(2), complete z0 mean and
continuous nine-jet cut correction is retained.  No historical A tail or
height primitive is substituted.  The default small display mesh is kept
separate from the field's actual Fourier and quadrature resolutions.
"""
from __future__ import annotations

import json
import math
import os
from pathlib import Path
import sys

for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import numpy as np

import geometry_20261114_large_core_closed_assembly as original
from geometry_20261114_lifted_modes_saved_prefix import (
    LiftedModesSavedPrefix, actions_only, sha)


HERE = Path(__file__).resolve().parent
_original_load = original.load_bundle
_original_install = original.install_consumer


def display_plan(consumer, args):
    """Original finite rings, retaining every saved physical/scalar node.

    The original planner's 64-angle floor is a display choice.  This entry
    permits 48/32 when the real byte/ring count requires it; no finite field
    coefficient, physical node, tail input or geometry rule is discarded.
    """
    saved, tail, config = load_bundle(args)
    cut, inner = float(tail.r[-1]), float(tail.r[0])
    cuff = config["rCut"]-config["width"]
    if not 0 < args.cut_correction_width < cut-inner:
        raise ValueError("Outer correction must fit inside the actual finite tail")
    s = np.unique(np.r_[0., np.linspace(0, saved.flow.end, args.prefix_intervals+1),
                        saved.flow.breaks, saved.sol.x, saved.flow.end])
    if np.any(s < 0) or np.any(s > saved.flow.end):
        raise ValueError("A saved scalar/physical node lies outside the complete prefix")
    cell_edges = [row["geometry"]["r"] for row in tail.meta["rows"]
                  if row.get("rawSegment") == 0 and row.get("x") == 0]
    r = consumer.anchors(np.r_[np.linspace(inner, cut, args.tail_intervals+1),
                              cell_edges, cut-args.cut_correction_width], inner, cut)
    collar = np.linspace(cuff, inner, args.collar_intervals+1)
    k = args.marker_k
    if k <= 0:
        raise ValueError("Positive weak-marker scale required")
    centers = [[cuff/2, 0.], [0., cuff/2], [-cuff/2, 0.], [0., 0.]]
    markers = [dict(index=i, upper=i < 4, center=centers[i-1], radius=cuff/(8*i),
                    kappa=i*i*k, height=k*cuff*cuff/512) for i in range(1, 5)]
    marker_radii = []
    for row in markers:
        center = np.linalg.norm(row["center"])
        marker_radii.extend([center, center+row["radius"]/2, center+row["radius"]])
        if center:
            marker_radii.extend([center-row["radius"]/2, center-row["radius"]])
    cap = consumer.anchors(np.r_[np.linspace(0, cuff, args.cap_intervals+1), marker_radii], 0, cuff)
    upper = [dict(kind="prefix", coordinate=float(v)) for v in s]
    upper[-1]["cut"] = True
    upper += [dict(kind="tail", coordinate=float(v)) for v in r[-2::-1]]
    upper += [dict(kind="collar", coordinate=float(v)) for v in collar[-2::-1]]
    upper[-1]["cuff"] = True
    upper += [dict(kind="cap", coordinate=float(v)) for v in cap[-2:0:-1]]
    rings = 2*len(upper)-1
    requested = int(args.angular)
    divisor = 4*(args.phase_samples-1)
    candidates = list(dict.fromkeys([requested, *[n for n in (64, 48, 32) if n <= requested]]))
    tried, selected = [], None
    for angular in candidates:
        if angular < 32 or angular % divisor:
            continue
        vertices, faces = rings*angular+2, 2*rings*angular
        bound = 25*vertices+13*faces+4096
        tried.append(dict(angular=angular, vertices=vertices, faces=faces, binary_PLY_byte_bound=bound))
        if selected is None and bound < 5_000_000:
            selected = tried[-1]
    if selected is None:
        raise ValueError("No permitted display angle count fits the actual complete rings below 5 MB: "+json.dumps(tried))
    args.angular = selected["angular"]
    paths = dict(checkpoint=args.checkpoint, port=args.port, config=args.config, complete=args.complete)
    result = dict(schema="refined-tail-finite-closed-plan-v1", finished=True,
        source_sha256_at_start=sha(__file__),
        adapter_sha256=sha(HERE/"exact_20261114_refined_tail_adapter.py"),
        inputs={key:dict(file=str(path.resolve()), sha256=sha(path)) for key,path in paths.items()},
        source_revision="869436630c99aa5a68afb55bd8877c826034d117",
        profile_fingerprint=tail.meta["original_profile_fingerprint"],
        cut=cut, cuff=cuff, tail_inner=inner, prefix_end=saved.flow.end,
        cut_correction_width=args.cut_correction_width, upper_rings=upper,
        background_radii=sorted(set(map(float, np.r_[r, collar, cut-args.cut_correction_width]))),
        angular=args.angular, phase_samples=args.phase_samples,
        phase_angles=np.linspace(0, math.pi/2, args.phase_samples).tolist(),
        mesh_phase_indices=[0, (args.phase_samples-1)//2, args.phase_samples-1],
        vertices=selected["vertices"], faces=selected["faces"],
        uncompressed_mesh_byte_bound=selected["binary_PLY_byte_bound"],
        display_budget=dict(requested_angular=requested, considered=tried, selected=selected,
            complete_ring_count=rings, upper_ring_count=len(upper),
            saved_physical_nodes=len(saved.sol.x), saved_scalar_breaks=len(saved.flow.breaks),
            all_physical_C2_nodes_retained=bool(np.all(np.isin(saved.sol.x, s))),
            all_scalar_breaks_retained=bool(np.all(np.isin(saved.flow.breaks, s))),
            physical_state_or_scalar_node_removed=False,
            byte_formula="25*vertices + 13*faces + 4096, unchanged binary PLY consumer"),
        fixed_cap=dict(theorem="R14-arbitrarily-weak-gaussian-cap-markers", marker_k=k, markers=markers,
            conditional="The exact rotational metric has no isolated strict Gaussian maxima on active latitude circles; not asserted for the finite approximate field"),
        piece_labels={"0":"moving prefix, finite tail and nonzero finite collar",
                      "1":"fixed caps outside markers and common cuff", "2":"fixed weak markers"},
        phase_rule="For all real alpha, moving F_alpha(s,theta)=R_alpha F_0(s,theta-alpha); fixed caps are unchanged; alpha=pi*t/2",
        mean_rule="The complete full-state material mean is read analytically; no historical height primitive is added",
        exact_infinite_nonlinear_tail=False, exact_common_metric_limit=False)
    output = Path(str(args.out_prefix)+"-plan.json")
    consumer.write(output, result)
    print(json.dumps(dict(event="independent_modes_display_plan", plan=str(output),
        actual_rings=rings, saved_physical_nodes=len(saved.sol.x), requested_angular=requested,
        selected=selected)), flush=True)


def load_bundle(args):
    saved, tail, config = _original_load(args)
    if int(config["modes"]) != saved.M or saved.mode_identity["actual_tail_modes"] != saved.M:
        raise ValueError("The accepted independent-mode field requires its own complete equal-mode tail")
    original._bundle[3].update(
        independent_field_modes=saved.mode_identity,
        field_representation=saved.rec["field_representation"],
        independent_modes_closed_adapter_sha256=sha(__file__),
        independent_modes_saved_prefix_sha256=sha(HERE/"geometry_20261114_lifted_modes_saved_prefix.py"),
        independent_modes_scalar_profile_sha256=sha(HERE/"geometry_20261114_lifted_modes_profile.py"))
    return saved, tail, config


def install_consumer(args):
    args.source_hash = sha(__file__)
    if args.action == "render" and args.plan is not None:
        stored_plan = original.read(args.plan)
        args.angular = int(stored_plan["angular"])
        args.phase_samples = int(stored_plan["phase_samples"])
    consumer = _original_install(args)
    previous_write = consumer.write

    def write(path, data):
        if isinstance(data, dict):
            saved = original._bundle[0]
            data["independent_field_modes"] = saved.mode_identity
            data["field_representation"] = saved.rec["field_representation"]
            data["independent_modes_closed_adapter_sha256"] = sha(__file__)
            data["independent_modes_saved_prefix_sha256"] = sha(HERE/"geometry_20261114_lifted_modes_saved_prefix.py")
            data["display_sampling"] = dict(angular=args.angular,
                prefix_intervals=args.prefix_intervals, tail_intervals=args.tail_intervals,
                collar_intervals=args.collar_intervals, cap_intervals=args.cap_intervals,
                all_actual_scalar_breaks_retained=True,
                purpose="Meshes and the explicitly labeled existing finite geometry samples",
                field_frequency_changed=False, substitutes_for_continuous_geometry_check=False,
                full_material_readout_entry="geometry_20261114_lifted_modes_readout.py")
            if "sampled_piece_jets" in data:
                pieces = data["sampled_piece_jets"]
                data["whole_closed_metric_samples"] = dict(
                    component_max=max(row["metric_component_max"] for row in pieces.values()),
                    relative_operator_max=max(row["metric_relative_operator_max"] for row in pieces.values()),
                    active_pieces=list(pieces),
                    fixed_caps_metric_error=0.,
                    fixed_caps_reference="The actual fixed cap/marker map induces its own time-independent metric; no flat metric is substituted on markers",
                    operator_definition="spectral norm of g0^(-1/2) (Gram-g0) g0^(-1/2); for diagonal g0, (|e+d|+sqrt((e-d)^2+4f^2))/2",
                    continuous_bound=False,
                    full_material_prefix_readout_is_separate=True)
        previous_write(path, data)

    consumer.write = write
    consumer.plan = lambda parsed: display_plan(consumer, parsed)
    return consumer


def main():
    actions_only()
    # The complete scalar has over 400 original knots.  All are preserved by
    # the original plan constructor; modest display counts keep each mesh
    # below the repository's existing 5 MB gate, which is still checked there.
    defaults = {"--angular": "64", "--prefix-intervals": "48",
                "--tail-intervals": "64", "--collar-intervals": "16",
                "--cap-intervals": "24"}
    for flag, value in defaults.items():
        if not any(token == flag or token.startswith(flag+"=") for token in sys.argv[1:]):
            sys.argv.extend([flag, value])
    original.LargeCoreSavedPrefix = LiftedModesSavedPrefix
    original.load_bundle = load_bundle
    original.install_consumer = install_consumer
    original._bundle = None
    original._last_assembly = None
    # The original closed driver passes these two absolute constants to the
    # public asset helper, whose public interface requires repository-relative
    # paths. Adapt only those named inputs; keep all bytes/hash gates and all
    # other path validation in the original helper unchanged.
    import exact_20261114_true_tail_client as native_client
    public_asset = native_client.public_asset
    permitted = {native_client.DEFAULT_LEDGER.resolve(), native_client.DEFAULT_STORED.resolve()}
    def known_public_asset(relative, directory):
        candidate = Path(relative)
        if candidate.is_absolute():
            if candidate.resolve() not in permitted:
                raise ValueError("Only the two original frozen calibration assets may use absolute paths here")
            relative = candidate.resolve().relative_to(native_client.REPO.resolve())
        return public_asset(relative, directory)
    native_client.public_asset = known_public_asset
    try:
        original.main()
    finally:
        native_client.public_asset = public_asset


if __name__ == "__main__":
    main()
