#!/usr/bin/env python3
"""R928 standard-library selected-source, retained-carrier and public Actions driver."""
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
RESULT="R928-original-whole-Artin-target-differential-transport"
FINAL="p41-original-whole-Artin-target-differential-transport-certificate.json"
PREFIX="R928-"
CORE="R928_original_whole_Artin_target_differential_transport.py"
REQUEST=TOPIC/"notes/R928-whole-Artin-target-differential-transport-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R928-retained-original-inputs.tar.gz"
INVENTORY="R928-original-source-inventory.json"
INPUT_RECEIPT="R928-retained-inputs-receipt.json"
EXPANDED="R928-expanded-job.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
GROUPS=("R919","R885","R827","R882","R873")
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
    "source_node_ordinal":0,"source_z":0,
    "source_algebra":"entire original Fp[X]/chi_0(X), dimension272",
    "correspondence":"entire A0[U]/(P(U)/a8), rank8",
    "original_target_w":"V=K(U)/P_U(U), K is the original numerator in columns9..16",
    "new_delta_K":"33 completed derivative blocks times the final8 original R882 columns",
    "derivative_block_size":64,"target_normal_block_size":16,
    "dotU":"completed R919 negative_deltaP_times_original_PU_inverse",
    "dotV":"old_PU_inverse*(deltaK+K_U*dotU-V*(deltaP_U+P_UU*dotU))",
    "target_g_h":"all272 original target normal coordinates contracted with original four coefficient vectors",
    "frame_trial_sequence":"integers0..2176 in this order; finite prefixes can be extended",
    "transport":"ell=g_target+t*h_target; J=(dotU+t*dotV)/ell",
    "acceptance":"ell whole-E unit and all2176 coordinates of J*g_target=dotU and J*h_target=dotV",
    "unit_algorithm":"division-free rank8 characteristic polynomial plus full A0 Bezout and E multiplication back",
    "J_inverse_or_J_unit_required":False,
    "old_2058_derivatives_nine_deltaP_dotU_a8_PU_or_Gamma_recomputed":False,
    "old_target_coordinates_Krylov_or_correspondence_recomputed":False,
    "delta_claimed_to_descend_to_source_fibre":False,
    "source_factors_nilpotents_or_multiplicities_discarded":False,
    "finite_values_claimed_char0_expanded_or_global_calibration":False,
    "budget_and_maximum_frame_trials_excluded_from_identity":True}

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
    description=importlib.util.spec_from_file_location("R928_frozen_stdlib_Range",path)
    IO=importlib.util.module_from_spec(description);description.loader.exec_module(IO)

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve() and item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False and 0<item["budget_minutes"]<=300
    assert 1<=item["maximum_frame_trials"]<=2177
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
        if group=="R919":
            assert source["files"] is None
            names=source["required_names"]
            assert all(n in names and plain(r)["file"]==n for n,r in source["pinned_files"].items())
        else:
            names=list(source["files"])
            assert all(plain(r)["file"]==n for n,r in source["files"].items())
        assert len(names)==len(set(names)) and MANIFEST in names and set(META).issubset(names)
        for name in names:assert Path(name).name==name and name not in ("",".","..") and "\\" not in name
    transport=item["completed_R919_input_transport"]
    assert transport["source_group"]=="R919"
    assert plain(transport["package"])["file"]=="R919-retained-original-inputs.tar.gz"
    assert transport["source_inventory"]["file"]=="R919-original-source-inventory.json"
    assert transport["retained_receipt_file"]=="R919-retained-inputs-receipt.json"
    load_io()

def request_contract(raw):
    return {"result":raw["result"],"p":raw["p"],"core_sha256":raw["core_sha256"],
        "method_sha256":raw["method_sha256"],"helper_sha256":raw["helper_sha256"],"proofs":raw["proofs"],
        "sources":raw["sources"],"input_bindings":raw["input_bindings"],
        "completed_R919_input_transport":raw["completed_R919_input_transport"],"strategy":STRATEGY}

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
        if group!="R919":
            assert actual==expected
            continue
        assert {k:v for k,v in actual.items() if k!="files"}=={k:v for k,v in expected.items() if k!="files"}
        assert set(actual["files"])==set(expected["required_names"])
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
    source=raw["sources"]["R919"];folder=Path(retained)/"R919";folder.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(source,Path(work)/"original-R919",whole=False)
    try:
        manifest=folder/MANIFEST
        if manifest.exists():assert sha(manifest)==source["manifest_sha256"] and manifest.stat().st_size==source["manifest_bytes"]
        else:archive.extract_bound(MANIFEST,source["manifest_sha256"],manifest,source["manifest_bytes"])
        expanded=selected_manifest(source,manifest);tasks=[]
        for name,row in expanded["files"].items():
            if (folder/name).exists():assert spec(folder/name)==row
            else:tasks.append((name,row["sha256"],folder/name,row["bytes"]))
        if tasks:archive.extract_many(tasks)
        transport=raw["completed_R919_input_transport"]
        package=plain(transport["package"])
        full=read(manifest);entries={r["file"]:plain(r) for r in full["files"]}
        assert entries[package["file"]]==package
        assert expanded["files"][transport["source_inventory"]["file"]]==plain(transport["source_inventory"])
        inventory=read(bound(folder,transport["source_inventory"]))
        receipt=read(folder/transport["retained_receipt_file"])
        old=Source("R919",expanded,retained);initial=old.raw("public-actions-input.json")
        assert inventory["result"]==receipt["result"]==source["result"]
        assert inventory["complete"] is True and receipt["complete"] is True
        assert inventory["sources"]==initial["job"]["sources"] and inventory["inputs"]==initial["job"]["inputs"]
        assert initial["source_inventory"]==plain(transport["source_inventory"])
        assert receipt["source_inventory"]==plain(transport["source_inventory"]) and receipt["source_bundle"]==package
        assert receipt["source_identities"]==old.tag["sources"]
        assert receipt["source_identities"]=={g:identity(s) for g,s in inventory["sources"].items()}
        nested={g:raw["sources"][g] for g in GROUPS if g!="R919"}
        for group,selected in nested.items():
            same_source(selected,inventory["sources"][group])
            assert all(inventory["sources"][group]["files"][name]==row for name,row in selected["files"].items())
        target=Path(work)/package["file"]
        if target.exists():assert spec(target)==package
        else:archive.extract_bound(package["file"],package["sha256"],target,package["bytes"])
        extracted=extract_nested_subset(target,retained,inventory["sources"],nested)
        sources={"R919":expanded,**copy.deepcopy(nested)}
        return sources,{"R919":{"kind":"completed_original_R919_and_its_existing_input_carrier",
            "source":{k:source[k] for k in BASE},"package":package,
            "original_source_inventory":plain(transport["source_inventory"]),
            "transport":archive.receipt(),"nested_selection":extracted,
            "old_large_producer_archives_downloaded":False}}
    finally:archive.close()

class InputReview:
    def __init__(self,item,retained):
        self.item=item;self.inputs=item["inputs"]
        self.sources={g:Source(g,item["sources"][g],retained) for g in GROUPS}
        for key in ("source_functions","correspondence_algebra","fibre_certificate","target_normal_index",
                    "full_target_equations","original_W","original_place","seventeen_coordinates",
                    "same_place_interface","correspondence_DAG","basis_derivative_index",
                    "source_leaf_derivatives","nine_delta_P_coefficients","Euler_trace_row",
                    "full_eight_basis_identity","completed_dotU","exact_R919_DAG"):
            row=self.inputs[key];setattr(self,key,self.sources[row["source_group"]].stage(row))
        self.validate_sources()

    def validate_sources(self):
        old=self.sources["R919"];cert=old.certificate
        assert cert["actual_auxiliary_prime"]==P and cert["original_source_node"]==0
        assert cert["source_algebra_dimension"]==272 and cert["correspondence_rank"]==8
        assert cert["correspondence_scalar_dimension"]==2176
        for flag in ("actual_nine_original_delta_P_values_certified",
                     "actual_complete_A0_linear_Euler_row_certified","actual_all8_trace_basis_identities_verified",
                     "actual_all272_target_normal_differential_traces_computed","whole_source_factors_and_nilpotents_retained"):
            assert cert[flag] is True
        for field in ("basis_derivative_index","source_leaf_derivatives","nine_delta_P_coefficients",
                      "Euler_trace_row","full_eight_basis_identity"):
            assert plain(cert[field])==plain(self.inputs[field])
        assert plain(cert["exact_characteristic_zero_expression_DAG"])==plain(self.inputs["exact_R919_DAG"])
        oldjob=old.raw("public-actions-input.json")["job"]
        assert oldjob["core_sha256"]==old.item["core_sha256"]
        for group in GROUPS:
            if group=="R919":continue
            same_source(old.tag["sources"][group],identity(self.item["sources"][group]))
            same_source(oldjob["sources"][group],self.item["sources"][group])
            for name,row in self.item["sources"][group]["files"].items():
                assert oldjob["sources"][group]["files"][name]==row,(group,name)
        for key in ("source_functions","correspondence_algebra","fibre_certificate","target_normal_index",
                    "full_target_equations","original_W","original_place","seventeen_coordinates",
                    "same_place_interface","correspondence_DAG","target_normal_blocks"):
            assert self.inputs[key]==oldjob["inputs"][key],key
        s=self.source_functions;c=self.correspondence_algebra;f=self.fibre_certificate
        assert s["source_node_ordinal"]==0 and s["source_node_value"]==0 and s["prime"]==P
        assert s["source_algebra_dimension"]==272 and s["all2058_functions_consumed"] is True
        assert s["original82_scales_retained_once"] is True and s["new_scale_applied"]=="1"
        assert s["column_order"]=="P0..P8,K0..K7" and s["complete_fibre_factors_or_multiplicities_removed"] is False
        shape(s["seventeen_values_over_A"],17,272)
        assert plain(s["source_seventeen_coordinates"])==plain(self.inputs["seventeen_coordinates"])
        assert plain(s["source_DAG"])==plain(self.inputs["correspondence_DAG"])
        assert c["original_P_coefficients"]==s["seventeen_values_over_A"][:9]
        assert c["original_K_coefficients"]==s["seventeen_values_over_A"][9:]
        assert c["base_algebra_dimension"]==272 and c["correspondence_rank"]==8 and c["full_scalar_dimension"]==2176
        assert c["full_Pprime_times_target_w_equals_K_verified"] is True
        assert c["any_source_factor_or_multiplicity_discarded"] is False
        assert c["leading_coefficient_unit_certificate"]["whole_fibre_unit"] is True
        assert c["Pprime_unit_certificate"]["whole_fibre_unit"] is True
        assert plain(c["source_functions"])==plain(self.inputs["source_functions"])
        shape(c["Pprime_at_U"],8,272);shape(c["target_w"],8,272)
        assert f["whole_fibre_success"] is True and f["all_required_units_on_entire_algebras_verified"] is True
        assert f["all272_original_target_normal_coordinates_certified"] is True
        for field,key in (("source_functions","source_functions"),("correspondence_algebra","correspondence_algebra"),
                          ("target_normal_row","target_normal_index"),("full_target_equations","full_target_equations")):
            assert plain(f[field])==plain(self.inputs[key])
        idx=self.target_normal_index
        assert idx["all272_target_normal_coordinates_computed"] is True and idx["target_gamma0_equals_one"] is True
        assert len(idx["blocks"])==len(self.inputs["target_normal_blocks"])==17
        for ordinal,(part,ref) in enumerate(zip(idx["blocks"],self.inputs["target_normal_blocks"])):
            assert part["normal_columns"]==[16*ordinal,min(16*ordinal+16,272)]
            assert plain(part["source"])==plain(ref)
        assert self.full_target_equations["all272_original_target_equations_verified"] is True
        assert self.full_target_equations["all2176_scalar_coordinates_of_each_equation_checked"] is True
        assert self.full_target_equations["no_factor_or_nilpotent_component_discarded"] is True
        place=self.original_place
        assert place["prime"]==P and place["original_zeta_root"]==549966761 and place["original_s_root"]==99932770
        assert place["original_integral_B_root"]==3197390 and place["original_branch"]==0
        assert self.original_W["prime"]==P and self.original_W["original_rational_denominators_all_units"] is True
        for field in ("g_vector_coefficients_mod_prime","h_vector_coefficients_mod_prime"):
            shape(self.original_W[field],4,272)
        cc=self.seventeen_coordinates
        assert cc["prime"]==P and cc["same_characteristic_zero_coefficients_integral_at_new_place"] is True
        shape(cc["coordinate_matrix_mod_prime"],2058,17)
        dag=self.correspondence_DAG
        assert plain(cc["source_exact_R873_unit_solve"])==plain(dag["coefficient_unit_solve"])
        assert self.same_place_interface["all2200_by17_original_equations_verified"] is True
        assert self.same_place_interface["prime"]==P and self.same_place_interface["original_zeta_root"]==549966761
        assert plain(self.same_place_interface["new_modular_coordinates"])==plain(self.inputs["seventeen_coordinates"])
        assert plain(self.same_place_interface["source_R873_correspondence_DAG"])==plain(self.inputs["correspondence_DAG"])
        assert dag["exact_original_correspondence_expression_certified"] is True
        assert dag["rigidified_Hecke_transport"]["frozen_direction"]=="Nm_pi_t(pi_s^*I)"
        assert dag["P_over_tau8_coefficients"]=={"powers_U":list(range(9)),"unit_solve_columns":list(range(9))}
        ix=self.basis_derivative_index
        assert ix["basis_dimension"]==2058 and ix["all2058_original_basis_derivatives_evaluated"] is True
        assert plain(ix["source_original_DAG"])==plain(self.inputs["correspondence_DAG"])
        expected=[(i,min(i+64,2058)) for i in range(0,2058,64)]
        assert [(p["first"],p["stop"]) for p in ix["blocks"]]==expected
        assert len(self.inputs["basis_derivative_blocks"])==33
        for part,ref in zip(ix["blocks"],self.inputs["basis_derivative_blocks"]):
            assert plain(part["source"])==plain(ref)
        leaf=self.source_leaf_derivatives
        assert leaf["derivation_applied_before_fibre_reduction"] is True and leaf["delta_claimed_to_descend_to_A0"] is False
        assert leaf["old_source_values_or_inverse_recomputed"] is False
        assert plain(leaf["source_DAG"])==plain(self.inputs["correspondence_DAG"])
        dp=self.nine_delta_P_coefficients
        assert plain(dp["source_basis_derivatives"])==plain(self.inputs["basis_derivative_index"])
        assert plain(dp["source_original_seventeen_coordinates"])==plain(self.inputs["seventeen_coordinates"])
        assert dp["coefficient_indices"]==list(range(9))
        shape(dp["delta_P_coefficients_over_A"],9,272)
        assert dp["all2058_rows_and_nine_original_P_columns_consumed"] is True
        assert dp["delta_K_or_new_coefficient_solve_computed"] is False
        row=self.Euler_trace_row
        assert plain(row["source_original_correspondence"])==plain(self.inputs["correspondence_algebra"])
        assert plain(row["source_nine_delta_P_coefficients"])==plain(self.inputs["nine_delta_P_coefficients"])
        assert row["input_frame"]=="dz_target" and row["output_frame"]=="nu_source"
        assert row["a8_inverse_reused_from_original_complete_certificate"] is True
        tr=self.full_eight_basis_identity
        assert tr["all8_basis_identities_in_entire_A0_verified"] is True
        assert plain(tr["source_Euler_row"])==plain(self.inputs["Euler_trace_row"])
        assert plain(tr["basis_certificates"][0])==plain(self.inputs["completed_dotU"])
        du=self.completed_dotU
        assert du["basis_U_power"]==0
        assert plain(du["source_Euler_row"])==plain(self.inputs["Euler_trace_row"])
        assert plain(du["source_original_Pprime_inverse"])==plain(self.inputs["correspondence_algebra"])
        assert du["complete_all272_coordinate_equality_verified"] is True and du["new_inverse_computed"] is False
        shape(du["negative_h_deltaP_over_Pprime_in_E"],8,272)
        assert self.exact_R919_DAG["exact_characteristic_zero_expression_defined"] is True
        assert self.exact_R919_DAG["finite_fibre_values_substituted_for_global_functions"] is False
        assert self.exact_R919_DAG["original_rigidified_Hecke_transport"]==dag["rigidified_Hecke_transport"]

def source_review(item,retained):
    view=InputReview(item,retained)
    for part,ref in zip(view.basis_derivative_index["blocks"],item["inputs"]["basis_derivative_blocks"]):
        value=view.sources["R919"].stage(ref)
        first,stop=part["first"],part["stop"]
        assert (value["first"],value["stop"])==(first,stop)
        shape(value["delta_basis_values_over_A"],stop-first,272)
        assert plain(value["source_new_leaf_derivatives"])==plain(item["inputs"]["source_leaf_derivatives"])
        assert plain(value["source_original_DAG"])==plain(item["inputs"]["correspondence_DAG"])
        assert plain(value["source_original_values"])==plain(item["inputs"]["source_functions"])
        assert value["product_and_quotient_rules_include_all_original_factors"] is True
        assert value["old_complete_V8_values_recomputed"] is False and value["old_input_scales_changed"] is False
    for ref in item["inputs"]["target_normal_blocks"]:
        value=view.sources["R885"].stage(ref);first,stop=value["normal_columns"]
        assert len(value["normal_values_over_E"])==stop-first
        for v in value["normal_values_over_E"]:shape(v,8,272)
    return {"result":RESULT,"original_source_groups":list(GROUPS),"prime":P,
        "original_source_z":0,"whole_source_dimension":272,"whole_correspondence_dimension":2176,
        "completed_derivative_block_count":33,"completed_target_normal_block_count":17,
        "original_R919_nine_deltaP_dotU_and_original_PU_inverse_present":True,
        "original_R873_K_numerator_column_identity_retained":True,
        "historical_R827_source_schema_exactly_preserved":True,
        "selected_file_counts":{g:len(item["sources"][g]["files"]) for g in GROUPS},
        "no_new_mathematics_in_wrapper":True}

def prepare(raw,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R928";retained.mkdir(parents=True,exist_ok=True)
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
    work=out.parent/"R928-source-transport";work.mkdir(parents=True,exist_ok=True)
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
    print("R928_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
    return item,retained,review

def restore(raw,out):
    resume=raw.get("resume")
    if not resume:return
    assert resume["result"]==RESULT and resume["core_sha256"]==raw["core_sha256"]
    directory=out.parent/"R928-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R928-resume-archive",whole=False)
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
    assert cert["actual_auxiliary_prime"]==P and cert["original_source_node"]==0
    assert cert["source_algebra_dimension"]==272 and cert["correspondence_rank"]==8 and cert["correspondence_scalar_dimension"]==2176
    for key in ("actual_eight_original_numerator_delta_K_values_certified",
                "actual_full_quotient_derivative_identity_verified","actual_target_g_h_on_whole_E_computed",
                "actual_whole_E_target_frame_unit_and_both_transport_identities_certified",
                "original_V_equals_K_over_P_U_preserved","whole_source_factors_and_nilpotents_retained","J_unit_not_claimed"):
        assert cert[key] is True
    for key in ("J_inverse_computed","old_2058_derivatives_nine_deltaP_dotU_a8_PU_Gamma_or_target_coordinates_recomputed",
                "actual_characteristic_zero_derivative_coordinates_expanded","actual_original_Gamma_characteristic_zero_expanded",
                "seven_connection_numerator_evaluations_computed","original_Hecke_projector_or_endpoint_calibration_computed",
                "nonp_terms_Poincare_period_or_height_computed"):
        assert cert[key] is False
    names=("source_audit","eight_delta_K_coefficients","whole_quotient_derivative","whole_target_g_h",
           "target_differential_transport","exact_characteristic_zero_expression_DAG")
    refs={key:plain(cert[key]) for key in names}
    values={key:output_stage(out,entries,tag,row) for key,row in refs.items()}
    audit=values["source_audit"]
    assert audit["sources"]=={g:identity(item["sources"][g]) for g in GROUPS} and audit["inputs"]==item["inputs"]
    assert audit["old_33_derivative_blocks_nine_deltaP_dotU_a8_PU_and_target_coordinates_reused"] is True
    dk=values["eight_delta_K_coefficients"]
    shape(dk["delta_K_coefficients_over_A"],8,272)
    assert dk["source_basis_derivatives"]==item["inputs"]["basis_derivative_index"]
    assert dk["source_original_seventeen_coordinates"]==item["inputs"]["seventeen_coordinates"]
    assert dk["original_coordinate_columns"]==list(range(9,17)) and dk["numerator_powers_U"]==list(range(8))
    assert dk["all2058_rows_and_original_eight_numerator_columns_consumed"] is True
    assert dk["original_K_is_numerator_not_target_w"] is True
    assert dk["old_2058_derivatives_and_nine_deltaP_recomputed"] is False
    assert len(dk["completed_contractions"])==33
    for j,(ref,oldref) in enumerate(zip(dk["completed_contractions"],item["inputs"]["basis_derivative_blocks"])):
        part=output_stage(out,entries,tag,ref);first=64*j;stop=min(first+64,2058)
        assert (part["first"],part["stop"])==(first,stop)
        assert part["source_completed_basis_derivative_block"]==oldref
        assert part["source_original_seventeen_coordinates"]==item["inputs"]["seventeen_coordinates"]
        shape(part["contributions_to_eight_delta_K_over_A"],8,272)
        assert part["original_coordinate_columns"]==list(range(9,17))
        assert part["old_basis_function_derivatives_recomputed"] is False and part["old_nine_delta_P_recomputed"] is False
    quotient=values["whole_quotient_derivative"]
    assert quotient["source_new_eight_delta_K"]==refs["eight_delta_K_coefficients"]
    assert quotient["source_completed_nine_delta_P"]==item["inputs"]["nine_delta_P_coefficients"]
    assert quotient["source_completed_dotU"]==item["inputs"]["completed_dotU"]
    assert quotient["source_original_P_K_PU_inverse_V"]==item["inputs"]["correspondence_algebra"]
    for key in ("delta_K_at_U","K_U_at_U","delta_P_U_at_U","P_UU_at_U","Delta_K_at_U","H_K_at_U",
                "dotV_over_E","quotient_identity_left","quotient_identity_right"):
        shape(quotient[key],8,272)
    assert quotient["quotient_identity_left"]==quotient["quotient_identity_right"]
    assert quotient["complete_2176_coordinate_quotient_identity_verified"] is True
    assert quotient["original_V_definition"]=="K(U)/P_U(U)"
    assert quotient["derivative_before_specialization"] is True and quotient["delta_claimed_to_descend_to_A0"] is False
    assert quotient["old_PU_inverse_dotU_nine_deltaP_or_Gamma_recomputed"] is False
    gh=values["whole_target_g_h"]
    assert gh["source_original_W_g_h"]==item["inputs"]["original_W"]
    assert gh["source_all272_target_normal_index"]==item["inputs"]["target_normal_index"]
    assert gh["source_original_full_target_equations"]==item["inputs"]["full_target_equations"]
    shape(gh["g_target_over_E"],8,272);shape(gh["h_target_over_E"],8,272)
    assert gh["original_normal_coefficient_powers"]==[0,1,2,3] and len(gh["completed_contractions"])==17
    for flag in ("all272_original_target_normal_coordinates_consumed","complete_rank8_over_entire_A0_preserved",
                 "target_functions_not_source_z0_specializations"):assert gh[flag] is True
    assert gh["old_target_normal_or_Gamma_recomputed"] is False
    for j,(ref,oldref) in enumerate(zip(gh["completed_contractions"],item["inputs"]["target_normal_blocks"])):
        part=output_stage(out,entries,tag,ref)
        assert part["normal_columns"]==[16*j,16*j+16]
        assert part["source_original_target_normal_block"]==oldref
        assert part["source_original_W_g_h"]==item["inputs"]["original_W"]
        for field in ("four_g_coefficient_contributions_over_E","four_h_coefficient_contributions_over_E"):
            assert len(part[field])==4
            for value in part[field]:shape(value,8,272)
        assert part["target_functions_not_source_z0_specializations"] is True
        assert part["original_target_normal_coordinates_recomputed"] is False
    transport=values["target_differential_transport"]
    t=transport["selected_t"];assert isinstance(t,int) and 0<=t<2177
    assert len(transport["trials_in_original_integer_order"])==t+1
    for j,ref in enumerate(transport["trials_in_original_integer_order"]):
        trial=output_stage(out,entries,tag,ref)
        assert trial["t"]==j and trial["source_target_g_h"]==refs["whole_target_g_h"]
        assert trial["whole_E_unit"] is (j==t)
        assert trial["complete_original_2176_dimensional_algebra_preserved"] is True
        assert trial["factors_or_nilpotents_removed"] is False
        shape(trial["ell_over_E"],8,272)
        proof=trial["unit_certificate"]
        assert proof["input"]==trial["ell_over_E"] and proof["whole_fibre_unit"] is trial["whole_E_unit"]
        assert proof["base_dimension"]==272 and proof["extension_rank"]==8
        assert proof["division_free_Berkowitz_used"] is True and proof["all8_Cayley_Hamilton_coordinates_verified"] is True
        assert proof["squarefree_factorization_or_geometric_point_selection_used"] is False
        if j==t:
            assert transport["selected_whole_E_unit_trial"]==plain(ref)
            shape(proof["inverse"],8,272)
            assert proof["complete2176_scalar_product_equals_one"] is True
            assert proof["base_norm_unit_witness"]["whole_fibre_unit"] is True
            assert proof["base_norm_unit_witness"]["full_unreduced_polynomial_Bezout_identity_verified"] is True
    assert transport["source_quotient_derivative"]==refs["whole_quotient_derivative"]
    assert transport["source_target_g_h"]==refs["whole_target_g_h"]
    assert transport["source_completed_dotU"]==item["inputs"]["completed_dotU"]
    for key in ("J_over_E","J_g_target_over_E","J_h_target_over_E"):shape(transport[key],8,272)
    retained=out.parent/"retained-R928";old=Source("R919",item["sources"]["R919"],retained)
    du=old.stage(item["inputs"]["completed_dotU"])
    assert transport["J_g_target_over_E"]==du["negative_h_deltaP_over_Pprime_in_E"]
    assert transport["J_h_target_over_E"]==quotient["dotV_over_E"]
    assert transport["both_complete2176_transport_identities_verified"] is True
    assert transport["whole_E_ell_unit_certified"] is True
    assert transport["source_differential_frame"]=="nu_source" and transport["target_differential_frame"]=="nu_target"
    assert transport["J_inverse_computed"] is False and transport["J_unit_not_claimed"] is True
    assert transport["canonical_dual7_scalar7_diamond_and_original_minus3_descent_preserved"] is True
    assert transport["kappa_nu_endpoint_constants_replaced_or_evaluated"] is False
    dag=values["exact_characteristic_zero_expression_DAG"]
    assert dag["source_R922_proof"]==item["proofs"]["R922"]
    assert dag["source_original_correspondence_DAG"]==item["inputs"]["correspondence_DAG"]
    assert len(dag["eight_numerator_derivative_nodes"])==8
    assert dag["target_w"]["numerator"]=="K(U)" and dag["target_w"]["denominator"]=="P_U(U)"
    assert dag["exact_original_characteristic_zero_expression_defined"] is True
    assert dag["canonical_dual7_transports_both_determinant_frames"] is True
    assert dag["scalar7_diamond_original_minus3_descent_and_kappa_nu_retained"] is True
    assert dag["actual_characteristic_zero_derivative_coordinates_expanded"] is False
    assert dag["finite_fibre_values_substituted_for_global_functions"] is False
    assert dag["seven_connections_Hecke_calibration_nonp_period_or_height_computed"] is False

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
        "eight_delta_K_coefficients":None if cert is None else cert.get("eight_delta_K_coefficients"),
        "whole_quotient_derivative":None if cert is None else cert.get("whole_quotient_derivative"),
        "whole_target_g_h":None if cert is None else cert.get("whole_target_g_h"),
        "target_differential_transport":None if cert is None else cert.get("target_differential_transport"),
        "exact_characteristic_zero_expression_DAG":None if cert is None else cert.get("exact_characteristic_zero_expression_DAG"),
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
        print("R928_COMPLETE_IO_REVIEW="+json.dumps(result,sort_keys=True),flush=True)
        return 0 if result["complete"] else 1
    code=compute(raw,args.output,args.request)
    try:print("R928_COMPLETE_IO_REVIEW="+json.dumps(verify(raw,args.output),sort_keys=True),flush=True)
    except Exception:
        traceback.print_exc()
        if code==0:code=1
    return code
if __name__=="__main__":sys.exit(main())
