#!/usr/bin/env python3
"""Five original R791 addition points as exact DAGs after actual non-torsion.

No rational-reconstruction candidate is used. Original R841 nodes and R791
matrices are read unchanged. Only new Hom words and exact symbolic point
operations are generated, in this public repository's Actions.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import time

RESULT = "R792-original-Hom-word-point-DAG"
FINAL = "p41-original-Hom-word-point-DAG-certificate.json"
PREFIX = "R792-Hom-word-DAG-"
DAG_CORE_SHA = "afb49c1ac4245674d29364789e817b566517e1f5bf6d506cee684ed03fa34b8b"
METHOD_SHA = "39880a1f21f33e49aad0117de3e15568b54f6c78ed3e0c6ccc1b1be235c2836e"
NONTORSION_CORE_SHA = "dd3f06a2ed34d31d4d9cc7000eeb5ca763b3fa26b238b418de3e2a47e8dca9c0"
NONTORSION_CERT_SHA = "e4f926d374b5225c45036b363f4cc8a0e4918f54a711e2c3e824f803f3a8e506"
STRATEGY = {
    "input_point": "R841 exact beta_C=f4(c1), never modular or RR coordinates",
    "nontorsion": "actual R843 finite positive formal-parameter valuation for the same point",
    "scope": "five original R791 g_j=(1+T^j)f, j=1..5; not the different R794 basis",
    "point_branches": "actual integral Hom words and the certified non-torsion of all nonzero original Hom values",
    "field_transport": "original sigma acts on all exact DAG leaves; T^j=D_(rho_j^-1)*sigma^j; T^7=[zeta^2]",
    "comparison_values": "original R791(791R.13d), true seven-conjugate norms, no omitted constant",
    "representation": "source-bound exact arithmetic DAG with proof-carrying inverses",
    "expanded_coordinates_eta_or_height": False,
    "old_CM_Dixon_RR_Hom_Galois_or_nontorsion_arithmetic_recomputed": False}


class BudgetStop(RuntimeError):
    pass


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load(path, digest):
    assert sha(path) == digest == DAG_CORE_SHA
    module_spec = importlib.util.spec_from_file_location("frozen_original_point_DAG_definitions", path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


def word_add(a, b):
    assert len(a) == len(b) == 12
    return tuple(x+y for x, y in zip(a, b))


def word_neg(a):
    return tuple(-x for x in a)


def matrix_word(matrix, word):
    assert len(matrix) == len(word) == 12 and all(len(row) == 12 for row in matrix)
    return tuple(sum(int(row[j])*word[j] for j in range(12)) for row in matrix)


class PointProgram:
    def __init__(self, job):
        self.job, self.io = job, job.io
        self.p = self.io.Program()
        original = job.original_program
        for node in original["nodes"]:
            payload = {key: value for key, value in node.items() if key != "id"}
            assert self.io.fingerprint(payload) == node["id"]
            assert all(root in self.p.known for root in node["inputs"])
            assert node["id"] not in self.p.known
            self.p.nodes.append(dict(node))
            self.p.known[node["id"]] = payload
        self.imported_count = len(self.p.nodes)
        self.roots = dict(original["roots"])
        self.b, self.zeta = self.roots["b"], self.roots["zeta"]
        self.one, self.two, self.three, self.nine = (self.p.rational(v) for v in (1, 2, 3, 9))
        self.s = self.p.add(self.one, self.p.mul(self.two, self.zeta))
        self.points, self.labels, self.branches = {}, {}, []
        f = tuple(1 if i == 4 else 0 for i in range(12))
        self.base = self.register("f", f, self.roots["beta_C_x"], self.roots["beta_C_y"],
            {"kind": "completed_original_point", "source": job.program_reference})
        real_word = tuple(int(x) for x in job.descent["selected_real_map_Hom_coordinates"])
        assert real_word == word_add(f, word_neg(matrix_word(job.J, matrix_word(job.J, f))))
        self.real_base = self.register("f_R", real_word, self.roots["f_R_c1_x"], self.roots["f_R_c1_y"],
            {"kind": "completed_original_real_descent_point", "source": job.program_reference})

    def word(self, point):
        return tuple(int(x) for x in point["original_Hom_coordinates"])

    def register(self, label, word, x=None, y=None, construction=None):
        word = tuple(word)
        identity = self.io.fingerprint({"original_integral_Hom_word": [str(x) for x in word]})
        if identity in self.points:
            old = self.points[identity]
            assert self.word(old) == word
            self.labels[label] = identity
            return old
        zero = not any(word)
        assert zero or x in self.p.known and y in self.p.known
        answer = {"id": identity, "original_Hom_coordinates": [str(v) for v in word],
            "point_at_infinity": zero, "coordinates": None if zero else {"x": x, "y": y},
            "construction": construction, "original_primitive_factor": "A_42",
            "nonzero_word_value_nontorsion": not zero}
        self.points[identity] = answer
        self.labels[label] = identity
        return answer

    def nonzero(self, rule, point=None, other=None, **extra):
        if point is not None:
            assert any(self.word(point))
        return {"rule": rule, "source": self.job.nontorsion_reference,
            "actual_all_nonzero_original_Hom_values_nontorsion": True,
            "point_word": None if point is None else point["original_Hom_coordinates"],
            "other_word": None if other is None else other["original_Hom_coordinates"],
            "method": self.job.config["proofs"]["Hom_word_interface"], **extra}

    def sigma(self, root, power):
        assert 0 <= power <= 6 and root in self.p.known
        if power == 0:
            return root
        return self.p.node("original_L_automorphism", (root,), power=power,
            original_transport_source=self.job.hom_reference, action="sigma_gamma^power",
            field_generator_image_key="field_sigma_b", fixes_zeta=True,
            applies_to_all_exact_leaves_and_constants=True,
            original_unit_chart_is_conjugated_as_a_whole=True)

    def rho(self, power):
        assert 0 <= power <= 6
        if power == 0:
            return self.one
        return self.p.node("source_field_element", source=self.job.hom_reference,
            source_key="rho_iterates_zero_through_seven", source_index=power,
            exact_value=self.job.hom["rho_iterates_zero_through_seven"][power],
            exact_encoding="two polynomials in original b, first 1 then zeta; rational denominators")

    def transport(self, point, power, label):
        word = self.word(point)
        for _ in range(power):
            word = matrix_word(self.job.T, word)
        if point["point_at_infinity"]:
            return self.register(label, word, construction={"kind": "transport_zero", "power": power})
        if power == 0:
            self.labels[label] = point["id"]
            return point
        rho = self.rho(power)
        inverse = self.p.inverse(rho, {"rule": "nonzero scalar of the original target isomorphism",
            "source": self.job.hom_reference, "power": power, "proof": self.job.config["proofs"]["R791"]})
        inverse2 = self.p.mul(inverse, inverse)
        x = self.p.mul(inverse2, self.sigma(point["coordinates"]["x"], power))
        y = self.p.mul(self.p.mul(inverse2, inverse), self.sigma(point["coordinates"]["y"], power))
        return self.register(label, word, x, y, {"kind": "original_T_transport", "input": point["id"],
            "power": power, "original_sigma_and_rho": self.job.hom_reference,
            "T_seventh_power": "[zeta^2]", "source_point_is_original_c1": True})

    def add(self, point, other, label):
        u, v = self.word(point), self.word(other)
        result_word = word_add(u, v)
        if not any(u):
            self.labels[label] = other["id"]
            return other
        if not any(v):
            self.labels[label] = point["id"]
            return point
        if u == word_neg(v):
            self.branches.append({"label": label, "type": "opposite_original_Hom_words", "inputs": [point["id"], other["id"]]})
            return self.register(label, result_word, construction={"kind": "opposite", "inputs": [point["id"], other["id"]]})
        x, y = point["coordinates"]["x"], point["coordinates"]["y"]
        xx, yy = other["coordinates"]["x"], other["coordinates"]["y"]
        if u == v:
            denominator = self.p.mul(self.two, y)
            inverse = self.p.inverse(denominator, self.nonzero("nonzero Hom value is not two-torsion", point))
            slope = self.p.mul(self.p.mul(self.three, self.p.mul(x, x)), inverse)
            x_result = self.p.sub(self.p.mul(slope, slope), self.p.mul(self.two, x))
            branch = "equal_original_Hom_words_doubling"
        else:
            denominator = self.p.sub(xx, x)
            inverse = self.p.inverse(denominator,
                self.nonzero("different nonopposite Hom words have different x coordinates", point, other,
                    original_sum_word_nonzero=any(result_word), original_difference_word_nonzero=any(word_add(v, word_neg(u)))))
            slope = self.p.mul(self.p.sub(yy, y), inverse)
            x_result = self.p.sub(self.p.sub(self.p.mul(slope, slope), x), xx)
            branch = "different_nonopposite_original_Hom_words_secant"
        y_result = self.p.sub(self.p.mul(slope, self.p.sub(x, x_result)), y)
        assert any(result_word)
        self.branches.append({"label": label, "type": branch, "inputs": [point["id"], other["id"]],
            "denominator": denominator, "inverse": inverse, "output_word": [str(a) for a in result_word]})
        return self.register(label, result_word, x_result, y_result,
            {"kind": "original_elliptic_addition", "branch": branch, "inputs": [point["id"], other["id"]]})

    def descend(self, point, label):
        word = self.word(point)
        real_word = word_add(word, word_neg(matrix_word(self.job.J, matrix_word(self.job.J, word))))
        if not any(word):
            return self.register(label, real_word, construction={"kind": "three_isogeny_zero"})
        x, y = point["coordinates"]["x"], point["coordinates"]["y"]
        y2 = self.p.mul(y, y)
        w = self.p.sub(y2, self.b)
        inverse = self.p.inverse(w, self.nonzero("nonzero Hom value is not in the kernel of 1-zeta", point))
        thirds = self.p.node("rational", numerator="1", denominator="3")
        s_inverse = self.p.inverse(self.s, {"rule": "s^2=-3 in characteristic zero", "proof": self.job.config["proofs"]["R791"]})
        xr = self.p.neg(self.p.mul(thirds, self.p.mul(self.zeta,
            self.p.mul(x, self.p.mul(self.p.add(y2, self.p.mul(self.three, self.b)), inverse)))))
        yr = self.p.mul(thirds, self.p.mul(y, self.p.mul(self.p.sub(y2, self.p.mul(self.nine, self.b)), self.p.mul(s_inverse, inverse))))
        return self.register(label, real_word, xr, yr, {"kind": "original_three_isogeny", "input": point["id"],
            "alpha3": "1-zeta^2", "alpha3_cube": "3*(1+2*zeta)", "existing_formula": "R791(791R.6)"})

    def norm_factor(self, point):
        y = point["coordinates"]["y"]
        w = self.p.sub(self.p.mul(y, y), self.b)
        answer = self.one
        for k in range(7):
            answer = self.p.mul(answer, self.sigma(w, k))
        return answer

    def power(self, value, exponent):
        assert isinstance(exponent, int) and exponent >= 0
        result = self.one
        while exponent:
            if exponent & 1:
                result = self.p.mul(result, value)
            exponent >>= 1
            if exponent:
                value = self.p.mul(value, value)
        return result

    def components(self, point):
        assert not point["point_at_infinity"]
        return [{"sigma_power": k, "curve_b": self.sigma(self.b, k),
            "x": self.sigma(point["coordinates"]["x"], k),
            "y": self.sigma(point["coordinates"]["y"], k),
            "target_is_original_conjugate_curve": True,
            "same_target_conversion": "D_(rho_k^-1), not an omitted scalar"} for k in range(7)]

    def build(self):
        outputs, norm_base = [], self.norm_factor(self.base)
        for row in self.job.descent["degree_zero_basis"]:
            self.job.budget()
            j = row["j"]
            assert 1 <= j <= 5
            conjugate = self.transport(self.base, j, f"T{j}f")
            g = self.add(self.base, conjugate, f"g{j}")
            real = self.descend(g, f"gR{j}")
            assert self.word(real) == tuple(int(x) for x in row["sum_map_Hom_coordinates"])
            a, b = (int(x) for x in row["degree_zero_coefficient_dj_over_d0"])
            assert b > 0 and 2*b+a > 0
            denominator = self.power(norm_base, 2*b+a)
            inverse = self.p.inverse(denominator,
                self.nonzero("product of true Galois conjugates of nonzero (y_f^2-b)", self.base,
                    true_norm=True, exponent=2*b+a))
            comparison = self.p.mul(self.power(self.norm_factor(g), b), inverse)
            real_degree = int(row["sum_map_degree"])
            assert real_degree % 3 == 0
            outputs.append({"j": j, "g_point_id": g["id"], "real_g_point_id": real["id"],
                "original_rj": [str(a), str(b)], "degree_g": real_degree//3, "degree_real_g": real_degree,
                "comparison_function_value_root": comparison,
                "original_comparison_function": "R791(791R.13d)",
                "true_norm_keeps_Nb_over_b7": True,
                "original_c0_rigidification_applied": False,
                "g_Weil_components": self.components(g), "real_g_Weil_components": self.components(real)})
            self.roots[f"g{j}_x"] = g["coordinates"]["x"]
            self.roots[f"g{j}_y"] = g["coordinates"]["y"]
            self.roots[f"gR{j}_x"] = real["coordinates"]["x"]
            self.roots[f"gR{j}_y"] = real["coordinates"]["y"]
            self.roots[f"R791_comparison_{j}"] = comparison
        assert [row["j"] for row in outputs] == list(range(1, 6))
        assert len(self.branches) == 5
        assert all(row["type"] == "different_nonopposite_original_Hom_words_secant" for row in self.branches)
        base_components, real_base_components = self.components(self.base), self.components(self.real_base)
        return {"format": "original-L-arithmetic-DAG-with-original-automorphisms-v1",
            "nodes": self.p.nodes, "roots": self.roots, "node_count": len(self.p.nodes),
            "imported_R841_node_count": self.imported_count, "imported_R841_nodes_unchanged": True,
            "imported_R841_program": self.job.program_reference,
            "point_records": list(self.points.values()), "point_labels": self.labels,
            "addition_branches": self.branches, "five_original_eta_addition_inputs": outputs,
            "original_base_Weil_components": base_components,
            "original_real_base_Weil_components": real_base_components,
            "exact_original_beta_C_as_expression_certified": True,
            "five_original_R791_addition_points_as_exact_DAG": True,
            "all_addition_denominators_certified_by_original_Hom_words": True,
            "original_Galois_transport_and_T7_phase_preserved": True,
            "original_R791_comparison_function_values_as_exact_DAG": True,
            "expanded_coordinates_exactly_certified": False,
            "original_abstract_A_coordinate_preimage_recovered": False,
            "actual_eta_or_height_computed": False}


class Job:
    def __init__(self, args):
        self.args, self.started = args, time.monotonic()
        self.io = load(args.dag_core, DAG_CORE_SHA)
        self.config, self.out = self.io.read(args.config), Path(args.output)
        self.out.mkdir(parents=True, exist_ok=True)
        c = self.config
        assert c["result"] == RESULT and c["p"] == 41 and c["core_sha256"] == sha(__file__)
        assert c["dag_core_sha256"] == DAG_CORE_SHA and 0 < args.budget_minutes <= 300
        assert c["proofs"]["Hom_word_interface"]["sha256"] == METHOD_SHA
        for row in c["proofs"].values():
            path = (Path(args.topic)/row["path"]).resolve()
            assert path.is_relative_to(Path(args.topic).resolve()) and sha(path) == row["sha256"]
        assert set(c["retained_sources"]) == {"CM", "R791", "DAG", "NONTORSION"}
        self.sources = {label: self.io.Source(label, item, args.retained) for label, item in c["retained_sources"].items()}
        self.tag = {"result": RESULT, "source_sha256": c["core_sha256"], "p": 41,
            "dag_core_sha256": DAG_CORE_SHA, "proofs": c["proofs"],
            "source_identities": {key: value.identity for key, value in self.sources.items()},
            "strategy": STRATEGY, "budget_excluded_from_mathematical_identity": True}
        self.prepare_sources()

    def budget(self):
        if time.monotonic()-self.started > self.args.budget_minutes*60:
            raise BudgetStop("completed exact Hom-word stages retained")

    def path(self, name):
        return self.out/(PREFIX+name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        answer = self.io.read(path)
        assert answer["complete"] is True and answer["configuration"] == self.tag
        return answer

    def store(self, name, data):
        self.budget()
        data = {"complete": True, "configuration": self.tag, **data}
        self.io.save(self.path(name), data)
        return data

    def ref(self, name):
        return self.io.spec(self.path(name))

    def prepare_sources(self):
        d, n, h, cm = (self.sources[key] for key in ("DAG", "NONTORSION", "R791", "CM"))
        df, nf = d.certificate, n.certificate
        assert n.item["core_sha256"] == NONTORSION_CORE_SHA
        assert n.item["certificate"]["sha256"] == NONTORSION_CERT_SHA
        for flag in ("actual_original_beta_C_nontorsion_certified", "original_primitive_Q_beta_nontorsion_consequence",
                     "all_nonzero_original_L_Hom_values_nontorsion_consequence"):
            assert nf[flag] is True
        assert nf["source_original_point_DAG"] == d.identity
        assert nf["original_map_index"] == 4 and nf["original_map_degree"] == 1206
        assert nf["source_Dixon_digits"] == 518
        assert nf["rational_reconstruction_candidates_used"] is False
        for key in ("CM", "R791", "DAG"):
            assert n.tag["source_identities"][key] == self.sources[key].identity
        assert d.tag["source_identities"]["CM"] == cm.identity
        assert d.tag["source_identities"]["R791"] == h.identity
        assert df["exact_original_beta_C_as_expression_certified"] is True
        assert df["exact_original_descent_point_as_expression_certified"] is True
        assert df["expanded_coordinates_exactly_certified"] is False
        self.original_program = d.stage(df["original_point_DAG"])
        self.program_reference = d.ref(df["original_point_DAG"]["file"])
        self.nontorsion_reference = n.ref(n.item["certificate"]["file"])
        witness = n.stage(nf["finite_witness"])
        finite = n.stage(nf["finite_annihilator"])
        assert witness["status"] == "certified" and witness["actual_original_point_nontorsion_certified"] is True
        assert witness["formal_group_torsion_freeness_applied"] is True
        t = witness["formal_parameter_t"]
        assert t["known_nonzero"] is True and 1 <= t["valuation_or_lower_bound"] < t["absolute_precision"]
        assert finite["m_times_original_reduction_is_O"] is True
        assert witness["integer_m"] == finite["integer_m"] > 0
        self.hom = h.stage(h.files[self.io.HOM])
        self.descent = h.stage(h.files[self.io.DESCENT])
        self.hom_reference, self.descent_reference = h.ref(self.io.HOM), h.ref(self.io.DESCENT)
        assert self.hom["gamma_order"] == 21 and self.hom["gamma_seventh_power"] == "zeta^2"
        assert self.hom["all_84_coordinates_verified"] is True
        assert self.hom["all_three_actions_integral_unimodular"] is True
        assert self.hom["remaining_elliptic_factor_included"] is False
        assert len(self.hom["rho_iterates_zero_through_seven"]) == 8
        self.T, self.J = self.hom["gamma_matrix"], self.hom["zeta_matrix"]
        assert self.descent["all_original_F0_directions_covered"] is True
        assert self.descent["original_F0_dimension"] == 5
        assert self.descent["unknown_original_kappa_set_to_one"] is False
        assert self.descent["original_vdagger_v_replaced_by_scalar"] is False
        if not self.cached("source-audit"):
            self.store("source-audit", {"source_identities": self.tag["source_identities"],
                "actual_same_original_point_nontorsion": self.nontorsion_reference,
                "actual_nontorsion_witness": n.ref(nf["finite_witness"]["file"]),
                "actual_integer_m": witness["integer_m"],
                "actual_formal_parameter_valuation": t["valuation_or_lower_bound"],
                "actual_formal_parameter_absolute_precision": t["absolute_precision"],
                "exact_original_point_program": self.program_reference,
                "original_Hom_and_transport": self.hom_reference,
                "original_eta_and_polarization": self.descent_reference,
                "old_CM_Dixon_RR_Hom_Galois_or_nontorsion_arithmetic_recomputed": False})

    def finish(self):
        program = self.cached("five-addition-point-program")
        assert program is not None
        rows = [self.io.spec(path) for path in sorted(self.out.glob(PREFIX+"*.json.gz"))
                if not path.name.startswith(PREFIX+"stage-manifest-")]
        manifest_name = "stage-manifest-"+self.io.fingerprint(rows)[:24]
        self.io.save(self.path(manifest_name), {"complete": True, "configuration": self.tag, "files": rows})
        cert = {"result": RESULT, "complete": True, "configuration": self.tag, "p": 41,
            "original_map_index": 4, "original_map_degree": 1206,
            "source_audit": self.ref("source-audit"), "point_program": self.ref("five-addition-point-program"),
            "original_eta_normalization": self.ref("original-eta-normalization"),
            "actual_nontorsion_source_verified": True,
            "five_original_R791_addition_points_as_exact_DAG": True,
            "all_addition_denominators_certified_by_original_Hom_words": True,
            "original_Galois_transport_and_T7_phase_preserved": True,
            "original_R791_comparison_function_values_as_exact_DAG": True,
            "original_abstract_A_coordinate_preimage_recovered": False,
            "expanded_coordinates_exactly_certified": False,
            "original_value_rowspace_zero_A1_proved": False,
            "actual_eta_or_height_computed": False,
            "old_CM_Dixon_RR_Hom_Galois_or_nontorsion_arithmetic_recomputed": False,
            "original_R794_selected_five_points_computed": False,
            "new_addition_count": 5, "point_program_node_count": program["node_count"],
            "stage_manifest": self.ref(manifest_name), "seconds": time.monotonic()-self.started}
        self.io.save(self.out/FINAL, cert)
        print("HOM_WORD_POINT_DAG_RESULT="+json.dumps({key: cert[key] for key in (
            "complete", "actual_nontorsion_source_verified", "five_original_R791_addition_points_as_exact_DAG",
            "new_addition_count", "point_program_node_count", "expanded_coordinates_exactly_certified",
            "actual_eta_or_height_computed", "seconds")}), flush=True)
        return cert

    def run(self):
        if (self.out/FINAL).exists():
            cert = self.io.read(self.out/FINAL)
            assert cert["complete"] is True and cert["configuration"] == self.tag
            return cert
        if not self.cached("five-addition-point-program"):
            self.store("five-addition-point-program", PointProgram(self).build())
        if not self.cached("original-eta-normalization"):
            self.store("original-eta-normalization", {
                "source": self.descent_reference,
                "kappa_times_vdagger_v_in_original_real_basis": self.descent["kappa_times_vdagger_v_in_real_Chebyshev_basis"],
                "original_hj": "kappa^-1*e*(s_j-r_j), same R791 directions",
                "original_rj": [row["degree_zero_coefficient_dj_over_d0"] for row in self.descent["degree_zero_basis"]],
                "true_norm_semantics": "seven actual sigma conjugates, including all transported constants",
                "same_target_product_scalar_if_used": "(N_L/K(b)/b^7)^(-b_j-a_j)",
                "same_target_product_replaced_true_norm": False,
                "original_c0_rigidification_or_Picard_comparison_computed": False,
                "unknown_original_kappa_set_to_one": False, "original_vdagger_v_replaced_by_scalar": False,
                "global_polar_divisors_computed": False, "actual_eta_or_height_computed": False})
        return self.finish()


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematics belongs only to public repository Actions.")
    parser = argparse.ArgumentParser()
    for key in ("config", "topic", "dag-core", "retained", "output"):
        parser.add_argument("--"+key, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=30)
    args = parser.parse_args()
    started, job, code, error, cert = time.monotonic(), None, 0, None, None
    io = load(args.dag_core, DAG_CORE_SHA)
    try:
        job = Job(args)
        cert = job.run()
    except BudgetStop as exc:
        code, error = 124, str(exc)
    except Exception as exc:
        code, error = 1, f"{type(exc).__name__}: {exc}"
        import traceback
        traceback.print_exc()
    args.output.mkdir(parents=True, exist_ok=True)
    receipt = {"result": RESULT, "source_sha256": sha(__file__), "complete": code == 0 and cert is not None,
        "error": error, "certificate_sha256": sha(args.output/FINAL) if cert is not None else None,
        "expanded_coordinates_exactly_certified": False,
        "all_completed_stages_preserved": True, "seconds": time.monotonic()-started}
    io.save(args.output/"core-receipt.json", receipt)
    print("CORE_RECEIPT="+json.dumps(receipt), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
