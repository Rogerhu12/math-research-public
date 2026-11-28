#!/usr/bin/env python3
"""Regenerate the six exact retired branch parameter publications, without a solver.

Run from a repository checkout containing the ledger and residual metadata.
A partial Git clone may fetch the named immutable queue blob. The original
derived ready file is not read. Use a scratch output directory.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
TOPIC = "topics/visible-flex-larger-amplitude"
LEDGER = HERE / "ret100c-old-branch-science-publications.json"


def identity(data):
    header = b"blob " + str(len(data)).encode() + b"\0"
    return [len(data), hashlib.sha256(data).hexdigest(), hashlib.sha1(header+data).hexdigest()]


def recover(out):
    meta = json.loads(LEDGER.read_text("utf-8"))
    root = HERE.parent
    marker = meta["placeholder"].encode()
    for row in meta["rows"]:
        envelope = (root/row["envelope_path"]).read_bytes()
        if identity(envelope) != row["envelope"]:
            raise ValueError("retained complete envelope differs: "+row["path"])
        queue = subprocess.check_output(
            ["git","-C",str(root),"show",meta["source_commit"]+":"+TOPIC+"/"+row["queue_path"]])
        if identity(queue) != row["queue"]:
            raise ValueError("source queue differs: "+row["queue_path"])
        start, size, digest = row["source_span"]
        step = queue[start:start+size]
        if len(step) != size or hashlib.sha256(step).hexdigest() != digest:
            raise ValueError("complete source step differs: "+row["pointer"])
        h = row["placeholder_offset"]
        if envelope[h:h+len(marker)] != marker or envelope.count(marker) != 1:
            raise ValueError("invalid documentary insertion address")
        data = envelope[:h]+step+envelope[h+len(marker):]
        if identity(data) != row["original"]:
            raise ValueError("regenerated whole differs: "+row["path"])
        dest = out/row["path"]
        dest.parent.mkdir(parents=True,exist_ok=True)
        with dest.open("xb") as f:
            f.write(data)


if __name__ == "__main__":
    recover(Path(sys.argv[1]))
