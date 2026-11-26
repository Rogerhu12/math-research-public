#!/usr/bin/env python3
"""Small exact local Jacobians; every paid physical row still qualifies a step.

The working matrix is an optimizer device, not a smaller physical problem.
Full 1536-ring values, all paid actual peak orbits, the complete nested 3072
grid and the unchanged actual angular localizer gate every accepted state.
"""
import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

import numpy as np
from scipy.optimize import minimize

PAID_SOURCE_SHA256 = "cc1a1fa3fdca03d1b15fcd2ee6151133a64ab64a571f20990c1f029d5babc1b0"
paid_path = Path(__file__).with_name("inverse_r566_theta_peak_paid_resume_20261126.py")
if hashlib.sha256(paid_path.read_bytes()).hexdigest() != PAID_SOURCE_SHA256:
    raise RuntimeError("the identified paid source loader changed")
import inverse_r566_theta_peak_paid_resume_20261126 as paid

old = paid.checkpoint
driver, angular, hard = old.previous, old.angular, old.hard
SCHEMA = "r566-subradial-working-rows-with-complete-physical-acceptance-v1"
INPUT_SCHEMA = "r566-paid-complete-start-after-callback-source-v1"
SOURCE_RUN, SOURCE_JOB = 45819650602, 139908280075
SOURCE_COMMIT = "b8fd978de20dfdc9f4921c4c9168fb77f6afc6c1"
SOURCE_RAW_SHA = "5cc35960724511c9de99271622d8cdd25e6c8266045d5c39f4ae1f9a00d38afb"
SOURCE_START_SHA = "be0ca792a9dea74b01e50142c400ed40a2a53d33d6268610ca0aeefe37532de4"
SOURCE_ANCESTOR_INPUT_SHA = "0f22f75b4ac02c3e6c286b894b310c85bc61f3959ca4476397fc487fc59262ba"
SOURCE_Q_SHA = "7e708ba7a973e8505a81e94073707e8c39504d1f3285253f97e3564382992080"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def check_time(deadline):
    if time.monotonic() >= deadline:
        raise hard.EndSegment("working-row scientific clock before next atomic operation")


class RestartWorking(Exception):
    pass


def source_input(args):
    source = json.loads(args.source_state_json)
    if source.get("schema") != INPUT_SCHEMA:
        raise ValueError("wrong complete START input schema")
    ancestor_text = source["ancestor_exact_source_state_json"]
    if digest(ancestor_text.encode()) != SOURCE_ANCESTOR_INPUT_SHA:
        raise ValueError("the preceding complete callback input text was changed")
    ancestor_args = argparse.Namespace(**vars(args))
    ancestor_args.source_state_json = ancestor_text
    ancestor, par, geo, q, nodes, angles, trust = paid.source_input(ancestor_args)
    peaks = old.merge_peaks(ancestor["actual_input_state"]["extra_actual_peak_orbits"],
                           ancestor["recorded_unapplied_constraint_proposal"]["extra_peak_orbits"])
    origin = source["origin"]
    expected = {"run_id": SOURCE_RUN, "job_id": SOURCE_JOB, "source_commit": SOURCE_COMMIT,
                "executed_wrapper_sha256": PAID_SOURCE_SHA256,
                "raw_stdout_bytes": 576947, "raw_stdout_sha256": SOURCE_RAW_SHA,
                "complete_START_JSON_bytes": 74878, "complete_START_JSON_sha256": SOURCE_START_SHA,
                "retained_q_binary64_sha256": SOURCE_Q_SHA,
                "kind": "complete_START_only_before_external_runner_shutdown"}
    if origin != expected:
        raise ValueError("the last observed START and censored origin were changed")
    repository = Path(__file__).resolve().parents[3]
    original = subprocess.run(["git", "show", SOURCE_COMMIT +
        ":topics/visible-flex-new-mechanism/scripts/inverse_r566_theta_peak_paid_resume_20261126.py"],
        cwd=repository, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False, timeout=60)
    if original.returncode or digest(original.stdout) != PAID_SOURCE_SHA256:
        raise ValueError("last actually executed wrapper is not its original Git object")
    start = dict(source["complete_START_without_repeated_coordinates"])
    if any(k in start for k in ("q", "actual_constraint_radial_nodes", "actual_extra_peak_orbits")):
        raise ValueError("the compact START duplicates instead of identifying the paid coordinates")
    start.update(q=q.tolist(), actual_constraint_radial_nodes=nodes.tolist(),
                 actual_extra_peak_orbits=peaks)
    raw = compact(start).encode()
    if len(raw) != 74878 or digest(raw) != SOURCE_START_SHA:
        raise ValueError("reconstructed full original START bytes differ")
    if (len(nodes), len(peaks), angles) != (571, 1276, 1536):
        raise ValueError("the actually adopted START library was not retained")
    if (digest(q.tobytes()) != SOURCE_Q_SHA or trust != start["local_step_trust"]
            or trust != 1.20135498046875 or start["phase"] != "metric"
            or start["new_initial_peaks_pending_for_this_backend"] != []):
        raise ValueError("last true q, unadapted trust, phase or pending identity differs")
    costs = source["source_cost_ledger"]
    if (costs["prior_recorded_scientific_seconds_lower_bound"] !=
            ancestor["source_cost_ledger"]["recorded_chain_scientific_seconds_lower_bound"]
            or costs["new_disjoint_completed_localizer_seconds"] != 22.603199331
            or costs["recorded_chain_scientific_seconds_lower_bound"] != 2875.8708450680003
            or costs["recorded_chain_scientific_seconds_is_exact"] is not False
            or costs["START_to_external_shutdown_wall_seconds"] != 68.2931574
            or not costs["pre_START_unclosed_work_unknown"]
            or not costs["post_START_unflushed_work_unknown"]):
        raise ValueError("completed science and censored wall time were conflated")
    return source, ancestor, start, par, geo, q, nodes, peaks, angles, trust


def row_key(row):
    if row["field"] == "mean_E_floor":
        angle_key = ("ring_mean", 0)
    elif row["kind"] == "uniform":
        angle_key = ("uniform", int(row["angular_index"]))
    else:
        angle_key = ("actual", float(row["theta"]).hex())
    return row["field"], float(row["s"]).hex(), angle_key


def row_angles(row, nt):
    if row["field"] == "mean_E_floor":
        return np.zeros(4)
    if row["kind"] == "uniform":
        j = int(row["angular_index"])
        indices = np.array([j, (-j) % nt, (nt//2-j) % nt, (nt//2+j) % nt])
        # Use the original exact stored uniform values, not theta +/- pi
        # arithmetic which can turn a strict gather into an off-grid sum.
        return (np.arange(nt)*(2*np.pi/nt))[indices]
    return old.orbit_angles(float(row["theta"]))


def add_rows(library, proposed, maximum):
    found = {row_key(r): dict(r) for r in library}
    newly = []
    for row in proposed:
        key = row_key(row)
        if key not in found:
            found[key] = dict(row)
            newly.append(dict(row))
    result = list(found.values())
    if len(result) > maximum:
        return library, newly, result
    return result, newly, None


def append_radial_nodes(actual, new, length):
    """The old actual floating nodes are protected, including both endpoints."""
    retained = [float(s) for s in actual]
    if not retained or retained[0] != 0. or retained[-1] != length:
        raise ValueError("the complete physical library lost its original endpoints")
    threshold = 1e-12*max(1., length)
    for s in sorted(float(s) for s in new):
        if not np.isfinite(s) or not 0. <= s <= length:
            raise ValueError("invalid proposed material radial point")
        if min(abs(s-t) for t in retained) > threshold:
            retained.append(s)
    return np.asarray(sorted(retained))


def bind_working_radii(descriptors, actual_nodes):
    """Use exactly the same material circle as the full paid point evaluator.

    The old full library maps a recorded peak to its retained radial node
    within 1e-12. Preserve the recorded coordinate in evidence and use that
    very node here, never a new independent near-node interpolation.
    """
    result = {}
    for original in descriptors:
        row = dict(original)
        i = int(np.argmin(abs(actual_nodes-float(row["s"]))))
        if abs(actual_nodes[i]-float(row["s"])) > 1e-12:
            raise ValueError("working row is not part of the complete physical radial library")
        if float(actual_nodes[i]) != float(row["s"]):
            row["recorded_source_s_before_original_full_point_node_map"] = float(row["s"])
            row["s"] = float(actual_nodes[i])
        result[row_key(row)] = row
    return list(result.values())


def point_set_for_rows(oracle, descriptors):
    indices, theta = [], []
    for row in descriptors:
        i = int(np.argmin(abs(oracle.uniform.s-float(row["s"]))))
        if abs(oracle.uniform.s[i]-float(row["s"])) > 1e-12:
            raise ValueError("a true working radial coordinate was not retained")
        indices.extend([i]*4)
        theta.extend(row_angles(row, oracle.uniform.nt).tolist())
    return oracle.points(indices, theta)


def selected_point_rows(g, descriptors, par, geo, phase, extra, nd=0):
    groups, flags = driver.constraint_groups(g, par, geo["mean_E_floor"],
        geo["det_floor"], geo["geometry_margin"], phase, extra)
    values, derivatives, last = [], [], []
    for i, row in enumerate(descriptors):
        field = groups[row["field"]]
        candidates = field.v.ravel()[4*i:4*i+4]
        selected = 4*i+int(np.argmin(candidates))
        value = float(field.v.ravel()[selected])
        # Match the old actual argmin BEFORE adding the common sigma.
        if phase == "geometry_restoration":
            value += extra
        values.append(value)
        last.append(float(flags[row["field"]]))
        if nd:
            derivatives.append(field.d.reshape(-1, nd)[selected])
    return (np.asarray(values), np.asarray(derivatives) if nd else None,
            np.asarray(last))


class OracleLedger:
    def __init__(self):
        self.retired = {}
        self.live = []
        self.constructor_seconds = 0.
        self.constructed_oracles = 0

    def create(self, par, radial, nt, batch):
        started = time.monotonic()
        oracle = angular.AngularOracle(par, radial, nt, batch)
        self.constructor_seconds += time.monotonic()-started
        self.constructed_oracles += 1
        self.live.append(oracle)
        return oracle

    def retire(self, oracle):
        if oracle is None or oracle not in self.live:
            return
        for key, value in oracle.counts.items():
            self.retired[key] = self.retired.get(key, 0)+value
        self.live.remove(oracle)
        oracle.release()

    def snapshot(self):
        result = dict(self.retired)
        result["oracle_constructor_seconds"] = self.constructor_seconds
        result["oracle_constructors_completed"] = self.constructed_oracles
        for oracle in self.live:
            for key, value in oracle.counts.items():
                result[key] = result.get(key, 0)+value
        return result


class WorkingRows:
    """Only evidenced field/orbit rows; each radial mean uses all 1536 nodes."""
    def __init__(self, par, geo, descriptors, nt, phase, args, deadline, ledger):
        self.par, self.geo, self.rows = par, geo, list(descriptors)
        self.phase, self.args, self.deadline, self.ledger = phase, args, deadline, ledger
        self.batches = []
        radial = sorted({float(r["s"]) for r in descriptors})
        for first in range(0, len(radial), args.working_radial_batch):
            chosen = set(radial[first:first+args.working_radial_batch])
            chosen_rows = [i for i, r in enumerate(descriptors) if float(r["s"]) in chosen]
            # The physical constructor requires endpoints and at least five
            # circles. Fillers are only FFT circles, never extra objective rows.
            # Protect every actual working circle against near filler nodes.
            # hard.merged_nodes on the union could otherwise retain the filler
            # and replace a true row's r by a nearby distinct float.
            sub_values = sorted(chosen | {0., float(par.length)})
            for filler in np.linspace(0, par.length, 5):
                if min(abs(filler-s) for s in sub_values) > 1e-12:
                    sub_values.append(float(filler))
            sub = np.asarray(sorted(sub_values))
            oracle = ledger.create(par, sub, nt, args.point_batch_size)
            desc = [descriptors[i] for i in chosen_rows]
            points = point_set_for_rows(oracle, desc)
            self.batches.append((oracle, np.asarray(chosen_rows), desc, points))
        self.size = self.batches[0][0].uniform.size
        self.key = self.values = self.jacobian = None
        self.counts = {"value_keys": 0, "complete_jacobians": 0, "direction_blocks": 0,
            "maximum_block_value_difference": 0.0, "value_seconds": 0.0, "jacobian_seconds": 0.0}

    def fun(self, value):
        value = np.asarray(value, dtype=float)
        key = value.tobytes()
        if key == self.key:
            return self.values
        start = time.monotonic()
        answer = np.empty(len(self.rows))
        for oracle, indices, descriptors, points in self.batches:
            check_time(self.deadline)
            state = oracle.prepare(value[:-1])
            field = oracle.evaluate(state, points)
            answer[indices] = selected_point_rows(field, descriptors, self.par, self.geo,
                                                   self.phase, float(value[-1]))[0]
            oracle.release()
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError("nonfinite working row value")
        self.key, self.values, self.jacobian = key, answer, None
        self.counts["value_keys"] += 1
        self.counts["value_seconds"] += time.monotonic()-start
        return answer

    def jac(self, value):
        value = np.asarray(value, dtype=float)
        self.fun(value)
        if self.jacobian is not None:
            return self.jacobian
        started = time.monotonic()
        answer = np.empty((len(self.rows), self.size+1))
        for oracle, rows, descriptors, points in self.batches:
            for first in range(0, self.size, self.args.block_directions):
                check_time(self.deadline)
                columns = np.arange(first, min(first+self.args.block_directions, self.size))
                state = oracle.prepare(value[:-1], columns)
                fields = oracle.evaluate(state, points)
                reconstructed, derivative, extra = selected_point_rows(fields, descriptors,
                    self.par, self.geo, self.phase, float(value[-1]), len(columns))
                error = float(np.max(abs(reconstructed-self.values[rows])))
                self.counts["maximum_block_value_difference"] = max(
                    self.counts["maximum_block_value_difference"], error)
                if error > 1e-12*max(1., float(np.max(abs(self.values[rows])))):
                    raise ArithmeticError("restricted radial AD changed the actual row or value")
                answer[np.ix_(rows, columns)] = derivative
                if first == 0:
                    answer[rows, -1] = extra
                self.counts["direction_blocks"] += 1
                oracle.release()
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError("nonfinite working Jacobian")
        self.jacobian = answer
        self.counts["complete_jacobians"] += 1
        seconds = time.monotonic()-started
        self.counts["jacobian_seconds"] += seconds
        hard.emit("WORKING_ROWS_JACOBIAN", {"rows": len(self.rows), "columns": self.size+1,
            "sub_radial_batches": len(self.batches), "largest_sub_radial_grid":
            max(o.uniform.nr for o, _, _, _ in self.batches), "FFT_nodes_each_ring": 1536,
            "full_physical_constraint_count_not_replaced_by_working_row_count": True,
            "seconds": seconds, "counts": self.counts})
        return answer

    def close(self):
        for oracle, _, _, _ in self.batches:
            self.ledger.retire(oracle)


def candidate_rows(oracle, state, actual_peaks, geo, phase, extra, per_field,
                   existing=(), violations_only=False, tolerance=1e-8):
    """Read every required value, then choose actual witnesses for the matrix.

    A negative row never disappears when it is outside the witness budget:
    the global minimum rejects the trial regardless of the selected subset.
    """
    values_min, total, proposed = np.inf, 0, []
    minima, existing_keys = {}, {row_key(r) for r in existing}
    sets = [(state.uniform_fields, True)]
    extra_actual_s = []
    if actual_peaks:
        extra_actual_s = [float(oracle.uniform.s[int(np.argmin(abs(oracle.uniform.s-p["s"])))])
                          for p in actual_peaks]
        sets.append((oracle.evaluate(state, old.extra_point_set(oracle, actual_peaks)), False))
    for g, uniform in sets:
        groups, _ = driver.constraint_groups(g, oracle.uniform.par, geo["mean_E_floor"],
            geo["det_floor"], geo["geometry_margin"], phase, extra)
        for name, field in groups.items():
            if uniform:
                if field.v.shape[1] == 1:
                    array = field.v.copy()
                else:
                    j = np.arange(oracle.uniform.nt//4+1)
                    orbit = np.stack([j, (-j)%oracle.uniform.nt,
                        (oracle.uniform.nt//2-j)%oracle.uniform.nt,
                        (oracle.uniform.nt//2+j)%oracle.uniform.nt], axis=-1)
                    array = np.min(field.v[:, orbit], axis=-1)
                total += array.size
            else:
                array = np.min(field.v.reshape(-1, 4), axis=1)[:, None]
                total += field.v.size
            if phase == "geometry_restoration":
                array = array+extra
            if not np.all(np.isfinite(array)):
                raise FloatingPointError("nonfinite complete physical constraint value")
            minimum = float(np.min(array))
            values_min = min(values_min, minimum)
            minima[name] = min(minima.get(name, np.inf), minimum)
            # Existing witness exclusions affect selection only, never min.
            selectable = array.copy()
            extra_row_indices = {}
            if not uniform:
                for ir, peak in enumerate(actual_peaks):
                    candidate = {"field":name, "s":extra_actual_s[ir],
                                 "theta":peak["theta"], "kind":"actual"}
                    extra_row_indices.setdefault(row_key(candidate), []).append(ir)
            for row in existing:
                if row["field"] != name:
                    continue
                if uniform and (row["kind"] == "uniform" or name == "mean_E_floor"):
                    ir = int(np.argmin(abs(oracle.uniform.s-row["s"])))
                    if abs(oracle.uniform.s[ir]-row["s"]) <= 1e-12:
                        col = 0 if name == "mean_E_floor" else int(row["angular_index"])
                        selectable[ir, col] = np.inf
                elif not uniform:
                    for ir in extra_row_indices.get(row_key(row), ()):
                        selectable[ir, 0] = np.inf
            radial_min = np.min(selectable, axis=1)
            if violations_only:
                choices = np.flatnonzero(radial_min < -tolerance)
            elif not uniform:
                choices = np.flatnonzero(radial_min <= max(.02, minimum+.01))
                choices = np.unique(np.r_[choices, int(np.argmin(radial_min))])
            else:
                before, after = np.r_[np.inf, radial_min[:-1]], np.r_[radial_min[1:], np.inf]
                local = (radial_min <= before) & (radial_min <= after) & (
                    (radial_min < before) | (radial_min < after))
                choices = np.flatnonzero(local & (radial_min <= max(.02, minimum+.01)))
                choices = np.unique(np.r_[choices, int(np.argmin(radial_min))])
            choices = sorted(choices.tolist(), key=lambda i: (radial_min[i], i))[:per_field]
            for i in choices:
                col = int(np.argmin(selectable[i]))
                if not np.isfinite(selectable[i, col]):
                    continue
                if uniform:
                    row = {"field": name, "s": float(oracle.uniform.s[i]), "kind": "uniform",
                           "angular_index": col, "theta": float(oracle.uniform.theta[col])}
                else:
                    peak = actual_peaks[i]
                    actual_s = extra_actual_s[i]
                    row = {"field": name, "s": actual_s, "kind": "actual",
                           "theta": float(peak["theta"]),
                           "recorded_source_s_before_original_full_point_node_map": float(peak["s"])}
                row["evidence"] = {"source": "complete_required_value_scan",
                    "row_value_including_backend_extra": float(selectable[i, col]),
                    "q_binary64_sha256": digest(state.q.tobytes())}
                if row_key(row) not in existing_keys:
                    proposed.append(row)
    return {"minimum_complete_required_row": float(values_min),
            "complete_required_row_count": total, "minimum_by_group": minima,
            "maximum_violation": float(max(0., -values_min)), "working_witnesses": proposed}


def restricted_mapping_observation(rows, full_oracle, q, extra, geo, deadline):
    """One new radial-restriction map/derivative observation inside this run."""
    value = np.r_[q, extra]
    points = point_set_for_rows(full_oracle, rows.rows)
    check_time(deadline)
    state = full_oracle.prepare(q)
    reference = selected_point_rows(full_oracle.evaluate(state, points), rows.rows,
        rows.par, geo, rows.phase, extra)[0]
    actual = rows.fun(value)
    error = float(np.max(abs(reference-actual)))
    direction = np.sin(np.arange(len(value))+.417)
    direction /= np.linalg.norm(direction)
    analytic = rows.jac(value)@direction
    step = 1e-6
    observations = []
    for sign in (1, -1):
        check_time(deadline)
        v = value+sign*step*direction
        state = full_oracle.prepare(v[:-1])
        observations.append(selected_point_rows(full_oracle.evaluate(state, points), rows.rows,
            rows.par, geo, rows.phase, float(v[-1]))[0])
    numerical = (observations[0]-observations[1])/(2*step)
    relative = float(np.linalg.norm(analytic-numerical)/max(np.linalg.norm(numerical), 1e-14))
    hard.emit("WORKING_ROWS_NEW_RESTRICTION_MAP", {
        "full_vs_subradial_value_max_difference": error,
        "directional_relative_l2": relative,
        "directional_absolute_max": float(np.max(abs(analytic-numerical))),
        "actual_field_orbit_rows": rows.rows, "complete_full_radial_count": full_oracle.uniform.nr,
        "sub_radial_batch_counts": [o.uniform.nr for o, _, _, _ in rows.batches],
        "full_1536_mean_E_preserved_in_both_models": True,
        "new_restriction_mapping_not_replay_of_old_oracle_parity": True,
        "finite_difference_observation_not_a_proof": True})
    full_oracle.release()
    if error > 1e-9 or relative >= 3e-4:
        raise ArithmeticError("new working-row radial restriction failed its declared observation")


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source-state-json", required=True)
    p.add_argument("--source-state-sha256", required=True)
    for name, value in {"radial-base":49, "outer":120, "maxiter":80,
        "maximum-radial-nodes":1025, "maximum-extra-peaks":2048,
        "localizer-batch-size":512, "block-directions":16, "point-batch-size":64,
        "working-radial-batch":24, "working-witnesses-per-field":6,
        "maximum-working-rows":512}.items():
        p.add_argument("--"+name, type=int, default=value)
    for name, value in {"angle-tolerance":1e-10, "peak-near-band":.002,
        "pending-peak-tolerance":1e-8, "nested-quadrature-tolerance":1e-7,
        "minimum-trust":1/256, "maximum-trust":4., "maximum-seconds":2400.,
        "final-reserve-seconds":30.}.items():
        p.add_argument("--"+name, type=float, default=value)
    return p


def main():
    args = parser().parse_args()
    raw = sys.stdin.buffer.read() if args.source_state_json == "@stdin" else args.source_state_json.encode()
    if digest(raw) != args.source_state_sha256:
        raise ValueError("complete stdin source-state hash differs")
    args.source_state_json = raw.decode()
    if (not 0 < args.final_reserve_seconds < args.maximum_seconds <= 2400
            or not 0 < args.minimum_trust <= args.maximum_trust <= 4
            or min(args.radial_base, args.outer, args.maxiter, args.working_radial_batch,
                   args.working_witnesses_per_field, args.maximum_working_rows) < 1
            or not 1 <= args.block_directions <= 81 or args.point_batch_size < 1):
        raise ValueError("invalid working-row scope")
    started = time.monotonic()
    deadline = started+args.maximum_seconds-args.final_reserve_seconds
    source, ancestor, start, par, geo, q, nodes, peaks, nt, trust = source_input(args)
    tolerance = geo["feasibility_tolerance"]
    mean_floor, det_floor, margin = geo["mean_E_floor"], geo["det_floor"], geo["geometry_margin"]
    best_scan = dict(start["initial_fine_and_observed_scan"])
    best_geo = 0.
    best_eta = best_scan["accepted_eta_max"]
    best_observed = dict(start["initial_observed_peaks"])
    pending, proposed_working, working = [], [], []
    actual_nodes, actual_peaks = nodes.copy(), list(peaks)
    actual_trust, proposed_trust = trust, trust
    trust_decision_completed = False
    ledger = OracleLedger()
    counts = {"outer_started":0, "outer_completed":0, "accepted_metric_steps":0,
        "accepted_restoration_steps":0, "working_value_rejected_callbacks":0,
        "complete_coarse_scans":0, "complete_fine_scans":0,
        "complete_localizations":0, "localizer_candidates":0, "localizer_completed_candidates":0,
        "localizer_point_objective_evaluations":0, "localizer_unresolved_returns":0,
        "required_row_rejections":0, "fine_required_row_rejections":0,
        "nested_quadrature_rejections":0, "working_exchanges":0, "physical_exchanges":0,
        "backend_natural_returns":0, "new_restriction_observations":0,
        "working_value_keys":0, "working_complete_jacobians":0,
        "working_direction_blocks":0, "working_jacobian_seconds":0.}
    last_trial = last_backend = None
    active_rows = None
    current_outer, phase = -1, "metric"
    status = "declared_outer_limit_not_complete"

    def costs():
        return {"elapsed_seconds":time.monotonic()-started, "counts":dict(counts),
            "active_working_counts_not_yet_retired": None if active_rows is None else dict(active_rows.counts),
            "oracle_totals_once_per_live_or_retired_oracle":ledger.snapshot(),
            "prior_cost_ledger":source["source_cost_ledger"],
            "all_unclosed_current_operation_work_in_elapsed_not_fabricated_as_completed":True}

    def snapshot(tag, reason):
        hard.emit(tag, {"schema":SCHEMA, "reason":reason, "outer":current_outer,
            "phase":phase, "actual_retained_q":q.tolist(), "actual_q_binary64_sha256":digest(q.tobytes()),
            "actual_retained_qualification":best_scan,
            "actual_retained_observed_peak_summary":best_observed,
            "actual_complete_required_radial_nodes":actual_nodes.tolist(),
            "actual_complete_required_peak_orbits":actual_peaks,
            "actual_uniform_angles_and_FFT_nodes":nt,
            "recorded_unapplied_physical_peak_orbits":pending,
            "actual_working_field_orbit_rows":working,
            "recorded_unapplied_working_rows":proposed_working,
            "actual_backend_local_trust":actual_trust, "proposed_next_local_trust":proposed_trust,
            "post_backend_trust_decision_completed": trust_decision_completed,
            "proposed_trust_not_yet_adopted": proposed_trust != actual_trust,
            "retained_qualification_is_on_its_recorded_grid_not_automatic_for_new_library": True,
            "last_trial_not_implicitly_accepted":last_trial, "last_backend":last_backend,
            "cost":costs(), "no_physical_row_removed_by_working_selection":True,
            "continuous_geometry_reach_or_README_completion_claim":False})

    hard.emit("WORKING_ROWS_DEFINITION", {"schema":SCHEMA, "source_state":source,
        "source_state_sha256":digest(raw), "physical_parameters":asdict(par), "geometry_parameters":geo,
        "solver_arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "original_571_rings_and_1276_orbits_retained":True,
        "all_old_1536_uniform_inequalities_retained_for_full_value_acceptance":True,
        "working_points_never_redefine_mean_E":True,
        "old_completed_START_scan_and_localization_not_replayed":True,
        "old_unadapted_trust_retained":True,
        "every_accepted_step_requires_complete_coarse_fine_actual_peaks_and_nested_quadrature":True,
        "unrepresented_violations_reject_and_enter_working_or_physical_libraries":True,
        "fine_geometry_margin_and_backend_metric_epigraph_enforced_at_acceptance":True,
        "only_local_optimization_matrix_is_restricted":True,
        "old_oracle_parity_check_not_repeated":True,
        "one_new_radial_restriction_mapping_observation_in_this_same_run":True,
        "metric_changes_during_static_design":True, "fixed_g_or_README_completion_claim":False})
    snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT", "paid START retained before new scientific work")

    try:
        for outer in range(args.outer):
            current_outer = outer
            check_time(deadline)
            if pending:
                proposal_peaks = old.merge_peaks(actual_peaks, pending)
                proposal_nodes = append_radial_nodes(actual_nodes,
                    [p["s"] for p in pending], par.length)
                if len(proposal_nodes)>args.maximum_radial_nodes or len(proposal_peaks)>args.maximum_extra_peaks:
                    status = "complete_physical_library_capacity_checkpoint"
                    break
                actual_nodes, actual_peaks = proposal_nodes, proposal_peaks
                pending = []
                counts["physical_exchanges"] += 1
            if proposed_working:
                new_working, added, overflow = add_rows(working, proposed_working, args.maximum_working_rows)
                if overflow is not None:
                    status = "working_matrix_capacity_with_all_physical_rows_still_required"
                    break
                working, proposed_working = new_working, []
                counts["working_exchanges"] += bool(added)
            actual_trust = proposed_trust
            trust_decision_completed = False
            working = bind_working_radii(working, actual_nodes)
            coarse = fine = None
            outcome = None
            accepted_this_outer = 0
            last_checked_key = None
            backend_reason = "before_backend"
            seed_q = q.copy()
            counts["outer_started"] += 1
            try:
                coarse = ledger.create(par, actual_nodes, nt, args.point_batch_size)
                # This full value scan is needed to select this new matrix and
                # exposes every prior physical row. It is not an old fine replay.
                state = coarse.prepare(q)
                seed = candidate_rows(coarse, state, actual_peaks, geo, "metric", best_eta+1e-8,
                                      args.working_witnesses_per_field)
                counts["complete_coarse_scans"] += 1
                geometry_min = min(v for k,v in seed["minimum_by_group"].items()
                                   if not k.startswith("metric_"))
                phase = "geometry_restoration" if geometry_min < -tolerance else "metric"
                if phase == "geometry_restoration":
                    best_geo = max(best_geo, -geometry_min)
                    extra = best_geo+.01
                    seed = candidate_rows(coarse, state, actual_peaks, geo, phase, extra,
                                          args.working_witnesses_per_field)
                    seed_proposal = seed["working_witnesses"]
                    # Metric rows are inactive in Phase I, never invalid fields.
                    working = [r for r in working if not r["field"].startswith("metric_")]
                else:
                    extra = best_eta+args.pending_peak_tolerance+max(0.,
                        -seed["minimum_by_group"].get("metric_plus",0.),
                        -seed["minimum_by_group"].get("metric_minus",0.))
                    seed_proposal = seed["working_witnesses"]
                working, added, overflow = add_rows(working, seed_proposal, args.maximum_working_rows)
                if overflow is not None:
                    proposed_working = seed_proposal
                    status = "working_matrix_capacity_at_new_evidenced_selection"
                    break
                lower, upper = coarse.uniform.bounds()
                if q.shape != (81,) or np.any(q<lower-1e-12) or np.any(q>upper+1e-12):
                    raise ValueError("retained source violates unchanged physical boxes")
                scales = np.r_[np.full(2*coarse.uniform.block,.5),
                    np.full(par.radial_count,.2), np.full(par.radial_count,.15), .1]
                lo, hi = np.maximum(lower,q-actual_trust*scales), np.minimum(upper,q+actual_trust*scales)
                active_rows = WorkingRows(par,geo,working,nt,phase,args,deadline,ledger)
                del state
                x0 = np.r_[q,extra]
                if counts["new_restriction_observations"] == 0:
                    restricted_mapping_observation(active_rows,coarse,q,extra,geo,deadline)
                    counts["new_restriction_observations"] += 1
                fine_nodes = append_radial_nodes(actual_nodes,
                    np.r_[(actual_nodes[:-1]+actual_nodes[1:])/2,
                          np.linspace(0,par.length,2*args.radial_base-1)],par.length)
                fine = ledger.create(par,fine_nodes,2*nt,args.point_batch_size)
                hard.emit("WORKING_ROWS_BACKEND_START", {"outer":outer,"phase":phase,
                    "q":q.tolist(),"backend_extra":extra,"actual_local_trust":actual_trust,
                    "complete_required_radial_nodes":len(actual_nodes),
                    "complete_required_peak_orbits":len(actual_peaks),
                    "complete_required_scalar_rows":seed["complete_required_row_count"],
                    "working_rows":working,"working_sub_radial_batches":
                    [o.uniform.s.tolist() for o,_,_,_ in active_rows.batches],
                    "full_fine_radial_nodes":len(fine_nodes),"full_fine_theta_nodes":2*nt,
                    "baseline_fine_observation_reused_from_identified_paid_START_or_last_acceptance":True})

                def callback(value, terminal=False):
                    nonlocal q,best_scan,best_observed,best_geo,best_eta,last_trial,last_checked_key
                    nonlocal pending,proposed_working,accepted_this_outer,backend_reason
                    v=np.asarray(value,dtype=float)
                    key=v.tobytes()
                    if key==last_checked_key:
                        return
                    last_checked_key=key
                    check_time(deadline)
                    trial=v[:-1].copy()
                    last_trial={"q":trial.tolist(),"q_binary64_sha256":digest(trial.tobytes()),
                        "backend_extra":float(v[-1]),"outer":outer,"phase":phase,
                        "terminal_backend_point":terminal,"working_row_violation":None,
                        "accepted":False,"full_coarse_completed":False,"full_fine_completed":False,
                        "full_localization_completed":False}
                    local=active_rows.fun(v)
                    last_trial["working_row_violation"]=float(max(0.,-np.min(local)))
                    if np.min(local)<-tolerance:
                        counts["working_value_rejected_callbacks"]+=1
                        last_trial["reason"]="working_infeasible_internal_iterate_not_accepted"
                        snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
                        return
                    coarse_state=coarse.prepare(trial)
                    complete=candidate_rows(coarse,coarse_state,actual_peaks,geo,phase,float(v[-1]),
                        args.working_witnesses_per_field,working,True,tolerance)
                    counts["complete_coarse_scans"]+=1
                    last_trial.update(full_coarse_completed=True,
                        complete_required_minimum_by_group=complete["minimum_by_group"],
                        complete_required_scalar_rows=complete["complete_required_row_count"])
                    if complete["maximum_violation"]>tolerance:
                        counts["required_row_rejections"]+=1
                        proposed_working.extend(complete["working_witnesses"])
                        last_trial["reason"]="unrepresented_required_coarse_rows_rejected"
                        snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
                        if proposed_working:
                            backend_reason="required_coarse_row_exchange"
                            raise RestartWorking()
                        return
                    # Only a complete-coarse-feasible candidate spends a full
                    # fine/localizer qualification. No acceptance bypass exists.
                    fine_state=fine.prepare(trial)
                    scan=old.full_scan(fine,fine_state,mean_floor,det_floor)
                    counts["complete_fine_scans"]+=1
                    quadrature=old.quadrature_comparison(coarse_state.uniform_fields,fine_state,
                        coarse.uniform.s,fine.uniform.s,par.reach_target)
                    last_trial.update(full_fine_completed=True,full_fine_scan=scan,nested_quadrature=quadrature)
                    quadokay=max(quadrature[k] for k in (
                        "same_q_nested_FFT_metric_components_difference","same_q_relative_mean_E_difference",
                        "same_q_tau_curvature_difference"))<=args.nested_quadrature_tolerance
                    if not quadokay:
                        counts["nested_quadrature_rejections"]+=1
                        last_trial["reason"]="nested_full_FFT_difference_not_qualified"
                        snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
                        return
                    observed=old.locate_peaks(fine,fine_state,mean_floor,det_floor,margin,float(v[-1]),
                        deadline,args.angle_tolerance,args.peak_near_band,args.localizer_batch_size)
                    counts["localizer_candidates"]+=observed["candidate_count"]
                    counts["localizer_completed_candidates"]+=observed["completed_candidate_count"]
                    counts["localizer_point_objective_evaluations"]+=observed["evaluations"]
                    counts["localizer_unresolved_returns"]+=observed["unresolved_candidate_count"]
                    resolved=(observed["status"]=="observed_brackets_localized" and
                              observed["unresolved_candidate_count"]==0)
                    counts["complete_localizations"]+=int(resolved)
                    last_trial["full_localization_completed"]=resolved
                    last_trial["observed_peaks"]=old.compact_observation(observed)
                    observed_current=old.observation_metrics(scan,observed,margin)
                    geometry_peak=max(old.fine_geometry_limits(scan,margin).values())
                    for peak in observed["peaks"]:
                        if not peak["field"].startswith("metric_"):
                            geometry_peak=max(geometry_peak,float(peak["value"]))
                    limits={name:(float(v[-1]) if phase=="geometry_restoration" else 0.)
                            for name in scan["geometry_attainers"]}
                    limits.update(metric_plus=float(v[-1]),metric_minus=float(v[-1]))
                    grid=old.observed_grid_peaks(fine,fine_state,mean_floor,det_floor,margin,
                                                  limits,args.pending_peak_tolerance)
                    violations=[p for p in observed["peaks"]+grid
                        if p["value"]>limits.get(p["field"],0.)+args.pending_peak_tolerance
                        and (phase=="metric" or not p["field"].startswith("metric_"))]
                    additions=old.new_only(violations,actual_nodes,actual_peaks,nt)
                    pending=old.merge_peaks(pending,additions)
                    # All violating coordinates remain physical pending rows.
                    # Only the worst evidenced witnesses enter the next small
                    # matrix; every unselected violation still rejects here.
                    for name in sorted({p["field"] for p in violations}):
                        group=sorted([p for p in violations if p["field"]==name],
                                     key=lambda p:-p["value"])
                        selected_keys=set()
                        for p in group:
                            descriptor={"field":p["field"],"s":float(p["s"]),
                                "kind":"actual","theta":float(p["theta"]),
                                "evidence":{"source":"complete_fine_or_actual_angular_peak",
                                    "value":float(p["value"]),"q_binary64_sha256":digest(trial.tobytes())}}
                            key=row_key(descriptor)
                            if key not in selected_keys:
                                proposed_working.append(descriptor)
                                selected_keys.add(key)
                            if len(selected_keys)>=args.working_witnesses_per_field:
                                break
                    if not resolved:
                        last_trial["reason"]="incomplete_actual_peak_localization_rejected"
                        snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
                        raise hard.EndSegment("unresolved observed angular localization")
                    boundokay=(geometry_peak<=(float(v[-1]) if phase=="geometry_restoration" else 0.)+tolerance
                        and (phase=="geometry_restoration" or
                             observed_current["accepted_eta_max"]<=float(v[-1])+tolerance))
                    if not boundokay or violations:
                        counts["fine_required_row_rejections"]+=1
                        last_trial["reason"]="complete_fine_or_real_peak_epigraph_rejected"
                        snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
                        if additions or proposed_working:
                            backend_reason="complete_fine_actual_peak_exchange"
                            raise RestartWorking()
                        return
                    physicalokay=observed_current["accepted_geometry_violation_max"]<=tolerance
                    accepted=(geometry_peak<best_geo-1e-10 if phase=="geometry_restoration" else
                              physicalokay and observed_current["accepted_eta_max"]<best_eta-1e-12)
                    # Preserve a genuine successful restoration even below the
                    # usual improvement threshold, before emitting its checkpoint.
                    restored=phase=="geometry_restoration" and geometry_peak<=tolerance and physicalokay
                    accepted=accepted or restored
                    last_trial.update(actual_complete_geometry_margin_violation=max(0.,geometry_peak),
                        actual_complete_eta=observed_current["accepted_eta_max"],accepted=bool(accepted))
                    if accepted:
                        q=trial.copy();best_scan=observed_current;best_observed=old.compact_observation(observed)
                        best_geo=max(0.,geometry_peak);best_eta=observed_current["accepted_eta_max"]
                        accepted_this_outer+=1
                        counts["accepted_restoration_steps" if phase=="geometry_restoration" else "accepted_metric_steps"]+=1
                        last_trial["reason"]="accepted_after_all_actual_constraints_and_old_qualification"
                    else:
                        last_trial["reason"]="complete_qualified_trial_without_strict_actual_improvement"
                    snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
                    if restored:
                        backend_reason="complete_geometry_restoration_reached"
                        raise RestartWorking()

                try:
                    backend_reason="inside_SLSQP"
                    outcome=minimize(lambda v:float(v[-1]),x0,jac=lambda v:np.r_[np.zeros(81),1.],
                        method="SLSQP",bounds=list(zip(np.r_[lo,0.],np.r_[hi,np.inf])),
                        constraints={"type":"ineq","fun":active_rows.fun,"jac":active_rows.jac},
                        callback=callback,options={"ftol":1e-9,"maxiter":args.maxiter,"disp":False})
                    counts["backend_natural_returns"]+=1
                    last_backend=old.backend_record(outcome)
                    backend_reason="natural_backend_return"
                    callback(outcome.x,terminal=True)
                except RestartWorking:
                    pass
                if accepted_this_outer and float(np.max(abs(q-seed_q)/scales))>=.9*actual_trust:
                    proposed_trust=min(args.maximum_trust,1.5*actual_trust)
                elif not accepted_this_outer and not pending and not proposed_working and outcome is not None:
                    proposed_trust=max(args.minimum_trust,.5*actual_trust)
                else:
                    proposed_trust=actual_trust
                trust_decision_completed=True
                counts["outer_completed"]+=1
                snapshot("WORKING_ROWS_OUTER_COMPLETE",backend_reason)
                if (outcome is not None and not accepted_this_outer and not pending and not proposed_working
                        and actual_trust<=args.minimum_trust):
                    status="minimum_trust_without_actual_complete_improvement"
                    break
            finally:
                if active_rows is not None:
                    c=active_rows.counts
                    counts["working_value_keys"]+=c["value_keys"]
                    counts["working_complete_jacobians"]+=c["complete_jacobians"]
                    counts["working_direction_blocks"]+=c["direction_blocks"]
                    counts["working_jacobian_seconds"]+=c["jacobian_seconds"]
                    active_rows.close();active_rows=None
                ledger.retire(coarse);ledger.retire(fine)
    except hard.EndSegment as error:
        status="cooperative_clock_or_unresolved_localizer_checkpoint"
        hard.emit("WORKING_ROWS_STOP",{"type":type(error).__name__,"message":str(error)})
    except Exception as error:
        status="explicit_backend_exception_checkpoint"
        hard.emit("WORKING_ROWS_STOP",{"type":type(error).__name__,"message":str(error)})
    finally:
        snapshot("WORKING_ROWS_FINAL",status)


if __name__ == "__main__":
    main()
