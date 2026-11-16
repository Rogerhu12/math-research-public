#!/usr/bin/env python3
"""Transfer the six remaining same-s original U.1 branches and completed F69 sources.
Only archive bytes, source identities, shapes and recorded certificates are read here.
No arithmetic core, finite field package, matrix operation, or new root calculation runs.
"""
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import sys
import tarfile
import traceback

S=Path(__file__).resolve().parent
RANGE_HELPER_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
INTAKE_HELPER_SHA="15924bc6e7352d2c58b922bb85efbca6b324b3cf24632a5de46c51b03d9aefc3"
R877_IO_SHA="a574bd4fa95c2d80b1b6b6037f7e944a0c9f79660b7c4667ac99e97be3507221"
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
PRIME=1000000753
SELECTION="R787-prime-1000000753-selection.json.gz"
CHART="R787-prime-1000000753-chart.json.gz"
BLOCKS="R787-prime-1000000753-rational-blocks.json.gz"
R824_CHART="R824-power5-prime-1000000753-chart.json.gz"
CERT877="p41-original-canonical-A-normal-input-certificate.json"
CERT824="p41-original-global-polar-generators-certificate.json"
GROUPS=("R827","R842","R787","R849")

def load(name,digest,alias):
    path=S/name
    assert hashlib.sha256(path.read_bytes()).hexdigest()==digest,name
    spec=importlib.util.spec_from_file_location(alias,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

q=load("R880_public_original_pencil_jet_cusp_source_intake.py",INTAKE_HELPER_SHA,
       "R880_six_branch_frozen_intake_IO")
w=load("R877_public_original_canonical_A_normal_input.py",R877_IO_SHA,
       "R880_six_branch_frozen_R877_IO")
m=q.m
assert q.HELPER_SHA==RANGE_HELPER_SHA

def identity(value):
    return {key:value[key] for key in BASE}

def fetch_selected_from_parent(archive,parent_files,reference,directory):
    reference=m.plain(reference)
    assert parent_files[reference["file"]]==reference
    archive.extract_bound(reference["file"],reference["sha256"],directory/reference["file"],reference["bytes"])
    assert m.file_spec(directory/reference["file"])==reference
    return directory/reference["file"]

def validate_metadata(folder,source,files,certificate_name):
    for name in META[:2]:
        w.bound(folder,files[name])
    initial,run=(m.read(folder/name) for name in META[:2])
    assert initial["result"]==run["result"]==source["result"]
    assert initial["source_commit"]==run["source_commit"]==source["source_commit"]
    assert str(run["workflow_run_id"])==str(source["run_id"])
    assert initial["core_sha256"]==source["core_sha256"]
    assert initial.get("driver_sha256",initial.get("wrapper_sha256"))==source["wrapper_sha256"]
    cert=m.read(w.bound(folder,files[certificate_name]))
    assert cert["complete"] is True and cert["result"]==source["result"]
    tag=cert["configuration"]
    assert tag["result"]==source["result"] and tag["source_sha256"]==source["core_sha256"]
    assert run["complete"] is True and run["process_exit_code"]==0 and run["error"] is None
    assert run["core_receipt_sha256"]==files[META[2]]["sha256"]
    core=m.read(w.bound(folder,files[META[2]]))
    assert core["result"]==source["result"] and core["source_sha256"]==source["core_sha256"]
    assert core["complete"] is True and core["certificate_sha256"]==files[certificate_name]["sha256"]
    return initial,run,cert,tag

def selected_files(summary):
    files={name:m.plain(entry) for name,entry in summary["selected_files"].items()}
    assert len(files)==summary["selected_file_count"]
    files[MANIFEST]=m.plain(summary["manifest"])
    if summary["manifest_reference"] is not None:
        files[REFERENCE]=m.plain(summary["manifest_reference"])
    return files

def stream_subset(bundle,folder,files,keep):
    assert keep<=set(files)
    folder.mkdir(parents=True,exist_ok=True)
    seen=set()
    with tarfile.open(bundle,"r|gz") as tar:
        for member in tar:
            path=PurePosixPath(member.name)
            assert member.isfile() and not path.is_absolute() and len(path.parts)==2
            assert path.parts[0]=="original" and ".." not in path.parts and "\\" not in member.name
            name=path.name
            assert name in files and name not in seen
            seen.add(name);ref=files[name]
            assert member.size==ref["bytes"]
            stream=tar.extractfile(member);assert stream is not None
            digest=hashlib.sha256();count=0
            target=folder/name
            temporary=target.with_name(name+".tmp")
            output=temporary.open("wb") if name in keep else None
            try:
                for block in iter(lambda:stream.read(4*1024*1024),b""):
                    count+=len(block);digest.update(block)
                    if output is not None:output.write(block)
            finally:
                if output is not None:output.close()
            assert count==ref["bytes"] and digest.hexdigest()==ref["sha256"],name
            if name in keep:temporary.replace(target)
    assert seen==set(files)
    return {name:files[name] for name in sorted(keep)}

def original_subset_names(label,files,selectors):
    keep=set(META)|{MANIFEST,REFERENCE}
    for value in selectors.values():
        if value["source_group"]==label:keep.add(value["file"])
    if label=="R787":
        keep|={SELECTION,CHART,BLOCKS}
    else:
        keep|={name for name in files if name.endswith("-certificate.json")}
    if label=="R849":
        keep.add("R839-global-polar-source-audit.json.gz")
    assert keep<=set(files),{"source":label,"missing":sorted(keep-set(files))}
    return keep

def subset_summary(label,raw,old_summary,files,folder,out,transport):
    bundle=out/(label+"-intake-selected-original-sources.tar.gz")
    q.tar_sources(bundle,folder,set(files))
    old_manifest=m.read(folder/MANIFEST)
    original={row["file"]:m.plain(row) for row in old_manifest["files"]}
    assert len(original)==raw["manifest_file_count"]
    assert files[MANIFEST]["sha256"]==raw["manifest_sha256"]
    for name,entry in files.items():
        if name not in (MANIFEST,REFERENCE):assert original[name]==entry
    value=dict(raw,directory=str(folder),files=files,selected_file_count=len(files),
               selected_files_sha256=w.fingerprint(files))
    tag=w.review_original(label,value)
    summary={
        "schema":1,"purpose":"original source subset transported from completed R877 only",
        "label":label,"source":raw,"original_result":raw["result"],
        "manifest":files[MANIFEST],"manifest_reference":files[REFERENCE],
        "original_manifest_count":len(original),"selected_file_count":len(files)-2,
        "selected_files":{n:v for n,v in files.items() if n not in (MANIFEST,REFERENCE)},
        "retained_input_bundle":m.file_spec(bundle),"source_core_sha256":raw["core_sha256"],
        "source_wrapper_sha256":raw["wrapper_sha256"],"source_configuration_sha256":w.fingerprint(tag),
        "source_initial_job":old_summary.get("source_initial_job"),
        "run_receipt":old_summary["run_receipt"],"core_receipt":old_summary["core_receipt"],
        "original_transport_binding":transport,
        "all_parent_carrier_members_bytes_and_SHA_verified":True,
        "only_the_recorded_subset_repacked":True,
        "new_mathematics_executed":False,
        "read_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
    target=out/(label+"-intake-source-summary.json");m.save(target,summary)
    print("SIX_BRANCH_INHERITED_SOURCE="+json.dumps({
        "label":label,"source":identity(raw),"configuration_sha256":w.fingerprint(tag),
        "selected_file_count_including_manifest":len(files),"retained_input_bundle":m.file_spec(bundle),
        "selected_files":files,"new_mathematics_executed":False}),flush=True)
    return {"label":label,"source":raw,"summary":m.file_spec(target),
            "retained_input_bundle":m.file_spec(bundle)},value,tag

def inherit_R877_sources(request,work,out,parent_entry):
    parent_summary=m.read(w.bound(out,parent_entry["summary"]))
    parent_files=selected_files(parent_summary)
    folder=work/"R877"/"original"
    initial,run,certificate,tag=validate_metadata(folder,request["R877"],parent_files,CERT877)
    assert certificate["all1380_original_short_coordinates_verified"] is True
    assert certificate["characteristic_zero_normal_coordinates_reconstructed"] is False
    assert tag["strategy"]["original_branch"]==0 and tag["strategy"]["canonical_free_column"]==1186
    source_job=initial["job"]
    assert set(source_job["sources"])==set(GROUPS)
    selectors=source_job["input_selectors"]
    expected_chunks=["R877-original-V5-prefix-and-A-part-"+str(first).zfill(4)+"-"+
                     str(min(first+64,1234)).zfill(4)+".json.gz" for first in range(0,1234,64)]
    assert len(expected_chunks)==20
    audit=m.read(w.bound(folder,parent_files["R877-original-source-audit.json.gz"]))
    assert audit["complete"] is True and audit["configuration"]==tag
    rows=audit["original_real_V5_rows"];assert len(rows)==1234
    for first,name in zip(range(0,1234,64),expected_chunks):
        part=m.read(w.bound(folder,parent_files[name]))
        assert part["complete"] is True and part["configuration"]==tag and part["prime"]==PRIME
        assert part["first_column"]==first and part["stop_column"]==min(first+64,1234)
        assert [m.plain(x) for x in part["source_original_V5_rows"]]==[m.plain(x) for x in rows[first:first+64]]
        assert len(part["original_prefix_columns_mod_prime"])==min(64,1234-first)
        assert all(len(column)==1380 for column in part["original_prefix_columns_mod_prime"])
    transport_dir=work/"R877-inherited-transport";transport_dir.mkdir(parents=True,exist_ok=True)
    archive=m.Archive(request["R877"],work/"R877"/"transport",whole=False)
    entries=[];values={};tags={}
    try:
        original_manifest=m.read(folder/MANIFEST)
        fs={row["file"]:m.plain(row) for row in original_manifest["files"]}
        index_spec=m.plain(source_job["intake"]["source_index"])
        index=m.read(fetch_selected_from_parent(archive,fs,index_spec,transport_dir))
        old_intake=source_job["intake"]
        assert index["new_mathematics_executed"] is False and index["errors"]==[]
        assert str(index["workflow_run_id"])==str(old_intake["run_id"])
        assert index["source_commit"]==old_intake["source_commit"]
        assert index["request_sha256"]==old_intake["request_sha256"]
        originals={entry["label"]:entry for entry in index["sources"]}
        assert set(originals)==set(GROUPS) and len(originals)==len(index["sources"])
        for label in GROUPS:
            entry=originals[label];raw=source_job["sources"][label]
            for key in ("run_id","source_commit","core_sha256","manifest_sha256"):
                assert str(entry["source"][key])==str(raw[key])
            summary_ref=m.plain(entry["summary"])
            old_summary=m.read(fetch_selected_from_parent(archive,fs,summary_ref,transport_dir))
            assert old_summary["source"]==entry["source"]
            assert old_summary["label"]==label and old_summary["original_result"]==raw["result"]
            assert old_summary["new_mathematics_executed"] is False
            assert old_summary["source_core_sha256"]==raw["core_sha256"]
            assert old_summary["source_wrapper_sha256"]==raw["wrapper_sha256"]
            files=selected_files(old_summary)
            assert len(files)==raw["expected_selected_file_count"]
            assert w.stable_source(dict(raw,selected_file_count=len(files),
                      selected_files_sha256=w.fingerprint(files)))==tag["sources"][label]
            for name,pin in raw.get("file_pins",{}).items():assert files[name]==m.plain(pin)
            bundle_ref=m.plain(entry["retained_input_bundle"])
            assert bundle_ref==m.plain(old_summary["retained_input_bundle"])
            assert bundle_ref==m.plain(old_intake["bundles"][label])
            bundle=fetch_selected_from_parent(archive,fs,bundle_ref,transport_dir)
            selected=stream_subset(bundle,work/label/"original",files,
                                   original_subset_names(label,files,selectors))
            link={"via_source":request["R877"],"via_manifest":parent_summary["manifest"],
                "completed_R877_certificate":parent_files[CERT877],
                "original_intake_index":index_spec,"original_source_summary":summary_ref,
                "original_complete_selected_carrier":bundle_ref,
                "original_selected_source_count":len(files),
                "original_selected_files_sha256":w.fingerprint(files),
                "completed_R877_original_source_identity":tag["sources"][label]}
            item,value,oldtag=subset_summary(label,raw,old_summary,selected,work/label/"original",out,link)
            entries.append(item);values[label]=value;tags[label]=oldtag
        return entries,values,tags,parent_files,certificate,tag,expected_chunks,archive.receipt()
    finally:archive.close()

def select_remaining_branches(request,values):
    original=values["R787"]
    folder=Path(original["directory"])
    selection=m.read(w.bound(folder,original["files"][SELECTION]))
    chart=m.read(w.bound(folder,original["files"][CHART]))
    assert selection["complete"] is True and chart["complete"] is True
    assert selection["configuration"]==chart["configuration"]
    assert chart["chosen_free_column"]==1186 and chart["other_free_columns_set_to_zero"] is True
    assert chart["actual_modular_rank"]==1186
    assert selection["prime"]==PRIME and selection["prime_proved"] is True
    assert selection["all_14_L_branches_distinct"] is True
    assert selection["all_rational_denominators_units"] is True
    assert selection["all_kappa_reductions_invertible"] is True
    roots=selection["roots_B_s"]
    assert len(roots)==14 and all(isinstance(row,list) and len(row)==2 for row in roots)
    assert roots[0]==request["original_branch0_roots_B_s"]
    same=[i for i,pair in enumerate(roots) if pair[1]==request["original_s_root"]]
    assert len(same)==7 and 0 in same and len({roots[i][0] for i in same})==7
    remaining=[i for i in same if i!=0]
    assert len(remaining)==6
    return selection,chart,roots,same,remaining

def review_R824(request,work,out,entry,values,selection,chart,roots,remaining):
    summary=m.read(w.bound(out,entry["summary"]))
    files=selected_files(summary);folder=work/"R824"/"original"
    initial,run,certificate,tag=validate_metadata(folder,request["R824"],files,CERT824)
    assert identity(tag["source_identities"]["R787"])==identity(values["R787"])
    assert tag["field"]==chart["configuration"]["field"]
    newchart=m.read(w.bound(folder,files[R824_CHART]))
    assert newchart["complete"] is True and newchart["configuration"]==tag
    assert newchart["prime"]==PRIME and newchart["ordinary_power"]==5
    assert newchart["actual_rank"]==1186 and newchart["kernel_dimension"]==28
    assert newchart["pivot_rows"]==chart["pivot_rows"] and newchart["pivot_columns"]==chart["pivot_columns"]
    old_manifest=m.read(Path(values["R787"]["directory"])/MANIFEST)
    original_files={v["file"]:m.plain(v) for v in old_manifest["files"]}
    profiles=[];free=None
    for branch in remaining:
        name="R824-power5-prime-"+str(PRIME)+"-branch-"+str(branch).zfill(2)+".json.gz"
        value=m.read(w.bound(folder,files[name]))
        assert value["complete"] is True and value["configuration"]==tag
        assert value["prime"]==PRIME and value["ordinary_power"]==5 and value["branch"]==branch
        assert value["roots_B_s"]==roots[branch]
        assert value["actual_Schur_rank"]==1186 and value["selected_minor_det_mod_prime"]!=0
        assert m.plain(value["chart"])==files[R824_CHART]
        assert m.plain(value["rational_block"])==values["R787"]["files"][BLOCKS]
        assert value["original_reserved_column_retained_without_new_lift"] is True
        assert value["full_original_modular_relations_verified_for_all_new_free_targets"] is True
        origin=m.plain(value["original_branch_inverse_reused_from"])
        assert origin["file"]=="R787-prime-"+str(PRIME)+"-branch-"+str(branch).zfill(2)+".json.gz"
        assert original_files[origin["file"]]==origin
        columns=value["kernel_free_columns"]
        assert len(columns)==len(set(columns))==28 and 1186 in columns
        if free is None:free=columns
        else:assert free==columns
        index=columns.index(1186)
        aa,cc=value["kernel_A_mod_prime"],value["kernel_C_mod_prime"]
        assert len(aa)==1234 and all(len(row)==28 for row in aa)
        assert len(cc)==1214 and all(len(row)==28 for row in cc)
        assert all(cc[c][index]==int(c==1186) for c in columns)
        profiles.append({"original_branch":branch,"roots_B_s":roots[branch],
            "canonical_free_column":1186,"canonical_column_position":index,
            "recorded_unit_minor_determinant":value["selected_minor_det_mod_prime"],
            "source_profile":files[name],"source_original_R787_branch":origin,
            "source_original_chart":values["R787"]["files"][CHART],
            "source_original_rational_blocks":values["R787"]["files"][BLOCKS],
            "recorded_original_reserved_column_retained_without_new_lift":True,
            "stored_A_shape":[1234,28],"stored_C_shape":[1214,28]})
    return profiles,files,tag

def main():
    m.guard();sys.set_int_max_str_digits(0)
    request_path=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
    item=m.read(request_path)
    assert item["schema"]==1 and item["new_mathematics_executed"] is False
    assert item["reader_sha256"]==hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    assert item["intake_helper_sha256"]==INTAKE_HELPER_SHA
    assert item["R877_IO_sha256"]==R877_IO_SHA and item["helper_sha256"]==RANGE_HELPER_SHA
    work=out.parent/"working-sources";entries=[];errors=[];branch_spec=None
    try:
        parent=q.read_source({"label":"R877","source":item["R877"],
            "mode":"all_original_math_json_by_prefix","prefix":"R877-",
            "minimum_selected_file_count":28,"additional_names":[
                "R877-original-source-inventory.json","R877-retained-inputs-receipt.json"],
            "known_file_pins":[item["R877_certificate"]]},work,out)
        entries.append(parent)
        inherited,values,tags,parent_files,certificate,parent_tag,chunks,transport=inherit_R877_sources(item,work,out,parent)
        entries.extend(inherited)
        selection,chart,roots,same,remaining=select_remaining_branches(item,values)
        names=[R824_CHART]+["R824-power5-prime-"+str(PRIME)+"-branch-"+str(i).zfill(2)+".json.gz" for i in remaining]
        selected=q.read_source({"label":"R824","source":item["R824"],
            "mode":"named_original_members","names":names},work,out)
        entries.append(selected)
        profiles,files824,tag824=review_R824(item,work,out,selected,values,selection,chart,roots,remaining)
        receipt={
            "schema":1,"purpose":"six original same-s branches; no new RHS or arithmetic",
            "prime":PRIME,"original_s_root":item["original_s_root"],
            "original_zeta_root":item["original_zeta_root"],"source_selection":values["R787"]["files"][SELECTION],
            "original_roots_B_s":roots,"original_same_s_branch_indices":same,
            "remaining_branch_indices":remaining,"canonical_free_column":1186,
            "existing_original_branch0_R877_certificate":parent_files[CERT877],
            "completed_F69_prefix_groups":[parent_files[name] for name in chunks],
            "complete_original_F69_column_count":1234,"prefix_row_count":1380,
            "remaining_A_B_profiles":profiles,"new_right_hand_sides_requested":12,
            "original_R877_configuration_sha256":w.fingerprint(parent_tag),
            "original_R824_configuration_sha256":w.fingerprint(tag824),
            "old_source_configuration_sha256":{label:w.fingerprint(tag) for label,tag in tags.items()},
            "new_mathematics_executed":False,"old_F69_rows_recomputed":False,
            "original_1186_direction_recomputed":False,"original_S5_inverse_recomputed":False,
            "arithmetic_Galois_orbit_order_still_to_be_certified_by_new_consumer":True,
            "all_selected_stage_bytes_and_SHA_verified":True,
            "inherited_archive_transport":transport}
        path=out/"R880-six-branch-source-selection.json";m.save(path,receipt);branch_spec=m.file_spec(path)
        print("SIX_BRANCH_SELECTION_IO="+json.dumps(receipt,sort_keys=True),flush=True)
    except BaseException as error:
        record={"error":str(error),"traceback":traceback.format_exc()}
        errors.append(record);print("SOURCE_INTAKE_ERROR="+json.dumps(record),flush=True)
    index={"schema":1,"source_commit":os.environ["GITHUB_SHA"],
        "workflow_run_id":os.environ["GITHUB_RUN_ID"],"request_sha256":m.sha(request_path),
        "new_mathematics_executed":False,"sources":entries,"branch_selection":branch_spec,"errors":errors,
        "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
    m.save(out/"intake-source-index.json",index)
    print("INTAKE_INDEX="+json.dumps(m.file_spec(out/"intake-source-index.json")),flush=True)
    if errors:raise SystemExit(1)

if __name__=="__main__":main()
