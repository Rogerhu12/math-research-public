#!/usr/bin/env python3
"""Restore four old, generated parameter archive copies from original queues."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
LEDGER = HERE/"ret100d-four-closed-original-queue-archives.json"
TOPIC = "topics/visible-flex-larger-amplitude"


def ident(data):
    return [len(data), hashlib.sha256(data).hexdigest(),
            hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()]


def compact(data):
    quoted = escaped = False
    result = bytearray()
    for b in data:
        if quoted:
            result.append(b)
            if escaped:
                escaped = False
            elif b == 92:
                escaped = True
            elif b == 34:
                quoted = False
        elif b == 34:
            quoted = True
            result.append(b)
        elif b not in b"\r\n\t ":
            result.append(b)
    return bytes(result)+b"\n"


def main(outdir, spell):
    meta = json.loads(LEDGER.read_text("utf-8"))
    for row in meta["rows"]:
        source = subprocess.check_output(["git","-C",str(HERE),"show",
            row["source_commit"]+":"+TOPIC+"/"+row["source_path"]])
        if ident(source) != row["source"]:
            raise ValueError("Original independent fixed queue differs")
        current = source if row["method"]=="whole" else compact(source)
        if ident(current) != row["original"]:
            raise ValueError("Complete published archive differs")
        target = outdir/row["target"]
        target.parent.mkdir(parents=True,exist_ok=True)
        with target.open("xb") as out:
            out.write(source if spell else current)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("outdir",type=Path)
    p.add_argument("--initial-archive-spelling",action="store_true")
    a = p.parse_args()
    main(a.outdir,a.initial_archive_spelling)
