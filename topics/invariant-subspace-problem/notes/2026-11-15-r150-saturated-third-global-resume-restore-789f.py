#!/usr/bin/env python3
"""Reuse one complete actual global checkpoint without rerunning any old local page."""
from __future__ import annotations
import hashlib,json,os,shutil
from pathlib import Path
NOTES=Path("topics/invariant-subspace-problem/notes")
PREFIX="2026-11-15-r150-saturated-third-global-"
def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def save(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(x,indent=2)+"\n")
def main():
 req=json.loads((NOTES/(PREFIX+"resume-request-789f.json")).read_text())
 if req["shared_mathematical_seconds"]!=1200 or req["prior_run_id"]!=43670796654:raise ValueError("Fixed continuation scope")
 for path,digest in req["resume_entry_sha256"].items():
  if sha(Path(path))!=digest:raise ValueError("Frozen continuation entry changed")

 old=Path(os.environ["RUNNER_TEMP"])/"isp-r150-global-resume-recovery-download"
 prior=Path(os.environ["RUNNER_TEMP"])/"isp-r150-global-resume-results-download"
 out=Path(os.environ["ISP_SAT_GLOBAL_OUT"]);new=out/"recovery"
 source=json.loads((prior/"actions-source.json").read_text())
 if str(source["run_id"])!=str(req["prior_run_id"]) or source["source_commit"]!=req["prior_mathematical_source_commit"]:
  raise ValueError("Exact prior mathematical run and source required")
 manifest_path=prior/"recovery-manifest.json"
 if sha(manifest_path)!=req["prior_recovery_manifest_sha256"]:raise ValueError("Exact complete recovery manifest required")
 manifest=json.loads(manifest_path.read_text());records=manifest["files"]
 expected={x["file"] for x in records}
 actual={str(p.relative_to(old)) for p in old.rglob("*") if p.is_file()}
 if actual!=expected:raise ValueError("Complete actual recovery file set required")
 for x in records:
  rel=Path(x["file"])
  if rel.is_absolute() or ".." in rel.parts:raise ValueError("Bounded recovery path")
  p=old/rel
  if p.stat().st_size!=x["bytes"] or sha(p)!=x["sha256"]:raise ValueError("Actual recovery bytes differ: "+str(rel))
 c=json.loads((NOTES/(PREFIX+"contract-789f.json")).read_text())
 found={}
 for key,item in c["inputs"].items():
  q=next((p for p in (old/"inputs").glob(key+".*") if p.is_file() and p.stat().st_size==item["bytes"] and sha(p)==item["sha256"]),None)
  if q is None:raise ValueError("Original frozen input missing from actual checkpoint: "+key)
  found[key]={"file":str(q.relative_to(old)),"bytes":q.stat().st_size,"sha256":item["sha256"]}
 if len(found)!=49:raise ValueError("All49 original frozen inputs required")
 if new.exists():
  if any(new.iterdir()):raise ValueError("New recovery destination must be empty")
  new.rmdir()
 shutil.move(str(old),str(new))
 # Preserve already sealed byte-identical pieces for the runner's own SHA reuse.
 cert=json.loads((prior/"certificate-manifest.json").read_text())
 retained=[]
 for record in cert["files"]:
  for piece in record["parts"]:
   rel=Path(piece["file"])
   if rel.is_absolute() or ".." in rel.parts:raise ValueError("Bounded sealed path")
   p=prior/rel
   if p.stat().st_size!=piece["bytes"] or sha(p)!=piece["sha256"]:raise ValueError("Saved sealed piece differs")
   dst=out/"results"/rel;dst.parent.mkdir(parents=True,exist_ok=True)
   try:os.link(p,dst)
   except OSError:shutil.copyfile(p,dst)
   retained.append(piece["file"])
 shutil.copyfile(prior/"certificate-manifest.json",out/"results/certificate-manifest.json")
 audit={"format":"r150-global-complete-checkpoint-reuse-v1","source_commit":os.environ["GITHUB_SHA"],
  "run_id":os.environ["GITHUB_RUN_ID"],"prior_run_id":req["prior_run_id"],
  "prior_source_commit":req["prior_mathematical_source_commit"],"allOriginal49InputHashesVerified":True,
  "allActualRecoveryFilesVerified":True,"recoveryFiles":len(records),"recoveryBytes":sum(x["bytes"] for x in records),
  "priorRecoveryManifestSHA256":req["prior_recovery_manifest_sha256"],
  "sealedPartsRetained":len(retained),"priorMathematicalStagesAreReusedOnlyAfterRunnerBindingAndOutputChecks":True,
  "oldLocalPagesRecomputed":False,"characteristicZeroIdentityAsserted":False,"inputs":found}
 save(out/"results/actions-actual-resume.json",audit)
 with open(os.environ["GITHUB_ENV"],"a") as f:
  f.write("ISP_SAT_GLOBAL_RESUME_RECOVERY="+str(new)+"\n")
  for scope in ("t96","old200","all198","seven","ninth","second","current","third"):
   f.write("ISP_SAT_GLOBAL_"+scope.upper()+"="+str(new/"inputs")+"\n")
 print(json.dumps({k:v for k,v in audit.items() if k!="inputs"}),flush=True)
if __name__=="__main__":main()
