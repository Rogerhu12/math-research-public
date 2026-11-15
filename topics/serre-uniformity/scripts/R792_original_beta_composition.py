#!/usr/bin/env python3
"""R792: compose the original CM point from source-bound completed producers.

New arithmetic is restricted to the public repository's GitHub Actions.
No periods, Laurent recurrences, basis selection, or CM traces are recomputed.
The original A-coordinate lift across the comparison isogeny is not claimed.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpq_mat, fmpq_poly

RESULT = "R792-original-beta-composition"
FINAL = "p41-original-beta-composition-certificate.json"
FIELD_CORE_SHA = "f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251"
R786_PROOF_SHA = "c46008726fb18f52a5430b72c4994ce76164f11bea51044f1677278294f7011d"
R787_METHOD_SHA = "1d91bfc7bdf61c40c4deda19833a5f50491630a61a7a25feb7a3a1e0b451204b"
R790_PROOF_SHA = "83303dcd6abc65875d8c67eb8977126db1c85cf3e9dafb3fbd2881163aadfc39"
MODEL = "p41-original-CM-model-certificate.json"
MODEL_SHA = "752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574"
R786_CERT_SHA = "dc6c23568f80b861d839280846c3250063abdfb2716a20481779816bb7cd37d9"
R786_INDEX_SHA = "0bb7cfeda48d6759f1553dec74485a28dc16e31cf3d500a095963888973c9b35"
R791_CERT_SHA = "94429377ebd63ff8bdcb9fd1d9468fc2e28e981db2b10b8c494d15c05e073d46"
TANGENTS = "R791-original-twelve-CM-tangents.json.gz"
TANGENTS_SHA = "32be372f46560ce7cfc0af40666cdc32b39170bfc7b6ec32b92ea747a0629e7e"
HOM = "R791-original-Hom-Galois-matrices.json.gz"
HOM_SHA = "f3793ddc7680b718a4448d45587661182986a3558db346ad0a2c9031c8952183"
BASIS_FILES = {
    1: ("R775-basis-M2.json.gz", "51113988c90b301cb6117fec5c294b77110e1826bf00229b7993ba82144f5d3d"),
    2: ("R775-basis-power-2.json.gz", "734a61e967c51ba3c9cd93eaff1a81fba165600110abb941dfdbbeed41b6ebe4"),
    3: ("R775-basis-power-3.json.gz", "00361e5155c429de5c54b613b8a3cb46ac9530c554e1a812823748bb2bf5fe18"),
    4: ("R775-basis-power-4.json.gz", "85beb7662eee64f4eca9e205314a6625506e3041bea199985489c7cf1f62dd4e"),
    5: ("R775-basis-power-5.json.gz", "7aff6faa89a91649db5549bbf9360647534bff6f9586ce3f5963e322d33c30ba"),
}
DIMENSIONS = {1: 146, 2: 418, 3: 690, 4: 962, 5: 1234}
GROUP_RESULTS = {
    "R735": "R732-p41-original-CM-model",
    "R775": "R775-p41-original-K-defined-RR-bases",
    "R786": "R786-exact-original-power5-short-basis",
    "R787": "R787-original-power5-function-relation",
    "R790": "R790-original-CM-fiber-jets",
    "R791": "R791-original-Hom-Galois-and-eta-inputs",
}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New exact arithmetic belongs to public repository Actions.")


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    raw = (json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"))+"\n").encode("utf-8")
    if path.suffix == ".gz":
        with temporary.open("wb") as stream:
            with gzip.GzipFile(filename="", fileobj=stream, mode="wb",
                               mtime=0, compresslevel=2) as compressed:
                compressed.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def rational(value):
    return [str(value.numer()), str(value.denom())]


def rational_polynomial(poly):
    return [rational(poly[i]) for i in range(poly.degree()+1)]


def conjugate(value):
    return value.F.elt(value.a-value.b, -value.b)


def same_producer(left, right):
    # A later consumer may retain more files from the same completed artifact.
    for key in ("result", "run_id", "source_commit", "core_sha256",
                "manifest_sha256", "certificate_name"):
        assert left[key] == right[key], "Changed producer identity: "+key
    name = left["certificate_name"]
    assert left["files"][name] == right["files"][name]


class Retained:
    def __init__(self, root, label, spec):
        self.directory, self.spec, self.label = Path(root)/label, spec, label
        mp = self.directory/"full-outputs-manifest.json"
        assert sha(mp) == spec["manifest_sha256"]
        manifest = read(mp)
        assert manifest["result"] == spec["result"] == GROUP_RESULTS[label]
        self.files = {row["file"]: row for row in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        run = self.raw("run-receipt.json")
        core = self.raw("core-receipt.json")
        initial = self.raw("public-actions-input.json")
        assert run["result"] == spec["result"] and run["complete"] is True
        assert run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(spec["run_id"])
        assert run["source_commit"] == spec["source_commit"]
        if label == "R791":
            # Its original runner records both files in the authenticated
            # manifest but has no direct core-receipt hash in the run receipt.
            assert "core_receipt_sha256" not in run
        else:
            assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["source_commit"] == spec["source_commit"]
        if label == "R791":
            assert initial["job"]["core_sha256"] == spec["core_sha256"]
        else:
            assert initial["core_sha256"] == spec["core_sha256"]
        self.certificate = self.raw(spec["certificate_name"])
        self.certificate_sha = self.files[spec["certificate_name"]]["sha256"]
        assert self.certificate_sha == spec["files"][spec["certificate_name"]]
        assert core["certificate_sha256"] == self.certificate_sha
        assert self.certificate["complete"] is True
        if label == "R735":
            self.tag = None
            identity = self.certificate["identity"]
            assert identity["source_sha256"] == spec["core_sha256"]
            assert identity["p"] == 41 and identity["python_flint"] == "0.9.0"
            assert self.certificate_sha == MODEL_SHA
        else:
            assert self.certificate["result"] == spec["result"]
            self.tag = self.certificate["configuration"]
            assert self.tag["source_sha256"] == spec["core_sha256"]
            assert self.tag["python_flint"] == "0.9.0"

    def raw(self, name, expected=None):
        assert Path(name).name == name
        row = self.files[name]
        if expected is not None:
            assert row["sha256"] == expected
        if name in self.spec["files"]:
            assert row["sha256"] == self.spec["files"][name]
        path = self.directory/name
        assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        return read(path)

    def get(self, name, expected=None):
        value = self.raw(name, expected)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def get_spec(self, spec):
        name = spec["file"]
        assert self.files[name]["bytes"] == spec["bytes"]
        return self.get(name, spec["sha256"])


class BudgetStop(RuntimeError):
    pass


def polynomial_trim(poly):
    poly = list(poly)
    while poly and not poly[-1]:
        poly.pop()
    return poly


def polynomial_remainder(left, right):
    left, right = polynomial_trim(left), polynomial_trim(right)
    assert right
    inverse = right[-1].inverse()
    while len(left) >= len(right):
        factor, shift = left[-1]*inverse, len(left)-len(right)
        for i, value in enumerate(right):
            left[i+shift] -= factor*value
        left = polynomial_trim(left)
    return left


def polynomial_gcd(left, right):
    left, right = polynomial_trim(left), polynomial_trim(right)
    while right:
        left, right = right, polynomial_remainder(left, right)
    assert left
    inverse = left[-1].inverse()
    return [value*inverse for value in left]


class Job:
    def __init__(self, args):
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        assert flint.__version__ == "0.9.0"
        self.config = read(args.config)
        assert self.config["producer_inputs_pending"] is False
        assert self.config["result"] == RESULT and self.config["p"] == 41
        assert self.config["core_sha256"] == sha(__file__)
        assert self.config["coarse_jet_order"] == 1
        assert sha(args.proof) == self.config["R792_proof_sha256"]
        assert sha(args.field_core) == self.config["field_core_sha256"] == FIELD_CORE_SHA
        module_spec = importlib.util.spec_from_file_location("retained_R754", args.field_core)
        self.module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(self.module)
        assert set(self.config["retained_artifacts"]) == set(GROUP_RESULTS)
        self.inputs = {label: Retained(args.retained, label, producer)
                       for label, producer in self.config["retained_artifacts"].items()}
        model = self.inputs["R735"].certificate
        self.L = self.module.QKField(self.module.dp(model["minimal_polynomial"]))
        assert self.L.degree == 7
        self.b, self.zeta = self.L.gen, self.L.zeta
        self.s = 1+2*self.zeta
        self.tag = {"result": RESULT, "source_sha256": sha(__file__),
            "python_flint": flint.__version__, "R792_proof_sha256": sha(args.proof),
            "field_core_sha256": FIELD_CORE_SHA, "coarse_jet_order": 1,
            "retained_artifacts": self.config["retained_artifacts"],
            "original_map_index": 4, "original_map_degree": "1206"}
        self.prepare_relation_and_recipes(model)
        self.prepare_original_direction()

    def budget(self):
        if time.monotonic()-self.started > self.args.budget_minutes*60:
            raise BudgetStop("Completed source-bound composition stages retained.")

    def path(self, name):
        assert name.startswith("R792-") and Path(name).name == name
        return self.out/(name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def store(self, name, value):
        value = dict(value, complete=True, configuration=self.tag)
        save(self.path(name), value)
        print(json.dumps({"stage": name, "complete": True,
                          "seconds": round(time.monotonic()-self.started, 3)}), flush=True)
        return value

    def prepare_relation_and_recipes(self, model):
        r775, r786, r787, r790 = (self.inputs[key] for key in ("R775", "R786", "R787", "R790"))
        cert = r787.certificate
        assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
        assert cert["actual_y_map_recovered"] is True
        assert cert["exact_nonzero_A_B_relation_verified"] is True
        assert cert["original_full_L_retained"] is True
        assert cert["exact_verified_Laurent_exponents"] == [-1, 127]
        assert cert["exact_verified_orders"] == 129
        assert cert["exact_verified_t_coordinates"] == 20
        assert cert["exact_verified_Q_coordinates_per_order"] == 280
        assert r787.tag["R786_proof_sha256"] == R786_PROOF_SHA
        assert r787.tag["R787_method_sha256"] == R787_METHOD_SHA
        self.relation = r787.get_spec(cert["relation_spec"])
        assert cert["relation_spec"]["file"] == "R787-original-function-recipe.json.gz"
        for flag in ("exact_original_A_equals_yB", "B_nonzero", "full_129_original_relations_verified",
                     "original_R786_basis_order"):
            assert self.relation[flag] is True
        assert self.relation["candidate_only_until_full_exact_verification"] is False
        assert self.relation["L_basis"] == "B^i*s^j, j=0..1 outer, i=0..6; B=lambda*b"
        assert self.relation["field"] == r787.tag["field"]
        assert self.relation["field"]["original_b_minimal_polynomial"] == model["minimal_polynomial"]
        assert self.relation["field"]["original_b_replaced_by_another_twist"] is False
        self.lam = int(self.relation["field"]["lambda"])
        assert self.lam > 0
        same_producer(self.relation["R786_producer"], r786.spec)
        assert self.relation["R786_producer"] == r787.tag["retained_artifacts"]["R786"]
        assert r786.certificate_sha == R786_CERT_SHA
        assert r786.tag["R786_proof_sha256"] == R786_PROOF_SHA
        assert r786.certificate["basis_in_original_R775_saved_order"] is True
        assert r786.certificate["exact_power5_basis_dimension"] == 1234
        assert self.relation["R786_basis_index"] == r786.certificate["basis_index"]
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

    def decode_K(self, value):
        assert len(value) == 2 and all(len(pair) == 2 for pair in value)
        assert all(int(pair[1]) > 0 for pair in value)
        return self.L.elt(*(fmpq(int(pair[0]), int(pair[1])) for pair in value))

    def prepare_original_direction(self):
        producer = self.inputs["R791"]
        assert producer.certificate_sha == R791_CERT_SHA
        assert producer.tag["field_helper_sha256"] == FIELD_CORE_SHA
        assert producer.tag["retained_inputs"][MODEL] == MODEL_SHA
        assert producer.certificate["original_index4_c1_tangent_nonzero"] is True
        stages = {row["file"]: row for row in producer.certificate["stages"]}
        assert stages[TANGENTS]["sha256"] == TANGENTS_SHA
        assert stages[HOM]["sha256"] == HOM_SHA
        tangent = producer.get_spec(stages[TANGENTS])
        assert tangent["original_map_index"] == 4 and tangent["original_map_degree"] == "1206"
        assert tangent["coordinate"] == "s=a-1 at the original c1"
        assert tangent["original_c1_slash_count"] == 1
        assert tangent["original_map_c1_tangent_nonzero"] is True
        self.h0 = self.L.decode(tangent["actual_L_coefficients_h_i_over_ds_at_c1"][4])
        assert self.h0 and tangent["zero_flags"][4] is False
        hom = producer.get_spec(stages[HOM])
        assert hom["all_84_coordinates_verified"] is True
        assert hom["all_three_actions_integral_unimodular"] is True
        R = [[int(value) for value in row] for row in hom["complex_conjugation_matrix"]]
        J = [[int(value) for value in row] for row in hom["zeta_matrix"]]
        assert len(R) == len(J) == 12 and all(len(row) == 12 for row in R+J)
        # Validate the retained column relation; do not recompute either action.
        assert all(R[i][4] == -sum(J[i][k]*J[k][4] for k in range(12)) for i in range(12))
        assert conjugate(self.h0) == -(self.zeta**2)*self.h0

    def section_jets(self):
        name = "R792-original-composed-section-jets"
        prior = self.cached(name)
        if prior:
            return tuple(self.L.decode(prior[key]) for key in ("A0", "A1", "B0", "B1"))
        cache = {(1, index): pair for index, pair in enumerate(self.m2)}

        def product(power, index):
            key = power, index
            if key in cache:
                return cache[key]
            self.budget()
            assert 2 <= power <= 5 and 0 <= index < DIMENSIONS[power]
            recipe = self.recipes[power][index]
            assert recipe["kind"] == "product"
            k, ell = recipe["left_power"], recipe["right_power"]
            i, j = recipe["left_index"], recipe["right_index"]
            assert 1 <= k < power and 1 <= ell < power and k+ell == power
            assert 0 <= i < DIMENSIONS[k] and 0 <= j < DIMENSIONS[ell]
            a, da = product(k, i)
            b, db = product(ell, j)
            cache[key] = a*b, da*b+a*db
            return cache[key]

        values = [self.L.zero for _ in range(4)]
        aa, bb = self.coefficients
        for index in range(1234):
            self.budget()
            value, derivative = product(5, index)
            values[0] += aa[index]*value
            values[1] += aa[index]*derivative
            values[2] += bb[index]*value
            values[3] += bb[index]*derivative
        self.store(name, dict(zip(("A0", "A1", "B0", "B1"),
                                 (value.encode() for value in values)),
            original_c1=4424, coarse_coordinate="z=a-1", derivative_order=1,
            original_M2_scale="6724", original_power5_scale="13744803133596058624",
            original_basis_rows=1234, division_by_M2_values_used=False,
            old_q_series_or_basis_or_CM_traces_recomputed=False,
            common_denominator_and_integer_content_reinserted=False))
        return tuple(values)

    def cube_root(self, w):
        assert not w.b
        name = "R792-original-Galois-cube-root"
        prior = self.cached(name)
        if prior:
            assert self.L.decode(prior["w"]) == w
            root = self.L.decode(prior["u"])
            assert not root.b and root**3 == w
            return root
        if not w:
            self.store(name, {"w": w.encode(), "u": w.encode(),
                              "case": "zero", "unique_Fb_cube_root_verified": True})
            return w
        self.budget()
        powers = [self.L.one]
        for _ in range(6):
            powers.append(powers[-1]*self.b)
        columns = [w*power for power in powers]
        assert all(not value.b for value in columns)
        matrix = fmpq_mat([[value.a[i] for value in columns] for i in range(7)])
        H = matrix.charpoly()
        assert H.degree() == 7 and H[7] == 1
        coefficients = [fmpq(0) for _ in range(22)]
        for i in range(8):
            coefficients[3*i] = H[i]
        N = fmpq_poly(coefficients)
        self.budget()
        content, factors = N.factor(monic=True)
        assert content == 1
        reconstructed = fmpq_poly([content])
        for poly, exponent in factors:
            reconstructed *= poly**exponent
        assert reconstructed == N
        pattern = sorted((poly.degree(), int(exponent)) for poly, exponent in factors)
        assert pattern in ([(1, 7), (2, 7)], [(7, 1), (14, 1)])
        odd = [poly for poly, exponent in factors if poly.degree() % 2]
        assert len(odd) == 1
        q = odd[0]
        left = [self.L.elt(q[i]) for i in range(q.degree()+1)]
        right = [-w, self.L.zero, self.L.zero, self.L.one]
        gcd = polynomial_gcd(left, right)
        assert len(gcd) == 2 and gcd[1] == self.L.one
        root = -gcd[0]
        assert not root.b and root**3 == w
        assert not polynomial_remainder(left, gcd)
        assert not polynomial_remainder(right, gcd)
        self.store(name, {"w": w.encode(), "u": root.encode(),
            "multiplication_matrix_Q": [[rational(matrix[i, j]) for j in range(7)] for i in range(7)],
            "H_w_Q_coefficients": rational_polynomial(H),
            "H_w_X_cubed_Q_coefficients": rational_polynomial(N),
            "Q_irreducible_factors": [{"coefficients": rational_polynomial(poly),
                "degree": poly.degree(), "multiplicity": int(exponent)} for poly, exponent in factors],
            "selected_odd_degree_factor": rational_polynomial(q),
            "gcd_over_original_Fb": [value.encode() for value in gcd],
            "factorization_product_verified": True, "gcd_degree": 1,
            "unique_Fb_cube_root_verified": True, "numerical_branch_selection_used": False})
        return root

    def point(self, jets):
        prior = self.cached("R792-original-beta-C-and-real-descent-point")
        if prior:
            return prior
        a0, a1, b0, b1 = jets
        if a0 or b0:
            common_order, numerator, denominator = 0, a0, b0
        elif a1 or b1:
            common_order, numerator, denominator = 1, a1, b1
        else:
            self.store("R792-common-zero-needs-more-jets", {
                "actual_beta_C_computed": False, "common_zero_order_at_least": 2,
                "proven_common_zero_order_upper_bound": 154,
                "existing_coarse_jet_order": 1,
                "next_required_operation": "continue exact local section evaluation until the first nonzero pair",
                "completed_section_composition_preserved": True})
            return None
        payload = {"original_map_index": 4, "original_map_degree": "1206",
            "original_c1": 4424, "original_c0_image": "O", "common_zero_order": common_order,
            "original_h0_over_dz": self.h0.encode(),
            "actual_beta_C_computed": True, "actual_real_descent_image_computed": True,
            "original_A_coordinate_lift_computed": False,
            "comparison_to_original_A": "q_R([c1-c0])=v*q([c1-c0]); original v and kappa retained",
            "actual_heights_or_uniformity_computed": False}
        if not denominator:
            assert numerator
            if common_order == 0:
                assert not b1, "Original nonzero tangent forces a third-order pole at c1."
            payload.update({"point_status": "infinity", "beta_C": "O", "real_descent_image": "O",
                "original_y_pole_order": 3, "pole_order_from_original_nonzero_tangent": True,
                "quotient_derivative_independently_compared": False})
        else:
            y = numerator/denominator
            assert conjugate(y) == -y
            v = y/self.s
            assert not v.b
            w = y*y-self.b
            assert not w.b and w, "The fixed original real embedding has b>0."
            u = self.cube_root(w)
            x = self.zeta**2*u
            assert y*y == x**3+self.b and conjugate(x) == self.zeta**2*x
            derivative = 3*x*x*self.h0
            assert derivative and conjugate(derivative) == -derivative
            compared = common_order == 0
            if compared:
                assert derivative == (a1*b0-a0*b1)/(b0*b0)
            xr = -u*(y*y+3*self.b)/(3*w)
            yr = v*(y*y-9*self.b)/(3*w)
            assert not xr.b and not yr.b and yr*yr == xr**3+self.b
            payload.update({"point_status": "finite", "x_original_L": x.encode(),
                "y_original_L": y.encode(), "u_original_Fb": u.encode(), "v_original_Fb": v.encode(),
                "y_derivative_original_z": derivative.encode(),
                "x_real_descent_Fb": xr.encode(), "y_real_descent_Fb": yr.encode(),
                "original_elliptic_equation_verified": True, "original_Galois_direction_verified": True,
                "real_descent_elliptic_equation_verified": True,
                "quotient_derivative_independently_compared": compared,
                "derivative_source": "3*x^2*h0 from original pullback; quotient comparison iff common_zero_order=0",
                "no_extra_c1_phase_or_base_translation": True})
        self.store("R792-original-beta-C-and-real-descent-point", payload)
        return payload

    def run(self):
        point = self.point(self.section_jets())
        if point is None:
            save(self.out/"core-receipt.json", {"result": RESULT, "complete": False,
                "source_sha256": sha(__file__), "actual_beta_C_computed": False,
                "needs_higher_common_zero_evaluation": True,
                "common_zero_order_at_least": 2, "exit_code": 75,
                "completed_stages_preserved": True})
            return 75
        manifest_name = "R792-stage-manifest"
        rows = []
        for path in sorted(self.out.glob("R792-*.json.gz")):
            if path == self.path(manifest_name):
                continue
            data = read(path)
            assert data["complete"] is True and data["configuration"] == self.tag
            rows.append(file_spec(path))
        self.store(manifest_name, {"files": rows})
        certificate = {"result": RESULT, "complete": True, "configuration": self.tag,
            "p": 41, "original_map_index": 4, "original_map_degree": "1206",
            "point_status": point["point_status"], "common_zero_order": point["common_zero_order"],
            "actual_beta_C_computed": True, "actual_real_descent_image_computed": True,
            "original_A_coordinate_lift_computed": False,
            "actual_heights_or_uniformity_computed": False,
            "original_M2_scale": "6724", "original_power5_scale": "13744803133596058624",
            "original_h0_nonzero": True, "original_Galois_direction_input_verified": True,
            "quotient_derivative_independently_compared": point["quotient_derivative_independently_compared"],
            "point_spec": file_spec(self.path("R792-original-beta-C-and-real-descent-point")),
            "stage_manifest": file_spec(self.path(manifest_name)),
            "old_periods_Laurent_basis_or_CM_traces_recomputed": False,
            "seconds": time.monotonic()-self.started}
        save(self.out/FINAL, certificate)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(self.out/FINAL),
            "actual_beta_C_computed": True, "actual_real_descent_image_computed": True,
            "original_A_coordinate_lift_computed": False,
            "actual_heights_or_uniformity_computed": False})
        return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "proof", "field-core", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    try:
        return Job(args).run()
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "actual_beta_C_computed": False,
            "error": type(error).__name__+": "+str(error), "completed_stages_preserved": True})
        raise


if __name__ == "__main__":
    sys.exit(main())
