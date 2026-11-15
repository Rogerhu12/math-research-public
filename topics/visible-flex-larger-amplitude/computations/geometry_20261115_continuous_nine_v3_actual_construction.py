#!/usr/bin/env python3
"""Request147: actual R300 v3 target construction using R323 finite strict boxes.

All scientific work is public-repository Actions only. This consumes the same
job's full original v3 cut result, keeps all nine literal actual146 parameters,
selects explicit R323 rational widths, and invokes the unmodified v3 factory.
The optional numerical compilation creates no tail J, field or BVP acceptance.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import struct
import sys
import time
import traceback

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="request147-actual-v3-continuous-nine-construction-v1"
REQUEST_SCHEMA="public-continuous-nine-v3-construction-request-v1"
FACTORY_NAME="geometry_20261115_continuous_nine_scalar_factory_v3.py"
FACTORY_SHA="0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e"
NUMERIC_NAME="geometry_20261115_continuous_nine_scalar_numeric_v3.py"
NUMERIC_SHA="7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60"
PROOF_NAME="R323-finite-cut-boxes-and-explicit-uniform-dyadic-windows.md"
PROOF_SHA="3830f0cb1b5ecd4bd4382826068721551140392cb3a29639e2cd9bb308e0922d"
PARAMETERS=["p1","p2","p3","theta1","theta2","theta3","eta1","eta2","eta3"]


def actions_only():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise RuntimeError("Scientific construction is restricted to this public repository Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=True,allow_nan=False)+"\n").encode()


def receipt(path):
    path=Path(path);raw=path.read_bytes()
    return dict(file=path.name,bytes=len(raw),sha256=sha(raw))


def read_bound(path,item):
    path=Path(path);raw=path.read_bytes()
    if len(raw)!=item["bytes"] or sha(raw)!=item["sha256"]:
        raise ValueError("Actual complete input bytes differ: "+path.name)
    decoded=gzip.decompress(raw) if raw.startswith(b"\x1f\x8b") else raw
    return json.loads(decoded),dict(receipt(path),decoded_bytes=len(decoded),
        decoded_sha256=sha(decoded))


def write(path,value):
    raw=canonical(value);Path(path).write_bytes(raw)
    return dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))


def load_source(directory,name,expected,label):
    path=Path(directory)/name;raw=path.read_bytes()
    if sha(raw)!=expected:
        raise ValueError("The actual independent source differs: "+name)
    spec=importlib.util.spec_from_file_location(label,path)
    module=importlib.util.module_from_spec(spec);sys.modules[label]=module
    spec.loader.exec_module(module)
    return module,dict(file=name,bytes=len(raw),sha256=sha(raw))


def strict_dyadic_below(x):
    x=Q(x)
    if x<=0:
        raise ArithmeticError("R323 requires an actually positive finite rational margin")
    exponent=max(1,x.denominator.bit_length()-x.numerator.bit_length()+1)
    value=Q(1,1<<exponent)
    if not 0<value<x:
        raise AssertionError("The explicit R323 integer-bit formula did not retain strictness")
    return value,dict(input=str(x),exponent=exponent,value=str(value),
        strict_lower_than_input=True,no_root_refinement_or_parameter_scan=True)


def select_recipe(factory,kernel,geometry,core_end,cut,cut_boxes,parameters):
    """The exact R323 formulas, with every original construction condition read back."""
    original,jet=factory.core_pieces(kernel,geometry,core_end)
    A,V,BA=jet
    if not (cut>0 and A>cut and abs(V)<1 and cut_boxes["E0"].lo>1):
        raise ArithmeticError("The actual R323 core endpoint/cut/E0 strict premises remain unpaid")
    tree=factory.Tree()
    E0,E1,E2=(tree.leaf(k) for k in ("E0","E1","E2"))
    v=-1/E0.sqrt()
    b=-E1/(2*E0**2)
    q=E2/(2*E0**2*E0.sqrt())-E1**2/(E0**3*E0.sqrt())
    vals=tree.evaluate(cut_boxes,256)
    vb,bb,qb=(vals[item.index] for item in (v,b,q))
    if not -1<vb.lo<=vb.hi<0:
        raise ArithmeticError("The actual finite cut-speed box is not strictly inside (-1,0)")
    margin=min(-vb.hi,1-vb.absolute_upper())
    B,Qmax=bb.absolute_upper(),qb.absolute_upper();T=1+B+Qmax
    gap=A-cut;kappa=Q(1,2)
    xd=min(Q(1),gap/(8*T),cut/(8*T),margin/(8*T))
    d,dr=strict_dyadic_below(xd)
    RB=factory.Box(cut)-vb*d+bb*d*d/2-qb*d*d*d/6
    VB=vb-bb*d+qb*d*d/2
    BB=bb-qb*d
    D=(factory.Box(A)-RB).lo
    A2,F=abs(BA),BB.absolute_upper()
    mA=min(1-abs(V),1-kappa)
    mB=min(1-VB.absolute_upper(),1-kappa)
    if min(D,RB.lo,mA,mB)<=0:
        raise AssertionError("The explicit R323 collar bounds lost a proved strict margin")
    xe=min(Q(1),D/8,A/4,RB.lo/4,mA/(1+A2),mB/(1+F),
        D/(8*(2+A2+F)))
    e,er=strict_dyadic_below(xe)
    # These two operations and the stored difference are the literal original
    # PrefixControls first support convention. This is not CompleteProfile's
    # distinct .15/.70 default support.
    L=float(core_end)
    left=float(.05*L);right=float(.30*L);width=float(right-left)
    l,w=Q.from_float(left),Q.from_float(width)
    if not 0<l<l+w<core_end:
        raise ArithmeticError("The actual original first stored support is not strictly inside the accurate core")
    recipe=dict(schema=factory.RECIPE_SCHEMA,parameter_order=PARAMETERS,
        nine_parameters=list(parameters),collar_mode="cut-cubic-jet-collar",
        root_choice="R286-dovetailed-rational-middle-third",
        core_end=str(core_end),cut_radius=str(cut),kappa=str(kappa),
        collar_width=str(d),first_transition_width=str(e),last_transition_width=str(e),
        first_support=dict(left=str(l),stored_width=str(w)),
        width_selection=dict(proof=PROOF_NAME,sha256=PROOF_SHA,
            algorithm="R323 finite strict boxes, explicit dyadic bit-length formula",
            one_finite_box_is_not_an_arbitrarily_refinable_oracle=True,
            no_original_cut_or_warp_or_root_family_changed=True))
    model=factory.build_expression(kernel,geometry,recipe,cut_boxes,cut)
    values=model["tree"].evaluate(cut_boxes,256)
    conditions=factory.construction_conditions(model,values)
    if not conditions["all_strict_conditions_proved"]:
        raise AssertionError("The exact R323-selected widths did not satisfy the original eleven conditions")
    calibration=dict(schema=SCHEMA+"-finite-width-selection",
        actual_core_endpoint_jet=[str(x) for x in jet],accurate_core_piece_count=len(original),
        actual_cut_boxes={k:v.record() for k,v in cut_boxes.items()},
        actual_v_b_q_boxes={k:v.record() for k,v in zip(("v","b","q"),(vb,bb,qb))},
        gamma=str(gap),cut_speed_margin=str(margin),T=str(T),collar_width_choice=dr,
        actual_RB_VB_BB_boxes={k:v.record() for k,v in zip(("RB","VB","BB"),(RB,VB,BB))},
        D_lower=str(D),mA=str(mA),mB=str(mB),transition_width_choice=er,
        original_first_support_binary64_words={
            "left":struct.pack("<d",left).hex(),"right":struct.pack("<d",right).hex(),
            "stored_width":struct.pack("<d",width).hex()},
        full_original_construction_conditions=conditions,
        literal_all_nine_parameters_preserved=True,
        original_core_full_domain_not_claimed_from_endpoint_only=True,
        given_nine_parameters_not_claimed_automatically_feasible=True,
        accurate_semantic_cut_leaves_not_replaced_by_enclosure_endpoints=True)
    return recipe,calibration


def print_complete_segments(label,value):
    raw=canonical(value);text=raw.decode("ascii");width=20000
    pieces=[text[i:i+width] for i in range(0,len(text),width)]
    identity=dict(label=label,bytes=len(raw),sha256=sha(raw),segments=len(pieces),
        reconstruction="concatenate decoded data strings in exact zero-based order; ASCII UTF8 includes final LF")
    print(json.dumps(dict(event="request147_complete_metadata_group",**identity)),flush=True)
    for i,chunk in enumerate(pieces):
        event=dict(event="request147_complete_metadata_segment",label=label,index=i,
            segments=len(pieces),data=chunk)
        encoded=canonical(event)
        if len(encoded)>89000:
            raise AssertionError("The lossless metadata segment exceeded the declared transport scope")
        print(encoded.decode(),end="",flush=True)
    return identity


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--inputs-directory",type=Path,required=True)
    parser.add_argument("--tail-cover-directory",type=Path,required=True)
    parser.add_argument("--cut-twojet-readout",type=Path,required=True)
    parser.add_argument("--code-directory",type=Path,required=True)
    parser.add_argument("--r300-proof",type=Path,required=True)
    parser.add_argument("--r323-proof",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args(argv);actions_only();started=time.monotonic()
    if args.out.exists():
        raise FileExistsError("Use an independent fresh request147 output directory")
    for item in (args.request,args.inputs_directory,args.tail_cover_directory,args.cut_twojet_readout,
                 args.code_directory,args.r300_proof,args.r323_proof):
        if item.resolve()==args.out.resolve() or item.resolve().is_relative_to(args.out.resolve()):
            raise ValueError("A new owned output cannot own an original input")
    args.out.mkdir(parents=True)
    summary=dict(schema=SCHEMA,repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"],source=receipt(Path(__file__)),
        request=receipt(args.request),phase="bind-inputs",error=None,
        exact_model_definition_created=False,base_domain_complete=False,
        all_nine_requested_domain_complete=False,numerical_profile_compiled=False,
        actual_tail_J_or_native_calls=0,actual_BVP_or_fullDN_success=False,
        actual_accepted_field_created=False,same_field_metric_or_C2_geometry_certificate=False,
        all_raw_outputs_temporary_only=True)
    try:
        request=json.loads(args.request.read_bytes())
        if (request["schema"]!=REQUEST_SCHEMA or request["request_number"]!=147
                or request["repository"]!=REPOSITORY):
            raise ValueError("Use the complete independent request147")
        policy=request["construction"]
        if (policy["sqrt_bits"],policy["domain_max_cells"],policy["domain_max_depth"],
                policy["domain_budget_seconds_per_pass"],policy["field_modes"])!=(256,65536,32,300,112):
            raise ValueError("Explicit construction resources or original field mode scope differ")
        for path,name,expected in ((args.r323_proof,PROOF_NAME,PROOF_SHA),
                (args.r300_proof,policy["R300_proof"]["file"].split("/")[-1],
                 policy["R300_proof"]["sha256"])):
            raw=path.read_bytes()
            if path.name!=name or sha(raw)!=expected:
                raise ValueError("The exact published construction proof differs")
        if request["source_sha256"][Path(__file__).name]!=summary["source"]["sha256"]:
            raise ValueError("The actual construction wrapper source differs")
        factory,factory_source=load_source(args.code_directory,FACTORY_NAME,FACTORY_SHA,"_r147_factory")
        kernel,core_source=factory.load_core_kernel(args.code_directory)
        accepted_item=request["construction_inputs"]["accepted"]
        accepted,accepted_receipt=read_bound(args.inputs_directory/accepted_item["runtime_basename"],accepted_item)
        config_item=request["inputs"]["config"]
        config,config_receipt=read_bound(args.inputs_directory/config_item["runtime_basename"],config_item)
        if accepted.get("success") is not True or accepted.get("M")!=96:
            raise ValueError("The complete original accepted M96 prefix identity differs")
        geometry=accepted["fixed_scalar_profile"]["geometry"]
        core_end=Q.from_float(float(accepted["mesh"][-1]))
        cut=Q.from_float(float(config["rCut"]))
        if config["modes"]!=112 or config["quadrature"]!=2048:
            raise ValueError("The unchanged original T112 configuration differs")
        summary.update(actual_accepted_core_input=accepted_receipt,
            geometry_pointer="/fixed_scalar_profile/geometry",core_end_pointer="/mesh/-1",
            selected_geometry_canonical_sha256=factory.sha(factory.canonical(geometry)),
            actual_original_config=config_receipt,factory_source=factory_source,
            core_kernel_source=core_source,actual_parameter_origin=policy["parameter_origin"])
        parameters=policy["initial_nine_parameters"]
        if len(parameters)!=9 or policy["parameter_order"]!=PARAMETERS:
            raise ValueError("All actual nine original starting parameters must be retained")
        summary["literal_initial_nine_parameters"]=parameters
        summary["phase"]="consume-actual-complete-cut"
        result_path=args.tail_cover_directory/"result.json"
        tail_sha=receipt(result_path)["sha256"]
        cut_sha=receipt(args.cut_twojet_readout)["sha256"]
        boxes,tail_binding=factory.cut_jet_from_actual_cover(args.tail_cover_directory,
            tail_sha,args.code_directory,cut,args.cut_twojet_readout,cut_sha)
        summary["actual_tail_result"]=receipt(result_path)
        summary["actual_cut_twojet_readout"]=receipt(args.cut_twojet_readout)
        if tail_binding["actual_input_binding"]["config"]["sha256"]!=config_item["sha256"]:
            raise ValueError("The current core collar and actual C tail use different original config bytes")
        summary["phase"]="select-explicit-R323-widths"
        recipe,calibration=select_recipe(factory,kernel,geometry,core_end,cut,boxes,parameters)
        recipe["parameter_origin"]=policy["parameter_origin"]
        recipe_path=args.out/"actual-R323-new-continuous-nine-recipe.json"
        recipe_desc=write(recipe_path,recipe)
        calibration_path=args.out/"actual-R323-width-selection.json"
        calibration_desc=write(calibration_path,calibration)
        summary.update(actual_recipe=recipe,actual_recipe_file=recipe_desc,
            actual_width_selection_file=calibration_desc,
            complete_width_selection_log=print_complete_segments("R323-width-selection",calibration))
        summary["phase"]="original-v3-exact-factory-and-two-complete-domain-passes"
        factory_out=args.out/"factory"
        arguments=["--core-file",str(args.inputs_directory/accepted_item["runtime_basename"]),
            "--core-file-sha256",accepted_item["sha256"],
            "--core-geometry-pointer","/fixed_scalar_profile/geometry",
            "--tail-cover-directory",str(args.tail_cover_directory),"--tail-result-sha256",tail_sha,
            "--cut-twojet-readout",str(args.cut_twojet_readout),"--cut-twojet-readout-sha256",cut_sha,
            "--model-recipe",str(recipe_path),"--model-recipe-sha256",recipe_desc["sha256"],
            "--code-directory",str(args.code_directory),"--r300-proof",str(args.r300_proof),
            "--sqrt-bits","256","--max-domain-cells","65536","--max-domain-depth","32",
            "--domain-budget-seconds","300","--out",str(factory_out)]
        code=factory.main(arguments)
        factory_result_path=factory_out/"result.json"
        original=json.loads(factory_result_path.read_bytes())
        summary.update(original_factory_return_code=code,
            original_factory_result_file=receipt(factory_result_path),original_factory_result=original,
            exact_model_definition_created=original["exact_model_definition_created"],
            base_domain_complete=original["nonempty_family_conditions_paid"],
            all_nine_requested_domain_complete=original["full_current_nine_domain_certificate_complete"])
        if original["model_definition"] is not None:
            summary["phase"]="explicit-binary64-search-profile-compilation"
            desc=original["model_definition"]
            definition_path=factory_out/desc["file"]
            numeric,numeric_source=load_source(args.code_directory,NUMERIC_NAME,NUMERIC_SHA,"_r147_numeric")
            profile=numeric.NumericContinuousNineProfile(definition_path,desc["sha256"],
                modes=112,code_directory=args.code_directory)
            spec=profile.export_specification(parameters)
            spec_path=args.out/"numeric-search-profile-specification.json"
            spec_desc=write(spec_path,spec)
            joins=profile.compilation["complete_numerical_piece_join_traces"]
            numerical=dict(actual_source=numeric_source,
                accurate_definition=profile.definition_receipt,complete_numeric_specification=spec_desc,
                numeric_compilation_sha256=profile.compilation_sha256,
                public_material_interval=["0","1"],numeric_physical_length=profile.end,
                complete_piece_count=len(profile.pieces),support_count=len(profile.supports),
                field_modes=profile.M,active_scalar_parameters=profile.parameter_count,
                actual_nine_parameters=spec["nine_parameters"],
                nine_parameter_float64le=spec["nine_parameter_float64le"],
                numerical_cut_leaf_midpoints=profile.compilation["numerical_leaf_midpoints"],
                full_seam_count=len(joins),identical_finite_jet_word_pairs=sum(
                    int(row["numerical_jet_words_identical"]) for row in joins),
                complete_seam_log=print_complete_segments("complete-numerical-piece-joins",joins),
                numerical_midpoints_not_asserted_one_true_tail_root=True,
                accurate_target_length_not_replaced_by_numeric_length=True,
                true_evaluator_error_bound_not_supplied=True,
                tail_J_or_current_C_DN_not_supplied=True,
                numerical_compilation_not_native_or_BVP_acceptance=True)
            summary.update(numerical_profile_compiled=True,numerical_compilation=numerical)
        summary["phase"]="complete-with-original-paid-and-unpaid-scopes"
    except Exception as exc:
        summary["error"]=dict(type=type(exc).__name__,message=str(exc),
            original_traceback=traceback.format_exc())
        summary["incomplete_input_or_construction_not_original_nonlinear_rejection"]=True
    summary["elapsed_seconds"]=time.monotonic()-started
    full_path=args.out/"construction-result.json";desc=write(full_path,summary)
    raw=canonical(dict(summary,actual_construction_result=desc))
    if len(raw)>90000:
        identity=print_complete_segments("complete-construction-summary",json.loads(raw))
        raw=canonical(dict(schema=SCHEMA,run_id=os.environ["GITHUB_RUN_ID"],
            source_commit=os.environ["GITHUB_SHA"],summary_complete=False,
            complete_summary_segment_identity=identity,actual_construction_result=desc,
            exact_model_definition_created=summary["exact_model_definition_created"],
            base_domain_complete=summary["base_domain_complete"],
            all_nine_requested_domain_complete=summary["all_nine_requested_domain_complete"],
            numerical_profile_compiled=summary["numerical_profile_compiled"],
            actual_BVP_or_fullDN_success=False,error=summary["error"]))
    if len(raw)>90000:
        raise RuntimeError("Even the explicit incomplete transport record exceeds 90000 bytes")
    print("BEGIN_REQUEST147_CONTINUOUS_NINE_CONSTRUCTION_SUMMARY",flush=True)
    print(raw.decode(),end="",flush=True)
    print("END_REQUEST147_CONTINUOUS_NINE_CONSTRUCTION_SUMMARY",flush=True)
    print(json.dumps(dict(event="request147_construction_summary_identity",
        bytes=len(raw),sha256=sha(raw),hash_scope="canonical ASCII UTF8 including final LF")),flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            stream.write("construction_summary="+raw.decode().rstrip("\n")+"\n")
            stream.write("construction_summary_bytes="+str(len(raw))+"\n")
            stream.write("construction_summary_sha256="+sha(raw)+"\n")
    return 2 if summary["error"] or summary.get("original_factory_return_code",0)!=0 else 0


if __name__=="__main__":
    raise SystemExit(main())
