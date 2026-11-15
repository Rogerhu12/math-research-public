#!/usr/bin/env python3
"""R804: the eight original Hom additions evaluated at the actual R792 CM point.

Point collisions are decided from exact point coordinates, never from different
Hom labels. No old beta, periods, Hom matrices, or global functions are computed.
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

RESULT = "R804-original-selected-CM-point-values"
FINAL = "p41-original-selected-CM-point-values-certificate.json"
FIELD_CORE_SHA = "f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251"
MODEL = "p41-original-CM-model-certificate.json"
MODEL_SHA = "752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574"
HOM = "R791-original-Hom-Galois-matrices.json.gz"
HOM_SHA = "f3793ddc7680b718a4448d45587661182986a3558db346ad0a2c9031c8952183"
DESCENT = "R791-original-real-descent-and-eta-basis-inputs.json.gz"
DESCENT_SHA = "24a894163f136a4e8c71b117e373f8fafb66a6e0c94b4efe3f141f78bb39b968"
SELECTED = "R794-selected-original-low-degree-eta-basis.json.gz"
SELECTED_SHA = "5b96f623e1f43d834a7db21064ff2cb101284b9a4038e5434eb291b6e73f6e0f"
GAMMA_SHA = "cf37105d407ace9df6b86a80d112b58915202bfecfc9e2fd118f4be76af2b1d0"
PHI21 = (1, -1, 0, 1, -1, 0, 1, 0, -1, 1, 0, -1, 1)
CANDIDATES = (0, 3, 1, 21, 15)
DEGREES = (1485, 1521, 1602, 1674, 1728)
LABELS = {"R792", "R735", "R791", "R794"}


BETA_SCHEMAS = {
    "R792-original-beta-composition": {
        "core_sha256": "7b7a5483e560f2d244092af486c8aed606b18c1f3557dddb3b850a290b4e343d",
        "certificate_name": "p41-original-beta-composition-certificate.json",
        "point_key": "point_spec", "manifest": "R792-stage-manifest.json.gz",
        "bundle": "R792-retained-producer-inputs.tar.gz",
        "parent_groups": {"R735", "R775", "R786", "R787", "R790", "R791"}},
    "R792-original-beta-from-R824-relation": {
        "core_sha256": "a8a33d32b19525896a137fcf02c3fbf07ced88207839e9c89f16c9c527e827bf",
        "certificate_name": "p41-original-beta-from-R824-relation-certificate.json",
        "point_key": "point_stage", "manifest": "R792-R824-stage-manifest.json.gz",
        "bundle": "R792-R824-retained-producer-inputs.tar.gz",
        "parent_groups": {"R735", "R775", "R786", "R824", "R790", "R791"}},
}


def beta_schema(spec):
    value = BETA_SCHEMAS[spec["result"]]
    assert spec["core_sha256"] == value["core_sha256"]
    assert spec["certificate_name"] == value["certificate_name"]
    return value


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("All new exact point arithmetic belongs to public repository Actions.")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


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


def same_producer(left, right):
    for key in ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "certificate_name"):
        assert str(left[key]) == str(right[key]), ("producer identity", key)
    name = left["certificate_name"]
    assert left["files"][name] == right["files"][name]
    for name in set(left["files"]) & set(right["files"]):
        assert left["files"][name] == right["files"][name]


def reduce_word(coefficients):
    answer = list(coefficients)
    while len(answer) > 12:
        leading, shift = answer[-1], len(answer)-13
        if leading:
            for j, coefficient in enumerate(PHI21):
                answer[shift+j] -= leading*coefficient
        assert answer[-1] == 0
        answer.pop()
    return tuple(answer+[0]*(12-len(answer)))


def shift_word(word, exponent):
    assert len(word) == 12 and exponent >= 0
    return reduce_word([0]*exponent+list(word))


class Retained:
    def __init__(self, root, label, spec):
        self.directory, self.label, self.spec = Path(root)/label, label, spec
        path = self.directory/"full-outputs-manifest.json"
        assert sha(path) == spec["manifest_sha256"]
        manifest = read(path)
        assert manifest["result"] == spec["result"]
        self.files = {row["file"]: row for row in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        self.checked = set()
        run, receipt, initial = (self.raw(name) for name in
            ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert str(run["workflow_run_id"]) == str(spec["run_id"])
        assert run["source_commit"] == initial["source_commit"] == spec["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert run["result"] == initial["result"] == spec["result"]
        if label == "R735":
            assert "result" not in receipt and receipt["p"] == 41
        else:
            assert receipt["result"] == spec["result"]
        assert receipt["complete"] is True and receipt["source_sha256"] == spec["core_sha256"]
        if label in ("R791", "R794"):
            assert "core_receipt_sha256" not in run
            assert initial["job"]["core_sha256"] == spec["core_sha256"]
        else:
            assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
            assert initial["core_sha256"] == spec["core_sha256"]
        self.initial = initial
        certificate = spec["certificate_name"]
        assert self.files[certificate]["sha256"] == spec["files"][certificate] == receipt["certificate_sha256"]
        self.certificate = self.raw(certificate)
        assert self.certificate["complete"] is True
        if label == "R735":
            assert certificate == MODEL and self.files[certificate]["sha256"] == MODEL_SHA
            identity = self.certificate["identity"]
            assert identity["source_sha256"] == spec["core_sha256"]
            assert identity["p"] == 41 and identity["python_flint"] == "0.9.0"
            self.tag = None
        else:
            assert self.certificate["result"] == spec["result"]
            self.tag = self.certificate["configuration"]
            assert self.tag["source_sha256"] == spec["core_sha256"] and self.tag["python_flint"] == "0.9.0"

    def raw(self, name, expected=None):
        assert Path(name).name == name
        row = self.files[name]
        if expected is not None:
            assert row["sha256"] == expected
        if name in self.spec["files"]:
            assert row["sha256"] == self.spec["files"][name]
        path = self.directory/name
        if name not in self.checked:
            assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
            self.checked.add(name)
        return read(path)

    def stage(self, spec):
        assert plain_spec(spec) == plain_spec(self.files[spec["file"]])
        value = self.raw(spec["file"], spec["sha256"])
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def cert_stage(self, name, digest=None):
        specs = {row["file"]: row for row in self.certificate["stages"]}
        if digest is not None:
            assert specs[name]["sha256"] == digest
        return self.stage(specs[name])

    def source(self, name):
        return dict(plain_spec(self.files[name]), producer=self.label)


class PointArithmetic:
    def __init__(self, field, sigma, ratios):
        self.L, self.b, self.sigma, self.ratios = field, field.gen, sigma, ratios
        self.units = (field.one, field.zeta, field.zeta**2)

    def check(self, point):
        if point is not None:
            x, y = point
            assert y*y == x**3+self.b, "Point left the original target C_b."
        return point

    def encode(self, point):
        self.check(point)
        if point is None:
            return {"status": "infinity", "projective_coordinates": ["0", "1", "0"]}
        return {"status": "finite", "x_original_L": point[0].encode(),
                "y_original_L": point[1].encode(), "projective_z": "1"}

    def decode(self, data):
        if data["status"] == "infinity":
            assert data["projective_coordinates"] == ["0", "1", "0"]
            return None
        assert data["status"] == "finite" and data["projective_z"] == "1"
        return self.check((self.L.decode(data["x_original_L"]), self.L.decode(data["y_original_L"])))

    def negate(self, point):
        return None if point is None else self.check((point[0], -point[1]))

    def unit(self, point, exponent):
        assert exponent in (0, 1, 2)
        return None if point is None else self.check((self.units[exponent]*point[0], point[1]))

    def add(self, left, right):
        self.check(left); self.check(right)
        if left is None:
            return right, "left_point_is_O"
        if right is None:
            return left, "right_point_is_O"
        x1, y1 = left
        x2, y2 = right
        if x1 == x2:
            if y1 == -y2:
                return None, "opposite_points_including_equal_two_torsion"
            assert y1 == y2 and y1
            slope = 3*x1*x1/(2*y1)
            branch = "doubling_with_nonzero_y"
        else:
            slope = (y2-y1)/(x2-x1)
            branch = "secant_with_distinct_x"
        x3 = slope*slope-x1-x2
        y3 = slope*(x1-x3)-y1
        return self.check((x3, y3)), branch

    def transport(self, point, exponent):
        assert 0 <= exponent <= 7
        if point is None:
            return None
        x, y = point
        for _ in range(exponent):
            x, y = self.sigma(x), self.sigma(y)
        rho = self.ratios[exponent]
        return self.check((x/(rho*rho), y/(rho*rho*rho)))


class BudgetStop(RuntimeError):
    pass


class Job:
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(args.proof) == self.item["R804_proof_sha256"]
        assert sha(args.interface) == self.item["R804_point_interface_sha256"]
        assert sha(args.field_core) == self.item["field_core_sha256"] == FIELD_CORE_SHA
        assert flint.__version__ == "0.9.0"
        assert self.item["selected_candidate_indices"] == list(CANDIDATES)
        assert self.item["selected_addition_node_count"] == 8
        assert set(self.item["retained_artifacts"]) == LABELS
        self.inputs = {label: Retained(args.retained, label, spec)
                       for label, spec in self.item["retained_artifacts"].items()}
        r792, r735, r791, r794 = (self.inputs[label] for label in ("R792", "R735", "R791", "R794"))
        beta_input = beta_schema(r792.spec)
        assert r791.spec["result"] == "R791-original-Hom-Galois-and-eta-inputs"
        assert r794.spec["result"] == "R794-original-low-degree-eta-basis"
        for label in ("R735", "R791"):
            same_producer(r792.tag["retained_artifacts"][label], self.inputs[label].spec)
            same_producer(r792.initial["job"]["retained_artifacts"][label], self.inputs[label].spec)
        same_producer(r794.tag["retained_artifacts"]["R791"], r791.spec)
        same_producer(r794.initial["job"]["retained_artifacts"]["R791"], r791.spec)
        assert r791.tag["field_helper_sha256"] == r792.tag["field_core_sha256"] == FIELD_CORE_SHA
        assert r791.tag["retained_inputs"][MODEL] == MODEL_SHA
        assert r791.tag["retained_inputs"]["R754-gamma-descent.json.gz"] == GAMMA_SHA
        assert r791.tag["retained_inputs"]["p41-original-period-and-Hom-kernel-certificate.json"] == \
            "da4ef0eeac285da5cf32ad1372155dbb9d03917c18044b81b8236fac6e51107c"
        self.hom = r791.cert_stage(HOM, HOM_SHA)
        self.descent = r791.cert_stage(DESCENT, DESCENT_SHA)
        assert self.hom["gamma_order"] == 21 and self.hom["gamma_seventh_power"] == "zeta^2"
        assert self.hom["Phi21_ascending"] == list(PHI21)
        assert self.hom["all_84_coordinates_verified"] is True
        assert self.hom["all_three_actions_integral_unimodular"] is True
        assert self.hom["remaining_elliptic_factor_included"] is False
        assert self.descent["selected_real_map_recipe"] == "f+c(f)"
        assert self.descent["selected_real_map_degree"] == "3618"
        assert self.descent["selected_real_map_Hom_coordinates"] == ["0", "0", "0", "0", "1", "0", "-1", "0", "0", "0", "0", "0"]
        for key in ("unknown_original_kappa_set_to_one", "original_vdagger_v_replaced_by_scalar", "original_q_alpha_or_c1_changed"):
            assert self.descent[key] is False
        self.selected = r794.cert_stage(SELECTED, SELECTED_SHA)
        assert self.selected["selected_candidate_indices"] == list(CANDIDATES)
        assert self.selected["original_kappa_e_R_q_c0_c1_preserved"] is True
        self.maps = {row["candidate_index"]: row for row in self.selected["selected_maps"]}
        assert len(self.maps) == 5
        for candidate, degree in zip(CANDIDATES, DEGREES):
            row = self.maps[candidate]
            assert int(row["map_degree"]) == degree
            assert len(row["original_Hom_integer_column"]) == 12
            assert len(row["a_in_Q_T_mod_Phi21"]) == 12
            assert all(value[1] == "1" for value in row["a_in_Q_T_mod_Phi21"])
        spec = importlib.util.spec_from_file_location("R804_frozen_original_field", args.field_core)
        self.field_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.field_module)
        self.model = r735.certificate
        self.L = self.field_module.QKField(self.field_module.dp(self.model["minimal_polynomial"]))
        assert self.L.degree == 7
        self.rho = self.L.decode(self.hom["field_rho"])
        self.sigma_b = self.L.decode(self.hom["field_sigma_b"])
        self.sigma = self.field_module.Composer(self.sigma_b)
        ratios = [self.L.decode(value) for value in self.hom["rho_iterates_zero_through_seven"]]
        assert len(ratios) == 8 and all(ratios)
        assert ratios[0] == 1 and ratios[1] == self.rho and ratios[7] == self.L.zeta**2
        self.points = PointArithmetic(self.L, self.sigma, ratios)
        certificate = r792.certificate
        assert certificate["p"] == 41 and certificate["original_map_index"] == 4
        assert certificate["original_map_degree"] == "1206"
        assert certificate["actual_beta_C_computed"] is True and certificate["actual_real_descent_image_computed"] is True
        assert certificate["original_A_coordinate_lift_computed"] is False
        assert certificate["actual_heights_or_uniformity_computed"] is False
        inventory = r792.stage(certificate["stage_manifest"])
        inventory_rows = {row["file"]: row for row in inventory["files"]}
        assert certificate["stage_manifest"]["file"] == beta_input["manifest"]
        point_spec = certificate[beta_input["point_key"]]
        assert plain_spec(point_spec) == plain_spec(inventory_rows[point_spec["file"]])
        if r792.spec["result"] == "R792-original-beta-from-R824-relation":
            assert certificate["original_y_ratio_preserved"] is True
            assert certificate["synthetic_R787_producer_or_relation_file_created"] is False
            assert certificate["original_R824_denominator_and_content_reinserted"] is False
        self.original_point = r792.stage(point_spec)
        self.original_point_spec = r792.source(point_spec["file"])
        assert self.original_point["original_map_index"] == 4 and self.original_point["original_map_degree"] == "1206"
        assert self.original_point["original_c1"] == 4424 and self.original_point["original_c0_image"] == "O"
        assert self.original_point["actual_beta_C_computed"] is True
        assert self.original_point["actual_real_descent_image_computed"] is True
        assert self.original_point["original_A_coordinate_lift_computed"] is False
        self.tag = {"result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R804_proof_sha256": sha(args.proof), "R804_point_interface_sha256": sha(args.interface),
            "field_core_sha256": FIELD_CORE_SHA, "retained_artifacts": self.item["retained_artifacts"],
            "actual_beta_input_result": r792.spec["result"],
            "actual_beta_input_point_field": beta_input["point_key"],
            "p": 41, "original_model_certificate_sha256": MODEL_SHA,
            "original_target": "C_b:y^2=x^3+b; L=Q(b,zeta); original b",
            "original_map_index": 4, "original_map_degree": "1206", "original_c1": 4424,
            "selected_candidate_indices": list(CANDIDATES), "selected_addition_node_count": 8,
            "Hom_word_basis": "1,T,...,T^11 modulo original Phi21; zeta=T^14; zeta^2=T^7",
            "T_seventh_power": "zeta^2", "Galois_transport": "D_(rho_j^-1) sigma^j; original R791 field data",
            "original_A_coordinate_lift_computed": False,
            "R803_global_M6_coordinates_consumed": False,
            "old_beta_periods_Hom_matrices_or_Laurent_recomputed": False}
        self.additions = []

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes-15:
            raise BudgetStop("Completed source-bound exact point nodes retained for continuation.")

    def path(self, name):
        assert name.startswith("R804-") and Path(name).name == name
        return self.out/(name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        data = read(path)
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def store(self, name, value):
        save(self.path(name), dict(value, complete=True, configuration=self.tag))
        print(json.dumps({"stage": name, "seconds": time.monotonic()-self.started}), flush=True)
        return self.cached(name)

    def conjugate(self, value):
        return self.L.elt(value.a-value.b, -value.b)

    def reference(self):
        name = "R804-reference-original-R792-beta"
        word = (1,)+(0,)*11
        old = self.cached(name)
        if old is not None:
            assert old["source_original_point"] == self.original_point_spec
            return {"name": name, "spec": file_spec(self.path(name)), "word": word,
                    "point": self.points.decode(old["point"])}
        self.budget()
        data = self.original_point
        if data["point_status"] == "infinity":
            assert data["beta_C"] == data["real_descent_image"] == "O"
            point = None
        else:
            assert data["point_status"] == "finite"
            point = self.points.check((self.L.decode(data["x_original_L"]), self.L.decode(data["y_original_L"])))
            assert self.conjugate(point[0]) == self.L.zeta**2*point[0]
            assert self.conjugate(point[1]) == -point[1]
        self.store(name, {"point": self.points.encode(point), "Hom_word": [str(v) for v in word],
            "source_original_point": self.original_point_spec, "source_model": self.inputs["R735"].source(MODEL),
            "original_elliptic_equation_verified": True, "old_beta_recomputed": False,
            "original_c0_translation_added": False})
        return {"name": name, "spec": file_spec(self.path(name)), "word": word, "point": point}

    def node(self, name, operation, sources, word, compute):
        name = "R804-point-node-"+name
        assert len(word) == 12
        dependency_specs = [source["spec"] for source in sources]
        old = self.cached(name)
        if old is not None:
            assert old["operation"] == operation and old["sources"] == dependency_specs
            assert old["Hom_word"] == [str(x) for x in word]
            point = self.points.decode(old["point"])
        else:
            self.budget()
            point, branch = compute()
            self.points.check(point)
            if not any(word):
                assert point is None, "The zero Hom word must specialize to O."
            self.store(name, {"operation": operation, "sources": dependency_specs,
                "Hom_word": [str(x) for x in word], "point": self.points.encode(point),
                "actual_point_branch": branch, "original_elliptic_equation_verified": True,
                "specialized_point_comparison_not_Hom_inequality_selects_addition_branch": True,
                "nonzero_Hom_word_was_allowed_to_specialize_to_O": True})
        return {"name": name, "spec": file_spec(self.path(name)), "word": word, "point": point}

    def unit(self, name, node, exponent=0, sign=1):
        assert exponent in (0, 1, 2) and sign in (-1, 1)
        word = tuple(sign*x for x in shift_word(node["word"], 14*exponent))
        def calculate():
            point = self.points.unit(node["point"], exponent)
            return (self.points.negate(point) if sign == -1 else point), "exact_CM_unit_and_sign"
        return self.node(name, {"kind": "CM_unit", "zeta_exponent": exponent, "sign": sign}, [node], word, calculate)

    def transport(self, name, node, exponent):
        return self.node(name, {"kind": "original_T_transport", "power": exponent,
                "rho_input_index": exponent, "source_original_Galois_stage": self.inputs["R791"].source(HOM)},
            [node], shift_word(node["word"], exponent),
            lambda: (self.points.transport(node["point"], exponent), "exact_sigma_on_entire_L_point_then_original_target_transport"))

    def add(self, name, left, right):
        assert name not in self.additions
        self.additions.append(name)
        return self.node(name, {"kind": "selected_Hom_addition"}, [left, right],
            tuple(a+b for a, b in zip(left["word"], right["word"])),
            lambda: self.points.add(left["point"], right["point"]))

    def selected_output(self, candidate, node):
        expected = self.maps[candidate]
        word = tuple(int(value[0]) for value in expected["a_in_Q_T_mod_Phi21"])
        assert node["word"] == word, ("Short addition chain differs from actual original Hom", candidate)
        name = "R804-selected-original-CM-point-candidate-"+str(candidate).zfill(2)
        payload = {"candidate_index": candidate, "map_degree": str(expected["map_degree"]),
            "original_Hom_integer_column": expected["original_Hom_integer_column"],
            "actual_R794_a_in_Q_T_mod_Phi21": expected["a_in_Q_T_mod_Phi21"],
            "computed_short_chain_Hom_word": [str(x) for x in node["word"]],
            "source_selected_map_stage": self.inputs["R794"].source(SELECTED),
            "source_final_point_node": node["spec"], "point": self.points.encode(node["point"]),
            "actual_original_Hom_word_matched": True, "actual_g_at_original_c1_computed": True,
            "original_elliptic_equation_verified": True, "original_c0_image": "O",
            "global_polar_divisor_eta_or_height_computed": False}
        old = self.cached(name)
        if old is None:
            self.store(name, payload)
        else:
            for key, value in payload.items():
                assert old[key] == value
        return file_spec(self.path(name))

    def vbeta(self, reference):
        name = "R804-original-vbeta-isogeny-consistency"
        old = self.cached(name)
        if old is not None:
            assert old["source_original_point"] == self.original_point_spec
            assert old["actual_original_isogeny_image_verified"] is True
            return file_spec(self.path(name))
        self.budget()
        point, branch = self.points.add(reference["point"], self.points.negate(self.points.unit(reference["point"], 2)))
        if self.original_point["point_status"] == "infinity":
            expected = None
        else:
            expected = (self.L.decode(self.original_point["x_real_descent_Fb"]),
                        self.L.decode(self.original_point["y_real_descent_Fb"]))
            assert all(not value.b for value in expected)
            self.points.check(expected)
        assert point == expected
        if point is not None:
            assert all(self.conjugate(value) == value and not value.b for value in point)
        self.store(name, {"point": self.points.encode(point), "actual_point_branch": branch,
            "point_model": "B=Res_(Q(b)/Q) C_b, primitive original A_42 image; original b",
            "equation": "q_R([c1-c0])=v*beta=[1-zeta^2]*beta_C",
            "source_original_point": self.original_point_spec,
            "source_original_real_descent": self.inputs["R791"].source(DESCENT),
            "source_original_beta_node": reference["spec"],
            "selected_real_map_Hom_coordinates": self.descent["selected_real_map_Hom_coordinates"],
            "original_elliptic_equation_verified": True,
            "actual_original_isogeny_image_verified": True,
            "original_Fb_coordinates_verified": True,
            "original_v_and_kappa_preserved": True, "unknown_original_kappa_set_to_one": False,
            "original_vdagger_v_replaced_by_scalar": False,
            "original_A_coordinate_lift_computed": False,
            "global_polar_divisors_eta_values_or_heights_computed": False})
        return file_spec(self.path(name))

    def run(self):
        final = self.out/FINAL
        if final.exists():
            certificate = read(final)
            assert certificate["result"] == RESULT and certificate["complete"] is True
            assert certificate["configuration"] == self.tag
            manifest_spec = certificate["stage_manifest"]
            assert file_spec(self.out/manifest_spec["file"]) == manifest_spec
            for row in read(self.out/manifest_spec["file"])["files"]:
                assert file_spec(self.out/row["file"]) == row
        else:
            f = self.reference()
            t1 = self.transport("T1-f", f, 1)
            t2 = self.transport("T2-f", t1, 1)
            t4 = self.transport("T4-f", t2, 2)
            t6 = self.transport("T6-f", t4, 2)
            t7 = self.transport("T7-f", t6, 1)
            z2f = self.unit("zeta2-f", f, 2)
            assert t7["point"] == z2f["point"] and t7["word"] == z2f["word"]
            phase_name = "R804-original-T7-CM-phase-check"
            if self.cached(phase_name) is None:
                self.store(phase_name, {"T7_point": t7["spec"], "zeta2_point": z2f["spec"],
                    "actual_reference_point_identity_verified": True,
                    "original_Hom_T_order": 21, "T7_was_not_replaced_by_identity": True,
                    "source_original_Galois_stage": self.inputs["R791"].source(HOM)})
            minus_t1 = self.unit("minus-T1-f", t1, sign=-1)
            c0 = self.add("candidate0", minus_t1, t6)
            c3a = self.add("candidate3-step1", self.unit("minus-T2-f", t2, sign=-1), z2f)
            c3b = self.add("candidate3-step2", c3a, self.unit("minus-zeta2-T1-f", t1, 2, -1))
            c3 = self.add("candidate3", c3b, self.unit("minus-zeta2-T4-f", t4, 2, -1))
            c1a = self.add("candidate1-step1", f, self.unit("minus-zeta-T2-f", t2, 1, -1))
            c1b = self.add("candidate1-step2", self.unit("zeta2-candidate1-step1", c1a, 2),
                          self.transport("T1-candidate1-step1", c1a, 1))
            c1 = self.transport("candidate1-final-T2", c1b, 2)
            c21 = self.add("candidate21", minus_t1, self.unit("minus-zeta-T6-f", t6, 1, -1))
            c15 = self.add("candidate15", f, c0)
            assert len(self.additions) == 8
            nodes = {0: c0, 3: c3, 1: c1, 21: c21, 15: c15}
            outputs = {str(candidate): self.selected_output(candidate, nodes[candidate]) for candidate in CANDIDATES}
            image = self.vbeta(f)
            rows = [file_spec(path) for path in sorted(self.out.glob("R804-*.json.gz"))
                    if path.name != "R804-stage-manifest.json.gz"]
            self.store("R804-stage-manifest", {"files": rows})
            certificate = {"result": RESULT, "complete": True, "configuration": self.tag, "p": 41,
                "selected_candidate_indices": list(CANDIDATES), "selected_map_degrees": list(DEGREES),
                "selected_point_stages": outputs, "reference_beta_stage": f["spec"],
                "original_vbeta_stage": image, "original_T7_phase_check": file_spec(self.path(phase_name)),
                "selected_addition_node_count": 8, "selected_addition_node_names": self.additions,
                "all_five_original_CM_points_computed": True,
                "all_five_short_Hom_words_match_original_R794": True,
                "all_original_elliptic_point_equations_verified": True,
                "point_branches_include_O_opposites_doubling_and_two_torsion": True,
                "point_collisions_not_decided_by_Hom_labels": True,
                "original_T7_equals_zeta2_preserved": True,
                "actual_original_vbeta_verified": True,
                "R803_global_M6_coordinates_consumed": False,
                "old_beta_periods_Hom_matrices_or_Laurent_recomputed": False,
                "original_A_coordinate_lift_computed": False,
                "global_polar_divisors_computed": False, "eta_values_computed": False, "heights_computed": False,
                "stage_manifest": file_spec(self.path("R804-stage-manifest")),
                "seconds": time.monotonic()-self.started}
            save(final, certificate)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(final),
            "all_five_original_CM_points_computed": True, "actual_original_vbeta_verified": True,
            "original_A_coordinate_lift_computed": False,
            "global_polar_divisors_eta_values_or_heights_computed": False})
        return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "proof", "interface", "field-core", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    try:
        return Job(args).run()
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "completed_exact_point_nodes_preserved": True})
        raise


if __name__ == "__main__":
    sys.exit(main())
