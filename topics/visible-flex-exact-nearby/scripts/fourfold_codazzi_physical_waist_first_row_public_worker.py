#!/usr/bin/env python3
"""Run one new complete physical-waist first-row scalar readout from immutable small successes."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import urllib.error,urllib.request,select,importlib.metadata
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_physical_waist_first_row_receiver.py"
REPORTS=TOPIC/"notes/physical_waist_first_row_receiver_ci"
HISTORICAL=[]
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
            limit=75000 if Path(name).name=="actual-scientific-conclusion.json" else 60000
            if len(body)>limit:raise ValueError("an owned HEAD conclusion exceeds its exact small-text limit")
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

PUBLICATION_LIMITS=json.loads("{\"complete_science_bytes\":75000,\"complete_science_target_bytes\":35000,\"complete_report_bytes\":8000,\"complete_prepublication_science_report_payload_bytes\":90000,\"complete_execution_bytes\":59000,\"pre_science_topic_reserve_bytes\":150000,\"scientific_file_atomic_and_complete_stdout_before_size_guards\":true,\"new_artifacts\":0,\"new_Releases\":0}")
SCIENCE_FIELDS=json.loads("[\"kind\",\"complete\",\"proved\",\"stage\",\"failure\",\"source_sha256\",\"input_manifest_sha256\",\"input_sha256\",\"verified_original_inputs\",\"parameters\",\"runtime\",\"arithmetic_bits\",\"public_repository\",\"run_id\",\"run_attempt\",\"workflow_event_commit\",\"actual_scientific_checkout_commit\",\"actual_returncode\",\"gates\",\"actual_progress\",\"accepted_old_receipts\",\"copied_original_scalar_records\",\"copied_complete_original_scopes\",\"complete_new_first_row_gain_conclusion\",\"complete_new_whole_row_candidate_conclusion\",\"complete_whole_row_selection\",\"original_scalar14_canonical_sha256\",\"original_scope9_canonical_sha256\",\"scope\",\"actual_mathematical_wall_seconds\",\"old_successful_targets_recomputed\",\"new_reproducible_arrays_persisted\"]")
SCIENCE_GATE_NAMES=json.loads("[\"public runtime and exact 320-bit arithmetic with actual workflow and checkout identities\",\"four exact current mathematical texts and their complete manifest closure are frozen\",\"only bounded current UTF8 JSON proof and source texts are read with no archive or old import\",\"original ST execution and its complete embedded science retain all 25 original gates\",\"original SW complete science retains its distinct 24-gate schema and same successful target\",\"same repaired real family cut selected parameter root input and original normalizer remain typed\",\"saved complete reverse matrix contains both means and every shorter ordered source insertion\",\"original positive algorithm and exact row proof are only read with true radial endpoint and source directions\",\"SW separately saved primitive full Q mean and all interfaces refer to the same complete compressed trial\",\"fourteen entire old scalar records and nine whole scope objects are copied literally with finite positive budgets\",\"four new first-row scalar records retain cut density and separate ungauged primitive mean source units\",\"the complete new candidate sums all four physical contributions PC ST4 and the one saved waist correction\",\"only final serialized complete same-row uppers are compared with the old complete record retained on a tie\",\"all fourteen old balls nine scopes and all independent physical obligations remain unchanged\",\"every old mathematical byte and the actual manifest still have their original exact hashes\",\"all sixteen gates nine new scalar records and the complete 32-field small schema retain their declared scope\"]")
SCIENCE_PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"exact_complete_radial_interval\":[\"0\",\"76285779072683/320000000000000\"],\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"input_cutoff_abs_j\":97,\"exact_moving_normalizer_cutoff_abs_j\":268435456,\"physical_frequency\":\"n=4|j|\",\"selected_parameter_absolute_upper\":\"0.00000000009368259853002\",\"reference_column\":\"same terminal Ai free P8 first column\",\"exact_row\":\"B_partial Q_R (Y_A - Y_WJ)\",\"exact_row_input\":\"same reflected natural root H^(-4/3) with |j|>=97\",\"exact_row_output\":\"raw moving-angle even meanzero L2 primitive row\",\"same_trial\":\"single W=A(1+M_C I)Lc and original compressed TJ\",\"same_cut_density_error\":\"original full-T cut difference from SW/UT\",\"ordinary_source\":\"(P[T DW-Q W], -Zy T W), ungauged primitive and complete mean\",\"complete_source_rows\":3071,\"complete_interface_rows\":3070,\"genuine_interface_rows\":2549,\"conservative_interface_rows\":521,\"independent_physical_mean_coordinates\":2,\"old_ST_gate_count\":25,\"old_SW_gate_count\":24,\"saved_original_scalar_record_count\":14,\"copied_complete_scope_object_count\":9,\"new_gain_scalar_count\":4,\"new_contribution_scalar_count\":5,\"expected_actual_gate_count\":16,\"whole_selection\":\"final serialized complete upper endpoints; old candidate wins ties\",\"old_successful_scientific_calls_allowed\":0,\"signed_adjoint_cancellation_numerically_certified\":false,\"full_incoming_or_finite_Schur_or_return_R0_claimed\":false}")
SCIENCE_SCOPE=json.loads("{\"same_complete_reflected_primitive_waist_row\":true,\"same_selected_parameter_and_original_terminal_Ai_column\":true,\"same_single_W_and_same_compressed_TJ_trial\":true,\"input_window\":\"same reflected natural root H^(-4/3), original |j|>=97\",\"output_window\":\"raw moving-angle even meanzero L2 primitive row\",\"complete_mean_source_and_both_physical_mean_coordinates_retained\":true,\"raw_h1_mean_redundancy_does_not_delete_even_mean_or_amplitude\":true,\"all_3070_interfaces_without_length_factor_retained\":true,\"PC_ST4_cut_and_saved_waist_FT_each_retained_once\":true,\"old_ST_and_SW_successes_read_only\":true,\"old_scientific_imports_calls_native_restoration_and_new_grids\":0,\"whole_selection_same_object_and_same_output_units_only\":true,\"signed_adjoint_cancellation_numerically_certified\":false,\"raw_L2_derivative_readout_proved\":false,\"physical_leading_row_square_inverse_proved\":false,\"full_incoming_inverse_proved\":false,\"finite_Schur_inverse_proved\":false,\"whole_return_R0_proved\":false,\"actual_nonlinear_background_proved\":false,\"final_surface_proved\":false,\"independent_even_mean_amplitude_nu_head_and_other_ports_retained\":true}")
SUCCESS_ACTUAL_PROGRESS=json.loads("{\"completed_old_receipts_read\":2,\"completed_old_scalar_records_copied\":14,\"completed_old_scope_objects_copied\":9,\"entered_new_scalar_stage\":true,\"complete_first_row_gain_graph_count\":1,\"new_gain_scalar_records_saved\":4,\"complete_whole_candidate_graph_count\":1,\"new_contribution_scalar_records_saved\":5,\"complete_whole_selection_count\":1,\"actual_old_source_calls\":0,\"actual_old_scientific_targets_recomputed\":0,\"final_readonly_input_check_count\":5}")
SCIENCE_PIN_SHA256=json.loads("{\"contract\":\"0a92e2e5e5c1f0e1e93bc509ad5883d20630ad9909be3b33eaff7546f641702a\",\"st_execution\":\"b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637\",\"sw_science\":\"f16a1dc6177ef8a76d34e859fa37a51461a6ed142f20714e3dcb9212a3647659\",\"st_source\":\"743e4318ca0cbdf57afde3a188013a64c2bacba0958c31fde3b42fcf8a7aa7d5\"}")
SCIENCE_PIN_BYTES=json.loads("{\"contract\":28366,\"st_execution\":47282,\"sw_science\":27687,\"st_source\":50111}")
SCIENTIFIC_GRAPH_SHAPES=json.loads("{\"complete_new_first_row_gain_conclusion\":{\"complete_first_matrix_row_L2_upper\":{\"ball\":\"__FINITE_SCALAR__\"},\"complete_density_cut_row_gain_upper\":{\"ball\":\"__FINITE_SCALAR__\"},\"complete_ungauged_primitive_row_gain_upper\":{\"ball\":\"__FINITE_SCALAR__\"},\"complete_ungauged_mean_row_gain_upper\":{\"ball\":\"__FINITE_SCALAR__\"},\"uses_complete_saved_first_row_not_whole_Frobenius\":true,\"all_shorter_insertions_from_original_positive_algorithm\":true,\"waist_output_and_cut_input_factors_in_true_directions\":true,\"full_mean_source_not_removed\":true,\"physical_frequency_and_ordinary_measure_retained\":true},\"complete_new_whole_row_candidate_conclusion\":{\"complete_cut_contribution_upper\":{\"ball\":\"__FINITE_SCALAR__\"},\"complete_primitive_source_contribution_upper\":{\"ball\":\"__FINITE_SCALAR__\"},\"complete_independent_mean_source_contribution_upper\":{\"ball\":\"__FINITE_SCALAR__\"},\"complete_all_3070_interface_contribution_upper\":{\"ball\":\"__FINITE_SCALAR__\"},\"complete_first_row_candidate_upper\":{\"ball\":\"__FINITE_SCALAR__\"},\"PC_ST4_and_waist_FT_retained_verbatim_once\":true,\"primitive_source_uses_both_complete_leading_and_Q_parts\":true,\"same_original_single_W_and_compressed_TJ_trial\":true,\"interfaces_have_no_radial_length_factor\":true,\"no_new_source_integral_or_positive_product\":true,\"source_gain_already_contains_waist_output_factor\":true,\"saved_waist_FT_correction_not_multiplied_by_ng_again\":true}}")
ACCEPTED_OLD_RECEIPTS=json.loads("{\"st_execution\":{\"execution_kind\":\"actual_public_strict_tail_true_cut_to_waist_execution\",\"scientific_kind\":\"actual_complete_strict_tail_true_branch_cut_to_waist_v1\",\"run_id\":\"43757644616\",\"run_attempt\":\"1\",\"source_sha256\":\"743e4318ca0cbdf57afde3a188013a64c2bacba0958c31fde3b42fcf8a7aa7d5\",\"input_manifest_sha256\":\"e43b2c7036088cd8d1401c580c1aa6ef694d283057dcce7c65839f92fc1b0e80\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"gates\":25,\"complete\":true,\"proved\":true,\"actual_returncode\":0,\"input_sha256\":\"b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637\"},\"sw_science\":{\"scientific_kind\":\"actual_single_complete_root_first_symbol_trial_v1\",\"run_id\":\"43781399696\",\"run_attempt\":\"1\",\"source_sha256\":\"d0380618d0e57fe4771ad0fb5b6a92990225abc9c6f2f379959653eab4e93fb9\",\"input_manifest_sha256\":\"5d62a5e758cd11d4325d1797666bb57683ee94f79e4d4fb4351c33b7f94d78e4\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"gates\":24,\"complete\":true,\"proved\":true,\"actual_returncode\":0,\"input_sha256\":\"f16a1dc6177ef8a76d34e859fa37a51461a6ed142f20714e3dcb9212a3647659\"}}")
FROZEN_SCALAR14_SHA256="070b718bed4a386dea25f0570c17a8573e8d1f33befea4edb81db9ebf0d4dc66"
FROZEN_SCOPE9_SHA256="fa01be532e31dc611aaf858b505115afb2596120f54de30de59ddb4b537ddec7"

def scientific_receipt_valid(proc,source,manifest,parameters,pins,runtime):
    """Validate the whole new receipt without recomputing any scientific scalar."""
    if not isinstance(proc,dict):
        return False
    p=proc
    def hexid(value,size):
        return isinstance(value,str) and len(value)==size and all(x in "0123456789abcdef" for x in value)
    def scalar(value):
        return isinstance(value,str) and 0<len(value)<=256 and not any(x in value.lower() for x in ("nan","inf"))
    def shape(value,expected):
        if expected=="__FINITE_SCALAR__":
            return scalar(value)
        if isinstance(expected,dict):
            return (isinstance(value,dict) and set(value)==set(expected)
                and all(shape(value[k],v) for k,v in expected.items()))
        if isinstance(expected,list):
            return (isinstance(value,list) and len(value)==len(expected)
                and all(shape(a,b) for a,b in zip(value,expected)))
        return type(value) is type(expected) and value==expected
    try:
        if not (set(p)==set(SCIENCE_FIELDS) and len(p)==32
            and p["kind"]=="actual_complete_physical_waist_first_row_receiver_v1"
            and p["complete"] is True and p["proved"] is True
            and p["actual_returncode"]==0 and p["failure"] is None and p["stage"]=="complete"
            and p["source_sha256"]==source and hexid(source,64)
            and p["public_repository"]==PUBLIC
            and isinstance(p["run_id"],str) and p["run_id"].isdigit()
            and isinstance(p["run_attempt"],str) and p["run_attempt"].isdigit()
            and hexid(p["actual_scientific_checkout_commit"],40)
            and hexid(p["workflow_event_commit"],40)
            and p["runtime"]==runtime and p["arithmetic_bits"]==320
            and parameters==SCIENCE_PARAMETERS and p["parameters"]==parameters
            and pins==SCIENCE_PIN_SHA256
            and hexid(p["input_manifest_sha256"],64)
            and (manifest is None or p["input_manifest_sha256"]==manifest)
            and p["input_sha256"]==dict(manifest=p["input_manifest_sha256"],**pins)
            and p["verified_original_inputs"]=={k:dict(bytes=SCIENCE_PIN_BYTES[k],sha256=v) for k,v in pins.items()}
            and p["scope"]==SCIENCE_SCOPE
            and p["actual_progress"]==SUCCESS_ACTUAL_PROGRESS
            and p["accepted_old_receipts"]==ACCEPTED_OLD_RECEIPTS
            and p["old_successful_targets_recomputed"]==0
            and p["new_reproducible_arrays_persisted"] is False
            and isinstance(p["gates"],list) and len(p["gates"])==16
            and [v["name"] for v in p["gates"]]==SCIENCE_GATE_NAMES
            and all(set(v)=={"name","passed"} and v["passed"] is True for v in p["gates"])
            and type(p["actual_mathematical_wall_seconds"]) in (int,float)
            and 0<=p["actual_mathematical_wall_seconds"]<900):
            return False
        scalars=p["copied_original_scalar_records"]
        scopes=p["copied_complete_original_scopes"]
        if not (len(scalars)==14 and len(scopes)==9
            and p["original_scalar14_canonical_sha256"]==FROZEN_SCALAR14_SHA256
            and p["original_scope9_canonical_sha256"]==FROZEN_SCOPE9_SHA256
            and hashlib.sha256(compact(scalars)).hexdigest()==FROZEN_SCALAR14_SHA256
            and hashlib.sha256(compact(scopes)).hexdigest()==FROZEN_SCOPE9_SHA256):
            return False
        if not all(shape(p[key],expected) for key,expected in SCIENTIFIC_GRAPH_SHAPES.items()):
            return False
        selected=p["complete_whole_row_selection"]
        index=selected["selected_index"]
        rows=[
            dict(label="saved_old_complete_Cstar",upper=scalars["Cold"]),
            dict(label="new_complete_first_row_candidate",
                 upper=p["complete_new_whole_row_candidate_conclusion"]["complete_first_row_candidate_upper"])]
        if type(index) is not int or index not in (0,1):
            return False
        expected=dict(comparison="whole saved old Cstar and complete new first-row candidate",
            complete_candidates=rows,selected_index=index,selected_label=rows[index]["label"],
            complete_selected_row_upper=rows[index]["upper"],
            new_candidate_upper_strictly_smaller=(index==1),old_candidate_wins_ties=True,
            entrywise_minimum_used=False,different_trial_or_different_output_unit_minimum_used=False)
        return selected==expected
    except (KeyError,TypeError,ValueError):
        return False

def render(state,science):
    s=science or {}
    failed=state.get("actual_failure") is not None or s.get("failure") is not None
    lines=[
        "# Actual complete physical waist first-row receiver",
        "",
        "This is the complete new scalar readout for WAD.32--36. The old ST and SW successes are immutable inputs.",
        "It retains the original natural-root H^(-4/3) input and raw moving-angle even meanzero L2 primitive output.",
        "",
        "## Actual execution",
        "",
        "| Item | Recorded value |",
        "|---|---|",
        "| Public run / attempt | "+cell(state["run_id"])+"/"+cell(state["run_attempt"])+" |",
        "| Workflow event commit | "+cell(state["workflow_commit"])+" |",
        "| Actual scientific checkout | "+cell(state.get("actual_scientific_checkout_commit","not launched"))+" |",
        "| Scientific source SHA256 | "+cell(state["source_sha256"])+" |",
        "| Manifest SHA256 | "+cell(state["input_manifest_sha256"])+" |",
        "| Complete scientific receipt | "+cell(state.get("complete_mathematical_receipt_available",False))+" |",
        "| Actual return code | "+cell(state.get("actual_returncode"))+" |",
        "| New scientific child processes | "+cell(state["actual_new_scientific_processes"])+" |",
        "| Original ST / SW successes | 43757644616/1 and 43781399696/1 |",
        "| Gates passed / recorded | "+str(sum(g.get("passed") is True for g in s.get("gates",[])))+"/"+str(len(s.get("gates",[])))+" |",
        "",
        "## Complete new scalar records",
        "",
        "| Whole scalar | Outward record |",
        "|---|---|"]
    if failed:
        lines+=["",
            "Every completed scalar and candidate is retained in actual-scientific-conclusion.json when that file exists. The full diagnostic appears below; execution.json records whether a scientific child and result existed."]
    else:
        for key in ("complete_new_first_row_gain_conclusion","complete_new_whole_row_candidate_conclusion"):
            graph=s.get(key) or {}
            for name,value in graph.items():
                if isinstance(value,dict) and set(value)=={"ball"}:
                    lines.append("| "+cell(name)+" | "+cell(value["ball"])+" |")
    selected=s.get("complete_whole_row_selection") or {}
    lines+=["",
        "## Whole-row selection",
        "",
        "| Candidate | Complete outward record |",
        "|---|---|"]
    if not failed:
        for row in selected.get("complete_candidates",[]):
            lines.append("| "+cell(row["label"])+" | "+cell(ball(row["upper"]))+" |")
    lines+=["",
        "Selected complete record: "+cell(selected.get("selected_label","no complete selection"))+".",
        "",
        "## Retained scope",
        "",
        "All PC, ST4, original cut, ordinary leading and full Q sources, independent mean, all 3070 interfaces, and the saved waist FT correction are retained exactly once. Interface terms have no radial length factor.",
        "The scientific schema covers fourteen original scalar records, nine complete original scopes, three new graphs and sixteen gates. Every stage actually completed is retained without truncation; the actual progress and complete/proved flags determine success.",
        "The first matrix row comes from the saved complete positive reverse algorithm. No old matrix product, source integral, exponential, trial, native enclosure or numerical graph is rerun.",
        "The comparison selects one entire final serialized upper record, with the old candidate retained on a tie. It does not splice favorable contributions.",
        "This readout has the original raw primitive-row units. It does not on its own prove a signed adjoint cancellation, WPL's differently normalized error, a usable high-frequency gate, a finite/mean/nu inverse, a nonlinear background or the final surface.",
        "",
        "Available scientific hashes are in execution.json. Available scientific output and this report are printed before Git publication, with an independent execution prepublication receipt.",
        "Current-tree capacity and both README reviews are recorded after real git pull --rebase operations. No new reproducible array, artifact or Release is published.",
        ""]
    if state.get("actual_failure") is not None or s.get("failure") is not None:
        wf=state.get("actual_failure");sf=s.get("failure")
        lines+=["## Actual incomplete outcome",""]
        if wf==sf:
            lines+=["Same complete worker/science failure: "+cell(json.dumps(sf,sort_keys=True,ensure_ascii=False))]
        else:
            lines+=["Worker: "+cell(json.dumps(wf,sort_keys=True,ensure_ascii=False)),
                    "Science: "+cell(json.dumps(sf,sort_keys=True,ensure_ascii=False))]
        lines+=["Every completed scientific stage remains in the full science record. An incomplete run is not permission to recompute completed stages.",""]
    return "\n".join(lines)

def emit_prepublication(state,science):
    report=render(state,science)
    science_raw=None if science is None else compact(science)
    payload=dict(marker="PHYSICAL_WAIST_FIRST_ROW_COMPLETE_SCIENTIFIC_PREPUBLICATION_V1",
        source_sha256=state["source_sha256"],manifest_sha256=state["input_manifest_sha256"],
        run_id=state["run_id"],run_attempt=state["run_attempt"],
        actual_returncode=state.get("actual_returncode"),scientific_result=science,report_text=report)
    raw=compact(payload)
    status=dict(marker="PHYSICAL_WAIST_FIRST_ROW_PREPUBLICATION_STATUS",
        actual_returncode=state.get("actual_returncode"),
        complete_mathematics=state.get("complete_mathematical_receipt_available",False),
        gates_passed=sum(g.get("passed") is True for g in (science or {}).get("gates",[])),
        gates_total=len((science or {}).get("gates",[])),
        science_bytes=None if science_raw is None else len(science_raw),
        science_sha256=None if science_raw is None else hashlib.sha256(science_raw).hexdigest(),
        payload_bytes=len(raw),payload_sha256=hashlib.sha256(raw).hexdigest(),
        failure=None if len(raw)<=90000 else "complete_prepublication_payload_over90000")
    status_raw=compact(status)
    if len(status_raw)>1000:raise ValueError("prepublication status exceeds1000 bytes")
    print(status_raw.decode(),end="",flush=True)
    if len(raw)>90000:
        raise ValueError("full physical-waist-first-row-receiver science is saved and printed; prepublication payload exceeds90000")
    print(raw.decode(),end="",flush=True)
    process=compact(dict(marker="PHYSICAL_WAIST_FIRST_ROW_EXECUTION_PREPUBLICATION_V1",execution=state))
    if len(process)>59000:
        raise ValueError("full physical-waist-first-row-receiver science is preserved; execution metadata exceeds59000")
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
        raise RuntimeError("only this public repository Actions may evaluate new physical-waist-first-row-receiver mathematics")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:
        raise ValueError("the separately pinned physical-waist-first-row-receiver manifest or reviewed rules changed")
    m=read(a.manifest);rules=read(a.rules)
    current=m.get("files",[])
    history=m.get("historical_inputs",[])
    current_roles={v["role"] for v in current}
    current_paths={v["path"] for v in current}
    historical_roles={v["role"] for v in history}
    historical_paths={v["path"] for v in history}
    all_entries=current+history
    if (m.get("public_repository")!=PUBLIC or rules.get("repository")!=PUBLIC
        or m.get("kind")!="complete_physical_waist_first_row_receiver_inputs_v1"
        or m.get("source_sha256")!=a.pipeline_sha
        or m.get("source_path")!=str(PIPELINE)
        or m.get("parameters")!=SCIENCE_PARAMETERS
        or m.get("scope")!=SCIENCE_SCOPE
        or current_roles!=(set(SCIENCE_PIN_SHA256)|{"source","worker","rules"})
        or m.get("complete_input_bytes")!=sum(v["bytes"] for v in current)
        or m.get("publication_limits")!=PUBLICATION_LIMITS
        or m.get("mathematical_input_sha256")!=SCIENCE_PIN_SHA256
        or m.get("expected_actual_gate_count")!=16
        or m.get("expected_current_input_count")!=7
        or m.get("expected_input_count")!=7
        or m.get("expected_immutable_AST_files")!=3
        or history!=HISTORICAL
        or m.get("file_sha256")!={x["path"]:x["sha256"] for x in current}
        or len(current_roles)!=len(current) or len(current_paths)!=len(current)
        or current_roles&historical_roles or current_paths&historical_paths
        or m.get("expected_current_input_count")!=len(current)
        or m.get("expected_input_count")!=len(all_entries)
        or m.get("expected_immutable_AST_files")!=sum(x["path"].endswith(".py") for x in current)
        or set(m.get("current_input_paths",[]))!=current_paths
        or m.get("input_paths")!={x["role"]:x["path"] for x in all_entries}
        or m.get("legacy_artifact_inputs")!=[]
        or m.get("all_inputs_are_current_small_texts") is not True
        or m.get("old_successful_scientific_calls_allowed")!=0
        or m.get("new_native_arrays_or_artifact_persistence_allowed") is not False):
        raise ValueError("the exact seven-current-text physical waist first-row contract changed")
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
        raise ValueError("temporary physical-waist-first-row-receiver work and outcome directories are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():
        raise FileExistsError("preserve the previous complete or partial physical-waist-first-row-receiver run")
    if any(v.is_relative_to(root) for v in (work,out)):
        raise ValueError("all new numerical arrays must remain outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__)
    state=dict(kind="actual_public_physical_waist_first_row_receiver_execution_v1",repository=PUBLIC,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_commit=os.environ["GITHUB_SHA"],worker_source_sha256=ws,
        source_sha256=a.pipeline_sha,input_manifest_sha256=a.manifest_sha,
        reviewed_rules_sha256=a.rules_sha,explicitly_read_rules_commit=rules["read_commit"],
        started_utc=utc(),complete=False,actual_returncode=None,readme_checks=[],
        actual_new_scientific_processes=0,old_numerical_enclosures_recomputed=0,
        old_R97_root_graphs_recomputed=0,old_R97_strict_comparisons_reevaluated=0,
        old_RNE_inverse_polynomials_recomputed=0,old_coordinate_leading_constants_recomputed=0,
        old_exponentials_or_logs_recomputed=0,
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
            raise ValueError("a pinned physical-waist-first-row-receiver source manifest or rule record changed during pull")
        if sha(root/rw)!=ws:
            raise ValueError("the currently running immutable physical-waist-first-row-receiver wrapper changed")
        for name in m["current_input_paths"]:
            if sha(root/relpath(name))!=m["file_sha256"][name]:
                raise ValueError("an immutable current physical-waist-first-row-receiver source or contract changed")
        published,blobs=topic_tree_metadata(git,TOPIC,PUBLIC)
        capacity=owned_head_delta(git,root,published,blobs,owned_paths)
        state.update(current_published_topic_capacity_metadata=published,
            current_topic_capacity_metadata=capacity,current_topic_blob_bytes=capacity["blob_bytes"],
            current_topic_blob_count=capacity["blob_count"],current_topic_metadata_commit=capacity["commit"],
            current_topic_below_200000000_bytes=capacity["blob_bytes"]<200000000)
        save(out/"worker-process.json",state)
        if capacity["blob_bytes"]+150000>=200000000:
            raise ValueError("the actual topic lacks the reviewed150000-byte small-conclusion reserve")
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
        print(json.dumps(dict(kind="PHYSICAL_WAIST_FIRST_ROW_DEFERRED_READ_ONLY_METADATA_PUBLICATION",**event,
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
            raise ValueError("each current physical-waist-first-row-receiver input must be complete small current text")
        checked(src,entry["bytes"],entry["sha256"])
        raw=src.read_bytes()
        raw.decode("utf-8")
        if hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()!=entry["git_blob"]:
            raise ValueError("the complete current text differs from its frozen Git blob")
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
            same_record=previous.get("mathematical_input_sha256")==pins
            if previous.get("source_sha256")!=a.pipeline_sha and not same_record:
                continue
            ref=previous.get("scientific_conclusion")
            if ref:
                pp=path.parent/safe_name(ref["file"])
                checked(pp,ref["bytes"],ref["sha256"])
                prior=read(pp)
                if previous.get("source_sha256")==a.pipeline_sha and scientific_receipt_valid(prior,a.pipeline_sha,None,parameters,pins,runtime):
                    print(json.dumps(dict(reused_complete_same_scientific_conclusion=str(pp.relative_to(root)),
                        original_run_id=previous["run_id"],original_science_bytes=ref["bytes"],
                        original_science_sha256=ref["sha256"],execution_sha256=sha(path),
                        original_wrapper_complete=previous.get("complete"),
                        new_scientific_processes=0,old_successful_mathematics_recomputed=0)),flush=True)
                    return
            if same_record and previous.get("actual_new_scientific_processes",0)>0:
                raise RuntimeError("same physical waist first-row arithmetic has a prior incomplete outcome; require its concrete review and preserved scientific-result review")
        state["mathematical_input_sha256"]=pins
        inputs=[];index_files={}
        for entry in m["files"]:
            dst,receipt=copy_current(entry)
            inputs.append(receipt)
            index_files[entry["role"]]=dict(path=str(dst),bytes=dst.stat().st_size,sha256=entry["sha256"])
            checkpoint()
        state["old_binary_parts_restored"]=0
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
        if len(inputs)!=m["expected_input_count"] or len(parsed)!=m["expected_immutable_AST_files"]:
            raise ValueError("the complete physical waist first-row input and Python AST closure differs")
        if history or state.get("old_binary_parts_restored")!=0:
            raise ValueError("the physical waist first-row consumer must not restore old native inputs")
        state["old_artifacts_downloaded"]=0
        state["old_producers_or_integrals_reexecuted"]=0
        state["new_artifact_count"]=0;state["new_Release_count"]=0
        cmd=[sys.executable,"-u",str(work/PIPELINE),"--repo",str(work),
            "--manifest",str(tm),"--manifest-sha",a.manifest_sha,"--bits","320",
            "--out",str(out/"actual-scientific-conclusion.json")]
        for role in pins:
            cmd.extend(["--"+role.replace("_","-"),index_files[role]["path"]])
        for role,digest in pins.items():
            if index_files[role]["sha256"]!=digest:
                raise ValueError("one complete physical waist first-row mathematical input identity changed")
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
            # Tee continuously: complete new scientific stages reach Actions before
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
            dict(type="IncompleteScientificReceipt",message="the complete physical waist first-row scalar receipt did not validate"))
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
        print(json.dumps(dict(kind="PHYSICAL_WAIST_FIRST_ROW_ATOMIC_SCIENCE_REPRINT",
            bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())),flush=True)
        print("PHYSICAL_WAIST_FIRST_ROW_SCIENTIFIC_RESULT_BEGIN",flush=True)
        print(raw.decode(),end="",flush=True)
        print("PHYSICAL_WAIST_FIRST_ROW_SCIENTIFIC_RESULT_END",flush=True)
        state["complete_atomic_scientific_result_reprinted"]=True
    outputs=[out/name for name in ("actual-scientific-conclusion.json","new-scientific-child.stdout.log")]
    state["output_hashes"]=[rec(path,out) for path in outputs if path.is_file()]
    if proc is not None:
        original=out/"actual-scientific-conclusion.json"
        if original.read_bytes()!=compact(proc):
            raise ValueError("the complete physical-waist-first-row-receiver child science must retain its original canonical bytes")
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
    # Full science, every completed new stage and child log are already in stdout.
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
        if len(raw)>59000 or len(text.encode())>8000 or (science_raw is not None and len(science_raw)>75000):
            raise ValueError("full science is already preserved in stdout; one publication small-text gate failed")
        (report/"actual-result.md").write_text(text)
        (report/"execution.json").write_bytes(raw)
        if science_raw is not None:
            (report/"actual-scientific-conclusion.json").write_bytes(science_raw)
    def publish():
        snapshot();owned=str(report.relative_to(root));git("add","--sparse","--",owned)
        if git("diff","--cached","--quiet","--",owned,check=False).returncode!=0:
            git("commit","-m","visible-exact: record complete complete physical waist first-row receiver")
        while True:
            result=git("push","origin","HEAD:refs/heads/main",check=False)
            if result.returncode==0:
                return owned
            if not any(v in result.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
                raise RuntimeError("small physical-waist-first-row-receiver conclusion push failed outside concurrent-main rebase")
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
