#!/usr/bin/env python3
"""R890 stdlib source transport, same-source continuation and public driver.
No mathematics is performed or imported by this wrapper.
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
RESULT="R890-original-Ef-eight-flip-and-marked-frame"
FINAL="p41-original-Ef-eight-flip-and-marked-frame-certificate.json"
PREFIX="R890-"
CORE="R890_original_Ef_eight_flip_and_marked_frame.py"
REQUEST=TOPIC/"notes/R890-eight-flip-Ef-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R890-retained-original-inputs.tar.gz"
INVENTORY="R890-original-source-inventory.json"
INPUT_RECEIPT="R890-retained-inputs-receipt.json"
EXPANDED="R890-expanded-job.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
GROUPS=("R887","R880","R872","R883","R827")
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
P=1000000753
EPS=[0]+[1]*144+[2]*127
IO=None

CHAIN=(("A","D","D"),("B","A","H"),("C","B","D"),
       ("D2","X","X"),("E","D2","D2"),("F","Cstar","C"),
       ("G","F","E"),("DE","G","H"))
STRATEGY={
    "original_curve":"original genus127 Y, level82 and minus3 descent",
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "original_integral_B_root":3197390,"original_free_direction":1186,
    "normal_basis_degrees":EPS,"normal_V3_dimension":690,"complete_divisor_space_dimension":418,
    "old_fibres":[0,1,2,3,4,5,6],"complete_evaluation_length":1904,
    "degree6H":1632,"original_W_and_Krylov_inverses_recomputed":False,
    "product_image_dimension":962,"product_anchor_schedule":"original first-input kernel columns, in order",
    "product_rank_extension":"new residual Schur block, old selected span and inverse reused",
    "membership_anchors":["tau^3","sigma^3"],"full_membership_matrix_shape":[1884,690],
    "complete_U_dimension":146,"U_unit_selection":"first nonzero original P0 evaluation, no rescaling",
    "pencil_second_anchor":"sum(n^j*U_j), j0..145, positive integer n",
    "complete_pencil_matrix_shape":[1904,1380],"complete_relation_kernel_dimension":418,
    "projection":"second690 rows of complete kernel of [uV3,vV3]",
    "neutral_divisor":"div_H(tau), represented by tau V2 in original normal V3",
    "chain":[list(row) for row in CHAIN],
    "principal_recurrence":"Fnew=1/(q*Fa*Fb), q=u/tau^3",
    "target_class_coefficients_Cstar_Dstar_Dchi":[-1,3,4],
    "target_identity":"Ef-1206P0=(DE-H)+div(Qtilde*F_DE)",
    "original_rho_order":-1205,"original_t_leading":"rho_leading * original_c^1205",
    "old_three418_spaces_point_jets_or_t_c_recomputed":False,
    "characteristic_zero_arrays_expanded":False,"other_six_branches_or_five_Lj_computed":False,
    "only_budget_finite_search_limits_and_transport_excluded_from_identity":True}

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
    assert STRATEGY is not None
    return {"result":RESULT,"source_sha256":item["core_sha256"],
            "python_flint":"0.9.0","p":41,"method_sha256":item["method_sha256"],
            "proofs":item["proofs"],"sources":{g:identity(sources[g]) for g in GROUPS},
            "inputs":inputs,"strategy":STRATEGY}

def load_io():
    global IO
    path=S/RANGE_FILE
    assert sha(path)==RANGE_SHA
    d=importlib.util.spec_from_file_location("R890_frozen_stdlib_Range",path)
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
    assert item["maximum_pencil_trials"]>=4
    assert 1<=item["maximum_product_anchors"]<=418
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert set(item["source_artifacts"])=={"R887","R880","R872","R883"}
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
    core_sha=initial["core_sha256"] if "core_sha256" in initial else initial["job"]["core_sha256"]
    assert core_sha==core["source_sha256"]==source["core_sha256"]
    if source.get("wrapper_sha256") is not None:
        driver=initial.get("wrapper_sha256",initial.get("driver_sha256"))
        assert driver==source["wrapper_sha256"]
    if run.get("core_receipt_sha256") is not None:
        assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
    if group=="R827":
        assert run["complete"] is False and core["complete"] is False
        assert run["process_exit_code"]==124
        certificate=None
        anchor=read(bound(folder,source["configuration_stage"]))
        assert anchor["complete"] is True
        tag=anchor["configuration"]
    else:
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
    assert tag.get("source_sha256",tag.get("core_sha256"))==source["core_sha256"]
    if source.get("configuration_sha256") is not None:
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
            path=PurePosixPath(member.name)
            assert member.isfile() and not path.is_absolute() and ".." not in path.parts
            assert "\\" not in member.name and len(path.parts)==2 and path.parts[0]=="original"
            assert path.name not in seen;seen.add(path.name)
            target=folder/path.name
            with archive.extractfile(member) as src,target.open("wb") as dst:
                shutil.copyfileobj(src,dst)
            assert target.stat().st_size==member.size

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
        self.archive=None;self.selected={};self.transport=None;self.reference_transport=None
        prepared=item.get("prepared_transport",{}).get(group)
        if prepared is not None:
            outer=IO.Archive(prepared["archive"],Path(work)/("prepared-"+group),whole=False)
            try:
                package=plain(prepared["package"]);target=Path(work)/package["file"]
                outer.extract_bound(package["file"],package["sha256"],target,package["bytes"])
                extract_flat_package(target,self.folder)
                self.transport={"kind":"completed_original_intake","source":prepared["archive"],
                                "package":package,"range_receipt":outer.receipt()}
            finally:
                outer.close()
        else:
            self.archive=IO.Archive(self.prior,Path(work)/("archive-"+group),whole=False)
            if self.prior.get("manifest_sha256") is None:
                assert self.prior["read_complete_manifest_from_original_reference"] is True
                members=self.archive.by_name[REFERENCE]
                assert len(members)==1 and members[0].file_size<4096
                raw=self.archive.zip.read(members[0]);(self.folder/REFERENCE).write_bytes(raw)
                reference=read(self.folder/REFERENCE)
                self.reference_transport={"original_reference":spec(self.folder/REFERENCE),
                                          "original_reference_utf8":raw.decode("utf-8")}
                assert reference["result"]==self.prior["result"] and reference["file"]==MANIFEST
                self.prior["manifest_sha256"]=reference["sha256"]
                self.prior["manifest_bytes"]=reference["bytes"]
            self.archive.extract_bound(MANIFEST,self.prior["manifest_sha256"],self.folder/MANIFEST,
                                       self.prior.get("manifest_bytes"))
        self.entries=entry_map(self.folder,self.prior)
        wanted=self.prior["certificate"]
        actual=self.entries[wanted["file"]]
        assert actual["sha256"]==wanted["sha256"]
        if wanted.get("bytes") is not None:
            assert actual["bytes"]==wanted["bytes"]
        self.prior["certificate"]=actual
        self.take(list(META)+[self.prior["certificate"]["file"]])
        self.certificate,self.tag,self.initial=metadata(group,self.folder,self.prior,self.entries)

    def take(self,names):
        names=sorted(set(names))
        if self.archive is not None:
            self.archive.extract_many([(name,self.entries[name]["sha256"],self.folder/name,self.entries[name]["bytes"])
                                       for name in names])
        for name in names:
            bound(self.folder,self.entries[name]);self.selected[name]=self.entries[name]

    def stage(self,row):
        row=plain(row);assert self.entries[row["file"]]==row
        self.take([row["file"]]);value=read(self.folder/row["file"])
        assert value["complete"] is True and value["configuration"]==self.tag
        return value

    def finish_source(self):
        self.selected[MANIFEST]=self.entries[MANIFEST]
        source={**{k:self.prior[k] for k in BASE},"certificate":plain(self.prior["certificate"]),
                "configuration_sha256":fingerprint(self.tag),"files":dict(sorted(self.selected.items()))}
        if self.prior.get("manifest_bytes") is not None:
            source["manifest_bytes"]=self.prior["manifest_bytes"]
        if self.prior.get("manifest_file_count") is not None:
            source["manifest_file_count"]=self.prior["manifest_file_count"]
        return source

    def receipt(self):
        if self.archive is None:
            return self.transport
        value={"kind":"direct_original_Range","source":self.prior,"range_receipt":self.archive.receipt()}
        if self.reference_transport is not None:
            value["manifest_reference_read_from_pinned_original_archive"]=self.reference_transport
        return value

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
    assert set(sources)==set(GROUPS)
    for group,prior in item["source_artifacts"].items():
        actual=sources[group]
        same_source(prior,actual)
        assert plain(prior["certificate"])==plain(actual["certificate"])
    expected=item["R827_source"];actual=sources["R827"]
    same_source(expected,actual)
    assert plain(expected["configuration_stage"])==plain(actual["configuration_stage"])
    assert expected["selected_files_sha256"]==fingerprint(actual["files"])
    if inputs is not None:
        for key,row in item["input_pins"].items():
            assert plain(inputs[key])==plain(row)
        required={"Cstar","Dstar","Dchi","point_jets","point_linear_functional","Qtilde",
                  "t_frame","original_W","original_grid","original_place","original_Krylov_points"}
        assert set(inputs)==required
        assert len(inputs["original_Krylov_points"])==7

def source_review(item,retained,sources,inputs):
    original_pins(item,sources,inputs)
    tags={};certs={}
    for group,source in sources.items():
        folder=Path(retained)/group
        entries=entry_map(folder,source)
        assert all(entries[name]==plain(row) for name,row in source["files"].items())
        for row in source["files"].values():
            bound(folder,row)
        cert,tag,initial=metadata(group,folder,source,entries)
        tags[group]=tag;certs[group]=cert
    def stage(row):
        group=row["source_group"];original=plain(row)
        assert sources[group]["files"][original["file"]]==original
        value=read(bound(Path(retained)/group,original))
        assert value["complete"] is True and value["configuration"]==tags[group]
        return value
    def own(group,row):
        return stage(group_ref(group,row))
    C=stage(inputs["Cstar"]);D=stage(inputs["Dstar"]);X=stage(inputs["Dchi"])
    assert plain(certs["R887"]["complete_Cstar_418"])==plain(inputs["Cstar"])
    assert plain(certs["R880"]["complete_Dstar_418_kernel"])==plain(inputs["Dstar"])
    assert plain(certs["R872"]["complete_fixed_chi_418_kernel"])==plain(inputs["Dchi"])
    for value in (C,D):
        assert value["prime"]==P and value["accepted"] is True
        assert value["actual_projected_rank"]==418 and value["matrix_shape"]==[690,418]
        assert value["complete_RR_space_certified"] is True
        dimensions(value["normal_V3_basis_mod_prime"],690,418)
        assert value["exact_unit_solve_expression"]["modular_images_not_reconstructed_exact_coefficients"] is True
    assert X["prime"]==P and X["actual_kernel_dimension"]==418
    dimensions(X["V3_kernel_basis_mod_prime"],690,418)
    assert X["full_characteristic_zero_dimension"]==418
    assert X["exact_full_characteristic_zero_W_Dchi_certified"] is True
    assert X["all544_by418_quotient_residuals_zero"] is True
    assert X["all1234_by418_complete_V5_relations_zero"] is True
    assert X["normal_integer_scale_applied_again"] is False
    jets=stage(inputs["point_jets"]);point=stage(inputs["point_linear_functional"])
    assert plain(certs["R872"]["original_V2_jet_matrix"])==plain(inputs["point_jets"])
    assert plain(certs["R872"]["point_linearization"])==plain(inputs["point_linear_functional"])
    assert jets["prime"]==point["prime"]==P and point["original_zeta_root"]==549966761
    assert jets["matrix_shape"]==[273,418]
    dimensions(jets["matrix_mod_prime"],273,418)
    assert jets["row_orders"]==list(range(273)) and len(jets["V2_basis"])==418
    assert jets["normal_basis_degrees"]==EPS and jets["normal_integer_scale_applied_again"] is False
    assert len(point["point_evaluation_mod_prime"])==272
    assert point["chosen_local_parameter"]=="z_minus_z0"
    assert point["chosen_parameter_derivative_is_a_unit"] is True
    Q=stage(inputs["Qtilde"]);frame=stage(inputs["t_frame"])
    assert plain(certs["R887"]["original_principal_inputs"])==plain(inputs["Qtilde"])
    assert plain(Q["source_complete_Cstar_418"])==plain(inputs["Cstar"])
    assert plain(Q["source_complete_original_Dstar_418"])==plain(inputs["Dstar"])
    assert plain(Q["source_complete_original_Dchi_418"])==plain(inputs["Dchi"])
    parent=own("R880",Q["source_original_Q_f"])
    uC=own("R887",Q["source_exact_u_C"])
    assert plain(parent["source_complete_Dstar_418_space"])==plain(inputs["Dstar"])
    assert plain(parent["source_complete_D_chi_418_space"])==plain(inputs["Dchi"])
    assert Q["actual_rho_order"]==-1205 and 0<Q["actual_leading_coefficient_mod_prime"]<P
    assert Q["original_Qtilde_order_minus1205_certified"] is True
    assert Q["all_three_effective_degree272_representatives_avoid_original_P0"] is True
    assert Q["ideal_principal_factor_direction"]=="positive multiplication by Qtilde"
    assert Q["actual_local_parameter"]=="z_minus_z0"
    assert Q["exact_leading_coefficient_expression"]["no_actual_unit_rescaled_to_one"] is True
    assert len(certs["R883"]["stages"])==5
    assert any(plain(row)==plain(inputs["t_frame"]) for row in certs["R883"]["stages"].values())
    assert frame["original_t_first_order_unit_certified"] is True
    assert frame["quotient_all_three_coefficients_multiplied_back"] is True
    assert frame["exact_zero_not_inferred_from_modular_zero"] is True
    assert frame["original_t_first_three_coefficients_mod_prime"][0]==0
    assert 0<frame["original_t_over_rho_constant_mod_prime"]<P
    assert 0<frame["actual_c_powers_mod_prime"]["1205"]<P
    assert frame["exact_characteristic_zero_c_rational_expansion_computed"] is False
    W=stage(inputs["original_W"]);grid=stage(inputs["original_grid"]);place=stage(inputs["original_place"])
    assert W["prime"]==grid["prime"]==place["prime"]==P
    assert place["original_zeta_root"]==549966761
    assert grid["points"]==list(range(8))
    assert grid["all_eight_actual_determinants_nonzero"] is True
    assert len(W["W_coefficients_mod_prime"])==4
    for coefficient in W["W_coefficients_mod_prime"]:
        dimensions(coefficient,272,272)
    for j,ref in enumerate(inputs["original_Krylov_points"]):
        assert plain(ref)==plain(grid["Krylov_point_stages"][j])
        old=stage(ref)
        assert old["z0"]==j and old["prime"]==P
        assert old["usable"] is True and old["both_inverse_products_verified"] is True
        assert old["actual_cyclic_rank"]==272
        assert plain(old["source_original_W"])==plain(inputs["original_W"])
    for parent,children in (("R887",("R880","R872","R827")),("R880",("R872","R827")),
                            ("R872",("R827",))):
        for child in children:
            same_source(tags[parent]["sources"][child],sources[child])
    same_source(tags["R883"]["sources"]["R872"]["identity"],sources["R872"])
    assert tags["R883"]["sources"]["R872"]["configuration_sha256"]==sources["R872"]["configuration_sha256"]
    return {"result":RESULT,
            "source_identities":{g:identity(sources[g]) for g in GROUPS},
            "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
            "selected_file_count":sum(len(s["files"]) for s in sources.values()),
            "three_complete_original_normal_V3_spaces":[690,418],
            "normal_fields":{"Cstar":"normal_V3_basis_mod_prime","Dstar":"normal_V3_basis_mod_prime",
                             "Dchi":"V3_kernel_basis_mod_prime"},
            "original_V2_point_jets_shape":[273,418],
            "actual_old_source_nodes":grid["points"][:7],
            "Qtilde_rho_order":Q["actual_rho_order"],
            "Qtilde_original_rho_leading_coefficient_mod_prime":Q["actual_leading_coefficient_mod_prime"],
            "original_t_over_rho_constant_mod_prime":frame["original_t_over_rho_constant_mod_prime"],
            "original_c_power1205_mod_prime":frame["actual_c_powers_mod_prime"]["1205"],
            "all_selected_original_bytes_and_configurations_verified":True,
            "original_normal_coordinate_transformations_recomputed":False,
            "old_Hensel_or_Krylov_arithmetic_recomputed":False,
            "new_mathematics_executed":False}

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R890";retained.mkdir(parents=True,exist_ok=True)
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
    assert allow_download,"A complete retained R890 input carrier is required for offline verification."
    work=out.parent/"R890-download";handles={};poly=None
    try:
        for group in ("R887","R880","R872","R883"):
            handles[group]=Handle(group,item,retained,work)
        c=handles["R887"]
        for key in ("source_audit","complete_Cstar_418","original_principal_inputs","u_C","stage_manifest"):
            c.stage(c.certificate[key])
        d=handles["R880"]
        for key in ("source_audit","complete_Dstar_418_kernel","original_D_cusp_chi_principal_inputs","stage_manifest"):
            d.stage(d.certificate[key])
        x=handles["R872"]
        for key in ("source_audit","complete_fixed_chi_418_kernel","original_V2_jet_matrix",
                    "point_linearization","anchor_u","fixed_chi_divisor_and_principal_function","stage_manifest"):
            x.stage(x.certificate[key])
        t=handles["R883"]
        assert len(t.certificate["stages"])==5
        for row in t.certificate["stages"].values():
            t.stage(row)
        tname=item["input_pins"]["t_frame"]["file"]
        assert any(plain(row)==plain(item["input_pins"]["t_frame"]) for row in t.certificate["stages"].values())
        inputs={
            "Cstar":group_ref("R887",c.certificate["complete_Cstar_418"]),
            "Dstar":group_ref("R880",d.certificate["complete_Dstar_418_kernel"]),
            "Dchi":group_ref("R872",x.certificate["complete_fixed_chi_418_kernel"]),
            "point_jets":group_ref("R872",x.certificate["original_V2_jet_matrix"]),
            "point_linear_functional":group_ref("R872",x.certificate["point_linearization"]),
            "Qtilde":group_ref("R887",c.certificate["original_principal_inputs"]),
            "t_frame":group_ref("R883",t.entries[tname])}
        Q=c.stage(c.certificate["original_principal_inputs"])
        d.stage(Q["source_original_Q_f"]);c.stage(Q["source_exact_u_C"])
        bootstrap=item["R827_transport"]
        poly_item={"source_artifacts":{"POLY":bootstrap["archive"]}}
        poly=Handle("POLY",poly_item,work/"bootstrap-retained",work)
        for key in ("source_inventory","retained_inputs_receipt","package"):
            row=plain(bootstrap[key])
            assert poly.entries[row["file"]]==row
            poly.take([row["file"]])
        old_inventory=read(poly.folder/bootstrap["source_inventory"]["file"])
        old_receipt=read(poly.folder/bootstrap["retained_inputs_receipt"]["file"])
        assert old_receipt["source_inventory"]==plain(bootstrap["source_inventory"])
        assert old_receipt["source_bundle"]==plain(bootstrap["package"])
        old_source=old_inventory["source_R827"]
        assert identity(old_source)==item["R827_source"]
        assert poly.tag["source_R827"]==identity(old_source)
        original_inputs=old_inventory["inputs"]
        assert original_inputs==poly.tag["inputs"]
        extract_bound_group(poly.folder/bootstrap["package"]["file"],retained,"R827",old_source)
        inputs["original_W"]=group_ref("R827",original_inputs["W_reduction"])
        inputs["original_grid"]=group_ref("R827",original_inputs["cyclic_grid"])
        inputs["original_place"]=group_ref("R827",original_inputs["place_audit"])
        assert len(original_inputs["Krylov_points"])==8
        inputs["original_Krylov_points"]=[group_ref("R827",row) for row in original_inputs["Krylov_points"][:7]]
        sources={group:handle.finish_source() for group,handle in handles.items()}
        sources["R827"]=old_source
        original_pins(item,sources,inputs)
        review=source_review(item,retained,sources,inputs)
        transports={group:handle.receipt() for group,handle in handles.items()}
        transports["R827"]={"kind":"completed_original_R827_carrier_from_POLY",
            "transport_archive":bootstrap["archive"],"package":plain(bootstrap["package"]),
            "source_inventory":plain(bootstrap["source_inventory"]),
            "retained_inputs_receipt":plain(bootstrap["retained_inputs_receipt"]),
            "completed_POLY_certificate":plain(poly.prior["certificate"]),
            "completed_POLY_configuration_sha256":fingerprint(poly.tag),
            "original_R827_identity":identity(old_source),
            "unchanged_original_R827_file_count":len(old_source["files"]),
            "original_carrier_fully_hashed_and_each_member_verified":True,
            "duplicate_nested_carrier_not_embedded":True,
            "range_receipt":poly.receipt()}
        save(out/INVENTORY,{"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
                           "transports":transports,"original_large_carriers_read":False,
                           "new_mathematics_executed":False})
        pack(retained,sources,out/BUNDLE)
        save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,
            "source_inventory":spec(out/INVENTORY),"source_bundle":spec(out/BUNDLE),
            "source_identities":{g:identity(sources[g]) for g in GROUPS},
            "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
            "all_original_selected_bytes_and_stage_configurations_verified":True,
            "old_matrices_jets_or_normal_conversions_recomputed":False,"new_mathematics_executed":False})
        print("R890_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,sources,inputs,review
    finally:
        for handle in handles.values():
            handle.close()
        if poly is not None:
            poly.close()

def restore(item,out):
    resume=item.get("resume")
    if not resume:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R890-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R890-resume-archive",whole=False)
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
            "source_identities":{g:identity(sources[g]) for g in GROUPS},
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
    assert cert["p"]==41 and cert["actual_auxiliary_prime"]==P
    assert cert["actual_complete_flip_count"]==8
    assert len(cert["complete_flip_certificates"])==8
    assert cert["actual_all_eight_complete_normal418_spaces_certified"] is True
    assert cert["actual_original_Ef_bounded_divisor_identity_certified"] is True
    assert cert["actual_original_t_leading_coefficient_computed"] is True
    assert cert["original_characteristic_zero_functions_defined_by_bound_unit_solve_DAGs"] is True
    for key in ("old_three418_spaces_W_Krylov_jets_or_original_c_recomputed",
                "original_selected_scalars_rescaled_to_one",
                "characteristic_zero_coefficients_or_leading_scalar_expanded",
                "other_six_Galois_representatives_computed",
                "five_original_Lj_RR128_or144_computed",
                "Hecke_active_support_nonp_connection_period_or_height_computed"):
        assert cert[key] is False
    def own(ref):
        ref=plain(ref)
        assert entries[ref["file"]]==ref
        value=read(bound(out,ref))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        return value
    audit=own(cert["source_audit"])
    assert audit["sources"]=={g:identity(sources[g]) for g in GROUPS}
    assert audit["inputs"]==inputs and audit["prime"]==P
    assert audit["Cstar_Dstar_and_Dchi_complete_normal418_inputs"] is True
    assert audit["old_original_W_Krylov_inverses_and_jets_not_recomputed"] is True
    assert audit["original_t_first_order_and_powers_consumed_without_recomputation"] is True
    assert audit["original_characteristic_zero_unit_solve_definitions_retained"] is True
    neutral=own(entries[PREFIX+"neutral-H-and-original-P0-functional.json.gz"])
    assert neutral["tau_V2_is_complete_W_H"] is True and neutral["neutral_avoids_original_P0"] is True
    dimensions(neutral["neutral_W_H_normal_V3_basis_mod_prime"],690,418)
    assert len(neutral["normal_V3_P0_functional_mod_prime"])==690
    assert plain(neutral["source_original_point"])==plain(inputs["point_linear_functional"])
    assert plain(neutral["source_original_V2_jets"])==plain(inputs["point_jets"])
    spaces={"Cstar":plain(inputs["Cstar"]),"D":plain(inputs["Dstar"]),"X":plain(inputs["Dchi"]),
            "H":entries[PREFIX+"neutral-H-and-original-P0-functional.json.gz"]}
    function_values={"Cstar":1,"D":1,"X":1,"H":1}
    vectors=[[0,-2,0],[0,2,0],[0,-3,0],[0,0,-2],[0,0,4],[-1,3,0],[1,-3,-4],[-1,3,4]]
    last_principal=None
    for index,((new,left,right),ref,vector) in enumerate(zip(CHAIN,cert["complete_flip_certificates"],vectors),1):
        flip=own(ref)
        assert flip["prime"]==P and flip["flip_index"]==index
        assert flip["new_space_label"]==new and flip["input_labels"]==[left,right]
        assert plain(flip["left_complete_space"])==spaces[left]
        assert plain(flip["right_complete_space"])==spaces[right]
        assert flip["actual_product_image_dimension"]==flip["actual_pencil_rank"]==962
        assert flip["actual_U_dimension"]==146 and flip["actual_complete_space_dimension"]==418
        for key in ("all1904_by418_pencil_relations_verified","all1884_by146_membership_relations_verified",
                    "effective_degree272_and_original_P0_avoidance_certified",
                    "complete_characteristic_zero_space_defined_by_original_unit_minors",
                    "original_function_divisor_identity_and_unit_retained"):
            assert flip[key] is True
        assert flip["characteristic_zero_arrays_reconstructed"] is False
        product=own(flip["complete_product_image"])
        assert product["actual_product_image_dimension"]==962
        assert 1<=product["number_of_original_left_anchors_used"]<=418
        assert product["complete_product_image_is_H0_6H_minus_D1_minus_D2"] is True
        assert product["evaluation_injective_on_entire_V6"] is True
        assert product["full_seven_fibre_length"]==1904 and product["degree6H"]==1632
        assert product["no_geometric_point_or_reduced_fibre_selected"] is True
        span=own(product["selected_span_state"])
        assert span["actual_rank"]==962 and len(span["selected_rows"])==962
        assert len(set(span["selected_rows"]))==962
        for block in span["selected_blocks"]:
            assert len(block["source_fibre_products"])==7
            for row in block["source_fibre_products"]:
                assert entries[row["file"]]==plain(row)
        membership=own(flip["complete_membership_matrix"])
        assert membership["matrix_shape"]==[1884,690]
        assert membership["membership_anchors"]==["tau^3","sigma^3"]
        assert membership["all_selected_row_residuals_zero"] is True
        assert membership["two_anchors_have_no_common_zero"] is True
        assert plain(membership["source_complete_product_image"])==plain(flip["complete_product_image"])
        U=own(flip["complete_U146"])
        assert U["matrix_shape"]==[1884,690] and U["actual_rank"]==544 and U["actual_kernel_dimension"]==146
        dimensions(U["kernel_basis_mod_prime"],690,146)
        assert U["both_selected_inverse_products_verified"] is True
        assert U["all_original_matrix_rows_times_complete_kernel_zero"] is True
        assert U["free_normalization_identity_verified"] is True
        anchor=own(flip["original_unscaled_P0_unit_section"])
        assert plain(anchor["source_complete_U146"])==plain(flip["complete_U146"])
        assert len(anchor["normal_V3_coordinates_mod_prime"])==690
        assert len(anchor["all146_P0_values_mod_prime"])==146
        assert 0<=anchor["selected_original_column"]<146
        assert anchor["q_P0_value_mod_prime"]==anchor["all146_P0_values_mod_prime"][anchor["selected_original_column"]]
        assert 0<anchor["q_P0_value_mod_prime"]<P
        assert anchor["q_P0_value_is_unit"] is True and anchor["original_scalar_not_rescaled"] is True
        space=own(flip["complete_normal418_space"])
        assert space["matrix_shape"]==[690,418] and space["actual_projected_rank"]==418
        assert space["projection_rows"]==[690,1380]
        dimensions(space["normal_V3_basis_mod_prime"],690,418)
        assert space["both_projection_inverse_products_verified"] is True
        assert space["all1904_rows_of_original_relation_verified"] is True
        assert space["complete_RR_space_certified"] is True
        assert space["D3_effective_degree272_and_avoids_original_P0"] is True
        assert space["characteristic_zero_coefficients_reconstructed"] is False
        assert plain(space["source_complete_U146"])==plain(flip["complete_U146"])
        assert plain(space["source_original_unscaled_u"])==plain(flip["original_unscaled_P0_unit_section"])
        profile=own(space["source_rank962_profile"])
        assert profile["accepted"] is True and profile["actual_rank"]==profile["required_rank"]==962
        assert profile["matrix_shape"]==[1904,1380]
        kernel=own(space["source_complete_relation_kernel"])
        assert kernel["matrix_shape"]==[1904,1380]
        assert kernel["actual_rank"]==962 and kernel["actual_kernel_dimension"]==418
        assert kernel["both_selected_inverse_products_verified"] is True
        assert kernel["all_original_matrix_rows_times_complete_kernel_zero"] is True
        dimensions(kernel["kernel_basis_mod_prime"],1380,418)
        principal=own(flip["principal_function_and_P0_unit"])
        assert principal["new_space_label"]==new
        assert principal["left_space_label"]==left and principal["right_space_label"]==right
        assert plain(principal["source_left_complete_space"])==spaces[left]
        assert plain(principal["source_right_complete_space"])==spaces[right]
        assert plain(principal["source_original_unscaled_u"])==plain(flip["original_unscaled_P0_unit_section"])
        assert plain(principal["source_complete_new_normal418"])==plain(flip["complete_normal418_space"])
        assert principal["new_original_class_coefficients"]==vector
        assert principal["class_coordinate_order"]==["Cstar-H","Dstar-H","Dchi-H"]
        assert principal["q_P0_value_mod_prime"]==anchor["q_P0_value_mod_prime"]
        assert principal["left_F_P0_value_mod_prime"]==function_values[left]
        assert principal["right_F_P0_value_mod_prime"]==function_values[right]
        assert 0<principal["F_P0_value_mod_prime"]<P
        assert principal["F_P0_unit_inverse_product_verified"] is True
        assert principal["all_selected_original_scalars_retained"] is True
        assert principal["original_rho_order_of_F"]==0
        assert principal["exact_F_function_DAG"]["operation"]=="inverse_of_product"
        assert len(principal["exact_F_function_DAG"]["factors"])==3
        assert principal["exact_F_function_DAG"]["repeated_parent_factors_are_retained_twice"] is True
        assert principal["characteristic_zero_function_or_unit_value_expanded"] is False
        spaces[new]=plain(flip["complete_normal418_space"])
        function_values[new]=principal["F_P0_value_mod_prime"]
        last_principal=plain(flip["principal_function_and_P0_unit"])
    marked=own(cert["marked_principal_QE"])
    assert marked["source_all_eight_complete_flips"]==cert["complete_flip_certificates"]
    assert plain(marked["source_complete_DE_normal418"])==spaces["DE"]
    assert plain(marked["source_original_Qtilde"])==plain(inputs["Qtilde"])
    assert plain(marked["source_original_t_frame"])==plain(inputs["t_frame"])
    assert marked["target_original_class_coefficients"]==[-1,3,4]
    assert marked["exact_original_divisor_identity"]=="Ef-1206P0=(DE-H)+div(QE)"
    assert marked["original_fractional_ideal_principal_factor_direction"]=="positive multiplication by QE"
    assert marked["DE_effective_degree"]==272 and marked["DE_avoids_original_P0"] is True
    assert marked["complete_W_DE_dimension"]==418
    assert marked["actual_rho_order"]==-1205
    assert marked["source_Qtilde_rho_leading_mod_prime"]==267133051
    assert marked["terminal_F_P0_unit_mod_prime"]==function_values["DE"]
    assert marked["actual_original_c_power1205_mod_prime"]==201313487
    assert 0<marked["actual_QE_rho_leading_mod_prime"]<P
    assert 0<marked["actual_QE_t_leading_mod_prime"]<P
    assert marked["exact_QE_function_DAG"]["operation"]=="multiply"
    assert plain(marked["exact_QE_function_DAG"]["right"]["source"])==last_principal
    assert marked["exact_t_leading_expression"]["positive_exponent"]==1205
    assert marked["all_eight_original_unscaled_q_P0_units_retained"] is True
    assert marked["actual_original_t_frame_evaluated"] is True
    for key in ("auxiliary_unit_asserted_to_be_41_adic_unit",
                "characteristic_zero_RR_coefficients_or_leading_scalar_expanded",
                "other_six_Galois_representatives_computed",
                "five_original_Lj_RR128_or144_computed",
                "Hecke_active_support_nonp_connection_period_or_height_computed"):
        assert marked[key] is False

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
            assert cert["actual_complete_math_stage_count"]==len(stages)
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
            "actual_complete_flip_count":cert.get("actual_complete_flip_count",0) if cert else 0,
            "complete_flip_certificates":cert.get("complete_flip_certificates",[]) if cert else [],
            "marked_principal_QE":cert.get("marked_principal_QE") if cert else None,
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
        print("R890_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
        return 0
    code=compute(item,args.output,args.request)
    try:
        print("R890_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
    except Exception:
        traceback.print_exc()
        if code==0:
            code=1
    return code

if __name__=="__main__":
    raise SystemExit(main())
