#!/usr/bin/env python3
"""Read the pinned small failed receipt; never unpack its large candidate state.
Author: Astra-ISP-789f / root. AI-assisted: GPT-6 Astra Pro.
"""
import argparse,hashlib,json,os,pathlib,resource,time
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument("--receipt",type=pathlib.Path,required=True);p.add_argument("--out",type=pathlib.Path,required=True);a=p.parse_args()
 resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,)*2);start=time.monotonic()
 b=a.receipt.read_bytes()
 if len(b)!=2301 or hashlib.sha256(b).hexdigest()!="b947eb34c7b9b8507689fa9d6560b30fe58268341e65b9be66eafbd21d99d1c0":raise ValueError("actual failed receipt byte identity")
 v=json.loads(b)
 if v.get("status")!="failed" or not isinstance(v.get("error"),dict):raise ValueError("actual structured failure required")
 out={"format":"r150-localized-row-module-small-error-inspection-v1","status":"completed","originalStatus":v["status"],"originalErrorType":v["error"].get("type"),"originalErrorMessage":v["error"].get("message"),"parameters":{"receiptBytes":len(b),"receiptSHA256":hashlib.sha256(b).hexdigest(),"originalBinding":v["binding"],"originalError":v["error"],"largeCandidateStateRead":False,"newMatrixOperations":False,"originalElapsedSeconds":v["elapsedSeconds"],"checkpointManifest":v["parameters"]["checkpointManifest"]},"elapsedSeconds":time.monotonic()-start}
 a.out.parent.mkdir(parents=True,exist_ok=True);raw=json.dumps(out,sort_keys=True,indent=2).encode()+b"\n";tmp=a.out.with_name(a.out.name+".partial");tmp.write_bytes(raw);os.replace(tmp,a.out);print(json.dumps(out,sort_keys=True),flush=True)
if __name__=="__main__":main()
