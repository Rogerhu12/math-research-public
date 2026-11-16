#!/usr/bin/env python3
"""Append original comparison first jets to the completed 529-node point DAG."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import time

RESULT = "R792-original-Hom-comparison-log-jets"
FINAL = "p41-original-Hom-comparison-log-jets-certificate.json"
PREFIX = "R792-Hom-log-jets-"
DAG_CORE_SHA = "afb49c1ac4245674d29364789e817b566517e1f5bf6d506cee684ed03fa34b8b"
POINT_CORE_SHA = "719c170ac00cf7b15db0d74b5a58998f2901ad838db33dc9d01fd29acd36805a"
POINT_CERT_SHA = "57a2e3ec0b18c6a49e7c4cbfba23a4bda347384788f6b075e6dd8d0b7cf0ee41"
METHOD_SHA = "2d613dc15ac9a0fb93a22415633c58704c914affd987960d74b93637e9e9d555"
STRATEGY = {
    "original_point_program": "R844 original 529 exact nodes imported unchanged",
    "original_differential": "dx/(2y), coordinate z=a-1 at the same original c1",
    "new_scope": "f and five original g_j=(1+T^j)f, their coordinate first jets and five original comparison first jets",
    "tangents": "linear combinations of the original twelve R791 integer-Hom tangents",
    "logarithmic_derivative": "6*y_u*h_u/x_u; no logarithm branch",
    "norm_derivative": "actual seven sigma conjugates; same Q-defined parameter",
    "inverse_proof": "same-point R843 non-torsion via original nonzero integral Hom word",
    "original_comparison_constants_preserved": True,
    "old_CM_Hom_point_or_nontorsion_arithmetic_recomputed": False,
    "nonzero_jet_expanded_coordinates_eta_or_height_certified": False,
}

class BudgetStop(RuntimeError):
    pass

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()

def load_io(path):
    assert sha(path) == DAG_CORE_SHA
    spec = importlib.util.spec_from_file_location("frozen_exact_DAG_and_source_IO", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class Job:
    def __init__(self, args):
        self.args, self.started = args, time.monotonic()
        self.io = load_io(args.dag_core)
        self.config = self.io.read(args.config)
        self.out = Path(args.output)
        self.out.mkdir(parents=True, exist_ok=True)
        c = self.config
        assert c["result"] == RESULT and c["p"] == 41 and c["core_sha256"] == sha(__file__)
        assert c["dag_core_sha256"] == DAG_CORE_SHA and 0 < args.budget_minutes <= 300
        assert c["proofs"]["log_jets"]["sha256"] == METHOD_SHA
        for row in c["proofs"].values():
            path = (Path(args.topic)/row["path"]).resolve()
            assert path.is_relative_to(Path(args.topic).resolve()) and sha(path) == row["sha256"]
        assert set(c["retained_sources"]) == {"CM", "R791", "DAG", "NONTORSION", "POINTS"}
        self.sources = {key: self.io.Source(key, value, args.retained)
                        for key, value in c["retained_sources"].items()}
        self.tag = {"result": RESULT, "source_sha256": c["core_sha256"], "p": 41,
            "dag_core_sha256": DAG_CORE_SHA, "proofs": c["proofs"],
            "source_identities": {key: value.identity for key, value in self.sources.items()},
            "strategy": STRATEGY, "budget_excluded_from_mathematical_identity": True}
        self.prepare()

    def budget(self):
        if time.monotonic()-self.started > self.args.budget_minutes*60:
            raise BudgetStop("Completed original comparison jet stages preserved.")

    def path(self, name):
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
        data = {"complete": True, "configuration": self.tag, **data}
        self.io.save(self.path(name), data)
        return data

    def ref(self, name):
        return self.io.spec(self.path(name))

    def prepare(self):
        source, h, n = (self.sources[key] for key in ("POINTS", "R791", "NONTORSION"))
        cert = source.certificate
        assert source.item["core_sha256"] == POINT_CORE_SHA
        assert source.item["certificate"]["sha256"] == POINT_CERT_SHA
        for key in ("CM", "R791", "DAG", "NONTORSION"):
            assert source.tag["source_identities"][key] == self.sources[key].identity
        for flag in ("actual_nontorsion_source_verified", "five_original_R791_addition_points_as_exact_DAG",
                     "all_addition_denominators_certified_by_original_Hom_words",
                     "original_Galois_transport_and_T7_phase_preserved",
                     "original_R791_comparison_function_values_as_exact_DAG"):
            assert cert[flag] is True
        assert cert["original_map_index"] == 4 and cert["original_map_degree"] == 1206
        assert cert["new_addition_count"] == 5 and cert["point_program_node_count"] == 529
        assert cert["expanded_coordinates_exactly_certified"] is False
        assert cert["actual_eta_or_height_computed"] is False
        self.old = source.stage(cert["point_program"])
        self.old_reference = source.ref(cert["point_program"]["file"])
        assert self.old["node_count"] == 529 and self.old["imported_R841_node_count"] == 50
        assert self.old["imported_R841_nodes_unchanged"] is True
        self.points = {row["id"]: row for row in self.old["point_records"]}
        self.tangents = h.stage(h.files[self.io.TANGENTS])
        self.tangent_ref = h.ref(self.io.TANGENTS)
        self.hom_ref = h.ref(self.io.HOM)
        self.tangent_values = self.tangents["actual_L_coefficients_h_i_over_ds_at_c1"]
        assert len(self.tangent_values) == 12
        assert self.tangents["coordinate"] == "s=a-1 at the original c1"
        assert self.tangents["original_c1_slash_count"] == 1
        assert self.tangents["original_map_index"] == 4 and self.tangents["original_map_degree"] == "1206"
        assert n.certificate["all_nonzero_original_L_Hom_values_nontorsion_consequence"] is True
        self.nontorsion_ref = n.ref(n.item["certificate"]["file"])
        if self.get("source-audit") is None:
            self.put("source-audit", {
                "source_original_point_program": self.old_reference,
                "source_original_twelve_tangents": self.tangent_ref,
                "source_actual_same_point_nontorsion": self.nontorsion_ref,
                "original_parameter": "z=a-1", "original_differential": "dx/(2y)",
                "old_point_node_count": 529, "no_extra_c1_phase": True,
                "all_original_parent_child_identities_preserved": True,
                "old_CM_Hom_point_or_nontorsion_arithmetic_recomputed": False})

    def build(self):
        p = self.io.Program()
        for node in self.old["nodes"]:
            payload = {key: value for key, value in node.items() if key != "id"}
            assert self.io.fingerprint(payload) == node["id"] and node["id"] not in p.known
            assert all(root in p.known for root in node["inputs"])
            p.nodes.append(dict(node))
            p.known[node["id"]] = payload
        imported = len(p.nodes)
        assert imported == 529
        zero, two, three, six = (p.rational(i) for i in (0, 2, 3, 6))
        h_nodes = [
            p.node("source_field_element", source=self.tangent_ref,
                source_key="actual_L_coefficients_h_i_over_ds_at_c1", source_index=i,
                exact_value=value,
                exact_encoding="two polynomials in original b, first 1 then zeta; rational denominators",
                no_extra_c1_phase=True)
            for i, value in enumerate(self.tangent_values)]
        assert h_nodes[4] == self.old["roots"]["h0"]

        def sigma(root, k):
            if k == 0:
                return root
            return p.node("original_L_automorphism", (root,), power=k,
                original_transport_source=self.hom_ref, action="sigma_gamma^power",
                field_generator_image_key="field_sigma_b", fixes_zeta=True,
                applies_to_all_exact_leaves_and_constants=True,
                original_unit_chart_is_conjugated_as_a_whole=True)

        def trace(root):
            result = zero
            for k in range(7):
                result = p.add(result, sigma(root, k))
            return result

        roots, point_jets, trace_jets = dict(self.old["roots"]), [], {}
        labels = ["f"]+["g"+str(j) for j in range(1, 6)]
        for label in labels:
            self.budget()
            point = self.points[self.old["point_labels"][label]]
            word = tuple(int(x) for x in point["original_Hom_coordinates"])
            assert len(word) == 12 and any(word) and point["point_at_infinity"] is False
            assert point["nonzero_word_value_nontorsion"] is True
            x, y = point["coordinates"]["x"], point["coordinates"]["y"]
            terms = [h_nodes[i] if value == 1 else p.mul(p.rational(value), h_nodes[i])
                     for i, value in enumerate(word) if value]
            assert terms
            h = terms[0]
            for term in terms[1:]:
                h = p.add(h, term)
            if label == "f":
                assert h == self.old["roots"]["h0"]
            proof = {
                "rule": "same original nonzero Hom value is not in the kernel of 1-zeta, so x is nonzero",
                "original_Hom_coordinates": point["original_Hom_coordinates"],
                "original_point_id": point["id"], "source_point_program": self.old_reference,
                "source_same_point_nontorsion": self.nontorsion_ref,
                "method": self.config["proofs"]["log_jets"]}
            inverse_x = p.inverse(x, proof)
            dx = p.mul(two, p.mul(y, h))
            dy = p.mul(three, p.mul(p.mul(x, x), h))
            dlog = p.mul(six, p.mul(p.mul(y, h), inverse_x))
            traced = trace(dlog)
            trace_jets[label] = traced
            roots[label+"_h"] = h
            roots[label+"_derivative_z_x"] = dx
            roots[label+"_derivative_z_y"] = dy
            roots[label+"_logarithmic_derivative_y2_minus_b"] = dlog
            roots[label+"_trace_logarithmic_derivative_y2_minus_b"] = traced
            point_jets.append({
                "label": label, "original_point_id": point["id"],
                "original_Hom_coordinates": point["original_Hom_coordinates"],
                "original_coordinates": {"x": x, "y": y}, "h": h,
                "derivative_z_x": dx, "derivative_z_y": dy,
                "logarithmic_derivative_y2_minus_b": dlog,
                "trace_logarithmic_derivative_y2_minus_b": traced,
                "nonzero_x_certified_by_original_Hom_word": True})

        comparisons = []
        for row in self.old["five_original_eta_addition_inputs"]:
            self.budget()
            j = row["j"]
            a, b = (int(v) for v in row["original_rj"])
            assert b > 0
            dlog = p.sub(p.mul(p.rational(b), trace_jets["g"+str(j)]),
                        p.mul(p.rational(2*b+a), trace_jets["f"]))
            value = row["comparison_function_value_root"]
            assert value == self.old["roots"]["R791_comparison_"+str(j)]
            derivative = p.mul(value, dlog)
            roots["R791_comparison_"+str(j)+"_logarithmic_derivative_z"] = dlog
            roots["R791_comparison_"+str(j)+"_derivative_z"] = derivative
            comparisons.append({
                "j": j, "original_rj": row["original_rj"],
                "original_comparison_value_root": value,
                "logarithmic_derivative_z": dlog, "derivative_z": derivative,
                "actual_seven_sigma_trace_used": True,
                "original_value_and_all_norm_constants_unchanged": True,
                "original_c0_rigidification_applied": False})
        assert [row["j"] for row in comparisons] == [1, 2, 3, 4, 5]
        return {
            "format": "original-L-arithmetic-DAG-with-original-automorphisms-v1",
            "nodes": p.nodes, "roots": roots, "node_count": len(p.nodes),
            "imported_R844_node_count": imported, "imported_R844_nodes_unchanged": True,
            "source_original_point_program": self.old_reference,
            "source_original_twelve_tangents": self.tangent_ref,
            "source_actual_same_point_nontorsion": self.nontorsion_ref,
            "point_first_jets": point_jets, "original_comparison_first_jets": comparisons,
            "original_parameter": "z=a-1", "original_differential": "dx/(2y)",
            "original_comparison_logarithmic_first_jets_as_exact_expressions": True,
            "original_comparison_first_jets_as_exact_expressions": True,
            "all_new_inverse_nodes_have_original_nonzero_Hom_proofs": True,
            "original_comparison_constants_preserved": True,
            "old_CM_Hom_point_or_nontorsion_arithmetic_recomputed": False,
            "expanded_coordinates_exactly_certified": False,
            "any_logarithmic_jet_proved_nonzero": False,
            "real_descent_point_first_jets_computed": False,
            "original_rigidification_computed": False,
            "global_polar_divisors_computed": False,
            "actual_eta_or_height_computed": False}

    def run(self):
        if (self.out/FINAL).exists():
            cert = self.io.read(self.out/FINAL)
            assert cert["complete"] is True and cert["configuration"] == self.tag
            return cert
        name = "original-comparison-first-jet-program"
        if self.get(name) is None:
            self.put(name, self.build())
        program = self.get(name)
        rows = [self.io.spec(p) for p in sorted(self.out.glob(PREFIX+"*.json.gz"))
                if not p.name.startswith(PREFIX+"stage-manifest-")]
        manifest_name = "stage-manifest-"+self.io.fingerprint(rows)[:24]
        self.io.save(self.path(manifest_name), {"complete": True, "configuration": self.tag, "files": rows})
        cert = {
            "result": RESULT, "complete": True, "configuration": self.tag,
            "p": 41, "original_map_index": 4, "original_map_degree": 1206,
            "source_audit": self.ref("source-audit"), "jet_program": self.ref(name),
            "stage_manifest": self.ref(manifest_name), "complete_math_stage_count": len(rows),
            "point_program_node_count": program["node_count"],
            "imported_R844_node_count": 529, "new_point_addition_count": 0,
            "actual_nontorsion_source_verified": True,
            "original_comparison_logarithmic_first_jets_as_exact_expressions": True,
            "original_comparison_first_jets_as_exact_expressions": True,
            "all_new_inverse_nodes_have_original_nonzero_Hom_proofs": True,
            "original_comparison_constants_preserved": True,
            "old_CM_Hom_point_or_nontorsion_arithmetic_recomputed": False,
            "expanded_coordinates_exactly_certified": False,
            "any_logarithmic_jet_proved_nonzero": False,
            "original_value_rowspace_zero_A1_proved": False,
            "original_rigidification_computed": False,
            "global_polar_divisors_computed": False,
            "actual_eta_or_height_computed": False, "seconds": time.monotonic()-self.started}
        self.io.save(self.out/FINAL, cert)
        print("ORIGINAL_LOG_JET_RESULT="+json.dumps({key: cert[key] for key in (
            "complete", "point_program_node_count", "imported_R844_node_count", "new_point_addition_count",
            "original_comparison_logarithmic_first_jets_as_exact_expressions",
            "any_logarithmic_jet_proved_nonzero", "actual_eta_or_height_computed", "seconds")}), flush=True)
        return cert

def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematics belongs only to this public repository Actions.")
    parser = argparse.ArgumentParser()
    for key in ("config", "topic", "dag-core", "retained", "output"):
        parser.add_argument("--"+key, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=30)
    args = parser.parse_args()
    started, code, error, cert = time.monotonic(), 0, None, None
    io = load_io(args.dag_core)
    try:
        job = Job(args)
        cert = job.run()
    except BudgetStop as exc:
        code, error = 124, str(exc)
    except Exception as exc:
        code, error = 1, type(exc).__name__+": "+str(exc)
        import traceback
        traceback.print_exc()
    args.output.mkdir(parents=True, exist_ok=True)
    receipt = {"result": RESULT, "source_sha256": sha(__file__),
        "complete": code == 0 and cert is not None, "error": error,
        "certificate_sha256": sha(args.output/FINAL) if cert is not None else None,
        "expanded_coordinates_exactly_certified": False,
        "all_completed_stages_preserved": True, "seconds": time.monotonic()-started}
    io.save(args.output/"core-receipt.json", receipt)
    print("CORE_RECEIPT="+json.dumps(receipt), flush=True)
    raise SystemExit(code)

if __name__ == "__main__":
    main()
