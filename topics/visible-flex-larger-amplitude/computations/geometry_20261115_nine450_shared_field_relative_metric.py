#!/usr/bin/env python3
"""Complete shared-B relative-metric consumer for actual frozen-nine450 v2.

Use the explicit new seven-member loader and the complete original six-jet
field.  The prefix uses all nine frozen controls with the original finite
Gauss real expression.  Optional tail bounds are actual outputs of the R286
convention-C producer, not generic external inequalities or the old finite
selector.  The model-layer choice and natural outer-radius responsibility
remain explicit.  Both closed active sheets, all angular endpoints, and
both original fixed-cap targets are retained.  No native gate is changed.

Scientific imports and arithmetic run only in the named public Actions.
All detailed outputs are request-owned temporary data under rule15.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "frozen-nine450-shared-field-R251-relative-metric-model-C-v1"
MODEL_CHOICE = "R286-convention-C-all-original-exact-root-sequences"
TARGET_DEFINITION = "Declared R286 model C: g_C=E_C(r)dr^2+r^2dtheta^2, uniformly over all original exact deep roots in [1/2,2]"
SOURCE_PINS = {
    "geometry_20261115_nine450_scalar_interval.py": "0c4353d18f1b6b2290cac6907c26a78f04d17909b3a9c83aeac696f29a44f6a0",
    "geometry_20261115_shared_field_relative_metric.py": "a601e5b5dca3c7d87ea7b78a4eb0cebf0b7884d9d4663570f262d6cda578ed17",
    "geometry_20261115_shared_active_interval_balls.py": "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b",
    "geometry_20261115_fixed_cap_rational_balls.py": "a3ada50b5389a075f1da2d2237269a1a1ccc83c29aa35bc889d721eac0e2552e",
    "geometry_20261115_nine_control_shared_closed_dispatch.py": "69bbba2647b2356f2c4023c74a938e29d1b93effcb1c99385fdaa73b78b9d17d",
    "geometry_20261115_stored_continuous_E_cover.py": "9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed",
}


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Scientific arithmetic only in the named public Actions repository")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def receipt(path, root=None):
    digest, size = hashlib.sha256(), 0
    with Path(path).open("rb") as stream:
        for raw in iter(lambda: stream.read(1048576), b""):
            size += len(raw)
            digest.update(raw)
    path = Path(path)
    return dict(file=str(path.relative_to(root)) if root is not None else path.name,
        bytes=size, sha256=digest.hexdigest())


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (str, int, F)):
        raise ValueError("Use exact rational strings or integers for declared bounds")
    return F(value)


def load_module(directory, name):
    require_actions()
    path = Path(directory)/name
    if receipt(path)["sha256"] != SOURCE_PINS[name]:
        raise ValueError("A frozen defining module changed: "+name)
    module_name = name[:-3]
    previous = sys.modules.get(module_name)
    if previous is not None:
        if receipt(previous.__file__)["sha256"] != SOURCE_PINS[name]:
            raise ValueError("Another module with this basename was already imported")
        return previous
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def dyadic_endpoint(row):
    if (not isinstance(row, dict) or not isinstance(row.get("mantissa"), str)
            or type(row.get("binary_exponent")) is not int):
        raise ValueError("Expected an original exact dyadic endpoint record")
    m, e = int(row["mantissa"]), row["binary_exponent"]
    return F(m*(1 << e)) if e >= 0 else F(m, 1 << -e)


def producer_interval(row):
    if not isinstance(row, dict):
        raise ValueError("A completed producer bound is absent")
    lo, hi = dyadic_endpoint(row["lower"]), dyadic_endpoint(row["upper"])
    if lo > hi:
        raise ValueError("Reversed actual producer interval")
    return lo, hi


def bound_member(C, directory, descriptor):
    if not isinstance(descriptor, dict):
        raise ValueError("A required original result descriptor is absent")
    relative = Path(descriptor["file"])
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        raise ValueError("A result member must remain within its actual output directory")
    directory = Path(directory).resolve()
    path = (directory/relative).resolve()
    if not path.is_relative_to(directory):
        raise ValueError("A result member escaped through a symlink")
    value, original = C.read_bound(path, descriptor["sha256"])
    if original["bytes"] != descriptor["bytes"]:
        raise ValueError("An original result member size differs")
    return value, original


def field_tail_identity(field, args, scalar_descriptor):
    return dict(
        complete_field_binding=field.binding,
        exact_field_closed_radial_domain=[str(field.cuff), str(field.cut)],
        configuration=receipt(args.config),
        actual_tail_response=receipt(args.tail_response),
        complete_tail_readout=receipt(args.complete),
        original_reference_table=receipt(field.paths["background"]),
        original_profile_fingerprint=field.table["profile_fingerprint"],
        original_factory_alpha=field.table["original_factory_alpha"],
        original_source_revision=field.table["source_revision"],
        original_target_metric_background_sha256=field.A.shared_background_geometry[
            "original_target_metric_background_sha256"],
        full_prefix_scalar_mathematical_identity_sha256=scalar_descriptor["mathematical_identity_sha256"],
        frozen_v2_scalar_identity_sha256=scalar_descriptor["frozen_v2_scalar_identity_sha256"],
        complete_material_core_coefficients=[str(v) for v in field.core],
        complete_material_density_lower=str(field.rho_lower),
        explicit_requested_model_choice=args.tail_model_choice,
        target_definition=TARGET_DEFINITION,
        model_choice_is_a_declared_real_integral_interpretation=True,
        old_finite_selector_relabelled_as_continuous_target=False,
        target_metric_replaced_by_shared_Bprime=False,
        sampled_reference_rows_used_as_continuous_enclosures=False,
        actual_field_outer_cut_unchanged=True)


class ContinuousModelCTarget:
    """Consume completed query bounds from the actual 9aa0 producer.

    Coarse but rigorous completed queries remain usable when the producer's
    work-resolution goal failed. Unvisited or unproved regions remain unpaid.
    A whole-natural-domain query covers this field only up to the certified
    lower bound of its true R_out; the cut is never rescaled or relabelled.
    """
    def __init__(self, C, field, args, expected_binding):
        require_actions()
        self.rows, self.cuts = [], []
        self.supplied = args.continuous_e_result is not None
        self.identity = expected_binding
        self.receipts = {}
        self.producer_report = self.binding = None
        self.query_status = []
        self.natural_radius = None
        self.conditions_proved = False
        self.domain = (field.cuff, field.cut)
        if not self.supplied:
            return
        if args.tail_model_choice != MODEL_CHOICE:
            raise ValueError("Explicitly choose model C; do not silently reinterpret the old finite target")
        report, self.receipts["result"] = C.read_bound(args.continuous_e_result,
            args.continuous_e_result_sha256)
        directory = args.continuous_e_result.resolve().parent
        if (report.get("schema") != C.SCHEMA
                or report.get("source_sha256") != SOURCE_PINS["geometry_20261115_stored_continuous_E_cover.py"]
                or report.get("repository") != REPOSITORY
                or report.get("target_model_schema") != C.MODEL_SCHEMA
                or report.get("deep_definition") != "original-exact-root-family"
                or report.get("model_choice_is_explicit_and_not_original_finite_output_relabel") is not True
                or report.get("original_finite_output_certified_as_continuous_solution") is not False
                or report.get("R26_numerical_certificate_or_rational_deep_target_used") is not False):
            raise ValueError("This is not the original pinned convention-C producer result")
        binding, self.receipts["input_binding"] = bound_member(C, directory, report["input_binding"])
        plan, self.receipts["query_plan"] = bound_member(C, directory, report["query_plan"])
        queries, self.receipts["query_results"] = bound_member(C, directory, report["query_results"])
        if (binding.get("schema") != C.SCHEMA+"-input-binding"
                or binding.get("source_sha256") != report["source_sha256"]
                or binding["proof"]["sha256"] != C.PROOF_SHA
                or binding["original_source_revision"] != C.REVISION
                or plan.get("schema") != C.QUERY_SCHEMA
                or plan.get("input_binding_sha256") != report["input_binding"]["sha256"]
                or queries.get("schema") != C.SCHEMA+"-queries"):
            raise ValueError("The actual continuous source/queries/proof identity differs")
        if (set(binding["original_sources"]) != set(C.PINS)
                or any(binding["original_sources"][name]["sha256"] != expected
                       for name,expected in C.PINS.items())):
            raise ValueError("A producer original frozen source was substituted")
        convention = binding["convention"]
        if (convention.get("schema") != C.MODEL_SCHEMA
                or convention.get("explicit_model_layer_choice") is not True
                or convention.get("deep_definition") != report["deep_definition"]
                or convention.get("deep_bounds_valid_for_every_original_root_in_half_to_two") is not True
                or convention.get("deep_roots_numerically_selected_or_computed") is not False
                or convention.get("natural_outer_radius_reidentified_as_nominal_cut") is not False
                or convention.get("global_lambda_reselected") is not False):
            raise ValueError("The original exact-root family or natural radial model was changed")
        config, config_receipt = C.read_bound(args.config, receipt(args.config)["sha256"])
        C.compare_geometry(config, binding["physical_parameters"], "Actual450 config/model-C source")
        p = binding["physical_parameters"]
        if (field.cuff != C.rat(p["rCuff"])
                or field.table["profile_fingerprint"] != binding["original_profile_fingerprint"]
                or field.table["source_revision"] != C.REVISION
                or field.plan["source_revision"] != C.REVISION
                or not C.same(field.table["original_factory_alpha"], binding["original_frozen_warp_alpha"])
                or field.table["source_sha256_at_start"] != C.PINS["runtime:exact_20261114_closed_background.mjs"]):
            raise ValueError("The actual shared field has another stored source, cuff or frozen warp coefficient")
        self.receipts["field_config"] = config_receipt
        self.producer_report, self.binding = report, binding
        self.conditions_proved = bool(
            report.get("declared_continuous_model_family_conditions_proved") is True
            and report.get("original_exact_deep_root_existence_proved") is True
            and report.get("all_admissible_original_root_choices_uniformly_enclosed") is True
            and report.get("full_finite_head_complete") is True
            and report.get("complete_original_pieces") == 1440
            and report.get("original_piece_count") == 1440
            and report.get("original_finite_cell_count") == 160
            and report.get("protected_join", {}).get("proved") is True
            and report.get("finite_joins", {}).get("proved") is True
            and convention.get("root_existence_proved") is True)
        if report.get("natural_outer_radius") is not None:
            self.natural_radius = producer_interval(report["natural_outer_radius"])
        requested = plan["queries"]
        if (len(requested) != report["requested_query_count"]
                or len(queries["results"]) != report["returned_query_count"]
                or queries.get("unvisited_query_suffix") != report.get("unvisited_query_suffix")):
            raise ValueError("The complete original query plan or returned prefix differs")
        for index, row in enumerate(queries["results"]):
            q = row["query"]
            if index >= len(requested) or q != requested[index] or q["index"] != index:
                raise ValueError("A returned query was reordered or omitted inside its actual prefix")
            if q.get("left_closed") is not True or q.get("right_closed") is not True:
                raise ValueError("The original query must retain both closed endpoints")
            status = dict(index=index, query=q,
                complete_closed_domain_bound=row.get("complete_closed_domain_bound"),
                domain_containment_proved=row.get("domain_containment_proved"),
                continuous_model_family_conditions_proved=row.get("continuous_model_family_conditions_proved"),
                work_resolution_complete=row.get("work_resolution_complete"),
                budget_or_refinement_stop=row.get("budget_or_refinement_stop"),
                leaf_ledger_rows=row.get("leaf_ledger_rows"), usable=False,
                original_reason=row.get("reason"))
            self.query_status.append(status)
            if not (self.conditions_proved and self.natural_radius is not None
                    and row.get("complete_closed_domain_bound") is True
                    and row.get("domain_containment_proved") is True
                    and row.get("continuous_model_family_conditions_proved") is True):
                continue
            if q["kind"] == "whole-natural-domain":
                left, right = field.cuff, self.natural_radius[0]
            elif q["kind"] == "closed-rational-radius-interval":
                left, right = rational(q["left"]), rational(q["right"])
                if left < field.cuff or right > self.natural_radius[0]:
                    raise ValueError("A supposedly proved closed query exceeds the certified natural domain")
            else:
                raise ValueError("Unsupported actual producer query kind")
            lo, hi = producer_interval(row["E"])
            if hi < 1 or lo > hi:
                raise ValueError("The E=1+w^2 producer bound contradicts its exact analytic range")
            left, right = max(left, field.cuff), min(right, field.cut)
            if left > right:
                status["unused_reason"] = "This actual query does not intersect the field's radial domain"
                continue
            # E_C>=1 follows from the declared exact formula, not a sample.
            self.rows.append(dict(index=index, left=left, right=right,
                lower=max(F(1),lo), upper=hi, raw_E=row["E"],
                query_kind=q["kind"], work_resolution_complete=row["work_resolution_complete"]))
            status.update(usable=True, effective_closed_field_interval=[str(left),str(right)],
                E_lower_used=str(max(F(1),lo)), E_upper_used=str(hi),
                analytic_E_ge_one_intersection=True)
        self.rows.sort(key=lambda row:(row["left"],row["right"],row["index"]))
        self.cuts = sorted(set(x for row in self.rows for x in (row["left"],row["right"])))

    def bounds(self, a, b):
        selected = [row for row in self.rows if row["left"] <= b and a <= row["right"]]
        cursor, started = a, False
        for row in selected:
            if row["left"] > cursor:
                break
            if row["right"] >= cursor:
                cursor, started = max(cursor,row["right"]), True
            if cursor >= b:
                break
        if not started or cursor < b:
            return None
        return (min(row["lower"] for row in selected),
                max(row["upper"] for row in selected), [row["index"] for row in selected])

    def report(self):
        original = self.producer_report or {}
        radius_status = "no_actual_continuous_report"
        if self.natural_radius is not None:
            if self.domain[1] <= self.natural_radius[0]:
                radius_status = "actual_field_cut_at_or_below_proved_natural_Rout_lower"
            elif self.domain[1] > self.natural_radius[1]:
                radius_status = "actual_field_cut_beyond_proved_natural_Rout_upper"
            else:
                radius_status = "actual_field_cut_containment_unresolved_inside_Rout_interval"
        return dict(supplied=self.supplied, actual_result_and_members=self.receipts,
            explicit_model_choice=self.identity["explicit_requested_model_choice"],
            target_definition=TARGET_DEFINITION,
            same_original_config_geometry_fingerprint_and_warp_checked=self.supplied,
            model_family_conditions_proved=self.conditions_proved,
            natural_outer_radius=None if self.natural_radius is None else list(map(str,self.natural_radius)),
            actual_field_radial_domain=list(map(str,self.domain)),
            natural_cut_containment_status=radius_status,
            complete_field_radial_domain_covered=self.bounds(*self.domain) is not None,
            every_returned_query_status=self.query_status,
            actual_unvisited_query_suffix=original.get("unvisited_query_suffix"),
            actual_unvisited_source_piece_suffix=original.get("unvisited_source_piece_suffix"),
            original_complete_ledgers=original.get("ledgers"),
            original_resolution_unpaid_count=original.get("resource_or_unpaid_scope_rows"),
            original_error=original.get("error"),
            original_full_report_flags={key:original.get(key) for key in (
                "all_requested_closed_query_bounds_complete", "numerical_work_resolution_complete",
                "continuous_convention_C_query_enclosures_complete")},
            coarse_complete_query_bounds_used_without_work_goal_gate=True,
            unvisited_or_domain_unproved_queries_used=False,
            original_primitive_or_inverse_ledgers_reexecuted_or_audited_here=False,
            payload_scope="Read actual result, input binding, query plan and complete query-results; other original ledgers remain named by their producer receipts",
            source_pins_or_schema_alone_claimed_as_interval_proof=False,
            theorem_scope="Consume inequalities emitted by pinned9aa0 under its R286 proven model-C contract",
            every_admissible_original_exact_deep_root_sequence_retained=True,
            original_finite_selector_error_certified=False,
            original_continuous_metric_identity_automatically_inherited=False,
            global_C2_field_or_target_seams_proved=False,
            field_cut_or_global_warp_renormalised=False)


def inspect_cell(Kernel, M, field, scalar, tail, spec, eta):
    piece = field.pieces[spec["piece_index"]]
    radial, angular = tuple(map(F,spec["radial"])), tuple(map(F,spec["angular"]))
    kind = piece["kind"]
    target_bounds = None if kind == "prefix" else tail.bounds(*radial)
    if kind != "prefix" and target_bounds is None:
        return dict(certified=False, missing_target_premise=True,
            reason="actual_model_C_query_cover_or_natural_radius_containment_unpaid_on_this_closed_cell",
            actual_closed_radial_cell=list(map(str,radial)),
            original_finite_target_relabelled=False, Bprime_substituted=False)
    values = field.evaluate(piece, radial, angular, spec["lower"])
    X, Y = tuple(v.d[1] for v in values), tuple(v.d[2] for v in values)
    E, B, C = M.dot(X,X), M.dot(X,Y), M.dot(Y,Y)
    theta_q, angular_record = Kernel.angle_density(field,M,angular)
    if kind == "prefix":
        a, scalar_record = Kernel.closed_scalar_range(scalar,M,*radial)
        if M.bounds(a)[0] <= 0:
            return dict(certified=False, reason="complete_nine_scalar_positive_lower_unresolved",
                scalar=scalar_record, scalar_value=M.encode_interval(a), angular=angular_record)
        g11, g22 = M.arb(1), a*a*theta_q*theta_q
        target = dict(kind="complete_frozen_nine_exact_real_scalar", scalar=scalar_record,
            scalar_value=M.encode_interval(a), all_nine_controls_retained=True,
            original_returned_ap_app_used_as_radius_derivatives=False)
    else:
        elo, ehi, rows = target_bounds
        g11 = M.interval(elo,ehi)
        r = M.interval(*radial)
        g22 = r*r*theta_q*theta_q
        target = dict(kind="actual_R286_convention_C_continuous_query_bounds",
            original_query_indices=rows, explicit_model_choice=MODEL_CHOICE,
            target_definition=TARGET_DEFINITION, every_admissible_original_root_sequence=True,
            original_finite_selector_substituted=False, field_cut_unchanged=True)
    result = Kernel.loewner_certificate(M,E,B,C,g11,g22,eta)
    result.update(target=target, angular=angular_record,
        complete_position_and_six_jets={name:[M.encode_interval(v.d[j]) for v in values]
            for j,name in enumerate(M.JET_NAMES)},
        derivatives_of_bound_exact_field=True,
        renderer_jets_used_as_consistent_derivatives=False,
        complete_material_cut_and_zero_mode_mean_retained=True,
        original_four_R251_Loewner_tests_unchanged=True)
    return result


def cap_identity_for_nine450(Kernel, Caps, geometry, field):
    """Same original cap graphs, through the actual new wrapper identity.

    The old cap reader's legacy-wrapper restriction is not bypassed or
    rewritten.  This independent binder retains the complete new guard and
    supplies only the unchanged mathematical cap-target consumer interface.
    """
    plan, assembly, g = field.plan, field.assembly, field.A.shared_background_geometry
    if (plan.get("schema") != Caps.PLAN_SCHEMA or assembly.get("schema") != Caps.ASSEMBLY_SCHEMA
            or plan.get("finished") is not True or assembly.get("finished") is not True
            or g != plan["shared_background_geometry"] or g != assembly["shared_background_geometry"]
            or g.get("schema") != geometry.SHARED_SCHEMA
            or g.get("wrapper_sha256") != SOURCE_PINS["geometry_20261115_nine_control_shared_closed_dispatch.py"]
            or g.get("required_geometry_loader") != geometry.LOADER_NAME
            or g.get("unchanged_shared_background_kernel_sha256") !=
               geometry.SOURCE_PINS["geometry_20261114_shared_background_closed_assembly.py"]
            or g.get("frozen_nine450_field") != geometry.field_identity(field.saved)
            or assembly["inputs"]["plan"]["sha256"] != receipt(field.paths["plan"])["sha256"]
            or g["fixed_cap_definition_sha256"] != Caps.canonical_sha(plan["fixed_cap"])
            or assembly["mean_gauge"]["whole_lower_sheet_reflected"] is not True):
        raise ValueError("The current complete nine450 cap source/guard/definition differs")
    cuff = Caps.exact_stored(plan["cuff"])
    height = Caps.exact_stored(assembly["mean_gauge"]["upper_cap_height"])
    if (cuff <= 0 or cuff != field.cuff
            or height != Caps.exact_stored(g["original_cap_height"])):
        raise ValueError("The actual finite cap height or positive cuff was changed")
    definitions, seen = [], set()
    for row in plan["fixed_cap"]["markers"]:
        key = row["index"]
        if (type(key) is not int or key in seen or type(row["upper"]) is not bool
                or len(row["center"]) != 2):
            raise ValueError("Retain the complete original distinct fixed-cap marker list")
        seen.add(key)
        center = tuple(Caps.exact_stored(x) for x in row["center"])
        radius, amplitude = Caps.exact_stored(row["radius"]), Caps.exact_stored(row["height"])
        if radius <= 0:
            raise ValueError("A genuine marker support radius must be positive")
        definitions.append(dict(index=key,upper=row["upper"],
            center=[Caps.original_number(x) for x in row["center"]],
            radius=Caps.original_number(row["radius"]),height=Caps.original_number(row["height"]),
            actual_graph_amplitude_exact=str(amplitude),
            support_strictly_inside_own_cap=(cuff > radius and
                sum(x*x for x in center) < (cuff-radius)**2),
            stored_normal_kappa_not_used_as_graph_derivative=True))
    binding = dict(plan=receipt(field.paths["plan"]),assembly=receipt(field.paths["assembly"]),
        shared_background_geometry=g,
        fixed_cap_definition_sha256=Caps.canonical_sha(plan["fixed_cap"]),
        cap_height=Caps.original_number(assembly["mean_gauge"]["upper_cap_height"]),
        cuff=Caps.original_number(plan["cuff"]),marker_definitions=definitions,
        actual_frozen_nine450_field_identity=geometry.field_identity(field.saved),
        original_fixed_cap_kernel_source_sha256=SOURCE_PINS["geometry_20261115_fixed_cap_rational_balls.py"],
        independent_current_wrapper_binder_source_sha256=sha(Path(__file__).read_bytes()),
        complete_shared_guard_retained=True,legacy_wrapper_schema_substituted=False,
        definition="(x,y,+/-[H+sum A_j max(0,1-|xy-c_j|^2/R_j^2)^4]) on x^2+y^2<=cuff^2",
        original_target_metric_changed=False,renderer_cap_positions_recomputed=False)

    def current_binding(args):
        if (Path(args.plan).resolve() != field.paths["plan"].resolve()
                or Path(args.assembly).resolve() != field.paths["assembly"].resolve()
                or args.plan_sha256 != binding["plan"]["sha256"]
                or args.assembly_sha256 != binding["assembly"]["sha256"]):
            raise ValueError("The cap-target call names another actual bundle")
        return cuff,height,definitions,binding

    return Kernel.cap_identity(SimpleNamespace(bind_geometry=current_binding),field)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("directory", "source-directory", "descriptor", "checkpoint", "port", "config",
                 "tail-response", "complete", "source-topic", "out"):
        p.add_argument("--"+name, type=Path, required=True)
    p.add_argument("--basename", default="surface")
    p.add_argument("--source-basename", default="surface")
    p.add_argument("--code-directory", type=Path, default=HERE)
    p.add_argument("--scalar-descriptor", type=Path)
    p.add_argument("--scalar-descriptor-sha256")
    p.add_argument("--continuous-e-result", type=Path)
    p.add_argument("--continuous-e-result-sha256")
    p.add_argument("--tail-model-choice", choices=[MODEL_CHOICE])
    p.add_argument("--eta", required=True,
                   help="Explicit requested original R251 relative-operator tolerance, as exact rational text")
    p.add_argument("--precision-bits", type=int, default=192)
    p.add_argument("--initial-angular-depth", type=int, default=3)
    p.add_argument("--max-depth", type=int, default=10)
    p.add_argument("--max-visited-cells", type=int, default=1000000)
    p.add_argument("--budget-seconds", type=int, default=3600)
    args = p.parse_args()
    require_actions()
    if args.out.exists():
        raise FileExistsError("Preserve all previous results")
    for path_key, hash_key in (("scalar_descriptor", "scalar_descriptor_sha256"),
                              ("continuous_e_result", "continuous_e_result_sha256")):
        if (getattr(args,path_key) is None) != (getattr(args,hash_key) is None):
            raise ValueError("An actual optional input and its SHA must be supplied together")
    if args.continuous_e_result is not None and args.tail_model_choice != MODEL_CHOICE:
        raise ValueError("Selecting continuous model C is an explicit target choice")
    eta = rational(args.eta)
    if (not 0 < eta < 1 or not 64 <= args.precision_bits <= 8192
            or not 0 <= args.initial_angular_depth <= 20 or not 0 <= args.max_depth <= 30
            or args.max_visited_cells <= 0 or args.budget_seconds <= 0):
        raise ValueError("Invalid explicit target or resource parameters")
    sys.path.insert(0, str(args.code_directory.resolve()))
    Kernel = load_module(args.code_directory, "geometry_20261115_shared_field_relative_metric.py")
    M = load_module(args.code_directory, "geometry_20261115_shared_active_interval_balls.py")
    unused_legacy_loader, background, _, active_sources = M.initialise_runtime(args.code_directory)
    geometry = load_module(args.code_directory, "geometry_20261115_nine_control_shared_closed_dispatch.py")
    Caps = load_module(args.code_directory, "geometry_20261115_fixed_cap_rational_balls.py")
    Scalar = load_module(args.code_directory, "geometry_20261115_nine450_scalar_interval.py")
    Continuous = load_module(args.code_directory, "geometry_20261115_stored_continuous_E_cover.py")
    scalar_runtime = Scalar.checked_runtime(args.code_directory)
    source_closure = dict(active_sources)
    source_closure.update(scalar_runtime["source_closure"])
    source_closure.update({name:receipt(args.code_directory/name) for name in SOURCE_PINS})
    for name,digest in geometry.checked_sources().items():
        actual = receipt(args.code_directory/name)
        if actual["sha256"] != digest:
            raise ValueError("A complete explicit new-loader dependency differs: "+name)
        source_closure[name] = actual
    # The original field and numerical kernels are reused.  Only the explicit
    # new loader supplies the seven-member bundle; no old guard is stripped.
    roots, split_cell, Journal = Kernel.roots, Kernel.split_cell, Kernel.Journal
    started = time.monotonic()
    old_precision = M.ctx.prec
    args.out.mkdir(parents=True)
    large = args.out/"large-arrays"
    large.mkdir()
    journal = None
    try:
        M.ctx.prec = args.precision_bits+args.max_depth
        bundle = geometry.load_shared_bundle(args)
        field = M.ExactFiniteField(bundle, background)
        specification = field.saved.rec["fixed_scalar_profile"]["geometry"]
        reconstructed = Scalar.export_scalar_descriptor(scalar_runtime, field.saved.profile_model,
            specification, checkpoint_sha256=receipt(args.checkpoint)["sha256"],
            origin="reconstructed-from-checkpoint")
        supplied = supplied_receipt = None
        if args.scalar_descriptor is not None:
            supplied, supplied_receipt = Continuous.read_bound(args.scalar_descriptor,
                args.scalar_descriptor_sha256)
        scalar_binding = Scalar.descriptor_binding(reconstructed,supplied,supplied_receipt)
        scalar = Scalar.ScalarExpression(scalar_runtime,specification,reconstructed)
        if scalar.boundaries["end"] != field.x[-1]:
            raise ValueError("The complete nine scalar and full finite field have different prefix domains")
        tail_binding = field_tail_identity(field,args,reconstructed)
        tail = ContinuousModelCTarget(Continuous,field,args,tail_binding)
        cap = cap_identity_for_nine450(Kernel,Caps,geometry,field)
        cap.update(actual_frozen_nine450_field_identity=geometry.field_identity(field.saved),
            original_fixed_cap_kernel_source_sha256=SOURCE_PINS["geometry_20261115_fixed_cap_rational_balls.py"],
            complete_shared_guard_retained=True)
        (large/"same-scalar-expression.json").write_bytes(canonical(reconstructed))
        (large/"required-original-tail-target-identity.json").write_bytes(canonical(tail_binding))
        (large/"original-fixed-cap-target-identity.json").write_bytes(canonical(cap))
        input_binding = dict(schema=SCHEMA+"-binding", source_sha256=sha(Path(__file__).read_bytes()),
            source_closure=source_closure, complete_field_binding=field.binding,
            shared_background_geometry=field.A.shared_background_geometry,
            actual_plan=receipt(field.paths["plan"]), actual_assembly=receipt(field.paths["assembly"]),
            original_inputs={name:receipt(getattr(args,name)) for name in
                ("descriptor", "checkpoint", "port", "config", "tail_response", "complete")},
            explicit_loader=geometry.LOADER_NAME, new_loader_wrapper_guard_retained=True,
            actual_frozen_nine450_field_identity=geometry.field_identity(field.saved),
            scalar_binding=scalar_binding, continuous_model_C_target=tail.report(),
            original_accepted_parent_required_only_by_original_loader=True,
            postprocessed_field_does_not_inherit_an_exact_isometry_from_native_acceptance=True,
            same_material_theta_and_all_components_preserved=True)
        (large/"input-binding.json").write_bytes(canonical(input_binding))
        planned = Kernel.root_plan(field,scalar,tail,args.initial_angular_depth)
        planned["original_partition_schema"] = planned["schema"]
        planned["schema"] = SCHEMA+"-complete-closed-root-plan"
        planned["original_partition_source_sha256"] = SOURCE_PINS["geometry_20261115_shared_field_relative_metric.py"]
        planned["all_nine_stored_width_support_boundaries_retained"] = True
        planned["actual_model_C_query_cover_boundaries_retained"] = True
        planned_count = planned["planned_roots"]
        (large/"planned-closed-roots.json").write_bytes(canonical(planned))
        journal = Journal(large/"relative-metric-cells.jsonl.gz")
        journal.append(dict(type="identity", input_binding=receipt(large/"input-binding.json",args.out),
            requested_eta_exact=str(eta), planned_roots=receipt(large/"planned-closed-roots.json",args.out),
            complete_closed_caps=receipt(large/"original-fixed-cap-target-identity.json",args.out)))
        visited = terminal = passed = missing = 0
        root_results = []
        resource_stop = execution_error = None
        pending = []
        next_rank = 0
        counters = {name:dict(planned_roots=sum(row["piece_kind"] == name for row in planned["radial_blocks"])
                              *planned["angular_count"],
                              completed_roots=0, certified_roots=0, terminal_cells=0,
                              certified_cells=0, unresolved_cells=0)
                    for name in ("prefix", "collar", "native")}
        for root in roots(planned):
            next_rank = root["rank"]
            stack = [root]
            root_ok = True
            while stack:
                if visited >= args.max_visited_cells or time.monotonic()-started >= args.budget_seconds:
                    resource_stop = "explicit_cell_or_wall_time_budget_before_next_complete_cell"
                    pending = list(reversed(stack))
                    break
                spec = stack.pop()
                visited += 1
                try:
                    report = inspect_cell(Kernel, M, field, scalar, tail, spec, eta)
                except (ArithmeticError, ValueError) as exc:
                    report = dict(certified=False, reason="interval_or_declared_expression_evaluation_unresolved",
                                  exception=dict(type=type(exc).__name__, message=str(exc)))
                except Exception as exc:
                    execution_error = dict(type=type(exc).__name__, message=str(exc), cell=spec)
                    pending = [spec]+list(reversed(stack))
                    break
                if (not report["certified"] and not report.get("missing_target_premise", False)
                        and spec["depth"] < args.max_depth):
                    journal.append(dict(type="subdivided", cell=spec, diagnostic=report))
                    stack.extend(reversed(split_cell(spec)))
                    continue
                journal.append(dict(type="terminal_closed_cell", cell=spec, operator=report))
                terminal += 1
                passed += int(report["certified"])
                missing += int(report.get("missing_target_premise", False))
                stats = counters[spec["piece_kind"]]
                stats["terminal_cells"] += 1
                stats["certified_cells"] += int(report["certified"])
                stats["unresolved_cells"] += int(not report["certified"])
                root_ok = root_ok and report["certified"]
            if resource_stop is not None or execution_error is not None:
                break
            root_results.append(dict(rank=root["rank"], piece_kind=root["piece_kind"],
                                     complete_closed_subdivision=True, certified=root_ok))
            counters[root["piece_kind"]]["completed_roots"] += 1
            counters[root["piece_kind"]]["certified_roots"] += int(root_ok)
            next_rank = root["rank"]+1
            if len(root_results) % 20 == 0:
                print(json.dumps(dict(event="same_field_relative_metric_progress",
                    completed_roots=len(root_results), planned_roots=planned_count,
                    terminal_closed_cells=terminal, certified_cells=passed,
                    actual_model_C_output_supplied=tail.supplied, seconds=time.monotonic()-started),
                    separators=(",", ":")), flush=True)
        complete = len(root_results) == planned_count
        # A partially visited root is represented by its exact remaining DFS
        # cells; all later roots are preserved as a suffix of the immutable plan.
        suffix_start = planned_count if complete else next_rank+1
        pending_record = dict(current_root_rank=None if complete else next_rank,
            remaining_closed_DFS_cells=pending,
            untouched_root_rank_suffix=[suffix_start, planned_count],
            immutable_root_plan=receipt(large/"planned-closed-roots.json",args.out),
            completed_roots=root_results,
            all_unresolved_terminal_cells_remain_in_ledger=True)
        (large/"coverage-and-pending.json").write_bytes(canonical(pending_record))
        journal.append(dict(type="coverage_end", completed=complete,
            coverage=receipt(large/"coverage-and-pending.json",args.out),
            resource_stop=resource_stop, execution_error=execution_error))
        journal.close()
        journal = None
        expression = field.expression_identity()
        expression["original_exact_field_expression_schema"] = expression["schema"]
        expression.update(schema=SCHEMA+"-complete-finite-field-expression",
            original_exact_field_evaluator_source_sha256=SOURCE_PINS["geometry_20261115_shared_active_interval_balls.py"],
            explicit_nine450_loader=geometry.LOADER_NAME,
            shared_wrapper_guard_retained=True,
            actual_frozen_nine450_field_identity=geometry.field_identity(field.saved),
            same_field_material_cut_and_all_six_jets_retained=True,
            legacy_v3_v4_scalar_relabelled=False)
        (large/"same-exact-finite-field-expression.json").write_bytes(canonical(expression))
        prefix_complete = counters["prefix"]["completed_roots"] == counters["prefix"]["planned_roots"]
        prefix_ok = prefix_complete and counters["prefix"]["certified_roots"] == counters["prefix"]["planned_roots"]
        active_ok = complete and all(row["certified"] for row in root_results)
        result = dict(schema=SCHEMA, completed=complete,
            source_sha256=input_binding["source_sha256"], source_closure=source_closure,
            parameters=dict(eta_exact=str(eta), precision_bits=args.precision_bits,
                effective_precision_bits=args.precision_bits+args.max_depth,
                initial_angular_depth=args.initial_angular_depth,max_depth=args.max_depth,
                max_visited_cells=args.max_visited_cells,budget_seconds=args.budget_seconds,
                explicit_tail_model_choice=args.tail_model_choice),
            input_binding=receipt(large/"input-binding.json",args.out),
            expression=receipt(large/"same-exact-finite-field-expression.json",args.out),
            scalar_expression=receipt(large/"same-scalar-expression.json",args.out),
            required_tail_target_identity=receipt(large/"required-original-tail-target-identity.json",args.out),
            fixed_cap_identity=receipt(large/"original-fixed-cap-target-identity.json",args.out),
            complete_cell_ledger=receipt(large/"relative-metric-cells.jsonl.gz",args.out),
            coverage_and_pending=receipt(large/"coverage-and-pending.json",args.out),
            partition=dict(planned_roots=planned_count,completed_roots=len(root_results),
                visited_cells=visited,terminal_closed_cells=terminal,certified_cells=passed,
                unresolved_terminal_cells=terminal-passed,missing_continuous_model_C_target_cells=missing,
                by_piece=counters,both_reflected_sheets_and_all_closed_angle_endpoints=True,
                all_original_field_nine_scalar_and_target_boundaries_split=True,
                unvisited_space_never_discarded=True),
            explicit_actual450_loader=geometry.LOADER_NAME,
            new_shared_guard_retained=True,
            exact_two_original_fixed_cap_operator_error="0",
            complete_nine_prefix_operator_bound_for_declared_real_expression=prefix_ok,
            complete_nine_prefix_operator_bound_with_actual_live_scalar_constants=bool(
                prefix_ok and scalar_binding["actual_live_runtime_constants_verified"]),
            complete_active_operator_bound_for_explicit_declared_model=active_ok,
            whole_closed_chartwise_operator_bound_for_explicit_declared_model=active_ok,
            actual_continuous_model_C_target=tail.report(),
            target_scalar_live_constants_verified=scalar_binding["actual_live_runtime_constants_verified"],
            actual_accepted_field_created=False,
            original_stored_continuous_g_identity_automatically_inherited=False,
            finite_point_batch_and_exact_real_evaluators_identified=False,
            original_48_selector_error_certified=False,
            global_C2_geometry_seams_proved_here=False,
            global_target_metric_interface_compatibility_proved_here=False,
            all_phase_reduction=dict(theorem="R248 section4",sampled_time_grid_used=False,
                conditional_on_actual_C2_and_the_declared_target_metric_atlas_compatibility=True,
                conclusion="On original active material charts, relative errors shift by theta-alpha; original fixed-cap errors are zero",
                finite_phi_band_assumed_for_tail_composition=False,
                actual_complete_closed_family_certificate_paid=False),
            whole_original_g_closed_surface_standard4_certified=False,
            rigorous_pointwise_counterexample_proved=False,
            mathematical_failure_inferred_from_budget_or_interval_failure=False,
            target_replaced_by_Bprime=False,new_metric_fitted=False,
            finite_theta_band_mislabeled_finite_phi_band=False,
            full_mean_or_native_mode_dropped=False,
            ordinary_floating_renderer_error_bound_certified=False,
            original_native_BVP_or_RMS_BC_tolerances_changed=False,
            new_native_acceptance_or_jet_machine_gate_added=False,
            same_g_refinement_sequence_completed=False,reach_held_delta_E_or_task_completed=False,
            resource_stop=resource_stop,execution_error=execution_error,
            elapsed_seconds=time.monotonic()-started)
        raw = canonical(result)
        (args.out/"result.json").write_bytes(raw)
        print(json.dumps(dict(event="frozen-nine450-relative-metric-component",completed=complete,
            source_sha256=result["source_sha256"],result_bytes=len(raw),result_sha256=sha(raw),
            complete_prefix_operator_bound_for_declared_real_expression=prefix_ok,
            whole_closed_chartwise_bound_for_explicit_declared_model=active_ok,
            tail_model_choice=args.tail_model_choice,
            old_finite_selector_certified=False,global_seams_and_standard4_paid=False,
            resource_stop=resource_stop,execution_error=execution_error),separators=(",", ":")),flush=True)
        if execution_error is not None:
            raise SystemExit(1)
    finally:
        if journal is not None:
            journal.close()
        M.ctx.prec = old_precision


if __name__ == "__main__":
    main()
