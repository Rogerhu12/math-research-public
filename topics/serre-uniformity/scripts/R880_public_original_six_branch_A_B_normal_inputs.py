#!/usr/bin/env python3
"""R880 six-branch source transport, resumable run and pure-IO certificate review."""
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import traceback

S=Path(__file__).resolve().parent
REPO=S.parents[2]
TOPIC=REPO/"topics/serre-uniformity"
REQUEST=TOPIC/"notes/R880-six-branch-A-B-public-request.json"
LEGACY_IO_SHA="a574bd4fa95c2d80b1b6b6037f7e944a0c9f79660b7c4667ac99e97be3507221"
LEGACY_CORE_SHA="a40ed5b1bbb27b29cb54c94dca36322276c17c4534f43134e422acbb6f33983a"
LEGACY_IO=S/"R877_public_original_canonical_A_normal_input.py"
assert hashlib.sha256(LEGACY_IO.read_bytes()).hexdigest()==LEGACY_IO_SHA
_loader=importlib.util.spec_from_file_location("R880_six_frozen_R877_standard_library_IO",LEGACY_IO)
W=importlib.util.module_from_spec(_loader);_loader.loader.exec_module(W)
sha,read,save,fingerprint,plain,spec,bound=W.sha,W.read,W.save,W.fingerprint,W.plain,W.spec,W.bound
identity,stable_source,topic_path=W.identity,W.stable_source,W.topic_path
RESULT="R880-original-six-branch-A-B-normal-inputs"
FINAL="p41-original-six-branch-A-B-normal-inputs-certificate.json"
PREFIX="R880-six-branch-"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
INVENTORY=PREFIX+"original-source-inventory.json"
RETAINED_RECEIPT=PREFIX+"retained-inputs-receipt.json"
SELECTION_FILE="R880-six-branch-source-selection.json"
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
SOURCES=("R877","R824","R827","R842","R787","R849")
PROOFS=("R880","GP")
INPUTS=("canonical_coefficients","B_normal","S5_inverse","S5_matrix","global_DAG",
        "place_audit","original_chart","original_rational_blocks","original_selection",
        "parent_source_audit","parent_normal_A","parent_normal_fraction","parent_full_rhs","R824_chart")
EPS=[0]+[1]*144+[2]*127
PRIME,DIM,ROWS,RANK=1000000753,1234,1380,272
STRATEGY={
    "scope":"six_remaining_original_same_s_branches_twelve_A_B_normal_RHSs",
    "prime":PRIME,"original_branch0":0,"original_s_root":99932770,
    "original_zeta_root":549966761,"canonical_free_column":1186,
    "branch_order":"original roots_B_s indices; sigma powers computed from original R849 sigma(b)",
    "source_A_C":"original reserved R787 direction copied into completed R824 profiles",
    "B_expansion":"original Z_pivot_integer_rows and Z_free_diagonal, once",
    "source_F69":"twenty complete original R877 prefix-column stages",
    "S5_matrix":"completed original R842 1380 by 1234 matrix",
    "S5_inverse":"completed original R827 prime753 selected inverse",
    "new_rhs_count":12,"prefix_blocks":69,"real_coordinates_per_block":20,
    "source_column_chunk_size":64,"all1380_by12_original_coordinates_required":True,
    "normal_polynomial_bound":"5-epsilon_output",
    "original_branch0_A_B_recomputed":False,
    "original_Fourier_rows_or_F69_recomputed":False,
    "original_1186_inverse_or_Dixon_recomputed":False,
    "original_S5_inverse_recomputed":False,"additional_original_scale_inserted":False,
    "characteristic_zero_coordinates_reconstructed":False,
    "original_Dstar_pencils_or_five_Lj_RR_spaces_computed":False,
    "only_budget_and_transport_excluded_from_mathematical_identity":True,
}

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "method_sha256":item["method_sha256"],"legacy_R877_core_sha256":LEGACY_CORE_SHA,
        "proofs_sha256":{key:item["proofs"][key]["sha256"] for key in PROOFS},
        "sources":{label:stable_source(item["sources"][label]) for label in SOURCES},
        "inputs":item["inputs"],"prefix_groups":item["prefix_groups"],
        "branch_profiles":item["branch_profiles"],"normal_basis_degrees":EPS,"strategy":STRATEGY}

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
    assert request.resolve()==REQUEST.resolve()
    assert item["schema"]==1 and item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["core"]=="R880_original_six_branch_A_B_normal_inputs.py"
    assert sha(S/item["core"])==item["core_sha256"]
    assert item["legacy_R877_core_sha256"]==LEGACY_CORE_SHA
    assert sha(S/"R877_original_canonical_A_normal_input.py")==LEGACY_CORE_SHA
    assert item["legacy_R877_IO_sha256"]==LEGACY_IO_SHA
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    assert set(item["proofs"])==set(PROOFS)
    for proof in item["proofs"].values():
        assert sha(topic_path(proof["path"]))==proof["sha256"]
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert isinstance(item["session"],str) and item["session"]
    assert set(item["sources"])==set(SOURCES) and set(item["input_selectors"])==set(INPUTS)
    assert 0<item["budget_minutes"]<=300
    assert item["resume"] is None or isinstance(item["resume"],dict)
    return W.load_IO(item)

def output_manifest(out):
    entries=[dict(spec(path),included_in_git=False) for path in sorted(out.iterdir())
        if path.is_file() and path.name not in (MANIFEST,REFERENCE) and not path.name.endswith(".tmp")]
    save(out/MANIFEST,{"result":RESULT,"files":entries,
        "temporary_active_checkpoint_retention_days":1,"reproducible_data_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,**spec(out/MANIFEST)})

def inspect_manifest(out):
    manifest=read(out/MANIFEST);assert manifest["result"]==RESULT
    files={entry["file"]:plain(entry) for entry in manifest["files"]}
    assert len(files)==len(manifest["files"])
    actual={path.name for path in out.iterdir() if path.is_file()
            and path.name not in (MANIFEST,REFERENCE) and not path.name.endswith(".tmp")}
    assert actual==set(files)
    for entry in files.values():bound(out,entry)
    reference=read(out/REFERENCE)
    assert reference["result"]==RESULT and plain(reference)==spec(out/MANIFEST)
    return files

def checked_index(item,folder):
    intake=item["intake"];index=read(bound(folder,intake["source_index"]))
    assert index["schema"]==1 and index["new_mathematics_executed"] is False and index["errors"]==[]
    assert str(index["workflow_run_id"])==str(intake["run_id"])
    assert index["source_commit"]==intake["source_commit"]
    assert index["request_sha256"]==intake["request_sha256"]
    entries={entry["label"]:entry for entry in index["sources"]}
    assert len(entries)==len(index["sources"])==6 and set(entries)==set(SOURCES)
    branch_spec=plain(index["branch_selection"])
    assert branch_spec["file"]==SELECTION_FILE
    return index,entries,branch_spec

def intake_from_archive(item,out,work,IO):
    intake=item["intake"];archive=IO.Archive(intake,work/"intake-transport",whole=True)
    try:
        ref=plain(intake["source_index"])
        archive.extract_bound(ref["file"],ref["sha256"],out/ref["file"],ref["bytes"])
        index,entries,selection=checked_index(item,out)
        wanted={ref["file"],selection["file"]}
        archive.extract_bound(selection["file"],selection["sha256"],out/selection["file"],selection["bytes"])
        for label in SOURCES:
            entry=entries[label]
            assert identity(entry["source"])==identity(item["sources"][label])
            for kind in ("summary","retained_input_bundle"):
                ref=plain(entry[kind]);wanted.add(ref["file"])
                archive.extract_bound(ref["file"],ref["sha256"],out/ref["file"],ref["bytes"])
            assert plain(entry["retained_input_bundle"])==plain(intake["bundles"][label])
        assert len(wanted)==14 and set(archive.by_name)==wanted
        return archive.receipt()
    finally:archive.close()

def prepare_sources(item,out,work):
    intake=item["intake"];index,entries,selection_spec=checked_index(item,out)
    selection=read(bound(out,selection_spec))
    assert selection["schema"]==1 and selection["new_mathematics_executed"] is False
    assert selection["prime"]==PRIME and selection["original_s_root"]==99932770
    assert selection["original_zeta_root"]==549966761 and selection["canonical_free_column"]==1186
    assert selection["new_right_hand_sides_requested"]==12
    assert selection["original_same_s_branch_indices"]==list(range(7))
    assert selection["remaining_branch_indices"]==list(range(1,7))
    assert selection["complete_original_F69_column_count"]==DIM and selection["prefix_row_count"]==ROWS
    assert selection["all_selected_stage_bytes_and_SHA_verified"] is True
    assert selection["arithmetic_Galois_orbit_order_still_to_be_certified_by_new_consumer"] is True
    for key in ("old_F69_rows_recomputed","original_1186_direction_recomputed","original_S5_inverse_recomputed"):
        assert selection[key] is False
    sources={};tags={};total=0
    for label in SOURCES:
        raw=item["sources"][label];entry=entries[label]
        assert identity(entry["source"])==identity(raw)
        summary=read(bound(out,entry["summary"]))
        assert summary["label"]==label and summary["original_result"]==raw["result"]
        assert summary["new_mathematics_executed"] is False and summary["source"]==entry["source"]
        assert summary["manifest"]["sha256"]==raw["manifest_sha256"]
        assert summary["manifest"]["bytes"]==raw["manifest_bytes"]
        assert summary["original_manifest_count"]==raw["manifest_file_count"]
        assert summary["source_core_sha256"]==raw["core_sha256"]
        assert summary["source_wrapper_sha256"]==raw["wrapper_sha256"]
        if "source_configuration_sha256" in summary:
            assert summary["source_configuration_sha256"]==raw["configuration_sha256"]
        carrier=plain(entry["retained_input_bundle"])
        assert carrier==plain(summary["retained_input_bundle"])==plain(intake["bundles"][label])
        files={name:plain(value) for name,value in summary["selected_files"].items()}
        assert len(files)==summary["selected_file_count"]
        assert MANIFEST not in files and REFERENCE not in files
        files[MANIFEST]=plain(summary["manifest"]);files[REFERENCE]=plain(summary["manifest_reference"])
        assert set(files)==set(raw["selected_file_names"])
        assert len(files)==raw["expected_selected_file_count"]
        for name,pin in raw.get("file_pins",{}).items():assert files[name]==plain(pin)
        directory=work/"retained"/label
        W.unpack_source(bound(out,carrier),directory,files)
        value=dict(raw,directory=str(directory),files=files,selected_file_count=len(files),
                   selected_files_sha256=fingerprint(files))
        tags[label]=W.review_original(label,value);sources[label]=value;total+=len(files)
    assert total==80
    assert fingerprint(tags["R877"])==selection["original_R877_configuration_sha256"]
    assert fingerprint(tags["R824"])==selection["original_R824_configuration_sha256"]
    for label in ("R827","R842","R787","R849"):
        assert fingerprint(tags[label])==selection["old_source_configuration_sha256"][label]
        assert identity(tags["R877"]["sources"][label])==identity(sources[label])
        assert tags["R877"]["sources"][label]["configuration_sha256"]==sources[label]["configuration_sha256"]
    for label in ("R824","R827","R849"):
        assert identity(tags[label]["source_identities"]["R787"])==identity(sources["R787"])
    assert plain(selection["source_selection"])==sources["R787"]["files"]["R787-prime-1000000753-selection.json.gz"]
    assert plain(selection["existing_original_branch0_R877_certificate"])==plain(sources["R877"]["certificate"])
    inputs={}
    for key,selector in item["input_selectors"].items():
        label,name=selector["source_group"],selector["file"]
        assert label in sources and name in sources[label]["files"]
        inputs[key]={"source_group":label,**sources[label]["files"][name]}
        for field in ("bytes","sha256"):
            if field in selector:assert inputs[key][field]==selector[field]
    assert set(inputs)==set(INPUTS)
    prefixes=[]
    recorded=selection["completed_F69_prefix_groups"];assert len(recorded)==20
    for first,entry in zip(range(0,DIM,64),recorded):
        name=f"R877-original-V5-prefix-and-A-part-{first:04d}-{min(first+64,DIM):04d}.json.gz"
        ref=plain(entry)
        assert ref["file"]==name and sources["R877"]["files"][name]==ref
        prefixes.append({"source_group":"R877",**ref})
    branches=[]
    profiles=selection["remaining_A_B_profiles"];assert len(profiles)==6
    assert [row["original_branch"] for row in profiles]==selection["remaining_branch_indices"]
    for record in profiles:
        branch=record["original_branch"];ref=plain(record["source_profile"])
        assert ref["file"]==f"R824-power5-prime-{PRIME}-branch-{branch:02d}.json.gz"
        assert sources["R824"]["files"][ref["file"]]==ref
        assert record["canonical_free_column"]==1186 and record["recorded_unit_minor_determinant"]!=0
        assert record["recorded_original_reserved_column_retained_without_new_lift"] is True
        assert record["roots_B_s"]==selection["original_roots_B_s"][branch]
        assert record["stored_A_shape"]==[1234,28] and record["stored_C_shape"]==[1214,28]
        branches.append({"original_branch":branch,"source":{"source_group":"R824",**ref}})
    expanded=dict(item,sources=sources,inputs=inputs,prefix_groups=prefixes,branch_profiles=branches)
    expanded["method"]=str(topic_path(item["method"]))
    expanded["proofs"]={key:{**value,"path":str(topic_path(value["path"]))} for key,value in item["proofs"].items()}
    stable={label:stable_source(value) for label,value in sources.items()}
    inventory={"result":RESULT,"source_identities":stable,
        "selected_files":{label:value["files"] for label,value in sources.items()},
        "actual_selected_source_count":total,"new_mathematics_executed":False}
    receipt={"result":RESULT,"complete":True,"intake":intake,"source_index":plain(intake["source_index"]),
        "source_selection":selection_spec,
        "summaries":{label:plain(entries[label]["summary"]) for label in SOURCES},
        "original_carriers":{label:plain(entries[label]["retained_input_bundle"]) for label in SOURCES},
        "original_source_identities":stable,"actual_selected_source_count":total,
        "completed_original_F69_chunk_count":20,"selected_original_remaining_profile_count":6,
        "all_selected_original_members_bytes_and_SHA_verified":True,
        "source_arithmetic_recomputed":False,"new_mathematics_executed":False}
    save(out/INVENTORY,inventory);save(out/RETAINED_RECEIPT,receipt)
    return expanded,receipt

def restore_archive(item,out,work,IO):
    source=item["resume"]
    if source is None:return None
    assert source["result"]==RESULT and source["core_sha256"]==item["core_sha256"]
    assert source["wrapper_sha256"]==item["wrapper_sha256"]
    archive=IO.Archive(source,work/"resume-transport",whole=True)
    folder=work/"previous-output";folder.mkdir(parents=True,exist_ok=True)
    try:
        manifest_spec=plain(source["manifest"])
        assert manifest_spec["file"]==MANIFEST
        archive.extract_bound(MANIFEST,manifest_spec["sha256"],folder/MANIFEST,manifest_spec["bytes"])
        manifest=read(folder/MANIFEST);assert manifest["result"]==RESULT
        files={value["file"]:plain(value) for value in manifest["files"]}
        assert len(files)==len(manifest["files"])
        assert set(archive.by_name)==set(files)|{MANIFEST,REFERENCE}
        for ref in files.values():
            archive.extract_bound(ref["file"],ref["sha256"],folder/ref["file"],ref["bytes"])
        entry=archive.by_name[REFERENCE];assert len(entry)==1 and entry[0].file_size<1000000
        (folder/REFERENCE).write_bytes(archive.zip.read(entry[0]))
        reference=read(folder/REFERENCE)
        assert reference["result"]==RESULT and plain(reference)==manifest_spec
        old=read(folder/META[0]);run=read(folder/META[1])
        assert old["result"]==run["result"]==RESULT
        assert old["source_commit"]==run["source_commit"]==source["source_commit"]
        assert str(run["workflow_run_id"])==str(source["run_id"])
        assert old["core_sha256"]==item["core_sha256"] and old["driver_sha256"]==item["wrapper_sha256"]
        if run.get("core_receipt_sha256") is not None:
            assert files[META[2]]["sha256"]==run["core_receipt_sha256"]
            cr=read(folder/META[2])
            assert cr["result"]==RESULT and cr["source_sha256"]==item["core_sha256"]
            assert cr["configuration_sha256"] in (None,fingerprint(old["actual_configuration"]))
        else:assert run["complete"] is False
        index,entries,selection=checked_index(item,folder)
        needed=[plain(item["intake"]["source_index"]),selection]
        for entry in index["sources"]:
            needed.extend([plain(entry["summary"]),plain(entry["retained_input_bundle"])])
        assert len(needed)==14
        for ref in needed:
            assert files[ref["file"]]==ref
            target=out/ref["file"]
            if target.exists():assert spec(target)==ref
            else:shutil.copyfile(bound(folder,ref),target)
        return {"folder":folder,"files":files,"initial":old,"run":run,"transport":archive.receipt()}
    finally:archive.close()

def restore_stages(previous,tag,out):
    if previous is None:return
    assert previous["initial"]["actual_configuration"]==tag
    folder,files=previous["folder"],previous["files"]
    for name,ref in files.items():
        if not(name.startswith(PREFIX) and name.endswith(".json.gz")):continue
        value=read(folder/name)
        assert value["result"]==RESULT and value["configuration"]==tag
        assert value["complete"] is (name!=PREFIX+"current.json.gz")
        target=out/name
        if target.exists():assert spec(target)==ref
        else:shutil.copyfile(folder/name,target)
    if FINAL in files:
        final=read(folder/FINAL)
        assert final["result"]==RESULT and final["configuration"]==tag
        if final["complete"] is True:
            assert previous["run"]["complete"] is True
            inventory=read(bound(folder,final["stage_manifest"]))
            assert inventory["result"]==RESULT and inventory["configuration"]==tag and inventory["complete"] is True
            for ref in inventory["files"]:
                assert files[ref["file"]]==plain(ref);bound(out,ref)
            for key in ("source_audit","original_Galois_orbit","full1380_rhs","all_twelve_normal_solves",
                        "seven_Galois_normal_inputs","resume_state"):
                bound(out,final[key])
            for key in ("original_coefficient_sources","new_normal_pairs"):
                for ref in final[key]:bound(out,ref)
            shutil.copyfile(folder/FINAL,out/FINAL)
        # A false FINAL remains only in the source archive; its inventory may be older than current.

def compute(item,out,request,IO):
    out.mkdir(parents=True,exist_ok=True)
    work=out.parent/"R880-six-branch-working";work.mkdir(parents=True,exist_ok=True)
    code=1;error=None;outer=False;expanded=None;tag=None;child=None;transport=None
    try:
        previous=restore_archive(item,out,work,IO)
        transport=previous["transport"] if previous is not None else intake_from_archive(item,out,work,IO)
        expanded,source_receipt=prepare_sources(item,out,work)
        tag=expected_tag(expanded);restore_stages(previous,tag,out)
        config=work/"expanded-job.json";save(config,expanded)
        initial={"result":RESULT,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_sha256":item["core_sha256"],"driver_sha256":item["wrapper_sha256"],
            "request_sha256":sha(request),"job":item,"actual_configuration":tag,
            "actual_source_inventory":spec(out/INVENTORY),"retained_inputs":spec(out/RETAINED_RECEIPT),
            "transport":transport,"root_readme_sha256":item["readme_sha256"]["root"],
            "topic_readme_sha256":item["readme_sha256"]["topic"],
            "execution_environment":"public-repository-github-actions"}
        save(out/META[0],initial)
        command=[sys.executable,"-u",str(S/item["core"]),"--config",str(config),
                 "--out",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"core.log").open("ab",buffering=0) as log:
            child=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:code=child.wait(timeout=60*item["budget_minutes"]+180)
            except subprocess.TimeoutExpired:
                outer=True;code=124;os.killpg(child.pid,signal.SIGTERM)
                try:child.wait(timeout=15)
                except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
        if code<0:code=128-code
        if (out/"core.log").exists():
            for line in (out/"core.log").read_text(errors="replace").splitlines()[-18:]:
                if len(line)<=2400:print(line,flush=True)
        if (out/META[2]).exists():
            print("R880_SIX_BRANCH_CORE_RECEIPT="+json.dumps(read(out/META[2]),sort_keys=True),flush=True)
    except BaseException as exc:
        traceback.print_exc();error={"type":type(exc).__name__,"message":str(exc)};code=1
    finally:
        core=read(out/META[2]) if (out/META[2]).exists() else None
        final=read(out/FINAL) if (out/FINAL).exists() else None
        complete=bool(code==0 and core and core["complete"] and final and final["complete"])
        save(out/META[1],{"result":RESULT,"p":41,"complete":complete,"process_exit_code":code,
            "error":error,"outer_timeout":outer,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],
            "workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_receipt_sha256":sha(out/META[2]) if core is not None else None,
            "all_seven_original_Galois_normal_inputs_certified":bool(final and final["all_seven_original_Galois_normal_inputs_certified"]),
            "all1380_by12_original_coordinates_verified":bool(final and final["all1380_by12_original_coordinates_verified"]),
            "original_five_Lj_RR128_or_144_computed":False,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    return code

def dimensions(value,n,m):
    assert isinstance(value,list) and len(value)==n
    assert all(isinstance(row,list) and len(row)==m for row in value)

def verify(item,out,request,IO):
    files=inspect_manifest(out);run=read(out/META[1])
    assert run["result"]==RESULT and run["source_commit"]==os.environ["GITHUB_SHA"]
    assert str(run["workflow_run_id"])==os.environ["GITHUB_RUN_ID"]
    if META[0] not in files:
        assert run["complete"] is False and run["process_exit_code"]!=0
        assert run["core_receipt_sha256"] is None
        print("R880_SIX_BRANCH_VERIFY="+json.dumps({"complete":False,"source_preparation_failed":True,
            "all_existing_output_bytes_verified":True,"new_mathematics_executed":False}),flush=True)
        return 0
    expanded,source_receipt=prepare_sources(item,out,out.parent/"R880-six-branch-verification")
    tag=expected_tag(expanded);initial=read(out/META[0])
    assert initial["result"]==RESULT and initial["source_commit"]==os.environ["GITHUB_SHA"]
    assert initial["core_sha256"]==item["core_sha256"] and initial["driver_sha256"]==item["wrapper_sha256"]
    assert initial["request_sha256"]==sha(request) and initial["job"]==item
    assert initial["actual_configuration"]==tag
    assert files[INVENTORY]==spec(out/INVENTORY) and files[RETAINED_RECEIPT]==spec(out/RETAINED_RECEIPT)
    assert initial["actual_source_inventory"]==files[INVENTORY] and initial["retained_inputs"]==files[RETAINED_RECEIPT]
    complete_stages={}
    for name,ref in files.items():
        if not(name.startswith(PREFIX) and name.endswith(".json.gz")):continue
        value=read(out/name)
        assert value["result"]==RESULT and value["configuration"]==tag
        if name==PREFIX+"current.json.gz":
            assert value["complete"] is False and isinstance(value["status"],str)
            assert 0<=value["next_original_prefix_chunk"]<=20
        else:
            assert value["complete"] is True
            if name!=PREFIX+"stage-manifest.json.gz":complete_stages[name]=ref
    def stage(ref):
        ref=plain(ref);assert files[ref["file"]]==ref
        value=read(bound(out,ref))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        return value
    def original(ref):
        label=ref["source_group"];assert label in SOURCES
        value=expanded["sources"][label];pin=plain(ref)
        assert value["files"][pin["file"]]==pin
        return read(bound(value["directory"],pin))
    core=read(out/META[2]) if META[2] in files else None
    if core is not None:
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        assert files[META[2]]["sha256"]==run["core_receipt_sha256"]
        assert core["configuration_sha256"] in (None,fingerprint(tag))
        assert core["old_branch0_A_B_F69_or_inverse_recomputed"] is False
        assert core["characteristic_zero_normal_coordinates_reconstructed"] is False
        assert core["original_five_Lj_RR128_or_144_computed"] is False
    else:
        assert run["complete"] is False and run["core_receipt_sha256"] is None
    final=read(out/FINAL) if FINAL in files else None
    if final is not None:
        assert final["result"]==RESULT and final["configuration"]==tag
        for key in ("old_branch0_A_B_F69_or_inverse_recomputed","characteristic_zero_normal_coordinates_reconstructed",
                    "all_seven_Dstar_pencils_computed","original_five_Lj_RR128_or_144_computed",
                    "connection_Poincare_period_or_height_computed"):
            assert final[key] is False
        if final["complete"]:
            assert run["complete"] is True and run["process_exit_code"]==0 and run["error"] is None
            assert core is not None and core["complete"] is True and core["exit_code"]==0 and core["error"] is None
            assert core["certificate_sha256"]==files[FINAL]["sha256"] and core["configuration_sha256"]==fingerprint(tag)
            assert final["p"]==41 and final["prime"]==PRIME and final["stop_reason"] is None
            for key in ("all_seven_original_Galois_normal_inputs_certified","all1380_by12_original_coordinates_verified"):
                assert final[key] is core[key] is run[key] is True
            assert final["original_Galois_seven_cycle_certified"] is True
            assert final["new_right_hand_side_count"]==core["new_right_hand_side_count"]==12
            assert final["actual_new_normal_pair_count"]==6
            inventory=stage(final["stage_manifest"])
            indexed={ref["file"]:plain(ref) for ref in inventory["files"]}
            assert len(indexed)==len(inventory["files"]) and indexed==complete_stages
            assert inventory["current_excluded"] is True and inventory["all_complete_stages_retained"] is True
            assert plain(final["resume_state"])==files[PREFIX+"current.json.gz"]
            current=read(bound(out,final["resume_state"]))
            assert current["seven_Galois_normal_inputs"]==final["seven_Galois_normal_inputs"]
            assert current["all12_normal_solve"]==final["all_twelve_normal_solves"]
            assert current["coefficient_sources"]==final["original_coefficient_sources"]
            assert current["normal_pairs"]==final["new_normal_pairs"]
            audit=stage(final["source_audit"])
            assert audit["prime"]==PRIME and audit["canonical_free_column"]==1186
            assert audit["original_s_root"]==99932770 and audit["original_zeta_root"]==549966761
            assert audit["original_branch0"]==0 and audit["remaining_original_branch_indices"]==list(range(1,7))
            for label in ("R877","R824"):
                assert audit["source_completed_"+label]=={"source_group":label,**plain(expanded["sources"][label]["certificate"])}
            for output_key,input_key in (
                ("source_original_S5_inverse","S5_inverse"),("source_original_S5_matrix","S5_matrix"),
                ("source_original_R787_chart","original_chart"),("source_original_R787_selection","original_selection"),
                ("source_original_Z","original_rational_blocks"),("source_original_global_DAG","global_DAG")):
                assert audit[output_key]==expanded["inputs"][input_key]
            assert audit["completed_prefix_groups"]==expanded["prefix_groups"]
            assert audit["source_branch_profiles"]==expanded["branch_profiles"]
            assert audit["original_V5_integer_scale"]=="13744803133596058624"
            for key in ("same_original_unit_chart_and_free1186_direction_certified",
                        "old_F69_and_S5_inverse_are_complete_bound_inputs","branch0_A_B_read_without_recomputation"):
                assert audit[key] is True
            assert audit["arbitrary_modular_kernel_lift_used"] is False and audit["new_normalized_Dixon_digits_computed"]==0
            orbit=stage(final["original_Galois_orbit"])
            assert orbit["prime"]==PRIME and orbit["actual_order"]==7
            assert orbit["source_audit"]==final["source_audit"]
            assert orbit["source_original_selection"]==expanded["inputs"]["original_selection"]
            assert orbit["source_original_Galois_DAG"]==expanded["inputs"]["global_DAG"]
            assert orbit["source_original_Galois_node"]==audit["source_original_Galois_node"]
            assert orbit["original_s_root"]==99932770 and orbit["original_zeta_root"]==549966761
            for key in ("all_original_rational_denominators_used_here_are_units",
                        "fixes_original_z_w_and_normal_basis","branch_labels_not_assigned_by_guessing_sorted_roots"):
                assert orbit[key] is True
            cycle=orbit["original_same_s_seven_cycle"];assert len(cycle)==7
            assert [row["sigma_power"] for row in cycle]==list(range(7))
            assert cycle[0]["original_branch"]==0
            assert {row["original_branch"] for row in cycle}==set(range(7))
            _,_,selection_spec=checked_index(item,out)
            selection=read(bound(out,selection_spec));roots=selection["original_roots_B_s"]
            powers={}
            for i,row in enumerate(cycle):
                branch=row["original_branch"];powers[branch]=row["sigma_power"]
                assert row["roots_B_s"]==roots[branch]
                assert row["next_original_branch"]==cycle[(i+1)%7]["original_branch"]
                assert isinstance(row["original_b_reduction"],int) and isinstance(row["sigma_b_reduction"],int)
            coefficient_refs=final["original_coefficient_sources"]
            assert len(coefficient_refs)==6 and len(final["new_normal_pairs"])==6
            for j,ref in enumerate(coefficient_refs):
                branch=j+1;value=stage(ref)
                assert value["prime"]==PRIME and value["original_branch"]==branch
                assert value["sigma_power"]==powers[branch] and value["roots_B_s"]==roots[branch]
                assert value["canonical_free_column"]==1186
                assert value["source_original_profile"]==expanded["branch_profiles"][j]["source"]
                assert value["source_original_chart"]==expanded["inputs"]["original_chart"]
                assert value["source_original_rational_blocks"]==expanded["inputs"]["original_rational_blocks"]
                assert value["source_original_Galois_cycle"]==final["original_Galois_orbit"]
                recorded=selection["remaining_A_B_profiles"][j]
                assert value["canonical_column_position"]==recorded["canonical_column_position"]
                assert value["original_unit_minor_determinant_mod_prime"]==recorded["recorded_unit_minor_determinant"]
                assert plain(value["source_original_reserved_R787_branch"])==plain(recorded["source_original_R787_branch"])
                assert len(value["A_coefficients_mod_prime_in_original_V5_basis"])==DIM
                assert len(value["B_coefficients_mod_prime_in_original_V5_basis"])==DIM
                assert len(value["C_coefficients_mod_prime_in_original_constant_kernel"])==1214
                for key in ("all_original_free_coordinates_match_1186_normalization",
                            "source_reserved_A_C_not_recomputed","original_Z_expanded_once_for_this_new_B_RHS"):
                    assert value[key] is True
                assert value["original_common_clear_or_lambda_factor_inserted"] is False
                assert value["characteristic_zero_coefficients_reconstructed"] is False
                definition=value["characteristic_zero_coefficient_definition"]
                assert definition["operation"]=="apply_original_L_over_K_sigma_to_R849_unit_chart_solution"
                assert definition["source_original_DAG"]==expanded["inputs"]["global_DAG"]
                assert definition["sigma_power"]==powers[branch] and definition["original_free_column"]==1186
            labels=[{"original_branch":branch,"sigma_power":powers[branch],"target":target}
                    for branch in range(1,7) for target in ("A","B")]
            rhs=stage(final["full1380_rhs"])
            assert rhs["prime"]==PRIME and rhs["source_audit"]==final["source_audit"]
            assert rhs["source_original_coefficients"]==coefficient_refs and rhs["target_labels"]==labels
            assert rhs["matrix_shape"]==[ROWS,12]
            dimensions(rhs["right_hand_sides_mod_prime"],ROWS,12)
            assert rhs["original_constant_block_retained"] is True and rhs["all_six_B_constant_blocks_zero"] is True
            assert rhs["old_branch0_A_B_or_F69_recomputed"] is False
            assert len(rhs["source_parts"])==20
            for first,ref,source_ref in zip(range(0,DIM,64),rhs["source_parts"],expanded["prefix_groups"]):
                value=stage(ref)
                assert value["prime"]==PRIME and value["source_audit"]==final["source_audit"]
                assert value["first_column"]==first and value["stop_column"]==min(DIM,first+64)
                assert value["source_completed_F69_chunk"]==source_ref
                assert value["source_original_coefficients"]==coefficient_refs and value["target_labels"]==labels
                assert value["matrix_shape"]==[ROWS,12]
                dimensions(value["partial_right_hand_sides_mod_prime"],ROWS,12)
                assert value["original_F69_not_reduced_or_constructed_again"] is True
            solved=stage(final["all_twelve_normal_solves"])
            assert solved["prime"]==PRIME and solved["source_rhs"]==final["full1380_rhs"]
            assert solved["source_original_S5_matrix"]==expanded["inputs"]["S5_matrix"]
            assert solved["source_completed_S5_inverse"]==expanded["inputs"]["S5_inverse"]
            assert solved["target_labels"]==labels and solved["solution_shape"]==[DIM,12]
            dimensions(solved["S5_coordinates_mod_prime"],DIM,12)
            selected=solved["selected_row_indices"]
            assert len(selected)==len(set(selected))==DIM and all(0<=i<ROWS for i in selected)
            mapping=[[a,k] for a in range(RANK) for k in range(6-EPS[a])]
            assert solved["original_normal_basis_row_mapping"]==mapping
            for key in ("all1380_by12_original_coordinates_verified","all_twelve_original_reductions_nonzero",
                        "characteristic_zero_selected_unit_solve_defined"):
                assert solved[key] is True
            assert solved["old_S5_inverse_or_branch0_solve_recomputed"] is False
            assert solved["characteristic_zero_coordinates_reconstructed"] is False
            for j,ref in enumerate(final["new_normal_pairs"]):
                branch=j+1;value=stage(ref)
                assert value["prime"]==PRIME and value["original_branch"]==branch and value["sigma_power"]==powers[branch]
                assert value["roots_B_s"]==roots[branch] and value["original_zeta_root"]==549966761
                assert value["canonical_free_column"]==1186
                assert value["source_original_coefficients"]==coefficient_refs[j]
                assert value["source_all_twelve_normal_solves"]==final["all_twelve_normal_solves"]
                assert value["normal_basis_rank"]==RANK and value["normal_basis_degrees"]==EPS
                assert value["regular_degree_bound"]==5
                dimensions(value["A_vector_coefficients_mod_prime"],6,RANK)
                dimensions(value["B_vector_coefficients_mod_prime"],6,RANK)
                for key in ("all1380_original_coordinates_for_each_vector_verified",
                            "all_original_weighted_support_bounds_verified","same_original_82power10_scales_preserved",
                            "both_original_function_reductions_nonzero","abstract_p_integral_original_normal_lifts_certified"):
                    assert value[key] is True
                assert value["finite_fiber_B_invertibility_checked"] is False
                assert value["characteristic_zero_coordinates_reconstructed"] is False
                exact=value["exact_unit_solve_expression"]
                assert exact["operation"]=="original_S5_selected_unit_solve_for_sigma_A_and_B"
                assert exact["source_original_global_DAG"]==expanded["inputs"]["global_DAG"]
                assert exact["source_original_Galois_node"]==audit["source_original_Galois_node"]
                assert exact["sigma_power"]==powers[branch]
                assert exact["source_original_F69_chunks"]==expanded["prefix_groups"]
                assert exact["source_original_S5_matrix"]==expanded["inputs"]["S5_matrix"]
                assert exact["source_actual_selected_unit_inverse"]==expanded["inputs"]["S5_inverse"]
                assert exact["selected_row_indices"]==selected and exact["original_free_column"]==1186
                assert exact["original_scale_applied_again"] is False
            seven=stage(final["seven_Galois_normal_inputs"])
            assert seven["prime"]==PRIME and seven["source_audit"]==final["source_audit"]
            assert seven["source_original_Galois_cycle"]==final["original_Galois_orbit"]
            assert seven["source_original_global_DAG"]==expanded["inputs"]["global_DAG"]
            assert seven["original_s_root"]==99932770 and seven["original_zeta_root"]==549966761
            assert seven["normal_basis_rank"]==RANK and seven["normal_basis_degrees"]==EPS
            assert seven["regular_degree_bound"]==5 and seven["actual_normal_pair_count"]==7
            assert seven["new_right_hand_side_count"]==12
            for key in ("all_seven_original_Galois_normal_inputs_certified",
                        "same_original_unit_chart_normalization_for_every_branch",
                        "original_global_fraction_defined_by_exact_source_unit_solves"):
                assert seven[key] is True
            for key in ("all_other_s_branches_used","source_scales_changed","all_seven_Dstar_pencils_computed",
                        "original_five_Lj_RR128_or_144_computed","connection_rigidification_period_or_height_computed"):
                assert seven[key] is False
            ordered=seven["ordered_original_sigma_powers"]
            assert len(ordered)==7 and [row["sigma_power"] for row in ordered]==list(range(7))
            for row,cycle_row in zip(ordered,cycle):
                branch=row["original_branch"]
                assert branch==cycle_row["original_branch"] and row["roots_B_s"]==roots[branch]
                if branch==0:
                    assert row["source_original_A_normal"]==expanded["inputs"]["parent_normal_A"]
                    assert row["source_original_B_normal"]==expanded["inputs"]["B_normal"]
                    assert row["source_original_fraction"]==expanded["inputs"]["parent_normal_fraction"]
                    assert row["old_original_A_B_recomputed"] is False
                else:assert row["source_original_normal_pair"]==final["new_normal_pairs"][branch-1]
            assert len(complete_stages)==37
        else:
            assert run["complete"] is False
            # False FINAL references are historical; all actual retained stages and current were checked above.
    if run["complete"]:assert final is not None and final["complete"] is True
    print("R880_SIX_BRANCH_VERIFY="+json.dumps({"result":RESULT,"complete":bool(final and final["complete"]),
        "actual_selected_source_count":source_receipt["actual_selected_source_count"],
        "actual_complete_math_stage_count":len(complete_stages),
        "all_seven_original_Galois_normal_inputs_certified":bool(final and final["all_seven_original_Galois_normal_inputs_certified"]),
        "all1380_by12_original_coordinates_verified":bool(final and final["all1380_by12_original_coordinates_verified"]),
        "old_branch0_A_B_F69_or_inverse_recomputed":False,"original_five_Lj_RR128_or_144_computed":False,
        "new_mathematics_executed_in_verifier":False},sort_keys=True),flush=True)
    return 0

def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("compute","verify"))
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    item=read(args.request);IO=guard(item,args.request)
    try:
        code=compute(item,args.output,args.request,IO) if args.mode=="compute" else verify(item,args.output,args.request,IO)
    except BaseException:
        traceback.print_exc();raise
    raise SystemExit(code)

if __name__=="__main__":main()
