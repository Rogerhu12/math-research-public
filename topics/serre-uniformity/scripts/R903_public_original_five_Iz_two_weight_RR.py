#!/usr/bin/env python3
"""R903 standard-library source transport, resume and completed-output verification."""
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
RESULT="R903-original-five-Iz-two-weight-RR-and-marked-frame"
FINAL="p41-original-five-Iz-two-weight-RR-certificate.json"
PREFIX="R903-"
CORE="R903_original_five_Iz_two_weight_RR.py"
REQUEST=TOPIC/"notes/R903-five-Iz-two-weight-RR-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R903-retained-original-inputs.tar.gz"
INVENTORY="R903-original-source-inventory.json"
INPUT_RECEIPT="R903-retained-inputs-receipt.json"
EXPANDED="R903-expanded-job.json"
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
LEGACY_FILE="R890_original_Ef_eight_flip_and_marked_frame.py"
LEGACY_SHA="da8498fc6ab0f143ba347f4a7dec91c7474bbe2520c349bf33a84bba8e65420f"
COMPACT_FILE="R894_original_seven_conjugate_pole_trace.py"
COMPACT_SHA="9a2793c79e552c04ea384f5c6bfb673e6e7d506ff91cf9e246fbc00a76f2da56"
LEGACY_IO_FILE="R890_public_original_Ef_eight_flip_and_marked_frame.py"
LEGACY_IO_SHA="5a5e706d11d3b61a6af7acadd4624f7f1e398afe02e6ee77c339fcf7b01f57f1"
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
R901_CORE_SHA="2cacb66f8b111746cdb8e51879f1c861e0aa59f0fb15d891c18c3c7c749fc920"
P=1000000753
EPS=[0]+[1]*144+[2]*127
RHO_ORDERS=[-686,-182,-231,-707,-1659]
GROUPS=("R827","R872","R880","R883","R890","R901")
DIRECT_GROUPS=("R890","R872","R880","R901")
IO=None
STRATEGY={
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "normal_basis_degrees":EPS,"original_z_P0_mod_prime":110702704,
    "original_t_over_rho_mod_prime":354813668,
    "original_R901_core_sha256":R901_CORE_SHA,
    "legacy_product_core_sha256":LEGACY_SHA,"compact_product_core_sha256":COMPACT_SHA,
    "frozen_methods_imported_without_monkey_patch":True,
    "original_directions":[1,2,3,4,5],
    "original_line_bundle":"M_j=I_Zj(254P0), not the real-descent cubed ideal",
    "positive_global_multiplier":"Phi_j=QZ_j/qchi",
    "original_qchi_divisor":"Dchi-2H+272P0",
    "old_fibres":[0,1,2,3,4,5,6],"complete_fibre_length":1904,
    "old_V3_dimension":690,"new_V4_dimension":962,
    "single_product_image_dimension":962,"product_quotient_dimension":942,
    "membership_matrix_shapes":{"3":[1884,690],"4":[1884,962]},
    "two_anchor_powers":{"3":3,"4":2},"membership_rank":544,
    "complete_unpadded_dimensions":{"3":146,"4":418},
    "old_jet_orders_used":list(range(19)),"padding_orders":list(range(18)),
    "padded_dimensions":{"3":128,"4":400},
    "weight_one_prefix":"original tau*A128 followed by original sigma*A128",
    "weight_one_prefix_dimension":256,"weight_one_complement_dimension":144,
    "complement_rule":"canonical 400 coordinate rows; keep the original 256 columns and supplement original C columns",
    "complete_two_chart_rank":272,
    "normal_function_coordinates_divided_by_tau_again":False,
    "original_QZ_rho_orders":RHO_ORDERS,
    "selected_P0_column_not_rescaled":True,
    "t_frame_formula":"LCrho(QZ)*a18/LCrho(qchi) * c^(254-ord(QZ))",
    "complete_marked_QZ_source_tree_retained":True,
    "old_sources_W_Krylov_V3_fibres_Hensel_jets_or_126_flips_recomputed":False,
    "closed_product_work_retained_by_selected_columns_and_full_unit_solve":True,
    "split_trial_scope":"only the seven already completed whole fibres; a failed trial is not a negative Picard conclusion",
    "all_new_mathematics_only_in_public_Actions":True,
    "bounds_budget_search_prefix_and_transport_excluded_from_mathematical_identity":True}

def frozen_stdlib_module():
    import hashlib
    path=S/LEGACY_IO_FILE
    assert hashlib.sha256(path.read_bytes()).hexdigest()==LEGACY_IO_SHA
    d=importlib.util.spec_from_file_location("R903_original_R890_stdlib_IO",path)
    module=importlib.util.module_from_spec(d);d.loader.exec_module(module)
    return module

L=frozen_stdlib_module()
sha,read,save,fingerprint,plain,spec=L.sha,L.read,L.save,L.fingerprint,L.plain,L.spec
bound,topic_path,identity,group_ref,same_source=L.bound,L.topic_path,L.identity,L.group_ref,L.same_source
entry_map,metadata,dimensions,pack,unpack=L.entry_map,L.metadata,L.dimensions,L.pack,L.unpack

def expected_tag(item,sources,inputs):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "legacy_product_core_sha256":LEGACY_SHA,"compact_product_core_sha256":COMPACT_SHA,
        "method_sha256":item["method_sha256"],"proofs":item["proofs"],
        "sources":{g:identity(sources[g]) for g in GROUPS},"inputs":inputs,"strategy":STRATEGY}

def guard(item,request):
    global IO
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve()
    assert item["result"]==RESULT and item["p"]==41 and item["producer_inputs_pending"] is False
    for key,name in (("core",CORE),("wrapper",Path(__file__).name),("legacy_core",LEGACY_FILE),
                     ("compact_core",COMPACT_FILE),("legacy_io",LEGACY_IO_FILE),("io_helper",RANGE_FILE)):
        assert item[key]==name and sha(S/name)==item[key+"_sha256"]
    assert item["legacy_core_sha256"]==LEGACY_SHA and item["compact_core_sha256"]==COMPACT_SHA
    assert item["legacy_io_sha256"]==LEGACY_IO_SHA and item["io_helper_sha256"]==RANGE_SHA
    assert 0<item["budget_minutes"]<=300 and 1<=item["maximum_product_anchors"]<=418
    assert 1<=item["maximum_split_fibres"]<=7 and 1<=item["maximum_directions"]<=5
    assert item["minimum_free_disk_bytes"]>=256*1024*1024
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert set(item["source_artifacts"])==set(DIRECT_GROUPS)
    assert all(item["source_artifacts"][g] is not None for g in DIRECT_GROUPS)
    assert set(item["prepared_transport"])==set(DIRECT_GROUPS)
    assert item["source_artifacts"]["R901"]["core_sha256"]==R901_CORE_SHA
    L.load_io();IO=L.IO

class Handle(L.Handle):
    """Reuse a completed original flat intake and Range-fetch only absent members."""
    def __init__(self,group,item,retained,work):
        self.work=Path(work)
        super().__init__(group,item,retained,work)

    def take(self,names):
        names=sorted(set(names));missing=[]
        for name in names:
            assert name in self.entries
            if (self.folder/name).exists():
                bound(self.folder,self.entries[name])
            else:
                missing.append(name)
        if missing:
            if self.archive is None:
                self.archive=IO.Archive(self.prior,self.work/("missing-original-"+self.group),whole=False)
            self.archive.extract_many([(n,self.entries[n]["sha256"],self.folder/n,self.entries[n]["bytes"])
                                       for n in missing])
        for name in names:
            bound(self.folder,self.entries[name]);self.selected[name]=self.entries[name]

    def receipt(self):
        answer={"completed_intake":self.transport}
        if self.archive is not None:
            answer["additional_original_members"]={"source":self.prior,"range_receipt":self.archive.receipt()}
        return answer

def source_pins(item,sources,inputs=None):
    assert set(sources)==set(GROUPS)
    for group in DIRECT_GROUPS:
        prior=item["source_artifacts"][group];actual=sources[group]
        same_source(prior,actual)
        assert plain(prior["certificate"])==plain(actual["certificate"])
        assert prior["configuration_sha256"]==actual["configuration_sha256"]
    if inputs is None:
        return
    required={"Dchi","point_linear_functional","t_frame","original_W","original_grid","original_place",
        "original_Krylov_points","R890_normal_fibres","R890_cached_space_fibres",
        "normal_V3_point_jets","qchi_anchor","fixed_chi_divisor","directions",
        "R901_source_audit","R901_function_provenance"}
    assert set(inputs)==required
    assert len(inputs["original_Krylov_points"])==len(inputs["R890_normal_fibres"])==7
    assert inputs["R890_cached_space_fibres"]=={}
    assert set(inputs["directions"])=={"1","2","3","4","5"}
    for row in inputs["directions"].values():
        assert set(row)=={"space","principal"} and all(x["source_group"]=="R901" for x in row.values())
    for key,row in item["input_pins"].items():
        assert plain(inputs[key])==plain(row) and inputs[key]["source_group"]==row["source_group"]

def source_review(item,retained,sources,inputs):
    source_pins(item,sources,inputs)
    tags={};certs={};initials={}
    for group,source in sources.items():
        folder=Path(retained)/group;entries=entry_map(folder,source)
        for name,row in source["files"].items():
            if name!=REFERENCE:
                assert entries[name]==plain(row)
            bound(folder,row)
        cert,tag,initial=metadata(group,folder,source,entries)
        tags[group]=tag;certs[group]=cert;initials[group]=initial
    def stage(row):
        group=row["source_group"];assert sources[group]["files"][row["file"]]==plain(row)
        value=read(bound(Path(retained)/group,row))
        assert value["configuration"]==tags[group] and value["complete"] is True
        return value
    old=certs["R890"];old_inputs=tags["R890"]["inputs"]
    assert old["actual_all_eight_complete_normal418_spaces_certified"] is True
    for g in ("R827","R872","R883"):
        same_source(tags["R890"]["sources"][g],sources[g])
        same_source(tags["R901"]["sources"][g],sources[g])
    same_source(tags["R901"]["sources"]["R890"],sources["R890"])
    same_source(tags["R880"]["sources"]["R872"],sources["R872"])
    for key in ("Dchi","point_linear_functional","t_frame","original_W",
                "original_grid","original_place","original_Krylov_points"):
        assert inputs[key]==old_inputs[key]
    assert tags["R901"]["source_sha256"]==R901_CORE_SHA
    assert certs["R901"]["actual_new_complete_flip_count"]==126
    assert certs["R901"]["actual_original_all_five_I_Z_bounded_representatives_certified"] is True
    assert certs["R901"]["actual_all_five_exact_Galois_descent_data_recorded"] is True
    W=stage(inputs["original_W"]);place=stage(inputs["original_place"]);grid=stage(inputs["original_grid"])
    assert W["prime"]==place["prime"]==grid["prime"]==P
    assert place["original_zeta_root"]==549966761 and grid["points"]==list(range(8))
    assert grid["all_eight_actual_determinants_nonzero"] is True
    for z,row in enumerate(inputs["original_Krylov_points"]):
        value=stage(row)
        assert plain(row)==plain(grid["Krylov_point_stages"][z])
        assert value["prime"]==P and value["z0"]==z and value["usable"] is True
        assert value["actual_cyclic_rank"]==272 and value["both_inverse_products_verified"] is True
        assert plain(value["source_original_W"])==plain(inputs["original_W"])
    V3=[(i,k) for i in range(272) for k in range(4-EPS[i])]
    for z,row in enumerate(inputs["R890_normal_fibres"]):
        value=stage(row)
        assert value["prime"]==P and value["z0"]==z
        assert value["normal_V3_basis"]==[list(x) for x in V3]
        assert plain(value["source_original_Krylov_point"])==plain(inputs["original_Krylov_points"][z])
        assert plain(value["source_original_W"])==plain(inputs["original_W"])
        assert value["normal_integer_scale_applied_again"] is False
        dimensions(value["normal_evaluation_mod_prime"],272,690)
        dimensions(value["cyclic_evaluation_mod_prime"],272,690)
    point=stage(inputs["point_linear_functional"])
    assert point["chosen_local_parameter"]=="z_minus_z0" and point["z0_mod_prime"]==110702704
    assert point["original_zeta_root"]==549966761
    jets=stage(inputs["normal_V3_point_jets"])
    assert jets["matrix_shape"]==[252,690] and jets["row_orders"]==list(range(252))
    assert jets["V3_basis"]==[{"normal_basis_row":i,"power_of_z":k} for i,k in V3]
    assert jets["local_parameter"]=="z_minus_z0" and jets["no_original_Hensel_step_recomputed"] is True
    dimensions(jets["matrix_mod_prime"],252,690)
    chi=stage(inputs["Dchi"]);anchor=stage(inputs["qchi_anchor"]);fixed=stage(inputs["fixed_chi_divisor"])
    assert chi["full_characteristic_zero_dimension"]==418
    assert chi["all1234_by418_complete_V5_relations_zero"] is True
    assert chi["normal_integer_scale_applied_again"] is False
    dimensions(chi["V3_kernel_basis_mod_prime"],690,418)
    assert plain(certs["R872"]["anchor_u"])==plain(inputs["qchi_anchor"])
    assert plain(certs["R872"]["fixed_chi_divisor_and_principal_function"])==plain(inputs["fixed_chi_divisor"])
    assert plain(fixed["source_exact_u"])==plain(inputs["qchi_anchor"])
    assert plain(fixed["source_complete_W_Dchi"])==plain(inputs["Dchi"])
    assert fixed["D_chi_effective_and_avoids_original_P0"] is True
    assert fixed["principal_function"]["tau_power"]==2
    assert fixed["principal_function"]["no_additional_scalar_or_82_power"] is True
    assert anchor["role"]=="u" and anchor["order272_is_exact"] is True
    assert anchor["vanishes_at_original_P0_to_order_at_least272"] is True
    assert 0<anchor["exact_order272_unit"]<P
    frame=stage(inputs["t_frame"])
    assert frame["original_t_first_order_unit_certified"] is True
    assert frame["original_s_root"]==99932770
    assert frame["original_t_over_rho_constant_mod_prime"]==354813668
    stage(inputs["R901_source_audit"])
    for j in range(1,6):
        r=inputs["directions"][str(j)]
        assert plain(certs["R901"]["original_direction_marked_principal_and_descent"][str(j)])==plain(r["principal"])
        qz=stage(r["principal"]);basis=stage(r["space"])
        assert qz["original_direction"]==j and qz["prime"]==P
        assert plain(qz["source_complete_DZ_normal418"])==plain(r["space"])
        assert qz["DZ_effective_degree"]==272 and qz["DZ_avoids_original_P0"] is True
        assert qz["actual_QZ_rho_order"]==qz["actual_QZ_t_order"]==RHO_ORDERS[j-1]
        assert qz["principal_factor_direction"]=="positive multiplication"
        assert qz["negative_support_not_assumed_to_be_only_P0"] is True
        assert qz["terminal_divisor_or_normal_basis_claimed_K_fixed"] is False
        assert plain(qz["source_original_t_frame"])==plain(inputs["t_frame"])
        assert 0<qz["actual_QZ_rho_leading_mod_prime"]<P and 0<qz["actual_QZ_t_leading_mod_prime"]<P
        assert basis["complete_RR_space_certified"] is True and basis["actual_projected_rank"]==418
        assert basis["all1904_rows_of_original_relation_verified"] is True
        assert basis["D3_effective_degree272_and_avoids_original_P0"] is True
        dimensions(basis["normal_V3_basis_mod_prime"],690,418)
    provenance=inputs["R901_function_provenance"]
    assert set(provenance)=={"original_source_inventory","original_retained_inputs_receipt","opaque_original_source_bundle"}
    for row in provenance.values():
        assert row["source_group"]=="R901" and sources["R901"]["files"][row["file"]]==plain(row)
    folder=Path(retained)/"R901"
    inv=read(bound(folder,provenance["original_source_inventory"]))
    receipt=read(bound(folder,provenance["original_retained_inputs_receipt"]))
    assert inv["result"]==receipt["result"]==sources["R901"]["result"]
    assert inv["complete"] is True and receipt["complete"] is True
    assert plain(receipt["source_inventory"])==plain(provenance["original_source_inventory"])
    assert plain(receipt["source_bundle"])==plain(provenance["opaque_original_source_bundle"])
    assert plain(initials["R901"]["source_inventory"])==plain(provenance["original_source_inventory"])
    assert receipt["source_identities"]=={g:identity(s) for g,s in inv["sources"].items()}==tags["R901"]["sources"]
    assert inv["inputs"]==tags["R901"]["inputs"]
    return {"result":RESULT,"source_identities":{g:identity(sources[g]) for g in GROUPS},
        "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
        "selected_file_count":sum(len(s["files"]) for s in sources.values()),
        "five_original_complete418_and_marked_QZ_bound":True,
        "R872_qchi_order272_and_unchanged_scalar_bound":True,
        "old_complete_normal_fibres_and_R880_nineteen_of_252_jets_bound":True,
        "R901_complete_nested_global_function_provenance_preserved_as_original_bytes":True,
        "R901_nested_source_carrier_rehashed":True,
        "old_mathematics_recomputed":False,"new_mathematics_executed":False}

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R903";retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (BUNDLE,INVENTORY,INPUT_RECEIPT)):
        inv=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inv["result"]==receipt["result"]==RESULT and inv["complete"] is True and receipt["complete"] is True
        assert plain(receipt["source_inventory"])==spec(out/INVENTORY)
        assert plain(receipt["source_bundle"])==spec(out/BUNDLE)
        sources,inputs=inv["sources"],inv["inputs"];source_pins(item,sources,inputs)
        unpack(out/BUNDLE,retained,sources)
        review=source_review(item,retained,sources,inputs)
        assert receipt["source_identities"]=={g:identity(sources[g]) for g in GROUPS}
        return retained,sources,inputs,review
    assert allow_download,"Complete same-source R903 retained carrier required for offline verification."
    work=out.parent/"R903-download";handles={}
    try:
        old=Handle("R890",item,retained,work);handles["R890"]=old
        pins=item["R890_original_carrier"]
        for key in ("source_inventory","retained_inputs_receipt","package"):
            row=plain(pins[key]);assert old.entries[row["file"]]==row;old.take([row["file"]])
        original_inv=read(old.folder/pins["source_inventory"]["file"])
        original_receipt=read(old.folder/pins["retained_inputs_receipt"]["file"])
        assert original_inv["complete"] is True and original_receipt["complete"] is True
        assert plain(original_receipt["source_inventory"])==plain(pins["source_inventory"])
        assert plain(original_receipt["source_bundle"])==plain(pins["package"])
        originals=original_inv["sources"];old_inputs=original_inv["inputs"]
        assert set(originals)=={"R887","R880","R872","R883","R827"}
        assert sum(len(s["files"]) for s in originals.values())==pins["selected_original_member_count"]
        assert {g:identity(s) for g,s in originals.items()}==old.tag["sources"]
        assert original_receipt["source_identities"]==old.tag["sources"] and old_inputs==old.tag["inputs"]
        unpack(old.folder/pins["package"]["file"],retained,originals)
        sources={g:originals[g] for g in ("R827","R883")}
        keep=("Dchi","point_linear_functional","t_frame","original_W","original_grid","original_place","original_Krylov_points")
        inputs={k:old_inputs[k] for k in keep}
        old.stage(old.certificate["source_audit"])
        inputs["R890_normal_fibres"]=[]
        for z in range(7):
            row=old.entries[f"R890-normal-V3-fibre-{z}.json.gz"];old.stage(row)
            inputs["R890_normal_fibres"].append(group_ref("R890",row))
        inputs["R890_cached_space_fibres"]={}
        for group in ("R872","R880","R901"):
            handles[group]=Handle(group,item,retained,work)
        r872=handles["R872"];r880=handles["R880"];r901=handles["R901"]
        for key in ("Dchi","point_linear_functional"):
            r872.stage(inputs[key])
        inputs["qchi_anchor"]=group_ref("R872",r872.certificate["anchor_u"])
        inputs["fixed_chi_divisor"]=group_ref("R872",r872.certificate["fixed_chi_divisor_and_principal_function"])
        r872.stage(inputs["qchi_anchor"]);r872.stage(inputs["fixed_chi_divisor"])
        inputs["normal_V3_point_jets"]=dict(item["input_pins"]["normal_V3_point_jets"])
        r880.stage(inputs["normal_V3_point_jets"])
        inputs["R901_source_audit"]=group_ref("R901",r901.certificate["source_audit"])
        r901.stage(inputs["R901_source_audit"])
        inputs["directions"]={}
        for j in range(1,6):
            qref=r901.certificate["original_direction_marked_principal_and_descent"][str(j)]
            qz=r901.stage(qref);sref=qz["source_complete_DZ_normal418"];r901.stage(sref)
            inputs["directions"][str(j)]={"principal":group_ref("R901",qref),"space":group_ref("R901",sref)}
        names={"original_source_inventory":"R901-original-source-inventory.json",
               "original_retained_inputs_receipt":"R901-retained-inputs-receipt.json",
               "opaque_original_source_bundle":"R901-retained-original-inputs.tar.gz"}
        r901.take(list(names.values()))
        inputs["R901_function_provenance"]={key:group_ref("R901",r901.entries[name]) for key,name in names.items()}
        # The old 56-file transport has been fully checked and its needed groups extracted.
        # It is not retained as a second live copy inside R890 selected outputs.
        for key in ("source_inventory","retained_inputs_receipt","package"):
            name=pins[key]["file"];old.selected.pop(name,None)
        for group,handle in handles.items():
            sources[group]=handle.finish_source()
        source_pins(item,sources,inputs)
        review=source_review(item,retained,sources,inputs)
        inv={"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
             "transport_receipts":{g:h.receipt() for g,h in handles.items()},
             "original_R890_carrier":{"source":item["source_artifacts"]["R890"],**pins},
             "all_selected_original_members_bound":True,"new_mathematics_executed":False}
        save(out/INVENTORY,inv);pack(retained,sources,out/BUNDLE)
        save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,"source_inventory":spec(out/INVENTORY),
            "source_bundle":spec(out/BUNDLE),"source_identities":{g:identity(sources[g]) for g in GROUPS},
            "selected_file_counts":{g:len(sources[g]["files"]) for g in GROUPS},
            "all_original_selected_bytes_and_stage_configurations_verified":True,
            "old_mathematics_recomputed":False,"new_mathematics_executed":False})
        print("R903_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,sources,inputs,review
    finally:
        for h in handles.values():
            h.close()

def restore(item,out):
    resume=item.get("resume")
    if not resume:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R903-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R903-resume-archive",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],directory/MANIFEST,resume.get("manifest_bytes"))
        entries=entry_map(directory,resume)
        names=(set(META)&set(entries))|{BUNDLE,INVENTORY,INPUT_RECEIPT}
        archive.extract_many([(n,entries[n]["sha256"],directory/n,entries[n]["bytes"]) for n in sorted(names)])
        initial=read(directory/"public-actions-input.json");run=read(directory/"run-receipt.json")
        assert initial["result"]==run["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]==resume["source_commit"]
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        assert initial["core_sha256"]==item["core_sha256"]
        assert initial["wrapper_sha256"]==item["wrapper_sha256"]
        for key in ("proofs","method_sha256"):
            assert initial["job"][key]==item[key]
        core=None
        if run.get("core_receipt_sha256") is not None:
            assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
            core=read(directory/"core-receipt.json")
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        else:
            assert run["complete"] is False
        inv=read(directory/INVENTORY);receipt=read(directory/INPUT_RECEIPT)
        assert plain(receipt["source_inventory"])==entries[INVENTORY]
        assert plain(receipt["source_bundle"])==entries[BUNDLE]
        sources,inputs=inv["sources"],inv["inputs"];source_pins(item,sources,inputs)
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
                sm=read(bound(directory,cert["stage_manifest"]))
                for row in sm["files"]:
                    assert entries[row["file"]]==plain(row)
                assert entries[cert["resume_state"]["file"]]==plain(cert["resume_state"])
                shutil.copyfile(directory/FINAL,out/FINAL)
        save(out/"resume-import-receipt.json",{
            "result":RESULT,"complete":True,"source":resume,"original_manifest":spec(directory/MANIFEST),
            "mathematical_configuration_sha256":fingerprint(tag),"restored_stage_count":len(stages),
            "same_new_core_and_all_original_sources_preserved":True,
            "false_historical_FINAL_and_inventory_do_not_constrain_later_live_files":True,
            "missing_core_receipt_honestly_retained":core is None,"range_transport":archive.receipt()})
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
    out=Path(out);out.mkdir(parents=True,exist_ok=True);code,error,outer=1,None,False
    try:
        restore(item,out)
        retained,sources,inputs,review=prepare(item,out)
        expanded={**item,"sources":sources,"inputs":inputs};save(out/EXPANDED,expanded)
        tag=expected_tag(item,sources,inputs)
        save(out/"public-actions-input.json",{
            "result":RESULT,"p":41,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"job":item,
            "core_sha256":item["core_sha256"],"wrapper_sha256":item["wrapper_sha256"],
            "request_sha256":sha(request),"workflow_sha256":sha(REPO/item["workflow"]),
            "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
            "expanded_job":spec(out/EXPANDED),"source_inventory":spec(out/INVENTORY),
            "mathematical_configuration_sha256":fingerprint(tag),
            "source_identities":{g:identity(sources[g]) for g in GROUPS},"new_mathematics_in_wrapper":False})
        command=[sys.executable,str(S/CORE),"--config",str(out/EXPANDED),"--retained",str(retained),
                 "--output",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"core.log").open("ab") as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                code=process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                outer=True;os.killpg(process.pid,signal.SIGTERM)
                try:
                    process.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid,signal.SIGKILL);process.wait()
                code=124;error="outer_timeout"
        if code==0:
            assert read(out/FINAL)["complete"] is True
        print((out/"core.log").read_text(errors="replace")[-16000:],flush=True)
    except Exception as exc:
        error=type(exc).__name__+": "+str(exc);traceback.print_exc()
        if code==0:
            code=1
    finally:
        save(out/"run-receipt.json",{
            "result":RESULT,"source_commit":os.environ["GITHUB_SHA"],"workflow_run_id":os.environ["GITHUB_RUN_ID"],
            "workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_sha256":item["core_sha256"],"wrapper_sha256":item["wrapper_sha256"],
            "complete":code==0,"process_exit_code":code,"error":error,"outer_timeout":outer,
            "execution_environment":"public-repository-github-actions",
            "core_receipt_sha256":sha(out/"core-receipt.json") if (out/"core-receipt.json").exists() else None,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    return code

def live_refs(value):
    if isinstance(value,dict):
        if {"file","bytes","sha256"}<=set(value):
            yield value;return
        for key,child in value.items():
            if key in ("configuration","discarded_intermediate_stage_history","historical_product_work","original_source_provenance"):
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
            assert sources[ref["source_group"]]["files"][row["file"]]==row
            continue
        name=row["file"];assert name.startswith(PREFIX)
        if name in seen:
            assert seen[name]==row;continue
        assert entries[name]==row
        value=read(bound(out,row))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        seen[name]=row;todo.extend(live_refs(value))
    return seen

def verify_complete_final(item,out,entries,tag,cert,sources,inputs):
    assert cert["completed_directions"]==[1,2,3,4,5]
    for flag in ("actual_all_five_original_Iz_128_spaces_certified",
                 "actual_all_five_original_weight1_400_spaces_certified",
                 "actual_all_five_original144_complements_certified",
                 "actual_all_five_complete_two_chart272_lattices_certified",
                 "actual_all_five_original_P0_frame_coefficients_certified"):
        assert cert[flag] is True
    for flag in ("original_Hensel_W_Krylov_V3_fibres_R901_flips_recomputed",
                 "original_P1_values_K_Q_fixed_bases_Hecke_norm_connection_period_nonp_height_computed",
                 "real_descent_cubed_ideal_claimed_equal_to_Iz","characteristic_zero_RR_coefficients_reconstructed"):
        assert cert[flag] is False
    assert len(cert["closed_work_retention_receipts"])==5
    def own(row):
        assert row.get("source_group") is None
        assert entries[row["file"]]==plain(row)
        value=read(bound(out,row))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        return value
    def kernel(ref,m,n,r,dim):
        value=own(ref)
        assert value["matrix_shape"]==[m,n] and value["actual_rank"]==r and value["actual_kernel_dimension"]==dim
        assert len(value["selected_rows"])==len(value["selected_columns"])==r
        assert len(value["free_columns"])==dim
        dimensions(value["inverse_selected_minor_mod_prime"],r,r)
        dimensions(value["kernel_basis_mod_prime"],n,dim)
        for f in ("both_selected_inverse_products_verified","all_original_matrix_rows_times_complete_kernel_zero",
                  "free_normalization_identity_verified"):
            assert value[f] is True
        return value
    roots=[]
    for j in range(1,6):
        cref=cert["complete_direction_certificates"][str(j)];complete=own(cref);roots.append(cref)
        assert complete["original_direction"]==j
        assert complete["source_original_DZ_complete418"]==inputs["directions"][str(j)]["space"]
        assert complete["source_original_marked_QZ"]==inputs["directions"][str(j)]["principal"]
        assert complete["source_original_Dchi_complete418"]==inputs["Dchi"]
        assert complete["actual_shared_product_dimension"]==962
        assert complete["actual_membership_ranks"]==[544,544] and complete["actual_eighteen_jet_ranks"]==[18,18]
        assert complete["actual_padded_dimensions"]==[128,400]
        assert complete["actual_weight1_prefix_rank"]==256 and complete["actual_complement_dimension"]==144
        assert complete["actual_split_rank"]==272
        for flag in ("actual_original_Iz_128_RR_space_certified","actual_original_Iz_weight1_400_RR_space_certified",
                     "actual_original144_complement_with_original256_prefix_certified",
                     "actual_original_two_affine_rank272_lattices_certified",
                     "actual_original_unscaled_P0_frame_coefficient_certified"):
            assert complete[flag] is True
        product=own(complete["single_shared_product_image"])
        assert product["left_complete_space"]==inputs["directions"][str(j)]["space"]
        assert product["right_complete_space"]==inputs["Dchi"]
        assert product["actual_product_image_dimension"]==962
        dimensions(product["selected_product_basis_mod_prime"],1904,962)
        dimensions(product["inverse_selected_minor_mod_prime"],962,962)
        assert len(product["selected_rows"])==962
        assert sum(len(b["right_original_kernel_columns"]) for b in product["selected_original_product_columns_in_order"])==962
        assert product["both_complete_selected_inverse_products_verified_in_frozen_method"] is True
        assert product["all1904_original_fibre_rows_retained"] is True
        quotient=own(complete["shared_row_quotient"])
        assert quotient["source_complete_product_image"]==complete["single_shared_product_image"]
        assert quotient["selected_rows"]==product["selected_rows"] and len(quotient["complementary_rows"])==942
        dimensions(quotient["complement_times_selected_inverse_mod_prime"],942,962)
        normals={}
        for m,width,udim,dim,ukey,nkey in ((3,690,146,128,"complete_U3_146","complete_original_normal128"),
                                         (4,962,418,400,"complete_U4_418","complete_original_normal400")):
            u=kernel(complete[ukey],1884,width,544,udim)
            normal=own(complete[nkey]);normals[m]=normal
            assert normal["source_complete_U"]==complete[ukey]
            assert normal["ordinary_weight"]==m and normal["normal_shape"]==[width,dim]
            dimensions(normal["normal_basis_mod_prime"],width,dim)
            assert len(normal["canonical_normal_identity_rows"])==dim
            assert normal["canonical_identity_rows_verified"] is True
            assert len(normal["order18_coefficients_mod_prime"])==dim
            assert normal["all_eighteen_jet_rows_times_complete_basis_zero"] is True
            kernel(normal["source_complete_eighteen_jet_kernel"],18,udim,18,dim)
            jet=own(normal["source_nineteen_jet_restriction"])
            assert jet["matrix_shape"]==[19,udim] and jet["row_orders"]==list(range(19))
            assert jet["source_complete_U"]==complete[ukey]
        comp=own(complete["complete_original144_complement"])
        assert comp["source_complete_normal128"]==complete["complete_original_normal128"]
        assert comp["source_complete_normal400"]==complete["complete_original_normal400"]
        assert len(comp["selected_original_C400_columns"])==144
        assert len(set(comp["selected_original_C400_columns"]))==144
        dimensions(comp["normal_144_complement_mod_prime"],962,144)
        dimensions(comp["normal_complete400_with_prefix_mod_prime"],962,400)
        dimensions(comp["normal_tau_chart_272_columns_mod_prime"],962,272)
        dimensions(comp["complete_400_coordinate_change_mod_prime"],400,400)
        dimensions(comp["complete_400_coordinate_change_inverse_mod_prime"],400,400)
        for flag in ("both256_selected_inverse_products_verified","both400_inverse_products_verified",
                     "all962_normal_rows_of_complete400_basis_and_representation_verified",
                     "exact_complete_weight1_basis_is_original256_prefix_plus_selected144","original_scalars_not_rescaled"):
            assert comp[flag] is True
        assert comp["extra_tau_factor"]==0
        split=own(complete["complete_two_chart_splitting"])
        assert split["source_complete128_and144"]==complete["complete_original144_complement"]
        assert split["actual_rank"]==split["pushforward_rank"]==272 and split["both_vector_bundle_degrees"]==-144
        assert split["complete_two_affine_lattices_and_original_transition_certified"] is True
        assert split["extra_tau_division"] is False
        fibre=own(split["actual_unit_whole_fibre"])
        assert 0<=fibre["z0"]<7 and fibre["actual_rank"]==272 and fibre["accepted"] is True
        dimensions(fibre["matrix_mod_prime"],272,272);dimensions(fibre["inverse_mod_prime"],272,272)
        assert fibre["both_complete272_inverse_products_verified"] is True
        assert fibre["whole_fibre_regular_source_frame_certified_by_full_unit_matrix"] is True
        marked=own(complete["marked_original_P0_frame_and_embedding"])
        assert marked["original_direction"]==j and marked["source_original_marked_QZ"]==inputs["directions"][str(j)]["principal"]
        assert marked["source_original_qchi"]==inputs["qchi_anchor"]
        assert marked["source_original_t_frame"]==inputs["t_frame"]
        assert marked["source_complete_normal128"]==complete["complete_original_normal128"]
        assert marked["source_actual144_complement"]==complete["complete_original144_complement"]
        assert marked["source_complete_two_chart_splitting"]==complete["complete_two_chart_splitting"]
        assert marked["positive_multiplication_is_an_isomorphism_at_every_curve_DVR"] is True
        assert marked["selected_column_not_rescaled"] is True
        column=marked["original_P0_selected_column"];assert 0<=column<128
        assert normals[3]["order18_coefficients_mod_prime"][column]==marked["selected_order18_coefficient_mod_prime"]
        assert marked["actual_target_rho_order"]==marked["actual_target_t_order"]==RHO_ORDERS[j-1]-254
        assert marked["actual_c_exponent"]==254-RHO_ORDERS[j-1]
        for key in ("actual_rho_leading_mod_prime","actual_c_power_mod_prime","actual_t_frame_coefficient_mod_prime"):
            assert 0<marked[key]<P
        assert marked["same_exact_global_section_value_at_original_P1_computed"] is False
        assert marked["P0_unit_claimed_to_certify_P1_unit"] is False
        assert marked["K_or_Q_fixed_basis_computed"] is False
        assert marked["real_descent_cubed_ideal_identified_with_I_Z"] is False
        assert marked["negative_support_of_Z_not_assumed_to_be_only_P0"] is True
        closure=live_closure(out,entries,tag,sources,[cref])
        receipt=own(cert["closed_work_retention_receipts"][j-1])
        assert receipt["complete_direction_certificate"]==cref
        assert {x["file"]:plain(x) for x in receipt["required_live_witness_files"]}==closure
        assert receipt["active_or_pending_work_discarded"] is False
        assert receipt["cleanup_only_after_complete_direction_certificate"] is True
        for row in receipt["discarded_intermediate_stage_history"]:
            assert row["file"] not in entries
    return {"actual_complete_direction_count":5,"actual_dimensions":[128,400,144,272],
        "all_exact_live_witness_references_and_original_QZ_sources_verified":True,
        "new_mathematics_executed_by_verifier":False}

def verify(item,out):
    out=Path(out);run=read(out/"run-receipt.json")
    assert run["result"]==RESULT and run["source_commit"]==os.environ["GITHUB_SHA"]
    assert str(run["workflow_run_id"])==os.environ["GITHUB_RUN_ID"]
    assert run["core_sha256"]==item["core_sha256"] and run["wrapper_sha256"]==item["wrapper_sha256"]
    entries=entry_map(out,{"result":RESULT,"manifest_sha256":sha(out/MANIFEST)})
    reference=read(out/REFERENCE)
    assert reference["result"]==RESULT and plain(reference)==spec(out/MANIFEST)
    full=read(out/MANIFEST)
    assert full["source_commit"]==run["source_commit"]
    assert str(full["workflow_run_id"])==str(run["workflow_run_id"])
    for row in entries.values():
        bound(out,row)
    report={"result":RESULT,"complete":True,"run_complete":run["complete"],
            "process_exit_code":run["process_exit_code"],"all_output_bytes_and_SHA_verified":True,
            "mathematical_final_present":FINAL in entries,"new_mathematics_executed":False}
    if "public-actions-input.json" not in entries:
        assert run["complete"] is False and run["core_receipt_sha256"] is None
        report["stopped_before_core"]=True
    else:
        retained,sources,inputs,review=prepare(item,out,allow_download=False)
        tag=expected_tag(item,sources,inputs);initial=read(out/"public-actions-input.json")
        assert initial["result"]==RESULT and initial["core_sha256"]==item["core_sha256"]
        assert initial["job"]==item and initial["wrapper_sha256"]==item["wrapper_sha256"]
        assert initial["source_commit"]==run["source_commit"]
        assert str(initial["workflow_run_id"])==str(run["workflow_run_id"])
        assert plain(initial["source_inventory"])==entries[INVENTORY]
        assert plain(initial["expanded_job"])==entries[EXPANDED]
        expanded=read(out/EXPANDED)
        assert expanded["sources"]==sources and expanded["inputs"]==inputs
        assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
        assert initial["source_identities"]=={g:identity(sources[g]) for g in GROUPS}
        core=None
        if run.get("core_receipt_sha256") is not None:
            assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
            core=read(out/"core-receipt.json")
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
            if core.get("configuration") is not None:
                assert core["configuration"]==tag
        for name,row in entries.items():
            if name.startswith(PREFIX) and name.endswith(".json.gz"):
                value=read(bound(out,row))
                assert value["result"]==RESULT and value["configuration"]==tag
                assert value["complete"] is (False if name==PREFIX+"current.json.gz" else True)
                if "discarded_intermediate_stage_history" in value:
                    assert value["historical_hashes_are_not_live_dependencies"] is True
                    assert value["active_or_pending_work_discarded"] is False
                    for discarded in value["discarded_intermediate_stage_history"]:
                        assert discarded["file"] not in entries
        if FINAL in entries:
            cert=read(out/FINAL)
            assert cert["result"]==RESULT and cert["configuration"]==tag
            if cert["complete"] is True:
                assert run["complete"] is True and run["process_exit_code"]==0
                assert core is not None and core["complete"] is True
                assert core["certificate_sha256"]==entries[FINAL]["sha256"]
                assert core["actual_complete_direction_count"]==5
                sm=read(bound(out,cert["stage_manifest"]))
                assert sm["complete"] is True and sm["configuration"]==tag
                for row in sm["files"]:
                    assert entries[row["file"]]==plain(row)
                actual_stages={n:r for n,r in entries.items() if n.startswith(PREFIX) and n.endswith(".json.gz")
                    and n!=PREFIX+"current.json.gz" and not n.startswith(PREFIX+"stage-manifest-")}
                assert {r["file"]:plain(r) for r in sm["files"]}==actual_stages
                assert len(sm["files"])==cert["actual_retained_complete_stage_count"]
                assert entries[cert["resume_state"]["file"]]==plain(cert["resume_state"])
                report.update(verify_complete_final(item,out,entries,tag,cert,sources,inputs))
            else:
                assert run["complete"] is False
                report["honest_partial_final"]=True
                report["actual_complete_direction_count"]=len(cert["completed_directions"])
        else:
            assert run["complete"] is False
        report["source_review"]=review
    save(out/"verification-receipt.json",report)
    output_manifest(out)
    print("R903_VERIFY="+json.dumps(report,sort_keys=True),flush=True)
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
