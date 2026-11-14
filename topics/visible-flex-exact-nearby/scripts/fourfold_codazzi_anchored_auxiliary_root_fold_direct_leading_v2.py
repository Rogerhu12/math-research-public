#!/usr/bin/env python3
"""Refine only the failed larger auxiliary speed; reuse every accepted old stage."""
from __future__ import annotations
import argparse,copy,gzip,hashlib,importlib.util,json,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint
from flint import arb,acb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
OLD_SOURCE="410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783"
OLD_MANIFEST="1f5de8e5f2a877bad414ec50d50b47ca8ac816a05ef1e90303e3dc79edecbdb9"
OLD_NATIVE="a6f6225cd993718f48b9d35533b81134f966f350b1c9ce704e61e38b34855807"
OLD_PROCESS="69b410c192ed7445c97d13420672844fdf6f73e6548e9febf220645bc13ad04b"
OLD_RUN="43646714623"
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix==".gz" else raw)
def identity(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def save(p,d):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(d,separators=(",",":"),allow_nan=False)+"\n").encode()
    if p.suffix==".gz":raw=gzip.compress(raw,mtime=0)
    q=p.with_name(p.name+".partial");q.write_bytes(raw);q.replace(p)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","out"):p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--resume",type=Path);args=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new mathematics runs only in the actual public Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0"):raise RuntimeError("the pinned runtime changed")
    if args.out.exists():raise FileExistsError("preserve every actual native")
    ctx.prec=320;ctx.cap=4;started=time.monotonic()
    doc=dict(kind="actual_root_anchored_characteristic_refinement_and_preserved_auxiliary_prefix",
        complete=False,proved=False,failure=None,source_sha256=sha(__file__),runtime=runtime,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        original_prefix_run=OLD_RUN,original_prefix_native_sha256=OLD_NATIVE,
        original_prefix_source_sha256=OLD_SOURCE,original_prefix_manifest_sha256=OLD_MANIFEST,
        original_prefix_actual_returncode=1,original_prefix_global_proved_false_retained=True,
        original_targets_primitives_cubics_and_completed_domain_jets_recomputed=0,
        complete_old_smaller_case_recomputed=0,original_complete_coefficient_stages_recomputed=0,
        original_anchor_reused=True,new_coefficient_cases=0,reused_coefficient_cases=2,
        new_characteristic_refinements=0,reused_characteristic_refinements=0,
        new_fold_cases=0,reused_fold_cases=1,new_direct_leading_cases=0,reused_direct_leading_cases=1,
        new_first_forcing_cases=0,reused_first_forcing_cases=1,
        true_root_anchor_and_complete_parameter_mean_retained=True,
        physical_background_outside_original_piece_changed=False,
        original_physical_seam_and_source_equations_retained=True,
        old_circle_I_J_and_independent_mean_source_on_w1_paid=False,
        complete_strong_return_or_cutoff97_inverse_claimed=False,
        original_auxiliary_audit_global_proved_false_retained=True,gates=[],cases=[])
    def checkpoint():
        doc["seconds"]=time.monotonic()-started;save(args.out,doc)
    def input_check(name,truth):
        passed=bool(truth);doc["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("immutable-prefix gate failed: "+name)
    try:
        manifest=read(args.manifest);doc["input_manifest_sha256"]=sha(args.manifest)
        for f in manifest["files"]:
            q=args.repo_root/f["path"]
            if not q.is_file() or sha(q)!=f["sha256"] or q.stat().st_size!=f["bytes"]:
                raise ValueError("a frozen scientific input changed: "+f["path"])
        paths={k:args.repo_root/v for k,v in manifest["input_paths"].items()}
        parent_source=paths["original_scientific_source"]
        input_check("the_unchanged_complete_parent_science_and_its_original_manifest_match",
            sha(parent_source)==OLD_SOURCE and sha(paths["original_manifest"])==OLD_MANIFEST)
        spec=importlib.util.spec_from_file_location("actual_anchored_auxiliary_parent",parent_source)
        b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
        old,proc=read(paths["original_prefix_native"]),read(paths["original_prefix_process"])
        input_check("the_exact_original_failed_global_run_and_all_accepted_prefix_bytes_match",
            sha(paths["original_prefix_native"])==OLD_NATIVE
            and sha(paths["original_prefix_process"])==OLD_PROCESS
            and proc["actual_returncode"]==1 and proc["native_sha256"]==OLD_NATIVE
            and proc["mathematical_source_sha256"]==OLD_SOURCE
            and proc["manifest_sha256"]==OLD_MANIFEST
            and proc["complete"] is False and proc["mathematical_complete"] is True
            and proc["mathematical_proved"] is False and str(proc["run_id"])==OLD_RUN
            and old["source_sha256"]==OLD_SOURCE and old["input_manifest_sha256"]==OLD_MANIFEST
            and old["runtime"]==runtime and old["complete"] is True and old["proved"] is False
            and str(old["run_id"])==OLD_RUN and old["failure"]["type"]=="RuntimeError")
        input_check("the_smaller_case_is_complete_and_the_larger_case_has_only_its_accepted_coefficients",
            len(old["cases"])==2
            and all(old["cases"][0][k] is True for k in ("complete","proved","attempt_complete"))
            and old["cases"][0]["failure"] is None
            and len(old["cases"][0]["gates"])==13 and all(g["passed"] for g in old["cases"][0]["gates"])
            and old["cases"][1]["complete"] is False and old["cases"][1]["proved"] is False
            and old["cases"][1]["attempt_complete"] is True
            and old["cases"][1]["failure"]==dict(type="CaseGateFailure",message="the_true_auxiliary_inverse_is_a_radial_self_map")
            and "coefficient_evidence" in old["cases"][1] and "fold_evidence" not in old["cases"][1]
            and "direct_leading_evidence" not in old["cases"][1]
            and "first_forcing_evidence" not in old["cases"][1]
            and Q(old["cases"][0]["exact_fold_radius"])==Q(3,40000)
            and Q(old["cases"][1]["exact_fold_radius"])==Q(3,8000))
        input_check("the_complete_repaired_family_and_all_original_native_identities_are_unchanged",
            old["root_germ_sha256"]==b.ROOTSHA and old["root_budget_sha256"]==b.BUDGETSHA
            and old["auxiliary_native_sha256"]==b.AUXSHA
            and old["background_definition_sha256"]==b.BASE
            and old["explicit_direction_definition_sha256"]==b.ZDEF
            and old["actual_intrinsic_parameter"]=="eta_0"
            and Q(old["exact_complex_delta_radius"])==b.DELTA
            and old["original_targets_primitives_cubics_and_completed_domain_jets_recomputed"]==0
            and old["original_auxiliary_audit_global_proved_false_retained"] is True)
        for key in ("root_germ_sha256","root_budget_sha256","auxiliary_native_sha256",
            "background_definition_sha256","explicit_direction_definition_sha256",
            "actual_intrinsic_parameter","exact_complex_delta_radius","exact_root_interval",
            "exact_original_piece_interval","exact_original_scalar_germ"):
            doc[key]=copy.deepcopy(old[key])
        doc["complete_original_root_anchor"]=copy.deepcopy(old["complete_original_root_anchor"])
        doc["original_smaller_case_payload_sha256"]=identity(old["cases"][0])
        doc["original_larger_coefficient_payload_sha256"]=identity(old["cases"][1]["coefficient_evidence"])
        doc["original_larger_complex_boxes_payload_sha256"]=identity(old["cases"][1]["complete_coefficient_complex_boxes"])
        doc["original_larger_failed_case_audit"]=copy.deepcopy(old["cases"][1])
        if args.resume:
            previous=read(args.resume)
            input_check("every_new_partial_stage_has_the_same_new_source_manifest_runtime_and_original_prefix",
                previous["source_sha256"]==sha(__file__)
                and previous["input_manifest_sha256"]==sha(args.manifest)
                and previous["runtime"]==runtime
                and previous["original_prefix_native_sha256"]==OLD_NATIVE
                and previous["original_prefix_source_sha256"]==OLD_SOURCE
                and previous["original_prefix_manifest_sha256"]==OLD_MANIFEST)
            doc["cases"]=copy.deepcopy(previous["cases"])
        else:
            case=copy.deepcopy(old["cases"][1])
            case.update(complete=False,proved=False,attempt_complete=False,failure=None,
                original_failed_gate_retained_in_separate_audit=True)
            case["gates"]=copy.deepcopy(old["cases"][1]["gates"][:2])
            doc["cases"]=[copy.deepcopy(old["cases"][0]),case]
        input_check("the_entire_smaller_case_and_both_original_coefficient_payloads_are_reused_exactly",
            len(doc["cases"])==2
            and doc["cases"][0]==old["cases"][0]
            and doc["cases"][1]["coefficient_evidence"]==old["cases"][1]["coefficient_evidence"]
            and doc["cases"][1]["complete_coefficient_complex_boxes"]==old["cases"][1]["complete_coefficient_complex_boxes"])
        doc["complete_smaller_case_payload_unchanged"]=True
        doc["complete_larger_coefficient_payload_unchanged"]=True
        checkpoint()
        anchor={k:b.cb(v) for k,v in doc["complete_original_root_anchor"].items()}
        for k in ("k","gamma"):anchor[k]=anchor[k].real
        case=doc["cases"][1];R=Q(case["exact_fold_radius"])
        roots=list(map(Q,doc["exact_root_interval"]))
        original_cell=list(map(Q,doc["exact_original_piece_interval"]))
        scalar_cell=list(map(Q,doc["exact_original_scalar_germ"]))
        def check(name,truth):
            passed=bool(truth);case["gates"].append(dict(name=name,passed=passed))
            if not passed:raise b.CaseGateFailure(name)
        if case.get("attempt_complete"):
            doc["reused_characteristic_refinements"]=int("characteristic_refinement_evidence" in case)
            for field,counter in (("fold_evidence","reused_fold_cases"),
                ("direct_leading_evidence","reused_direct_leading_cases"),
                ("first_forcing_evidence","reused_first_forcing_cases")):
                doc[counter]+=int(field in case)
        else:
            try:
                if "characteristic_refinement_evidence" in case:
                    re=case["characteristic_refinement_evidence"]
                    c=b.decode(re["complete_refined_coefficient_majorants"])
                    cboxes={k:b.cb(v) for k,v in re["complete_refined_coefficient_complex_boxes"].items()}
                    doc["reused_characteristic_refinements"]+=1
                else:
                    c=b.decode(case["coefficient_evidence"]["complete_coefficient_majorants"])
                    cboxes={k:b.cb(v) for k,v in case["complete_coefficient_complex_boxes"].items()}
                    old_a=cboxes["a"];old_am=c["am"];old_ap=c["ap"]
                    integral_box=anchor["a"]+b.square(b.ex(R)*c["a1"])
                    new_a=b.cintersection(old_a,integral_box)
                    am=new_a.real.lower()
                    ap=min(b.up(new_a),(c["ep"]*c["kp"].sqrt()).upper(),old_ap).upper()
                    check("the_existing_complete_radial_derivative_anchors_the_same_speed_on_the_full_complex_domain",
                        am>0 and ap>0 and am>=old_am and ap<=old_ap)
                    c["am"],c["ap"],cboxes["a"]=am,ap,new_a
                    re=dict(exact_refinement_identity="a(rho)-a_star=rho*integral_0^1 a_rho(t*rho)dt",
                        exact_fold_radius=str(R),complete_old_characteristic_box=b.crecord(old_a),
                        complete_root_integral_box=b.crecord(integral_box),
                        complete_new_characteristic_box=b.crecord(new_a),
                        saved_original_radial_derivative_bound=b.rec(c["a1"]),
                        independent_modulus_bound=b.rec((c["ep"]*c["kp"].sqrt()).upper()),
                        complete_refined_coefficient_majorants=b.encode(c),
                        complete_refined_coefficient_complex_boxes={k:b.crecord(v) for k,v in cboxes.items()},
                        original_complete_coefficient_constructor_called=False)
                    case["characteristic_refinement_evidence"]=re
                    doc["new_characteristic_refinements"]+=1;checkpoint()
                if "fold_evidence" in case:
                    f=b.decode(case["fold_evidence"]["complete_fold_and_leading_bounds"])
                    doc["reused_fold_cases"]+=1
                else:
                    f,fe=b.fold_budget(c,cboxes,anchor,R,check)
                    case["fold_evidence"]=fe;doc["new_fold_cases"]+=1;checkpoint()
                if "direct_leading_evidence" in case:
                    le=case["direct_leading_evidence"]
                    av={tuple(map(int,k.split(","))):b.box(v) for k,v in le["direct_a0_ordinary_derivatives"].items()}
                    bv={tuple(map(int,k.split(","))):b.box(v) for k,v in le["direct_b0_ordinary_derivatives"].items()}
                    chain=b.decode(le["full_direct_fold_chain"]);doc["reused_direct_leading_cases"]+=1
                else:
                    av,bv,chain,le=b.direct_leading(c,f,R,check)
                    case["direct_leading_evidence"]=le;doc["new_direct_leading_cases"]+=1;checkpoint()
                if "first_forcing_evidence" in case:
                    doc["reused_first_forcing_cases"]+=1
                else:
                    case["first_forcing_evidence"]=b.forced_case(av,bv,chain,c,f,R,roots,original_cell,scalar_cell,check)
                    doc["new_first_forcing_cases"]+=1;checkpoint()
                case.update(complete=True,proved=True,attempt_complete=True)
            except b.CaseGateFailure as error:
                case.update(complete=False,proved=False,attempt_complete=True,
                    failure=dict(type=type(error).__name__,message=str(error)))
            checkpoint()
        input_check("the_complete_original_smaller_case_is_still_byte_semantically_unchanged",
            identity(doc["cases"][0])==doc["original_smaller_case_payload_sha256"])
        doc["complete"]=all(x["attempt_complete"] for x in doc["cases"])
        doc["proved"]=doc["complete"] and all(x["proved"] for x in doc["cases"])
        if not doc["proved"]:raise RuntimeError("the new larger characteristic continuation remains unresolved; all exact prefixes are preserved")
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            original_smaller_case_recomputed=0,original_coefficient_stages_recomputed=0,
            native_sha256=sha(args.out),seconds=doc["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()
