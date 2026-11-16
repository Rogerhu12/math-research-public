#!/usr/bin/env python3
"""R900 source-preserving standard-library transport and structural verification.
No mathematical core is imported by this public wrapper.
"""
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
import traceback

S=Path(__file__).resolve().parent
TOPIC=S.parent
REPO=TOPIC.parent.parent
REPOSITORY="Rogerhu12/math-research-public"
RESULT="R900-original-K-defined-degree272-representative"
FINAL="p41-original-K-defined-degree272-representative-certificate.json"
PREFIX="R900-"
CORE="R900_original_K_defined_degree272_representative.py"
REQUEST=TOPIC/"notes/R900-K-defined-degree272-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R900-retained-original-inputs.tar.gz"
INVENTORY="R900-original-source-inventory.json"
INPUT_RECEIPT="R900-retained-inputs-receipt.json"
EXPANDED="R900-expanded-job.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
MANDATORY=("R899","R894","R883","R827","R890")
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
IO=None

STRATEGY={
    "original_curve":"original genus127 Y, level82 and original minus3 descent",
    "ground_field":"original K=Q(zeta), not an auxiliary residue field",
    "prime":P,"original_branch":0,"original_integral_B_root":3197390,
    "original_s_root":99932770,"original_zeta_root":549966761,
    "normal_basis_degrees":EPS,"normal_V3_dimension":690,
    "input_K_fixed_functions":"S_i=original_QN*w_i; w_i are the already tau-normalized normal V3 functions",
    "input_normal_space_shape":[690,418],
    "first_anchor":"first unscaled original R899 column with unit pole-leading coefficient at P0",
    "second_anchor":"sum(c^i*S_i), exact positive integer c=1,2,...; same coefficients on w_i",
    "shared_QN_cancellation":"S0*r+S1*s=QN*(w0*r+w1*s); all normal V3 functions are already tau-normalized",
    "first_original_product_shape":[1904,1380],"first_product_rank":1234,
    "first_common_divisor_degree":272,"D0_degree":544,
    "complete_H0_3H_minus_D0_dimension":146,
    "first_kernel_projection":"second690 original V3 rows",
    "v_selection":"first unchanged canonical146 column with unit value at original P0",
    "second_pencil":"sum(c^i*U_i), exact positive integer c=1,2,...",
    "second_original_product_shape":[1904,1380],"second_product_rank":962,
    "DK_degree":272,"complete_H0_3H_minus_DK_dimension":418,
    "whole_source_fibres":[0,1,2,3,4,5,6],
    "whole_fibre_length":1904,"degree6H":1632,
    "whole_artin_factors_or_multiplicities_removed":False,
    "canonical_K_descent":"K-stable relation space plus free-coordinate identity; no new Galois sampling",
    "principal_QK":"QN*w0/v; w0 and v are already tau-normalized, with no additional tau power",
    "class_identity":"T0=(DK-H)+div(QK)",
    "original_QN_rho_order":-8435,"QK_rho_order":-8435,
    "QK_rho_leading":"original_LC_QN*w0(P0)/v(P0)",
    "QK_t_leading":"QK_rho_leading*original_c^8435",
    "old_16_flips_QN_K_basis_Krylov_normal_evaluations_and_point_jets_recomputed":False,
    "fixed_anchor_products_shared_across_trials":True,
    "normal_integer_scale_applied_again":False,
    "characteristic_zero_coordinates_reconstructed":False,
    "nonp_Hecke_support_Picard_principality_connection_period_or_height_computed":False,
    "only_budget_and_two_positive_integer_trial_limits_excluded_from_identity":True,
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
    temporary=path.with_name(path.name+".tmp")
    temporary.write_text(json.dumps(value,sort_keys=True,separators=(",",":"),
                                    ensure_ascii=False)+"\n",encoding="utf-8")
    temporary.replace(path)

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
    assert spec(path)==row,("bound_file",row["file"])
    return path

def topic_path(name):
    p=PurePosixPath(name)
    assert not p.is_absolute() and ".." not in p.parts
    path=(TOPIC/str(p)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path

def identity(source):
    answer={**{k:source[k] for k in BASE},"configuration_sha256":source["configuration_sha256"],
            "selected_files_sha256":fingerprint(source["files"])}
    if source.get("certificate") is not None:
        answer["certificate"]=plain(source["certificate"])
    else:
        answer["configuration_stage"]=plain(source["configuration_stage"])
        answer["accepted_process_exit_codes"]=source["accepted_process_exit_codes"]
    return answer

def group_ref(group,row):
    return {"source_group":group,**plain(row)}

def same_source(left,right):
    assert all(str(left[k])==str(right[k]) for k in BASE)
    if left.get("configuration_sha256") is not None:
        assert left["configuration_sha256"]==right["configuration_sha256"]

def expected_tag(item,sources,inputs):
    return {"result":RESULT,"source_sha256":item["core_sha256"],
            "python_flint":"0.9.0","p":41,"method_sha256":item["method_sha256"],
            "proofs":item["proofs"],"sources":{g:identity(sources[g]) for g in sorted(sources)},
            "inputs":inputs,"strategy":STRATEGY}

def load_io():
    global IO
    path=S/RANGE_FILE
    assert sha(path)==RANGE_SHA
    d=importlib.util.spec_from_file_location("R900_frozen_stdlib_Range",path)
    IO=importlib.util.module_from_spec(d);d.loader.exec_module(IO)

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve()
    assert item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False
    assert item["core"]==CORE and sha(S/CORE)==item["core_sha256"]
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["io_helper"]==RANGE_FILE and item["io_helper_sha256"]==RANGE_SHA
    assert 0<item["budget_minutes"]<=300
    assert 1<=item["maximum_first_pencil_trials"]<P
    assert 1<=item["maximum_second_pencil_trials"]<P
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert set(item["source_artifacts"])==set(MANDATORY)
    assert all(item["source_artifacts"][g] is not None for g in MANDATORY)
    load_io()

def entry_map(folder,source):
    path=Path(folder)/MANIFEST
    assert sha(path)==source["manifest_sha256"]
    if source.get("manifest_bytes") is not None:
        assert path.stat().st_size==source["manifest_bytes"]
    value=read(path)
    assert value["result"]==source["result"]
    entries={r["file"]:plain(r) for r in value["files"]}
    assert len(entries)==len(value["files"])
    if source.get("manifest_file_count") is not None:
        assert len(entries)==source["manifest_file_count"]
    entries[MANIFEST]=spec(path)
    return entries

def metadata(group,folder,source,entries):
    initial,run,core=[read(bound(folder,entries[name])) for name in META]
    assert initial["source_commit"]==run["source_commit"]==source["source_commit"]
    assert str(run["workflow_run_id"])==str(source["run_id"])
    original_core=initial.get("core_sha256",initial.get("job",{}).get("core_sha256"))
    assert original_core==core["source_sha256"]==source["core_sha256"]
    if source.get("wrapper_sha256") is not None:
        actual=initial.get("wrapper_sha256",initial.get("driver_sha256"))
        assert actual==source["wrapper_sha256"]
    assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
    if source.get("certificate") is not None:
        assert run["complete"] is True and core["complete"] is True
        assert run["process_exit_code"]==0
        for key in ("process_exit_code","exit_code"):
            if key in core:
                assert core[key]==0
        certspec=plain(source["certificate"])
        assert entries[certspec["file"]]==certspec
        certificate=read(bound(folder,certspec))
        assert certificate["result"]==source["result"] and certificate["complete"] is True
        assert core["certificate_sha256"]==certspec["sha256"]
        tag=certificate["configuration"]
    else:
        assert run["complete"] is False and core["complete"] is False
        assert run["process_exit_code"] in source["accepted_process_exit_codes"]
        certificate=None
        anchor=read(bound(folder,source["configuration_stage"]))
        assert anchor["complete"] is True
        tag=anchor["configuration"]
    assert tag.get("source_sha256",tag.get("core_sha256"))==source["core_sha256"]
    actual=fingerprint(tag)
    if source.get("configuration_sha256") is None:
        assert source.get("derive_configuration_from_pinned_original_stage") is True
        source["configuration_sha256"]=actual
    else:
        assert actual==source["configuration_sha256"]
    if core.get("configuration") is not None:
        assert core["configuration"]==tag
    if core.get("configuration_sha256") is not None:
        assert core["configuration_sha256"]==fingerprint(tag)
    return certificate,tag,initial

def extract_flat_package(package,folder):
    folder=Path(folder);folder.mkdir(parents=True,exist_ok=True);seen=set()
    with tarfile.open(package,"r|gz") as archive:
        for member in archive:
            if member.isdir():
                continue
            p=PurePosixPath(member.name)
            assert member.isfile() and not p.is_absolute() and ".." not in p.parts
            assert "\\" not in member.name and len(p.parts)==2 and p.parts[0]=="original"
            assert p.name not in seen;seen.add(p.name)
            target=folder/p.name;tmp=target.with_name(target.name+".download")
            with archive.extractfile(member) as src,tmp.open("wb") as dst:
                shutil.copyfileobj(src,dst)
            assert tmp.stat().st_size==member.size
            if target.exists():
                assert target.stat().st_size==member.size and sha(target)==sha(tmp)
                tmp.unlink()
            else:
                tmp.replace(target)

def extract_bound_group(package,retained,label,source):
    folder=Path(retained)/label;folder.mkdir(parents=True,exist_ok=True);seen=set()
    with tarfile.open(package,"r|gz") as archive:
        for member in archive:
            if member.isdir():
                continue
            path=PurePosixPath(member.name)
            assert member.isfile() and not path.is_absolute() and ".." not in path.parts and "\\" not in member.name
            assert len(path.parts)==2 and path.parts[0]==label and path.name not in seen
            row=source["files"][path.name];assert member.size==row["bytes"]
            target=folder/path.name;tmp=target.with_name(target.name+".download")
            h=hashlib.sha256();count=0
            with archive.extractfile(member) as src,tmp.open("wb") as dst:
                for chunk in iter(lambda:src.read(4*1024*1024),b""):
                    dst.write(chunk);h.update(chunk);count+=len(chunk)
            assert count==row["bytes"] and h.hexdigest()==row["sha256"]
            if target.exists():
                assert spec(target)==plain(row);tmp.unlink()
            else:
                tmp.replace(target)
            seen.add(path.name)
    assert seen==set(source["files"])
    return folder

class Handle:
    def __init__(self,group,item,retained,work):
        self.group=group;self.prior=dict(item["source_artifacts"][group])
        self.folder=Path(retained)/group;self.folder.mkdir(parents=True,exist_ok=True)
        self.work=Path(work);self.archive=None;self.selected={};self.transports=[]
        for prepared in item.get("prepared_transports",{}).get(group,[]):
            outer=IO.Archive(prepared["archive"],self.work/("prepared-"+group+"-"+str(len(self.transports))),whole=False)
            try:
                package=plain(prepared["package"]);target=self.work/(group+"-"+package["file"])
                outer.extract_bound(package["file"],package["sha256"],target,package["bytes"])
                extract_flat_package(target,self.folder)
                self.transports.append({"kind":"completed_original_intake","source":prepared["archive"],
                    "package":package,"range_receipt":outer.receipt()})
            finally:
                outer.close()
        if not (self.folder/MANIFEST).exists():
            self.open_archive().extract_bound(MANIFEST,self.prior["manifest_sha256"],
                self.folder/MANIFEST,self.prior.get("manifest_bytes"))
        self.entries=entry_map(self.folder,self.prior)
        if self.prior.get("certificate") is not None or self.prior.get("certificate_name") is not None:
            wanted=self.prior.get("certificate")
            name=wanted["file"] if wanted else self.prior["certificate_name"]
            actual=self.entries[name]
            if wanted is not None:
                assert actual["sha256"]==wanted["sha256"]
                if wanted.get("bytes") is not None:
                    assert actual["bytes"]==wanted["bytes"]
            self.prior["certificate"]=actual
            anchor=name
        else:
            self.prior["certificate"]=None
            row=plain(self.prior["configuration_stage"])
            assert self.entries[row["file"]]==row
            anchor=row["file"]
        self.take(list(META)+[anchor])
        self.certificate,self.tag,self.initial=metadata(group,self.folder,self.prior,self.entries)

    def open_archive(self):
        if self.archive is None:
            self.archive=IO.Archive(self.prior,self.work/("original-"+self.group),whole=False)
        return self.archive

    def take(self,names):
        names=sorted(set(names));missing=[]
        for name in names:
            row=self.entries[name];path=self.folder/name
            if path.exists():
                assert spec(path)==row,(self.group,name)
            else:
                missing.append(name)
        if missing:
            self.open_archive().extract_many([
                (name,self.entries[name]["sha256"],self.folder/name,self.entries[name]["bytes"])
                for name in missing])
        for name in names:
            bound(self.folder,self.entries[name]);self.selected[name]=self.entries[name]

    def stage(self,row):
        row=plain(row);assert self.entries[row["file"]]==row
        self.take([row["file"]]);value=read(self.folder/row["file"])
        assert value["complete"] is True and value["configuration"]==self.tag
        return value

    def named(self,name):
        self.take([name]);return self.stage(self.entries[name])

    def ref(self,row):
        return group_ref(self.group,row)

    def finish_source(self):
        self.selected[MANIFEST]=self.entries[MANIFEST]
        answer={**{k:self.prior[k] for k in BASE},
            "configuration_sha256":fingerprint(self.tag),"files":dict(sorted(self.selected.items()))}
        if self.prior["certificate"] is not None:
            answer["certificate"]=plain(self.prior["certificate"])
        else:
            answer["configuration_stage"]=plain(self.prior["configuration_stage"])
            answer["accepted_process_exit_codes"]=self.prior["accepted_process_exit_codes"]
        for key in ("manifest_bytes","manifest_file_count"):
            if self.prior.get(key) is not None:
                answer[key]=self.prior[key]
        return answer

    def receipt(self):
        return {"kind":"hash-bound-original-source-selection","source":self.prior,
            "completed_transports":self.transports,
            "additional_original_Range":self.archive.receipt() if self.archive else None,
            "selected_files":dict(sorted(self.selected.items())),
            "existing_complete_original_files_reused":True}

    def close(self):
        if self.archive is not None:
            self.archive.close()

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

def dimensions(value,m,n):
    assert len(value)==m and all(len(row)==n for row in value),(m,n)

def bootstrap_R827(item,retained,work):
    transport=item["R827_transport"];parent=transport["producer"]
    synthetic={"source_artifacts":{"POLY":parent},"prepared_transports":{}}
    handle=Handle("POLY",synthetic,retained,work)
    try:
        for key in ("source_inventory","retained_inputs_receipt","package"):
            row=plain(transport[key]);assert handle.entries[row["file"]]==row
            handle.take([row["file"]])
        inventory=read(handle.folder/transport["source_inventory"]["file"])
        receipt=read(handle.folder/transport["retained_inputs_receipt"]["file"])
        assert plain(receipt["source_inventory"])==plain(transport["source_inventory"])
        assert plain(receipt["source_bundle"])==plain(transport["package"])
        source=inventory["source_R827"]
        same_source(source,item["source_artifacts"]["R827"])
        old_identity={k:source[k] for k in BASE}
        old_identity["configuration_sha256"]=source["configuration_sha256"]
        old_identity["selected_files_sha256"]=fingerprint(source["files"])
        if source.get("certificate") is not None:
            old_identity["certificate"]=plain(source["certificate"])
        else:
            old_identity["configuration_stage"]=plain(source["configuration_stage"])
        assert old_identity==handle.tag["source_R827"]
        assert inventory["inputs"]==handle.tag["inputs"]
        extract_bound_group(handle.folder/transport["package"]["file"],retained,"R827",source)
        return {"kind":"completed_POLY_carrier_transport_only","source":parent,
                "package":plain(transport["package"]),"source_inventory":plain(transport["source_inventory"]),
                "retained_inputs_receipt":plain(transport["retained_inputs_receipt"]),
                "original_R827_identity":old_identity,
                "old_complete_R827_bytes_and_individual_members_verified":True,
                "mathematical_POLY_stages_called":False,"new_mathematics_executed":False,
                "range_transport":handle.receipt()}
    finally:
        handle.close()

def node_map(value):
    if isinstance(value,list):
        assert len(value)==7
        return {str(i):value[i] for i in range(7)}
    assert isinstance(value,dict) and set(value)==set(map(str,range(7)))
    return value

def original_pins(item,sources,inputs=None):
    assert set(sources)==set(MANDATORY)
    for group,source in sources.items():
        prior=item["source_artifacts"][group]
        assert prior is not None
        assert all(str(source[k])==str(prior[k]) for k in BASE)
        if prior.get("configuration_sha256") is not None:
            assert source["configuration_sha256"]==prior["configuration_sha256"]
        else:
            assert prior.get("derive_configuration_from_pinned_original_stage") is True
        if prior.get("certificate") is not None:
            assert plain(source["certificate"])==plain(prior["certificate"])
        else:
            assert group=="R827"
            assert plain(source["configuration_stage"])==plain(prior["configuration_stage"])
            assert source["accepted_process_exit_codes"]==prior["accepted_process_exit_codes"]
        for name,row in item.get("source_file_pins",{}).get(group,{}).items():
            assert source["files"][name]==plain(row)
    if inputs is not None:
        for key,row in item.get("input_pins",{}).items():
            assert plain(inputs[key])==plain(row)
        for key in ("original_normal_V3_fibres","original_Krylov_points"):
            assert set(inputs[key])==set(map(str,range(7)))
        assert set(inputs["completed_normalized_space_fibres"])<=set(map(str,range(7)))
        for z,row in item.get("cached_normal_V3_fibres",{}).items():
            assert inputs["original_normal_V3_fibres"][z]==row
        assert inputs["K_fixed_normal_basis"]["source_group"]=="R899"
        assert inputs["P0_leading_row"]["source_group"]=="R899"
        assert inputs["original_QN"]["source_group"]=="R894"
        assert inputs["original_W"]["source_group"]=="R827"
        assert inputs["t_frame"]["source_group"]=="R883"

def source_review(item,retained,sources,inputs):
    original_pins(item,sources,inputs)
    tags={};certificates={}
    for group,source in sources.items():
        folder=Path(retained)/group
        entries=entry_map(folder,source)
        for name,row in source["files"].items():
            assert entries[name]==plain(row)
            bound(folder,row)
        cert,tag,_=metadata(group,folder,source,entries)
        tags[group]=tag;certificates[group]=cert
        for name,row in source["files"].items():
            if name.endswith(".json.gz"):
                value=read(folder/name)
                assert value["complete"] is True and value["configuration"]==tag
                if group=="R827":
                    assert "result" not in value
                    assert value["configuration"]["result"]==source["result"]
                else:
                    assert value["result"]==source["result"]
    def stage(row):
        group=row["source_group"]
        assert sources[group]["files"][row["file"]]==plain(row)
        value=read(bound(Path(retained)/group,row))
        assert value["configuration"]==tags[group] and value["complete"] is True
        return value
    original=certificates["R899"]
    assert original["result"]=="R899-original-K-fixed-seven-trace-RR-basis"
    assert original["all418_original_K_fixed_functions_certified"] is True
    assert original["new_fixed_basis_descent_identity_certified"] is True
    assert original["original_QN_and_selected_scalars_rescaled"] is False
    for group in ("R894","R890","R827","R883"):
        same_source(original["source_identities"][group],sources[group])
    assert plain(inputs["K_fixed_normal_basis"])==plain(original["complete_K_fixed_normal_basis"])
    assert plain(inputs["P0_leading_row"])==plain(original["original_P0_leading_row"])
    assert plain(inputs["original_QN"])==plain(original["marked_QN"])
    basis=stage(inputs["K_fixed_normal_basis"]);point=stage(inputs["P0_leading_row"])
    positions=[[i,k] for i in range(272) for k in range(4-EPS[i])]
    assert len(positions)==690 and basis["normal_V3_basis"]==positions
    dimensions(basis["normal_V3_basis_mod_prime"],690,418)
    assert basis["all418_original_K_fixed_functions_certified"] is True
    assert basis["normal_sections_without_QN_claimed_K_fixed"] is False
    assert basis["new_fixed_basis_action_identity_certified_by_uniqueness"] is True
    assert plain(basis["source_original_QN"])==plain(inputs["original_QN"])
    definition=basis["exact_fixed_functions_DAG"]
    assert definition["operation"]=="positive_multiply_original_QN"
    assert plain(definition["original_QN_source"])==plain(inputs["original_QN"])
    assert definition["normal_sections"]["operation"]=="right_multiply_original_WN_basis"
    assert plain(definition["normal_sections"]["source_original_WN"])==plain(basis["source_original_DN_normal418"])
    inverse=stage(group_ref("R899",basis["source_selected_evaluation_inverse"]))
    assert plain(basis["source_selected_evaluation_inverse"])==plain(original["selected_evaluation_inverse"])
    assert inverse["accepted"] is True and inverse["actual_rank"]==418
    assert inverse["both_selected_inverse_products_verified"] is True
    assert inverse["selected_coordinates_of_all418_normalized_functions_are_identity"] is True
    assert definition["normal_sections"]["exact_basis_change_unit_solve"]==inverse["exact_inverse_definition"]
    QN=stage(inputs["original_QN"])
    assert isinstance(QN["exact_QN_function_DAG"],dict)
    assert QN["actual_rho_order"]==-8435 and QN["DN_avoids_original_P0"] is True
    assert QN["DN_effective_degree"]==272 and QN["complete_W_DN_dimension"]==418
    assert QN["Q_orbit_fixed_by_original_Gal_L_over_K"] is True
    assert QN["original_fractional_ideal_principal_factor_direction"]=="positive multiplication by Q_N"
    assert QN["exact_original_divisor_identity"]=="T_f^0=(D_N-H)+div(Q_N)"
    assert plain(QN["source_complete_DN_normal418"])==plain(basis["source_original_DN_normal418"])
    assert plain(point["source_K_fixed_normal_basis"])==plain(inputs["K_fixed_normal_basis"])
    assert plain(point["source_original_QN"])==plain(inputs["original_QN"])
    assert point["original_rho_and_t_order"]==-8435 and point["selected_column_rescaled"] is False
    assert point["old_point_jets_or_t_constant_recomputed"] is False
    assert len(point["normal_V3_P0_functional_mod_prime"])==690
    for key in ("normal_V3_P0_values_mod_prime","rho_leading_coefficients_mod_prime",
                "t_leading_coefficients_mod_prime"):
        assert len(point[key])==418
        assert all(isinstance(x,int) and 0<=x<P for x in point[key])
    first=next((i for i,x in enumerate(point["t_leading_coefficients_mod_prime"]) if x),None)
    assert point["first_unit_column"]==first
    assert point["actual_marked_P0_unit_column_certified"] is (first is not None)
    assert original["actual_first_P0_unit_column"]==first
    for key in ("actual_QN_rho_leading_mod_prime","actual_QN_t_leading_mod_prime",
                "actual_original_c_power8435_mod_prime"):
        assert point[key]==QN[key]
    assert plain(point["source_original_t_frame"])==plain(inputs["t_frame"])
    assert plain(QN["source_original_t_frame"])==plain(inputs["t_frame"])
    frame=stage(inputs["t_frame"])
    assert frame["original_t_first_order_unit_certified"] is True
    assert frame["exact_zero_not_inferred_from_modular_zero"] is True
    assert frame["original_t_over_rho_constant_mod_prime"]==354813668
    W=stage(inputs["original_W"]);assert W["prime"]==P
    assert plain(inputs["original_W"])==plain(original["original_W"])
    oldE=node_map(original["original_normal_V3_fibres"])
    oldK=node_map(original["original_Krylov_points"])
    for z in map(str,range(7)):
        assert plain(inputs["original_normal_V3_fibres"][z])==plain(oldE[z])
        assert plain(inputs["original_Krylov_points"][z])==plain(oldK[z])
        E=stage(inputs["original_normal_V3_fibres"][z]);K=stage(inputs["original_Krylov_points"][z])
        assert E["prime"]==K["prime"]==P and E["z0"]==K["z0"]==int(z)
        assert E["normal_V3_basis"]==positions
        assert E["normal_integer_scale_applied_again"] is False
        assert E["old_W_K_or_Kinverse_recomputed"] is False
        assert plain(E["source_original_Krylov_point"])==plain(inputs["original_Krylov_points"][z])
        assert plain(E["source_original_W"])==plain(inputs["original_W"])
        assert K["usable"] is True and K["actual_cyclic_rank"]==272
        assert K["both_inverse_products_verified"] is True
        for key in ("normal_evaluation_mod_prime","cyclic_evaluation_mod_prime"):
            dimensions(E[key],272,690)
        for key in ("W_evaluated_mod_prime","Krylov_matrix_mod_prime","inverse_Krylov_matrix_mod_prime"):
            dimensions(K[key],272,272)
    assert {z:plain(row) for z,row in inputs["completed_normalized_space_fibres"].items()}=={
        z:plain(row) for z,row in original["completed_normalized_space_fibres"].items()}
    for z,ref in inputs["completed_normalized_space_fibres"].items():
        value=stage(ref)
        assert value["prime"]==P and value["z0"]==int(z)
        assert value["original_QN_factor_included"] is False
        assert plain(value["source_K_fixed_normal_basis"])==plain(inputs["K_fixed_normal_basis"])
        assert plain(value["source_original_normal_V3_fibre"])==plain(inputs["original_normal_V3_fibres"][z])
        assert plain(value["source_original_Krylov_point"])==plain(inputs["original_Krylov_points"][z])
        for key in ("normal_evaluation_mod_prime","cyclic_evaluation_mod_prime"):
            dimensions(value[key],272,418)
    return {"result":RESULT,"complete":True,
        "selected_counts":{g:len(v["files"]) for g,v in sources.items()},
        "selected_file_total":sum(len(v["files"]) for v in sources.values()),
        "source_configuration_sha256":{g:v["configuration_sha256"] for g,v in sources.items()},
        "original_complete_K_fixed_functions":418,
        "underlying_normal_columns_alone_claimed_K_fixed":False,
        "source_first_P0_unit_column":first,
        "completed_original_normalized_space_fibres":sorted(map(int,inputs["completed_normalized_space_fibres"])),
        "all_seven_whole_V3_and_Krylov_sources_retained":True,
        "whole_original_QN_function_DAG_retained_under_original_R894_identity":True,
        "old_original_W_Kinverse_E3_QN_or_point_arithmetic_recomputed":False,
        "new_mathematics_executed_in_source_review":False}

def bootstrap_QN_from_R899(item,handle,retained):
    if not item.get("R894_from_R899_carrier",False):
        return None
    names=("R899-original-source-inventory.json","R899-retained-inputs-receipt.json",
           "R899-retained-original-inputs.tar.gz")
    handle.take(names)
    inventory=read(handle.folder/names[0]);receipt=read(handle.folder/names[1])
    assert inventory["result"]==receipt["result"]==handle.prior["result"]
    assert inventory["complete"] is True and receipt["complete"] is True
    assert plain(receipt["source_inventory"])==handle.entries[names[0]]
    assert plain(receipt["source_bundle"])==handle.entries[names[2]]
    assert handle.initial["source_inventory"]==handle.entries[names[0]]
    source=inventory["sources"]["R894"]
    same_source(source,item["source_artifacts"]["R894"])
    assert identity(source)==handle.tag["sources"]["R894"]
    assert identity(source)==handle.certificate["source_identities"]["R894"]
    target=Path(retained)/"R894";target.mkdir(parents=True,exist_ok=True)
    QN=plain(handle.certificate["marked_QN"])
    assert source["files"][QN["file"]]==QN
    required=set(META)|{MANIFEST,source["certificate"]["file"],QN["file"]}
    seen=set()
    with tarfile.open(handle.folder/names[2],"r|gz") as archive:
        for member in archive:
            if member.isdir():
                continue
            p=PurePosixPath(member.name)
            assert member.isfile() and not p.is_absolute() and ".." not in p.parts
            assert "\\" not in member.name and len(p.parts)==2
            if p.parts[0]!="R894" or p.name not in required:
                continue
            assert p.name not in seen
            row=plain(source["files"][p.name]);assert member.size==row["bytes"]
            temporary=target/(p.name+".download");h=hashlib.sha256();count=0
            with archive.extractfile(member) as src,temporary.open("wb") as dst:
                for chunk in iter(lambda:src.read(4*1024*1024),b""):
                    dst.write(chunk);h.update(chunk);count+=len(chunk)
            assert count==row["bytes"] and h.hexdigest()==row["sha256"]
            final=target/p.name
            if final.exists():
                assert spec(final)==row;temporary.unlink()
            else:
                temporary.replace(final)
            seen.add(p.name)
    assert seen==required
    record={"kind":"completed_R899_carrier_original_R894_group",
        "source_R899":handle.prior,"source_inventory":handle.entries[names[0]],
        "retained_inputs_receipt":handle.entries[names[1]],"package":handle.entries[names[2]],
        "original_R894_identity":identity(source),
        "selected_original_files":{name:source["files"][name] for name in sorted(required)},
        "original_QN_global_DAG_and_configuration_preserved":True,
        "large_R899_carrier_not_placed_in_new_mathematical_input_bundle":True,
        "new_mathematics_executed":False}
    for name in names:
        handle.selected.pop(name,None)
    return record

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R900";retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (BUNDLE,INVENTORY,INPUT_RECEIPT)):
        inventory=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        assert receipt["source_inventory"]==spec(out/INVENTORY)
        assert receipt["source_bundle"]==spec(out/BUNDLE)
        sources,inputs=inventory["sources"],inventory["inputs"]
        original_pins(item,sources,inputs)
        unpack(out/BUNDLE,retained,sources)
        review=source_review(item,retained,sources,inputs)
        return retained,sources,inputs,review
    assert allow_download,"The retained original source carrier is required for offline verification."
    work=out.parent/"R900-download";work.mkdir(parents=True,exist_ok=True);handles={}
    try:
        bootstrap=bootstrap_R827(item,retained,work)
        handles["R899"]=Handle("R899",item,retained,work)
        QN_transport=bootstrap_QN_from_R899(item,handles["R899"],retained)
        for group in MANDATORY:
            if group!="R899":
                handles[group]=Handle(group,item,retained,work)
        R=handles["R899"];cert=R.certificate
        assert cert["all418_original_K_fixed_functions_certified"] is True
        assert cert["new_fixed_basis_descent_identity_certified"] is True
        if cert.get("source_audit") is not None:
            R.stage(cert["source_audit"])
        basis=R.stage(cert["complete_K_fixed_normal_basis"])
        point=R.stage(cert["original_P0_leading_row"])
        inverse=R.stage(cert["selected_evaluation_inverse"])
        assert plain(basis["source_selected_evaluation_inverse"])==plain(cert["selected_evaluation_inverse"])
        assert inverse["accepted"] is True and inverse["actual_rank"]==418
        inputs={
            "K_fixed_normal_basis":R.ref(cert["complete_K_fixed_normal_basis"]),
            "P0_leading_row":R.ref(cert["original_P0_leading_row"]),
            "original_QN":handles["R894"].ref(cert["marked_QN"]),
            "original_W":handles["R827"].ref(cert["original_W"]),
            "t_frame":handles["R883"].ref(point["source_original_t_frame"]),
            "original_normal_V3_fibres":{},"original_Krylov_points":{},
            "completed_normalized_space_fibres":{}}
        for group in ("R894","R890","R827","R883"):
            same_source(cert["source_identities"][group],handles[group].prior)
        assert cert["marked_QN"]["source_group"]=="R894"
        QN=handles["R894"].stage(cert["marked_QN"])
        assert plain(point["source_original_QN"])==plain(cert["marked_QN"])
        assert plain(QN["source_original_t_frame"])==plain(inputs["t_frame"])
        handles["R883"].stage(inputs["t_frame"])
        handles["R827"].stage(inputs["original_W"])
        E=node_map(cert["original_normal_V3_fibres"])
        K=node_map(cert["original_Krylov_points"])
        for z in map(str,range(7)):
            assert E[z]["source_group"]=="R890" and K[z]["source_group"]=="R827"
            handles["R890"].stage(E[z]);handles["R827"].stage(K[z])
            inputs["original_normal_V3_fibres"][z]=handles["R890"].ref(E[z])
            inputs["original_Krylov_points"][z]=handles["R827"].ref(K[z])
        for z,ref in cert["completed_normalized_space_fibres"].items():
            assert z in inputs["original_normal_V3_fibres"]
            R.stage(ref);inputs["completed_normalized_space_fibres"][z]=R.ref(ref)
        sources={g:h.finish_source() for g,h in handles.items()}
        original_pins(item,sources,inputs)
        review=source_review(item,retained,sources,inputs)
        transports={g:h.receipt() for g,h in handles.items()}
        transports["R827"]["completed_POLY_original_source_carrier"]=bootstrap
        transports["R894"]["completed_R899_original_QN_transport"]=QN_transport
        save(out/INVENTORY,{"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
            "transports":transports,"all_source_selected_bytes_preserved":True,
            "original_QN_global_DAG_preserved_under_original_R894_configuration":True,
            "old_sixteen_flip_matrices_and_large_producer_carriers_not_selected":True,
            "new_mathematics_executed":False})
        pack(retained,sources,out/BUNDLE)
        save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,
            "source_inventory":spec(out/INVENTORY),"source_bundle":spec(out/BUNDLE),
            "source_identities":{g:identity(v) for g,v in sources.items()},
            "selected_file_counts":{g:len(v["files"]) for g,v in sources.items()},
            "all_original_selected_bytes_and_stage_configurations_verified":True,
            "old_QN_K_fixed_basis_Krylov_normal_fibres_and_point_arithmetic_recomputed":False,
            "new_mathematics_executed":False})
        print("R900_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,sources,inputs,review
    finally:
        for h in handles.values():
            h.close()

def restore(item,out):
    resume=item.get("resume")
    if not resume:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R900-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R900-resume-archive",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],directory/MANIFEST,resume.get("manifest_bytes"))
        entries=entry_map(directory,resume)
        names=(set(META)&set(entries))|{BUNDLE,INVENTORY,INPUT_RECEIPT}
        archive.extract_many([(n,entries[n]["sha256"],directory/n,entries[n]["bytes"]) for n in sorted(names)])
        initial=read(directory/"public-actions-input.json");run=read(directory/"run-receipt.json")
        assert initial["result"]==run["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]==resume["source_commit"]
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        for key in ("core_sha256","wrapper_sha256"):
            assert initial[key]==item[key]
        for key in ("proofs","method_sha256"):
            assert initial["job"][key]==item[key]
        core=None
        if run.get("core_receipt_sha256") is not None:
            assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
            core=read(directory/"core-receipt.json")
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        else:
            assert run["complete"] is False
        inventory=read(directory/INVENTORY);receipt=read(directory/INPUT_RECEIPT)
        assert plain(receipt["source_inventory"])==entries[INVENTORY]
        assert plain(receipt["source_bundle"])==entries[BUNDLE]
        sources,inputs=inventory["sources"],inventory["inputs"]
        original_pins(item,sources,inputs)
        for key,row in item.get("input_pins",{}).items():
            assert plain(inputs[key])==plain(row)
        tag=expected_tag(item,sources,inputs)
        assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
        if core is not None and core.get("configuration") is not None:
            assert core["configuration"]==tag
        if core is not None and core.get("configuration_sha256") is not None:
            assert core["configuration_sha256"]==fingerprint(tag)
        for name in (BUNDLE,INVENTORY,INPUT_RECEIPT):
            target=out/name
            if target.exists():
                assert spec(target)==entries[name]
            else:
                shutil.copyfile(directory/name,target)
        stages=[n for n in entries if n.startswith(PREFIX) and n.endswith(".json.gz")]
        archive.extract_many([(n,entries[n]["sha256"],directory/n,entries[n]["bytes"]) for n in stages])
        for name in stages:
            value=read(directory/name)
            assert value["result"]==RESULT and value["configuration"]==tag
            assert value["complete"] is (False if name==PREFIX+"current.json.gz" else True)
            target=out/name
            if target.exists():
                assert spec(target)==entries[name]
            else:
                shutil.copyfile(directory/name,target)
        if FINAL in entries:
            archive.extract_bound(FINAL,entries[FINAL]["sha256"],directory/FINAL,entries[FINAL]["bytes"])
            cert=read(directory/FINAL)
            assert cert["result"]==RESULT and cert["configuration"]==tag
            if cert["complete"] is True:
                assert plain(cert["stage_manifest"])==entries[cert["stage_manifest"]["file"]]
                old_manifest=read(bound(directory,cert["stage_manifest"]))
                for row in old_manifest["files"]:
                    assert plain(row)==entries[row["file"]]
                assert plain(cert["resume_state"])==entries[cert["resume_state"]["file"]]
                shutil.copyfile(directory/FINAL,out/FINAL)
        save(out/"resume-import-receipt.json",{
            "result":RESULT,"complete":True,"source":resume,
            "original_manifest":spec(directory/MANIFEST),
            "mathematical_configuration_sha256":fingerprint(tag),
            "restored_stage_count":len(stages),"same_new_core_and_original_source_tags_preserved":True,
            "incomplete_historical_final_did_not_constrain_later_current":True,
            "missing_core_receipt_honestly_retained":core is None,
            "range_transport":archive.receipt()})
    finally:
        archive.close()

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

def compute(item,out,request):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    code,error,outer_timeout=1,None,False
    try:
        restore(item,out)
        retained,sources,inputs,review=prepare(item,out)
        expanded={**item,"sources":sources,"inputs":inputs}
        save(out/EXPANDED,expanded)
        tag=expected_tag(item,sources,inputs)
        save(out/"public-actions-input.json",{
            "result":RESULT,"p":41,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"job":item,
            "core_sha256":item["core_sha256"],"wrapper_sha256":item["wrapper_sha256"],
            "request_sha256":sha(request),"workflow_sha256":sha(REPO/item["workflow"]),
            "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
            "expanded_job":spec(out/EXPANDED),"source_inventory":spec(out/INVENTORY),
            "mathematical_configuration_sha256":fingerprint(tag),
            "source_identities":{g:identity(sources[g]) for g in sorted(sources)},
            "new_mathematics_in_wrapper":False})
        command=[sys.executable,str(S/CORE),"--config",str(out/EXPANDED),
                 "--retained",str(retained),"--output",str(out),
                 "--budget-minutes",str(item["budget_minutes"])]
        with (out/"core.log").open("ab") as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                code=process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                outer_timeout=True
                os.killpg(process.pid,signal.SIGTERM)
                try:
                    process.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid,signal.SIGKILL);process.wait()
                code=124;error="outer_timeout"
        if code==0:
            assert read(out/FINAL)["complete"] is True
        print((out/"core.log").read_text(errors="replace")[-16000:],flush=True)
    except Exception as exc:
        code=code if code not in (0,1) else 1
        error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    finally:
        save(out/"run-receipt.json",{
            "result":RESULT,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_sha256":item["core_sha256"],"wrapper_sha256":item["wrapper_sha256"],
            "complete":code==0,"process_exit_code":code,"error":error,"outer_timeout":outer_timeout,
            "execution_environment":"public-repository-github-actions",
            "core_receipt_sha256":sha(out/"core-receipt.json") if (out/"core-receipt.json").exists() else None,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    return code

def verify_complete_final(item,out,entries,tag,cert,sources,inputs):
    def own(row):
        row=plain(row);assert entries[row["file"]]==row
        value=read(bound(out,row))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        return value
    def relation(row,rank,dimension):
        value=own(row)
        assert value["matrix_shape"]==[1904,1380]
        assert value["actual_rank"]==rank and value["actual_kernel_dimension"]==dimension
        assert value["all_original_rows_checked"]==1904
        for key in ("all_original_rows_times_complete_kernel_zero","canonical_free_identity_verified",
                    "both_selected_inverse_products_verified","complete_characteristic_zero_space_certified"):
            assert value[key] is True
        profile=own(value["source_rank_profile"])
        assert profile["required_rank"]==profile["actual_rank"]==rank and profile["accepted"] is True
        assert profile["matrix_shape"]==[1904,1380]
        inverse=own(value["source_selected_unit_inverse"])
        assert plain(inverse["source_rank_profile"])==plain(value["source_rank_profile"])
        assert inverse["matrix_shape"]==[rank,rank]
        assert inverse["both_selected_inverse_products_verified"] is True
        assert inverse["characteristic_zero_minor_is_a_unit"] is True
        assert 0<inverse["actual_selected_minor_determinant_mod_prime"]<P
        dimensions(inverse["inverse_selected_minor_mod_prime"],rank,rank)
        raw=own(value["source_canonical_kernel"])
        assert raw["matrix_shape"]==[1380,dimension]
        dimensions(raw["kernel_basis_mod_prime"],1380,dimension)
        assert len(raw["free_columns"])==dimension and len(raw["pivot_columns"])==rank
        assert sorted(raw["free_columns"]+raw["pivot_columns"])==list(range(1380))
        assert raw["canonical_free_identity_verified"] is True
        assert raw["all_selected_original_rows_times_kernel_zero"] is True
        assert plain(raw["source_selected_unit_inverse"])==plain(value["source_selected_unit_inverse"])
        checks=value["source_all_original_row_checks"]
        assert len(checks)==7
        for i,ref in enumerate(checks):
            check=own(ref)
            assert check["original_row_interval"]==[272*i,272*(i+1)]
            assert check["checked_shape"]==[272,dimension]
            assert check["all_original_rows_in_interval_times_kernel_zero"] is True
            assert plain(check["source_canonical_kernel"])==plain(value["source_canonical_kernel"])
        return value
    def projection(row,kernel_ref,dimension):
        value=own(row)
        assert plain(value["source_complete_kernel"])==plain(kernel_ref)
        assert value["matrix_shape"]==[690,dimension] and value["projection_rows"]==[690,1380]
        assert value["actual_projected_rank"]==dimension
        assert len(value["independent_normal_V3_rows"])==dimension
        assert 0<value["actual_projection_minor_determinant_mod_prime"]<P
        assert value["complete_RR_space_certified"] is True
        assert value["normal_integer_scale_applied_again"] is False
        assert value["characteristic_zero_coordinates_reconstructed"] is False
        dimensions(value["normal_V3_basis_mod_prime"],690,dimension)
        return value
    def products(refs,anchor_ref):
        assert len(refs)==7
        for z,row in enumerate(refs):
            value=own(row)
            assert value["z0"]==z and value["prime"]==P
            assert plain(value["source_anchor"])==plain(anchor_ref)
            assert plain(value["source_original_normal_V3_fibre"])==plain(inputs["original_normal_V3_fibres"][str(z)])
            assert plain(value["source_original_Krylov_point"])==plain(inputs["original_Krylov_points"][str(z)])
            assert value["matrix_shape"]==[272,690]
            dimensions(value["product_evaluation_mod_prime"],272,690)
            assert len(value["anchor_evaluation_mod_prime"])==272
            assert value["whole272_dimensional_Artin_fibre_retained"] is True
            assert value["factors_or_nilpotents_removed"] is False
            assert value["old_Krylov_inverse_QN_or_point_arithmetic_recomputed"] is False
    assert cert["prime"]==P and cert["p"]==41
    assert set(cert["complete_direction_certificates"])=={"D0_146","DK_418","marked_QK"}
    assert cert["complete_first_residual_certificate"]==cert["complete_direction_certificates"]["D0_146"]
    assert cert["complete_K_defined_degree272_certificate"]==cert["complete_direction_certificates"]["DK_418"]
    assert cert["marked_original_principal_QK"]==cert["complete_direction_certificates"]["marked_QK"]
    assert cert["source_original_R899_K_fixed_basis"]==inputs["K_fixed_normal_basis"]
    assert cert["source_original_P0_leading_row"]==inputs["P0_leading_row"]
    assert cert["source_original_t_frame"]==inputs["t_frame"]
    audit=own(cert["source_audit"])
    assert audit["sources"]=={g:identity(v) for g,v in sources.items()} and audit["inputs"]==inputs
    assert audit["source_original_QN"]==inputs["original_QN"]
    assert audit["source_QN_configuration"]==read(bound(Path(out).parent/"retained-R900"/"R894",sources["R894"]["certificate"]))["configuration"]
    assert isinstance(audit["original_QN_function_DAG_preserved"],dict)
    assert audit["original_K_fixed_functions_include_positive_QN"] is True
    assert audit["underlying_normal_columns_alone_not_claimed_K_fixed"] is True
    assert audit["QN_units_in_all_seven_fibres_required"] is False
    D0=own(cert["complete_first_residual_certificate"])
    assert D0["actual_product_rank"]==1234 and D0["all_original_product_rows_checked"]==1904
    assert D0["complete_relation_dimension"]==D0["second_projection_dimension"]==146
    assert D0["D0_degree"]==544
    for key in ("D0_effective","D0_defined_over_original_K","D0_avoids_original_P0",
                "whole_original_V6_evaluation_injective","source_QN_not_evaluated_again",
                "canonical_relation_free_coordinates_give_K_fixed_basis",
                "complete_characteristic_zero_H0_3H_minus_D0_certified"):
        assert D0[key] is True
    assert D0["source_complete_K_fixed_functions"]==inputs["K_fixed_normal_basis"]
    S0=own(D0["source_unscaled_S0"]);S1=own(D0["source_S1"])
    assert S0["trial"] is None and S0["role"]=="S0"
    assert S0["original_scalar_not_rescaled"] is True and S0["actual_order_minus8435_certified"] is True
    assert S0["source_K_fixed_normal_basis"]==inputs["K_fixed_normal_basis"]
    assert S0["source_original_QN"]==inputs["original_QN"]
    assert S0["extra_tau_power"]==0
    assert 0<S0["actual_normal_value_at_P0_mod_prime"]<P
    assert 0<S0["actual_S_rho_leading_mod_prime"]<P and 0<S0["actual_S_t_leading_mod_prime"]<P
    assert S1["trial"]==D0["accepted_second_anchor_integer"] and S1["role"]=="S1"
    assert S1["exact_K_fixed_function_definition"]["integer_parameter"]==S1["trial"]
    assert S1["exact_K_fixed_function_definition"]["exponents"]==[0,417]
    assert S1["original_scalar_not_rescaled"] is True and S1["extra_tau_power"]==0
    products(D0["source_w0_products"],D0["source_unscaled_S0"])
    products(D0["source_w1_products"],D0["source_S1"])
    first=relation(D0["source_complete_relation_kernel"],1234,146)
    U=projection(D0["complete_normal146_space"],D0["source_complete_relation_kernel"],146)
    assert first["exact_complete_space_definition"]["K_fixed_relation_basis_by_unique_free_coordinate_identity"] is True
    assert U["exact_RR_space"]["K_fixed_by_canonical_relation_and_projection"] is True
    DK=own(cert["complete_K_defined_degree272_certificate"])
    assert DK["source_complete_D0_certificate"]==cert["complete_first_residual_certificate"]
    assert DK["source_complete146_space"]==D0["complete_normal146_space"]
    assert DK["actual_product_rank"]==962 and DK["all_original_product_rows_checked"]==1904
    assert DK["complete_relation_dimension"]==DK["second_projection_dimension"]==418
    assert DK["DK_degree"]==272
    for key in ("DK_effective","DK_defined_over_original_K","DK_avoids_original_P0",
                "whole_original_V6_evaluation_injective","canonical_relation_free_coordinates_give_K_fixed_basis",
                "complete_characteristic_zero_H0_3H_minus_DK_certified"):
        assert DK[key] is True
    v=own(DK["source_exact_v"]);w=own(DK["source_exact_w"])
    assert v["trial"] is None and v["role"]=="v" and v["exact_P0_unit_certified"] is True
    assert v["source_complete146_space"]==D0["complete_normal146_space"]
    assert v["section_defined_over_original_K"] is True and v["original_scalar_not_rescaled"] is True
    local=own(v["source_complete146_P0_values"])
    assert local["source_complete_normal146_space"]==D0["complete_normal146_space"]
    assert local["source_original_P0_functional"]==inputs["P0_leading_row"]
    assert local["original_P0_functional_recomputed"] is False
    assert len(local["normal_V3_P0_values_mod_prime"])==146
    assert local["first_unit_column"]==v["selected_original_column"]
    assert v["actual_value_at_original_P0_mod_prime"]==local["normal_V3_P0_values_mod_prime"][local["first_unit_column"]]
    assert 0<v["actual_value_at_original_P0_mod_prime"]<P
    assert w["trial"]==DK["accepted_second_anchor_integer"]
    assert w["exact_section_definition"]["integer_parameter"]==w["trial"]
    assert w["exact_section_definition"]["exponents"]==[0,145]
    assert w["original_scalar_not_rescaled"] is True
    products(DK["source_v_products"],DK["source_exact_v"])
    products(DK["source_w_products"],DK["source_exact_w"])
    second=relation(DK["source_complete_relation_kernel"],962,418)
    finalspace=projection(DK["complete_normal418_space"],DK["source_complete_relation_kernel"],418)
    assert second["exact_complete_space_definition"]["K_fixed_relation_basis_by_unique_free_coordinate_identity"] is True
    assert finalspace["exact_RR_space"]["K_fixed_by_canonical_relation_and_projection"] is True
    marked=own(cert["marked_original_principal_QK"])
    assert marked["source_original_QN"]==inputs["original_QN"]
    assert marked["source_unscaled_S0"]==D0["source_unscaled_S0"]
    assert marked["source_unscaled_exact_v"]==DK["source_exact_v"]
    assert marked["source_complete_D0_certificate"]==cert["complete_first_residual_certificate"]
    assert marked["source_complete_DK_certificate"]==cert["complete_K_defined_degree272_certificate"]
    assert marked["complete_normal146_space"]==D0["complete_normal146_space"]
    assert marked["complete_normal418_space"]==DK["complete_normal418_space"]
    assert marked["source_original_t_frame"]==inputs["t_frame"]
    assert marked["exact_class_identity"]=="T0=(DK-H)+div(QK)"
    assert marked["QK_defined_over_original_K"] is True and marked["DK_defined_over_original_K"] is True
    assert marked["D0_and_DK_avoid_original_P0"] is True
    assert marked["actual_QK_rho_order"]==marked["actual_QK_t_order"]==-8435
    assert marked["actual_original_t_over_rho_mod_prime"]==354813668
    assert marked["actual_original_t_scaling_power"]==8435
    assert 0<marked["actual_QK_rho_leading_mod_prime"]<P and 0<marked["actual_QK_t_leading_mod_prime"]<P
    assert marked["positive_QN_and_positive_c8435_retained"] is True
    assert marked["original_unscaled_sections_and_tau_frames_preserved"] is True
    assert marked["original_t_or_QN_jets_recomputed"] is False
    assert marked["no_prime41_unit_claim_from_auxiliary_unit"] is True
    dag=marked["exact_principal_DAG"]
    assert [node["id"] for node in dag]==["QN","w0","S0","v","QK"]
    assert dag[0]["source_original_QN"]==inputs["original_QN"]
    assert dag[1]["normal_coordinates_already_mean_section_over_tau3"] is True
    assert dag[2]["operation"]=="positive_multiply" and dag[2]["left"]=="QN" and dag[2]["right"]=="w0"
    assert dag[3]["normal_coordinates_already_mean_section_over_tau3"] is True
    assert dag[4]["operation"]=="divide" and dag[4]["numerator"]=="S0" and dag[4]["denominator"]=="v"
    assert dag[4]["extra_tau_power"]==0
    assert cert["actual_D0_degree"]==544 and cert["actual_DK_degree"]==272
    assert cert["actual_complete_H0_3H_minus_D0_dimension"]==146
    assert cert["actual_complete_H0_3H_minus_DK_dimension"]==418
    for key in ("original_K_defined_degree272_representative_certified",
                "original_K_defined_marked_principal_certified","canonical_K_fixed_relation_bases_certified",
                "full_seven_whole_fibres_for_V6_not_six_fibre_support_assumption"):
        assert cert[key] is True
    for key in ("QN_units_in_all_seven_fibres_required",
                "old_flips_QN_K_basis_Krylov_jets_or_V3_evaluations_recomputed",
                "characteristic_zero_coefficients_reconstructed",
                "nonp_Hecke_support_Picard_principality_connection_period_or_height_computed"):
        assert cert[key] is False

def verify(item,out):
    out=Path(out)
    full=read(out/MANIFEST)
    assert full["result"]==RESULT
    entries={row["file"]:plain(row) for row in full["files"]}
    assert len(entries)==len(full["files"])
    for name,row in entries.items():
        assert name==row["file"]
        bound(out,row)
    reference=read(out/REFERENCE)
    assert reference["result"]==RESULT and plain(reference)==spec(out/MANIFEST)
    run=read(out/"run-receipt.json")
    assert run["result"]==RESULT
    assert run["core_sha256"]==item["core_sha256"] and run["wrapper_sha256"]==item["wrapper_sha256"]
    assert full["source_commit"]==run["source_commit"]
    assert str(full["workflow_run_id"])==str(run["workflow_run_id"])
    if not all(name in entries for name in ("public-actions-input.json",INVENTORY,INPUT_RECEIPT,BUNDLE)):
        assert run["complete"] is False and run["process_exit_code"]!=0
        return {"result":RESULT,"complete":False,"failure_before_complete_input_carrier":True,
                "process_exit_code":run["process_exit_code"],"error":run["error"],
                "source_manifest":spec(out/MANIFEST),"new_mathematics_executed_in_IO_verification":False}
    retained,sources,inputs,source_check=prepare(item,out,allow_download=False)
    tag=expected_tag(item,sources,inputs)
    initial=read(out/"public-actions-input.json")
    assert initial["result"]==RESULT and initial["source_commit"]==run["source_commit"]
    assert str(initial["workflow_run_id"])==str(run["workflow_run_id"])
    assert initial["core_sha256"]==item["core_sha256"] and initial["wrapper_sha256"]==item["wrapper_sha256"]
    assert initial["job"]==item
    assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
    assert initial["source_inventory"]==entries[INVENTORY]
    assert initial["expanded_job"]==entries[EXPANDED]
    expanded=read(out/EXPANDED)
    assert expanded["sources"]==sources and expanded["inputs"]==inputs
    assert expected_tag(expanded,sources,inputs)==tag
    stages={};currents={};inventories={}
    for name,row in entries.items():
        if not name.startswith(PREFIX) or not name.endswith(".json.gz"):
            continue
        value=read(out/name)
        assert value["result"]==RESULT and value["configuration"]==tag
        if name==PREFIX+"current.json.gz":
            assert value["complete"] is False
            currents[name]=row
        else:
            assert value["complete"] is True
            if "stage-manifest" in name:
                inventories[name]=row
                refs={ref["file"]:plain(ref) for ref in value["files"]}
                assert len(refs)==len(value["files"])
                for filename,ref in refs.items():
                    assert entries[filename]==ref and filename!=name
            else:
                stages[name]=row
    core=None
    if run["core_receipt_sha256"] is not None:
        assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
        core=read(out/"core-receipt.json")
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        if core.get("configuration") is not None:
            assert core["configuration"]==tag
        if core.get("configuration_sha256") is not None:
            assert core["configuration_sha256"]==fingerprint(tag)
    else:
        assert run["complete"] is False
    cert=None
    if FINAL in entries:
        cert=read(out/FINAL)
        assert cert["result"]==RESULT and cert["configuration"]==tag
        if cert["complete"] is True:
            assert run["complete"] is True and run["process_exit_code"]==0
            assert core is not None and core["complete"] is True
            assert core["certificate_sha256"]==entries[FINAL]["sha256"]
            manifest_ref=plain(cert["stage_manifest"])
            assert entries[manifest_ref["file"]]==manifest_ref
            inventory=read(bound(out,manifest_ref))
            assert inventory["result"]==RESULT and inventory["configuration"]==tag
            for row in inventory["files"]:
                assert entries[row["file"]]==plain(row)
            assert {row["file"]:plain(row) for row in inventory["files"]}==stages
            assert len(inventory["files"])==len(stages)
            if cert.get("resume_state") is not None:
                assert entries[cert["resume_state"]["file"]]==plain(cert["resume_state"])
            verify_complete_final(item,out,entries,tag,cert,sources,inputs)
        else:
            assert run["complete"] is False
            # A false endpoint is historical: newer atomic stages/current may have advanced.
    if run["complete"]:
        assert cert is not None and cert["complete"] is True
    return {"result":RESULT,"complete":run["complete"],"process_exit_code":run["process_exit_code"],
            "core_receipt_present":core is not None,"outer_timeout":run["outer_timeout"],
            "source_manifest":spec(out/MANIFEST),"certificate":entries.get(FINAL),
            "actual_complete_stage_count":len(stages),"actual_current_count":len(currents),
            "source_inventory":entries[INVENTORY],"retained_source_bundle":entries[BUNDLE],
            "source_check":source_check,
            "complete_direction_certificates":cert.get("complete_direction_certificates",{}) if cert else {},
            "original_K_defined_degree272_representative_certified":cert.get("original_K_defined_degree272_representative_certified",False) if cert else False,
            "original_K_defined_marked_principal_certified":cert.get("original_K_defined_marked_principal_certified",False) if cert else False,
            "new_mathematics_executed_in_IO_verification":False}

def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("compute","verify"))
    parser.add_argument("--request",type=Path,default=REQUEST)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    item=read(args.request);guard(item,args.request)
    if args.mode=="verify":
        print("R900_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
        return 0
    code=compute(item,args.output,args.request)
    try:
        print("R900_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
    except Exception:
        traceback.print_exc()
        if code==0:
            code=1
    return code

if __name__=="__main__":
    raise SystemExit(main())
