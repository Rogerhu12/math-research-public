#!/usr/bin/env python3
"""Whole-source binding for exactly two complete fixed-Fejer refinements.

The N4096 and M320 families have separate full sources, layouts, norms and
immutable packets. The full existing family reader and model validator are
used without alteration. No generic schema bypass, fabricated coarse field,
working field evaluation or numerical success is introduced by this module.
"""
from __future__ import annotations
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

SCHEMA = "complete-fixed-fejer-base-bound-N4096-or-M320-accurate-field-family-binding-v1"
SOURCE_NAME = "fixed_fejer_base_bound_refinement_fee_source_binding.py"
TOPIC = "topics/visible-flex-larger-amplitude"
SCRIPT_DIRECTORY = "scripts/resume_20261126"
PARENT_DRIVER = ("fullclosed_fixed_fejer_immutable_point_so3_qp.py",
    "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd")
COMMON_PINS = {
    "reference": [
        "fixed_fejer_axisymmetric_reference.py",
        "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
    ],
    "continuous": [
        "so3_axisymmetric_continuous_integrand.py",
        "a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6"
    ],
    "reference_fees": [
        "fixed_fejer_reference_seed_angular_profile_error_bounds.py",
        "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b"
    ],
    "mean_integrals": [
        "fixed_fejer_reference_accurate_mean_residuals.py",
        "ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0"
    ],
    "fixed_input_binding": [
        "fixed_fejer_reference_input_binding.py",
        "3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f"
    ]
}
FAMILIES = {
    "N4096": {
        "family": "N4096",
        "report_schema": "complete-fixed-fejer-angular-refined-immutable-point-SO3-QP-v1",
        "pure_schema": "actual-fixed-fejer-angular-refined-envelope-SO3-readout-v1",
        "normal_schema": "complete-fixed-fejer-angular-refined-immutable-point-closure-values-normal-layer-v1",
        "base_schema": "complete-fixed-fejer-angular-refined-supported-SO3-meridian-v1",
        "current_M": 160,
        "current_N": 4096,
        "reference_M": 160,
        "reference_N": 2048,
        "J": 923,
        "K": 3,
        "n": 482,
        "free_size": 1333370,
        "source_role_count": 128,
        "source_registry_identity_sha256": "6fa504b099aaedac69d6c6c88d1ffa764408df7688eb7d80865c9b8c6ffc4e5c",
        "pins": {
            "reader": [
                "read_fixed_fejer_angular_refined_base_bound_so3_report.py",
                "015fc63cee72ffa9b2cc288c906844e61b8fc1bd96463b7d2281b3620b94b9ae"
            ],
            "driver": [
                "fullclosed_fixed_fejer_angular_refined_base_bound_so3_qp.py",
                "2ccf1d251e83850428c577fd522eeadbadd53df79c6f234848ad1eb8b94ccae4"
            ],
            "packets": [
                "fixed_fejer_angular_refined_root_packets.py",
                "fc1c35ff4e3b89e8702c3ce5ddf8ac8f665361624058974ac2b60e26635ff5d0"
            ],
            "normal": [
                "fixed_fejer_angular_refined_normal_lift.py",
                "2db038574bb13e226b61826949cc66d917f0186fe5b9156a50eb7180da3d4bda"
            ],
            "base": [
                "fixed_fejer_angular_refined_meridian_operator.py",
                "3f4d5c0ec5b03eba9e93660e1341c32f1bd4872e0d1250d489894dd4ba6ed915"
            ],
            "field_binding": [
                "fixed_fejer_angular_refined_source_binding.py",
                "dddfc5d0476c58c25cac37f5a6ceada612b55de465e91c08c58b098761a7c982"
            ],
            "refinement_layout": [
                "fixed_fejer_angular_observation_refinement.py",
                "52b13e57f058001a5f1640809ae09995c793aadb2ab8eaa54e9c5ab9619d2b21"
            ]
        },
        "refinement_pure_key": "angular_observation",
        "layout_role": "angular_observation"
    },
    "M320": {
        "family": "M320",
        "report_schema": "complete-fixed-fejer-frequency-refined-immutable-point-SO3-QP-v1",
        "pure_schema": "actual-fixed-fejer-frequency-refined-immutable-point-SO3-readout-v1",
        "normal_schema": "complete-fixed-fejer-frequency-refined-immutable-point-normal-layer-v1",
        "base_schema": "complete-fixed-fejer-frequency-refined-frozen-reference-so3-meridian-v1",
        "current_M": 320,
        "current_N": 2048,
        "reference_M": 160,
        "reference_N": 2048,
        "J": 923,
        "K": 3,
        "n": 962,
        "free_size": 2661210,
        "source_role_count": 128,
        "source_registry_identity_sha256": "a25ffd18c4a8286c904ca186d820e8939f71337dd4fe41c365d6202bf291f608",
        "pins": {
            "reader": [
                "read_fixed_fejer_frequency_so3_report.py",
                "b79c352d11b41de5384016f103c07db7abc2a41bf438ef92fe20b8a9b43e75bb"
            ],
            "driver": [
                "fullclosed_fixed_fejer_frequency_so3_qp.py",
                "fff956cc086c8f69c7de87c2d9117792b6b1d5e1de853e59a992fb67e04b4e51"
            ],
            "packets": [
                "fixed_fejer_frequency_root_packets.py",
                "767be252b02b0f92ee1a7229881cfa693a2d4e73f48f6a703fe0c21340c59b78"
            ],
            "normal": [
                "fixed_fejer_frequency_normal_lift.py",
                "60769d4999af17f6dc904400e414e3f34ec1000bd84529ad168dca67f6889b5f"
            ],
            "base": [
                "fixed_fejer_frequency_meridian_operator.py",
                "f7058f9c9d3f02292b738b360b116062b60bcf07907286acb42346eb431bdf9a"
            ],
            "field_binding": [
                "fixed_fejer_frequency_source_binding.py",
                "caf16fbc87ef618ddae5ba42616d9bbe136beac6d32487224073ac6958c4d3c0"
            ],
            "refinement_layout": [
                "fixed_fejer_frequency_layout.py",
                "67c5503e8df036aa1468a3df2f395f5a33c91c4309520fbb8862b39c2495a251"
            ]
        },
        "refinement_pure_key": "frequency_refinement_binding",
        "layout_role": "frequency_layout"
    }
}


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()


def copy_json(value):
    return json.loads(json.dumps(value,allow_nan=False))


def sha(path):
    digest=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1<<20),b""):
            digest.update(block)
    return digest.hexdigest()


def file_record(path):
    path=Path(path).resolve()
    return dict(path=str(path),bytes=path.stat().st_size,sha256=sha(path))


def family_for_driver(digest,expected_family=None):
    matches=[value for value in FAMILIES.values() if value["pins"]["driver"][1]==digest]
    if len(matches)!=1:
        raise ValueError("Only the two explicitly pinned complete N4096/M320 field sources are accepted")
    family=copy_json(matches[0])
    if expected_family is not None and family["family"]!=expected_family:
        raise ValueError("The explicitly requested complete refinement family differs from the actual report")
    return family


def input_pins(family):
    if not isinstance(family,dict) or FAMILIES.get(family.get("family"))!=family:
        raise ValueError("Use the complete immutable family definition, without altered layout or sources")
    result=copy_json(COMMON_PINS)
    result.update(copy_json(family["pins"]))
    result["refinement_binding"]=[SOURCE_NAME,sha(__file__)]
    return result


def family_from_actual(actual):
    family=family_for_driver(actual.get("actual_driver_sha256"))
    expected=input_pins(family)
    if (actual.get("complete_pure_reader_sha256")!=family["pins"]["reader"][1]
            or actual.get("source_sha256_by_role")!={key:value[1] for key,value in expected.items()}
            or actual.get("complete_accurate_input_source_pins")!=expected):
        raise ValueError("The complete accurate-input source table or actual family changed")
    return family,expected


def source_pins(path):
    raw=Path(path).read_bytes()
    if len(raw)>=100000:
        raise ValueError("A complete source body must remain below the published small-source limit")
    tree=ast.parse(raw)
    values=[node.value for node in tree.body if isinstance(node,ast.Assign)
        and len(node.targets)==1 and isinstance(node.targets[0],ast.Name)
        and node.targets[0].id=="SOURCE_PINS"]
    if len(values)!=1:
        raise ValueError("The exact whole driver must contain its single literal complete source registry")
    result=ast.literal_eval(values[0])
    if not isinstance(result,dict):
        raise ValueError("The entire source registry must be an explicit mapping")
    return result


def checked_source(directory,pair,files):
    name,digest=pair
    path=Path(directory)/name
    record=file_record(path)
    if record["sha256"]!=digest or record["bytes"]>=100000:
        raise ValueError("Changed complete bound source: "+str(path))
    files.verify(record)
    return path


def module(directory,pair,files):
    path=checked_source(directory,pair,files)
    name=("_complete_refined_fee_source_"+pair[1]+"_"+
        hashlib.sha256(str(path.resolve()).encode()).hexdigest()[:16])
    result=sys.modules.get(name)
    if result is None:
        spec=importlib.util.spec_from_file_location(name,path)
        result=importlib.util.module_from_spec(spec)
        sys.modules[name]=result
        spec.loader.exec_module(result)
    if (sha(result.__file__)!=pair[1]
            or Path(result.__file__).resolve()!=path.resolve()):
        raise ValueError("The loaded complete source is not the exact recorded file")
    checked_source(directory,pair,files)
    return result


def read_complete_report(repo,report_record,files,expected_family=None):
    """Invoke the unmodified complete family-specific pure reader on actual bytes."""
    path=files.verify(report_record)
    content=Path(path).read_bytes()
    if len(content)!=report_record["bytes"] or hashlib.sha256(content).hexdigest()!=report_record["sha256"]:
        raise ValueError("The entire actual report changed during capture")
    report=json.loads(content)
    family=family_for_driver(report.get("source_sha256"),expected_family)
    directory=Path(repo).resolve()/TOPIC/SCRIPT_DIRECTORY
    reader=module(directory,family["pins"]["reader"],files)
    if sha(reader.read_report.__code__.co_filename)!=family["pins"]["reader"][1]:
        raise ValueError("Use the actual complete selected-family report reader")
    pure=reader.read_report(Path(repo).resolve(),str(Path(path).resolve()),verify_final_bundle=False)
    files.verify(report_record)
    if (pure.get("report_sha256")!=report_record["sha256"]
            or pure.get("report_bytes")!=report_record["bytes"]
            or pure.get("report_path")!=str(Path(path).resolve())):
        raise ValueError("The full reader did not consume the same immutable report")
    return report,pure,family


def validate_report(report,pure,*,repo,files,expected_family=None):
    """Bind the full declared family; use only its own explicit layout validator."""
    family=family_for_driver(report.get("source_sha256"),expected_family)
    if (report.get("schema")!=family["report_schema"]
            or pure.get("schema")!=family["pure_schema"]
            or pure.get("actual_driver_sha256")!=family["pins"]["driver"][1]
            or pure.get("reader_sha256")!=family["pins"]["reader"][1]):
        raise ValueError("Do not relabel a baseline, another refinement or a progress file as a complete field report")
    directory=Path(repo).resolve()/TOPIC/SCRIPT_DIRECTORY
    driver=checked_source(directory,family["pins"]["driver"],files)
    registry=source_pins(driver)
    if (len(registry)!=family["source_role_count"]
            or canonical(registry)!=family["source_registry_identity_sha256"]
            or report.get("source_sha256_by_role")!={key:value[1] for key,value in registry.items()}):
        raise ValueError("All 128 exact current and historical whole-source roles are required")
    topic=Path(repo).resolve()/TOPIC
    for role,pair in registry.items():
        if (not isinstance(pair,(tuple,list)) or len(pair)!=2
                or not isinstance(pair[0],str) or not isinstance(pair[1],str)):
            raise ValueError("The complete source-role pair changed: "+role)
        path=topic/pair[0]
        record=file_record(path)
        if record["sha256"]!=pair[1]:
            raise ValueError("A full declared scientific source differs: "+role)
        files.verify(record)
    parent=checked_source(directory,PARENT_DRIVER,files)
    original=source_pins(parent)
    if len(original)!=110 or not {tuple(v) for v in original.values()}.issubset({tuple(v) for v in registry.values()}):
        raise ValueError("Retain every whole path/SHA pair of the original 110-role Fejer family")
    pins=input_pins(family)
    for pair in pins.values():
        checked_source(directory,pair,files)
    selected={"packets":"root_packets","normal":"endpoint","base":"meridian",
        "field_binding":"analytic_J3_binding","refinement_layout":family["layout_role"]}
    for name,role in selected.items():
        if tuple(registry[role])!=(SCRIPT_DIRECTORY+"/"+pins[name][0],pins[name][1]):
            raise ValueError("A current physical or layout role was confused with a historical alias")
    model=report["representation"]
    base=model["base_complete_model"]
    reference=base["complete_axisymmetric_reference_model"]
    if (canonical(model)!=report.get("model_identity_sha256")
            or pure.get("model_identity_sha256")!=report.get("model_identity_sha256")
            or model.get("schema")!=family["normal_schema"]
            or model.get("source_sha256")!=pins["normal"][1]
            or base.get("schema")!=family["base_schema"]
            or base.get("source_sha256")!=pins["base"][1]
            or canonical(base)!=model.get("base_model_identity_sha256")
            or reference.get("M")!=160 or reference.get("J")!=923
            or reference.get("source_sha256")!=COMMON_PINS["reference"][1]):
        raise ValueError("Bind the entire current normal/base model and unchanged complete M160/J923 reference")
    if (report.get("M")!=family["current_M"] or report.get("N")!=family["current_N"]
            or report.get("J")!=923 or report.get("original_variables")!=family["free_size"]
            or base.get("M")!=family["current_M"] or base.get("J")!=923
            or model.get("M")!=family["current_M"] or model.get("J")!=923):
        raise ValueError("The actual current space differs from its explicitly declared full refinement")
    for key in ("mesh_sha256","fixed_chart_core_sha256","fixed_core_first3",
            "fixed_scalar_metric_identity_sha256","fixed_scalar_profile_definition"):
        if base.get(key)!=reference.get(key):
            raise ValueError("The fixed reference/base identity differs beyond the declared current layout: "+key)
    if (model.get("normal_stage_count")!=32 or model.get("implicit_control_dimension")!=6
            or model.get("normal_increment_dimension")!=3
            or model.get("complete_first_angular_implicit_dimension")!=192
            or model.get("complete_second_angular_implicit_dimension")!=288
            or report.get("saved_parent_Phi_used_as_current_baseline") is not False):
        raise ValueError("Keep all thirty-two stages, all six controls and freshly read current field values")
    bound=module(directory,pins["field_binding"],files)
    role_shas={key:value[1] for key,value in registry.items()}
    bound.validate_current_model(model,roles=role_shas,source_directory=directory)
    if family["family"]=="N4096":
        refinement=bound.angular_observation_binding(report,roles=role_shas,source_directory=directory)
        if (report.get("reference_full_N")!=2048 or report.get("current_full_N")!=4096
                or base.get("reference_full_N")!=2048 or base.get("current_full_N")!=4096):
            raise ValueError("Only the complete observer changes to N4096")
    elif family["family"]=="M320":
        refinement=bound.frequency_refinement_binding(report,roles=role_shas,source_directory=directory)
        if (report.get("reference_M")!=160 or report.get("current_M")!=320
                or base.get("reference_M")!=160 or base.get("current_M")!=320):
            raise ValueError("The frozen material chart stays M160 while the entire current space is M320")
    else:
        raise ValueError("No combined, radial or undeclared refinement is accepted")
    if pure.get(family["refinement_pure_key"])!=refinement:
        raise ValueError("The complete original family reader and source/model layout validator disagree")
    transfer=pure.get("material_envelope_transfer")
    if not isinstance(transfer,dict):
        raise ValueError("Keep the entire current transfer, typed history and unresolved-peer interpretation")
    # The unmodified family reader above already re-reads the real prior-final
    # 13-member bundle when that mode is used. An independent point cannot be
    # reclassified as a parent, and no hypothetical parent is synthesized here.
    layout=dict(reference_M=160,current_M=family["current_M"],J=923,K=3,
        reference_full_N=2048,current_full_N=family["current_N"],
        rotation_slot_count=family["n"],current_free_size=family["free_size"],
        current_free_core=family["current_M"]-3,
        fixed_zero_radial_slots=[0,2766,2767],
        omega_blocks=[dict(component="x",basis="odd-sine",start=0,count=family["current_M"]+1),
            dict(component="y",basis="odd-cosine",start=family["current_M"]+1,count=family["current_M"]+1),
            dict(component="z",basis="even-sine",start=2*(family["current_M"]+1),count=family["current_M"])])
    result=dict(schema=SCHEMA,source_sha256=sha(__file__),family=family["family"],
        actual_driver_sha256=pins["driver"][1],actual_reader_sha256=pins["reader"][1],
        actual_normal_source_sha256=pins["normal"][1],actual_base_source_sha256=pins["base"][1],
        actual_field_binding_source_sha256=pins["field_binding"][1],
        complete_model_identity_sha256=canonical(model),complete_base_model_identity_sha256=canonical(base),
        complete_reference_model_identity_sha256=canonical(reference),
        complete_source_registry_identity_sha256=canonical(registry),complete_source_role_count=128,
        all_original_110_path_and_source_pairs_retained=True,layout=layout,
        complete_current_refinement_binding=copy_json(refinement),
        complete_current_coordinate_norm=copy_json(report["coordinate_norm"]),
        complete_pure_current_coordinate_norm=copy_json(pure["coordinate_norm"]),
        complete_material_envelope_transfer=copy_json(transfer),
        complete_prior_final_seed=copy_json(pure.get("prior_envelope_final_variable_seed")),
        current_model_and_norm_not_relabelled_as_reference=True,
        existing_13_member_parent_validation_retained_in_original_reader=True,
        complete_typed_history_and_unresolved_peer_obligations_retained=True,
        previous_point_values_or_certificates_inherited=False,
        no_new_field_root_J_or_scientific_integral_evaluation=True)
    checked_source(directory,family["pins"]["driver"],files)
    return result


def validate_actual_binding(actual,outer,*,repo,files):
    family,pins=family_from_actual(actual)
    report,pure,selected=read_complete_report(repo,actual["scientific_report"],files,family["family"])
    if report!=outer or report.get("representation")!=actual.get("complete_model"):
        raise ValueError("The complete original scientific report or selected mathematical model changed")
    result=validate_report(report,pure,repo=repo,files=files,expected_family=family["family"])
    if result!=actual.get("refinement_family_binding"):
        raise ValueError("The full source/layout/norm/transfer binding changed since accurate evaluation")
    if (actual.get("model_identity_sha256")!=result["complete_model_identity_sha256"]
            or actual.get("actual_reference_model_identity_sha256")!=result["complete_reference_model_identity_sha256"]):
        raise ValueError("The accurate input is not the complete same refined field")
    return dict(family=family,input_pins=pins,binding=result)
