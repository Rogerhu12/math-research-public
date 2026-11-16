#!/usr/bin/env python3
"""R530: R526 finite bidirectional distance correspondences on actual R520 images.

All arithmetic runs only in the named public Actions.  The exact registered
R517/R520 binder, its complete original image ledger and its cap member
evaluation are reused.  This module adds the finite correspondence kernel;
a single literal source view reuses the original R520 owned caller.
No numerical field, accepted parent, request, gamma, clock or solver gate
is created.  No current workflow is changed.
Author: OpenAI ChatGPT geometry agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import traceback

HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R530-complete-bidirectional-distance-correspondence-lower-bound-v1"
LIMIT = 90000
PROOF = dict(file="R526-complete-bidirectional-distance-correspondences-and-quotient-lower-bound.md",
    bytes=21774, sha256="a02c931e0453b499abfa763a934953581d7d2f995d71301e5d19526c2efb4b49")
R520 = dict(file="geometry_20261116_current_generated_image_quotient.py",
    bytes=47597, sha256="8d48856dcdc642f56779bff949a473b352c26edf0fda9e65937e2ce4feba1ef2")
R520_PLAN = dict(file="R520-current-generated-image-quotient-source-plan.json",
    bytes=11453, sha256="e288f2d037c65f05682ec498ab4230613920d82a3deb15780567d43088fe5877")
PLAN_SCHEMA = "R530-original-R520-owned-distance-correspondence-source-view-v1"
ADAPTER_NAME = "geometry_20261116_current_generated_distance_correspondence.py"
FAMILIES = ("original112", "resolution112", "incrementalM")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "Scientific arithmetic is only allowed in the named public Actions")


def receipt(path):
    path = Path(path).resolve(strict=True)
    size, h = 0, hashlib.sha256()
    with path.open("rb") as stream:
        for raw in iter(lambda: stream.read(1048576), b""):
            size += len(raw)
            h.update(raw)
    return dict(file=str(path), bytes=size, sha256=h.hexdigest())


def same(a, b):
    return isinstance(a, dict) and isinstance(b, dict) and (
        a.get("bytes"), a.get("sha256")) == (b.get("bytes"), b.get("sha256"))


def read(path, expected):
    got = receipt(path)
    require(same(got, expected), "Use the exact complete source metadata: "+str(path))
    raw = Path(path).read_bytes()
    require(len(raw) == got["bytes"] and hashlib.sha256(raw).hexdigest() == got["sha256"],
        "The complete source metadata changed during reading")
    return json.loads(raw), got


def registered_backend(backend, computations, family, original_plan):
    """Select an already generated original binder; no class/global patch."""
    actions()
    comp = Path(computations).resolve(strict=True)
    require(comp == HERE and family in FAMILIES,
        "Use the actual same computations and one explicit R520 family")
    plan, plan_id = read(original_plan, R520_PLAN)
    require(plan.get("schema") ==
        "R520-current-generated-image-quotient-source-registration-v1"
        and plan.get("repository") == REPOSITORY
        and set(plan["families"]) == set(FAMILIES),
        "Keep the complete original finite image-source registration")
    row = plan["families"][family]
    source = receipt(comp/row["kernel"]["file"])
    require(Path(backend.__file__).resolve() == comp/row["kernel"]["file"]
        and same(source, row["kernel"]) and backend.SCHEMA == row["kernel"]["schema"],
        "The actual original binder module/source differs")
    require((backend.R425_NAME, backend.R425_SHA, backend.R425_SCHEMA) ==
        (row["producer"]["file"], row["producer"]["sha256"], row["producer"]["schema"])
        and (backend.CAP_NAME, backend.CAP_SHA, backend.CAP_SCHEMA) ==
        (row["cap"]["file"], row["cap"]["sha256"], row["cap"]["schema"]),
        "Retain the actual complete field/cap tuple")
    return row, source, plan_id


class Work:
    """Same caller clock; independent explicit finite-search work maxima."""
    def __init__(self, backend, check_budget, *, max_prefixes,
                 max_distance_evaluations, max_cover_balls):
        actions()
        require(callable(check_budget), "Use the actual original absolute-clock callback")
        limits = dict(prefixes=max_prefixes, distances=max_distance_evaluations,
            cover_balls=max_cover_balls)
        require(all(type(v) is int and v > 0 for v in limits.values()),
            "Every declared work limit must be an explicit positive integer")
        self.backend, self.external, self.limits = backend, check_budget, limits
        self.counts = dict.fromkeys(limits, 0)
        self.cursor = dict(stage="complete-original-image-input-binding")
        self.observed_original = {}

    def check(self):
        self.external()

    def begin(self, kind):
        self.check()
        require(kind in self.limits, "An unknown unit cannot be charged to an original work counter")
        if self.counts[kind] >= self.limits[kind]:
            raise self.backend.Stop("declared_correspondence_"+kind+"_work_limit")
        self.counts[kind] += 1


class CorrespondenceCover:
    """DFS frontier is an exact disjoint union of mixed-radix suffix blocks.

    A frame is (fixed prefix, next candidate for the next vertex).  All later
    vertices still range over their entire corresponding target ball lists.
    On descent the parent's suffix advances atomically with insertion of the
    complete child frame.  A budget check occurs before any frontier removal.
    """
    def __init__(self, backend, images, gamma, sqrt_bits, work, ledger):
        actions()
        require(type(images) is backend.BoundImages and isinstance(images.binding, dict),
            "Use the actual already bound complete R520 BoundImages object")
        require(images.cover0 and images.cover1 and images.witness0 and images.witness1,
            "Both full image covers and both true member lists must be nonempty")
        self.K, self.images, self.work, self.ledger = backend, images, work, ledger
        self.gamma = backend.rational(gamma)
        require(self.gamma > 0, "Use an explicit positive candidate; no default gamma is chosen")
        require(type(sqrt_bits) is int and 0 <= sqrt_bits <= 8192,
            "Use an explicit nonnegative square-root work precision")
        self.sqrt_bits = sqrt_bits
        self.n0, self.n1 = len(images.witness0), len(images.witness1)
        self.m0, self.m1 = len(images.cover0), len(images.cover1)
        self.n = self.n0+self.n1
        self.radices = [self.m1]*self.n0+[self.m0]*self.n1
        self.stack = [dict(prefix=[], next_candidate=0,
            lower=Q(0), witness_edge=None)]
        self.current = None
        self.paid_prefixes = 0
        self.minimum_paid_prefix_lower = None
        self.completed = False
        self.unseparated_complete_assignment = None

    def vertex(self, prefix, index):
        """A=S0 and B=S1; both directions are in the same correspondence."""
        selected = prefix[index]
        if index < self.n0:
            xb = self.images.witness0[index]
            yb = self.images.cover1[selected]
            references = dict(A=dict(kind="witness0", index=index),
                B=dict(kind="cover1", index=selected))
        else:
            j = index-self.n0
            xb = self.images.cover0[selected]
            yb = self.images.witness1[j]
            references = dict(A=dict(kind="cover0", index=selected),
                B=dict(kind="witness1", index=j))
        return dict(X=xb["center"], Y=yb["center"],
            alpha=xb["radius"], beta=yb["radius"],
            sum_error=xb["radius"]+yb["radius"], references=references)

    def evaluate_child(self, frame, selected):
        prefix = list(frame["prefix"])+[selected]
        last = len(prefix)-1
        current = dict(prefix=prefix, new_vertex_index=last,
            next_previous_vertex_index=0, accumulated_lower=frame["lower"],
            witness_edge=copy.deepcopy(frame["witness_edge"]),
            complete_new_edges=False, prefix_ledger_ordinal=None,
            within_original_frontier=True)
        self.current = current
        self.work.cursor = dict(stage="before-correspondence-prefix",
            complete_prefix=list(prefix), new_vertex_index=last,
            next_previous_vertex_index=0, original_frontier_retained=True)
        self.work.begin("prefixes")
        ordinal = self.ledger.rows
        self.ledger.add(dict(kind="begin_complete_candidate_prefix",
            prefix=prefix, new_vertex_index=last, inherited_lower=frame["lower"],
            complete_remaining_target_radices=self.radices[len(prefix):],
            repeated_target_indices_allowed=True))
        current["prefix_ledger_ordinal"] = ordinal
        end = self.vertex(prefix, last)
        for previous in range(last):
            other = self.vertex(prefix, previous)
            pair = [previous,last]
            self.work.cursor = dict(stage="correspondence-edge-distance",
                complete_prefix=list(prefix), pair=pair,
                next_previous_vertex_index=previous, distance_side="A",
                accumulated_complete_edge_lower=current["accumulated_lower"],
                completed_prefix_edge_count=previous,
                current_prefix_ledger_ordinal=ordinal,
                original_frontier_retained=True)
            current["next_previous_vertex_index"] = previous
            self.work.begin("distances")
            x_bounds = self.K.sqrt_bounds(
                self.K.square_distance(other["X"], end["X"]), self.sqrt_bits)
            self.work.cursor.update(distance_side="B", completed_A_distance_interval=x_bounds)
            self.work.begin("distances")
            y_bounds = self.K.sqrt_bounds(
                self.K.square_distance(other["Y"], end["Y"]), self.sqrt_bits)
            gap = max(Q(0), x_bounds[0]-y_bounds[1], y_bounds[0]-x_bounds[1])
            errors = other["sum_error"]+end["sum_error"]
            lower = max(Q(0), gap-errors)/2
            edge = dict(pair=pair, A_distance_interval=x_bounds,
                B_distance_interval=y_bounds, distance_interval_gap=gap,
                complete_vertex_error_sum=errors, edge_lower=lower,
                vertex_references=[other["references"],end["references"]],
                vertex_individual_errors=[
                    dict(alpha=other["alpha"],beta=other["beta"]),
                    dict(alpha=end["alpha"],beta=end["beta"])])
            self.ledger.add(dict(kind="complete_candidate_edge",
                prefix_ledger_ordinal=ordinal, **edge))
            if lower > current["accumulated_lower"]:
                current["accumulated_lower"] = lower
                current["witness_edge"] = edge
            current["next_previous_vertex_index"] = previous+1
            self.work.cursor.update(stage="complete-correspondence-edge",
                next_previous_vertex_index=previous+1,
                accumulated_complete_edge_lower=current["accumulated_lower"])
        current["complete_new_edges"] = True
        self.work.cursor = dict(stage="complete-correspondence-prefix-bound",
            complete_prefix=list(prefix), new_vertex_index=last,
            next_previous_vertex_index=last,
            accumulated_complete_edge_lower=current["accumulated_lower"],
            all_edges_between_assigned_vertices_paid=True,
            current_prefix_ledger_ordinal=ordinal, original_frontier_retained=True)
        return current

    def run(self):
        while self.stack:
            self.work.check()
            frame = self.stack[-1]
            variable = len(frame["prefix"])
            require(variable < self.n, "Complete assignments are never silently expanded")
            radix = self.radices[variable]
            if frame["next_candidate"] == radix:
                # All its complete candidate subtrees have already been paid.
                self.work.check()
                self.stack.pop()
                continue
            require(0 <= frame["next_candidate"] < radix,
                "Retain the entire unvisited half-open candidate suffix")
            selected = frame["next_candidate"]
            current = self.evaluate_child(frame, selected)
            prefix = current["prefix"]
            lower = current["accumulated_lower"]
            if lower >= self.gamma:
                self.work.check()
                self.ledger.add(dict(kind="entire_correspondence_prefix_paid",
                    prefix=prefix, complete_remaining_target_radices=self.radices[len(prefix):],
                    prefix_ledger_ordinal=current["prefix_ledger_ordinal"],
                    bound=lower, requested_gamma=self.gamma,
                    witness_edge=current["witness_edge"],
                    all_edges_between_assigned_vertices_paid=True,
                    every_remaining_repeated_target_choice_included=True))
                # No budget callback or asynchronous scientific exception is
                # inserted between recording this proof and advancing its suffix.
                frame["next_candidate"] = selected+1
                self.paid_prefixes += 1
                self.minimum_paid_prefix_lower = (lower if
                    self.minimum_paid_prefix_lower is None else
                    min(self.minimum_paid_prefix_lower, lower))
                self.current = None
                continue
            if len(prefix) == self.n:
                # One full nonseparated assignment is enough to leave this
                # candidate gamma unproved.  It is not a congruence witness.
                self.work.check()
                self.ledger.add(dict(kind="complete_assignment_not_separated",
                    prefix=prefix, prefix_ledger_ordinal=current["prefix_ledger_ordinal"],
                    bound=lower, requested_gamma=self.gamma,
                    all_N_choose_two_edges_included=True,
                    actual_rigid_motion_or_congruence_not_inferred=True,
                    current_assignment_and_all_other_frontier_retained=True))
                self.unseparated_complete_assignment = copy.deepcopy(current)
                return
            self.work.check()
            child = dict(prefix=list(prefix), next_candidate=0,
                lower=lower, witness_edge=copy.deepcopy(current["witness_edge"]))
            parent = dict(frame, next_candidate=selected+1)
            # Allocate the entire replacement before making it current.
            self.stack = self.stack[:-1]+[parent,child]
            self.current = None
        self.completed = True
        self.work.cursor = dict(stage="all_finite_correspondence_blocks_paid",
            complete_frontier_empty=True)

    def report(self):
        return dict(
            vertex_order=dict(first="all witness0 in original list order",
                second="all witness1 in original list order",
                witness0_count=self.n0, witness1_count=self.n1),
            complete_target_ball_counts=dict(cover0=self.m0,cover1=self.m1),
            complete_target_radices=list(self.radices),
            complete_universe_cardinality_factorization=[
                dict(base=self.m1,exponent=self.n0),
                dict(base=self.m0,exponent=self.n1)],
            repeated_candidates_allowed=True,
            both_same_direction_and_all_cross_edges_included=True,
            desired_gamma=self.gamma,
            complete_candidate_lower_test=self.completed,
            requested_quotient_lower_bound_proved=self.completed,
            quotient_distance_lower_bound=self.gamma if self.completed else None,
            minimum_retired_prefix_lower=self.minimum_paid_prefix_lower,
            retired_prefix_minimum_is_not_a_partial_global_lower=True,
            retired_prefix_count=self.paid_prefixes,
            complete_unvisited_frontier=[
                dict(fixed_prefix=list(frame["prefix"]),
                    next_vertex_index=len(frame["prefix"]),
                    unvisited_target_half_open_suffix=[
                        frame["next_candidate"],self.radices[len(frame["prefix"])]],
                    complete_later_target_radices=self.radices[len(frame["prefix"])+1:],
                    certified_lower_for_this_prefix=frame["lower"],
                    original_maximizing_edge=copy.deepcopy(frame["witness_edge"]))
                for frame in self.stack],
            frontier_blocks_are_disjoint_and_cover_every_unretired_complete_assignment=True,
            current_evaluation=copy.deepcopy(self.current),
            current_evaluation_is_part_of_frontier_not_an_additional_disjoint_block=True,
            complete_unseparated_assignment=copy.deepcopy(self.unseparated_complete_assignment),
            unresolved_is_not_a_congruence_or_actual_upper_bound=True,
            complete_original_distance_maximum_Lstar_not_claimed=True,
            no_pose_grid_no_permutation_or_injectivity_assumption=True,
            continuous_input_refinement_or_finite_budget_success_not_promised=True)


def produce(*, backend, family, original_plan, computations, directory,
            result_sha256, out, cap_points, desired_gamma, sqrt_bits,
            max_prefixes, max_distance_evaluations, max_cover_balls,
            check_budget, caller_clock_identity):
    """Drop-in owned-call slot; all clock/owner work stays in the R520 caller."""
    actions()
    row, backend_source, plan_id = registered_backend(
        backend, computations, family, original_plan)
    K = backend
    require(isinstance(caller_clock_identity, dict) and caller_clock_identity,
        "Record the actual original clock and owned process provenance")
    gamma = K.rational(desired_gamma)
    require(gamma > 0 and type(sqrt_bits) is int and 0 <= sqrt_bits <= 8192,
        "Use an explicit positive candidate and bounded square-root work precision")
    root = K.output_directory(out, directory, computations)
    root.mkdir()
    large = root/"large-arrays"
    large.mkdir()
    work = Work(K, check_budget, max_prefixes=max_prefixes,
        max_distance_evaluations=max_distance_evaluations, max_cover_balls=max_cover_balls)
    images = cover = ledger = None
    members, errors = {}, []
    resource = None
    stage = "complete-original-image-input-binding"
    scope = dict(family=family, complete_original_source_plan=plan_id,
        actual_registered_binder=backend_source, actual_registered_tuple=row,
        actual_original_directory=str(Path(directory).resolve()),
        actual_original_result_sha256=result_sha256,
        explicit_cap_point_plan=copy.deepcopy(cap_points),
        desired_gamma=gamma, sqrt_bits=sqrt_bits, explicit_work_limits=work.limits,
        caller_clock_identity=copy.deepcopy(caller_clock_identity))
    try:
        work.check()
        members["request_scope"] = K.write_member(root,"actual-input-scope.json",scope)
        images = K.bind_r425(computations=computations,directory=directory,
            result_sha256=result_sha256,cap_points=cap_points,sqrt_bits=sqrt_bits,work=work)
        members["complete_image_binding"] = K.write_member(
            root,"complete-image-binding.json",images.binding)
        members["all_member_balls"] = K.write_member(
            root,"large-arrays/all-actual-member-balls.json",
            dict(phase0=images.witness0,phase1=images.witness1,
                same_actual_fixed_caps_in_both_phases=True))
        ledger = K.DecisionLedger(large/"complete-correspondence-decisions.jsonl.gz",root)
        cover = CorrespondenceCover(K,images,gamma,sqrt_bits,work,ledger)
        stage = "complete-finite-correspondence-universe"
        cover.run()
        stage = ("all-finite-correspondence-blocks-paid" if cover.completed else
            "complete-assignment-unseparated-with-entire-frontier-retained")
    except K.Stop as exc:
        resource = dict(type=type(exc).__name__,message=str(exc),stage=stage,
            original_caller_cause=None if exc.__cause__ is None else dict(
                type=type(exc.__cause__).__name__,message=str(exc.__cause__)))
    except BaseException as exc:
        errors.append(dict(type=type(exc).__name__,message=str(exc),stage=stage,
            complete_traceback=traceback.format_exc()))
    finally:
        if ledger is not None:
            try:
                members["complete_correspondence_decisions"] = ledger.close()
            except BaseException as exc:
                errors.append(dict(type=type(exc).__name__,message=str(exc),
                    stage="close-actual-decision-ledger",complete_traceback=traceback.format_exc()))
    search = None if cover is None else cover.report()
    proved = (cover is not None and cover.completed and resource is None and not errors)
    result = dict(schema=SCHEMA,source=K.file_receipt(__file__),proof=PROOF,
        repository=REPOSITORY,run_id=os.environ.get("GITHUB_RUN_ID"),
        source_commit=os.environ.get("GITHUB_SHA"),family=family,
        actual_complete_registered_binder_source=backend_source,
        original_complete_source_plan=plan_id,current_stage=stage,
        errors=errors,resource_stop=resource,
        resources=dict(limits=work.limits,actual_counts=work.counts,sqrt_bits=sqrt_bits),
        caller_clock_identity=copy.deepcopy(caller_clock_identity),
        only_original_supplied_clock_used=True,
        new_science_clock_or_owned_process_created=False,
        complete_original_input_binding_returned=images is not None,
        observed_original_source=copy.deepcopy(work.observed_original),
        complete_original_images=None if images is None else dict(
            phase0_cover_balls=len(images.cover0),phase1_cover_balls=len(images.cover1),
            phase0_member_balls=len(images.witness0),phase1_member_balls=len(images.witness1),
            source_result=images.binding["actual_R425_result"],
            input_binding=images.binding["actual_input_binding"],
            position_result=images.binding["actual_position_result"],
            original_complete_position_ledger=images.binding["actual_position_ledger"],
            original_active_member_count=images.binding["active_member_count"],
            actual_cap_member_counts=images.binding["cap_member_counts"],
            complete_binding_identity=K.identity(images.binding)),
        correspondence_cover=search,
        requested_quotient_lower_bound_proved=proved,
        quotient_distance_lower_bound=gamma if proved else None,
        unfinished_before_search=None if cover is not None else dict(
            actual_complete_input_cursor=copy.deepcopy(work.cursor),
            entire_finite_correspondence_universe_unstarted=True,
            target_cardinalities_unavailable_until_complete_images=images is None),
        actual_interruption_cursor=copy.deepcopy(work.cursor),members=members,
        all_unretired_correspondences_remain_in_the_complete_frontier=True,
        successful_decision_rows_only_identified_in_chat_not_reencoded=True,
        original_field_parent_or_raw_members_removed=False,
        actual_owned_process_quiescence_observed=False,
        actual_metric_reach_native_or_task_success_inferred=False)
    rid = K.write_member(root,"result.json",result)
    summary = dict(result,actual_result=rid,
        necessary_scope="Complete finite frontier, current prefix/pair/side cursor, "
            "all errors/resource/unseparated assignment and actual input identities; "
            "complete successful decisions remain only in the actual temporary ledger.")
    payload = K.canonical(summary)
    if len(payload) > LIMIT:
        fallback = dict(schema=SCHEMA+"-necessary-over-budget",
            attempted_bytes=len(payload),attempted_sha256=K.digest(payload),
            actual_result=rid,complete_necessary_readback=False,raw_retained=True,
            original_scientific_result_not_replaced=True,quiescent_or_cleanup_allowed=False)
        necessary = K.write_member(root,"necessary-over-budget.json",fallback)
        print("BEGIN_R530_COMPLETE_CORRESPONDENCE_NECESSARY",flush=True)
        print(K.canonical(fallback).decode(),end="",flush=True)
        print("END_R530_COMPLETE_CORRESPONDENCE_NECESSARY",flush=True)
        return dict(exit_code=70,original_result=rid,necessary=necessary,
            complete_necessary_readback=False)
    necessary = K.write_member(root,"necessary-summary.json",summary)
    print("BEGIN_R530_COMPLETE_CORRESPONDENCE_NECESSARY",flush=True)
    print(payload.decode(),end="",flush=True)
    print("END_R530_COMPLETE_CORRESPONDENCE_NECESSARY",flush=True)
    return dict(exit_code=1 if errors else 2 if not proved else 0,
        original_result=rid,necessary=necessary,complete_necessary_readback=True,
        original_caller_must_observe_true_quiescence_before_any_cleanup=True)


def materialize(args):
    """Metadata only, after the original R520 binder views really exist."""
    actions()
    comp = Path(args.computations).resolve(strict=True)
    require(comp == HERE,"Materialize the actual new basename in this computations directory")
    require(same(receipt(comp/R520["file"]),R520),"Keep the actual original R520 caller")
    spec = importlib.util.spec_from_file_location("_R530_original_R520",comp/R520["file"])
    old = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = old
    spec.loader.exec_module(old)
    B = old.Binding(args.base,comp,args.original_plan)
    _, gid = B.generated()
    plan_bytes = Path(args.plan).read_bytes()
    require(hashlib.sha256(plan_bytes).hexdigest() == args.plan_sha256,
        "Bind the complete literal caller-view plan")
    plan = json.loads(plan_bytes)
    require(plan.get("schema") == PLAN_SCHEMA and plan.get("repository") == REPOSITORY,
        "Use the one explicit R530 caller registration")
    require(same(plan.get("baseline"),R520)
        and same(plan.get("kernel"),receipt(__file__))
        and same(plan.get("original_image_source_plan"),R520_PLAN)
        and plan["output"]["file"] == ADAPTER_NAME,
        "Only the new finite kernel and the exact original caller are registered")
    out = B.inside(args.out,exists=False)
    require(out != B.base and not out.exists() and not comp.is_relative_to(out),
        "Use a fresh own metadata output under the existing namespace")
    out.mkdir()
    value = dict(schema=PLAN_SCHEMA+"-actual-preparation",repository=REPOSITORY,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        source=receipt(__file__),actual_plan=receipt(args.plan),actual_original_caller=receipt(comp/R520["file"]),
        actual_kernel=receipt(__file__),actual_original_image_views=gid,
        actual_original_namespace_start=B.start_id,completed=False,
        actual_generated_source=None,complete_unconfirmed_sources=[plan["output"]],
        scientific_arithmetic_performed=False,old_sources_overwritten=False,
        new_clock_created=False,error=None)
    def persist():
        return B.H.write(out/"result.json",value)
    persist()
    try:
        target = comp/plan["output"]["file"]
        require(not target.exists(),"Never replace an existing original or generated source")
        text = (comp/R520["file"]).read_text(encoding="utf-8")
        for patch in plan["replacements"]:
            require(text.count(patch["before"]) == patch["count"],
                "An exact original caller fragment differs")
            text = text.replace(patch["before"],patch["after"])
        raw = text.encode("utf-8")
        require(same(dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()),plan["output"]),
            "The full generated caller identity differs")
        with target.open("xb") as stream:
            stream.write(raw);stream.flush();os.fsync(stream.fileno())
        value["actual_generated_source"] = receipt(target)
        value["complete_unconfirmed_sources"] = []
        value["completed"] = True
    except BaseException as exc:
        value["error"] = dict(type=type(exc).__name__,message=str(exc),
            complete_traceback=traceback.format_exc())
    rid = persist()
    print(json.dumps(dict(event="R530_actual_owned_caller_source",
        actual_result=rid,completed=value["completed"],error=value["error"],
        complete_unconfirmed_sources=value["complete_unconfirmed_sources"]),ensure_ascii=True),flush=True)
    return 0 if value["completed"] else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command",required=True)
    p = commands.add_parser("materialize")
    for name in ("base","computations","original-plan","plan","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--plan-sha256",required=True)
    return materialize(parser.parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
