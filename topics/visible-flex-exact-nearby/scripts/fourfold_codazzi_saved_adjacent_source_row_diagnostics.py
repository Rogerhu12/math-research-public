#!/usr/bin/env python3
"""Diagnose saved complete source rows without re-evaluating an enclosure.

This is a new public Actions diagnostic process. Exact comparison of the
already saved rational upper endpoints is not a new operator norm,
interval integral, target, Taylor coefficient or source enclosure.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,os,re,sys,time
from fractions import Fraction as Q
from pathlib import Path

PUBLIC="Rogerhu12/math-research-public"
ORIGINAL_RUN="43676926141"
SOURCE="fa344d170bca13c3faec22034aabbeab27da6116daef59f45c128c011998758d"
ALGEBRA="071065fcdad85536af613d0d198b0034f27ee575b6b2a1c31752cb6ea4a9bc0b"
MANIFEST="57b978dbff16590d593686a8c7b98b8374aae532b500ec88cf975d3ab3821695"
NATIVE_SHA="5754193c193b9769eeec94bf6a9258489db14f9bfda758bf34a549d71c867a0f"
PROCESS_SHA="9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"
PUBLICATION_SHA="0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"
WORKER_SHA="ec4a322eec84198fe1d3306978de3b5cde171a417c21eb6d7c3f16ef5dc6c87a"
RADII=("1/1000","1/500","1/200","1/100","3/200","1/50")
ROW_COUNTS=(145,275,628,899,1107,1329)
CHANNELS=("complete_pair","original_first_local","first_nonlocal","independent_even_mean")
SIDES=("negative","positive")
TERM_NAMES=("complete_SV","complete_SQ","complete_RQ_J_gd","complete_RQ_JL_h",
    "complete_primitive_error","old_mean_rQ","old_mean_vphi","old_mean_raw_D","old_mean_V0")
MEAN_NAMES=("direct_u_h","complete_uJ_gd","complete_uJL_h","complete_uJB_w",
    "complete_curvature_v_nonmean_w")
CASE_HASHES=(
 "5a80c2f959596095d731f32948ad3d8398ded9914eced9aa2e844dc45926fe18",
 "c6b91d1d2a412461eb82305be0d680ba3294b1029a602d1d2d24cf5c49d21ef4",
 "5bb361b5a6fe706de8d9828cd6f81674b73652e4b0136ec9096d0719d822d3db",
 "23e3a485db14a3028151ce1b0d88cf68cb587a418c1c0aba212f57d066ec5daf",
 "bb50ec2c93c3de337484679ec9ce5e2b1e1db25e92834213fb7d8cc326bd6914",
 "cce603603bbbc35e32897a36a570b98dbb993b8e80396862a7f330c98965264c")
RUNTIME={"python":"3.12.14","python_flint":"0.9.0","numpy":"2.3.5","scipy":"1.17.0"}
NATIVE="complete-correlated-adjacent-source-row-diagnostics.json.gz"
SUMMARY="complete-correlated-adjacent-source-row-diagnostics-summary.json"
SMALLEST="smallest-radius-dominant-source-rows.json"

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def payload_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)
def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(value,indent=2,allow_nan=False)+"\n").encode()
    if path.suffix==".gz":raw=gzip.compress(raw,mtime=0)
    tmp=path.with_name(path.name+".partial");tmp.write_bytes(raw);tmp.replace(path)
def receipt(path,base):
    path=Path(path);return dict(file=str(path.relative_to(base)),bytes=path.stat().st_size,sha256=sha(path))
def checked(path,entry):
    path=Path(path)
    if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
        raise ValueError("a complete original scientific file is absent or changed: "+str(path))
    return read(path)
def safe_file(base,relative):
    relative=Path(relative)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("an input or stage escapes its immutable directory")
    return Path(base)/relative
def original_publication_entry(publication,name):
    selected=[v for v in publication["files"] if v["file"]==name]
    if len(selected)!=1:raise ValueError("an original natural file has no unique publication receipt")
    entry=selected[0]
    expected=entry.get("sha256",entry.get("original_sha256"))
    if entry.get("original_sha256")!=expected:
        raise ValueError("an original published file was transformed")
    return dict(bytes=entry["bytes"],sha256=expected)
def saved_upper(value):
    """Read the exact rational upper endpoint of an already saved decimal ball.

    There is no floating point evaluation, transcendental evaluation, norm
    recomputation or new interval enclosure in this diagnostic operation.
    """
    if isinstance(value,dict):
        if "upper" in value:
            result=Q(str(value["upper"]))
        elif isinstance(value.get("ball"),str):
            text=value["ball"].strip()
            if text.startswith("[") and text.endswith("]"):text=text[1:-1].strip()
            if text.startswith("+/-"):
                result=Q(text[3:].strip())
            elif "+/-" in text:
                mid,rad=text.split("+/-")
                radius=Q(rad.strip())
                if radius<0:raise ValueError("a saved radius is negative")
                result=Q(mid.strip())+radius
            else:result=Q(text)
        else:raise ValueError("a saved scalar has no exact endpoint representation")
    elif isinstance(value,(str,int)):result=Q(value)
    else:raise ValueError("a saved endpoint has an undeclared type")
    if result<0:raise ValueError("a nonnegative stored source bound has a negative upper endpoint")
    return result
def score(row,channel):
    return row["complete_squared_source_integral"] if channel=="complete_pair" else row["separate_squared_source_integrals"][channel]
def row_identity(row,serial,role):
    return dict(serial=serial,common_row=row["common_row"],original_root_row=row["original_root_row"],
        original_piece=row["original_piece"],side=row["side"],interval=copy.deepcopy(row["interval"]),
        selected_row_role=role["kind"],complete_original_row_payload_sha256=payload_sha(row))
def row_diagnostic(row,serial,role):
    result=row_identity(row,serial,role)
    result.update(radial_weight_integral=copy.deepcopy(row["radial_weight_integral"]),
        complete_squared_source_integral=copy.deepcopy(row["complete_squared_source_integral"]),
        separate_squared_source_integrals=copy.deepcopy(row["separate_squared_source_integrals"]),
        source_bounds=copy.deepcopy(row["source_bounds"]))
    for key in ("actual_local_source_is_JP_S_of_unnormalized_Nraw",
                "complete_nine_nonlocal_and_five_independent_mean_terms_retained",
                "uncertain_root_one_sided_charge","exact_rho_cover",
                "correlated_local_numerator_operator_evidence"):
        if key in row:result[key]=copy.deepcopy(row[key])
    operators=row.get("complete_amplitude_operator_evidence",{})
    result["saved_complete_amplitude_operator_bounds"]={
        key:copy.deepcopy(value["bound"]) for key,value in operators.items()
        if isinstance(value,dict) and "bound" in value}
    bounds=row["source_bounds"]
    result["nonlocal_word_order_by_saved_envelope"]=[
        key for key in sorted(TERM_NAMES,key=lambda k:(-saved_upper(bounds["complete_nine_nonlocal_terms"][k]),k))]
    result["independent_mean_word_order_by_saved_envelope"]=[
        key for key in sorted(MEAN_NAMES,key=lambda k:(-saved_upper(bounds["complete_five_independent_even_mean_terms"][k]),k))]
    return result
def interval_cover(rows,left,right):
    spans=sorted(tuple(map(Q,row["interval"])) for row in rows)
    return bool(spans and spans[0][0]==left and spans[-1][1]==right
        and all(a<b for a,b in spans) and all(spans[i][1]==spans[i+1][0] for i in range(len(spans)-1)))
def consume_case(case,ci,native,case_sha):
    if not (case.get("complete") is True and case.get("source_sha256")==SOURCE
        and case.get("input_manifest_sha256")==MANIFEST and case.get("algebra_sha256")==ALGEBRA
        and case.get("runtime")==RUNTIME and case.get("exact_radius")==RADII[ci]
        and len(case["rows"])==ROW_COUNTS[ci] and len(case["row_roles"])==ROW_COUNTS[ci]
        and case["complete_case_summary"]==native["cases"][ci]
        and case.get("summary_stage")=="complete-six-radius-summary-"+str(ci)
        and case.get("selection_stage")=="complete-neighbor-selection-radius-"+str(ci)
        and case.get("exact_old_physical_seams_and_full_independent_means_preserved") is True):
        raise ValueError("a complete saved source case lost its exact identity or summary")
    roots=tuple(map(Q,native["exact_root_interval"]))
    cover=tuple(map(Q,case["complete_case_summary"]["exact_cover"]))
    for side,left,right in (("negative",cover[0],roots[1]),("positive",roots[0],cover[1])):
        if not interval_cover([v for v in case["rows"] if v["side"]==side],left,right):
            raise ValueError("a saved source case lost its complete side or uncertain-root charge")
    table=[];copied=0;selected=0
    for serial,(row,role) in enumerate(zip(case["rows"],case["row_roles"])):
        if row["side"] not in SIDES or role.get("oldserial")!=serial:
            raise ValueError("a saved row lost its side or original order")
        if role["kind"]=="new_complete_neighbor_bound":
            selected+=1
            if (row["original_piece"] not in (2548,2550)
                or role.get("new_complete_row_payload_sha256")!=payload_sha(row)):
                raise ValueError("a selected neighboring row lost its complete payload")
        elif role["kind"] in ("copied_original_complete_row","copied_original_better_complete_bound"):
            copied+=1
            if role.get("original_complete_row_payload_sha256")!=payload_sha(row):
                raise ValueError("an unchanged row lost its complete original payload")
        else:raise ValueError("an unknown saved-row selection role was used")
        source=row["source_bounds"]
        if (set(source["complete_nine_nonlocal_terms"])!=set(TERM_NAMES)
            or set(source["complete_five_independent_even_mean_terms"])!=set(MEAN_NAMES)):
            raise ValueError("a saved complete source row lost an old-circle word or independent mean")
        for channel in CHANNELS:saved_upper(score(row,channel))
        item=row_identity(row,serial,role)
        item["complete_squared_source_integral"]=copy.deepcopy(row["complete_squared_source_integral"])
        item["separate_squared_source_integrals"]=copy.deepcopy(row["separate_squared_source_integrals"])
        table.append(item)
    if selected!=28 or copied!=ROW_COUNTS[ci]-28:
        raise ValueError("the exact28 selected source rows or copied row count changed")
    rankings={};details={}
    for side in SIDES:
        serials=[j for j,v in enumerate(case["rows"]) if v["side"]==side]
        rankings[side]={}
        for channel in CHANNELS:
            order=sorted(serials,key=lambda j:(-saved_upper(score(case["rows"][j],channel)),j))
            rankings[side][channel]=order
            for j in order[:16]:
                if str(j) not in details:details[str(j)]=row_diagnostic(case["rows"][j],j,case["row_roles"][j])
    original_summary=copy.deepcopy(case["complete_case_summary"])
    return dict(exact_radius=RADII[ci],complete=True,original_case_sha256=case_sha,
        original_complete_summary=original_summary,complete_rows=ROW_COUNTS[ci],
        complete_row_identity_and_saved_integral_table=table,
        full_orderings_of_saved_upper_bounds=rankings,
        top_sixteen_row_diagnostics_per_side_and_channel=details,
        selected_complete_neighbor_rows=selected,unchanged_original_complete_rows=copied,
        old_numerical_enclosures_recomputed=0,new_saved_row_diagnostic_consumption=True,
        ordering_is_not_a_lower_bound_for_the_actual_error=True,
        no_original_upper_bound_subtraction=True)
def compact_case(case,top):
    summary=case["original_complete_summary"];out=dict(exact_radius=case["exact_radius"],
        original_case_sha256=case["original_case_sha256"],complete_rows=case["complete_rows"],
        exact_cover=summary["exact_cover"],copied_complete_source_bounds={})
    for side,value in summary["source_summary"].items():
        out["copied_complete_source_bounds"][side]={
            key:copy.deepcopy(value[key]) for key in
            ("complete_rows","complete_first_correction_ordinary_L2_source","separate_component_L2_bounds")}
    out["leading_saved_squared_integral_rows"]={}
    for side in SIDES:
        out["leading_saved_squared_integral_rows"][side]={}
        for channel in CHANNELS:
            values=[]
            for serial in case["full_orderings_of_saved_upper_bounds"][side][channel][:top]:
                row=case["complete_row_identity_and_saved_integral_table"][serial]
                values.append(dict(serial=serial,common_row=row["common_row"],
                    physical_piece=row["original_piece"],original_root_row=row["original_root_row"],
                    selected_row_role=row["selected_row_role"],
                    saved_squared_source_integral=copy.deepcopy(score(row,channel))))
            out["leading_saved_squared_integral_rows"][side][channel]=values
    return out
def text_bytes(value):return len((json.dumps(value,indent=2,allow_nan=False)+"\n").encode())

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--out-dir",type=Path,required=True)
    p.add_argument("--resume",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("saved-row diagnostic consumption runs only in the public Actions repository")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the separately pinned diagnostic manifest changed")
    a.out_dir.mkdir(parents=True,exist_ok=True)
    output=a.out_dir/NATIVE;process=a.out_dir/"process.json"
    if output.exists() or process.exists():raise FileExistsError("preserve every existing complete or failed diagnostic output")
    started=time.monotonic()
    identity=dict(source_sha256=sha(__file__),input_manifest_sha256=a.manifest_sha)
    state=dict(kind="actual_saved_complete_adjacent_source_row_diagnostics",complete=False,failure=None,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        **identity,actual_diagnostic_processes=1,old_numerical_enclosures_recomputed=0,
        new_operator_norms_or_interval_integrals_evaluated=0,new_saved_row_diagnostic_consumption=True,
        original_mathematical_run_id=ORIGINAL_RUN,original_mathematical_native_sha256=NATIVE_SHA,
        original_mathematical_process_sha256=PROCESS_SHA,original_mathematical_publication_sha256=PUBLICATION_SHA,
        actual_returncode=None,original_run_source_sha256=SOURCE,original_run_algebra_sha256=ALGEBRA,
        original_run_manifest_sha256=MANIFEST,gates=[],case_stages=[],complete_cases=[],
        new_complete_diagnostic_case_stages=0,reused_complete_diagnostic_case_stages=0,
        all_original_seams_means_and_scope_flags_retained=True,
        strong_return_cutoff97_inverse_or_PDE_branch_claimed=False)
    def checkpoint():save(output,state)
    def gate(name,condition):
        flag=bool(condition);state["gates"].append(dict(name=name,passed=flag));checkpoint()
        if not flag:raise ValueError("saved-row diagnostic gate failed: "+name)
    def stage_case(ci,path,native):
        name="saved-row-diagnostics-radius-"+str(ci);target=a.out_dir/"stages"/(name+".json.gz")
        case_sha=CASE_HASHES[ci]
        if target.exists():
            stage=read(target);state["reused_complete_diagnostic_case_stages"]+=1
        else:
            payload=consume_case(read(path),ci,native,case_sha)
            stage=dict(name=name,stage=name,stage_kind="saved_complete_row_diagnostic_consumption",
                complete=True,**identity,original_complete_case_sha256=case_sha,
                payload_sha256=payload_sha(payload),payload=payload)
            save(target,stage);state["new_complete_diagnostic_case_stages"]+=1
        if not (stage.get("name")==name and stage.get("stage")==name and stage.get("complete") is True
            and stage.get("stage_kind")=="saved_complete_row_diagnostic_consumption"
            and all(stage.get(k)==v for k,v in identity.items())
            and stage.get("original_complete_case_sha256")==case_sha
            and stage.get("payload_sha256")==payload_sha(stage["payload"])):
            raise ValueError("a complete diagnostic case stage changed its exact identity")
        state["case_stages"].append(receipt(target,a.out_dir))
        state["complete_cases"].append(dict(exact_radius=RADII[ci],complete=True,
            original_case_sha256=case_sha,payload_sha256=stage["payload_sha256"]))
        checkpoint();return stage["payload"]
    try:
        manifest=read(a.manifest)
        gate("only the declared original successful six-case result is diagnosed",
            manifest.get("public_repository")==PUBLIC and manifest.get("original_run_id")==ORIGINAL_RUN)
        pins={v["path"]:v for v in manifest["files"]}
        for item in manifest["files"]:
            path=safe_file(a.repo,item["path"])
            if not path.is_file() or path.stat().st_size!=item["bytes"] or sha(path)!=item["sha256"]:
                raise ValueError("one immutable diagnostic input changed: "+item["path"])
        input_paths=manifest["input_paths"]
        paths={k:safe_file(a.repo,v) for k,v in input_paths.items()}
        wanted=dict(original_native=NATIVE_SHA,original_process=PROCESS_SHA,
            original_publication=PUBLICATION_SHA,original_worker=WORKER_SHA)
        for key,value in wanted.items():
            if sha(paths[key])!=value:raise ValueError("one original actual scientific receipt changed")
        native=read(paths["original_native"]);actual=read(paths["original_process"])
        pub=read(paths["original_publication"]);worker=read(paths["original_worker"])
        gate("the original science actually succeeded with all14 gates and all28 retained stages",
            native.get("complete") is True and native.get("proved") is True and native.get("failure") is None
            and native.get("source_sha256")==SOURCE and native.get("algebra_sha256")==ALGEBRA
            and native.get("input_manifest_sha256")==MANIFEST and native.get("runtime")==RUNTIME
            and len(native.get("gates",[]))==14 and all(v["passed"] for v in native["gates"])
            and actual.get("run_id")==ORIGINAL_RUN and actual.get("actual_returncode")==0
            and actual.get("native_sha256")==NATIVE_SHA and actual.get("all_complete_rows_and_natural_files_verified") is True
            and actual.get("inherited_original_stage_count")==28
            and actual.get("original_scalar_coercion_stages_recomputed")==0
            and pub.get("run_id")==ORIGINAL_RUN and pub.get("actual_returncode")==0 and pub.get("complete") is True
            and worker.get("run_id")==ORIGINAL_RUN and worker.get("actual_returncode")==0 and worker.get("complete") is True)
        gate("the complete physical family source units and outstanding mathematical scope are unchanged",
            native.get("fixed_intrinsic_parameter")=="eta_0" and native.get("input_cutoff")==97
            and native.get("exact_real_delta_radius")=="1/100000000"
            and native.get("exact_complex_coefficient_delta_radius")=="1/100000000"
            and native.get("original_complete_physical_seams_retained")==1079
            and native.get("original_complete_normalized_seam_rows_retained")==653
            and native.get("old_circle_nine_terms_and_five_independent_mean_terms_retained") is True
            and native.get("original_physical_or_parameter_family_replaced") is False
            and native.get("complete_corrected_seam_operator_paid") is False
            and native.get("full_strong_return_or_high_inverse_claimed") is False)
        gate("all six original natural case receipts are present without artificial splitting",
            len(native["case_stages"])==len(native["cases"])==len(actual["complete_case_stage_receipts"])==6)
        for ci in range(6):
            path=paths["case_"+str(ci)];entry=native["case_stages"][ci]
            original=original_publication_entry(pub,"consumers/"+entry["file"])
            if entry["sha256"]!=CASE_HASHES[ci] or original!={k:entry[k] for k in ("bytes","sha256")}:
                raise ValueError("an original case has inconsistent native and publication receipts")
            if path.stat().st_size!=entry["bytes"] or sha(path)!=CASE_HASHES[ci]:
                raise ValueError("an original complete natural case changed bytes")
            receipt0=actual["complete_case_stage_receipts"][ci]
            if any(receipt0[k]!=entry[k] for k in ("file","bytes","sha256")):
                raise ValueError("an original case changed its independently verified actual receipt")
        if a.resume:
            prior=read(a.resume)
            if any(prior.get(k)!=v for k,v in identity.items()):
                raise ValueError("a resumed diagnostic prefix changed source or manifest")
            for entry in prior.get("case_stages",[]):
                old=safe_file(a.resume.parent,entry["file"]);checked(old,entry)
                destination=safe_file(a.out_dir,entry["file"])
                destination.parent.mkdir(parents=True,exist_ok=True)
                if destination.exists():raise FileExistsError("a resumed diagnostic stage would overwrite another file")
                destination.write_bytes(old.read_bytes())
        results=[]
        for ci in range(6):
            results.append(stage_case(ci,paths["case_"+str(ci)],native))
        gate("all4383 saved rows retain the exact source integrals complete means and side covers",
            len(results)==6 and sum(v["complete_rows"] for v in results)==4383
            and sum(v["unchanged_original_complete_rows"] for v in results)==4215
            and all(v["selected_complete_neighbor_rows"]==28 for v in results))
        state["complete_original_mathematical_scope"]={key:copy.deepcopy(native[key]) for key in
            ("fixed_intrinsic_parameter","exact_real_delta_radius","exact_complex_coefficient_delta_radius",
             "exact_root_interval","original_root_piece","physical_neighbor_pieces","input_cutoff",
             "exact_positive_body_cut","actual_first_correction_density","source_window")}
        compact=dict(kind="complete_saved_adjacent_source_row_diagnostic_summary",complete=True,
            **identity,original_run_id=ORIGINAL_RUN,original_native_sha256=NATIVE_SHA,
            original_process_sha256=PROCESS_SHA,case_count=6,rows_consumed=4383,
            old_numerical_enclosures_recomputed=0,new_saved_row_diagnostic_consumption=True,
            ordering_is_not_a_lower_bound_for_the_actual_error=True,
            source_scope=copy.deepcopy(state["complete_original_mathematical_scope"]),
            original_78_completed_mathematical_stages_recomputed=0,
            all_original_1079_physical_and653_normalized_seam_rows_retained=True)
        top=3
        while top>=1:
            compact["displayed_leading_rows_per_channel"]=top
            compact["cases"]=[compact_case(v,top) for v in results]
            if text_bytes(compact)<=60000:break
            top-=1
        if top<1:raise ValueError("the compact saved-row diagnostic view exceeds60000 UTF8 bytes")
        save(a.out_dir/SUMMARY,compact)
        first=results[0];wanted_rows=sorted({first["full_orderings_of_saved_upper_bounds"][side][channel][0]
            for side in SIDES for channel in CHANNELS})
        detail=dict(kind="smallest_radius_complete_saved_dominant_source_rows",complete=True,
            **identity,original_run_id=ORIGINAL_RUN,exact_radius=RADII[0],
            original_case_sha256=CASE_HASHES[0],
            interpretation="Ordering of previously saved upper bounds only; not a lower bound for an actual residual.",
            rows=[copy.deepcopy(first["top_sixteen_row_diagnostics_per_side_and_channel"][str(j)]) for j in wanted_rows])
        if text_bytes(detail)>60000:
            for row in detail["rows"]:row.pop("correlated_local_numerator_operator_evidence",None)
            detail["full_saved_operator_evidence_retained_in_case_diagnostic_stages"]=True
        if text_bytes(detail)>60000:
            raise ValueError("the smallest-radius complete diagnostic view exceeds60000 UTF8 bytes")
        save(a.out_dir/SMALLEST,detail)
        state["readable_summary"]=receipt(a.out_dir/SUMMARY,a.out_dir)
        state["smallest_radius_complete_dominant_rows"]=receipt(a.out_dir/SMALLEST,a.out_dir)
        state["original_readable_science_process"]=copy.deepcopy({
            key:actual[key] for key in ("run_id","run_attempt","workflow_event_commit",
                "actual_scientific_checkout_commit","native_sha256","native_bytes",
                "mathematical_source_sha256","algebra_sha256","manifest_sha256",
                "inherited_original_stage_count","complete_natural_stage_inventory")})
        gate("no new numerical enclosure or original successful mathematics was evaluated",
            state["old_numerical_enclosures_recomputed"]==0
            and state["new_operator_norms_or_interval_integrals_evaluated"]==0)
        state["complete"]=True;state["actual_returncode"]=0
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error))
        state["actual_returncode"]=1
    finally:
        state["diagnostic_wall_seconds"]=time.monotonic()-started
        checkpoint()
        report=copy.deepcopy(state)
        report["diagnostic_native"]=receipt(output,a.out_dir)
        if text_bytes(report)>60000:raise ValueError("the actual diagnostic process receipt exceeds60000 UTF8 bytes")
        save(process,report)
        print(json.dumps(dict(complete=state["complete"],actual_returncode=state["actual_returncode"],
            old_numerical_enclosures_recomputed=0,new_saved_row_diagnostic_consumption=True,
            complete_case_count=len(state["complete_cases"]),failure=state["failure"],
            process_sha256=sha(process)),allow_nan=False),flush=True)
    raise SystemExit(state["actual_returncode"])

if __name__=="__main__":main()
