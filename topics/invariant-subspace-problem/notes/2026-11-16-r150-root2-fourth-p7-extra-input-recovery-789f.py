#!/usr/bin/env python3
"""Recover only four true sources and three small original p7 dependencies.
Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
No new mathematics, elimination, artifact upload, or tracked-repository edit.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,re,resource,signal,subprocess,time,zipfile
from pathlib import Path,PurePosixPath

REPOSITORY="Rogerhu12/math-research-public"
TOPIC="topics/invariant-subspace-problem/notes/"
MANIFEST_SHA="16e4bc219a2c77433aec58aae78b574155405537a4efed66be196de2f01a9cf7"
MANIFEST_BYTES=16228
REF="8c6304e273e64b0544d3dd58bc0e48a672a87c36"
FORMAT="r150-root2-fourth-p7-extra-input-recovery-v1"
DEADLINE=0.0
class BudgetStop(Exception):pass
def check(ok,why):
 if not ok:raise ValueError(why)
def tick():
 if time.monotonic()>=DEADLINE:raise BudgetStop("bounded completed-file recovery checkpoint")
def sha(data):return hashlib.sha256(data).hexdigest()
def clean(value):
 s=str(value)
 for key in ("GH_TOKEN","GITHUB_TOKEN","GIT_CONFIG_VALUE_0"):
  secret=os.environ.get(key)
  if secret:s=s.replace(secret,"***")
 return s
def canonical(x):return (json.dumps(x,sort_keys=True,separators=(",",":"))+"\n").encode("ascii")
def atomic_bytes(path,data):
 path.parent.mkdir(parents=True,exist_ok=True)
 tmp=path.with_name(path.name+".part-"+str(os.getpid()))
 with tmp.open("wb") as f:f.write(data);f.flush();os.fsync(f.fileno())
 os.replace(tmp,path)
def atomic_json(path,obj):
 data=canonical(obj);check(len(data)<60000,"small metadata-only recovery receipt")
 atomic_bytes(path,data)
def identity(path):
 digest=hashlib.sha256();size=0
 with path.open("rb") as f:
  for part in iter(lambda:f.read(1048576),b""):
   tick();size+=len(part);digest.update(part)
 return {"bytes":size,"sha256":digest.hexdigest()}
def same(path,pin):
 return path.is_file() and path.stat().st_size==pin["bytes"] and identity(path)=={"bytes":pin["bytes"],"sha256":pin["sha256"]}
def command(argv,repo,stdout=None,cap=240):
 tick()
 try:
  p=subprocess.run(argv,cwd=repo,stdout=subprocess.PIPE if stdout is None else stdout,
    stderr=subprocess.PIPE,timeout=max(.1,min(cap,DEADLINE-time.monotonic())))
 except subprocess.TimeoutExpired as exc:
  raise BudgetStop("historical gh/git subprocess reached the shared deadline") from exc
 if p.returncode:
  raise RuntimeError("historical read failed (exit "+str(p.returncode)+"): "+clean(p.stderr.decode(errors="replace")[-1800:]))
 return p.stdout
def safe_topic(path):
 q=PurePosixPath(path)
 check(path.startswith(TOPIC) and not q.is_absolute() and ".." not in q.parts,"immutable authorized topic path")
 return path
def copy_checked(stream,target,pin):
 target.parent.mkdir(parents=True,exist_ok=True)
 part=target.with_name(target.name+".part-"+str(os.getpid()));h=hashlib.sha256();size=0
 with part.open("wb") as out:
  while True:
   tick();block=stream.read(1048576)
   if not block:break
   size+=len(block);check(size<=pin["bytes"],"selected member exceeds its exact byte pin")
   h.update(block);out.write(block)
  out.flush();os.fsync(out.fileno())
 check(size==pin["bytes"] and h.hexdigest()==pin["sha256"],"selected historical member SHA256")
 os.replace(part,target)

def restore(a,receipt,save):
 raw=a.manifest.read_bytes()
 check(len(raw)==MANIFEST_BYTES and sha(raw)==MANIFEST_SHA,"complete frozen source/input manifest")
 m=json.loads(raw)
 check(m["format"]=="r150-root2-fourth-positive-two-p7-sources-and-inputs-v1","manifest format")
 check(m["prime"]==31 and m["modulus"]==27512614111,"same original p7 interface")
 archives=m["additionalSourceArchives"]
 check([(x["run"],x["artifact"]) for x in archives]==[(43619888599,14124017685),(43630666145,14127663630)],
       "only the two authorized historical true-source archives")
 check(sum(len(x["onlyUniqueSuffixMembers"]) for x in archives)==4,"exactly four extra true-source members")
 original=a.work/"original127-inputs";jet=a.work/"root2-fourth-jet-map"
 sources=a.work/"root2-fourth-true-source-inputs";cache=a.work/"root2-fourth-p7-extra-input-recovery"
 for path in (original,jet,sources,cache):path.mkdir(parents=True,exist_ok=True)
 receipt["binding"]=sha(canonical({"format":FORMAT,"manifestSHA256":MANIFEST_SHA,
    "scriptSHA256":sha(Path(__file__).read_bytes())}))
 entries=receipt["parameters"]["files"];archive_records=receipt["parameters"]["archives"]
 cli=m["suggestedCLI"]
 destinations={"--true-source-dir":"{work}/root2-fourth-true-source-inputs",
  "--exact-gzip":"{work}/original127-inputs/original-primitive-integer-equations.json.gz",
  "--jet-map-dir":"{work}/root2-fourth-jet-map"}
 for flag,expected in destinations.items():
  check(cli[cli.index(flag)+1]==expected,"destinations agree exactly with frozen suggestedCLI")
 ep=m["exactPrimitive"];jm=m["jetMap"]
 check(ep["historicalRef"]==REF and jm["historicalRef"]==REF,"same immutable historical commit")
 records=[("exactPrimitive",safe_topic(ep["historicalPath"]),
           original/"original-primitive-integer-equations.json.gz",ep)]
 check(len(jm["files"])==2,"exactly two quotient-map files")
 for x in jm["files"]:
  check(PurePosixPath(x["file"]).name==x["file"],"simple quotient-map output name")
  records.append((x["file"],safe_topic(jm["historicalDirectory"]+"/"+x["file"]),jet/x["file"],x))
 need_git=any(not same(dest,pin) for _,_,dest,pin in records)
 if need_git:
  probe=subprocess.run(["git","cat-file","-e",REF+"^{commit}"],cwd=a.repo,
     stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=max(.1,min(30,DEADLINE-time.monotonic())))
  if probe.returncode:
   command(["git","fetch","--no-tags","--depth=1","--filter=blob:none","origin",REF],a.repo,cap=120)
 for key,path,dest,pin in records:
  reused=same(dest,pin)
  if not reused:
   data=command(["git","show",REF+":"+path],a.repo,cap=120)
   check(len(data)==pin["bytes"] and sha(data)==pin["sha256"],"exact historical git object "+key)
   if pin.get("blob"):
    actual=hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
    check(actual==pin["blob"],"exact historical git blob "+key)
   atomic_bytes(dest,data)
  check(same(dest,pin),"final historical object identity "+key)
  item={"relativePath":str(dest.relative_to(a.work)),"bytes":pin["bytes"],"sha256":pin["sha256"],
    "historicalRef":REF,"historicalPath":path,"reused":reused,"temporaryOnly":True}
  if key=="exactPrimitive":
   decoded=gzip.decompress(dest.read_bytes())
   check(len(decoded)==ep["payloadBytes"] and sha(decoded)==ep["payloadSHA256"],"exact primitive decompressed identity")
   item.update(payloadBytes=len(decoded),payloadSHA256=sha(decoded),allPayloadBytesVerified=True)
  entries[key]=item;save()
 for spec in archives:
  aid=spec["artifact"];pin={"bytes":spec["bytes"],"sha256":spec["sha256"]}
  metadata=json.loads(command(["gh","api","repos/"+REPOSITORY+"/actions/artifacts/"+str(aid)],a.repo,cap=60))
  check(metadata.get("id")==aid and metadata.get("workflow_run",{}).get("id")==spec["run"]
    and metadata.get("size_in_bytes")==pin["bytes"] and metadata.get("digest")=="sha256:"+pin["sha256"]
    and metadata.get("expired") is False,"actual historical artifact/run/size/digest/expiry")
  members=spec["onlyUniqueSuffixMembers"]
  for member in members:
   check(PurePosixPath(member["output"]).name==member["output"] and member["output"] not in (".",".."),"simple true-source output name")
   suffix=PurePosixPath(member["memberSuffix"])
   check(not suffix.is_absolute() and ".." not in suffix.parts,"safe selected member suffix")
  present={x["output"]:same(sources/x["output"],x) for x in members}
  archive=cache/("historical-"+str(aid)+".zip")
  verified_archive=same(archive,pin)
  selected_names={}
  if not all(present.values()):
   if not verified_archive:
    part=archive.with_name(archive.name+".download-part")
    with part.open("wb") as output:
     command(["gh","api","repos/"+REPOSITORY+"/actions/artifacts/"+str(aid)+"/zip"],a.repo,stdout=output,cap=300)
     output.flush();os.fsync(output.fileno())
    check(same(part,pin),"complete downloaded historical archive SHA256")
    os.replace(part,archive);verified_archive=True
   with zipfile.ZipFile(archive) as z:
    for member in members:
     suffix=member["memberSuffix"]
     matches=[info for info in z.infolist() if not info.is_dir() and
       (info.filename==suffix or info.filename.endswith("/"+suffix))]
     check(len(matches)==1,"unique complete archive member suffix "+suffix)
     info=matches[0]
     check(info.file_size==member["bytes"],"selected original archive member size")
     selected_names[member["output"]]=info.filename
     if not present[member["output"]]:
      with z.open(info) as stream:copy_checked(stream,sources/member["output"],member)
     check(same(sources/member["output"],member),"complete extracted source identity")
     entries[member["output"]]={"relativePath":str((sources/member["output"]).relative_to(a.work)),
       "bytes":member["bytes"],"sha256":member["sha256"],"run":spec["run"],"artifact":aid,
       "uniqueMember":info.filename,"memberSuffix":suffix,"reused":present[member["output"]],"temporaryOnly":True}
     save()
  else:
   for member in members:
    entries[member["output"]]={"relativePath":str((sources/member["output"]).relative_to(a.work)),
      "bytes":member["bytes"],"sha256":member["sha256"],"run":spec["run"],"artifact":aid,
      "memberSuffix":member["memberSuffix"],"reused":True,"temporaryOnly":True}
  archive_records.append({"run":spec["run"],"artifact":aid,"bytes":pin["bytes"],"sha256":pin["sha256"],
    "metadataVerified":True,"selectedMemberCount":len(members),"allSelectedMembersSHA256Verified":True,
    "allAlreadyPresent":all(present.values()),"archiveBytesVerifiedThisRun":verified_archive,
    "onlyUniqueSuffixMembersExtracted":bool(selected_names),"selectedMembers":selected_names})
  save()
  if archive.exists():archive.unlink()
 check(len(entries)==7,"all and only seven requested extra input files")
 for key,path in [("kernels.bin",sources/"kernels.bin"),("fourK2.bin",sources/"fourK2.bin"),
  ("selectedK2.bin",sources/"selectedK2.bin"),("newOriginal.bin",sources/"newOriginal.bin")]:
  check(path.is_file() and identity(path)=={"bytes":entries[key]["bytes"],"sha256":entries[key]["sha256"]},
        "final complete original true-source identity")
 receipt["parameters"].update(allSevenExtraInputsVerified=True,allFourTrueSourceMembersVerified=True,
  exactPrimitivePayloadVerified=True,bothQuotientMapObjectsVerified=True,totalFileBytes=sum(x["bytes"] for x in entries.values()))
 receipt["status"]="completed"
 receipt["outcome"]="seven-exact-extra-inputs-restored-in-temporary-workspace"

def main():
 global DEADLINE
 p=argparse.ArgumentParser()
 for key in ("repo","manifest","work"):p.add_argument("--"+key,type=Path,required=True)
 p.add_argument("--seconds",type=float,default=600);a=p.parse_args()
 check(0<a.seconds<=1800,"explicit bounded recovery time")
 resource.setrlimit(resource.RLIMIT_AS,(1073741824,1073741824))
 a.work.mkdir(parents=True,exist_ok=True);start=time.monotonic();DEADLINE=start+max(.1,a.seconds-5)
 receipt_path=a.work/"root2-fourth-p7-extra-input-recovery-receipt.json"
 rec={"format":FORMAT,"status":"started","parameters":{"manifestBytes":MANIFEST_BYTES,"manifestSHA256":MANIFEST_SHA,
  "author":"ChatGPT (AI), literature_audit","newMathematicsExecuted":False,"oldEliminationRecomputed":False,
  "newArtifactsCreated":False,"repositoryTrackedFilesWritten":False,"allArraysTemporaryOnly":True,
  "executionRunID":os.environ.get("GITHUB_RUN_ID"),"executionRunAttempt":os.environ.get("GITHUB_RUN_ATTEMPT"),
  "seconds":a.seconds,"memoryMiB":1024,"allSevenExtraInputsVerified":False,"files":{},"archives":[]}}
 def save():
  rec["elapsedSeconds"]=time.monotonic()-start;atomic_json(receipt_path,rec)
 def stop(signum,frame):raise BudgetStop("recovery signal "+str(signum))
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 try:restore(a,rec,save);code=0
 except (BudgetStop,subprocess.TimeoutExpired) as exc:
  rec["status"]="budget-checkpoint";rec["errorType"]=type(exc).__name__;rec["error"]=clean(exc);code=75
 except Exception as exc:
  rec["status"]="failed";rec["errorType"]=type(exc).__name__;rec["error"]=clean(exc);code=1
 finally:
  save();print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
 return code
if __name__=="__main__":raise SystemExit(main())
