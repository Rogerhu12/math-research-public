#!/usr/bin/env python3
"""R902 standard-library byte transport and fixed-source schema verification.
The mathematical cores are never imported.  Original producer groups retain
all configurations and byte identities; IO aliases name only local folders.
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
CORE="R902_original_six_Galois_low_weight_RR.py"
HELPER="R902_fixed_Galois_unit_charts.py"
REQUEST=TOPIC/"notes/R902-six-Galois-low-weight-RR-public-request.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R902-retained-original-inputs.tar.gz"
INVENTORY="R902-original-source-inventory.json"
INPUT_RECEIPT="R902-retained-inputs-receipt.json"
EXPANDED="R902-expanded-job.json"
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
IO=None
REPOSITORY="Rogerhu12/math-research-public"
RESULT="R902-original-six-Galois-five-sum-Hom-low-weight-RR"
FINAL="p41-original-six-Galois-five-sum-Hom-low-weight-RR-certificate.json"
PREFIX="R902-"
MANIFEST="full-outputs-manifest.json"
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127
POWERS=[12,8,8,13,14]
DEGREES=[2970,1674,1800,3024,3339]
FIBRES=[23,15,15,25,27]
DELTAS=[294,502,376,512,469]
INITIAL_DIMS=[168,376,250,386,343]
RESIDUAL_DIMS=[396,188,314,178,221]
PADDING=[250,42,168,32,75]
SIGMA_BRANCHES=[0,6,1,2,4,3,5]
FIELD_BASIS="b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
MANDATORY=("R893","R896","R849","R877","R809","R827","AB","SIXD","R872","R883","JETS","R890")
STRATEGY={
 "original_curve":"original genus127 Y, level82 and original minus3 descent",
 "prime":P,"s_root":99932770,"zeta_root":549966761,
 "original_sigma_branch_order":SIGMA_BRANCHES,"canonical_free_column":1186,
 "normal_basis_degrees":EPS,"initial_powers":POWERS,"pole_degrees":DEGREES,
 "original_fibre_counts":FIBRES,"initial_space_dimensions":INITIAL_DIMS,
 "residual_dimensions":RESIDUAL_DIMS,"padding_orders":PADDING,
 "fixed_task_order":[[j,r] for j in range(1,6) for r in range(1,7)],
 "sigma0":"external original R893/R896 stages, never recomputed or relabelled",
 "phase":"sigma^r(rho_j)^-3; T^7=zeta^2 retained; sigma^7 is identity on constants",
 "complete_initial_space":"same exact I,J,F unit-solve defines the entire conjugate space",
 "initial_numeric_columns":2,
 "two_free_RHS":"original B0 canonical column and original integer B1 power weights",
 "initial_Schur":"only old selected rows, with unchanged scalar Lagrange blocks",
 "strict_selection":"no new rows, columns, free order, projection rows or integer anchors",
 "fixed_nodes":"exact original node lists; no replacement after a new nonunit",
 "whole_fibre":"all272 factors and multiplicities, single actual Q unit and full Q*y=P",
 "only_new_derivative":"delta A at original sigma_power6; all other A/B derivatives reused",
 "low_weight":"complete residual kernel, complete146 and complete418, all original rows",
 "final_product_fibres":7,"V6_injection_length":1904,
 "principal":"Q=sigma(B0/tau^n)/(sigma(v)/tau^3)*qchi^(-(n-2))",
 "frame":"unscaled rho leading times original c^(deg(E)-1)",
 "transport_aliases":"source groups are IO labels; old producer configurations stay unchanged",
 "characteristic_zero_coordinates_reconstructed":False,
 "scope_control_and_budget_excluded_from_mathematical_identity":True,
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

def group_ref(group,row):
    return {"source_group":group,**plain(row)}

def same_source(left,right):
    assert all(str(left[k])==str(right[k]) for k in BASE)
    if left.get("configuration_sha256") is not None:
        assert left["configuration_sha256"]==right["configuration_sha256"]

def load_io():
    global IO
    path=S/RANGE_FILE
    assert sha(path)==RANGE_SHA
    d=importlib.util.spec_from_file_location("R902_frozen_stdlib_Range",path)
    IO=importlib.util.module_from_spec(d);d.loader.exec_module(IO)

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

def identity(source):
    answer={**{key:source[key] for key in BASE},
        "configuration_sha256":source["configuration_sha256"],
        "selected_files_sha256":fingerprint(source["files"])}
    if source.get("certificate") is not None:
        answer["certificate"]=plain(source["certificate"])
    else:
        answer["configuration_stage"]=plain(source["configuration_stage"])
    return answer

class Handle:
    def __init__(self,group,item,retained,work):
        self.group=group;self.prior=dict(item["source_artifacts"][group])
        self.folder=Path(retained)/group;self.folder.mkdir(parents=True,exist_ok=True)
        self.work=Path(work);self.archive=None;self.selected={};self.transports=[]
        for prepared in ([] if (self.folder/MANIFEST).exists() else item.get("prepared_transports",{}).get(group,[])):
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

def expected_tag(item,sources,inputs):
    return {"result":RESULT,"source_sha256":item["core_sha256"],
        "python_flint":"0.9.0","p":41,"method_sha256":item["method_sha256"],
        "proofs":item["proofs"],"fixed_chart_helper_sha256":item["fixed_chart_helper_sha256"],
        "sources":{g:identity(sources[g]) for g in sorted(sources)},
        "inputs":inputs,"strategy":STRATEGY}

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve()
    assert item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False
    assert item["core"]==CORE and sha(S/CORE)==item["core_sha256"]
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["fixed_chart_helper"]=="scripts/"+HELPER
    assert sha(topic_path(item["fixed_chart_helper"]))==item["fixed_chart_helper_sha256"]
    assert item["io_helper"]==RANGE_FILE and item["io_helper_sha256"]==RANGE_SHA
    assert 0<item["budget_minutes"]<=300 and 1<=item["maximum_pairs"]<=30
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert set(item["source_artifacts"])==set(MANDATORY)
    assert all(item["source_artifacts"][g] is not None for g in MANDATORY)
    load_io()

def original_pins(item,sources,inputs=None):
    assert set(sources)==set(MANDATORY)
    for group,source in sources.items():
        prior=item["source_artifacts"][group]
        same_source(prior,source)
        if prior.get("configuration_sha256") is None:
            assert prior.get("derive_configuration_from_pinned_original_stage") is True
        if source.get("certificate") is not None:
            wanted=prior.get("certificate")
            assert wanted is not None or prior.get("certificate_name") is not None
            if wanted is not None:
                for k in ("file","sha256"):
                    assert source["certificate"][k]==wanted[k]
                if wanted.get("bytes") is not None:
                    assert source["certificate"]["bytes"]==wanted["bytes"]
            else:
                assert source["certificate"]["file"]==prior["certificate_name"]
        else:
            assert group=="R827" and source["configuration_stage"]==plain(prior["configuration_stage"])
            assert source["accepted_process_exit_codes"]==prior["accepted_process_exit_codes"]
        for name,row in item.get("source_file_pins",{}).get(group,{}).items():
            assert source["files"][name]==plain(row)
    if inputs is not None:
        assert set(inputs["initial_certificates"])==set(inputs["low_weight_certificates"])==set(map(str,range(1,6)))
        assert set(inputs["initial_scalar_blocks"])==set(map(str,range(1,6)))
        assert set(inputs["original_algebras"])==set(inputs["normal_V3_fibres"])==set(map(str,range(27)))
        assert set(inputs["completed_A_derivatives"])==set(map(str,range(6)))
        assert set(inputs["completed_B_derivatives"])==set(map(str,range(7)))
        for key,row in item.get("input_pins",{}).items():
            assert plain(inputs[key])==plain(row)

def transport_old_R893_carrier(item,handle,retained):
    """Verify its exact 131 original members, retaining requested groups only.
    This is an immutable byte transport.  It calls no original mathematics.
    """
    transport=item["R893_original_input_transport"]
    assert handle.group=="R893"
    for key in ("source_inventory","retained_inputs_receipt","package"):
        wanted=transport[key]
        row=handle.entries[wanted["file"]]
        if wanted.get("sha256") is not None:
            assert row["sha256"]==wanted["sha256"]
        if wanted.get("bytes") is not None:
            assert row["bytes"]==wanted["bytes"]
        handle.take([row["file"]])
    inventory_spec=handle.entries[transport["source_inventory"]["file"]]
    receipt_spec=handle.entries[transport["retained_inputs_receipt"]["file"]]
    package_spec=handle.entries[transport["package"]["file"]]
    inv=read(bound(handle.folder,inventory_spec));receipt=read(bound(handle.folder,receipt_spec))
    assert inv["result"]==receipt["result"]==handle.prior["result"]
    assert inv["complete"] is True and receipt["complete"] is True
    assert plain(receipt["source_inventory"])==inventory_spec
    assert plain(receipt["source_bundle"])==package_spec
    old_sources=inv["sources"]
    assert {g:identity(s) for g,s in old_sources.items()}==handle.tag["sources"]
    assert receipt["source_identities"]==handle.tag["sources"]
    assert inv["inputs"]==handle.tag["inputs"]
    aliases={"R880":"AB","R877":"R877","R809":"R809","R849":"R849","R827":"R827","DSTAR":"SIXD"}
    for original,new in aliases.items():
        same_source(old_sources[original],item["source_artifacts"][new])
    seen=set()
    with tarfile.open(bound(handle.folder,package_spec),"r|gz") as archive:
        for member in archive:
            if member.isdir():
                continue
            p=PurePosixPath(member.name)
            assert member.isfile() and len(p.parts)==2 and not p.is_absolute()
            assert ".." not in p.parts and "\\" not in member.name
            group,name=p.parts;key=(group,name)
            assert group in old_sources and name in old_sources[group]["files"] and key not in seen
            row=plain(old_sources[group]["files"][name]);assert row["bytes"]==member.size
            target=None;stream=None;tmp=None
            if group in aliases:
                folder=Path(retained)/aliases[group];folder.mkdir(parents=True,exist_ok=True)
                target=folder/name;tmp=target.with_name(target.name+".download")
                stream=tmp.open("wb")
            count=0;h=hashlib.sha256()
            try:
                with archive.extractfile(member) as raw:
                    for chunk in iter(lambda:raw.read(4*1024*1024),b""):
                        h.update(chunk);count+=len(chunk)
                        if stream is not None:
                            stream.write(chunk)
            finally:
                if stream is not None:
                    stream.close()
            assert count==row["bytes"] and h.hexdigest()==row["sha256"]
            if target is not None:
                if target.exists():
                    assert spec(target)==row;tmp.unlink()
                else:
                    tmp.replace(target)
            seen.add(key)
    assert seen=={(g,n) for g,s in old_sources.items() for n in s["files"]}
    assert len(seen)==131
    # Only original leaves and the small provenance files enter the new carrier.
    handle.selected.pop(package_spec["file"])
    return {"kind":"completed_R893_original_input_carrier","producer":handle.prior,
        "source_inventory":inventory_spec,"retained_inputs_receipt":receipt_spec,"package":package_spec,
        "actual_original_member_count":len(seen),"source_aliases":aliases,
        "all_original_members_byte_verified":True,"old_configurations_preserved":True,
        "duplicate_nested_package_retained":False,"old_mathematics_recomputed":False}

def choose_inputs(handles,item):
    """Read only published immutable stages and follow their exact references."""
    def resolve(parent,row,readable=True):
        key=parent
        if row.get("source_group") is not None and row["source_group"]!=parent:
            old=row["source_group"];ids=handles[parent].tag.get("sources",{})
            origin=ids.get(old)
            if origin is None and old in handles:
                origin=handles[old].prior
            assert origin is not None,(parent,old)
            choices=[g for g,h in handles.items() if all(str(h.prior[k])==str(origin[k]) for k in BASE)]
            assert len(choices)==1,(parent,old,choices)
            key=choices[0]
        h=handles[key];ref=group_ref(key,row)
        assert h.entries[row["file"]]==plain(row)
        if readable:
            h.stage(row)
        return ref
    def get(parent,row):
        ref=resolve(parent,row);return handles[ref["source_group"]].stage(ref),ref
    initial=handles["R893"];low=handles["R896"]
    assert initial.certificate["all_five_complete_initial_RR_spaces_certified"] is True
    assert low.certificate["all_five_complete_low_weight_RR_spaces_certified"] is True
    initial.stage(initial.certificate["source_audit"]);low.stage(low.certificate["source_audit"])
    inputs={}
    for key in ("global_DAG","original_place","original_W","seven_normal_inputs","zero_branch_A",
                "zero_branch_B","g_index","Gamma_index","operator_identity","S5_index"):
        inputs[key]=resolve("R893",initial.tag["inputs"][key])
    for key in ("other_normal_pairs","C_indexes"):
        inputs[key]=[resolve("R893",row) for row in initial.tag["inputs"][key]]
    for key in ("point_linear_functional","normal_V3_point_jets","fixed_chi_divisor","fixed_chi_anchor","t_frame"):
        inputs[key]=resolve("R896",low.tag["inputs"][key])
    for key in ("g_index","Gamma_index"):
        row=inputs[key];h=handles[row["source_group"]];index=h.stage(row)
        assert len(index["row_blocks"])==17
        for child in index["row_blocks"]:
            get(h.group,child)
    for row in inputs["C_indexes"]:
        h=handles[row["source_group"]];index=h.stage(row)
        assert len(index["coordinate_groups"])==2
        for child in index["coordinate_groups"]:
            get(h.group,child)
    inputs["initial_certificates"]={};inputs["low_weight_certificates"]={};inputs["initial_scalar_blocks"]={}
    def chart(ref):
        h=handles[ref["source_group"]];cert=h.stage(ref)
        get(h.group,cert["source_canonical_kernel"])
        # This old large inverse is an inherited witness, not a numerical input.
        resolve(h.group,cert["source_selected_unit_inverse"],readable=False)
    for j in range(1,6):
        ic,iref=get("R893",initial.certificate["complete_initial_RR_certificates"][str(j)])
        lc,lref=get("R896",low.certificate["complete_direction_certificates"][str(j)])
        assert plain(lc["source_complete_initial_RR"])==plain(iref)
        inputs["initial_certificates"][str(j)]=iref;inputs["low_weight_certificates"][str(j)]=lref
        for key in ("complete_B_kernel","source_original_unit_minor","source_complete_fibres"):
            get("R893",ic[key])
        name=f"R893-sum-{j}-three-scalar-interpolation-blocks.json.gz"
        initial.named(name);inputs["initial_scalar_blocks"][str(j)]=initial.ref(initial.entries[name])
        for key in ("source_marked_original_pair","source_unscaled_exact_v","marked_principal_Q"):
            get("R896",lc[key])
        residual,_=get("R896",lc["source_complete_two_B_residual_certificate"])
        get("R896",residual["source_B1"])
        chart(resolve("R896",residual["source_complete_relation_kernel"]))
        get("R896",residual["complete_residual_normal_V3_space"])
        padding,_=get("R896",lc["complete_padding146_space"])
        chart(resolve("R896",padding["source_complete_padding_kernel"]))
        bounded,_=get("R896",lc["source_complete_Dstd_certificate"])
        get("R896",bounded["source_exact_w"])
        chart(resolve("R896",bounded["source_complete_relation_kernel"]))
        get("R896",bounded["complete_normal_V3_space"])
    inputs["original_algebras"]={};inputs["normal_V3_fibres"]={}
    for a in range(27):
        name=f"R893-node-{a:06d}-original-Krylov.json.gz";fibre=initial.named(name)
        inputs["original_algebras"][str(a)]=initial.ref(initial.entries[name])
        if "source_original_Krylov" in fibre:
            get("R893",fibre["source_original_Krylov"])
        else:
            get("R893",fibre["source_new_Krylov_matrix"])
        if a<7:
            ref=resolve("R896",low.tag["inputs"]["cached_normal_V3_fibres"][str(a)])
        else:
            name=f"R896-node-{a:06d}-new-normal-V3-evaluation.json.gz"
            low.named(name);ref=low.ref(low.entries[name])
        inputs["normal_V3_fibres"][str(a)]=ref
    inputs["completed_A_derivatives"]={};inputs["completed_B_derivatives"]={}
    for r in range(6):
        for target in ("A","B"):
            name=(f"R893-sigma-{r:02d}-{target}-original-derivative.json.gz" if target=="A" or r==0
                  else f"R893-sigma-{r:02d}-B-imported-original-derivative.json.gz")
            initial.named(name);inputs["completed_"+target+"_derivatives"][str(r)]=initial.ref(initial.entries[name])
    name="R880-six-Dstar-branch-05-original-B-derivative-vectors.json.gz"
    last=handles["SIXD"].named(name)
    assert last["sigma_power"]==6 and last["original_branch"]==5
    inputs["completed_B_derivatives"]["6"]=handles["SIXD"].ref(handles["SIXD"].entries[name])
    return inputs

def source_review(item,retained,sources,inputs):
    original_pins(item,sources,inputs)
    tags={};certificates={};entries_by_group={}
    for group,source in sources.items():
        folder=Path(retained)/group;entries=entry_map(folder,source);entries_by_group[group]=entries
        for name,row in source["files"].items():
            assert entries[name]==plain(row);bound(folder,row)
        cert,tag,initial=metadata(group,folder,source,entries)
        tags[group]=tag;certificates[group]=cert
        for name,row in source["files"].items():
            if not name.endswith(".json.gz"):
                continue
            data=read(bound(folder,row))
            assert data["complete"] is True and data["configuration"]==tag,(group,name)
            if group in ("R827","R809"):
                # Both immutable producers place result only in configuration.
                assert "result" not in data,(group,name,"historical_stage_schema")
                assert data["configuration"]["result"]==source["result"]
            else:
                assert data.get("result")==source["result"],(group,name,"stage_result")
    def stage(ref):
        group=ref["source_group"];row=plain(ref)
        assert sources[group]["files"][row["file"]]==row
        value=read(bound(Path(retained)/group,row))
        assert value["complete"] is True and value["configuration"]==tags[group]
        return value
    def ref(parent,row,readable=True):
        group=parent
        if row.get("source_group") is not None and row["source_group"]!=parent:
            key=row["source_group"];origin=tags[parent].get("sources",{}).get(key)
            if origin is None and key in sources:
                origin=sources[key]
            assert origin is not None
            aliases=[g for g,s in sources.items() if all(str(s[k])==str(origin[k]) for k in BASE)]
            assert len(aliases)==1;group=aliases[0]
        assert entries_by_group[group][row["file"]]==plain(row)
        result=group_ref(group,row)
        if readable:
            stage(result)
        return result
    assert certificates["R893"]["all_five_complete_initial_RR_spaces_certified"] is True
    assert certificates["R896"]["all_five_complete_low_weight_RR_spaces_certified"] is True
    same_source(tags["R896"]["sources"]["R893"],sources["R893"])
    for old,new in (("R880","AB"),("R877","R877"),("R809","R809"),("R849","R849"),("R827","R827"),("DSTAR","SIXD")):
        same_source(tags["R893"]["sources"][old],sources[new])
    for old,new in (("R880","JETS"),("R872","R872"),("R883","R883"),("R827","R827"),("R890","R890")):
        same_source(tags["R896"]["sources"][old],sources[new])
    for key in ("global_DAG","original_place","original_W","seven_normal_inputs","zero_branch_A","zero_branch_B",
                "g_index","Gamma_index","operator_identity","S5_index"):
        assert ref("R893",tags["R893"]["inputs"][key])==inputs[key]
    for key in ("other_normal_pairs","C_indexes"):
        assert [ref("R893",x) for x in tags["R893"]["inputs"][key]]==inputs[key]
    for key in ("point_linear_functional","normal_V3_point_jets","fixed_chi_divisor","fixed_chi_anchor","t_frame"):
        assert ref("R896",tags["R896"]["inputs"][key])==inputs[key]
    graph=stage(inputs["global_DAG"])
    assert graph["global_y_exact_unit_expression_defined"] is True
    assert graph["five_original_addition_pole_ideals_as_fractional_DAGs_certified"] is True
    assert plain(certificates["R849"]["exact_expression_DAG"])==plain(inputs["global_DAG"])
    for j in range(1,6):
        data=graph["five_original_polar_and_eta_outputs"][str(j)]
        assert data["original_Hom_word"]=="1+T^"+str(j) and data["original_map_degree"]==DEGREES[j-1]
    place=stage(inputs["original_place"])
    assert place["prime"]==P and place["original_branch"]==0 and place["canonical_free_column"]==1186
    assert place["original_s_root"]==99932770 and place["original_zeta_root"]==549966761
    assert place["original_integral_B_root"]==3197390 and place["original_field"]==graph["original_field"]
    seven=stage(inputs["seven_normal_inputs"]);order=seven["ordered_original_sigma_powers"]
    assert [r["sigma_power"] for r in order]==list(range(7))
    assert [r["original_branch"] for r in order]==SIGMA_BRANCHES
    assert certificates["AB"]["all_seven_original_Galois_normal_inputs_certified"] is True
    assert certificates["AB"]["all1380_by12_original_coordinates_verified"] is True
    assert plain(certificates["AB"]["seven_Galois_normal_inputs"])==plain(inputs["seven_normal_inputs"])
    assert plain(order[0]["source_original_A_normal"])==plain(inputs["zero_branch_A"])
    assert plain(order[0]["source_original_B_normal"])==plain(inputs["zero_branch_B"])
    for key in ("zero_branch_A","zero_branch_B"):
        obj=stage(inputs[key]);dimensions(obj["vector_coefficients_mod_prime"],6,272)
        assert obj["all1380_original_short_coordinates_verified"] is True
    for r,row in enumerate(inputs["other_normal_pairs"],1):
        obj=stage(row);assert plain(row)==plain(order[r]["source_original_normal_pair"])
        assert obj["sigma_power"]==r and obj["original_branch"]==SIGMA_BRANCHES[r]
        assert obj["roots_B_s"]==order[r]["roots_B_s"]
        assert obj["all1380_original_coordinates_for_each_vector_verified"] is True
        dimensions(obj["A_vector_coefficients_mod_prime"],6,272)
        dimensions(obj["B_vector_coefficients_mod_prime"],6,272)
    assert len(inputs["C_indexes"])==6
    for j,row in enumerate(inputs["C_indexes"]):
        assert plain(certificates["R809"]["normal_vectors"]["C"+str(j)])==plain(row)
        index=stage(row);assert len(index["coordinate_groups"])==2
        for child in index["coordinate_groups"]:
            ref("R809",child)
    for key,target in (("g_index","g"),("Gamma_index","Gamma")):
        obj=stage(inputs[key]);assert obj["prime"]==P and obj["target"]==target and obj["chart"]=="tau"
        assert len(obj["row_blocks"])==17 and obj["normal_basis_degrees"]==EPS
        for ordinal,row in enumerate(obj["row_blocks"]):
            block=stage(ref("R827",row));first=16*ordinal
            assert (block["row_first"],block["row_stop"])==(first,min(first+16,272))
    point=stage(inputs["point_linear_functional"])
    assert point["z0_mod_prime"]==110702704 and point["w0_mod_prime"]==645975656
    jets=stage(inputs["normal_V3_point_jets"])
    assert jets["matrix_shape"]==[252,690] and jets["row_orders"]==list(range(252))
    dimensions(jets["matrix_mod_prime"],252,690)
    frame=stage(inputs["t_frame"])
    assert frame["original_t_first_order_unit_certified"] is True
    assert frame["original_t_over_rho_constant_mod_prime"]==354813668
    u=stage(inputs["fixed_chi_anchor"]);assert u["order272_is_exact"] is True
    chi=stage(inputs["fixed_chi_divisor"])
    assert chi["actual_complete_fixed_chi_RR_space_certified"] is True
    assert plain(chi["source_exact_u"])==plain(inputs["fixed_chi_anchor"])
    counts=[]
    for j in range(1,6):
        iref=inputs["initial_certificates"][str(j)];lref=inputs["low_weight_certificates"][str(j)]
        assert plain(iref)==plain(certificates["R893"]["complete_initial_RR_certificates"][str(j)])
        assert plain(lref)==plain(certificates["R896"]["complete_direction_certificates"][str(j)])
        ic,lc=stage(iref),stage(lref)
        assert ic["j"]==lc["j"]==j and ic["ordinary_power"]==lc["ordinary_power"]==POWERS[j-1]
        assert ic["complete_initial_RR_space_certified"] is True
        assert lc["complete_original_low_weight_RR_and_marked_principal_certified"] is True
        assert plain(lc["source_complete_initial_RR"])==plain(iref)
        B=stage(ref("R893",ic["complete_B_kernel"]))
        exact=B["exact_unit_solve_expression"]
        assert exact["complete_characteristic_zero_rank"]==DEGREES[j-1]
        minor=stage(ref("R893",ic["source_original_unit_minor"]))
        assert minor["row_indices"]==exact["row_indices"] and minor["column_indices"]==exact["pivot_columns"]
        assert minor["actual_determinant_mod_prime"]!=0
        selected=stage(ref("R893",ic["source_complete_fibres"]))
        assert selected["nodes"]==list(range(FIBRES[j-1]))
        scalar=stage(inputs["initial_scalar_blocks"][str(j)])
        assert scalar["nodes"]==selected["nodes"] and scalar["ordinary_power"]==POWERS[j-1]
        marked=stage(ref("R896",lc["source_marked_original_pair"]))
        assert marked["exact_B0_rho_order"]==1 and marked["actual_A0_P0_value_mod_prime"]!=0
        assert plain(marked["source_complete_B_kernel"])==plain(ic["complete_B_kernel"])
        residual=stage(ref("R896",lc["source_complete_two_B_residual_certificate"]))
        B1=stage(ref("R896",residual["source_B1"]))
        assert B1["trial"]==residual["accepted_B1_integer_parameter"]
        U=stage(ref("R896",lc["complete_padding146_space"]))
        v=stage(ref("R896",lc["source_unscaled_exact_v"]))
        assert v["exact_section_definition"]["column"]==U["first_unit_next_order_column"]
        bounded=stage(ref("R896",lc["source_complete_Dstd_certificate"]))
        w=stage(ref("R896",bounded["source_exact_w"]))
        assert w["trial"]==bounded["accepted_second_anchor_parameter"]
        for row in (residual["source_complete_relation_kernel"],U["source_complete_padding_kernel"],bounded["source_complete_relation_kernel"]):
            complete=stage(ref("R896",row))
            assert complete["complete_characteristic_zero_space_certified"] is True
            assert complete["all_original_rows_times_complete_kernel_zero"] is True
            raw=stage(ref("R896",complete["source_canonical_kernel"]))
            assert raw["canonical_free_identity_verified"] is True
            ref("R896",complete["source_selected_unit_inverse"],readable=False)
        Q=stage(ref("R896",lc["marked_principal_Q"]))
        assert Q["actual_Q_rho_order"]==Q["actual_Q_t_order"]==1-DEGREES[j-1]
        assert Q["original_fixed_chi_sign_is_negative_power_in_Q"] is True
        counts.append({"j":j,"B0_column":marked["original_kernel_column"],
            "B1_integer_parameter":B1["trial"],"v_column":v["exact_section_definition"]["column"],
            "second_integer_parameter":w["trial"],"same_original_fixed_charts_available":True})
    for a in range(27):
        obj=stage(inputs["original_algebras"][str(a)])
        assert obj["z0"]==a and obj["prime"]==P and obj["usable"] is True
        if "source_original_Krylov" in obj:
            old=stage(ref("R893",obj["source_original_Krylov"]))
            assert old["both_inverse_products_verified"] is True and old["actual_cyclic_rank"]==272
        else:
            built=stage(ref("R893",obj["source_new_Krylov_matrix"]))
            assert built["full_original_characteristic_relation_on_cyclic_vector_verified"] is True
            assert obj["both_inverse_products_verified"] is True and obj["actual_cyclic_rank"]==272
        fibre=stage(inputs["normal_V3_fibres"][str(a)])
        assert fibre["z0"]==a and fibre["prime"]==P
        dimensions(fibre["normal_evaluation_mod_prime"],272,690)
        dimensions(fibre["cyclic_evaluation_mod_prime"],272,690)
    for target,count in (("A",6),("B",7)):
        for r in range(count):
            obj=stage(inputs["completed_"+target+"_derivatives"][str(r)])
            assert obj["prime"]==P and obj["normal_basis_degrees"]==EPS
            if target=="B" and r==6:
                assert obj["sigma_power"]==6 and obj["original_branch"]==5
                assert obj["first_column_copied_from_actual_completed_derivative_matrices"] is True
                dimensions(obj["delta_B_coefficients_mod_prime"],8,272)
            else:
                dimensions(obj["vector_coefficients_mod_prime"],8,272)
    return {"result":RESULT,"prime":P,"complete_source_IO":True,
        "source_configuration_sha256":{g:fingerprint(tags[g]) for g in sorted(tags)},
        "selected_file_counts":{g:len(s["files"]) for g,s in sources.items()},
        "original_sigma_branch_order":SIGMA_BRANCHES,"original_fixed_choices":counts,
        "complete_old_algebras_and_normal_V3_fibres":27,"old_A_derivatives":6,"old_B_derivatives":7,
        "old_selected_inverse_matrices_not_required_as_numeric_inputs":True,
        "all_selected_original_bytes_and_configurations_verified":True,
        "new_mathematics_executed":False}

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R902";retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (BUNDLE,INVENTORY,INPUT_RECEIPT)):
        inv=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inv["result"]==receipt["result"]==RESULT
        assert inv["complete"] is True and receipt["complete"] is True
        assert plain(receipt["source_inventory"])==spec(out/INVENTORY)
        assert plain(receipt["source_bundle"])==spec(out/BUNDLE)
        sources,inputs=inv["sources"],inv["inputs"]
        original_pins(item,sources,inputs);unpack(out/BUNDLE,retained,sources)
        review=source_review(item,retained,sources,inputs)
        return retained,sources,inputs,review
    assert allow_download,"The complete same-source retained input carrier is required for offline verification."
    work=out.parent/"R902-download";work.mkdir(parents=True,exist_ok=True);handles={}
    try:
        handles["R893"]=Handle("R893",item,retained,work)
        bootstrap=transport_old_R893_carrier(item,handles["R893"],retained)
        for group in MANDATORY:
            if group!="R893":
                handles[group]=Handle(group,item,retained,work)
        inputs=choose_inputs(handles,item)
        sources={g:h.finish_source() for g,h in handles.items()}
        review=source_review(item,retained,sources,inputs)
        transports={g:h.receipt() for g,h in handles.items()}
        transports["R893"]["completed_original_input_carrier"]=bootstrap
        save(out/INVENTORY,{"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
            "transports":transports,"all_selected_original_bytes_preserved":True,
            "source_aliases_do_not_relabel_original_mathematical_identity":True,
            "old_dense_initial_Schur_y_multipliers_products_and_selected_inverses_not_selected":True,
            "duplicate_nested_R893_original_input_carrier_retained":False,"new_mathematics_executed":False})
        pack(retained,sources,out/BUNDLE)
        save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,
            "source_inventory":spec(out/INVENTORY),"source_bundle":spec(out/BUNDLE),
            "source_identities":{g:identity(sources[g]) for g in sorted(sources)},
            "selected_file_counts":{g:len(sources[g]["files"]) for g in sorted(sources)},
            "all_original_selected_bytes_and_stage_configurations_verified":True,
            "old_sigma0_RR_Krylov_derivative_jets_or_Normal_evaluation_arithmetic_recomputed":False,
            "new_mathematics_executed":False})
        print("R902_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,sources,inputs,review
    finally:
        for h in handles.values():
            h.close()

def verify_complete_final(item,out,entries,tag,cert,sources,inputs):
    def stage(row):
        row=plain(row);assert entries[row["file"]]==row
        obj=read(bound(out,row))
        assert obj["result"]==RESULT and obj["configuration"]==tag and obj["complete"] is True
        return obj
    retained=Path(out).parent/"retained-R902"
    def external(row):
        group=row["source_group"];assert sources[group]["files"][row["file"]]==plain(row)
        return read(bound(retained/group,row))
    def original_own(group,row):
        return external(group_ref(group,row))
    def old_chart(row):
        obj=external(row)
        raw=original_own("R896",obj["source_canonical_kernel"])
        return obj,raw
    def check_full_kernel(row,original,m,n,rank):
        obj=stage(row);old,raw=old_chart(original)
        assert obj["matrix_shape"]==[m,n] and obj["actual_rank"]==rank
        assert obj["actual_complete_kernel_dimension"]==n-rank
        assert obj["all_original_rows_checked"]==m
        assert obj["all_original_rows_times_kernel_zero"] is True
        assert obj["fixed_free_identity_verified"] is True
        assert obj["complete_conjugate_characteristic_zero_space_certified"] is True
        assert obj["new_rows_columns_free_order_or_anchor_chosen"] is False
        chart=obj["source_original_chart"]
        assert chart["source_original_complete_kernel"]==original
        assert plain(chart["source_original_selected_unit_minor"])==plain(old["source_selected_unit_inverse"])
        assert chart["matrix_shape"]==[m,n] and chart["rank"]==rank
        for key in ("selected_rows","pivot_columns","free_columns"):
            assert chart[key]==raw[key]
        minor=stage(obj["source_actual_conjugate_unit_minor"])
        assert minor["actual_unit"] is True and minor["actual_determinant_mod_prime"]!=0
        assert minor["source_original_chart"]==chart and minor["new_pivot_search_performed"] is False
        newraw=stage(obj["source_actual_conjugate_kernel"])
        assert newraw["fixed_free_identity_verified"] is True
        assert newraw["source_original_chart"]==chart
        dimensions(newraw["kernel_basis_mod_prime"],n,n-rank)
        offset=0
        for checkref in obj["source_all_original_row_checks"]:
            check=stage(checkref);first,stop=check["original_row_interval"]
            assert first==offset and first<stop<=m
            assert check["checked_shape"]==[stop-first,n-rank]
            assert check["all_original_rows_in_interval_times_kernel_zero"] is True
            assert check["source_actual_conjugate_kernel"]==obj["source_actual_conjugate_kernel"]
            offset=stop
        assert offset==m
        return obj
    def check_projection(row,kernel,original,dimension):
        obj=stage(row);old=external(original)
        assert obj["source_actual_conjugate_kernel"]==kernel
        assert obj["source_original_projection"]==original
        assert obj["original_independent_normal_rows"]==old["independent_normal_V3_rows"]
        assert obj["projection_rows"]==[690,1380] and obj["matrix_shape"]==[690,dimension]
        assert obj["actual_projection_minor_determinant_mod_prime"]!=0
        assert obj["complete_conjugate_RR_space_certified"] is True
        assert obj["new_projection_rows_chosen"] is False
        assert obj["normal_integer_scale_applied_again"] is False
        dimensions(obj["normal_V3_basis_mod_prime"],690,dimension)
        return obj
    assert cert["p"]==41 and cert["prime"]==P
    assert cert["actual_complete_conjugate_count"]==30
    assert cert["all_thirty_strict_conjugate_complete_low_weight_spaces_certified"] is True
    assert cert["original_sigma0_direction_certificates"]==inputs["low_weight_certificates"]
    assert cert["source_original_t_frame"]==inputs["t_frame"]
    assert cert["materialized_initial_B_columns_per_completed_pair"]==2
    assert cert["full_conjugate_initial_B_bases_numerically_materialized"] is False
    assert cert["complete_later146_and418_kernels_not_reduced_to_two_columns"] is True
    assert cert["strict_original_selection_and_integer_anchors_preserved"] is True
    assert cert["sigma0_or_old_Krylov_characteristic_S5_AB_derivatives_jets_recomputed"] is False
    assert cert["characteristic_zero_coefficients_expanded"] is False
    assert cert["Hecke_Picard_support_connection_period_or_height_computed"] is False
    audit=stage(cert["source_audit"])
    assert audit["sources"]==tag["sources"] and audit["inputs"]==inputs
    assert audit["original_sigma_branch_order"]==SIGMA_BRANCHES
    derivative=stage(cert["source_new_sigma6_A_derivative"])
    assert derivative["sigma_power"]==6 and derivative["target"]=="A"
    dimensions(derivative["vector_coefficients_mod_prime"],8,272)
    complete=cert["complete_direction_conjugate_certificates"]
    assert set(complete)==set(map(str,range(1,6)))
    for j in range(1,6):
        assert set(complete[str(j)])==set(map(str,range(1,7)))
        old_initial=external(inputs["initial_certificates"][str(j)])
        old_B=original_own("R893",old_initial["complete_B_kernel"])
        old_low=external(inputs["low_weight_certificates"][str(j)])
        old_marked=original_own("R896",old_low["source_marked_original_pair"])
        old_residual=original_own("R896",old_low["source_complete_two_B_residual_certificate"])
        old_U=original_own("R896",old_low["complete_padding146_space"])
        old_v=original_own("R896",old_low["source_unscaled_exact_v"])
        old_bounded=original_own("R896",old_low["source_complete_Dstd_certificate"])
        n=POWERS[j-1];d=272*n-126;nodes=list(range(FIBRES[j-1]))
        for r in range(1,7):
            result=stage(complete[str(j)][str(r)])
            assert (result["original_direction"],result["sigma_power"],result["original_branch"])==(j,r,SIGMA_BRANCHES[r])
            assert result["source_original_sigma0_complete_initial_space"]==inputs["initial_certificates"][str(j)]
            assert result["source_original_sigma0_complete_low_weight_space"]==inputs["low_weight_certificates"][str(j)]
            for flag in ("complete_initial_space_exact_unit_solve_defined","complete_residual_space_certified",
                         "complete_146_space_certified","complete_418_space_certified",
                         "strict_original_selection_and_integer_anchors_preserved",
                         "all_original_complete_fibre_relations_and_low_weight_kernel_rows_verified",
                         "complete_strict_conjugate_low_weight_RR_and_marked_principal_certified",
                         "original_tau_weight_negative_chi_power_and_t_frame_preserved"):
                assert result[flag] is True
            assert result["materialized_initial_B_columns"]==2
            assert result["actual_complete_initial_space_dimension"]==INITIAL_DIMS[j-1]
            assert result["full_conjugate_initial_B_basis_numerically_materialized"] is False
            assert result["old_sigma0_Krylov_Schur_derivatives_or_jets_recomputed"] is False
            initial=stage(result["source_actual_initial_space_and_two_columns"])
            assert initial["original_nodes"]==nodes and initial["all_original_rows_checked"]==272*len(nodes)
            assert initial["materialized_initial_B_columns"]==2
            assert initial["all_original_two_column_A_minus_yB_relations_verified"] is True
            assert initial["exact_two_columns_are_original_B0_B1_conjugates"] is True
            assert initial["all_factors_and_multiplicities_retained"] is True
            minor=stage(initial["source_actual_unit_minor"])
            chart=minor["source_original_chart"];old_exact=old_B["exact_unit_solve_expression"]
            assert chart["selected_rows"]==old_exact["row_indices"]
            assert chart["pivot_columns"]==old_exact["pivot_columns"]
            assert chart["free_columns"]==old_exact["free_columns"]
            assert minor["actual_unit"] is True and minor["actual_determinant_mod_prime"]!=0
            assert minor["new_pivot_search_performed"] is False
            A=stage(initial["source_actual_two_A_columns"]);B=stage(initial["source_actual_two_B_columns"])
            dimensions(A["A_coefficients_mod_prime"],d,2);dimensions(B["B_coefficients_mod_prime"],d,2)
            assert B["fixed_free_coordinates_verified"] is True and B["materialized_initial_B_columns"]==2
            assert B["full_square_inverse_materialized"] is False
            checks=initial["source_all_original_relations"];values=initial["source_all_complete_B_values"]
            assert len(checks)==len(values)==len(nodes)
            for a,checkref,valueref in zip(nodes,checks,values):
                check=stage(checkref);value=stage(valueref)
                assert check["z0"]==value["z0"]==a
                assert check["checked_shape"]==[272,2]
                assert check["all_original_A_minus_yB_coordinates_zero"] is True
                assert check["factors_multiplicities_or_rows_removed"] is False
                assert check["source_actual_complete_B_values"]==valueref
                assert value["all272_fibre_coordinates_retained"] is True
                dimensions(value["B_fibre_values_mod_prime"],272,2)
                dimensions(value["y_times_B_fibre_values_mod_prime"],272,2)
            marked=stage(result["source_actual_marked_pair"])
            assert marked["original_kernel_column"]==old_marked["original_kernel_column"]
            assert marked["exact_B0_rho_order"]==1 and marked["actual_A0_P0_value_mod_prime"]!=0
            assert marked["actual_B0_first_coefficient_mod_prime"]!=0
            assert marked["original_scalar_not_rescaled"] is True
            residual=stage(result["source_complete_two_B_residual_certificate"])
            assert residual["original_nodes"]==nodes and residual["actual_product_rank"]==690+DELTAS[j-1]
            B1=stage(residual["source_actual_B1"])
            assert B1["original_integer_parameter"]==old_residual["accepted_B1_integer_parameter"]
            kr=residual["source_complete_relation_kernel"]
            check_full_kernel(kr,group_ref("R896",old_residual["source_complete_relation_kernel"]),
                              272*len(nodes),1380,690+DELTAS[j-1])
            assert result["complete_residual_normal_V3_space"]==residual["complete_residual_normal_V3_space"]
            check_projection(residual["complete_residual_normal_V3_space"],kr,
                group_ref("R896",old_residual["complete_residual_normal_V3_space"]),RESIDUAL_DIMS[j-1])
            U=stage(result["complete_padding146_space"])
            assert U["matrix_shape"]==[690,146] and U["padding_order"]==PADDING[j-1]
            assert U["complete_conjugate_146_space_certified"] is True
            assert U["all_padding_rows_times_full146_space_zero"] is True
            assert U["original_selected_v_column"]==old_U["first_unit_next_order_column"]
            dimensions(U["normal_V3_basis_mod_prime"],690,146)
            check_full_kernel(U["source_complete_padding_kernel"],group_ref("R896",old_U["source_complete_padding_kernel"]),
                              PADDING[j-1],RESIDUAL_DIMS[j-1],PADDING[j-1])
            v=stage(result["source_unscaled_exact_v"])
            assert v["original_column"]==old_v["exact_section_definition"]["column"]
            assert v["original_scalar_not_rescaled"] is True and v["exact_order_equals_padding_certified"] is True
            bounded=stage(result["source_complete_Dstd_certificate"])
            assert bounded["original_nodes"]==nodes[:7]
            assert bounded["actual_product_rank"]==962 and bounded["all1904_original_rows_verified"] is True
            assert bounded["full_conjugate_bounded_space_certified"] is True
            w=stage(bounded["source_exact_w"])
            assert w["original_integer_parameter"]==old_bounded["accepted_second_anchor_parameter"]
            kb=bounded["source_complete_relation_kernel"]
            check_full_kernel(kb,group_ref("R896",old_bounded["source_complete_relation_kernel"]),1904,1380,962)
            assert result["complete_normal418_space"]==bounded["complete_normal_V3_space"]
            check_projection(result["complete_normal418_space"],kb,
                             group_ref("R896",old_bounded["complete_normal_V3_space"]),418)
            principal=stage(result["marked_principal_Q"])
            assert principal["complete_normal418_space"]==result["complete_normal418_space"]
            assert principal["source_original_sigma0_marked_principal_Q"]==group_ref("R896",old_low["marked_principal_Q"])
            assert principal["source_original_t_frame"]==inputs["t_frame"]
            assert principal["actual_original_t_over_rho_mod_prime"]==354813668
            assert principal["actual_Q_rho_order"]==principal["actual_Q_t_order"]==1-DEGREES[j-1]
            assert principal["actual_Q_rho_leading_mod_prime"]!=0 and principal["actual_Q_t_leading_mod_prime"]!=0
            assert principal["actual_original_t_scaling_power"]==DEGREES[j-1]-1
            for flag in ("strict_original_selection_and_integer_anchors_preserved",
                         "original_fixed_chi_sign_is_negative_power_in_Q","original_tau_weight_and_unscaled_constants_preserved",
                         "exact_principal_and_original_t_leading_defined"):
                assert principal[flag] is True
            nodes0={node["id"]:node for node in principal["exact_principal_nodes"]}
            assert len(nodes0)==len(principal["exact_principal_nodes"])
            assert principal["exact_principal_root"] in nodes0
            assert principal["characteristic_zero_coefficients_expanded"] is False
            assert principal["Hecke_Picard_support_connection_period_or_height_computed"] is False
    return {"all30_fixed_original_conjugate_RR_and_marked_principals_verified":True,
            "new_matrix_arithmetic_in_IO_verification":False}

def restore(item,out):
    resume=item.get("resume")
    if not resume:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R902-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R902-resume-archive",whole=False)
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
        for key in ("proofs","method_sha256","fixed_chart_helper_sha256"):
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
            "actual_complete_conjugate_count":cert.get("actual_complete_conjugate_count",0) if cert else 0,
            "complete_direction_conjugate_certificates":cert.get("complete_direction_conjugate_certificates",{}) if cert else {},
            "all_thirty_strict_conjugate_complete_low_weight_spaces_certified":cert.get("all_thirty_strict_conjugate_complete_low_weight_spaces_certified",False) if cert else False,
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
        print("R902_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
        return 0
    code=compute(item,args.output,args.request)
    try:
        print("R902_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
    except Exception:
        traceback.print_exc()
        if code==0:
            code=1
    return code

if __name__=="__main__":
    raise SystemExit(main())
