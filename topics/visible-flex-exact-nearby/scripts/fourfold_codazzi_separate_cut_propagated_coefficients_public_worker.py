#!/usr/bin/env python3
"""Public separate cut and propagated first coefficients from five completed scientific records."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import urllib.error,urllib.request,select,importlib.metadata
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_separate_cut_propagated_coefficients.py"
REPORTS=TOPIC/"notes/separate_cut_propagated_coefficients_ci"
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
    """Reuse only a complete same five-receipt coefficient target, including every finite row."""
    p=proc or {}
    c=p.get("complete_new_cut_and_transported_coefficient_conclusion",{}) or {}
    m=p.get("complete_new_multiplier_conclusion",{}) or {}
    d=p.get("complete_new_dual_row_conclusion",{}) or {}
    f=p.get("complete_new_ordered_coefficient_fee_conclusion",{}) or {}
    saved=p.get("copied_complete_scalar_inputs_read_verbatim",{}) or {}
    ident=p.get("complete_original_receipt_identities",{}) or {}
    tf=p.get("copied_complete_tf_structure",{}) or {}
    scope=p.get("scope",{}) or {}
    signs=p.get("complete_sign_wave_scope",[]) or []
    def enclosure(x):
        return isinstance(x,dict) and isinstance(x.get("ball"),str)
    def triple(x):
        return isinstance(x,list) and len(x)==3 and all(enclosure(v) for v in x)
    arrays=("complete_original_phi_own_coefficient_0_2_upper",
        "complete_cut_coefficient_0_2_upper","complete_propagated_coefficient_0_2_upper",
        "complete_branch_coefficient_0_2_upper")
    fees=("algebra_two_primitive","algebra_two_complete_ranks","algebra_complete",
        "complete_waist_projection_fee","complete_tilde_C_supremum",
        "root_two_primitive_after_one_right_inverse",
        "root_finite_after_one_right_inverse_read_verbatim","complete_principal_two_rank_fee",
        "coefficient_only_common_input_strong_fee")
    expected_old={"fa_science":("43763658978",24),"kl_science":("43766439345",16),
        "wx_execution":("43763424840",20),"tf_science":("43766881076",14),
        "sj_execution":("43768006977",26)}
    scopes=("complete_cut_and_propagated_coefficients_kept_separately",
        "complete_real_family_coefficients_and_full_means_retained",
        "same_terminal_Ai_reference_column_not_a_full_free_basis",
        "no_derivative_inferred_from_a_whole_norm",
        "no_total_upper_subtracted_to_obtain_a_summand",
        "full_physical_4j_Fourier_sums_used",
        "conditional_deviation_candidate_does_not_replace_failed_domain_gate",
        "two_complete_density_primitive_ranks_retained",
        "waist_projection_rank_is_independent_of_FA_and_SJ_primitive_errors",
        "TF_completed_after_right_factors_read_without_second_KF",
        "selected_common_input_only_not_a_family_of_conjugacies",
        "coefficient_only_fee_not_the_complete_state_error",
        "original_low_mean_other_sign_and_finite_border_rows_remain_separate",
        "exact_right_order_Lambda_inverse_TF_inverse_S_inverse_retained",
        "no_state_only_exact_left_angle_cancellation_used",
        "no_new_incoming_inverse_Schur_inverse_or_full_R0_claimed")
    return bool(isinstance(proc,dict)
        and p.get("kind")=="actual_separate_cut_propagated_first_coefficient_budgets_v1"
        and p.get("complete") is True and p.get("proved") is True and p.get("stage")=="complete"
        and p.get("actual_returncode")==0 and p.get("failure") is None
        and p.get("source_sha256")==source and p.get("parameters")==parameters
        and p.get("runtime")==runtime and p.get("arithmetic_bits")==320
        and parameters.get("arithmetic_bits")==320
        and (manifest is None or p.get("input_manifest_sha256")==manifest)
        and p.get("input_sha256")==pins and len(pins)==6
        and len(p.get("gates",[]))==21 and all(g.get("passed") is True for g in p["gates"])
        and p.get("complete_separate_coefficient_budgets_proved") is True
        and p.get("original_completed_scientific_receipts_read")==5
        and p.get("new_cut_leading_inverse_count")==1
        and p.get("new_complete_coefficient_arrays")==3
        and p.get("new_complete_multiplier_window_bounds")==9
        and p.get("new_complete_dual_row_bounds")==3
        and p.get("new_complete_coefficient_only_fee_count")==1
        and set(ident)==set(expected_old)
        and all((ident[k].get("run"),ident[k].get("gates"))==v for k,v in expected_old.items())
        and all(triple(c.get(k)) for k in arrays)
        and enclosure(c.get("complete_cut_leading_inverse_upper"))
        and enclosure(c.get("complete_root_F_A0_read_verbatim"))
        and c.get("complete_root_F_A0_read_verbatim")==saved.get("TF_F_A0")
        and c.get("all_three_arrays_are_complete_scalar_suprema") is True
        and c.get("two_input_signs_have_the_same_exact_real_coefficient_by_WY39_44") is True
        and c.get("original_branch_and_input_sign_normalization_retained") is True
        and c.get("KL_numerator_divided_by_cut_ng_lower_exactly_once") is True
        and c.get("no_saved_waist_KLambda_or_WX_radial_forward_applied") is True
        and c.get("ordinary_SJ_integrals_used_verbatim_without_reintegration") is True
        and c.get("no_difference_of_upper_bounds_used") is True
        and c.get("reference_column")==parameters["reference_column"]
        and c.get("second_reference_column_not_covered") is True
        and triple(saved.get("SJ_complete_cprop_integrals"))
        and triple(saved.get("FA_A1_jets")) and triple(saved.get("FA_inverse_phase_jets"))
        and set(m)=={"cut","propagated","complete"}
        and all(all(enclosure(x.get(k)) for k in ("L2","Hminus1_3","Hminus4_3",
            "complete_direct_Hminus1_3","complete_direct_Hminus4_3","complete_alternative_H2"))
            and x.get("zero_mode_and_scalar_component_convention_retained") is True for x in m.values())
        and all(enclosure(d.get(k)) for k in ("C_I2_L2_to_H4_3_upper",
            "inverse_second_derivative_upper","inverse_displacement_H4_3",
            "inverse_displacement_Linfty","phase_derivative_deviation","complete_IC_H4_3"))
        and d.get("optional_positive_deviation_gate") in (True,False)
        and len(d.get("complete_Linfty_candidates",[]))==(3 if d["optional_positive_deviation_gate"] else 2)
        and all(enclosure(x) for x in d["complete_Linfty_candidates"])
        and ((d["optional_positive_deviation_gate"] and enclosure(d.get("optional_complete_bound")))
            or (not d["optional_positive_deviation_gate"] and d.get("optional_complete_bound") is None))
        and d.get("mean_annihilated_only_by_the_exact_primitive") is True
        and all(enclosure(f.get(k)) for k in fees)
        and f.get("root_finite_after_one_right_inverse_read_verbatim")==saved.get("TF_finite_after_right_inverse")
        and f.get("right_TF_inverse_applied_once") is True
        and f.get("state_only_exact_left_coordinate_cancellation_not_used") is True
        and f.get("full_state_error_other_rows_and_finite_inverse_not_claimed") is True
        and p.get("complete_selected_coefficient_only_Hminus4_3_to_L2_upper")
            ==f.get("coefficient_only_common_input_strong_fee")
        and tf.get("finite_original_input_and_output_support_abs_j")==tf.get("actual_J_F",0)+191
        and tf.get("right_transformed_finite_rows_keep_actual_dual_norms") is True
        and tf.get("right_transformed_finite_input_support_not_claimed") is True
        and (p.get("copied_selected_common_input_scope",{}) or {}).get("exact_order")
            ==parameters["selected_common_input_order"]
        and (p.get("copied_selected_common_input_scope",{}) or {}).get("only_same_selected_actual_conjugacy") is True
        and len(signs)==4
        and [(x.get("physical_wave"),x.get("physical_input_sign")) for x in signs]
            ==[(-1,-1),(-1,1),(1,-1),(1,1)]
        and all(x.get("same_common_bound_applies_without_sum_over_input_signs") is True for x in signs)
        and set(scope)==set(scopes) and all(scope.get(k) is True for k in scopes)
        and p.get("independent_physical_mean_coordinates")==2
        and all(p.get(k)==0 for k in ("old_completed_SJ_integrals_or_FA_KL_WX_TF_targets_recomputed",
            "old_scientific_source_imports","old_binary_native_or_archive_restored"))
        and p.get("original_input_bytes_modified") is False
        and p.get("new_recomputable_arrays_persisted") is False
        and all(p.get(k) is False for k in ("full_incoming_inverse_proved","finite_Schur_inverse_proved",
            "complete_state_error_proved","full_return_R0_proved",
            "actual_nonlinear_background_proved","final_surface_proved")))

def render(state,science):
    s=science or {}
    c=s.get("complete_new_cut_and_transported_coefficient_conclusion",{}) or {}
    m=s.get("complete_new_multiplier_conclusion",{}) or {}
    d=s.get("complete_new_dual_row_conclusion",{}) or {}
    f=s.get("complete_new_ordered_coefficient_fee_conclusion",{}) or {}
    ready=s.get("complete_separate_coefficient_budgets_proved") is True
    lines=["# Actual separate cut and propagated first coefficients","",
      "- Run: "+str(state["run_id"])+"/"+str(state["run_attempt"]),
      "- Actual child return: "+str(state.get("actual_returncode")),
      "- Complete mathematical receipt: "+str(state.get("complete_mathematical_receipt_available",False)),
      "- Source SHA256: "+state["source_sha256"],
      "- Manifest SHA256: "+state["input_manifest_sha256"],
      "- Complete scientific file: [actual-scientific-conclusion.json](actual-scientific-conclusion.json).",
      "- Original completed receipts read: "+str(s.get("original_completed_scientific_receipts_read",0)),
      "- Complete coefficient arrays / multiplier windows / dual rows / final fee: "+
          " / ".join(str(s.get(k,0)) for k in ("new_complete_coefficient_arrays",
          "new_complete_multiplier_window_bounds","new_complete_dual_row_bounds",
          "new_complete_coefficient_only_fee_count")),
      "- Old successful mathematical targets repeated:0.",
      "- Binary inputs, new numerical arrays, Releases and artifacts persisted:0.",""]
    if ready:
        lines+=["## Separate complete angular derivatives","",
          "Each entry bounds the full scalar coefficient including its mean. "
          "The propagated input is the completed SJ ordinary integral, read without reintegration.",
          "","| Coefficient | Angular derivative | Complete upper |","|---|---|---|"]
        for label,key in (("Original own coefficient","complete_original_phi_own_coefficient_0_2_upper"),
            ("Cut","complete_cut_coefficient_0_2_upper"),
            ("Propagated","complete_propagated_coefficient_0_2_upper"),
            ("Complete branch","complete_branch_coefficient_0_2_upper")):
            for q,value in enumerate(c.get(key,[])):
                lines.append("| "+label+" | "+str(q)+" | "+cell(ball(value))+" |")
        lines+=["","- Cut leading inverse, with one cut density division: "+
          cell(ball(c.get("complete_cut_leading_inverse_upper")))+".",
          "- Completed root F_A0, read verbatim: "+cell(ball(c.get("complete_root_F_A0_read_verbatim")))+".",
          "","## Complete multiplier windows","","| Coefficient | Window | Complete upper |","|---|---|---|"]
        for label,row in m.items():
            for window in ("L2","Hminus1_3","Hminus4_3"):
                lines.append("| "+label+" | "+window+" | "+cell(ball(row[window]))+" |")
        lines+=["","## Complete dual rows","","| Quantity | Complete upper |","|---|---|"]
        for label,key in (("Inverse displacement H4/3","inverse_displacement_H4_3"),
            ("Inverse displacement Linfty","inverse_displacement_Linfty"),
            ("Full primitive IC in H4/3","complete_IC_H4_3"),
            ("Phase derivative deviation","phase_derivative_deviation")):
            lines.append("| "+label+" | "+cell(ball(d.get(key)))+" |")
        lines+=["","- Optional strict phase-deviation candidate accepted: "+
          str(d.get("optional_positive_deviation_gate"))+".",
          "","## Ordered coefficient-only fees","","| Quantity | Complete upper |","|---|---|"]
        for label,key in (("Two primitives","algebra_two_primitive"),
            ("Two complete ranks","algebra_two_complete_ranks"),
            ("Complete algebra","algebra_complete"),
            ("Independent waist projection","complete_waist_projection_fee"),
            ("Full tilde coefficient","complete_tilde_C_supremum"),
            ("Root two primitives after one right inverse","root_two_primitive_after_one_right_inverse"),
            ("Root finite map after one right inverse","root_finite_after_one_right_inverse_read_verbatim"),
            ("Selected coordinate two ranks","complete_principal_two_rank_fee"),
            ("Selected coefficient-only Hminus4/3 to L2","coefficient_only_common_input_strong_fee")):
                lines.append("| "+label+" | "+cell(ball(f.get(key)))+" |")
        lines+=["","TF's saved after-right factors are read directly. Only the independent waist-projection "
          "fee receives an additional T_F inverse. The complete h0, h1 and h2 and the original F_A0 "
          "remain independently available for subsequent principal estimates.",""]
    else:
        lines+=["This incomplete receipt does not assert complete coefficient or strong-error fees.",""]
    lines+=["## Completed original identities",""]
    for key,v in (s.get("complete_original_receipt_identities",{}) or {}).items():
        lines+=["- "+key+": run "+str(v.get("run"))+"/1; source "+str(v.get("source"))+
          "; manifest "+str(v.get("manifest"))+"; complete gates "+str(v.get("gates"))+"."]
    lines+=["","## Structural gates",""]
    lines+=["- "+("PASS" if g["passed"] else "FAIL")+": "+g["name"] for g in s.get("gates",[])]
    if state.get("actual_failure"):
        lines+=["","## Actual failure","",json.dumps(state["actual_failure"],ensure_ascii=False,sort_keys=True)]
    lines+=["","## Exact scope","",
      "The coefficient bounds cover the same real family, both physical signs and both wave branches "
      "of the one terminal-Ai reference column. Equality of the two input-sign coefficients does not "
      "delete either sign sector. No second reference column is supplied.",
      "The two complete density ranks, the independent waist projection, both physical means, "
      "the original low and other-sign rows and the transported finite complement remain.",
      "Only the final S and S inverse step uses the already selected true conjugacy. The state-only "
      "exact left-coordinate cancellation is not applied to coefficient terms.",
      "This is a coefficient-only strong fee. The complete state error, complete incoming inverse, "
      "finite Schur inverse, full return remainder and final nonlinear surface are separate obligations.","",
      "## Actual README pulls",""]
    for r in state.get("readme_checks",[]):
        lines.append("- "+r["time"]+" -> "+r["after"]+"; README diff empty: "+str(r["actual_diff"]==""))
    return "\n".join(lines)+"\n"

def emit_prepublication(state,science):
    report=render(state,science)
    science_raw=None if science is None else compact(science)
    payload=dict(marker="SEPARATE_CUT_PROPAGATED_COEFFICIENT_COMPLETE_SCIENTIFIC_PREPUBLICATION_V1",
        source_sha256=state["source_sha256"],manifest_sha256=state["input_manifest_sha256"],
        run_id=state["run_id"],run_attempt=state["run_attempt"],
        actual_returncode=state.get("actual_returncode"),scientific_result=science,report_text=report)
    raw=compact(payload)
    status=dict(marker="SEPARATE_CUT_PROPAGATED_COEFFICIENT_PREPUBLICATION_STATUS",
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
        raise ValueError("full separate-coefficient science is saved and printed; prepublication payload exceeds59000")
    print(raw.decode(),end="",flush=True)
    process=compact(dict(marker="SEPARATE_CUT_PROPAGATED_COEFFICIENT_EXECUTION_PREPUBLICATION_V1",execution=state))
    if len(process)>59000:
        raise ValueError("full separate-coefficient science is preserved; execution metadata exceeds59000")
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
        raise RuntimeError("only this public repository Actions may evaluate new separate-coefficient mathematics")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:
        raise ValueError("the separately pinned separate-coefficient manifest or reviewed rules changed")
    m=read(a.manifest);rules=read(a.rules)
    if (m.get("public_repository")!=PUBLIC or rules.get("repository")!=PUBLIC
        or m.get("kind")!="separate_cut_propagated_first_coefficient_public_inputs_v1"
        or m.get("expected_actual_gate_count")!=21
        or m.get("source_sha256")!=a.pipeline_sha
        or m.get("file_sha256")!={x["path"]:x["sha256"] for x in m["files"]}
        or len(m["files"])!=9 or len(m["file_sha256"])!=9
        or set(m["current_input_paths"])!=set(m["file_sha256"])
        or set(m["input_paths"].values())!=set(m["file_sha256"])
        or m.get("legacy_artifact_inputs")!=[] or m.get("all_inputs_are_current_small_texts") is not True
        or m.get("old_successful_scientific_calls_allowed") is not False
        or m.get("new_native_arrays_or_artifact_persistence_allowed") is not False):
        raise ValueError("the exact new separate-coefficient input contract changed")
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
        raise ValueError("temporary separate-coefficient work and outcome directories are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():
        raise FileExistsError("preserve the previous complete or partial separate-coefficient run")
    if any(v.is_relative_to(root) for v in (work,out)):
        raise ValueError("all new numerical arrays must remain outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__)
    state=dict(kind="actual_public_separate_cut_propagated_coefficients_execution_v1",repository=PUBLIC,
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
            raise ValueError("a pinned separate-coefficient source manifest or rule record changed during pull")
        if sha(root/rw)!=ws:
            raise ValueError("the currently running immutable separate-coefficient wrapper changed")
        for name in m["current_input_paths"]:
            if sha(root/relpath(name))!=m["file_sha256"][name]:
                raise ValueError("an immutable current separate-coefficient source or contract changed")
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
        print(json.dumps(dict(kind="SEPARATE_CUT_PROPAGATED_COEFFICIENT_DEFERRED_READ_ONLY_METADATA_PUBLICATION",**event,
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
            raise ValueError("all nine separate-coefficient inputs must be complete small current text")
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
                raise RuntimeError("same separate cut and propagated coefficient arithmetic has a prior incomplete outcome; require its concrete review and preserved scientific-result review")
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
        if len(inputs)!=9 or len(parsed)!=2:
            raise ValueError("the complete nine-input and two-Python AST closure differs")
        state["old_binary_parts_restored"]=0
        state["old_artifacts_downloaded"]=0
        state["old_producers_or_integrals_reexecuted"]=0
        state["new_artifact_count"]=0;state["new_Release_count"]=0
        cmd=[sys.executable,"-u",str(work/PIPELINE),"--manifest",str(tm),
            "--manifest-sha",a.manifest_sha,"--bits","320",
            "--out",str(out/"actual-scientific-conclusion.json")]
        for role,digest in pins.items():
            if index_files[role]["sha256"]!=digest:
                raise ValueError("one complete separate-coefficient mathematical identity changed")
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
            dict(type="IncompleteScientificReceipt",message="the full twenty-one-gate separate-coefficient receipt did not validate"))
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
        print(json.dumps(dict(kind="SEPARATE_CUT_PROPAGATED_COEFFICIENT_ATOMIC_SCIENCE_REPRINT",
            bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())),flush=True)
        print("SEPARATE_CUT_PROPAGATED_COEFFICIENT_SCIENTIFIC_RESULT_BEGIN",flush=True)
        print(raw.decode(),end="",flush=True)
        print("SEPARATE_CUT_PROPAGATED_COEFFICIENT_SCIENTIFIC_RESULT_END",flush=True)
        state["complete_atomic_scientific_result_reprinted"]=True
    outputs=[out/name for name in ("actual-scientific-conclusion.json","new-scientific-child.stdout.log")]
    state["output_hashes"]=[rec(path,out) for path in outputs if path.is_file()]
    if proc is not None:
        original=out/"actual-scientific-conclusion.json"
        if original.read_bytes()!=compact(proc):
            raise ValueError("the complete separate-coefficient child science must retain its original canonical bytes")
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
            git("commit","-m","visible-exact: record complete separate cut and propagated coefficient scalar bounds")
        while True:
            result=git("push","origin","HEAD:refs/heads/main",check=False)
            if result.returncode==0:
                return owned
            if not any(v in result.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
                raise RuntimeError("small separate-coefficient conclusion push failed outside concurrent-main rebase")
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
