#!/usr/bin/env python3
"""Public primitive-and-mean strict propagation complete source comparisons; persist only small conclusions."""
from __future__ import annotations
import argparse,ast,base64,gzip,hashlib,json,os,shutil,signal,subprocess,sys,time,zipfile
import re,urllib.error,urllib.parse,urllib.request
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_primitive_mean_strict_propagation.py"
REPORTS=TOPIC/"notes/primitive_mean_strict_propagation_ci"
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

def emit_recoverable_conclusion(state,consumers):
    """Preserve the entire small mathematical conclusion before any publication or rebase can fail."""
    path=consumers/"conclusion.md"
    result=path.read_text() if path.is_file() else "# No complete scientific conclusion was produced.\n"
    execution={key:state.get(key) for key in (
        "repository","run_id","run_attempt","workflow_commit","worker_source_sha256",
        "source_budget_source_sha256","input_manifest_sha256","reviewed_rules_sha256",
        "actual_scientific_checkout_commit","actual_returncode","complete","actual_failure",
        "actual_source_budget_processes","source_budget_child_wall_seconds",
        "actual_verified_input_count","actual_verified_input_receipts_sha256",
        "complete_immutable_Python_AST_closure_passed","complete_immutable_Python_AST_file_count",
        "complete_immutable_Python_AST_inventory_sha256","output_hashes",
        "actual_scientific_receipt")}
    payload=dict(kind="recoverable_primitive_mean_strict_propagation_small_result_v1",
        full_small_actual_result=result,execution=execution,
        native_or_stage_data_included=False)
    raw=(json.dumps(payload,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    if len(raw)>59000:raise ValueError("the complete small result and execution gate envelope exceed59000 bytes")
    identity=dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
        encoding="UTF-8",published_before_any_git_publication=True)
    print("BEGIN_R133_PRIMITIVE_MEAN_STRICT_PROPAGATION_SMALL_RESULT "+json.dumps(identity,sort_keys=True,separators=(",",":")),flush=True)
    print(raw.decode(),end="",flush=True)
    print("END_R133_PRIMITIVE_MEAN_STRICT_PROPAGATION_SMALL_RESULT",flush=True)
    return identity


def scientific_complete(proc,source,manifest):
    zeros=("old_numerical_enclosures_recomputed","old_target_FFT_intrinsic_or_repair_recomputed",
        "old_strict_H1_flow_recomputed_or_reused","old_grouped_curvature_integral_recomputed",
        "old_root_Cauchy_normalizer_or_source_enclosures_recomputed",
        "old_original_source_rows_or_radial_source_integrals_recomputed","original_natural_part_bytes_modified")
    p=proc or {}
    forward=p.get("complete_strict_propagation_conclusion",{}).get("forward_complete_matrix",[])
    reverse=p.get("complete_strict_propagation_conclusion",{}).get("reverse_complete_matrix",[])
    return bool(p.get("kind")=="actual_complete_primitive_mean_strict_propagation_v1"
        and p.get("complete") is True and p.get("proved") is True
        and p.get("actual_returncode")==0 and p.get("failure") is None
        and p.get("source_sha256")==source and p.get("input_manifest_sha256")==manifest
        and len(p.get("gates",[]))==20 and all(g.get("passed") is True for g in p["gates"])
        and p.get("original_strict_container_parts_read")==5
        and p.get("original_complete_strict_rows_verified")==3071
        and p.get("original_complete_body_prefix_parts_read")==17
        and p.get("original_complete_body_prefix_rows_verified")==3066
        and p.get("new_forward_and_reverse_ordered_products")==2
        and p.get("new_compact_log_variation_integrals")==1
        and p.get("new_common_intersection_count",0)>0
        and p.get("new_common_comparison_rows")==p.get("new_common_intersection_count")
        and p.get("new_positive_two_state_exponentials")==2*p.get("new_common_intersection_count",0)
        and all(p.get(k)==0 for k in zeros)
        and len(forward)==len(reverse)==2 and all(len(row)==2 for row in forward+reverse)
        and p.get("complete_endpoint_readout_conclusion",{}).get("all_root_and_affine_jump_inputs_still_separate") is True
        and p.get("scope",{}).get("all_Fourier_variations_and_two_means_retained") is True
        and p.get("scope",{}).get("both_chronological_Cauchy_directions_retained") is True
        and p.get("scope",{}).get("complete_current_RJ_ledger_read_verbatim") is True
        and p.get("full_high_inverse_claimed") is False
        and p.get("full_return_remainder_claimed") is False)

def api_json(path,token):
    url="https://api.github.com/repos/"+PUBLIC+path
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self,*args,**kwargs):return None
    request=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json",
        "Authorization":"Bearer "+token,"X-GitHub-Api-Version":"2022-11-28"})
    try:
        with urllib.request.build_opener(NoRedirect()).open(request,timeout=60) as response:
            if response.geturl()!=url:raise RuntimeError("the public metadata URL was redirected")
            raw=response.read(2000001)
    except (urllib.error.HTTPError,urllib.error.URLError):
        raise RuntimeError("an original public artifact metadata request failed") from None
    if len(raw)>2000000:raise ValueError("the original artifact metadata is unexpectedly large")
    return json.loads(raw)

def download_original_archive(entry,destination,token):
    metadata=api_json("/actions/artifacts/"+str(entry["id"]),token)
    if (metadata.get("id")!=entry["id"] or metadata.get("name")!=entry["name"]
        or metadata.get("size_in_bytes")!=entry["bytes"] or metadata.get("expired") is not False
        or metadata.get("digest")!="sha256:"+entry["sha256"]
        or str(metadata.get("workflow_run",{}).get("id"))!=str(entry["run_id"])
        or metadata.get("workflow_run",{}).get("head_sha")!=entry["original_workflow_commit"]):
        raise ValueError("an old complete row archive changed its public immutable identity")
    url="https://api.github.com/repos/"+PUBLIC+"/actions/artifacts/"+str(entry["id"])+"/zip"
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self,*args,**kwargs):return None
    request=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json",
        "Authorization":"Bearer "+token,"X-GitHub-Api-Version":"2022-11-28"})
    response=None
    try:
        response=urllib.request.build_opener(NoRedirect()).open(request,timeout=60)
        if response.geturl()!=url:raise RuntimeError("the authenticated artifact request was redirected")
    except urllib.error.HTTPError as error:
        if error.code not in (301,302,303,307,308):
            raise RuntimeError("the original artifact download endpoint failed") from None
        target=error.headers.get("Location","");parsed=urllib.parse.urlparse(target)
        if (parsed.scheme!="https" or not parsed.hostname or parsed.username or parsed.password
            or not any(parsed.hostname.endswith(suffix) for suffix in
                       (".blob.core.windows.net",".githubusercontent.com"))):
            raise RuntimeError("an original archive redirected outside the allowed public storage hosts") from None
        try:
            # The Actions token is deliberately not sent to the signed storage URL.
            response=urllib.request.build_opener(NoRedirect()).open(
                urllib.request.Request(target,headers={"Accept":"application/octet-stream"}),timeout=180)
            if response.geturl()!=target:raise RuntimeError("the signed old archive URL was redirected again")
        except (urllib.error.HTTPError,urllib.error.URLError):
            raise RuntimeError("the original signed archive download failed") from None
    except urllib.error.URLError:
        raise RuntimeError("the original artifact download transport failed") from None
    if response is None:raise RuntimeError("the original archive endpoint returned no response")
    destination=Path(destination);destination.parent.mkdir(parents=True,exist_ok=True)
    temporary=destination.with_name(destination.name+".partial")
    count=0;h=hashlib.sha256()
    with response,temporary.open("wb") as stream:
        while True:
            chunk=response.read(1024*1024)
            if not chunk:break
            count+=len(chunk)
            if count>entry["bytes"]:raise ValueError("the old archive exceeded its exact byte count")
            h.update(chunk);stream.write(chunk)
    if count!=entry["bytes"] or h.hexdigest()!=entry["sha256"]:
        raise ValueError("the complete old archive byte count or SHA256 differs")
    temporary.replace(destination)
    return dict(artifact_id=entry["id"],name=entry["name"],run_id=entry["run_id"],
        run_attempt=entry["run_attempt"],bytes=count,sha256=h.hexdigest(),
        token_not_forwarded_to_storage=True,only_original_archive_read=True)


def restore_original_body_prefix(m,work,root,git,token,state,checkpoint):
    old=read(work/m["input_paths"]["original_body_manifest"])
    accepted=read(work/m["input_paths"]["response_summary"])
    prior=read(work/m["input_paths"]["selected_scalar_manifest"])
    expected={tuple(e["indices"]):e["sha256"] for e in accepted["original_parts"] if e["indices"][1]<=3066}
    entries={tuple(e["indices"]):e for e in m["original_body_prefix_parts"]}
    if (len(expected)!=17 or set(entries)!=set(expected)
        or any(e["sha256"]!=expected[k] for k,e in entries.items())):
        raise ValueError("the original prefix is not exactly the seventeen accepted natural parts")
    paths={};receipts=[];archives=[]
    def put(key,payload,origin):
        if key in paths or key not in expected or hashlib.sha256(payload).hexdigest()!=expected[key]:
            raise ValueError("a complete original natural prefix is duplicated or changed")
        data=json.loads(gzip.decompress(payload))
        if (data.get("kind")!=old["residual_kind"] or data.get("identity")!=old["row_identity"]
            or data.get("selected_indices")!=list(key)
            or data.get("selected_cells_complete") is not True or data.get("failure") is not None):
            raise ValueError("an accepted complete prefix native has changed its science identity")
        path=work/relpath(entries[key]["temporary_path"])
        path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(payload);paths[key]=path
        receipts.append(dict(indices=list(key),bytes=len(payload),sha256=expected[key],origin=origin))
    history=m["original_body_historical_input_commit"]
    if history!=prior["historical_input_commit"]:raise ValueError("the original natural prefix recovery commit changed")
    for e in m["historical_natural_parts"]:
        key=tuple(e["indices"]);rel=relpath(e["path"])
        if old["already_complete_original_parts"].count(e)!=1 or prior["historical_natural_parts"].count(e)!=1:
            raise ValueError("a historical natural part lost its original two-manifest identity")
        if (root/rel).is_file() and sha(root/rel)==e["sha256"]:
            payload=(root/rel).read_bytes();origin=dict(kind="exact_current_original_natural_part")
        else:
            scratch=work/"original-body-history"/(str(key[0])+"-"+str(key[1])+".json.gz")
            scratch.parent.mkdir(parents=True,exist_ok=True)
            with scratch.open("wb") as stream:git("show",history+":"+str(rel),stdout=stream)
            payload=scratch.read_bytes();origin=dict(kind="exact_public_historical_natural_part",commit=history)
        put(key,payload,origin);checkpoint()
    if len(paths)!=4:raise ValueError("the exact four independent historical prefix parts were not restored")
    wanted={(257,1200),(1200,2133),(2133,3066)};observed=set()
    for e in m["original_row_archives"]:
        pair=tuple(e["requested_rows"])
        if pair not in wanted or pair in observed or prior["original_row_archives"].count(e)!=1:
            raise ValueError("an original complete archive is not one of the three exact prefix receipts")
        observed.add(pair)
        path=work/"original-body-archives"/(str(e["id"])+".zip")
        receipt=download_original_archive(e,path,token)
        with zipfile.ZipFile(path) as archive:
            names=archive.namelist()
            if len(names)!=len(set(names)) or any(Path(n).is_absolute() or ".." in Path(n).parts for n in names):
                raise ValueError("an original complete archive has invalid or duplicate member paths")
            if names.count("process.json")!=1:raise ValueError("the original archive has no unique actual process")
            raw=archive.read("process.json");proc=json.loads(raw)
            if (proc.get("repository")!=PUBLIC or str(proc.get("run_id"))!=str(e["run_id"])
                or str(proc.get("run_attempt"))!=str(e["run_attempt"])
                or proc.get("input_manifest_sha256")!=m["original_body_manifest_sha256"]
                or proc.get("complete") is not True or proc.get("failure")
                or tuple(proc.get("requested_rows",[]))!=pair
                or any(c.get("actual_returncode")!=0 for c in proc.get("children",[]))):
                raise ValueError("the accepted complete archive has no original successful process")
            required={tuple(v) for v in old["atomic_ranges"][str(pair[0])+"-"+str(pair[1])]}
            got=set()
            for name in names:
                if not name.startswith("native/") or not name.endswith(".json.gz"):continue
                payload=archive.read(name);v=json.loads(gzip.decompress(payload));key=tuple(v.get("selected_indices",[]))
                if key not in required or key in got:raise ValueError("an archive natural member has the wrong exact range")
                put(key,payload,dict(kind="exact_original_Actions_native",artifact_id=e["id"],member=name))
                got.add(key)
            if got!=required:raise ValueError("the accepted original archive has an incomplete natural cover")
            receipt.update(original_process_bytes=len(raw),original_process_sha256=hashlib.sha256(raw).hexdigest(),
                actual_returncodes=[c.get("actual_returncode") for c in proc.get("children",[])],
                requested_rows=list(pair),complete_natural_parts=len(got))
        archives.append(receipt);checkpoint()
    if observed!=wanted or set(paths)!=set(expected) or len(paths)!=17:
        raise ValueError("the seventeen natural prefix parts were not restored exactly")
    state["actual_original_row_archive_receipts"]=archives
    state["actual_original_natural_prefix_parts_restored"]=17
    state["actual_original_natural_prefix_rows"]=3066
    state["actual_original_part_receipts_sha256"]=hashlib.sha256(
        json.dumps(sorted(receipts,key=lambda e:e["indices"]),sort_keys=True,separators=(",",":")).encode()).hexdigest()
    state["original_parts_recomputed"]=0;state["original_part_bytes_modified"]=0
    return receipts


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--mode",choices=("hydrate","run"),required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--pipeline-sha",required=True)
    p.add_argument("--rules",type=Path,required=True)
    p.add_argument("--rules-sha",required=True)
    p.add_argument("--work",type=Path);p.add_argument("--out-dir",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("only the public repository Actions may consume the scientific inputs")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:raise ValueError("separate execution pins changed")
    m=read(a.manifest);rules=read(a.rules)
    if m["public_repository"]!=PUBLIC or rules["repository"]!=PUBLIC:raise ValueError("wrong public repository")
    for k in ("reproducible_data_persisted_in_repository","reproducible_data_persisted_in_Releases","new_reproducible_Actions_output_uploads"):
        if rules["large_data_policy"].get(k) is not False:raise ValueError("latest no-data rule15 is required")
    rm=a.manifest.relative_to(root);rr=a.rules.relative_to(root);rw=Path(__file__).resolve().relative_to(root)
    gb=["git","-c","safe.directory="+str(root)]
    if a.mode=="hydrate":
        paths={str(PIPELINE),str(rw),str(rm),str(rr),str(REPORTS)+"/"}|set(rules["readme_sha256"])
        # Every post-history input is explicitly present before freezing science.
        paths.update(e["path"] for e in m["files"] if e["path"].endswith((".py",".md")))
        paths.update(m["input_paths"][k] for k in m["current_text_input_roles"])
        subprocess.run(gb+["sparse-checkout","set","--no-cone","--stdin"],cwd=root,
            input="\n".join("/"+v for v in sorted(paths))+"\n",text=True,check=True)
        print("Hydrated the reviewed primitive-and-mean strict scalar script and current contracts; old data will remain temporary.",flush=True);return
    if a.work is None or a.out_dir is None:raise ValueError("temporary work paths are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():raise FileExistsError("preserve an existing actual execution")
    if any(v.is_relative_to(root) for v in (work,out)):raise ValueError("reproducible data must stay outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True);ws=sha(__file__)
    state=dict(kind="actual_public_primitive_mean_strict_propagation_execution",repository=PUBLIC,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_commit=os.environ["GITHUB_SHA"],worker_source_sha256=ws,
        source_budget_source_sha256=a.pipeline_sha,input_manifest_sha256=a.manifest_sha,
        reviewed_rules_sha256=a.rules_sha,explicitly_read_rules_commit=rules["read_commit"],
        started_utc=utc(),complete=False,actual_returncode=None,readme_checks=[],
        actual_source_budget_processes=0,old_numerical_enclosures_recomputed=0,
        reproducible_data_published_to_repository=False,reproducible_data_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False,full_high_inverse_claimed=False,final_topic_complete=False)
    owned_small_paths={str(REPORTS/("run-"+state["run_id"]+"-"+state["run_attempt"])/name)
        for name in ("actual-result.md","execution.json")}
    env=os.environ.copy();token=env.pop("GITHUB_TOKEN")
    env.update(GIT_TERMINAL_PROMPT="0",GIT_CONFIG_COUNT="1",
        GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
        GIT_CONFIG_VALUE_0="AUTHORIZATION: basic "+base64.b64encode(("x-access-token:"+token).encode()).decode())
    def git(*args,check=True,stdout=None):
        r=subprocess.run(gb+list(args),cwd=root,env=env,text=stdout is None,
            stdout=subprocess.PIPE if stdout is None else stdout,stderr=subprocess.PIPE,timeout=900)
        if check and r.returncode:
            e=r.stderr if isinstance(r.stderr,str) else r.stderr.decode("utf-8","replace")
            raise RuntimeError("public Git "+str(args[0])+" failed: "+e[:1200])
        return r
    def sync():
        before=git("rev-parse","HEAD").stdout.strip();git("pull","--rebase","origin","main")
        after=git("rev-parse","origin/main").stdout.strip()
        diff=git("diff",before,after,"--",*rules["readme_sha256"]).stdout
        state["readme_checks"].append(dict(time=utc(),before=before,after=after,actual_diff=diff,
            explicitly_reviewed_commit=rules["read_commit"]))
        published,blob_map=topic_tree_metadata(git,TOPIC,PUBLIC)
        capacity=owned_head_delta(git,root,published,blob_map,owned_small_paths)
        state["current_published_topic_capacity_metadata"]=published
        state["current_topic_capacity_metadata"]=capacity
        state["current_topic_blob_bytes"]=capacity["blob_bytes"]
        state["current_topic_blob_count"]=capacity["blob_count"]
        state["current_topic_metadata_commit"]=capacity["commit"]
        state["current_topic_below_200000000_bytes"]=capacity["blob_bytes"]<200000000
        save(out/"worker-process.json",state)
        if not state["current_topic_below_200000000_bytes"]:
            raise ValueError("actual topic Git blobs reach the200000000-byte hard limit")
        for path,digest in rules["readme_sha256"].items():
            if sha(root/path)!=digest:
                print(diff,flush=True);raise RuntimeError("read and apply the newly changed README diff")
        if sha(a.rules)!=a.rules_sha or sha(a.manifest)!=a.manifest_sha or sha(root/PIPELINE)!=a.pipeline_sha:
            raise ValueError("the separately pinned execution contract changed during pull")
        if sha(root/rw)!=ws:raise ValueError("the running wrapper changed during pull")
    git("config","user.name","github-actions[bot]")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com");sync()
    for old in sorted((root/REPORTS).glob("*/execution.json")):
        v=read(old)
        if v.get("complete") is True and v.get("input_manifest_sha256")==a.manifest_sha and v.get("source_budget_source_sha256")==a.pipeline_sha:
            if v.get("actual_returncode")!=0 or not scientific_complete(v.get("actual_scientific_receipt"),a.pipeline_sha,a.manifest_sha):
                raise ValueError("an existing same-identity successful conclusion has inconsistent complete receipts")
            print(json.dumps(dict(reused_existing_complete_conclusion=str(old.relative_to(root)),
                original_run_id=v["run_id"],new_source_budget_processes=0,new_numerical_enclosures=0)),flush=True);return
        if (v.get("input_manifest_sha256")==a.manifest_sha
            and v.get("source_budget_source_sha256")==a.pipeline_sha
            and v.get("actual_source_budget_processes",0)>0
            and v.get("actual_returncode") not in (None,0)
            and v.get("actual_scientific_receipt",{}).get("failure") is not None):
            raise RuntimeError("an unchanged mathematical failure is already recorded at "+str(old.relative_to(root)))
    hist=m["historical_input_commit"]
    if len(hist)!=40 or any(c not in "0123456789abcdef" for c in hist):raise ValueError("the input commit is not immutable")
    git("fetch","--filter=blob:none","--no-tags","origin",hist)
    state["historical_input_commit"]=hist;state["input_receipts"]=[]
    if m.get("legacy_artifact_inputs",[]):raise ValueError("only the explicitly pinned three original body archives are allowed")
    body_history=m["original_body_historical_input_commit"]
    if body_history!=hist:git("fetch","--filter=blob:none","--no-tags","origin",body_history)
    last_sync=time.monotonic()
    actual_inputs=[]
    must_be_current={str(PIPELINE)}|{m["input_paths"][k] for k in m["current_text_input_roles"]}
    for e in m["files"]:
        rel=relpath(e["path"]);dst=work/rel;dst.parent.mkdir(parents=True,exist_ok=True)
        if str(rel) in must_be_current:
            checked(root/rel,e["bytes"],e["sha256"]);shutil.copyfile(root/rel,dst)
            origin=dict(kind="exact_current_text_input")
        elif ((root/rel).is_file() and (root/rel).stat().st_size==e["bytes"]
            and sha(root/rel)==e["sha256"]):
            shutil.copyfile(root/rel,dst)
            origin=dict(kind="exact_current_identical_legacy_input")
        else:
            with dst.open("wb") as stream:git("show",hist+":"+str(rel),stdout=stream)
            origin=dict(kind="exact_public_historical_blob",commit=hist)
        checked(dst,e["bytes"],e["sha256"])
        actual_inputs.append(dict(path=str(rel),bytes=e["bytes"],sha256=e["sha256"],origin=origin))
        if time.monotonic()-last_sync>540:
            sync();last_sync=time.monotonic()
    def restore_checkpoint():
        nonlocal last_sync
        if time.monotonic()-last_sync>540:
            sync();last_sync=time.monotonic()
    restored_parts=restore_original_body_prefix(m,work,root,git,token,state,restore_checkpoint)
    state["actual_separate_original_natural_part_count"]=len(restored_parts)
    # Preserve the exact complete input digest without copying reproducible numerical data.
    state.pop("input_receipts",None)
    state["actual_verified_input_count"]=len(actual_inputs)
    state["actual_verified_input_receipts_sha256"]=hashlib.sha256(
        json.dumps(actual_inputs,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
    origins={}
    for entry in actual_inputs:
        key=entry["origin"]["kind"];origins[key]=origins.get(key,0)+1
    state["actual_input_origins"]=origins
    critical=must_be_current|{str(rm),str(rr)}
    state["actual_current_contract_receipts"]=[
        entry for entry in actual_inputs if entry["path"] in critical]
    tm=work/rm;tm.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.manifest,tm)
    checked(tm,a.manifest.stat().st_size,a.manifest_sha)
    tr=work/rr;tr.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.rules,tr)
    checked(tr,a.rules.stat().st_size,a.rules_sha)
    state["actual_current_contract_receipts"].extend([
        dict(path=str(rm),bytes=tm.stat().st_size,sha256=a.manifest_sha,
            origin=dict(kind="exact_current_separately_pinned_manifest")),
        dict(path=str(rr),bytes=tr.stat().st_size,sha256=a.rules_sha,
            origin=dict(kind="exact_current_separately_pinned_rules"))])
    checked(work/PIPELINE,next(e["bytes"] for e in m["files"] if e["path"]==str(PIPELINE)),a.pipeline_sha)
    parsed=[]
    for entry in m["files"]:
        if entry["path"].endswith(".py"):
            path=work/relpath(entry["path"])
            ast.parse(path.read_text(),filename=str(path))
            parsed.append(dict(path=entry["path"],sha256=entry["sha256"]))
    state["complete_immutable_Python_AST_closure_passed"]=True
    state["complete_immutable_Python_AST_file_count"]=len(parsed)
    state["complete_immutable_Python_AST_inventory_sha256"]=hashlib.sha256(
        json.dumps(parsed,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
    if state["current_topic_blob_bytes"]+120000>200000000:
        print(json.dumps(dict(kind="insufficient_small_conclusion_capacity",
            actual_source_budget_processes=0,capacity=state["current_topic_capacity_metadata"],
            reserved_small_conclusion_bytes=120000),ensure_ascii=False),flush=True)
        raise ValueError("the actual topic has insufficient space for two bounded small conclusions")
    cmd=[sys.executable,"-u",str(work/PIPELINE),"--repo",str(work),"--manifest",str(tm),
        "--manifest-sha",a.manifest_sha,"--out-dir",str(out/"consumers")]
    state["command"]=cmd;state["actual_scientific_checkout_commit"]=git("rev-parse","HEAD").stdout.strip()
    state["actual_source_budget_processes"]=1;save(out/"worker-process.json",state)
    ce=os.environ.copy();ce.pop("GITHUB_TOKEN",None);ce["VISIBLE_PHASE_SCIENCE_COMMIT"]=state["actual_scientific_checkout_commit"]
    started=time.monotonic()
    with (out/"source-budget.stdout.log").open("wb") as log:
        child=subprocess.Popen(cmd,cwd=work,env=ce,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        try:
            while child.poll() is None:
                remaining=900-(time.monotonic()-started)
                if remaining<=0:
                    state["timeout_seconds"]=900
                    break
                if time.monotonic()-last_sync>540:
                    sync();last_sync=time.monotonic()
                try:child.wait(timeout=min(60,remaining))
                except subprocess.TimeoutExpired:pass
        finally:
            if child.poll() is None:
                os.killpg(child.pid,signal.SIGTERM)
                try:child.wait(timeout=10)
                except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
            state["actual_returncode"]=child.returncode
    state["source_budget_child_wall_seconds"]=time.monotonic()-started
    c=out/"consumers";proc=read(c/"process.json") if (c/"process.json").is_file() else None
    state["complete"]=bool(child.returncode==0 and scientific_complete(proc,a.pipeline_sha,a.manifest_sha))
    state["new_complete_primitive_mean_strict_propagation_proved"]=state["complete"]
    state["actual_failure"]=(dict(type="MissingScientificProcessReport",
        message="the actual child did not produce its small process.json") if proc is None else proc.get("failure"))
    if proc and proc.get("formatting_failure") is not None:
        state["formatting_failure"]=proc["formatting_failure"]
        state["actual_scientific_returncode"]=proc.get("actual_scientific_returncode")
    selected_outputs=[c/"conclusion.md",c/"process.json",
        c/"temporary-complete-primitive-mean-strict-propagation.json.gz",out/"source-budget.stdout.log"]
    state["output_hashes"]=[rec(path,out) for path in selected_outputs if path.is_file()]
    if proc is not None:
        state["actual_scientific_receipt"]={k:proc.get(k) for k in (
            "kind",
            "complete",
            "proved",
            "actual_returncode",
            "failure",
            "gates",
            "actual_mathematical_wall_seconds",
            "source_sha256",
            "input_manifest_sha256",
            "runtime",
            "arithmetic_bits",
            "public_repository",
            "run_id",
            "run_attempt",
            "workflow_event_commit",
            "actual_scientific_checkout_commit",
            "mathematical_parameters",
            "accepted_small_input_conclusions",
            "original_complete_strict_rows_verified",
            "original_strict_container_parts_read",
            "original_strict_native_bytes",
            "original_strict_native_sha256",
            "original_strict_part_receipts",
            "original_complete_body_prefix_rows_verified",
            "original_complete_body_prefix_parts_read",
            "original_body_prefix_actual_interval",
            "original_body_prefix_part_receipts",
            "exact_family_identity",
            "new_common_intersection_count",
            "new_common_cover_sha256",
            "new_positive_two_state_exponentials",
            "new_forward_and_reverse_ordered_products",
            "new_common_comparison_rows",
            "new_compact_metric_intersections",
            "new_compact_log_variation_integrals",
            "positive_exponential_max_scaling_squarings",
            "positive_exponential_series_degree",
            "complete_strict_propagation_conclusion",
            "complete_endpoint_readout_conclusion",
            "scope",
            "old_numerical_enclosures_recomputed",
            "old_target_FFT_intrinsic_or_repair_recomputed",
            "old_strict_H1_flow_recomputed_or_reused",
            "old_grouped_curvature_integral_recomputed",
            "old_root_Cauchy_normalizer_or_source_enclosures_recomputed",
            "old_original_source_rows_or_radial_source_integrals_recomputed",
            "original_natural_part_bytes_modified",
            "full_high_inverse_claimed",
            "full_return_remainder_claimed",
            "temporary_native_sha256",
            "temporary_native_bytes",
            "temporary_native_is_not_published",
            "reproducible_outputs_published_to_repository",
            "reproducible_outputs_uploaded_to_Releases",
            "new_reproducible_data_artifact_uploaded")}
    save(out/"worker-process.json",state)
    # Print the full small conclusion plus exact gates and identities before any publication operation.
    state["recoverable_prepublication_stdout"]=emit_recoverable_conclusion(state,c)
    save(out/"worker-process.json",state)
    # One bounded15-minute child with periodic checked pulls; print its conclusion before the final pull.
    sync();report=root/REPORTS/("run-"+state["run_id"]+"-"+state["run_attempt"]);report.mkdir(parents=True,exist_ok=True)
    def conclusion():
        actual=c/"conclusion.md"
        if actual.is_file():
            return actual.read_text()
        return "\n".join(["# Complete primitive-and-mean strict propagation: actual incomplete run","",
            "- Public repository: "+PUBLIC,
            "- Actual run: "+state["run_id"]+"/"+state["run_attempt"],
            "- Script: "+str(PIPELINE),"- Script SHA256: "+a.pipeline_sha,
            "- Manifest: "+str(rm),"- Manifest SHA256: "+a.manifest_sha,
            "- Original input commit: "+hist,
            "- Actual child return code: "+str(state["actual_returncode"]),
            "- Actual failure: "+json.dumps(state["actual_failure"],ensure_ascii=False),
            "- Old numerical enclosures recomputed: 0.",
            "No new complete primitive-and-mean strict propagation source improvement is asserted. No new data, Release, or artifact is persisted.",""])
    def snapshot():
        text=conclusion()
        names=[str((report/name).relative_to(root)) for name in ("actual-result.md","execution.json")]
        capacity,blob_map=topic_tree_metadata(git,TOPIC,PUBLIC)
        state["publication_owned_HEAD_delta"]=owned_head_delta(git,root,capacity,blob_map,owned_small_paths)
        total=capacity["blob_bytes"]
        oldbytes=sum(blob_map[name]["bytes"] for name in names if name in blob_map)
        state["publication_capacity_metadata"]=capacity
        state["publication_base_topic_blob_bytes"]=total
        state["publication_capacity_metadata_commit"]=capacity["commit"]
        state["projected_topic_blob_bytes"]=0
        while True:
            raw=(json.dumps(state,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            projected=total-oldbytes+len(text.encode())+len(raw)
            if projected==state["projected_topic_blob_bytes"]:break
            state["projected_topic_blob_bytes"]=projected
        if projected>=200000000:raise ValueError("the two small conclusions exceed the actual topic capacity")
        if len(text.encode())>60000 or len(raw)>60000:raise ValueError("small conclusion or provenance exceeds its size limit")
        (report/"actual-result.md").write_text(text);(report/"execution.json").write_bytes(raw)
        # Never copy any native, stage, numerical array or original case into Git.
    snapshot();owned=str(report.relative_to(root));git("add","--sparse","--",owned)
    git("commit","-m","visible-exact: record complete primitive-and-mean strict propagation")
    while True:
        r=git("push","origin","HEAD:refs/heads/main",check=False)
        if r.returncode==0:break
        if not any(v in r.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
            raise RuntimeError("conclusion push failed outside concurrent-main rebase")
        sync();snapshot();git("add","--sparse","--",owned);git("commit","--amend","--no-edit")
    print(json.dumps(dict(complete=state["complete"],actual_returncode=state["actual_returncode"],
        report=owned,old_numerical_enclosures_recomputed=0,new_source_budget_processes=1,
        reproducible_output_files_persisted=0,output_hash_count=len(state["output_hashes"]),
        original_inputs_unchanged=True),ensure_ascii=False),flush=True)
    if not state["complete"]:raise SystemExit(1)
if __name__=="__main__":main()
