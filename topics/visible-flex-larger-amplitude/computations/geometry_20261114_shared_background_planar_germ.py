#!/usr/bin/env python3
"""Bind the unchanged R258/R254 witnesses to the actual shared-B closed field.

The same-radius angular differences remove a common B and its cut Hermite
correction exactly.  The existing exact proof kernels can therefore consume
the same full native Fourier nodes and complete prefix jets.  This adapter
changes only the actual geometry loader, explicit prefix-metadata view and
optional held-report schema.  It does not assert renderer/error transfer,
global embedding, all remaining C2 seams, or a positive actual delta_E.
"""
from __future__ import annotations

import copy
import hashlib
import inspect
import json
from pathlib import Path

import geometry_20261114_full_state_planar_germ as original
import geometry_20261114_shared_background_closed_assembly as geometry


HERE = Path(__file__).resolve().parent
SCHEMA = "R258-actual-shared-background-planar-germ-inputs-v1"
EXPECTED_SOURCES = {
    "geometry_20261114_full_state_planar_germ.py":
        "6ac3997b756c9c8ec49e6526983d530cb3f92656f555b3da88ca584f6e3bfc62",
    "geometry_20261114_prefix_exact_nonplanarity.py":
        "a40dc7a50d90694006342ec964f18fac90bb2743ad622e1b715d920d376c1aa6",
    "geometry_20261114_planar_germ_coefficients.py":
        "a8403ae178916d9b88f4f74b6dc126fa5a5939d412ed86b9587e1343bd856360",
    "geometry_20261114_cardinal_tail_exact_check.py":
        "1d33b952d539ae9fbbff6807f8b61c73fc65c1b85bb9514fe3d29fc0f507af8e",
    "geometry_20261114_shared_background_normal_form.py":
        "da4a0b5004ef8466119025d8e39e23ffb0366a5367e6761c8321299aeb19c3f9",
    "geometry_20261114_shared_background_closed_assembly.py":
        "ac635c11aa31925a4175876ffa2c8b959766629aebf9e3abaf97a68ca0e096cb",
    "geometry_20261114_shared_background_held_hausdorff.py":
        "f9c6466c1a9b8eccde3a5cf83159d2f30f2b2a00b0ab51bf49b83c9b1e698b90",
}
read, sha = original.read, original.sha


def check_sources():
    for name, expected in {**original.FROZEN_SOURCES, **EXPECTED_SOURCES}.items():
        if sha(HERE / name) != expected:
            raise ValueError("An unchanged exact or geometry source differs: " + name)
    geometry.check_sources()


def build_program():
    """Add geometry arguments only; all original proof/return logic remains."""
    baseline = inspect.getsource(original.main)
    before = '    parser.add_argument("--basename", default="surface")'
    after = before + '\n    parser.add_argument("--source-directory", type=Path, required=True)' \
        + '\n    parser.add_argument("--source-basename", default="surface")' \
        + '\n    parser.add_argument("--descriptor", type=Path, required=True)'
    if baseline.count(before) != 1:
        raise ValueError("The frozen R258 CLI insertion anchor changed")
    program = baseline.replace(before, after)
    if program.count(after) != 1 or program.replace(after, before) != baseline:
        raise AssertionError("The original complete R258 main was not exactly recovered")
    return baseline, program


def main():
    original.actions_only()
    check_sources()
    baseline, program = build_program()
    state = {}

    def load_actual_shared(args):
        bundle = geometry.load_shared_bundle(args)
        paths, plan, assembly, reference, saved, A, binding = bundle
        A.assert_unchanged()
        selected = binding["shared_background_geometry"]
        expected = geometry.guarded_definition(saved.definition, selected)
        for label, record in (("plan", plan), ("assembly", assembly)):
            if (record["large_core_prefix"] != expected
                    or record["original_complete_prefix_definition"] != saved.definition):
                raise ValueError("The shared " + label + " changed the original complete prefix")
        guard = expected[geometry.GUARD_KEY]
        if (guard["identity_annotation_only"] is not True
                or guard["prefix_numerical_coefficients_unchanged"] is not True
                or guard["required_geometry_loader"] !=
                "geometry_20261114_shared_background_closed_assembly.load_shared_bundle"):
            raise ValueError("Only the declared shared-background identity annotation may decorate this prefix")
        state.update(args=args, paths=paths, saved=saved, A=A, plan=plan, assembly=assembly,
                     binding=binding, geometry=selected, guard=guard)
        return bundle

    def prefix_views(saved, plan, assembly):
        if (saved is not state["saved"] or plan is not state["plan"]
                or assembly is not state["assembly"]):
            raise ValueError("The exact prefix proof must use the actual new geometry loader's objects")
        # The prefix itself is unchanged by B.  The closed-object guard remains
        # in the real files and complete binding; only a private mathematical
        # prefix view removes its explicitly identity-only annotation after
        # exact validation.  No old loader sees the shared closed bundle.
        views = []
        for record in (plan, assembly):
            view = copy.deepcopy(record)
            definition = copy.deepcopy(view["large_core_prefix"])
            if definition.pop(geometry.GUARD_KEY) != state["guard"] or definition != saved.definition:
                raise ValueError("The mathematical prefix view is not the identical saved finite prefix")
            view["large_core_prefix"] = definition
            views.append(view)
        state["prefix_view_checked"] = True
        return views

    def certify_actual_prefix(saved, *, assembly=None, plan=None, complete_fallback=True):
        view_plan, view_assembly = prefix_views(saved, plan, assembly)
        return original.certify_prefix(saved, assembly=view_assembly, plan=view_plan,
                                       complete_fallback=complete_fallback)

    def use_actual_prefix_report(path, saved, plan, assembly):
        view_plan, view_assembly = prefix_views(saved, plan, assembly)
        return original.use_prefix_report(path, saved, view_plan, view_assembly)

    def optional_actual_held(path, bindings):
        if path is None:
            return dict(provided=False, actual_continuous_image_change_certified=False)
        report = read(path)
        if (report.get("schema") != "actual-complete-shared-background-held-Hausdorff-cover-witness-v1"
                or report.get("adapter_source_sha256") != EXPECTED_SOURCES[
                    "geometry_20261114_shared_background_held_hausdorff.py"]):
            raise ValueError("Use this actual shared-B held consumer, not another finite geometry")
        evidence = report["full_state_input_binding"]
        if (evidence["complete_field_binding"] != bindings
                or evidence["shared_background_descriptor_sha256"] != sha(state["args"].descriptor)
                or evidence["explicit_loader"] !=
                "geometry_20261114_shared_background_closed_assembly.load_shared_bundle"):
            raise ValueError("The held report and this actual shared-B normal form differ")
        return dict(provided=True, report_sha256=sha(path),
            bound_conditional_image_change=report["genuine_image_change_conditionally_established"],
            reported_delta_hold_lower=report["delta_hold_lower"],
            actual_continuous_image_change_certified=False,
            unpaid="The reported continuous envelopes, exact normal-form versus renderer errors, remaining seams and global embedding are not proved by this nonplanarity consumer.")

    namespace = dict(original.__dict__)
    namespace.update(__name__="_shared_background_R258_loader_adapter", __file__=str(Path(__file__).resolve()),
        __doc__=__doc__, SCHEMA=SCHEMA, HERE=HERE,
        FROZEN_SOURCES={**original.FROZEN_SOURCES, **EXPECTED_SOURCES},
        load_full_bundle=load_actual_shared,
        certify_prefix=certify_actual_prefix,
        use_prefix_report=use_actual_prefix_report,
        optional_held=optional_actual_held)
    exec(compile(program, str(HERE / "geometry_20261114_full_state_planar_germ.py") +
                 "::<explicit-shared-background-input-adapter>", "exec"), namespace)
    status = namespace["main"]()
    # Original main writes its actual positive or unresolved result before
    # returning.  Preserve that result and return code; append binding scope.
    args, A = state["args"], state["A"]
    A.assert_unchanged()
    path = Path(args.out) / "summary.json"
    result = read(path)
    if result.get("schema") != SCHEMA or result.get("complete_field_binding") != state["binding"]:
        raise ValueError("The actual exact-proof output lost its complete new-field identity")
    result["shared_background_proof_adapter"] = dict(
        source_sha256=sha(__file__), frozen_sources=EXPECTED_SOURCES,
        original_R258_main_sha256=hashlib.sha256(baseline.encode()).hexdigest(),
        actual_adapter_main_sha256=hashlib.sha256(program.encode()).hexdigest(),
        original_main_exact_source_round_trip_verified=True,
        main_body_changes_only_three_new_geometry_arguments=True,
        explicit_loader="geometry_20261114_shared_background_closed_assembly.load_shared_bundle",
        shared_background_geometry=state["geometry"],
        actual_descriptor_sha256=sha(args.descriptor),
        prefix_metadata_view=dict(identity_only_guard=state["guard"],
            original_actual_files_and_full_binding_unchanged=True,
            exact_identical_prefix_definition_checked=state.get("prefix_view_checked", False),
            actual_shared_nodes_not_changed_or_recomputed_by_this_view=True,
            legacy_geometry_loader_never_substituted=True),
        exact_tail_witness_kernels_unchanged=True,
        fixed_cap_marker_algebra_on_actual_shared_files=True,
        same_radius_cancellation="If F_B=V+B(r)e_z+sum_i h_i(r)[T_i-V_i(c)-B^(i)(c)e_z], then F_B(r,theta)-F_B(r,theta0) equals the identical V/T difference without B and all common B^(i)(c); no surface value or mean is discarded.",
        common_B_real_C2_definition_bound=True,
        original_target_g_replaced_by_Bprime=False,
        tail_renderer_or_exact_nonlinear_limit_proof_created=False,
        all_remaining_seams_C2_or_global_embedding_certified=False,
        previous_rounded_geometry_envelopes_transferred=False,
        all_R238_hypotheses_paid=False,
        actual_delta_E_certified=False)
    result["R238_inputs"]["shared_common_background_real_C2_definition_identified"] = True
    result["R238_inputs"]["same_exact_common_background_mean_and_all_seams_C2_certified"] = False
    result["actual_delta_E_certified"] = False
    result["task_completed"] = False
    path.write_text(json.dumps(result, sort_keys=True, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps(dict(event="shared-background-R258-inputs-completed",
        original_status=status, output=str(path), sha256=sha(path),
        nonplanarity_and_marker_algebra_completed=result["nonplanarity_and_marker_algebra_completed"],
        actual_delta_E_certified=False)), flush=True)
    return status


if __name__ == "__main__":
    raise SystemExit(main())
