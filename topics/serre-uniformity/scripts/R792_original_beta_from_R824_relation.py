#!/usr/bin/env python3
"""R792 arithmetic with an authentic completed R824 relation as the source."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpq_poly

S = Path(__file__).resolve().parent
FRAMEWORK_NAME = "R792_original_beta_composition.py"
FRAMEWORK_SHA = "7b7a5483e560f2d244092af486c8aed606b18c1f3557dddb3b850a290b4e343d"
ADAPTER_NAME = "R824_original_exact_relation_adapter.py"
ADAPTER_SHA = "5a6a100a561ce02350a5d538df908d4cca9575e21b251a848a3bfba9d3df1958"
METHOD_SHA = "68877a988f4df5dc3a7609ea46d4f40129d40af40b5467200456829df730d818"
PROOF_SHA = "75362e44da996c4c481b548816bfeb532f799bde47f63400bcc7791e0aa5f46b"
RESULT = "R792-original-beta-from-R824-relation"
FINAL = "p41-original-beta-from-R824-relation-certificate.json"

def source_sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


assert source_sha(S/ADAPTER_NAME) == ADAPTER_SHA
assert source_sha(S/FRAMEWORK_NAME) == FRAMEWORK_SHA
_loader = importlib.util.spec_from_file_location("original_R824_relation_adapter", S/ADAPTER_NAME)
relation_adapter = importlib.util.module_from_spec(_loader)
_loader.loader.exec_module(relation_adapter)
_loader = importlib.util.spec_from_file_location("original_R792_beta_framework", S/FRAMEWORK_NAME)
beta = importlib.util.module_from_spec(_loader)
_loader.loader.exec_module(beta)

read, save, sha, file_spec = beta.read, beta.save, beta.sha, beta.file_spec
BASIS_FILES, DIMENSIONS = beta.BASIS_FILES, beta.DIMENSIONS
R786_CERT_SHA, R786_INDEX_SHA = beta.R786_CERT_SHA, beta.R786_INDEX_SHA
R786_PROOF_SHA, R790_PROOF_SHA = beta.R786_PROOF_SHA, beta.R790_PROOF_SHA
FIELD_CORE_SHA, MODEL_SHA, MODEL = beta.FIELD_CORE_SHA, beta.MODEL_SHA, beta.MODEL
same_producer = beta.same_producer
ORIGINAL_LABELS = {"R735", "R775", "R786", "R790", "R791"}
SOURCE_STAGE = "R792-R824-original-relation-source"


class Job(beta.Job):
    def __init__(self, args):
        beta.guard()
        assert flint.__version__ == "0.9.0"
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.config = read(args.config)
        assert self.config["result"] == RESULT and self.config["p"] == 41
        assert self.config["producer_inputs_pending"] is False
        assert self.config["core_sha256"] == sha(__file__)
        assert self.config["coarse_jet_order"] == 1
        assert self.config["beta_framework"] == FRAMEWORK_NAME
        assert self.config["beta_framework_sha256"] == FRAMEWORK_SHA
        assert self.config["relation_adapter"] == ADAPTER_NAME
        assert self.config["relation_adapter_sha256"] == ADAPTER_SHA
        assert self.config["R792_proof_sha256"] == sha(args.proof) == PROOF_SHA
        assert self.config["relation_adapter_method_sha256"] == sha(args.method) == METHOD_SHA
        assert self.config["field_core_sha256"] == sha(args.field_core) == FIELD_CORE_SHA
        assert set(self.config["retained_artifacts"]) == ORIGINAL_LABELS | {"R824"}
        self.inputs = {label: beta.Retained(args.retained, label, self.config["retained_artifacts"][label])
                       for label in ORIGINAL_LABELS}
        model = self.inputs["R735"].certificate
        self.actual_relation = relation_adapter.OriginalWeightFiveRelation(
            Path(args.retained)/"R824", self.config["retained_artifacts"]["R824"],
            self.config["relation_spec"], self.inputs["R786"].spec,
            self.inputs["R786"].certificate["basis_index"], model["minimal_polynomial"])
        self.relation = self.actual_relation.data
        self.lam = int(self.relation["field"]["lambda"])
        module_spec = importlib.util.spec_from_file_location("retained_R754", args.field_core)
        self.module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(self.module)
        self.L = self.module.QKField(self.module.dp(model["minimal_polynomial"]))
        assert self.L.degree == 7
        self.b, self.zeta = self.L.gen, self.L.zeta
        self.s = 1+2*self.zeta
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R792_proof_sha256": PROOF_SHA, "relation_adapter_method_sha256": METHOD_SHA,
            "beta_framework_sha256": FRAMEWORK_SHA, "relation_adapter_sha256": ADAPTER_SHA,
            "field_core_sha256": FIELD_CORE_SHA, "coarse_jet_order": 1,
            "retained_artifacts": self.config["retained_artifacts"],
            "actual_R824_relation": relation_adapter.plain(self.config["relation_spec"]),
            "original_map_index": 4, "original_map_degree": "1206",
            "original_R787_reserved_target_recomputed": False,
            "original_R824_denominator_and_content_reinserted": False,
        }
        self.prepare_relation_and_recipes(model)
        self.prepare_original_direction()
        receipt = self.actual_relation.receipt()
        old = self.cached(SOURCE_STAGE)
        if old is None:
            self.store(SOURCE_STAGE, receipt)
        else:
            for key, value in receipt.items():
                assert old[key] == value

    def prepare_relation_and_recipes(self, model):
        r775, r786, r790 = (self.inputs[key] for key in ("R775", "R786", "R790"))
        assert self.relation["field"]["original_b_minimal_polynomial"] == model["minimal_polynomial"]
        assert self.relation["field"]["original_b_replaced_by_another_twist"] is False
        assert r786.certificate_sha == R786_CERT_SHA
        assert r786.tag["R786_proof_sha256"] == R786_PROOF_SHA
        assert r786.certificate["basis_in_original_R775_saved_order"] is True
        assert r786.certificate["exact_power5_basis_dimension"] == 1234
        assert self.relation["original_basis_index"] == r786.certificate["basis_index"]
        assert r786.certificate["basis_index"]["sha256"] == R786_INDEX_SHA
        index = r786.get_spec(r786.certificate["basis_index"])
        assert index["dimension"] == 1234 and index["bound_qY"] == 128
        assert [row["index"] for row in index["basis_rows"]] == list(range(1234))
        scale = "13744803133596058624"
        assert self.relation["basis_integer_scale"] == r786.certificate["basis_integer_scale"] == scale
        assert index["integer_scale"] == scale
        assert r775.certificate["all_recipes_defined_over_original_K"] is True
        self.recipes = {}
        old_prefix = r786.tag["R775_completed_prefix_producer"]
        for power, (name, digest) in BASIS_FILES.items():
            assert old_prefix["files"][name] == digest
            stage = r775.get(name, digest)
            assert stage["rank"] == DIMENSIONS[power] and len(stage["basis"]) == DIMENSIONS[power]
            assert stage["characteristic_zero_independence_certified_by_unit_reduction"] is True
            self.recipes[power] = [row["recipe"] for row in stage["basis"]]
        cm = r790.certificate
        assert cm["p"] == 41 and cm["M2_dimension"] == 146 and cm["cm_jet_order"] == 5
        assert cm["original_psi_values_and_first_coarse_jets_verified"] is True
        assert cm["original_M2_scale"] == "6724" and cm["R786_power5_product_scale"] == scale
        assert cm["distinct_retained_M2_seeds"] == 5 and cm["actual_reflected_seed_pairs"] == 10
        assert r790.tag["R790_proof_sha256"] == R790_PROOF_SHA
        assert r790.tag["field_core_sha256"] == FIELD_CORE_SHA
        assert r790.tag["retained_artifacts"]["R735"]["files"][MODEL] == MODEL_SHA
        same_producer(r790.tag["retained_artifacts"]["R775"], r775.spec)
        manifest = r790.get_spec(cm["stage_manifest"])
        assert manifest["M2_output_rows"] == cm["M2_output_rows"]
        stage_files = {row["file"]: row for row in manifest["files"]}
        assert len(cm["M2_output_rows"]) == 146
        self.m2 = []
        for index, spec in enumerate(cm["M2_output_rows"]):
            assert spec["file"] == "R790-M2-CM-jet-"+str(index).zfill(4)+".json.gz"
            assert stage_files[spec["file"]] == spec
            row = r790.get_spec(spec)
            assert row["index"] == index and row["original_recipe"] == self.recipes[1][index]
            assert row["integer_scale"] == "6724" and row["R786_power1_scale_preserved"] is True
            assert row["M2_recipe_source_sha256"] == BASIS_FILES[1][1]
            assert row["original_c1"] == 4424
            assert row["coarse_coordinate"] == "z=a-1; z=-epsilon^3/(81*(U/4)^2)+O(epsilon^6)"
            assert row["K_basis"] == ["1", "zeta=(-1+sqrt(-3))/2"]
            self.m2.append(tuple(self.decode_K(row[key]) for key in
                                 ("value_K_1_zeta", "derivative_z_K_1_zeta")))
        self.coefficients = []
        for key in ("A_integer_L_coordinates", "B_integer_L_coordinates"):
            rows = self.relation[key]
            assert len(rows) == 1234 and all(len(row) == 14 for row in rows)
            values = []
            for row in rows:
                aa = [(int(row[i])+int(row[7+i]))*self.lam**i for i in range(7)]
                dd = [2*int(row[7+i])*self.lam**i for i in range(7)]
                values.append(self.L.elt(fmpq_poly(aa), fmpq_poly(dd)))
            self.coefficients.append(values)
        assert any(self.coefficients[1])

    def run(self):
        point = self.point(self.section_jets())
        if point is None:
            save(self.out/"core-receipt.json", {
                "result": RESULT, "complete": False, "source_sha256": sha(__file__),
                "beta_framework_sha256": FRAMEWORK_SHA, "actual_beta_C_computed": False,
                "needs_higher_common_zero_evaluation": True, "common_zero_order_at_least": 2,
                "actual_R824_relation": relation_adapter.plain(self.config["relation_spec"]),
                "completed_stages_preserved": True, "exit_code": 75})
            return 75
        manifest_name = "R792-R824-stage-manifest"
        files = []
        for path in sorted(self.out.glob("R792-*.json.gz")):
            if path == self.path(manifest_name):
                continue
            data = read(path)
            assert data["complete"] is True and data["configuration"] == self.tag
            files.append(file_spec(path))
        self.store(manifest_name, {"files": files})
        certificate = {
            "result": RESULT, "complete": True, "configuration": self.tag,
            "p": 41, "original_map_index": 4, "original_map_degree": "1206",
            "point_status": point["point_status"], "common_zero_order": point["common_zero_order"],
            "actual_beta_C_computed": True, "actual_real_descent_image_computed": True,
            "original_A_coordinate_lift_computed": False, "actual_heights_or_uniformity_computed": False,
            "original_M2_scale": "6724", "original_power5_scale": "13744803133596058624",
            "original_h0_nonzero": True, "original_Galois_direction_input_verified": True,
            "quotient_derivative_independently_compared": point["quotient_derivative_independently_compared"],
            "actual_R824_relation": relation_adapter.plain(self.config["relation_spec"]),
            "original_R824_free_column": self.actual_relation.free_column,
            "original_y_ratio_preserved": True,
            "original_R787_reserved_target_recomputed": False,
            "synthetic_R787_producer_or_relation_file_created": False,
            "original_R824_denominator_and_content_reinserted": False,
            "relation_source_receipt": file_spec(self.path(SOURCE_STAGE)),
            "section_jet_stage": file_spec(self.path("R792-original-composed-section-jets")),
            "point_stage": file_spec(self.path("R792-original-beta-C-and-real-descent-point")),
            "stage_manifest": file_spec(self.path(manifest_name)),
            "seconds": time.monotonic()-self.started,
        }
        save(self.out/FINAL, certificate)
        save(self.out/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "beta_framework_sha256": FRAMEWORK_SHA, "relation_adapter_sha256": ADAPTER_SHA,
            "certificate_sha256": sha(self.out/FINAL),
            "actual_beta_C_computed": True, "actual_real_descent_image_computed": True,
            "original_A_coordinate_lift_computed": False, "actual_heights_or_uniformity_computed": False})
        return 0


def main():
    beta.guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "proof", "method", "field-core", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    try:
        return Job(args).run()
    except beta.BudgetStop as error:
        args.output.mkdir(parents=True, exist_ok=True)
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "budget_stop": str(error), "completed_source_bound_stages_preserved": True})
        return 124
    except BaseException as error:
        args.output.mkdir(parents=True, exist_ok=True)
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "error": type(error).__name__+": "+str(error),
            "completed_source_bound_stages_preserved": True})
        raise


if __name__ == "__main__":
    raise SystemExit(main())
