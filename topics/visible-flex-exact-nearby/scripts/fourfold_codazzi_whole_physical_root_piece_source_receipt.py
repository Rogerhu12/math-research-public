#!/usr/bin/env python3
"""Finalize the exact successful run43669106351 without running mathematics.

Only immutable file validation, copying and readable extraction are performed.
The original mathematical source, manifest, native and25 stages remain unchanged.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,os,shutil,sys,time
from fractions import Fraction
from pathlib import Path

PUBLIC="Rogerhu12/math-research-public"
ORIGINAL_RUN="43669106351"
ORIGINAL_SOURCE="66668065abd27ae37f789adf72a9deda9a15eda33d751f0c4b6fef8e54f17a81"
ORIGINAL_MANIFEST="d30c306e58f3e6be96768b983db4df840843455e2cc5147c84c6e2d7958e5aac"
ORIGINAL_NATIVE="6668c9b2c8f1632e3bd8af392a803335f076c64e1d7fb74dfc9e1605f0e1ee2d"
ORIGINAL_PROCESS="242d82b6f1ead216bf8e90679a9952a2aaad0e9d7ba29293739911e70ab4d145"
ORIGINAL_CI="855bcec6d31a9f0bdb3e3710c4e6418c2be0d816edf09a59da01ab6ec956904d"
ORIGINAL_RUNTIME={"python":"3.12.14","python_flint":"0.9.0","numpy":"2.3.5","scipy":"1.17.0"}
NATIVE_NAME="whole-physical-root-piece-first-Airy-sources.json.gz"
ROOTS=(Fraction(1191984371497,5000000000000),Fraction(2383968743003,10000000000000))
BODY=Fraction(1192029371497,5000000000000)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(value,indent=2,allow_nan=False)+"\n").encode()
    if path.suffix==".gz":
        raw=gzip.compress(raw,mtime=0)
    elif len(raw)>60000:
        raise ValueError("a readable receipt exceeds60000 bytes: "+path.name)
    temporary=path.with_name(path.name+".partial")
    temporary.write_bytes(raw);temporary.replace(path)

def payload_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()

def check_file(path,entry):
    path=Path(path)
    if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
        raise ValueError("an exact original or receipt input changed: "+str(path))
    return path

def ball_upper(value):
    """Order existing saved enclosures by exact decimal endpoints; no new norm."""
    s=value["ball"].strip()
    if s.startswith("[") and s.endswith("]"):
        s=s[1:-1].strip()
    if "+/-" in s:
        midpoint,radius=s.split("+/-",1)
        return Fraction(midpoint.strip() or "0")+abs(Fraction(radius.strip()))
    return Fraction(s)

def compact_channel(value):
    keys=("complete_rows","complete_first_correction_ordinary_L2_source",
          "complete_squared_source_integral","separate_component_L2_bounds")
    return {key:copy.deepcopy(value[key]) for key in keys if key in value}

def compact_case(value):
    keys=("exact_radius","exact_cover","complete","complete_rows",
          "exact_complete_physical_root_piece",
          "original_actual_negative_source_to_primitive_L2_gain",
          "negative_first_correction_source_component_Hminus4over3_to_primitive_L2",
          "positive_collar_first_correction_source_L2","positive_body_first_correction_source_L2",
          "uncertain_root_band_charged_separately_on_each_side",
          "all_complete_means_and_physical_seams_retained",
          "positive_weighted_port_conversion_claimed","complete_corrected_seam_operator_paid",
          "whole_first_corrected_strong_return_or_cutoff97_inverse_claimed")
    result={key:copy.deepcopy(value[key]) for key in keys if key in value}
    result["source_summary"]={key:compact_channel(v) for key,v in value["source_summary"].items()}
    return result

def exact_cover(rows,left,right):
    pairs=sorted(tuple(Fraction(v) for v in row["interval"]) for row in rows)
    return bool(pairs and pairs[0][0]==left and pairs[-1][1]==right
        and all(a<b for a,b in pairs)
        and all(pairs[i][1]==pairs[i+1][0] for i in range(len(pairs)-1)))

def row_view(row):
    keys=("common_row","interval","original_root_row","original_piece","side",
          "exact_rho_cover","uncertain_root_one_sided_charge",
          "radial_weight_integral","complete_squared_source_integral",
          "separate_squared_source_integrals")
    result={key:copy.deepcopy(row[key]) for key in keys if key in row}
    result["complete_original_row_payload_sha256"]=payload_sha(row)
    result["complete_original_source_bounds"]=copy.deepcopy(row["source_bounds"])
    return result

def dominant_rows(rows):
    result={}
    for side in ("negative","positive"):
        selected=[row for row in rows if row["side"]==side]
        if not selected:
            continue
        channels={}
        for key in ("original_first_local","first_nonlocal","independent_even_mean"):
            row=max(selected,key=lambda v:ball_upper(v["separate_squared_source_integrals"][key]))
            channels[key]=row_view(row)
        result[side]=channels
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("repo","manifest","out-dir","prepared"):
        p.add_argument("--"+key,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("the receipt runs in the actual public repository Actions")
    if sha(a.manifest)!=a.manifest_sha:
        raise ValueError("the independent receipt manifest changed")
    if sys.version.split()[0]!="3.12.14":
        raise RuntimeError("the standard-library receipt runtime differs")
    manifest=read(a.manifest)
    if manifest["public_repository"]!=PUBLIC or manifest["kind"]!="exact_completed_whole_root_piece_receipt_manifest":
        raise ValueError("another receipt or repository was supplied")
    a.out_dir.mkdir(parents=True,exist_ok=True)
    process=a.out_dir/"process.json"
    if process.exists():
        raise FileExistsError("preserve every actual receipt attempt")
    state=dict(kind="actual_public_completed_whole_root_piece_receipt_only",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        receipt_source_sha256=sha(__file__),receipt_manifest_sha256=a.manifest_sha,
        complete=False,failure=None,receipt_gates=[],original_run_id=ORIGINAL_RUN,
        original_mathematical_source_sha256=ORIGINAL_SOURCE,
        original_scientific_manifest_sha256=ORIGINAL_MANIFEST,
        original_mathematical_native_sha256=ORIGINAL_NATIVE,
        original_mathematical_process_sha256=ORIGINAL_PROCESS,
        mathematical_subprocesses_started=0,new_target_FFT_Taylor_or_interval_norm_evaluations=0,
        original_successful_scalar_stages_recomputed=0,original_source_rows_recomputed=0,
        original_scientific_native_rewritten=False,
        final_strong_return_full_high_inverse_or_PDE_branch_claimed=False)
    started=time.monotonic();code=1
    def gate(name,value):
        value=bool(value);state["receipt_gates"].append(dict(name=name,passed=value))
        if not value:
            raise ValueError("completed-science receipt gate failed: "+name)
    try:
        pins={}
        for entry in manifest["files"]:
            path=check_file(a.repo/entry["path"],entry)
            pins[entry["path"]]=entry
        for entry in manifest.get("external_completed_natives",[]):
            check_file(a.prepared/entry["prepared_path"],entry)
        state["verified_input_file_count"]=len(pins)
        state["external_original_natural_file_count"]=len(manifest.get("external_completed_natives",[]))
        paths={key:a.repo/value for key,value in manifest["input_paths"].items()}
        oldprocess=read(paths["original_process"])
        oldmanifest=read(paths["original_scientific_manifest"])
        oldworker=read(paths["original_worker"])
        publication=read(paths["original_publication"])
        native=read(paths["original_native"])
        gate("only the exact previously successful scientific native and failed summary wrapper are selected",
            sha(paths["original_source"])==ORIGINAL_SOURCE
            and sha(paths["original_scientific_manifest"])==ORIGINAL_MANIFEST
            and sha(paths["original_CI"])==ORIGINAL_CI
            and sha(paths["original_process"])==ORIGINAL_PROCESS
            and sha(paths["original_native"])==ORIGINAL_NATIVE
            and str(oldprocess["run_id"])==ORIGINAL_RUN
            and oldprocess["actual_returncode"]==0
            and oldprocess["verified_input_file_count"]==len(oldmanifest["files"])==80
            and oldprocess["all_exact_input_pins_preserved_in_manifest"] is True
            and oldprocess["mathematical_complete"] is True
            and oldprocess["mathematical_proved"] is True
            and oldprocess["mathematical_failure"] is None
            and oldprocess["complete"] is False
            and oldprocess["failure"]=={"type":"TypeError","message":"dict() got multiple values for keyword argument 'complete'"})
        gate("the original source manifest runtime and all ten mathematical gates remain unchanged",
            native["source_sha256"]==oldprocess["mathematical_source_sha256"]==ORIGINAL_SOURCE
            and native["input_manifest_sha256"]==oldprocess["manifest_sha256"]==ORIGINAL_MANIFEST
            and native["runtime"]==ORIGINAL_RUNTIME
            and native["complete"] is True and native["proved"] is True and native["failure"] is None
            and len(native["gates"])==10 and all(v["passed"] for v in native["gates"])
            and native["gates"]==oldprocess["mathematical_gates"])
        gate("the original actual wrapper failure and all real pull README records remain preserved",
            str(oldworker["run_id"])==ORIGINAL_RUN and oldworker["actual_returncode"]==1
            and oldworker["complete"] is False and oldworker["manifest_sha256"]==ORIGINAL_MANIFEST
            and publication["actual_returncode"]==1 and publication["complete"] is False
            and str(publication["run_id"])==ORIGINAL_RUN
            and oldworker["readme_checks"]==publication["reviewed_pull_history"]
            and all(v["actual_diff"]=="" for v in oldworker["readme_checks"]))
        state["original_pipeline_failure"]=copy.deepcopy(oldprocess["failure"])
        state["original_actual_mathematical_returncode"]=oldprocess["actual_returncode"]
        state["original_actual_mathematical_wall_seconds"]=oldprocess["mathematical_wall_seconds"]
        state["original_mathematical_gates"]=copy.deepcopy(native["gates"])
        state["scientific_metadata"]=copy.deepcopy(oldprocess["scientific_metadata"])
        for key,value in state["scientific_metadata"].items():
            if key in native and native[key]!=value:
                raise ValueError("an original scientific metadata field changed: "+key)
        selected=native["original_selected_complete_stage_receipts"]
        oldpins={(v["bytes"],v["sha256"]) for v in oldmanifest["files"]}
        gate("all forty-eight original norms and the multiplier receipt retain original frozen pins",
            len(selected)==49
            and all((v["bytes"],v["sha256"]) in oldpins for v in selected)
            and sum(v["native_sha256"]==native["original_Taylor_native_sha256"] for v in selected)==26
            and sum(v["native_sha256"]==native["original_Nraw_native_sha256"] for v in selected)==23)
        base=paths["original_native"].parent
        external={v["original_relative_file"]:v for v in manifest.get("external_completed_natives",[])}
        published={v["file"]:v for v in publication["files"]}
        def natural_path(entry):
            relative=Path(entry["file"])
            if relative.is_absolute() or ".." in relative.parts or relative.parts[0] not in ("stages","cases"):
                raise ValueError("an original natural file leaves its directory")
            if entry["file"] in external:
                spec=external[entry["file"]]
                if spec["bytes"]!=entry["bytes"] or spec["sha256"]!=entry["sha256"]:
                    raise ValueError("the exact complete artifact receipt differs")
                path=a.prepared/spec["prepared_path"]
            else:
                path=base/relative
                relative_repo=str(path.relative_to(a.repo))
                if relative_repo not in pins:
                    raise ValueError("an original natural file is not receipt-manifest pinned")
            check_file(path,entry)
            pub=published["consumers/"+entry["file"]]
            if pub["bytes"]!=entry["bytes"] or pub["original_sha256"]!=entry["sha256"]:
                raise ValueError("the original publication receipt differs")
            return path
        inventory=[];payloads={};kinds={}
        for name,entry in native["stages"].items():
            path=natural_path(entry);value=read(path)
            if not (value["stage"]==name and value["complete"] is True
                and value["source_sha256"]==ORIGINAL_SOURCE
                and value["input_manifest_sha256"]==ORIGINAL_MANIFEST
                and value["runtime"]==ORIGINAL_RUNTIME
                and value["stage_kind"]==entry["stage_kind"]
                and value["original_Taylor_native_sha256"]==native["original_Taylor_native_sha256"]
                and value["original_Nraw_native_sha256"]==native["original_Nraw_native_sha256"]):
                raise ValueError("an exact original scalar stage changed its identity")
            payloads[name]=value["payload"]
            kinds[value["stage_kind"]]=kinds.get(value["stage_kind"],0)+1
            item=copy.deepcopy(entry)
            item.update(name=name,complete=True,complete_payload_sha256=payload_sha(value["payload"]))
            inventory.append(item)
        gate("all twenty-five complete original scalar stages are present without recalculation",
            len(inventory)==25 and kinds=={"profile_stages":1,"radius_budget_stages":8,
                "complete_source_rows":9,"piece_summary_stages":1,"case_summary_stages":6})
        case_receipts=[];case_reports=[];dominants=[];copied_total=0
        rootrows=[payloads[name] for name,entry in native["stages"].items()
                  if entry["stage_kind"]=="complete_source_rows"]
        if len(rootrows)!=9:
            raise ValueError("the nine accepted root rows are incomplete")
        for ci,entry in enumerate(native["case_stages"]):
            path=natural_path(entry);case=read(path)
            if not (case["complete"] is True and case["source_sha256"]==ORIGINAL_SOURCE
                and case["input_manifest_sha256"]==ORIGINAL_MANIFEST
                and case["runtime"]==ORIGINAL_RUNTIME):
                raise ValueError("a completed original radial case changed identity")
            rows=case["rows"];roles=case["row_roles"]
            if len(rows)!=len(roles) or entry["accepted_rows"]!=len(rows) or entry["complete"] is not True:
                raise ValueError("an original completed case receipt is inconsistent")
            counts={key:0 for key in ("copied_original","partial_original","new_complete_root_piece")}
            for row,role in zip(rows,roles):
                if row["interval"]!=role["interval"] or row["side"]!=role["side"]:
                    raise ValueError("a saved row changed its exact role")
                kind=role["kind"]
                if kind=="copied_original":
                    if payload_sha(row)!=role["original_row_payload_sha256"]:
                        raise ValueError("an unchanged original row changed its complete payload")
                elif kind=="new_complete_root_piece":
                    name=role["stage"]
                    if row!=payloads[name] or payload_sha(row)!=role["row_payload_sha256"]:
                        raise ValueError("a saved root-piece row differs from its independent stage")
                else:
                    raise ValueError("the exact successful run contains no partial original row")
                counts[kind]+=1
            copied_total+=counts["copied_original"]
            if counts["new_complete_root_piece"]!=9:
                raise ValueError("a completed case omitted a true physical root row")
            lo,hi=map(Fraction,case["exact_cover"])
            negative=[v for v in rows if v["side"]=="negative"]
            positive=[v for v in rows if v["side"]=="positive"]
            if not (exact_cover(negative,lo,ROOTS[1]) and exact_cover(positive,ROOTS[0],hi)):
                raise ValueError("a completed radial case has a gap or duplicate")
            if any(Fraction(v["interval"][0])<BODY<Fraction(v["interval"][1]) for v in positive):
                raise ValueError("a saved positive row crosses the actual body cut")
            summary=case["complete_case_summary"]
            if not (summary==native["cases"][ci]
                and summary==payloads["complete-recombined-case-summary-"+str(ci)]
                and summary["complete"] is True
                and case["all_original_physical_seam_ledgers_retained"] is True
                and case["no_artificial_interface_source"] is True
                and case["complete_first_corrected_trial_seam_sources_paid"] is False):
                raise ValueError("a completed case summary or physical seam scope changed")
            receipt=copy.deepcopy(entry)
            receipt.update(complete=case["complete"],accepted_rows=len(rows),accepted_row_kinds=counts,
                original_complete_case_sha256=case["original_complete_case_sha256"])
            case_receipts.append(receipt)
            detail=dict(original_run_id=ORIGINAL_RUN,original_case=receipt,
                original_complete_summary=copy.deepcopy(summary),
                original_domain_gates=copy.deepcopy(case["original_bstar_profile"]["domain_gates"]),
                original_normalized_seam_rows=len(case["original_normalized_seam_ledger"]),
                original_normalized_seam_ledger_payload_sha256=payload_sha(case["original_normalized_seam_ledger"]),
                original_outward_states_payload_sha256=payload_sha(case["original_complete_outward_states"]),
                dominant_existing_squared_envelope_rows=dominant_rows(rows),
                interpretation="largest existing upper envelopes, not measured error or signed cancellation")
            details=a.out_dir/"cases"/("radius-"+case["exact_radius"].replace("/","-")+"-receipt.json")
            save(details,detail)
            case_reports.append(dict(file=str(details.relative_to(a.out_dir)),bytes=details.stat().st_size,sha256=sha(details)))
            dominants.append(detail)
        gate("all six complete saved cases keep4329 unchanged exterior rows and both root-band charges",
            len(case_receipts)==len(native["cases"])==6 and copied_total==4329
            and native["copied_original_complete_rows"]==4329
            and native["new_partial_original_rows"]==0)
        piece_summary=payloads["whole-root-piece-complete-two-sided-source-summary"]
        gate("the independent whole-piece source summary and all original mean and seam restrictions agree",
            piece_summary==native["whole_root_piece_source_summary"]
            and native["whole_root_piece_row_count"]==9
            and native["original_complete_physical_seams_retained"]==1079
            and native["original_complete_normalized_seam_rows_retained"]==653
            and native["all_old_circle_and_independent_mean_terms_retained"] is True
            and native["artificial_interface_source_introduced"] is False
            and native["complete_first_corrected_trial_seam_sources_paid"] is False
            and native["positive_weighted_port_conversion_claimed"] is False
            and native["full_high_feedback_strong_return_or_PDE_branch_claimed"] is False)
        inventory_doc=dict(original_run_id=ORIGINAL_RUN,original_native_sha256=ORIGINAL_NATIVE,
            original_science_sha256=ORIGINAL_SOURCE,original_manifest_sha256=ORIGINAL_MANIFEST,
            original_norm_and_multiplier_receipts=selected,complete_original_scalar_stages=inventory,
            complete_original_case_receipts=case_receipts,new_interval_arithmetic_evaluations=0)
        invpath=a.out_dir/"complete-original-natural-stage-inventory.json.gz"
        save(invpath,inventory_doc)
        diagnostics=a.out_dir/"complete-existing-source-diagnostics.json.gz"
        save(diagnostics,dict(original_run_id=ORIGINAL_RUN,original_native_sha256=ORIGINAL_NATIVE,
            whole_root_piece_complete_original_summary=piece_summary,
            nine_complete_root_rows=rootrows,six_complete_case_reports=dominants))
        summary=dict(original_run_id=ORIGINAL_RUN,original_native_sha256=ORIGINAL_NATIVE,
            original_mathematical_returncode=0,original_mathematical_gates=native["gates"],
            original_failed_pipeline=oldprocess["failure"],scientific_metadata=state["scientific_metadata"],
            actual_whole_root_piece_results=piece_summary,
            actual_radius_results=[compact_case(v) for v in native["cases"]],
            nine_root_row_component_integrals=[
                {k:copy.deepcopy(v[k]) for k in ("common_row","interval","side",
                    "complete_squared_source_integral","separate_squared_source_integrals")}
                for v in rootrows],
            case_report_files=case_reports,new_interval_arithmetic_evaluations=0,
            all_original_physical_seams_and_independent_means_preserved=True,
            full_corrected_seam_operator_positive_ports_and_full_high_inverse_still_unpaid=True)
        summary["complete_existing_source_diagnostics"]=dict(file=diagnostics.name,
            bytes=diagnostics.stat().st_size,sha256=sha(diagnostics))
        if len((json.dumps(summary,indent=2,allow_nan=False)+"\n").encode())>60000:
            summary.pop("nine_root_row_component_integrals",None)
            summary["nine_root_row_detail_location"]="nine_complete_root_rows in "+diagnostics.name
        summarypath=a.out_dir/"complete-whole-physical-root-piece-source-summary.json"
        save(summarypath,summary)
        evidence=a.out_dir/"evidence";evidence.mkdir()
        for key in ("original_native","original_process","original_worker","original_publication"):
            source=paths[key];target=evidence/(key+"".join(source.suffixes))
            shutil.copyfile(source,target)
            if sha(target)!=sha(source):
                raise ValueError("original immutable evidence changed during copy")
        state.update(complete=True,actual_returncode=0,original_mathematical_complete=True,
            original_mathematical_proved=True,original_mathematical_failure=None,
            complete_original_scalar_stage_count=len(inventory),complete_scalar_stage_kinds=kinds,
            original_norm_and_multiplier_stage_count=len(selected),complete_case_count=len(case_receipts),
            complete_case_stage_receipts=case_receipts,whole_root_piece_row_count=9,
            copied_original_complete_rows=copied_total,
            actual_whole_root_piece_results={k:compact_channel(v) for k,v in piece_summary.items()},
            actual_radius_results=[compact_case(v) for v in native["cases"]],
            readable_complete_summary=dict(file=summarypath.name,bytes=summarypath.stat().st_size,sha256=sha(summarypath)),
            case_report_files=case_reports,
            complete_original_inventory=dict(file=invpath.name,bytes=invpath.stat().st_size,sha256=sha(invpath)),
            complete_original_diagnostics=dict(file=diagnostics.name,bytes=diagnostics.stat().st_size,sha256=sha(diagnostics)),
            all_natural_stage_and_case_hashes_verified=True,
            original_native_index_and_evidence_copied_byte_identically=True)
        code=0
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));state["complete"]=False
        state["actual_returncode"]=1
    finally:
        state["receipt_wall_seconds"]=time.monotonic()-started
        raw=(json.dumps(state,indent=2,allow_nan=False)+"\n").encode()
        if len(raw)>60000:
            full=a.out_dir/"full-receipt-before-readable-guard.json.gz";save(full,state)
            state.pop("actual_radius_results",None)
            state["full_receipt_archive"]=dict(file=full.name,bytes=full.stat().st_size,sha256=sha(full))
        save(process,state)
        print(json.dumps(dict(complete=state["complete"],failure=state["failure"],
            mathematical_subprocesses_started=0,original_native_sha256=ORIGINAL_NATIVE,
            process_sha256=sha(process)),allow_nan=False),flush=True)
    raise SystemExit(code)

if __name__=="__main__":
    main()
