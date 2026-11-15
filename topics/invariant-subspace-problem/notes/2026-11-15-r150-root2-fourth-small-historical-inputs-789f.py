#!/usr/bin/env python3
"""Restore six small paid B2/B3 inputs, without restoring the historical chain.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-15.
Only immutable git objects are read; all restored data remain temporary.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,subprocess,sys,time
from pathlib import Path,PurePosixPath
REF="8c6304e273e64b0544d3dd58bc0e48a672a87c36"
PREFIX="topics/invariant-subspace-problem/notes/"
SECOND=PREFIX+"r150-saturated-second-page-actions-789f/43662590949-1"
THIRD=PREFIX+"r150-saturated-third-page-actions-789f/43664532571-1"
RECORDS=[
 ("second-prepared-receipt",SECOND,"prepared-second/prepared-saturated-second-receipt.json",
 18840,"f8ffc939972363e79d0027946c5268c32f869e90adc6fead115fbd29b0ea1ca4"),
 ("second-prepared-system",SECOND,"prepared-second/prepared-saturated-second.bin.gz",
 42012,"691717421b0b7558f7ca053054c6c3f23bde5aa96fc93f36a744ad1171c4ba03"),
 ("second-complete-receipt",SECOND,"complete-second/complete-saturated-second-page-receipt.json",
 22107,"50e8aa0cecafc697b1d52a43792e095be35c4dadc71eff07b861569591d092b7"),
 ("second-complete-system",SECOND,"complete-second/complete-saturated-second.bin.gz",
 72934,"f20487d290193e738a5df67dccdf0c6d11c1c0b9e224dbd310fdc1a0180acaf7"),
 ("third-complete-receipt",THIRD,"complete-third/complete-saturated-third-page-receipt.json",
 17757,"3bb98210ccf8a7941f2a9a71c0d8d1a5fc8c0e11891c26d0e76d8079fa413619"),
 ("third-complete-system",THIRD,"complete-third/complete-saturated-third.bin.gz",
 70591,"786333a4baa562a15e38666a31207e3ce0179e03a0e9505da2d6a4cc5fbe7c2c")]
def check(ok,msg):
 if not ok:raise ValueError(msg)
def sha(data):return hashlib.sha256(data).hexdigest()
def canonical(obj):return json.dumps(obj,sort_keys=True,separators=(",",":")).encode()
def atomic(path,obj):
 q=path.with_name(path.name+".tmp");q.write_bytes(canonical(obj)+b"\n");os.replace(q,path)
def main():
 p=argparse.ArgumentParser();p.add_argument("--repo",type=Path,required=True)
 p.add_argument("--out",type=Path,required=True);a=p.parse_args()
 a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
 result={"format":"r150-root2-fourth-six-small-historical-inputs-v1","status":"running",
  "parameters":{"historicalRef":REF,"author":"Astra-ISP-789f / normal_annihilator",
   "aiAssisted":"GPT-6 Astra Pro","mathematicsRecomputed":False,"largeHistoricalChainRestored":False,
   "allRestoredFilesTemporaryOnly":True},"events":[]}
 def run(cmd,timeout=60):
  z=time.monotonic()
  c=subprocess.run(cmd,cwd=a.repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout)
  result["events"].append({"event":"immutable-git-read","argv":cmd,"exitCode":c.returncode,
                            "elapsedSeconds":time.monotonic()-z})
  check(c.returncode==0,"git read failed: "+c.stderr.decode(errors="replace")[-1000:])
  return c.stdout
 def show(path):
  q=PurePosixPath(path)
  check(not q.is_absolute() and ".." not in q.parts,"safe historical path")
  return run(["git","show",REF+":"+path])
 try:
  probe=subprocess.run(["git","cat-file","-e",REF+"^{commit}"],cwd=a.repo,
                        stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30)
  if probe.returncode:
   run(["git","fetch","--filter=blob:none","--no-tags","origin",REF],timeout=90)
  manifests={};done=[]
  for key,directory,original,size,digest in RECORDS:
   suffix=".json" if key.endswith("receipt") else ".bin.gz"
   dest=a.out/(key+suffix)
   if dest.exists() and len(dest.read_bytes())==size and sha(dest.read_bytes())==digest:
    mode="verified-existing"
   elif key.endswith("receipt"):
    data=show(directory+"/"+original.replace("/","__"))
    check(len(data)==size and sha(data)==digest,"historical exact text identity "+key)
    tmp=dest.with_name(dest.name+".tmp");tmp.write_bytes(data);os.replace(tmp,dest);mode="exact-text"
   else:
    if directory not in manifests:
     raw=show(directory+"/certificate-manifest.json")
     manifests[directory]=(json.loads(raw),sha(raw))
    manifest,manifest_sha=manifests[directory]
    found=[x for x in manifest["files"] if x["originalFile"]==original]
    check(len(found)==1,"unique paid historical binary record "+original)
    record=found[0]
    check(record["uncompressedBytes"]==size and record["uncompressedSHA256"]==digest,
          "historical raw input identity "+key)
    chunks=[]
    for part in record["parts"]:
     data=show(directory+"/"+part["file"])
     check(len(data)==part["bytes"] and sha(data)==part["sha256"],"stored historical part")
     chunks.append(data)
    packed=b"".join(chunks)
    check(len(packed)==record["compressedBytes"] and sha(packed)==record["compressedSHA256"],
          "complete historical storage wrapper")
    data=gzip.decompress(packed)
    check(len(data)==size and sha(data)==digest,"restored exact raw binary "+key)
    tmp=dest.with_name(dest.name+".tmp");tmp.write_bytes(data);os.replace(tmp,dest);mode="exact-wrapper"
   done.append({"key":key,"file":dest.name,"bytes":size,"sha256":digest,"mode":mode,
                "historicalOriginalFile":original,"historicalDirectory":directory})
   result["parameters"]["completedInputs"]=done
   atomic(a.out/"root2-fourth-small-inputs-restore-receipt.json",result)
  result["status"]="completed"
  result["parameters"].update({"allSixExactInputSHA256Verified":True,"inputCount":6,
    "totalRawBytes":sum(x["bytes"] for x in done),
    "certificateManifestSHA256":{k:v[1] for k,v in manifests.items()}})
  rc=0
 except BaseException as e:
  result["status"]="failed";result["errorType"]=type(e).__name__;result["error"]=str(e);rc=1
 result["elapsedSeconds"]=time.monotonic()-start
 atomic(a.out/"root2-fourth-small-inputs-restore-receipt.json",result)
 print(json.dumps({"status":result["status"],"elapsedSeconds":result["elapsedSeconds"],
  "completedInputs":len(result["parameters"].get("completedInputs",[])),"error":result.get("error")}),flush=True)
 return rc
if __name__=="__main__":sys.exit(main())
