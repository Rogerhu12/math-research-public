#!/usr/bin/env python3
"""Restore all published early selector maps and the closed run10 queue copy."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
TOPIC = "topics/visible-flex-larger-amplitude"
LEDGER = HERE/"ret100f-early-selector-archive-recovery.json"


def verify(data, identity):
    digest = hashlib.sha256(data).hexdigest()
    git = hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
    if [len(data),digest,git] != identity:
        raise ValueError("Whole file mismatch "+identity[1])
    return data


def compact(raw):
    # A complete JSON string matches the first alternative; its escapes and
    # interior whitespace stay byte-exact. Only JSON structural whitespace falls.
    return re.sub(rb'"(?:\\[\s\S]|[^"\\])*"|[ \n\r\t]+',
                  lambda m: m[0] if m[0].startswith(b'"') else b"", raw)


def restore(out):
    meta = json.loads(LEDGER.read_text("utf8"))
    p, *identity = meta["group"]
    group = verify((HERE.parent/p).read_bytes(),identity)
    sources = []
    for path,commit,*identity in meta["sources"]:
        if subprocess.run(["git","-C",str(HERE),"cat-file","-e",commit+"^{commit}"],
                          stderr=subprocess.DEVNULL).returncode:
            subprocess.run(["git","-C",str(HERE),"fetch","--depth=1","--filter=blob:none",
                            "--no-tags","origin",commit],check=True)
        data = subprocess.check_output(["git","-C",str(HERE),"show",commit+":"+TOPIC+"/"+path])
        sources.append(verify(data, identity))
    for row in meta["rows"]:
        offset,n,digest = row["envelope_span"]
        body = group[offset:offset+n]
        if len(body)!=n or hashlib.sha256(body).hexdigest()!=digest:
            raise ValueError("Unexpected archive envelope")
        for j,(_,i,_,start,count,mode) in enumerate(row["records"]):
            marker = ('{"$ret100f":'+str(j)+'}').encode()
            if body.count(marker) != 1:
                raise ValueError("Missing original selector insertion")
            raw = sources[i][start:start+count]
            if len(raw)!=count or mode not in ("raw","compact"):
                raise ValueError("Invalid original range or recipe")
            body = body.replace(marker, raw if mode=="raw" else compact(raw))
        dest = out/row["path"]
        dest.parent.mkdir(parents=True,exist_ok=True)
        with dest.open("xb") as stream:
            stream.write(verify(body,row["original"]))


if __name__=="__main__":
    restore(Path(sys.argv[1]))
