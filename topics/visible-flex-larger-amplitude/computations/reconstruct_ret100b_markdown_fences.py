#!/usr/bin/env python3
"""Reproduce the RET100B documentary whitespace edit from immutable originals.

Run from the repository with an empty scratch output directory. --original
recovers each complete old file for readers expecting its old whole hash.
Without --original, emit the new readable Markdown containing every old word.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

TOPIC = "topics/visible-flex-larger-amplitude"
LEDGER = Path(__file__).with_name("ret100b-historical-note-json-fence-whitespace.json")
OPEN = re.compile(rb"^( {0,3})(`{3,}|~{3,})([^\r\n]*)(?:\r\n|\n|$)$")
WS = b" \t\r\n"


def reject_constant(value):
    raise ValueError("Non-JSON literal " + value)


def compact_body(body):
    if body.lstrip(WS)[:1] not in (b"{", b"["):
        return body, False
    try:
        # Structural recognition only. Discard the parsed object. The original
        # lexical numbers, escaping, duplicate keys and field order are retained.
        json.loads(body.decode("utf-8"), parse_int=str, parse_float=str, parse_constant=reject_constant)
    except (ValueError, UnicodeError):
        return body, False
    out = bytearray()
    quoted = escaped = False
    for byte in body:
        if quoted:
            out.append(byte)
            if escaped:
                escaped = False
            elif byte == 92:
                escaped = True
            elif byte == 34:
                quoted = False
        elif byte == 34:
            quoted = True
            out.append(byte)
        elif byte not in WS:
            out.append(byte)
    out.extend(b"\r\n" if body.endswith(b"\r\n") else b"\n")
    return bytes(out), True


def transform(data):
    lines = re.findall(rb"[^\n]*\n|[^\n]+$", data)
    out = []
    i = 0
    blocks = 0
    while i < len(lines):
        opening = OPEN.fullmatch(lines[i])
        if not opening or (opening[2][:1] == b"`" and b"`" in opening[3]):
            out.append(lines[i])
            i += 1
            continue
        delimiter = opening[2]
        closing = re.compile(rb"^ {0,3}"+delimiter[:1]+b"{"+str(len(delimiter)).encode()+rb",}[ \t]*(?:\r\n|\n|$)$")
        j = i+1
        while j < len(lines) and not closing.fullmatch(lines[j]):
            j += 1
        if j == len(lines):
            out.extend(lines[i:])
            break
        body = b"".join(lines[i+1:j])
        if opening[3].strip().lower() in (b"", b"json"):
            body, valid = compact_body(body)
            blocks += valid
        out.extend((lines[i], body, lines[j]))
        i = j+1
    return b"".join(out), blocks


def identity(data):
    git = b"blob "+str(len(data)).encode()+b"\0"+data
    return [len(data), hashlib.sha256(data).hexdigest(), hashlib.sha1(git).hexdigest()]


def main(outdir, old):
    ledger = json.loads(LEDGER.read_text("utf-8"))
    for path, before, after, count in ledger["rows"]:
        original = subprocess.check_output(["git","show",ledger["base_commit"]+":"+TOPIC+"/"+path])
        if identity(original) != before:
            raise ValueError("Original complete file differs: "+path)
        edited, actual_count = transform(original)
        if identity(edited) != after or actual_count != count:
            raise ValueError("Regenerated complete file differs: "+path)
        dest = outdir/path
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open("xb") as stream:
            stream.write(original if old else edited)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("outdir", type=Path)
    parser.add_argument("--original", action="store_true")
    args = parser.parse_args()
    main(args.outdir, args.original)
