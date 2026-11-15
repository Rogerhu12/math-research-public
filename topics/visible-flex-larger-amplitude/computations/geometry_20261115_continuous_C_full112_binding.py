#!/usr/bin/env python3
"""Bind the new R300 v3 profile to complete physical112 sampling and linear C rows.

This source prepares the actual independent numerical profile and optional
same-C R324 linear data. It supplies neither a nonzero nonlinear tail client
nor an accepted BVP. Original physical338/core112/active3 rows may be used
as an explicitly reparameterised initial guess with a freshly evaluated RHS.
Old finite tail responses, old scalar schemas and old RHS values are not
relabelled. All numerical use is restricted to the named public Actions.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import struct
import sys

REPOSITORY="Rogerhu12/math-research-public"
HERE=Path(__file__).resolve().parent
SCHEMA="R300-new-C-complete112-profile-and-linear-binding-v1"
FACTORY_NAME="geometry_20261115_continuous_nine_scalar_factory_v3.py"
FACTORY_SHA="0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e"
FACTORY_SCHEMA="R300-continuous-nine-scalar-v3-cut-exact-expression-construction-v1"
DEFINITION_SCHEMA="R300-new-continuous-nine-target-family-v3-cut-v1"
NUMERIC_NAME="geometry_20261115_continuous_nine_scalar_numeric_v3.py"
NUMERIC_SHA="7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60"
FLOW_NAME="geometry_20261115_continuous_nine_augmented_v3.py"
FLOW_SHA="d86f6fdf3cf59df3d45c907c655fe54ab830180facd27b7402e649b2e14d151b"
AUGMENTED_NAME="geometry_20261114_full_dn_augmented.py"
AUGMENTED_SHA="f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e"
PHYSICAL_NAME="geometry_20261114_r225_free_core_bvp.py"
PHYSICAL_SHA="a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08"
BOUNDARY_NAME="geometry_20261114_physical_test_boundary.py"
BOUNDARY_SHA="3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681"
MATERIAL_BOUNDARY_NAME="geometry_20261114_full_dn_boundary.py"
MATERIAL_BOUNDARY_SHA="4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2"
LINEAR_NAME="geometry_20261115_stored_C_finite_head_flux.py"
LINEAR_SHA="4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d"
LINEAR_SCHEMA="R324-original-C-complete112-cut-flux-column-enclosure-v1"
C_SCHEMA="R286-original-stored-continuous-model-convention-C-v1"
CUT_READER_SHA="1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed"
C_PRODUCER_SHA="f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
PARAMETERS=["p1","p2","p3","theta1","theta2","theta3","eta1","eta2","eta3"]
MODES=tuple(range(2,225,2))
SUMMARY_LIMIT=90000


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
               [rational(x) for x in definition["nine_parameters"]]
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
        original_given_parameter_domain_paid=report.get("full_current_nine_domain_certificate_complete") is True,
        factory_interval_domain_is_not_a_new_BVP_gate=True)


class CurrentProfile:
    """Own one actual accurate definition and one disclosed numerical compiler."""
    def __init__(self,factory_directory,factory_result_sha,code_directory):
        require_actions()
        self.code_directory=Path(code_directory)
        self.data=bind_definition(factory_directory,factory_result_sha,self.code_directory)
        self.numeric,self.numeric_source=load_source(self.code_directory,NUMERIC_NAME,NUMERIC_SHA,
            "_r300_current_C_numeric_binding")
        self.designed=self.numeric.NumericContinuousNineProfile(
            self.data["definition_path"],self.data["definition_receipt"]["sha256"],
            modes=112,code_directory=self.code_directory)
        self.np=self.numeric.np
        self.flow_module,self.flow_source=load_source(self.code_directory,FLOW_NAME,FLOW_SHA,
            "_r300_current_C_original_physical_flow")
        self.cut=dict(radius=float(self.data["cut"]),
            E=float(self.designed.leaf_values["E0"]),
            Ep=float(self.designed.leaf_values["E1"]),
            Epp=float(self.designed.leaf_values["E2"]))
        if not all(math.isfinite(x) for x in self.cut.values()) or self.cut["E"]<=1:
            raise ArithmeticError("The disclosed finite cut data cannot represent the current scalar domain")
        self.designed.cut=dict(self.cut)
        self.binding=dict(schema=SCHEMA+"-target-binding",
            source_sha256=sha(Path(__file__).read_bytes()),
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
        p=valid_vector(self.np,parameters,9,"Retain every actual current nine parameter")
        if mode=="three-active":
            profile=self.designed.frozen_shapes(p[3:])
            profile.initial_parameters=p[:3].copy()
        elif mode=="all-nine-frozen":
            profile=self.designed.frozen_nine(p)
        elif mode=="all-nine-active":
            # A fresh designed instance owns its own initial parameter value.
            profile=self.numeric.NumericContinuousNineProfile(
                self.data["definition_path"],self.data["definition_receipt"]["sha256"],
                modes=112,code_directory=self.code_directory)
            profile.initial_parameters=p.copy()
        else:raise ValueError("Declare three-active, all-nine-frozen, or all-nine-active")
        profile.cut=dict(self.cut)
        profile.current_C_boundary_binding=dict(self.binding,
            view=mode,actual_nine_parameter_float64le=words(p),
            active_parameter_count=profile.parameter_count,
            expected_augmented_dimension=338+112+profile.parameter_count,
            original_453_problem_only_when_three_active=mode=="three-active")
        return profile

    def current_nine(self,profile,active):
        np=self.np
        active=valid_vector(np,active,profile.parameter_count,"Retain all current active coordinates")
        if profile.parameter_count==9:return active
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
        return dict(actual_nine_parameters=self.current_nine(profile,active).tolist(),
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
        if expected not in (0,3,9):
            raise ValueError("Square T=M requires K=k; never call a 459-row problem 453")
        value=actual_boundary_module.PhysicalTestBoundary(profile,target,
            flow.point_rhs,flow.point_jacobian,tail_map,
            height_sign=height_sign,radial_sign=-1,angular=material_angles,
            physical_angles=physical_angles)
        value.current_C_profile_binding=profile.current_C_boundary_binding
        value.current_C_nonlinear_tail_verified_by_this_binding=False
        return value


class CurrentLinearRows:
    """Read every actual R324 mode; never invent a missing or resonant graph."""
    def __init__(self,directory,result_sha,profile):
        require_actions()
        directory=Path(directory)
        source(profile.code_directory,LINEAR_NAME,LINEAR_SHA)
        report,receipt=original_json(directory/"result.json",result_sha)
        if (report.get("schema")!=LINEAR_SCHEMA or report.get("source_sha256")!=LINEAR_SHA
                or report.get("repository")!=REPOSITORY or report.get("target_model_schema")!=C_SCHEMA
                or report.get("complete_requested_modes")!=list(MODES)):
            raise ValueError("Use the actual complete-scope R324 linear producer")
        binding=member_json(directory,report["input_binding"])
        if (binding.get("schema")!=LINEAR_SCHEMA+"-input-binding"
                or binding.get("source_sha256")!=LINEAR_SHA
                or original_C_core(binding["original_C_input_binding"])!=
                   original_C_core(profile.data["complete_C_binding"])
                or rational(report["original_binary_cut_exact_rational"])!=profile.data["cut"]):
            raise ValueError("The R324 operator belongs to a different continuous C or cut")
        descriptor=report["complete_original_mode_scope"]
        if descriptor!=report["detailed_ledgers"]["complete112_mode_status_and_columns"]:
            raise ValueError("The complete original mode-stream alias differs")
        path=bound_member(directory,descriptor)
        rows=[]
        with path.open("rb") as stream:
            for line in stream:
                item=decode(line);index=len(rows)
                if index>=112 or item["mode_index"]!=index or item["physical_frequency"]!=MODES[index]:
                    raise ValueError("A complete mode or row order was lost")
                if item["complete_required_cut_propagation"]:
                    if (item["original_Q_F_one_column_normalization_restored"] is not True
                            or item["family_uniform_over_every_fixed_original_root_sequence"] is not True):
                        raise ValueError("The same normalized family column was not retained")
                    ulo,uhi=bounds(item["physical_cut_column"]["u"])
                    klo,khi=bounds(item["physical_cut_column"]["k"])
                    row=item["original_Robin_row"]
                    if (row["order"]!=["u","k"] or bounds(row["coefficient_u"])!=(-khi,-klo)
                            or bounds(row["coefficient_k"])!=(ulo,uhi)):
                        raise ValueError("The original non-divided Robin row changed")
                    nonzero=ulo>0 or uhi<0
                    if item["actual_cut_height_interval_excludes_zero"] is not nonzero:
                        raise ValueError("The actual height interval flag differs from its words")
                    if item["actual_cut_slope_enclosure_computed"]:
                        if not nonzero:raise ValueError("No graph may divide an interval containing zero")
                        bounds(item["cut_slope_per_unit_physical_height"])
                rows.append(item)
        if len(rows)!=112 or len(rows)!=descriptor["rows"]:
            raise ValueError("Keep every complete or unpaid requested mode")
        paid=[r["physical_frequency"] for r in rows if r["complete_required_cut_propagation"]]
        nonzero=[r["physical_frequency"] for r in rows if r["actual_cut_height_interval_excludes_zero"]]
        graph=[r["physical_frequency"] for r in rows if r.get("actual_cut_slope_enclosure_computed") is True]
        if paid!=report["completed_cut_column_modes"] or nonzero!=report["actual_nonzero_height_modes"]:
            raise ValueError("The report and all actual row scopes disagree")
        if (report["all_complete112_physical_cut_columns_enclosed"]!=(len(paid)==112)
                or report["all_complete112_height_denominators_verified"]!=(len(nonzero)==112)
                or report["all_complete112_cut_slope_enclosures_computed"]!=(len(graph)==112)):
            raise ValueError("Do not promote a partial or height-unpaid result to a full graph")
        if report["complete112_cut_DN_diagonal"] is not None:
            diagonal=member_json(directory,report["complete112_cut_DN_diagonal"])
            if (len(graph)!=112 or diagonal["physical_frequencies"]!=list(MODES)
                    or diagonal["diagonal_enclosures"]!=[r["cut_slope_per_unit_physical_height"] for r in rows]):
                raise ValueError("The graph file does not preserve every original bound")
        elif len(graph)==112:
            raise ValueError("The declared complete graph payload is absent")
        self.directory,self.report,self.receipt=directory,report,receipt
        self.rows,self.graph_modes=rows,graph
        self.binding=dict(schema=SCHEMA+"-same-C-linear-rows",
            actual_linear_result=receipt,actual_linear_input_binding=report["input_binding"],
            complete_mode_stream=descriptor,complete_requested_modes=list(MODES),
            completed_cut_columns=paid,verified_nonzero_heights=nonzero,
            computed_graph_modes=graph,
            same_C_common_root_family_and_binary_cut_proved_by_complete_binding=True,
            producer_run_id=report["run_id"],producer_source_commit=report["source_commit"],
            profile_factory_result=profile.data["result_receipt"],
            different_runs_allowed_only_with_identical_frozen_C_core=True,
            complete_Robin_rows_do_not_require_dividing_by_height=True,
            numerical_midpoints_need_not_be_jointly_realised_by_one_root_sequence=True,
            actual_nonlinear_DN_or_J_proved=False,
            original_pending_scope=report["complete_unstarted_mode_suffix"],
            original_error=report["error"])

    def numerical_linear_model(self,profile):
        require_actions()
        if self.graph_modes!=list(MODES):
            raise ArithmeticError("Complete current graph sampling remains unpaid; retain the original Robin rows")
        np=profile.np
        selected=[];rounding=[]
        for row in self.rows:
            lo,hi=bounds(row["cut_slope_per_unit_physical_height"])
            midpoint=(lo+hi)/2
            value=float(midpoint)
            if not math.isfinite(value):raise ArithmeticError("A graph midpoint is not representable")
            actual=Q.from_float(value)
            selected.append(value)
            rounding.append(dict(physical_frequency=row["physical_frequency"],
                full_original_interval=row["cut_slope_per_unit_physical_height"],
                original_exact_rational_midpoint=str(midpoint),
                numerical_float64le=word(value),
                numerical_value_inside_original_interval=lo<=actual<=hi,
                exact_numeric_minus_original_interval=[str(actual-hi),str(actual-lo)],
                simultaneous_realisation_by_one_original_root_not_proved=True))
        return NumericalLinearTail(np,np.asarray(selected),self.binding,rounding)


class NumericalLinearTail:
    """A declared finite linear model, deliberately not a true TailClient."""
    def __init__(self,np,diagonal,binding,rounding):
        self.np=np;self.diagonal=diagonal.copy();self.J=np.diag(diagonal)
        self.binding=binding;self.rounding=rounding
        self.actual_nonlinear_solve=False

    def __call__(self,height):
        require_actions()
        H=valid_vector(self.np,height,112,"The linear model retains every current height mode")
        return dict(slope=self.J@H,jacobian=self.J.copy(),actual_nonlinear_solve=False,
            current_C_linear_model_only=True,linear_source_binding=self.binding,
            numerical_midpoints_are_explicit_approximation=True,
            actual_nonlinear_tail_or_final_audit_supplied=False)

    def solve(self,*args,**kwargs):
        raise RuntimeError("A linear C interval model is not a nonzero native TailClient or final audit")


def _reparameterize_complete453_guess(profile_owner,profile,flow,old_mesh,old_states,
                                   actual_active_parameters,source_identity):
    """Keep all physical/core seed rows; replace only explicitly new controls.

    The source is only an initial guess. Map its entire old physical interval
    to the same public u, then to the actual new finite length, and recompute
    every RHS row. No old RHS, metric acceptance or physical-s identity is used.
    """
    require_actions();np=profile_owner.np
    mesh=np.asarray(old_mesh,float);states=np.asarray(old_states)
    p=valid_vector(np,actual_active_parameters,3,"The new 453 seed has three explicit active values")
    if (profile.parameter_count!=3 or flow.profile is not profile
            or (flow.M,flow.n,flow.k,flow.dimension)!=(112,338,3,453)
            or mesh.ndim!=1 or len(mesh)<2 or states.shape!=(len(mesh),453)
            or not np.isrealobj(states) or not np.all(np.isfinite(states))
            or not np.all(np.isfinite(mesh)) or mesh[0]!=0 or mesh[-1]<=0
            or np.any(np.diff(mesh)<=0)):
        raise ValueError("Supply the complete source mesh and every original 453 seed component")
    if (not isinstance(source_identity,dict)
            or source_identity.get("complete_original_JSON_bytes_read") is not True):
        raise ValueError("Use read_complete453_guess to bind the complete original source bytes")
    public_u=mesh/mesh[-1]
    public_u[0],public_u[-1]=0.,1.
    current_mesh=profile.mesh_from_public_u(public_u)
    current=np.array(states,dtype=float,copy=True)
    old_parameters=np.array(current[:,flow.parameter_slice],copy=True)
    current[:,flow.parameter_slice]=p
    derivative=flow(current_mesh,current.T).T
    if derivative.shape!=current.shape:
        raise ValueError("The fresh current RHS lost physical/core/scalar rows")
    bad=np.flatnonzero(~np.all(np.isfinite(derivative),axis=1))
    return dict(schema=SCHEMA+"-complete453-initial-guess",
        mesh=current_mesh,states=current,rhs=derivative,public_u=public_u,
        source_identity=source_identity,original_node_count=len(mesh),
        original_mesh_float64le=words(mesh),public_u_float64le=words(public_u),
        actual_new_mesh_float64le=words(current_mesh),
        original_active_parameter_float64le=[words(row) for row in old_parameters],
        current_active_parameter_float64le=words(p),
        source_decoded_physical338_and_core112_rows_copied_without_projection=True,
        raw_words_not_exported_by_original_JSON_not_claimed_restored=True,
        source_old_parameter_rows_not_relabelled=True,
        original_RHS_discarded_and_all_current_rows_recomputed=True,
        actual_fresh_node_domain_failure_indices=bad.tolist(),
        original_node_mid_RMS_preflight_still_required=True,
        current_C_profile=profile.export_specification(p),
        original_seed_acceptance_or_g_not_inherited=True,
        actual_current_BVP_or_native_accepted=False)


def read_complete453_guess(profile_owner,profile,flow,*,source_file,source_sha256,
                           mesh_pointer,states_pointer,actual_active_parameters):
    """Read the actual whole original JSON source before forming a new guess."""
    require_actions()
    document,receipt=original_json(source_file,source_sha256)
    source_identity=dict(original_complete_file=receipt,
        mesh_pointer=mesh_pointer,states_pointer=states_pointer,
        complete_original_JSON_bytes_read=True,
        original_document_schema=document.get("schema") if isinstance(document,dict) else None,
        original_acceptance_and_target_not_inherited=True)
    return _reparameterize_complete453_guess(profile_owner,profile,flow,
        json_pointer(document,mesh_pointer),json_pointer(document,states_pointer),
        actual_active_parameters,source_identity)


class Journal:
    def __init__(self,path,root):
        self.path,self.root=Path(path),Path(root)
        self.stream=self.path.open("xb");self.count=0;self.size=0;self.digest=hashlib.sha256()
    def add(self,value):
        raw=canonical(value);self.stream.write(raw);self.digest.update(raw)
        self.size+=len(raw);self.count+=1
    def finish(self):
        self.stream.flush();os.fsync(self.stream.fileno());self.stream.close()
        return dict(file=str(self.path.relative_to(self.root)),bytes=self.size,
            sha256=self.digest.hexdigest(),rows=self.count)


def finite_array_values(np,array):
    """Preserve nonfinite words separately without emitting invalid JSON."""
    value=np.asarray(array)
    if value.ndim==0:
        scalar=float(value)
        return scalar if math.isfinite(scalar) else None
    return [finite_array_values(np,row) for row in value]


def sample_plan(owner,profile,active,plan,out):
    require_actions()
    np=owner.np
    if (plan.get("schema")!="R300-complete-public-u-profile-sampling-plan-v1"
            or plan.get("coordinates")!="public-u"
            or not isinstance(plan.get("queries"),list)):
        raise ValueError("Use an explicit public-u sample plan; no whole-domain certificate is inferred")
    journal=Journal(out/"large-arrays"/"complete-requested-numeric-profile-samples.jsonl",out)
    bad=[];point_batch_differences=[];failed=[];rows=0
    try:
        for index,item in enumerate(plan["queries"]):
            record=dict(query_index=index,original_query=item,
                original_scalar_domain_at_this_point=None,
                original_evaluation_returned=False,error=None,
                sample_not_continuous_domain_or_evaluator_error_certificate=True)
            try:
                u=rational(item["u"])
                if not 0<=u<=1:raise ValueError("The public material query leaves [0,1]")
                uf=float(u);s=uf*profile.end
                if u==0:s=0.
                if u==1:s=profile.end
                raw=np.asarray(profile.raw_jet(s,active),float)
                valid=bool(np.all(np.isfinite(raw)) and raw[0]>0 and abs(raw[1])<1)
                if not valid:bad.append(index)
                batch=None;consistent=None
                if valid:
                    batch=np.asarray(profile.scalar_jets(np.asarray([s]),active)[0],float)
                    consistent=words(raw)==words(batch)
                    if not consistent:point_batch_differences.append(index)
                controls=np.asarray(profile.control_jets(s))
                public=np.asarray([raw[0],profile.end*raw[1],profile.end**2*raw[2]])
                record.update(requested_public_u_exact_rational=str(u),
                    evaluated_public_u_float64le=word(uf),actual_numeric_s_float64le=word(s),
                    numerical_s_jet=finite_array_values(np,raw),
                    numerical_s_jet_float64le=words(raw),
                    numerical_public_u_jet=finite_array_values(np,public),
                    numerical_public_u_jet_float64le=words(public),
                    actual_control_jets=finite_array_values(np,controls),
                    actual_control_jets_float64le=[words(row) for row in controls],
                    complete_active_parameter_float64le=words(active),
                    original_scalar_domain_at_this_point=valid,
                    original_evaluation_returned=True,
                    actual_point_batch_words_equal=consistent,
                    complete_batch_jet_float64le=None if batch is None else words(batch),
                    fixed_public_u_true_target_uses_different_L_true=True,
                    JSON_null_for_nonfinite_scalar_retains_complete_original_float64_word=True)
            except Exception as failure:
                failed.append(index)
                record["error"]=dict(type=type(failure).__name__,message=str(failure))
            journal.add(record);rows+=1
    finally:descriptor=journal.finish()
    return dict(complete_requested_sample_count=rows,
        expected_requested_sample_count=len(plan["queries"]),
        complete_declared_sample_outcomes_recorded=rows==len(plan["queries"]),
        complete_requested_numeric_evaluations_returned=not failed,
        numeric_evaluation_exception_indices=failed,
        scalar_domain_failure_indices=bad,point_batch_difference_indices=point_batch_differences,
        sample_stream=descriptor,original_all_domain_conditions_not_certified_by_samples=True)


def arguments():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--factory-directory",type=Path,required=True)
    parser.add_argument("--factory-result-sha256",required=True)
    parser.add_argument("--parameter-recipe",type=Path,required=True)
    parser.add_argument("--parameter-recipe-sha256",required=True)
    parser.add_argument("--sample-plan",type=Path,required=True)
    parser.add_argument("--sample-plan-sha256",required=True)
    parser.add_argument("--finite-head-directory",type=Path)
    parser.add_argument("--finite-head-result-sha256")
    parser.add_argument("--code-directory",type=Path,default=HERE)
    parser.add_argument("--out",type=Path,required=True)
    return parser


def main(argv=None):
    args=arguments().parse_args(argv);require_actions()
    if bool(args.finite_head_directory)!=bool(args.finite_head_result_sha256):
        raise ValueError("Bind both actual optional R324 directory and actual result SHA")
    recipe,recipe_identity=original_json(args.parameter_recipe,args.parameter_recipe_sha256)
    if (recipe.get("schema")!="R300-new-C-complete112-profile-view-recipe-v1"
            or recipe.get("parameter_order")!=PARAMETERS
            or recipe.get("field_modes")!=112):
        raise ValueError("Use the complete independent current nine-parameter view recipe")
    plan,plan_identity=original_json(args.sample_plan,args.sample_plan_sha256)
    out=args.out.resolve();root=Path(os.environ["RUNNER_TEMP"]).resolve()
    if root not in out.parents or out.exists():
        raise ValueError("Use a fresh owned temporary output under actual RUNNER_TEMP")
    for path in (args.factory_directory,args.parameter_recipe,args.sample_plan,args.code_directory,
                 *([args.finite_head_directory] if args.finite_head_directory else [])):
        if Path(path).resolve().is_relative_to(out):
            raise ValueError("Owned output cannot contain an original input or source")
    owner=CurrentProfile(args.factory_directory,args.factory_result_sha256,args.code_directory)
    p=valid_vector(owner.np,recipe["nine_parameters"],9,"Supply all nine actual current values")
    profile=owner.view(p,recipe["view"])
    active=(p if profile.parameter_count==9 else p[:3] if profile.parameter_count==3 else owner.np.empty(0))
    out.mkdir();(out/"large-arrays").mkdir()
    error=None;samples=None;linear=None;numeric_linear=None
    try:
        samples=sample_plan(owner,profile,active,plan,out)
        if samples["numeric_evaluation_exception_indices"]:
            error=dict(type="NumericSampleEvaluationIncomplete",
                message="Every requested outcome is recorded; one or more evaluations raised")
        if args.finite_head_directory:
            actual=CurrentLinearRows(args.finite_head_directory,args.finite_head_result_sha256,owner)
            linear=actual.binding
            # A partial or non-divisible actual row stream remains a usable
            # diagnostic; profile sampling does not add a nonresonance gate.
            if actual.graph_modes==list(MODES):
                model=actual.numerical_linear_model(owner)
                raw=canonical(dict(schema=SCHEMA+"-disclosed-linear-model",
                    binding=model.binding,complete_diagonal_float64le=words(model.diagonal),
                    complete_original_intervals_and_rounding=model.rounding,
                    no_nonlinear_tail_response_fabricated=True))
                path=out/"large-arrays"/"complete112-disclosed-linear-model.json"
                path.write_bytes(raw);numeric_linear=identity(path,out)
    except Exception as failure:
        error=dict(type=type(failure).__name__,message=str(failure))
    spec=profile.export_specification(active)
    raw=canonical(spec);path=out/"large-arrays"/"current-complete-profile-specification.json";path.write_bytes(raw)
    specification=identity(path,out)
    report=dict(schema=SCHEMA,source_sha256=sha(Path(__file__).read_bytes()),
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        runtime=dict(python=sys.version,numpy=owner.np.__version__,platform=sys.platform),
        actual_target_binding=owner.binding,actual_recipe=recipe_identity,actual_plan=plan_identity,
        actual_profile_view=recipe["view"],active_parameter_count=profile.parameter_count,
        physical_rows=338,constant_core_rows=112,augmented_rows=450+profile.parameter_count,
        actual_complete_nine_parameters=p.tolist(),actual_complete_nine_float64le=words(p),
        full_profile_specification=specification,
        actual_numeric_cut_endpoint=owner.endpoint_record(profile,active),
        original_requested_sampling=samples,actual_same_C_linear_rows=linear,
        optional_disclosed_linear_model=numeric_linear,
        all_original_physical_equations_available_via_pinned_flow_adapter=True,
        original_boundary_cut_input_tolerance_unchanged=True,
        nondivided_Robin_rows_not_relabeled_as_a_full_DN_map=True,
        native_tail_provider_implemented=False,actual_nonlinear_tail_calls=0,
        original_full453_Newton_or_FD_or_final_audit_executed=False,
        old_full699_or_453_success_reused=False,
        actual_BVP_or_closed_field_or_same_g_success=False,
        complete_target_interval_metric_consumer_remains_separate=True,
        raw_outputs_owned_temporary_and_recomputable=True,error=error)
    raw=canonical(report);(out/"result.json").write_bytes(raw)
    if len(raw)>SUMMARY_LIMIT:
        print(json.dumps(dict(event="current-C-binding-summary-over-budget",
            bytes=len(raw),sha256=sha(raw),no_scientific_success_or_truncation=True)),flush=True)
        return 70
    print("BEGIN_CURRENT_C_COMPLETE112_PROFILE_BINDING_SUMMARY",flush=True)
    print(raw.decode(),end="",flush=True)
    print("END_CURRENT_C_COMPLETE112_PROFILE_BINDING_SUMMARY",flush=True)
    print(json.dumps(dict(event="current-C-binding-summary-identity",
        bytes=len(raw),sha256=sha(raw),hash_scope="canonical UTF8 including final LF")),flush=True)
    return 2 if error else 0


if __name__=="__main__":
    raise SystemExit(main())
