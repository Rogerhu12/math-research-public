#!/usr/bin/env python3
"""Run the new WGS finite-jet graph once; retain complete separate original-input evidence."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import urllib.error,urllib.request,select,importlib.metadata
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_global_fold_free_transport_finite_jets.py"
REPORTS=TOPIC/"notes/global_fold_free_transport_finite_jets_ci"
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
            raise ValueError("an unpublished local topic change is outside the four owned small conclusions")
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
            limit={"actual-scientific-conclusion.json":PUBLICATION_LIMITS["complete_science_max_bytes"],
                "complete-original-inputs.json":PUBLICATION_LIMITS["complete_original_inputs_max_bytes"],
                "report.md":PUBLICATION_LIMITS["complete_report_max_bytes"],
                "execution.json":PUBLICATION_LIMITS["complete_execution_max_bytes"]}[Path(name).name]
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

PUBLICATION_LIMITS=json.loads('{"all_four_preGit_payloads_are_complete_separate_files":true,"complete_execution_max_bytes":59000,"complete_original_inputs_max_bytes":50000,"complete_preGit_execution_max_bytes":59000,"complete_preGit_original_inputs_max_bytes":50000,"complete_preGit_report_max_bytes":8000,"complete_preGit_science_max_bytes":95000,"complete_report_max_bytes":8000,"complete_science_max_bytes":95000,"reserved_publication_bytes":230000}')
SCIENCE_FIELDS=json.loads('["kind","complete","proved","actual_returncode","failure","stage","source_sha256","math_module_sha256","input_manifest_sha256","public_repository","run_id","run_attempt","workflow_event_commit","actual_scientific_checkout_commit","runtime","arithmetic_bits","parameters","retained_scope","planned_shape","actual_progress","gates","actual_mathematical_wall_seconds","input_sha256","verified_original_inputs","original_source_AST_evidence","accepted_original_inputs","complete_original_inputs_file","complete_derivative_request_certificate","complete_strict_coefficient_conclusion","complete_higher_flow_and_cut_conclusion","complete_strict_geometry_conclusion","complete_strict_leading_conclusion","complete_strict_forcing_conclusion","complete_local_regular_packet_conclusion","complete_free_first_transport_conclusion","complete_named_global_graph_conclusion"]')
COPY_FIELDS=json.loads('["kind","complete","public_repository","run_id","run_attempt","workflow_event_commit","actual_scientific_checkout_commit","source_sha256","math_module_sha256","input_manifest_sha256","original_input_sha256","copied_original_scalar_records","copied_original_scalar_records_sha256","copied_complete_original_scopes","copied_complete_original_scopes_sha256","copied_original_stage_records","copied_original_stage_records_sha256","copied_complete_local_coefficients","copied_complete_local_coefficients_sha256","local_coefficient_qualification","copy_counts","complete_readonly_input_projection"]')
SCIENCE_KIND=json.loads('"actual_complete_global_fold_free_transport_finite_jets_v1"')
COPY_KIND=json.loads('"complete_original_inputs_for_global_fold_free_transport_finite_jets_v1"')
SCIENCE_GATE_NAMES=json.loads('["actual public runtime and complete manifest identity","twenty current small texts have their complete exact bytes","two historical stages have exact immutable original identities","seven Python AST files with four old producers never imported","original complete free-Airy success and local domains","original complete strict ordinary jets and all real intervals","original shorter flows and two ungauged scalar directions","original fourth derivatives and cut phase jets","the original FA input chain remains exactly identified","original adjacent child and full fold publication succeeded","original whole child mathematics and formatter failure remain distinct","complete original fold payload and all consumed holomorphic domains","complete saved p0-p2 q0-q3 free records and exact FA overlap","typed old records scopes and same original real family","complete triangular derivative request certificate","complete strict coefficient products with both physical means","only new higher flow and cut derivatives with actual positive phase gap","complete strict fold geometry and all retained lower denominators","complete leading jets with original forward and reverse scalar fees","complete first forcing with every drift theta and mean term","complete local analytic packet and read-only free amplitude seeds","complete free first transport with nonzero old cut trace","complete named global graph and all original inputs unchanged","complete thirty-six fields twenty-four gates and limited conclusion"]')
SCIENCE_PARAMETERS=json.loads('{"actual_original_interfaces":3070,"arithmetic_bits":320,"background_physical_bandwidth":384,"complete_genuine_potential_and_received_error_claimed":false,"derivative_convention":"ordinary one-sided radial derivatives and physical angular derivatives; complete Fourier A0 norms","drift_label_bandwidth":192,"exact_coefficient_strip":"1/32","exact_fold_radius":"3/8000","exact_fold_strip":"3/128","exact_old_free_holomorphic_radius":"1/6000","exact_old_free_holomorphic_width":"1/128","exact_real_delta_radius":"1/100000000","exact_root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"exact_saved_free_radius":"9/1000000","exact_saved_free_width":"1/512","exact_strict_cut":"76285779072683/320000000000000","exact_strict_interval":["0","76285779072683/320000000000000"],"expected_actual_gate_count":24,"expected_current_inputs":20,"expected_historical_inputs":2,"expected_immutable_AST_files":7,"expected_mathematical_input_roles":19,"expected_total_inputs":22,"fixed_intrinsic_parameter":"eta_0","formal_angular_weight":1,"formal_radial_weight":1,"historical_gzip_input_only":true,"jet_shapes":{"forcing":[12,1],"free_transport":[12,2],"geometry":[15,3],"leading":[14,3]},"maximum_strict_radial_degree":3,"maximum_total_degree":15,"new_ray_ODE_solves":0,"new_scalar_exponentials":0,"new_scalar_logarithms":0,"old_cut_phase_derivatives_recomputed":0,"old_flow_derivatives_recomputed":0,"old_free_amplitude_budgets_recomputed":0,"old_producer_execution_allowed":false,"original_local_piece_label":2549,"physical_drift_bandwidth":768,"physical_frequency":"n=4|j|"}')
SCIENCE_SCOPE=json.loads('{"both_characteristic_branches_and_physical_signs":true,"complete_N6_received_source_constants_proved":false,"complete_four_endpoint_constants_proved":false,"complete_ordinary_one_sided_jets_only":true,"complete_physical_means":2,"genuine_potential_packet_proved":false,"high_contraction_or_finite_border_inverse_proved":false,"individual_root_Phi_radial_three_not_claimed":true,"local_analytic_X_T_and_regular_packet_separate":true,"new_complete_free_jet_graph_only":true,"no_old_targets_recomputed":true,"old_free_w1_distinct_from_genuine_w1V":true,"old_full_complex_domains_only_used_on_qualified_local_piece":true,"old_whole_mathematics_success_and_formatter_failure_distinct":true,"ordinary_dr_transport_nonzero_cut_trace":true,"original_all_partial_intervals_and_interfaces_retained":true,"physical_incoming_or_nonlinear_background_proved":false,"root_or_waist_receiver_norms_newly_proved":false,"same_original_real_family_and_fixed_intrinsic_eta0":true,"selected_true_radial_state_and_original_reflection":true}')
SUCCESS_ACTUAL_PROGRESS=json.loads('{"current_text_files_verified":20,"historical_stage_bytes_read":25425,"historical_stage_files_read":2,"immutable_AST_files_checked":7,"new_derivative_certificates":1,"new_free_transport_graphs":1,"new_global_graph_conclusions":1,"new_higher_flow_graphs":1,"new_local_regular_graphs":1,"new_scalar_slots_saved":437,"new_strict_coefficient_graphs":1,"new_strict_forcing_graphs":1,"new_strict_geometry_graphs":1,"new_strict_leading_graphs":1,"old_complete_local_coefficient_objects_copied":1,"old_current_scalar_records_copied":66,"old_historical_scalar_records_copied":40,"old_mathematical_stage_products_read":2,"old_producer_imports_or_calls":0,"old_rays_flows_exponentials_evaluated":0,"old_saved_free_budget_calls":0,"old_scientific_receipts_admitted":4,"old_scientific_targets_recomputed":0,"old_scope_objects_copied":9,"original_input_bytes_modified":0}')
CURRENT_PIN_SPECS=json.loads('{"adjacent_process":{"bytes":37783,"git_blob":"26a04e8d7f79bc87623b149351599b328da4c427","path":"topics/visible-flex-exact-nearby/notes/correlated_adjacent_piece_first_Airy_sources_ci/run-43676926141-1/consumers/process.json","sha256":"9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"},"adjacent_publication":{"bytes":26496,"git_blob":"51b165e8b8d93a800524a5aab616f22196d7ed30","path":"topics/visible-flex-exact-nearby/notes/correlated_adjacent_piece_first_Airy_sources_ci/run-43676926141-1/publication.json","sha256":"0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"},"dza_science":{"bytes":26909,"git_blob":"67b41ac717207f8696b637c667fb210088fca638","path":"topics/visible-flex-exact-nearby/notes/fourth_angle_global_sign_budgets_ci/run-43773671216-1/actual-scientific-conclusion.json","sha256":"05036749a28c55499e2ed6fe47019cd31f4438652e3e6ab1319e6f9f2f2c4dba"},"fa_manifest":{"bytes":23418,"git_blob":"8ff0dbf8a5042f30f7f31ad68f9c29d93a6af95e","path":"topics/visible-flex-exact-nearby/notes/2026-11-15-R133-free-Airy-first-omitted-cut-scalars-CI-inputs.json","sha256":"d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b"},"fa_science":{"bytes":35718,"git_blob":"2001f4e2eeece1cda56b18b90dccab04b7f6d336","path":"topics/visible-flex-exact-nearby/notes/free_Airy_first_omitted_cut_scalars_ci/run-43763658978-1/actual-scientific-conclusion.json","sha256":"2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2"},"math_module":{"bytes":31846,"git_blob":"afa3b49b2035be07abee6a7f9041899c135dcdea","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_global_fold_free_transport_jet_math.py","sha256":"cb9c9aa0f7e5749967ece4e51210f359b4c58eecc7f83a05040607543ac47621"},"original_adjacent_source":{"bytes":53824,"git_blob":"380f628bbabdf146cba2f39b34204b63e92f736a","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_adjacent_piece_correlated_first_Airy_sources.py","sha256":"fa344d170bca13c3faec22034aabbeab27da6116daef59f45c128c011998758d"},"original_fa_source":{"bytes":48827,"git_blob":"9e0a75461e0b8302a82e0444828a2c86379c3443","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_free_Airy_first_omitted_cut_scalars.py","sha256":"a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954"},"original_fold_algorithm":{"bytes":32009,"git_blob":"27427dd6302b1d9c4ce8e0dd4a9d48fa15f920c3","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_anchored_auxiliary_root_fold_direct_leading.py","sha256":"410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783"},"original_whole_algorithm":{"bytes":51126,"git_blob":"327ecef0f265b88be9789212b4044afde9a28f22","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_whole_physical_root_piece_first_Airy_sources.py","sha256":"66668065abd27ae37f789adf72a9deda9a15eda33d751f0c4b6fef8e54f17a81"},"sj_execution":{"bytes":46318,"git_blob":"7dac244799016d9cae317a61f6c5dbe47ca0a013","path":"topics/visible-flex-exact-nearby/notes/strict_radial_first_symbol_defect_ci/run-43768006977-1/execution.json","sha256":"2540a3a81f1b6cd83c24b6a1c9ad2bdc119fb04a9a37c0251f6157a3cbc7cb88"},"wgs_contract":{"bytes":28978,"git_blob":"4980f1a2c119b6470afc24a2fc662c75fa210479","path":"topics/visible-flex-exact-nearby/results/R133-supplement-complete-global-fold-and-free-first-transport-finite-jets.md","sha256":"4d3638fe6ae8793b937d4c7f57a4c092d59d41df94991722d8b622ed958e576e"},"whole_process":{"bytes":8346,"git_blob":"ad2035cbd7aed089c2be0fdd7f552243447373c0","path":"topics/visible-flex-exact-nearby/notes/whole_physical_root_piece_first_Airy_sources_ci/run-43669106351-1/consumers/process.json","sha256":"242d82b6f1ead216bf8e90679a9952a2aaad0e9d7ba29293739911e70ab4d145"},"whole_publication":{"bytes":11945,"git_blob":"eb418b7ece29d12c0274c141364cf3c93dffaa15","path":"topics/visible-flex-exact-nearby/notes/whole_physical_root_piece_first_Airy_sources_ci/run-43669106351-1/publication.json","sha256":"fc3a190d8b701ef84188f2a37ee846c4f3669b5ac409faa5a6b72850162d1099"},"wua_contract":{"bytes":40111,"git_blob":"7b89251dcd51e8cb78fd3e8e42905114ef982ebf","path":"topics/visible-flex-exact-nearby/results/R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md","sha256":"9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad"},"wui_contract":{"bytes":31558,"git_blob":"730400be921fbdfd109b9c378a607cf768f674b6","path":"topics/visible-flex-exact-nearby/results/R133-supplement-readonly-input-closure-for-the-global-genuine-waist-error.md","sha256":"2a77f1cd53a09c952daa8ba64eebe2bb80bb2e9735c6c78e3ceaba4223ad90d6"},"wx_execution":{"bytes":43753,"git_blob":"5121a599896025d90e2861450756a256aaba659d","path":"topics/visible-flex-exact-nearby/notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json","sha256":"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12"}}')
CURRENT_ROLE_ORDER=json.loads('["source","math_module","worker","rules","wgs_contract","wui_contract","wua_contract","fa_science","sj_execution","wx_execution","dza_science","fa_manifest","adjacent_process","adjacent_publication","whole_process","whole_publication","original_fa_source","original_adjacent_source","original_fold_algorithm","original_whole_algorithm"]')
AST_ROLES=json.loads('["source","math_module","worker","original_fa_source","original_adjacent_source","original_fold_algorithm","original_whole_algorithm"]')
HISTORICAL=json.loads('[{"bytes":4501,"commit":"a3d84d905ce72e3a854874bbe98d119623f3f8de","git_blob_sha":"fe180735fb6cbfaef8dff2ef68aa511ed3ac0643","path":"topics/visible-flex-exact-nearby/notes/correlated_adjacent_piece_first_Airy_sources_ci/run-43676926141-1/consumers/stages/complete-original-reference-holomorphic-majorants.json.gz","role":"fold_majorants_native","sha256":"29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"},{"bytes":20924,"commit":"a3d84d905ce72e3a854874bbe98d119623f3f8de","git_blob_sha":"786700a1a0da5cdb7a0dde90b1dd04eb586db860","path":"topics/visible-flex-exact-nearby/notes/whole_physical_root_piece_first_Airy_sources_ci/run-43669106351-1/consumers/stages/complete-radius-budget-9-1000000.json.gz","role":"free_radius_native","sha256":"8b31b1c0030f892ec763d32ecf7b4968d468c5f93b30bbfe7408d6bf0b4892d5"}]')
SCIENTIFIC_GRAPH_SHAPES=json.loads('{"complete_free_first_transport_conclusion":{"actual_original_interfaces_retained":3070,"both_characteristic_branches_and_physical_signs":true,"complete_cut_ratio_angular_jet":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,0],"value_omitted_for_lift":false},"complete_jets":{"R":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,2],"value_omitted_for_lift":false},"a1":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,2],"value_omitted_for_lift":false},"b1":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,2],"value_omitted_for_lift":false},"transport_kernel":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,1],"value_omitted_for_lift":false}},"genuine_potential_addition_included":false,"new_ray_integrations":0,"new_scalar_exponential_evaluations":0,"old_free_amplitude_targets_recomputed":0,"old_root_trace_preserved_at_cut":true,"ordinary_fixed_dr_endpoints_and_all_partial_intervals":true},"complete_higher_flow_and_cut_conclusion":{"all_shorter_intervals_both_branches_both_orientations":true,"complete_strict_phase_angular_orders_1_through_15":["#U","#U","#U","#U","#U","#U","#U","#U","#U","#U","#U","#U","#U","#U","#U"],"cut_phase_lower":"#L","cut_phase_orders_5_through_15":["#U","#U","#U","#U","#U","#U","#U","#U","#U","#U","#U"],"flow_orders_5_through_15":["#U","#U","#U","#U","#U","#U","#U","#U","#U","#U","#U"],"old_cut_phase_1_through_4_recomputed":0,"old_flow_1_through_4_recomputed":0,"strict_phase_lower":"#L"},"complete_local_regular_packet_conclusion":{"both_old_component_tables_read":true,"complete_jets":{"Fa":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,1],"value_omitted_for_lift":false},"Fb":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,1],"value_omitted_for_lift":false},"G":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[14,3],"value_omitted_for_lift":false},"H_inverse_entry_sum":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[13,2],"value_omitted_for_lift":false},"Q":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[13,2],"value_omitted_for_lift":false},"T":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[15,3],"value_omitted_for_lift":false},"X_minus_phi":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[15,3],"value_omitted_for_lift":false},"a0":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[14,3],"value_omitted_for_lift":false},"a1":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,2],"value_omitted_for_lift":false},"b0":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[14,3],"value_omitted_for_lift":false},"b1":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,2],"value_omitted_for_lift":false},"mu_inverse":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[13,2],"value_omitted_for_lift":false}},"complete_local_H_inverse_holomorphic_upper":"#U","complete_local_mu_inverse_holomorphic_upper":"#U","free_and_genuine_amplitude_distinct":true,"free_p0_p1_p2_q0_through_q3_recomputed":0,"individual_Phi_radial_jets_at_root_not_used":true,"local_cover_saved_h_margin":"#L","local_original_piece_label":2549,"local_to_strict_function_identity":"same actual root-normalized germ at rc","old_FA_free_orders_through_six_recomputed":0},"complete_named_global_graph_conclusion":{"T_strict_rule":"T=-t, with identical absolute derivative bounds","X_local_rule":"add the exact identity derivative at (0,1); omit the lift value","actual_nonlinear_background_proved":false,"complete_N6_residual_constants_proved":false,"complete_four_waist_endpoint_constants_proved":false,"complete_genuine_potential_packet_proved":false,"complete_named_global_free_jet_graph":true,"complete_negative_receiver_constant_proved":false,"finite_or_incoming_inverse_proved":false,"high_contraction_proved":false,"independent_physical_means_retained":true,"normalization":"old root-normalized free first transport; original fixed intrinsic eta0","ordinary_one_sided_derivatives":true,"patch_links":{"Fa":["strict_forcing.Fa","local.Fa"],"Fb":["strict_forcing.Fb","local.Fb"],"G":["strict_leading.G","local.G"],"H_inverse":["strict_geometry.H_inverse_entry_sum","local.H_inverse_entry_sum"],"Q":["strict_geometry.Q","local.Q"],"T":["strict_geometry.t","local.T"],"X":["strict_geometry.X_derivatives","local.X_minus_phi"],"a0":["strict_leading.a0","local.a0"],"a1":["strict_transport.a1","local.a1"],"b0":["strict_leading.b0","local.b0"],"b1":["strict_transport.b1","local.b1"],"mu_inverse":["strict_geometry.mu_inverse","local.mu_inverse"]},"physical_angular_frequency":4,"same_actual_functions_on_the_common_cut":true,"union_bound_rule":"max of the two already complete patch bounds after their common identity"},"complete_strict_coefficient_conclusion":{"background_pair_used_as_each_component_upper":true,"full_physical_mean_kept":true,"new_jets":{"a_sigma":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[15,2],"value_omitted_for_lift":false},"d":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[15,2],"value_omitted_for_lift":false},"ell0":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[14,2],"value_omitted_for_lift":false},"eta":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[15,2],"value_omitted_for_lift":false}},"new_target":"whole strict coefficient products, not old per-piece rows","old_Qmixed_and_intrinsic_jets_read_only":true},"complete_strict_forcing_conclusion":{"background_ordinary_radial_order_max":2,"both_components":true,"complete_coefficient_jets":{"T0":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,1],"value_omitted_for_lift":false},"V0":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,1],"value_omitted_for_lift":false},"b_local":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[13,2],"value_omitted_for_lift":false},"e":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[13,2],"value_omitted_for_lift":false},"ell":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[13,2],"value_omitted_for_lift":false},"rQ":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,1],"value_omitted_for_lift":false},"tQ":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,1],"value_omitted_for_lift":false},"theta":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,1],"value_omitted_for_lift":false}},"complete_forcing_jets":{"Fa":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,1],"value_omitted_for_lift":false},"Fb":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,1],"value_omitted_for_lift":false}},"full_second_order_drift_and_original_means_present":true,"full_theta_Q_KT_product_present":true,"leading_ordinary_radial_order_max":3,"no_old_forcing_target_executed":true},"complete_strict_geometry_conclusion":{"complete_jets":{"H_inverse_entry_sum":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[13,2],"value_omitted_for_lift":false},"Q":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[13,2],"value_omitted_for_lift":false},"X_derivatives":{"group_upper":[null,"#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[15,3],"value_omitted_for_lift":true},"determinant":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[13,2],"value_omitted_for_lift":false},"mu_inverse":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[13,2],"value_omitted_for_lift":false},"omega":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[15,3],"value_omitted_for_lift":false},"phase_derivatives":{"group_upper":[null,"#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[15,3],"value_omitted_for_lift":true},"t":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[15,3],"value_omitted_for_lift":false},"x":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[14,3],"value_omitted_for_lift":false},"y":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[14,3],"value_omitted_for_lift":false}},"complete_positive_lowers":{"Q_fold":"#L","determinant":"#L","mu":"#L","whole_t_over_rho":"#L"},"ordinary_one_sided_r_and_full_real_lifts":true,"root_Phi_radial_derivatives_not_asserted":true,"strict_minus_T_lower_is_old_cut_lower":true,"t_over_rho_candidates":{"local":"#L","strict":"#L"}},"complete_strict_leading_conclusion":{"complete_G_lower":"#L","complete_G_upper":"#U","complete_jets":{"G":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[14,3],"value_omitted_for_lift":false},"a0":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[14,3],"value_omitted_for_lift":false},"b0":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[14,3],"value_omitted_for_lift":false},"v0":{"group_upper":["#U","#U","#U","#U","#U","#U","#U","#U"],"shape":[12,2],"value_omitted_for_lift":false}},"complete_v0_lower":"#L","forward_and_reverse_old_scalar_fees_used_in_their_own_direction":true,"log_derivative_signs_replaced_only_by_complete_positive_triangle":true,"new_scalar_flow_exponentials":0,"v0_positive_identity":"G times Phi_sigma_phi squared"}}')
SCIENTIFIC_GRAPH_SLOT_COUNTS=json.loads('{"complete_free_first_transport_conclusion":40,"complete_higher_flow_and_cut_conclusion":39,"complete_local_regular_packet_conclusion":107,"complete_named_global_graph_conclusion":0,"complete_strict_coefficient_conclusion":36,"complete_strict_forcing_conclusion":83,"complete_strict_geometry_conclusion":94,"complete_strict_leading_conclusion":38}')
DERIVATIVE_CERTIFICATE=json.loads('{"all_product_indices_checked_before_their_arithmetic":true,"allowed_indices":"0<=a<=p; b>=0; a+b<=m","fixed_degree_groups":[[0,0],[1,1],[2,2],[3,3],[4,4],[5,6],[7,9],[10,12],[13,15]],"formal_angular_weight":1,"formal_radial_weight":1,"local_shapes":{"Fa":[12,1],"Fb":[12,1],"G":[14,3],"H_inverse_entry_sum":[13,2],"Q":[13,2],"T":[15,3],"X_minus_phi":[15,3],"a0":[14,3],"a1":[12,2],"b0":[14,3],"b1":[12,2],"mu_inverse":[13,2]},"new_genuine_potential_packet_included":false,"no_root_radial_three_bound_for_individual_Phi":true,"normalized_coefficients":"ordinary derivative norm divided by a! b!","ordered_predecessors":{"G":[["t",14,3],["q",3,3],["ell0",2,2]],"forcing":[["w0",14,3],["background",14,2],["eta",2,2],["Q",12,1],["mu_inverse",12,1]],"free_w1":[["transport_kernel",12,1],["v0",12,2],["a_sigma",11,1],["flow",12,0],["t",12,2]],"phase_derivatives":[["flow",15,0],["a_sigma",14,2]],"t":[["phase_derivatives",15,3]],"transport_kernel":[["forcing",12,1],["v0",12,1],["Q",12,1],["phase_derivatives",13,1],["t",12,1]],"w0":[["G",14,3],["x",14,3],["y",14,3],["t",14,3]],"x":[["phase_derivatives",15,3]],"y":[["t",15,3]]},"phase_value_not_a_periodic_function":true,"reconstruction":"a! b! times the upper for the group containing a+b","strict_shapes":{"Fa":[12,1],"Fb":[12,1],"G":[14,3],"H_inverse_entry_sum":[13,2],"Q":[13,2],"R":[12,2],"X_derivatives":[15,3],"a0":[14,3],"a1":[12,2],"b0":[14,3],"b1":[12,2],"determinant":[13,2],"mu_inverse":[13,2],"omega":[15,3],"phase_derivatives":[15,3],"t":[15,3],"transport_kernel":[12,1],"v0":[12,2],"x":[14,3],"y":[14,3]}}')
PLANNED_SHAPE=json.loads('{"current_inputs":20,"historical_bytes":25425,"historical_inputs":2,"immutable_AST_files":7,"local_coefficient_extra_original_fields_preserved":true,"local_coefficient_required_ball_count":72,"mathematical_input_roles":19,"new_complete_jet_graphs":7,"new_global_closure_graphs":1,"new_graph_slot_counts":{"complete_free_first_transport_conclusion":40,"complete_higher_flow_and_cut_conclusion":39,"complete_local_regular_packet_conclusion":107,"complete_named_global_graph_conclusion":0,"complete_strict_coefficient_conclusion":36,"complete_strict_forcing_conclusion":83,"complete_strict_geometry_conclusion":94,"complete_strict_leading_conclusion":38},"new_scalar_slots":437,"old_complete_local_coefficient_objects":1,"original_complete_scope_objects":9,"original_current_scalar_records":66,"original_mathematical_targets_to_call":0,"original_stage_scalar_records":40}')
FROZEN_OLD_COPY_HASHES=json.loads('{"complete_scopes":"986561d54c780e1ff9d121110e473594aac8f96cd36552fc7b85d9d657a0cd2f","scalar_records":"5aa27845005a14774eaa4c3d01509dcd8e8869d6b1e2e7a0f588f346487e608e"}')
LOCAL_COEFFICIENT_QUALIFICATION=json.loads('{"actual_root_centered_disk_used_by_fold":"3/8000","all_original_coefficient_fields_copied":true,"array_convention":"full component Wiener norms of ordinary radial and physical angular derivatives; no factorial division","complete_original_source_path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_anchored_auxiliary_root_fold_direct_leading.py","complete_original_source_sha256":"410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783","exact_complete_consumed_coefficient_radius":"3/8000","exact_identity_with_original_family_only_on_original_germ_intersection":true,"exact_original_auxiliary_input_radius":"1/2000","exact_original_coefficient_strip":"1/32","fixed_intrinsic_parameter":"eta_0","full_U_and_V_shape":[4,5],"missing_higher_derivatives_not_inferred":true,"not_root_circle_only":true,"original_full_payload_sha256":"e0f1852f561b2596018e387a0b6c728441b665fee227e4c6fa85bc352060bf23","original_full_stage_sha256":"29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144","original_path":"payload.coefficients","radial_r_and_rho_absolute_derivatives_identical":true,"real_delta_radius":"1/100000000","same_original_piece":2549}')
LOCAL_COEFFICIENT_SHAPE=json.loads('{"D":[6],"Dr":[3],"U":[4,5],"V":[4,5],"additional_original_fields_retained":true,"full_original_dictionary_is_copied":true,"minimum_original_scalar_records":72,"required_scalar_fields":["km","kp","em","ep","am","ap","k1","k2","a1","a2","beta","beta_r","K","Kr","T0","V0","vartheta","rQ","ell","b0","eta_log_r","log_EG_r","log_EG_rr"]}')
ORIGINAL_CURRENT_RECORD_KEYS=json.loads('["K_0","K_1","K_2","K_3","Q_0_0","Q_0_1","Q_0_2","Q_0_3","Q_1_0","Q_1_1","Q_1_2","Q_1_3","Q_2_0","Q_2_1","Q_2_2","Q_2_3","beta_0","beta_1","beta_2","beta_3","cut_phase_1","cut_phase_2","cut_phase_3","cut_phase_4","cut_t_1","cut_t_2","cut_t_3","cut_t_4","eta_lower","flow_1","flow_2","flow_3","flow_4","flow_lower","free_old_0_0","free_old_0_1","free_old_0_2","free_old_0_3","free_old_0_4","free_old_0_5","free_old_0_6","free_old_1_0","free_old_1_1","free_old_1_2","free_old_1_3","free_old_1_4","free_old_1_5","free_old_1_6","gamma_0","gamma_1","gamma_2","gamma_3","leading_forward","leading_reverse","q_0","q_1","q_2","q_3","q_cut_lower","q_cut_upper","q_lower","q_upper","t_cut_lower","t_cut_upper","xdev_cut","y_cut"]')
ORIGINAL_SCOPE_KEYS=json.loads('["dza_parameters","dza_scope","fa_parameters","sj_parameters","sj_scope","wx_flow","wx_leading","wx_parameters","wx_scope"]')
SCIENTIFIC_RUNTIME=json.loads('{"Python":"3.12.14","python_flint":"0.9.0"}')
MAIN_FILENAME=json.loads('"actual-scientific-conclusion.json"')
COPIES_FILENAME=json.loads('"complete-original-inputs.json"')
PUBLICATION_FILES=json.loads('["actual-scientific-conclusion.json","complete-original-inputs.json","report.md","execution.json"]')
MANIFEST_KIND=json.loads('"complete_global_fold_free_transport_finite_jets_public_inputs_v1"')
EXPECTED_ACCEPTED_ORIGINAL_INPUTS=json.loads('{"fa":{"actual_scientific_checkout_commit":"0c214d0b9b0c4cfa7c6ec363f253e419d14aae01","arithmetic_bits":320,"field_count":52,"gate_count":24,"gate_sha256":"06860c1ba885d8676ab24fc1debaf795d015a3ea8a9697175a0e9c01fa2f5a05","input_manifest_sha256":"d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b","kind":"actual_complete_free_Airy_first_omitted_cut_scalars_v1","parameter_key":"mathematical_parameters","parameter_sha256":"1dd546a7fbd67da27077a72569c9124062445986d8cb77682ad94eee3131b553","run_attempt":"1","run_id":"43763658978","runtime":{"Python":"3.12.14","arithmetic_bits":320,"python_flint":"0.9.0"},"source_sha256":"a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954","stage":"complete-new-free-Airy-strong-cut-scalars","workflow_event_commit":"0c214d0b9b0c4cfa7c6ec363f253e419d14aae01","complete":true,"proved":true,"actual_returncode":0,"failure":null},"sj":{"actual_scientific_checkout_commit":"095ca270433abd339346790ffa35e4205b08b000","arithmetic_bits":320,"field_count":66,"gate_count":26,"gate_sha256":"d753118fcff4893dbfa863509f5b85dfa72d9dc0c10d0f1a6f097e11de1f2f6b","input_manifest_sha256":"31602b830279bc5141950f3c34b70442f5a2997f872179b45effccb0ff3cdb48","kind":"actual_complete_strict_radial_first_symbol_defect_v1","parameter_key":"mathematical_parameters","parameter_sha256":"21da24e83a81c3156053a927774ab469ce91c20e0e4917095801d8d68cfb31df","run_attempt":"1","run_id":"43768006977","runtime":{"numpy":"2.3.5","python":"3.12.14","python_flint":"0.9.0","scipy":"1.17.0"},"source_sha256":"dfcf40ab948ea71ea80d733cd851602dcf5c78fdd83993e25f06664fc62b39d0","stage":"complete","workflow_event_commit":"095ca270433abd339346790ffa35e4205b08b000","complete":true,"proved":true,"actual_returncode":0,"failure":null},"wx":{"actual_scientific_checkout_commit":"cd14574e6b1bd74973214d57979305e5e3dfe41f","arithmetic_bits":320,"field_count":55,"gate_count":20,"gate_sha256":"4c8f214fc05eaf3c8c3a9970a41921037356bf0f9021ef1b1ec942c485b90d47","input_manifest_sha256":"aa3c9d7e9f3a217122af5a321fadfcb2abe420e7e7c48217e3a181c9dbdd6f26","kind":"actual_true_waist_coordinates_from_saved_positive_products_v1","parameter_key":"mathematical_parameters","parameter_sha256":"a0d15289f39599e00531eeaab70be7b469ef27b35de1d8593e9f365c23a7399b","run_attempt":"1","run_id":"43763424840","runtime":{"numpy":"2.3.5","python":"3.12.14","python_flint":"0.9.0","scipy":"1.17.0"},"source_sha256":"63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424","workflow_event_commit":"cd14574e6b1bd74973214d57979305e5e3dfe41f","complete":true,"proved":true,"actual_returncode":0,"failure":null},"dza":{"actual_scientific_checkout_commit":"2a7dc8cc3ab6d52287e034a9cb2f0302f020b8a6","arithmetic_bits":320,"field_count":61,"gate_count":24,"gate_sha256":"19774f5f2793d8b428ba1deae87c3c81e446f8d61ff43a80024827b44c6fa7b1","input_manifest_sha256":"296f84d4f05510525258bc563f2313ba34872256aa9131bcf3f6cd0489cb94af","kind":"actual_fourth_angle_and_global_sign_budgets_v1","parameter_key":"parameters","parameter_sha256":"c27ceb81a2b4666a88238153c8cf15cd7c8912dac061ae3168fcda1d19393ba4","run_attempt":"1","run_id":"43773671216","runtime":{"Python":"3.12.14","python_flint":"0.9.0"},"source_sha256":"5909e8da91d61bd2646941e18190fdd20dc98370e4563ff41526449658f75b28","stage":"complete","workflow_event_commit":"2a7dc8cc3ab6d52287e034a9cb2f0302f020b8a6","complete":true,"proved":true,"actual_returncode":0,"failure":null},"original_adjacent_mathematics":{"actual_scientific_checkout_commit":"0326a07674e4c99a33995d1901463180a98e2f96","manifest_sha256":"57b978dbff16590d593686a8c7b98b8374aae532b500ec88cf975d3ab3821695","mathematical_gate_count":14,"mathematical_gates_sha256":"ef1d25f0187114f80cb6797eeace52792bf4c2a988b308c3067f0d60c6258273","mathematical_source_sha256":"fa344d170bca13c3faec22034aabbeab27da6116daef59f45c128c011998758d","native_bytes":42046,"native_sha256":"5754193c193b9769eeec94bf6a9258489db14f9bfda758bf34a549d71c867a0f","run_attempt":"1","run_id":"43676926141","source_sha256":"41282a7fb1f63f1a307a7ff721e4e1c553388613feb3c033013a9dfc10aaa2f5","workflow_event_commit":"f111751254dc2bc3af41d5a647dca8b5d9b391e7","complete":true,"actual_returncode":0,"mathematical_complete":true,"mathematical_proved":true,"mathematical_failure":null,"publication_complete":true,"publication_actual_returncode":0},"original_whole_mathematics":{"actual_scientific_checkout_commit":"ef6f75878fc78981d3f75a056e7501f7131a37e0","manifest_sha256":"d30c306e58f3e6be96768b983db4df840843455e2cc5147c84c6e2d7958e5aac","mathematical_gate_count":10,"mathematical_gates_sha256":"5cb0afffe99e4e8b01529f3ad323416754c95be1ded41fa16839fb6b3b89ce30","mathematical_source_sha256":"66668065abd27ae37f789adf72a9deda9a15eda33d751f0c4b6fef8e54f17a81","native_bytes":44628,"native_sha256":"6668c9b2c8f1632e3bd8af392a803335f076c64e1d7fb74dfc9e1605f0e1ee2d","run_attempt":"1","run_id":"43669106351","source_sha256":"855bcec6d31a9f0bdb3e3710c4e6418c2be0d816edf09a59da01ab6ec956904d","workflow_event_commit":"d549f0c80a0df695152fc883999007ad4f4edfe9","actual_returncode":0,"mathematical_complete":true,"mathematical_proved":true,"mathematical_failure":null,"wrapper_complete":false,"formatter_failure":{"message":"dict() got multiple values for keyword argument \'complete\'","type":"TypeError"},"publication_complete":false,"publication_actual_returncode":1,"full_original_process_sha256":"242d82b6f1ead216bf8e90679a9952a2aaad0e9d7ba29293739911e70ab4d145","full_original_publication_sha256":"fc3a190d8b701ef84188f2a37ee846c4f3669b5ac409faa5a6b72850162d1099"},"fold_stage":{"complete":true,"stage":"complete-original-reference-holomorphic-majorants","source_sha256":"f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739","algebra_sha256":"1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53","input_manifest_sha256":"76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a","runtime":{"numpy":"2.3.5","python":"3.12.14","python_flint":"0.9.0","scipy":"1.17.0"},"complete_payload_sha256":"e0f1852f561b2596018e387a0b6c728441b665fee227e4c6fa85bc352060bf23","consumed_majorants":["chi","T","G","Q","a0","b0","F0","F1"],"consumed_fold_fields":["E","TM","BT","gap","mu","Am","G","Gi"],"complete_local_coefficients_copied_entirely":true,"complete_local_coefficient_ball_count":"#LOCAL_COEFFICIENT_BALL_COUNT"},"free_stage":{"complete":true,"stage":"complete-radius-budget-9-1000000","stage_kind":"radius_budget_stages","source_sha256":"66668065abd27ae37f789adf72a9deda9a15eda33d751f0c4b6fef8e54f17a81","input_manifest_sha256":"d30c306e58f3e6be96768b983db4df840843455e2cc5147c84c6e2d7958e5aac","runtime":{"numpy":"2.3.5","python":"3.12.14","python_flint":"0.9.0","scipy":"1.17.0"},"original_Taylor_native_sha256":"758a2901d194e9d54ec10bb5004014ee34a972c35367589fd5c86afce3f30c9f","original_Nraw_native_sha256":"fbe1bce690f33335d2b024fe38a751743e0017e7d275b4d1fb0712be155f177e","complete_payload_sha256":"e3658e369da9076e464c39eb6324f23d9685b5909e11a3b25e0d0bfb17761581","exact_physical_rho_cover":"9/1000000","exact_holomorphic_rho_radius":"1/6000","exact_holomorphic_phi_width":"1/128","exact_output_phi_width":"1/512","original_free_and_genuine_amplitudes_distinct":true,"all_24_original_component_records_read":true,"all_16_original_FA_overlap_records_equal":true},"original_FA_manifest_sha256":"d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b","all_complete_original_inputs_identified":true}')
ORIGINAL_STAGE_SHAPE=json.loads('{"majorants":{"chi":["#U","3/8000","3/128"],"T":["#U","3/8000","3/128"],"G":["#U","3/8000","3/128"],"Q":["#U","3/8000","3/128"],"a0":["#U","3/8000","3/128"],"b0":["#U","3/8000","3/128"],"F0":["#U","1/6000","1/128"],"F1":["#U","1/6000","1/128"]},"fold":{"E":"#U","TM":"#U","BT":"#U","gap":"#U","mu":"#U","Am":"#U","G":"#U","Gi":"#U"},"free_components":{"a1":{"0":["#U","#U","#U","#U"],"1":["#U","#U","#U","#U"],"2":["#U","#U","#U","#U"]},"b1":{"0":["#U","#U","#U","#U"],"1":["#U","#U","#U","#U"],"2":["#U","#U","#U","#U"]}}}')
EXPECTED_AST_EVIDENCE=dict(count=7,roles=AST_ROLES,old_source_imports=0,new_module_sha256=CURRENT_PIN_SPECS["math_module"]["sha256"],four_old_producers_are_AST_and_literal_evidence_only=True)
SCIENCE_PIN_SHA256={k:v["sha256"] for k,v in CURRENT_PIN_SPECS.items()}
SCIENCE_PIN_SHA256.update({v["role"]:v["sha256"] for v in HISTORICAL})
SCIENCE_PIN_BYTES={k:v["bytes"] for k,v in CURRENT_PIN_SPECS.items()}
SCIENCE_PIN_BYTES.update({v["role"]:v["bytes"] for v in HISTORICAL})

def scalar_record(value):
    return (isinstance(value,dict) and set(value)=={"ball"}
        and isinstance(value["ball"],str) and 0<len(value["ball"])<=256
        and not any(x in value["ball"].lower() for x in ("nan","inf")))

def full_shape(value,expected):
    if isinstance(expected,str) and expected in ("#U","#L"):
        return scalar_record(value)
    if isinstance(expected,dict):
        return (isinstance(value,dict) and set(value)==set(expected)
            and all(full_shape(value[k],v) for k,v in expected.items()))
    if isinstance(expected,list):
        return (isinstance(value,list) and len(value)==len(expected)
            and all(full_shape(a,b) for a,b in zip(value,expected)))
    return type(value) is type(expected) and value==expected

def original_ball_count(value):
    if isinstance(value,dict):
        if set(value)=={"ball"}:
            if not scalar_record(value):raise ValueError("nonfinite retained original scalar")
            return 1
        return sum(original_ball_count(v) for v in value.values())
    if isinstance(value,list):return sum(original_ball_count(v) for v in value)
    return 0

def original_inputs_valid(proc,copies,source,manifest,pins):
    try:
        if not (isinstance(proc,dict) and isinstance(copies,dict)
            and set(copies)==set(COPY_FIELDS) and len(copies)==22
            and copies["kind"]==COPY_KIND and copies["complete"] is True
            and copies["complete_readonly_input_projection"] is True
            and copies["public_repository"]==PUBLIC
            and copies["source_sha256"]==source
            and copies["math_module_sha256"]==SCIENCE_PIN_SHA256["math_module"]
            and (manifest is None or copies["input_manifest_sha256"]==manifest)):
            return False
        binding=("run_id","run_attempt","workflow_event_commit","actual_scientific_checkout_commit",
                 "source_sha256","math_module_sha256","input_manifest_sha256")
        if any(copies[k]!=proc[k] for k in binding):return False
        raw=compact(copies);ref=proc["complete_original_inputs_file"]
        if not (isinstance(ref,dict) and set(ref)=={"filename","bytes","sha256"}
            and ref["filename"]==COPIES_FILENAME and ref["bytes"]==len(raw)
            and ref["sha256"]==hashlib.sha256(raw).hexdigest()
            and copies["original_input_sha256"]==dict(manifest=copies["input_manifest_sha256"],**pins)):
            return False
        records=copies["copied_original_scalar_records"];scopes=copies["copied_complete_original_scopes"]
        if (not isinstance(records,dict) or set(records)!=set(ORIGINAL_CURRENT_RECORD_KEYS)
            or not all(scalar_record(v) for v in records.values())
            or not isinstance(scopes,dict) or set(scopes)!=set(ORIGINAL_SCOPE_KEYS)):
            return False
        for field,digest_key,frozen in (
            ("copied_original_scalar_records","copied_original_scalar_records_sha256","scalar_records"),
            ("copied_complete_original_scopes","copied_complete_original_scopes_sha256","complete_scopes")):
            digest=hashlib.sha256(compact(copies[field])).hexdigest()
            if digest!=copies[digest_key] or digest!=FROZEN_OLD_COPY_HASHES[frozen]:return False
        stages=copies["copied_original_stage_records"];coeff=copies["copied_complete_local_coefficients"]
        if not full_shape(stages,ORIGINAL_STAGE_SHAPE) or original_ball_count(stages)!=40:return False
        if not isinstance(coeff,dict):return False
        for key in LOCAL_COEFFICIENT_SHAPE["required_scalar_fields"]:
            if not scalar_record(coeff[key]):return False
        for key in ("U","V"):
            if not full_shape(coeff[key],[["#U"]*5 for _ in range(4)]):return False
        if not full_shape(coeff["D"],["#U"]*6) or not full_shape(coeff["Dr"],["#U"]*3):return False
        count=original_ball_count(coeff)
        if count<72:return False
        for field,digest_key in (
            ("copied_original_stage_records","copied_original_stage_records_sha256"),
            ("copied_complete_local_coefficients","copied_complete_local_coefficients_sha256")):
            if hashlib.sha256(compact(copies[field])).hexdigest()!=copies[digest_key]:return False
        if (copies["local_coefficient_qualification"]!=LOCAL_COEFFICIENT_QUALIFICATION
            or copies["copy_counts"]!=dict(current_scalar_records=66,stage_scalar_records=40,
                complete_scope_objects=9,complete_local_coefficient_objects=1,
                local_coefficient_ball_count=count)):
            return False
        accepted=json.loads(json.dumps(EXPECTED_ACCEPTED_ORIGINAL_INPUTS))
        accepted["fold_stage"]["complete_local_coefficient_ball_count"]=count
        return proc["accepted_original_inputs"]==accepted
    except (KeyError,TypeError,ValueError):
        return False

def scientific_receipt_valid(proc,copies,source,manifest,parameters,pins,runtime,execution=None):
    def hexid(value,size):
        return isinstance(value,str) and len(value)==size and all(x in "0123456789abcdef" for x in value)
    try:
        p=proc
        if not (isinstance(p,dict) and set(p)==set(SCIENCE_FIELDS) and len(p)==36
            and p["kind"]==SCIENCE_KIND and p["complete"] is True and p["proved"] is True
            and p["actual_returncode"]==0 and p["failure"] is None and p["stage"]=="complete"
            and p["source_sha256"]==source and hexid(source,64)
            and p["math_module_sha256"]==SCIENCE_PIN_SHA256["math_module"]
            and p["public_repository"]==PUBLIC
            and isinstance(p["run_id"],str) and p["run_id"].isdigit()
            and isinstance(p["run_attempt"],str) and p["run_attempt"].isdigit()
            and hexid(p["workflow_event_commit"],40) and hexid(p["actual_scientific_checkout_commit"],40)
            and p["runtime"]==runtime==SCIENTIFIC_RUNTIME and p["arithmetic_bits"]==320
            and parameters==SCIENCE_PARAMETERS and p["parameters"]==parameters
            and pins==SCIENCE_PIN_SHA256
            and hexid(p["input_manifest_sha256"],64)
            and (manifest is None or p["input_manifest_sha256"]==manifest)
            and p["input_sha256"]==dict(manifest=p["input_manifest_sha256"],**pins)
            and p["verified_original_inputs"]=={k:dict(bytes=SCIENCE_PIN_BYTES[k],sha256=v) for k,v in pins.items()}
            and p["original_source_AST_evidence"]==EXPECTED_AST_EVIDENCE
            and p["retained_scope"]==SCIENCE_SCOPE and p["actual_progress"]==SUCCESS_ACTUAL_PROGRESS
            and p["planned_shape"]==PLANNED_SHAPE
            and p["complete_derivative_request_certificate"]==DERIVATIVE_CERTIFICATE
            and isinstance(p["gates"],list) and len(p["gates"])==24
            and [v["name"] for v in p["gates"]]==SCIENCE_GATE_NAMES
            and all(set(v)=={"name","passed"} and v["passed"] is True for v in p["gates"])
            and type(p["actual_mathematical_wall_seconds"]) in (int,float)
            and 0<=p["actual_mathematical_wall_seconds"]<float("inf")):
            return False
        if execution is not None:
            for science_key,execution_key in (
                ("run_id","run_id"),("run_attempt","run_attempt"),
                ("workflow_event_commit","workflow_commit"),
                ("actual_scientific_checkout_commit","actual_scientific_checkout_commit"),
                ("source_sha256","source_sha256"),("input_manifest_sha256","input_manifest_sha256")):
                if p[science_key]!=execution[execution_key]:return False
        if not original_inputs_valid(p,copies,source,manifest,pins):return False
        if not all(full_shape(p[k],shape) for k,shape in SCIENTIFIC_GRAPH_SHAPES.items()):return False
        return all(original_ball_count(p[k])==SCIENTIFIC_GRAPH_SLOT_COUNTS[k]
                   for k in SCIENTIFIC_GRAPH_SHAPES)
    except (KeyError,TypeError,ValueError):
        return False

def render(state,science,copies):
    s=science or {};c=copies or {}
    complete=state.get("complete_mathematical_receipt_available") is True
    admitted=state.get("complete_original_input_receipt_available") is True
    failed=state.get("actual_failure") is not None or s.get("failure") is not None
    lines=["# Actual global fold and free first-transport finite jets","",
        ("Complete new WGS finite-jet conclusion." if complete else
         "Execution record; a complete new WGS jet conclusion is not admitted."),
        "The separate input file retains all original scalar bounds, scopes and local coefficient fields.","",
        "## Actual execution","","| Item | Recorded value |","|---|---|"]
    for label,value in (
        ("Run / attempt",str(state["run_id"])+"/"+str(state["run_attempt"])),
        ("Workflow event",state["workflow_commit"]),
        ("Actual checkout",state.get("actual_scientific_checkout_commit","not launched")),
        ("Scientific source SHA256",state["source_sha256"]),
        ("New math module SHA256",SCIENCE_PIN_SHA256["math_module"]),
        ("Manifest SHA256",state["input_manifest_sha256"]),
        ("Complete dual-file mathematics",complete),
        ("Complete original-input admission",admitted),
        ("Actual return code",state.get("actual_returncode")),
        ("New scientific children",state["actual_new_scientific_processes"])):
        lines.append("| "+cell(label)+" | "+cell(value)+" |")
    lines+=["","## Complete new records","","| Record | Outward value |","|---|---|"]
    if complete:
        flow=s["complete_higher_flow_and_cut_conclusion"]
        local=s["complete_local_regular_packet_conclusion"]
        for label,value in (
            ("Actual cut phase derivative lower",flow["cut_phase_lower"]),
            ("All strict phase derivative lower",flow["strict_phase_lower"]),
            ("Qualified local cover margin",local["local_cover_saved_h_margin"])):
            lines.append("| "+cell(label)+" | "+cell(ball(value))+" |")
        for field,key,label in (
            ("complete_strict_forcing_conclusion","Fa","Strict complete Fa, highest saved group"),
            ("complete_strict_forcing_conclusion","Fb","Strict complete Fb, highest saved group"),
            ("complete_free_first_transport_conclusion","a1","Free a1, highest saved group"),
            ("complete_free_first_transport_conclusion","b1","Free b1, highest saved group")):
            group="complete_forcing_jets" if field=="complete_strict_forcing_conclusion" else "complete_jets"
            value=s[field][group][key]["group_upper"][-1]
            lines.append("| "+cell(label)+" | "+cell(ball(value))+" |")
        lines+=["","Main: all 437 new records and both full patches. Input copy: 66 current and 40 stage records, nine scopes and every local coefficient field."]
    else:
        lines+=["| Complete new targets | not admitted |","",
            "Every returned atomic stage is retained. A partial result does not authorize repeating completed mathematics."]
    lines+=["","## Recorded gates","","| Gate | Passed |","|---|---|"]
    for g in s.get("gates",[]):
        lines.append("| "+cell(g.get("name"))+" | "+cell(g.get("passed"))+" |")
    lines+=["","## Actual progress","","| Counter | Value |","|---|---|"]
    for key,value in (s.get("actual_progress") or {}).items():
        lines.append("| "+cell(key)+" | "+cell(value)+" |")
    lines+=["","## Scope and preservation","",
        "Same real family and fixed eta0; both branches/signs, partial ordinary-dr intervals, 3070 interfaces and both physical means remain. The local analytic packet does not assert phase radial jets at the root. The nonzero cut trace remains.",
        "Only free jets are proved; genuine potential, N6/source/endpoints/receivers, contraction, finite/incoming inverse and nonlinear background remain unpaid.",
        "Two frozen Git gzip stages are temporary only. No old producer, target, ray, exp/log or free-amplitude budget is rerun; no gzip, array, artifact or Release is published.",
        ("The admitted input copy is bound by filename, bytes and SHA256 in the main file." if admitted else
         "Input admission is incomplete; all available files remain preserved."),
        "Four full payloads are separately printed and hashed before publication. Execution retains every pull and both README diffs."]
    checks=state.get("readme_checks",[])
    lines+=["","Latest pulls ("+str(len(checks))+" total; full history in execution.json):"]
    for check in checks[-2:]:
        lines.append("- "+cell(check["time"])+" -> "+cell(check["after"]))
    if failed:
        failure=state.get("actual_failure") or s.get("failure") or {}
        excerpt=json.dumps(failure,sort_keys=True,ensure_ascii=False)
        lines+=["",("## Operational failure after complete mathematics" if complete else "## Incomplete outcome"),"",
            cell(excerpt[:256])+(" [report excerpt; full diagnostic remains in execution/science and the job log]" if len(excerpt)>256 else ""),
            "All completed stages and available original inputs remain locked; this failure does not authorize another scientific child."]
    lines.append("")
    return "\n".join(lines)

def emit_prepublication(state,science,copies):
    """Print all four full files before format gates."""
    payloads=[
        (MAIN_FILENAME,None if science is None else compact(science),"complete_preGit_science_max_bytes"),
        (COPIES_FILENAME,None if copies is None else compact(copies),"complete_preGit_original_inputs_max_bytes"),
        ("report.md",render(state,science,copies).encode("utf-8"),"complete_preGit_report_max_bytes"),
        ("execution.json",compact(state),"complete_preGit_execution_max_bytes")]
    receipts={};oversized=[]
    for filename,raw,limit_key in payloads:
        available=raw is not None
        receipt=dict(available=available,bytes=None if raw is None else len(raw),
            sha256=None if raw is None else hashlib.sha256(raw).hexdigest(),
            limit_bytes=PUBLICATION_LIMITS[limit_key])
        receipts[filename]=receipt
        print(json.dumps(dict(marker="GLOBAL_FOLD_FREE_TRANSPORT_FINITE_JETS_PREPUBLICATION_FILE_V1",
            filename=filename,run_id=state["run_id"],run_attempt=state["run_attempt"],**receipt),
            sort_keys=True,separators=(",",":")),flush=True)
        if available:
            print("BEGIN_COMPLETE_WGS_PREPUBLICATION_FILE "+filename,flush=True)
            sys.stdout.buffer.write(raw);sys.stdout.buffer.flush()
            if not raw.endswith(b"\n"):print("",flush=True)
            print("END_COMPLETE_WGS_PREPUBLICATION_FILE "+filename,flush=True)
            if len(raw)>PUBLICATION_LIMITS[limit_key]:oversized.append(filename)
    print(json.dumps(dict(marker="GLOBAL_FOLD_FREE_TRANSPORT_FINITE_JETS_PREPUBLICATION_STATUS_V1",
        complete_mathematics=state.get("complete_mathematical_receipt_available",False),
        complete_original_inputs=state.get("complete_original_input_receipt_available",False),
        all_four_payloads_separately_printed=True,oversized_files=oversized)),flush=True)
    if oversized:
        raise ValueError("all complete WGS payloads were printed; per-file format gate failed: "+",".join(oversized))
    return dict(files=receipts,all_four_payloads_separate=True,
        every_available_payload_preserved_in_full=True,before_any_git_publication=True,
        execution_payload_precedes_this_recoverable_metadata_field=True)

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
        raise RuntimeError("only this public repository Actions may evaluate new WGS mathematics")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:
        raise ValueError("the separately pinned WGS manifest or reviewed rules changed")
    m=read(a.manifest);rules=read(a.rules)
    current=m.get("files",[])
    history=m.get("historical_inputs",[])
    current_roles={v["role"] for v in current}
    current_paths={v["path"] for v in current}
    historical_roles={v["role"] for v in history}
    historical_paths={v["path"] for v in history}
    all_entries=current+history
    if (m.get("public_repository")!=PUBLIC or rules.get("repository")!=PUBLIC
        or m.get("kind")!=MANIFEST_KIND
        or m.get("source_sha256")!=a.pipeline_sha
        or m.get("source_path")!=str(PIPELINE)
        or m.get("parameters")!=SCIENCE_PARAMETERS
        or m.get("scope")!=SCIENCE_SCOPE
        or current_roles!=(set(CURRENT_PIN_SPECS)|{"source","worker","rules"})
        or [v["role"] for v in current]!=CURRENT_ROLE_ORDER
        or m.get("current_text_input_roles")!=CURRENT_ROLE_ORDER
        or m.get("complete_input_bytes")!=sum(v["bytes"] for v in all_entries)
        or m.get("publication_limits")!=PUBLICATION_LIMITS
        or m.get("mathematical_input_sha256")!=SCIENCE_PIN_SHA256
        or m.get("expected_actual_gate_count")!=24
        or m.get("expected_current_input_count")!=20
        or m.get("expected_input_count")!=22
        or m.get("expected_immutable_AST_files")!=7
        or history!=HISTORICAL
        or m.get("historical_input_roles")!=[v["role"] for v in HISTORICAL]
        or m.get("historical_input_paths")!=[v["path"] for v in HISTORICAL]
        or m.get("file_sha256")!={x["path"]:x["sha256"] for x in current}
        or len(current_roles)!=len(current) or len(current_paths)!=len(current)
        or current_roles&historical_roles or current_paths&historical_paths
        or m.get("expected_current_input_count")!=len(current)
        or m.get("expected_input_count")!=len(all_entries)
        or m.get("expected_immutable_AST_files")!=sum(x["path"].endswith(".py") for x in current)
        or m.get("current_input_paths")!=[v["path"] for v in current]
        or m.get("input_paths")!={x["role"]:x["path"] for x in all_entries}
        or m.get("legacy_artifact_inputs")!=[]
        or m.get("all_inputs_are_current_small_texts") is not False
        or m.get("old_successful_scientific_calls_allowed") is not False
        or m.get("new_native_arrays_or_artifact_persistence_allowed") is not False):
        raise ValueError("the exact twenty-current and two-history WGS contract changed")
    by_role={v["role"]:v for v in current}
    for role,spec in CURRENT_PIN_SPECS.items():
        if any(by_role[role].get(k)!=v for k,v in spec.items()):
            raise ValueError("one frozen current mathematical input specification changed")
    if ([v["role"] for v in current if v["path"].endswith(".py")]!=AST_ROLES
        or by_role["source"]["sha256"]!=a.pipeline_sha
        or by_role["source"]["path"]!=str(PIPELINE)
        or by_role["worker"]["sha256"]!=sha(__file__)
        or by_role["worker"]["path"]!=str(Path(__file__).resolve().relative_to(root))
        or by_role["rules"]["sha256"]!=a.rules_sha):
        raise ValueError("source, worker, rules or exact seven-file AST order changed")
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
        print("Hydrated twenty pinned current texts and rule reviews; history remains unread until the same-input reuse and partial locks pass.",flush=True)
        return
    if a.work is None or a.out_dir is None:
        raise ValueError("temporary WGS work and outcome directories are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():
        raise FileExistsError("preserve the previous complete or partial WGS run")
    if any(v.is_relative_to(root) for v in (work,out)):
        raise ValueError("all temporary scientific work and restored gzip inputs must remain outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__)
    state=dict(kind="actual_public_global_fold_free_transport_finite_jets_execution_v1",repository=PUBLIC,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_commit=os.environ["GITHUB_SHA"],worker_source_sha256=ws,
        source_sha256=a.pipeline_sha,input_manifest_sha256=a.manifest_sha,
        reviewed_rules_sha256=a.rules_sha,explicitly_read_rules_commit=rules["read_commit"],
        started_utc=utc(),complete=False,actual_returncode=None,readme_checks=[],
        actual_new_scientific_processes=0,old_numerical_enclosures_recomputed=0,
        old_flow_root_or_free_amplitude_targets_recomputed=0,
        old_successful_scientific_targets_recomputed=0,old_completed_scalar_products_recomputed=0,
        old_exponentials_or_logs_recomputed=0,
        new_artifact_count=0,new_Release_count=0,
        reproducible_data_published_to_repository=False,
        complete_original_input_array_recomputation=False,
        new_per_row_arrays_retained_after_job=False,
        final_topic_complete=False)
    report=root/REPORTS/("run-"+state["run_id"]+"-"+state["run_attempt"])
    owned_paths={str((report/name).relative_to(root))
        for name in PUBLICATION_FILES}
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
            raise ValueError("a pinned WGS source manifest or rule record changed during pull")
        if sha(root/rw)!=ws:
            raise ValueError("the currently running immutable WGS wrapper changed")
        for name in m["current_input_paths"]:
            if sha(root/relpath(name))!=m["file_sha256"][name]:
                raise ValueError("an immutable current WGS source or contract changed")
        published,blobs=topic_tree_metadata(git,TOPIC,PUBLIC)
        capacity=owned_head_delta(git,root,published,blobs,owned_paths)
        state.update(current_published_topic_capacity_metadata=published,
            current_topic_capacity_metadata=capacity,current_topic_blob_bytes=capacity["blob_bytes"],
            current_topic_blob_count=capacity["blob_count"],current_topic_metadata_commit=capacity["commit"],
            current_topic_below_200000000_bytes=capacity["blob_bytes"]<200000000)
        save(out/"worker-process.json",state)
        if capacity["blob_bytes"]+PUBLICATION_LIMITS["reserved_publication_bytes"]>=200000000:
            raise ValueError("the actual topic lacks the reviewed230000-byte four-file reserve")
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
        print(json.dumps(dict(kind="GLOBAL_FOLD_FREE_TRANSPORT_FINITE_JETS_DEFERRED_READ_ONLY_METADATA_PUBLICATION",**event,
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
            raise ValueError("each current WGS input must be complete small current text")
        checked(src,entry["bytes"],entry["sha256"])
        raw=src.read_bytes()
        raw.decode("utf-8")
        if hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()!=entry["git_blob"]:
            raise ValueError("the complete current text differs from its frozen Git blob")
        dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
        checked(dst,entry["bytes"],entry["sha256"])
        return dst,dict(role=entry["role"],path=str(name),bytes=entry["bytes"],
            sha256=entry["sha256"],origin="exact_current_small_text")
    fetched_history=set()
    def restore_history(entry):
        if entry not in HISTORICAL:
            raise ValueError("an unlisted historical input was requested")
        name=relpath(entry["path"]);commit=entry["commit"];dst=work/name
        if not str(name).endswith(".json.gz") or dst.exists():
            raise ValueError("historical gzip must be missing in temporary work")
        if commit not in fetched_history:
            git("fetch","--filter=blob:none","--no-tags","origin",commit)
            if git("rev-parse",commit+"^{commit}").stdout.strip()!=commit:
                raise ValueError("the historical public commit identity changed")
            fetched_history.add(commit)
        line=git("ls-tree","-z",commit,"--",str(name)).stdout
        if not line.endswith("\0") or line.count("\0")!=1:
            raise ValueError("the historical gzip is not one exact Git entry")
        header,path=line[:-1].split("\t",1);mode,kind,digest=header.split()
        if (path!=str(name) or mode!="100644" or kind!="blob"
            or digest!=entry["git_blob_sha"]
            or int(git("cat-file","-s",digest).stdout.strip())!=entry["bytes"]):
            raise ValueError("the historical gzip metadata differs from its frozen identity")
        dst.parent.mkdir(parents=True,exist_ok=True)
        with dst.open("wb") as target:
            git("show",commit+":"+str(name),stdout=target)
        checked(dst,entry["bytes"],entry["sha256"])
        raw=dst.read_bytes()
        if (not raw.startswith(b"\x1f\x8b")
            or hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()!=digest):
            raise ValueError("historical gzip bytes or Git blob differ")
        return dst,dict(role=entry["role"],path=str(name),bytes=entry["bytes"],
            sha256=entry["sha256"],git_blob_sha=digest,commit=commit,
            origin="exact_public_git_history_gzip_bytes_only",
            old_producer_executed=False,compressed_payload_decoded_by_worker=False)
    def read_available_pair():
        return tuple(read(out/name) if (out/name).is_file() else None
                     for name in (MAIN_FILENAME,COPIES_FILENAME))
    proc=None;copies=None;child=None;runtime=None
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
            prior_copies=None;copyref=previous.get("complete_original_inputs")
            if copyref:
                if copyref.get("file")!=COPIES_FILENAME:
                    raise ValueError("prior WGS copy filename changed")
                cp=path.parent/COPIES_FILENAME
                checked(cp,copyref["bytes"],copyref["sha256"]);prior_copies=read(cp)
                if cp.read_bytes()!=compact(prior_copies):
                    raise ValueError("prior WGS copy bytes are not canonical")
            ref=previous.get("scientific_conclusion")
            if ref:
                pp=path.parent/safe_name(ref["file"])
                checked(pp,ref["bytes"],ref["sha256"])
                prior=read(pp)
                pairref=prior.get("complete_original_inputs_file") if isinstance(prior,dict) else None
                if pairref is not None:
                    if (not isinstance(pairref,dict) or set(pairref)!={"filename","bytes","sha256"}
                        or pairref["filename"]!=COPIES_FILENAME):
                        raise ValueError("prior WGS input-copy reference malformed")
                    cp=path.parent/COPIES_FILENAME
                    checked(cp,pairref["bytes"],pairref["sha256"])
                    prior_copies=read(cp)
                    er=previous.get("complete_original_inputs")
                    if (not isinstance(er,dict) or er.get("file")!=COPIES_FILENAME
                        or er.get("bytes")!=pairref["bytes"] or er.get("sha256")!=pairref["sha256"]
                        or cp.read_bytes()!=compact(prior_copies)):
                        raise ValueError("prior WGS execution and input-copy identities disagree")
                if pp.name!=MAIN_FILENAME or pp.read_bytes()!=compact(prior):
                    raise ValueError("prior WGS main bytes not canonical")
                if (previous.get("source_sha256")==a.pipeline_sha
                    and scientific_receipt_valid(prior,prior_copies,a.pipeline_sha,None,parameters,pins,runtime,previous)):
                    print(json.dumps(dict(reused_complete_same_scientific_conclusion=str(pp.relative_to(root)),
                        reused_complete_original_inputs=str(cp.relative_to(root)),
                        original_run_id=previous["run_id"],original_run_attempt=previous["run_attempt"],
                        original_science_bytes=ref["bytes"],original_science_sha256=ref["sha256"],
                        original_inputs_bytes=pairref["bytes"],original_inputs_sha256=pairref["sha256"],
                        execution_sha256=sha(path),original_wrapper_complete=previous.get("complete"),
                        new_scientific_processes=0,old_successful_mathematics_recomputed=0)),flush=True)
                    return
            if same_record and previous.get("actual_new_scientific_processes",0)>0:
                raise RuntimeError("same WGS finite jets arithmetic has a prior incomplete outcome; require its concrete review and preserved scientific-result review")
        state["mathematical_input_sha256"]=pins
        inputs=[];index_files={}
        for entry in m["files"]:
            dst,receipt=copy_current(entry)
            inputs.append(receipt)
            index_files[entry["role"]]=dict(path=str(dst),bytes=dst.stat().st_size,sha256=entry["sha256"])
            checkpoint()
        for entry in HISTORICAL:
            dst,receipt=restore_history(entry)
            inputs.append(receipt)
            index_files[entry["role"]]=dict(path=str(dst),bytes=dst.stat().st_size,sha256=entry["sha256"])
            checkpoint()
        state["old_binary_parts_restored"]=len(HISTORICAL)
        state["historical_gzip_payloads_decoded_by_worker"]=0
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
            raise ValueError("the complete WGS finite jets input and Python AST closure differs")
        if history!=HISTORICAL or state.get("old_binary_parts_restored")!=2:
            raise ValueError("only the two exact public historical gzip inputs may be restored")
        state["old_artifacts_downloaded"]=0
        state["old_producers_or_integrals_reexecuted"]=0
        state["new_artifact_count"]=0;state["new_Release_count"]=0
        cmd=[sys.executable,"-u",str(work/PIPELINE),"--repo",str(work),
            "--manifest",str(tm),"--manifest-sha",a.manifest_sha,"--bits","320",
            "--out",str(out/MAIN_FILENAME)]
        for role,digest in pins.items():
            if index_files[role]["sha256"]!=digest:
                raise ValueError("one complete WGS finite jets mathematical input identity changed")
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
        proc,copies=read_available_pair()
        admitted=original_inputs_valid(proc,copies,a.pipeline_sha,a.manifest_sha,pins)
        valid=scientific_receipt_valid(proc,copies,a.pipeline_sha,a.manifest_sha,parameters,pins,runtime,state)
        state["complete_original_input_receipt_available"]=admitted
        state["complete_mathematical_receipt_available"]=valid
        state["complete"]=bool(child.returncode==0 and valid)
        state["actual_failure"]=None if state["complete"] else (
            proc.get("failure") if proc and proc.get("failure") else
            dict(type="IncompleteScientificReceipt",message="the complete WGS finite jets scalar receipt did not validate"))
    except BaseException as error:
        if child is not None and child.poll() is None:
            os.killpg(child.pid,signal.SIGTERM)
            try:child.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(child.pid,signal.SIGKILL);child.wait()
        if child is not None:
            state["actual_returncode"]=child.poll()
        state["actual_failure"]=dict(type=type(error).__name__,message=str(error))
        proc,copies=read_available_pair()
        state["complete_original_input_receipt_available"]=original_inputs_valid(
            proc,copies,a.pipeline_sha,a.manifest_sha,m["mathematical_input_sha256"])
        state["complete_mathematical_receipt_available"]=scientific_receipt_valid(
            proc,copies,a.pipeline_sha,a.manifest_sha,m["parameters"],
            m["mathematical_input_sha256"],runtime,state)
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
    for filename in (MAIN_FILENAME,COPIES_FILENAME):
        target=out/filename
        if target.is_file():
            raw=target.read_bytes()
            print(json.dumps(dict(kind="GLOBAL_FOLD_FREE_TRANSPORT_ATOMIC_FILE_REPRINT",
                filename=filename,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())),flush=True)
            print("BEGIN_COMPLETE_WGS_ATOMIC_FILE "+filename,flush=True)
            sys.stdout.buffer.write(raw);sys.stdout.buffer.flush()
            if not raw.endswith(b"\n"):print("",flush=True)
            print("END_COMPLETE_WGS_ATOMIC_FILE "+filename,flush=True)
    state["complete_atomic_scientific_files_reprinted"]=True
    outputs=[out/name for name in (MAIN_FILENAME,COPIES_FILENAME,"new-scientific-child.stdout.log")]
    state["output_hashes"]=[rec(path,out) for path in outputs if path.is_file()]
    for filename,document,field in ((MAIN_FILENAME,proc,"scientific_conclusion"),
                                    (COPIES_FILENAME,copies,"complete_original_inputs")):
        if document is None:continue
        original=out/filename
        if original.read_bytes()!=compact(document):
            raise ValueError("the complete WGS file must retain its original canonical bytes: "+filename)
        reference=dict(file=filename,bytes=original.stat().st_size,sha256=sha(original),
            complete=document.get("complete"),original_result_printed_before_any_format_gate=True)
        if filename==MAIN_FILENAME:
            reference.update(actual_returncode=document.get("actual_returncode"),
                actual_gate_count=len(document.get("gates",[])),
                actual_passed_gate_count=sum(g.get("passed") is True for g in document.get("gates",[])))
        state[field]=reference
    save(out/"worker-process.json",state)
    state["recoverable_prepublication_stdout"]=emit_prepublication(state,proc,copies)
    save(out/"worker-process.json",state)
    # Publication changes only the four complete science/input/report/execution files.
    # Full science, every completed new stage and child log are already in stdout.
    report.mkdir(parents=True,exist_ok=True)
    def snapshot():
        text=render(state,proc,copies);names=sorted(owned_paths)
        science_raw=None if proc is None else compact(proc)
        copies_raw=None if copies is None else compact(copies)
        capacity,blobs=topic_tree_metadata(git,TOPIC,PUBLIC)
        state["publication_owned_HEAD_delta"]=owned_head_delta(git,root,capacity,blobs,owned_paths)
        total=capacity["blob_bytes"];oldbytes=sum(blobs[name]["bytes"] for name in names if name in blobs)
        state.update(publication_capacity_metadata=capacity,publication_base_topic_blob_bytes=total,
            publication_capacity_metadata_commit=capacity["commit"],projected_topic_blob_bytes=0)
        while True:
            raw=compact(state)
            projected=(total-oldbytes+len(text.encode())+len(raw)
                +(0 if science_raw is None else len(science_raw))
                +(0 if copies_raw is None else len(copies_raw)))
            if projected==state["projected_topic_blob_bytes"]:
                break
            state["projected_topic_blob_bytes"]=projected
        if projected>=200000000:
            raise ValueError("the actual complete small conclusions exceed topic capacity")
        if (len(raw)>PUBLICATION_LIMITS["complete_execution_max_bytes"]
            or len(text.encode())>PUBLICATION_LIMITS["complete_report_max_bytes"]
            or (science_raw is not None and len(science_raw)>PUBLICATION_LIMITS["complete_science_max_bytes"])
            or (copies_raw is not None and len(copies_raw)>PUBLICATION_LIMITS["complete_original_inputs_max_bytes"])):
            raise ValueError("all four full payloads are preserved in stdout; one publication format gate failed")
        (report/"report.md").write_text(text,encoding="utf-8")
        (report/"execution.json").write_bytes(raw)
        if science_raw is not None:(report/MAIN_FILENAME).write_bytes(science_raw)
        if copies_raw is not None:(report/COPIES_FILENAME).write_bytes(copies_raw)
    def publish():
        snapshot();owned=str(report.relative_to(root));git("add","--sparse","--",owned)
        if git("diff","--cached","--quiet","--",owned,check=False).returncode!=0:
            git("commit","-m","visible-exact: record complete WGS finite jets")
        while True:
            result=git("push","origin","HEAD:refs/heads/main",check=False)
            if result.returncode==0:
                return owned
            if not any(v in result.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
                raise RuntimeError("small WGS conclusion push failed outside concurrent-main rebase")
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
