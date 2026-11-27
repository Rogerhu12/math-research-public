#!/usr/bin/env python3
"""Stream complete actual-fixed-fejer upper-field boxes into R625/R716 flux integrals.

The accurate upper field is read from the complete source-bound normal-fee
journal. This program never evaluates F, J, a root, a reference mean or a
quadrature sample. It retains every full-circle cell and every accurate radial
leaf. Missing cells produce partial output with full-domain moments set to null.

A formal reflected lower surface and both flat caps are integrated explicitly.
Its interpretation as an embedded outward closed boundary, the normal-tube
placement of fixed markers, and the physical phase contract remain distinct
proof obligations. No Boolean label is used to invent those proofs.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time
import uuid

SCHEMA="actual-fixed-fejer-meridian-batched-complete-closed-parametric-flux-integrals-v1"
BLOCK_SCHEMA="actual-fixed-fejer-meridian-batched-complete-angle-flux-integral-block-v1"
TOPIC="topics/visible-flex-larger-amplitude"
KERNEL=("r716_closed_surface_moment_arithmetic.py","f79c69edc4686148ca0a1418a498ce0154492a842561542c6bbdb8d810563e9a")
NORMAL_FEE_SOURCE=("fixed_fejer_meridian_batched_complete_normal_root_and_sixjet_fees.py","242fc2f403db2495ea70e27437823031a84b26da717190b5f7e7ea252f9c0e2e")
NORMAL_FEE_SCHEMA="actual-fixed-fejer-meridian-batched-complete-normal-root-and-physical-sixjet-fees-v1"
JOURNAL_SCHEMA="actual-fixed-fejer-meridian-batched-complete-normal-fee-journal-v1"
STREAM_SCHEMA="complete-actual-fixed-fejer-meridian-batched-accurate-physical-sixjet-stream-v1"
ACTUAL_DRIVER="41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2"
ACTUAL_READER="d3f1b33c0b298f5000c5973281507557212299324ce246ce73ca1551822d0c52"
ACTUAL_MODEL_SOURCE="388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4"
FIXED_INPUT_BINDING_SOURCE=("fixed_fejer_reference_input_binding.py","3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f")
FIXED_ENTRY_BINDING_SOURCE=("fixed_fejer_meridian_source_binding.py","15cd8e201db8aeef7139baf0e82d9d18fcf190194cd33dc8b112bebe05a7dffc")
ACTUAL_BASE="552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3"


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("Actual moment integration runs only in public repository Actions")


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda:handle.read(1<<20),b""):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()


def file_record(path):
    path=Path(path).resolve()
    return dict(path=str(path),bytes=path.stat().st_size,sha256=sha(path))


def load_kernel(repo):
    path=Path(repo).resolve()/TOPIC/"scripts/resume_20261126"/KERNEL[0]
    if sha(path)!=KERNEL[1]:
        raise ValueError("The entire moment arithmetic source changed")
    spec=importlib.util.spec_from_file_location("_complete_r716_moment_arithmetic",path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    if sha(path)!=KERNEL[1] or sha(module.__file__)!=KERNEL[1]:
        raise ValueError("The complete moment arithmetic module changed during loading")
    return module,path


def strict_json(raw):
    return json.loads(raw,parse_constant=lambda value:(_ for _ in ()).throw(
        ValueError("Nonfinite JSON word: "+value)))


class Files:
    def __init__(self):
        self.records={}

    def add(self,path):
        record=file_record(path)
        return self.verify(record)

    def verify(self,record,*,force=False):
        if (not isinstance(record,dict) or set(record)!={"path","bytes","sha256"}
                or type(record["bytes"]) is not int or record["bytes"]<0):
            raise ValueError("Retain the entire original file identity")
        path=Path(record["path"]).resolve()
        previous=self.records.get(str(path))
        if previous is not None and previous!=record:
            raise ValueError("One immutable input path has inconsistent identities")
        if previous is not None and not force:
            return path
        current=file_record(path)
        if current!=record:
            raise ValueError("A complete actual input changed: "+str(path))
        self.records[str(path)]=dict(record)
        return path

    def read_json(self,record):
        path=self.verify(record)
        raw=path.read_bytes()
        if len(raw)!=record["bytes"] or hashlib.sha256(raw).hexdigest()!=record["sha256"]:
            raise ValueError("An actual JSON changed during capture")
        value=strict_json(raw)
        self.verify(record,force=True)
        return value,raw

    def recheck(self):
        for record in list(self.records.values()):
            self.verify(record,force=True)

    def protect_output(self,path):
        path=Path(path).resolve()
        for record in self.records.values():
            source=Path(record["path"]).resolve()
            if source==path or path in source.parents:
                raise ValueError("The output namespace contains an original complete input")
        return path


def immutable_bytes(path,raw):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():
        if path.read_bytes()!=raw:
            raise ValueError("An immutable integral record already has different bytes")
        return file_record(path)
    tmp=path.with_name(path.name+".partial-"+uuid.uuid4().hex)
    with tmp.open("xb") as handle:
        handle.write(raw)
        handle.flush()
        os.fsync(handle.fileno())
    try:
        os.link(tmp,path)
    except FileExistsError:
        if path.read_bytes()!=raw:
            raise ValueError("Concurrent immutable integral contents differ")
    finally:
        if tmp.exists():
            tmp.unlink()
    return file_record(path)


def immutable_json(path,value,k):
    raw=(json.dumps(k.serialize(value),sort_keys=True,indent=2,allow_nan=False)+"\n").encode()
    return immutable_bytes(path,raw)


def write_report(path,value,k):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".partial-"+uuid.uuid4().hex)
    raw=(json.dumps(k.serialize(value),sort_keys=True,indent=2,allow_nan=False)+"\n").encode()
    with tmp.open("xb") as handle:
        handle.write(raw)
        handle.flush()
        os.fsync(handle.fileno())
    tmp.replace(path)
    return file_record(path)


def affine(value,k):
    if not isinstance(value,list) or len(value)!=2:
        raise ValueError("Keep the exact affine convention s=alpha*S+beta")
    return tuple(k.rational(v) for v in value)


def affine_width(left,right,S,k):
    a,b=affine(left,k),affine(right,k)
    result=(b[0]-a[0])*S+(b[1]-a[1])
    if result.lo<=0:
        raise ArithmeticError("A true radial leaf does not have proved positive exact width")
    return result


def _verify_source_roles(binding,repo,files):
    root=Path(repo).resolve()/TOPIC/"scripts/resume_20261126"
    source=root/NORMAL_FEE_SOURCE[0]
    if sha(source)!=NORMAL_FEE_SOURCE[1] or binding.get("source_sha256")!=NORMAL_FEE_SOURCE[1]:
        raise ValueError("Use the complete specifically bound normal-fee producer")
    files.add(source)
    roles=binding.get("complete_source_sha256_by_role")
    expected_names={
        "actual_input":("fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py",
            "d9cbf733957e3577cfc6175a1d69024a2874468e1cde7141f5d81b984676430b"),
        "accurate_rotation":("accurate_normal_rotation_and_stage_boxes.py",
            "29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b"),
        "accurate_radial":("fixed_fejer_meridian_batched_accurate_reference_control_radial_boxes.py",
            "a978609f6ec973c5c495e7cdb2a2da36eb2e786f48bd948e5ed1ce488934a1fb")}
    if not isinstance(roles,dict) or set(roles)!=set(expected_names):
        raise ValueError("The complete normal-fee role set changed")
    for role,(name,expected) in expected_names.items():
        path=root/name
        if roles[role]!=expected or sha(path)!=expected:
            raise ValueError("An accurate field role differs from its original producer binding")
        files.add(path)
    return roles


def verify_point_layout(actual,geometry,files,k):
    """Read the complete original point, without constructing or evaluating F."""
    import numpy as np
    record=actual["current_point_arrays_file"]
    path=files.verify(record)
    with np.load(path,allow_pickle=False) as data:
        if set(data.files)!={"x"}:
            raise ValueError("Use the original immutable full-point packet, not selected variables")
        x=np.array(data["x"],copy=True)
    files.verify(record,force=True)
    M,J,n,fixed=160,923,482,3
    excluded=(0,3*(J-1),3*(J-1)+1)
    free_rows=[i for i in range(3*J) if i not in excluded]
    expected=(M-fixed)+len(free_rows)*n+1
    if x.dtype!=np.dtype("float64") or x.shape!=(expected,) or not np.isfinite(x).all():
        raise ValueError("The actual original complete coordinate layout changed")
    h=hashlib.sha256(str(x.dtype).encode())
    h.update(json.dumps(list(x.shape)).encode())
    h.update(np.ascontiguousarray(x).tobytes())
    if h.hexdigest()!=actual["current_full_point_sha256"]:
        raise ValueError("The entire current free point differs from the accurate field")
    height=float(x[-1])
    if (height.hex()!=actual["original_current_H_hex"]
            or F(height)!=k.rational(geometry["current_H"])):
        raise ValueError("The cap height is not the actual current free-height word")
    x.setflags(write=False)
    model=actual["complete_model"]
    base=model["base_complete_model"]
    if base.get("source_sha256")!=ACTUAL_BASE:
        raise ValueError("Endpoint assembly is tied to the complete original base layout")
    if (model.get("source_sha256")!=ACTUAL_MODEL_SOURCE
            or canonical(model)!=actual["model_identity_sha256"]):
        raise ValueError("Use the entire accurately bound original normal model")
    for key in ("exact_relative_bubble_nodes","exact_relative_gamma_nodes"):
        triples=model[key] if key=="exact_relative_bubble_nodes" else [model[key]]
        if any(len(t)!=3 or not 0<k.rational(t[0])<k.rational(t[1])<k.rational(t[2])<1
                for t in triples):
            raise ValueError("Every endpoint control must have its entire support strictly inside (0,S)")
    seed=base["fixed_supported_unit_seed_model"]
    support=seed["exact_relative_support_intervals"]
    if len(support)!=2 or any(len(t)!=2 or not 0<k.rational(t[0])<k.rational(t[1])<1
            for t in support):
        raise ValueError("Retain the original compactly supported reference modification")
    return dict(complete_point_arrays=record,current_point_sha256=h.hexdigest(),
        complete_free_variable_count=expected,M=M,J=J,rotation_slot_count=n,
        fixed_core_count=fixed,exact_zero_rotation_rows=list(excluded),
        current_H_binary64_hex=height.hex(),
        source_layout_assertion="552f fixed-Fejer literal unpack excludes exactly these complete rows",
        core_first_second_and_cap_second_rotation_jets_remain_free=True,
        full_point_read_without_F_J_or_root_calls=True,
        analytic_endpoint_relations_used=[
            "core: F=Gamma, Fs=ez, Fss horizontal, Fsphi=0",
            "cap: F=R*er(theta0)+H*ez, Fs=-er(theta0), Fss=0",
            "cap: Fphi=R*rho0*et(theta0), Fsphi=-rho0*et(theta0)",
            "both endpoints: hprime=hsecond=0; complete raw lift retained"],
        reference_endpoint_law_and_original_operator_sources_retained=True,
        closed_C2_seam_claim_requires_complete_same_branch_upper_field=True,
        embedded_outward_boundary_or_half_turn_covariance_proved_here=False)


def verify_actual_fixed_reference(actual, outer, repo, files):
    """Read the whole predeclared target; never compare two unvalidated labels."""
    root=Path(repo).resolve()/TOPIC/"scripts/resume_20261126"
    path=root/FIXED_ENTRY_BINDING_SOURCE[0]
    for name,digest in (FIXED_ENTRY_BINDING_SOURCE,FIXED_INPUT_BINDING_SOURCE):
        candidate=root/name
        if sha(candidate)!=digest:
            raise ValueError("The complete fixed-target binding source changed")
        files.add(candidate)
    key="_moment_complete_fixed_fejer_entry_binding"
    spec=importlib.util.spec_from_file_location(key,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[key]=module
    spec.loader.exec_module(module)
    if (sha(module.__file__)!=FIXED_ENTRY_BINDING_SOURCE[1]
            or sha(module.bind_fixed_fejer_input.__code__.co_filename)!=FIXED_ENTRY_BINDING_SOURCE[1]):
        raise ValueError("The complete fixed-target entry method changed")
    entry=outer.get("actual_fixed_reference_input_binding")
    if (not isinstance(entry,dict)
            or actual.get("complete_actual_fixed_reference_input_binding")!=entry):
        raise ValueError("Retain the full actual scientific input binding")
    record=entry["actual_binding_file"]
    files.verify(record)
    current=module.bind_fixed_fejer_input(record["path"],
        current_files=actual["complete_six_actual_inputs"])
    if current!=entry:
        raise ValueError("The complete current entry and all six input files changed")
    payload,_=files.read_json(record)
    target=payload["fixed_target_definition"]
    reference=actual["complete_model"]["base_complete_model"]["complete_axisymmetric_reference_model"]
    if (reference!=target["complete_current_reference_model"]
            or canonical(reference)!=entry["actual_reference_model_identity_sha256"]
            or actual.get("actual_reference_model_identity_sha256")!=entry["actual_reference_model_identity_sha256"]
            or actual.get("exact_fixed_target_identity_sha256")!=entry["actual_fixed_target_definition_identity_sha256"]
            or actual.get("mathematical_target_identity_sha256")!=entry["mathematical_target_identity_sha256"]
            or actual.get("fixed_chart_core_sha256")!=entry["actual_fixed_chart_core_sha256"]
            or canonical(target)!=entry["actual_fixed_target_definition_identity_sha256"]
            or payload["current_files"]!=actual["complete_six_actual_inputs"]
            or entry["complete_current_input_files"]!=actual["complete_six_actual_inputs"]):
        raise ValueError("Bind the complete reference, pure recipe and working target separately")
    for value in payload["current_files"].values():
        files.verify(value)
    for name in ("fixed_input_preparation_report","fixed_target_definition_file",
                 "new_locations","complete_supplied_location_provenance"):
        files.verify(payload[name])
    files.verify(record,force=True)


def bind_input(report_path,expected_sha,repo,files,k):
    record=file_record(report_path)
    if expected_sha is not None and record["sha256"]!=expected_sha:
        raise ValueError("The requested complete normal-fee report SHA differs")
    report,raw=files.read_json(record)
    if (report.get("schema")!=NORMAL_FEE_SCHEMA
            or report.get("source_sha256")!=NORMAL_FEE_SOURCE[1]):
        raise ValueError("Use the complete actual-fixed-fejer normal-fee report")
    if report.get("complete_binding") is None:
        return dict(available=False,record=record,raw=raw,report=report,
            reason="The upstream accurate producer has no complete input binding")
    binding,_=files.read_json(report["complete_binding"])
    identity=canonical(binding)
    if identity!=report.get("complete_binding_identity_sha256"):
        raise ValueError("The normal-fee execution binding is not canonical")
    roles=_verify_source_roles(binding,repo,files)
    request_doc,_=files.read_json(report["complete_input_and_request"])
    request_identity=canonical(request_doc)
    if (request_identity!=report.get("complete_input_and_request_identity_sha256")
            or request_identity!=binding.get("complete_input_and_request_identity_sha256")
            or request_doc.get("source_sha256")!=NORMAL_FEE_SOURCE[1]):
        raise ValueError("The entire original planned input/request binding changed")
    for key in ("complete_source_sha256_by_role","actual_complete_input",
            "actual_complete_input_identity_sha256","complete_parameters","complete_angle_requests",
            "accurate_pi_enclosure","complete_normal_stage_count"):
        if request_doc.get(key)!=binding.get(key):
            raise ValueError("The final geometry binding differs from its entire original request")
    actual=binding["actual_complete_input"]
    actual_id=canonical(actual)
    if (binding.get("actual_complete_input_identity_sha256")!=actual_id
            or report["actual_input"].get("binding")!=actual
            or report["actual_input"].get("binding_identity_sha256")!=actual_id):
        raise ValueError("The exact field and selected point changed across complete objects")
    if (actual.get("actual_driver_sha256")!=ACTUAL_DRIVER
            or actual.get("complete_pure_reader_sha256")!=ACTUAL_READER
            or report.get("actual_scientific_driver_sha256")!=ACTUAL_DRIVER
            or report.get("actual_pure_reader_sha256")!=ACTUAL_READER):
        raise ValueError("No older target, working representation or repaired-source label may be substituted")
    if (report.get("actual_current_full_point_sha256")!=actual["current_full_point_sha256"]
            or report.get("actual_snapshot_identity_sha256")!=actual["actual_snapshot_identity_sha256"]
            or report.get("actual_report")!=actual["scientific_report"]):
        raise ValueError("All complete records must identify the very same actual point")
    outer,_=files.read_json(actual["scientific_report"])
    if (outer.get("source_sha256")!=ACTUAL_DRIVER
            or outer.get("representation")!=actual["complete_model"]):
        raise ValueError("The complete actual mathematical model differs from the scientific report")
    verify_actual_fixed_reference(actual,outer,repo,files)
    for source in actual["full_scientific_runtime_source_records"].values():
        files.verify(source)
    for source in actual["complete_six_actual_inputs"].values():
        files.verify(source)
    files.verify(actual["actual_snapshot_file"])
    geometry=report.get("accurate_geometry")
    if not isinstance(geometry,dict):
        return dict(available=False,record=record,raw=raw,report=report,
            reason="The entire accurate radial/scalar geometry has not returned")
    if (geometry.get("identity")!=binding.get("accurate_geometry_identity_sha256")
            or geometry.get("actual_input_identity")!=actual_id
            or geometry.get("source_sha256")!=roles["accurate_radial"]):
        raise ValueError("The complete accurate geometry is not from the bound point")
    for name in ("fixed_rho_proof","current_rho_proof"):
        proof=geometry[name]
        if (proof.get("whole_angle_domain_over_pi")!=["0","2"]
                or proof.get("all_coefficients_used") is not True
                or k.rational(proof["lower"])<=0):
            raise ValueError("Global positive fixed/current material charts are required")
    bits=k.integer(binding["complete_parameters"]["precision_bits"],minimum=64,maximum=1024)
    S,R=k.box(geometry["accurate_S"],bits),k.box(geometry["accurate_R"],bits)
    H=k.Interval(k.rational(geometry["current_H"]),bits=bits)
    pi=k.box(binding["accurate_pi_enclosure"],bits)
    if S.lo<=0 or R.lo<=0 or not 3<pi.lo<=pi.hi<4:
        raise ArithmeticError("Use complete positive length/radius and the producer's accurate pi enclosure")
    partition=[k.rational(v) for v in actual["exact_common_normal_partition"]]
    if (len(partition)!=33 or partition[0]!=0 or partition[-1]!=1
            or any(a>=b for a,b in zip(partition,partition[1:]))
            or binding.get("complete_normal_stage_count")!=32
            or actual.get("full_stage_count")!=32):
        raise ValueError("Do not reduce or relabel any of the thirty-two normal stages")
    plan=geometry["complete_exact_radial_plan"]
    if not isinstance(plan,list) or not plan:
        raise ValueError("A complete original radial partition is required")
    if affine(plan[0]["left"],k)!=(F(0),F(0)) or affine(plan[-1]["right"],k)!=(F(1),F(0)):
        raise ValueError("The exact upper radial domain must be all [0,S]")
    for i,leaf in enumerate(plan):
        if (not isinstance(leaf,dict) or leaf.get("id")!="r"+str(i)
                or leaf.get("depth")!=0 or type(leaf.get("original_cell")) is not int
                or not 0<=leaf["original_cell"]<922):
            raise ValueError("The original complete radial-cell identity changed")
        affine_width(leaf["left"],leaf["right"],S,k)
        if i and leaf["left"]!=plan[i-1]["right"]:
            raise ValueError("A radial gap or overlap cannot be discarded")
    if set(leaf["original_cell"] for leaf in plan)!=set(range(922)):
        raise ValueError("Every original radial cell, including the complete tail, is required")
    point=verify_point_layout(actual,geometry,files,k)
    return dict(available=True,record=record,raw=raw,report=report,binding=binding,
        binding_identity=identity,actual=actual,actual_identity=actual_id,geometry=geometry,
        partition=partition,plan=plan,S=S,R=R,H=H,pi=pi,bits=bits,point=point,
        upstream_final_bytes_rechecked=report.get(
            "all_bound_input_and_output_bytes_rechecked_at_final_report") is True)


def load_job(summary,request,context,files,k):
    if summary.get("request")!=request:
        raise ValueError("An accurate angular job was relabelled")
    if summary.get("journal_header") is None:
        if (summary.get("complete") is not False or summary.get("journal") is not None
                or summary.get("complete_physical_stream") is not None
                or summary.get("completed_stage_count") is not None):
            raise ValueError("An uninitialized complete angular journal cannot claim results")
        return dict(request=request,summary=summary,header=None,identity=None,
            stages=[],physical=None,complete=None,last_event=None,last_stage_event=None,
            complete_reference_and_domain_file=None)
    header,_=files.read_json(summary["journal_header"])
    identity=canonical(header)
    if (header.get("schema")!=JOURNAL_SCHEMA
            or header.get("complete_execution_binding")!=context["binding_identity"]
            or header.get("request")!=request
            or header.get("exact_normal_step_nodes")!=[str(v) for v in context["partition"]]
            or header.get("original_stage_count")!=32
            or identity!=summary.get("journal_binding_identity_sha256")
            or header.get("root_radius_proposals")!=context["binding"]["complete_parameters"]["root_radius"]):
        raise ValueError("Retain the original complete same-field angular journal binding")
    stages=[]
    physical=None
    complete=None
    last=identity
    events=0
    unavailable=0
    last_stage_event=None
    reference_record=None
    def bind_reference(record):
        nonlocal reference_record
        wanted=(Path(summary["journal_header"]["path"]).resolve().parent/
            "accurate-reference-and-domain.json").resolve()
        if Path(record["path"]).resolve()!=wanted:
            raise ValueError("The whole same-field mean/domain proof belongs to another angular job")
        if reference_record is not None:
            if record!=reference_record:
                raise ValueError("One immutable angular job changed its exact reference proof")
            return
        proof,_=files.read_json(record)
        if (proof.get("schema")!="complete-actual-reference-mean-and-domain-for-normal-fees-v1"
                or proof.get("execution_identity_sha256")!=context["binding_identity"]
                or proof.get("request")!=request
                or proof.get("precise_whole_radial_plan")!=list(refined_leaves(context,k))
                or not isinstance(proof.get("accurate_reference_mean_evidence"),dict)
                or not isinstance(proof.get("complete_accurate_core_and_cap"),dict)):
            raise ValueError("The complete original angular mean, endpoints or radial domain changed")
        mean=proof["accurate_reference_mean_evidence"]
        if (mean.get("actual_input_identity")!=context["actual_identity"]
                or mean.get("geometry_identity")!=context["geometry"]["identity"]
                or mean.get("accurate_phi_interval")!=request["accurate_phi_interval"]
                or mean.get("candidate_literal_phi_hex")!=request["actual_anchor"]
                or mean.get("all_original_mean_radial_pieces_included") is not True
                or mean.get("sufficient_R709_inequalities_verified_on_this_whole_interval") is not True
                or mean.get("whole_interval_bounds_computed_here") is not True):
            raise ValueError("The complete whole-angle reference mean is not the same actual field/request")
        reference_record=dict(record)
    journal_record=summary.get("journal")
    if journal_record is not None:
        path=files.verify(journal_record)
        with path.open("rb") as handle:
            for raw in handle:
                if not raw.endswith(b"\n"):
                    raise ValueError("A partial accuracy-journal line is not a proof record")
                item=strict_json(raw)
                events+=1
                event=item.get("definition")
                if (not isinstance(event,dict) or item.get("sequence")!=events
                        or item.get("previous_identity_sha256")!=last
                        or item.get("event_identity_sha256")!=canonical(event)
                        or event.get("journal_binding_identity_sha256")!=identity):
                    raise ValueError("The complete ordered accurate-stage journal changed")
                last=item["event_identity_sha256"]
                kind=event.get("kind")
                if kind=="stage_complete":
                    stage=event["stage"]
                    proof=stage["complete_proof"]
                    index=len(stages)+1
                    if (physical is not None or complete is not None
                            or stage.get("normal_stage_index")!=index or index>32
                            or k.rational(proof["tau"])!=context["partition"][index]
                            or proof.get("passed") is not True
                            or k.rational(proof["q"])>=1
                            or k.rational(proof["q"])<0
                            or k.rational(proof["strict_invariance_margin"])<=0
                            or k.rational(proof["contraction_radius"])<=0
                            or proof.get("all_upstream_control_and_frame_angular_jets_propagated") is not True
                            or str(k.rational(stage["selected_radius"])) not in header["root_radius_proposals"]
                            or k.rational(proof["contraction_radius"])!=k.rational(stage["selected_radius"])):
                        raise ValueError("An original accurate normal stage is incomplete or inconsistent")
                    eta=proof["eta_jets"]
                    controls=proof["controls"]
                    if len(eta)!=3 or any(len(row)!=3 for row in eta) or len(controls)!=3 or any(
                            len(row)!=6 for row in controls):
                        raise ValueError("Keep all true angular jets and all six controls")
                    for value in [v for row in eta+controls for v in row]:
                        k.box(value,context["bits"])
                    if len(stage.get("eta0_centre_binary64_hex",[]))!=3:
                        raise ValueError("A complete actual local root-centre word is required")
                    for word in stage["eta0_centre_binary64_hex"]:
                        value=float.fromhex(word)
                        if not math.isfinite(value) or value.hex()!=word:
                            raise ValueError("Do not round or invent the actual root-centre proposal")
                    provenance=stage["source"]
                    if provenance.get("original_root_order_not_upgraded") is not True:
                        raise ValueError("The original working root order may not be silently upgraded")
                    for key in ("original_packet_file","actual_packet_arrays_file"):
                        files.verify(provenance[key])
                    bind_reference(stage["whole_accurate_oracle_reference"])
                    stages.append(stage)
                    last_stage_event=last
                elif kind=="accurate_attempt_unavailable":
                    if complete is not None or event.get("next_normal_stage_index")!=len(stages)+1:
                        raise ValueError("A failed attempt may not skip or overwrite a stage")
                    unavailable+=1
                elif kind=="physical_file_complete":
                    if len(stages)!=32 or physical is not None or complete is not None:
                        raise ValueError("Physical flux requires the entire original accurate stage chain")
                    if event.get("entire_accurate_same_field_sixjets") is not True:
                        raise ValueError("Require the complete true physical sixjet output")
                    k.integer(event["complete_radial_leaf_count"],minimum=1)
                    files.verify(event["file"])
                    physical=event
                elif kind=="job_complete":
                    if physical is None or complete is not None or event.get("all_original_stage_count")!=32:
                        raise ValueError("Do not complete a job without its full physical stream")
                    if event.get("accurate_current_point_sha256")!=context["actual"]["current_full_point_sha256"]:
                        raise ValueError("An accurate angular job belongs to another actual point")
                    bind_reference(event["complete_accurate_reference_and_domain"])
                    complete=event
                else:
                    raise ValueError("Unknown event in the complete normal-fee journal")
        files.verify(journal_record,force=True)
    if (summary.get("last_event_identity_sha256")!=last
            or summary.get("completed_stage_count")!=len(stages)
            or summary.get("complete_journal_event_count")!=events
            or summary.get("unavailable_attempt_count")!=unavailable
            or summary.get("complete_physical_stream")!=physical
            or summary.get("complete_reference_and_domain_file")!=reference_record
            or summary.get("complete")!=(complete is not None)):
        raise ValueError("The published angular summary differs from its whole journal")
    return dict(request=request,summary=summary,header=header,identity=identity,
        stages=stages,physical=physical,complete=complete,last_event=last,last_stage_event=last_stage_event,
        complete_reference_and_domain_file=reference_record)


def _root_domain(stage,k):
    radius=k.rational(stage["selected_radius"])
    return [[F(float.fromhex(word))-radius,F(float.fromhex(word))+radius]
        for word in stage["eta0_centre_binary64_hex"]]


def _included(inner,outer,k):
    if len(inner)!=3 or len(outer)!=3:
        raise ValueError("Use the whole three-dimensional root enclosure")
    return all(k.rational(a[0])>=b[0] and k.rational(a[1])<=b[1]
        for a,b in zip(inner,outer))


def glue(left,right,k):
    if left["complete"] is None or right["complete"] is None:
        return dict(passed=False,complete_stage_count=0,
            reason="One original complete angular chain remains unpaid")
    checks=[]
    for a,b in zip(left["stages"],right["stages"]):
        ab=_included(a["complete_proof"]["eta_jets"][0],_root_domain(b,k),k)
        ba=_included(b["complete_proof"]["eta_jets"][0],_root_domain(a,k),k)
        checks.append(ab or ba)
    return dict(passed=len(checks)==32 and all(checks),complete_stage_count=len(checks),
        every_original_stage_directed_root_inclusion=checks,
        overlapping_boxes_alone_are_not_sufficient=True)


def complete_branch(context,jobs,k):
    requests=context["binding"]["complete_angle_requests"]
    circles=[jobs[r["id"]] for r in requests if r["kind"]=="full_angle_cell"]
    count=k.integer(context["binding"]["complete_parameters"]["full_angle_cells"],minimum=0)
    if len(circles)!=count:
        raise ValueError("The declared complete circle plan changed")
    if count==0:
        return dict(complete=False,full_circle_requested=False,complete_circle_count=0,
            expected_circle_count=0,reason="Literal angles are not a whole-circle integral domain")
    for i,job in enumerate(circles):
        r=job["request"]
        exact=[str(F(2*i,count)),str(F(2*(i+1),count))]
        if (r.get("full_circle_cell_index")!=i or r.get("exact_phi_over_pi_interval")!=exact
                or r.get("id")!="circle-"+str(i).zfill(6)):
            raise ValueError("The exact full-circle request contains a gap, overlap or altered cell")
        phi=k.box(r["accurate_phi_interval"],context["bits"])
        expected=k.Interval(F(2*i,count),F(2*(i+1),count),context["bits"])*context["pi"]
        if phi.lo>expected.lo or phi.hi<expected.hi:
            raise ValueError("The whole physical angular box misses its exact pi-scaled domain")
    all_complete=all(job["complete"] is not None for job in circles)
    if not all_complete:
        return dict(complete=False,full_circle_requested=True,
            complete_circle_count=sum(job["complete"] is not None for job in circles),
            expected_circle_count=count,reason="Some complete whole-angle chains remain unpaid")
    adjacent=[glue(a,b,k) for a,b in zip(circles,circles[1:])]
    periodic=glue(circles[0],circles[-1],k)
    associations=[]
    for request in requests:
        if request["kind"]!="actual_literal":
            continue
        q=F(float.fromhex(request["literal_phi_hex"]))
        matching=[job for job in circles if k.rational(job["request"]["accurate_phi_interval"][0])<=q
                  <=k.rational(job["request"]["accurate_phi_interval"][1])]
        checks=[glue(jobs[request["id"]],job,k) for job in matching]
        associations.append(dict(id=request["id"],literal_phi_hex=request["literal_phi_hex"],
            passed=any(v["passed"] for v in checks),complete_checks=checks))
    exact_proof=context["report"].get("full_same_field_angle_branch",{}).get(
        "periodic_equation_proof",{})
    periodic_keys=("all_current_and_fixed_angular_modes_are_original_integer_frequencies",
        "accurate_global_positive_core_inverse_has_exact_two_pi_lift",
        "full_R709_unique_reference_mean_and_projected_frame_are_two_pi_periodic",
        "exact_controls_and_fixed_common_stage_partition_preserved",
        "unique_local_roots_glued_from_the_identical_zero_control_stage")
    periodic_source=(all(exact_proof.get(key) is True for key in periodic_keys)
        and exact_proof.get("source_specific_field_model_identity_sha256")==
            context["actual"]["model_identity_sha256"])
    complete=all(v["passed"] for v in adjacent) and periodic["passed"] and (
        all(v["passed"] for v in associations)) and periodic_source
    return dict(complete=complete,full_circle_requested=True,
        expected_circle_count=count,complete_circle_count=count,
        exact_angle_domain_over_pi=["0","2"],adjacent_stage_inclusions=adjacent,
        periodic_stage_inclusion=periodic,actual_literal_branch_associations=associations,
        periodic_equation_source_proof_retained=periodic_source,
        actual_branch_check_recomputed_from_complete_original_journals=True,
        half_turn_signed_control_equivariance_proved=False)



def _half_turn_eta_box(stage,k):
    rows=stage["complete_proof"]["eta_jets"][0]
    return [[str(-k.rational(v[1])),str(-k.rational(v[0]))] if i<2 else list(v)
        for i,v in enumerate(rows)]


def half_turn_branch(context,jobs,branch,k):
    """Source-specific exact covariance plus all-stage directed root inclusion.

    P=diag(-1,-1,1), D=P direct-sum P.  The actual six-control coefficient
    satisfies B6(phi+pi) D=P B6(phi), the original reference/omega/cap/core
    transform by P, and C(phi+pi,Du)=P C(phi,u). Therefore A'=P A D and
    the stage normal update u+B^T eta transforms with eta'=P eta.
    Local uniqueness is applied inductively at every original stage. Merely
    having even/odd modes is never taken as an already selected root branch.
    """
    source=context["actual"]["complete_model"].get("source_sha256")
    if source!=ACTUAL_MODEL_SOURCE:
        raise ValueError("The exact half-turn frame covariance is source-specific")
    requests=[q for q in context["binding"]["complete_angle_requests"] if q["kind"]=="full_angle_cell"]
    count=len(requests)
    if not branch["complete"] or not context["upstream_final_bytes_rechecked"]:
        return dict(complete=False,reason="The full original same-field periodic branch or final source-byte recheck remains unpaid",
            half_turn_inferred_from_frequencies_alone=False)
    if count==0 or count%2:
        return dict(complete=False,
            reason="This exact pairing implementation needs an even full-circle partition; no cell is dropped",
            half_turn_inferred_from_frequencies_alone=False)
    pairs=[]
    for index in range(count//2):
        a=jobs[requests[index]["id"]]
        b=jobs[requests[index+count//2]["id"]]
        qa=[k.rational(v) for v in a["request"]["exact_phi_over_pi_interval"]]
        qb=[k.rational(v) for v in b["request"]["exact_phi_over_pi_interval"]]
        if qb!=[v+1 for v in qa]:
            raise ValueError("Do not infer a half turn from rounded angular endpoints")
        stages=[]
        for stage_index,(left,right) in enumerate(zip(a["stages"],b["stages"]),1):
            forward=_included(_half_turn_eta_box(left,k),_root_domain(right,k),k)
            backward=_included(_half_turn_eta_box(right,k),_root_domain(left,k),k)
            stages.append(dict(normal_stage_index=stage_index,
                signed_left_root_enclosure_in_right_uniqueness_cube=forward,
                signed_right_root_enclosure_in_left_uniqueness_cube=backward,
                passed=forward or backward))
        pairs.append(dict(left_job=a["request"]["id"],right_job=b["request"]["id"],
            exact_left_phi_over_pi=[str(v) for v in qa],
            exact_right_phi_over_pi=[str(v) for v in qb],
            stages=stages,passed=len(stages)==32 and all(v["passed"] for v in stages)))
    complete=all(v["passed"] for v in pairs)
    return dict(complete=complete,
        exact_world_rotation_diagonal=[-1,-1,1],
        exact_control_rotation_diagonal=[-1,-1,1,-1,-1,1],
        complete_original_stage_count=32,
        full_periodic_branch_identity_checked_first=True,
        actual_model_identity_sha256=context["actual"]["model_identity_sha256"],
        actual_current_point_sha256=context["actual"]["current_full_point_sha256"],
        actual_normal_source_sha256=ACTUAL_MODEL_SOURCE,
        exact_complete_angle_pairing_checked=True,all_actual_pairs=pairs,
        root_uniqueness_is_local_and_used_by_directed_inclusion=True,
        no_whole_control_ball_uniqueness_assumed=True,
        no_additional_F_J_or_root_evaluations=True,
        half_turn_inferred_from_frequencies_alone=False,
        bounded_entity_or_global_embedding_not_inferred_from_this_symmetry=True)

def refined_leaves(context,k):
    depth=k.integer(context["binding"]["complete_parameters"]["radial_depth"],minimum=0,maximum=20)
    def recurse(leaf,remaining):
        if remaining==0:
            yield leaf
            return
        left,right=affine(leaf["left"],k),affine(leaf["right"],k)
        middle=tuple((a+b)/2 for a,b in zip(left,right))
        for index,(a,b) in enumerate(((left,middle),(middle,right))):
            child=dict(leaf,id=leaf["id"]+"/"+str(index),
                left=[str(v) for v in a],right=[str(v) for v in b],depth=leaf["depth"]+1)
            yield from recurse(child,remaining-1)
    for leaf in context["plan"]:
        yield from recurse(dict(leaf),depth)


def integrate_job(job,context,files,k,binding_identity):
    if job["complete"] is None or job["request"]["kind"]!="full_angle_cell":
        raise ValueError("Only a fully completed whole-angle chain can enter an integral block")
    record=job["physical"]["file"]
    path=files.verify(record)
    integral=k.zero_moments(context["bits"])
    area=k.Interval(0,bits=context["bits"])
    position_radius=F(0)
    q0,q1=[k.rational(v) for v in job["request"]["exact_phi_over_pi_interval"]]
    angle_width=(q1-q0)*context["pi"]
    expected=iter(refined_leaves(context,k))
    leaves=0
    footer=None
    radial_end=None
    with gzip.open(path,"rb") as handle:
        first=handle.readline()
        if not first.endswith(b"\n"):
            raise ValueError("The complete physical-stream header is missing")
        header=strict_json(first)
        if (header.get("schema")!=STREAM_SCHEMA
                or header.get("execution_identity_sha256")!=context["binding_identity"]
                or header.get("journal_binding_identity_sha256")!=job["identity"]
                or header.get("accurate_request")!=job["request"]
                or header.get("original_stage_count")!=32
                or header.get("accurate_final_stage_event_identity")!=job["last_stage_event"]
                or header.get("complete_original_field_model")!=context["actual"]["model_identity_sha256"]):
            raise ValueError("The physical stream is not this complete same-field angular job")
        for raw in handle:
            if not raw.endswith(b"\n"):
                raise ValueError("A partial physical-stream line cannot enter a complete integral")
            value=strict_json(raw)
            if footer is not None:
                raise ValueError("A physical interval stream has trailing records after its footer")
            if value.get("kind")=="complete_radial_cover_footer":
                footer=value
                break
            if value.get("kind")!="complete_closed_radial_cell":
                raise ValueError("Only complete true radial cells may enter the full-domain integral")
            leaf=next(expected,None)
            leaves+=1
            if (leaf is None or value.get("ordinal")!=leaves
                    or value.get("exact_radial_leaf")!=leaf
                    or value.get("accurate_phi_interval")!=job["request"]["accurate_phi_interval"]
                    or value.get("all_same_field_radial_and_angular_chains_retained") is not True):
                raise ValueError("A complete exact physical cell was changed, omitted or duplicated")
            if radial_end is not None and leaf["left"]!=radial_end:
                raise ValueError("The physical integral cannot cross an unrecorded radial gap")
            radial_end=leaf["right"]
            width=affine_width(leaf["left"],leaf["right"],context["S"],k)
            channels,norm,position=k.flux_channels(value["physical_sixjets"],context["bits"])
            measure=width*angle_width
            integral=k.add_moments(integral,k.scale_moments(channels,measure))
            area=area+norm*measure
            position_radius=max(position_radius,position.hi)
        if handle.read(1):
            raise ValueError("No content may follow the complete radial footer")
    files.verify(record,force=True)
    if (footer is None or footer.get("all_exact_radial_leaves_written") is not True
            or footer.get("full_closed_surface_seams_or_reach_certified") is not False
            or footer.get("complete_radial_leaf_count")!=leaves
            or job["physical"]["complete_radial_leaf_count"]!=leaves
            or next(expected,None) is not None
            or affine(radial_end,k)!=(F(1),F(0))):
        raise ValueError("The entire accurate radial cover has not been consumed")
    return dict(schema=BLOCK_SCHEMA,source_sha256=sha(__file__),
        moment_binding_identity_sha256=binding_identity,
        current_full_point_sha256=context["actual"]["current_full_point_sha256"],
        model_identity_sha256=context["actual"]["model_identity_sha256"],
        exact_fixed_target_identity_sha256=context["actual"]["exact_fixed_target_identity_sha256"],
        mathematical_target_identity_sha256=context["actual"]["mathematical_target_identity_sha256"],
        accurate_request=job["request"],normal_journal_binding_identity_sha256=job["identity"],
        original_complete_stage_count=32,physical_stream=record,
        original_journal=job["summary"]["journal"],original_journal_header=job["summary"]["journal_header"],
        complete_radial_leaf_count=leaves,complete=True,
        upper_oriented_flux_integrals=integral,upper_parametric_area=area,
        whole_cell_position_norm_upper=str(position_radius),
        orientation="Fphi cross Fs on the entire upper meridian",
        integration="outward whole-box range times exact affine radial width times exact pi-angle width",
        exact_original_tail_and_all_subcells_included=True,
        no_sampled_quadrature_or_working_field_evaluation=True,
        closed_surface_or_embedded_volume_interpretation_certified=False)


def read_block(path,job,context,files,k,binding_identity):
    record=file_record(path)
    value,_=files.read_json(record)
    if (value.get("schema")!=BLOCK_SCHEMA or value.get("source_sha256")!=sha(__file__)
            or value.get("moment_binding_identity_sha256")!=binding_identity
            or value.get("current_full_point_sha256")!=context["actual"]["current_full_point_sha256"]
            or value.get("model_identity_sha256")!=context["actual"]["model_identity_sha256"]
            or value.get("exact_fixed_target_identity_sha256")!=context["actual"]["exact_fixed_target_identity_sha256"]
            or value.get("mathematical_target_identity_sha256")!=context["actual"]["mathematical_target_identity_sha256"]
            or value.get("accurate_request")!=job["request"]
            or value.get("normal_journal_binding_identity_sha256")!=job["identity"]
            or value.get("physical_stream")!=job["physical"]["file"]
            or value.get("original_journal")!=job["summary"]["journal"]
            or value.get("original_journal_header")!=job["summary"]["journal_header"]
            or value.get("original_complete_stage_count")!=32
            or value.get("complete_radial_leaf_count")!=job["physical"]["complete_radial_leaf_count"]
            or value.get("complete") is not True):
        raise ValueError("A saved complete integral block belongs to a different source or actual field")
    values=value.get("upper_oriented_flux_integrals")
    if not isinstance(values,dict) or set(values)!=set(k.CHANNELS):
        raise ValueError("Keep every original complete moment channel")
    value["upper_oriented_flux_integrals"]={name:k.box(values[name],context["bits"]) for name in k.CHANNELS}
    value["upper_parametric_area"]=k.box(value["upper_parametric_area"],context["bits"])
    if value["upper_parametric_area"].lo<0 or k.rational(value["whole_cell_position_norm_upper"])<0:
        raise ValueError("A magnitude enclosure must be nonnegative")
    return value,record


def completed_flux(context,blocks,k):
    upper=k.zero_moments(context["bits"])
    area=k.Interval(0,bits=context["bits"])
    radius=F(0)
    for block,_ in blocks.values():
        upper=k.add_moments(upper,block["upper_oriented_flux_integrals"])
        area=area+block["upper_parametric_area"]
        radius=max(radius,k.rational(block["whole_cell_position_norm_upper"]))
    return upper,area,radius


def complete_closed_flux(context,upper,upper_area,active_radius,k):
    sides=k.reflected_upper_and_lower(upper)
    caps=k.flat_cap_moments(context["R"],context["H"],context["pi"])
    whole=k.add_moments(sides,caps)
    caps_area=2*context["pi"]*context["R"].square()
    marked_area_upper=2*upper_area.hi+caps_area.hi
    for radius in (F(1,25),F(9,200),F(1,20),F(11,200)):
        slope=F(2,1000)/radius
        excess=context["pi"]*radius*radius*(k.Interval(1+slope*slope,bits=context["bits"]).sqrt()-1)
        marked_area_upper+=excess.hi
    cap_norm=(context["R"].square()+context["H"].square()).sqrt()
    Dupper=2*max(active_radius,cap_norm.hi)+F(2,1000)
    return dict(upper_flux=upper,reflected_upper_plus_lower_flux=sides,
        analytic_two_flat_cap_flux=caps,formal_unmarked_closed_flux=whole,
        upper_parametric_area=upper_area,
        complete_unmarked_parametric_area_upper=str(2*upper_area.hi+caps_area.hi),
        marked_parametric_area_upper=str(marked_area_upper),
        full_physical_phase_image_diameter_upper=str(Dupper),
        actual_S=context["S"],actual_R=context["R"],actual_H=context["H"],
        accurate_pi=context["pi"],
        all_t_image_bound_is_conditional_on_the_exact_R248_phase_assembly=True,
        no_markers_added_to_unmarked_A2=True,
        cap_A2_exact_zero_by_complete_angular_integral=True,
        cap_volume_retained_from_actual_same_field_R_and_H=True,
        lower_orientation_is_Fs_cross_Fphi=True,
        formal_lower_definition_is_diag_1_1_minus1_of_whole_upper=True,
        actual_unmarked_embedded_bounded_volume_interpretation_certified=False,
        fixed_marker_external_tube_and_disjointness_certified=False)


def parse_args():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--normal-fee-report",type=Path,required=True)
    p.add_argument("--normal-fee-report-sha256")
    p.add_argument("--outdir",type=Path,required=True)
    p.add_argument("--seconds",type=float,default=600.)
    p.add_argument("--maximum-angle-blocks",type=int,default=0,
        help="Zero retains all complete planned circle blocks; a positive scheduling limit leaves the rest explicitly unfinished")
    args=p.parse_args()
    if not math.isfinite(args.seconds) or args.seconds<=0 or args.maximum_angle_blocks<0:
        raise ValueError("Use a positive explicit time budget and nonnegative scheduling limit")
    return args


def main():
    args=parse_args()
    require_actions()
    started=time.monotonic()
    k,kernel_path=load_kernel(args.repo)
    files=Files()
    files.add(__file__)
    files.add(kernel_path)
    outdir=args.outdir.resolve()
    repo=args.repo.resolve()
    if outdir==repo or repo in outdir.parents:
        raise ValueError("All complete scientific streams and moment outputs stay outside the repository")
    expected_input=args.normal_fee_report.resolve()
    if expected_input==outdir or outdir in expected_input.parents:
        raise ValueError("The complete output namespace must not contain even a pending normal-fee input")
    if not args.normal_fee_report.exists():
        files.protect_output(outdir)
        value=dict(schema=SCHEMA,source_sha256=sha(__file__),arithmetic_source_sha256=KERNEL[1],
            source_commit=os.environ.get("GITHUB_SHA"),github_run_id=os.environ.get("GITHUB_RUN_ID"),
            github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),complete=False,
            actual_input_available=False,
            expected_normal_fee_report_path=str(args.normal_fee_report.resolve()),
            full_domain_upper_flux_integrals=None,full_closed_parametric_flux=None,
            reason="The actual complete accurate normal-fee report does not exist",
            missing_input_is_not_a_failed_field_or_an_empty_domain=True,
            existing_working_F_J_root_calls=0,mathematical_problem_completion_claimed=False)
        record=write_report(outdir/"report.json",value,k)
        print(json.dumps(dict(report=record,complete=False,actual_input_available=False),sort_keys=True))
        return 0
    context=bind_input(args.normal_fee_report,args.normal_fee_report_sha256,args.repo,files,k)
    files.protect_output(outdir)
    snapshot=immutable_bytes(outdir/"inputs"/("normal-report-"+context["record"]["sha256"]+".json"),context["raw"])
    if not context["available"]:
        files.recheck()
        value=dict(schema=SCHEMA,source_sha256=sha(__file__),arithmetic_source_sha256=KERNEL[1],
            source_commit=os.environ.get("GITHUB_SHA"),github_run_id=os.environ.get("GITHUB_RUN_ID"),
            github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),complete=False,
            actual_input_available=False,actual_normal_report=context["record"],
            immutable_normal_report_snapshot=snapshot,
            full_domain_upper_flux_integrals=None,full_closed_parametric_flux=None,
            reason=context["reason"],existing_working_F_J_root_calls=0,
            mathematical_problem_completion_claimed=False)
        record=write_report(outdir/"report.json",value,k)
        print(json.dumps(dict(report=record,complete=False,actual_input_available=False),sort_keys=True))
        return 0
    requests=context["binding"]["complete_angle_requests"]
    if len({q["id"] for q in requests})!=len(requests):
        raise ValueError("The original complete angular job identities are not unique")
    summaries=context["report"]["actual_jobs"]
    if len(summaries)!=len(requests) or any(s.get("request")!=q for s,q in zip(summaries,requests)):
        raise ValueError("Every original planned accurate angular job is retained in order")
    jobs={request["id"]:load_job(summary,request,context,files,k)
          for summary,request in zip(summaries,requests)}
    branch=complete_branch(context,jobs,k)
    half_turn=half_turn_branch(context,jobs,branch,k)
    files.protect_output(outdir)
    circles=[q for q in requests if q["kind"]=="full_angle_cell"]
    binding=dict(schema=SCHEMA,source_sha256=sha(__file__),arithmetic_source_sha256=KERNEL[1],
        actual_normal_fee_source_sha256=NORMAL_FEE_SOURCE[1],
        complete_normal_execution_binding=context["report"]["complete_binding"],
        complete_normal_execution_identity_sha256=context["binding_identity"],
        actual_model_identity_sha256=context["actual"]["model_identity_sha256"],
        actual_current_full_point_sha256=context["actual"]["current_full_point_sha256"],
        actual_snapshot_identity_sha256=context["actual"]["actual_snapshot_identity_sha256"],
        exact_fixed_target_identity_sha256=context["actual"]["exact_fixed_target_identity_sha256"],
        mathematical_target_identity_sha256=context["actual"]["mathematical_target_identity_sha256"],
        complete_actual_scientific_report=context["actual"]["scientific_report"],
        complete_point_layout_evidence=context["point"],
        outward_arithmetic_precision_bits=context["bits"],
        exact_full_angular_domain_over_pi=["0","2"],
        exact_full_upper_radial_domain=[["0","0"],["1","0"]],
        integration_channels=list(k.CHANNELS),
        complete_radial_plan_identity_sha256=canonical(context["plan"]),
        complete_circle_requests_identity_sha256=canonical(circles),
        range_integrals_pay_whole_boxes_without_sampled_quadrature=True,
        reflection_and_flat_caps_are_explicit_formal_surface_components=True,
        complete_boundary_embedding_orientation_and_fixed_cap_tube_are_separate=True)
    identity=canonical(binding)
    binding_record=immutable_json(outdir/"complete-binding.json",binding,k)
    blocks={}
    for request in circles:
        job=jobs[request["id"]]
        path=outdir/"blocks"/(request["id"]+".json")
        if path.exists():
            if job["complete"] is None:
                raise ValueError("An existing integral block has lost its original accurate whole-angle proof")
            blocks[request["id"]]=read_block(path,job,context,files,k,identity)
    new_blocks=0
    stopped=None
    def report():
        upper,area,radius=completed_flux(context,blocks,k)
        full_cover=bool(circles) and len(blocks)==len(circles)
        complete=full_cover and branch["complete"] and context["upstream_final_bytes_rechecked"]
        whole=complete_closed_flux(context,upper,area,radius,k) if complete else None
        return dict(schema=SCHEMA,source_sha256=sha(__file__),arithmetic_source_sha256=KERNEL[1],
            source_commit=os.environ.get("GITHUB_SHA"),github_run_id=os.environ.get("GITHUB_RUN_ID"),
            github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
            complete_binding=binding_record,complete_binding_identity_sha256=identity,
            actual_normal_report=context["record"],immutable_normal_report_snapshot=snapshot,
            actual_input_available=True,
            actual_model_identity_sha256=context["actual"]["model_identity_sha256"],
            actual_current_full_point_sha256=context["actual"]["current_full_point_sha256"],
            actual_snapshot_identity_sha256=context["actual"]["actual_snapshot_identity_sha256"],
            exact_fixed_target_identity_sha256=context["actual"]["exact_fixed_target_identity_sha256"],
        mathematical_target_identity_sha256=context["actual"]["mathematical_target_identity_sha256"],
            complete=complete,all_angular_radial_cells_integrated=full_cover,
            upstream_normal_final_bytes_rechecked=context["upstream_final_bytes_rechecked"],
            complete_same_field_branch_association=branch,
            expected_complete_circle_blocks=len(circles),completed_circle_blocks=len(blocks),
            remaining_circle_block_ids=[q["id"] for q in circles if q["id"] not in blocks],
            original_literal_jobs_preserved_for_branch_association=True,
            complete_integral_blocks=[blocks[q["id"]][1] for q in circles if q["id"] in blocks],
            partial_upper_flux_contribution_sum=upper,
            partial_contribution_is_not_a_whole_domain_integral=not complete,
            full_domain_upper_flux_integrals=upper if complete else None,
            full_closed_parametric_flux=whole,
            exact_current_height_and_whole_radius_from_original_field=True,
            endpoint_assembly_evidence=context["point"],
            source_defined_closed_parametric_extension_integrated=complete,
            exact_endpoint_gluing_formulas_and_full_layout_retained=True,
            C2_closed_image_embedding_certificate=False,
            closed_embedded_outward_boundary_proved=False,
            half_turn_signed_root_branch_covariance_proved=half_turn["complete"],
            complete_half_turn_branch_evidence=half_turn,
            external_marker_normal_tube_and_disjointness_proved=False,
            R716_conditional_integral_input_complete=complete,
            unconditional_R716_noncongruence_or_volume_certificate=False,
            original_working_F_J_root_calls=0,accurate_field_oracle_calls=0,
            accurate_whole_box_arithmetic_only=True,
            no_full_domain_obligation_was_removed=True,
            full_domain_integrals_remain_null_until_cover_and_branch_complete=True,
            deadline_stops_between_complete_angle_blocks_only=True,
            scheduling_stop_reason=stopped,
            elapsed_seconds_binary64_hex=float(time.monotonic()-started).hex(),
            mathematical_problem_completion_claimed=False)
    write_report(outdir/"report.json",report(),k)
    for request in circles:
        if request["id"] in blocks or jobs[request["id"]]["complete"] is None:
            continue
        if time.monotonic()-started>=args.seconds:
            stopped="Declared moment-processing time budget exhausted between complete blocks"
            break
        if args.maximum_angle_blocks and new_blocks>=args.maximum_angle_blocks:
            stopped="Declared complete-block scheduling limit reached; no domain was removed"
            break
        job=jobs[request["id"]]
        value=integrate_job(job,context,files,k,identity)
        value["immutable_normal_report_snapshot"]=snapshot
        path=outdir/"blocks"/(request["id"]+".json")
        immutable_json(path,value,k)
        blocks[request["id"]]=read_block(path,job,context,files,k,identity)
        new_blocks+=1
        write_report(outdir/"report.json",report(),k)
    files.recheck()
    final=report()
    record=write_report(outdir/"report.json",final,k)
    print(json.dumps(dict(schema=SCHEMA,report=record,complete=final["complete"],
        expected_complete_circle_blocks=len(circles),completed_circle_blocks=len(blocks),
        full_closed_embedded_volume_interpretation_certified=False,
        mathematical_problem_completion_claimed=False),sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
