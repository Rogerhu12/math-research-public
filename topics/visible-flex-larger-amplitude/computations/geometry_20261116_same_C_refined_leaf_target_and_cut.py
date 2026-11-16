#!/usr/bin/env python3
"""R492: read-only same-C leaf evaluation of the actual R400/R416 expressions.

The original checkpoint, accurate definition, all nodal words, background,
material map and ten coefficients remain their original objects.  This
component consumes an actual same-job R489 result and constructs an
independent enclosure view of the SAME exact target and cut-patch functions.
It does not write new coefficients into the saved definition, select a C
member, rerun a BVP, or register itself as an existing metric/reach producer.

The original R416 loader must first return its genuinely bound current field.
The API then supplies target.closed_range and complete active six-jet
evaluate with the new same-semantic leaf intervals.  Tail C(r) queries and
the full closed metric/reach/held traversals are deliberately separate.
All mathematical evaluation is restricted to this public repository Actions.
Author: geometry agent (AI), 2026-11-16.
"""
from __future__ import annotations

import argparse
from collections import OrderedDict
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R492-same-C-refined-leaf-target-and-accurate-cut-evaluation-v1"
BUNDLE_SCHEMA = SCHEMA + "-bundle"
PLAN_SCHEMA = SCHEMA + "-closed-cell-plan"
LIMIT = 90000
PROVIDER_NAME = "geometry_20261116_same_C_full_head_refinement.py"
PROVIDER_SHA = "0ce2f7ab8d1cfc95097ac8089c41ecc1f888343c8432255bd91b1d6cc5d3f8f8"
CUT_NAME = "geometry_20261115_current_C_accurate_cut_patch.py"
CUT_SHA = "28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b"
TARGET_NAME = "geometry_20261115_continuous_ten_frozen450_prefix_metric.py"
TARGET_SHA = "011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84"
FACTORY_NAME = "geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py"
FACTORY_SHA = "72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682"
ACTIVE_NAME = "geometry_20261115_shared_active_interval_balls.py"
ACTIVE_SHA = "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b"
PINS = {PROVIDER_NAME:PROVIDER_SHA, CUT_NAME:CUT_SHA,
        TARGET_NAME:TARGET_SHA, FACTORY_NAME:FACTORY_SHA, ACTIVE_NAME:ACTIVE_SHA}
LEAVES = (("E0", "E"), ("E1", "E_r"), ("E2", "E_rr"))
COEFFICIENTS = ("k", "radial_first", "radial_second", "radial_third",
    "target_first_multiplier", "target_second_multiplier",
    "target_first_in_second_multiplier")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY
        and os.environ.get("GITHUB_RUN_ID") and os.environ.get("GITHUB_SHA"),
        "Execute only in this repository's actual public Actions")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=hashlib.sha256(raw).hexdigest())


def receipt(path, check=None):
    path = Path(path).resolve(strict=True)
    before = path.stat(); h = hashlib.sha256(); size = 0
    with path.open("rb") as stream:
        while raw := stream.read(1048576):
            if check is not None:
                check()
            h.update(raw); size += len(raw)
    after = path.stat()
    require((before.st_dev,before.st_ino,before.st_size,before.st_mtime_ns)
        == (after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns)
        and size == after.st_size, "An actual input changed while being read")
    return dict(file=str(path),bytes=size,sha256=h.hexdigest())


def same(a, b):
    return isinstance(a,dict) and isinstance(b,dict) and all(
        a.get(key) == b.get(key) for key in ("bytes", "sha256"))


def write(path, value):
    raw = canonical(value)
    with Path(path).open("xb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    return receipt(path)


def load(directory, name):
    actions()
    path = (Path(directory)/name).resolve(strict=True)
    require(receipt(path)["sha256"] == PINS[name], "A complete defining source differs: "+name)
    label = "_r492_private_"+name[:-3]+"_"+str(time.monotonic_ns())
    spec = importlib.util.spec_from_file_location(label,path)
    module = importlib.util.module_from_spec(spec); sys.modules[label] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(label,None); raise
    return module


def actual_owner(value, class_name, filename, expected, computations):
    """Use the object's real class owner, not the first module at this path."""
    module = sys.modules.get(type(value).__module__)
    path = None if module is None else getattr(module,"__file__",None)
    require(path is not None and Path(path).resolve() == Path(computations,filename).resolve()
        and receipt(path)["sha256"] == expected
        and getattr(module,class_name,None) is type(value),
        "The actual loaded object is not owned by the complete pinned "+class_name)
    return module


class ResourceStop(RuntimeError):
    pass


class RefinedLeafProvider:
    """Bind genuine R489 and original cut files; recompute their leaf intersection.

    The same complete source result/cut identity must be the one already in
    this target definition.  A merely equal fingerprint or newly relabelled
    checkpoint does not qualify.  All original payloads are read-only.
    """
    def __init__(self, target, *, computations, refinement_directory,
                 refinement_result_sha256, budget_check=None):
        actions()
        self.external_check = budget_check or (lambda:None)
        self.deadline = None
        self.check()
        self.comp = Path(computations).resolve(strict=True)
        require(self.comp == HERE, "Run this independent source from the actual computations HERE")
        self.R = R = load(self.comp,PROVIDER_NAME)
        self.directory = R.inside(refinement_directory,os.environ["RUNNER_TEMP"])
        self.report,self.report_id = R.read(self.directory/"result.json",refinement_result_sha256,self.check)
        report = self.report; R.current(report)
        require(report.get("schema") == R.SCHEMA
            and report.get("source",{}).get("sha256") == PROVIDER_SHA
            and report.get("binding_complete") is True
            and report.get("completed_source_and_cut_recomputation") is True
            and report.get("new_complete_cut_enclosures") is True
            and report.get("same_semantic_C_proved_by_actual_bindings") is True
            and report.get("all_owned_children_quiescent") is True,
            "An actual complete same-C cut recomputation is required, not a partial source claim")
        source_descriptor = report["actual_input"]
        self.input,self.input_id = R.read(source_descriptor["file"],source_descriptor,self.check)
        R.current(self.input)
        require(self.input.get("schema") == R.INPUT_SCHEMA
            and Path(self.input["computations"]).resolve() == self.comp
            and Path(self.input["out"]).resolve() == self.directory,
            "The actual R489 input/HERE/output differs")
        namespace = R.inside(self.input["namespace"],os.environ["RUNNER_TEMP"])
        require(self.directory.is_relative_to(namespace), "Use the actual original same-job namespace")
        launch,lid = R.read(self.input["clock"]["launch_result"]["file"],
            self.input["clock"]["launch_result"],self.check); R.current(launch)
        clock,did = R.read(self.input["clock"]["actual_job_deadline"]["file"],
            self.input["clock"]["actual_job_deadline"],self.check); R.current(clock)
        require(launch.get("schema") == R.LAUNCH_SCHEMA
            and launch.get("source_sha256") == R.LAUNCH_SHA
            and launch.get("driver") == dict(file=R.DRIVER_NAME,sha256=R.DRIVER_SHA)
            and same(lid,report["actual_original_launch"])
            and same(did,launch["actual_job_deadline"])
            and same(did,report["actual_job_deadline"])
            and clock.get("schema") == R.DEADLINE_SCHEMA
            and clock.get("recipe_sha256") == launch.get("recipe",{}).get("sha256")
            and clock.get("science_seconds_from_namespace") == 18900
            and clock.get("readback_reserve_seconds") == 2700,
            "Retain the actual original launch-bound clock and explicit actual202205 origin")
        start = clock.get("namespace_created_unix_seconds")
        require(type(start) in (int,float) and math.isfinite(start), "The original clock has no finite start")
        self.deadline = start+18900
        require(report.get("original_science_deadline_unix_seconds") == self.deadline,
            "The R489 report does not carry the same original absolute deadline")
        self.check()
        self.source_receipts = {name:receipt(self.comp/name,self.check) for name in PINS}
        require(all(self.source_receipts[name]["sha256"] == expected for name,expected in PINS.items()),
            "Retain the complete original scientific and new provider sources")
        old_dir = R.inside(self.input["baseline_C"]["directory"],namespace)
        fresh_dir = self.directory/"refined-C"
        old,oid,ob,obid = R.checked_C(old_dir,self.input["baseline_C"]["result_sha256"])
        fresh,fid,fb,fbid = R.checked_C(fresh_dir,report["actual_refined_C"])
        oc,ocid = R.checked_cut(self.input["baseline_cut"]["file"],self.input["baseline_cut"],oid,obid)
        nc,ncid = R.checked_cut(self.directory/"refined-cut"/"cut-twojet-readout.json",
            report["actual_refined_cut"],fid,fbid)
        require(oc.get("point_twojet_enclosure_complete") is True
            and nc.get("point_twojet_enclosure_complete") is True,
            "A loaded actual target and its refined evaluation need both complete original cut hulls")
        equality = R.semantic_bindings(ob,fb)
        require(canonical(equality) == canonical(report["semantic_input_equivalence"]),
            "Re-read complete semantic equality differs from the actual R489 result")
        baseline = report["baseline"]
        require(same(baseline["C_result"],oid) and same(baseline["C_input_binding"],obid)
            and same(baseline["cut_readout"],ocid), "An actual baseline payload was substituted")
        tail = target.definition["continuous_tail"]
        require(same(tail["actual_result"],oid)
            and same(tail["actual_complete_cut_twojet_readout"],ocid)
            and canonical(tail["actual_input_binding"]) == canonical(ob)
            and tail.get("source_sha256") == R.C_SHA
            and tail.get("actual_cut_twojet_readout_source_sha256") == R.CUT_SHA,
            "R489 must refine this exact actual definition's original C and full cut reader")
        require(canonical(oc["original_binary_cut"]) == canonical(nc["original_binary_cut"])
            and canonical(tail["original_binary_cut"]) == canonical(oc["original_binary_cut"])
            and Q(target.definition["cut_radius"]) == Q(oc["original_binary_cut"]["exact_rational"]),
            "Keep the original physical binary cut without radius renormalisation")
        joined,jid = R.read(self.directory/"same-C-refined-enclosures.json",
            report["intersection"]["actual_file"],self.check)
        require(joined.get("schema") == R.SCHEMA+"-same-semantic-enclosures"
            and same(joined["actual_refined_C"],fid) and same(joined["actual_refined_cut"],ncid)
            and canonical(joined["semantic_input_equivalence"]) == canonical(equality),
            "The independent refined-leaf file lacks its actual complete producer")
        self.intersections = {}; self.leaf_bounds = {}
        require(set(joined["semantic_cut_leaf_enclosures"]) == {x for x,_ in LEAVES},
            "Retain exactly the three original semantic C leaves")
        for name,key in LEAVES:
            self.check()
            before = R.interval(oc["same_point_E_Er_Err_enclosures"][key])
            existing = target.leaves[name]
            require(before == (existing.lo,existing.hi)
                and before == (Q(target.definition["actual_enclosure_leaves"][name]["lower"]),
                    Q(target.definition["actual_enclosure_leaves"][name]["upper"])),
                "The source target's actual original leaf differs: "+name)
            both = R.intersect(oc["same_point_E_Er_Err_enclosures"][key],
                nc["same_point_E_Er_Err_enclosures"][key])
            require(canonical(both) == canonical(joined["cut_twojet_intersections"][key]),
                "The full original leaf intersection was changed: "+name)
            actual = (Q(both["lower_exact"]),Q(both["upper_exact"]))
            leaf = joined["semantic_cut_leaf_enclosures"][name]
            require(actual == (Q(leaf["lower"]),Q(leaf["upper"])),
                "The reported semantic leaf is not the original exact intersection: "+name)
            self.intersections[name] = both; self.leaf_bounds[name] = actual
        require(canonical(joined) == canonical(report["intersection"]["necessary_original_values"]),
            "The original R489 result and its actual intersection member differ")
        self.actual = dict(actual_R489_result=self.report_id,actual_R489_input=self.input_id,
            actual_refined_leaf_file=jid,actual_original_C=oid,actual_original_cut=ocid,
            actual_refined_C=fid,actual_refined_cut=ncid,
            actual_original_C_binding=obid,actual_refined_C_binding=fbid,
            original_launch=lid,original_deadline=did,
            original_science_deadline_unix_seconds=self.deadline,
            semantic_input_equivalence=identity(equality),
            complete_original_C_input_binding=identity(ob),
            same_all_original_root_family=True,physical_cut_unchanged=True,
            original_whole_query_complete=old.get("continuous_convention_C_query_enclosures_complete"),
            refined_whole_query_complete=fresh.get("continuous_convention_C_query_enclosures_complete"),
            whole_query_success_not_used_as_a_cut_leaf_gate=True)
        self.definition_id = identity(target.definition)
        self.target_identity = copy.deepcopy(target.binding["complete_target_identity"])
        self.check()

    def check(self):
        self.external_check()
        if self.deadline is not None and time.time() >= self.deadline:
            raise ResourceStop("original_absolute_science_deadline_reached; no clock restarted")

    def describe(self):
        return dict(schema=SCHEMA+"-provider",source=receipt(__file__),
            actual=copy.deepcopy(self.actual),
            unchanged_accurate_definition_identity=copy.deepcopy(self.definition_id),
            original_complete_target_identity=identity(self.target_identity),
            semantic_leaf_intersections=copy.deepcopy(self.intersections),
            evaluated_leaf_endpoints={key:dict(lower=str(lo),upper=str(hi))
                for key,(lo,hi) in self.leaf_bounds.items()},
            no_common_realization_of_arbitrary_independent_box_points_claimed=True,
            no_original_C_CP_definition_or_nodal_payload_written=True,
            new_tail_query_provider_installed=False)


class RefinedTenTarget:
    """Independent evaluation state, delegating the complete original cell formula."""
    def __init__(self, original, provider, sqrt_bits, original_module):
        actions(); provider.check()
        require(type(sqrt_bits) is int and sqrt_bits > 0, "Specify the actual positive sqrt work precision")
        self.original, self.provider = original, provider
        self._original_module = original_module
        self.Factory = original.Factory
        self.definition = original.definition
        self.parameters = copy.deepcopy(original.parameters)
        self.tree = self.Factory.Tree(); self.tree.nodes = copy.deepcopy(original.tree.nodes)
        self.leaves = {name:self.Factory.Box(lo,hi) for name,(lo,hi) in provider.leaf_bounds.items()}
        self.values = self.tree.evaluate(self.leaves,sqrt_bits)
        self.pieces = copy.deepcopy(original.pieces)
        self.supports = copy.deepcopy(original.supports)
        self.roots = copy.deepcopy(original.roots)
        self.length = self.values[self.roots["total_length"]]
        self.numeric_length = original.numeric_length
        require(self.length.lo > 0 and self.numeric_length > 0,
            "The same accurate/physical length evaluation remains unresolved")
        for item in self.pieces+self.supports:
            require(self.values[item["width"]].lo > 0,
                "A complete original piece/support width remains unresolved")
        self.model = dict(tree=self.tree,pieces=self.pieces,supports=self.supports,
            roots=self.roots,parameters=self.parameters,
            control_terms=copy.deepcopy(original.model["control_terms"]))
        self.breakpoints = tuple(original.breakpoints); self.cache = OrderedDict()
        self.calls = 0
        self.binding = dict(schema=SCHEMA+"-accurate-target-evaluation",
            complete_target_identity=copy.deepcopy(original.binding["complete_target_identity"]),
            complete_accurate_definition=copy.deepcopy(original.binding["complete_accurate_definition"]),
            complete_original_C_input_binding=copy.deepcopy(original.binding["complete_original_C_input_binding"]),
            actual_factory_result=copy.deepcopy(original.binding["actual_factory_result"]),
            original_target_binding_identity=identity(original.binding),
            original_target_binding_schema=original.binding["schema"],
            original_declared_leaf_enclosures=copy.deepcopy(self.definition["actual_enclosure_leaves"]),
            actual_evaluation_leaf_enclosures={name:box.record() for name,box in self.leaves.items()},
            actual_refined_leaf_provider=provider.describe(),
            true_length_enclosure=self.length.record(),numeric_length_exact=str(self.numeric_length),
            all10_original_exact_parameters=[str(x) for x in self.parameters],
            complete_original_tree=identity(self.tree.nodes),
            complete_original_pieces=identity(self.pieces),
            complete_original_supports=identity(self.supports),
            only_evaluation_enclosures_changed=True,original_definition_receipt_not_relabelled=True,
            all_original_piece_and_control_cases_still_enumerated=True,
            old_requested_parameter_domain_result_not_relabelled_or_recomputed=True)
        require(identity(self.definition) == provider.definition_id
            and self.tree.nodes == original.tree.nodes and self.roots == original.roots
            and self.parameters == original.parameters,
            "The exact function definition was changed while forming an enclosure view")
        provider.check()

    def closed_range(self,left,right):
        actions(); self.provider.check()
        jets,radial,report = self._original_module.AccurateTenTarget.closed_range(self,left,right)
        self.calls += 1; self.provider.check()
        report = copy.deepcopy(report)
        report.update(schema=SCHEMA+"-closed-target-cell",
            original_callee_schema=self._original_module.SCHEMA+"-closed-target-cell",
            actual_refined_leaf_file=self.provider.actual["actual_refined_leaf_file"],
            all_original_pieces_controls_and_closed_endpoints_retained=True,
            exact_target_definition_identity=self.provider.definition_id)
        return jets,radial,report


class RefinedCutBundle:
    def __init__(self, original, target, model, field, provider, cut_module, binding):
        self.original = original
        self.source_bundle = original.source_bundle
        self.target,self.model,self.field = target,model,field
        self.Active,self.Background = original.Active,original.Background
        self.provider,self._cut_module = provider,cut_module
        self.binding = binding; self.schema = BUNDLE_SCHEMA
        self.required_geometry_loader = Path(__file__).stem+".load_refined_accurate_cut_field"
        self.calls = 0

    @property
    def pieces(self):
        return self.field.pieces

    def evaluate(self,piece,radial,angular,lower=False):
        actions(); self.provider.check()
        result = self._cut_module.AccurateCutBundle.evaluate(self,piece,radial,angular,lower)
        self.calls += 1; self.provider.check()
        return result

    def expression_identity(self):
        return dict(schema=SCHEMA+"-same-expression-enclosure-view",
            source=receipt(__file__),original_expression=self.original.expression_identity(),
            actual_evaluation_expression=self.field.expression_identity(),
            mathematical_expression_signature=self.binding["mathematical_expression_signature"],
            same_exact_R416_function_for_every_original_C_member=True,
            new_C_or_parameter_midpoint_not_chosen=True)

    def describe(self):
        return dict(schema=SCHEMA+"-description",source=receipt(__file__),
            provider=self.provider.describe(),binding=copy.deepcopy(self.binding),
            old_and_evaluated_true_length=dict(original=self.original.target.length.record(),
                refined=self.target.length.record()),
            evaluated_cut_coefficients={name:self.model.coefficients[name].record() for name in COEFFICIENTS},
            original_cut_coefficient_enclosures={name:self.original.model.coefficients[name].record()
                for name in COEFFICIENTS},
            original_common_chart_window=copy.deepcopy(self.original.model.chart),
            evaluated_common_chart_window=copy.deepcopy(self.model.chart),
            actual_target_closed_cell_calls=self.target.calls,actual_active_sixjet_cell_calls=self.calls,
            scope=dict(prefix_target_reads_refined_semantic_leaves=True,
                exact_cut_chart_coefficients_read_refined_semantic_leaves=True,
                active_cut_patch_sixjets_read_refined_semantic_leaves=True,
                unchanged_prefix_and_native_nodes_B_material_and_caps=True,
                complete_active_piece_list_unchanged=True,
                tail_E_of_r_query_provider_rebound=False,
                live_query_or_whole_query_error_bounds_improved_here=False,
                full_closed_metric_reach_held_or_error_traversal_executed=False,
                R418_R459_R483_outer_source_registration_added=False,
                R441_R451_R464_generated_families_registered=False,
                new_BVP_or_acceptance_or_solver_gate=False,
                all_t_cap_and_atlas_theorems_not_replaced_by_declared_cell_examples=True))


def bind_loaded_refined_cut_bundle(current, *, computations, refinement_directory,
        refinement_result_sha256, sqrt_bits, budget_check=None):
    """Consume a genuinely loaded original R416 bundle, retaining its full provenance."""
    actions()
    if budget_check is not None:
        budget_check()
    comp = Path(computations).resolve(strict=True)
    Cut = actual_owner(current,"AccurateCutBundle",CUT_NAME,CUT_SHA,comp)
    require(current.schema == Cut.SCHEMA and current.required_geometry_loader == Cut.LOADER_NAME,
        "This first thin registration is the actual original R416 family only")
    Target = actual_owner(current.target,"AccurateTenTarget",TARGET_NAME,TARGET_SHA,comp)
    require(receipt(current.model.Factory.__file__)["sha256"] == FACTORY_SHA
        and receipt(current.Active.__file__)["sha256"] == ACTIVE_SHA,
        "Use the actual same complete scalar and six-jet arithmetic modules")
    original_definition = current.source_bundle[4].checkpoint.owner.data["definition_path"]
    expected_definition = current.target.binding["complete_accurate_definition"]
    require(same(receipt(original_definition,budget_check),expected_definition),
        "The actual complete saved definition bytes changed")
    provider = RefinedLeafProvider(current.target,computations=comp,
        refinement_directory=refinement_directory,
        refinement_result_sha256=refinement_result_sha256,budget_check=budget_check)
    target = RefinedTenTarget(current.target,provider,sqrt_bits,Target)
    model = Cut.AccurateCutModel(target,current.field,current.model.Factory,sqrt_bits)
    # These equalities are definitions/source binding, not a new residual or precision gate.
    require(model.tree.nodes == current.model.tree.nodes and model.roots == current.model.roots
        and model.cut == current.model.cut and model.numeric_length == current.model.numeric_length,
        "Refining intervals must not alter the exact appended cut-coefficient DAG")
    signature = identity(dict(original_nodes=target.tree.nodes,appended_nodes=model.tree.nodes,
        roots=model.roots,parameters=[str(x) for x in target.parameters],
        cut=str(model.cut),numeric_length=str(model.numeric_length),
        original_complete_target=current.target.binding["complete_target_identity"],
        original_source_bundle_binding=current.source_bundle[-1]))
    binding = dict(schema=SCHEMA+"-binding",source=receipt(__file__),
        original_R416_source=dict(file=CUT_NAME,sha256=CUT_SHA),
        original_R400_source=dict(file=TARGET_NAME,sha256=TARGET_SHA),
        actual_refined_provider_result=provider.report_id,
        actual_refined_leaf_file=provider.actual["actual_refined_leaf_file"],
        original_R416_binding_identity=identity(current.binding),
        original_R409_source_bundle_binding_identity=identity(current.source_bundle[-1]),
        actual_original_450_checkpoint=copy.deepcopy(current.binding["actual_450_checkpoint"]),
        original_accurate_definition=copy.deepcopy(expected_definition),
        original_complete_target_identity=identity(current.target.binding["complete_target_identity"]),
        original_exact_ten_parameters=[str(x) for x in target.parameters],
        original_material_definition=identity(dict(core=[str(x) for x in current.field.core],
            density=[str(x) for x in current.field.density],rho_lower=str(current.field.rho_lower),
            registration=current.field.registration)),
        mathematical_expression_signature=signature,
        actual_evaluation_target_binding_identity=identity(target.binding),
        actual_evaluation_cut_model_identity=identity(model.definition),
        original_checkpoint_definition_nodes_B_and_material_not_written=True,
        new_enclosure_identity_is_not_a_new_exact_field_identity=True,
        original_accepted_parent_not_replaced=True)
    field = Cut.new_exact_field(current.source_bundle,current.Active,current.Background,model,binding)
    require(field.pieces == current.field.pieces and field.x == current.field.x
        and field.radii == current.field.radii and field.core == current.field.core
        and field.density == current.field.density and field.rho_lower == current.field.rho_lower
        and field.registration == current.field.registration,
        "The complete original field coordinates/nodes/material sources differ")
    require(same(receipt(original_definition,provider.check),expected_definition),
        "The actual original definition was modified")
    provider.check()
    return RefinedCutBundle(current,target,model,field,provider,Cut,binding)


def load_refined_accurate_cut_field(args, *, budget_check=None):
    """Original R416 load -> independent R492 read-only enclosure view.

    All original R416 arguments remain real and mandatory as before.
    Added: refinement_directory and refinement_result_sha256.  This first
    adapter does not bypass an original field which has not actually loaded.
    """
    actions()
    if budget_check is not None:
        budget_check()
    Cut = load(args.computations,CUT_NAME)
    current = Cut.load_accurate_cut_field(args)
    return bind_loaded_refined_cut_bundle(current,computations=args.computations,
        refinement_directory=args.refinement_directory,
        refinement_result_sha256=args.refinement_result_sha256,
        sqrt_bits=args.sqrt_bits,budget_check=budget_check)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations",type=Path,default=HERE)
    parser.add_argument("--directory",type=Path,required=True)
    parser.add_argument("--result-sha256",required=True)
    parser.add_argument("--checkpoint-directory",type=Path)
    parser.add_argument("--proof-directory",type=Path)
    parser.add_argument("--refinement-directory",type=Path,required=True)
    parser.add_argument("--refinement-result-sha256",required=True)
    parser.add_argument("--sqrt-bits",type=int,required=True)
    parser.add_argument("--interval-bits",type=int,required=True)
    parser.add_argument("--budget-seconds",type=float,required=True)
    parser.add_argument("--cell-plan",type=Path)
    parser.add_argument("--cell-plan-sha256")
    parser.add_argument("--out",type=Path,required=True)
    args = parser.parse_args(argv); actions()
    require(math.isfinite(args.budget_seconds) and args.budget_seconds > 0,
        "Declare an actual positive complete consumer work budget")
    began = time.monotonic(); signals = []; handlers = {}
    def receive(number,frame):
        signals.append(dict(number=int(number),name=signal.Signals(number).name))
    def check():
        if signals:
            raise ResourceStop("external_interruption; no mathematical refutation inferred")
        if time.monotonic()-began >= args.budget_seconds:
            raise ResourceStop("declared_complete_consumer_budget_reached")
    root = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out = args.out.resolve(); require(out.is_relative_to(root) and not out.exists(),
        "Use a fresh temporary output under RUNNER_TEMP")
    for path in (args.directory,args.refinement_directory,args.computations,
                 args.checkpoint_directory,args.proof_directory,args.cell_plan):
        if path is not None:
            require(not Path(path).resolve().is_relative_to(out), "Never own or overwrite an original input")
    out.mkdir(parents=True)
    for number in (signal.SIGTERM,signal.SIGINT):
        handlers[number] = signal.signal(number,receive)
    result = dict(schema=SCHEMA,source=receipt(__file__),repository=REPOSITORY,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        binding_complete=False,description=None,declared_cells=[],completed_cells=0,
        current_cell=None,unvisited_cell_indices=[],error=None,resource_partial=False,
        full_domain_certificate=False,new_accepted_parent=False,raw_deleted=False,
        original_absolute_deadline_restarted=False,outer_owned_hard_deadline_required=True)
    code = 2; plan = None
    try:
        check()
        if (args.cell_plan is None) != (args.cell_plan_sha256 is None):
            raise ValueError("Bind both the actual cell-plan file and SHA, or neither")
        if args.cell_plan is not None:
            R = load(args.computations,PROVIDER_NAME)
            plan,pid = R.read(args.cell_plan,args.cell_plan_sha256,check)
            require(plan.get("schema") == PLAN_SCHEMA and isinstance(plan.get("cells"),list),
                "Use the explicit finite declared cell list; it is not a full-domain cover")
            result["actual_cell_plan"] = pid
            result["requested_cell_count"] = len(plan["cells"])
            result["unvisited_cell_indices"] = list(range(len(plan["cells"])))
        current = load_refined_accurate_cut_field(args,budget_check=check)
        result["binding_complete"] = True; result["description"] = current.describe()
        cells = [] if plan is None else plan["cells"]
        for index,row in enumerate(cells):
            current.provider.check()  # do not remove the unvisited index before the work check
            result["current_cell"] = dict(index=index,original=row)
            if row.get("kind") == "target":
                require(set(row) == {"kind","radial"} and len(row["radial"]) == 2,
                    "Declare the complete closed numerical-prefix target interval")
                lo,hi = map(Q,row["radial"])
                jets,g11,detail = current.target.closed_range(lo,hi)
                actual = dict(index=index,original=row,all_three_radius_jets=[x.record() for x in jets],
                    radial_metric=g11.record(),original_complete_cell_record=detail)
            elif row.get("kind") == "field":
                require(set(row) == {"kind","piece_index","radial","angular","lower"}
                    and type(row["piece_index"]) is int
                    and 0 <= row["piece_index"] < len(current.pieces),
                    "Use an actual complete active piece index and reflected side")
                values = current.evaluate(current.pieces[row["piece_index"]],
                    row["radial"],row["angular"],row["lower"])
                actual = dict(index=index,original=row,complete_six_jets={name:[
                    current.Active.encode_interval(value.d[j]) for value in values]
                    for j,name in enumerate(current.Active.JET_NAMES)})
            else:
                raise ValueError("Only actual target or active-field cells are registered")
            current.provider.check()
            result["declared_cells"].append(actual); result["completed_cells"] += 1
            result["unvisited_cell_indices"] = list(range(index+1,len(cells)))
            result["current_cell"] = None
        result["description"] = current.describe()
        result["all_declared_cells_returned"] = True
        result["no_cells_requested_is_binding_only"] = plan is None or not cells
        code = 0
    except BaseException as error:
        result["error"] = dict(type=type(error).__name__,message=str(error),
            traceback=traceback.format_exc())
        result["resource_partial"] = isinstance(error,ResourceStop)
    finally:
        for number,previous in handlers.items():
            signal.signal(number,previous)
        result["external_signals"] = signals
        result["elapsed_seconds_including_original_loading"] = time.monotonic()-began
        result["actual_exit_code_before_transport"] = code
    rid = write(out/"result.json",result)
    raw = canonical(result)
    if len(raw) > LIMIT:
        small = dict(schema=SCHEMA+"-transport-partial",original_result=rid,
            required_necessary_bytes=len(raw),summary_limit_bytes=LIMIT,
            original_exit_code=code,complete_necessary_readback=False,
            raw_deleted=False,unread_necessary_scope="complete original result retained only in Actions")
        write(out/"necessary-summary.json",small)
        print("BEGIN_R492_SAME_C_LEAF_CONSUMER_NECESSARY")
        print(canonical(small).decode("ascii"),end="")
        print("END_R492_SAME_C_LEAF_CONSUMER_NECESSARY")
        return 70
    sid = write(out/"necessary-summary.json",result)
    print("BEGIN_R492_SAME_C_LEAF_CONSUMER_NECESSARY")
    print(raw.decode("ascii"),end="")
    print("END_R492_SAME_C_LEAF_CONSUMER_NECESSARY")
    print(json.dumps(dict(event="R492_necessary_identity",summary=sid,actual_result=rid,
        complete_necessary_readback=True),sort_keys=True,separators=(",",":")))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
