#!/usr/bin/env python3
"""R907 stdlib source transport, same-source continuation and public driver; no mathematics."""
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
RESULT="R907-original-Iz-pencils-and-nine-Hecke-norm-generators"
FINAL="p41-original-Iz-pencils-and-nine-Hecke-norm-generators-certificate.json"
PREFIX="R907-"
CORE="R907_original_Iz_pencils_and_nine_Hecke_norms.py"
HELPER="R907_complete_pencil_norm_algebra.py"
ARTIN="R885_whole_Artin_algebra.py"
ARTIN_SHA="e47cd50d254700b98446866297d79694c100f1435c46f3b4f42e3835763f897d"
REQUEST=TOPIC/"notes/R907-nine-Hecke-norms-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R907-retained-original-inputs.tar.gz"
INVENTORY="R907-original-source-inventory.json"
INPUT_RECEIPT="R907-retained-inputs-receipt.json"
EXPANDED="R907-expanded-job.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
DIRECT_GROUPS=("R903","R901","R899","ARTIN")
STD_IO="R890_public_original_Ef_eight_flip_and_marked_frame.py"
STD_SHA="5a5e706d11d3b61a6af7acadd4624f7f1e398afe02e6ee77c339fcf7b01f57f1"
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
P=1000000753
EPS=[0]+[1]*144+[2]*127
SIGMA_BRANCHES=[0,6,1,2,4,3,5]
RHO_ORDERS=[-686,-182,-231,-707,-1659]
IO=None

STRATEGY={
    "original_curve":"genus127 Y, p41, level82, original minus3 descent",
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "normal_basis_degrees":EPS,
    "space":"R903 H0(3H-DZ-Dchi-18P0), dim128, positive Phi=QZ/qchi",
    "pencil":"unchanged first P0-unit column, then original positive-integer power combination",
    "pencil_fibre_matrix_shape":[816,836],"required_pencil_rank":672,
    "pencil_common_Phi_cancelled_only_for_rank":True,
    "complete_fibre_count_per_pencil_matrix":3,"whole_fibre_dimension":272,
    "source_node_schedule":list(range(7)),
    "norm_source":"completed R885 full A272 and E2176, all272 original target coordinates",
    "norm_pencil":"one division-free Berkowitz over A[T], degrees0..8, full E[T] Cayley-Hamilton",
    "norm_Phi":"positive complete rank8 norm, no assumption Phi or pencil sections are units",
    "all_expression_denominators_required_units_on_entire_E":True,
    "norm_parameters":list(range(9)),
    "source_sigma_branch_order":SIGMA_BRANCHES,
    "reference":"R879 (1,v0), old R885 nine values reused",
    "two_chart_ideal":"same nine exact global functions on both original charts; Jj*inverse(J0)",
    "inverse_ideal":"colon {x:x*J0 subset R}, not a sum of generator reciprocals",
    "frozen_Hecke_direction":"Nm_target(source_pullback I), via original canonical dual7",
    "endpoint_P0_P1_det_fibre_expressions_retained":True,
    "endpoint_numeric_calibration_not_in_this_scope":True,
    "old_flips_Krylov_target_coordinates_reference_norms_or_jets_recomputed":False,
    "Q_fixed_basis_or_modular_inactive_claimed":False,
    "budget_trial_prefix_direction_prefix_excluded_from_identity":True}


def frozen_stdlib():
    path=S/STD_IO
    assert hashlib.sha256(path.read_bytes()).hexdigest()==STD_SHA
    d=importlib.util.spec_from_file_location("R907_frozen_R890_stdlib",path)
    module=importlib.util.module_from_spec(d);d.loader.exec_module(module)
    return module
L=frozen_stdlib()
sha,read,save,fingerprint,plain,spec=L.sha,L.read,L.save,L.fingerprint,L.plain,L.spec
bound,topic_path,group_ref,same_source=L.bound,L.topic_path,L.group_ref,L.same_source
entry_map,metadata,pack,unpack=L.entry_map,L.metadata,L.pack,L.unpack

def identity(source):
    d={k:source[k] for k in BASE}
    d.update(configuration_sha256=source["configuration_sha256"],
             selected_files_sha256=fingerprint(source["files"]))
    if source.get("certificate") is not None:
        d["certificate"]=plain(source["certificate"])
    else:
        d["configuration_stage"]=plain(source["configuration_stage"])
    return d

def expected_tag(item,sources,inputs):
    return {"result":RESULT,"source_sha256":item["core_sha256"],
        "helper_sha256":item["helper_sha256"],"original_Artin_helper_sha256":ARTIN_SHA,
        "python_flint":"0.9.0","p":41,"method_sha256":item["method_sha256"],"proofs":item["proofs"],
        "sources":{g:identity(v) for g,v in sorted(sources.items())},
        "inputs":inputs,"strategy":STRATEGY}

def load_io():
    global IO
    path=S/RANGE_FILE
    assert sha(path)==RANGE_SHA
    d=importlib.util.spec_from_file_location("R907_frozen_stdlib_Range",path)
    IO=importlib.util.module_from_spec(d);d.loader.exec_module(IO)

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve()
    assert item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False,"R907 producer inputs remain pending"
    for key,name in (("core",CORE),("wrapper",Path(__file__).name),("helper",HELPER)):
        assert item[key]==name and sha(S/name)==item[key+"_sha256"]
    assert item["original_Artin_helper"]==ARTIN and item["original_Artin_helper_sha256"]==ARTIN_SHA
    assert sha(S/ARTIN)==ARTIN_SHA
    assert item["stdlib_io"]==STD_IO and item["stdlib_io_sha256"]==STD_SHA
    assert item["io_helper"]==RANGE_FILE and item["io_helper_sha256"]==RANGE_SHA
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert 0<item["budget_minutes"]<=300
    assert item["maximum_pencil_trials"]>=1 and 1<=item["maximum_fibre_triples"]<=35
    assert item["requested_directions"] and sorted(set(item["requested_directions"]))==item["requested_directions"]
    assert all(1<=j<=5 for j in item["requested_directions"])
    assert all(item["source_artifacts"].get(g) is not None for g in DIRECT_GROUPS)
    load_io()

class Original:
    """Preserve original identity/tag; only transport and the selected-file inventory change."""
    def __init__(self,registry,label,source,direct=False):
        self.R=registry;self.label=label;self.source=dict(source);self.folder=registry.retained/label
        self.folder.mkdir(parents=True,exist_ok=True)
        self.archive=None;self.selected={};self.transports=[];self.direct=bool(direct)
        self.route=registry.routes.get(label)
        if direct:
            assert self.route is not None
            same_source(self.route,source)
        self.entries=None;self.tag=None;self.certificate=None;self.initial=None
    def archive_open(self):
        if self.archive is None:
            assert self.route is not None,("missing_original_transport_route",self.label)
            same_source(self.source,self.route)
            self.archive=IO.Archive(self.route,self.R.work/("archive-"+self.label),whole=False)
        return self.archive
    def initialize(self):
        if not (self.folder/MANIFEST).exists():
            prepared=self.R.item.get("prepared_transport",{}).get(self.label)
            if prepared is not None:
                outer=IO.Archive(prepared["archive"],self.R.work/("intake-"+self.label),whole=False)
                try:
                    row=plain(prepared["package"]);path=self.R.work/(self.label+"-"+row["file"])
                    outer.extract_bound(row["file"],row["sha256"],path,row["bytes"])
                    L.extract_flat_package(path,self.folder)
                    self.transports.append({"kind":"completed_original_intake","archive":prepared["archive"],
                        "package":row,"Range":outer.receipt()})
                finally:
                    outer.close()
            else:
                self.archive_open().extract_bound(MANIFEST,self.source["manifest_sha256"],
                    self.folder/MANIFEST,self.source.get("manifest_bytes"))
        self.entries=entry_map(self.folder,self.source)
        names=list(META)
        if self.source.get("certificate") is None:
            assert self.label=="R827"
            names.append(self.source["configuration_stage"]["file"])
        else:
            row=self.entries[self.source["certificate"]["file"]]
            assert row["sha256"]==self.source["certificate"]["sha256"]
            if self.source["certificate"].get("bytes") is not None:
                assert row["bytes"]==self.source["certificate"]["bytes"]
            self.source["certificate"]=row;names.append(row["file"])
        self.take(names)
        self.certificate,self.tag,self.initial=metadata(self.label,self.folder,self.source,self.entries)
        self.source["configuration_sha256"]=fingerprint(self.tag)
        self.selected[MANIFEST]=self.entries[MANIFEST]
        return self
    def take(self,names):
        names=sorted(set(names));missing=[]
        for name in names:
            assert name in self.entries,(self.label,name)
            if (self.folder/name).exists():
                bound(self.folder,self.entries[name])
            else:
                missing.append(name)
        if missing:
            self.archive_open().extract_many([(n,self.entries[n]["sha256"],self.folder/n,self.entries[n]["bytes"]) for n in missing])
        for n in names:
            bound(self.folder,self.entries[n]);self.selected[n]=self.entries[n]
    def raw(self,row):
        row=self.entries[row] if isinstance(row,str) else plain(row)
        assert self.entries[row["file"]]==plain(row);self.take([row["file"]])
        return read(self.folder/row["file"])
    def stage(self,row):
        value=self.raw(row)
        assert value["complete"] is True and value["configuration"]==self.tag
        return value
    def ref(self,row):
        if isinstance(row,str):
            row=self.entries[row]
        self.take([row["file"]])
        return group_ref(self.label,row)
    def finish(self):
        value={**{k:self.source[k] for k in BASE},"configuration_sha256":fingerprint(self.tag),
            "files":dict(sorted(self.selected.items()))}
        if self.source.get("certificate") is None:
            value["certificate"]=None;value["configuration_stage"]=plain(self.source["configuration_stage"])
        else:
            value["certificate"]=plain(self.source["certificate"])
        for key in ("manifest_bytes","manifest_file_count","wrapper_sha256"):
            if self.source.get(key) is not None:
                value[key]=self.source[key]
        return value
    def transport(self):
        out=list(self.transports)
        if self.archive is not None:
            out.append({"kind":"manifest_bound_original_Range","archive":self.route,"receipt":self.archive.receipt()})
        return out
    def close(self):
        if self.archive is not None:
            self.archive.close()

class Registry:
    def __init__(self,item,retained,work):
        self.item=item;self.retained=Path(retained);self.work=Path(work)
        self.routes={g:dict(v) for g,v in item["source_artifacts"].items() if v is not None}
        self.retained.mkdir(parents=True,exist_ok=True);self.work.mkdir(parents=True,exist_ok=True)
        self.groups={};self.carriers={}
    def add(self,label,source,direct=False):
        if label in self.groups:
            h=self.groups[label];same_source(h.source,source)
            assert fingerprint(h.tag)==source["configuration_sha256"]
            if direct:
                h.route=self.item["source_artifacts"][label];h.direct=True
            return h
        h=Original(self,label,source,direct)
        self.groups[label]=h
        return h.initialize()
    def direct(self,label):
        return self.add(label,self.item["source_artifacts"][label],True)
    def carry(self,parent,prefix):
        """Original bundle checked in full; no nested carrier is packed into the child a second time."""
        inventory=prefix+"-original-source-inventory.json"
        receipt=prefix+"-retained-inputs-receipt.json"
        package=prefix+"-retained-original-inputs.tar.gz"
        parent.take([inventory,receipt,package])
        inv=parent.raw(inventory);r=parent.raw(receipt)
        assert inv["complete"] is True and r["complete"] is True
        assert inv["result"]==r["result"]==parent.source["result"]
        assert plain(r["source_inventory"])==parent.entries[inventory]
        assert plain(r["source_bundle"])==parent.entries[package]
        if parent.initial.get("source_inventory") is not None:
            assert plain(parent.initial["source_inventory"])==parent.entries[inventory]
        assert inv["inputs"]==parent.tag["inputs"]
        assert {g:identity(s) for g,s in inv["sources"].items()}==parent.tag["sources"]
        assert r["source_identities"]==parent.tag["sources"]
        unpack(parent.folder/package,self.retained,inv["sources"])
        inherited_routes=parent.initial.get("job",{}).get("source_artifacts",{})
        for label,source in inv["sources"].items():
            route=inherited_routes.get(label)
            if route is not None and label not in self.routes:
                same_source(source,route);self.routes[label]=dict(route)
            h=self.add(label,source)
            if h.route is None and label in self.routes:
                h.route=self.routes[label]
        parent.selected.pop(package,None)
        self.carriers[parent.label]={"original_source":{k:parent.source[k] for k in BASE},
            "inventory":parent.ref(inventory),"receipt":parent.ref(receipt),
            "package":plain(parent.entries[package]),"all_original_members_bytes_SHA_verified":True,
            "nested_bundle_repacked":False}
        return inv
    def resolve(self,row,default=None):
        if row.get("source_group") is not None:
            label=row["source_group"]
            assert label in self.groups,(label,row["file"])
            h=self.groups[label];assert h.entries[row["file"]]==plain(row)
            return h.ref(row)
        name=row["file"]
        if default in self.groups and self.groups[default].entries.get(name)==plain(row):
            return self.groups[default].ref(row)
        hits=[g for g,h in self.groups.items() if h.entries.get(name)==plain(row)]
        if len(hits)>1:
            actual=[g for g in hits if (self.groups[g].folder/name).exists()]
            if len(actual)==1:
                hits=actual
        assert len(hits)==1,("ambiguous_original_plain_reference",name,hits)
        return self.groups[hits[0]].ref(row)
    def stage(self,row,default=None):
        ref=self.resolve(row,default)
        return self.groups[ref["source_group"]].stage(ref),ref
    def close(self):
        for h in self.groups.values():
            h.close()

def function_leaf_selection(R,node,default):
    """Traverse exact global function syntax only; never evaluate or expand its coefficients."""
    op=node["operation"]
    if op.startswith("one_for_"):
        return
    if op=="q_u_over_tau_cubed":
        R.stage(node["source"],default);return
    if op=="external_original_exact_principal_function_DAG":
        value,ref=R.stage(node["source"],default)
        function_leaf_selection(R,value["exact_F_function_DAG"],ref["source_group"]);return
    if op in ("inverse_of_product","multiply","product_of_all_seven_strict_original_constant_field_conjugates"):
        children=node.get("factors")
        if children is None:
            children=[node["left"],node["right"]]
        for child in children:
            function_leaf_selection(R,child,default)
        return
    if op=="integer_power":
        function_leaf_selection(R,node["base"],default);return
    if op=="completed_original_marked_Q_root":
        value,ref=R.stage(node["source"],default)
        b=value["source_actual_marked_pair"] if int(node["sigma_power"]) else value["source_marked_original_pair"]
        R.stage(b,ref["source_group"]);R.stage(value["source_exact_v"],ref["source_group"])
        R.stage(value["source_original_chi_anchor"],ref["source_group"]);return
    if op=="completed_original_K_defined_QK":
        value,ref=R.stage(node["source"],default)
        R.stage(value["source_unscaled_S0"],ref["source_group"])
        R.stage(value["source_unscaled_exact_v"],ref["source_group"])
        return
    raise AssertionError(("unrecognized_original_QZ_operation",op))

def source_pins(item,sources,inputs):
    for group in DIRECT_GROUPS:
        same_source(item["source_artifacts"][group],sources[group])
        assert plain(item["source_artifacts"][group]["certificate"])==plain(sources[group]["certificate"])
    assert set(inputs["directions"])==set(map(str,range(1,6)))
    assert set(inputs["normal_V3_fibres"])==set(inputs["Krylov_points"])==set(inputs["characteristic_nodes"])==set(map(str,range(7)))
    assert inputs["QN_provenance"]["source_R899_identity"]=={k:sources["R899"][k] for k in BASE}
    assert inputs["QN_provenance"]["input_inventory_sha256"]==inputs["R899_original_inventory"]["sha256"]
    assert inputs["completed_artin_fibres"] and all(x["complete"]["source_group"]=="ARTIN" for x in inputs["completed_artin_fibres"])

def source_review(item,retained,sources,inputs):
    source_pins(item,sources,inputs);tags={};certs={}
    for group,source in sources.items():
        folder=Path(retained)/group;entries=entry_map(folder,source)
        for name,row in source["files"].items():
            assert entries[name]==plain(row);bound(folder,row)
        cert,tag,initial=metadata(group,folder,source,entries)
        tags[group]=tag;certs[group]=cert
    def stage(row):
        group=row["source_group"]
        assert sources[group]["files"][row["file"]]==plain(row)
        value=read(bound(Path(retained)/group,row))
        assert value["complete"] is True and value["configuration"]==tags[group]
        return value
    assert certs["R903"]["actual_all_five_original_Iz_128_spaces_certified"] is True
    assert certs["R903"]["actual_all_five_complete_two_chart272_lattices_certified"] is True
    same_source(tags["R903"]["sources"]["R901"],sources["R901"])
    audit=stage(inputs["R899_source_audit"])
    assert audit["inputs"]==inputs["QN_inputs"]
    assert audit["same_original_Galois_orbit_and_all_unscaled_leaves_bound"] is True
    for g,s in tags["R899"]["sources"].items():
        same_source(s,sources[g])
    for key in ("normal_V3_fibres","Krylov_points","characteristic_nodes"):
        for row in inputs[key].values():
            stage(row)
    for j,record in inputs["directions"].items():
        c,b,f,q=(stage(record[k]) for k in ("complete","basis","frame","QZ"))
        assert plain(record["complete"])==plain(certs["R903"]["complete_direction_certificates"][j])
        assert plain(c["complete_original_normal128"])==plain(record["basis"])
        assert plain(c["marked_original_P0_frame_and_embedding"])==plain(record["frame"])
        assert len(b["normal_basis_mod_prime"])==690 and all(len(r)==128 for r in b["normal_basis_mod_prime"])
        assert b["exact_complete_RR_dimension"]==128
        assert b["original_global_multiplier_not_yet_applied_to_normal_arrays"] is True
        assert plain(f["source_original_marked_QZ"])==plain(record["QZ"])
        assert q["actual_QZ_rho_order"]==RHO_ORDERS[int(j)-1]
    assert certs["ARTIN"]["actual_whole_Artin_target_normal_coordinates_certified"] is True
    for record in inputs["completed_artin_fibres"]:
        value=stage(record["complete"])
        assert value["whole_fibre_success"] is True
        for key in ("source_functions","correspondence_algebra","target_normal_row","full_target_equations",
                    "original_reference_value","nine_reference_norms"):
            assert plain(value[key])==plain(record[key]);stage(record[key])
        index=stage(record["target_normal_row"])
        assert [plain(x["source"]) for x in index["blocks"]]==[plain(x) for x in record["target_normal_blocks"]]
        for block in record["target_normal_blocks"]:
            stage(block)
    assert stage(inputs["reference_function"])["actual_reference_basepoint_free_pencil_certified"] is True
    assert "rigidified_Hecke_transport" in stage(inputs["correspondence_DAG"])
    return {"source_file_count":sum(len(x["files"]) for x in sources.values()),
        "source_group_counts":{g:len(x["files"]) for g,x in sources.items()},
        "all_original_bytes_SHA_tags_and_existing_complete_flags_checked":True,
        "all_five_128_spaces_and_same_global_Phi_source_bound":True,
        "R899_QN_original_leaf_inventory_bound":True,
        "completed_target_fibres":[r["ordinal"] for r in inputs["completed_artin_fibres"]],
        "new_mathematics_executed":False}

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R907"
    retained.mkdir(parents=True,exist_ok=True)
    if all((out/n).exists() for n in (BUNDLE,INVENTORY,INPUT_RECEIPT)):
        inv=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inv["result"]==receipt["result"]==RESULT and inv["complete"] is True and receipt["complete"] is True
        assert plain(receipt["source_inventory"])==spec(out/INVENTORY)
        assert plain(receipt["source_bundle"])==spec(out/BUNDLE)
        sources,inputs=inv["sources"],inv["inputs"]
        unpack(out/BUNDLE,retained,sources)
        review=source_review(item,retained,sources,inputs)
        assert receipt["source_identities"]=={g:identity(s) for g,s in sources.items()}
        return retained,sources,inputs,review
    assert allow_download,"R907 same-source complete carrier required for offline verification"
    R=Registry(item,retained,out.parent/"R907-source-download")
    try:
        r903=R.direct("R903");i903=R.carry(r903,"R903")
        # R903 carries the unchanged R901 input package. R901 own new u leaves
        # are selected from its real manifest, rather than re-running any flip.
        r901=R.direct("R901");i901=R.carry(r901,"R901")
        r899=R.direct("R899");i899=R.carry(r899,"R899")
        artin=R.direct("ARTIN");ia=R.carry(artin,"R885-Artin")
        audit_ref=r899.ref(r899.certificate["source_audit"]);audit=r899.stage(audit_ref)
        assert audit["inputs"]==i899["inputs"]
        inputs={"R899_source_audit":audit_ref,"QN_inputs":i899["inputs"],
            "R899_original_inventory":r899.ref("R899-original-source-inventory.json"),
            "QN_provenance":{"source_R899_identity":{k:r899.source[k] for k in BASE},
                "input_inventory_sha256":r899.entries["R899-original-source-inventory.json"]["sha256"],
                "input_receipt":r899.ref("R899-retained-inputs-receipt.json"),
                "historical_verified_original_carrier":R.carriers["R899"]["package"],
                "all_carrier_members_hashed_and_needed_leaves_selected":True},
            "directions":{}}
        qi=inputs["QN_inputs"]
        # Every actual leaf, parent source and recorded complete witness is read
        # as original data. No current group identity is substituted.
        for key in ("marked_QN","original_zero_Qf","original_zero_Qtilde",
                    "original_zero_a_selection","original_zero_a_candidate",
                    "original_zero_v","original_u_C","original_u_chi"):
            R.stage(qi[key])
        for row in qi["original_zero_a_old_fibres"]:
            R.stage(row)
        for row in qi["six_original_branches"]:
            for key in ("principal","a","v"):
                R.stage(row[key])
        for row in qi["two_original_chi_flips"]+qi["new_trace_flips"]:
            for key in ("complete","principal","u"):
                R.stage(row[key])
        inputs["existing_a0_normal_polynomial"]=None
        existing="R899-zero-branch-a-normal-polynomial-from-old-five-fibres.json.gz"
        if existing in r899.entries:
            r899.stage(r899.entries[existing]);inputs["existing_a0_normal_polynomial"]=r899.ref(existing)
        _,inputs["qchi_anchor"]=R.stage(i903["inputs"]["qchi_anchor"])
        _,inputs["t_frame"]=R.stage(i903["inputs"]["t_frame"])
        inputs["normal_V3_fibres"]={str(z):R.stage(row)[1] for z,row in enumerate(i903["inputs"]["R890_normal_fibres"])}
        inputs["Krylov_points"]={str(z):R.stage(row)[1] for z,row in enumerate(i903["inputs"]["original_Krylov_points"])}
        inputs["characteristic_nodes"]={str(z):R.stage(row)[1] for z,row in enumerate(qi["original_characteristic_nodes"])}
        for j in range(1,6):
            complete,c_ref=R.stage(r903.certificate["complete_direction_certificates"][str(j)],"R903")
            basis,b_ref=R.stage(complete["complete_original_normal128"],"R903")
            frame,f_ref=R.stage(complete["marked_original_P0_frame_and_embedding"],"R903")
            qz,q_ref=R.stage(frame["source_original_marked_QZ"],"R901")
            function_leaf_selection(R,qz["exact_QZ_function_DAG"],"R901")
            inputs["directions"][str(j)]={"complete":c_ref,"basis":b_ref,"frame":f_ref,"QZ":q_ref}
        _,inputs["reference_function"]=R.stage(ia["inputs"]["reference_function"])
        _,inputs["correspondence_DAG"]=R.stage(ia["inputs"]["correspondence_DAG"])
        _,inputs["reference_norm_program"]=R.stage(artin.certificate["exact_global_reference_norm_expression_program"],"ARTIN")
        inputs["completed_artin_fibres"]=[]
        for success in artin.certificate["successful_fibre_certificates"]:
            assert success["success"] is True
            c,cref=R.stage(success["certificate"],"ARTIN")
            record={"ordinal":int(c["source_node_ordinal"]),"source_node_value":c["source_node_value"],"complete":cref}
            for key in ("source_functions","correspondence_algebra","target_normal_row","full_target_equations",
                        "original_reference_value","nine_reference_norms"):
                _,record[key]=R.stage(c[key],"ARTIN")
            index=R.groups["ARTIN"].stage(record["target_normal_row"])
            record["target_normal_blocks"]=[R.stage(x["source"],"ARTIN")[1] for x in index["blocks"]]
            inputs["completed_artin_fibres"].append(record)
        assert inputs["completed_artin_fibres"]
        inputs["completed_artin_fibres"].sort(key=lambda x:x["ordinal"])
        sources={g:h.finish() for g,h in R.groups.items()}
        review=source_review(item,retained,sources,inputs)
        save(out/INVENTORY,{"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
            "original_carriers_verified":R.carriers,
            "transports":{g:h.transport() for g,h in R.groups.items() if h.transport()},
            "all_original_source_objects_unmodified":True,
            "no_old_mathematics_rerun":True,"new_mathematics_executed":False})
        pack(retained,sources,out/BUNDLE)
        save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,
            "source_inventory":spec(out/INVENTORY),"source_bundle":spec(out/BUNDLE),
            "source_identities":{g:identity(s) for g,s in sources.items()},
            "selected_file_counts":{g:len(s["files"]) for g,s in sources.items()},
            "all_nested_original_carriers_checked_before_selective_repacking":True,
            "new_mathematics_executed":False})
        print("R907_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,sources,inputs,review
    finally:
        R.close()

def restore(item,out):
    resume=item.get("resume")
    if resume is None:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    root=out.parent/"R907-resume";root.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R907-resume-archive",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],root/MANIFEST,resume.get("manifest_bytes"))
        entries=entry_map(root,resume)
        wanted={BUNDLE,INVENTORY,INPUT_RECEIPT,"public-actions-input.json","run-receipt.json"}
        wanted|=set(META)&set(entries)
        archive.extract_many([(n,entries[n]["sha256"],root/n,entries[n]["bytes"]) for n in sorted(wanted)])
        initial=read(root/"public-actions-input.json");run=read(root/"run-receipt.json")
        assert initial["result"]==run["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]==resume["source_commit"]
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        for key in ("core_sha256","helper_sha256","original_Artin_helper_sha256","method_sha256","proofs"):
            assert initial["job"][key]==item[key]
        assert initial["wrapper_sha256"]==item["wrapper_sha256"]
        inventory=read(root/INVENTORY);receipt=read(root/INPUT_RECEIPT)
        assert inventory["complete"] is True and receipt["complete"] is True
        assert plain(receipt["source_inventory"])==entries[INVENTORY]
        assert plain(receipt["source_bundle"])==entries[BUNDLE]
        sources,inputs=inventory["sources"],inventory["inputs"]
        source_pins(item,sources,inputs)
        tag=expected_tag(item,sources,inputs)
        assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
        if run.get("core_receipt_sha256") is not None:
            assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
            core=read(root/"core-receipt.json")
            assert core["source_sha256"]==item["core_sha256"]
            assert core["helper_sha256"]==item["helper_sha256"]
            if core.get("configuration_sha256") is not None:
                assert core["configuration_sha256"]==fingerprint(tag)
        else:
            assert run["complete"] is False
        for name in (BUNDLE,INVENTORY,INPUT_RECEIPT):
            if (out/name).exists():
                assert spec(out/name)==entries[name]
            else:
                shutil.copy(root/name,out/name)
        stages=[n for n in entries if n.startswith(PREFIX) and n.endswith(".json.gz")]
        archive.extract_many([(n,entries[n]["sha256"],root/n,entries[n]["bytes"]) for n in stages])
        for name in stages:
            value=read(root/name)
            assert value["result"]==RESULT and value["configuration"]==tag
            assert value["complete"] is (False if name==PREFIX+"current.json.gz" else True)
            if (out/name).exists():
                assert spec(out/name)==entries[name]
            else:
                shutil.copy(root/name,out/name)
        old_final=None
        if FINAL in entries:
            archive.extract_bound(FINAL,entries[FINAL]["sha256"],root/FINAL,entries[FINAL]["bytes"])
            old_final=read(root/FINAL)
            assert old_final["result"]==RESULT and old_final["configuration"]==tag
            # An incomplete final records its old inventory/current. It cannot
            # constrain subsequently committed stages or replace the new final.
            if old_final["complete"] is True:
                assert run["complete"] is True and run["process_exit_code"]==0
                for key in ("stage_manifest","resume_state"):
                    assert entries[old_final[key]["file"]]==plain(old_final[key])
                old_manifest=read(root/old_final["stage_manifest"]["file"])
                for row in old_manifest["files"]:
                    assert entries[row["file"]]==plain(row)
        save(out/"resume-import-receipt.json",{"result":RESULT,"complete":True,
            "source":resume,"configuration_sha256":fingerprint(tag),
            "restored_complete_stage_count":len([n for n in stages if n!=PREFIX+"current.json.gz"]),
            "restored_actual_current":entries.get(PREFIX+"current.json.gz"),
            "old_FINAL_complete":old_final["complete"] if old_final else None,
            "old_FINAL_not_reused_as_current_completion":True,
            "source_carrier":entries[BUNDLE],"source_inventory":entries[INVENTORY],
            "Range_receipt":archive.receipt(),"new_mathematics_executed":False})
    finally:
        archive.close()

def output_manifest(out):
    out=Path(out);entries=[]
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in (MANIFEST,REFERENCE):
            continue
        if path.name.endswith((".tmp",".download",".partial")):
            continue
        entries.append(spec(path))
    save(out/MANIFEST,{"result":RESULT,"source_commit":os.environ["GITHUB_SHA"],
        "workflow_run_id":os.environ["GITHUB_RUN_ID"],"files":entries})
    save(out/REFERENCE,{"result":RESULT,**spec(out/MANIFEST)})
    return spec(out/MANIFEST)

def compute(item,out,request):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    code,error,outer_timeout=1,None,False
    try:
        restore(item,out)
        retained,sources,inputs,review=prepare(item,out)
        expanded={**item,"sources":sources,"inputs":inputs}
        save(out/EXPANDED,expanded);tag=expected_tag(item,sources,inputs)
        save(out/"public-actions-input.json",{"result":RESULT,"p":41,
            "source_commit":os.environ["GITHUB_SHA"],"workflow_run_id":os.environ["GITHUB_RUN_ID"],
            "job":item,"core_sha256":item["core_sha256"],"wrapper_sha256":item["wrapper_sha256"],
            "request_sha256":sha(request),"workflow_sha256":sha(REPO/item["workflow"]),
            "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
            "expanded_job":spec(out/EXPANDED),"source_inventory":spec(out/INVENTORY),
            "mathematical_configuration_sha256":fingerprint(tag),
            "source_identities":{g:identity(s) for g,s in sources.items()},"new_mathematics_in_wrapper":False})
        command=[sys.executable,str(S/CORE),"--config",str(out/EXPANDED),
                 "--retained",str(retained),"--output",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"core.log").open("ab") as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                code=process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                outer_timeout=True;os.killpg(process.pid,signal.SIGTERM)
                try:
                    process.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid,signal.SIGKILL);process.wait()
                code=124;error="outer_timeout"
        print((out/"core.log").read_text(errors="replace")[-16000:],flush=True)
        if code==0:
            assert read(out/FINAL)["complete"] is True
    except Exception as exc:
        code=code if code not in (0,1) else 1
        error=type(exc).__name__+": "+str(exc);traceback.print_exc()
    finally:
        save(out/"run-receipt.json",{"result":RESULT,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_sha256":item["core_sha256"],"wrapper_sha256":item["wrapper_sha256"],
            "complete":code==0,"process_exit_code":code,"error":error,"outer_timeout":outer_timeout,
            "execution_environment":"public-repository-github-actions",
            "core_receipt_sha256":sha(out/"core-receipt.json") if (out/"core-receipt.json").exists() else None,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    return code

def refs(value):
    if isinstance(value,dict):
        if {"file","bytes","sha256"}<=set(value):
            yield value;return
        for key,child in value.items():
            if key in ("configuration","historical_verified_original_carrier"):
                continue
            yield from refs(child)
    elif isinstance(value,list):
        for child in value:
            yield from refs(child)

def live_closure(out,entries,tag,sources,roots):
    queue=list(roots);seen={}
    while queue:
        ref=queue.pop();row=plain(ref);group=ref.get("source_group")
        if group not in (None,"R907"):
            assert group in sources and sources[group]["files"][row["file"]]==row
            continue
        if group is None and row["file"] in (INVENTORY,INPUT_RECEIPT,BUNDLE):
            assert entries[row["file"]]==row;continue
        if group is None and not row["file"].startswith(PREFIX):
            matches=[g for g,s in sources.items() if s["files"].get(row["file"])==row]
            assert matches,("missing_original_reference",row["file"])
            continue
        assert row["file"].startswith(PREFIX)
        if row["file"] in seen:
            assert seen[row["file"]]==row;continue
        assert entries[row["file"]]==row
        value=read(bound(out,row))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        seen[row["file"]]=row;queue.extend(refs(value))
    return seen

def verify_complete_final(item,out,entries,tag,cert,sources,inputs):
    completed=cert["complete_direction_certificates"]
    assert sorted(map(int,completed))==cert["actual_completed_directions"]
    assert all(str(j) in completed for j in item["requested_directions"])
    own=lambda row: read(bound(out,row))
    for j in item["requested_directions"]:
        c=own(completed[str(j)])
        assert c["configuration"]==tag and c["complete"] is True and c["original_direction"]==j
        assert c["actual_original672_pencil_certified"] is True
        assert c["actual_nine_norm_values_on_entire_Artin_fibre_computed"] is True
        pencil=own(c["source_complete_basepoint_free_pencil"])
        rank=own(pencil["source_actual672_rank_certificate"])
        assert pencil["actual_pencil_rank"]==rank["actual_rank"]==672
        assert rank["matrix_shape"]==[816,836]
        assert len(rank["selected_original_rows"])==len(set(rank["selected_original_rows"]))==672
        assert len(rank["selected_original_columns"])==len(set(rank["selected_original_columns"]))==672
        assert all(0<=x<816 for x in rank["selected_original_rows"])
        assert all(0<=x<836 for x in rank["selected_original_columns"])
        assert rank["both_unit_inverse_products_verified"] is True
        assert 0<int(rank["actual_unit_minor_determinant_mod_prime"])<P
        assert len(rank["selected_minor_mod_prime"])==len(rank["selected_minor_inverse_mod_prime"])==672
        assert all(len(r)==672 for r in rank["selected_minor_mod_prime"]+rank["selected_minor_inverse_mod_prime"])
        norm=own(c["source_actual_complete_Artin_nine_norms"])
        assert norm["actual_nine_full_A_values_computed"] is True
        assert norm["actual_entire_E_Phi_expression_evaluated"] is True
        assert norm["all_original_expression_denominators_units_on_complete_E"] is True
        assert norm["all_source_factors_and_nilpotents_retained"] is True
        poly=own(norm["source_complete_pencil_norm_polynomial"])
        assert poly["complete_E_T_Cayley_Hamilton_verified"] is True
        assert poly["Cayley_Hamilton_scalar_coordinates_checked"]==19584
        assert len(poly["norm_polynomial_over_A"])==9 and all(len(r)==272 for r in poly["norm_polynomial_over_A"])
        values=own(norm["nine_original_M_section_norms"])
        assert values["parameters"]==list(range(9)) and values["original_Mj_positive_Phi_factor_included"] is True
        assert len(values["nine_norm_values_over_entire_A"])==9
        assert all(len(r)==272 for r in values["nine_norm_values_over_entire_A"])
        assert values["reference_nine_values_recomputed"] is False
        ideal=own(c["complete_two_chart_Hecke_ideal_and_endpoint_expressions"])
        assert set(ideal["complete_original_two_chart_fractional_ideals"])=={"tau","sigma"}
        assert len(ideal["exact_global_nine_generators"])==9
        assert ideal["exact_nine_generators_complete_by_actual_basepoint_free_pencil"] is True
        assert ideal["canonical_dual7_not_replaced_by_self_adjointness"] is True
        assert ideal["original_scalar7_diamond_and_minus3_descent_retained"] is True
        assert set(ideal["two_endpoint_determinant_fibre_expressions"])=={"P0","P1"}
        for point in ("P0","P1"):
            e=ideal["two_endpoint_determinant_fibre_expressions"][point]
            assert e["numeric_endpoint_algebra_and_transition_matrices"] is None
            assert e["numeric_endpoint_calibration_computed"] is False
            assert e["original_source_z0_fibre_substituted_for_endpoint"] is False
        for key in ("P0_endpoint_numeric_calibration_computed","P1_endpoint_numeric_calibration_computed",
                    "endpoint_transition_scalars_set_to_one","modular_zero_used_to_mark_original_eta_inactive",
                    "nonp_terms_Poincare_periods_or_height_computed"):
            assert ideal[key] is False
    closure=live_closure(out,entries,tag,sources,list(completed.values()))
    return {"actual_completed_directions":cert["actual_completed_directions"],
        "complete_own_live_closure_count":len(closure),
        "actual672_full_Artin_nine_norms_and_original_dual7_schema_verified":True,
        "P0_endpoint_numeric_calibration_computed":False,"P1_endpoint_numeric_calibration_computed":False,
        "new_mathematics_executed":False}

def verify(item,out):
    out=Path(out);run=read(out/"run-receipt.json")
    assert run["result"]==RESULT and run["source_commit"]==os.environ["GITHUB_SHA"]
    assert str(run["workflow_run_id"])==os.environ["GITHUB_RUN_ID"]
    assert run["core_sha256"]==item["core_sha256"] and run["wrapper_sha256"]==item["wrapper_sha256"]
    entries=entry_map(out,{"result":RESULT,"manifest_sha256":sha(out/MANIFEST)})
    ref=read(out/REFERENCE);assert ref["result"]==RESULT and plain(ref)==spec(out/MANIFEST)
    for row in entries.values():
        bound(out,row)
    report={"result":RESULT,"complete":True,"run_complete":run["complete"],
        "process_exit_code":run["process_exit_code"],"all_output_bytes_SHA_verified":True,
        "new_mathematics_executed":False}
    if "public-actions-input.json" not in entries:
        assert run["complete"] is False and run["core_receipt_sha256"] is None
        report["stopped_before_core"]=True
    else:
        retained,sources,inputs,review=prepare(item,out,allow_download=False)
        tag=expected_tag(item,sources,inputs);initial=read(out/"public-actions-input.json")
        assert initial["job"]==item and initial["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]
        assert str(initial["workflow_run_id"])==str(run["workflow_run_id"])
        assert initial["core_sha256"]==item["core_sha256"] and initial["wrapper_sha256"]==item["wrapper_sha256"]
        assert plain(initial["expanded_job"])==entries[EXPANDED]
        assert plain(initial["source_inventory"])==entries[INVENTORY]
        expanded=read(out/EXPANDED)
        assert expanded["sources"]==sources and expanded["inputs"]==inputs
        assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
        assert initial["source_identities"]=={g:identity(s) for g,s in sources.items()}
        core=None
        if run.get("core_receipt_sha256") is not None:
            assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
            core=read(out/"core-receipt.json")
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
            assert core["helper_sha256"]==item["helper_sha256"] and core["original_Artin_helper_sha256"]==ARTIN_SHA
            if core.get("configuration_sha256") is not None:
                assert core["configuration_sha256"]==fingerprint(tag)
        for name,row in entries.items():
            if name.startswith(PREFIX) and name.endswith(".json.gz"):
                value=read(bound(out,row))
                assert value["result"]==RESULT and value["configuration"]==tag
                assert value["complete"] is (False if name==PREFIX+"current.json.gz" else True)
        if FINAL in entries:
            cert=read(out/FINAL)
            assert cert["result"]==RESULT and cert["configuration"]==tag
            for key in ("P0_endpoint_numeric_calibration_computed","P1_endpoint_numeric_calibration_computed",
                        "endpoint_transition_scalars_set_to_one","global_Hermite_Picard_inactivity_nonp_terms_or_height_computed"):
                assert cert[key] is False
            if cert["complete"] is True:
                assert run["complete"] is True and run["process_exit_code"]==0 and core is not None and core["complete"] is True
                assert core["certificate_sha256"]==entries[FINAL]["sha256"]
                manifest=read(bound(out,cert["stage_manifest"]))
                assert manifest["configuration"]==tag and manifest["complete"] is True
                actual={n:r for n,r in entries.items() if n.startswith(PREFIX) and n.endswith(".json.gz")
                    and n!=PREFIX+"current.json.gz" and not n.startswith(PREFIX+"stage-manifest-")}
                assert {r["file"]:plain(r) for r in manifest["files"]}==actual
                assert entries[cert["resume_state"]["file"]]==plain(cert["resume_state"])
                report.update(verify_complete_final(item,out,entries,tag,cert,sources,inputs))
            else:
                assert run["complete"] is False
                report["honest_partial_final"]=True
                report["actual_completed_directions"]=cert["actual_completed_directions"]
        else:
            assert run["complete"] is False
        report["source_review"]=review
    save(out/"verification-receipt.json",report);output_manifest(out)
    print("R907_VERIFY="+json.dumps(report,sort_keys=True),flush=True)
    return 0

def main():
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("mode",choices=("compute","verify"))
    parser.add_argument("--request",default=str(REQUEST));parser.add_argument("--output",required=True)
    args=parser.parse_args();request=Path(args.request);item=read(request)
    guard(item,request)
    return compute(item,Path(args.output),request) if args.mode=="compute" else verify(item,Path(args.output))

if __name__=="__main__":
    raise SystemExit(main())

