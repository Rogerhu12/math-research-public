#!/usr/bin/env python3
"""R426 same-job live closed queries of the unchanged f12f continuous C.

Only public Actions performs arithmetic. This adapter consumes actual retained
source panels, not a digest substituted for deleted payload. It reuses the
original ContinuousHead, SixPrimitiveIntegrator and QueryCover; no calibration
root, shallow coefficient, lambda, target, native gate or Loewner test changes.
An original complete coarse query remains usable when further refinement is
unavailable. All new detailed evidence stays in the owned temporary directory.
Author: OpenAI / ChatGPT exact_refinement agent, 2026-11-16.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
import json
import math
import os
from pathlib import Path
from types import SimpleNamespace
import time

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R426-same-job-original-C-live-closed-query-provider-v1"
C_NAME = "geometry_20261115_stored_continuous_E_cover_v3.py"
C_SHA = "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
BASE_METRIC_NAME = "geometry_20261115_current_C_ten_complete_relative_metric.py"
BASE_METRIC_SHA = "28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590"
FIELDS = (
    "precision_bits", "integral_absolute_bits", "integral_relative_bits",
    "analytic_guard_bits", "integral_evaluation_limit", "value_width_bits",
    "max_depth", "query_depth", "max_panels", "max_query_nodes", "budget_seconds")
ARGUMENTS = {
    "precision_bits": "c_query_precision_bits",
    "integral_absolute_bits": "c_query_integral_absolute_bits",
    "integral_relative_bits": "c_query_integral_relative_bits",
    "analytic_guard_bits": "c_query_analytic_guard_bits",
    "integral_evaluation_limit": "c_query_integral_evaluation_limit",
    "value_width_bits": "c_query_value_width_bits",
    "max_depth": "c_query_integral_max_depth",
    "query_depth": "c_query_inverse_max_depth",
    "max_panels": "c_query_max_panels",
    "max_query_nodes": "c_query_max_nodes",
    "budget_seconds": "c_query_budget_seconds",
}


def actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Scientific arithmetic only in the named public Actions repository")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode()


def receipt(path, root=None):
    path = Path(path)
    digest, size = hashlib.sha256(), 0
    with path.open("rb") as stream:
        for raw in iter(lambda:stream.read(1048576), b""):
            digest.update(raw); size += len(raw)
    return dict(file=str(path.relative_to(root)) if root else path.name,
                bytes=size, sha256=digest.hexdigest())


def identity(value):
    raw = canonical(value)
    return dict(bytes=len(raw), sha256=sha(raw))


def write(path, value, root):
    raw = canonical(value)
    with Path(path).open("xb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    return dict(file=str(Path(path).relative_to(root)), bytes=len(raw), sha256=sha(raw))


def endpoint(record):
    if (not isinstance(record, dict) or type(record.get("binary_exponent")) is not int
            or not isinstance(record.get("mantissa"), str)):
        raise ValueError("Use an actual f12f exact dyadic endpoint record")
    mantissa, exponent = int(record["mantissa"]), record["binary_exponent"]
    return Q(mantissa)*(Q(2)**exponent)


def endpoints(record):
    a, b = endpoint(record["lower"]), endpoint(record["upper"])
    if a > b:
        raise ValueError("An actual f12f interval is reversed")
    return a, b


def source_member(directory, descriptor):
    name = descriptor.get("file")
    if not isinstance(name, str) or not name:
        raise ValueError("The actual C member has no complete path")
    relative = Path(name)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("The original C member escapes its owned directory")
    result = (directory/relative).resolve()
    if result == directory or not result.is_relative_to(directory):
        raise ValueError("The original C member escapes through a symlink")
    return result


def parameter_record(args):
    result = {key:getattr(args, value) for key,value in ARGUMENTS.items()}
    bits = result["precision_bits"]
    if (type(bits) is not int or not 128 <= bits <= 8192
            or not 1 <= result["integral_absolute_bits"] <= bits
            or not 1 <= result["integral_relative_bits"] <= bits
            or not 0 <= result["analytic_guard_bits"] <= 64
            or not 1 <= result["value_width_bits"] <= bits
            or not 0 <= result["max_depth"] <= 80
            or not 0 <= result["query_depth"] <= 60
            or result["max_panels"] <= 0 or result["max_query_nodes"] <= 0
            or result["integral_evaluation_limit"] <= 0
            or not math.isfinite(result["budget_seconds"])
            or result["budget_seconds"] <= 0):
        raise ValueError("Declare the original C integration and query work parameters explicitly")
    return result


class RetainedSourceUnavailable(ValueError):
    """A missing actual input only leaves optional refinement unpaid."""


def retained_lines(path):
    try:
        with Path(path).open("rb") as stream:
            while True:
                raw = stream.readline()
                if not raw:
                    break
                yield raw
    except OSError as error:
        raise RetainedSourceUnavailable(
            "Actual retained source payload unavailable: "+Path(path).name+": "+str(error)) from error


class ActiveBudget:
    """Original panel/node counters; active oracle seconds plus global deadline.

    No independent signal handler is installed. The enclosing metric owner's
    actual signal propagates through this adapter and preserves its live query.
    As in f12f, checks are cooperative, not a hard asynchronous time bound.
    """
    def __init__(self, C, parameters, metric_started, metric_seconds):
        self.C = C
        self.seconds = parameters["budget_seconds"]
        self.max_panels = parameters["max_panels"]
        self.max_query_nodes = parameters["max_query_nodes"]
        self.panels = self.query_nodes = self.integral_calls = 0
        self.started = metric_started
        self.global_deadline = metric_started+metric_seconds
        self.active_since = None
        self.active_seconds = 0.0
        self.last_stop = None

    def begin(self):
        if self.active_since is not None:
            raise RuntimeError("Live C queries are sequential and may not nest")
        self.active_since = time.monotonic()

    def end(self):
        if self.active_since is not None:
            self.active_seconds += time.monotonic()-self.active_since
            self.active_since = None

    def check(self):
        now = time.monotonic()
        used = self.active_seconds+(0.0 if self.active_since is None else now-self.active_since)
        if now >= self.global_deadline:
            self.last_stop = "enclosing_metric_absolute_deadline_reached"
        elif used >= self.seconds:
            self.last_stop = "declared_total_active_C_query_seconds_reached"
        else:
            return
        raise self.C.ResourceStop(self.last_stop)

    def panel(self):
        self.check()
        if self.panels >= self.max_panels:
            self.last_stop = "declared_complete_primitive_panel_budget_reached"
            raise self.C.ResourceStop(self.last_stop)
        self.panels += 1

    def query(self):
        self.check()
        if self.query_nodes >= self.max_query_nodes:
            self.last_stop = "declared_complete_inverse_cover_node_budget_reached"
            raise self.C.ResourceStop(self.last_stop)
        self.query_nodes += 1

    def describe(self):
        return dict(active_query_seconds=self.active_seconds,
            active_call_in_flight=self.active_since is not None,
            active_query_seconds_budget=self.seconds,
            global_deadline_measured_from_original_metric_start=True,
            integral_panels=self.panels, inverse_cover_nodes=self.query_nodes,
            rigorous_component_integrals=self.integral_calls,
            max_integral_panels=self.max_panels, max_inverse_cover_nodes=self.max_query_nodes,
            last_actual_stop=self.last_stop, cooperative_not_hard_asynchronous_deadline=True)


class LiveQueryTarget:
    """Wrap the actual fixed R418 target; append rigorously valid same-C queries.

    The original immutable root plan sees the original cuts only. New queries
    are made on a failed metric cell's true radial interval. Identical radial
    intervals share their result across all physical angles and reflected sides.
    """
    def __init__(self, C, baseline, args, output, metric_started):
        actions()
        if Path(C.__file__).name != C_NAME or receipt(C.__file__)["sha256"] != C_SHA:
            raise ValueError("Use the complete original f12f implementation")
        self.C, self.baseline, self.args = C, baseline, args
        self.parameters = parameter_record(args)
        self.owner = Path(output).resolve()
        self.path = self.owner/"large-arrays"/"live-C-queries"
        self.path.mkdir(exist_ok=False)
        self.budget = ActiveBudget(C, self.parameters, metric_started, args.budget_seconds)
        self.state = "not_requested"
        self.disabled_reason = self.error = self.active_query = None
        self.prepared = False
        self.head = self.cover = self.integrator = None
        self.original_source_members = {}
        self.source_read = dict(expected_rows=None, committed_rows=0,
            complete_payload_identity_verified=False, complete_original1440_parameter_cover=False)
        self.actual_new_queries = 0
        self.cache_hits = 0
        self.failed_refinements = 0
        self.cache = {}
        self.ledgers = {}
        self.closed_receipts = None
        self.directory = None if not baseline.supplied else Path(args.continuous_e_result).resolve().parent
        if baseline.supplied:
            producer = baseline.producer_report
            if (producer.get("run_id") != os.environ.get("GITHUB_RUN_ID")
                    or producer.get("source_commit") != os.environ.get("GITHUB_SHA")):
                raise ValueError("This live interface consumes the actual same-job C, not a cross-run substitute")
            runner = Path(os.environ["RUNNER_TEMP"]).resolve()
            if self.directory == runner or not self.directory.is_relative_to(runner):
                raise ValueError("Retain the actual original C directory under this job RUNNER_TEMP")
        self.binding = dict(schema=SCHEMA+"-binding", source=receipt(__file__),
            original_metric_source=dict(file=BASE_METRIC_NAME, sha256=BASE_METRIC_SHA),
            original_C_source=receipt(C.__file__),
            actual_original_C_result_and_four_members=copy.deepcopy(baseline.receipts),
            complete_original_C_input_binding_identity=identity(baseline.expected_binding),
            complete_current_frozen_target_identity=identity(baseline.explicit_target),
            run_id=os.environ.get("GITHUB_RUN_ID"), source_commit=os.environ.get("GITHUB_SHA"),
            original_root_family="all-admissible-original-exact-root-sequences",
            parameters=self.parameters,
            shallow_rows_and_lambda_read_as_full_actual_binding_values=True,
            original_deleted_payload_not_recovered_from_SHA=True,
            old_source_radius_enclosures_retained_without_recalibration=True,
            original_query_index_cut_partition_immutable=True,
            original_Loewner_and_native_acceptance_unchanged=True)
        self.ledgers = {
            "requests": C.Journal(self.path/"requests.jsonl", self.owner),
            "six_primitives": C.Journal(self.path/"six-primitive-panels.jsonl", self.owner),
            "inverse_cover": C.Journal(self.path/"closed-inverse-cover.jsonl", self.owner),
            "unpaid": C.Journal(self.path/"unpaid-query-scope.jsonl", self.owner),
        }
        self.binding_receipt = write(self.path/"input-binding.json", self.binding, self.owner)

    def __getattr__(self, name):
        return getattr(self.baseline, name)

    def ball(self, value):
        return self.C.interval(*endpoints(value))

    def prepare(self):
        C, old = self.C, self.baseline
        if self.prepared:
            return
        if not old.supplied or not old.conditions_proved or old.natural_radius is None:
            self.disabled_reason = "original_complete_C_source_or_all_root_conditions_unpaid"
            return
        self.state = "binding_actual_retained_source_panels"
        self.budget.check()
        binding, report = old.binding, old.producer_report
        work = binding["work_parameters"]
        if work.get("deep_definition") != "original-exact-root-family":
            raise ValueError("The original complete root-family definition changed")
        p, rows, lam = (binding["physical_parameters"], binding["original_shallow_rows"],
                        binding["original_frozen_warp_alpha"])
        if (len(rows) != 160 or any(row["n"] != n for n,row in enumerate(rows))
                or binding["convention"].get("deep_roots_numerically_selected_or_computed") is not False):
            raise ValueError("Retain the full literal shallow table and unselected deep roots")
        self.head = C.ContinuousHead(p, rows, lam, binding)
        self.budget.check()
        index_desc = report["source_piece_index"]
        index_path = source_member(self.directory, index_desc)
        try:
            index, index_actual = C.read_bound(index_path, index_desc["sha256"])
        except OSError as error:
            raise RetainedSourceUnavailable(
                "Actual retained original source index unavailable: "+str(error)) from error
        if index_actual["bytes"] != index_desc["bytes"]:
            raise ValueError("The actual original source index size differs")
        if (index.get("schema") != C.SCHEMA+"-source-pieces"
                or index.get("original_source_order") != "n159..0/j0..8"
                or index.get("complete_piece_count") != 1440
                or len(index.get("pieces", [])) != len(self.head.pieces)):
            raise ValueError("The actual complete original source-piece index differs")
        for i,(record,piece) in enumerate(zip(index["pieces"], self.head.pieces)):
            self.budget.check()
            expected = dict(index=i, original_cell=piece.n, original_segment=piece.j,
                x_interval=["0","1"], original_order="cell159..0, segment0..8",
                cap_enabled=piece.cap_on,
                cap_layer_values=piece.cap_values if piece.cap_on else None,
                positive_weight_levels=piece.weights, flat_full=piece.flat_full,
                flat_transition=piece.flat_transition, cut_preserving=piece.cut_preserving)
            if any(not C.same(record.get(key),value) for key,value in expected.items()):
                raise ValueError("An original piece formula or literal branch parameter differs")
        self.original_source_members["source_piece_index"] = dict(index_desc)
        descriptor = report["ledgers"]["source_radial_panels"]
        path = source_member(self.directory, descriptor)
        expected_rows = descriptor["rows"]
        if type(expected_rows) is not int or expected_rows < 1440:
            raise ValueError("A complete head needs its real source panels")
        self.source_read["expected_rows"] = expected_rows
        fragments, digest, nbytes = [], hashlib.sha256(), 0
        piece_index, cursor, previous_right = 0, Q(0), None
        for raw in retained_lines(path):
            self.budget.check()
            digest.update(raw); nbytes += len(raw)
            record = json.loads(raw, object_pairs_hook=C.unique_object,
                parse_int=lambda token:-0.0 if token == "-0" else int(token),
                parse_float=C.finite_json_float,
                parse_constant=lambda token:(_ for _ in ()).throw(ValueError("Nonfinite source token")))
            if cursor == 1:
                piece_index += 1; cursor = Q(0)
            if piece_index >= len(self.head.pieces):
                raise ValueError("Extra panel after the complete original 1440 pieces")
            piece = self.head.pieces[piece_index]
            lo, hi = map(Q,record["closed_parameter_interval"])
            if (record.get("kind") != "head" or record.get("source_piece") != piece_index
                    or record.get("original_cell") != piece.n or record.get("original_segment") != piece.j
                    or lo != cursor or not Q(0) <= lo < hi <= Q(1)
                    or record.get("inverse_refinement_depth") != 0):
                raise ValueError("The original ordered closed source-panel partition has a gap or changed identity")
            rl, rr = endpoints(record["radius_left"]), endpoints(record["radius_right"])
            if previous_right is not None and rl != previous_right:
                raise ValueError("The original shared cumulative-radius record is not the preceding panel endpoint")
            fragment = dict(kind="head", piece=piece, left=lo, right=hi,
                radius_left=C.interval(*rl), radius_right=C.interval(*rr),
                box={key:self.ball(record[key]) for key in ("E","E_r","E_rr")},
                depth=0, ledger_row=record.get("primitive_ledger_row"))
            fragments.append(fragment)
            cursor, previous_right = hi, rr
            self.source_read.update(committed_rows=len(fragments), current_source_piece=piece_index,
                current_parameter_right=str(cursor), actually_read_bytes=nbytes)
        actual = dict(file=descriptor["file"], rows=len(fragments), bytes=nbytes, sha256=digest.hexdigest())
        if any(actual[key] != descriptor[key] for key in ("rows","bytes","sha256")):
            raise ValueError("The actual retained source-panel payload differs from its original complete receipt")
        if piece_index != 1439 or cursor != 1:
            raise ValueError("The full original closed source partition was not read")
        self.original_source_members["source_radial_panels"] = actual
        self.source_read.update(complete_payload_identity_verified=True,
            complete_original1440_parameter_cover=True, unvisited_original_source_panel_suffix=None)
        deep = self.head.deep_cover()
        if deep is None:
            raise ValueError("The same original all-root-family analytic deep enclosure is unavailable")
        source = dict(complete=True, complete_pieces=1440, full_source_piece_count=1440,
            fragments=fragments, outer_radius=self.ball(report["natural_outer_radius"]))
        options = SimpleNamespace(**self.parameters)
        self.integrator = C.SixPrimitiveIntegrator(self.head, options, self.budget,
            self.ledgers["six_primitives"], self.ledgers["unpaid"])
        self.cover = C.QueryCover(self.head, source, deep, options, self.budget,
            self.integrator, self.ledgers["inverse_cover"], self.ledgers["unpaid"])
        self.prepared = True
        self.state = "original_source_and_same_root_family_ready"
        self.ledgers["requests"].add(dict(kind="complete_actual_source_prepared",
            actual_source_members=self.original_source_members, source_read=self.source_read,
            all1440_original_pieces=True,
            deep_analytic_enclosure_reexecuted_for_all_original_roots=True,
            finite_head_all_six_integrals_not_reexecuted=True,
            old_cumulative_radius_intervals_not_replaced=True))

    def bounds(self, a, b):
        old = self.baseline.bounds(a,b)
        row = self.cache.get((a,b))
        fresh = row if row is not None and row.get("complete") is True else None
        if old is not None:
            lo,hi,indices = old
            sources = [dict(kind="original_complete_query", index=i) for i in indices]
            if fresh is not None:
                lo,hi = max(lo,fresh["lo"]), min(hi,fresh["hi"])
                sources.append(dict(kind="actual_same_job_refined_query", index=fresh["index"],
                    exact_same_closed_radial_interval=True))
            if lo > hi:
                raise ArithmeticError("Proved enclosures of the same C function are disjoint")
            return lo,hi,sources
        if fresh is not None:
            return fresh["lo"],fresh["hi"],[dict(kind="actual_same_job_refined_query",
                index=fresh["index"], exact_same_closed_radial_interval=True)]
        # This final/full-domain or missing-coarse path only combines real
        # completed query intervals. A query point is never extrapolated.
        selected = sorted((v for (l,r),v in self.cache.items()
            if v.get("complete") is True and l <= b and a <= r),
            key=lambda v:(v["left"],v["right"],v["index"]))
        cursor, begun = a, False
        for v in selected:
            if v["left"] > cursor:
                break
            if v["right"] >= cursor:
                cursor, begun = max(cursor,v["right"]),True
            if cursor >= b:
                break
        if not begun or cursor < b:
            return None
        return (min(v["lo"] for v in selected), max(v["hi"] for v in selected),
            [dict(kind="actual_same_job_refined_query",index=v["index"],
                closed_interval=[str(v["left"]),str(v["right"])]) for v in selected])

    def refine(self, a, b, cell):
        if not self.domain[0] <= a <= b <= self.domain[1]:
            raise ValueError("Only the actual metric cell inside the original radial field is queried")
        key = (a,b)
        if key in self.cache:
            self.cache_hits += 1
            row = self.cache[key]
            return dict(attempted=False, reused_same_interval=True, query_index=row["index"],
                complete_closed_query_bound=row.get("complete") is True,
                work_resolution_complete=row.get("work_resolution_complete"),
                previous_actual_outcome=row.get("outcome"))
        if self.disabled_reason is not None:
            return dict(attempted=False, reason=self.disabled_reason,
                old_complete_coarse_bounds_remain_available=True)
        index = self.actual_new_queries
        query = dict(index=index,id="R426-live-"+str(index),
            kind="closed-rational-radius-interval",left=a,right=b)
        query_address = dict(index=index,id=query["id"],closed_radius=[str(a),str(b)],
            requested_by_original_metric_cell=copy.deepcopy(cell))
        self.actual_new_queries += 1
        self.active_query = query_address
        self.state = "original_query_in_flight"
        self.ledgers["requests"].add(dict(kind="actual_query_begin", **query_address))
        from flint import ctx as actual_context
        old_precision = actual_context.prec
        self.budget.begin()
        row = dict(index=index,left=a,right=b,complete=False,
                   outcome="query_not_completed",work_resolution_complete=False)
        result = None
        try:
            self.budget.check()
            runtime = self.C.initialise_math(self.parameters["precision_bits"])
            self.prepare()
            if not self.prepared:
                row["outcome"] = self.disabled_reason or "source_preparation_unpaid"
            else:
                result = self.cover.run(query)
                result["continuous_model_family_conditions_proved"] = self.baseline.conditions_proved
                if (result.get("complete_closed_domain_bound") is True
                        and result.get("domain_containment_proved") is True
                        and self.baseline.conditions_proved):
                    lo,hi = endpoints(result["E"])
                    if hi < 1:
                        raise ArithmeticError("The same exact E=1+w^2 bound is inconsistent")
                    row.update(complete=True,lo=max(Q(1),lo),hi=hi,
                        outcome="actual_original_QueryCover_return",
                        work_resolution_complete=result.get("work_resolution_complete"))
                else:
                    row["outcome"] = result.get("reason","original_query_domain_unpaid")
                self.ledgers["requests"].add(dict(kind="actual_query_return", **query_address,
                    original_QueryCover_result=result, runtime=runtime,
                    complete_condition_uses_original_root_family_not_resolution_goal=True))
                if self.budget.last_stop is not None:
                    self.disabled_reason = self.budget.last_stop
        except self.C.ResourceStop as error:
            self.disabled_reason = str(error)
            row.update(outcome="controlled_live_query_resource_stop",
                complete=False, work_resolution_complete=False)
            self.failed_refinements += 1
            self.ledgers["requests"].add(dict(kind="actual_query_resource_stop",
                **query_address, error=dict(type=type(error).__name__,message=str(error)),
                actual_source_read=copy.deepcopy(self.source_read),
                old_complete_coarse_bounds_retained=True))
        except (ArithmeticError,ValueError,KeyError,TypeError) as error:
            self.error = dict(type=type(error).__name__,message=str(error),
                query_address=copy.deepcopy(query_address), source_read=copy.deepcopy(self.source_read))
            self.failed_refinements += 1
            row.update(outcome="actual_refinement_unpaid",
                complete=False, work_resolution_complete=False)
            if not self.prepared:
                self.disabled_reason = "actual_retained_source_preparation_unpaid"
            self.ledgers["requests"].add(dict(kind="actual_query_unpaid",
                **query_address,error=copy.deepcopy(self.error),
                original_complete_coarse_proof_not_revoked=True,
                pointwise_C_or_metric_failure_inferred=False))
        finally:
            self.budget.end()
            actual_context.prec = old_precision
        # An external owner signal or other uncaught interruption exits before
        # this transaction; active_query remains explicit and no new row is used.
        self.cache[key] = row
        self.active_query = None
        self.state = "query_returned" if self.disabled_reason is None else "refinement_stopped"
        return dict(attempted=True,reused_same_interval=False,query_index=index,
            complete_closed_query_bound=row["complete"],
            work_resolution_complete=row["work_resolution_complete"],
            original_result_identity=None if result is None else identity(result),
            actual_outcome=row["outcome"], disabled_reason=self.disabled_reason,
            complete_raw_query_result_retained_only_in_owned_ledger=True)

    def close(self):
        if self.closed_receipts is not None:
            return self.closed_receipts
        result = {}
        for name,ledger in self.ledgers.items():
            try:
                result[name] = ledger.finish()
            except BaseException as error:
                result[name] = dict(file=str(ledger.path.relative_to(self.owner)),
                    complete_payload_identity_not_claimed=True,
                    error=dict(type=type(error).__name__,message=str(error)))
        self.closed_receipts = result
        return result

    def live_status(self):
        suffix = None
        if (not self.source_read["complete_payload_identity_verified"]
                and self.source_read["expected_rows"] is not None):
            suffix = [self.source_read["committed_rows"],self.source_read["expected_rows"]]
        committed = list(self.cache.values())
        completed = sum(int(row.get("complete") is True) for row in committed)
        resolved = sum(int(row.get("work_resolution_complete") is True) for row in committed)
        active = copy.deepcopy(self.active_query)
        active_already_committed = (active is not None and
            any(row["index"] == active["index"] for row in committed))
        last_panel = None if self.integrator is None else self.integrator.last_panel
        last_address = None if last_panel is None else {key:copy.deepcopy(last_panel[key])
            for key in ("purpose", "source_piece", "original_cell", "original_segment",
                        "closed_parameter_interval", "depth", "finite_complete_real_range",
                        "range_error") if key in last_panel}
        return dict(schema=SCHEMA, source=receipt(__file__),
            input_binding=self.binding_receipt, actual_source_members=self.original_source_members,
            state=self.state, source_prepared=self.prepared,
            complete_original_source_read=copy.deepcopy(self.source_read),
            original_source_rows_not_yet_committed=suffix,
            entire_source_payload_unstarted=self.source_read["committed_rows"] == 0 and not self.prepared,
            active_uncommitted_query=None if active_already_committed else active,
            last_committed_query_address_not_yet_retired=active if active_already_committed else None,
            last_actual_original_integrator_address=last_address,
            requested_query_count=self.actual_new_queries, committed_query_count=len(committed),
            complete_new_query_bounds=completed,
            work_resolution_complete_queries=resolved,
            query_completion_counts_derived_from_atomic_cache_entries=True,
            failed_refinement_attempts=self.failed_refinements,
            exact_same_radial_interval_cache_hits=self.cache_hits,
            cached_radial_intervals=len(self.cache),
            actual_budget=self.budget.describe(), disabled_reason=self.disabled_reason,
            last_actual_error=copy.deepcopy(self.error), ledgers=self.closed_receipts,
            journals_closed=self.closed_receipts is not None,
            complete_journal_receipts=(None if self.closed_receipts is None else
                all("error" not in row for row in self.closed_receipts.values())),
            work_resolution_is_not_an_additional_acceptance_gate=True,
            original_C_root_sequence_or_warp_never_reselected=True,
            original_1440_head_primitive_sum_not_reexecuted=True,
            original_cumulative_radius_uncertainty_remains=True,
            original_infinite_root_family_width_remains=True,
            fixed_prefix_semantic_cut_leaf_boxes_not_refined_by_this_adapter=True,
            current_R416_cut_coefficient_boxes_not_refined_by_this_adapter=True,
            missing_target_margin_not_inferred_as_mathematical_failure=True,
            no_raw_enclosures_or_scientific_arrays_exported_in_necessary_summary=True)

    def describe(self):
        result = self.baseline.describe()
        result.update(schema=SCHEMA+"-target",same_actual_complete_original_target=True,
            live_query=self.live_status(),
            complete_field_radial_domain_covered=self.bounds(*self.domain) is not None,
            original_R418_fixed_query_description_preserved=True)
        return result

    def necessary(self):
        result = self.baseline.necessary()
        result.update(same_job_live_query=self.live_status(),
            complete_field_radial_domain_covered=self.bounds(*self.domain) is not None)
        return result
