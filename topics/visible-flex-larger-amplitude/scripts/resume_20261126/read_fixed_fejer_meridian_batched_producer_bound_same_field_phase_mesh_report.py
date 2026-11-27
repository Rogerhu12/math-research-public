#!/usr/bin/env python3
"""Pure complete fixed Fejer same-field mesh provenance and raw-byte readout.

This reader imports only stdlib-level mesh/input modules and the original
source-bound pure report reader. It never constructs q, calls F/J/root,
resolves a chart, creates a mesh, or recomputes a numerical criterion.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import sys

SCHEMA = "actual-fixed-fejer-meridian-batched-producer-bound-complete-same-field-closed-phase-mesh-refinement-v1"
MAIN_NAME = "fixed_fejer_meridian_batched_producer_bound_complete_same_field_phase_meshes.py"
MAIN_SHA = "b3991da8585b553a6c3133da806fafa4903e2c01087634c18ee168e6718bc4d7"
TOPIC = "topics/visible-flex-larger-amplitude"
SCRIPT = "scripts/resume_20261126"


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda:stream.read(1<<20),b""):
            h.update(part)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()


def record(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)


def actual(record_value):
    if (not isinstance(record_value,dict) or set(record_value)!={"path","sha256","bytes"}
            or record(record_value["path"])!=record_value):
        raise ValueError("A complete actual input or output changed")
    return Path(record_value["path"])


def load(name,path,digest):
    if sha(path)!=digest:
        raise ValueError("A complete pure-reader dependency changed")
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    if sha(path)!=digest:
        raise ValueError("A whole source changed while loading")
    return module


def pins(path):
    tree=ast.parse(Path(path).read_text())
    value=[n.value for n in tree.body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id=="SOURCE_PINS" for t in n.targets)]
    if len(value)!=1:
        raise ValueError("Keep the one complete source registry")
    return ast.literal_eval(value[0])


def read_json(record_value):
    path=actual(record_value)
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=record_value["sha256"] or len(raw)!=record_value["bytes"]:
        raise ValueError("An immutable complete JSON changed while reading")
    value=json.loads(raw)
    actual(record_value)
    return value


def read_npy_header(record_value,shape):
    path=actual(record_value)
    with path.open("rb") as f:
        if f.read(6)!=b"\x93NUMPY":
            raise ValueError("Use the actual complete NumPy array, not a relabelled file")
        version=tuple(f.read(2))
        if version==(1,0):
            length=struct.unpack("<H",f.read(2))[0]
        elif version in ((2,0),(3,0)):
            length=struct.unpack("<I",f.read(4))[0]
        else:
            raise ValueError("Unsupported actual NPY format")
        if length>65536:
            raise ValueError("An actual numerical array needs a bounded complete NPY header")
        header=ast.literal_eval(f.read(length).decode("utf-8" if version==(3,0) else "latin1"))
        if (set(header)!={"descr","fortran_order","shape"} or header["descr"]!="<f8"
                or header["fortran_order"] is not False or list(header["shape"])!=shape):
            raise ValueError("The whole actual six-jet array layout changed")
        count=1
        for v in shape:
            if type(v)is not int or v<1:
                raise ValueError("Keep complete positive actual array dimensions")
            count*=v
        if f.tell()+8*count!=record_value["bytes"]:
            raise ValueError("The full actual NPY payload length differs")
    return dict(shape=shape,dtype="float64",whole_file_sha256=record_value["sha256"])


def read_ply_header(item,*,preview_limit=None):
    path=actual(item["file"])
    with path.open("rb") as f:
        data=bytearray()
        while not data.endswith(b"end_header\n"):
            byte=f.read(1)
            if not byte or len(data)>=8192:
                raise ValueError("The actual standalone PLY header is incomplete or unbounded")
            data+=byte
    text=data.decode("ascii")
    lines=text.splitlines()
    if lines[:2]!=["ply","format binary_little_endian 1.0"]:
        raise ValueError("Use the exact documented complete binary PLY format")
    vertices=[int(v.split()[-1]) for v in lines if v.startswith("element vertex ")]
    faces=[int(v.split()[-1]) for v in lines if v.startswith("element face ")]
    kind="double" if item["coordinate_bits"]==64 else "float"
    if (vertices!=[item["vertex_count"]] or faces!=[item["triangle_count"]]
            or lines.count("property "+kind+" x")!=1
            or lines.count("property "+kind+" y")!=1
            or lines.count("property "+kind+" z")!=1
            or lines.count("property list uchar int vertex_indices")!=1):
        raise ValueError("The complete actual mesh header differs from the reported topology")
    size=len(data)+item["vertex_count"]*3*(item["coordinate_bits"]//8)+item["triangle_count"]*13
    if (item["coordinate_bits"] not in (32,64) or item["bytes"]!=size
            or item["file"]["bytes"]!=size or item["triangle_count"]!=2*item["vertex_count"]-4
            or (preview_limit is not None and size>=preview_limit)):
        raise ValueError("The complete actual mesh counts or explicit preview byte limit differ")
    for key in ("full_belt_and_both_cartesian_marked_caps","cuff_indices_shared_with_caps",
                "central_reflection_indices_shared","exact_port_formula_used_for_mesh_boundary_vertices",
                "working_field_values_not_silently_relabelled_as_exact_ports"):
        if item.get(key)is not True:
            raise ValueError("The actual mesh omitted an explicit whole-surface/port responsibility")
    if item.get("geometric_self_intersection_or_reach_certified")is not False:
        raise ValueError("A finite closed mesh is not a reach or embedding certificate")
    return dict(file=item["file"],vertices=item["vertex_count"],triangles=item["triangle_count"],
        physical_t_exact=item["physical_t_exact"],coordinate_bits=item["coordinate_bits"],
        port_rounding_projection_maximum=item["port_rounding_projection_maximum"],
        coordinate_serialization_error_maximum=item["coordinate_serialization_error_maximum"])


def read_report(repo,report_path):
    repo=Path(repo).resolve()
    topic=repo/TOPIC
    main_path=topic/SCRIPT/MAIN_NAME
    if sha(main_path)!=MAIN_SHA:
        raise ValueError("The whole actual mesh consumer source differs")
    source_pins=pins(main_path)
    if len(source_pins)!=144:
        raise ValueError("Keep all 137 scientific roles and seven mesh/input/evidence source roles")
    main=load("_pure_complete_actual_mesh_entry",main_path,MAIN_SHA)
    report_record=record(report_path)
    report=read_json(report_record)
    if (report.get("schema")!=SCHEMA or report.get("source_sha256")!=MAIN_SHA
            or report.get("source_sha256_by_role")!={k:v[1] for k,v in source_pins.items()}):
        raise ValueError("The actual complete mesh report/source family differs")
    for role,(relative,digest) in source_pins.items():
        expected=record(topic/relative)
        stored=report["source_records"][role]
        actual(stored)
        if (expected["sha256"]!=digest or stored["sha256"]!=digest
                or expected["bytes"]!=stored["bytes"]):
            raise ValueError("A complete original or mesh source role changed: "+role)
    answer=main.public_summary(report)
    answer.update(pure_reader_source_sha256=sha(__file__),actual_report=report_record,
        numerical_field_or_mesh_calls_by_reader=0)
    binding=report.get("field_binding")
    if binding is not None:
        if canonical(binding)!=report.get("field_binding_identity_sha256"):
            raise ValueError("The complete actual field reconstruction identity differs")
        immutable=binding.get("immutable_consumed_file_records")
        if (not isinstance(immutable,list) or not immutable
                or len({v["path"] for v in immutable})!=len(immutable)):
            raise ValueError("Retain the whole immutable consumed input inventory")
        for expected in immutable:
            actual(expected)
        payload=read_json(report["field_binding_file"])
        if (payload.get("definition")!=binding
                or payload.get("definition_identity_sha256")!=canonical(binding)):
            raise ValueError("The actual complete binding file differs from this report")
        raw=read_json(binding["scientific_report_capture"]["captured_copy"])
        original_reader=load("_pure_original_fixed_fejer_scientific_report",
            topic/source_pins["original_fixed_fejer_reader"][0],source_pins["original_fixed_fejer_reader"][1])
        pure=original_reader.read_report(repo,
            binding["scientific_report_capture"]["captured_copy"]["path"],verify_final_bundle=False)
        if (pure["report_sha256"]!=report["captured_scientific_report_sha256"]
                or raw["representation"]!=binding["complete_model"]
                or raw["model_identity_sha256"]!=binding["model_identity_sha256"]
                or raw["independent_fixed_target_definition_identity_sha256"]
                    !=binding["fixed_target_definition_identity_sha256"]
                or raw["coordinate_norm"]!=binding["complete_original_coordinate_norm"]
                or raw["working_evaluation"]!=binding["complete_original_working_evaluation"]
                or raw["source_commit"]!=binding["actual_source_commit"]
                or raw["github_run_id"]!=binding["actual_scientific_run_id"]
                or raw["workflow_trigger_commit"]!=binding["actual_workflow_trigger_commit"]):
            raise ValueError("The actual original scientific field and mesh input changed scope")
        command=read_json(binding["original_complete_command"])
        if (command["command"]!=binding["original_full_argv"]
                or command.get("github_run_id")!=binding["actual_scientific_run_id"]
                or command.get("source_sha256")!=source_pins["original_fixed_fejer_launcher"][1]
                or command.get("driver_sha256")!=source_pins["original_fixed_fejer_driver"][1]
                or binding["original_launcher_numerical_environment"]!={k:"1"
                    for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")}):
            raise ValueError("Keep every original actual scientific command argument")
        binder=load("_pure_complete_fixed_fejer_mesh_input",
            topic/source_pins["mesh_input"][0],source_pins["mesh_input"][1])
        inventory=binder.VerifiedFiles()
        for item in immutable:
            inventory.verify(item)
        scoped=binder.bind_actual_fixed_reference(raw,pure,repo,inventory)
        if (scoped["entry"]!=binding["complete_actual_fixed_reference_input_binding"]
                or scoped["exact_fixed_target_identity_sha256"]!=binding["fixed_target_definition_identity_sha256"]
                or scoped["actual_reference_model_identity_sha256"]!=binding["reference_model_identity_sha256"]
                or scoped["fixed_chart_core_sha256"]!=binding["fixed_chart_core_sha256"]
                or scoped["mathematical_target_identity_sha256"]!=binding["mathematical_target_identity_sha256"]
                or scoped["complete_current_input_files"]!=binding["complete_six_actual_inputs"]):
            raise ValueError("The complete actual fixed input binding changed after mesh construction")
        copies=binding["original_complete_source_copy_relations"]
        if set(copies.get("complete_source_roles",{}))!=set(binding["source_roles"]):
            raise ValueError("Keep every full original-to-current scientific source copy relationship")
        for relation in [copies["driver"],copies["launcher"],*copies["complete_source_roles"].values()]:
            original,current=relation["original"],relation["current"]
            if (relation.get("complete_sha256_and_bytes_equal")is not True
                    or relation.get("original_path_identity_preserved")is not True
                    or original["sha256"]!=current["sha256"] or original["bytes"]!=current["bytes"]):
                raise ValueError("An original source path was relabelled without complete byte equality")
            inventory.verify(original);inventory.verify(current)
        if report.get("optional_closed_phase_evidence")is not None:
            rebound=binder.bind_closed_phase_evidence(report.get("optional_closed_phase_report_argument"),
                report.get("expected_closed_phase_report_sha256"),binding=binding,
                repo=Path(copies["current_repository"]),used=inventory)
            if rebound!=report["optional_closed_phase_evidence"]:
                raise ValueError("The exact same-point optional closed report changed")
        inventory.recheck()
        point=binding["point"]
        if point["mode"]=="actual-complete-thirteen-member-final":
            actual(point["checkpoint"])
            if (raw.get("complete")is not True
                    or raw["final_bundle_sha256"]!=point["checkpoint"]["sha256"]
                    or raw["final_geometry"]["current_full_point_sha256"]
                        !=point["current_full_point_sha256"]):
                raise ValueError("The current mesh point is not its actual final")
        elif point["mode"]=="actual-immutable-complete-point-snapshot":
            snapshot=read_json(point["snapshot_file"])
            if (snapshot["snapshot_identity_sha256"]!=point["snapshot_identity_sha256"]
                    or snapshot["definition"]["current_full_point_sha256"]
                        !=point["current_full_point_sha256"]
                    or not any(x["snapshot_identity_sha256"]==point["snapshot_identity_sha256"]
                        and x["snapshot_file"]==point["snapshot_file"]
                        and x.get("summary",{}).get("all_required_angle_roots_recorded") is True
                        for x in raw["normal_root_packets"]["snapshots"])):
                raise ValueError("The actual complete mesh point is not in its genuine immutable input report")
        else:
            raise ValueError("No unrecorded or reset initial point may be substituted")
        if (binding["point_sha256"]!=point["current_full_point_sha256"]
                or binding["M"]!=160 or binding["J"]!=923 or binding["N"]!=2048
                or binding["normal_stages"]!=32
                or binding["current_scalar_reconstruction"]["actual_current_leaf_count"]!=2218
                or binding["current_scalar_reconstruction"]["historical_2397_table_used_as_current"]is not False):
            raise ValueError("The original complete finite field or exact target changed")
        snapshot_record=binding.get("actual_snapshot_file")
        if snapshot_record is None:
            if binding.get("actual_snapshot_identity_sha256")is not None:
                raise ValueError("A missing original snapshot cannot acquire a synthetic identity")
        else:
            snapshot=read_json(snapshot_record)
            if (snapshot.get("snapshot_identity_sha256")!=binding.get("actual_snapshot_identity_sha256")
                    or snapshot["definition"]["current_full_point_sha256"]!=binding["point_sha256"]
                    or not any(item.get("snapshot_identity_sha256")==binding["actual_snapshot_identity_sha256"]
                        and item.get("snapshot_file")==snapshot_record
                        and item.get("summary",{}).get("all_required_angle_roots_recorded") is True
                        for item in raw["normal_root_packets"]["snapshots"])):
                raise ValueError("The optional accurate evidence must use the same actual original snapshot")
        packets=load("_pure_mesh_actual_root_packets",topic/source_pins["root_packets"][0],
            source_pins["root_packets"][1])
        if report.get("normal_root_packets")is not None:
            answer["actual_mesh_packet_validation"]=packets.validate_metadata(
                report["normal_root_packets"],model=binding["complete_model"],
                operator_source_sha256=source_pins["endpoint"][1],caller_source_sha256=MAIN_SHA,
                source_sha256_by_role={k:v[1] for k,v in source_pins.items()},
                reread_packets=True,reread_arrays=True)
    if report.get("complete")is True:
        if (binding is None or report.get("all_complete_source_and_input_bytes_rechecked")is not True
                or report.get("all_complete_declared_output_bytes_rechecked")is not True
                or report.get("closed_isometry_accepted")is not False
                or report.get("optional_closed_phase_evidence")is None):
            raise ValueError("A complete numerical readout must preserve its exact input/output scope")
        result=report["field_evaluation"]
        shape=result["shape"]
        if (len(shape)!=3 or shape[-1]!=3
                or shape[0]!=922*report["requested_levels"][-1]["radial"]+1
                or shape[1]!=report["requested_levels"][-1]["angles"]
                or result["evaluated_field_points"]!=shape[0]*shape[1]
                or result["complete_full_circle"]is not True or result["all_original_cells"]is not True
                or result["continuous_error_certified"]is not False):
            raise ValueError("The complete original radial domain or full circle was truncated")
        if set(report["complete_sixjet_files"])!={"F","Fs","Ftheta","Fss","Fstheta","Fthetatheta"}:
            raise ValueError("Retain all six actual physical-material-coordinate jets")
        for expected in report["complete_sixjet_files"].values():
            read_npy_header(expected,shape)
        grid=read_json(report["material_grid"])
        if (grid["arrays_file"]!=report["material_grid_arrays"]
                or grid["actual_point_sha256"]!=binding["point_sha256"]
                or grid["model_identity_sha256"]!=binding["model_identity_sha256"]
                or grid["fixed_target_definition_identity_sha256"]!=binding["fixed_target_definition_identity_sha256"]
                or grid["radial"]["every_original_cell_retained"]is not True):
            raise ValueError("The full exact-material address plan differs from the selected field")
        actual(report["material_grid_arrays"]);actual(report["actual_evaluation_chart"])
        if (len(report["spatial_refinement"])!=len(report["requested_levels"])-1
                or len(report["time_refinement"])!=len(report["requested_time_levels"])-1
                or len(report["cap_metric_readouts"])!=len(report["requested_levels"])):
            raise ValueError("Keep every requested complete spatial/time/cap readout")
        count=len(report["export_level_indices"])*len(report["requested_physical_times"])
        if len(report["meshes"])!=count or len(report["previews"])!=len(report["requested_physical_times"]):
            raise ValueError("A complete declared surface/time export is absent")
        answer["mesh_records"]=[read_ply_header(item) for item in report["meshes"]]
        answer["preview_records"]=[read_ply_header(item,
            preview_limit=report["preview_parameters"]["strict_byte_limit"]) for item in report["previews"]]
        frequency=report["exact_frequency_input"]
        for key in ("input_definition","coefficient_file","actual_same_model_checkpoint"):
            actual(frequency[key])
        freq=read_json(frequency["input_definition"])
        definition=freq["definition"]
        if (canonical(definition)!=frequency["definition_identity_sha256"]
                or freq["definition_identity_sha256"]!=frequency["definition_identity_sha256"]
                or definition["source_point_sha256"]!=binding["point_sha256"]
                or definition["fixed_target_definition_identity_sha256"]!=binding["fixed_target_definition_identity_sha256"]
                or definition["actual_new_frequency_field_evaluated"]is not False
                or definition["nonlinear_same_g_frequency_refinement_convergence_claimed"]is not False):
            raise ValueError("Exact coefficient inclusion must not masquerade as a refined solve")
        for key in ("frequency_solution_refinement_performed","continuous_metric_error_paid",
                    "continuous_root_error_paid","complete_continuous_branch_certified",
                    "marked_closed_surface_embedding_certified",
                    "reach_or_grip_or_Euclidean_quotient_gap_certified"):
            if report.get(key)is not False:
                raise ValueError("Keep each unpaid continuous or nonlinear-refinement responsibility explicit")
    elif report.get("status")!="actual-incomplete-mesh-consumer":
        answer["actual_intermediate_report_not_terminal"]=True
    if record(report_path)!=report_record:
        raise ValueError("The actual mesh report changed during the pure read")
    return answer


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--report",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    output=args.output.resolve();repo=args.repo.resolve()
    if (output.exists() or output==args.report.resolve()
            or output==repo or repo in output.parents):
        raise FileExistsError("Use a fresh independent pure mesh readout outside the repository")
    result=read_report(args.repo,args.report)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:v for k,v in result.items()
        if v is None or isinstance(v,(str,int,float,bool))},allow_nan=False),flush=True)


if __name__=="__main__":
    main()
