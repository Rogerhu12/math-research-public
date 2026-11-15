#!/usr/bin/env python3
"""Restore only pinned historical inputs for complete original197 I2.
Author: Astra-ISP-789f / root. AI-assisted: GPT-6 Astra Pro.
No new arrays are uploaded. Historical artifacts are read, never created.
"""
import argparse,gzip,hashlib,json,os,pathlib,re,resource,subprocess,time,zipfile
REPO="Rogerhu12/math-research-public"
ROOT="topics/invariant-subspace-problem/"
MANIFEST_SHA="a5d9cd78042fcbde42a6cc4fb8c740ce30b4064fb2be60f85b48b8c1db66aeac"
DEADLINE=0
class BudgetStop(Exception):pass
def require(ok,why):
    if not ok:raise RuntimeError(why)
def tick():
    if time.monotonic()>=DEADLINE:raise BudgetStop("Completed-file recovery checkpoint")
def clean(value):
    s=str(value)
    for k in ("GH_TOKEN","GITHUB_TOKEN","GIT_CONFIG_VALUE_0"):
        v=os.environ.get(k)
        if v:s=s.replace(v,"***")
    return s
def identity(path):
    h=hashlib.sha256();n=0
    with pathlib.Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):
            n+=len(b);h.update(b);tick()
    return {"bytes":n,"sha256":h.hexdigest()}
def same(path,pin):
    return pathlib.Path(path).is_file() and identity(path)=={"bytes":pin["bytes"],"sha256":pin["sha256"]}
def command(args,cwd,stdout=None):
    tick()
    try:
        p=subprocess.run(args,cwd=cwd,stdout=stdout if stdout is not None else subprocess.PIPE,
            stderr=subprocess.PIPE,timeout=max(1,min(180,DEADLINE-time.monotonic())))
    except subprocess.TimeoutExpired as e:
        raise BudgetStop("Bounded historical-input operation timed out") from e
    require(p.returncode==0,"Historical-input command failed: "+clean(p.stderr.decode(errors="replace")[-1500:]))
    return p.stdout
def atomic_json(path,obj):
    raw=(json.dumps(obj,sort_keys=True,separators=(",",":"))+"\n").encode()
    require(len(raw)<80000,"Small recovery receipt only")
    tmp=path.with_suffix(path.suffix+".part");tmp.write_bytes(raw);os.replace(tmp,path)
def copy_checked(stream,target,pin):
    temp=target.with_suffix(target.suffix+".part");n=0;h=hashlib.sha256()
    with temp.open("wb") as f:
        while True:
            tick();block=stream.read(1048576)
            if not block:break
            n+=len(block);require(n<=pin["bytes"],"Historical member exceeds exact byte pin")
            h.update(block);f.write(block)
    require(n==pin["bytes"] and h.hexdigest()==pin["sha256"],"Historical member identity mismatch: "+target.name)
    os.replace(temp,target)
def restore(args,receipt):
    raw=pathlib.Path(args.manifest).read_bytes()
    require(hashlib.sha256(raw).hexdigest()==MANIFEST_SHA,"Pinned manifest source bytes")
    manifest=json.loads(raw)
    require(manifest["format"]=="r150-global197-i2-original-input-manifest-v1","Manifest format")
    require(manifest["prime"]==31 and manifest["sourceCount"]==197,"Original197 source family")
    specs={**manifest["files"],**manifest["smallFiles"]}
    require(len(specs)==14,"Exactly fourteen original inputs")
    out=pathlib.Path(args.out);out.mkdir(parents=True,exist_ok=True)
    records={}
    def target_for(key):
        name=specs[key].get("logicalName",key+".bin")
        require(pathlib.PurePosixPath(name).name==name and name not in (".",".."),"Simple temporary input name")
        return out/name
    def record(key,source,reused):
        target=target_for(key)
        require(same(target,specs[key]),"Final exact historical input identity")
        records[key]={"file":target.name,"bytes":specs[key]["bytes"],"sha256":specs[key]["sha256"],
            "source":source,"reused":reused,"temporaryOnly":True}
    ref=manifest["historicalSmallRef"]
    require(re.fullmatch(r"[0-9a-f]{40}",ref) is not None,"Pinned historical commit")
    needed=[key for key in manifest["historicalSmallPaths"] if not same(target_for(key),specs[key])]
    if needed:
        command(["git","fetch","--no-tags","--depth=1","--filter=blob:none","origin",ref],args.repo)
    for key,path in manifest["historicalSmallPaths"].items():
        require(path.startswith(ROOT+"notes/") and ".." not in pathlib.PurePosixPath(path).parts,"Authorized historical topic path")
        target=target_for(key);reused=same(target,specs[key])
        if not reused:
            data=command(["git","show",ref+":"+path],args.repo)
            if "compressedSHA256" in specs[key]:
                require(hashlib.sha256(data).hexdigest()==specs[key]["compressedSHA256"],"Historical compressed identity: "+key)
                data=gzip.decompress(data)
            require(len(data)==specs[key]["bytes"] and hashlib.sha256(data).hexdigest()==specs[key]["sha256"],
                "Historical git input identity: "+key)
            temp=target.with_suffix(target.suffix+".part");temp.write_bytes(data);os.replace(temp,target)
        record(key,{"historicalCommit":ref,"historicalPath":path},reused)
        receipt["parameters"]["files"]=records
        atomic_json(out/"recovery-progress.json",receipt)
    artifacts=[]
    for artifact in manifest["historicalRecoveryLocations"]:
        require(artifact["artifact"] in (14114364261,14118112895),"Only the two paid historical artifacts")
        mapping=[]
        for member in artifact["members"]:
            matches=[key for key,spec in specs.items() if pathlib.PurePosixPath(member).name in spec["aliases"]]
            require(len(matches)==1,"Unique original member-to-input mapping")
            mapping.append((member,matches[0]))
        all_present=all(same(target_for(key),specs[key]) for member,key in mapping)
        archive=out/("historical-"+str(artifact["artifact"])+".zip")
        if not all_present:
            metadata=json.loads(command(["gh","api","repos/"+REPO+"/actions/artifacts/"+str(artifact["artifact"])],args.repo))
            require(metadata["id"]==artifact["artifact"] and metadata["name"]==artifact["artifactName"]
                and metadata["size_in_bytes"]==artifact["bytes"] and not metadata["expired"]
                and metadata["workflow_run"]["id"]==artifact["run"]
                and metadata["digest"]=="sha256:"+artifact["archiveSHA256"],"Actual original artifact metadata")
            pin={"bytes":artifact["bytes"],"sha256":artifact["archiveSHA256"]}
            if not same(archive,pin):
                part=archive.with_suffix(".zip.part")
                with part.open("wb") as output:
                    command(["gh","api","repos/"+REPO+"/actions/artifacts/"+str(artifact["artifact"])+"/zip"],args.repo,output)
                require(same(part,pin),"Whole original archive byte identity")
                os.replace(part,archive)
            with zipfile.ZipFile(archive) as zf:
                for member,key in mapping:
                    target=target_for(key);reused=same(target,specs[key])
                    if not reused:
                        info=zf.getinfo(member)
                        require(not info.is_dir() and info.file_size==specs[key]["bytes"],"Exact original archive member size")
                        with zf.open(info) as stream:copy_checked(stream,target,specs[key])
                    record(key,{"artifact":artifact["artifact"],"run":artifact["run"],"member":member},reused)
                    receipt["parameters"]["files"]=records
                    atomic_json(out/"recovery-progress.json",receipt)
        else:
            for member,key in mapping:record(key,{"artifact":artifact["artifact"],"run":artifact["run"],"member":member},True)
        artifacts.append({"artifact":artifact["artifact"],"run":artifact["run"],"bytes":artifact["bytes"],
            "archiveSHA256":artifact["archiveSHA256"],"selectedMemberCount":len(mapping),
            "allSelectedMembersVerified":True,"allAlreadyPresent":all_present})
        receipt["parameters"]["historicalArtifacts"]=artifacts
        if archive.exists():archive.unlink()
    require(set(records)==set(specs),"All fourteen inputs recovered without substitute")
    receipt["parameters"].update(files=records,all14OriginalInputsVerified=True,
        fullOriginal505FreeAnd315TorsionInputsPresent=True)
    receipt["status"]="completed"
    receipt["outcome"]="fourteen-exact-historical-original197-inputs-temporary-only"
def main():
    global DEADLINE
    parser=argparse.ArgumentParser()
    for name in ("manifest","repo","out"):parser.add_argument("--"+name,required=True)
    parser.add_argument("--remaining-seconds",type=float,default=300)
    parser.add_argument("--memory-mib",type=int,default=2048)
    args=parser.parse_args()
    require(0<args.remaining_seconds<=1200 and 256<=args.memory_mib<=2048,"Explicit recovery budget")
    resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024**2,args.memory_mib*1024**2))
    started=time.monotonic();DEADLINE=started+max(.01,args.remaining_seconds-15)
    out=pathlib.Path(args.out);out.mkdir(parents=True,exist_ok=True)
    receipt={"format":"r150-global197-exact-historical-input-recovery-v1","status":"started",
        "parameters":{"author":"Astra-ISP-789f / root","aiAssisted":"GPT-6 Astra Pro",
            "manifestSHA256":MANIFEST_SHA,"newMathematicsExecuted":False,
            "oldGaussianEliminationRecomputed":False,"releaseAssetsUsedOrCreated":False,
            "newArtifactsCreated":False,"allArraysTemporaryOnly":True,
            "remainingSeconds":args.remaining_seconds,"memoryMiB":args.memory_mib,
            "all14OriginalInputsVerified":False,"files":{}}}
    try:restore(args,receipt)
    except BudgetStop as e:
        receipt["status"]="budget-checkpoint";receipt["parameters"]["stopReason"]=clean(e)
    except Exception as e:
        receipt["status"]="failed";receipt["parameters"]["error"]={"type":type(e).__name__,"message":clean(e)}
    finally:
        receipt["elapsedSeconds"]=time.monotonic()-started
        atomic_json(out/"original-input-recovery-receipt.json",receipt)
        print(json.dumps(receipt,sort_keys=True,separators=(",",":")),flush=True)
    return 0 if receipt["status"]=="completed" else (75 if receipt["status"]=="budget-checkpoint" else 1)
if __name__=="__main__":raise SystemExit(main())
