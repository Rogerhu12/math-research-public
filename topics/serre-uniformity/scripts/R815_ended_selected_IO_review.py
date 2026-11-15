#!/usr/bin/env python3
"""Selected IO review of one ended original R815 run; no mathematical core import."""
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re

S=Path(__file__).resolve().parent
REPO=S.parents[2]
TOPIC=REPO/"topics/serre-uniformity"
IO_NAME="R824_public_original_global_polar_generators.py"
IO_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
ORIGINAL="R815-original-normal-derivation-operators"
RESULT="R815-ended-run-selected-IO-review"
FINAL="p41-original-normal-derivation-operator-certificate.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R815-retained-producer-inputs.tar.gz"
CORE_SHA="80516ff9598fdb6251628c00794dc3529b998a7c563fe80fd9c31406e3896c7d"
WRAPPER_SHA="ab725da038ec458493f461088ceee0fd105e0dc90cbfb4ad6f3047cbec90b454"
FRAMEWORK_SHA="849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3"
TARGETS=("g","Gamma")
EPS=[0]+[1]*144+[2]*127
SMALL_LIMIT=64*1024*1024

def sha(path):
    digest=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1024*1024),b""):digest.update(block)
    return digest.hexdigest()

assert sha(S/IO_NAME)==IO_SHA
loader=importlib.util.spec_from_file_location("R815_ended_run_frozen_range_IO",S/IO_NAME)
IO=importlib.util.module_from_spec(loader)
loader.loader.exec_module(IO)
read,save,spec,plain=IO.read,IO.save,IO.file_spec,IO.plain

def producer_identity(item):
    value={key:item[key] for key in
           ("result","run_id","source_commit","core_sha256","manifest_sha256","certificate_name")}
    value["certificate_sha256"]=item["files"][item["certificate_name"]]
    return value

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def run(args):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
    request=read(args.request)
    assert request["session"]=="serre-public-astra-20261115"
    assert request["result"]==RESULT
    assert request["io_helper_sha256"]==IO_SHA
    assert request["script_sha256"]==sha(__file__)
    for label,path in (("root",REPO/"README.md"),("topic",TOPIC/"README.md")):
        assert sha(path)==request["current_readme_sha256"][label]
    source=request["source"]
    assert source["result"]==ORIGINAL and source["core_sha256"]==CORE_SHA
    assert source["run_id"]=="43719622321"
    assert source["source_commit"]=="2a3300a9edec73c23e72f23127a0ae7d8222d13e"
    assert source["expected_conclusion"] in ("success","failure","cancelled","timed_out")
    # The archive constructor requires a completed run and its real published artifact.
    archive=IO.Archive(source,args.output.parent/"R815-range-transfer",whole=False)
    args.output.mkdir(parents=True,exist_ok=True)
    selected=args.output/"selected-original-R815"
    selected.mkdir(parents=True,exist_ok=True)
    reviewed={}

    def unbound_reference():
        members=archive.by_name.get(REFERENCE,[])
        assert len(members)==1 and 0<members[0].file_size<1024*1024
        raw=archive.zip.read(members[0])
        assert len(raw)==members[0].file_size
        path=selected/REFERENCE
        path.write_bytes(raw)
        return read(path)

    try:
        reference=unbound_reference()
        assert reference["result"]==ORIGINAL
        assert reference["manifest_file"]=="full-outputs-manifest.json"
        assert 0<reference["manifest_bytes"]<=SMALL_LIMIT
        manifest_path=archive.extract_bound("full-outputs-manifest.json",reference["manifest_sha256"],
            selected/"full-outputs-manifest.json",reference["manifest_bytes"])
        manifest=read(manifest_path)
        assert manifest["result"]==ORIGINAL
        files={row["file"]:plain(row) for row in manifest["files"]}
        assert len(files)==len(manifest["files"])==reference["file_count"]
        assert set(archive.by_name)==set(files)|{"full-outputs-manifest.json",REFERENCE}
        for name,row in files.items():
            IO.check_spec(row)
            members=archive.by_name[name]
            assert len(members)==1 and members[0].file_size==row["bytes"]
        if source.get("manifest_sha256") is not None:
            assert sha(manifest_path)==source["manifest_sha256"]

        def take(name):
            row=files[name]
            assert row["bytes"]<=SMALL_LIMIT,("Not a selected small metadata member",name,row["bytes"])
            path=archive.extract_bound(name,row["sha256"],selected/name,row["bytes"])
            reviewed[name]=spec(path)
            return path

        def value(name):
            return read(take(name))

        initial,run_receipt=(value(name) for name in
            ("public-actions-input.json","run-receipt.json"))
        core=value("core-receipt.json") if "core-receipt.json" in files else None
        assert initial["result"]==run_receipt["result"]==ORIGINAL
        if core is not None:
            assert core["result"]==ORIGINAL
        assert initial["source_commit"]==run_receipt["source_commit"]==source["source_commit"]
        assert str(run_receipt["workflow_run_id"])==str(source["run_id"])
        assert initial["source_repository"]=="Rogerhu12/math-research-public"
        assert initial["core_sha256"]==initial["job"]["core_sha256"]==CORE_SHA
        if core is not None:
            assert core["source_sha256"]==CORE_SHA
        assert initial["driver_sha256"]==initial["job"]["wrapper_sha256"]==WRAPPER_SHA
        assert initial["framework_sha256"]==initial["job"]["framework_sha256"]==FRAMEWORK_SHA
        assert initial["request_sha256"]==request["original_request_sha256"]
        assert fingerprint(initial["job"])==request["original_job_sha256"]
        if core is not None:
            assert run_receipt["core_receipt_sha256"]==files["core-receipt.json"]["sha256"]
        else:
            assert run_receipt["core_receipt_sha256"] is None
        for label,key in (("root","root_readme_sha256"),("topic","topic_readme_sha256")):
            assert initial[key]==request["original_readme_sha256"][label]
        job=initial["job"]
        assert job["requested_targets"]==["g","Gamma"]
        assert job["requested_stage"]=="original_normal_derivation_operators"
        assert job["producer_inputs_pending"] is False
        assert job["auxiliary_prime_start"]==1000000007
        assert job["matrix_row_block_size"]==16 and job["reconstruct_every_primes"]==8
        assert set(job["retained_artifacts"])=={"R806","R813"}
        initial_spec=files["public-actions-input.json"]

        def check_tag(tag):
            assert tag["result"]==ORIGINAL and tag["source_sha256"]==CORE_SHA
            assert tag["python_flint"]=="0.9.0" and tag["p"]==41
            for key in ("R813_proof_sha256","R817_proof_sha256","R815_method_sha256","framework_sha256",
                        "auxiliary_prime_start","matrix_row_block_size","reconstruct_every_primes","exact_identity_mode"):
                assert tag[key]==job[key]
            assert tag["normal_affine_basis_rank"]==272 and tag["normal_basis_degrees"]==EPS
            assert tag["R806_producer"]==producer_identity(job["retained_artifacts"]["R806"])
            assert tag["R806_polynomial_multiplier"]["sha256"]==job["retained_artifacts"]["R806"]["files"][
                "R806-exact-polynomial-multiplier-in-original-normal-basis.json.gz"]
            assert tag["R806_cyclic_witness"]["sha256"]==job["retained_artifacts"]["R806"]["files"][
                "R806-candidate-0000000000-prime-1000000007-z-0-cyclic.json.gz"]

        configuration=None
        def stage(name,target=None):
            nonlocal configuration
            data=value(name)
            assert data["complete"] is True
            check_tag(data["configuration"])
            if configuration is None:configuration=data["configuration"]
            assert data["configuration"]==configuration
            if target is not None:
                assert data["target"]==target
                target_tag=data["target_configuration"]
                assert data["target_configuration_sha256"]==fingerprint(target_tag)
                assert target_tag["basis_configuration_sha256"]==fingerprint(configuration)
                assert target_tag["R813_producer"]==producer_identity(job["retained_artifacts"]["R813"])
                assert target_tag["source_R813_exact_coordinates"]["sha256"]==job["retained_artifacts"]["R813"]["files"][
                    "R813-two-exact-S3-Wronskian-coordinates.json.gz"]
                assert target_tag["source_R813_normal_interface"]["sha256"]==job["retained_artifacts"]["R813"]["files"][
                    "R813-original-g-h-normal-vector-interface.json.gz"]
                assert target_tag["target"]==target
            return data

        input_summary=None
        if "retained-inputs-receipt.json" in files:
            retained=value("retained-inputs-receipt.json")
            assert retained["result"]==ORIGINAL
            assert retained["producer_identities"]=={
                label:producer_identity(job["retained_artifacts"][label]) for label in ("R806","R813")}
            assert retained["input_bundle"]==files[BUNDLE]
            assert retained["all_selected_bundle_members_individually_size_and_sha256_verified"] is True
            selected_files=retained["selected_files"]
            assert set(selected_files)=={"R806","R813"}
            for entries in selected_files.values():
                assert len({entry["file"] for entry in entries})==len(entries)
                for entry in entries:IO.check_spec(entry)
            assert retained["actual_selected_file_count"]==sum(map(len,selected_files.values()))
            source_groups=[row for row in selected_files["R806"] if re.fullmatch(
                r"R806-candidate-0000000000-group-[0-9]{3}-exact-coordinates[.]json[.]gz",row["file"])]
            assert len(source_groups)==34
            r813_names={row["file"] for row in selected_files["R813"]}
            assert {"R813-two-exact-S3-Wronskian-coordinates.json.gz",
                    "R813-original-g-h-normal-vector-interface.json.gz"}<=r813_names
            input_summary={
                "retained_receipt":files["retained-inputs-receipt.json"],
                "input_bundle":files[BUNDLE],"actual_selected_file_count":retained["actual_selected_file_count"],
                "actual_group_counts":{label:len(rows) for label,rows in selected_files.items()},
                "original_R806_exact_group_count":len(source_groups),
                "original_R813_two_normal_inputs_present":True,
                "original_frozen_prepare_recorded_full_member_SHA_verification":True,
                "bundle_or_its_inner_raw_members_redownloaded_in_this_small_review":False,
                "actual_source_identities":retained["producer_identities"]}

        completion=(core is not None and run_receipt["complete"] is True
                    and core["complete"] is True and run_receipt["process_exit_code"]==0)
        certificate=None
        stage_inventory_spec=None
        stage_count=None
        if FINAL in files:
            certificate=value(FINAL)
            if core is not None:
                assert core.get("certificate_sha256")==files[FINAL]["sha256"]
            assert certificate["result"]==ORIGINAL and certificate["complete"] is True
            check_tag(certificate["configuration"])
            configuration=certificate["configuration"]
            stage_inventory_spec=plain(certificate["stage_manifest"])
            assert stage_inventory_spec==files[stage_inventory_spec["file"]]
            inventory=stage(stage_inventory_spec["file"])
            entries={entry["file"]:plain(entry) for entry in inventory["files"]}
            assert len(entries)==len(inventory["files"])
            for name,row in entries.items():assert row==files[name]
            stage_count=len(entries)
            assert certificate["requested_targets"]==["g","Gamma"]
            assert certificate["independent_Mh_reconstructed_or_stored"] is False
            assert certificate["Mg_exact_commutator_points"]==list(range(7))
            assert certificate["Gamma_exact_nested_commutator_points"]==list(range(7))
            assert certificate["original_Mg_computed"] is True
            assert certificate["original_normal_derivation_connection_computed"] is True
            assert certificate["all_complete_polynomial_defining_identities_verified"] is True
        if completion:assert certificate is not None

        operators={}
        for target,suffix in (("g","certified-multiplier-index"),("Gamma","certified-connection-index")):
            name="R815-target-"+target+"-component-00-"+suffix+".json.gz"
            if name not in files:continue
            data=stage(name,target)
            assert data["field_component"]==0
            assert data["regular_degree_bound"]==(3 if target=="g" else 2)
            assert len(data["matrix_row_blocks_tau"])==len(data["matrix_row_blocks_sigma"])==17
            for chart in ("tau","sigma"):
                for row in data["matrix_row_blocks_"+chart]:
                    assert plain(row)==files[row["file"]]
            if target=="g":
                assert data["original_first_column_verified_coefficientwise"] is True
                assert data["complete_polynomial_commutator_identity_verified"] is True
            else:
                assert data["Gamma_zero_first_column_and_H_original_first_column_verified"] is True
                assert data["complete_nested_commutator_identity_verified"] is True
            if certificate is not None:
                assert certificate["operator_indices"][target]==files[name]
                assert certificate["actual_CRT_prime_counts"][target]==data["actual_CRT_prime_count"]
            operators[target]={
                "index":files[name],"actual_CRT_prime_count":data["actual_CRT_prime_count"],
                "regular_degree_bound":data["regular_degree_bound"],
                "matrix_row_blocks_tau":data["matrix_row_blocks_tau"],
                "matrix_row_blocks_sigma":data["matrix_row_blocks_sigma"],
                "only_index_read_not_large_matrix_rows":True}

        currents={}
        histories={}
        for target in TARGETS:
            stem="R815-target-"+target+"-component-00"
            current_name=stem+"-CRT-current.json.gz"
            current_spec=files.get(current_name)
            names=[name for name in files if re.fullmatch(re.escape(stem)+r"-CRT-step-[0-9]{6}-receipt[.]json[.]gz",name)]
            if names:
                newest=sorted(names)[-1]
                record=stage(newest,target)
                number=int(newest.split("-CRT-step-")[1].split("-")[0])
                assert record["prime_count"]==number
                assert record["large_vector_or_matrix_embedded"] is False
                assert record["full_temporary_images_discarded_only_after_CRT_commit"] is True
                if record["previous_CRT_receipt"] is not None:
                    prior=plain(record["previous_CRT_receipt"])
                    assert prior==files[prior["file"]]
                histories[target]={"receipt":files[newest],"prime_count":record["prime_count"],
                    "latest_prime":record["latest_prime"],"modulus_bits":record["modulus_bits"],
                    "current_full_CRT_checkpoint":record["current_full_CRT_checkpoint"],
                    "previous_checkpoint_sha256":record["previous_checkpoint_sha256"],
                    "previous_CRT_receipt":record["previous_CRT_receipt"],
                    "latest_receipt_matches_published_current":current_spec==record["current_full_CRT_checkpoint"]}
            if current_spec is not None:
                currents[target]={"checkpoint":current_spec,"large_current_not_read_in_selected_review":True,
                    "prime_count_confirmed_by_matching_small_receipt":
                        histories.get(target,{}).get("prime_count")
                        if histories.get(target,{}).get("latest_receipt_matches_published_current") else None,
                    "completed_mathematical_operator_claimed_from_current":False}
        if completion:assert not currents and set(operators)==set(TARGETS)

        def compact_log_line(line):
            line=re.sub(r"(?<![A-Za-z0-9_])[0-9]{32,}(?![A-Za-z0-9_])",
                        lambda match:"<"+str(len(match.group(0)))+"-digit integer omitted>",str(line))
            return line if len(line)<=1000 else line[:1000]+" <remaining log text omitted>"

        log_tail=[]
        progress=[]
        log_name="public-actions-run.log"
        if log_name in files:
            path=take(log_name)
            lines=path.read_text(encoding="utf-8",errors="replace").splitlines()
            log_tail=[compact_log_line(line) for line in lines[-20:]]
            if sum(map(len,log_tail))>8000:
                log_tail=["\n".join(log_tail)[-8000:]]
            for line in lines:
                try:entry=json.loads(line)
                except (ValueError,TypeError):continue
                if isinstance(entry,dict) and entry.get("stage") in ("CRT_regular_multiplier","CRT_normal_connection"):
                    progress.append({key:entry[key] for key in
                        ("stage","target","field_component","prime_count","prime","modulus_bits","coefficient_count","seconds")
                        if key in entry})
        if completion:
            endpoint="complete_original_two_operator_certificate"
        elif core is not None and "BudgetStop" in str(core.get("error","")):
            endpoint="natural_budget_checkpoint_no_math_failure_inferred"
        elif run_receipt["process_exit_code"]==124:
            endpoint="outer_timeout_checkpoint_no_math_failure_inferred"
        else:
            endpoint="ended_failure_requires_actual_error_review"
        summary={
            "result":RESULT,"complete":True,"original_run_finished_before_any_source_read":True,
            "original_source":source,"original_public_input":initial_spec,
            "original_full_manifest":spec(manifest_path),"original_reference":spec(selected/REFERENCE),
            "original_manifest_member_count":len(files),
            "original_manifest_member_lengths_checked_against_ZIP_directory":True,
            "all_large_output_members_rehashed_by_this_small_review":False,
            "source_core_sha256":CORE_SHA,"source_wrapper_sha256":WRAPPER_SHA,
            "actual_endpoint":endpoint,"original_process_exit_code":run_receipt["process_exit_code"],
            "original_run_complete":run_receipt["complete"],
            "original_core_receipt":files.get("core-receipt.json"),
            "original_core_receipt_present":core is not None,
            "original_core_complete":None if core is None else core["complete"],
            "original_core_error":None if core is None or core.get("error") is None else compact_log_line(core["error"]),
            "original_mathematical_completion_claimed":completion,
            "missing_core_receipt_does_not_imply_completion_or_mathematical_failure":core is None,
            "original_runner_error":None if run_receipt.get("error") is None else compact_log_line(run_receipt["error"]),
            "original_certificate":files.get(FINAL),"original_stage_manifest":stage_inventory_spec,
            "original_complete_stage_count":stage_count,
            "actual_complete_operator_indexes":operators,"actual_latest_CRT_history":histories,
            "actual_current_checkpoint_specs":currents,
            "input_carrier_coverage":input_summary,
            "last_original_CRT_progress_records":progress[-4:],"original_core_log_tail":log_tail,
            "actual_core_seconds_if_complete":None if certificate is None else certificate["seconds"],
            "selected_original_files":[reviewed[name] for name in sorted(reviewed)],
            "selected_original_member_count":len(reviewed),
            "selected_original_bytes":sum(row["bytes"] for row in reviewed.values()),
            "archive_subset_transfer":archive.receipt(),
            "new_mathematical_arithmetic_executed":False,
            "source_inputs_or_old_matrices_recomputed":False,
            "raw_current_or_matrix_data_printed":False,
            "read_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
        save(args.output/"R815-ended-selected-IO-summary.json",summary)
        print("R815_ENDED_SOURCE_IO_REVIEW="+json.dumps(summary,sort_keys=True),flush=True)
        return 0
    finally:
        archive.close()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    return run(args)

if __name__=="__main__":
    raise SystemExit(main())
