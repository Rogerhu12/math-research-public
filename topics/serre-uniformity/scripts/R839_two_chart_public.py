#!/usr/bin/env python3
"""Public standard-library carrier and source runner for R839's two-chart completion."""
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

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R839-two-chart-public-request.json"
RESULT = "R839-original-two-chart-short-RR-spaces-and-D-kernel"
FINAL = "p41-original-two-chart-short-RR-and-D-kernel-certificate.json"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R839-two-chart-retained-original-inputs.tar.gz"
INVENTORY = "R839-two-chart-original-source-inventory.json"
INPUT_RECEIPT = "R839-two-chart-retained-inputs-receipt.json"
OLD_FINAL = "p41-original-short-RR-and-D-kernel-certificate.json"
OLD_BUNDLE = "R839-retained-original-inputs.tar.gz"
OLD_INVENTORY = "R839-original-source-inventory.json"
OLD_CORE = "0a027c2dd83cfab37181e6386cfd8b22baf176421b727d81a7584d7b351d0c36"
OLD_WRAPPER = "dee4e8fb7fedae80e0076d8a1b3fa0e24114477d129a7b8381238d33b88529c7"
OLD_CONFIGURATION = "111621ab17dfb725e3898319e9b421883663d0eac2bfc7dc28d11e42ef978e33"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "configuration_sha256")
LABELS = ("R827", "R838", "R837", "R809", "R786")
ALL_LABELS = LABELS+("R839_tau",)
PROOFS = ("proof", "completion_proof", "method")
EPS = [0]+[1]*144+[2]*127
SIGMA_COLUMNS = [0]+list(range(73, 92))
SIGMA_INDEXES = (
    "R827-target-B-sigma-polynomial-index.json.gz",
    "R827-target-g-sigma-polynomial-index.json.gz",
    "R827-target-Gamma-sigma-polynomial-index.json.gz",
    "R827-sigma-layer-001-precision-0004-index.json.gz",
)
FLAGS = ("exact_original_T11_as_unit_chart_expression_certified",
         "exact_original_T5_quotient_as_unit_chart_expression_certified",
         "exact_original_D_RR_space_as_unit_chart_expression_certified")
SCOPE = {
    "auxiliary_prime":1000000753,"original_branch":0,
    "normal_basis_rank":272,"normal_basis_degrees":EPS,
    "uniform_homogeneous_weight":11,
    "old_tau_matrix_shape":[2866,2886],"old_actual_tau_rank":2431,
    "sigma_first_derivative_columns":SIGMA_COLUMNS,
    "old_sigma_coefficient_range":[0,4],"new_sigma_coefficient_range":[4,10],
    "new_sigma_shifted_matrix_shape":[2866,81],
    "old_selected_column_quotient_shape":[435,2866],
    "incremental_quotient_matrix_shape":[435,81],
    "required_added_rank":20,"T11_required_rank":2451,
    "T5_matrix_shape":[830,1234],"T5_required_rank":415,
    "D_matrix_shape":[830,690],"D_required_rank":395,"D_RR_dimension":295,
    "old_tau_matrix_or_complete_column_RREF_recomputed":False,
    "old_sigma_coefficients_zero_through_three_recomputed":False,
    "sigma_stored_g_already_is_signed_base_variable_derivative":True,
    "old_same_prime_S5_inverse_or_Fourier_prefixes_recomputed":False,
    "all_new_global_sources_are_original_sigma_homogenizations":True,
    "old_tau_rank_not_asserted_as_full_characteristic_zero_tau_rank":True,
    "accurate_characteristic_zero_objects_are_source_bound_unit_solve_expressions":True,
    "budget_and_absolute_directories_excluded_from_mathematical_identity":True,
}
H64 = re.compile(r"[0-9a-f]{64}")
IO = OLD_IO = None


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(4*1024*1024),b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path,"rt",encoding="utf-8") as stream:
        return json.load(stream)


def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    tmp.write_text(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
    tmp.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()


def safe_name(name):
    assert isinstance(name,str) and Path(name).name==name and name not in (".","..") and "\\" not in name
    return name


def plain(value):
    answer={key:value[key] for key in ("file","bytes","sha256")}
    safe_name(answer["file"])
    assert isinstance(answer["bytes"],int) and answer["bytes"]>=0 and H64.fullmatch(answer["sha256"])
    return answer


def file_spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}


def bound(folder,value):
    value=plain(value);path=Path(folder)/value["file"]
    assert file_spec(path)==value,("Changed bound bytes",path.name)
    return path


def topic_path(value):
    value=PurePosixPath(value)
    assert not value.is_absolute() and ".." not in value.parts
    path=(TOPIC/str(value)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def source_identity(item):
    return {key:item[key] for key in BASE_KEYS}


def load_helpers(item,helper_dir=None):
    global IO,OLD_IO
    folder=S if helper_dir is None else Path(helper_dir)
    for name,key,expected in (
        ("R824_public_original_global_polar_generators.py","io_helper_sha256",RANGE_SHA),
        ("R839_public_original_short_RR_spaces.py","legacy_wrapper_sha256",OLD_WRAPPER)):
        assert sha(folder/name)==item[key]==expected
        loader=importlib.util.spec_from_file_location("R839_two_chart_stdlib_"+name[:-3],folder/name)
        value=importlib.util.module_from_spec(loader);loader.loader.exec_module(value)
        if name.startswith("R824_"):
            IO=value
        else:
            OLD_IO=value


def guard(item,path):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
    assert item["result"]==RESULT and item["p"]==41 and item["producer_inputs_pending"] is False
    assert path.resolve()==REQUEST.resolve()
    assert item["core"]=="R839_two_chart_short_RR_spaces.py"
    assert item["wrapper"]=="R839_two_chart_public.py"
    assert sha(__file__)==item["wrapper_sha256"] and sha(S/item["core"])==item["core_sha256"]
    assert item["legacy_core"]=="R839_original_short_RR_spaces.py"
    assert sha(S/item["legacy_core"])==item["legacy_core_sha256"]==OLD_CORE
    assert 0<item["budget_minutes"]<=300
    for key in PROOFS:
        assert sha(topic_path(item[key]))==item[key+"_sha256"]
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    source=item["previous_tau_source"]
    assert source["result"]=="R839-original-short-RR-spaces-and-D-kernel"
    assert source["core_sha256"]==OLD_CORE and source["configuration_sha256"]==OLD_CONFIGURATION
    assert source["certificate_name"]==OLD_FINAL and source["expected_conclusion"]=="failure"
    assert source["selected_file_count"]==14 and source["manifest_file_count"]==13
    assert source["accepted_process_exit_codes"]==[2]
    assert item["sigma_extra_file_count"]==123 and item["selected_original_file_count"]==2919
    assert H64.fullmatch(item["sigma_extra_files_sha256"]) and H64.fullmatch(item["expanded_sources_sha256"])
    load_helpers(item)


def previous_selected_names(manifest):
    names={row["file"] for row in manifest["files"] if not row["file"].endswith(".tar.gz")}
    names.update((MANIFEST,REFERENCE))
    return sorted(names)


def review_previous(item,folder):
    source=item["previous_tau_source"];folder=Path(folder)
    assert file_spec(folder/MANIFEST)=={"file":MANIFEST,"bytes":source["manifest_bytes"],"sha256":source["manifest_sha256"]}
    manifest=read(folder/MANIFEST)
    assert manifest["result"]==source["result"]
    entries={row["file"]:plain(row) for row in manifest["files"]}
    assert len(entries)==len(manifest["files"])==source["manifest_file_count"]
    entries[MANIFEST]=file_spec(folder/MANIFEST)
    entries[REFERENCE]=plain(source["manifest_reference"])
    reference=read(bound(folder,entries[REFERENCE]))
    assert reference["result"]==source["result"]
    assert reference["manifest_sha256"]==source["manifest_sha256"] and reference["manifest_bytes"]==source["manifest_bytes"]
    assert reference["file_count"]==source["manifest_file_count"]
    names=previous_selected_names(manifest)
    assert len(names)==source["selected_file_count"]==14
    selected={name:entries[name] for name in names}
    for row in selected.values():bound(folder,row)
    assert fingerprint([selected[name] for name in sorted(selected)])==source["selected_files_sha256"]
    initial=read(folder/"public-actions-input.json")
    run=read(folder/"run-receipt.json");core=read(folder/"core-receipt.json")
    final=read(folder/OLD_FINAL)
    assert initial["result"]==run["result"]==core["result"]==final["result"]==source["result"]
    assert initial["source_commit"]==run["source_commit"]==source["source_commit"]
    assert str(run["workflow_run_id"])==str(source["run_id"])
    assert initial["core_sha256"]==core["source_sha256"]==source["core_sha256"]
    assert initial["driver_sha256"]==OLD_WRAPPER
    assert run["process_exit_code"]==2 and run["complete"] is False and run["error"] is None
    assert run["core_receipt_sha256"]==selected["core-receipt.json"]["sha256"]
    assert core["complete"] is False and final["complete"] is False
    assert core["certificate_sha256"]==selected[OLD_FINAL]["sha256"]
    tag=final["configuration"]
    assert tag["source_sha256"]==OLD_CORE and tag["result"]==source["result"]
    assert fingerprint(tag)==source["configuration_sha256"]==OLD_CONFIGURATION
    assert final["actual_T11_rank"]==2431 and final["actual_T5_rank"] is None and final["actual_D_kernel_rank"] is None
    assert not any(final[key] for key in FLAGS)
    assert final["stop_reason"]=="T11_actual_modular_rank_below_required_sufficient_rank" and final["error"] is None
    stages=read(bound(folder,final["stage_manifest"]))
    assert stages["complete"] is True and stages["configuration"]==tag
    assert len(stages["files"])==final["complete_math_stage_count"]==3
    for row in stages["files"]:
        assert plain(row)==selected[row["file"]]
        if row["file"]=="R839-T11-shifted-source-matrix.json.gz":
            # Byte authentication is complete; shape/tag is consumed once by
            # the mathematical core rather than parsing the large matrix here.
            continue
        value=read(folder/row["file"])
        assert value["complete"] is True and value["configuration"]==tag
    rank=read(folder/"R839-T11-source-column-rank.json.gz")
    assert rank["actual_rank"]==2431 and rank["required_rank"]==2451
    assert rank["all_2866_rows_and_2886_columns_used"] is True
    assert len(rank["independent_original_source_column_indices"])==2431
    assert plain(rank["source_matrix"])==selected["R839-T11-shifted-source-matrix.json.gz"]
    inventory=read(folder/OLD_INVENTORY)
    assert inventory["result"]==source["result"] and inventory["complete"] is True
    assert inventory["sources"]==tag["sources"]
    assert entries[OLD_BUNDLE]==plain(source["input_bundle"])
    old_input_receipt=read(folder/"R839-retained-inputs-receipt.json")
    assert old_input_receipt["minimal_bundle_member_count"]==2782
    assert plain(old_input_receipt["source_bundle"])==entries[OLD_BUNDLE]
    assert plain(old_input_receipt["source_inventory"])==selected[OLD_INVENTORY]
    return {**source_identity(source),"certificate_name":OLD_FINAL,"files":selected},initial["job"],inventory


def sigma_names(folder):
    folder=Path(folder);names=set(SIGMA_INDEXES)
    for name in SIGMA_INDEXES:
        value=read(folder/name)
        key="coefficient_row_blocks" if "precision-0004" in name else "row_blocks"
        names.update(plain(row)["file"] for row in value[key])
    return sorted(names)


def review_sigma_extra(item,folder,old_source):
    folder=Path(folder);manifest=read(folder/MANIFEST)
    assert manifest["result"]==old_source["result"] and sha(folder/MANIFEST)==old_source["manifest_sha256"]
    entries={row["file"]:plain(row) for row in manifest["files"]}
    names=sigma_names(folder)
    assert len(names)==item["sigma_extra_file_count"]==123
    selected={name:entries[name] for name in names}
    assert fingerprint([selected[name] for name in sorted(selected)])==item["sigma_extra_files_sha256"]
    tag=read(folder/"R827-original-place-and-unit-source-audit.json.gz")["configuration"]
    assert fingerprint(tag)==old_source["configuration_sha256"]
    for name,row in selected.items():
        value=read(bound(folder,row))
        assert value["complete"] is True and value["configuration"]==tag
        if "result" in value:assert value["result"]==old_source["result"]
        assert value["chart"]=="sigma" and value["prime"]==1000000753
    operators=read(folder/"R827-complete-short-operator-identities-and-sigma-transport.json.gz")
    for target,name,degree in zip(("B","g","Gamma"),SIGMA_INDEXES[:3],(5,3,2)):
        index=read(folder/name)
        assert plain(operators["operator_indexes"][target]["sigma"])==selected[name]
        assert index["target"]==target and index["regular_degree_bound"]==degree
        assert index["normal_basis_degrees"]==EPS and len(index["row_blocks"])==17
        assert index["all_negative_powers_and_weighted_zeros_verified"] is True
        assert index["g_matrix_means_negative_sigma_base_derivative"] is (target=="g")
        for row in index["row_blocks"]:
            assert plain(row)==selected[row["file"]]
    jets=read(folder/SIGMA_INDEXES[3])
    assert jets["derivative_order"]==1 and jets["precision_stop"]==4
    assert jets["full_polynomial_coefficients_computed"] is False
    assert len(jets["coefficient_row_blocks"])==68
    for row in jets["coefficient_row_blocks"]:
        assert plain(row)==selected[row["file"]]
    infinity=read(folder/"R827-sigma-infinity-order-0004-certificate.json.gz")
    assert plain(infinity["source_layer_jets"][1]["source"])==selected[SIGMA_INDEXES[3]]
    assert infinity["actual_selected_pivot_columns"]==list(range(252))+[272]+list(range(345,364))
    assert infinity["actual_rank_mod_prime"]==272 and infinity["actual_full_minor_determinant_mod_prime"]==695832206
    return selected


def review_all(item,retained):
    retained=Path(retained)
    previous,old_job,old_inventory=review_previous(item,retained/"R839_tau")
    original={label:OLD_IO.source_review(label,old_job,retained/label) for label in LABELS}
    assert original==old_inventory["sources"]
    extra=review_sigma_extra(item,retained/"R827",old_job["sources"]["R827"])
    assert not (set(extra)&set(original["R827"]["files"]))
    reviewed={label:{**value,"files":dict(value["files"])} for label,value in original.items()}
    reviewed["R827"]["files"].update(extra)
    reviewed["R839_tau"]=previous
    assert sum(len(s["files"]) for s in reviewed.values())==item["selected_original_file_count"]==2919
    assert fingerprint(reviewed)==item["expanded_sources_sha256"]
    return reviewed,old_job


def fetch_sources(item,out):
    out=Path(out);retained=out.parent/"retained-original-two-chart-R839"
    retained.mkdir(parents=True,exist_ok=True)
    folder=retained/"R839_tau";folder.mkdir(parents=True,exist_ok=True)
    source=item["previous_tau_source"]
    archive=IO.Archive(source,out.parent/"download-original-R839-tau",whole=False)
    try:
        archive.extract_bound(MANIFEST,source["manifest_sha256"],folder/MANIFEST,source["manifest_bytes"])
        entries={row["file"]:plain(row) for row in read(folder/MANIFEST)["files"]}
        entries[REFERENCE]=plain(source["manifest_reference"])
        names=previous_selected_names(read(folder/MANIFEST))
        archive.extract_many([(name,entries[name]["sha256"],folder/name,entries[name]["bytes"])
                              for name in names if name!=MANIFEST])
        _,old_job,old_inventory=review_previous(item,folder)
        old_bundle=out.parent/"original-R839-selected-source-carrier.tar.gz"
        row=plain(source["input_bundle"])
        archive.extract_bound(row["file"],row["sha256"],old_bundle,row["bytes"])
        count=OLD_IO.unpack_sources(old_bundle,retained,old_inventory)
        assert count==2782
        previous_transport=archive.receipt()
    finally:archive.close()
    old_r827=old_job["sources"]["R827"]
    sigma_archive=IO.Archive(old_r827,out.parent/"download-original-R827-sigma",whole=False)
    try:
        folder=retained/"R827"
        entries={row["file"]:plain(row) for row in read(folder/MANIFEST)["files"]}
        sigma_archive.extract_many([(name,entries[name]["sha256"],folder/name,entries[name]["bytes"])
                                    for name in SIGMA_INDEXES])
        names=sigma_names(folder)
        sigma_archive.extract_many([(name,entries[name]["sha256"],folder/name,entries[name]["bytes"])
                                    for name in names if name not in SIGMA_INDEXES])
        sigma_transport=sigma_archive.receipt()
    finally:sigma_archive.close()
    reviewed,_=review_all(item,retained)
    return retained,reviewed,{"original_R839_tau":previous_transport,"original_R827_sigma":sigma_transport}


def expected_tag(item,reviewed):
    return {
        "result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "legacy_R839_core_sha256":OLD_CORE,
        "R839_corrected_proof_sha256":item["proof_sha256"],
        "R839_two_chart_completion_proof_sha256":item["completion_proof_sha256"],
        "R839_two_chart_method_sha256":item["method_sha256"],
        "sources":{label:reviewed[label] for label in LABELS},
        "previous_tau_source":reviewed["R839_tau"],
        "frozen_original_tail_scope":OLD_IO.SCOPE,**SCOPE,
    }


def prepare_sources(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-original-two-chart-R839"
    retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (INPUT_RECEIPT,INVENTORY,BUNDLE)):
        receipt=read(out/INPUT_RECEIPT);inventory=read(out/INVENTORY)
        assert receipt["result"]==RESULT and receipt["complete"] is True
        assert receipt["original_tau_producer"]==item["previous_tau_source"]
        assert receipt["expanded_sources_sha256"]==item["expanded_sources_sha256"]
        bound(out,receipt["source_inventory"]);bound(out,receipt["source_bundle"])
        assert inventory["result"]==RESULT and inventory["complete"] is True
        count=OLD_IO.unpack_sources(out/BUNDLE,retained,inventory)
        reviewed,_=review_all(item,retained)
        assert reviewed==inventory["sources"] and count==receipt["minimal_bundle_member_count"]==2919
        return retained,receipt,reviewed
    assert allow_download,"Continuation must retain its complete selected source carrier."
    retained,reviewed,transport=fetch_sources(item,out)
    inventory={"result":RESULT,"complete":True,"sources":reviewed,
               "all_entries_are_unchanged_original_producer_bytes":True}
    save(out/INVENTORY,inventory)
    OLD_IO.pack_sources(retained,inventory,out/BUNDLE)
    receipt={"result":RESULT,"complete":True,"original_tau_producer":item["previous_tau_source"],
             "expanded_sources_sha256":item["expanded_sources_sha256"],
             "source_inventory":file_spec(out/INVENTORY),"source_bundle":file_spec(out/BUNDLE),
             "minimal_bundle_member_count":2919,"range_transport":transport,
             "original_2782_inputs_plus_123_sigma_members_plus_14_previous_members":True,
             "old_tau_RREF_or_sigma_jets_or_original_S5_inverse_recomputed":False}
    save(out/INPUT_RECEIPT,receipt)
    print("TWO_CHART_INPUT_REVIEW="+json.dumps({
        "source_inventory":receipt["source_inventory"],"source_bundle":receipt["source_bundle"],
        "selected_original_files":2919,"new_mathematics_executed_in_source_preparation":False},sort_keys=True),flush=True)
    return retained,receipt,reviewed


def output_manifest(out):
    entries=[dict(file_spec(path),included_in_git=False) for path in sorted(out.iterdir())
             if path.is_file() and path.name not in (MANIFEST,REFERENCE)
             and not path.name.endswith((".tmp",".download"))]
    save(out/MANIFEST,{"result":RESULT,"files":entries,"temporary_active_checkpoint_retention_days":1,
                       "reproducible_data_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,"manifest_file":MANIFEST,"manifest_sha256":sha(out/MANIFEST),
                        "manifest_bytes":(out/MANIFEST).stat().st_size,"file_count":len(entries)})


def stable_job(item):
    return {key:value for key,value in item.items()
            if key not in ("resume","budget_minutes","readme_sha256","rules_last_read_commit")}


def restore(item,out):
    resume=item.get("resume")
    if resume is None:return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    meta=out.parent/"resume-two-chart-metadata";meta.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"download-two-chart-continuation",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],meta/MANIFEST,resume["manifest_bytes"])
        manifest=read(meta/MANIFEST);assert manifest["result"]==RESULT
        entries={row["file"]:plain(row) for row in manifest["files"]}
        assert len(entries)==len(manifest["files"])==resume["manifest_file_count"]
        for name in ("run-receipt.json","public-actions-input.json","core-receipt.json",INPUT_RECEIPT,INVENTORY,BUNDLE):
            if name=="core-receipt.json" and name not in entries:continue
            row=entries[name];dest=out/name if name in (INPUT_RECEIPT,INVENTORY,BUNDLE) else meta/name
            archive.extract_bound(name,row["sha256"],dest,row["bytes"])
        run=read(meta/"run-receipt.json");initial=read(meta/"public-actions-input.json")
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
        else:
            assert run.get("core_receipt_sha256") is None and run["complete"] is False
        _,_,reviewed=prepare_sources(item,out,allow_download=False)
        tag=expected_tag(item,reviewed)
        names=sorted(name for name in entries if name.startswith("R839-") and name.endswith(".json.gz"))
        archive.extract_many([(name,entries[name]["sha256"],out/name,entries[name]["bytes"]) for name in names])
        for name in names:
            value=read(out/name)
            assert value["complete"] is True and value["configuration"]==tag and value["result"]==RESULT
        restored_final=False
        if FINAL in entries:
            row=entries[FINAL]
            archive.extract_bound(FINAL,row["sha256"],meta/FINAL,row["bytes"])
            final=read(meta/FINAL);assert final["configuration"]==tag
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
    out.mkdir(parents=True,exist_ok=True)
    process=None;exitcode=1;error=None;outer_timeout=False
    try:
        restore(item,out)
        retained,receipt,reviewed=prepare_sources(item,out)
        expanded=dict(item)
        expanded["sources"]={label:{**reviewed[label],"directory":str((retained/label).resolve())} for label in LABELS}
        expanded["previous_tau_source"]={**reviewed["R839_tau"],"directory":str((retained/"R839_tau").resolve())}
        for key in PROOFS:expanded[key]=str(topic_path(item[key]))
        save(out/"public-actions-expanded-job.json",expanded)
        initial={"result":RESULT,"p":41,"source_repository":"Rogerhu12/math-research-public",
                 "source_commit":os.environ["GITHUB_SHA"],"job":item,
                 "request_sha256":sha(request_path),"driver_sha256":sha(__file__),
                 "core_sha256":item["core_sha256"],"legacy_core_sha256":OLD_CORE,
                 "proof_sha256":item["proof_sha256"],"completion_proof_sha256":item["completion_proof_sha256"],
                 "method_sha256":item["method_sha256"],"io_helper_sha256":RANGE_SHA,
                 "legacy_wrapper_sha256":OLD_WRAPPER,"workflow_sha256":sha(REPO/item["workflow"]),
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
        print("TWO_CHART_RUN_RECEIPT="+json.dumps(run,sort_keys=True),flush=True)
    return exitcode


def verify(item,out,request_path):
    manifest=read(out/MANIFEST);assert manifest["result"]==RESULT
    entries={row["file"]:plain(row) for row in manifest["files"]}
    assert len(entries)==len(manifest["files"])
    for row in entries.values():bound(out,row)
    reference=read(out/REFERENCE)
    assert reference["result"]==RESULT and reference["manifest_sha256"]==sha(out/MANIFEST)
    assert reference["manifest_bytes"]==(out/MANIFEST).stat().st_size and reference["file_count"]==len(entries)
    run=read(out/"run-receipt.json")
    if not run.get("complete"):
        print("TWO_CHART_INCOMPLETE_IO_REVIEW="+json.dumps({
            "complete":False,"run":run,"manifest_files":len(entries),
            "no_partial_rank_is_claimed_as_a_complete_RR_space":True},sort_keys=True),flush=True)
        return 2
    _,receipt,reviewed=prepare_sources(item,out,allow_download=False)
    initial=read(out/"public-actions-input.json");core=read(out/"core-receipt.json");final=read(out/FINAL)
    assert initial["job"]==item and initial["request_sha256"]==sha(request_path)
    assert initial["source_commit"]==run["source_commit"]
    assert initial["driver_sha256"]==sha(__file__) and initial["core_sha256"]==item["core_sha256"]
    assert core["result"]==final["result"]==RESULT and core["complete"] is True and final["complete"] is True
    assert run["process_exit_code"]==0 and core["source_sha256"]==item["core_sha256"]
    assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
    assert core["certificate_sha256"]==entries[FINAL]["sha256"]
    tag=expected_tag(item,reviewed);assert final["configuration"]==tag
    assert all(final[key] is True and core[key] is True for key in FLAGS)
    assert final["actual_T11_rank"]==2451 and final["actual_T5_rank"]==415
    assert final["actual_D_kernel_rank"]==395 and final["actual_D_RR_dimension"]==295
    assert final["expanded_characteristic_zero_coordinates_computed"] is False
    assert final["actual_eta_or_height_computed"] is False
    assert final["previous_tau_full_matrix_and_column_selection_recomputed"] is False
    assert final["old_sigma_coefficients_zero_through_three_recomputed"] is False
    inventory=read(bound(out,final["stage_manifest"]))
    assert inventory["complete"] is True and inventory["configuration"]==tag and inventory["result"]==RESULT
    stages={row["file"]:plain(row) for row in inventory["files"]}
    assert len(stages)==len(inventory["files"])==final["complete_math_stage_count"]
    for name,row in stages.items():
        assert entries[name]==row
        value=read(bound(out,row))
        assert value["complete"] is True and value["configuration"]==tag and value["result"]==RESULT
    def stage(row):
        assert plain(row)==stages[row["file"]]
        return read(bound(out,row))
    audit=stage(final["source_audit"])
    assert audit["previous_actual_tau_rank"]==2431
    assert audit["selected_sigma_first_derivative_columns"]==SIGMA_COLUMNS
    assert audit["original_global_I2_source_completed_by_actual_infinity_minor"] is True
    oldq=stage(final["old_selected_column_quotient"])
    assert oldq["actual_rank"]==2431 and oldq["actual_minor_determinant_mod_prime"]!=0
    assert oldq["all_selected_2431_columns_annihilated_in_all435_rows"] is True
    sigma=stage(final["sigma_shifted_columns"])
    assert sigma["matrix_shape"]==[2866,81]
    assert len(sigma["source_completed_original_sigma_coefficients"])==68
    assert len(sigma["source_new_sigma_coefficients"])==6
    for row in sigma["source_new_sigma_coefficients"]:
        value=stage(row)
        assert value["original_normal_columns"]==SIGMA_COLUMNS
        assert value["all_original_weighted_support_zeros_verified"] is True
        assert value["old_coefficients_zero_through_three_recomputed"] is False
    for row in sigma["source_completed_original_sigma_coefficients"]:
        assert row["producer"]=="R827" and plain(row)==reviewed["R827"]["files"][row["file"]]
    augmentation=stage(final["incremental_rank"])
    assert augmentation["actual_added_rank"]==20 and augmentation["actual_combined_selected_rank"]==2451
    assert len(augmentation["independent_new_sigma_column_indices"])==20
    T11=stage(final["T11_quotient"])
    assert T11[FLAGS[0]] is True and T11["actual_rank"]==2451
    assert T11["actual_minor_determinant_mod_prime"]!=0
    assert T11["actual_20_by20_schur_minor_determinant_mod_prime"]!=0
    assert len(T11["selected_original_rows"])==len(set(T11["selected_original_rows"]))==2451
    assert len(T11["selected_original_tau_columns"])==2431 and len(T11["selected_new_sigma_columns"])==20
    assert len(T11["complement_original_rows"])==415
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
    print("TWO_CHART_COMPLETE_IO_REVIEW="+json.dumps({
        "result":RESULT,"certificate":entries[FINAL],"stage_manifest":plain(final["stage_manifest"]),
        "actual_T11_rank":2451,"new_added_rank":20,"actual_T5_rank":415,"actual_D_kernel_rank":395,
        "D_RR_dimension":295,"complete_stages":len(stages),"manifest_files":len(entries),
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


if __name__=="__main__":
    raise SystemExit(main())
