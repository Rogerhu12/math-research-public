"""Extract the true finite old-tail loading of a replacement buffer.

The scaling identity is exact for the linear equation.  The constants here
are maxima over an already computed trajectory, not continuous enclosures.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--count", type=int, default=8)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    report = json.loads(args.report.read_text())
    trajectory = args.report.parent / report["trajectory"]["file"]
    if sha(trajectory) != report["trajectory"]["sha256"]:
        raise ValueError("Existing actual trajectory identity mismatch")
    per_cell, inner = {}, {}
    with gzip.open(trajectory, "rt") as stream:
        for line in stream:
            row = json.loads(line)
            n = row["cell"]
            gamma = row["L"] - 4 * row["H"] * row["w"] / row["r"]
            values = {
                "II": row["linear_shape_operator_row_bound"],
                "Gamma": abs(gamma),
            }
            maxima = per_cell.setdefault(n, {})
            for key, value in values.items():
                if key not in maxima or value > maxima[key]["value"]:
                    maxima[key] = {"value": value, "row": row}
            if row["segment"] == 0 and row["x"] == 0:
                inner[n + 1] = row
    out = []
    for n in range(1, min(args.count, report["far"] - 1) + 1):
        port = inner[n]
        if not port["H"]:
            raise ValueError("Vertical height chart at replacement join")
        maxima = {
            key: max((v[key] for j, v in per_cell.items() if j >= n),
                     key=lambda v: v["value"])
            for key in ("II", "Gamma")
        }
        out.append({
            "replace_outer_cells": n,
            "inner_port": {k: port[k] for k in ("r", "w", "wr", "H", "Hr")},
            "sampled_inner_unit_II": maxima["II"]["value"] / abs(port["H"]),
            "sampled_inner_unit_Gamma": maxima["Gamma"]["value"] / abs(port["H"]),
            "sampled_old_tail_peaks": maxima,
        })
    payload = {
        "schema": "fd2d-finite-tail-inner-loading-v1",
        "source_sha256": sha(__file__),
        "report": {"file": args.report.name, "sha256": sha(args.report)},
        "trajectory": report["trajectory"],
        "config_sha256": report["config_sha256"],
        "scope": "Actual full finite trajectory maxima. They are sampled lower bounds on the continuous supremum, not upper certificates.",
        "identity": "For the same bounded inner linear direction, all linear physical II and Gamma values on the unchanged tail scale by Hnew(inner)/Hold(inner).",
        "objective": "max(localII, gamma*CII, localGamma, gamma*CGamma), gamma=abs(Hinner/Hcut)",
        "rows": out,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "sha256": sha(args.output),
                      "rows": [{k: row[k] for k in
                                ("replace_outer_cells", "sampled_inner_unit_II", "sampled_inner_unit_Gamma")}
                               for row in out]}))


if __name__ == "__main__":
    main()
