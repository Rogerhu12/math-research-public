#!/usr/bin/env python3
"""Reassemble exact completed mixed CI bytes and verify all SHA256 identities."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
def sha(x):return hashlib.sha256(x).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--manifest",type=Path,default=Path(
        "notes/2026-11-12-canonical-mixed-recovery-complete-parts/manifest.json"))
    p.add_argument("--out",type=Path,required=True);a=p.parse_args()
    d=json.loads(a.manifest.read_text());chunks=[]
    for item in d["parts"]:
        data=Path(item["path"]).read_bytes()
        if len(data)!=item["bytes"] or sha(data)!=item["sha256"]:raise ValueError("chunk identity failed")
        chunks.append(data)
    data=b"".join(chunks)
    if len(data)!=d["full_report_bytes"] or sha(data)!=d["full_report_sha256"]:
        raise ValueError("complete actual report identity failed")
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_bytes(data)
    print(json.dumps(dict(verified=True,sha256=sha(data),bytes=len(data))),flush=True)
if __name__=="__main__":main()
