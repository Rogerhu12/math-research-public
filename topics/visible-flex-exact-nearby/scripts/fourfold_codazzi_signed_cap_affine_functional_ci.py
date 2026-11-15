#!/usr/bin/env python3
"""Public exact-input restoration and new SC signed functional, with no new artifact export."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import re,gzip,zipfile,urllib.error,urllib.parse,urllib.request,select,importlib.metadata
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_signed_cap_affine_functional.py"
REPORTS=TOPIC/"notes/signed_cap_affine_functional_ci"
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


def scientific_receipt_valid(proc,source,manifest,parameters,pins,runtime,helper,reader):
    """A wrapper-only change never repeats an already complete same science."""
    return (isinstance(proc,dict)
        and proc.get("kind")=="actual_complete97_signed_radial_subtracted_cap_affine_v1"
        and proc.get("complete") is True and proc.get("failure") is None
        and proc.get("actual_returncode")==0 and proc.get("source_sha256")==source
        and (manifest is None or proc.get("input_manifest_sha256")==manifest)
        and proc.get("parameters")==parameters and proc.get("actual_runtime")==runtime
        and proc.get("helper_sha256")==helper and proc.get("reader_sha256")==reader
        and proc.get("scientific_identity",{}).get("helper_sha256")==helper
        and proc.get("scientific_identity",{}).get("reader_sha256")==reader
        and proc.get("scientific_identity",{}).get("actual_runtime")==runtime
        and proc.get("scientific_identity",{}).get("input_sha256")==pins
        and proc.get("actual_new_signed_functional_complete") is True
        and len(proc.get("gates",[]))==20 and all(g.get("passed") is True for g in proc["gates"])
        and proc.get("complete_body_cover",{}).get("groups")==32
        and proc["complete_body_cover"].get("quarters")==7908
        and len(proc.get("complete_signed97_parameter_model",{}).get(
            "coefficients_in_increasing_delta_power",[]))==3
        and all(len(row)==97 for row in proc["complete_signed97_parameter_model"][
            "coefficients_in_increasing_delta_power"])
        and len(proc.get("complete_posterior_rows",[]))==2
        and proc.get("full_original_mean_and_same97_input_space_retained") is True
        and all(proc.get(k) is False for k in (
            "new_low_trace_gate_claimed","new_core_selfmap_claimed",
            "new_full_BVP_inverse_claimed","new_global_surface_claimed"))
        and proc.get("new_artifact_count")==0 and proc.get("new_Release_count")==0)


def render(state,science):
    lines=["# Actual complete97 signed cap affine functional","",
        "The new scalar calculation uses the exact radial-reference subtraction and the same physical cap, original adjoint trial and complete means.","",
        "- Run: "+str(state["run_id"])+"/"+str(state["run_attempt"]),
        "- Scientific child return: "+str(state.get("actual_returncode")),
        "- Complete mathematical result: "+str(state.get("complete_mathematical_receipt_available",False)),
        "- Source SHA256: "+state["source_sha256"],
        "- Manifest SHA256: "+state["input_manifest_sha256"],
        "- Complete scientific file: [actual-scientific-conclusion.json](actual-scientific-conclusion.json).",
        "- Old QR, target, residual-norm, Gram, RW and Green calculations repeated: 0.",
        "- New array artifact / Release uploads: 0 / 0.",""]
    if science:
        model=science.get("complete_signed97_parameter_model",{})
        cover=science.get("complete_body_cover",{})
        lines+=["## Exact object and complete known output","",
            "- Complete original groups / quarters: "+str(cover.get("groups"))+" / "+str(cover.get("quarters")),
            "- True cap interval: 9/10 to 25/8; radial measure is dr.",
            "- Every original scalar row must retain one candidate piece and its same saved midpoint.",
            "- All 128 physical nonmean modes and the independent even mean are retained.",
            "- All 97 input columns are retained in each of the three signed parameter-coefficient arrays.",
            "- Actual selected parameter interval: [-1e-10,1e-10].",
            "- Complete third parameter remainder: "+ball(model.get("complete_third_remainder_norm")),
            "- All input, exponential, radial and arithmetic errors are enclosed in the stored balls.",""]
        if model.get("coefficients_in_increasing_delta_power"):
            lines+=["| Complete scalar-mean input | Signed coefficient |","|---|---:|"]
            for k,row in enumerate(model["coefficients_in_increasing_delta_power"]):
                lines.append("| delta power "+str(k)+" | "+cell(row[96])+" |")
        accounting=science.get("complete_error_accounting",{})
        lines+=["","## Complete actual error accounting","",
            "- Uniform norm of the complete known parameter model: "+ball(accounting.get("uniform_known_parameter_model_norm")),
            "- Repaired A15 outer affine omission: "+ball(accounting.get("complete_outer_omission_norm")),
            "- Selected true left-defect norm: "+ball(accounting.get("selected_left_defect_norm")),
            "- Full selected known left shift: "+ball(accounting.get("complete_selected_known_left_shift")),
            "",
            "Body HS data already are norms; the original endpoint Gram traces are square-rooted once. The formal residual is used without a second Hessian fee.",""]
        for row in science.get("complete_posterior_rows",[]):
            p=row["selected_complete_prior"]
            lines+=["### "+row["domain"],"",
                "- Physical input gamma upper for this complete prior: "+row["physical_gamma_A0_upper"],
                "- Whole prior selected: "+p["weight"],
                "- Complete formal and nonlinear body error: "+p["formal_and_nonlinear_body_error"],
                "- Complete left-defect error: "+p["complete_left_defect_error"],
                "- Complete outer-feedback error: "+p["complete_outer_feedback_error"],
                "- Complete affine97 norm upper: "+row["complete_affine_97_norm_upper"],""]
        lines+=["## Structural and mathematical completeness gates",""]
        lines += ["- "+("PASS" if g["passed"] else "FAIL")+": "+g["name"]
                  for g in science.get("gates",[])]
    if state.get("actual_failure"):
        lines+=["","## Actual failure","",json.dumps(state["actual_failure"],ensure_ascii=False,sort_keys=True)]
    if state.get("last_complete_scientific_prefix"):
        lines+=["","## Preserved partial scientific conclusion","",
            json.dumps(state["last_complete_scientific_prefix"],sort_keys=True),
            "Its complete cumulative97 enclosure is in the Actions stdout checkpoint. No unprocessed interval is asserted."]
    lines+=["","## Scope","",
        "The unknown correction remains actual cap minus the repaired centre. Radial subtraction does not reduce its prior bound. The two listed priors apply only when the actual inner physical input is the same selected trace required by SC7.",
        "The physical gamma domain, whole-core nonlinear domain, low and high cut data, chart regularity, waist and independent height rows remain separate. No new low-trace gate, core self-map, infinite inverse or closed surface is asserted.",
        "",
        "Every restored native is an original immutable input in temporary storage. New per-row arrays and audits stay temporary. Complete source/input identities, exact coverage, audit hashes and actual return codes are preserved.","",
        "## Actual README pulls",""]
    for r in state.get("readme_checks",[]):
        lines.append("- "+r["time"]+" -> "+r["after"]+"; README diff empty: "+str(r["actual_diff"]==""))
    return "\n".join(lines)+"\n"


def emit_prepublication(state,science):
    report=render(state,science)
    science_raw=compact(science) if science is not None else None
    payload=dict(marker="SC_COMPLETE_SCIENTIFIC_PREPUBLICATION_V1",
        source_sha256=state["source_sha256"],manifest_sha256=state["input_manifest_sha256"],
        run_id=state["run_id"],run_attempt=state["run_attempt"],
        actual_returncode=state.get("actual_returncode"),scientific_result=science,report_text=report)
    raw=compact(payload)
    status=dict(marker="SC_PREPUBLICATION_STATUS",actual_returncode=state.get("actual_returncode"),
        complete_mathematics=state.get("complete_mathematical_receipt_available",False),
        gates_passed=sum(g.get("passed") is True for g in (science or {}).get("gates",[])),
        gates_total=len((science or {}).get("gates",[])),
        science_bytes=None if science_raw is None else len(science_raw),
        science_sha256=None if science_raw is None else hashlib.sha256(science_raw).hexdigest(),
        payload_bytes=len(raw),payload_sha256=hashlib.sha256(raw).hexdigest(),
        packaging_failure=None if len(raw)<=59000 else "complete_prepublication_payload_over59000")
    print(json.dumps(status,ensure_ascii=False),flush=True)
    if len(raw)>59000:
        raise ValueError("the full SC science was saved and printed by its child; publication payload exceeds59000")
    print(raw.decode(),end="",flush=True)
    # No second copy of science is embedded in the complete process record.
    process=compact(dict(marker="SC_EXECUTION_PREPUBLICATION_V1",execution=state))
    if len(process)>59000:
        raise ValueError("the complete scientific result is preserved; execution metadata exceeds59000")
    print(process.decode(),end="",flush=True)
    return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
        process_bytes=len(process),process_sha256=hashlib.sha256(process).hexdigest(),
        complete_science_and_report_preserved=True,before_any_git_publication=True)


def safe_name(value):
    p=Path(value)
    if p.is_absolute() or not value or ".." in p.parts:
        raise ValueError("an original archive member has an unsafe path")
    return p


def exact_old_artifact(item,folder,token,checkpoint):
    """Download only one specifically pinned old archive, never create an artifact."""
    folder.mkdir(parents=True,exist_ok=True)
    archive=folder/"original.zip"
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self,request,fp,code,message,headers,newurl):
            return None
    api="https://api.github.com/repos/"+PUBLIC+"/actions/artifacts/"+str(item["artifact_id"])
    headers={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28",
             "Authorization":"Bearer "+token}
    opener=urllib.request.build_opener(NoRedirect())
    try:
        with opener.open(urllib.request.Request(api,headers=headers),timeout=60) as response:
            raw=response.read(200001)
        if len(raw)>200000:
            raise ValueError("one original artifact metadata response is unexpectedly large")
        meta=json.loads(raw)
        if (meta.get("id")!=item["artifact_id"] or meta.get("name")!=item["name"]
            or meta.get("expired") is not False or meta.get("size_in_bytes")!=item["bytes"]
            or str(meta.get("workflow_run",{}).get("id"))!=str(item["run_id"])
            or meta.get("digest")!="sha256:"+item["sha256"]):
            raise ValueError("an original artifact identity size digest or availability changed")
        url=api+"/zip"
        try:
            response=opener.open(urllib.request.Request(url,headers=headers),timeout=90)
            location=None
        except urllib.error.HTTPError as redirect:
            if redirect.code not in (301,302,303,307,308):
                raise
            location=redirect.headers.get("Location")
            response=None
        if location is not None:
            parsed=urllib.parse.urlparse(location)
            host=parsed.hostname or ""
            if (parsed.scheme!="https" or parsed.username or parsed.password
                or not (host.endswith(".blob.core.windows.net")
                    or host.endswith(".actions.githubusercontent.com")
                    or host.endswith(".githubusercontent.com")
                    or host.endswith(".s3.amazonaws.com")
                    or host.endswith(".s3.us-east-1.amazonaws.com"))):
                raise ValueError("the authenticated artifact endpoint gave an unexpected storage host")
            # The signed storage URL receives no GitHub Authorization header.
            response=opener.open(urllib.request.Request(location),timeout=90)
        total=0
        with response,archive.open("wb") as out:
            while True:
                chunk=response.read(1<<20)
                if not chunk:
                    break
                total+=len(chunk)
                if total>item["bytes"]:
                    raise ValueError("the old artifact exceeds its exact declared byte count")
                out.write(chunk);checkpoint()
        checked(archive,item["bytes"],item["sha256"])
    except urllib.error.HTTPError as error:
        raise RuntimeError("original artifact access returned HTTP "+str(error.code)) from None
    except urllib.error.URLError:
        raise RuntimeError("original artifact transport failed; no old mathematics will be reconstructed") from None
    return archive,dict(artifact_id=item["artifact_id"],run_id=str(item["run_id"]),
        bytes=item["bytes"],sha256=item["sha256"],metadata_bytes=len(raw),
        metadata_sha256=hashlib.sha256(raw).hexdigest(),original_artifact_only=True)


def extract_exact_members(archive,folder,requests):
    """Select exact old members; reject duplicate names, links or traversal."""
    selected={}
    with zipfile.ZipFile(archive) as z:
        members=z.infolist()
        for info in members:
            safe_name(info.filename)
            mode=(info.external_attr>>16)&0o170000
            if mode==0o120000:
                raise ValueError("an old artifact contains a symbolic link")
        for key,item in requests.items():
            logical=item["logical_file"]
            matches=[x for x in members if not x.is_dir()
                     and (x.filename==logical or x.filename.endswith("/"+logical))]
            if len(matches)!=1:
                raise ValueError("an exact original archive member is absent or ambiguous: "+logical)
            info=matches[0];dst=folder/safe_name(item.get("output",Path(logical).name))
            dst.parent.mkdir(parents=True,exist_ok=True)
            with z.open(info) as source,dst.open("wb") as out:
                shutil.copyfileobj(source,out,1<<20)
            expected=item.get("bytes")
            if expected is not None and dst.stat().st_size!=expected:
                raise ValueError("an original restored member size changed")
            if item.get("sha256") is not None and sha(dst)!=item["sha256"]:
                raise ValueError("an original restored member SHA changed")
            selected[key]=dst
    return selected

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
    p.add_argument("--resume",type=Path);p.add_argument("--resume-sha")
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("only this public repository Actions may evaluate new SC mathematics")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:
        raise ValueError("the separately pinned SC manifest or reviewed rules changed")
    m=read(a.manifest);rules=read(a.rules)
    if (m.get("public_repository")!=PUBLIC or rules.get("repository")!=PUBLIC
        or m.get("kind")!="immutable_complete97_signed_cap_affine_inputs_v1"
        or m.get("expected_actual_gate_count")!=20
        or m.get("files")!={x["path"]:x["sha256"] for x in m["file_receipts"]}
        or len(m["files"])!=len(m["file_receipts"])
        or m.get("new_native_arrays_or_artifact_persistence_allowed") is not False):
        raise ValueError("the exact new SC input contract changed")
    for key in ("reproducible_data_persisted_in_repository","reproducible_data_persisted_in_Releases",
                "new_reproducible_Actions_output_uploads"):
        if rules["large_data_policy"].get(key) is not False:
            raise ValueError("the current complete rule15 policy is required")
    rm=a.manifest.relative_to(root);rr=a.rules.relative_to(root);rw=Path(__file__).resolve().relative_to(root)
    gb=["git","-c","safe.directory="+str(root)]
    if a.mode=="hydrate":
        paths={str(PIPELINE),str(rw),str(rm),str(rr),str(REPORTS)+"/"}|set(rules["readme_sha256"])
        paths.update(entry["path"] for entry in m["file_receipts"])
        paths.add(m["operational_live_review_index"])
        paths.add(str(TOPIC/"notes")+"/*reviewed-public-CI-rules*.json")
        subprocess.run(gb+["sparse-checkout","set","--no-cone","--stdin"],cwd=root,
            input="\n".join("/"+v for v in sorted(paths))+"\n",text=True,check=True)
        print("Hydrated only pinned small text and explicit rule reviews; old natives stay outside Git.",flush=True)
        return
    if a.work is None or a.out_dir is None:
        raise ValueError("temporary SC work and outcome directories are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():
        raise FileExistsError("preserve the previous complete or partial SC run")
    if any(v.is_relative_to(root) for v in (work,out)):
        raise ValueError("original natives and new numerical arrays must remain outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__)
    state=dict(kind="actual_public_complete97_signed_cap_affine_execution_v1",repository=PUBLIC,
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
            raise ValueError("a pinned SC source manifest or rule record changed during pull")
        if sha(root/rw)!=ws:
            raise ValueError("the currently running immutable SC wrapper changed")
        for name in m["current_input_paths"]:
            if sha(root/relpath(name))!=m["files"][name]:
                raise ValueError("an immutable current SC helper or contract changed")
        published,blobs=topic_tree_metadata(git,TOPIC,PUBLIC)
        capacity=owned_head_delta(git,root,published,blobs,owned_paths)
        state.update(current_published_topic_capacity_metadata=published,
            current_topic_capacity_metadata=capacity,current_topic_blob_bytes=capacity["blob_bytes"],
            current_topic_blob_count=capacity["blob_count"],current_topic_metadata_commit=capacity["commit"],
            current_topic_below_200000000_bytes=capacity["blob_bytes"]<200000000)
        save(out/"worker-process.json",state)
        if capacity["blob_bytes"]+120000>=200000000:
            raise ValueError("the actual topic lacks the required120000-byte small-conclusion reserve")
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
        print(json.dumps(dict(kind="SC_DEFERRED_READ_ONLY_METADATA_PUBLICATION",**event,
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
    fetched=set()
    def ensure_commit(commit):
        if (not isinstance(commit,str) or len(commit)!=40
            or any(c not in "0123456789abcdef" for c in commit)):
            raise ValueError("one old restoration commit is not immutable")
        if commit not in fetched:
            git("fetch","--filter=blob:none","--no-tags","origin",commit)
            fetched.add(commit)
    def restore_git(entry,default_commit,allow_current):
        name=relpath(entry["path"]);dst=work/name
        dst.parent.mkdir(parents=True,exist_ok=True)
        expected=entry.get("bytes")
        current=root/name
        if allow_current and current.is_file() and (expected is None or current.stat().st_size==expected) \
                and sha(current)==entry["sha256"]:
            shutil.copyfile(current,dst);origin="exact_current_small_text"
        else:
            if entry["path"] in m["current_input_paths"]:
                raise ValueError("a new immutable SC source or contract is absent from checkout")
            commit=entry.get("commit",default_commit);ensure_commit(commit)
            # cat-file is immutable Git metadata; it is not a target or numerical producer.
            size=int(git("cat-file","-s",commit+":"+str(name)).stdout.strip())
            if size<0 or size>m["maximum_original_Git_blob_bytes"]:
                raise ValueError("an old native exceeds its explicitly bounded restore size")
            if expected is not None and size!=expected:
                raise ValueError("an original Git blob byte count differs from its pinned receipt")
            with dst.open("wb") as stream:
                git("show",commit+":"+str(name),stdout=stream)
            expected=size;origin="exact_historical_Git_blob"
        checked(dst,expected if expected is not None else dst.stat().st_size,entry["sha256"])
        return dst,dict(role=entry["role"],path=str(name),bytes=dst.stat().st_size,
            sha256=entry["sha256"],origin=origin,
            commit=None if origin=="exact_current_small_text" else entry.get("commit",default_commit))
    proc=None;child=None;new_array_dir=work/"new-scientific-temporary"
    try:
        git("config","user.name","github-actions[bot]")
        git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
        sync();last_checkpoint=time.monotonic()
        pins=m["mathematical_input_sha256"];parameters=m["parameters"]
        runtime=dict(python=sys.version.split()[0],bits=parameters["arithmetic_bits"],
            packages={k:importlib.metadata.version(k) for k in m["scientific_runtime"]["packages"]})
        helper=next(x["sha256"] for x in m["file_receipts"] if x["role"]=="math_helper")
        reader=next(x["sha256"] for x in m["file_receipts"] if x["role"]=="original_reader")
        state["actual_scientific_runtime"]=runtime
        if runtime!=m["scientific_runtime"]:
            raise ValueError("exact Python arithmetic packages or precision differ before reuse")
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
                if scientific_receipt_valid(prior,a.pipeline_sha,None,parameters,pins,runtime,helper,reader):
                    print(json.dumps(dict(reused_complete_same_scientific_conclusion=str(pp.relative_to(root)),
                        original_run_id=previous["run_id"],original_science_bytes=ref["bytes"],
                        original_science_sha256=ref["sha256"],execution_sha256=sha(path),
                        original_wrapper_complete=previous.get("complete"),
                        new_scientific_processes=0,old_successful_mathematics_recomputed=0)),flush=True)
                    return
            if same_record and previous.get("actual_new_scientific_processes",0)>0 and a.resume is None:
                raise RuntimeError("same SC mathematics has a prior incomplete outcome; require its concrete review and exact scientific-prefix recovery")
        state["mathematical_input_sha256"]=pins
        inputs=[];index_files={}
        for entry in m["file_receipts"]:
            dst,receipt=restore_git(entry,m["historical_small_text_commit"],True)
            inputs.append(receipt)
            index_files[entry["role"]]=dict(path=str(dst),bytes=dst.stat().st_size,sha256=entry["sha256"])
            checkpoint()
        for entry in m["historical_native_receipts"]:
            dst,receipt=restore_git(entry,entry["commit"],False)
            inputs.append(receipt)
            if not entry["role"].startswith("candidate_shard_"):
                index_files[entry["role"]]=dict(path=str(dst),bytes=dst.stat().st_size,sha256=entry["sha256"])
            checkpoint()
        state["actual_original_Git_input_receipts"]=inputs
        state["actual_verified_Git_input_count"]=len(inputs)
        state["actual_verified_Git_input_receipts_sha256"]=hashlib.sha256(compact(inputs)).hexdigest()
        tm=work/rm;tm.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.manifest,tm)
        checked(tm,a.manifest.stat().st_size,a.manifest_sha)
        tr=work/rr;tr.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.rules,tr)
        checked(tr,a.rules.stat().st_size,a.rules_sha)
        parsed=[]
        for entry in m["file_receipts"]:
            if entry["path"].endswith(".py"):
                source=work/relpath(entry["path"]);ast.parse(source.read_text(),filename=str(source))
                parsed.append(dict(path=entry["path"],sha256=entry["sha256"]))
        state.update(complete_immutable_Python_AST_closure_passed=True,
            complete_immutable_Python_AST_file_count=len(parsed),
            complete_immutable_Python_AST_inventory_sha256=hashlib.sha256(compact(parsed)).hexdigest())
        # Restore only specifically pinned OLD artifacts.  No workflow creates a new artifact.
        archives=work/"original-artifacts";archive_receipts=[]
        plan_spec=m["old_artifacts"]["plan"]
        archive,receipt=exact_old_artifact(plan_spec,archives/"plan",token,checkpoint)
        selected=extract_exact_members(archive,archives/"plan",{
            "native":dict(plan_spec["native"],output="original-plan.json.gz"),
            "process":dict(plan_spec["process"],output="original-plan-process.json")})
        archive_receipts.append(receipt);archive.unlink()
        plan_path=selected["native"]
        index_files["plan"]=dict(path=str(plan_path),bytes=plan_path.stat().st_size,
            sha256=sha(plan_path))
        plan=json.loads(gzip.decompress(plan_path.read_bytes()))
        if (plan.get("complete") is not True or plan.get("failure") is not None
            or len(plan.get("bundles",[]))!=32
            or plan.get("object_identity_sha256")!=m["original_object_identity_sha256"]
            or index_files["plan"]["sha256"]!=pins["plan"]):
            raise ValueError("the complete immutable original slice plan changed")
        pilots=[]
        for k,spec in enumerate(m["old_artifacts"]["pilot_ranges"]):
            archive,receipt=exact_old_artifact(spec,archives/("pilot-%d"%k),token,checkpoint)
            selected=extract_exact_members(archive,archives/("pilot-%d"%k),{
                "native":dict(logical_file=spec["logical_file"],sha256=spec["native_sha256"],
                              output="original-pilot-range.json.gz"),
                "process":dict(logical_file="process.json",sha256=spec["artifact_process_sha256"],
                               output="original-pilot-process.json")})
            archive_receipts.append(receipt);archive.unlink()
            pilots.append(dict(path=str(selected["native"]),sha256=spec["native_sha256"]))
            checkpoint()
        slices=[]
        for group,spec in enumerate(m["old_artifacts"]["slices"]):
            if spec.get("group")!=group:
                raise ValueError("the complete original slice artifact list changed order")
            folder=archives/("slice-%02d"%group)
            archive,receipt=exact_old_artifact(spec,folder,token,checkpoint)
            desc=plan["bundles"][group]
            index_spec=dict(desc["bundle_index"])
            index_spec["logical_file"]=Path(index_spec["file"]).name
            index_spec["output"]="bundle-index.json"
            selected=extract_exact_members(archive,folder,{"index":index_spec})
            oldindex=read(selected["index"])
            if (oldindex.get("group")!=group
                or oldindex.get("object_identity_sha256")!=m["original_object_identity_sha256"]):
                raise ValueError("one immutable original slice index has the wrong object")
            members={}
            for i,item in enumerate(oldindex["exact_source_files"]):
                member=dict(item);member["logical_file"]=item["file"];member["output"]=item["file"]
                members[str(i)]=member
            extract_exact_members(archive,folder,members)
            receipt.update(group=group,bundle_index_sha256=sha(selected["index"]),
                exact_member_count=1+len(members))
            archive_receipts.append(receipt);archive.unlink()
            slices.append(dict(group=group,path=str(folder)))
            print(json.dumps(dict(kind="SC_ORIGINAL_INPUT_SLICE_RESTORED",group=group,
                artifact_id=spec["artifact_id"],bundle_index_sha256=receipt["bundle_index_sha256"],
                old_mathematical_producer_calls=0)),flush=True)
            checkpoint()
        if len(slices)!=32 or len(pilots)!=3 or len(archive_receipts)!=36:
            raise ValueError("the original exact input restoration is incomplete")
        state["original_artifact_receipts"]=archive_receipts
        state["complete_old_artifact_restore_count"]=36
        state["original_artifact_archive_bytes"]=sum(x["bytes"] for x in archive_receipts)
        state["original_artifact_restore_receipts_sha256"]=hashlib.sha256(compact(archive_receipts)).hexdigest()
        state["new_artifact_count"]=0;state["new_Release_count"]=0
        index=dict(kind="exact_original_SC_input_paths_v1",manifest_sha256=a.manifest_sha,
            files=index_files,pilot_native_files=pilots,slice_directories=slices,
            original_artifact_receipts_sha256=state["original_artifact_restore_receipts_sha256"])
        ip=work/"complete-original-input-index.json";save(ip,index)
        state["complete_original_input_index"]=dict(bytes=ip.stat().st_size,sha256=sha(ip))
        cmd=[sys.executable,"-u",str(work/PIPELINE),"--manifest",str(tm),
            "--manifest-sha",a.manifest_sha,"--input-index",str(ip),
            "--temporary",str(new_array_dir),"--out",str(out/"actual-scientific-conclusion.json")]
        if a.resume is not None:
            if not a.resume_sha or sha(a.resume)!=a.resume_sha:
                raise ValueError("an explicit scientific-prefix recovery requires its exact SHA")
            recovered=work/"recovered-complete-scientific-prefix.json"
            shutil.copyfile(a.resume,recovered)
            cmd+=["--resume",str(recovered),"--resume-sha",a.resume_sha]
            state["authorized_exact_scientific_prefix"]=dict(bytes=recovered.stat().st_size,
                sha256=a.resume_sha,source=str(a.resume))
        state["command_sha256"]=hashlib.sha256(compact(cmd)).hexdigest()
        state["actual_scientific_checkout_commit"]=git("rev-parse","HEAD").stdout.strip()
        state["scientific_child_launch_attempted"]=True
        state["ordinary_source_target_QR_and_Gram_recomputations"]=0
        save(out/"worker-process.json",state)
        ce=os.environ.copy()
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
        valid=scientific_receipt_valid(proc,a.pipeline_sha,a.manifest_sha,parameters,pins,runtime,helper,reader)
        state["complete_mathematical_receipt_available"]=valid
        state["complete"]=bool(child.returncode==0 and valid)
        state["actual_failure"]=None if state["complete"] else (
            proc.get("failure") if proc and proc.get("failure") else
            dict(type="IncompleteScientificReceipt",message="the full twenty-gate SC receipt did not validate"))
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
                runtime,helper,reader)
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
    for filename,field,marker in (
        ("latest-scientific-prefix.json","last_complete_scientific_prefix","SC_SCIENTIFIC_PREFIX"),
        ("complete-known-parameter-model.json","complete_known_parameter_model_checkpoint","SC_KNOWN_MODEL")):
        path=new_array_dir/filename
        if path.is_file():
            raw=path.read_bytes();value=json.loads(raw)
            info=dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
            # Re-emit the complete atomic file even if its last original print
            # was still buffered at termination. This reads saved science only.
            print(json.dumps(dict(kind="SC_ATOMIC_SCIENCE_REPRINT",file=filename,**info)),flush=True)
            print(marker+"_BEGIN",flush=True);print(raw.decode(),end="",flush=True)
            print(marker+"_END",flush=True)
            state[field]=dict(**info,complete_groups=value.get("completed_groups"),
                complete_quarters=value.get("completed_quarters"),
                covered_exact_interval=value.get("covered_exact_interval"),
                atomic_file_completely_reprinted=True,preserved_in_original_Actions_stdout=True,
                not_uploaded_as_array_artifact=True)
    outputs=[out/name for name in ("actual-scientific-conclusion.json","new-scientific-child.stdout.log")]
    state["output_hashes"]=[rec(path,out) for path in outputs if path.is_file()]
    if proc is not None:
        original=out/"actual-scientific-conclusion.json"
        if original.read_bytes()!=compact(proc):
            raise ValueError("the complete child science must retain its original canonical bytes")
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
        if len(raw)>59000 or len(text.encode())>12000 or (science_raw is not None and len(science_raw)>45000):
            raise ValueError("full science is already preserved in stdout; one publication small-text gate failed")
        (report/"actual-result.md").write_text(text)
        (report/"execution.json").write_bytes(raw)
        if science_raw is not None:
            (report/"actual-scientific-conclusion.json").write_bytes(science_raw)
    def publish():
        snapshot();owned=str(report.relative_to(root));git("add","--sparse","--",owned)
        if git("diff","--cached","--quiet","--",owned,check=False).returncode!=0:
            git("commit","-m","visible-exact: record complete97 signed cap affine functional and full error")
        while True:
            result=git("push","origin","HEAD:refs/heads/main",check=False)
            if result.returncode==0:
                return owned
            if not any(v in result.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
                raise RuntimeError("small SC conclusion push failed outside concurrent-main rebase")
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
