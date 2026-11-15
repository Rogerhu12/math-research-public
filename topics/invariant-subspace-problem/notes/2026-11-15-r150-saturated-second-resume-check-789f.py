#!/usr/bin/env python3
"""Validate the actual saved second-page recovery before continuing its cursor."""
import argparse, hashlib, json, os, time
from pathlib import Path
def sha(path):
 h=hashlib.sha256()
 with path.open("rb") as stream:
  while block:=stream.read(1<<20):h.update(block)
 return h.hexdigest()
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--recovery",type=Path,required=True)
 p.add_argument("--results",type=Path,required=True)
 p.add_argument("--request",type=Path,required=True)
 a=p.parse_args();began=time.monotonic();spec=json.loads(a.request.read_text())["resume"]
 root=a.recovery.resolve();prior=Path(spec["previous_result_directory"]).resolve()
 for field,name in (("recovery_manifest_sha256","recovery-manifest.json"),("certificate_manifest_sha256","certificate-manifest.json")):
  if sha(prior/name)!=spec[field]:raise ValueError("Actual paid manifest differs: "+name)
 manifest=json.loads((prior/"recovery-manifest.json").read_text());count=0;total=0
 for entry in manifest["files"]:
  target=(root/entry["file"]).resolve()
  if not target.is_relative_to(root) or not target.is_file() or target.stat().st_size!=entry["bytes"] or sha(target)!=entry["sha256"]:
   raise ValueError("Actual complete recovery differs: "+entry["file"])
  count+=1;total+=entry["bytes"]
 actual={str(q.relative_to(root)) for q in root.rglob("*") if q.is_file()}
 if actual!={x["file"] for x in manifest["files"]}:raise ValueError("Saved recovery file set differs")
 if count!=spec["actual_recovery_files"] or total!=spec["actual_recovery_bytes"]:raise ValueError("Saved recovery size differs")
 for name in spec["completed_stage_names"]:
  cp=root/"stage-cache"/(name+".json")
  cache=json.loads(cp.read_text())
  if not cache.get("inputBindingSHA256") or not cache.get("outputs"):raise ValueError("Completed stage cache missing: "+name)
 result={"status":"completed","sourceRun":spec["run_id"],"sourceCommit":spec["source_commit"],
  "actualRecoveryFiles":count,"actualRecoveryBytes":total,"allSavedRawFileHashesMatched":True,
  "completedStagesToReuse":spec["completed_stage_names"],"continueStage":spec["continue_stage"],
  "priorRawAndCompressedManifestsVerified":True,"noMathematicsRecomputed":True,
  "elapsedSeconds":time.monotonic()-began}
 a.results.mkdir(parents=True,exist_ok=True)
 (a.results/"actual-restored-second-resume.json").write_text(json.dumps(result,indent=2)+"\n")
 print(json.dumps(result),flush=True)
if __name__=="__main__":main()
