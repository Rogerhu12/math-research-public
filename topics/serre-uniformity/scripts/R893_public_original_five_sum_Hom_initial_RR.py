#!/usr/bin/env python3
"""R893 standard-library transport and continuation of original five initial RR kernels.
Only hash, schema, archive and source-identity operations occur in this wrapper.
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
RESULT="R893-original-five-sum-Hom-complete-initial-RR"
FINAL="p41-original-five-sum-Hom-complete-initial-RR-certificate.json"
PREFIX="R893-"
CORE="R893_original_five_sum_Hom_initial_RR.py"
REQUEST=TOPIC/"notes/R893-five-sum-Hom-initial-RR-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R893-retained-original-inputs.tar.gz"
INVENTORY="R893-original-source-inventory.json"
INPUT_RECEIPT="R893-retained-inputs-receipt.json"
EXPANDED="R893-expanded-job.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
MANDATORY=("R880","R877","R809","R849","R827","R885")
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
DEGREES=[2970,1674,1800,3024,3339]
POWERS=[12,8,8,13,14]
FIBRES=[23,15,15,25,27]
RESIDUAL_DEGREES=[294,502,376,512,469]
DIMENSIONS=[168,376,250,386,343]
PADDING=[250,42,168,32,75]
FIELD_BASIS="b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
IO=None

STRATEGY={
 "original_curve":"original Y of genus127, level82, original minus3 descent",
 "original_Hom_words":["1+T^"+str(j) for j in range(1,6)],
 "prime":P,"original_s_root":99932770,"original_zeta_root":549966761,
 "original_integral_B_root":3197390,"canonical_free_column":1186,
 "normal_basis_degrees":EPS,"original_sigma_branch_order":[0,6,1,2,4,3,5],
 "Cj_semantics":"theta*U_j/tau^4=h_Tjf/h_f times C0; original rho phase already included",
 "Cj_scale":"each original field numerator/denominator times its own rational scale exactly once",
 "normal_derivative":"Gamma*a+Mg*partial_z(a), original tau operators",
 "same_target_conjugate":"C=rho_j^-3*sigma^j(A), D=sigma^j(B)",
 "single_denominator":"Q=B*D^3*(Cj*(C^2-bD^2)*W-C0*(A^2-bB^2)*Wj)^3",
 "single_numerator":"-A*D^3*Delta^3+Xi*D^2*Delta^2*(2*S+R)-Xi^3*C0^3*F^2*Wj^3",
 "common_homogeneous_weight":98,"direct_sigma_formula_weight":95,
 "true_weight98_sigma_transport":"multiply direct sigma formula by t^3; normal beta_i by t^epsilon_i",
 "whole_fibre_dimension":272,"characteristic_polynomial":"completed original R885, never recomputed",
 "node_schedule":"least nonnegative integers, old source-bound Krylov points reused",
 "only_denominator_unit_test":"Q in the whole degree272 Artin algebra; no factor removal",
 "initial_powers":POWERS,"original_pole_degrees":DEGREES,
 "required_complete_fibres":FIBRES,"residual_degrees":RESIDUAL_DEGREES,
 "complete_initial_kernel_dimensions":DIMENSIONS,"future_padding":PADDING,
 "normal_basis_order":"(i,k), i=0..271, k=0..n-epsilon_i",
 "A_elimination":"three scalar Vandermonde lengths n+1,n,n-1",
 "Schur_sign":"H_complement-Lambda*H_selected; H=Y*E",
 "minor_selection":"left-to-right RREF pivots of S^t choose original rows, then RREF chooses columns",
 "kernel_coordinates":"all nonpivot normal columns are free identity; pivot=-minor^-1*free",
 "complete_checks":"all Schur rows, all N*272 original A-yB rows, free identity",
 "exact_output":"source-bound characteristic-zero unit-solve expression and its actual modular reduction",
 "initial_nodes_are_not_generic_V2n_injection":True,
 "marked_pair_padding_or_five_Lj128_computed":False,
 "budget_node_limit_requested_directions_and_transport_excluded_from_identity":True
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
    d=importlib.util.spec_from_file_location("R893_frozen_stdlib_Range",path)
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
    assert 27<=item["maximum_node_attempts"]<P
    assert item["requested_directions"]==sorted(set(item["requested_directions"]))
    assert item["requested_directions"] and all(1<=j<=5 for j in item["requested_directions"])
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert set(MANDATORY)<=set(item["source_artifacts"])
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
    assert fingerprint(tag)==source["configuration_sha256"]
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
    assert len(value)==m and all(len(row)==n for row in value)

def original_pins(item,sources,inputs=None):
    assert set(sources)==set(item["source_artifacts"])
    assert set(MANDATORY)<=set(sources)
    for group,prior in item["source_artifacts"].items():
        actual=sources[group]
        same_source(prior,actual)
        if prior.get("certificate") is not None:
            assert plain(prior["certificate"])==plain(actual["certificate"])
        elif prior.get("certificate_name") is not None:
            assert actual["certificate"]["file"]==prior["certificate_name"]
        else:
            assert plain(prior["configuration_stage"])==plain(actual["configuration_stage"])
            assert prior["accepted_process_exit_codes"]==actual["accepted_process_exit_codes"]
    if inputs is not None:
        required={"global_DAG","original_place","seven_normal_inputs","zero_branch_A","zero_branch_B",
            "other_normal_pairs","original_W","characteristic","original_Krylov_points",
            "original_characteristic_nodes","g_index","Gamma_index","operator_identity","S5_index",
            "C_indexes","base_B_derivative_C_column","C_basis_reduction","completed_B_derivatives"}
        assert set(inputs)==required
        assert len(inputs["other_normal_pairs"])==len(inputs["C_indexes"])==6
        assert len(inputs["original_Krylov_points"])==len(inputs["original_characteristic_nodes"])==8
        for key,row in item.get("input_pins",{}).items():
            assert plain(inputs[key])==plain(row)
        assert len(inputs["completed_B_derivatives"])==len(item.get("completed_B_derivative_inputs",[]))
        for actual,expected in zip(inputs["completed_B_derivatives"],item.get("completed_B_derivative_inputs",[])):
            assert actual["sigma_power"]==expected["sigma_power"]
            assert actual["source"]["source_group"]==expected["source_group"]
            assert plain(actual["source"])==plain(expected["stage"])

def source_review(item,retained,sources,inputs):
    original_pins(item,sources,inputs)
    tags={};certificates={}
    for group,source in sources.items():
        folder=Path(retained)/group;entries=entry_map(folder,source)
        for name,row in source["files"].items():
            assert entries[name]==plain(row);bound(folder,row)
        cert,tag,initial=metadata(group,folder,source,entries)
        tags[group]=tag;certificates[group]=cert
    def stage(ref):
        group=ref["source_group"];row=plain(ref)
        assert sources[group]["files"][row["file"]]==row
        value=read(bound(Path(retained)/group,row))
        assert value["complete"] is True and value["configuration"]==tags[group]
        return value
    def own(group,row):
        return stage(group_ref(group,row))
    G=stage(inputs["global_DAG"])
    assert plain(certificates["R849"]["exact_expression_DAG"])==plain(inputs["global_DAG"])
    assert G["global_y_exact_unit_expression_defined"] is True
    assert G["five_original_addition_pole_ideals_as_fractional_DAGs_certified"] is True
    assert G["all_three_minor_formulas_are_exact_DVR_ideal_equalities"] is True
    same_source(tags["R849"]["source_identities"]["R809"],sources["R809"])
    for j in range(1,6):
        g=G["five_original_polar_and_eta_outputs"][str(j)]
        assert g["original_Hom_word"]=="1+T^"+str(j)
        assert g["original_map_degree"]==DEGREES[j-1]
        assert set(g["global_pole_ideals"])=={"tau","sigma"}
    seven=stage(inputs["seven_normal_inputs"])
    assert plain(certificates["R880"]["seven_Galois_normal_inputs"])==plain(inputs["seven_normal_inputs"])
    assert seven["all_seven_original_Galois_normal_inputs_certified"] is True
    assert certificates["R880"]["all1380_by12_original_coordinates_verified"] is True
    assert plain(seven["source_original_global_DAG"])==plain(inputs["global_DAG"])
    order=seven["ordered_original_sigma_powers"]
    assert [row["sigma_power"] for row in order]==list(range(7))
    assert [row["original_branch"] for row in order]==[0,6,1,2,4,3,5]
    assert plain(order[0]["source_original_A_normal"])==plain(inputs["zero_branch_A"])
    assert plain(order[0]["source_original_B_normal"])==plain(inputs["zero_branch_B"])
    assert plain(certificates["R877"]["normal_A"])==plain(inputs["zero_branch_A"])
    for key in ("zero_branch_A","zero_branch_B"):
        v=stage(inputs[key]);dimensions(v["vector_coefficients_mod_prime"],6,272)
        assert v["prime"]==P and v["original_branch"]==0 and v["canonical_free_column"]==1186
        assert v["all1380_original_short_coordinates_verified"] is True
        assert v["normal_basis_degrees"]==EPS and v["regular_degree_bound"]==5
    for j,ref in enumerate(inputs["other_normal_pairs"],1):
        assert plain(ref)==plain(order[j]["source_original_normal_pair"])
        pair=stage(ref)
        assert pair["prime"]==P and pair["sigma_power"]==j
        assert pair["original_branch"]==order[j]["original_branch"]
        assert pair["roots_B_s"]==order[j]["roots_B_s"]
        assert pair["abstract_p_integral_original_normal_lifts_certified"] is True
        assert pair["all1380_original_coordinates_for_each_vector_verified"] is True
        dimensions(pair["A_vector_coefficients_mod_prime"],6,272)
        dimensions(pair["B_vector_coefficients_mod_prime"],6,272)
    place=stage(inputs["original_place"])
    assert place["prime"]==P and place["original_branch"]==0
    assert place["original_zeta_root"]==549966761 and place["original_s_root"]==99932770
    assert place["original_integral_B_root"]==3197390
    assert place["original_field"]==G["original_field"]
    W=stage(inputs["original_W"])
    assert W["prime"]==P and W["original_rational_denominators_all_units"] is True
    assert len(W["W_coefficients_mod_prime"])==4
    for coefficient in W["W_coefficients_mod_prime"]:
        dimensions(coefficient,272,272)
    chi=stage(inputs["characteristic"])
    assert plain(certificates["R885"]["characteristic_relation"])==plain(inputs["characteristic"])
    assert chi["prime"]==P and chi["exact_original_modular_characteristic_polynomial_certified"] is True
    assert chi["all273_nodes_for_all273_T_coefficients_verified"] is True
    assert plain(chi["source_original_W"])==plain(inputs["original_W"])
    assert len(chi["coefficient_polynomials_ascending_z"])==273
    for a,(point_ref,node_ref) in enumerate(zip(inputs["original_Krylov_points"],inputs["original_characteristic_nodes"])):
        point=stage(point_ref);node=stage(node_ref)
        assert point["prime"]==P and point["z0"]==a and point["usable"] is True
        assert point["both_inverse_products_verified"] is True and point["actual_cyclic_rank"]==272
        assert plain(point["source_original_W"])==plain(inputs["original_W"])
        assert node["z_value"]==a and node["full_K_times_relation_equals_k272"] is True
        assert plain(node["source_original_Krylov"])==plain(point_ref)
        dimensions(point["Krylov_matrix_mod_prime"],272,272)
        dimensions(point["inverse_Krylov_matrix_mod_prime"],272,272)
    op=stage(inputs["operator_identity"])
    for target,key,count in (("g","g_index",6),("Gamma","Gamma_index",5)):
        index=stage(inputs[key]);assert index["target"]==target and index["chart"]=="tau"
        assert index["prime"]==P and index["normal_basis_degrees"]==EPS
        assert index["all_weighted_support_zeros_verified"] is True
        assert index["original_true_operator_reduction_certified"] is True
        assert plain(op["operator_indexes"][target]["tau"])==plain(inputs[key])
        assert len(index["row_blocks"])==17
        for first,row in zip(range(0,272,16),index["row_blocks"]):
            data=own("R827",row)
            assert data["target"]==target and data["chart"]=="tau" and data["prime"]==P
            assert (data["row_first"],data["row_stop"])==(first,min(first+16,272))
            assert data["original_weighted_support_verified"] is True
            assert len(data["coefficient_matrices_low_to_high"])==count
            for coefficient in data["coefficient_matrices_low_to_high"]:
                dimensions(coefficient,data["row_stop"]-first,272)
    S5=stage(inputs["S5_index"])
    assert S5["dimension"]==1234 and S5["normal_basis_degrees"]==EPS
    assert S5["integer_scale"]=="13744803133596058624"
    assert len(S5["basis_rows"])==1234
    assert plain(certificates["R809"]["S5_basis_index"])==plain(inputs["S5_index"])
    assert certificates["R809"]["coefficient_field_basis"]==FIELD_BASIS
    for j,row in enumerate(inputs["C_indexes"]):
        index=stage(row)
        assert plain(certificates["R809"]["normal_vectors"]["C"+str(j)])==plain(row)
        assert index["target"]=="C"+str(j) and index["regular_degree_bound"]==4
        assert index["normal_function"]=="theta*U_"+str(j)+"/tau^4"
        assert index["all14_original_field_columns_retained"] is True
        assert index["weighted_polynomial_support_verified"] is True
        assert index["literal_tau_factor_highest_S5_coefficients_zero"] is True
        assert plain(index["S5_basis_index"])==plain(inputs["S5_index"])
        assert len(index["coordinate_groups"])==2
        covered=[]
        for group in index["coordinate_groups"]:
            g=own("R809",group)
            assert g["target"]=="C"+str(j) and g["target_configuration"]==index["target_configuration"]
            assert g["target_configuration_sha256"]==fingerprint(g["target_configuration"])
            assert g["coefficient_field_basis"]==FIELD_BASIS
            assert g["all1380_original_coordinates_verified"] is True
            assert g["original_field_and_scalar_normalizations_preserved"] is True
            dimensions(g["coordinate_numerators"],1234,7)
            assert len(g["column_denominators"])==len(g["original_target_rational_scales"])==7
            covered.extend(g["column_indices"])
        assert covered==list(range(14))
    CB=stage(inputs["base_B_derivative_C_column"]);C=stage(inputs["C_basis_reduction"])
    assert CB["chart"]=="tau" and CB["derivative_order"]==1
    assert CB["original_B_times_normal_basis_index"]==0
    assert CB["exact_monic_degree20_division_and_original_column_multiplyback_verified"] is True
    assert plain(CB["source_complete_C"])==plain(inputs["C_basis_reduction"])
    assert len(CB["column_coefficients_in_original_C_basis"])==272
    tau=C["charts"]["tau"] if "charts" in C else C["tau"]
    assert len(tau["q_polynomials"])==271 and len(tau["P_polynomial"])==21
    for entry in inputs["completed_B_derivatives"]:
        j=entry["sigma_power"];v=stage(entry["source"])
        assert 1<=j<=5 and v["sigma_power"]==j and v["prime"]==P
        assert v["original_branch"]==order[j]["original_branch"]
        assert plain(v["source_original_B"])==plain(inputs["other_normal_pairs"][j-1])
        assert v["first_column_copied_from_actual_completed_derivative_matrices"] is True
        assert v["additional_derivative_arithmetic_computed"] is False
        dimensions(v["delta_B_coefficients_mod_prime"],8,272)
        dimensions(v["delta2_B_coefficients_mod_prime"],10,272)
    return {"result":RESULT,"source_identities":{g:identity(sources[g]) for g in sorted(sources)},
        "selected_file_counts":{g:len(sources[g]["files"]) for g in sorted(sources)},
        "selected_file_count":sum(len(s["files"]) for s in sources.values()),
        "actual_sigma_branch_order":[row["original_branch"] for row in order],
        "old_original_Krylov_nodes":list(range(8)),"original_C_group_count":12,
        "original_g_and_Gamma_row_block_counts":[17,17],
        "completed_B_derivative_sigma_powers":[entry["sigma_power"] for entry in inputs["completed_B_derivatives"]],
        "base_B_derivative_source":"completed C-column with exact original monic C basis transport",
        "all_selected_original_bytes_and_configurations_verified":True,
        "original_rational_scales_not_applied_by_IO_wrapper":True,
        "old_mathematical_stages_recomputed":False,"new_mathematics_executed":False}

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R893";retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (BUNDLE,INVENTORY,INPUT_RECEIPT)):
        inventory=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        assert receipt["source_inventory"]==spec(out/INVENTORY)
        assert receipt["source_bundle"]==spec(out/BUNDLE)
        sources=inventory["sources"];inputs=inventory["inputs"]
        original_pins(item,sources,inputs)
        unpack(out/BUNDLE,retained,sources)
        review=source_review(item,retained,sources,inputs)
        return retained,sources,inputs,review
    assert allow_download,"A complete same-source retained input carrier is required for offline verification."
    work=out.parent/"R893-download";work.mkdir(parents=True,exist_ok=True)
    handles={}
    try:
        # R885's immutable old-source carrier is used only as an IO transport.
        # No R885 mathematics or old inverse is called by this wrapper.
        poly=Handle("R885",item,retained,work);handles["R885"]=poly
        transport=item["R827_transport"]
        for key in ("source_inventory","retained_inputs_receipt","package"):
            row=plain(transport[key]);assert poly.entries[row["file"]]==row
            poly.take([row["file"]])
        old_inventory=read(poly.folder/transport["source_inventory"]["file"])
        old_receipt=read(poly.folder/transport["retained_inputs_receipt"]["file"])
        assert old_receipt["source_inventory"]==plain(transport["source_inventory"])
        assert old_receipt["source_bundle"]==plain(transport["package"])
        old_source=old_inventory["source_R827"]
        same_source(old_source,item["source_artifacts"]["R827"])
        assert identity(old_source)==poly.tag["source_R827"]
        assert old_inventory["inputs"]==poly.tag["inputs"]
        extract_bound_group(poly.folder/transport["package"]["file"],retained,"R827",old_source)
        # The original individual files, not a duplicate nested bundle, are kept.
        poly.selected.pop(transport["package"]["file"])
        bootstrap={"completed_POLY_identity":identity(poly.finish_source()),
            "source_inventory":plain(transport["source_inventory"]),
            "retained_inputs_receipt":plain(transport["retained_inputs_receipt"]),
            "package":plain(transport["package"]),
            "original_R827_identity":identity(old_source),
            "all_old_carrier_bytes_and_individual_members_verified":True,
            "duplicate_nested_carrier_retained":False,"old_mathematics_recomputed":False}
        for group in item["source_artifacts"]:
            if group!="R885":
                handles[group]=Handle(group,item,retained,work)
        seven_handle=handles["R880"];seven=seven_handle.stage(seven_handle.certificate["seven_Galois_normal_inputs"])
        global_handle=handles["R849"];global_handle.stage(global_handle.certificate["exact_expression_DAG"])
        for group in ("R880","R877","R849"):
            if "source_audit" in handles[group].certificate:
                handles[group].stage(handles[group].certificate["source_audit"])
        ordered=seven["ordered_original_sigma_powers"]
        assert len(ordered)==7 and [row["sigma_power"] for row in ordered]==list(range(7))
        A=ordered[0]["source_original_A_normal"];B=ordered[0]["source_original_B_normal"]
        handles["R877"].stage(A);r827=handles["R827"];r827.stage(B)
        assert plain(handles["R877"].certificate["normal_A"])==plain(A)
        pair_refs=[]
        for row in ordered[1:]:
            ref=row["source_original_normal_pair"];seven_handle.stage(ref);pair_refs.append(seven_handle.ref(ref))
        original=old_inventory["inputs"]
        assert len(original["Krylov_points"])==8
        W=original["W_reduction"];place=original["place_audit"]
        r827.stage(W);r827.stage(place)
        for row in original["Krylov_points"]:
            r827.stage(row)
        identity_name="R827-complete-short-operator-identities-and-sigma-transport.json.gz"
        operators=r827.named(identity_name)
        op_refs={}
        for target in ("g","Gamma"):
            ref=operators["operator_indexes"][target]["tau"]
            index=r827.stage(ref);op_refs[target]=r827.ref(ref)
            assert len(index["row_blocks"])==17
            for row in index["row_blocks"]:
                r827.stage(row)
        base_derivative_name="R827-tau-layer-001-C-column-000.json.gz"
        column=r827.named(base_derivative_name)
        r827.stage(column["source_complete_C"])
        chi_ref=poly.certificate["characteristic_relation"];chi=poly.stage(chi_ref)
        assert len(chi["source_node_stages"])==273
        nodes=[]
        for a,ref in enumerate(chi["source_node_stages"][:8]):
            node=poly.stage(ref);assert node["z_value"]==a
            nodes.append(poly.ref(ref))
        r809=handles["R809"];S5ref=r809.certificate["S5_basis_index"];r809.stage(S5ref)
        Crefs=[]
        for j in range(6):
            ref=r809.certificate["normal_vectors"]["C"+str(j)]
            index=r809.stage(ref);Crefs.append(r809.ref(ref))
            assert len(index["coordinate_groups"])==2
            for row in index["coordinate_groups"]:
                r809.stage(row)
        derivative_inputs=[]
        for entry in item.get("completed_B_derivative_inputs",[]):
            group=entry["source_group"];ref=plain(entry["stage"])
            data=handles[group].stage(ref)
            assert data["sigma_power"]==entry["sigma_power"] and 1<=entry["sigma_power"]<=5
            derivative_inputs.append({"sigma_power":entry["sigma_power"],"source":group_ref(group,ref)})
        inputs={"global_DAG":global_handle.ref(global_handle.certificate["exact_expression_DAG"]),
            "original_place":r827.ref(place),
            "seven_normal_inputs":seven_handle.ref(seven_handle.certificate["seven_Galois_normal_inputs"]),
            "zero_branch_A":handles["R877"].ref(A),"zero_branch_B":r827.ref(B),
            "other_normal_pairs":pair_refs,"original_W":r827.ref(W),
            "characteristic":poly.ref(chi_ref),
            "original_Krylov_points":[r827.ref(row) for row in original["Krylov_points"]],
            "original_characteristic_nodes":nodes,"g_index":op_refs["g"],"Gamma_index":op_refs["Gamma"],
            "operator_identity":r827.ref(r827.entries[identity_name]),"S5_index":r809.ref(S5ref),
            "C_indexes":Crefs,"base_B_derivative_C_column":r827.ref(r827.entries[base_derivative_name]),
            "C_basis_reduction":r827.ref(column["source_complete_C"]),
            "completed_B_derivatives":derivative_inputs}
        sources={group:handle.finish_source() for group,handle in handles.items()}
        original_pins(item,sources,inputs)
        review=source_review(item,retained,sources,inputs)
        transports={group:handle.receipt() for group,handle in handles.items()}
        transports["R827"]["completed_R885_original_source_carrier"]=bootstrap
        save(out/INVENTORY,{"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
            "transports":transports,"old_GALOIS_or_global_large_carriers_read":False,
            "new_mathematics_executed":False})
        pack(retained,sources,out/BUNDLE)
        save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,
            "source_inventory":spec(out/INVENTORY),"source_bundle":spec(out/BUNDLE),
            "source_identities":{g:identity(sources[g]) for g in sorted(sources)},
            "selected_file_counts":{g:len(sources[g]["files"]) for g in sorted(sources)},
            "all_original_selected_bytes_and_stage_configurations_verified":True,
            "old_normal_solves_derivative_operators_characteristic_or_inverses_recomputed":False,
            "new_mathematics_executed":False})
        print("R893_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,sources,inputs,review
    finally:
        for handle in handles.values():
            handle.close()

def restore(item,out):
    resume=item.get("resume")
    if not resume:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R893-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R893-resume-archive",whole=False)
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
    assert cert["prime"]==P and cert["p"]==41
    assert cert["requested_directions"]==item["requested_directions"]
    completed=cert["completed_directions"]
    assert completed==sorted(set(completed))
    assert set(item["requested_directions"])<=set(completed)
    assert cert["requested_complete_initial_RR_spaces_certified"] is True
    assert cert["all_five_complete_initial_RR_spaces_certified"] is (len(completed)==5)
    assert cert["initial_RR_powers"]==POWERS and cert["original_pole_degrees"]==DEGREES
    assert cert["initial_RR_dimensions"]==DIMENSIONS and cert["future_padding_to_544"]==PADDING
    for key in ("characteristic_zero_kernel_coordinates_reconstructed",
                "original_c0_marked_pairs_or_padding_spaces_computed",
                "original_Lj128_or_Hecke_Picard_support_computed",
                "connection_period_or_height_computed"):
        assert cert[key] is False
    def own(row):
        row=plain(row);assert entries[row["file"]]==row
        data=read(bound(out,row))
        assert data["result"]==RESULT and data["configuration"]==tag and data["complete"] is True
        return data
    audit=own(cert["source_audit"])
    assert audit["source_original_global_DAG"]==inputs["global_DAG"]
    assert audit["original_pole_degrees"]==DEGREES
    assert audit["source_completed_B_derivatives"]==inputs["completed_B_derivatives"]
    assert audit["original_positive_Hom_words_phase_and_twist_preserved"] is True
    assert set(cert["complete_initial_RR_certificates"])=={str(j) for j in completed}
    for j in completed:
        data=own(cert["complete_initial_RR_certificates"][str(j)])
        n=POWERS[j-1];r=DIMENSIONS[j-1];d=272*n-126;count=FIBRES[j-1]
        assert data["j"]==j and data["prime"]==P and data["original_Hom_word"]=="1+T^"+str(j)
        assert data["ordinary_power"]==n and data["original_pole_degree"]==DEGREES[j-1]
        assert data["complete_kernel_dimension"]==r and data["independent_original_global_dimension"]==r
        for key in ("all_original_Schur_rows_verified","all_complete_fibre_original_A_minus_yB_relations_verified",
                    "complete_initial_RR_space_certified","actual_arrays_are_only_modular_reductions",
                    "exact_unit_solve_expression_certified"):
            assert data[key] is True
        for key in ("characteristic_zero_coordinates_reconstructed","original_c0_marked_pair_computed",
                    "later_V2n_injection_assumed_from_initial_fibres",
                    "future_threeH_RR_padding_or_complete418_space_computed",
                    "original_Lj128_Picard_support_or_height_computed"):
            assert data[key] is False
        selected=own(data["source_complete_fibres"])
        assert selected["j"]==j and selected["whole_fibre_count"]==count
        nodes=selected["nodes"];assert len(nodes)==count and nodes==sorted(set(nodes))
        assert selected["complete_evaluation_length"]==272*count
        assert selected["complete_global_section_evaluation_injective"] is True
        assert selected["all_denominators_units_in_the_whole_fibres"] is True
        assert selected["residue_field_factors_or_multiplicities_removed"] is False
        assert len(selected["full_fibre_sources"])==count
        for a,row in zip(nodes,selected["full_fibre_sources"]):
            val=own(row)
            assert val["j"]==j and val["z0"]==a and val["whole_fibre_unit"] is True
            assert val["whole_original_Q_times_inverse_equals_one"] is True
            assert val["all272_original_Q_times_y_equals_P_verified"] is True
            assert val["full_unreduced_polynomial_Bezout_identity_verified"] is True
            assert val["factors_or_nilpotents_removed"] is False
            assert val["single_F_factor_cancelled_exactly_once"] is True
            assert val["extra_C0_F_or_Wj_unit_conditions_imposed"] is False
            assert val["common_section_weight"]==98 and val["original_sigma_extra_frame_power"]==3
            for key in ("P_coefficients_ascending_w","Q_coefficients_ascending_w",
                        "Q_inverse_coefficients_ascending_w","y_coefficients_ascending_w",
                        "y_normal_coordinates_mod_prime"):
                assert len(val[key])==272
            assert len(val["complete_original_algebra_modulus"])==273
        Schur=own(data["source_complete_Schur"])
        assert Schur["Schur_shape"]==[272*count-d,d]
        assert Schur["independent_characteristic_zero_rank"]==DEGREES[j-1]
        assert Schur["independent_complete_kernel_dimension"]==r
        assert Schur["nodes"]==nodes and len(Schur["row_blocks"])==17
        assert len(Schur["original_column_mapping"])==d
        assert len(Schur["complete_row_labels"])==272*count-d
        total_rows=0
        for row in Schur["row_blocks"]:
            block=own(row)
            assert block["j"]==j and block["column_count"]==d
            assert block["source_three_scalar_blocks"]==Schur["source_three_scalar_blocks"]
            values=block["Schur_matrix_rows_mod_prime"]
            dimensions(values,len(block["row_labels_output_component_and_node_ordinal"]),d)
            total_rows+=len(values)
        assert total_rows==272*count-d
        minor=own(data["source_original_unit_minor"])
        e=DEGREES[j-1]
        assert minor["matrix_shape"]==[e,e] and len(minor["row_indices"])==len(minor["column_indices"])==e
        assert 0<minor["actual_determinant_mod_prime"]<P
        assert minor["characteristic_zero_selected_minor_is_a_DVR_unit"] is True
        assert minor["source_matrix_characteristic_zero_rank_already_known"]==e
        assert minor["all_remaining_characteristic_zero_rows_follow_from_equal_rank"] is True
        A=own(data["complete_A_kernel"]);B=own(data["complete_B_kernel"])
        dimensions(A["A_coefficients_mod_prime"],d,r)
        dimensions(B["B_coefficients_mod_prime"],d,r)
        assert B["all_original_Schur_rows_times_full_kernel_zero"] is True
        assert B["canonical_free_identity_verified"] is True
        assert B["source_unit_minor"]==data["source_original_unit_minor"]
        assert B["complete_kernel_dimension"]==r and len(B["free_columns"])==r
        assert B["exact_unit_solve_expression"]["array_is_modular_reduction_not_expanded_characteristic_zero_coordinates"] is True
        assert len(A["source_complete_yB_fibre_values"])==count
        for a,row in zip(nodes,A["source_complete_yB_fibre_values"]):
            value=own(row)
            assert value["j"]==j and value["z0"]==a
            assert value["source_complete_B_kernel"]==data["complete_B_kernel"]
            dimensions(value["B_fibre_values_mod_prime"],272,r)
            dimensions(value["y_times_B_fibre_values_mod_prime"],272,r)
        assert len(data["all_original_fibre_relation_certificates"])==count
        for a,row in zip(nodes,data["all_original_fibre_relation_certificates"]):
            check=own(row)
            assert check["j"]==j and check["z0"]==a and check["checked_shape"]==[272,r]
            assert check["source_complete_A_kernel"]==data["complete_A_kernel"]
            assert check["source_complete_B_kernel"]==data["complete_B_kernel"]
            assert check["all272_times_complete_kernel_dimension_original_relations_zero"] is True
            assert check["complete_fibre_factors_or_multiplicities_removed"] is False
        assert data["all_original_fibre_rows_checked"]==272*count

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
            "completed_directions":cert.get("completed_directions",[]) if cert else [],
            "complete_initial_RR_certificates":cert.get("complete_initial_RR_certificates",{}) if cert else {},
            "all_five_complete_initial_RR_spaces_certified":cert.get("all_five_complete_initial_RR_spaces_certified",False) if cert else False,
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
        print("R893_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
        return 0
    code=compute(item,args.output,args.request)
    try:
        print("R893_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
    except Exception:
        traceback.print_exc()
        if code==0:
            code=1
    return code

if __name__=="__main__":
    raise SystemExit(main())
