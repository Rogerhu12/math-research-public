#!/usr/bin/env python3
"""Standard-library source transport, resume and output review for R927."""
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

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R927-reference-endpoint-norm-frames-public-request.json"
RESULT = "R927-original-two-endpoint-reference-ideal-and-norm-frames"
FINAL = "p41-original-two-endpoint-reference-norm-frames-certificate.json"
PREFIX = "R927-reference-"
CURRENT = PREFIX + "current.json.gz"
INVENTORY = PREFIX + "stage-manifest.json.gz"
PRIME, ZETA, SROOT = 1000000753, 549966761, 99932770
DIM, NORMAL, CAP = 8, 272, 9
EPS = [0] + [1]*144 + [2]*127
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
SOURCES = ("R923", "R917", "R914", "R879", "R872")
PROOFS = ("R927", "R912", "R923", "R879", "R876", "R872")
HELPER_SHA = "c728c8e06cef3dfbe4d33f3a988cbbc1c3012909d67b4684d941effdec67033d"
H64 = re.compile(r"[0-9a-f]{64}")
DEFINITIONS = {
    "R923": ("R923-original-two-endpoint-target-normal-coordinates",
        "4aef4b448338f62216d3ce44135ace89f83c5be966acb6f90dc47adaed4d334c"),
    "R917": ("R917-original-two-endpoint-normal-orders",
        "f0e321a19ef6dbd259e88de1b670f514b0f9ed0df5b24659a9f787978b8fd743"),
    "R914": ("R914-original-full-V1-involution-and-P1-local-jets",
        "c7dded45af13c7cd37b9c5261d917c2e81d3c179debe963296bbd8caf746e004"),
    "R879": ("R879-original-reference-pole254-pencil",
        "a8573c2a0dfd830cd3cd41dda0858fa108dbcfe0e0fc1ad1d4f78a1b95a2bf33"),
    "R872": ("R872-original-P0-jets-and-fixed-Picard-RR-spaces",
        "0e5897512a2f45baaed9cd1b6b2badcb6bf6ee2b100fcd45db871ad9f6db1874"),
}
STRATEGY = {
    "scope": "original_reference_only_two_endpoint_ideal_coordinates_and_Norm_frames",
    "original_auxiliary_prime": PRIME, "original_zeta_root": ZETA, "original_s_root": SROOT,
    "complete_endpoint_rank": DIM, "normal_target_dimension": NORMAL,
    "endpoint_parameters": ["rho0=z-z0", "rho1=iota^*rho0=z-2*beta72-z0"],
    "reference_exact_function": "v0=f/u=-g/b; original ug+bf=0",
    "original_reference_pole_order": 254,
    "old_numerator_P0_order": 18, "old_denominator_P0_order": 272,
    "original_V1_scale_already_in_source": 6724, "new_scale_applied": 1,
    "target_P0_ideal_generators": "U-z0 and gamma_i-e_(i+1)(P0)/tau for i1..144",
    "normal_ring_generation": "all degree2 normal basis rows are original V1 products",
    "complete_P0_primary_summand": "annihilator of eighth power of pulled-back maximal ideal",
    "idempotent_lift": "e -> 3e^2-2e^3; entire two summands retained",
    "working_rho_precision_cap": CAP,
    "target_P0_parameter_norm_order_bound": 8,
    "reference_regular_complement": "(f-eta*g)/(u+eta*b), eta0..8 with entire block unit",
    "common_reference_frame_parameter_candidates": list(range(17)),
    "original_nine_parameters": list(range(9)),
    "original_P0_pole_summand_relative_matrices": "0 and lambda^-1*identity modulo rho",
    "reference_norm_leading": "lambda^r*U272^(-r)*LC(Norm(qrho0))^(-254)*C_complement(lambda)",
    "reference_norm_order": "-254*ord(Norm(qrho0))",
    "original_t_frame": "rho-leading*c_epsilon^(-rho-order), c1=-c0",
    "reference_generic_frame_and_both_dual7_determinants_retained": True,
    "all_factors_and_nilpotents_preserved": True,
    "zero_truncation": "NeedPrecision, never zero function or inactive",
    "five_target_sources": {"R903": None, "R907": None},
    "new_values_are_at_original_auxiliary_place_not_expanded_char0": True,
    "old_normal_orders_target_coordinates_jets_RR_or_reference_solution_recomputed": False,
    "only_budget_and_transport_paths_excluded_from_identity": True,
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    ensure_ascii=False).encode()).hexdigest()


def plain(value):
    answer = {k: value[k] for k in ("file", "bytes", "sha256")}
    assert Path(answer["file"]).name == answer["file"] and "\\" not in answer["file"]
    assert isinstance(answer["bytes"], int) and answer["bytes"] >= 0
    assert H64.fullmatch(answer["sha256"])
    return answer


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt", encoding="utf-8") if path.name.endswith(".gz")
          else path.open("r", encoding="utf-8")) as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    data = (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False) + "\n").encode()
    with tmp.open("wb") as raw:
        if path.name.endswith(".gz"):
            with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(data)
        else:
            raw.write(data)
        raw.flush()
        os.fsync(raw.fileno())
    tmp.replace(path)


def identity(value):
    return {k: str(value[k]) for k in BASE}


def source_identity(value):
    return {**identity(value), "configuration_sha256": value["configuration_sha256"],
        "selected_files_sha256": value["selected_files_sha256"],
        "selected_file_count": value["selected_file_count"],
        "certificate": plain(value["certificate"])}


def expected_tag(item):
    return {"result": RESULT, "source_sha256": item["core_sha256"],
        "helper_sha256": item["helper_sha256"], "p": 41, "prime": PRIME,
        "python_flint": "0.9.0", "method_sha256": item["method_sha256"],
        "proofs_sha256": {k: item["proofs"][k]["sha256"] for k in PROOFS},
        "sources": {k: source_identity(item["sources"][k]) for k in SOURCES},
        "inputs": item["inputs"], "strategy": STRATEGY}


class Source:
    def __init__(self, label, item):
        self.label, self.item, self.path = label, item, Path(item["directory"])
        assert (item["result"], item["core_sha256"]) == DEFINITIONS[label]
        self.files = {name: plain(v) for name, v in item["files"].items()}
        assert len(self.files) == item["selected_file_count"]
        assert fingerprint(self.files) == item["selected_files_sha256"]
        for name, row in self.files.items():
            assert name == row["file"] and spec(self.path/name) == row, (label, name)
        manifest = self.get("full-outputs-manifest.json")
        assert self.files["full-outputs-manifest.json"]["sha256"] == item["manifest_sha256"]
        assert manifest["result"] == item["result"]
        entries = {r["file"]: plain(r) for r in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == item["manifest_file_count"]
        for name, row in self.files.items():
            if name != "full-outputs-manifest.json":
                assert entries[name] == row, (label, name)
        initial, run, core = (self.get(name) for name in META)
        assert initial["source_commit"] == run["source_commit"] == item["source_commit"]
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        recorded = initial["core_sha256"] if "core_sha256" in initial else initial["job"]["core_sha256"]
        assert recorded == core["source_sha256"] == item["core_sha256"]
        if run.get("core_receipt_sha256") is not None:
            assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert core["complete"] is True
        self.cert = self.get(item["certificate"]["file"])
        assert self.cert["complete"] is True and self.cert["result"] == item["result"]
        assert self.files[item["certificate"]["file"]] == plain(item["certificate"])
        assert core["certificate_sha256"] == item["certificate"]["sha256"]
        self.tag = self.cert["configuration"]
        assert fingerprint(self.tag) == item["configuration_sha256"]
        assert self.tag.get("source_sha256", self.tag.get("core_sha256")) == item["core_sha256"]

    def get(self, name):
        assert name in self.files, (self.label, name)
        return read(self.path/name)

    def stage(self, row):
        assert self.files[row["file"]] == plain(row)
        value = self.get(row["file"])
        assert value["complete"] is True and value["configuration"] == self.tag
        assert value.get("result", self.tag["result"]) == self.item["result"]
        return value


MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R927-retained-original-inputs.tar.gz"
SOURCE_INVENTORY = "R927-original-source-inventory.json"
INPUT_RECEIPT = "R927-retained-inputs-receipt.json"
EXPANDED = "public-actions-expanded-job.json"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
FINALS = {
    "R923":"p41-original-two-endpoint-target-normal-coordinates-certificate.json",
    "R917":"p41-original-two-endpoint-normal-orders-certificate.json",
    "R914":"p41-original-full-V1-involution-and-P1-jets-certificate.json",
    "R879":"p41-original-reference-pole254-pencil-certificate.json",
    "R872":"p41-original-P0-jets-and-fixed-Picard-RR-spaces-certificate.json",
}


def bound(folder, row):
    row=plain(row)
    path=Path(folder)/row["file"]
    assert spec(path)==row,str(path)
    return path


def topic_path(name):
    p=PurePosixPath(name)
    assert not p.is_absolute() and ".." not in p.parts
    path=(TOPIC/str(p)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def module(name,path,expected):
    assert sha(path)==expected
    loader=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(loader)
    loader.loader.exec_module(value)
    return value


def guard(item):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
    assert item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False
    assert item["future_target_sources"]=={"R903":None,"R907":None}
    assert item["core"]=="R927_original_two_endpoint_reference_norm_frames.py"
    assert item["wrapper"]==Path(__file__).name
    assert item["helper"]=="R917_endpoint_order_arithmetic.py"
    assert sha(HERE/item["core"])==item["core_sha256"]
    assert sha(__file__)==item["wrapper_sha256"]
    assert sha(HERE/item["helper"])==item["helper_sha256"]==HELPER_SHA
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    assert set(item["proofs"])==set(PROOFS)
    for row in item["proofs"].values():
        assert sha(topic_path(row["file"]))==row["sha256"]
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert 0 < float(item["budget_minutes"]) <= 300
    assert set(item["source_artifacts"])==set(SOURCES)
    for label,source in item["source_artifacts"].items():
        assert source is not None
        assert (source["result"],source["core_sha256"])==DEFINITIONS[label]
        assert source["certificate"]["file"]==FINALS[label]
        assert source["manifest_bytes"]>0 and source["manifest_file_count"]>0
        assert source["expected_conclusion"]=="success"
    assert item["io_helper"]=="R824_public_original_global_polar_generators.py"
    assert item["io_helper_sha256"]==RANGE_SHA
    return module("R927_frozen_Range_IO",HERE/item["io_helper"],RANGE_SHA)


def stable_request(item):
    source={}
    for label,row in item["source_artifacts"].items():
        source[label]={**identity(row),"certificate":plain(row["certificate"])}
    return {"result":RESULT,"p":41,"core_sha256":item["core_sha256"],
        "helper_sha256":item["helper_sha256"],"method_sha256":item["method_sha256"],
        "proofs":item["proofs"],"source_identities_and_certificates":source,
        "input_pins":item["input_pins"],
        "future_target_sources":item["future_target_sources"],
        "strategy":STRATEGY}


def entry_map(folder,source):
    mp=Path(folder)/MANIFEST
    assert mp.stat().st_size==source["manifest_bytes"] and sha(mp)==source["manifest_sha256"]
    value=read(mp)
    assert value["result"]==source["result"]
    entries={r["file"]:plain(r) for r in value["files"]}
    assert len(entries)==len(value["files"])==source["manifest_file_count"]
    entries[MANIFEST]=spec(mp)
    return entries


def open_archive(io,source,folder,work):
    folder.mkdir(parents=True,exist_ok=True)
    archive=io.Archive(source,work,whole=False)
    try:
        if not (folder/MANIFEST).exists():
            archive.extract_bound(MANIFEST,source["manifest_sha256"],folder/MANIFEST,source["manifest_bytes"])
        entries=entry_map(folder,source)
        assert set(archive.by_name)==(set(entries)-{MANIFEST})|{MANIFEST,REFERENCE}
        for name,row in entries.items():
            assert len(archive.by_name[name])==1
            assert archive.by_name[name][0].file_size==row["bytes"]
        return archive,entries
    except BaseException:
        archive.close()
        raise


def extract(archive,entries,folder,names):
    pending=[]
    for name in sorted(set(names)):
        assert name in entries,name
        row=entries[name]
        if (folder/name).exists():
            bound(folder,row)
        else:
            assert archive is not None,("Missing selected original member",name)
            pending.append((name,row["sha256"],folder/name,row["bytes"]))
    if pending:
        archive.extract_many(pending)


def source_review(label,source,folder,names):
    entries=entry_map(folder,source)
    files={n:entries[n] for n in sorted(set(names))}
    for row in files.values():
        bound(folder,row)
    assert {MANIFEST,*META,source["certificate"]["file"]} <= set(files)
    initial,run,core=(read(folder/name) for name in META)
    assert initial["source_commit"]==run["source_commit"]==source["source_commit"]
    assert str(run["workflow_run_id"])==str(source["run_id"])
    actual=initial["core_sha256"] if "core_sha256" in initial else initial["job"]["core_sha256"]
    assert actual==core["source_sha256"]==source["core_sha256"]
    if run.get("core_receipt_sha256") is not None:
        assert run["core_receipt_sha256"]==files["core-receipt.json"]["sha256"]
    assert run["complete"] is True and run["process_exit_code"]==0 and core["complete"] is True
    cert=read(bound(folder,source["certificate"]))
    assert cert["result"]==source["result"] and cert["complete"] is True
    assert core["certificate_sha256"]==source["certificate"]["sha256"]
    tag=cert["configuration"]
    assert tag.get("source_sha256",tag.get("core_sha256"))==source["core_sha256"]
    cfg=fingerprint(tag)
    if source.get("configuration_sha256") is not None:
        assert source["configuration_sha256"]==cfg
    for name in files:
        if name.endswith(".json.gz"):
            value=read(folder/name)
            assert value["complete"] is True and value["configuration"]==tag
            assert value.get("result",tag["result"])==source["result"]
    return {**identity(source),"certificate":plain(source["certificate"]),
        "manifest_bytes":source["manifest_bytes"],"manifest_file_count":source["manifest_file_count"],
        "configuration_sha256":cfg,"files":files,
        "selected_file_count":len(files),"selected_files_sha256":fingerprint(files)}


def stage(folder,entries,row,tag,source):
    row=plain(row)
    assert entries[row["file"]]==row
    value=read(bound(folder,row))
    assert value["complete"] is True and value["configuration"]==tag
    assert value.get("result",tag["result"])==source["result"]
    return value


def unpack_original_bundle(bundle,inventory,retained):
    expected={(label,name):plain(row) for label,group in inventory["groups"].items()
              for name,row in group["files"].items()}
    seen=set()
    with tarfile.open(bundle,"r|gz") as stream:
        for member in stream:
            if member.isdir():
                continue
            path=PurePosixPath(member.name)
            assert member.isfile() and not path.is_absolute() and ".." not in path.parts
            assert "\\" not in member.name and len(path.parts)==2
            key=(path.parts[0],path.name)
            assert key in expected and key not in seen
            row=expected[key];assert member.size==row["bytes"]
            destination=retained/key[0]/key[1]
            destination.parent.mkdir(parents=True,exist_ok=True)
            temporary=destination.with_name(destination.name+".download")
            h=hashlib.sha256();count=0
            source=stream.extractfile(member);assert source is not None
            with temporary.open("wb") as out:
                while True:
                    block=source.read(1048576)
                    if not block:
                        break
                    h.update(block);count+=len(block);out.write(block)
            assert count==row["bytes"] and h.hexdigest()==row["sha256"]
            temporary.replace(destination);seen.add(key)
    assert seen==set(expected)


def write_bundle(out,retained,groups):
    inventory={"result":RESULT,"groups":groups,
        "original_source_files_preserve_their_own_configurations":True,
        "all_selected_original_files_sha256_verified":True,
        "selected_original_file_count":sum(g["selected_file_count"] for g in groups.values())}
    save(out/SOURCE_INVENTORY,inventory)
    path=out/BUNDLE
    tmp=path.with_name(path.name+".tmp")
    with tmp.open("wb") as raw:
        with gzip.GzipFile(filename="",fileobj=raw,mode="wb",mtime=0,compresslevel=2) as zipped:
            with tarfile.open(fileobj=zipped,mode="w|") as archive:
                for label in sorted(groups):
                    for name,row in sorted(groups[label]["files"].items()):
                        source=bound(retained/label,row)
                        info=tarfile.TarInfo(label+"/"+name)
                        info.size=row["bytes"];info.mtime=0;info.mode=0o644
                        with source.open("rb") as stream:
                            archive.addfile(info,stream)
    tmp.replace(path)
    receipt={"result":RESULT,"input_bundle":spec(path),"source_inventory":spec(out/SOURCE_INVENTORY),
        "producer_identities":{k:source_identity(v) for k,v in groups.items()},
        "selected_original_file_count":inventory["selected_original_file_count"],
        "mathematical_arithmetic_executed_by_transport":False,
        "complete_original_archives_rehashed":False}
    save(out/INPUT_RECEIPT,receipt)


def prepare_sources(item,out,io):
    retained=out.parent/"R927-retained-original"
    retained.mkdir(parents=True,exist_ok=True)
    if (out/BUNDLE).exists():
        receipt=read(out/INPUT_RECEIPT)
        bound(out,receipt["input_bundle"]);bound(out,receipt["source_inventory"])
        inventory=read(out/SOURCE_INVENTORY)
        assert set(inventory["groups"])==set(SOURCES)
        for label,source in item["source_artifacts"].items():
            group=inventory["groups"][label]
            assert identity(group)==identity(source)
            assert plain(group["certificate"])==plain(source["certificate"])
            assert source_identity(group)==receipt["producer_identities"][label]
        unpack_original_bundle(out/BUNDLE,inventory,retained)
        inherited=inventory["groups"]
    else:
        inherited=None
    archives={};entries={};certs={};tags={};names={}
    try:
        for label in SOURCES:
            source=item["source_artifacts"][label]
            folder=retained/label;folder.mkdir(parents=True,exist_ok=True)
            if inherited is None:
                archive,fs=open_archive(io,source,folder,out.parent/("R927-download-"+label))
            else:
                archive,fs=None,entry_map(folder,source)
            archives[label]=archive;entries[label]=fs
            need={MANIFEST,*META,source["certificate"]["file"]}
            extract(archive,fs,folder,need)
            initial=source_review(label,source,folder,need)
            certs[label]=read(folder/source["certificate"]["file"])
            tags[label]=certs[label]["configuration"]
            names[label]=need
        def take(label,row):
            row=plain(row)
            assert entries[label][row["file"]]==row
            extract(archives[label],entries[label],retained/label,[row["file"]])
            names[label].add(row["file"])
            value=stage(retained/label,entries[label],row,tags[label],item["source_artifacts"][label])
            return value,{**row,"source_group":label}
        def pin(label,key):
            return take(label,item["input_pins"][key])
        reference,rref=take("R879",certs["R879"]["reference_function_and_pencil"])
        assert plain(rref)==plain(item["input_pins"]["reference_function"])
        take("R879",reference["source_unit_solution"])
        take("R879",certs["R879"]["source_audit"])
        u,uref=take("R872",reference["source_anchor_u"])
        b,bref=take("R872",reference["source_anchor_b"])
        assert plain(uref)==plain(item["input_pins"]["anchor_u"])
        assert plain(bref)==plain(item["input_pins"]["anchor_b"])
        fixed,fref=take("R872",certs["R872"]["fixed_chi_divisor_and_principal_function"])
        take("R872",certs["R872"]["source_audit"])
        P0,pref=pin("R914","P0_V1_jets")
        point,pointref=pin("R914","P1_point_check")
        inputs={"reference_function":rref,"anchor_u":uref,"anchor_b":bref,
                "fixed_chi_divisor":fref,"P0_V1_jets":pref,"P1_point_check":pointref,"endpoints":{}}
        assert identity(reference["source_R872"])==identity(item["source_artifacts"]["R872"])
        assert identity(certs["R923"]["source_identities"]["R917"])==identity(item["source_artifacts"]["R917"])
        assert identity(certs["R917"]["source_identities"]["R914"])==identity(item["source_artifacts"]["R914"])
        assert certs["R923"]["actual_original_two_endpoint_target_normal_coordinates_certified"] is True
        for epsilon in (0,1):
            e=str(epsilon)
            target,tref=take("R923",certs["R923"]["completed_endpoint_certificates"][e])
            operators,oref=take("R923",target["target_operators"])
            blocks=[]
            for row in target["complete_target_normal_coordinate_blocks"]:
                _,s=take("R923",row);blocks.append(s)
            take("R923",target["all_original_normal_equations"])
            old,oldref=take("R917",target["source_original_order_certificate"])
            normal,nref=take("R917",target["source_original_normal_order"])
            frame,fr=take("R917",target["source_original_primitive_and_t_frames"])
            assert plain(oldref)==plain(certs["R917"]["completed_endpoint_certificates"][e])
            assert plain(old["complete_normal_order"])==plain(nref)
            assert plain(old["primitive_and_t_frames"])==plain(fr)
            assert normal["order"]["all_factors_and_nilpotents_retained"] is True
            inputs["endpoints"][e]={"target_certificate":tref,"target_operators":oref,
                "target_blocks":blocks,"order_certificate":oldref,"normal_order":nref,"frame":fr}
        groups={}
        for label in SOURCES:
            groups[label]=source_review(label,item["source_artifacts"][label],retained/label,names[label])
            if inherited is not None:
                assert groups[label]==inherited[label]
        if inherited is None:
            write_bundle(out,retained,groups)
        else:
            receipt=read(out/INPUT_RECEIPT)
            assert receipt["selected_original_file_count"]==sum(g["selected_file_count"] for g in groups.values())
        expanded={**item,"topic_directory":str(TOPIC),"inputs":inputs,
            "sources":{k:{**v,"directory":str(retained/k)} for k,v in groups.items()}}
        save(out/EXPANDED,expanded)
        return expanded
    finally:
        for archive in archives.values():
            if archive is not None:
                archive.close()



def restore(item,out,io):
    source=item.get("resume")
    if source is None:
        return None
    assert source["result"]==RESULT and source["core_sha256"]==item["core_sha256"]
    folder=out.parent/"R927-resume-source"
    archive,entries=open_archive(io,source,folder,out.parent/"R927-resume-range")
    try:
        names={META[0],META[1],BUNDLE,SOURCE_INVENTORY,INPUT_RECEIPT}
        if META[2] in entries:
            names.add(META[2])
        extract(archive,entries,folder,names)
        initial,run=read(folder/META[0]),read(folder/META[1])
        assert initial["result"]==run["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]==source["source_commit"]
        assert str(run["workflow_run_id"])==str(source["run_id"])
        assert initial["core_sha256"]==item["core_sha256"]
        assert stable_request(initial["job"])==stable_request(item)
        if source.get("wrapper_sha256") is not None:
            assert initial["wrapper_sha256"]==source["wrapper_sha256"]
        assert run["process_exit_code"] in source["accepted_process_exit_codes"]
        core=None
        if META[2] in entries:
            core=read(folder/META[2])
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
            assert run["core_receipt_sha256"]==entries[META[2]]["sha256"]
        else:
            assert run["complete"] is False and run["core_receipt_sha256"] is None
        for name in (BUNDLE,SOURCE_INVENTORY,INPUT_RECEIPT):
            if (out/name).exists():
                assert spec(out/name)==entries[name]
            else:
                shutil.copyfile(folder/name,out/name)
        expanded=prepare_sources(item,out,io)
        tag=expected_tag(expanded)
        assert initial["actual_configuration"]==tag
        if core is not None:
            assert core["configuration_sha256"] in (None,fingerprint(tag))
        completed=sorted(n for n in entries if n.startswith(PREFIX) and n.endswith(".json.gz"))
        extract(archive,entries,out,completed)
        for name in completed:
            value=read(out/name)
            assert value["result"]==RESULT and value["configuration"]==tag
            assert value["complete"] is (name!=CURRENT)
        restored_success=False
        reused_parent=None
        if FINAL in entries:
            extract(archive,entries,folder,[FINAL])
            final=read(folder/FINAL)
            assert final["result"]==RESULT and final["configuration"]==tag
            assert isinstance(final["complete"],bool)
            if final["complete"]:
                assert core is not None and core["complete"] is True
                assert run["complete"] is True and run["process_exit_code"]==0
                assert core["certificate_sha256"]==entries[FINAL]["sha256"]
                inventory=read(bound(out,final["stage_manifest"]))
                assert inventory["configuration"]==tag and inventory["complete"] is True
                for row in inventory["files"]:
                    bound(out,row)
                bound(out,final["resume_state"])
                if (out/FINAL).exists():
                    assert spec(out/FINAL)==entries[FINAL]
                else:
                    shutil.copyfile(folder/FINAL,out/FINAL)
                restored_success=True
                retained_metadata={}
                for name in (MANIFEST,*META):
                    original=entries[name]
                    alias="R927-reused-parent-"+name
                    path=out/alias
                    if path.exists():
                        assert spec(path)==dict(original,file=alias)
                    else:
                        shutil.copyfile(folder/name,path)
                    retained_metadata[name]={"original":original,"retained":spec(path)}
                if (out/META[2]).exists():
                    assert spec(out/META[2])==entries[META[2]]
                else:
                    shutil.copyfile(folder/META[2],out/META[2])
                reused_parent={
                    "source":source,"original_complete_certificate":entries[FINAL],
                    "original_complete_core_receipt":entries[META[2]],
                    "retained_original_metadata":retained_metadata,
                    "actual_parent_process_exit_code":run["process_exit_code"],
                    "actual_parent_run_complete":run["complete"],
                    "actual_parent_core_complete":core["complete"],
                    "all_original_complete_math_stages_and_FINAL_reused_byte_for_byte":True,
                    "core_reexecuted":False}
        save(out/"resume-inheritance-receipt.json",{
            "result":RESULT,"complete":True,"source_resume":source,
            "source_manifest":spec(folder/MANIFEST),
            "restored_complete_and_current_files":[entries[n] for n in completed],
            "restored_true_final":restored_success,"reused_actual_parent":reused_parent,
            "false_final_is_historical_not_completion_or_current_SHA_constraint":True,
            "range_transport":archive.receipt(),
            "new_or_old_mathematics_executed_by_transport":False})
        return {"expanded":expanded,"reused_actual_parent":reused_parent}
    finally:
        archive.close()


def write_manifest(out):
    rows=[dict(spec(path),included_in_git=False) for path in sorted(out.iterdir())
          if path.is_file() and path.name not in (MANIFEST,REFERENCE)
          and not path.name.endswith((".tmp",".download",".partial"))]
    save(out/MANIFEST,{"result":RESULT,"files":rows,
        "temporary_active_checkpoint_retention_days":1,
        "reproducible_mathematical_data_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,"manifest_file":MANIFEST,
        "manifest_bytes":(out/MANIFEST).stat().st_size,"manifest_sha256":sha(out/MANIFEST),
        "file_count":len(rows)})


def compute(item,out,io):
    out.mkdir(parents=True,exist_ok=True)
    code,error,outer_timeout,proc=1,None,False,None
    core_reexecuted=False
    reused_parent=None
    try:
        inherited=restore(item,out,io)
        expanded=inherited["expanded"] if inherited is not None else prepare_sources(item,out,io)
        reused_parent=None if inherited is None else inherited["reused_actual_parent"]
        receipt=read(out/INPUT_RECEIPT)
        save(out/META[0],{
            "result":RESULT,"p":41,"source_repository":"Rogerhu12/math-research-public",
            "source_commit":os.environ["GITHUB_SHA"],"core_sha256":item["core_sha256"],
            "wrapper_sha256":sha(__file__),"request_sha256":sha(REQUEST),"job":item,
            "method_sha256":item["method_sha256"],"proofs":item["proofs"],
            "actual_configuration":expected_tag(expanded),
            "source_inventory":receipt["source_inventory"],"input_bundle":receipt["input_bundle"],
            "workflow_sha256":sha(REPO/item["workflow"]),
            "prepared_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
            "all_new_mathematics_only_in_separate_public_Actions_core":True,
            "reused_actual_parent":reused_parent,
            "complete_parent_reuse_requires_no_core_invocation":reused_parent is not None})
        if reused_parent is not None:
            # restore already checked the original complete FINAL, core receipt,
            # original run/source identity and every original complete stage.
            # Keep the original core receipt bytes; this is an IO-only new run.
            assert reused_parent["core_reexecuted"] is False
            assert read(out/FINAL)["complete"] is True and read(out/META[2])["complete"] is True
            code=0
            record={"result":RESULT,"core_reexecuted":False,
                "reused_actual_parent":reused_parent,
                "new_mathematical_stage_count":0}
            line="R927_REFERENCE_COMPLETED_SOURCE_REUSED="+json.dumps(record,sort_keys=True)
            (out/"public-actions-run.log").write_text(line+"\n",encoding="utf-8")
            print(line,flush=True)
        else:
            command=[sys.executable,str(HERE/item["core"]),"--config",str(out/EXPANDED),
                     "--out",str(out),"--budget-minutes",str(item["budget_minutes"])]
            with (out/"public-actions-run.log").open("w",encoding="utf-8") as log:
                proc=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
                core_reexecuted=True
                try:
                    code=proc.wait(timeout=60*item["budget_minutes"]+600)
                except subprocess.TimeoutExpired:
                    outer_timeout,code=True,124
                    os.killpg(proc.pid,signal.SIGTERM)
                    try:
                        proc.wait(timeout=30)
                    except subprocess.TimeoutExpired:
                        os.killpg(proc.pid,signal.SIGKILL)
                        proc.wait()
                    error="Actual outer timeout; completed atomic stages and current checkpoint retained."
            with (out/"public-actions-run.log").open("r",encoding="utf-8",errors="replace") as log:
                for line in log:
                    print(line,end="",flush=True)
    except BaseException as exc:
        traceback.print_exc()
        code=1
        error=type(exc).__name__+": "+str(exc)
    finally:
        core=read(out/META[2]) if (out/META[2]).exists() else None
        complete=bool(code==0 and core and core["complete"] is True and (out/FINAL).exists())
        save(out/META[1],{
            "result":RESULT,"p":41,"source_commit":os.environ.get("GITHUB_SHA"),
            "workflow_run_id":os.environ.get("GITHUB_RUN_ID"),
            "workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT"),
            "complete":complete,"process_exit_code":code,"outer_timeout":outer_timeout,
            "error":error,"core_receipt_sha256":sha(out/META[2]) if core else None,
            "core_reexecuted":core_reexecuted,"reused_actual_parent":reused_parent,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
            "execution_environment":"public_GitHub_Actions"})
        write_manifest(out)
    return code


def own(out,row,tag):
    value=read(bound(out,row))
    assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
    return value


def shape(value,dimensions):
    if not dimensions:
        assert isinstance(value,int) and not isinstance(value,bool) and 0<=value<PRIME
        return
    assert isinstance(value,list) and len(value)==dimensions[0]
    for entry in value:
        shape(entry,dimensions[1:])


def own_live_refs(out,value,tag):
    # Original source identities contain historical specs. Only live filenames
    # from this producer are interpreted as new output references.
    if isinstance(value,dict):
        if {"file","bytes","sha256"}<=set(value) and isinstance(value["file"],str):
            name=value["file"]
            if name.startswith(PREFIX):
                referenced=read(bound(out,value))
                assert referenced["result"]==RESULT and referenced["configuration"]==tag
                assert referenced["complete"] is (name!=CURRENT)
                return
        for key,entry in value.items():
            if key!="configuration":
                own_live_refs(out,entry,tag)
    elif isinstance(value,list):
        for entry in value:
            own_live_refs(out,entry,tag)


def endpoint_review(out,row,epsilon,tag,inputs,common):
    value=own(out,row,tag)
    assert value["endpoint"]==epsilon and value["prime"]==PRIME
    assert value["original_zeta_root"]==ZETA and value["original_s_root"]==SROOT
    assert value["local_parameter"]==STRATEGY["endpoint_parameters"][epsilon]
    old=inputs["endpoints"][str(epsilon)]
    assert value["source_original_reference_function"]==inputs["reference_function"]
    for source_key,input_key in (
        ("source_original_normal_order","normal_order"),
        ("source_original_target_certificate","target_certificate"),
        ("source_original_order_and_t_frame","frame")):
        assert value[source_key]==old[input_key]
    assert value["source_common_global_reference_frame"]==common[0]
    lam=common[1]["actual_common_integer_parameter_lambda0"]
    assert value["actual_common_integer_parameter_lambda0"]==lam and 0<=lam<=16
    r=value["target_P0_block_rank"];rc=value["complement_rank"]
    assert isinstance(r,int) and 0<=r<=8 and rc==8-r
    N=value["actual_working_rho_precision"]
    assert 1<=N<=CAP and N<=value["actual_original_target_input_precision"]
    shape(value["complete_relative_first_generator_matrix_mod_rho"],[8,8])
    shape(value["complete_relative_second_generator_matrix_mod_rho"],[8,8])
    shape(value["nine_reference_relative_coordinates_mod_prime"],[9])
    assert value["original_nine_parameters"]==list(range(9))
    for key in (
        "all64_reverse_identity_coefficients_verified",
        "all9_complete_rank8_determinants_equal_primitive_polynomial_values",
        "both_determinant_factors_under_dual7_retained",
        "actual_reference_local_ideal_and_relative_coordinates_at_original_place_certified",
        "actual_reference_complete_Norm_frame_at_original_place_computed",
        "all_original_eight_factors_and_nilpotents_preserved"):
        assert value[key] is True
    for key in (
        "characteristic_zero_expanded_coordinates_or_observed_orders_claimed",
        "full_Laurent_lattice_basis_expanded",
        "five_target_NormPhi_or_Poincare_frame_computed",
        "Picard_inactive_or_height_computed"):
        assert value[key] is False
    assert value["original_P0_block_exact_inverse_reference_order_lower_bound"]==254
    assert value["P0_block_relative_matrix_zero_bound_in_rho"]==(84 if r else None)
    for key in ("actual_reference_norm_rho_leading_mod_prime",
                "actual_original_t_over_rho_mod_prime","actual_reference_norm_t_leading_mod_prime"):
        assert isinstance(value[key],int) and 0<value[key]<PRIME
    assert isinstance(value["actual_reference_norm_rho_order"],int)
    assert -2032<=value["actual_reference_norm_rho_order"]<=0
    assert value["original_dual7"]["frozen_direction"]=="Nm_pi_t(pi_s^*I)"
    assert value["original_dual7"]["determinant_numerator_and_denominator_both_transported"] is True
    assert value["original_nu"]["iota_fixes_nu"] is True
    ideal=value["original_reference_lattice_exact_expression"]
    assert ideal["operation"]=="positive_principal_fractional_B_ideal"
    assert ideal["lambda0"]==lam and ideal["source_original_reference"]==inputs["reference_function"]
    assert ideal["exact_reverse_relation"]=="C0+lambda0*C1=identity"
    assert value["original_determinant_exact_expression"]["same_original_reference_scalar_and_generic_frame_retained"] is True
    prepared=own(out,value["source_prepared_endpoint"],tag)
    assert prepared["endpoint"]==epsilon and prepared["target_P0_block_rank"]==r and prepared["complement_rank"]==rc
    assert prepared["new_reference_endpoint_preparation_complete"] is True
    assert prepared["future_five_target_pencils_computed"] is False
    residue=own(out,prepared["source_complete_residue_summand"],tag)
    assert residue["target_P0_block_rank"]==r and residue["complement_rank"]==rc
    shape(residue["target_P0_ideal_generators_mod_prime"],[145,8])
    assert len(residue["generator_labels"])==145
    assert [x["power"] for x in residue["complete_ideal_power_sequence"]]==list(range(1,9))
    shape(residue["complete_residue_basis_mod_prime"],[8,8])
    shape(residue["complete_residue_basis_inverse_mod_prime"],[8,8])
    for key in ("all_complete_ideal_and_annihilator_products_verified","all_eight_dimensions_and_nilpotents_retained"):
        assert residue[key] is True
    assert residue["empty_target_P0_block"] is (r==0)
    assert residue["empty_complement"] is (rc==0)
    lifted=own(out,value["source_complete_block_basis"],tag)
    assert lifted["absolute_rho_precision"]==N
    assert lifted["target_P0_block_rank"]==r and lifted["complement_rank"]==rc
    shape(lifted["complete_block_basis_in_original_basis"],[8,8,N])
    shape(lifted["original_basis_in_complete_block_basis"],[8,8,N])
    shape(lifted["target_P0_idempotent"],[8,N])
    shape(lifted["complement_idempotent"],[8,N])
    for key in ("both_full8_basis_inverse_products_verified",
                "full_idempotent_orthogonality_and_sum_one_verified",
                "no_factors_or_nilpotents_removed"):
        assert lifted[key] is True
    norm=own(out,prepared["source_parameter_norm"],tag)
    assert norm["target_P0_block_rank"]==r and norm["absolute_rho_precision"]==N
    m=norm["actual_parameter_norm_order"]
    assert isinstance(m,int) and ((m==0) if r==0 else (1<=m<=8))
    assert 0<norm["actual_parameter_norm_leading_mod_prime"]<PRIME
    assert norm["empty_block_norm_equals_one"] is (r==0)
    if r==0:
        assert norm["actual_parameter_norm_leading_mod_prime"]==1
    shape(norm["complete_parameter_norm_series"],[N])
    regular=own(out,value["source_reference_regular_complement"],tag)
    assert regular["complement_rank"]==rc and regular["absolute_rho_precision"]==N
    assert 0<=regular["actual_unit_representation_parameter_eta"]<=8
    for key in ("complete_denominator_multiplication","complete_denominator_inverse",
                "complete_numerator_multiplication","complete_reference_multiplication"):
        shape(regular[key],[rc,rc,N])
    shape(regular["C_complement_coefficients_ascending_T_mod_prime"],[rc+1])
    assert regular["C_complement_coefficients_ascending_T_mod_prime"][0]==1
    for key in ("both_complete_unit_inverse_products_verified","both_complete_quotient_products_verified",
                "complete_characteristic_matrix_identity_verified","C_complement_zero_parameter_is_one",
                "no_nonunit_denominator_or_reduced_quotient_used"):
        assert regular[key] is True
    assert regular["empty_complement_unit_and_norm_equal_one"] is (rc==0)
    return {"certificate":plain(row),"endpoint":epsilon,"target_P0_block_rank":r,
        "complement_rank":rc,"actual_target_input_precision":value["actual_original_target_input_precision"],
        "actual_working_precision":N,"actual_common_lambda0":lam,
        "actual_parameter_norm_order":m,
        "actual_parameter_norm_leading_mod_prime":norm["actual_parameter_norm_leading_mod_prime"],
        "actual_reference_norm_rho_order":value["actual_reference_norm_rho_order"],
        "actual_reference_norm_rho_leading_mod_prime":value["actual_reference_norm_rho_leading_mod_prime"],
        "actual_reference_norm_t_leading_mod_prime":value["actual_reference_norm_t_leading_mod_prime"],
        "nine_relative_coordinates":value["nine_reference_relative_coordinates_mod_prime"],
        "characteristic_zero_content_orders_claimed":False}


def review_reused_complete_parent(item,out,initial,run,entries,tag):
    parent=run.get("reused_actual_parent")
    assert initial.get("reused_actual_parent")==parent
    if parent is None:
        assert run.get("core_reexecuted") is True
        return None
    assert run["core_reexecuted"] is False and parent["core_reexecuted"] is False
    assert initial["complete_parent_reuse_requires_no_core_invocation"] is True
    assert item.get("resume") is not None and parent["source"]==item["resume"]
    source=parent["source"]
    assert source["result"]==RESULT and source["core_sha256"]==item["core_sha256"]
    originals={}
    raw=parent["retained_original_metadata"]
    assert set(raw)=={MANIFEST,*META}
    for name,record in raw.items():
        original,retained=plain(record["original"]),plain(record["retained"])
        assert original["file"]==name and retained["file"]=="R927-reused-parent-"+name
        assert retained["bytes"]==original["bytes"] and retained["sha256"]==original["sha256"]
        assert entries[retained["file"]]==retained
        originals[name]=read(bound(out,retained))
    original_manifest=originals[MANIFEST]
    assert raw[MANIFEST]["original"]["sha256"]==source["manifest_sha256"]
    assert raw[MANIFEST]["original"]["bytes"]==source["manifest_bytes"]
    fs={row["file"]:plain(row) for row in original_manifest["files"]}
    assert original_manifest["result"]==RESULT and len(fs)==len(original_manifest["files"])==source["manifest_file_count"]
    for name in META:
        assert fs[name]==plain(raw[name]["original"])
    old_initial,old_run,old_core=(originals[name] for name in META)
    assert old_initial["source_commit"]==old_run["source_commit"]==source["source_commit"]
    assert str(old_run["workflow_run_id"])==str(source["run_id"])
    assert old_initial["core_sha256"]==old_core["source_sha256"]==item["core_sha256"]
    if source.get("wrapper_sha256") is not None:
        assert old_initial["wrapper_sha256"]==source["wrapper_sha256"]
    assert stable_request(old_initial["job"])==stable_request(item)
    assert old_initial["actual_configuration"]==tag
    assert old_run["complete"] is True and old_run["process_exit_code"]==0
    assert old_core["complete"] is True and old_core["process_exit_code"]==0
    assert old_run["core_receipt_sha256"]==fs[META[2]]["sha256"]
    assert old_core["configuration_sha256"]==fingerprint(tag)
    assert parent["original_complete_core_receipt"]==fs[META[2]]==entries[META[2]]
    assert parent["original_complete_certificate"]==fs[FINAL]==entries[FINAL]
    assert old_core["certificate_sha256"]==fs[FINAL]["sha256"]
    assert parent["actual_parent_process_exit_code"]==0
    assert parent["actual_parent_run_complete"] is True and parent["actual_parent_core_complete"] is True
    assert parent["all_original_complete_math_stages_and_FINAL_reused_byte_for_byte"] is True
    actual_stages={name:row for name,row in fs.items() if name.startswith(PREFIX) and name.endswith(".json.gz")}
    assert actual_stages
    for name,row in actual_stages.items():
        assert entries[name]==row
    return {"source":identity(source),"original_core_receipt":fs[META[2]],
        "original_complete_certificate":fs[FINAL],"core_reexecuted":False,
        "all_original_complete_stage_bytes_preserved":True,"new_mathematical_stage_count":0}


def verify(item,out,io):
    manifest=read(out/MANIFEST)
    assert manifest["result"]==RESULT
    entries={row["file"]:plain(row) for row in manifest["files"]}
    assert len(entries)==len(manifest["files"])
    for row in entries.values():
        bound(out,row)
    reference=read(out/REFERENCE)
    assert reference["manifest_sha256"]==sha(out/MANIFEST)
    assert reference["manifest_bytes"]==(out/MANIFEST).stat().st_size
    assert reference["file_count"]==len(entries)
    run=read(out/META[1])
    assert run["result"]==RESULT and str(run["workflow_run_id"])==str(os.environ["GITHUB_RUN_ID"])
    assert run["source_commit"]==os.environ["GITHUB_SHA"]
    if META[0] not in entries:
        assert run["complete"] is False and run["process_exit_code"]!=0
        assert run["core_receipt_sha256"] is None
        print("R927_REFERENCE_SOURCE_PREPARATION_FAILED="+json.dumps(run,sort_keys=True),flush=True)
        return 0
    initial=read(out/META[0])
    assert initial["result"]==RESULT and initial["source_commit"]==run["source_commit"]
    assert initial["core_sha256"]==item["core_sha256"] and initial["wrapper_sha256"]==item["wrapper_sha256"]
    assert stable_request(initial["job"])==stable_request(item)
    assert {BUNDLE,SOURCE_INVENTORY,INPUT_RECEIPT}<=set(entries)
    expanded=prepare_sources(item,out,io)
    tag=expected_tag(expanded)
    inputs=expanded["inputs"]
    receipt=read(out/INPUT_RECEIPT)
    assert initial["actual_configuration"]==tag
    assert initial["source_inventory"]==receipt["source_inventory"]
    assert initial["input_bundle"]==receipt["input_bundle"]
    core=read(out/META[2]) if META[2] in entries else None
    if core is not None:
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        assert run["core_receipt_sha256"]==entries[META[2]]["sha256"]
        assert core["configuration_sha256"] in (None,fingerprint(tag))
        assert core["five_target_NormPhi_theta_Poincare_or_height_computed"] is False
    else:
        assert run["complete"] is False and run["core_receipt_sha256"] is None
    all_stages={}
    for name,row in entries.items():
        if name.startswith(PREFIX) and name.endswith(".json.gz"):
            value=read(out/name)
            assert value["result"]==RESULT and value["configuration"]==tag
            assert value["complete"] is (name!=CURRENT)
            own_live_refs(out,value,tag)
            if name not in (CURRENT,INVENTORY):
                all_stages[name]=row
    final=read(out/FINAL) if FINAL in entries else None
    endpoints={}
    if final is not None:
        assert final["result"]==RESULT and final["configuration"]==tag
        assert isinstance(final["complete"],bool)
        assert final["source_identities"]==tag["sources"]
        assert final["future_target_sources"]=={"R903":None,"R907":None}
        assert set(final["completed_endpoint_certificates"])<={"0","1"}
        assert final["actual_completed_endpoint_count"]==len(final["completed_endpoint_certificates"])
        for key in (
            "old_R917_normal_orders_R923_target_coordinates_or_R879_solution_recomputed",
            "new_original_point_jets_or_char0_coefficients_reconstructed",
            "full_Laurent_lattice_bases_expanded","characteristic_zero_observed_content_orders_claimed",
            "five_target_endpoint_ideal_lattices_computed",
            "five_target_NormPhi_detU_complete_calibration_computed",
            "Hecke_Picard_inactive_theta_Poincare_nonp_or_height_computed"):
            assert final[key] is False
        if core is not None:
            assert core["certificate_sha256"]==entries[FINAL]["sha256"]
        if final["same_global_reference_integer_frame"] is not None:
            common=own(out,final["same_global_reference_integer_frame"],tag)
            assert common["same_global_reference_generator_at_both_endpoints"] is True
            assert common["original_nine_global_parameters_unchanged"]==list(range(9))
            assert common["five_target_sources"]=={"R903":None,"R907":None}
            for epsilon,row in final["completed_endpoint_certificates"].items():
                endpoints[epsilon]=endpoint_review(out,row,int(epsilon),tag,inputs,
                    (final["same_global_reference_integer_frame"],common))
        else:
            assert final["completed_endpoint_certificates"]=={}
    if not run["complete"]:
        assert run["process_exit_code"]!=0 and (final is None or final["complete"] is False)
        if final is not None:
            for key in (
                "actual_original_two_endpoint_reference_ideals_and_relative_coordinates_certified",
                "actual_original_two_endpoint_reference_Norm_frames_computed",
                "actual_full_length8_algebras_and_nilpotents_preserved"):
                assert final[key] is False
        print("R927_REFERENCE_INCOMPLETE_IO_REVIEW="+json.dumps({
            "result":RESULT,"actual_complete_math_stages":len(all_stages),
            "core_receipt_present":core is not None,"actual_process_exit_code":run["process_exit_code"],
            "actual_stop":core.get("error") if core else run.get("error"),
            "actual_endpoint_stops":None if final is None else final["endpoint_stops"],
            "actual_completed_endpoint_count":len(endpoints),"completed_endpoints":endpoints,
            "actual_selected_original_file_count":receipt["selected_original_file_count"],
            "mathematics_reexecuted_by_wrapper":False},sort_keys=True),flush=True)
        return 0
    assert run["process_exit_code"]==0 and core is not None and core["complete"] is True
    reused=review_reused_complete_parent(item,out,initial,run,entries,tag)
    assert core["configuration_sha256"]==fingerprint(tag)
    assert final is not None and final["complete"] is True and final["stop_reason"] is None
    assert final["prime"]==PRIME and final["original_zeta_root"]==ZETA and final["original_s_root"]==SROOT
    assert final["actual_completed_endpoint_count"]==core["actual_completed_endpoint_count"]==2
    assert core["actual_original_two_endpoint_reference_Norm_frames_computed"] is True
    for key in ("actual_original_two_endpoint_reference_ideals_and_relative_coordinates_certified",
                "actual_original_two_endpoint_reference_Norm_frames_computed",
                "actual_full_length8_algebras_and_nilpotents_preserved"):
        assert final[key] is True
    assert set(endpoints)=={"0","1"} and final["endpoint_stops"]=={}
    inventory=own(out,final["stage_manifest"],tag)
    assert {row["file"]:plain(row) for row in inventory["files"]}==all_stages
    assert inventory["only_actual_complete_stages_listed"] is True
    assert inventory["current_checkpoint_excluded"] is True
    assert plain(final["resume_state"])["file"]==CURRENT
    current=read(bound(out,final["resume_state"]))
    assert current["configuration"]==tag and current["complete"] is False
    assert current["completed_endpoint_certificates"]==final["completed_endpoint_certificates"]
    assert current["prepared_endpoint_records"]==final["prepared_endpoint_records"]
    audit=own(out,final["source_audit"],tag)
    assert audit["source_identities"]==tag["sources"] and audit["inputs"]==inputs
    assert audit["new_target_normal_evaluations_or_old_point_jets_recomputed"] is False
    assert audit["five_original_target_pencil_sources"]=={"R903":None,"R907":None}
    assert audit["new_arithmetic_only_at_the_original_auxiliary_place"] is True
    comparison=own(out,final["complete_original_t_frame_comparison"],tag)
    assert comparison["source_two_complete_reference_frames"]==final["completed_endpoint_certificates"]
    assert comparison["same_global_reference_norm_function_at_both_original_endpoints"] is True
    assert comparison["both_original_determinant_factors_and_reference_norm_retained"] is True
    assert comparison["five_target_NormPhi_detU_and_reference_comparison_computed"] is False
    assert comparison["original_theta_Poincare_nonp_or_height_computed"] is False
    ratio=comparison["actual_original_t_frame_leading_ratio_P1_over_P0_mod_prime"]
    assert isinstance(ratio,int) and 0<ratio<PRIME
    print("R927_REFERENCE_COMPLETE_IO_REVIEW="+json.dumps({
        "result":RESULT,"certificate":entries[FINAL],"stage_manifest":final["stage_manifest"],
        "actual_complete_math_stages":len(all_stages),
        "actual_original_source_files":receipt["selected_original_file_count"],
        "endpoints":endpoints,"actual_original_t_frame_leading_ratio_P1_over_P0_mod_prime":ratio,
        "actual_five_target_NormPhi_detU_or_height_computed":False,
        "core_reexecuted":run["core_reexecuted"],"reused_actual_parent":reused,
        "mathematics_reexecuted_by_wrapper":False,"seconds":final["seconds"]},sort_keys=True),flush=True)
    return 0


def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--verify",action="store_true")
    args=parser.parse_args()
    item=read(REQUEST)
    io=guard(item)
    return verify(item,args.output,io) if args.verify else compute(item,args.output,io)


if __name__=="__main__":
    raise SystemExit(main())
