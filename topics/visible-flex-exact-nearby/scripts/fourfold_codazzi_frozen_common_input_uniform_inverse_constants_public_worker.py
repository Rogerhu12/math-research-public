#!/usr/bin/env python3
"""Compute only new frozen common-input coordinate bounds from four immutable successful small receipts."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import urllib.error,urllib.request,select,importlib.metadata
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_frozen_common_input_uniform_inverse_constants.py"
REPORTS=TOPIC/"notes/frozen_common_input_uniform_inverse_constants_ci"
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

PUBLICATION_LIMITS=json.loads("{\"complete_science_bytes\":75000,\"complete_report_bytes\":8000,\"complete_prepublication_science_report_payload_bytes\":90000,\"complete_execution_bytes\":59000,\"pre_science_topic_reserve_bytes\":150000,\"target_complete_science_bytes\":35000,\"target_complete_prepublication_payload_bytes\":50000,\"scientific_file_atomic_and_complete_stdout_before_size_guards\":true,\"new_artifacts\":0,\"new_Releases\":0}")
SCIENCE_FIELDS=json.loads("[\"kind\",\"complete\",\"proved\",\"actual_returncode\",\"failure\",\"stage\",\"source_sha256\",\"input_manifest_sha256\",\"public_repository\",\"run_id\",\"run_attempt\",\"workflow_event_commit\",\"actual_scientific_checkout_commit\",\"runtime\",\"arithmetic_bits\",\"parameters\",\"input_sha256\",\"verified_original_inputs\",\"accepted_old_inputs\",\"complete_original_scope_fields_read_verbatim\",\"complete_original_scope_fields_sha256\",\"complete_saved_scalar_records_read_verbatim\",\"complete_saved_scalar_records_sha256\",\"complete_forward_leading_conclusion\",\"complete_coordinate_conclusion\",\"complete_frozen_stable_inverse_conclusion\",\"complete_operator_identity_conclusion\",\"retained_scope\",\"planned_shape\",\"actual_progress\",\"gates\",\"actual_mathematical_wall_seconds\"]")
SCIENCE_GATE_NAMES=json.loads("[\"actual public Actions runtime and the frozen new source are exact\",\"eight current small texts and the complete new parameter closure are frozen\",\"all five mathematical primaries retain their original bytes SHA and Git identity\",\"the TF complete fourteen gate success retains its full family and same two window inverse\",\"the KL complete sixteen gate success retains the full correlated mean and absolute short rate\",\"the WX complete twenty gate success retains its original embedded schema runtime and selected scope\",\"the RNE complete sixteen gate success retains both original natural negative inverse records\",\"the common family and frozen reflected phase domain retain every original endpoint and mean\",\"sixteen complete old scalar records and all required original scope fields are preserved\",\"the new complete forward leading bound uses the true reverse factor and a positive denominator\",\"both coordinate windows retain complete forward and inverse products in their exact order\",\"both frozen stable inverse windows retain the natural weights and the exact rational gamma\",\"all original inputs and records remain unchanged with zero old scientific evaluation\",\"all twenty three new scalar records and the complete operator identities are retained\",\"actual progress and every declared new scalar count match the complete target\",\"the complete thirty two field schema preserves the frozen reflected domain and every independent port\"]")
SCIENCE_PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"expected_actual_gate_count\":16,\"expected_current_inputs\":8,\"expected_total_inputs\":8,\"expected_Python_AST_files\":2,\"expected_historical_inputs\":0,\"original_actual_runs\":{\"TF\":\"43766881076/1\",\"KL\":\"43766439345/1\",\"WX\":\"43763424840/1\",\"RNE\":\"43792291190/1\"},\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_intrinsic_parameter\":\"-7789843107295549/4611686018427387904\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"exact_strict_cut\":\"76285779072683/320000000000000\",\"physical_root_piece\":2549,\"physical_period\":\"pi/2\",\"normalized_angular_measure\":true,\"physical_frequency\":\"n=4|j|\",\"original_natural_cutoff_abs_j\":97,\"actual_common_root_cutoff_abs_j\":1024,\"coordinate_windows\":[\"0\",\"-4/3\"],\"natural_negative_windows\":[\"-7/6\",\"-5/2\"],\"stable_output_windows\":[\"-1/6\",\"-3/2\"],\"exact_gamma97\":\"150545/150544\",\"fixed_selected_parameter_absolute_upper\":\"0.00000000009368259853002\",\"frozen_input_space\":\"X_s_fr = S_star D_plus H_nat^s\",\"natural_reflection_not_all_signed_carriers\":true,\"original_primitive_and_two_physical_means_retained\":true,\"independent_physical_means\":2,\"saved_actual_receipts\":4,\"saved_scalar_records\":16,\"saved_original_scope_collections\":4,\"new_principal_scalar_outputs\":7,\"new_elementary_scalar_records\":16,\"new_total_scalar_records\":23,\"optional_forward_Cs_constants_evaluated\":false,\"varying_selected_chart_identifications_evaluated\":false,\"old_target_calls_allowed\":0,\"old_source_imports_allowed\":0,\"old_exponentials_or_logarithms_reevaluated\":0,\"old_R97_RNE_graphs_or_comparisons_reevaluated\":0,\"full_incoming_or_finite_Schur_inverse_claimed\":false,\"full_complex_parameter_square_claimed\":false,\"uniform_selected_conjugacy_family_claimed\":false}")
SCIENCE_SCOPE=json.loads("{\"scientific_target\":\"uniform frozen reflected common input coordinates and two stable inverse window constants\",\"same_real_delta_family_and_fixed_intrinsic_eta0\":true,\"original_two_signed_carriers_and_natural_reflection_retained\":true,\"fixed_Dplus_phase_is_included_in_the_input_space\":true,\"TF_parity_and_sign_commutation_have_distinct_proofs\":true,\"natural_reflection_projection_not_replaced_by_full_signed_P97\":true,\"selected_H_and_S_are_frozen_once_not_extended_as_KAM_family\":true,\"forward_leading_uses_the_saved_reverse_radial_bound\":true,\"short_factor_has_original_absolute_rate_qualification\":true,\"root_eta_lower_from_full_original_coefficient_domain\":true,\"complete_mean_residual_used_in_exact_radial_correlation\":true,\"same_distributional_inverse_in_both_windows\":true,\"exact_weight_and_coordinate_order_retained\":true,\"independent_physical_mean_coordinates\":2,\"full_density_mean_identity_corrections_retained\":true,\"original_low_head_second_reference_and_infinite_radial_ports_retained\":true,\"old_actual_objects_read_only_and_scopes_not_widened\":true,\"old_R97_RNE_graphs_and_comparison_not_recomputed\":true,\"physical_bulk_Poisson_extension_newly_proved\":false,\"complete_incoming_inverse_claimed\":false,\"finite_Schur_inverse_claimed\":false,\"Riccati_operator_norm_continuity_claimed\":false,\"uniform_selected_conjugacy_family_claimed\":false,\"nonlinear_background_or_final_surface_claimed\":false,\"same_selected_ambient_operator_formula_at_original_delta_star\":true,\"old_SE8_literal_Sstar_Hnat_domain_not_claimed\":true,\"full_circle_principal_or_Cayley_restriction_proved\":false}")
SCIENCE_PLANNED_SHAPE=json.loads("{\"saved_actual_receipts\":4,\"saved_original_scope_collections\":4,\"saved_scalar_records\":16,\"new_forward_leading_scalars\":1,\"new_coordinate_window_bounds\":4,\"new_frozen_stable_inverse_windows\":2,\"new_principal_scalar_outputs\":7,\"new_elementary_scalar_records\":16,\"new_total_scalar_records\":23,\"new_pi_constants\":1,\"new_fixed_square_roots\":1,\"new_positive_sixth_roots\":1,\"new_optional_forward_Cs_constants\":0,\"retained_physical_means\":2}")
SUCCESS_ACTUAL_PROGRESS=json.loads("{\"accepted_original_successes\":4,\"saved_original_scalar_records\":16,\"saved_original_scope_collections\":4,\"new_forward_leading_scalar_completed\":1,\"new_common_input_window_bounds_completed\":4,\"new_frozen_stable_inverse_windows_completed\":2,\"new_pi_constants_completed\":1,\"new_fixed_square_roots_completed\":1,\"new_positive_sixth_roots_completed\":1,\"new_elementary_factor_records_completed\":16,\"old_scientific_targets_recomputed\":0,\"old_exponentials_reevaluated\":0,\"old_logarithms_reevaluated\":0,\"old_R97_RNE_graphs_or_comparisons_recomputed\":0,\"historical_inputs_restored\":0}")
SCIENCE_PIN_SHA256=json.loads("{\"contract\":\"8f3784473b98f9b49449b7012e4c5c919670418246fa03a7f28441aaca28b640\",\"tf_science\":\"a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720\",\"kl_science\":\"1ea36ae6462bf34bbda338cca3af6ad1cff3b5f3f6d293ed81fcb94472deadee\",\"wx_execution\":\"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12\",\"rne_science\":\"579b09aa7164ec4800187436248fdafca85691066afa419ed6fa8b6ab1de3086\"}")
SCIENCE_PIN_BYTES=json.loads("{\"contract\":32942,\"tf_science\":18206,\"kl_science\":20537,\"wx_execution\":43753,\"rne_science\":57079}")
SCIENTIFIC_GRAPH_SHAPES=json.loads("{\"complete_forward_leading_conclusion\":{\"complete_pi_interval\":\"__FINITE_SCALAR__\",\"complete_two_pi_interval\":\"__FINITE_SCALAR__\",\"complete_sqrt_two_pi_lower\":\"__FINITE_SCALAR__\",\"complete_inverse_sqrt_two_pi_upper\":\"__FINITE_SCALAR__\",\"complete_root_k_over_eta_upper\":\"__FINITE_SCALAR__\",\"complete_root_ratio_sixth_upper\":\"__FINITE_SCALAR__\",\"complete_root_to_waist_radial_upper\":\"__FINITE_SCALAR__\",\"complete_density_times_radial_upper\":\"__FINITE_SCALAR__\",\"complete_forward_leading_prefactor_upper\":\"__FINITE_SCALAR__\",\"complete_forward_leading_scalar_upper\":\"__FINITE_SCALAR__\",\"exact_formula\":\"ng_waist_upper * saved_reverse_radial_upper * saved_absolute_short_exp_upper * (2*pi)^(-1/2) * (Kr_root_upper/eta_root_lower)^(1/6)\",\"all_four_terminal_Ai_sign_wave_moduli_share_one_bound\":true,\"saved_absolute_short_exponential_used_in_both_directions\":true,\"positive_lower_endpoint_roles\":[\"eta_root_lower\",\"sqrt_two_pi_lower\"],\"old_exponential_not_recomputed\":true,\"true_waist_reverse_radial_factor_used\":true,\"root_full_coefficient_eta_lower_not_cut_only\":true,\"no_sector_sum_or_extra_sqrt2\":true},\"complete_coordinate_conclusion\":{\"windows\":{\"0\":{\"input_and_output_exponent\":\"0\",\"complete_Lambda_TF_inverse_product_upper\":\"__FINITE_SCALAR__\",\"complete_Ni_upper\":\"__FINITE_SCALAR__\",\"complete_S_TF_forward_product_upper\":\"__FINITE_SCALAR__\",\"complete_Ni_inverse_upper\":\"__FINITE_SCALAR__\",\"same_inverse_in_the_two_windows\":true},\"-4/3\":{\"input_and_output_exponent\":\"-4/3\",\"complete_Lambda_TF_inverse_product_upper\":\"__FINITE_SCALAR__\",\"complete_Ni_upper\":\"__FINITE_SCALAR__\",\"complete_S_TF_forward_product_upper\":\"__FINITE_SCALAR__\",\"complete_Ni_inverse_upper\":\"__FINITE_SCALAR__\",\"same_inverse_in_the_two_windows\":true}},\"exact_Ni_order\":\"Lambda_plus_delta^-1 T_F_delta^-1 S_star^-1\",\"exact_inverse_order\":\"S_star T_F_delta Lambda_plus_delta\",\"frozen_input_space\":\"X_s_fr = S_star D_plus H_nat^s\",\"original_natural_cutoff_abs_j\":97,\"actual_common_root_cutoff_abs_j\":1024,\"reflection_domain_transported_by_fixed_Dplus\":true,\"independent_mean_and_other_ports_use_identity_extension\":true},\"complete_frozen_stable_inverse_conclusion\":{\"exact_gamma97\":\"150545/150544\",\"complete_gamma97_upper\":\"__FINITE_SCALAR__\",\"windows\":{\"0\":{\"common_input_exponent\":\"0\",\"natural_exponent\":\"-7/6\",\"stable_output_exponent\":\"-1/6\",\"complete_coordinate_times_natural_inverse_upper\":\"__FINITE_SCALAR__\",\"complete_frozen_stable_inverse_upper\":\"__FINITE_SCALAR__\",\"uses_same_original_natural_distributional_inverse\":true},\"-4/3\":{\"common_input_exponent\":\"-4/3\",\"natural_exponent\":\"-5/2\",\"stable_output_exponent\":\"-3/2\",\"complete_coordinate_times_natural_inverse_upper\":\"__FINITE_SCALAR__\",\"complete_frozen_stable_inverse_upper\":\"__FINITE_SCALAR__\",\"uses_same_original_natural_distributional_inverse\":true}},\"exact_forward_order\":\"N_out^-1 S_nat_delta N_in^(7/6) Ni_delta_fr\",\"exact_inverse_order\":\"Ni_delta_fr^-1 N_in^(-7/6) S_nat_delta^-1 N_out\",\"old_natural_inverse_polynomials_not_recomputed\":true,\"frequency_weights_only_on_original_high_spaces\":true,\"optional_forward_Cs_constants_not_evaluated\":true}}")
SCIENCE_OPERATOR_IDENTITY=json.loads("{\"full_signed_carrier_space\":\"H_car^s = P97 H^s\",\"natural_space\":\"H_nat^s is the original SE reflected high space\",\"Dplus\":\"exp(-i*pi/4) Pi_plus + exp(i*pi/4) Pi_minus\",\"Lambda_plus_on_high_nonmean\":\"Lambda_plus_delta = a_delta D_plus with a_delta > 0\",\"frozen_input_space\":\"X_s_fr = S_star D_plus H_nat^s = (Ni_delta_star)^-1 H_nat^s\",\"frozen_norm\":\"inherited physical H^s norm\",\"natural_projector\":\"Q_fr = S_star D_plus Q_nat D_plus^-1 S_star^-1\",\"ambient_high_projector\":\"P_fr = S_star P97 S_star^-1\",\"natural_and_ambient_projectors_not_identified\":true,\"TF_reflection_identity\":\"R M_Fstar R = -M_Fstar and R I R = -I; R commutes with P1024\",\"TF_same_inverse_preserves_original_natural_reflection\":true,\"fixed_input_identity_across_delta\":\"identity on X_s_fr\",\"exact_Ni_restriction\":\"Ni_delta_fr(S_star D_plus f) = a_delta^-1 T_F_delta^-1 f\",\"independent_rest_extension\":\"diag(Ni_delta_fr, Id_rest); rest may include infinite radial ports\",\"full_circle_scalar_mean_not_scaled_by_a_delta\":true,\"physical_mean_coordinates\":2,\"selected_KAM_conjugacy_only_at_original_delta_star\":true,\"new_full_incoming_or_finite_Schur_inverse_proved\":false,\"old_SE8_literal_domain_corrected\":true,\"full_circle_principal_Cayley_restriction_needs_separate_domain_range\":true}")
FROZEN_ACCEPTED_OLD_INPUTS_SHA256="269bbedf447b770ffc9cd27085fc932a26cca3c80df62ff37595d54ab24983fc"
FROZEN_ORIGINAL_SCOPE_FIELDS_SHA256="3f12846bb79fc7cefd00649fecf6ac4ca3a7babe7fa584ff7cace9cf90f58c73"
FROZEN_SAVED_SCALAR_RECORDS_SHA256="57731cdef27a9fa90024339d9d4d4e58daef926f532f5d2290a1956516073b10"

def scientific_receipt_valid(proc,source,manifest,parameters,pins,runtime):
    """Accept exactly one complete same-family frozen-coordinate consequence, without old arithmetic."""
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
        if not (set(p)==set(SCIENCE_FIELDS)
            and p["kind"]=="complete_frozen_common_input_uniform_inverse_constants_v1"
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
            and p["planned_shape"]==SCIENCE_PLANNED_SHAPE
            and p["actual_progress"]==SUCCESS_ACTUAL_PROGRESS
            and isinstance(p["gates"],list) and len(p["gates"])==16
            and [v["name"] for v in p["gates"]]==SCIENCE_GATE_NAMES
            and all(set(v)=={"name","passed"} and v["passed"] is True for v in p["gates"])
            and type(p["actual_mathematical_wall_seconds"]) in (int,float)
            and p["actual_mathematical_wall_seconds"]>=0):
            return False
        originals=p["complete_original_scope_fields_read_verbatim"]
        scalars=p["complete_saved_scalar_records_read_verbatim"]
        if not (hashlib.sha256(compact(p["accepted_old_inputs"])).hexdigest()==FROZEN_ACCEPTED_OLD_INPUTS_SHA256
            and p["complete_original_scope_fields_sha256"]==FROZEN_ORIGINAL_SCOPE_FIELDS_SHA256
            and hashlib.sha256(compact(originals)).hexdigest()==FROZEN_ORIGINAL_SCOPE_FIELDS_SHA256
            and p["complete_saved_scalar_records_sha256"]==FROZEN_SAVED_SCALAR_RECORDS_SHA256
            and hashlib.sha256(compact(scalars)).hexdigest()==FROZEN_SAVED_SCALAR_RECORDS_SHA256):
            return False
        if not all(shape(p[key],expected) for key,expected in SCIENTIFIC_GRAPH_SHAPES.items()):
            return False
        if p["complete_operator_identity_conclusion"]!=SCIENCE_OPERATOR_IDENTITY:
            return False
        return True
    except (KeyError,TypeError,ValueError):
        return False

def render(state,science):
    """Render complete saved scalar records and actual statuses without evaluating arithmetic."""
    p=science if isinstance(science,dict) else {}
    run=str(state.get("run_id","unknown"));attempt=str(state.get("run_attempt","unknown"))
    lines=["# Actual frozen common-input uniform inverse constants","",
        "Run: ["+run+"/"+attempt+"](https://github.com/"+PUBLIC+"/actions/runs/"+run+")",
        "","Complete: "+str(state.get("complete",False)),
        "Child return code: "+str(state.get("actual_returncode")),
        "Actual new scientific processes: "+str(state.get("actual_new_scientific_processes",0)),
        "Scientific stage: "+str(p.get("stage","no scientific result")),
        "Scientific source SHA256: "+str(state.get("source_sha256")),
        "Manifest SHA256: "+str(state.get("input_manifest_sha256")),
        "Actual scientific checkout: "+str(state.get("actual_scientific_checkout_commit","not launched")),""]
    rows=[]
    f=p.get("complete_forward_leading_conclusion")
    if isinstance(f,dict) and "complete_forward_leading_scalar_upper" in f:
        rows.append(("Forward terminal-Ai leading scalar",f["complete_forward_leading_scalar_upper"]))
    c=p.get("complete_coordinate_conclusion")
    if isinstance(c,dict):
        for exponent,row in c.get("windows",{}).items():
            for key,label in (("complete_Ni_upper","Ni"),("complete_Ni_inverse_upper","Ni inverse")):
                if key in row:rows.append((label+" at s="+exponent,row[key]))
    z=p.get("complete_frozen_stable_inverse_conclusion")
    if isinstance(z,dict):
        for exponent,row in z.get("windows",{}).items():
            if "complete_frozen_stable_inverse_upper" in row:
                rows.append(("Stable C inverse at s="+exponent,row["complete_frozen_stable_inverse_upper"]))
    if rows:
        lines+=["## Complete new principal scalar records","",
            "| Bound | Original complete upper record |","|---|---|"]
        lines += ["| "+cell(label)+" | "+cell(ball(value))+" |" for label,value in rows]
        lines+=["","Every printed scalar is copied from the scientific document; its certified upper endpoint is used.",
            "All elementary factors and all 23 scalar slots remain in that complete document.",""]
    lines+=["## Exact scope","",
        "The following statements describe the frozen analytic contract.",
        ("The complete frozen scientific receipt has passed acceptance." if state.get("complete_mathematical_receipt_available") is True else
         "No complete new quantitative NIF conclusion is admitted by this report."),
        "The real reference family has |delta| <= 1/100000000 and fixed intrinsic eta0.",
        "The fixed physical input is X_s_fr = S_star D_plus H_nat^s, with its inherited H^s norm.",
        "D_plus is the original fixed signed phase; the natural reflection and ambient high projectors are distinct.",
        "Ni = Lambda_plus_delta^-1 T_F_delta^-1 S_star^-1, with inverse S_star T_F_delta Lambda_plus_delta.",
        "The stable inverse keeps Ni^-1 N_in^(-7/6) S_nat^-1 N_out in exactly that order.",
        "The two windows use the same inverse and the saved natural bounds at -7/6 and -5/2.",
        "Both independent physical means, low and radial head spaces, second inputs and other ports remain.",
        "No selected KAM family, complete incoming or finite Schur inverse, nonlinear background or final surface is claimed.",
        "Old scalars, exponentials, logarithms, R97 graphs and RNE inverse polynomials are not recomputed.","",
        "## Actual gates",""]
    gates=p.get("gates",[])
    for index,g in enumerate(gates,1):
        lines.append(str(index)+". "+("PASS" if g.get("passed") is True else "FAIL")+" - "+cell(g.get("name","")))
    if not gates:lines.append("No scientific gate has been recorded.")
    lines+=["","## Actual completion counters",""]
    for key,value in p.get("actual_progress",{}).items():
        lines.append("- "+cell(key)+": "+cell(value))
    lines+=["","## Execution and original inputs","",
        "Current complete text receipts: "+str(state.get("actual_verified_Git_input_count",0)),
        "Complete Python AST files: "+str(state.get("complete_immutable_Python_AST_file_count",0)),
        "Historical binary restores: "+str(state.get("old_binary_parts_restored",0)),
        "Scientific child wall seconds: "+str(state.get("new_scientific_child_wall_seconds","not launched")),
        "Input receipt SHA256: "+str(state.get("actual_verified_Git_input_receipts_sha256","not yet available")),
        "Python AST inventory SHA256: "+str(state.get("complete_immutable_Python_AST_inventory_sha256","not yet available")),"",
        "## Latest actual Git pulls and README checks","",
        "Total recorded checks: "+str(len(state.get("readme_checks",[])))+
        "; the complete original history is retained in [execution.json](execution.json).",""]
    for check in state.get("readme_checks",[])[-2:]:
        delta=check.get("actual_diff","")
        lines.append("- "+str(check.get("time"))+" -> "+str(check.get("after"))+
            "; README diff bytes="+str(len(delta.encode()))+
            (" (empty)" if not delta else "; SHA256="+hashlib.sha256(delta.encode()).hexdigest()))
    if not state.get("readme_checks"):lines.append("No successful pull was recorded.")
    failure=state.get("actual_failure")
    if failure:
        lines+=["","## Recorded failure","",cell(failure.get("type","Failure"))+": "+cell(failure.get("message",""))]
    lines+=["","The complete scientific JSON and both prepublication payloads are printed before publication size checks.",
        "A completed scientific child is preserved and is never repeated for publication or metadata failures.",""]
    return "\n".join(lines)

def emit_prepublication(state,science):
    report=render(state,science)
    science_raw=None if science is None else compact(science)
    payload=dict(marker="FROZEN_COMMON_INPUT_UNIFORM_INVERSE_CONSTANTS_COMPLETE_SCIENTIFIC_PREPUBLICATION_V1",
        source_sha256=state["source_sha256"],manifest_sha256=state["input_manifest_sha256"],
        run_id=state["run_id"],run_attempt=state["run_attempt"],
        actual_returncode=state.get("actual_returncode"),scientific_result=science,report_text=report)
    raw=compact(payload)
    status=dict(marker="FROZEN_COMMON_INPUT_UNIFORM_INVERSE_CONSTANTS_PREPUBLICATION_STATUS",
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
        raise ValueError("full frozen-common-input-uniform-inverse-constants science is saved and printed; prepublication payload exceeds90000")
    print(raw.decode(),end="",flush=True)
    process=compact(dict(marker="FROZEN_COMMON_INPUT_UNIFORM_INVERSE_CONSTANTS_EXECUTION_PREPUBLICATION_V1",execution=state))
    if len(process)>59000:
        raise ValueError("full frozen-common-input-uniform-inverse-constants science is preserved; execution metadata exceeds59000")
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
        raise RuntimeError("only this public repository Actions may evaluate new frozen-common-input-uniform-inverse-constants mathematics")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:
        raise ValueError("the separately pinned frozen-common-input-uniform-inverse-constants manifest or reviewed rules changed")
    m=read(a.manifest);rules=read(a.rules)
    current=m.get("files",[])
    history=m.get("historical_inputs",[])
    current_roles={v["role"] for v in current}
    current_paths={v["path"] for v in current}
    historical_roles={v["role"] for v in history}
    historical_paths={v["path"] for v in history}
    all_entries=current+history
    if (m.get("public_repository")!=PUBLIC or rules.get("repository")!=PUBLIC
        or m.get("kind")!="frozen_common_input_uniform_inverse_constants_public_inputs_v1"
        or m.get("source_sha256")!=a.pipeline_sha
        or m.get("source_path")!=str(PIPELINE)
        or m.get("parameters")!=SCIENCE_PARAMETERS
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
        or m.get("old_successful_scientific_calls_allowed") is not False
        or m.get("new_native_arrays_or_artifact_persistence_allowed") is not False):
        raise ValueError("the exact eight-current-text frozen common-input contract changed")
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
        raise ValueError("temporary frozen-common-input-uniform-inverse-constants work and outcome directories are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():
        raise FileExistsError("preserve the previous complete or partial frozen-common-input-uniform-inverse-constants run")
    if any(v.is_relative_to(root) for v in (work,out)):
        raise ValueError("all new numerical arrays must remain outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__)
    state=dict(kind="actual_public_frozen_common_input_uniform_inverse_constants_execution_v1",repository=PUBLIC,
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
            raise ValueError("a pinned frozen-common-input-uniform-inverse-constants source manifest or rule record changed during pull")
        if sha(root/rw)!=ws:
            raise ValueError("the currently running immutable frozen-common-input-uniform-inverse-constants wrapper changed")
        for name in m["current_input_paths"]:
            if sha(root/relpath(name))!=m["file_sha256"][name]:
                raise ValueError("an immutable current frozen-common-input-uniform-inverse-constants source or contract changed")
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
        print(json.dumps(dict(kind="FROZEN_COMMON_INPUT_UNIFORM_INVERSE_CONSTANTS_DEFERRED_READ_ONLY_METADATA_PUBLICATION",**event,
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
            raise ValueError("each current frozen-common-input-uniform-inverse-constants input must be complete small current text")
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
                raise RuntimeError("same frozen common-input arithmetic has a prior incomplete outcome; require its concrete review and preserved scientific-result review")
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
            raise ValueError("the complete frozen common-input input and Python AST closure differs")
        if history or state.get("old_binary_parts_restored")!=0:
            raise ValueError("the frozen common-input consumer must not restore old native inputs")
        state["old_artifacts_downloaded"]=0
        state["old_producers_or_integrals_reexecuted"]=0
        state["new_artifact_count"]=0;state["new_Release_count"]=0
        cmd=[sys.executable,"-u",str(work/PIPELINE),"--repo",str(work),
            "--manifest",str(tm),"--manifest-sha",a.manifest_sha,"--bits","320",
            "--out",str(out/"actual-scientific-conclusion.json")]
        for role,digest in pins.items():
            if index_files[role]["sha256"]!=digest:
                raise ValueError("one complete frozen common-input mathematical input identity changed")
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
            dict(type="IncompleteScientificReceipt",message="the complete frozen common-input scalar receipt did not validate"))
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
        print(json.dumps(dict(kind="FROZEN_COMMON_INPUT_UNIFORM_INVERSE_CONSTANTS_ATOMIC_SCIENCE_REPRINT",
            bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())),flush=True)
        print("FROZEN_COMMON_INPUT_UNIFORM_INVERSE_CONSTANTS_SCIENTIFIC_RESULT_BEGIN",flush=True)
        print(raw.decode(),end="",flush=True)
        print("FROZEN_COMMON_INPUT_UNIFORM_INVERSE_CONSTANTS_SCIENTIFIC_RESULT_END",flush=True)
        state["complete_atomic_scientific_result_reprinted"]=True
    outputs=[out/name for name in ("actual-scientific-conclusion.json","new-scientific-child.stdout.log")]
    state["output_hashes"]=[rec(path,out) for path in outputs if path.is_file()]
    if proc is not None:
        original=out/"actual-scientific-conclusion.json"
        if original.read_bytes()!=compact(proc):
            raise ValueError("the complete frozen-common-input-uniform-inverse-constants child science must retain its original canonical bytes")
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
            git("commit","-m","visible-exact: record complete frozen common-input uniform inverse constants")
        while True:
            result=git("push","origin","HEAD:refs/heads/main",check=False)
            if result.returncode==0:
                return owned
            if not any(v in result.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
                raise RuntimeError("small frozen-common-input-uniform-inverse-constants conclusion push failed outside concurrent-main rebase")
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
