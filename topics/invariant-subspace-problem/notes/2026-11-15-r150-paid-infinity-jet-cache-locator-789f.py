#!/usr/bin/env python3
"""Read-only locator for paid R150 infinity first-jet replay inputs.
Only filenames, byte counts and streaming hashes are emitted. Archives are
not extracted, no normal forms are recomputed, and no binary contents print.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time

EXPECTED = {
    "nf-forward.bin": "66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e",
    "nf-backward.bin": "cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f",
    "nf-reduction.bin": "23955e3f69605d307a8a63beef93d776da2eec41305e7ce8977a7fdae210c14e",
    "nf-normal-forms.bin": "aecf6ad7cf1dc15fb07670936c82aabc6cf02d93677717437293195e81b627db",
    "jet-operations.bin": "d2555a117c9f79db448e8eb183d5420952fe001707f5ca81e20e98705b83a3ad",
    "jet-summary.json": "06197081e680a6fbbbf0102632ab514b7f5784f1c505a7a810c7dbb8c8849a5a",
}
SMALL = {"infinity-first-jet-receipt.json", "infinity-first-jet-input.txt"}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--work", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--remaining-seconds", type=float, default=10.0)
    a = p.parse_args()
    if a.remaining_seconds <= 0:
        raise ValueError("Positive remaining shared time required")
    start = time.monotonic()
    deadline = start + a.remaining_seconds
    root = Path(a.work).resolve()
    r = {"format":"r150-paid-infinity-first-jet-cache-locator-v1",
         "status":"started","work":str(root),"files":[],
         "archivesExtracted":False,"normalFormsRecomputed":False,
         "binaryContentsPrinted":False}
    try:
        for path in root.rglob("*"):
            if time.monotonic() >= deadline:
                raise TimeoutError("Locator shared budget exhausted")
            name = path.name
            base = name[:-3] if name.endswith(".gz") else name
            if base not in EXPECTED and base not in SMALL:
                continue
            if not path.is_file():
                continue
            h = hashlib.sha256()
            count = 0
            with path.open("rb") as f:
                for block in iter(lambda:f.read(1<<20),b""):
                    if time.monotonic() >= deadline:
                        raise TimeoutError("Locator hash budget exhausted")
                    count += len(block)
                    h.update(block)
            digest = h.hexdigest()
            r["files"].append({
                "path":str(path),"bytes":count,"sha256":digest,
                "compressed":name.endswith(".gz"),
                "paidRawSHA256":EXPECTED.get(base),
                "matchesPaidRaw":not name.endswith(".gz") and digest == EXPECTED.get(base),
            })
        r["status"] = "completed"
    except BaseException as e:
        r["status"]="incomplete"
        r["error"]=type(e).__name__+": "+str(e)
    r["elapsedSeconds"]=time.monotonic()-start
    out=Path(a.out)
    out.parent.mkdir(parents=True,exist_ok=True)
    r["parameters"]={"files":r["files"],"remainingSeconds":a.remaining_seconds,"expectedPaidRawHashes":EXPECTED}
    data=json.dumps(r,sort_keys=True,indent=2).encode()
    if len(data)>100000:
        raise RuntimeError("Locator small receipt size exceeded")
    tmp=out.with_name(out.name+".tmp")
    tmp.write_bytes(data)
    os.replace(tmp,out)
    print(json.dumps({"status":r["status"],"receipt":str(out),
                      "bytes":len(data),"sha256":hashlib.sha256(data).hexdigest(),
                      "matches":len(r["files"]),"elapsedSeconds":r["elapsedSeconds"]}),
          flush=True)
    if r["status"]!="completed":
        raise SystemExit(2)

if __name__=="__main__":
    main()
