#!/usr/bin/env python3
"""Store a complete native certificate in small, SHA-bound gzip parts.

The original bytes, including the original gzip container, are restored.
This changes no numerical record and grants no mathematical conclusion.
Every output is new or is checked to be exactly the requested bytes.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def write_new(path, data):
    path = Path(path)
    if path.exists():
        if path.read_bytes() != data:
            raise FileExistsError(f"different existing bytes: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)


def encode_json(value):
    return (json.dumps(value, indent=2, allow_nan=False) + "\n").encode()


def pack(original, manifest, part_bytes):
    if not 0 < part_bytes <= 3_000_000:
        raise ValueError("each complete byte part must be at most 3 MB")
    original, manifest = Path(original), Path(manifest)
    raw = original.read_bytes()
    doc = json.loads(gzip.decompress(raw) if original.suffix == ".gz" else raw)
    parts = []
    for index, offset in enumerate(range(0, len(raw), part_bytes)):
        data = raw[offset:offset + part_bytes]
        name = manifest.stem + f"-part{index:03d}.bin.gz"
        compressed = gzip.compress(data, compresslevel=9, mtime=0)
        if len(compressed) >= 5_000_000:
            raise ValueError("a native part exceeds the repository file limit")
        write_new(manifest.parent / name, compressed)
        parts.append(dict(file=name, index=index, offset=offset,
                          bytes=len(data), sha256=digest(data),
                          compressed_bytes=len(compressed),
                          compressed_sha256=digest(compressed)))
    result = dict(kind="complete_native_lossless_container_binary_parts_v2",
                  original_file=original.name, original_bytes=len(raw),
                  original_sha256=digest(raw),
                  native_kind=doc.get("kind"), native_complete=doc.get("complete"),
                  native_failure=doc.get("failure"),
                  complete_native_rows=len(doc.get("rows", [])),
                  original_source_sha256=doc.get("source_sha256", doc.get("identity", {}).get("source_sha256")),
                  candidate_sha256=doc.get("candidate_sha256", doc.get("identity", {}).get("candidate_sha256")),
                  parts=parts, no_numerical_record_changed=True,
                  original_container_restored_exactly=True)
    write_new(manifest, encode_json(result))
    return result


def restore(manifest, output):
    manifest, output = Path(manifest), Path(output)
    doc = json.loads(manifest.read_text())
    if doc["kind"] != "complete_native_lossless_container_binary_parts_v2":
        raise ValueError("unexpected native manifest kind")
    data = bytearray()
    for index, part in enumerate(doc["parts"]):
        name = part["file"]
        if Path(name).name != name or part["index"] != index or part["offset"] != len(data):
            raise ValueError("native byte parts are not a complete ordered partition")
        raw = (manifest.parent / name).read_bytes()
        if len(raw) != part["compressed_bytes"] or digest(raw) != part["compressed_sha256"]:
            raise ValueError("a complete compressed native part changed")
        block = gzip.decompress(raw)
        if len(block) != part["bytes"] or digest(block) != part["sha256"]:
            raise ValueError("a complete native byte part changed")
        data.extend(block)
    data = bytes(data)
    if len(data) != doc["original_bytes"] or digest(data) != doc["original_sha256"]:
        raise ValueError("the restored native does not have the original identity")
    write_new(output, data)
    return doc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="operation", required=True)
    p = sub.add_parser("pack")
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--part-bytes", type=int, default=2_000_000)
    p = sub.add_parser("restore")
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.operation == "pack":
        doc = pack(args.input, args.manifest, args.part_bytes)
    else:
        doc = restore(args.manifest, args.out)
    print(json.dumps(dict(operation=args.operation, original_sha256=doc["original_sha256"],
                          original_bytes=doc["original_bytes"], parts=len(doc["parts"]),
                          complete=doc["native_complete"])), flush=True)


if __name__ == "__main__":
    main()
