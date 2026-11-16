#!/usr/bin/env python3
"""R919 standard-library source, carrier, resume and public-Action driver."""
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
RESULT="R919-original-whole-Artin-Hecke-differential-trace"
FINAL="p41-original-whole-Artin-Hecke-differential-trace-certificate.json"
PREFIX="R919-"
CORE="R919_original_whole_Artin_Hecke_differential_trace.py"
HELPER="R885_whole_Artin_algebra.py"
REQUEST=TOPIC/"notes/R919-whole-Artin-Hecke-differential-trace-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R919-retained-original-inputs.tar.gz"
INVENTORY="R919-original-source-inventory.json"
INPUT_RECEIPT="R919-retained-inputs-receipt.json"
EXPANDED="R919-expanded-job.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
GROUPS=("R885","R827","R882","R873","R807")
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
P=1000000753
EPS=[0]+[1]*144+[2]*127
IO=None


STRATEGY={
    "original_curve":"original genus127 Y, level82, original minus3 descent",
    "prime":P,"original_zeta_root":549966761,"original_s_root":99932770,
    "source_node_ordinal":0,"source_z":0,
    "source_algebra":"entire original Fp[X]/chi_0(X), dimension272",
    "correspondence":"entire A0[U]/(P(U)/a8), rank8",
    "derivation":"delta=g*d/dz on the original function field, evaluated only after original-leaf differentiation",
    "M2_leaves":"1,z-beta72,beta1,...,beta144 with original82 scales retained once",
    "derivative_basis_block_size":64,"target_normal_block_size":16,
    "new_coefficient_columns":"delta(P0),...,delta(P8), nine columns only",
    "Euler_row":"L(h)=-a8^-1*[U^7](h*deltaP mod (P/a8))",
    "row_domain_basis":"1,U,...,U^7 over the entire A0",
    "input_differential_frame":"dz_target","output_differential_frame":"original nu_source=dz_source/g_source",
    "exact_check":"all8 basis values equal -Tr_E/A0(h*deltaP/Pprime), using the completed original inverse",
    "target_application":"all272 completed original target normal coordinates",
    "old_theta_a8_Pprime_Krylov_inverses_recomputed":False,
    "old2058_values_17coordinates_adjugate_or_correspondence_recomputed":False,
    "delta_claimed_to_descend_to_source_fibre":False,
    "source_factors_nilpotents_or_multiplicities_discarded":False,
    "finite_values_claimed_char0_expanded_or_global_calibration":False,
    "budget_excluded_from_identity":True}

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(4*1024*1024),b""):h.update(b)
    return h.hexdigest()

def read(path):
    path=Path(path)
    with (gzip.open if path.suffix==".gz" else open)(path,"rt",encoding="utf-8") as f:
        return json.load(f)

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    raw=(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n").encode()
    if path.suffix==".gz":
        with tmp.open("wb") as f:
            with gzip.GzipFile(filename="",fileobj=f,mode="wb",mtime=0,compresslevel=2) as z:z.write(raw)
    else:tmp.write_bytes(raw)
    tmp.replace(path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def plain(row):
    out={k:row[k] for k in ("file","bytes","sha256")}
    p=PurePosixPath(out["file"])
    assert len(p.parts)==1 and p.name not in ("",".","..") and "\\" not in out["file"]
    assert isinstance(out["bytes"],int) and out["bytes"]>=0 and re.fullmatch("[0-9a-f]{64}",out["sha256"])
    return out

def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}

def identity(source):
    out={**{k:source[k] for k in BASE},"configuration_sha256":source["configuration_sha256"],
         "selected_files_sha256":fingerprint(source["files"]),
         "stage_result_location":source["stage_result_location"]}
    key="certificate" if source.get("certificate") is not None else "configuration_stage"
    out[key]=plain(source[key])
    return out

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"helper_sha256":item["helper_sha256"],
            "python_flint":"0.9.0","p":41,"method_sha256":item["method_sha256"],"proofs":item["proofs"],
            "sources":{g:identity(item["sources"][g]) for g in GROUPS},"inputs":item["inputs"],"strategy":STRATEGY}

def same_source(left,right):
    assert all(str(left[k])==str(right[k]) for k in BASE)
    assert left["configuration_sha256"]==right["configuration_sha256"]

def shape(raw,m,n):
    assert len(raw)==m and all(len(row)==n for row in raw),(m,n)

class Source:
    def __init__(self,group,item,root):
        self.group,self.item=group,item
        self.folder=Path(root)/group
        self.files={n:plain(r) for n,r in item["files"].items()};self.checked=set()
        assert all(k==r["file"] for k,r in self.files.items())
        assert spec(self.folder/MANIFEST)==self.files[MANIFEST]
        assert self.files[MANIFEST]["sha256"]==item["manifest_sha256"]
        manifest=read(self.folder/MANIFEST)
        assert manifest["result"]==item["result"]
        indexed={r["file"]:plain(r) for r in manifest["files"]}
        assert len(indexed)==len(manifest["files"])
        indexed[MANIFEST]=self.files[MANIFEST]
        assert all(indexed[n]==r for n,r in self.files.items())
        initial=self.raw("public-actions-input.json");run=self.raw("run-receipt.json")
        core=self.raw("core-receipt.json")
        assert initial["source_commit"]==run["source_commit"]==item["source_commit"]
        assert str(run["workflow_run_id"])==str(item["run_id"])
        recorded=initial["core_sha256"] if "core_sha256" in initial else initial["job"]["core_sha256"]
        assert recorded==core["source_sha256"]==item["core_sha256"]
        assert run["core_receipt_sha256"]==self.files["core-receipt.json"]["sha256"]
        self.certificate=None
        if item.get("certificate") is not None:
            self.certificate=self.raw(item["certificate"]["file"])
            assert self.files[item["certificate"]["file"]]==plain(item["certificate"])
            assert self.certificate["complete"] is True and self.certificate["result"]==item["result"]
            assert run["complete"] is True and core["complete"] is True and run["process_exit_code"]==0
            assert core["certificate_sha256"]==item["certificate"]["sha256"]
            self.tag=self.certificate["configuration"]
        else:
            assert group=="R827" and run["complete"] is False and core["complete"] is False
            assert run["process_exit_code"]==124
            anchor=self.raw(item["configuration_stage"]["file"])
            assert anchor["complete"] is True
            self.tag=anchor["configuration"]
        assert fingerprint(self.tag)==item["configuration_sha256"]
        assert self.tag["result"]==item["result"]
        assert self.tag.get("source_sha256",self.tag.get("core_sha256"))==item["core_sha256"]
        if core.get("configuration") is not None:assert core["configuration"]==self.tag
        if core.get("configuration_sha256") is not None:assert core["configuration_sha256"]==item["configuration_sha256"]
        assert item["stage_result_location"]==("configuration" if group in ("R807","R827") else "top_level")

    def raw(self,name):
        if name not in self.checked:
            assert spec(self.folder/name)==self.files[name],(self.group,name)
            self.checked.add(name)
        return read(self.folder/name)

    def stage(self,row):
        row=plain(row);assert self.files[row["file"]]==row
        value=self.raw(row["file"])
        assert value["complete"] is True and value["configuration"]==self.tag,(self.group,row["file"])
        if self.item["stage_result_location"]=="configuration":
            assert "result" not in value and value["configuration"]["result"]==self.item["result"]
        else:
            assert value["result"]==self.item["result"]
        return value

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

class Review:
    def __init__(self,item,retained):
        self.item=item;self.inputs=item["inputs"]
        self.sources={g:Source(g,item["sources"][g],retained) for g in GROUPS}
        for key in ("fibre_certificate","source_functions","correspondence_algebra","target_normal_index",
                    "full_target_equations","original_W","original_place","original_Krylov","original_Gamma",
                    "operator_identity","seventeen_coordinates","same_place_interface","correspondence_DAG",
                    "theta","E6_clearing"):
            row=self.inputs[key]
            setattr(self,key,self.sources[row["source_group"]].stage(row))
        self.validate_sources()
        for key in ("Gamma_blocks","target_normal_blocks"):
            for row in self.inputs[key]:
                self.sources[row["source_group"]].stage(row)

    def validate_sources(self):
        s=self.source_functions;c=self.correspondence_algebra;f=self.fibre_certificate
        assert s["source_node_ordinal"]==0 and s["source_node_value"]==0
        assert s["prime"]==P and s["source_algebra_dimension"]==272
        assert s["all2058_functions_consumed"] is True and s["original82_scales_retained_once"] is True
        assert s["new_scale_applied"]=="1" and s["column_order"]=="P0..P8,K0..K7"
        assert s["complete_fibre_factors_or_multiplicities_removed"] is False
        shape(s["original_M2_functions_over_A"],146,272)
        shape(s["original2058_basis_function_values_over_A"],2058,272)
        shape(s["seventeen_values_over_A"],17,272)
        for field,key in (("source_DAG","correspondence_DAG"),("source_seventeen_coordinates","seventeen_coordinates"),
                          ("source_theta","theta"),("source_E6_clearing","E6_clearing"),
                          ("source_original_Krylov","original_Krylov")):
            assert plain(s[field])==plain(self.inputs[key])
        assert f["whole_fibre_success"] is True and f["all_required_units_on_entire_algebras_verified"] is True
        assert f["all272_original_target_normal_coordinates_certified"] is True
        for field,key in (("source_functions","source_functions"),("correspondence_algebra","correspondence_algebra"),
                          ("target_normal_row","target_normal_index"),("full_target_equations","full_target_equations")):
            assert plain(f[field])==plain(self.inputs[key])
        assert plain(c["source_functions"])==plain(self.inputs["source_functions"])
        assert c["base_algebra_dimension"]==272 and c["correspondence_rank"]==8 and c["full_scalar_dimension"]==2176
        assert c["original_P_coefficients"]==s["seventeen_values_over_A"][:9]
        assert c["original_K_coefficients"]==s["seventeen_values_over_A"][9:]
        for proof in (s["theta_unit_certificate"],c["leading_coefficient_unit_certificate"],c["Pprime_unit_certificate"]):
            assert proof["whole_fibre_unit"] is True
        assert c["full_Pprime_times_target_w_equals_K_verified"] is True
        assert c["any_source_factor_or_multiplicity_discarded"] is False
        idx=self.target_normal_index
        assert idx["all272_target_normal_coordinates_computed"] is True and idx["target_gamma0_equals_one"] is True
        assert len(idx["blocks"])==len(self.inputs["target_normal_blocks"])==17
        for ordinal,(part,ref) in enumerate(zip(idx["blocks"],self.inputs["target_normal_blocks"])):
            assert part["normal_columns"]==[16*ordinal,min(16*ordinal+16,272)]
            assert plain(part["source"])==plain(ref)
        assert self.full_target_equations["all272_original_target_equations_verified"] is True
        assert self.full_target_equations["all2176_scalar_coordinates_of_each_equation_checked"] is True
        assert self.full_target_equations["no_factor_or_nilpotent_component_discarded"] is True
        place=self.original_place
        assert place["prime"]==P and place["original_zeta_root"]==549966761 and place["original_s_root"]==99932770
        assert place["original_integral_B_root"]==3197390 and place["original_branch"]==0
        assert self.original_W["prime"]==P and self.original_W["original_rational_denominators_all_units"] is True
        assert self.original_W["original_W_e0_equals_e1_verified"] is True
        shape(self.original_W["g_vector_coefficients_mod_prime"],4,272)
        point=self.original_Krylov
        assert point["prime"]==P and point["z0"]==0
        assert plain(point["source_original_W"])==plain(self.inputs["original_W"])
        shape(point["inverse_Krylov_matrix_mod_prime"],272,272)
        gamma=self.original_Gamma
        assert gamma["prime"]==P and gamma["target"]=="Gamma" and gamma["chart"]=="tau"
        assert gamma["normal_basis_degrees"]==EPS and gamma["regular_degree_bound"]==2
        assert gamma["original_true_operator_reduction_certified"] is True and gamma["all_weighted_support_zeros_verified"] is True
        assert len(gamma["row_blocks"])==len(self.inputs["Gamma_blocks"])==17
        assert all(plain(a)==plain(b) for a,b in zip(gamma["row_blocks"],self.inputs["Gamma_blocks"]))
        oi=self.operator_identity
        assert oi["all_operators_are_true_original_p_integral_reductions"] is True
        assert oi["Gamma_nested_full_polynomial_identity_certified_by_seven_points"] is True
        assert oi["Gamma_first_column_zero_and_second_column_original_vh"] is True
        assert oi["all_sigma_negative_powers_and_original_minus_sign_verified"] is True
        assert plain(oi["operator_indexes"]["Gamma"]["tau"])==plain(self.inputs["original_Gamma"])
        assert self.seventeen_coordinates["prime"]==P
        assert self.seventeen_coordinates["same_characteristic_zero_coefficients_integral_at_new_place"] is True
        shape(self.seventeen_coordinates["coordinate_matrix_mod_prime"],2058,17)
        assert plain(self.seventeen_coordinates["source_exact_R873_unit_solve"])==plain(self.correspondence_DAG["coefficient_unit_solve"])
        assert self.same_place_interface["all2200_by17_original_equations_verified"] is True
        assert self.same_place_interface["prime"]==P and self.same_place_interface["original_zeta_root"]==549966761
        assert plain(self.same_place_interface["new_modular_coordinates"])==plain(self.inputs["seventeen_coordinates"])
        assert plain(self.same_place_interface["source_R873_correspondence_DAG"])==plain(self.inputs["correspondence_DAG"])
        dag=self.correspondence_DAG
        assert dag["exact_original_correspondence_expression_certified"] is True
        assert dag["rigidified_Hecke_transport"]["frozen_direction"]=="Nm_pi_t(pi_s^*I)"
        assert len(dag["old_V8_over_tau8"])==2050 and len(dag["new_eight_complement_functions"])==8
        for k,row in enumerate(dag["old_V8_over_tau8"]):
            assert row["index"]==k and len(row["original_M2_leaf_indices"])==8
        for k,row in enumerate(dag["new_eight_complement_functions"]):
            assert row["index"]==2050+k and len(row["original_M2_leaf_indices"])==2
        assert dag["new_eight_complement_functions"][0]["original_M2_leaf_indices"]==[0,0]
        assert dag["P_over_tau8_coefficients"]=={"powers_U":list(range(9)),"unit_solve_columns":list(range(9))}
        theta=self.theta;clear=self.E6_clearing
        assert theta["original_M2_integer_scale"]=="6724" and theta["theta_nonzero_by_original_independent_M2_input"] is True
        assert plain(theta["M6_index692_cleared_coordinate_stage"])==plain(self.inputs["E6_clearing"])
        assert clear["M6_index"]==692 and clear["basis_dimension"]==962 and len(clear["solution_numerators"])==962
        assert clear["all1100_rows_verified"] is True and clear["exact_global_V4_membership_certified"] is True
        assert clear["basis_integer_scale"]=="2044140858654976"
        assert str(clear["solution_common_denominator"])==s["completed_N692_common_denominator"]
        ed=dag["E6hat_over_tau3"]
        assert plain(ed["theta_source"])==plain(self.inputs["theta"])
        assert plain(ed["V4_coordinate_source"])==plain(self.inputs["E6_clearing"]) and ed["new_scale_applied"]=="1"
        for group in ("R827","R882","R873","R807"):
            same_source(self.sources["R885"].tag["sources"][group],identity(self.item["sources"][group]))
        same_source(self.sources["R882"].tag["sources"]["R873"],identity(self.item["sources"]["R873"]))
        same_source(self.sources["R873"].tag["sources"]["R807"],identity(self.item["sources"]["R807"]))

def source_review(item,retained):
    review=Review(item,retained)
    return {"result":RESULT,"original_groups":list(GROUPS),
        "selected_file_counts":{g:len(item["sources"][g]["files"]) for g in GROUPS},
        "original_source_z":0,"prime":P,"complete_source_dimension":272,
        "complete_correspondence_scalar_dimension":2176,
        "old_Gamma17_and_target_normal17_blocks_reused":True,
        "historical_schema_and_original_configuration_verified":True,
        "new_mathematics_executed":False}



def load_io():
    global IO
    path=S/RANGE_FILE
    assert sha(path)==RANGE_SHA
    description=importlib.util.spec_from_file_location("R919_frozen_stdlib_Range",path)
    IO=importlib.util.module_from_spec(description);description.loader.exec_module(IO)

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve() and item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False and 0<item["budget_minutes"]<=300
    assert item["core"]==CORE and sha(S/CORE)==item["core_sha256"]
    assert item["helper"]==HELPER and sha(S/HELPER)==item["helper_sha256"]
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["io_helper"]==RANGE_FILE and item["io_helper_sha256"]==RANGE_SHA
    assert set(item["sources"])==set(GROUPS)
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():assert sha(topic_path(row["path"]))==row["sha256"]
    load_io()

def selected_from_tar(package,retained,source):
    root=Path(retained);root.mkdir(parents=True,exist_ok=True)
    selected=source["files"];seen=set()
    with tarfile.open(package,"r|gz") as stream:
        for member in stream:
            if member.isdir():continue
            p=PurePosixPath(member.name)
            assert member.isfile() and not p.is_absolute() and ".." not in p.parts
            assert "\\" not in member.name and len(p.parts)==2 and p.parts[0]=="original"
            name=p.name
            if name not in selected:continue
            assert name not in seen;seen.add(name)
            row=plain(selected[name]);assert member.size==row["bytes"]
            dst=root/name;tmp=dst.with_name(name+".download");h=hashlib.sha256();count=0
            with stream.extractfile(member) as src,tmp.open("wb") as out:
                for chunk in iter(lambda:src.read(4*1024*1024),b""):
                    out.write(chunk);h.update(chunk);count+=len(chunk)
            assert count==row["bytes"] and h.hexdigest()==row["sha256"],name
            if dst.exists():assert spec(dst)==row;tmp.unlink()
            else:tmp.replace(dst)
    assert seen==set(selected),("prepared_transport_incomplete",sorted(set(selected)-seen))

def fetch_source(item,group,retained,work):
    source=item["sources"][group];folder=Path(retained)/group
    folder.mkdir(parents=True,exist_ok=True)
    wanted=source["files"];missing=[]
    for name,row in wanted.items():
        if (folder/name).exists():assert spec(folder/name)==plain(row),(group,name)
        else:missing.append(name)
    if not missing:return {"kind":"existing_selected_bytes","new_mathematics_executed":False}
    prepared=item.get("prepared_transports",{}).get(group)
    if prepared is not None:
        archive=IO.Archive(prepared["archive"],Path(work)/("transport-"+group),whole=False)
        try:
            package=plain(prepared["package"]);path=Path(work)/(group+"-"+package["file"])
            if path.exists():assert spec(path)=={**package,"file":path.name}
            else:archive.extract_bound(package["file"],package["sha256"],path,package["bytes"])
            selected_from_tar(path,folder,source)
            return {"kind":"completed_original_intake","archive":prepared["archive"],
                "package":package,"transport":archive.receipt(),"original_mathematical_identity_unchanged":True}
        finally:archive.close()
    archive=IO.Archive(source,Path(work)/("original-"+group),whole=False)
    try:
        archive.extract_many([(n,wanted[n]["sha256"],folder/n,wanted[n]["bytes"]) for n in missing])
        return {"kind":"original_artifact_Range","source":{k:source[k] for k in BASE},
            "transport":archive.receipt(),"all_selected_bytes_manifest_bound":True}
    finally:archive.close()

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R919";retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (BUNDLE,INVENTORY,INPUT_RECEIPT)):
        inventory=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        assert inventory["sources"]==item["sources"] and inventory["inputs"]==item["inputs"]
        assert receipt["source_inventory"]==spec(out/INVENTORY) and receipt["source_bundle"]==spec(out/BUNDLE)
        assert receipt["source_identities"]=={g:identity(item["sources"][g]) for g in GROUPS}
        unpack(out/BUNDLE,retained,item["sources"])
        return retained,source_review(item,retained)
    assert allow_download,"Offline verification requires the completed minimal source carrier."
    work=out.parent/"R919-source-transport";work.mkdir(parents=True,exist_ok=True)
    transports={g:fetch_source(item,g,retained,work) for g in GROUPS}
    review=source_review(item,retained)
    save(out/INVENTORY,{"result":RESULT,"complete":True,"sources":item["sources"],"inputs":item["inputs"],
        "transports":transports,"original_selected_bytes_and_tags_preserved":True,
        "new_mathematics_executed":False,"old_large_carriers_not_needed":True})
    pack(retained,item["sources"],out/BUNDLE)
    save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,
        "source_inventory":spec(out/INVENTORY),"source_bundle":spec(out/BUNDLE),
        "source_identities":{g:identity(item["sources"][g]) for g in GROUPS},
        "selected_file_counts":{g:len(item["sources"][g]["files"]) for g in GROUPS},
        "all_original_source_bytes_and_schemas_verified":True,"new_mathematics_executed":False})
    print("R919_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
    return retained,review

def restore(item,out):
    resume=item.get("resume")
    if not resume:return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R919-resume";directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R919-resume-archive",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],directory/MANIFEST,resume.get("manifest_bytes"))
        old=read(directory/MANIFEST)
        assert old["result"]==RESULT and old["source_commit"]==resume["source_commit"]
        entries={r["file"]:plain(r) for r in old["files"]}
        assert len(entries)==len(old["files"])
        names=(set(META)&set(entries))|{BUNDLE,INVENTORY,INPUT_RECEIPT}
        archive.extract_many([(n,entries[n]["sha256"],directory/n,entries[n]["bytes"]) for n in sorted(names)])
        initial=read(directory/"public-actions-input.json");run=read(directory/"run-receipt.json")
        assert initial["result"]==run["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]==resume["source_commit"]
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        assert initial["core_sha256"]==item["core_sha256"] and initial["wrapper_sha256"]==item["wrapper_sha256"]
        tag=expected_tag(item)
        assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
        assert expected_tag(initial["job"])==tag
        core=None
        if run["core_receipt_sha256"] is not None:
            assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
            core=read(directory/"core-receipt.json")
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
            assert core["helper_sha256"]==item["helper_sha256"]
            if core.get("configuration") is not None:assert core["configuration"]==tag
        else:
            assert run["complete"] is False and run["process_exit_code"]==124 and run["outer_timeout"] is True
        inventory=read(directory/INVENTORY);receipt=read(directory/INPUT_RECEIPT)
        assert inventory["sources"]==item["sources"] and inventory["inputs"]==item["inputs"]
        assert receipt["source_inventory"]==entries[INVENTORY] and receipt["source_bundle"]==entries[BUNDLE]
        for name in (BUNDLE,INVENTORY,INPUT_RECEIPT):
            if (out/name).exists():assert spec(out/name)==entries[name]
            else:shutil.copyfile(directory/name,out/name)
        stages=[n for n in entries if n.startswith(PREFIX) and n.endswith(".json.gz")]
        archive.extract_many([(n,entries[n]["sha256"],directory/n,entries[n]["bytes"]) for n in stages])
        for name in stages:
            value=read(directory/name)
            assert value["result"]==RESULT and value["configuration"]==tag
            assert value["complete"] is (False if name==PREFIX+"current.json.gz" else True)
            if (out/name).exists():assert spec(out/name)==entries[name]
            else:shutil.copyfile(directory/name,out/name)
        if FINAL in entries:
            archive.extract_bound(FINAL,entries[FINAL]["sha256"],directory/FINAL,entries[FINAL]["bytes"])
            cert=read(directory/FINAL)
            assert cert["result"]==RESULT and cert["configuration"]==tag
            if cert["complete"] is True:
                assert run["complete"] is True and core is not None and core["complete"] is True
                assert core["certificate_sha256"]==entries[FINAL]["sha256"]
                sm=plain(cert["stage_manifest"]);assert entries[sm["file"]]==sm
                for row in read(bound(directory,sm))["files"]:assert entries[row["file"]]==plain(row)
                if cert.get("resume_state") is not None:
                    assert entries[cert["resume_state"]["file"]]==plain(cert["resume_state"])
                shutil.copyfile(directory/FINAL,out/FINAL)
        save(out/"resume-import-receipt.json",{"result":RESULT,"complete":True,"source":resume,
            "source_manifest":spec(directory/MANIFEST),"restored_stage_count":len(stages),
            "mathematical_configuration_sha256":fingerprint(tag),"same_core_and_source_bytes_preserved":True,
            "false_historical_FINAL_not_used_to_overwrite_newer_current":True,
            "original_missing_core_receipt_retained_as_missing":core is None,"transport":archive.receipt()})
    finally:archive.close()

def compute(item,out,request):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    code,error,outer_timeout=1,None,False
    try:
        restore(item,out)
        retained,review=prepare(item,out)
        save(out/EXPANDED,item);tag=expected_tag(item)
        save(out/"public-actions-input.json",{
            "result":RESULT,"p":41,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"job":item,
            "core_sha256":item["core_sha256"],"wrapper_sha256":item["wrapper_sha256"],
            "request_sha256":sha(request),"workflow_sha256":sha(REPO/item["workflow"]),
            "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
            "expanded_job":spec(out/EXPANDED),"source_inventory":spec(out/INVENTORY),
            "mathematical_configuration_sha256":fingerprint(tag),
            "source_identities":{g:identity(item["sources"][g]) for g in GROUPS},
            "new_mathematics_in_wrapper":False})
        command=[sys.executable,str(S/CORE),"--config",str(out/EXPANDED),
            "--retained",str(retained),"--output",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"core.log").open("ab") as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:code=process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                outer_timeout=True
                os.killpg(process.pid,signal.SIGTERM)
                try:process.wait(timeout=15)
                except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
                code=124;error="outer_timeout"
        if code==0:assert read(out/FINAL)["complete"] is True
        print((out/"core.log").read_text(errors="replace")[-16000:],flush=True)
    except Exception as exc:
        if code in (0,1):code=1
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

def output_stage(out,entries,tag,row):
    row=plain(row);assert entries[row["file"]]==row
    value=read(bound(out,row))
    assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
    return value

def verify_complete_final(item,out,entries,tag,cert):
    assert cert["actual_auxiliary_prime"]==P and cert["original_source_node"]==0
    assert cert["source_algebra_dimension"]==272 and cert["correspondence_rank"]==8
    assert cert["correspondence_scalar_dimension"]==2176
    for key in ("actual_nine_original_delta_P_values_certified","actual_complete_A0_linear_Euler_row_certified",
                "actual_all8_trace_basis_identities_verified","actual_all272_target_normal_differential_traces_computed",
                "whole_source_factors_and_nilpotents_retained"):
        assert cert[key] is True
    for key in ("actual_characteristic_zero_derivative_coordinates_expanded","actual_original_Gamma_characteristic_zero_expanded",
                "seven_connection_numerator_evaluations_computed","original_Hecke_projector_or_endpoint_calibration_computed",
                "nonp_terms_Poincare_period_or_height_computed","old_source_arithmetic_recomputed"):
        assert cert[key] is False
    refs={k:cert[k] for k in ("source_audit","source_leaf_derivatives","basis_derivative_index",
        "nine_delta_P_coefficients","Euler_trace_row","full_eight_basis_identity",
        "all272_target_normal_trace_table","exact_characteristic_zero_expression_DAG")}
    values={k:output_stage(out,entries,tag,r) for k,r in refs.items()}
    audit=values["source_audit"]
    assert audit["sources"]=={g:identity(item["sources"][g]) for g in GROUPS}
    assert audit["inputs"]==item["inputs"] and audit["old_complete_p753_source_identities_verified"] is True
    leaf=values["source_leaf_derivatives"]
    shape(leaf["delta_original_M2_values_over_A"],146,272)
    for key in ("delta_z_value_over_A","delta_theta_over_tau","delta_N692_over_tau4",
                "delta_E6hat_over_tau3","delta_E6hat_square_over_tau6"):
        assert len(leaf[key])==272
    assert leaf["source_Gamma_index"]==item["inputs"]["original_Gamma"]
    assert leaf["source_Gamma_blocks"]==item["inputs"]["Gamma_blocks"]
    assert leaf["old_E6hat_square_value_reused_from_basis_index"]==2050
    assert leaf["derivation_applied_before_fibre_reduction"] is True
    assert leaf["delta_claimed_to_descend_to_A0"] is False
    idx=values["basis_derivative_index"];assert idx["basis_dimension"]==2058
    assert idx["all2058_original_basis_derivatives_evaluated"] is True
    expected=[(f,min(f+64,2058)) for f in range(0,2058,64)]
    assert [(x["first"],x["stop"]) for x in idx["blocks"]]==expected
    for part in idx["blocks"]:
        data=output_stage(out,entries,tag,part["source"])
        assert (data["first"],data["stop"])==(part["first"],part["stop"])
        shape(data["delta_basis_values_over_A"],part["stop"]-part["first"],272)
        assert data["source_new_leaf_derivatives"]==refs["source_leaf_derivatives"]
        assert data["old_complete_V8_values_recomputed"] is False
        assert data["product_and_quotient_rules_include_all_original_factors"] is True
    dp=values["nine_delta_P_coefficients"]
    assert dp["source_basis_derivatives"]==refs["basis_derivative_index"]
    assert dp["source_original_seventeen_coordinates"]==item["inputs"]["seventeen_coordinates"]
    assert dp["coefficient_indices"]==list(range(9))
    shape(dp["delta_P_coefficients_over_A"],9,272)
    assert dp["all2058_rows_and_nine_original_P_columns_consumed"] is True
    assert dp["delta_K_or_new_coefficient_solve_computed"] is False
    row=values["Euler_trace_row"];shape(row["linear_functional_coefficients_over_A"],8,272)
    shape(row["deltaP_reduced_in_E"],8,272)
    assert len(row["U_power_deltaP_remainders_over_E"])==8
    for rem in row["U_power_deltaP_remainders_over_E"]:shape(rem,8,272)
    assert row["row_domain_basis_U_powers"]==list(range(8))
    assert row["source_nine_delta_P_coefficients"]==refs["nine_delta_P_coefficients"]
    assert row["source_original_correspondence"]==item["inputs"]["correspondence_algebra"]
    assert row["input_frame"]=="dz_target" and row["output_frame"]=="nu_source"
    assert row["a8_inverse_reused_from_original_complete_certificate"] is True
    tr=values["full_eight_basis_identity"]
    assert tr["source_Euler_row"]==refs["Euler_trace_row"]
    assert tr["all8_basis_identities_in_entire_A0_verified"] is True
    assert len(tr["basis_certificates"])==8
    for j,r in enumerate(tr["basis_certificates"]):
        v=output_stage(out,entries,tag,r)
        assert v["basis_U_power"]==j and v["source_Euler_row"]==refs["Euler_trace_row"]
        shape(v["multiplication_matrix_diagonal_over_A"],8,272)
        shape(v["negative_h_deltaP_over_Pprime_in_E"],8,272)
        assert v["actual_trace_over_A"]==v["coefficient_functional_over_A"]==row["linear_functional_coefficients_over_A"][j]
        assert v["complete_all272_coordinate_equality_verified"] is True and v["new_inverse_computed"] is False
        if j<7:shape(v["next_negative_h_deltaP_over_Pprime_in_E"],8,272)
        else:assert v["next_negative_h_deltaP_over_Pprime_in_E"] is None
    table=values["all272_target_normal_trace_table"]
    assert table["all272_original_target_normal_differentials_evaluated"] is True
    assert table["source_original_full_target_equations"]==item["inputs"]["full_target_equations"]
    assert table["source_Euler_row"]==refs["Euler_trace_row"]
    assert table["input_frame"]=="dz_target" and table["output_frame"]=="nu_source"
    assert table["connection_numerators_evaluated"] is False
    assert [r["normal_columns"] for r in table["blocks"]]==[[i,min(i+16,272)] for i in range(0,272,16)]
    for part,old_source in zip(table["blocks"],item["inputs"]["target_normal_blocks"]):
        v=output_stage(out,entries,tag,part["source"]);first,stop=part["normal_columns"]
        assert v["normal_columns"]==[first,stop]
        assert v["source_original_target_normal_block"]==old_source
        assert v["source_full_rank8_trace_certificate"]==refs["full_eight_basis_identity"]
        shape(v["Tr_beta_target_dz_target_over_nu_source"],stop-first,272)
        assert v["full_eight_coefficients_and_entire_source_algebra_used"] is True
        assert v["original_target_coordinates_recomputed"] is False
    dag=values["exact_characteristic_zero_expression_DAG"]
    assert dag["source_original_correspondence_DAG"]==item["inputs"]["correspondence_DAG"]
    assert dag["source_R915_proof"]==item["proofs"]["R915"]
    assert dag["exact_characteristic_zero_expression_defined"] is True
    assert len(dag["nine_derivative_nodes"])==9
    assert dag["characteristic_zero_derivative_or_Hecke_coordinates_expanded"] is False
    assert dag["original_Gamma_characteristic_zero_expanded"] is False
    assert dag["original_connections_evaluated_or_calibrated"] is False
    assert dag["nonp_terms_Poincare_period_or_height_computed"] is False
    assert dag["original_rigidified_Hecke_transport"]["frozen_direction"]=="Nm_pi_t(pi_s^*I)"
    assert dag["differential_transport"]["kappa_nu_endpoint_constants_replaced"] is False

def verify(item,out):
    out=Path(out);full=read(out/MANIFEST)
    assert full["result"]==RESULT
    entries={r["file"]:plain(r) for r in full["files"]};assert len(entries)==len(full["files"])
    for name,row in entries.items():assert name==row["file"];bound(out,row)
    reference=read(out/REFERENCE)
    assert reference["result"]==RESULT and plain(reference)==spec(out/MANIFEST)
    run=read(out/"run-receipt.json")
    assert run["result"]==RESULT and run["core_sha256"]==item["core_sha256"] and run["wrapper_sha256"]==item["wrapper_sha256"]
    assert run["source_commit"]==full["source_commit"] and str(run["workflow_run_id"])==str(full["workflow_run_id"])
    if not all(n in entries for n in ("public-actions-input.json",INVENTORY,INPUT_RECEIPT,BUNDLE)):
        assert run["complete"] is False and run["process_exit_code"]!=0
        return {"result":RESULT,"complete":False,"failure_before_complete_input_carrier":True,
            "process_exit_code":run["process_exit_code"],"error":run["error"],
            "source_manifest":spec(out/MANIFEST),"new_mathematics_executed_in_IO":False}
    retained,review=prepare(item,out,allow_download=False);tag=expected_tag(item)
    initial=read(out/"public-actions-input.json")
    assert initial["result"]==RESULT and initial["source_commit"]==run["source_commit"]
    assert str(initial["workflow_run_id"])==str(run["workflow_run_id"])
    assert initial["job"]==item and initial["core_sha256"]==item["core_sha256"]
    assert initial["wrapper_sha256"]==item["wrapper_sha256"]
    assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
    assert initial["source_inventory"]==entries[INVENTORY] and initial["expanded_job"]==entries[EXPANDED]
    assert read(out/EXPANDED)==item
    stages={};currents={}
    for name,row in entries.items():
        if not name.startswith(PREFIX) or not name.endswith(".json.gz"):continue
        value=read(out/name);assert value["result"]==RESULT and value["configuration"]==tag
        if name==PREFIX+"current.json.gz":
            assert value["complete"] is False;currents[name]=row
        else:
            assert value["complete"] is True
            if name.startswith(PREFIX+"stage-manifest-"):
                inv={r["file"]:plain(r) for r in value["files"]}
                assert len(inv)==len(value["files"])
                for n,r in inv.items():assert n!=name and entries[n]==r
            else:stages[name]=row
    core=None
    if run["core_receipt_sha256"] is not None:
        assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
        core=read(out/"core-receipt.json")
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        assert core["helper_sha256"]==item["helper_sha256"]
        if core.get("configuration") is not None:assert core["configuration"]==tag
    else:
        assert run["complete"] is False and run["process_exit_code"]==124 and run["outer_timeout"] is True
    cert=None
    if FINAL in entries:
        cert=read(out/FINAL)
        assert cert["result"]==RESULT and cert["configuration"]==tag
        if cert["complete"] is True:
            assert run["complete"] is True and run["process_exit_code"]==0
            assert core is not None and core["complete"] is True
            assert core["certificate_sha256"]==entries[FINAL]["sha256"]
            inventory=output_stage(out,entries,tag,cert["stage_manifest"])
            assert {r["file"]:plain(r) for r in inventory["files"]}==stages
            assert len(inventory["files"])==len(stages)
            if cert.get("resume_state") is not None:
                assert entries[cert["resume_state"]["file"]]==plain(cert["resume_state"])
            verify_complete_final(item,out,entries,tag,cert)
        else:assert run["complete"] is False
    if run["complete"]:assert cert is not None and cert["complete"] is True
    return {"result":RESULT,"complete":run["complete"],"process_exit_code":run["process_exit_code"],
        "core_receipt_present":core is not None,"outer_timeout":run["outer_timeout"],
        "manifest":spec(out/MANIFEST),"certificate":entries.get(FINAL),"actual_complete_stage_count":len(stages),
        "actual_current_count":len(currents),"retained_source_bundle":entries[BUNDLE],
        "source_inventory":entries[INVENTORY],"source_review":review,
        "configuration_sha256":fingerprint(tag),
        "nine_delta_P_coefficients":None if cert is None else cert.get("nine_delta_P_coefficients"),
        "Euler_trace_row":None if cert is None else cert.get("Euler_trace_row"),
        "full_eight_basis_identity":None if cert is None else cert.get("full_eight_basis_identity"),
        "all272_target_normal_trace_table":None if cert is None else cert.get("all272_target_normal_trace_table"),
        "exact_characteristic_zero_expression_DAG":None if cert is None else cert.get("exact_characteristic_zero_expression_DAG"),
        "new_mathematics_executed_in_IO":False}

def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("compute","verify"))
    parser.add_argument("--request",type=Path,default=REQUEST)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();item=read(args.request);guard(item,args.request)
    if args.mode=="verify":
        result=verify(item,args.output)
        print("R919_COMPLETE_IO_REVIEW="+json.dumps(result,sort_keys=True),flush=True)
        return 0 if result["complete"] else 1
    code=compute(item,args.output,args.request)
    try:print("R919_COMPLETE_IO_REVIEW="+json.dumps(verify(item,args.output),sort_keys=True),flush=True)
    except Exception:
        traceback.print_exc()
        if code==0:code=1
    return code
if __name__=="__main__":sys.exit(main())

