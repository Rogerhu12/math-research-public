#!/usr/bin/env python3
"""R930 standard-library selected-source, retained-carrier and public Actions driver."""
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
RESULT="R930-original-seven-whole-Artin-connection-traces"
FINAL="p41-original-seven-whole-Artin-connection-traces-certificate.json"
PREFIX="R930-"
CORE="R930_original_seven_whole_Artin_connection_traces.py"
REQUEST=TOPIC/"notes/R930-seven-whole-Artin-connection-traces-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R930-retained-original-inputs.tar.gz"
INVENTORY="R930-original-source-inventory.json"
INPUT_RECEIPT="R930-retained-inputs-receipt.json"
EXPANDED="R930-expanded-job.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
GROUPS=("R922","R926","R928","R905","R885","R919")
DIRECT_GROUPS=("R922","R926","R928","R905")
LABELS=("D1","D2","D3","D4","D5","X","DN")
BLOCK=16
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
HELPER="R885_whole_Artin_algebra.py"
IO=None

STRATEGY={
    "original_curve":"original genus127 Y, level82, original minus3 descent",
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "source_node_ordinal":0,"source_z":0,"source_algebra_dimension":272,"whole_correspondence_rank":8,
    "divisor_order":list(LABELS),"normal_basis_degrees":EPS,
    "connection":"alpha_D=(y_D^t*R*beta/d_D)*nu with the original R905 gauge and section1",
    "new_global_contraction":"r_D=y_D^t R, coefficient bound274-epsilon_j",
    "polynomial_product_coefficients_checked":277,"contraction_block_size":BLOCK,
    "target_substitution":"matrix-contract all272 completed target beta, then U-Horner; never source-specialize coefficients",
    "denominator":"full d_D(U) unit on all of E, no factor cancellation claimed",
    "differential_transport":"reuse the completed original R928 J and its two full identities",
    "trace":"whole rank8 multiplication trace on B_D*J",
    "ordinary_trace_row":"old_a8_inverse*[U^7](U^i*old_P_U mod old_monic_P), all8 checked by full multiplication",
    "second_trace_identity":"old_L(B*ell^-1*(1+t*old_PU^-1*H_K))+t*T(B*ell^-1*old_PU^-1*Delta_K)",
    "old_R_G_y_d_J_deltaK_deltaP_inverses_Gamma_or_target_coordinates_recomputed":False,
    "source_factors_nilpotents_or_multiplicities_discarded":False,
    "J_inverse_or_J_unit_required":False,
    "five_Picard_sigma_cY_or_principal_combinations_computed":False,
    "budget_and_maximum_divisors_excluded_from_identity":True}


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
    return {"result":RESULT,"source_sha256":item["core_sha256"],"helper_sha256":item["helper_sha256"],
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
    description=importlib.util.spec_from_file_location("R930_frozen_stdlib_Range",path)
    IO=importlib.util.module_from_spec(description);description.loader.exec_module(IO)

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve() and item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False and 0<item["budget_minutes"]<=300
    assert isinstance(item["maximum_divisors"],int) and 1<=item["maximum_divisors"]<=7
    assert item["core"]==CORE and sha(S/CORE)==item["core_sha256"]
    assert item["helper"]==HELPER and sha(S/HELPER)==item["helper_sha256"]
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["io_helper"]==RANGE_FILE and item["io_helper_sha256"]==RANGE_SHA
    assert set(item["sources"])==set(GROUPS)
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():assert sha(topic_path(row["path"]))==row["sha256"]
    for group,source in item["sources"].items():
        if source["files"] is None:
            names=source["required_names"]
            assert all(n in names and plain(r)["file"]==n for n,r in source["pinned_files"].items())
        else:
            names=list(source["files"])
            assert all(plain(r)["file"]==n for n,r in source["files"].items())
        assert len(names)==len(set(names)) and MANIFEST in names and set(META).issubset(names)
        for name in names:assert Path(name).name==name and name not in ("",".","..") and "\\" not in name
        assert source["stage_result_location"]=="top_level" and source.get("certificate") is not None
        assert source["certificate"]["file"] in names
        refs=source.get("required_references",{})
        if group=="R928":
            assert refs=={"target_frame_unit":{
                "from_file":"R928-complete-target-differential-transport.json.gz",
                "field":"selected_whole_E_unit_trial"}}
            assert all(row["from_file"] in names for row in refs.values())
        else:assert not refs
    transport=item["completed_R928_input_transport"]
    assert transport["source_group"]=="R928" and transport["nested_groups"]==["R885","R919"]
    assert plain(transport["package"])["file"]=="R928-retained-original-inputs.tar.gz"
    assert transport["source_inventory"]["file"]=="R928-original-source-inventory.json"
    assert transport["retained_receipt_file"]=="R928-retained-inputs-receipt.json"
    load_io()

def request_contract(raw):
    return {"result":raw["result"],"p":raw["p"],"core_sha256":raw["core_sha256"],
        "method_sha256":raw["method_sha256"],"helper_sha256":raw["helper_sha256"],"proofs":raw["proofs"],
        "sources":raw["sources"],"input_bindings":raw["input_bindings"],
        "completed_R928_input_transport":raw["completed_R928_input_transport"],"strategy":STRATEGY}

def resolve_inputs(bindings,sources):
    def walk(value):
        if isinstance(value,list):return [walk(row) for row in value]
        assert isinstance(value,dict)
        if "source_group" in value:
            group=value["source_group"];assert group in sources
            if "derived_reference" in value:
                assert set(value)=={"source_group","derived_reference"}
                row=plain(sources[group]["resolved_references"][value["derived_reference"]])
                assert sources[group]["files"][row["file"]]==row
            else:
                assert set(value)=={"source_group","file"}
                row=plain(sources[group]["files"][value["file"]])
            return {"source_group":group,**row}
        return {key:walk(row) for key,row in value.items()}
    return walk(bindings)

def expanded_item(raw,sources):
    assert set(sources)==set(GROUPS)
    for group in GROUPS:
        expected=raw["sources"][group];actual=sources[group]
        if expected["files"] is not None:
            assert actual==expected
            continue
        ignored={"files","resolved_references"}
        assert {k:v for k,v in actual.items() if k not in ignored}=={k:v for k,v in expected.items() if k not in ignored}
        selectors=expected.get("required_references",{})
        resolved=actual.get("resolved_references",{})
        assert set(resolved)==set(selectors)
        names=set(expected["required_names"])
        for key,row in resolved.items():
            row=plain(row);assert row["file"] not in names
            names.add(row["file"])
            assert actual["files"][row["file"]]==row
        assert set(actual["files"])==names
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
    assert len(entries)==len(value["files"])
    if rawsource.get("manifest_file_count") is not None:assert len(entries)==rawsource["manifest_file_count"]
    assert MANIFEST not in entries;entries[MANIFEST]=spec(path)
    assert set(rawsource["required_names"]).issubset(entries)
    chosen={name:entries[name] for name in rawsource["required_names"]}
    for name,row in rawsource["pinned_files"].items():assert chosen[name]==plain(row),(name,"pinned_source_member")
    source=copy.deepcopy(rawsource);source["files"]=chosen
    return source

def extract_nested_subset(package,retained,original_sources,selected_sources):
    expected={(g,n):plain(r) for g,s in original_sources.items() for n,r in s["files"].items()}
    wanted={(g,n):plain(r) for g,s in selected_sources.items() for n,r in s["files"].items()}
    assert set(wanted).issubset(expected)
    assert all(expected[key]==row for key,row in wanted.items())
    seen=set()
    with tarfile.open(package,"r|gz") as archive:
        for member in archive:
            if member.isdir():continue
            p=PurePosixPath(member.name)
            assert member.isfile() and not p.is_absolute() and ".." not in p.parts and "\\" not in member.name
            assert len(p.parts)==2
            key=tuple(p.parts);assert key in expected and key not in seen
            row=expected[key];assert member.size==row["bytes"]
            output=None;target=None;tmp=None;h=hashlib.sha256();count=0
            if key in wanted:
                group,name=key;target=Path(retained)/group/name;target.parent.mkdir(parents=True,exist_ok=True)
                tmp=target.with_name(name+".download");output=tmp.open("wb")
            try:
                with archive.extractfile(member) as src:
                    for chunk in iter(lambda:src.read(4*1024*1024),b""):
                        h.update(chunk);count+=len(chunk)
                        if output is not None:output.write(chunk)
            finally:
                if output is not None:output.close()
            assert count==row["bytes"] and h.hexdigest()==row["sha256"],key
            if tmp is not None:
                if target.exists():assert spec(target)==row;tmp.unlink()
                else:tmp.replace(target)
            seen.add(key)
    assert seen==set(expected)
    return {"all_original_carrier_members_hashed":len(seen),"selected_members_preserved":len(wanted),
            "original_mathematical_tags_or_bytes_changed":False,"new_mathematics_executed":False}

def fetch_sources(raw,retained,work):
    sources={};transports={}
    for group in DIRECT_GROUPS:
        source=raw["sources"][group];folder=Path(retained)/group;folder.mkdir(parents=True,exist_ok=True)
        archive=IO.Archive(source,Path(work)/("original-"+group),whole=False)
        try:
            manifest=folder/MANIFEST
            if manifest.exists():assert sha(manifest)==source["manifest_sha256"] and manifest.stat().st_size==source["manifest_bytes"]
            else:archive.extract_bound(MANIFEST,source["manifest_sha256"],manifest,source["manifest_bytes"])
            expanded=selected_manifest(source,manifest);tasks=[]
            for name,row in expanded["files"].items():
                if (folder/name).exists():assert spec(folder/name)==row
                else:tasks.append((name,row["sha256"],folder/name,row["bytes"]))
            if tasks:archive.extract_many(tasks)
            entries={r["file"]:plain(r) for r in read(manifest)["files"]}
            selectors=source.get("required_references",{})
            if selectors:
                resolved={}
                for key,selector in selectors.items():
                    parent=read(bound(folder,expanded["files"][selector["from_file"]]))
                    row=plain(parent[selector["field"]])
                    assert entries[row["file"]]==row and row["file"] not in expanded["files"]
                    if (folder/row["file"]).exists():assert spec(folder/row["file"])==row
                    else:archive.extract_bound(row["file"],row["sha256"],folder/row["file"],row["bytes"])
                    expanded["files"][row["file"]]=row;resolved[key]=row
                expanded["resolved_references"]=resolved
            sources[group]=expanded
            if group!="R928":
                transports[group]={"kind":"actual_completed_source_selected_members",
                    "source":{k:source[k] for k in BASE},"transport":archive.receipt()}
                continue
            transport=raw["completed_R928_input_transport"];package=plain(transport["package"])
            assert entries[package["file"]]==package
            assert expanded["files"][transport["source_inventory"]["file"]]==plain(transport["source_inventory"])
            inventory=read(bound(folder,transport["source_inventory"]))
            receipt=read(folder/transport["retained_receipt_file"])
            old=Source(group,expanded,retained);initial=old.raw("public-actions-input.json")
            assert inventory["result"]==receipt["result"]==source["result"]
            assert inventory["complete"] is True and receipt["complete"] is True
            assert inventory["sources"]==initial["job"]["sources"] and inventory["inputs"]==initial["job"]["inputs"]
            assert initial["source_inventory"]==plain(transport["source_inventory"])
            assert receipt["source_inventory"]==plain(transport["source_inventory"]) and receipt["source_bundle"]==package
            assert receipt["source_identities"]==old.tag["sources"]
            assert receipt["source_identities"]=={g:identity(s) for g,s in inventory["sources"].items()}
            nested={}
            for g in transport["nested_groups"]:
                selected=copy.deepcopy(raw["sources"][g]);original=inventory["sources"][g]
                same_source(selected,original)
                if selected["files"] is None:
                    assert not selected.get("required_references")
                    selected["files"]={n:plain(original["files"][n]) for n in selected["required_names"]}
                    for n,r in selected["pinned_files"].items():assert selected["files"][n]==plain(r)
                assert all(original["files"][n]==r for n,r in selected["files"].items())
                nested[g]=selected
            target=Path(work)/package["file"]
            if target.exists():assert spec(target)==package
            else:archive.extract_bound(package["file"],package["sha256"],target,package["bytes"])
            extracted=extract_nested_subset(target,retained,inventory["sources"],nested)
            sources.update(nested)
            transports[group]={"kind":"completed_original_R928_and_its_existing_input_carrier",
                "source":{k:source[k] for k in BASE},"package":package,
                "original_source_inventory":plain(transport["source_inventory"]),
                "transport":archive.receipt(),"nested_selection":extracted,
                "actual_completed_unit_reference_resolved":expanded["resolved_references"],
                "old_R885_R919_producer_archives_downloaded":False}
        finally:archive.close()
    assert set(sources)==set(GROUPS)
    return sources,transports

class InputReview:
    def __init__(self,item,retained):
        self.item=item;self.inputs=item["inputs"]
        self.sources={g:Source(g,item["sources"][g],retained) for g in GROUPS}
        for key in ("R_low_weight_polynomial","R_complete_identity","R_exact_expression",
                    "source_functions","correspondence_algebra","fibre_certificate","target_normal_index",
                    "full_target_equations","Euler_trace_row","full_eight_basis_identity",
                    "target_transport","target_quotient_derivative","target_g_h","target_frame_unit",
                    "exact_transport_DAG"):
            setattr(self,key,self.stage_ref(self.inputs[key]))
        self.divisors={label:{k:self.stage_ref(r) for k,r in self.inputs["divisors"][label].items()} for label in LABELS}
        self.validate_sources()

    def stage_ref(self,row):
        return self.sources[row["source_group"]].stage(row)

    def validate_sources(self):
        cr=self.sources["R922"].certificate;cy=self.sources["R926"].certificate
        cj=self.sources["R928"].certificate;cd=self.sources["R905"].certificate
        assert cr["actual_original_low_weight_R_mod_p_certified"] is True
        assert cr["actual_all_polynomial_RG_equal_Mg_entries_verified"] is True
        for field,key in (("polynomial_low_weight_R","R_low_weight_polynomial"),
                          ("complete_polynomial_identity","R_complete_identity"),
                          ("exact_original_trace_dual_expression","R_exact_expression")):
            assert plain(cr[field])==plain(self.inputs[key])
        R=self.R_low_weight_polynomial;proof=self.R_complete_identity
        assert R["prime"]==P and R["normal_basis_rank"]==272 and R["normal_basis_degrees"]==EPS
        assert R["coefficient_count"]==4 and len(R["coefficient_matrices_low_to_high"])==4
        for part in R["coefficient_matrices_low_to_high"]:shape(part,272,272)
        for field in ("negative_weight_bound_entries_are_zero","all_weighted_degree_zeros_verified",
                      "full_matrix_symmetry_verified","all_127_by127_weight_two_block_entries_zero"):
            assert R[field] is True
        assert plain(proof["source_R_polynomial"])==plain(self.inputs["R_low_weight_polynomial"])
        assert proof["whole_polynomial_R_times_G_equals_original_Mg_verified"] is True
        assert proof["all_eight_z_coefficients_checked"] is True
        assert proof["true_original_trace_dual_identified_by_nonzero_Gram"] is True
        assert self.R_exact_expression["exact_characteristic_zero_expression_defined"] is True
        assert self.R_exact_expression["normal_trace_dual"]["r_j"]=="g*beta_j_star"
        assert self.R_exact_expression["target_coordinate_reminder"]=="V=K(U)/P_U(U), eight K columns are numerators"
        assert cy["actual_seven_original_bounded_connection_numerators_certified"] is True
        assert cy["source_divisor_order"]==list(LABELS)
        assert cd["actual_seven_complete_full_principal_parts_solutions"] is True
        assert cd["actual_completed_source_connections"]==7
        same_source(self.sources["R926"].tag["sources"]["R905"],identity(self.item["sources"]["R905"]))
        old_r827=self.sources["R928"].tag["sources"]["R827"]
        same_source(self.sources["R922"].tag["sources"]["R827"],old_r827)
        same_source(self.sources["R905"].tag["sources"]["R827"],old_r827)
        for group in ("R922","R926","R928"):
            assert self.sources[group].tag["proofs"]["R922"]==self.item["proofs"]["R922"]
        for label in LABELS:
            refs=self.inputs["divisors"][label];data=self.divisors[label]
            assert set(refs)=={"certificate","denominator","numerator"}
            complete=data["certificate"];den=data["denominator"];num=data["numerator"]
            assert plain(cy["complete_bounded_connection_certificates"][label])==plain(refs["certificate"])
            assert plain(complete["source_original_connection"])==plain(cd["complete_source_connection_certificates"][label])
            for value in (complete,den,num):assert value["prime"]==P and value["label"]==label
            assert plain(complete["denominator"])==plain(refs["denominator"])
            assert plain(complete["bounded_numerator"])==plain(refs["numerator"])
            for flag in ("all277_coefficients_times272_rows_verified",
                         "full_original_F_transpose_times_y_equals_d_times_c_verified",
                         "all_original_numerator_degree_bounds_verified",
                         "original_543_gauge_and_full_logarithmic_principal_parts_preserved",
                         "whole_D_norm_all_length272_multiplicities_preserved"):
                assert complete[flag] is True
            assert complete["characteristic_zero_numerator_denominator_coordinates_expanded"] is False
            assert complete["exact_characteristic_zero_expression"]["alpha"]=="sum_i (y_i/d)*beta_i_trace_dual*dz"
            assert complete["exact_characteristic_zero_expression"]["proof"]==self.item["proofs"]["R922"]
            assert plain(num["source_denominator"])==plain(refs["denominator"])
            assert plain(num["source_original_connection"])==plain(complete["source_original_connection"])
            assert num["normal_basis_degrees"]==EPS and num["numerator_degree_bounds"]==[271+e for e in EPS]
            assert num["all_original_weighted_numerator_degree_bounds_verified"] is True
            shape(num["numerator_coefficients_in_z_low_to_high"],274,272)
            assert len(den["denominator_coefficients_in_z_low_to_high"])==273
            assert den["full_rank272_characteristic_polynomial_computed"] is True
            assert den["denominator_is_det_I_minus_tZ"] is True
            assert den["normalization_and_all_multiplicities_preserved"] is True
            assert den["nilpotent_zero_eigenparts_not_removed"] is True
            assert den["same_original_determinant_ratio_expression"]=="det(F(z))/det(F(a))"
        for flag in ("actual_eight_original_numerator_delta_K_values_certified",
                     "actual_full_quotient_derivative_identity_verified","actual_target_g_h_on_whole_E_computed",
                     "actual_whole_E_target_frame_unit_and_both_transport_identities_certified",
                     "original_V_equals_K_over_P_U_preserved","whole_source_factors_and_nilpotents_retained"):
            assert cj[flag] is True
        for field,key in (("target_differential_transport","target_transport"),
                          ("whole_quotient_derivative","target_quotient_derivative"),
                          ("whole_target_g_h","target_g_h"),
                          ("exact_characteristic_zero_expression_DAG","exact_transport_DAG")):
            assert plain(cj[field])==plain(self.inputs[key])
        j=self.target_transport;q=self.target_quotient_derivative;u=self.target_frame_unit
        assert j["both_complete2176_transport_identities_verified"] is True and j["whole_E_ell_unit_certified"] is True
        assert j["J_unit_not_claimed"] is True and j["J_inverse_computed"] is False
        assert plain(j["source_quotient_derivative"])==plain(self.inputs["target_quotient_derivative"])
        assert plain(j["source_target_g_h"])==plain(self.inputs["target_g_h"])
        assert plain(j["selected_whole_E_unit_trial"])==plain(self.inputs["target_frame_unit"])
        assert u["whole_E_unit"] is True and u["t"]==j["selected_t"]
        assert u["unit_certificate"]["whole_fibre_unit"] is True
        assert u["unit_certificate"]["complete2176_scalar_product_equals_one"] is True
        assert plain(u["source_target_g_h"])==plain(self.inputs["target_g_h"])
        assert q["complete_2176_coordinate_quotient_identity_verified"] is True
        assert q["original_V_definition"]=="K(U)/P_U(U)"
        assert q["quotient_identity_left"]==q["quotient_identity_right"]
        for key in ("J_over_E","J_g_target_over_E","J_h_target_over_E"):shape(j[key],8,272)
        for key in ("Delta_K_at_U","H_K_at_U","dotV_over_E"):shape(q[key],8,272)
        assert j["J_h_target_over_E"]==q["dotV_over_E"]
        assert self.exact_transport_DAG["canonical_dual7_transports_both_determinant_frames"] is True
        assert self.exact_transport_DAG["scalar7_diamond_original_minus3_descent_and_kappa_nu_retained"] is True
        oldjob=self.sources["R928"].raw("public-actions-input.json")["job"]
        for group in ("R885","R919"):
            same_source(self.sources["R928"].tag["sources"][group],identity(self.item["sources"][group]))
            for name,row in self.item["sources"][group]["files"].items():
                assert oldjob["sources"][group]["files"][name]==row
        for key in ("source_functions","correspondence_algebra","fibre_certificate","target_normal_index",
                    "full_target_equations","target_normal_blocks","Euler_trace_row","full_eight_basis_identity"):
            assert self.inputs[key]==oldjob["inputs"][key]
        s=self.source_functions;c=self.correspondence_algebra
        assert s["prime"]==P and s["source_node_ordinal"]==0 and s["source_node_value"]==0
        assert s["original82_scales_retained_once"] is True and s["new_scale_applied"]=="1"
        assert s["complete_fibre_factors_or_multiplicities_removed"] is False
        assert c["base_algebra_dimension"]==272 and c["correspondence_rank"]==8 and c["full_scalar_dimension"]==2176
        assert c["full_Pprime_times_target_w_equals_K_verified"] is True
        assert c["Pprime_unit_certificate"]["whole_fibre_unit"] is True
        assert c["leading_coefficient_unit_certificate"]["whole_fibre_unit"] is True
        assert plain(q["source_original_P_K_PU_inverse_V"])==plain(self.inputs["correspondence_algebra"])
        f=self.fibre_certificate
        assert f["whole_fibre_success"] is True and f["all272_original_target_normal_coordinates_certified"] is True
        for field,key in (("source_functions","source_functions"),("correspondence_algebra","correspondence_algebra"),
                          ("target_normal_row","target_normal_index"),("full_target_equations","full_target_equations")):
            assert plain(f[field])==plain(self.inputs[key])
        idx=self.target_normal_index
        assert idx["all272_target_normal_coordinates_computed"] is True and idx["target_gamma0_equals_one"] is True
        assert len(idx["blocks"])==len(self.inputs["target_normal_blocks"])==17
        for ordinal,(part,ref) in enumerate(zip(idx["blocks"],self.inputs["target_normal_blocks"])):
            assert part["normal_columns"]==[ordinal*16,(ordinal+1)*16]
            assert plain(part["source"])==plain(ref)
        assert self.full_target_equations["all272_original_target_equations_verified"] is True
        assert self.full_target_equations["all2176_scalar_coordinates_of_each_equation_checked"] is True
        row=self.Euler_trace_row;all8=self.full_eight_basis_identity
        assert row["input_frame"]=="dz_target" and row["output_frame"]=="nu_source"
        assert row["complete_rank8_and_all272_source_coordinates_preserved"] is True
        assert plain(row["source_original_correspondence"])==plain(self.inputs["correspondence_algebra"])
        assert plain(all8["source_Euler_row"])==plain(self.inputs["Euler_trace_row"])
        assert all8["all8_basis_identities_in_entire_A0_verified"] is True
        shape(row["linear_functional_coefficients_over_A"],8,272)

def source_review(item,retained):
    view=InputReview(item,retained)
    count=0
    for ref in item["inputs"]["target_normal_blocks"]:
        value=view.sources["R885"].stage(ref);first,stop=value["normal_columns"]
        assert first==count and stop==first+16 and len(value["normal_values_over_E"])==16
        for v in value["normal_values_over_E"]:shape(v,8,272)
        count=stop
    assert count==272
    for group,source in item["sources"].items():
        for key,selector in source.get("required_references",{}).items():
            parent=view.sources[group].stage(source["files"][selector["from_file"]])
            row=plain(parent[selector["field"]])
            assert source["resolved_references"][key]==row and source["files"][row["file"]]==row
    unit=view.target_frame_unit["unit_certificate"]
    assert unit["input"]==view.target_frame_unit["ell_over_E"]
    assert unit["base_dimension"]==272 and unit["extension_rank"]==8
    assert unit["division_free_Berkowitz_used"] is True
    assert unit["all8_Cayley_Hamilton_coordinates_verified"] is True
    assert unit["squarefree_factorization_or_geometric_point_selection_used"] is False
    assert unit["base_norm_unit_witness"]["whole_fibre_unit"] is True
    assert unit["base_norm_unit_witness"]["full_unreduced_polynomial_Bezout_identity_verified"] is True
    shape(unit["inverse"],8,272)
    assert isinstance(view.target_transport["selected_t"],int) and 0<=view.target_transport["selected_t"]<=2176
    return {"result":RESULT,"original_source_groups":list(GROUPS),"prime":P,
        "original_source_z":0,"whole_source_dimension":272,"whole_correspondence_dimension":2176,
        "completed_R922_R_coefficients":4,"completed_R926_connection_count":7,
        "completed_R928_selected_t":view.target_transport["selected_t"],
        "completed_target_normal_block_count":17,
        "original_R905_seven_gauges_and_source_identities_verified":True,
        "actual_R928_unit_reference_resolved_from_its_completed_transport":True,
        "original_R885_R919_bytes_from_R928_carrier_unchanged":True,
        "selected_file_counts":{g:len(item["sources"][g]["files"]) for g in GROUPS},
        "no_new_mathematics_in_wrapper":True}

def prepare(raw,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R930";retained.mkdir(parents=True,exist_ok=True)
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
    work=out.parent/"R930-source-transport";work.mkdir(parents=True,exist_ok=True)
    sources,transports=fetch_sources(raw,retained,work)
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
    print("R930_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
    return item,retained,review

def restore(raw,out):
    resume=raw.get("resume")
    if not resume:return
    assert resume["result"]==RESULT and resume["core_sha256"]==raw["core_sha256"]
    directory=out.parent/"R930-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R930-resume-archive",whole=False)
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
            assert core["helper_sha256"]==raw["helper_sha256"]
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
    assert cert["prime"]==P and cert["source_node"]==0 and cert["p"]==41
    assert cert["source_algebra_dimension"]==272 and cert["correspondence_rank"]==8 and cert["correspondence_scalar_dimension"]==2176
    assert cert["source_divisor_order"]==list(LABELS) and cert["actual_completed_connections"]==7
    assert cert["actual_all_seven_whole_target_connection_values_and_differential_traces_certified"] is True
    assert cert["all_original_factors_nilpotents_multiplicities_and_section_gauges_retained"] is True
    assert set(cert["complete_original_target_connection_certificates"])==set(LABELS)
    assert cert["nonunit_target_denominators"]=={} and cert["scope_stop_reason"] is None
    for flag in ("old_R_G_y_d_J_deltaK_deltaP_Gamma_or_inverses_recomputed",
                 "J_inverse_computed_or_J_unit_claimed","actual_characteristic_zero_connection_coordinates_expanded",
                 "five_Picard_sigma_cY_or_principal_function_combinations_computed",
                 "original_Hecke_projector_or_endpoint_calibration_computed",
                 "nonp_terms_Poincare_period_or_height_computed"):
        assert cert[flag] is False
    def get(row):return output_stage(out,entries,tag,row)
    audit=get(cert["source_audit"])
    assert audit["sources"]=={g:identity(item["sources"][g]) for g in GROUPS}
    assert audit["inputs"]==item["inputs"] and audit["prime"]==P and audit["source_node"]==0
    assert audit["seven_original_R905_gauges_and_complete_principal_parts_preserved"] is True
    assert audit["old_R_G_numerators_denominators_J_deltaK_deltaP_Gamma_or_inverses_recomputed"] is False
    trace=get(cert["complete_ordinary_trace_row"])
    assert trace["source_original_a8_PU_and_monic_relation"]==item["inputs"]["correspondence_algebra"]
    assert trace["basis_powers"]==list(range(8)) and len(trace["basis_checks"])==8
    shape(trace["linear_functional_coefficients_over_A"],8,272)
    assert trace["all8_full_multiplication_trace_identities_verified"] is True
    assert trace["whole_rank8_and_all272_source_factors_retained"] is True
    assert trace["old_a8_or_PU_inverse_recomputed"] is False
    for j,check in enumerate(trace["basis_checks"]):
        assert check["basis_power"]==j
        shape(check["multiplication_diagonal_over_A"],8,272)
        assert len(check["actual_trace_over_A"])==272
        assert check["actual_trace_over_A"]==check["Euler_coefficient_over_A"]==trace["linear_functional_coefficients_over_A"][j]
        assert check["all272_source_coordinates_verified"] is True
    factors=get(cert["complete_trace_transport_factors"])
    for field,key in (("source_completed_R928_transport","target_transport"),
                      ("source_completed_R928_quotient_data","target_quotient_derivative"),
                      ("source_completed_frame_inverse","target_frame_unit"),
                      ("source_original_PU_inverse","correspondence_algebra")):
        assert factors[field]==item["inputs"][key]
    shape(factors["coefficient_for_old_L_over_E"],8,272)
    shape(factors["coefficient_for_t_times_ordinary_trace_over_E"],8,272)
    assert factors["old_J_deltaK_deltaP_PU_inverse_or_frame_inverse_recomputed"] is False
    retained=out.parent/"retained-R930"
    old=Source("R928",item["sources"]["R928"],retained)
    oldtransport=old.stage(item["inputs"]["target_transport"])
    assert factors["selected_original_t"]==oldtransport["selected_t"]
    for label in LABELS:
        refs=item["inputs"]["divisors"][label]
        complete=get(cert["complete_original_target_connection_certificates"][label])
        assert complete["prime"]==P and complete["label"]==label
        for field,key in (("source_original_bounded_connection","certificate"),
                          ("source_original_bounded_numerator","numerator"),("source_original_denominator","denominator")):
            assert complete[field]==refs[key]
        assert complete["source_completed_original_J"]==item["inputs"]["target_transport"]
        assert complete["source_completed_old_L"]==item["inputs"]["Euler_trace_row"]
        assert complete["source_new_full_ordinary_trace_row"]==plain(cert["complete_ordinary_trace_row"])
        assert complete["source_trace_transport_factors"]==plain(cert["complete_trace_transport_factors"])
        den=get(complete["source_complete_whole_target_denominator_unit"])
        assert den["prime"]==P and den["label"]==label and den["whole_E_unit"] is True
        assert den["source_completed_original_denominator"]==refs["denominator"]
        assert den["source_original_correspondence"]==item["inputs"]["correspondence_algebra"]
        assert den["full_original_rank8_over_272_source_dimension"] is True
        assert den["factor_removal_or_cancellation_claimed"] is False and den["source_F0_unit_not_used_as_target_unit"] is True
        shape(den["d_target_over_E"],8,272)
        proof=den["unit_certificate"]
        assert proof["input"]==den["d_target_over_E"] and proof["whole_fibre_unit"] is True
        assert proof["base_dimension"]==272 and proof["extension_rank"]==8
        assert proof["division_free_Berkowitz_used"] is True and proof["all8_Cayley_Hamilton_coordinates_verified"] is True
        assert proof["squarefree_factorization_or_geometric_point_selection_used"] is False
        assert proof["complete2176_scalar_product_equals_one"] is True
        assert proof["base_norm_unit_witness"]["whole_fibre_unit"] is True
        assert proof["base_norm_unit_witness"]["full_unreduced_polynomial_Bezout_identity_verified"] is True
        shape(proof["inverse"],8,272)
        index=get(complete["source_complete_numerator_contraction_index"])
        assert index["prime"]==P and index["label"]==label and index["complete_coefficient_range"]==[0,277]
        assert index["source_original_bounded_numerator"]==refs["numerator"]
        assert index["source_completed_low_weight_R"]==item["inputs"]["R_low_weight_polynomial"]
        assert index["source_completed_all272_target_coordinates"]==item["inputs"]["target_normal_index"]
        assert index["all277_times272_product_coordinates_and_weights_verified"] is True
        assert index["zero_tail_degrees275_and276_certified"] is True
        assert len(index["blocks"])==18
        for j,part in enumerate(index["blocks"]):
            first=BLOCK*j;stop=min(first+BLOCK,277)
            assert (part["first"],part["stop"])==(first,stop)
            block=get(part["source"])
            assert block["prime"]==P and block["label"]==label and (block["first"],block["stop"])==(first,stop)
            assert block["source_original_bounded_numerator"]==refs["numerator"]
            assert block["source_completed_low_weight_R"]==item["inputs"]["R_low_weight_polynomial"]
            assert block["source_completed_all272_target_coordinates"]==item["inputs"]["target_normal_index"]
            assert block["normal_numerator_degree_bounds"]==[274-e for e in EPS]
            shape(block["normal_numerator_coefficients_mod_prime"],stop-first,272)
            assert len(block["target_normal_contracted_coefficients_over_E"])==stop-first
            for value in block["target_normal_contracted_coefficients_over_E"]:shape(value,8,272)
            for k,row in enumerate(block["normal_numerator_coefficients_mod_prime"],first):
                assert all(c==0 for j,c in enumerate(row) if k>274-EPS[j])
            assert block["all_original_weighted_product_degree_bounds_verified"] is True
            assert block["actual_z_coefficients_before_target_U_Horner"] is True
            assert block["old_R_y_or_target_normal_coordinates_recomputed"] is False
        previous=None;last=None
        for part in reversed(index["blocks"]):
            first,stop=part["first"],part["stop"]
            name=PREFIX+label+f"-U-Horner-{first:03d}-{stop:03d}.json.gz"
            row=entries[name];block=get(row)
            assert block["prime"]==P and block["label"]==label and (block["first"],block["stop"])==(first,stop)
            assert block["source_coefficient_block"]==plain(part["source"])
            assert block["previous_higher_degree_block"]==previous
            assert block["complete_rank8_U_Horner_without_point_specialization"] is True
            shape(block["accumulator_over_E"],8,272)
            previous=plain(row);last=block
        assert complete["source_complete_target_U_Horner"]==previous
        assert complete["numerator_target_over_E"]==last["accumulator_over_E"]==complete["denominator_times_B_D_over_E"]
        for field in ("numerator_target_over_E","B_D_target_over_E","denominator_times_B_D_over_E",
                      "B_D_times_J_over_E","input_to_original_L_over_E","input_to_new_T_over_E"):
            shape(complete[field],8,272)
        shape(complete["full_multiplication_diagonal_over_A"],8,272)
        for field in ("actual_complete_differential_trace_over_A","actual_direct_rank8_multiplication_trace_over_A",
                      "original_L_term_over_A","ordinary_T_term_before_multiply_t_over_A",
                      "actual_R922_quotient_transport_trace_over_A"):
            assert len(complete[field])==272
        assert complete["actual_complete_differential_trace_over_A"]==complete["actual_direct_rank8_multiplication_trace_over_A"]==complete["actual_R922_quotient_transport_trace_over_A"]
        assert complete["selected_original_frame_t"]==factors["selected_original_t"]
        for flag in ("all2176_target_connection_quotient_coordinates_verified",
                     "all272_trace_coordinates_verified_by_full_rank8_multiplication",
                     "all272_R922_quotient_transport_trace_coordinates_verified",
                     "original_R905_gauge_and_normalization_preserved",
                     "whole_source_and_target_factors_multiplicities_retained",
                     "canonical_dual7_frames_scalar7_diamond_and_minus3_transport_retained"):
            assert complete[flag] is True
        assert complete["direct_correspondence_direction"]=="Tr_pi_s(pi_t^*alpha_D)"
        assert complete["source_output_differential_frame"]=="nu_source"
        assert complete["original_target_rational_connection_section"]=="1 of O(H-D)"
        assert complete["original_target_principal_parts"]=="H-D"
        for flag in ("endpoint_kappa_nu_numerical_calibration_computed","five_Picard_sigma_cY_combinations_computed",
                     "characteristic_zero_connection_or_trace_coordinates_expanded","nonp_terms_Poincare_period_or_height_computed"):
            assert complete[flag] is False
    dag=get(cert["exact_original_target_connection_trace_DAG"])
    assert dag["source_R922_proof"]==item["proofs"]["R922"]
    assert dag["source_exact_original_R"]==item["inputs"]["R_exact_expression"]
    assert dag["source_exact_original_target_transport"]==item["inputs"]["exact_transport_DAG"]
    olddag=old.stage(item["inputs"]["exact_transport_DAG"])
    assert dag["original_rigidified_Hecke_transport"]==olddag["original_rigidified_Hecke_transport"]
    assert dag["original_cY_definition_retained_but_not_applied"]==olddag["original_cY"]
    assert set(dag["connections"])==set(LABELS)
    for label in LABELS:
        connection=dag["connections"][label]
        assert connection["source_completed_original_bounded_connection"]==item["inputs"]["divisors"][label]["certificate"]
        assert connection["target_B"]["required_unit"]=="whole d(U)"
        assert connection["differential_trace"]["direct_direction"]=="Tr_pi_s(pi_t^*alpha_D)"
        assert connection["canonical_dual7_transports_both_frames_to_frozen_Hecke_direction"] is True
    assert dag["exact_original_characteristic_zero_expressions_defined"] is True
    assert dag["all_original_section1_gauges_and_principal_parts_H_minus_D_preserved"] is True
    assert dag["scalar7_diamond_original_minus3_descent_and_kappa_nu_retained"] is True
    for flag in ("finite_fibre_values_substituted_for_global_functions","characteristic_zero_coordinates_expanded",
                 "five_Picard_sigma_cY_or_principal_function_combinations_computed",
                 "Hecke_calibration_nonp_terms_periods_or_height_computed"):
        assert dag[flag] is False

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
        assert core["helper_sha256"]==item["helper_sha256"]
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
        "actual_completed_connections":None if cert is None else cert.get("actual_completed_connections"),
        "actual_all_seven_whole_target_connection_values_and_differential_traces_certified":
            False if cert is None else cert.get("actual_all_seven_whole_target_connection_values_and_differential_traces_certified",False),
        "complete_ordinary_trace_row":None if cert is None else cert.get("complete_ordinary_trace_row"),
        "complete_trace_transport_factors":None if cert is None else cert.get("complete_trace_transport_factors"),
        "complete_original_target_connection_certificates":{} if cert is None else cert.get("complete_original_target_connection_certificates",{}),
        "nonunit_target_denominators":{} if cert is None else cert.get("nonunit_target_denominators",{}),
        "exact_original_target_connection_trace_DAG":None if cert is None else cert.get("exact_original_target_connection_trace_DAG"),
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
        print("R930_COMPLETE_IO_REVIEW="+json.dumps(result,sort_keys=True),flush=True)
        return 0 if result["complete"] else 1
    code=compute(raw,args.output,args.request)
    try:print("R930_COMPLETE_IO_REVIEW="+json.dumps(verify(raw,args.output),sort_keys=True),flush=True)
    except Exception:
        traceback.print_exc()
        if code==0:code=1
    return code
if __name__=="__main__":sys.exit(main())
