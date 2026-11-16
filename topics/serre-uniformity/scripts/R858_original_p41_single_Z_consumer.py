#!/usr/bin/env python3
"""R858: the original p=41 single Z and five elliptic derivative rows.

Mathematics is executable only in the named public Actions repository.  This
driver imports a separately source-pinned, pure-Python original-field ball
helper.  It consumes certified R854 response balls, never an auxiliary-prime
candidate, and cuts the old unit-chart DAG at its four linear responses.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import sys
import time
import traceback
from fractions import Fraction

RESULT = "R858-original-p41-single-Z-and-elliptic-rows"
FINAL = "p41-original-p41-single-Z-and-elliptic-rows-certificate.json"
PREFIX = "R858-single-Z-"
REPOSITORY = "Rogerhu12/math-research-public"
P, E, DEGREE = 41, 7, 14
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256",
             "manifest_sha256", "configuration_sha256")
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
INPUT_KEYS = (
    "R852_certificate", "coefficient_program", "exact_C_coordinates",
    "response_certificate", "four_response_balls", "implicit_CM",
    "galois", "tangents",
)
RESPONSE_IDS = {
    "A0": "df6f79bf61aa7e45aa64e7c8c41d71931149981dc98e2c15c85f2d84bc61a003",
    "A1": "36654715fce2f382459a02034ad56a2ae3f02f7cb560476722b414ae5e69bd7b",
    "B0": "34111de3daeff665213d65dbee07fd2595797fbbaff1d57db1cc58faf3bd3c7e",
    "B1": "992e92890e48c629ed973846db3d5255e9021dff9a3ab38bb848dcb206c98bcf",
}
SOLVE_ID = "1fd48e17a8801b2125bb57c1ce0811d4736c7bcd5aabd07dd4a7d83d103d9d98"
CHAIN = ((2, 1, 1), (4, 2, 2), (5, 4, 1), (10, 5, 5),
         (20, 10, 10), (21, 20, 1), (42, 21, 21))
ROOT_NAMES = ("beta_C_x", "beta_C_y", "D_1", "D_2", "D_3", "D_4", "D_5")
STRATEGY = {
    "original_p": P,
    "original_map_index": 4,
    "original_map_degree": 1206,
    "original_point": "f4(c1), roots beta_C_x and beta_C_y; not f_R(c1)",
    "original_parameter": "z=a-1",
    "original_differential": "dx/(2*y)",
    "coefficient_field": "Q41[B,s]/(original_F_B,s^2+3); B=lambda*b",
    "coefficient_order": "B^0..B^6,s*B^0..s*B^6",
    "absolute_precision_unit": "v_B=7*v41",
    "ramification_index": E,
    "residue_degree": 2,
    "DAG_operation": "prune original 839-node program at four original responses",
    "unit_chart_solve_recomputed": False,
    "exact_C_coordinates_recomputed": False,
    "whole_expression_Galois_action": True,
    "multiplication_chain": [1, 2, 4, 5, 10, 20, 21, 42],
    "addition_Z_law": "Z(P+Q)=Z(P)+Z(Q)+original_secant(P,Q)",
    "beta_recurrence": "beta_(a+b)=beta_a+beta_b+original_slope(aP,bP)",
    "base_Z": "(Z(42P)-beta42)/42",
    "psi42_or_psi42_derivative_computed": False,
    "formal_branch": "t=-x/y,u=t^2*x,A=b*t^6; v_B(A)>0,v_B(u-1)>0",
    "series_H": "H_n=[A^(n-1)](9*u+4)/(u^2*(3*u-2)); u=1-delta",
    "delta_coefficients": "delta_n=binom(3*n-2,n-1)/n in Z",
    "tail_rule": "N>=2; (N+1)*vB(A)-vB(t)-7*ceil_log41(6*(N+1)-1)",
    "trace14": "(1+c_Bfixed)*sum_(k=0..6) sigma^k; c_Bfixed(s)=-s",
    "elliptic_row": "c_chi*(Trace14(C_j*Z+D_j)/2)",
    "c_chi_preserved_symbolically": True,
    "Y_Picard_or_global_Hecke_correction_computed": False,
    "actual_height_computed": False,
    "auxiliary_518_balls_used_as_p41": False,
    "budget_target_precision_and_term_limit_excluded_from_mathematical_identity": True,
}


class BudgetStop(RuntimeError):
    pass


class TermLimit(RuntimeError):
    pass


def authorize():
    assert os.environ.get("GITHUB_ACTIONS") == "true", "New arithmetic is public-Actions-only."
    assert os.environ.get("GITHUB_REPOSITORY") == REPOSITORY
    assert re.fullmatch(r"[0-9a-f]{40}", os.environ.get("GITHUB_SHA", ""))


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda: stream.read(1 << 20), b""):
            h.update(part)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name+".tmp")
    encoded = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temp.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(encoded)
    else:
        temp.write_bytes(encoded)
    temp.replace(path)


def plain(row):
    result = {k: row[k] for k in ("file", "bytes", "sha256")}
    assert Path(result["file"]).name == result["file"] and "\\" not in result["file"]
    assert isinstance(result["bytes"], int) and result["bytes"] >= 0
    assert re.fullmatch(r"[0-9a-f]{64}", result["sha256"])
    return result


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def bound(directory, row):
    row = plain(row)
    path = Path(directory)/row["file"]
    assert path.is_file() and path.stat().st_size == row["bytes"], str(path)
    assert sha(path) == row["sha256"], str(path)
    return path


def load_module(path, expected_sha):
    path = Path(path)
    assert sha(path) == expected_sha
    entry = importlib.util.spec_from_file_location("R858_source_bound_ball_arithmetic", path)
    module = importlib.util.module_from_spec(entry)
    sys.modules[entry.name] = module
    entry.loader.exec_module(module)
    return module


def source_identity(item):
    result = {key: item[key] for key in BASE_KEYS}
    result["selected_files_sha256"] = fingerprint({
        name: plain(row) for name, row in sorted(item["files"].items())})
    result["certificate"] = plain(item["certificate"])
    return result


class Source:
    """Selected original bytes; the public wrapper verifies producer receipts."""
    def __init__(self, label, item, retained):
        self.label, self.item = label, item
        self.directory = Path(item.get("directory", Path(retained)/label))
        self.files = {name: plain(row) for name, row in item["files"].items()}
        assert all(name == row["file"] for name, row in self.files.items())
        assert MANIFEST in self.files
        assert self.files[MANIFEST]["sha256"] == item["manifest_sha256"]
        manifest = read(bound(self.directory, self.files[MANIFEST]))
        assert manifest["result"] == item["result"]
        recorded = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(recorded) == len(manifest["files"])
        if "manifest_file_count" in item:
            assert len(recorded) == item["manifest_file_count"]
        recorded[MANIFEST] = self.files[MANIFEST]
        for name, row in self.files.items():
            if name != REFERENCE:
                assert recorded[name] == row
            bound(self.directory, row)
        if REFERENCE in self.files:
            ref = read(self.directory/REFERENCE)
            assert ref["manifest_sha256"] == item["manifest_sha256"]
        self.identity = source_identity(item)
        assert self.files[item["certificate"]["file"]] == plain(item["certificate"])
        self.certificate = read(self.directory/item["certificate"]["file"])
        assert self.certificate["result"] == item["result"]
        self.tag = self.certificate["configuration"]
        assert fingerprint(self.tag) == item["configuration_sha256"]
        assert self.tag["source_sha256"] == item["core_sha256"]
        if label != "R854":
            assert self.certificate["complete"] is True
        self.memo = {item["certificate"]["file"]: self.certificate}

    def stage(self, row, complete=True):
        row = plain(row)
        assert self.files[row["file"]] == row
        if row["file"] not in self.memo:
            self.memo[row["file"]] = read(bound(self.directory, row))
        value = self.memo[row["file"]]
        assert value["configuration"] == self.tag
        if complete:
            assert value["complete"] is True
        return value


class Job:
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.item = read(args.config)
        assert self.item["result"] == RESULT and self.item["p"] == P
        assert self.item["producer_inputs_pending"] is False
        assert self.item["core_sha256"] == sha(__file__)
        assert self.item["ball_helper"] == "R858_original_p41_ball_arithmetic.py"
        self.work_precision = int(self.item.get("exact_leaf_B_precision", 256))
        assert self.work_precision >= 1
        self.target_Z = int(self.item.get("target_Z_B_precision", 7))
        self.target_rows = int(self.item.get("target_elliptic_row_B_precision", 7))
        assert self.target_Z >= 1 and self.target_rows >= 1
        self.maximum_terms = int(self.item.get("maximum_series_terms", 10000))
        assert self.maximum_terms >= 2
        self.block_size = int(self.item.get("series_block_size", 16))
        assert 1 <= self.block_size <= 256
        topic = Path(self.item.get("topic_directory", Path(__file__).resolve().parent.parent))
        assert set(("SP", "ZA", "41S", "method", "consumer")) <= set(self.item["proofs"])
        for row in self.item["proofs"].values():
            path = Path(row["path"])
            assert not path.is_absolute() and ".." not in path.parts
            assert sha(topic/path) == row["sha256"]
        helper_path = Path(self.item.get("script_directory", Path(__file__).resolve().parent))/self.item["ball_helper"]
        self.helper = load_module(helper_path, self.item["ball_helper_sha256"])
        self.NeedPrecision = self.helper.NeedPrecision
        self.sources = {label: Source(label, row, args.retained)
                        for label, row in self.item["sources"].items()}
        assert set(("R852", "R854", "CM", "R791")) <= set(self.sources)
        assert set(INPUT_KEYS) == set(self.item["inputs"])
        self.input_values = {}
        for key in INPUT_KEYS:
            row = self.item["inputs"][key]
            source = self.sources[row["source_group"]]
            self.input_values[key] = source.stage(row, complete=(key != "response_certificate"))
        self.program = self.input_values["coefficient_program"]
        self.C_exact = self.input_values["exact_C_coordinates"]
        self.implicit = self.input_values["implicit_CM"]
        self.hom = self.input_values["galois"]
        self.tangents = self.input_values["tangents"]
        self.response = self.input_values["four_response_balls"]
        self.response_certificate = self.input_values["response_certificate"]
        self.description = self.implicit["original_field"]
        self.validate_sources()
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "p": P,
            "ball_helper_sha256": self.item["ball_helper_sha256"],
            "proofs": self.item["proofs"],
            "source_identities": {label: source.identity for label, source in sorted(self.sources.items())},
            "inputs": {key: {"source_group": row["source_group"], **plain(row)}
                       for key, row in sorted(self.item["inputs"].items())},
            "field": self.description,
            "exact_leaf_B_precision": self.work_precision,
            "series_block_size": self.block_size,
            "strategy": STRATEGY,
        }
        self.out.mkdir(parents=True, exist_ok=True)
        self.field = None
        self.refs, self.balls, self.node_specs = {}, {}, {}
        self.context = {"stage": "source-audit"}
        self.current_spec = None

    def validate_sources(self):
        c852 = self.input_values["R852_certificate"]
        assert c852 == self.sources["R852"].certificate
        assert c852["complete"] is True
        assert c852["original_one_Z_coefficient_program_certified"] is True
        assert c852["original_map_index"] == 4 and c852["original_map_degree"] == 1206
        assert c852["coefficient_program"] == plain(self.item["inputs"]["coefficient_program"])
        assert c852["five_exact_C_coordinates"] == plain(self.item["inputs"]["exact_C_coordinates"])
        assert self.program["node_count"] == len(self.program["nodes"]) == 839
        assert self.program["imported_original_node_count"] == 733
        assert self.program["original_sigma_applies_to_entire_unit_chart"] is True
        assert self.program["original_T7_phase_preserved"] is True
        assert self.C_exact["coefficient_program"] == c852["coefficient_program"]
        assert self.C_exact["five_C_coefficients_nonzero"] is True
        assert self.C_exact["five_C_coefficients_Q_linearly_independent"] is True
        assert self.C_exact["basis"] == "1,b,...,b^6,zeta,zeta*b,...,zeta*b^6; original b and zeta"
        assert self.implicit["original_relation_exactly_defined_by_unit_chart"] is True
        assert self.implicit["original_finite_CM_y_expression_defined"] is True
        assert self.implicit["unit_chart_solve"]["free_column"] == 1186
        assert self.implicit["unit_chart_solve"]["other_free_values"] == "zero"
        assert self.description["dimension_over_Q"] == 280  # Original M+, not L.
        assert len(self.description["integral_B_minimal_polynomial"]) == 8
        assert self.description["original_b_replaced_by_another_twist"] is False
        assert self.sources["R854"].tag["field"] == self.description
        t854 = self.sources["R854"].tag
        for key, value in (("original_p", 41), ("original_map_index", 4),
                           ("unknown_dimension", 2420), ("original_free_column", 1186),
                           ("full_cleared_equation_rows", 2560), ("full_L_coordinate_dimension", 14)):
            assert t854[key] == value
        assert t854["auxiliary_518_balls_are_p41_inputs"] is False
        assert t854["unaccepted_A1_candidate_consumed"] is False
        for label in ("CM", "R791"):
            old = c852["configuration"]["source_identities"][label]
            assert {key: old[key] for key in BASE_KEYS} == {
                key: self.sources[label].identity[key] for key in BASE_KEYS}
        oldcm = t854["source_identities"]["CM"]
        assert {key: oldcm[key] for key in BASE_KEYS} == {
            key: self.sources["CM"].identity[key] for key in BASE_KEYS}
        assert self.response_certificate == self.sources["R854"].certificate
        assert self.response_certificate["actual_original_p41_four_response_balls_certified"] is True
        assert self.response_certificate["four_response_balls"] == plain(self.item["inputs"]["four_response_balls"])
        assert self.response["labels"] == ["A0", "A1", "B0", "B1"]
        assert self.response["actual_original_p41_four_response_balls_certified"] is True
        assert self.response["B_response_free1186_constant_preserved"] is True
        assert self.response["original_CM_scale_applied_again"] is False
        assert self.response["exact_functionals"] == self.implicit["linear_responses"]
        assert self.response["numerators"]["shape"] == [4, 1]
        assert self.response["numerators"]["p"] == 41
        assert self.response["numerators"]["basis"] == "B^0..B^6,s*B^0..s*B^6; s^2=-3"
        assert self.response["absolute_B_precision"] == self.response_certificate["actual_response_absolute_B_precision"]
        assert self.tangents["original_map_index"] == 4
        assert str(self.tangents["original_map_degree"]) == "1206"
        assert self.tangents["original_c1_slash_count"] == 1
        self.nodes = {}
        leaf_count, response_count = 0, 0
        for node in self.program["nodes"]:
            payload = {k: v for k, v in node.items() if k != "id"}
            assert fingerprint(payload) == node["id"]
            assert node["id"] not in self.nodes
            assert all(x in self.nodes for x in node["inputs"])
            op = node["operation"]
            if op == "source_field_element":
                leaf_count += 1
                key = node["source_key"]
                if key == "actual_L_coefficients_h_i_over_ds_at_c1":
                    assert plain(node["source"]) == plain(self.item["inputs"]["tangents"])
                    assert node["exact_value"] == self.tangents[key][node["source_index"]]
                else:
                    assert key == "rho_iterates_zero_through_seven"
                    assert plain(node["source"]) == plain(self.item["inputs"]["galois"])
                    assert node["exact_value"] == self.hom[key][node["source_index"]]
                assert node["source"]["source_group"] == "R791"
            elif op == "linear_response":
                response_count += 1
                label = node["response"]
                assert node["id"] == RESPONSE_IDS[label]
                assert node["inputs"] == [SOLVE_ID]
                assert node["functional"] == self.implicit["linear_responses"][label]
            elif op == "original_L_automorphism":
                assert node["fixes_zeta"] is True
                assert node["applies_to_all_exact_leaves_and_constants"] is True
                assert node["original_unit_chart_is_conjugated_as_a_whole"] is True
                assert node["field_generator_image_key"] == "field_sigma_b"
                assert plain(node["original_transport_source"]) == plain(self.item["inputs"]["galois"])
                assert 0 <= int(node["power"]) < 7
            elif op == "unit_chart_solve":
                assert node["id"] == SOLVE_ID and node["free_column"] == 1186
                assert node["shape"] == [2420, 2420]
                assert plain(node["exact_recipe_source"]) == plain(self.item["inputs"]["implicit_CM"])
            elif op == "original_field_generator":
                assert node["name"] in ("b", "zeta")
                assert plain(node["exact_field_source"]) == plain(self.item["inputs"]["implicit_CM"])
            else:
                assert op in ("rational", "multiply", "add", "negate", "inverse")
            self.nodes[node["id"]] = node
        assert leaf_count == 17 and response_count == 4
        self.roots = {name: self.program["roots"][name] for name in ROOT_NAMES}
        assert self.roots["beta_C_x"] != self.program["roots"]["f_R_c1_x"]
        assert self.roots["beta_C_y"] != self.program["roots"]["f_R_c1_y"]
        self.needed = set()
        def visit(key):
            if key in self.needed:
                return
            node = self.nodes[key]
            self.needed.add(key)
            if node["operation"] != "linear_response":
                for parent in node["inputs"]:
                    visit(parent)
        for root in self.roots.values():
            visit(root)
        assert SOLVE_ID not in self.needed
        self.ordered_needed = [node["id"] for node in self.program["nodes"] if node["id"] in self.needed]
        self.five = self.C_exact["five_coefficients"]
        assert [row["j"] for row in self.five] == [1, 2, 3, 4, 5]
        for row, definition in zip(self.five, self.program["five_original_one_Z_rows"]):
            j = row["j"]
            assert row["nonzero"] is True and len(row["exact_original_L_coordinates"]) == 14
            assert row["C_root"] == definition["C"] == self.program["roots"]["C_"+str(j)]
            assert row["D_root"] == definition["D"] == self.roots["D_"+str(j)]
            assert str(row["original_p"]) == definition["p"]
            assert str(row["original_q"]) == definition["q"]
        self.sigma_b = self.hom["field_sigma_b"]

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes:
            raise BudgetStop("Only complete source-bound stages are reused on continuation.")

    def path(self, stem):
        assert re.fullmatch(r"[A-Za-z0-9_.-]+", stem)
        return self.out/(PREFIX+stem+".json.gz")

    def cache(self, stem):
        path = self.path(stem)
        if not path.exists():
            return None
        value = read(path)
        assert value["result"] == RESULT and value["configuration"] == self.tag
        assert value["complete"] is True
        return value

    def put(self, stem, value):
        # A completed operation is committed before the next budget boundary.
        # This avoids discarding newly completed arithmetic merely because the
        # wall-clock budget expired while that operation was returning.
        assert self.cache(stem) is None, "An immutable completed stage must not be overwritten."
        data = {**value, "result": RESULT, "configuration": self.tag, "complete": True}
        save(self.path(stem), data)
        row = spec(self.path(stem))
        print(json.dumps({"stage": row["file"], "bytes": row["bytes"],
                          "seconds": time.monotonic()-self.started}), flush=True)
        return row

    def ref(self, stem):
        assert self.cache(stem) is not None
        return spec(self.path(stem))

    def data_ball(self, value):
        return self.field.from_data(value)

    def ball_info(self, value):
        return {"ball": value.to_data(),
                "absolute_B_precision": value.absolute_precision,
                "absolute_p41_precision_rational": [value.absolute_precision, E],
                "valuation_B_lower_bound": value.valuation_lower_bound(),
                "valuation_B": None if value.is_zero_ball else value.valuation(),
                "zero_residue_ball_is_not_exact_zero": value.is_zero_ball}

    def scalar(self, q):
        return self.field.exact_rational(q, self.work_precision)

    def context_precision_error(self, error):
        if getattr(error, "node", None) is None:
            error.node = dict(self.context)
        return error

    def need(self, reason, **bounds):
        raise self.NeedPrecision(reason, node=dict(self.context), bounds=bounds)

    def require_precision(self, value, target, subject):
        if value.absolute_precision < target:
            self.need("Certified ball precision is below the requested bound.",
                      subject=subject, available_absolute_B_precision=value.absolute_precision,
                      required_absolute_B_precision=target,
                      deficit_B=target-value.absolute_precision)

    def arithmetic_context(self, stage, **details):
        self.context = {"stage": stage, **details}
        self.budget()

    def initialize(self):
        self.arithmetic_context("source-audit")
        stem = "source-audit"
        if self.cache(stem) is None:
            self.put(stem, {
                "source_identities": self.tag["source_identities"],
                "inputs": self.tag["inputs"],
                "original_839_nodes_hash_and_topological_order_verified": True,
                "original_17_field_elements_matched_to_R791": True,
                "pruned_root_ids": self.roots,
                "pruned_evaluable_node_ids": self.ordered_needed,
                "actual_pruned_evaluable_node_count": len(self.ordered_needed),
                "unit_chart_solve_cut_at_the_four_original_responses": True,
                "new_unit_chart_solves": 0,
                "old_C_rank_recomputed": False,
                "whole_expression_Galois_semantics_preserved": True,
                "source_four_response_B_precision": self.response["absolute_B_precision"],
                "original_point_is_f4_not_fR": True,
            })
        self.refs["source_audit"] = self.ref(stem)
        self.field = self.helper.Field(self.description, default_precision=self.work_precision,
                                       budget=self.budget)
        stem = "field-model"
        if self.cache(stem) is None:
            self.put(stem, {
                "original_Mplus_description_dimension": 280,
                "coefficient_field_dimension_over_Q41": 14,
                "ramification_index": 7, "residue_degree": 2,
                "source_field_description": self.description,
                "original_sigma_b_source": self.item["inputs"]["galois"],
                "original_sigma_b": self.sigma_b,
                "B_fixed_conjugation": "B maps to B; s maps to -s",
                "helper_source_sha256": self.item["ball_helper_sha256"],
                "auxiliary_prime_input_imported": False,
            })
        self.refs["field_model"] = self.ref(stem)
        self.arithmetic_context("four-response-import")
        stem = "four-response-import"
        value = self.cache(stem)
        if value is None:
            response_balls = {label: self.field.from_response(self.response, label)
                              for label in ("A0", "A1", "B0", "B1")}
            self.put(stem, {
                "source_four_response_balls": self.item["inputs"]["four_response_balls"],
                "labels": ["A0", "A1", "B0", "B1"],
                "response_node_ids": RESPONSE_IDS,
                "balls": {label: self.ball_info(ball) for label, ball in response_balls.items()},
                "common_denominator_B_power": self.response["common_denominator_B_power"],
                "common_denominator_p41_power": self.response["common_denominator_p41_power"],
                "source_absolute_B_precision": self.response["absolute_B_precision"],
                "original_CM_scale_applied_again": False,
                "original_free1186_constant_preserved": True,
            })
            value = self.cache(stem)
        self.responses = {label: self.data_ball(info["ball"]) for label, info in value["balls"].items()}
        self.refs["four_response_import"] = self.ref(stem)
        self.C_balls = []
        for row in self.five:
            j = row["j"]
            stem = "exact-C-"+str(j)
            self.arithmetic_context(stem)
            value = self.cache(stem)
            if value is None:
                c = self.field.exact_bzeta(row["exact_original_L_coordinates"], self.work_precision)
                self.put(stem, {
                    "j": j, "C_root": row["C_root"], "D_root": row["D_root"],
                    "source_exact_C_coordinates": self.item["inputs"]["exact_C_coordinates"],
                    "original_p": row["original_p"], "original_q": row["original_q"],
                    "reduced_rational_coordinates_reused_without_rank_or_Hom_recomputation": True,
                    **self.ball_info(c),
                })
                value = self.cache(stem)
            self.C_balls.append(self.data_ball(value["ball"]))
        # A lower valuation bound suffices to control multiplication by C_j.
        # Coefficient uncertainty itself remains visible to the final ball test.
        self.effective_Z_target = max(self.target_Z,
            *(self.target_rows-c.valuation_lower_bound() for c in self.C_balls))

    def eval_node(self, key):
        if key in self.balls:
            return self.balls[key]
        assert key in self.needed
        node = self.nodes[key]
        stem = "algebraic-node-"+key
        saved = self.cache(stem)
        if saved is not None:
            assert saved["node_id"] == key and saved["operation"] == node["operation"]
            result = self.data_ball(saved["ball"])
            self.balls[key], self.node_specs[key] = result, self.ref(stem)
            return result
        op = node["operation"]
        args = [] if op == "linear_response" else [self.eval_node(x) for x in node["inputs"]]
        self.arithmetic_context("original-DAG-node", node_id=key, operation=op,
                                inputs=node["inputs"], source_program=self.item["inputs"]["coefficient_program"])
        try:
            if op == "rational":
                result = self.scalar(Fraction(int(node["numerator"]), int(node["denominator"])))
            elif op == "add":
                assert len(args) == 2
                result = args[0]+args[1]
            elif op == "multiply":
                assert len(args) == 2
                result = args[0]*args[1]
            elif op == "negate":
                assert len(args) == 1
                result = -args[0]
            elif op == "inverse":
                assert len(args) == 1
                result = args[0]**-1
            elif op == "linear_response":
                result = self.responses[node["response"]]
            elif op == "source_field_element":
                result = self.field.exact_bzeta(node["exact_value"], self.work_precision)
            elif op == "original_field_generator":
                coordinates = [0]*14
                coordinates[1 if node["name"] == "b" else 7] = 1
                result = self.field.exact_bzeta(coordinates, self.work_precision)
            elif op == "original_L_automorphism":
                assert len(args) == 1
                result = args[0].automorphism(self.sigma_b, power=int(node["power"]))
            else:
                raise AssertionError("Unimplemented or forbidden original DAG operation: "+op)
        except self.NeedPrecision as exc:
            raise self.context_precision_error(exc)
        parents = ([self.refs["four_response_import"]] if op == "linear_response"
                   else [self.node_specs[x] for x in node["inputs"]])
        self.node_specs[key] = self.put(stem, {
            "node_id": key, "operation": op, "original_node": node,
            "source_program": self.item["inputs"]["coefficient_program"],
            "parent_stages": parents,
            "unit_chart_solve_executed": False,
            "automorphism_applies_to_the_whole_input_ball": op == "original_L_automorphism",
            **self.ball_info(result),
        })
        self.balls[key] = result
        return result

    def base_point(self):
        stem = "base-point"
        value = self.cache(stem)
        if value is None:
            x = self.eval_node(self.roots["beta_C_x"])
            y = self.eval_node(self.roots["beta_C_y"])
            b = self.field.exact_bzeta([0, 1]+[0]*12, self.work_precision)
            self.arithmetic_context(stem)
            residual = y*y-x*x*x-b
            assert residual.is_zero_ball, "Original point ball violates its source curve equation."
            self.put(stem, {
                "point": "original f4(c1), not the real-descended f_R point",
                "x_root": self.roots["beta_C_x"], "y_root": self.roots["beta_C_y"],
                "parent_stages": [self.node_specs[self.roots["beta_C_x"]],
                                  self.node_specs[self.roots["beta_C_y"]]],
                "x": self.ball_info(x), "y": self.ball_info(y), "b": self.ball_info(b),
                "curve_residual": self.ball_info(residual),
                "curve_residual_contains_zero": True,
                "exact_curve_membership_is_from_original_DAG_proof": True,
            })
            value = self.cache(stem)
        self.refs["base_point"] = self.ref(stem)
        return {"x": self.data_ball(value["x"]["ball"]),
                "y": self.data_ball(value["y"]["ball"]),
                "beta": self.scalar(0), "multiple": 1}, self.data_ball(value["b"]["ball"])

    def multiples(self, base, b):
        points, point_refs = {1: base}, {1: self.refs["base_point"]}
        for total, na, nb in CHAIN:
            stem = "multiple-"+str(total).zfill(6)
            value = self.cache(stem)
            if value is None:
                aa, bb = points[na], points[nb]
                self.arithmetic_context(stem, multiple=total, summands=[na, nb])
                denominator = 2*aa["y"] if na == nb else bb["x"]-aa["x"]
                numerator = 3*aa["x"]**2 if na == nb else bb["y"]-aa["y"]
                try:
                    slope = numerator/denominator
                except self.NeedPrecision as exc:
                    exc.bounds.update({"denominator": self.ball_info(denominator),
                        "accurate_nonzero_reason": "Original non-torsion point; distinct positive multiples or doubling."})
                    raise self.context_precision_error(exc)
                x = slope*slope-aa["x"]-bb["x"]
                y = slope*(aa["x"]-x)-aa["y"]
                beta = aa["beta"]+bb["beta"]+slope
                residual = y*y-x*x*x-b
                assert residual.is_zero_ball, "Multiplication-chain ball violates the original curve."
                self.put(stem, {
                    "multiple": total, "summand_multiples": [na, nb],
                    "parent_stages": [point_refs[na], point_refs[nb]],
                    "x": self.ball_info(x), "y": self.ball_info(y),
                    "beta": self.ball_info(beta), "slope": self.ball_info(slope),
                    "actual_denominator": self.ball_info(denominator),
                    "denominator_valuation_identified": True,
                    "curve_residual": self.ball_info(residual),
                    "curve_residual_contains_zero": True,
                    "definition": "Z(nP)=n*Z(P)+beta_n; beta1=0",
                    "addition_formula_source": self.item["proofs"]["ZA"],
                    "psi_or_Dlog_psi_computed": False,
                })
                value = self.cache(stem)
            assert value["multiple"] == total and value["summand_multiples"] == [na, nb]
            points[total] = {name: self.data_ball(value[name]["ball"]) for name in ("x", "y", "beta")}
            points[total]["multiple"] = total
            point_refs[total] = self.ref(stem)
        self.refs["multiplication_chain"] = [point_refs[n] for n, _, _ in CHAIN]
        return points[42], point_refs[42]

    def formal_point(self, q, qspec, b):
        stem = "formal-point-42"
        value = self.cache(stem)
        if value is None:
            self.arithmetic_context(stem)
            try:
                t = -q["x"]/q["y"]
                tv = t.valuation()
                inverse_t = t**-1
                u = t*t*q["x"]
                A = b*t**6
                error = u-1
                av, ev = A.valuation_lower_bound(), error.valuation_lower_bound()
                if av <= 0:
                    if A.is_zero_ball:
                        self.need("The formal-disk A=b*t^6 ball has not certified positive valuation.",
                                  A=self.ball_info(A), t=self.ball_info(t), required_A_valuation_lower_bound=1)
                    raise AssertionError("Actual v_B(A)<=0 contradicts the original [42] formal-disk source.")
                if ev <= 0:
                    if error.is_zero_ball:
                        self.need("The actual u=t^2*x ball has not identified the original u(0)=1 branch.",
                                  u_minus_one=self.ball_info(error), required_valuation_lower_bound=1)
                    raise AssertionError("Actual v_B(u-1)<=0 contradicts the original [42] branch source.")
                rational_part = (3*u-2)*inverse_t
            except self.NeedPrecision as exc:
                raise self.context_precision_error(exc)
            self.put(stem, {
                "original_multiple_42": qspec,
                "t": self.ball_info(t), "u": self.ball_info(u), "A": self.ball_info(A),
                "u_minus_one": self.ball_info(error), "inverse_t": self.ball_info(inverse_t),
                "rational_part": self.ball_info(rational_part),
                "actual_t_valuation_B": tv,
                "certified_A_valuation_B_lower_bound": av,
                "certified_u_minus_one_valuation_B_lower_bound": ev,
                "actual_original_formal_branch_certified": True,
                "rational_part_uses_actual_u_not_a_truncation": True,
                "field_extension_degree84_materialized": False,
            })
            value = self.cache(stem)
        self.refs["formal_point_42"] = self.ref(stem)
        return value

    @staticmethod
    def ceil_log41(n):
        assert n >= 1
        power, exponent = 1, 0
        while power < n:
            power *= 41
            exponent += 1
        return exponent

    def tail_cutoff(self, formal, target):
        A = formal["certified_A_valuation_B_lower_bound"]
        t = formal["actual_t_valuation_B"]
        assert A >= 1
        for N in range(2, self.maximum_terms+1):
            self.budget()
            L = self.ceil_log41(6*(N+1)-1)
            lower = (N+1)*A-t-7*L
            if lower >= target:
                stem = "tail-N"+str(N).zfill(6)+"-T"+str(target).zfill(6)
                if self.cache(stem) is None:
                    self.put(stem, {
                        "source_formal_point": self.refs["formal_point_42"],
                        "last_included_n": N, "first_omitted_n": N+1,
                        "A_valuation_B_lower_bound": A, "t_valuation_B": t,
                        "ceil_log41_of_6_first_omitted_minus_one": L,
                        "full_tail_B_precision": lower,
                        "target_B_precision": target,
                        "all_omitted_terms_certified": True,
                        "argument": "n*A-t-7*log41(6*n-1) strictly increases for n>=3, A>=1; integer ceil gives a weaker initial bound",
                        "proof": self.item["proofs"]["method"],
                        "no_last_visible_coefficient_test_substituted": True,
                    })
                self.refs["full_tail_certificate"] = self.ref(stem)
                return N, lower
        raise TermLimit("No certified all-tail cutoff within maximum_series_terms; increase this control, not the mathematical source.")

    def prefix_cache(self, family):
        pattern = re.compile(re.escape(PREFIX+family)+r"(\d{6})\.json\.gz")
        choices = []
        for path in self.out.glob(PREFIX+family+"*.json.gz"):
            match = pattern.fullmatch(path.name)
            if match:
                choices.append((int(match.group(1)), path))
        result = []
        for n, path in sorted(choices):
            row = read(path)
            assert row["configuration"] == self.tag and row["complete"] is True
            assert row["result"] == RESULT and row["last_included_n"] == n
            result.append((n, row, spec(path)))
        return result

    def coefficients(self, N):
        """Exact integral series; H_n is h[n-1], never h[n]."""
        found = self.prefix_cache("coefficients-through-")
        adequate = [item for item in found if item[0] >= N]
        if adequate:
            _, value, source = min(adequate, key=lambda item: item[0])
            self.refs["H_coefficients"] = source
            return [int(x) for x in value["h_coefficients"]]
        if found:
            oldN, value, previous = max(found, key=lambda item: item[0])
            delta = [int(x) for x in value["delta_coefficients"]]
            square = [int(x) for x in value["delta_square_coefficients"]]
            cube = [int(x) for x in value["delta_cube_coefficients"]]
            den = [int(x) for x in value["denominator_coefficients"]]
            h = [int(x) for x in value["h_coefficients"]]
            assert all(len(v) == oldN for v in (delta, square, cube, den, h))
            start = oldN
        else:
            delta, square, cube, den, h = [0], [0], [0], [1], [13]
            start, previous = 1, None
        for k in range(start, N):
            self.arithmetic_context("exact-integral-H-coefficient", degree=k, H_index=k+1)
            numerator = math.comb(3*k-2, k-1)
            dk, remainder = divmod(numerator, k)
            assert remainder == 0
            delta.append(dk)
            square.append(sum(delta[i]*delta[k-i] for i in range(1, k)))
            cube.append(sum(square[i]*delta[k-i] for i in range(1, k)))
            den.append(-5*delta[k]+7*square[k]-3*cube[k])
            hk = -9*delta[k]-sum(den[i]*h[k-i] for i in range(1, k+1))
            h.append(hk)
            assert sum(den[i]*h[k-i] for i in range(k+1)) == -9*delta[k]
            through = k+1
            if through % self.block_size == 0 or through == N:
                stem = "coefficients-through-"+str(through).zfill(6)
                previous = self.put(stem, {
                    "last_included_n": through,
                    "h_coefficient_degree_interval": [0, through-1],
                    "H_n_is_h_coefficient_n_minus_one": True,
                    "delta_coefficients": [str(x) for x in delta],
                    "delta_square_coefficients": [str(x) for x in square],
                    "delta_cube_coefficients": [str(x) for x in cube],
                    "denominator_coefficients": [str(x) for x in den],
                    "h_coefficients": [str(x) for x in h],
                    "previous_complete_prefix": previous,
                    "formula": "(1-5*delta+7*delta^2-3*delta^3)*h=13-9*delta",
                    "all_new_coefficients_exact_integers_and_product_verified": True,
                    "completed_old_coefficient_prefix_recomputed": False,
                })
        # N>=2 in this consumer, so a completed prefix always exists here.
        self.refs["H_coefficients"] = previous
        return h

    def series_sum(self, formal, h, N):
        found = [row for row in self.prefix_cache("sum-through-") if row[0] <= N]
        if found:
            done, value, previous = max(found, key=lambda item: item[0])
            subtotal = self.data_ball(value["finite_integral_sum"]["ball"])
            power = self.data_ball(value["A_power_at_last_n"]["ball"])
            if done == N:
                self.refs["finite_series_sum"] = previous
                return subtotal
        else:
            done, subtotal, power, previous = 0, None, self.scalar(1), None
        A = self.data_ball(formal["A"]["ball"])
        inverse_t = self.data_ball(formal["inverse_t"]["ball"])
        terms = []
        for n in range(done+1, N+1):
            self.arithmetic_context("sigma-integral-sum", n=n, last_required_n=N)
            power = power*A
            term = power*inverse_t*Fraction(h[n-1], 6*n-1)
            subtotal = term if subtotal is None else subtotal+term
            terms.append({"n": n, "coefficient_H_n": str(h[n-1]),
                          "denominator_6n_minus_one": 6*n-1,
                          "absolute_B_precision": term.absolute_precision,
                          "valuation_B_lower_bound": term.valuation_lower_bound()})
            if n % self.block_size == 0 or n == N:
                stem = "sum-through-"+str(n).zfill(6)
                previous = self.put(stem, {
                    "last_included_n": n,
                    "source_formal_point": self.refs["formal_point_42"],
                    "source_H_coefficients": self.refs["H_coefficients"],
                    "previous_complete_partial_sum": previous,
                    "new_terms": terms,
                    "finite_integral_sum": self.ball_info(subtotal),
                    "A_power_at_last_n": self.ball_info(power),
                    "formula": "sum_(n=1..N) H_n*A^n/(t*(6*n-1))",
                    "all_actual_denominator_precision_losses_propagated": True,
                    "completed_partial_sum_recomputed": False,
                })
                terms = []
        self.refs["finite_series_sum"] = previous
        return subtotal

    def original_Z(self, q, formal):
        rational = self.data_ball(formal["rational_part"]["ball"])
        self.arithmetic_context("base-Z-prerequisites")
        self.require_precision(rational, self.effective_Z_target, "actual (3u-2)/t")
        self.require_precision(q["beta"], self.effective_Z_target, "beta42")
        N, tail_precision = self.tail_cutoff(formal, self.effective_Z_target)
        stem = "base-Z-through-"+str(N).zfill(6)
        value = self.cache(stem)
        if value is None:
            h = self.coefficients(N)
            subtotal = self.series_sum(formal, h, N)
            self.arithmetic_context("base-Z-combination", last_included_n=N)
            finite_Q = rational+subtotal
            ZQ = finite_Q.clamp(min(finite_Q.absolute_precision, tail_precision))
            ZP = (ZQ-q["beta"])/42
            self.put(stem, {
                "original_point": self.refs["base_point"],
                "multiple_42": self.refs["multiplication_chain"][-1],
                "source_formal_point": self.refs["formal_point_42"],
                "H_coefficients": self.refs["H_coefficients"],
                "finite_series_sum": self.refs["finite_series_sum"],
                "full_tail_certificate": self.refs["full_tail_certificate"],
                "last_included_n": N, "full_tail_B_precision": tail_precision,
                "finite_Z_at_42P": self.ball_info(finite_Q),
                "certified_Z_at_42P": self.ball_info(ZQ),
                "beta42": self.ball_info(q["beta"]),
                "original_Z": self.ball_info(ZP),
                "formula": "(Z(42P)-beta42)/42",
                "division_by_42_p41_unit": True,
                "original_mu3_splitting_and_sigma_normalization_preserved": True,
                "psi42_derivative_recomputed": False,
                "actual_original_41_base_Z_ball_computed": True,
                "actual_height_computed": False,
            })
            value = self.cache(stem)
        for key in ("H_coefficients", "finite_series_sum", "full_tail_certificate"):
            self.refs[key] = value[key]
        Z = self.data_ball(value["original_Z"]["ball"])
        self.refs["base_Z"] = self.ref(stem)
        self.arithmetic_context("base-Z-precision", last_included_n=N)
        self.require_precision(Z, self.effective_Z_target, "original Z_b(f4(c1))")
        return Z

    def orbit(self, Z):
        source = self.refs["base_Z"]
        stem = "seven-Z-conjugates-"+source["sha256"][:24]
        value = self.cache(stem)
        if value is None:
            self.arithmetic_context("seven-Z-conjugates")
            values = [Z if k == 0 else Z.automorphism(self.sigma_b, power=k) for k in range(7)]
            assert all(x.absolute_precision == Z.absolute_precision for x in values)
            self.put(stem, {
                "source_original_Z": source,
                "original_sigma_b_source": self.item["inputs"]["galois"],
                "conjugate_balls": [{"sigma_power": k, **self.ball_info(x)} for k, x in enumerate(values)],
                "all_seven_original_conjugates_transport_certified": True,
                "source_formula": "Z_(sigma^k b)(sigma^k P)=sigma^k(Z_b(P))",
                "original_T_phases_untouched": True,
                "new_seven_sigma_integrals_computed": False,
                "same_absolute_B_precision_from_unique_place_isometry": True,
            })
        self.refs["original_seven_conjugates"] = self.ref(stem)

    def elliptic_rows(self, Z):
        self.refs["elliptic_rows"] = []
        for row, C in zip(self.five, self.C_balls):
            j = row["j"]
            source_Z = self.refs["base_Z"]
            stem = "elliptic-row-"+str(j)+"-Z-"+source_Z["sha256"][:24]
            value = self.cache(stem)
            if value is None:
                D = self.eval_node(row["D_root"])
                self.arithmetic_context("elliptic-row-trace", j=j, original_D_root=row["D_root"])
                base = C*Z+D
                conjugates = [base if k == 0 else base.automorphism(self.sigma_b, power=k) for k in range(7)]
                trace7 = conjugates[0]
                for term in conjugates[1:]:
                    trace7 = trace7+term
                trace14 = trace7+trace7.conjugate()
                normalized = trace14/2
                self.put(stem, {
                    "j": j, "original_p": row["original_p"], "original_q": row["original_q"],
                    "source_original_Z": source_Z,
                    "source_C": self.ref("exact-C-"+str(j)),
                    "source_D": self.node_specs[row["D_root"]],
                    "original_C_root": row["C_root"], "original_D_root": row["D_root"],
                    "C_Z_plus_D": self.ball_info(base),
                    "seven_whole_element_conjugates": [self.ball_info(x) for x in conjugates],
                    "trace_L_over_Q41_sqrt_minus3": self.ball_info(trace7),
                    "trace14": self.ball_info(trace14),
                    "elliptic_row_divided_by_c_chi": self.ball_info(normalized),
                    "target_coefficient_field": "Q41 embedded in the original rank14 ball field",
                    "rational_descent_reason": "relative degree7 trace, then B-fixed s conjugation",
                    "normalized_trace_degree": 14, "original_outer_factor": 7,
                    "final_rational_scale": ["1", "2"],
                    "original_c_chi": "symbolic unchanged multiplier; not evaluated or set equal to 1",
                    "formula": "7*tr_chi(C_j*Z+D_j)=c_chi/2*Trace14(C_j*Z+D_j)",
                    "degree84_extension_trace_substituted": False,
                    "actual_elliptic_first_derivative_row_ball_computed": True,
                    "actual_Y_Picard_period_computed": False,
                    "actual_height_computed": False,
                })
                value = self.cache(stem)
            self.refs["elliptic_rows"].append(self.ref(stem))
            self.arithmetic_context("elliptic-row-precision", j=j)
            answer = self.data_ball(value["elliptic_row_divided_by_c_chi"]["ball"])
            self.require_precision(answer, self.target_rows, "elliptic row divided by unchanged c_chi")

    def failure(self, kind, error):
        data = error.to_data() if hasattr(error, "to_data") else {"reason": str(error)}
        data["kind"] = kind
        data["context"] = dict(self.context)
        data["original_four_response_source"] = self.item["inputs"]["four_response_balls"]
        data["available_response_absolute_B_precision"] = self.response["absolute_B_precision"]
        data["unaccepted_A1_or_auxiliary_prime_candidate_used"] = False
        data["exact_zero_or_original_point_exclusion_proved"] = False
        if kind == "NeedPrecision":
            bounds = data.get("bounds") or {}
            deficit = max(1, int(bounds.get("deficit_B", 1)))
            data["suggested_next_response_absolute_B_precision_trial"] = max(1,
                int(self.response["absolute_B_precision"])+max(7, deficit))
            data["suggested_precision_is_not_a_guaranteed_sufficient_bound"] = True
        stem = "stop-"+fingerprint(data)[:32]
        # Error recording itself must remain possible after the time budget.
        if not self.path(stem).exists():
            save(self.path(stem), {"result": RESULT, "configuration": self.tag,
                 "complete": True, "stop_record": data,
                 "completed_only_as_an_honest_execution_record": True})
        self.refs["stop_record"] = spec(self.path(stem))
        return data

    def finish(self, stop=None):
        files = []
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name.startswith(PREFIX+"stage-manifest-") or path.name == PREFIX+"current.json.gz":
                continue
            value = read(path)
            assert value["result"] == RESULT and value["configuration"] == self.tag
            assert value["complete"] is True
            files.append(spec(path))
        stem = "stage-manifest-"+fingerprint(files)[:24]
        if not self.path(stem).exists():
            save(self.path(stem), {"result": RESULT, "configuration": self.tag,
                 "complete": True, "files": files,
                 "all_complete_mathematical_and_execution_records_bound": True,
                 "original_source_tags_not_overwritten": True})
        manifest = spec(self.path(stem))
        current = {
            "result": RESULT, "configuration": self.tag, "complete": False,
            "context": dict(self.context), "completed_stage_manifest": manifest,
            "references": self.refs, "requested_Z_B_precision": self.target_Z,
            "requested_elliptic_row_B_precision": self.target_rows,
            "stop": stop,
            "continuation_rule": "same bound original source and tag; reuse all completed stages before new arithmetic",
        }
        save(self.path("current"), current)
        self.current_spec = spec(self.path("current"))
        z_precision = None
        if "base_Z" in self.refs:
            value = read(bound(self.out, self.refs["base_Z"]))
            z_precision = value["original_Z"]["absolute_B_precision"]
        row_precisions = []
        for item in self.refs.get("elliptic_rows", []):
            value = read(bound(self.out, item))
            row_precisions.append(value["elliptic_row_divided_by_c_chi"]["absolute_B_precision"])
        complete = (stop is None and z_precision is not None and z_precision >= self.target_Z
                    and len(row_precisions) == 5 and min(row_precisions) >= self.target_rows)
        final = {
            "result": RESULT, "configuration": self.tag, "complete": complete,
            "p": 41, "original_map_index": 4, "original_map_degree": 1206,
            "requested_Z_absolute_B_precision": self.target_Z,
            "requested_elliptic_row_absolute_B_precision": self.target_rows,
            "effective_Z_absolute_B_precision_for_C_multiplication": getattr(self, "effective_Z_target", None),
            "actual_Z_absolute_B_precision": z_precision,
            "actual_elliptic_row_absolute_B_precisions": row_precisions,
            "original_response_absolute_B_precision": self.response["absolute_B_precision"],
            "exact_original_point_expression_source_verified": "source_audit" in self.refs,
            "actual_original_p41_response_balls_consumed": "four_response_import" in self.refs,
            "actual_original_41_base_Z_computed": z_precision is not None,
            "actual_original_41_base_Z_certified_to_positive_absolute_B_precision": z_precision is not None and z_precision >= 1,
            "original_seven_conjugates_transport_verified": "original_seven_conjugates" in self.refs,
            "actual_elliptic_first_derivative_rows_computed": len(row_precisions) == 5,
            "original_c_chi_preserved_symbolically": True,
            "source_audit": self.refs.get("source_audit"),
            "field_model": self.refs.get("field_model"),
            "four_response_import": self.refs.get("four_response_import"),
            "base_point": self.refs.get("base_point"),
            "multiplication_chain": self.refs.get("multiplication_chain", []),
            "formal_point_42": self.refs.get("formal_point_42"),
            "H_coefficients": self.refs.get("H_coefficients"),
            "finite_series_sum": self.refs.get("finite_series_sum"),
            "full_tail_certificate": self.refs.get("full_tail_certificate"),
            "base_Z": self.refs.get("base_Z"),
            "original_seven_conjugates": self.refs.get("original_seven_conjugates"),
            "elliptic_rows": self.refs.get("elliptic_rows", []),
            "stage_manifest": manifest, "resume_state": self.current_spec,
            "stop_record": self.refs.get("stop_record"), "stop": stop,
            "unit_chart_solve_recomputed": False,
            "old_exact_C_coordinates_or_rank_recomputed": False,
            "auxiliary_518_balls_used_as_p41": False,
            "exact_expanded_rational_point_coordinates_certified": False,
            "original_CM_candidate_A1_accepted": False,
            "actual_Y_Picard_period_computed": False,
            "actual_global_Hecke_correction_computed": False,
            "actual_height_computed": False,
            "height_nonzero_proved": False,
            "all_p_uniformity_proved": False,
            "seconds": time.monotonic()-self.started,
        }
        save(self.out/FINAL, final)
        return final

    def run(self):
        try:
            self.initialize()
            base, b = self.base_point()
            q, qspec = self.multiples(base, b)
            formal = self.formal_point(q, qspec, b)
            Z = self.original_Z(q, formal)
            self.orbit(Z)
            self.elliptic_rows(Z)
            return self.finish(), 0
        except self.NeedPrecision as error:
            self.context_precision_error(error)
            return self.finish(self.failure("NeedPrecision", error)), 2
        except BudgetStop as error:
            return self.finish(self.failure("BudgetStop", error)), 124
        except TermLimit as error:
            return self.finish(self.failure("SeriesTermLimit", error)), 2


def main():
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--retained", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=60.0)
    args = parser.parse_args()
    started, job, final, error, code = time.monotonic(), None, None, None, 1
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        authorize()
        job = Job(args)
        final, code = job.run()
        assert code != 0 or final["complete"] is True
    except Exception as exc:
        error = {"type": type(exc).__name__, "message": str(exc),
                 "context": None if job is None else job.context}
        traceback.print_exc()
        if job is not None:
            try:
                final = job.finish(job.failure("UnexpectedError", exc))
            except Exception:
                traceback.print_exc()
        code = 1
    receipt = {
        "result": RESULT, "core_sha256": sha(__file__),
        "configuration": None if job is None else job.tag,
        "configuration_sha256": None if job is None else fingerprint(job.tag),
        "process_exit_code": code, "complete": bool(final and final["complete"]),
        "final_sha256": sha(args.output/FINAL) if (args.output/FINAL).exists() else None,
        "actual_original_41_base_Z_computed": bool(final and final["actual_original_41_base_Z_computed"]),
        "actual_Z_absolute_B_precision": None if final is None else final["actual_Z_absolute_B_precision"],
        "actual_elliptic_first_derivative_rows_computed": bool(final and final["actual_elliptic_first_derivative_rows_computed"]),
        "stop": None if final is None else final["stop"],
        "actual_Y_Picard_period_computed": False,
        "actual_height_computed": False,
        "error": error, "seconds": time.monotonic()-started,
    }
    save(args.output/"core-receipt.json", receipt)
    print(json.dumps({"result": RESULT, "exit_code": code, "complete": receipt["complete"],
          "actual_Z_absolute_B_precision": receipt["actual_Z_absolute_B_precision"],
          "stop_kind": None if receipt["stop"] is None else receipt["stop"]["kind"],
          "error": error, "seconds": receipt["seconds"]}), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
