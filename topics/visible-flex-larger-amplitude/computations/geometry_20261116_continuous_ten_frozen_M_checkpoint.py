#!/usr/bin/env python3
"""R442 actual continuous-ten frozen-M physical-DN checkpoint.

A real freshly solved 4M+2 problem, full current-H FD, complete (3M+2) by M
endpoint response, both means and fresh original native audit are inputs.
An old R400/R441 or own M checkpoint is a true parent and initial guess,
never a cache or an accepted zero-padded high-mode field. The whole actual
scalar specification is compared except its two explicit dimension fields.
Every original acceptance threshold and current-source responsibility remains.
All scientific execution and temporary payload ownership are public Actions.
"""
from __future__ import annotations
import argparse
import copy
import gzip
import hashlib
import importlib.util
import inspect
import json
import math
import os
from pathlib import Path
import re
import shutil
import struct
import sys

REPOSITORY="Rogerhu12/math-research-public"
HERE=Path(__file__).resolve().parent
SCHEMA="R442-current-continuous-ten-frozen-M-physical-DN-checkpoint-v1"
ORIGINAL_CHECKPOINT_NAME="geometry_20261115_continuous_ten_frozen450_checkpoint.py"
ORIGINAL_CHECKPOINT_SHA="43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae"
ORIGINAL_CHECKPOINT_SCHEMA="R400-current-continuous-ten-complete-physical-DN-checkpoint-v1"
PROFILE_NAME="geometry_20261116_continuous_ten_M_same_metric_profile.py"
PROFILE_SHA="cc70e7699a817c5715e12de2b131d1a381082f630f0fdadf3648d9a8bec0151a"
ORIGINAL_NAME="geometry_20261114_full_dn_solve.py"
ORIGINAL_SHA="c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162"
AUGMENTED_NAME="geometry_20261114_full_dn_augmented.py"
AUGMENTED_SHA="f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e"
BOUNDARY_NAME="geometry_20261114_physical_test_boundary.py"
BOUNDARY_SHA="3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681"
CUT_AUDIT_NAME="geometry_20261114_physical_test_cut_audit.py"
CUT_AUDIT_SHA="7a548961ff0bd3e5171db18f1133d42f606be19e65e5d2e919432514042ba420"
RESOLUTION_CHECKPOINT_NAME="geometry_20261116_continuous_ten_resolution_checkpoint.py"
RESOLUTION_CHECKPOINT_SHA="bf7dedd2135e3f6b54bc806a17064428111b502b6ddb8572ec66a883b1ce34ad"
RESOLUTION_CHECKPOINT_SCHEMA="R441-current-continuous-ten-resolution450-physical-DN-checkpoint-v1"
DEPTH=576
P=None


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise RuntimeError("Use the named public repository Actions for the actual checkpoint")


def load_profile(code_directory=HERE):
    global P
    require_actions()
    path=Path(code_directory)/PROFILE_NAME
    if hashlib.sha256(path.read_bytes()).hexdigest()!=PROFILE_SHA:
        raise ValueError("The independent continuous-ten profile source differs")
    if P is None:
        for loaded in tuple(sys.modules.values()):
            filename=getattr(loaded,"__file__",None)
            if (filename is not None and Path(filename).resolve()==path.resolve()
                    and hasattr(loaded,"CurrentTenProfile")):
                P=loaded;break
    if P is None:
        spec=importlib.util.spec_from_file_location("_r400_continuous_ten_profile",path)
        P=importlib.util.module_from_spec(spec);sys.modules[spec.name]=P
        try:spec.loader.exec_module(P)
        except BaseException:
            P=None;sys.modules.pop(spec.name,None);raise
    elif Path(P.__file__).resolve()!=path.resolve():
        raise ValueError("One checkpoint process must use one actual profile source directory")
    return P


def own_identity():
    raw=Path(__file__).read_bytes()
    return dict(file=Path(__file__).name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def source_of_module(module,name,expected):
    path=Path(module.__file__)
    if path.name!=name or P.identity(path)["sha256"]!=expected:
        raise ValueError("Actually loaded original module differs: "+name)
    return P.identity(path)


def source_closure(directory,expected):
    if not isinstance(expected,dict) or not expected:
        raise ValueError("Retain the actual complete source closure, not a producer name only")
    out={}
    for name,digest in expected.items():
        if (not isinstance(name,str) or Path(name).name!=name
                or re.fullmatch(r"[0-9a-f]{64}",str(digest)) is None):
            raise ValueError("Use explicit local source basenames and full SHA256 values")
        path,rec=P.source(directory,name,digest);out[name]=rec
    return out


def copied(original,destination,root):
    original,destination,root=map(Path,(original,destination,root))
    if (not destination.resolve().is_relative_to(root.resolve())
            or destination.exists() or destination.resolve()==original.resolve()):
        raise ValueError("Copy original bytes only to a fresh owned member")
    destination.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(original,destination)
    before,after=P.identity(original),P.identity(destination,root)
    if (before["bytes"],before["sha256"])!=(after["bytes"],after["sha256"]):
        raise OSError("A complete temporary input copy changed its bytes")
    return after


def actual_json(path,expected=None):
    path=Path(path)
    if expected is None:expected=P.identity(path)["sha256"]
    return P.original_json(path,expected)


def finite_number(value,label):
    if type(value) not in (int,float) or not math.isfinite(value):
        raise ValueError("Keep the actual finite scalar: "+label)
    return value


def original_acceptance(data):
    if (data.get("source_sha256")!=ORIGINAL_SHA or data.get("success") is not True
            or data.get("status")!=0 or not isinstance(data.get("actual_tail"),dict)):
        raise ValueError("Use the actual unannotated result emitted by the unchanged full-DN core")
    result={}
    for name,upper in (("collocation_rms_max",1e-6),
                       ("boundary_residual_max",1e-11),
                       ("physical_frozen_control_RMS_max",1e-6)):
        value=finite_number(data.get(name),name)
        if not 0<=value<=upper:
            raise ValueError("The original complete finite gate was not met: "+name)
        result[name]=value
    if re.fullmatch(r"[0-9a-f]{64}",str(data["actual_tail"].get("final_response_sha256",""))) is None:
        raise ValueError("The actual audited final response identity is absent")
    return result


def complete_arrays(np,data,k,profile,expected_parameters):
    """Validate layout and source equality; retain measured constant-row drift."""
    M=P.field_modes(profile.M);n=3*M+2;dimension=4*M+2+k
    x=np.asarray(data["mesh"],dtype=float)
    Y=np.asarray(data["states"],dtype=float)
    DY=np.asarray(data["rhs"],dtype=float)
    U=np.asarray(data["augmented_states"],dtype=float)
    DU=np.asarray(data["augmented_rhs"],dtype=float)
    c=np.asarray(data["core"]["coefficients"],dtype=float)
    if (data.get("M")!=M or type(data.get("N")) is not int
            or data["N"]<=8*M or data["N"]%2
            or x.ndim!=1 or len(x)<2 or x[0]!=0
            or P.word(x[-1])!=P.word(profile.end)
            or not np.all(np.isfinite(x)) or np.any(np.diff(x)<=0)
            or Y.shape!=(len(x),n) or DY.shape!=Y.shape
            or U.shape!=(len(x),dimension) or DU.shape!=U.shape
            or c.shape!=(M,)):
        raise ValueError("Every complete physical/core/scalar row and actual mesh node is required")
    if any(not np.all(np.isfinite(a)) for a in (Y,DY,U,DU,c)):
        raise ValueError("The accepted source contains nonfinite full-state data")
    if Y.astype("<f8").tobytes()!=U[:,:n].astype("<f8").tobytes():
        raise ValueError("The physical state is not the complete accepted augmented state")
    # The two RHS arrays are intentionally NOT required equal: physical RHS
    # was evaluated with final frozen controls, while augmented RHS preserves
    # every actual nodal control.  Both original arrays remain in the bundle.
    if P.words(c)!=P.words(U[0,1:M+1]):
        raise ValueError("The complete reported core differs from the original inlet words")
    active=U[-1,4*M+2:].copy()
    if P.words(active)!=P.words(data["scalar_parameters"]):
        raise ValueError("The original final active coordinates differ")
    if P.words(active)!=P.words(expected_parameters):
        raise ValueError("The selected scalar view differs from the actual endpoint")
    if k==0 and active.shape!=(0,):
        raise ValueError("The all-ten-frozen M problem has no active parameter rows")
    return dict(mesh=x,physical=Y,physical_rhs=DY,augmented=U,
        augmented_rhs=DU,core=c,active=active,
        array_identity={name:dict(shape=list(a.shape),dtype="<f8",
            sha256=hashlib.sha256(a.astype("<f8").tobytes()).hexdigest())
            for name,a in (("mesh",x),("physical_states",Y),("physical_rhs",DY),
                ("augmented_states",U),("augmented_rhs",DU),("core",c))},
        original_constant_core_state_drift=data.get("constant_core_state_drift"),
        original_constant_parameter_state_drift=data.get("constant_parameter_state_drift"))


def restored_height(np,response,mode_count):
    M=P.field_modes(mode_count)
    cp=response["checkpoint"]
    H=P.valid_vector(np,cp["cutHeight"],M,"Retain every actual full physical height")
    side=cp["cutHeight_negative_zero_columns"]
    if not isinstance(side,list) or side!=sorted(set(side)):
        raise ValueError("The original signed-zero height sidecar differs")
    for j in side:
        if type(j) is not int or not 0<=j<M or H[j]!=0:
            raise ValueError("The actual negative-zero height index differs")
        H[j]=-0.0
    raw=H.astype("<f8").tobytes()
    if hashlib.sha256(raw).hexdigest()!=cp["cutHeight_sha256"]:
        raise ValueError("The current full H raw word identity differs")
    return H


def full_final_native(np,response,config,native_identity):
    M=P.field_modes(config.get("field_modes"));K=2*M;n=3*M+2
    if (response.get("schema")!="current-C-complete-M-general-Robin-native-owner-v1"
            or response.get("actual_nonlinear_solve") is not True
            or response.get("converged") is not True or response.get("failed",False)
            or response.get("identity")!=native_identity
            or response.get("old_graphs_or_gains_used") is not False
            or response.get("old_finite_tail_output_relabelled") is not False
            or response.get("complete_infinite_C_nonlinear_DN_certified") is not False):
        raise ValueError("Use the actual current finite nonlinear owner, not a legacy or affine response")
    finite_number(response["normalizedResidual"],"actual normalizedResidual")
    cp=response["checkpoint"]
    if (cp.get("actual_current_native_call")!=response["call"]
            or cp.get("source_sha256") not in config["source_sha256"].values()
            or len(cp["rows"])!=577):
        raise ValueError("The actual complete current checkpoint source or node count differs")
    for i,row in enumerate(cp["rows"]):
        if row.get("node")!=i:
            raise ValueError("The complete native node order changed")
        P.valid_vector(np,row["state"],K,"Retain every native Q/Pi component")
        zero=row["negative_zero_columns"]
        if not isinstance(zero,list) or zero!=sorted(set(zero)):
            raise ValueError("The original native signed-zero sidecar differs")
        for j in zero:
            if type(j) is not int or not 0<=j<K or row["state"][j]!=0:
                raise ValueError("An original native negative-zero address differs")
    jets=response["jets"]
    for name in ("height","slope","second"):
        P.valid_vector(np,jets[name],M,"Retain all native "+name+" components")
    for name in ("radius","E","Ep","backgroundSlope","backgroundSecond","meanSlope","meanSecond"):
        finite_number(jets[name],"complete native jet "+name)
    J=P.valid_vector(np,response["heightJetJacobian"],n*M,"Retain the complete (3M+2) by M endpoint J")
    if (not isinstance(response.get("audit"),dict)
            or response["audit"].get("actual_all_stage_finite_audit") is not True):
        raise ValueError("The original fresh all-stage audit is required")
    H=restored_height(np,response,M)
    return dict(actual_call=response["call"],actual_owner=copy.deepcopy(native_identity),
        complete_height_float64le=P.words(H),
        complete_height_sha256=hashlib.sha256(H.astype("<f8").tobytes()).hexdigest(),
        decoded_complete_endpoint_J_float64le_sha256=hashlib.sha256(J.astype("<f8").tobytes()).hexdigest(),
        original_normalized_residual=response["normalizedResidual"],
        original_meanSlope=jets["meanSlope"],original_meanSecond=jets["meanSecond"],
        original_audit=copy.deepcopy(response["audit"]),
        complete_checkpoint_rows=DEPTH+1,complete_checkpoint_shape_columns=K,
        complete_endpoint_J_rows=n,complete_endpoint_J_columns=M,
        retained_original_height_and_both_mean_fields=True,
        original_JSON_does_not_certify_unexported_native_array_word_signs=True,
        finite_response_not_a_joint_exact_C_or_infinite_DN_certificate=True)


def native_context(owner,raw_client):
    """Bind the actual live client's files, common C object and true config."""
    P=load_profile(owner.code_directory)
    cfg=raw_client.config
    M=P.field_modes(owner.M)
    client_module=inspect.getmodule(type(raw_client))
    if client_module is None:
        raise ValueError("The actual current client source is unavailable")
    actual_client=P.identity(client_module.__file__)
    if (cfg.get("schema")!="current-C-complete-M-client-config-v1"
            or cfg.get("field_modes")!=M or raw_client.M!=M
            or cfg.get("model_schema")!=P.C_SCHEMA
            or cfg.get("repository")!=REPOSITORY
            or cfg["source_sha256"].get(actual_client["file"])!=actual_client["sha256"]):
        raise ValueError("Bind the actual current-C client and its explicit source configuration")
    policy={"max_iterations":32,"line_search_trials":10,"nonlinear_tolerance":2e-9,"sensitivity_eta":0}
    if any(cfg.get(k)!=v for k,v in policy.items()):
        raise ValueError("The original32/10/tolerance/full eta0 sensitivity policy changed")
    source_closure(raw_client.computations,cfg["source_sha256"])
    config,config_receipt=actual_json(raw_client.config_path,raw_client.config_receipt["sha256"])
    if config!=cfg:
        raise ValueError("The live configuration differs from the original complete file")
    geometry_directory=Path(cfg["geometry_directory"])
    report,receipt=actual_json(geometry_directory/"result.json",cfg["geometry_result_sha256"])
    if (report.get("native_geometry_ready") is not True or report.get("completed") is not True
            or report.get("source_sha256") not in cfg["source_sha256"].values()):
        raise ValueError("The actual current sampler has not produced its full geometry")
    ib=report["actual_original_input_binding"]
    if (P.original_C_core(ib["original_C_input_binding"])!=P.original_C_core(owner.data["complete_C_binding"])
            or ib["actual_cover_result"]["sha256"]!=owner.data["definition"]["continuous_tail"]["actual_result"]["sha256"]
            or P.rational(ib["original_binary_cut_exact_rational"])!=owner.data["cut"]):
        raise ValueError("The profile and complete current native geometry belong to different C inputs")
    geometry=P.member_json(geometry_directory,report["geometry"])
    if (geometry.get("schema")!="current-C-complete-M-native-radial-geometry-bundle-v1"
            or geometry.get("model_schema")!=P.C_SCHEMA
            or (geometry.get("modes"),geometry.get("stage_count"))!=(M,DEPTH)
            or geometry.get("native_old_graphs_or_gains_used") is not False
            or geometry["original_C_input_binding"]!=ib
            or geometry["numeric_geometry_identity"].get(
                "exact_global_C_realization_of_numeric_representatives_certified") is not False
            or P.rational(geometry["cut_radius"])!=owner.data["cut"]
            or geometry.get("steps_per_stage")!=cfg.get("steps")) :
        raise ValueError("Keep the full independently bound current-C numeric geometry")
    if raw_client.owner is None:
        raise ValueError("A merely configured client is not an actually created current owner")
    return dict(actual_client_source=actual_client,configuration=config_receipt,
        actual_geometry_result=receipt,geometry_descriptor=copy.deepcopy(report["geometry"]),
        sampler_source_sha256=report["source_sha256"],
        original_C_input_binding=copy.deepcopy(ib),
        actual_owner=copy.deepcopy(raw_client.owner),
        source_sha256=copy.deepcopy(cfg["source_sha256"]),
        original_runtime_sha256=copy.deepcopy(cfg["original_runtime_sha256"]),
        original_nonlinear_policy=policy,
        actual_complete_geometry_payload_not_copied_into_this_prefix_checkpoint=True,
        current_tail_radial_readout_or_shared_B_background_not_created=True),geometry_directory



def actual_resolution(field_N,config,boundary,owner_identity,field_mode_count):
    """Actual finite-program dimensions, never a target or error certificate."""
    M=P.field_modes(field_mode_count)
    values=dict(field_modes=M,field_angular_quadrature=field_N,
        native_quadrature=config.get("quadrature"),
        native_steps_per_stage=config.get("steps"),
        material_angles=boundary.get("material_angles"),
        physical_angles=boundary.get("physical_angles"),native_stage_count=576)
    if any(type(value) is not int or value<=0 for value in values.values()):
        raise ValueError("Keep all actual positive integer resolution fields")
    if (field_N<=8*M or field_N%2 or values["native_quadrature"]!=field_N
            or any(values[key]<=4*M or values[key]%2
                   for key in ("material_angles","physical_angles"))):
        raise ValueError("Retain the original resolved full-angle rules and declared common N")
    actual=owner_identity.get("parameter_record",{})
    expected=dict(modes=M,spacing=2,depth=DEPTH,quadrature=field_N,
        steps=values["native_steps_per_stage"])
    if any(actual.get(key)!=value for key,value in expected.items()):
        raise ValueError("The live original native owner does not use the bound resolution")
    return values


def resolution_from_checkpoint(parent):
    return actual_resolution(parent.raw["N"],parent.native_configuration,
        parent.manifest["original_physical_boundary_description"],
        parent.manifest["original_native_binding"]["actual_owner"],parent.raw["M"])


def bound_checkpoint_module(code_directory,basename,digest):
    path=Path(code_directory)/basename
    if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
        raise ValueError("The explicit complete parent reader source differs")
    for module in tuple(sys.modules.values()):
        filename=getattr(module,"__file__",None)
        if (filename is not None and Path(filename).resolve()==path.resolve()
                and hasattr(module,"Checkpoint")):
            return module
    name="_R442_actual_parent_"+digest
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    try:spec.loader.exec_module(module)
    except BaseException:sys.modules.pop(name,None);raise
    return module


def require_parent_instance(parent,code_directory):
    """Three explicit actual writer/reader sources; no label-only parent."""
    actual=inspect.getmodule(type(parent))
    filename=getattr(actual,"__file__",None)
    if filename is None or getattr(actual,"Checkpoint",None) is not type(parent):
        raise TypeError("An actual bound checkpoint reader instance is required")
    path=Path(filename).resolve()
    possibilities={Path(__file__).resolve():(SCHEMA,own_identity()["sha256"]),
        (Path(code_directory)/ORIGINAL_CHECKPOINT_NAME).resolve():
            (ORIGINAL_CHECKPOINT_SCHEMA,ORIGINAL_CHECKPOINT_SHA),
        (Path(code_directory)/RESOLUTION_CHECKPOINT_NAME).resolve():
            (RESOLUTION_CHECKPOINT_SCHEMA,RESOLUTION_CHECKPOINT_SHA)}
    if path not in possibilities:
        raise TypeError("Only the explicit R400, R441 or own-M actual parent is supported")
    schema,digest=possibilities[path]
    if (hashlib.sha256(path.read_bytes()).hexdigest()!=digest
            or parent.manifest.get("schema")!=schema
            or parent.manifest.get("writer_source",{}).get("sha256")!=digest
            or parent.k!=0):
        raise ValueError("Retain a genuine zero-active field from its actual reader source")
    if schema==SCHEMA:
        parent.require_frozen_M()
    else:
        parent.require_frozen450()
    resolution_from_checkpoint(parent)
    return parent


def load_parent_checkpoint(directory,manifest_sha256,code_directory=HERE):
    load_profile(code_directory)
    data,_=actual_json(Path(directory)/"checkpoint.json",manifest_sha256)
    schema=data.get("schema")
    if schema==SCHEMA:
        parent=Checkpoint(directory,manifest_sha256,code_directory)
    elif schema in (ORIGINAL_CHECKPOINT_SCHEMA,RESOLUTION_CHECKPOINT_SCHEMA):
        name,digest=((ORIGINAL_CHECKPOINT_NAME,ORIGINAL_CHECKPOINT_SHA)
            if schema==ORIGINAL_CHECKPOINT_SCHEMA else
            (RESOLUTION_CHECKPOINT_NAME,RESOLUTION_CHECKPOINT_SHA))
        module=bound_checkpoint_module(code_directory,name,digest)
        parent=module.Checkpoint(directory,manifest_sha256,code_directory)
    else:
        raise ValueError("No historical or unrecognised parent is relabelled as a new-M field")
    return require_parent_instance(parent,code_directory)


class LiveCheckpointWriter:
    """An explicit hook AFTER the unchanged original final acceptance.

    The caller supplies the actual runtime objects from the single live
    full-DN invocation.  The writer verifies these inputs and copies their
    existing files.  It cannot replace the solver/main, choose a future
    coefficient vector or treat a recipe/failed checkpoint as accepted.
    """
    def __init__(self,owner,flow,boundary,separated,original_core_module,
                 raw_client,*,driver_source,complete_source_sha256,
                 original_law,parent=None):
        P=load_profile(owner.code_directory)
        if not isinstance(owner,P.CurrentTenProfile):
            raise TypeError("Use the independent current-ten profile owner")
        np=owner.np;M=P.field_modes(owner.M);n=3*M+2;dimension=4*M+2
        if (flow.profile.current_C_boundary_binding["factory_result"]!=owner.binding["factory_result"]
                or flow.r300_profile_module is not owner.numeric
                or (flow.M,flow.n)!=(M,n) or flow.k not in (0,3)
                or flow.dimension!=dimension+flow.k
                or type(flow.q.N) is not int or flow.q.N<=8*M or flow.q.N%2
                or boundary.profile is not flow.profile
                or separated.original is not boundary
                or (boundary.M,boundary.T,boundary.K,boundary.k)!=(M,M,flow.k,flow.k)
                or (separated.dimension,separated.left_count)!=(dimension+flow.k,n+flow.k)):
            raise ValueError("Bind the real complete declared-M separated problem")
        source_of_module(original_core_module,ORIGINAL_NAME,ORIGINAL_SHA)
        source_of_module(flow.r300_original_module,AUGMENTED_NAME,AUGMENTED_SHA)
        boundary_module=inspect.getmodule(type(boundary))
        source_of_module(boundary_module,BOUNDARY_NAME,BOUNDARY_SHA)
        for table in (original_core_module.FROZEN_SOURCES,owner.consumed_source_sha256):
            for name,digest in table.items():
                if complete_source_sha256.get(name)!=digest:
                    raise ValueError("The original/current complete source closure omitted or changed "+name)
        closure=source_closure(owner.code_directory,complete_source_sha256)
        for name,digest in ((ORIGINAL_NAME,ORIGINAL_SHA),(PROFILE_NAME,PROFILE_SHA),
                (AUGMENTED_NAME,AUGMENTED_SHA),(BOUNDARY_NAME,BOUNDARY_SHA),
                (CUT_AUDIT_NAME,CUT_AUDIT_SHA)):
            if complete_source_sha256.get(name)!=digest:
                raise ValueError("The actual full-DN runtime closure omitted "+name)
        own=own_identity()
        if complete_source_sha256.get(own["file"])!=own["sha256"]:
            raise ValueError("The actual checkpoint writer is absent from the complete runtime closure")
        driver_source=Path(driver_source)
        driver=P.identity(driver_source)
        if complete_source_sha256.get(driver["file"])!=driver["sha256"]:
            raise ValueError("The actual independent entry source is not in its complete closure")
        if flow.k!=0 or parent is None:
            raise ValueError("R442 writes a freshly solved complete frozen-M field with an actual frozen parent")
        require_parent_instance(parent,owner.code_directory)
        if parent.raw["M"]>M:
            raise ValueError("This M refinement branch does not drop parent modes")
        if flow.k==3 and parent is not None:
            raise ValueError("The active-parameter writer does not assert frozen-parent refinement provenance")
        for name in ("velocity","length","k0"):
            finite_number(original_law[name],"actual original probe law "+name)
        native,geometry_directory=native_context(owner,raw_client)
        resolution=actual_resolution(flow.q.N,raw_client.config,
            boundary.description(),native["actual_owner"],M)
        self.resolution=resolution
        self.owner,self.flow,self.boundary,self.separated=owner,flow,boundary,separated
        self.original,self.raw_client=original_core_module,raw_client
        self.parent,self.native,self.geometry_directory=parent,native,geometry_directory
        self.source_closure,self.driver=closure,driver
        self.original_law=copy.deepcopy(original_law)

    def capture(self,*,original_result,fd_result,fd_anchor_response,
                final_native_response,physical_cut_audit,out):
        require_actions();P=load_profile(self.owner.code_directory)
        np=self.owner.np;M=self.owner.M;n=3*M+2;dimension=4*M+2;out=Path(out)
        temp=Path(os.environ["RUNNER_TEMP"]).resolve()
        if out.exists() or not out.resolve().is_relative_to(temp):
            raise ValueError("Use a fresh owned temporary checkpoint directory")
        inputs=[Path(v) for v in (original_result,fd_result,fd_anchor_response,
                                  final_native_response,physical_cut_audit)]
        if any(v.resolve().is_relative_to(out.resolve()) for v in inputs):
            raise ValueError("The checkpoint output cannot own an original input")
        raw,raw_receipt=actual_json(original_result)
        accepted=original_acceptance(raw)
        if raw["actual_tail"]["final_response_sha256"]!=P.identity(final_native_response)["sha256"]:
            raise ValueError("The final audit file differs from the original accepted result")
        active=np.asarray(raw["scalar_parameters"],dtype=float)
        expected=self.owner.current_parameters(self.flow.profile,active)
        arrays=complete_arrays(np,raw,self.flow.k,self.flow.profile,active)
        specification=self.flow.profile.export_specification(active)
        if raw["complete_scalar_profile"]!=specification:
            raise ValueError("The original scalar_spec hook did not retain this exact current profile")
        target=P.current_target_identity(self.owner,self.flow.profile,active)
        scalar_binding=P.same_scalar_target_across_modes(
            self.parent.owner,self.parent.profile,self.parent.owner.np.empty(0),
            self.owner,self.flow.profile,active)
        fd,fd_receipt=actual_json(fd_result)
        if (fd.get("implementation_check_passed") is not True
                or fd.get("verification_threshold")!=5e-5
                or fd.get("second_order_truncation_contracts") is not True
                or fd.get("actual_current_H_solved_before_this_FD") is not True
                or fd.get("native_anchor_response_sha256")!=P.identity(fd_anchor_response)["sha256"]):
            raise ValueError("Retain the original complete current-H directional FD result")
        for name in ("direct_boundary","separated_boundary"):
            if not isinstance(fd.get(name),dict):
                raise ValueError("The original full FD group is missing")
        anchor,_=actual_json(fd_anchor_response)
        if (anchor.get("identity")!=self.native["actual_owner"]
                or anchor.get("actual_nonlinear_solve") is not True
                or anchor.get("converged") is not True):
            raise ValueError("The FD anchor did not come from the same actual nonlinear owner")
        P.valid_vector(np,anchor["heightJetJacobian"],n*M,"Retain the FD anchor whole endpoint J")
        final,final_receipt=actual_json(final_native_response)
        final_binding=full_final_native(np,final,self.raw_client.config,self.native["actual_owner"])
        # Same original MaterialTrace formula, with the actual augmented
        # endpoint core, and the original constant-mode projection convention.
        current_H=self.original.true_height(self.boundary,arrays["augmented"][-1])
        actual_H=restored_height(np,final,M)
        current_H_word_equal=P.words(current_H)==P.words(actual_H)
        current_H_gap=float(np.max(np.abs(current_H-actual_H),initial=0))
        if current_H_gap>1e-12:
            raise ValueError("The original full-field H binding tolerance fails at this actual endpoint")
        cut_record,cut_receipt=actual_json(physical_cut_audit)
        if not isinstance(cut_record,dict) or not isinstance(raw.get("height_seam"),dict):
            raise ValueError("Retain the original full physical-cut and both mean diagnostics")
        # No new threshold is applied to reported seam errors, mean errors,
        # constant-row drift, target-domain certificates or exact-real gaps.
        out.mkdir(parents=True)
        data_dir=out/"original";data_dir.mkdir()
        members={}
        for key,path in (("fullDN",original_result),("FD",fd_result),
                         ("FD_anchor",fd_anchor_response),("final_native",final_native_response),
                         ("physical_cut_audit",physical_cut_audit)):
            members[key]=copied(path,data_dir/(key+(".json.gz" if Path(path).suffix==".gz" else ".json")),out)
        factory_dir=out/"factory"
        factory_source=Path(self.owner.data["definition_path"]).parents[
            len(Path(self.owner.data["definition_receipt"]["file"]).parts)-1]
        # The factory root is found by its bound relative descriptor; neither
        # a definition alone nor a fabricated factory result is sufficient.
        factory_result_path=factory_source/"result.json"
        if P.identity(factory_result_path)["sha256"]!=self.owner.data["result_receipt"]["sha256"]:
            raise ValueError("The complete original factory result directory was not retained")
        members["factory_result"]=copied(factory_result_path,factory_dir/"result.json",out)
        members["factory_definition"]=copied(self.owner.data["definition_path"],
            factory_dir/self.owner.data["definition_receipt"]["file"],out)
        members["native_configuration"]=copied(self.raw_client.config_path,
            data_dir/"native-configuration.json",out)
        members["native_geometry_result"]=copied(self.geometry_directory/"result.json",
            data_dir/"native-geometry-result.json",out)
        parent_descriptor=None
        if self.parent is not None:
            # The full parent source is provenance only.  Its arrays and old
            # tail are not substituted for any new actual450 acceptance.
            parent_descriptor=dict(manifest=copy.deepcopy(self.parent.receipt),
                original_fullDN=copy.deepcopy(self.parent.manifest["members"]["fullDN"]),
                target_identity_sha256=P.sha(P.canonical(self.parent.target_identity)),
                actual_parent_k=self.parent.k,accepted_parent_was_not_created_by_this_call=True,
                actual_parent_schema=self.parent.manifest["schema"],
                actual_parent_writer_source=copy.deepcopy(self.parent.manifest["writer_source"]),
                actual_parent_resolution=resolution_from_checkpoint(self.parent))
        result=dict(schema=SCHEMA,repository=REPOSITORY,
            run_id=os.environ.get("GITHUB_RUN_ID"),source_commit=os.environ.get("GITHUB_SHA"),
            writer_source=own_identity(),actual_driver_source=self.driver,
            actual_runtime_source_closure=self.source_closure,
            members=members,factory_directory="factory",current_target_identity=target,
            parent_same_scalar_binding=scalar_binding,
            scalar_view="all-ten-fixed-zero-active" if self.flow.k==0 else "seven-shapes-fixed-three-active",
            actual_dimension=self.flow.dimension,actual_physical_dimension=n,
            actual_core_dimension=M,actual_active_parameter_count=self.flow.k,
            actual_fixed_core_targets=self.boundary.K,
            separated_left_rows=self.separated.left_count,separated_right_rows=self.boundary.T,
            M=M,N=self.resolution["field_angular_quadrature"],
            actual_resolution=copy.deepcopy(self.resolution),
            original_resolution_checkpoint_source=dict(file=ORIGINAL_CHECKPOINT_NAME,
                sha256=ORIGINAL_CHECKPOINT_SHA),
            complete_ten_float64le=P.words(expected),
            complete_ten_exact_dyadics=target["complete_ten_exact_dyadics"],
            active_parameter_indices=list(range(self.flow.k)),
            fixed_parameter_indices=list(range(self.flow.k,10)),
            original_acceptance=accepted,complete_arrays=arrays["array_identity"],
            original_constant_core_state_drift=arrays["original_constant_core_state_drift"],
            original_constant_parameter_state_drift=arrays["original_constant_parameter_state_drift"],
            original_unannotated_fixed_modes_metadata=raw.get("fixed_modes"),
            original_core_metadata_fixed_modes_is_not_actual_runtime_K=True,
            original_law=copy.deepcopy(self.original_law),
            exact_profile_specification_sha256=P.sha(P.canonical(specification)),
            original_profile_binding=copy.deepcopy(self.flow.profile.current_C_boundary_binding),
            original_physical_boundary_description=self.boundary.description(),
            original_height_seam=copy.deepcopy(raw["height_seam"]),
            original_native_binding=copy.deepcopy(self.native),
            final_native_binding=final_binding,
            final_native_actual_H_recomputed_by_unchanged_original_trace=True,
            final_native_H_recomputed_words_identical=current_H_word_equal,
            final_native_H_recomputed_max_difference=current_H_gap,
            unchanged_original_closed_loader_H_binding_tolerance=1e-12,
            original_current_H_FD_record=fd_receipt,
            original_physical_cut_audit_record=cut_receipt,
            parent=parent_descriptor,
            finite_fullDN_accepted_by_original_gates=True,
            actual_frozen_M_accepted=self.flow.k==0,
            source_parameter_rows_dropped_relabelled_as_accepted_frozen_M=False,
            original_Z0_and_both_native_mean_jets_retained=True,
            same_accurate_ten_point_as_parent=self.parent is not None,
            same_physical_angle_target_does_not_assert_identical_material_Phi=True,
            all_parent_state_words_are_only_seed_provenance_not_a_final_state_constraint=True,
            no_angular_quadrature_RK_or_mesh_error_bound_inferred=True,
            finite_numeric_shadow_does_not_certify_accurate_target=True,
            exact_joint_C_root_or_infinite_nonlinear_DN_certified=False,
            continuous_target_metric_error_or_C2_seam_certified=False,
            closed_surface_or_embedding_or_reach_or_held_certified=False,
            shared_B_current_C_tail_producer_still_required=True)
        manifest=out/"checkpoint.json";manifest.write_bytes(P.canonical(result))
        return P.identity(manifest,out)


class Checkpoint:
    """Read own actual field evidence without loading or calling a native solver."""
    def __init__(self,directory,manifest_sha256,code_directory=HERE):
        P=load_profile(code_directory)
        self.directory=Path(directory)
        manifest,self.receipt=actual_json(self.directory/"checkpoint.json",manifest_sha256)
        if (manifest.get("schema")!=SCHEMA
                or manifest.get("writer_source",{}).get("sha256")!=own_identity()["sha256"]
                or manifest.get("repository")!=REPOSITORY
                or manifest.get("finite_fullDN_accepted_by_original_gates") is not True):
            raise ValueError("Use the actual independent continuous-ten field checkpoint")
        source_closure(code_directory,{name:row["sha256"]
            for name,row in manifest["actual_runtime_source_closure"].items()})
        factory_directory=P.within(self.directory,manifest["factory_directory"])
        factory_result=P.bound_member(self.directory,manifest["members"]["factory_result"])
        if factory_result.resolve()!=(factory_directory/"result.json").resolve():
            raise ValueError("The actual factory result path is inconsistent")
        self.owner=P.CurrentTenProfile(factory_directory,
            manifest["members"]["factory_result"]["sha256"],code_directory,modes=manifest["M"])
        M=self.owner.M;n=3*M+2;dimension=4*M+2
        k=manifest["actual_active_parameter_count"]
        if type(k) is not int or k!=0:
            raise ValueError("This independent M checkpoint is a complete actual zero-active result only")
        raw=P.member_json(self.directory,manifest["members"]["fullDN"])
        acceptance=original_acceptance(raw)
        p=[struct.unpack("<d",bytes.fromhex(w))[0] for w in manifest["complete_ten_float64le"]]
        p=P.valid_vector(self.owner.np,p,10,"Retain all actual ten words")
        view=self.owner.view(p,"all-ten-frozen" if k==0 else "three-active")
        active=self.owner.np.empty(0) if k==0 else p[:3]
        arrays=complete_arrays(self.owner.np,raw,k,view,active)
        target=P.current_target_identity(self.owner,view,active)
        if (target!=manifest["current_target_identity"]
                or arrays["array_identity"]!=manifest["complete_arrays"]
                or acceptance!=manifest["original_acceptance"]
                or manifest["actual_dimension"]!=dimension+k
                or manifest["actual_physical_dimension"]!=n
                or manifest["actual_core_dimension"]!=M
                or manifest["actual_fixed_core_targets"]!=k
                or manifest["separated_left_rows"]!=n+k
                or manifest["separated_right_rows"]!=M
                or manifest["actual_frozen_M_accepted"]!=(k==0)
                or manifest["source_parameter_rows_dropped_relabelled_as_accepted_frozen_M"] is not False
                or (k==0 and manifest["parent"] is None)):
            raise ValueError("The complete current field layout, source or same-target identity differs")
        scalar_binding=manifest["parent_same_scalar_binding"]
        if (scalar_binding.get("current_field_modes")!=M
                or scalar_binding.get("complete_ten_float64le")!=manifest["complete_ten_float64le"]
                or scalar_binding.get("current_complete_numeric_specification_sha256")!=
                   target["complete_numeric_specification_sha256"]
                or scalar_binding.get("actual_factory_result")!=self.owner.data["result_receipt"]
                or scalar_binding.get("actual_accurate_definition")!=self.owner.data["definition_receipt"]
                or scalar_binding.get("all_other_original_specification_fields_compared_exactly") is not True
                or scalar_binding.get("inherited_state_J_native_or_geometry_acceptance") is not False):
            raise ValueError("The original parent/new-M scalar comparison receipt differs")
        spec=view.export_specification(active)
        common_spec=copy.deepcopy(self.owner.designed.export_specification(p))
        if common_spec.get("field_modes")!=M or common_spec.get("tail_modes")!=M:
            raise ValueError("Current complete numeric scalar dimension differs")
        del common_spec["field_modes"];del common_spec["tail_modes"]
        if P.sha(P.canonical(common_spec))!=scalar_binding["complete_common_specification_without_only_M_fields_sha256"]:
            raise ValueError("The current full scalar specification was not retained")
        if (raw["complete_scalar_profile"]!=spec
                or P.sha(P.canonical(spec))!=manifest["exact_profile_specification_sha256"]):
            raise ValueError("The full ten scalar source was truncated or relabelled")
        for descriptor in manifest["members"].values():
            P.bound_member(self.directory,descriptor)
        fd=P.member_json(self.directory,manifest["members"]["FD"])
        if (fd.get("implementation_check_passed") is not True
                or fd.get("verification_threshold")!=5e-5
                or fd.get("second_order_truncation_contracts") is not True):
            raise ValueError("The original complete actual-H FD input is not passed")
        final=P.member_json(self.directory,manifest["members"]["final_native"])
        cfg=P.member_json(self.directory,manifest["members"]["native_configuration"])
        policy={"max_iterations":32,"line_search_trials":10,"nonlinear_tolerance":2e-9,"sensitivity_eta":0}
        if any(cfg.get(key)!=value for key,value in policy.items()):
            raise ValueError("The original full native policy differs")
        ib=manifest["original_native_binding"]["original_C_input_binding"]
        geometry_report=P.member_json(self.directory,manifest["members"]["native_geometry_result"])
        if (P.original_C_core(ib["original_C_input_binding"])!=P.original_C_core(self.owner.data["complete_C_binding"])
                or geometry_report["actual_original_input_binding"]!=ib
                or geometry_report["geometry"]!=manifest["original_native_binding"]["geometry_descriptor"]
                or cfg["geometry_result_sha256"]!=manifest["members"]["native_geometry_result"]["sha256"]
                or cfg["source_sha256"]!=manifest["original_native_binding"]["source_sha256"]
                or P.rational(ib["original_binary_cut_exact_rational"])!=self.owner.data["cut"]):
            raise ValueError("The complete actual C target/native binding changed")
        resolution=actual_resolution(raw["N"],cfg,
            manifest["original_physical_boundary_description"],
            manifest["original_native_binding"]["actual_owner"],M)
        if (manifest.get("actual_resolution")!=resolution or manifest.get("M")!=M
                or manifest.get("N")!=raw["N"]):
            raise ValueError("Actual field/native/boundary resolution identities disagree")
        native=full_final_native(self.owner.np,final,cfg,
            manifest["original_native_binding"]["actual_owner"])
        if native!=manifest["final_native_binding"]:
            raise ValueError("The whole final endpoint/audit/mean source differs")
        if raw["actual_tail"]["final_response_sha256"]!=manifest["members"]["final_native"]["sha256"]:
            raise ValueError("The original accepted result points to a different final audit")
        self.manifest,self.raw,self.k,self.M=manifest,raw,k,M
        self.profile,self.arrays,self.target_identity=view,arrays,target
        self.native_response,self.native_configuration=final,cfg
        self.resolution=resolution
        self.definition=dict(schema=SCHEMA+"-readback",field_modes=M,
            actual_manifest=self.receipt,actual_original_result=manifest["members"]["fullDN"],
            actual_dimension=dimension+k,actual_frozen_M_accepted=k==0,
            actual_resolution=copy.deepcopy(resolution),
            current_target_identity=target,
            actual_full_native_response_and_complete_endpoint_J_read=True,
            complete_C_geometry_arrays_read_by_this_prefix_reader=False,
            accepted_field_created_by_this_reader=False,
            shared_closed_B_geometry_or_continuous_metric_paid=False)

    def require_frozen_M(self):
        if self.k!=0:
            raise ValueError("A genuine fresh complete frozen-M result is required; dropping active rows is not a solve")
        return self


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory",type=Path,required=True)
    parser.add_argument("--manifest-sha256",required=True)
    parser.add_argument("--code-directory",type=Path,default=HERE)
    parser.add_argument("--require-frozen",action="store_true")
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args(argv);require_actions();load_profile(args.code_directory)
    temp=Path(os.environ["RUNNER_TEMP"]).resolve()
    if args.out.exists() or not args.out.resolve().is_relative_to(temp):
        raise ValueError("Use a fresh owned temporary readout")
    data=Checkpoint(args.directory,args.manifest_sha256,args.code_directory)
    if args.require_frozen:data.require_frozen_M()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_bytes(P.canonical(data.definition))
    print(json.dumps(dict(event="actual-continuous-ten-checkpoint-read",
        output=P.identity(args.out),dimension=4*data.M+2+data.k,
        actual_frozen_M_accepted=data.k==0,continuous_metric_certified=False)),flush=True)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
