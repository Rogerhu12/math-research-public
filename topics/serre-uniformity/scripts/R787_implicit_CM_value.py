#!/usr/bin/env python3
"""Original R787 CM responses from a completed 518-digit direction.

All new arithmetic runs only in the public repository's GitHub Actions.
This result never certifies expanded characteristic-zero point coordinates.
It records exact source-bound solve expressions, their modular values, and
separately labelled rational-reconstruction suggestions.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

RESULT = "R787-original-implicit-CM-value"
FINAL = "p41-original-implicit-CM-value-certificate.json"
PREFIX = "R787-implicit-CM-"
ELL, DIGITS, FREE = 1000000753, 518, 1186
N, D, RANK = 1234, 1214, 1186
DIMENSIONS = {1: 146, 2: 418, 3: 690, 4: 962, 5: 1234}
SCALE = "13744803133596058624"
OLD_TAG_SHA = "71ea66416a42e024de61cf5927bc493fbc8422dc1b5970d75c51bd788d88529d"
OLD_CORE_SHA = "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
PROOF_SHA = "8d5b58a5f6e9748805af3c032de1bae955543b1855535b6c51f0ca9cd6947820"
OLD_METHOD_SHA = "1d91bfc7bdf61c40c4deda19833a5f50491630a61a7a25feb7a3a1e0b451204b"
R786_PROOF_SHA = "c46008726fb18f52a5430b72c4994ce76164f11bea51044f1677278294f7011d"
R786_INDEX_SHA = "0bb7cfeda48d6759f1553dec74485a28dc16e31cf3d500a095963888973c9b35"
R790_PROOF_SHA = "83303dcd6abc65875d8c67eb8977126db1c85cf3e9dafb3fbd2881163aadfc39"
CURRENT = "R787-prime-1000000753-dixon-00000518.json.gz"
CHART = "R787-prime-1000000753-chart.json.gz"
BLOCKS = "R787-prime-1000000753-rational-blocks.json.gz"
SELECTION = "R787-prime-1000000753-selection.json.gz"
CURRENT_SHA = "4997a05b79ab9e7c7f9286fc483b1f459ff6e23fa18df5344bd8ef0eb80f10f5"
BASIS_FILES = {
    1: ("R775-basis-M2.json.gz", "51113988c90b301cb6117fec5c294b77110e1826bf00229b7993ba82144f5d3d"),
    2: ("R775-basis-power-2.json.gz", "734a61e967c51ba3c9cd93eaff1a81fba165600110abb941dfdbbeed41b6ebe4"),
    3: ("R775-basis-power-3.json.gz", "00361e5155c429de5c54b613b8a3cb46ac9530c554e1a812823748bb2bf5fe18"),
    4: ("R775-basis-power-4.json.gz", "85beb7662eee64f4eca9e205314a6625506e3041bea199985489c7cf1f62dd4e"),
    5: ("R775-basis-power-5.json.gz", "7aff6faa89a91649db5549bbf9360647534bff6f9586ce3f5963e322d33c30ba")}
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
BLOCK_SIZE = 32
STRATEGY = {
    "CM_target": "original P1 over c1=4424, z=a-1",
    "exact_K_basis": "1,s; s=1+2*zeta; s^2=-3",
    "integral_L_basis": "B^i*s^j, j=0..1 outer, i=0..6; B=lambda*b",
    "product_rule": "(v,d)*(w,e)=(v*w,d*w+v*e)",
    "denominator_response": "exact e_j Z first; no separate Z*C expansion",
    "modular_inverse": "stored branch evaluation inverse at ell, then scalar Newton doubling",
    "coordinate_reconstruction": "one strict scalar RR suggestion per coordinate; never exact acceptance",
    "accurate_acceptance_executed": False,
    "old_q_rows_Schur_inverse_Dixon_CM_traces_recomputed": False,
    "fixed_block_size": BLOCK_SIZE}


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda: stream.read(1024*1024), b""):
            digest.update(part)
    return digest.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


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


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain(item):
    return {key: item[key] for key in ("file", "bytes", "sha256")}


def rational(pair):
    assert len(pair) == 2 and int(pair[1]) > 0
    return Fraction(int(pair[0]), int(pair[1]))


def encode_q(value):
    return [str(value.numerator), str(value.denominator)]


def encode_k(value):
    return [encode_q(value[0]), encode_q(value[1])]


def decode_k(value):
    assert len(value) == 2
    return rational(value[0]), rational(value[1])


def kadd(left, right):
    return left[0]+right[0], left[1]+right[1]


def kscale(left, scalar):
    return left[0]*scalar, left[1]*scalar


def kmul(left, right):
    a, b = left
    c, d = right
    return a*c-3*b*d, a*d+b*c


def dual_product(left, right):
    a, da = left
    b, db = right
    return kmul(a, b), kadd(kmul(da, b), kmul(a, db))


def same_producer(left, right):
    for key in BASE_KEYS:
        assert str(left[key]) == str(right[key]), ("producer identity", key)


class BudgetStop(RuntimeError):
    pass


class Source:
    def __init__(self, root, label, item):
        self.directory, self.label, self.item = root/label, label, item
        path = self.directory/"full-outputs-manifest.json"
        assert sha(path) == item["manifest_sha256"]
        manifest = read(path)
        assert manifest["result"] == item["result"]
        self.inventory = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(self.inventory) == len(manifest["files"])
        self.files = item["files"]
        assert fingerprint([self.files[name] for name in sorted(self.files)]) == item["selected_files_sha256"]
        for name, row in self.files.items():
            assert name == row["file"] and Path(name).name == name
            if name == "full-outputs-manifest.json":
                assert row["sha256"] == item["manifest_sha256"]
            else:
                assert row == self.inventory[name]
        self.identity = {key: item[key] for key in BASE_KEYS}
        self.identity.update(configuration_sha256=item["configuration_sha256"],
                             selected_files_sha256=item["selected_files_sha256"])
        self.certificate = None
        if item.get("certificate"):
            self.certificate = self.get(item["certificate"]["file"], check_tag=False)
            assert self.certificate["complete"] is True
            assert self.certificate["result"] == item["result"]
            self.tag = self.certificate["configuration"]
            self.identity["certificate"] = item["certificate"]
        else:
            assert label == "R787"
            self.tag = self.get(CHART, check_tag=False)["configuration"]
        assert fingerprint(self.tag) == item["configuration_sha256"]
        assert self.tag["source_sha256"] == item["core_sha256"]

    def path(self, name):
        row = self.files[name]
        path = self.directory/name
        assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        return path

    def get(self, name, check_tag=True):
        value = read(self.path(name))
        if check_tag:
            assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def get_spec(self, item):
        assert plain(item) == self.files[item["file"]]
        return self.get(item["file"])


class Ring14:
    """The original monic quotient (Z/m)[B,s]/(f_B,s^2+3)."""
    def __init__(self, coefficients):
        self.f = [int(value) for value in coefficients]
        assert len(self.f) == 8 and self.f[-1] == 1

    def mul(self, left, right, modulus):
        assert len(left) == len(right) == 14
        low, high = [0]*13, [0]*13
        for i in range(7):
            for j in range(7):
                low[i+j] += left[i]*right[j]-3*left[7+i]*right[7+j]
                high[i+j] += left[i]*right[7+j]+left[7+i]*right[j]
        for values in (low, high):
            for degree in range(12, 6, -1):
                scalar = values[degree] % modulus
                if scalar:
                    for j in range(7):
                        values[degree-7+j] -= scalar*self.f[j]
            values[:] = [value % modulus for value in values[:7]]
        return low+high


def rr_candidate(value, modulus):
    value %= modulus
    if not value:
        return ["0", "1"]
    bound = math.isqrt(modulus//2)
    r0, r1, t0, t1 = modulus, value, 0, 1
    while abs(r1) > bound:
        q = r0//r1
        r0, r1, t0, t1 = r1, r0-q*r1, t1, t0-q*t1
    if not t1 or abs(t1) > bound or math.gcd(r1, t1) != 1:
        return None
    if t1 < 0:
        r1, t1 = -r1, -t1
    if (value*t1-r1) % modulus:
        return None
    return [str(r1), str(t1)]


class Job:
    def __init__(self, args):
        self.args, self.out = args, args.output
        self.started = time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.config = read(args.config)
        assert self.config["result"] == RESULT and self.config["p"] == 41
        assert self.config["producer_inputs_pending"] is False
        assert self.config["core_sha256"] == sha(__file__)
        assert sha(args.proof) == self.config["proof_sha256"] == PROOF_SHA
        assert set(self.config["retained_sources"]) == {"R787", "R790", "R775", "R786"}
        self.inputs = {label: Source(args.retained, label, item)
                       for label, item in self.config["retained_sources"].items()}
        self.tag = {"result": RESULT, "source_sha256": sha(__file__),
            "proof_sha256": PROOF_SHA, "arithmetic": "exact Python Fraction and original rank14 monic integer ring",
            "p": 41, "auxiliary_prime": ELL, "source_Dixon_digits": DIGITS,
            "canonical_free_column": FREE, "source_identities":
                {label: source.identity for label, source in self.inputs.items()},
            "strategy": STRATEGY,
            "original_map_index": 4, "original_map_degree": "1206",
            "budget_excluded_from_mathematical_identity": True}
        self.modulus = ELL**DIGITS
        self.inverse_denominators = {}
        self.prepare_sources()

    def budget(self):
        if time.monotonic()-self.started > self.args.budget_minutes*60:
            raise BudgetStop("All completed CM product and contraction stages retained.")

    def path(self, name):
        assert name.startswith(PREFIX) and Path(name).name == name
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
        print(json.dumps({"stage": name, "seconds": round(time.monotonic()-self.started, 3)}), flush=True)
        return value

    def ref(self, name):
        return spec(self.path(name))

    def prepare_sources(self):
        r787, r790, r775, r786 = (self.inputs[k] for k in ("R787", "R790", "R775", "R786"))
        assert fingerprint(r787.tag) == OLD_TAG_SHA
        assert r787.tag["source_sha256"] == OLD_CORE_SHA
        assert r787.tag["R787_method_sha256"] == OLD_METHOD_SHA
        assert r787.tag["R786_proof_sha256"] == R786_PROOF_SHA
        assert r787.tag["basis_dimension"] == N and r787.tag["basis_integer_scale"] == SCALE
        assert r787.tag["original_map_index"] == 4 and r787.tag["original_map_degree"] == "1206"
        self.field = r787.tag["field"]
        assert self.field["original_b_replaced_by_another_twist"] is False
        assert int(self.field["lambda"]) % ELL
        self.ring = Ring14(self.field["integral_B_minimal_polynomial"])
        self.chart = r787.get(CHART)
        self.selection = r787.get(SELECTION)
        block = r787.get(BLOCKS)
        assert self.chart["prime"] == block["prime"] == self.selection["prime"] == ELL
        assert self.chart["actual_modular_rank"] == RANK
        assert self.chart["chosen_free_column"] == FREE
        assert self.chart["other_free_columns_set_to_zero"] is True
        self.pivots = self.chart["pivot_columns"]
        assert len(self.pivots) == len(set(self.pivots)) == RANK
        self.free_columns = [j for j in range(D) if j not in set(self.pivots)]
        assert len(self.free_columns) == 28 and FREE in self.free_columns
        self.P, self.Q = block["B_constant_pivot_columns"], block["B_constant_free_columns"]
        self.Zp = [[int(value) for value in row] for row in block["Z_pivot_integer_rows"]]
        self.Zd = int(block["Z_free_diagonal"])
        assert len(self.P) == 20 and len(self.Q) == D and sorted(self.P+self.Q) == list(range(N))
        assert len(self.Zp) == 20 and all(len(row) == D for row in self.Zp)
        assert self.Zd > 0 and self.Zd % ELL and block["exact_E0_Z_zero_verified"] is True
        assert block["A_inverse_over_Q_computed"] is False
        self.Arows, self.AR = block["A_pivot_rows"], block["A_remaining_rows"]
        assert len(self.Arows) == N and len(self.AR) == 1326
        assert sorted(self.Arows+self.AR) == list(range(2560))
        assert len(self.chart["pivot_rows"]) == RANK
        assert block["A_minor_det_mod_prime"] == 336446771
        assert block["B_constant_minor_det_mod_prime"] == 322380492
        del block
        for key in ("prime_proved", "all_14_L_branches_distinct", "all_kappa_reductions_invertible",
                    "all_rational_denominators_units"):
            assert self.selection[key] is True
        assert len(self.selection["roots_B_s"]) == 14
        assert len(self.selection["evaluation_matrix"]) == 14
        assert all(len(row) == 14 for row in self.selection["evaluation_matrix"])
        assert len(self.selection["inverse_evaluation_matrix"]) == 14
        assert all(len(row) == 14 for row in self.selection["inverse_evaluation_matrix"])
        assert r787.files[CURRENT]["sha256"] == CURRENT_SHA
        self.current = r787.get(CURRENT)
        assert self.current["digits"] == DIGITS and self.current["prime"] == ELL
        assert self.current["chart_sha256"] == r787.files[CHART]["sha256"]
        assert self.current["full_original_modular_relations_verified"] is True
        assert int(self.current["modulus"]) == self.modulus
        aa, cc = self.current["A_L_coordinates"], self.current["C_L_coordinates"]
        assert len(aa) == N and len(cc) == D and all(len(row) == 14 for row in aa+cc)
        for j in self.free_columns:
            assert [int(value) for value in cc[j]] == [int(j == FREE)]+[0]*13
        same_producer(r787.tag["retained_artifacts"]["R786"], r786.item)
        c786 = r786.certificate
        assert c786["basis_in_original_R775_saved_order"] is True
        assert c786["exact_power5_basis_dimension"] == N and c786["basis_integer_scale"] == SCALE
        assert c786["basis_index"]["sha256"] == R786_INDEX_SHA
        index = r786.get_spec(c786["basis_index"])
        assert index["dimension"] == N and index["bound_qY"] == 128
        assert index["integer_scale"] == SCALE
        assert [row["index"] for row in index["basis_rows"]] == list(range(N))
        self.basis_index = c786["basis_index"]
        assert r775.certificate["all_recipes_defined_over_original_K"] is True
        self.recipes = {}
        for power, (name, digest) in BASIS_FILES.items():
            assert r775.files[name]["sha256"] == digest
            assert r786.tag["R775_completed_prefix_producer"]["files"][name] == digest
            obj = r775.get(name)
            assert obj["rank"] == DIMENSIONS[power] and len(obj["basis"]) == DIMENSIONS[power]
            assert obj["characteristic_zero_independence_certified_by_unit_reduction"] is True
            self.recipes[power] = [row["recipe"] for row in obj["basis"]]
        cm = r790.certificate
        assert cm["p"] == 41 and cm["M2_dimension"] == 146 and cm["cm_jet_order"] == 5
        assert cm["original_psi_values_and_first_coarse_jets_verified"] is True
        assert cm["original_M2_scale"] == "6724" and cm["R786_power5_product_scale"] == SCALE
        assert cm["distinct_retained_M2_seeds"] == 5 and cm["actual_reflected_seed_pairs"] == 10
        assert r790.tag["R790_proof_sha256"] == R790_PROOF_SHA
        same_producer(r790.tag["retained_artifacts"]["R775"], r775.item)
        cmmanifest = r790.get_spec(cm["stage_manifest"])
        assert cmmanifest["M2_output_rows"] == cm["M2_output_rows"]
        cmspecs = {row["file"]: plain(row) for row in cmmanifest["files"]}
        self.cm_rows = []
        for i, item in enumerate(cm["M2_output_rows"]):
            assert i < 146 and cmspecs[item["file"]] == plain(item)
            row = r790.get_spec(item)
            assert row["index"] == i and row["original_recipe"] == self.recipes[1][i]
            assert row["integer_scale"] == "6724" and row["R786_power1_scale_preserved"] is True
            assert row["M2_recipe_source_sha256"] == BASIS_FILES[1][1]
            assert row["original_c1"] == 4424
            assert row["coarse_coordinate"] == "z=a-1; z=-epsilon^3/(81*(U/4)^2)+O(epsilon^6)"
            assert row["K_basis"] == ["1", "zeta=(-1+sqrt(-3))/2"]
            self.cm_rows.append(row)
        assert len(self.cm_rows) == 146
        name = PREFIX+"source-audit"
        if self.cached(name) is None:
            self.store(name, {"actual_source_Dixon_digits": DIGITS, "new_Dixon_digits_computed": 0,
                "old_R787_configuration_sha256": OLD_TAG_SHA, "source_current": r787.files[CURRENT],
                "source_chart": r787.files[CHART], "source_rational_blocks": r787.files[BLOCKS],
                "source_selection": r787.files[SELECTION], "original_field": self.field,
                "R786_original_basis_index": self.basis_index,
                "original_complete_relation_identification": "unit-chart proposition U.1 and independently proved kernel dimension28",
                "original_complete_modular_relations_read": True,
                "normalized_free_coordinates_verified": True,
                "all_original_CM_and_recipe_source_identities_verified": True,
                "original_Z_pivot_sign_read_without_negating_again": True,
                "original_q_rows_loaded_or_recomputed": False,
                "new_Schur_inverse_or_relation_coordinates_computed": False,
                "expanded_coordinates_exactly_certified": False})

    def product_closure(self):
        required = {power: set() for power in DIMENSIONS}
        def visit(power, index):
            assert power in DIMENSIONS and 0 <= index < DIMENSIONS[power]
            if index in required[power]:
                return
            required[power].add(index)
            if power == 1:
                return
            recipe = self.recipes[power][index]
            assert recipe["kind"] == "product"
            left, right = recipe["left_power"], recipe["right_power"]
            assert 1 <= left < power and 1 <= right < power and left+right == power
            visit(left, recipe["left_index"])
            visit(right, recipe["right_index"])
        for i in range(N):
            visit(5, i)
        return {power: sorted(indices) for power, indices in required.items()}

    def section_values(self):
        required = self.product_closure()
        cache, rowspecs = {}, []
        for power in range(1, 6):
            indices = required[power]
            for first in range(0, len(indices), BLOCK_SIZE):
                self.budget()
                chosen = indices[first:first+BLOCK_SIZE]
                name = PREFIX+"power-"+str(power)+"-jets-block-"+str(first//BLOCK_SIZE).zfill(4)
                stage = self.cached(name)
                if stage is None:
                    rows = []
                    for index in chosen:
                        if power == 1:
                            pair = []
                            for key in ("value_K_1_zeta", "derivative_z_K_1_zeta"):
                                a, b = decode_k(self.cm_rows[index][key])
                                pair.append((a-b/2, b/2))
                            value = tuple(pair)
                        else:
                            recipe = self.recipes[power][index]
                            left = cache[(recipe["left_power"], recipe["left_index"])]
                            right = cache[(recipe["right_power"], recipe["right_index"])]
                            value = dual_product(left, right)
                        rows.append({"index": index, "value": encode_k(value[0]), "derivative_z": encode_k(value[1])})
                    stage = self.store(name, {"power": power, "indices": chosen, "rows": rows,
                        "original_CM_point": "P1", "coarse_coordinate": "z=a-1",
                        "integer_scale": str(6724**power), "exact_K_basis": "1,s; s^2=-3",
                        "scale_applied_again": False, "only_required_recipe_nodes_computed": True})
                assert stage["power"] == power and stage["indices"] == chosen
                assert [row["index"] for row in stage["rows"]] == chosen
                for row in stage["rows"]:
                    cache[(power, row["index"])] = (decode_k(row["value"]), decode_k(row["derivative_z"]))
                rowspecs.append(self.ref(name))
        name = PREFIX+"power5-exact-jets-index"
        if self.cached(name) is None:
            self.store(name, {"dimension": N, "derivative_order": 1, "integer_scale": SCALE,
                "required_recipe_indices": {str(k): v for k, v in required.items()},
                "completed_blocks": rowspecs, "original_M2_scale": "6724",
                "old_P0_evaluations_consumed": False, "old_CM_traces_recomputed": False,
                "original_basis_order": True})
        return [cache[(5, i)] for i in range(N)]

    def eZ(self, jets):
        values, blocks = [], []
        for first in range(0, D, BLOCK_SIZE):
            self.budget()
            stop = min(first+BLOCK_SIZE, D)
            name = PREFIX+"exact-eZ-block-"+str(first//BLOCK_SIZE).zfill(4)
            stage = self.cached(name)
            if stage is None:
                rows = []
                for j in range(first, stop):
                    pair = []
                    for derivative in range(2):
                        value = kscale(jets[self.Q[j]][derivative], self.Zd)
                        for i in range(20):
                            value = kadd(value, kscale(jets[self.P[i]][derivative], self.Zp[i][j]))
                        pair.append(value)
                    rows.append({"index": j, "value": encode_k(pair[0]), "derivative_z": encode_k(pair[1])})
                stage = self.store(name, {"first_column": first, "stop_column": stop, "rows": rows,
                    "power5_jets": self.ref(PREFIX+"power5-exact-jets-index"),
                    "exact_original_Z": self.inputs["R787"].files[BLOCKS],
                    "Z_pivot_rows_already_include_minus_sign": True,
                    "denominator_vector_ZC_not_separately_reconstructed": True})
            assert stage["first_column"] == first and stage["stop_column"] == stop
            assert [row["index"] for row in stage["rows"]] == list(range(first, stop))
            values.extend((decode_k(row["value"]), decode_k(row["derivative_z"])) for row in stage["rows"])
            blocks.append(self.ref(name))
        name = PREFIX+"exact-eZ-index"
        if self.cached(name) is None:
            self.store(name, {"columns": D, "blocks": blocks, "exact_K_basis": "1,s",
                "integer_scale": SCALE, "eZ_computed_in_characteristic_zero": True})
        assert len(values) == D
        return values

    def qmod(self, value):
        denominator = value.denominator
        assert denominator % ELL
        if denominator not in self.inverse_denominators:
            self.inverse_denominators[denominator] = pow(denominator, -1, self.modulus)
        return value.numerator*self.inverse_denominators[denominator] % self.modulus

    def contract(self, label, values, source_key):
        name = PREFIX+"response-"+label
        done = self.cached(name)
        if done is not None:
            return done
        current = self.current[source_key]
        assert len(values) == len(current)
        blocks = []
        total = [[0]*14 for _ in range(2)]
        for first in range(0, len(values), BLOCK_SIZE):
            self.budget()
            stop = min(first+BLOCK_SIZE, len(values))
            blockname = PREFIX+"response-"+label+"-block-"+str(first//BLOCK_SIZE).zfill(4)
            stage = self.cached(blockname)
            if stage is None:
                sums = [[0]*14 for _ in range(2)]
                for index in range(first, stop):
                    vector = [int(value) for value in current[index]]
                    assert all(0 <= value < self.modulus for value in vector)
                    for derivative in range(2):
                        a, b = (self.qmod(value) for value in values[index][derivative])
                        for i in range(7):
                            sums[derivative][i] = (sums[derivative][i]+a*vector[i]-3*b*vector[7+i]) % self.modulus
                            sums[derivative][7+i] = (sums[derivative][7+i]+b*vector[i]+a*vector[7+i]) % self.modulus
                stage = self.store(blockname, {"response": label, "first_index": first, "stop_index": stop,
                    "value": [str(v) for v in sums[0]], "derivative_z": [str(v) for v in sums[1]],
                    "source_current": self.inputs["R787"].files[CURRENT], "digits": DIGITS,
                    "exact_scalar_source": self.ref(PREFIX+("power5-exact-jets-index" if label == "A" else "exact-eZ-index")),
                    "all_CM_rational_denominators_units": True})
            assert stage["first_index"] == first and stage["stop_index"] == stop and stage["response"] == label
            for d, key in enumerate(("value", "derivative_z")):
                assert len(stage[key]) == 14
                total[d] = [(a+int(b)) % self.modulus for a, b in zip(total[d], stage[key])]
            blocks.append(self.ref(blockname))
        return self.store(name, {"response": label, "value": [str(v) for v in total[0]],
            "derivative_z": [str(v) for v in total[1]], "digits": DIGITS, "modulus": str(self.modulus),
            "blocks": blocks, "source_current": self.inputs["R787"].files[CURRENT],
            "integral_L_basis": STRATEGY["integral_L_basis"], "lambda_powers_not_applied": True,
            "relation_denominator_or_content_not_reinserted": True})

    def denominator_witness(self, b):
        name = PREFIX+"denominator-unit-witness"
        stage = self.cached(name)
        if stage is not None:
            return stage
        vector = [int(value) % ELL for value in b["value"]]
        evaluations = self.selection["evaluation_matrix"]
        values = [sum(int(w)*v for w, v in zip(row, vector)) % ELL for row in evaluations]
        return self.store(name, {"source_response": self.ref(PREFIX+"response-B"),
            "source_selection": self.inputs["R787"].files[SELECTION],
            "prime": ELL, "roots_B_s": self.selection["roots_B_s"],
            "B0_values_at_original_14_branches": values,
            "nonzero_flags": [bool(value) for value in values],
            "nonzero_branch_indices": [i for i, value in enumerate(values) if value],
            "all_14_branches_units": all(values),
            "characteristic_zero_B0_nonzero_certified": any(values),
            "modular_zero_claimed_to_prove_characteristic_zero_zero": False,
            "common_zero_or_point_at_infinity_claimed": False})

    def inverse(self, b, witness):
        assert witness["all_14_branches_units"] is True
        name = PREFIX+"B0-ring-inverse-0001"
        stage = self.cached(name)
        if stage is None:
            branch_inverse = [pow(value, -1, ELL) for value in witness["B0_values_at_original_14_branches"]]
            inverse_matrix = self.selection["inverse_evaluation_matrix"]
            inverse = [sum(int(a)*b for a, b in zip(row, branch_inverse)) % ELL for row in inverse_matrix]
            assert self.ring.mul([int(value) % ELL for value in b["value"]], inverse, ELL) == [1]+[0]*13
            stage = self.store(name, {"digits": 1, "modulus": str(ELL), "inverse": [str(v) for v in inverse],
                "source_unit_witness": self.ref(PREFIX+"denominator-unit-witness"),
                "stored_evaluation_inverse_reused": True, "full14_product_equals_one": True})
        precision = 1
        while precision < DIGITS:
            self.budget()
            following = min(2*precision, DIGITS)
            nextname = PREFIX+"B0-ring-inverse-"+str(following).zfill(4)
            following_stage = self.cached(nextname)
            if following_stage is None:
                modulus = ELL**following
                inverse = [int(value) for value in stage["inverse"]]
                bv = [int(value) % modulus for value in b["value"]]
                product = self.ring.mul(bv, inverse, modulus)
                correction = [(-value) % modulus for value in product]
                correction[0] = (correction[0]+2) % modulus
                new_inverse = self.ring.mul(inverse, correction, modulus)
                assert self.ring.mul(bv, new_inverse, modulus) == [1]+[0]*13
                following_stage = self.store(nextname, {"digits": following, "modulus": str(modulus),
                    "inverse": [str(v) for v in new_inverse], "previous_inverse": self.ref(name),
                    "source_response_B": self.ref(PREFIX+"response-B"),
                    "full14_product_equals_one": True, "composite_modulus_matrix_inverse_computed": False})
            assert following_stage["digits"] == following
            precision, name, stage = following, nextname, following_stage
        return stage, self.ref(name)

    def quotient(self, a, b, witness):
        if not witness["all_14_branches_units"]:
            return None
        name = PREFIX+"original-y-modular-value-and-first-jet"
        prior = self.cached(name)
        if prior is not None:
            return prior
        inverse, inverse_spec = self.inverse(b, witness)
        av, ad, bv, bd = ([int(v) for v in obj[key]] for obj, key in
                          ((a, "value"), (a, "derivative_z"), (b, "value"), (b, "derivative_z")))
        iv = [int(v) for v in inverse["inverse"]]
        y = self.ring.mul(av, iv, self.modulus)
        left, right = self.ring.mul(ad, bv, self.modulus), self.ring.mul(av, bd, self.modulus)
        numerator = [(x-y) % self.modulus for x, y in zip(left, right)]
        derivative = self.ring.mul(numerator, self.ring.mul(iv, iv, self.modulus), self.modulus)
        assert self.ring.mul(y, bv, self.modulus) == [v % self.modulus for v in av]
        assert self.ring.mul(derivative, self.ring.mul(bv, bv, self.modulus), self.modulus) == numerator
        return self.store(name, {"digits": DIGITS, "prime": ELL, "modulus": str(self.modulus),
            "value_y0": [str(v) for v in y], "derivative_z_y0": [str(v) for v in derivative],
            "A_response": self.ref(PREFIX+"response-A"), "B_response": self.ref(PREFIX+"response-B"),
            "ring_inverse": inverse_spec, "all14_original_quotient_identities_verified": True,
            "original_field": self.field, "integral_L_basis": STRATEGY["integral_L_basis"],
            "only_modular_values_computed": True, "expanded_coordinates_exactly_certified": False})

    def expression(self, witness):
        name = PREFIX+"exact-source-bound-implicit-expression"
        prior = self.cached(name)
        if prior is not None:
            return prior
        r787 = self.inputs["R787"]
        original_rows = [r787.inventory["R787-real-power5-row-"+str(i).zfill(4)+".json.gz"] for i in range(N)]
        jrows = self.Arows+[self.AR[i] for i in self.chart["pivot_rows"]]
        assert len(jrows) == 2420 and len(set(jrows)) == 2420
        return self.store(name, {"proof_sha256": PROOF_SHA, "original_field": self.field,
            "unit_chart_solve": {"shape": [2420, 2420], "row_order": jrows,
                "first_block_columns": "F_A[rows,0..1233]",
                "second_block_columns": {"operator": "-C[rows,pivot_columns]", "pivot_columns": self.pivots},
                "right_hand_side": "C[rows,1186]", "free_column": FREE,
                "other_free_columns": [i for i in self.free_columns if i != FREE], "other_free_values": "zero",
                "original_chart": r787.files[CHART], "original_Z_and_A_row_selection": r787.files[BLOCKS],
                "exact_inverse_expression": "adj(M)*r/det(M)", "matrix_or_inverse_expanded": False,
                "nonzero_determinant_reason": "original unit chart and full kernel dimension28; proof U.1"},
            "operator_recipe": {"F_shape": [2580, 1234], "F_coordinate_order": "v^n*t^r; n0..128,r0..19",
                "F_A_rows": [0, 2560], "original_F_rows": original_rows,
                "original_F_rows_retained_in_this_numeric_subset": False,
                "original_F_rows_parent_manifest_sha256": r787.item["manifest_sha256"],
                "Z_formula": "Z[P,:]=stored Z_pivot_integer_rows; Z[Q,:]=Z_free_diagonal*I",
                "Y_formula": "-(1/246^3)*sum(R_m*kappa^(-m-1)*v^m,m0..128)",
                "C_formula": "take v^1..v^128,20 t coordinates of Y*(F*Z)",
                "R781_completed_original_Laurent_source": r787.tag["retained_artifacts"]["R781"],
                "R781_source_files": ["R781-original-real-field-input.json.gz"]+
                    ["R781-inverse-free-Laurent-"+str(i).zfill(3)+".json.gz" for i in range(130)],
                "no_cleared_row_substitution_at_same_individual_row_numbers": True,
                "future_exact_zero_consumer_must_restore_bound_original_rows": True},
            "linear_responses": {"A0": {"row": "(e0,0)", "constant": "0"},
                "A1": {"row": "(e1,0)", "constant": "0"},
                "B0": {"row": "(0,(e0Z)[pivot_columns])", "constant": "(e0Z)[1186]"},
                "B1": {"row": "(0,(e1Z)[pivot_columns])", "constant": "(e1Z)[1186]"},
                "e0_e1": self.ref(PREFIX+"power5-exact-jets-index"), "e0Z_e1Z": self.ref(PREFIX+"exact-eZ-index")},
            "bordered_determinant_definition": "Delta(l,c)=det([[M,r],[-l,c]])=det(M)*(c+l*M^-1*r)",
            "original_relation_exactly_defined_by_unit_chart": True,
            "full129_t20_Q280_relation_identity_source": "proved full kernel equals selected kernel, dimension28",
            "original_finite_CM_y_expression_defined": witness["characteristic_zero_B0_nonzero_certified"],
            "B0_nonzero_witness": self.ref(PREFIX+"denominator-unit-witness"),
            "y0_expression_if_denominator_nonzero": "Delta(l_A0,0)/Delta(l_B0,c_B0)",
            "derivative_expression_if_denominator_nonzero": "(A1*B0-A0*B1)/B0^2",
            "expanded_coordinates_exactly_certified": False,
            "bordered_determinant_zero_or_exact_rowspace_acceptance_executed": False,
            "old_R792_expanded_coordinate_recipe_produced": False})

    def candidates(self, quotient):
        if quotient is None:
            return None
        name = PREFIX+"point-coordinate-reconstruction-candidates"
        prior = self.cached(name)
        if prior is not None:
            return prior
        candidates = {}
        for key in ("value_y0", "derivative_z_y0"):
            self.budget()
            rows = [rr_candidate(int(value), self.modulus) for value in quotient[key]]
            candidates[key] = {"coordinates": rows, "all14_reconstructed": all(row is not None for row in rows)}
        return self.store(name, {"source_modular_quotient": self.ref(PREFIX+"original-y-modular-value-and-first-jet"),
            "candidates": candidates, "integral_L_basis": STRATEGY["integral_L_basis"],
            "strict_scalar_RR_bound": "floor(sqrt(modulus/2))",
            "candidate_only": True, "expanded_coordinates_exactly_certified": False,
            "exact_bordered_determinant_or_rowspace_zero_certificate_obtained": False,
            "curve_equation_or_Galois_symmetry_used_as_exact_identity_certificate": False,
            "x_coordinate_or_beta_point_claimed": False, "may_be_consumed_by_old_R792_success_path": False})

    def finish(self, witness, quotient, candidate):
        records = []
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name.startswith(PREFIX+"stage-manifest-"):
                continue
            value = read(path)
            assert value["complete"] is True and value["configuration"] == self.tag
            records.append(spec(path))
        inventory = {"complete": True, "configuration": self.tag, "files": records,
            "all_stages_are_new_source_identity": True, "old_sources_kept_in_retained_directories": True}
        name = PREFIX+"stage-manifest-"+fingerprint(records)[:24]
        save(self.path(name), inventory)
        result = {"result": RESULT, "configuration": self.tag, "complete": True,
            "p": 41, "original_map_index": 4, "original_map_degree": "1206",
            "source_Dixon_digits": DIGITS, "new_Dixon_digits_computed": 0,
            "source_audit": self.ref(PREFIX+"source-audit"),
            "power5_CM_values_and_jets": self.ref(PREFIX+"power5-exact-jets-index"),
            "exact_eZ": self.ref(PREFIX+"exact-eZ-index"),
            "A_response": self.ref(PREFIX+"response-A"), "B_response": self.ref(PREFIX+"response-B"),
            "denominator_unit_witness": self.ref(PREFIX+"denominator-unit-witness"),
            "implicit_expression": self.ref(PREFIX+"exact-source-bound-implicit-expression"),
            "all_14_branches_units": witness["all_14_branches_units"],
            "characteristic_zero_B0_nonzero_certified": witness["characteristic_zero_B0_nonzero_certified"],
            "exact_implicit_relation_defined": True,
            "exact_finite_y_implicit_expression_defined": witness["characteristic_zero_B0_nonzero_certified"],
            "modular_value_computed": quotient is not None,
            "modular_value": self.ref(PREFIX+"original-y-modular-value-and-first-jet") if quotient is not None else None,
            "coordinate_candidates": self.ref(PREFIX+"point-coordinate-reconstruction-candidates") if candidate is not None else None,
            "expanded_coordinates_exactly_certified": False,
            "actual_beta_point_eta_or_height_computed": False,
            "old_R792_success_recipe_produced": False,
            "stage_manifest": self.ref(name), "seconds": time.monotonic()-self.started}
        save(self.out/FINAL, result)
        print("IMPLICIT_CM_RESULT="+json.dumps({key: result[key] for key in
            ("complete", "source_Dixon_digits", "new_Dixon_digits_computed", "all_14_branches_units",
             "characteristic_zero_B0_nonzero_certified", "exact_finite_y_implicit_expression_defined",
             "modular_value_computed", "expanded_coordinates_exactly_certified", "seconds")}), flush=True)
        return result

    def run(self):
        if (self.out/FINAL).exists():
            prior = read(self.out/FINAL)
            assert prior["complete"] is True and prior["configuration"] == self.tag
            return prior
        jets = self.section_values()
        ez = self.eZ(jets)
        a = self.contract("A", jets, "A_L_coordinates")
        b = self.contract("B", ez, "C_L_coordinates")
        witness = self.denominator_witness(b)
        self.expression(witness)
        quotient = self.quotient(a, b, witness)
        candidate = self.candidates(quotient)
        return self.finish(witness, quotient, candidate)


def main():
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New arithmetic belongs only to this public repository's GitHub Actions.")
    parser = argparse.ArgumentParser()
    for option in ("config", "proof", "retained", "output"):
        parser.add_argument("--"+option, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    started, complete, error, result = time.monotonic(), False, None, None
    code = 1
    try:
        result = Job(args).run()
        complete, code = True, 0
    except BudgetStop as exc:
        error, code = "BudgetStop: "+str(exc), 124
    except Exception as exc:
        error = type(exc).__name__+": "+str(exc)
        import traceback
        traceback.print_exc()
    args.output.mkdir(parents=True, exist_ok=True)
    receipt = {"result": RESULT, "source_sha256": sha(__file__), "complete": complete,
        "error": error, "seconds": time.monotonic()-started,
        "source_Dixon_digits": DIGITS, "new_Dixon_digits_computed": 0,
        "expanded_coordinates_exactly_certified": False,
        "all_completed_stages_preserved": True,
        "certificate_sha256": sha(args.output/FINAL) if complete else None}
    if result is not None:
        receipt["all_14_branches_units"] = result["all_14_branches_units"]
        receipt["modular_value_computed"] = result["modular_value_computed"]
    save(args.output/"core-receipt.json", receipt)
    print("CORE_RECEIPT="+json.dumps(receipt, sort_keys=True), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
