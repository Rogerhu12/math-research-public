#!/usr/bin/env python3
"""Publish the three complete fitted R781 closed fields and their original terminal geometry reports."""
import argparse
from pathlib import Path

import observe_run48_readme_publications as observer


original_documents = observer.scientific_documents


def circular_documents(value, note):
    records, documents = original_documents(value, note)
    output_root = Path(value["command"][-1])
    for directory in ("inner-grip", "spatial-rings"):
        index = output_root / directory / "closed-geometry-index.json"
        if not index.is_file():
            continue
        file_identity, data = observer.scalar_packet(index)
        key = directory + "-geometry"
        records[key] = {"file": file_identity}
        if data is None:
            records[key]["scope"] = "Whole runner index identity with all separate original stage documents retained."
        else:
            public_path = note[:-5] + "-" + key + ".json"
            records[key]["public_path"] = public_path
            documents[public_path] = data
    return records, documents


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--setup-conclusion", required=True)
    args = parser.parse_args()
    observer.scientific_documents = circular_documents
    return observer.supervise(args.request, args.setup_conclusion)


if __name__ == "__main__":
    raise SystemExit(main())
