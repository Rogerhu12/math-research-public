#!/usr/bin/env python3
"""R899 source-preserving standard-library transport, resume, and structural verification."""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
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
RESULT="R899-original-K-fixed-seven-trace-RR-basis"
FINAL="p41-original-K-fixed-seven-trace-RR-basis-certificate.json"
PREFIX="R899-"
CORE="R899_original_K_fixed_seven_trace_RR_basis.py"
REQUEST=TOPIC/"notes/R899-K-fixed-seven-trace-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R899-retained-original-inputs.tar.gz"
INVENTORY="R899-original-source-inventory.json"
RECEIPT="R899-retained-inputs-receipt.json"
EXPANDED="R899-expanded-job.json"
TRACE_BUNDLE="R894-retained-original-inputs.tar.gz"
TRACE_INVENTORY="R894-original-source-inventory.json"
TRACE_RECEIPT="R894-retained-inputs-receipt.json"
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
GROUPS=("R894","R890","SIXD","R880","R887","R872","R883","R827","R885","R845")
OLD_GROUPS=("R887","R880","R872","R883","R827","R890","SIXD")
P=1000000753
N=272
DIM=418
V3DIM=690
EPS=[0]+[1]*144+[2]*127
ARTIN_SHA="e47cd50d254700b98446866297d79694c100f1435c46f3b4f42e3835763f897d"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
TRACE_CORE="9a2793c79e552c04ea384f5c6bfb673e6e7d506ff91cf9e246fbc00a76f2da56"
CHAIN=(("A1","D0","D1"),("A2","D2","D3"),("A3","A1","A2"),
       ("A4","A3","D4"),("A5","D5","D6"),("A6","A4","A5"),
       ("A7","A6","A6"),("A8","A7","H"),("A9","A8","A6"),
       ("B3","Cstar","H"),("B4","B3","X4"),("B5","B4","B4"),
       ("B6","B5","B5"),("B7","B6","B4"),("B8","B7","B5"),("DN","A9","B8"))
IO=None

STRATEGY={
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "original_integral_B_root":3197390,
    "normal_basis_degrees":EPS,"normal_V3_dimension":V3DIM,"fixed_RR_dimension":DIM,
    "constant_field_descent":"original Gal(L/K) of order7, K=Q(zeta3)",
    "space":"H0(2H-T_f^0), T_f^0=sum_sigma(E_f)-8442P0",
    "positive_identification":"Q_N * H0(3H-D_N)",
    "old_fibre_schedule":[0,1,2,3,4,5,6],"initial_usable_fibres":3,
    "no_automatic_three_fibre_injectivity_assumed":True,
    "acceptance":"actual 418-row unit minor of all computed K-coordinate evaluations",
    "every_required_division_in_complete272_Artin_algebra":True,
    "QN_itself_not_required_to_be_a_unit":True,
    "original_charpoly_Krylov_inverse_and_V3_evaluation_recomputed":False,
    "zero_branch_a_old_fibres":[0,1,2,3,4],
    "zero_branch_a_missing_node_rule":"only if needed: degree<=3-epsilon interpolation from old0..3, checked on old4",
    "normal_basis_change":"B_N times inverse(selected_QN_times_WN_evaluation)",
    "exact_old_descent_matrix":"A^-1 sigma(A), expression only",
    "exact_new_fixed_basis_action":"I418 by uniqueness of K-linear selected coordinates",
    "new_sigma_replay_or_old_flip_repetition":False,
    "source_flip_chain":[list(x) for x in CHAIN],
    "original_QN_rho_order":-8435,"original_t_leading_exponent":8435,
    "original_P0_values_and_all_scalars_preserved_without_rescaling":True,
    "characteristic_zero_arrays_expanded":False,
    "Q_fixed_basis_Hecke_norm_connection_or_height_computed":False,
    "only_budget_and_transport_excluded_from_mathematical_identity":True}


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for part in iter(lambda:f.read(4*1024*1024),b""):h.update(part)
    return h.hexdigest()
def read(path):
    p=Path(path)
    with (gzip.open if p.suffix==".gz" else open)(p,"rt",encoding="utf-8") as f:return json.load(f)
def save(path,value):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_name(p.name+".tmp")
    raw=(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode()
    if p.suffix==".gz":
        with tmp.open("wb") as f:
            with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0,compresslevel=2) as g:g.write(raw)
    else:tmp.write_bytes(raw)
    tmp.replace(p)
def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def plain(value):
    r={k:value[k] for k in ("file","bytes","sha256")}
    p=PurePosixPath(r["file"])
    assert len(p.parts)==1 and p.name not in ("",".","..") and "\\" not in p.name
    assert isinstance(r["bytes"],int) and r["bytes"]>=0
    assert len(r["sha256"])==64 and all(c in "0123456789abcdef" for c in r["sha256"])
    return r
def spec(path):
    p=Path(path);return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p)}
def bound(folder,row):
    row=plain(row);p=Path(folder)/row["file"]
    assert spec(p)==row,str(p)
    return p
def group_ref(g,row):
    return {"source_group":g,**plain(row)}
def identity(source):
    d={k:source[k] for k in BASE}
    d.update(configuration_sha256=source["configuration_sha256"],
             selected_files_sha256=fingerprint(source["files"]))
    if source.get("certificate") is not None:d["certificate"]=plain(source["certificate"])
    else:d["configuration_stage"]=plain(source["configuration_stage"])
    return d
def same_source(a,b):
    assert all(str(a[k])==str(b[k]) for k in BASE)
    if a.get("configuration_sha256") is not None and b.get("configuration_sha256") is not None:
        assert a["configuration_sha256"]==b["configuration_sha256"]
def expected_tag(item,sources,inputs):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
            "method_sha256":item["method_sha256"],"proofs":item["proofs"],
            "artin_helper_sha256":ARTIN_SHA,
            "sources":{g:identity(sources[g]) for g in GROUPS},
            "inputs":inputs,"strategy":STRATEGY}
def topic_path(text):
    p=PurePosixPath(text);assert not p.is_absolute() and ".." not in p.parts
    return TOPIC/Path(*p.parts)
def dimensions(raw,m,n):
    assert isinstance(raw,list) and len(raw)==m and all(isinstance(r,list) and len(r)==n for r in raw)
def guard(item,path):
    global IO
    assert os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert path.resolve()==REQUEST.resolve()
    assert item["result"]==RESULT and item["p"]==41 and item["producer_inputs_pending"] is False
    assert item["core"]==CORE and sha(S/CORE)==item["core_sha256"]
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["artin_helper"]=="R885_whole_Artin_algebra.py"
    assert sha(S/item["artin_helper"])==ARTIN_SHA==item["artin_helper_sha256"]
    assert item["io_helper"]=="R824_public_original_global_polar_generators.py"
    helper=S/item["io_helper"];assert sha(helper)==RANGE_SHA==item["io_helper_sha256"]
    descriptor=importlib.util.spec_from_file_location("r899_frozen_stdlib_range",helper)
    IO=importlib.util.module_from_spec(descriptor);descriptor.loader.exec_module(IO)
    assert 0<item["budget_minutes"]<=300
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():assert sha(topic_path(row["path"]))==row["sha256"]
    assert item["proofs"]["R899"]["sha256"]=="eff6a8abf489bedf2cda8549a027ebd250717b2ddedece420f2a9d729cebc044"
    assert set(item["source_artifacts"])=={"R894","R845","R885","R880","R887","R872"}
    assert item["source_artifacts"]["R894"] is not None

def manifest_entries(folder,item):
    path=Path(folder)/MANIFEST
    assert sha(path)==item["manifest_sha256"]
    if item.get("manifest_bytes") is not None:assert path.stat().st_size==item["manifest_bytes"]
    m=read(path);assert m["result"]==item["result"]
    if m.get("source_commit") is not None:assert m["source_commit"]==item["source_commit"]
    entries={r["file"]:plain(r) for r in m["files"]}
    assert len(entries)==len(m["files"])
    if item.get("manifest_file_count") is not None:assert len(entries)==item["manifest_file_count"]
    entries[MANIFEST]=spec(path)
    return entries

def metadata(folder,item,entries):
    initial=read(bound(folder,entries["public-actions-input.json"]))
    run=read(bound(folder,entries["run-receipt.json"]))
    assert initial["source_commit"]==run["source_commit"]==item["source_commit"]
    assert str(run["workflow_run_id"])==str(item["run_id"])
    assert initial.get("core_sha256",initial.get("job",{}).get("core_sha256"))==item["core_sha256"]
    if item.get("wrapper_sha256") is not None:
        assert initial.get("wrapper_sha256",initial.get("job",{}).get("wrapper_sha256"))==item["wrapper_sha256"]
    core=None
    if run.get("core_receipt_sha256") is not None:
        assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
        core=read(bound(folder,entries["core-receipt.json"]))
        assert core["source_sha256"]==item["core_sha256"]
    cert=None
    if item.get("certificate") is not None:
        row=plain(item["certificate"]);assert entries[row["file"]]==row
        cert=read(bound(folder,row))
        assert cert["result"]==item["result"] and cert["complete"] is True
        assert run["complete"] is True and run["process_exit_code"]==0
        assert core is not None and core["complete"] is True and core["certificate_sha256"]==row["sha256"]
        tag=cert["configuration"]
    else:
        assert item["result"]=="R827-original-global-modular-derivative-termination"
        assert run["complete"] is False and run["process_exit_code"]==124
        row=plain(item["configuration_stage"]);assert entries[row["file"]]==row
        anchor=read(bound(folder,row));assert anchor["complete"] is True
        tag=anchor["configuration"]
    assert tag.get("source_sha256",tag.get("core_sha256"))==item["core_sha256"]
    if item.get("configuration_sha256") is not None:assert fingerprint(tag)==item["configuration_sha256"]
    if core is not None:
        if core.get("configuration") is not None:assert core["configuration"]==tag
        if core.get("configuration_sha256") is not None:assert core["configuration_sha256"]==fingerprint(tag)
    return initial,run,core,cert,tag

class Handle:
    def __init__(self,label,source,retained,work,inherited=None,archive_spec=None):
        self.label=label;self.item=dict(source);self.folder=Path(retained)/label
        self.folder.mkdir(parents=True,exist_ok=True)
        self.work=Path(work);self.archive=None;self.archive_spec=archive_spec or source
        self.selected={}
        if inherited is None:
            self.open_archive()
            self.archive.extract_bound(MANIFEST,source["manifest_sha256"],self.folder/MANIFEST,source.get("manifest_bytes"))
        self.entries=manifest_entries(self.folder,self.item)
        self.selected[MANIFEST]=self.entries[MANIFEST]
        names=["public-actions-input.json","run-receipt.json"]
        if "core-receipt.json" in self.entries:names.append("core-receipt.json")
        if source.get("certificate") is not None:names.append(source["certificate"]["file"])
        else:names.append(source["configuration_stage"]["file"])
        self.take(names)
        self.initial,self.run,self.core,self.certificate,self.tag=metadata(self.folder,self.item,self.entries)
        self.item["configuration_sha256"]=fingerprint(self.tag)
    def open_archive(self):
        if self.archive is None:
            assert self.archive_spec.get("artifact_id") is not None,("missing_source_route",self.label)
            same_source(self.archive_spec,self.item)
            self.archive=IO.Archive(self.archive_spec,self.work/("archive-"+self.label),whole=False)
    def take(self,names):
        todo=[]
        for name in sorted(set(names)):
            assert name in self.entries,(self.label,name)
            p=self.folder/name
            if p.exists():bound(self.folder,self.entries[name])
            else:todo.append(name)
        if todo:
            self.open_archive()
            self.archive.extract_many([(n,self.entries[n]["sha256"],self.folder/n,self.entries[n]["bytes"]) for n in todo])
        for name in names:
            bound(self.folder,self.entries[name]);self.selected[name]=self.entries[name]
    def raw(self,name):
        self.take([name]);return read(self.folder/name)
    def stage(self,row):
        row=plain(row);assert self.entries[row["file"]]==row
        value=self.raw(row["file"])
        assert value["complete"] is True and value["configuration"]==self.tag
        assert value.get("result",value["configuration"]["result"])==self.item["result"]
        return value
    def finish(self):
        item={k:v for k,v in self.item.items() if k not in ("files","directory","selected_files_sha256","selected_file_count")}
        item["files"]=dict(sorted(self.selected.items()))
        item["configuration_sha256"]=fingerprint(self.tag)
        return item
    def transport(self):
        return None if self.archive is None else self.archive.receipt()
    def close(self):
        if self.archive is not None:self.archive.close()

def unpack(bundle,root,sources):
    root=Path(root)
    wanted={g+"/"+n:(g,plain(row)) for g,s in sources.items() for n,row in s["files"].items()}
    seen=set()
    with tarfile.open(bundle,"r:gz") as tf:
        for member in tf:
            assert member.isfile() and not member.issym() and not member.islnk()
            name=member.name
            assert name in wanted and name not in seen,name
            group,row=wanted[name];assert member.size==row["bytes"]
            dest=root/group/row["file"];dest.parent.mkdir(parents=True,exist_ok=True)
            src=tf.extractfile(member);assert src is not None
            digest=hashlib.sha256();count=0
            if dest.exists():
                bound(dest.parent,row)
                for block in iter(lambda:src.read(4*1024*1024),b""):digest.update(block);count+=len(block)
            else:
                tmp=dest.with_name(dest.name+".unpack")
                with tmp.open("wb") as out:
                    for block in iter(lambda:src.read(4*1024*1024),b""):
                        digest.update(block);count+=len(block);out.write(block)
                assert count==row["bytes"] and digest.hexdigest()==row["sha256"]
                tmp.replace(dest)
            assert count==row["bytes"] and digest.hexdigest()==row["sha256"]
            seen.add(name)
    assert seen==set(wanted)
def pack(root,sources,target):
    root=Path(root);target=Path(target);tmp=target.with_name(target.name+".tmp")
    with tmp.open("wb") as f:
        with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0,compresslevel=1) as compressed:
            with tarfile.open(fileobj=compressed,mode="w|") as tf:
                for group in sorted(sources):
                    for name,row in sorted(sources[group]["files"].items()):
                        path=bound(root/group,row)
                        info=tf.gettarinfo(str(path),arcname=group+"/"+name)
                        info.uid=info.gid=0;info.uname=info.gname="";info.mtime=0;info.mode=0o644
                        with path.open("rb") as src:tf.addfile(info,src)
    tmp.replace(target)

def source_review(item,retained,sources,inputs):
    assert set(sources)==set(GROUPS)
    tags={};certs={}
    for group,source in sources.items():
        entries=manifest_entries(Path(retained)/group,source)
        for name,row in source["files"].items():
            assert name==row["file"]
            if name!=REFERENCE:assert entries[name]==plain(row)
            bound(Path(retained)/group,row)
        _,_,_,cert,tag=metadata(Path(retained)/group,source,entries)
        tags[group]=tag;certs[group]=cert
        for name in source["files"]:
            if name.endswith(".json.gz"):
                value=read(Path(retained)/group/name)
                if isinstance(value,dict) and "configuration" in value:
                    assert value["configuration"]==tag and value["complete"] is True
    trace=sources["R894"]
    same_source(item["source_artifacts"]["R894"],trace)
    assert trace["core_sha256"]==TRACE_CORE
    for g in OLD_GROUPS:same_source(tags["R894"]["sources"][g],sources[g])
    same_source(tags["R880"]["sources"]["R845"],sources["R845"])
    for group in ("R845","R885","R880","R887","R872"):
        same_source(item["source_artifacts"][group],sources[group])
    def stage(ref):
        group=ref["source_group"];row=plain(ref)
        assert sources[group]["files"][row["file"]]==row
        value=read(Path(retained)/group/row["file"])
        assert value["complete"] is True and value["configuration"]==tags[group]
        return value
    cert=certs["R894"]
    assert cert["actual_new_complete_flip_count"]==16 and cert["actual_reused_R890_complete_flip_count"]==2
    assert cert["actual_original_seven_pole_trace_bounded_identity_certified"] is True
    marked=stage(inputs["marked_QN"])
    assert plain(cert["marked_principal_and_descent"])==plain(inputs["marked_QN"])
    assert marked["actual_rho_order"]==-8435 and marked["DN_avoids_original_P0"] is True
    assert plain(marked["source_complete_DN_normal418"])==plain(inputs["terminal_normal418"])
    basis=stage(inputs["terminal_normal418"])
    dimensions(basis["normal_V3_basis_mod_prime"],690,418)
    assert basis["complete_RR_space_certified"] is True
    assert len(inputs["original_normal_V3_fibres"])==len(inputs["original_Krylov_points"])==len(inputs["original_characteristic_nodes"])==7
    assert len(inputs["new_trace_flips"])==16 and len(inputs["two_original_chi_flips"])==2
    assert len(inputs["six_original_branches"])==6 and len(inputs["original_zero_a_old_fibres"])==5
    relation=stage(inputs["original_characteristic_relation"])
    assert relation["exact_original_modular_characteristic_polynomial_certified"] is True
    for z,row in enumerate(inputs["original_characteristic_nodes"]):
        assert plain(row)==plain(relation["source_node_stages"][z])
        node=stage(row);assert node["z_value"]==z and node["ordinal"]==z
        assert len(node["characteristic_coefficients_ascending_T"])==273 and node["monic"] is True
    for j,row in enumerate(inputs["six_original_branches"],1):
        principal=stage(row["principal"])
        assert principal["sigma_power"]==j and principal["original_branch"]==[0,6,1,2,4,3,5][j]
        stage(row["a"]);stage(row["v"])
    for row in inputs["new_trace_flips"]+inputs["two_original_chi_flips"]:
        complete=stage(row["complete"]);principal=stage(row["principal"]);u=stage(row["u"])
        assert plain(complete["principal_function_and_P0_unit"])==plain(row["principal"])
        assert plain(complete["original_unscaled_P0_unit_section"])==plain(row["u"])
        assert principal["all_selected_original_scalars_retained"] is True
        assert u["original_scalar_not_rescaled"] is True
    return {"result":RESULT,"source_identities":{g:identity(sources[g]) for g in GROUPS},
        "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
        "selected_file_count":sum(len(sources[g]["files"]) for g in GROUPS),
        "all_selected_original_bytes_and_configurations_verified":True,
        "new_mathematics_executed":False,"old_normal_conversion_or_charpoly_recomputed":False}

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R899";retained.mkdir(parents=True,exist_ok=True)
    if all((out/n).exists() for n in (BUNDLE,INVENTORY,RECEIPT)):
        inv=read(out/INVENTORY);receipt=read(out/RECEIPT)
        assert inv["result"]==receipt["result"]==RESULT and inv["complete"] is True and receipt["complete"] is True
        assert plain(receipt["source_inventory"])==spec(out/INVENTORY)
        assert plain(receipt["source_bundle"])==spec(out/BUNDLE)
        sources,inputs=inv["sources"],inv["inputs"]
        unpack(out/BUNDLE,retained,sources)
        review=source_review(item,retained,sources,inputs)
        assert receipt["source_identities"]=={g:identity(sources[g]) for g in GROUPS}
        return retained,sources,inputs,review
    assert allow_download,"Bound source carrier is required for offline verification"
    work=out.parent/"R899-download";handles={}
    try:
        tr=Handle("R894",item["source_artifacts"]["R894"],retained,work);handles["R894"]=tr
        assert tr.item["core_sha256"]==TRACE_CORE
        cert=tr.certificate
        assert cert["actual_original_seven_pole_trace_bounded_identity_certified"] is True
        tr.take([TRACE_INVENTORY,TRACE_RECEIPT,TRACE_BUNDLE])
        inv=tr.raw(TRACE_INVENTORY);receipt=tr.raw(TRACE_RECEIPT)
        assert inv["result"]==receipt["result"]==tr.item["result"]
        assert inv["complete"] is True and receipt["complete"] is True
        assert plain(receipt["source_inventory"])==tr.entries[TRACE_INVENTORY]
        assert plain(receipt["source_bundle"])==tr.entries[TRACE_BUNDLE]
        assert tr.initial["source_inventory"]==tr.entries[TRACE_INVENTORY]
        inherited=inv["sources"];oldinputs=inv["inputs"]
        assert set(inherited)==set(OLD_GROUPS)
        assert {g:identity(inherited[g]) for g in OLD_GROUPS}==tr.tag["sources"]
        assert oldinputs==tr.tag["inputs"]
        unpack(tr.folder/TRACE_BUNDLE,retained,inherited)
        for group in OLD_GROUPS:
            route=item["source_artifacts"].get(group)
            handles[group]=Handle(group,inherited[group],retained,work,inherited=True,archive_spec=route)
        for group in ("R845","R885"):
            handles[group]=Handle(group,item["source_artifacts"][group],retained,work)
        def take(group,row):
            value=handles[group].stage(row)
            return value,group_ref(group,row)
        def old(row):
            return take(row["source_group"],row)
        inputs={}
        marked,inputs["marked_QN"]=take("R894",cert["marked_principal_and_descent"])
        _,inputs["terminal_normal418"]=take("R894",marked["source_complete_DN_normal418"])
        neutral_name="R894-neutral-H-and-original-P0-functional.json.gz"
        _,inputs["original_neutral"]=take("R894",tr.entries[neutral_name])
        for key in ("original_W","original_place"):
            _,inputs[key]=old(oldinputs[key])
        _,inputs["original_t_frame"]=old(oldinputs["t_frame"])
        _,inputs["original_point_linearization"]=old(oldinputs["point_linear_functional"])
        inputs["original_Krylov_points"]=[old(x)[1] for x in oldinputs["original_Krylov_points"]]
        inputs["original_normal_V3_fibres"]=[old(x)[1] for x in oldinputs["R890_normal_fibres"]]
        q0,inputs["original_zero_Qtilde"]=old(oldinputs["Qtilde"])
        qf,inputs["original_zero_Qf"]=take("R880",q0["source_original_Q_f"])
        selection,inputs["original_zero_a_selection"]=take("R880",qf["source_original_anchor_selection"])
        _,inputs["original_zero_v"]=take("R880",qf["source_exact_v"])
        _,inputs["original_zero_a_candidate"]=take("R845",selection["source_original_sections"])
        assert selection["selected_original_role"]=="a" and selection["no_rescaling"] is True
        inputs["original_zero_a_old_fibres"]=[]
        for z in range(5):
            name=f"R839-pole-fixed-a-fiber-{z}-times-V3.json.gz"
            _,ref=take("R845",handles["R845"].entries[name]);inputs["original_zero_a_old_fibres"].append(ref)
        _,inputs["original_u_C"]=take("R887",q0["source_exact_u_C"])
        _,inputs["original_u_chi"]=take("R872",qf["exact_function_DAG"]["u_chi_over_tau2"]["source_section"])
        inputs["six_original_branches"]=[]
        for j,row in enumerate(oldinputs["six_Dstar_branches"],1):
            principal,pr=old(row["principal"])
            _,ar=take("SIXD",principal["source_actual_a"]);_,vr=take("SIXD",principal["source_actual_v"])
            inputs["six_original_branches"].append({"sigma_power":j,"principal":pr,"a":ar,"v":vr})
        inputs["two_original_chi_flips"]=[]
        for key in ("X2","X4"):
            complete,cr=old(oldinputs["reused_complete_flips"][key])
            _,pr=take("R890",complete["principal_function_and_P0_unit"])
            _,ur=take("R890",complete["original_unscaled_P0_unit_section"])
            inputs["two_original_chi_flips"].append({"complete":cr,"principal":pr,"u":ur})
        inputs["new_trace_flips"]=[]
        for row in cert["complete_new_flip_certificates"]:
            complete,cr=take("R894",row)
            _,pr=take("R894",complete["principal_function_and_P0_unit"])
            _,ur=take("R894",complete["original_unscaled_P0_unit_section"])
            inputs["new_trace_flips"].append({"complete":cr,"principal":pr,"u":ur,
                                             "space":group_ref("R894",complete["complete_normal418_space"])})
        poly=handles["R885"]
        relation,inputs["original_characteristic_relation"]=take("R885",poly.certificate["characteristic_relation"])
        inputs["original_characteristic_nodes"]=[take("R885",row)[1] for row in relation["source_node_stages"][:7]]
        # Keep the original inventory/receipt but avoid a second nested copy of
        # its full carrier. The selected unchanged old files are packed once.
        del tr.selected[TRACE_BUNDLE]
        sources={g:handles[g].finish() for g in GROUPS}
        review=source_review(item,retained,sources,inputs)
        transports={g:h.transport() for g,h in handles.items() if h.archive is not None}
        transports["original_R894_carrier"]={
            "source":item["source_artifacts"]["R894"],"inventory":tr.entries[TRACE_INVENTORY],
            "receipt":tr.entries[TRACE_RECEIPT],"bundle":tr.entries[TRACE_BUNDLE],
            "all_original_carrier_members_hashed":True,"only_needed_original_members_repacked":True}
        save(out/INVENTORY,{"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
            "transports":transports,"new_mathematics_executed":False})
        pack(retained,sources,out/BUNDLE)
        save(out/RECEIPT,{"result":RESULT,"complete":True,"source_inventory":spec(out/INVENTORY),
            "source_bundle":spec(out/BUNDLE),"source_identities":{g:identity(sources[g]) for g in GROUPS},
            "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
            "selected_original_file_count":sum(len(s["files"]) for s in sources.values()),
            "new_mathematics_executed":False})
        print("R899_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,sources,inputs,review
    finally:
        for h in handles.values():h.close()

def stable_job(item):
    return {k:v for k,v in item.items() if k not in (
        "resume","budget_minutes","rules_last_read_commit","session",
        "wrapper_sha256","workflow")}
def restore(item,out):
    resume=item.get("resume")
    if resume is None:return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R899-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R899-resume-archive",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],directory/MANIFEST,resume.get("manifest_bytes"))
        entries=manifest_entries(directory,resume)
        names=set(META)&set(entries)
        names|={BUNDLE,INVENTORY,RECEIPT}
        if FINAL in entries:names.add(FINAL)
        for name in names:assert name in entries
        archive.extract_many([(n,entries[n]["sha256"],directory/n,entries[n]["bytes"]) for n in names])
        initial=read(directory/"public-actions-input.json");run=read(directory/"run-receipt.json")
        assert initial["source_commit"]==run["source_commit"]==resume["source_commit"]
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        assert initial["core_sha256"]==item["core_sha256"]
        assert stable_job(initial["job"])==stable_job(item)
        if run.get("core_receipt_sha256") is not None:
            assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
            core=read(directory/"core-receipt.json");assert core["source_sha256"]==item["core_sha256"]
        else:assert run["complete"] is False
        inventory=read(directory/INVENTORY);receipt=read(directory/RECEIPT)
        assert plain(receipt["source_inventory"])==entries[INVENTORY]
        assert plain(receipt["source_bundle"])==entries[BUNDLE]
        sources,inputs=inventory["sources"],inventory["inputs"]
        tag=expected_tag(item,sources,inputs)
        assert fingerprint(tag)==initial["mathematical_configuration_sha256"]
        stages=[n for n in entries if n.startswith(PREFIX) and n.endswith(".json.gz")]
        archive.extract_many([(n,entries[n]["sha256"],directory/n,entries[n]["bytes"]) for n in stages])
        for n in stages:
            value=read(directory/n)
            assert value["result"]==RESULT and value["configuration"]==tag
            assert value["complete"] is True or n==PREFIX+"current.json.gz"
            shutil.copyfile(directory/n,out/n)
        for n in (BUNDLE,INVENTORY,RECEIPT):shutil.copyfile(directory/n,out/n)
        if FINAL in entries:
            cert=read(directory/FINAL)
            assert cert["result"]==RESULT and cert["configuration"]==tag
            if cert["complete"] is True:
                assert run["complete"] is True
                inv=read(bound(directory,cert["stage_manifest"]))
                for row in inv["files"]:assert entries[row["file"]]==plain(row)
                assert entries[cert["resume_state"]["file"]]==plain(cert["resume_state"])
                shutil.copyfile(directory/FINAL,out/FINAL)
        save(out/"resume-import-receipt.json",{"result":RESULT,"complete":True,
            "source":resume,"source_manifest":spec(directory/MANIFEST),
            "mathematical_configuration_sha256":fingerprint(tag),
            "restored_complete_or_current_stage_count":len(stages),
            "false_FINAL_not_restored_as_completed_or_used_to_pin_later_current":True,
            "core_receipt_present":run.get("core_receipt_sha256") is not None,
            "range_transport":archive.receipt()})
    finally:archive.close()

def output_manifest(out):
    files=[]
    for p in sorted(Path(out).iterdir()):
        if not p.is_file() or p.name in (MANIFEST,REFERENCE):continue
        if p.name.endswith((".tmp",".download",".partial",".unpack")):continue
        files.append(spec(p))
    save(Path(out)/MANIFEST,{"result":RESULT,"source_commit":os.environ["GITHUB_SHA"],
        "workflow_run_id":os.environ["GITHUB_RUN_ID"],"files":files})
    save(Path(out)/REFERENCE,{"result":RESULT,**spec(Path(out)/MANIFEST)})
    return spec(Path(out)/MANIFEST)
def compute(item,out,request):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    code,error,outer=1,None,False
    try:
        restore(item,out)
        retained,sources,inputs,review=prepare(item,out)
        expanded={**item,"sources":sources,"inputs":inputs}
        save(out/EXPANDED,expanded);tag=expected_tag(item,sources,inputs)
        save(out/"public-actions-input.json",{"result":RESULT,"p":41,
            "source_commit":os.environ["GITHUB_SHA"],"workflow_run_id":os.environ["GITHUB_RUN_ID"],
            "core_sha256":item["core_sha256"],"wrapper_sha256":item["wrapper_sha256"],
            "job":item,"request_sha256":sha(request),"workflow_sha256":sha(REPO/item["workflow"]),
            "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
            "source_inventory":spec(out/INVENTORY),"expanded_job":spec(out/EXPANDED),
            "source_identities":{g:identity(sources[g]) for g in GROUPS},
            "mathematical_configuration_sha256":fingerprint(tag),"new_mathematics_in_wrapper":False})
        command=[sys.executable,str(S/CORE),"--config",str(out/EXPANDED),
                 "--retained",str(retained),"--output",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"core.log").open("ab") as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:code=process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                outer=True
                os.killpg(process.pid,signal.SIGTERM)
                try:process.wait(timeout=15)
                except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
                code=124;error="outer_timeout"
        print((out/"core.log").read_text(errors="replace")[-16000:],flush=True)
        if code==0:assert read(out/FINAL)["complete"] is True
    except Exception as exc:
        code=1 if code in (0,1) else code
        error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    finally:
        save(out/"run-receipt.json",{"result":RESULT,
            "source_commit":os.environ["GITHUB_SHA"],"workflow_run_id":os.environ["GITHUB_RUN_ID"],
            "workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_sha256":item["core_sha256"],"wrapper_sha256":item["wrapper_sha256"],
            "complete":code==0,"process_exit_code":code,"error":error,"outer_timeout":outer,
            "core_receipt_sha256":sha(out/"core-receipt.json") if (out/"core-receipt.json").exists() else None,
            "execution_environment":"public-repository-github-actions",
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    return code

def verify_complete(out,entries,tag,cert,sources,inputs):
    def own(row):
        row=plain(row);assert entries[row["file"]]==row
        value=read(bound(out,row))
        assert value["complete"] is True and value["configuration"]==tag and value["result"]==RESULT
        return value
    assert cert["all418_original_K_fixed_functions_certified"] is True
    assert cert["new_fixed_basis_descent_identity_certified"] is True
    assert cert["actual_evaluation_rank"]==418
    assert cert["source_inputs"]==inputs
    assert cert["source_identities"]=={g:identity(sources[g]) for g in GROUPS}
    assert cert["original_normal_V3_fibres"]==inputs["original_normal_V3_fibres"]
    assert cert["original_Krylov_points"]==inputs["original_Krylov_points"]
    assert cert["original_W"]==inputs["original_W"] and cert["marked_QN"]==inputs["marked_QN"]
    profile=own(cert["selected_evaluation_inverse"])
    assert profile["actual_rank"]==418 and profile["accepted"] is True
    assert profile["actual_selected_minor_determinant_mod_prime"]!=0
    assert len(profile["selected_row_indices"])==len(set(profile["selected_row_indices"]))==418
    assert profile["selected_row_labels"]==cert["actual_selected_row_labels"]
    dimensions(profile["selected_square_mod_prime"],418,418)
    dimensions(profile["selected_inverse_mod_prime"],418,418)
    assert profile["both_selected_inverse_products_verified"] is True
    assert profile["all_computed_rows_multiplied_by_same_inverse"] is True
    assert profile["selected_coordinates_of_all418_normalized_functions_are_identity"] is True
    dimensions(profile["complete_normalized_evaluation_mod_prime"],profile["matrix_shape"][0],418)
    basis=own(cert["complete_K_fixed_normal_basis"])
    assert basis["source_original_QN"]==inputs["marked_QN"]
    assert basis["source_original_DN_normal418"]==inputs["terminal_normal418"]
    assert basis["source_selected_evaluation_inverse"]==cert["selected_evaluation_inverse"]
    dimensions(basis["normal_V3_basis_mod_prime"],690,418)
    assert basis["all418_original_K_fixed_functions_certified"] is True
    assert basis["normal_sections_without_QN_claimed_K_fixed"] is False
    assert basis["exact_fixed_functions_DAG"]["operation"]=="positive_multiply_original_QN"
    assert basis["exact_fixed_functions_DAG"]["original_QN_source"]==inputs["marked_QN"]
    assert basis["new_fixed_basis_descent_matrix"]=={"operation":"identity_matrix","dimension":418}
    assert basis["old_descent_matrix_numeric_arrays_computed"] is False
    assert basis["new_fixed_basis_action_identity_certified_by_uniqueness"] is True
    assert basis["sevenfold_cocycle_certified_by_exact_telescoping"] is True
    point=own(cert["original_P0_leading_row"])
    assert point["source_K_fixed_normal_basis"]==cert["complete_K_fixed_normal_basis"]
    assert point["source_original_QN"]==inputs["marked_QN"]
    assert len(point["normal_V3_P0_functional_mod_prime"])==690
    for k in ("normal_V3_P0_values_mod_prime","rho_leading_coefficients_mod_prime","t_leading_coefficients_mod_prime"):
        assert len(point[k])==418
    assert point["original_rho_and_t_order"]==-8435 and point["selected_column_rescaled"] is False
    assert point["actual_marked_P0_unit_column_certified"]==cert["original_marked_P0_unit_column_certified"]
    assert point["first_unit_column"]==cert["actual_first_P0_unit_column"]
    first=point["first_unit_column"]
    if first is not None:
        assert 0<=first<418 and point["t_leading_coefficients_mod_prime"][first]!=0
        assert all(v==0 for v in point["t_leading_coefficients_mod_prime"][:first])
    else:assert all(v==0 for v in point["t_leading_coefficients_mod_prime"])
    for z,row in cert["completed_normalized_space_fibres"].items():
        value=own(row);assert value["z0"]==int(z)
        assert value["source_K_fixed_normal_basis"]==cert["complete_K_fixed_normal_basis"]
        assert value["original_QN_factor_included"] is False
        dimensions(value["normal_evaluation_mod_prime"],272,418)
        dimensions(value["cyclic_evaluation_mod_prime"],272,418)
    for row in cert["node_decisions"]:
        value=own(row)
        if value["accepted"]:
            H=own(value["complete_evaluation"])
            dimensions(H["matrix_mod_prime"],272,418)
            assert H["original_QN_factor_included"] is True
            assert H["coordinates_in_original_K_defined_normal_basis"] is True
        else:
            assert value["failure_witness"]["whole_fibre_unit"] is False
            assert value["geometric_nonexistence_concluded"] is False
    for key in ("old_basis_descent_matrix_numeric_arrays_computed",
                "original_QN_and_selected_scalars_rescaled",
                "old_sixteen_flips_or_six_Galois_replays_computed",
                "old_charpoly_Krylov_V3_evaluations_point_jets_or_t_constant_recomputed",
                "characteristic_zero_coefficients_reconstructed",
                "Q_fixed_basis_K_defined_effective272_representative_or_height_computed"):
        assert cert[key] is False

def verify(item,out):
    out=Path(out)
    manifest=read(out/MANIFEST);assert manifest["result"]==RESULT
    entries={r["file"]:plain(r) for r in manifest["files"]}
    assert len(entries)==len(manifest["files"])
    for row in entries.values():bound(out,row)
    run=read(out/"run-receipt.json")
    assert run["source_commit"]==manifest["source_commit"]
    assert run["core_sha256"]==item["core_sha256"]
    if not all(n in entries for n in ("public-actions-input.json",BUNDLE,INVENTORY,RECEIPT)):
        assert run["complete"] is False and run["core_receipt_sha256"] is None
        return {"result":RESULT,"complete":False,"source_preparation_failed":True,
                "process_exit_code":run["process_exit_code"],"error":run["error"],
                "new_mathematics_executed_in_IO":False}
    retained,sources,inputs,review=prepare(item,out,allow_download=False)
    tag=expected_tag(item,sources,inputs)
    initial=read(out/"public-actions-input.json")
    assert initial["source_commit"]==run["source_commit"]
    assert initial["source_inventory"]==entries[INVENTORY]
    assert initial["expanded_job"]==entries[EXPANDED]
    expanded=read(out/EXPANDED)
    assert expanded["sources"]==sources and expanded["inputs"]==inputs
    assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
    stages={};currents=[]
    for name,row in entries.items():
        if not name.startswith(PREFIX) or not name.endswith(".json.gz"):continue
        value=read(out/name)
        assert value["result"]==RESULT and value["configuration"]==tag
        if name==PREFIX+"current.json.gz":
            assert value["complete"] is False;currents.append(row)
        else:
            assert value["complete"] is True
            if not name.startswith(PREFIX+"stage-manifest-"):stages[name]=row
    core=None
    if run["core_receipt_sha256"] is not None:
        assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
        core=read(out/"core-receipt.json")
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        if core.get("configuration_sha256") is not None:assert core["configuration_sha256"]==fingerprint(tag)
    else:assert run["complete"] is False
    cert=None
    if FINAL in entries:
        cert=read(out/FINAL);assert cert["result"]==RESULT and cert["configuration"]==tag
        if cert["complete"] is True:
            assert run["complete"] is True and run["process_exit_code"]==0
            assert core is not None and core["complete"] is True
            assert core["certificate_sha256"]==entries[FINAL]["sha256"]
            inv=read(bound(out,cert["stage_manifest"]))
            assert inv["result"]==RESULT and inv["configuration"]==tag and inv["complete"] is True
            assert {r["file"]:plain(r) for r in inv["files"]}==stages
            assert cert["actual_retained_complete_math_stage_count"]==len(stages)
            assert entries[cert["resume_state"]["file"]]==plain(cert["resume_state"])
            verify_complete(out,entries,tag,cert,sources,inputs)
        else:assert run["complete"] is False
    if run["complete"]:assert cert is not None and cert["complete"] is True
    return {"result":RESULT,"complete":run["complete"],"process_exit_code":run["process_exit_code"],
        "core_receipt_present":core is not None,"outer_timeout":run["outer_timeout"],
        "source_manifest":spec(out/MANIFEST),"certificate":entries.get(FINAL),
        "actual_retained_complete_stage_count":len(stages),"actual_current_count":len(currents),
        "source_inventory":entries[INVENTORY],"retained_source_bundle":entries[BUNDLE],
        "actual_evaluation_rank":cert.get("actual_evaluation_rank") if cert else None,
        "all418_original_K_fixed_functions_certified":bool(cert and cert["all418_original_K_fixed_functions_certified"]),
        "original_marked_P0_unit_column_certified":bool(cert and cert["original_marked_P0_unit_column_certified"]),
        "actual_first_P0_unit_column":cert.get("actual_first_P0_unit_column") if cert else None,
        "source_check":review,"new_mathematics_executed_in_IO_verification":False}

def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("compute","verify"))
    parser.add_argument("--request",type=Path,default=REQUEST)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();item=read(args.request);guard(item,args.request)
    if args.mode=="verify":
        print("R899_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
        return 0
    code=compute(item,args.output,args.request)
    try:print("R899_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
    except Exception:
        traceback.print_exc()
        if code==0:code=1
    return code
if __name__=="__main__":
    raise SystemExit(main())

