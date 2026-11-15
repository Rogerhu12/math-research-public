#!/usr/bin/env python3
"""R825 source-bound public IO runner; no mathematical core is imported."""
import argparse
import datetime as dt
import hashlib
import gzip
import importlib.util
import re
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import signal
import subprocess
import sys
import tarfile


S=Path(__file__).resolve().parent
REPO=S.parents[2]
TOPIC=REPO/"topics/serre-uniformity"
REQUEST=TOPIC/"notes/R825-public-original-normal-derivatives-from-R824-request.json"
RESULT="R825-original-normal-derivatives-from-R824-normal-vectors"
FINAL="p41-original-normal-derivatives-from-R824-certificate.json"
SCOPE="original_a_b_normal_derivatives_in_two_charts"
BUNDLE="R825-R824-retained-producer-inputs.tar.gz"
REFERENCE="full-outputs-manifest-reference.json"
LABELS=("R809","R809_basis","R815","R820")
TARGETS=("A","B")
CHARTS=("tau","sigma")
EPS=[0]+[1]*144+[2]*127
FIELD="b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"
IO_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
IO_NAME="R824_public_original_global_polar_generators.py"
DERIVATIVE_NAME="R825_original_normal_derivative_inputs.py"
DERIVATIVE_SHA="89579f796e0f62132b37aa081719f7e7a7d62b87e7ef789d19289a8edaa462e1"
CORE_NAME="R825_original_normal_derivatives_from_R824.py"
CORE_SHA="f09fae2ba8ab06672f3b2ff3088cec16bd8a5b2442da8f999adbddc8d175e735"
METHOD_SHA="fa3d8a19fa1dfdecbd68a903667b506e94a338a073c19bde2a907afe83d227af"
NORMAL_RESULT="R809-original-A-B-normal-coordinates-from-R824"
NORMAL_SHA="cdc381fc5e1b9dfab705608f1d62a8ab80b282984479499a6edd635ea05fa62b"
BASIS_SHA="dedb5d6149a3c3ae86ad09e51f30c1424951a09010bf48afd948d2628e1ec21d"
S5_INDEX_SHA="f6f6f0ee2bae106ef474d2cff32c743b1d8e0a886f80c26aaf8708c89ea1c119"
META=("full-outputs-manifest.json","run-receipt.json","core-receipt.json","public-actions-input.json")
PATTERN_SHA=re.compile(r"[0-9a-f]{64}")
FRAMEWORK_SHA="849bca27968dcec4353b1af0f458d2329b6a5c8ab3b0dc2a7d65779da7fed2b3"
PROOF_SHA="73f9f293f0a0526a2f1eed8b62aea562b659090b546d1e122c0e12dbd1f90930"


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0, compresslevel=2) as compressed:
                compressed.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain(row):
    return {key: row[key] for key in ("file", "bytes", "sha256")}


def check_spec(row):
    assert Path(row["file"]).name == row["file"] and row["file"] not in ("", ".", "..")
    assert isinstance(row["bytes"], int) and row["bytes"] >= 0
    assert PATTERN_SHA.fullmatch(row["sha256"])


def identity(item):
    value = {key: item[key] for key in
             ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "certificate_name")}
    value["certificate_sha256"] = item["files"][item["certificate_name"]]
    return value


def same_identity(left, right):
    if "files" in left:
        left = identity(left)
    if "files" in right:
        right = identity(right)
    assert set(left) == set(right)
    for key in left:
        assert str(left[key]) == str(right[key]), ("Changed mathematical producer", key)


def topic_path(relative):
    path = (TOPIC/relative).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def github(path):
    return json.loads(subprocess.check_output(
        ["gh", "api", "repos/Rogerhu12/math-research-public/"+path], text=True))


assert sha(S/IO_NAME) == IO_SHA
loader = importlib.util.spec_from_file_location("R811_R824_frozen_public_IO", S/IO_NAME)
IO = importlib.util.module_from_spec(loader)
loader.loader.exec_module(IO)


class Archive(IO.Archive):
    """Range-select original sources; fully hash same-core continuation archives."""
    def __init__(self, item, directory, expected_conclusion="success", whole=False):
        bound = dict(item)
        bound.setdefault("expected_conclusion", expected_conclusion)
        super().__init__(bound, directory, whole=whole)

    @property
    def receipt(self):
        return IO.Archive.receipt(self)

    def verify_all_manifest_members(self, manifest):
        return self.verify_all(manifest)


def relation_source_identity(item):
    value = {key: item[key] for key in
             ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")}
    name = item["certificate_name"]
    value["certificate"] = {"file": name, "sha256": item["files"][name]}
    return value


class Producer:
    def __init__(self, label, item, directory, archive=None):
        self.label, self.item, self.directory, self.archive = label, item, Path(directory), archive
        self.directory.mkdir(parents=True, exist_ok=True)
        self.selected = {}
        manifest_path = self.materialize("full-outputs-manifest.json", item["manifest_sha256"])
        manifest = read(manifest_path)
        assert manifest["result"] == item["result"]
        self.files = {entry["file"]: entry for entry in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        for entry in self.files.values():
            check_spec(entry)
        run, core, initial = (self.raw(name) for name in META[1:])
        assert run["result"] == core["result"] == initial["result"] == item["result"]
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        assert run["source_commit"] == initial["source_commit"] == item["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == item["core_sha256"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert core["complete"] is True and core["source_sha256"] == item["core_sha256"]
        certname = item["certificate_name"]
        assert core["certificate_sha256"] == self.files[certname]["sha256"] == item["files"][certname]
        self.certificate, self.initial = self.raw(certname), initial
        assert self.certificate["result"] == item["result"] and self.certificate["complete"] is True
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == item["core_sha256"] and self.tag["python_flint"] == "0.9.0"
        inventory_spec = self.certificate["stage_manifest"]
        inventory = self.stage(inventory_spec)
        self.inventory = {entry["file"]: plain(entry) for entry in inventory["files"]}
        assert len(self.inventory) == len(inventory["files"])
        for name, entry in self.inventory.items():
            assert entry == plain(self.files[name])

    def materialize(self, name, digest, expected_bytes=None):
        assert Path(name).name == name
        path = self.directory/name
        if self.archive is not None:
            self.archive.extract_bound(name, digest, path, expected_bytes)
        else:
            assert path.is_file() and sha(path) == digest
            if expected_bytes is not None:
                assert path.stat().st_size == expected_bytes
        self.selected[name] = path
        return path

    def raw(self, name):
        entry = self.files[name]
        if name in self.item["files"]:
            assert entry["sha256"] == self.item["files"][name]
        path = self.materialize(name, entry["sha256"], entry["bytes"])
        return read(path)

    def stage(self, entry):
        assert plain(entry) == plain(self.files[entry["file"]])
        data = self.raw(entry["file"])
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def indexed(self, entry):
        assert self.inventory[entry["file"]] == plain(entry)
        return self.stage(entry)



def guard():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise SystemExit("Public repository Actions execution required.")


def local(relative):
    path=(TOPIC/relative).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def rational_shape(pair,nonzero=False):
    assert isinstance(pair,list) and len(pair)==2
    assert int(pair[1])>0
    if nonzero:assert int(pair[0])!=0


def select(producers):
    r9,r15,r20=(producers[label] for label in ("R809","R815","R820"))
    basis=producers["R809_basis"]
    c9,c15,c20=(p.certificate for p in (r9,r15,r20))
    assert r9.item["result"]==NORMAL_RESULT and r9.item["core_sha256"]==NORMAL_SHA
    assert basis.item["result"]=="R809-original-S5-normal-coordinates"
    assert basis.item["core_sha256"]==BASIS_SHA
    cbasis=basis.certificate
    assert c9["completed_scope"]=="A_and_B_only_from_one_true_R824_relation"
    assert c9["completed_rational_RHS_columns"]==28
    assert c9["all28_rational_RHS_columns_verified_in_all1380_rows"] is True
    assert c9["external_S5_references_keep_their_original_configuration"] is True
    assert c9["normal_function_equation"]=="y=normal(A)/normal(B)"
    assert c9["original_R824_denominator_and_content_reinserted"] is False
    assert c9["synthetic_original_R809_or_R787_result_created"] is False
    assert c9["original_S5_producer"]==relation_source_identity(basis.item)
    assert r9.tag["source_identities"]["R809"]==relation_source_identity(basis.item)
    assert r9.tag["original_S5_configuration_sha256"]==fingerprint(basis.tag)
    assert c9["actual_R824_source"]==r9.tag["actual_R824_source"]
    assert c9["actual_R824_relation"]==r9.tag["actual_R824_relation"]
    assert c9["original_b_model"]==cbasis["original_b_model"]
    assert cbasis["normal_basis_rank"]==272 and cbasis["normal_basis_degrees"]==EPS
    assert cbasis["S5_dimension"]==1234 and cbasis["qY_count"]==69
    assert cbasis["full_real_coordinates"]==1380
    assert cbasis["all_requested_targets_verified_in_all1380_rows"] is True
    assert cbasis["coefficient_field_basis"]==FIELD
    assert c9["actual_sigma_integer_n"]==cbasis["actual_sigma_integer_n"]
    assert r9.tag["actual_sigma_integer_n"]==basis.tag["actual_sigma_integer_n"]
    receipt=r9.indexed(c9["relation_source_receipt"])
    assert receipt["original_S5_producer"]==relation_source_identity(basis.item)
    assert receipt["original_S5_configuration"]==basis.tag
    assert receipt["original_S5_basis_index"]==cbasis["S5_basis_index"]
    assert r15.item["result"]=="R815-original-normal-derivation-operators"
    assert r20.item["result"]=="R820-original-cusp-finite-algebra-and-ideals"
    assert c9["actual_A_B_normal_vectors_computed"] is True
    assert set(TARGETS)<=set(c9["completed_target_groups"])
    assert c9["normal_basis_rank"]==272 and c9["normal_basis_degrees"]==EPS
    assert c9["S5_dimension"]==1234 and c9["full_real_coordinates"]==1380
    assert c9["coefficient_field_basis"]==FIELD
    assert c9["original_scalar_and_field_normalizations_preserved"] is True
    assert c15["completed_scope"]=="original_normal_derivation_operators"
    assert c15["requested_targets"]==["g","Gamma"]
    assert c15["normal_affine_basis_rank"]==272 and c15["normal_basis_degrees"]==EPS
    assert c15["coefficient_field_basis"]=="Q in the unchanged original K-normal basis"
    for key in ("original_Mg_computed","original_normal_derivation_connection_computed",
                "all_complete_polynomial_defining_identities_verified",
                "all_original_scalar_and_field_normalizations_preserved","normal_integral_basis_preserved"):
        assert c15[key] is True
    assert c15["Mg_exact_commutator_points"]==c15["Gamma_exact_nested_commutator_points"]==list(range(7))
    assert c20["completed_scope"]=="two_original_cusp_finite_algebra_kernels"
    assert c20["normal_basis_rank"]==272 and c20["normal_basis_degrees"]==EPS
    assert c20["actual_cusp_colengths"]=={"tau":20,"sigma":20}
    for key in ("original_two_chart_cusp_ideals_computed","complete_polynomial_kernels_certified",
                "same_original_cusp_field_and_two_chart_transitions_verified"):
        assert c20[key] is True
    free=basis.tag["original_graded_free_basis"]
    assert r15.tag["original_R805_free_basis"]==r20.tag["original_R805_free_basis"]==free
    same_identity(basis.tag["basis_producers"]["R805"],r20.tag["producer_identities"]["R805"])
    same_identity(r15.tag["R806_producer"],r20.tag["producer_identities"]["R806"])
    assert r9.tag["actual_sigma_integer_n"]==c15["actual_sigma_integer_n"]==r20.tag["actual_pencil_n"]==1
    assert c9["S5_basis_index"]==cbasis["S5_basis_index"]==r9.tag["original_S5_basis_index"]
    assert c9["S5_basis_index"]["sha256"]==S5_INDEX_SHA
    s5=basis.indexed(c9["S5_basis_index"])
    assert c9["minor_stage"]==cbasis["minor_stage"]
    minor=basis.indexed(cbasis["minor_stage"])
    rank=basis.indexed(minor["actual_rank_stage"])
    assert minor["actual_rank"]==rank["actual_rank"]==1234
    assert minor["S5_basis_index"]==rank["S5_basis_index"]==cbasis["S5_basis_index"]
    assert s5["dimension"]==1234 and s5["normal_affine_basis_rank"]==272
    assert s5["normal_basis_degrees"]==EPS and s5["original_graded_free_basis"]==free
    assert s5["integer_scale"]==str(82**10)
    assert s5["all_original_term_phases_and_scales_verified"] is True
    mapping=[(a,power) for a in range(272) for power in range(6-EPS[a])]
    assert len(s5["basis_rows"])==len(mapping)==1234
    for index,((a,power),entry) in enumerate(zip(mapping,s5["basis_rows"])):
        assert (entry["index"],entry["normal_basis_index"],entry["z_degree"],entry["normal_basis_degree"])==(index,a,power,EPS[a])
    target_specs={}
    group_specs={}
    for target in TARGETS:
        entry=c9["normal_vectors"][target]
        value=r9.indexed(entry)
        assert value["target"]==target and value["normal_basis_rank"]==272
        assert value["normal_basis_degrees"]==EPS and value["regular_degree_bound"]==5
        assert value["coefficient_field_basis"]==FIELD and value["S5_basis_index"]==c9["S5_basis_index"]
        assert value["original_b_model"]==c9["original_b_model"]
        config=c9["completed_target_configurations"][target]
        assert value["target_configuration"]==config
        assert value["target_configuration_sha256"]==fingerprint(config)
        assert config["basis_configuration_sha256"]==fingerprint(r9.tag)
        for key in ("all14_original_field_columns_retained","normal_vector_actually_nonzero",
                    "all1380_original_coordinates_verified","weighted_polynomial_support_verified",
                    "original_field_and_scalar_normalizations_preserved"):
            assert value[key] is True
        assert len(value["coordinate_groups"])==2
        for number,group_spec in enumerate(value["coordinate_groups"]):
            group=r9.indexed(group_spec)
            assert group["target"]==target and group["column_indices"]==list(range(number*7,(number+1)*7))
            assert group["normal_basis_rank"]==272 and group["basis_dimension"]==1234
            assert group["full_coordinate_rows"]==1380 and group["regular_degree_bound"]==5
            assert group["S5_basis_index"]==c9["S5_basis_index"] and group["coefficient_field_basis"]==FIELD
            assert group["target_configuration"]==config and group["target_configuration_sha256"]==fingerprint(config)
            assert group["all1380_original_coordinates_verified"] is True
            assert group["original_field_and_scalar_normalizations_preserved"] is True
            assert len(group["coordinate_numerators"])==1234 and all(len(row)==7 for row in group["coordinate_numerators"])
            assert len(group["column_denominators"])==len(group["original_target_rational_scales"])==7
            assert all(int(value)>0 for value in group["column_denominators"])
            for scale in group["original_target_rational_scales"]:rational_shape(scale)
        target_specs[target]=entry
        group_specs[target]=value["coordinate_groups"]
    operators={}
    operator_specs=c15["operator_indices"]
    assert set(operator_specs)=={"g","Gamma"}
    ranges=[(first,min(first+16,272)) for first in range(0,272,16)]
    for target,bound,kind in (("g",3,"multiplication"),("Gamma",2,"normal_derivation_connection")):
        value=r15.indexed(operator_specs[target])
        assert value["target"]==target and value["field_component"]==0
        assert value["operator_kind"]==kind and value["regular_degree_bound"]==bound
        assert value["coefficient_field_basis"]==c15["coefficient_field_basis"]
        assert value["target_configuration"]==c15["target_configurations"][target]
        assert value["target_configuration_sha256"]==fingerprint(value["target_configuration"])
        for chart in CHARTS:
            blocks=value["matrix_row_blocks_"+chart]
            assert len(blocks)==17
            for number,(block_spec,(first,stop)) in enumerate(zip(blocks,ranges)):
                block=r15.indexed(block_spec)
                assert block["target"]==target and block["field_component"]==0
                assert block["operator_kind"]==kind
                assert block["target_configuration"]==value["target_configuration"]
                assert block["target_configuration_sha256"]==value["target_configuration_sha256"]
                assert (block["row_first"],block["row_stop"],block["regular_degree_bound"])==(first,stop,bound)
                assert int(block["common_positive_denominator"])>0
                count=sum(bound+EPS[column]-EPS[row]+1 for row in range(first,stop) for column in range(272))
                assert len(block["coefficient_numerators"])==count
                if chart=="sigma":assert block["source_tau_matrix_row_block"]==value["matrix_row_blocks_tau"][number]
        operators[target]=value
    sigma=c15["sigma_base_variable_derivative"]
    assert sigma["matrix_blocks"]==operators["g"]["matrix_row_blocks_sigma"]
    assert sigma["rational_scalar"]==[-1,1]
    assert sigma["identity"]=="M_(delta_sigma t)=-t^3*D*Mg(1/t)*D^-1"
    cusp_columns={}
    for chart in CHARTS:
        value=r20.indexed(c20["two_chart_cusp_ideal_indexes"][chart])
        assert value["chart"]==chart and value["normal_basis_rank"]==272
        assert value["normal_basis_degrees"]==EPS and value["actual_diagonal_degrees"]==[0]*271+[20]
        assert value["actual_quotient_dimension_over_Q"]==20
        assert value["complete_polynomial_kernel_certified_by_inclusion_and_equal_colength"] is True
        columns=value["Hermite_columns_in_original_basis_order"]
        assert len(columns)==272
        for a,column in enumerate(columns):
            data=r20.indexed(column)
            degree=20 if a==271 else 0
            assert data["chart"]==chart and data["normal_basis_index"]==a
            assert data["kind"]=="first_dependence" and data["first_dependent_power"]==data["monic_diagonal_degree"]==degree
            assert data["exact_original_normal_basis_column"]==a
            assert data["source_field_interface"]==value["source_field_interface"]
            assert data["complete_relation_evaluation_zero_in_all_20_original_coordinates"] is True
            positions=set()
            for term in data["column_terms"]:
                key=(term["normal_basis_row"],term["power"])
                assert key not in positions
                positions.add(key)
                rational_shape(term["coefficient"],True)
                if key==(a,degree):
                    assert term["coefficient"]==["1","1"]
                elif a<271:
                    assert key[0]==271 and 0<=key[1]<20
                else:assert key[0]==271 and 0<=key[1]<20
            assert (a,degree) in positions
        cusp_columns[chart]=columns
    return {
        "original_R805_free_basis":free,"actual_sigma_integer_n":1,
        "original_R809_S5_index":c9["S5_basis_index"],
        "original_target_normal_vectors":target_specs,
        "original_target_coordinate_groups":group_specs,
        "original_R815_operator_indexes":operator_specs,
        "original_R815_matrix_row_blocks":{target:{chart:operators[target]["matrix_row_blocks_"+chart] for chart in CHARTS}
                                          for target in ("g","Gamma")},
        "original_R820_cusp_ideal_indexes":c20["two_chart_cusp_ideal_indexes"],
        "original_R820_cusp_Hermite_columns":cusp_columns,
        "old_R809_R815_R820_arithmetic_recomputed":False,
        "actual_normal_input_result":NORMAL_RESULT,
        "actual_R824_source":c9["actual_R824_source"],
        "actual_R824_relation":c9["actual_R824_relation"],
        "original_S5_producer":identity(basis.item),
        "original_S5_configuration_preserved":True}


def expected_tag(item,producers):
    r9,r15,r20=(producers[label] for label in ("R809","R815","R820"))
    basis=producers["R809_basis"]
    c9,c15,c20=(p.certificate for p in (r9,r15,r20))
    return {
        "result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "R825_proof_sha256":item["R825_proof_sha256"],
        "R825_adapter_method_sha256":item["R825_adapter_method_sha256"],
        "framework_sha256":item["framework_sha256"],"derivative_framework_sha256":DERIVATIVE_SHA,
        "actual_normal_input_result":NORMAL_RESULT,
        "actual_R824_source":c9["actual_R824_source"],
        "actual_R824_relation":c9["actual_R824_relation"],
        "actual_R824_free_column":c9["original_R824_free_column"],
        "original_S5_configuration_sha256":fingerprint(basis.tag),
        "normal_configuration_sha256":fingerprint(r9.tag),
        "external_S5_configuration_preserved":True,
        "producers":{label:identity(producers[label].item) for label in LABELS},
        "original_R805_free_basis":basis.tag["original_graded_free_basis"],"actual_sigma_integer_n":1,
        "normal_basis_rank":272,"normal_basis_degrees":EPS,"coefficient_field_basis":FIELD,
        "original_b_model":c9["original_b_model"],"original_R809_S5_index":c9["S5_basis_index"],
        "original_target_normal_vectors":{target:c9["normal_vectors"][target] for target in TARGETS},
        "original_R815_operator_indexes":c15["operator_indices"],
        "original_R820_cusp_ideal_indexes":c20["two_chart_cusp_ideal_indexes"],
        "requested_targets":list(TARGETS),"original_input_degree":5,
        "derivative_weighted_bound":7,"regular_g_product_weighted_bound":8,
        "original_D0_multiplier":["1","82"],"sigma_base_derivative_scalar":[-1,1],
        "field_component_order":[{"target":target,"field_component":component} for target in TARGETS for component in range(14)],
        "matrix_row_block_size":16,"completed_old_arithmetic_recomputed":False}


def scan_bundle(bundle,allowed,root=None):
    actual={}
    with tarfile.open(bundle,"r:gz") as stream:
        for member in stream:
            name=PurePosixPath(member.name)
            assert member.isfile() and len(name.parts)==2 and name.parts[0] in allowed
            assert not name.is_absolute() and ".." not in name.parts and member.name not in actual
            target=None if root is None else Path(root)/name.parts[0]/name.parts[1]
            if target is not None:
                target.parent.mkdir(parents=True,exist_ok=True)
                temporary=target.with_name(target.name+".transfer")
            digest,total=hashlib.sha256(),0
            source=stream.extractfile(member)
            destination=open(temporary,"wb") if target is not None else None
            try:
                for block in iter(lambda:source.read(1024*1024),b""):
                    digest.update(block);total+=len(block)
                    if destination is not None:destination.write(block)
            finally:
                source.close()
                if destination is not None:destination.close()
            assert total==member.size
            if target is not None:temporary.replace(target)
            actual[member.name]={"file":name.parts[1],"bytes":total,"sha256":digest.hexdigest()}
    return actual

def prepare(item,out):
    root=out.parent/"retained"
    present=[(root/label/"full-outputs-manifest.json").exists() for label in LABELS]
    assert all(present) or not any(present),"Partial input transfer has not yet formed a bound continuation bundle."
    producers,archives,transports={},{},[]
    for label in LABELS:
        original=item["retained_artifacts"][label]
        archive=None
        if not all(present):
            carrier=original.get("input_carrier")
            if carrier is not None:
                assert carrier["role"]=="unchanged_original_selected_files"
                assert carrier["original_result"]==original["result"]
                assert str(carrier["original_run_id"])==str(original["run_id"])
                assert carrier["original_source_commit"]==original["source_commit"]
            archive=Archive(carrier or original,out.parent/("download-"+label))
            archives[label]=archive
        producers[label]=Producer(label,original,root/label,archive)
    selection=select(producers)
    transports=[{"producer":label,"actual_transport":archive.receipt,
                 "original_mathematical_producer_preserved":True}
                for label,archive in archives.items()]
    for label,p in producers.items():
        assert {path.name for path in p.directory.iterdir() if path.is_file()}==set(p.selected)
    expected={label+"/"+name:file_spec(path) for label,p in producers.items() for name,path in p.selected.items()}
    bundle=out/BUNDLE
    if not bundle.exists():
        temporary=bundle.with_name(bundle.name+".tmp")
        with tarfile.open(temporary,"w:gz") as stream:
            for label,p in producers.items():
                for name,path in sorted(p.selected.items()):stream.add(path,arcname=label+"/"+name,recursive=False)
        temporary.replace(bundle)
    assert scan_bundle(bundle,set(LABELS))==expected
    save(out/"retained-inputs-receipt.json",{
        "result":RESULT,"producer_identities":{label:identity(p.item) for label,p in producers.items()},
        "selection":selection,"input_bundle":file_spec(bundle),
        "selected_files":{label:[file_spec(path) for _,path in sorted(p.selected.items())]
                          for label,p in producers.items()},
        "actual_selected_file_count":len(expected),"all_selected_member_hashes_verified":True,
        "transport_artifacts":transports,"same_core_selected_input_bundle_reused":all(present),
        "new_mathematics_executed":False})
    for archive in archives.values():
        archive.close()
    return producers,selection,root


def restore_resume(item,out):
    previous=item.get("resume")
    if previous is None:return
    archive=Archive(previous,out.parent/"download-resume",expected_conclusion="failure",whole=True)
    path=archive.extract_bound("full-outputs-manifest.json",previous["manifest_sha256"],
                              out.parent/"previous-manifest.json")
    manifest=read(path)
    assert manifest["result"]==RESULT
    files=archive.verify_all_manifest_members(manifest)
    def take(name,destination):
        row=files[name]
        return archive.extract_bound(name,row["sha256"],destination,row["bytes"])
    initial=read(take("public-actions-input.json",out.parent/"previous-input.json"))
    run=read(take("run-receipt.json",out.parent/"previous-run.json"))
    assert initial["result"]==run["result"]==RESULT
    assert initial["source_commit"]==run["source_commit"]==previous["source_commit"]
    assert str(run["workflow_run_id"])==str(previous["run_id"])
    old=initial["job"]
    for key in ("result","p","core","core_sha256","proof","R825_proof_sha256",
                "method","R825_adapter_method_sha256","requested_stage","requested_targets",
                "matrix_row_block_size","framework","framework_sha256","io_helper","io_helper_sha256",
                "derivative_framework","derivative_framework_sha256"):
        assert old[key]==item[key]
    for label in LABELS:
        same_identity(old["retained_artifacts"][label],item["retained_artifacts"][label])
        left,right=old["retained_artifacts"][label]["files"],item["retained_artifacts"][label]["files"]
        for name in set(left)&set(right):assert left[name]==right[name]
    bundle=take(BUNDLE,out/BUNDLE)
    transferred=scan_bundle(bundle,set(LABELS),out.parent/"retained")
    producers={label:Producer(label,item["retained_artifacts"][label],out.parent/"retained"/label)
               for label in LABELS}
    select(producers)
    expected={label+"/"+name:file_spec(path) for label,p in producers.items() for name,path in p.selected.items()}
    assert transferred==expected
    tag=expected_tag(item,producers)
    copied=0
    for name in files:
        if name!=FINAL and not (name.startswith("R825-") and name.endswith(".json.gz")):continue
        data=read(take(name,out/name))
        assert data["configuration"]==tag and data["complete"] is True
        assert not name.endswith("-current.json.gz")
        copied+=1
    save(out/"resume-receipt.json",{
        "result":RESULT,"previous_actual_artifact":previous,"actual_archive":archive.receipt,
        "all_previous_manifest_files_verified":len(files),"restored_complete_stage_files":copied,
        "all_selected_bundle_files_verified":len(transferred),
        "same_original_mathematical_sources_and_core":True,"old_completed_arithmetic_recomputed":False})
    archive.close()


def output_manifest(out):
    for path in out.iterdir():
        if path.is_file() and path.name.endswith((".tmp",".transfer",".partial")):path.unlink()
    artifact="serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    rows=[dict(file_spec(path),artifact=artifact,included_in_git=False)
          for path in sorted(out.iterdir()) if path.is_file() and path.name not in ("full-outputs-manifest.json",REFERENCE)]
    path=out/"full-outputs-manifest.json"
    save(path,{"result":RESULT,"files":rows,"temporary_active_checkpoint_artifact":artifact,
        "temporary_active_checkpoint_retention_days":1,
        "reproducible_rows_certificates_or_input_bundles_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,"manifest_file":path.name,"manifest_sha256":sha(path),
        "manifest_bytes":path.stat().st_size,"file_count":len(rows),"full_outputs_artifact":artifact,
        "automatic_git_or_release_publication":False})


def compute(item,out):
    out.mkdir(parents=True,exist_ok=True)
    core,proof,method=S/item["core"],local(item["proof"]),local(item["method"])
    source=subprocess.check_output(["git","rev-parse","HEAD"],cwd=REPO,text=True).strip()
    save(out/"public-actions-input.json",{
        "result":RESULT,"p":41,"source_repository":"Rogerhu12/math-research-public","source_commit":source,
        "job":item,"core_sha256":sha(core),"driver_sha256":sha(__file__),"proof_sha256":sha(proof),
        "method_sha256":sha(method),"framework_sha256":sha(S/item["framework"]),
        "derivative_framework_sha256":sha(S/item["derivative_framework"]),
        "io_helper_sha256":sha(IO.__file__),"request_sha256":sha(REQUEST),
        "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
        "workflow_sha256":sha(REPO/item["workflow"]),
        "prepared_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
        "new_arithmetic":"original A/B normal derivatives, exact two-chart transport, and original cusp coordinates",
        "old_R809_R815_R820_results_recomputed":False})
    code,error=1,None
    try:
        assert item["result"]==RESULT and item["p"]==41 and item["producer_inputs_pending"] is False
        assert item["requested_stage"]==SCOPE and item["requested_targets"]==list(TARGETS)
        assert item["matrix_row_block_size"]==16 and set(item["retained_artifacts"])==set(LABELS)
        assert item["core"]==CORE_NAME
        assert sha(core)==item["core_sha256"]==CORE_SHA and sha(__file__)==item["wrapper_sha256"]
        assert item["derivative_framework"]==DERIVATIVE_NAME
        assert sha(S/DERIVATIVE_NAME)==item["derivative_framework_sha256"]==DERIVATIVE_SHA
        assert item["io_helper"]==IO_NAME
        assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
        assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
        assert sha(proof)==item["R825_proof_sha256"]==PROOF_SHA
        assert sha(method)==item["R825_adapter_method_sha256"]==METHOD_SHA
        assert sha(IO.__file__)==item["io_helper_sha256"]==IO_SHA
        assert sha(S/item["framework"])==item["framework_sha256"]==FRAMEWORK_SHA
        restore_resume(item,out)
        _,_,retained=prepare(item,out)
        config=out.parent/"job-config.json"
        save(config,item)
        command=[sys.executable,"-u",str(core),"--config",str(config),"--proof",str(proof),
                 "--method",str(method),"--retained",str(retained),"--output",str(out),
                 "--budget-minutes",str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process=subprocess.Popen(command,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
            try:code=process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                error="Budget reached; completed original derivative and cusp-coordinate blocks retained."
                os.killpg(process.pid,signal.SIGTERM)
                try:process.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid,signal.SIGKILL)
                    process.wait()
                code=124
    except Exception as exception:
        error=type(exception).__name__+": "+str(exception)
    receipt=out/"core-receipt.json"
    core_receipt=read(receipt) if receipt.exists() else {"complete":False}
    complete=code==0 and core_receipt.get("complete") is True
    save(out/"run-receipt.json",{
        "result":RESULT,"p":41,"complete":complete,"process_exit_code":code,"error":error,"source_commit":source,
        "workflow_run_id":os.environ["GITHUB_RUN_ID"],"workflow_attempt":os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment":"public-repository-github-actions",
        "core_receipt_sha256":sha(receipt) if receipt.exists() else None,
        "original_a_b_normal_derivatives_computed":complete,
        "P_Q_operator_matrices_computed":False,"general_polar_ideal_or_D_computed":False,
        "original_eta_principal_functions_rigidification_or_heights_computed":False,
        "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result":RESULT,"complete":complete,"exit_code":code,"error":error}),flush=True)
    return code if code else (0 if complete else 1)

def verify(item,out):
    initial,run,core=(read(out/name) for name in ("public-actions-input.json","run-receipt.json","core-receipt.json"))
    assert initial["job"]==item and initial["result"]==run["result"]==core["result"]==RESULT
    assert initial["core_sha256"]==core["source_sha256"]==item["core_sha256"]==CORE_SHA
    assert initial["driver_sha256"]==item["wrapper_sha256"]
    assert initial["proof_sha256"]==item["R825_proof_sha256"]==PROOF_SHA
    assert initial["method_sha256"]==item["R825_adapter_method_sha256"]==METHOD_SHA
    assert initial["derivative_framework_sha256"]==item["derivative_framework_sha256"]==DERIVATIVE_SHA
    assert initial["framework_sha256"]==item["framework_sha256"]==FRAMEWORK_SHA
    assert initial["io_helper_sha256"]==item["io_helper_sha256"]==IO_SHA
    assert run["source_commit"]==initial["source_commit"]
    assert run["complete"] is True and run["process_exit_code"]==0
    assert run["core_receipt_sha256"]==sha(out/"core-receipt.json")
    assert core["complete"] is True and core["certificate_sha256"]==sha(out/FINAL)
    root=out.parent/"retained"
    if not all((root/label/"full-outputs-manifest.json").exists() for label in LABELS):
        scan_bundle(out/BUNDLE,set(LABELS),root)
    producers={label:Producer(label,item["retained_artifacts"][label],root/label) for label in LABELS}
    selection=select(producers)
    expected={label+"/"+name:file_spec(path) for label,p in producers.items() for name,path in p.selected.items()}
    assert scan_bundle(out/BUNDLE,set(LABELS))==expected
    receipt=read(out/"retained-inputs-receipt.json")
    assert receipt["selection"]==selection and receipt["actual_selected_file_count"]==len(expected)
    assert receipt["producer_identities"]=={label:identity(producers[label].item) for label in LABELS}
    assert receipt["input_bundle"]==file_spec(out/BUNDLE)
    assert receipt["all_selected_member_hashes_verified"] is True
    tag=expected_tag(item,producers)
    certificate=read(out/FINAL)
    assert certificate["result"]==RESULT and certificate["complete"] is True and certificate["configuration"]==tag
    assert certificate["completed_scope"]==SCOPE and certificate["requested_targets"]==list(TARGETS)
    assert certificate["normal_basis_rank"]==272 and certificate["normal_basis_degrees"]==EPS
    assert certificate["coefficient_field_basis"]==FIELD and certificate["original_b_model"]==tag["original_b_model"]
    assert certificate["actual_sigma_integer_n"]==1 and certificate["original_input_weight"]==5
    assert certificate["actual_normal_input_result"]==NORMAL_RESULT
    assert certificate["actual_R824_source"]==producers["R809"].certificate["actual_R824_source"]
    assert certificate["actual_R824_relation"]==producers["R809"].certificate["actual_R824_relation"]
    assert certificate["actual_R824_free_column"]==producers["R809"].certificate["original_R824_free_column"]
    assert certificate["original_S5_producer"]==identity(producers["R809_basis"].item)
    assert certificate["original_S5_configuration_preserved"] is True
    assert certificate["original_relation_denominator_or_content_reinserted"] is False
    assert certificate["synthetic_R787_or_C_only_R809_A_B_output_created"] is False
    assert certificate["derivative_weighted_bound"]==7 and certificate["regular_g_product_weighted_bound"]==8
    true_flags=("original_a_b_normal_derivatives_computed","all_complete_two_chart_transports_verified",
                "all_original_cusp_coordinate_changes_verified","all_28_original_field_columns_preserved",
                "original_scalar_and_field_normalizations_preserved","all_negative_power_transport_terms_cancelled_exactly")
    for key in true_flags:assert certificate[key] is True
    false_flags=("old_R809_R815_R820_arithmetic_recomputed","P_Q_operator_matrices_computed",
                 "general_polar_ideal_or_D_computed",
                 "original_eta_principal_functions_rigidification_or_heights_computed")
    for key in false_flags:assert certificate[key] is False
    for key in ("original_a_b_normal_derivatives_computed","complete_two_chart_transports_verified",
                "original_cusp_coordinate_changes_verified"):
        assert core[key] is True
    for key in false_flags[1:]:assert core[key] is False
    inventory_spec=certificate["stage_manifest"]
    assert file_spec(out/inventory_spec["file"])==inventory_spec
    inventory=read(out/inventory_spec["file"])
    assert inventory["configuration"]==tag and inventory["complete"] is True
    assert inventory["all_listed_stages_complete"] is True
    assert inventory["normal_derivative_row_block_count"]==34
    assert inventory["exact_two_chart_transition_block_count"]==17
    assert inventory["original_cusp_component_coordinate_count"]==56
    entries={entry["file"]:entry for entry in inventory["files"]}
    assert len(entries)==len(inventory["files"])
    for name,entry in entries.items():
        check_spec(entry)
        assert file_spec(out/name)==entry
        value=read(out/name)
        assert value["complete"] is True and value["configuration"]==tag
    actual={path.name for path in out.glob("R825-*.json.gz") if path.name!=inventory_spec["file"]}
    assert set(entries)==actual and not list(out.glob("R825-*-current.json.gz"))
    def ref(entry):
        assert entries[entry["file"]]==plain(entry)
        return read(out/entry["file"])
    input_specs=[]
    r9=producers["R809"]
    for target in TARGETS:
        original=r9.indexed(selection["original_target_normal_vectors"][target])
        for component in range(14):
            name="R825-input-"+target+"-component-"+str(component).zfill(2)+".json.gz"
            entry=entries[name]
            value=ref(entry)
            group_spec=original["coordinate_groups"][component//7]
            group=r9.indexed(group_spec)
            assert value["target"]==target and value["field_component"]==component
            assert value["source_normal_vector"]==selection["original_target_normal_vectors"][target]
            assert value["source_exact_coordinate_group"]==group_spec
            assert value["source_target_configuration"]==original["target_configuration"]
            assert value["original_S5_index"]==selection["original_R809_S5_index"]
            assert value["original_target_rational_scale"]==group["original_target_rational_scales"][component%7]
            assert value["original_group_column_denominator"]==str(int(group["column_denominators"][component%7]))
            assert value["normal_basis_rank"]==272 and value["normal_basis_degrees"]==EPS
            assert value["regular_degree_bound"]==5 and value["coefficient_field_basis"]==FIELD
            assert value["original_scalar_applied_exactly_once"] is True
            assert value["weighted_polynomial_support_verified"] is True
            assert int(value["common_positive_denominator"])>0 and int(value["normalization_content"])>0
            coefficients=value["coefficient_numerators"]
            assert len(coefficients)==6 and all(len(row)==272 for row in coefficients)
            for power,row in enumerate(coefficients):
                for output,number in enumerate(row):
                    if power>5-EPS[output]:assert int(number)==0
            assert value["actual_zero_component"] is (not any(int(number) for row in coefficients for number in row))
            input_specs.append(entry)
    assert len(input_specs)==28
    ranges=[(first,min(first+16,272)) for first in range(0,272,16)]
    blocks=certificate["two_chart_derivative_and_g_product_row_blocks"]
    assert set(blocks)==set(CHARTS)
    for chart in CHARTS:
        assert len(blocks[chart])==17
        for number,(entry,(first,stop)) in enumerate(zip(blocks[chart],ranges)):
            value=ref(entry)
            assert (value["chart"],value["row_first"],value["row_stop"])==(chart,first,stop)
            assert value["normal_basis_rank"]==272 and value["normal_basis_degrees"]==EPS
            assert value["field_component_order"]==tag["field_component_order"]
            assert value["source_original_input_components"]==input_specs
            assert value["source_Gamma_matrix_row_block"]==selection["original_R815_matrix_row_blocks"]["Gamma"][chart][number]
            assert value["source_regular_g_matrix_row_block"]==selection["original_R815_matrix_row_blocks"]["g"][chart][number]
            assert value["source_R815_certificate_sha256"]==tag["producers"]["R815"]["certificate_sha256"]
            assert value["base_derivative_scalar"]==(1 if chart=="tau" else -1)
            assert value["sigma_input_transport"]==(None if chart=="tau" else "v_sigma[i](t)=t^(5-eps_i)*v_tau[i](1/t)")
            assert value["derivative_weighted_bound"]==7 and value["regular_g_product_weighted_bound"]==8
            assert value["coefficient_field_basis"]==FIELD
            for key in ("original_scales_applied_exactly_once","one_original_g_matrix_product_shared_by_product_and_derivative",
                        "full_weighted_support_verified","all_original_Q_rational_coefficients_computed"):
                assert value[key] is True
            for key in ("column_denominators","original_input_column_denominators","joint_column_normalization_contents"):
                assert len(value[key])==28 and all(int(number)>0 for number in value[key])
            assert int(value["operator_common_positive_denominator"])>0
            for key,count,bound in (("derivative_coefficient_numerators",8,7),
                                    ("regular_g_product_coefficient_numerators",9,8)):
                coefficients=value[key]
                assert len(coefficients)==count
                assert all(len(rows)==stop-first and all(len(row)==28 for row in rows) for rows in coefficients)
                for power,rows in enumerate(coefficients):
                    for local,row in enumerate(rows):
                        if power>bound-EPS[first+local]:assert all(int(number)==0 for number in row)
    transitions=certificate["complete_two_chart_transition_certificates"]
    assert len(transitions)==17
    for number,(entry,(first,stop)) in enumerate(zip(transitions,ranges)):
        value=ref(entry)
        assert (value["row_first"],value["row_stop"])==(first,stop)
        assert value["source_tau_derivative_row_block"]==blocks["tau"][number]
        assert value["source_sigma_derivative_row_block"]==blocks["sigma"][number]
        assert value["field_component_order"]==tag["field_component_order"] and value["normal_basis_degrees"]==EPS
        assert value["derivative_transport"]=="d_sigma=t^6*D*d_tau(1/t)-5*t^7*D*u_tau(1/t)"
        assert value["regular_g_product_transport"]=="u_sigma=t^8*D*u_tau(1/t)"
        assert value["D"]=="diag(t^-eps_i)" and value["original_input_weight"]==5
        for key in ("all_28_original_field_columns_verified","full_rational_polynomial_identities_verified",
                    "both_separate_negative_power_terms_retained_and_cancelled","no_field_conjugation_or_new_mu3_choice"):
            assert value[key] is True
    for chart in CHARTS:
        value=ref(certificate["original_cusp_coordinate_interfaces"][chart])
        assert value["chart"]==chart and value["source_R820_cusp_index"]==selection["original_R820_cusp_ideal_indexes"][chart]
        assert value["source_original_Hermite_columns"]==selection["original_R820_cusp_Hermite_columns"][chart]
        assert value["normal_basis_rank"]==272 and value["actual_diagonal_degrees"]==[0]*271+[20]
        assert value["original_monic_modulus_degree"]==20
        assert value["coordinate_change_only_not_ideal_quotient"] is True
        assert value["exact_existing_sparse_shape_verified"] is True
        assert value["new_cusp_kernel_or_field_computed"] is False
    for target in TARGETS:
        target_number=TARGETS.index(target)
        cusp=certificate["original_cusp_coordinate_components"][target]
        assert set(cusp)==set(CHARTS)
        for chart in CHARTS:
            assert len(cusp[chart])==14
            for component,entry in enumerate(cusp[chart]):
                value=ref(entry)
                assert (value["chart"],value["target"],value["field_component"],value["joint_column_index"])==(
                    chart,target,component,target_number*14+component)
                assert value["source_derivative_row_blocks"]==blocks[chart]
                assert value["source_cusp_coordinate_interface"]==certificate["original_cusp_coordinate_interfaces"][chart]
                assert value["source_R820_cusp_index"]==selection["original_R820_cusp_ideal_indexes"][chart]
                assert value["source_original_input_component"]==input_specs[target_number*14+component]
                assert value["normal_basis_rank"]==272 and value["coefficient_field_basis"]==FIELD
                assert value["cusp_coordinate_last_row"]==271
                quotient=value["cusp_coordinate_last_row_polynomial"]
                assert len(quotient)<=7
                for coefficient in quotient:rational_shape(coefficient)
                if quotient:assert int(quotient[-1][0])!=0
                assert value["remaining_cusp_coordinate_rows_equal_source_normal_rows"]==list(range(271))
                assert value["numerator_identity"]=="d_271+sum(q_j*d_j)"
                for key in ("normal_and_cusp_basis_coordinates_are_distinct","coordinate_change_only_not_ideal_quotient",
                            "exact_original_P20_division_remainder_zero","full_rational_polynomial_product_verified",
                            "actual_derivative_vector_belongs_original_cusp_ideal"):
                    assert value[key] is True
                assert value["general_ideal_quotient_computed"] is False
        interface=ref(certificate["original_target_derivative_interfaces"][target])
        assert interface["target"]==target and interface["source_original_normal_vector"]==selection["original_target_normal_vectors"][target]
        assert interface["source_original_input_components"]==input_specs[target_number*14:(target_number+1)*14]
        assert interface["joint_field_column_indices"]==list(range(target_number*14,(target_number+1)*14))
        assert interface["normal_basis_rank"]==272 and interface["normal_basis_degrees"]==EPS
        assert interface["coefficient_field_basis"]==FIELD and interface["original_b_model"]==tag["original_b_model"]
        assert interface["derivative_vector_weighted_bound_on_each_chart"]==7
        assert interface["regular_g_product_vector_weighted_bound_on_each_chart"]==8
        assert interface["two_chart_derivative_and_g_product_row_blocks"]==blocks
        assert interface["complete_two_chart_transition_certificates"]==transitions
        assert interface["two_chart_original_cusp_coordinate_components"]==cusp
        for key in ("derivative_transition_is_not_weight7_homogeneous","original_sigma_extra_term_minus_5_t7_gv_retained",
                    "all14_original_field_columns_retained","all_normal_weighted_supports_verified",
                    "all_derivatives_in_original_two_chart_cusp_ideals_verified",
                    "all_two_chart_rational_polynomial_identities_verified","original_field_and_scalar_normalizations_preserved"):
            assert interface[key] is True
        for key in ("derivative_multiplication_matrix_computed","general_polar_ideal_or_D_computed",
                    "original_eta_principal_functions_rigidification_or_heights_computed"):
            assert interface[key] is False
    full=read(out/"full-outputs-manifest.json")
    assert full["result"]==RESULT
    files=set()
    for entry in full["files"]:
        assert entry["file"] not in files
        assert file_spec(out/entry["file"])==plain(entry)
        files.add(entry["file"])
    assert files=={path.name for path in out.iterdir() if path.is_file() and path.name not in ("full-outputs-manifest.json",REFERENCE)}
    reference=read(out/REFERENCE)
    assert reference["manifest_sha256"]==sha(out/"full-outputs-manifest.json")
    assert reference["file_count"]==len(files)
    print(json.dumps({"R825_VERIFY_REVIEW":{
        "complete":True,"selected_original_input_files_verified":len(expected),
        "complete_stage_files_verified":len(entries),"normal_derivative_row_blocks":34,
        "complete_transition_row_blocks":17,"cusp_coordinate_component_certificates":56,
        "actual_core_seconds":certificate["seconds"],
        "P_Q_operator_matrices_computed":False,"general_polar_ideal_or_D_computed":False}}),flush=True)
    return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=["compute","verify"])
    args=parser.parse_args()
    out=Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT/"output"
    if args.mode=="compute":
        request=read(REQUEST)
        assert request["session"]=="serre-public-astra-20261115"
        return compute(request["job"],out)
    return verify(read(out/"public-actions-input.json")["job"],out)


if __name__=="__main__":
    raise SystemExit(main())
