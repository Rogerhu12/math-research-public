"""Attach the fixed G13 calculation only to the two true original endpoint functions."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research Actions.")

import ast
from hashlib import sha256
import inspect
import textwrap
from types import FunctionType
from pathlib import Path

import original_scalar_base_divisor_support as scalar
import original_triangular_artinian_values as values
from original_short_graph_global import fixed_original_low_graph
from original_short_graph_outer import fixed_endpoint_after_low_graph
from original_ys_divisor_ideal_tools import digest, element_digest, polynomial_matrix_digest

IMPLEMENTATION = "original-complete-short-G13-two-chart-endpoint"
SOURCE_DEPENDENCIES = (
    "original_short_graph_production_binding.py", "original_short_graph_global.py",
    "original_short_graph_kernel.py", "original_short_graph_outer.py", "original_short_graph_field.py",
    "original_short_graph_popov.py", "original_short_graph_multichain.py", "original_adaptive_dixon_solver.py",
)
ORIGINAL_RUNNER = scalar._new_geometry_runner
ORIGINAL_ZERO_POLES = values.OriginalTriangularIdealEngine.zero_pole_ideals
ORIGINAL_GRAPH = values.complete_paired_fraction_graph
ORIGINAL_MULTIPLE = values.OriginalTriangularIdealEngine.integral_fraction_multiple
SESSIONS = []
TEMPLATE = None


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


class EndpointSession:
    def __init__(self):
        self.pending = {}
        self.entries = {}
        self.low = {}

    def selected(self, six, engines, function, flag, N, D, label):
        possible = [i for i in (0,1) if function is six["A"][i]["y0"]]
        if not possible:
            require(label not in ("original A0 y0","original A1 y0"), "Changed labelled endpoint identity")
            return engines[flag].zero_pole_ideals(N,D,label)
        index, = possible
        engine = engines[flag]
        require(type(flag) is bool and engine.infinity_chart is flag and
                label == "original A%d y0"%index and (index,flag) not in self.entries,
                "Duplicated or mismatched original endpoint chart")
        actual = function.chart_pair(flag)
        require(actual[0] is N and actual[1] is D, "Changed original endpoint fraction objects")
        if not flag:
            require(index not in self.low and not self.pending,
                    "The original finite/reciprocal endpoint order changed")
            engine.progress("constructing actual two-chart degree13 endpoint graph", endpoint=index)
            blocks, low = fixed_original_low_graph(six,index,engines)
            self.low[index] = low
            self.pending[index] = blocks
            engine.progress("actual degree13 complete fibre and both original graphs returned", endpoint=index,
                            full_RR_dimension=low["actual_full_RR_dimension"],
                            paired_weight_sum=low["actual_low_graph_row_weight_sum"],
                            full_low_receipt_sha256=digest(low))
        require(index in self.pending and flag in self.pending[index], "Missing actual paired chart")
        Y,X = self.pending[index].pop(flag)
        if not self.pending[index]:
            del self.pending[index]
        low = self.low[index]
        chart = "reciprocal" if flag else "finite"
        key = "infinity" if flag else "finite"
        require(low["actual_original_function_id"] == id(function) and
                low["actual_"+key+"_engine_id"] == id(engine) and
                low["original_"+key+"_N"] == element_digest(N) and
                low["original_"+key+"_D"] == element_digest(D) and
                low["original_"+chart+"_Y"] == polynomial_matrix_digest(Y) and
                low["original_"+chart+"_X"] == polynomial_matrix_digest(X),
                "A low graph no longer matches its actual chart, source, or polynomial blocks")
        positives, negatives, ret = fixed_endpoint_after_low_graph(engine,six,index,Y,X,engines)
        graph, outer = ret["kernel"], ret["post_ideal_outer"]
        require(graph["original_G_N_sha256"] == element_digest(N) and
                graph["original_G_D_sha256"] == element_digest(D) and
                outer["actual_positive_id"] == id(positives) and outer["actual_negative_id"] == id(negatives),
                "The actual polynomial sources or returned original ideal objects changed")
        ret.update(original_function=label,numerator_sha256=element_digest(N),
                   denominator_sha256=element_digest(D),zero_ideal=positives.receipt,
                   pole_ideal=negatives.receipt,concrete_implementation=IMPLEMENTATION,
                   only_this_affine_chart=True,closed_points_or_shadow_claimed=False,
                   complete_original_low_graph_sha256=digest(low))
        self.entries[index,flag] = (six,engines,function,positives,negatives,ret)
        engine.progress("actual short endpoint complete after both current ideals", endpoint=index,
                        infinity_chart=flag, actual_positive_length=int(positives.length),
                        actual_negative_length=int(negatives.length), complete_post_ideal=outer)
        return positives,negatives,ret


def _new_geometry_runner():
    old, scalar_session = ORIGINAL_RUNNER()
    require(old.__code__ is scalar.PREPARED.__code__ and
            old.__globals__["_scalar_base_support_only"] == scalar_session.decompose,
            "The per-call original scalar-support geometry runner changed")
    env = dict(old.__globals__)
    session = EndpointSession()
    SESSIONS.append(session)
    env["_short_endpoint_or_original"] = session.selected
    runner = FunctionType(TEMPLATE,env,old.__name__,old.__defaults__,old.__closure__)
    runner.__kwdefaults__ = old.__kwdefaults__
    return runner,scalar_session


def bind_original_endpoint_graphs():
    global TEMPLATE
    require(TEMPLATE is None and not SESSIONS and scalar._new_geometry_runner is ORIGINAL_RUNNER and
            values.OriginalTriangularIdealEngine.zero_pole_ideals is ORIGINAL_ZERO_POLES and
            values.complete_paired_fraction_graph is ORIGINAL_GRAPH and
            values.OriginalTriangularIdealEngine.integral_fraction_multiple is ORIGINAL_MULTIPLE,
            "The unchanged original fallback or a geometry session is already bound")
    info = scalar.prepare_source_bindings()
    base = textwrap.dedent(inspect.getsource(scalar.ORIGINAL_GEOMETRY))
    require(sha256(base.encode()).hexdigest() == info["original_geometry_source_sha256"],
            "Wrong complete original geometry source")
    scalar_code = base.replace("def prepare_original_ys_geometry_with_complete_transports(",
                               "def _prepare_geometry_with_scalar_base_support(")
    scalar_code = scalar_code.replace("points,record = decompose_complete_ideal(",
                                      "points,record = _scalar_base_support_only(")
    require(sha256(scalar_code.encode()).hexdigest() == info["prepared_geometry_source_sha256"],
            "The original scalar-support body did not authenticate")
    previous = "positive,negative,record = engines[flag].zero_pole_ideals(N,D,label)"
    current = "positive,negative,record = _short_endpoint_or_original(six,engines,function,flag,N,D,label)"
    require(scalar_code.count(previous) == 1 and current not in scalar_code, "Changed geometric call site")
    new = scalar_code.replace(previous,current)
    require(new.replace(current,previous) == scalar_code, "Nonreversible original geometry addition")
    ast.parse(new)
    namespace = dict(scalar.PREPARED.__globals__)
    exec(compile(new,str(Path(__file__))+":complete-physical-geometry","exec"),namespace)
    TEMPLATE = namespace["_prepare_geometry_with_scalar_base_support"].__code__
    scalar._new_geometry_runner = _new_geometry_runner
    return dict(implementation=IMPLEMENTATION,previous_body=sha256(scalar_code.encode()).hexdigest(),
                prepared_body=sha256(new.encode()).hexdigest(),reversible_new_call_sites=1,
                general_zero_pole_method_and_full_paired_graph_unchanged=True,
                original_scalar_support_runner_and_all_remaining_calls_preserved=True,
                mathematical_instances_by_binding=0)


def actual_endpoint_usage(context):
    require(context["certificate"]["status"] == "all_requested_original_acceptance_gates_completed" and
            len(SESSIONS) == 1 and scalar._new_geometry_runner is _new_geometry_runner and
            values.OriginalTriangularIdealEngine.zero_pole_ideals is ORIGINAL_ZERO_POLES and
            values.complete_paired_fraction_graph is ORIGINAL_GRAPH and
            values.OriginalTriangularIdealEngine.integral_fraction_multiple is ORIGINAL_MULTIPLE,
            "Original complete pipeline or unchanged general source did not return")
    session, = SESSIONS
    geo,six = context["geometry"],context["six"]
    require(geo["six"] is six and not session.pending and set(session.low) == {0,1} and
            set(session.entries) == {(i,f) for i in (0,1) for f in (False,True)}, "Missing a true chart")
    checks = []
    for (i,flag),(owner,engines,function,positive,negative,rec) in sorted(session.entries.items()):
        engine, low = engines[flag], session.low[i]
        item = geo["endpoint_poles"][i]["y0"]
        N,D = function.chart_pair(flag)
        graph, outer = rec["kernel"], rec["post_ideal_outer"]
        scan, proof = graph["all_rows"], graph["complete_low_graph"]
        require(owner is six and engines is geo["engines"] and function is six["A"][i]["y0"] and
                item is geo["complete_principal_divisor_cache"][id(function)] and item["function"] is function and
                rec is item["records"][str(flag)] and positive is item["charts"][flag]["positive"] and
                negative is item["charts"][flag]["negative"] and positive.engine is negative.engine is engine and
                rec["zero_ideal"] == positive.receipt and rec["pole_ideal"] == negative.receipt,
                "The final geometric consumer did not use those same two actual ideals")
        require(rec["complete_original_low_graph_sha256"] == digest(low) and
                rec["numerator_sha256"] == graph["original_G_N_sha256"] == element_digest(N) and
                rec["denominator_sha256"] == graph["original_G_D_sha256"] == element_digest(D) and
                graph["full_MN_sha256"] == low["original_operator_sha256"][2 if flag else 0] and
                graph["full_MD_sha256"] == low["original_operator_sha256"][3 if flag else 1] and
                proof["actual_original_function_id"] == id(function) and proof["actual_chart"] is flag and
                proof["actual_original_endpoint"] == i and proof["full_independent_shift_count"] == 1164 and
                positive.basis.is_hermite() and negative.basis.is_hermite(),
                "The final raw numerator/denominator/paired module binding changed")
        require(outer["actual_engine_id"] == id(engine) and outer["infinity_chart"] is flag and
                outer["actual_numerator_input_id"] == id(N) and outer["actual_denominator_input_id"] == id(D) and
                outer["actual_positive_id"] == id(positive) and outer["actual_negative_id"] == id(negative) and
                outer["positive_hnf_sha256"] == polynomial_matrix_digest(positive.basis) and
                outer["negative_hnf_sha256"] == scan["complete_hermite_sha256"] == polynomial_matrix_digest(negative.basis) and
                outer["source_row_count_verified_after_both_ideals"] == 306 and
                [row["index"] for row in scan["complete_source_rows"]] == list(range(306)) and
                all(row["exact_full_residual_zero"] for row in scan["complete_source_rows"]) and
                outer["complete_X_sha256"] == scan["complete_X_sha256"] and
                outer["complete_post_ideal_row_stream_sha256"] == digest(scan["complete_source_rows"]),
                "Actual post-ideal complete polynomial row identity missing")
        checks.append(dict(endpoint=i,infinity_chart=flag,full_graph_sha256=digest(graph),
                           actual_positive_receipt_sha256=digest(positive.receipt),
                           actual_negative_receipt_sha256=digest(negative.receipt),post_ideal_outer=outer))
    f = geo["F_poles"]
    require(f["function"] is six["F_y"] and f is geo["complete_principal_divisor_cache"][id(six["F_y"])],
            "Wrong original first factor")
    old_f = []
    for flag in (False,True):
        graph = f["records"][str(flag)]["kernel"]
        div = graph["full_paired_numerator_division"]
        require(div["method"] == "same full attached-column Hermite reduction and exact back substitution" and
                div["reduction"] is not None and div["reduction"]["attached_block"] and
                div["every_source_row_returned_against_original_denominator"] and
                div["no_source_row_dropped_or_rescaled"] and not div["fractional_solution_or_denominator_clearing_used"],
                "Missing complete original first-factor attached-column return")
        old_f.append(dict(infinity_chart=flag,graph_sha256=digest(graph)))
    return dict(implementation=IMPLEMENTATION,actual_two_complete_RR_inputs=[session.low[i] for i in (0,1)],
                actual_four_whole_current_endpoint_calls=checks, original_F_attached_Hermite_route=old_f)
