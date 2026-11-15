#!/usr/bin/env python3
"""Execute and retain only the two same-solution adjacent-piece comparisons."""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path
import fourfold_codazzi_adjacent_piece_scalar_coercion_prefix as predecessor

PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
SCI=TOPIC/"scripts/fourfold_codazzi_adjacent_piece_correlated_first_Airy_sources.py"
ALG=TOPIC/"scripts/fourfold_codazzi_adjacent_piece_correlated_Airy_algebra.py"
NATIVE="correlated-adjacent-piece-first-Airy-sources.json.gz"
KINDS={"new_exact_cubic_difference_stages","new_intrinsic_consumption_stages",
       "new_reference_coefficient_norm_stages","new_piece_comparison_stages",
       "new_reference_radius_budgets","new_complete_source_rows","new_case_summaries"}
ROLES={"copied_original_complete_row","copied_original_better_complete_bound",
       "new_complete_neighbor_bound"}

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
def local(base,relative,kind):
    relative=Path(relative)
    if relative.is_absolute() or ".." in relative.parts or not relative.parts or relative.parts[0]!=kind:
        raise ValueError("a natural "+kind+" file leaves its exact output directory")
    return Path(base)/relative
def receipt(path,base):
    return dict(file=str(Path(path).relative_to(base)),bytes=Path(path).stat().st_size,sha256=sha(path))
def check_receipt(path,entry):
    if not path.is_file() or path.stat().st_size!=entry["bytes"] or sha(path)!=entry["sha256"]:
        raise ValueError("an accepted original natural file is absent or changed: "+str(path))
def expected_identity(repo,manifest,manifest_sha):
    pins={v["path"]:v for v in manifest["files"]}
    return dict(source_sha256=pins[str(SCI)]["sha256"],input_manifest_sha256=manifest_sha,
        algebra_sha256=pins[str(ALG)]["sha256"])
def check_identity(value,expected,runtime=None):
    if any(value.get(k)!=v for k,v in expected.items()):
        raise ValueError("a complete adjacent-piece stage changed its exact scientific identity")
    if runtime is not None and value.get("runtime")!=runtime:
        raise ValueError("a complete adjacent-piece stage changed its exact runtime")
def verified_natural_tree(native,base,repo,manifest,manifest_sha):
    """Check complete original rows or complete new stage payloads; no numerical re-evaluation."""
    expected=expected_identity(repo,manifest,manifest_sha)
    check_identity(native,expected)
    legacy=predecessor.load_policy(repo,manifest)
    if native.get("accepted_scalar_coercion_prefix") is not None and native["accepted_scalar_coercion_prefix"]!=legacy["receipt"]:
        raise ValueError("the one inherited28-stage lineage changed")
    if native.get("complete") is True and (native.get("accepted_scalar_coercion_prefix")!=legacy["receipt"]
        or not set(legacy["stages"]).issubset(native.get("stages",{}))):
        raise ValueError("a completed new result lost its28 original accepted stages")
    runtime=native["runtime"]
    for key in ("python","python_flint","numpy","scipy"):
        if runtime[key]!=manifest["runtime"][key]:
            raise ValueError("one separately pinned scientific runtime changed")
    stages={};inventory=[];kinds={}
    for name,entry in native.get("stages",{}).items():
        path=local(base,entry["file"],"stages");check_receipt(path,entry);value=read(path)
        stage_expected=predecessor.identity_for_stage(name,entry,legacy,expected)
        check_identity(value,stage_expected,runtime)
        if (value.get("name")!=name or value.get("stage")!=name or value.get("complete") is not True
            or value.get("stage_kind") not in KINDS or value["stage_kind"]!=entry["stage_kind"]
            or path.name!=name+".json.gz" or value.get("payload_sha256")!=payload_sha(value["payload"])):
            raise ValueError("one complete natural comparison stage lost its exact identity")
        stages[name]=value
        row=dict(entry);row.update(name=name,complete=True,payload_sha256=value["payload_sha256"],
            inherited_from_exact_scalar_coercion_run=name in legacy["stages"])
        inventory.append(row);kinds[value["stage_kind"]]=kinds.get(value["stage_kind"],0)+1
    cases=[];seen=set()
    original_paths=[Path(repo)/manifest["input_paths"]["whole_case_"+str(i)] for i in range(6)]
    originals={read(path)["exact_radius"]:(path,read(path)) for path in original_paths}
    if len(originals)!=6:raise ValueError("the six exact original cases are not distinct")
    for entry in native.get("case_stages",[]):
        path=local(base,entry["file"],"cases");check_receipt(path,entry);case=read(path)
        check_identity(case,expected,runtime)
        radius=case["exact_radius"]
        if radius in seen or radius not in originals:raise ValueError("a complete case has the wrong exact radius")
        seen.add(radius);oldpath,original=originals[radius]
        if (case.get("complete") is not True or case.get("original_complete_case_sha256")!=sha(oldpath)
            or case.get("exact_cover")!=original.get("exact_cover")):
            raise ValueError("a new case changed its original complete physical domain")
        for key in ("original_normalized_seam_ledger","original_complete_outward_states",
                    "original_complete_case_summary"):
            if key in original and case.get(key)!=original[key]:
                raise ValueError("a new case changed original seam, outward, or failure evidence: "+key)
        rows,roles=case["rows"],case["row_roles"]
        if len(rows)!=len(roles) or len(rows)!=len(original["rows"]):
            raise ValueError("the complete source-row role ledger or original cover is missing")
        selection_name=case["selection_stage"]
        if (selection_name not in stages or stages[selection_name]["stage_kind"]!="new_piece_comparison_stages"
            or stages[selection_name]["payload"].get("row_roles")!=roles
            or stages[selection_name]["payload"].get("original_complete_case_sha256")!=sha(oldpath)):
            raise ValueError("the complete row selection differs from its accepted immutable stage")
        counts={key:0 for key in ROLES}
        for serial,(row,role) in enumerate(zip(rows,roles)):
            kind=role["kind"];index=role["oldserial"]
            if kind not in ROLES or type(index) is not int or index!=serial:
                raise ValueError("a new row has no exact original case-row identity")
            old=original["rows"][index]
            if role.get("original_complete_row_payload_sha256")!=payload_sha(old):
                raise ValueError("an original row payload receipt changed")
            if row.get("interval")!=old.get("interval") or row.get("side")!=old.get("side"):
                raise ValueError("a complete replacement changed its original physical row interval")
            if kind in ("copied_original_complete_row","copied_original_better_complete_bound") and row!=old:
                raise ValueError("an unchanged accepted source row is not its complete original payload")
            if kind!="copied_original_complete_row":
                name=role["stage"]
                if name not in stages or stages[name]["stage_kind"]!="new_complete_source_rows":
                    raise ValueError("a new complete row has no independent immutable source stage")
                candidate=stages[name]["payload"]
                expected_payload=role.get("new_complete_row_payload_sha256")
                if expected_payload!=payload_sha(candidate):
                    raise ValueError("a candidate complete source row has a changed payload receipt")
                if kind=="new_complete_neighbor_bound" and row!=candidate:
                    raise ValueError("a selected complete source row differs from its complete accepted stage")
            counts[kind]+=1
        name=case["summary_stage"]
        if (name not in stages or stages[name]["stage_kind"]!="new_case_summaries"
            or case.get("complete_case_summary")!=stages[name]["payload"]):
            raise ValueError("a complete case summary has no unchanged independent accepted stage")
        current=dict(entry);current.update(complete=True,accepted_rows=len(rows),accepted_row_kinds=counts,
            original_complete_case_sha256=sha(oldpath),summary_stage=name)
        cases.append(current)
    return dict(stage_inventory=inventory,stage_kinds=kinds,case_receipts=cases,
        complete_case_count=len(cases),all_complete_rows_and_natural_files_verified=True,
        accepted_scalar_coercion_prefix=legacy["receipt"],
        inherited_original_stage_count=sum(name in legacy["stages"] for name in native.get("stages",{})))

def compact_channel(value):
    return {k:value[k] for k in ("complete_rows","complete_first_correction_ordinary_L2_source",
        "complete_squared_source_integral","separate_component_L2_bounds") if k in value}
def compact_case(value):
    out={k:value[k] for k in ("exact_radius","complete","proved","exact_cover","rows","complete_rows")
         if k in value and k!="rows"}
    if "source_summary" in value:out["source_summary"]={k:compact_channel(v) for k,v in value["source_summary"].items()}
    for key in ("negative_source","positive_source","source_bounds"):
        if key in value:out[key]=value[key]
    out["complete_summary_payload_sha256"]=payload_sha(value)
    return out

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("repo","manifest","out-dir"):p.add_argument("--"+key,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);p.add_argument("--resume",type=Path);p.add_argument("--resume-sha")
    p.add_argument("--adopt-process",type=Path);p.add_argument("--adopt-process-sha")
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mathematics requires this public repository's own Actions")
    if sha(a.manifest)!=a.manifest_sha:raise ValueError("the pinned adjacent-piece manifest changed")
    manifest=read(a.manifest)
    if manifest["public_repository"]!=PUBLIC:raise ValueError("another repository was supplied")
    a.out_dir.mkdir(parents=True,exist_ok=True);process=a.out_dir/"process.json";native=a.out_dir/NATIVE
    if process.exists() or native.exists():raise FileExistsError("preserve every actual native and failed prefix")
    state=dict(kind="actual_public_correlated_adjacent_piece_first_Airy_sources",
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),manifest_sha256=a.manifest_sha,
        complete=False,failure=None,actual_returncode=None,original_successful_mathematics_recomputed=0,
        complete_strong_return_or_full_inverse_claimed=False)
    code=1
    try:
        for entry in [*manifest["files"],*manifest.get("external_completed_natives",[])]:
            path=a.repo/entry["path"]
            check_receipt(path,entry)
        state["verified_repository_file_count"]=len(manifest["files"])
        state["verified_original_artifact_file_count"]=len(manifest.get("external_completed_natives",[]))
        expected=expected_identity(a.repo,manifest,a.manifest_sha)
        state["mathematical_source_sha256"]=expected["source_sha256"]
        state["algebra_sha256"]=expected["algebra_sha256"]
        command=[sys.executable,"-u",str(a.repo/SCI),"--repo-root",str(a.repo),
                 "--manifest",str(a.manifest),"--out",str(native)]
        if a.resume:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:raise ValueError("the accepted prefix bytes changed")
            command+=["--resume",str(a.resume)];state["original_prefix_sha256"]=a.resume_sha
        state["command"]=command;save(process,state)
        if a.adopt_process:
            if (not a.resume or not a.adopt_process_sha or sha(a.adopt_process)!=a.adopt_process_sha):
                raise ValueError("complete mathematical reuse requires its exact original child receipt")
            prior=read(a.adopt_process);prior_native=read(a.resume)
            prior_child0=(prior.get("actual_returncode")==0 or
                (prior.get("original_complete_success_reused") is True
                 and prior.get("original_mathematical_actual_returncode")==0))
            if (not prior_child0 or prior.get("mathematical_source_sha256")!=expected["source_sha256"]
                or prior.get("algebra_sha256")!=expected["algebra_sha256"]
                or prior.get("manifest_sha256")!=a.manifest_sha
                or prior.get("native_sha256")!=sha(a.resume)
                or prior.get("mathematical_complete") is not True
                or prior.get("mathematical_proved") is not True
                or prior.get("mathematical_failure") is not None
                or prior_native.get("complete") is not True or prior_native.get("proved") is not True
                or prior_native.get("failure") is not None):
                raise ValueError("a claimed complete prefix lacks its actual same-source mathematical success")
            import shutil
            shutil.copyfile(a.resume,native)
            for entry in [*prior_native.get("stages",{}).values(),*prior_native.get("case_stages",[])]:
                source=a.resume.parent/entry["file"];check_receipt(source,entry)
                relative=Path(entry["file"])
                if relative.is_absolute() or ".." in relative.parts or relative.parts[0] not in ("stages","cases"):
                    raise ValueError("a complete accepted natural file leaves its original prefix")
                destination=a.out_dir/relative;destination.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(source,destination);check_receipt(destination,entry)
            evidence=a.out_dir/"original-complete-mathematical-process.json"
            shutil.copyfile(a.adopt_process,evidence)
            state.update(original_complete_success_reused=True,original_mathematical_actual_returncode=0,
                original_success_process_sha256=sha(evidence),actual_new_mathematical_subprocesses=0,
                original_complete_native_sha256=sha(a.resume))
        else:
            state["actual_new_mathematical_subprocesses"]=1;started=time.monotonic()
            with (a.out_dir/"correlated-adjacent-piece-first-Airy-sources.stdout.log").open("wb") as stream:
                try:
                    child=subprocess.run(command,cwd=a.repo,stdout=stream,stderr=subprocess.STDOUT,timeout=2700)
                    state["actual_returncode"]=child.returncode
                except subprocess.TimeoutExpired:
                    state["actual_timeout_seconds"]=2700;state["actual_returncode"]=124
            state["mathematical_wall_seconds"]=time.monotonic()-started
        if native.is_file():
            document=read(native)
            state.update(native_sha256=sha(native),native_bytes=native.stat().st_size,
                mathematical_complete=document.get("complete"),mathematical_proved=document.get("proved"),
                mathematical_failure=document.get("failure"),mathematical_gates=document.get("gates",[]))
            tree=verified_natural_tree(document,native.parent,a.repo,manifest,a.manifest_sha)
            inventory=a.out_dir/"complete-natural-stage-and-original-row-inventory.json.gz"
            save(inventory,tree)
            state["complete_natural_stage_inventory"]=dict(file=inventory.name,bytes=inventory.stat().st_size,
                sha256=sha(inventory),complete_scalar_stage_count=len(tree["stage_inventory"]),
                stage_kinds=tree["stage_kinds"],complete_case_count=tree["complete_case_count"])
            state["all_complete_rows_and_natural_files_verified"]=tree["all_complete_rows_and_natural_files_verified"]
            state["accepted_scalar_coercion_prefix"]=tree["accepted_scalar_coercion_prefix"]
            state["inherited_original_stage_count"]=tree["inherited_original_stage_count"]
            state["complete_case_stage_receipts"]=tree["case_receipts"]
            state["actual_radius_results"]=[compact_case(v) for v in document.get("cases",[])]
            state["complete_scientific_native_payload_sha256"]=payload_sha(document)
            state["actual_piece_results"]=[]
            for value in document.get("pieces",[]):
                item={k:value[k] for k in ("piece","interval","side","exact_entry_seam","complete_common_rows",
                    "complete_comparison_stage") if k in value}
                if "full_complete_source_summary" in value:
                    item["full_complete_source_summary"]=compact_channel(value["full_complete_source_summary"])
                state["actual_piece_results"].append(item)
            for key,value in document.items():
                if key.startswith(("new_","reused_","recovered_","copied_","original_")) and type(value) in (int,bool):
                    state[key]=value
            for key in ("full_strong_return_or_high_inverse_claimed","complete_corrected_seam_operator_paid",
                        "old_circle_nine_terms_and_five_independent_mean_terms_retained",
                        "original_physical_or_parameter_family_replaced","physical_neighbor_pieces",
                        "fixed_intrinsic_parameter","exact_real_delta_radius","exact_complex_coefficient_delta_radius"):
                if key in document:state[key]=document[key]
        state["complete"]=bool((state["actual_returncode"]==0 or state.get("original_complete_success_reused") is True)
            and state.get("mathematical_complete") is True
            and state.get("mathematical_proved") is True and state.get("mathematical_failure") is None
            and state.get("mathematical_gates") and all(v["passed"] for v in state["mathematical_gates"])
            and state.get("complete_natural_stage_inventory",{}).get("complete_case_count")==6
            and len(state.get("actual_radius_results",[]))==6
            and state.get("all_complete_rows_and_natural_files_verified") is True)
        code=0 if state["complete"] else 1
    except BaseException as error:
        state["failure"]=dict(type=type(error).__name__,message=str(error));code=1
    finally:
        raw=(json.dumps(state,indent=2,allow_nan=False)+"\n").encode()
        if len(raw)>60000:
            archive=a.out_dir/"complete-process-before-readable-summary.json.gz";save(archive,state)
            full=copy.deepcopy(state)
            for key in ("actual_piece_results","actual_radius_results","complete_case_stage_receipts"):
                state.pop(key,None)
            state["full_original_process_archive"]=dict(file=archive.name,bytes=archive.stat().st_size,
                sha256=sha(archive),uncompressed_bytes=len(raw))
            state["actual_complete_case_count"]=len(full.get("actual_radius_results",[]))
            if len((json.dumps(state,indent=2,allow_nan=False)+"\n").encode())>60000:
                raise ValueError("the complete actual summary still exceeds60000 UTF8 bytes")
        save(process,state)
        print(json.dumps(dict(complete=state["complete"],actual_returncode=state.get("actual_returncode"),
            failure=state.get("failure"),process_sha256=sha(process)),allow_nan=False),flush=True)
    raise SystemExit(code)

if __name__=="__main__":main()
