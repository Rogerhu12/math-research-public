#!/usr/bin/env python3
"""R882 stdlib-only provenance, immutable source transport and same-core recovery."""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import subprocess
import sys
import traceback

S=Path(__file__).resolve().parent
TOPIC=S.parent
REPO=TOPIC.parent.parent
REPOSITORY="Rogerhu12/math-research-public"
RESULT="R882-original-cyclic-seven-common-place-coefficients"
FINAL="p41-original-cyclic-seven-common-place-coefficients-certificate.json"
PREFIX="R882-common-place-"
CORE="R882_original_common_place_coefficients.py"
REQUEST=TOPIC/"notes/R882-common-place-coefficients-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R882-retained-R873-selected-stages.tar.gz"
OLD_BUNDLE="R873-retained-original-inputs.tar.gz"
OLD_INVENTORY="R873-original-source-inventory.json"
OLD_RECEIPT="R873-retained-inputs-receipt.json"
INVENTORY="R882-original-source-inventory.json"
INPUT_RECEIPT="R882-retained-inputs-receipt.json"
EXPANDED="R882-expanded-job.json"
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
SOURCE_RESULT="R873-original-cyclic-seven-correspondence"
SOURCE_CORE="3c4922ee5b83d82123d234df47e67f82d7c8032f1152c6cf14df34622101918c"
OLD_IO_FILE="R873_public_original_cyclic_seven_correspondence.py"
OLD_IO_SHA="033a8cacb5d9699f3426e0a66cb11d2659a724e1300a5f4d4488f27483d2560a"
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
P=1000000753
OLD=None
STRATEGY={
    "scope": "common-place-seventeen-coefficients-only",
    "original_curve": "original genus127 Y at p41; original minus3 descent and level82 phase",
    "auxiliary_prime": 1000000753,
    "original_zeta_root": 549966761,
    "original_s_root": 99932770,
    "old_auxiliary_prime": 739,
    "integer_scale": "82^16",
    "matrix_shape": [
        2200,
        2058
    ],
    "right_hand_side_shape": [
        2200,
        17
    ],
    "column_order": "2050 original R799 V8 columns with only q109 from R801; eight completed R873 complements",
    "complement_V2_indices": [
        0,
        1,
        2,
        3,
        73,
        74,
        75,
        76
    ],
    "selected_rows": "exactly the completed R873 2058 selected coordinate rows",
    "matrix_column_block_size": 64,
    "verification_row_block_size": 64,
    "unit_minor_policy": "fixed original rows; stop honestly if singular at1000000753",
    "inverse_verification": "both complete2058 square products",
    "coordinate_verification": "all2200 rows for all17 targets",
    "target_column_order": "P coefficients0..8 then K coefficients0..7",
    "characteristic_zero_coordinates": "same exact R873 integer-minor unit-solve expression; not expanded",
    "old_739_coordinates_or_inverse_reused_as753": False,
    "new_Eisenstein_tail_or_exact_norm_recomputed": False,
    "target_normal_basis_computed": False,
    "nine_reference_norms_computed": False,
    "original_Picard_support_computed": False,
    "height_or_nonp_calibration_computed": False,
    "budget_and_transport_excluded_from_identity": True
}

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for part in iter(lambda:f.read(4*1024*1024),b""):
            h.update(part)
    return h.hexdigest()

def read(path):
    path=Path(path)
    with (gzip.open if path.suffix==".gz" else open)(path,"rt",encoding="utf-8") as f:
        return json.load(f)

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    tmp.write_text(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
    tmp.replace(path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def plain(row):
    ans={k:row[k] for k in ("file","bytes","sha256")}
    p=PurePosixPath(ans["file"])
    assert len(p.parts)==1 and p.name not in ("",".","..") and "\\" not in ans["file"]
    assert isinstance(ans["bytes"],int) and ans["bytes"]>=0
    assert re.fullmatch("[0-9a-f]{64}",ans["sha256"])
    return ans

def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}

def bound(folder,row):
    row=plain(row);path=Path(folder)/row["file"]
    assert spec(path)==row,("source_bytes",row["file"])
    return path

def topic_path(name):
    p=PurePosixPath(name)
    assert not p.is_absolute() and ".." not in p.parts
    path=(TOPIC/str(p)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path

def identity(source):
    return {**{k:source[k] for k in BASE},
            "configuration_sha256":source["configuration_sha256"],
            "certificate":plain(source["certificate"]),
            "selected_files_sha256":fingerprint(source["files"])}

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"p":41,
            "python_flint":"0.9.0","proofs":item["proofs"],
            "method_sha256":item["method_sha256"],
            "sources":{g:identity(item["retained_sources"][g]) for g in ("R873","R799","R801")},
            "inputs":item["inputs"],"original_carrier":item["original_carrier"],
            "strategy":STRATEGY}

def load_io():
    global OLD
    assert sha(S/OLD_IO_FILE)==OLD_IO_SHA and sha(S/RANGE_FILE)==RANGE_SHA
    description=importlib.util.spec_from_file_location("R882_frozen_R873_stdlib_source_IO",S/OLD_IO_FILE)
    OLD=importlib.util.module_from_spec(description)
    description.loader.exec_module(OLD)
    OLD.load_io()
    assert OLD.RESULT==SOURCE_RESULT
    # Only stdlib IO helpers are used; no old mathematical Job/core is imported.

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve()
    assert item["result"]==RESULT and item["p"]==41 and item["producer_inputs_pending"] is False
    assert item["core"]==CORE and sha(S/CORE)==item["core_sha256"]
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["source_io_helper"]==OLD_IO_FILE and item["source_io_helper_sha256"]==OLD_IO_SHA
    assert item["io_helper"]==RANGE_FILE and item["io_helper_sha256"]==RANGE_SHA
    assert 0<item["budget_minutes"]<=300
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert item["source_artifact"]["result"]==SOURCE_RESULT
    assert item["source_artifact"]["core_sha256"]==SOURCE_CORE
    assert set(item["original_source_pins"])=={"R799","R801"}
    load_io()

def original_pins(item,sources,inputs,carrier):
    prior=item["source_artifact"]
    assert all(str(prior[k])==str(sources["R873"][k]) for k in BASE)
    assert sources["R873"]["certificate"]==plain(prior["certificate"])
    assert carrier==item["original_carrier"]
    assert plain(inputs["V8_index"])==plain(item["selection_pins"]["V8_index"])
    assert plain(inputs["V8_frontier"])==plain(item["selection_pins"]["V8_frontier"])
    assert plain(inputs["recipe_plan"])==plain(item["selection_pins"]["recipe_plan"])
    for group in ("R799","R801"):
        OLD.same_original_source(item["original_source_pins"][group],sources[group])
    assert set(inputs)=={"section_basis","target_index","exact_expression","correspondence_DAG",
                         "V8_index","V8_frontier","recipe_plan"}

def source_review(item,retained,sources,inputs):
    root=Path(retained);source=sources["R873"];folder=root/"R873"
    entries=OLD.entry_map(folder,source)
    pin=dict(source,certificate_name=source["certificate"]["file"],
             certificate_sha256=source["certificate"]["sha256"])
    cert,tag,initial=OLD.metadata(folder,pin,entries)
    assert tag["source_sha256"]==SOURCE_CORE
    assert cert["actual_auxiliary_prime"]==739 and cert["actual_new_complement_V2_indices"]==[0,1,2,3,73,74,75,76]
    for key in ("all17_exact_characteristic_zero_unit_solve_expressions_certified",
                "all2200_original_modular_coordinate_relations_verified",
                "actual_original_cyclic7_correspondence_source_target_expression_certified"):
        assert cert[key] is True
    for name,row in source["files"].items():
        assert entries[name]==row and name==row["file"]
        path=bound(folder,row)
        if name.endswith(".json.gz"):
            value=read(path)
            assert value["complete"] is True and value["configuration"]==tag
    assert fingerprint(tag)==source["configuration_sha256"]
    mathematical_inventory=read(bound(folder,cert["stage_manifest"]))
    mathematical_entries={r["file"]:plain(r) for r in mathematical_inventory["files"]}
    assert len(mathematical_entries)==len(mathematical_inventory["files"])
    for name,row in source["files"].items():
        if name.startswith("R873-") and name.endswith(".json.gz") and name!=cert["stage_manifest"]["file"]:
            assert mathematical_entries[name]==row
    assert initial["wrapper_sha256"]==OLD_IO_SHA
    for left,right in (("section_basis","section_basis"),("target_index","norm_target_index"),
                       ("exact_expression","exact_coordinate_expression"),("correspondence_DAG","correspondence_DAG")):
        assert plain(inputs[left])==plain(cert[right]) and inputs[left]["source_group"]=="R873"
    basis=read(bound(folder,inputs["section_basis"]))
    assert basis["actual_nonzero_minor_rank"]==2058 and basis["prime"]==739
    assert basis["actual_2058_minor_determinant"]==510
    assert len(basis["selected_coordinate_rows"])==2058
    assert [v["original_V2_index"] for v in basis["selected_complement"]]==[0,1,2,3,73,74,75,76]
    for entry in basis["selected_complement"]:
        value=read(bound(folder,entry["candidate"]))
        assert value["original_V2_index"]==entry["original_V2_index"]
        assert value["integer_scale"]==str(82**16)
        assert len(value["integer_v_t_coefficients"])==110
        assert all(len(row)==20 for row in value["integer_v_t_coefficients"])
    targets=read(bound(folder,inputs["target_index"]))
    assert targets["actual_target_count"]==17 and len(targets["targets"])==17
    assert targets["targets"][:9]==targets["P_coefficients"]
    assert targets["targets"][9:]==targets["K_coefficients"]
    for row in targets["targets"]:
        value=read(bound(folder,row))
        assert value["integer_scale"]==str(82**16) and value["qY_count"]==110
        assert len(value["integer_v_t_coefficients"])==110
        assert all(len(r)==20 for r in value["integer_v_t_coefficients"])
    expression=read(bound(folder,inputs["exact_expression"]))
    assert expression["prime"]==739 and expression["basis_minor"]==plain(inputs["section_basis"])
    assert expression["all2200_coordinates_for_all17_targets_verified_mod_prime"] is True
    assert expression["target_index"]==plain(inputs["target_index"])
    assert expression["selected_coordinate_rows"]==basis["selected_coordinate_rows"]
    program=read(bound(folder,inputs["correspondence_DAG"]))
    assert program["coefficient_unit_solve"]==plain(inputs["exact_expression"])
    assert program["exact_original_correspondence_expression_certified"] is True
    oldinv=read(bound(folder,source["files"][OLD_INVENTORY]))
    oldreceipt=read(bound(folder,source["files"][OLD_RECEIPT]))
    assert oldinv["result"]==oldreceipt["result"]==SOURCE_RESULT
    assert oldinv["complete"] is True and oldreceipt["complete"] is True
    assert plain(oldreceipt["source_inventory"])==plain(item["original_carrier"]["source_inventory"])
    assert plain(oldreceipt["source_bundle"])==plain(item["original_carrier"]["input_bundle"])
    assert oldreceipt["selected_file_count"]==item["original_carrier"]["selected_file_count"]==4960
    for group in ("R799","R801"):
        assert sources[group]==oldinv["sources"][group]
        pin0=item["original_source_pins"][group]
        actual=OLD.review_group(group,pin0,root,sources[group]["files"])
        assert actual==sources[group]
    for key in ("V8_index","V8_frontier","recipe_plan"):
        assert inputs[key]==oldinv["inputs"][key]
    index=read(bound(root/"R799",inputs["V8_index"]))
    frontier=read(bound(root/"R801",inputs["V8_frontier"]))
    assert len(index["basis_rows"])==len(frontier["basis_rows"])==2050
    for i,(left,right) in enumerate(zip(index["basis_rows"],frontier["basis_rows"])):
        assert left["index"]==right["index"]==i
        assert sources["R799"]["files"][left["file"]]==plain(left)
        candidates=[v for v in right["new_tail_segments"] if v["first"]<=109<v["stop"]]
        assert len(candidates)==1 and candidates[0]["producer"]=="R801"
        assert sources["R801"]["files"][candidates[0]["file"]]==plain(candidates[0])
    original_pins(item,sources,inputs,item["original_carrier"])
    return {"result":RESULT,"complete":True,"source_R873":identity(source),
            "old_carrier_selected_member_count":4960,
            "direct_R873_stage_and_metadata_count":len(source["files"]),
            "original_R799_R801_actual_source_counts":{g:len(sources[g]["files"]) for g in ("R799","R801")},
            "all_retained_original_byte_identities_verified":True,
            "old_source_configuration_unchanged":True,
            "old_mod739_values_not_relabelled":True,
            "new_mathematics_executed_in_source_review":False}

def unpack_all(item,out,retained,inventory):
    sources=inventory["retained_sources"]
    OLD.inherited_bundle(out/BUNDLE,retained,{"R873"},{"sources":{"R873":sources["R873"]}})
    oldinv=read(Path(retained)/"R873"/OLD_INVENTORY)
    OLD.inherited_bundle(out/OLD_BUNDLE,retained,set(oldinv["sources"]),oldinv)
    assert sum(len(s["files"]) for s in oldinv["sources"].values())==4960
    original_pins(item,sources,inventory["inputs"],inventory["original_carrier"])
    return source_review(item,retained,sources,inventory["inputs"])

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R882";retained.mkdir(parents=True,exist_ok=True)
    if all((out/n).exists() for n in (BUNDLE,OLD_BUNDLE,INVENTORY,INPUT_RECEIPT)):
        inventory=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        assert plain(receipt["source_inventory"])==spec(out/INVENTORY)
        assert plain(receipt["selected_stage_bundle"])==spec(out/BUNDLE)
        assert plain(receipt["unchanged_original_carrier"])==spec(out/OLD_BUNDLE)
        review=unpack_all(item,out,retained,inventory)
        expanded=dict(item,retained_sources=inventory["retained_sources"],
                      inputs=inventory["inputs"],original_carrier=inventory["original_carrier"])
        save(out/EXPANDED,expanded)
        return retained,expanded,receipt,review
    assert allow_download,"No complete R882 source carriers are available for verify-only."
    prior=dict(item["source_artifact"],
               certificate_name=item["source_artifact"]["certificate"]["file"],
               certificate_sha256=item["source_artifact"]["certificate"]["sha256"])
    handle=OLD.Handle("R873",{"source_artifacts":{"R873":prior}},out.parent/"R882-source-download")
    try:
        cert,tag=handle.certificate,handle.tag
        assert handle.entries[prior["certificate_name"]]==plain(item["source_artifact"]["certificate"])
        assert cert["complete"] is True and tag["source_sha256"]==SOURCE_CORE
        names=set(META)|{MANIFEST,prior["certificate_name"],OLD_INVENTORY,OLD_RECEIPT}
        for key in ("section_basis","norm_target_index","exact_coordinate_expression",
                    "correspondence_DAG","source_audit","stage_manifest"):
            names.add(cert[key]["file"])
        handle.take(names)
        basis=handle.get(cert["section_basis"]["file"])
        targets=handle.get(cert["norm_target_index"]["file"])
        for entry in basis["selected_complement"]:
            names.add(entry["candidate"]["file"])
        names.update(row["file"] for row in targets["targets"])
        # The opaque original carrier is retained separately, never duplicated in the small bundle.
        carrier=item["original_carrier"]
        assert handle.entries[OLD_BUNDLE]==plain(carrier["input_bundle"])
        assert handle.entries[OLD_INVENTORY]==plain(carrier["source_inventory"])
        handle.take([OLD_BUNDLE])
        oldinv=handle.get(OLD_INVENTORY)
        oldreceipt=handle.get(OLD_RECEIPT)
        assert plain(oldreceipt["source_bundle"])==plain(carrier["input_bundle"])
        assert plain(oldreceipt["source_inventory"])==plain(carrier["source_inventory"])
        assert oldreceipt["selected_file_count"]==4960
        selected=handle.select(names,retained)
        source={**{k:prior[k] for k in BASE},
                "certificate":plain(item["source_artifact"]["certificate"]),
                "configuration_sha256":fingerprint(tag),
                "files":{n:handle.entries[n] for n in sorted(selected)}}
        sources={"R873":source,"R799":oldinv["sources"]["R799"],"R801":oldinv["sources"]["R801"]}
        inputs={left:dict(plain(cert[right]),source_group="R873") for left,right in (
            ("section_basis","section_basis"),("target_index","norm_target_index"),
            ("exact_expression","exact_coordinate_expression"),("correspondence_DAG","correspondence_DAG"))}
        for key in ("V8_index","V8_frontier","recipe_plan"):
            inputs[key]=oldinv["inputs"][key]
        for group in ("R799","R801"):
            OLD.same_original_source(item["original_source_pins"][group],sources[group])
        OLD.copy_bound(handle.directory/OLD_BUNDLE,out/OLD_BUNDLE,carrier["input_bundle"])
        OLD.inherited_bundle(out/OLD_BUNDLE,retained,set(oldinv["sources"]),oldinv)
        review=source_review(item,retained,sources,inputs)
        original_pins(item,sources,inputs,carrier)
        transport=handle.archive.receipt() if handle.archive is not None else handle.transport
        inventory={"result":RESULT,"complete":True,"retained_sources":sources,"inputs":inputs,
                   "original_carrier":carrier,"source_transport":transport,
                   "old_original_carrier_copied_verbatim":True,
                   "all4960_original_members_verified":True,
                   "direct_old_mathematical_stage_tags_unchanged":True}
        save(out/INVENTORY,inventory)
        OLD.pack(retained,{"R873":source},out/BUNDLE)
        receipt={"result":RESULT,"complete":True,"source_inventory":spec(out/INVENTORY),
                 "selected_stage_bundle":spec(out/BUNDLE),"unchanged_original_carrier":spec(out/OLD_BUNDLE),
                 "selected_direct_R873_file_count":len(source["files"]),
                 "original_carrier_file_count":4960,
                 "actual_mathematical_old_source_count":sum(len(s["files"]) for s in sources.values()),
                 "all_retained_bytes_verified":True,"new_mathematics_executed":False,
                 "source_transport":transport}
        save(out/INPUT_RECEIPT,receipt)
        expanded=dict(item,retained_sources=sources,inputs=inputs,original_carrier=carrier)
        save(out/EXPANDED,expanded)
        print("R882_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,expanded,receipt,review
    finally:
        handle.close()

def stable_request(item):
    prior=item["source_artifact"]
    return {"result":item["result"],"p":item["p"],"core_sha256":item["core_sha256"],
            "wrapper_sha256":item["wrapper_sha256"],"proofs":item["proofs"],
            "method_sha256":item["method_sha256"],
            "source_R873":{**{k:prior[k] for k in BASE},"certificate":plain(prior["certificate"])},
            "original_carrier":item["original_carrier"],"original_source_pins":item["original_source_pins"],
            "selection_pins":item["selection_pins"]}

def restore(item,out):
    resume=item.get("resume")
    if resume is None:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    folder=out.parent/"R882-resume";folder.mkdir(parents=True,exist_ok=True)
    archive=OLD.IO.Archive(resume,out.parent/"R882-resume-archive",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],folder/MANIFEST,resume.get("manifest_bytes"))
        entries=OLD.entry_map(folder,resume)
        names=(set(META)&set(entries))|{BUNDLE,OLD_BUNDLE,INVENTORY,INPUT_RECEIPT}
        archive.extract_many([(n,entries[n]["sha256"],folder/n,entries[n]["bytes"]) for n in sorted(names)])
        initial=read(folder/"public-actions-input.json");run=read(folder/"run-receipt.json")
        assert initial["result"]==run["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]==resume["source_commit"]
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        assert stable_request(initial["job"])==stable_request(item)
        assert initial["core_sha256"]==run["core_sha256"]==item["core_sha256"]
        assert initial["wrapper_sha256"]==run["wrapper_sha256"]==item["wrapper_sha256"]
        if run.get("core_receipt_sha256") is not None:
            assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
            core=read(folder/"core-receipt.json")
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        else:
            assert run["complete"] is False
        inventory=read(folder/INVENTORY);receipt=read(folder/INPUT_RECEIPT)
        assert plain(receipt["source_inventory"])==entries[INVENTORY]
        assert plain(receipt["selected_stage_bundle"])==entries[BUNDLE]
        assert plain(receipt["unchanged_original_carrier"])==entries[OLD_BUNDLE]
        sources=inventory["retained_sources"];inputs=inventory["inputs"]
        original_pins(item,sources,inputs,inventory["original_carrier"])
        expanded=dict(item,retained_sources=sources,inputs=inputs,original_carrier=inventory["original_carrier"])
        tag=expected_tag(expanded)
        assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
        for name in (BUNDLE,OLD_BUNDLE,INVENTORY,INPUT_RECEIPT):
            OLD.copy_bound(folder/name,out/name,entries[name])
        names=[n for n in entries if n.startswith(PREFIX) and n.endswith(".json.gz")]
        archive.extract_many([(n,entries[n]["sha256"],folder/n,entries[n]["bytes"]) for n in names])
        for name in names:
            value=read(folder/name)
            assert value["result"]==RESULT and value["configuration"]==tag
            assert value["complete"] is (False if name==PREFIX+"current.json.gz" else True)
            OLD.copy_bound(folder/name,out/name,entries[name])
        if FINAL in entries:
            archive.extract_bound(FINAL,entries[FINAL]["sha256"],folder/FINAL,entries[FINAL]["bytes"])
            cert=read(folder/FINAL)
            assert cert["result"]==RESULT and cert["configuration"]==tag
            if cert["complete"] is True:
                assert plain(cert["stage_manifest"])==entries[cert["stage_manifest"]["file"]]
                inv=read(bound(folder,cert["stage_manifest"]))
                for row in inv["files"]:
                    assert plain(row)==entries[row["file"]]
                OLD.copy_bound(folder/FINAL,out/FINAL,entries[FINAL])
        save(out/"resume-import-receipt.json",{
            "result":RESULT,"complete":True,"source":resume,
            "original_manifest":spec(folder/MANIFEST),
            "mathematical_configuration_sha256":fingerprint(tag),
            "restored_mathematical_stage_count":len(names),
            "old_complete_inverse_coordinates_and_verifications_reused":True,
            "incomplete_old_final_did_not_constrain_later_current":True,
            "range_transport":archive.receipt()})
    finally:
        archive.close()

def output_manifest(out):
    files=[]
    for path in sorted(Path(out).iterdir()):
        if not path.is_file() or path.name in (MANIFEST,REFERENCE) or path.name.endswith((".tmp",".download")):
            continue
        files.append(spec(path))
    value={"result":RESULT,"files":files,"file_count":len(files),
           "temporary_active_checkpoint_retention_days":1}
    save(Path(out)/MANIFEST,value)
    save(Path(out)/REFERENCE,{"result":RESULT,"manifest":spec(Path(out)/MANIFEST)})
    return spec(Path(out)/MANIFEST)

def compute(item,out,request):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    source=subprocess.check_output(["git","rev-parse","HEAD"],cwd=REPO,text=True).strip()
    initial={"result":RESULT,"source_repository":REPOSITORY,"source_commit":source,
             "core_sha256":item["core_sha256"],"wrapper_sha256":sha(__file__),
             "job":item,"request_sha256":sha(request),
             "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
             "started_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
    save(out/"public-actions-input.json",initial)
    code,error,receipt=1,None,None
    try:
        restore(item,out)
        retained,expanded,receipt,review=prepare(item,out,True)
        initial["expanded_job"]=spec(out/EXPANDED)
        initial["mathematical_configuration_sha256"]=fingerprint(expected_tag(expanded))
        save(out/"public-actions-input.json",initial)
        command=[sys.executable,str(S/CORE),"--config",str(out/EXPANDED),"--retained",str(retained),
                 "--output",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"core.log").open("wb") as log:
            process=subprocess.Popen(command,cwd=REPO,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                code=process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid,signal.SIGTERM)
                try:
                    process.wait(timeout=40)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid,signal.SIGKILL);process.wait()
                code=124;error="OuterTimeout: only actual completed stages and actual receipts are retained."
    except BaseException as exc:
        error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    core=read(out/"core-receipt.json") if (out/"core-receipt.json").exists() else None
    complete=code==0 and core is not None and core["complete"] is True
    if core is not None:
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
    run={"result":RESULT,"source_commit":source,
         "workflow_run_id":os.environ["GITHUB_RUN_ID"],"workflow_run_attempt":os.environ["GITHUB_RUN_ATTEMPT"],
         "core_sha256":item["core_sha256"],"wrapper_sha256":sha(__file__),
         "complete":complete,"process_exit_code":code,
         "error":error if error is not None else (None if core is None else core.get("error")),
         "core_receipt_sha256":None if core is None else sha(out/"core-receipt.json"),
         "source_carriers_complete":receipt is not None,
         "finished_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
         "temporary_active_checkpoint_retention_days":1,
         "mathematical_files_saved_in_repository_or_release":False}
    save(out/"run-receipt.json",run)
    manifest=output_manifest(out)
    print("R882_RUN_RECEIPT="+json.dumps(dict(run,full_manifest=manifest),sort_keys=True),flush=True)
    return 0 if complete else (124 if code==124 else 1)

def dimensions(value,m,n):
    assert len(value)==m and all(len(row)==n for row in value)

def verify(item,out,request):
    out=Path(out);manifest=read(out/MANIFEST)
    assert manifest["result"]==RESULT
    entries={row["file"]:plain(row) for row in manifest["files"]}
    assert len(entries)==len(manifest["files"])
    for row in entries.values():
        bound(out,row)
    reference=read(out/REFERENCE)
    assert reference["result"]==RESULT and plain(reference["manifest"])==spec(out/MANIFEST)
    initial=read(out/"public-actions-input.json");run=read(out/"run-receipt.json")
    assert initial["result"]==run["result"]==RESULT
    assert initial["source_commit"]==run["source_commit"]
    assert initial["core_sha256"]==run["core_sha256"]==item["core_sha256"]
    assert initial["wrapper_sha256"]==run["wrapper_sha256"]==item["wrapper_sha256"]
    assert stable_request(initial["job"])==stable_request(item)
    needed=(BUNDLE,OLD_BUNDLE,INVENTORY,INPUT_RECEIPT,EXPANDED)
    if not all(n in entries for n in needed):
        assert run["complete"] is False
        print("R882_PARTIAL_IO_REVIEW="+json.dumps({"complete":False,"source_carriers_complete":False,
              "manifest":spec(out/MANIFEST),"error":run.get("error")},sort_keys=True),flush=True)
        return 2
    retained,expanded,receipt,review=prepare(item,out,False)
    assert spec(out/EXPANDED)==entries[EXPANDED]
    assert initial["expanded_job"]==entries[EXPANDED]
    tag=expected_tag(expanded)
    assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
    for name in entries:
        if name.startswith(PREFIX) and name.endswith(".json.gz"):
            value=read(out/name)
            assert value["result"]==RESULT and value["configuration"]==tag
            assert value["complete"] is (False if name==PREFIX+"current.json.gz" else True)
    core=None
    if "core-receipt.json" in entries:
        core=read(out/"core-receipt.json")
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
        if core["configuration"] is not None:
            assert core["configuration"]==tag
    else:
        assert run["core_receipt_sha256"] is None and run["complete"] is False
    if not run["complete"]:
        assert core is None or core["complete"] is False
        print("R882_PARTIAL_IO_REVIEW="+json.dumps({
            "complete":False,"process_exit_code":run["process_exit_code"],"error":run.get("error"),
            "full_manifest":spec(out/MANIFEST),"all_old_source_bytes_preserved":True,
            "actual_completed_stage_count":sum(n.startswith(PREFIX) and n.endswith(".json.gz") for n in entries),
            "new_mathematics_executed_by_verifier":False},sort_keys=True),flush=True)
        return 2
    assert core is not None and core["complete"] is True and run["process_exit_code"]==0
    certificate=read(out/FINAL)
    assert certificate["result"]==RESULT and certificate["configuration"]==tag and certificate["complete"] is True
    assert core["certificate_sha256"]==entries[FINAL]["sha256"]
    assert certificate["old_auxiliary_prime"]==739 and certificate["actual_auxiliary_prime"]==P
    assert certificate["original_zeta_root"]==549966761 and certificate["original_s_root"]==99932770
    assert certificate["actual_matrix_shape"]==[2200,2058] and certificate["actual_target_shape"]==[2200,17]
    for key in ("all17_same_exact_coefficient_expressions_reduced_at_common_place",
                "all2200_by17_original_equations_verified","both_complete_inverse_products_verified"):
        assert certificate[key] is True
    for key in ("old739_coordinates_or_inverse_relabelled","old_exact_norm_Berkowitz_or_q_tail_recomputed",
                "R879_reference_system_recomputed","old_Krylov_inverses_recomputed",
                "characteristic_zero_coefficients_expanded","target_normal_basis_computed",
                "nine_reference_norms_computed","original_Picard_support_computed",
                "height_or_nonp_calibration_computed"):
        assert certificate[key] is False
    def stage(row):
        row=plain(row);assert entries[row["file"]]==row
        value=read(bound(out,row))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        return value
    inventory=stage(certificate["stage_manifest"])
    for row in inventory["files"]:
        assert entries[row["file"]]==plain(row)
    for row in inventory["current_checkpoints"]:
        assert entries[row["file"]]==plain(row)
        assert read(out/row["file"])["complete"] is False
    audit=stage(certificate["source_audit"])
    assert audit["inputs"]==expanded["inputs"] and audit["old_mod739_coordinates_not_used_as_mod1000000753"] is True
    index=stage(certificate["original_matrix_index"])
    assert index["matrix_shape"]==[2200,2058]
    expected=0
    for row in index["matrix_column_blocks"]:
        block=stage(row);first,stop=block["column_interval"]
        assert first==expected and stop==min(2058,first+64)
        dimensions(block["matrix_mod_prime"],2200,stop-first)
        assert len(block["original_column_sources"])==stop-first
        assert block["only_new_modular_reduction"] is True and block["old_q_coefficients_recomputed"] is False
        expected=stop
    assert expected==2058
    rhs=stage(index["right_hand_side"]);dimensions(rhs["matrix_mod_prime"],2200,17)
    inverse=stage(certificate["new_complete_unit_inverse"])
    dimensions(inverse["inverse_matrix_mod_prime"],2058,2058)
    assert inverse["both_complete_inverse_products_verified"] is True
    assert inverse["old_mod739_inverse_reused"] is False
    assert inverse["new_complete_mod1000000753_inverse_computed"] is True
    assert inverse["selected_coordinate_rows"]==index["selected_coordinate_rows"]
    assert 0<inverse["actual_determinant_mod_prime"]<P
    assert certificate["actual_new_minor_determinant"]==inverse["actual_determinant_mod_prime"]
    coordinate=stage(certificate["seventeen_coordinates"])
    dimensions(coordinate["coordinate_matrix_mod_prime"],2058,17)
    assert coordinate["source_inverse"]==certificate["new_complete_unit_inverse"]
    assert coordinate["same_characteristic_zero_coefficients_integral_at_new_place"] is True
    complete=stage(certificate["same_place_correspondence_coefficients"])
    assert complete["new_modular_coordinates"]==certificate["seventeen_coordinates"]
    assert complete["new_complete_inverse"]==certificate["new_complete_unit_inverse"]
    assert complete["source_R873_correspondence_DAG"]==expanded["inputs"]["correspondence_DAG"]
    expected=0
    for row in complete["full_verification_stages"]:
        value=stage(row);first,stop=value["coordinate_row_interval"]
        assert first==expected and stop==min(2200,first+64)
        assert value["target_columns"]==list(range(17))
        assert value["all_original_rows_and_all17_targets_verified"] is True
        assert value["source_coordinates"]==certificate["seventeen_coordinates"]
        expected=stop
    assert expected==2200 and complete["all2200_by17_original_equations_verified"] is True
    print("R882_COMPLETE_IO_REVIEW="+json.dumps({
        "complete":True,"certificate":entries[FINAL],"full_manifest":spec(out/MANIFEST),
        "new_auxiliary_prime":P,"old_auxiliary_prime":739,
        "actual_nonzero2058_minor_determinant":inverse["actual_determinant_mod_prime"],
        "new_complete_inverse":certificate["new_complete_unit_inverse"],
        "seventeen_coordinates":certificate["seventeen_coordinates"],
        "same_place_correspondence_coefficients":certificate["same_place_correspondence_coefficients"],
        "all2200_by17_original_relations_verified":True,
        "old_exact_norm_or_q_tail_recomputed":False,
        "selected_stage_bundle":entries[BUNDLE],"unchanged_original_carrier":entries[OLD_BUNDLE],
        "original_source_inventory":entries[INVENTORY],"stage_manifest":certificate["stage_manifest"],
        "target_normal_basis_computed":False,"nine_reference_norms_computed":False,
        "seconds":certificate["seconds"],"new_mathematics_executed_by_verifier":False},
        sort_keys=True),flush=True)
    return 0

def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("mode",choices=("compute","verify"))
    parser.add_argument("--request",default=str(REQUEST))
    parser.add_argument("--output",required=True)
    args=parser.parse_args();request=Path(args.request)
    raw=read(request);item=raw.get("job",raw)
    guard(item,request)
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    raise SystemExit(compute(item,out,request) if args.mode=="compute" else verify(item,out,request))

if __name__=="__main__":
    main()
