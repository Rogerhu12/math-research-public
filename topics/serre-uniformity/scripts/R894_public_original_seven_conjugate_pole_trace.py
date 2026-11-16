#!/usr/bin/env python3
"""R894 standard-library transport and verification; no mathematical module import."""
import argparse
import datetime as dt
import importlib.util
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import traceback

S=Path(__file__).resolve().parent
TOPIC=S.parent
REPO=TOPIC.parent.parent
REPOSITORY="Rogerhu12/math-research-public"
RESULT="R894-original-seven-conjugate-pole-trace-bounded-descent"
FINAL="p41-original-seven-conjugate-pole-trace-certificate.json"
PREFIX="R894-"
CORE="R894_original_seven_conjugate_pole_trace.py"
REQUEST=TOPIC/"notes/R894-seven-conjugate-pole-trace-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R894-retained-original-inputs.tar.gz"
INVENTORY="R894-original-source-inventory.json"
INPUT_RECEIPT="R894-retained-inputs-receipt.json"
EXPANDED="R894-expanded-job.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
LEGACY_FILE="R890_original_Ef_eight_flip_and_marked_frame.py"
LEGACY_SHA="da8498fc6ab0f143ba347f4a7dec91c7474bbe2520c349bf33a84bba8e65420f"
LEGACY_IO_FILE="R890_public_original_Ef_eight_flip_and_marked_frame.py"
LEGACY_IO_SHA="5a5e706d11d3b61a6af7acadd4624f7f1e398afe02e6ee77c339fcf7b01f57f1"
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
IO=None

P=1000000753
EPS=[0]+[1]*144+[2]*127
OLD_GROUPS=("R887","R880","R872","R883","R827")
GROUPS=OLD_GROUPS+("R890","SIXD")
CLASS_ORDER=["Cstar-H"]+["sigma^%d(Dstar)-H"%j for j in range(7)]+["Dchi-H"]
TARGET=[-7]+[3]*7+[28]
NEW_CHAIN=(
    ("A1","D0","D1"),("A2","D2","D3"),("A3","A1","A2"),
    ("A4","A3","D4"),("A5","D5","D6"),("A6","A4","A5"),
    ("A7","A6","A6"),("A8","A7","H"),("A9","A8","A6"),
    ("B3","Cstar","H"),("B4","B3","X4"),("B5","B4","B4"),
    ("B6","B5","B5"),("B7","B6","B4"),("B8","B7","B5"),
    ("DN","A9","B8"))
STRATEGY={
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "original_b_branch_order_by_sigma_power":[0,6,1,2,4,3,5],
    "normal_basis_degrees":EPS,"normal_V3_dimension":690,
    "complete_divisor_space_dimension":418,"complete_U_dimension":146,
    "old_fibres":[0,1,2,3,4,5,6],"complete_fibre_length":1904,
    "original_W_Krylov_and_V3_fibres_recomputed":False,
    "legacy_flip_core_sha256":LEGACY_SHA,
    "legacy_flip_algebra_methods_used_without_monkey_patch":True,
    "product_image_rank":962,"membership_shape":[1884,690],
    "complete_relation_shape":[1904,1380],"complete_relation_kernel_dimension":418,
    "product_anchor_schedule":"unchanged ordered original left kernel columns",
    "pencil_schedule":"unchanged positive integer power combinations of complete U146",
    "P0_unit_selection":"unchanged first nonzero column, no scalar rescaling",
    "new_flip_chain":[list(x) for x in NEW_CHAIN],
    "reused_R890_nodes":{"X2":"flip-04-D2","X4":"flip-05-E"},
    "total_mathematical_flip_nodes":18,"new_mathematical_flip_nodes":16,
    "class_coordinate_order":CLASS_ORDER,"target_class_coordinates":TARGET,
    "principal_recurrence":"Fnew=1/(q*Fleft*Fright), repeated factors retained",
    "original_trace":"sum of seven original constant-field conjugate pole divisors",
    "target_identity":"T_f^0=(D_N-H)+div(Q_orbit*F_N), T_f^0=sum sigma^j(E_f)-8442P0",
    "Q_orbit":"product of seven unchanged original Qtilde conjugates",
    "actual_rho_order":-8435,"original_t_leading_exponent":8435,
    "t_power_source":"seventh power of the already certified c^1205",
    "descent_factor":"sigma(Q_N)/Q_N, not its inverse",
    "descent_space_identity":"Q_N*W_DN=H0(2H-T_f^0) tensor_K L",
    "terminal_divisor_or_basis_asserted_K_fixed":False,
    "Hecke_correspondence_norm_computed":False,
    "product_witness_compaction":"selected original 1904x962 product basis, exact column identities and inverse",
    "closed_work_retention":"only remove non-live scan work after complete flip certificate and atomic hash history",
    "active_or_pending_work_discarded":False,
    "only_budget_search_limits_disk_floor_and_transport_excluded_from_identity":True}


def frozen_stdlib_module():
    import hashlib
    path=S/LEGACY_IO_FILE
    assert hashlib.sha256(path.read_bytes()).hexdigest()==LEGACY_IO_SHA
    descriptor=importlib.util.spec_from_file_location("R894_original_R890_stdlib_IO",path)
    module=importlib.util.module_from_spec(descriptor)
    descriptor.loader.exec_module(module)
    return module

L=frozen_stdlib_module()
sha,read,save,fingerprint,plain,spec=L.sha,L.read,L.save,L.fingerprint,L.plain,L.spec
bound,topic_path,identity,group_ref,same_source=L.bound,L.topic_path,L.identity,L.group_ref,L.same_source
entry_map,metadata,dimensions,pack,unpack=L.entry_map,L.metadata,L.dimensions,L.pack,L.unpack

def expected_tag(item,sources,inputs):
    return {"result":RESULT,"source_sha256":item["core_sha256"],
        "python_flint":"0.9.0","p":41,"legacy_flip_core_sha256":LEGACY_SHA,
        "method_sha256":item["method_sha256"],"proofs":item["proofs"],
        "sources":{g:identity(sources[g]) for g in GROUPS},
        "inputs":inputs,"strategy":STRATEGY}

def guard(item,request):
    global IO
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve()
    assert item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False
    assert item["core"]==CORE and sha(S/CORE)==item["core_sha256"]
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["legacy_core"]==LEGACY_FILE and item["legacy_core_sha256"]==LEGACY_SHA
    assert sha(S/LEGACY_FILE)==LEGACY_SHA
    assert item["legacy_io"]==LEGACY_IO_FILE and item["legacy_io_sha256"]==LEGACY_IO_SHA
    assert item["io_helper"]==RANGE_FILE and item["io_helper_sha256"]==RANGE_SHA
    assert 0<item["budget_minutes"]<=300
    assert 1<=item["maximum_pencil_trials"]<=1000
    assert 1<=item["maximum_product_anchors"]<=418
    assert 1<=item["maximum_new_flips"]<=16
    assert item["minimum_free_disk_bytes"]>=256*1024*1024
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert set(item["source_artifacts"])=={"R890","SIXD"}
    assert set(item["prepared_transport"])=={"R890","SIXD"}
    L.load_io();IO=L.IO

class Handle(L.Handle):
    """Keep completed intake bytes; fetch only absent, manifest-pinned old members."""
    def __init__(self,group,item,retained,work):
        self.r894_work=Path(work)
        super().__init__(group,item,retained,work)

    def take(self,names):
        names=sorted(set(names))
        for name in names:
            assert name in self.entries
        missing=[]
        for name in names:
            path=self.folder/name
            if path.exists():
                bound(self.folder,self.entries[name])
            else:
                missing.append(name)
        if missing:
            if self.archive is None:
                self.archive=IO.Archive(self.prior,self.r894_work/("missing-original-"+self.group),whole=False)
            self.archive.extract_many([(n,self.entries[n]["sha256"],self.folder/n,self.entries[n]["bytes"])
                                       for n in missing])
        for name in names:
            bound(self.folder,self.entries[name])
            self.selected[name]=self.entries[name]

    def receipt(self):
        value={"completed_intake":self.transport}
        if self.archive is not None:
            value["additional_original_members"]={"source":self.prior,"range_receipt":self.archive.receipt()}
        return value

def source_pins(item,sources,inputs=None):
    assert set(sources)==set(GROUPS)
    for group in ("R890","SIXD"):
        prior=item["source_artifacts"][group];actual=sources[group]
        same_source(prior,actual)
        assert plain(prior["certificate"])==plain(actual["certificate"])
        assert prior["configuration_sha256"]==actual["configuration_sha256"]
    if inputs is not None:
        old_required={"Cstar","Dstar","Dchi","point_jets","point_linear_functional","Qtilde",
            "t_frame","original_W","original_grid","original_place","original_Krylov_points"}
        new_required={"R890_neutral","R890_normal_fibres","R890_cached_space_fibres",
            "reused_complete_flips","sixD_source_audit","six_Dstar_branches"}
        assert set(inputs)==old_required|new_required
        assert len(inputs["original_Krylov_points"])==len(inputs["R890_normal_fibres"])==7
        assert set(inputs["R890_cached_space_fibres"])=={"H","X4"}
        assert all(len(x)==7 for x in inputs["R890_cached_space_fibres"].values())
        assert set(inputs["reused_complete_flips"])=={"X2","X4"}
        assert [x["sigma_power"] for x in inputs["six_Dstar_branches"]]==[1,2,3,4,5,6]
        assert [x["original_branch"] for x in inputs["six_Dstar_branches"]]==[6,1,2,4,3,5]

def source_review(item,retained,sources,inputs):
    source_pins(item,sources,inputs)
    tags={};certs={};initials={}
    for group in GROUPS:
        source=sources[group];folder=Path(retained)/group
        entries=entry_map(folder,source)
        for name,row in source["files"].items():
            assert entries[name]==plain(row)
            bound(folder,row)
        cert,tag,initial=metadata(group,folder,source,entries)
        tags[group]=tag;certs[group]=cert;initials[group]=initial
    old_sources={g:sources[g] for g in OLD_GROUPS}
    old_inputs=tags["R890"]["inputs"]
    for key,row in old_inputs.items():
        assert inputs[key]==row
    assert {g:identity(old_sources[g]) for g in OLD_GROUPS}==tags["R890"]["sources"]
    old_job=initials["R890"]["job"]
    inherited=L.source_review(old_job,retained,old_sources,old_inputs)
    def stage(row):
        group=row["source_group"];row0=plain(row)
        assert sources[group]["files"][row0["file"]]==row0
        value=read(bound(Path(retained)/group,row0))
        assert value["complete"] is True and value["configuration"]==tags[group]
        return value
    def external(group,row):
        return stage(group_ref(group,row))
    old=certs["R890"]
    assert old["actual_all_eight_complete_normal418_spaces_certified"] is True
    assert old["actual_original_Ef_bounded_divisor_identity_certified"] is True
    assert old["actual_complete_flip_count"]==8
    assert tags["R890"]["source_sha256"]==LEGACY_SHA
    neutral=stage(inputs["R890_neutral"])
    assert neutral["neutral_avoids_original_P0"] is True and neutral["tau_V2_is_complete_W_H"] is True
    assert neutral["source_original_point"]==old_inputs["point_linear_functional"]
    assert neutral["source_original_V2_jets"]==old_inputs["point_jets"]
    dimensions(neutral["neutral_W_H_normal_V3_basis_mod_prime"],690,418)
    assert len(neutral["normal_V3_P0_functional_mod_prime"])==690
    for z,ref in enumerate(inputs["R890_normal_fibres"]):
        value=stage(ref)
        assert value["prime"]==P and value["z0"]==z
        assert plain(value["source_original_Krylov_point"])==plain(inputs["original_Krylov_points"][z])
        assert plain(value["source_original_W"])==plain(inputs["original_W"])
        assert value["normal_integer_scale_applied_again"] is False
        dimensions(value["normal_evaluation_mod_prime"],272,690)
        dimensions(value["cyclic_evaluation_mod_prime"],272,690)
    spaces={}
    for label,index,oldlabel,vector in (("X2",4,"D2",[0,0,-2]),("X4",5,"E",[0,0,4])):
        ref=inputs["reused_complete_flips"][label]
        assert plain(ref) in [plain(x) for x in old["complete_flip_certificates"]]
        complete=stage(ref)
        assert complete["flip_index"]==index and complete["new_space_label"]==oldlabel
        assert complete["actual_product_image_dimension"]==complete["actual_pencil_rank"]==962
        assert complete["actual_U_dimension"]==146 and complete["actual_complete_space_dimension"]==418
        for key in ("all1904_by418_pencil_relations_verified","all1884_by146_membership_relations_verified",
                    "effective_degree272_and_original_P0_avoidance_certified",
                    "complete_characteristic_zero_space_defined_by_original_unit_minors",
                    "original_function_divisor_identity_and_unit_retained"):
            assert complete[key] is True
        space=external("R890",complete["complete_normal418_space"])
        u=external("R890",complete["original_unscaled_P0_unit_section"])
        principal=external("R890",complete["principal_function_and_P0_unit"])
        dimensions(space["normal_V3_basis_mod_prime"],690,418)
        assert space["complete_RR_space_certified"] is True
        assert principal["new_original_class_coefficients"]==vector
        assert principal["class_coordinate_order"]==["Cstar-H","Dstar-H","Dchi-H"]
        assert plain(principal["source_complete_new_normal418"])==plain(complete["complete_normal418_space"])
        assert plain(principal["source_original_unscaled_u"])==plain(complete["original_unscaled_P0_unit_section"])
        assert principal["q_P0_value_mod_prime"]==u["q_P0_value_mod_prime"]
        assert 0<principal["F_P0_value_mod_prime"]<P
        for key in ("F_P0_unit_inverse_product_verified","all_selected_original_scalars_retained"):
            assert principal[key] is True
        assert principal["original_rho_order_of_F"]==0
        assert u["original_scalar_not_rescaled"] is True and u["q_P0_value_is_unit"] is True
        spaces[label]=complete["complete_normal418_space"]
    for label,oldlabel in (("H","H"),("X4","E")):
        for z,ref in enumerate(inputs["R890_cached_space_fibres"][label]):
            value=stage(ref)
            assert value["prime"]==P and value["space"]==oldlabel and value["z0"]==z
            assert plain(value["source_complete_normal_V3_fibre"])==plain(inputs["R890_normal_fibres"][z])
            wanted=inputs["R890_neutral"] if label=="H" else spaces["X4"]
            assert plain(value["source_complete_normal418_space"])==plain(wanted)
            dimensions(value["normal_evaluation_mod_prime"],272,418)
            dimensions(value["cyclic_evaluation_mod_prime"],272,418)
            assert value["all418_original_columns_evaluated"] is True
    six=certs["SIXD"]
    for key in ("all_seven_original_Dstar_inputs_certified","all_six_new_Dstar_418_spaces_certified"):
        assert six[key] is True
    assert six["actual_new_complete_Dstar_count"]==6
    for key,wanted in (("original_branch_zero_Dstar","Dstar"),("original_branch_zero_Qtilde","Qtilde"),
                       ("common_Cstar_418","Cstar"),("common_Dchi_418","Dchi")):
        assert plain(six[key])==plain(inputs[wanted])
    audit=stage(inputs["sixD_source_audit"])
    for key in ("exact_objects_are_conjugates_of_original_characteristic_zero_unit_solves",
                "original_selected_charts_and_all_free_coordinates_unchanged"):
        assert audit[key] is True
    assert audit["original_sigma_powers"]==list(range(1,7))
    assert audit["original_branches"]==[6,1,2,4,3,5]
    for group in ("R827","R872","R880","R887"):
        same_source(audit["source_identities"][group],sources[group])
    for j,row in enumerate(inputs["six_Dstar_branches"],1):
        record=six["completed_new_conjugate_inputs"][j-1]
        assert record["sigma_power"]==row["sigma_power"]==j
        assert record["original_branch"]==row["original_branch"]==[0,6,1,2,4,3,5][j]
        assert plain(record["stage"])==plain(row["complete"])
        complete,basis,principal=[stage(row[k]) for k in ("complete","space","principal")]
        assert complete["roots_B_s"]==principal["roots_B_s"]==record["roots_B_s"]
        assert record["roots_B_s"][1]==99932770
        assert complete["same_original_zero_branch_unit_diagram_conjugated"] is True
        assert complete["complete_original_conjugate_Dstar_418_certified"] is True
        assert plain(complete["complete_Dstar_418_basis"])==plain(row["space"])
        assert plain(complete["original_principal_input"])==plain(row["principal"])
        dimensions(basis["normal_V3_basis_mod_prime"],690,418)
        assert basis["actual_projected_rank"]==418 and basis["complete_RR_space_certified"] is True
        assert plain(principal["source_complete_Dstar"])==plain(row["space"])
        for key,wanted in (("source_complete_common_Cstar","Cstar"),
                           ("source_complete_common_Dchi","Dchi"),("source_original_zero_branch_Qtilde","Qtilde")):
            assert plain(principal[key])==plain(inputs[wanted])
        assert principal["actual_rho_order"]==-1205 and 0<principal["actual_leading_coefficient_mod_prime"]<P
        assert principal["principal_factor_direction"]=="positive multiplication"
        assert principal["exact_original_Galois_conjugate_not_a_new_linearly_equivalent_choice"] is True
        assert principal["all_original_free_coordinates_and_section_scales_preserved"] is True
        for key in ("source_actual_a","source_actual_v"):
            external("SIXD",principal[key])
    return {"result":RESULT,"source_identities":{g:identity(sources[g]) for g in GROUPS},
        "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
        "selected_file_count":sum(len(sources[g]["files"]) for g in GROUPS),
        "inherited_original_five_source_review":inherited,
        "two_complete_R890_chi_flips_reused":True,
        "all_seven_original_Dstar_spaces_same_place_and_fixed_chart":True,
        "seven_normal_V3_and_fourteen_old_H_E_fibre_evaluations_reused":True,
        "no_old_mathematical_stage_recomputed":True,"new_mathematics_executed":False}


def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R894";retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (BUNDLE,INVENTORY,INPUT_RECEIPT)):
        inventory=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        assert plain(receipt["source_inventory"])==spec(out/INVENTORY)
        assert plain(receipt["source_bundle"])==spec(out/BUNDLE)
        sources,inputs=inventory["sources"],inventory["inputs"]
        source_pins(item,sources,inputs)
        unpack(out/BUNDLE,retained,sources)
        review=source_review(item,retained,sources,inputs)
        assert receipt["source_identities"]=={g:identity(sources[g]) for g in GROUPS}
        return retained,sources,inputs,review
    assert allow_download,"Complete bound R894 source carrier is required for offline verification."
    work=out.parent/"R894-download";handles={}
    try:
        for group in ("R890","SIXD"):
            handles[group]=Handle(group,item,retained,work)
        old=handles["R890"];bundle_pins=item["R890_original_carrier"]
        for key in ("source_inventory","retained_inputs_receipt","package"):
            row=plain(bundle_pins[key])
            assert old.entries[row["file"]]==row
            old.take([row["file"]])
        original_inventory=read(old.folder/bundle_pins["source_inventory"]["file"])
        original_receipt=read(old.folder/bundle_pins["retained_inputs_receipt"]["file"])
        assert original_inventory["result"]==original_receipt["result"]==old.prior["result"]
        assert original_inventory["complete"] is True and original_receipt["complete"] is True
        assert plain(original_receipt["source_inventory"])==plain(bundle_pins["source_inventory"])
        assert plain(original_receipt["source_bundle"])==plain(bundle_pins["package"])
        assert plain(old.initial["source_inventory"])==plain(bundle_pins["source_inventory"])
        old_sources=original_inventory["sources"];old_inputs=original_inventory["inputs"]
        assert set(old_sources)==set(OLD_GROUPS)
        assert sum(len(x["files"]) for x in old_sources.values())==bundle_pins["selected_original_member_count"]
        assert {g:identity(old_sources[g]) for g in OLD_GROUPS}==old.tag["sources"]
        assert old_inputs==old.tag["inputs"]
        assert original_receipt["source_identities"]==old.tag["sources"]
        unpack(old.folder/bundle_pins["package"]["file"],retained,old_sources)
        L.original_pins(old.initial["job"],old_sources,old_inputs)
        inputs=dict(old_inputs)
        old.stage(old.certificate["source_audit"])
        old.stage(old.certificate["stage_manifest"])
        neutral_name="R890-neutral-H-and-original-P0-functional.json.gz"
        old.stage(old.entries[neutral_name]);inputs["R890_neutral"]=group_ref("R890",old.entries[neutral_name])
        normal_refs=[]
        for z in range(7):
            name=f"R890-normal-V3-fibre-{z}.json.gz"
            old.stage(old.entries[name]);normal_refs.append(group_ref("R890",old.entries[name]))
        inputs["R890_normal_fibres"]=normal_refs
        reused={}
        for label,stem in (("X2","flip-04-D2"),("X4","flip-05-E")):
            name="R890-"+stem+"-complete-flip-certificate.json.gz"
            candidates=[r for r in old.certificate["complete_flip_certificates"] if r["file"]==name]
            assert len(candidates)==1
            ref=plain(candidates[0]);complete=old.stage(ref)
            for key in ("complete_normal418_space","original_unscaled_P0_unit_section","principal_function_and_P0_unit"):
                old.stage(complete[key])
            reused[label]=group_ref("R890",ref)
        inputs["reused_complete_flips"]=reused
        # These fourteen completed evaluations are not present in the v16 intake.
        # Handle.take fetches only missing original bytes, never reevaluates a fibre.
        cache={}
        for label,old_label in (("H","H"),("X4","E")):
            names=[f"R890-space-{old_label}-fibre-{z}.json.gz" for z in range(7)]
            old.take(names)
            cache[label]=[group_ref("R890",old.entries[n]) for n in names]
            for ref in cache[label]:
                old.stage(ref)
        inputs["R890_cached_space_fibres"]=cache
        six=handles["SIXD"]
        six.stage(six.certificate["source_audit"]);six.stage(six.certificate["stage_manifest"])
        inputs["sixD_source_audit"]=group_ref("SIXD",six.certificate["source_audit"])
        branches=[]
        for record in six.certificate["completed_new_conjugate_inputs"]:
            completed=six.stage(record["stage"])
            for key in ("complete_Dstar_418_basis","original_principal_input","original_a_b_sections","original_v"):
                six.stage(completed[key])
            principal=six.stage(completed["original_principal_input"])
            for key in ("source_actual_a","source_actual_v"):
                six.stage(principal[key])
            branches.append({"sigma_power":record["sigma_power"],"original_branch":record["original_branch"],
                "complete":group_ref("SIXD",record["stage"]),
                "space":group_ref("SIXD",completed["complete_Dstar_418_basis"]),
                "principal":group_ref("SIXD",completed["original_principal_input"])})
        assert [r["sigma_power"] for r in branches]==[1,2,3,4,5,6]
        inputs["six_Dstar_branches"]=branches
        # Retain the old inventory and receipt as provenance; their source package
        # is unpacked and not nested a second time in this new source carrier.
        del old.selected[bundle_pins["package"]["file"]]
        sources=dict(old_sources)
        sources.update({g:h.finish_source() for g,h in handles.items()})
        source_pins(item,sources,inputs)
        review=source_review(item,retained,sources,inputs)
        transports={g:h.receipt() for g,h in handles.items()}
        transports["original_five_groups"]={
            "transport_source":item["source_artifacts"]["R890"],
            "original_inventory":plain(bundle_pins["source_inventory"]),
            "original_receipt":plain(bundle_pins["retained_inputs_receipt"]),
            "original_bundle":plain(bundle_pins["package"]),
            "original_member_count":sum(len(s["files"]) for s in old_sources.values()),
            "all_original_bundle_members_hashed_and_tags_preserved":True,
            "duplicate_nested_source_bundle_not_embedded":True}
        save(out/INVENTORY,{"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
            "transports":transports,"new_mathematics_executed":False})
        pack(retained,sources,out/BUNDLE)
        save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,
            "source_inventory":spec(out/INVENTORY),"source_bundle":spec(out/BUNDLE),
            "source_identities":{g:identity(sources[g]) for g in GROUPS},
            "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
            "all_original_selected_bytes_and_stage_configurations_verified":True,
            "old_mathematics_or_original_fibres_recomputed":False,"new_mathematics_executed":False})
        print("R894_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,sources,inputs,review
    finally:
        for handle in handles.values():
            handle.close()
def restore(item,out):
    resume=item.get("resume")
    if not resume:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R894-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R894-resume-archive",whole=False)
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
        source_pins(item,sources,inputs)
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


def live_refs(value):
    if isinstance(value,dict):
        if {"file","bytes","sha256"}<=set(value):
            yield value
            return
        for key,child in value.items():
            if key in ("configuration","discarded_intermediate_stage_history",
                       "historical_product_work","original_source_provenance"):
                continue
            yield from live_refs(child)
    elif isinstance(value,list):
        for child in value:
            yield from live_refs(child)

def live_closure(out,entries,tag,sources,root):
    todo=[root];seen={}
    while todo:
        ref=todo.pop();row=plain(ref)
        if ref.get("source_group") is not None:
            group=ref["source_group"]
            assert group in sources and sources[group]["files"][row["file"]]==row
            continue
        name=row["file"]
        assert name.startswith(PREFIX),("unqualified_external_reference",name)
        if name in seen:
            assert seen[name]==row
            continue
        assert entries[name]==row
        value=read(bound(out,row))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        seen[name]=row
        todo.extend(live_refs(value))
    return seen

def verify_complete_final(item,out,entries,tag,cert,sources,inputs):
    assert cert["p"]==41 and cert["actual_auxiliary_prime"]==P
    assert cert["actual_new_complete_flip_count"]==16
    assert cert["actual_reused_R890_complete_flip_count"]==2
    assert cert["actual_total_complete_flip_count"]==18
    assert len(cert["complete_new_flip_certificates"])==16
    assert len(cert["closed_work_retention_receipts"])==16
    assert cert["reused_R890_complete_flip_certificates"]==[
        inputs["reused_complete_flips"]["X2"],inputs["reused_complete_flips"]["X4"]]
    for key in ("actual_all_sixteen_new_complete_normal418_spaces_certified",
                "actual_original_seven_pole_trace_bounded_identity_certified",
                "actual_original_t_leading_coefficient_computed",
                "exact_original_Galois_descent_datum_recorded"):
        assert cert[key] is True
    for key in ("terminal_divisor_or_basis_claimed_K_fixed","descent_matrix_or_K_fixed_basis_computed",
                "old_seven_Dstar_Cstar_Dchi_and_R890_two_flips_recomputed",
                "old_W_Krylov_V3_fibres_P0_jets_or_t_constant_recomputed",
                "original_selected_scalars_rescaled_to_one","characteristic_zero_RR_coefficients_reconstructed",
                "Hecke_norm_five_Lj_RR128_RR144_connection_or_height_computed"):
        assert cert[key] is False
    def own(ref):
        row=plain(ref);assert entries[row["file"]]==row
        value=read(bound(out,row))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        return value
    def external(ref):
        group=ref["source_group"];row=plain(ref)
        assert sources[group]["files"][row["file"]]==row
        return read(bound(Path(out).parent/"retained-R894"/group,row))
    audit=own(cert["source_audit"])
    assert audit["sources"]=={g:identity(sources[g]) for g in GROUPS}
    assert audit["inputs"]==inputs and audit["prime"]==P
    assert audit["all_seven_same_original_Galois_Dstar_spaces_bound"] is True
    assert audit["old_W_Krylov_V3_fibres_P0_and_normal_spaces_recomputed"] is False
    assert audit["original_selected_scalars_preserved_without_rescaling"] is True
    assert audit["two_completed_R890_chi_flips_reused"]==cert["reused_R890_complete_flip_certificates"]
    neutral_ref=entries[PREFIX+"neutral-H-and-original-P0-functional.json.gz"]
    neutral=own(neutral_ref)
    assert neutral["source_original_R890_neutral"]==inputs["R890_neutral"]
    assert neutral["old_complete_neutral_space_and_P0_functional_copied_without_arithmetic"] is True
    assert neutral["neutral_avoids_original_P0"] is True and neutral["neutral_degree"]==272
    dimensions(neutral["neutral_W_H_normal_V3_basis_mod_prime"],690,418)
    assert len(neutral["normal_V3_P0_functional_mod_prime"])==690
    spaces={"Cstar":plain(inputs["Cstar"]),"D0":plain(inputs["Dstar"]),"H":plain(neutral_ref)}
    values={"Cstar":1,"D0":1,"H":1}
    for j,row in enumerate(inputs["six_Dstar_branches"],1):
        spaces["D"+str(j)]=plain(row["space"]);values["D"+str(j)]=1
    for label in ("X2","X4"):
        complete=external(inputs["reused_complete_flips"][label])
        spaces[label]=plain(complete["complete_normal418_space"])
        principal=external(group_ref("R890",complete["principal_function_and_P0_unit"]))
        values[label]=principal["F_P0_value_mod_prime"]
    vectors={
        "A1":[0,-1,-1,0,0,0,0,0,0],"A2":[0,0,0,-1,-1,0,0,0,0],
        "A3":[0,1,1,1,1,0,0,0,0],"A4":[0,-1,-1,-1,-1,-1,0,0,0],
        "A5":[0,0,0,0,0,0,-1,-1,0],"A6":[0,1,1,1,1,1,1,1,0],
        "A7":[0,-2,-2,-2,-2,-2,-2,-2,0],"A8":[0,2,2,2,2,2,2,2,0],
        "A9":[0,-3,-3,-3,-3,-3,-3,-3,0],"B3":[-1,0,0,0,0,0,0,0,0],
        "B4":[1,0,0,0,0,0,0,0,-4],"B5":[-2,0,0,0,0,0,0,0,8],
        "B6":[4,0,0,0,0,0,0,0,-16],"B7":[-5,0,0,0,0,0,0,0,20],
        "B8":[7,0,0,0,0,0,0,0,-28],"DN":TARGET}
    last_principal=None;discarded_total=0
    for index,((new,left,right),ref,retention_ref) in enumerate(zip(
            NEW_CHAIN,cert["complete_new_flip_certificates"],cert["closed_work_retention_receipts"]),1):
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
        assert product["matrix_shape"]==[1904,962] and product["actual_product_image_dimension"]==962
        assert plain(product["left_complete_space"])==spaces[left]
        assert plain(product["right_complete_space"])==spaces[right]
        dimensions(product["selected_product_basis_mod_prime"],1904,962)
        dimensions(product["inverse_selected_minor_mod_prime"],962,962)
        assert len(product["selected_rows"])==len(set(product["selected_rows"]))==962
        assert all(0<=r<1904 for r in product["selected_rows"])
        selected=product["selected_original_product_columns_in_order"]
        assert sum(len(x["right_original_kernel_columns"]) for x in selected)==962
        for block in selected:
            assert 0<=block["left_original_kernel_column"]<418
            assert all(0<=c<418 for c in block["right_original_kernel_columns"])
        assert product["source_original_normal_fibres"]==inputs["R890_normal_fibres"]
        assert product["source_original_Krylov_points"]==inputs["original_Krylov_points"]
        assert 1<=product["number_of_original_left_anchors_used"]<=418
        for key in ("both_complete_selected_inverse_products_verified_in_frozen_method",
                    "complete_product_image_is_H0_6H_minus_D1_minus_D2",
                    "all1904_original_fibre_rows_retained",
                    "exact_unit_solve_sources_closed_by_two_complete_parent_spaces"):
            assert product[key] is True
        assert product["already_computed_products_rank_profiles_and_inverses_recomputed"] is False
        assert product["historical_product_work"]["not_a_live_dependency"] is True
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
        for key in ("both_projection_inverse_products_verified","all1904_rows_of_original_relation_verified",
                    "complete_RR_space_certified","D3_effective_degree272_and_avoids_original_P0"):
            assert space[key] is True
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
        assert principal["new_space_label"]==new and principal["class_coordinate_order"]==CLASS_ORDER
        assert principal["left_space_label"]==left and principal["right_space_label"]==right
        assert plain(principal["source_left_complete_space"])==spaces[left]
        assert plain(principal["source_right_complete_space"])==spaces[right]
        assert plain(principal["source_original_unscaled_u"])==plain(flip["original_unscaled_P0_unit_section"])
        assert plain(principal["source_complete_new_normal418"])==plain(flip["complete_normal418_space"])
        assert principal["new_original_class_coefficients"]==vectors[new]
        assert principal["q_P0_value_mod_prime"]==anchor["q_P0_value_mod_prime"]
        assert principal["left_F_P0_value_mod_prime"]==values[left]
        assert principal["right_F_P0_value_mod_prime"]==values[right]
        assert 0<principal["F_P0_value_mod_prime"]<P
        assert principal["F_P0_unit_inverse_product_verified"] is True
        assert principal["all_selected_original_scalars_retained"] is True
        assert principal["original_rho_order_of_F"]==0
        assert principal["exact_F_function_DAG"]["operation"]=="inverse_of_product"
        assert len(principal["exact_F_function_DAG"]["factors"])==3
        assert principal["exact_F_function_DAG"]["repeated_parent_factors_are_retained_twice"] is True
        assert principal["characteristic_zero_function_or_unit_value_expanded"] is False
        spaces[new]=plain(flip["complete_normal418_space"]);values[new]=principal["F_P0_value_mod_prime"]
        last_principal=plain(flip["principal_function_and_P0_unit"])
        retention=own(retention_ref)
        assert plain(retention["complete_flip_certificate"])==plain(ref)
        closure=live_closure(out,entries,tag,sources,ref)
        assert {x["file"]:plain(x) for x in retention["required_live_witness_files"]}==closure
        history=retention["discarded_intermediate_stage_history"]
        assert len(history)==retention["discarded_intermediate_count"]
        assert sum(x["bytes"] for x in history)==retention["discarded_intermediate_bytes"]
        discarded_total+=len(history)
        for row in history:
            row=plain(row)
            assert row["file"].startswith(PREFIX+f"flip-{index:02d}-{new}-")
            assert row["file"] not in entries and row["file"] not in closure
        for key in ("discarded_items_are_hash_history_not_live_references",
                    "all_needed_original_product_column_identities_retained",
                    "complete_selected_product_basis_and_inverse_retained",
                    "full_membership_U146_successful_pencil_kernel_418_and_qF_retained",
                    "cleanup_started_only_after_complete_flip_certificate"):
            assert retention[key] is True
        assert retention["active_or_pending_work_discarded"] is False
    assert cert["historical_discarded_intermediate_stage_count"]==discarded_total
    marked=own(cert["marked_principal_and_descent"])
    assert marked["source_all_new_complete_flips"]==cert["complete_new_flip_certificates"]
    assert marked["source_two_reused_R890_flips"]==cert["reused_R890_complete_flip_certificates"]
    assert plain(marked["source_complete_DN_normal418"])==spaces["DN"]
    assert plain(marked["source_original_t_frame"])==plain(inputs["t_frame"])
    assert marked["class_coordinate_order"]==CLASS_ORDER and marked["target_original_class_coefficients"]==TARGET
    assert marked["exact_original_divisor_identity"]=="T_f^0=(D_N-H)+div(Q_N)"
    assert marked["original_unbased_trace_degree"]==8442 and marked["degree_zero_trace_degree"]==0
    assert marked["original_fractional_ideal_principal_factor_direction"]=="positive multiplication by Q_N"
    assert marked["exact_original_ideal_identity"]=="I_(T_f^0)=Q_N*I_DN*I_H_inverse"
    assert marked["DN_effective_degree"]==272 and marked["DN_avoids_original_P0"] is True
    assert marked["complete_W_DN_dimension"]==418
    assert marked["actual_rho_order"]==marked["actual_Q_orbit_rho_order"]==-8435
    assert marked["actual_terminal_F_P0_unit_mod_prime"]==values["DN"]
    assert marked["actual_original_c_power1205_mod_prime"]==201313487
    for key in ("actual_Q_orbit_rho_leading_mod_prime","actual_QN_rho_leading_mod_prime",
                "actual_original_c_power8435_mod_prime","actual_QN_t_leading_mod_prime"):
        assert 0<marked[key]<P
    original_principals=marked["source_all_seven_original_principals"]
    assert [x["sigma_power"] for x in original_principals]==list(range(7))
    assert [x["original_branch"] for x in original_principals]==[0,6,1,2,4,3,5]
    assert original_principals[0]["source"]==inputs["Qtilde"]
    for j,row in enumerate(inputs["six_Dstar_branches"],1):
        assert original_principals[j]["source"]==row["principal"]
    assert marked["exact_QN_function_DAG"]["operation"]=="multiply"
    assert plain(marked["exact_QN_function_DAG"]["right"]["source"])==last_principal
    assert marked["Q_orbit_fixed_by_original_Gal_L_over_K"] is True
    transition=marked["exact_descent_transition_function_DAG"]
    assert transition["operation"]=="divide"
    assert transition["numerator"]["input"]==transition["denominator"]==marked["exact_QN_function_DAG"]
    assert transition["numerator"]["power"]==1 and transition["numerator"]["Y_normal_generators_fixed"] is True
    assert marked["descent_divisor_identity"]=="div(sigma(Q_N)/Q_N)=D_N-sigma(D_N)"
    assert marked["exact_semilinear_action"]=="s -> (sigma(Q_N)/Q_N)*sigma(s)"
    assert marked["K_descent_identification"]=="Q_N*W_DN=H0(2H-T_f^0) tensor_K L"
    assert marked["all_eighteen_original_unscaled_q_P0_units_preserved"] is True
    for key in ("terminal_DN_or_normal418_basis_claimed_K_fixed",
                "descent_matrix_or_K_fixed_basis_computed","Hecke_correspondence_norm_computed",
                "original_c_or_t_jets_recomputed","auxiliary_units_asserted_to_be_41_adic_units",
                "characteristic_zero_RR_coefficients_or_leading_scalar_expanded",
                "five_original_Lj_RR128_or144_computed","connection_nonp_period_or_height_computed"):
        assert marked[key] is False
    live_closure(out,entries,tag,sources,cert["marked_principal_and_descent"])


def verify(item,out):
    out=Path(out);full=read(out/MANIFEST)
    assert full["result"]==RESULT
    entries={r["file"]:plain(r) for r in full["files"]}
    assert len(entries)==len(full["files"])
    for name,row in entries.items():
        assert name==row["file"];bound(out,row)
    reference=read(out/REFERENCE)
    assert reference["result"]==RESULT and plain(reference)==spec(out/MANIFEST)
    run=read(out/"run-receipt.json")
    assert run["result"]==RESULT and full["source_commit"]==run["source_commit"]
    assert str(full["workflow_run_id"])==str(run["workflow_run_id"])
    assert run["core_sha256"]==item["core_sha256"] and run["wrapper_sha256"]==item["wrapper_sha256"]
    if not all(n in entries for n in ("public-actions-input.json",INVENTORY,INPUT_RECEIPT,BUNDLE)):
        assert run["complete"] is False and run["process_exit_code"]!=0
        return {"result":RESULT,"complete":False,"failure_before_complete_input_carrier":True,
            "process_exit_code":run["process_exit_code"],"error":run["error"],
            "source_manifest":spec(out/MANIFEST),"new_mathematics_executed_in_IO_verification":False}
    retained,sources,inputs,review=prepare(item,out,allow_download=False)
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
    stages={};currents={};inventories={};history_count=0
    for name,row in entries.items():
        if not name.startswith(PREFIX) or not name.endswith(".json.gz"):
            continue
        value=read(out/name)
        assert value["result"]==RESULT and value["configuration"]==tag
        if name==PREFIX+"current.json.gz":
            assert value["complete"] is False;currents[name]=row
        else:
            assert value["complete"] is True
            if name.startswith(PREFIX+"stage-manifest-"):
                inventories[name]=row
                # Older false endpoints can predate a later completed cleanup.
                # Their file list is historical; only the current true final binds
                # a complete inventory of the files that must now be present.
            else:
                stages[name]=row
                if "discarded_intermediate_stage_history" in value:
                    history=value["discarded_intermediate_stage_history"]
                    assert value["discarded_items_are_hash_history_not_live_references"] is True
                    assert value["active_or_pending_work_discarded"] is False
                    assert value["cleanup_started_only_after_complete_flip_certificate"] is True
                    assert value["discarded_intermediate_count"]==len(history)
                    for old in history:
                        assert plain(old)["file"].startswith(PREFIX)
                    history_count+=len(history)
    core=None
    if run["core_receipt_sha256"] is not None:
        assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
        core=read(out/"core-receipt.json")
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
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
            row=plain(cert["stage_manifest"]);assert entries[row["file"]]==row
            inventory=read(bound(out,row))
            assert inventory["result"]==RESULT and inventory["configuration"]==tag
            assert {r["file"]:plain(r) for r in inventory["files"]}==stages
            assert cert["actual_retained_complete_math_stage_count"]==len(stages)
            assert cert["historical_discarded_intermediate_stage_count"]==history_count
            assert inventory["historical_discarded_intermediate_count"]==history_count
            assert inventory["historical_hashes_not_claimed_as_present_files"] is True
            assert inventory["all_required_live_witnesses_and_unclosed_work_retained"] is True
            assert inventory["closed_work_retention_receipts"]==cert["closed_work_retention_receipts"]
            assert plain(cert["resume_state"])==entries[cert["resume_state"]["file"]]
            verify_complete_final(item,out,entries,tag,cert,sources,inputs)
        else:
            assert run["complete"] is False
            # False FINAL is a historical receipt, not a constraint on later current.
    if run["complete"]:
        assert cert is not None and cert["complete"] is True
    return {"result":RESULT,"complete":run["complete"],"process_exit_code":run["process_exit_code"],
        "core_receipt_present":core is not None,"outer_timeout":run["outer_timeout"],
        "source_manifest":spec(out/MANIFEST),"certificate":entries.get(FINAL),
        "actual_retained_complete_stage_count":len(stages),"actual_current_count":len(currents),
        "historical_discarded_intermediate_stage_count":history_count,
        "source_inventory":entries[INVENTORY],"retained_source_bundle":entries[BUNDLE],
        "source_check":review,
        "actual_new_complete_flip_count":cert.get("actual_new_complete_flip_count",0) if cert else 0,
        "actual_reused_R890_complete_flip_count":cert.get("actual_reused_R890_complete_flip_count",0) if cert else 0,
        "complete_new_flip_certificates":cert.get("complete_new_flip_certificates",[]) if cert else [],
        "marked_principal_and_descent":cert.get("marked_principal_and_descent") if cert else None,
        "new_mathematics_executed_in_IO_verification":False}

def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("compute","verify"))
    parser.add_argument("--request",type=Path,default=REQUEST)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();item=read(args.request);guard(item,args.request)
    if args.mode=="verify":
        print("R894_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
        return 0
    code=compute(item,args.output,args.request)
    try:
        print("R894_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
    except Exception:
        traceback.print_exc()
        if code==0:
            code=1
    return code

if __name__=="__main__":
    raise SystemExit(main())






