#!/usr/bin/env python3
"""Public fourth-angle and global-sign scalar combinations from five completed scientific records."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import urllib.error,urllib.request,select,importlib.metadata
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_fourth_angle_and_Maslov_sign_budgets.py"
REPORTS=TOPIC/"notes/fourth_angle_global_sign_budgets_ci"
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
    """Reuse only the identical complete DZ scalar result, with every unpaid scope preserved."""
    p=proc or {}
    derivatives=p.get("complete_new_fourth_angle_conclusion",{}) or {}
    sign=p.get("complete_new_strong_sign_conclusion",{}) or {}
    common=p.get("complete_new_commonout_paid_conclusion",{}) or {}
    out=p.get("complete_new_standardout_paid_conclusion",{}) or {}
    old=p.get("complete_original_receipt_identities",{}) or {}
    scalars=p.get("copied_complete_scalar_inputs_read_verbatim",{}) or {}
    original_retained=p.get("copied_original_WE_retained_register_read_verbatim",[]) or []
    retained=p.get("retained_row_register",[]) or []
    rows=p.get("complete_two_sign_readout",[]) or []
    candidates=common.get("complete_whole_negative_sign_candidates",[]) or []
    selected=common.get("selected_complete_candidate_index")
    bound=out.get("complete_known_standardout_subtotal_upper")
    flags=("complete_full_Ei_Eo_proved","full_incoming_inverse_proved",
        "finite_Schur_inverse_proved","whole_return_R0_proved",
        "actual_nonlinear_background_proved","final_surface_proved")
    roles={"fa_science","tc_execution","wx_execution","pg_execution","we_science"}
    original_ids={"physical_mean_matching_rows","full_density_mean_identity_difference",
        "transported_original_low_input","root_head_and_two_reference_blocks",
        "opposite_sign_and_Maslov_realization","final_principal_cross_rows"}
    new_ids={"original_WE_remainder","physical_mean_and_transported_low_matching",
        "second_reference_and_remaining_opposite_sign_blocks",
        "incoming_inverse_and_complete_ratio_error","second_global_Cayley_sign_commutator",
        "actual_finite_Schur_and_return"}
    scalar_keys={"x","y","tminus","tplus","P1","P2","P3","kappa2","kappa3","M","F","G",
        "W1","W2","h1","h2","psi_min","psi2","S0","Sminus","Sinv0","Sinvminus",
        "co_A0","co_B13","Cpaid"}
    derivative_keys={"t1","t2","t3","t4","X4","omega4","P4","kappa4","Hchi",
        "W3","W4","h3","h4","psi3","psi4"}
    def is_ball(x):return isinstance(x,dict) and isinstance(x.get("ball"),str)
    return bool(isinstance(proc,dict)
        and p.get("kind")=="actual_fourth_angle_and_global_sign_budgets_v1"
        and p.get("complete") is True and p.get("proved") is True
        and p.get("actual_returncode")==0 and p.get("failure") is None
        and p.get("source_sha256")==source and p.get("parameters")==parameters
        and p.get("runtime")==runtime and p.get("arithmetic_bits")==320
        and (manifest is None or p.get("input_manifest_sha256")==manifest)
        and p.get("input_sha256")==pins and len(pins)==11
        and len(p.get("gates",[]))==24 and all(g.get("passed") is True for g in p["gates"])
        and all(p.get(k)==0 for k in ("old_successful_scientific_targets_recomputed",
            "old_scientific_source_imports","old_scientific_source_calls",
            "old_binary_native_or_archive_restored","new_ray_or_KAM_calls",
            "new_radial_or_angular_integrals","old_coordinate_or_normalizer_targets_recomputed"))
        and p.get("complete_new_fourth_angle_and_sign_budgets_proved") is True
        and p.get("complete_known_standardout_subtotal_proved") is True
        and p.get("original_completed_scientific_receipts_read")==5 and set(old)==roles
        and all(v.get("source") and v.get("manifest") and v.get("gates",0)>0
            and v.get("attempt")=="1" and v.get("original_file_sha256")==pins[k]
            for k,v in old.items())
        and set(scalars)==scalar_keys and all(is_ball(v) for v in scalars.values())
        and set(p.get("complete_original_consumed_scalar_paths",{}))==scalar_keys
        and p.get("new_higher_derivative_scalar_count")==15
        and set(derivatives.get("new_scalar_upper",{}))==derivative_keys
        and all(is_ball(v) for v in derivatives["new_scalar_upper"].values())
        and derivatives.get("complete_selected_common_input_third_derivative_upper")
            ==derivatives["new_scalar_upper"]["psi3"]
        and derivatives.get("complete_selected_common_input_fourth_derivative_upper")
            ==derivatives["new_scalar_upper"]["psi4"]
        and derivatives.get("saved_P1_P2_P3_and_M_F_G_W1_W2_h1_h2_are_not_recomputed") is True
        and derivatives.get("complete_both_characteristic_branches_and_all_shorter_intervals") is True
        and derivatives.get("only_same_selected_H_in_final_composition") is True
        and derivatives.get("old_complete_holomorphic_strip_used_without_promoting_real_jets") is True
        and derivatives.get("original_lower_T_endpoint_used_in_every_inverse_half_power") is True
        and is_ball(sign.get("complete_D_Hminus4_3_to_L2_upper"))
        and sign.get("exact_D")=="D = Z^S - Z = [S,Z] S_inverse"
        and all(sign.get(k) is True for k in
            ("both_opposite_sign_quadrants_and_commutator_factor_two_included",
             "output_mean_of_density_commutator_is_exactly_zero",
             "nonzero_output_mean_of_root_multiplier_commutator_is_retained",
             "input_mean_rank_is_paid_separately",
             "Pi_S_inverse_equals_Pi_used_only_for_input_mean_rank",
             "no_inverse_factor_on_the_input_mean_rank",
             "independent_physical_mean_coordinates_not_deleted",
             "complete_sign_operator_not_relabelled_finite_rank"))
        and len(candidates)==2 and selected in (0,1)
        and all(is_ball(v) for v in candidates)
        and common.get("complete_ZS_Hminus4_3_whole_upper")==candidates[selected]
        and common.get("complete_ZS_Hminus4_3_product_upper")==candidates[0]
        and common.get("selection_rule")==parameters["whole_negative_sign_selection"]
        and common.get("physical_common_outgoing_order")==parameters["physical_common_outgoing_order"]
        and common.get("individually_normalized_branch_paid_value_read_verbatim")==scalars["Cpaid"]
        and common.get("no_entrywise_minimum_or_unpaid_remainder_zero_substitution") is True
        and common.get("original_Lambda_TF_S_order_not_changed") is True
        and is_ball(bound)
        and out.get("exact_standardout_order")==parameters["standard_outgoing_order"]
        and out.get("exact_error")=="Z_inverse ([Tco,Z] + Tco D + Eo Z^S)"
        and out.get("exact_unpaid_remainder")=="Z_inverse E_ret Z^S"
        and all(out.get(k) is True for k in ("full_co_mean_used_in_Tco_L2",
            "only_constant_coefficient_part_removed_from_exact_commutator",
            "root_commutator_output_scalar_mean_kept",
            "WE_subtotal_already_contains_state_and_CG_once",
            "state_only_coordinate_cancellation_not_reapplied",
            "complete_Estandard_or_actual_incoming_inverse_not_claimed"))
        and out.get("retained_remainder_norm_supplied") is False
        and len(rows)==2 and [r.get("physical_input_sign") for r in rows]==[-1,1]
        and all(r.get("complete_known_standardout_subtotal_upper")==bound
            and r.get("same_complete_operator_bound_not_a_sign_sum") is True for r in rows)
        and all(p.get(k)==1 for k in ("new_complete_strong_sign_bound_count",
            "new_complete_commonout_paid_bound_count","new_complete_paid_commutator_bound_count",
            "new_complete_standardout_subtotal_count","new_complete_whole_minimum_count"))
        and p.get("new_sign_record_count")==2
        and len(original_retained)==6 and {r.get("id") for r in original_retained}==original_ids
        and all(r.get("status")=="exact-border-unpaid" and r.get("actual_norm_supplied") is False
            for r in original_retained)
        and len(retained)==6 and {r.get("id") for r in retained}==new_ids
        and all(r.get("status")=="exact-unpaid" and r.get("actual_norm_supplied") is False
            and r.get("operator_is_not_assumed_finite_rank") is True for r in retained)
        and p.get("retained_mode")=="exact-unpaid" and p.get("retained_norm_budget") is None
        and p.get("independent_physical_mean_coordinates")==2
        and p.get("original_input_bytes_modified") is False
        and p.get("new_recomputable_arrays_persisted") is False
        and all(p.get(k) is False for k in flags))

def render(state,science):
    s=science or {};d=s.get("complete_new_fourth_angle_conclusion",{}) or {}
    sg=s.get("complete_new_strong_sign_conclusion",{}) or {}
    co=s.get("complete_new_commonout_paid_conclusion",{}) or {}
    std=s.get("complete_new_standardout_paid_conclusion",{}) or {}
    ready=s.get("complete_known_standardout_subtotal_proved") is True
    lines=["# Actual fourth-angle and global-sign scalar bounds","",
      "- Run: "+str(state["run_id"])+"/"+str(state["run_attempt"]),
      "- Actual child return: "+str(state.get("actual_returncode")),
      "- Complete mathematical receipt: "+str(state.get("complete_mathematical_receipt_available",False)),
      "- Source SHA256: "+state["source_sha256"],
      "- Manifest SHA256: "+state["input_manifest_sha256"],
      "- Complete scientific file: [actual-scientific-conclusion.json](actual-scientific-conclusion.json).",
      "- Original-record complete-audit counter: "+str(s.get("original_completed_scientific_receipts_read",0))+" (assigned only after every input gate).",
      "- Old rays, KAM, integrals, coordinates, normalizers or scientific sources reevaluated: 0.",
      "- Original binaries or archives restored; new arrays, Releases or artifacts persisted: 0.",""]
    if ready:
        lines+=["## New complete derivative combinations","",
          "These are new positive combinations of saved FA, TC and WX values. The original lower-order "
          "phase and flow bounds remain verbatim in the complete scientific file.","",
          "| Quantity | Complete enclosure |","|---|---|"]
        for key,value in (d.get("new_scalar_upper",{}) or {}).items():
            lines.append("| "+key+" | "+cell(ball(value))+" |")
        lines+=["","## Complete sign difference and ordered paid terms","",
          "| Quantity | Complete enclosure |","|---|---|"]
        for name,key,obj in (
          ("Three-IBP coefficient C3","complete_three_IBP_coefficient_upper",sg),
          ("Nonmean Hilbert-Schmidt contribution","complete_root_nonmean_Hilbert_Schmidt_upper",sg),
          ("Independent input-mean rank","complete_input_mean_rank_upper",sg),
          ("Full D = Z^S - Z strong bound","complete_D_Hminus4_3_to_L2_upper",sg),
          ("Z^S on L2","complete_ZS_L2_upper",co),
          ("Z^S negative-window product","complete_ZS_Hminus4_3_product_upper",co),
          ("Selected complete negative-window bound","complete_ZS_Hminus4_3_whole_upper",co),
          ("Original MS paid commonout product","complete_original_MS_commonout_paid_upper",co),
          ("Paid commutator","complete_paid_commutator_upper",co),
          ("Root coefficient commutator","complete_root_coefficient_sign_commutator_upper",std),
          ("Full T_co on L2","complete_full_Tco_L2_upper",std),
          ("Full T_co D","complete_Tco_D_strong_upper",std),
          ("Paid E_o Z^S","complete_paid_ZS_strong_upper",std),
          ("Known standardout subtotal","complete_known_standardout_subtotal_upper",std)):
            lines.append("| "+name+" | "+cell(ball(obj.get(key)))+" |")
        lines+=["","The two complete negative-window candidates, in their fixed order, are:"]
        for index,value in enumerate(co.get("complete_whole_negative_sign_candidates",[])):
            lines.append("- Candidate "+str(index)+": "+ball(value)+".")
        lines+=["- Selected index: "+str(co.get("selected_complete_candidate_index"))+".",
          "- Selection compares the final saved outward endpoints; the first candidate wins ties.","",
          "The input-mean rank uses Pi S_inverse = Pi and is not multiplied by the negative-window inverse. "
          "The full scalar mean of c_o remains in the T_co bound. Its constant part alone commutes with "
          "the root sign; the root commutator still retains its output mean.","",
          "The physical common-input outgoing order is U_R B_minus Z^S. The standard form is "
          "Z U_R (T_co + E_standard). Its displayed known subtotal is the sum of the root commutator, "
          "T_co D and the already paid E_o part times one complete sign bound. This does not move Lambda "
          "through S or repeat TF, state or CG fees.","",
          "Both input signs share the same complete operator bound. No second sign sum or uncharged "
          "two-wave pair norm is asserted.",""]
    else:
        lines+=["No complete new fourth-angle or global-sign conclusion is asserted by this incomplete receipt.",""]
    lines+=["## Complete original identities",""]
    for key,v in (s.get("complete_original_receipt_identities",{}) or {}).items():
        lines.append("- "+key+": run "+str(v.get("run"))+"/"+str(v.get("attempt"))+
            "; original file SHA256 "+str(v.get("original_file_sha256"))+
            "; all "+str(v.get("gates"))+" original gates retained.")
    lines+=["","## Exact unpaid remainder",""]
    if s.get("copied_original_WE_retained_register_read_verbatim"):
        lines+=["The complete original six-row WE register is preserved verbatim in the scientific file. "
          "The following current obligations are not assigned a numerical norm or finite-rank status:",""]
    else:
        lines+=["The input audit stopped before the complete WE register was copied. Its original "
          "unpaid obligations remain in the pinned WE record; none is assigned a zero norm here.",""]
    for row in s.get("retained_row_register",[]):
        lines.append("- "+row["id"]+": "+row["formula"]+".")
    lines+=["","## Structural gates",""]
    lines+=["- "+("PASS" if g["passed"] else "FAIL")+": "+g["name"] for g in s.get("gates",[])]
    if state.get("actual_failure"):
        lines+=["","## Actual failure","",json.dumps(state["actual_failure"],ensure_ascii=False,sort_keys=True)]
    lines+=["","## Exact scope",""]
    if ready:
        lines+=["This is a known strong-error subtotal on the same selected S and terminal-Ai reference. "
          "The complete infinite sign difference is bounded, but this does not pay every remaining "
          "opposite-sign or second-reference block. Both physical matching means, transported low input, "
          "complete incoming error and inverse, the second global Cayley sign commutator and the actual "
          "finite Schur inverse remain explicit. Full E_i/E_o, whole return R0, a nonlinear background "
          "and a final surface are not asserted.",""]
    else:
        lines+=["This incomplete run proves no complete new sign bound or standardout subtotal. "
          "Only the recorded completed gates and saved partial fields apply. All original unpaid "
          "operator, physical mean, finite-column and incoming/Schur obligations remain unpaid.",""]
    lines+=["## Actual README pulls",""]
    for r in state.get("readme_checks",[]):
        lines.append("- "+r["time"]+" -> "+r["after"]+"; README diff empty: "+str(r["actual_diff"]==""))
    return "\n".join(lines)+"\n"

def emit_prepublication(state,science):
    report=render(state,science)
    science_raw=None if science is None else compact(science)
    payload=dict(marker="FOURTH_ANGLE_GLOBAL_SIGN_COMPLETE_SCIENTIFIC_PREPUBLICATION_V1",
        source_sha256=state["source_sha256"],manifest_sha256=state["input_manifest_sha256"],
        run_id=state["run_id"],run_attempt=state["run_attempt"],
        actual_returncode=state.get("actual_returncode"),scientific_result=science,report_text=report)
    raw=compact(payload)
    status=dict(marker="FOURTH_ANGLE_GLOBAL_SIGN_PREPUBLICATION_STATUS",
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
        raise ValueError("full fourth-angle-global-sign science is saved and printed; prepublication payload exceeds59000")
    print(raw.decode(),end="",flush=True)
    process=compact(dict(marker="FOURTH_ANGLE_GLOBAL_SIGN_EXECUTION_PREPUBLICATION_V1",execution=state))
    if len(process)>59000:
        raise ValueError("full fourth-angle-global-sign science is preserved; execution metadata exceeds59000")
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
        raise RuntimeError("only this public repository Actions may evaluate new fourth-angle-global-sign mathematics")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:
        raise ValueError("the separately pinned fourth-angle-global-sign manifest or reviewed rules changed")
    m=read(a.manifest);rules=read(a.rules)
    if (m.get("public_repository")!=PUBLIC or rules.get("repository")!=PUBLIC
        or m.get("kind")!="fourth_angle_and_global_sign_public_inputs_v1"
        or m.get("expected_actual_gate_count")!=24
        or m.get("source_sha256")!=a.pipeline_sha
        or m.get("file_sha256")!={x["path"]:x["sha256"] for x in m["files"]}
        or len(m["files"])!=14 or len(m["file_sha256"])!=14
        or set(m["current_input_paths"])!=set(m["file_sha256"])
        or set(m["input_paths"].values())!=set(m["file_sha256"])
        or m.get("legacy_artifact_inputs")!=[] or m.get("all_inputs_are_current_small_texts") is not True
        or m.get("old_successful_scientific_calls_allowed") is not False
        or m.get("new_native_arrays_or_artifact_persistence_allowed") is not False):
        raise ValueError("the exact new fourth-angle-global-sign input contract changed")
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
        raise ValueError("temporary fourth-angle-global-sign work and outcome directories are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():
        raise FileExistsError("preserve the previous complete or partial fourth-angle-global-sign run")
    if any(v.is_relative_to(root) for v in (work,out)):
        raise ValueError("all new numerical arrays must remain outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__)
    state=dict(kind="actual_public_fourth_angle_global_sign_execution_v1",repository=PUBLIC,
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
            raise ValueError("a pinned fourth-angle-global-sign source manifest or rule record changed during pull")
        if sha(root/rw)!=ws:
            raise ValueError("the currently running immutable fourth-angle-global-sign wrapper changed")
        for name in m["current_input_paths"]:
            if sha(root/relpath(name))!=m["file_sha256"][name]:
                raise ValueError("an immutable current fourth-angle-global-sign source or contract changed")
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
        print(json.dumps(dict(kind="FOURTH_ANGLE_GLOBAL_SIGN_DEFERRED_READ_ONLY_METADATA_PUBLICATION",**event,
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
            raise ValueError("all fourteen fourth-angle-global-sign inputs must be complete small current text")
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
                raise RuntimeError("same fourth-angle global-sign arithmetic has a prior incomplete outcome; require its concrete review and preserved scientific-result review")
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
        if len(inputs)!=14 or len(parsed)!=4:
            raise ValueError("the complete fourteen-input and four-Python AST closure differs")
        state["old_binary_parts_restored"]=0
        state["old_artifacts_downloaded"]=0
        state["old_producers_or_integrals_reexecuted"]=0
        state["new_artifact_count"]=0;state["new_Release_count"]=0
        cmd=[sys.executable,"-u",str(work/PIPELINE),"--manifest",str(tm),
            "--manifest-sha",a.manifest_sha,"--bits","320",
            "--out",str(out/"actual-scientific-conclusion.json")]
        for role,digest in pins.items():
            if index_files[role]["sha256"]!=digest:
                raise ValueError("one complete fourth-angle-global-sign mathematical identity changed")
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
            dict(type="IncompleteScientificReceipt",message="the full twenty-four-gate fourth-angle-global-sign receipt did not validate"))
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
        print(json.dumps(dict(kind="FOURTH_ANGLE_GLOBAL_SIGN_ATOMIC_SCIENCE_REPRINT",
            bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())),flush=True)
        print("FOURTH_ANGLE_GLOBAL_SIGN_SCIENTIFIC_RESULT_BEGIN",flush=True)
        print(raw.decode(),end="",flush=True)
        print("FOURTH_ANGLE_GLOBAL_SIGN_SCIENTIFIC_RESULT_END",flush=True)
        state["complete_atomic_scientific_result_reprinted"]=True
    outputs=[out/name for name in ("actual-scientific-conclusion.json","new-scientific-child.stdout.log")]
    state["output_hashes"]=[rec(path,out) for path in outputs if path.is_file()]
    if proc is not None:
        original=out/"actual-scientific-conclusion.json"
        if original.read_bytes()!=compact(proc):
            raise ValueError("the complete fourth-angle-global-sign child science must retain its original canonical bytes")
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
            git("commit","-m","visible-exact: record complete fourth-angle global-sign scalar bounds")
        while True:
            result=git("push","origin","HEAD:refs/heads/main",check=False)
            if result.returncode==0:
                return owned
            if not any(v in result.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
                raise RuntimeError("small fourth-angle-global-sign conclusion push failed outside concurrent-main rebase")
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
