"""W2C public collar/dual runner: complete21 restoration and one new child.

Every 1800 seconds during the child, pull main and check both complete README
diffs.  A failed rule check stops and drains the child before preserving its
whole scientific prefix.  Only operational diagnostics are size bounded.
"""
from __future__ import annotations
import argparse, ast, base64, codecs, gzip, hashlib, json, os
from pathlib import Path
import selectors, subprocess, sys, tempfile, time, traceback, urllib.request
from datetime import datetime, timezone

REPO="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby"
LIMIT=200000000
RESERVE=120000

class ReadonlyCompleted(Exception):
    """Internal successful readonly completion; never a scientific outcome."""
    pass

def check(ok, message):
    if not ok:
        raise ValueError(message)

def utc():
    return datetime.now(timezone.utc).isoformat()

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def encode(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode("utf-8")

def parse(raw):
    return json.loads(raw,parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))

def atomic(path, raw):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+".tmp")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary,path)

def safe_path(value):
    check(isinstance(value,str) and value.startswith(TOPIC+"/"),"topic path required")
    check(not any(p in ("..",".","") for p in value.split("/")),"unsafe relative path")
    return value

def bounded_operation_text(text, maximum_json_bytes):
    """Only an operational diagnostic; complete text is printed first."""
    check(isinstance(text,str) and type(maximum_json_bytes) is int
          and maximum_json_bytes>=2,"operational diagnostic byte contract")
    def size(prefix):
        return len(json.dumps(prefix,ensure_ascii=False).encode("utf-8"))
    if size(text)<=maximum_json_bytes:
        return text,False
    left,right=0,len(text)
    while left<right:
        middle=(left+right+1)//2
        if size(text[:middle])<=maximum_json_bytes:
            left=middle
        else:
            right=middle-1
    return text[:left],True

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo",required=True)
    ap.add_argument("--manifest",required=True)
    ap.add_argument("--manifest-sha",required=True)
    args=ap.parse_args()
    check(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPO,
          "only the authorized public repository runner")
    root=Path(args.repo).resolve()
    os.chdir(root)
    def git(*argv,check_return=True,binary=False):
        p=subprocess.run(["git","-c","user.name=github-actions[bot]",
            "-c","user.email=41898282+github-actions[bot]@users.noreply.github.com",
            *argv],cwd=root,capture_output=True,text=not binary)
        if check_return and p.returncode:
            error=p.stderr.decode("utf-8","replace") if binary else p.stderr
            raise RuntimeError("git "+" ".join(argv)+" failed: "+error)
        return p
    token=os.environ["GITHUB_TOKEN"]
    auth=base64.b64encode(("x-access-token:"+token).encode()).decode()
    os.environ["GIT_CONFIG_COUNT"]="1"
    os.environ["GIT_CONFIG_KEY_0"]="http.https://github.com/.extraheader"
    os.environ["GIT_CONFIG_VALUE_0"]="AUTHORIZATION: basic "+auth
    run=os.environ["GITHUB_RUN_ID"]
    attempt=os.environ["GITHUB_RUN_ATTEMPT"]
    entry_head=git("rev-parse","HEAD").stdout.strip()
    mpath=Path(args.manifest)
    if not mpath.is_absolute():
        mpath=root/mpath
    manifest_raw=mpath.read_bytes()
    check(len(manifest_raw)<100000 and sha(manifest_raw)==args.manifest_sha,"complete frozen manifest")
    manifest=parse(manifest_raw)
    check(manifest["repository"]==REPO,"manifest repository")
    op=manifest["operation"]
    check(op["reserve_bytes"]==RESERVE and op["topic_maximum_bytes"]==LIMIT,"fixed capacity policy")
    check(type(op["maximum_total_publication_bytes"]) is int and op["maximum_total_publication_bytes"]>0,
          "complete publication budget")
    output_relative=safe_path(op["output_base"]+"/run-"+run+"-"+attempt)
    marker_relative=safe_path(op["consumed_marker"])
    result_name=op["scientific_filename"]
    check(result_name=="actual-scientific-conclusion.json","complete single scientific output")
    state={"kind":"small_frozen_public_scientific_execution_v1","repository":REPO,
           "problem_id":manifest["problem_id"],"manifest_sha256":args.manifest_sha,
           "run_id":run,"run_attempt":attempt,"workflow_event_commit":os.environ["GITHUB_SHA"],
           "entry_checkout":entry_head,"started_utc":utc(),"readme_checks":[],
           "current_input_receipts":[],"AST_receipts":[],"historical_restoration":None,
           "scientific_children":0,"completed_old_targets_recomputed":0,
           "new_artifacts":0,"new_Releases":0,"new_arrays_published":0,
           "readme_check_count":0,"readme_receipt_chain_sha256":None,"all_pulls_match_review":True,
           "failure":None,"actual_child_returncode":None,"publication_attempts":0}
    check(type(op.get("readonly_diagnostic_only",False)) is bool,"typed diagnostic flag")
    state["readonly_diagnostic_only"]=op.get("readonly_diagnostic_only",False)
    state["readonly_diagnostic_complete"]=False
    temporary=Path(tempfile.mkdtemp(prefix="visible-exact-frozen-",dir=os.environ.get("RUNNER_TEMP")))
    output=temporary/result_name
    staged_files={}
    science_started=False
    result=None

    def fetch_commit(commit):
        check(isinstance(commit,str) and len(commit)==40 and all(c in "0123456789abcdef" for c in commit),
              "immutable commit required")
        if git("cat-file","-e",commit+"^{commit}",check_return=False).returncode:
            git("fetch","--filter=blob:none","--no-tags","--depth=1","origin",commit)

    review_spec=manifest["reviewed_rules"]
    def current_bytes(spec,head):
        path=safe_path(spec["path"])
        tree_blob=git("rev-parse",head+":"+path).stdout.strip()
        check(tree_blob==spec["git_blob_sha"],"current Git identity: "+path)
        raw=git("show",head+":"+path,binary=True).stdout
        check(0<len(raw)<100000 and len(raw)==spec["bytes"] and sha(raw)==spec["sha256"]
              and blob(raw)==tree_blob,"complete current bytes: "+path)
        raw.decode("utf-8")
        return raw

    review_raw=current_bytes(review_spec,entry_head)
    review=parse(review_raw)
    check(review["repository"]==REPO and review["scientific_input_manifests_and_sources_not_changed"] is True
          and review["new_unread_rules_must_still_be_reported_and_applied"] is True,"explicit rule review")
    policy=review["large_data_policy"]
    check(policy["maximum_topic_bytes"]==LIMIT and policy["keep_only_scripts_parameters_runs_output_hashes_and_conclusions"] is True
          and policy["original_completed_mathematics_must_not_be_recomputed"] is True
          and policy["normal_deletion_only"] is True and policy["no_history_rewrite"] is True,
          "unchanged public execution policy")
    read_commit=review["read_commit"]
    fetch_commit(read_commit)
    for path,digest in review["readme_sha256"].items():
        check(sha(git("show",read_commit+":"+path,binary=True).stdout)==digest,"review commit README identity")

    def pull():
        before=git("rev-parse","HEAD").stdout.strip()
        began=utc()
        git("pull","--rebase","origin","main")
        after=git("rev-parse","HEAD").stdout.strip()
        paths=list(review["readme_sha256"])
        actual_diff=git("diff",before,after,"--",*paths).stdout
        review_diff=git("diff",read_commit,after,"--",*paths).stdout
        observed={path:sha(git("show",after+":"+path,binary=True).stdout) for path in paths}
        receipt={"started":began,"finished":utc(),"before":before,"after":after,
                 "actual_diff":actual_diff,"diff_from_explicit_review":review_diff,
                 "read_commit":read_commit,"review_sha256":review_spec["sha256"],
                 "readme_sha256":observed}
        previous=state["readme_receipt_chain_sha256"]
        state["readme_check_count"]+=1
        state["readme_receipt_chain_sha256"]=sha(encode({"previous":previous,"receipt":receipt}))
        state["readme_checks"].append(receipt)
        if len(state["readme_checks"])>4:
            state["readme_checks"]=[state["readme_checks"][0],*state["readme_checks"][-3:]]
            state["readme_retention"]="first and latest three full receipts; all earlier receipts printed before hash chaining"
        state["all_pulls_match_review"] &= observed==review["readme_sha256"] and not review_diff
        print("COMPLETE ACTUAL PULL RECEIPT "+encode(receipt).decode("utf-8"),end="",flush=True)
        if actual_diff:
            print("ACTUAL README DIFF\n"+actual_diff,flush=True)
        if review_diff:
            print("DIFF FROM EXPLICIT RULE REVIEW\n"+review_diff,flush=True)
        check(observed==review["readme_sha256"] and not review_diff,"new unread README requires root review")
        return after

    capacity_tree_cache={}
    def capacity(head):
        """Published whole-tree metadata plus the exact complete local Git delta.

        After a rejected push and a real rebase, HEAD may contain our unpushed
        output commit.  Such a local tree is not a GitHub REST resource.  The
        fetched origin/main is published; only changed local blob sizes need
        Git object reads.  This is administrative byte accounting only.
        """
        tree_sha=git("rev-parse",head+":"+TOPIC).stdout.strip()
        base_head=git("rev-parse","origin/main").stdout.strip()
        base_tree=git("rev-parse",base_head+":"+TOPIC).stdout.strip()
        if base_tree not in capacity_tree_cache:
            request=urllib.request.Request(
                "https://api.github.com/repos/"+REPO+"/git/trees/"+base_tree+"?recursive=1",
                headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json"})
            with urllib.request.urlopen(request,timeout=60) as response:
                raw=response.read()
            data=parse(raw)
            check(data.get("truncated") is False and data["sha"]==base_tree,
                  "complete published-base capacity metadata")
            base_sizes={};base_blobs={}
            for row in data["tree"]:
                if row["type"]=="blob":
                    check(type(row["size"]) is int and row["size"]>=0,
                          "complete Git-tree size")
                    relative=safe_path(TOPIC+"/"+row["path"])
                    check(relative not in base_sizes,"unique whole published-tree path")
                    base_sizes[relative]=row["size"]
                    base_blobs[relative]=row["sha"]
            capacity_tree_cache.clear()
            capacity_tree_cache[base_tree]=(len(raw),sha(raw),base_sizes,base_blobs)
        metadata_bytes,metadata_sha256,base_sizes,base_blobs=capacity_tree_cache[base_tree]
        sizes=dict(base_sizes);blobs=dict(base_blobs)
        delta=git("diff","--raw","--no-abbrev","--no-renames","-z",
                  base_head,head,"--",TOPIC,binary=True).stdout
        tokens=delta.split(b"\0")
        check(tokens[-1]==b"" and (len(tokens)-1)%2==0,
              "complete NUL-delimited local topic delta")
        changes=[];null_sha="0"*40
        for i in range(0,len(tokens)-1,2):
            parts=tokens[i].decode("ascii").split()
            relative=safe_path(tokens[i+1].decode("utf-8"))
            check(len(parts)==5 and parts[0].startswith(":")
                  and parts[4] in ("A","D","M","T"),
                  "complete ordinary local file delta")
            old_sha,new_sha=parts[2],parts[3]
            check(old_sha==blobs.get(relative,null_sha),
                  "local delta starts at the exact published-base blob")
            before=sizes.get(relative,0)
            if new_sha==null_sha:
                after=0
                check(relative in sizes,"complete original deleted local blob")
                del sizes[relative];del blobs[relative]
            else:
                check(git("cat-file","-t",new_sha).stdout.strip()=="blob",
                      "changed local topic object is a complete blob")
                after=int(git("cat-file","-s",new_sha).stdout.strip())
                check(after>=0,"exact complete changed local blob size")
                sizes[relative]=after;blobs[relative]=new_sha
            changes.append({"path":relative,"status":parts[4],
                            "old_git_blob_sha":old_sha,"new_git_blob_sha":new_sha,
                            "old_bytes":before,"new_bytes":after})
        return {"head":head,"topic_tree":tree_sha,"topic_blob_bytes":sum(sizes.values()),
                "metadata_bytes":metadata_bytes,"metadata_sha256":metadata_sha256,
                "blob_count":len(sizes),"published_metadata_base_head":base_head,
                "published_metadata_base_topic_tree":base_tree,
                "complete_local_delta_bytes":len(delta),
                "complete_local_delta_sha256":sha(delta),
                "complete_changed_local_blobs":changes},sizes

    def concurrent_pending_reservations():
        """Admit every other active workflow's exact source before classifying it."""
        declared=op["concurrent_pending_run_reservations"]
        bindings=op["concurrent_workflow_scope_bindings"]
        check(isinstance(declared,list) and isinstance(bindings,list),
              "explicit complete active-workflow scopes and publication reservations")
        expected_keys={"run_id","run_attempt","workflow_path","maximum_total_publication_bytes"}
        for item in declared:
            check(set(item)==expected_keys and str(item["run_id"]).isdigit()
                  and str(item["run_attempt"]).isdigit()
                  and type(item["maximum_total_publication_bytes"]) is int
                  and item["maximum_total_publication_bytes"]>0,
                  "whole explicit concurrent run reservation")
        binding_keys={"role","path","git_blob_sha","bytes","sha256","writes_topic"}
        for item in bindings:
            path=item.get("path")
            check(set(item)==binding_keys and isinstance(item["role"],str)
                  and bool(item["role"]) and isinstance(path,str)
                  and path.startswith(".github/workflows/")
                  and not any(p in ("..",".","") for p in path.split("/"))
                  and path.endswith((".yml",".yaml"))
                  and type(item["bytes"]) is int and 0<item["bytes"]<100000
                  and isinstance(item["git_blob_sha"],str)
                  and len(item["git_blob_sha"])==40
                  and all(c in "0123456789abcdef" for c in item["git_blob_sha"])
                  and isinstance(item["sha256"],str) and len(item["sha256"])==64
                  and all(c in "0123456789abcdef" for c in item["sha256"])
                  and type(item["writes_topic"]) is bool,
                  "whole typed active-workflow source binding")
        by_run={(str(x["run_id"]),str(x["run_attempt"])):x for x in declared}
        by_source={(x["path"],x["git_blob_sha"]):x for x in bindings}
        check(len(by_run)==len(declared)
              and len(by_source)==len(bindings)
              and len({x["role"] for x in bindings})==len(bindings),
              "unique concurrent run reservations and exact source identities")
        active={};observed={};verified_sources={}
        for status in ("queued","in_progress","waiting","pending","requested"):
            page=1
            while True:
                url=("https://api.github.com/repos/"+REPO+"/actions/runs?status="+status+
                     "&per_page=100&page="+str(page))
                request=urllib.request.Request(url,headers={
                    "Authorization":"Bearer "+token,"Accept":"application/vnd.github+json"})
                with urllib.request.urlopen(request,timeout=60) as response:
                    raw=response.read()
                payload=parse(raw);runs=payload["workflow_runs"]
                check(isinstance(runs,list),"complete active-run metadata page")
                for item in runs:
                    if str(item["id"])==run:
                        continue
                    key=(str(item["id"]),str(item["run_attempt"]))
                    path=item.get("path","")
                    check(any(x["path"]==path for x in bindings),
                          "undeclared active workflow requires complete source scope: "+str(key)+" "+path)
                    run_head=item["head_sha"]
                    fetch_commit(run_head)
                    actual_blob=git("rev-parse",run_head+":"+path).stdout.strip()
                    check((path,actual_blob) in by_source,
                          "unreviewed active-workflow source version: "+str(key)+" "+path)
                    spec=by_source[(path,actual_blob)]
                    cache_key=(run_head,path,actual_blob)
                    if cache_key not in verified_sources:
                        source_raw=git("show",run_head+":"+path,binary=True).stdout
                        check(len(source_raw)==spec["bytes"]
                              and sha(source_raw)==spec["sha256"]
                              and blob(source_raw)==spec["git_blob_sha"],
                              "complete actual active-workflow UTF8 source identity")
                        source_raw.decode("utf-8")
                        verified_sources[cache_key]=True
                    receipt={"run_id":key[0],"run_attempt":key[1],"workflow_head":run_head,
                             "source_binding":dict(spec),"complete_source_byte_identity_verified":True}
                    check(key not in observed or observed[key]==receipt,
                          "immutable workflow source throughout active-run pagination")
                    observed[key]=receipt
                    if spec["writes_topic"]:
                        check(key in by_run and by_run[key]["workflow_path"]==path,
                              "active topic writer needs its whole publication budget: "+str(key))
                        active[key]=by_run[key]
                if len(runs)<100:
                    break
                page+=1
        result={"checked_utc":utc(),
                "complete_other_active_workflows":[observed[k] for k in sorted(observed)],
                "complete_active_topic_runs":[active[k] for k in sorted(active)],
                "reserved_bytes":sum(x["maximum_total_publication_bytes"] for x in active.values()),
                "all_active_workflow_sources_byte_verified":True,
                "workflow_code_executed":False}
        print("COMPLETE ACTIVE WORKFLOW SCOPE RECEIPT "+encode(result).decode("utf-8"),end="",flush=True)
        return result

    def emit(name,raw):
        print("BEGIN COMPLETE PUBLIC FILE "+name+" bytes="+str(len(raw))+" sha256="+sha(raw),flush=True)
        sys.stdout.write(raw.decode("utf-8"))
        sys.stdout.flush()
        print("END COMPLETE PUBLIC FILE "+name,flush=True)

    def publish(files,message,budget):
        while True:
            head=pull()
            if marker_relative in files and git("cat-file","-e",head+":"+marker_relative,check_return=False).returncode==0:
                prior=parse(git("show",head+":"+marker_relative,binary=True).stdout)
                check(prior.get("run_id")==run and prior.get("run_attempt")==attempt,
                      "another attempt already consumed this exact new target")
            cap,sizes=capacity(head)
            projected=cap["topic_blob_bytes"]
            for relative,raw in files.items():
                safe_path(relative)
                check(0<len(raw)<100000,"complete small UTF8 publication")
                raw.decode("utf-8")
                projected+=len(raw)-sizes.get(relative,0)
            check(sum(map(len,files.values()))<=budget,"complete publication branch budget")
            pending=concurrent_pending_reservations()
            check(projected+op["maximum_total_publication_bytes"]+
                  pending["reserved_bytes"]+RESERVE<=LIMIT,
                  "reserved new child, concurrent pending outputs and120000B before marker")
            for relative,raw in files.items():
                atomic(root/relative,raw)
                emit(relative,raw)
            git("add","--sparse","--",*files)
            if git("diff","--cached","--quiet",check_return=False).returncode==0:
                return {"commit":head,"capacity":cap,"projected_topic_bytes":projected,"already_present":True}
            git("-c","user.name=github-actions[bot]",
                "-c","user.email=41898282+github-actions[bot]@users.noreply.github.com",
                "commit","-m",message)
            pushed=git("push","origin","HEAD:main",check_return=False)
            if pushed.returncode==0:
                return {"commit":git("rev-parse","HEAD").stdout.strip(),"capacity":cap,
                        "projected_topic_bytes":projected,"already_present":False}
            print("Push rejected: immediately pull --rebase and check both READMEs.",flush=True)
            pull()

    def materialize(head):
        specs=manifest["files"]
        check(len(specs)==manifest["expected_current_input_count"]
              and len({x["path"] for x in specs})==len(specs)
              and len({x["role"] for x in specs})==len(specs),"unique current inputs")
        receipts=[]
        asts=[]
        for spec in specs:
            raw=current_bytes(spec,head)
            path=root/spec["path"]
            if not path.is_file() or path.read_bytes()!=raw:
                atomic(path,raw)
            receipts.append(dict(spec))
            if path.suffix==".py":
                ast.parse(raw.decode("utf-8"),filename=spec["path"])
                asts.append({"path":spec["path"],"sha256":spec["sha256"],"role":spec["role"]})
        check(manifest["worker"] in specs and Path(__file__).resolve()==(root/manifest["worker"]["path"]).resolve(),
              "actual frozen worker")
        check(review_spec in specs,"review is a complete admitted current input")
        check(all(x in specs for x in manifest["scientific_modules"]),"all new modules bound")
        check(sha(mpath.read_bytes())==args.manifest_sha,"manifest unchanged after pull")
        state["current_input_receipts"]=receipts
        state["AST_receipts"]=asts

    def restore():
        all_originals=manifest.get("historical_inputs",[])
        check(len(all_originals)==21 and len({x["role"] for x in all_originals})==21
              and len({x["path"] for x in all_originals})==21,"whole21 original restoration list")
        originals=all_originals[:19]
        additions=all_originals[19:]
        check(manifest["inventory"] in manifest["files"]
              and manifest["collar_input_inventory"] in manifest["files"],
              "both complete typed inventories admitted")
        inventory=parse((root/safe_path(manifest["inventory"]["path"])).read_bytes())
        collar_inventory=parse((root/safe_path(manifest["collar_input_inventory"]["path"])).read_bytes())
        check(originals==inventory["historical_inputs"]==
                  collar_inventory["preexisting_WVC_historical_inputs_retained"]
              and additions==collar_inventory["two_additional_native_restorations"],
              "exact original19 plus two source-qualified collar natives")
        check(len(originals)==19 and len({x["path"] for x in originals})==19
              and len({x["role"] for x in originals})==19,"all19 distinct original objects")
        body=[x for x in originals if x["role"].startswith("original_positive_native_part_")]
        candidate=[x for x in originals if x["role"].startswith("original_candidate_part_")]
        repairs=[x for x in originals if x["role"]=="original_continuous_centre_repair"]
        check(len(body)==13 and len(candidate)==5 and len(repairs)==1,"13 native,5 cubic,1 repair")
        check(originals==body+candidate+repairs,"frozen typed restoration order")
        expected=inventory["readonly_restoration"]["original_positive_native"]
        index_spec=next(x for x in inventory["existing_small_text_inputs"] if x["role"]=="candidate_index")
        check(index_spec in manifest["files"],"complete original candidate index admitted")
        index_raw=(root/safe_path(index_spec["path"])).read_bytes()
        check(len(index_raw)==index_spec["bytes"] and sha(index_raw)==index_spec["sha256"]
              and blob(index_raw)==index_spec["git_blob_sha"],"original complete index bytes")
        index=parse(index_raw)
        check(index["kind"]=="complete_lossless_radial_cubic_shards_v1"
              and len(index["parts"])==5,"unchanged original cubic index")
        for item,part in zip(candidate,index["parts"]):
            check(Path(item["path"]).name==part["file"]
                  and item["bytes"]==part["bytes"] and item["sha256"]==part["sha256"]
                  and item["first_interval"]==part["first_interval"]
                  and item["last_interval_exclusive"]==part["last_interval_exclusive"],
                  "exact historical parts agree with the admitted cubic index")
        native=temporary/"complete-original-native.json.gz"
        candidate_dir=temporary/"original-candidate"
        candidate_dir.mkdir()
        candidate_index=candidate_dir/Path(index_spec["path"]).name
        atomic(candidate_index,index_raw)
        repair_path=temporary/Path(repairs[0]["path"]).name
        histories=[]
        offset=0
        def restored_bytes(item):
            fetch_commit(item["commit"])
            path=safe_path(item["path"])
            observed=git("rev-parse",item["commit"]+":"+path).stdout.strip()
            check(observed==item["git_blob_sha"],"historical Git identity")
            raw=git("show",item["commit"]+":"+path,binary=True).stdout
            check(len(raw)==item["bytes"] and blob(raw)==observed
                  and sha(raw)==item["sha256"],"complete historical compressed identity")
            return raw
        with native.open("wb") as stream:
            for number,item in enumerate(body):
                check(item["index"]==number,"complete original native part order")
                raw=restored_bytes(item)
                chunk=gzip.decompress(raw)
                check(item["offset"]==offset and len(chunk)==item["uncompressed_chunk_bytes"]
                      and sha(chunk)==item["uncompressed_chunk_sha256"],"complete original chunk")
                stream.write(chunk)
                offset+=len(chunk)
                histories.append({**item,"git_tree_blob_and_size_verified":True,
                    "compressed_sha256_verified":True,"chunk_sha256_verified":True})
            stream.flush()
            os.fsync(stream.fileno())
        raw=native.read_bytes()
        check(len(raw)==expected["complete_container_bytes"] and sha(raw)==expected["complete_container_sha256"],
              "complete original concatenated gzip")
        native_identity={"bytes":len(raw),"sha256":sha(raw),"complete_concatenation_verified":True}
        for item in candidate:
            raw=restored_bytes(item)
            destination=candidate_dir/Path(item["path"]).name
            atomic(destination,raw)
            check(destination.read_bytes()==raw,"complete original candidate writeback")
            histories.append({**item,"git_tree_blob_and_size_verified":True,
                "compressed_sha256_verified":True,"identical_original_bytes_materialized":True})
        raw=restored_bytes(repairs[0])
        atomic(repair_path,raw)
        check(repair_path.read_bytes()==raw,"complete original repair writeback")
        histories.append({**repairs[0],"git_tree_blob_and_size_verified":True,
            "compressed_sha256_verified":True,"identical_original_bytes_materialized":True})
        receipt={"kind":"complete_readonly_native_cubic_repair_restoration_v1",
             "historical_inputs":histories,"native":native_identity,
             "candidate_index":dict(index_spec),
             "candidate_part_roles":[x["role"] for x in candidate],
             "centre_repair_role":repairs[0]["role"],
             "old_producers_executed":0,"original_repairs_regenerated":0,
             "new_artifacts":0,"new_arrays_published":0,
             "scope":"Exact original data bytes only; scientific admission and new targets are separate."}
        original_raw=encode(receipt)
        provider_spec=manifest["completed_tracefree_scientific_input"]
        check(provider_spec in manifest["files"],"whole fixed WVC scientific provider")
        provider=parse((root/safe_path(provider_spec["path"])).read_bytes())
        check(receipt==provider["complete_restoration_receipts"]
              and len(original_raw)==13771
              and sha(original_raw)=="4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac",
              "entire original WVC19 restoration object unchanged")
        added_receipts=[];added_paths=[]
        for item in additions:
            raw=restored_bytes(item)
            check(raw.startswith(b"\x1f\x8b"),"complete original gzip before readonly child")
            destination=temporary/Path(item["path"]).name
            check(not destination.exists(),"two distinct private native materializations")
            atomic(destination,raw)
            check(destination.read_bytes()==raw,"complete original added native writeback")
            added_paths.append(destination)
            added_receipts.append({**item,"git_tree_blob_and_size_verified":True,
                "compressed_sha256_verified":True,"identical_original_bytes_materialized":True})
        receipt={"kind":"complete_W2C_readonly_restoration_v1",
            "original_WVC_restoration":receipt,"additional_historical_inputs":added_receipts,
            "historical_input_count":21,"old_producers_executed":0,
            "original_repairs_regenerated":0,"new_artifacts":0,"new_arrays_published":0}
        receipt_path=temporary/"complete-restoration-receipts.json"
        atomic(receipt_path,encode(receipt))
        state["historical_restoration"]=receipt
        return ["--native",str(native),"--native-receipts",str(receipt_path),
                "--candidate-index",str(candidate_index),"--centre-repair",str(repair_path),
                "--root-germ",str(added_paths[0]),"--root-budget",str(added_paths[1])]

    def child_environment():
        env=dict(os.environ)
        for key in tuple(env):
            if key in ("GITHUB_TOKEN","GH_TOKEN") or key.startswith("GIT_CONFIG_"):
                env.pop(key,None)
        env["PYTHONDONTWRITEBYTECODE"]="1"
        env["ACTUAL_CHECKOUT_COMMIT"]=state["actual_scientific_checkout"]
        return env

    def validate_scientific(raw):
        check(0<len(raw)<100000,"complete scientific output must remain one small UTF8 file")
        result=parse(raw)
        check(result["kind"]==op["scientific_kind"] and result["problem_id"]==manifest["problem_id"]
              and result["manifest_sha256"]==args.manifest_sha,"scientific identity binding")
        restored=state["historical_restoration"]
        check(isinstance(restored,dict)
              and restored["kind"]=="complete_W2C_readonly_restoration_v1",
              "complete actual restoration in this same execution")
        expected_restoration={
            "kind":"whole_same_outcome_execution_object_reference_v1",
            "path":output_relative+"/execution.json","json_path":["historical_restoration"],
            "complete_original_object_identity":{"bytes":len(encode(restored)),"sha256":sha(encode(restored))},
            "historical_input_count":21,
            "original_WVC_restoration_identity":{
                "bytes":len(encode(restored["original_WVC_restoration"])),
                "sha256":sha(encode(restored["original_WVC_restoration"]))},
            "whole_original_object_must_be_published_in_same_outcome":True}
        check(result["complete_restoration_receipts"]==expected_restoration,
              "lossless full21 receipt bound to the complete same-outcome execution field")
        check(result["parameters"]==manifest["parameters"],"complete parameters retained")
        check(result["scientific_modules"]==op.get("scientific_module_binding",manifest["scientific_modules"]),"complete source binding")
        check(result["actual_checkout_commit"]==state["actual_scientific_checkout"],"actual science checkout")
        check(type(result["complete"]) is bool and isinstance(result["gates"],list),"complete scientific envelope")
        check(result.get("retained_scope")==op["retained_scope"],"complete retained physical scope")
        check(len(raw)<=op["maximum_scientific_bytes"],"scientific complete byte budget")
        target_names=result["completed_targets"]
        expected=op["ordered_targets"]
        check(isinstance(target_names,list) and target_names==expected[:len(target_names)],"whole ordered completed prefix")
        check(len(set(target_names))==len(target_names),"no new target repeated")
        check(result["current_target"] is None or result["current_target"]==expected[len(target_names)],
              "exact interrupted target")
        if result["complete"]:
            check(set(result)==set(op["scientific_field_names"]),"complete scientific field set")
            check(result["failure"] is None and result["current_target"] is None,"complete successful scientific state")
            check(all(x.get("passed") is True for x in result["gates"])
                  and [x["name"] for x in result["gates"]]==op["complete_gate_names"],"complete actual gates")
            check(len(target_names) in op["complete_target_counts"],"complete scientific target count")
        return result

    try:
        head=pull()
        if git("cat-file","-e",head+":"+marker_relative,check_return=False).returncode==0:
            prior=parse(git("show",head+":"+marker_relative,binary=True).stdout)
            check(prior.get("problem_id")==manifest["problem_id"],"unexpected consumed-marker owner")
            print("This precise scientific target already has a persistent consumed marker. No scientific child is allowed.",flush=True)
            print(json.dumps(prior,sort_keys=True),flush=True)
            return
        materialize(head)
        cap,_=capacity(head)
        pending=concurrent_pending_reservations()
        cap["concurrent_pending_publications"]=pending
        state["pre_execution_capacity"]=cap
        check(cap["topic_blob_bytes"]+op["maximum_total_publication_bytes"]+
              pending["reserved_bytes"]+RESERVE<=LIMIT,
              "full publication, concurrent pending outputs and reserve before science")
        native_args=restore()
        command=[sys.executable,str(root/manifest["scientific_modules"][0]["path"]),
                 "--repo",str(root),"--manifest",str(mpath),"--manifest-sha",args.manifest_sha,
                 "--bits",str(manifest["parameters"][op.get("bits_parameter","bits")]),"--out",str(output),*native_args]
        state["actual_scientific_checkout"]=git("rev-parse","HEAD").stdout.strip()
        preflight=subprocess.run([*command,"--preflight-only"],cwd=root,env=child_environment(),capture_output=True)
        state["readonly_preflight"]={"returncode":preflight.returncode,
             "stdout_bytes":len(preflight.stdout),"stdout_sha256":sha(preflight.stdout),
             "stderr_bytes":len(preflight.stderr),"stderr_sha256":sha(preflight.stderr)}
        print(preflight.stdout.decode("utf-8"),end="",flush=True)
        print(preflight.stderr.decode("utf-8"),end="",flush=True)
        if preflight.returncode:
            state["readonly_preflight"]["complete_stdout_utf8"]=preflight.stdout.decode("utf-8")
            state["readonly_preflight"]["complete_stderr_utf8"]=preflight.stderr.decode("utf-8")
        check(preflight.returncode==0,"complete readonly preflight failed before science")
        state["readonly_preflight"]["complete_output"]=parse(preflight.stdout)
        if op.get("readonly_diagnostic_only",False):
            check(state["scientific_children"]==0 and not science_started,
                  "successful diagnostic has no scientific child or consumed marker")
            raise ReadonlyCompleted()
        marker={"kind":"consumed_new_scientific_target_v1","problem_id":manifest["problem_id"],
                "manifest_sha256":args.manifest_sha,"run_id":run,"run_attempt":attempt,
                "event_commit":os.environ["GITHUB_SHA"],"prepared_utc":utc(),
                "status":"readonly_preflight_passed_new_child_reserved",
                "output_directory":output_relative,"old_completed_targets_may_be_recomputed":False,
                "only_explicit_remaining_target_contract_can_continue_after_failure":True}
        marked=publish({marker_relative:encode(marker)},"visible-exact: reserve one new "+manifest["problem_id"],4000)
        state["consumed_marker_publication"]=marked
        head=pull()
        materialize(head)
        state["actual_scientific_checkout"]=head
        cap,_=capacity(head)
        pending=concurrent_pending_reservations()
        cap["concurrent_pending_publications"]=pending
        state["immediate_pre_science_capacity"]=cap
        check(cap["topic_blob_bytes"]+op["maximum_total_publication_bytes"]+
              pending["reserved_bytes"]+RESERVE<=LIMIT,
              "fresh full output, concurrent pending outputs and reserve immediately before child")
        state["scientific_started_utc"]=utc()
        state["scientific_children"]=1
        science_started=True
        log=temporary/"new-scientific-child.stdout.log"
        began=time.monotonic()
        p=subprocess.Popen(command,cwd=root,env=child_environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        selector=selectors.DefaultSelector()
        selector.register(p.stdout,selectors.EVENT_READ)
        decoder=codecs.getincrementaldecoder("utf-8")()
        timed_out=False
        periodic_rule_error=None
        next_rules_pull=time.monotonic()+1800
        with log.open("wb") as stream:
            while selector.get_map():
                if p.poll() is None and periodic_rule_error is None and time.monotonic()>=next_rules_pull:
                    try:
                        pull()
                    except BaseException as rules_error:
                        periodic_rule_error=rules_error
                        print("Periodic pull or README check failed; preserve the exact child prefix.",flush=True)
                        traceback.print_exc()
                        if p.poll() is None:
                            p.kill()
                    next_rules_pull=time.monotonic()+1800
                if time.monotonic()-began>op["child_timeout_seconds"] and p.poll() is None:
                    p.kill()
                    timed_out=True
                for key,_ in selector.select(timeout=1):
                    chunk=os.read(key.fd,65536)
                    if not chunk:
                        selector.unregister(key.fileobj)
                        continue
                    stream.write(chunk)
                    stream.flush()
                    sys.stdout.write(decoder.decode(chunk))
                    sys.stdout.flush()
            sys.stdout.write(decoder.decode(b"",final=True))
            sys.stdout.flush()
        selector.close()
        state["actual_child_returncode"]=p.wait()
        state["child_wall_seconds"]=time.monotonic()-began
        state["child_timeout"]=timed_out
        state["scientific_finished_utc"]=utc()
        raw_log=log.read_bytes()
        state["complete_child_stdout"]={"bytes":len(raw_log),"sha256":sha(raw_log),
               "body_not_published_or_split":True}
        if output.is_file():
            raw=output.read_bytes()
            staged_files[output_relative+"/"+result_name]=raw
            result=validate_scientific(raw)
        if periodic_rule_error is not None:
            raise periodic_rule_error
        check(state["actual_child_returncode"]==0 and not timed_out,"unique scientific child failed")
        check(result is not None and result["complete"] is True,"complete scientific conclusion absent")
        state["scientific_complete"]=True
    except ReadonlyCompleted:
        state["readonly_diagnostic_complete"]=True
        state["scientific_complete"]=False
        check(state["failure"] is None and state["scientific_children"]==0
              and not science_started and not output.exists(),
              "complete pure diagnostic without a mathematical output")
    except BaseException as error:
        full_traceback=traceback.format_exc()
        print(full_traceback,flush=True)
        error_type,cut_type=bounded_operation_text(type(error).__name__,64)
        error_message,cut_message=bounded_operation_text(str(error),1000)
        error_traceback,cut_traceback=bounded_operation_text(full_traceback,2048)
        state["failure"]={"type":error_type,"message":error_message,"traceback":error_traceback,
             "text_truncated":bool(cut_type or cut_message or cut_traceback),
             "full_text_in_job_log":True}
        state["scientific_complete"]=False
        if output.is_file():
            staged_files[output_relative+"/"+result_name]=output.read_bytes()
            try:
                result=parse(output.read_bytes())
            except Exception:
                result=None
    state["finished_utc"]=utc()
    state["scientific_started"]=science_started
    state["completed_target_names"]=(result or {}).get("completed_targets",[])
    state["interrupted_target"]=(result or {}).get("current_target")
    state["original_scientific_complete_flag"]=(result or {}).get("complete")
    state["original_scientific_failure"]=(result or {}).get("failure")
    state["scientific_files"]=[{"path":path,"bytes":len(raw),"sha256":sha(raw)}
                                for path,raw in staged_files.items()]
    for path,raw in staged_files.items():
        emit(path,raw)
    while True:
        state["publication_attempts"]+=1
        head=pull()
        cap,sizes=capacity(head)
        state["final_capacity_metadata"]=cap
        body=encode(state)
        report=("# Actual frozen public execution\n\n"
                "Run "+run+"/"+attempt+"; problem "+manifest["problem_id"]+".\n\n"
                "Complete readonly diagnostic: "+str(state["readonly_diagnostic_complete"])+". "
                "Complete scientific outcome: "+str(state["scientific_complete"])+". "
                "Readonly completion does not evaluate a target. "
                "A false sufficient scientific comparison remains a complete outcome.\n\n"
                "New scientific children: "+str(state["scientific_children"])+
                "; old completed targets recomputed: 0.\n\n"
                "Read the complete scientific JSON and execution JSON together. "
                "All independent physical mean, head, finite, metric and nonlinear obligations remain as declared.\n").encode()
        files={**staged_files,output_relative+"/execution.json":body,output_relative+"/report.md":report}
        projected=cap["topic_blob_bytes"]+sum(len(raw)-sizes.get(path,0) for path,raw in files.items())
        check(all(0<len(raw)<100000 for raw in files.values()),"full output must remain small UTF8")
        check(projected<=LIMIT,"actual complete publication exceeds the topic limit")
        check(len(body)<=op["maximum_execution_bytes"],"complete execution budget")
        check(sum(map(len,files.values()))<=op["maximum_total_publication_bytes"],"complete actual publication budget")
        for path,raw in files.items():
            atomic(root/path,raw)
            emit(path,raw)
        git("add","--sparse","--",*files)
        if git("diff","--cached","--quiet",check_return=False).returncode==0:
            break
        git("-c","user.name=github-actions[bot]","-c","user.email=41898282+github-actions[bot]@users.noreply.github.com",
            "commit","-m","visible-exact: preserve complete "+manifest["problem_id"]+" outcome")
        pushed=git("push","origin","HEAD:main",check_return=False)
        if pushed.returncode==0:
            print("Published complete scientific outcome "+git("rev-parse","HEAD").stdout.strip(),flush=True)
            break
        print("Push rejected: immediately pull --rebase and check both READMEs.",flush=True)
        pull()
    if not (state["scientific_complete"] or state["readonly_diagnostic_complete"]):
        raise SystemExit(1)

if __name__=="__main__":
    main()
