#!/usr/bin/env python3
"""R342: one new total-flux observation from four published mixed roots.

No old roots, pure coordinates, response rank, self map, or forcing are compiled.
The output is an exact polynomial on ONE predeclared C7 test family.  A zero
polynomial is inconclusive for the universal functional.  Run only on Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import resource
import sys
import time

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
ENTRY = TOPIC + "/scripts/literature_weight_minus6_total_flux_observer.py"
SCHEMA = "visible-flex-weight-minus6-total-flux-observation-v1"
REQUEST_SCHEMA = SCHEMA + "-request"
OLD_RUN = "43655713308"
OLD_SOURCE = "d21c87a4d9341369a3dee35598ed88fb666cb99d"
OLD_DIR = TOPIC + "/notes/actions-43655713308-1-g_translation_successor"
OLD_INPUTS = {
    "main": {
        "path": OLD_DIR + "/G-seventh-translation.json",
        "bytes": 26745,
        "sha256": "f5e514164cede76ba91786833d455b4638a45a3ee82cd2b7cadbcd76ee18ff15",
    },
    "receipt": {
        "path": OLD_DIR + "/receipt.json",
        "bytes": 35234,
        "sha256": "d1a5b9d8aa03553dfcf45731cbbbbb7861fbcbb496e90fb960e723e1597c3389",
    },
    "original": {
        "path": OLD_DIR + "/G-seventh-translation-original-expressions.json.gz",
        "bytes": 15427,
        "sha256": "936a19bd60b49b236343cdea9466f8a2bbbfbf108b3163ffe6b25e99eb66a664",
        "raw_bytes": 80081,
        "raw_sha256": "cffc0109bccd0a2aeb4e6e23e400c2de94e0bde68c57b41f08df724cd37a9dcb",
    },
}
OLD_SOURCES = {
    TOPIC + "/scripts/literature_G_translation_successor.py": {
        "bytes": 39670,
        "sha256": "a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406",
    },
    TOPIC + "/scripts/literature_local_fourth_quotient.py": {
        "bytes": 38857,
        "sha256": "9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0",
    },
}
ROOT_COMBINATION = {
    "target_-2": Q(1),
    "column_000_-2": Q(315, 32),
    "column_002_-2": Q(315, 16),
    "column_003_-2": Q(-315, 32),
}
LABELS = {0: ("p0", 18), 2: ("r0", 3), 3: ("r0", 4)}
PARAMETERS = {
    "max_seconds": 120,
    "memory_mib": 512,
    "integer_bits": 8192,
    "max_products": 15000000,
    "max_t_degree": 160,
    "max_parameter_degree": 5,
    "max_report_bytes": 95000,
    "max_stdout_bytes": 35000,
}
FAMILY = {
    "coordinate": "t=x-2",
    "support": [2, 3],
    "right_anchor": 4,
    "bump_power": 8,
    "parameter_factor": "1+lambda*(2*t+3*t^2+5*t^3)",
    "witness_nodes": [0, 1, 2, 3, 4, 5],
    "zero_extension_regularity": "C7, not claimed C-infinity",
}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def identity(path):
    raw = path.read_bytes()
    return {"bytes": len(raw), "sha256": sha(raw)}


def integer(value):
    return isinstance(value, int) and not isinstance(value, bool)


class BudgetExceeded(RuntimeError):
    pass


class Budget:
    def __init__(self, parameters):
        self.p = parameters
        self.started = time.monotonic()
        self.products = 0
        self.maximum_bits = 0
        self.maximum_t_degree = 0
        self.maximum_parameter_degree = 0
        self.next_check = 1024

    def check(self, products=0, force=False):
        self.products += products
        if self.products > self.p["max_products"]:
            raise BudgetExceeded("new polynomial product budget")
        if force or self.products >= self.next_check:
            self.next_check = self.products + 1024
            if time.monotonic() - self.started > self.p["max_seconds"]:
                raise BudgetExceeded("new observation wall budget")
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > \
                    self.p["memory_mib"] * 1024:
                raise BudgetExceeded("new observation RSS budget")

    def coefficient(self, value):
        bits = max(abs(value.numerator).bit_length(), value.denominator.bit_length())
        self.maximum_bits = max(self.maximum_bits, bits)
        if bits > self.p["integer_bits"]:
            raise BudgetExceeded("new exact coefficient bit budget")

    def report(self):
        return {
            "rational_products": self.products,
            "maximum_integer_bits": self.maximum_bits,
            "maximum_t_degree": self.maximum_t_degree,
            "maximum_parameter_degree": self.maximum_parameter_degree,
            "elapsed_seconds": time.monotonic() - self.started,
            "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        }


class Poly:
    """Exact Q[t,lambda].  t has physical width one; no floating arithmetic."""
    def __init__(self, budget, terms=None):
        self.budget = budget
        self.terms = {}
        for key, value in (terms or {}).items():
            if len(key) != 2 or any(not integer(x) or x < 0 for x in key):
                raise ValueError("nonnegative bivariate powers required")
            a, b = key
            if a > budget.p["max_t_degree"] or b > budget.p["max_parameter_degree"]:
                raise BudgetExceeded("new polynomial degree budget")
            value = Q(value)
            if value:
                budget.coefficient(value)
                self.terms[(a, b)] = value
                budget.maximum_t_degree = max(budget.maximum_t_degree, a)
                budget.maximum_parameter_degree = max(budget.maximum_parameter_degree, b)
        budget.check(force=True)

    def scalar(self, value):
        return Poly(self.budget, {(0, 0): Q(value)})

    def coerce(self, other):
        if not isinstance(other, Poly):
            return self.scalar(other)
        if other.budget is not self.budget:
            raise ValueError("polynomial budget/coordinate identity mismatch")
        return other

    def __add__(self, other):
        other = self.coerce(other)
        out = dict(self.terms)
        for key, value in other.terms.items():
            out[key] = out.get(key, Q(0)) + value
        return Poly(self.budget, out)

    __radd__ = __add__

    def __neg__(self):
        return Poly(self.budget, {key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        out = {}
        for (a, b), x in self.terms.items():
            for (c, d), y in other.terms.items():
                self.budget.check(1)
                key = (a + c, b + d)
                out[key] = out.get(key, Q(0)) + x * y
        return Poly(self.budget, out)

    __rmul__ = __mul__

    def __pow__(self, power):
        if not integer(power) or power < 0:
            raise ValueError("nonnegative integer polynomial power")
        answer, value = self.scalar(1), self
        while power:
            if power & 1:
                answer = answer * value
            power //= 2
            if power:
                value = value * value
        return answer

    def D(self, order=1):
        answer = self
        for _ in range(order):
            answer = Poly(self.budget, {
                (a - 1, b): a * value for (a, b), value in answer.terms.items() if a
            })
        return answer

    def I_from_one(self):
        """SIGNED primitive integral_1^t, including its exact right constant."""
        out = {}
        for (a, b), value in self.terms.items():
            value /= a + 1
            out[(a + 1, b)] = out.get((a + 1, b), Q(0)) + value
            out[(0, b)] = out.get((0, b), Q(0)) - value
        return Poly(self.budget, out)

    def integral_zero_one(self):
        out = {}
        for (a, b), value in self.terms.items():
            out[b] = out.get(b, Q(0)) + value / (a + 1)
        out = {b: value for b, value in out.items() if value}
        for value in out.values():
            self.budget.coefficient(value)
        self.budget.check(force=True)
        return out

    def endpoint(self, t):
        out = {}
        for (a, b), value in self.terms.items():
            out[b] = out.get(b, Q(0)) + value * Q(t) ** a
        return {b: value for b, value in out.items() if value}


class PublishedReader:
    """Evaluate only reachable atoms of the four selected original roots."""
    def __init__(self, data, u):
        self.data, self.u, self.budget = data, u, u.budget
        self.nodes = data["profile_atoms"]
        self.atom_values, self.monomials = {}, {}
        self.degrees, self.active = {}, set()
        self.jets = {0: u}
        self.x = Poly(self.budget, {(0, 0): Q(2), (1, 0): Q(1)})
        self.xpowers = {0: u.scalar(1), 1: self.x}
        self.profile_positive_integrals = set()
        self.root_names = []

    @staticmethod
    def monomial_key(raw, before):
        if not isinstance(raw, list) or len(raw) != 2:
            raise ValueError("original monomial layout")
        power, indices = raw
        if not integer(power) or power < 0 or not isinstance(indices, list):
            raise ValueError("original polynomial coordinate power")
        if any(not integer(i) or not 0 <= i < before for i in indices):
            raise ValueError("original atom is not a topological DAG")
        return power, tuple(indices)

    def degree_monomial(self, key):
        degree, weight = 0, key[0]
        for identifier in key[1]:
            d, w = self.degree_atom(identifier)
            degree += d
            weight += w
        return degree, weight

    def degree_atom(self, identifier):
        if identifier in self.degrees:
            return self.degrees[identifier]
        if identifier in self.active:
            raise ValueError("cycle in original profile DAG")
        self.active.add(identifier)
        node = self.nodes[identifier]
        if not isinstance(node, list) or not node:
            raise ValueError("original atom layout")
        if node[0] == "jet":
            if len(node) != 3 or node[1] not in ("q", "qbar") or \
                    not integer(node[2]) or not 0 <= node[2] <= 4:
                raise ValueError("original color or maximum jet changed")
            result = (1, -node[2])
        elif node[0] == "int_right" and len(node) == 2:
            key = self.monomial_key(node[1], identifier)
            degree, weight = self.degree_monomial(key)
            if degree <= 0:
                raise ValueError(
                    "unpaid anchor change: a profile-free primitive would retain anchor 4")
            result = degree, weight + 1
            self.profile_positive_integrals.add(identifier)
        else:
            raise ValueError("unsupported original atom")
        self.active.remove(identifier)
        self.degrees[identifier] = result
        return result

    def atom(self, identifier):
        if identifier in self.atom_values:
            return self.atom_values[identifier]
        self.degree_atom(identifier)
        node = self.nodes[identifier]
        if node[0] == "jet":
            order = node[2]
            while order not in self.jets:
                n = max(self.jets)
                self.jets[n + 1] = self.jets[n].D()
            value = self.jets[order]
        else:
            key = self.monomial_key(node[1], identifier)
            value = self.monomial(key).I_from_one()
        self.atom_values[identifier] = value
        return value

    def monomial(self, key):
        if key not in self.monomials:
            power, identifiers = key
            if power not in self.xpowers:
                self.xpowers[power] = self.x ** power
            value = self.xpowers[power]
            for identifier in identifiers:
                value = value * self.atom(identifier)
            self.monomials[key] = value
        return self.monomials[key]

    def root(self, name, required_grade=None):
        if name in self.root_names:
            raise ValueError("an original root must not be reevaluated")
        self.root_names.append(name)
        out, seen = self.u.scalar(0), set()
        for row in self.data["roots"][name]:
            if not isinstance(row, list) or len(row) != 3:
                raise ValueError("original root term layout")
            raw, numerator, denominator = row
            if not integer(numerator) or not integer(denominator) or denominator <= 0:
                raise ValueError("original exact coefficient layout")
            key = self.monomial_key(raw, len(self.nodes))
            if key in seen:
                raise ValueError("duplicate original root monomial")
            seen.add(key)
            if required_grade is not None and self.degree_monomial(key) != required_grade:
                raise ValueError("selected original root is not quartic true weight minus six")
            out += Q(numerator, denominator) * self.monomial(key)
        return out


def parameter_value(coefficients, value):
    return sum((coefficient * Q(value) ** degree
                for degree, coefficient in coefficients.items()), Q(0))


def serial_coefficients(coefficients):
    return [[degree, str(value)] for degree, value in sorted(coefficients.items())]


def new_development():
    """Only new evaluator/phase/selection interfaces; no real input file is read."""
    b = Budget(PARAMETERS)
    t = Poly(b, {(1, 0): Q(1)})
    z = Poly(b, {(0, 1): Q(1)})
    u = t * (1 + z * t)
    checks = {}
    checks["exact_bivariate_product"] = (u * u).terms == {
        (2, 0): Q(1), (3, 1): Q(2), (4, 2): Q(1)}
    checks["physical_unit_width_derivative"] = u.D().terms == {
        (0, 0): Q(1), (1, 1): Q(2)}
    checks["signed_right_constant_per_parameter"] = u.I_from_one().terms == {
        (2, 0): Q(1, 2), (0, 0): Q(-1, 2),
        (3, 1): Q(1, 3), (0, 1): Q(-1, 3)}
    data = {
        "profile_atoms": [
            ["jet", "q", 0], ["jet", "qbar", 0],
            ["int_right", [0, [0]]],
            ["int_right", [1, [2]]],
        ],
        "roots": {
            "both": [[[0, [0, 1]], 1, 1]],
            "nested": [[[0, [3]], 1, 1]],
        },
    }
    r = PublishedReader(data, t)
    checks["both_original_colors_map_to_same_real_profile"] = \
        r.root("both").terms == {(2, 0): Q(1)}
    nested = r.root("nested")
    checks["nested_signed_integral_keeps_every_constant"] = nested.terms == {
        (4, 0): Q(1, 8), (3, 0): Q(1, 3), (2, 0): Q(-1, 4),
        (1, 0): Q(-1), (0, 0): Q(19, 24)}
    checks["all_nested_right_values_zero"] = not nested.endpoint(1)
    bad = {"profile_atoms": [["int_right", [0, []]]],
           "roots": {"bad": [[[0, [0]], 1, 1]]}}
    try:
        PublishedReader(bad, t).root("bad")
        checks["profile_free_integral_cannot_silently_change_anchor"] = False
    except ValueError as error:
        checks["profile_free_integral_cannot_silently_change_anchor"] = \
            "unpaid anchor change" in str(error)
    artificial_mixed = t ** 3
    checks["self_from_mixed_has_minus_four_and_total_integral"] = \
        (-4 * artificial_mixed).integral_zero_one() == {0: Q(-1)}
    root_polys = {
        "target_-2": 2 * t,
        "column_000_-2": 3 * t,
        "column_002_-2": -t,
        "column_003_-2": 5 * t,
    }
    combined = sum((weight * root_polys[name]
                    for name, weight in ROOT_COMBINATION.items()), t.scalar(0))
    checks["four_original_root_combination_exact"] = \
        combined.terms == {(1, 0): Q(-299, 8)}
    checks["zero_family_does_not_prove_universal_zero"] = \
        next((a for a in FAMILY["witness_nodes"] if parameter_value({}, a)), None) is None
    return {"scope": "new evaluator and observation interfaces only",
            "checks": checks, "passed": all(checks.values()),
            "old_development_calls": 0, "scientific_inputs_read": 0,
            "statistics": b.report()}


def safe_repo_path(repo, name):
    if not isinstance(name, str) or Path(name).is_absolute():
        raise ValueError("repository-relative path required")
    path = (repo / name).resolve()
    if repo.resolve() not in path.parents:
        raise ValueError("path escapes the repository")
    return path


def read_checked(repo, specification):
    path = safe_repo_path(repo, specification["path"])
    raw = path.read_bytes()
    if len(raw) != specification["bytes"] or sha(raw) != specification["sha256"]:
        raise ValueError("published input identity mismatch: " + specification["path"])
    return raw


def bind_request(path, report):
    raw = path.read_bytes()
    if len(raw) > 50000:
        raise ValueError("new request must be a small text file")
    request = json.loads(raw)
    if request.get("schema") != REQUEST_SCHEMA or request.get("entry_point") != ENTRY:
        raise ValueError("new observation request schema/entry point")
    if request.get("lane") != "weight_minus6_total_flux_observation":
        raise ValueError("new observation lane")
    if request.get("inputs") != OLD_INPUTS or request.get("parameters") != PARAMETERS:
        raise ValueError("new request altered the frozen inputs or exact budget")
    if request.get("profile_family") != FAMILY:
        raise ValueError("new request altered the predeclared profile family")
    if request.get("goal") != "profile-family-nonzero-witness-not-universal-identity":
        raise ValueError("the finite family must not be reported as a universal identity")
    repo = Path(__file__).resolve().parents[3]
    sources = request.get("source_bindings")
    if not isinstance(sources, dict) or set(sources) != set(OLD_SOURCES) | {ENTRY}:
        raise ValueError("new request source binding set")
    actual = {}
    for name, expected in sources.items():
        got = identity(safe_repo_path(repo, name))
        if got != expected:
            raise ValueError("source text identity mismatch: " + name)
        if name in OLD_SOURCES and expected != OLD_SOURCES[name]:
            raise ValueError("frozen serializer/producer source changed")
        actual[name] = got
    report["request"] = {"path": str(path), "bytes": len(raw), "sha256": sha(raw)}
    report["source_files"] = actual
    return repo, request


def load_four_roots(repo, report):
    main = json.loads(read_checked(repo, OLD_INPUTS["main"]))
    receipt = json.loads(read_checked(repo, OLD_INPUTS["receipt"]))
    packed = read_checked(repo, OLD_INPUTS["original"])
    with gzip.GzipFile(fileobj=io.BytesIO(packed), mode="rb") as stream:
        raw = stream.read(OLD_INPUTS["original"]["raw_bytes"] + 1)
    if len(raw) != OLD_INPUTS["original"]["raw_bytes"] or \
            sha(raw) != OLD_INPUTS["original"]["raw_sha256"]:
        raise ValueError("original input uncompressed identity")
    data = json.loads(raw)
    if main.get("completion") != "complete" or \
            main.get("github_run_id") != OLD_RUN or main.get("github_sha") != OLD_SOURCE:
        raise ValueError("R144 completed main provenance")
    if receipt.get("repository") != REPOSITORY or \
            str(receipt.get("run_id")) != OLD_RUN or \
            receipt.get("source_commit") != OLD_SOURCE or \
            receipt.get("lane") != "g_translation_successor":
        raise ValueError("R144 terminal publication provenance")
    output = [row for row in receipt.get("outputs", [])
              if row.get("path") == Path(OLD_INPUTS["original"]["path"]).name]
    if len(output) != 1:
        raise ValueError("original input absent from terminal publication")
    for key in ("bytes", "sha256", "raw_bytes", "raw_sha256"):
        if output[0].get(key) != OLD_INPUTS["original"][key]:
            raise ValueError("terminal original input binding")
    if data.get("schema") != "visible-flex-G-translation-successor-original-v1-original-expressions" \
            or data.get("github_run_id") != OLD_RUN or data.get("github_sha") != OLD_SOURCE \
            or data.get("github_repository") != REPOSITORY:
        raise ValueError("original export identity")
    if data.get("anchor") != \
            "I(F)=integral_r^xi F; all input colors zero on the same right collar":
        raise ValueError("original signed primitive convention")
    if data.get("translation", {}).get("order") != 7 or \
            data["translation"].get("weight") != -6:
        raise ValueError("only the existing N7G weight-minus-six target is allowed")
    if data.get("original_root_sha256", {}).get("target_-2") != \
            "67e55d68ca5498a698438f389ffb28346aaed3da329cd024a5332183846ed09c":
        raise ValueError("original complete target mixed-root hash label")
    records = {row["index"]: row for row in data["column_records"]}
    selected = {}
    for index, (quadratic, third) in LABELS.items():
        row = records[index]
        label = row["label"]
        if label.get("quadratic_name") != quadratic or label.get("third_index") != third:
            raise ValueError("R144 original response index must not be compacted")
        name = "column_%03d_-2" % index
        if row["roots"]["-2"] != name or \
                row["original_mode_sha256"]["-2"] != data["original_root_sha256"][name]:
            raise ValueError("selected original mixed-root metadata")
        selected[str(index)] = {
            "quadratic_name": quadratic, "third_index": third,
            "root_name": name, "original_sha256": data["original_root_sha256"][name]}
    if set(ROOT_COMBINATION) - set(data["roots"]):
        raise ValueError("one of the four original roots is absent")
    report["input"] = {
        "run": OLD_RUN, "source": OLD_SOURCE, "files": OLD_INPUTS,
        "selected_response_roots": selected,
        "selected_root_names": list(ROOT_COMBINATION),
        "original_target_sha256": data["original_root_sha256"]["target_-2"],
        "original_hash_labels_consumed_under_pinned_raw_sha": True,
        "old_ring_root_digest_or_original_compilation_repeated": False,
        "pure_roots_evaluated": 0, "old_rank_or_self_calls": 0}
    return data


def observation(data, report):
    budget = Budget(PARAMETERS)
    t = Poly(budget, {(1, 0): Q(1)})
    parameter = Poly(budget, {(0, 1): Q(1)})
    u = t ** 8 * (1 - t) ** 8 * \
        (1 + parameter * (2 * t + 3 * t ** 2 + 5 * t ** 3))
    reader = PublishedReader(data, u)
    third = u.D(3)
    components, full = {}, u.scalar(0)
    for name, weight in ROOT_COMBINATION.items():
        value = reader.root(name, required_grade=(4, -6))
        components[name] = (-4 * third * value).integral_zero_one()
        full += weight * value
        print("R342 ORIGINAL MIXED ROOT evaluated " + name, flush=True)
    polynomial = (-4 * third * full).integral_zero_one()
    independent_sum = {}
    for name, weight in ROOT_COMBINATION.items():
        for degree, value in components[name].items():
            independent_sum[degree] = independent_sum.get(degree, Q(0)) + weight * value
    independent_sum = {degree: value for degree, value in independent_sum.items() if value}
    if polynomial != independent_sum:
        raise AssertionError("one combined integral and four weighted integrals disagree")
    if any(degree > 5 for degree in polynomial):
        raise AssertionError("quartic cost times one outer profile must have degree at most five")
    if set(reader.root_names) != set(ROOT_COMBINATION) or len(reader.root_names) != 4:
        raise AssertionError("the study may evaluate exactly four old mixed roots")
    if any(u.D(j).endpoint(a) for j in range(8) for a in (0, 1)):
        raise AssertionError("test family must have both endpoint jets zero through order seven")
    witness = next((a for a in FAMILY["witness_nodes"]
                    if parameter_value(polynomial, a)), None)
    if polynomial and witness is None:
        raise AssertionError("a nonzero degree-five polynomial cannot vanish at six nodes")
    outcome = ("nonzero_total_flux_witness" if witness is not None
               else "declared_family_zero_universal_functional_unresolved")
    result = {
        "outcome": outcome,
        "Omega_A_parameter_coefficients": serial_coefficients(polynomial),
        "new_root_observations": {
            name: serial_coefficients(coefficients) for name, coefficients in components.items()},
        "combined_root_weights": {name: str(weight)
                                  for name, weight in ROOT_COMBINATION.items()},
        "independent_weighted_integral_reassembly_exact": True,
        "predeclared_family": FAMILY,
        "witness": (None if witness is None else {
            "lambda": witness, "Omega_A_exact": str(parameter_value(polynomial, witness)),
            "four_unweighted_Omega_values": {
                name: str(parameter_value(value, witness))
                for name, value in components.items()},
            "extension_regularity": "C7; C-infinity conclusion uses C4 continuity and approximation"}),
        "actual_reachable_atoms": len(reader.atom_values),
        "actual_reachable_monomials": len(reader.monomials),
        "maximum_input_jet": max(reader.jets),
        "positive_profile_degree_integrals": len(reader.profile_positive_integrals),
        "every_evaluated_primitive_has_zero_integrand_on_3_to_4": True,
        "original_signed_primitive_constant_retained": True,
        "unselected_original_roots_evaluated": 0,
        "universal_functional_zero_proved": False,
        "finite_family_restriction_computed_exactly": True,
        "true_smooth_nonzero_witness_implied_by_C4_continuity": witness is not None,
        "study_statistics": budget.report(),
    }
    report["observation"] = result
    report["completion"] = "complete"
    return result


def atomic_json(path, value):
    raw = canonical(value)
    if len(raw) > PARAMETERS["max_report_bytes"]:
        raise BudgetExceeded("temporary report byte limit")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(raw)
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    report = {
        "schema": SCHEMA, "completion": "not_started",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_sha": os.environ.get("GITHUB_SHA"),
        "goal": "one predeclared profile-family nonzero witness; not universal zero",
        "new_original_roots_compiled": 0,
        "new_pure_self_rank_or_membership_calls": 0,
    }
    try:
        if os.environ.get("GITHUB_ACTIONS", "").lower() != "true" or \
                os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
            raise RuntimeError("new checks and this observation run only in the public Actions repository")
        repo, _ = bind_request(args.request, report)
        report["development"] = new_development()
        print("R342 NEW DEVELOPMENT " +
              json.dumps(report["development"], sort_keys=True), flush=True)
        if not report["development"]["passed"]:
            raise AssertionError("new evaluator development did not pass; science not entered")
        data = load_four_roots(repo, report)
        report["completion"] = "running_new_observation"
        result = observation(data, report)
        printed = {
            "outcome": result["outcome"],
            "Omega_A_parameter_coefficients": result["Omega_A_parameter_coefficients"],
            "witness": result["witness"],
            "input_run": OLD_RUN,
            "input_source": OLD_SOURCE,
            "input_raw_sha256": OLD_INPUTS["original"]["raw_sha256"],
            "four_root_weights": result["combined_root_weights"],
            "statistics": result["study_statistics"],
            "scope": "finite declared family; no universal-zero or full-period claim",
        }
        line = "R342 SCIENTIFIC RESULT " + json.dumps(
            printed, sort_keys=True, ensure_ascii=False, allow_nan=False)
        if len(line.encode("utf-8")) > PARAMETERS["max_stdout_bytes"]:
            raise BudgetExceeded("scientific result text exceeds the declared bound")
        print(line, flush=True)
    except Exception as error:
        report["completion"] = "error"
        report["error"] = {"type": type(error).__name__, "message": str(error)}
        print("R342 ERROR " + json.dumps(report["error"], ensure_ascii=False), flush=True)
    finally:
        try:
            atomic_json(args.out, report)
        except Exception as error:
            print("R342 REPORT ERROR " +
                  json.dumps({"type": type(error).__name__, "message": str(error)}), flush=True)
            return 1
    return 0 if report["completion"] == "complete" else 1


if __name__ == "__main__":
    sys.exit(main())
