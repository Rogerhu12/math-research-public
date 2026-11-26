"""TCX: disjoint complete-cell continuation of one immutable TC trial.

Metadata validation imports no numerical runtime. The public owner supplies
its ORIGINAL directed context and exact whole96/all-source cell evaluator.
All children share already verified readonly trial arrays; no child may
select a trial, reconstruct an old carrier or evaluate a preceding cell.
"""
KIND = "R149_same_trial_disjoint_complete_cell_slices_v1"
SLICE_KIND = "R149_same_trial_complete_cell_slice_v1"
NORM_NAMES = ("positive_low", "positive_high_collar", "positive_high_body",
              "negative_root", "negative_strict")
SOURCE_NAMES = {"owner", "trial_math", "proposal_math", "inputs_math", "box_math", "fft_math",
                "candidate_reader", "repair_source", "direction_source"}
ROWS = 96
MAX_WORKERS = 3


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    import json
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def digest(raw):
    import hashlib
    return hashlib.sha256(raw).hexdigest()


def validate_hex_sums(sums):
    import math
    require(set(sums) == set(NORM_NAMES), "all five complete source windows")
    for values in sums.values():
        require(type(values) is list and len(values) == ROWS, "all96 source-square uppers")
        for value in values:
            require(type(value) is str, "one exact saved binary64 hexadecimal value")
            point = float.fromhex(value)
            require(math.isfinite(point) and point >= 0 and point.hex() == value,
                    "canonical finite nonnegative binary64 upper, never a midpoint")


def balanced_partition(total, first, workers=MAX_WORKERS):
    """Integer scheduling only; the exact original cell cuts never change."""
    require(type(total) is int and type(first) is int and 0 <= first <= total <= 9000
            and type(workers) is int and 1 <= workers <= MAX_WORKERS,
            "one bounded complete exact-plan partition")
    remaining = total-first
    if not remaining:
        return []
    workers = min(workers, remaining)
    boundaries = [first+(remaining*j)//workers for j in range(workers+1)]
    require(boundaries[0] == first and boundaries[-1] == total
            and all(a < b for a, b in zip(boundaries, boundaries[1:])),
            "nonempty disjoint consecutive whole-cell assignments")
    return [list(pair) for pair in zip(boundaries, boundaries[1:])]


def validate_slice_metadata(record, assignment, ordinal, proposal_sha, residual_sha):
    fields = {"kind", "ordinal", "first_cell", "stop_cell", "next_cell", "accepted_complete_cells",
              "complete", "proposal_identity_sha256", "residual_math_sha256", "complete_columns",
              "all_declared_source_components_retained", "squared_norm_upper_exact_binary64"}
    require(set(record) == fields and record["kind"] == SLICE_KIND
            and record["ordinal"] == ordinal
            and [record["first_cell"], record["stop_cell"]] == assignment
            and record["proposal_identity_sha256"] == proposal_sha
            and record["residual_math_sha256"] == residual_sha
            and record["complete_columns"] == ROWS
            and record["all_declared_source_components_retained"] is True,
            "one complete same-trial whole-source slice identity")
    first, stop, next_cell = (record[key] for key in ("first_cell", "stop_cell", "next_cell"))
    require(all(type(value) is int for value in (first, stop, next_cell))
            and 0 <= first <= next_cell <= stop and first < stop
            and record["accepted_complete_cells"] == next_cell-first
            and record["complete"] is (next_cell == stop),
            "the exact complete-cell accepted cursor")
    validate_hex_sums(record["squared_norm_upper_exact_binary64"])
    if next_cell == first:
        require(all(value == float(0).hex() for values in record["squared_norm_upper_exact_binary64"].values()
                    for value in values), "the empty slice is exactly zero in every column/window")
    return next_cell


def validate_parallel_metadata(record, proposal, sources, parallel_source_sha, *, require_prefix=False):
    require(set(sources) == SOURCE_NAMES and record["kind"] == KIND
            and record["parallel_source_sha256"] == parallel_source_sha
            and record["scientific_sources"] == sources
            and record["proposal_identity_sha256"] == digest(canonical(proposal))
            and record["certificate_plan_sha256"] == proposal["certificate_plan_sha256"]
            and record["complete_total_cells"] == proposal["complete_certificate_cells"]
            and record["maximum_arithmetic_children"] == MAX_WORKERS
            and record["one_complete_trial_materialization_before_fork"] is True
            and record["new_slice_boundary_conditions_or_trial_jumps"] is False
            and record["all96_columns_and_all5_source_windows_retained"] is True
            and record["old_scientific_target_calls"] == 0,
            "same whole trial, unchanged original8 mathematical sources and exact plan")
    seed = record["seed_prefix"]
    raw = canonical(seed)
    receipt = record["seed_prefix_receipt"]
    require(receipt["bytes"] == len(raw) and receipt["sha256"] == digest(raw)
            and seed["kind"] == "R149_true_root_residual_full_cell_prefix_v1"
            and seed["proposal_identity"] == proposal
            and seed["certificate_plan_sha256"] == proposal["certificate_plan_sha256"]
            and seed["total_cells"] == proposal["complete_certificate_cells"]
            and set(seed["scientific_sources"]) == SOURCE_NAMES
            and all(seed["scientific_sources"][key] == sources[key] for key in SOURCE_NAMES-{"owner"})
            and seed["next_cell"] == seed["complete_cell_count"]
            and seed["complete_cells_have_all_declared_sources"] is True
            and seed["all96_columns_and_all_declared_source_components_retained"] is True
            and seed["arbitrary_midpoint_not_used_as_an_upper"] is True
            and seed["whole_mathematical_target_complete"] is (seed["next_cell"] == seed["total_cells"]),
            "the whole original qualified seed prefix is immutable")
    validate_hex_sums(seed["squared_norm_upper_exact_binary64"])
    first, total = seed["next_cell"], seed["total_cells"]
    require(type(first) is int and type(total) is int and 0 <= first <= total <= 9000,
            "the original actual full-plan seed index")
    assignments, slices = record["partition"], record["slices"]
    require(assignments == balanced_partition(total, first, MAX_WORKERS)
            and len(slices) == len(assignments) <= MAX_WORKERS,
            "the fixed original disjoint partition is never silently repartitioned")
    union, contiguous, preceding_complete = first, first, True
    for ordinal, (assignment, saved) in enumerate(zip(assignments, slices)):
        end = validate_slice_metadata(saved, assignment, ordinal,
            record["proposal_identity_sha256"], sources["trial_math"])
        union += end-assignment[0]
        if preceding_complete:
            contiguous = end
            preceding_complete = saved["complete"]
    require(record["accepted_union_complete_cells"] == union
            and record["contiguous_next_cell"] == contiguous
            and record["complete"] is (union == total)
            and (union == total) == all(value["complete"] for value in slices),
            "the disjoint union and original contiguous prefix are distinguished")
    prefix_receipt = record["contiguous_prefix_receipt"]
    require(not require_prefix or isinstance(prefix_receipt, dict), "a stable whole prefix receipt is required")
    if prefix_receipt is not None:
        require(set(prefix_receipt) == {"bytes", "sha256"}
                and type(prefix_receipt["bytes"]) is int and 0 < prefix_receipt["bytes"] < 100000
                and type(prefix_receipt["sha256"]) is str and len(prefix_receipt["sha256"]) == 64,
                "whole formal contiguous-prefix byte identity")
    return first, total, contiguous, union


def stable_prefix_matches(record, raw_prefix):
    """No numeric work: a prefix may briefly lead its following state write."""
    import json
    wanted = record["contiguous_prefix_receipt"]
    if not isinstance(wanted, dict) or wanted["bytes"] != len(raw_prefix) or wanted["sha256"] != digest(raw_prefix):
        return False
    prefix = json.loads(raw_prefix)
    return prefix["next_cell"] == record["contiguous_next_cell"]


def _decode(c, sums):
    validate_hex_sums(sums)
    return {name: c.Box(c.np.array([float.fromhex(value) for value in sums[name]], dtype=c.np.float64))
            for name in NORM_NAMES}


def _encode(c, sums):
    result = {}
    for name in NORM_NAMES:
        value = c.upper(sums[name])
        require(value.hi.shape == (ROWS,), "all96 values before exact hexadecimal serialization")
        result[name] = [float(point).hex() for point in value.hi]
    validate_hex_sums(result)
    return result


def whole_sums(c, seed, slices):
    """Recompute ONLY nonnegative saved-upper sums, never any cell integral."""
    union = _decode(c, seed["squared_norm_upper_exact_binary64"])
    contiguous = _decode(c, seed["squared_norm_upper_exact_binary64"])
    count, previous_complete = seed["next_cell"], True
    for record in slices:
        value = _decode(c, record["squared_norm_upper_exact_binary64"])
        union = {name: c.add_upper(union[name], value[name]) for name in NORM_NAMES}
        if previous_complete:
            contiguous = {name: c.add_upper(contiguous[name], value[name]) for name in NORM_NAMES}
            count = record["next_cell"]
            previous_complete = record["complete"]
    return count, contiguous, union


def fork_remaining_cells(c, seed, previous, proposal, sources, parallel_source_sha,
                         evaluate_cell, expected_norms, publish_complete_record,
                         *, private_directory, seconds_remaining, checkpoint_stride=8):
    """At most3 fork children, each computing only its own unaccepted cells.

    publish_complete_record(record, contiguous_count, contiguous_sums,
    union_sums) must write/read the ENTIRE updated scientific checkpoint and
    set record.contiguous_prefix_receipt to the exact formal prefix. Every
    partial union survives through this callback before an unfinished run
    may return. The original seed is not replaced with a merged prefix.
    """
    import copy
    import json
    import multiprocessing
    import os
    import sys
    import time
    import traceback
    from pathlib import Path
    require(sys.platform.startswith("linux") and os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
            and seconds_remaining > 0 and type(checkpoint_stride) is int and checkpoint_stride > 0,
            "the first qualified public Linux disjoint-cell batch")
    proposal_sha = digest(canonical(proposal))
    if previous is None:
        seed = copy.deepcopy(seed)
        assignments = balanced_partition(seed["total_cells"], seed["next_cell"])
        slices = []
        for ordinal, (first, stop) in enumerate(assignments):
            slices.append({"kind": SLICE_KIND, "ordinal": ordinal, "first_cell": first,
                "stop_cell": stop, "next_cell": first, "accepted_complete_cells": 0, "complete": False,
                "proposal_identity_sha256": proposal_sha, "residual_math_sha256": sources["trial_math"],
                "complete_columns": ROWS, "all_declared_source_components_retained": True,
                "squared_norm_upper_exact_binary64": {name: [float(0).hex()]*ROWS for name in NORM_NAMES}})
    else:
        validate_parallel_metadata(previous, proposal, sources, parallel_source_sha, require_prefix=True)
        seed = copy.deepcopy(previous["seed_prefix"])
        assignments, slices = copy.deepcopy(previous["partition"]), copy.deepcopy(previous["slices"])
    raw_seed = canonical(seed)
    outcomes = []

    def publish():
        count, contiguous, union = whole_sums(c, seed, slices)
        record = {"kind": KIND, "parallel_source_sha256": parallel_source_sha,
            "scientific_sources": dict(sources), "proposal_identity_sha256": proposal_sha,
            "certificate_plan_sha256": proposal["certificate_plan_sha256"],
            "complete_total_cells": seed["total_cells"], "maximum_arithmetic_children": MAX_WORKERS,
            "one_complete_trial_materialization_before_fork": True,
            "new_slice_boundary_conditions_or_trial_jumps": False,
            "all96_columns_and_all5_source_windows_retained": True, "old_scientific_target_calls": 0,
            "seed_prefix": copy.deepcopy(seed),
            "seed_prefix_receipt": {"bytes": len(raw_seed), "sha256": digest(raw_seed)},
            "partition": copy.deepcopy(assignments), "slices": copy.deepcopy(slices),
            "accepted_union_complete_cells": seed["next_cell"]+sum(value["accepted_complete_cells"] for value in slices),
            "contiguous_next_cell": count, "complete": all(value["complete"] for value in slices),
            "contiguous_prefix_receipt": None, "child_outcomes": copy.deepcopy(outcomes)}
        validate_parallel_metadata(record, proposal, sources, parallel_source_sha)
        publish_complete_record(record, count, contiguous, union)
        validate_parallel_metadata(record, proposal, sources, parallel_source_sha, require_prefix=True)
        return record

    record = publish()
    if record["complete"]:
        return record
    directory = Path(private_directory)
    directory.mkdir(parents=True, exist_ok=False)
    ctx = multiprocessing.get_context("fork")
    stop_event = ctx.Event()
    deadline = time.monotonic()+seconds_remaining

    def child(ordinal, original):
        path = directory/("slice-"+str(ordinal)+".json")
        failure_path = directory/("failure-"+str(ordinal)+".json")
        current = copy.deepcopy(original)
        sums = _decode(c, current["squared_norm_upper_exact_binary64"])
        require(current["next_cell"] < current["stop_cell"], "only an unfinished disjoint child starts")

        def commit():
            current["squared_norm_upper_exact_binary64"] = _encode(c, sums)
            current["accepted_complete_cells"] = current["next_cell"]-current["first_cell"]
            current["complete"] = current["next_cell"] == current["stop_cell"]
            validate_slice_metadata(current, assignments[ordinal], ordinal, proposal_sha, sources["trial_math"])
            raw = canonical(current)
            require(len(raw) < 20000, "one whole96/all5 cell slice remains a small scalar record")
            temporary = path.with_suffix(".candidate")
            with temporary.open("wb") as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
            saved = json.loads(temporary.read_bytes())
            require(saved == current, "the entire exact-hex slice saved/read before acceptance")
            restored = _decode(c, saved["squared_norm_upper_exact_binary64"])
            require(all(c.np.array_equal(restored[name].hi, c.upper(sums[name]).hi) for name in NORM_NAMES),
                    "every formal upper is exactly the original finite binary64 endpoint")
            temporary.replace(path)
            require(path.read_bytes() == raw, "the entire formal atomic slice readback")

        try:
            commit()
            for index in range(current["next_cell"], current["stop_cell"]):
                if stop_event.is_set() or time.monotonic() >= deadline:
                    break
                contributions = evaluate_cell(index)
                require(set(contributions) == set(expected_norms(index)) <= set(NORM_NAMES),
                        "all original source components for this exact cell, and no other domain")
                require(all(value.hi.shape == (ROWS,) and c.np.all(c.np.isfinite(value.hi))
                            and c.np.all(value.hi >= 0) for value in contributions.values()),
                        "every complete cell contribution has all96 finite nonnegative uppers")
                # Form ALL updated source components before changing the cursor.
                updates = {name: c.add_upper(sums[name], value) for name, value in contributions.items()}
                sums.update(updates)
                current["next_cell"] = index+1
                if (index+1) % checkpoint_stride == 0 or index+1 == current["stop_cell"]:
                    commit()
            commit()
        except BaseException as error:
            # A failed current cell never advances the cursor. Earlier complete
            # cells can still be saved even if this is not a regular stride.
            try:
                commit()
            except BaseException:
                pass
            payload = {"type": type(error).__name__, "message": str(error)[:1500],
                       "traceback": traceback.format_exc()[-3000:]}
            failure_path.write_bytes(canonical(payload))
            raise

    processes = []
    for ordinal, saved in enumerate(slices):
        if saved["complete"]:
            continue
        process = ctx.Process(target=child, args=(ordinal, saved), daemon=True)
        process.start()
        processes.append((ordinal, process))
    require(len(processes) <= MAX_WORKERS, "no more than3 disjoint arithmetic children")

    def read_updates():
        changed = False
        for ordinal, _ in processes:
            path = directory/("slice-"+str(ordinal)+".json")
            if not path.exists():
                continue
            saved = json.loads(path.read_bytes())
            validate_slice_metadata(saved, assignments[ordinal], ordinal, proposal_sha, sources["trial_math"])
            old = slices[ordinal]
            require(saved["next_cell"] >= old["next_cell"], "accepted complete-cell cursors never regress")
            require(all(float.fromhex(new) >= float.fromhex(previous)
                        for name in NORM_NAMES for new, previous in zip(
                            saved["squared_norm_upper_exact_binary64"][name],
                            old["squared_norm_upper_exact_binary64"][name])),
                    "nonnegative complete source-square sums never decrease")
            if saved != old:
                slices[ordinal] = saved
                changed = True
        return changed

    try:
        while any(process.is_alive() for _, process in processes):
            if read_updates():
                record = publish()
            if time.monotonic() >= deadline:
                stop_event.set()
                break
            time.sleep(0.25)
    finally:
        stop_event.set()
        drain = time.monotonic()+20
        for _, process in processes:
            process.join(timeout=max(0, drain-time.monotonic()))
        for _, process in processes:
            if process.is_alive():
                process.terminate()
        for ordinal, process in processes:
            process.join(timeout=5)
            failure_path = directory/("failure-"+str(ordinal)+".json")
            outcomes.append({"ordinal": ordinal, "actual_exitcode": process.exitcode,
                "failure": json.loads(failure_path.read_bytes()) if failure_path.exists() else None,
                "ended_before_complete_assignment": not slices[ordinal]["complete"]})
        read_updates()
        for outcome in outcomes:
            outcome["ended_before_complete_assignment"] = not slices[outcome["ordinal"]]["complete"]
        record = publish()
    return record
