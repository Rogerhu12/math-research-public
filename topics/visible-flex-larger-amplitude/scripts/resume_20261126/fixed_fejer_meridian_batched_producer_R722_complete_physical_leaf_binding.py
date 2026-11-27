#!/usr/bin/env python3
"""Complete actual-fixed-fejer R722 normal-chain and physical-leaf reader.

This independent whole-source reader binds the returned accurate producer,
the original full point/target and all original angular/stage journals. It
does not construct F, run a root, evaluate an integrand or produce geometry.
Complete uniform branch association is recomputed from the recorded accurate
root enclosures. All full-array reads and interval operations are Actions-only.
"""
from __future__ import annotations

from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys

SCHEMA="actual-fixed-fejer-meridian-batched-R722-complete-physical-sixjet-leaf-reader-v1"
TOPIC="topics/visible-flex-larger-amplitude"
NORMAL_FEE_SOURCE=("fixed_fejer_meridian_batched_producer_R722_complete_normal_root_and_sixjet_fees.py",
    "c6f6c9726b23ceb25533d5a6a6ac41fd31e8a3c14226895d5fc32e74787c0108")
ROTATION_SOURCE=("accurate_normal_rotation_and_stage_boxes.py",
    "29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b")
NORMAL_FEE_SCHEMA="actual-fixed-fejer-meridian-batched-R722-complete-normal-root-and-physical-sixjet-fees-v1"
JOURNAL_SCHEMA="actual-fixed-fejer-meridian-batched-R722-complete-normal-fee-journal-v1"
STREAM_SCHEMA="complete-actual-fixed-fejer-meridian-batched-R722-accurate-physical-sixjet-stream-v1"
ACTUAL_DRIVER = "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f"
ACTUAL_READER = "8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49"
ACTUAL_MODEL_SOURCE = "76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d"
ACTUAL_BASE = "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3"
ACTUAL_INPUT_SOURCE_PINS = {
    "reader": ("read_fixed_fejer_meridian_batched_so3_report.py", "8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49"),
    "driver": ("fullclosed_fixed_fejer_meridian_batched_so3_qp.py", "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f"),
    "packets": ("fixed_fejer_meridian_root_packets.py", "c750d234fc370d3c74da4577bc99f7fca417dbed169bc3a9d1e7222ea99c84b4"),
    "normal": ("fixed_fejer_detached_meridian_normal_lift.py", "76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d"),
    "base": ("fixed_fejer_supported_so3_meridian_operator.py", "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3"),
    "reference": ("fixed_fejer_axisymmetric_reference.py", "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"),
    "continuous": ("so3_axisymmetric_continuous_integrand.py", "a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6"),
    "reference_fees": ("fixed_fejer_reference_seed_angular_profile_error_bounds.py", "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b"),
    "mean_integrals": ("fixed_fejer_reference_accurate_mean_residuals.py", "ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0"),
    "fixed_input_binding": ("fixed_fejer_reference_input_binding.py", "3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f"),
    "field_binding": ("fixed_fejer_meridian_source_binding.py", "3ee65e2c45d6e9cb81fac1ad0a4c439a291aa2cc3fc73d68f896107c24e2ee68"),
}
BINDING_LOGIC_SOURCE_TEXT_ORIGIN="19e4ab31976615b12d002a6ef26c15973859fc4268134b5fd61676206e9c11b4"
POSTERIOR_MEAN_SOURCE=("fixed_fejer_meridian_batched_producer_R722_posterior_mean_jets.py",
    "4fc252f8977f4f4246d2cc13583efc0bccd4b28742df3a797d1c266cdd1eac7d")

ACCURATE_INPUT_SOURCE = ("fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py", "d892bedeadca4fe0689069ac7489a41c1d348311c2b84dad292bf48133e71cc7")


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("Complete physical-leaf consumption runs only in public repository Actions")


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
            "d892bedeadca4fe0689069ac7489a41c1d348311c2b84dad292bf48133e71cc7"),
        "accurate_rotation":("accurate_normal_rotation_and_stage_boxes.py",
            "29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b"),
        "accurate_radial":("fixed_fejer_meridian_batched_producer_R722_accurate_reference_control_radial_boxes.py",
            "7c66ed0f31323451156c1cd76ae7401eb497f37377393bb66503523ad2aaac54"),
        "posterior_mean":POSTERIOR_MEAN_SOURCE}
    if not isinstance(roles,dict) or set(roles)!=set(expected_names):
        raise ValueError("The complete normal-fee role set changed")
    for role,(name,expected) in expected_names.items():
        path=root/name
        if roles[role]!=expected or sha(path)!=expected:
            raise ValueError("An accurate field role differs from its original producer binding")
        files.add(path)
    expected_actual={role:value[1] for role,value in ACTUAL_INPUT_SOURCE_PINS.items()}
    if binding["actual_complete_input"].get("source_sha256_by_role")!=expected_actual:
        raise ValueError("The complete accurate input's eleven source roles changed")
    for role,(name,digest) in ACTUAL_INPUT_SOURCE_PINS.items():
        path=root/name
        if sha(path)!=digest:
            raise ValueError("A complete reference/root/profile fee dependency changed: "+role)
        files.add(path)
    return roles

def bind_posterior_mean_sources(actual,geometry,repo,files):
    """Read original producer records and bind complete current source copies."""
    require_actions()
    metadata=geometry.get("posterior_mean")
    if not isinstance(metadata,dict):
        raise ValueError("The complete posterior mean source/theorem attribution is missing")
    original_source=metadata["source"]
    original_theorem=metadata["theorem_source"]
    files.verify(original_source,force=True)
    files.verify(original_theorem,force=True)
    root=Path(repo).resolve()/TOPIC/"scripts/resume_20261126"
    def load_complete(role,name,digest):
        path=(root/name).resolve()
        record=file_record(path)
        if record["sha256"]!=digest:
            raise ValueError("A complete posterior-mean mathematical source changed: "+role)
        files.verify(record)
        spec=importlib.util.spec_from_file_location("_fixed_fejer_R722_leaf_"+role,path)
        module=importlib.util.module_from_spec(spec)
        sys.modules[spec.name]=module
        spec.loader.exec_module(module)
        files.verify(record,force=True)
        if Path(module.__file__).resolve()!=path or sha(module.__file__)!=digest:
            raise ValueError("Use the entire pinned posterior-mean mathematical source")
        return module,record
    posterior,current_source=load_complete("posterior",*POSTERIOR_MEAN_SOURCE)
    parent,parent_source=load_complete("parent_math",*ACTUAL_INPUT_SOURCE_PINS["reference_fees"])
    if (original_source["sha256"]!=current_source["sha256"]
            or original_source["bytes"]!=current_source["bytes"]
            or original_theorem["sha256"]!=posterior.THEOREM_SHA256
            or original_theorem["bytes"]!=posterior.THEOREM_BYTES
            or parent_source["sha256"]!=posterior.PARENT_MATH_SHA256):
        raise ValueError("Original proof/source records differ from their complete pinned copies")
    for name in ("definition","validate_root_domain_attribution","bind_parent_math"):
        if Path(getattr(posterior,name).__code__.co_filename).resolve()!=Path(posterior.__file__).resolve():
            raise ValueError("The complete posterior validator is not from its bound source")
    posterior.bind_parent_math(parent)
    definition=posterior.definition()
    expected=dict(schema=posterior.SCHEMA,source=original_source,
        theorem_source=original_theorem,definition=definition,
        definition_identity_sha256=canonical(definition),
        actual_input_identity=canonical(actual),
        original_complete_math_source_sha256=posterior.PARENT_MATH_SHA256,
        complete_root_domain_and_original_jet_arithmetic_source_explicit=True,
        whole_circle_normal_or_geometry_completion_inferred=False)
    if metadata!=expected:
        raise ValueError("The entire posterior mean source/theorem/actual-input definition changed")
    return posterior,parent


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
        source_layout_assertion="552f75 literal unpack excludes exactly these complete rows",
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


def bind_fixed_reference_scope(actual, outer, repo, files):
    """Independently re-read the actual new-target closure before consuming leaves."""
    root = Path(repo).resolve()/TOPIC/"scripts/resume_20261126"
    input_name, input_digest = ACTUAL_INPUT_SOURCE_PINS["fixed_input_binding"]
    actual_input_name, actual_input_digest = ACCURATE_INPUT_SOURCE
    source = root/actual_input_name
    if sha(source) != actual_input_digest:
        raise ValueError("The complete accurate-input constructor changed")
    files.add(source)
    spec = importlib.util.spec_from_file_location("_fixed_fejer_leaf_actual_input", source)
    actual_module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = actual_module
    spec.loader.exec_module(actual_module)
    if sha(source) != actual_input_digest:
        raise ValueError("The accurate-input source changed during loading")
    module = actual_module.load("_fixed_fejer_leaf_input_binding", root/input_name, input_digest)
    book = actual_module.VerifiedFiles()
    state = actual_module.bind_fixed_reference_inputs(outer,
        actual.get("complete_actual_fixed_reference_input_binding"), module, book)
    for record in book.used.values():
        files.verify(record)
    expected = {
        "exact_fixed_target_identity_sha256": state["exact_fixed_target_identity_sha256"],
        "actual_reference_model_identity_sha256": state["actual_reference_model_identity_sha256"],
        "fixed_chart_core_sha256": state["fixed_chart_core_sha256"],
        "mathematical_target_identity_sha256": state["mathematical_target_identity_sha256"],
        "complete_six_actual_inputs": state["complete_current_input_files"],
    }
    if any(actual.get(key) != value for key, value in expected.items()):
        raise ValueError("The complete actual field binding changed its recipe, chart or any actual input")
    base = actual["complete_model"]["base_complete_model"]
    reference = base["complete_axisymmetric_reference_model"]
    if (base.get("fixed_chart_core_sha256") != expected["fixed_chart_core_sha256"]
            or canonical(reference) != expected["actual_reference_model_identity_sha256"]
            or reference.get("fixed_chart_core_sha256") != expected["fixed_chart_core_sha256"]):
        raise ValueError("The normal/base/reference chain differs from the actual fixed chart")
    return state


def bind_input(report_path,expected_sha,repo,files,k):
    require_actions()
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
    fixed_reference_scope=bind_fixed_reference_scope(actual,outer,repo,files)
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
    H=k.point(k.rational(geometry["current_H"]),bits)
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
    posterior,parent_math=bind_posterior_mean_sources(actual,geometry,repo,files)
    return dict(available=True,record=record,raw=raw,report=report,binding=binding,
        posterior_mean_module=posterior,posterior_parent_math=parent_math,
        binding_identity=identity,actual=actual,actual_identity=actual_id,geometry=geometry,
        fixed_reference_scope=fixed_reference_scope,
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
        posterior=context["posterior_mean_module"]
        parent_math=context["posterior_parent_math"]
        if (mean.get("schema")!="same-actual-reference-whole-angle-R722-posterior-mean-enclosure-v1"
                or mean.get("actual_input_identity")!=context["actual_identity"]
                or mean.get("geometry_identity")!=context["geometry"]["identity"]
                or mean.get("accurate_phi_interval")!=request["accurate_phi_interval"]
                or mean.get("candidate_literal_phi_hex")!=request["actual_anchor"]
                or mean.get("all_original_mean_radial_pieces_included") is not True
                or type(mean.get("sufficient_R709_inequalities_verified_on_this_whole_interval")) is not bool
                or mean.get("posterior_R722_existence_verified_on_this_whole_interval") is not True
                or mean.get("complete_pointwise_theorem_source_sha256")!=POSTERIOR_MEAN_SOURCE[1]
                or mean.get("complete_shared_R710_R711_math_source_sha256")!=posterior.PARENT_MATH_SHA256
                or mean.get("complete_R722_theorem_sha256")!=posterior.THEOREM_SHA256
                or mean.get("whole_interval_bounds_computed_here") is not True):
            raise ValueError("The complete whole-angle posterior mean is not the same actual field/request")
        checked=posterior.validate_root_domain_attribution(
            mean["complete_posterior_mean_root_domain"],parent_math=parent_math,
            actual_binding=context["actual"],geometry_identity=context["geometry"]["identity"],
            phi_interval=request["accurate_phi_interval"],
            total_equation=mean["complete_accurate_total_equation"],
            exact_partition=mean["exact_partition"],
            active_leaves=mean["complete_active_leaves"],
            structural_reference=mean["structural_boundary_unit_proof"],
            files=files,bits=context["bits"])
        scope=mean["complete_posterior_mean_root_domain"]["definition"]["source_scope"]
        if (checked["original_R709_coarse_inequalities_proved"]!=mean[
                "sufficient_R709_inequalities_verified_on_this_whole_interval"]
                or scope["candidate_literal_phi_hex"]!=request["actual_anchor"]
                or mean["complete_actual_mean_candidate"]!=scope["complete_actual_candidate_source"]):
            raise ValueError("The actual posterior candidate or original true-or-false R709 result changed")
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
        "full_R722_unique_reference_mean_and_projected_frame_are_two_pi_periodic",
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

class Arithmetic:
    """An explicit adapter; the pinned arithmetic module itself is not modified."""
    def __init__(self,module):
        self.module=module

    def __getattr__(self,name):
        return getattr(self.module,name)

    @staticmethod
    def integer(value,*,minimum=None,maximum=None):
        if type(value) is not int:
            raise ValueError("Keep an exact integer count, never a Boolean or rounded value")
        if minimum is not None and value<minimum or maximum is not None and value>maximum:
            raise ValueError("An exact count lies outside its declared domain")
        return value


def load_arithmetic(repo,files):
    path=Path(repo).resolve()/TOPIC/"scripts/resume_20261126"/ROTATION_SOURCE[0]
    record=file_record(path)
    if record["sha256"]!=ROTATION_SOURCE[1]:
        raise ValueError("The complete outward arithmetic source changed")
    files.verify(record)
    spec=importlib.util.spec_from_file_location("_fixed_fejer_geometry_complete_interval_kernel",path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    files.verify(record,force=True)
    if Path(module.__file__).resolve()!=path or sha(module.__file__)!=ROTATION_SOURCE[1]:
        raise ValueError("The imported arithmetic is not the entire pinned source")
    return Arithmetic(module),record


def verify_geometry_identity(context,k):
    if not context["available"]:
        return
    g,b,a=context["geometry"],context["binding"],context["actual"]
    p=b["complete_parameters"]
    definition=dict(
        schema="actual-fixed-fejer-meridian-batched-R722-complete-accurate-reference-control-radial-boxes-v1",
        source_sha256=b["complete_source_sha256_by_role"]["accurate_radial"],
        complete_actual_input_identity=context["actual_identity"],
        precise_field_model=a["model_identity_sha256"],
        rotation_source_sha256=ROTATION_SOURCE[1],
        reference_math_source_sha256="0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b",
        complete_mean_integral_source_sha256="ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0",
        whole_scalar_source_sha256="a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6",
        posterior_mean_source_sha256=POSTERIOR_MEAN_SOURCE[1],
        posterior_mean_theorem_sha256=context["posterior_mean_module"].THEOREM_SHA256,
        posterior_mean_definition_identity_sha256=g["posterior_mean"]["definition_identity_sha256"],
        precision_bits=context["bits"],complete_exact_radial_plan=context["plan"],
        fixed_rho_proof=g["fixed_rho_proof"],current_rho_proof=g["current_rho_proof"],
        inverse_steps=p["inverse_steps"],inverse_width=str(k.rational(p["inverse_width"])),
        all_outer_variables_retained=True,working_mesh_is_not_the_accurate_domain=True,
        no_working_normal_root_or_field_replayed=True)
    if canonical(definition)!=g["identity"] or g.get("precision_bits")!=context["bits"]:
        raise ValueError("The complete accurate geometry definition is not canonical")
    if (a.get("schema")!="actual-fixed-fejer-meridian-batched-complete-normal-packet-accurate-field-input-v1"
            or a.get("source_sha256")!=b["complete_source_sha256_by_role"]["actual_input"]
            or a.get("fixed_scalar_metric_identity_sha256")!=
                a["complete_model"]["base_complete_model"]["fixed_scalar_metric_identity_sha256"]):
        raise ValueError("The scalar metric and entire actual field input must agree")


def read_all_jobs(context,files,k):
    require_actions()
    verify_geometry_identity(context,k)
    if not context["available"]:
        return {},dict(complete=False,full_circle_requested=False,
            reason=context["reason"])
    requests=context["binding"]["complete_angle_requests"]
    summaries=context["report"].get("actual_jobs")
    if not isinstance(summaries,list) or len(summaries)!=len(requests):
        raise ValueError("Retain every original literal and whole-angle job, including incomplete jobs")
    ids=[q.get("id") for q in requests]
    if len(set(ids))!=len(ids) or any(not isinstance(q,str) for q in ids):
        raise ValueError("All original angular job identifiers must be unique")
    actual=[q for q in requests if q.get("kind")=="actual_literal"]
    cached=context["actual"]["complete_cached_literal_angles"]
    required=context["actual"]["complete_required_literal_angles"]
    if ([q.get("literal_phi_hex") for q in actual]!=cached or len(set(cached))!=len(cached)
            or not set(required).issubset(cached)):
        raise ValueError("The original complete cached and required angle words changed")
    for i,q in enumerate(actual):
        word=q["literal_phi_hex"]
        value=float.fromhex(word)
        if (not math.isfinite(value) or value.hex()!=word or q.get("id")!="actual-"+str(i).zfill(6)
                or q.get("original_cache_index")!=i or q.get("actual_anchor")!=word
                or q.get("original_required_angle")!=(word in required)
                or q.get("accurate_phi_interval")!=[str(F(value)),str(F(value))]):
            raise ValueError("A literal-angle job was rounded, wrapped or relabelled")
    if any(q.get("kind") not in ("actual_literal","full_angle_cell") for q in requests):
        raise ValueError("Unknown angular job kind")
    jobs={q["id"]:load_job(summary,q,context,files,k)
          for q,summary in zip(requests,summaries)}
    report=context["report"]
    if (report.get("planned_job_count")!=len(requests)
            or report.get("completed_job_count")!=sum(j["complete"] is not None for j in jobs.values())
            or report.get("all_original_recorded_angle_count")!=len(cached)
            or report.get("all_original_required_angle_count")!=len(required)):
        raise ValueError("The whole report counts differ from all original journals")
    return jobs,complete_branch(context,jobs,k)


def physical_cells(job,context,files,k):
    """Yield complete cells; exhaust this generator before committing any output."""
    require_actions()
    if job["complete"] is None or job["request"]["kind"]!="full_angle_cell":
        raise ValueError("Only a completed original whole-angle chain supplies continuous cells")
    record=job["physical"]["file"]
    path=files.verify(record)
    expected=iter(refined_leaves(context,k))
    count=0
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
            raise ValueError("The complete sixjet stream belongs to another point or stage chain")
        for raw in handle:
            if not raw.endswith(b"\n"):
                raise ValueError("A partial physical-stream line is not a complete interval cell")
            value=strict_json(raw)
            if value.get("kind")=="complete_radial_cover_footer":
                footer=value
                break
            if value.get("kind")!="complete_closed_radial_cell":
                raise ValueError("Unknown record in the whole sixjet stream")
            leaf=next(expected,None)
            count+=1
            if (leaf is None or value.get("ordinal")!=count
                    or value.get("exact_radial_leaf")!=leaf
                    or value.get("accurate_phi_interval")!=job["request"]["accurate_phi_interval"]
                    or value.get("all_same_field_radial_and_angular_chains_retained") is not True
                    or value.get("original_working_physical_field_arrays_compared") is not False):
                raise ValueError("A full accurate physical leaf was changed, duplicated or omitted")
            if radial_end is not None and radial_end!=leaf["left"]:
                raise ValueError("The complete physical stream contains a radial gap")
            radial_end=leaf["right"]
            affine_width(leaf["left"],leaf["right"],context["S"],k)
            scalar=value.get("accurate_fixed_scalar")
            fields=value.get("physical_sixjets")
            if not isinstance(scalar,dict) or not isinstance(fields,dict):
                raise ValueError("Keep every complete physical sixjet and same-target scalar box")
            if (scalar.get("fixed_scalar_metric_identity_sha256")!=
                    context["actual"]["fixed_scalar_metric_identity_sha256"]
                    or scalar.get("accurate_S")!=context["geometry"]["accurate_S"]
                    or scalar.get("accurate_R")!=context["geometry"]["accurate_R"]
                    or scalar.get("enclosure_formula")!=
                        "a_deep(s)=R-integral_s^S b; complete exact-width whole-leaf suffix"
                    or scalar.get("full_same_scalar_infinite_tail_included") is not True
                    or scalar.get("working_observation_or_quadrature_values_treated_as_exact") is not False
                    or fields.get("raw_lift_or_reference_error_dropped") is not False
                    or fields.get("original_working_sixjet_words_supplied") is not False):
                raise ValueError("The same accurate scalar, infinite tail or full physical lift was dropped")
            for name in ("a_deep","b","c","bs","cs"):
                k.box(scalar[name],context["bits"])
            k.box(fields["rho0"],context["bits"])
            for name in ("F","Fs","Fphi","Fss","Fsphi","Fphiphi"):
                row=fields.get(name)
                if not isinstance(row,list) or len(row)!=3:
                    raise ValueError("Keep all six complete three-dimensional physical jet vectors")
                for v in row:
                    k.box(v,context["bits"])
            raw_defects=fields.get("all_three_raw_accurate_closure_defects")
            if (not isinstance(raw_defects,list) or len(raw_defects)!=3
                    or any(not isinstance(row,list) or len(row)!=3 for row in raw_defects)):
                raise ValueError("Retain all three complete raw physical endpoint-defect jets")
            for row in raw_defects:
                for v in row:
                    k.box(v,context["bits"])
            yield value
        if handle.read(1):
            raise ValueError("No record may follow the complete radial footer")
    files.verify(record,force=True)
    if (footer is None or footer.get("all_exact_radial_leaves_written") is not True
            or footer.get("full_closed_surface_seams_or_reach_certified") is not False
            or footer.get("working_sixjet_words_not_supplied") is not True
            or footer.get("complete_radial_leaf_count")!=count
            or job["physical"]["complete_radial_leaf_count"]!=count
            or next(expected,None) is not None
            or affine(radial_end,k)!=(F(1),F(0))):
        raise ValueError("The whole accurate radial stream has not been completely consumed")
