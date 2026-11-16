#!/usr/bin/env python3
"""R885 stdlib complete-Artin provenance, source closure, resume and public driver."""
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
RESULT="R885-original-whole-Artin-reference-norms"
FINAL="p41-original-whole-Artin-reference-norms-certificate.json"
PREFIX="R885-Artin-"
CORE="R885_original_whole_Artin_norms.py"
HELPER="R885_whole_Artin_algebra.py"
REQUEST=TOPIC/"notes/R885-whole-Artin-reference-norms-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R885-Artin-retained-original-inputs.tar.gz"
INVENTORY="R885-Artin-original-source-inventory.json"
INPUT_RECEIPT="R885-Artin-retained-inputs-receipt.json"
EXPANDED="R885-Artin-expanded-job.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
GROUPS=("POLY","R827","R882","R873","R879","R807")
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
P=1000000753
EPS=[0]+[1]*144+[2]*127
IO=None

STRATEGY={
    "original_curve":"original genus127 Y, p41, original level82 and minus3 descent",
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "source_algebra":"Fp[X]/chi(a,X), entire272-dimensional Artin fibre",
    "source_nodes":"completed original eight cyclic nodes, in their actual saved order",
    "correspondence_algebra":"A[U]/(P(U)/a8), free rank8 over entire A",
    "target_w":"K(U)/Pprime(U)","normal_basis_rank":272,"normal_basis_degrees":EPS,
    "normal_column_block_size":16,"T_Horner_checkpoint_levels":16,
    "target_adjugate":"completed polynomial r(U,V), one complete original left row",
    "target_normalization":"gamma_j=r_j/r_0, only if r_0 is a unit on entire E",
    "target_verification":"all272 components gamma*(V*I-W(U))=0 and gamma0=1",
    "base_unit":"unreduced polynomial Bezout identity and full A product",
    "extension_unit":"division-free8 Berkowitz norm and complete E product",
    "reference_function":"original R879 f/u in its unchanged normal basis",
    "nine_norms":"one8 characteristic polynomial, det(I+t*M_x) for t0..8",
    "original_frame":"R879 t^-254 and lc(t/x)^254/U272 retained, never replaced by1",
    "norm_orientation":"Nm_source(target^*section), transported to frozen Nm_target(source^*I) by original dual7 involution",
    "factors_removed_or_semisimplicity_assumed":False,
    "old_polynomial_adjugate_Krylov_or17_coordinates_recomputed":False,
    "old_reference_system_theta_or_E6_clearing_recomputed":False,
    "finite_fibre_values_used_as_global_Picard_or_height_certificate":False,
    "budget_and_requested_fibre_count_excluded_from_identity":True}

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

def expected_tag(item,sources,inputs):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"helper_sha256":item["helper_sha256"],
            "python_flint":"0.9.0","p":41,"method_sha256":item["method_sha256"],"proofs":item["proofs"],
            "sources":{g:identity(sources[g]) for g in GROUPS},"inputs":inputs,"strategy":STRATEGY}

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
    d=importlib.util.spec_from_file_location("R885_Artin_frozen_stdlib_Range",path)
    IO=importlib.util.module_from_spec(d);d.loader.exec_module(IO)

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve() and item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False
    assert item["core"]==CORE and sha(S/CORE)==item["core_sha256"]
    assert item["helper"]==HELPER and sha(S/HELPER)==item["helper_sha256"]
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["io_helper"]==RANGE_FILE and item["io_helper_sha256"]==RANGE_SHA
    assert 0<item["budget_minutes"]<=300
    assert 1<=item["required_successful_fibres"]<=item["maximum_source_nodes"]<=8
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert set(item["source_artifacts"])=={"POLY","R882","R873","R879","R807"}
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
    if run.get("core_receipt_sha256") is not None:
        assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
    if group=="R827":
        assert run["complete"] is False and core["complete"] is False and run["process_exit_code"]==124
        certificate=None
        anchor=read(bound(folder,source["configuration_stage"]))
        assert anchor["complete"] is True
        tag=anchor["configuration"]
    else:
        assert run["complete"] is True and core["complete"] is True and run["process_exit_code"]==0
        certspec=plain(source["certificate"])
        assert entries[certspec["file"]]==certspec
        certificate=read(bound(folder,certspec))
        assert certificate["result"]==source["result"] and certificate["complete"] is True
        assert core["certificate_sha256"]==certspec["sha256"]
        tag=certificate["configuration"]
    assert tag.get("source_sha256",tag.get("core_sha256"))==source["core_sha256"]
    if source.get("configuration_sha256") is not None:
        assert fingerprint(tag)==source["configuration_sha256"]
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

def original_pins(item,sources):
    assert set(sources)==set(GROUPS)
    for group,prior in item["source_artifacts"].items():
        for key in BASE:
            if key=="manifest_sha256" and prior.get(key) is None:
                assert prior["read_complete_manifest_from_original_reference"] is True
            else:
                assert str(prior[key])==str(sources[group][key])
        for key in ("file","sha256"):
            assert prior["certificate"][key]==sources[group]["certificate"][key]
        if prior["certificate"].get("bytes") is not None:
            assert prior["certificate"]["bytes"]==sources[group]["certificate"]["bytes"]
        if prior.get("configuration_sha256") is not None:
            assert prior["configuration_sha256"]==sources[group]["configuration_sha256"]
    assert sources["R827"]["result"]=="R827-original-global-modular-derivative-termination"
    assert sources["R827"]["core_sha256"]=="d9cf773976f3beff7f44ff30f8b593665f481470cb52297239710e0ce6e062d2"

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

def source_review(item,retained,sources,inputs):
    original_pins(item,sources)
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
    poly=certs["POLY"]
    assert poly["actual_original_complete_polynomial_adjugate_row_certified"] is True
    assert poly["actual_completed_node_count"]==poly["actual_completed_row_level_count"]==273
    assert plain(poly["characteristic_relation"])==plain(inputs["characteristic_relation"])
    assert plain(poly["one_row_adjugate"])==plain(inputs["adjugate_row_index"])
    characteristic=stage(inputs["characteristic_relation"]);adj=stage(inputs["adjugate_row_index"])
    assert len(inputs["row_levels"])==len(adj["adjugate_row_T_terms"])==272
    for k,(row,term) in enumerate(zip(inputs["row_levels"],adj["adjugate_row_T_terms"])):
        assert plain(row)==plain(term["source"]) and term["T_power"]==271-k and term["b_level"]==k
        value=stage(row)
        assert value["row_level"]==k and value["shape"]==[k+3,272]
        assert value["full_weighted_support_verified"] is True
        assert plain(value["source_characteristic_relation"])==plain(inputs["characteristic_relation"])
    assert characteristic["all273_nodes_for_all273_T_coefficients_verified"] is True
    assert adj["all272_polynomial_components_of_terminal_row_zero"] is True
    terminal=read(bound(Path(retained)/"POLY",adj["terminal_Cayley_Hamilton_row"]))
    assert terminal["complete"] is True and terminal["configuration"]==tags["POLY"]
    assert terminal["terminal_complete_polynomial_row_zero"] is True
    W=stage(inputs["original_W"]);grid=stage(inputs["original_grid"]);place=stage(inputs["original_place"])
    assert W["prime"]==grid["prime"]==place["prime"]==P and place["original_zeta_root"]==549966761
    assert len(grid["points"])==len(set(grid["points"]))==8
    assert grid["all_eight_actual_determinants_nonzero"] is True
    for j in range(8):
        assert plain(inputs["original_Krylov_points"][j])==plain(grid["Krylov_point_stages"][j])
        assert plain(inputs["original_characteristic_nodes"][j])==plain(characteristic["source_node_stages"][j])
        old=stage(inputs["original_Krylov_points"][j])
        node=stage(inputs["original_characteristic_nodes"][j])
        assert old["z0"]==node["z_value"]==grid["points"][j] and old["prime"]==P
        assert old["usable"] is True and old["both_inverse_products_verified"] is True
        assert old["actual_cyclic_rank"]==272
        assert plain(node["source_original_Krylov"])==plain(inputs["original_Krylov_points"][j])
    C=stage(inputs["seventeen_coordinates"]);common=stage(inputs["same_place_interface"])
    assert C["prime"]==common["prime"]==P and common["all2200_by17_original_equations_verified"] is True
    assert common["original_zeta_root"]==549966761
    assert len(C["coordinate_matrix_mod_prime"])==2058 and all(len(row)==17 for row in C["coordinate_matrix_mod_prime"])
    assert plain(common["new_modular_coordinates"])==plain(inputs["seventeen_coordinates"])
    DAG=stage(inputs["correspondence_DAG"])
    assert plain(common["source_R873_correspondence_DAG"])==plain(inputs["correspondence_DAG"])
    assert plain(C["source_exact_R873_unit_solve"])==plain(DAG["coefficient_unit_solve"])
    assert len(DAG["old_V8_over_tau8"])==2050 and len(DAG["new_eight_complement_functions"])==8
    assert DAG["rigidified_Hecke_transport"]["frozen_direction"]=="Nm_pi_t(pi_s^*I)"
    theta=stage(inputs["theta"]);clearing=stage(inputs["E6_clearing"])
    assert plain(DAG["E6hat_over_tau3"]["theta_source"])==plain(inputs["theta"])
    assert plain(DAG["E6hat_over_tau3"]["V4_coordinate_source"])==plain(inputs["E6_clearing"])
    assert theta["theta_nonzero_by_original_independent_M2_input"] is True
    assert clearing["M6_index"]==692 and clearing["all1100_rows_verified"] is True
    assert clearing["exact_global_V4_membership_certified"] is True
    reference=stage(inputs["reference_function"])
    assert reference["prime"]==P and reference["original_zeta_root"]==549966761
    assert reference["actual_reference_basepoint_free_pencil_certified"] is True
    for key in ("numerator_normal_polynomial_mod_prime","denominator_normal_polynomial_mod_prime"):
        assert len(reference[key])==3 and all(len(row)==272 for row in reference[key])
    same_source(tags["POLY"]["source_R827"],sources["R827"])
    same_source(tags["R882"]["sources"]["R873"],sources["R873"])
    same_source(tags["R873"]["sources"]["R807"],sources["R807"])
    return {"result":RESULT,"source_identities":{g:identity(sources[g]) for g in GROUPS},
            "selected_file_count":sum(len(x["files"]) for x in sources.values()),
            "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
            "actual_old_source_nodes":grid["points"],"all_selected_source_bytes_and_configurations_verified":True,
            "old_failed_R827_contributes_only_completed_original_stages":True,
            "new_mathematics_executed":False,"original_large_R873_or_R882_carrier_read":False}

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R885-Artin";retained.mkdir(parents=True,exist_ok=True)
    if all((out/n).exists() for n in (BUNDLE,INVENTORY,INPUT_RECEIPT)):
        inventory=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        assert receipt["source_inventory"]==spec(out/INVENTORY) and receipt["source_bundle"]==spec(out/BUNDLE)
        sources=inventory["sources"];inputs=inventory["inputs"]
        original_pins(item,sources);unpack(out/BUNDLE,retained,sources)
        review=source_review(item,retained,sources,inputs)
        return retained,sources,inputs,review
    assert allow_download,"No complete retained R885 Artin input bundle is available."
    handles={}
    try:
        for group in ("POLY","R882","R873","R879","R807"):
            handles[group]=Handle(group,item,retained,out.parent/"R885-Artin-download")
        p=handles["POLY"];cert=p.certificate
        for key in ("source_audit","characteristic_relation","one_row_adjugate","stage_manifest"):
            p.stage(cert[key])
        characteristic=p.stage(cert["characteristic_relation"])
        adj=p.stage(cert["one_row_adjugate"])
        inputs={"characteristic_relation":group_ref("POLY",cert["characteristic_relation"]),
                "adjugate_row_index":group_ref("POLY",cert["one_row_adjugate"]),
                "row_levels":[group_ref("POLY",row["source"]) for row in adj["adjugate_row_T_terms"]],
                "original_characteristic_nodes":[group_ref("POLY",row) for row in characteristic["source_node_stages"][:8]]}
        p.take([row["file"] for row in inputs["row_levels"]]+
               [row["file"] for row in inputs["original_characteristic_nodes"]]+
               [adj["terminal_Cayley_Hamilton_row"]["file"]])
        old_inventory="R885-original-source-inventory.json"
        old_receipt="R885-retained-inputs-receipt.json"
        old_bundle="R885-retained-R827-inputs.tar.gz"
        p.take([old_inventory,old_receipt,old_bundle])
        inventory=read(p.folder/old_inventory);receipt=read(p.folder/old_receipt)
        assert receipt["source_inventory"]==p.entries[old_inventory]
        assert receipt["source_bundle"]==p.entries[old_bundle]
        old_source=inventory["source_R827"]
        original_inputs=inventory["inputs"]
        extract_bound_group(p.folder/old_bundle,retained,"R827",old_source)
        # The verified original bundle is expanded once; do not embed a duplicate copy.
        p.selected.pop(old_bundle)
        inputs["original_W"]=group_ref("R827",original_inputs["W_reduction"])
        inputs["original_grid"]=group_ref("R827",original_inputs["cyclic_grid"])
        inputs["original_place"]=group_ref("R827",original_inputs["place_audit"])
        inputs["original_Krylov_points"]=[group_ref("R827",row) for row in original_inputs["Krylov_points"]]
        r=handles["R882"]
        for key in ("source_audit","seventeen_coordinates","same_place_correspondence_coefficients"):
            r.stage(r.certificate[key])
        inputs["seventeen_coordinates"]=group_ref("R882",r.certificate["seventeen_coordinates"])
        inputs["same_place_interface"]=group_ref("R882",r.certificate["same_place_correspondence_coefficients"])
        s=handles["R873"];DAG=s.stage(s.certificate["correspondence_DAG"])
        inputs["correspondence_DAG"]=group_ref("R873",s.certificate["correspondence_DAG"])
        s.stage(s.certificate["source_audit"])
        v=handles["R879"];reference=v.stage(v.certificate["reference_function_and_pencil"])
        v.stage(v.certificate["unit_solution"]);v.stage(v.certificate["source_audit"])
        inputs["reference_function"]=group_ref("R879",v.certificate["reference_function_and_pencil"])
        reference_bundle="R879-retained-R872-inputs.tar.gz"
        reference_inventory="R879-original-source-inventory.json"
        reference_receipt="R879-retained-inputs-receipt.json"
        v.take([reference_bundle,reference_inventory,reference_receipt])
        rr=read(v.folder/reference_receipt)
        assert rr["source_bundle"]==v.entries[reference_bundle]
        assert rr["source_inventory"]==v.entries[reference_inventory]
        # This small opaque reference carrier preserves the actual characteristic-zero v0 leaves.
        t=handles["R807"]
        inputs["theta"]=group_ref("R807",DAG["E6hat_over_tau3"]["theta_source"])
        inputs["E6_clearing"]=group_ref("R807",DAG["E6hat_over_tau3"]["V4_coordinate_source"])
        t.stage(inputs["theta"]);t.stage(inputs["E6_clearing"])
        for key,row in item.get("input_pins",{}).items():
            assert plain(inputs[key])==plain(row)
        sources={g:handles[g].finish_source() for g in handles}
        sources["R827"]=old_source
        original_pins(item,sources)
        review=source_review(item,retained,sources,inputs)
        transports={g:h.receipt() for g,h in handles.items()}
        transports["POLY"]["completed_original_R827_bundle_expanded"]=p.entries[old_bundle]
        transports["R879"]["opaque_original_reference_carrier_retained"]=v.entries[reference_bundle]
        save(out/INVENTORY,{"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
                           "transports":transports,"old_large_R873_R882_carriers_not_read":True,
                           "new_mathematics_executed":False})
        pack(retained,sources,out/BUNDLE)
        save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,"source_inventory":spec(out/INVENTORY),
                               "source_bundle":spec(out/BUNDLE),
                               "source_identities":{g:identity(sources[g]) for g in GROUPS},
                               "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
                               "new_mathematics_executed":False})
        print("R885_ARTIN_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,sources,inputs,review
    finally:
        for handle in handles.values():
            handle.close()

def restore(item,out):
    resume=item.get("resume")
    if not resume:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R885-Artin-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R885-Artin-resume-archive",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],directory/MANIFEST,resume.get("manifest_bytes"))
        entries=entry_map(directory,resume)
        names=(set(META)&set(entries))|{BUNDLE,INVENTORY,INPUT_RECEIPT}
        archive.extract_many([(n,entries[n]["sha256"],directory/n,entries[n]["bytes"]) for n in sorted(names)])
        initial=read(directory/"public-actions-input.json");run=read(directory/"run-receipt.json")
        assert initial["result"]==run["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]==resume["source_commit"]
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        for key in ("core_sha256","wrapper_sha256","helper_sha256"):
            assert initial[key]==item[key]
        for key in ("proofs","method_sha256"):
            assert initial["job"][key]==item[key]
        core=None
        if run.get("core_receipt_sha256") is not None:
            assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
            core=read(directory/"core-receipt.json")
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
            assert core["helper_sha256"]==item["helper_sha256"]
        else:
            assert run["complete"] is False
        inventory=read(directory/INVENTORY);receipt=read(directory/INPUT_RECEIPT)
        assert plain(receipt["source_inventory"])==entries[INVENTORY]
        assert plain(receipt["source_bundle"])==entries[BUNDLE]
        sources,inputs=inventory["sources"],inventory["inputs"]
        original_pins(item,sources)
        for key,row in item.get("input_pins",{}).items():
            assert plain(inputs[key])==plain(row)
        tag=expected_tag(item,sources,inputs)
        assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
        if core is not None and core.get("configuration") is not None:
            assert core["configuration"]==tag
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
            "helper_sha256":item["helper_sha256"],
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
            "helper_sha256":item["helper_sha256"],
            "complete":code==0,"process_exit_code":code,"error":error,"outer_timeout":outer_timeout,
            "execution_environment":"public-repository-github-actions",
            "core_receipt_sha256":sha(out/"core-receipt.json") if (out/"core-receipt.json").exists() else None,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    return code

def dimensions(value,m,n):
    assert len(value)==m and all(len(row)==n for row in value)

def verify(item,out,request):
    out=Path(out)
    manifest=read(out/MANIFEST);assert manifest["result"]==RESULT
    entries={r["file"]:plain(r) for r in manifest["files"]}
    assert len(entries)==len(manifest["files"])
    for row in entries.values():
        bound(out,row)
    actual={p.name for p in out.iterdir() if p.is_file() and not p.name.endswith((".tmp",".download",".partial"))}
    assert actual==set(entries)|{MANIFEST,REFERENCE}
    assert plain(read(out/REFERENCE))==spec(out/MANIFEST)
    retained,sources,inputs,review=prepare(item,out,allow_download=False)
    tag=expected_tag(item,sources,inputs)
    initial=read(out/"public-actions-input.json");run=read(out/"run-receipt.json")
    assert initial["result"]==run["result"]==RESULT
    assert initial["source_commit"]==run["source_commit"]==os.environ["GITHUB_SHA"]
    assert str(run["workflow_run_id"])==os.environ["GITHUB_RUN_ID"]
    for key in ("core_sha256","wrapper_sha256","helper_sha256"):
        assert initial[key]==run[key]==item[key]
    assert initial["request_sha256"]==sha(request)
    assert initial["expanded_job"]==entries[EXPANDED]
    assert initial["source_inventory"]==entries[INVENTORY]
    assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
    expanded=read(out/EXPANDED)
    assert expected_tag(expanded,expanded["sources"],expanded["inputs"])==tag
    core=None
    if run["core_receipt_sha256"] is not None:
        assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
        core=read(out/"core-receipt.json")
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        assert core["helper_sha256"]==item["helper_sha256"]
        if core["configuration"] is not None:
            assert core["configuration"]==tag
    else:
        assert run["complete"] is False
    complete_stages=[]
    for name,row in entries.items():
        if not name.startswith(PREFIX) or not name.endswith(".json.gz"):
            continue
        value=read(out/name)
        assert value["result"]==RESULT and value["configuration"]==tag
        if name==PREFIX+"current.json.gz":
            assert value["complete"] is False
            for member in value["completed_stages"].values():
                assert plain(member)==entries[member["file"]]
            continue
        assert value["complete"] is True
        if name.startswith(PREFIX+"stage-manifest-"):
            for member in value["files"]:
                assert plain(member)==entries[member["file"]]
            continue
        complete_stages.append(row)
    def stage(row):
        row=plain(row);assert entries[row["file"]]==row
        value=read(bound(out,row))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        return value
    def Avalue(raw):
        assert len(raw)==272 and all(isinstance(x,int) and 0<=x<P for x in raw)
    def Evalue(raw):
        assert len(raw)==8
        for v in raw:
            Avalue(v)
    def base_unit(value):
        assert value["whole_fibre_unit"] is True
        assert value["full_unreduced_polynomial_Bezout_identity_verified"] is True
        assert value["complete_original_algebra_product_equals_one"] is True
        assert value["factors_removed_or_squarefree_replacement_used"] is False
        Avalue(value["inverse"])
    def extension_characteristic(value):
        assert value["prime"]==P and value["base_dimension"]==272 and value["extension_rank"]==8
        assert value["division_free_Berkowitz_used"] is True
        assert value["all8_Cayley_Hamilton_coordinates_verified"] is True
        assert value["norm_is_last_coefficient_because_rank8_even"] is True
        assert value["squarefree_factorization_or_geometric_point_selection_used"] is False
        assert len(value["characteristic_coefficients_over_A"])==9
        for row in value["characteristic_coefficients_over_A"]:
            Avalue(row)
        dimensions(value["multiplication_matrix_over_entire_A"],8,8)
        for row in value["multiplication_matrix_over_entire_A"]:
            for entry in row:
                Avalue(entry)
    def extension_unit(value):
        extension_characteristic(value)
        assert value["whole_fibre_unit"] is True and value["complete2176_scalar_product_equals_one"] is True
        base_unit(value["base_norm_unit_witness"]);Evalue(value["inverse"])
    cert=read(out/FINAL) if FINAL in entries else None
    successors=[]
    if cert is not None:
        assert cert["result"]==RESULT and cert["configuration"]==tag and cert["p"]==41
        assert cert["actual_auxiliary_prime"]==P
        assert cert["complete_factors_and_nilpotent_multiplicities_retained"] is True
        for key in ("characteristic_zero_expanded_norm_coefficients_computed",
                    "old_W_Krylov_polynomial_adjugate_17coordinates_or_reference_solve_recomputed",
                    "original_Hecke_active_support_principal_calibration_nonp_terms_or_height_computed"):
            assert cert[key] is False
        assert cert["actual_source_dimension_for_every_accepted_fibre"]==272
        assert cert["actual_correspondence_scalar_dimension_for_every_accepted_fibre"]==2176
        grid=read(bound(retained/"R827",inputs["original_grid"]))
        assert cert["source_node_schedule"]==grid["points"]
        outcomes=cert["fibre_outcomes"]
        assert cert["actual_tested_fibres"]==len(outcomes)
        good=[x for x in outcomes if x["success"]]
        failed=[x for x in outcomes if not x["success"]]
        assert cert["actual_successful_fibres"]==len(good) and cert["actual_failed_unit_fibres"]==len(failed)
        assert cert["successful_fibre_certificates"]==good
        assert cert["actual_nine_reference_norm_values_computed"]==bool(good)
        assert cert["all_required_units_certified_on_entire_accepted_fibres"]==bool(good)
        assert cert["actual_whole_Artin_target_normal_coordinates_certified"]==bool(
            cert["complete_original_target_normal_coordinate_certificates"])
        if cert["complete"] is True:
            assert len(good)>=cert["requested_successful_fibres"]
            assert cert["requested_successful_fibres"]==item["required_successful_fibres"]
            assert plain(cert["stage_manifest"])==entries[cert["stage_manifest"]["file"]]
            inventory=stage(cert["stage_manifest"])
            assert inventory["files"]==sorted(complete_stages,key=lambda r:r["file"])
            assert plain(cert["resume_state"])==entries[cert["resume_state"]["file"]]
            assert inventory["current_checkpoints"]==[plain(cert["resume_state"])]
        # An incomplete endpoint may predate the current atomic pointer after a hard stop.
        if cert.get("source_audit") is not None:
            audit=stage(cert["source_audit"])
            assert audit["sources"]=={g:identity(sources[g]) for g in GROUPS}
            assert audit["inputs"]==inputs and audit["whole_Artin_fibre_required"] is True
        if cert.get("exact_global_reference_norm_expression_program") is not None:
            program=stage(cert["exact_global_reference_norm_expression_program"])
            assert program["source_original_correspondence_DAG"]==inputs["correspondence_DAG"]
            assert program["source_original_reference_function"]==inputs["reference_function"]
            assert program["exact_global_expressions_defined_by_existing_sources_and_R876"] is True
            assert program["characteristic_zero_norm_coefficients_expanded"] is False
            assert program["finite_modular_target_coordinates_not_substituted_for_characteristic_zero_functions"] is True
            assert program["original_t_frame_scalar_not_replaced_by_one"] is True
        for expected_ordinal,row in enumerate(outcomes):
            assert row["ordinal"]==expected_ordinal and row["z0"]==grid["points"][expected_ordinal]
            value=stage(row["certificate"])
            assert value["source_node_ordinal"]==row["ordinal"] and value["source_node_value"]==row["z0"]
            assert value["whole_fibre_success"] is row["success"] and value["prime"]==P
            if not row["success"]:
                assert value["unit_failure_label"]==row["unit_failure_label"]
                assert value["failing_factors_not_removed_and_no_partial_fibre_promoted"] is True
                assert value["original_characteristic_zero_formula_not_refuted"] is True
                assert value["complete_original_algebra_failure_witness"]
                continue
            assert value["source_dimension"]==272 and value["correspondence_scalar_dimension"]==2176
            for key in ("all_required_units_on_entire_algebras_verified",
                        "all272_original_target_normal_coordinates_certified",
                        "all_nine_reference_norms_on_entire_source_fibre_computed"):
                assert value[key] is True
            for key in ("factors_multiplicities_or_ramification_components_discarded",
                        "old_producer_arithmetic_recomputed","global_Picard_support_nonp_terms_or_height_computed"):
                assert value[key] is False
            functions=stage(value["source_functions"])
            assert functions["source_node_value"]==row["z0"] and functions["source_algebra_dimension"]==272
            assert functions["source_characteristic_node"]==inputs["original_characteristic_nodes"][row["ordinal"]]
            assert functions["source_original_Krylov"]==inputs["original_Krylov_points"][row["ordinal"]]
            dimensions(functions["original_M2_functions_over_A"],146,272)
            dimensions(functions["original2058_basis_function_values_over_A"],2058,272)
            dimensions(functions["seventeen_values_over_A"],17,272)
            assert functions["new_scale_applied"]=="1" and functions["original82_scales_retained_once"] is True
            base_unit(functions["theta_unit_certificate"])
            correspondence=stage(value["correspondence_algebra"])
            assert correspondence["source_functions"]==plain(value["source_functions"])
            assert correspondence["full_scalar_dimension"]==2176 and correspondence["correspondence_rank"]==8
            base_unit(correspondence["leading_coefficient_unit_certificate"])
            extension_unit(correspondence["Pprime_unit_certificate"])
            assert correspondence["full_Pprime_times_target_w_equals_K_verified"] is True
            assert correspondence["any_source_factor_or_multiplicity_discarded"] is False
            relation=stage(value["target_characteristic_relation"])
            assert relation["full_chi_U_V_equals_zero"] is True and relation["full_scalar_dimension"]==2176
            assert relation["source_characteristic_relation"]==inputs["characteristic_relation"]
            cofactors=stage(value["evaluated_cofactor_row"])
            assert cofactors["all272_original_left_cofactors_evaluated"] is True
            r0=stage(value["r0_unit"]);extension_unit(r0["unit_certificate"])
            assert r0["original_principal271_minor_unit_on_complete_E"] is True
            normal=stage(value["target_normal_row"])
            assert normal["all272_target_normal_coordinates_computed"] is True and normal["target_gamma0_equals_one"] is True
            assert len(normal["blocks"])==17
            for k,block in enumerate(normal["blocks"]):
                first=16*k;stop=min(272,first+16)
                assert block["normal_columns"]==[first,stop]
                actual_block=stage(block["source"])
                assert actual_block["normal_columns"]==[first,stop]
                assert actual_block["source_r0_unit"]==plain(value["r0_unit"])
                assert len(actual_block["normal_values_over_E"])==stop-first
                for entry in actual_block["normal_values_over_E"]:
                    Evalue(entry)
            equations=stage(value["full_target_equations"])
            assert equations["all272_original_target_equations_verified"] is True
            assert equations["all2176_scalar_coordinates_of_each_equation_checked"] is True
            assert equations["no_factor_or_nilpotent_component_discarded"] is True
            assert equations["source_original_W"]==inputs["original_W"]
            for degree,member in enumerate(equations["source_four_coefficient_products"]):
                product=stage(member);assert product["W_power"]==degree
                dimensions(product["products_flat_mod_prime"],272,2176)
            reference=stage(value["original_reference_value"])
            assert reference["source_original_reference_function"]==inputs["reference_function"]
            extension_unit(reference["denominator_unit_certificate"])
            assert reference["full_original_target_reference_quotient_verified"] is True
            assert reference["original_t_frame_scalar_not_replaced_by_one"] is True
            norms=stage(value["nine_reference_norms"])
            assert norms["parameters"]==list(range(9))
            dimensions(norms["norm_polynomial_over_A"],9,272)
            dimensions(norms["nine_norm_values_over_entire_A"],9,272)
            extension_characteristic(norms["one_multiplication_characteristic_polynomial"])
            assert norms["parameter_zero_norm_equals_one"] is True
            assert norms["one_new_rank8_characteristic_polynomial_for_all_nine_values"] is True
            assert norms["nine_separate_determinants_computed"] is False
            assert norms["single_geometric_point_or_reduced_quotient_used"] is False
            assert norms["frozen_Hecke_direction_recovered_by_original_dual7"] is True
            assert norms["global_Picard_nonzero_or_principal_calibration_certified"] is False
            successors.append({"ordinal":row["ordinal"],"source_node_value":row["z0"],
                "certificate":plain(row["certificate"]),"target_normal_row_index":plain(value["target_normal_row"]),
                "full_target_equations":plain(value["full_target_equations"]),
                "nine_reference_norms":plain(value["nine_reference_norms"])})
        for row in cert["complete_original_target_normal_coordinate_certificates"]:
            equations=stage(row["certificate"])
            assert equations["all272_original_target_equations_verified"] is True
            assert row["z0"]==grid["points"][row["ordinal"]]
    if run["complete"] is True:
        assert run["process_exit_code"]==0 and run["error"] is None
        assert core is not None and core["complete"] is True and core["error"] is None
        assert core["process_exit_code"]==0 and core["configuration"]==tag
        assert cert is not None and cert["complete"] is True
        assert core["certificate_sha256"]==entries[FINAL]["sha256"]
    summary={"result":RESULT,"complete":bool(run["complete"] and cert and cert["complete"]),
             "actual_complete_stage_count":len(complete_stages),
             "all_output_bytes_and_original_source_identities_verified":True,
             "selected_source_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
             "source_complete_manifest":spec(out/MANIFEST),
             "certificate":entries.get(FINAL),"core_receipt":entries.get("core-receipt.json"),
             "configuration_sha256":fingerprint(tag),
             "source_inventory":entries[INVENTORY],"source_bundle":entries[BUNDLE],
             "stage_manifest":cert.get("stage_manifest") if cert else None,
             "resume_state":cert.get("resume_state") if cert else None,
             "actual_tested_fibres":cert.get("actual_tested_fibres") if cert else None,
             "actual_successful_fibres":cert.get("actual_successful_fibres") if cert else None,
             "actual_failed_unit_fibres":cert.get("actual_failed_unit_fibres") if cert else None,
             "actual_whole_Artin_target_normal_coordinates_certified":
                 bool(cert and cert["actual_whole_Artin_target_normal_coordinates_certified"]),
             "actual_nine_reference_norm_values_computed":
                 bool(cert and cert["actual_nine_reference_norm_values_computed"]),
             "successful_fibre_sources":successors,
             "completed_R885_polynomial_source":{
                 **{k:sources["POLY"][k] for k in BASE},
                 "configuration_sha256":sources["POLY"]["configuration_sha256"],
                 "certificate":sources["POLY"]["certificate"],
                 "manifest":sources["POLY"]["files"][MANIFEST],
                 "characteristic_relation":plain(inputs["characteristic_relation"]),
                 "one_row_adjugate":plain(inputs["adjugate_row_index"])},
             "new_mathematics_executed_in_verifier":False,
             "old_producer_arithmetic_recomputed":False,
             "original_Hecke_active_support_nonp_terms_or_height_computed":False}
    print("R885_ARTIN_COMPLETE_IO_REVIEW="+json.dumps(summary,sort_keys=True),flush=True)
    return 0 if summary["complete"] else 1

def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("command",choices=("compute","verify"))
    parser.add_argument("--request",default=str(REQUEST))
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    request=Path(args.request);item=read(request)
    if "job" in item:
        item=item["job"]
    guard(item,request)
    if args.command=="compute":
        raise SystemExit(compute(item,Path(args.output),request))
    raise SystemExit(verify(item,Path(args.output),request))

if __name__=="__main__":
    main()
