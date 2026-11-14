#!/usr/bin/env python3
"""Resume the original complete first-symbol prefix without reintegration.

Reuse the actual2838 accepted strict cells and both directed root Newton
steps from public run43589646508. Allocate the remaining width over its
actual remaining cells. When a cached point's derivative floor would
consume that budget, evaluate only that new strict midpoint with the
same complete intrinsic Arb provider; retain the original whole-cell
sixth-derivative bound. No scalar cover or completed integral is rerun.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import math
import os
from pathlib import Path
import time

from flint import arb, arb_series, ctx

from fourfold_codazzi_current_first_symbol_finite_part import (
    Consumer, CANDIDATE, CENTRE, NU, N, actual_width, angular_moments)
from fourfold_codazzi_phase_scalar_cache_jets import read
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha


ORIGINAL_SOURCE = "c866d7d0f75a36d969d291c4379be34df1b1634a5234875d40819baf555c9a7f"
ORIGINAL_PREFIX = "5167e64ff6076e0100fa1c643b7168ce889b2fe4f6dab034631ce8d7115f0e1d"
ORIGINAL_COMMIT = "409ca5fdf95b9b9d7eda5eee7c6770698869c24b"
ORIGINAL_RUN = "43589646508"
ORIGINAL_STOP = Fraction(136414032713052333, 576460752303423488)


class ResumeConsumer(Consumer):
    def __init__(self, args):
        if sha(Path(__file__).with_name("fourfold_codazzi_current_first_symbol_finite_part.py")) != ORIGINAL_SOURCE:
            raise ValueError("the original exact integrator changed")
        if sha(args.resume) != ORIGINAL_PREFIX:
            raise ValueError("the actual failed prefix changed")
        original = read(args.resume)
        if (original["source_sha256"] != ORIGINAL_SOURCE
                or original["public_run_id"] != ORIGINAL_RUN
                or original["candidate_sha256"] != CANDIDATE
                or original["continuous_centre_definition_sha256"] != CENTRE
                or original["complete"]
                or original["finite_part_enclosure_complete"]
                or original["stage"] != "failed-original-prefix-preserved"
                or original["accepted_strict_rows"] != 2838
                or len(original["rows"]) != 2838
                or Fraction(original["exact_completed_strict_prefix"]) != ORIGINAL_STOP
                or original["exact_nu"] != str(NU)
                or original["explicit_family_parameter_delta"] != "0"):
            raise ValueError("a different scientific prefix or failure was supplied")
        super().__init__(args)
        if (original["exact_strict_cut"] != str(self.cut)
                or original["exact_root_collar_gap_from_original_lower"] != str(args.cut_gap)
                or original["requested_interval_width"] != str(args.width_goal)):
            raise ValueError("resumption must retain the same exact cut and whole target")
        cursor = Fraction(0)
        aggregate_check = arb(0)
        cover_shas = {g["sha256"] for g in self.cover["germs"]}
        for row in original["rows"]:
            left, right = map(Fraction, row["interval"])
            piece = row["actual_candidate_piece"]
            if (left != cursor or not left < right
                    or not self.nodes[piece] <= left < right <= self.nodes[piece+1]
                    or row["scalar_native_sha256"] not in cover_shas):
                raise ValueError("the original accepted partition is incomplete")
            term = box_from_record(row["complete_signed_integral"])
            if not term.is_finite():
                raise ValueError("an original accepted integral is not finite")
            aggregate_check += term
            cursor = right
        aggregate = box_from_record(original["completed_strict_integral"])
        if cursor != ORIGINAL_STOP or not aggregate.overlaps(aggregate_check):
            raise ValueError("the original complete aggregate and its cells disagree")
        oldlo, oldhi = map(Fraction, original["original_unique_root_enclosure"])
        lo, hi = map(Fraction, original["actual_eta0_root_enclosure"])
        history = original["root_refinement"]
        if (len(history) != 2 or [str(oldlo),str(oldhi)] != self.root["root_interval"]
                or not oldlo <= lo < hi <= oldhi
                or not hi-lo < Fraction(1,2**args.root_precision_bits)
                or history[-1]["new_interval"] != [str(lo),str(hi)]):
            raise ValueError("the actual complete two-step root certificate changed")
        prior = [oldlo, oldhi]
        for step in history:
            if list(map(Fraction,step["old_interval"])) != prior:
                raise ValueError("the two original root steps are disconnected")
            prior = list(map(Fraction,step["new_interval"]))
        original_scalar_inputs = original["scalar_inputs"]
        for index, item in enumerate(original_scalar_inputs):
            if item["germ_index"] != index or item["sha256"] != self.cover["germs"][index]["sha256"]:
                raise ValueError("the original scalar provenance is not the current exact cover")
        if original_scalar_inputs[-1]["germ_index"] != 167:
            raise ValueError("the actual failing germ changed")
        self.rows = original["rows"]
        self.rejected = []
        self.strict_integral = aggregate
        self.cursor = cursor
        self.root_lo_new, self.root_hi_new = lo, hi
        self.scalar_inputs = [dict(germ_index=x["germ_index"],
            path=str(self.base/self.cover["germs"][x["germ_index"]]["path"]),
            sha256=x["sha256"],original_run=ORIGINAL_RUN)
            for x in original_scalar_inputs]
        self.fresh_points = []
        self.fresh_point_cache = {}
        self.remaining_tasks = []
        self.state.update(kind="current_first_symbol_finite_part_resumed_v2",
            source_sha256=sha(__file__), original_integrator_source_sha256=ORIGINAL_SOURCE,
            original_run_id=ORIGINAL_RUN, original_published_commit=ORIGINAL_COMMIT,
            original_prefix_sha256=ORIGINAL_PREFIX, original_prefix_path=str(args.resume),
            original_failure=original["failure"], original_failure_relabelled_as_success=False,
            original_successful_integral_rows_reused=2838,
            original_successful_integral_rows_recomputed=0,
            original_root_newton_steps_reused=2, original_root_newton_steps_recomputed=0,
            original_unique_root_enclosure=original["original_unique_root_enclosure"],
            actual_eta0_root_enclosure=original["actual_eta0_root_enclosure"],
            root_refinement=history, original_rejected_cells=original["rejected_cells"],
            original_prefix_complete_integral=original["completed_strict_integral"],
            exact_resume_point=str(ORIGINAL_STOP),
            remaining_interval_width_policy="equal allocation over actual remaining original cells; binary subcells split their own allocation",
            original169_scalar_models_recomputed=False,
            only_true_common_root_scalar_jet_evaluations_are_new=False,
            only_budget_needed_strict_midpoints_and_root_finite_part_jets_are_new=True,
            original_whole_cell_sixth_derivative_bounds_reused=True,
            same_true_intrinsic_object_not_a_new_fitted_polynomial=True,
            workflow_event_commit=os.environ.get("GITHUB_SHA"),
            actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"))

    def checkpoint(self, label):
        self.state.update(new_strict_midpoint_scalar_evaluations=len(self.fresh_points),
            new_strict_midpoint_records=self.fresh_points,
            new_root_scalar_evaluations=self.provider.evaluations-len(self.fresh_points))
        if "genuine_root_scalar_evaluations" in self.state:
            self.state["genuine_root_scalar_evaluations"] = self.provider.evaluations-len(self.fresh_points)
        super().checkpoint(label)

    def fresh_strict_point(self, row, scalar_sha, piece, middle):
        key = piece, middle
        if key in self.fresh_point_cache:
            return self.fresh_point_cache[key]
        if len(self.fresh_points) >= self.args.max_fresh_points:
            raise ArithmeticError("the declared new strict-midpoint budget was exhausted")
        values, germ = self.provider.coefficients(middle, middle, NU)
        if list(map(str,germ)) != row["actual_scalar_germ"]:
            raise ValueError("a fresh midpoint belongs to a different intrinsic germ")
        def series(name):
            return arb_series([values[name+(str(j) if j else "")]/math.factorial(j)
                               for j in range(8)],prec=8)
        b, gamma, s, K = (series(name) for name in ("beta","gamma","s","K"))
        if not K[0] < 0:
            raise ArithmeticError("a fresh strict midpoint does not have true negative curvature")
        q = (-K).sqrt()
        states = self.candidate_states(piece,middle,middle,s)
        moments = angular_moments(states)
        eta = -gamma*states[N]
        if not eta[0] > 0 or not q[0] > 0:
            raise ArithmeticError("a fresh complete strict denominator is unresolved")
        h = q.derivative()/(2*q)
        U2, V2, U4, UV, V4, cross = (moments[name] for name in
            ("u2","v2","u4","u2v2","v4","uvphi_minus_vuphi"))
        square = 1+2*U2+2*q*q*V2+U4-2*q*q*UV+q**4*V4
        Xi = (h*h+2*h*b*(1+U2+q*q*V2)+b*b*square)/(eta*q)-2*b*q*cross
        if Xi.prec < 7 or any(not Xi[j].is_finite() for j in range(7)):
            raise ArithmeticError("a fresh strict midpoint has incomplete true jets")
        self.fresh_points.append(dict(exact_point=str(middle),actual_candidate_piece=piece,
            original_scalar_native_sha256=scalar_sha,actual_scalar_germ=list(map(str,germ)),
            complete_intrinsic_jets={name:[record(values[name+(str(j) if j else "")])
                for j in range(8)] for name in ("beta","gamma","s","K")},
            complete_normalized_Xi_jets=[record(Xi[j]) for j in range(7)],
            complete_intrinsic_provider_details=self.provider.last_details))
        self.fresh_point_cache[key] = Xi
        return Xi

    def integrate_budgeted_cell(self, row, scalar_sha, piece, left, right, allocation, depth):
        middle = (left+right)/2
        point = super().strict_jets(row,piece,middle,middle)
        whole = super().strict_jets(row,piece,left,right)
        h = exact_arb((right-left)/2)
        central = sum((2*point[j]*h**(j+1)/(j+1) for j in (0,2,4)),arb(0))
        old_point_width = actual_width(central)
        fresh = bool(old_point_width > exact_arb(allocation)/4)
        if fresh:
            point = self.fresh_strict_point(row,scalar_sha,piece,middle)
            central = sum((2*point[j]*h**(j+1)/(j+1) for j in (0,2,4)),arb(0))
        remainder = (2*abs(whole[6])*h**7/7).upper()
        value = central+arb(0,remainder)
        if not actual_width(value) <= exact_arb(allocation):
            self.rejected.append(dict(interval=[str(left),str(right)],depth=depth,
                width=record(actual_width(value)),exact_allocated_width=str(allocation),
                original_cached_midpoint_width=record(old_point_width),
                fresh_complete_midpoint_used=fresh,
                complete_Taylor_remainder=record(remainder)))
            if depth >= self.args.max_depth:
                raise ArithmeticError("a resumed strict Taylor integral exhausted its actual budget")
            self.integrate_budgeted_cell(row,scalar_sha,piece,left,middle,allocation/2,depth+1)
            self.integrate_budgeted_cell(row,scalar_sha,piece,middle,right,allocation/2,depth+1)
            return
        if left != self.cursor:
            raise ArithmeticError("a resumed strict cell does not continue the exact original prefix")
        self.strict_integral += value
        self.cursor = right
        self.rows.append(dict(interval=[str(left),str(right)],actual_candidate_piece=piece,
            scalar_native_sha256=scalar_sha,depth=depth,
            complete_signed_integral=record(value),complete_sixth_derivative_Taylor_fee=record(remainder),
            exact_allocated_width=str(allocation),fresh_complete_midpoint_used=fresh,
            original_cached_midpoint_width=record(old_point_width),
            resumed_from_original_run=ORIGINAL_RUN))

    def integrate_strict(self):
        cursor = self.cursor
        for germ in self.cover["germs"]:
            if germ["germ_index"] < 167:
                continue
            path = self.base/Path(germ["path"])
            if sha(path) != germ["sha256"]:
                raise ValueError("an original remaining scalar germ changed")
            native = read(path)
            if not native["complete"] or native["configuration"] != self.cover["configuration"]:
                raise ValueError("a complete original remaining scalar germ is required")
            if germ["germ_index"] >= len(self.scalar_inputs):
                self.scalar_inputs.append(dict(germ_index=germ["germ_index"],path=str(path),sha256=germ["sha256"]))
            for row in native["rows"]:
                a,b = map(Fraction,row["interval"])
                if b <= cursor:
                    continue
                if a >= self.cut:
                    break
                if not a <= cursor < b:
                    raise ValueError("the remaining scalar cells do not meet the original prefix")
                end = min(b,self.cut)
                while cursor < end:
                    piece = bisect_right(self.nodes,cursor)-1
                    right = min(end,self.nodes[piece+1])
                    self.remaining_tasks.append((row,germ["sha256"],piece,cursor,right,germ["germ_index"]))
                    cursor = right
            if cursor == self.cut:
                break
        if cursor != self.cut or not self.remaining_tasks:
            raise ValueError("the complete remaining original partition does not reach the unchanged cut")
        allocation = self.args.width_goal/Fraction(4*len(self.remaining_tasks))
        self.state.update(remaining_original_cells=len(self.remaining_tasks),
            exact_remaining_total_width_allocation=str(self.args.width_goal/4),
            exact_width_allocation_per_remaining_original_cell=str(allocation))
        self.checkpoint("original-prefix-and-remaining-partition-verified")
        for index,(row,scalar_sha,piece,left,right,germ_index) in enumerate(self.remaining_tasks):
            self.integrate_budgeted_cell(row,scalar_sha,piece,left,right,allocation,0)
            self.checkpoint("resumed-strict-cell-"+str(index))
            if index%8 == 0 or index+1 == len(self.remaining_tasks):
                print(dict(stage="resumed-strict",new_original_cells=index+1,
                    total_new_original_cells=len(self.remaining_tasks),original_reused_rows=2838,
                    complete_point=str(self.cursor),rows=len(self.rows),
                    new_strict_midpoints=len(self.fresh_points),
                    integral=self.strict_integral.str(18),seconds=time.monotonic()-self.started),flush=True)
        if self.cursor != self.cut:
            raise ArithmeticError("the resumed strict integral misses its unchanged exact cut")
        self.state["actual_complete_strict_width"] = record(actual_width(self.strict_integral))
        self.state["actual_complete_strict_width_below_half_goal"] = bool(
            actual_width(self.strict_integral) < exact_arb(self.args.width_goal)/2)
        if not self.state["actual_complete_strict_width_below_half_goal"]:
            raise ArithmeticError("the actual aggregate strict width exhausts its whole budget")
        self.checkpoint("complete-resumed-strict-integral")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic",type=Path,default=Path.cwd())
    parser.add_argument("--candidate",type=Path,required=True)
    parser.add_argument("--scalar-cover",type=Path,required=True)
    parser.add_argument("--repair",type=Path,required=True)
    parser.add_argument("--root-germ",type=Path,required=True)
    parser.add_argument("--object",type=Path,required=True)
    parser.add_argument("--resume",type=Path,required=True)
    parser.add_argument("--cut-gap",type=Fraction,default=Fraction(1,262144))
    parser.add_argument("--width-goal",type=Fraction,default=Fraction(1,1000))
    parser.add_argument("--max-depth",type=int,default=14)
    parser.add_argument("--max-fresh-points",type=int,default=512)
    parser.add_argument("--bits",type=int,default=256)
    parser.add_argument("--exponential-bits",type=int,default=192)
    parser.add_argument("--root-precision-bits",type=int,default=140)
    parser.add_argument("--partial",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args = parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("run the mathematical continuation in the actual public repository Actions")
    if args.out.exists() or args.partial.exists():
        raise FileExistsError("preserve every original continuation and prefix")
    if not 0 < args.width_goal < 1 or not 0 < args.cut_gap < Fraction(1,100000):
        raise ValueError("retain explicit valid original width and root collar")
    ctx.prec = args.bits
    ctx.cap = 8
    work = None
    try:
        work = ResumeConsumer(args)
        work.checkpoint("original-2838-cells-and-two-root-steps-reused")
        work.integrate_strict()
        work.integrate_root()
    except Exception as exc:
        if work is not None:
            work.state["failure"] = f"{type(exc).__name__}: {exc}"
            work.state["complete"] = False
            work.checkpoint("failed-resumed-prefix-preserved")
            if not args.out.exists():
                save(args.out,work.state)
        raise


if __name__ == "__main__":
    main()
