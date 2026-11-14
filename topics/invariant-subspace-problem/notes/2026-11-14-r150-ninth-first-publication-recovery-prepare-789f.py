#!/usr/bin/env python3
"""Recover three exact completed artifacts and read the real prior push error; no mathematics."""
from __future__ import annotations
import argparse,ast,hashlib,importlib.util,json,os,shutil,stat,sys,urllib.error,urllib.request,zipfile
from pathlib import Path,PurePosixPath
sys.dont_write_bytecode=True
RUN=43638830039
SOURCE="eaa240d96fda143c65a8eccede55b64b87f50ef8"
PREFIX="topics/invariant-subspace-problem/notes/"
PUBLISHER=PREFIX+"2026-11-14-r150-ninth-first-publication-recovery-publish-789f.py"
PREPARE=PREFIX+"2026-11-14-r150-ninth-first-publication-recovery-prepare-789f.py"
WORKFLOW=".github/workflows/invariant-subspace-r150-ninth-first-publication-recovery.yml"
ARTIFACTS=[
 ("results",14130438457,"isp-r150-ninth-first-results-43638830039-1",32103220,"3314b864fd4cb6bf474b4ab934f8cbe062414fd3e31c8ec63f34c00a801592b0"),
 ("recovery",14130842468,"isp-r150-ninth-first-recovery-43638830039-1",32846922,"5ce43eb8fc4ea285c41570abe763b9cce4febbf163c80c25907b420b373ff855"),
 ("prior-publication",14131112175,"isp-r150-ninth-first-publication-43638830039-1",7763,"3841572883147dff2de87086e68c6c261c5e072ab5904dbf0081e982d465ebe7")]
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
 with open(os.environ["GITHUB_ENV"],"a") as stream:stream.write("ISP_NINTH_RECOVERY="+str(out)+"\n")
 request_path=checkout/(PREFIX+"2026-11-14-r150-ninth-first-publication-recovery-request-789f.json")
 request=json.loads(request_path.read_text())
 expected={"format":"r150-ninth-first-publication-recovery-request-v1","original_run_id":RUN,"original_run_attempt":1,
  "original_source_commit":SOURCE,"new_mathematical_stages":False,
  "original_result_directory":PREFIX+"r150-ninth-first-actions-789f/43638830039-1"}
 if any(request.get(k)!=v for k,v in expected.items()):raise ValueError("exact original publication recovery request changed")
 rules={name:sha(checkout/name) for name in ("README.md","topics/invariant-subspace-problem/README.md")}
 if request["rules_sha256"]!=rules:raise ValueError("README changed; root must read/apply the actual diff before publication recovery")
 if set(request["source_sha256"])!={WORKFLOW,PUBLISHER,PREPARE}:raise ValueError("exact three publication recovery source hashes required")
 for name,expected_sha in request["source_sha256"].items():
  if sha(checkout/name)!=expected_sha:raise ValueError("publication recovery source changed "+name)
  if name.endswith(".py"):ast.parse((checkout/name).read_text(),filename=name)
 write(out/"recovery-source.json",{"format":"r150-ninth-first-publication-recovery-initial-v1","status":"prepared",
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
   response=urllib.request.urlopen(location,timeout=120)
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
  write(out/"artifact-recovery.json",{"format":"r150-ninth-first-exact-three-artifact-recovery-v1","newMathematicalStagesExecuted":False,
   "allThreeCompleteZipHashesVerified":len(recovered)==3,"artifacts":recovered})
 results=out/"results";prior=out/"prior-publication"
 spec=importlib.util.spec_from_file_location("r150_publication_error_reader",checkout/PUBLISHER)
 helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
 original_files=[{"file":str(path.relative_to(results)),"bytes":path.stat().st_size,"sha256":sha(path)}
                 for path in sorted(results.rglob("*")) if path.is_file()]
 source=json.loads((results/"actions-source.json").read_text())
 if str(source.get("run_id"))!=str(RUN) or str(source.get("run_attempt"))!="1" or source.get("source_commit")!=SOURCE:raise ValueError("original mathematical source receipt changed")
 math=json.loads((results/"ninth-first-pipeline-receipt.json").read_text())
 if math.get("status")!="completed" or math.get("outcome")!="complete-ninth-first-obstruction-no-compatible-current-source" or math.get("newFirstImageRank")!=0 or math.get("individualTargetCompatible")!=[False]*9 or not math.get("fullF9FirstImageComplete"):raise ValueError("different actual mathematical result; no re-execution authorized")
 old=json.loads((prior/"publication-receipt.json").read_text());log=(prior/"terminal-git.log").read_text()
 last_push=log.rsplit("$ git push ",1)[-1] if "$ git push " in log else log
 diagnosis={"format":"r150-ninth-first-actual-prior-publication-diagnosis-v1","priorPublicationReceipt":old,
  "actualPriorPushErrorClass":helper.classify_push_error(last_push),"actualLastPushSegment":last_push,
  "originalMathematicalRun":RUN,"publicationRecoveryRunId":os.environ["GITHUB_RUN_ID"],"newMathematicalStagesExecuted":False}
 print("ACTUAL_PRIOR_PUBLICATION_RECEIPT",flush=True);print(json.dumps(old,indent=2),flush=True)
 print("ACTUAL_PRIOR_TERMINAL_GIT_LOG_TAIL",flush=True);print("\n".join(log.splitlines()[-160:]),flush=True)
 print(json.dumps({"actualPriorPushErrorClass":diagnosis["actualPriorPushErrorClass"]}),flush=True)
 shutil.copytree(prior,results/"previous-publication",dirs_exist_ok=False)
 write(results/"publication-recovery-diagnosis.json",diagnosis)
 write(results/"publication-recovery-inputs.json",{"format":"r150-ninth-first-original-publication-recovery-inputs-v1",
  "publicationRecoveryRunId":os.environ["GITHUB_RUN_ID"],"publicationRecoveryRunAttempt":os.environ["GITHUB_RUN_ATTEMPT"],
  "publicationRecoverySourceCommit":os.environ["GITHUB_SHA"],"originalMathematicalSource":source,
  "originalResultsFiles":original_files,"artifacts":json.loads((out/"artifact-recovery.json").read_text()),"newMathematicalStagesExecuted":False})
 shutil.copyfile(out/"recovery-source.json",results/"publication-recovery-source.json")
 print(json.dumps({"status":"original-artifacts-recovered-and-prior-error-read","actualPriorPushErrorClass":diagnosis["actualPriorPushErrorClass"],"newMathematicalStagesExecuted":False}),flush=True)
if __name__=="__main__":main()
