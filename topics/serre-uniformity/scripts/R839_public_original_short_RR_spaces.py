#!/usr/bin/env python3
"""Public source-bound runner for R839; standard-library IO only."""
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
import tarfile

S=Path(__file__).resolve().parent
REPO=S.parents[2]
TOPIC=REPO/"topics/serre-uniformity"
REQUEST=TOPIC/"notes/R839-short-RR-public-request.json"
RESULT="R839-original-short-RR-spaces-and-D-kernel"
FINAL="p41-original-short-RR-and-D-kernel-certificate.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R839-retained-original-inputs.tar.gz"
INVENTORY="R839-original-source-inventory.json"
INPUT_RECEIPT="R839-retained-inputs-receipt.json"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
BASE_KEYS=("result","run_id","source_commit","core_sha256","manifest_sha256","configuration_sha256")
PROOFS=("proof","method")
PREFIX="R839-"
H64=re.compile(r"[0-9a-f]{64}")
IO=None
SOURCES=("R827","R838","R837","R809","R786")
EPS=[0]+[1]*144+[2]*127
FLAGS=("exact_original_T11_as_unit_chart_expression_certified",
       "exact_original_T5_quotient_as_unit_chart_expression_certified",
       "exact_original_D_RR_space_as_unit_chart_expression_certified")
CERTIFICATES={
 "R827":None,
 "R838":"p41-original-order2-colength-certificate.json",
 "R837":"p41-original-fixed-branch-pencil-certificate.json",
 "R809":"p41-original-S5-normal-coordinate-certificate.json",
 "R786":"p41-exact-original-power5-short-basis-certificate.json"}
LAYER_INDEXES=("R827-target-B-tau-polynomial-index.json.gz",
 "R827-tau-layer-001-precision-0010-index.json.gz",
 "R827-tau-layer-002-precision-0012-index.json.gz")
R827_EXTRA=("R827-canonical-B-normal-vector.json.gz",
 "R827-canonical-B-original-V5-expansion.json.gz",
 "R827-complete-short-operator-identities-and-sigma-transport.json.gz",
 "R827-original-place-and-unit-source-audit.json.gz",
 "R827-original-two-chart-C-reduction.json.gz",
 "R827-prime-1000000753-S5-fixed-minor-inverse.json.gz",
 "R827-sigma-infinity-order-0004-certificate.json.gz")
SCOPE={
 "auxiliary_prime":1000000753,"original_branch":0,
 "normal_basis_rank":272,"normal_basis_degrees":EPS,
 "uniform_homogeneous_weight":11,"source_derivative_orders":[0,1,2],
 "source_generator_order":"derivative_order, original_normal_basis_index, z_shift",
 "target_normal_row_order":"normal_basis_index outer; z_degree increasing",
 "T11_matrix_shape":[2866,2886],"T11_required_rank":2451,
 "T5_matrix_shape":[830,1234],"T5_required_rank":415,
 "D_matrix_shape":[830,690],"D_required_rank":395,"D_RR_dimension":295,
 "source_coordinate_order":"20*qY_exponent+t_degree; v=xi^-10*qY",
 "original_V2_integer_scale":"45212176",
 "original_V3_integer_scale":"304006671424",
 "original_V5_integer_scale":"13744803133596058624",
 "product_group_size":17,"old_derivatives_and_same_prime_S5_inverse_recomputed":False,
 "accurate_characteristic_zero_objects_are_source_bound_unit_solve_expressions":True,
 "budget_excluded_from_mathematical_identity":True}


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(4*1024*1024),b""):h.update(block)
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

def safe_name(value):
    assert isinstance(value,str) and Path(value).name==value and value not in (".","..")
    assert "\\" not in value
    return value

def plain(value):
    row={k:value[k] for k in ("file","bytes","sha256")}
    safe_name(row["file"])
    assert isinstance(row["bytes"],int) and row["bytes"]>=0 and H64.fullmatch(row["sha256"])
    return row

def file_spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}

def bound(folder,row):
    row=plain(row);p=Path(folder)/row["file"]
    assert file_spec(p)==row,("Changed bound bytes",p.name)
    return p

def topic_path(value):
    value=PurePosixPath(value)
    assert not value.is_absolute() and ".." not in value.parts
    path=(TOPIC/str(value)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path

def pack_sources(retained,inventory,target):
    retained=Path(retained);tmp=target.with_name(target.name+".tmp")
    with tmp.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw,mode="wb",mtime=0,compresslevel=2) as gz:
            with tarfile.open(fileobj=gz,mode="w|") as tar:
                for label,source in sorted(inventory["sources"].items()):
                    for name,row in sorted(source["files"].items()):
                        p=bound(retained/label,row)
                        info=tar.gettarinfo(str(p),arcname=label+"/"+name)
                        info.uid=info.gid=0;info.uname=info.gname="";info.mtime=0
                        with p.open("rb") as f:tar.addfile(info,f)
    tmp.replace(target)

def unpack_sources(path,retained,inventory):
    retained=Path(retained)
    wanted={label+"/"+name:plain(row)
            for label,source in inventory["sources"].items() for name,row in source["files"].items()}
    seen=set()
    with tarfile.open(path,"r:gz") as tar:
        for member in tar:
            assert member.isfile() and not member.issym() and not member.islnk()
            name=PurePosixPath(member.name)
            assert not name.is_absolute() and ".." not in name.parts and len(name.parts)==2
            assert member.name in wanted and member.name not in seen
            seen.add(member.name);row=wanted[member.name]
            assert member.size==row["bytes"]
            dest=retained/member.name;dest.parent.mkdir(parents=True,exist_ok=True)
            tmp=dest.with_name(dest.name+".tmp");h=hashlib.sha256();count=0
            with tar.extractfile(member) as src,tmp.open("wb") as output:
                for block in iter(lambda:src.read(4*1024*1024),b""):
                    output.write(block);h.update(block);count+=len(block)
            assert count==row["bytes"] and h.hexdigest()==row["sha256"]
            tmp.replace(dest)
    assert seen==set(wanted)
    return len(seen)

def output_manifest(out):
    entries=[dict(file_spec(p),included_in_git=False) for p in sorted(out.iterdir())
             if p.is_file() and p.name not in (MANIFEST,REFERENCE)
             and not p.name.endswith((".tmp",".download"))]
    save(out/MANIFEST,{"result":RESULT,"files":entries,"temporary_active_checkpoint_retention_days":1,
                       "reproducible_data_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,"manifest_file":MANIFEST,
                        "manifest_sha256":sha(out/MANIFEST),"manifest_bytes":(out/MANIFEST).stat().st_size,
                        "file_count":len(entries)})

def source_identity(item):
    return {key:item[key] for key in BASE_KEYS}


def seed_names(label):
    names={MANIFEST,"run-receipt.json","core-receipt.json","public-actions-input.json"}
    if label!="R786":names.add(REFERENCE)
    if CERTIFICATES[label]:names.add(CERTIFICATES[label])
    if label=="R827":names.update(LAYER_INDEXES);names.update(R827_EXTRA)
    elif label=="R809":names.update(("R809-S5-basis-index.json.gz","R809-accepted-S5-short-minor.json.gz"))
    elif label=="R786":names.update(("R786-exact-stages-manifest.json.gz","R786-exact-power5-basis-index.json.gz"))
    return names


def selected_names(label,directory):
    directory=Path(directory);names=seed_names(label)
    if label=="R827":
        for index_name in LAYER_INDEXES:
            index=read(directory/index_name)
            key="row_blocks" if index_name==LAYER_INDEXES[0] else "coefficient_row_blocks"
            names.update(plain(row)["file"] for row in index[key])
    elif label=="R809":
        index=read(directory/"R809-S5-basis-index.json.gz")
        names.update(plain(row["source"])["file"] for row in index["basis_rows"])
    elif label=="R786":
        for power,count in ((2,418),(3,690)):
            names.update("R786-exact-power-"+str(power)+"-row-"+str(i).zfill(4)+".json.gz" for i in range(count))
    elif label=="R837":
        cert=read(directory/CERTIFICATES[label])
        names.update(plain(cert[key])["file"] for key in ("stage_manifest","fixed_branch_space","pencil_certificate"))
        pencil_path=directory/plain(cert["pencil_certificate"])["file"]
        if pencil_path.exists():
            pencil=read(pencil_path)
            names.update(plain(pencil[key])["file"] for key in ("first_anchor","second_anchor"))
    elif label=="R838":
        cert=read(directory/CERTIFICATES[label])
        names.add(plain(cert["stage_manifest"])["file"])
        names.add(plain(cert["colength_certificate"])["file"])
    return sorted(names)


def load_io(item):
    global IO
    path=S/safe_name(item["io_helper"])
    assert path.name=="R824_public_original_global_polar_generators.py"
    assert sha(path)==item["io_helper_sha256"]==RANGE_SHA
    module=importlib.util.spec_from_file_location("R839_frozen_Range_only_IO",path)
    IO=importlib.util.module_from_spec(module);module.loader.exec_module(IO)


def guard(item,path):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
    assert item["result"]==RESULT and item["p"]==41 and item["producer_inputs_pending"] is False
    assert path.resolve()==REQUEST.resolve()
    assert item["core"]=="R839_original_short_RR_spaces.py"
    assert item["wrapper"]=="R839_public_original_short_RR_spaces.py"
    assert sha(__file__)==item["wrapper_sha256"] and sha(S/item["core"])==item["core_sha256"]
    assert 0<item["budget_minutes"]<=300
    for key in PROOFS:assert sha(topic_path(item[key]))==item[key+"_sha256"]
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert set(item["sources"])==set(SOURCES)
    for label,source in item["sources"].items():
        assert H64.fullmatch(source["configuration_sha256"])
        assert source["manifest_bytes"]>0 and source["manifest_file_count"]>0
        assert H64.fullmatch(source["selected_files_sha256"])
        assert source["certificate_name"]==CERTIFICATES[label]
        assert source["selected_file_count"]>0
        assert source["expected_conclusion"]==("failure" if label=="R827" else "success")
        assert source["accepted_process_exit_codes"]==([124] if label=="R827" else [0])
    load_io(item)


def source_review(label,item,directory):
    """Original producer bytes/schema only; never imports a mathematical core."""
    source=item["sources"][label];directory=Path(directory)
    manifest_path=directory/MANIFEST
    assert manifest_path.stat().st_size==source["manifest_bytes"] and sha(manifest_path)==source["manifest_sha256"]
    manifest=read(manifest_path);assert manifest["result"]==source["result"]
    entries={row["file"]:plain(row) for row in manifest["files"]}
    assert len(entries)==len(manifest["files"])==source["manifest_file_count"]
    entries[MANIFEST]=file_spec(manifest_path)
    if label!="R786":
        entries[REFERENCE]=plain(source["manifest_reference"])
        reference=read(bound(directory,entries[REFERENCE]))
        assert reference["manifest_sha256"]==source["manifest_sha256"]
        assert reference["manifest_bytes"]==source["manifest_bytes"]
        assert reference["file_count"]==source["manifest_file_count"]
    names=selected_names(label,directory)
    assert len(names)==source["selected_file_count"]
    selected={name:entries[name] for name in names}
    for value in selected.values():bound(directory,value)
    assert fingerprint([selected[name] for name in sorted(selected)])==source["selected_files_sha256"]
    initial=read(directory/"public-actions-input.json")
    run=read(directory/"run-receipt.json");core=read(directory/"core-receipt.json")
    assert initial["result"]==run["result"]==core["result"]==source["result"]
    assert initial["source_commit"]==run["source_commit"]==source["source_commit"]
    assert str(run["workflow_run_id"])==str(source["run_id"])
    assert initial["core_sha256"]==core["source_sha256"]==source["core_sha256"]
    assert run["process_exit_code"] in source["accepted_process_exit_codes"]
    assert run.get("error") is None
    if run.get("core_receipt_sha256") is not None:
        assert run["core_receipt_sha256"]==selected["core-receipt.json"]["sha256"]
    cert=None
    if CERTIFICATES[label]:
        cert=read(directory/CERTIFICATES[label])
        assert cert["complete"] is True and cert["result"]==source["result"]
        assert run["complete"] is True and core["complete"] is True
        assert core["certificate_sha256"]==selected[CERTIFICATES[label]]["sha256"]
        tag=cert["configuration"]
    else:
        assert run["complete"] is False and core["complete"] is False
        assert core.get("budget_stop")
        tag=read(directory/"R827-original-place-and-unit-source-audit.json.gz")["configuration"]
    assert tag["result"]==source["result"] and tag["source_sha256"]==source["core_sha256"]
    assert tag["python_flint"]=="0.9.0" and fingerprint(tag)==source["configuration_sha256"]
    for name in names:
        if name.endswith(".json.gz"):
            value=read(directory/name)
            assert value["complete"] is True and value["configuration"]==tag
            if "result" in value:assert value["result"]==source["result"]
    if label=="R827":
        place=read(directory/"R827-original-place-and-unit-source-audit.json.gz")
        assert place["genuine_DVR_lift_source_not_an_arbitrary_modular_kernel_candidate"] is True
        assert place["prime"]==1000000753 and place["original_branch"]==0
        assert place["canonical_free_column"]==1186
        assert tag["normal_basis_degrees"]==EPS
        assert len(names)==406
        for order,index_name in enumerate(LAYER_INDEXES):
            index=read(directory/index_name)
            key="row_blocks" if order==0 else "coefficient_row_blocks"
            assert len(index[key])==(17 if order==0 else 17*(8+2*order))
            assert index["chart"]=="tau" and index["prime"]==1000000753
            for value in index[key]:assert plain(value)==selected[value["file"]]
        inv=read(directory/"R827-prime-1000000753-S5-fixed-minor-inverse.json.gz")
        assert inv["both_inverse_products_verified"] is True
        assert inv["prime"]==1000000753 and len(inv["row_indices"])==1234
    elif label=="R838":
        assert cert["original_characteristic_zero_J2_equals_I2"] is True
        assert cert["actual_P0_multiplicity_in_D"]==0 and cert["actual_original_I2_colength"]==415
        assert cert["configuration"]["source_identity"]=={key:item["sources"]["R827"][key] for key in BASE_KEYS if key!="configuration_sha256"}
        assert cert["configuration"]["source_configuration_sha256"]==item["sources"]["R827"]["configuration_sha256"]
    elif label=="R837":
        for flag in ("original_P0_evaluation_certified","complete_fixed_branch_space_certified","fixed_branch_pencil_certified"):
            assert cert[flag] is True
        assert cert["actual_pencil_rank"]==1213
        pencil=read(directory/cert["pencil_certificate"]["file"])
        assert pencil["rank1213_implies_exact_common_zero_divisor_Dcusp_plus_P0"] is True
        for key in ("first_anchor","second_anchor"):
            assert plain(pencil[key])==selected[pencil[key]["file"]]
    elif label=="R809":
        index=read(directory/"R809-S5-basis-index.json.gz")
        assert index["dimension"]==1234 and index["qY_count"]==69
        assert index["full_coordinate_rows"]==1380 and index["integer_scale"]=="13744803133596058624"
        assert index["normal_basis_degrees"]==EPS
        assert len(index["basis_rows"])==1234
        for i,entry in enumerate(index["basis_rows"]):
            assert entry["index"]==i and plain(entry["source"])==selected[entry["source"]["file"]]
    elif label=="R786":
        assert cert["exact_power5_basis_dimension"]==1234 and cert["exact_K_basis_prefix_bound_qY"]==128
        stages=read(directory/"R786-exact-stages-manifest.json.gz")
        stage_map={value["file"]:plain(value) for value in stages["files"]}
        for power,count in ((2,418),(3,690)):
            for i in range(count):
                name="R786-exact-power-"+str(power)+"-row-"+str(i).zfill(4)+".json.gz"
                assert selected[name]==stage_map[name]
                value=read(directory/name)
                assert value["weight"]==2*power and value["bound_qY"]==128
                assert value["original_R775_finite_coefficients_verified"] is True
    return {**source_identity(source),"certificate_name":CERTIFICATES[label],"files":selected}


def expected_tag(item,sources):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
            "R839_proof_sha256":item["proof_sha256"],"R839_method_sha256":item["method_sha256"],
            "sources":sources,**SCOPE}


def fetch_sources(item,out):
    out=Path(out);retained=out.parent/"retained-original-R839";retained.mkdir(parents=True,exist_ok=True)
    reviewed,transport={},{}
    for label in SOURCES:
        source=item["sources"][label];folder=retained/label;folder.mkdir(parents=True,exist_ok=True)
        archive=IO.Archive(source,out.parent/("download-"+label),whole=False)
        try:
            archive.extract_bound(MANIFEST,source["manifest_sha256"],folder/MANIFEST,source["manifest_bytes"])
            entries={value["file"]:plain(value) for value in read(folder/MANIFEST)["files"]}
            assert len(entries)==source["manifest_file_count"]
            if label!="R786":entries[REFERENCE]=plain(source["manifest_reference"])
            for name,row in entries.items():
                assert name in archive.by_name and len(archive.by_name[name])==1
                assert archive.by_name[name][0].file_size==row["bytes"]
            def extract(names):
                missing=[name for name in names if not (folder/name).exists()]
                archive.extract_many([(name,entries[name]["sha256"],folder/name,entries[name]["bytes"])
                                      for name in missing if name!=MANIFEST])
            extract(seed_names(label)-{MANIFEST})
            extract(selected_names(label,folder))
            # R837's exact anchor references are learned from the just-read actual pencil.
            extract(selected_names(label,folder))
            reviewed[label]=source_review(label,item,folder)
            transport[label]=archive.receipt()
        finally:archive.close()
    return retained,reviewed,transport


def prepare_sources(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-original-R839";retained.mkdir(parents=True,exist_ok=True)
    receipt_path=out/INPUT_RECEIPT;inventory_path=out/INVENTORY
    if receipt_path.exists() and (out/BUNDLE).exists() and inventory_path.exists():
        receipt=read(receipt_path);inventory=read(inventory_path)
        assert receipt["result"]==RESULT and receipt["complete"] is True and receipt["sources"]==item["sources"]
        assert inventory["result"]==RESULT and inventory["complete"] is True
        bound(out,receipt["source_inventory"]);bound(out,receipt["source_bundle"])
        count=unpack_sources(out/BUNDLE,retained,inventory)
        reviewed={label:source_review(label,item,retained/label) for label in SOURCES}
        assert reviewed==inventory["sources"] and count==receipt["minimal_bundle_member_count"]
        return retained,receipt,reviewed
    assert allow_download,"Continuation requires its completed selected-source carrier."
    retained,reviewed,transport=fetch_sources(item,out)
    inventory={"result":RESULT,"complete":True,"sources":reviewed,
               "all_entries_are_unchanged_original_producer_bytes":True}
    save(inventory_path,inventory);pack_sources(retained,inventory,out/BUNDLE)
    count=sum(len(value["files"]) for value in reviewed.values())
    receipt={"result":RESULT,"complete":True,"sources":item["sources"],
             "source_inventory":file_spec(inventory_path),"source_bundle":file_spec(out/BUNDLE),
             "minimal_bundle_member_count":count,"range_transport":transport,
             "old_Fourier_derivative_anchor_and_S5_inverse_arithmetic_recomputed":False}
    save(receipt_path,receipt)
    print("SHORT_RR_INPUT_REVIEW="+json.dumps({
        "source_inventory":receipt["source_inventory"],"source_bundle":receipt["source_bundle"],
        "selected_original_files":count,"new_mathematics_executed_in_source_preparation":False},sort_keys=True),flush=True)
    return retained,receipt,reviewed


def stable_job(item):
    return {key:value for key,value in item.items()
            if key not in ("resume","budget_minutes","readme_sha256","rules_last_read_commit")}


def restore(item,out):
    resume=item.get("resume")
    if resume is None:return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    meta=out.parent/"resume-metadata";meta.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"download-R839-continuation",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],meta/MANIFEST,resume["manifest_bytes"])
        manifest=read(meta/MANIFEST);assert manifest["result"]==RESULT
        entries={value["file"]:plain(value) for value in manifest["files"]}
        assert len(entries)==len(manifest["files"])==resume["manifest_file_count"]
        for name in ("run-receipt.json","public-actions-input.json","core-receipt.json",INPUT_RECEIPT,INVENTORY,BUNDLE):
            if name=="core-receipt.json" and name not in entries:continue
            row=entries[name];dest=out/name if name in (INPUT_RECEIPT,INVENTORY,BUNDLE) else meta/name
            archive.extract_bound(name,row["sha256"],dest,row["bytes"])
        run,initial=read(meta/"run-receipt.json"),read(meta/"public-actions-input.json")
        assert run["result"]==initial["result"]==RESULT
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        assert run["source_commit"]==initial["source_commit"]==resume["source_commit"]
        assert initial["core_sha256"]==item["core_sha256"]
        assert stable_job(initial["job"])==stable_job(item)
        assert run["process_exit_code"] in resume["accepted_process_exit_codes"]
        core=None
        if (meta/"core-receipt.json").exists():
            core=read(meta/"core-receipt.json")
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
            assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
        else:assert run.get("core_receipt_sha256") is None and run["complete"] is False
        retained,receipt,sources=prepare_sources(item,out,allow_download=False)
        tag=expected_tag(item,sources)
        names=sorted(name for name in entries if name.startswith(PREFIX) and name.endswith(".json.gz"))
        archive.extract_many([(name,entries[name]["sha256"],out/name,entries[name]["bytes"]) for name in names])
        for name in names:
            value=read(out/name)
            assert value["complete"] is True and value["configuration"]==tag and value["result"]==RESULT
        restored_final=False
        if FINAL in entries:
            row=entries[FINAL];archive.extract_bound(FINAL,row["sha256"],meta/FINAL,row["bytes"])
            final=read(meta/FINAL)
            assert final["configuration"]==tag
            if final.get("complete") is True:
                assert all(final[key] is True for key in FLAGS)
                assert run["complete"] is True and run["process_exit_code"]==0
                assert core is not None and core["complete"] is True and core["certificate_sha256"]==row["sha256"]
                shutil.copyfile(meta/FINAL,out/FINAL);restored_final=True
        save(out/"resume-inheritance-receipt.json",{
            "result":RESULT,"complete":True,"source_resume":resume,
            "original_manifest":file_spec(meta/MANIFEST),"range_transport":archive.receipt(),
            "all_restored_complete_stages":[entries[name] for name in names],
            "restored_successful_final":restored_final,
            "old_completed_source_bound_stages_not_recomputed":True,
            "incomplete_final_not_used_to_override_newer_completed_stages":True})
    finally:archive.close()


def compute(item,out,request_path):
    out.mkdir(parents=True,exist_ok=True);process=None;exitcode=1;error=None;outer_timeout=False
    try:
        restore(item,out)
        retained,receipt,sources=prepare_sources(item,out)
        expanded=dict(item)
        expanded["sources"]={label:{**value,"directory":str((retained/label).resolve())} for label,value in sources.items()}
        for key in PROOFS:expanded[key]=str(topic_path(item[key]))
        save(out/"public-actions-expanded-job.json",expanded)
        initial={"result":RESULT,"p":41,"source_repository":"Rogerhu12/math-research-public",
                 "source_commit":os.environ["GITHUB_SHA"],"job":item,"request_sha256":sha(request_path),
                 "driver_sha256":sha(__file__),"core_sha256":item["core_sha256"],
                 "proof_sha256":item["proof_sha256"],"method_sha256":item["method_sha256"],
                 "io_helper_sha256":RANGE_SHA,"workflow_sha256":sha(REPO/item["workflow"]),
                 "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
                 "source_inventory":receipt["source_inventory"],
                 "prepared_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
                 "all_new_mathematics_runs_only_in_separate_public_Actions_core":True}
        save(out/"public-actions-input.json",initial)
        command=[sys.executable,str(S/item["core"]),"--config",str(out/"public-actions-expanded-job.json"),
                 "--out",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w",encoding="utf-8") as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:exitcode=process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                outer_timeout=True;os.killpg(process.pid,signal.SIGTERM)
                try:process.wait(timeout=20)
                except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
                exitcode=124
    except BaseException as exc:
        error=type(exc).__name__+": "+str(exc)
        if process is not None and process.poll() is None:
            os.killpg(process.pid,signal.SIGTERM)
            try:process.wait(timeout=20)
            except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
        exitcode=1
    finally:
        core_path=out/"core-receipt.json";core=read(core_path) if core_path.exists() else None
        final=read(out/FINAL) if (out/FINAL).exists() else None
        complete=exitcode==0 and core is not None and core.get("complete") is True and \
            final is not None and final.get("complete") is True and all(final.get(key) is True for key in FLAGS)
        run={"result":RESULT,"p":41,"complete":complete,"process_exit_code":exitcode,"error":error,
             "core_receipt_sha256":sha(core_path) if core_path.exists() else None,
             "source_commit":os.environ.get("GITHUB_SHA"),"workflow_run_id":os.environ.get("GITHUB_RUN_ID"),
             "workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT"),
             "execution_environment":"public-repository-github-actions","outer_timeout":outer_timeout,
             "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
        save(out/"run-receipt.json",run);output_manifest(out)
        print("SHORT_RR_RUN_RECEIPT="+json.dumps(run,sort_keys=True),flush=True)
    return exitcode


def verify(item,out,request_path):
    manifest=read(out/MANIFEST);assert manifest["result"]==RESULT
    entries={value["file"]:plain(value) for value in manifest["files"]}
    assert len(entries)==len(manifest["files"])
    for value in entries.values():bound(out,value)
    reference=read(out/REFERENCE)
    assert reference["result"]==RESULT and reference["manifest_sha256"]==sha(out/MANIFEST)
    assert reference["manifest_bytes"]==(out/MANIFEST).stat().st_size and reference["file_count"]==len(entries)
    run=read(out/"run-receipt.json")
    if not run.get("complete"):
        print("SHORT_RR_INCOMPLETE_IO_REVIEW="+json.dumps({
            "complete":False,"run":run,"manifest_files":len(entries),
            "no_incomplete_rank_is_claimed_as_a_complete_RR_space":True},sort_keys=True),flush=True)
        return 2
    retained,receipt,sources=prepare_sources(item,out,allow_download=False)
    initial,core,final=(read(out/name) for name in ("public-actions-input.json","core-receipt.json",FINAL))
    assert initial["job"]==item and initial["request_sha256"]==sha(request_path)
    assert initial["source_commit"]==run["source_commit"]
    assert initial["driver_sha256"]==sha(__file__) and initial["core_sha256"]==item["core_sha256"]
    assert core["result"]==final["result"]==RESULT and core["complete"] is True and final["complete"] is True
    assert run["process_exit_code"]==0 and core["source_sha256"]==item["core_sha256"]
    assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
    assert core["certificate_sha256"]==entries[FINAL]["sha256"]
    tag=expected_tag(item,sources);assert final["configuration"]==tag
    assert all(final[key] is True and core[key] is True for key in FLAGS)
    assert final["actual_T11_rank"]==2451 and final["actual_T5_rank"]==415
    assert final["actual_D_kernel_rank"]==395 and final["actual_D_RR_dimension"]==295
    assert final["expanded_characteristic_zero_coordinates_computed"] is False
    assert final["actual_eta_or_height_computed"] is False
    inventory=read(bound(out,final["stage_manifest"]))
    assert inventory["complete"] is True and inventory["configuration"]==tag and inventory["result"]==RESULT
    stages={value["file"]:plain(value) for value in inventory["files"]}
    assert len(stages)==len(inventory["files"])==final["complete_math_stage_count"]
    for name,row in stages.items():
        assert entries[name]==row
        value=read(bound(out,row))
        assert value["complete"] is True and value["configuration"]==tag and value["result"]==RESULT
    def stage(value):
        assert plain(value)==stages[value["file"]]
        return read(bound(out,value))
    audit=stage(final["source_audit"])
    assert audit["actual_E2_degree"]==415 and audit["actual_P0_multiplicity_in_D"]==0
    T11=stage(final["T11_quotient"])
    assert T11[FLAGS[0]] is True and T11["actual_rank"]==2451
    assert T11["actual_minor_determinant_mod_prime"]!=0
    assert len(T11["selected_original_rows"])==len(set(T11["selected_original_rows"]))==2451
    assert len(T11["selected_original_source_columns"])==2451 and len(T11["complement_original_rows"])==415
    assert T11["all_2451_source_columns_annihilated_in_all415_rows"] is True
    assert T11["complement_identity_verified"] is True
    T5=stage(final["T5_quotient"])
    assert T5[FLAGS[1]] is True and T5["actual_rank"]==415 and T5["actual_minor_determinant_mod_prime"]!=0
    assert T5["full_830_by1234_row_space_reconstruction_verified"] is True
    D=stage(final["D_kernel_basis"])
    assert D[FLAGS[2]] is True and D["actual_rank"]==395 and D["actual_minor_determinant_mod_prime"]!=0
    assert len(D["original_V3_free_columns"])==295
    assert D["all830_original_equations_verified_for_all295_columns"] is True
    assert D["original_free_normalization_identity_verified"] is True
    print("SHORT_RR_COMPLETE_IO_REVIEW="+json.dumps({
        "result":RESULT,"certificate":entries[FINAL],"stage_manifest":plain(final["stage_manifest"]),
        "actual_T11_rank":2451,"actual_T5_rank":415,"actual_D_kernel_rank":395,"D_RR_dimension":295,
        "complete_stages":len(stages),"manifest_files":len(entries),
        "source_inventory":receipt["source_inventory"],"source_bundle":receipt["source_bundle"],
        "seconds":final["seconds"],"all_output_and_selected_source_bytes_verified":True,
        "mathematics_reexecuted_by_wrapper":False},sort_keys=True),flush=True)
    return 0


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--verify",action="store_true")
    args=parser.parse_args()
    item=read(REQUEST);guard(item,REQUEST)
    return verify(item,args.output,REQUEST) if args.verify else compute(item,args.output,REQUEST)


if __name__=="__main__":raise SystemExit(main())
