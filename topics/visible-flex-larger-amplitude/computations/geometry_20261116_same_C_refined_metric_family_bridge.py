#!/usr/bin/env python3
"""R495 explicit same-C enclosure bridge for existing complete metric families.

Use R492's actual provider/evaluation classes after checking each original
loaded class owner and complete source identity. No original module globals,
CP, definition, nodes, material map, coefficients or solver gates are changed.
The outer metric/error views use the original closed algorithms. Their tail
C(r) query producer is intentionally still the original bound producer.
All scientific evaluation belongs only to the named public Actions.
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R495-same-C-refined-leaf-complete-metric-family-bridge-v1"
LEAF_NAME = "geometry_20261116_same_C_refined_leaf_target_and_cut.py"
LEAF_SHA = "a7b1bd9d64db43986b5718d664dc6209227cd89a0cd9fb490e8dc6f9f4482aa7"
FAMILIES = {
    "original112": dict(
        cut="geometry_20261115_current_C_accurate_cut_patch.py",
        cut_sha256="28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b",
        schema="R416-current-C-ten450-accurate-cut-atlas-field-v1",
        target="geometry_20261115_continuous_ten_frozen450_prefix_metric.py",
        target_sha256="011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84",
        checkpoint_key="actual_450_checkpoint"),
    "resolution112": dict(
        cut="geometry_20261116_current_C_resolution_accurate_cut_patch.py",
        cut_sha256="8811f89c7395bb4aed1adabe6c6825c801e1e41a9d80d416b0a4746596ae9a52",
        schema="R441-current-C-resolution450-accurate-cut-atlas-field-v1",
        target="geometry_20261115_continuous_ten_frozen450_prefix_metric.py",
        target_sha256="011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84",
        checkpoint_key="actual_450_checkpoint"),
    "completeM": dict(
        cut="geometry_20261116_current_C_M_accurate_cut_patch.py",
        cut_sha256="747b9d1f77b307529aeb65e3ad31e831b9f54238916bcae23fa578efd6a76492",
        schema="R451-current-C-complete-M-accurate-cut-atlas-field-v1",
        target="geometry_20261116_continuous_ten_M_prefix_metric.py",
        target_sha256="56a3a9fed5b52130199e0fd6d6d72d6d12a82fbbf9c248e77608e8bfd056be",
        checkpoint_key="actual_frozen_M_checkpoint"),
    "incrementalM": dict(
        cut="geometry_20261116_current_C_incremental_M_accurate_cut_patch.py",
        cut_sha256="8105c8148d221b5ba10bc332631c88764d620dc59d30936bbe1067b6a54228e2",
        schema="R464-current-C-incremental-M-accurate-cut-atlas-field-v1",
        target="geometry_20261116_continuous_ten_incremental_M_prefix_metric.py",
        target_sha256="fd74b6ad9dc1b6069b016dd7fce14e0c35215bc76b045682172e3e10522a7402",
        checkpoint_key="actual_frozen_M_checkpoint"),
}


def require(ok,message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "Execute this interval bridge only in the named public Actions")


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=True,allow_nan=False)+"\n").encode("ascii")


def identity(value):
    raw=canonical(value)
    return dict(canonical_bytes=len(raw),canonical_sha256=hashlib.sha256(raw).hexdigest())


def receipt(path):
    path=Path(path);raw=path.read_bytes()
    return dict(file=path.name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def leaf_library(comp):
    actions()
    comp=Path(comp).resolve(strict=True)
    require(comp == HERE,"Use the bridge and all actual loaders in the same computations HERE")
    path=comp/LEAF_NAME
    require(receipt(path)["sha256"] == LEAF_SHA,"The complete R492 source differs")
    label="_r495_leaf_"+str(time.monotonic_ns())
    spec=importlib.util.spec_from_file_location(label,path)
    module=importlib.util.module_from_spec(spec);sys.modules[label]=module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(label,None);raise
    return module


class Stop(RuntimeError):
    pass


def check_local_budget(started,budget_seconds):
    if time.monotonic()-started >= budget_seconds:
        raise Stop("original_complete_metric_allowance_exhausted_in_leaf_binding")


def bind_loaded(current, *, family, args, budget_check=None):
    """The original family loader has already executed its complete input checks."""
    actions()
    require(family in FAMILIES,"Use one explicitly registered actual loaded family")
    row=FAMILIES[family];R=leaf_library(args.computations)
    Cut=R.actual_owner(current,"AccurateCutBundle",row["cut"],row["cut_sha256"],HERE)
    Target=R.actual_owner(current.target,"AccurateTenTarget",row["target"],row["target_sha256"],HERE)
    require(current.schema == row["schema"] == Cut.SCHEMA
        and current.required_geometry_loader == Cut.LOADER_NAME,
        "The actual field loader schema/source tuple differs")
    require(R.receipt(current.model.Factory.__file__)["sha256"] == R.FACTORY_SHA
        and R.receipt(current.Active.__file__)["sha256"] == R.ACTIVE_SHA,
        "Keep the actual complete72c target and675 six-jet formulas")
    original_definition=current.source_bundle[4].checkpoint.owner.data["definition_path"]
    definition_receipt=current.target.binding["complete_accurate_definition"]
    require(R.same(R.receipt(original_definition,budget_check),definition_receipt),
        "The original complete accurate definition bytes differ")
    provider=R.RefinedLeafProvider(current.target,computations=HERE,
        refinement_directory=args.refinement_directory,
        refinement_result_sha256=args.refinement_result_sha256,budget_check=budget_check)
    target=R.RefinedTenTarget(current.target,provider,args.sqrt_bits,Target)
    # This is the unchanged actual parameter list required by the old complete
    # metric binding. It is not a new coefficient or a new interval leaf.
    frozen=copy.deepcopy(current.target.binding["all10_frozen_exact_dyadics"])
    require(frozen == [str(x) for x in target.parameters],"The actual ten frozen values differ")
    target.binding["all10_frozen_exact_dyadics"]=frozen
    model=Cut.AccurateCutModel(target,current.field,current.model.Factory,args.sqrt_bits)
    require(model.tree.nodes == current.model.tree.nodes and model.roots == current.model.roots
        and model.cut == current.model.cut and model.numeric_length == current.model.numeric_length,
        "Only enclosures, not the exact appended function DAG, may change")
    signature=identity(dict(original_nodes=target.tree.nodes,appended_nodes=model.tree.nodes,
        roots=model.roots,ten_parameters=frozen,cut=str(model.cut),
        numeric_length=str(model.numeric_length),
        actual_target_identity=current.target.binding["complete_target_identity"],
        original_source_bundle_binding=current.source_bundle[-1]))
    binding=copy.deepcopy(current.binding)
    binding.update(schema=SCHEMA+"-"+family+"-binding",source=receipt(__file__),
        required_geometry_loader=Path(__file__).stem+".bind_loaded",
        original_loaded_family=family,original_loaded_schema=current.schema,
        original_complete_field_binding_identity=identity(current.binding),
        original_R492_source=receipt(HERE/LEAF_NAME),
        actual_R489_result=provider.report_id,
        actual_refined_leaf_file=provider.actual["actual_refined_leaf_file"],
        complete_target_binding_identity=identity(target.binding),
        accurate_cut_expression_identity=identity(model.definition),
        mathematical_expression_signature=signature,
        exact_field_function_and_original_ten_parameters_unchanged=True,
        original_complete_nodal_material_and_B_payloads_unchanged=True,
        old_definition_receipt_not_changed_to_new_enclosure_receipt=True,
        tail_E_of_r_query_result_still_the_original_bound_result=True,
        actual_interval_bits=args.interval_bits,actual_sqrt_bits=args.sqrt_bits)
    require(row["checkpoint_key"] in binding,"Keep the actual original complete checkpoint descriptor")
    field=Cut.new_exact_field(current.source_bundle,current.Active,current.Background,model,binding)
    require(field.pieces == current.field.pieces and field.x == current.field.x
        and field.radii == current.field.radii and field.core == current.field.core
        and field.density == current.field.density and field.registration == current.field.registration
        and field.rho_lower == current.field.rho_lower and field.M == current.field.M,
        "The original complete field or material data changed")
    require(R.same(R.receipt(original_definition,provider.check),definition_receipt),
        "The original definition was modified")
    view=R.RefinedCutBundle(current,target,model,field,provider,Cut,binding)
    view.schema=SCHEMA+"-"+family+"-bundle"
    view.required_geometry_loader=Path(__file__).stem+".bind_loaded"
    view.R495_family=family
    provider.check()
    return view


def original_material_current(current):
    """Keep the already registered original material API and its valid enclosures.

    Its exact field is equal to the refined view by the identical DAG/raw
    source checks above. The base/global metric uses the refined view; these
    finite t-witness queries may keep wider original coefficient enclosures.
    No unregistered new object is relabelled as an old material source.
    """
    require(getattr(current,"R495_family",None) in FAMILIES,
        "Use the actual registered refined enclosure view")
    return current.original


def clipped_total_allowance(current,started,requested):
    current.provider.check()
    elapsed=time.monotonic()-started
    remaining=max(0.0,current.provider.deadline-time.time())
    return min(float(requested),elapsed+remaining)


def is_resource_stop(error):
    if isinstance(error,Stop):
        return True
    module=sys.modules.get(type(error).__module__)
    path=getattr(module,"__file__",None)
    return bool(path is not None and Path(path).name == LEAF_NAME
        and receipt(path)["sha256"] == LEAF_SHA
        and getattr(module,"ResourceStop",None) is type(error))


def compact(current):
    if current is None:
        return None
    require(getattr(current,"R495_family",None) in FAMILIES,
        "The necessary refined-field record has an unknown source family")
    p=current.provider
    return dict(schema=SCHEMA+"-necessary-evaluation-scope",source=receipt(__file__),
        original_loaded_family=current.R495_family,
        actual_field_mode_count=current.field.M,
        original_loaded_source=FAMILIES[current.R495_family],
        actual_R489_result=p.report_id,actual_refined_leaf_file=p.actual["actual_refined_leaf_file"],
        original_accurate_definition_identity=p.definition_id,
        original_C_result=p.actual["actual_original_C"],refined_C_result=p.actual["actual_refined_C"],
        original_deadline=p.actual["original_deadline"],
        original_science_deadline_unix_seconds=p.deadline,
        actual_evaluation_leaf_bounds={key:dict(lower=str(lo),upper=str(hi))
            for key,(lo,hi) in p.leaf_bounds.items()},
        actual_accurate_length_enclosure=current.target.length.record(),
        actual_cut_coefficient_enclosures={key:value.record()
            for key,value in current.model.coefficients.items()},
        same_exact_function_signature=current.binding["mathematical_expression_signature"],
        prefix_target_and_active_cut_patch_use_new_leaf_enclosures=True,
        original_all_piece_control_and_closed_domain_scope_retained=True,
        same_exact_original_field_parameters_and_material_map=True,
        actual_t_witness_query_path_retains_original_valid_enclosures=True,
        base_metric_evaluation_path_uses_refined_field_and_target=True,
        scope_flags_describe_bound_paths_not_completed_cover=True,
        old_and_refined_views_are_the_same_exact_function_for_every_C_member=True,
        tail_C_query_producer_not_switched_to_R489_refined_C=True,
        solver_FD_fullDN_final_or_acceptance_gate_changed=False)
