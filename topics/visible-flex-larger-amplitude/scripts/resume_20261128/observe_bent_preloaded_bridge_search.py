#!/usr/bin/env python3
"""Publish the complete R770 finite-phase solve, its stage records and its independent even-family terminal geometry."""
import argparse
from pathlib import Path

import observe_bent_shared_rim_search as observer


original_documents = observer.scientific_documents


def bridge_documents(value, note):
    records, documents = original_documents(value, note)
    out = Path(value["command"][-1])
    even_index = out / "even" / "closed-geometry-index.json"
    if even_index.is_file():
        file_identity, data = observer.scalar_packet(even_index)
        key = "even-geometry"
        records[key] = {"file": file_identity}
        if data is None:
            records[key]["scope"] = "Whole runner index identity with the separate original stage documents retained."
        else:
            path = note[:-5] + "-" + key + ".json"
            records[key]["public_path"] = path
            documents[path] = data
    return records, documents


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--setup-conclusion", required=True)
    args = parser.parse_args()
    # The shared supervisor takes one document snapshot per publish, including
    # its checked ordinary Git push. Supply the second scientific index there.
    observer.scientific_documents = bridge_documents
    return observer.supervise(args.request, args.setup_conclusion)


if __name__ == "__main__":
    raise SystemExit(main())
