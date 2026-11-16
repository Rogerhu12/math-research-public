#!/usr/bin/env python3
"""R887 completed common-cusp flip and principal input certificate; pure IO only."""
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
        dependency_binding = None
        mode = row["mode"]
        if mode == "completed_R887_common_cusp_flip":
            assert label == "R887" and item["expected_conclusion"] == "success"
            certificate_name = "p41-original-common-cusp-flip-and-bounded-RR-certificate.json"
            assert fs[certificate_name]["sha256"] == row["certificate_sha256"]
            fetch([certificate_name])
            certificate = m.read(out/certificate_name)
            assert certificate["result"] == item["result"] and certificate["complete"] is True
            tag = certificate["configuration"]
            assert tag["source_sha256"] == item["core_sha256"]
            actual_fp = hashlib.sha256(json.dumps(tag,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
            assert actual_fp == row["configuration_sha256"]
            assert certificate["actual_pencil_rank"] == 962
            for flag in ("complete_U_C_146_certified","original_u_C_order252_certified",
                         "complete_Cstar_418_certified","original_Qtilde_order_minus1205_certified"):
                assert certificate[flag] is True
            for field in ("source_audit","restriction","complete_U_C_146","u_C",
                          "accepted_profile","accepted_v_C","complete_Cstar_418",
                          "original_principal_inputs","stage_manifest","resume_state"):
                value = m.plain(certificate[field])
                assert fs[value["file"]] == value
                names.add(value["file"])
            names.add(certificate_name)
            item = dict(item,manifest_sha256=ms["sha256"])
        elif mode == "ended":
            names.update(n for n in fs if fs[n]["bytes"] <= 5000000 and
                         (re.search(r"(history|compaction|chart|selection|state|source-audit|receipt|index)",n)
                          or n in ("public-actions-run.log","core.log")))
        elif mode in ("R827","selected"):
            for wanted in row["files"]:
                assert fs[wanted["file"]] == wanted
                names.add(wanted["file"])
        elif mode == "named_original_members":
            assert item.get("manifest_sha256"), "Name selection requires a pinned original manifest."
            assert len(row["names"]) == len(set(row["names"]))
            for name in row["names"]:
                assert Path(name).name == name and name in fs
                names.add(name)
            for wanted in row.get("known_file_pins", []):
                assert fs[wanted["file"]] == wanted
        elif mode == "all_original_math_json_by_prefix":
            assert item.get("manifest_sha256")
            prefix = row["prefix"]
            assert prefix and "/" not in prefix
            names.update(n for n in fs if n.startswith(prefix) and n.endswith(".json.gz"))
            for name in row.get("additional_names", []):
                assert Path(name).name == name and name in fs
                names.add(name)
            for wanted in row.get("known_file_pins", []):
                assert fs[wanted["file"]] == wanted
            assert len(names) >= row["minimum_selected_file_count"]
        elif mode == "original_C_columns_from_completed_R827_reduction":
            assert label == "R820"
            dependency = row["dependency"]
            assert dependency["label"] == "R827"
            dep_summary = m.read(output/"R827-intake-source-summary.json")
            assert dep_summary["source"]["run_id"] == dependency["source_run_id"]
            assert dep_summary["source"]["source_commit"] == dependency["source_commit"]
            dep_spec = dep_summary["selected_files"][dependency["file"]]
            dep_path = work/"R827"/"original"/dependency["file"]
            assert m.file_spec(dep_path) == dep_spec
            value = m.read(dep_path)
            assert value["complete"] is True and value["prime"] == 1000000753
            assert value["all_original_rational_coefficients_p_integral"] is True
            assert value["complete_flat_target_not_squarefree_replacement"] is True
            assert value["original_exact_two_chart_transition_certificate_preserved"] is True
            origin = value["configuration"]["source_identities"]["R820"]
            for key in ("run_id","source_commit","core_sha256","manifest_sha256"):
                assert origin[key] == item[key]
            assert set(value["charts"]) == set(value["source_R820_indexes"]) == {"tau","sigma"}
            complete_columns = {}
            for chart in ("tau","sigma"):
                index = m.plain(value["source_R820_indexes"][chart])
                assert fs[index["file"]] == index
                names.add(index["file"])
                columns = value["charts"][chart]["original_column_sources"]
                assert len(columns) == 272
                actual = []
                for ref in columns:
                    entry = m.plain(ref)
                    assert fs[entry["file"]] == entry
                    names.add(entry["file"])
                    actual.append(entry)
                assert len({x["file"] for x in actual}) == 272
                complete_columns[chart] = actual
            assert len(set(x["file"] for a0 in complete_columns.values() for x in a0)) == 544
            for name in row.get("additional_names", []):
                assert Path(name).name == name and name in fs
                names.add(name)
            dependency_binding = {
                "source_label":"R827","source_completed_C_reduction":dep_spec,
                "source_identity":origin,"complete_original_column_count":544,
                "both_original_indexes":value["source_R820_indexes"],
                "every_original_column_spec_matches_the_R820_manifest":True,
                "no_cusp_kernel_or_rational_reduction_recomputed":True}
        else:
            raise AssertionError(mode)
        fetch(names)
        if mode == "completed_R887_common_cusp_flip":
            inventory = m.read(out/certificate["stage_manifest"]["file"])
            assert inventory["result"] == item["result"] and inventory["configuration"] == tag
            assert inventory["complete"] is True and len(inventory["files"]) == row["expected_complete_stage_count"]
            for entry in inventory["files"]:
                entry = m.plain(entry)
                assert fs[entry["file"]] == entry
            current_name = certificate["resume_state"]["file"]
            for name in names:
                if name.endswith(".json.gz"):
                    value = m.read(out/name)
                    assert value["result"] == item["result"] and value["configuration"] == tag
                    assert value["complete"] is (name != current_name)
        ini,rr = (m.read(out/n) for n in ("public-actions-input.json","run-receipt.json"))
        assert ini["result"] == rr["result"] == manifest["result"]
        assert ini["source_commit"] == rr["source_commit"] == item["source_commit"]
        assert str(rr["workflow_run_id"]) == str(item["run_id"])
        cr = m.read(out/"core-receipt.json") if "core-receipt.json" in names else None
        if cr is not None:
            assert cr["result"] == manifest["result"] and cr["source_sha256"] == ini["core_sha256"]
        if item.get("core_sha256"):
            assert ini["core_sha256"] == item["core_sha256"]
        if mode == "completed_R887_common_cusp_flip":
            assert ini["driver_sha256"] == row["wrapper_sha256"]
            assert rr["complete"] is True and rr["process_exit_code"] == 0 and rr["error"] is None
            assert rr["core_receipt_sha256"] == fs["core-receipt.json"]["sha256"]
            assert cr["certificate_sha256"] == row["certificate_sha256"]
            assert cr["complete"] is True and cr["exit_code"] == 0
        special = {}
        for field in row.get("print_certificate_stage_fields", []):
            n = certificate[field]["file"]
            assert n in names
            special[n] = m.read(out/n)
        for n in row.get("print_json_files", []):
            assert n in names
            special[n] = m.read(out/n)
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
          "dependency_binding":dependency_binding,
          "checkpoint_specs_identity_only":checkpoint_specs,"source_details":special,
          "file_schemas":schemas,"log_tails":logtails,"archive_transport":a.receipt(),
          "source_configuration_sha256":row.get("configuration_sha256"),
          "new_mathematics_executed":False,"all_large_outputs_rehashed":False,
          "read_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
        target=output/(label+"-intake-source-summary.json")
        m.save(target,summary)
        printed=dict(summary)
        printed.pop("source_initial_job")
        printed["source_details"] = {n:{k:v for k,v in value.items()
            if isinstance(v,(bool,int,float)) or v is None or (isinstance(v,str) and len(v)<=160)}
            if isinstance(value,dict) else shape(value,1) for n,value in special.items()}
        printed["selected_files"]=selected
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
    labels = [row["label"] for row in request["sources"]]
    assert len(labels) == len(set(labels))
    first_labels = request.get("read_first",[])
    assert first_labels == ["R887"] and labels == ["R887"]
    for label in first_labels:
        row = next(v for v in request["sources"] if v["label"] == label)
        try:
            done.append(read_source(row,work,output))
        except BaseException as error:
            errors.append({"label":label,"error":str(error),"traceback":traceback.format_exc()})
            print("SOURCE_INTAKE_ERROR="+json.dumps(errors[-1]),flush=True)
    remaining = [row for row in request["sources"] if row["label"] not in first_labels]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        pending={pool.submit(read_source,row,work,output):row["label"] for row in remaining}
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
