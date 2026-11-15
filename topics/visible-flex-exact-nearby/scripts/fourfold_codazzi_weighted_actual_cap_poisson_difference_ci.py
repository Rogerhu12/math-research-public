#!/usr/bin/env python3
"""Consume complete small RW and F receipts for new weighted actual-cap derivative decisions."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import re,gzip,zipfile,urllib.error,urllib.parse,urllib.request
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_weighted_actual_cap_poisson_difference.py"
REPORTS=TOPIC/"notes/weighted_actual_cap_poisson_difference_ci"
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def save(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+".partial")
    t.write_text(json.dumps(v,indent=2,ensure_ascii=False,allow_nan=False)+"\n");t.replace(p)
def checked(p,size,digest):
    p=Path(p)
    if not p.is_file() or p.stat().st_size!=size or sha(p)!=digest:
        raise ValueError("a complete pinned input differs: "+str(p))
def read(p):return json.loads(Path(p).read_text())
def relpath(p):
    p=Path(p)
    if p.is_absolute() or ".." in p.parts or not str(p).startswith(str(TOPIC)+"/"):
        raise ValueError("an input left the authorized topic")
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
        try:
            with opener.open(request,timeout=45) as response:
                if response.geturl()!=url:
                    raise RuntimeError("the capacity metadata request was redirected")
                data=response.read(16000001)
        except urllib.error.HTTPError as error:
            raise RuntimeError("the Git tree metadata request returned HTTP "+str(error.code)) from None
        except urllib.error.URLError:
            raise RuntimeError("the Git tree metadata request failed at transport") from None
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
            raise ValueError("an unpublished local topic change is outside the two owned small conclusions")
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
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()

def scientific_receipt_valid(proc,source,manifest):
    return (isinstance(proc,dict)
        and proc.get("kind")=="actual_weighted_cap_Poisson_difference_v1"
        and proc.get("complete") is True and proc.get("failure") is None
        and proc.get("actual_returncode")==0 and proc.get("source_sha256")==source
        and proc.get("input_manifest_sha256")==manifest
        and proc.get("proved_complete_weighted_inner_cap_difference_diagnosis") is True
        and len(proc.get("gates",[]))==18 and all(g.get("passed") is True for g in proc["gates"])
        and len(proc.get("complete_gamma_domain_cases",[]))==2
        and len(proc.get("original_feedback_cases_copied",[]))==2
        and proc["original_feedback_cases_copied"][0].get("all_strict_sufficient_gates_passed") is True
        and proc["original_feedback_cases_copied"][1].get("all_strict_sufficient_gates_passed") is False
        and all(isinstance(c.get("all_new_strict_sufficient_gates_passed"),bool)
            and c.get("unweighted_whole_body_difference_claimed") is False
            and c.get("affine_cap_mismatch_or_new_height_direction_paid") is False
            for c in proc["complete_gamma_domain_cases"])
        and proc.get("complete_inner_B_and_Cmean_pair_is_the_only_kappa_output") is True
        and proc.get("full_even_mean_and_all_physical_modes_retained") is True
        and proc.get("unknown_high_and_original_full97_coordinates_retained") is True
        and all(proc.get(k) is False for k in (
            "infinite_BVP_inverse_proved","actual_core_solution_or_full_matching_proved",
            "new_physical_cap_domain_entry_proved","affine_cap_mismatch_or_boundary_nonlinearity_proved",
            "independent_new_height_or_waist_source_proved","new_recomputable_arrays_persisted"))
        and all(proc.get(k)==0 for k in (
            "original_Green_native_matrix_Gram_sweep_or_target_calls",
            "original_residual_primitive_repair_Riccati_or_integral_calls","original_F_case_recomputations")))

def render(state):
    r=state.get("actual_scientific_receipt",{})
    lines=["# Actual weighted cap inner Poisson difference and finite193 feedback","",
        "This public scalar consumer reads completed RW and F conclusions unchanged.",
        "Every strict prerequisite and finite feedback verdict is separate from structural success.","",
        "- Run: "+str(state["run_id"])+"/"+str(state["run_attempt"]),
        "- Scientific child return: "+str(state.get("actual_returncode")),
        "- Complete scalar receipt: "+str(scientific_receipt_valid(r,state["source_budget_source_sha256"],state["input_manifest_sha256"])),
        "- Source SHA256: "+state["source_budget_source_sha256"],
        "- Manifest SHA256: "+state["input_manifest_sha256"],
        "- Old source integrals, Green products, cap solutions and accepted F cases repeated: 0.",""]
    if r:
        k=r.get("new_weighted_constants",{})
        lines+=["## Complete weighted prerequisites","",
            "- Strict prerequisites: "+json.dumps(k.get("prerequisite_strict_checks",{}),sort_keys=True),
            "- Complete old-reference Hilbert feedback: "+ball(k.get("old_reference_chi")),
            "- Corresponding strict gap: "+ball(k.get("old_reference_gap")),
            "",
            "The Q input uses separate uniform B and C envelopes and the independent C mean.",
            "The original Wiener pair budget is not substituted for the Hilbert pair norm.",""]
        constants=k.get("complete_constants",{})
        if constants:
            lines+=["| Complete new constant | Directed bound |","|---|---:|"]
            for name in (
                "Q_Hilbert_pair_complete_upper","Q_B_nonmean_component_upper","Q_C_nonmean_component_upper",
                "U_w","V_w","O_B","O_C","d_minus_lower",
                "old_Hessian_weighted_body_complete","old_Hessian_inner_pair_complete",
                "right_D_to_left_weighted","right_Cmean_to_left_weighted"):
                lines.append("| "+cell(name)+" | "+cell(ball(constants.get(name)))+" |")
        lines+=["","## Both original F cases remain unchanged","",
            "| Original case | Original physical cap kappa | Original strict verdict |","|---|---:|---:|"]
        for old in r.get("original_feedback_cases_copied",[]):
            lines.append("| "+cell(old["name"])+" | "+cell(old["physical_cap_kappa"])+" | "+
                str(old["all_strict_sufficient_gates_passed"])+" |")
        for c in r.get("complete_gamma_domain_cases",[]):
            lines+=["","## "+c["name"],"",
                "- Physical nonmean gamma A0 radius: "+c["physical_gamma_A0_radius"],
                "- Complete weighted difference available: "+str(c["complete_weighted_difference_bound_available"]),
                "- Inner B-L2 plus absolute C-mean operator bound: "+ball(c.get("inner_pair_kappa")),
                "- This is not an unweighted whole-cap difference bound.",
                "- The actual product domain and affine/nonlinear matching sources are still required."]
            if c.get("complete_weighted_difference_bound_available"):
                lines+=["- Complete weighted value: "+ball(c["complete_weighted_value_upper"]),
                    "- Complete weighted difference field: "+ball(c["weighted_body_difference_upper"]),
                    "- Original threshold comparison: "+str(c["old_threshold_diagnostic_strict_comparison"])]
                finite=c["new_finite_feedback"]
                lines+=["- New full97 row epsilon: "+ball(finite["epsilon_low"]),
                    "- Complete finite determinant: "+ball(finite["determinant"]),
                    "- Three strict finite gates: "+json.dumps(finite["strict_sufficient_gates"],sort_keys=True),
                    "- Conditional finite inverse: "+str(finite["finite193_inverse_under_stated_boundary_hypotheses_proved"])]
                if finite.get("transferred_columns") is not None:
                    lines+=["","| Independent input | Whole core output | Fixed negative output | True cut output |",
                        "|---|---:|---:|---:|"]
                    for name,values in finite["transferred_columns"].items():
                        lines.append("| "+cell(name)+" | "+" | ".join(cell(ball(values[key])) for key in (
                            "whole_inner_body","fixed_complete_negative_phase_window","true_cut_trace"))+" |")
                    lines+=["","The additional parameter columns below cover only their stated volume source."]
                    for name,value in finite["additional_parameter_volume_response_bound"].items():
                        lines.append("- "+name+": "+ball(value))
                else:
                    lines+=["","No inverse column is asserted for a nonpassing sufficient comparison."]
        lines+=["","## Complete input and evaluation gates",""]
        for g in r.get("gates",[]):lines.append("- "+("PASS" if g["passed"] else "FAIL")+": "+g["name"])
    if state.get("actual_failure"):
        lines+=["","## Actual failure","",json.dumps(state["actual_failure"],sort_keys=True)]
    lines+=["","## Real pull and storage record",""]
    for check in state.get("readme_checks",[]):
        lines.append("- "+check["time"]+" -> "+check["after"]+"; README diff empty: "+str(check["actual_diff"]==""))
    lines+=["","The execution record preserves all original copied balls and the complete new scalar conclusion.",
        "No native array, Release or new numerical artifact is persisted.",
        "Actual cap entry, affine and nonlinear boundary loads, waist and independent height, the infinite high inverse, true parameter Schur and complete core matching remain separate.",""]
    return "\n".join(lines)

def emit_recoverable_conclusion(state):
    payload=dict(marker="WEIGHTED_ACTUAL_CAP_POISSON_DIFFERENCE_PREPUBLICATION_V1",
                 execution=state,report_text=render(state))
    raw=compact(payload)
    if len(raw)>59000:
        # The complete small scientific receipt remains intact; the report is a derived display.
        payload.pop("report_text");raw=compact(payload)
    if len(raw)>59000:raise ValueError("the complete small prepublication evidence exceeds 59000 bytes")
    print(raw.decode("utf-8"),end="",flush=True)
    return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),encoding="UTF-8",
                complete_scientific_receipt_preserved=True,published_before_any_git_publication=True)

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
        raise RuntimeError("only the public repository Actions may evaluate new scalar mathematics")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:
        raise ValueError("the separate manifest or reviewed rules changed")
    m=read(a.manifest);rules=read(a.rules)
    if (m.get("public_repository")!=PUBLIC or rules.get("repository")!=PUBLIC
        or m.get("kind")!="immutable_weighted_actual_cap_poisson_difference_inputs_v1"
        or m.get("expected_actual_gate_count")!=18
        or m.get("files")!={x["path"]:x["sha256"] for x in m["file_receipts"]}
        or len(m["files"])!=len(m["file_receipts"])):
        raise ValueError("the new immutable scalar input contract changed")
    for key in ("reproducible_data_persisted_in_repository","reproducible_data_persisted_in_Releases",
                "new_reproducible_Actions_output_uploads"):
        if rules["large_data_policy"].get(key) is not False:
            raise ValueError("the current no-recomputable-data rule15 is required")
    rm=a.manifest.relative_to(root);rr=a.rules.relative_to(root);rw=Path(__file__).resolve().relative_to(root)
    gb=["git","-c","safe.directory="+str(root)]
    if a.mode=="hydrate":
        paths={str(PIPELINE),str(rw),str(rm),str(rr),str(REPORTS)+"/"}|set(rules["readme_sha256"])
        paths.update(entry["path"] for entry in m["file_receipts"])
        paths.add(m["operational_live_review_index"])
        paths.add(str(TOPIC/"notes")+"/*reviewed-public-CI-rules*.json")
        subprocess.run(gb+["sparse-checkout","set","--no-cone","--stdin"],cwd=root,
            input="\n".join("/"+v for v in sorted(paths))+"\n",text=True,check=True)
        print("Hydrated only pinned small scripts, proofs, complete conclusions and explicit rule reviews.",flush=True)
        return
    if a.work is None or a.out_dir is None:raise ValueError("temporary work and outcome directories are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():raise FileExistsError("preserve an existing actual run")
    if any(v.is_relative_to(root) for v in (work,out)):raise ValueError("recomputable inputs must stay outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__);hist=m["historical_input_commit"]
    state=dict(kind="actual_public_weighted_actual_cap_poisson_difference_execution_v1",repository=PUBLIC,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_commit=os.environ["GITHUB_SHA"],worker_source_sha256=ws,
        source_budget_source_sha256=a.pipeline_sha,input_manifest_sha256=a.manifest_sha,
        reviewed_rules_sha256=a.rules_sha,explicitly_read_rules_commit=rules["read_commit"],
        started_utc=utc(),complete=False,actual_returncode=None,readme_checks=[],
        actual_source_budget_processes=0,old_numerical_enclosures_recomputed=0,
        reproducible_data_published_to_repository=False,reproducible_data_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False,full_high_inverse_claimed=False,final_topic_complete=False)
    report=root/REPORTS/("run-"+state["run_id"]+"-"+state["run_attempt"])
    owned_paths={str((report/name).relative_to(root)) for name in ("actual-result.md","execution.json")}
    env=os.environ.copy();token=env.pop("GITHUB_TOKEN")
    env.update(GIT_TERMINAL_PROMPT="0",GIT_CONFIG_COUNT="1",
        GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
        GIT_CONFIG_VALUE_0="AUTHORIZATION: basic "+base64.b64encode(("x-access-token:"+token).encode()).decode())
    def git(*args,check=True,stdout=None):
        result=subprocess.run(gb+list(args),cwd=root,env=env,text=stdout is None,
            stdout=subprocess.PIPE if stdout is None else stdout,stderr=subprocess.PIPE,timeout=900)
        if check and result.returncode:
            error=result.stderr if isinstance(result.stderr,str) else result.stderr.decode("utf-8","replace")
            raise RuntimeError("public Git "+str(args[0])+" failed: "+error[:1200])
        return result
    def sync():
        before=git("rev-parse","HEAD").stdout.strip();git("pull","--rebase","origin","main")
        after=git("rev-parse","origin/main").stdout.strip()
        diff=git("diff",before,after,"--",*rules["readme_sha256"]).stdout
        state["readme_checks"].append(dict(time=utc(),before=before,after=after,actual_diff=diff,
            explicitly_reviewed_commit=rules["read_commit"]))
        save(out/"worker-process.json",state)
        try:
            reviewed=accept_live_rules(root,git,rules,m,state)
        except Exception:
            print(diff,flush=True);raise
        state["readme_checks"][-1].update(accepted_review_sha256=reviewed["sha256"],
            separately_read_rules_commit=reviewed["read_commit"])
        if sha(a.rules)!=a.rules_sha or sha(a.manifest)!=a.manifest_sha or sha(root/PIPELINE)!=a.pipeline_sha:
            raise ValueError("the separately pinned scalar contract changed during pull")
        if sha(root/rw)!=ws:raise ValueError("the running scalar wrapper changed during pull")
        published,blob_map=topic_tree_metadata(git,TOPIC,PUBLIC)
        capacity=owned_head_delta(git,root,published,blob_map,owned_paths)
        state.update(current_published_topic_capacity_metadata=published,
            current_topic_capacity_metadata=capacity,current_topic_blob_bytes=capacity["blob_bytes"],
            current_topic_blob_count=capacity["blob_count"],current_topic_metadata_commit=capacity["commit"],
            current_topic_below_200000000_bytes=capacity["blob_bytes"]<200000000)
        save(out/"worker-process.json",state)
        if capacity["blob_bytes"]+120000>=200000000:
            raise ValueError("the actual topic has insufficient room for two complete small conclusions")
    last_checkpoint=time.monotonic()
    def checkpoint(force=False):
        nonlocal last_checkpoint
        save(out/"worker-process.json",state)
        if force or time.monotonic()-last_checkpoint>=600:
            sync();last_checkpoint=time.monotonic()
    proc=None;child=None
    try:
        git("config","user.name","github-actions[bot]")
        git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
        sync();last_checkpoint=time.monotonic()
        for path in sorted((root/REPORTS).glob("*/execution.json")):
            previous=read(path)
            prior_science=previous.get("actual_scientific_receipt")
            same_identity=(previous.get("worker_source_sha256")==ws
                and previous.get("input_manifest_sha256")==a.manifest_sha
                and previous.get("source_budget_source_sha256")==a.pipeline_sha)
            if same_identity and previous.get("actual_returncode") not in (None,0):
                raise RuntimeError("the same exact mathematical child already failed; preserve its outcome until a concrete correction")
            if (previous.get("actual_returncode")==0
                and previous.get("worker_source_sha256")==ws
                and previous.get("input_manifest_sha256")==a.manifest_sha
                and previous.get("source_budget_source_sha256")==a.pipeline_sha
                and scientific_receipt_valid(prior_science,a.pipeline_sha,a.manifest_sha)):
                original_outputs=[entry for entry in previous.get("output_hashes",[])
                    if entry.get("file")=="actual-scalar-conclusion.json"]
                native_bytes=compact(prior_science)
                if (len(original_outputs)!=1 or original_outputs[0].get("bytes")!=len(native_bytes)
                    or original_outputs[0].get("sha256")!=hashlib.sha256(native_bytes).hexdigest()):
                    raise ValueError("a prior complete small mathematical receipt lost its exact output identity")
                print(json.dumps(dict(reused_existing_complete_conclusion=str(path.relative_to(root)),
                    original_run_id=previous["run_id"],execution_sha256=sha(path),
                    original_scientific_conclusion_sha256=original_outputs[0]["sha256"],
                    original_wrapper_complete=previous.get("complete"),
                    original_later_infrastructure_failure=previous.get("actual_failure"),
                    new_source_budget_processes=0,old_enclosures_recomputed=0)),flush=True)
                return
        if len(hist)!=40 or any(c not in "0123456789abcdef" for c in hist):
            raise ValueError("the old input recovery commit is not immutable")
        git("fetch","--filter=blob:none","--no-tags","origin",hist)
        state["historical_input_commit"]=hist;inputs=[]
        for entry in m["file_receipts"]:
            rel=relpath(entry["path"]);dst=work/rel;dst.parent.mkdir(parents=True,exist_ok=True)
            if ((root/rel).is_file() and (root/rel).stat().st_size==entry["bytes"]
                and sha(root/rel)==entry["sha256"]):
                shutil.copyfile(root/rel,dst);origin="exact_current_small_input"
            elif entry["path"] in m["current_input_paths"]:
                raise ValueError("a new exact source or contract is absent from the current checkout")
            else:
                with dst.open("wb") as stream:git("show",hist+":"+str(rel),stdout=stream)
                origin="exact_public_historical_small_input"
            checked(dst,entry["bytes"],entry["sha256"])
            inputs.append(dict(path=str(rel),bytes=entry["bytes"],sha256=entry["sha256"],origin=origin))
            checkpoint()
        state["actual_verified_input_count"]=len(inputs)
        state["actual_verified_input_receipts_sha256"]=hashlib.sha256(compact(inputs)).hexdigest()
        state["actual_current_contract_receipts"]=[e for e in inputs if e["path"] in m["current_input_paths"]]
        tm=work/rm;tm.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.manifest,tm)
        checked(tm,a.manifest.stat().st_size,a.manifest_sha)
        tr=work/rr;tr.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.rules,tr)
        checked(tr,a.rules.stat().st_size,a.rules_sha)
        parsed=[]
        for entry in m["file_receipts"]:
            if entry["path"].endswith(".py"):
                path=work/relpath(entry["path"]);ast.parse(path.read_text(),filename=str(path))
                parsed.append(dict(path=entry["path"],sha256=entry["sha256"]))
        state.update(complete_immutable_Python_AST_closure_passed=True,
            complete_immutable_Python_AST_file_count=len(parsed),
            complete_immutable_Python_AST_inventory_sha256=hashlib.sha256(compact(parsed)).hexdigest())
        cmd=[sys.executable,"-u",str(work/PIPELINE),"--root",str(work),
            "--manifest",str(tm),"--manifest-sha",a.manifest_sha,
            "--out",str(out/"actual-scalar-conclusion.json"),"--bits","320"]
        state["command_sha256"]=hashlib.sha256(compact(cmd)).hexdigest()
        state["actual_scientific_checkout_commit"]=git("rev-parse","HEAD").stdout.strip()
        state["actual_source_budget_processes"]=1;save(out/"worker-process.json",state)
        ce=os.environ.copy();ce.pop("GITHUB_TOKEN",None)
        started=time.monotonic()
        with (out/"source-budget.stdout.log").open("wb") as log:
            child=subprocess.Popen(cmd,cwd=work,env=ce,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            while child.poll() is None:
                if time.monotonic()-started>1800:
                    state["timeout_seconds"]=1800;os.killpg(child.pid,signal.SIGTERM)
                    try:child.wait(timeout=10)
                    except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
                    break
                time.sleep(1);checkpoint()
            state["actual_returncode"]=child.returncode
        state["source_budget_child_wall_seconds"]=time.monotonic()-started
        path=out/"actual-scalar-conclusion.json"
        proc=read(path) if path.is_file() else None
        state["complete_mathematical_receipt_available"]=scientific_receipt_valid(proc,a.pipeline_sha,a.manifest_sha)
        if child.returncode!=0 or proc is None:
            diagnostic=out/"source-budget.stdout.log"
            raw=diagnostic.read_bytes() if diagnostic.is_file() else b""
            state["actual_child_diagnostic_full_bytes"]=len(raw)
            state["actual_child_diagnostic_full_sha256"]=hashlib.sha256(raw).hexdigest()
            state["actual_child_diagnostic_is_complete"]=len(raw)<=16384
            shown=raw if len(raw)<=16384 else raw[:4096]+b"\n[bounded middle omitted; full log identity retained]\n"+raw[-12288:]
            state["actual_child_diagnostic_text"]=shown.decode("utf-8","replace")
            print("BEGIN_WEIGHTED_CAP_ACTUAL_CHILD_DIAGNOSTIC",flush=True)
            print(state["actual_child_diagnostic_text"],flush=True)
            print("END_WEIGHTED_CAP_ACTUAL_CHILD_DIAGNOSTIC",flush=True)
        state["complete"]=bool(child.returncode==0 and scientific_receipt_valid(proc,a.pipeline_sha,a.manifest_sha))
        state["actual_failure"]=None if state["complete"] else (
            proc.get("failure") if proc and proc.get("failure") else
            dict(type="IncompleteScientificReceipt",message="the complete eighteen-gate scalar receipt did not validate"))
    except BaseException as error:
        if child is not None and child.poll() is None:
            os.killpg(child.pid,signal.SIGTERM)
            try:child.wait(timeout=10)
            except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
            state["actual_returncode"]=child.returncode
        if child is not None:state["actual_returncode"]=child.poll()
        state["actual_failure"]=dict(type=type(error).__name__,message=str(error))
        path=out/"actual-scalar-conclusion.json"
        if path.is_file():proc=read(path)
        if proc is not None:
            state["complete_mathematical_receipt_before_infrastructure_failure"]=scientific_receipt_valid(
                proc,a.pipeline_sha,a.manifest_sha)
        state["complete"]=False
    if proc is not None:state["actual_scientific_receipt"]=proc
    outputs=[out/name for name in ("actual-scalar-conclusion.json","source-budget.stdout.log")]
    state["output_hashes"]=[rec(path,out) for path in outputs if path.is_file()]
    save(out/"worker-process.json",state)
    state["recoverable_prepublication_stdout"]=emit_recoverable_conclusion(state)
    save(out/"worker-process.json",state)
    sync();report.mkdir(parents=True,exist_ok=True)
    def snapshot():
        text=render(state);names=sorted(owned_paths)
        capacity,blob_map=topic_tree_metadata(git,TOPIC,PUBLIC)
        state["publication_owned_HEAD_delta"]=owned_head_delta(git,root,capacity,blob_map,owned_paths)
        total=capacity["blob_bytes"];oldbytes=sum(blob_map[name]["bytes"] for name in names if name in blob_map)
        state.update(publication_capacity_metadata=capacity,publication_base_topic_blob_bytes=total,
                     publication_capacity_metadata_commit=capacity["commit"],projected_topic_blob_bytes=0)
        while True:
            raw=compact(state);projected=total-oldbytes+len(text.encode())+len(raw)
            if projected==state["projected_topic_blob_bytes"]:break
            state["projected_topic_blob_bytes"]=projected
        if projected>=200000000:raise ValueError("the complete small conclusions exceed topic capacity")
        if len(raw)>60000 or len(text.encode())>60000:
            raise ValueError("the complete small scientific evidence exceeds the publication size limit")
        (report/"actual-result.md").write_text(text);(report/"execution.json").write_bytes(raw)
    snapshot();owned=str(report.relative_to(root));git("add","--sparse","--",owned)
    git("commit","-m","visible-exact: record weighted actual-cap inner Poisson difference and finite193 feedback")
    while True:
        result=git("push","origin","HEAD:refs/heads/main",check=False)
        if result.returncode==0:break
        if not any(value in result.stderr for value in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
            raise RuntimeError("small conclusion push failed outside concurrent-main rebase")
        sync();snapshot();git("add","--sparse","--",owned);git("commit","--amend","--no-edit")
    print(json.dumps(dict(complete=state["complete"],actual_returncode=state["actual_returncode"],
        report=owned,old_numerical_enclosures_recomputed=0,
        actual_source_budget_processes=state["actual_source_budget_processes"],
        reproducible_output_files_persisted=0)),flush=True)
    if not state["complete"]:raise SystemExit(1)

if __name__=="__main__":main()
