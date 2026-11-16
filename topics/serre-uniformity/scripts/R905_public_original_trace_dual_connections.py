#!/usr/bin/env python3
"""R905 standard-library source transport, source schema and output verification.
No mathematical module is imported by this wrapper.
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
CORE="R905_original_trace_dual_connections.py"
HELPER="R905_trace_dual_linear_algebra.py"
REQUEST=TOPIC/"notes/R905-trace-dual-connections-public-request.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R905-retained-original-inputs.tar.gz"
INVENTORY="R905-original-source-inventory.json"
INPUT_RECEIPT="R905-retained-inputs-receipt.json"
EXPANDED="R905-expanded-job.json"
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
IO=None
P=1000000753
N=272
EPS=[0]+[1]*144+[2]*127

REPOSITORY = "Rogerhu12/math-research-public"
RESULT = "R905-original-seven-bounded-divisor-connections-and-five-Picard-inputs"
FINAL = "p41-original-seven-bounded-divisor-connections-and-five-Picard-inputs-certificate.json"
PREFIX = "R905-"
MANIFEST = "full-outputs-manifest.json"
GROUPS = ("R896", "R894", "R872", "R827", "GLOBAL", "R883")
LABELS = ("D1", "D2", "D3", "D4", "D5", "X", "DN")
POWERS = (12, 8, 8, 13, 14)
DEGREES = (2970, 1674, 1800, 3024, 3339)
P_NUMERATORS = (165, 93, 100, 168, 371)
Q_DENOMINATORS = (67, 67, 67, 67, 134)
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
STRATEGY = {
    "original_curve": "original level82 minus3 twist Y, genus127, p41",
    "prime": P, "normal_basis_degrees": EPS,
    "original_s_root": 99932770, "original_zeta_root": 549966761,
    "original_integral_B_root": 3197390,
    "source_divisor_order": list(LABELS),
    "complete_source_spaces": "five R896 W_Dj, R872 W_X, R894 W_DN; each H0(3H-D), dimension418",
    "U_source": "new exact kernel of each final W_D modulo V2; never an unrelated old flip146",
    "bundle_source_weights": [1]*146+[0]*126,
    "bundle_auxiliary_schedule": "z=a, a=0,1,2,...; first actual complete272 unit graph",
    "bundle_complement": "first independent columns of [U_D(a),W_D(a)] after all146 U columns",
    "full_differential_basis": "(z-a)^k theta_i dz, k<=2-column_weight_i; length670",
    "full_principal_parts": "V3/(tau U_D), length544, perfect residue pairing including intersections and nilpotents",
    "principal_part_entry": "-[u^(2-k)](F(a+u)^-1 p_s(a+u))_i",
    "only_new_inverse_jets": [1,2], "existing_F0_inverse_recomputed": False,
    "target": "whole Artin trace on H minus whole Artin trace on D",
    "H_trace": "one common trace row; h_a restricts to sigma on H for every a",
    "primitive_section": "s_n=sum_(i=0)^145 n^i ell_i, original normal V1 basis, n=1,2,...",
    "primitive_whole_algebras": "dimension272, no support reduction or factor peeling",
    "new_weight1_multiplier_nodes": [0,1,2,3],
    "old_W_Krylov_inverses_or_273_point_charpoly_recomputed": False,
    "new_weight1_multiplier_bound": "degree(M_s)_ij<=1+epsilon_j-epsilon_i<=3",
    "target_trace_method": "actual full cyclic unit basis, complete companion relation and Newton trace identities",
    "principal_parts_rank": 543,
    "connection_gauge": "first canonical543 row/column unit chart, other127 coefficients zero",
    "characteristic_zero_solution": "same exact selected system; full image follows complete residue theorem, plus all544 modular rows verified",
    "special_case": "no characteristic-zero h0=1 claim from a modular kernel; preserve failure and explicit finite fallback contract",
    "seven_source_transport": "q sum_sigma alpha_Dj+7q(n-2)alpha_X-p average_sigma(alpha_DN-dlog QN)-q dlog Norm(Qj)",
    "true_Q_descent": "(alpha+cY(alpha))/2; cY(z)=z-2 adj(TI-W)0,72/adj(TI-W)0,0; cY(w)=w; cY(s)=-s",
    "original_nu_fixed": True,
    "original_principal_units_and_P0_t_frame_retained": True,
    "Hecke_calibration_nonp_period_or_height_computed": False,
    "only_budget_and_finite_search_scope_excluded_from_identity": True,
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
    d=importlib.util.spec_from_file_location("R905_frozen_stdlib_Range",path)
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
    out = {k: source[k] for k in BASE}
    out["configuration_sha256"] = source["configuration_sha256"]
    out["selected_files_sha256"] = fingerprint(source["files"])
    out["stage_result_location"] = source["stage_result_location"]
    for key in ("certificate", "configuration_stage"):
        if source.get(key) is not None:
            out[key] = plain(source[key])
    return out

class Source:
    def __init__(self, group, item, root):
        self.group, self.item = group, item
        self.folder = Path(root)/group
        self.files = {name: plain(row) for name, row in item["files"].items()}
        self.checked = set()
        assert spec(self.folder/MANIFEST) == self.files[MANIFEST]
        assert self.files[MANIFEST]["sha256"] == item["manifest_sha256"]
        manifest = read(self.folder/MANIFEST)
        assert manifest["result"] == item["result"]
        indexed = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(indexed) == len(manifest["files"])
        indexed[MANIFEST] = self.files[MANIFEST]
        for name, row in self.files.items():
            assert name == row["file"]
            if name != "full-outputs-manifest-reference.json":
                assert indexed[name] == row, (group, name)
        initial = self.raw("public-actions-input.json")
        run = self.raw("run-receipt.json")
        assert initial["source_commit"] == run["source_commit"] == item["source_commit"]
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        assert initial.get("core_sha256", initial.get("job", {}).get("core_sha256")) == item["core_sha256"]
        self.certificate = None
        if item.get("certificate") is not None:
            self.certificate = self.raw(item["certificate"]["file"])
            assert self.files[item["certificate"]["file"]] == plain(item["certificate"])
            assert self.certificate["result"] == item["result"] and self.certificate["complete"] is True
            assert run["complete"] is True and run["process_exit_code"] == 0
            self.tag = self.certificate["configuration"]
        else:
            assert group == "R827" and run["complete"] is False
            assert run["process_exit_code"] in item["accepted_process_exit_codes"]
            assert 0 not in item["accepted_process_exit_codes"]
            anchor = self.raw(item["configuration_stage"]["file"])
            assert anchor["complete"] is True
            self.tag = anchor["configuration"]
        assert fingerprint(self.tag) == item["configuration_sha256"]
        assert self.tag.get("source_sha256", self.tag.get("core_sha256")) == item["core_sha256"]
        assert self.tag["result"] == item["result"]
        assert item["stage_result_location"] == ("configuration" if group == "R827" else "top_level")
        if run.get("core_receipt_sha256") is not None:
            assert self.files["core-receipt.json"]["sha256"] == run["core_receipt_sha256"]
            receipt = self.raw("core-receipt.json")
            assert receipt["source_sha256"] == item["core_sha256"]
            if receipt.get("configuration") is not None:
                assert receipt["configuration"] == self.tag
            if receipt.get("configuration_sha256") is not None:
                assert receipt["configuration_sha256"] == item["configuration_sha256"]
            if self.certificate is not None:
                assert receipt["complete"] is True
                assert receipt["certificate_sha256"] == item["certificate"]["sha256"]

    def raw(self, name):
        if name not in self.checked:
            assert spec(self.folder/name) == self.files[name], (self.group, name)
            self.checked.add(name)
        return read(self.folder/name)

    def stage(self, row):
        assert self.files[row["file"]] == plain(row)
        value = self.raw(row["file"])
        assert value["complete"] is True and value["configuration"] == self.tag
        if self.item["stage_result_location"] == "configuration":
            assert "result" not in value and value["configuration"]["result"] == self.item["result"]
        else:
            assert value.get("result") == self.item["result"], (self.group, row["file"], "stage_result")
        return value

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
            "configuration_sha256":fingerprint(self.tag),"files":dict(sorted(self.selected.items())),
            "stage_result_location":"configuration" if self.group=="R827" else "top_level"}
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
        "proofs":item["proofs"],"linear_algebra_helper_sha256":item["linear_algebra_helper_sha256"],
        "sources":{g:identity(sources[g]) for g in GROUPS},"inputs":inputs,"strategy":STRATEGY}

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve()
    assert item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False
    assert item["core"]==CORE and sha(S/CORE)==item["core_sha256"]
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["linear_algebra_helper"]=="scripts/"+HELPER
    assert sha(topic_path(item["linear_algebra_helper"]))==item["linear_algebra_helper_sha256"]
    assert item["io_helper"]==RANGE_FILE and item["io_helper_sha256"]==RANGE_SHA
    assert 0<item["budget_minutes"]<=300
    assert 1<=item["maximum_auxiliary_fibres"]<=273
    assert 1<=item["maximum_primitive_trials"]<P and 1<=item["maximum_divisors"]<=7
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    assert set(item["proofs"])=={"R905","R909","YP","RF","R860"}
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert set(item["source_artifacts"])==set(GROUPS)
    assert all(item["source_artifacts"][g] is not None for g in GROUPS)
    load_io()

def original_pins(item,sources,inputs=None):
    assert set(sources)==set(GROUPS)
    for group,source in sources.items():
        prior=item["source_artifacts"][group]
        same_source(prior,source)
        assert source["stage_result_location"]==("configuration" if group=="R827" else "top_level")
        if prior.get("configuration_sha256") is None:
            assert prior.get("derive_configuration_from_pinned_original_stage") is True
        if source.get("certificate") is not None:
            wanted=prior.get("certificate")
            assert wanted is not None or prior.get("certificate_name") is not None
            if wanted is None:
                assert source["certificate"]["file"]==prior["certificate_name"]
            else:
                for key in ("file","sha256"):
                    assert source["certificate"][key]==wanted[key]
                if wanted.get("bytes") is not None:
                    assert source["certificate"]["bytes"]==wanted["bytes"]
        else:
            assert group=="R827"
            assert source["configuration_stage"]==plain(prior["configuration_stage"])
            assert source["accepted_process_exit_codes"]==prior["accepted_process_exit_codes"]
        for name,row in item.get("source_file_pins",{}).get(group,{}).items():
            assert source["files"][name]==plain(row),(group,name,"original_pin")
    if inputs is not None:
        assert set(inputs)=={"global_function_DAG","original_t_frame","original_W",
                             "original_Krylov_points","divisors"}
        assert set(inputs["original_Krylov_points"])==set(map(str,range(4)))
        assert set(inputs["divisors"])==set(LABELS)
        for label,entry in inputs["divisors"].items():
            assert set(entry)=={"space","certificate","principal"}
            group="R872" if label=="X" else "R894" if label=="DN" else "R896"
            assert all(row["source_group"]==group for row in entry.values())
        for key,row in item.get("input_pins",{}).items():
            assert plain(inputs[key])==plain(row)

def choose_inputs(handles,item):
    def named(group,key):
        handle=handles[group];name=item["input_names"][key]
        handle.named(name)
        return handle.ref(handle.entries[name])
    inputs={"global_function_DAG":named("GLOBAL","global_function_DAG"),
        "original_t_frame":named("R883","original_t_frame"),
        "original_W":named("R827","original_W"),"original_Krylov_points":{},"divisors":{}}
    for a in range(4):
        handle=handles["R827"];name=item["input_names"]["original_Krylov_points"][str(a)]
        handle.named(name)
        inputs["original_Krylov_points"][str(a)]=handle.ref(handle.entries[name])
    h=handles["R896"]
    assert h.certificate["all_five_complete_low_weight_RR_spaces_certified"] is True
    assert set(h.certificate["complete_direction_certificates"])==set(map(str,range(1,6)))
    for j in range(1,6):
        low=h.stage(h.certificate["complete_direction_certificates"][str(j)])
        assert low["j"]==j and low["complete_original_low_weight_RR_and_marked_principal_certified"] is True
        bounded=h.stage(low["source_complete_Dstd_certificate"])
        space=plain(low["complete_normal418_space"])
        assert space==plain(bounded["complete_normal_V3_space"])
        h.stage(space)
        principal=h.stage(low["marked_principal_Q"])
        assert plain(principal["complete_normal418_space"])==space
        # These are existing small, marked function leaves, not old dense kernel arrays.
        for key in ("source_marked_original_pair","source_exact_v"):
            if key in principal:
                h.stage(principal[key])
        inputs["divisors"]["D"+str(j)]={"space":h.ref(space),
            "certificate":h.ref(low["source_complete_Dstd_certificate"]),
            "principal":h.ref(low["marked_principal_Q"])}
    h=handles["R872"]
    x={key:named("R872","X_"+key) for key in ("space","certificate","principal")}
    definition=h.stage(x["certificate"])
    assert plain(definition["source_exact_u"])==plain(x["principal"])
    inputs["divisors"]["X"]=x
    h=handles["R894"]
    assert h.certificate["actual_original_seven_pole_trace_bounded_identity_certified"] is True
    complete=h.certificate["complete_new_flip_certificates"]
    assert len(complete)==16
    last=h.stage(complete[-1])
    assert last["flip_index"]==16 and last["new_space_label"]=="DN"
    principal=h.stage(h.certificate["marked_principal_and_descent"])
    space=plain(principal["source_complete_DN_normal418"])
    assert space==plain(last["complete_normal418_space"])
    h.stage(space)
    inputs["divisors"]["DN"]={"space":h.ref(space),"certificate":h.ref(complete[-1]),
        "principal":h.ref(h.certificate["marked_principal_and_descent"])}
    for group,rows in item.get("source_file_pins",{}).items():
        handles[group].take(list(rows))
        for name,row in rows.items():
            assert handles[group].entries[name]==plain(row)
    return inputs

def source_review(item,retained,sources,inputs):
    original_pins(item,sources,inputs)
    producers={g:Source(g,sources[g],retained) for g in GROUPS}
    # Re-read every selected byte identity. No producer mathematical core is imported.
    for group,source in sources.items():
        for name,row in source["files"].items():
            bound(Path(retained)/group,row)
            if name.endswith(".json.gz"):
                producers[group].stage(row)
    def stage(row):
        return producers[row["source_group"]].stage(row)
    def own(group,row):
        return stage(group_ref(group,row))
    graph=stage(inputs["global_function_DAG"])
    assert graph["global_y_exact_unit_expression_defined"] is True
    assert graph["original_eta_Picard_input_DAGs_defined"] is True
    nodes={v["id"]:v for v in graph["graph_nodes"]}
    assert len(nodes)==len(graph["graph_nodes"])
    sigma=nodes[graph["original_Galois_automorphism_node"]]
    assert sigma["operation"]=="original_Galois_automorphism_definition"
    assert sigma["data"]["fixes_zeta"] is True
    assert sigma["data"]["fixes_original_z_w_and_normal_basis"] is True
    assert graph["original_global_derivative_nodes"]["W"] in nodes
    frame=stage(inputs["original_t_frame"])
    assert frame["original_t_first_order_unit_certified"] is True
    assert frame["original_t_over_rho_constant_mod_prime"]==354813668
    assert frame["original_s_root"]==99932770
    assert frame["quotient_all_three_coefficients_multiplied_back"] is True
    assert producers["R896"].certificate["all_five_complete_low_weight_RR_spaces_certified"] is True
    assert producers["R894"].certificate["actual_original_seven_pole_trace_bounded_identity_certified"] is True
    normal3=[[i,k] for i,e in enumerate(EPS) for k in range(4-e)]
    selected=[]
    for label in LABELS:
        refs=inputs["divisors"][label]
        space,certificate,principal=[stage(refs[k]) for k in ("space","certificate","principal")]
        assert space["prime"]==P
        if label=="X":
            dimensions(space["V3_kernel_basis_mod_prime"],690,418)
            assert space["full_characteristic_zero_dimension"]==418
            assert space["all1234_by418_complete_V5_relations_zero"] is True
            assert space["normal_integer_scale_applied_again"] is False
            assert certificate["actual_complete_fixed_chi_RR_space_certified"] is True
            assert plain(certificate["source_exact_u"])==plain(refs["principal"])
            assert principal["order272_is_exact"] is True
        else:
            dimensions(space["normal_V3_basis_mod_prime"],690,418)
            assert space["normal_V3_basis"]==normal3
            assert space["complete_RR_space_certified"] is True
            assert space["actual_projected_rank"]==418
            if label=="DN":
                full=producers["R894"].certificate
                assert plain(refs["certificate"])==plain(full["complete_new_flip_certificates"][-1])
                assert plain(refs["principal"])==plain(full["marked_principal_and_descent"])
                assert certificate["flip_index"]==16 and certificate["new_space_label"]=="DN"
                assert certificate["effective_degree272_and_original_P0_avoidance_certified"] is True
                assert plain(certificate["complete_normal418_space"])==plain(refs["space"])
                assert principal["DN_effective_degree"]==272 and principal["DN_avoids_original_P0"] is True
                assert principal["actual_rho_order"]==-8435
                assert principal["exact_original_divisor_identity"]=="T_f^0=(D_N-H)+div(Q_N)"
                assert plain(principal["source_complete_DN_normal418"])==plain(refs["space"])
                assert isinstance(principal["exact_QN_function_DAG"],dict)
                assert plain(principal["source_original_t_frame"])==plain(inputs["original_t_frame"])
            else:
                j=int(label[1:]);full=producers["R896"].certificate
                low=own("R896",full["complete_direction_certificates"][str(j)])
                assert low["complete_original_low_weight_RR_and_marked_principal_certified"] is True
                assert plain(low["source_complete_Dstd_certificate"])==plain(refs["certificate"])
                assert plain(low["complete_normal418_space"])==plain(refs["space"])
                assert plain(low["marked_principal_Q"])==plain(refs["principal"])
                assert certificate["complete_characteristic_zero_H0_3H_minus_Dstd_certified"] is True
                assert certificate["Dstd_effective_degree272_and_avoids_original_P0"] is True
                assert plain(certificate["complete_normal_V3_space"])==plain(refs["space"])
                assert principal["j"]==j and principal["Dstd_degree"]==272
                assert principal["ordinary_power"]==POWERS[j-1]
                assert principal["original_pole_degree"]==DEGREES[j-1]
                assert principal["actual_Q_rho_order"]==principal["actual_Q_t_order"]==1-DEGREES[j-1]
                assert principal["original_fixed_chi_sign_is_negative_power_in_Q"] is True
                assert plain(principal["complete_normal418_space"])==plain(refs["space"])
                assert plain(principal["source_original_t_frame"])==plain(inputs["original_t_frame"])
                assert plain(principal["source_original_chi_anchor"])==plain(inputs["divisors"]["X"]["principal"])
                assert isinstance(principal["exact_principal_nodes"],list) and principal["Q_root"]=="Q"
                old=graph["five_original_polar_and_eta_outputs"][str(j)]
                assert old["original_Hom_word"]=="1+T^"+str(j)
                assert old["original_map_degree"]==DEGREES[j-1]
                assert old["p"]==P_NUMERATORS[j-1] and old["q"]==Q_DENOMINATORS[j-1]
                assert principal["original_E_definition"]==old["global_pole_ideals"]
        selected.append({"label":label,"space":refs["space"],"certificate":refs["certificate"],
                         "principal":refs["principal"],"original_complete_dimension":418})
    W=stage(inputs["original_W"])
    assert W["prime"]==P and W["original_rational_denominators_all_units"] is True
    assert W["original_primitive_coordinate_solutions_not_recomputed"] is True
    assert producers["R827"].tag["normal_basis_degrees"]==EPS
    for a in range(4):
        point=stage(inputs["original_Krylov_points"][str(a)])
        assert point["prime"]==P and point["z0"]==a and point["usable"] is True
        assert point["actual_cyclic_rank"]==272 and point["both_inverse_products_verified"] is True
        assert plain(point["source_original_W"])==plain(inputs["original_W"])
        for key in ("W_evaluated_mod_prime","Krylov_matrix_mod_prime","inverse_Krylov_matrix_mod_prime"):
            dimensions(point[key],272,272)
    return {"result":RESULT,"complete_source_IO":True,"prime":P,
        "source_configuration_sha256":{g:sources[g]["configuration_sha256"] for g in GROUPS},
        "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
        "seven_complete_original_source_spaces":selected,"old_complete_Krylov_nodes":[0,1,2,3],
        "all_selected_original_bytes_and_configurations_verified":True,
        "historical_R827_top_level_result_not_invented":True,
        "source_418_or_old_W_Krylov_inverse_Gamma_derivatives_recomputed":False,
        "characteristic_zero_connection_coordinates_claimed_expanded":False,
        "new_mathematics_executed":False}

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R905";retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (BUNDLE,INVENTORY,INPUT_RECEIPT)):
        inventory=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        assert plain(receipt["source_inventory"])==spec(out/INVENTORY)
        assert plain(receipt["source_bundle"])==spec(out/BUNDLE)
        sources,inputs=inventory["sources"],inventory["inputs"]
        original_pins(item,sources,inputs);unpack(out/BUNDLE,retained,sources)
        review=source_review(item,retained,sources,inputs)
        return retained,sources,inputs,review
    assert allow_download,"The same-source retained carrier is required for offline verification."
    work=out.parent/"R905-download";work.mkdir(parents=True,exist_ok=True);handles={}
    try:
        for group in GROUPS:
            handles[group]=Handle(group,item,retained,work)
        inputs=choose_inputs(handles,item)
        sources={g:handles[g].finish_source() for g in GROUPS}
        review=source_review(item,retained,sources,inputs)
        save(out/INVENTORY,{"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
            "transports":{g:handles[g].receipt() for g in GROUPS},
            "all_selected_original_bytes_preserved":True,
            "source_aliases_do_not_relabel_original_mathematical_identity":True,
            "old_big_carriers_initial_Schur_Gamma_and_273_node_charpoly_not_required":True,
            "exact_ancestor_definitions_retained_by_original_manifest_and_source_reference":True,
            "new_mathematics_executed":False})
        pack(retained,sources,out/BUNDLE)
        save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,
            "source_inventory":spec(out/INVENTORY),"source_bundle":spec(out/BUNDLE),
            "source_identities":{g:identity(sources[g]) for g in GROUPS},
            "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
            "all_original_selected_bytes_and_stage_configurations_verified":True,
            "old_source_RR_W_Krylov_or_inverse_arithmetic_recomputed":False,
            "new_mathematics_executed":False})
        print("R905_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,sources,inputs,review
    finally:
        for handle in handles.values():
            handle.close()

def verify_complete_final(item,out,entries,tag,cert,sources,inputs):
    def stage(row):
        row=plain(row);assert entries[row["file"]]==row
        value=read(bound(out,row))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        return value
    def flags(value,keys):
        for key in keys:
            assert value[key] is True,(key,"completed_stage_flag")
    assert cert["p"]==41 and cert["prime"]==P
    assert cert["actual_completed_source_connections"]==7 and cert["source_divisor_order"]==list(LABELS)
    assert cert["unresolved_divisors"]=={} and set(cert["complete_source_connection_certificates"])==set(LABELS)
    flags(cert,("actual_seven_complete_full_principal_parts_solutions",
        "actual_five_original_I_Z_regular_connections_as_expressions_certified",
        "actual_true_cY_and_Galois_descent_of_complete_connections_certified",
        "original_P0_t_frames_Qj_QN_kappa_and_polarization_preserved"))
    for key in ("old_original_W_Krylov_or_inverse_or_418_spaces_recomputed",
                "old_273_node_characteristic_polynomial_Gamma_or_delta_B_recomputed",
                "source_characteristic_zero_arrays_or_connection_coordinates_expanded",
                "Hecke_calibration_nonp_Picard_period_height_or_Tp_nonvanishing_computed"):
        assert cert[key] is False
    audit=stage(cert["source_audit"])
    assert audit["sources"]==tag["sources"] and audit["inputs"]==inputs
    flags(audit,("seven_actual_complete_H0_3H_minus_D418_spaces_consumed",
        "source_DN_not_assumed_K_fixed","all_original_unscaled_Qj_QN_and_t_frame_sources_retained",
        "original_W_Krylov_and_inverses_not_recomputed","original_Gamma_B_derivatives_charpoly_or_RR418_not_recomputed"))
    common_H=None
    for label in LABELS:
        connection=stage(cert["complete_source_connection_certificates"][label])
        assert connection["label"]==label
        assert connection["source_original_complete_divisor_space"]==inputs["divisors"][label]["space"]
        assert connection["source_original_divisor_certificate"]==inputs["divisors"][label]["certificate"]
        assert connection["source_original_marked_principal"]==inputs["divisors"][label]["principal"]
        assert connection["complete_trace_dual_differential_basis_dimension"]==670
        assert connection["complete_principal_parts_dimension"]==544 and connection["actual_principal_parts_rank"]==543
        flags(connection,("all544_principal_part_equations_multiplied_back",
            "exact_regular_connection_on_original_O_H_minus_D_as_expression_certified",
            "exact_full_principal_parts_not_only_residues_certified",
            "all_ramification_nilpotents_and_D_H_intersections_preserved"))
        assert connection["characteristic_zero_connection_coefficients_expanded"] is False
        assert connection["canonical_splitting_Hecke_period_or_height_computed"] is False
        U=stage(connection["source_complete_U146"])
        assert U["source_original_final_418_space"]==inputs["divisors"][label]["space"]
        assert U["actual_truncation_rank"]==272 and U["actual_truncation_minor_determinant_mod_prime"]!=0
        flags(U,("all272_by146_truncation_relations_verified","both_projection_inverse_products_verified",
                 "previous_flip_146_space_not_assumed_to_have_this_divisor"))
        dimensions(U["free_identity_kernel_mod_prime"],418,146)
        dimensions(U["normal_V2_basis_mod_prime"],418,146)
        F=stage(connection["source_complete_bundle_unit_graph"])
        assert F["source_same_D_U146"]==connection["source_complete_U146"]
        assert F["source_original_W_D"]==inputs["divisors"][label]["space"]
        assert F["column_weights"]==[1]*146+[0]*126 and len(F["selected_original_W_columns"])==126
        assert F["actual_F_determinant_mod_prime"]!=0
        flags(F,("both_F_inverse_products_verified","full_rank272_equal_degree146_bundle_isomorphism_certified",
                 "D_and_H_disjoint_from_whole_auxiliary_fibre_certified",
                 "h0_H_minus_D_zero_follows_from_actual_unit_graph"))
        assert len(F["F_coefficients_low_to_high"])==4
        for value in F["F_coefficients_low_to_high"]:
            dimensions(value,272,272)
        model=stage(connection["source_complete_quotient_models"])
        assert model["source_same_D_U146"]==connection["source_complete_U146"]
        assert model["source_complete_bundle_unit_graph"]==connection["source_complete_bundle_unit_graph"]
        assert model["whole_D_algebra_dimension"]==272 and model["whole_D_plus_H_dimension"]==544
        flags(model,("all690_original_polynomial_division_identities_verified",
            "all146_U_relations_and272_canonical_quotient_rows_verified","D_H_intersections_not_assumed_empty",
            "no_new_denominator_inverse_or_polynomial_Hermite_performed"))
        dimensions(model["V2_D_quotient_projection_mod_prime"],272,418)
        dimensions(model["V3_to_V2_h_division_mod_prime"],418,690)
        pp=stage(connection["source_full_principal_parts_matrix"])
        assert pp["source_complete_bundle_unit_graph"]==connection["source_complete_bundle_unit_graph"]
        assert pp["source_complete_quotient_models"]==connection["source_complete_quotient_models"]
        assert pp["matrix_shape"]==[544,670] and len(pp["differential_basis_indices"])==670
        dimensions(pp["matrix_mod_prime"],544,670)
        flags(pp,("all146_original_test_relations_times_all670_columns_zero","all670_total_residues_zero_verified",
                  "complete_principal_parts_not_residue_only","all_nilpotents_ramification_and_D_H_intersections_preserved"))
        jets=stage(pp["source_three_inverse_coefficients"])
        assert jets["source_existing_inverse0"]==connection["source_complete_bundle_unit_graph"]
        assert jets["both_inverse_series_products_mod_u3_verified"] is True
        assert jets["zero_order_inverse_recomputed"] is False
        assert len(jets["new_inverse_hasse_coefficients_1_through2"])==2
        for value in jets["new_inverse_hasse_coefficients_1_through2"]:
            dimensions(value,272,272)
        target=stage(connection["source_full_target"])
        assert target["source_principal_parts_matrix"]==connection["source_full_principal_parts_matrix"]
        assert target["source_complete_quotient_model"]==connection["source_complete_quotient_models"]
        flags(target,("all146_U_test_relations_times_target_zero","exact_total_residue_degH_minus_degD_zero",
            "constant_test_function_target_zero_verified","complete_full_principal_parts_via_perfect_pairing",
            "D_H_intersections_and_nonnormal_fibre_multiplicities_not_discarded",
            "exact_target_lies_in_full_image_by_global_residue_theorem"))
        dimensions(target["target_vector_544_mod_prime"],544,1)
        if common_H is None:
            common_H=target["source_common_complete_H_trace"]
        assert target["source_common_complete_H_trace"]==common_H
        for role in ("source_common_complete_H_trace","source_complete_D_trace"):
            trace=stage(target[role])
            assert trace["complete_artin_algebra_length"]==272 and trace["trace_of_unit_equals272"] is True
            assert len(trace["canonical_quotient_trace_row_mod_prime"])==272
            assert len(trace["all690_original_V3_test_function_traces_mod_prime"])==690
            power=stage(trace["source_complete_Artin_power_basis"])
            assert power["actual_primitive_unit"] is True
            if role=="source_common_complete_H_trace":
                assert trace["same_trace_reused_for_every_D_and_every_auxiliary_a"] is True
                assert trace["support_reduced_or_closed_points_split"] is False
            else:
                assert trace["source_complete_quotient_model"]==connection["source_complete_quotient_models"]
                assert trace["all_finite_factors_and_nilpotent_multiplicities_retained"] is True
        solution=stage(connection["source_full543_unit_solution"])
        assert solution["source_full_principal_parts_matrix"]==connection["source_full_principal_parts_matrix"]
        assert solution["source_full_target"]==connection["source_full_target"]
        assert solution["required_full_principal_parts_rank"]==solution["exact_rank_upper_bound_from_R905_R909"]==543
        assert solution["rank_is_required"] is True and solution["all_original_rows_multiplied_back"] is True
        assert len(solution["selected_rows"])==len(solution["selected_columns"])==543
        assert connection["exact_connection_DAG"]["coefficients"]["actual_auxiliary_unit_minor"]==connection["source_full543_unit_solution"]
    program=stage(cert["five_original_connection_DAGs"])
    assert program["source_seven_complete_regular_connections"]==cert["complete_source_connection_certificates"]
    assert program["source_original_global_function_DAG"]==inputs["global_function_DAG"]
    assert program["source_original_t_frame"]==inputs["original_t_frame"]
    flags(program,("all_five_original_I_Z_regular_connections_as_exact_expressions_certified",
        "original_QN_corrected_before_average","original_Qj_negative_chi_power_used_exactly_once",
        "true_curve_semilinear_action_not_coefficient_conjugation",
        "all_original_rigidification_constants_retained_by_source_reference"))
    assert program["seven_source_connections_only_new_principal_part_solves"]==7
    assert program["new_30_conjugate_numeric_connection_solves"]==program["new_126_aggregate_flip_computations"]==0
    assert program["canonical_Hecke_calibration_nonp_period_and_height_computed"] is False
    assert program["characteristic_zero_connection_coordinates_expanded"] is False
    seen=set();nodes={}
    for node in program["nodes"]:
        assert node["id"] not in seen and all(x in seen for x in node["arguments"])
        seen.add(node["id"]);nodes[node["id"]]=node
    assert nodes["connection_minus_Tf"]["arguments"]==["alpha_DN","dlog_QN"]
    assert nodes["beta_N"]["data"]["rational_factor"]==[1,7]
    cy=nodes["original_cY"]["data"]
    assert cy["curve_action"]=={"z":"z-2*N(z,w)/D(z,w)","w":"w"}
    assert cy["constant_action"]=={"original_b":"fixed","s":"-s","zeta":"zeta^2"}
    assert cy["coefficient_conjugation_alone_is_not_used"] is True
    assert set(program["five_original_outputs"])==set(map(str,range(1,6)))
    for j in range(1,6):
        value=program["five_original_outputs"][str(j)]
        p,q,n=P_NUMERATORS[j-1],Q_DENOMINATORS[j-1],POWERS[j-1]
        assert (value["original_index"],value["p"],value["q"],value["n"])==(j,p,q,n)
        assert value["source_original_Qj"]==inputs["divisors"]["D"+str(j)]["principal"]
        assert value["source_original_QN"]==inputs["divisors"]["DN"]["principal"]
        assert value["source_original_t_frame"]==inputs["original_t_frame"]
        assert value["P0_rational_connection_residue"]==7*(p-q)
        assert value["P0_original_principal_order"]==7*(q-p)
        assert value["exact_original_I_Z_regular_connection_as_expression_certified"] is True
        assert value["true_Galois_and_cY_descent_applied_to_complete_connection"] is True
        assert value["height_or_original_Tp_nonvanishing_certified"] is False
        assert nodes[value["exact_K_connection_root"]]["data"]["coefficients"]==[q,7*q*(n-2),-p,-q]
        assert nodes[value["exact_Q_connection_root"]]["data"]["rational_factor"]==[1,2]



def restore(item,out):
    resume=item.get("resume")
    if not resume:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R905-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R905-resume-archive",whole=False)
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
        for key in ("proofs","method_sha256","linear_algebra_helper_sha256"):
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
            "actual_completed_source_connections":cert.get("actual_completed_source_connections",0) if cert else 0,
            "complete_source_connection_certificates":cert.get("complete_source_connection_certificates",{}) if cert else {},
            "actual_five_original_I_Z_regular_connections_as_expressions_certified":cert.get("actual_five_original_I_Z_regular_connections_as_expressions_certified",False) if cert else False,
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
        print("R905_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
        return 0
    code=compute(item,args.output,args.request)
    try:
        print("R905_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
    except Exception:
        traceback.print_exc()
        if code==0:
            code=1
    return code


if __name__=="__main__":
    sys.exit(main())
