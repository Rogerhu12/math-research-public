#!/usr/bin/env python3
"""Unchanged whole-image held witness for the checked shared-background field.

Use the new shared-background R241 producer and its complete position packet.
The exact original full-state binding body is reused, adapting only its
coverage schema and producer SHA; the complete new load_shared_bundle is also
called and its binding must equal the packet's binding.  All active balls,
both full cap disks, the whole-family diameter, all supplied error budgets,
and the original 0.2 gates remain in the frozen original held consumer.
No spatial pair pass, tail solve, zero solve or BVP is repeated.  The checked
geometry loader reconstructs the same complete field/registration for source
identity; it does not create a new acceptance or certify continuous envelopes.
"""
from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import math
from pathlib import Path
import sys

import geometry_20261114_full_state_held_hausdorff as original
import geometry_20261114_shared_background_closed_assembly as geometry
import geometry_20261114_shared_background_continuous_cover as cover_source


HERE = Path(__file__).resolve().parent
EXPECTED_SOURCES = {
    "geometry_20261114_full_state_held_hausdorff.py":
        "31d99236cfd9a522ac54c8ddc6e4c615ac0be2f292535a05f776ab64bfd9fe1c",
    "geometry_20261114_full_state_continuous_cover.py":
        "c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6",
    "geometry_20261114_held_hausdorff_cover.py":
        "3ba8a0d02266d2b057862c0741dc0a6f65c1276514adab8e403852d69a55809c",
    "geometry_20261114_shared_background_closed_assembly.py":
        "ac635c11aa31925a4175876ffa2c8b959766629aebf9e3abaf97a68ca0e096cb",
    "geometry_20261114_shared_background_continuous_cover.py":
        "fc5bbb6762cf589a8ab6096c066bdd1bbad17c516954a43c4a40496445e9a5fb",
}
read,sha = original.read,original.sha


def check_sources():
    for name,digest in EXPECTED_SOURCES.items():
        original.equal(sha(HERE/name),digest,"frozen shared held source "+name)
    cover_source.check_sources()


def build_binding_body():
    """Only the new coverage schema and its actual producer identity differ."""
    body = inspect.getsource(original.bind)
    schema_old = 'coverage.get("schema") != "R37-R241-complete-full-state-spatial-cover-budget-v1"'
    schema_new = 'coverage.get("schema") != "'+cover_source.SCHEMA+'"'
    producer_old = 'producer_sha = EXPECTED_SOURCES["geometry_20261114_full_state_continuous_cover.py"]'
    producer_new = 'producer_sha = SHARED_COVER_SHA'
    adapted = body
    for before,after in ((schema_old,schema_new),(producer_old,producer_new)):
        if adapted.count(before) != 1:
            raise ValueError("The frozen full-state held binding anchor changed")
        adapted = adapted.replace(before,after)
    namespace = dict(original.__dict__)
    namespace["SHARED_COVER_SHA"] = EXPECTED_SOURCES[
        "geometry_20261114_shared_background_continuous_cover.py"]
    exec(compile(adapted,str(HERE/"geometry_20261114_full_state_held_hausdorff.py")+
                 "::<shared-producer-identity-only>","exec"),namespace)
    return namespace["bind"],dict(
        original_full_state_binding_body_sha256=hashlib.sha256(body.encode()).hexdigest(),
        adapted_full_state_binding_body_sha256=hashlib.sha256(adapted.encode()).hexdigest(),
        adaptations_exactly_coverage_schema_and_producer_SHA=True)


def bind_shared(args, unchanged_bind, body_identity):
    """Retain every original binding check and explicitly reconstruct own B."""
    paths,plan,assembly,reference,saved,A,binding = geometry.load_shared_bundle(args)
    old_paths,evidence = unchanged_bind(args)
    if {key:Path(value).resolve() for key,value in paths.items()} != {
            key:Path(value).resolve() for key,value in old_paths.items()}:
        raise ValueError("The held packet and shared geometry loader selected different files")
    original.equal(evidence["complete_field_binding"],binding,
                   "new loader vs complete position producer binding")
    coverage = read(args.coverage)
    producer = coverage["shared_background_consumer"]
    original.equal(producer["loader"],
        "geometry_20261114_shared_background_closed_assembly.load_shared_bundle",
        "explicit new geometry loader")
    original.equal(producer["wrapper_sha256"],EXPECTED_SOURCES[
        "geometry_20261114_shared_background_closed_assembly.py"],"same geometric wrapper")
    original.equal(producer["descriptor_sha256"],sha(args.descriptor),"same exact B descriptor")
    original.equal(producer["exact_background_payload_sha256"],
        binding["shared_background_geometry"]["exact_background_payload_sha256"],"same exact B payload")
    original.equal(producer["no_legacy_loader_fallback"],True,"no old background fallback")
    A.assert_unchanged()
    evidence.update(shared_background_geometry=binding["shared_background_geometry"],
        shared_background_wrapper_sha256=EXPECTED_SOURCES[
            "geometry_20261114_shared_background_closed_assembly.py"],
        shared_background_cover_source_sha256=EXPECTED_SOURCES[
            "geometry_20261114_shared_background_continuous_cover.py"],
        shared_background_descriptor_sha256=sha(args.descriptor),
        original_closed_source_bundle_revalidated=True,
        complete_new_geometry_loader_actually_called=True,
        explicit_loader="geometry_20261114_shared_background_closed_assembly.load_shared_bundle",
        no_legacy_loader_fallback=True,
        new_SavedPrefix_or_tail_evaluation_run=True,
        reconstruction_scope="The same complete prefix/tail/background and cut are reconstructed only by the bound geometry loader; no BVP, nonlinear tail solve, spatial pair pass or new geometric acceptance",
        full_state_binding_body=body_identity,
        original_target_metric_and_all_envelopes_retained=True,
        exact_continuous_envelopes_certified_here=False)
    return paths,evidence


def main():
    original.actions_only()
    check_sources()
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("directory","source-directory","descriptor","cover","coverage",
                 "checkpoint","port","config","tail-response","complete","source-topic","out"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--basename",default="surface")
    parser.add_argument("--source-basename",default="surface")
    parser.add_argument("--phase",type=float,default=math.pi/2)
    parser.add_argument("--witness-source-index",type=int)
    parser.add_argument("--rotation-position-error",type=float)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Keep the original held evidence; use a fresh output")
    unchanged_bind,body_identity = build_binding_body()
    arguments = [__file__]
    for key in ("directory","cover","coverage","checkpoint","port","config",
                "tail_response","complete","out"):
        arguments += ["--"+key.replace("_","-"),str(getattr(args,key))]
    arguments += ["--phase",repr(args.phase)]
    if args.witness_source_index is not None:
        arguments += ["--witness-source-index",str(args.witness_source_index)]
    if args.rotation_position_error is not None:
        arguments += ["--rotation-position-error",repr(args.rotation_position_error)]
    previous_bind,previous_argv = original.bind,sys.argv
    def own_binding(parsed):
        # The unchanged original main parsed exactly these numerical witness
        # options. Additional arguments select only the explicit geometry.
        for key in ("directory","cover","coverage","checkpoint","port","config",
                    "tail_response","complete","out","phase","witness_source_index",
                    "rotation_position_error"):
            original.equal(getattr(parsed,key),getattr(args,key),"unchanged held argument "+key)
        return bind_shared(args,unchanged_bind,body_identity)
    original.bind,sys.argv = own_binding,arguments
    try:
        original.main()
    finally:
        original.bind,sys.argv = previous_bind,previous_argv
    result = read(args.out)
    result["original_complete_held_adapter_schema"] = result["schema"]
    result["schema"] = "actual-complete-shared-background-held-Hausdorff-cover-witness-v1"
    result["original_complete_held_adapter_sha256"] = EXPECTED_SOURCES[
        "geometry_20261114_full_state_held_hausdorff.py"]
    result["adapter_source_sha256"] = sha(__file__)
    result["shared_background_consumer_sources"] = EXPECTED_SOURCES
    result["shared_background_binding_body"] = body_identity
    result["same_new_geometry_loader_used_as_position_producer"] = True
    result["distance_formula_and_thresholds_changed"] = False
    result["all_active_blocks_and_both_whole_disks_retained"] = True
    result["whole_family_diameter_and_point_normal_error_budgets_unchanged"] = True
    result["no_legacy_loader_fallback"] = True
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+"\n")


if __name__ == "__main__":
    main()
