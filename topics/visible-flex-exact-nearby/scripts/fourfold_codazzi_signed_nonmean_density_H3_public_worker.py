#!/usr/bin/env python3
"""Public complete signed nonmean density transport; persist only small conclusions."""
from __future__ import annotations
import argparse,ast,base64,hashlib,json,os,shutil,signal,subprocess,sys,time
import re,urllib.error,urllib.parse,urllib.request,zipfile
from datetime import datetime,timezone
from pathlib import Path
PUBLIC="Rogerhu12/math-research-public"
TOPIC=Path("topics/visible-flex-exact-nearby")
PIPELINE=TOPIC/"scripts/fourfold_codazzi_signed_nonmean_density_H3.py"
REPORTS=TOPIC/"notes/signed_nonmean_density_H3_ci"
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


CHILD_SECONDS=340*60
PULL_SECONDS=540
GATE_COUNT=21
KIND="actual_complete_signed_nonmean_density_H3_validation_v1"

def canonical(v):
    return (json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()

def scientific_complete(proc,source,helper,manifest):
    p=proc or {};t=p.get("complete_new_transport_conclusion",{})
    c=p.get("complete_first_nonmean_coefficient_H3_conclusion",{})
    a=c.get("true_angle_derivatives",{});branches=c.get("branches",{})
    return bool(p.get("kind")==KIND and p.get("complete") is True
        and p.get("new_target_complete") is True and p.get("actual_returncode")==0
        and p.get("failure") is None and p.get("source_sha256")==source
        and p.get("helper_sha256")==helper and p.get("input_manifest_sha256")==manifest
        and p.get("actual_gate_count")==GATE_COUNT and len(p.get("gates",[]))==GATE_COUNT
        and all(g.get("passed") is True for g in p["gates"])
        and p.get("old_successful_mathematical_computations_repeated")==0
        and p.get("new_recomputable_arrays_persisted") is False
        and p.get("complete_infinite_inverse_or_PDE_solution_proved") is False
        and t.get("original_intervals_read")==3146 and t.get("original_candidate_pieces_read")==2550
        and 0<t.get("new_subcells",0)<=120000
        and set(t.get("complete_error_columns",{}))=={"-1","1"}
        and all(len(t["complete_error_columns"][s])==4 for s in ("-1","1"))
        and t.get("complete_residual_modes_not_truncated") is True
        and t.get("original_scalar_integrals_not_repeated") is True
        and t.get("ordinary_inward_radial_measure")=="dr"
        and a.get("literal_31over32_33over32_gates_verified") is True
        and set(branches)=={"-1","1"}
        and all(branches[s].get("complete_mean_is_exactly_zero") is True for s in branches)
        and isinstance(c.get("complete_nonmean_first_symbol_H3_upper"),dict)
        and c.get("full_real_family_transport_half_width")=="1/10000000000"
        and c.get("true_angle_only_at_original_selected_parameter") is True
        and c.get("same_selected_parameter_and_true_mean") is True
        and c.get("original_two_rays_and_KAM_not_recomputed") is True
        and c.get("original_scalar_beta_not_substituted_for_this_target") is True
        and c.get("linear_or_exponential_strong_return_remainder_proved") is False
        and c.get("incoming_high_inverse_or_true_PDE_background_transfer_proved") is False)

def latest_progress(path):
    if not path.is_file():return None
    with path.open("rb") as stream:
        stream.seek(max(0,path.stat().st_size-30000))
        lines=stream.read().decode("utf-8","replace").splitlines()
    for line in reversed(lines):
        try:v=json.loads(line)
        except (ValueError,TypeError):continue
        if isinstance(v,dict) and v.get("stage")=="new-complete-nonmean-transport":
            return {k:v.get(k) for k in ("stage","original_interval","new_subcells",
                "exact_radial_cursor","complete_error_H3")}
    return None

def emit_recoverable_conclusion(state,science,log):
    """Print complete original small science and the whole child log before publication."""
    records={}
    for label,path in (("SCIENCE",science),("CHILD_LOG",log)):
        if not path.is_file():continue
        raw=path.read_bytes()
        receipt=dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
            encoding="UTF-8",complete_original_bytes=True,
            printed_before_final_pull_or_publication=True)
        records[label]=receipt
        print("BEGIN_R133_SIGNED_NONMEAN_H3_"+label+" "+json.dumps(receipt,sort_keys=True,separators=(",",":")),flush=True)
        text=raw.decode("utf-8");print(text,end="",flush=True)
        if not text.endswith("\n"):print("",flush=True)
        print("END_R133_SIGNED_NONMEAN_H3_"+label,flush=True)
    small={k:state.get(k) for k in ("run_id","run_attempt","workflow_commit",
        "worker_source_sha256","source_budget_source_sha256","helper_source_sha256",
        "input_manifest_sha256","reviewed_rules_sha256","actual_returncode",
        "actual_source_budget_processes","scientific_target_complete","actual_failure",
        "supervision_failure","latest_actual_progress","source_budget_child_wall_seconds")}
    print("R133_SIGNED_NONMEAN_H3_ACTUAL_STATUS "+json.dumps(small,sort_keys=True,separators=(",",":")),flush=True)
    return records

def render(state):
    p=state.get("actual_scientific_receipt") or {}
    t=p.get("complete_new_transport_conclusion",{})
    c=p.get("complete_first_nonmean_coefficient_H3_conclusion",{})
    progress=state.get("latest_actual_progress")
    lines=["# Complete signed nonmean density transport: actual execution","",
        "- Public repository: "+PUBLIC,
        "- Run: "+state["run_id"]+"/"+state["run_attempt"],
        "- New source SHA256: "+state["source_budget_source_sha256"],
        "- New helper SHA256: "+state["helper_source_sha256"],
        "- Frozen input manifest SHA256: "+state["input_manifest_sha256"],
        "- Actual child count: "+str(state["actual_source_budget_processes"]),
        "- Actual child return code: "+str(state.get("actual_returncode")),
        "- Complete new scientific target: "+str(state.get("scientific_target_complete",False)),
        "- Old successful mathematical computations repeated: 0.",
        "- New numerical arrays, native files, artifacts and Releases published: 0.",""]
    if progress is not None:
        lines+=["## Actual progress","", "Latest complete child stdout record; this is not a terminal certificate.","",
            "~~~json",json.dumps(progress,sort_keys=True,separators=(",",":")),"~~~",""]
    if state.get("scientific_target_complete"):
        lines+=["## Complete new conclusion","",
            "The entire scientific receipt, all twenty-one gates, both branches, all Fourier modes and the true mean are in execution.json.","",
            "| Quantity | Complete directed enclosure |","|---|---|",
            "| True-angle nonmean first-symbol H3 norm | "+cell(ball(c["complete_nonmean_first_symbol_H3_upper"]))+" |",
            "| Original selected scalar mean, copied | "+cell(ball(c["complete_scalar_mu_copied"]))+" |",
            "| New complete subcells | "+str(t["new_subcells"])+" |",""]
        for sign in ("-1","1"):
            b=c["branches"][sign]
            lines+=["### Branch "+sign,"",
                "- Complete qG H3: "+ball(b["complete_qG_H3"]),
                "- Complete transport H3 error: "+ball(b["complete_transport_H3_error"]),
                "- Complete finite-angle H3 tail: "+ball(b["complete_finite_angle_tail_H3"]),
                "- Exact nonmean normalization: "+str(b["complete_mean_is_exactly_zero"])+".",""]
    elif state.get("actual_returncode") is not None or state.get("actual_failure") is not None:
        lines+=["## Actual incomplete target","","~~~json",
            json.dumps(state.get("actual_failure"),sort_keys=True,separators=(",",":")),"~~~","",
            "No new complete H3 constant is asserted. The original child log and any produced scientific bytes were printed before publication.",""]
    else:
        lines+=["The one declared new scientific child is active or preparing. No terminal H3 constant is asserted.",""]
    lines+=["## Scope","",
        "Old scalar finite parts, intrinsic germs, root steps, responses, rays and circle iterations are read only. The new target is the signed nonmean forced density, its full residual and H3 enclosure. The true-angle readout uses the original selected parameter and retains both branches and all means.","",
        "This receipt gives no complete strong-return remainder, incoming inverse, infinite high inverse or true PDE background transfer. Temporary complete source and reference coefficients remain only within this runner.",""]
    return "\n".join(lines)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--mode",choices=("hydrate","run"),required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);p.add_argument("--pipeline-sha",required=True)
    p.add_argument("--rules",type=Path,required=True);p.add_argument("--rules-sha",required=True)
    p.add_argument("--work",type=Path);p.add_argument("--out-dir",type=Path)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("only the declared public Actions may consume these scientific inputs")
    root=Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    a.manifest=a.manifest.resolve();a.rules=a.rules.resolve()
    if sha(a.manifest)!=a.manifest_sha or sha(a.rules)!=a.rules_sha:
        raise ValueError("a separately pinned execution contract changed")
    m=read(a.manifest);rules=read(a.rules)
    if m["public_repository"]!=PUBLIC or rules["repository"]!=PUBLIC:raise ValueError("wrong public repository")
    for key in ("reproducible_data_persisted_in_repository","reproducible_data_persisted_in_Releases","new_reproducible_Actions_output_uploads"):
        if rules["large_data_policy"].get(key) is not False:raise ValueError("the reviewed no-data rule15 is required")
    if (m.get("old_successful_scientific_calls_allowed") is not False
        or m.get("historical_input_commit")!="5e14fd1de48f7c51dbe465cebef048c3d948fc76"
        or set(m.get("allowed_historical_commits",[]))!={"5e14fd1de48f7c51dbe465cebef048c3d948fc76","46f127c7153f5393dcd2a00f42d4c1d3662c294d"}
        or m.get("maximum_child_seconds")!=CHILD_SECONDS):
        raise ValueError("only the declared read-only historical inputs and single long new child are allowed")
    rows=m["file_receipts"]
    if len(rows)!=len(m["files"]) or any(m["files"].get(e["path"])!=e["sha256"] for e in rows):
        raise ValueError("the two complete input identity tables disagree")
    rm=a.manifest.relative_to(root);rr=a.rules.relative_to(root);rw=Path(__file__).resolve().relative_to(root)
    gb=["git","-c","safe.directory="+str(root)]
    if a.mode=="hydrate":
        paths={str(PIPELINE),str(rw),str(rm),str(rr),str(REPORTS)+"/"}|set(rules["readme_sha256"])
        paths.update(m["current_text_paths"])
        subprocess.run(gb+["sparse-checkout","set","--no-cone","--stdin"],cwd=root,
            input="\n".join("/"+v for v in sorted(paths))+"\n",text=True,check=True)
        print("Hydrated only frozen new sources, small contracts, prior small execution records and reviewed READMEs.",flush=True)
        return
    if a.work is None or a.out_dir is None:raise ValueError("temporary work paths are required")
    work=a.work.resolve();out=a.out_dir.resolve()
    if work.exists() or out.exists():raise FileExistsError("preserve an existing actual execution")
    if any(v.is_relative_to(root) for v in (work,out)):raise ValueError("all restored or new numerical data stays outside Git")
    work.mkdir(parents=True);out.mkdir(parents=True)
    ws=sha(__file__);helper=m["helper_source_sha256"]
    state=dict(kind="actual_public_signed_nonmean_density_H3_execution",repository=PUBLIC,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt=os.environ["GITHUB_RUN_ATTEMPT"],
        workflow_commit=os.environ["GITHUB_SHA"],worker_source_sha256=ws,
        source_budget_source_sha256=a.pipeline_sha,helper_source_sha256=helper,
        input_manifest_sha256=a.manifest_sha,reviewed_rules_sha256=a.rules_sha,
        explicitly_read_rules_commit=rules["read_commit"],started_utc=utc(),
        complete=False,scientific_target_complete=False,actual_returncode=None,
        actual_source_budget_processes=0,old_numerical_enclosures_recomputed=0,
        reproducible_data_published_to_repository=False,reproducible_data_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False,full_high_inverse_claimed=False,
        final_topic_complete=False,readme_checks=[],latest_actual_progress=None)
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
            raise ValueError("a separately pinned execution contract changed during pull")
        if sha(root/m["helper_path"])!=helper or sha(root/rw)!=ws:
            raise ValueError("the frozen helper or running wrapper changed during pull")

    report=root/REPORTS/("run-"+state["run_id"]+"-"+state["run_attempt"])
    def snapshot():
        report.mkdir(parents=True,exist_ok=True);text=render(state)
        names=[str((report/name).relative_to(root)) for name in ("actual-result.md","execution.json")]
        capacity,blob_map=topic_tree_metadata(git,TOPIC,PUBLIC)
        state["publication_owned_HEAD_delta"]=owned_head_delta(git,root,capacity,blob_map,owned_small_paths)
        total=capacity["blob_bytes"];oldbytes=sum(blob_map[n]["bytes"] for n in names if n in blob_map)
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
        if len(text.encode())>60000 or len(raw)>60000:
            raise ValueError("mathematical bytes are saved; only this publication wrapper exceeds the small-text limit")
        (report/"actual-result.md").write_text(text);(report/"execution.json").write_bytes(raw)
    def publish(final=False):
        snapshot();owned=str(report.relative_to(root));git("add","--sparse","--",owned)
        if git("diff","--cached","--quiet","--",owned,check=False).returncode==0:return
        git("commit","-m","visible-exact: record signed nonmean H3 "+("conclusion" if final else "actual progress"))
        while True:
            r=git("push","origin","HEAD:refs/heads/main",check=False)
            if r.returncode==0:break
            if not any(v in r.stderr for v in ("non-fast-forward","fetch first","cannot lock ref","remote rejected")):
                raise RuntimeError("small conclusion push failed outside concurrent-main rebase")
            sync();snapshot();git("add","--sparse","--",owned);git("commit","--amend","--no-edit")
        state["last_small_publication_utc"]=utc()

    git("config","user.name","github-actions[bot]")
    git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
    sync()
    for old in sorted((root/REPORTS).glob("*/execution.json")):
        v=read(old)
        if v.get("input_manifest_sha256")!=a.manifest_sha or v.get("source_budget_source_sha256")!=a.pipeline_sha:continue
        if scientific_complete(v.get("actual_scientific_receipt"),a.pipeline_sha,helper,a.manifest_sha):
            print(json.dumps(dict(reused_existing_complete_conclusion=str(old.relative_to(root)),
                original_run_id=v["run_id"],new_source_budget_processes=0,
                original_wrapper_returncode=v.get("actual_returncode"),new_numerical_enclosures=0)),flush=True)
            return
        if v.get("actual_source_budget_processes",0)>0:
            raise RuntimeError("the same frozen target has a prior started child; recover its saved science or bind a specific new lost-result receipt before any replay")

    actual_inputs=[];fetched=set();last_sync=time.monotonic()
    current=set(m["current_text_paths"])
    for entry in rows:
        rel=relpath(entry["path"]);src=root/rel;dst=work/rel
        dst.parent.mkdir(parents=True,exist_ok=True)
        if str(rel) in current:
            if entry["bytes"]>=100000 or not str(rel).endswith((".json",".py",".md")):
                raise ValueError("a current contract is not pinned small text")
            checked(src,entry["bytes"],entry["sha256"]);shutil.copyfile(src,dst)
            origin=dict(kind="exact_current_small_contract")
        elif src.is_file() and src.stat().st_size==entry["bytes"] and sha(src)==entry["sha256"]:
            shutil.copyfile(src,dst);origin=dict(kind="exact_current_original_input")
        else:
            commit=m["historical_input_overrides"].get(str(rel),m["historical_input_commit"])
            if commit not in m["allowed_historical_commits"]:raise ValueError("an original restore commit is not pinned")
            if commit not in fetched:
                git("fetch","--no-tags","--filter=blob:none","origin",commit);fetched.add(commit)
            with dst.open("wb") as stream:git("show",commit+":"+str(rel),stdout=stream)
            origin=dict(kind="exact_immutable_original_historical_input",commit=commit)
        checked(dst,entry["bytes"],entry["sha256"])
        actual_inputs.append(dict(path=str(rel),bytes=entry["bytes"],sha256=entry["sha256"],origin=origin))
        if time.monotonic()-last_sync>PULL_SECONDS:
            sync();last_sync=time.monotonic()
    state["actual_verified_input_count"]=len(actual_inputs)
    state["actual_verified_input_receipts_sha256"]=hashlib.sha256(canonical(actual_inputs)).hexdigest()
    origins={}
    for entry in actual_inputs:
        key=entry["origin"]["kind"];origins[key]=origins.get(key,0)+1
    state["actual_input_origins"]=origins
    state["actual_current_contract_receipts"]=[e for e in actual_inputs if e["path"] in current]
    tm=work/rm;tm.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.manifest,tm)
    checked(tm,a.manifest.stat().st_size,a.manifest_sha)
    parsed=[]
    for entry in rows:
        if entry["path"].endswith(".py"):
            path=work/relpath(entry["path"]);ast.parse(path.read_text(),filename=str(path))
            parsed.append(dict(path=entry["path"],sha256=entry["sha256"]))
    state["complete_immutable_Python_AST_closure_passed"]=True
    state["complete_immutable_Python_AST_file_count"]=len(parsed)
    state["complete_immutable_Python_AST_inventory_sha256"]=hashlib.sha256(canonical(parsed)).hexdigest()
    if state["current_topic_blob_bytes"]+120000>200000000:
        print(json.dumps(dict(kind="insufficient_small_conclusion_capacity",actual_source_budget_processes=0,
            capacity=state["current_topic_capacity_metadata"],reserved_small_conclusion_bytes=120000)),flush=True)
        raise ValueError("actual topic capacity cannot reserve two bounded small conclusions")
    c=out/"consumers";c.mkdir()
    science=c/"science.json";log=out/"source-budget.stdout.log"
    cmd=[sys.executable,"-u",str(work/PIPELINE),"--root",str(work),"--manifest",str(tm),
        "--manifest-sha",a.manifest_sha,"--out",str(science),"--temporary",str(out/"temporary-new-source"),
        "--bits","320"]
    state["command"]=cmd;state["actual_scientific_checkout_commit"]=git("rev-parse","HEAD").stdout.strip()
    state["actual_source_budget_processes"]=1
    state["maximum_child_seconds"]=CHILD_SECONDS;state["periodic_true_pull_seconds"]=PULL_SECONDS
    save(out/"worker-process.json",state)
    ce=os.environ.copy();ce.pop("GITHUB_TOKEN",None)
    ce["ACTUAL_CHECKOUT_COMMIT"]=state["actual_scientific_checkout_commit"]
    started=time.monotonic();state["supervision_failure"]=None
    with log.open("wb") as stream:
        child=subprocess.Popen(cmd,cwd=work,env=ce,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
        try:
            while child.poll() is None:
                remaining=CHILD_SECONDS-(time.monotonic()-started)
                if remaining<=0:
                    state["timeout_seconds"]=CHILD_SECONDS
                    break
                if time.monotonic()-last_sync>PULL_SECONDS:
                    state["latest_actual_progress"]=latest_progress(log)
                    state["source_budget_child_wall_seconds"]=time.monotonic()-started
                    save(out/"worker-process.json",state)
                    sync()
                    if child.poll() is None:publish(final=False)
                    last_sync=time.monotonic()
                try:child.wait(timeout=min(60,remaining))
                except subprocess.TimeoutExpired:pass
        except Exception as error:
            state["supervision_failure"]=dict(type=type(error).__name__,message=str(error))
        finally:
            if child.poll() is None:
                os.killpg(child.pid,signal.SIGTERM)
                try:child.wait(timeout=10)
                except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
            state["actual_returncode"]=child.returncode
    state["source_budget_child_wall_seconds"]=time.monotonic()-started
    state["latest_actual_progress"]=latest_progress(log)
    proc=read(science) if science.is_file() else None
    state["scientific_target_complete"]=scientific_complete(proc,a.pipeline_sha,helper,a.manifest_sha)
    state["complete"]=state["scientific_target_complete"]
    state["actual_failure"]=(dict(type="MissingScientificConclusion",
        message="the actual child produced no complete science.json; its entire original log is retained")
        if proc is None else proc.get("failure"))
    if proc is not None:state["actual_scientific_receipt"]=proc
    state["output_hashes"]=[rec(path,out) for path in (science,log) if path.is_file()]
    temporary=out/"temporary-new-source"/"complete-new-signed-source-and-reference.jsonl.gz"
    if temporary.is_file():state["output_hashes"].append(rec(temporary,out))
    save(out/"worker-process.json",state)
    state["recoverable_prepublication_stdout"]=emit_recoverable_conclusion(state,science,log)
    save(out/"worker-process.json",state)
    # Every mathematical byte and every child log byte is already saved and emitted.
    # A later wrapper failure never authorizes repeating a completed scientific child.
    sync();publish(final=True)
    print(json.dumps(dict(complete=state["complete"],actual_returncode=state["actual_returncode"],
        report=str(report.relative_to(root)),old_numerical_enclosures_recomputed=0,
        new_source_budget_processes=1,new_recomputable_data_files_persisted=0)),flush=True)
    if not state["scientific_target_complete"] or state.get("supervision_failure") is not None:
        raise SystemExit(1)

if __name__=="__main__":main()
