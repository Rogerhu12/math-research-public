#!/usr/bin/env python3
"""Collect genuine recovered mixed cells with exact source and cover checks."""
from __future__ import annotations
import argparse,copy,glob,gzip,json
from pathlib import Path
from fourfold_phase_canonical_collar_bivariate_recovery import read,sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--parts",default="ci-output/parts/mixed-part-*.json.gz")
    ap.add_argument("--base",type=Path,default=Path(
        "notes/2026-11-12-actual-finite-canonical-collar-centered-cover.json.gz"))
    ap.add_argument("--out",type=Path,default=Path(
        "ci-output/actual-canonical-mixed-recovery-complete.json.gz"))
    args=ap.parse_args()
    base=read(args.base)
    if not base.get("proved") or base["pending"] or base["failed_cells"]:
        raise ValueError("complete original collar required")
    files=sorted(map(Path,glob.glob(args.parts)))
    if not files:raise ValueError("no actual saved pieces")
    pieces=[(path,read(path)) for path in files]
    pieces.sort(key=lambda item:item[1]["first_index"])
    first=pieces[0][1]
    ignored={"proved","covered_specified_cells","first_index","last_index","next_index",
             "cells","failed_cells","seconds"}
    identities={k:v for k,v in first.items() if k not in ignored}
    if first["source_sha256"]!=sha(Path(__file__).with_name(
            "fourfold_phase_canonical_collar_bivariate_recovery.py")):
        raise ValueError("the actual native source changed")
    if first["base_cover_sha256"]!=sha(args.base):
        raise ValueError("the actual base report changed")
    for name,value in first["dependencies"].items():
        if sha(Path(__file__).with_name(name))!=value:
            raise ValueError("actual dependency changed: "+name)
    cursor=0;rows=[];sources=[];seconds=0.0
    for path,part in pieces:
        if {k:v for k,v in part.items() if k not in ignored}!=identities:
            raise ValueError("actual source/configuration mismatch between pieces")
        if (not part.get("covered_specified_cells") or part["failed_cells"]
                or part["first_index"]!=cursor
                or part["next_index"]!=part["last_index"]
                or len(part["cells"])!=part["last_index"]-part["first_index"]):
            raise ValueError("actual pieces do not form a completed exact partition")
        for row in part["cells"]:
            if row["base_index"]!=cursor or row["exact_quarter_interval"]!=base["cells"][cursor]["exact_quarter_interval"]:
                raise ValueError("missing, duplicate, or changed actual angular cell")
            rows.append(row);cursor+=1
        sources.append(dict(path=str(path),sha256=sha(path),
            first_index=part["first_index"],last_index=part["last_index"]))
        seconds+=float(part["seconds"])
    if cursor!=len(base["cells"]):raise ValueError("the full actual cover is incomplete")
    report=copy.deepcopy(first)
    report.update(proved=True,covered_specified_cells=True,first_index=0,last_index=cursor,
        next_index=cursor,cells=rows,failed_cells=[],seconds=seconds,
        collector_source_sha256=sha(__file__),actual_piece_sources=sources)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with gzip.open(args.out,"wt") as f:json.dump(report,f,indent=2);f.write("\n")
    small=dict(kind="actual_recovered_mixed_complete_summary",proved=True,
        full_report_path=str(args.out),full_report_sha256=sha(args.out),
        full_report_bytes=args.out.stat().st_size,actual_cells=cursor,
        collector_source_sha256=sha(__file__),native_source_sha256=first["source_sha256"],
        base_cover_sha256=first["base_cover_sha256"],actual_object=first["actual_object"],
        root_certificate_sha256=first["root_certificate_sha256"],
        retained_native_root_order=40,retained_E_order=39,
        lost_previous_results_reconstructed_from_prose=False,actual_piece_sources=sources)
    summary=args.out.with_suffix("").with_suffix(".summary.json")
    summary.write_text(json.dumps(small,indent=2)+"\n")
    print(json.dumps(small),flush=True)


if __name__=="__main__":main()
