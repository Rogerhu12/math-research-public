#!/usr/bin/env python3
"""Prepare pinned sources or run the new accepted-A node reader, retaining actual outcomes."""
from __future__ import annotations
import argparse, gzip, hashlib, json, os, shutil, subprocess, sys, time
from pathlib import Path
TOPIC = "topics/visible-flex-larger-amplitude"
REV = "869436630c99aa5a68afb55bd8877c826034d117"
MANIFEST_SHA = "7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941"
PREPARE_SHA = "13ee15a05cb0d73487ac217a1b1b1a8fc17f60c7fa54e1bb2fdc84ceb8b0a875"
def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(1048576), b""): h.update(b)
    return h.hexdigest()
def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as f: json.dump(obj, f, indent=2); f.write("\n")
def call(argv, cwd):
    p = subprocess.run(argv, cwd=cwd, check=False)
    if p.returncode: raise RuntimeError("child nonzero " + str(p.returncode) + ": " + repr(argv))
def collect(work, notes, run_rc):
    inventory = []
    for p in sorted(work.rglob("*")):
        if p.is_file():
            inventory.append({"file":p.relative_to(work).as_posix(),
                              "bytes":p.stat().st_size, "sha256":digest(p)})
    index = {"schema":"accepted-A-node-readout-artifact-index-v1",
             "new_readout_wrapper_returncode":run_rc, "files":inventory,
             "scientific_completion_not_inferred_from_inventory":True}
    save(notes / "new-node-readout-artifact-index.json", index)
    for base in ["owned-resource.json", "owned-intent.json", "owned-heartbeat.json"]:
        src = work / base
        if src.exists(): shutil.copyfile(src, notes / base)
    for base in ["owned.log", "nodes/preflight.json"]:
        src = work / base
        if src.exists():
            target = notes / (base.replace("/", "-") + ".gz")
            with src.open("rb") as fi, target.open("xb") as fo:
                with gzip.GzipFile(filename="", mode="wb", fileobj=fo, mtime=0, compresslevel=6) as gz:
                    shutil.copyfileobj(fi, gz)
    complete = work / "nodes/complete.json"
    resource = work / "owned-resource.json"
    if not complete.exists() or not resource.exists():
        save(notes / "new-node-readout-summary.json", {
            "schema":"accepted-A-node-readout-summary-v1","complete":False,
            "wrapper_returncode":run_rc,"complete_json_present":complete.exists(),
            "owned_resource_present":resource.exists(),
            "mathematical_task_complete":False})
        if run_rc == 0: raise RuntimeError("Owned zero requires the complete node file and owned resource")
        return
    c = json.loads(complete.read_text()); r = json.loads(resource.read_text())
    rows = c.get("rows", [])
    all_ok = (run_rc == 0 and r.get("wait4_observed") is True and r.get("exitcode") == 0
              and c.get("finished") is True and c.get("range") == [0,577]
              and c.get("completedNodes") == 577 and len(rows) == 577
              and [x["node"] for x in rows] == list(range(577)))
    radii = [x["geometry"]["r"] for x in rows]
    gaps = [radii[i] - radii[i+1] for i in range(len(radii)-1)]
    summary = {k:v for k,v in c.items() if k not in ["rows","checks"]}
    summary.update(schema="accepted-A-node-readout-summary-v1", complete=all_ok,
        complete_json_sha256=digest(complete), complete_json_bytes=complete.stat().st_size,
        owned_resource_sha256=digest(resource), owned_exitcode=r.get("exitcode"),
        owned_wait4_observed=r.get("wait4_observed"), source_gate_count=len(c.get("checks", [])),
        first_radius=radii[0] if radii else None, last_radius=radii[-1] if radii else None,
        positive_outer_to_inner_gaps=bool(gaps) and all(x>0 for x in gaps),
        minimum_outer_to_inner_gap=min(gaps) if gaps else None,
        first_mean=rows[0]["meanHeightInnerAnchor"] if rows else None,
        last_mean=rows[-1]["meanHeightInnerAnchor"] if rows else None,
        mathematical_task_complete=False,
        big_node_arrays="Retained in the workflow artifact; regenerate from the committed source and request.")
    save(notes / "new-node-readout-summary.json", summary)
    if not all_ok: raise RuntimeError("Complete file does not have the required actual owned zero and whole-node cover")
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--work",type=Path,required=True)
    ap.add_argument("--notes",type=Path,required=True)
    ap.add_argument("--phase",choices=["prepare","readout"],required=True)
    a=ap.parse_args(); repo=a.repo.resolve(); work=a.work.resolve(); notes=a.notes.resolve()
    comp=repo/TOPIC/"computations"; source=work/"sources"
    work.mkdir(parents=True,exist_ok=True); notes.mkdir(parents=True,exist_ok=True)
    manifest=comp/"source-dependencies.json"; prepare=comp/"prepare-source-dependencies.py"
    if digest(manifest)!=MANIFEST_SHA or digest(prepare)!=PREPARE_SHA:
        raise RuntimeError("Pinned source preparation identity changed")
    if a.phase=="prepare":
        if source.exists(): raise FileExistsError(source)
        exists=subprocess.run(["git","cat-file","-e",REV+"^{commit}"],cwd=repo,
                              stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        if exists.returncode:
            call(["git","fetch","--no-tags","--filter=blob:none","--depth","1","origin",REV],repo)
        before=time.monotonic()
        call([sys.executable,str(prepare),"--repo",str(repo),"--dest",str(source),"--manifest",str(manifest)],repo)
        save(notes/"new-node-source-preparation.json",{
            "schema":"accepted-A-node-source-preparation-v1","revision":REV,
            "manifest_sha256":digest(manifest),"prepare_sha256":digest(prepare),
            "seconds":time.monotonic()-before,"new_node_readout_started":False,
            "source_destination":str(source),"preparation_is_not_mathematical_success":True})
        return 0
    argv=[sys.executable,str(comp/"root_actual_A_tail_readout_owned.py"),
          "--prefix",str(work/"owned"),"--timeout-seconds","3600","--rss-limit-kib","393216","--",
          "node","--expose-gc","--max-old-space-size=192",
          str(comp/"root_actual_A_tail_allnodes_firstjet_readout.mjs"),
          "--repo-root",str(repo),"--source-topic",str(source/"topics/visible-flexible-closed-surface"),
          "--first-node","0","--last-node-exclusive","577","--out-dir",str(work/"nodes")]
    code=None
    try:
        code=subprocess.run(argv,cwd=repo,check=False).returncode
    finally:
        collect(work,notes,code)
    return code if code is not None and code>=0 else 1
if __name__=="__main__": raise SystemExit(main())
