#!/usr/bin/env python3
"""Permanently preserve missing immutable completed scientific input closures.

No arithmetic result is recomputed. Original files.json, source and report
SHAs are checked by the existing intake. Small original logs included in
that immutable inventory are retained because the unchanged complete-block
validator checks the entire transaction. The large reconstructible reference
cache and already tracked equal files are not duplicated.
"""
from __future__ import annotations
import json, os, time
from pathlib import Path
from fourfold_ci_complete_parameter_flow_v2 import ARTIFACTS, intake, read, sha, save, BLOCKS
from fourfold_ci_inspect_complete_flow_v2 import git


def main():
    started=time.monotonic()
    work=Path("ci-output/scientific-input-archive")
    work.mkdir(parents=True,exist_ok=True)
    proofs=[]
    # The first five density blocks are already permanent in main.
    for spec in ARTIFACTS[5:]:
        proofs.append(intake(spec,work))
    rows={}
    for proof in proofs:
        manifest=Path(proof["block_manifest_path"])
        inventory=Path(proof["inventory_path"])
        doc=read(inventory)
        for row in doc["files"]:
            path=Path(row["path"])
            try:path.relative_to(manifest.parent)
            except ValueError:continue
            if path.stat().st_size!=row["bytes"] or sha(path)!=row["sha256"]:
                raise ValueError("the original completed input changed after intake")
            rows[str(path)]=row
        for path in (manifest,inventory):
            rows[str(path)]=dict(path=str(path),bytes=path.stat().st_size,sha256=sha(path))
    for row in rows.values():
        path=Path(row["path"])
        if row["bytes"]>=5_000_000 or row["bytes"]>1_000_000 and path.suffix!=".gz":
            raise ValueError("a scientific file violates repository compression/size rules")
    inventory_path=Path("notes/2026-11-12-missing-complete-input-archive-files.json.gz")
    save(inventory_path,dict(complete=True,source_sha256=sha(__file__),
        original_artifact_intakes=proofs,files=[rows[k] for k in sorted(rows)],
        no_density_or_ODE_recomputed=True,original_files_preserved_byte_for_byte=True))
    summary_path=Path("notes/2026-11-12-missing-complete-input-archive.json")
    summary=dict(complete=True,source_sha256=sha(__file__),blocks=len(proofs),
        files=len(rows),bytes=sum(row["bytes"] for row in rows.values()),
        inventory_path=str(inventory_path),inventory_sha256=sha(inventory_path),
        no_density_or_ODE_recomputed=True,no_reference_cache_added=True)
    save(summary_path,summary)
    script=Path("scripts/fourfold_ci_archive_missing_inputs_v1.py")
    source=script.read_bytes()
    workspace=Path(os.environ["GITHUB_WORKSPACE"])
    workflow=Path(".github/workflows/visible-exact-input-archive.yml")
    workflow_source=(workspace/workflow).read_bytes()
    git(["fetch","--filter=blob:none","--depth=1","origin","main"])
    base=git(["rev-parse","FETCH_HEAD"]).strip()
    branch="visible-exact-scientific-inputs-"+os.environ["GITHUB_RUN_ID"]
    git(["switch","-c",branch,"FETCH_HEAD"])
    script.write_bytes(source);(workspace/workflow).write_bytes(workflow_source)
    topic=Path("topics/visible-flex-exact-nearby")
    selected=[Path(name) for name in rows]+[inventory_path,summary_path,script]
    # Explicit batches preserve the operating-system argument-length limit.
    paths=[str(topic/path) for path in selected]+[str(workflow)]
    for first in range(0,len(paths),200):
        git(["add","--sparse","--",*paths[first:first+200]])
    git(["-c","user.name=github-actions[bot]",
        "-c","user.email=41898282+github-actions[bot]@users.noreply.github.com",
        "commit","-m","visible-flex: preserve missing original completed scientific input closures"])
    commit=git(["rev-parse","HEAD"]).strip()
    git(["push","origin","HEAD:refs/heads/"+branch])
    summary.update(publication_branch=branch,publication_commit_sha=commit,main_base_sha=base,
        wall_seconds=time.monotonic()-started)
    save(work/"publication.json",summary)
    print("INPUT_ARCHIVE_PUBLICATION",json.dumps(summary),flush=True)


if __name__=="__main__":main()
