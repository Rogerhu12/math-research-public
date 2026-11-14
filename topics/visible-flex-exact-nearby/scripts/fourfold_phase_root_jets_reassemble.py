#!/usr/bin/env python3
"""Verify and exactly reconstruct the immutable R83 native gzip report."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path(
        "notes/2026-11-12-R83-native-root-jets-parts/manifest.json"))
    parser.add_argument("--out", type=Path)
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    report = json.loads(args.manifest.read_text())
    if report["kind"] != "exact_binary_split_of_original_gzip":
        raise ValueError("wrong binary archive manifest")
    digest = hashlib.sha256()
    payload = []
    cursor = 0
    for row in report["parts"]:
        path = args.manifest.parent/row["filename"]
        block = path.read_bytes()
        if (row["offset"] != cursor or len(block) != row["bytes"]
                or len(block) >= 5_000_000
                or hashlib.sha256(block).hexdigest() != row["sha256"]):
            raise ValueError("binary archive identity or exact tiling mismatch: "+str(path))
        cursor += len(block)
        digest.update(block)
        payload.append(block)
    if cursor != report["original_bytes"] or digest.hexdigest() != report["original_sha256"]:
        raise ValueError("reassembled bytes differ from the original immutable gzip")
    output = args.out or Path(report["original_relative_path"])
    if not args.verify_only:
        output.parent.mkdir(parents=True, exist_ok=True)
        temporary = output.with_suffix(output.suffix+".reassembly-tmp")
        with temporary.open("wb") as stream:
            for block in payload:
                stream.write(block)
        if hashlib.sha256(temporary.read_bytes()).hexdigest() != report["original_sha256"]:
            temporary.unlink()
            raise ValueError("post-write identity failure")
        temporary.replace(output)
    print(json.dumps({"verified": True, "bytes": cursor, "sha256": digest.hexdigest(),
                      "reassembled": not args.verify_only, "output": str(output)}))


if __name__ == "__main__":
    main()
