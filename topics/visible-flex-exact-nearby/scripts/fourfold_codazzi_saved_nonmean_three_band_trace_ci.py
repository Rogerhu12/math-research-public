#!/usr/bin/env python3
"""Restrict saved nonmean norms; publish only complete small trace coefficients."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import re,gzip,zipfile,urllib.error,urllib.parse,urllib.request
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_saved_nonmean_three_band_trace.py"
REPORTS=TOPIC/"notes/saved_nonmean_three_band_trace_ci"
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
        or str(metadata.get("workflow_run",{}).get("id"))!=str(entry["run_id"])):
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

def restore_original_parts(m,work,root,git,token,state,checkpoint):
    old=read(work/m["input_paths"]["original_manifest"])
    accepted=read(work/m["input_paths"]["response_summary"])
    expected={tuple(item["indices"]):item["sha256"] for item in accepted["original_parts"]}
    if len(expected)!=40:raise ValueError("the exact original forty-part table changed")
    directory=work/"original-natural-row-parts";directory.mkdir()
    paths={};receipts=[];archives=[]
    for entry in m["historical_natural_parts"]:
        key=tuple(entry["indices"]);rel=relpath(entry["path"])
        if old["already_complete_original_parts"].count(entry)!=1 or expected.get(key)!=entry["sha256"]:
            raise ValueError("a separately restored original natural part changed its manifest identity")
        dst=directory/("original-"+str(key[0])+"-"+str(key[1])+".json.gz")
        if (root/rel).is_file() and sha(root/rel)==entry["sha256"]:
            shutil.copyfile(root/rel,dst);origin=dict(kind="exact_current_original_natural_part")
        else:
            with dst.open("wb") as stream:git("show",m["historical_input_commit"]+":"+str(rel),stdout=stream)
            origin=dict(kind="exact_public_historical_natural_part",commit=m["historical_input_commit"])
        if sha(dst)!=entry["sha256"]:raise ValueError("an original natural part changed its exact bytes")
        paths[key]=dst;receipts.append(dict(indices=list(key),path=str(rel),bytes=dst.stat().st_size,
            sha256=entry["sha256"],origin=origin))
    if len(paths)!=6:raise ValueError("the original six independent parts were not restored exactly")
    requested={tuple(pair) for pair in old["consumer_ranges"]};observed=set()
    for index,entry in enumerate(m["original_row_archives"]):
        pair=tuple(entry["requested_rows"])
        if pair not in requested or pair in observed:raise ValueError("the eight old worker ranges differ")
        observed.add(pair)
        archive=work/"original-archives"/(str(entry["id"])+".zip")
        ar=download_original_archive(entry,archive,token)
        with zipfile.ZipFile(archive) as z:
            members=z.namelist()
            if any(Path(name).is_absolute() or ".." in Path(name).parts for name in members):
                raise ValueError("an old archive member leaves its original relative tree")
            process_names=[name for name in members if name=="process.json"]
            if len(process_names)!=1:raise ValueError("the original row archive has no unique actual process")
            raw=z.read(process_names[0]);proc=json.loads(raw)
            if (proc.get("repository")!=PUBLIC or str(proc.get("run_id"))!=str(entry["run_id"])
                or str(proc.get("run_attempt"))!=str(entry["run_attempt"])
                or proc.get("input_manifest_sha256")!=m["original_body_manifest_sha256"]
                or proc.get("complete") is not True or proc.get("failure")
                or tuple(proc.get("requested_rows",[]))!=pair
                or any(child.get("actual_returncode")!=0 for child in proc.get("children",[]))):
                raise ValueError("an original row archive does not contain its actual successful process")
            required={tuple(v) for v in old["atomic_ranges"][str(pair[0])+"-"+str(pair[1])]}
            got=set()
            for name in members:
                if not name.startswith("native/") or not name.endswith(".json.gz"):continue
                payload=z.read(name);source=json.loads(gzip.decompress(payload))
                key=tuple(source.get("selected_indices",[]))
                digest=hashlib.sha256(payload).hexdigest()
                if (key not in required or key in got or key in paths or expected.get(key)!=digest
                    or source.get("kind")!=old["residual_kind"]
                    or source.get("identity")!=old["row_identity"]
                    or source.get("selected_cells_complete") is not True or source.get("failure") is not None):
                    raise ValueError("an original natural row payload differs from its accepted complete receipt")
                dst=directory/("original-"+str(key[0])+"-"+str(key[1])+".json.gz")
                dst.write_bytes(payload);paths[key]=dst;got.add(key)
                receipts.append(dict(indices=list(key),bytes=len(payload),sha256=digest,
                    origin=dict(kind="exact_original_Actions_native",artifact_id=entry["id"],member=name)))
            if got!=required:raise ValueError("the original archive has an incomplete natural part cover")
            ar.update(original_process_bytes=len(raw),original_process_sha256=hashlib.sha256(raw).hexdigest(),
                      actual_returncodes=[c.get("actual_returncode") for c in proc.get("children",[])],
                      requested_rows=list(pair),complete_natural_parts=len(got))
        archives.append(ar)
        state.update(actual_original_row_archive_receipts=archives,
            actual_original_natural_parts_restored=len(paths),
            original_parts_recomputed=0,original_part_bytes_modified=0)
        checkpoint()
    if observed!=requested or set(paths)!=set(expected) or len(paths)!=40:
        raise ValueError("the restored complete old part cover is not exactly the original forty parts")
    state["actual_original_part_receipts_sha256"]=hashlib.sha256(compact(sorted(receipts,key=lambda e:e["indices"]))).hexdigest()
    state["actual_original_part_count"]=40
    return [paths[key] for key in sorted(paths)]

def scientific_receipt_valid(proc,source,manifest):
    return (isinstance(proc,dict) and proc.get("kind")=="actual_saved_nonmean_restriction_and_three_band_trace_coefficients_v1"
        and proc.get("complete") is True and proc.get("proved") is True
        and proc.get("failure") is None and proc.get("actual_returncode")==0
        and proc.get("source_sha256")==source and proc.get("input_manifest_sha256")==manifest
        and len(proc.get("gates",[]))==13 and all(g.get("passed") is True for g in proc["gates"])
        and proc.get("complete_original_rows_verified")==7721
        and len(proc.get("original_part_receipts",[]))==40
        and proc.get("complete_source_and_trace_coefficient_tables_proved") is True
        and proc.get("cases_evaluated")==5
        and len(proc.get("complete_retained_three_band_cases",{}))==5
        and len(proc.get("complete_new_nonmean_windows",{}))==2
        and len(proc.get("corrected_raw_mean_windows_copied_without_recomputation",{}))==2
        and proc.get("corrected_raw_mean_execution_sha256")=="c5424be21b98cf5e195ea7246ccba46cf746d1f16d9c118042fda1fad433e408"
        and proc.get("successful_raw_mean_restrictions_recomputed") is False
        and proc.get("original_91_cases_or_five_corrected_verdicts_changed") is False
        and proc.get("old_numerical_enclosures_recomputed")==0
        and proc.get("old_target_Fourier_cubic_mean_residual_integral_or_Green_calls")==0
        and proc.get("complete_finite193_transferred_inverse_proved") is False
        and proc.get("complete_infinite_BVP_inverse_proved") is False
        and proc.get("true_parameter_Schur_proved") is False
        and proc.get("actual_core_solution_proved") is False
        and proc.get("actual_low_curvature_entry_proved") is False
        and proc.get("all_original_natural_part_bytes_modified")==0)

def render(state):
    result=state.get("actual_scientific_receipt") or {}
    text=["# Actual saved-nonmean restrictions and three-band trace coefficients","",
        "Public run: "+str(state.get("run_id"))+"/"+str(state.get("run_attempt"))+".",
        "Actual scientific child code: "+str(state.get("actual_returncode"))+".",
        "Complete new scalar accounting: "+str(result.get("complete",False))+".","",
        "Scientific SHA256: "+str(state.get("source_budget_source_sha256"))+".",
        "Manifest SHA256: "+str(state.get("input_manifest_sha256"))+".","",
        "This run reads the original raw nonmean norm fields. It does not solve for an unknown state.",
        "The old complete integral and the uniform norm give two separate restriction bounds.",
        "The successful raw-mean restriction and corrected high-case authorizations are copied unchanged.","",
        "## Complete new nonmean source windows",""]
    for name,row in result.get("complete_new_nonmean_windows",{}).items():
        text += ["### "+name,"","Exact interval: "+str(row.get("exact_interval"))+".",
            "True radial measure: "+str(row.get("exact_radial_measure"))+".",
            "Original closed rows: "+str(row.get("original_closed_rows_consumed"))+".","",
            "| Complete new scalar | Directed bound |","|---|---|"]
        for key in ("raw_nonmean_L2","P_scaled_raw_nonmean_L2","raw_nonmean_H1",
                    "P_scaled_raw_nonmean_H1","P_scaled_raw_nonmean_angular_L2_upper",
                    "complete_scaled_square_integral","complete_scaled_H1_square_integral"):
            text.append("| "+key+" | "+cell(ball(row.get(key)))+" |")
        text += ["","The minimum uses true length times uniform squared and the whole old integral squared.",
            "It never shrinks the old whole integral by the intersection fraction.",""]
    text += ["## All five explicit coefficient tables","",
        "| Raw C0 radius | Complete known H96 source | Known middle H1 additive upper | Signed remaining sufficient radius |",
        "|---|---|---|---|"]
    for radius,row in result.get("complete_retained_three_band_cases",{}).items():
        src=row["source_restriction"];c=row["complete_trace_coefficients"]
        text.append("| "+radius+" | "+cell(ball(src["complete_known_F96_upper"]))+" | "+
            cell(ball(c["known_middle_source_additive_upper"]))+" | "+
            cell(ball(c["residual_budget_after_known_middle_term"]))+" |")
    text += ["","The signed last column is a source budget, not a proved actual-state gate.",
        "No unknown cut or body norm has been set to zero.",
        "All E96/E288 coefficients, source derivatives, repair fees, original case hashes and high authorizations are in execution.json.","",
        "## Actual identity and source gates",""]
    for g in result.get("gates",[]):
        text.append("- "+str(g.get("name"))+": "+str(g.get("passed"))+".")
    text += ["","## Mathematical scope","",
        "- The complete known reference residual has degree at most 288; its high-above-288 source is exactly zero.",
        "- The independent mean remains paid in the full equation by the successful corrected execution.",
        "- The finite cut is in original moving units, with its complete even mean.",
        "- Same-state left and right low/high body norms remain actual required inputs.",
        "- The old Green covers only the inner side up to the true cut; the right cap half is not relabelled as that output.",
        "- Approximate-state ordinary residuals and the mean-speed source remain explicit.",
        "- No core solution, high inverse, parameter Schur or low curvature entry is claimed.",
        "- Old target, Fourier, cubic residual, mean flow and Green routines are not rerun.",
        "- New row audits are temporary and only their hashes persist.","",
        "Actual failure: "+json.dumps(state.get("actual_failure"),ensure_ascii=False)+".",
        "New scalar seconds: "+str(result.get("seconds"))+".",""]
    return "\n".join(text)

def public_execution(state):
    """Keep all science and README pulls; replace repeated infrastructure tables by exact audit identities."""
    result=dict(state)
    for key in ("actual_current_contract_receipts","actual_original_row_archive_receipts"):
        if key in result:
            table=result.pop(key)
            result[key+"_audit"]=dict(count=len(table),sha256=hashlib.sha256(compact(table)).hexdigest(),
                complete_table_checked=True,complete_original_table_pinned_by_manifest=True,
                input_manifest_sha256=state["input_manifest_sha256"])
    for key in ("current_published_topic_capacity_metadata","publication_capacity_metadata"):
        if key in result:
            original=result[key]
            result[key]={name:original[name] for name in
                ("method","commit","root_tree","topic","topic_tree","truncated","all_blob_sizes_checked",
                 "blob_count","blob_bytes","nested_tree_count","gitlink_count",
                 "complete_blob_metadata_inventory_sha256","blob_bodies_requested") if name in original}
            responses=original.get("metadata_responses",[])
            result[key].update(complete_capacity_receipt_sha256=hashlib.sha256(compact(original)).hexdigest(),
                complete_metadata_response_count=len(responses),
                complete_metadata_responses_sha256=hashlib.sha256(compact(responses)).hexdigest())
    return result

def emit_recoverable_conclusion(state):
    exported=public_execution(state)
    identity_keys=("repository","run_id","run_attempt","workflow_commit","actual_scientific_checkout_commit",
        "worker_source_sha256","source_budget_source_sha256","input_manifest_sha256",
        "reviewed_rules_sha256","historical_input_commit","actual_returncode","complete","actual_failure",
        "actual_source_budget_processes","actual_verified_input_count","actual_verified_input_receipts_sha256",
        "actual_original_part_count","actual_original_part_receipts_sha256",
        "actual_current_contract_receipts_audit","actual_original_row_archive_receipts_audit",
        "readme_checks","current_topic_blob_bytes","current_topic_blob_count","current_topic_metadata_commit",
        "complete_immutable_Python_AST_closure_passed","complete_immutable_Python_AST_inventory_sha256",
        "actual_scientific_receipt","output_hashes")
    evidence={name:exported[name] for name in identity_keys if name in exported}
    payload=dict(marker="SAVED_NONMEAN_THREE_BAND_TRACE_PREPUBLICATION_V2",
                 execution=evidence,report_text=render(state))
    raw=compact(payload)
    science=state.get("actual_scientific_receipt")
    native=compact(science) if science is not None else None
    gates=science.get("gates",[]) if isinstance(science,dict) else []
    failure=state.get("actual_failure")
    short_failure=None if failure is None else dict(
        type=str(failure.get("type",""))[:80],message=str(failure.get("message",""))[:160],
        complete_failure_sha256=hashlib.sha256(compact(failure)).hexdigest())
    status=dict(marker="SAVED_NONMEAN_THREE_BAND_TRACE_PREPUBLICATION_STATUS_V2",
        actual_returncode=state.get("actual_returncode"),complete=state.get("complete"),
        gates_passed=sum(g.get("passed") is True for g in gates),gates_total=len(gates),
        complete_science_bytes=None if native is None else len(native),
        complete_science_sha256=None if native is None else hashlib.sha256(native).hexdigest(),
        complete_payload_bytes=len(raw),complete_payload_sha256=hashlib.sha256(raw).hexdigest(),
        actual_failure=short_failure)
    status_raw=compact(status)
    if len(status_raw)>1000:raise ValueError("the prepublication status unexpectedly exceeds 1000 bytes")
    print(status_raw.decode("utf-8"),end="",flush=True)
    if len(raw)>59000:raise ValueError("the complete small prepublication evidence exceeds 59000 bytes: "+str(len(raw)))
    print(raw.decode("utf-8"),end="",flush=True)
    return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),encoding="UTF-8",
                complete_scientific_receipt_preserved=True,complete_report_preserved=True,
                infrastructure_tables_replaced_only_by_complete_audit_hashes=True,
                published_before_any_git_publication=True)

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
        or m.get("kind")!="immutable_saved_nonmean_three_band_trace_inputs_v1"
        or m.get("expected_actual_gate_count")!=13
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
        subprocess.run(gb+["sparse-checkout","set","--no-cone","--stdin"],cwd=root,
            input="\n".join("/"+v for v in sorted(paths))+"\n",text=True,check=True)
        print("Hydrated only current scripts, contracts, original small conclusions and review records.",flush=True)
        return
    if a.work is None or a.out_dir is None:raise ValueError("temporary work and outcome directories are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():raise FileExistsError("preserve an existing actual run")
    if any(v.is_relative_to(root) for v in (work,out)):raise ValueError("recomputable inputs must stay outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__);hist=m["historical_input_commit"]
    state=dict(kind="actual_public_saved_nonmean_three_band_trace_execution_v1",repository=PUBLIC,
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
        for path,digest in rules["readme_sha256"].items():
            if sha(root/path)!=digest:
                print(diff,flush=True);raise RuntimeError("read and apply the newly changed README diff")
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
        parts=restore_original_parts(m,work,root,git,token,state,checkpoint)
        cmd=[sys.executable,"-u",str(work/PIPELINE),"--manifest",str(tm),
            "--manifest-sha",a.manifest_sha,"--original-manifest",str(work/m["input_paths"]["original_manifest"]),
            "--response-summary",str(work/m["input_paths"]["response_summary"]),
            "--intrinsic-execution",str(work/m["input_paths"]["intrinsic_execution"]),
            "--collar-conclusion",str(work/m["input_paths"]["collar_conclusion"]),
            "--collar-process",str(work/m["input_paths"]["collar_process"]),
            "--corrected-mean-execution",str(work/m["input_paths"]["corrected_mean_execution"]),
            "--temporary-rows",str(out/"temporary-new-scalar-rows.jsonl"),
            "--out",str(out/"actual-scalar-conclusion.json"),"--bits","320",
            "--parts",*[str(path) for path in parts]]
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
        state["complete"]=bool(child.returncode==0 and scientific_receipt_valid(proc,a.pipeline_sha,a.manifest_sha))
        state["actual_failure"]=None if state["complete"] else (
            proc.get("failure") if proc and proc.get("failure") else
            dict(type="IncompleteScientificReceipt",message="the complete thirteen-gate scalar receipt did not validate"))
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
    outputs=[out/name for name in ("actual-scalar-conclusion.json","temporary-new-scalar-rows.jsonl",
                                   "source-budget.stdout.log")]
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
            raw=compact(public_execution(state));projected=total-oldbytes+len(text.encode())+len(raw)
            if projected==state["projected_topic_blob_bytes"]:break
            state["projected_topic_blob_bytes"]=projected
        if projected>=200000000:raise ValueError("the complete small conclusions exceed topic capacity")
        if len(raw)>60000 or len(text.encode())>60000:
            raise ValueError("the complete small scientific evidence exceeds the publication size limit")
        (report/"actual-result.md").write_text(text);(report/"execution.json").write_bytes(raw)
    snapshot();owned=str(report.relative_to(root));git("add","--sparse","--",owned)
    git("commit","-m","visible-exact: record saved nonmean restrictions and three-band trace coefficients")
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
