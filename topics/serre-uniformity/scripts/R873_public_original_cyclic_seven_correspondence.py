#!/usr/bin/env python3
"""R873 standard-library original-source transport, checkpoint IO, and public runner."""
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

S = Path(__file__).resolve().parent
TOPIC = S.parent
REPO = TOPIC.parent.parent
REPOSITORY = "Rogerhu12/math-research-public"
RESULT = "R873-original-cyclic-seven-correspondence"
FINAL = "p41-original-cyclic-seven-correspondence-certificate.json"
CORE = "R873_original_cyclic_seven_correspondence.py"
REQUEST = TOPIC/"notes/R873-original-cyclic-seven-correspondence-public-request.json"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R873-retained-original-inputs.tar.gz"
INVENTORY = "R873-original-source-inventory.json"
INPUT_RECEIPT = "R873-retained-inputs-receipt.json"
EXPANDED = "R873-expanded-job.json"
META = ("run-receipt.json", "core-receipt.json", "public-actions-input.json")
GROUPS = ("R771", "R775", "R786", "R799", "R800", "R801", "R807")
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
RANGE_FILE = "R824_public_original_global_polar_generators.py"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
ORIGINAL_SHA = "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851"
IO = None
COUNT, OLD_DIM, DIM, REAL, CYC = 110, 2050, 2058, 20, 40
FIRST, STOP, LEVEL, P = 196, 764, 82, 41
M2_INDICES = (0, 1, 2, 73)
STRATEGY = {
    "original_curve": "Y=X1/mu3; original minus3 descent; genus127",
    "original_level": 82,
    "original_three_sections": {"tau": [0], "sigma": [1, 73], "w0": [2]},
    "original_M2_scale_already_present": "6724",
    "source_projection": "retain E and original G-level82",
    "target_projection": "quotient E by its chosen cyclic7 subgroup",
    "slash": "det(A)*(c*tau+d)^-2*f(A*tau)",
    "finite_branch_coefficient_automorphism": 6,
    "infinity_branch_coefficient_automorphism": 7,
    "automorphisms_fix_s": True,
    "norm_scalar": "7^6; cancels 7*(1/7)^7",
    "primitive_target": "z=sigma/tau; nonzero q1 distinguishes all eight branches",
    "coarse_norm_space": "H0(8H+4(P0+P1))",
    "coarse_norm_space_dimension": DIM,
    "old_V8_dimension": OLD_DIM,
    "new_complement_dimension": 8,
    "complement_family": "(82^6 E6)^2 times original V2, in original order",
    "common_section_integer_scale": str(82**16),
    "qY_count": COUNT,
    "full_original_xi_coordinates": CYC,
    "full_original_real_coordinates": REAL,
    "selected_M2_indices": list(M2_INDICES),
    "new_M2_exponent_interval": [FIRST, STOP],
    "old_M2_or_E1_prefix_through_195_recomputed": False,
    "old_V8_or_V2_coefficients_or_basis_recomputed": False,
    "old_2050_inverse_previously_available": False,
    "norm_algorithm": "eight T values; division-free 7x7 Berkowitz over Z[xi][q,S]/(q^110,S^2)",
    "interpolation_nodes": list(range(8)),
    "target_coefficients": "P=F(T,0), K=-dF/dS(T,0)",
    "target_function_embedding": "z->U, w->K(U)/P'(U)",
    "char0_coordinate_output": "exact original integer minor inverse applied to exact selected RHS",
    "char0_coordinates_expanded": False,
    "norm_of_line_bundle": "Nm_target(source*I); dual7 involution required for source-norm implementation",
    "original_descent": "cY tau=tau; cY w0=w0; cY sigma=e1-e73; cY z=z-2 e73/tau",
    "old_W_theta_E6_or_Hecke_matrix_recomputed": False,
    "active_eta_support_or_principal_calibration_computed": False,
    "auxiliary_prime_policy": "ascending primes from739 excluding2,3,7,41 and singular old minor",
    "complement_batch_size": 32,
    "budget_excluded_from_mathematical_identity": True,
}


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(4*1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path=Path(path)
    with (gzip.open if path.suffix==".gz" else open)(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+".tmp")
    temp.write_text(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
    temp.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()


def plain(value):
    row={k:value[k] for k in ("file","bytes","sha256")}
    p=PurePosixPath(row["file"])
    assert len(p.parts)==1 and p.name not in ("",".","..") and "\\" not in row["file"]
    assert isinstance(row["bytes"],int) and row["bytes"]>=0
    assert re.fullmatch(r"[0-9a-f]{64}",row["sha256"])
    return row


def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}


def bound(folder,row):
    row=plain(row);path=Path(folder)/row["file"]
    assert spec(path)==row,(str(folder),row["file"],"bytes/SHA")
    return path


def topic_path(name):
    p=PurePosixPath(name)
    assert not p.is_absolute() and ".." not in p.parts
    result=(TOPIC/str(p)).resolve()
    assert result.is_relative_to(TOPIC.resolve())
    return result


def source_identity(value):
    return {**{k:value[k] for k in BASE},
            "configuration_sha256":value["configuration_sha256"],
            "certificate":plain(value["certificate"]),
            "selected_files_sha256":fingerprint(value["files"])}


def expected_tag(expanded):
    return {"result":RESULT,"source_sha256":expanded["core_sha256"],
            "python_flint":"0.9.0","p":41,"proofs":expanded["proofs"],
            "original_helper_sha256":ORIGINAL_SHA,
            "sources":{g:source_identity(expanded["retained_sources"][g]) for g in GROUPS},
            "inputs":expanded["inputs"],"strategy":STRATEGY}


def load_io():
    global IO
    path=S/RANGE_FILE
    assert sha(path)==RANGE_SHA
    module=importlib.util.spec_from_file_location("R873_frozen_Range_only_IO",path)
    IO=importlib.util.module_from_spec(module)
    module.loader.exec_module(IO)


def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve()
    assert item["result"]==RESULT and item["p"]==41 and item["producer_inputs_pending"] is False
    assert item["core"]==CORE and sha(S/CORE)==item["core_sha256"]
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["original_helper"]=="R786_exact_power5_short_basis.py"
    assert item["original_helper_sha256"]==sha(S/item["original_helper"])==ORIGINAL_SHA
    assert item["io_helper"]==RANGE_FILE and item["io_helper_sha256"]==RANGE_SHA
    assert 0<item["budget_minutes"]<=300
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert set(item["original_source_pins"])==set(GROUPS)
    assert set(item["source_artifacts"])=={"R799","R800","R801","R807","R837"}
    load_io()


def entry_map(directory,source):
    path=Path(directory)/MANIFEST
    assert sha(path)==source["manifest_sha256"]
    if "manifest_bytes" in source:
        assert path.stat().st_size==source["manifest_bytes"]
    data=read(path)
    assert data["result"]==source["result"]
    entries={r["file"]:plain(r) for r in data["files"]}
    assert len(entries)==len(data["files"])
    if "manifest_file_count" in source:
        assert len(entries)==source["manifest_file_count"]
    entries[MANIFEST]=spec(path)
    return entries


def metadata(directory,source,entries):
    directory=Path(directory)
    for name in META:
        bound(directory,entries[name])
    run,core,initial=(read(directory/name) for name in META)
    assert run["complete"] is True and run["process_exit_code"]==0
    assert str(run["workflow_run_id"])==str(source["run_id"])
    assert run["source_commit"]==initial["source_commit"]==source["source_commit"]
    assert run.get("error") is None
    assert core["complete"] is True and core["source_sha256"]==source["core_sha256"]
    assert core.get("result",source["result"])==initial.get("result",source["result"])==source["result"]
    if run.get("core_receipt_sha256") is not None:
        assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
    recorded=initial.get("core_sha256")
    if recorded is None:
        recorded=initial["job"]["core_sha256"]
    assert recorded==source["core_sha256"]
    assert initial.get("source_repository",REPOSITORY)==REPOSITORY
    name=source["certificate_name"]
    certificate=read(bound(directory,entries[name]))
    assert certificate["result"]==source["result"] and certificate["complete"] is True
    assert core["certificate_sha256"]==entries[name]["sha256"]
    if source.get("certificate_sha256") is not None:
        assert source["certificate_sha256"]==entries[name]["sha256"]
    tag=certificate["configuration"]
    assert tag.get("source_sha256",tag.get("core_sha256"))==source["core_sha256"]
    if source.get("configuration_sha256") is not None:
        assert fingerprint(tag)==source["configuration_sha256"]
    return certificate,tag,initial


def copy_bound(source,target,row):
    source=Path(source);target=Path(target)
    assert spec(source)==plain(row)
    target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():
        assert spec(target)==plain(row)
    else:
        shutil.copyfile(source,target)
    return target


def unpack_flat_package(path,directory):
    directory=Path(directory);directory.mkdir(parents=True,exist_ok=True)
    seen=set()
    with tarfile.open(path,"r:gz") as archive:
        for member in archive:
            relative=PurePosixPath(member.name)
            assert not relative.is_absolute() and ".." not in relative.parts and "\\" not in member.name
            if member.isdir():
                continue
            assert member.isfile() and not member.issym() and not member.islnk()
            name=relative.name
            assert name not in seen
            seen.add(name)
            target=directory/name
            with archive.extractfile(member) as source,target.open("wb") as destination:
                shutil.copyfileobj(source,destination)
            assert target.stat().st_size==member.size
    return seen


class Handle:
    """One original immutable producer, direct Range or a source-bound prepared package."""
    def __init__(self,label,item,work):
        self.label=label;self.source=item["source_artifacts"][label]
        self.directory=Path(work)/("source-"+label);self.directory.mkdir(parents=True,exist_ok=True)
        self.archive=None;self.transport={}
        prepared=item.get("prepared_transport")
        if prepared and label in prepared["packages"]:
            package_item=prepared["packages"][label]
            package=plain(package_item.get("package",package_item))
            outer_source=package_item.get("archive",prepared.get("archive"))
            assert outer_source is not None
            outer=IO.Archive(outer_source,Path(work)/("prepared-archive-"+label),whole=False)
            try:
                if outer_source.get("manifest_sha256") is not None:
                    manifest_path=Path(work)/("prepared-manifest-"+label+".json")
                    outer.extract_bound(MANIFEST,outer_source["manifest_sha256"],manifest_path,
                                        outer_source.get("manifest_bytes"))
                    entries={r["file"]:plain(r) for r in read(manifest_path)["files"]}
                    assert entries[package["file"]]==package
                package_path=Path(work)/package["file"]
                outer.extract_bound(package["file"],package["sha256"],package_path,package["bytes"])
                unpack_flat_package(package_path,self.directory)
                self.transport={"kind":"completed_original_source_intake",
                                "archive":outer_source,"package":package,
                                "range_receipt":outer.receipt()}
            finally:
                outer.close()
        else:
            self.archive=IO.Archive(self.source,Path(work)/("archive-"+label),whole=False)
            self.archive.extract_bound(MANIFEST,self.source["manifest_sha256"],self.directory/MANIFEST,
                                       self.source.get("manifest_bytes"))
        self.entries=entry_map(self.directory,self.source)
        self.take(list(META)+[self.source["certificate_name"]])
        self.certificate,self.tag,self.initial=metadata(self.directory,self.source,self.entries)

    def take(self,names):
        names=sorted(set(names))
        if self.archive is not None:
            self.archive.extract_many([(n,self.entries[n]["sha256"],self.directory/n,self.entries[n]["bytes"])
                                       for n in names if n!=MANIFEST])
        for name in names:
            bound(self.directory,self.entries[name])

    def get(self,name):
        self.take([name])
        return read(self.directory/name)

    def select(self,names,retained):
        names=sorted(set(names)|set(META)|{MANIFEST,self.source["certificate_name"]})
        self.take(names)
        target=Path(retained)/self.label;target.mkdir(parents=True,exist_ok=True)
        for n in names:
            copy_bound(self.directory/n,target/n,self.entries[n])
        if self.archive is not None:
            self.transport=self.archive.receipt()
        return names

    def close(self):
        if self.archive is not None:
            self.archive.close()


def inherited_bundle(path,root,allowed_groups,expected_inventory=None):
    """Hash selected original members; never import a mathematical source."""
    root=Path(root);root.mkdir(parents=True,exist_ok=True)
    seen=set()
    expected=None
    if expected_inventory is not None:
        expected={label+"/"+n:plain(row) for label,s in expected_inventory["sources"].items()
                  for n,row in s["files"].items()}
    with tarfile.open(path,"r:gz") as archive:
        for member in archive:
            relative=PurePosixPath(member.name)
            assert not relative.is_absolute() and ".." not in relative.parts and "\\" not in member.name
            if member.isdir():
                continue
            assert member.isfile() and not member.issym() and not member.islnk()
            assert len(relative.parts)==2 and member.name not in seen
            seen.add(member.name)
            label,name=relative.parts
            if expected is not None:
                assert member.name in expected and member.size==expected[member.name]["bytes"]
            assert label in allowed_groups
            target=root/label/name;target.parent.mkdir(parents=True,exist_ok=True)
            with archive.extractfile(member) as source,target.open("wb") as destination:
                shutil.copyfileobj(source,destination)
            assert target.stat().st_size==member.size
            if expected is not None:
                assert spec(target)==expected[member.name]
    if expected is not None:
        assert seen==set(expected)
    return seen


def review_group(group,pin,retained,names):
    directory=Path(retained)/group
    entries=entry_map(directory,pin)
    names=sorted(set(names)|set(META)|{MANIFEST,pin["certificate_name"]})
    for n in names:
        bound(directory,entries[n])
    certificate,tag,initial=metadata(directory,pin,entries)
    stage_entry=certificate.get("stage_manifest",certificate.get("stages_manifest"))
    if stage_entry is not None and stage_entry["file"] in names:
        stage=read(bound(directory,stage_entry))
        assert stage["complete"] is True and stage["configuration"]==tag
        inventory={r["file"]:plain(r) for r in stage["files"]}
        assert all(entries[n]==row for n,row in inventory.items())
    for n in names:
        if n in META or n in (MANIFEST,pin["certificate_name"]):
            continue
        value=read(directory/n)
        assert value["complete"] is True and value["configuration"]==tag,(group,n,"completed source tag")
    return {**{k:pin[k] for k in BASE},"certificate":entries[pin["certificate_name"]],
            "configuration_sha256":fingerprint(tag),
            "files":{n:entries[n] for n in names}}


def stage_spec(group,entry):
    return dict(plain(entry),source_group=group)


def pack(retained,sources,target):
    retained=Path(retained);target=Path(target);temporary=target.with_name(target.name+".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(filename="",fileobj=raw,mode="wb",mtime=0,compresslevel=2) as zipped:
            with tarfile.open(fileobj=zipped,mode="w|") as archive:
                for group,source in sorted(sources.items()):
                    for name,row in sorted(source["files"].items()):
                        p=bound(retained/group,row)
                        info=archive.gettarinfo(str(p),arcname=group+"/"+name)
                        info.uid=info.gid=0;info.uname=info.gname="";info.mtime=0
                        with p.open("rb") as stream:
                            archive.addfile(info,stream)
    temporary.replace(target)


def unpack_minimal(path,retained,sources):
    inventory={"sources":sources}
    inherited_bundle(path,retained,set(GROUPS),inventory)


def same_original_source(pin,actual):
    for key in BASE:
        assert str(pin[key])==str(actual[key]),("original producer",key)
    if "certificate_name" in actual:
        assert pin["certificate_name"]==actual["certificate_name"]
    if "certificate" in actual:
        assert pin["certificate_name"]==actual["certificate"]["file"]
        assert pin["certificate_sha256"]==actual["certificate"]["sha256"]
    elif "files" in actual and pin["certificate_name"] in actual["files"]:
        value=actual["files"][pin["certificate_name"]]
        digest=value if isinstance(value,str) else value["sha256"]
        assert pin["certificate_sha256"]==digest



def import_completed_source_carrier(item,out):
    """Reuse the actual source-only failed R873 run, without importing its math tag."""
    previous=item["completed_source_carrier"]
    assert previous["result"]==RESULT
    assert previous["no_completed_mathematical_stages_expected"] is True
    assert previous["expected_conclusion"]=="failure"
    folder=out.parent/"completed-R873-source-carrier"
    folder.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(previous,out.parent/"completed-R873-source-archive",whole=False)
    try:
        archive.extract_bound(MANIFEST,previous["manifest_sha256"],folder/MANIFEST,
                              previous["manifest_bytes"])
        original_manifest=read(folder/MANIFEST)
        assert original_manifest["result"]==RESULT
        entries={row["file"]:plain(row) for row in original_manifest["files"]}
        assert len(entries)==len(original_manifest["files"])
        assert not any(n.startswith("R873-") and n.endswith(".json.gz") for n in entries)
        names=list(META)+[BUNDLE,INVENTORY,INPUT_RECEIPT,EXPANDED]
        archive.extract_many([(n,entries[n]["sha256"],folder/n,entries[n]["bytes"]) for n in names])
        initial=read(folder/"public-actions-input.json")
        run=read(folder/"run-receipt.json")
        core=read(folder/"core-receipt.json")
        assert initial["result"]==run["result"]==core["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]==previous["source_commit"]
        assert str(run["workflow_run_id"])==str(previous["run_id"])
        assert initial["core_sha256"]==run["core_sha256"]==core["source_sha256"]==previous["core_sha256"]
        assert initial["wrapper_sha256"]==run["wrapper_sha256"]==previous["wrapper_sha256"]
        assert run["complete"] is False and core["complete"] is False
        assert run["process_exit_code"]==core["process_exit_code"]==1
        assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]==previous["core_receipt_sha256"]
        assert core["configuration"] is None and core["certificate_sha256"] is None
        assert FINAL not in entries
        old_item=initial["job"]
        keys=("result","p","producer_inputs_pending","original_helper","original_helper_sha256",
              "proofs","original_source_pins","selection_pins")
        assert all(old_item[k]==item[k] for k in keys)
        old_expanded=read(folder/EXPANDED)
        assert initial["expanded_job"]==entries[EXPANDED]
        assert old_expanded["core_sha256"]==previous["core_sha256"]
        assert initial["mathematical_configuration_sha256"]==fingerprint(expected_tag(old_expanded))
        inventory=read(folder/INVENTORY);receipt=read(folder/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        assert plain(receipt["source_bundle"])==entries[BUNDLE]==plain(previous["input_bundle"])
        assert plain(receipt["source_inventory"])==entries[INVENTORY]==plain(previous["source_inventory"])
        assert receipt["selected_file_count"]==previous["selected_file_count"]==4960
        assert old_expanded["retained_sources"]==inventory["sources"]
        assert old_expanded["inputs"]==inventory["inputs"]
        for group in GROUPS:
            same_original_source(item["original_source_pins"][group],inventory["sources"][group])
        for name in (BUNDLE,INVENTORY,INPUT_RECEIPT):
            copy_bound(folder/name,out/name,entries[name])
        # Only the transport config changes. Every original producer file/tag remains verbatim.
        expanded=dict(item,retained_sources=inventory["sources"],inputs=inventory["inputs"])
        save(out/EXPANDED,expanded)
        save(out/"source-carrier-import-receipt.json",{
            "result":RESULT,"complete":True,"source":previous,
            "original_manifest":spec(folder/MANIFEST),
            "original_expanded_job":entries[EXPANDED],
            "source_bundle":entries[BUNDLE],"source_inventory":entries[INVENTORY],
            "original_input_receipt":entries[INPUT_RECEIPT],
            "original_selected_file_count":4960,"mathematical_stages_imported":0,
            "original_seven_producer_identities_preserved":True,
            "old_core_or_configuration_impersonated":False,
            "original_source_byte_revalidation_required_before_new_math":True,
            "range_transport":archive.receipt()})
    finally:
        archive.close()


def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R873";retained.mkdir(parents=True,exist_ok=True)
    if all((out/n).exists() for n in (BUNDLE,INVENTORY,INPUT_RECEIPT,EXPANDED)):
        inventory=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        bound(out,receipt["source_inventory"]);bound(out,receipt["source_bundle"])
        unpack_minimal(out/BUNDLE,retained,inventory["sources"])
        for g,source in inventory["sources"].items():
            same_original_source(item["original_source_pins"][g],source)
            assert review_group(g,item["original_source_pins"][g],retained,source["files"])==source
        expanded=dict(item,retained_sources=inventory["sources"],inputs=inventory["inputs"])
        old=read(out/EXPANDED)
        assert expected_tag(old)==expected_tag(expanded)
        save(out/EXPANDED,expanded)
        return retained,expanded,receipt
    assert allow_download,"A completed R873 carrier is required for verify-only."
    if item.get("completed_source_carrier") is not None:
        import_completed_source_carrier(item,out)
        return prepare(item,out,allow_download=False)
    handles={};transport={}
    try:
        # These are the earliest-expiring sources; all their mathematical bytes are reused.
        for label in ("R800","R799","R801","R807","R837"):
            handles[label]=Handle(label,item,out.parent)
        h800,h799,h801,h807,h837=(handles[g] for g in ("R800","R799","R801","R807","R837"))
        old800=h800.initial.get("job",h800.initial)
        original=old800["retained_artifacts"]
        for g in ("R771","R775","R786"):
            same_original_source(item["original_source_pins"][g],original[g])
        input800=item["carrier_specs"]["R800"]
        assert h800.entries[input800["file"]]==plain(input800)
        h800.take([input800["file"]])
        if (h800.directory/"retained-inputs-receipt.json").exists() or h800.archive is not None:
            prior_receipt=h800.get("retained-inputs-receipt.json")
            assert plain(prior_receipt["input_bundle"])==plain(input800)
        raw800=out.parent/"inherited-R800"
        inherited_bundle(h800.directory/input800["file"],raw800,{"R771","R775","R786"})
        selected={}
        for g in ("R771","R775","R786"):
            pin=item["original_source_pins"][g]
            entries=entry_map(raw800/g,pin)
            names=set(META)|{MANIFEST,pin["certificate_name"]}
            if g=="R771":
                names.add("R771-original-level82-Eisenstein-label-group.json.gz")
                names.update(f"R771-Eisenstein-row-{i:02d}.json.gz" for i in range(82))
            elif g=="R775":
                names.update(("R775-basis-M2.json.gz","R775-determinant-cosets.json.gz"))
            else:
                names.add("R786-exact-stages-manifest.json.gz")
                names.update(f"R786-exact-integral-E1-row-{i:02d}.json.gz" for i in range(82))
                names.update(f"R786-exact-power-1-row-{i:04d}.json.gz" for i in range(146))
            directory=retained/g;directory.mkdir(exist_ok=True)
            for n in names:
                copy_bound(raw800/g/n,directory/n,entries[n])
            selected[g]=names
        # Current R837 transports completed R786 V2, not a new R786 producer.
        input837=item["carrier_specs"]["R837"]
        for row in (input837,item["R837_inventory"]):
            assert h837.entries[row["file"]]==plain(row)
            h837.take([row["file"]])
        inv837=h837.get(item["R837_inventory"]["file"])
        receipt837=h837.get("R837-retained-inputs-receipt.json")
        assert plain(receipt837["source_bundle"])==plain(input837)
        assert plain(receipt837["source_inventory"])==plain(item["R837_inventory"])
        assert inv837["result"]==h837.source["result"] and inv837["complete"] is True
        same_original_source(item["original_source_pins"]["R786"],inv837["sources"]["R786"])
        raw837=out.parent/"inherited-R837"
        inherited_bundle(h837.directory/input837["file"],raw837,{"R786","R790"},inv837)
        entries786=entry_map(raw837/"R786",item["original_source_pins"]["R786"])
        assert sha(raw837/"R786"/MANIFEST)==sha(retained/"R786"/MANIFEST)
        for i in range(418):
            n=f"R786-exact-power-2-row-{i:04d}.json.gz"
            copy_bound(raw837/"R786"/n,retained/"R786"/n,entries786[n])
            selected["R786"].add(n)
        # Direct source selections are driven by the immutable actual indexes.
        selected["R800"]=set(META)|{MANIFEST,h800.source["certificate_name"]}
        selected["R800"].add(h800.certificate["basis_tail_index"]["file"])
        e1=[n for n in h800.entries if re.fullmatch(r"R800-original-E1-tail-row-\d{2}\.json\.gz",n)]
        assert len(e1)==82
        selected["R800"].update(e1)
        selected["R800"].update(f"R800-original-M2-tail-row-{i:04d}.json.gz" for i in (0,1,2,73))
        h800.select(selected["R800"],retained)
        vi=plain(item["selection_pins"]["V8_index"]);assert h799.entries[vi["file"]]==vi
        index=h799.get(vi["file"]);assert index["complete"] is True and index["configuration"]==h799.tag
        assert index["dimension"]==2050 and len(index["basis_rows"])==2050
        selected["R799"]=set(META)|{MANIFEST,h799.source["certificate_name"],vi["file"]}
        for row in index["basis_rows"]:
            assert h799.entries[row["file"]]==plain(row)
            selected["R799"].add(row["file"])
        h799.select(selected["R799"],retained)
        fi=plain(item["selection_pins"]["V8_frontier"]);plan=plain(item["selection_pins"]["recipe_plan"])
        assert h801.entries[fi["file"]]==fi and h801.entries[plan["file"]]==plan
        frontier=h801.get(fi["file"])
        assert frontier["complete"] is True and frontier["configuration"]==h801.tag
        assert len(frontier["basis_rows"])==2050 and frontier["new_first_exponent"]==109
        selected["R801"]=set(META)|{MANIFEST,h801.source["certificate_name"],fi["file"],plan["file"]}
        for i,(row,oldrow) in enumerate(zip(frontier["basis_rows"],index["basis_rows"])):
            assert row["index"]==oldrow["index"]==i
            prefixes=[v for v in row["original_prefix_segments"] if v["first"]==0 and v["stop"]==109]
            assert len(prefixes)==1 and prefixes[0]["producer"]=="R799" and plain(prefixes[0])==plain(oldrow)
            tails=[v for v in row["new_tail_segments"] if v["first"]<=109<v["stop"]]
            assert len(tails)==1 and tails[0]["producer"]=="R801"
            tail=plain(tails[0]);assert h801.entries[tail["file"]]==tail
            selected["R801"].add(tail["file"])
        h801.select(selected["R801"],retained)
        selected["R807"]=set(META)|{MANIFEST,h807.source["certificate_name"],h807.certificate["stage_manifest"]["file"]}
        for key in ("theta","E6_clearing"):
            row=plain(item["selection_pins"][key])
            assert h807.entries[row["file"]]==row
            selected["R807"].add(row["file"])
        assert plain(h807.certificate["theta_stage"])==plain(item["selection_pins"]["theta"])
        assert plain(h807.certificate["cleared_coordinate_stages"]["692"])==plain(item["selection_pins"]["E6_clearing"])
        h807.select(selected["R807"],retained)
        sources={g:review_group(g,item["original_source_pins"][g],retained,selected[g]) for g in GROUPS}
        inputs={key:stage_spec(group,sources[group]["files"][name]) for key,(group,name) in {
            "V8_index":("R799",vi["file"]), "V8_frontier":("R801",fi["file"]),
            "recipe_plan":("R801",plan["file"]), "M2_recipe":("R775","R775-basis-M2.json.gz"),
            "determinant_cosets":("R775","R775-determinant-cosets.json.gz"),
            "label_group":("R771","R771-original-level82-Eisenstein-label-group.json.gz"),
            "theta":("R807",item["selection_pins"]["theta"]["file"]),
            "E6_clearing":("R807",item["selection_pins"]["E6_clearing"]["file"])}.items()}
        for label,h in handles.items():
            transport[label]=h.archive.receipt() if h.archive is not None else h.transport
        transport["R800_original_input_bundle"]=plain(input800)
        transport["R837_original_input_bundle"]=plain(input837)
        transport["R837_original_source_inventory"]=plain(item["R837_inventory"])
        inventory={"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
                   "all_selected_bytes_and_original_tags_preserved":True}
        save(out/INVENTORY,inventory)
        pack(retained,sources,out/BUNDLE)
        expanded=dict(item,retained_sources=sources,inputs=inputs)
        save(out/EXPANDED,expanded)
        receipt={"result":RESULT,"complete":True,"source_inventory":spec(out/INVENTORY),
                 "source_bundle":spec(out/BUNDLE),"selected_file_count":sum(len(s["files"]) for s in sources.values()),
                 "selected_counts":{g:len(s["files"]) for g,s in sources.items()},
                 "source_transport":transport,"no_old_mathematical_stage_recomputed":True}
        save(out/INPUT_RECEIPT,receipt)
        print("R873_INPUT_REVIEW="+json.dumps(receipt,sort_keys=True),flush=True)
        return retained,expanded,receipt
    finally:
        for h in handles.values():
            h.close()


def stable_math_request(item):
    return {k:item[k] for k in ("result","p","producer_inputs_pending","core","core_sha256",
                                "original_helper","original_helper_sha256","proofs",
                                "original_source_pins","selection_pins")}


def restore(item,out):
    previous=item.get("resume")
    if previous is None:
        return
    assert previous["result"]==RESULT and previous["core_sha256"]==item["core_sha256"]
    folder=out.parent/"previous-R873";folder.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(previous,out.parent/"previous-R873-archive",whole=False)
    try:
        archive.extract_bound(MANIFEST,previous["manifest_sha256"],folder/MANIFEST,previous.get("manifest_bytes"))
        entries={r["file"]:plain(r) for r in read(folder/MANIFEST)["files"]}
        for name in ("public-actions-input.json","run-receipt.json"):
            archive.extract_bound(name,entries[name]["sha256"],folder/name,entries[name]["bytes"])
        initial=read(folder/"public-actions-input.json")
        run=read(folder/"run-receipt.json")
        assert initial["source_commit"]==run["source_commit"]==previous["source_commit"]
        assert str(run["workflow_run_id"])==str(previous["run_id"])
        assert stable_math_request(initial["job"])==stable_math_request(item)
        names=[n for n in (BUNDLE,INVENTORY,INPUT_RECEIPT,EXPANDED) if n in entries]
        if len(names)<4:
            assert not any(n.startswith("R873-") and n.endswith(".json.gz") for n in entries)
            save(out/"resume-receipt.json",{"result":RESULT,"resumed":True,
                 "source":previous,"completed_source_carrier_present":False,"mathematical_stages_restored":0})
            return
        archive.extract_many([(n,entries[n]["sha256"],folder/n,entries[n]["bytes"]) for n in names])
        expanded=read(folder/EXPANDED);tag=expected_tag(expanded)
        assert expanded["core_sha256"]==item["core_sha256"]
        stage_names=sorted(n for n in entries if n.startswith("R873-") and n.endswith(".json.gz"))
        archive.extract_many([(n,entries[n]["sha256"],folder/n,entries[n]["bytes"]) for n in stage_names])
        for name in stage_names:
            value=read(folder/name)
            assert value["complete"] is True and value["configuration"]==tag
            copy_bound(folder/name,out/name,entries[name])
        for name in names:
            copy_bound(folder/name,out/name,entries[name])
        copied_final=False
        if FINAL in entries:
            archive.extract_bound(FINAL,entries[FINAL]["sha256"],folder/FINAL,entries[FINAL]["bytes"])
            cert=read(folder/FINAL)
            assert cert["configuration"]==tag
            if cert["complete"] is True:
                inventory=read(bound(folder,cert["stage_manifest"]))
                for row in inventory["files"]:
                    assert entries[row["file"]]==plain(row)
                    bound(folder,row)
                copy_bound(folder/FINAL,out/FINAL,entries[FINAL])
                copied_final=True
        save(out/"resume-receipt.json",{
            "result":RESULT,"resumed":True,"source":previous,
            "mathematical_stages_restored":len(stage_names),"true_final_restored":copied_final,
            "all_completed_original_bytes_and_new_tag_verified":True,
            "no_old_mathematical_stage_recomputed":True,"range_receipt":archive.receipt()})
    finally:
        archive.close()


def output_manifest(out):
    rows=[spec(path) for path in sorted(Path(out).iterdir()) if path.is_file()
          and path.name not in (MANIFEST,REFERENCE)
          and not path.name.endswith((".tmp",".download",".partial"))]
    save(Path(out)/MANIFEST,{"result":RESULT,"files":rows,
         "temporary_active_checkpoint_retention_days":1,
         "reproducible_outputs_saved_in_repository_or_release":False})
    save(Path(out)/REFERENCE,{"result":RESULT,"manifest":spec(Path(out)/MANIFEST)})
    return spec(Path(out)/MANIFEST)


def compute(item,out,request):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    source=subprocess.check_output(["git","rev-parse","HEAD"],cwd=REPO,text=True).strip()
    started=dt.datetime.now(dt.timezone.utc).isoformat()
    initial={"result":RESULT,"source_repository":REPOSITORY,"source_commit":source,
             "core_sha256":item["core_sha256"],"wrapper_sha256":sha(__file__),
             "job":item,"request_sha256":sha(request),"started_utc":started,
             "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md")}
    save(out/"public-actions-input.json",initial)
    error,code,receipt,expanded=None,1,None,None
    try:
        restore(item,out)
        retained,expanded,receipt=prepare(item,out,True)
        initial["expanded_job"]=spec(out/EXPANDED)
        initial["mathematical_configuration_sha256"]=fingerprint(expected_tag(expanded))
        save(out/"public-actions-input.json",initial)
        command=[sys.executable,str(S/CORE),"--config",str(out/EXPANDED),
                 "--retained",str(retained),"--output",str(out),
                 "--budget-minutes",str(item["budget_minutes"])]
        with (out/"core.log").open("wb") as log:
            process=subprocess.Popen(command,cwd=REPO,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                code=process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid,signal.SIGTERM)
                try:
                    process.wait(timeout=40)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid,signal.SIGKILL);process.wait()
                code=124;error="OuterTimeout: completed stages retained without a fabricated core receipt."
    except BaseException as exc:
        error=type(exc).__name__+": "+str(exc)
        traceback.print_exc()
    core=read(out/"core-receipt.json") if (out/"core-receipt.json").exists() else None
    complete=code==0 and core is not None and core["complete"] is True
    if core is not None:
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
    run={"result":RESULT,"complete":complete,"process_exit_code":code,
         "workflow_run_id":os.environ["GITHUB_RUN_ID"],"workflow_run_attempt":os.environ["GITHUB_RUN_ATTEMPT"],
         "source_commit":source,"core_sha256":item["core_sha256"],"wrapper_sha256":sha(__file__),
         "started_utc":started,"finished_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
         "core_receipt_sha256":None if core is None else sha(out/"core-receipt.json"),
         "error":error if error is not None else (None if core is None else core.get("error")),
         "source_carrier_complete":receipt is not None,
         "completed_mathematical_stages_preserved":True,
         "temporary_active_checkpoint_retention_days":1,
         "reproducible_outputs_saved_in_repository_or_release":False}
    save(out/"run-receipt.json",run)
    manifest=output_manifest(out)
    print("R873_RUN_RECEIPT="+json.dumps(dict(run,full_manifest=manifest),sort_keys=True),flush=True)
    return 0 if complete else (124 if code==124 else 1)


def verify(item,out,request):
    out=Path(out);mp=out/MANIFEST
    manifest=read(mp)
    assert manifest["result"]==RESULT
    entries={row["file"]:plain(row) for row in manifest["files"]}
    assert len(entries)==len(manifest["files"])
    for row in entries.values():
        bound(out,row)
    reference=read(out/REFERENCE)
    assert reference["result"]==RESULT and plain(reference["manifest"])==spec(mp)
    initial=read(out/"public-actions-input.json");run=read(out/"run-receipt.json")
    assert initial["result"]==run["result"]==RESULT
    assert initial["source_commit"]==run["source_commit"]
    assert initial["core_sha256"]==run["core_sha256"]==item["core_sha256"]
    assert initial["wrapper_sha256"]==run["wrapper_sha256"]==item["wrapper_sha256"]
    assert stable_math_request(initial["job"])==stable_math_request(item)
    if not all((out/n).exists() for n in (BUNDLE,INVENTORY,INPUT_RECEIPT,EXPANDED)):
        assert run["complete"] is False
        print("R873_PARTIAL_IO_REVIEW="+json.dumps({"complete":False,"manifest":spec(mp),
              "source_carrier_complete":False,"error":run.get("error")}),flush=True)
        return 2
    retained,expanded,receipt=prepare(item,out,False)
    # prepare performs no mutation to mathematics and only normalizes this run's transport config.
    assert spec(out/EXPANDED)==entries[EXPANDED]
    tag=expected_tag(expanded)
    assert initial["expanded_job"]==entries[EXPANDED]
    for name,row in entries.items():
        if name.startswith("R873-") and name.endswith(".json.gz"):
            data=read(out/name)
            assert data["complete"] is True and data["configuration"]==tag
    core=None
    if "core-receipt.json" in entries:
        core=read(out/"core-receipt.json")
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
        if core.get("configuration") is not None:
            assert core["configuration"]==tag
    else:
        assert run["core_receipt_sha256"] is None and run["complete"] is False
    if not run["complete"]:
        assert core is None or core["complete"] is False
        print("R873_PARTIAL_IO_REVIEW="+json.dumps({
            "complete":False,"process_exit_code":run["process_exit_code"],"error":run.get("error"),
            "full_manifest":spec(mp),"selected_source_count":receipt["selected_file_count"],
            "completed_stages":sum(n.startswith("R873-") and n.endswith(".json.gz") for n in entries),
            "new_mathematics_executed_by_verifier":False}),flush=True)
        return 2
    assert run["process_exit_code"]==0 and core is not None and core["complete"] is True
    cert=read(out/FINAL)
    assert cert["result"]==RESULT and cert["complete"] is True and cert["configuration"]==tag
    assert core["certificate_sha256"]==entries[FINAL]["sha256"]
    expected={"exact_section_space_dimension":2058,"old_V8_dimension_reused":2050,
              "actual_new_basis_columns":8,"qY_count":110,"full_coordinate_rows":2200,
              "actual_exact_norm_coefficients":17,"P_degree":8,"K_degree_bound":7}
    for k,v in expected.items():
        assert cert[k]==v
    for k in ("all17_exact_characteristic_zero_unit_solve_expressions_certified",
              "all2200_original_modular_coordinate_relations_verified",
              "actual_original_cyclic7_correspondence_source_target_expression_certified"):
        assert cert[k] is True
    for k in ("actual_new_E1_or_M2_prefixes_through195_recomputed",
              "old_V8_V2_W_Hecke_or_E6_clearing_recomputed","ordinary_V8_membership_assumed",
              "expanded_characteristic_zero_coefficients_computed","normalized_curve_integral_basis_computed",
              "actual_ideal_norm_or_Picard_support_computed","actual_calibration_or_nonp_terms_computed",
              "actual_height_or_period_computed"):
        assert cert[k] is False
    assert cert["new_M2_indices"]==[0,1,2,73] and cert["new_M2_interval"]==[196,764]
    def stage(row):
        assert entries[row["file"]]==plain(row)
        value=read(bound(out,row))
        assert value["complete"] is True and value["configuration"]==tag
        return value
    inventory=stage(cert["stage_manifest"])
    for row in inventory["files"]:
        assert entries[row["file"]]==plain(row)
        stage(row)
    assert inventory["current_checkpoints"]==[]
    audit=stage(cert["source_audit"])
    assert audit["inputs"]==expanded["inputs"]
    assert audit["old_source_tags_and_bytes_preserved"] is True
    primitive=stage(cert["primitive_target_witness"])
    assert primitive["target_primitive_degree"]==8
    assert primitive["tau_constant_nonzero_and_sigma_q1_nonzero"] is True
    basis=stage(cert["section_basis"])
    assert basis["independent_columns"]==basis["actual_nonzero_minor_rank"]==2058
    assert basis["actual_2058_minor_determinant"]!=0
    assert basis["prime"]==cert["actual_auxiliary_prime"]
    chosen=[r["original_V2_index"] for r in basis["selected_complement"]]
    assert chosen==cert["actual_new_complement_V2_indices"] and len(set(chosen))==8
    for row in basis["selected_complement"]:
        candidate=stage(row["candidate"])
        assert candidate["original_V2_index"]==row["original_V2_index"]
    targets=stage(cert["norm_target_index"])
    assert targets["actual_target_count"]==17 and len(targets["targets"])==17
    assert len(targets["P_coefficients"])==9 and len(targets["K_coefficients"])==8
    for row in targets["targets"]:
        target=stage(row)
        assert target["integer_scale"]==str(82**16) and target["qY_count"]==110
        assert len(target["integer_qY_xi_coefficients"])==len(target["integer_v_t_coefficients"])==110
        assert all(len(v)==40 for v in target["integer_qY_xi_coefficients"])
        assert all(len(v)==20 for v in target["integer_v_t_coefficients"])
    coordinates=stage(cert["exact_coordinate_expression"])
    assert coordinates["basis_minor"]==cert["section_basis"]
    assert coordinates["target_index"]==cert["norm_target_index"]
    assert coordinates["all2200_coordinates_for_all17_targets_verified_mod_prime"] is True
    assert coordinates["exact_expanded_char0_coordinate_acceptance_claimed"] is False
    assert len(coordinates["modular_coordinates"])==2058
    assert all(len(v)==17 for v in coordinates["modular_coordinates"])
    for row in coordinates["coordinate_verification_stages"]:
        assert stage(row)["all_rows_mod_prime_verified"] is True
    program=stage(cert["correspondence_DAG"])
    assert program["coefficient_unit_solve"]==cert["exact_coordinate_expression"]
    assert program["exact_original_correspondence_expression_certified"] is True
    assert program["correspondence_function_field"]["degree_over_source"]==8
    assert program["rigidified_Hecke_transport"]["frozen_direction"]=="Nm_pi_t(pi_s^*I)"
    assert program["original_cY"]["z_claimed_Q_fixed"] is False
    print("R873_COMPLETE_IO_REVIEW="+json.dumps({
        "complete":True,"full_manifest":spec(mp),"certificate":entries[FINAL],
        "stage_manifest":cert["stage_manifest"],"source_inventory":receipt["source_inventory"],
        "source_bundle":receipt["source_bundle"],"selected_source_count":receipt["selected_file_count"],
        "actual_prime":cert["actual_auxiliary_prime"],"actual_complement_V2_indices":chosen,
        "actual_minor":cert["actual_nonzero_2058_minor"],"exact_norm_coefficients":17,
        "accurate_unexpanded_correspondence_expression":cert["correspondence_DAG"],
        "expanded_char0_coordinates":False,"active_eta_support_computed":False,
        "seconds":cert["seconds"],"new_mathematics_executed_by_verifier":False},sort_keys=True),flush=True)
    return 0


def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action",choices=("compute","verify"))
    parser.add_argument("--request",type=Path,default=REQUEST)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    raw=read(args.request);item=raw.get("job",raw)
    guard(item,args.request)
    if args.action=="compute":
        return compute(item,args.output,args.request)
    return verify(item,args.output,args.request)


if __name__=="__main__":
    sys.exit(main())
