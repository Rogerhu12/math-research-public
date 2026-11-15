#!/usr/bin/env python3
"""Public full-normalizer endpoint replacement from four completed scientific records."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import urllib.error,urllib.request,select,importlib.metadata
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_full_normalizer_endpoint_replacement.py"
REPORTS=TOPIC/"notes/full_normalizer_endpoint_replacement_ci"
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def save(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+".partial")
    t.write_text(json.dumps(v,indent=2,ensure_ascii=False,allow_nan=False)+"\n");t.replace(p)
def checked(p,size,digest):
    p=Path(p)
    if not p.is_file() or p.stat().st_size!=size or sha(p)!=digest:
        raise ValueError("one complete pinned input differs: "+str(p))
def read(p):return json.loads(Path(p).read_text())
def relpath(p):
    p=Path(p)
    if p.is_absolute() or ".." in p.parts or not str(p).startswith(str(TOPIC)+"/"):
        raise ValueError("one input left the authorized topic")
    return p
def safe_name(value):
    p=Path(value)
    if p.is_absolute() or not value or ".." in p.parts:
        raise ValueError("one scientific conclusion has an unsafe relative path")
    return p
def rec(p,base):
    p=Path(p);return dict(file=str(p.relative_to(base)),bytes=p.stat().st_size,sha256=sha(p))
def ball(v):
    if isinstance(v,dict):
        if isinstance(v.get("ball"),str):return v["ball"]
        if "upper" in v:return str(v["upper"])
        return json.dumps(v,ensure_ascii=False,separators=(",",":"))
    return str(v)
def cell(v):return str(v).replace("|","\\|").replace("\n"," ")

class TransientMetadataError(RuntimeError):
    """Retryable read-only metadata failure; no failed identity or policy gate is suppressed."""
    pass

def topic_tree_metadata(git,topic,repository):
    """Read the exact published origin/main tree; never request an unpublished local HEAD or a blob body."""
    head=git("rev-parse","origin/main").stdout.strip()
    def oid(value):
        return isinstance(value,str) and len(value)==40 and all(c in "0123456789abcdef" for c in value)
    if not oid(head):raise ValueError("the capacity audit requires an exact Git commit")
    root_tree=git("rev-parse",head+"^{tree}").stdout.strip()
    local_topic_tree=git("rev-parse",head+":"+str(topic)).stdout.strip()
    if not oid(root_tree) or not oid(local_topic_tree):
        raise ValueError("the capacity audit requires complete local commit and tree identities")
    token=os.environ.get("GITHUB_TOKEN")
    if not token:raise RuntimeError("the public metadata request requires its Actions token")
    responses=[]
    class NoMetadataRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self,request,fp,code,message,headers,newurl):
            raise RuntimeError("the capacity metadata endpoint attempted a redirect")
    opener=urllib.request.build_opener(NoMetadataRedirect())
    def request_tree(tree,recursive=False):
        url="https://api.github.com/repos/"+repository+"/git/trees/"+tree
        if recursive:url+="?recursive=1"
        request=urllib.request.Request(url,headers={
            "Accept":"application/vnd.github+json",
            "X-GitHub-Api-Version":"2022-11-28",
            "Authorization":"Bearer "+token})
        # A transient read-only service failure is not a scientific or policy gate.
        # Retry the same frozen tree identity; never substitute stale capacity.
        for attempt in range(4):
            try:
                with opener.open(request,timeout=45) as response:
                    if response.geturl()!=url:
                        raise RuntimeError("the capacity metadata request was redirected")
                    data=response.read(16000001)
                break
            except urllib.error.HTTPError as error:
                if error.code not in (408,425,429,500,502,503,504):
                    raise RuntimeError("the Git tree metadata request returned HTTP "+str(error.code)) from None
                if attempt==3:
                    raise TransientMetadataError("read-only Git tree metadata returned HTTP "+str(error.code)) from None
            except (urllib.error.URLError,TimeoutError) as error:
                if attempt==3:
                    raise TransientMetadataError("read-only Git tree metadata transport failed") from None
            time.sleep(2**attempt)
        if len(data)>16000000:raise ValueError("the Git tree metadata response exceeded its bounded size")
        doc=json.loads(data)
        if doc.get("sha")!=tree or doc.get("truncated") is not False or not isinstance(doc.get("tree"),list):
            raise ValueError("a Git tree metadata identity or complete-response gate failed")
        responses.append(dict(tree=tree,recursive=recursive,bytes=len(data),
            sha256=hashlib.sha256(data).hexdigest(),truncated=False))
        return doc["tree"]
    # Freeze the public origin/main commit before resolving its topic components.
    # Compare with Git's independent commit:topic identity; API URLs contain only exact object IDs.
    tree=root_tree
    for component in topic.parts:
        entries=request_tree(tree)
        matches=[entry for entry in entries if entry.get("path")==component]
        if len(matches)!=1 or matches[0].get("type")!="tree" or matches[0].get("mode")!="040000":
            raise ValueError("the authorized topic is not an exact tree at this commit")
        tree=matches[0].get("sha")
        if not oid(tree):raise ValueError("the topic path contains an invalid Git tree identity")
    if tree!=local_topic_tree:
        raise ValueError("the API and local published-commit topic tree identities differ")
    entries=request_tree(tree,recursive=True)
    seen=set();blobs={};inventory=[];trees=0;gitlinks=0
    for entry in entries:
        path=entry.get("path")
        if (not isinstance(path,str) or not path or path.startswith("/")
            or any(part in ("",".","..") for part in path.split("/")) or path in seen):
            raise ValueError("the complete topic tree contains an invalid or duplicate path")
        seen.add(path)
        kind=entry.get("type");mode=entry.get("mode");digest=entry.get("sha")
        if not oid(digest):raise ValueError("a topic object has an invalid Git identity")
        if kind=="blob":
            size=entry.get("size")
            if type(size) is not int or size<0 or mode not in ("100644","100755","120000"):
                raise ValueError("a topic blob has no exact nonnegative metadata size or valid mode")
            full=str(topic)+"/"+path
            blobs[full]=dict(bytes=size,git_blob=digest,mode=mode)
            inventory.append(dict(path=full,bytes=size,git_blob=digest,mode=mode))
        elif kind=="tree":
            if mode!="040000":raise ValueError("a nested topic tree has the wrong mode")
            trees+=1
        elif kind=="commit":
            if mode!="160000":raise ValueError("a topic Git link has the wrong mode")
            gitlinks+=1
        else:raise ValueError("the complete topic tree has an unsupported entry type")
    inventory.sort(key=lambda entry:entry["path"])
    receipt=dict(method="published_origin_main_Git_Trees_API_metadata_only",commit=head,
        root_tree=root_tree,topic=str(topic),topic_tree=tree,
        truncated=False,all_blob_sizes_checked=True,blob_count=len(blobs),
        blob_bytes=sum(entry["bytes"] for entry in blobs.values()),
        nested_tree_count=trees,gitlink_count=gitlinks,
        complete_blob_metadata_inventory_sha256=hashlib.sha256(
            json.dumps(inventory,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest(),
        metadata_responses=responses,blob_bodies_requested=False)
    return receipt,blobs

def owned_head_delta(git,root,capacity,blob_map,allowed_paths):
    """Audit local unpushed report blobs without querying their unpublished Git tree through the API."""
    base=capacity["commit"];head=git("rev-parse","HEAD").stdout.strip()
    raw=git("diff","--name-status","--no-renames","-z",base,head,"--",str(TOPIC)).stdout
    fields=raw.split("\0")
    if fields[-1:]!=[""]:raise ValueError("the complete local topic delta lacks its terminator")
    fields=fields[:-1]
    if len(fields)%2:raise ValueError("the local topic delta is not an exact name-status list")
    total=capacity["blob_bytes"];count=capacity["blob_count"];changes=[]
    for status,name in zip(fields[0::2],fields[1::2]):
        if name not in allowed_paths or status not in ("A","M","D"):
            raise ValueError("an unpublished local topic change is outside the three owned small conclusions")
        before=blob_map.get(name)
        if status=="A" and before is not None:raise ValueError("an added owned path already exists in the published base")
        if status in ("M","D") and before is None:raise ValueError("a changed owned path is absent from the published base")
        oldbytes=0 if before is None else before["bytes"]
        total-=oldbytes;count-=int(before is not None)
        change=dict(path=name,status=status,published_bytes=oldbytes,
            published_git_blob=None if before is None else before["git_blob"])
        if status!="D":
            line=git("ls-tree","-z",head,"--",name).stdout
            if not line.endswith("\0") or line.count("\0")!=1:
                raise ValueError("the owned HEAD path is not one exact Git entry")
            header,path=line[:-1].split("\t",1);mode,kind,digest=header.split()
            if path!=name or mode!="100644" or kind!="blob" or len(digest)!=40:
                raise ValueError("the owned HEAD conclusion is not a regular text blob")
            body=git("show",head+":"+name).stdout.encode()
            if len(body)>60000:raise ValueError("an owned HEAD conclusion exceeds the small-text limit")
            calculated=hashlib.sha1(b"blob "+str(len(body)).encode()+b"\0"+body).hexdigest()
            if calculated!=digest:raise ValueError("the exact owned HEAD bytes do not match their Git blob")
            total+=len(body);count+=1
            change.update(head_bytes=len(body),head_git_blob=digest,head_sha256=hashlib.sha256(body).hexdigest())
        changes.append(change)
    return dict(method="published_origin_main_API_plus_exact_owned_HEAD_delta",commit=head,
        published_base_commit=base,published_base_topic_tree=capacity["topic_tree"],
        head_topic_tree=git("rev-parse",head+":"+str(TOPIC)).stdout.strip(),
        blob_bytes=total,blob_count=count,owned_local_delta=changes,
        original_complete_base_metadata_inventory_sha256=capacity["complete_blob_metadata_inventory_sha256"],
        exact_owned_paths_only=True,unpublished_tree_requested_from_API=False)


def compact(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,
                       allow_nan=False)+"\n").encode()

def scientific_receipt_valid(proc,source,manifest,parameters,pins,runtime):
    """Reuse only identical complete UT science, never repeat a completed target."""
    p=proc or {};old=p.get("complete_original_receipt_identities",{}) or {}
    scalar=p.get("copied_complete_scalar_inputs_read_verbatim",{}) or {}
    end=p.get("complete_new_endpoint_strong_conclusion",{}) or {}
    src=p.get("complete_new_full_trial_source_conclusion",{}) or {}
    full=p.get("complete_new_full_trial_bound_conclusion",{}) or {}
    select=p.get("complete_original_trial_whole_selection",{}) or {}
    paid=p.get("complete_new_ordered_paid_conclusion",{}) or {}
    rows=p.get("complete_sign_wave_readout",[]) or []
    retained=p.get("retained_row_register",[]) or []
    original=p.get("copied_original_WE_retained_register_read_verbatim",[]) or []
    parts=p.get("copied_complete_four_source_parts_read_verbatim",{}) or {}
    jump=p.get("copied_complete_interface_conclusion_read_verbatim",{}) or {}
    candidates=select.get("complete_candidates",[]) or [];index=select.get("selected_index")
    scalar_keys={"S_A0","Z2_A0","t10","t2minus","mc","vminus","Kcminus","Ec_old","Gcut","Gsource",
        "CSF_old","Kfree_cut_minus","ng0_upper","Astate","C_PC","C_ST4","CGwhole","CWE_old"}
    ids={"physical_mean_matching_rows","full_density_mean_identity_difference",
        "transported_original_low_input","root_head_and_two_reference_blocks",
        "opposite_sign_and_Maslov_realization","final_principal_cross_rows"}
    def is_ball(x):return isinstance(x,dict) and isinstance(x.get("ball"),str)
    return bool(isinstance(proc,dict)
        and p.get("kind")=="actual_full_normalizer_endpoint_replacement_v1"
        and p.get("complete") is True and p.get("proved") is True
        and p.get("actual_returncode")==0 and p.get("failure") is None
        and p.get("source_sha256")==source and p.get("parameters")==parameters
        and p.get("runtime")==runtime and p.get("arithmetic_bits")==320
        and (manifest is None or p.get("input_manifest_sha256")==manifest)
        and p.get("input_sha256")==pins and len(pins)==6
        and len(p.get("gates",[]))==22 and all(v.get("passed") is True for v in p["gates"])
        and set(old)=={"sj_execution","fa_science","wt_science","we_science"}
        and p.get("original_completed_scientific_receipts_read")==4
        and all(v.get("original_file_sha256")==pins[k]
            and v.get("complete_science_canonical_sha256")
            and v.get("info",{}).get("source") and v["info"].get("manifest")
            and v["info"].get("attempt")=="1" and v["info"].get("gates",0)>0
            for k,v in old.items())
        and set(scalar)==scalar_keys and all(is_ball(v) for v in scalar.values())
        and end.get("exact_Af_input_and_output_support")==268435456+191
        and end.get("exact_FT_input_and_output_support")==268435456+575
        and is_ball(end.get("complete_FT_Hminus4_3_to_L2_upper"))
        and end.get("same_closed_interval_upper_used_at_both_endpoints") is True
        and end.get("full_T_inverse_not_assumed") is True
        and src.get("exact_selected_original_whole_part_keys")==parameters["new_source_parts"]
        and src.get("excluded_from_new_trial_but_preserved_old_part")=="complete_finite_FT_FJ"
        and set(parts)==set(parameters["new_source_parts"]+["complete_finite_FT_FJ"])
        and src.get("no_total_minus_upper_operation") is True
        and src.get("complete_Q_F0_F1_F2_and_independent_Zy_mean_row_retained") is True
        and jump.get("complete_interface_count")==3070 and jump.get("genuine_polynomial_join_count")==2549
        and jump.get("conservative_artificial_refinement_count")==521 and jump.get("no_radial_length_factor") is True
        and all(is_ball(full.get(k)) for k in ("complete_physical_cut_endpoint_correction_upper",
            "complete_new_physical_cut_error_upper","complete_cut_receiver_contribution",
            "complete_three_source_receiver_contribution","complete_all_interface_receiver_contribution",
            "complete_fullT_trial_waist_density_error_upper","complete_physical_waist_endpoint_correction_upper",
            "complete_returned_original_TJ_trial_error_upper"))
        and full.get("both_endpoints_norm_paid_before_returning_to_original_trial") is True
        and full.get("cut_ng_times_Bc_is_exact_corrected_Bfree") is True
        and full.get("waist_ng_upper_is_the_actual_right_waist_factor") is True
        and full.get("source_receiver_already_includes_output_waist_ng") is True
        and len(candidates)==2 and index in (0,1)
        and candidates[0].get("bound")==scalar["CSF_old"]
        and candidates[1].get("bound")==full["complete_returned_original_TJ_trial_error_upper"]
        and select.get("complete_selected_SF_bound")==candidates[index].get("bound")
        and select.get("entrywise_minimum_used") is False
        and select.get("comparison")=="final retained outward upper; old wins ties"
        and is_ball(paid.get("complete_paid_Hminus4_3_to_L2_upper"))
        and paid.get("complete_CG_fee_read_verbatim")==scalar["CGwhole"]
        and paid.get("original_state_factor_read_verbatim")==scalar["Astate"]
        and paid.get("exact_original_input_order")==parameters["state_operator_order"]
        and paid.get("same_individually_Lambda_normalized_wave_not_global_commonout") is True
        and paid.get("old_CG_coefficients_and_trial_unchanged_after_return") is True
        and paid.get("coefficient_fee_not_multiplied_by_state_factor") is True
        and len(rows)==4
        and {(x.get("physical_wave"),x.get("physical_input_sign")) for x in rows}=={(-1,-1),(-1,1),(1,-1),(1,1)}
        and all(x.get("complete_paid_Hminus4_3_to_L2_upper")==paid["complete_paid_Hminus4_3_to_L2_upper"]
            and x.get("same_whole_two_sign_operator_not_a_sector_sum") is True for x in rows)
        and len(retained)==6 and retained==original and {x.get("id") for x in retained}==ids
        and all(x.get("status")=="exact-border-unpaid" and x.get("actual_norm_supplied") is False for x in retained)
        and all(p.get(k) is True for k in ("complete_new_full_normalizer_endpoint_bound_proved",
            "complete_new_original_trial_whole_bound_proved","complete_new_ordered_paid_subtotal_proved"))
        and all(p.get(k)==1 for k in ("new_complete_endpoint_strong_bound_count",
            "new_complete_three_part_source_count","new_complete_full_trial_bound_count",
            "new_complete_returned_trial_bound_count","new_complete_whole_selection_count",
            "new_complete_ordered_paid_bound_count"))
        and p.get("new_physical_endpoint_correction_count")==2 and p.get("new_sign_wave_record_count")==4
        and all(p.get(k)==0 for k in ("old_successful_scientific_targets_recomputed",
            "old_scientific_source_imports","old_scientific_source_calls","old_binary_native_or_archive_restored",
            "new_ray_or_KAM_calls","new_radial_or_angular_integrals","old_coordinate_or_normalizer_targets_recomputed"))
        and p.get("retained_mode")=="exact-border-unpaid" and p.get("retained_norm_budget") is None
        and p.get("independent_physical_mean_coordinates")==2
        and p.get("original_input_bytes_modified") is False and p.get("new_recomputable_arrays_persisted") is False
        and all(p.get(k) is False for k in ("complete_full_Ei_Eo_proved","full_incoming_inverse_proved",
            "finite_Schur_inverse_proved","whole_return_R0_proved","actual_nonlinear_background_proved","final_surface_proved")))

def render(state,science):
    s=science or {};end=s.get("complete_new_endpoint_strong_conclusion",{}) or {}
    src=s.get("complete_new_full_trial_source_conclusion",{}) or {}
    full=s.get("complete_new_full_trial_bound_conclusion",{}) or {}
    sel=s.get("complete_original_trial_whole_selection",{}) or {}
    paid=s.get("complete_new_ordered_paid_conclusion",{}) or {}
    ready=s.get("complete_new_ordered_paid_subtotal_proved") is True
    lines=["# Actual full-normalizer endpoint replacement","",
        "- Run: "+str(state["run_id"])+"/"+str(state["run_attempt"]),
        "- Actual child return: "+str(state.get("actual_returncode")),
        "- Complete mathematical receipt: "+str(state.get("complete_mathematical_receipt_available",False)),
        "- Source SHA256: "+state["source_sha256"],
        "- Manifest SHA256: "+state["input_manifest_sha256"],
        "- Complete scientific file: [actual-scientific-conclusion.json](actual-scientific-conclusion.json).",
        "- Original-record audit counter: "+str(s.get("original_completed_scientific_receipts_read",0))+
            " (assigned only after all input gates).",
        "- Old scientific targets, source integrals, ray or normalizer evaluations: 0.",
        "- Old binary inputs, new arrays, artifacts and Releases: 0.",""]
    if ready:
        lines+=["## Complete new bounds","",
            "| Quantity | Complete enclosure |","|---|---|"]
        for label,key,obj in (
            ("Endpoint A_f strong bound","complete_Af_Hminus4_3_to_L2_upper",end),
            ("Endpoint B_f strong bound","complete_Bf_Hminus4_3_to_L2_upper",end),
            ("Full F_T endpoint strong bound","complete_FT_Hminus4_3_to_L2_upper",end),
            ("Three original whole source parts","complete_ordinary_L1_three_part_source_upper",src),
            ("Physical cut endpoint correction","complete_physical_cut_endpoint_correction_upper",full),
            ("New physical cut error","complete_new_physical_cut_error_upper",full),
            ("Cut receiver contribution","complete_cut_receiver_contribution",full),
            ("Three source receiver contribution","complete_three_source_receiver_contribution",full),
            ("All interface receiver contribution","complete_all_interface_receiver_contribution",full),
            ("Full-T trial waist error","complete_fullT_trial_waist_density_error_upper",full),
            ("Physical waist endpoint correction","complete_physical_waist_endpoint_correction_upper",full),
            ("Returned original T_J trial error","complete_returned_original_TJ_trial_error_upper",full),
            ("Selected whole original-trial SF bound","complete_selected_SF_bound",sel),
            ("Updated complete state sum","complete_Cstar_upper",paid),
            ("Updated ordered state contribution","complete_state_error_contribution_upper",paid),
            ("Original complete CG coefficient fee","complete_CG_fee_read_verbatim",paid),
            ("Updated ordered paid subtotal","complete_paid_Hminus4_3_to_L2_upper",paid)):
            lines.append("| "+label+" | "+cell(ball(obj.get(key)))+" |")
        lines+=["","## Same-operator whole selection",""]
        for i,row in enumerate(sel.get("complete_candidates",[])):
            lines.append("- Candidate "+str(i)+" ("+row["label"]+"): "+ball(row["bound"])+".")
        lines+=["- Selected index: "+str(sel.get("selected_index"))+".",
            "- Comparison uses final retained outward upper endpoints; the old whole bound wins ties.","",
            "The full-T trial is a changed operator. The cut correction uses exact ng(c) Bc = Bfree, "
            "and the waist correction retains ng(0) and the same T_J(0) inverse. Both endpoint fees "
            "are paid before returning to the original trial and taking the whole minimum.","",
            "The three original source integrals are selected independently; no total-minus-upper "
            "operation is used. The original fourth part and every original interface subclass remain "
            "verbatim in the scientific file. No old row or integral has been evaluated again.","",
            "WE uses its original state factor once, then adds the whole CG coefficient fee once. "
            "Both physical signs are already in each wave operator. The displayed four sign-wave "
            "records are not an additional sign sum or an uncharged two-wave pair norm.",""]
    else:
        lines+=["No complete new endpoint bound, restored-trial bound or paid subtotal is asserted.",""]
    lines+=["## Original complete receipt identities",""]
    for key,row in (s.get("complete_original_receipt_identities",{}) or {}).items():
        info=row.get("info",{})
        lines.append("- "+key+": run "+str(info.get("run"))+"/"+str(info.get("attempt"))+
            "; SHA256 "+str(row.get("original_file_sha256"))+"; all "+str(info.get("gates"))+" gates.")
    lines+=["","## Retained exact unpaid obligations",""]
    if not s.get("retained_row_register"):
        lines+=["The input audit has not yet copied the complete original register; it remains in the pinned WE receipt.",""]
    for row in s.get("retained_row_register",[]):
        lines.append("- "+row["id"]+": "+row["formula"]+".")
    lines+=["","All independent physical matching means, transported original low inputs, complete "
        "root/second-reference blocks, actual cross rows, global Maslov order and the full incoming "
        "inverse retain their original obligations. Complete E_i/E_o, finite Schur inverse, full return R0, "
        "a nonlinear background and a final surface are not claimed.","","## Structural gates",""]
    lines+=["- "+("PASS" if g["passed"] else "FAIL")+": "+g["name"] for g in s.get("gates",[])]
    if state.get("actual_failure"):
        lines+=["","## Actual failure","",json.dumps(state["actual_failure"],ensure_ascii=False,sort_keys=True)]
    lines+=["","## Actual README pulls",""]
    for r in state.get("readme_checks",[]):
        lines.append("- "+r["time"]+" -> "+r["after"]+"; README diff empty: "+str(r["actual_diff"]==""))
    return "\n".join(lines)+"\n"

def emit_prepublication(state,science):
    report=render(state,science)
    science_raw=None if science is None else compact(science)
    payload=dict(marker="FULL_NORMALIZER_ENDPOINT_COMPLETE_SCIENTIFIC_PREPUBLICATION_V1",
        source_sha256=state["source_sha256"],manifest_sha256=state["input_manifest_sha256"],
        run_id=state["run_id"],run_attempt=state["run_attempt"],
        actual_returncode=state.get("actual_returncode"),scientific_result=science,report_text=report)
    raw=compact(payload)
    status=dict(marker="FULL_NORMALIZER_ENDPOINT_PREPUBLICATION_STATUS",
        actual_returncode=state.get("actual_returncode"),
        complete_mathematics=state.get("complete_mathematical_receipt_available",False),
        gates_passed=sum(g.get("passed") is True for g in (science or {}).get("gates",[])),
        gates_total=len((science or {}).get("gates",[])),
        science_bytes=None if science_raw is None else len(science_raw),
        science_sha256=None if science_raw is None else hashlib.sha256(science_raw).hexdigest(),
        payload_bytes=len(raw),payload_sha256=hashlib.sha256(raw).hexdigest(),
        failure=None if len(raw)<=59000 else "complete_prepublication_payload_over59000")
    status_raw=compact(status)
    if len(status_raw)>1000:raise ValueError("prepublication status exceeds1000 bytes")
    print(status_raw.decode(),end="",flush=True)
    if len(raw)>59000:
        raise ValueError("full full-normalizer-endpoint science is saved and printed; prepublication payload exceeds59000")
    print(raw.decode(),end="",flush=True)
    process=compact(dict(marker="FULL_NORMALIZER_ENDPOINT_EXECUTION_PREPUBLICATION_V1",execution=state))
    if len(process)>59000:
        raise ValueError("full full-normalizer-endpoint science is preserved; execution metadata exceeds59000")
    print(process.decode(),end="",flush=True)
    return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
        process_bytes=len(process),process_sha256=hashlib.sha256(process).hexdigest(),
        complete_science_and_report_preserved=True,before_any_git_publication=True)

def accept_live_rules(root,git,initial,manifest,state):
    relative=relpath(manifest["operational_live_review_index"])
    index_path=root/relative
    if not index_path.is_file() or index_path.stat().st_size>60000:
        raise ValueError("the explicit operational live review index is absent or too large")
    index=read(index_path);policy=initial["large_data_policy"]
    if (index.get("kind")!="explicit_live_review_index_for_unchanged_public_execution_rules"
        or index.get("repository")!=PUBLIC or index.get("execution_policy")!=policy
        or index.get("new_or_changed_operational_rules_require_new_worker_review") is not True
        or index.get("unread_README_revisions_are_not_accepted") is not True):
        raise ValueError("the live index attempted to change an execution policy")
    current={name:sha(root/name) for name in initial["readme_sha256"]}
    matching=[v for v in index.get("accepted_reviews",[]) if v.get("readme_sha256")==current]
    if not matching:
        raise RuntimeError("new unread README revision requires its actual diff and a root review")
    for record in matching:
        name=relpath(record["path"]);path=root/name
        checked(path,record["bytes"],record["sha256"])
        review=read(path);commit=record.get("read_commit")
        if (not isinstance(commit,str) or len(commit)!=40
            or any(c not in "0123456789abcdef" for c in commit)
            or record.get("all_operational_rules_unchanged") is not True
            or record.get("scientific_input_manifests_and_sources_not_changed") is not True
            or review.get("repository")!=PUBLIC or review.get("read_commit")!=commit
            or review.get("readme_sha256")!=current
            or review.get("large_data_policy")!=policy
            or review.get("scientific_input_manifests_and_sources_not_changed") is not True
            or review.get("new_unread_rules_must_still_be_reported_and_applied") is not True):
            raise ValueError("a live review did not retain the exact unchanged execution policy")
        if git("cat-file","-e",commit+"^{commit}",check=False).returncode:
            git("fetch","--filter=blob:none","--no-tags","origin",commit)
        for readme,digest in current.items():
            text=git("show",commit+":"+readme).stdout
            if hashlib.sha256(text.encode("utf-8")).hexdigest()!=digest:
                raise ValueError("the separately read commit does not contain the exact current README")
        receipt=dict(path=str(name),bytes=record["bytes"],sha256=record["sha256"],
            read_commit=commit,readme_sha256=current,actual_review_commit_README_bytes_verified=True,
            all_operational_rules_unchanged=True)
        state.setdefault("accepted_live_rule_versions",[])
        if receipt not in state["accepted_live_rule_versions"]:
            state["accepted_live_rule_versions"].append(receipt)
        state["actual_reviewed_readme_sha256"]=current
        state["live_review_index"]=dict(path=str(relative),bytes=index_path.stat().st_size,
            sha256=sha(index_path),observed_at_commit=git("rev-parse","HEAD").stdout.strip())
        return receipt
    raise RuntimeError("no valid explicitly reviewed current README exists")


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--mode",choices=("hydrate","run"),required=True)
    p.add_argument("--manifest",type=Path,required=True);p.add_argument("--manifest-sha",required=True)
    p.add_argument("--pipeline-sha",required=True)
    p.add_argument("--rules",type=Path,required=True);p.add_argument("--rules-sha",required=True)
    p.add_argument("--work",type=Path);p.add_argument("--out-dir",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("only this public repository Actions may evaluate new full-normalizer-endpoint mathematics")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:
        raise ValueError("the separately pinned full-normalizer-endpoint manifest or reviewed rules changed")
    m=read(a.manifest);rules=read(a.rules)
    if (m.get("public_repository")!=PUBLIC or rules.get("repository")!=PUBLIC
        or m.get("kind")!="full_normalizer_endpoint_replacement_public_inputs_v1"
        or m.get("expected_actual_gate_count")!=22
        or m.get("source_sha256")!=a.pipeline_sha
        or m.get("file_sha256")!={x["path"]:x["sha256"] for x in m["files"]}
        or len(m["files"])!=9 or len(m["file_sha256"])!=9
        or set(m["current_input_paths"])!=set(m["file_sha256"])
        or set(m["input_paths"].values())!=set(m["file_sha256"])
        or m.get("legacy_artifact_inputs")!=[] or m.get("all_inputs_are_current_small_texts") is not True
        or m.get("old_successful_scientific_calls_allowed") is not False
        or m.get("new_native_arrays_or_artifact_persistence_allowed") is not False):
        raise ValueError("the exact new full-normalizer-endpoint input contract changed")
    for key in ("reproducible_data_persisted_in_repository","reproducible_data_persisted_in_Releases",
                "new_reproducible_Actions_output_uploads"):
        if rules["large_data_policy"].get(key) is not False:
            raise ValueError("the current complete rule15 policy is required")
    rm=a.manifest.relative_to(root);rr=a.rules.relative_to(root);rw=Path(__file__).resolve().relative_to(root)
    gb=["git","-c","safe.directory="+str(root)]
    if a.mode=="hydrate":
        paths={str(PIPELINE),str(rw),str(rm),str(rr),str(REPORTS)+"/"}|set(rules["readme_sha256"])
        paths.update(entry["path"] for entry in m["files"])
        paths.add(m["operational_live_review_index"])
        paths.add(str(TOPIC/"notes")+"/*reviewed-public-CI-rules*.json")
        subprocess.run(gb+["sparse-checkout","set","--no-cone","--stdin"],cwd=root,
            input="\n".join("/"+v for v in sorted(paths))+"\n",text=True,check=True)
        print("Hydrated only pinned small text and explicit rule reviews; no original native or archive is restored.",flush=True)
        return
    if a.work is None or a.out_dir is None:
        raise ValueError("temporary full-normalizer-endpoint work and outcome directories are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():
        raise FileExistsError("preserve the previous complete or partial full-normalizer-endpoint run")
    if any(v.is_relative_to(root) for v in (work,out)):
        raise ValueError("all new numerical arrays must remain outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__)
    state=dict(kind="actual_public_full_normalizer_endpoint_execution_v1",repository=PUBLIC,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_commit=os.environ["GITHUB_SHA"],worker_source_sha256=ws,
        source_sha256=a.pipeline_sha,input_manifest_sha256=a.manifest_sha,
        reviewed_rules_sha256=a.rules_sha,explicitly_read_rules_commit=rules["read_commit"],
        started_utc=utc(),complete=False,actual_returncode=None,readme_checks=[],
        actual_new_scientific_processes=0,old_numerical_enclosures_recomputed=0,
        new_artifact_count=0,new_Release_count=0,
        reproducible_data_published_to_repository=False,
        complete_original_input_array_recomputation=False,
        new_per_row_arrays_retained_after_job=False,
        final_topic_complete=False)
    report=root/REPORTS/("run-"+state["run_id"]+"-"+state["run_attempt"])
    owned_paths={str((report/name).relative_to(root))
        for name in ("actual-result.md","execution.json","actual-scientific-conclusion.json")}
    env=os.environ.copy();token=env.pop("GITHUB_TOKEN")
    env.update(GIT_TERMINAL_PROMPT="0",GIT_CONFIG_COUNT="1",
        GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
        GIT_CONFIG_VALUE_0="AUTHORIZATION: basic "+base64.b64encode(("x-access-token:"+token).encode()).decode())
    def git(*args,check=True,stdout=None):
        result=subprocess.run(gb+list(args),cwd=root,env=env,text=stdout is None,
            stdout=subprocess.PIPE if stdout is None else stdout,stderr=subprocess.PIPE,timeout=900)
        if check and result.returncode:
            err=result.stderr if isinstance(result.stderr,str) else result.stderr.decode("utf-8","replace")
            raise RuntimeError("public Git "+str(args[0])+" failed: "+err[:1200])
        return result
    def sync():
        before=git("rev-parse","HEAD").stdout.strip()
        git("pull","--rebase","origin","main")
        after=git("rev-parse","origin/main").stdout.strip()
        diff=git("diff",before,after,"--",*rules["readme_sha256"]).stdout
        state["readme_checks"].append(dict(time=utc(),before=before,after=after,actual_diff=diff,
            explicitly_reviewed_commit=rules["read_commit"]))
        save(out/"worker-process.json",state)
        try:
            review=accept_live_rules(root,git,rules,m,state)
        except Exception:
            print(diff,flush=True);raise
        state["readme_checks"][-1].update(accepted_review_sha256=review["sha256"],
            separately_read_rules_commit=review["read_commit"])
        if sha(a.rules)!=a.rules_sha or sha(a.manifest)!=a.manifest_sha or sha(root/PIPELINE)!=a.pipeline_sha:
            raise ValueError("a pinned full-normalizer-endpoint source manifest or rule record changed during pull")
        if sha(root/rw)!=ws:
            raise ValueError("the currently running immutable full-normalizer-endpoint wrapper changed")
        for name in m["current_input_paths"]:
            if sha(root/relpath(name))!=m["file_sha256"][name]:
                raise ValueError("an immutable current full-normalizer-endpoint source or contract changed")
        published,blobs=topic_tree_metadata(git,TOPIC,PUBLIC)
        capacity=owned_head_delta(git,root,published,blobs,owned_paths)
        state.update(current_published_topic_capacity_metadata=published,
            current_topic_capacity_metadata=capacity,current_topic_blob_bytes=capacity["blob_bytes"],
            current_topic_blob_count=capacity["blob_count"],current_topic_metadata_commit=capacity["commit"],
            current_topic_below_200000000_bytes=capacity["blob_bytes"]<200000000)
        save(out/"worker-process.json",state)
        if capacity["blob_bytes"]+120000>=200000000:
            raise ValueError("the actual topic lacks the required120000-byte small-conclusion reserve")
    last_checkpoint=time.monotonic()
    def metadata_event(error,healthy):
        event=dict(time=utc(),type=type(error).__name__,message=str(error),
            healthy_child_preserved=healthy,completed_child_not_repeated=not healthy,
            publication_deferred_without_stale_capacity=True)
        previous=state.get("metadata_retry_event_chain_sha256","0"*64)
        state["metadata_retry_event_chain_sha256"]=hashlib.sha256(
            bytes.fromhex(previous)+compact(event)).hexdigest()
        state["metadata_retry_event_count"]=state.get("metadata_retry_event_count",0)+1
        state.setdefault("last_read_only_metadata_retry_events",[]).append(event)
        state["last_read_only_metadata_retry_events"]=state["last_read_only_metadata_retry_events"][-12:]
        state["metadata_publication_retry_pending"]=True
        save(out/"worker-process.json",state)
        print(json.dumps(dict(kind="FULL_NORMALIZER_ENDPOINT_DEFERRED_READ_ONLY_METADATA_PUBLICATION",**event,
            full_event_count=state["metadata_retry_event_count"],
            full_event_chain_sha256=state["metadata_retry_event_chain_sha256"])),flush=True)
    def checkpoint(force=False):
        nonlocal last_checkpoint
        interval=60 if state.get("metadata_publication_retry_pending") else 600
        if force or time.monotonic()-last_checkpoint>=interval:
            try:
                # This performs real pull, live README review, and frozen pin checks
                # BEFORE any potentially retryable read-only capacity request.
                sync()
                state["metadata_publication_retry_pending"]=False
            except TransientMetadataError as error:
                if child is None or child.poll() is not None:
                    raise
                # Exact policy, identity, shape, and capacity violations are NOT
                # this type. A healthy immutable scientific child stays outside Git.
                metadata_event(error,True)
            last_checkpoint=time.monotonic()
    def copy_current(entry):
        name=relpath(entry["path"]);src=root/name;dst=work/name
        if name.suffix not in (".py",".md",".json") or not 0<entry["bytes"]<100000:
            raise ValueError("all nine full-normalizer-endpoint inputs must be complete small current text")
        checked(src,entry["bytes"],entry["sha256"])
        dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
        checked(dst,entry["bytes"],entry["sha256"])
        return dst,dict(role=entry["role"],path=str(name),bytes=entry["bytes"],
            sha256=entry["sha256"],origin="exact_current_small_text")
    proc=None;child=None;runtime=None
    try:
        git("config","user.name","github-actions[bot]")
        git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
        sync();last_checkpoint=time.monotonic()
        pins=m["mathematical_input_sha256"];parameters=m["parameters"]
        runtime={"Python":sys.version.split()[0],
                 "python_flint":importlib.metadata.version("python-flint")}
        state["actual_scientific_runtime"]=runtime
        if runtime!=m["scientific_runtime"]:
            raise ValueError("exact Python and directed arithmetic runtime differ before reuse")
        # A manifest/worker-only change cannot authorize repetition of completed mathematics.
        for path in sorted((root/REPORTS).glob("*/execution.json")):
            previous=read(path)
            if previous.get("source_sha256")!=a.pipeline_sha:
                continue
            ref=previous.get("scientific_conclusion")
            same_record=previous.get("mathematical_input_sha256")==pins
            if ref:
                pp=path.parent/safe_name(ref["file"])
                checked(pp,ref["bytes"],ref["sha256"])
                prior=read(pp)
                if scientific_receipt_valid(prior,a.pipeline_sha,None,parameters,pins,runtime):
                    print(json.dumps(dict(reused_complete_same_scientific_conclusion=str(pp.relative_to(root)),
                        original_run_id=previous["run_id"],original_science_bytes=ref["bytes"],
                        original_science_sha256=ref["sha256"],execution_sha256=sha(path),
                        original_wrapper_complete=previous.get("complete"),
                        new_scientific_processes=0,old_successful_mathematics_recomputed=0)),flush=True)
                    return
            if same_record and previous.get("actual_new_scientific_processes",0)>0:
                raise RuntimeError("same full-normalizer endpoint arithmetic has a prior incomplete outcome; require its concrete review and preserved scientific-result review")
        state["mathematical_input_sha256"]=pins
        inputs=[];index_files={}
        for entry in m["files"]:
            dst,receipt=copy_current(entry)
            inputs.append(receipt)
            index_files[entry["role"]]=dict(path=str(dst),bytes=dst.stat().st_size,sha256=entry["sha256"])
            checkpoint()
        state["actual_original_Git_input_receipts"]=inputs
        state["actual_verified_Git_input_count"]=len(inputs)
        state["actual_verified_Git_input_receipts_sha256"]=hashlib.sha256(compact(inputs)).hexdigest()
        tm=work/rm;tm.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.manifest,tm)
        checked(tm,a.manifest.stat().st_size,a.manifest_sha)
        tr=work/rr;tr.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.rules,tr)
        checked(tr,a.rules.stat().st_size,a.rules_sha)
        parsed=[]
        for entry in m["files"]:
            if entry["path"].endswith(".py"):
                source=work/relpath(entry["path"]);ast.parse(source.read_text(),filename=str(source))
                parsed.append(dict(path=entry["path"],sha256=entry["sha256"]))
        state.update(complete_immutable_Python_AST_closure_passed=True,
            complete_immutable_Python_AST_file_count=len(parsed),
            complete_immutable_Python_AST_inventory_sha256=hashlib.sha256(compact(parsed)).hexdigest())
        if len(inputs)!=9 or len(parsed)!=3:
            raise ValueError("the complete nine-input and three-Python AST closure differs")
        state["old_binary_parts_restored"]=0
        state["old_artifacts_downloaded"]=0
        state["old_producers_or_integrals_reexecuted"]=0
        state["new_artifact_count"]=0;state["new_Release_count"]=0
        cmd=[sys.executable,"-u",str(work/PIPELINE),"--manifest",str(tm),
            "--manifest-sha",a.manifest_sha,"--bits","320",
            "--out",str(out/"actual-scientific-conclusion.json")]
        for role,digest in pins.items():
            if index_files[role]["sha256"]!=digest:
                raise ValueError("one complete full-normalizer-endpoint mathematical identity changed")
            cmd+=["--"+role.replace("_","-"),index_files[role]["path"]]
        state["command_sha256"]=hashlib.sha256(compact(cmd)).hexdigest()
        state["actual_scientific_checkout_commit"]=git("rev-parse","HEAD").stdout.strip()
        state["scientific_child_launch_attempted"]=True
        state["old_flow_root_mean_or_Airy_recomputations"]=0
        save(out/"worker-process.json",state)
        ce=os.environ.copy();ce["ACTUAL_CHECKOUT_COMMIT"]=state["actual_scientific_checkout_commit"]
        for key in ("GITHUB_TOKEN","GH_TOKEN"):
            ce.pop(key,None)
        started=time.monotonic();timeout=m["new_scientific_timeout_seconds"]
        logpath=out/"new-scientific-child.stdout.log"
        with logpath.open("wb") as log:
            child=subprocess.Popen(cmd,cwd=work,env=ce,stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,start_new_session=True,bufsize=0)
            state["actual_new_scientific_processes"]=1
            fd=child.stdout.fileno();os.set_blocking(fd,False)
            # Tee continuously: scientific prefix checkpoints reach Actions before
            # later failure, timeout, capacity, or publication-format checks.
            eof=False
            while not eof:
                ready,_,_=select.select([fd],[],[],1)
                if ready:
                    raw=os.read(fd,1<<16)
                    if raw:
                        log.write(raw);log.flush()
                        sys.stdout.buffer.write(raw);sys.stdout.buffer.flush()
                    else:
                        eof=True
                if child.poll() is None and time.monotonic()-started>timeout:
                    state["timeout_seconds"]=timeout
                    os.killpg(child.pid,signal.SIGTERM)
                    try:child.wait(timeout=15)
                    except subprocess.TimeoutExpired:
                        os.killpg(child.pid,signal.SIGKILL);child.wait()
                checkpoint()
                if child.poll() is not None and not ready:
                    raw=os.read(fd,1<<16)
                    if raw:
                        log.write(raw);log.flush()
                        sys.stdout.buffer.write(raw);sys.stdout.buffer.flush()
                    else:
                        eof=True
            child.wait();state["actual_returncode"]=child.returncode
            state["complete_child_stdout_tee"]=True
        state["new_scientific_child_wall_seconds"]=time.monotonic()-started
        target=out/"actual-scientific-conclusion.json"
        proc=read(target) if target.is_file() else None
        valid=scientific_receipt_valid(proc,a.pipeline_sha,a.manifest_sha,parameters,pins,runtime)
        state["complete_mathematical_receipt_available"]=valid
        state["complete"]=bool(child.returncode==0 and valid)
        state["actual_failure"]=None if state["complete"] else (
            proc.get("failure") if proc and proc.get("failure") else
            dict(type="IncompleteScientificReceipt",message="the full twenty-two-gate full-normalizer-endpoint receipt did not validate"))
    except BaseException as error:
        if child is not None and child.poll() is None:
            os.killpg(child.pid,signal.SIGTERM)
            try:child.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(child.pid,signal.SIGKILL);child.wait()
        if child is not None:
            state["actual_returncode"]=child.poll()
        state["actual_failure"]=dict(type=type(error).__name__,message=str(error))
        target=out/"actual-scientific-conclusion.json"
        if target.is_file():
            proc=read(target)
        if proc is not None:
            state["complete_mathematical_receipt_available"]=scientific_receipt_valid(
                proc,a.pipeline_sha,a.manifest_sha,m["parameters"],m["mathematical_input_sha256"],
                runtime)
        state["complete"]=False
    state["finished_mathematical_stage_utc"]=utc()
    if child is not None and not state.get("complete_child_stdout_tee"):
        # After any hard supervision failure, drain the terminated child's pipe.
        with (out/"new-scientific-child.stdout.log").open("ab") as log:
            stop=time.monotonic()+10
            while time.monotonic()<stop:
                ready,_,_=select.select([child.stdout.fileno()],[],[],1)
                if not ready:
                    continue
                raw=os.read(child.stdout.fileno(),1<<16)
                if not raw:
                    state["complete_child_stdout_tee"]=True;break
                log.write(raw);log.flush();sys.stdout.buffer.write(raw);sys.stdout.buffer.flush()
    target=out/"actual-scientific-conclusion.json"
    if target.is_file():
        raw=target.read_bytes()
        print(json.dumps(dict(kind="FULL_NORMALIZER_ENDPOINT_ATOMIC_SCIENCE_REPRINT",
            bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())),flush=True)
        print("FULL_NORMALIZER_ENDPOINT_SCIENTIFIC_RESULT_BEGIN",flush=True)
        print(raw.decode(),end="",flush=True)
        print("FULL_NORMALIZER_ENDPOINT_SCIENTIFIC_RESULT_END",flush=True)
        state["complete_atomic_scientific_result_reprinted"]=True
    outputs=[out/name for name in ("actual-scientific-conclusion.json","new-scientific-child.stdout.log")]
    state["output_hashes"]=[rec(path,out) for path in outputs if path.is_file()]
    if proc is not None:
        original=out/"actual-scientific-conclusion.json"
        if original.read_bytes()!=compact(proc):
            raise ValueError("the complete full-normalizer-endpoint child science must retain its original canonical bytes")
        state["scientific_conclusion"]=dict(file="actual-scientific-conclusion.json",
            bytes=original.stat().st_size,sha256=sha(original),
            complete=proc.get("complete"),actual_returncode=proc.get("actual_returncode"),
            actual_gate_count=len(proc.get("gates",[])),
            actual_passed_gate_count=sum(g.get("passed") is True for g in proc.get("gates",[])),
            original_result_printed_before_any_format_gate=True)
    save(out/"worker-process.json",state)
    state["recoverable_prepublication_stdout"]=emit_prepublication(state,proc)
    save(out/"worker-process.json",state)
    # Publication changes only these three small scientific/operational files.
    # Full science, all prefix checkpoints and child log are already in stdout.
    report.mkdir(parents=True,exist_ok=True)
    def snapshot():
        text=render(state,proc);names=sorted(owned_paths)
        science_raw=None if proc is None else compact(proc)
        capacity,blobs=topic_tree_metadata(git,TOPIC,PUBLIC)
        state["publication_owned_HEAD_delta"]=owned_head_delta(git,root,capacity,blobs,owned_paths)
        total=capacity["blob_bytes"];oldbytes=sum(blobs[name]["bytes"] for name in names if name in blobs)
        state.update(publication_capacity_metadata=capacity,publication_base_topic_blob_bytes=total,
            publication_capacity_metadata_commit=capacity["commit"],projected_topic_blob_bytes=0)
        while True:
            raw=compact(state)
            projected=total-oldbytes+len(text.encode())+len(raw)+(0 if science_raw is None else len(science_raw))
            if projected==state["projected_topic_blob_bytes"]:
                break
            state["projected_topic_blob_bytes"]=projected
        if projected>=200000000:
            raise ValueError("the actual complete small conclusions exceed topic capacity")
        if len(raw)>59000 or len(text.encode())>12000 or (science_raw is not None and len(science_raw)>40000):
            raise ValueError("full science is already preserved in stdout; one publication small-text gate failed")
        (report/"actual-result.md").write_text(text)
        (report/"execution.json").write_bytes(raw)
        if science_raw is not None:
            (report/"actual-scientific-conclusion.json").write_bytes(science_raw)
    def publish():
        snapshot();owned=str(report.relative_to(root));git("add","--sparse","--",owned)
        if git("diff","--cached","--quiet","--",owned,check=False).returncode!=0:
            git("commit","-m","visible-exact: record complete full-normalizer endpoint scalar bounds")
        while True:
            result=git("push","origin","HEAD:refs/heads/main",check=False)
            if result.returncode==0:
                return owned
            if not any(v in result.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
                raise RuntimeError("small full-normalizer-endpoint conclusion push failed outside concurrent-main rebase")
            sync();snapshot();git("add","--sparse","--",owned);git("commit","--amend","--no-edit")
    publication_retry_start=time.monotonic()
    while True:
        try:
            sync()
            state["metadata_publication_retry_pending"]=False
            owned=publish()
            break
        except TransientMetadataError as error:
            metadata_event(error,False)
            if time.monotonic()-publication_retry_start>600:
                raise
            time.sleep(10)
    print(json.dumps(dict(complete=state["complete"],actual_returncode=state["actual_returncode"],
        report=owned,actual_new_scientific_processes=state["actual_new_scientific_processes"],
        old_successful_mathematics_recomputed=0,new_artifacts=0,new_Releases=0,
        new_numerical_arrays_retained=False)),flush=True)
    if not state["complete"]:
        raise SystemExit(1)


if __name__=="__main__":
    main()
