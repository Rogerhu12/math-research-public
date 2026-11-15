#!/usr/bin/env python3
"""R820 public IO carrier and certificate runner; no mathematical core is imported."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import signal
import subprocess
import sys
import tarfile

import R815_public_original_normal_derivation_operators as io
from R815_public_original_normal_derivation_operators import (
    Archive, Producer, sha, read, save, file_spec, plain, check_spec, identity, same_identity, fingerprint
)

S=Path(__file__).resolve().parent
REPO=S.parents[2]
TOPIC=REPO/"topics/serre-uniformity"
REQUEST=TOPIC/"notes/R820-public-original-cusp-finite-algebra-ideals-request.json"
RESULT="R820-original-cusp-finite-algebra-and-ideals"
FINAL="p41-original-cusp-finite-algebra-ideals-certificate.json"
BUNDLE="R820-retained-producer-inputs.tar.gz"
REFERENCE="full-outputs-manifest-reference.json"
LABELS=("R805","R806")
EPS=[0]+[1]*144+[2]*127
IO_SHA="ab725da038ec458493f461088ceee0fd105e0dc90cbfb4ad6f3047cbec90b454"
FRAMEWORK_SHA="849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3"


def guard():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise SystemExit("Public repository Actions execution required.")


def local(relative):
    path=(TOPIC/relative).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def row_index(a):
    return 0 if a==0 else 4+3*(a-1) if a<=144 else 436+2*(a-145)


def select(producers):
    r5,r6=producers["R805"],producers["R806"]
    c5,c6=r5.certificate,r6.certificate
    assert r5.item["core_sha256"]=="730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420"
    assert r6.item["core_sha256"]=="b014f9b3cb4923421e6a879eddb4da58dd0baefb28d61a2191f6b0a33e51810d"
    same_identity(r6.tag["retained_artifacts"]["R805"],r5.item)
    assert c5["affine_free_module_rank"]==272 and c5["graded_free_basis_degrees"]==[1,144,127]
    assert c5["actual_pencil_n"]==1 and c5["actual_pencil_rank"]==690
    assert c5["degree3_S_basis_dimension"]==690 and c5["degree3_S_prefix_count"]==41
    assert c5["all_S_rows_original_and_real_coordinates_verified"] is True
    assert c5["original_82_scales_preserved"] is True
    for key in ("exact_polynomial_multiplication_computed","all272_columns_verified_in_all820_original_rows",
                "actual_cyclic_minor_certified","original_function_field_primitive_generator_certified",
                "normal_integral_basis_preserved"):
        assert c6[key] is True
    assert c6["actual_cyclic_minor"]["rank"]==272 and c6["actual_cyclic_minor"]["determinant_mod_prime"]!=0
    free=r5.indexed(c5["graded_free_basis_stage"])
    assert free["affine_free_module_rank"]==272 and free["degree_distribution"]==[1,144,127]
    assert free["degree1_original_indices"]==list(range(2,146))
    assert len(free["degree2_original_indices"])==127 and free["characteristic_zero_complement_certified"] is True
    r5.indexed(c5["pencil_stage"])
    index=r5.indexed(c5["S_basis_index"])
    assert index["dimension"]==690 and index["integer_scale"]==str(82**6)
    assert index["graded_free_basis_stage"]==c5["graded_free_basis_stage"]
    assert index["qY_count"]==41 and index["all_original_and_real_coordinates_verified"] is True
    assert index["all_new_S_rows_have_original_generation_witnesses"] is True
    assert len(index["basis_rows"])==690
    w=r6.indexed(c6["polynomial_multiplier"])
    assert w["original_R805_free_basis"]==c5["graded_free_basis_stage"]
    assert w["original_R805_S_basis_index"]==c5["S_basis_index"]
    assert w["coefficient_field"]=="Q, certified by exact original rational coordinate equations"
    assert w["normal_affine_basis_rank"]==272 and w["normal_affine_basis_degrees"]==EPS
    assert w["original_function_field_primitive_generator_certified"] is True
    assert w["all272_columns_verified_in_all820_original_rows"] is True
    selected={}
    for i in sorted({row_index(a) for a in range(272)}|{1}):
        entry=index["basis_rows"][i]
        assert entry["index"]==i
        data=r5.indexed(entry)
        assert data["index"]==i and data["weight"]==6 and data["integer_scale"]==str(82**6)
        assert data["qY_count"]==41 and data["free_basis_stage"]==c5["graded_free_basis_stage"]
        assert data["recipe"]==entry["recipe"]
        assert data["all_original_and_real_coordinates_verified"] is True
        assert data["V3_membership_has_original_product_generation_witness"] is True
        assert len(data["integer_v_t_coefficients"][0])==20
        selected[i]=plain(entry)
    assert len(selected)==273
    for a in range(272):
        recipe=index["basis_rows"][row_index(a)]["recipe"]
        if a==0:
            expected={"kind":"degree0_free_generator","tau_power":3,"sigma_power":0}
        elif a<=144:
            expected={"kind":"degree1_free_generator","original_M2_index":a+1,"tau_power":2,"sigma_power":0}
        else:
            expected={"kind":"degree2_free_generator","original_V2_index":free["degree2_original_indices"][a-145],
                      "tau_power":1,"sigma_power":0}
        assert recipe==expected
    assert index["basis_rows"][1]["recipe"]=={"kind":"degree0_free_generator","tau_power":2,"sigma_power":1}
    return {"original_R805_free_basis":c5["graded_free_basis_stage"],"original_R805_S3_index":c5["S_basis_index"],
            "original_R805_pencil":c5["pencil_stage"],"original_R806_Q_primitive_multiplier":c6["polynomial_multiplier"],
            "selected_original_S3_files":[selected[i] for i in sorted(selected)],
            "old_Fourier_or_primitive_coordinates_recomputed":False}


def expected_tag(item,producers):
    c5,c6=producers["R805"].certificate,producers["R806"].certificate
    return {
        "result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "R820_proof_sha256":item["R820_proof_sha256"],"R820_method_sha256":item["R820_method_sha256"],
        "framework_sha256":item["framework_sha256"],
        "producer_identities":{label:identity(producers[label].item) for label in LABELS},
        "original_R805_free_basis":c5["graded_free_basis_stage"],"original_R805_S3_index":c5["S_basis_index"],
        "original_R805_pencil":c5["pencil_stage"],"original_R806_Q_primitive_multiplier":c6["polynomial_multiplier"],
        "normal_basis_degrees":EPS,"normal_basis_rank":272,"actual_pencil_n":1,
        "finite_field_degree":20,"fixed_charts":["tau","sigma"],
        "normal_basis_processing_order":"271,270,...,0",
        "kernel_algorithm":"first dependence in each reverse-ordered original Z-Krylov chain",
        "old_Fourier_or_primitive_arithmetic_recomputed":False,
        "transport_carrier_and_budget_excluded_from_mathematical_identity":True}


def scan_bundle(bundle,allowed,root=None):
    actual={}
    with tarfile.open(bundle,"r:gz") as stream:
        for member in stream:
            name=PurePosixPath(member.name)
            assert member.isfile() and len(name.parts)==2 and name.parts[0] in allowed
            assert not name.is_absolute() and ".." not in name.parts and member.name not in actual
            target=None if root is None else Path(root)/name.parts[0]/name.parts[1]
            if target is not None:
                target.parent.mkdir(parents=True,exist_ok=True)
                temporary=target.with_name(target.name+".transfer")
            digest,total=hashlib.sha256(),0
            source=stream.extractfile(member)
            destination=open(temporary,"wb") if target is not None else None
            try:
                for block in iter(lambda:source.read(1024*1024),b""):
                    digest.update(block);total+=len(block)
                    if destination is not None:
                        destination.write(block)
            finally:
                source.close()
                if destination is not None:
                    destination.close()
            assert total==member.size
            if target is not None:
                temporary.replace(target)
            actual[member.name]={"file":name.parts[1],"bytes":total,"sha256":digest.hexdigest()}
    return actual


class TarLabel:
    def __init__(self,stream,label,actual):
        self.stream,self.label,self.actual=stream,label,actual

    def extract_bound(self,name,digest,target,expected_bytes=None):
        key=self.label+"/"+name
        entry=self.actual[key]
        assert entry["sha256"]==digest
        if expected_bytes is not None:
            assert entry["bytes"]==expected_bytes
        target=Path(target)
        if not target.exists():
            target.parent.mkdir(parents=True,exist_ok=True)
            temporary=target.with_name(target.name+".transfer")
            with self.stream.extractfile(key) as source,temporary.open("wb") as destination:
                shutil.copyfileobj(source,destination,1024*1024)
            assert temporary.stat().st_size==entry["bytes"] and sha(temporary)==digest
            temporary.replace(target)
        assert target.stat().st_size==entry["bytes"] and sha(target)==digest
        return target


def restore_carrier(item,out):
    carrier=item["input_carrier"]
    archive=Archive(carrier,out.parent/"download-carrier")
    source=Producer("R813",carrier,out.parent/"carrier-metadata",archive)
    assert source.item["result"]=="R813-original-Wronskian-derivation-inputs"
    assert source.certificate["completed_scope"]=="two_original_S3_Wronskian_inputs"
    archive.verify_all_manifest_members(read(source.directory/"full-outputs-manifest.json"))
    for label in LABELS:
        same_identity(source.initial["job"]["retained_artifacts"][label],item["retained_artifacts"][label])
    receipt=source.raw("retained-inputs-receipt.json")
    bundle_spec=carrier["input_bundle"]
    assert receipt["input_bundle"]==bundle_spec
    bundle=archive.extract_bound(bundle_spec["file"],bundle_spec["sha256"],
                                 out.parent/"carrier-inputs.tar.gz",bundle_spec["bytes"])
    originals=source.initial["job"]["retained_artifacts"]
    actual=scan_bundle(bundle,set(originals))
    with tarfile.open(bundle,"r:gz") as stream:
        for label,original in originals.items():
            key=label+"/full-outputs-manifest.json"
            assert actual[key]["sha256"]==original["manifest_sha256"]
            with stream.extractfile(key) as f:
                manifest=json.load(f)
            assert manifest["result"]==original["result"]
            files={row["file"]:plain(row) for row in manifest["files"]}
            for path,entry in actual.items():
                if path.startswith(label+"/") and entry["file"]!="full-outputs-manifest.json":
                    assert entry==files[entry["file"]]
        counts={label:sum(path.startswith(label+"/") for path in actual) for label in originals}
        for group in receipt["groups"]:
            label=group["label"]
            same_identity(group["producer_identity"],originals[label])
            assert counts[label]==group["file_count"]
            assert group["original_manifest_and_selected_file_hashes_verified"] is True
        producers={label:Producer(label,item["retained_artifacts"][label],
                    out.parent/"retained"/label,TarLabel(stream,label,actual)) for label in LABELS}
        selection=select(producers)
    archive.zip.close()
    archive.path.unlink()
    return producers,selection,{"actual_carrier_archive":archive.receipt,
        "original_source_input_bundle":bundle_spec,"all_original_bundle_members_verified":len(actual),
        "all_original_producer_labels_preserved":True}


def prepare(item,out):
    root=out.parent/"retained"
    present=[(root/label/"full-outputs-manifest.json").exists() for label in LABELS]
    assert all(present) or not any(present)
    if all(present):
        producers={label:Producer(label,item["retained_artifacts"][label],root/label) for label in LABELS}
        selection=select(producers)
        carrier={"same_core_selected_input_bundle_reused":True}
    else:
        producers,selection,carrier=restore_carrier(item,out)
    for label,p in producers.items():
        assert {x.name for x in p.directory.iterdir() if x.is_file()}==set(p.selected)
    bundle=out/BUNDLE
    if not bundle.exists():
        temp=bundle.with_name(bundle.name+".tmp")
        with tarfile.open(temp,"w:gz") as stream:
            for label,p in producers.items():
                for name,path in sorted(p.selected.items()):
                    stream.add(path,arcname=label+"/"+name,recursive=False)
        temp.replace(bundle)
    expected={label+"/"+name:file_spec(path) for label,p in producers.items() for name,path in p.selected.items()}
    actual=scan_bundle(bundle,set(LABELS))
    assert actual==expected
    save(out/"retained-inputs-receipt.json",{
        "result":RESULT,"producer_identities":{label:identity(p.item) for label,p in producers.items()},
        "selection":selection,"input_bundle":file_spec(bundle),
        "selected_files":{label:[file_spec(p) for _,p in sorted(producer.selected.items())]
                          for label,producer in producers.items()},
        "actual_selected_file_count":len(actual),"all_selected_member_hashes_verified":True,
        "carrier":carrier,"new_mathematics_executed":False})
    return producers,selection,root


def restore_resume(item,out):
    previous=item.get("resume")
    if previous is None:
        return
    archive=Archive(previous,out.parent/"download-resume",expected_conclusion="failure")
    path=archive.extract_bound("full-outputs-manifest.json",previous["manifest_sha256"],
                               out.parent/"previous-manifest.json")
    manifest=read(path)
    assert manifest["result"]==RESULT
    files=archive.verify_all_manifest_members(manifest)
    def take(name,destination):
        row=files[name]
        return archive.extract_bound(name,row["sha256"],destination,row["bytes"])
    initial=read(take("public-actions-input.json",out.parent/"previous-input.json"))
    run=read(take("run-receipt.json",out.parent/"previous-run.json"))
    assert initial["result"]==run["result"]==RESULT
    assert initial["source_commit"]==run["source_commit"]==previous["source_commit"]
    assert str(run["workflow_run_id"])==str(previous["run_id"])
    old=initial["job"]
    for key in ("result","p","core","core_sha256","proof","R820_proof_sha256","method","R820_method_sha256",
                "requested_stage","framework","framework_sha256","io_helper","io_helper_sha256"):
        assert old[key]==item[key]
    for label in LABELS:
        same_identity(old["retained_artifacts"][label],item["retained_artifacts"][label])
    bundle=take(BUNDLE,out/BUNDLE)
    transferred=scan_bundle(bundle,set(LABELS),out.parent/"retained")
    producers={label:Producer(label,item["retained_artifacts"][label],out.parent/"retained"/label) for label in LABELS}
    select(producers)
    expected={label+"/"+name:file_spec(path) for label,p in producers.items() for name,path in p.selected.items()}
    assert transferred==expected
    tag=expected_tag(item,producers)
    copied=0
    for name,entry in files.items():
        if name!=FINAL and not (name.startswith("R820-") and name.endswith(".json.gz")):
            continue
        value=read(take(name,out/name))
        assert value["configuration"]==tag
        assert value["complete"] is (not name.endswith("-current.json.gz"))
        copied+=1
    save(out/"resume-receipt.json",{"result":RESULT,"previous_actual_artifact":previous,
        "all_previous_manifest_files_verified":len(files),"restored_stage_files":copied,
        "all_selected_bundle_files_verified":len(transferred),
        "same_original_mathematical_sources_and_core":True,"old_completed_arithmetic_recomputed":False})
    archive.zip.close()
    archive.path.unlink()


def output_manifest(out):
    for path in out.iterdir():
        if path.is_file() and path.name.endswith((".tmp",".transfer",".partial")):
            path.unlink()
    artifact="serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    rows=[dict(file_spec(path),artifact=artifact,included_in_git=False)
          for path in sorted(out.iterdir()) if path.is_file() and path.name not in ("full-outputs-manifest.json",REFERENCE)]
    path=out/"full-outputs-manifest.json"
    save(path,{"result":RESULT,"files":rows,"temporary_active_checkpoint_artifact":artifact,
        "temporary_active_checkpoint_retention_days":1,
        "reproducible_rows_certificates_or_input_bundles_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,"manifest_file":path.name,"manifest_sha256":sha(path),
        "manifest_bytes":path.stat().st_size,"file_count":len(rows),"full_outputs_artifact":artifact,
        "automatic_git_or_release_publication":False})


def compute(item,out):
    out.mkdir(parents=True,exist_ok=True)
    core,proof,method=S/item["core"],local(item["proof"]),local(item["method"])
    source=subprocess.check_output(["git","rev-parse","HEAD"],cwd=REPO,text=True).strip()
    save(out/"public-actions-input.json",{"result":RESULT,"p":41,
        "source_repository":"Rogerhu12/math-research-public","source_commit":source,"job":item,
        "core_sha256":sha(core),"driver_sha256":sha(__file__),"proof_sha256":sha(proof),
        "method_sha256":sha(method),"framework_sha256":sha(S/item["framework"]),
        "io_helper_sha256":sha(io.__file__),"request_sha256":sha(REQUEST),
        "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
        "workflow_sha256":sha(REPO/item["workflow"]),
        "prepared_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
        "new_arithmetic":"original two-chart cusp finite-algebra kernels only",
        "old_Fourier_or_primitive_results_recomputed":False})
    code,error=1,None
    try:
        assert item["result"]==RESULT and item["p"]==41 and item["producer_inputs_pending"] is False
        assert item["requested_stage"]=="two_original_cusp_finite_algebra_kernels"
        assert set(item["retained_artifacts"])==set(LABELS)
        assert sha(core)==item["core_sha256"] and sha(__file__)==item["wrapper_sha256"]
        assert sha(proof)==item["R820_proof_sha256"] and sha(method)==item["R820_method_sha256"]
        assert sha(io.__file__)==item["io_helper_sha256"]==IO_SHA
        assert sha(S/item["framework"])==item["framework_sha256"]==FRAMEWORK_SHA
        restore_resume(item,out)
        _,_,retained=prepare(item,out)
        config=out.parent/"job-config.json"
        save(config,item)
        command=[sys.executable,"-u",str(core),"--config",str(config),"--proof",str(proof),"--method",str(method),
                 "--retained",str(retained),"--output",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process=subprocess.Popen(command,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                code=process.wait(timeout=item["budget_minutes"]*60+120)
            except subprocess.TimeoutExpired:
                error="Budget reached; complete source-bound finite-algebra steps and short current states retained."
                os.killpg(process.pid,signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid,signal.SIGKILL)
                    process.wait()
                code=124
    except Exception as exception:
        error=type(exception).__name__+": "+str(exception)
    receipt=out/"core-receipt.json"
    core_receipt=read(receipt) if receipt.exists() else {"complete":False}
    complete=code==0 and core_receipt.get("complete") is True
    save(out/"run-receipt.json",{"result":RESULT,"p":41,"complete":complete,"process_exit_code":code,"error":error,
        "source_commit":source,"workflow_run_id":os.environ["GITHUB_RUN_ID"],
        "workflow_attempt":os.environ["GITHUB_RUN_ATTEMPT"],"execution_environment":"public-repository-github-actions",
        "core_receipt_sha256":sha(receipt) if receipt.exists() else None,
        "original_two_chart_cusp_ideals_computed":complete,
        "general_polar_ideal_eta_or_height_computed":False,
        "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result":RESULT,"complete":complete,"exit_code":code,"error":error}),flush=True)
    return code if code else (0 if complete else 1)


def verify(item,out):
    initial,run,core=(read(out/name) for name in ("public-actions-input.json","run-receipt.json","core-receipt.json"))
    assert initial["job"]==item and initial["result"]==run["result"]==core["result"]==RESULT
    assert initial["core_sha256"]==core["source_sha256"]==item["core_sha256"]
    assert initial["driver_sha256"]==item["wrapper_sha256"]
    assert initial["proof_sha256"]==item["R820_proof_sha256"] and initial["method_sha256"]==item["R820_method_sha256"]
    assert initial["framework_sha256"]==item["framework_sha256"]
    assert initial["io_helper_sha256"]==item["io_helper_sha256"]
    assert run["source_commit"]==initial["source_commit"]
    assert run["complete"] is True and run["process_exit_code"]==0
    assert run["core_receipt_sha256"]==sha(out/"core-receipt.json")
    assert core["complete"] is True and core["certificate_sha256"]==sha(out/FINAL)
    root=out.parent/"retained"
    if not all((root/label/"full-outputs-manifest.json").exists() for label in LABELS):
        scan_bundle(out/BUNDLE,set(LABELS),root)
    producers={label:Producer(label,item["retained_artifacts"][label],root/label) for label in LABELS}
    selection=select(producers)
    expected={label+"/"+name:file_spec(path) for label,p in producers.items() for name,path in p.selected.items()}
    assert scan_bundle(out/BUNDLE,set(LABELS))==expected
    receipt=read(out/"retained-inputs-receipt.json")
    assert receipt["selection"]==selection and receipt["actual_selected_file_count"]==len(expected)
    assert receipt["input_bundle"]==file_spec(out/BUNDLE)
    tag=expected_tag(item,producers)
    certificate=read(out/FINAL)
    assert certificate["result"]==RESULT and certificate["complete"] is True and certificate["configuration"]==tag
    assert certificate["completed_scope"]=="two_original_cusp_finite_algebra_kernels"
    assert certificate["normal_basis_rank"]==272 and certificate["normal_basis_degrees"]==EPS
    assert certificate["finite_field_degree"]==20 and certificate["selected_original_S3_row_count"]==273
    assert certificate["actual_cusp_colengths"]=={"tau":20,"sigma":20}
    assert certificate["actual_input_producers"]=={label:identity(p.item) for label,p in producers.items()}
    for key in ("original_two_chart_cusp_ideals_computed","complete_polynomial_kernels_certified",
                "same_original_cusp_field_and_two_chart_transitions_verified"):
        assert certificate[key] is True
    for key in ("old_Fourier_or_primitive_results_recomputed","original_Gamma_or_general_polar_ideal_computed",
                "actual_eta_principal_function_or_height_computed"):
        assert certificate[key] is False
    inventory_spec=certificate["stage_manifest"]
    assert file_spec(out/inventory_spec["file"])==inventory_spec
    inventory=read(out/inventory_spec["file"])
    assert inventory["complete"] is True and inventory["configuration"]==tag
    entries={entry["file"]:entry for entry in inventory["files"]}
    assert len(entries)==len(inventory["files"])
    for name,entry in entries.items():
        check_spec(entry)
        assert file_spec(out/name)==entry
        data=read(out/name)
        assert data["complete"] is True and data["configuration"]==tag
    names={p.name for p in out.glob("R820-*.json.gz") if not p.name.startswith("R820-stage-manifest-")}
    assert set(entries)==names and not list(out.glob("R820-*-current.json.gz"))

    def ref(entry):
        assert entries[entry["file"]]==plain(entry)
        return read(out/entry["file"])

    def rational(pair,nonzero=False):
        assert len(pair)==2 and int(pair[1])>0
        if nonzero:
            assert int(pair[0])!=0

    source=ref(certificate["original_source_constants"])
    assert source["selected_original_S3_files"]==selection["selected_original_S3_files"]
    assert len(source["normal_basis_rows"])==272 and source["integer_scale"]==str(82**6)
    field_spec=certificate["original_finite_algebra_interface"]
    field=ref(field_spec)
    assert field["source_original_constants"]==certificate["original_source_constants"]
    assert field["finite_field_degree"]==20 and len(field["field_modulus_low_to_high"])==21
    assert field["field_modulus_low_to_high"][-1]==["1","1"]
    for key in ("both_original_nonzero_denominators_inverted_and_fully_multiplied_back",
                "alpha_inverse_product_verified","all_base_multiplication_columns_verified_in_original_field",
                "all_272_original_two_chart_evaluation_transitions_verified",
                "all_original_frames_and_cusp_conjugates_preserved"):
        assert field[key] is True
    assert field["original_common_82_power_cancels_exactly"]==6
    stats={}
    for chart in ("tau","sigma"):
        vectors=field["evaluation_vectors"][chart]
        matrix=field["base_multiplication_matrices"][chart]
        assert len(vectors)==272 and all(len(row)==20 for row in vectors)
        assert len(matrix)==20 and all(len(row)==20 for row in matrix)
        for row in vectors+matrix:
            for value in row:
                rational(value)
        index=ref(certificate["two_chart_cusp_ideal_indexes"][chart])
        assert index["chart"]==chart and index["source_field_interface"]==field_spec
        assert index["normal_basis_rank"]==272 and index["normal_basis_degrees"]==EPS
        assert index["actual_reachable_rank"]==20 and index["actual_total_diagonal_degree"]==20
        assert index["actual_quotient_dimension_over_Q"]==20 and index["actual_step_count"]==292
        for key in ("all_272_original_relations_verified_in_full_finite_algebra",
                    "canonical_lower_triangular_monic_and_reduced_conditions_verified",
                    "complete_polynomial_kernel_certified_by_inclusion_and_equal_colength",
                    "quotient_is_original_separable_cusp_field",
                    "reduced_cusp_multiplicity_one_at_all_20_geometric_cusps"):
            assert index[key] is True
        history=[]
        entry=index["latest_completed_step"]
        while entry is not None:
            value=ref(entry)
            history.append((entry,value))
            entry=value["previous_completed_step"]
        assert len(history)==292
        a,k=271,0
        selected,relations,pivots=[],[],[]
        degrees=[None]*272
        for number,(entry,value) in enumerate(reversed(history)):
            assert value["step_number"]==number and value["chart"]==chart
            assert value["source_field_interface"]==field_spec
            assert value["normal_basis_index"]==a and value["power"]==k
            assert value["previous_selected_steps"]==selected
            assert value["full_20_coordinate_echelon_multiply_back_verified"] is True
            assert len(value["original_candidate_vector"])==20
            if value["kind"]=="independent":
                assert value["selected_position"]==len(selected) and value["pivot_row"] not in pivots
                rational(value["pivot_value"],True)
                assert len(value["normalized_echelon_vector"])==20
                assert len(value["echelon_in_selected_original_vectors"])==len(selected)+1
                assert len(value["next_candidate_vector"])==20
                assert value["actual_independence_certified_by_new_nonzero_pivot"] is True
                selected.append(entry);pivots.append(value["pivot_row"]);k+=1
            else:
                assert value["kind"]=="first_dependence"
                assert value["first_dependent_power"]==value["monic_diagonal_degree"]==k
                assert value["complete_relation_evaluation_zero_in_all_20_original_coordinates"] is True
                assert len(value["relation_coefficients_in_selected_vectors"])==len(selected)
                degrees[a]=k
                leading=0
                for term in value["column_terms"]:
                    b,j=term["normal_basis_row"],term["power"]
                    rational(term["coefficient"],True)
                    assert b>=a
                    if b==a and j==k:
                        assert term["coefficient"]==["1","1"]
                        leading+=1
                    else:
                        assert 0<=j<degrees[b]
                assert leading==1
                relations.append(entry);a-=1;k=0
        assert a==-1 and len(selected)==20 and len(relations)==272 and sorted(pivots)==list(range(20))
        assert degrees==index["actual_diagonal_degrees"] and sum(degrees)==20
        assert selected==index["selected_original_chain_vectors"]
        assert list(reversed(relations))==index["Hermite_columns_in_original_basis_order"]
        minor=ref(index["actual_reachable_minor"])
        assert minor["selected_original_chain_vectors"]==selected and minor["actual_pivot_rows"]==pivots
        assert minor["actual_rank"]==20 and minor["exact_minor_shape"]==[20,20]
        rational(minor["actual_nonzero_rational_determinant"],True)
        assert minor["minor_computed_over_Q_in_original_real_cyclotomic_coordinates"] is True
        assert minor["constant_evaluation_matrix_rank_or_base_primitivity_assumed"] is False
        stats[chart]={"actual_rank":20,"actual_colength":20,
                      "actual_nonmonic_coefficients":index["actual_nonmonic_nonzero_coefficient_count"]}
    full=read(out/"full-outputs-manifest.json")
    assert full["result"]==RESULT
    expected_files=set()
    for row in full["files"]:
        assert row["file"] not in expected_files and file_spec(out/row["file"])==plain(row)
        expected_files.add(row["file"])
    assert expected_files=={p.name for p in out.iterdir() if p.is_file() and p.name not in ("full-outputs-manifest.json",REFERENCE)}
    reference=read(out/REFERENCE)
    assert reference["manifest_sha256"]==sha(out/"full-outputs-manifest.json") and reference["file_count"]==len(expected_files)
    print(json.dumps({"R820_VERIFY_REVIEW":{"complete":True,"selected_input_files_verified":len(expected),
        "complete_stage_files_verified":len(entries),"charts":stats,"actual_core_seconds":certificate["seconds"],
        "general_polar_ideal_eta_or_height_computed":False}}),flush=True)
    return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=["compute","verify"])
    args=parser.parse_args()
    out=Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT/"output"
    if args.mode=="compute":
        request=read(REQUEST)
        assert request["session"]=="serre-public-astra-20261115"
        return compute(request["job"],out)
    return verify(read(out/"public-actions-input.json")["job"],out)


if __name__=="__main__":
    sys.exit(main())
