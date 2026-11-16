#!/usr/bin/env python3
"""Continue an actual completed full-dual current using its necessary parity.

No primal current is an input.  The frozen full-dual arithmetic supplies the
original operator and the exact final verifier.  Seven old prime inverses solve
new digits; the full original output still verifies every proposed correction.
Old target, pairing, current, and any completed next-step/exact-witness work are
explicit immutable sources, never relabelled as freshly computed arithmetic.
"""
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

import flint
from flint import fmpq, fmpz_mat, nmod_mat, nmod_poly

RESULT = "R787-original-cleared-dual-CM-value-acceptance"
FINAL = "p41-original-cleared-dual-CM-value-acceptance-certificate.json"
PREFIX = "R787-cleared-dual-"
HALF = PREFIX+"half-"
ELL, N, D, RANK, T, LD, FREE = 1000000753, 1234, 1214, 1186, 20, 14, 1186
FULL_CORE = "bad9741493b550b0d3543ec953642c2b2f11f30da4433c9346f0c3215d415323"
ORIGINAL_CORE = "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
FIELD_CORE = "d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751"
PROOF = "281de249137d88da3c67a25261ca744bd513ecb15b49ffb0125d82f7fb6b7c6f"
NESTED_PROOF = "eb5893ec0b8dcc4dd256648a96daa7a605d4cb96efc94a5c42544c0c6dea572b"
FULL_METHOD = "c6ca7d3a8036c2c0b5cfca69fd66ca7108555fae9f90614d7e3618c3044288bd"
MANIFEST = "full-outputs-manifest.json"
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
STRATEGY = {
    "mode": "source-bound-full-dual-continuation-with-necessary-antilinear-parity",
    "input": "actual completed full-dual current, never primal 518 coordinates",
    "old_dual_core_sha256": "bad9741493b550b0d3543ec953642c2b2f11f30da4433c9346f0c3215d415323",
    "coefficient_order": "B^i*s^j*t^r, j outer then i then r; s^2=-3; B=lambda*b",
    "retained_half": "chi_m: first 140 coordinates for odd m, last 140 for even m",
    "representatives": "for each original B root choose the s root of original branch 0",
    "paired_completion": "chi_m(B,-s)=(-1)^(m-1)*chi_m(B,s)",
    "next_digit_rhs": "negative original positive residual after division by ell^n in all original coordinates",
    "representative_check": "all original square equations on all seven solved branches",
    "completed_correction_check": "all 2560*14 original output coordinates",
    "known_wrong_RR_vector_does_not_reject_q": True,
    "parity_rejection_requires_original_unit_operator_and_integral_exact_target": True,
    "exact_exit": "original full rational Theta identity and original free-1186 Delta",
    "number_of_reconstructed_rational_coordinates": 17920,
    "full_rational_unknown_dimension": 35840,
    "old_RHS_pairing_CM_inverses_or_completed_digits_recomputed": False,
    "old_completed_next_step_and_exact_witness_work_imported_explicitly": True,
    "new_precision_begins_after_actual_source_dual_digit": True,
    "runtime_budget_and_new_digit_limit_excluded_from_mathematical_identity": True}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name+".tmp")
    payload = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temp.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(payload)
    else:
        temp.write_bytes(payload)
    temp.replace(path)


def plain(value):
    result = {key: value[key] for key in ("file", "bytes", "sha256")}
    assert Path(result["file"]).name == result["file"]
    return result


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def shape(rows, height, width):
    assert len(rows) == height and all(len(row) == width for row in rows)


def load_module(name, path, expected):
    assert sha(path) == expected
    definition = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(definition)
    definition.loader.exec_module(module)
    return module


def source_identity(source):
    result = {key: source[key] for key in BASE}
    result.update(configuration_sha256=source["configuration_sha256"],
        selected_files_sha256=source["selected_files_sha256"],
        current=plain(source["current"]), exact_target=plain(source["exact_target"]),
        source_audit=plain(source["source_audit"]), source_dual_digits=source["source_dual_digits"])
    return result


class FullDualSource:
    def __init__(self, root, item, expanded, pairing):
        self.root, self.item = Path(root)/"FULL_DUAL", item
        assert item["result"] == RESULT and item["core_sha256"] == FULL_CORE
        assert item["expected_conclusion"] == "failure"
        manifest_path = self.root/MANIFEST
        assert spec(manifest_path) == {"file": MANIFEST, "bytes": item["manifest_bytes"],
                                      "sha256": item["manifest_sha256"]}
        manifest = read(manifest_path)
        assert manifest["result"] == RESULT
        self.inventory = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(self.inventory) == len(manifest["files"]) == item["manifest_file_count"]
        self.inventory[MANIFEST] = spec(manifest_path)
        self.files, self.verified = item["files"], set()
        assert fingerprint([self.files[name] for name in sorted(self.files)]) == item["selected_files_sha256"]
        for name, row in self.files.items():
            assert name == row["file"] and Path(name).name == name
            assert plain(row) == self.inventory[name]
        run, public = (self.get(name, tagged=False) for name in ("run-receipt.json", "public-actions-input.json"))
        assert run["result"] == public["result"] == RESULT
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        assert run["source_commit"] == public["source_commit"] == item["source_commit"]
        assert public["source_repository"] == "Rogerhu12/math-research-public"
        assert public["core_sha256"] == public["job"]["core_sha256"] == FULL_CORE
        assert public["wrapper_sha256"] == public["job"]["wrapper_sha256"] == item["wrapper_sha256"]
        assert public["expanded_sources"] == expanded
        assert public["job"]["completed_pairing_source"] == pairing
        assert run["complete"] is False and run["process_exit_code"] in item["accepted_checkpoint_exit_codes"]
        expected_readme = item["original_readme_sha256"]
        assert public["root_readme_sha256"] == expected_readme["root"]
        assert public["topic_readme_sha256"] == expected_readme["topic"]
        self.public, self.run = public, run
        current = self.get_spec(item["current"], tagged=False)
        self.tag = current["configuration"]
        assert self.tag["source_sha256"] == FULL_CORE and self.tag["result"] == RESULT
        assert fingerprint(self.tag) == item["configuration_sha256"]
        assert current["complete"] is True and current["full_square_modular_identity_verified"] is True
        assert current["prime"] == ELL and current["digits"] == item["source_dual_digits"] >= 1
        assert current["old_primal_precision_or_vector_reused_as_dual"] is False
        assert plain(current["exact_target"]) == plain(item["exact_target"])
        assert plain(current["source_audit"]) == plain(item["source_audit"])
        if "core-receipt.json" in self.files:
            receipt = self.get("core-receipt.json", tagged=False)
            assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
            assert receipt["result"] == RESULT and receipt["source_sha256"] == FULL_CORE
            assert receipt["complete"] is False
            if receipt.get("configuration") is not None:
                assert receipt["configuration"] == self.tag
        else:
            assert run["core_receipt_sha256"] is None
        target, audit = self.get_spec(item["exact_target"]), self.get_spec(item["source_audit"])
        assert target["old_CM_values_or_eZ_recomputed"] is False
        assert target["original_value_identity_not_yet_accepted"] is True
        assert audit["exact_target"] == plain(item["exact_target"])
        assert audit["old_prime_inverses_read_without_recomputation"] is True
        assert audit["old_primal_current_consumed"] is False
        assert audit["completed_original_pairing_reused_without_recomputation"] is True
        assert audit["pairing"] == {"source_group": "PAIRING", **plain(pairing["pairing"])}
        inputs = self.get("retained-inputs-receipt.json", tagged=False)
        assert inputs["result"] == RESULT and inputs["complete"] is True
        assert inputs["retained_sources"] == expanded and inputs["input_bundle"] == plain(item["input_bundle"])
        assert inputs["all_source_member_bytes_verified"] is True
        self.current, self.target, self.audit = current, target, audit
        self.identity = source_identity(item)

    def path(self, name):
        row = self.files[name]
        path = self.root/name
        if name not in self.verified:
            assert spec(path) == plain(row)
            self.verified.add(name)
        return path

    def get(self, name, tagged=True):
        value = read(self.path(name))
        if tagged:
            assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def get_spec(self, row, tagged=True):
        assert plain(row) == self.files[row["file"]]
        return self.get(row["file"], tagged)

    def reference(self, row):
        assert plain(row) == self.files[row["file"]]
        return {"source_group": "FULL_DUAL", **plain(row)}


def make_job_class(base):
    class HalfOperator(base.ClearedDualOperator):
        def load_old_branches(self):
            roots = self.selection["roots_B_s"]
            assert len(roots) == 14 and len({tuple(row) for row in roots}) == 14
            chosen_s = int(roots[0][1]) % ELL
            assert chosen_s and (chosen_s*chosen_s+3) % ELL == 0
            grouped = {}
            for branch, (bb, ss) in enumerate(roots):
                grouped.setdefault(int(bb) % ELL, {})[int(ss) % ELL] = branch
            assert len(grouped) == 7
            pairs = []
            for bb, pair in sorted(grouped.items()):
                assert set(pair) == {chosen_s, -chosen_s % ELL}
                pairs.append({"B_root": bb, "representative": pair[chosen_s],
                              "paired": pair[-chosen_s % ELL], "s_root": chosen_s})
            self.branch_pairs = pairs
            chosen = {row["representative"] for row in pairs}
            source = self.job.sources["R787"]
            for branch in range(14):
                self.job.budget()
                name = "R787-prime-1000000753-branch-"+str(branch).zfill(2)+".json.gz"
                data = source.get(name)
                assert data["prime"] == ELL and data["branch"] == branch
                assert data["roots_B_s"] == roots[branch]
                assert data["chart_sha256"] == source.files[base.CHART]["sha256"]
                assert data["actual_Schur_rank"] == RANK and data["selected_minor_det_mod_prime"] % ELL
                assert data["all_2560_original_uncleared_rows_verified"] is True
                shape(data["Schur_minor_inverse_mod_prime"], RANK, RANK)
                shape(data["C_J_pivot_columns"], N, RANK)
                shape(data["inverse_original_clear_multipliers"], 128, 20)
                row = {"source": source.files[name],
                    "inverse_clear": [nmod_poly(v, ELL) for v in data["inverse_original_clear_multipliers"]]}
                if branch in chosen:
                    row["Schur_inverse_transpose"] = nmod_mat(data["Schur_minor_inverse_mod_prime"], ELL).transpose()
                    row["C_J_pivot_transpose"] = nmod_mat(data["C_J_pivot_columns"], ELL).transpose()
                self.branches.append(row)
                del data

        def seven_branch_correction(self, rhs):
            shape(rhs["A"], N, 14)
            shape(rhs["P"], RANK, 14)
            shape(rhs["outside"], 140, 14)
            outside_rows = [[0]*14 for _ in range(2560)]
            for i, row in enumerate(self.outside):
                outside_rows[row] = [int(x) % ELL for x in rhs["outside"][i]]
            outside_evaluated = nmod_mat(outside_rows, ELL)*self.Et
            outside_columns = [[int(outside_evaluated[r, b]) for r in range(2560)] for b in range(14)]
            if any(x for row in rhs["outside"] for x in row):
                chi_out = self.clear_inverse_from_branch_columns(outside_columns)
                contribution = self.apply_mod(chi_out, ELL)
                assert contribution["outside"] == [[int(x) % ELL for x in row] for row in rhs["outside"]]
                bA = [[(a-b) % ELL for a, b in zip(left, right)]
                      for left, right in zip(rhs["A"], contribution["A"])]
                bP = [[(a-b) % ELL for a, b in zip(left, right)]
                      for left, right in zip(rhs["P"], contribution["P"])]
            else:
                bA, bP = rhs["A"], rhs["P"]
            Aeval, Peval = nmod_mat(bA, ELL)*self.Et, nmod_mat(bP, ELL)*self.Et
            columns = [None]*14
            for pair in self.branch_pairs:
                self.job.budget()
                b = pair["representative"]
                old = self.branches[b]
                aa = nmod_mat([[int(Aeval[i, b])] for i in range(N)], ELL)
                pp = nmod_mat([[int(Peval[i, b])] for i in range(RANK)], ELL)
                u0 = self.Ainvt*aa
                tt = old["Schur_inverse_transpose"]*(old["C_J_pivot_transpose"]*u0+pp)
                uu = u0+self.Ainvt*(self.FIt*tt)
                column = list(outside_columns[b])
                for i, row in enumerate(self.rowsJ):
                    column[row] = int(uu[i, 0])
                for i, row in enumerate(self.rowsI):
                    column[row] = -int(tt[i, 0]) % ELL
                paired = nmod_mat([column[20*m:20*(m+1)] for m in range(128)], ELL)*self.Jinv_prime_t
                original, opposite = [], []
                for m in range(128):
                    poly = nmod_poly([int(paired[m, r]) for r in range(20)], ELL)
                    value = (old["inverse_clear"][m]*poly) % self.gt_prime
                    block = [int(value[r]) for r in range(20)]
                    original.extend(block)
                    opposite.extend([x if m % 2 == 0 else -x % ELL for x in block])
                columns[b], columns[pair["paired"]] = original, opposite
            assert all(row is not None for row in columns)
            coefficient_rows = nmod_mat([list(row) for row in zip(*columns)], ELL)*self.Einvt
            result = self.to_blocks(base.integer_matrix(coefficient_rows))
            assert self.job.first_forbidden(result) is None
            actual = self.apply_mod(result, ELL)
            actual_rows = self.job.square_rows(actual)
            rhs_rows = self.job.square_rows(rhs)
            # Failure here is an implementation/source error, never a rejection
            # of q.  Only after all seven actual solves have verified do we use
            # the full completion residual as HP.2's strict counterexample.
            evaluated_actual = nmod_mat(actual_rows, ELL)*self.Et
            evaluated_rhs = nmod_mat(rhs_rows, ELL)*self.Et
            for pair in self.branch_pairs:
                b = pair["representative"]
                assert all(evaluated_actual[i, b] == evaluated_rhs[i, b] for i in range(2560)), \
                    "An original representative branch solve did not verify; this does not reject q."
            return result, actual_rows

    class Job(base.Job):
        def __init__(self, args):
            assert flint.__version__ == "0.9.0"
            self.args, self.out, self.started = args, args.output, time.monotonic()
            self.out.mkdir(parents=True, exist_ok=True)
            self.item = read(args.config)
            assert self.item["result"] == RESULT and self.item["p"] == 41
            assert self.item["producer_inputs_pending"] is False
            assert self.item["core_sha256"] == sha(__file__)
            assert self.item["full_dual_core_sha256"] == FULL_CORE == sha(args.full_dual_core)
            assert sha(args.proof) == self.item["proof_sha256"] == PROOF
            assert sha(args.nested_proof) == self.item["nested_proof_sha256"] == NESTED_PROOF
            assert sha(args.method) == self.item["method_sha256"]
            assert self.item["full_dual_method_sha256"] == FULL_METHOD
            assert self.item["legacy_core_sha256"] == ORIGINAL_CORE
            assert self.item["field_core_sha256"] == FIELD_CORE
            assert self.item["completed_dual_source"] is not None and self.item["completed_pairing_source"] is not None
            self.legacy = base.module_from_path("original_R787_half_dual_source", args.legacy_core, ORIGINAL_CORE)
            self.field_module = base.module_from_path("original_R781_half_dual_field", args.field_core, FIELD_CORE)
            assert set(self.item["retained_sources"]) == {"R787", "R781", "R786", "CM"}
            self.sources = {key: base.Source(args.retained, key, value)
                            for key, value in self.item["retained_sources"].items()}
            self.previous = FullDualSource(args.retained, self.item["completed_dual_source"],
                                          self.item["retained_sources"], self.item["completed_pairing_source"])
            source = self.sources["R787"]
            assert fingerprint(source.tag) == base.OLD_TAG and source.tag["source_sha256"] == ORIGINAL_CORE
            self.chart, self.blocks, self.selection = (source.get(name) for name in (base.CHART, base.BLOCKS, base.SELECTION))
            assert self.chart["actual_modular_rank"] == RANK and self.chart["chosen_free_column"] == FREE
            assert self.chart["other_free_columns_set_to_zero"] is True
            assert self.selection["prime"] == self.blocks["prime"] == self.chart["prime"] == ELL
            assert self.selection["prime_proved"] and self.selection["all_14_L_branches_distinct"]
            assert self.selection["all_rational_denominators_units"] and self.selection["all_kappa_reductions_invertible"]
            assert self.blocks["exact_E0_Z_zero_verified"] is True and self.blocks["A_inverse_over_Q_computed"] is False
            assert self.blocks["A_minor_det_mod_prime"] % ELL and self.blocks["B_constant_minor_det_mod_prime"] % ELL
            self.rowsJ = [int(x) for x in self.blocks["A_pivot_rows"]]
            remaining = [int(x) for x in self.blocks["A_remaining_rows"]]
            self.rowsI = [remaining[int(x)] for x in self.chart["pivot_rows"]]
            self.pivots = [int(x) for x in self.chart["pivot_columns"]]
            assert len(self.rowsJ) == N and len(self.rowsI) == len(self.pivots) == RANK
            assert sorted(self.rowsJ+remaining) == list(range(2560))
            assert len(set(self.rowsI)) == len(set(self.pivots)) == RANK and FREE not in self.pivots
            assert len(set(self.rowsJ+self.rowsI)) == 2420
            self.outside = [r for r in range(2560) if r not in set(self.rowsJ+self.rowsI)]
            assert len(self.outside) == 140
            for label in ("R781", "R786"):
                old, child = source.tag["retained_artifacts"][label], self.sources[label]
                for key in BASE:
                    assert str(old[key]) == str(child.item[key])
                assert old["files"][old["certificate_name"]] == child.item["certificate"]["sha256"]
            inputs = self.sources["R781"].get("R781-original-real-field-input.json.gz")
            self.field = self.field_module.Field(inputs["field"]["original_b_minimal_polynomial"])
            assert self.field.description == inputs["field"] == source.tag["field"]
            expected_old_tag = {"result": RESULT, "source_sha256": FULL_CORE, "python_flint": "0.9.0",
                "proof_sha256": NESTED_PROOF, "method_sha256": FULL_METHOD,
                "legacy_core_sha256": ORIGINAL_CORE, "field_core_sha256": FIELD_CORE,
                "original_configuration_sha256": base.OLD_TAG,
                "source_identities": {key: value.identity for key, value in self.sources.items()},
                "p": 41, "auxiliary_prime": ELL, "original_map_index": 4, "original_map_degree": "1206",
                "field": self.field.description, "normalization_free_column": FREE, "unknown_shape": [128, 280],
                "rational_unknown_dimension": 35840, "square_L_output_shape": [1234, 1186, 140],
                "basis_integer_scale": base.SCALE, "strategy": base.STRATEGY,
                "completed_pairing_source": self.item["completed_pairing_source"]}
            assert self.previous.tag == expected_old_tag
            self.tag = {"result": RESULT, "source_sha256": sha(__file__), "python_flint": "0.9.0",
                "proof_sha256": PROOF, "nested_proof_sha256": NESTED_PROOF,
                "method_sha256": self.item["method_sha256"], "full_dual_core_sha256": FULL_CORE,
                "full_dual_method_sha256": FULL_METHOD, "legacy_core_sha256": ORIGINAL_CORE,
                "field_core_sha256": FIELD_CORE, "original_configuration_sha256": base.OLD_TAG,
                "source_identities": expected_old_tag["source_identities"],
                "completed_dual_source": self.previous.identity,
                "completed_pairing_source": self.item["completed_pairing_source"],
                "p": 41, "auxiliary_prime": ELL, "original_map_index": 4, "original_map_degree": "1206",
                "field": self.field.description, "normalization_free_column": FREE,
                "unknown_shape": [128, 280], "retained_half_shape": [128, 140],
                "rational_unknown_dimension": 35840, "rational_reconstruction_dimension": 17920,
                "square_L_output_shape": [1234, 1186, 140], "basis_integer_scale": base.SCALE,
                "strategy": STRATEGY}
            self.source_digits = int(self.previous.item["source_dual_digits"])
            self.latest, self.parity_decision = None, None
            self.importing = set()
            self.R, self.K = self.load_original_coefficients()
            self.F = self.load_original_rows()
            self.pairing = self.import_pairing()
            self.target = self.import_target()
            self.operator = HalfOperator(self)
            self.source_audit = self.audit()

        def import_pairing(self):
            previous = self.item["completed_pairing_source"]
            path = self.args.retained/"PAIRING"/previous["pairing"]["file"]
            assert spec(path) == plain(previous["pairing"])
            value = read(path)
            assert value["complete"] is True and fingerprint(value["configuration"]) == previous["configuration_sha256"]
            old = dict(self.previous.tag)
            old.pop("completed_pairing_source")
            old["source_sha256"] = previous["core_sha256"]
            assert value["configuration"] == old
            assert value["integer_unimodular_pairing_and_full_inverse_identity_verified"] is True
            assert value["ordinary_coefficient_transpose_not_trace_or_Hermitian"] is True
            assert value["original_t_modulus"] == [str(x) for x in self.field.gt.coeffs()]
            shape(value["J"], 20, 20)
            shape(value["J_inverse"], 20, 20)
            self.pairing_reference = {"source_group": "PAIRING", **plain(previous["pairing"])}
            return value

        def import_target(self):
            name = PREFIX+"exact-target"
            cached = self.cached(name)
            old = self.previous.target
            assert old["original_scale_applied_once"] == base.SCALE
            shape(old["target_integer_L_rows"], 2560, 14)
            assert int(old["target_common_positive_denominator"]) > 0
            assert len(old["candidate_y"]) == 14
            for row in old["candidate_y"]:
                assert len(row) == 2 and int(row[1]) > 0
            assert all(int(row[0]) == 0 for row in old["candidate_y"][:7]), \
                "This consumer requires the actual candidate to be anti-fixed over Q(b)."
            if cached is None:
                body = {key: value for key, value in old.items() if key not in ("complete", "configuration")}
                body.update(original_completed_target_source=self.previous.reference(self.previous.item["exact_target"]),
                    original_target_and_denominator_recomputed=False,
                    candidate_anti_fixed_in_original_B_s_coordinates_verified=True)
                self.store(name, body)
                cached = self.cached(name)
            assert cached["original_completed_target_source"] == self.previous.reference(self.previous.item["exact_target"])
            for key, value in old.items():
                if key not in ("complete", "configuration"):
                    assert cached[key] == value
            return cached

        def cached(self, name):
            path = self.path(name)
            if path.exists():
                data = read(path)
                assert data["complete"] is True and data["configuration"] == self.tag
                return data
            # Only completed exact-witness stages are eligible for an explicit
            # data-transfer alias.  Their original bytes and configuration stay
            # in FULL_DUAL.  Currents, target construction, and digit stages have
            # their own stricter import paths below.
            filename = name+".json.gz"
            if not name.startswith(PREFIX+"witness-") or filename not in self.previous.files:
                return None
            assert name not in self.importing
            self.importing.add(name)
            old = self.previous.get(filename)

            def transfer(value):
                if isinstance(value, list):
                    return [transfer(row) for row in value]
                if not isinstance(value, dict):
                    return value
                if set(value) == {"file", "bytes", "sha256"}:
                    if plain(value) == plain(self.previous.item["exact_target"]):
                        return spec(self.path(PREFIX+"exact-target"))
                    if re.fullmatch(re.escape(PREFIX)+r"current-\d{8}\.json\.gz", value["file"]):
                        if value["file"] in self.previous.files:
                            return self.previous.reference(value)
                        # Old exact witnesses may refer to an earlier current
                        # whose full array the original producer compacted.
                        # Preserve that hash as history, never point it at the
                        # different same-named imported current in this output.
                        return {"source_group": "FULL_DUAL_HISTORY",
                            "source_manifest_sha256": self.previous.item["manifest_sha256"],
                            "only_a_historical_original_checkpoint_reference": True, **plain(value)}
                    if value["file"].startswith(PREFIX+"witness-") and value["file"] in self.previous.files:
                        assert plain(value) == self.previous.files[value["file"]]
                        dependency = value["file"].removesuffix(".json.gz")
                        assert self.cached(dependency) is not None
                        return spec(self.path(dependency))
                    return dict(value)
                return {key: transfer(row) for key, row in value.items()}

            body = transfer({key: value for key, value in old.items() if key not in ("complete", "configuration")})
            body.update(completed_original_stage_source=self.previous.reference(self.previous.files[filename]),
                original_completed_configuration_sha256=self.previous.item["configuration_sha256"],
                only_explicit_source_reference_transport_performed=True,
                previously_completed_exact_arithmetic_recomputed=False)
            self.store(name, body)
            self.importing.remove(name)
            return read(self.path(name))

        @staticmethod
        def first_forbidden(values):
            shape(values, 128, 280)
            for index, row in enumerate(values):
                forbidden = range(140, 280) if index % 2 == 0 else range(140)
                for coordinate in forbidden:
                    if int(row[coordinate]) != 0:
                        return [index+1, coordinate, str(row[coordinate])]
            return None

        def audit(self):
            name = HALF+"source-audit"
            old = self.previous.audit
            assert old["source_identities"] == self.tag["source_identities"]
            assert old["original_A_rows"] == self.rowsJ
            assert old["original_Schur_rows_in_full_order"] == self.rowsI
            assert old["original_outside_rows"] == self.outside
            assert old["original_pivot_columns"] == self.pivots and old["original_free_column"] == FREE
            assert old["original_complete_branch_stages"] == [row["source"] for row in self.operator.branches]
            if self.cached(name) is None:
                # These are exact source-structure checks, not fresh Laurent or
                # kappa computations.  The full functions were already made.
                for m, value in enumerate(self.R):
                    vector = self.field.vector(value)
                    forbidden = vector[140:] if m % 2 == 0 else vector[:140]
                    assert all(int(x) == 0 for x in forbidden)
                for value in self.K:
                    assert all(int(x) == 0 for x in self.field.vector(value)[140:])
                self.store(name, {"source_identities": self.tag["source_identities"],
                    "completed_dual_source": self.previous.identity,
                    "original_source_audit": self.previous.reference(self.previous.item["source_audit"]),
                    "original_current": self.previous.reference(self.previous.item["current"]),
                    "original_target": self.previous.reference(self.previous.item["exact_target"]),
                    "exact_target": spec(self.path(PREFIX+"exact-target")),
                    "pairing": self.pairing_reference,
                    "original_A_rows": self.rowsJ, "original_Schur_rows_in_full_order": self.rowsI,
                    "original_outside_rows": self.outside, "original_pivot_columns": self.pivots,
                    "original_free_column": FREE,
                    "original_complete_branch_stages": [row["source"] for row in self.operator.branches],
                    "representative_branch_pairs": self.operator.branch_pairs,
                    "all_fourteen_original_unit_minors_and_denominators_preserved": True,
                    "original_R_parity_and_kappa_fixed_exact_coordinates_verified": True,
                    "candidate_q_anti_fixed_verified": True,
                    "source_target_integer_coordinates_preserved": True,
                    "row_support_unchanged_and_coefficient_conjugation_does_not_mix_rows": True,
                    "completed_original_pairing_reused_without_recomputation": True,
                    "old_RHS_Laurent_CM_inverse_and_completed_dual_digits_recomputed": False,
                    "first_new_dual_digit": self.source_digits+1,
                    "old_primal_current_consumed": False})
            return spec(self.path(name))

        def current_value(self, current):
            values = super().current_value(current)
            assert current["digits"] >= self.source_digits
            assert current["original_complete_dual_current_source"] == self.previous.reference(self.previous.item["current"])
            assert current["necessary_half_coordinate_condition_verified"] is True
            assert self.first_forbidden(values) is None
            return values

        def parity_rejection(self, kind, payload):
            assert kind in ("original-complete-current", "completed-seven-branch-correction")
            name = HALF+"strict-rejection-"+kind
            if self.cached(name) is None:
                self.store(name, dict(payload,
                    original_unit_square_operator_and_integral_target_certified=True,
                    conditional_parity_derived_from_original_A1_and_full_row_uniqueness=True,
                    original_candidate_y_strictly_rejected=True,
                    original_value_rowspace_zero_A1_proved=False,
                    ordinary_failed_RR_candidate_used_as_rejection=False,
                    dual_linear_system_exactly_solved=False,
                    rejection_kind=kind, exact_target=spec(self.path(PREFIX+"exact-target")),
                    source_audit=self.source_audit))
            self.parity_decision = spec(self.path(name))
            return self.parity_decision

        def import_current(self):
            old = self.previous.current
            values = [[int(x) for x in row] for row in old["chi_integer_coordinates"]]
            shape(values, 128, 280)
            modulus = int(old["modulus"])
            assert modulus == ELL**self.source_digits
            assert all(0 <= x < modulus for row in values for x in row)
            forbidden = self.first_forbidden(values)
            if forbidden is not None:
                self.parity_rejection("original-complete-current", {
                    "original_current": self.previous.reference(self.previous.item["current"]),
                    "source_dual_digits": self.source_digits, "modulus": old["modulus"],
                    "first_forbidden_nonzero_original_coordinate": forbidden,
                    "old_all35840_modular_equations_verified": True,
                    "old_equations_or_digits_recomputed": False})
                return None
            name = self.current_name(self.source_digits)
            if self.cached(name) is None:
                self.store(name, {"prime": ELL, "digits": self.source_digits, "modulus": old["modulus"],
                    "chi_integer_coordinates": old["chi_integer_coordinates"],
                    "exact_target": spec(self.path(PREFIX+"exact-target")), "source_audit": self.source_audit,
                    "previous_completed_checkpoint_sha256": old.get("previous_completed_checkpoint_sha256"),
                    "original_complete_dual_current_source": self.previous.reference(self.previous.item["current"]),
                    "original_complete_configuration_sha256": self.previous.item["configuration_sha256"],
                    "necessary_half_coordinate_condition_verified": True,
                    "full_square_modular_identity_verified": True,
                    "verification": "explicit immutable full-dual current import; no original modular equation replay",
                    "imported_current_arithmetic_recomputed": False,
                    "old_primal_precision_or_vector_reused_as_dual": False})
            current = self.cached(name)
            self.current_value(current)
            self.repair_history_and_compact(current)
            return current

        def repair_history_and_compact(self, current):
            digits = current["digits"]
            current_spec = spec(self.path(self.current_name(digits)))
            name = PREFIX+"checkpoint-history"
            old = self.cached(name)
            entries = [] if old is None else old["entries"]
            indexed = {row["digits"]: row for row in entries}
            if digits not in indexed:
                if digits == self.source_digits:
                    assert not entries
                else:
                    assert digits-1 in indexed
                    assert current["previous_completed_checkpoint_sha256"] == indexed[digits-1]["checkpoint"]["sha256"]
                entries.append({"digits": digits, "checkpoint": current_spec,
                    "previous_completed_checkpoint_sha256": current.get("previous_completed_checkpoint_sha256"),
                    "full_square_modular_identity_verified": True,
                    "necessary_half_coordinate_condition_verified": True,
                    "step_intermediates": current.get("step_intermediates", [])})
                self.store(name, {"entries": entries, "latest_digits": digits,
                    "latest_checkpoint": current_spec,
                    "source_full_dual_current": self.previous.reference(self.previous.item["current"]),
                    "first_owned_digit_is_original_source_digit": self.source_digits,
                    "history_entries_are_hash_records_not_required_live_arrays": True})
            else:
                assert indexed[digits]["checkpoint"] == current_spec and digits == max(indexed)
            save(self.path(PREFIX+"current-index"), {"complete": False, "configuration": self.tag,
                "latest_complete_checkpoint": current_spec, "digits": digits,
                "history": spec(self.path(name))})
            for path in self.out.glob(PREFIX+"current-*.json.gz"):
                match = re.fullmatch(re.escape(PREFIX)+r"current-(\d{8})\.json\.gz", path.name)
                if match and int(match.group(1)) < digits:
                    assert int(match.group(1)) in indexed
                    path.unlink()
            for row in current.get("step_intermediates", []):
                path = self.out/row["file"]
                if path.exists():
                    assert spec(path) == row
                    path.unlink()
            self.latest = current

        def old_next_stage(self, name):
            filename = name+".json.gz"
            if filename not in self.previous.files:
                return None
            value = self.previous.get(filename)
            assert value["from_current"] == plain(self.previous.item["current"])
            return value

        def step(self, current):
            self.budget()
            digits, modulus = current["digits"], int(current["modulus"])
            next_digits = digits+1
            old_spec = spec(self.path(self.current_name(digits)))
            old_values = self.current_value(current)
            stem = PREFIX+"step-"+str(next_digits).zfill(8)
            residue_name, correction_name = stem+"-positive-residual", stem+"-prime-correction"
            residual = self.cached(residue_name)
            old_residual = self.old_next_stage(residue_name) if digits == self.source_digits else None
            if residual is None:
                if old_residual is not None:
                    assert old_residual["digits_divided"] == digits
                    assert old_residual["division_in_original_L_coordinates_before_branch_evaluation"] is True
                    assert old_residual["all35840_coordinates_divisible_by_previous_modulus"] is True
                    divided = old_residual["positive_residual_divided_mod_prime"]
                    inherited = self.previous.reference(self.previous.files[residue_name+".json.gz"])
                else:
                    actual = self.square_rows(self.operator.apply_mod(old_values, modulus*ELL))
                    divided = []
                    for left, right in zip(actual, self.target["target_integer_L_rows"]):
                        values = [(x-int(y)) % (modulus*ELL) for x, y in zip(left, right)]
                        assert all(x % modulus == 0 for x in values)
                        divided.append([x//modulus for x in values])
                    inherited = None
                shape(divided, 2560, 14)
                self.store(residue_name, {"from_current": old_spec, "digits_divided": digits,
                    "division_in_original_L_coordinates_before_branch_evaluation": True,
                    "positive_residual_divided_mod_prime": divided,
                    "all35840_coordinates_divisible_by_previous_modulus": True,
                    "completed_original_positive_residual_source": inherited,
                    "old_completed_residual_recomputed": False})
                residual = self.cached(residue_name)
            assert residual["from_current"] == old_spec and residual["digits_divided"] == digits
            divided = residual["positive_residual_divided_mod_prime"]
            shape(divided, 2560, 14)
            assert all(0 <= int(x) < ELL for row in divided for x in row)
            correction = self.cached(correction_name)
            if correction is None:
                rhs = [[-int(x) % ELL for x in row] for row in divided]
                candidate_name = stem+"-seven-branch-completion"
                completed_candidate = self.cached(candidate_name)
                if completed_candidate is not None:
                    assert completed_candidate["from_current"] == old_spec
                    assert completed_candidate["positive_residual"] == spec(self.path(residue_name))
                    assert completed_candidate["original_seven_branch_solutions_verified"] is True
                    assert completed_candidate["necessary_half_coordinate_condition_verified"] is True
                    assert completed_candidate["all35840_prime_correction_coordinates_verified"] is False
                    assert completed_candidate["representative_branch_pairs"] == self.operator.branch_pairs
                    self.parity_rejection("completed-seven-branch-correction", {
                        "from_current": old_spec, "dual_digit_tested": next_digits,
                        "positive_residual": spec(self.path(residue_name)),
                        "completed_seven_branch_candidate": spec(self.path(candidate_name)),
                        "original_seven_branch_solutions_verified": True,
                        "full_original_Theta_completion_failed": True,
                        "first_nonzero_original_residual": completed_candidate["first_nonzero_original_residual"]})
                    return None
                old_correction = self.old_next_stage(correction_name) if digits == self.source_digits else None
                if old_correction is not None:
                    assert old_residual is not None
                    assert old_correction["positive_residual"] == self.previous.files[residue_name+".json.gz"]
                    assert old_correction["all35840_prime_correction_coordinates_verified"] is True
                    assert old_correction["RHS_is_negative_divided_positive_residual"] is True
                    delta = old_correction["chi_prime_correction"]
                    shape(delta, 128, 280)
                    assert all(0 <= int(x) < ELL for row in delta for x in row)
                    forbidden = self.first_forbidden(delta)
                    if forbidden is not None:
                        self.parity_rejection("completed-seven-branch-correction", {
                            "from_current": old_spec, "dual_digit_tested": next_digits,
                            "positive_residual": spec(self.path(residue_name)),
                            "completed_original_full_correction": self.previous.reference(self.previous.files[correction_name+".json.gz"]),
                            "source_full_correction_already_verifies_all_original_equations": True,
                            "first_forbidden_nonzero_original_coordinate": forbidden,
                            "original_seven_branch_solutions_verified": True,
                            "completed_original_full_correction_not_recomputed": True})
                        return None
                    inherited = self.previous.reference(self.previous.files[correction_name+".json.gz"])
                    verify_kind = "immutable previously completed full-fourteen-branch correction"
                else:
                    delta, actual_rows = self.operator.seven_branch_correction(self.split_rows(rhs))
                    mismatch = next(([i, j, str((int(actual_rows[i][j])-rhs[i][j]) % ELL)]
                        for i in range(2560) for j in range(14) if int(actual_rows[i][j]) != rhs[i][j]), None)
                    if mismatch is not None:
                        self.store(candidate_name, {"from_current": old_spec,
                            "positive_residual": spec(self.path(residue_name)),
                            "chi_prime_correction": delta,
                            "full_original_output": actual_rows,
                            "representative_branch_pairs": self.operator.branch_pairs,
                            "original_seven_branch_solutions_verified": True,
                            "necessary_half_coordinate_condition_verified": True,
                            "all35840_prime_correction_coordinates_verified": False,
                            "first_nonzero_original_residual": mismatch})
                        self.parity_rejection("completed-seven-branch-correction", {
                            "from_current": old_spec, "dual_digit_tested": next_digits,
                            "positive_residual": spec(self.path(residue_name)),
                            "completed_seven_branch_candidate": spec(self.path(candidate_name)),
                            "original_seven_branch_solutions_verified": True,
                            "full_original_Theta_completion_failed": True,
                            "first_nonzero_original_residual": mismatch})
                        return None
                    inherited = None
                    verify_kind = "seven original branch solutions plus parity; all original 35840 output coordinates verified"
                self.store(correction_name, {"from_current": old_spec,
                    "positive_residual": spec(self.path(residue_name)), "chi_prime_correction": delta,
                    "all35840_prime_correction_coordinates_verified": True,
                    "necessary_half_coordinate_condition_verified": True,
                    "RHS_is_negative_divided_positive_residual": True,
                    "original_seven_branch_solutions_verified": True,
                    "completed_original_full_correction_source": inherited,
                    "verification": verify_kind,
                    "previously_completed_correction_arithmetic_recomputed": False})
                correction = self.cached(correction_name)
            assert correction["from_current"] == old_spec
            assert correction["positive_residual"] == spec(self.path(residue_name))
            assert correction["all35840_prime_correction_coordinates_verified"] is True
            delta = correction["chi_prime_correction"]
            shape(delta, 128, 280)
            assert self.first_forbidden(delta) is None
            values = [[a+modulus*int(b) for a, b in zip(row, change)] for row, change in zip(old_values, delta)]
            assert all(0 <= x < modulus*ELL for row in values for x in row)
            self.store(self.current_name(next_digits), {"prime": ELL, "digits": next_digits,
                "modulus": str(modulus*ELL), "chi_integer_coordinates": [[str(x) for x in row] for row in values],
                "exact_target": spec(self.path(PREFIX+"exact-target")), "source_audit": self.source_audit,
                "previous_completed_checkpoint_sha256": old_spec["sha256"],
                "original_complete_dual_current_source": self.previous.reference(self.previous.item["current"]),
                "necessary_half_coordinate_condition_verified": True,
                "step_intermediates": [spec(self.path(residue_name)), spec(self.path(correction_name))],
                "full_square_modular_identity_verified": True,
                "verification": "complete divided residual and complete correction; exact original linearity",
                "old_primal_precision_or_vector_reused_as_dual": False})
            completed = self.cached(self.current_name(next_digits))
            self.repair_history_and_compact(completed)
            return completed

        def reconstruction(self, current):
            digits, modulus = current["digits"], int(current["modulus"])
            assert digits > self.source_digits
            name = PREFIX+"reconstruction-attempt-"+str(digits).zfill(8)
            cached = self.cached(name)
            if cached is not None:
                return cached.get("witness")
            values = self.current_value(current)
            denominator, coordinates = 1, []
            for index, row in enumerate(values):
                self.budget()
                allowed = range(140) if index % 2 == 0 else range(140, 280)
                result = [fmpq(0)]*280
                for j in allowed:
                    value = self.legacy.rational_reconstruct(row[j], modulus)
                    if value is None:
                        self.store(name, {"source_current": spec(self.path(self.current_name(digits))),
                            "digits": digits, "all17920_retained_coordinates_reconstructed": False,
                            "all35840_coordinates_reconstructed": False,
                            "first_failed_coordinate": [index, j], "candidate_y_rejected": False,
                            "new_dual_precision_not_original_primal_precision": True})
                        return None
                    result[j] = value
                    denominator = math.lcm(denominator, int(value.denom()))
                coordinates.append(result)
            numerators = [[str(int(value.numer())*(denominator//int(value.denom()))) for value in row] for row in coordinates]
            raw = {"coordinate_numerators": numerators, "common_positive_denominator": str(denominator)}
            name_w = PREFIX+"witness-"+fingerprint(raw)
            if self.cached(name_w) is None:
                self.store(name_w, dict(raw, source_current=spec(self.path(self.current_name(digits))),
                    reconstructed_at_dual_digits=digits, exact_target=spec(self.path(PREFIX+"exact-target")),
                    candidate_only_until_full_exact_transpose_verification=True,
                    projective_rescaling_or_content_removal_used=False,
                    only17920_coordinates_reconstructed_other_half_exact_zero=True))
            witness = spec(self.path(name_w))
            self.store(name, {"source_current": spec(self.path(self.current_name(digits))), "digits": digits,
                "all17920_retained_coordinates_reconstructed": True, "all35840_coordinates_reconstructed": True,
                "witness": witness, "candidate_y_rejected": False,
                "new_dual_precision_not_original_primal_precision": True})
            return witness

        def inherited_exact_witness(self):
            # Resume a genuinely completed prior RR candidate without redoing
            # its RR or any completed exact blocks.  Source-bound aliases above
            # preserve those blocks and explicitly mark data transfer only.
            name = PREFIX+"reconstruction-attempt-"+str(self.source_digits).zfill(8)+".json.gz"
            if name not in self.previous.files:
                return None
            attempt = self.previous.get(name)
            assert attempt["digits"] == self.source_digits
            assert attempt["source_current"] == plain(self.previous.item["current"])
            if not attempt["all35840_coordinates_reconstructed"]:
                return None
            row = plain(attempt["witness"])
            assert row == self.previous.files[row["file"]]
            value = self.cached(row["file"].removesuffix(".json.gz"))
            assert self.first_forbidden(value["coordinate_numerators"]) is None
            return spec(self.out/row["file"])

        def finish(self, obstruction=None, reason=None):
            solved, accepted, rejected, kind = False, False, False, None
            if obstruction is not None:
                value = read(self.out/obstruction["file"])
                assert spec(self.out/obstruction["file"]) == obstruction
                assert value["configuration"] == self.tag and value["complete"] is True
                solved = value["dual_linear_system_exactly_solved"]
                accepted = value["original_value_rowspace_zero_A1_proved"]
                rejected = value["original_candidate_y_strictly_rejected"]
                assert solved and accepted != rejected
                kind = "original-full-exact-Theta-and-Delta"
            elif self.parity_decision is not None:
                value = read(self.out/self.parity_decision["file"])
                assert value["original_candidate_y_strictly_rejected"] is True
                assert value["dual_linear_system_exactly_solved"] is False
                rejected, kind = True, value["rejection_kind"]
            completed = bool(accepted or rejected)
            latest = None if self.latest is None else spec(self.path(self.current_name(self.latest["digits"])))
            value = {"result": RESULT, "configuration": self.tag, "complete": completed,
                "p": 41, "original_map_index": 4, "original_map_degree": "1206",
                "source_audit": self.source_audit, "exact_target": spec(self.path(PREFIX+"exact-target")),
                "source_CM_Dixon_digits": 518, "source_CM_Dixon_digits_used_as_dual_precision": False,
                "source_completed_full_dual_digits": self.source_digits,
                "actual_new_dual_digits": self.source_digits if self.latest is None else self.latest["digits"],
                "newly_committed_dual_digits_in_this_source_chain": 0 if self.latest is None else self.latest["digits"]-self.source_digits,
                "latest_dual_current": latest, "source_full_dual_current": self.previous.reference(self.previous.item["current"]),
                "decision_kind": kind, "dual_linear_system_exactly_solved": solved,
                "original_value_rowspace_zero_A1_proved": accepted,
                "original_candidate_y_strictly_rejected": rejected,
                "exact_original_y_value_accepted": accepted,
                "original_expanded_x_and_derivative_accepted": False,
                "rational_reconstruction_dimension": 17920,
                "original_full_rational_identity_dimension": 35840,
                "old_primal_inverse_Laurent_CM_or_function_Dixon_arithmetic_recomputed": False,
                "old_completed_full_dual_digits_or_target_recomputed": False,
                "old_primal_complete_function_recipe_produced": False,
                "actual_eta_or_height_computed": False,
                "exact_value_obstruction": obstruction, "strict_parity_rejection": self.parity_decision,
                "reason": reason,
                "resume_state": spec(self.path(PREFIX+"current-index")) if self.path(PREFIX+"current-index").exists() else None,
                "stage_manifest": self.inventory(), "seconds": time.monotonic()-self.started}
            save(self.out/FINAL, value)
            return value

        def run(self):
            final_path = self.out/FINAL
            if final_path.exists():
                data = read(final_path)
                assert data["configuration"] == self.tag
                if data["complete"] is True:
                    inventory = read(self.out/data["stage_manifest"]["file"])
                    assert spec(self.out/data["stage_manifest"]["file"]) == data["stage_manifest"]
                    for row in inventory["files"]+inventory["current_checkpoints"]:
                        assert spec(self.out/row["file"]) == row
                    return data
            # A committed strict decision remains terminal if a hard stop
            # occurred before FINAL was written.
            for kind in ("original-complete-current", "completed-seven-branch-correction"):
                name = HALF+"strict-rejection-"+kind
                if self.cached(name) is not None:
                    self.parity_decision = spec(self.path(name))
                    current = self.restore_current()
                    return self.finish()
            current = self.restore_current()
            if current is None:
                current = self.import_current()
                if current is None:
                    return self.finish()
            if current["digits"] == self.source_digits:
                witness = self.inherited_exact_witness()
                if witness:
                    obstruction = self.verify_exact(witness)
                    if obstruction:
                        return self.finish(obstruction)
            start_digits = current["digits"]
            every = int(self.item.get("reconstruct_every_digits", 8))
            limit = self.item.get("maximum_new_digits")
            if limit is not None:
                limit = int(limit)
                assert limit >= 0
            assert every >= 1
            while True:
                self.budget()
                if current["digits"] > self.source_digits and current["digits"] % every == 0:
                    witness = self.reconstruction(current)
                    if witness:
                        obstruction = self.verify_exact(witness)
                        if obstruction:
                            return self.finish(obstruction)
                if limit is not None and current["digits"]-start_digits >= limit:
                    return self.finish(reason="requested number of genuinely new dual digits reached; no exact decision")
                current = self.step(current)
                if current is None:
                    return self.finish()

    return Job


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical arithmetic runs only in the public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser()
    for name in ("config", "proof", "nested-proof", "method", "full-dual-core", "legacy-core", "field-core", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, required=True)
    args = parser.parse_args()
    assert args.budget_minutes > 0
    args.output.mkdir(parents=True, exist_ok=True)
    started, job, final, error, code = time.monotonic(), None, None, None, 1
    base = load_module("frozen_original_full_dual", args.full_dual_core, FULL_CORE)
    Job = make_job_class(base)
    try:
        job = Job(args)
        final = job.run()
        code = 0 if final["complete"] else 2
    except base.BudgetStop as exc:
        error, code = str(exc), 124
        if job is not None:
            final = job.finish(reason=error)
    except BaseException as exc:
        error = type(exc).__name__+": "+str(exc)
        traceback.print_exc()
        if isinstance(exc, KeyboardInterrupt):
            code = 130
    receipt = {"result": RESULT, "source_sha256": sha(__file__),
        "configuration": None if job is None else job.tag,
        "complete": bool(final and final["complete"]), "exit_code": code,
        "source_completed_full_dual_digits": None if job is None else job.source_digits,
        "actual_new_dual_digits": None if final is None else final["actual_new_dual_digits"],
        "dual_linear_system_exactly_solved": bool(final and final["dual_linear_system_exactly_solved"]),
        "original_value_rowspace_zero_A1_proved": bool(final and final["original_value_rowspace_zero_A1_proved"]),
        "original_candidate_y_strictly_rejected": bool(final and final["original_candidate_y_strictly_rejected"]),
        "decision_kind": None if final is None else final["decision_kind"],
        "old_primal_CM_target_pairing_or_completed_dual_arithmetic_recomputed": False,
        "seconds": time.monotonic()-started, "error": error,
        "final": spec(args.output/FINAL) if final is not None else None}
    save(args.output/"core-receipt.json", receipt)
    print("HALF_DUAL_RECEIPT="+json.dumps(receipt, sort_keys=True, separators=(",", ":")), flush=True)
    return code


if __name__ == "__main__":
    sys.exit(main())
