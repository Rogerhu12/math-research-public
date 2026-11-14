#!/usr/bin/env python3
"""Recover two exact completed artifact ZIPs and retain all original bytes; no mathematics."""
from __future__ import annotations
import argparse,ast,hashlib,json,os,shutil,stat,urllib.error,urllib.request,zipfile
from pathlib import Path,PurePosixPath
RUN=43648025236
SOURCE="5137a924244d90e6d725ad5436df13296cdb57b0"
PREFIX="topics/invariant-subspace-problem/notes/"
PUBLISHER=PREFIX+"2026-11-14-r150-five-third-target-space-recovery-publish-789f.py"
PREPARE=PREFIX+"2026-11-14-r150-five-third-target-space-recovery-prepare-789f.py"
WORKFLOW=".github/workflows/invariant-subspace-r150-five-third-target-space-recovery.yml"
ARTIFACTS=[
 ("original-output",14134449743,"isp-r150-five-third-target-space-43648025236-1",6668,"5281e3f5bfe6f8418607cb623eac521c9190b338a092d4aa52f3de102f64a1a0"),
 ("prior-publication",14134723893,"isp-r150-five-third-target-space-publication-43648025236-1",2458,"ca238815457d1dcffce07482dddc1ae5d0ca14319d51777bb718ec2a979e86c2")]
def sha(path):
 h=hashlib.sha256()
 with path.open("rb") as stream:
  for block in iter(lambda:stream.read(1048576),b""):h.update(block)
 return h.hexdigest()
def write(path,data):path.write_text(json.dumps(data,indent=2)+"\n")
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,hdrs,newurl):return None
def main():
 p=argparse.ArgumentParser();p.add_argument("--checkout",type=Path,required=True);p.add_argument("--out",type=Path,required=True)
 a=p.parse_args();checkout=a.checkout.resolve();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 if os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":raise ValueError("fixed repository only")
 with open(os.environ["GITHUB_ENV"],"a") as stream:stream.write("ISP_FIVE_SPACE_RECOVERY="+str(out)+"\n")
 request_path=checkout/(PREFIX+"2026-11-14-r150-five-third-target-space-recovery-request-789f.json")
 request=json.loads(request_path.read_text())
 expected={"format":"r150-five-third-target-space-recovery-request-v1","original_run_id":RUN,"original_run_attempt":1,
  "original_source_commit":SOURCE,"new_mathematical_stages":False,
  "original_result_directory":PREFIX+"r150-five-third-actions-789f/43648025236-1"}
 if any(request.get(k)!=v for k,v in expected.items()):raise ValueError("exact original publication recovery request changed")
 rules={name:sha(checkout/name) for name in ("README.md","topics/invariant-subspace-problem/README.md")}
 if request["rules_sha256"]!=rules:raise ValueError("README changed; root must read/apply actual diff before recovery")
 if set(request["source_sha256"])!={WORKFLOW,PUBLISHER,PREPARE}:raise ValueError("exact three publication recovery sources required")
 for name,digest in request["source_sha256"].items():
  if sha(checkout/name)!=digest:raise ValueError("publication recovery source changed "+name)
  if name.endswith(".py"):ast.parse((checkout/name).read_text(),filename=name)
 write(out/"recovery-source.json",{"format":"r150-five-third-target-space-recovery-initial-v1","status":"prepared",
  "publicationRecoveryRunId":os.environ["GITHUB_RUN_ID"],"publicationRecoveryRunAttempt":os.environ["GITHUB_RUN_ATTEMPT"],
  "publicationRecoverySourceCommit":os.environ["GITHUB_SHA"],"newMathematicalStagesExecuted":False,
  "request":request,"requestSHA256":sha(request_path),"rules_sha256":rules})
 token=os.environ["GH_TOKEN"];base="https://api.github.com/repos/Rogerhu12/math-research-public/actions/artifacts/"
 headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"isp-r150-publication-recovery"}
 opener=urllib.request.build_opener(NoRedirect);recovered=[]
 for scope,artifact,name,size,digest in ARTIFACTS:
  with urllib.request.urlopen(urllib.request.Request(base+str(artifact),headers=headers),timeout=60) as response:meta=json.load(response)
  if meta.get("id")!=artifact or meta.get("name")!=name or meta.get("size_in_bytes")!=size or meta.get("digest")!="sha256:"+digest or meta.get("expired") is not False or meta.get("workflow_run",{}).get("id")!=RUN or meta.get("workflow_run",{}).get("head_sha")!=SOURCE:raise ValueError("original artifact metadata differs "+scope)
  try:response=opener.open(urllib.request.Request(base+str(artifact)+"/zip",headers=headers),timeout=60)
  except urllib.error.HTTPError as error:
   if error.code not in (301,302,303,307,308):raise
   location=error.headers["Location"]
   if not location.startswith("https://"):raise ValueError("non-HTTPS artifact redirect")
   response=urllib.request.urlopen(location,timeout=60)
  archive=out/(scope+".zip");h=hashlib.sha256();actual_size=0
  with response,archive.open("wb") as destination:
   for block in iter(lambda:response.read(1048576),b""):
    destination.write(block);h.update(block);actual_size+=len(block)
  if actual_size!=size or h.hexdigest()!=digest:raise ValueError("complete original ZIP differs "+scope)
  destination=out/scope;destination.mkdir(exist_ok=True)
  with zipfile.ZipFile(archive) as zipped:
   for item in zipped.infolist():
    path=PurePosixPath(item.filename)
    if path.is_absolute() or ".." in path.parts or stat.S_ISLNK(item.external_attr>>16):raise ValueError("invalid archive member")
   zipped.extractall(destination)
  recovered.append({"scope":scope,"id":artifact,"name":name,"zipBytes":actual_size,"zipSHA256":h.hexdigest(),"metadata":meta})
  print(json.dumps({k:recovered[-1][k] for k in ("scope","id","zipBytes","zipSHA256")}),flush=True)
  write(out/"artifact-recovery.json",{"format":"r150-five-third-target-space-exact-artifact-recovery-v1",
   "newMathematicalStagesExecuted":False,"allCompleteZipHashesVerified":len(recovered)==2,"artifacts":recovered})
 original=out/"original-output";results=out/"results";recovery=out/"recovery";prior=out/"prior-publication"
 original_files=[{"file":str(path.relative_to(original/"results")),"bytes":path.stat().st_size,"sha256":sha(path)}
                 for path in sorted((original/"results").rglob("*")) if path.is_file()]
 if not original_files:raise ValueError("actual original result files absent")
 shutil.copytree(original/"results",results)
 shutil.copytree(original/"recovery",recovery)
 source=json.loads((results/"actions-source.json").read_text())
 if str(source.get("run_id"))!=str(RUN) or source.get("source_commit")!=SOURCE:raise ValueError("original mathematical source receipt changed")
 math=json.loads((results/"five-third-target-space-receipt.json").read_text())
 outcome=json.loads((results/"actions-outcome.json").read_text())
 if math.get("status")!="completed" or math.get("noNativeMathematicsRecomputed") is not True or outcome.get("complete") is not True:raise ValueError("actual small matrix computation incomplete")
 if sha(results/"five-third-target-space-receipt.json")!=sha(recovery/"five-third-target-space-receipt.json"):raise ValueError("result and recovery copies differ")
 old=json.loads((prior/"publication-receipt.json").read_text());log=(prior/"terminal-git.log").read_text()
 diagnosis={"format":"r150-five-third-target-space-prior-publication-diagnosis-v1","priorPublicationReceipt":old,
  "actualPriorTerminalGitLog":log,"originalMathematicalRun":RUN,"publicationRecoveryRunId":os.environ["GITHUB_RUN_ID"],
  "newMathematicalStagesExecuted":False,"stagingAllowsExactResultPathOutsideSparseCheckout":True}
 print("ACTUAL_PRIOR_PUBLICATION_RECEIPT",flush=True);print(json.dumps(old,indent=2),flush=True)
 print("ACTUAL_PRIOR_TERMINAL_GIT_LOG",flush=True);print(log,flush=True)
 print("ACTUAL_COMPLETE_SMALL_MATRIX_RECEIPT",flush=True);print(json.dumps(math,indent=2),flush=True)
 shutil.copytree(prior,results/"previous-publication",dirs_exist_ok=False)
 write(results/"publication-recovery-diagnosis.json",diagnosis)
 write(results/"publication-recovery-inputs.json",{"format":"r150-five-third-target-space-original-publication-recovery-inputs-v1",
  "publicationRecoveryRunId":os.environ["GITHUB_RUN_ID"],"publicationRecoveryRunAttempt":os.environ["GITHUB_RUN_ATTEMPT"],
  "publicationRecoverySourceCommit":os.environ["GITHUB_SHA"],"originalMathematicalSource":source,
  "originalResultsFiles":original_files,"artifacts":json.loads((out/"artifact-recovery.json").read_text()),"newMathematicalStagesExecuted":False})
 shutil.copyfile(out/"recovery-source.json",results/"publication-recovery-source.json")
 print(json.dumps({"status":"original-artifacts-recovered-and-prior-error-read","newMathematicalStagesExecuted":False}),flush=True)
if __name__=="__main__":main()
