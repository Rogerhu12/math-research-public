#!/usr/bin/env python3
"""R901 standard-library transport, resume and exact-source/schema verification."""
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
RESULT="R901-original-five-Z-shared-bounded-flip-DAG"
FINAL="p41-original-five-Z-shared-bounded-flip-certificate.json"
PREFIX="R901-"
CORE="R901_original_five_Z_shared_bounded_flips.py"
REQUEST=TOPIC/"notes/R901-five-Z-shared-flips-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R901-retained-original-inputs.tar.gz"
INVENTORY="R901-original-source-inventory.json"
INPUT_RECEIPT="R901-retained-inputs-receipt.json"
EXPANDED="R901-expanded-job.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
LEGACY_FILE="R890_original_Ef_eight_flip_and_marked_frame.py"
LEGACY_SHA="da8498fc6ab0f143ba347f4a7dec91c7474bbe2520c349bf33a84bba8e65420f"
COMPACT_FILE="R894_original_seven_conjugate_pole_trace.py"
COMPACT_SHA="9a2793c79e552c04ea384f5c6bfb673e6e7d506ff91cf9e246fbc00a76f2da56"
LEGACY_IO_FILE="R890_public_original_Ef_eight_flip_and_marked_frame.py"
LEGACY_IO_SHA="5a5e706d11d3b61a6af7acadd4624f7f1e398afe02e6ee77c339fcf7b01f57f1"
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
IO=None

P=1000000753
EPS=[0]+[1]*144+[2]*127
OLD_GROUPS=("R827","R872","R883")
DIRECT_GROUPS=("R890","R896","R900","R902")
GROUPS=OLD_GROUPS+DIRECT_GROUPS
CLASS_ORDER=["Dchi-H","DK-H"]+[
    "sigma^%d(Dstd_%d)-H"%(k,j) for j in range(1,6) for k in range(7)]
POWERS=[12,8,8,13,14]
DEGREES=[2970,1674,1800,3024,3339]
P_NUMERATORS=[165,93,100,168,371]
Q_DENOMINATORS=[67,67,67,67,134]
RHO_ORDERS=[-686,-182,-231,-707,-1659]
BRANCH_ORDER=[0,6,1,2,4,3,5]
STRATEGY={
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "original_b_branch_order_by_sigma_power":BRANCH_ORDER,
    "normal_basis_degrees":EPS,"normal_V3_dimension":690,
    "complete_divisor_space_dimension":418,"complete_U_dimension":146,
    "old_fibres":[0,1,2,3,4,5,6],"complete_fibre_length":1904,
    "legacy_flip_core_sha256":LEGACY_SHA,"compact_flip_core_sha256":COMPACT_SHA,
    "frozen_methods_imported_without_monkey_patch":True,
    "product_image_rank":962,"membership_shape":[1884,690],
    "complete_relation_shape":[1904,1380],"complete_relation_kernel_dimension":418,
    "product_anchor_schedule":"unchanged ordered original left kernel columns",
    "pencil_schedule":"unchanged positive integer power combinations of complete U146",
    "P0_unit_selection":"unchanged first nonzero column; no scalar rescaling",
    "new_flip_count":126,"reused_flip_count":2,
    "original_R890_reused_nodes":{"Xminus2":"flip-04-D2","X4":"flip-05-E"},
    "class_coordinate_order":CLASS_ORDER,
    "original_Hom_words":["1+T^"+str(j) for j in range(1,6)],
    "ordinary_powers":POWERS,"original_pole_degrees":DEGREES,
    "original_p_numerators":P_NUMERATORS,"original_q_denominators":Q_DENOMINATORS,
    "original_QZ_rho_orders":RHO_ORDERS,
    "principal_recurrence":"Fnew=1/(qnew*Fleft*Fright), repeated parents retained twice",
    "terminal_principal":"QZ_j=F_j*(product_k sigma^k(Q_j))^q_j*QK^(-p_j)",
    "equivalent_NormG_qchi_formula_is_audit_only_not_an_additional_factor":True,
    "original_I_Z_identity":"I_Zj=QZ_j*I_DZj*I_H_inverse, positive multiplication",
    "descent_factor":"sigma(QZ_j)/QZ_j",
    "descent_space_identity":"QZ_j*W_DZj=H0(2H-Z_j) tensor_K L",
    "negative_support_of_Zj_not_assumed_to_be_only_P0":True,
    "later_K_evaluation_requires_actual_whole_Artin_denominator_units_and_418_minor":True,
    "terminal_divisor_or_normal_basis_asserted_K_fixed":False,
    "old_W_Krylov_fibres_jets_original_RR_or_two_old_flips_recomputed":False,
    "closed_work_retention":"R894 exact selected product columns, full basis/inverse and live unit-solve closure",
    "only_complete_work_compacted_active_or_pending_work_preserved":True,
    "reference_count_eviction_discards_only_in_memory_matrices_not_live_proof_bytes":True,
    "search_limits_budget_disk_floor_and_transport_excluded_from_mathematical_identity":True}


def frozen_stdlib_module():
    import hashlib
    path=S/LEGACY_IO_FILE
    assert hashlib.sha256(path.read_bytes()).hexdigest()==LEGACY_IO_SHA
    descriptor=importlib.util.spec_from_file_location("R901_original_R890_stdlib_IO",path)
    module=importlib.util.module_from_spec(descriptor);descriptor.loader.exec_module(module)
    return module

L=frozen_stdlib_module()
sha,read,save,fingerprint,plain,spec=L.sha,L.read,L.save,L.fingerprint,L.plain,L.spec
bound,topic_path,identity,group_ref,same_source=L.bound,L.topic_path,L.identity,L.group_ref,L.same_source
entry_map,metadata,dimensions,pack,unpack=L.entry_map,L.metadata,L.dimensions,L.pack,L.unpack

def expected_tag(item,sources,inputs):
    return {"result":RESULT,"source_sha256":item["core_sha256"],
        "python_flint":"0.9.0","p":41,"legacy_flip_core_sha256":LEGACY_SHA,
        "compact_flip_core_sha256":COMPACT_SHA,"method_sha256":item["method_sha256"],
        "proofs":item["proofs"],"fixed_plan_sha256":item["fixed_plan_sha256"],
        "sources":{g:identity(sources[g]) for g in GROUPS},
        "inputs":inputs,"strategy":STRATEGY}

def guard(item,request):
    global IO
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve()
    assert item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False
    for key,expected in (("core",CORE),("wrapper",Path(__file__).name),
            ("legacy_core",LEGACY_FILE),("compact_core",COMPACT_FILE),
            ("legacy_io",LEGACY_IO_FILE),("io_helper",RANGE_FILE)):
        assert item[key]==expected and sha(S/expected)==item[key+"_sha256"]
    assert item["legacy_core_sha256"]==LEGACY_SHA and item["compact_core_sha256"]==COMPACT_SHA
    assert item["legacy_io_sha256"]==LEGACY_IO_SHA and item["io_helper_sha256"]==RANGE_SHA
    assert 0<item["budget_minutes"]<=300
    assert 1<=item["maximum_product_anchors"]<=418
    assert 1<=item["maximum_pencil_trials"]<=1000
    assert 1<=item["maximum_new_flips"]<=126
    assert item["minimum_free_disk_bytes"]>=256*1024*1024
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert sha(topic_path(item["fixed_plan"]))==item["fixed_plan_sha256"]
    plan=read(topic_path(item["fixed_plan"]))
    assert plan["proof"]["sha256"]==item["proofs"]["R901"]["sha256"]
    assert plan["planned_new_flip_count"]==126 and plan["actual_outputs"]["completed_new_flip_count"]==0
    assert set(item["source_artifacts"])==set(DIRECT_GROUPS)
    assert all(item["source_artifacts"][g] is not None for g in DIRECT_GROUPS)
    assert set(item["prepared_transport"])==set(DIRECT_GROUPS)
    L.load_io();IO=L.IO

class Handle(L.Handle):
    """Original intake route plus manifest-bound Range only for absent members."""
    def __init__(self,group,item,retained,work):
        self.r901_work=Path(work)
        super().__init__(group,item,retained,work)

    def take(self,names):
        names=sorted(set(names))
        for name in names:
            assert name in self.entries
        missing=[]
        for name in names:
            if (self.folder/name).exists():
                bound(self.folder,self.entries[name])
            else:
                missing.append(name)
        if missing:
            if self.archive is None:
                self.archive=IO.Archive(self.prior,self.r901_work/("missing-original-"+self.group),whole=False)
            self.archive.extract_many([(n,self.entries[n]["sha256"],self.folder/n,self.entries[n]["bytes"])
                                       for n in missing])
        for name in names:
            bound(self.folder,self.entries[name]);self.selected[name]=self.entries[name]

    def receipt(self):
        value={"completed_intake":self.transport}
        if self.archive is not None:
            value["additional_original_members"]={"source":self.prior,"range_receipt":self.archive.receipt()}
        return value

def source_pins(item,sources,inputs=None):
    assert set(sources)==set(GROUPS)
    for group in DIRECT_GROUPS:
        prior=item["source_artifacts"][group];actual=sources[group]
        same_source(prior,actual)
        assert plain(prior["certificate"])==plain(actual["certificate"])
        assert prior["configuration_sha256"]==actual["configuration_sha256"]
    if inputs is None:
        return
    expected={"Dchi","point_jets","point_linear_functional","t_frame","original_W","original_grid","original_place",
        "original_Krylov_points","R890_neutral","R890_normal_fibres","R890_cached_space_fibres",
        "reused_complete_flips","R896_source_audit","R902_source_audit","R900_source_audit",
        "R900_complete","R900_space","R900_QK","original_orbits"}
    assert set(inputs)==expected
    assert len(inputs["original_Krylov_points"])==len(inputs["R890_normal_fibres"])==7
    assert set(inputs["R890_cached_space_fibres"])=={"H","X4"}
    assert all(len(x)==7 for x in inputs["R890_cached_space_fibres"].values())
    assert set(inputs["reused_complete_flips"])=={"Xminus2","X4"}
    assert len(inputs["original_orbits"])==5
    for j,row in enumerate(inputs["original_orbits"],1):
        assert row["j"]==j and len(row["conjugates"])==7
        for k,entry in enumerate(row["conjugates"]):
            assert entry["sigma_power"]==k and entry["original_branch"]==BRANCH_ORDER[k]
            group="R896" if k==0 else "R902"
            assert all(entry[key]["source_group"]==group for key in ("complete","space","principal"))

def source_review(item,retained,sources,inputs):
    source_pins(item,sources,inputs)
    tags={};certs={};initials={}
    for group in GROUPS:
        source=sources[group];folder=Path(retained)/group
        entries=entry_map(folder,source)
        for name,row in source["files"].items():
            assert entries[name]==plain(row);bound(folder,row)
        cert,tag,initial=metadata(group,folder,source,entries)
        tags[group]=tag;certs[group]=cert;initials[group]=initial
    def stage(row):
        group=row["source_group"];r=plain(row)
        assert sources[group]["files"][r["file"]]==r
        value=read(bound(Path(retained)/group,r))
        assert value["complete"] is True and value["configuration"]==tags[group]
        return value
    original=certs["R890"];old_inputs=tags["R890"]["inputs"]
    assert original["actual_all_eight_complete_normal418_spaces_certified"] is True
    assert original["actual_original_Ef_bounded_divisor_identity_certified"] is True
    assert original["actual_complete_flip_count"]==8 and tags["R890"]["source_sha256"]==LEGACY_SHA
    for group in OLD_GROUPS:
        same_source(tags["R890"]["sources"][group],sources[group])
    for key in ("Dchi","point_jets","point_linear_functional","t_frame",
                "original_W","original_grid","original_place","original_Krylov_points"):
        assert inputs[key]==old_inputs[key]
    neutral=stage(inputs["R890_neutral"])
    assert neutral["neutral_avoids_original_P0"] is True and neutral["tau_V2_is_complete_W_H"] is True
    assert neutral["source_original_point"]==old_inputs["point_linear_functional"]
    assert neutral["source_original_V2_jets"]==old_inputs["point_jets"]
    dimensions(neutral["neutral_W_H_normal_V3_basis_mod_prime"],690,418)
    assert len(neutral["normal_V3_P0_functional_mod_prime"])==690
    chi=stage(inputs["Dchi"])
    dimensions(chi["V3_kernel_basis_mod_prime"],690,418)
    assert chi["full_characteristic_zero_dimension"]==418
    assert chi["all1234_by418_complete_V5_relations_zero"] is True
    assert chi["normal_integer_scale_applied_again"] is False
    frame=stage(inputs["t_frame"])
    assert frame["original_t_first_order_unit_certified"] is True
    assert frame["original_t_over_rho_constant_mod_prime"]==354813668
    assert frame["original_s_root"]==99932770
    for z,ref in enumerate(inputs["original_Krylov_points"]):
        point=stage(ref)
        assert point["prime"]==P and point["z0"]==z and point["usable"] is True
        assert point["actual_cyclic_rank"]==272 and point["both_inverse_products_verified"] is True
        assert plain(point["source_original_W"])==plain(inputs["original_W"])
        fibre=stage(inputs["R890_normal_fibres"][z])
        assert fibre["prime"]==P and fibre["z0"]==z
        assert plain(fibre["source_original_Krylov_point"])==plain(ref)
        assert plain(fibre["source_original_W"])==plain(inputs["original_W"])
        assert fibre["normal_integer_scale_applied_again"] is False
        dimensions(fibre["normal_evaluation_mod_prime"],272,690)
        dimensions(fibre["cyclic_evaluation_mod_prime"],272,690)
    reused={}
    for label,index,oldlabel,coefficient in (("Xminus2",4,"D2",-2),("X4",5,"E",4)):
        ref=inputs["reused_complete_flips"][label]
        assert plain(ref) in [plain(x) for x in original["complete_flip_certificates"]]
        complete=stage(ref)
        assert complete["flip_index"]==index and complete["new_space_label"]==oldlabel
        assert complete["actual_product_image_dimension"]==complete["actual_pencil_rank"]==962
        assert complete["actual_U_dimension"]==146 and complete["actual_complete_space_dimension"]==418
        for key in ("all1904_by418_pencil_relations_verified","all1884_by146_membership_relations_verified",
                    "effective_degree272_and_original_P0_avoidance_certified"):
            assert complete[key] is True
        basis=stage(group_ref("R890",complete["complete_normal418_space"]))
        principal=stage(group_ref("R890",complete["principal_function_and_P0_unit"]))
        u=stage(group_ref("R890",complete["original_unscaled_P0_unit_section"]))
        dimensions(basis["normal_V3_basis_mod_prime"],690,418)
        assert principal["class_coordinate_order"]==["Cstar-H","Dstar-H","Dchi-H"]
        assert principal["new_original_class_coefficients"]==[0,0,coefficient]
        assert principal["F_P0_unit_inverse_product_verified"] is True
        assert principal["all_selected_original_scalars_retained"] is True
        assert principal["original_rho_order_of_F"]==0
        assert 0<principal["F_P0_value_mod_prime"]<P
        assert principal["q_P0_value_mod_prime"]==u["q_P0_value_mod_prime"]
        assert u["q_P0_value_is_unit"] is True and u["original_scalar_not_rescaled"] is True
        reused[label]=complete
    assert plain(reused["Xminus2"]["left_complete_space"])==plain(inputs["Dchi"])
    assert plain(reused["Xminus2"]["right_complete_space"])==plain(inputs["Dchi"])
    assert plain(reused["X4"]["left_complete_space"])==plain(reused["Xminus2"]["complete_normal418_space"])
    assert plain(reused["X4"]["right_complete_space"])==plain(reused["Xminus2"]["complete_normal418_space"])
    for label,refs in inputs["R890_cached_space_fibres"].items():
        for z,ref in enumerate(refs):
            value=stage(ref)
            expected=inputs["R890_neutral"] if label=="H" else reused["X4"]["complete_normal418_space"]
            assert value["prime"]==P and value["z0"]==z
            assert plain(value["source_complete_normal418_space"])==plain(expected)
            assert plain(value["source_complete_normal_V3_fibre"])==plain(inputs["R890_normal_fibres"][z])
            dimensions(value["normal_evaluation_mod_prime"],272,418)
            dimensions(value["cyclic_evaluation_mod_prime"],272,418)
    r900=certs["R900"]
    assert r900["original_K_defined_degree272_representative_certified"] is True
    assert r900["original_K_defined_marked_principal_certified"] is True
    assert plain(r900["complete_K_defined_degree272_certificate"])==plain(inputs["R900_complete"])
    assert plain(r900["marked_original_principal_QK"])==plain(inputs["R900_QK"])
    complete=stage(inputs["R900_complete"]);qk=stage(inputs["R900_QK"]);basis=stage(inputs["R900_space"])
    assert plain(complete["complete_normal418_space"])==plain(inputs["R900_space"])
    assert plain(qk["complete_normal418_space"])==plain(inputs["R900_space"])
    assert qk["QK_defined_over_original_K"] is True and qk["DK_defined_over_original_K"] is True
    assert qk["D0_and_DK_avoid_original_P0"] is True
    assert qk["actual_QK_rho_order"]==qk["actual_QK_t_order"]==-8435
    assert plain(qk["source_original_t_frame"])==plain(inputs["t_frame"])
    assert qk["actual_original_t_over_rho_mod_prime"]==354813668
    assert qk["QK_root"]=="QK" and qk["exact_principal_DAG"]
    assert qk["original_unscaled_sections_and_tau_frames_preserved"] is True
    dimensions(basis["normal_V3_basis_mod_prime"],690,418)
    original=certs["R896"];conjugates=certs["R902"]
    assert original["all_five_complete_low_weight_RR_spaces_certified"] is True
    assert original["completed_directions"]==[1,2,3,4,5]
    assert original["initial_powers"]==POWERS and original["original_pole_degrees"]==DEGREES
    same_source(tags["R902"]["sources"]["R896"],sources["R896"])
    accepted=[]
    for j,orbit in enumerate(inputs["original_orbits"],1):
        zero=orbit["conjugates"][0]
        assert plain(zero["complete"])==plain(original["complete_direction_certificates"][str(j)])
        assert plain(conjugates["original_sigma0_direction_certificates"][str(j)])==plain(zero["complete"])
        for k,entry in enumerate(orbit["conjugates"]):
            complete=stage(entry["complete"]);principal=stage(entry["principal"]);basis=stage(entry["space"])
            assert plain(complete["complete_normal418_space"])==plain(entry["space"])
            assert plain(complete["marked_principal_Q"])==plain(entry["principal"])
            assert plain(principal["complete_normal418_space"])==plain(entry["space"])
            assert principal["prime"]==basis["prime"]==P
            dimensions(basis["normal_V3_basis_mod_prime"],690,418)
            assert principal["actual_Q_rho_order"]==principal["actual_Q_t_order"]==1-DEGREES[j-1]
            assert plain(principal["source_original_t_frame"])==plain(inputs["t_frame"])
            assert principal["actual_original_t_over_rho_mod_prime"]==354813668
            assert 0<principal["actual_Q_rho_leading_mod_prime"]<P
            assert 0<principal["actual_Q_t_leading_mod_prime"]<P
            assert principal["exact_principal_nodes"]
            if k==0:
                for key in ("complete_original_low_weight_RR_and_marked_principal_certified",
                            "true_characteristic_zero_unit_solve_expressions","F0_and_Dstd_avoid_original_P0"):
                    assert complete[key] is True
                assert principal["j"]==j and principal["ordinary_power"]==POWERS[j-1]
                assert principal["original_pole_degree"]==DEGREES[j-1]
                assert principal["original_fixed_chi_sign_is_negative_power_in_Q"] is True
                assert principal["Q_root"]=="Q"
            else:
                assert plain(conjugates["complete_direction_conjugate_certificates"][str(j)][str(k)])==plain(entry["complete"])
                assert principal["original_direction"]==j and principal["sigma_power"]==k
                assert principal["original_branch"]==BRANCH_ORDER[k]
                assert principal["strict_original_selection_and_integer_anchors_preserved"] is True
                assert plain(principal["source_original_sigma0_marked_principal_Q"])==plain(zero["principal"])
                assert principal["exact_principal_root"]
            accepted.append({"j":j,"sigma_power":k,"space":plain(entry["space"]),"principal":plain(entry["principal"])})
    for key in ("R896_source_audit","R900_source_audit","R902_source_audit"):
        stage(inputs[key])
    return {"result":RESULT,"source_groups":list(GROUPS),
        "source_selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
        "all35_original_strict_conjugate_spaces_bound":len(accepted)==35,
        "accepted_original_space_principal_refs":accepted,
        "old_R890_D2_E_accumulated_F_preserved":True,
        "R900_K_defined_representative_and_marked_QK_bound":True,
        "original_auxiliary_prime":P,"original_sigma_branch_order":BRANCH_ORDER,
        "old_W_Krylov_normal_fibres_jets_or_spaces_recomputed":False,
        "new_mathematics_executed":False}

def select_local_function_leaves(handle,value):
    """Keep small original function definitions; completed linear proofs keep original producer identity."""
    selected=[]
    for key in ("source_marked_original_pair","source_exact_v","source_unscaled_S0","source_unscaled_exact_v"):
        row=value.get(key)
        if isinstance(row,dict) and {"file","bytes","sha256"}<=set(row):
            name=row["file"]
            if name in handle.entries and handle.entries[name]==plain(row):
                handle.stage(row);selected.append(plain(row))
    nodes=value.get("exact_principal_nodes",value.get("exact_principal_DAG",[]))
    for node in nodes:
        for key in ("source","source_original_section"):
            row=node.get(key)
            if isinstance(row,dict) and {"file","bytes","sha256"}<=set(row):
                name=row["file"]
                if name in handle.entries and handle.entries[name]==plain(row):
                    handle.stage(row);selected.append(plain(row))
    return list({r["file"]:r for r in selected}.values())

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R901";retained.mkdir(parents=True,exist_ok=True)
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
    assert allow_download,"A complete same-source R901 carrier is required for offline verification."
    work=out.parent/"R901-download";handles={}
    try:
        for group in DIRECT_GROUPS:
            handles[group]=Handle(group,item,retained,work)
        old=handles["R890"];bundle_pins=item["R890_original_carrier"]
        for key in ("source_inventory","retained_inputs_receipt","package"):
            row=plain(bundle_pins[key]);assert old.entries[row["file"]]==row
            old.take([row["file"]])
        original_inventory=read(old.folder/bundle_pins["source_inventory"]["file"])
        original_receipt=read(old.folder/bundle_pins["retained_inputs_receipt"]["file"])
        assert original_inventory["result"]==original_receipt["result"]==old.prior["result"]
        assert original_inventory["complete"] is True and original_receipt["complete"] is True
        assert plain(original_receipt["source_inventory"])==plain(bundle_pins["source_inventory"])
        assert plain(original_receipt["source_bundle"])==plain(bundle_pins["package"])
        assert plain(old.initial["source_inventory"])==plain(bundle_pins["source_inventory"])
        original_sources=original_inventory["sources"];old_inputs=original_inventory["inputs"]
        assert set(original_sources)=={"R887","R880","R872","R883","R827"}
        assert sum(len(x["files"]) for x in original_sources.values())==bundle_pins["selected_original_member_count"]
        assert {g:identity(s) for g,s in original_sources.items()}==old.tag["sources"]
        assert old_inputs==old.tag["inputs"] and original_receipt["source_identities"]==old.tag["sources"]
        # Hash every member of the true 56-file carrier once, then retain only needed old groups.
        unpack(old.folder/bundle_pins["package"]["file"],retained,original_sources)
        sources={g:original_sources[g] for g in OLD_GROUPS}
        keep_keys=("Dchi","point_jets","point_linear_functional","t_frame",
                   "original_W","original_grid","original_place","original_Krylov_points")
        inputs={k:old_inputs[k] for k in keep_keys}
        old.stage(old.certificate["source_audit"]);old.stage(old.certificate["stage_manifest"])
        name="R890-neutral-H-and-original-P0-functional.json.gz"
        old.stage(old.entries[name]);inputs["R890_neutral"]=group_ref("R890",old.entries[name])
        normals=[]
        for z in range(7):
            name=f"R890-normal-V3-fibre-{z}.json.gz"
            old.stage(old.entries[name]);normals.append(group_ref("R890",old.entries[name]))
        inputs["R890_normal_fibres"]=normals
        reused={}
        for label,stem in (("Xminus2","flip-04-D2"),("X4","flip-05-E")):
            name="R890-"+stem+"-complete-flip-certificate.json.gz"
            refs=[r for r in old.certificate["complete_flip_certificates"] if r["file"]==name]
            assert len(refs)==1
            complete=old.stage(refs[0])
            for key in ("complete_normal418_space","original_unscaled_P0_unit_section","principal_function_and_P0_unit"):
                old.stage(complete[key])
            reused[label]=group_ref("R890",refs[0])
        inputs["reused_complete_flips"]=reused
        cache={}
        for label,old_label in (("H","H"),("X4","E")):
            names=[f"R890-space-{old_label}-fibre-{z}.json.gz" for z in range(7)]
            old.take(names);cache[label]=[group_ref("R890",old.entries[n]) for n in names]
            for row in cache[label]:
                old.stage(row)
        inputs["R890_cached_space_fibres"]=cache
        r900=handles["R900"]
        r900.stage(r900.certificate["source_audit"])
        r900.stage(r900.certificate["stage_manifest"])
        inputs["R900_source_audit"]=group_ref("R900",r900.certificate["source_audit"])
        complete_ref=r900.certificate["complete_K_defined_degree272_certificate"]
        complete=r900.stage(complete_ref);r900.stage(complete["complete_normal418_space"])
        principal_ref=r900.certificate["marked_original_principal_QK"]
        qk=r900.stage(principal_ref)
        inputs["R900_complete"]=group_ref("R900",complete_ref)
        inputs["R900_space"]=group_ref("R900",complete["complete_normal418_space"])
        inputs["R900_QK"]=group_ref("R900",principal_ref)
        local_leaves={"R900":select_local_function_leaves(r900,qk),"R896":[],"R902":[]}
        for group in ("R896","R902"):
            handle=handles[group]
            handle.stage(handle.certificate["source_audit"])
            handle.stage(handle.certificate["stage_manifest"])
            inputs[group+"_source_audit"]=group_ref(group,handle.certificate["source_audit"])
        orbits=[]
        for j in range(1,6):
            records=[]
            for k in range(7):
                group="R896" if k==0 else "R902";handle=handles[group]
                if k==0:
                    ref=handle.certificate["complete_direction_certificates"][str(j)]
                else:
                    ref=handle.certificate["complete_direction_conjugate_certificates"][str(j)][str(k)]
                complete=handle.stage(ref)
                sref=complete["complete_normal418_space"];pref=complete["marked_principal_Q"]
                handle.stage(sref);principal=handle.stage(pref)
                local_leaves[group].extend(select_local_function_leaves(handle,principal))
                records.append({"sigma_power":k,"original_branch":BRANCH_ORDER[k],
                    "complete":group_ref(group,ref),"space":group_ref(group,sref),"principal":group_ref(group,pref)})
            orbits.append({"j":j,"conjugates":records})
        inputs["original_orbits"]=orbits
        del old.selected[bundle_pins["package"]["file"]]
        sources.update({g:h.finish_source() for g,h in handles.items()})
        source_pins(item,sources,inputs);review=source_review(item,retained,sources,inputs)
        transports={g:h.receipt() for g,h in handles.items()}
        transports["original_R890_carrier"]={
            "transport_source":item["source_artifacts"]["R890"],
            "original_inventory":plain(bundle_pins["source_inventory"]),
            "original_receipt":plain(bundle_pins["retained_inputs_receipt"]),
            "original_bundle":plain(bundle_pins["package"]),
            "all56_original_members_hashed":True,"retained_old_source_groups":list(OLD_GROUPS),
            "old_R887_R880_not_needed_again_by_new_flip_arithmetic":True,
            "duplicate_nested_source_bundle_not_embedded":True}
        save(out/INVENTORY,{"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
            "selected_function_leaf_files":local_leaves,"transports":transports,
            "all_input_source_identities_preserved":True,"new_mathematics_executed":False})
        pack(retained,sources,out/BUNDLE)
        save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,
            "source_inventory":spec(out/INVENTORY),"source_bundle":spec(out/BUNDLE),
            "source_identities":{g:identity(sources[g]) for g in GROUPS},
            "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
            "all_original_selected_bytes_and_stage_configurations_verified":True,
            "old_mathematics_or_original_fibres_recomputed":False,"new_mathematics_executed":False})
        print("R901_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,sources,inputs,review
    finally:
        for handle in handles.values():
            handle.close()

def restore(item,out):
    resume=item.get("resume")
    if not resume:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R901-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R901-resume-archive",whole=False)
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

def live_closure(out,entries,tag,sources,roots):
    todo=list(roots);seen={}
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
        seen[name]=row;todo.extend(live_refs(value))
    return seen

def verify_complete_final(item,out,entries,tag,cert,sources,inputs):
    plan=read(topic_path(item["fixed_plan"]))
    chain=[(r["id"],r["left"],r["right"]) for r in plan["nodes"]]
    assert len(chain)==126
    assert cert["actual_new_complete_flip_count"]==126
    assert cert["actual_reused_R890_complete_flip_count"]==2
    assert cert["actual_total_complete_flip_count"]==128
    assert cert["completed_directions"]==[1,2,3,4,5]
    assert cert["fixed_plan_sha256"]==item["fixed_plan_sha256"]
    for key in ("actual_all_126_new_complete_normal418_spaces_certified",
                "actual_original_all_five_I_Z_bounded_representatives_certified",
                "actual_original_all_five_t_leading_coefficients_computed",
                "actual_all_five_exact_Galois_descent_data_recorded"):
        assert cert[key] is True
    for key in ("terminal_divisors_or_bases_claimed_K_fixed","descent_matrices_or_K_fixed_bases_computed",
                "old_sources_original_conjugates_or_two_R890_flips_recomputed",
                "original_selected_scalars_rescaled_to_one","characteristic_zero_RR_coordinates_reconstructed",
                "real_descent_cubed_ideal_claimed_equal_to_I_Z",
                "Hecke_norm_RR128_144_connection_period_nonp_or_height_computed"):
        assert cert[key] is False
    def own(ref):
        row=plain(ref);assert entries[row["file"]]==row
        value=read(bound(out,row))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        return value
    def external(ref):
        group=ref["source_group"];row=plain(ref)
        assert sources[group]["files"][row["file"]]==row
        return read(bound(out.parent/"retained-R901"/group,row))
    audit=own(cert["source_audit"])
    assert audit["source_identities"]=={g:identity(sources[g]) for g in GROUPS}
    assert audit["inputs"]==inputs and audit["fixed_plan_sha256"]==item["fixed_plan_sha256"]
    assert audit["all_five_by_seven_original_Dstd_spaces_and_principals_bound"] is True
    assert audit["original_D2_E_accumulated_F_not_reset"] is True
    assert audit["old_W_Krylov_V3_fibres_P0_and_normal_spaces_recomputed"] is False
    assert audit["actual_new_flip_arithmetic_performed_in_source_audit"] is False
    assert len(cert["complete_new_flip_certificates"])==126
    assert len(cert["closed_work_retention_receipts"])==126
    assert cert["reused_R890_complete_flip_certificates"]==[
        inputs["reused_complete_flips"]["Xminus2"],inputs["reused_complete_flips"]["X4"]]
    neutral_ref=entries[PREFIX+"neutral-H-and-original-P0-functional.json.gz"]
    spaces={"H":neutral_ref,"X":inputs["Dchi"],"Tf":inputs["R900_space"]}
    for label in ("Xminus2","X4"):
        old=external(inputs["reused_complete_flips"][label])
        spaces[label]=group_ref("R890",old["complete_normal418_space"])
    for orbit in inputs["original_orbits"]:
        for record in orbit["conjugates"]:
            spaces["D%d_%d"%(orbit["j"],record["sigma_power"])]=record["space"]
    roots=[];discarded_total=0
    for index,((new,left,right),ref,retention_ref) in enumerate(zip(
            chain,cert["complete_new_flip_certificates"],cert["closed_work_retention_receipts"]),1):
        complete=own(ref)
        assert complete["flip_index"]==index and complete["new_space_label"]==new
        assert complete["input_labels"]==[left,right]
        assert complete["left_complete_space"]==spaces[left]
        assert complete["right_complete_space"]==spaces[right]
        assert complete["actual_product_image_dimension"]==complete["actual_pencil_rank"]==962
        assert complete["actual_U_dimension"]==146 and complete["actual_complete_space_dimension"]==418
        for key in ("all1904_by418_pencil_relations_verified","all1884_by146_membership_relations_verified",
                    "effective_degree272_and_original_P0_avoidance_certified",
                    "complete_characteristic_zero_space_defined_by_original_unit_minors",
                    "original_function_divisor_identity_and_unit_retained"):
            assert complete[key] is True
        assert complete["characteristic_zero_arrays_reconstructed"] is False
        product=own(complete["complete_product_image"])
        assert product["left_complete_space"]==spaces[left] and product["right_complete_space"]==spaces[right]
        dimensions(product["selected_product_basis_mod_prime"],1904,962)
        dimensions(product["inverse_selected_minor_mod_prime"],962,962)
        assert len(product["selected_rows"])==962 and len(set(product["selected_rows"]))==962
        definitions=product["selected_original_product_columns_in_order"]
        assert sum(len(row["right_original_kernel_columns"]) for row in definitions)==962
        for row in definitions:
            assert 0<=row["left_original_kernel_column"]<418
            assert all(0<=j<418 for j in row["right_original_kernel_columns"])
        for key in ("both_complete_selected_inverse_products_verified_in_frozen_method",
                    "complete_product_image_is_H0_6H_minus_D1_minus_D2",
                    "all1904_original_fibre_rows_retained",
                    "exact_unit_solve_sources_closed_by_two_complete_parent_spaces"):
            assert product[key] is True
        assert product["already_computed_products_rank_profiles_and_inverses_recomputed"] is False
        assert product["source_original_normal_fibres"]==inputs["R890_normal_fibres"]
        assert product["source_original_Krylov_points"]==inputs["original_Krylov_points"]
        membership=own(complete["complete_membership_matrix"])
        assert membership["source_complete_product_image"]==complete["complete_product_image"]
        assert membership["matrix_shape"]==[1884,690]
        assert membership["membership_anchors"]==["tau^3","sigma^3"]
        assert membership["all_selected_row_residuals_zero"] is True
        dimensions(membership["matrix_mod_prime"],1884,690)
        U=own(complete["complete_U146"])
        assert U["actual_rank"]==544 and U["actual_kernel_dimension"]==146
        assert U["all_original_matrix_rows_times_complete_kernel_zero"] is True
        assert U["free_normalization_identity_verified"] is True
        assert U["both_selected_inverse_products_verified"] is True
        dimensions(U["kernel_basis_mod_prime"],690,146)
        dimensions(U["inverse_selected_minor_mod_prime"],544,544)
        u=own(complete["original_unscaled_P0_unit_section"])
        assert u["source_complete_U146"]==complete["complete_U146"]
        assert u["q_P0_value_is_unit"] is True and u["original_scalar_not_rescaled"] is True
        assert 0<u["q_P0_value_mod_prime"]<P
        assert len(u["normal_V3_coordinates_mod_prime"])==690
        basis=own(complete["complete_normal418_space"])
        dimensions(basis["normal_V3_basis_mod_prime"],690,418)
        assert basis["actual_projected_rank"]==418 and basis["complete_RR_space_certified"] is True
        assert basis["both_projection_inverse_products_verified"] is True
        assert basis["all1904_rows_of_original_relation_verified"] is True
        assert basis["source_original_unscaled_u"]==complete["original_unscaled_P0_unit_section"]
        assert basis["source_complete_U146"]==complete["complete_U146"]
        principal=own(complete["principal_function_and_P0_unit"])
        assert principal["source_complete_new_normal418"]==complete["complete_normal418_space"]
        assert principal["source_original_unscaled_u"]==complete["original_unscaled_P0_unit_section"]
        assert principal["source_left_complete_space"]==spaces[left]
        assert principal["source_right_complete_space"]==spaces[right]
        assert principal["class_coordinate_order"]==CLASS_ORDER
        assert len(principal["new_original_class_coefficients"])==37
        assert principal["F_P0_unit_inverse_product_verified"] is True
        assert principal["all_selected_original_scalars_retained"] is True
        assert principal["original_rho_order_of_F"]==0
        assert principal["q_P0_value_mod_prime"]==u["q_P0_value_mod_prime"]
        assert 0<principal["F_P0_value_mod_prime"]<P
        assert principal["exact_F_function_DAG"]["operation"]=="inverse_of_product"
        assert len(principal["exact_F_function_DAG"]["factors"])==3
        assert principal["exact_F_function_DAG"]["repeated_parent_factors_are_retained_twice"] is True
        retention=own(retention_ref)
        assert retention["complete_flip_certificate"]==ref
        for key in ("discarded_items_are_hash_history_not_live_references",
                    "all_needed_original_product_column_identities_retained",
                    "complete_selected_product_basis_and_inverse_retained",
                    "full_membership_U146_successful_pencil_kernel_418_and_qF_retained",
                    "cleanup_started_only_after_complete_flip_certificate"):
            assert retention[key] is True
        assert retention["active_or_pending_work_discarded"] is False
        keep={r["file"]:plain(r) for r in retention["required_live_witness_files"]}
        assert len(keep)==len(retention["required_live_witness_files"])
        for name,row in keep.items():
            assert entries[name]==row
        history=retention["discarded_intermediate_stage_history"]
        assert len(history)==retention["discarded_intermediate_count"]
        assert sum(r["bytes"] for r in history)==retention["discarded_intermediate_bytes"]
        for row in history:
            assert row["file"].startswith(PREFIX+"flip-%02d-%s-"%(index,new))
            assert row["file"] not in entries and row["file"] not in keep
        discarded_total+=len(history)
        spaces[new]=complete["complete_normal418_space"]
        roots.append(ref)
    assert cert["historical_discarded_intermediate_stage_count"]==discarded_total
    assert set(cert["original_direction_marked_principal_and_descent"])=={"1","2","3","4","5"}
    for j in range(1,6):
        ref=cert["original_direction_marked_principal_and_descent"][str(j)]
        value=own(ref);roots.append(ref)
        assert value["original_direction"]==j and value["original_Hom_word"]=="1+T^"+str(j)
        assert value["original_degree_zero_coefficients"]=={"p":P_NUMERATORS[j-1],"q":Q_DENOMINATORS[j-1]}
        assert value["ordinary_power"]==POWERS[j-1] and value["original_pole_degree"]==DEGREES[j-1]
        assert value["source_complete_DZ_normal418"]==spaces["Z"+str(j)]
        assert value["source_original_QK"]==inputs["R900_QK"]
        assert value["source_original_t_frame"]==inputs["t_frame"]
        assert len(value["source_all_seven_original_Q"])==7
        for k,record in enumerate(value["source_all_seven_original_Q"]):
            assert record["source"]==inputs["original_orbits"][j-1]["conjugates"][k]["principal"]
            assert record["sigma_power"]==k and record["original_branch"]==BRANCH_ORDER[k]
        assert value["actual_QZ_rho_order"]==value["actual_QZ_t_order"]==RHO_ORDERS[j-1]
        assert value["actual_original_c_exponent"]==[686,182,231,707,1659][j-1]
        assert 0<value["actual_QZ_rho_leading_mod_prime"]<P
        assert 0<value["actual_QZ_t_leading_mod_prime"]<P
        assert value["t_leading_agrees_with_product_of_original_t_leading_inputs"] is True
        assert value["principal_factor_direction"]=="positive multiplication"
        assert value["DZ_effective_degree"]==272 and value["DZ_avoids_original_P0"] is True
        assert value["complete_W_DZ_dimension"]==418
        assert value["exact_QZ_function_DAG"]["operation"]=="multiply"
        assert len(value["exact_QZ_function_DAG"]["factors"])==3
        assert value["exact_norm_Qj_function_DAG"]["already_contains_negative_qchi_power"] is True
        assert value["equivalent_formula_not_multiplied_a_second_time"] is True
        assert value["exact_descent_transition_DAG"]["operation"]=="divide"
        for key in ("norm_Qj_fixed_by_original_Gal_L_over_K",
                    "negative_support_not_assumed_to_be_only_P0",
                    "later_K_coordinate_normalization_requires_actual_whole_Artin_units_and_418_minor",
                    "all_original_unscaled_q_and_principal_leading_constants_preserved"):
            assert value[key] is True
        for key in ("terminal_divisor_or_normal_basis_claimed_K_fixed",
                    "old_original_sections_qchi_QK_frames_or_jets_recomputed",
                    "auxiliary_units_claimed_to_be_41_units","real_descent_cube_identified_with_I_Z",
                    "original_Rcal_kappa_theta_torsion_and_nonp_factors_changed",
                    "Hecke_correspondence_norm_or_RR128_144_connection_or_height_computed"):
            assert value[key] is False
    live=live_closure(out,entries,tag,sources,roots)
    return {"complete_flip_count":126,"completed_directions":[1,2,3,4,5],
            "unique_complete_live_witness_files":len(live),"new_mathematics_in_verifier":False}

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
    assert run["result"]==RESULT and run["core_sha256"]==item["core_sha256"]
    assert run["wrapper_sha256"]==item["wrapper_sha256"]
    assert full["source_commit"]==run["source_commit"]
    assert str(full["workflow_run_id"])==str(run["workflow_run_id"])
    if not all(n in entries for n in ("public-actions-input.json",INVENTORY,INPUT_RECEIPT,BUNDLE)):
        assert run["complete"] is False and run["process_exit_code"]!=0
        return {"result":RESULT,"complete":False,"failure_before_complete_input_carrier":True,
            "process_exit_code":run["process_exit_code"],"error":run["error"],
            "source_manifest":spec(out/MANIFEST),"new_mathematics_executed_in_IO_verification":False}
    retained,sources,inputs,source_check=prepare(item,out,allow_download=False)
    tag=expected_tag(item,sources,inputs);initial=read(out/"public-actions-input.json")
    assert initial["result"]==RESULT and initial["source_commit"]==run["source_commit"]
    assert str(initial["workflow_run_id"])==str(run["workflow_run_id"])
    assert initial["core_sha256"]==item["core_sha256"] and initial["wrapper_sha256"]==item["wrapper_sha256"]
    assert initial["job"]==item and initial["mathematical_configuration_sha256"]==fingerprint(tag)
    assert initial["source_inventory"]==entries[INVENTORY] and initial["expanded_job"]==entries[EXPANDED]
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
            assert value["complete"] is False;currents[name]=row
        else:
            assert value["complete"] is True
            if name.startswith(PREFIX+"stage-manifest-"):
                # A previous checkpoint inventory can name later discarded scan work.
                # Only the current successful final's inventory is a current-file assertion.
                inventories[name]=row
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
    certificate=None;complete_review=None
    if FINAL in entries:
        certificate=read(out/FINAL)
        assert certificate["result"]==RESULT and certificate["configuration"]==tag
        if certificate["complete"] is True:
            assert run["complete"] is True and run["process_exit_code"]==0
            assert core is not None and core["complete"] is True
            assert core["certificate_sha256"]==entries[FINAL]["sha256"]
            ref=plain(certificate["stage_manifest"]);assert entries[ref["file"]]==ref
            inventory=read(bound(out,ref))
            assert inventory["result"]==RESULT and inventory["configuration"]==tag
            assert {r["file"]:plain(r) for r in inventory["files"]}==stages
            assert certificate["actual_retained_complete_math_stage_count"]==len(stages)
            assert entries[certificate["resume_state"]["file"]]==plain(certificate["resume_state"])
            complete_review=verify_complete_final(item,out,entries,tag,certificate,sources,inputs)
        else:
            assert run["complete"] is False
    if run["complete"]:
        assert certificate is not None and certificate["complete"] is True
    return {"result":RESULT,"complete":run["complete"],"process_exit_code":run["process_exit_code"],
        "core_receipt_present":core is not None,"outer_timeout":run["outer_timeout"],
        "source_manifest":spec(out/MANIFEST),"certificate":entries.get(FINAL),
        "actual_complete_stage_count":len(stages),"actual_current_count":len(currents),
        "historical_inventory_count":len(inventories),"historical_inventories_not_current_file_constraints":True,
        "source_inventory":entries[INVENTORY],"retained_source_bundle":entries[BUNDLE],
        "source_check":source_check,"complete_endpoint_review":complete_review,
        "actual_new_complete_flip_count":certificate.get("actual_new_complete_flip_count",0) if certificate else 0,
        "completed_directions":certificate.get("completed_directions",[]) if certificate else [],
        "new_mathematics_executed_in_IO_verification":False}

def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("compute","verify"))
    parser.add_argument("--request",type=Path,default=REQUEST)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();item=read(args.request);guard(item,args.request)
    if args.mode=="verify":
        print("R901_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
        return 0
    code=compute(item,args.output,args.request)
    try:
        print("R901_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
    except Exception:
        traceback.print_exc()
        if code==0:
            code=1
    return code

if __name__=="__main__":
    raise SystemExit(main())
