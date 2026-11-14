#!/usr/bin/env python3
"""Preserve an actual completed CI mixed report without tool-side binary IO."""
from __future__ import annotations
import argparse,gzip,hashlib,json,shutil
from pathlib import Path
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--artifact",type=Path,default=Path("ci-output/recovered"))
    p.add_argument("--budget",type=Path,default=Path("ci-output/actual-direct-canonical-source-budget.json"))
    p.add_argument("--run-id",required=True);a=p.parse_args()
    reports=list(a.artifact.rglob("actual-canonical-mixed-recovery-complete.json.gz"))
    summaries=list(a.artifact.rglob("actual-canonical-mixed-recovery-complete.summary.json"))
    if len(reports)!=1 or len(summaries)!=1:raise ValueError("actual completed artifact is ambiguous")
    report=reports[0];sm=json.loads(summaries[0].read_text())
    if not sm["proved"] or sm["actual_cells"]!=178 or sha(report)!=sm["full_report_sha256"]:
        raise ValueError("actual completed report identity is false")
    with gzip.open(report,"rt") as f:d=json.load(f)
    if not d["proved"] or len(d["cells"])!=178 or d["failed_cells"]:
        raise ValueError("actual full cover was not completed")
    source=Path("scripts/fourfold_phase_canonical_collar_bivariate_recovery.py")
    if sha(source)!=d["source_sha256"] or sha(source)!=sm["native_source_sha256"]:
        raise ValueError("mathematical mixed source changed")
    out=Path("notes");out.mkdir(exist_ok=True)
    folder=out/"2026-11-12-canonical-mixed-recovery-complete-parts";folder.mkdir(exist_ok=True)
    chunks=[];payload=report.read_bytes()
    for i,left in enumerate(range(0,len(payload),4000000)):
        path=folder/f"part-{i:03d}.bin";path.write_bytes(payload[left:left+4000000])
        chunks.append(dict(path=str(path),bytes=path.stat().st_size,sha256=sha(path)))
    manifest=dict(kind="exact_binary_reassembly_of_actually_completed_mixed_report",proved=True,
        full_report_sha256=sha(report),full_report_bytes=len(payload),parts=chunks,
        actual_cells=178,native_source_sha256=d["source_sha256"],
        reassembly_source_sha256=sha("scripts/fourfold_phase_canonical_mixed_reassemble.py"),
        actual_object=d["actual_object"],root_certificate_sha256=d["root_certificate_sha256"],
        original_compute_run_id="43300408666",original_artifact_id=13981612102,
        preservation_run_id=a.run_id,scope="Exact artifact bytes; no interval data reconstructed from summaries.")
    mp=folder/"manifest.json";mp.write_text(json.dumps(manifest,indent=2)+"\n")
    sm["exact_reassembly_manifest"]=str(mp);sm["exact_reassembly_manifest_sha256"]=sha(mp)
    sm["preservation_run_id"]=a.run_id
    sp=out/"2026-11-12-ci-canonical-mixed-recovery-summary.json"
    sp.write_text(json.dumps(sm,indent=2)+"\n")
    budget=json.loads(a.budget.read_text())
    if not budget["proved"] or budget["actual_cells"]!=178:raise ValueError("R96 aggregation incomplete")
    bp=out/"2026-11-12-actual-direct-canonical-source-budget.json"
    shutil.copyfile(a.budget,bp)
    small=dict(kind="actual_complete_R96_source_contact_summary",proved=True,
        full_report_path=str(bp),full_report_sha256=sha(bp),source_sha256=budget["source_sha256"],
        input_sha256=budget["input_sha256"],actual_cells=178,
        constants=budget["constants"],all_root_contact=budget["all_root_contact"],
        high_root_contact_table=budget["high_root_contact_table"],
        complete_residual_budgets=[{k:v for k,v in row.items() if k not in ("all_terms","largest_terms")}
                                  for row in budget["complete_residual_budgets"]])
    qp=out/"2026-11-12-ci-direct-canonical-source-summary.json"
    qp.write_text(json.dumps(small,indent=2)+"\n")
    if bp.stat().st_size>1000000:raise ValueError("budget exceeds repository plain-data compression threshold")
    print(json.dumps(dict(proved=True,mixed_summary=str(sp),mixed_summary_sha256=sha(sp),
        R96_summary=str(qp),R96_summary_sha256=sha(qp),parts_manifest=str(mp),
        actual_cells=178)),flush=True)
if __name__=="__main__":main()
