#!/usr/bin/env python3
"""Pure standard-library original-source transport and six Dstar certificate IO."""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tarfile
import traceback

S=Path(__file__).resolve().parent
REPO=S.parents[2]
TOPIC=REPO/"topics/serre-uniformity"
REQUEST=TOPIC/"notes/R880-six-conjugate-Dstar-public-request.json"
LEGACY_IO_SHA="3a888af1b0ff3339743a1369c416be0d85111562c167260637b4b0da1b52b630"
LEGACY_IO=S/"R880_public_original_D_and_cusp_bounded_RR_inputs.py"
assert hashlib.sha256(LEGACY_IO.read_bytes()).hexdigest()==LEGACY_IO_SHA
_loader=importlib.util.spec_from_file_location("R880_six_Dstar_frozen_standard_library_IO",LEGACY_IO)
W=importlib.util.module_from_spec(_loader);_loader.loader.exec_module(W)
sha,read,save,fingerprint,plain,spec,bound=W.sha,W.read,W.save,W.fingerprint,W.plain,W.spec,W.bound
identity,stable_source,topic_path=W.identity,W.stable_source,W.topic_path
RESULT="R880-original-six-conjugate-Dstar-RR-inputs"
FINAL="p41-original-six-conjugate-Dstar-RR-inputs-certificate.json"
PREFIX="R880-six-Dstar-"
PRIME=1000000753
EPS=[0]+[1]*144+[2]*127
NODES=[0,1,2,3,4]
MULTIPLICITIES=[3,3,2,2,2]
SIGMA_COLUMNS=[0]+list(range(73,92))
LEGACY_SHA="ca46e8f9a9410be240ad77c0863b193e77ef701b06186a31b3edb20eb3e997a4"
PROOF_SHA="b2e523171c08f61b4c1f66ee7738e8fb687f45a3e1dd72ccd6956800cc9d2d84"
PROOFS=("six_D","R880","R887")
SOURCE_GROUPS=("AB","R827","R842","R845","R880","R887","R872")
INPUTS=(
 "seven_inputs","AB_audit","W_reduction","place_audit","g_index","Gamma_index","operator_identity",
 "T11_chart","T5_chart","D_chart","D_matrix","rank1111","old_sections","normal_index","alias_audit",
 "old_anchor_selection","V3_jets","standardizing_kernel","standardizing_basis","old_v","old_w",
 "rank962","old_Dstar","old_principal","u_C","Cstar_principal","Cstar_basis",
 "chi_anchor","chi_divisor","chi_kernel")
STRATEGY={
 "prime":PRIME,"original_zeta_root":549966761,"original_s_root":99932770,
 "original_branch_zero_integral_B_root":3197390,"canonical_free_column":1186,
 "new_branches":"six nonzero original sigma powers, read actual orbit",
 "old_nodes":NODES,"Hasse_multiplicities":MULTIPLICITIES,
 "confluent_polynomial_dimension":12,"old_K0_and_inverse_copied_from_source":True,
 "new_shared_K_and_inverse_jet_orders":"1 through m_i+1",
 "F0_jet_orders":"0 through m_i+1","F1_jet_orders":"0 through m_i","F2_jet_orders":"0 through m_i-1",
 "matrix_entry_degree_bounds":[7,9,11],
 "sigma_first_layer":"z*F1-(5+epsilon_column)*Mg*F0",
 "original_sigma_generator_columns":SIGMA_COLUMNS,
 "selected_T11_shape":[2866,2451],"T11_quotient_shape":[415,2866],
 "T5_two_pencil_shape":[830,1234],"T5_quotient_shape":[415,1234],
 "D_constraint_shape":[830,690],"D_basis_dimension":295,
 "original_1111_kernel_dimension":269,"point_jet_constraint_shape":[123,269],
 "standardizing_dimension":146,"new_Dstar_kernel_dimension":418,
 "all_original_pivot_rows_columns_free_coordinates_v_and_trial_preserved":True,
 "no_new_rank_selection_defines_conjugate_objects":True,
 "same_original_82_scales_preserved_without_extra_multiplication":True,
 "old_S5_products_and_inverse_normal_conversion_and_point_jets_recomputed":False,
 "old_branch_zero_RR_or_products_recomputed":False,
 "complete_new_relation_residuals_required":True,
 "exact_objects":"Galois images of the original fixed unit-solve expressions",
 "modular_arrays_are_not_reconstructed_characteristic_zero_coefficients":True,
 "new_principal_function":"(a_j/v_j)^3*(u_C/tau^2)/(u_chi/tau^2)^4",
 "new_principal_rho_order":-1205,
 "new_t_parameter_or_Picard_height_computed":False,
 "only_budget_branch_limit_and_transport_excluded_from_identity":True,
}

MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
INVENTORY=PREFIX+"original-source-inventory.json"
RETAINED_RECEIPT=PREFIX+"retained-inputs-receipt.json"
AB_BUNDLE=PREFIX+"AB-selected-original-inputs.tar.gz"
AB_RECEIPT=PREFIX+"AB-original-input-receipt.json"

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "legacy_R880_core_sha256":LEGACY_SHA,"method_sha256":item["method_sha256"],
        "proofs_sha256":{k:item["proofs"][k]["sha256"] for k in PROOFS},
        "sources":{k:stable_source(item["sources"][k]) for k in SOURCE_GROUPS},
        "inputs":item["inputs"],"normal_basis_degrees":EPS,"strategy":STRATEGY}

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
    assert request.resolve()==REQUEST.resolve()
    assert item["schema"]==1 and item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["core"]=="R880_original_six_conjugate_Dstar_RR_inputs.py"
    assert sha(S/item["core"])==item["core_sha256"]
    assert item["legacy_R880_core_sha256"]==sha(S/"R880_original_D_and_cusp_bounded_RR_inputs.py")==LEGACY_SHA
    assert item["legacy_R880_IO_sha256"]==LEGACY_IO_SHA
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    assert set(item["proofs"])==set(PROOFS)
    assert item["proofs"]["six_D"]["sha256"]==PROOF_SHA
    for value in item["proofs"].values():assert sha(topic_path(value["path"]))==value["sha256"]
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert isinstance(item["session"],str) and item["session"]
    assert set(item["sources"])==set(SOURCE_GROUPS) and set(item["input_selectors"])==set(INPUTS)
    assert set(item["intakes"])=={"fixed_five","R827"}
    assert 0<item["budget_minutes"]<=300 and 1<=item["maximum_branches"]<=6
    assert item["resume"] is None or isinstance(item["resume"],dict)
    return W.load_IO(item)

def output_manifest(out):
    entries=[dict(spec(path),included_in_git=False) for path in sorted(out.iterdir())
        if path.is_file() and path.name not in (MANIFEST,REFERENCE) and not path.name.endswith(".tmp")]
    save(out/MANIFEST,{"result":RESULT,"files":entries,
        "temporary_active_checkpoint_retention_days":1,"reproducible_data_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,**spec(out/MANIFEST)})

def inspect_manifest(out):
    value=read(out/MANIFEST);assert value["result"]==RESULT
    files={v["file"]:plain(v) for v in value["files"]}
    assert len(files)==len(value["files"])
    actual={p.name for p in out.iterdir() if p.is_file() and p.name not in (MANIFEST,REFERENCE)
            and not p.name.endswith(".tmp")}
    assert actual==set(files)
    for v in files.values():bound(out,v)
    reference=read(out/REFERENCE);assert reference["result"]==RESULT
    assert plain(reference)==spec(out/MANIFEST)
    return files

def index_output_spec(key,transport):
    ref=plain(transport["source_index"])
    assert ref["file"]=="intake-source-index.json"
    return dict(ref,file=PREFIX+"transport-"+key+"-source-index.json")

def checked_index(item,key,folder):
    transport=item["intakes"][key]
    value=read(bound(folder,index_output_spec(key,transport)))
    assert value["schema"]==1 and value["new_mathematics_executed"] is False
    assert str(value["workflow_run_id"])==str(transport["run_id"])
    assert value["source_commit"]==transport["source_commit"]
    assert value["request_sha256"]==transport["request_sha256"]
    errors=value["errors"]
    assert isinstance(errors,list)
    assert [x["label"] for x in errors]==transport["expected_error_labels"]
    entries={x["label"]:x for x in value["sources"]}
    assert len(entries)==len(value["sources"])
    assert set(entries)==set(transport["source_labels"])
    assert not(set(entries)&set(transport["expected_error_labels"]))
    for label,entry in entries.items():
        assert label in SOURCE_GROUPS and label!="AB"
        assert identity(entry["source"])==identity(item["sources"][label])
        assert plain(entry["retained_input_bundle"])==plain(transport["bundles"][label])
    return value,entries

def download_intakes(item,out,work,IO):
    receipts={}
    for key,transport in item["intakes"].items():
        archive=IO.Archive(transport,work/("transport-"+key),whole=True)
        try:
            remote=plain(transport["source_index"]);local=index_output_spec(key,transport)
            archive.extract_bound(remote["file"],remote["sha256"],out/local["file"],remote["bytes"])
            index,entries=checked_index(item,key,out)
            wanted={remote["file"]}
            for label,entry in entries.items():
                for kind in ("summary","retained_input_bundle"):
                    ref=plain(entry[kind]);wanted.add(ref["file"])
                    archive.extract_bound(ref["file"],ref["sha256"],out/ref["file"],ref["bytes"])
            assert set(archive.by_name)==wanted
            receipts[key]=archive.receipt()
        finally:archive.close()
    return receipts

def make_AB_bundle(directory,files,out):
    path=out/AB_BUNDLE
    if path.exists():return spec(path)
    temporary=path.with_name(path.name+".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw,filename="",mtime=0,compresslevel=1) as zipped:
            with tarfile.open(fileobj=zipped,mode="w|") as tar:
                for name,ref in sorted(files.items()):
                    source=bound(directory,ref)
                    entry=tarfile.TarInfo("original/"+name)
                    entry.size=ref["bytes"];entry.mode=0o444;entry.mtime=0;entry.uid=entry.gid=0
                    entry.uname=entry.gname=""
                    with source.open("rb") as stream:tar.addfile(entry,stream)
    temporary.replace(path)
    return spec(path)

def direct_AB(item,out,work,IO):
    raw=item["sources"]["AB"];folder=work/"retained"/"AB";folder.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(raw,work/"AB-direct-transport",whole=False)
    try:
        manifest={"file":MANIFEST,"bytes":raw["manifest_bytes"],"sha256":raw["manifest_sha256"]}
        archive.extract_bound(MANIFEST,manifest["sha256"],folder/MANIFEST,manifest["bytes"])
        body=read(folder/MANIFEST);assert body["result"]==raw["result"]
        indexed={x["file"]:plain(x) for x in body["files"]}
        assert len(indexed)==len(body["files"])==raw["manifest_file_count"]
        assert set(archive.by_name)==set(indexed)|{MANIFEST,REFERENCE}
        reference=plain(raw["manifest_reference"])
        assert reference["file"]==REFERENCE
        archive.extract_bound(REFERENCE,reference["sha256"],folder/REFERENCE,reference["bytes"])
        files={MANIFEST:manifest,REFERENCE:reference}
        for name in raw["selected_file_names"]:
            W.safe_name(name)
            if name in files:continue
            ref=indexed[name]
            archive.extract_bound(name,ref["sha256"],folder/name,ref["bytes"])
            files[name]=ref
        assert set(files)==set(raw["selected_file_names"])
        assert len(files)==raw["expected_selected_file_count"]
        for name,ref in raw.get("file_pins",{}).items():assert files[name]==plain(ref)
        value=dict(raw,directory=str(folder),files=files,selected_file_count=len(files),
                   selected_files_sha256=fingerprint(files))
        tag=W.review_original("AB",value)
        certificate=read(bound(folder,value["certificate"]))
        assert certificate["all_seven_original_Galois_normal_inputs_certified"] is True
        assert certificate["all1380_by12_original_coordinates_verified"] is True
        assert certificate["original_Galois_seven_cycle_certified"] is True
        bundle=make_AB_bundle(folder,files,out)
        receipt={"result":RESULT,"source_group":"AB","original_producer":identity(raw),
                 "source_configuration_sha256":fingerprint(tag),"selected_files":files,
                 "selected_file_count":len(files),"selected_files_sha256":fingerprint(files),
                 "original_input_bundle":bundle,"archive_transport":archive.receipt(),
                 "all_selected_original_member_bytes_and_SHA_verified":True,
                 "complete_original_archive_downloaded_or_rehashed":False,
                 "new_mathematics_executed":False}
        save(out/AB_RECEIPT,receipt)
        return receipt["archive_transport"]
    finally:archive.close()

def prepare_sources(item,out,work):
    sources={};tags={};entries_all={};summaries={};all_transport_refs=[]
    for key in item["intakes"]:
        _,entries=checked_index(item,key,out)
        all_transport_refs.append(index_output_spec(key,item["intakes"][key]))
        for label,entry in entries.items():
            assert label not in entries_all;entries_all[label]=entry
            summary=read(bound(out,entry["summary"]));summaries[label]=summary
            raw=item["sources"][label]
            assert summary["label"]==label and summary["original_result"]==raw["result"]
            assert summary["new_mathematics_executed"] is False and summary["source"]==entry["source"]
            assert summary["source_core_sha256"]==raw["core_sha256"]
            assert summary["source_wrapper_sha256"]==raw["wrapper_sha256"]
            assert summary["manifest"]["sha256"]==raw["manifest_sha256"]
            assert summary["manifest"]["bytes"]==raw["manifest_bytes"]
            assert summary["original_manifest_count"]==raw["manifest_file_count"]
            carrier=plain(entry["retained_input_bundle"])
            assert carrier==plain(summary["retained_input_bundle"])
            files={name:plain(v) for name,v in summary["selected_files"].items()}
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
            tags[label]=W.review_original(label,value);sources[label]=value
            all_transport_refs.extend([plain(entry["summary"]),carrier])
    assert set(sources)==set(SOURCE_GROUPS)-{"AB"}
    abr=read(out/AB_RECEIPT);raw=item["sources"]["AB"]
    assert abr["result"]==RESULT and abr["source_group"]=="AB"
    assert abr["original_producer"]==identity(raw) and abr["new_mathematics_executed"] is False
    assert abr["all_selected_original_member_bytes_and_SHA_verified"] is True
    assert abr["complete_original_archive_downloaded_or_rehashed"] is False
    files={name:plain(v) for name,v in abr["selected_files"].items()}
    assert len(files)==abr["selected_file_count"]==raw["expected_selected_file_count"]
    assert fingerprint(files)==abr["selected_files_sha256"]
    assert set(files)==set(raw["selected_file_names"])
    for name,pin in raw.get("file_pins",{}).items():assert files[name]==plain(pin)
    carrier=plain(abr["original_input_bundle"]);assert carrier["file"]==AB_BUNDLE
    directory=work/"retained"/"AB"
    W.unpack_source(bound(out,carrier),directory,files)
    value=dict(raw,directory=str(directory),files=files,selected_file_count=len(files),
               selected_files_sha256=fingerprint(files))
    tags["AB"]=W.review_original("AB",value);sources["AB"]=value
    assert abr["source_configuration_sha256"]==fingerprint(tags["AB"])
    all_transport_refs.extend([spec(out/AB_RECEIPT),carrier])
    assert set(sources)==set(SOURCE_GROUPS)
    def same(record,label):
        assert identity(record)==identity(sources[label])
        if record.get("configuration_sha256") is not None:
            assert record["configuration_sha256"]==sources[label]["configuration_sha256"]
    for label in ("R827","R842","R845","R872"):same(tags["R880"]["sources"][label],label)
    for label in ("R827","R842"):same(tags["R845"]["sources"][label],label)
    same(tags["R842"]["sources"]["R827"],"R827")
    same(tags["R872"]["sources"]["R827"],"R827")
    for label in ("R827","R842"):same(tags["AB"]["sources"][label],label)
    same(tags["R887"]["sources"]["R880"],"R880")
    inputs={}
    for key,selector in item["input_selectors"].items():
        label,name=selector["source_group"],selector["file"]
        assert label in sources and name in sources[label]["files"]
        ref=sources[label]["files"][name]
        for field in ("bytes","sha256"):
            if field in selector:assert selector[field]==ref[field]
        inputs[key]={"source_group":label,**ref}
    expanded=dict(item,sources=sources,inputs=inputs)
    expanded["method"]=str(topic_path(item["method"]))
    expanded["proofs"]={k:{**v,"path":str(topic_path(v["path"]))} for k,v in item["proofs"].items()}
    stable={label:stable_source(v) for label,v in sources.items()}
    total=sum(v["selected_file_count"] for v in sources.values())
    assert total==item["expected_total_selected_file_count"]
    inventory={"result":RESULT,"source_identities":stable,
        "selected_files":{k:v["files"] for k,v in sources.items()},
        "actual_selected_source_count":total,"new_mathematics_executed":False}
    receipt={"result":RESULT,"complete":True,"original_source_identities":stable,
        "actual_selected_source_count":total,"source_transport_files":all_transport_refs,
        "intake_original_carriers":{k:plain(v["retained_input_bundle"]) for k,v in entries_all.items()},
        "AB_original_carrier":carrier,"AB_input_receipt":spec(out/AB_RECEIPT),
        "all_selected_original_members_bytes_and_SHA_verified":True,
        "all_original_source_tags_preserved":True,"new_mathematics_executed":False}
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
        ms=plain(source["manifest"]);assert ms["file"]==MANIFEST
        archive.extract_bound(MANIFEST,ms["sha256"],folder/MANIFEST,ms["bytes"])
        value=read(folder/MANIFEST);assert value["result"]==RESULT
        files={v["file"]:plain(v) for v in value["files"]}
        assert len(files)==len(value["files"])
        assert set(archive.by_name)==set(files)|{MANIFEST,REFERENCE}
        for ref in files.values():
            archive.extract_bound(ref["file"],ref["sha256"],folder/ref["file"],ref["bytes"])
        entry=archive.by_name[REFERENCE];assert len(entry)==1 and entry[0].file_size<1000000
        (folder/REFERENCE).write_bytes(archive.zip.read(entry[0]))
        reference=read(folder/REFERENCE);assert reference["result"]==RESULT and plain(reference)==ms
        old,run=read(folder/META[0]),read(folder/META[1])
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
        needed=[]
        for key,transport in item["intakes"].items():
            index,entries=checked_index(item,key,folder)
            needed.append(index_output_spec(key,transport))
            for entry in entries.values():needed.extend([plain(entry["summary"]),plain(entry["retained_input_bundle"])])
        assert AB_RECEIPT in files
        abr=read(folder/AB_RECEIPT)
        needed.extend([files[AB_RECEIPT],plain(abr["original_input_bundle"])])
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
            for key in ("source_audit","Hasse_interpolation","resume_state"):bound(out,final[key])
            for record in final["completed_new_conjugate_inputs"]:bound(out,record["stage"])
            shutil.copyfile(folder/FINAL,out/FINAL)
        # A false FINAL is historical; it is never copied as a completed endpoint.

def compute(item,out,request,IO):
    out.mkdir(parents=True,exist_ok=True)
    work=out.parent/"R880-six-Dstar-working";work.mkdir(parents=True,exist_ok=True)
    code=1;error=None;outer=False;expanded=None;tag=None;child=None;transport=None
    try:
        previous=restore_archive(item,out,work,IO)
        if previous is None:
            transport={"completed_intakes":download_intakes(item,out,work,IO),
                       "original_AB_direct":direct_AB(item,out,work,IO)}
        else:transport={"resume":previous["transport"]}
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
            for line in (out/"core.log").read_text(errors="replace").splitlines()[-22:]:
                if len(line)<=2400:print(line,flush=True)
        if (out/META[2]).exists():
            print("R880_SIX_DSTAR_CORE_RECEIPT="+json.dumps(read(out/META[2]),sort_keys=True),flush=True)
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
            "actual_new_complete_Dstar_count":final["actual_new_complete_Dstar_count"] if final else 0,
            "all_seven_original_Dstar_inputs_certified":bool(final and final["all_seven_original_Dstar_inputs_certified"]),
            "original_five_Lj_RR128_or_144_or_height_computed":False,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    return code

def dimensions(value,h,w):
    assert isinstance(value,list) and len(value)==h
    assert all(isinstance(row,list) and len(row)==w for row in value)

def verify(item,out,request,IO):
    files=inspect_manifest(out);run=read(out/META[1])
    assert run["result"]==RESULT and run["source_commit"]==os.environ["GITHUB_SHA"]
    assert str(run["workflow_run_id"])==os.environ["GITHUB_RUN_ID"]
    if META[0] not in files:
        assert run["complete"] is False and run["process_exit_code"]!=0
        assert run["core_receipt_sha256"] is None
        print("R880_SIX_DSTAR_VERIFY="+json.dumps({"complete":False,"source_preparation_failed":True,
            "all_existing_output_bytes_verified":True,"new_mathematics_executed":False}),flush=True)
        return 0
    expanded,source_receipt=prepare_sources(item,out,out.parent/"R880-six-Dstar-verification")
    tag=expected_tag(expanded);initial=read(out/META[0])
    assert initial["result"]==RESULT and initial["source_commit"]==os.environ["GITHUB_SHA"]
    assert initial["core_sha256"]==item["core_sha256"] and initial["driver_sha256"]==item["wrapper_sha256"]
    assert initial["request_sha256"]==sha(request) and initial["job"]==item
    assert initial["actual_configuration"]==tag
    assert files[INVENTORY]==spec(out/INVENTORY) and files[RETAINED_RECEIPT]==spec(out/RETAINED_RECEIPT)
    assert initial["actual_source_inventory"]==files[INVENTORY] and initial["retained_inputs"]==files[RETAINED_RECEIPT]
    original_maps={k:v["files"] for k,v in expanded["sources"].items()}
    def references(value):
        if isinstance(value,dict):
            if all(k in value for k in ("file","bytes","sha256")):
                pin=plain(value);name=pin["file"]
                if "source_group" in value:
                    assert original_maps[value["source_group"]][name]==pin
                elif name.startswith(PREFIX) and name.endswith(".json.gz"):
                    assert files[name]==pin
                else:
                    assert any(group.get(name)==pin for group in original_maps.values()),name
                return
            for key,v in value.items():
                if key!="configuration":references(v)
        elif isinstance(value,list) and value and isinstance(value[0],dict):
            for v in value:references(v)
    complete_stages={};false_stages=[]
    for name,ref in files.items():
        if not(name.startswith(PREFIX) and name.endswith(".json.gz")):continue
        value=read(out/name)
        assert value["result"]==RESULT and value["configuration"]==tag
        if name==PREFIX+"current.json.gz":
            assert value["complete"] is False and isinstance(value["status"],str)
            assert isinstance(value["completed_branches"],list) and len(value["completed_branches"])<=6
        else:
            assert value["complete"] is True
            if name!=PREFIX+"stage-manifest.json.gz":complete_stages[name]=ref
            if value.get("accepted") is False:false_stages.append(name)
        references(value)
    def stage(ref):
        ref=plain(ref);assert files[ref["file"]]==ref
        value=read(bound(out,ref))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        return value
    def original(ref):
        label=ref["source_group"];assert label in SOURCE_GROUPS
        pin=plain(ref);value=expanded["sources"][label]
        assert value["files"][pin["file"]]==pin
        return read(bound(value["directory"],pin))
    core=read(out/META[2]) if META[2] in files else None
    if core is not None:
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        assert files[META[2]]["sha256"]==run["core_receipt_sha256"]
        assert core["configuration_sha256"] in (None,fingerprint(tag))
        assert core["old_branch_zero_or_original_Krylov_inverse_recomputed"] is False
        assert core["original_five_Lj_RR128_or_144_or_height_computed"] is False
    else:assert run["complete"] is False and run["core_receipt_sha256"] is None
    final=read(out/FINAL) if FINAL in files else None
    if final is None:
        assert run["complete"] is False
    else:
        assert final["result"]==RESULT and final["configuration"]==tag
        for key in ("old_branch_zero_arithmetic_recomputed","old_S5_products_Krylov_inverses_or_P0_jets_recomputed",
                    "actual_norm_polynomial_or_complete_five_Lj_RR128_or_144_computed",
                    "expanded_characteristic_zero_coordinates_computed","new_original_t_frame_values_computed",
                    "connection_Poincare_period_or_height_computed"):
            assert final[key] is False
        if final["complete"] is True:
            assert run["complete"] is True and run["process_exit_code"]==0 and run["error"] is None
            assert core is not None and core["complete"] is True and core["exit_code"]==0 and core["error"] is None
            assert core["certificate_sha256"]==files[FINAL]["sha256"]
            assert core["configuration_sha256"]==fingerprint(tag)
            assert final["p"]==41 and final["prime"]==PRIME and final["stop_reason"] is None
            assert final["actual_new_complete_Dstar_count"]==core["actual_new_complete_Dstar_count"]==run["actual_new_complete_Dstar_count"]==6
            assert final["all_six_new_Dstar_418_spaces_certified"] is True
            assert final["all_seven_original_Dstar_inputs_certified"] is core["all_seven_original_Dstar_inputs_certified"] is run["all_seven_original_Dstar_inputs_certified"] is True
            assert not false_stages
            inventory=stage(final["stage_manifest"])
            indexed={x["file"]:plain(x) for x in inventory["files"]}
            assert len(indexed)==len(inventory["files"]) and indexed==complete_stages
            assert inventory["all_actual_complete_stages_retained"] is True and inventory["current_excluded"] is True
            references(final)
            assert plain(final["resume_state"])==files[PREFIX+"current.json.gz"]
            current=read(bound(out,final["resume_state"]))
            assert current["completed_branches"]==final["completed_new_conjugate_inputs"]
            for key,input_key in (("original_branch_zero_Dstar","old_Dstar"),("original_branch_zero_Qtilde","Cstar_principal"),
                                  ("common_Cstar_418","Cstar_basis"),("common_Dchi_418","chi_kernel"),
                                  ("original_seven_Galois_order","seven_inputs")):
                assert final[key]==expanded["inputs"][input_key]
            audit=stage(final["source_audit"])
            assert audit["prime"]==PRIME and audit["input_references"]==expanded["inputs"]
            assert audit["source_identities"]==tag["sources"]
            for key in ("all_six_original_B_unit_solve_reductions_bound","original_K_place_and_scales_preserved",
                        "original_selected_charts_and_all_free_coordinates_unchanged",
                        "exact_objects_are_conjugates_of_original_characteristic_zero_unit_solves"):
                assert audit[key] is True
            assert audit["old_operator_K0_inverse_S5_products_normal_conversion_and_point_jets_recomputed"] is False
            hasse=stage(final["Hasse_interpolation"])
            assert hasse["condition_labels"]==[[i,n] for i,m in enumerate(MULTIPLICITIES) for n in range(m)]
            dimensions(hasse["matrix_mod_prime"],12,12);dimensions(hasse["inverse_mod_prime"],12,12)
            assert hasse["both_inverse_products_verified"] is True and hasse["Hasse_coefficients_not_unscaled_derivative_values"] is True
            assert hasse["new_Krylov_inverse_computed"] is False
            seven=original(expanded["inputs"]["seven_inputs"]);records=seven["ordered_original_sigma_powers"][1:]
            assert len(records)==6
            completed=final["completed_new_conjugate_inputs"]
            assert [v["sigma_power"] for v in completed]==[v["sigma_power"] for v in records]==list(range(1,7))
            assert [v["original_branch"] for v in completed]==[v["original_branch"] for v in records]
            for actual,old in zip(completed,records):
                assert actual["roots_B_s"]==old["roots_B_s"]
                branch=stage(actual["stage"])
                assert branch["original_branch"]==old["original_branch"] and branch["sigma_power"]==old["sigma_power"]
                assert branch["roots_B_s"]==old["roots_B_s"]
                pair={"source_group":"AB",**plain(old["source_original_normal_pair"])}
                assert branch["source_original_normal_B"]==pair
                assert branch["complete_original_conjugate_Dstar_418_certified"] is True
                assert branch["same_original_zero_branch_unit_diagram_conjugated"] is True
                assert branch["old_branch_zero_arithmetic_recomputed"] is False
                assert branch["expanded_characteristic_zero_coefficients_computed"] is False
                verify_branch(branch,stage,original,expanded,pair,old)
        else:
            assert run["complete"] is False and 0<=final["actual_new_complete_Dstar_count"]<=6
            for record in final["completed_new_conjugate_inputs"]:
                branch=stage(record["stage"])
                assert branch["complete_original_conjugate_Dstar_418_certified"] is True
    print("R880_SIX_DSTAR_VERIFY="+json.dumps({"result":RESULT,
        "complete":bool(final and final["complete"]),"actual_complete_math_stage_count":len(complete_stages),
        "actual_selected_source_count":source_receipt["actual_selected_source_count"],
        "actual_new_complete_Dstar_count":final["actual_new_complete_Dstar_count"] if final else 0,
        "all_seven_original_Dstar_inputs_certified":bool(final and final["all_seven_original_Dstar_inputs_certified"]),
        "old_branch_zero_arithmetic_recomputed":False,"original_five_Lj_RR128_or_144_or_height_computed":False,
        "new_mathematics_executed_in_verifier":False},sort_keys=True),flush=True)
    return 0

def verify_branch(branch,stage,original,expanded,pair,orbit):
    assert branch["prime"]==PRIME
    for key in ("F0","F1","F2","sigma1"):
        index=stage(branch["source_polynomial_layers"][key])
        assert index["prime"]==PRIME and index["original_branch"]==orbit["original_branch"]
        assert index["sigma_power"]==orbit["sigma_power"] and index["source_original_B"]==pair
        assert index["target"]==key and index["normal_basis_degrees"]==EPS
        assert index["all_weighted_support_zeros_verified"] is True
        assert index["true_original_polynomial_reduction_certified"] is True
        degree=7 if key=="sigma1" else 5+2*int(key[-1]);width=20 if key=="sigma1" else 272
        assert index["regular_degree_bound"]==degree and len(index["row_blocks"])==16
        count=0
        for ref in index["row_blocks"]:
            block=stage(ref)
            assert block["row_first"]==count and block["row_stop"]==min(count+17,272)
            assert block["target"]==key and block["source_original_B"]==pair
            assert block["all_original_weighted_degree_zeros_verified"] is True
            assert block["exact_original_polynomial_reduction_certified"] is True
            assert block["characteristic_zero_coefficients_reconstructed"] is False
            assert len(block["source_twelve_Hasse_conditions"])==12
            assert len(block["coefficient_matrices_low_to_high"])==degree+3
            for value in block["coefficient_matrices_low_to_high"]:
                dimensions(value,block["row_stop"]-count,width)
            if key=="sigma1":
                assert block["original_normal_columns"]==SIGMA_COLUMNS
                assert block["original_sigma_highest_layer_cancellation_verified"] is True
            else:assert block["original_normal_columns"]==list(range(272))
            count=block["row_stop"]
        assert count==272
    derivatives=stage(branch["original_B_derivative_vectors"])
    assert derivatives["source_original_B"]==pair
    assert derivatives["source_F1"]==branch["source_polynomial_layers"]["F1"]
    assert derivatives["source_F2"]==branch["source_polynomial_layers"]["F2"]
    dimensions(derivatives["delta_B_coefficients_mod_prime"],8,272)
    dimensions(derivatives["delta2_B_coefficients_mod_prime"],10,272)
    assert derivatives["first_column_copied_from_actual_completed_derivative_matrices"] is True
    assert derivatives["additional_derivative_arithmetic_computed"] is False
    t11=stage(branch["complete_T11_quotient"])
    assert t11["matrix_shape"]==[415,2866]
    dimensions(t11["quotient_matrix_mod_prime"],415,2866)
    for key in ("all2451_columns_annihilated_in_all415_rows","complement_identity_verified",
                "same_original_quotient_coordinates_under_sigma","complete_original_two_chart_space_certified"):
        assert t11[key] is True
    assert t11["exact_kernel_dimension"]==2451
    oldchart=original(expanded["inputs"]["T11_chart"])
    assert t11["selected_original_rows"]==oldchart["selected_original_rows"]
    assert t11["complement_original_rows"]==oldchart["complement_original_rows"]
    columns=stage(t11["source_T11_columns"])
    assert columns["matrix_shape"]==[2866,2451]
    dimensions(columns["matrix_mod_prime"],2866,2451)
    assert columns["selected_original_tau_columns"]==oldchart["selected_original_tau_columns"]
    assert columns["selected_new_sigma_columns"]==oldchart["selected_new_sigma_columns"]
    assert columns["only_2451_original_selected_columns_materialized"] is True
    assert columns["source_polynomial_layers"]==branch["source_polynomial_layers"]
    t5=stage(branch["complete_T5_quotient"])
    assert t5["matrix_shape"]==[415,1234] and t5["exact_rank"]==415
    dimensions(t5["quotient_matrix_mod_prime"],415,1234)
    assert t5["all830_by1234_original_rows_reconstructed"] is True
    assert t5["same_original_selected_rows_under_sigma"] is True
    assert stage(t5["source_two_pencil_matrix"])["source_T11_quotient"]==branch["complete_T11_quotient"]
    def kernel(ref,shape0,dimension):
        value=stage(ref)
        assert value["matrix_shape"]==shape0 and value["actual_kernel_dimension"]==dimension
        assert value["actual_rank"]==shape0[1]-dimension
        dimensions(value["kernel_basis_mod_prime"],shape0[1],dimension)
        assert value["all_original_matrix_equations_verified"] is True
        assert value["free_identity_verified"] is True
        assert value["complete_original_conjugate_kernel_certified"] is True
        solve=stage(value["source_selected_solve"])
        assert solve["accepted"] is True and solve["selected_square_reduced_to_identity"] is True
        assert solve["all_selected_equations_verified"] is True
        assert solve["original_pivot_selection_recomputed"] is False
        assert solve["unconsumed_full_inverse_or_determinant_computed"] is False
        return value
    dk=kernel(branch["complete_original_D_295_basis"],[830,690],295)
    oldd=original(expanded["inputs"]["D_chart"])
    assert dk["selected_rows"]==oldd["selected_original_equation_rows"]
    assert dk["selected_columns"]==oldd["selected_original_V3_pivot_columns"]
    assert dk["free_columns"]==oldd["original_V3_free_columns"]
    ab=stage(branch["original_a_b_sections"])
    assert ab["accepted"] is True and ab["original_a_basis_column"]==0
    assert ab["original_b_basis_coefficients"]==[1]*295
    assert ab["block_swap_used"] is False and ab["no_rescaling"] is True
    assert ab["a_value_at_P0_mod_prime"]!=0
    for key in ("a_original_V3_coordinates_mod_prime","b_original_V3_coordinates_mod_prime",
                "a_normal_V3_coordinates_mod_prime","b_normal_V3_coordinates_mod_prime"):
        dimensions(ab[key],690,1)
    assert ab["source_complete_original_D_basis"]==branch["complete_original_D_295_basis"]
    f=stage(branch["complete_residual_F_269_basis"])
    assert f["actual_projected_rank"]==269 and f["complete_RR_space_certified"] is True
    dimensions(f["original_V3_basis_mod_prime"],690,269)
    dimensions(f["normal_V3_basis_mod_prime"],690,269)
    fkernel=kernel(f["source_complete_kernel"],[1360,1380],269)
    old1111=original(expanded["inputs"]["rank1111"])
    assert fkernel["selected_rows"]==old1111["selected_original_fiber_rows"]
    assert fkernel["selected_columns"]==old1111["selected_original_V3_pair_columns"]
    standard=stage(branch["complete_standardizing_146_basis"])
    assert standard["accepted"] is True and standard["dimension"]==146
    assert standard["actual_complete_standardizing_RR_space_certified"] is True
    assert standard["source_residual_F_space"]==branch["complete_residual_F_269_basis"]
    assert standard["original_v_column_reselected"] is False and standard["selected_column_rescaled"] is False
    dimensions(standard["original_V3_basis_mod_prime"],690,146)
    dimensions(standard["normal_V3_basis_mod_prime"],690,146)
    sk=kernel(standard["source_complete_146_kernel"],[123,269],146)
    olds=original(expanded["inputs"]["standardizing_kernel"])
    assert sk["selected_rows"]==olds["selected_row_indices"]
    assert sk["selected_columns"]==olds["selected_pivot_columns"] and sk["free_columns"]==olds["free_columns"]
    oldbasis=original(expanded["inputs"]["standardizing_basis"])
    vindex=oldbasis["selected_first_order123_unit_column"]
    assert standard["selected_original_v_column"]==vindex
    assert len(standard["order123_coefficients_mod_prime"])==146
    assert standard["order123_coefficients_mod_prime"][vindex]!=0
    for which in ("v","w"):
        value=stage(branch["original_"+which])
        assert value["source_complete_standardizing_space"]==branch["complete_standardizing_146_basis"]
        assert value["which"]==which
        assert value["standardizing_basis_coefficients_mod_prime"]==(
            [int(i==vindex) for i in range(146)] if which=="v" else [1]*146)
        assert value["no_rescaling_or_new_column_selection"] is True
        assert value["order_at_original_P0_at_least123"] is True
        dimensions(value["original_V3_coordinates_mod_prime"],690,1)
        dimensions(value["normal_V3_coordinates_mod_prime"],690,1)
        if which=="v":assert value["order123_is_exact"] is True and value["order123_coefficient_mod_prime"]!=0
        else:assert value["trial"]==1
    dstar=stage(branch["complete_Dstar_418_basis"])
    assert dstar["accepted"] is True and dstar["actual_projected_rank"]==418
    assert dstar["matrix_shape"]==[690,418] and dstar["complete_RR_space_certified"] is True
    dimensions(dstar["original_V3_basis_mod_prime"],690,418)
    dimensions(dstar["normal_V3_basis_mod_prime"],690,418)
    assert dstar["new_projected_independence_rows_only_witness_no_basis_change"] is True
    assert dstar["exact_RR_space"]["degree_Dstar"]==272 and dstar["exact_RR_space"]["P0_not_in_Dstar"] is True
    assert dstar["source_complete_kernel"]==branch["complete_Dstar_relation_kernel"]
    relation=kernel(branch["complete_Dstar_relation_kernel"],[1360,1380],418)
    assert relation["source_references"]["source_matrix"]==branch["complete_new_two_anchor_matrix"]
    old962=original(expanded["inputs"]["rank962"])
    assert relation["selected_rows"]==old962["selected_rows"] and relation["selected_columns"]==old962["selected_columns"]
    pencil=stage(branch["complete_new_two_anchor_matrix"])
    assert pencil["matrix_shape"]==[1360,1380]
    assert pencil["source_left"]==branch["original_v"] and pencil["source_right"]==branch["original_w"]
    assert pencil["fiber_disjointness_or_reducedness_not_assumed"] is True
    assert pencil["complete_original_two_section_multiplication_evaluated"] is True
    assert [x["z0"] for x in pencil["source_fiber_products"]]==NODES
    principal=stage(branch["original_principal_input"])
    assert principal["source_complete_Dstar"]==branch["complete_Dstar_418_basis"]
    assert principal["source_actual_a"]==branch["original_a_b_sections"]
    assert principal["source_actual_v"]==branch["original_v"]
    assert principal["source_original_common_u_C"]==expanded["inputs"]["u_C"]
    assert principal["source_original_common_u_chi"]==expanded["inputs"]["chi_anchor"]
    assert principal["source_complete_common_Cstar"]==expanded["inputs"]["Cstar_basis"]
    assert principal["source_complete_common_Dchi"]==expanded["inputs"]["chi_kernel"]
    assert principal["actual_rho_order"]==-1205 and principal["actual_leading_coefficient_mod_prime"]!=0
    assert principal["principal_factor_direction"]=="positive multiplication"
    assert principal["exact_original_Galois_conjugate_not_a_new_linearly_equivalent_choice"] is True
    assert principal["all_original_free_coordinates_and_section_scales_preserved"] is True
    for key in ("original_t_frame_value_computed","new_t_parameter_jets_computed",
                "five_original_Lj_RR128_or_144_computed","connection_Poincare_period_or_height_computed"):
        assert principal[key] is False

def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("action",choices=("compute","verify"))
    parser.add_argument("--request",required=True);parser.add_argument("--output",required=True)
    args=parser.parse_args()
    request=Path(args.request);item=read(request);out=Path(args.output)
    IO=guard(item,request)
    if args.action=="compute":return compute(item,out,request,IO)
    return verify(item,out,request,IO)

if __name__=="__main__":
    raise SystemExit(main())
