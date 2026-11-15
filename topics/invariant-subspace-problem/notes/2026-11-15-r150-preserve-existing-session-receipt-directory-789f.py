#!/usr/bin/env python3
"""Keep the existing run's small receipt directory present across rebases.
Astra-ISP-789f / root; AI-assisted, GPT-6 Astra Pro.
Only a reversible checkout pattern is changed; no repository content is edited.
"""
import argparse,hashlib,json,pathlib,subprocess,time
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=pathlib.Path,required=True)
    ap.add_argument("--out",type=pathlib.Path,required=True)
    a=ap.parse_args()
    start=time.monotonic()
    result={"format":"isp-existing-session-sparse-receipt-preservation-v1","status":"started",
            "largeDataUploadedOrCommitted":False,"parameters":{}}
    def git(args,input=None):
        p=subprocess.run(["git","-C",str(a.repo),*args],input=input,capture_output=True,text=True,timeout=30)
        if p.returncode:raise RuntimeError("checkout operation failed: "+p.stderr[-1000:])
        return p.stdout.strip()
    try:
        before=git(["rev-parse","HEAD"])
        if git(["config","--bool","core.sparseCheckout"])!="true":
            raise RuntimeError("existing sparse checkout required")
        if git(["config","--bool","core.sparseCheckoutCone"])!="false":
            raise RuntimeError("existing non-cone checkout required")
        old=git(["sparse-checkout","list"])
        pattern="/topics/invariant-subspace-problem/notes/r150-infinity-remote-session-789f/"
        git(["sparse-checkout","add","--stdin"],input=pattern+"\n")
        after=git(["sparse-checkout","list"])
        if pattern not in after.splitlines():raise RuntimeError("exact receipt pattern was not retained")
        if git(["rev-parse","HEAD"])!=before or git(["status","--porcelain"]):
            raise RuntimeError("checkout maintenance must preserve HEAD and clean tracked worktree")
        directory=a.repo/"topics/invariant-subspace-problem/notes/r150-infinity-remote-session-789f"
        if not directory.is_dir():raise RuntimeError("actual receipt parent directory absent")
        result.update(status="completed",actualReceiptParentPresent=True,headUnchanged=True,
                      trackedWorktreeClean=True,checkoutPatternOnly=True)
        result["parameters"]={"head":before,"receiptPattern":pattern,
            "beforePatternSHA256":hashlib.sha256(old.encode()).hexdigest(),
            "afterPatternSHA256":hashlib.sha256(after.encode()).hexdigest(),
            "newMathematicsClaimed":False,"noGitContentCommitPerformed":True}
    except BaseException as e:
        result.update(status="failed",error=type(e).__name__+": "+str(e))
        raise
    finally:
        result["elapsedSeconds"]=time.monotonic()-start
        a.out.parent.mkdir(parents=True,exist_ok=True)
        a.out.write_text(json.dumps(result,sort_keys=True,separators=(",",":"))+"\n")
        print(json.dumps(result,sort_keys=True),flush=True)
if __name__=="__main__":
    main()
