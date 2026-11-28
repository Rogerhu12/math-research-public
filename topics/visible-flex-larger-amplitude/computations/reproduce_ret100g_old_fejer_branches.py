#!/usr/bin/env python3
"""Restore the complete eleven closed publications into a supplied scratch tree."""
from hashlib import sha1, sha256
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
TOPIC = "topics/visible-flex-larger-amplitude"
LEDGER = HERE/"ret100g-old-fejer-branch-recovery.json"


def checked(data, spec):
    h=sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
    if [len(data),sha256(data).hexdigest(),h]!=spec:
        raise ValueError("whole original identity differs: "+str(spec))
    return data


def generate(destination):
    index=json.loads(LEDGER.read_bytes())
    sources=[]
    for path,commit,n,hash256,blob in index["independent_sources"]:
        data=subprocess.check_output(["git","show",commit+":"+TOPIC+"/"+path],cwd=HERE)
        sources.append(checked(data,[n,hash256,blob]))
    groups={}
    for path,n,hash256,blob in index["envelope_groups"]:
        groups[path]=checked((HERE.parent/path).read_bytes(),[n,hash256,blob])
    for entry in index["retired_publications"]:
        path,n,hash256,blob,group,begin,size,parts=entry
        doc=groups[group][begin:begin+size]
        for j,(target,source,original,start,count) in enumerate(parts):
            marker=('{"$ret100g_whole_original":'+str(j)+'}').encode()
            if doc.count(marker)!=1:
                raise ValueError("missing or duplicate input slot: "+path+" "+target)
            original_bytes=sources[source][start:start+count]
            if len(original_bytes)!=count:
                raise ValueError("original span outside input: "+original)
            doc=doc.replace(marker,original_bytes)
        checked(doc,[n,hash256,blob])
        dest=destination/path
        dest.parent.mkdir(parents=True,exist_ok=True)
        if dest.exists() and dest.read_bytes()!=doc:
            raise ValueError("different output exists: "+str(dest))
        dest.write_bytes(doc)
        print(path,n,hash256,blob)


if __name__=="__main__":
    if len(sys.argv)!=2:
        raise SystemExit("usage: reproduce_ret100g_old_fejer_branches.py SCRATCH_OUTPUT_DIRECTORY")
    generate(Path(sys.argv[1]).resolve())
