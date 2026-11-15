#!/usr/bin/env python3
"""One inherited finite system, one R166 static cut, and all R168 quadratic parities.

No old RREF, original coefficient, path integral or normal form is recomputed.
Each wrong-parity stored Q2 coefficient is added as two necessary halfspaces
in the unchanged inherited free coordinates.  Published R168 is the theorem
prerequisite; this module does not infer parity from the previous candidate.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction as F
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import time

import literature_character_minus2_static_cut as cut

base = cut.base
SCHEMA = "visible-flex-character-minus2-static-and-quadratic-parity-cuts-v1"
REPOSITORY = cut.REPOSITORY
STATIC_HELPER = {"filename": "literature_character_minus2_static_cut.py", "bytes": 26313,
    "sha256": "d5a65482df040627b1a9a13fb8fce3e813f90e8ec196714cb9cf1bd78e97da5d"}
PARITY = (("Q2_0", 0), ("Q2_1", 1), ("Q2_2", 0))


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(path):
    path=Path(path);raw=path.read_bytes()
    return {"filename":path.name,"bytes":len(raw),"sha256":sha(raw)}


def source_identity():
    if identity(cut.__file__) != STATIC_HELPER:
        raise ValueError("frozen one-static-cut source changed")
    return {"driver":identity(__file__),"frozen_single_static_cut_helper":STATIC_HELPER,
        "inherited_exact_finite_system_engine":cut.source_identity()["archived_exact_finite_system_engine"],
        "head_or_profile_helpers_imported":False}


def append_without_mutating_old_records(table,row,reason):
    """Deduplicate new halfspaces without incrementing any old reason counter."""
    normalized=base.primitive(row,equality=False)
    if not normalized:
        return None,"zero_after_inherited_equalities"
    key=tuple(sorted(normalized.items()))
    if key in table.keys:
        return table.keys[key],"already_present"
    return table.add(normalized,reason),"new"


def append_complete_quadratic_parities(data,system,budget):
    n=data["normal_coordinate_count"];free=list(system["free"]);d=len(free)
    if free!=data["free_normal_coordinates"]:
        raise ValueError("quadratic parity must use the unchanged inherited free coordinates")
    raw_transform=data["normal_coordinates_as_free_linear_forms"]
    if len(raw_transform)!=n:
        raise ValueError("inherited normal-to-free transform has wrong length")
    transform=[base.read_row(row,d) for row in raw_transform]
    for j,index in enumerate(free):
        if transform[index]!=base.unit(j):
            raise ValueError("inherited free coordinate meanings changed")
    table=system["reduced"];old_count=len(table.records)
    old_prefix=deepcopy(table.records);old_prefix_sha=sha(canonical(old_prefix))
    fields=data["corrected_scalar_k_polynomials"]
    scan=[];relations=[]
    for family,required in PARITY:
        terms=fields[family]
        degrees=[term[0] for term in terms]
        if (any(not isinstance(power,int) or power<0 for power in degrees)
            or len(set(degrees))!=len(degrees)):
            raise ValueError("invalid stored Q2 polynomial degree list")
        scan.append({"family":family,"required_degree_mod_two":required,
                     "all_stored_degrees":list(degrees),"stored_family_forms_sha256":sha(canonical(terms))})
        for power,raw in terms:
            normal_row=base.read_row(raw,n)
            if power%2==required:
                continue
            reduced=base.substitute(normal_row,transform)
            budget.check(reduced)
            signs=[]
            for sign in (1,-1):
                signed=base.row_add((reduced,sign))
                reason={"kind":"R168_complete_corrected_quadratic_reflection_parity",
                        "family":family,"degree":power,"required_parity":required,
                        "equality_as_halfspace_sign":sign}
                index,status=append_without_mutating_old_records(table,signed,reason)
                signs.append({"sign":sign,"reduced_row_index":index,"status":status,
                              "signed_free_linear_form":base.serial_row(signed)})
            relations.append({"family":family,"degree":power,"required_degree_mod_two":required,
                "normal_coordinate_linear_form":deepcopy(raw),
                "free_coordinate_equality":base.serial_row(reduced),"two_halfspaces":signs})
    if table.records[:old_count]!=old_prefix:
        raise AssertionError("adding parity mutated inherited/static-cut row metadata")
    return {"theorem":"R168","scanned_families":scan,"wrong_parity_coefficient_rows":relations,
        "all_stored_degrees_of_all_three_Q2_families_scanned":True,
        "not_only_the_previous_candidate_nonzero_entries":True,
        "old_RREF_not_recomputed":True,"equality_representation":"two_opposite_necessary_halfspaces",
        "row_count_before_parity":old_count,"row_count_after_parity":len(table.records),
        "new_distinct_halfspaces":len(table.records)-old_count,
        "unchanged_prefix_rows_sha256":old_prefix_sha}


def actual(args,report,ctx,budget):
    report["phase"]="consume_complete_previous_finite_system"
    _,data=cut.consume_previous(args,report,budget)
    system,inherited,static=cut.append_one_cut(data,budget)
    ctx.update(system=system,inherited=inherited,static_cut=static)
    report["phase"]="append_all_R168_wrong_quadratic_parity_coefficients"
    parity=append_complete_quadratic_parities(data,system,budget)
    ctx["parity"]=parity
    report["inherited_system"]={k:inherited[k] for k in (
        "normal_coordinate_count","external_equality_rank","free_normal_coordinates",
        "old_reduced_row_count","old_equalities_or_rows_or_path_integrals_regenerated")}
    report["one_new_static_cut"]=static
    report["quadratic_parity"]={k:v for k,v in parity.items() if k!="wrong_parity_coefficient_rows"}
    report["quadratic_parity"]["wrong_parity_coefficient_count"]=len(parity["wrong_parity_coefficient_rows"])
    report["quadratic_parity"]["wrong_parity_family_degrees"]=[
        [r["family"],r["degree"]] for r in parity["wrong_parity_coefficient_rows"]]
    report["phase"]="exact_dual_or_exact_outer_point_after_specific_static_and_parity_cuts"
    print(json.dumps({"phase":report["phase"],"free_coordinates":len(system["free"]),
        "old_rows":inherited["old_reduced_row_count"],"new_static_rows":1,
        "new_parity_halfspaces":parity["new_distinct_halfspaces"]}),flush=True)
    decision=base.certify_zero(system,budget);ctx["decision"]=decision
    excluded=decision["all_coordinates_forced_zero"]
    report.update(completion="complete",phase="static_and_quadratic_parity_continuation_complete",
        positive_character_excluded=excluded,
        outcome=("all_nonzero_true_positive_weight_minus2_characters_excluded_by_exact_outer_system"
                 if excluded else "static_and_quadratic_parity_outer_system_remains_unresolved"))
    report["decision"]={k:v for k,v in decision.items() if k not in ("certificates","outer_candidate")}
    report["decision"]["exact_dual_certificates"]=len(decision.get("certificates",[]))
    report["decision"]["nonzero_exact_outer_candidate_saved"]=decision.get("outer_candidate") is not None
    report["checkpoint"]={"target_weight":-2,
        "all_true_positive_characters_embed_in_the_test":True,
        "all_original_generating_coordinates_are_still_covered":True,
        "same_normal_coordinates_and_same_unique_R164_multiplier":True,
        "one_specific_published_outer_point_excluded":True,
        "all_three_quadratic_families_have_their_complete_R168_parity_rows":True,
        "only_weight_minus2_positive_characters_excluded":excluded,
        "all_positive_characters_excluded":False,"true_character_existence_claimed":False,
        "complete_action_positivity_proved":False,"complete_period_or_ruling_paid":False}


def fake_data():
    return {"normal_coordinate_count":4,"free_normal_coordinates":[0,1,2],
        "normal_coordinates_as_free_linear_forms":[[[0,"1"]],[[1,"1"]],[[2,"1"]],[[0,"1"],[1,"-1"]]],
        "corrected_scalar_k_polynomials":{
            "Q2_0":[[0,[[0,"1"]]],[1,[[1,"1"]]],[5,[[0,"2"]]]],
            "Q2_1":[[0,[[2,"1"]]],[1,[[0,"1"]]],[4,[[1,"-3"]]],[7,[[2,"2"]]]],
            "Q2_2":[[2,[[0,"1"]]],[3,[[1,"1"]]],[7,[[0,"1"],[1,"-1"]]],
                    [9,[[3,"1"],[0,"-1"],[1,"1"]]]]}}
    

def toy_only():
    checks={};budget=base.Budget(30,512)
    names=("rref","construct_system","path_integrals")
    saved={name:getattr(base,name) for name in names}
    def forbidden(*_args,**_kwargs):
        raise AssertionError("new parity consumer attempted old research")
    try:
        for name in names:setattr(base,name,forbidden)
        data=fake_data();data_sha=sha(canonical(data))
        table=base.RowTable(budget)
        table.add(base.unit(2),{"kind":"artificial_preexisting_row"})
        old_records=deepcopy(table.records)
        system={"free":[0,1,2],"reduced":table}
        result=append_complete_quadratic_parities(data,system,budget)
        labels={(r["family"],r["degree"]) for r in result["wrong_parity_coefficient_rows"]}
        assert labels=={("Q2_0",1),("Q2_0",5),("Q2_1",0),("Q2_1",4),
                       ("Q2_2",3),("Q2_2",7),("Q2_2",9)}
        checks["all_stored_wrong_parity_degrees_are_scanned_including_high_degrees"]=True
        assert not labels.intersection({("Q2_0",0),("Q2_1",1),("Q2_1",7),("Q2_2",2)})
        checks["correct_parity_coefficients_are_not_discarded_or_constrained"]=True
        for r in result["wrong_parity_coefficient_rows"]:
            row=base.read_row(r["free_coordinate_equality"],3)
            assert [s["sign"] for s in r["two_halfspaces"]]==[1,-1]
            for s in r["two_halfspaces"]:
                expected=base.row_add((row,s["sign"]))
                assert base.read_row(s["signed_free_linear_form"],3)==expected
                if expected:
                    idx=s["reduced_row_index"]
                    assert table.rows[idx]==base.primitive(expected,equality=False)
        checks["every_nonzero_parity_equality_has_both_exact_inequality_signs"]=True
        zero=next(r for r in result["wrong_parity_coefficient_rows"]
                  if (r["family"],r["degree"])==("Q2_2",9))
        assert not zero["free_coordinate_equality"]
        assert all(s["reduced_row_index"] is None for s in zero["two_halfspaces"])
        checks["an_already_zero_parity_relation_is_recorded_without_a_spurious_row"]=True
        assert table.records[:1]==old_records
        assert any(s["status"]=="already_present" for r in result["wrong_parity_coefficient_rows"]
                   for s in r["two_halfspaces"])
        assert sha(canonical(data))==data_sha
        checks["deduplication_does_not_mutate_the_inherited_rows_or_input"]=True
        # Every coordinate is forced zero in this invented parity example; no LP needed.
        for j in range(3):
            assert tuple(sorted(base.unit(j).items())) in table.keys
            assert tuple(sorted(base.row_add((base.unit(j),-1)).items())) in table.keys
        checks["paired_artificial_relations_control_the_intended_coordinates"]=True
        bad=fake_data()
        bad["corrected_scalar_k_polynomials"]["Q2_0"].append([1,[[0,"1"]]])
        try:append_complete_quadratic_parities(bad,{"free":[0,1,2],"reduced":base.RowTable(budget)},budget)
        except ValueError:checks["ambiguous_degree_metadata_is_rejected"]=True
        else:raise AssertionError("duplicate degree accepted")
        checks["old_RREF_system_and_path_integrals_are_never_called"]=True
    finally:
        for name,value in saved.items():setattr(base,name,value)
    return {"checks":checks,"all_passed":all(checks.values()),
        "artificial_rational_arithmetic_only":True,"real_previous_system_or_head_read":False,
        "real_coefficients_or_path_integrals_evaluated":False,
        "previous_single_cut_artificial_suite_not_repeated":True}


def complete_certificate(report,ctx):
    if "system" not in ctx:return None
    return {"schema":SCHEMA+"-certificate","source_hashes":report["source_hashes"],
        "github_run_id":report["github_run_id"],"github_sha":report["github_sha"],
        "input":report.get("input"),"target_weight":-2,
        "inherited_system_identity_and_unchanged_data":ctx["inherited"],
        "one_new_static_cut":ctx["static_cut"],"complete_quadratic_parity":ctx.get("parity"),
        "updated_reduced_inequalities":ctx["system"]["reduced"].records,
        "free_normal_coordinates":ctx["system"]["free"],"decision":ctx.get("decision"),
        "all_true_positive_characters_embed_in_this_outer_system":True,
        "old_complete_certificate_is_required_to_interpret_normal_coordinates":True,
        "outer_system_feasibility_does_not_prove_a_true_character":True,
        "old_source_system_or_integrals_recomputed":False}


def write_outputs(args,report,certificate):
    args.output.parent.mkdir(parents=True,exist_ok=True);packed=b""
    if certificate is not None:
        raw=canonical(certificate)+b"\n";packed=gzip.compress(raw,mtime=0)
        if len(packed)>args.max_certificate_bytes:
            raise base.Limit("complete static-and-parity certificate exceeds its output budget")
        path=args.output.with_name(args.output.stem+"-certificate.json.gz");path.write_bytes(packed)
        report["complete_necessary_certificate"]={"filename":path.name,"stored_bytes":len(packed),
            "stored_sha256":sha(packed),"raw_bytes":len(raw),"raw_sha256":sha(raw),
            "contains_old_row_binding_one_static_cut_all_quadratic_parities_and_exact_duals":True}
    raw=canonical(report)+b"\n"
    if len(raw)>args.max_main_bytes or len(raw)+len(packed)>4800000:
        raise base.Limit("bounded static-and-parity publication output limit")
    args.output.write_bytes(raw)
    return {"output":str(args.output),"completion":report["completion"],"bytes":len(raw),"sha256":sha(raw)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    for name in ("source-report","source-publication","source-certificate"):
        parser.add_argument("--"+name,type=Path)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--max-seconds",type=float,default=240)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--rational-bits",type=int,default=16384)
    parser.add_argument("--max-main-bytes",type=int,default=95000)
    parser.add_argument("--max-certificate-bytes",type=int,default=4500000)
    args=parser.parse_args()
    if min(args.max_seconds,args.memory_mib,args.rational_bits,
           args.max_main_bytes,args.max_certificate_bytes)<=0:
        parser.error("positive explicit budgets required")
    if args.max_main_bytes>=100000 or args.max_main_bytes+args.max_certificate_bytes>4800000:
        parser.error("main below100KB and total output at most4.8MB required")
    if not args.toy_only and not all((args.source_report,args.source_publication,args.source_certificate)):
        parser.error("the three exact published previous files are required")
    if not args.toy_only and (os.environ.get("GITHUB_ACTIONS")!="true"
                              or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        parser.error("actual continuation only in this public repository Actions")
    started=time.monotonic();budget=base.Budget(args.max_seconds,args.memory_mib,args.rational_bits)
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "source_hashes":{},"target_weight":-2,"positive_character_excluded":False,
        "complete_action_positivity_proved":False,"true_character_existence_claimed":False,
        "theorem_prerequisites":["R164","R166","R168"],
        "old_equalities_or_rows_or_path_integrals_regenerated":False,
        "forcing_or_original_function_or_old_normal_form_evaluated":False,
        "head_export_read":False,"fixed_new_static_k":str(cut.CUT_K),
        "all_wrong_parities_of_Q2_are_added_not_a_selected_candidate_subset":True,
        "floating_status_is_never_a_mathematical_certificate":True,
        "limits":{"elapsed_seconds":args.max_seconds,"polled_memory_mib":args.memory_mib,
                  "rational_bit_ceiling":args.rational_bits,"main_bytes":args.max_main_bytes,
                  "certificate_bytes":args.max_certificate_bytes}}
    ctx={};code=0
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["toy"]=toy_only()
            report.update(completion="toy_passed",phase="new_complete_parity_artificial_interface_only")
        else:actual(args,report,ctx,budget)
    except base.Limit as error:
        code=2;report.update(completion="resource_limit",error=str(error))
    except Exception as error:
        code=1;report.update(completion="implementation_check_failed",
                            error={"type":type(error).__name__,"message":str(error)})
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    try:written=write_outputs(args,report,complete_certificate(report,ctx))
    except base.Limit as error:
        code=2
        failed={k:report[k] for k in (
            "schema","phase","github_repository","github_run_id","github_sha","source_hashes",
            "target_weight","elapsed_seconds","peak_rss_mib") if k in report}
        failed.update(completion="output_limit",error=str(error),positive_character_excluded=False,
                      mathematical_exclusion_not_claimed_without_complete_saved_certificate=True)
        if "input" in report:failed["input_identity_sha256"]=sha(canonical(report["input"]))
        raw=canonical(failed)+b"\n";args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(raw)
        written={"output":str(args.output),"completion":"output_limit","bytes":len(raw),"sha256":sha(raw)}
    print(json.dumps(written),flush=True)
    return code


if __name__=="__main__":
    raise SystemExit(main())

