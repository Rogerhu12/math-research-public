#!/usr/bin/env python3
"""R400 explicit current-C ten-control profile, frozen views and source binding.

This independently typed source retains the complete R300 accurate expression
DAG and the actual numerical compiler.  Freezing a coefficient vector does not
solve a 450-row problem, repair finite polynomial seam gaps, select one common
C root, or supply a closed surface.  The original full physical RHS and both
physical/material boundary modules are reused without changing their formulas.
No finite-Gauss nine/ten schema, old tail output or old accepted field is relabelled.
Scientific construction and evaluation are public-Actions-only.
"""
from __future__ import annotations
import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path, PurePosixPath
from fractions import Fraction as Q
import re
import struct
import sys

REPOSITORY="Rogerhu12/math-research-public"
HERE=Path(__file__).resolve().parent
SCHEMA="R400-current-continuous-C-ten-complete112-profile-and-freeze-binding-v1"
FACTORY_NAME="geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py"
FACTORY_SHA="72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682"
FACTORY_SCHEMA="R300-continuous-ten-fixed-support1-power4-v3-cut-exact-expression-construction-v1"
DEFINITION_SCHEMA="R300-new-continuous-ten-fixed-support1-power4-target-family-v3-cut-v1"
NUMERIC_NAME="geometry_20261115_continuous_ten_fixed_power_scalar_numeric_v3.py"
NUMERIC_SHA="7dedb7134cd2efc43f136c4a87795f06c6f3824c12a25261b6886c624f6e4ddd"
FLOW_NAME="geometry_20261115_continuous_ten_fixed_power_augmented_v3.py"
FLOW_SHA="a248e9577bf6f522b86c7c9b32d3fd51cc49dc9468760ef1d3e78e33062f9e0f"
AUGMENTED_NAME="geometry_20261114_full_dn_augmented.py"
AUGMENTED_SHA="f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e"
PHYSICAL_NAME="geometry_20261114_r225_free_core_bvp.py"
PHYSICAL_SHA="a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08"
BOUNDARY_NAME="geometry_20261114_physical_test_boundary.py"
BOUNDARY_SHA="3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681"
MATERIAL_BOUNDARY_NAME="geometry_20261114_full_dn_boundary.py"
MATERIAL_BOUNDARY_SHA="4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2"
C_SCHEMA="R286-original-stored-continuous-model-convention-C-v1"
CUT_READER_SHA="1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed"
C_PRODUCER_SHA="f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
PARAMETERS=["p1","p2","p3","theta1","theta2","theta3","eta1","eta2","eta3","xi"]
CONTROL_TERMS=[
    {"parameter_index":0,"support_index":0,"power":0},
    {"parameter_index":1,"support_index":1,"power":0},
    {"parameter_index":2,"support_index":2,"power":0},
    {"parameter_index":3,"support_index":0,"power":1},
    {"parameter_index":4,"support_index":1,"power":1},
    {"parameter_index":5,"support_index":2,"power":1},
    {"parameter_index":6,"support_index":0,"power":2},
    {"parameter_index":7,"support_index":1,"power":2},
    {"parameter_index":8,"support_index":2,"power":2},
    {"parameter_index":9,"support_index":1,"power":4}]
MODES=tuple(range(2,225,2))
SUMMARY_LIMIT=90000
SOURCE_PINS={
    FACTORY_NAME:FACTORY_SHA,NUMERIC_NAME:NUMERIC_SHA,FLOW_NAME:FLOW_SHA,
    AUGMENTED_NAME:AUGMENTED_SHA,PHYSICAL_NAME:PHYSICAL_SHA,
    BOUNDARY_NAME:BOUNDARY_SHA,MATERIAL_BOUNDARY_NAME:MATERIAL_BOUNDARY_SHA,
    "geometry_20261115_continuous_C_full112_binding.py":
        "c0bda3350b30b9659c326112eaf8f411d0bb6f825a7a3f81fcc6c7502ed3f952"}


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise RuntimeError("Execute numerical preparation only in the named public repository Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,ensure_ascii=False,sort_keys=True,
        separators=(",",":"),allow_nan=False)+"\n").encode()


def unique(items):
    value={}
    for key,item in items:
        if key in value:raise ValueError("Duplicate JSON key: "+key)
        value[key]=item
    return value


def decode(raw):
    return json.loads(raw,object_pairs_hook=unique,
        parse_constant=lambda x: (_ for _ in ()).throw(ValueError("Nonfinite JSON token")))


def identity(path,root=None):
    path=Path(path);digest=hashlib.sha256();size=0
    with path.open("rb") as stream:
        for block in iter(lambda:stream.read(1048576),b""):
            digest.update(block);size+=len(block)
    return dict(file=str(path.relative_to(root)) if root else path.name,
        bytes=size,sha256=digest.hexdigest())


def original_json(path,expected):
    path=Path(path);raw=path.read_bytes()
    if sha(raw)!=expected:raise ValueError("Actual original bytes differ: "+str(path))
    decoded=gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw
    return decode(decoded),dict(file=path.name,bytes=len(raw),sha256=expected,
        gzip_original=raw[:2]==b"\x1f\x8b",decoded_bytes=len(decoded),
        decoded_sha256=sha(decoded))


def within(directory,name):
    relative=PurePosixPath(name)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("An original descriptor escaped its directory")
    path=Path(directory)/relative
    if path.is_symlink() or not path.resolve().is_relative_to(Path(directory).resolve()):
        raise ValueError("Keep original descriptors inside the actual directory")
    return path


def bound_member(directory,descriptor):
    path=within(directory,descriptor["file"])
    rec=identity(path,directory)
    if any(rec[k]!=descriptor[k] for k in ("bytes","sha256")):
        raise ValueError("Original member identity differs: "+descriptor["file"])
    return path


def member_json(directory,descriptor):
    raw=bound_member(directory,descriptor).read_bytes()
    return decode(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw)


def json_pointer(value,path):
    if path=="":return value
    if not isinstance(path,str) or not path.startswith("/"):
        raise ValueError("Use an explicit RFC6901 pointer")
    for part in path[1:].split("/"):
        part=part.replace("~1","/").replace("~0","~")
        value=value[int(part)] if isinstance(value,list) else value[part]
    return value


def rational(value):
    if isinstance(value,bool):raise ValueError("Boolean is not an exact coordinate")
    if type(value) is float:
        if not math.isfinite(value):raise ValueError("Nonfinite coordinate")
        return Q.from_float(value)
    if type(value) in (str,int):return Q(value)
    raise ValueError("Use an exact rational string or original finite number")


def pow2(exponent):
    if type(exponent) is not int:raise ValueError("Integral binary exponent required")
    return Q(1<<exponent) if exponent>=0 else Q(1,1<<(-exponent))


def dyadic(value):
    if (not isinstance(value,dict) or set(value)!={"mantissa","binary_exponent"}
            or not isinstance(value["mantissa"],str)
            or re.fullmatch(r"-?(0|[1-9][0-9]*)",value["mantissa"]) is None):
        raise ValueError("Use original dyadic interval words, not display decimals")
    return Q(int(value["mantissa"]))*pow2(value["binary_exponent"])


def bounds(value):
    lower,upper=dyadic(value["lower"]),dyadic(value["upper"])
    if lower>upper:raise ValueError("Reversed original interval")
    return lower,upper


def original_C_core(binding):
    # These are the same work/query exclusions as the frozen R324 binder.
    ignored={"query_input","runtime","work_parameters"}
    return {key:value for key,value in binding.items() if key not in ignored}


def word(value):
    return struct.pack("<d",float(value)).hex()


def words(values):
    return [word(x) for x in values]


def source(directory,name,expected):
    path=Path(directory)/name;rec=identity(path)
    if rec["sha256"]!=expected:raise ValueError("Frozen source differs: "+name)
    return path,rec


def load_source(directory,name,expected,unique_name):
    path,rec=source(directory,name,expected)
    spec=importlib.util.spec_from_file_location(unique_name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    try:spec.loader.exec_module(module)
    except Exception:
        sys.modules.pop(spec.name,None)
        raise
    return module,rec


def valid_vector(np,values,count,label):
    array=np.asarray(values)
    if (array.shape!=(count,) or array.dtype.kind not in "fiu"
            or not np.isrealobj(array) or not np.all(np.isfinite(array))):
        raise ValueError(label)
    return np.array(array,dtype=float,copy=True)


def bind_definition(directory,result_sha,code_directory):
    report,report_rec=original_json(Path(directory)/"result.json",result_sha)
    if (report.get("schema")!=FACTORY_SCHEMA
            or report.get("source_sha256")!=FACTORY_SHA
            or report.get("repository")!=REPOSITORY
            or report.get("exact_model_definition_created") is not True
            or report.get("model_definition") is None):
        raise ValueError("An actual independently produced R300 v3 definition is required")
    source(code_directory,FACTORY_NAME,FACTORY_SHA)
    descriptor=report["model_definition"]
    path=bound_member(directory,descriptor);definition=decode(path.read_bytes())
    if (definition.get("schema")!=DEFINITION_SCHEMA
            or definition.get("source_sha256")!=FACTORY_SHA
            or definition.get("parameter_order")!=PARAMETERS
            or definition.get("control_terms")!=CONTROL_TERMS
            or definition.get("construction_conditions",{}).get("all_strict_conditions_proved") is not True
            or definition.get("polynomial_coefficients_are_expressions_not_cut_interval_midpoints") is not True
            or definition.get("no_early_segment_mask_or_primal_clip") is not True
            or definition.get("true_derivatives_from_the_same_radius_expression") is not True):
        raise ValueError("Retain the actual complete new exact-expression family")
    tail=definition["continuous_tail"]
    if (tail.get("source_sha256")!=C_PRODUCER_SHA
            or tail.get("actual_cut_twojet_readout_source_sha256")!=CUT_READER_SHA
            or tail["actual_input_binding"]["convention"]["schema"]!=C_SCHEMA
            or tail["actual_input_binding"]["convention"]["deep_definition"]!="original-exact-root-family"
            or tail.get("coefficient_midpoints_substituted") is not False
            or tail.get("original_producer_encloses_every_admissible_root_sequence") is not True):
        raise ValueError("The exact new target lost its original C semantic leaves")
    if (report["actual_tail_result_sha256"]!=tail["actual_result"]["sha256"]
            or report["actual_cut_twojet_readout_sha256"]!=tail["actual_complete_cut_twojet_readout"]["sha256"]
            or [rational(x) for x in report["starting_parameters"]]!=
               [rational(x) for x in definition["ten_parameters"]]
            or report["actual_core_input"]!=definition["core_input"]
            or report["actual_model_recipe"]!=definition["model_recipe_input"]):
        raise ValueError("The actual factory result and definition have different producers or inputs")
    cut=rational(definition["cut_radius"])
    if cut!=rational(tail["cut_radius"]) or cut!=rational(tail["original_binary_cut"]["exact_rational"]):
        raise ValueError("Do not renormalise or reinterpret the original binary cut")
    for leaf,key in (("E0","E"),("E1","E_r"),("E2","E_rr")):
        lo,hi=bounds(tail["actual_cut_twojet_enclosures"][key])
        box=definition["actual_enclosure_leaves"][leaf]
        if (lo,hi)!=(Q(box["lower"]),Q(box["upper"])):
            raise ValueError("The numerical compiler's leaves are not the actual common cut hull")
    return dict(report=report,result_receipt=report_rec,definition=definition,
        definition_path=path,definition_receipt=descriptor,
        complete_C_binding=tail["actual_input_binding"],cut=cut,
        semantic_cut_hulls=tail["actual_cut_twojet_enclosures"],
        original_base_domain_paid=report.get("nonempty_family_conditions_paid") is True,
        original_given_parameter_domain_paid=report.get("full_current_ten_domain_certificate_complete") is True,
        factory_interval_domain_is_not_a_new_BVP_gate=True)


class CurrentTenProfile:
    """Own one actual accurate definition and one disclosed numerical compiler."""
    def __init__(self,factory_directory,factory_result_sha,code_directory):
        require_actions()
        self.code_directory=Path(code_directory)
        self.consumed_source_sha256={}
        for name,expected in SOURCE_PINS.items():
            source(self.code_directory,name,expected)
            self.consumed_source_sha256[name]=expected
        self.consumed_source_sha256[Path(__file__).name]=sha(Path(__file__).read_bytes())
        self.data=bind_definition(factory_directory,factory_result_sha,self.code_directory)
        self.numeric,self.numeric_source=load_source(self.code_directory,NUMERIC_NAME,NUMERIC_SHA,
            "_r400_current_C_ten_numeric_binding")
        self.designed=self.numeric.NumericContinuousTenProfile(
            self.data["definition_path"],self.data["definition_receipt"]["sha256"],
            modes=112,code_directory=self.code_directory)
        self.np=self.numeric.np
        self.flow_module,self.flow_source=load_source(self.code_directory,FLOW_NAME,FLOW_SHA,
            "_r400_current_C_ten_physical_flow")
        self.cut=dict(radius=float(self.data["cut"]),
            E=float(self.designed.leaf_values["E0"]),
            Ep=float(self.designed.leaf_values["E1"]),
            Epp=float(self.designed.leaf_values["E2"]))
        if not all(math.isfinite(x) for x in self.cut.values()) or self.cut["E"]<=1:
            raise ArithmeticError("The disclosed finite cut data cannot represent the current scalar domain")
        self.designed.cut=dict(self.cut)
        self.binding=dict(schema=SCHEMA+"-target-binding",
            source_sha256=sha(Path(__file__).read_bytes()),
            consumed_source_sha256=copy.deepcopy(self.consumed_source_sha256),
            factory_result=self.data["result_receipt"],
            accurate_definition=self.data["definition_receipt"],
            numeric_source=self.numeric_source,flow_adapter_source=self.flow_source,
            accurate_target_model_schema=DEFINITION_SCHEMA,continuous_tail_model_schema=C_SCHEMA,
            actual_accurate_cut_hulls=self.data["semantic_cut_hulls"],
            numerical_cut=self.cut,numerical_cut_float64le={k:word(v) for k,v in self.cut.items()},
            original_binary_cut_exact_rational=str(self.data["cut"]),
            numeric_compilation_sha256=self.designed.compilation_sha256,
            actual_source_core=self.data["definition"]["core_input"],
            public_coordinate="u in [0,1]; s_numeric=L_numeric*u and s_true=L_true*u",
            accurate_target_radial_metric="L_true^2 du^2",
            numerical_shadow_radial_metric="L_numeric^2 du^2",
            root_choice=self.data["definition"]["chosen_root_scope"],
            numerical_cut_leaf_midpoints_jointly_realised_by_one_tail_root_not_proved=True,
            finite_compiler_or_old_Gauss_target_relabelled=False,
            continuous_target_evaluator_error_or_final_metric_paid=False,
            complete_base_domain_certificate_from_factory=self.data["original_base_domain_paid"],
            complete_given_parameter_domain_certificate_from_factory=self.data["original_given_parameter_domain_paid"])

    def view(self,parameters,mode):
        require_actions()
        p=valid_vector(self.np,parameters,10,"Retain every actual current ten parameter")
        if mode=="three-active":
            profile=self.designed.frozen_seven_shapes(p[3:])
            profile.initial_parameters=p[:3].copy()
        elif mode=="all-ten-frozen":
            profile=self.designed.frozen_ten(p)
        elif mode=="all-ten-active":
            # A fresh designed instance owns its own initial parameter value.
            profile=self.numeric.NumericContinuousTenProfile(
                self.data["definition_path"],self.data["definition_receipt"]["sha256"],
                modes=112,code_directory=self.code_directory)
            profile.initial_parameters=p.copy()
        else:raise ValueError("Declare three-active, all-ten-frozen, or all-ten-active")
        profile.cut=dict(self.cut)
        profile.current_C_boundary_binding=dict(self.binding,
            view=mode,actual_ten_parameter_float64le=words(p),
            active_parameter_count=profile.parameter_count,
            expected_augmented_dimension=338+112+profile.parameter_count,
            original_453_problem_only_when_three_active=mode=="three-active")
        return profile

    def current_parameters(self,profile,active):
        np=self.np
        active=valid_vector(np,active,profile.parameter_count,"Retain all current active coordinates")
        if profile.parameter_count==10:return active
        if profile.parameter_count==3:return np.r_[active,profile.fixed]
        if profile.parameter_count==0:return profile.fixed.copy()
        raise ValueError("Unknown actual current scalar view")

    def flow(self,actual_augmented_module,actual_probe,profile,workers=1):
        require_actions()
        source(Path(actual_augmented_module.__file__).parent,
            Path(actual_augmented_module.__file__).name,AUGMENTED_SHA)
        if Path(actual_augmented_module.__file__).name!=AUGMENTED_NAME:
            raise ValueError("Use the actual original complete physical AugmentedFlow module")
        actual_physical=Path(actual_augmented_module.base.__file__)
        if (actual_physical.name!=PHYSICAL_NAME
                or identity(actual_physical)["sha256"]!=PHYSICAL_SHA):
            raise ValueError("The actual loaded complete FFT physical RHS source differs")
        if (actual_probe.M!=112 or actual_probe.n!=338
                or actual_probe.N<=448 or actual_probe.N%2
                or not self.np.array_equal(actual_probe.freq,self.np.arange(113)*2)):
            raise ValueError("The supplied original probe must retain every complete112 physical mode")
        if profile.current_C_boundary_binding["factory_result"]!=self.binding["factory_result"]:
            raise ValueError("A different current target owns this profile")
        return self.flow_module.wrap_augmented_flow(actual_augmented_module,
            self.numeric,actual_probe,profile,workers)

    def endpoint_record(self,profile,active):
        require_actions()
        np=self.np
        active=valid_vector(np,active,profile.parameter_count,"Endpoint active coordinates differ")
        actual=np.asarray(profile.raw_jet(profile.end,active),float)
        reference=np.asarray([self.cut["radius"],-1/math.sqrt(self.cut["E"]),
            -self.cut["Ep"]/(2*self.cut["E"]**2)])
        difference=actual-reference
        return dict(actual_ten_parameters=self.current_parameters(profile,active).tolist(),
            actual_complete_numeric_endpoint_jet=actual.tolist(),
            actual_complete_numeric_endpoint_float64le=words(actual),
            boundary_numeric_reference_jet=reference.tolist(),
            boundary_numeric_reference_float64le=words(reference),
            finite_endpoint_difference=difference.tolist(),
            original_boundary_input_tolerance=5e-12,
            original_boundary_input_check_would_pass=bool(
                np.all(np.isfinite(actual)) and np.max(np.abs(difference))<=5e-12),
            finite_comparison_is_not_exact_real_seam_or_C2=True,
            boundary_radial_sign=-1,height_sign_must_be_supplied_by_actual_problem=True,
            no_original_boundary_formula_or_threshold_changed=True)

    def boundary(self,actual_boundary_module,profile,target_core,flow,tail_map,
                 *,height_sign,material_angles,physical_angles):
        require_actions()
        if (Path(actual_boundary_module.__file__).name!=BOUNDARY_NAME
                or identity(actual_boundary_module.__file__)["sha256"]!=BOUNDARY_SHA):
            raise ValueError("Use the unchanged complete physical-angle boundary source")
        source(self.code_directory,MATERIAL_BOUNDARY_NAME,MATERIAL_BOUNDARY_SHA)
        actual_material=Path(sys.modules[actual_boundary_module.FullDNBoundary.__module__].__file__)
        if (actual_material.name!=MATERIAL_BOUNDARY_NAME
                or identity(actual_material)["sha256"]!=MATERIAL_BOUNDARY_SHA):
            raise ValueError("The actually loaded full material trace/boundary module differs")
        if flow.profile is not profile or flow.M!=112 or flow.n!=338:
            raise ValueError("The actual flow, full field and current scalar owner differ")
        expected=profile.parameter_count
        target=valid_vector(self.np,target_core,expected,"Retain every finite fixed low-core target")
        if expected not in (0,3,10):
            raise ValueError("Square T=M requires K=k; never call a 460-row problem 453")
        value=actual_boundary_module.PhysicalTestBoundary(profile,target,
            flow.point_rhs,flow.point_jacobian,tail_map,
            height_sign=height_sign,radial_sign=-1,angular=material_angles,
            physical_angles=physical_angles)
        value.current_C_profile_binding=profile.current_C_boundary_binding
        value.current_C_nonlinear_tail_verified_by_this_binding=False
        return value


def current_target_identity(owner,profile,active):
    """Bind the actual current dyadic point and BOTH precise/finite objects.

    This same-job identity is deliberately stronger than a semantic
    cross-run theorem: it retains the actual factory and compiler receipts.
    No unequal source/evaluator is accepted through a provenance-only flag.
    """
    require_actions()
    p=owner.current_parameters(profile,active)
    exported=owner.designed.export_specification(p)
    return dict(schema=SCHEMA+"-same-point-identity",
        accurate_factory_result=copy.deepcopy(owner.data["result_receipt"]),
        accurate_definition=copy.deepcopy(owner.data["definition_receipt"]),
        accurate_family_base_identity_sha256=exported["accurate_family_base_identity_sha256"],
        accurate_target_model_schema=DEFINITION_SCHEMA,
        continuous_C_model_schema=C_SCHEMA,
        original_complete_C_input_binding=copy.deepcopy(owner.data["complete_C_binding"]),
        original_binary_cut_exact_rational=str(owner.data["cut"]),
        chosen_root_scope=copy.deepcopy(owner.data["definition"]["chosen_root_scope"]),
        parameter_order=list(PARAMETERS),control_terms=copy.deepcopy(CONTROL_TERMS),
        complete_ten_float64le=words(p),
        complete_ten_exact_dyadics=[str(Q.from_float(float(v))) for v in p],
        numerical_compilation_sha256=owner.designed.compilation_sha256,
        numerical_length_float64le=word(owner.designed.end),
        accurate_length_expression_root=owner.data["definition"]["derived_expression_roots"]["total_length"],
        public_material_coordinate="u in [0,1]",
        target_metric_components=["L_true^2","a_true(L_true*u;p)^2"],
        numerical_shadow_components=["L_numeric^2","a_numeric(L_numeric*u;p)^2"],
        complete_numeric_specification_sha256=sha(canonical(exported)),
        numerical_shadow_equals_accurate_target_not_asserted=True,
        global_C_root_selected_or_native_solution_created=False)


def freeze_at_current_state(owner,flow,actual_ten_parameters):
    """A new K=k=0 view of the identical point; it is not an accepted field."""
    require_actions()
    np=owner.np
    p=valid_vector(np,actual_ten_parameters,10,"Freeze every actual ten word")
    if (flow.r300_profile_module is not owner.numeric
            or flow.M!=112 or flow.n!=338
            or flow.profile.current_C_boundary_binding["factory_result"]!=owner.binding["factory_result"]):
        raise ValueError("The current original complete physical flow belongs to another target")
    before=current_target_identity(owner,flow.profile,
        p if flow.k==10 else p[:3] if flow.k==3 else np.empty(0))
    if before["complete_ten_float64le"]!=words(p):
        raise ValueError("A different fixed shape vector cannot be substituted during freezing")
    view=owner.view(p,"all-ten-frozen")
    frozen_flow=owner.flow(flow.r300_original_module,flow.q,view,flow.workers)
    after=current_target_identity(owner,view,np.empty(0))
    if before!=after or (frozen_flow.dimension,frozen_flow.k)!=(450,0):
        raise ValueError("Freezing must retain the entire accurate target and finite evaluator")
    return view,frozen_flow,dict(schema=SCHEMA+"-frozen-problem",
        before_target_identity=before,after_target_identity=after,
        physical_rows=338,core_rows=112,scalar_rows=0,
        fixed_core_targets_after_freezing=0,left_boundary_rows=338,right_boundary_rows=112,
        complete_field_unknowns=450,full_tail_modes=112,
        parent_state_may_only_be_used_as_a_new_initial_guess=True,
        original_current_H_FD_fullDN_and_fresh_final_audit_still_required=True,
        actual_450_accepted=False)


def fresh450_seed(owner,frozen_flow,mesh,complete_parent_states,*,parent_receipt):
    """Keep complete physical/core seed words and recompute all 450 RHS rows.

    This function accepts 453 or 450 only as an input seed.  It never reads a
    parent success flag, writes an accepted checkpoint or drops equations from
    an existing solved problem.  The caller owns original RMS preflight and
    the full separated 338+112 nonlinear boundary problem.
    """
    require_actions()
    np=owner.np
    x=np.asarray(mesh,dtype=float)
    Y=np.asarray(complete_parent_states)
    if (frozen_flow.M,frozen_flow.n,frozen_flow.k,frozen_flow.dimension)!=(112,338,0,450):
        raise ValueError("The complete current zero-active flow is required")
    if (x.ndim!=1 or len(x)<2 or x[0]!=0 or word(x[-1])!=word(frozen_flow.profile.end)
            or np.any(~np.isfinite(x)) or np.any(np.diff(x)<=0)
            or Y.shape not in ((len(x),453),(len(x),450))
            or not np.isrealobj(Y) or np.any(~np.isfinite(Y))):
        raise ValueError("Retain every source mesh node and physical/core seed component")
    if (not isinstance(parent_receipt,dict)
            or type(parent_receipt.get("bytes")) is not int
            or re.fullmatch(r"[0-9a-f]{64}",str(parent_receipt.get("sha256",""))) is None):
        raise ValueError("Bind the actual complete parent bytes before forming the seed")
    retained=np.array(Y[:,:450],dtype=float,copy=True)
    if retained.tobytes(order="C")!=np.asarray(Y[:,:450],dtype=float).tobytes(order="C"):
        raise AssertionError("A complete retained seed word changed")
    rhs=np.asarray(frozen_flow(x,retained.T)).T
    if rhs.shape!=retained.shape:
        raise ValueError("The fresh complete RHS lost a physical/core row")
    return dict(mesh=x.copy(),states=retained,rhs=rhs,
        binding=dict(schema=SCHEMA+"-seed-only",
            actual_parent=copy.deepcopy(parent_receipt),
            complete_original_nodes_retained=True,
            actual_source_dimension=int(Y.shape[1]),new_unknown_dimension=450,
            physical338_and_core112_seed_word_sha256=sha(retained.astype("<f8").tobytes()),
            all_rhs_rows_freshly_evaluated=True,
            fresh_node_nonfinite_indices=np.flatnonzero(~np.all(np.isfinite(rhs),axis=1)).tolist(),
            original_node_mid_RMS_preflight_still_required=True,
            original_K_equals_k_zero_full_boundary_required=True,
            dropped_parameter_seed_rows_are_not_a_new_accepted_solution=True,
            actual_450_accepted=False))


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--factory-directory",type=Path,required=True)
    parser.add_argument("--factory-result-sha256",required=True)
    parser.add_argument("--parameters",type=Path,required=True)
    parser.add_argument("--parameters-sha256",required=True)
    parser.add_argument("--view",choices=("three-active","all-ten-frozen","all-ten-active"),required=True)
    parser.add_argument("--code-directory",type=Path,default=HERE)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args(argv);require_actions()
    root=Path(os.environ["RUNNER_TEMP"]).resolve()
    if args.out.exists() or not args.out.resolve().is_relative_to(root):
        raise ValueError("Use a fresh owned RUNNER_TEMP output")
    parameters,parameter_receipt=original_json(args.parameters,args.parameters_sha256)
    if (parameters.get("schema")!=SCHEMA+"-actual-parameters"
            or parameters.get("parameter_order")!=PARAMETERS):
        raise ValueError("Use an explicit current ten-word parameter record, never a historical default")
    owner=CurrentTenProfile(args.factory_directory,args.factory_result_sha256,args.code_directory)
    p=valid_vector(owner.np,parameters["ten_parameters"],10,"Retain all ten actual parameters")
    if words(p)!=parameters["ten_float64le"]:
        raise ValueError("The exact parameter words differ")
    view=owner.view(p,args.view)
    active=p if view.parameter_count==10 else p[:3] if view.parameter_count==3 else owner.np.empty(0)
    record=dict(schema=SCHEMA,repository=REPOSITORY,
        run_id=os.environ.get("GITHUB_RUN_ID"),source_commit=os.environ.get("GITHUB_SHA"),
        source_sha256=sha(Path(__file__).read_bytes()),actual_parameters=parameter_receipt,
        profile_binding=owner.binding,target_identity=current_target_identity(owner,view,active),
        active_parameter_count=view.parameter_count,expected_dimension=450+view.parameter_count,
        actual_BVP_calls=0,actual_native_calls=0,accepted_parent_consumed=False,
        actual_450_accepted=False,shared_closed_field_created=False,
        relative_metric_or_C2_seams_certified=False)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_bytes(canonical(record))
    print(json.dumps(dict(event="current-C-ten-profile-binding-written",
        output=identity(args.out),actual_accepted_field_created=False)),flush=True)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
