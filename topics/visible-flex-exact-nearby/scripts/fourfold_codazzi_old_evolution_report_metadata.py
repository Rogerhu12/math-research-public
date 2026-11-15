#!/usr/bin/env python3
"""Pure metadata audit of two immutable old floating reports; zero scientific work."""
from __future__ import annotations
import argparse,base64,hashlib,json,os,subprocess,sys,time,urllib.error,urllib.request
from datetime import datetime,timezone
from pathlib import Path

PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
SOURCE=TOPIC/"scripts/fourfold_codazzi_old_evolution_report_metadata.py"
REPORTS=TOPIC/"notes/old_evolution_report_metadata_ci"
RESTORE="b9c7cde9c28a38d9d7db2ad03fcfd3835578ac6b"
EXPECTED_INPUTS=[
 dict(path=str(TOPIC/"notes/2026-11-13-codazzi-evolution-r0235-n512-floating.json"),
      git_blob="e7fe4210bae462d8360d967534f3425c9e1756e7",bytes=360313),
 dict(path=str(TOPIC/"notes/2026-11-13-codazzi-evolution-r0235-n1024-floating.json"),
      git_blob="de04339caa70cc10e4c55aaf3e9ea18fdfc719b8",bytes=360182)]
EXPECTED_READMES={
 "README.md":"6979d793d8335488df16d92c5617c6e5f25503187d5c27f22041eb8a027dbec9",
 str(TOPIC/"README.md"):"81249053c4c14a7a14289b58184e1b81601146d412fa117973f7a1d05bf95220"}
FIELDS=(
 "kind","complete","certified","status","exception","source_sha256","object_sha256",
 "dependency_sha256","origin_sha256","direction_sha256","exact_center_parameter",
 "primitive_nodes","angular_grid","nonlinear_grid","Nyquist_removed","mean_retained",
 "original_target_fixed","whole_real_angular_circle","whole_parameter_interval",
 "whole_radial_domain","method","rtol","atol","max_step","n_floor","max_rhs",
 "requested_radial_interval","finished_radial_interval","rhs_calls",
 "sampled_maxima","sampled_minimum_abs_n","sampled_support_min",
 "endpoint_state_path","endpoint_state_sha256","wall_seconds","limitations")
REQUIRED=("kind","complete","certified","status","exception","source_sha256",
 "object_sha256","origin_sha256","direction_sha256","requested_radial_interval",
 "finished_radial_interval","endpoint_state_path","endpoint_state_sha256","rows")
def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)
def raw_json(x):return (canonical(x)+"\n").encode()
def utc():return datetime.now(timezone.utc).isoformat()
def digest(b):return hashlib.sha256(b).hexdigest()
def sha(p):return digest(Path(p).read_bytes())
def save(p,x):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    q=p.with_name(p.name+".tmp");q.write_bytes(raw_json(x));q.replace(p)
def read(p):return json.loads(Path(p).read_bytes())
def require(test,message):
    if not test:raise ValueError(message)
class TransientMetadataError(RuntimeError):pass

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


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest",type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    parser.add_argument("--source-sha",required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and
            os.environ.get("GITHUB_REPOSITORY")==PUBLIC,"only the authorized public Actions job")
    manifest=args.manifest.resolve();out=args.out.resolve()
    require(not out.is_relative_to(root),"all temporary old report bodies remain outside Git")
    require(not out.exists(),"preserve any pre-existing metadata audit")
    out.mkdir(parents=True)
    source=Path(__file__).resolve()
    require(sha(source)==args.source_sha,"the separately pinned metadata source changed")
    require(sha(manifest)==args.manifest_sha,"the separately pinned metadata manifest changed")
    spec=read(manifest)
    require(spec.get("kind")=="immutable_old_evolution_report_metadata_inputs_v1"
        and spec.get("public_repository")==PUBLIC
        and spec.get("restore_commit")==RESTORE
        and spec.get("source_sha256")==args.source_sha
        and spec.get("reports")==EXPECTED_INPUTS
        and spec.get("readme_sha256")==EXPECTED_READMES
        and spec.get("scientific_computations")==0
        and spec.get("producer_calls")==0 and spec.get("delete_any_file") is False,
        "the exact two-file metadata contract changed")
    state=dict(kind="actual_immutable_old_evolution_report_metadata_v1",
        repository=PUBLIC,run_id=os.environ["GITHUB_RUN_ID"],
        run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],workflow_commit=os.environ["GITHUB_SHA"],
        source_sha256=args.source_sha,manifest_sha256=args.manifest_sha,
        immutable_restore_commit=RESTORE,started_utc=utc(),finished_audit_utc=None,
        complete=False,actual_returncode=None,failure=None,readme_checks=[],
        complete_report_metadata=[],input_count=2,report_bodies_requested_by_chat=False,
        old_report_bodies_only_runner_temporary=True,
        scientific_computations=0,producer_calls=0,old_math_recomputed=0,
        new_numerical_enclosures=0,new_artifacts=0,new_Releases=0,new_arrays=0,
        deleted_files=0,eligible_for_deletion_not_decided=True,
        original_failed_reports_are_not_relabelled_as_success=True,
        metadata_complete_does_not_assert_original_report_success=True,
        publication=None)
    run_dir=REPORTS/("run-"+state["run_id"]+"-"+state["run_attempt"])
    owned=str(run_dir/"actual-report-metadata.json")
    gb=["git","-c","safe.directory="+str(root)]
    env=os.environ.copy();token=env.pop("GITHUB_TOKEN")
    env.update(GIT_TERMINAL_PROMPT="0",GIT_CONFIG_COUNT="1",
        GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
        GIT_CONFIG_VALUE_0="AUTHORIZATION: basic "+base64.b64encode(("x-access-token:"+token).encode()).decode())
    def git(*cmd,check=True,binary=False):
        result=subprocess.run(gb+list(cmd),cwd=root,env=env,text=not binary,
            stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=180)
        if check and result.returncode:
            err=result.stderr if isinstance(result.stderr,str) else result.stderr.decode("utf-8","replace")
            raise RuntimeError("Git "+str(cmd[0])+" failed: "+err[:1200])
        return result
    def emit(stage):
        save(out/"actual-report-metadata.json",state)
        data=raw_json(state)
        print(canonical(dict(marker="OLD_REPORT_METADATA_STATUS",stage=stage,
            bytes=len(data),sha256=digest(data),complete=state["complete"],
            reports_read=len(state["complete_report_metadata"]),scientific_computations=0)),flush=True)
        print("OLD_REPORT_METADATA_COMPLETE_PAYLOAD_BEGIN",flush=True)
        print(data.decode(),end="",flush=True)
        print("OLD_REPORT_METADATA_COMPLETE_PAYLOAD_END",flush=True)
        return data
    def sync():
        before=git("rev-parse","HEAD").stdout.strip()
        git("pull","--rebase","origin","main")
        after=git("rev-parse","origin/main").stdout.strip()
        diff=git("diff",before,after,"--",*EXPECTED_READMES).stdout
        current={name:sha(root/name) for name in EXPECTED_READMES}
        state["readme_checks"].append(dict(time=utc(),before=before,after=after,
            actual_diff=diff,actual_readme_sha256=current))
        save(out/"actual-report-metadata.json",state)
        if diff or current!=EXPECTED_READMES:
            print("OLD_REPORT_METADATA_UNREVIEWED_README_DIFF_BEGIN",flush=True)
            print(diff,end="" if diff.endswith("\n") else "\n",flush=True)
            print("OLD_REPORT_METADATA_UNREVIEWED_README_DIFF_END",flush=True)
            raise RuntimeError("unreviewed README change: preserve metadata and await root review")
        require(sha(source)==args.source_sha and sha(manifest)==args.manifest_sha,
                "a frozen metadata source or manifest changed after the actual pull")
        state["actual_checkout_commit"]=git("rev-parse","HEAD").stdout.strip()
    policy_ok=False
    try:
        git("config","user.name","github-actions[bot]")
        git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
        sync();policy_ok=True
        if git("cat-file","-e",RESTORE+"^{commit}",check=False).returncode:
            git("fetch","--filter=blob:none","--no-tags","origin",RESTORE)
        for expected in EXPECTED_INPUTS:
            row=dict(expected=expected,immutable_restore_commit=RESTORE,
                metadata_complete=False,identity_verified=False,failure=None)
            state["complete_report_metadata"].append(row)
            try:
                oid=git("rev-parse",RESTORE+":"+expected["path"]).stdout.strip()
                require(oid==expected["git_blob"],"immutable report Git blob differs")
                body=git("cat-file","blob",oid,binary=True).stdout
                actual_oid=hashlib.sha1(b"blob "+str(len(body)).encode()+b"\0"+body).hexdigest()
                row.update(actual_git_blob=actual_oid,actual_bytes=len(body),actual_sha256=digest(body))
                require(len(body)==expected["bytes"] and actual_oid==oid,
                        "immutable report full bytes or Git object identity differs")
                row["identity_verified"]=True
                temporary=out/(Path(expected["path"]).name+".temporary")
                temporary.write_bytes(body)
                nonfinite_tokens={}
                def preserve_original_constant(token):
                    nonfinite_tokens[token]=nonfinite_tokens.get(token,0)+1
                    return {"original_nonfinite_JSON_token":token}
                original=json.loads(body.decode("utf-8"),parse_constant=preserve_original_constant)
                row["original_nonfinite_JSON_constant_counts"]=nonfinite_tokens
                row["nonfinite_encoding"]="Only original NaN/Infinity tokens, if present, are tagged; ordinary JSON fields are unchanged."
                require(isinstance(original,dict),"the old report is not a complete JSON object")
                row["all_top_level_keys"]=list(original)
                row["original_fields_read_verbatim"]={k:original[k] for k in FIELDS if k in original}
                row["missing_required_fields"]=[k for k in REQUIRED if k not in original]
                rows=original.get("rows")
                row["original_sampled_row_count"]=len(rows) if isinstance(rows,list) else None
                row["original_first_sample_r"]=rows[0].get("r") if isinstance(rows,list) and rows else None
                row["original_last_sample_r"]=rows[-1].get("r") if isinstance(rows,list) and rows else None
                row["original_sampled_rows_not_recomputed"]=True
                row["original_success_flag_read_from_report"]=(
                    original.get("complete") is True and original.get("status")=="finished"
                    and original.get("exception") is None)
                require(not row["missing_required_fields"],"the exact old report metadata schema is incomplete")
                require(original["kind"]=="floating_dealiased_two_field_Codazzi_with_position_reconstruction",
                        "the old file is not the authorized floating diagnostic report")
                row["metadata_complete"]=True
                # The whole original bytes are runner-only and are never uploaded or committed.
                temporary.unlink()
                del body,original,rows
            except Exception as error:
                row["failure"]=dict(type=type(error).__name__,message=str(error))
            emit("one_original_report_metadata_complete")
        state["complete"]=len(state["complete_report_metadata"])==2 and all(
            r["identity_verified"] and r["metadata_complete"] for r in state["complete_report_metadata"])
        state["actual_returncode"]=0 if state["complete"] else 1
        if not state["complete"]:
            state["failure"]=dict(type="IncompleteMetadataAudit",
                message="one or both original report metadata records are incomplete")
    except BaseException as error:
        state["complete"]=False;state["actual_returncode"]=1
        state["failure"]=dict(type=type(error).__name__,message=str(error))
    state["finished_audit_utc"]=utc()
    emit("complete_audit_before_any_publication")
    # No scientific reserve gate is bypassed: there is no scientific child or arithmetic.
    # The only output is this complete small metadata receipt. The topic limit still applies.
    try:
        if not policy_ok:raise RuntimeError("initial policy check failed; stdout preserves the full partial metadata")
        deadline=time.monotonic()+600
        while True:
            try:
                sync()
                capacity,blobs=topic_tree_metadata(git,TOPIC,PUBLIC)
                previous=blobs.get(owned,{}).get("bytes",0)
                state["publication"]=dict(base_commit=capacity["commit"],
                    base_topic_blob_bytes=capacity["blob_bytes"],
                    metadata_inventory_sha256=capacity["complete_blob_metadata_inventory_sha256"],
                    blob_bodies_requested_for_capacity=False,
                    owned_output_path=owned,old_owned_output_bytes=previous,
                    projected_topic_blob_bytes=0)
                while True:
                    data=raw_json(state)
                    projected=capacity["blob_bytes"]-previous+len(data)
                    if projected==state["publication"]["projected_topic_blob_bytes"]:break
                    state["publication"]["projected_topic_blob_bytes"]=projected
                data=emit("complete_metadata_before_git_publication")
                require(len(data)<=30000,"complete metadata exceeds the predesigned small receipt bound")
                require(projected<200000000,"the complete tiny metadata receipt exceeds topic capacity")
                target=root/owned;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
                git("add","--sparse","--",owned)
                staged=git("diff","--cached","--name-only").stdout.splitlines()
                require(set(staged)<={owned},"unrelated staged paths cannot enter metadata publication")
                if staged:git("commit","-m","visible-exact: preserve immutable old report metadata without science")
                pushed=git("push","origin","HEAD:refs/heads/main",check=False)
                if pushed.returncode==0:break
                if not any(v in pushed.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
                    raise RuntimeError("small metadata publication push failed")
                # The real failed push is preserved; rebase retains every concurrent remote commit.
                if time.monotonic()>deadline:raise RuntimeError("metadata publication retry time exceeded")
            except TransientMetadataError:
                if time.monotonic()>deadline:raise
                time.sleep(10)
        print(canonical(dict(kind="OLD_REPORT_METADATA_PUBLISHED",path=owned,
            bytes=len(data),sha256=digest(data),complete=state["complete"],
            scientific_computations=0,deleted_files=0,new_artifacts=0,new_Releases=0)),flush=True)
    except BaseException as error:
        state["publication_failure"]=dict(type=type(error).__name__,message=str(error))
        emit("metadata_preserved_publication_failed")
        raise SystemExit(1)
    raise SystemExit(state["actual_returncode"])

if __name__=="__main__":main()
