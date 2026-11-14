#!/usr/bin/env python3
"""Export the missing exact factors for geometric derivative weights two/four.

N^[0], N^[2] are the unreduced actual local third potential.
v^[2], v^[4] retain both complete fourth phase modes. Real s derivatives and
history ODE substitutions precede zeroing accumulated history values.
No W generators/basis, static fourth target, or old fourth response is rebuilt.
Actual research runs only in this public repository's GitHub Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import json
import os
from pathlib import Path
import resource
import time

import literature_local_fourth_quotient as old
import literature_full_m8_tail_response_projection as io_helper

colored, exact, local, formal = old.colored, old.exact, old.local, old.formal
SCHEMA = "visible-flex-local-fourth-derivative-original-factors-v1"
REPOSITORY = "Rogerhu12/math-research-public"
STATIC_PRODUCER_SHA = "9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0"
IO_HELPER_SHA = "e66bf0d2f41570526d5e6b05aedc28118a18a492a299e097d341cc71e804e345"
MAX_RAW_BYTES = 40000000
TOTAL_OUTPUT_BYTES = 4800000
MAIN_RESERVE = 150000
MODES = (-4, -2)
GEOMETRY_NAMES = tuple(local.NAMES)+("h_sss", "k_sss")
GZERO = (0,)*len(GEOMETRY_NAMES)
canonical, sha, identity = io_helper.canonical, io_helper.sha, io_helper.identity


def dependencies():
    source = old.dependencies()
    if source["driver"]["sha256"] != STATIC_PRODUCER_SHA:
        raise ValueError("keep the complete original static producer frozen")
    helper = identity(io_helper.__file__)
    if helper["sha256"] != IO_HELPER_SHA:
        raise ValueError("rebind the frozen original-expression IO interfaces explicitly")
    result = dict(source)
    result["static_expression_producer"] = result.pop("driver")
    result["original_expression_io"] = helper
    result["driver"] = identity(__file__)
    return result



def extend_key(key):
    if len(key) == 8:
        return tuple(key)+(0, 0)
    if len(key) != len(GEOMETRY_NAMES):
        raise ValueError("complete derivative factors require eight or ten geometry coordinates")
    return tuple(key)


def geometry_weight(key):
    key = extend_key(key)
    return key[3]+key[4]+2*key[5]+2*key[6]+3*key[8]+3*key[9]


class ThirdJetGeometryExpansion:
    """Keep real third s-jets before any exact coefficient cancellation."""
    def __init__(self, algebra, limits):
        self.a, self.limits, self.cache = algebra, limits, {}

    def power(self, terms, exponent):
        if exponent < 0:
            if len(terms) != 1:
                raise ValueError("only an actual Laurent monomial can have a negative power")
            key, value = next(iter(terms.items()))
            return {tuple(exponent*x for x in key): value**exponent}
        result, base = {GZERO:F(1)}, terms
        while exponent:
            if exponent & 1:
                result = local.smul(result, base, self.limits)
            exponent >>= 1
            if exponent:
                base = local.smul(base, base, self.limits)
        return result

    def node(self, index):
        if index in self.cache:
            return self.cache[index]
        self.limits.check()
        node = self.a.c.nodes[index]
        tag = node[0]
        if tag == "c":
            answer = {GZERO:F(node[1],node[2])} if node[1] else {}
        elif tag == "st":
            answer = {}
        elif tag == "g":
            lookup = {("h",0):0, ("k",0):1, ("omega",0):2,
                      ("h",1):3, ("k",1):4, ("h",2):5, ("k",2):6,
                      ("h",3):8, ("k",3):9}
            if (node[1],node[2]) not in lookup:
                raise AssertionError(("unsupported true geometry jet retained in raw DAG",node))
            key=list(GZERO); key[lookup[(node[1],node[2])]]=1
            answer={tuple(key):F(1)}
        elif tag == "add":
            answer={}
            for child,n,d in node[1]:
                answer=local.sadd(answer,{key:F(n,d)*value for key,value in self.node(child).items()})
        elif tag == "mul":
            answer={GZERO:F(node[1],node[2])}
            for child,exponent in node[3]:
                answer=local.smul(answer,self.power(self.node(child),exponent),self.limits)
        else:
            raise AssertionError(("unknown coefficient node",node))
        self.cache[index]=answer
        return answer

    def separated(self, expression, ring):
        answer={}
        for profile,coefficient in expression.terms.items():
            for geometry,value in self.node(coefficient).items():
                answer[geometry]=answer.get(geometry,ring.number(0))+value*ring.monomial(profile)
        return local.GExpr(ring,answer)


def reachable_geometry_jets(expression):
    algebra=expression.algebra
    seen, jets=set(), set()
    def visit(index):
        if index in seen:
            return
        seen.add(index)
        node=algebra.c.nodes[index]
        if node[0]=="g":
            jets.add((node[1],node[2]))
        elif node[0]=="add":
            for child,n,d in node[1]:
                visit(child)
        elif node[0]=="mul":
            for child,exponent in node[3]:
                visit(child)
        elif node[0] not in ("c","st"):
            raise ValueError("unknown raw coefficient kind during real jet scan")
    for index in expression.terms.values():
        visit(index)
    return {"reachable_coefficient_nodes":len(seen),
            "real_geometry_jets":[[name,order] for name,order in sorted(jets)],
            "maximum_s_derivative_order":max((order for name,order in jets),default=0)}

def split_geometry(value, allowed, profile_degree):
    answer = {weight: {} for weight in allowed}
    for key, expression in value.terms.items():
        weight = geometry_weight(key)
        if weight not in answer:
            raise AssertionError("an undeclared actual geometric derivative weight appeared")
        if any(value.ring.p.weight(m) != profile_degree for m in expression.terms):
            raise AssertionError("actual profile degree changed")
        answer[weight][key] = expression
    return {weight: local.GExpr(value.ring, rows) for weight, rows in answer.items()}


def raw_potential(ring, report):
    # The previous public export contains W and L^[0], not these original N roots.
    # These missing factors require the local third calculation; no control_templates,
    # pre_reduce_templates or W membership calculation is called here.
    normalizer = colored.ColoredNormalizer(ring)
    density, records, nodes = old.producer.compile_colored_local(ring)
    pieces = old.producer.raw_decomposition(density, normalizer)
    raw = (pieces["potential_acc"]+pieces["potential_h"]
           +old.endpoint.endpoint_potential(pieces["residual_k"],
                h_base=1, k_base=1, omega_base=1))
    parts = split_geometry(raw, (0, 2), 3)
    for part in parts.values():
        for expression in part.terms.values():
            if any(degree != (("a", 1), ("b", 1), ("c", 1))
                   for degree in ring.color_degrees(expression)):
                raise AssertionError("original potential lost its exterior and inner slots")
    # P_acc is the whole weight-two factor; do not assume it belongs to W.
    delta = parts[2]-pieces["potential_acc"]
    if delta.terms:
        raise AssertionError("N^[2] must retain the complete original P_acc")
    report["new_potential"] = {
        "formula": "P_acc + P_h + exact R79 endpoint_potential, base h=k=omega=1",
        "source_records_sha256": sha(canonical(records)),
        "expanded_local_geometry_nodes": nodes,
        "local_third_geometry_coefficients": len(density.terms),
        "potential_geometry_coefficients": {str(w): len(x.terms) for w, x in parts.items()},
        "exact_local_third_reconstruction_verified": pieces["reconstruction_zero"],
        "potential_two_equals_original_P_acc": True,
        "potential_reduced_mod_W": False, "potential_two_assumed_in_W": False,
        "W_generators_recompiled": False, "W_basis_recomputed": False,
        "prior_36_W_hash_checks_repeated": False,
        "new_missing_unreduced_potential_factors_only": True}
    return parts


def new_local_generators(ring, report):
    """Same complete phase formula as the frozen producer, with static=False."""
    comp = local.SharedCompiler(ring.algebra)
    A = comp.initial("q")
    B, _ = comp.forcing_range([(1, A, A)], 2, "derivative_B_qq", True)
    U, _ = comp.forcing_range([(1, A, B)], 3, "derivative_U_qB", True)
    V, _ = comp.forcing_range([(1, A, B.conjugate())], 3, "derivative_V_qBb", True)
    state_count = len(ring.algebra.c.state_rhs)
    fields = {"A": A, "Ab": A.conjugate(), "B": B, "Bb": B.conjugate(),
              "U": U, "Ub": U.conjugate(), "V": V, "Vb": V.conjugate()}
    # Resolve the real covariant derivatives before specializing any history value.
    for field in fields.values():
        field.cov()
    zero = old.ZeroStateCoefficients(ring.algebra, static=False)
    values = {name: zero.field(field) for name, field in fields.items()}
    pairs = {"P": ("B", "B"), "Q": ("B", "Bb"), "R": ("A", "U"),
             "S": ("A", "V"), "T": ("A", "Vb"), "J": ("Ab", "U")}
    output = {name: old.local_forcing(comp, [(1, values[a], values[b])], zero)["period_rhs"]
              for name, (a, b) in pairs.items()}
    combinations = {
        -4: [("P", F(-1, 16)), ("R", F(-1, 4))],
        -2: [("P", F(1, 8)), ("Q", F(1, 8)), ("R", F(1, 4)),
             ("S", F(1, 4)), ("T", F(-1, 4)), ("J", F(-1, 4))]}
    expansion = ThirdJetGeometryExpansion(ring.algebra, ring.limits)
    answer, coverage = {}, {}
    for mode, terms in combinations.items():
        raw = comp.zero.add(*(output[name].scale(value) for name, value in terms))
        scan = reachable_geometry_jets(raw)
        report.setdefault("actual_raw_geometry_jet_scans", {})[str(mode)] = scan
        expanded = expansion.separated(raw, ring)
        parts = split_geometry(expanded, (0, 2, 4), 4)
        # v^[0] appears inside the literal finite formula but is not a new target:
        # it is discarded, not composed with N and not reevaluated against old results.
        answer[mode] = {weight: parts[weight] for weight in (2, 4)}
        if mode == -4:
            for part in answer[mode].values():
                for expression in part.terms.values():
                    if any(degree != (("q", 4),) for degree in ring.color_degrees(expression)):
                        raise AssertionError("pure derivative generator contains a mixed profile color")
        coverage[str(mode)] = {str(weight): len(parts[weight].terms) for weight in (2, 4)}
    report["new_local_generator"] = {
        "source_records_sha256": sha(canonical(comp.records)),
        "compiled_real_history_count": state_count,
        "new_fourth_history_states": len(ring.algebra.c.state_rhs)-state_count,
        "history_values_specialized": len(zero.histories_seen),
        "differentiate_before_specialize": True,
        "history_derivatives_were_set_zero": False,
        "static_geometry_specialization_used": False,
        "complete_modes": list(MODES),
        "new_geometry_derivative_weights": [2, 4],
        "real_geometry_jets_through_order_three_retained": True,
        "geometry_coefficient_counts": coverage,
        "phase_combinations": {str(mode): [[name, str(v)] for name, v in terms]
                               for mode, terms in combinations.items()},
        "old_static_local_fourth_target_recompiled": False,
        "complete_old_fourth_forcing_compiled": False}
    if report["new_local_generator"]["new_fourth_history_states"]:
        raise AssertionError("local derivative target introduced accumulated fourth states")
    return answer


def make_export(ring, potential, generators, report, scope, matrix_override=None):
    named, potential_records, generator_records = {}, [], []
    for weight, part in sorted(potential.items()):
        for index, (key, expression) in enumerate(sorted(part.terms.items())):
            name = "N"+str(weight)+"_"+str(index)
            named[name] = expression
            potential_records.append({
                "geometry_derivative_weight": weight, "geometry_key": list(extend_key(key)), "root": name})
    for mode, modes in sorted(generators.items()):
        for weight, part in sorted(modes.items()):
            for index, (key, expression) in enumerate(sorted(part.terms.items())):
                name = "v"+str(mode)+"_"+str(weight)+"_"+str(index)
                named[name] = expression
                generator_records.append({
                    "mode": mode, "geometry_derivative_weight": weight,
                    "geometry_key": list(extend_key(key)), "root": name})
    matrix = old.pointwise_matrix() if matrix_override is None else matrix_override
    matrix_rows = [
        [{"geometry_key": list(extend_key(key)), "coefficient": str(value),
          "geometry_derivative_weight": geometry_weight(key)}
         for key, value in sorted(coordinate.terms.items())]
        for coordinate in matrix]
    return {
        "schema": SCHEMA+"-original-expressions",
        "github_run_id": report["github_run_id"], "github_sha": report["github_sha"],
        "source_hashes": report["source_hashes"], "content_scope": scope,
        "geometry_names": list(GEOMETRY_NAMES),
        "potential_definition": "unreduced P_acc+P_h+R79 endpoint_potential, fixed base (1,1,1)",
        "potential_records": potential_records, "local_generator_records": generator_records,
        "pointwise_matrix_coordinate_order": list(exact.PARAMETERS),
        "pointwise_matrix_original_coefficients": matrix_rows,
        "complete_L2_formula": "v2 - B_m0(N2) - B_m2(N0)",
        "complete_L4_formula": "v4 - B_m2(N2)",
        "phase": "original complete minus-four and minus-two coefficients; no additional division",
        "real_s_derivatives_before_history_zero": True,
        "potential_two_assumed_in_W": False,
        "static_L0_and_W_recompiled": False,
        **old.serialize_expressions(ring, named)}


def write_export(path, data, maximum):
    raw = canonical(data)
    if len(raw) > MAX_RAW_BYTES:
        raise formal.CompilationBudgetExceeded("new complete original-factor raw byte budget")
    packed = gzip.compress(raw, mtime=0)
    if len(packed) > maximum:
        raise formal.CompilationBudgetExceeded("remaining complete original-factor export byte budget")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(packed)
    return {"filename": path.name, "stored_bytes": len(packed), "stored_sha256": sha(packed),
            "raw_bytes": len(raw), "raw_sha256": sha(raw), "content_scope": data["content_scope"],
            "root_count": len(data["roots"]), "profile_atom_count": len(data["profile_atoms"]),
            "potential_records": len(data["potential_records"]),
            "local_generator_records": len(data["local_generator_records"]),
            "all_original_expressions_present": True}


def actual(args, report):
    if (os.environ.get("GITHUB_ACTIONS", "").lower() != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("the real derivative-factor target is restricted to this public repository Actions")
    started = time.monotonic()
    limits = exact.Limits(seconds=args.max_seconds, nodes=500000, atoms=100000,
                          terms=100000, rewrites=1000000,
                          memory_mib=args.memory_mib, rational_bits=8192)
    ring = colored.ColoredRing(limits)
    report["phase"] = "new_missing_original_local_potential_factors"
    potential = raw_potential(ring, report)
    early = make_export(ring, potential, {}, report, "unreduced-N0-N2-only")
    path = args.out.with_name(args.out.stem+"-potential-original-expressions.json.gz")
    report["portable_potential_export"] = write_export(path, early, min(args.max_export_bytes, 1100000))
    limits.formal.time_check()
    report["phase"] = "true_s_derivatives_then_zero_history_values_for_v2_v4"
    generators = new_local_generators(ring, report)
    report["phase"] = "complete_factored_original_L2_L4_export"
    complete = make_export(ring, potential, generators, report,
                          "unreduced-N0-N2-and-complete-two-mode-v2-v4")
    remaining = min(args.max_export_bytes,
        TOTAL_OUTPUT_BYTES-MAIN_RESERVE-report["portable_potential_export"]["stored_bytes"])
    full_path = args.out.with_name(args.out.stem+"-original-expressions.json.gz")
    report["portable_complete_factor_export"] = write_export(full_path, complete, remaining)
    report.update(
        completion="complete", phase="complete",
        factored_L2_and_L4_complete=True,
        original_v2_v4_both_modes_present=True, original_N0_N2_present=True,
        response_compositions_evaluated=False, profile_substitutions_evaluated=False,
        pure_tail_quotient_or_period_evaluated=False,
        all_geometric_coefficients_independently_realizable=False,
        full_R8_or_U4_quotient_computed=False,
        coefficient_nodes=len(ring.algebra.c.nodes), profile_atoms=len(ring.p.atoms),
        elapsed_seconds=time.monotonic()-started,
        peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,
        task_complete=False)
    return report


def toy_only():
    limits = exact.Limits(seconds=40, nodes=10000, atoms=10000, terms=10000,
                          rewrites=10000, memory_mib=256)
    ring = colored.ColoredRing(limits)
    a, b, c, q = (ring.color(name) for name in ("a", "b", "c", "q"))
    zero = (0,)*8
    key2 = (0,0,0,2,0,0,0,0)
    key4 = (0,0,0,1,0,0,0,0,1,0)
    potential = split_geometry(local.GExpr(ring, {zero: a*b*c, key2: a.D()*b*c}), (0,2), 3)
    vparts = split_geometry(local.GExpr(ring, {key2: q*q*q*q, key4: q.D()*q*q*q}), (2,4), 4)
    report = {"github_run_id":None, "github_sha":None, "source_hashes":{}}
    artificial_matrix = [old.ScalarGeo.number(1)]+[old.ScalarGeo.number(0) for _ in range(7)]
    portable = make_export(ring, potential, {-4:vparts, -2:vparts}, report,
                          "artificial-only", matrix_override=artificial_matrix)
    restored_ring = colored.ColoredRing(limits)
    roots = old.decode_expressions(restored_ring, portable)
    hashes_match = all(restored_ring.digest(roots[name]) == digest
                       for name, digest in portable["original_root_sha256"].items())
    coef = ring.algebra.c
    state = coef.state(coef.constant(7), ("artificial_derivative_factor_check",))
    specializer = old.ZeroStateCoefficients(ring.algebra, static=False)
    zero_state_not_rhs = (specializer.node(state) == coef.zero
        and specializer.node(coef.derivative(state)) == coef.constant(7))
    first_jet = coef.geometry("h", 1)
    jets_kept = specializer.node(first_jet) == first_jet
    third_jet = coef.geometry("h", 3)
    third_jet_product = coef.multiply(first_jet, third_jet)
    third_jet_kept = (ThirdJetGeometryExpansion(ring.algebra, limits).node(third_jet_product)
                      == {key4:F(1)} and geometry_weight(key4)==4)
    wrong_weight_rejected = False
    try:
        split_geometry(local.GExpr(ring, {(0,0,0,1,0,0,0,0): a*b*c}), (0,2), 3)
    except AssertionError:
        wrong_weight_rejected = True
    checks = {
        "artificial_N0_and_N2_both_retained": set(potential)=={0,2} and all(x.terms for x in potential.values()),
        "artificial_v2_and_v4_both_retained": set(vparts)=={2,4} and all(x.terms for x in vparts.values()),
        "portable_original_DAG_all_root_hashes_roundtrip": hashes_match,
        "real_history_derivative_is_kept_after_value_zero": zero_state_not_rhs,
        "nonstatic_specializer_keeps_real_geometric_jets": jets_kept,
        "third_geometry_jets_are_retained_with_true_weight": third_jet_kept,
        "unexpected_geometry_weight_is_rejected": wrong_weight_rejected,
        "no_research_target_or_actual_m8_profile_evaluated": True}
    if not all(checks.values()):
        raise AssertionError("new artificial factor-export checks failed")
    return {"completion":"complete", "mode":"small_artificial_development_only",
            "checks":checks, "all_passed":True, "task_complete":False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--max-seconds", type=float, default=600)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--max-export-bytes", type=int, default=4500000)
    args = parser.parse_args()
    if min(args.max_seconds, args.memory_mib, args.max_export_bytes) <= 0:
        parser.error("positive declared budgets required")
    if args.max_export_bytes > TOTAL_OUTPUT_BYTES-MAIN_RESERVE:
        parser.error("reserve the compact main and artificial report inside the total output bound")
    started = time.monotonic()
    report = {
        "schema":SCHEMA, "completion":"started", "phase":"source_identities",
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),
        "github_sha":os.environ.get("GITHUB_SHA"),
        "scope":"new complete original factors for geometric derivative weights two/four",
        "task_complete":False}
    failed = False
    try:
        report["source_hashes"] = dependencies()
        report.update(toy_only() if args.toy_only else actual(args, report))
    except Exception as error:
        failed = True
        report.update(completion="incomplete", error_type=type(error).__name__, error=str(error),
                      new_mathematical_conclusion_published=False, task_complete=False)
    report["wall_seconds"] = time.monotonic()-started
    raw = canonical(report)+b"\n"
    if len(raw)>95000:
        raise RuntimeError("the deliberately compact producer main exceeded 95 KB")
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_bytes(raw)
    print(json.dumps({"filename":args.out.name,"bytes":len(raw),"sha256":sha(raw)},sort_keys=True),flush=True)
    if failed:
        raise SystemExit(1)


if __name__=="__main__":
    main()
