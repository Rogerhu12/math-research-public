#!/usr/bin/env python3
"""Stage a source dependency by terminal git; never transmit or recommit payloads."""
import argparse,json,hashlib,subprocess
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument("--repo",required=True);p.add_argument("--ref",required=True)
p.add_argument("--path",required=True);p.add_argument("--output",required=True);a=p.parse_args()
assert a.path.startswith("topics/invariant-subspace-problem/notes/") and ".." not in Path(a.path).parts
def git(*args,check=True):
 r=subprocess.run(["git","-C",a.repo,*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if check and r.returncode:raise RuntimeError("Historical input git operation failed: "+r.stderr.decode("utf-8","replace")[-500:])
 return r
r=git("show",a.ref+":"+a.path,check=False);historical=False
if r.returncode:
 index=git("show",a.ref+":topics/invariant-subspace-problem/notes/2026-11-28-historical-input-provenance-8542.json")
 doc=json.loads(index.stdout);item=doc["files"][a.path];old=doc["sourceCommit"]
 git("fetch","--no-tags","--filter=blob:none","--depth=1","origin",old)
 r=git("show",old+":"+a.path)
 assert len(r.stdout)==item["bytes"] and hashlib.sha256(r.stdout).hexdigest()==item["sha256"]
 historical=True
out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(r.stdout)
print(json.dumps({"dependency":a.path,"stagedInRunnerTemporaryDirectory":True,
                  "historical":historical,"payloadPrintedOrRecommitted":False}),flush=True)
