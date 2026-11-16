#!/usr/bin/env python3
"""Read required original public Actions sources; no mathematical core is executed."""
import concurrent.futures
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import tarfile
import traceback

S = Path(__file__).resolve().parent
HELPER = S/"R824_public_original_global_polar_generators.py"
HELPER_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
assert hashlib.sha256(HELPER.read_bytes()).hexdigest() == HELPER_SHA
spec = importlib.util.spec_from_file_location("serre_original_artifact_IO", HELPER)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def shape(value, depth=1):
    if isinstance(value, dict):
        return {k: shape(v, depth-1) if depth else type(v).__name__ for k,v in value.items()}
    if isinstance(value, list):
        return {"type":"list","length":len(value),"first_shape":shape(value[0],depth-1) if value and depth else None}
    return type(value).__name__

def names_in(value, files):
    found = set()
    def visit(v):
        if isinstance(v, str):
            if v in files:
                found.add(v)
        elif isinstance(v, dict):
            for w in v.values():
                visit(w)
        elif isinstance(v, list):
            for w in v:
                visit(w)
    visit(value)
    return found

def bind_manifest(a, out, item):
    rn, mn = "full-outputs-manifest-reference.json", "full-outputs-manifest.json"
    ref, rs = {}, None
    if rn in a.by_name:
        members = a.by_name[rn]
        assert len(members) == 1 and members[0].file_size < 1000000
        raw = a.zip.read(members[0])
        (out/rn).write_bytes(raw)
        ref = json.loads(raw)
        rs = m.file_spec(out/rn)
        if "manifest" in ref:
            ms = m.plain(ref["manifest"])
        elif all(k in ref for k in ("file","bytes","sha256")):
            ms = m.plain(ref)
        else:
            ms = {"file":ref["manifest_file"],"bytes":ref["manifest_bytes"],"sha256":ref["manifest_sha256"]}
    else:
        assert item.get("manifest_sha256") and len(a.by_name[mn]) == 1
        ms = {"file":mn,"bytes":a.by_name[mn][0].file_size,"sha256":item["manifest_sha256"]}
    assert ms["file"] == mn
    if item.get("manifest_sha256"):
        assert ms["sha256"] == item["manifest_sha256"]
    a.extract_bound(mn, ms["sha256"], out/mn, ms["bytes"])
    manifest = m.read(out/mn)
    files = {v["file"]: m.plain(v) for v in manifest["files"]}
    assert len(files) == len(manifest["files"])
    if "file_count" in ref:
        assert ref["file_count"] == len(files)
    assert set(a.by_name) == set(files)|{mn}|({rn} if rs is not None else set())
    for n,row in files.items():
        m.check_spec(row)
        assert len(a.by_name[n]) == 1 and a.by_name[n][0].file_size == row["bytes"]
    return manifest, files, ms, rs

def tar_sources(target, original, names):
    with target.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, compresslevel=2) as zipped:
            with tarfile.open(fileobj=zipped,mode="w|") as tar:
                for name in sorted(names):
                    p = original/name
                    info = tarfile.TarInfo("original/"+name)
                    info.size = p.stat().st_size
                    info.mode,info.mtime,info.uid,info.gid = 0o644,0,0,0
                    with p.open("rb") as stream:
                        tar.addfile(info,stream)

def read_source(row, work, output):
    label,item = row["label"],row["source"]
    root = work/label
    out = root/"original"
    out.mkdir(parents=True,exist_ok=True)
    a = m.Archive(item,root/"transport",whole=False)
    try:
        manifest,fs,ms,rs = bind_manifest(a,out,item)
        def fetch(names):
            a.extract_many([(n,fs[n]["sha256"],out/n,fs[n]["bytes"]) for n in sorted(set(names))])
        metadata = {n for n in fs if n in ("public-actions-input.json","run-receipt.json","core-receipt.json","stage-manifest.json")
                    or (n.endswith("-certificate.json") and fs[n]["bytes"] < 2000000)
                    or ("stage-manifest" in n and fs[n]["bytes"] < 20000000)}
        names = set(metadata)
        mode = row["mode"]
        if mode == "ended":
            names.update(n for n in fs if fs[n]["bytes"] <= 5000000 and
                         (re.search(r"(history|compaction|chart|selection|state|source-audit|receipt|index)",n)
                          or n in ("public-actions-run.log","core.log")))
        elif mode == "R827":
            for wanted in row["files"]:
                assert fs[wanted["file"]] == wanted
                names.add(wanted["file"])
        elif mode == "R800":
            names.add("R800-retained-producer-inputs.tar.gz")
            names.update(n for n in fs if "index" in n and fs[n]["bytes"] < 2000000)
            e1 = {n for n in fs if re.fullmatch(r"R800-original-E1-tail-row-\d{2}\.json\.gz",n)}
            m2 = {n for n in fs if n.startswith("R800-") and "M2-tail" in n and re.search(r"(?:0000|0001|0002|0073)\.json\.gz$",n)}
            assert len(e1) == 82 and len(m2) == 4, (sorted(e1),sorted(m2))
            names.update(e1|m2)
        elif mode == "R799":
            index = "R799-original-power8-basis-index.json.gz"
            assert fs[index]["sha256"] == row["index_sha256"]
            fetch([index])
            value = m.read(out/index)
            basis = value["basis_rows"]
            assert len(basis) == 2050
            leaves = names_in(basis,fs)
            assert len(leaves) == 2050, (len(leaves),shape(basis))
            names.update(leaves|{index})
        elif mode == "R801":
            index = "R801-original-power8-frontier-0193.json.gz"
            assert fs[index]["sha256"] == row["index_sha256"]
            fetch([index])
            value = m.read(out/index)
            basis = value["basis_rows"]
            assert len(basis) == 2050
            leaves = set()
            for record in (basis.values() if isinstance(basis,dict) else basis):
                segments = record["new_tail_segments"]
                chosen = [v for v in segments if int(v["first"]) <= 109 < int(v["stop"])]
                assert len(chosen) == 1
                selected = names_in(chosen[0],fs)
                assert len(selected) == 1
                leaves.update(selected)
            assert len(leaves) == 2050
            names.update(leaves|{index,"R801-original-recipe-dependency-plan.json.gz"})
        else:
            raise AssertionError(mode)
        fetch(names)
        ini,rr = (m.read(out/n) for n in ("public-actions-input.json","run-receipt.json"))
        assert ini["result"] == rr["result"] == manifest["result"]
        assert ini["source_commit"] == rr["source_commit"] == item["source_commit"]
        assert str(rr["workflow_run_id"]) == str(item["run_id"])
        cr = m.read(out/"core-receipt.json") if "core-receipt.json" in names else None
        if cr is not None:
            assert cr["result"] == manifest["result"] and cr["source_sha256"] == ini["core_sha256"]
        if item.get("core_sha256"):
            assert ini["core_sha256"] == item["core_sha256"]
        special = {}
        for n in sorted(names):
            if n.endswith("-certificate.json"):
                value = m.read(out/n)
                special[n] = {k:v for k,v in value.items()
                              if k not in ("configuration","source_inventory","actual_source_inventory")}
            if n in ("dixon-checkpoint-history.json","dixon-output-compaction-receipt.json"):
                v = m.read(out/n)
                if "checkpoints" in v:
                    records = v["checkpoints"]
                    special[n] = {"keys":list(v),"checkpoint_count":len(records),"last_records":records[-8:] if isinstance(records,list) else None}
                else:
                    special[n] = v
        checkpoint_specs = {n:v for n,v in fs.items() if
                            re.search(r"(current|retained.*inputs|input.*bundle|Dixon|dixon|lift|CRT)",n)}
        if len(checkpoint_specs) > 120:
            checkpoint_specs = dict(list(sorted(checkpoint_specs.items()))[-120:])
        logtails = {}
        for n in names:
            if n.endswith(".log"):
                lines = (out/n).read_text(errors="replace").splitlines()
                logtails[n] = [re.sub(r"(?<![A-Za-z0-9_])[0-9]{32,}(?![A-Za-z0-9_])",
                             lambda z:"<"+str(len(z[0]))+"-digit integer omitted>",x)[:1800] for x in lines[-18:]]
        schemas = {}
        if mode == "R827":
            for wanted in row["files"]:
                n=wanted["file"]
                value=m.read(out/n)
                schemas[n]=shape(value,2)
                if "source-audit" in n:
                    special[n]=value
        def compact(v):
            return None if v is None else {k:x for k,x in v.items() if k not in ("configuration","job")}
        keep = set(names)|{"full-outputs-manifest.json"}
        if rs is not None:
            keep.add("full-outputs-manifest-reference.json")
        bundle = output/(label+"-intake-selected-original-sources.tar.gz")
        tar_sources(bundle,out,keep)
        selected = {n:fs[n] for n in sorted(names)}
        summary = {"schema":1,"purpose":"required original source transfer and ended-checkpoint reading only",
          "label":label,"source":item,"original_result":manifest["result"],"manifest":ms,
          "manifest_reference":rs,"original_manifest_count":len(fs),"selected_file_count":len(names),
          "selected_files":selected,"retained_input_bundle":m.file_spec(bundle),
          "source_core_sha256":ini["core_sha256"],"source_wrapper_sha256":ini.get("driver_sha256"),
          "original_readme_sha256":{k:ini.get(k+"_readme_sha256") for k in ("root","topic")},
          "source_initial_job":ini.get("job"),"core_receipt":compact(cr),"run_receipt":compact(rr),
          "checkpoint_specs_identity_only":checkpoint_specs,"source_details":special,
          "file_schemas":schemas,"log_tails":logtails,"archive_transport":a.receipt(),
          "new_mathematics_executed":False,"all_large_outputs_rehashed":False,
          "read_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
        target=output/(label+"-intake-source-summary.json")
        m.save(target,summary)
        printed=dict(summary)
        printed.pop("source_initial_job")
        printed["selected_files"]={n:v for n,v in selected.items() if n in metadata or
                                  re.search(r"(index|history|compaction|chart|selection|source-audit)",n)}
        print("SOURCE_INTAKE_SUMMARY="+json.dumps(printed,ensure_ascii=False),flush=True)
        return {"label":label,"source":item,"summary":m.file_spec(target),"retained_input_bundle":m.file_spec(bundle)}
    finally:
        a.close()

def main():
    m.guard()
    request_path = Path(sys.argv[1])
    output = Path(sys.argv[2])
    output.mkdir(parents=True,exist_ok=True)
    request = json.loads(request_path.read_bytes())
    assert request["schema"] == 1 and request["new_mathematics_executed"] is False
    assert request["helper_sha256"] == HELPER_SHA
    assert request["reader_sha256"] == hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    work = output.parent/"working-sources"
    done,errors=[],[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        pending={pool.submit(read_source,row,work,output):row["label"] for row in request["sources"]}
        for future in concurrent.futures.as_completed(pending):
            label=pending[future]
            try:
                done.append(future.result())
            except BaseException as error:
                errors.append({"label":label,"error":str(error),"traceback":traceback.format_exc()})
                print("SOURCE_INTAKE_ERROR="+json.dumps(errors[-1]),flush=True)
    m.save(output/"intake-source-index.json",{"schema":1,"source_commit":os.environ["GITHUB_SHA"],
        "workflow_run_id":os.environ["GITHUB_RUN_ID"],"request_sha256":m.sha(request_path),
        "new_mathematics_executed":False,"sources":done,"errors":errors,
        "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
    print("INTAKE_INDEX="+json.dumps(m.file_spec(output/"intake-source-index.json")),flush=True)
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
