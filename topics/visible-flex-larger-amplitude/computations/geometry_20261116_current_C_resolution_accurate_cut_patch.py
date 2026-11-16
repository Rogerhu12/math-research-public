#!/usr/bin/env python3
"""R416 accurate-C cut atlas and independently typed full-angle geometric patch.

The original R409 payload is source data.  This module defines a NEW field
with cut radial jets from the same semantic C/DAG used by the accurate
continuous-ten target.  It never inserts enclosure midpoints as geometry
coefficients and never rewrites the R409 nodes, background or accepted parent.

Only cut_targets is changed in the complete original 675 six-jet engine.
The exact common chart includes all three jets needed by the C2 metric.
R400/R409 input and acceptance responsibilities remain with their original
loaders.  This component is not a new BVP gate or a whole-field certificate.
All mathematical evaluation is public repository Actions only.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R441-current-C-resolution450-accurate-cut-atlas-field-v1"
EXPRESSION_SCHEMA = SCHEMA+"-real-expression"
LOADER_NAME = "geometry_20261116_current_C_resolution_accurate_cut_patch.load_accurate_cut_field"
PROOF_NAME = "R416-current-C-cut-atlas-compatibility-and-accurate-geometric-patch.md"
PROOF_SHA = "3aac8f522649a1375adf937d6be411038aab216e0e2e4bbb71a2cea4816ce7f7"
SHARED_NAME = "geometry_20261116_current_C_ten450_resolution_shared_field.py"
TARGET_NAME = "geometry_20261115_continuous_ten_frozen450_prefix_metric.py"
FACTORY_NAME = "geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py"
ACTIVE_NAME = "geometry_20261115_shared_active_interval_balls.py"
SOURCE_PINS = {
    SHARED_NAME: "1ceda9d32cfcf50e28e737cd0aee981cb8dc2329027aa2967d08532a1ea6e935",
    TARGET_NAME: "011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84",
    FACTORY_NAME: "72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682",
    ACTIVE_NAME: "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b",
}
SUMMARY_LIMIT = 90000


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Accurate field arithmetic is restricted to the named public Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False)+"\n").encode()


def receipt(path, root=None):
    path = Path(path)
    size = 0
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for raw in iter(lambda: stream.read(1048576), b""):
            size += len(raw)
            digest.update(raw)
    return dict(file=str(path.relative_to(root)) if root else path.name,
        bytes=size, sha256=digest.hexdigest())


def identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=sha(raw))


def load(directory, name):
    path = Path(directory)/name
    if receipt(path)["sha256"] != SOURCE_PINS[name]:
        raise ValueError("An actual defining source differs: "+name)
    module_name = "_r416_accurate_cut_"+name[:-3]
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(module_name, None)
        raise
    return module


def write(path, value):
    path = Path(path)
    raw = canonical(value)
    with path.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return receipt(path)


class AccurateCutModel:
    """The exact appended DAG and outward enclosures, never midpoint data.

    Every semantic coefficient is a function of the same three C leaves
    and original total-length expression.  Original accepted ten words,
    natural length, support definitions and chosen-root scope stay bound.
    """
    def __init__(self, target, source_field, Factory, sqrt_bits):
        require_actions()
        if type(sqrt_bits) is not int or sqrt_bits < 1:
            raise ValueError("Use an explicit positive square-root enclosure precision")
        self.target, self.Factory = target, Factory
        self.sqrt_bits = sqrt_bits
        self.original_nodes = copy.deepcopy(target.tree.nodes)
        original_count = len(self.original_nodes)
        roots = target.roots
        required = ("v", "b", "q", "total_length")
        if any(type(roots.get(key)) is not int
                or not 0 <= roots[key] < original_count for key in required):
            raise ValueError("Retain the original canonical cut and natural-length roots")
        if (Q(roots["R"]) != source_field.cut
                or Q(target.definition["cut_radius"]) != source_field.cut
                or target.numeric_length != source_field.x[-1]):
            raise ValueError("Keep the actual original cut and actual numerical length")
        leaf_indices = {}
        for index, node in enumerate(self.original_nodes):
            if node.get("op") == "semantic-cut-leaf":
                name = node["name"]
                if name in leaf_indices:
                    raise ValueError("Do not duplicate a semantic C leaf")
                leaf_indices[name] = index
        if set(leaf_indices) != {"E0", "E1", "E2"}:
            raise ValueError("Use the same complete three-leaf C expression")
        if target.leaves["E0"].lo <= 0 or target.length.lo <= 0:
            raise ArithmeticError("A positive accurate cut/length enclosure remains unpaid")

        tree = Factory.Tree()
        tree.nodes = copy.deepcopy(self.original_nodes)
        # Constants are only an interning optimisation.  Starting a fresh
        # table cannot alter any original node or root.
        Ex = lambda index: Factory.Expression(tree, index)
        E0, E1, E2 = (Ex(leaf_indices[key]) for key in ("E0", "E1", "E2"))
        L = Ex(roots["total_length"])
        k = L/tree.constant(target.numeric_length)
        vc = k*Ex(roots["v"])
        bc = k**2*Ex(roots["b"])
        cc = k**3*Ex(roots["q"])
        sqrtE0 = E0.sqrt()
        m1 = -sqrtE0/k
        m2 = E0/k**2
        m3 = E1/(2*k*sqrtE0)
        self.roots = dict(k=k.index, radial_first=vc.index,
            radial_second=bc.index, radial_third=cc.index,
            target_first_multiplier=m1.index,
            target_second_multiplier=m2.index,
            target_first_in_second_multiplier=m3.index)
        self.tree = tree
        if tree.nodes[:original_count] != self.original_nodes:
            raise AssertionError("The original exact target DAG was modified")
        self.values = tree.evaluate(target.leaves, sqrt_bits)
        self.coefficients = {key:self.values[index] for key,index in self.roots.items()}
        self.original_count = original_count
        self.cut = source_field.cut
        self.numeric_length = target.numeric_length
        self.numeric_v = source_field.v
        self.numeric_b = source_field.acceleration
        self.chart = self.closed_chart_window(source_field)
        self.definition = dict(
            schema=EXPRESSION_SCHEMA+"-cut-coefficients",
            original_target_definition=copy.deepcopy(target.binding["complete_accurate_definition"]),
            complete_current_target_identity=copy.deepcopy(target.binding["complete_target_identity"]),
            complete_original_C_input_binding=copy.deepcopy(
                target.binding["complete_original_C_input_binding"]),
            common_C_root_scope=target.definition["chosen_root_scope"],
            original_expression_node_count=original_count,
            original_expression_nodes_identity=identity(self.original_nodes),
            complete_appended_expression_nodes=copy.deepcopy(tree.nodes),
            original_semantic_leaf_indices=leaf_indices,
            original_total_length_expression_root=roots["total_length"],
            numerical_length_exact=str(target.numeric_length),
            actual_original_cut_exact=str(self.cut),
            original_canonical_cut_roots={key:roots[key] for key in ("v", "b", "q")},
            new_expression_roots=copy.deepcopy(self.roots),
            mathematical_coefficient_definition="same C/DAG real functions, not interval endpoints",
            actual_enclosures={key:value.record() for key,value in self.coefficients.items()},
            actual_original_leaf_enclosures={key:value.record() for key,value in target.leaves.items()},
            sqrt_enclosure_bits=sqrt_bits,
            public_coordinate="u=t/L_numeric=s_true/L_true",
            common_cut_chart="gamma(z)=R+(k*v)*z+(k^2*b)*z^2/2+(k^3*q)*z^3/6",
            cut_target_zero="same complete registered prefix value",
            cut_target_first="(-sqrt(E0)/k)*P_t",
            cut_target_second="(E0/k^2)*P_tt-(E1/(2*k*sqrt(E0)))*P_t",
            closed_common_chart=copy.deepcopy(self.chart),
            no_box_midpoint_or_endpoint_selected_as_accurate_coefficient=True,
            no_independent_per_piece_C_member_selected=True,
            enclosures_are_not_arbitrarily_refinable_real_names=True,
            original_ten_words_and_all_target_pieces_unchanged=True,
            old_R409_numeric_cut_jets_are_source_only=dict(
                r_s=str(self.numeric_v), r_ss=str(self.numeric_b), quadratic_extension_r_sss="0"),
            old_R409_target_atlas_compatibility_asserted=False,
            original_native_trajectory_error_or_whole_metric_bound_certified=False)

    def closed_chart_window(self, field):
        """R416.15 uses rational endpoints; it is not a sampled monotonicity test."""
        F = self.Factory
        k = self.coefficients["k"]
        vc = self.coefficients["radial_first"]
        bc = self.coefficients["radial_second"]
        cc = self.coefficients["radial_third"]
        if k.lo <= 0 or vc.hi >= 0:
            raise ArithmeticError("This enclosure has not resolved a common oriented cut chart")
        original_C = self.target.binding["complete_original_C_input_binding"]
        cuff = F.rational(original_C["physical_parameters"]["rCuff"])
        collar = self.target.pieces[-1]
        if collar["name"] != "canonical-cubic-cut-collar":
            raise ValueError("Retain the actual canonical cut-collar piece")
        collar_width = self.target.values[collar["width"]]
        hP = field.x[-1]-field.x[-2]
        if (collar_width.lo <= 0 or hP <= 0 or not 0 < cuff < field.cut
                or field.width <= 0):
            raise ValueError("The actual cut collar and original inner radial domain differ")
        m = -vc.hi
        B, C, V = bc.absolute_upper(), cc.absolute_upper(), vc.absolute_upper()
        variation = V+B+C+1
        bounds = {
            "unit":Q(1),
            "negative_derivative":m/(4*(B+C+1)),
            "original_patch":field.width/(4*variation),
            "original_C_inner_domain":(field.cut-cuff)/(4*variation),
            "accurate_collar":collar_width.lo/(2*k.hi),
            "last_complete_prefix_cell":hP/2,
        }
        delta = min(bounds.values())
        if delta <= 0:
            raise ArithmeticError("The closed common-chart window remains unpaid")
        return dict(
            exact_positive_delta=str(delta),
            complete_closed_parameter_interval=[str(-delta),str(delta)],
            exact_upper_bound_on_gamma_derivative=str(-3*m/4),
            selected_minimum_candidates={key:str(value) for key,value in bounds.items()},
            source_original_cuff_exact=str(cuff),
            actual_R409_patch_width_exact=str(field.width),
            accurate_collar_width_enclosure=collar_width.record(),
            actual_last_prefix_cell_width_exact=str(hP),
            negative_side_within_accurate_collar_and_last_prefix_cell=True,
            nonnegative_side_within_original_tail_and_same_patch=True,
            original_C_outside_natural_domain_extended=False,
            third_chart_jet_included=True,
            all_same_C_members_in_actual_input_enclosures_retained=True)

    def compact_identity(self):
        return dict(
            schema=EXPRESSION_SCHEMA+"-cut-coefficients",
            complete_definition_identity=identity(self.definition),
            original_expression_node_count=self.original_count,
            appended_node_count=len(self.tree.nodes)-self.original_count,
            roots=copy.deepcopy(self.roots),
            original_numeric_length_exact=str(self.numeric_length),
            actual_original_cut_exact=str(self.cut),
            same_original_C_root_scope=self.target.definition["chosen_root_scope"],
            mathematical_coefficients_not_replaced_by_boxes=True)


def new_exact_field(bundle, Active, Background, model, binding):
    """Keep all raw nodes/B/material structure, replace only the exact patch."""
    require_actions()

    class AccurateCutField(Active.ExactFiniteField):
        def __init__(self):
            super().__init__(bundle, Background)
            self.source_R409_binding = self.binding
            self.binding = binding
            self.accurate_cut_model = model
            self.required_geometry_loader = LOADER_NAME
            # Convert final coefficient enclosures only to multipliers.
            # A wide Arb ball is never reused as a denominator here.
            self.cut_multipliers = {
                name:Active.Jet2.constant(Active.interval(
                    model.coefficients[name].lo, model.coefficients[name].hi))
                for name in ("target_first_multiplier", "target_second_multiplier",
                             "target_first_in_second_multiplier")}

        def cut_targets(self, phi):
            worlds = [self.registered_world(
                tuple(Active.Jet2.constant(Active.exact(value[-1,j]))
                    for j in range(3*self.M+2)),
                phi, translate=(d==0)) for d,value in enumerate(self.nodal)]
            m1 = self.cut_multipliers["target_first_multiplier"]
            m2 = self.cut_multipliers["target_second_multiplier"]
            m3 = self.cut_multipliers["target_first_in_second_multiplier"]
            return (worlds[0],
                tuple(m1*value for value in worlds[1]),
                tuple(m2*worlds[2][j]-m3*worlds[1][j] for j in range(3)))

        def expression_identity(self):
            old = super().expression_identity()
            old_chart = old.pop("cut_chart")
            source_expression_schema = old.pop("schema")
            old.update(
                schema=EXPRESSION_SCHEMA,
                source=receipt(__file__),
                required_geometry_loader=LOADER_NAME,
                source_R409_expression_schema=source_expression_schema,
                source_R409_numeric_cut_chart=old_chart,
                cut_chart=dict(
                    coefficient_expression=model.compact_identity(),
                    actual_closed_chart=copy.deepcopy(model.chart),
                    target_metric_third_chart_jet_is_explicit=True,
                    first_second_geometric_targets_are_same_C_real_functions=True),
                accurate_cut_expression_identity=identity(model.definition),
                actual_target_identity=copy.deepcopy(
                    model.target.binding["complete_target_identity"]),
                same_original_target_and_all10_parameters_retained=True,
                all_raw_radial_and_background_nodes_unchanged=True,
                current_geometry_is_not_old_R409_expression=True,
                source_A_numerical_plot_methods_not_current_geometry=True,
                tail_E_not_replaced_by_one_plus_Bprime_squared=True,
                current_caps_interval_sixjets_or_full_coverage_paid=False,
                old_field_acceptance_or_metric_or_reach_certificate_reused=False,
                original_native_RK_to_accurate_C_error_certified=False)
            return old

    return AccurateCutField()


class AccurateCutBundle:
    """Independent typed handle; intentionally not an old seven-tuple.

    field.evaluate supplies all six jets for complete active closed cells.
    source_bundle is original provenance/data only; calling its numerical A
    renderer would evaluate the old R409 patch, not this new real expression.
    """
    def __init__(self, source_bundle, field, target, model, Active, Background, binding):
        self.source_bundle = source_bundle
        self.field, self.target, self.model = field, target, model
        self.Active, self.Background, self.binding = Active, Background, binding
        self.schema = SCHEMA
        self.required_geometry_loader = LOADER_NAME

    @property
    def pieces(self):
        return self.field.pieces

    def evaluate(self, piece, radial, angular, lower=False):
        require_actions()
        if piece not in self.field.pieces or type(lower) is not bool:
            raise ValueError("Use a complete actual active piece and explicit reflected side")
        if len(radial) != 2 or len(angular) != 2:
            raise ValueError("Use full closed radial and physical-angle intervals")
        r0,r1 = map(self.model.Factory.rational, radial)
        q0,q1 = map(self.model.Factory.rational, angular)
        if not piece["left"] <= r0 <= r1 <= piece["right"] or not 0 <= q0 <= q1 <= 1:
            raise ValueError("The requested closed cell is outside the actual piece")
        return self.field.evaluate(piece, (r0,r1), (q0,q1), lower)

    def expression_identity(self):
        return self.field.expression_identity()


def load_accurate_cut_field(args):
    """Actual R409 binding -> independent accurate-cut full-angle six-jet API.

    Required args: computations, directory, result_sha256, sqrt_bits,
    interval_bits.  Optional: checkpoint_directory, proof_directory.
    No future field, coefficient or root is supplied by this function.
    """
    require_actions()
    if (type(args.sqrt_bits) is not int or args.sqrt_bits < 1
            or type(args.interval_bits) is not int or args.interval_bits < 2):
        raise ValueError("Specify actual interval and rational sqrt working precisions")
    sources = {name:receipt(Path(args.computations)/name) for name in SOURCE_PINS}
    for name, record in sources.items():
        if record["sha256"] != SOURCE_PINS[name]:
            raise ValueError("A complete direct source differs: "+name)
    proof_directory = getattr(args, "proof_directory", None)
    if proof_directory is None:
        proof_directory = Path(args.computations).parent/"results"
    proof = receipt(Path(proof_directory)/PROOF_NAME)
    if proof["sha256"] != PROOF_SHA:
        raise ValueError("Bind the complete actual R416 structural proof")
    Shared = load(args.computations, SHARED_NAME)
    bundle, source_field, Active, Background = Shared.exact_field(args)
    # The original loader retains all R400/450/338+112/means/FD/final/source
    # responsibilities.  No source-only success marker replaces them.
    Factory = load(args.computations, FACTORY_NAME)
    Target = load(args.computations, TARGET_NAME)
    Active.ctx.prec = args.interval_bits
    target = Target.AccurateTenTarget(bundle[4], Factory, args.sqrt_bits)
    model = AccurateCutModel(target, source_field, Factory, args.sqrt_bits)
    current_source = receipt(__file__)
    sources[current_source["file"]] = current_source
    binding = dict(
        schema=SCHEMA+"-binding", source=current_source, sources=sources,
        proof=proof, required_geometry_loader=LOADER_NAME,
        source_R409_result=receipt(Path(args.directory)/"result.json"),
        complete_source_R409_binding_identity=identity(bundle[-1]),
        actual_450_checkpoint=copy.deepcopy(bundle[-1]["actual_450_checkpoint"]),
        current_target_identity=copy.deepcopy(target.binding["complete_target_identity"]),
        complete_target_binding_identity=identity(target.binding),
        accurate_cut_expression_identity=identity(model.definition),
        whole_original_R400_R409_binding_checks_retained=True,
        shared_semantic_C_leaves_and_root_scope_retained=True,
        actual_interval_bits=args.interval_bits, actual_sqrt_bits=args.sqrt_bits,
        source_bundle_and_source_A_are_old_data_not_new_geometry=True,
        current_field_is_independent_R416_expression=True,
        original_BVP_acceptance_replaced=False,
        source_R409_cuff_binding_changed=False,
        full_cap_interval_coverage_paid=False,
        full_relative_metric_or_curvature_or_reach_or_held_paid=False)
    field = new_exact_field(bundle, Active, Background, model, binding)
    return AccurateCutBundle(bundle, field, target, model, Active, Background, binding)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations", type=Path, default=HERE)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--result-sha256", required=True)
    parser.add_argument("--checkpoint-directory", type=Path)
    parser.add_argument("--proof-directory", type=Path)
    parser.add_argument("--sqrt-bits", type=int, required=True)
    parser.add_argument("--interval-bits", type=int, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    require_actions()
    # CLI owns only this fresh output directory, never the old R409 inputs.
    args.out.mkdir(parents=True, exist_ok=False)
    start = time.monotonic()
    try:
        current = load_accurate_cut_field(args)
        expression = write(args.out/"accurate-cut-expression.json", current.model.definition)
        target = write(args.out/"complete-original-target-binding.json", current.target.binding)
        binding = write(args.out/"binding.json", current.binding)
        field_identity = write(args.out/"new-exact-field-identity.json", current.expression_identity())
        result = dict(
            schema=SCHEMA, completed=True,
            completion_scope="definition and bound six-jet API only; no field envelope sweep",
            source=receipt(__file__),
            run_id=os.environ.get("GITHUB_RUN_ID"), source_commit=os.environ.get("GITHUB_SHA"),
            source_R409_result=current.binding["source_R409_result"],
            actual_450_checkpoint=current.binding["actual_450_checkpoint"],
            files=dict(accurate_cut_expression=expression,
                complete_original_target_binding=target, binding=binding,
                new_exact_field_identity=field_identity),
            original_expression_node_count=current.model.original_count,
            appended_expression_node_count=len(current.model.tree.nodes)-current.model.original_count,
            original_complete_active_piece_count=len(current.pieces),
            explicit_closed_cell_evaluations_performed=0,
            all_native_nodes_re_evaluated_in_this_API_call=False,
            full_caps_sixjet_cover_performed=False,
            original_R409_numeric_atlas_compatibility_asserted=False,
            new_field_metric_or_final_geometry_accepted=False,
            pending=[
                "actual closed-cell and whole-cap six-jet/envelope execution",
                "same original target full-domain metric and all original geometry requirements",
                "original native-trajectory and numerical-shadow error responsibilities"],
            error=None, elapsed_seconds=time.monotonic()-start)
        exit_code = 0
    except BaseException as exc:
        result = dict(
            schema=SCHEMA, completed=False, source=receipt(__file__),
            run_id=os.environ.get("GITHUB_RUN_ID"), source_commit=os.environ.get("GITHUB_SHA"),
            completion_scope="binding or expression construction incomplete",
            actual_input_R409_result_sha256=args.result_sha256,
            error=dict(type=type(exc).__name__,message=str(exc)),
            original_BVP_rejected_by_this_component=False,
            pending=["entire independently bound accurate-cut field and all geometric estimates"],
            elapsed_seconds=time.monotonic()-start)
        exit_code = 2
    result_record = write(args.out/"result.json", result)
    summary = dict(schema=SCHEMA+"-necessary-summary",
        result=result_record, completed=result["completed"],
        completion_scope=result["completion_scope"],
        original_input_result_sha256=args.result_sha256,
        error=result["error"],
        pending=result["pending"],
        scientific_or_final_task_success_asserted=False,
        elapsed_seconds=result["elapsed_seconds"])
    if result["completed"]:
        summary.update(files=result["files"],
            original_expression_node_count=result["original_expression_node_count"],
            appended_expression_node_count=result["appended_expression_node_count"],
            original_complete_active_piece_count=result["original_complete_active_piece_count"],
            explicit_closed_cell_evaluations_performed=0)
    raw = canonical(summary)
    if len(raw) > SUMMARY_LIMIT:
        # No splitting/encoding of large scientific payload or silent truncation.
        print(json.dumps(dict(schema=SCHEMA+"-summary-over-budget",
            result=result_record, attempted_bytes=len(raw), attempted_sha256=sha(raw),
            complete_necessary_readback=False, outputs_not_deleted=True)), flush=True)
        return 70
    with (args.out/"necessary-summary.json").open("xb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    print("BEGIN_R416_ACCURATE_C_CUT_ATLAS_SUMMARY", flush=True)
    print(raw.decode(), end="", flush=True)
    print("END_R416_ACCURATE_C_CUT_ATLAS_SUMMARY", flush=True)
    print(json.dumps(dict(event="R416-necessary-summary-identity",
        bytes=len(raw), sha256=sha(raw), source=receipt(__file__))), flush=True)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
