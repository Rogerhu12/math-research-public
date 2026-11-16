#!/usr/bin/env python3
"""Finite-precision witnesses for the five completed original logarithmic jets.

The original arithmetic DAG is immutable.  Its four unit-chart response leaves
are read from completed 518-digit outputs; its original branch-zero point balls
are reused.  A zero-containing ball never certifies an exact zero or a usable
inverse.  No CM trace, Dixon lift, Hensel lift, or group-law branch is rerun.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
import traceback

RESULT = "R792-original-comparison-log-jet-padic-witness"
FINAL = "p41-original-comparison-log-jet-padic-witness-certificate.json"
PREFIX = "R792-log-jet-padic-"
P, PRECISION = 1000000753, 518
DAG_CORE_SHA = "afb49c1ac4245674d29364789e817b566517e1f5bf6d506cee684ed03fa34b8b"
BALL_CORE_SHA = "dd3f06a2ed34d31d4d9cc7000eeb5ca763b3fa26b238b418de3e2a47e8dca9c0"
METHOD_SHA = "d55f377e2bb3532bfe6d5b18ecfdc26f74f1c6451507fefea5f3ea0b6a09fbf2"
JET_CORE_SHA = "417f2df7365fcb3ea2e9ce5403404b9c0d0859fc43359b52bb775468452328c2"
JET_CERT_SHA = "b35690551630afced22b426b92f58e5e5747c9d7667c66fb02413d750609054c"
JET_PROGRAM_SHA = "555e3c6c877ef2b3fb64f0dfe17f463f49fd6ca83bb1a1faedc2db562724547b"
STRATEGY = {
    "original_program": "R846 complete 733-node DAG, unchanged, with its original five logarithmic-jet roots",
    "source_precision": 518,
    "local_prime": 1000000753,
    "embedding": "R843 completed branch 0; original simple-root lift and original f4 point balls reused",
    "Galois": "eval(node,k)=iota_0(sigma^k(value(node))); each sigma node shifts the complete context modulo 7",
    "unit_chart": "four completed modular linear responses only; no 2420-vector is solved or reconstructed",
    "arithmetic": "frozen R843 absolute-precision Qell Ball arithmetic with exact rational constants",
    "inverse": "only a ball with known finite valuation; an uncertain denominator makes this dependency inconclusive",
    "witness": "a final ball not containing zero proves the original logarithmic jet nonzero",
    "ordinary_derivative": "nonzero logarithmic jet and R844 original nonzero comparison value imply nonzero first derivative",
    "new_point_additions_or_Hensel_Dixon_CM_traces": False,
    "rational_reconstruction_candidates_consumed": False,
    "height_or_A1_acceptance": False,
    "budget_excluded_from_mathematical_identity": True,
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for part in iter(lambda: f.read(1024*1024), b""):
            h.update(part)
    return h.hexdigest()


def load(path, digest, name):
    assert sha(path) == digest
    definition = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(definition)
    definition.loader.exec_module(module)
    return module


class BudgetStop(RuntimeError):
    pass


class Job:
    def __init__(self, args):
        self.args, self.started = args, time.monotonic()
        self.io = load(args.dag_core, DAG_CORE_SHA, "original_R841_source_IO_for_log_jet_balls")
        self.pad = load(args.ball_core, BALL_CORE_SHA, "original_R843_absolute_precision_balls")
        assert self.pad.P == P and self.pad.N == PRECISION
        self.Ball = self.pad.Ball
        self.item = self.io.read(args.config)
        c = self.item
        assert c["result"] == RESULT and c["p"] == 41 and c["producer_inputs_pending"] is False
        assert c["core_sha256"] == sha(__file__)
        assert c["dag_core_sha256"] == DAG_CORE_SHA and c["ball_core_sha256"] == BALL_CORE_SHA
        assert sha(args.method) == c["method_sha256"] == METHOD_SHA
        assert 0 < args.budget_minutes <= 300
        self.out = Path(args.output)
        self.out.mkdir(parents=True, exist_ok=True)
        assert set(c["retained_sources"]) == {"CM", "R791", "DAG", "NONTORSION", "POINTS", "JETS"}
        self.sources = {label: self.io.Source(label, spec, args.retained)
                        for label, spec in c["retained_sources"].items()}
        self.tag = {"result": RESULT, "source_sha256": sha(__file__), "p": 41,
            "method_sha256": METHOD_SHA, "dag_core_sha256": DAG_CORE_SHA,
            "ball_core_sha256": BALL_CORE_SHA,
            "source_identities": {key: value.identity for key, value in self.sources.items()},
            "strategy": STRATEGY, "budget_excluded_from_mathematical_identity": True}
        self.memo, self.node_lookup, self.source_stage_cache = {}, {}, {}
        self.prepare()

    def budget(self):
        if time.monotonic()-self.started >= self.args.budget_minutes*60:
            raise BudgetStop("All completed node/context enclosures and output decisions are retained.")

    def path(self, name):
        assert Path(name).name == name
        return self.out/(PREFIX+name+".json.gz")

    def get(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        data = self.io.read(path)
        assert data["complete"] is True and data["configuration"] == self.tag
        return data

    def put(self, name, data):
        self.budget()
        self.io.save(self.path(name), dict(data, complete=True, configuration=self.tag))
        return self.get(name)

    def ref(self, name):
        return self.io.spec(self.path(name))

    def source_stage(self, reference):
        label, filename = reference["source_group"], reference["file"]
        key = (label, filename)
        if key not in self.source_stage_cache:
            self.source_stage_cache[key] = self.sources[label].stage(reference)
        return self.source_stage_cache[key]

    def prepare(self):
        jets = self.sources["JETS"]
        assert jets.item["core_sha256"] == JET_CORE_SHA
        assert jets.item["certificate"]["sha256"] == JET_CERT_SHA
        cert = jets.certificate
        for key in ("CM", "R791", "DAG", "NONTORSION", "POINTS"):
            assert jets.tag["source_identities"][key] == self.sources[key].identity
        for key in ("actual_nontorsion_source_verified", "all_new_inverse_nodes_have_original_nonzero_Hom_proofs",
                    "original_comparison_first_jets_as_exact_expressions",
                    "original_comparison_logarithmic_first_jets_as_exact_expressions",
                    "original_comparison_constants_preserved"):
            assert cert[key] is True
        assert cert["point_program_node_count"] == 733 and cert["imported_R844_node_count"] == 529
        assert cert["new_point_addition_count"] == 0 and cert["actual_eta_or_height_computed"] is False
        assert cert["jet_program"]["sha256"] == JET_PROGRAM_SHA
        self.program_ref = jets.ref(cert["jet_program"]["file"])
        self.program = jets.stage(cert["jet_program"])
        assert self.program["node_count"] == len(self.program["nodes"]) == 733
        assert self.program["original_parameter"] == "z=a-1"
        assert self.program["original_differential"] == "dx/(2y)"
        supported = {"original_field_generator", "rational", "multiply", "add", "negate", "inverse",
                     "source_field_element", "unit_chart_solve", "linear_response", "original_L_automorphism"}
        for row in self.program["nodes"]:
            node = row["id"]
            assert node not in self.node_lookup
            assert self.io.fingerprint({key: value for key, value in row.items() if key != "id"}) == node
            assert all(value in self.node_lookup for value in row["inputs"])
            assert row["operation"] in supported
            self.node_lookup[node] = row
        points = self.sources["POINTS"]
        old = points.stage(points.certificate["point_program"])
        assert self.program["nodes"][:529] == old["nodes"]
        assert self.program["imported_R844_nodes_unchanged"] is True
        self.roots = self.program["roots"]
        self.outputs = self.program["original_comparison_first_jets"]
        assert [row["j"] for row in self.outputs] == list(range(1, 6))
        for row in self.outputs:
            assert row["logarithmic_derivative_z"] == self.roots["R791_comparison_"+str(row["j"])+"_logarithmic_derivative_z"]
            assert row["actual_seven_sigma_trace_used"] and row["original_value_and_all_norm_constants_unchanged"]
        h = self.sources["R791"]
        self.hom = h.stage(h.files[self.io.HOM])
        self.hom_ref = h.ref(self.io.HOM)
        self.sigma_b = self.hom["field_sigma_b"]
        assert self.hom["all_84_coordinates_verified"] is True
        cm = self.sources["CM"]
        cf = cm.certificate
        assert cf["source_Dixon_digits"] == PRECISION and cf["new_Dixon_digits_computed"] == 0
        assert cf["all_14_branches_units"] and cf["characteristic_zero_B0_nonzero_certified"]
        expression = cm.stage(cf["implicit_expression"])
        assert expression["original_relation_exactly_defined_by_unit_chart"] is True
        self.field = expression["original_field"]
        self.lam = int(self.field["lambda"])
        assert self.lam % P
        self.response_values, self.response_refs = {}, {}
        for letter in ("A", "B"):
            reference = cf[letter+"_response"]
            data = cm.stage(reference)
            assert data["response"] == letter and data["digits"] == PRECISION
            assert int(data["modulus"]) == P**PRECISION
            assert data["lambda_powers_not_applied"] and data["relation_denominator_or_content_not_reinserted"]
            assert data["integral_L_basis"] == "B^i*s^j, j=0..1 outer, i=0..6; B=lambda*b"
            for derivative, key in ((0, "value"), (1, "derivative_z")):
                values = data[key]
                assert len(values) == 14 and all(0 <= int(value) < P**PRECISION for value in values)
                label = letter+str(derivative)
                self.response_values[label] = values
                self.response_refs[label] = dict(cm.ref(reference["file"]), value_key=key)
        self.unit_chart = [row["id"] for row in self.program["nodes"] if row["operation"] == "unit_chart_solve"]
        assert len(self.unit_chart) == 1
        assert sorted(row["response"] for row in self.program["nodes"] if row["operation"] == "linear_response") == ["A0", "A1", "B0", "B1"]
        for row in self.program["nodes"]:
            if row["operation"] == "linear_response":
                assert row["inputs"] == self.unit_chart
            elif self.unit_chart[0] in row["inputs"]:
                raise AssertionError("The vector-valued unit solve may only be consumed through completed linear responses.")
        nt = self.sources["NONTORSION"]
        assert nt.item["core_sha256"] == BALL_CORE_SHA
        assert nt.certificate["actual_original_beta_C_nontorsion_certified"]
        assert nt.certificate["all_nonzero_original_L_Hom_values_nontorsion_consequence"]
        assert nt.certificate["source_Dixon_digits"] == PRECISION
        assert nt.certificate["local_prime"] == P
        self.point_ref = nt.ref(nt.certificate["original_point_balls"]["file"])
        self.point = nt.stage(nt.certificate["original_point_balls"])
        assert self.point["branch_index"] == 0 and self.point["point_is_the_source_bound_original_f4_c1"]
        assert self.point["rational_reconstruction_candidates_used"] is False
        self.old_roots_ref = nt.ref(self.point["roots"]["file"])
        self.old_roots = nt.stage(self.point["roots"])
        assert self.old_roots["digits"] == PRECISION and self.old_roots["branch_index"] == 0
        assert self.old_roots["unique_lift_of_original_simple_roots"] is True
        self.bindings = {self.roots[node]: key for node, key in (
            ("b", "b"), ("beta_C_x", "x"), ("beta_C_y", "y"),
            ("h0", "h0"), ("derivative_z_y", "yprime"))}
        assert self.roots["f_h"] == self.roots["h0"]
        for node, key in self.bindings.items():
            ball = self.Ball.decode(self.point[key])
            reference = dict(self.point_ref, value_key=key, original_node_id=node, sigma_power=0)
            self.memo[(node, 0)] = {"available": True, "ball": ball, "reference": reference,
                                   "source_completed_ball_reused": True}
        self.embeddings = self.embedding_balls()
        if self.get("source-audit") is None:
            self.put("source-audit", {
                "source_identities": self.tag["source_identities"], "original_program": self.program_ref,
                "original_node_count": 733, "imported_R844_nodes_unchanged": True,
                "original_completed_point_balls": self.point_ref, "original_completed_root_lift": self.old_roots_ref,
                "bindings_at_original_embedding": [{"node_id": node, "source_key": key} for node, key in sorted(self.bindings.items())],
                "completed_linear_response_leaves": self.response_refs,
                "original_Galois_source": self.hom_ref,
                "original_source_precision": PRECISION, "new_Hensel_or_Dixon_digits": 0,
                "new_point_additions": 0, "source_candidate_arrays_consumed": False,
                "new_CM_trace_or_Hom_arithmetic": False})

    def rational_ball(self, numerator, denominator=1, precision=PRECISION):
        numerator, denominator = int(numerator), int(denominator)
        assert denominator != 0
        if numerator == 0:
            return self.Ball(0, precision, precision)
        nv, dv = self.pad.valuation(numerator), self.pad.valuation(denominator)
        value = nv-dv
        if value >= precision:
            return self.Ball(0, precision, precision)
        modulus = P**(precision-value)
        unit = (numerator//P**nv)*pow(denominator//P**dv, -1, modulus) % modulus
        return self.Ball(unit, value, precision)

    def exact_field_ball(self, enc, b, zeta):
        assert len(enc) == 2
        values = []
        for polynomial in enc:
            denominator = int(polynomial["denominator"])
            assert denominator > 0
            value = self.rational_ball(0)
            for coefficient in reversed(polynomial["numerator"]):
                value = value*b+self.rational_ball(coefficient, denominator)
            values.append(value)
        return values[0]+zeta*values[1]

    def embedding_balls(self):
        old = self.get("original-seven-embedding-balls")
        if old is None:
            b0 = self.Ball.decode(self.point["b"])
            assert b0.u and b0.v == 0 and b0.A == PRECISION
            s = self.Ball.integer(int(self.old_roots["s"]), PRECISION)
            zeta = (s-1)*self.rational_ball(1, 2)
            values = [b0]
            for k in range(1, 7):
                self.budget()
                values.append(self.exact_field_ball(self.sigma_b, values[-1], zeta))
            returned = self.exact_field_ball(self.sigma_b, values[-1], zeta)
            residual = returned-b0
            assert residual.u == 0, "The original sevenfold field action has inconsistent finite-precision images."
            reductions = [value.reduction() for value in values]
            assert len(set(reductions)) == 7
            old = self.put("original-seven-embedding-balls", {
                "original_completed_root_lift": self.old_roots_ref,
                "original_completed_point_balls": self.point_ref, "original_sigma_b": self.hom_ref,
                "b_values": [value.encode() for value in values], "s": s.encode(), "zeta": zeta.encode(),
                "seven_distinct_residue_embeddings": reductions,
                "sigma7_consistency_residual": residual.encode(),
                "sigma7_exact_identity_source": "R791 original field action, not this finite-precision check",
                "old_root_lift_recomputed": False})
        assert old["original_completed_root_lift"] == self.old_roots_ref
        assert old["original_completed_point_balls"] == self.point_ref
        assert old["original_sigma_b"] == self.hom_ref
        return {"b": [self.Ball.decode(value) for value in old["b_values"]],
                "s": self.Ball.decode(old["s"]), "zeta": self.Ball.decode(old["zeta"]),
                "reference": self.ref("original-seven-embedding-balls")}

    def response_ball(self, label, k):
        values = self.response_values[label]
        B = self.embeddings["b"][k]*self.lam
        result = []
        for shift in (0, 7):
            value = self.Ball.integer(0, PRECISION)
            for coefficient in reversed(values[shift:shift+7]):
                value = value*B+self.Ball.integer(int(coefficient), PRECISION)
            result.append(value)
        return result[0]+self.embeddings["s"]*result[1]

    def evaluate(self, node, context):
        row = self.node_lookup[node]
        context %= 7
        if row["operation"] == "rational":
            context = 0
        key = (node, context)
        if key in self.memo:
            return self.memo[key]
        name = "node-"+node+"-sigma-"+str(context)
        stage = self.get(name)
        if stage is not None:
            assert stage["original_node_id"] == node and stage["sigma_power"] == context
            answer = {"available": stage["evaluation_available"], "reference": self.ref(name)}
            if answer["available"]:
                answer["ball"] = self.Ball.decode(stage["ball"])
            else:
                answer["reason"] = stage["inconclusive_reason"]
            self.memo[key] = answer
            return answer
        self.budget()
        operation = row["operation"]
        dependencies, reason, ball = [], None, None
        if operation == "unit_chart_solve":
            raise AssertionError("No new unit-chart vector solve belongs to this consumer.")
        if operation == "original_L_automorphism":
            assert row["action"] == "sigma_gamma^power" and row["fixes_zeta"] is True
            assert row["applies_to_all_exact_leaves_and_constants"] is True
            assert row["original_unit_chart_is_conjugated_as_a_whole"] is True
            assert row["field_generator_image_key"] == "field_sigma_b"
            assert row["original_transport_source"] == self.hom_ref
            answer = self.evaluate(row["inputs"][0], context+int(row["power"]))
            dependencies = [answer["reference"]]
            if answer["available"]:
                ball = answer["ball"]
            else:
                reason = {"rule": "an entire conjugated input is numerically inconclusive", "source": answer["reference"]}
        elif operation == "linear_response":
            assert row["inputs"] == self.unit_chart
            label = row["response"]
            ball = self.response_ball(label, context)
            dependencies = [self.response_refs[label], self.embeddings["reference"]]
        elif operation == "rational":
            ball = self.rational_ball(row["numerator"], row["denominator"])
        elif operation == "original_field_generator":
            assert row["exact_field_source"] == self.sources["CM"].ref(self.sources["CM"].certificate["implicit_expression"]["file"])
            if row["name"] == "b":
                ball = self.embeddings["b"][context]
            else:
                assert row["name"] == "zeta"
                ball = self.embeddings["zeta"]
            dependencies = [self.embeddings["reference"]]
        elif operation == "source_field_element":
            data = self.source_stage(row["source"])
            value = data[row["source_key"]]
            if "source_index" in row:
                value = value[row["source_index"]]
            assert value == row["exact_value"]
            assert row["exact_encoding"] == "two polynomials in original b, first 1 then zeta; rational denominators"
            ball = self.exact_field_ball(value, self.embeddings["b"][context], self.embeddings["zeta"])
            dependencies = [row["source"], self.embeddings["reference"]]
        else:
            values = [self.evaluate(value, context) for value in row["inputs"]]
            dependencies = [value["reference"] for value in values]
            unavailable = [value for value in values if not value["available"]]
            if unavailable:
                reason = {"rule": "an input enclosure is unavailable", "sources": [value["reference"] for value in unavailable]}
            elif operation == "inverse" and not values[0]["ball"].u:
                assert row.get("nonzero_certificate")
                reason = {"rule": "the original exact nonzero denominator has only a zero-containing ball at this precision",
                    "denominator_ball": values[0]["ball"].encode(), "original_exact_nonzero_certificate": row["nonzero_certificate"]}
            elif operation == "inverse":
                assert len(values) == 1 and row.get("nonzero_certificate")
                ball = values[0]["ball"].inverse()
            elif operation == "negate":
                assert len(values) == 1
                ball = -values[0]["ball"]
            elif operation == "add":
                assert len(values) == 2
                ball = values[0]["ball"]+values[1]["ball"]
            elif operation == "multiply":
                assert len(values) == 2
                ball = values[0]["ball"]*values[1]["ball"]
            else:
                raise AssertionError("Unknown original scalar operation: "+operation)
        assert (ball is None) == (reason is not None)
        stage = self.put(name, {"original_program": self.program_ref, "original_node_id": node,
            "sigma_power": context, "operation": operation, "dependencies": dependencies,
            "evaluation_available": ball is not None, "ball": None if ball is None else ball.encode(),
            "inconclusive_reason": reason, "exact_zero_claimed": False,
            "original_DAG_node_modified": False})
        answer = {"available": ball is not None, "reference": self.ref(name)}
        if ball is not None:
            answer["ball"] = ball
        else:
            answer["reason"] = reason
        self.memo[key] = answer
        return answer

    def decide(self, row):
        name = "comparison-"+str(row["j"])
        old = self.get(name)
        if old is not None:
            assert old["source_logarithmic_jet_root"] == row["logarithmic_derivative_z"]
            return old
        answer = self.evaluate(row["logarithmic_derivative_z"], 0)
        known = bool(answer["available"] and answer["ball"].u)
        return self.put(name, {"j": row["j"], "source_original_program": self.program_ref,
            "source_logarithmic_jet_root": row["logarithmic_derivative_z"],
            "source_original_comparison_value_root": row["original_comparison_value_root"],
            "source_original_derivative_root": row["derivative_z"],
            "evaluated_root": answer["reference"], "evaluation_available": answer["available"],
            "ball": answer["ball"].encode() if answer["available"] else None,
            "inconclusive_reason": None if answer["available"] else answer["reason"],
            "original_logarithmic_jet_proved_nonzero": known,
            "original_comparison_derivative_proved_nonzero": known,
            "comparison_derivative_argument": "R844 comparison value is nonzero; R846 Rj'=Rj*Dj",
            "exact_jet_zero_claimed": False, "height_jet_nonzero_claimed": False})

    def finish(self, decisions, exhausted=False, reason=None):
        files = [self.io.spec(path) for path in sorted(self.out.glob(PREFIX+"*.json.gz"))
                 if not path.name.startswith(PREFIX+"stage-manifest-")]
        name = "stage-manifest-"+self.io.fingerprint(files)[:24]
        if self.get(name) is None:
            self.io.save(self.path(name), {"complete": True, "configuration": self.tag, "files": files})
        count = sum(bool(row["original_logarithmic_jet_proved_nonzero"]) for row in decisions)
        complete = len(decisions) == 5 and not exhausted
        final = {"result": RESULT, "configuration": self.tag, "complete": complete, "p": 41,
            "original_program": self.program_ref, "original_node_count": 733,
            "source_Dixon_digits": PRECISION, "local_prime": P, "original_branch": 0,
            "source_audit": self.ref("source-audit"), "seven_embedding_balls": self.embeddings["reference"],
            "comparison_decisions": [self.ref("comparison-"+str(row["j"])) for row in decisions],
            "processed_comparison_count": len(decisions), "strict_nonzero_witness_count": count,
            "all_five_logarithmic_jets_proved_nonzero": count == 5,
            "all_five_comparison_derivatives_proved_nonzero": count == 5,
            "zero_containing_ball_means_exact_zero": False,
            "new_point_addition_count": 0, "new_Hensel_or_Dixon_digits": 0,
            "old_CM_Hom_point_or_nontorsion_arithmetic_recomputed": False,
            "old_original_DAG_nodes_modified": False, "candidate_arrays_used": False,
            "original_value_rowspace_zero_A1_proved": False, "expanded_original_coordinates_exactly_certified": False,
            "original_rigidification_computed": False, "actual_eta_or_height_computed": False,
            "all_p_nonzero_conclusion_claimed": False, "reason": reason,
            "stage_manifest": self.ref(name), "seconds": time.monotonic()-self.started}
        self.io.save(self.out/FINAL, final)
        return final

    def run(self):
        path = self.out/FINAL
        if path.exists():
            final = self.io.read(path)
            assert final["configuration"] == self.tag
            if final["complete"]:
                assert self.io.spec(self.out/final["stage_manifest"]["file"]) == final["stage_manifest"]
                inventory = self.io.read(self.out/final["stage_manifest"]["file"])
                assert inventory["complete"] is True and inventory["configuration"] == self.tag
                for row in inventory["files"]:
                    assert self.io.spec(self.out/row["file"]) == row
                return final
        decisions = []
        for row in self.outputs:
            decisions.append(self.decide(row))
        return self.finish(decisions)


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New arithmetic is confined to public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser()
    for name in ("config", "method", "dag-core", "ball-core", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    started, job, final, error, code = time.monotonic(), None, None, None, 1
    try:
        job = Job(args)
        final = job.run()
        code = 0 if final["complete"] else 2
    except BudgetStop as exc:
        error, code = str(exc), 124
        if job is not None:
            decisions = [job.get("comparison-"+str(j)) for j in range(1, 6)]
            final = job.finish([row for row in decisions if row is not None], exhausted=True, reason=error)
    except BaseException as exc:
        error = type(exc).__name__+": "+str(exc)
        traceback.print_exc()
    receipt = {"result": RESULT, "source_sha256": sha(__file__),
        "configuration": None if job is None else job.tag,
        "complete": bool(final and final["complete"]), "exit_code": code, "error": error,
        "certificate_sha256": sha(args.output/FINAL) if final else None,
        "strict_nonzero_witness_count": None if final is None else final["strict_nonzero_witness_count"],
        "new_Hensel_or_Dixon_digits": 0, "new_point_addition_count": 0,
        "actual_eta_or_height_computed": False, "seconds": time.monotonic()-started}
    if job is not None:
        job.io.save(args.output/"core-receipt.json", receipt)
    else:
        temporary = args.output/"core-receipt.json.tmp"
        temporary.write_text(json.dumps(receipt, sort_keys=True)+"\n")
        temporary.replace(args.output/"core-receipt.json")
    print("PADIC_LOG_JET_RECEIPT="+json.dumps(receipt, sort_keys=True, separators=(",", ":")), flush=True)
    return code


if __name__ == "__main__":
    sys.exit(main())
