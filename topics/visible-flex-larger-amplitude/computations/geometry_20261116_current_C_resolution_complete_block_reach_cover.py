#!/usr/bin/env python3
"""R435: complete hierarchical root-pair organization of the frozen R422 field.

This independent consumer reuses the actual R422 binding, complete curvature
cover, original root cells, phase reduction and unmodified singleton pair run.
It may retire a multiple-pair rectangle only by the original non-strict
distance >= 2*tau alternative, using complete unions of actual closed root
enclosures.  Otherwise it partitions the complete index set; diagonal pairs
are retained and reach the original local/normal/phase alternatives.

No native/BVP gate, field, K, tau, metric result or accepted parent is supplied
by this source.  All geometric arithmetic and module imports are Actions-only.
All ledgers remain owned temporary runner files.  Necessary readback is one
unencoded JSON <= 90000 bytes; overflow is honest transport failure, not a
license to truncate pending blocks or to certify a surface.
Author: OpenAI / ChatGPT geometry agent, 2026-11-16.
"""
from __future__ import annotations

import argparse
from collections import Counter, OrderedDict
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import sys
import time
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R441-current-C-resolution450-complete-hierarchical-root-pair-reach-v1"
BASE = "geometry_20261116_current_C_resolution_complete_reach_cover.py"
BASE_SHA = "745b245eddd27c10522012756a33bd842b3883d918845de49cc2cdacbeed1a05"
LIMIT = 90000


def actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Execute this exact geometric consumer only in the named public Actions")


def receipt(path, root=None):
    path = Path(path)
    size, digest = 0, hashlib.sha256()
    with path.open("rb") as stream:
        for raw in iter(lambda: stream.read(1048576), b""):
            size += len(raw)
            digest.update(raw)
    return dict(file=str(path.relative_to(root)) if root is not None else path.name,
                bytes=size, sha256=digest.hexdigest())


def load_base(directory):
    actions()
    path = (Path(directory)/BASE).resolve()
    row = receipt(path)
    if row["sha256"] != BASE_SHA:
        raise ValueError("The complete original R422 consumer differs")
    name = "_R435_frozen_R422_complete_reach"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError("Missing frozen R422 loader")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(name, None)
        raise
    return module, row


def rank_of(roots, family, i, j):
    """Exactly the original flat rank; never a new ordering or a new universe."""
    A = roots.active_count
    if family == "AA" and 0 <= i <= j < A:
        return i*(2*A-i+1)//2+(j-i)
    if family == "CC" and A <= i <= j < A+2:
        a, b = i-A, j-A
        return roots.AA+a*(5-a)//2+(b-a)
    if family == "AC" and 0 <= i < A <= j < A+2:
        return roots.AA+roots.CC+2*i+(j-A)
    raise ValueError("A block attempted to address a rank outside the original universe")


def block(family, shape, left, right, path):
    left, right = tuple(left), tuple(right)
    if (len(left) != 2 or len(right) != 2 or left[0] >= left[1]
            or right[0] >= right[1] or shape not in ("triangle", "rectangle")):
        raise ValueError("Invalid nonempty index block")
    if shape == "triangle" and (left != right or family not in ("AA", "CC")):
        raise ValueError("A diagonal triangle must retain its identical index interval")
    if shape == "rectangle" and family in ("AA", "CC") and left[1] > right[0]:
        raise ValueError("An unordered rectangular block must be above the diagonal")
    return dict(family=family, shape=shape, left=left, right=right, path=path)


def block_count(item):
    n = item["left"][1]-item["left"][0]
    m = item["right"][1]-item["right"][0]
    return n*(n+1)//2 if item["shape"] == "triangle" else n*m


def block_scope(roots, item):
    a, b = item["left"]
    c, d = item["right"]
    return dict(path=item["path"], family=item["family"], shape=item["shape"],
        left_root_index_half_open=[a, b], right_root_index_half_open=[c, d],
        original_root_pair_count=block_count(item),
        original_flat_rank_min=rank_of(roots, item["family"], a, c),
        original_flat_rank_max=rank_of(roots, item["family"], b-1, d-1),
        min_and_max_are_only_extrema_not_a_contiguous_rank_set=True,
        exact_rank_set="rank_of(family,i,j) for this index rectangle; additionally i<=j in a triangle")


def split_block(item):
    family, path = item["family"], item["path"]
    a, b = item["left"]
    c, d = item["right"]
    if item["shape"] == "triangle":
        if b-a <= 1:
            raise ValueError("A singleton diagonal has no index split")
        m = (a+b)//2
        children = [block(family, "triangle", (a, m), (a, m), path+"/0"),
                    block(family, "rectangle", (a, m), (m, b), path+"/1"),
                    block(family, "triangle", (m, b), (m, b), path+"/2")]
        split = "complete_lower_triangle_cross_rectangle_upper_triangle"
    elif b-a >= d-c and b-a > 1:
        m = (a+b)//2
        children = [block(family, "rectangle", (a, m), (c, d), path+"/0"),
                    block(family, "rectangle", (m, b), (c, d), path+"/1")]
        split = "left_index_interval"
    elif d-c > 1:
        m = (c+d)//2
        children = [block(family, "rectangle", (a, b), (c, m), path+"/0"),
                    block(family, "rectangle", (a, b), (m, d), path+"/1")]
        split = "right_index_interval"
    else:
        raise ValueError("A singleton rectangle has no index split")
    if sum(map(block_count, children)) != block_count(item):
        raise AssertionError("An index split lost or duplicated an original root-pair count")
    return split, children


def initial_blocks(roots):
    A = roots.active_count
    if A < 1 or roots.count != A+2:
        raise ValueError("Use the complete original active universe and both cap roots")
    result = [block("AA", "triangle", (0, A), (0, A), "AA"),
              block("CC", "triangle", (A, A+2), (A, A+2), "CC"),
              block("AC", "rectangle", (0, A), (A, A+2), "AC")]
    if sum(map(block_count, result)) != roots.pair_count:
        raise AssertionError("The initial three blocks differ from the complete R422 universe")
    return result


class OnePairRoots:
    """A one-element iterator view; all actual roots, ranks and bindings stay original."""
    def __init__(self, original, selected):
        self.original, self.selected = original, selected

    def __getattr__(self, name):
        return getattr(self.original, name)

    def pairs(self):
        yield self.selected


def single_pair_type(B):
    class SinglePair(B.PairCover):
        # run/evaluate/phase_test are inherited unmodified.  Only report and
        # pending cease to pretend that a singleton execution visited a prefix
        # of the original flat rank order.
        def __init__(self, args, G, roots, budget, ledger, modules, local, selected, cache):
            super().__init__(args, G, OnePairRoots(roots, selected), budget, ledger, modules, local)
            self.selected = selected
            self.rank = selected[0]
            self.catalog_cache = cache

        def pending(self):
            unstarted = (self.current is None and not self.stack
                         and self.rank == self.selected[0] and self.counts["root_pairs_processed"] == 0)
            initial = None
            if unstarted:
                base = dict(left=self.roots.cell(self.selected[2]), right=self.roots.cell(self.selected[3]),
                    path="", depth=0, spatial_depth=0, chart=None)
                nodes = ([dict(base, chart=c, phase=(Q(-1), Q(1))) for c in ("t", "u")]
                         if self.selected[1] == "AC" else [base])
                initial = [B.node_scope(n, self.G.Cap, self.G.caps.cuff) for n in nodes]
            return dict(original_singleton_rank=self.selected[0],
                current_unretired_original_pair=copy.deepcopy(self.current),
                complete_original_space_phase_frontier=[
                    B.node_scope(n, self.G.Cap, self.G.caps.cuff) for n in reversed(self.stack)],
                original_singleton_not_started=unstarted,
                complete_original_closed_roots_if_unstarted=initial,
                terminal_unpaid_leaves=self.counts["unpaid"],
                terminal_unpaid_addresses="original root_pair_terminal paid=false rows in the complete pair ledger",
                no_flat_rank_prefix_or_suffix_claimed=True)

        def report(self):
            complete = (self.rank == self.selected[0]+1 and self.current is None and not self.stack
                        and self.counts["root_pairs_processed"] == 1)
            return dict(original_rank=self.selected[0], family=self.selected[1],
                left_root=self.selected[2], right_root=self.selected[3],
                singleton_run_completed=complete,
                singleton_complete_pair_paid=complete and self.counts["unpaid"] == 0,
                original_counts=dict(self.counts), pending=self.pending(),
                original_R422_run_evaluate_phase_test_unmodified=True)
    return SinglePair


class UnionBounds:
    """Closed position unions of actual R422 root cells, with a bounded cache.

    A failed or interrupted union never pays a root pair.  The enclosing block
    stays unretired while this object computes, including every child whose
    position enclosure has not yet been attempted.
    """
    def __init__(self, B, args, G, roots, budget, ledger, kernel):
        self.R, self.args, self.G, self.roots = B, args, G, roots
        self.budget, self.ledger, self.kernel = budget, ledger, kernel
        self.cache = OrderedDict()
        self.root_attempts = self.nodes_completed = self.cache_hits = 0
        self.active_stack = []
        self.active_request = None

    def remember(self, key, row):
        ordinal = self.ledger.rows
        self.ledger.add(dict(kind="complete_root_interval_position_union", **row))
        row = dict(row, union_ledger_ordinal=ordinal)
        self.nodes_completed += 1
        self.cache[key] = row
        self.cache.move_to_end(key)
        while len(self.cache) > self.args.block_cache_entries:
            self.cache.popitem(last=False)
        return row

    def range(self, interval):
        self.active_request = list(interval)
        self.active_stack = []
        try:
            row = self._range(tuple(interval))
        except (ArithmeticError, ValueError) as exc:
            # A complete description of the failed work is recorded, but no
            # geometric enclosure is asserted.  The enclosing pair block is
            # still present and will be split by the caller.  Stop and I/O
            # exceptions are not caught here and retain the live frames.
            row = self.remember(tuple(interval), dict(root_index_half_open=list(interval),
                complete_original_root_count=interval[1]-interval[0], available=False, empty=None,
                position_box=None, center=None, radius=None, normal=None, normal_radius=None,
                original_union_error=dict(type=type(exc).__name__, message=str(exc)),
                complete_unreturned_union_frames=copy.deepcopy(self.active_stack),
                geometric_failure_inferred=False))
            self.active_stack = []
        self.active_request = None
        if self.active_stack:
            raise AssertionError("A completed position union retained an unfinished frame")
        return row

    def _range(self, interval):
        self.budget.check()
        a, b = interval
        if not 0 <= a < b <= self.roots.count or a < self.roots.active_count < b:
            raise ValueError("A union must belong to the common-moving active set or the fixed caps")
        if interval in self.cache:
            self.cache_hits += 1
            self.cache.move_to_end(interval)
            return self.cache[interval]
        self.active_stack.append(dict(root_index_half_open=[a, b], stage="started"))
        root_count = b-a
        source = {}
        available, empty, box = True, False, None
        if root_count == 1:
            self.budget.check()
            if self.root_attempts >= self.args.max_union_cells:
                raise self.R.Stop("declared_multicell_root_enclosure_attempt_budget")
            self.root_attempts += 1
            self.active_stack[-1]["stage"] = "actual_original_root_enclosure"
            try:
                data = self.G.data(self.roots.cell(a), 0, curvature=False)
                source = dict(original_root_index=a, original_spatial_id=data["spatial_id"])
                empty = bool(data["empty"])
                if not empty:
                    box = tuple(tuple(Q(v) for v in pair) for pair in data["position_box"])
            except (ArithmeticError, ValueError) as exc:
                available = False
                source = dict(original_root_index=a,
                    original_enclosure_error=dict(type=type(exc).__name__, message=str(exc)),
                    geometric_failure_inferred=False)
        else:
            m = (a+b)//2
            self.active_stack[-1]["stage"] = "left_complete_child"
            left = self._range((a, m))
            self.active_stack[-1]["stage"] = "right_complete_child"
            right = self._range((m, b))
            source = dict(complete_children=[
                dict(root_index_half_open=left["root_index_half_open"],
                     union_ledger_ordinal=left["union_ledger_ordinal"]),
                dict(root_index_half_open=right["root_index_half_open"],
                     union_ledger_ordinal=right["union_ledger_ordinal"])])
            available = bool(left["available"] and right["available"])
            if available:
                empty = bool(left["empty"] and right["empty"])
                children = [x for x in (left, right) if not x["empty"]]
                if children:
                    box = tuple((min(x["position_box"][k][0] for x in children),
                                 max(x["position_box"][k][1] for x in children)) for k in range(3))
        center = radius = None
        if available and not empty:
            if box is None or len(box) != 3 or any(lo > hi for lo, hi in box):
                raise ValueError("A complete root union has no valid three-coordinate enclosure")
            center = tuple((lo+hi)/2 for lo, hi in box)
            radius = self.kernel.sqrt_upper(sum(((hi-lo)/2)**2 for lo, hi in box), self.args.sqrt_bits)
        row = dict(root_index_half_open=[a, b], complete_original_root_count=root_count,
            available=available, empty=empty if available else None,
            position_box=box, center=center, radius=radius,
            normal=None, normal_radius=None,
            motion="common-active-rotation" if b <= self.roots.active_count else "both-caps-fixed",
            closed_cells_and_all_coordinate_extrema_retained=True,
            no_normal_ball_averaging_or_new_normal_gate=True, **source)
        row = self.remember(interval, row)
        self.active_stack.pop()
        return row

    def report(self):
        return dict(actual_original_root_enclosure_attempts=self.root_attempts,
            completed_union_nodes=self.nodes_completed, cache_hits=self.cache_hits,
            retained_cache_entries=len(self.cache),
            current_unfinished_union_request=copy.deepcopy(self.active_request),
            complete_unreturned_union_frames=copy.deepcopy(self.active_stack),
            interrupted_union_pays_no_pair=True)


class BlockPairCover:
    def __init__(self, B, args, G, roots, budget, pair_ledger, block_ledger, union_ledger, modules, local):
        self.R, self.args, self.G, self.roots, self.budget = B, args, G, roots, budget
        self.pair_ledger, self.ledger, self.modules, self.local = pair_ledger, block_ledger, modules, local
        self.kernel = modules[B.KERNEL]
        self.union = UnionBounds(B, args, G, roots, budget, union_ledger, self.kernel)
        self.SinglePair = single_pair_type(B)
        self.catalog_cache = OrderedDict()
        self.frontier = list(reversed(initial_blocks(roots)))
        self.active_leaf = None
        self.block_attempts = 0
        self.counts = Counter()
        self.families = {name: Counter() for name in ("AA", "CC", "AC")}

    def bump(self, family, key, number=1):
        self.counts[key] += number
        self.families[family][key] += number

    def split(self, item, reason, attempt=None):
        how, children = split_block(item)
        self.ledger.add(dict(kind="complete_original_rank_block_split",
            block=block_scope(self.roots, item), split=how, reason=reason,
            attempted_original_distance=attempt,
            complete_children=[block_scope(self.roots, child) for child in children],
            original_index_sets_disjoint_and_exhaustive=True,
            closed_spatial_boundary_overlap_not_removed=True))
        self.frontier.pop()
        self.frontier.extend(reversed(children))
        self.bump(item["family"], "block_splits")

    def attempt_distance(self, item):
        left, right = self.union.range(item["left"]), self.union.range(item["right"])
        common = dict(union_ledger_ordinals=[left["union_ledger_ordinal"], right["union_ledger_ordinal"]],
            complete_left_root_count=left["complete_original_root_count"],
            complete_right_root_count=right["complete_original_root_count"],
            original_root_pair_count=block_count(item), no_phase_sample_used=True)
        if not (left["available"] and right["available"]):
            return dict(certified=False, owner=None,
                reason="a_complete_multicell_position_union_is_unavailable", **common)
        if left["empty"] or right["empty"]:
            # Root disks are normally nonempty.  Even if the inherited empty
            # proof applies, this layer pays only distance, so keep that
            # responsibility for the original singleton owner.
            return dict(certified=False, owner=None,
                reason="empty_union_retained_for_original_singleton_empty_owner", **common)
        if item["family"] == "AC":
            original = self.R.phase_distance((left, right), self.kernel, self.args.sqrt_bits, self.G.tau)
            paid = original["certified"]
            motion = "same actual R248 active inverse transport and entire common rotation; complete cap union fixed"
        else:
            original = self.R.static_gates((left, right), self.kernel, self.args.sqrt_bits, self.G.tau)
            paid = original["gates"]["distance"]
            if original["gates"]["left"] or original["gates"]["right"] or original["gates"]["joint"]:
                raise AssertionError("A position-only union must not invoke a normal alternative")
            motion = "both active unions share one rigid rotation" if item["family"] == "AA" else "both cap unions fixed"
        return dict(certified=bool(paid), owner="original_distance_at_least_2tau_on_complete_unions",
            original_distance_record=original, simultaneous_motion=motion,
            equality_retained=True, normal_alternatives_used_at_block_level=False, **common)

    def run_singleton(self, item):
        i, j = item["left"][0], item["right"][0]
        rank = rank_of(self.roots, item["family"], i, j)
        selected = (rank, item["family"], i, j)
        self.active_leaf = self.SinglePair(self.args, self.G, self.roots, self.budget,
            self.pair_ledger, self.modules, self.local, selected, self.catalog_cache)
        self.ledger.add(dict(kind="singleton_block_original_R422_delegation",
            block=block_scope(self.roots, item), original_rank=rank,
            exact_original_run_evaluate_phase_test_reused=True))
        # The original run owns every spatial/phase split and every original
        # gate.  A nonzero selected rank is not treated as a completed prefix.
        report = self.active_leaf.run()
        if not report["singleton_run_completed"]:
            raise RuntimeError("The original singleton run returned without closing its responsibility")
        paid = bool(report["singleton_complete_pair_paid"])
        self.ledger.add(dict(kind="singleton_block_retired_after_original_run",
            block=block_scope(self.roots, item), original_singleton=report, paid=paid))
        self.bump(item["family"], "root_pairs_retired")
        self.bump(item["family"], "singleton_root_pairs_retired")
        self.bump(item["family"], "singleton_root_pairs_paid", int(paid))
        self.bump(item["family"], "root_pairs_paid", int(paid))
        self.bump(item["family"], "original_terminal_unpaid_leaves", self.active_leaf.counts["unpaid"])
        self.bump(item["family"], "singleton_unpaid_root_pairs", int(not paid))
        self.frontier.pop()
        self.active_leaf = None

    def run(self):
        while self.frontier:
            self.budget.check()
            if self.block_attempts >= self.args.max_block_nodes:
                raise self.R.Stop("declared_hierarchical_block_attempt_budget")
            item = self.frontier[-1]  # Never pop before a complete retirement/split record.
            self.block_attempts += 1
            scope = block_scope(self.roots, item)
            # Preserve the old max_pairs meaning: it is an admissible original
            # flat-rank prefix, NOT a licence to retire a block crossing it.
            # This DFS need not visit that prefix in order; all other blocks
            # remain explicit if its first inadmissible block stops the run.
            if scope["original_flat_rank_min"] >= self.args.max_pairs:
                raise self.R.Stop("original_complete_root_pair_rank_budget")
            if scope["original_flat_rank_max"] >= self.args.max_pairs:
                self.split(item, "preserve_original_flat_rank_resource_boundary")
                continue
            if block_count(item) == 1:
                self.run_singleton(item)
                continue
            if item["shape"] == "triangle":
                # An identical union on both sides has centre distance zero.
                # For positive tau it cannot pay all included diagonal pairs
                # by the only permitted block gate.  Retain both triangles.
                self.split(item, "same_union_distance_cannot_pay_positive_tau_diagonal_responsibilities")
                continue
            try:
                attempted = self.attempt_distance(item)
            except (ArithmeticError, ValueError) as exc:
                attempted = dict(certified=False, owner=None,
                    reason="actual_complete_union_distance_unresolved",
                    exception=dict(type=type(exc).__name__, message=str(exc)),
                    geometric_failure_inferred=False)
            if not attempted["certified"]:
                self.split(item, "original_block_distance_not_proved", attempted)
                continue
            number = block_count(item)
            self.ledger.add(dict(kind="complete_original_rank_block_paid",
                block=scope, original_distance=attempted,
                all_original_ranks_in_this_index_set_paid=True,
                no_singleton_normal_or_local_gate_claimed_for_the_block=True))
            self.bump(item["family"], "root_pairs_retired", number)
            self.bump(item["family"], "root_pairs_paid", number)
            self.bump(item["family"], "block_paid_root_pairs", number)
            self.bump(item["family"], "distance_paid_blocks")
            self.frontier.pop()
        return self.report()

    def pending(self):
        return dict(complete_unretired_block_frontier=[block_scope(self.roots, x) for x in reversed(self.frontier)],
            unretired_root_pair_responsibility_count=sum(map(block_count, self.frontier)),
            current_original_singleton=None if self.active_leaf is None else self.active_leaf.report(),
            current_union_work=self.union.report(),
            retired_terminal_unpaid_original_leaves=self.counts["original_terminal_unpaid_leaves"],
            retired_unpaid_original_root_pairs=self.counts["singleton_unpaid_root_pairs"],
            terminal_unpaid_addresses="all original root_pair_terminal paid=false records, with actual rank and closed space/phase scope",
            incomplete_current_singleton_is_also_kept_as_its_whole_root_block=True,
            original_rank_prefix_or_suffix_not_inferred_from_DFS_order=True,
            no_same_point_product_cuff_pair_reflection_cap_or_phase_omitted=True)

    def report(self):
        complete = not self.frontier and self.active_leaf is None
        accounted = self.counts["root_pairs_retired"]+sum(map(block_count, self.frontier))
        consistent = accounted == self.roots.pair_count
        if not consistent:
            raise AssertionError("Retired blocks and unretired frontier do not preserve the original universe")
        paid = complete and self.counts["root_pairs_paid"] == self.roots.pair_count
        return dict(complete_root_pair_cover=complete,
            complete_pair_responsibility_paid=paid,
            planned_original_root_pairs=self.roots.pair_count,
            retired_original_root_pairs=self.counts["root_pairs_retired"],
            complete_index_count_invariant_preserved=consistent,
            hierarchy_block_attempts=self.block_attempts,
            original_singleton_space_phase_node_attempts=self.budget.pair_attempts,
            counts=dict(self.counts), by_family={name:dict(row) for name, row in self.families.items()},
            union_bounds=self.union.report(),
            old_flat_root_pair_rank_and_cells_unchanged=True,
            block_payment_uses_only_original_non_strict_distance=True,
            singleton_original_four_gate_OR_and_R282_unchanged=True,
            AA_and_CC_use_no_one_endpoint_phase_rotation=True,
            AC_entire_circle_at_block_and_both_closed_RP1_roots_at_leaf=True,
            terminal_depth_or_budget_failure_not_a_geometric_refutation=True,
            pending=self.pending())


def validate_resources(B, args):
    B.validate(args)
    if min(args.max_block_nodes, args.max_union_cells, args.block_cache_entries) < 1:
        raise ValueError("Declare positive block, original-root enclosure and cache resource limits")
    temporary = os.environ.get("RUNNER_TEMP")
    if not temporary:
        raise ValueError("The caller must provide the actual owned RUNNER_TEMP namespace")
    temp, out = Path(temporary).resolve(), args.out.resolve()
    if out == temp or temp not in out.parents:
        raise ValueError("Use a fresh owned child of the actual RUNNER_TEMP")
    inputs = [args.computations, args.directory, args.cuff_atlas]
    inputs += [p for p in (args.checkpoint_directory, args.proof_directory) if p is not None]
    for path in inputs:
        actual = Path(path).resolve()
        if actual == out or out in actual.parents:
            raise ValueError("The owned output must not contain an original input")


def necessary_summary(B, result, result_receipt):
    summary = {key:copy.deepcopy(result.get(key)) for key in (
        "schema", "source", "run_id", "source_commit", "stage", "error", "resource_partial",
        "resource_reason", "external_signal", "input_binding", "parameters", "universe_counts",
        "unstarted_scope", "members", "ledgers", "accurate_family_embedding_and_reach_certified",
        "accurate_family_reach_lower", "K_times_tau", "curvature_radius_gate",
        "README_reach_fraction_paid", "README_D_definition", "diameter", "elapsed_seconds")}
    summary["schema"] = SCHEMA+"-necessary-summary"
    summary["result"] = result_receipt
    summary["pairs"] = copy.deepcopy(result["pairs"])
    curvature = result["curvature"]
    if curvature is not None:
        summary["curvature"] = {key:copy.deepcopy(curvature.get(key)) for key in (
            "all_original_closed_roots_accounted_for", "processed_original_roots", "planned_original_roots",
            "counts", "actual_cell_attempts", "full_closed_immersion_proved", "full_closed_K_proved",
            "K", "full_first_jet_path_envelopes", "whole_phase_curvature_paid", "pending")}
        summary["curvature"]["complete_meridian_envelope_identity"] = B.identity(curvature["meridian_path_envelope"])
    else:
        summary["curvature"] = None
    summary["readback_scope"] = dict(
        complete_current_block_frontier_and_original_singleton_frontier_returned=True,
        all_retired_block_and_original_leaf_ledgers_hashed_not_all_rows_returned=True,
        all_union_position_coordinates_exist_in_temporary_ledgers_not_returned_raw=True,
        all_terminal_unpaid_leaf_addresses_preserved_in_original_ledger=True,
        complete_necessary_scalar_scope_in_this_one_document=True,
        no_metric_held_deltaE_or_actual_native_certificate_created=True,
        no_performance_convergence_or_success_promise=True,
        no_raw_split_encoding_artifact_upload_or_cleanup=True)
    return summary


def produce(args):
    actions()
    B, base_receipt = load_base(args.computations)
    validate_resources(B, args)
    args.out.mkdir(parents=True, exist_ok=False)
    large = args.out/"large-arrays"
    large.mkdir()
    budget = B.Budget(args)
    previous_handlers = {}
    for number in (signal.SIGTERM, signal.SIGINT):
        previous_handlers[number] = signal.getsignal(number)
        signal.signal(number, budget.signal)
    old_precision = saved_runtime_context = None
    modules, sources, members, ledgers = {}, {BASE:base_receipt}, {}, {}
    current = G = roots = cover = pairs = None
    spatial = curvature_ledger = pair_ledger = block_ledger = union_ledger = None
    curvature = pair_report = diameter = None
    error = stop_reason = binding_receipt = None
    stage = "original_input_binding_and_actual_source_load"
    try:
        budget.check()
        for name in B.SOURCE_PINS:
            if name == B.ACTIVE:
                row = B.receipt(args.computations/name)
                if row["sha256"] != B.SOURCE_PINS[name]:
                    raise ValueError("The exact six-jet helper differs")
                sources[name] = row
            else:
                modules[name], sources[name] = B.load(args.computations, name)
        from flint import ctx
        old_precision, saved_runtime_context = ctx.prec, ctx
        actual_args = SimpleNamespace(**vars(args))
        actual_args.interval_bits = args.interval_bits+max(args.curvature_max_depth, args.pair_max_depth)
        current = modules[B.CUT].load_accurate_cut_field(actual_args)
        M = current.Active
        if (Path(M.__file__).resolve() != (args.computations/B.ACTIVE).resolve()
                or B.receipt(M.__file__)["sha256"] != B.SOURCE_PINS[B.ACTIVE]):
            raise ValueError("The actual current field does not own the pinned six-jet helper")
        M.ctx.prec = args.interval_bits
        atlas, atlas_receipt = modules[B.CUFF].bound_json(args.cuff_atlas, args.cuff_atlas_sha256)
        attachment = modules[B.CUFF].bind_loaded_shared_bundle(current.source_bundle, atlas)
        caps = modules[B.CAP].bind_loaded_shared_bundle(current.source_bundle, atlas, attachment, args.computations)
        if caps.cuff != current.field.cuff or caps.height != current.field.B.nodal[0][0]:
            raise ValueError("Current active and fixed-cap cuff data differ")
        sources[Path(__file__).name] = B.receipt(__file__)
        spatial = B.Ledger(large/"complete-spatial-enclosures.jsonl.gz", args.out)
        curvature_ledger = B.Ledger(large/"complete-curvature-cover.jsonl.gz", args.out)
        pair_ledger = B.Ledger(large/"complete-original-singleton-space-phase-cover.jsonl.gz", args.out)
        block_ledger = B.Ledger(large/"complete-original-rank-block-cover.jsonl.gz", args.out)
        union_ledger = B.Ledger(large/"complete-root-interval-position-unions.jsonl.gz", args.out)
        G = B.CurrentGeometry(args, modules, current, caps, spatial)
        roots = B.Roots(G, args.active_depth)
        members["complete_original_root_universe"] = B.write(large/"complete-original-root-universe.json", roots.describe(), args.out)
        members["complete_initial_pair_blocks"] = B.write(large/"complete-initial-pair-blocks.json",
            dict(blocks=[block_scope(roots, x) for x in initial_blocks(roots)],
                original_rank_formula="AA:i(2A-i+1)/2+j-i; CC:AA+a(5-a)/2+b-a; AC:AA+3+2i+j-A",
                no_flat_rank_interval_substituted_for_an_index_block=True), args.out)
        budget.check()
        local = modules[B.LOCAL].CuffOwner(G.field, caps.markers, M, modules[B.KERNEL],
            sqrt_bits=args.sqrt_bits, max_constant_levels=args.max_constant_levels)
        members["actual_collar_coefficients"] = B.write(large/"actual-complete-collar-coefficients.json", local.coefficient_payload, args.out)
        members["actual_cuff_constants"] = B.write(large/"actual-cuff-local-constants.json", local.report(), args.out)
        members["same_accurate_cut_DAG"] = B.write(large/"same-accurate-cut-DAG.json", current.model.definition, args.out)
        members["complete_original_target_binding"] = B.write(large/"complete-original-ten-target-binding.json", current.target.binding, args.out)
        members["current_cap_binding"] = B.write(large/"current-complete-cap-binding.json", caps.describe(), args.out)
        binding = dict(schema=SCHEMA+"-input-binding", source=sources[Path(__file__).name],
            original_R422_source=base_receipt, direct_sources=sources,
            actual_R416_binding=copy.deepcopy(current.binding),
            original_seven_tuple_binding=copy.deepcopy(current.source_bundle[-1]),
            R413_atlas=atlas_receipt, R413_attachment=copy.deepcopy(attachment),
            R417_full_marker_and_graph_binding_identity=B.identity(caps.describe()),
            genuine_accepted450_checkpoint=copy.deepcopy(current.binding["actual_450_checkpoint"]),
            original_ten_target_binding_identity=B.identity(current.target.binding),
            proposed_constants=dict(K=args.curvature_upper, tau=args.target_reach),
            constants_are_explicit_recipe_inputs_not_chosen_by_this_consumer=True,
            original_K_and_tau_not_tuned_from_an_output=True,
            R418_relative_metric_or_complete_E_query_result_required=False,
            old_source_bundle_A_used_only_for_original_provenance_not_new_patch_evaluation=True,
            phase_family="R248 actual material inverse shift and common active rotation; both marked Cartesian caps fixed",
            all_real_phases_covered_not_only_t_endpoints=True,
            original_mean_Nyquist_FFT_Phi_and_shared_B_retained=True,
            original_scalar_target_not_replaced_by_Bprime_or_induced_metric=True,
            complete_original_R422_rank_universe_retained=True,
            block_gate_only_original_non_strict_distance=True,
            original_singleton_run_evaluate_phase_test_unmodified=True,
            old_static_R24_source_and_results_unchanged_and_not_relabelled=True,
            no_new_native_or_BVP_acceptance_gate=True, members=copy.deepcopy(members))
        binding_receipt = B.write(args.out/"input-binding.json", binding, args.out)
        image = modules[B.DIAMETER].ImageBounds(modules[B.KERNEL].sqrt_upper, args.sqrt_bits, "original_marked_image")
        cover = B.CurvatureCover(G, roots, budget, curvature_ledger, image)
        pairs = BlockPairCover(B, args, G, roots, budget, pair_ledger, block_ledger, union_ledger, modules, local)
        stage = "original_complete_closed_curvature_and_path_envelopes"
        curvature = cover.run()
        stage = "complete_hierarchical_AA_CC_AC_pair_cover"
        pair_report = pairs.run()
        stage = "complete_attempt_finished"
    except B.Stop as exc:
        stop_reason = str(exc)
    except BaseException as exc:
        error = dict(type=type(exc).__name__, message=str(exc), stage=stage,
            geometric_failure_or_native_rejection_inferred=False)
    finally:
        if cover is not None:
            try:
                curvature = cover.report()
                diameter = curvature["diameter"]
            except BaseException as exc:
                if error is None:
                    error = dict(type=type(exc).__name__, message=str(exc), stage="curvature_report")
        if pairs is not None:
            try:
                pair_report = pairs.report()
            except BaseException as exc:
                pair_report = dict(complete_pair_responsibility_paid=False,
                    report_error=dict(type=type(exc).__name__, message=str(exc)),
                    pending=pairs.pending(),
                    no_complete_index_accounting_or_reach_claimed_after_report_error=True)
                if error is None:
                    error = dict(type=type(exc).__name__, message=str(exc), stage="block_pair_report")
        for name, ledger in (("complete_spatial_enclosures", spatial),
                             ("complete_curvature_cover", curvature_ledger),
                             ("complete_original_singleton_space_phase_cover", pair_ledger),
                             ("complete_original_rank_block_cover", block_ledger),
                             ("complete_root_interval_position_unions", union_ledger)):
            if ledger is not None:
                try:
                    ledgers[name] = ledger.close()
                except BaseException as exc:
                    ledgers[name] = dict(file=str(ledger.path.relative_to(args.out)),
                        closure_error=dict(type=type(exc).__name__, message=str(exc)), complete_bytes_not_claimed=True)
                    if error is None:
                        error = dict(type=type(exc).__name__, message=str(exc), stage="ledger_close")
        if current is not None:
            try:
                members["actual_used_complete_field_identity"] = B.write(large/"actual-used-complete-field-identity.json", current.expression_identity(), args.out)
            except BaseException as exc:
                if error is None:
                    error = dict(type=type(exc).__name__, message=str(exc), stage="final_field_identity")
        if saved_runtime_context is not None and old_precision is not None:
            saved_runtime_context.prec = old_precision
        for number, handler in previous_handlers.items():
            signal.signal(number, handler)
    K, tau = B.rational(args.curvature_upper), B.rational(args.target_reach)
    curvature_paid = curvature is not None and curvature["full_closed_K_proved"] and curvature["full_closed_immersion_proved"]
    pair_paid = pair_report is not None and pair_report["complete_pair_responsibility_paid"]
    reached = error is None and stop_reason is None and curvature_paid and pair_paid and K*tau <= 1
    D = None if diameter is None else diameter["phase_zero_complete_image_diameter_upper"]
    ratio_paid = reached and D is not None and tau >= Q(3, 100)*Q(D)
    counts = None if roots is None else dict(active_cells=roots.active_count, cap_roots=2,
        AA=roots.AA, CC=roots.CC, AC=roots.AC, all_original_root_pairs=roots.pair_count,
        full_universe=members.get("complete_original_root_universe"))
    result = dict(schema=SCHEMA, source=B.receipt(__file__),
        run_id=os.environ.get("GITHUB_RUN_ID"), source_commit=os.environ.get("GITHUB_SHA"),
        stage=stage, error=error, resource_partial=stop_reason is not None,
        resource_reason=stop_reason, external_signal=budget.requested_signal,
        input_binding=binding_receipt, members=members, ledgers=ledgers, universe_counts=counts,
        unstarted_scope=dict(input_binding_incomplete=binding_receipt is None,
            all_closed_field_and_pair_responsibility_unbound=roots is None,
            curvature_root_suffix=[0, roots.count] if roots is not None and cover is None else None,
            complete_original_pair_blocks=[block_scope(roots, x) for x in initial_blocks(roots)]
                if roots is not None and pairs is None else None),
        parameters={key:getattr(args, key) for key in (
            "curvature_upper", "target_reach", "active_depth", "curvature_max_depth", "pair_max_depth",
            "interval_bits", "sqrt_bits", "max_cells", "max_pair_nodes", "max_pairs", "cache_entries",
            "max_constant_levels", "budget_seconds", "free_bytes_reserve", "max_block_nodes",
            "max_union_cells", "block_cache_entries")},
        curvature=curvature, pairs=pair_report, diameter=diameter,
        accurate_family_embedding_and_reach_certified=bool(reached),
        accurate_family_reach_lower=str(tau) if reached else None,
        K_times_tau=str(K*tau), curvature_radius_gate=K*tau <= 1,
        original_K_and_tau_not_reselected=True, README_reach_fraction_paid=bool(ratio_paid),
        README_D_definition="diameter of the entire marked closed F_0 image",
        original_static_base_R24_route_unchanged_and_not_assumed_paid=True,
        original_native_or_BVP_acceptance_changed=False,
        remaining_original_responsibilities=[
            "Every unpaid original curvature/space-phase leaf and every unretired index block",
            "The same original accurate target full-domain relative metric requirement",
            "Held-set interior/diameter, whole-image hold and reflection-inclusive Euclidean noncongruence",
            "Original numerical-shadow/RK-trajectory/new-exact-field comparisons",
            "All original final standards and subsequent same-g refinement"],
        output_policy="Owned RUNNER_TEMP ledgers only; no cleanup, artifacts, raw split or encoded transport",
        full_ledgers_not_claimed_as_locally_recomputed_or_returned_raw=True,
        worst_case_quadratic_or_worse_work_and_no_speedup_promise=True,
        elapsed_seconds=time.monotonic()-budget.start, task_completed=False)
    result_receipt = B.write(args.out/"result.json", result, args.out)
    summary = necessary_summary(B, result, result_receipt)
    raw = B.canonical(summary)
    if len(raw) > LIMIT:
        print(json.dumps(dict(schema=SCHEMA+"-summary-over-budget", attempted_bytes=len(raw),
            attempted_sha256=B.sha(raw), result=result_receipt,
            complete_necessary_readback=False, outputs_not_deleted=True), separators=(",", ":")), flush=True)
        return 70
    summary_receipt = B.write(args.out/"necessary-summary.json", summary, args.out)
    print("BEGIN_R435_CURRENT_C_BLOCK_REACH_SUMMARY", flush=True)
    print(raw.decode(), end="", flush=True)
    print("END_R435_CURRENT_C_BLOCK_REACH_SUMMARY", flush=True)
    print(json.dumps(dict(event="R435-necessary-summary-identity", **summary_receipt), separators=(",", ":")), flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as stream:
            stream.write("closed_reach_summary="+str(args.out/"necessary-summary.json")+"\n")
            stream.write("closed_reach_summary_bytes="+str(summary_receipt["bytes"])+"\n")
            stream.write("closed_reach_summary_sha256="+summary_receipt["sha256"]+"\n")
    if budget.requested_signal is not None:
        return 128+budget.requested_signal
    return 0 if error is None else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations", type=Path, default=HERE)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--result-sha256", required=True)
    parser.add_argument("--checkpoint-directory", type=Path)
    parser.add_argument("--proof-directory", type=Path)
    parser.add_argument("--cuff-atlas", type=Path, required=True)
    parser.add_argument("--cuff-atlas-sha256", required=True)
    parser.add_argument("--curvature-upper", required=True)
    parser.add_argument("--target-reach", required=True)
    parser.add_argument("--active-depth", type=int, required=True)
    parser.add_argument("--curvature-max-depth", type=int, required=True)
    parser.add_argument("--pair-max-depth", type=int, required=True)
    parser.add_argument("--interval-bits", type=int, required=True)
    parser.add_argument("--sqrt-bits", type=int, required=True)
    parser.add_argument("--max-cells", type=int, required=True)
    parser.add_argument("--max-pair-nodes", type=int, required=True)
    parser.add_argument("--max-pairs", type=int, required=True)
    parser.add_argument("--cache-entries", type=int, default=32)
    parser.add_argument("--max-constant-levels", type=int, default=32)
    parser.add_argument("--max-block-nodes", type=int, required=True)
    parser.add_argument("--max-union-cells", type=int, required=True)
    parser.add_argument("--block-cache-entries", type=int, required=True)
    parser.add_argument("--budget-seconds", type=float, required=True)
    parser.add_argument("--free-bytes-reserve", type=int, default=2147483648)
    parser.add_argument("--out", type=Path, required=True)
    return produce(parser.parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
