#!/usr/bin/env python3
"""Whole-source binding for the complete fixed-Fejer J1845 accurate field.

The fixed reference retains M160/J923/N2048. The current full point has J1845
and all 1844 exact-affine Hermite cells. The complete original radial reader,
source/model/history and observation-union validators remain authoritative.
No prior point, numerical field value or working-word error is inferred.
"""
from __future__ import annotations
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

SCHEMA = "complete-fixed-fejer-J1845-accurate-field-family-binding-v1"
SOURCE_NAME = "fixed_fejer_J1845_fee_source_binding.py"
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
    "J1845": {
        "family": "J1845",
        "report_schema": "complete-fixed-fejer-J1845-immutable-point-material-envelope-SO3-QP-v1",
        "pure_schema": "actual-fixed-fejer-J1845-immutable-point-envelope-SO3-readout-v1",
        "normal_schema": "complete-fixed-fejer-radial-refined-immutable-point-normal-layer-v1",
        "base_schema": "complete-fixed-fejer-radial-bisection-frozen-reference-so3-meridian-with-core-lift-v1",
        "current_M": 160,
        "current_N": 2048,
        "reference_M": 160,
        "reference_N": 2048,
        "reference_J": 923,
        "J": 1845,
        "K": 3,
        "n": 482,
        "free_size": 2666582,
        "source_role_count": 131,
        "source_registry_identity_sha256": "86c0f23b144cc9567f8809dd517f929b290da2a4f032f140e8ee94b2d44797e4",
        "pins": {
            "reader": [
                "read_fixed_fejer_radial_so3_report.py",
                "4ea3b45ecce7e02c7e911a3bfd6f33110b422173cc4a377ae63845398b6a80a5"
            ],
            "driver": [
                "fullclosed_fixed_fejer_radial_so3_qp.py",
                "97ae6ab8a2a19a07b134efc611b442d9e9113ca0b68c0cd322a45ec175d0f8fd"
            ],
            "packets": [
                "fixed_fejer_radial_immutable_root_packets.py",
                "8a6b68a63c25a48a1bae2718161b0346b197012cedec4f43e7cc92b0c4cf5b77"
            ],
            "normal": [
                "fixed_fejer_radial_normal_lift.py",
                "543ef57246c45f923133d121e414ca90cbba44e1ed9e4056b410f80ab5f2064f"
            ],
            "base": [
                "fixed_fejer_radial_refined_meridian_operator.py",
                "78ded2682f5a42bc44a1939e9d814eec17254d1385dfe08a545d6aee109892ef"
            ],
            "field_binding": [
                "fixed_fejer_radial_source_and_report_binding.py",
                "f890cb36952ed18543d63500b7e19d970cb341d73f5bc4f36c64e3e51fb02571"
            ],
            "refinement_layout": [
                "fixed_fejer_radial_bisection_layout.py",
                "a31d80a953722cc3644f793e4a28a372d980f6d0af7c8d98402f5f4739e3b5cf"
            ],
            "affine_reference": [
                "fixed_fejer_exact_affine_supported_reference.py",
                "622e50feab2dcd65b0191a880375a6fb064be2382a8fd576f09e08a69ac6fd95"
            ],
            "radial_observations": [
                "fixed_fejer_complete_dyadic_radial_observations.py",
                "a89cb4f660f56ccc49e6f59191730aacc414cb36714ec64c2061784d3215f07d"
            ],
            "radial_Q": [
                "fixed_fejer_radial_literal_zero_moment_input.py",
                "2e0c056652b10b4158bc74ec1fd2cdae54e05fb439154a462d6f1e4eb717428c"
            ]
        },
        "refinement_pure_key": "radial_refinement",
        "layout_role": "radial_layout"
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
        raise ValueError("Only the explicitly pinned complete J1845 field source is accepted")
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
        raise ValueError("All 131 exact current and historical whole-source roles are required")
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
        "field_binding":"analytic_J3_binding","refinement_layout":family["layout_role"],
        "affine_reference":"radial_affine_reference","radial_observations":"radial_observations",
        "radial_Q":"new_moment_input"}
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
            or report.get("J")!=1845 or report.get("original_variables")!=family["free_size"]
            or base.get("M")!=160 or base.get("J")!=1845
            or model.get("M")!=160 or model.get("J")!=1845):
        raise ValueError("The actual current space differs from its explicitly declared full refinement")
    for key in ("fixed_chart_core_sha256","fixed_core_first3",
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
    refinement=bound.radial_refinement_binding(report,roles=role_shas,source_directory=directory)
    radial=base["radial_layout_definition"]
    layout_module=module(directory,pins["refinement_layout"],files)
    if (layout_module.validate_definition(radial)!=base.get("radial_layout_identity_sha256")
            or radial.get("complete_original_reference_model")!=reference
            or radial.get("reference_J")!=923 or radial.get("current_J")!=1845
            or base.get("reference_J")!=923 or base.get("current_J")!=1845
            or report.get("reference_J")!=923 or report.get("current_J")!=1845
            or base.get("reference_mesh_sha256")!=reference.get("mesh_sha256")
            or base.get("mesh_sha256")!=radial.get("current_mesh_sha256")
            or model.get("mesh_sha256")!=base.get("mesh_sha256")
            or base.get("reference_seed_and_material_chart_unchanged") is not True):
        raise ValueError("Keep the entire accurate current J1845 and frozen reference J923 domains separate")
    observation_files=report.get("complete_radial_input_files")
    required_files={"current-symbolic-nodes.json","complete-a-boxes.json",
        "complete-parent-address-transfer.json","observation-definition.json",
        "complete-dyadic-observations.npz"}
    if (not isinstance(observation_files,dict)
            or observation_files.get("schema")!="complete-same-target-dyadic-observation-files-v1"
            or observation_files.get("definition_identity_sha256")!=base["radial_observation_identity_sha256"]
            or set(observation_files.get("files",{}))!=required_files
            or observation_files.get("raw_stays_on_runner") is not True
            or observation_files.get("scientific_input_precision_status_not_upgraded") is not True):
        raise ValueError("Retain all five exact actual fine and original observation-carrier files")
    for record in observation_files["files"].values():
        files.verify(record)
    if pure.get(family["refinement_pure_key"])!=refinement:
        raise ValueError("The complete original family reader and source/model layout validator disagree")
    transfer=pure.get("material_envelope_transfer")
    if not isinstance(transfer,dict):
        raise ValueError("Keep the entire current transfer, typed history and unresolved-peer interpretation")
    # The unmodified family reader above already re-reads the real prior-final
    # 13-member bundle when that mode is used. An independent point cannot be
    # reclassified as a parent, and no hypothetical parent is synthesized here.
    layout=dict(reference_M=160,current_M=160,reference_J=923,current_J=1845,J=1845,K=3,
        reference_full_N=2048,current_full_N=family["current_N"],
        rotation_slot_count=family["n"],current_free_size=family["free_size"],
        current_free_core=family["current_M"]-3,
        fixed_zero_radial_slots=[0,5532,5533],
        accurate_current_cell_count=1844,accurate_reference_cell_count=922,
        complete_radial_layout_identity_sha256=base["radial_layout_identity_sha256"],
        original_node_definition_identity_sha256=radial["original_node_definition_identity_sha256"],
        current_node_definition_identity_sha256=radial["current_node_definition_identity_sha256"],
        original_current_mesh_sha256=base["mesh_sha256"],
        frozen_reference_mesh_sha256=reference["mesh_sha256"],
        omega_blocks=[dict(component="x",basis="odd-sine",start=0,count=family["current_M"]+1),
            dict(component="y",basis="odd-cosine",start=family["current_M"]+1,count=family["current_M"]+1),
            dict(component="z",basis="even-sine",start=2*(family["current_M"]+1),count=family["current_M"])])
    result=dict(schema=SCHEMA,source_sha256=sha(__file__),family=family["family"],
        actual_driver_sha256=pins["driver"][1],actual_reader_sha256=pins["reader"][1],
        actual_normal_source_sha256=pins["normal"][1],actual_base_source_sha256=pins["base"][1],
        actual_field_binding_source_sha256=pins["field_binding"][1],
        complete_model_identity_sha256=canonical(model),complete_base_model_identity_sha256=canonical(base),
        complete_reference_model_identity_sha256=canonical(reference),
        complete_source_registry_identity_sha256=canonical(registry),complete_source_role_count=131,
        all_original_110_path_and_source_pairs_retained=True,layout=layout,
        complete_current_refinement_binding=copy_json(refinement),
        complete_current_radial_input_files=copy_json(observation_files),
        current_exact_affine_queries_not_rounded_into_reference_cells=True,
        all_original_new_Gauss_and_tagged_history_roles_retained=True,
        working_radial_carriers_not_treated_as_accurate_node_values=True,
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
