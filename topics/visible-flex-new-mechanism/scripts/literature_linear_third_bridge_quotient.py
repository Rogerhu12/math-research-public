#!/usr/bin/env python3
"""Full C1 diagonal-third one-form modulo the R71 and C3 operator spaces.

The genuine local compiler is called only in the named public Actions repo.
--toy-only uses hand-built expressions, never the research density or a profile.
The exterior slot is still q: this is a diagonal cubic identity, not a claim
about the unsymmetrized trilinear T(f;g,j) needed for all phase channels.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import sys
import time

import literature_local_third_bridge_decompose as local
import literature_pure_bulk_exact_membership as exact
import literature_pure_bulk_word_normal_form as words


SCHEMA = "visible-flex-linear-third-diagonal-quotient-v1"
EXPECTED = {
    "local": "08ada4219df23e50dff2c784c2457dab3c732cd82cacc1477389fdc53fbb6ee0",
    "word": "d39482c9e33e7358f1afa51b073daf5f65e84b4858f9a18f446206e8f9d9ea65",
    "exact": "f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70",
}
REFERENCE_POWERS = (-1, 0, 1)


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      allow_nan=False).encode()


def geometry_label(key):
    factors = []
    for name, power in zip(local.NAMES, key):
        if power:
            factors.append(name if power == 1 else "%s^%s" % (name, power))
    return "*".join(factors) or "1"


def reference_key(power):
    return local.gshift(local.GZERO, local.H, power)


class ExactWordSpan:
    """Reusable rational echelon form, retaining all unmatched target rows.

    A basis row is always an exact linear combination of the input columns.
    A reduction returns target = sum(coeff[j]*column[j]) + remainder.
    A nonzero remainder is not a nonmembership theorem for actual functions.
    """

    def __init__(self, columns, limits):
        if not columns:
            raise ValueError("a span needs its shared word owner")
        self.owner = columns[0].owner
        self.limits = limits
        self.columns = list(columns)
        self.basis = {}
        self.independent = []
        self.null_count = 0
        for index, column in enumerate(columns):
            if column.owner is not self.owner:
                raise ValueError("incompatible profile/right anchor")
            vec, representation = dict(column.terms), {index: F(1)}
            while vec:
                limits.check()
                pivot = min(vec)
                if pivot not in self.basis:
                    scale = vec[pivot]
                    vec = {m: limits.rational(v/scale) for m, v in vec.items()}
                    representation = {j: limits.rational(v/scale)
                                      for j, v in representation.items()}
                    self.basis[pivot] = (vec, representation)
                    self.independent.append(index)
                    break
                other, rep = self.basis[pivot]
                scale = vec[pivot]
                self._subtract(vec, other, scale)
                self._subtract(representation, rep, scale)
            if not vec:
                self.null_count += 1

    def _subtract(self, target, source, factor):
        for key, value in source.items():
            self.limits.check()
            words.add_term(target, key, self.limits.rational(-factor*value))
            if key in target:
                target[key] = self.limits.rational(target[key])

    def reduce(self, target):
        if target.owner is not self.owner:
            raise ValueError("target uses a different right anchor")
        vec, coefficients = dict(target.terms), {}
        for pivot in sorted(self.basis):
            self.limits.check()
            if pivot not in vec:
                continue
            row, representation = self.basis[pivot]
            factor = vec[pivot]
            self._subtract(vec, row, factor)
            for index, value in representation.items():
                words.add_term(coefficients, index, self.limits.rational(factor*value))
                coefficients[index] = self.limits.rational(coefficients[index]) if index in coefficients else F(0)
                if not coefficients[index]:
                    coefficients.pop(index, None)
        return coefficients, words.WordExpr(self.owner, vec)

    def summary(self):
        return {"columns": len(self.columns), "representative_rank": len(self.independent),
                "independent_column_indices": self.independent,
                "dependent_representatives": self.null_count,
                "actual_function_dimension_claimed": False}


def coefficient_rows(coefficients):
    return [[index, str(value)] for index, value in sorted(coefficients.items()) if value]


class ProfileNormalizer:
    def __init__(self, ring, max_calls, max_terms):
        self.ring = ring
        self.legacy = exact.RightIBP(ring)
        self.word = words.WordNormalizer(ring, max_calls=max_calls,
                                         max_terms=max_terms, max_weight=4)

    def expression(self, expr):
        return self.word.expression(self.legacy.expression(expr))


def independent_labels(raw_columns, labels, normalized):
    """Remove identical zero/duplicate representatives, retaining originals."""
    seen, raw, out_labels, normal = set(), [], [], []
    for expression, label in zip(raw_columns, labels):
        value = normalized.expression(expression)
        if not value.terms or value.digest() in seen:
            continue
        seen.add(value.digest())
        raw.append(expression)
        out_labels.append(label)
        normal.append(value)
    return raw, out_labels, normal


def fresh_zero(raw, fresh):
    value = fresh.expression(raw)
    if value.terms:
        raise AssertionError("a positive quotient relation failed the original-expression check")
    return value.digest()


def test_quotient(name, residual, references, raw_columns, labels, normalized,
                  fresh, readable, limits):
    ring, owner = residual.ring, normalized.word
    normal_columns = [normalized.expression(expr) for expr in raw_columns]
    if not normal_columns:
        # A real zero column carries the owner without enlarging the span.
        raw_columns = [ring.number(0)]
        labels = [{"kind": "zero_owner_column"}]
        normal_columns = [owner.zero()]
    modulus = ExactWordSpan(normal_columns, limits)
    ref_raw = [references[p] for p in REFERENCE_POWERS]
    extended_raw = raw_columns+ref_raw
    extended = ExactWordSpan(normal_columns+[normalized.expression(v) for v in ref_raw], limits)
    rows, bad_simple, bad_extended = [], [], []
    scalar_functions = {p: {} for p in REFERENCE_POWERS}
    simple_count = extended_count = 0
    all_keys = set(residual.terms) | {reference_key(p) for p in REFERENCE_POWERS}
    for key in sorted(all_keys):
        limits.check()
        value = residual.terms.get(key, ring.number(0))
        expected = ring.number(0)
        if key in {reference_key(p) for p in REFERENCE_POWERS}:
            expected = references[key[local.H]]
        delta = value-expected
        coefficients, remainder = modulus.reduce(normalized.expression(delta))
        row = {"geometry": list(key), "monomial": geometry_label(key),
               "simple_coefficients": coefficient_rows(coefficients),
               "simple_remainder": owner.summary(remainder)}
        if not remainder.terms:
            original = delta-sum((c*raw_columns[i] for i, c in coefficients.items()), ring.number(0))
            row["simple_original_zero_sha256"] = fresh_zero(original, fresh)
            simple_count += 1
        else:
            bad_simple.append({"geometry": list(key), "monomial": geometry_label(key),
                               "residual": owner.summary(remainder)})
            if len(bad_simple) <= 6:
                readable[name+"_simple_"+str(len(bad_simple))] = remainder
        extended_coeff, extended_remainder = extended.reduce(normalized.expression(value))
        row["extended_coefficients"] = coefficient_rows(extended_coeff)
        row["extended_remainder"] = owner.summary(extended_remainder)
        if not extended_remainder.terms:
            original = value-sum((c*extended_raw[i] for i, c in extended_coeff.items()), ring.number(0))
            row["extended_original_zero_sha256"] = fresh_zero(original, fresh)
            extended_count += 1
        else:
            bad_extended.append({"geometry": list(key), "monomial": geometry_label(key),
                                 "residual": owner.summary(extended_remainder)})
            if len(bad_extended) <= 6:
                readable[name+"_extended_"+str(len(bad_extended))] = extended_remainder
        for j, power in enumerate(REFERENCE_POWERS):
            c = extended_coeff.get(len(raw_columns)+j, F(0))
            if c:
                scalar_functions[power][key] = c
        rows.append(row)
    scalar_report = {
        str(power): [{"geometry": list(key), "monomial": geometry_label(key),
                      "coefficient": str(value)} for key, value in sorted(function.items())]
        for power, function in scalar_functions.items()
    }
    report = {
        "modulus": modulus.summary(), "modulus_labels": labels,
        "with_three_reference_profiles": extended.summary(),
        "geometry_coefficients_checked": len(rows),
        "simple_three_moments_identity_verified": not bad_simple,
        "simple_three_moments": "R(h,k,omega) = h^-1*L_minus + L_zero + h*L_plus modulo the declared space",
        "simple_verified_zero_rows": simple_count, "simple_unresolved": bad_simple,
        "extended_three_profile_span_identity_verified": not bad_extended,
        "extended_verified_zero_rows": extended_count, "extended_unresolved": bad_extended,
        "extended_scalar_functions": scalar_report,
        "extended_functions_are_not_asserted_equal_to_h_inverse_one_h": True,
        "coefficient_representation_not_unique_if_reference_profiles_are_dependent": True,
        "negative_is_not_actual_function_nonmembership": True,
    }
    return report, {"name": name, "modulus_labels": labels,
                    "extended_reference_order": list(REFERENCE_POWERS), "rows": rows}


def write_json(path, payload, pretty=True):
    data = (json.dumps(payload, indent=2 if pretty else None, sort_keys=True,
                       separators=None if pretty else (",", ":"), allow_nan=False)+"\n").encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return {"filename": path.name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def dependency_info():
    report = {}
    for label, module in (("local", local), ("word", words), ("exact", exact)):
        data = Path(module.__file__).read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if digest != EXPECTED[label]:
            raise RuntimeError("frozen %s dependency changed; explicitly bind the new mathematics" % label)
        report[label] = {"filename": Path(module.__file__).name, "bytes": len(data), "sha256": digest}
    report["formal_compiler"] = exact.compiler_dependency()
    return report


def small_toys():
    limits = exact.Limits(seconds=60, nodes=40000, atoms=6000, terms=12000,
                         rewrites=20000, memory_mib=1024)
    ring = exact.Ring(limits)
    n = ProfileNormalizer(ring, 25000, 12000)
    q, x = ring.jet(), ring.x()
    # These are only artificial profile polynomials, not compiled geometry.
    refs = {-1: q**3, 0: q*q.D()**2, 1: q.D()**3}
    missing = q*q.D().D()**2
    helper = x*q**3
    r = local.GExpr(ring, {reference_key(p): value for p, value in refs.items()})
    nuisance_key = local.gshift(local.gshift(local.GZERO, local.K, 2), local.O)
    r += local.GExpr(ring, {nuisance_key: 7*helper})
    readable = {}
    fresh = ProfileNormalizer(ring, 25000, 12000)
    good, _ = test_quotient("toy", r, refs, [helper], [{"kind": "artificial_helper"}],
                            n, fresh, readable, limits)
    if not good["simple_three_moments_identity_verified"]:
        raise AssertionError("artificial three-moment quotient")
    bad_key = local.gshift(local.GZERO, local.O, 2)
    bad, _ = test_quotient("toy_missing", r+local.GExpr(ring, {bad_key: missing}), refs,
                           [helper], [{"kind": "artificial_helper"}], n, fresh, readable, limits)
    if bad["extended_three_profile_span_identity_verified"]:
        raise AssertionError("unhandled artificial coefficient was silently discarded")
    # An unmatched leading row must not prevent a later pivot reduction.
    one = n.word.term((0, (0,)))
    two = n.word.term((0, (1,)))
    three = n.word.term((0, (2,)))
    span = ExactWordSpan([two, two.scale(2), three], limits)
    coefficients, remainder = span.reduce(one+two+three)
    reconstructed = remainder
    for index, value in coefficients.items():
        reconstructed += span.columns[index].scale(value)
    if reconstructed.terms != (one+two+three).terms or remainder.terms != one.terms:
        raise AssertionError("artificial reusable full-pivot elimination")
    # Integration of the scalar h_s one-form must retain the omega contact term.
    potential = local.GExpr(ring, {local.gshift(local.GZERO, local.O): helper}).shift(local.H, 2)
    if (potential.Ds()-potential.partial(local.H).shift(local.V)
            -potential.partial(local.O).shift(local.W).shift(local.H,-1).scale(F(1,2))).terms:
        raise AssertionError("omega_s=k_s/(2h) artificial contact derivative")
    # Physical three-ramp moments use h+*h-=1 and h++h-=4 exactly.
    # A quadratic-number pair (a,b) represents a+b*sqrt(3).
    hp, hm = (F(2),F(1)), (F(2),F(-1))
    product = (hp[0]*hm[0]+3*hp[1]*hm[1], hp[0]*hm[1]+hp[1]*hm[0])
    summed = (hp[0]+hm[0], hp[1]+hm[1])
    if product != (1,0) or summed != (4,0):
        raise AssertionError("exact h-plus/minus moment identities")
    return {"three_moment_positive_relation_from_original_expressions": True,
            "deliberately_missing_geometry_coefficient_retained": True,
            "all_pivots_reduced_after_unmatched_row": True,
            "omega_contact_chain_rule_retained": True,
            "h_plus_minus_exact_moments": {"integral_dk": "-2", "integral_h_dk": "-4",
                                           "integral_inverse_h_dk": "-4", "omega_increment": "-2"},
            "research_compiler_called": False, "profile_or_geometry_evaluated": False}


def run_research(args, payload):
    limits = exact.Limits(args.max_seconds, args.max_coefficient_nodes, args.max_profile_atoms,
                          args.max_terms, args.max_IBP_calls, args.max_memory_mib, args.max_rational_bits)
    ring = exact.Ring(limits)
    n = ProfileNormalizer(ring, args.max_IBP_calls, args.max_terms)
    fresh = ProfileNormalizer(ring, args.max_IBP_calls, args.max_terms)
    payload["phase"] = "compile_actual_local_third_then_decompose"
    raw, records, expanded = local.compile_local_third(ring)
    pieces = local.decompose(raw, n.legacy)
    payload["raw_local"] = raw.summary()
    payload["expanded_coefficient_nodes"] = expanded
    payload["compiler_records"] = records
    payload["decomposition"] = {key: value.summary() for key, value in pieces.items()
                                if isinstance(value, local.GExpr)}
    residual = pieces["residual_k"]
    if any(any(key[i] for i in (local.V,local.W,local.HV,local.KW)) for key in residual.terms):
        raise AssertionError("residual_k must be a static one-form coefficient")
    references = {power: residual.terms.get(reference_key(power), ring.number(0))
                  for power in REFERENCE_POWERS}
    readable = {"L_"+str(power): n.expression(value) for power, value in references.items()}
    payload["reference_profiles"] = {str(power): {
        "geometry_key": list(reference_key(power)), "exists_in_residual": reference_key(power) in residual.terms,
        "raw_sha256": ring.digest(value), "word": n.word.summary(n.expression(value))}
        for power, value in references.items()}
    q = ring.jet()
    operators = exact.operator_basis(ring)
    raw_commutators, commutator_labels = [], []
    for i, j in itertools.combinations(range(8), 2):
        raw_commutators.append(operators[i](q,operators[j](q,q))-operators[j](q,operators[i](q,q)))
        commutator_labels.append({"kind": "R71_diagonal_third_commutator",
                                  "pair": [exact.PARAMETERS[i],exact.PARAMETERS[j]]})
    c3_raw, c3_labels = [], []
    for component in ("area", "cubic"):
        for key, value in sorted(pieces[component].terms.items()):
            c3_raw.append(value)
            c3_labels.append({"kind": "weight_three_profile_coefficient", "component": component,
                              "geometry": list(key), "monomial": geometry_label(key)})
    c3_raw, c3_labels, _ = independent_labels(c3_raw, c3_labels, n)
    payload["c3_coefficient_columns_after_exact_duplicate_removal"] = len(c3_raw)
    payload["phase"] = "full_geometry_coefficient_quotients"
    payload["quotients"] = {}
    certificates = {}
    for name, cols, labels in (
        ("R71_only", raw_commutators, commutator_labels),
        ("C3_and_R71", raw_commutators+c3_raw, commutator_labels+c3_labels),
    ):
        report, rows = test_quotient(name, residual, references, cols, labels,
                                     n, fresh, readable, limits)
        payload["quotients"][name] = report
        certificates[name] = rows
    payload["phase"] = "write_exact_relations_and_readable_expressions"
    certificate_path = args.out.with_name(args.out.stem+"-relations.json")
    certificate = {"schema": SCHEMA+"-relations", "geometry_variable_order": list(local.NAMES),
                   "equation": "raw R coefficient minus stated three-moment coefficient = sum(c_i*raw modulus columns) + remainder",
                   "positive_relations_rechecked_from_original_expressions": True,
                   "right_anchor": "I(f)=integral_r^x f; J=-I; no reset of any left tail",
                   "diagonal_only_not_unsymmetrized_trilinear": True,
                   "cases": certificates}
    data = canonical_bytes(certificate)+b"\n"
    if len(data) > 1000000:
        import gzip
        certificate_path = certificate_path.with_suffix(".json.gz")
        data = gzip.compress(data, mtime=0)
    if len(data) >= 5000000:
        raise exact.formal.CompilationBudgetExceeded("exact quotient certificate exceeds the 5 MB artifact bound")
    certificate_path.parent.mkdir(parents=True, exist_ok=True)
    certificate_path.write_bytes(data)
    payload["exact_relation_artifact"] = {"filename": certificate_path.name, "bytes": len(data),
                                          "sha256": hashlib.sha256(data).hexdigest()}
    exported, _ = words.readable_export(n.word, readable, {}, [])
    exported["schema"] = SCHEMA+"-readable-expressions"
    exported["relation"] = "each labelled expression is a reference profile or a fully reduced unresolved quotient coefficient"
    exported.pop("elimination_coefficients",None)
    payload["readable_expressions"] = write_json(
        args.expressions_out or args.out.with_name(args.out.stem+"-expressions.json"), exported)
    payload["legacy_statistics"] = n.legacy.stats
    payload["word_statistics"] = n.word.stats
    payload["actual_sizes"] = {"coefficient_DAG_nodes": len(ring.algebra.c.nodes),
                               "profile_atoms": len(ring.p.atoms),
                               "history_states": len(ring.algebra.c.state_rhs)}
    payload["completion"], payload["phase"] = "complete", "finished"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--expressions-out", type=Path)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--max-seconds", type=int, default=240)
    parser.add_argument("--max-coefficient-nodes", type=int, default=600000)
    parser.add_argument("--max-profile-atoms", type=int, default=80000)
    parser.add_argument("--max-terms", type=int, default=100000)
    parser.add_argument("--max-IBP-calls", type=int, default=300000)
    parser.add_argument("--max-memory-mib", type=int, default=2048)
    parser.add_argument("--max-rational-bits", type=int, default=8192)
    args = parser.parse_args()
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS") == "true" and
                                 os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"):
        parser.error("actual C1 compilation only in this named public repository's GitHub Actions")
    for key, value in vars(args).items():
        if key.startswith("max_") and value <= 0:
            parser.error("all resource bounds must be positive")
    sys.setrecursionlimit(12000)
    started = time.monotonic()
    payload = {
        "schema": SCHEMA, "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "github": {key: os.environ.get(key) for key in
                   ("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")},
        "completion": "not_started", "phase": "dependencies_and_artificial_checks",
        "scope": "diagonal cubic tau(q)=T(q;q,q), not unsymmetrized full T or all phase channels",
        "geometry_relation": "h>0; omega_s=k_s/(2h); one compact physical xi interval and a common right collar",
        "decomposition_identity": "C_s = Ds(P_acc+P_h) + Area*(k_s*h_ss-h_s*k_ss) + Cubic + k_s*R",
        "potential_endpoint_scope": "constant endpoint germs remove P_acc; h=1 at both endpoints removes anchored P_h; otherwise retain its exact jump",
        "R71_modulus": "original exact cubic diagonal commutators, not their pure-fourth response images",
        "C3_modulus": "all Area and all cubic-velocity coefficient profiles; geometric reachability uses the separate R76/R77 theorem, never a numeric span test",
        "normal_form_complete": False,
        "negative_result_scope": "a nonzero rewritten coefficient does not prove actual functional nonmembership",
        "full_trilinear_identity_certified": False,
        "true_bridge_constructed": False, "all_fourth_phase_channels_paid": False,
        "P0_satisfied": False, "finite_isometric_family_certified": False,
        "profile_or_geometry_values_evaluated": False,
        "resource_limits": {key: value for key,value in vars(args).items() if key.startswith("max_")},
    }
    exit_code = 0
    try:
        payload["dependencies"] = dependency_info()
        payload["artificial_checks"] = small_toys()
        if args.toy_only:
            payload["completion"], payload["phase"] = "toy_only", "finished"
        else:
            run_research(args, payload)
    except exact.formal.CompilationBudgetExceeded as error:
        payload["completion"], payload["budget_failure"] = "resource_budget_exceeded", str(error)
        exit_code = 2
    except Exception as error:
        payload["completion"], payload["error_type"], payload["error"] = "implementation_check_failed", type(error).__name__, str(error)
        exit_code = 1
    payload["elapsed_seconds"] = time.monotonic()-started
    payload["peak_resident_mib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    # Detailed relation matrices live in their own reproducible artifact.
    # Keep the actual status summary inspectable without fetching large data.
    output = json.dumps(payload, indent=2, sort_keys=True, allow_nan=False)+"\n"
    if len(output.encode()) >= 95000:
        for report in payload.get("quotients",{}).values():
            for key in ("simple_unresolved","extended_unresolved"):
                report[key+"_count"] = len(report.get(key,[]))
                report[key] = report.get(key,[])[:12]
            report["modulus_labels_in_relation_artifact"] = True
            report.pop("modulus_labels",None)
        payload["summary_lists_excerpted_full_relations_retained"] = True
        output = json.dumps(payload, indent=2, sort_keys=True, allow_nan=False)+"\n"
    if len(output.encode()) >= 95000:
        raise RuntimeError("C1 quotient summary exceeded its 95 KB bound")
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(output,encoding="utf-8")
    print(json.dumps({"output":str(args.out),"bytes":len(output.encode()),
                      "sha256":hashlib.sha256(output.encode()).hexdigest(),"completion":payload["completion"]}))
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
