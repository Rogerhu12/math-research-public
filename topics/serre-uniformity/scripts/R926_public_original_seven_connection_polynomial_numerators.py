#!/usr/bin/env python3
"""R926 standard-library selected-source, retained-carrier and public Actions driver."""
import argparse
import copy
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
import traceback

S=Path(__file__).resolve().parent
TOPIC=S.parent
REPO=TOPIC.parent.parent
REPOSITORY="Rogerhu12/math-research-public"
RESULT="R926-original-seven-bounded-connection-polynomial-numerators"
FINAL="p41-original-seven-bounded-connection-polynomial-numerators-certificate.json"
PREFIX="R926-"
CORE="R926_original_seven_connection_polynomial_numerators.py"
REQUEST=TOPIC/"notes/R926-seven-connection-polynomial-numerators-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R926-retained-original-inputs.tar.gz"
INVENTORY="R926-original-source-inventory.json"
INPUT_RECEIPT="R926-retained-inputs-receipt.json"
EXPANDED="R926-expanded-job.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
GROUPS=("R905",)
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
LABELS=("D1","D2","D3","D4","D5","X","DN")
BLOCK=16
IO=None

STRATEGY={
    "original_curve":"original genus127 Y, level82, original minus3 descent",
    "prime":P,"normal_basis_rank":N,"normal_basis_degrees":EPS,
    "divisor_order":list(LABELS),
    "original_differential_basis":"(z-a)^k times trace dual of original F column times dz",
    "original_F_column_section_weights":[2]*146+[3]*126,
    "original_543_selection_and_all670_solution_coefficients_preserved":True,
    "whole_D_multiplier":"Z=Q_D*L_a*T_tau*E_D on the full canonical quotient, dimension272",
    "denominator":"d(a+t)=det(I-tZ)=det(F(a+t))/det(F(a))",
    "norm_algorithm":"new characteristic polynomial of the actual full Z matrix, reverse all273 coefficients",
    "Taylor_recurrence":"x_r=F0^-t*(c_r-sum_(m=1)^min(3,r) F_m^t*x_(r-m))",
    "Taylor_vector_count":274,"Taylor_atomic_block_size":BLOCK,
    "numerator":"y=(d*x) modulo t^274, with exact global degree bound271+epsilon_i",
    "full_acceptance":"all272 rows of F^t*y=d*c at all277 polynomial coefficients",
    "basis_coordinate":"t=z-a explicitly retained; also emit actual z coefficients",
    "old_F_inverse_543_system_original_D_primitive_or_old_characteristic_relation_recomputed":False,
    "source_factors_ramification_nilpotents_or_D_H_intersections_discarded":False,
    "actual_output_only_original_p753_reduction":True,
    "shared_R_target_units_Hecke_calibration_or_height_computed":False,
    "budget_and_requested_divisor_count_excluded_from_identity":True}

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(4*1024*1024),b""):h.update(b)
    return h.hexdigest()

def read(path):
    path=Path(path)
    with (gzip.open if path.suffix==".gz" else open)(path,"rt",encoding="utf-8") as f:
        return json.load(f)

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    raw=(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode()
    if path.suffix==".gz":
        with tmp.open("wb") as f:
            with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0,compresslevel=2) as z:z.write(raw)
    else:tmp.write_bytes(raw)
    tmp.replace(path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def plain(row):
    out={k:row[k] for k in ("file","bytes","sha256")}
    p=PurePosixPath(out["file"])
    assert len(p.parts)==1 and p.name not in ("",".","..") and "\\" not in out["file"]
    assert isinstance(out["bytes"],int) and out["bytes"]>=0 and re.fullmatch("[0-9a-f]{64}",out["sha256"])
    return out

def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}

def identity(source):
    out={**{k:source[k] for k in BASE},"configuration_sha256":source["configuration_sha256"],
         "selected_files_sha256":fingerprint(source["files"]),
         "stage_result_location":source["stage_result_location"]}
    key="certificate" if source.get("certificate") is not None else "configuration_stage"
    out[key]=plain(source[key])
    return out

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],
            "python_flint":"0.9.0","p":41,"method_sha256":item["method_sha256"],"proofs":item["proofs"],
            "sources":{g:identity(item["sources"][g]) for g in GROUPS},"inputs":item["inputs"],"strategy":STRATEGY}

def same_source(left,right):
    assert all(str(left[k])==str(right[k]) for k in BASE)
    assert left["configuration_sha256"]==right["configuration_sha256"]

def shape(raw,m,n):
    assert len(raw)==m and all(len(row)==n for row in raw),(m,n)

class Source:
    def __init__(self,group,item,root):
        self.group,self.item=group,item
        self.folder=Path(root)/group
        self.files={n:plain(r) for n,r in item["files"].items()};self.checked=set()
        assert all(k==r["file"] for k,r in self.files.items())
        assert spec(self.folder/MANIFEST)==self.files[MANIFEST]
        assert self.files[MANIFEST]["sha256"]==item["manifest_sha256"]
        manifest=read(self.folder/MANIFEST)
        assert manifest["result"]==item["result"]
        indexed={r["file"]:plain(r) for r in manifest["files"]}
        assert len(indexed)==len(manifest["files"])
        indexed[MANIFEST]=self.files[MANIFEST]
        assert all(indexed[n]==r for n,r in self.files.items())
        initial=self.raw("public-actions-input.json");run=self.raw("run-receipt.json")
        core=self.raw("core-receipt.json")
        assert initial["source_commit"]==run["source_commit"]==item["source_commit"]
        assert str(run["workflow_run_id"])==str(item["run_id"])
        recorded=initial["core_sha256"] if "core_sha256" in initial else initial["job"]["core_sha256"]
        assert recorded==core["source_sha256"]==item["core_sha256"]
        assert run["core_receipt_sha256"]==self.files["core-receipt.json"]["sha256"]
        self.certificate=None
        if item.get("certificate") is not None:
            self.certificate=self.raw(item["certificate"]["file"])
            assert self.files[item["certificate"]["file"]]==plain(item["certificate"])
            assert self.certificate["complete"] is True and self.certificate["result"]==item["result"]
            assert run["complete"] is True and core["complete"] is True and run["process_exit_code"]==0
            assert core["certificate_sha256"]==item["certificate"]["sha256"]
            self.tag=self.certificate["configuration"]
        else:
            assert group=="R827" and run["complete"] is False and core["complete"] is False
            assert run["process_exit_code"]==124
            anchor=self.raw(item["configuration_stage"]["file"])
            assert anchor["complete"] is True
            self.tag=anchor["configuration"]
        assert fingerprint(self.tag)==item["configuration_sha256"]
        assert self.tag["result"]==item["result"]
        assert self.tag.get("source_sha256",self.tag.get("core_sha256"))==item["core_sha256"]
        if core.get("configuration") is not None:assert core["configuration"]==self.tag
        if core.get("configuration_sha256") is not None:assert core["configuration_sha256"]==item["configuration_sha256"]
        assert item["stage_result_location"]==("configuration" if group=="R827" else "top_level")

    def raw(self,name):
        if name not in self.checked:
            assert spec(self.folder/name)==self.files[name],(self.group,name)
            self.checked.add(name)
        return read(self.folder/name)

    def stage(self,row):
        row=plain(row);assert self.files[row["file"]]==row
        value=self.raw(row["file"])
        assert value["complete"] is True and value["configuration"]==self.tag,(self.group,row["file"])
        if self.item["stage_result_location"]=="configuration":
            assert "result" not in value and value["configuration"]["result"]==self.item["result"]
        else:
            assert value["result"]==self.item["result"]
        return value

def bound(folder,row):
    row=plain(row);path=Path(folder)/row["file"]
    assert spec(path)==row,("bound_file",row["file"])
    return path

def topic_path(name):
    p=PurePosixPath(name)
    assert not p.is_absolute() and ".." not in p.parts
    path=(TOPIC/str(p)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path

def pack(retained,sources,target):
    tmp=Path(target).with_name(Path(target).name+".tmp")
    with tmp.open("wb") as raw:
        with gzip.GzipFile(filename="",fileobj=raw,mode="wb",mtime=0,compresslevel=2) as zipped:
            with tarfile.open(fileobj=zipped,mode="w|") as archive:
                for group in sorted(sources):
                    for name,row in sorted(sources[group]["files"].items()):
                        path=bound(Path(retained)/group,row)
                        info=archive.gettarinfo(str(path),arcname=group+"/"+name)
                        info.uid=info.gid=0;info.uname=info.gname="";info.mtime=0
                        with path.open("rb") as stream:
                            archive.addfile(info,stream)
    tmp.replace(target)

def unpack(package,retained,sources):
    seen=set();Path(retained).mkdir(parents=True,exist_ok=True)
    with tarfile.open(package,"r|gz") as archive:
        for member in archive:
            if member.isdir():
                continue
            path=PurePosixPath(member.name)
            assert member.isfile() and not path.is_absolute() and ".." not in path.parts and "\\" not in member.name
            assert len(path.parts)==2
            group,name=path.parts;key=(group,name)
            assert group in sources and name in sources[group]["files"] and key not in seen
            row=sources[group]["files"][name];assert member.size==row["bytes"]
            target=Path(retained)/group/name;target.parent.mkdir(parents=True,exist_ok=True)
            tmp=target.with_name(target.name+".download");h=hashlib.sha256();count=0
            with archive.extractfile(member) as src,tmp.open("wb") as dst:
                for chunk in iter(lambda:src.read(4*1024*1024),b""):
                    dst.write(chunk);h.update(chunk);count+=len(chunk)
            assert count==row["bytes"] and h.hexdigest()==row["sha256"]
            if target.exists():
                assert spec(target)==plain(row);tmp.unlink()
            else:
                tmp.replace(target)
            seen.add(key)
    assert seen=={(g,n) for g in sources for n in sources[g]["files"]}

def output_manifest(out):
    files=[]
    for path in sorted(Path(out).iterdir()):
        if not path.is_file() or path.name in (MANIFEST,REFERENCE):
            continue
        if path.name.endswith((".tmp",".download",".partial")):
            continue
        files.append(spec(path))
    save(Path(out)/MANIFEST,{"result":RESULT,"source_commit":os.environ["GITHUB_SHA"],
                            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"files":files})
    save(Path(out)/REFERENCE,{"result":RESULT,**spec(Path(out)/MANIFEST)})
    return spec(Path(out)/MANIFEST)


def load_io():
    global IO
    path=S/RANGE_FILE
    assert sha(path)==RANGE_SHA
    description=importlib.util.spec_from_file_location("R926_frozen_stdlib_Range",path)
    IO=importlib.util.module_from_spec(description);description.loader.exec_module(IO)

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve() and item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False and 0<item["budget_minutes"]<=300
    assert 1<=item["maximum_divisors"]<=7
    assert item["core"]==CORE and sha(S/CORE)==item["core_sha256"]
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["io_helper"]==RANGE_FILE and item["io_helper_sha256"]==RANGE_SHA
    assert set(item["sources"])==set(GROUPS)
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():assert sha(topic_path(row["path"]))==row["sha256"]
    for group,source in item["sources"].items():
        assert source["files"] is None
        names=source["required_names"]
        assert len(names)==len(set(names)) and MANIFEST in names and set(META).issubset(names)
        for name in names:
            assert Path(name).name==name and name not in ("",".","..") and "\\" not in name
        assert all(n in names and plain(r)["file"]==n for n,r in source["pinned_files"].items())
    load_io()

def request_contract(raw):
    return {"result":raw["result"],"p":raw["p"],"core_sha256":raw["core_sha256"],
        "method_sha256":raw["method_sha256"],"proofs":raw["proofs"],
        "sources":raw["sources"],"input_bindings":raw["input_bindings"],"strategy":STRATEGY}

def resolve_inputs(bindings,sources):
    def walk(value):
        if isinstance(value,list):return [walk(row) for row in value]
        assert isinstance(value,dict)
        if "source_group" in value:
            assert set(value)=={"source_group","file"}
            group,name=value["source_group"],value["file"]
            assert group in sources and name in sources[group]["files"]
            return {"source_group":group,**plain(sources[group]["files"][name])}
        return {key:walk(row) for key,row in value.items()}
    return walk(bindings)

def expanded_item(raw,sources):
    assert set(sources)==set(GROUPS)
    for group in GROUPS:
        expected=raw["sources"][group];actual=sources[group]
        assert {k:v for k,v in actual.items() if k!="files"}=={k:v for k,v in expected.items() if k!="files"}
        assert set(actual["files"])==set(expected["required_names"])
        assert all(n==plain(r)["file"] for n,r in actual["files"].items())
        assert actual["files"][MANIFEST]["sha256"]==expected["manifest_sha256"]
        assert actual["files"][MANIFEST]["bytes"]==expected["manifest_bytes"]
        for name,row in expected["pinned_files"].items():assert actual["files"][name]==plain(row),(group,name)
    item=copy.deepcopy(raw);item["sources"]=sources
    item["inputs"]=resolve_inputs(item["input_bindings"],sources)
    item["source_request_contract_sha256"]=fingerprint(request_contract(raw))
    return item

def selected_manifest(rawsource,path):
    assert path.name==MANIFEST and sha(path)==rawsource["manifest_sha256"]
    assert path.stat().st_size==rawsource["manifest_bytes"]
    value=read(path);assert value["result"]==rawsource["result"]
    if "source_commit" in value:assert value["source_commit"]==rawsource["source_commit"]
    if "workflow_run_id" in value:assert str(value["workflow_run_id"])==str(rawsource["run_id"])
    entries={row["file"]:plain(row) for row in value["files"]}
    assert len(entries)==len(value["files"])==rawsource["manifest_file_count"]
    assert MANIFEST not in entries
    entries[MANIFEST]=spec(path)
    assert set(rawsource["required_names"]).issubset(entries)
    chosen={name:entries[name] for name in rawsource["required_names"]}
    for name,row in rawsource["pinned_files"].items():assert chosen[name]==plain(row),(name,"pinned_source_member")
    source=copy.deepcopy(rawsource);source["files"]=chosen
    return source

def tar_manifest(package,folder,rawsource):
    target=folder/MANIFEST
    if target.exists():
        assert sha(target)==rawsource["manifest_sha256"] and target.stat().st_size==rawsource["manifest_bytes"]
        return
    seen=False
    with tarfile.open(package,"r|gz") as archive:
        for member in archive:
            if member.isdir():continue
            p=PurePosixPath(member.name)
            assert member.isfile() and not p.is_absolute() and ".." not in p.parts and "\\" not in member.name
            assert len(p.parts)==2 and p.parts[0]=="original"
            if p.name!=MANIFEST:continue
            assert not seen;seen=True
            assert member.size==rawsource["manifest_bytes"]
            tmp=target.with_name(MANIFEST+".download");h=hashlib.sha256();size=0
            with archive.extractfile(member) as inp,tmp.open("wb") as out:
                for chunk in iter(lambda:inp.read(4*1024*1024),b""):
                    out.write(chunk);h.update(chunk);size+=len(chunk)
            assert size==rawsource["manifest_bytes"] and h.hexdigest()==rawsource["manifest_sha256"]
            tmp.replace(target)
    assert seen,"completed transport lacks original manifest"

def selected_from_tar(package,retained,source):
    root=Path(retained);root.mkdir(parents=True,exist_ok=True)
    selected=source["files"];seen=set()
    with tarfile.open(package,"r|gz") as stream:
        for member in stream:
            if member.isdir():continue
            p=PurePosixPath(member.name)
            assert member.isfile() and not p.is_absolute() and ".." not in p.parts
            assert "\\" not in member.name and len(p.parts)==2 and p.parts[0]=="original"
            name=p.name
            if name not in selected:continue
            assert name not in seen;seen.add(name)
            row=plain(selected[name]);assert member.size==row["bytes"]
            dst=root/name;tmp=dst.with_name(name+".download");h=hashlib.sha256();count=0
            with stream.extractfile(member) as src,tmp.open("wb") as out:
                for chunk in iter(lambda:src.read(4*1024*1024),b""):
                    out.write(chunk);h.update(chunk);count+=len(chunk)
            assert count==row["bytes"] and h.hexdigest()==row["sha256"],name
            if dst.exists():assert spec(dst)==row;tmp.unlink()
            else:tmp.replace(dst)
    assert seen==set(selected),("prepared_transport_incomplete",sorted(set(selected)-seen))

def fetch_source(raw,group,retained,work):
    rawsource=raw["sources"][group];folder=Path(retained)/group
    folder.mkdir(parents=True,exist_ok=True)
    prepared=raw.get("prepared_transports",{}).get(group)
    if prepared is not None:
        archive=IO.Archive(prepared["archive"],Path(work)/("transport-"+group),whole=False)
        try:
            package=plain(prepared["package"]);path=Path(work)/(group+"-"+package["file"])
            if path.exists():assert spec(path)=={**package,"file":path.name}
            else:archive.extract_bound(package["file"],package["sha256"],path,package["bytes"])
            tar_manifest(path,folder,rawsource)
            source=selected_manifest(rawsource,folder/MANIFEST)
            selected_from_tar(path,folder,source)
            return source,{"kind":"completed_original_intake","archive":prepared["archive"],
                "package":package,"transport":archive.receipt(),"original_mathematical_identity_unchanged":True}
        finally:archive.close()
    archive=IO.Archive(rawsource,Path(work)/("original-"+group),whole=False)
    try:
        if (folder/MANIFEST).exists():
            assert sha(folder/MANIFEST)==rawsource["manifest_sha256"]
        else:archive.extract_bound(MANIFEST,rawsource["manifest_sha256"],folder/MANIFEST,rawsource["manifest_bytes"])
        source=selected_manifest(rawsource,folder/MANIFEST)
        tasks=[]
        for name,row in source["files"].items():
            if (folder/name).exists():assert spec(folder/name)==row
            else:tasks.append((name,row["sha256"],folder/name,row["bytes"]))
        if tasks:archive.extract_many(tasks)
        return source,{"kind":"original_artifact_Range","source":{k:source[k] for k in BASE},
            "transport":archive.receipt(),"all_selected_bytes_manifest_bound":True}
    finally:archive.close()

def source_review(item,retained):
    source=Source("R905",item["sources"]["R905"],retained)
    def stage(row):
        assert row["source_group"]=="R905"
        return source.stage(row)
    cert=source.certificate
    assert cert["complete"] is True and cert["prime"]==P
    assert cert["source_divisor_order"]==list(LABELS)
    assert cert["actual_completed_source_connections"]==7
    assert cert["actual_seven_complete_full_principal_parts_solutions"] is True
    assert set(item["inputs"]["divisors"])==set(LABELS)
    details={}
    for label in LABELS:
        inputs=item["inputs"]["divisors"][label]
        assert set(inputs)=={"connection","bundle","quotient","solution"}
        assert plain(cert["complete_source_connection_certificates"][label])==plain(inputs["connection"])
        connection=stage(inputs["connection"]);graph=stage(inputs["bundle"])
        model=stage(inputs["quotient"]);solution=stage(inputs["solution"])
        for value in (connection,graph,model,solution):
            assert value["prime"]==P and value["label"]==label
        assert graph["both_F_inverse_products_verified"] is True
        assert graph["full_rank272_equal_degree146_bundle_isomorphism_certified"] is True
        assert graph["h0_H_minus_D_zero_follows_from_actual_unit_graph"] is True
        assert graph["column_weights"]==[1]*146+[0]*126
        assert graph["trace_dual_differential_space_dimension"]==670
        assert len(graph["F_coefficients_low_to_high"])==4
        for value in graph["F_coefficients_low_to_high"]:shape(value,N,N)
        shape(graph["F_at_auxiliary_fibre_mod_prime"],N,N)
        shape(graph["inverse_F_at_auxiliary_fibre_mod_prime"],N,N)
        assert model["auxiliary_z"]==graph["auxiliary_z"]
        assert model["whole_D_algebra_dimension"]==272 and model["whole_D_plus_H_dimension"]==544
        for flag in ("all690_original_polynomial_division_identities_verified",
                     "all146_U_relations_and272_canonical_quotient_rows_verified",
                     "D_H_intersections_not_assumed_empty"):
            assert model[flag] is True
        assert plain(model["source_complete_bundle_unit_graph"])==plain(inputs["bundle"])
        assert plain(model["source_F0_inverse_reused_without_recomputation"])==plain(inputs["bundle"])
        shape(model["V2_D_quotient_projection_mod_prime"],272,418)
        shape(model["V3_to_V2_h_division_mod_prime"],418,690)
        shape(model["whole_D_algebra_unit_mod_prime"],272,1)
        free=model["V2_D_quotient_free_rows"]
        assert len(free)==272 and free==sorted(set(free)) and all(0<=r<418 for r in free)
        assert solution["actual_rank"]==solution["required_full_principal_parts_rank"]==543
        assert solution["rank_is_required"] is True and solution["all_original_rows_multiplied_back"] is True
        assert solution["free_coefficients_set_to_zero"] is True
        assert len(solution["solution_coefficients_mod_prime"])==670
        assert len(solution["selected_rows"])==len(solution["selected_columns"])==543
        assert connection["actual_principal_parts_rank"]==543
        for flag in ("all544_principal_part_equations_multiplied_back",
                     "exact_regular_connection_on_original_O_H_minus_D_as_expression_certified",
                     "exact_full_principal_parts_not_only_residues_certified",
                     "all_ramification_nilpotents_and_D_H_intersections_preserved"):
            assert connection[flag] is True
        assert plain(connection["source_complete_bundle_unit_graph"])==plain(inputs["bundle"])
        assert plain(connection["source_complete_quotient_models"])==plain(inputs["quotient"])
        assert plain(connection["source_full543_unit_solution"])==plain(inputs["solution"])
        assert plain(solution["source_full_principal_parts_matrix"])==plain(connection["source_full_principal_parts_matrix"])
        assert plain(solution["source_full_target"])==plain(connection["source_full_target"])
        dag=connection["exact_connection_DAG"]
        assert dag["original_rational_section"]=="1 of O(H-D)" and dag["full_logarithmic_principal_parts"]=="H-D"
        assert dag["basis"]["auxiliary_z"]==graph["auxiliary_z"]
        assert dag["basis"]["coefficient_power"]=="(z-a)^k" and dag["basis"]["differential"]=="the original dz"
        assert dag["basis"]["indices"]==[[i,k] for i in range(N) for k in range(2 if i<146 else 3)]
        assert dag["coefficients"]["rows"]==solution["selected_rows"]
        assert dag["coefficients"]["columns"]==solution["selected_columns"]
        details[label]={"auxiliary_z":graph["auxiliary_z"],"original_F_determinant":graph["actual_F_determinant_mod_prime"],
            "original_full_principal_parts_rank":543,"old_full_inverse_not_recomputed":True}
    return {"result":RESULT,"source_groups":["R905"],"source_divisor_order":list(LABELS),
        "selected_file_count":len(item["sources"]["R905"]["files"]),"details":details,
        "all_original_source_bytes_configuration_and_543_gauges_verified":True,
        "old_544_by670_matrices_not_downloaded_or_recomputed":True,
        "new_mathematics_executed":False}

def prepare(raw,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R926";retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (BUNDLE,INVENTORY,INPUT_RECEIPT)):
        inventory=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        assert inventory["source_request_contract_sha256"]==fingerprint(request_contract(raw))
        item=expanded_item(raw,inventory["sources"])
        assert inventory["inputs"]==item["inputs"]
        assert receipt["source_inventory"]==spec(out/INVENTORY) and receipt["source_bundle"]==spec(out/BUNDLE)
        assert receipt["source_identities"]=={g:identity(item["sources"][g]) for g in GROUPS}
        unpack(out/BUNDLE,retained,item["sources"])
        return item,retained,source_review(item,retained)
    assert allow_download,"Offline verification requires the completed selected source carrier."
    work=out.parent/"R926-source-transport";work.mkdir(parents=True,exist_ok=True)
    sources={};transports={}
    for group in GROUPS:sources[group],transports[group]=fetch_source(raw,group,retained,work)
    item=expanded_item(raw,sources);review=source_review(item,retained)
    save(out/INVENTORY,{"result":RESULT,"complete":True,"sources":sources,"inputs":item["inputs"],
        "source_request_contract_sha256":fingerprint(request_contract(raw)),
        "transports":transports,"original_selected_bytes_and_tags_preserved":True,
        "manifest_expansion_is_only_IO":True,"new_mathematics_executed":False,"old_large_carriers_not_needed":True})
    pack(retained,sources,out/BUNDLE)
    save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,
        "source_inventory":spec(out/INVENTORY),"source_bundle":spec(out/BUNDLE),
        "source_identities":{g:identity(sources[g]) for g in GROUPS},
        "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
        "all_original_source_bytes_and_schemas_verified":True,"new_mathematics_executed":False})
    print("R926_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
    return item,retained,review

def restore(raw,out):
    resume=raw.get("resume")
    if not resume:return
    assert resume["result"]==RESULT and resume["core_sha256"]==raw["core_sha256"]
    directory=out.parent/"R926-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R926-resume-archive",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],directory/MANIFEST,resume.get("manifest_bytes"))
        full=read(directory/MANIFEST)
        assert full["result"]==RESULT and full["source_commit"]==resume["source_commit"]
        entries={r["file"]:plain(r) for r in full["files"]};assert len(entries)==len(full["files"])
        required={"public-actions-input.json","run-receipt.json",BUNDLE,INVENTORY,INPUT_RECEIPT}
        assert required.issubset(entries)
        names=required|({"core-receipt.json"}&set(entries))
        archive.extract_many([(n,entries[n]["sha256"],directory/n,entries[n]["bytes"]) for n in sorted(names)])
        initial=read(directory/"public-actions-input.json");run=read(directory/"run-receipt.json")
        assert initial["result"]==run["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]==resume["source_commit"]
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        assert initial["core_sha256"]==raw["core_sha256"] and initial["wrapper_sha256"]==raw["wrapper_sha256"]
        inventory=read(directory/INVENTORY);receipt=read(directory/INPUT_RECEIPT)
        assert inventory["source_request_contract_sha256"]==fingerprint(request_contract(raw))
        item=expanded_item(raw,inventory["sources"]);tag=expected_tag(item)
        assert inventory["inputs"]==item["inputs"]
        assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
        assert expected_tag(initial["job"])==tag
        assert receipt["source_inventory"]==entries[INVENTORY] and receipt["source_bundle"]==entries[BUNDLE]
        core=None
        if run["core_receipt_sha256"] is not None:
            assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
            core=read(directory/"core-receipt.json")
            assert core["result"]==RESULT and core["source_sha256"]==raw["core_sha256"]
            if core.get("configuration") is not None:assert core["configuration"]==tag
        else:
            assert run["complete"] is False and run["process_exit_code"]==124 and run["outer_timeout"] is True
        for name in (BUNDLE,INVENTORY,INPUT_RECEIPT):
            if (out/name).exists():assert spec(out/name)==entries[name]
            else:shutil.copyfile(directory/name,out/name)
        stages=[n for n in entries if n.startswith(PREFIX) and n.endswith(".json.gz")]
        archive.extract_many([(n,entries[n]["sha256"],directory/n,entries[n]["bytes"]) for n in stages])
        for name in stages:
            value=read(directory/name)
            assert value["result"]==RESULT and value["configuration"]==tag
            assert value["complete"] is (False if name==PREFIX+"current.json.gz" else True)
            if (out/name).exists():assert spec(out/name)==entries[name]
            else:shutil.copyfile(directory/name,out/name)
        if FINAL in entries:
            archive.extract_bound(FINAL,entries[FINAL]["sha256"],directory/FINAL,entries[FINAL]["bytes"])
            cert=read(directory/FINAL)
            assert cert["result"]==RESULT and cert["configuration"]==tag
            if cert["complete"] is True:
                assert run["complete"] is True and core is not None and core["complete"] is True
                assert core["certificate_sha256"]==entries[FINAL]["sha256"]
                sm=plain(cert["stage_manifest"]);assert entries[sm["file"]]==sm
                for row in read(bound(directory,sm))["files"]:assert entries[row["file"]]==plain(row)
                if cert.get("resume_state") is not None:
                    assert entries[cert["resume_state"]["file"]]==plain(cert["resume_state"])
                shutil.copyfile(directory/FINAL,out/FINAL)
        save(out/"resume-import-receipt.json",{"result":RESULT,"complete":True,"source":resume,
            "source_manifest":spec(directory/MANIFEST),"restored_stage_count":len(stages),
            "mathematical_configuration_sha256":fingerprint(tag),"same_core_and_source_bytes_preserved":True,
            "false_historical_FINAL_not_used_to_overwrite_newer_current":True,
            "original_missing_core_receipt_retained_as_missing":core is None,"transport":archive.receipt()})
    finally:archive.close()

def compute(raw,out,request):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    code,error,outer_timeout=1,None,False
    try:
        restore(raw,out)
        item,retained,review=prepare(raw,out)
        save(out/EXPANDED,item);tag=expected_tag(item)
        save(out/"public-actions-input.json",{
            "result":RESULT,"p":41,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"job":item,
            "core_sha256":item["core_sha256"],"wrapper_sha256":item["wrapper_sha256"],
            "request_sha256":sha(request),"workflow_sha256":sha(REPO/item["workflow"]),
            "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
            "source_request_contract_sha256":fingerprint(request_contract(raw)),
            "expanded_job":spec(out/EXPANDED),"source_inventory":spec(out/INVENTORY),
            "mathematical_configuration_sha256":fingerprint(tag),
            "source_identities":{g:identity(item["sources"][g]) for g in GROUPS},
            "new_mathematics_in_wrapper":False})
        command=[sys.executable,str(S/CORE),"--config",str(out/EXPANDED),
            "--retained",str(retained),"--output",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"core.log").open("ab") as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:code=process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                outer_timeout=True;os.killpg(process.pid,signal.SIGTERM)
                try:process.wait(timeout=15)
                except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
                code=124;error="outer_timeout"
        if code==0:assert read(out/FINAL)["complete"] is True
        print((out/"core.log").read_text(errors="replace")[-16000:],flush=True)
    except Exception as exc:
        if code in (0,1):code=1
        error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    finally:
        save(out/"run-receipt.json",{
            "result":RESULT,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_sha256":raw["core_sha256"],"wrapper_sha256":raw["wrapper_sha256"],
            "complete":code==0,"process_exit_code":code,"error":error,"outer_timeout":outer_timeout,
            "execution_environment":"public-repository-github-actions",
            "core_receipt_sha256":sha(out/"core-receipt.json") if (out/"core-receipt.json").exists() else None,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    return code

def output_stage(out,entries,tag,row):
    row=plain(row);assert entries[row["file"]]==row
    value=read(bound(out,row))
    assert value["result"]==RESULT and value["complete"] is True and value["configuration"]==tag
    return value

def verify_complete_final(item,out,entries,tag,cert):
    assert cert["prime"]==P and cert["normal_basis_rank"]==N and cert["normal_basis_degrees"]==EPS
    assert cert["source_divisor_order"]==list(LABELS) and cert["actual_completed_divisors"]==7
    assert set(cert["complete_bounded_connection_certificates"])==set(LABELS)
    assert cert["actual_seven_original_bounded_connection_numerators_certified"] is True
    assert cert["same_original_543_choices_and_full_principal_parts_preserved"] is True
    for key in ("source_characteristic_zero_numerator_denominator_arrays_expanded",
                "shared_low_weight_R_computed_in_this_scope",
                "whole_target_denominator_units_or_seven_target_values_computed",
                "Hecke_calibration_nonp_Picard_period_or_height_computed",
                "old_F_inverse_543_solution_or_D_primitive_recomputed"):
        assert cert[key] is False
    audit=output_stage(out,entries,tag,cert["source_audit"])
    assert audit["sources"]=={"R905":identity(item["sources"]["R905"])}
    assert audit["inputs"]==item["inputs"]
    for label in LABELS:
        source=item["inputs"]["divisors"][label]
        complete=output_stage(out,entries,tag,cert["complete_bounded_connection_certificates"][label])
        assert complete["label"]==label and complete["prime"]==P
        assert complete["source_original_connection"]==source["connection"]
        assert complete["source_complete_bundle_F"]==source["bundle"]
        assert complete["source_original_full543_solution"]==source["solution"]
        for key in ("all277_coefficients_times272_rows_verified",
                    "full_original_F_transpose_times_y_equals_d_times_c_verified",
                    "all_original_numerator_degree_bounds_verified",
                    "original_543_gauge_and_full_logarithmic_principal_parts_preserved",
                    "whole_D_norm_all_length272_multiplicities_preserved",
                    "finite_arrays_are_true_original_auxiliary_place_images"):
            assert complete[key] is True
        for key in ("characteristic_zero_numerator_denominator_coordinates_expanded",
                    "target_denominator_units_or_target_connection_values_computed",
                    "Hecke_calibration_nonp_period_or_height_computed"):
            assert complete[key] is False
        expression=complete["exact_characteristic_zero_expression"]
        assert expression["proof"]==item["proofs"]["R922"]
        assert expression["source_original_connection"]==source["connection"]
        assert expression["source_original_exact_F"]==source["bundle"]
        assert expression["source_original_exact_c_unit_solve"]==source["solution"]
        denom=output_stage(out,entries,tag,complete["denominator"])
        numerator=output_stage(out,entries,tag,complete["bounded_numerator"])
        c=output_stage(out,entries,tag,complete["original_c"])
        assert denom["label"]==numerator["label"]==c["label"]==label
        assert denom["auxiliary_z"]==numerator["auxiliary_z"]==c["auxiliary_z"]
        assert denom["source_complete_bundle_F"]==source["bundle"]
        assert len(denom["characteristic_coefficients_ascending_T"])==273
        assert denom["characteristic_coefficients_ascending_T"][-1]==1
        assert len(denom["denominator_coefficients_in_t_low_to_high"])==273
        assert len(denom["denominator_coefficients_in_z_low_to_high"])==273
        assert denom["denominator_coefficients_in_t_low_to_high"][0]==1
        assert 0<=denom["actual_denominator_degree"]<=272
        assert denom["whole_norm_degree_count_before_possible_degree_drop"]==272
        for key in ("full_rank272_characteristic_polynomial_computed","denominator_is_det_I_minus_tZ",
                    "denominator_at_original_auxiliary_point_equals_one",
                    "normalization_and_all_multiplicities_preserved","nilpotent_zero_eigenparts_not_removed"):
            assert denom[key] is True
        mult=output_stage(out,entries,tag,denom["source_whole_D_multiplier"])
        assert mult["source_complete_quotient_model"]==source["quotient"]
        assert mult["whole_D_algebra_dimension"]==272
        assert mult["multiplication_times_original_unit_equals_tau_over_h_verified"] is True
        assert mult["all_nilpotents_and_D_H_intersections_retained"] is True
        shape(mult["whole_multiplication_matrix_mod_prime"],272,272)
        shape(mult["tau_over_h_canonical_coordinates_mod_prime"],272,1)
        assert len(mult["canonical_quotient_free_rows"])==len(mult["original_tau_V2_to_V3_columns"])==272
        assert c["source_original_connection"]==source["connection"]
        assert c["source_original_full543_solution"]==source["solution"]
        shape(c["coefficient_vectors_in_t_low_to_high"],3,272)
        assert len(c["original_selected_rows"])==len(c["original_selected_columns"])==543
        assert c["all670_original_solution_coefficients_used_exactly_once"] is True
        assert c["new_543_solve_or_new_gauge_performed"] is False
        assert numerator["source_original_connection"]==source["connection"]
        assert plain(numerator["source_denominator"])==plain(complete["denominator"])
        assert plain(numerator["source_original_c"])==plain(complete["original_c"])
        assert numerator["actual_Taylor_vector_count"]==274 and numerator["coordinate_dimensions"]==[274,272]
        assert numerator["numerator_degree_bounds"]==[271+e for e in EPS]
        assert numerator["all_original_weighted_numerator_degree_bounds_verified"] is True
        assert numerator["true_t_equals_z_minus_original_auxiliary_point"] is True
        shape(numerator["numerator_coefficients_in_t_low_to_high"],274,272)
        shape(numerator["numerator_coefficients_in_z_low_to_high"],274,272)
        blocks=numerator["complete_Taylor_blocks"];assert len(blocks)==18
        previous=None
        for ordinal,row in enumerate(blocks):
            first=16*ordinal;stop=min(first+16,274)
            block=output_stage(out,entries,tag,row)
            assert block["label"]==label and block["first"]==first and block["stop"]==stop
            assert block["previous_complete_Taylor_block"]==previous
            assert block["source_original_F_and_zero_order_inverse"]==source["bundle"]
            assert plain(block["source_original_c"])==plain(complete["original_c"])
            assert block["recurrence_uses_original_inverse_transpose"] is True
            assert block["old_zero_order_inverse_or_prior_complete_vectors_recomputed"] is False
            shape(block["vectors_low_to_high"],stop-first,272)
            previous=plain(row)
        checks=complete["full_polynomial_coefficient_checks"];assert len(checks)==18
        for ordinal,row in enumerate(checks):
            first=16*ordinal;stop=min(first+16,277)
            block=output_stage(out,entries,tag,row)
            assert block["label"]==label and block["first"]==first and block["stop"]==stop
            assert block["source_original_F"]==source["bundle"]
            assert plain(block["source_original_c"])==plain(complete["original_c"])
            assert plain(block["source_denominator"])==plain(complete["denominator"])
            assert plain(block["source_numerator"])==plain(complete["bounded_numerator"])
            assert block["all272_rows_for_each_coefficient_checked"] is True
            assert block["complete_polynomial_product_equals_d_times_c"] is True
            assert block["left_product_sha256"]==block["right_product_sha256"]

def verify(raw,out):
    out=Path(out);full=read(out/MANIFEST);assert full["result"]==RESULT
    entries={r["file"]:plain(r) for r in full["files"]};assert len(entries)==len(full["files"])
    for name,row in entries.items():assert name==row["file"];bound(out,row)
    reference=read(out/REFERENCE)
    assert reference["result"]==RESULT and plain(reference)==spec(out/MANIFEST)
    run=read(out/"run-receipt.json")
    assert run["result"]==RESULT and run["core_sha256"]==raw["core_sha256"] and run["wrapper_sha256"]==raw["wrapper_sha256"]
    assert run["source_commit"]==full["source_commit"] and str(run["workflow_run_id"])==str(full["workflow_run_id"])
    if not all(n in entries for n in ("public-actions-input.json",INVENTORY,INPUT_RECEIPT,BUNDLE)):
        assert run["complete"] is False and run["process_exit_code"]!=0
        return {"result":RESULT,"complete":False,"failure_before_complete_input_carrier":True,
            "process_exit_code":run["process_exit_code"],"error":run["error"],
            "source_manifest":spec(out/MANIFEST),"new_mathematics_executed_in_IO":False}
    item,retained,review=prepare(raw,out,allow_download=False);tag=expected_tag(item)
    initial=read(out/"public-actions-input.json")
    assert initial["result"]==RESULT and initial["source_commit"]==run["source_commit"]
    assert str(initial["workflow_run_id"])==str(run["workflow_run_id"])
    assert initial["job"]==item and initial["core_sha256"]==item["core_sha256"]
    assert initial["wrapper_sha256"]==item["wrapper_sha256"]
    assert initial["source_request_contract_sha256"]==fingerprint(request_contract(raw))
    assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
    assert initial["source_inventory"]==entries[INVENTORY] and initial["expanded_job"]==entries[EXPANDED]
    assert read(out/EXPANDED)==item
    stages={};currents={}
    for name,row in entries.items():
        if not name.startswith(PREFIX) or not name.endswith(".json.gz"):continue
        value=read(out/name);assert value["result"]==RESULT and value["configuration"]==tag
        if name==PREFIX+"current.json.gz":
            assert value["complete"] is False;currents[name]=row
        else:
            assert value["complete"] is True
            if name.startswith(PREFIX+"stage-manifest-"):
                inv={r["file"]:plain(r) for r in value["files"]}
                assert len(inv)==len(value["files"])
                for n,r in inv.items():assert n!=name and entries[n]==r
            else:stages[name]=row
    core=None
    if run["core_receipt_sha256"] is not None:
        assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
        core=read(out/"core-receipt.json")
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        if core.get("configuration") is not None:assert core["configuration"]==tag
    else:
        assert run["complete"] is False and run["process_exit_code"]==124 and run["outer_timeout"] is True
    cert=None
    if FINAL in entries:
        cert=read(out/FINAL)
        assert cert["result"]==RESULT and cert["configuration"]==tag
        if cert["complete"] is True:
            assert run["complete"] is True and run["process_exit_code"]==0
            assert core is not None and core["complete"] is True
            assert core["certificate_sha256"]==entries[FINAL]["sha256"]
            inventory=output_stage(out,entries,tag,cert["stage_manifest"])
            assert {r["file"]:plain(r) for r in inventory["files"]}==stages
            assert len(inventory["files"])==len(stages)
            if cert.get("resume_state") is not None:assert entries[cert["resume_state"]["file"]]==plain(cert["resume_state"])
            verify_complete_final(item,out,entries,tag,cert)
        else:assert run["complete"] is False
    if run["complete"]:assert cert is not None and cert["complete"] is True
    return {"result":RESULT,"complete":run["complete"],"process_exit_code":run["process_exit_code"],
        "core_receipt_present":core is not None,"outer_timeout":run["outer_timeout"],
        "manifest":spec(out/MANIFEST),"certificate":entries.get(FINAL),"actual_complete_stage_count":len(stages),
        "actual_current_count":len(currents),"retained_source_bundle":entries[BUNDLE],
        "source_inventory":entries[INVENTORY],"source_review":review,
        "configuration_sha256":fingerprint(tag),
        "complete_bounded_connection_certificates":None if cert is None else cert.get("complete_bounded_connection_certificates"),
        "actual_completed_divisors":None if cert is None else cert.get("actual_completed_divisors"),
        "actual_seven_original_bounded_connection_numerators_certified":None if cert is None else cert.get("actual_seven_original_bounded_connection_numerators_certified"),
        "new_mathematics_executed_in_IO":False}

def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("compute","verify"))
    parser.add_argument("--request",type=Path,default=REQUEST)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();raw=read(args.request);guard(raw,args.request)
    if args.mode=="verify":
        result=verify(raw,args.output)
        print("R926_COMPLETE_IO_REVIEW="+json.dumps(result,sort_keys=True),flush=True)
        return 0 if result["complete"] else 1
    code=compute(raw,args.output,args.request)
    try:print("R926_COMPLETE_IO_REVIEW="+json.dumps(verify(raw,args.output),sort_keys=True),flush=True)
    except Exception:
        traceback.print_exc()
        if code==0:code=1
    return code
if __name__=="__main__":sys.exit(main())
