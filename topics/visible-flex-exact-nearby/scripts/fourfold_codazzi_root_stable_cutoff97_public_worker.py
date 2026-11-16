#!/usr/bin/env python3
"""Public original-cutoff97 stable trace from complete saved root inputs."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import urllib.error,urllib.request,select,importlib.metadata
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_root_stable_cutoff97_scalar_gate.py"
REPORTS=TOPIC/"notes/root_stable_cutoff97_scalar_gate_ci"
HISTORICAL=json.loads("[{\"role\":\"majorants_native\",\"path\":\"topics/visible-flex-exact-nearby/notes/correlated_adjacent_piece_first_Airy_sources_ci/run-43676926141-1/consumers/stages/complete-original-reference-holomorphic-majorants.json.gz\",\"commit\":\"a3d84d905ce72e3a854874bbe98d119623f3f8de\",\"git_blob_sha\":\"fe180735fb6cbfaef8dff2ef68aa511ed3ac0643\",\"bytes\":4501,\"sha256\":\"29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144\"},{\"role\":\"root_native\",\"path\":\"topics/visible-flex-exact-nearby/notes/current_root_scalarization_ci/run-43594466882-1/consumers/complete-moving-root-scalarization.json.gz\",\"commit\":\"46f127c7153f5393dcd2a00f42d4c1d3662c294d\",\"git_blob_sha\":\"1b1c6f11478c800ef76e1519c266e80b9d08916c\",\"bytes\":30595,\"sha256\":\"10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f\"}]")
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
SCIENCE_FIELDS=json.loads("[\"kind\",\"complete\",\"proved\",\"actual_returncode\",\"failure\",\"stage\",\"source_sha256\",\"input_manifest_sha256\",\"public_repository\",\"run_id\",\"run_attempt\",\"workflow_event_commit\",\"actual_scientific_checkout_commit\",\"runtime\",\"arithmetic_bits\",\"parameters\",\"input_sha256\",\"verified_original_inputs\",\"accepted_old_inputs\",\"copied_old_inputs\",\"copied_old_inputs_sha256\",\"complete_mixed_norm_conclusion\",\"complete_root_domain_conclusion\",\"complete_real_radial_interval_conclusion\",\"complete_root_drift_conclusion\",\"complete_rational_quotient_conclusion\",\"complete_correlated_coefficient_conclusion\",\"complete_ordered_operator_conclusion\",\"original_cutoff97_sufficient_gate_passed\",\"retained_scope\",\"counts\",\"gates\",\"actual_mathematical_wall_seconds\"]")
SCIENCE_GATE_NAMES=json.loads("[\"actual public Actions runtime and frozen new source\",\"complete current and two-history manifest closure\",\"all fifteen mathematical originals and sixteen current texts match byte pins\",\"original high-root intrinsic run is complete at its fixed bump-zero root\",\"only separately successful auxiliary cases are accepted and its global failure stays visible\",\"root process and publication bind the same complete sharper native\",\"potential actual success separates the root case from the full terminal case\",\"genuine terminal Ai uses its original nonzero shear and both full columns\",\"FA2 success preserves the complete original mixed-stage payload\",\"restored root native has its original complete ordinary L2 and left derivative identity\",\"restored original 4501-byte stage has its complete no-LF payload identity\",\"all actual inputs restrict to the same real family and single root piece\",\"every complete original mixed and angular row is finite with full means\",\"complete mixed selection and actual independent root gaps are finite\",\"complete real moments and neighborhood radial derivatives retain all mean terms\",\"complete mixed drift derivatives and every D squared p term are finite\",\"complete rational quotient retains both gaps and all third ordinary derivatives\",\"complete collected correlations preserve all nine derivative groups and the true mean\",\"all ordered operator terms and genuine positive diagonal bounds are complete\",\"the optional strict comparison has its exact narrow ordinary L2 scope\",\"all original input bytes remain unchanged with zero old target calls\",\"complete scalar schema retains every conclusion whether the sufficient test passes or fails\"]")
SCIENCE_PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"expected_actual_gate_count\":22,\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_intrinsic_parameter\":\"-7789843107295549/4611686018427387904\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"physical_root_piece\":2549,\"physical_period\":\"pi/2\",\"normalized_angular_measure\":true,\"input_cutoff_abs_j\":97,\"physical_minimum_frequency\":388,\"physical_frequency\":\"n=4|j|\",\"exact_real_z_interval\":[\"0\",\"1/9409\"],\"frequency_relation\":\"z=j^-2=16*n^-2\",\"retained_physical_means\":2,\"old_target_calls_allowed\":0,\"old_source_imports_allowed\":0,\"expected_current_inputs\":16,\"expected_total_inputs\":18,\"expected_Python_AST_files\":2,\"expected_historical_gzip_inputs\":2,\"strict_failure_is_complete_scalar_result\":true,\"full_complex_square_claimed\":false,\"full_incoming_or_finite_Schur_inverse_claimed\":false}")
SCIENCE_SCOPE=json.loads("{\"scientific_target\":\"one complete ordinary-L2 original-cutoff97 root stable scalar comparison\",\"exact_real_parameter_family_only\":true,\"fixed_eta0_and_same_root_piece\":true,\"full_complex_square_result_claimed\":false,\"full_mean_of_v_and_every_radial_mean_retained\":true,\"independent_physical_mean_coordinates\":2,\"original_reflection_and_nonmean_inverse_domains_retained\":true,\"complete_two_reference_columns_and_two_carrier_signs_retained\":true,\"root_potential_small_case_does_not_replace_terminal_shear_case\":true,\"lambda_is_physical_root_kappa_not_frequency_Airy_scale\":true,\"positive_mean_rank_is_kept\":true,\"only_proved_diagonal_mean_subterm_vanishes\":true,\"full_IR0_uses_original_one_quarter\":true,\"input_diagonals_not_commuted_through_multipliers_or_J\":true,\"original_J1_is_complete_left_angular_derivative\":true,\"old_negative_Sobolev_norms_not_inferred_from_L2\":true,\"true_nonzero_beta_n_retained\":true,\"actual_PDE_solution_claimed\":false,\"full_incoming_inverse_claimed\":false,\"finite_Schur_inverse_claimed\":false,\"nonlinear_background_or_final_surface_claimed\":false,\"next_cutoff_or_scientific_rerun_triggered\":false}")
SCIENCE_COUNTS=json.loads("{\"original_current_mathematical_texts\":13,\"original_historical_natives\":2,\"complete_old_mixed_entries\":40,\"selected_complete_mixed_entries\":40,\"original_auxiliary_successful_cases\":2,\"original_auxiliary_failed_cases_retained\":2,\"reciprocal_eta_derivatives\":4,\"alpha_ordinary_derivatives\":4,\"Q1_ordinary_derivatives\":3,\"delta3_positive_groups\":5,\"DeltaRD_positive_groups\":9,\"E0_positive_groups\":4,\"H0_positive_groups\":4,\"C1_positive_groups\":7,\"amplitude_positive_groups\":2,\"R0_positive_groups\":8,\"new_original_cutoff_comparisons\":1,\"old_successful_scientific_targets_recomputed\":0,\"old_scientific_modules_imported\":0,\"new_reference_or_potential_or_fold_solutions\":0,\"new_grid_or_array_outputs\":0}")
SCIENCE_PIN_SHA256=json.loads("{\"r97_contract\":\"543ebc3899931db63bda92c31ce20d8f21013daac906e00eaf761a28ff582f74\",\"ri_proof\":\"01afb86c1d90db86732c4621abe3f35aeb7e2aea38039eaf56725127ffb8be96\",\"rbo_proof\":\"a45e0264875c1a5cded48c6f108004f3c21b6ade73247a7b02231d9b26a30f50\",\"rbg_proof\":\"157795fdc7fc415156229f5c0b9674b18f92cce1e8cef8ce8df65a271775f268\",\"rda_proof\":\"8d2570c7b28304001c785e7b7a6d4261cf127909dd59d594262fd22d42caa205\",\"rd_proof\":\"34eec24f901205c6e8002aa767484fed4832f590fbbfbb89b3a9f2ece218b81f\",\"high_root\":\"3b06c881b8b00f8bb830653b3eb290b09687b0a2576320b605ba758e2e706abe\",\"auxiliary\":\"a6783642ae2c49f66c3a7b54f1506389f24771790f3bd5a324646df8229f9728\",\"root_process\":\"9f1d18061f1b406f028916adc33484b4deea826a8e4175fd28b0fdb5b690342d\",\"potential_execution\":\"d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9\",\"genuine_execution\":\"fabe59eed2174e92352f71b8a0e9d80ce8c127580806f5dab917345b05337f57\",\"fa_science\":\"2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2\",\"root_publication\":\"89642fd97b7669449f1138d2c3de6840e19ca84dfe06b5a5a76b608239842812\",\"majorants_native\":\"29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144\",\"root_native\":\"10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f\"}")
SCIENCE_PIN_BYTES=json.loads("{\"r97_contract\":20143,\"ri_proof\":25837,\"rbo_proof\":18718,\"rbg_proof\":22284,\"rda_proof\":11486,\"rd_proof\":17725,\"high_root\":27056,\"auxiliary\":38267,\"root_process\":4120,\"potential_execution\":27645,\"genuine_execution\":16120,\"fa_science\":35718,\"root_publication\":2005,\"majorants_native\":4501,\"root_native\":30595}")

def scientific_receipt_valid(proc,source,manifest,parameters,pins,runtime):
    """Accept complete original97 scalar science even when its sufficient gate is false."""
    if not isinstance(proc,dict):
        return False
    p=proc
    def hexid(value,size):
        return isinstance(value,str) and len(value)==size and all(x in "0123456789abcdef" for x in value)
    def scalar(value):
        return isinstance(value,str) and 0<len(value)<=256 and not any(x in value.lower() for x in ("nan","inf"))
    def scalars(value,count):
        return isinstance(value,list) and len(value)==count and all(scalar(x) for x in value)
    def matrix(value,rows,columns):
        return isinstance(value,list) and len(value)==rows and all(scalars(x,columns) for x in value)
    def original_scalar(value):
        return scalar(value) or (isinstance(value,dict) and scalar(value.get("ball")))
    def original_matrix(value,rows,columns):
        return isinstance(value,list) and len(value)==rows and all(isinstance(row,list)
            and len(row)==columns and all(original_scalar(x) for x in row) for row in value)
    def fields(obj,names):
        return isinstance(obj,dict) and all(scalar(obj.get(k)) for k in names)
    try:
        if not (set(p)==set(SCIENCE_FIELDS)
            and p["kind"]=="complete_root_stable_cutoff97_scalar_gate"
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
            and p["retained_scope"]==SCIENCE_SCOPE and p["counts"]==SCIENCE_COUNTS
            and isinstance(p["gates"],list) and len(p["gates"])==22
            and [v["name"] for v in p["gates"]]==SCIENCE_GATE_NAMES
            and all(v["passed"] is True for v in p["gates"])
            and isinstance(p["actual_mathematical_wall_seconds"],(int,float))
            and p["actual_mathematical_wall_seconds"]>=0):
            return False
        old=p["accepted_old_inputs"]
        if set(old)!={"high_root","auxiliary","root","potential","genuine","FA2","majorants"}:
            return False
        for role,run,gates in (("high_root","43651259105",15),("auxiliary","43640181602",7),
            ("root","43594466882",13),("potential","43685624307",16),
            ("genuine","43688459733",16),("FA2","43763658978",24)):
            if str(old[role]["run_id"])!=run or old[role]["gates"]!=gates:
                return False
        aux=old["auxiliary"]
        if not (aux["global_complete"] is False and aux["global_returncode"]==1
            and aux["global_proved"] is False
            and aux["global_failure"]=={"type":"SystemExit","message":"1"}
            and aux["selected_exact_radius"]=="1/10000"
            and aux["successful_domains"]==["1/10000","1/2000"]
            and len(aux["failed_domains"])==2
            and old["root"]["native_sha256"]==pins["root_native"]
            and old["root"]["original_arithmetic_bits"]==256
            and old["potential"]["root_radius"]=="9/1000000"
            and old["potential"]["terminal_radius"]=="1/6000"
            and old["potential"]["root_case_whole_piece"] is False
            and old["genuine"]["full_original_terminal_certificate_retained"] is True):
            return False
        copied=p["copied_old_inputs"]
        if hashlib.sha256(compact(copied)).hexdigest()!=p["copied_old_inputs_sha256"]:
            return False
        if not (all(original_matrix(copied["mixed"][k],4,5) for k in ("U","V"))
            and all(len(copied["root_angular"][k])==5 and len(copied["aux_radial"][k])==4 for k in ("U","V"))
            and len(copied["intrinsic_K"])==len(copied["intrinsic_beta"])==4
            and len(copied["eta_moduli"])==len(copied["complete_mean_moduli"])==4
            and len(copied["root_drift"])==len(copied["aux_drift"])==3):
            return False
        projection=copied["root_record_projection"]
        expected_fields={"full_family_U_angular_norms":5,"full_family_V_angular_norms":5,
            "moving_d_Astrip":1,"moving_d_phi_Astrip":1,"moving_d_phiphi_Astrip":1,
            "inverse_same_space":1,"inverse_followed_by_angular_derivative":1,
            "L_derivative_commutator_bounds":4,"integer_derivative_recursion":5}
        if not (projection["count"]==24 and projection["original_native_sha256"]==pins["root_native"]
            and projection["original_field_counts"]==expected_fields
            and projection["unconsumed_record_fields"]==["lower","upper","mid_float","radius_upper_float"]
            and projection["original_complete_native_records_unchanged"] is True):
            return False
        inverse=copied["root_inverse"]
        native_scalars=(copied["root_angular"]["U"]+copied["root_angular"]["V"]+copied["root_drift"]
            +[inverse["inverse_same_space"],inverse["inverse_followed_by_angular_derivative"]]
            +inverse["L_derivative_commutator_bounds"]+inverse["integer_derivative_recursion"])
        if len(native_scalars)!=24 or not all(isinstance(v,dict) and set(v)=={"ball"} and scalar(v["ball"]) for v in native_scalars):
            return False
        mixed=p["complete_mixed_norm_conclusion"]
        if not (all(matrix(mixed["selected"][k],4,5) for k in ("U","V"))
            and mixed["radial_orders"]==[0,1,2,3] and mixed["physical_angular_orders"]==[0,1,2,3,4]):
            return False
        for k in ("U","V"):
            rows=mixed["selected_original_source"][k]
            if len(rows)!=4 or any(len(row)!=5 for row in rows):
                return False
            for a,row in enumerate(rows):
                for b,label in enumerate(row):
                    if label not in ({"majorants"}|({"root_angular"} if a==0 else set())|({"aux_radial"} if b==0 else set())):
                        return False
        domain=p["complete_root_domain_conclusion"]
        if not (all(scalars(domain[k],4) for k in ("beta","K","eta"))
            and fields(domain,("eta_low","lambda_low","lambda_up","qgap","k1","k2","k3","Vroot","shear","J0","J1","L0"))):
            return False
        radial=p["complete_real_radial_interval_conclusion"]
        if not fields(radial,("m_u","m_v","m_ur","eta_actual","eta_r","eta_rr","e1","e2","M","Mr","Bm","Em",
            "Bmr","Emr","ac","acp","trad","tradp","qrad","qradp","Vm","c2","c3","L","bt","bs","bA","bC")):
            return False
        drift=p["complete_root_drift_conclusion"]
        if not (fields(drift["complete_derivative_bounds"],("d","p","pphi","pphiphi","dr","pr","prphi","prr","Dp","D2p"))
            and scalars(drift["complete_projected_S_Sr_Srr"],3)
            and scalars(drift["complete_Sphi_Sphiphi_Srphi"],3)
            and scalars(drift["D2p_four_complete_terms"],4)
            and all(scalars(drift["complete_bound_candidates"][k],3)
                and drift["selected_candidate"][k] in (0,1,2) for k in ("d","p","pphi"))):
            return False
        q=p["complete_rational_quotient_conclusion"]
        if not (q["primitive_gap_exact"]=="193/9409" and q["z_interval"]==["0","1/9409"]
            and q["third_radial_derivative_only_in_C1_right_input_power"]=="-10/3"
            and scalars(q["U_radial_0_2"],3) and scalars(q["W_radial_0_1"],2)
            and all(scalars(q[k],4) for k in ("alpha_radial_0_3","reciprocal_eta_ordinary_0_3","h_ordinary_0_3"))
            and scalars(q["Q1_ordinary_0_2"],3) and scalars(q["qDelta_three_groups"],3)
            and len(q["alpha_Leibniz_terms"])==4
            and all(scalars(v,n) for v,n in zip(q["alpha_Leibniz_terms"],(1,3,6,10)))
            and len(q["Q1_complete_positive_groups"])==3
            and all(scalars(v,n) for v,n in zip(q["Q1_complete_positive_groups"],(2,5,8)))
            and scalars(q["C1_seven_groups_before_lambda_inverse_square"],7)
            and fields(q,("theta_gap_original","alpha_at_z_zero","alpha_frequency_quotient","qDelta"))
            and fields(q["complete_rational_bounds"],("C0","C1","d10"))):
            return False
        c=p["complete_correlated_coefficient_conclusion"]
        groups={"delta3_five_complete_terms":5,"ZDD_two_complete_terms":2,"WAC_two_complete_terms":2,
            "DeltaRD_nine_complete_terms":9,"E0_four_terms_before_lambda_inverse_square":4,
            "H0_four_complete_terms":4,"bop_complete_candidates":2,"D_ell_over_eta_three_terms":3,
            "signed_first_amplitude_three_terms":3}
        if not (all(scalars(c[k],n) for k,n in groups.items())
            and fields(c["radial_signed_collected_coefficients"],("P1","P2","PD","E0_coefficient","KH","astar_scalar"))
            and fields(c,("delta3","ZD","ZDD","DeltaRD","ell","ell_r","ell_phi"))
            and fields(c["complete_bounds"],("E","H","A","A1","b","V","C0","C1","d10"))
            and c["bop_selected_candidate"] in (0,1)
            and c["two_frequency_signs_share_one_multiplier"] is True
            and c["nonzero_constant_d10_kept_without_z"] is True):
            return False
        op=p["complete_ordered_operator_conclusion"]
        strict=p["original_cutoff97_sufficient_gate_passed"]
        if not (type(strict) is bool and op["original_cutoff97_sufficient_gate_passed"] is strict
            and op["root_stable_injectivity_certified"] is strict
            and op["same_window_onto_only_with_original_SE_identity"] is strict
            and op["cutoff_abs_j"]==97 and op["physical_minimum_frequency"]==388
            and fields(op,("original_shear_uniform_upper","Ai_A_upper","Ai_D_upper","genuine_diagonal_lower",
                "complete_unprojected_amplitude_upper","E2_upper","R0_upper","complete_positive_mean_rank",
                "complete_IR0_upper","high_leading_primitive_upper","same_original_J1_L0_product",
                "complete_inverse_error_upper","complete_stable_error_upper","strict_margin"))
            and set(op["right_input_powers"])=={"-1/3","-2/3","-1","-4/3","-2","-10/3","-4","-6"}
            and all(scalar(v) for v in op["right_input_powers"].values())
            and scalars(op["amplitude_two_terms"],2) and scalars(op["R0_eight_complete_terms"],8)
            and scalars(op["inverse_error_two_groups"],2)
            and op["E2_upper"]==op["complete_unprojected_amplitude_upper"]
            and op["complete_positive_mean_rank"]==op["R0_eight_complete_terms"][-1]
            and op["strict_comparison_uses_retained_75_digit_ball_endpoints"] is True
            and op["physical_independent_means_retained"] is True
            and op["full_IR0_norm_is_not_high_cut"] is True
            and all(op[k] is False for k in ("negative_window_numerical_inverse_claimed",
                "complete_incoming_inverse_claimed","finite_Schur_inverse_claimed"))):
            return False
        return True
    except (KeyError,TypeError,ValueError):
        return False

def render(state,science):
    s=science or {};op=s.get("complete_ordered_operator_conclusion",{}) or {}
    ready=s.get("complete") is True and s.get("proved") is True and s.get("stage")=="complete"
    lines=["# Actual original-cutoff97 root stable scalar gate","",
        "- Run: "+str(state["run_id"])+"/"+str(state["run_attempt"]),
        "- Actual child return: "+str(state.get("actual_returncode")),
        "- Complete mathematical receipt: "+str(state.get("complete_mathematical_receipt_available",False)),
        "- Source SHA256: "+state["source_sha256"],
        "- Manifest SHA256: "+state["input_manifest_sha256"],
        "- Complete result: [actual-scientific-conclusion.json](actual-scientific-conclusion.json).",
        "- Mathematical inputs: thirteen original small texts and two immutable original temporary gzip restores.",
        "- Old scientific targets and old source calls: 0. New artifacts and Releases: 0.",""]
    if ready:
        lines+=["## Whole original97 comparison","",
            "- Sufficient strict inequality proved: "+str(s["original_cutoff97_sufficient_gate_passed"])+".",
            "- The comparison uses the outward endpoints of the exact saved75-digit balls.","",
            "| Complete quantity | Saved enclosure |","|---|---|"]
        for label,key in (
            ("Genuine diagonal lower","genuine_diagonal_lower"),
            ("Whole stable error upper","complete_stable_error_upper"),
            ("Retained strict margin","strict_margin"),
            ("Complete E2 upper","E2_upper"),
            ("Complete R0 upper","R0_upper"),
            ("Full I R0 upper, original1/4","complete_IR0_upper"),
            ("Positive complete mean-rank fee","complete_positive_mean_rank"),
            ("Actual Airy A upper","Ai_A_upper"),
            ("Actual Airy D upper","Ai_D_upper"),
            ("Complete J1 L0 product","same_original_J1_L0_product"),
            ("Complete inverse error","complete_inverse_error_upper")):
            lines.append("| "+label+" | "+cell(op.get(key))+" |")
        coef=s.get("complete_correlated_coefficient_conclusion",{}).get("complete_bounds",{})
        lines+=["","## Complete correlated coefficient bounds","","| Quantity | Saved enclosure |","|---|---|"]
        for key in ("E","H","A","A1","C0","C1","d10"):
            lines.append("| "+key+" | "+cell(coef.get(key))+" |")
        lines+=["","Every one of the eight R0 terms and both amplitude terms is retained in the complete result. "
            "The original positive mean-rank fee is included. I R0 keeps its full1/4 norm; "
            "the third radial quotient occurs only with the right input power n^(-10/3).",""]
        if s["original_cutoff97_sufficient_gate_passed"]:
            lines+=["The complete sufficient gate holds for the same real |delta|<=10^(-8), fixed eta0 "
                "and original certified root at all |j|>=97. This certifies the normalized root stable "
                "injection; the original SE identity is required for the corresponding same-window onto statement.",""]
        else:
            lines+=["The complete scalar sufficient test did not establish the original97 gate. "
                "This is a completed upper-bound calculation and supplies no kernel or singularity conclusion. "
                "It does not trigger a new cutoff or a repeated scientific process.",""]
    else:
        lines+=["No completed original97 numerical comparison is asserted by this incomplete record.",""]
    lines+=["## Original source qualifications","",
        "The auxiliary run retains its global child1 failure; only its successful radius1/10000 case is consumed. "
        "Both failed cases remain in the result. Root lambda/V use the9/1000000 case; the nonzero Airy shear "
        "keeps its original1/6000 terminal case. Only the common real parameter family is used.","",
        "Complete mixed derivatives, full v mean and original left-angular J1 are retained. "
        "Root scalar balls are copied verbatim.","",
        "No numerical inverse on a negative window, complete incoming inverse, finite Schur inverse, "
        "nonlinear background or final surface is inferred here. Independent physical means, old low heads "
        "and every other supplied port keep their original equations.","",
        "## Structural gates",""]
    lines+=["- "+("PASS" if g["passed"] else "FAIL")+": "+g["name"] for g in s.get("gates",[])]
    if state.get("actual_failure"):
        lines+=["","## Actual failure","",json.dumps(state["actual_failure"],ensure_ascii=False,sort_keys=True)]
    lines+=["","## Actual README pulls",""]
    for row in state.get("readme_checks",[]):
        lines.append("- "+row["time"]+" -> "+row["after"]+"; README diff empty: "+str(row["actual_diff"]==""))
    return "\n".join(lines)+"\n"

def emit_prepublication(state,science):
    report=render(state,science)
    science_raw=None if science is None else compact(science)
    payload=dict(marker="ROOT_STABLE_CUTOFF97_COMPLETE_SCIENTIFIC_PREPUBLICATION_V1",
        source_sha256=state["source_sha256"],manifest_sha256=state["input_manifest_sha256"],
        run_id=state["run_id"],run_attempt=state["run_attempt"],
        actual_returncode=state.get("actual_returncode"),scientific_result=science,report_text=report)
    raw=compact(payload)
    status=dict(marker="ROOT_STABLE_CUTOFF97_PREPUBLICATION_STATUS",
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
        raise ValueError("full root-stable-cutoff97 science is saved and printed; prepublication payload exceeds90000")
    print(raw.decode(),end="",flush=True)
    process=compact(dict(marker="ROOT_STABLE_CUTOFF97_EXECUTION_PREPUBLICATION_V1",execution=state))
    if len(process)>59000:
        raise ValueError("full root-stable-cutoff97 science is preserved; execution metadata exceeds59000")
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
        raise RuntimeError("only this public repository Actions may evaluate new root-stable-cutoff97 mathematics")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:
        raise ValueError("the separately pinned root-stable-cutoff97 manifest or reviewed rules changed")
    m=read(a.manifest);rules=read(a.rules)
    current=m.get("files",[])
    history=m.get("historical_inputs",[])
    current_roles={v["role"] for v in current}
    current_paths={v["path"] for v in current}
    historical_roles={v["role"] for v in history}
    historical_paths={v["path"] for v in history}
    all_entries=current+history
    if (m.get("public_repository")!=PUBLIC or rules.get("repository")!=PUBLIC
        or m.get("kind")!="complete_root_stable_cutoff97_scalar_gate_public_inputs_v1"
        or m.get("source_sha256")!=a.pipeline_sha
        or m.get("source_path")!=str(PIPELINE)
        or m.get("parameters")!=SCIENCE_PARAMETERS
        or m.get("publication_limits")!=PUBLICATION_LIMITS
        or m.get("mathematical_input_sha256")!=SCIENCE_PIN_SHA256
        or m.get("expected_actual_gate_count")!=22
        or m.get("expected_current_input_count")!=16
        or m.get("expected_input_count")!=18
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
        or m.get("all_inputs_are_current_small_texts") is not False
        or m.get("old_successful_scientific_calls_allowed") is not False
        or m.get("new_native_arrays_or_artifact_persistence_allowed") is not False):
        raise ValueError("the exact current-text and two-historical-input root97 contract changed")
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
        raise ValueError("temporary root-stable-cutoff97 work and outcome directories are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():
        raise FileExistsError("preserve the previous complete or partial root-stable-cutoff97 run")
    if any(v.is_relative_to(root) for v in (work,out)):
        raise ValueError("all new numerical arrays must remain outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__)
    state=dict(kind="actual_public_root_stable_cutoff97_execution_v1",repository=PUBLIC,
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
            raise ValueError("a pinned root-stable-cutoff97 source manifest or rule record changed during pull")
        if sha(root/rw)!=ws:
            raise ValueError("the currently running immutable root-stable-cutoff97 wrapper changed")
        for name in m["current_input_paths"]:
            if sha(root/relpath(name))!=m["file_sha256"][name]:
                raise ValueError("an immutable current root-stable-cutoff97 source or contract changed")
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
        print(json.dumps(dict(kind="ROOT_STABLE_CUTOFF97_DEFERRED_READ_ONLY_METADATA_PUBLICATION",**event,
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
            raise ValueError("each current root-stable-cutoff97 input must be complete small current text")
        checked(src,entry["bytes"],entry["sha256"])
        dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
        checked(dst,entry["bytes"],entry["sha256"])
        return dst,dict(role=entry["role"],path=str(name),bytes=entry["bytes"],
            sha256=entry["sha256"],origin="exact_current_small_text")
    def restore_historical(entry):
        # Only the two immutable original blobs are restored. No old producer
        # is imported, executed, or added to the current sparse checkout.
        name=relpath(entry["path"]);dst=work/name
        commit=entry["commit"]
        if entry not in HISTORICAL or name.suffix!=".gz":
            raise ValueError("one historical root97 input lacks its exact reviewed identity")
        if git("cat-file","-e",commit+"^{commit}",check=False).returncode:
            git("fetch","--filter=blob:none","--no-tags","--depth=1","origin",commit)
        rows=git("ls-tree","-l","-z",commit,"--",str(name)).stdout.split("\0")
        if len(rows)!=2 or rows[-1]!="":
            raise ValueError("one original historical path is absent or ambiguous")
        header,actual_path=rows[0].split("\t")
        mode,kind,blob,size=header.split()
        if (actual_path!=str(name) or mode!="100644" or kind!="blob"
            or blob!=entry["git_blob_sha"] or int(size)!=entry["bytes"]):
            raise ValueError("one original historical Git tree identity differs")
        dst.parent.mkdir(parents=True,exist_ok=True)
        temp=dst.with_name(dst.name+".partial")
        with temp.open("wb") as stream:
            git("show",commit+":"+str(name),stdout=stream)
        checked(temp,entry["bytes"],entry["sha256"])
        body=temp.read_bytes()
        actual_blob=hashlib.sha1(b"blob "+str(len(body)).encode()+b"\0"+body).hexdigest()
        if actual_blob!=entry["git_blob_sha"]:
            raise ValueError("one original restored historical Git blob differs")
        temp.replace(dst)
        receipt=dict(entry)
        receipt.update(origin="exact_immutable_public_Git_history_temporary_restore",
            original_bytes_unmodified=True,Git_tree_identity_verified=True,
            Git_blob_identity_verified=True,old_scientific_producer_executed=False)
        return dst,receipt
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
                raise RuntimeError("same original cutoff97 stable-trace arithmetic has a prior incomplete outcome; require its concrete review and preserved scientific-result review")
        state["mathematical_input_sha256"]=pins
        inputs=[];index_files={}
        for entry in m["files"]:
            dst,receipt=copy_current(entry)
            inputs.append(receipt)
            index_files[entry["role"]]=dict(path=str(dst),bytes=dst.stat().st_size,sha256=entry["sha256"])
            checkpoint()
        for entry in history:
            dst,receipt=restore_historical(entry)
            inputs.append(receipt)
            index_files[entry["role"]]=dict(path=str(dst),bytes=dst.stat().st_size,sha256=entry["sha256"])
            state["old_binary_parts_restored"]=state.get("old_binary_parts_restored",0)+1
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
        if len(inputs)!=m["expected_input_count"] or len(parsed)!=m["expected_immutable_AST_files"]:
            raise ValueError("the complete root97 input and Python AST closure differs")
        if state.get("old_binary_parts_restored")!=2:
            raise ValueError("both original immutable historical inputs must be restored once")
        state["old_artifacts_downloaded"]=0
        state["old_producers_or_integrals_reexecuted"]=0
        state["new_artifact_count"]=0;state["new_Release_count"]=0
        cmd=[sys.executable,"-u",str(work/PIPELINE),"--repo",str(work),
            "--manifest",str(tm),"--manifest-sha",a.manifest_sha,"--bits","320",
            "--out",str(out/"actual-scientific-conclusion.json")]
        for role,digest in pins.items():
            if index_files[role]["sha256"]!=digest:
                raise ValueError("one complete root97 mathematical input identity changed")
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
            dict(type="IncompleteScientificReceipt",message="the complete root97 scalar receipt did not validate"))
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
        print(json.dumps(dict(kind="ROOT_STABLE_CUTOFF97_ATOMIC_SCIENCE_REPRINT",
            bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())),flush=True)
        print("ROOT_STABLE_CUTOFF97_SCIENTIFIC_RESULT_BEGIN",flush=True)
        print(raw.decode(),end="",flush=True)
        print("ROOT_STABLE_CUTOFF97_SCIENTIFIC_RESULT_END",flush=True)
        state["complete_atomic_scientific_result_reprinted"]=True
    outputs=[out/name for name in ("actual-scientific-conclusion.json","new-scientific-child.stdout.log")]
    state["output_hashes"]=[rec(path,out) for path in outputs if path.is_file()]
    if proc is not None:
        original=out/"actual-scientific-conclusion.json"
        if original.read_bytes()!=compact(proc):
            raise ValueError("the complete root-stable-cutoff97 child science must retain its original canonical bytes")
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
        if len(raw)>59000 or len(text.encode())>8000 or (science_raw is not None and len(science_raw)>75000):
            raise ValueError("full science is already preserved in stdout; one publication small-text gate failed")
        (report/"actual-result.md").write_text(text)
        (report/"execution.json").write_bytes(raw)
        if science_raw is not None:
            (report/"actual-scientific-conclusion.json").write_bytes(science_raw)
    def publish():
        snapshot();owned=str(report.relative_to(root));git("add","--sparse","--",owned)
        if git("diff","--cached","--quiet","--",owned,check=False).returncode!=0:
            git("commit","-m","visible-exact: record complete original cutoff97 stable-trace scalar bounds")
        while True:
            result=git("push","origin","HEAD:refs/heads/main",check=False)
            if result.returncode==0:
                return owned
            if not any(v in result.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
                raise RuntimeError("small root-stable-cutoff97 conclusion push failed outside concurrent-main rebase")
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
