#!/usr/bin/env python3
"""Run one new complete positive cutoff and reflected coefficient readout from five immutable successes."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import urllib.error,urllib.request,select,importlib.metadata
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_positive_cutoff_and_reflected_coefficient_refinement.py"
REPORTS=TOPIC/"notes/positive_cutoff_and_reflected_coefficient_refinement_ci"
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
SCIENCE_FIELDS=json.loads("[\"kind\",\"complete\",\"proved\",\"actual_returncode\",\"failure\",\"stage\",\"source_sha256\",\"input_manifest_sha256\",\"public_repository\",\"run_id\",\"run_attempt\",\"workflow_event_commit\",\"actual_scientific_checkout_commit\",\"runtime\",\"arithmetic_bits\",\"parameters\",\"input_sha256\",\"verified_original_inputs\",\"accepted_old_inputs\",\"copied_complete_original_scopes\",\"copied_complete_original_scopes_sha256\",\"copied_original_scalar_records\",\"copied_original_scalar_records_sha256\",\"copied_original_qualification_records\",\"copied_original_qualification_records_sha256\",\"complete_operator_identity_conclusion\",\"complete_wpc_geometry_and_moment_conclusion\",\"complete_wpc_cauchy_and_schur_conclusion\",\"complete_wpc_positive_correction_conclusion\",\"complete_wce_root_coefficient_conclusion\",\"complete_wce_projected_rank_conclusion\",\"complete_wce_waist_conclusion\",\"complete_wce_algebraic_conclusion\",\"retained_scope\",\"planned_shape\",\"actual_progress\",\"gates\",\"actual_mathematical_wall_seconds\"]")
SCIENCE_KIND=json.loads("\"complete_positive_cutoff_and_reflected_coefficient_refinement_v1\"")
SCIENCE_GATE_NAMES=json.loads("[\"public pinned runtime and directed scalar arithmetic in the actual checkout\",\"ten current small texts and no historical or native inputs\",\"two published contracts and seven immutable mathematical identities\",\"complete original PC thirty-gate positive correction success\",\"complete original TF fourteen-gate common-root normalizer success\",\"complete original WX twenty-gate selected full-density coordinate success\",\"complete original WT twenty-gate waist coefficient success with all fixed test results retained\",\"complete original SEI twenty-gate individual coefficient success\",\"same complete PC positive trial cutoff output window means and matrix-strip qualification\",\"same selected WCE root finite primitive and true waist identities\",\"all forty-two original bound records and three qualifications copied verbatim\",\"new shifted moments and actual-output-window geometry are complete\",\"new full-strip Cauchy lists and three weighted Schur functionals are complete\",\"new full two-row cutoff and same received positive candidate are complete\",\"new same-root coefficient factors retain already-paid right-normalizer costs\",\"new full and projected primitive ranks retain their exact mean rows\",\"new exact-waist second-order factors retain the saved forward remainder\",\"new complete algebraic candidates use the same reflected input and full target\",\"whole candidate choices use final saved upper endpoints and retain all candidates\",\"all original input bytes records scopes and receipts remain unchanged\",\"all seven new graphs and actual progress match the complete planned shape\",\"the complete thirty-eight-field conclusion retains all physical limits and twenty-two gates\"]")
SCIENCE_PARAMETERS=json.loads("{\"WCE_input_space\":\"Xfr_Hminus4_3 = S Dplus Hnat_Hminus4_3\",\"WCE_only_at_original_selected_parameter\":true,\"WCE_output_space\":\"P Fix(Ra) intersect L2\",\"WPC_input_window\":\"H^(-4/3)\",\"WPC_received_output\":\"same old-circle primitive-density L2 pair plus both means\",\"WPC_source_window\":\"ordinary L2_dr (H^(-2/3) pair)\",\"actual_common_root_cutoff_abs_j\":1024,\"actual_moving_waist_cutoff_abs_j\":268435456,\"arithmetic_bits\":320,\"exact_PC_cutoff_derivative_upper\":\"1875000\",\"exact_PC_full_amplitude_strip\":\"1/256\",\"exact_PC_matrix_lag_strip\":\"1/64\",\"exact_PC_positive_transition\":[\"1/500000\",\"3/1000000\"],\"exact_PC_saved_contour_shift\":\"1/512\",\"exact_PC_transition_length\":\"1/1000000\",\"exact_complete_matrix_weight_upper\":\"(64/63)*16^(2/3)\",\"exact_density_deviation_upper\":\"1/31\",\"exact_intrinsic_parameter\":\"-7789843107295549/4611686018427387904\",\"exact_new_profile_moment_upper_rule\":\"(3p/8)^(2p/3)\",\"exact_profile_moment_shift\":\"5/2\",\"exact_real_delta_radius\":\"1/100000000\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"exact_selected_parameter_absolute_upper\":\"0.00000000009368259853002\",\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_terminal_T\":\"1/2000\",\"expected_Python_AST_files\":2,\"expected_actual_gate_count\":22,\"expected_current_inputs\":10,\"expected_historical_inputs\":0,\"expected_total_inputs\":10,\"fixed_intrinsic_parameter\":\"eta_0\",\"full_complex_parameter_square_claimed\":false,\"full_physical_incoming_or_finite_Schur_inverse_claimed\":false,\"independent_physical_mean_coordinates\":2,\"minimum_physical_frequency\":388,\"natural_input_cutoff_abs_j\":97,\"new_complete_mathematical_graphs\":7,\"new_whole_candidate_choices\":2,\"normalized_angular_measure\":true,\"old_exponentials_or_logarithms_reevaluated\":0,\"old_profiles_integrals_exponential_sums_or_matrix_words_reevaluated\":0,\"old_scientific_source_imports_allowed\":0,\"old_successful_scientific_calls_allowed\":0,\"original_actual_runs\":{\"PC\":\"43740173506/1\",\"SEI\":\"43773319871/1\",\"TF\":\"43766881076/1\",\"WT\":\"43763134339/1\",\"WX\":\"43763424840/1\"},\"physical_frequency\":\"n=4|j|\",\"physical_period\":\"pi/2\",\"physical_root_piece\":2549,\"saved_actual_receipts\":5,\"saved_bound_records\":42,\"saved_original_scope_collections\":5,\"saved_qualification_records\":3,\"shifted_profile_moments\":[\"11/4\",\"13/4\",\"15/4\",\"17/4\",\"19/4\",\"23/4\",\"25/4\"]}")
SCIENCE_SCOPE=json.loads("{\"WCE_SEI_H2_is_Bessel_upper_not_unsaved_Wiener_record\":true,\"WCE_actual_input_is_fixed_phase_transported_reflection_not_full_signed_circle\":true,\"WCE_actual_two_I_waist_factor_and_physical_density_mean_rank_retained\":true,\"WCE_complete_two_primitive_ranks_written_before_restriction\":true,\"WCE_exact_waist_first_symbol_zero_does_not_set_second_symbol_zero\":true,\"WCE_full_density_S_preserves_integral_and_actual_input_has_zero_auxiliary_mean\":true,\"WCE_full_root_finite_dual_rows_and_TF_after_right_order_retained\":true,\"WCE_no_extra_TF_inverse_or_Ni_factor\":true,\"WCE_only_original_selected_real_member_and_fixed_intrinsic_reference\":true,\"WCE_only_projected_Ecoeff_equals_projected_E0\":true,\"WCE_saved_CI_B_product_read_verbatim\":true,\"WPC_Kpos_already_includes_positive_seven_port_and_factor9\":true,\"WPC_actual_scalar_X_pullback_not_full_density\":true,\"WPC_complete_angular_matrix_words_paid_before_weighting\":true,\"WPC_complete_both_signed_carriers_and_all_output_modes\":true,\"WPC_genuine_terminal_column_and_nonzero_root_beta_retained\":true,\"WPC_old_volume_finite_head_source_and_received_gain_read_only\":true,\"WPC_only_specific_two_thirds_weight_uses_C2_Schur\":true,\"WPC_root_finite_received_term_retained_separately_not_added_to_new_positive\":true,\"WPC_same_original_PC_positive_trial_cutoff_and_complete_real_family\":true,\"WPC_saved_wide_P_H_moduli_supply_new_finite_Cauchy_derivatives\":true,\"WPC_target_is_full_positive_pair_Hminus2_3_not_negative_special_source\":true,\"actual_finite_border_inverse_claimed\":false,\"all_old_complete_receipts_parameters_and_scopes_frozen\":true,\"all_original_targets_profiles_and_source_integrals_not_recomputed\":true,\"complete_physical_incoming_inverse_claimed\":false,\"complete_return_R0_or_nonlinear_background_claimed\":false,\"historical_native_or_archive_inputs_restored\":false,\"independent_physical_means\":2,\"negative_source_positive_volume_endpoint_and_true_mean_matching_not_removed\":true,\"physical_paired_row_source_target_not_replaced_by_Ti_endomorphism\":true,\"scientific_target\":\"same positive correction and same complete reflected coefficient error\",\"true_radial_head_actual_root_border_and_independent_second_input_retained\":true,\"two_new_targets_are_distinct_and_not_summed_as_an_operator_inverse\":true,\"whole_candidates_preserve_same_complete_operator_and_final_record_endpoints\":true}")
SUCCESS_ACTUAL_PROGRESS=json.loads("{\"accepted_original_successes\":5,\"copied_original_bound_records\":42,\"copied_original_qualification_records\":3,\"copied_original_scope_collections\":5,\"historical_or_native_inputs_restored\":0,\"new_wce_complete_candidate_graphs\":1,\"new_wce_rank_graphs\":1,\"new_wce_root_graphs\":1,\"new_wce_waist_graphs\":1,\"new_whole_candidate_choices\":2,\"new_wpc_cauchy_and_schur_graphs\":1,\"new_wpc_complete_positive_candidates\":1,\"new_wpc_geometry_and_moment_graphs\":1,\"old_completed_scalar_products_recomputed\":0,\"old_exponentials_or_logarithms_evaluated\":0,\"old_profiles_exponential_sums_or_integrals_recomputed\":0,\"old_scientific_producers_imported_or_called\":0,\"old_scientific_targets_recomputed\":0}")
SCIENCE_PIN_SHA256=json.loads("{\"pc_execution\":\"75f780f60446bd2a47fe286e72ca24fad929e3486c12d9ecbea42f42b9b1a817\",\"sei_execution\":\"b0088f831471f29d41624e487586fbb9f4801ef7837f9b4dd3c29a57e51b3d29\",\"tf_science\":\"a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720\",\"wce_contract\":\"3d77e17b15a2dd37c7c66d969d28c50edc5dcbaa7608d6686477ac322ebc0bcf\",\"wpc_contract\":\"2bc45c4c67261986bf2e94bb889d20757be8c713c31542c6a08e1da4353f8468\",\"wt_science\":\"2a406e4506bb5a19646924e2072ec83d8806055a083ba7e1b1acfb9ab21d142d\",\"wx_execution\":\"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12\"}")
SCIENCE_PIN_BYTES=json.loads("{\"pc_execution\":46253,\"sei_execution\":46192,\"tf_science\":18206,\"wce_contract\":22798,\"wpc_contract\":16086,\"wt_science\":27619,\"wx_execution\":43753}")
SCIENTIFIC_GRAPH_SHAPES=json.loads("{\"complete_wce_algebraic_conclusion\":{\"complete_full_Calg_upper\":\"record\",\"complete_full_candidate_after_projection_upper\":\"record\",\"complete_full_candidate_algebra_upper\":\"record\",\"complete_full_rank_and_root_before_projection_upper\":\"record\",\"complete_projected_Calg_upper\":\"record\",\"complete_projected_candidate_algebra_upper\":\"record\",\"complete_projected_rank_and_root_upper\":\"record\",\"complete_projected_root_upper\":\"record\",\"complete_whole_choice\":{\"all_candidates_retained\":true,\"complete_selected_upper\":\"record\",\"selected_label\":\"label\"},\"full_and_projected_candidates_both_saved\":true,\"input_normalizer_not_reapplied_to_coefficient_error\":true,\"no_full_physical_incoming_or_finite_inverse_claimed\":true,\"operator\":\"=D_alg = Lpartial Y_WJ Ni - Qa Ti\",\"physical_mean_rank_and_TF_finite_rank_retained\":true,\"positive_negative_endpoint_state_errors_remain_separate\":true,\"same_complete_operator_and_leading_row_for_both_candidates\":true,\"source\":\"=Xfr_Hminus4_3 = S Dplus Hnat_Hminus4_3\",\"target\":\"=P Fix(Ra) intersect L2\",\"whole_choice_uses_final_retained_outward_records\":true},\"complete_wce_projected_rank_conclusion\":{\"both_full_primitive_ranks_written_before_restriction\":true,\"complete_full_first_primitive_rank_upper\":\"record\",\"complete_full_second_primitive_rank_upper\":\"record\",\"complete_full_two_primitive_ranks_upper\":\"record\",\"complete_projected_density_mean_coefficient_upper\":\"record\",\"complete_projected_primitive_rank_upper\":\"record\",\"complete_projected_rank_coefficient_L2_upper\":\"record\",\"exact_density_deviation_upper\":\"=1/31\",\"exact_full_rank_formula\":\"=ci tensor ppsi - (ci*ppsi) tensor 1\",\"exact_projected_rank_on_actual_input\":\"=(vi - nu*(h-1)) tensor ppsi\",\"full_density_S_preserves_the_integral\":true,\"only_projected_Ecoeff_equals_projected_E0\":true,\"physical_density_mean_rank_not_removed\":true,\"zero_input_mean_only_on_actual_Xfr\":true},\"complete_wce_root_coefficient_conclusion\":{\"TF_after_right_factors_read_once\":true,\"complete_absolute_incoming_mean_upper\":\"record\",\"complete_conjugated_root_strong_fee_upper\":\"record\",\"complete_incoming_forward_Hminus4_3_upper\":\"record\",\"complete_nonmean_Wfour_thirds_upper\":\"record\",\"complete_root_coefficient_Linfty_upper\":\"record\",\"complete_root_strong_fee_upper\":\"record\",\"complete_root_two_primitive_fee_upper\":\"record\",\"exact_order\":\"=S (F_J - M_c I A_F) T_F_inverse S_inverse\",\"input_window\":\"=H^(-4/3)\",\"no_second_TF_inverse_or_Ni_factor\":true,\"old_CI_B_product_not_recomputed\":true,\"only_denominator_from_true_psi_lower\":true,\"output_window_for_root_strong_fees\":\"=L2\",\"root_FJ_full_mean_and_dual_rows_retained\":true},\"complete_wce_waist_conclusion\":{\"actual_moving_Js\":268435456,\"actual_second_normalizer_and_minus_Sr_retained\":true,\"complete_physical_density_mean_rank_upper\":\"record\",\"complete_physical_row_sum_upper\":\"record\",\"complete_physical_two_primitive_row_upper\":\"record\",\"complete_waist_forward_L2_upper\":\"record\",\"complete_waist_second_normalizer_L2_upper\":\"record\",\"complete_waist_second_normalizer_strong_upper\":\"record\",\"exact_Vw_order\":\"=U_H_inverse B_w U_H\",\"exact_first_waist_normalizer_is_zero_by_WPL\":true,\"no_old_first_finite_fee_subtracted\":true,\"old_complete_Id_plus_A1_times_A2_fee_read_verbatim\":true,\"reflected_pair_sqrt_two_cancels_on_both_sides\":true,\"two_independent_physical_mean_ports_retained\":true},\"complete_wpc_cauchy_and_schur_conclusion\":{\"all_output_means_and_original_P_retained\":true,\"complete_three_amplitude_functionals\":{\"g\":{\"complete_Hminus4_3_to_Hminus2_3_upper\":\"record\",\"complete_amplitude_angular_derivative_upper\":[\"record\",\"record\",\"record\"],\"complete_inverse_angle_second_derivative_upper\":\"record\",\"complete_weighted_phase_derivative_upper\":[\"record\",\"record\",\"record\"]},\"h\":{\"complete_Hminus4_3_to_Hminus2_3_upper\":\"record\",\"complete_amplitude_angular_derivative_upper\":[\"record\",\"record\",\"record\"],\"complete_inverse_angle_second_derivative_upper\":\"record\",\"complete_weighted_phase_derivative_upper\":[\"record\",\"record\",\"record\"]},\"w\":{\"complete_Hminus4_3_to_Hminus2_3_upper\":\"record\",\"complete_amplitude_angular_derivative_upper\":[\"record\",\"record\",\"record\"],\"complete_inverse_angle_second_derivative_upper\":\"record\",\"complete_weighted_phase_derivative_upper\":[\"record\",\"record\",\"record\"]}},\"exact_full_holomorphic_strip\":\"=1/256\",\"full_two_row_reconstruction_not_replaced_by_one_height\":true,\"g_second_derivative_includes_complete_p_third_derivative\":true,\"no_unsaved_RJ_jet_used\":true},\"complete_wpc_geometry_and_moment_conclusion\":{\"complete_a_profile_derivative_upper\":[\"record\",\"record\",\"record\"],\"complete_b_profile_derivative_upper\":[\"record\",\"record\",\"record\"],\"complete_pair_profile_derivative_upper\":[\"record\",\"record\",\"record\"],\"exact_profile_moment_shift\":\"=5/2\",\"exact_total_Tmin_exponent\":\"=-11/4\",\"full_two_sign_matrix_including_all_output_modes\":true,\"geometry\":{\"complete_same_shift_matrix_weight_upper\":\"record\",\"complete_shifted_profile_prefactor_upper\":\"record\",\"frequency_Bessel_factor_upper\":\"record\",\"frequency_inverse_upper\":\"record\",\"frequency_minus_one_third_upper\":\"record\",\"physical_cutoff_radial_factor_upper\":\"record\",\"scalar_pullback_Hminus2_3_upper\":\"record\",\"scalar_pullback_L2_upper\":\"record\"},\"old_Airy_profiles_or_exponential_sums_recomputed\":false,\"shifted_moment_upper\":{\"11/4\":\"record\",\"13/4\":\"record\",\"15/4\":\"record\",\"17/4\":\"record\",\"19/4\":\"record\",\"23/4\":\"record\",\"25/4\":\"record\"}},\"complete_wpc_positive_correction_conclusion\":{\"already_received_Kpos_used_exactly_once\":true,\"complete_cutoff_source_upper\":\"record\",\"complete_first_row_term_upper\":[\"record\",\"record\",\"record\"],\"complete_first_row_upper\":\"record\",\"complete_ordered_JB_word_upper\":\"record\",\"complete_ordered_JL_word_upper\":\"record\",\"complete_ordered_J_word_upper\":\"record\",\"complete_ordinary_volume_and_finite_head_source_read_only\":true,\"complete_positive_source_upper\":\"record\",\"complete_received_positive_candidate_upper\":\"record\",\"complete_second_row_upper\":\"record\",\"full_incoming_or_finite_border_inverse_claimed\":false,\"full_means_genuine_root_shear_and_terminal_column_retained\":true,\"new_positive_reception_is_same_Rplus_in_WUE\":true,\"root_finite_received_term_is_separate_and_unchanged\":true,\"same_original_PC_trial_and_cutoff\":true,\"whole_received_positive_candidates\":{\"new_actual_output_window_cutoff\":\"record\",\"saved_complete_positive\":\"record\"},\"whole_received_positive_choice\":{\"all_candidates_retained\":true,\"complete_selected_upper\":\"record\",\"selected_label\":\"label\"}}}")
FROZEN_ACCEPTED_OLD_INPUTS_SHA256=json.loads("\"1be092345ec066222873f45e624ce2544be035a104502622ad096a21cd4df0b8\"")
FROZEN_ORIGINAL_SCOPE_FIELDS_SHA256=json.loads("\"2e21ee2bf8bc0db069ea9a0390f326fa32a6cbc6d324bfcf6af86f099610ba20\"")
FROZEN_QUALIFICATION_RECORDS_SHA256=json.loads("\"e6d95b77b886921337ba37201e2fd0da67c26c02233672e794479b3019bd669e\"")
FROZEN_SAVED_SCALAR_RECORDS_SHA256=json.loads("\"1966c937ea41995ab4ee65cd870c997dfd0e201ad9afaf817f149eafa3e17c6a\"")
OPERATOR_IDENTITY=json.loads("{\"coefficient_complete_row\":\"D_alg=Qa Vw Ti-(h-1)rho_i+Qa A_J P_h(R_S+S R_F S_inverse)\",\"coefficient_projected_identity\":\"P_h E_coeff = P_h(R_S+S R_F S_inverse)\",\"coefficient_rank_exact\":\"R_S=ci tensor ppsi-(ci*ppsi) tensor 1\",\"coefficient_root_exact\":\"(Id+MC I) TF_inverse = Id+Mc I+(F_J-Mc I A_F) TF_inverse\",\"coefficient_source\":\"Xfr_Hminus4_3 = S Dplus Hnat_Hminus4_3\",\"coefficient_target\":\"P Fix(Ra) intersect L2\",\"full_physical_mean_rank_retained\":true,\"only_new_scalar_enclosures_not_new_inverse_or_actual_background\":true,\"positive_complete_reconstruction\":\"h1=P T(hamp)+J(P T(gamp)-L P T(hamp)-B P T(w)); h2=P T(w)\",\"positive_received_order\":\"Kpos*(saved_Cvol+new_Ccut+saved_CFH)\",\"positive_source\":\"original chi_prime times complete genuine raw pair hG\",\"positive_whole_choice\":\"same Rplus in the complete WUE tuple\",\"root_finite_output\":\"saved complete received RF remains separate; its actual trace border is not evaluated\",\"same_selected_parameter_only_for_coefficient\":true}")
PLANNED_SHAPE=json.loads("{\"complete_new_graphs\":7,\"complete_original_successes\":5,\"complete_saved_output_scalar_slots\":90,\"copied_bound_records\":42,\"copied_qualification_records\":3,\"full_physical_inverse_claimed\":false,\"historical_inputs_restored\":0,\"new_whole_choices\":2,\"old_scientific_calls\":0,\"original_scope_collections\":5,\"scalar_slots_by_graph\":{\"complete_wce_algebraic_conclusion\":9,\"complete_wce_projected_rank_conclusion\":6,\"complete_wce_root_coefficient_conclusion\":7,\"complete_wce_waist_conclusion\":6,\"complete_wpc_cauchy_and_schur_conclusion\":24,\"complete_wpc_geometry_and_moment_conclusion\":24,\"complete_wpc_positive_correction_conclusion\":14}}")

def scientific_receipt_valid(proc,source,manifest,parameters,pins,runtime):
    """Validate all seven complete new graphs without recomputing any scalar."""
    if not isinstance(proc,dict):
        return False
    p=proc
    def hexid(value,size):
        return isinstance(value,str) and len(value)==size and all(x in "0123456789abcdef" for x in value)
    def scalar(value):
        return isinstance(value,str) and 0<len(value)<=256 and not any(x in value.lower() for x in ("nan","inf"))
    def shape(value,expected):
        if expected=="record":
            return isinstance(value,dict) and set(value)=={"ball"} and scalar(value["ball"])
        if expected=="label":
            return isinstance(value,str)
        if isinstance(expected,str) and expected.startswith("="):
            return value==expected[1:]
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
        if not (set(p)==set(SCIENCE_FIELDS) and len(p)==38
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
            and hashlib.sha256(compact(p["accepted_old_inputs"])).hexdigest()==FROZEN_ACCEPTED_OLD_INPUTS_SHA256
            and isinstance(p["gates"],list) and len(p["gates"])==22
            and [v["name"] for v in p["gates"]]==SCIENCE_GATE_NAMES
            and all(set(v)=={"name","passed"} and v["passed"] is True for v in p["gates"])
            and type(p["actual_mathematical_wall_seconds"]) in (int,float)
            and 0<=p["actual_mathematical_wall_seconds"]<900):
            return False
        for name,expected in (
            ("copied_original_scalar_records",FROZEN_SAVED_SCALAR_RECORDS_SHA256),
            ("copied_complete_original_scopes",FROZEN_ORIGINAL_SCOPE_FIELDS_SHA256),
            ("copied_original_qualification_records",FROZEN_QUALIFICATION_RECORDS_SHA256)):
            if (p[name+"_sha256"]!=expected
                or hashlib.sha256(compact(p[name])).hexdigest()!=expected):
                return False
        if not all(shape(p[key],expected) for key,expected in SCIENTIFIC_GRAPH_SHAPES.items()):
            return False
        positive=p["complete_wpc_positive_correction_conclusion"]
        candidates=positive["whole_received_positive_candidates"]
        records=p["copied_original_scalar_records"]
        if (candidates["new_actual_output_window_cutoff"]!=positive["complete_received_positive_candidate_upper"]
            or candidates["saved_complete_positive"]!=records["WPC"]["old_positive_received"]):
            return False
        if not retained(positive["whole_received_positive_choice"],candidates):
            return False
        coefficient=p["complete_wce_algebraic_conclusion"]
        cc={"full_ranks":coefficient["complete_full_Calg_upper"],
            "projected_ranks":coefficient["complete_projected_Calg_upper"]}
        return retained(coefficient["complete_whole_choice"],cc)
    except (KeyError,TypeError,ValueError):
        return False

def render(state,science):
    s=science or {}
    failed=state.get("actual_failure") is not None or s.get("failure") is not None
    complete=state.get("complete_mathematical_receipt_available") is True
    lines=[
        "# Actual positive cutoff and reflected coefficient refinement",
        "",
        ("Complete new scalar consequences of the published WPC and WCE formulas." if complete
         else "Execution record for the WPC and WCE formulas; complete new conclusions are not admitted."),
        "The five original PC, TF, WX, WT and SEI successes are immutable inputs.",
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
        "## Complete target bounds",
        "",
        "| Same complete target | Outward record |",
        "|---|---|"]
    pc=s.get("complete_wpc_positive_correction_conclusion") or {}
    ce=s.get("complete_wce_algebraic_conclusion") or {}
    if complete:
        for label,value in (
            ("New complete original cutoff source",pc["complete_cutoff_source_upper"]),
            ("New complete received positive correction",pc["complete_received_positive_candidate_upper"]),
            ("Saved complete positive correction",pc["whole_received_positive_candidates"]["saved_complete_positive"]),
            ("Selected complete positive correction",pc["whole_received_positive_choice"]["complete_selected_upper"]),
            ("Complete D_alg: full primitive ranks",ce["complete_full_Calg_upper"]),
            ("Complete D_alg: actual projected ranks",ce["complete_projected_Calg_upper"]),
            ("Selected complete D_alg",ce["complete_whole_choice"]["complete_selected_upper"])):
            lines.append("| "+cell(label)+" | "+cell(ball(value))+" |")
        lines+=["",
            "Positive selection: "+cell(pc["whole_received_positive_choice"]["selected_label"])+".",
            "Coefficient selection: "+cell(ce["complete_whole_choice"]["selected_label"])+"."]
    lines+=["",
        "## Retained scope",
        "",
        "WPC bounds the same original two-row chi-prime times genuine trial in its ordinary L2_dr H^(-2/3) pair source window, followed by the original complete received gain once. The old volume and finite-head source remain. Its received result is the same Rplus in WUE.",
        "WCE bounds the same D_alg from Xfr_Hminus4_3 to the true reflected meanzero L2 target. Both full primitive ranks are retained before the exact actual-source projection; the physical density-mean row, full TF finite map, two primitives, full density coordinates and actual second waist normalizer remain.",
        ("All seven new graphs are preserved in actual-scientific-conclusion.json. Its 90 scalar slots include retained candidate copies and do not mean 90 independent new targets. Forty-two original bound records, three qualification records and five complete scope collections are copied exactly." if complete
         else "Any completed stage remains in the atomic scientific record when available. Neither complete new target is admitted until every required graph, original record and scope check passes."),
        "The original root finite response remains a distinct exact factor. All negative sources, true jumps, endpoint terms, independent physical means, radial head, metric parameter, other ports and the actual finite border still need their complete matching. These two different operators are not added or treated as an inverse.",
        "No old profile, source integral, exponential sum, matrix word, old scalar product or original scientific producer is recomputed. No native input or historical archive is restored.",
        "This readout supplies no useful high-frequency cutoff, physical incoming inverse, finite determinant, nonlinear background or final surface.",
        "",
        "Complete science and this report are printed before Git publication, together with a separate execution prepublication receipt. Actual pulls, both README checks and exact topic-capacity metadata are retained in execution.json. No new array, artifact or Release is published.",
        ""]
    if failed:
        lines+=[("## Execution failure with complete scientific receipt" if complete else "## Actual incomplete outcome"),"",
            "Worker: "+cell(json.dumps(state.get("actual_failure"),sort_keys=True,ensure_ascii=False)),
            "Science: "+cell(json.dumps(s.get("failure"),sort_keys=True,ensure_ascii=False)),
            "Every completed stage remains in the complete scientific record. An incomplete run does not authorize repeating completed mathematical stages.",""]
    return "\n".join(lines)

def emit_prepublication(state,science):
    report=render(state,science)
    science_raw=None if science is None else compact(science)
    payload=dict(marker="POSITIVE_CUTOFF_REFLECTED_COEFFICIENT_COMPLETE_SCIENTIFIC_PREPUBLICATION_V1",
        source_sha256=state["source_sha256"],manifest_sha256=state["input_manifest_sha256"],
        run_id=state["run_id"],run_attempt=state["run_attempt"],
        actual_returncode=state.get("actual_returncode"),scientific_result=science,report_text=report)
    raw=compact(payload)
    status=dict(marker="POSITIVE_CUTOFF_REFLECTED_COEFFICIENT_PREPUBLICATION_STATUS",
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
        raise ValueError("full positive-cutoff-and-reflected-coefficient-refinement science is saved and printed; prepublication payload exceeds90000")
    print(raw.decode(),end="",flush=True)
    process=compact(dict(marker="POSITIVE_CUTOFF_REFLECTED_COEFFICIENT_EXECUTION_PREPUBLICATION_V1",execution=state))
    if len(process)>59000:
        raise ValueError("full positive-cutoff-and-reflected-coefficient-refinement science is preserved; execution metadata exceeds59000")
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
        raise RuntimeError("only this public repository Actions may evaluate new positive-cutoff-and-reflected-coefficient-refinement mathematics")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:
        raise ValueError("the separately pinned positive-cutoff-and-reflected-coefficient-refinement manifest or reviewed rules changed")
    m=read(a.manifest);rules=read(a.rules)
    current=m.get("files",[])
    history=m.get("historical_inputs",[])
    current_roles={v["role"] for v in current}
    current_paths={v["path"] for v in current}
    historical_roles={v["role"] for v in history}
    historical_paths={v["path"] for v in history}
    all_entries=current+history
    if (m.get("public_repository")!=PUBLIC or rules.get("repository")!=PUBLIC
        or m.get("kind")!="positive_cutoff_and_reflected_coefficient_refinement_public_inputs_v1"
        or m.get("source_sha256")!=a.pipeline_sha
        or m.get("source_path")!=str(PIPELINE)
        or m.get("parameters")!=SCIENCE_PARAMETERS
        or m.get("scope")!=SCIENCE_SCOPE
        or current_roles!=(set(SCIENCE_PIN_SHA256)|{"source","worker","rules"})
        or m.get("complete_input_bytes")!=sum(v["bytes"] for v in current)
        or m.get("publication_limits")!=PUBLICATION_LIMITS
        or m.get("mathematical_input_sha256")!=SCIENCE_PIN_SHA256
        or m.get("expected_actual_gate_count")!=22
        or m.get("expected_current_input_count")!=10
        or m.get("expected_input_count")!=10
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
        raise ValueError("the exact ten-current-text positive cutoff and reflected coefficient contract changed")
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
        raise ValueError("temporary positive-cutoff-and-reflected-coefficient-refinement work and outcome directories are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():
        raise FileExistsError("preserve the previous complete or partial positive-cutoff-and-reflected-coefficient-refinement run")
    if any(v.is_relative_to(root) for v in (work,out)):
        raise ValueError("all new numerical arrays must remain outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__)
    state=dict(kind="actual_public_positive_cutoff_and_reflected_coefficient_refinement_execution_v1",repository=PUBLIC,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_commit=os.environ["GITHUB_SHA"],worker_source_sha256=ws,
        source_sha256=a.pipeline_sha,input_manifest_sha256=a.manifest_sha,
        reviewed_rules_sha256=a.rules_sha,explicitly_read_rules_commit=rules["read_commit"],
        started_utc=utc(),complete=False,actual_returncode=None,readme_checks=[],
        actual_new_scientific_processes=0,old_numerical_enclosures_recomputed=0,
        old_PC_cutoff_profiles_or_exponential_sums_recomputed=0,
        old_TF_WX_WT_SEI_targets_recomputed=0,old_completed_scalar_products_recomputed=0,
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
            raise ValueError("a pinned positive-cutoff-and-reflected-coefficient-refinement source manifest or rule record changed during pull")
        if sha(root/rw)!=ws:
            raise ValueError("the currently running immutable positive-cutoff-and-reflected-coefficient-refinement wrapper changed")
        for name in m["current_input_paths"]:
            if sha(root/relpath(name))!=m["file_sha256"][name]:
                raise ValueError("an immutable current positive-cutoff-and-reflected-coefficient-refinement source or contract changed")
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
        print(json.dumps(dict(kind="POSITIVE_CUTOFF_REFLECTED_COEFFICIENT_DEFERRED_READ_ONLY_METADATA_PUBLICATION",**event,
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
            raise ValueError("each current positive-cutoff-and-reflected-coefficient-refinement input must be complete small current text")
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
                raise RuntimeError("same positive cutoff and reflected coefficient arithmetic has a prior incomplete outcome; require its concrete review and preserved scientific-result review")
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
            raise ValueError("the complete positive cutoff and reflected coefficient input and Python AST closure differs")
        if history or state.get("old_binary_parts_restored")!=0:
            raise ValueError("the positive cutoff and reflected coefficient consumer must not restore old native inputs")
        state["old_artifacts_downloaded"]=0
        state["old_producers_or_integrals_reexecuted"]=0
        state["new_artifact_count"]=0;state["new_Release_count"]=0
        cmd=[sys.executable,"-u",str(work/PIPELINE),"--repo",str(work),
            "--manifest",str(tm),"--manifest-sha",a.manifest_sha,"--bits","320",
            "--out",str(out/"actual-scientific-conclusion.json")]
        for role,digest in pins.items():
            if index_files[role]["sha256"]!=digest:
                raise ValueError("one complete positive cutoff and reflected coefficient mathematical input identity changed")
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
            dict(type="IncompleteScientificReceipt",message="the complete positive cutoff and reflected coefficient scalar receipt did not validate"))
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
        print(json.dumps(dict(kind="POSITIVE_CUTOFF_REFLECTED_COEFFICIENT_ATOMIC_SCIENCE_REPRINT",
            bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())),flush=True)
        print("POSITIVE_CUTOFF_REFLECTED_COEFFICIENT_SCIENTIFIC_RESULT_BEGIN",flush=True)
        print(raw.decode(),end="",flush=True)
        print("POSITIVE_CUTOFF_REFLECTED_COEFFICIENT_SCIENTIFIC_RESULT_END",flush=True)
        state["complete_atomic_scientific_result_reprinted"]=True
    outputs=[out/name for name in ("actual-scientific-conclusion.json","new-scientific-child.stdout.log")]
    state["output_hashes"]=[rec(path,out) for path in outputs if path.is_file()]
    if proc is not None:
        original=out/"actual-scientific-conclusion.json"
        if original.read_bytes()!=compact(proc):
            raise ValueError("the complete positive-cutoff-and-reflected-coefficient-refinement child science must retain its original canonical bytes")
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
            git("commit","-m","visible-exact: record complete positive cutoff and reflected coefficient refinement")
        while True:
            result=git("push","origin","HEAD:refs/heads/main",check=False)
            if result.returncode==0:
                return owned
            if not any(v in result.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
                raise RuntimeError("small positive-cutoff-and-reflected-coefficient-refinement conclusion push failed outside concurrent-main rebase")
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
