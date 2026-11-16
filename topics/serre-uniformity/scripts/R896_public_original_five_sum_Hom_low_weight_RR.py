#!/usr/bin/env python3
"""R896 standard-library source transport and complete-output verification.
No mathematical core is imported.  The new consumer uses only completed
original RR arrays, whole fibres, jets and frame sources.
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
RESULT="R896-original-five-sum-Hom-low-weight-residual-RR"
FINAL="p41-original-five-sum-Hom-low-weight-residual-RR-certificate.json"
PREFIX="R896-"
CORE="R896_original_five_sum_Hom_low_weight_RR.py"
REQUEST=TOPIC/"notes/R896-five-sum-Hom-low-weight-RR-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R896-retained-original-inputs.tar.gz"
INVENTORY="R896-original-source-inventory.json"
INPUT_RECEIPT="R896-retained-inputs-receipt.json"
EXPANDED="R896-expanded-job.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
MANDATORY=("R893","R880","R872","R883","R827","R890","C0")
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
POLE_DEGREES=DEGREES
DELTAS=RESIDUAL_DEGREES
B_DIMENSIONS=DIMENSIONS
FIBRE_COUNTS=FIBRES
RESIDUAL_DIMENSIONS=[396,188,314,178,221]
FIELD_BASIS="b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
IO=None

STRATEGY={
    "original_curve":"original genus127 Y, level82 and original minus3 descent",
    "prime":P,"original_branch":0,"original_integral_B_root":3197390,
    "original_s_root":99932770,"original_zeta_root":549966761,
    "original_Hom_words":["1+T^"+str(j) for j in range(1,6)],
    "normal_basis_degrees":EPS,"ordinary_powers":POWERS,
    "original_pole_degrees":POLE_DEGREES,"residual_degrees":DELTAS,
    "complete_initial_B_dimensions":B_DIMENSIONS,"original_fibre_counts":FIBRE_COUNTS,
    "V3_dimension":690,"marked_B0":"first original A-kernel column with unit original P0 value; unscaled",
    "second_B":"sum(c^i*B_i), exact positive integer c=1,2,... in fixed original kernel",
    "two_B_product_rank":[690+d for d in DELTAS],
    "two_B_products_have_weight":"n+3; original N>n+3; no V2n injection assumed",
    "residual_complete_dimensions":RESIDUAL_DIMENSIONS,
    "kernel_projection":"second690 rows, full relation kernel of [B0 V3,B1 V3]",
    "padding_orders":PADDING,"padding_complete_dimension":146,
    "old_normal_V3_point_matrix_shape":[252,690],
    "v_selection":"first padding-kernel column with unit coefficient at exact padding order; unscaled",
    "w_schedule":"sum(c^i*U_i), exact positive integer c=1,2,...",
    "final_fibres":"first seven already accepted whole fibres for the same original direction",
    "final_pencil_matrix_shape":[1904,1380],"final_pencil_rank":962,
    "final_complete_space_shape":[690,418],
    "fixed_B0_and_v_products_shared_across_all_trials":True,
    "old_R890_normal_V3_fibres_0_through_6_reused":True,
    "old_initial_Schur_y_multipliers_Krylov_inverses_and_jets_recomputed":False,
    "principal_G":"(B0/tau^n)/(v/tau^3)=tau^(3-n)*B0/v",
    "principal_Q":"G*(u_chi/tau^2)^(-(n-2))",
    "class_identity":"E-deg(E)P0=(Dstd-H)+(n-2)(Dchi-H)+div(Q)",
    "P0_pole_multiplicity":1,"m0_source":"actual original R848 c0 nonzero tangents and original local model",
    "rho_leading_Q":"b1/v_k * u_chi_272^(-(n-2))",
    "t_leading_Q":"rho_leading_Q * original_c^(deg(E)-1)",
    "unit_is_only_at_the_original_auxiliary_place":True,
    "exact_Galois_transports_preserve_all_original_indices_and_integer_parameters":True,
    "normal_integer_scale_applied_again":False,
    "characteristic_zero_coefficients_reconstructed":False,
    "five_Lj128_Picard_support_connection_or_height_computed":False,
    "only_budget_requested_directions_and_trial_limits_excluded_from_identity":True,
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
    d=importlib.util.spec_from_file_location("R896_frozen_stdlib_Range",path)
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
    assert 1<=item["maximum_B_pencil_trials"]<P
    assert 1<=item["maximum_U_pencil_trials"]<P
    assert item["requested_directions"]==sorted(set(item["requested_directions"]))
    assert item["requested_directions"] and all(1<=j<=5 for j in item["requested_directions"])
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
            assert plain(source["configuration_stage"])==plain(prior["configuration_stage"])
            assert source["accepted_process_exit_codes"]==prior["accepted_process_exit_codes"]
        for name,row in item.get("source_file_pins",{}).get(group,{}).items():
            assert source["files"][name]==plain(row)
    if inputs is not None:
        for key,row in item.get("input_pins",{}).items():
            assert plain(inputs[key])==plain(row)
        for z,row in item["cached_normal_V3_fibres"].items():
            assert inputs["cached_normal_V3_fibres"][z]==row
        assert set(inputs["initial_RR_certificates"])==set(map(str,range(1,6)))

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
                assert value["result"]==source["result"]
    def stage(row):
        group=row["source_group"];assert sources[group]["files"][row["file"]]==plain(row)
        value=read(bound(Path(retained)/group,row))
        assert value["configuration"]==tags[group] and value["complete"] is True
        return value
    def own(group,row):
        return stage(group_ref(group,row))
    original=certificates["R893"]
    assert original["all_five_complete_initial_RR_spaces_certified"] is True
    assert original["original_pole_degrees"]==DEGREES
    assert original["initial_RR_dimensions"]==DIMENSIONS
    for parent in ("R893","R890"):
        same_source(tags[parent]["sources"]["R827"],sources["R827"])
    for parent in ("R880","R890"):
        same_source(tags[parent]["sources"]["R872"],sources["R872"])
    point=stage(inputs["point_linear_functional"])
    jets=stage(inputs["normal_V3_point_jets"])
    assert point["chosen_local_parameter"]=="z_minus_z0"
    assert point["z0_mod_prime"]==110702704 and point["w0_mod_prime"]==645975656
    assert jets["prime"]==P and jets["matrix_shape"]==[252,690]
    assert jets["row_orders"]==list(range(252)) and jets["local_parameter"]=="z_minus_z0"
    positions=[(i,k) for i in range(272) for k in range(4-EPS[i])]
    assert jets["V3_basis"]==[{"normal_basis_row":i,"power_of_z":k} for i,k in positions]
    dimensions(jets["matrix_mod_prime"],252,690)
    assert jets["no_original_Hensel_step_recomputed"] is True
    chi=stage(inputs["fixed_chi_divisor"]);anchor=stage(inputs["fixed_chi_anchor"])
    assert chi["D_chi_degree"]==272 and chi["D_chi_effective_and_avoids_original_P0"] is True
    assert chi["actual_complete_fixed_chi_RR_space_certified"] is True
    assert plain(chi["source_exact_u"])==plain(inputs["fixed_chi_anchor"])
    assert chi["exact_divisor_identity"]=="chi-(D_chi-H)=-div(u/tau^2)"
    assert anchor["order272_is_exact"] is True and anchor["exact_order272_unit"]
    frame=stage(inputs["t_frame"])
    assert frame["original_t_first_order_unit_certified"] is True
    assert frame["original_t_over_rho_constant_mod_prime"]==354813668
    assert frame["exact_zero_not_inferred_from_modular_zero"] is True
    c0=certificates["C0"]
    assert c0["all_original_nonzero_values_and_division_denominators_checked"] is True
    assert c0["all_six_original_lambda_cubes_and_logarithmic_derivatives_computed"] is True
    for j,row in inputs["c0_W_jets"].items():
        assert plain(row)==plain(c0["W_jets"][j])
        value=stage(row)
        assert value["j"]==int(j) and value["original_map"]=="f4+T^"+j+" f4"
        assert value["actual_W_and_lambda_cube_nonzero"] is True
        assert value["all_field_inverses_and_displayed_quotients_multiplied_back"] is True
    W=stage(inputs["original_W"]);assert W["prime"]==P
    assert plain(inputs["original_W"])==plain(tags["R893"]["inputs"]["original_W"])
    for z,row in inputs["cached_normal_V3_fibres"].items():
        value=stage(row);assert value["z0"]==int(z) and value["prime"]==P
        assert value["normal_V3_basis"]==[list(p) for p in positions]
        assert plain(value["source_original_W"])==plain(inputs["original_W"])
        dimensions(value["normal_evaluation_mod_prime"],272,690)
        dimensions(value["cyclic_evaluation_mod_prime"],272,690)
        assert value["normal_integer_scale_applied_again"] is False
        assert value["old_W_K_or_Kinverse_recomputed"] is False
    counts={}
    for j in range(1,6):
        ref=inputs["initial_RR_certificates"][str(j)]
        assert plain(ref)==plain(original["complete_initial_RR_certificates"][str(j)])
        cert=stage(ref);n=POWERS[j-1];r=DIMENSIONS[j-1]
        assert cert["j"]==j and cert["original_Hom_word"]=="1+T^"+str(j)
        assert cert["ordinary_power"]==n and cert["original_pole_degree"]==DEGREES[j-1]
        assert cert["residual_degree"]==RESIDUAL_DEGREES[j-1]
        assert cert["complete_initial_RR_space_certified"] is True
        assert cert["all_complete_fibre_original_A_minus_yB_relations_verified"] is True
        assert cert["exact_unit_solve_expression_certified"] is True
        A=own("R893",cert["complete_A_kernel"]);B=own("R893",cert["complete_B_kernel"])
        mapping=[[i,k] for i in range(272) for k in range(n-EPS[i]+1)]
        assert A["original_column_mapping"]==B["original_column_mapping"]==mapping
        dimensions(A["A_coefficients_mod_prime"],272*n-126,r)
        dimensions(B["B_coefficients_mod_prime"],272*n-126,r)
        assert B["canonical_free_identity_verified"] is True
        assert B["all_original_Schur_rows_times_full_kernel_zero"] is True
        chosen=own("R893",cert["source_complete_fibres"]);nodes=chosen["nodes"]
        assert nodes==sorted(set(nodes)) and len(nodes)==FIBRES[j-1] and len(nodes)>n+3
        assert chosen["all_denominators_units_in_the_whole_fibres"] is True
        assert chosen["residue_field_factors_or_multiplicities_removed"] is False
        assert len(A["source_complete_yB_fibre_values"])==len(nodes)
        assert len(cert["all_original_fibre_relation_certificates"])==len(nodes)
        for a,rr,vr,cr in zip(nodes,chosen["full_fibre_sources"],A["source_complete_yB_fibre_values"],
                              cert["all_original_fibre_relation_certificates"]):
            single=own("R893",rr);value=own("R893",vr);check=own("R893",cr)
            assert single["j"]==j and single["z0"]==a and single["whole_fibre_unit"] is True
            assert single["all272_original_Q_times_y_equals_P_verified"] is True
            assert single["factors_or_nilpotents_removed"] is False
            assert value["j"]==check["j"]==j and value["z0"]==check["z0"]==a
            assert plain(value["source_complete_B_kernel"])==plain(cert["complete_B_kernel"])
            dimensions(value["B_fibre_values_mod_prime"],272,r)
            assert check["all272_times_complete_kernel_dimension_original_relations_zero"] is True
            assert plain(check["source_original_yB_values"])==plain(vr)
            algebra=own("R893",single["source_complete_fibre"])
            assert algebra["z0"]==a and algebra["prime"]==P and algebra["usable"] is True
            if "source_original_Krylov" in algebra:
                assert algebra["source_original_Krylov"]["source_group"]=="R827"
                old=own("R827",algebra["source_original_Krylov"])
                assert old["z0"]==a and old["usable"] is True and old["actual_cyclic_rank"]==272
                assert old["both_inverse_products_verified"] is True
                dimensions(old["inverse_Krylov_matrix_mod_prime"],272,272)
            else:
                assert algebra["both_inverse_products_verified"] is True and algebra["actual_cyclic_rank"]==272
                built=own("R893",algebra["source_new_Krylov_matrix"])
                assert built["z0"]==a and built["prime"]==P
                dimensions(built["W_evaluated_mod_prime"],272,272)
                dimensions(algebra["inverse_Krylov_matrix_mod_prime"],272,272)
        counts[str(j)]={"whole_fibres":len(nodes),"complete_B_dimension":r,
                        "actual_complete_B_fibre_rows":272*len(nodes)}
    return {"result":RESULT,"complete":True,
        "selected_counts":{g:len(v["files"]) for g,v in sources.items()},
        "selected_file_total":sum(len(v["files"]) for v in sources.values()),
        "source_configuration_sha256":{g:v["configuration_sha256"] for g,v in sources.items()},
        "original_R893_complete_spaces":counts,
        "old252_point_jets_and_seven_normal_V3_fibres_preserved":True,
        "old_initial_Schur_whole_Q_or_point_arithmetic_recomputed":False,
        "new_mathematics_executed_in_source_review":False}

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

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R896";retained.mkdir(parents=True,exist_ok=True)
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
    assert allow_download,"The complete retained original source carrier is required for offline verification."
    work=out.parent/"R896-download";work.mkdir(parents=True,exist_ok=True);handles={}
    try:
        bootstrap=bootstrap_R827(item,retained,work)
        for group in MANDATORY:
            handles[group]=Handle(group,item,retained,work)
        r893=handles["R893"];r827=handles["R827"]
        assert r893.certificate["all_five_complete_initial_RR_spaces_certified"] is True
        r893.stage(r893.certificate["source_audit"])
        RR={}
        for j in range(1,6):
            ref=r893.certificate["complete_initial_RR_certificates"][str(j)]
            cert=r893.stage(ref);RR[str(j)]=r893.ref(ref)
            A=r893.stage(cert["complete_A_kernel"]);r893.stage(cert["complete_B_kernel"])
            r893.stage(cert["source_original_unit_minor"])
            selected=r893.stage(cert["source_complete_fibres"])
            for ref in A["source_complete_yB_fibre_values"]:
                r893.stage(ref)
            for ref in cert["all_original_fibre_relation_certificates"]:
                r893.stage(ref)
            for ref in selected["full_fibre_sources"]:
                single=r893.stage(ref)
                fibre=r893.stage(single["source_complete_fibre"])
                if "source_original_Krylov" in fibre:
                    assert fibre["source_original_Krylov"]["source_group"]=="R827"
                    r827.stage(fibre["source_original_Krylov"])
                else:
                    r893.stage(fibre["source_new_Krylov_matrix"])
        W=r893.tag["inputs"]["original_W"];assert W["source_group"]=="R827";r827.stage(W)
        inputs={"initial_RR_certificates":RR,"original_W":r827.ref(W)}
        for key,entry in item["input_selectors"].items():
            group=entry["source_group"]
            data=handles[group].named(entry["file"])
            if entry.get("sha256") is not None:
                assert handles[group].entries[entry["file"]]==plain(entry)
            inputs[key]=handles[group].ref(handles[group].entries[entry["file"]])
        inputs["c0_W_jets"]={}
        for j in range(1,6):
            ref=handles["C0"].certificate["W_jets"][str(j)]
            handles["C0"].stage(ref);inputs["c0_W_jets"][str(j)]=handles["C0"].ref(ref)
        inputs["cached_normal_V3_fibres"]={}
        for z,ref in item["cached_normal_V3_fibres"].items():
            handles["R890"].stage(ref);inputs["cached_normal_V3_fibres"][z]=handles["R890"].ref(ref)
        sources={g:h.finish_source() for g,h in handles.items()}
        original_pins(item,sources,inputs)
        review=source_review(item,retained,sources,inputs)
        transports={g:h.receipt() for g,h in handles.items()}
        transports["R827"]["completed_POLY_original_source_carrier"]=bootstrap
        save(out/INVENTORY,{"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
            "transports":transports,"all_source_selected_bytes_preserved":True,
            "R893_large_Schur_blocks_y_multipliers_and_old_large_carriers_not_selected":True,
            "new_mathematics_executed":False})
        pack(retained,sources,out/BUNDLE)
        save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,
            "source_inventory":spec(out/INVENTORY),"source_bundle":spec(out/BUNDLE),
            "source_identities":{g:identity(v) for g,v in sources.items()},
            "selected_file_counts":{g:len(v["files"]) for g,v in sources.items()},
            "all_original_selected_bytes_and_stage_configurations_verified":True,
            "old_initial_RR_jets_Krylov_or_Normal_evaluation_arithmetic_recomputed":False,
            "new_mathematics_executed":False})
        print("R896_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,sources,inputs,review
    finally:
        for h in handles.values():
            h.close()

def restore(item,out):
    resume=item.get("resume")
    if not resume:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R896-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R896-resume-archive",whole=False)
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
    assert completed==sorted(set(completed)) and set(item["requested_directions"])<=set(completed)
    assert cert["requested_low_weight_RR_spaces_certified"] is True
    assert cert["all_five_complete_low_weight_RR_spaces_certified"] is (len(completed)==5)
    assert cert["original_pole_degrees"]==DEGREES and cert["initial_powers"]==POWERS
    assert cert["residual_degrees"]==RESIDUAL_DEGREES and cert["padding_orders"]==PADDING
    assert cert["residual_dimensions"]==[396,188,314,178,221]
    assert cert["complete_padding_dimension"]==146 and cert["complete_bounded_dimension"]==418
    assert cert["original_tau_weight_and_negative_chi_power_retained"] is True
    for key in ("old_initial_RR_Schur_whole_Q_Krylov_inverses_and_jets_recomputed",
                "characteristic_zero_coefficients_reconstructed",
                "original_Lj128_Hecke_Picard_support_connection_period_or_height_computed"):
        assert cert[key] is False
    def own(row):
        row=plain(row);assert entries[row["file"]]==row
        value=read(bound(out,row))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        return value
    def kernel(row):
        value=own(row);m,n=value["matrix_shape"];r=value["actual_rank"];d=value["actual_kernel_dimension"]
        assert n-r==d and value["all_original_rows_checked"]==m
        assert value["all_original_rows_times_complete_kernel_zero"] is True
        assert value["canonical_free_identity_verified"] is True
        assert value["complete_characteristic_zero_space_certified"] is True
        inverse=own(value["source_selected_unit_inverse"])
        assert inverse["matrix_shape"]==[r,r] and inverse["both_selected_inverse_products_verified"] is True
        assert 0<inverse["actual_selected_minor_determinant_mod_prime"]<P
        dimensions(inverse["inverse_selected_minor_mod_prime"],r,r)
        raw=own(value["source_canonical_kernel"])
        dimensions(raw["kernel_basis_mod_prime"],n,d)
        assert len(raw["free_columns"])==d and raw["canonical_free_identity_verified"] is True
        covered=0
        for checkref in value["source_all_original_row_checks"]:
            check=own(checkref);first,stop=check["original_row_interval"]
            assert first==covered and first<stop<=m
            assert check["checked_shape"]==[stop-first,d]
            assert check["all_original_rows_in_interval_times_kernel_zero"] is True
            assert plain(check["source_canonical_kernel"])==plain(value["source_canonical_kernel"])
            covered=stop
        assert covered==m
        return value
    audit=own(cert["source_audit"])
    assert audit["sources"]=={g:identity(v) for g,v in sources.items()}
    assert audit["inputs"]==inputs and audit["original_c0_multiplicity"]==1
    assert audit["all_five_source_R893_complete_initial_spaces_certified"] is True
    assert audit["old_normal_V3_jets_and_seven_completed_normal_fibres_reused"] is True
    assert set(cert["complete_direction_certificates"])=={str(j) for j in completed}
    for j in completed:
        n=POWERS[j-1];degree=DEGREES[j-1];delta=RESIDUAL_DEGREES[j-1]
        k=PADDING[j-1];d=690-delta
        value=own(cert["complete_direction_certificates"][str(j)])
        assert value["j"]==j and value["original_Hom_word"]=="1+T^"+str(j)
        assert value["ordinary_power"]==n and value["original_pole_degree"]==degree
        assert value["residual_degree"]==delta and value["residual_dimension"]==d
        assert value["padding_order"]==k and value["complete_padding_dimension"]==146
        assert value["complete_bounded_space_dimension"]==418 and value["Dstd_degree"]==272
        assert value["source_complete_initial_RR"]==inputs["initial_RR_certificates"][str(j)]
        for key in ("full_original_low_weight_products_and_kernel_rows_verified",
                    "F0_and_Dstd_avoid_original_P0",
                    "complete_original_low_weight_RR_and_marked_principal_certified",
                    "correct_original_tau_weight_and_chi_sign_preserved",
                    "original_t_frame_and_unscaled_constants_preserved",
                    "true_characteristic_zero_unit_solve_expressions",
                    "actual_arrays_are_only_modular_reductions"):
            assert value[key] is True
        assert value["characteristic_zero_coordinates_reconstructed"] is False
        assert value["initial_RR_Schur_whole_Q_or_old_jets_recomputed"] is False
        marked=own(value["source_marked_original_pair"])
        assert marked["j"]==j and marked["ordinary_power"]==n and marked["P0_pole_multiplicity"]==1
        assert marked["exact_B0_rho_order"]==1 and marked["actual_B0_constant_mod_prime"]==0
        assert 0<marked["actual_A0_P0_value_mod_prime"]<P
        assert 0<marked["actual_B0_first_coefficient_mod_prime"]<P
        assert marked["original_scalar_not_rescaled"] is True
        assert marked["exact_zero_not_inferred_from_modular_zero"] is True
        assert len(marked["A_coordinates_mod_prime"])==len(marked["B_coordinates_mod_prime"])==272*n-126
        residual=own(value["source_complete_two_B_residual_certificate"])
        assert residual["actual_product_rank"]==690+delta
        assert residual["all_original_product_rows_checked"]==272*FIBRES[j-1]
        assert residual["actual_residual_dimension"]==d
        assert residual["two_original_B_sections_have_common_zero_exactly_E"] is True
        rker=kernel(residual["source_complete_relation_kernel"])
        assert rker["matrix_shape"]==[272*FIBRES[j-1],1380] and rker["actual_kernel_dimension"]==d
        projected=own(value["complete_residual_normal_V3_space"])
        dimensions(projected["normal_V3_basis_mod_prime"],690,d)
        assert projected["actual_projected_rank"]==d and projected["complete_RR_space_certified"] is True
        assert 0<projected["actual_projection_minor_determinant_mod_prime"]<P
        U=own(value["complete_padding146_space"])
        dimensions(U["normal_V3_basis_mod_prime"],690,146)
        assert U["padding_order"]==k and U["complete_characteristic_zero_146_space_certified"] is True
        assert U["all_original_padding_rows_times_full146_kernel_zero"] is True
        pker=kernel(U["source_complete_padding_kernel"])
        assert pker["matrix_shape"]==[k,d] and pker["actual_rank"]==k and pker["actual_kernel_dimension"]==146
        anchor=own(value["source_unscaled_exact_v"])
        assert len(anchor["normal_V3_coordinates_mod_prime"])==690
        assert anchor["vanishes_to_order_at_least"]==k and anchor["exact_order_equals_padding_certified"] is True
        assert 0<anchor["actual_coefficient_at_padding_mod_prime"]<P
        assert anchor["original_scalar_not_rescaled"] is True
        bounded=own(value["source_complete_Dstd_certificate"])
        assert bounded["actual_product_rank"]==962 and bounded["all_original_product_rows_checked"]==1904
        assert bounded["Dstd_effective_degree272_and_avoids_original_P0"] is True
        final_kernel=kernel(bounded["source_complete_relation_kernel"])
        assert final_kernel["matrix_shape"]==[1904,1380] and final_kernel["actual_kernel_dimension"]==418
        finalspace=own(value["complete_normal418_space"])
        dimensions(finalspace["normal_V3_basis_mod_prime"],690,418)
        assert finalspace["actual_projected_rank"]==418 and finalspace["complete_RR_space_certified"] is True
        assert 0<finalspace["actual_projection_minor_determinant_mod_prime"]<P
        principal=own(value["marked_principal_Q"])
        assert principal["ordinary_power"]==n and principal["original_pole_degree"]==degree
        assert principal["source_original_chi_anchor"]==inputs["fixed_chi_anchor"]
        assert principal["source_original_t_frame"]==inputs["t_frame"]
        assert principal["actual_G_rho_order"]==1-k
        assert principal["actual_Q_rho_order"]==principal["actual_Q_t_order"]==1-degree
        assert principal["actual_original_t_scaling_power"]==degree-1
        assert principal["class_coefficients_Dstd_Dchi"]==[1,n-2]
        assert principal["exact_principal_nodes"][2]["homogeneous_tau_exponent"]==3-n
        assert principal["exact_principal_nodes"][2]["no_second_tau_factor_applied_to_normal_arrays"] is True
        assert principal["exact_principal_nodes"][4]["right"]["exponent"]==-(n-2)
        for key in ("original_unscaled_constants_and_tau_weight_difference_preserved",
                    "original_fixed_chi_sign_is_negative_power_in_Q",
                    "exact_principal_and_original_t_leading_defined","unit_at_auxiliary_place_not_asserted_at41"):
            assert principal[key] is True
        for key in ("actual_G_rho_leading_mod_prime","actual_Q_rho_leading_mod_prime","actual_Q_t_leading_mod_prime"):
            assert 0<principal[key]<P

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
            "complete_direction_certificates":cert.get("complete_direction_certificates",{}) if cert else {},
            "all_five_complete_low_weight_RR_spaces_certified":cert.get("all_five_complete_low_weight_RR_spaces_certified",False) if cert else False,
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
        print("R896_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
        return 0
    code=compute(item,args.output,args.request)
    try:
        print("R896_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
    except Exception:
        traceback.print_exc()
        if code==0:
            code=1
    return code

if __name__=="__main__":
    raise SystemExit(main())
