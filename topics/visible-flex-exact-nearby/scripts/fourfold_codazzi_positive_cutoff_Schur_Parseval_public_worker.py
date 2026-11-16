#!/usr/bin/env python3
"""Run one new positive Schur-Parseval and coefficient-split readout from a frozen complete prior."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import urllib.error,urllib.request,select,importlib.metadata
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_positive_cutoff_Schur_Parseval.py"
REPORTS=TOPIC/"notes/positive_cutoff_Schur_Parseval_ci"
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

PUBLICATION_LIMITS=json.loads("{\"complete_preGit_max_bytes\":90000,\"complete_science_max_bytes\":75000,\"execution_max_bytes\":59000,\"publication_reserve_bytes\":150000,\"report_max_bytes\":8000}")
SCIENCE_FIELDS=json.loads("[\"kind\",\"public_repository\",\"workflow_event_commit\",\"actual_scientific_checkout_commit\",\"run_id\",\"run_attempt\",\"source_sha256\",\"input_manifest_sha256\",\"input_sha256\",\"runtime\",\"arithmetic_bits\",\"parameters\",\"retained_scope\",\"planned_shape\",\"actual_progress\",\"verified_original_inputs\",\"accepted_prior_input\",\"complete_prior_scientific_conclusion_read_verbatim\",\"prior_scientific_conclusion_sha256\",\"complete_new_split_coefficients\",\"complete_new_three_amplitude_functionals\",\"complete_new_positive_correction\",\"complete_new_coefficient_split\",\"complete_operator_identity_conclusion\",\"gates\",\"complete\",\"proved\",\"stage\",\"actual_returncode\",\"failure\",\"actual_mathematical_wall_seconds\"]")
SCIENCE_KIND=json.loads("\"complete_positive_cutoff_Schur_Parseval_and_coefficient_split_v1\"")
SCIENCE_GATE_NAMES=json.loads("[\"actual public runtime and directed arithmetic\",\"eight current pinned texts and no restored inputs\",\"four contracts and five full mathematical identities\",\"prior complete thirty-eight-field twenty-two-gate success retained\",\"all prior graphs records qualifications scopes and receipts retained\",\"twenty-one saved upper records at exact paths\",\"four complete split coefficients and all lag modes\",\"complete varying-symbol rows use pointwise bounds\",\"complete fixed-input columns use Parseval\",\"three complete Schur functionals include pullback\",\"complete physical pair cutoff and positive reception\",\"saved-first whole choice uses final record endpoints\",\"exact infinite coefficient remainder and all finite rows\",\"all old inputs frozen and old mathematical calls zero\",\"four complete graphs and operation counts agree\",\"complete thirty-one fields sixteen gates and physical limits\"]")
SCIENCE_PARAMETERS=json.loads("{\"Schur_input_window\":\"H^(-4/3)\",\"Schur_source_window\":\"H^(-2/3)\",\"Schur_split_integer\":128,\"arithmetic_bits\":320,\"coefficient_split_input\":\"selected Xfr_Hminus4_3 = S Dplus Hnat_Hminus4_3\",\"coefficient_split_output\":\"P Fix(Ra) intersect L2\",\"natural_input_cutoff_abs_j\":97,\"new_complete_graphs\":4,\"new_computed_scalar_records\":45,\"new_native_arrays_or_artifacts_allowed\":false,\"new_primary_targets\":\"same complete positive correction and exact infinite coefficient remainder\",\"new_printed_scalar_record_slots\":49,\"normalized_angular_measure\":true,\"old_exponentials_or_logarithms_reevaluated\":0,\"old_scientific_calls_allowed\":0,\"physical_frequency\":\"n=4|j|\",\"physical_period\":\"pi/2\",\"prior_success\":\"43812987299/1\"}")
SCIENCE_SCOPE=json.loads("{\"D_infinity_is_not_complete_Dalg\":true,\"FJ_and_both_primitive_ranks_retained\":true,\"both_signs_and_full_output_mean_retained\":true,\"finite_border_inverse_claimed\":false,\"full_prior_parameters_and_scopes_retained\":true,\"high_cutoff_or_background_claimed\":false,\"independent_physical_means\":2,\"physical_incoming_inverse_claimed\":false,\"physical_rhoi_and_complete_ell2_retained\":true,\"positive_comparison_only_same_operator\":true,\"root_sources_jumps_endpoints_and_matching_separate\":true,\"same_density_maps_and_normalizer_order\":true,\"same_positive_family_cutoff_and_receiver\":true,\"same_selected_reflected_coefficient_source\":true,\"varying_rows_and_fixed_columns_distinct\":true}")
SUCCESS_ACTUAL_PROGRESS=json.loads("{\"accepted_prior_successes\":1,\"copied_complete_prior_scientific_objects\":1,\"copied_prior_complete_graphs\":7,\"historical_or_native_inputs_restored\":0,\"new_amplitude_functionals\":3,\"new_coefficient_split_graphs\":1,\"new_positive_candidate_graphs\":1,\"new_rational_power_calls\":5,\"new_record_evaluations\":45,\"new_split_coefficient_graphs\":1,\"new_square_root_calls\":6,\"new_whole_positive_choices\":1,\"old_exponentials_or_logarithms_evaluated\":0,\"old_original_bound_records_retained\":42,\"old_original_qualification_records_retained\":3,\"old_original_scope_collections_retained\":5,\"old_scientific_producers_imported_or_called\":0,\"old_scientific_targets_recomputed\":0}")
SCIENCE_PIN_SHA256=json.loads("{\"pcra_proof\":\"f2b1e603654a3823bfc0e20664f191d06db739afa1dfdbe9b77426227b55f8ea\",\"prior_science\":\"e2cb2aacc031532e3b4db92873b404e9550599da75427dbb3c6448b65120d88d\",\"wcf_contract\":\"452ee9e41e27a1a2000ea2746e09decc6c936b37a5759a1ace656b500bbfb9dd\",\"wpc_contract\":\"2bc45c4c67261986bf2e94bb889d20757be8c713c31542c6a08e1da4353f8468\",\"wsp_contract\":\"80d2820758dd4f71cf170da237ce45ce14788a3d5f74c7a4e74820c4c297f3a7\"}")
SCIENCE_PIN_BYTES=json.loads("{\"pcra_proof\":12537,\"prior_science\":55533,\"wcf_contract\":23257,\"wpc_contract\":16086,\"wsp_contract\":10001}")
SCIENTIFIC_GRAPH_SHAPES=json.loads("{\"complete_new_coefficient_split\":{\"complete_D_infinity_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_Dalg_not_claimed_by_this_bound\":true,\"complete_FJ_primitive_ranks_and_ordered_dual_rows_retained\":true,\"complete_combined_density_row_positive_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_conjugated_two_primitive_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_ell2_dual_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_left_waist_two_primitive_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"exact_operator\":\"D_infinity=Qa Vw Ti-Qa A_J S Mc I A_F TF_inverse S_inverse\",\"finite_factor_is_not_a_physical_input_completion\":true,\"no_comparison_or_subtraction_from_old_Calg\":true,\"original_minus_h_minus_one_rhoi_and_new_plus_h_minus_one_ell2_retained\":true,\"selected_real_member_and_actual_reflected_source_only\":true},\"complete_new_positive_correction\":{\"complete_cutoff_source_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_first_row_terms_upper\":{\"g\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"h\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"w\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\"},\"complete_first_row_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_physical_pair_squared_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_physical_pair_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_positive_source_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_received_positive_candidate_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_second_row_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"genuine_root_shear_and_terminal_column_retained\":true,\"original_volume_finite_head_and_receiver_read_only\":true,\"physical_pair_and_two_means_retained\":true,\"root_finite_received_term_separate_and_unchanged\":true,\"same_original_positive_operator\":true,\"whole_received_positive_candidates\":{\"new_asymmetric_Schur_Parseval\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"saved_complete_positive\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\"},\"whole_received_positive_choice\":{\"all_candidates_retained\":true,\"complete_selected_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"selected_label\":\"__WHOLE_POSITIVE_CHOICE__\"}},\"complete_new_split_coefficients\":{\"column_head_coefficient_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"column_tail_coefficient_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"row_head_coefficient_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"row_tail_coefficient_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"split_integer\":128,\"split_is_not_an_operator_cutoff\":true,\"zero_output_and_both_lag_signs_retained\":true},\"complete_new_three_amplitude_functionals\":{\"amplitudes\":{\"g\":{\"column_head_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"column_tail_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_Schur_matrix_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_column_sum_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_functional_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_row_column_product_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_row_sum_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"row_head_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"row_tail_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\"},\"h\":{\"column_head_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"column_tail_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_Schur_matrix_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_column_sum_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_functional_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_row_column_product_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_row_sum_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"row_head_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"row_tail_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\"},\"w\":{\"column_head_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"column_tail_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_Schur_matrix_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_column_sum_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_functional_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_row_column_product_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_row_sum_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"row_head_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"row_tail_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\"}},\"fixed_input_columns_use_complete_Parseval\":true,\"full_both_signed_input_and_all_output_modes_including_mean\":true,\"original_scalar_pullback_paid_once\":true,\"varying_symbol_rows_use_pointwise_bounds_only\":true}}")
OPERATOR_IDENTITY=json.loads("{\"coefficient_finite_terms\":\"U_F V_F+U_S V_S-(h-1)rho_i+(h-1)ell2\",\"coefficient_remainder\":\"D_infinity=Qa Vw Ti-Qa A_J S Mc I A_F TF_inverse S_inverse\",\"no_inverse_or_finite_border_gate_claimed\":true,\"only_same_positive_operator_has_whole_candidate_comparison\":true,\"positive_received_order\":\"Kpos*(Cvol+Kchi*sqrt(C1^2+Fw^2)+CFH)\"}")
PLANNED_SHAPE=json.loads("{\"coefficient_split_compared_with_old_Dalg\":false,\"current_small_text_inputs\":8,\"historical_or_native_inputs\":0,\"immutable_AST_files\":2,\"mathematical_small_text_inputs\":5,\"new_complete_graphs\":4,\"new_computed_scalar_records\":45,\"new_printed_scalar_record_slots\":49,\"new_rational_power_calls\":5,\"new_square_root_calls\":6,\"new_whole_positive_choices\":1,\"prior_bound_records_preserved\":42,\"prior_complete_fields_preserved\":38,\"prior_complete_graphs_preserved\":7,\"prior_complete_successes\":1,\"prior_qualification_records_preserved\":3,\"prior_scope_collections_preserved\":5}")
SCALAR_SENTINEL=json.loads("\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\"")
LABEL_SENTINEL=json.loads("\"__WHOLE_POSITIVE_CHOICE__\"")
ALLOWED_WHOLE_LABELS=json.loads("[\"saved_complete_positive\",\"new_asymmetric_Schur_Parseval\"]")
FROZEN_ACCEPTED_PRIOR_SHA256=json.loads("\"c66145eafe7825b66a7bd857362f72c1fd70d2584386523db5d94024923bb096\"")
PRIOR_SCIENCE_SHA256=json.loads("\"e2cb2aacc031532e3b4db92873b404e9550599da75427dbb3c6448b65120d88d\"")
PRIOR_SCIENCE_BYTES=json.loads("55533")

def scientific_receipt_valid(proc,source,manifest,parameters,pins,runtime):
    """Validate four complete new graphs and the entire frozen prior without scalar arithmetic."""
    if not isinstance(proc,dict):
        return False
    p=proc
    def hexid(value,size):
        return isinstance(value,str) and len(value)==size and all(x in "0123456789abcdef" for x in value)
    def scalar(value):
        return isinstance(value,str) and 0<len(value)<=256 and not any(x in value.lower() for x in ("nan","inf"))
    def shape(value,expected):
        if expected==SCALAR_SENTINEL:
            return isinstance(value,dict) and set(value)=={"ball"} and scalar(value["ball"])
        if expected==LABEL_SENTINEL:
            return isinstance(value,str) and value in ALLOWED_WHOLE_LABELS
        if isinstance(expected,dict):
            return (isinstance(value,dict) and set(value)==set(expected)
                and all(shape(value[k],v) for k,v in expected.items()))
        if isinstance(expected,list):
            return (isinstance(value,list) and len(value)==len(expected)
                and all(shape(a,b) for a,b in zip(value,expected)))
        return type(value) is type(expected) and value==expected
    def retained(choice,candidates):
        return (isinstance(choice,dict)
            and set(choice)=={"selected_label","complete_selected_upper","all_candidates_retained"}
            and choice["selected_label"] in candidates
            and choice["complete_selected_upper"]==candidates[choice["selected_label"]]
            and choice["all_candidates_retained"] is True)
    try:
        if not (set(p)==set(SCIENCE_FIELDS) and len(p)==31
            and p["kind"]==SCIENCE_KIND
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
            and p["retained_scope"]==SCIENCE_SCOPE
            and p["actual_progress"]==SUCCESS_ACTUAL_PROGRESS
            and p["complete_operator_identity_conclusion"]==OPERATOR_IDENTITY
            and p["planned_shape"]==PLANNED_SHAPE
            and hashlib.sha256(compact(p["accepted_prior_input"])).hexdigest()==FROZEN_ACCEPTED_PRIOR_SHA256
            and isinstance(p["gates"],list) and len(p["gates"])==16
            and [v["name"] for v in p["gates"]]==SCIENCE_GATE_NAMES
            and all(set(v)=={"name","passed"} and v["passed"] is True for v in p["gates"])
            and type(p["actual_mathematical_wall_seconds"]) in (int,float)
            and 0<=p["actual_mathematical_wall_seconds"]<900):
            return False
        prior=p["complete_prior_scientific_conclusion_read_verbatim"]
        prior_raw=compact(prior)
        if (len(prior_raw)!=PRIOR_SCIENCE_BYTES
            or hashlib.sha256(prior_raw).hexdigest()!=PRIOR_SCIENCE_SHA256
            or p["prior_scientific_conclusion_sha256"]!=PRIOR_SCIENCE_SHA256):
            return False
        if not all(shape(p[key],expected) for key,expected in SCIENTIFIC_GRAPH_SHAPES.items()):
            return False
        positive=p["complete_new_positive_correction"]
        candidates=positive["whole_received_positive_candidates"]
        if (candidates["new_asymmetric_Schur_Parseval"]!=positive["complete_received_positive_candidate_upper"]
            or candidates["saved_complete_positive"]!=prior["complete_wpc_positive_correction_conclusion"]
                ["whole_received_positive_choice"]["complete_selected_upper"]
            or positive["complete_second_row_upper"]!=p["complete_new_three_amplitude_functionals"]
                ["amplitudes"]["w"]["complete_functional_upper"]):
            return False
        return retained(positive["whole_received_positive_choice"],candidates)
    except (KeyError,TypeError,ValueError):
        return False

def render(state,science):
    s=science or {}
    failed=state.get("actual_failure") is not None or s.get("failure") is not None
    complete=state.get("complete_mathematical_receipt_available") is True
    lines=[
        "# Actual positive Schur-Parseval and exact coefficient split bounds",
        "",
        ("Complete new scalar consequences of the published WSP and WCF formulas." if complete
         else "Execution record for WSP and WCF; complete new conclusions are not admitted."),
        "The entire prior success 43812987299/1, including its five inherited original successes, remains an immutable input.",
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
        "| Gates passed / recorded | "+str(sum(g.get("passed") is True for g in s.get("gates",[])))+"/"+str(len(s.get("gates",[])))+" |",
        "",
        "## Complete new target bounds",
        "",
        "| Target | Outward record |",
        "|---|---|"]
    pc=s.get("complete_new_positive_correction") or {}
    ce=s.get("complete_new_coefficient_split") or {}
    if complete:
        for label,value in (
            ("New complete original cutoff source",pc["complete_cutoff_source_upper"]),
            ("New complete received positive correction",pc["complete_received_positive_candidate_upper"]),
            ("Saved complete positive correction",pc["whole_received_positive_candidates"]["saved_complete_positive"]),
            ("Selected complete positive correction",pc["whole_received_positive_choice"]["complete_selected_upper"]),
            ("Exact remaining coefficient operator D_infinity",ce["complete_D_infinity_upper"]),
            ("Complete new mean dual ell2",ce["complete_ell2_dual_upper"]),
            ("Combined density dual ell2-rhoi: positive sum bound",ce["complete_combined_density_row_positive_upper"])):
            lines.append("| "+cell(label)+" | "+cell(ball(value))+" |")
        lines+=["",
            "Same-positive-operator selection: "+cell(pc["whole_received_positive_choice"]["selected_label"])+"."]
    lines+=["",
        "## Retained scope",
        "",
        "WSP uses pointwise estimates for varying-symbol rows and full Parseval sums for fixed-input columns. The split at 128 is a sum estimate, not a mode cutoff. Both input signs, every output mode including the mean, the original scalar pullback and the complete physical pair are retained. The original received gain is paid once; the original volume and finite-head source remain.",
        "WCF directly bounds D_infinity=Qa Vw Ti-Qa A_J S Mc I A_F TF_inverse S_inverse on the same selected reflected input. The exact FJ finite factor, both primitive ranks, original -(h-1)rhoi and new +(h-1)ell2 are retained separately. The new infinite remainder and dual are different targets from the former complete D_alg bound; no subtraction or numerical comparison with that bound is used.",
        ("All four new graphs and all 49 printed scalar slots are preserved in actual-scientific-conclusion.json. They contain 45 newly evaluated scalar records plus retained copies. The entire 55,533-byte prior scientific conclusion, with every graph, original bound, qualification, scope and receipt, is embedded unchanged." if complete
         else "Every available atomic new stage and the complete admitted prior remain in the scientific record. Complete new targets are admitted only after all four graphs and all identity, count and scope checks pass."),
        "The root finite response, negative sources, 3070 true jumps, all four endpoint terms, two physical means, radial head, metric parameter, 96 physical columns, all finite-factor cross terms and the actual finite border keep their separate matching obligations.",
        "No old profile, source integral, exponential sum, matrix word, prior scalar graph or original producer is recomputed. No historical archive or native input is restored. These bounds supply no high cutoff, physical incoming inverse, finite determinant, nonlinear background or final surface.",
        "",
        "Complete science and this report are printed before Git publication, with a separate execution prepublication receipt. Actual pulls, both README checks and exact topic-capacity metadata are retained in execution.json. No new array, artifact or Release is published.",
        ""]
    if failed:
        lines+=[("## Execution failure with complete scientific receipt" if complete else "## Actual incomplete outcome"),"",
            "Worker: "+cell(json.dumps(state.get("actual_failure"),sort_keys=True,ensure_ascii=False)),
            "Science: "+cell(json.dumps(s.get("failure"),sort_keys=True,ensure_ascii=False)),
            "Completed mathematical stages remain locked; an operational failure does not authorize repeating them.",""]
    return "\n".join(lines)

def emit_prepublication(state,science):
    report=render(state,science)
    science_raw=None if science is None else compact(science)
    payload=dict(marker="POSITIVE_CUTOFF_SCHUR_PARSEVAL_AND_COEFFICIENT_SPLIT_COMPLETE_SCIENTIFIC_PREPUBLICATION_V1",
        source_sha256=state["source_sha256"],manifest_sha256=state["input_manifest_sha256"],
        run_id=state["run_id"],run_attempt=state["run_attempt"],
        actual_returncode=state.get("actual_returncode"),scientific_result=science,report_text=report)
    raw=compact(payload)
    status=dict(marker="POSITIVE_CUTOFF_SCHUR_PARSEVAL_AND_COEFFICIENT_SPLIT_PREPUBLICATION_STATUS",
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
        raise ValueError("full positive-Schur-Parseval-and-coefficient-split science is saved and printed; prepublication payload exceeds90000")
    print(raw.decode(),end="",flush=True)
    process=compact(dict(marker="POSITIVE_CUTOFF_SCHUR_PARSEVAL_AND_COEFFICIENT_SPLIT_EXECUTION_PREPUBLICATION_V1",execution=state))
    if len(process)>59000:
        raise ValueError("full positive-Schur-Parseval-and-coefficient-split science is preserved; execution metadata exceeds59000")
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
        raise RuntimeError("only this public repository Actions may evaluate new positive-Schur-Parseval-and-coefficient-split mathematics")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:
        raise ValueError("the separately pinned positive-Schur-Parseval-and-coefficient-split manifest or reviewed rules changed")
    m=read(a.manifest);rules=read(a.rules)
    current=m.get("files",[])
    history=m.get("historical_inputs",[])
    current_roles={v["role"] for v in current}
    current_paths={v["path"] for v in current}
    historical_roles={v["role"] for v in history}
    historical_paths={v["path"] for v in history}
    all_entries=current+history
    if (m.get("public_repository")!=PUBLIC or rules.get("repository")!=PUBLIC
        or m.get("kind")!="positive_cutoff_Schur_Parseval_and_coefficient_split_current_only_inputs"
        or m.get("source_sha256")!=a.pipeline_sha
        or m.get("source_path")!=str(PIPELINE)
        or m.get("parameters")!=SCIENCE_PARAMETERS
        or m.get("scope")!=SCIENCE_SCOPE
        or current_roles!=(set(SCIENCE_PIN_SHA256)|{"source","worker","rules"})
        or m.get("complete_input_bytes")!=sum(v["bytes"] for v in current)
        or m.get("publication_limits")!=PUBLICATION_LIMITS
        or m.get("mathematical_input_sha256")!=SCIENCE_PIN_SHA256
        or m.get("expected_actual_gate_count")!=16
        or m.get("expected_current_input_count")!=8
        or m.get("expected_input_count")!=8
        or m.get("expected_immutable_AST_files")!=2
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
        raise ValueError("the exact eight-current-text positive Schur-Parseval and coefficient split contract changed")
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
        raise ValueError("temporary positive-Schur-Parseval-and-coefficient-split work and outcome directories are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():
        raise FileExistsError("preserve the previous complete or partial positive-Schur-Parseval-and-coefficient-split run")
    if any(v.is_relative_to(root) for v in (work,out)):
        raise ValueError("all new numerical arrays must remain outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__)
    state=dict(kind="actual_public_positive_cutoff_Schur_Parseval_and_coefficient_split_execution_v1",repository=PUBLIC,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_commit=os.environ["GITHUB_SHA"],worker_source_sha256=ws,
        source_sha256=a.pipeline_sha,input_manifest_sha256=a.manifest_sha,
        reviewed_rules_sha256=a.rules_sha,explicitly_read_rules_commit=rules["read_commit"],
        started_utc=utc(),complete=False,actual_returncode=None,readme_checks=[],
        actual_new_scientific_processes=0,old_numerical_enclosures_recomputed=0,
        old_prior_positive_graphs_recomputed=0,
        old_prior_coefficient_graphs_recomputed=0,old_completed_scalar_products_recomputed=0,
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
            raise ValueError("a pinned positive-Schur-Parseval-and-coefficient-split source manifest or rule record changed during pull")
        if sha(root/rw)!=ws:
            raise ValueError("the currently running immutable positive-Schur-Parseval-and-coefficient-split wrapper changed")
        for name in m["current_input_paths"]:
            if sha(root/relpath(name))!=m["file_sha256"][name]:
                raise ValueError("an immutable current positive-Schur-Parseval-and-coefficient-split source or contract changed")
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
        print(json.dumps(dict(kind="POSITIVE_CUTOFF_SCHUR_PARSEVAL_AND_COEFFICIENT_SPLIT_DEFERRED_READ_ONLY_METADATA_PUBLICATION",**event,
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
            raise ValueError("each current positive-Schur-Parseval-and-coefficient-split input must be complete small current text")
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
                raise RuntimeError("same positive Schur-Parseval and coefficient split arithmetic has a prior incomplete outcome; require its concrete review and preserved scientific-result review")
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
            raise ValueError("the complete positive Schur-Parseval and coefficient split input and Python AST closure differs")
        if history or state.get("old_binary_parts_restored")!=0:
            raise ValueError("the positive Schur-Parseval and coefficient split consumer must not restore old native inputs")
        state["old_artifacts_downloaded"]=0
        state["old_producers_or_integrals_reexecuted"]=0
        state["new_artifact_count"]=0;state["new_Release_count"]=0
        cmd=[sys.executable,"-u",str(work/PIPELINE),"--repo",str(work),
            "--manifest",str(tm),"--manifest-sha",a.manifest_sha,"--bits","320",
            "--out",str(out/"actual-scientific-conclusion.json")]
        for role,digest in pins.items():
            if index_files[role]["sha256"]!=digest:
                raise ValueError("one complete positive Schur-Parseval and coefficient split mathematical input identity changed")
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
            dict(type="IncompleteScientificReceipt",message="the complete positive Schur-Parseval and coefficient split scalar receipt did not validate"))
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
        print(json.dumps(dict(kind="POSITIVE_CUTOFF_SCHUR_PARSEVAL_AND_COEFFICIENT_SPLIT_ATOMIC_SCIENCE_REPRINT",
            bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())),flush=True)
        print("POSITIVE_CUTOFF_SCHUR_PARSEVAL_AND_COEFFICIENT_SPLIT_SCIENTIFIC_RESULT_BEGIN",flush=True)
        print(raw.decode(),end="",flush=True)
        print("POSITIVE_CUTOFF_SCHUR_PARSEVAL_AND_COEFFICIENT_SPLIT_SCIENTIFIC_RESULT_END",flush=True)
        state["complete_atomic_scientific_result_reprinted"]=True
    outputs=[out/name for name in ("actual-scientific-conclusion.json","new-scientific-child.stdout.log")]
    state["output_hashes"]=[rec(path,out) for path in outputs if path.is_file()]
    if proc is not None:
        original=out/"actual-scientific-conclusion.json"
        if original.read_bytes()!=compact(proc):
            raise ValueError("the complete positive-Schur-Parseval-and-coefficient-split child science must retain its original canonical bytes")
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
            git("commit","-m","visible-exact: record complete positive Schur-Parseval and coefficient split")
        while True:
            result=git("push","origin","HEAD:refs/heads/main",check=False)
            if result.returncode==0:
                return owned
            if not any(v in result.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
                raise RuntimeError("small positive-Schur-Parseval-and-coefficient-split conclusion push failed outside concurrent-main rebase")
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
