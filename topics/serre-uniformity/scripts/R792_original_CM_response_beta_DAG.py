#!/usr/bin/env python3
"""Source-bound original beta_C and f_R(c1), as exact arithmetic DAGs.

This consumes the completed implicit four responses.  It does not reconstruct
their rational coordinates or recompute CM traces, Hom maps, or point roots.
All newly generated mathematical expressions belong to public Actions.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time

RESULT = "R792-original-CM-response-beta-DAG"
FINAL = "p41-original-CM-response-beta-DAG-certificate.json"
PREFIX = "R792-CM-DAG-"
MANIFEST = "full-outputs-manifest.json"
CM_CERT = "p41-original-implicit-CM-value-certificate.json"
HOM_CERT = "p41-original-Hom-Galois-and-eta-input-certificate.json"
TANGENTS = "R791-original-twelve-CM-tangents.json.gz"
HOM = "R791-original-Hom-Galois-matrices.json.gz"
DESCENT = "R791-original-real-descent-and-eta-basis-inputs.json.gz"
PINS = {
    CM_CERT: "5de210b5ebb2a8a7fefcc8799888a68353c9c2ac10725fafa239d2bd1082d20c",
    HOM_CERT: "94429377ebd63ff8bdcb9fd1d9468fc2e28e981db2b10b8c494d15c05e073d46",
    TANGENTS: "32be372f46560ce7cfc0af40666cdc32b39170bfc7b6ec32b92ea747a0629e7e",
    HOM: "f3793ddc7680b718a4448d45587661182986a3558db346ad0a2c9031c8952183",
    DESCENT: "24a894163f136a4e8c71b117e373f8fafb66a6e0c94b4efe3f141f78bb39b968"}
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256",
        "configuration_sha256", "selected_files_sha256")
STRATEGY = {
    "existing_formula": "R791(791R.16), with R792(792.7) and the original nonzero h0",
    "point": "beta_C=f4(c1) in C(L): y^2=x^3+b; degree1206; f4(c0)=O",
    "coordinate": "z=a-1 at original c1=4424",
    "exact_response_semantics": "unit-chart linear functionals, never the modular response arrays",
    "nonzero_denominators": "B0 from completed modular witness; Q,N from original geometry",
    "output_representation": "content-addressed exact arithmetic DAG with proof-bound inverse nodes",
    "primitive_descent": "f_R(c1)=[1-zeta^2]f4(c1), original v and kappa retained",
    "numerical_expansion_or_root_search": False,
    "old_CM_Hom_or_Norm_arithmetic_recomputed": False,
    "point_additions_eta_or_heights_in_scope": False}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical expressions belong to public repository Actions.")


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


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    data = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(data)
    else:
        temporary.write_bytes(data)
    temporary.replace(path)


def plain(row):
    answer = {key: row[key] for key in ("file", "bytes", "sha256")}
    assert Path(answer["file"]).name == answer["file"] and "\\" not in answer["file"]
    assert isinstance(answer["bytes"], int) and answer["bytes"] >= 0
    assert len(answer["sha256"]) == 64
    return answer


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


class BudgetStop(Exception):
    pass


class Source:
    def __init__(self, label, item, root):
        self.label, self.item, self.root = label, item, Path(root)/label
        mp = self.root/MANIFEST
        assert mp.stat().st_size == item["manifest_bytes"] and sha(mp) == item["manifest_sha256"]
        manifest = read(mp)
        assert manifest["result"] == item["result"]
        inventory = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(inventory) == len(manifest["files"]) == item["manifest_file_count"]
        inventory[MANIFEST] = spec(mp)
        self.files = {name: plain(row) for name, row in item["files"].items()}
        assert fingerprint([self.files[name] for name in sorted(self.files)]) == item["selected_files_sha256"]
        for name, row in self.files.items():
            assert row == inventory[name]
            self.bound(row)
        self.certificate = self.get(item["certificate"]["file"])
        assert self.files[item["certificate"]["file"]] == plain(item["certificate"])
        self.tag = self.certificate["configuration"]
        assert self.certificate["complete"] is True and self.certificate["result"] == item["result"]
        assert fingerprint(self.tag) == item["configuration_sha256"]
        assert self.tag["source_sha256"] == item["core_sha256"]
        run, receipt, public = (self.get(name) for name in ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        assert run["source_commit"] == public["source_commit"] == item["source_commit"]
        assert run["result"] == receipt["result"] == public["result"] == item["result"]
        assert run["complete"] is True and run["process_exit_code"] == 0 and run.get("error") is None
        assert receipt["complete"] is True and receipt["source_sha256"] == item["core_sha256"]
        assert public.get("core_sha256", public["job"]["core_sha256"]) == item["core_sha256"]
        assert receipt["certificate_sha256"] == item["certificate"]["sha256"]
        self.identity = {key: item[key] for key in BASE}
        self.identity["certificate"] = plain(item["certificate"])

    def bound(self, row):
        row = plain(row)
        path = self.root/row["file"]
        assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        return path

    def get(self, name):
        return read(self.bound(self.files[name]))

    def stage(self, row):
        row = plain(row)
        assert self.files[row["file"]] == row
        value = read(self.bound(row))
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def ref(self, name):
        return {"source_group": self.label, **self.files[name]}


class Program:
    """A deterministic straight-line program, not a formal-zero oracle."""
    def __init__(self):
        self.nodes, self.known = [], {}

    def node(self, operation, inputs=(), **data):
        inputs = list(inputs)
        assert all(value in self.known for value in inputs)
        payload = {"operation": operation, "inputs": inputs, **data}
        identity = fingerprint(payload)
        if identity not in self.known:
            self.known[identity] = payload
            self.nodes.append({"id": identity, **payload})
        else:
            assert self.known[identity] == payload
        return identity

    def rational(self, value):
        return self.node("rational", numerator=str(value), denominator="1")

    def add(self, a, b):
        return self.node("add", (a, b))

    def mul(self, a, b):
        return self.node("multiply", (a, b))

    def neg(self, a):
        return self.node("negate", (a,))

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def inverse(self, a, proof):
        return self.node("inverse", (a,), nonzero_certificate=proof)


def evaluate_program(program, arithmetic, exact_leaf):
    """Backend-neutral evaluator for a downstream explicit exact field adapter.

    The caller must supply certified exact leaves.  Modular values and RR
    suggestions must not be passed as such leaves.  This first scope does not
    invoke the evaluator or claim an expanded value.
    """
    if arithmetic.value_semantics != "exact-original-L-elements":
        raise ValueError("An exact field backend is required, not modular candidates.")
    values = {}
    for node in program["nodes"]:
        payload = {key: value for key, value in node.items() if key != "id"}
        assert fingerprint(payload) == node["id"]
        args = [values[key] for key in node["inputs"]]
        op = node["operation"]
        if op == "rational":
            value = arithmetic.rational(int(node["numerator"]), int(node["denominator"]))
        elif op == "add":
            value = arithmetic.add(*args)
        elif op == "multiply":
            value = arithmetic.multiply(*args)
        elif op == "negate":
            value = arithmetic.negate(*args)
        elif op == "inverse":
            value = arithmetic.inverse(args[0], node["nonzero_certificate"])
        else:
            value = exact_leaf(node, args)
        values[node["id"]] = value
    return {key: values[node] for key, node in program["roots"].items()}


class Job:
    def __init__(self, args):
        self.args, self.started = args, time.monotonic()
        self.config, self.out = read(args.config), Path(args.output)
        self.out.mkdir(parents=True, exist_ok=True)
        c = self.config
        assert c["result"] == RESULT and c["p"] == 41
        assert c["core_sha256"] == sha(__file__)
        assert 0 < args.budget_minutes <= 300
        assert set(c["sources"]) == {"CM", "R791"}
        for item in c["proofs"].values():
            path = (Path(args.topic)/item["path"]).resolve()
            assert path.is_relative_to(Path(args.topic).resolve()) and sha(path) == item["sha256"]
        self.sources = {label: Source(label, item, args.retained) for label, item in c["sources"].items()}
        self.tag = {"result": RESULT, "source_sha256": c["core_sha256"], "p": 41,
            "proofs": c["proofs"], "source_identities": {key: value.identity for key, value in self.sources.items()},
            "strategy": STRATEGY, "arithmetic": "source-bound exact symbolic DAG; no coordinate reconstruction",
            "budget_excluded_from_mathematical_identity": True}
        self.prepare_sources()

    def budget(self):
        if time.monotonic()-self.started > self.args.budget_minutes*60:
            raise BudgetStop("completed exact-expression stages retained")

    def path(self, name):
        return self.out/(PREFIX+name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def store(self, name, value):
        self.budget()
        value = {"complete": True, "configuration": self.tag, **value}
        save(self.path(name), value)
        return value

    def ref(self, name):
        return spec(self.path(name))

    def prepare_sources(self):
        cm, h = self.sources["CM"], self.sources["R791"]
        assert cm.item["certificate"]["sha256"] == PINS[CM_CERT]
        assert h.item["certificate"]["sha256"] == PINS[HOM_CERT]
        cf, hf = cm.certificate, h.certificate
        assert cf["original_map_index"] == 4 and cf["original_map_degree"] == "1206"
        assert cf["source_Dixon_digits"] == 518 and cf["new_Dixon_digits_computed"] == 0
        for flag in ("all_14_branches_units", "characteristic_zero_B0_nonzero_certified",
                     "exact_implicit_relation_defined", "exact_finite_y_implicit_expression_defined"):
            assert cf[flag] is True
        for flag in ("expanded_coordinates_exactly_certified", "actual_beta_point_eta_or_height_computed",
                     "old_R792_success_recipe_produced"):
            assert cf[flag] is False
        self.expression = cm.stage(cf["implicit_expression"])
        self.witness = cm.stage(cf["denominator_unit_witness"])
        assert self.expression["proof_sha256"] == self.config["proofs"]["unit_chart"]["sha256"]
        assert self.expression["unit_chart_solve"]["shape"] == [2420, 2420]
        assert self.expression["unit_chart_solve"]["free_column"] == 1186
        assert self.expression["original_relation_exactly_defined_by_unit_chart"] is True
        assert self.expression["original_finite_CM_y_expression_defined"] is True
        assert self.witness["all_14_branches_units"] is True
        assert self.witness["characteristic_zero_B0_nonzero_certified"] is True
        assert self.witness["nonzero_branch_indices"] == list(range(14))
        assert len(self.witness["B0_values_at_original_14_branches"]) == 14
        assert all(value != 0 for value in self.witness["B0_values_at_original_14_branches"])
        assert self.witness["modular_zero_claimed_to_prove_characteristic_zero_zero"] is False
        self.jets = cm.stage(cf["power5_CM_values_and_jets"])
        self.ez = cm.stage(cf["exact_eZ"])
        assert self.jets["dimension"] == 1234 and self.jets["derivative_order"] == 1
        assert self.jets["integer_scale"] == self.ez["integer_scale"] == "13744803133596058624"
        assert self.jets["original_M2_scale"] == "6724" and self.jets["original_basis_order"] is True
        assert self.ez["columns"] == 1214 and self.ez["eZ_computed_in_characteristic_zero"] is True
        for row in self.jets["completed_blocks"]+self.ez["blocks"]:
            cm.stage(row)
        for key in ("A_response", "B_response", "modular_value", "source_audit"):
            cm.stage(cf[key])
        assert cm.stage(cf["modular_value"])["all14_original_quotient_identities_verified"] is True
        assert hf["original_index4_c1_tangent_nonzero"] is True
        assert hf["selected_real_map_recipe"] == "f+c(f)" and hf["selected_real_map_degree"] == "3618"
        stages = {row["file"]: plain(row) for row in hf["stages"]}
        for name in (TANGENTS, HOM, DESCENT):
            assert stages[name]["sha256"] == PINS[name]
        self.tangents = h.stage(stages[TANGENTS])
        self.hom = h.stage(stages[HOM])
        self.descent = h.stage(stages[DESCENT])
        assert self.tangents["original_map_index"] == 4 and self.tangents["original_map_degree"] == "1206"
        assert self.tangents["coordinate"] == "s=a-1 at the original c1"
        assert self.tangents["original_c1_slash_count"] == 1
        assert self.tangents["original_map_c1_tangent_nonzero"] is True and self.tangents["zero_flags"][4] is False
        self.h0 = self.tangents["actual_L_coefficients_h_i_over_ds_at_c1"][4]
        assert len(self.h0) == 2
        for block in self.h0:
            assert len(block["numerator"]) == 7 and int(block["denominator"]) > 0
        assert self.hom["gamma_order"] == 21
        assert self.hom["all_84_coordinates_verified"] is True
        assert self.hom["all_three_actions_integral_unimodular"] is True
        assert self.descent["original_vdagger_v_replaced_by_scalar"] is False
        assert self.descent["unknown_original_kappa_set_to_one"] is False
        assert self.descent["selected_real_map_recipe"] == "f+c(f)"
        assert h.tag["retained_inputs"]["p41-original-CM-model-certificate.json"] == \
            "752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574"
        if not self.cached("source-audit"):
            self.store("source-audit", {"source_identities": self.tag["source_identities"],
                "exact_expression": cm.ref(cf["implicit_expression"]["file"]),
                "power5_CM_values_and_jets": cm.ref(cf["power5_CM_values_and_jets"]["file"]),
                "exact_eZ": cm.ref(cf["exact_eZ"]["file"]),
                "modular_responses_are_not_exact_expanded_leaves": True,
                "original_h0": h.ref(TANGENTS), "original_Hom_and_transport": h.ref(HOM),
                "original_descent_and_polarization": h.ref(DESCENT),
                "old_CM_Hom_Norm_or_relation_arithmetic_recomputed": False})

    def nonzero_proofs(self):
        old = self.cached("nonzero-denominator-proofs")
        if old:
            return old
        cm, h = self.sources["CM"], self.sources["R791"]
        return self.store("nonzero-denominator-proofs", {"scope": "the actual finite beta_C=f4(c1)",
            "rules": {
                "B0": {"rule": "nonzero reduction of the original characteristic-zero response",
                    "source": cm.ref(cm.certificate["denominator_unit_witness"]["file"]), "all14_units": True},
                "h0": {"rule": "original completed nonzero tangent", "source": h.ref(TANGENTS), "index": 4},
                "Q": {"rule": "Q=B0^2*(y0^2-b), with R792(792.7): y0=s*v0 and b>0 at specified real embedding",
                    "dependencies": ["B0"], "proof": self.config["proofs"]["R792"],
                    "uses_all_embeddings_real": False, "uses_expanded_coordinates": False},
                "N": {"rule": "N=B0^2*y0_prime; dy=3*x^2*omega, x^3=y0^2-b, h0 nonzero",
                    "dependencies": ["B0", "Q", "h0"], "proof": self.config["proofs"]["R791"],
                    "existing_formula": "791R.16", "valid_when_y0_is_zero": True},
                "s": {"rule": "s^2=-3 in characteristic zero"}},
            "inverse_proofs_do_not_assert_auxiliary_or_original_p_units": True,
            "general_DAG_zero_oracle_claimed": False})

    def program(self):
        old = self.cached("original-point-program")
        if old:
            return old
        cm, h = self.sources["CM"], self.sources["R791"]
        p = Program()
        b = p.node("original_field_generator", name="b", exact_field_source=cm.ref(cm.certificate["implicit_expression"]["file"]))
        zeta = p.node("original_field_generator", name="zeta", minimal_polynomial_ascending=["1", "1", "1"])
        one, two, three, nine = (p.rational(i) for i in (1, 2, 3, 9))
        s = p.add(one, p.mul(two, zeta))
        solve = p.node("unit_chart_solve", exact_recipe_source=cm.ref(cm.certificate["implicit_expression"]["file"]),
            shape=[2420, 2420], free_column=1186, output_semantics="exact-original-L-vector",
            original_129_by_280_relation_identity="unit-chart proof U.1, same normalized direction")
        responses = {key: p.node("linear_response", (solve,), response=key,
            functional=self.expression["linear_responses"][key],
            accurate_local_rows={"e0_e1": cm.ref(cm.certificate["power5_CM_values_and_jets"]["file"]),
                                "e0Z_e1Z": cm.ref(cm.certificate["exact_eZ"]["file"])})
            for key in ("A0", "A1", "B0", "B1")}
        h0 = p.node("source_field_element", source=h.ref(TANGENTS),
            source_key="actual_L_coefficients_h_i_over_ds_at_c1", source_index=4,
            exact_value=self.h0, exact_encoding="two polynomials in original b, first 1 then zeta; rational denominators",
            no_extra_c1_phase=True)
        a0, a1, b0, b1 = (responses[key] for key in ("A0", "A1", "B0", "B1"))
        a02, b02 = p.mul(a0, a0), p.mul(b0, b0)
        Q = p.sub(a02, p.mul(b, b02))
        N = p.sub(p.mul(a1, b0), p.mul(a0, b1))
        proof = self.ref("nonzero-denominator-proofs")
        invB = p.inverse(b0, {**proof, "rule_key": "B0"})
        invQ = p.inverse(Q, {**proof, "rule_key": "Q"})
        invN = p.inverse(N, {**proof, "rule_key": "N"})
        invs = p.inverse(s, {**proof, "rule_key": "s"})
        third = p.node("rational", numerator="1", denominator="3")
        y = p.mul(a0, invB)
        dy = p.mul(N, p.mul(invB, invB))
        x = p.mul(p.mul(three, p.mul(h0, Q)), invN)
        xr = p.neg(p.mul(p.mul(zeta, h0), p.mul(p.add(a02, p.mul(three, p.mul(b, b02))), invN)))
        yr = p.mul(p.mul(a0, p.sub(a02, p.mul(nine, p.mul(b, b02)))), p.mul(third, p.mul(invs, p.mul(invB, invQ))))
        roots = {"beta_C_x": x, "beta_C_y": y, "derivative_z_y": dy,
                 "f_R_c1_x": xr, "f_R_c1_y": yr, "Q": Q, "N": N, "h0": h0, "b": b, "zeta": zeta,
                 "unique_Fb_cube_root_u0": p.mul(zeta, x), "anti_real_y_coefficient_v0": p.mul(y, invs)}
        assert len({node["id"] for node in p.nodes}) == len(p.nodes)
        return self.store("original-point-program", {"format": "original-L-arithmetic-DAG-v1", "nodes": p.nodes,
            "roots": roots, "exact_response_leaves": responses, "node_count": len(p.nodes),
            "original_field_source": cm.ref(cm.certificate["implicit_expression"]["file"]),
            "proof_application": {"x_formula": "R791(791R.16), written as 3*h0*Q/N",
                "finite_point_and_direction": "R792(792.2)-(792.7)",
                "real_descent": "R791(791R.3)-(791R.6); alpha3=1-zeta^2; alpha3^3=3s"},
            "curve_identity_as_original_map_proved": True,
            "curve_identity_verified_from_expanded_coordinates": False,
            "exact_original_beta_C_as_expression_certified": True,
            "exact_original_descent_point_as_expression_certified": True,
            "expanded_coordinates_exactly_certified": False,
            "original_abstract_A_coordinate_preimage_recovered": False,
            "point_at_infinity": False, "new_root_search_or_norm_computation": False})

    def downstream(self):
        old = self.cached("downstream-source-and-zero-obligations")
        if old:
            return old
        h = self.sources["R791"]
        return self.store("downstream-source-and-zero-obligations", {
            "actual_point": "beta_C=f4(c1)", "actual_descent_point": "f_R(c1)",
            "primitive_model_point_semantics": "q_R[c1-c0]=v*beta, using actual transported Weil components",
            "original_kappa_times_vdagger_v": self.descent["kappa_times_vdagger_v_in_real_Chebyshev_basis"],
            "original_scale_source": h.ref(DESCENT),
            "kappa_or_vdagger_v_set_to_one": False, "original_abstract_A_coordinate_preimage_recovered": False,
            "Galois_transport": {"source": h.ref(HOM), "rule": "T^j(x,y)=(rho_j^-2*sigma^j(x),rho_j^-3*sigma^j(y))",
                "all_coefficients_and_unit_chart_rows_transport": True, "T_seventh_power": "[zeta^2]",
                "Galois_or_Hom_matrices_recomputed": False},
            "point_additions_executed": False,
            "later_zero_decisions": ["point is O", "x(P)-x(Q)", "y(P)+y(Q)", "y(P)", "chosen projective chart denominator"],
            "permitted_zero_certificates": ["actual Hom identity", "proved original field or conjugation identity",
                "exact bordered determinant or row-space zero", "exactly certified expanded coordinates"],
            "modular_nonzero_can_certify_nonzero": True, "modular_zero_can_certify_exact_zero": False,
            "nonzero_Hom_implies_nonzero_value_at_c1": False,
            "eta_requires_global_polar_divisors_and_rigidification": True,
            "height_requires_original_polarization_splitting_and_period_data": True,
            "actual_eta_or_height_computed": False})

    def finish(self):
        records = [spec(path) for path in sorted(self.out.glob(PREFIX+"*.json.gz"))
                   if not path.name.startswith(PREFIX+"stage-manifest-")]
        for row in records:
            data = read(self.out/row["file"])
            assert data["complete"] is True and data["configuration"] == self.tag
        name = "stage-manifest-"+fingerprint(records)[:24]
        save(self.path(name), {"complete": True, "configuration": self.tag, "files": records})
        answer = {"result": RESULT, "complete": True, "configuration": self.tag, "p": 41,
            "original_map_index": 4, "original_map_degree": "1206", "original_c1_coordinate": "z=a-1",
            "source_audit": self.ref("source-audit"), "denominator_nonzero_proofs": self.ref("nonzero-denominator-proofs"),
            "original_point_DAG": self.ref("original-point-program"),
            "downstream_interface": self.ref("downstream-source-and-zero-obligations"),
            "exact_original_beta_C_as_expression_certified": True,
            "exact_original_descent_point_as_expression_certified": True,
            "expanded_coordinates_exactly_certified": False,
            "old_R792_expanded_coordinate_recipe_produced": False,
            "original_abstract_A_coordinate_preimage_recovered": False,
            "actual_eta_or_height_computed": False, "new_CM_Hom_root_or_Norm_arithmetic": False,
            "stage_manifest": self.ref(name), "seconds": time.monotonic()-self.started}
        save(self.out/FINAL, answer)
        print("BETA_DAG_RESULT="+json.dumps({key: answer[key] for key in ("complete", "exact_original_beta_C_as_expression_certified",
            "exact_original_descent_point_as_expression_certified", "expanded_coordinates_exactly_certified",
            "original_abstract_A_coordinate_preimage_recovered", "actual_eta_or_height_computed", "seconds")}), flush=True)
        return answer

    def run(self):
        if (self.out/FINAL).exists():
            value = read(self.out/FINAL)
            assert value["complete"] is True and value["configuration"] == self.tag
            return value
        self.nonzero_proofs()
        self.program()
        self.downstream()
        return self.finish()


def main():
    guard()
    parser = argparse.ArgumentParser()
    for name in ("config", "topic", "retained", "output"):
        parser.add_argument("--"+name, required=True)
    parser.add_argument("--budget-minutes", type=float, default=30)
    args = parser.parse_args()
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    started, result, error, code = time.monotonic(), None, None, 0
    try:
        result = Job(args).run()
    except BudgetStop as exc:
        error, code = "BudgetStop: "+str(exc), 124
    except Exception as exc:
        import traceback
        traceback.print_exc()
        error, code = type(exc).__name__+": "+str(exc), 1
    receipt = {"result": RESULT, "source_sha256": sha(__file__), "complete": result is not None,
        "error": error, "seconds": time.monotonic()-started,
        "certificate_sha256": sha(output/FINAL) if result is not None else None,
        "expanded_coordinates_exactly_certified": False, "all_completed_stages_preserved": True}
    save(output/"core-receipt.json", receipt)
    print("CORE_RECEIPT="+json.dumps(receipt), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
