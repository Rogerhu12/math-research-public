#!/usr/bin/env python3
"""R801: only missing original V6/V7/V8 tails, from certified old recipes."""
import argparse
from functools import lru_cache
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpz_poly

RESULT = "R801-original-power6-to8-long-tails"
FINAL = "p41-original-power6-to8-long-tails-certificate.json"
P, LEVEL, CYC, REAL, ELL, XI = 41, 82, 40, 20, 739, 538
PROOF_SHA = "b283280e94a9b429d57a20e8bc1c3e40ce552a8eb06ca8ddb19a6d43d18fb6fd"
METHOD_SHA = "a96d7c3b3e4665b1ca2cdd7383e08406fe3d4cc0b8a1bea0aa4a43d110a74126"
DIMS = {1: 146, 2: 418, 3: 690, 4: 962, 5: 1234, 6: 1506, 7: 1778, 8: 2050}
FIRST = {6: 109, 7: 96, 8: 109}
FRONTIERS = {6: (142,), 7: (170, 172, 176), 8: (193, 196)}
ANCHORS = (0, 1, 73)
PRODUCER_RESULTS = {
    "R775": "R775-p41-original-K-defined-RR-bases",
    "R786": "R786-exact-original-power5-short-basis",
    "R795": "R795-exact-original-power6-short-basis",
    "R799": "R799-original-power7-power8-short-bases",
    "R800": "R800-original-M2-tail-129-195"}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")


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


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain_spec(row):
    return {key: row[key] for key in ("file", "bytes", "sha256")}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def same_producer(left, right):
    for key in ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "certificate_name"):
        assert str(left[key]) == str(right[key]), ("producer identity", key)
    name = left["certificate_name"]
    assert left["files"][name] == right["files"][name]
    for name in set(left["files"]) & set(right["files"]):
        assert left["files"][name] == right["files"][name], ("shared producer file", name)


def rectangles(a, b, c, d, first, stop):
    """Disjoint rectangles partition exactly first <= i+j < stop."""
    low, high = a+c, b+d-2
    if a >= b or c >= d or high < first or low >= stop:
        return
    if first <= low and high < stop:
        yield a, b, c, d
        return
    if b-a >= d-c:
        middle = (a+b)//2
        assert a < middle < b
        yield from rectangles(a, middle, c, d, first, stop)
        yield from rectangles(middle, b, c, d, first, stop)
    else:
        middle = (c+d)//2
        assert c < middle < d
        yield from rectangles(a, b, c, middle, first, stop)
        yield from rectangles(a, b, middle, d, first, stop)


def packed(rows):
    assert rows
    values = [0]*(79*(len(rows)-1)+CYC)
    for n, row in enumerate(rows):
        assert len(row) == CYC
        for r, value in enumerate(row):
            values[79*n+r] = int(value)
    return fmpz_poly(values)


def unpacked(product, count):
    assert product.length() <= 79*count
    answer = []
    for n in range(count):
        cyclic = [0]*P
        for r in range(79):
            cyclic[r % P] += int(product[79*n+r])
        answer.append([cyclic[r]-cyclic[40] for r in range(CYC)])
    return answer


class Retained:
    def __init__(self, root, label, spec):
        self.label, self.directory, self.spec = label, Path(root)/label, spec
        assert spec["result"] == PRODUCER_RESULTS[label]
        mp = self.directory/"full-outputs-manifest.json"
        assert sha(mp) == spec["manifest_sha256"]
        manifest = read(mp)
        assert manifest["result"] == spec["result"]
        self.files = {row["file"]: row for row in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        self.checked = set()
        run, core, initial = (self.raw(name) for name in
            ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
        assert run["result"] == spec["result"] and run["complete"] is True and run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(spec["run_id"]) and run["source_commit"] == spec["source_commit"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
        assert initial["result"] == spec["result"] and initial["source_commit"] == spec["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == spec["core_sha256"]
        self.initial = initial
        name = spec["certificate_name"]
        assert self.files[name]["sha256"] == core["certificate_sha256"] == spec["files"][name]
        self.certificate = self.raw(name)
        assert self.certificate["complete"] is True and self.certificate["result"] == spec["result"]
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == spec["core_sha256"] and self.tag["python_flint"] == "0.9.0"

    def raw(self, name, expected=None):
        assert Path(name).name == name
        entry = self.files[name]
        if expected is not None:
            assert entry["sha256"] == expected
        if name in self.spec["files"]:
            assert entry["sha256"] == self.spec["files"][name]
        path = self.directory/name
        if (name, entry["sha256"]) not in self.checked:
            assert path.stat().st_size == entry["bytes"] and sha(path) == entry["sha256"]
            self.checked.add((name, entry["sha256"]))
        return read(path)

    def stage(self, row):
        assert plain_spec(self.files[row["file"]]) == plain_spec(row)
        value = self.raw(row["file"], row["sha256"])
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def inventory(self, key):
        data = self.stage(self.certificate[key])
        rows = {row["file"]: plain_spec(row) for row in data["files"]}
        assert len(rows) == len(data["files"])
        return rows


class Node:
    def __init__(self, key, power, original_recipe, factors, sources, reference_index=None):
        self.key, self.power = key, power
        self.original_recipe, self.factors = original_recipe, tuple(factors)
        self.initial_sources = list(sources)
        self.sources = list(sources)
        self.original_reference_index = reference_index
        self.old_stop = sources[-1]["stop"] if sources else 0
        self.valuation = None
        self.identity = {"node_key": key, "ordinary_power": power, "original_recipe": original_recipe,
                         "factor_nodes": list(factors), "integer_scale": str(LEVEL**(2*power)),
                         "original_reference_index": reference_index}
        self.digest = fingerprint(self.identity)

    @property
    def stop(self):
        return self.sources[-1]["stop"] if self.sources else 0


class BudgetStop(RuntimeError):
    pass


class Job:
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert flint.__version__ == "0.9.0"
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == P and self.item["core_sha256"] == sha(__file__)
        assert sha(args.proof) == self.item["R801_proof_sha256"] == PROOF_SHA
        assert sha(args.method) == self.item["R801_method_sha256"] == METHOD_SHA
        assert self.item["primary_new_intervals"] == {"6": [109, 142], "7": [96, 176], "8": [109, 196]}
        assert self.item["primary_frontiers"] == {str(p): list(stops) for p, stops in FRONTIERS.items()}
        assert self.item["auxiliary_max_exponent"] == 195
        assert self.item["generate_additional_pencil_V3_tail"] is False
        assert set(self.item["retained_artifacts"]) == set(PRODUCER_RESULTS)
        self.retained = {label: Retained(args.retained, label, self.item["retained_artifacts"][label])
                         for label in ("R775", "R786", "R795", "R799", "R800")}
        self.r775, self.r786, self.r795, self.r799, self.r800 = \
            (self.retained[label] for label in ("R775", "R786", "R795", "R799", "R800"))
        for parent in (self.r795, self.r799, self.r800):
            parents = parent.tag["retained_artifacts"]
            for label, child in parents.items():
                if label in self.retained:
                    same_producer(child, self.retained[label].spec)
                    same_producer(parent.initial["job"]["retained_artifacts"][label], self.retained[label].spec)
        self.original_bases = {}
        stages775 = {row["file"]: row for row in self.r775.certificate["stages"]}
        assert self.r775.certificate["all_recipes_defined_over_original_K"] is True
        assert self.r775.tag["prime"] == ELL and self.r775.tag["xi41_mod_ell"] == XI
        for power in range(1, 7):
            name = "R775-basis-M2.json.gz" if power == 1 else "R775-basis-power-"+str(power)+".json.gz"
            stage = self.r775.stage(stages775[name])
            assert stage["rank"] == len(stage["basis"]) == DIMS[power]
            assert stage["coefficient_bound"] >= 272*power
            assert stage["characteristic_zero_independence_certified_by_unit_reduction"] is True
            minor = stage["actual_nonzero_minor"]
            assert minor["prime"] == ELL and int(minor["determinant_mod_ell"]) % ELL
            assert minor["rows"] == minor["columns"] == DIMS[power]
            self.original_bases[power] = stage["basis"]
            if power <= 5:
                assert self.r786.tag["R775_completed_prefix_producer"]["files"][name] == stages775[name]["sha256"]
        assert sorted({row["recipe"]["left_index"] for row in self.original_bases[6]}) == list(ANCHORS)
        for row in self.original_bases[6]:
            assert row["recipe"]["kind"] == "product" and row["recipe"]["left_power"] == 1
            assert row["recipe"]["right_power"] == 5
        self.stages786 = self.r786.inventory("stages_manifest")
        self.stages795 = self.r795.inventory("stage_manifest")
        self.stages799 = self.r799.inventory("stage_manifest")
        self.stages800 = self.r800.inventory("stage_manifest")
        c786, c795, c799, c800 = (producer.certificate for producer in
                                 (self.r786, self.r795, self.r799, self.r800))
        assert c786["exact_power5_basis_dimension"] == 1234 and c786["exact_K_basis_prefix_bound_qY"] == 128
        assert c786["basis_in_original_R775_saved_order"] is True
        assert c795["exact_power6_basis_dimension"] == 1506 and c795["exact_K_basis_prefix_bound_qY"] == 81
        assert c795["basis_in_original_R775_saved_order"] is True and c795["basis_integer_scale"] == str(LEVEL**12)
        self.index795 = self.r795.stage(c795["basis_index"])
        self.index799six = self.r799.stage(c799["power6_tail_index"])
        assert c799["power6_tail_dimension"] == 1506 and c799["power6_new_interval"] == [82, 109]
        assert c799["new_exact_basis_dimensions"] == {"7": 1778, "8": 2050}
        assert c799["new_exact_basis_bounds_qY"] == {"7": 95, "8": 108}
        assert c799["three_original_anchor_basepoint_free_input_verified"] is True
        assert c799["all_new_basis_rows_match_selecting_modular_columns"] is True
        self.short_indices = {}
        for power in (7, 8):
            index = self.r799.stage(c799["basis_indices"][str(power)])
            assert index["dimension"] == len(index["basis_rows"]) == DIMS[power]
            assert index["ordinary_power"] == power and index["bound_qY"] == FIRST[power]-1
            assert index["integer_scale"] == str(LEVEL**(2*power))
            assert index["characteristic_zero_basis_certified"] is True
            assert index["full_original_real_coordinates"] == REAL
            assert index["all_exact_rows_compared_with_selecting_modular_columns"] is True
            assert [row["index"] for row in index["basis_rows"]] == list(range(DIMS[power]))
            positions = [row["candidate_position"] for row in index["basis_rows"]]
            assert positions == sorted(set(positions))
            assert len({row["file"] for row in index["basis_rows"]}) == DIMS[power]
            assert all(row["all_current_prime_coordinates_verified"] is True for row in index["basis_rows"])
            minor = index["actual_nonzero_minor"]
            assert minor == c799["actual_new_nonzero_minors"][str(power)]
            assert minor["rows"] == minor["columns"] == DIMS[power] and minor["determinant_mod_prime"] % minor["prime"]
            assert len(set(minor["coordinate_row_indices"])) == DIMS[power]
            assert all(0 <= i < REAL*FIRST[power] for i in minor["coordinate_row_indices"])
            assert minor["selected_basis_column_indices"] == list(range(DIMS[power]))
            assert minor["all_entries_from_saved_exact_integer_rows"] is True
            self.short_indices[power] = index
        for index in (self.index795, self.index799six):
            assert index["dimension"] == 1506
            assert [row["index"] for row in index["basis_rows"]] == list(range(1506))
        assert self.index799six["first_exponent"] == 82 and self.index799six["last_exponent_exclusive"] == 109
        assert c800["original_M2_dimension"] == 146 and c800["first_exponent"] == 129
        assert c800["last_exponent_exclusive"] == 196 and c800["original_M2_integer_scale"] == "6724"
        assert c800["all_new_original_mod739_coefficients_verified"] is True
        assert c800["all_new_real_tangent_involutions_verified"] is True
        self.index800 = self.r800.stage(c800["basis_tail_index"])
        assert self.index800["dimension"] == 146 and len(self.index800["tail_rows_in_original_order"]) == 146
        assert self.index800["first_exponent"] == 129 and self.index800["last_exponent_exclusive"] == 196
        assert self.index800["integer_scale"] == "6724"
        self.tag = {"result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R801_proof_sha256": sha(args.proof), "R801_method_sha256": sha(args.method),
            "retained_artifacts": self.item["retained_artifacts"], "p": P, "level": LEVEL,
            "primary_new_intervals": self.item["primary_new_intervals"],
            "primary_frontiers": self.item["primary_frontiers"], "auxiliary_max_exponent": 195,
            "generate_additional_pencil_V3_tail": False,
            "primary_dimensions": {"6": 1506, "7": 1778, "8": 2050},
            "integer_scales": {str(p): str(LEVEL**(2*p)) for p in range(1, 9)},
            "v_parameter": "v=xi41^-10*qY", "t_parameter": "t=xi41+xi41^-1",
            "packing": "two reduced xi39 inputs; stride79; reduce before the next product",
            "ordinary_basis_reselected": False, "old_coefficients_recomputed": False,
            "Laurent_Dixon_or_rational_map_computed": False}
        t = fmpz_poly([0, 1])
        cs = [fmpz_poly([2]), t]
        for _ in range(2, 21):
            cs.append(t*cs[-1]-cs[-2])
        modulus = fmpz_poly([1])
        for value in cs[1:]:
            modulus += value
        assert modulus.degree() == 20 and modulus[20] == 1
        self.real_change = []
        for value in cs:
            value %= modulus
            self.real_change.append([(j, int(value[j])) for j in range(20) if value[j]])
        self.xipowers = [pow(XI, r, ELL) for r in range(CYC)]
        self.nodes, self.used_aliases, self.original_aliases = {}, {}, {}
        for power in (2, 3):
            for index in range(DIMS[power]):
                leaves = self.original_leaves(power, index)
                assert leaves not in self.original_aliases, ("duplicate old product basis recipe", power, index)
                self.original_aliases[leaves] = (power, index)
        self.targets = {6: [self.original_node(6, i).key for i in range(1506)], 7: [], 8: []}
        for power in (7, 8):
            for index, item in enumerate(self.short_indices[power]["basis_rows"]):
                recipe = item["recipe"]
                original_index = recipe["right_index"]
                assert recipe["right_power"] == 6 and 0 <= original_index < 1506
                original = self.original_bases[6][original_index]["recipe"]
                if power == 7:
                    assert recipe["kind"] == "product" and recipe["left_power"] == 1
                    leaves = (recipe["left_index"], original["left_index"])
                else:
                    assert recipe["kind"] == "triple_product" and recipe["anchor_powers"] == [1, 1]
                    assert len(recipe["anchor_indices"]) == 2
                    leaves = tuple(recipe["anchor_indices"])+(original["left_index"],)
                assert all(a in ANCHORS for a in leaves)
                multiplier = self.multiplier(tuple(sorted(leaves)))
                factor = self.original_node(5, original["right_index"])
                key = "n"+str(power).zfill(2)+"-i"+str(index).zfill(4)
                source = self.source("R799", item, 0, FIRST[power])
                node = Node(key, power, recipe, (multiplier.key, factor.key), [source])
                self.nodes[key] = node
                self.targets[power].append(key)
        assert len([key for key in self.used_aliases if len(key) == 2]) <= 6
        assert len([key for key in self.used_aliases if len(key) == 3]) <= 10
        self.restore_segments()
        for node in self.nodes.values():
            self.valuation(node)
        self.save_plan()

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes-45:
            raise BudgetStop("Completed exact nonoverlapping tail segments retained for immediate continuation.")

    def path(self, name):
        assert name.startswith("R801-") and Path(name).name == name
        return self.out/(name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def store(self, name, value):
        save(self.path(name), dict(value, complete=True, configuration=self.tag))
        return file_spec(self.path(name))

    def source(self, label, row, first, stop):
        assert 0 <= first < stop <= 196
        producer = self.retained[label]
        assert plain_spec(row) == plain_spec(producer.files[row["file"]])
        return dict(plain_spec(row), producer=label, first=first, stop=stop)

    @lru_cache(maxsize=None)
    def original_leaves(self, power, index):
        assert 1 <= power <= 6 and 0 <= index < DIMS[power]
        if power == 1:
            return (index,)
        recipe = self.original_bases[power][index]["recipe"]
        assert recipe["kind"] == "product"
        a, b = recipe["left_power"], recipe["right_power"]
        assert 0 < a < power and 0 < b < power and a+b == power
        result = self.original_leaves(a, recipe["left_index"])+self.original_leaves(b, recipe["right_index"])
        assert len(result) == power
        return tuple(sorted(result))

    def original_node(self, power, index):
        assert 1 <= power <= 6 and 0 <= index < DIMS[power]
        key = "o"+str(power).zfill(2)+"-i"+str(index).zfill(4)
        if key in self.nodes:
            return self.nodes[key]
        recipe = self.original_bases[power][index]["recipe"]
        if power == 1:
            factors = ()
        else:
            assert recipe["kind"] == "product" and recipe["left_power"]+recipe["right_power"] == power
            factors = tuple(self.original_node(recipe[side+"_power"], recipe[side+"_index"]).key
                            for side in ("left", "right"))
        if power <= 5:
            name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
            sources = [self.source("R786", self.stages786[name], 0, 129)]
            if power == 1:
                tail = self.index800["tail_rows_in_original_order"][index]
                assert tail["file"] == "R800-original-M2-tail-row-"+str(index).zfill(4)+".json.gz"
                assert plain_spec(tail) == self.stages800[tail["file"]]
                sources.append(self.source("R800", tail, 129, 196))
        else:
            assert power == 6
            old, tail = self.index795["basis_rows"][index], self.index799six["basis_rows"][index]
            assert plain_spec(old) == self.stages795[old["file"]]
            assert plain_spec(tail) == self.stages799[tail["file"]]
            sources = [self.source("R795", old, 0, 82), self.source("R799", tail, 82, 109)]
        node = Node(key, power, recipe, factors, sources, reference_index=index)
        self.nodes[key] = node
        return node

    def multiplier(self, leaves):
        assert len(leaves) in (2, 3) and leaves == tuple(sorted(leaves))
        if leaves in self.used_aliases:
            return self.nodes[self.used_aliases[leaves]]
        if leaves in self.original_aliases:
            power, index = self.original_aliases[leaves]
            node = self.original_node(power, index)
        else:
            if len(leaves) == 2:
                factors = [self.original_node(1, a).key for a in leaves]
            else:
                factors = [self.multiplier(leaves[:2]).key, self.original_node(1, leaves[2]).key]
            key = "a"+str(len(leaves)).zfill(2)+"-"+"-".join(str(a).zfill(3) for a in leaves)
            node = Node(key, len(leaves), {"kind": "new_anchor_monomial", "anchor_indices": list(leaves)},
                        factors, [])
            self.nodes[key] = node
        self.used_aliases[leaves] = node.key
        return node

    @lru_cache(maxsize=64)
    def source_rows(self, node_key, producer, name, digest, size, first, stop):
        node = self.nodes[node_key]
        spec = {"file": name, "sha256": digest, "bytes": size}
        if producer == "R801":
            path = self.out/name
            assert Path(name).name == name and path.stat().st_size == size and sha(path) == digest
            data = read(path)
            assert data["complete"] is True and data["configuration"] == self.tag
            assert data["node_key"] == node_key and data["node_fingerprint"] == node.digest
            assert data["first_exponent"] == first and data["last_exponent_exclusive"] == stop
            assert data["all_original_phase_involutions_verified"] is True
        else:
            data = self.retained[producer].stage(spec)
            assert data["recipe"] == node.original_recipe
            if producer == "R786":
                assert first == 0 and stop == 129 and data["bound_qY"] == 128
                assert data["original_R775_finite_coefficients_verified"] is True
            elif producer == "R795":
                assert node.power == 6 and first == 0 and stop == 82 and data["bound_qY"] == 81
                assert data["index"] == node.original_reference_index
                assert data["original_R775_finite_coefficients_verified"] is True
                assert data["all_original_phase_involutions_verified"] is True
            elif producer == "R799":
                if node.power == 6:
                    assert first == 82 and stop == 109 and data["index"] == node.original_reference_index
                    assert data["first_exponent"] == first and data["last_exponent_exclusive"] == stop
                    assert data["old_R795_prefix"] == plain_spec(node.initial_sources[0])
                    assert data["original_R775_mod739_tail_verified"] is True
                else:
                    assert node.power in (7, 8) and data["ordinary_power"] == node.power
                    assert first == 0 and stop == FIRST[node.power] and data["bound_qY"] == stop-1
                    assert data["all_initial_modular_coordinates_verified"] is True
                assert data["all_original_phase_involutions_verified"] is True
            elif producer == "R800":
                assert node.power == 1 and data["index"] == node.original_reference_index
                assert first == 129 and stop == 196
                assert data["first_exponent"] == first and data["last_exponent_exclusive"] == stop
                assert data["original_R786_prefix"] == plain_spec(node.initial_sources[0])
                assert data["all_new_original_mod739_coefficients_verified"] is True
                assert data["all_new_real_tangent_involutions_verified"] is True
            else:
                raise AssertionError(producer)
        assert data["weight"] == 2*node.power and data["integer_scale"] == str(LEVEL**(2*node.power))
        rows = data["integer_qY_xi_coefficients"]
        assert len(rows) == stop-first and all(len(row) == CYC for row in rows)
        return tuple(tuple(int(v) for v in row) for row in rows)

    def read_source(self, node, source):
        return self.source_rows(node.key, source["producer"], source["file"], source["sha256"],
                                source["bytes"], source["first"], source["stop"])

    @lru_cache(maxsize=48)
    def series(self, key, stop):
        node = self.nodes[key]
        assert 0 < stop <= node.stop
        rows = []
        for source in node.sources:
            if source["first"] >= stop:
                break
            assert source["first"] == len(rows)
            values = self.read_source(node, source)
            rows.extend(values[:min(source["stop"], stop)-source["first"]])
        assert len(rows) == stop
        return tuple(rows)

    @lru_cache(maxsize=512)
    def pack_slice(self, key, first, stop):
        assert first < stop
        return packed(self.series(key, stop)[first:stop])

    def valuation(self, node):
        if node.valuation is not None:
            return node.valuation
        expected = sum(self.valuation(self.nodes[key]) for key in node.factors) if node.factors else None
        if node.initial_sources:
            first = node.initial_sources[0]
            assert first["first"] == 0
            rows = self.read_source(node, first)
            actual = next((n for n, row in enumerate(rows) if any(row)), None)
            assert actual is not None, (node.key, "a certified nonzero old prefix must have a leading term")
            if expected is not None:
                assert actual == expected, (node.key, "original recipe valuation")
            node.valuation = actual
        else:
            assert expected is not None
            node.valuation = expected
        return node.valuation

    def restore_segments(self):
        grouped = {}
        for path in sorted(self.out.glob("R801-tail-*.json.gz")):
            data = read(path)
            assert data["complete"] is True and data["configuration"] == self.tag
            key = data["node_key"]
            assert key in self.nodes
            node = self.nodes[key]
            assert data["node_fingerprint"] == node.digest and data["node_identity"] == node.identity
            first, stop = data["first_exponent"], data["last_exponent_exclusive"]
            assert 0 <= first < stop <= 196
            assert data["ordinary_power"] == node.power and data["weight"] == 2*node.power
            assert data["integer_scale"] == str(LEVEL**(2*node.power))
            assert data["all_original_phase_involutions_verified"] is True
            assert len(data["integer_qY_xi_coefficients"]) == len(data["integer_v_t_coefficients"]) == stop-first
            assert all(len(row) == CYC for row in data["integer_qY_xi_coefficients"])
            assert all(len(row) == REAL for row in data["integer_v_t_coefficients"])
            if node.original_reference_index is not None:
                assert data["original_R775_mod739_reference_verified"] is True
            if key.startswith("o"):
                assert node.power != 1
                assert first >= (109 if node.power == 6 else 129)
                assert stop <= (142 if node.power == 6 else 196)
            elif key.startswith("n"):
                assert first >= FIRST[node.power] and stop <= FRONTIERS[node.power][-1]
            else:
                assert key.startswith("a") and node.power in (2, 3)
            grouped.setdefault(key, []).append((first, stop, file_spec(path), data["previous_segments"]))
        for key, values in grouped.items():
            node = self.nodes[key]
            for first, stop, spec, previous in sorted(values):
                assert first == node.stop and previous == node.sources, (key, "disjoint continuation intervals")
                node.sources.append(dict(spec, producer="R801", first=first, stop=stop))

    def save_plan(self):
        name = "R801-original-recipe-dependency-plan"
        old = self.cached(name)
        plan = {"primary_targets": {str(p): self.targets[p] for p in (6, 7, 8)},
            "nodes": [dict(node.identity, node_fingerprint=node.digest, valuation=node.valuation,
                           old_coverage_stop=node.old_stop, original_input_segments=node.initial_sources)
                      for node in sorted(self.nodes.values(), key=lambda value: value.key)],
            "actual_anchor_multiplier_aliases": [
                {"anchor_multiset": list(leaves), "node_key": key,
                 "aliases_an_original_R786_row": key.startswith("o")}
                for leaves, key in sorted(self.used_aliases.items())],
            "all_original_recipe_valuations_verified_from_certified_old_prefixes": True,
            "old_rows_or_basis_selection_recomputed": False,
            "flattened_primary_7_8_do_not_require_original_6_after_141": True}
        if old is not None:
            for key, value in plan.items():
                assert old[key] == value
            return file_spec(self.path(name))
        return self.store(name, plan)

    def real_rows(self, rows, first):
        answer = []
        for n, values in enumerate(rows, first):
            cyclic = [0]*P
            for r, value in enumerate(values):
                cyclic[(r+10*n) % P] += value
            reduced = [value-cyclic[40] for value in cyclic[:40]]+[0]
            assert all(reduced[r] == reduced[P-r] for r in range(1, 21)), (n, "original tangent phase")
            real = [reduced[0]]+[0]*(REAL-1)
            for r in range(1, 21):
                scalar = reduced[r]
                if scalar:
                    for j, coefficient in self.real_change[r]:
                        real[j] += scalar*coefficient
            answer.append([str(value) for value in real])
        return answer

    def source_partitions(self, node, stop):
        assert 0 <= stop <= node.stop
        answer = []
        for source in node.sources:
            first, last = max(source["first"], node.valuation), min(source["stop"], stop)
            if first < last:
                answer.append((first, last))
        return answer

    def dependencies(self, node, stop):
        return {"node_key": node.key, "node_fingerprint": node.digest, "valuation": node.valuation,
                "required_stop": stop,
                "source_segments": [source for source in node.sources if source["first"] < stop]}

    def require(self, key, stop):
        node = self.nodes[key]
        assert 0 <= stop <= 196
        if node.key.startswith("o06"):
            assert stop <= 142
        if node.stop >= stop:
            return
        assert len(node.factors) == 2 and node.power >= 2
        left, right = (self.nodes[factor] for factor in node.factors)
        assert left.power+right.power == node.power
        left_stop, right_stop = max(0, stop-right.valuation), max(0, stop-left.valuation)
        self.require(left.key, left_stop)
        self.require(right.key, right_stop)
        first = node.stop
        assert first < stop
        self.budget()
        product, count = fmpz_poly([]), 0
        for a, b in self.source_partitions(left, left_stop):
            for c, d in self.source_partitions(right, right_stop):
                for aa, bb, cc, dd in rectangles(a, b, c, d, first, stop):
                    # Every exponent in this whole rectangle lies in the new interval.
                    piece = self.pack_slice(left.key, aa, bb)*self.pack_slice(right.key, cc, dd)
                    product += piece.left_shift(79*(aa+cc-first))
                    count += 1
        rows = unpacked(product, stop-first)
        reference_verified = None
        if node.original_reference_index is not None:
            assert 2 <= node.power <= 6
            finite = self.original_bases[node.power][node.original_reference_index]["coefficients_mod_ell"]
            scale = pow(LEVEL, 2*node.power, ELL)
            for n, row in enumerate(rows, first):
                actual = sum(value*power for value, power in zip(row, self.xipowers)) % ELL
                expected = scale*(int(finite[n]) if n < len(finite) else 0) % ELL
                assert actual == expected, (node.key, n, "original R775 finite coefficient")
            reference_verified = True
        name = "R801-tail-"+key+"-"+str(first).zfill(4)+"-"+str(stop).zfill(4)
        assert not self.path(name).exists(), "An already completed tail must be restored, not recomputed."
        spec = self.store(name, {"node_key": key, "node_fingerprint": node.digest, "node_identity": node.identity,
            "ordinary_power": node.power, "weight": 2*node.power, "integer_scale": str(LEVEL**(2*node.power)),
            "first_exponent": first, "last_exponent_exclusive": stop,
            "integer_qY_xi_coefficients": [[str(value) for value in row] for row in rows],
            "integer_v_t_coefficients": self.real_rows(rows, first),
            "valuation": node.valuation, "previous_segments": list(node.sources),
            "source_dependencies": [self.dependencies(left, left_stop), self.dependencies(right, right_stop)],
            "disjoint_band_rectangle_count": count,
            "original_R775_mod739_reference_verified": reference_verified,
            "all_original_phase_involutions_verified": True,
            "old_coefficients_recomputed": False, "original_prefix_bytes_modified": False,
            "coefficients_outside_this_missing_interval_generated": False})
        node.sources.append(dict(spec, producer="R801", first=first, stop=stop))

    def frontier(self, power, stop):
        name = "R801-original-power"+str(power)+"-frontier-"+str(stop).zfill(4)
        old = self.cached(name)
        if old is not None:
            assert old["ordinary_power"] == power and old["dimension"] == DIMS[power]
            assert old["coverage_stop"] == stop and old["new_first_exponent"] == FIRST[power]
            assert len(old["basis_rows"]) == DIMS[power]
            assert [row["index"] for row in old["basis_rows"]] == list(range(DIMS[power]))
            assert [row["node_key"] for row in old["basis_rows"]] == self.targets[power]
            for row in old["basis_rows"]:
                node = self.nodes[row["node_key"]]
                assert node.digest == row["node_fingerprint"] and node.stop >= stop
                assert row["original_recipe"] == node.original_recipe
                assert row["original_prefix_segments"] == node.initial_sources
                assert row["new_tail_segments"] == [source for source in node.sources
                    if source["producer"] == "R801" and source["first"] < stop]
            return file_spec(self.path(name))
        rows = []
        for index, key in enumerate(self.targets[power]):
            self.require(key, stop)
            node = self.nodes[key]
            assert node.stop >= stop
            rows.append({"index": index, "node_key": key, "node_fingerprint": node.digest,
                "original_recipe": node.original_recipe,
                "original_prefix_segments": node.initial_sources,
                "new_tail_segments": [row for row in node.sources
                                      if row["producer"] == "R801" and row["first"] < stop]})
            if index % 32 == 0 or index+1 == DIMS[power]:
                print(json.dumps({"stage": "original_power"+str(power)+"_new_tail",
                    "new_first_exponent": FIRST[power], "target_stop": stop, "rows": index+1,
                    "dimension": DIMS[power], "seconds": time.monotonic()-self.started}), flush=True)
        return self.store(name, {"ordinary_power": power, "dimension": DIMS[power],
            "new_first_exponent": FIRST[power], "coverage_stop": stop,
            "integer_scale": str(LEVEL**(2*power)), "basis_rows": rows,
            "basis_order": "R775/R795 for6; actual final R799 index for7/8",
            "all_rows_complete_through_this_frontier": True, "basis_reselected": False,
            "old_prefix_recomputed": False})

    def retained_prefix_index(self):
        # Keep every selected original short row available to the next relation consumer.
        rows = {}
        for node in self.nodes.values():
            for source in node.initial_sources:
                key = (source["producer"], source["file"])
                if key in rows:
                    assert plain_spec(rows[key]) == plain_spec(source)
                    continue
                producer = self.retained[source["producer"]]
                path = producer.directory/source["file"]
                assert path.stat().st_size == source["bytes"] and sha(path) == source["sha256"]
                rows[key] = dict(plain_spec(source), producer=source["producer"])
        return self.store("R801-required-original-prefix-retention-index", {
            "files": [rows[key] for key in sorted(rows)], "file_count": len(rows),
            "all_selected_R799_short_rows_included": True,
            "all_original_R795_and_R799_power6_prefix_segments_included": True,
            "all_required_R786_lower_power_prefixes_included": True,
            "prefix_bytes_modified": False,
            "next_relation_consumer_must_transfer_these_original_files_in_the_active_bundle": True})

    def run(self):
        final = self.out/FINAL
        if final.exists():
            cert = read(final)
            assert cert["result"] == RESULT and cert["complete"] is True and cert["configuration"] == self.tag
            inventory = cert["stage_manifest"]
            assert sha(self.out/inventory["file"]) == inventory["sha256"]
            assert (self.out/inventory["file"]).stat().st_size == inventory["bytes"]
            for row in read(self.out/inventory["file"])["files"]:
                path = self.out/row["file"]
                assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        else:
            frontiers, final_indices = {}, {}
            for power in (6, 7, 8):
                frontiers[str(power)] = []
                for stop in FRONTIERS[power]:
                    spec = self.frontier(power, stop)
                    frontiers[str(power)].append(spec)
                final_indices[str(power)] = frontiers[str(power)][-1]
            coverage = self.store("R801-actual-auxiliary-coverage-index", {
                "nodes": [{"node_key": node.key, "ordinary_power": node.power, "node_fingerprint": node.digest,
                           "valuation": node.valuation, "original_coverage_stop": node.old_stop,
                           "actual_coverage_stop": node.stop, "original_input_segments": node.initial_sources,
                           "new_tail_segments": [row for row in node.sources if row["producer"] == "R801"]}
                          for node in sorted(self.nodes.values(), key=lambda value: value.key)
                          if node.power <= 5],
                "no_extra_pencil_V3_rows_requested": True,
                "only_actual_dependency_closure_extended": True})
            retained = self.retained_prefix_index()
            files = [file_spec(path) for path in sorted(self.out.glob("R801-*.json.gz"))
                     if path.name != "R801-stage-manifest.json.gz"]
            manifest = self.store("R801-stage-manifest", {"files": files})
            cert = {"result": RESULT, "complete": True, "p": P, "configuration": self.tag,
                "primary_dimensions": {"6": 1506, "7": 1778, "8": 2050},
                "primary_new_intervals": self.item["primary_new_intervals"],
                "actual_primary_frontiers": {str(p): list(stops) for p, stops in FRONTIERS.items()},
                "basis_tail_indices": final_indices, "completed_frontier_indices": frontiers,
                "auxiliary_coverage_index": coverage, "original_prefix_retention_index": retained,
                "dependency_plan": file_spec(self.path("R801-original-recipe-dependency-plan")),
                "stage_manifest": manifest,
                "all_extended_original_power2_to6_tails_match_original_mod739_reference": True,
                "all_new_rows_have_full_original_phase_involution_checks": True,
                "all_selected_R799_short_rows_retained_for_the_next_consumer": True,
                "old_coefficients_recomputed": False, "ordinary_basis_reselected": False,
                "original_power6_coefficients_after141_generated": False,
                "primary_power7_after175_or_power8_after195_generated": False,
                "new_E1_M2_Laurent_Dixon_function_polar_divisor_eta_or_height_computed": False,
                "seconds": time.monotonic()-self.started}
            save(final, cert)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(final),
            "primary_dimensions": {"6": 1506, "7": 1778, "8": 2050},
            "primary_new_intervals": {"6": [109, 142], "7": [96, 176], "8": [109, 196]},
            "old_coefficients_recomputed": False,
            "new_E1_M2_Laurent_Dixon_function_polar_divisor_eta_or_height_computed": False})
        return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "proof", "method", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    try:
        return Job(args).run()
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "completed_nonoverlapping_segments_preserved": True})
        raise


if __name__ == "__main__":
    sys.exit(main())
