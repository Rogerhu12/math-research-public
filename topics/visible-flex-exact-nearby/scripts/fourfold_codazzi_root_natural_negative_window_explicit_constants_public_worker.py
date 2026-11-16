#!/usr/bin/env python3
"""Compute only new explicit natural-window constants from the immutable complete root97 receipt."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import urllib.error,urllib.request,select,importlib.metadata
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_root_natural_negative_window_explicit_constants.py"
REPORTS=TOPIC/"notes/root_natural_negative_window_explicit_constants_ci"
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

PUBLICATION_LIMITS=json.loads("{\"complete_science_bytes\":75000,\"complete_report_bytes\":8000,\"complete_prepublication_science_report_payload_bytes\":90000,\"complete_execution_bytes\":59000,\"pre_science_topic_reserve_bytes\":150000,\"scientific_file_atomic_and_complete_stdout_before_size_guards\":true,\"new_artifacts\":0,\"new_Releases\":0}")
SCIENCE_FIELDS=json.loads("[\"kind\",\"complete\",\"proved\",\"actual_returncode\",\"failure\",\"stage\",\"source_sha256\",\"input_manifest_sha256\",\"public_repository\",\"run_id\",\"run_attempt\",\"workflow_event_commit\",\"actual_scientific_checkout_commit\",\"runtime\",\"arithmetic_bits\",\"parameters\",\"input_sha256\",\"verified_original_inputs\",\"accepted_old_inputs\",\"complete_original_objects_read_verbatim\",\"complete_original_objects_sha256\",\"complete_saved_scalar_records_read_verbatim\",\"complete_saved_scalar_records_sha256\",\"complete_geometry_conclusion\",\"complete_L_commutator_conclusion\",\"complete_J_gain_conclusion\",\"complete_weighted_R0_conclusion\",\"complete_amplitude_gain_conclusion\",\"complete_stable_gain_conclusion\",\"complete_natural_inverse_conclusion\",\"retained_scope\",\"planned_shape\",\"actual_progress\",\"gates\",\"actual_mathematical_wall_seconds\"]")
SCIENCE_GATE_NAMES=json.loads("[\"actual public Actions runtime and the frozen new source are exact\",\"nine current small texts and the complete new parameter closure are frozen\",\"all six mathematical primaries have their complete original bytes SHA and Git identity\",\"the original recovery science and execution are matching complete actual identities\",\"the original nine gates strict true result and zero rerun counters are inherited\",\"four original objects and twenty three scalar records are preserved with typed endpoints\",\"four complete commutator Sobolev bounds retain the physical angular normalization\",\"the same direction J bootstrap retains both complete L2 candidates and all four windows\",\"both weighted R0 routes keep every one of the eight original positive terms and the mean rank\",\"all four amplitude gains retain double high projection and original input powers\",\"four complete E gains keep ordered J L and the full low output primitive one quarter\",\"both natural negative inverses use the saved positive gap and separate finite products\",\"all original objects and inputs stay unchanged with zero old comparison evaluation\",\"all complete new ball records and every positive finite formula are retained\",\"new scalar counts and actual completion progress match the complete target\",\"the complete thirty five field schema preserves the same inverse and every retained port\"]")
SCIENCE_PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"expected_actual_gate_count\":16,\"original_R97R_run\":\"43789221154/1\",\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_intrinsic_parameter\":\"-7789843107295549/4611686018427387904\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"physical_root_piece\":2549,\"physical_period\":\"pi/2\",\"normalized_angular_measure\":true,\"physical_frequency\":\"n=4|j|\",\"input_cutoff_abs_j\":97,\"physical_minimum_frequency\":388,\"natural_negative_windows\":[\"-7/6\",\"-5/2\"],\"ordered_gain_windows\":[\"-5/2\",\"-11/6\",\"-7/6\",\"-1/2\"],\"stable_error_gain\":\"2/3\",\"R0_complete_kernel_bandwidths\":[192,384,576,192,384,384,0,576],\"weighted_R0_output_cutoffs\":[1,97],\"complete_primitive_one_gain\":\"sqrt(17)/4\",\"physical_independent_means\":2,\"expected_current_inputs\":9,\"expected_total_inputs\":9,\"expected_Python_AST_files\":3,\"expected_historical_inputs\":0,\"saved_complete_objects\":4,\"saved_scalar_records\":23,\"old_target_calls_allowed\":0,\"old_source_imports_allowed\":0,\"old_strict_comparisons_reevaluated\":0,\"full_complex_parameter_square_claimed\":false,\"uniform_selected_chart_family_claimed\":false,\"complete_incoming_or_finite_Schur_inverse_claimed\":false}")
SCIENCE_SCOPE=json.loads("{\"scientific_target\":\"explicit uniform natural negative-window inverse constants for the actual original root97 stable operator\",\"same_real_delta_family_and_fixed_intrinsic_eta0\":true,\"original_reflection_and_two_carrier_signs_retained\":true,\"physical_fourier_factor_four_and_normalized_measure_retained\":true,\"complete_positive_R0_mean_rank_retained\":true,\"independent_physical_mean_coordinates\":2,\"full_low_intermediate_primitive_one_quarter_retained\":true,\"L_and_J_not_assigned_new_finite_bandwidth\":true,\"original_J1_is_left_angular_derivative\":true,\"J_negative_windows_use_same_direction_finite_bootstrap\":true,\"input_frequency_diagonals_kept_in_original_order\":true,\"old_scalar_upper_bounds_used_only_with_exact_positive_kernel_qualification\":true,\"saved_positive_strict_margin_read_only\":true,\"old_R97_graphs_and_comparison_not_recomputed\":true,\"same_distributional_inverse_in_both_natural_windows\":true,\"true_Riccati_frame_used_only_through_uniform_bounds_and_strong_realization\":true,\"Riccati_operator_norm_continuity_claimed\":false,\"uniform_selected_chart_family_claimed\":false,\"physical_bulk_Poisson_extension_claimed\":false,\"complete_incoming_inverse_claimed\":false,\"finite_Schur_inverse_claimed\":false,\"nonlinear_background_or_final_surface_claimed\":false,\"original_low_complement_radial_head_sources_and_all_other_finite_ports_retained\":true}")
SCIENCE_PLANNED_SHAPE=json.loads("{\"saved_actual_receipts\":1,\"saved_complete_objects\":4,\"saved_scalar_records\":23,\"new_L_commutator_bounds\":4,\"new_complete_J_L2_candidates\":2,\"new_J_gain_windows\":4,\"new_weighted_R0_routes\":8,\"new_weighted_R0_positive_terms\":64,\"new_amplitude_gain_windows\":4,\"new_amplitude_gain_positive_terms\":8,\"new_stable_gain_windows\":4,\"new_stable_gain_positive_terms\":12,\"new_natural_inverse_windows\":2,\"new_finite_inverse_polynomial_terms\":8,\"new_complete_whole_choices\":1,\"new_geometric_rational_powers\":26,\"new_fixed_square_roots\":4,\"retained_physical_means\":2}")
SCIENCE_PIN_SHA256=json.loads("{\"contract\":\"030e434ed31632c0c5330318251486d37424deba78f3fe35bf8b738960425120\",\"rni_contract\":\"d771cf43faa0d5351851168f9f1567e21f8b7e0be27480b6bd67880a4eb69a81\",\"saved_science\":\"0c27195fad92a0be1296e533594fae8df46f4f70a6af359e762374141ac770ea\",\"saved_execution\":\"a83f20c1b541173c871aee990b6797d9b76ecd9f1c831cbfac719900c18e379f\",\"saved_source\":\"799b7faa1d2a72374b591561fefeb446099f3d27fe47b2d6ddbd4ae21b6d2534\",\"saved_manifest\":\"5d993fefa9cbd2935812d051c4a83a0ff0d4e607d2836ea69d7a93423beb633e\"}")
SCIENCE_PIN_BYTES=json.loads("{\"contract\":17890,\"rni_contract\":19405,\"saved_science\":56630,\"saved_execution\":11832,\"saved_source\":61957,\"saved_manifest\":13656}")
SUCCESS_ACTUAL_PROGRESS=json.loads("{\"accepted_same_R97R_success\":true,\"new_commutator_bounds_completed\":4,\"new_complete_J_candidates_completed\":2,\"new_same_direction_J_windows_completed\":4,\"new_weighted_R0_routes_completed\":8,\"new_amplitude_gain_windows_completed\":4,\"new_stable_gain_windows_completed\":4,\"new_natural_inverse_windows_completed\":2,\"new_complete_whole_choices\":1,\"new_geometric_rational_powers_completed\":26,\"new_fixed_sqrt_constants_completed\":4,\"old_scientific_targets_recomputed\":0,\"old_R97_root_graphs_recomputed\":0,\"old_R97_strict_comparisons_reevaluated\":0,\"historical_inputs_restored\":0}")
SCIENTIFIC_GRAPH_SHAPES=json.loads("{\"complete_geometry_conclusion\":{\"fixed_square_roots\":{\"sqrt2\":\"__FINITE_SCALAR__\",\"sqrt3\":\"__FINITE_SCALAR__\",\"sqrt17\":\"__FINITE_SCALAR__\",\"sqrt67\":\"__FINITE_SCALAR__\"},\"positive_geometric_powers\":{\"192/1|5/2\":{\"base\":\"193\",\"exponent\":\"5/2\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"384/1|5/2\":{\"base\":\"385\",\"exponent\":\"5/2\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"576/1|5/2\":{\"base\":\"577\",\"exponent\":\"5/2\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"192/97|5/2\":{\"base\":\"289/97\",\"exponent\":\"5/2\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"384/97|5/2\":{\"base\":\"481/97\",\"exponent\":\"5/2\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"576/97|5/2\":{\"base\":\"673/97\",\"exponent\":\"5/2\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"192/1|11/6\":{\"base\":\"193\",\"exponent\":\"11/6\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"384/1|11/6\":{\"base\":\"385\",\"exponent\":\"11/6\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"576/1|11/6\":{\"base\":\"577\",\"exponent\":\"11/6\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"192/97|11/6\":{\"base\":\"289/97\",\"exponent\":\"11/6\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"384/97|11/6\":{\"base\":\"481/97\",\"exponent\":\"11/6\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"576/97|11/6\":{\"base\":\"673/97\",\"exponent\":\"11/6\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"192/1|7/6\":{\"base\":\"193\",\"exponent\":\"7/6\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"384/1|7/6\":{\"base\":\"385\",\"exponent\":\"7/6\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"576/1|7/6\":{\"base\":\"577\",\"exponent\":\"7/6\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"192/97|7/6\":{\"base\":\"289/97\",\"exponent\":\"7/6\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"384/97|7/6\":{\"base\":\"481/97\",\"exponent\":\"7/6\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"576/97|7/6\":{\"base\":\"673/97\",\"exponent\":\"7/6\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"192/1|1/2\":{\"base\":\"193\",\"exponent\":\"1/2\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"384/1|1/2\":{\"base\":\"385\",\"exponent\":\"1/2\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"576/1|1/2\":{\"base\":\"577\",\"exponent\":\"1/2\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"192/97|1/2\":{\"base\":\"289/97\",\"exponent\":\"1/2\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"384/97|1/2\":{\"base\":\"481/97\",\"exponent\":\"1/2\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"576/97|1/2\":{\"base\":\"673/97\",\"exponent\":\"1/2\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"rho97|1/3\":{\"base\":\"150545\",\"exponent\":\"1/3\",\"complete_upper\":\"__FINITE_SCALAR__\"},\"384/97|1/6\":{\"base\":\"481/97\",\"exponent\":\"1/6\",\"complete_upper\":\"__FINITE_SCALAR__\"}},\"old_frequency_power_is_read_verbatim_not_recomputed\":true,\"complete_CI_upper\":\"__FINITE_SCALAR__\",\"complete_rho_upper\":\"__FINITE_SCALAR__\",\"complete_chi_upper\":\"__FINITE_SCALAR__\"},\"complete_L_commutator_conclusion\":{\"integer_orders\":[0,1,2,3],\"complete_positive_terms\":[[\"__FINITE_SCALAR__\"],[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"]],\"complete_integer_Sobolev_bounds\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"ordinary_angular_derivative_has_physical_frequency_four\":true,\"same_bounds_for_L_and_its_adjoint\":true,\"negative_L_windows_follow_duality_and_interpolation\":true,\"no_finite_band_assumption_for_L_or_J\":true},\"complete_J_gain_conclusion\":{\"complete_P0_upper\":\"__FINITE_SCALAR__\",\"complete_BJ_whole_choice\":{\"complete_candidate_records\":{\"original_left_derivative\":\"__FINITE_SCALAR__\",\"complete_identity_minus_LJ\":\"__FINITE_SCALAR__\"},\"selected_complete_candidate\":\"__BJ_WHOLE_CHOICE__\",\"complete_selected_upper\":\"__FINITE_SCALAR__\",\"comparison_uses_complete_final_record_upper_endpoints\":true,\"first_candidate_wins_exact_ties\":true,\"all_candidates_bound_the_same_complete_operator_and_window\":true},\"complete_R1_upper\":\"__FINITE_SCALAR__\",\"complete_R2_upper\":\"__FINITE_SCALAR__\",\"windows\":{\"-5/2\":{\"input_exponent\":\"-5/2\",\"output_exponent\":\"-3/2\",\"intermediate_R_output_exponents\":[\"-3/2\",\"-1/2\",\"1/2\"],\"complete_positive_bracket_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_J_one_gain_upper\":\"__FINITE_SCALAR__\"},\"-11/6\":{\"input_exponent\":\"-11/6\",\"output_exponent\":\"-5/6\",\"intermediate_R_output_exponents\":[\"-5/6\",\"1/6\"],\"complete_positive_bracket_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_J_one_gain_upper\":\"__FINITE_SCALAR__\"},\"-7/6\":{\"input_exponent\":\"-7/6\",\"output_exponent\":\"-1/6\",\"intermediate_R_output_exponents\":[\"-1/6\",\"5/6\"],\"complete_positive_bracket_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_J_one_gain_upper\":\"__FINITE_SCALAR__\"},\"-1/2\":{\"input_exponent\":\"-1/2\",\"output_exponent\":\"1/2\",\"intermediate_R_output_exponents\":[\"1/2\"],\"complete_positive_bracket_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_J_one_gain_upper\":\"__FINITE_SCALAR__\"}},\"exact_L2_inverse\":\"(Id+L eta^-1 I)^-1 = eta partial_phi J\",\"J_is_same_direction_old_inverse_not_the_adjoint_inverse\":true,\"left_derivative_identity_retained\":true,\"independent_physical_means_not_in_J_domain\":true},\"complete_weighted_R0_conclusion\":{\"complete_kernel_bandwidths\":[192,384,576,192,384,384,0,576],\"windows\":{\"-5/2\":{\"1\":{\"input_exponent\":\"-5/2\",\"output_exponent\":\"-5/2\",\"input_cutoff_abs_j\":97,\"output_cutoff_abs_j\":1,\"complete_positive_weights\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_weighted_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_R0_upper\":\"__FINITE_SCALAR__\",\"complete_positive_mean_rank\":\"__FINITE_SCALAR__\",\"original_eight_terms_all_retained\":true},\"97\":{\"input_exponent\":\"-5/2\",\"output_exponent\":\"-5/2\",\"input_cutoff_abs_j\":97,\"output_cutoff_abs_j\":97,\"complete_positive_weights\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_weighted_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_R0_upper\":\"__FINITE_SCALAR__\",\"complete_positive_mean_rank\":\"__FINITE_SCALAR__\",\"original_eight_terms_all_retained\":true}},\"-11/6\":{\"1\":{\"input_exponent\":\"-11/6\",\"output_exponent\":\"-11/6\",\"input_cutoff_abs_j\":97,\"output_cutoff_abs_j\":1,\"complete_positive_weights\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_weighted_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_R0_upper\":\"__FINITE_SCALAR__\",\"complete_positive_mean_rank\":\"__FINITE_SCALAR__\",\"original_eight_terms_all_retained\":true},\"97\":{\"input_exponent\":\"-11/6\",\"output_exponent\":\"-11/6\",\"input_cutoff_abs_j\":97,\"output_cutoff_abs_j\":97,\"complete_positive_weights\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_weighted_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_R0_upper\":\"__FINITE_SCALAR__\",\"complete_positive_mean_rank\":\"__FINITE_SCALAR__\",\"original_eight_terms_all_retained\":true}},\"-7/6\":{\"1\":{\"input_exponent\":\"-7/6\",\"output_exponent\":\"-7/6\",\"input_cutoff_abs_j\":97,\"output_cutoff_abs_j\":1,\"complete_positive_weights\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_weighted_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_R0_upper\":\"__FINITE_SCALAR__\",\"complete_positive_mean_rank\":\"__FINITE_SCALAR__\",\"original_eight_terms_all_retained\":true},\"97\":{\"input_exponent\":\"-7/6\",\"output_exponent\":\"-7/6\",\"input_cutoff_abs_j\":97,\"output_cutoff_abs_j\":97,\"complete_positive_weights\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_weighted_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_R0_upper\":\"__FINITE_SCALAR__\",\"complete_positive_mean_rank\":\"__FINITE_SCALAR__\",\"original_eight_terms_all_retained\":true}},\"-1/2\":{\"1\":{\"input_exponent\":\"-1/2\",\"output_exponent\":\"-1/2\",\"input_cutoff_abs_j\":97,\"output_cutoff_abs_j\":1,\"complete_positive_weights\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_weighted_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_R0_upper\":\"__FINITE_SCALAR__\",\"complete_positive_mean_rank\":\"__FINITE_SCALAR__\",\"original_eight_terms_all_retained\":true},\"97\":{\"input_exponent\":\"-1/2\",\"output_exponent\":\"-1/2\",\"input_cutoff_abs_j\":97,\"output_cutoff_abs_j\":97,\"complete_positive_weights\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_weighted_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_R0_upper\":\"__FINITE_SCALAR__\",\"complete_positive_mean_rank\":\"__FINITE_SCALAR__\",\"original_eight_terms_all_retained\":true}}},\"exact_positive_A0_kernel_algorithm_qualification\":true,\"internal_mean_rank_has_complete_convolution_majorant\":true,\"ordinary_operator_norm_alone_not_used_to_infer_weighted_kernel\":true,\"independent_physical_means_retained\":true},\"complete_amplitude_gain_conclusion\":{\"windows\":{\"-5/2\":{\"input_exponent\":\"-5/2\",\"output_exponent\":\"-11/6\",\"complete_high_high_weight_upper\":\"__FINITE_SCALAR__\",\"complete_positive_gain_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_amplitude_gain_upper\":\"__FINITE_SCALAR__\"},\"-11/6\":{\"input_exponent\":\"-11/6\",\"output_exponent\":\"-7/6\",\"complete_high_high_weight_upper\":\"__FINITE_SCALAR__\",\"complete_positive_gain_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_amplitude_gain_upper\":\"__FINITE_SCALAR__\"},\"-7/6\":{\"input_exponent\":\"-7/6\",\"output_exponent\":\"-1/2\",\"complete_high_high_weight_upper\":\"__FINITE_SCALAR__\",\"complete_positive_gain_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_amplitude_gain_upper\":\"__FINITE_SCALAR__\"},\"-1/2\":{\"input_exponent\":\"-1/2\",\"output_exponent\":\"1/6\",\"complete_high_high_weight_upper\":\"__FINITE_SCALAR__\",\"complete_positive_gain_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_amplitude_gain_upper\":\"__FINITE_SCALAR__\"}},\"input_and_output_cutoff_abs_j\":97,\"old_two_amplitude_terms_are_complete_positive_algorithm_bounds\":true,\"input_frequency_powers_retained_on_the_right\":true,\"physical_frequency_monotonicity_used_only_for_the_two_saved_powers\":true,\"no_unweighted_column_norm_promoted_without_kernel_identity\":true},\"complete_stable_gain_conclusion\":{\"windows\":{\"-5/2\":{\"input_exponent\":\"-5/2\",\"output_exponent\":\"-11/6\",\"L_integer_order\":3,\"complete_full_IR0_upper\":\"__FINITE_SCALAR__\",\"complete_leading_plus_IR0_upper\":\"__FINITE_SCALAR__\",\"complete_ordered_JL_upper\":\"__FINITE_SCALAR__\",\"complete_three_positive_error_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_error_gain_upper\":\"__FINITE_SCALAR__\",\"original_low_intermediate_one_quarter_retained\":true},\"-11/6\":{\"input_exponent\":\"-11/6\",\"output_exponent\":\"-7/6\",\"L_integer_order\":2,\"complete_full_IR0_upper\":\"__FINITE_SCALAR__\",\"complete_leading_plus_IR0_upper\":\"__FINITE_SCALAR__\",\"complete_ordered_JL_upper\":\"__FINITE_SCALAR__\",\"complete_three_positive_error_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_error_gain_upper\":\"__FINITE_SCALAR__\",\"original_low_intermediate_one_quarter_retained\":true},\"-7/6\":{\"input_exponent\":\"-7/6\",\"output_exponent\":\"-1/2\",\"L_integer_order\":2,\"complete_full_IR0_upper\":\"__FINITE_SCALAR__\",\"complete_leading_plus_IR0_upper\":\"__FINITE_SCALAR__\",\"complete_ordered_JL_upper\":\"__FINITE_SCALAR__\",\"complete_three_positive_error_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_error_gain_upper\":\"__FINITE_SCALAR__\",\"original_low_intermediate_one_quarter_retained\":true},\"-1/2\":{\"input_exponent\":\"-1/2\",\"output_exponent\":\"1/6\",\"L_integer_order\":1,\"complete_full_IR0_upper\":\"__FINITE_SCALAR__\",\"complete_leading_plus_IR0_upper\":\"__FINITE_SCALAR__\",\"complete_ordered_JL_upper\":\"__FINITE_SCALAR__\",\"complete_three_positive_error_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_error_gain_upper\":\"__FINITE_SCALAR__\",\"original_low_intermediate_one_quarter_retained\":true}},\"exact_order\":\"P_H E2 - eta^-1 P_H N_out^-2/3 R0 + P_H Z N_out^1/3 J L eta^-1 I R\",\"J_and_L_not_given_a_finite_output_band\":true,\"all_original_input_diagonals_remain_on_their_original_side\":true,\"internal_mean_rank_and_both_physical_means_retained\":true,\"final_N_one_third_reads_Hqplus1_to_Hqplus2over3\":true},\"complete_natural_inverse_conclusion\":{\"complete_Broot_upper\":\"__FINITE_SCALAR__\",\"complete_A_gain_upper\":{\"-5/2\":\"__FINITE_SCALAR__\",\"-11/6\":\"__FINITE_SCALAR__\",\"-7/6\":\"__FINITE_SCALAR__\",\"-1/2\":\"__FINITE_SCALAR__\"},\"windows\":{\"-7/6\":{\"input_and_output_exponent\":\"-7/6\",\"ordered_gain_windows\":[\"-7/6\",\"-1/2\"],\"terminal_exponent\":\"1/6\",\"complete_finite_inverse_polynomial_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_B_upper\":\"__FINITE_SCALAR__\",\"complete_Shat_inverse_upper\":\"__FINITE_SCALAR__\",\"complete_Snat_inverse_upper\":\"__FINITE_SCALAR__\",\"same_distributional_inverse_as_original_L2\":true},\"-5/2\":{\"input_and_output_exponent\":\"-5/2\",\"ordered_gain_windows\":[\"-5/2\",\"-11/6\",\"-7/6\",\"-1/2\"],\"terminal_exponent\":\"1/6\",\"complete_finite_inverse_polynomial_terms\":[\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\",\"__FINITE_SCALAR__\"],\"complete_B_upper\":\"__FINITE_SCALAR__\",\"complete_Shat_inverse_upper\":\"__FINITE_SCALAR__\",\"complete_Snat_inverse_upper\":\"__FINITE_SCALAR__\",\"same_distributional_inverse_as_original_L2\":true}},\"saved_margin_is_read_directly_no_old_strict_comparison_repeated\":true,\"exact_order\":\"(Id+D_g^-1 E)^-1 D_g^-1 M^-1\",\"uniform_real_delta_family_only\":true,\"two_natural_negative_windows_certified\":true,\"selected_common_input_inverse_left_factor_remains_separate\":true,\"true_Riccati_operator_norm_continuity_claimed\":false,\"uniform_selected_chart_family_claimed\":false,\"complete_incoming_inverse_claimed\":false,\"finite_Schur_inverse_claimed\":false,\"independent_physical_means_retained\":true}}")
FROZEN_ACCEPTED_OLD_INPUTS_SHA256="df661705c26de22aeae2d032d8bc8d270c853a37b0ca2b449cd807083305affb"
FROZEN_ORIGINAL_OBJECTS_SHA256="01cac119904ff63260d1f7d7c3370e49f276b4c88aba2903ce2acae88b7c3313"
FROZEN_SAVED_SCALAR_RECORDS_SHA256="08b04bfb460b3a5c18b85092715d122a65586b1b258a4d1d64ce6928d7f971ed"

def scientific_receipt_valid(proc,source,manifest,parameters,pins,runtime):
    """Accept exactly one complete same-family negative-window consequence, without old arithmetic."""
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
        if expected=="__BJ_WHOLE_CHOICE__":
            return value in ("original_left_derivative","complete_identity_minus_LJ")
        if isinstance(expected,dict):
            return (isinstance(value,dict) and set(value)==set(expected)
                and all(shape(value[k],v) for k,v in expected.items()))
        if isinstance(expected,list):
            return (isinstance(value,list) and len(value)==len(expected)
                and all(shape(a,b) for a,b in zip(value,expected)))
        return type(value) is type(expected) and value==expected
    try:
        if not (set(p)==set(SCIENCE_FIELDS)
            and p["kind"]=="complete_root_natural_negative_window_explicit_constants_v1"
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
        originals=p["complete_original_objects_read_verbatim"]
        scalars=p["complete_saved_scalar_records_read_verbatim"]
        if not (hashlib.sha256(compact(p["accepted_old_inputs"])).hexdigest()==FROZEN_ACCEPTED_OLD_INPUTS_SHA256
            and p["complete_original_objects_sha256"]==FROZEN_ORIGINAL_OBJECTS_SHA256
            and hashlib.sha256(compact(originals)).hexdigest()==FROZEN_ORIGINAL_OBJECTS_SHA256
            and p["complete_saved_scalar_records_sha256"]==FROZEN_SAVED_SCALAR_RECORDS_SHA256
            and hashlib.sha256(compact(scalars)).hexdigest()==FROZEN_SAVED_SCALAR_RECORDS_SHA256):
            return False
        if not all(shape(p[key],expected) for key,expected in SCIENTIFIC_GRAPH_SHAPES.items()):
            return False
        choice=p["complete_J_gain_conclusion"]["complete_BJ_whole_choice"]
        if choice["complete_selected_upper"]!=choice["complete_candidate_records"][choice["selected_complete_candidate"]]:
            return False
        for q in SCIENCE_PARAMETERS["ordered_gain_windows"]:
            for cutoff in ("1","97"):
                row=p["complete_weighted_R0_conclusion"]["windows"][q][cutoff]
                if row["complete_positive_mean_rank"]!=row["complete_weighted_terms"][7]:
                    return False
            amplitude=p["complete_amplitude_gain_conclusion"]["windows"][q]["complete_amplitude_gain_upper"]
            if p["complete_stable_gain_conclusion"]["windows"][q]["complete_three_positive_error_terms"][0]!=amplitude:
                return False
        return True
    except (KeyError,TypeError,ValueError):
        return False

def render(state,science):
    s=science or {}
    ready=s.get("complete") is True and s.get("proved") is True and s.get("stage")=="complete"
    admitted=(s.get("actual_progress",{}) or {}).get("accepted_same_R97R_success") is True
    lines=["# Actual explicit natural negative-window inverse constants","",
        "- Run: "+str(state["run_id"])+"/"+str(state["run_attempt"]),
        "- Actual child return: "+str(state.get("actual_returncode")),
        "- Complete mathematical receipt: "+str(state.get("complete_mathematical_receipt_available",False)),
        "- Source SHA256: "+state["source_sha256"],
        "- Manifest SHA256: "+state["input_manifest_sha256"],
        "- Complete result: [actual-scientific-conclusion.json](actual-scientific-conclusion.json).",
        "- Six immutable mathematical texts and nine current inputs; three Python AST files; zero historical natives.",
        "- Only the new finite positive formulas in RNE are evaluated; old root97 graphs, strict comparison and original scientific targets are not rerun.",
        ("- The complete actual R97R run43789221154/1 is admitted; four complete original objects and all 23 saved scalar records are copied verbatim."
         if admitted else "- Admission of the saved R97R result is incomplete; no inherited mathematical premise is asserted by this record."),""]
    if ready:
        natural=s["complete_natural_inverse_conclusion"]
        lines+=["## Complete natural-window inverse bounds","",
            "| Natural exponent | Same normalized inverse upper | Same natural inverse upper |",
            "|---|---|---|"]
        for q in ("-7/6","-5/2"):
            row=natural["windows"][q]
            lines.append("| "+q+" | "+cell(row["complete_Shat_inverse_upper"])
                +" | "+cell(row["complete_Snat_inverse_upper"])+" |")
        lines+=["","## Complete gain bounds","",
            "| Input exponent | Same-direction J one-gain upper | Complete stable two-thirds-gain upper |",
            "|---|---|---|"]
        for q in SCIENCE_PARAMETERS["ordered_gain_windows"]:
            j=s["complete_J_gain_conclusion"]["windows"][q]
            e=s["complete_stable_gain_conclusion"]["windows"][q]
            lines.append("| "+q+" | "+cell(j["complete_J_one_gain_upper"])
                +" | "+cell(e["complete_error_gain_upper"])+" |")
        choice=s["complete_J_gain_conclusion"]["complete_BJ_whole_choice"]
        lines+=["","- Whole J L2 candidate selected: "+choice["selected_complete_candidate"]+".",
            "- Complete root L2 bootstrap upper: "+cell(natural["complete_Broot_upper"])+".",
            "- Both J L2 candidates, every positive term, all weighted routes and both finite inverse polynomials remain in the complete result.","",
            "These are uniform bounds for the same distributional inverse on the original real "
            "|delta|<=10^(-8), fixed eta0 and admitted root piece. The two negative-window bounds "
            "use their separate finite smoothing chains. Neither is replaced by the ordinary-L2 value.",""]
    else:
        lines+=["No complete new numerical natural-window inverse is asserted by this incomplete record.",""]
    lines+=["## Actual progress","",
        json.dumps(s.get("actual_progress",{}),ensure_ascii=False,sort_keys=True),"",
        "The original nine strict-pass gates are inherited records. The following gates belong only to the new natural-window target.","",
        "## Structural gates",""]
    lines+=["- "+("PASS" if g["passed"] else "FAIL")+": "+g["name"] for g in s.get("gates",[])]
    lines+=["","## Retained domain and operator order","",
        "All eight complete positive R0 terms, their internal mean rank and both independent physical "
        "mean equations are retained. The intermediate primitive uses its full1/4 bound. No finite "
        "bandwidth is assigned to J or L; all input frequency diagonals keep their original side.","",
        "The true Riccati frame enters through its established uniform bounds and strong realization. "
        "The selected common-input chart and its left inverse factor require their separate qualification. "
        "No full-parameter selected chart, physical bulk Poisson extension, complete incoming inverse, "
        "finite Schur inverse, nonlinear background or final surface is claimed. Old low complements, "
        "radial heads, independent inputs and every other finite port remain.",""]
    if state.get("actual_failure"):
        lines+=["## Actual failure","",json.dumps(state["actual_failure"],ensure_ascii=False,sort_keys=True),""]
    lines+=["## Latest actual README pulls","",
        "The complete pull and diff history is in execution.json; total records: "
        +str(len(state.get("readme_checks",[])))+".",""]
    for row in state.get("readme_checks",[])[-2:]:
        lines.append("- "+row["time"]+" -> "+row["after"]+"; README diff empty: "+str(row["actual_diff"]==""))
    return "\n".join(lines)+"\n"

def emit_prepublication(state,science):
    report=render(state,science)
    science_raw=None if science is None else compact(science)
    payload=dict(marker="ROOT_NATURAL_NEGATIVE_WINDOW_EXPLICIT_CONSTANTS_COMPLETE_SCIENTIFIC_PREPUBLICATION_V1",
        source_sha256=state["source_sha256"],manifest_sha256=state["input_manifest_sha256"],
        run_id=state["run_id"],run_attempt=state["run_attempt"],
        actual_returncode=state.get("actual_returncode"),scientific_result=science,report_text=report)
    raw=compact(payload)
    status=dict(marker="ROOT_NATURAL_NEGATIVE_WINDOW_EXPLICIT_CONSTANTS_PREPUBLICATION_STATUS",
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
        raise ValueError("full root-natural-negative-window-explicit-constants science is saved and printed; prepublication payload exceeds90000")
    print(raw.decode(),end="",flush=True)
    process=compact(dict(marker="ROOT_NATURAL_NEGATIVE_WINDOW_EXPLICIT_CONSTANTS_EXECUTION_PREPUBLICATION_V1",execution=state))
    if len(process)>59000:
        raise ValueError("full root-natural-negative-window-explicit-constants science is preserved; execution metadata exceeds59000")
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
        raise RuntimeError("only this public repository Actions may evaluate new root-natural-negative-window-explicit-constants mathematics")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:
        raise ValueError("the separately pinned root-natural-negative-window-explicit-constants manifest or reviewed rules changed")
    m=read(a.manifest);rules=read(a.rules)
    current=m.get("files",[])
    history=m.get("historical_inputs",[])
    current_roles={v["role"] for v in current}
    current_paths={v["path"] for v in current}
    historical_roles={v["role"] for v in history}
    historical_paths={v["path"] for v in history}
    all_entries=current+history
    if (m.get("public_repository")!=PUBLIC or rules.get("repository")!=PUBLIC
        or m.get("kind")!="root_natural_negative_window_explicit_constants_public_inputs_v1"
        or m.get("source_sha256")!=a.pipeline_sha
        or m.get("source_path")!=str(PIPELINE)
        or m.get("parameters")!=SCIENCE_PARAMETERS
        or m.get("publication_limits")!=PUBLICATION_LIMITS
        or m.get("mathematical_input_sha256")!=SCIENCE_PIN_SHA256
        or m.get("expected_actual_gate_count")!=16
        or m.get("expected_current_input_count")!=9
        or m.get("expected_input_count")!=9
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
        or m.get("old_successful_scientific_calls_allowed") is not False
        or m.get("new_native_arrays_or_artifact_persistence_allowed") is not False):
        raise ValueError("the exact nine-current-text natural negative-window contract changed")
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
        raise ValueError("temporary root-natural-negative-window-explicit-constants work and outcome directories are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():
        raise FileExistsError("preserve the previous complete or partial root-natural-negative-window-explicit-constants run")
    if any(v.is_relative_to(root) for v in (work,out)):
        raise ValueError("all new numerical arrays must remain outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__)
    state=dict(kind="actual_public_root_natural_negative_window_explicit_constants_execution_v1",repository=PUBLIC,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_commit=os.environ["GITHUB_SHA"],worker_source_sha256=ws,
        source_sha256=a.pipeline_sha,input_manifest_sha256=a.manifest_sha,
        reviewed_rules_sha256=a.rules_sha,explicitly_read_rules_commit=rules["read_commit"],
        started_utc=utc(),complete=False,actual_returncode=None,readme_checks=[],
        actual_new_scientific_processes=0,old_numerical_enclosures_recomputed=0,
        old_R97_root_graphs_recomputed=0,old_R97_strict_comparisons_reevaluated=0,
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
            raise ValueError("a pinned root-natural-negative-window-explicit-constants source manifest or rule record changed during pull")
        if sha(root/rw)!=ws:
            raise ValueError("the currently running immutable root-natural-negative-window-explicit-constants wrapper changed")
        for name in m["current_input_paths"]:
            if sha(root/relpath(name))!=m["file_sha256"][name]:
                raise ValueError("an immutable current root-natural-negative-window-explicit-constants source or contract changed")
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
        print(json.dumps(dict(kind="ROOT_NATURAL_NEGATIVE_WINDOW_EXPLICIT_CONSTANTS_DEFERRED_READ_ONLY_METADATA_PUBLICATION",**event,
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
            raise ValueError("each current root-natural-negative-window-explicit-constants input must be complete small current text")
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
                raise RuntimeError("same natural negative-window arithmetic has a prior incomplete outcome; require its concrete review and preserved scientific-result review")
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
            raise ValueError("the complete natural-window input and Python AST closure differs")
        if history or state.get("old_binary_parts_restored")!=0:
            raise ValueError("the natural-window consumer must not restore old native inputs")
        state["old_artifacts_downloaded"]=0
        state["old_producers_or_integrals_reexecuted"]=0
        state["new_artifact_count"]=0;state["new_Release_count"]=0
        cmd=[sys.executable,"-u",str(work/PIPELINE),"--repo",str(work),
            "--manifest",str(tm),"--manifest-sha",a.manifest_sha,"--bits","320",
            "--out",str(out/"actual-scientific-conclusion.json")]
        for role,digest in pins.items():
            if index_files[role]["sha256"]!=digest:
                raise ValueError("one complete natural-window mathematical input identity changed")
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
            dict(type="IncompleteScientificReceipt",message="the complete natural negative-window scalar receipt did not validate"))
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
        print(json.dumps(dict(kind="ROOT_NATURAL_NEGATIVE_WINDOW_EXPLICIT_CONSTANTS_ATOMIC_SCIENCE_REPRINT",
            bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())),flush=True)
        print("ROOT_NATURAL_NEGATIVE_WINDOW_EXPLICIT_CONSTANTS_SCIENTIFIC_RESULT_BEGIN",flush=True)
        print(raw.decode(),end="",flush=True)
        print("ROOT_NATURAL_NEGATIVE_WINDOW_EXPLICIT_CONSTANTS_SCIENTIFIC_RESULT_END",flush=True)
        state["complete_atomic_scientific_result_reprinted"]=True
    outputs=[out/name for name in ("actual-scientific-conclusion.json","new-scientific-child.stdout.log")]
    state["output_hashes"]=[rec(path,out) for path in outputs if path.is_file()]
    if proc is not None:
        original=out/"actual-scientific-conclusion.json"
        if original.read_bytes()!=compact(proc):
            raise ValueError("the complete root-natural-negative-window-explicit-constants child science must retain its original canonical bytes")
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
            git("commit","-m","visible-exact: record complete natural negative-window inverse constants")
        while True:
            result=git("push","origin","HEAD:refs/heads/main",check=False)
            if result.returncode==0:
                return owned
            if not any(v in result.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
                raise RuntimeError("small root-natural-negative-window-explicit-constants conclusion push failed outside concurrent-main rebase")
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
