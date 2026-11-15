#!/usr/bin/env python3
"""Explicit frozen-nine450 v2 dispatch for complete physical/closed readout.

This is an adapter to the existing SavedPrefix and seven-member bundle APIs.
It does not relabel a nine-control scalar as v3/v4, alter a producer, solve a
BVP or native tail, or manufacture an accepted parent. It retains the whole
physical/core/mean/material/cut field and the original actual-tail checks.
The old shared Hermite background and geometry kernels remain separate from
the original target metric. Continuous nine-control scalar/metric envelopes
are NOT supplied by this dispatcher; the old ScalarExpression is not reused
as a proof for this different scalar identity.

Numerical work is public-Actions-only. CLI output belongs in RUNNER_TEMP.
All temporary module dispatch is scoped and restored, including on failure.
Use this adapter in one synchronous call at a time, not beside a concurrent
legacy consumer in the same Python interpreter.
"""
from __future__ import annotations

import argparse
import copy
from contextlib import contextmanager
from fractions import Fraction as Q
import importlib
import json
import os
from pathlib import Path
import sys
import time
from types import SimpleNamespace

import geometry_20261115_nine_control_same_metric_saved_prefix as prefix

HERE = Path(__file__).resolve().parent
SCHEMA = "frozen-nine450-complete-field-dispatch-v1"
SHARED_SCHEMA = "frozen-nine450-shared-background-closed-geometry-v1"
LOADER_NAME = "geometry_20261115_nine_control_shared_closed_dispatch.load_shared_bundle"
SOURCE_PINS = {
    "geometry_20261115_nine_control_same_metric_saved_prefix.py": "e8deb4136dbaf021d2648e02a2cdb774db4ebe1836b239b609472c596fc70404",
    "geometry_20261114_inlet_parity_normal_form.py": "ce5f287c1de870b6bf71d1650d6942e23fd2bdd23a25af72ec5b637599a97410",
    "geometry_20261114_lifted_modes_readout.py": "d2d539559ab39638ca90c82f278353b73e1101c62ab73c2feb5353990f58a902",
    "geometry_20261114_large_core_closed_assembly.py": "e70d27a92bf153e49e50016706db854b339d96d3414d7f4c00a5993e1f7609c0",
    "geometry_20261114_lifted_modes_closed_assembly.py": "e5cf3eadb093fb741a8a610a09042a15f1869c79b2b4fc30f02c3de0635d2179",
    "geometry_20261114_full_state_continuous_cover.py": "c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6",
    "geometry_20261114_shared_background_normal_form.py": "da4a0b5004ef8466119025d8e39e23ffb0366a5367e6761c8321299aeb19c3f9",
    "geometry_20261114_shared_background_closed_assembly.py": "ac635c11aa31925a4175876ffa2c8b959766629aebf9e3abaf97a68ca0e096cb",
    "exact_20261114_refined_closed_assembly.py": "1fec55a9d9f6c2a9211e64036226496bb4e4ae42c641c842e863e8c4f34fcccc",
    "exact_20261114_refined_tail_adapter.py": "6b06db6c7c96078b9fabe403a0b3ade14f8b30b07a78b565ed299c77f840d937",
    "exact_20261114_closed_display_adapter.py": "d2cbff19a71eca9122475432a40bb6b4f809f696b4cb43e08b307d00f1897dd8",
    "exact_20261114_true_tail_client.py": "1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09",
    "geometry_20261114_full_dn_boundary.py": "4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2",
    'exact_20261114_resolved_radial_readout.mjs': 'd72f5a67ca8af8af77f4ea86c14b062bda43e09b1946bf43f430a594ac7bc757',
    'exact_20261114_closed_background.mjs': 'be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b',
    'exact_20261114_tail_capacity_loader.mjs': '07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395',
    'tail_frozen_geometry.mjs': 'db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3',
    'strong_frozen_calibration_factory.mjs': '77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247',
    'closure_bounded_point_cache.mjs': '35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043',
}
read, sha, actions_only = prefix.read, prefix.sha, prefix.actions_only
_RUNTIME = None
_ACTIVE = None


def checked_sources():
    sources = prefix.checked_sources()
    for name, expected in SOURCE_PINS.items():
        if sha(HERE/name) != expected or (name in sources and sources[name] != expected):
            raise ValueError("A complete field/geometry dispatch source differs: "+name)
        sources[name] = expected
    sources[Path(__file__).name] = sha(__file__)
    return sources


def runtime():
    global _RUNTIME
    actions_only()
    checked_sources()
    if _RUNTIME is None:
        modules = dict(
            inlet="geometry_20261114_inlet_parity_normal_form",
            lifted="geometry_20261114_lifted_modes_closed_assembly",
            large="geometry_20261114_large_core_closed_assembly",
            full="geometry_20261114_full_state_continuous_cover",
            background="geometry_20261114_shared_background_normal_form",
            shared="geometry_20261114_shared_background_closed_assembly")
        d = SimpleNamespace(**{key: importlib.import_module(name) for key, name in modules.items()})
        d.original_load = d.large.load_bundle
        d.original_first_cell_scalar_lower = d.inlet.first_cell_scalar_lower
        d.original_annotate = d.inlet._annotate_output
        d.original_full_load = d.full.load_full_bundle
        d.original_checked_background = d.shared.checked_background
        d.original_guard_for = d.shared.guard_for
        d.original_shared_annotate = d.shared.annotate_output
        _RUNTIME = d
    return _RUNTIME


def field_identity(saved):
    if not isinstance(saved, prefix.NineControlSameMetricSavedPrefix):
        raise TypeError("Only the explicit complete frozen-nine450 reader belongs to this dispatch")
    return dict(schema=SCHEMA, dispatcher_sha256=sha(__file__),
        saved_prefix_sha256=sha(prefix.__file__),
        scalar_profile_source_sha256=prefix.SOURCE_PINS[prefix.PROFILE_NAME],
        accepted_field_producer_sha256=prefix.SOURCE_PINS[prefix.ENTRY_NAME],
        actual450_file=copy.deepcopy(saved.mode_identity["accepted_field_file"]),
        canonical_scalar_identity_sha256=saved.profile_model.canonical_scalar_identity_sha256,
        complete_scalar_specification_sha256=prefix.canonical_sha(saved.profile_model.specification),
        parameter_order=prefix.PARAMETER_ORDER,
        frozen_nine_float64le=copy.deepcopy(saved.mode_identity["frozen_nine_float64le"]),
        scalar_support_float64le=copy.deepcopy(saved.mode_identity["scalar_support_float64le"]),
        origin_design_field=copy.deepcopy(saved.mode_identity["origin_design_field"]),
        no_legacy_v3_v4_relabel=True, complete_z0_retained=True,
        complete_core112_and_physical338_retained=True,
        native_acceptance_created=False, continuous_envelopes_inherited=False)


def read_saved(checkpoint, normalize=True):
    d = runtime()
    saved = prefix.NineControlSameMetricSavedPrefix(checkpoint)
    return d.inlet.normalize_inlet(saved) if normalize else saved


def first_cell_scalar_lower(saved):
    """Apply the unchanged base-quintic lemma only where ALL nine vanish."""
    d = runtime()
    identity = field_identity(saved)
    specification = saved.profile_model.specification
    original_three = specification["frozen_design_scalar_profile"]["original_three_parameter_specification"]
    bumps = saved.profile_model.designed_nine.bumps
    if len(bumps) != 9:
        raise ValueError("All nine support intervals are required for the original first-cell lemma")
    end = Q(float(saved.sol.x[1]))
    if any(Q(float(bump.left)) < end for bump in bumps):
        return dict(available=False,
            reason="A complete nine-control support meets the first physical cell; the old base-only lemma is not applied",
            frozen_nine450_field=identity,
            all_nine_control_supports_tested=True,
            general_nine_scalar_continuous_bound_created=False), None
    # This is only the genuine old base-polynomial theorem's argument view.
    # No accepted checkpoint/schema/profile is edited or presented as legacy.
    view = SimpleNamespace(sol=saved.sol,
        rec={"fixed_scalar_profile": {"geometry": original_three}})
    record, lower = d.original_first_cell_scalar_lower(view)
    record = copy.deepcopy(record)
    record.update(frozen_nine450_field=identity,
        original_three_base_specification_sha256=prefix.canonical_sha(original_three),
        all_nine_control_supports_tested=True,
        all_nine_control_supports_start_at_or_after_first_cell_end=True,
        actual450_checkpoint_or_scalar_schema_changed=False,
        original_base_only_Bernstein_formula_unchanged=True,
        general_nine_scalar_continuous_bound_created=False)
    return record, lower


def update_bundle_identity(binding, saved):
    binding.update(independent_field_modes=copy.deepcopy(saved.mode_identity),
        field_representation=copy.deepcopy(saved.rec["field_representation"]),
        independent_modes_closed_adapter_sha256=sha(__file__),
        independent_modes_saved_prefix_sha256=sha(prefix.__file__),
        independent_modes_scalar_profile_sha256=prefix.SOURCE_PINS[prefix.PROFILE_NAME],
        unchanged_independent_modes_closed_kernel_sha256=SOURCE_PINS["geometry_20261114_lifted_modes_closed_assembly.py"],
        frozen_nine450_field=field_identity(saved))


def load_actual_tail_bundle(args):
    """The original full tail/source/config/H/J/cut checks run before metadata."""
    d = runtime()
    saved, tail, config = d.original_load(args)
    if int(config["modes"]) != saved.M or saved.mode_identity["actual_tail_modes"] != saved.M:
        raise ValueError("The accepted complete field requires its own equal-mode actual tail")
    update_bundle_identity(d.large._bundle[3], saved)
    return saved, tail, config


def annotate_output(data, saved, consumer_file):
    d = runtime()
    d.original_annotate(data, saved, consumer_file)
    data.update(complete_field_dispatch=field_identity(saved),
        complete_field_dispatch_source_sha256=sha(__file__),
        actual_saved_prefix_constructor_sha256=sha(prefix.__file__),
        complete_state_adapter_sha256=sha(prefix.__file__),
        unchanged_complete_state_jet_kernel_sha256=prefix.SOURCE_PINS["geometry_20261114_large_core_saved_prefix.py"],
        independent_modes_saved_prefix_sha256=sha(prefix.__file__),
        independent_modes_scalar_profile_sha256=prefix.SOURCE_PINS[prefix.PROFILE_NAME],
        independent_modes_closed_adapter_sha256=sha(__file__),
        unchanged_independent_modes_closed_kernel_sha256=SOURCE_PINS["geometry_20261114_lifted_modes_closed_assembly.py"])
    if "large_core_binding" in data:
        update_bundle_identity(data["large_core_binding"], saved)
    if "display_sampling" in data:
        data["display_sampling"].update(
            full_material_readout_entry=Path(__file__).name+" readout",
            unchanged_full_material_readout_kernel_sha256=SOURCE_PINS["geometry_20261114_lifted_modes_readout.py"])


def _load_full_bundle(args):
    d = runtime()
    bundle = d.original_full_load(args)
    paths, plan, assembly, table, saved, A, binding = bundle
    expected = field_identity(saved)
    for name, record in (("plan", plan), ("assembly", assembly)):
        if record.get("complete_field_dispatch") != expected:
            raise ValueError("The "+name+" must bind this explicit frozen-nine450 field/dispatcher")
    # The original Node background table is deliberately unedited. Its exact
    # plan/config hashes, profile fingerprint and cut/cuff are already checked
    # by the original loader; it does not invent Python dispatcher metadata.
    if assembly.get("independent_modes_scalar_profile_sha256") != prefix.SOURCE_PINS[prefix.PROFILE_NAME]:
        raise ValueError("Do not retain a legacy scalar source label on this complete nine-control field")
    binding.update(frozen_nine450_field=expected,
        complete_geometry_dispatch_sources=checked_sources(),
        actual_scalar_continuous_interval_adapter_paid=False,
        old_ScalarExpression_relabelled_as_nine_control=False)
    return paths, plan, assembly, table, saved, A, binding


def checked_source_bundle(args):
    d = runtime()
    d.shared.check_sources()
    bundle = _load_full_bundle(d.shared.source_arguments(args))
    if (d.shared.GUARD_KEY in bundle[1]["large_core_prefix"]
            or "shared_background_geometry" in bundle[2]):
        raise ValueError("Start from this actual unwrapped complete bundle, not recursive postprocessing")
    return bundle


def checked_background(bundle, descriptor_path):
    d = runtime()
    record, B, geometry = d.original_checked_background(bundle, descriptor_path)
    saved = bundle[4]
    geometry.update(schema=SHARED_SCHEMA,
        unchanged_shared_background_kernel_sha256=geometry["wrapper_sha256"],
        wrapper_sha256=sha(__file__), frozen_nine450_field=field_identity(saved),
        explicit_dispatch_sources=checked_sources(),
        required_geometry_loader=LOADER_NAME,
        all_nine_scalar_coefficients_and_original_finite_paths_retained=True,
        old_v3_v4_scalar_identity_reused=False,
        original_nine_target_metric_not_replaced_by_Bprime=True,
        complete_continuous_nine_scalar_metric_envelope_certified=False)
    return record, B, geometry


def guard_for(geometry):
    d = runtime()
    guard = d.original_guard_for(geometry)
    guard.update(schema=SHARED_SCHEMA, required_geometry_loader=LOADER_NAME,
        frozen_nine450_field=copy.deepcopy(geometry["frozen_nine450_field"]),
        unchanged_shared_background_kernel_sha256=SOURCE_PINS["geometry_20261114_shared_background_closed_assembly.py"],
        old_ScalarExpression_authorized_for_current_nine_scalar=False)
    return guard


def shared_annotate_output(data, source_assembly, geometry, A):
    d = runtime()
    d.original_shared_annotate(data, source_assembly, geometry, A)
    # The frozen shared writer retains the true numerical kernels. Its guard
    # and this additional identity name the new explicit loader and scalar.
    data["complete_field_dispatch"] = field_identity(A.saved)
    data["complete_field_dispatch_source_sha256"] = sha(__file__)
    data["complete_state_adapter_sha256"] = sha(prefix.__file__)
    data["unchanged_complete_state_jet_kernel_sha256"] = prefix.SOURCE_PINS["geometry_20261114_large_core_saved_prefix.py"]


@contextmanager
def dispatch_scope():
    """Preserve unrelated legacy calls; no source text is rewritten/executed."""
    global _ACTIVE
    d = runtime()
    if _ACTIVE is not None:
        yield d
        return
    saved_attributes = []
    argv = sys.argv
    def replace(obj, key, value):
        saved_attributes.append((obj, key, getattr(obj, key)))
        setattr(obj, key, value)
    _ACTIVE = d
    try:
        replace(d.inlet, "read_saved", read_saved)
        replace(d.inlet, "first_cell_scalar_lower", first_cell_scalar_lower)
        replace(d.inlet, "_annotate_output", annotate_output)
        replace(d.lifted, "LiftedModesSavedPrefix", read_saved)
        replace(d.lifted, "load_bundle", load_actual_tail_bundle)
        for name in ("install_consumer",):
            replace(d.lifted, name, getattr(d.lifted, name))
        replace(d.large, "LargeCoreSavedPrefix", read_saved)
        replace(d.large, "load_bundle", load_actual_tail_bundle)
        replace(d.large, "install_consumer", d.large.install_consumer)
        replace(d.large, "_bundle", None)
        replace(d.large, "_last_assembly", None)
        replace(d.shared, "checked_source_bundle", checked_source_bundle)
        replace(d.shared, "checked_background", checked_background)
        replace(d.shared, "guard_for", guard_for)
        replace(d.shared, "annotate_output", shared_annotate_output)
        yield d
    finally:
        for obj, key, value in reversed(saved_attributes):
            setattr(obj, key, value)
        sys.argv = argv
        _ACTIVE = None


def load_full_bundle(args):
    """Original seven-tuple API for this explicitly bound original closed field."""
    with dispatch_scope():
        return _load_full_bundle(args)


def load_shared_bundle(args):
    """Seven-tuple API for its explicitly bound shared-B closed field."""
    with dispatch_scope() as d:
        bundle = d.shared.load_shared_bundle(args)
        geometry = bundle[2]["shared_background_geometry"]
        if (geometry.get("schema") != SHARED_SCHEMA
                or geometry.get("wrapper_sha256") != sha(__file__)
                or geometry.get("required_geometry_loader") != LOADER_NAME):
            raise ValueError("This field requires its actual frozen-nine450 shared loader")
        bundle[6].update(actual_complete_nine_scalar_bound=True,
            continuous_nine_scalar_interval_envelope_certified=False,
            old_ScalarExpression_relabelled_as_nine_control=False)
        return bundle


def temporary_output(path):
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve()
    output = Path(path).resolve()
    if temporary not in output.parents:
        raise ValueError("Recomputable output must remain below RUNNER_TEMP, not Git/Release")
    return output


def require_fresh_output(arguments, flag):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(flag, type=Path, required=True)
    args, _ = parser.parse_known_args(arguments)
    output = temporary_output(getattr(args, flag[2:].replace("-", "_")))
    if flag == "--out" and output.exists():
        raise FileExistsError("Use a fresh temporary output file")
    return output


def prepare_background(arguments):
    d = runtime()
    parser = argparse.ArgumentParser(description="Same complete background preparer, explicitly bound to frozen-nine450")
    for name in ("directory", "checkpoint", "port", "config", "tail-response", "complete", "source-topic", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--basename", default="surface")
    args = parser.parse_args(arguments)
    temporary_output(args.out)
    if args.out.exists():
        raise FileExistsError("Keep original evidence; use a fresh temporary descriptor")
    started = time.monotonic()
    bundle = _load_full_bundle(args)
    report = d.background.prepare_from_bundle(*bundle)
    report.update(scientific_execution_repository=os.environ["GITHUB_REPOSITORY"],
        scientific_execution_commit=os.environ["GITHUB_SHA"],
        elapsed_seconds=time.monotonic()-started,
        complete_field_dispatch=field_identity(bundle[4]),
        complete_field_dispatch_source_sha256=sha(__file__))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    d.background.write(args.out, report)
    print(json.dumps(dict(event="frozen-nine450-shared-background-defined", output=str(args.out),
        nodes=len(report["exact_background"]["nodes"]),
        exact_endpoint_identities=report["exact_background"]["exact_endpoint_identities_checked"],
        full_cut_correction_still_to_be_installed=True, actual_geometric_acceptance=False)), flush=True)


def main():
    actions_only()
    actions = ("prefix", "audit", "readout", "closed", "background", "shared-render")
    if len(sys.argv) < 2 or sys.argv[1] not in actions:
        raise SystemExit("Use prefix/audit/readout --out; closed all|plan|render --out-prefix; background --out; shared-render --out-prefix")
    action, arguments = sys.argv[1], sys.argv[2:]
    require_fresh_output(arguments, "--out-prefix" if action in ("closed", "shared-render") else "--out")
    with dispatch_scope() as d:
        if action == "prefix":
            sys.argv = [prefix.__file__, *arguments]
            return prefix.main()
        if action == "audit":
            return d.inlet.audit(arguments)
        if action == "readout":
            return d.inlet.delegated_readout(arguments)
        if action == "closed":
            return d.inlet.delegated_closed(arguments)
        if action == "background":
            return prepare_background(arguments)
        sys.argv = [d.shared.__file__, "render", *arguments]
        return d.shared.main()


if __name__ == "__main__":
    main()
