#!/usr/bin/env python3
"""Combine two preserved panel files with ten genuinely recomputed files.

This only validates and assembles a material-file manifest.  It neither
reconstructs numerical output from hashes nor changes a source enclosure.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw), raw


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def payload_hash(doc):
    data = {k: v for k, v in doc.items()
            if k not in ("elapsed_seconds", "peak_RSS_KiB")}
    return sha(json.dumps(data, sort_keys=True, separators=(",", ":")).encode())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("original-summary", "fresh-summary", "original-manifest", "out"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh assembled summary")
    old, oldraw = read(args.original_summary)
    fresh, freshraw = read(args.fresh_summary)
    manifest, mraw = read(args.original_manifest)
    if sorted(r["cell"] for r in old["cells"]) != list(range(12, 24)):
        raise ValueError("The archival summary must identify all twelve cells")
    if sorted(r["cell"] for r in fresh["cells"]) != list(range(14, 24)):
        raise ValueError("Fresh execution must have produced exactly cells 14 through 23")
    for field in ("input_hashes", "source_hashes"):
        if old[field] != fresh[field]:
            raise ValueError("The mathematical material definition changed: " + field)
    expected = manifest["mathematical_payload_sha256"]
    rows = [r for r in old["cells"] if r["cell"] in (12, 13)] + fresh["cells"]
    checks = []
    for row in rows:
        path = Path(row["file"])
        doc, raw = read(path)
        if len(raw) != row["bytes"] or sha(raw) != row["sha256"]:
            raise ValueError("A real panel file differs from its execution summary: " + str(path))
        if doc["cell"] != row["cell"]:
            raise ValueError("Cell identity differs from filename entry")
        for field in ("input_hashes", "source_hashes"):
            if doc[field] != old[field]:
                raise ValueError("Panel mathematical identity differs: " + str(path))
        phash = payload_hash(doc)
        if phash != expected[str(row["cell"])]:
            raise ValueError("Fresh mathematical payload differs from the archived payload: " + str(path))
        checks.append(dict(cell=row["cell"], file=str(path),
                           source="preserved" if row["cell"] in (12, 13) else "fresh execution",
                           sha256=sha(raw), mathematical_payload_sha256=phash))
    result = dict(
        status="All twelve actual material files: preserved cells 12/13 plus freshly executed cells 14..23",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        cells=sorted(rows, key=lambda row: row["cell"]),
        total_panels=sum(r["panels"] for r in rows),
        input_hashes=old["input_hashes"], source_hashes=old["source_hashes"],
        provenance=dict(
            original_summary=dict(path=str(args.original_summary), sha256=sha(oldraw)),
            fresh_summary=dict(path=str(args.fresh_summary), sha256=sha(freshraw)),
            original_manifest=dict(path=str(args.original_manifest), sha256=sha(mraw)),
            files=checks,
            no_numerical_data_generated_from_hashes=True,
            payload_hash_rule="Remove only top-level elapsed_seconds and peak_RSS_KiB; sorted compact JSON SHA256"))
    encoded = (json.dumps(result, indent=2) + "\n").encode()
    args.out.write_bytes(encoded)
    print(json.dumps(dict(output=str(args.out), bytes=len(encoded), sha256=sha(encoded),
                          cells=12, preserved_cells=[12, 13], freshly_recomputed_cells=list(range(14, 24)),
                          total_panels=result["total_panels"])), flush=True)


if __name__ == "__main__":
    main()
