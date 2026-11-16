#!/usr/bin/env python3
"""Publish one prepared ISP conclusion with real pull/rebase and non-force push."""
from __future__ import annotations
import base64,hashlib,json,os,re,subprocess,sys,time
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError
sys.dont_write_bytecode=True
REPO="Rogerhu12/math-research-public"
ROOT="topics/invariant-subspace-problem/"
RULES=("README.md",ROOT+"README.md")
REQUEST=ROOT+"notes/2026-11-14-root-terminal-publication-request-789f.json"

def main():
    if os.environ.get("GITHUB_REPOSITORY")!=REPO:
        raise ValueError("Only the authorized public repository")
    if not os.environ.get("GITHUB_REF_NAME","").startswith("isp-789f-root-publish-"):
        raise ValueError("Only a prepared root publication branch")
    token=os.environ.get("GH_TOKEN","")
    if not token:
        raise ValueError("Ephemeral Actions credential missing")
    run=os.environ["GITHUB_RUN_ID"]
    attempt=os.environ["GITHUB_RUN_ATTEMPT"]
    source=os.environ["GITHUB_SHA"]
    out=Path(os.environ["RUNNER_TEMP"])/("isp-root-publication-"+run+"-"+attempt)
    out.mkdir(parents=True,exist_ok=True)
    with open(os.environ["GITHUB_ENV"],"a") as f:
        f.write("ISP_ROOTPUB_OUT="+str(out)+"\n")
    request=json.loads(Path(REQUEST).read_text())
    auth=base64.b64encode(("x-access-token:"+token).encode()).decode()
    environment=dict(os.environ)
    environment.update(GIT_CONFIG_COUNT="2",
      GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
      GIT_CONFIG_VALUE_0="AUTHORIZATION: basic "+auth,
      GIT_CONFIG_KEY_1="credential.helper",GIT_CONFIG_VALUE_1="")
    state={"format":"isp-root-real-terminal-publication-v1","status":"preparing",
      "runId":run,"runAttempt":attempt,"sourceCommit":source,
      "branch":os.environ["GITHUB_REF_NAME"],"message":request["message"],
      "pulls":[],"pushes":[],"dispatches":[],"forcePushUsed":False}
    def save():
        (out/"publication-receipt.json").write_text(json.dumps(state,indent=2)+"\n")
    def git(*args,check=True,input_text=None):
        p=subprocess.run(["git",*args],env=environment,capture_output=True,text=True,input=input_text,timeout=180)
        stdout=p.stdout.replace(token,"***").replace(auth,"***")
        stderr=p.stderr.replace(token,"***").replace(auth,"***")
        with (out/"terminal-git.log").open("a") as f:
            f.write("$ git "+" ".join(args)+"\n"+stdout+stderr+"\nexit="+str(p.returncode)+"\n")
        if check and p.returncode:
            raise RuntimeError("git failed: "+" ".join(args[:4]))
        return p.returncode,stdout,stderr
    save()
    try:
        if set(request["rulesGitBlobs"])!=set(RULES):
            raise ValueError("Both exact README rules are required")
        if git("rev-parse","HEAD")[1].strip()!=source:
            raise ValueError("Source commit mismatch")
        parent=git("rev-parse","HEAD^")[1].strip()
        if parent!=request["parentCommit"]:
            raise ValueError("Prepared commit must have the exact reviewed parent")
        changed=git("diff","--name-only","-z",parent,source)[1].split("\0")
        allowed=set(request["allowedPaths"])
        for name in changed:
            if not name:continue
            if name not in allowed or not(name.startswith(ROOT) or name.startswith(".github/workflows/invariant-subspace")):
                raise ValueError("Change outside this prepared ISP conclusion: "+name)
        # Hydrate only this conclusion and its pull receipt; never the whole data tree.
        receipt_path=ROOT+"notes/root-terminal-pulls-789f/"+run+"-"+attempt+".json"
        sparse_paths=sorted(allowed|set(RULES)|{
            ROOT+"HANDOFF.md",REQUEST,
            ROOT+"notes/2026-11-14-root-terminal-publication-789f.py",
            ".github/workflows/invariant-subspace-789f-root-terminal-publication.yml",
            receipt_path})
        if any(not re.fullmatch(r"[A-Za-z0-9_./-]+",name)
               or name.startswith("/") or ".." in name.split("/") for name in sparse_paths):
            raise ValueError("Exact bounded publication paths required")
        git("sparse-checkout","set","--no-cone","--stdin",
            input_text="".join("/"+name+"\n" for name in sparse_paths))
        state["exactSparsePaths"]=sparse_paths
        state["wholeTopicCheckoutUsed"]=False
        save()
        if git("status","--porcelain")[1].strip():
            raise ValueError("Prepared checkout must be clean")
        git("switch","-c","isp-root-terminal-"+run+"-"+attempt)
        git("config","user.name","github-actions[bot]")
        git("config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
        last_read=parent
        while True:
            code,stdout,stderr=git("pull","--rebase","origin","main",check=False)
            origin=git("rev-parse","origin/main")[1].strip()
            diff=git("diff",last_read,origin,"--",*RULES)[1]
            blobs={p:git("rev-parse",origin+":"+p)[1].strip() for p in RULES}
            utc=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            receipt={"format":"isp-789f-actual-actions-pull-v1",
              "remoteCommit":origin,"beforeCommit":last_read,"utc":utc,
              "actualPullRebaseSucceeded":code==0,
              "rulesUnchanged":not diff and blobs==request["rulesGitBlobs"],
              "rulesGitBlobs":blobs,"executionEnvironment":"GitHubActions",
              "runId":run,"runAttempt":attempt,
              "workflowURL":"https://github.com/"+REPO+"/actions/runs/"+run}
            state["pulls"].append(receipt)
            last_read=origin
            (out/("readme-diff-"+str(len(state["pulls"]))+".patch")).write_text(diff)
            save()
            print("ISP_PULL_RECEIPT "+json.dumps(receipt),flush=True)
            if not receipt["rulesUnchanged"]:
                state["status"]="stopped-readme-change";save()
                print("ISP_RULE_DIFF_BEGIN\n"+diff+"\nISP_RULE_DIFF_END",flush=True)
                raise RuntimeError("Root must read and apply this actual README difference")
            if code:
                state["status"]="stopped-pull-rebase-error";save()
                raise RuntimeError("Actual pull/rebase failed; prepared branch remains preserved")
            receipt_path=ROOT+"notes/root-terminal-pulls-789f/"+run+"-"+attempt+".json"
            Path(receipt_path).parent.mkdir(parents=True,exist_ok=True)
            Path(receipt_path).write_text(json.dumps({"sourceCommit":source,"pulls":state["pulls"]},indent=2)+"\n")
            handoff=Path(ROOT+"HANDOFF.md")
            body=handoff.read_text()
            line="- **最近成功实际 pull 与已读规则提交：** "+origin+"（"+utc+"，Actions run"+run+"实际pull --rebase成功，两README无差异）。记录："+receipt_path[len(ROOT):]+"。"
            body,count=re.subn(r"^- \*\*最近成功实际 pull 与已读规则提交：\*\*[^\n]*$",line,body,flags=re.M)
            if count!=1 or len(body.encode())>10000:
                raise ValueError("HANDOFF pull record or byte limit")
            handoff.write_text(body)
            git("add","--",ROOT+"HANDOFF.md",receipt_path)
            git("commit","--amend","--no-edit")
            commit=git("rev-parse","HEAD")[1].strip()
            code,stdout,stderr=git("push","origin","HEAD:refs/heads/main",check=False)
            state["pushes"].append({"commit":commit,"exitCode":code})
            save()
            if code==0:
                state.update(status="pushed",publishedCommit=commit,lastRulesReadCommit=origin)
                save()
                break
            text=(stdout+stderr).lower()
            if (any(term in text for term in ("non-fast-forward","fetch first","[rejected]"))
                or ("cannot lock ref" in text and " is at " in text and " expected " in text)
                or ("[remote rejected]" in text and "failed to update ref" in text)):
                continue
            print("ISP_PUSH_FAILURE "+json.dumps({"exitCode":code,"stdout":stdout[-3000:],"stderr":stderr[-5000:]}),flush=True)
            raise RuntimeError("Non-rejection push failure; actual prepared changes retained")
        for workflow in request.get("dispatchWorkflows",[]):
            if not re.fullmatch(r"invariant-subspace[-a-z0-9]+\.yml",workflow):
                raise ValueError("Dispatch outside the authorized ISP workflow prefix")
            endpoint="https://api.github.com/repos/"+REPO+"/actions/workflows/"+workflow+"/dispatches"
            payload=json.dumps({"ref":"main"}).encode()
            req=Request(endpoint,data=payload,method="POST",
              headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json",
                       "X-GitHub-Api-Version":"2022-11-28","Content-Type":"application/json"})
            for registration_attempt in range(1,13):
                try:
                    with urlopen(req,timeout=60) as response:
                        status=response.status
                    break
                except HTTPError as dispatch_error:
                    if dispatch_error.code not in (404,409,422) or registration_attempt==12:
                        raise
                    time.sleep(2)
            state["dispatches"].append({"workflow":workflow,"ref":"main","httpStatus":status,
                                       "registrationAttempts":registration_attempt})
            save()
        print("ISP_ROOT_PUBLICATION "+json.dumps({k:state.get(k) for k in
          ("status","sourceCommit","publishedCommit","runId","runAttempt","lastRulesReadCommit","dispatches")}),flush=True)
    except Exception as error:
        state["errorType"]=type(error).__name__
        state["error"]=str(error)
        if state["status"] not in ("stopped-readme-change","stopped-pull-rebase-error"):
            state["status"]="publication-failed" if not state.get("publishedCommit") else "pushed-dispatch-incomplete"
        save()
        print("ISP_ROOT_PUBLICATION "+json.dumps({k:state.get(k) for k in
          ("status","sourceCommit","publishedCommit","runId","runAttempt","lastRulesReadCommit","error")}),flush=True)
        raise
if __name__=="__main__":
    main()
