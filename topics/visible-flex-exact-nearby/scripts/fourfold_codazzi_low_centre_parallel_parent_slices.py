"""Complete-source slices sharing one already materialized Green model.

No numerical imports or work at import.  The directed owner supplies all
arithmetic.  Source intervals are disjoint; every interval retains the full
radial output and all193 atoms.  Small scalar slice states are restartable.
The optional Linux fork runner shares private matrix pages without writing
any matrix or array to disk, an artifact, or the repository.
"""

KIND = "R142_disjoint_complete_parent_source_slice_v1"
UNION_KIND = "R142_disjoint_parent_source_slice_partition_v1"
PARENT_COUNT = 155
ATOM_COUNT = 193
SUM_KEYS = ("body_HS2_upper", "root97_HS2_upper", "outer96_HS2_upper")
CONTRACT = "GM1_through17_exact_whole_cell_covariance_and_two_signed_triangles"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def validate_slice_metadata(record, counts, roles):
    """Only integer/schema checks; saved scalar balls are decoded by owner."""
    require(record["kind"] == KIND and record["source_roles"] == list(roles)
            and record["complete_original_parent_count"] == PARENT_COUNT
            and len(counts) == PARENT_COUNT
            and all(type(n) is int and n > 0 for n in counts)
            and record["complete_model_cell_count"] == sum(counts)
            and record["whole_output_atom_count"] == ATOM_COUNT
            and record["all_real_radial_outputs_in_each_source_slice"] is True
            and record["both_same_cell_signed_triangles_retained"] is True
            and record["moments_contract"] == CONTRACT
            and record["whole_saved_slice_readback_used"] is True,
            "same complete source-slice semantics")
    first, stop, accepted = (record[key] for key in
                            ("first_parent", "stop_parent", "accepted_until_parent"))
    require(all(type(n) is int for n in (first, stop, accepted))
            and 0 <= first <= accepted <= stop <= PARENT_COUNT
            and record["accepted_parent_count"] == accepted-first
            and record["accepted_refined_cell_count"] == sum(counts[first:accepted])
            and record["complete"] == (accepted == stop)
            and set(record["sums"]) == set(roles)
            and all(set(record["sums"][role]) == set(SUM_KEYS) for role in roles),
            "exact original-parent source slice and accepted cursor")
    return first, stop, accepted


def balanced_partition(counts, first, workers=3, parent_weight=64):
    """Integer-only scheduling; no interval or source estimate is changed."""
    require(len(counts) == PARENT_COUNT and all(type(n) is int and n > 0 for n in counts)
            and type(first) is int and 0 <= first <= PARENT_COUNT
            and type(workers) is int and 1 <= workers <= 3
            and type(parent_weight) is int and parent_weight >= 0,
            "bounded complete-parent scheduling parameters")
    if first == PARENT_COUNT:
        return []
    workers = min(workers, PARENT_COUNT-first)
    weights = [parent_weight+n for n in counts]
    total = sum(weights[first:])
    boundaries, cursor, accumulated = [first], first, 0
    for part in range(1, workers):
        last_allowed = PARENT_COUNT-(workers-part)
        while cursor < last_allowed and accumulated*workers < total*part:
            accumulated += weights[cursor]
            cursor += 1
        cursor = max(cursor, boundaries[-1]+1)
        boundaries.append(cursor)
    boundaries.append(PARENT_COUNT)
    return list(zip(boundaries, boundaries[1:]))


def validate_partition(records, counts, first, roles):
    cursor = first
    accepted = 0
    for record in records:
        left, right, end = validate_slice_metadata(record, counts, roles)
        require(left == cursor and left < right, "disjoint consecutive complete-parent blocks")
        cursor = right
        accepted += end-left
    require(cursor == PARENT_COUNT, "every remaining source parent belongs to exactly one block")
    return accepted


def _state(api, model, roles, first, stop, accepted, sums, saved):
    counts = list(model["refined_plan"]["counts"])
    state = {"kind": KIND, "source_roles": list(roles),
        "complete_original_parent_count": PARENT_COUNT,
        "complete_model_cell_count": len(model["context"].domain.cells),
        "whole_output_atom_count": ATOM_COUNT,
        "first_parent": first, "stop_parent": stop,
        "accepted_until_parent": accepted,
        "accepted_parent_count": accepted-first,
        "accepted_refined_cell_count": sum(counts[first:accepted]),
        "complete": accepted == stop,
        "all_real_radial_outputs_in_each_source_slice": True,
        "both_same_cell_signed_triangles_retained": True,
        "moments_contract": CONTRACT,
        "whole_saved_slice_readback_used": bool(saved),
        "sums": {role: {} for role in roles},
        "private_model_token": model["private_model_token"]}
    for role in roles:
        require(set(sums[role]) == set(SUM_KEYS), "three whole source-square bounds")
        for key in SUM_KEYS:
            value = sums[role][key]
            require(value.is_finite() and bool(api.upper(value) >= api.zero),
                    "finite nonnegative directed source-square upper")
            state["sums"][role][key] = api.upper(value)
    if saved:
        validate_slice_metadata(state, counts, roles)
    return state


def empty_slice(api, model, roles, first, stop):
    return _state(api, model, roles, first, stop, first,
                  {role: {key: api.zero for key in SUM_KEYS} for role in roles}, True)


def bind_saved_slice(api, model, roles, saved, *, whole_input_admitted):
    require(whole_input_admitted is True, "whole prior model and complete scalar slice admitted")
    counts = list(model["refined_plan"]["counts"])
    first, stop, accepted = validate_slice_metadata(saved, counts, roles)
    return _state(api, model, roles, first, stop, accepted, saved["sums"], True)


def integrate_remaining_slice(api, km, core, provider, model, shared, stream_math,
                              state, commit_slice, progress=None):
    """PS.6--7 over only the unaccepted part of one source block.

    Every A/B/K is the existing whole-output covariance.  The root carry is
    a source-independent observation and may be materialized to the slice's
    first unaccepted cell.  No earlier source packet is evaluated.
    """
    require(provider.model is model
            and state["private_model_token"] is model["private_model_token"]
            and shared["private_model_token"] is model["private_model_token"]
            and state["whole_saved_slice_readback_used"] is True
            and shared["cells"] == len(model["context"].domain.cells)
            and shared["original_root97_and_outer96_retained"] is True,
            "same complete Green and all physical output covariances")
    roles = tuple(state["source_roles"])
    partition = stream_math.parent_partition(model)
    counts = list(model["refined_plan"]["counts"])
    first, stop, accepted = validate_slice_metadata(state, counts, roles)
    if accepted == stop:
        return state
    store, keys = model["private_store"], shared["keys"]
    root_carry = core.output_gram(api, km, model["root_atoms"])
    for i in range(partition[accepted][0]):
        root_carry = core.congruence(api, km, km.transpose(model["Uinv"][i]), root_carry)
        if progress is not None and i % 64 == 63:
            progress("source_independent_root_carry", {"cells": i+1})
    for parent in range(accepted, stop):
        left_cell, right_cell = partition[parent]
        sums = {role: dict(state["sums"][role]) for role in roles}
        for i in range(left_cell, right_cell):
            left = store.get(keys["A"]+(i,))
            right = core.congruence(api, km, km.transpose(model["Vinv"][i]),
                                    store.get(keys["B"]+(i+1,)))
            outer = store.get(keys["K"]+(i,))
            for role in roles:
                packet = provider.packet(i, role)
                require(packet["panel"] == i and packet["source_role"] == role
                        and packet["private_model_token"] is model["private_model_token"]
                        and packet["same_panel_both_triangles_in_signed_complete_sum"] is True
                        and packet["whole_cell_covariance_moment_contract"] == "R141_GM1_through17"
                        and packet["true_cell_length_retained"] is True
                        and packet["varying_source_was_treated_as_constant"] is False,
                        "same full variable-source packet and both signed triangles")
                integral = packet["totals"]
                sums[role]["body_HS2_upper"] += (
                    core.positive_upper(api, core.trace_product(api, left, integral["IL"]))
                    +core.positive_upper(api, core.trace_product(api, right, integral["IR"]))
                    +packet["same_panel_complete_HS2_upper"])
                sums[role]["root97_HS2_upper"] += core.positive_upper(
                    api, core.trace_product(api, root_carry, integral["IL"]))
                sums[role]["outer96_HS2_upper"] += core.positive_upper(
                    api, core.trace_product(api, outer, integral["IR"]))
            root_carry = core.congruence(api, km, km.transpose(model["Uinv"][i]), root_carry)
            if progress is not None and i+1 != right_cell:
                progress("unaccepted_source_cell", {"parent": parent, "cell": i})
        candidate = _state(api, model, roles, first, stop, parent+1, sums, False)
        saved = commit_slice(candidate)
        checked = bind_saved_slice(api, model, roles, saved, whole_input_admitted=True)
        require(checked["first_parent"] == first and checked["stop_parent"] == stop
                and checked["accepted_until_parent"] == parent+1,
                "one newly complete original parent accepted")
        for role in roles:
            for key in SUM_KEYS:
                require(bool(checked["sums"][role][key] >= candidate["sums"][role][key]),
                        "saved complete slice upper encloses every accumulated square")
        state = checked
        provider.release_parent()
        if progress is not None:
            progress("accepted_source_parent", {"parent": parent, "accepted_until": parent+1})
    return state


def union_complete_slices(api, stream_math, model, initial_prefix, slices):
    """Add exact disjoint source domains; no Green/source evaluation occurs."""
    roles = tuple(initial_prefix["source_roles"])
    counts = list(model["refined_plan"]["counts"])
    require(initial_prefix["private_model_token"] is model["private_model_token"]
            and initial_prefix["whole_saved_prefix_readback_used"] is True,
            "the unchanged admitted old whole source prefix")
    start = initial_prefix["complete_parent_count"]
    validate_partition(slices, counts, start, roles)
    require(all(record["complete"] for record in slices), "all assigned source intervals complete")
    sums = {role: dict(initial_prefix["sums"][role]) for role in roles}
    for record in slices:
        require(record["private_model_token"] is model["private_model_token"],
                "all source slices refer to the same exact Green")
        for role in roles:
            for key in SUM_KEYS:
                sums[role][key] = api.upper(sums[role][key]+record["sums"][role][key])
    return stream_math._state(api, model, roles, PARENT_COUNT, sums, saved=True)


def fork_remaining_slices(api, km, core, moment, parent_math, model, shared,
                          stream_math, initial_prefix, previous_slices,
                          encode_scalar, decode_scalar, publish_slices,
                          *, private_directory, seconds_remaining,
                          workers=3, parent_weight=64, degree=24):
    """One materialization, at most three disjoint-source arithmetic children.

    publish_slices receives COMPLETE JSON-compatible scalar records only.
    It must save them in the owner's formal outcome before it returns.
    Children save an entire accepted parent before observing the stop flag.
    This routine must only run inside the public scientific owner, after
    readonly admission and directed runtime selection.
    """
    import json
    import multiprocessing
    import os
    import sys
    import time
    from pathlib import Path
    require(sys.platform.startswith("linux") and os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public",
            "Linux public own-Actions scientific process")
    require(1 <= workers <= 3 and seconds_remaining > 0, "bounded shared-memory arithmetic batch")
    roles = tuple(initial_prefix["source_roles"])
    counts = list(model["refined_plan"]["counts"])
    start = initial_prefix["complete_parent_count"]

    def public(state):
        record = {key: value for key, value in state.items()
                  if key not in ("sums", "private_model_token")}
        record["sums"] = {role: {key: encode_scalar(state["sums"][role][key])
                                for key in SUM_KEYS} for role in roles}
        record["whole_saved_slice_readback_used"] = True
        return record

    def decode(record):
        validate_slice_metadata(record, counts, roles)
        saved = dict(record)
        saved["sums"] = {role: {key: api.upper(decode_scalar(record["sums"][role][key]))
                               for key in SUM_KEYS} for role in roles}
        return bind_saved_slice(api, model, roles, saved, whole_input_admitted=True)

    if previous_slices is None:
        records = [public(empty_slice(api, model, roles, a, b))
                   for a, b in balanced_partition(counts, start, workers, parent_weight)]
    else:
        records = list(previous_slices)
    validate_partition(records, counts, start, roles)
    require(len(records) <= workers, "at most the declared private arithmetic workers")
    # Validate all complete saved balls before any fork and preserve them in
    # the main outcome, even if no new child can start within the wall cap.
    for record in records:
        decode(record)
    publish_slices(records)
    if all(record["complete"] for record in records):
        return [decode(record) for record in records]
    directory = Path(private_directory)
    directory.mkdir(parents=True, exist_ok=True)
    require(not any(directory.iterdir()), "fresh private scalar-only run directory")
    ctx = multiprocessing.get_context("fork")
    stop_event = ctx.Event()
    deadline = time.monotonic()+seconds_remaining

    def canonical(value):
        return (json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)+"\n").encode()

    def child(index, record):
        path = directory/("slice-"+str(index)+".json")
        error_path = directory/("error-"+str(index)+".json")
        # The parent's decoded cache is disposable.  No packed entry in
        # the inherited same-model store is modified by any child.
        store = model["private_store"]
        store.cache.clear()
        store.decoded_entries = 0
        provider = parent_math.ParentMomentProvider(api, km, core, moment, model, degree=degree)

        def commit(state):
            result = public(state)
            raw = canonical(result)
            require(len(raw) < 16000, "one small complete scalar slice")
            temporary = path.with_suffix(".candidate")
            with temporary.open("wb") as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
            saved = json.loads(temporary.read_bytes())
            require(saved == result, "complete candidate scalar slice read back")
            for role in roles:
                for key in SUM_KEYS:
                    require(decode_scalar(saved["sums"][role][key]).contains(state["sums"][role][key]),
                            "serialized complete slice contains each directed square")
            temporary.replace(path)
            return decode(saved)

        def progress(stage, detail):
            require(not stop_event.is_set() and time.monotonic() <= deadline,
                    "bounded disjoint-source arithmetic child; saved parents retained")

        try:
            state = decode(record)
            # Preserve the prior slice unchanged before beginning a source
            # packet.  Initial zero-length slices are exact empty integrals.
            state = commit(state)
            integrate_remaining_slice(api, km, core, provider, model, shared, stream_math,
                                      state, commit, progress=progress)
        except BaseException as error:
            raw = canonical({"type": type(error).__name__, "message": str(error)[:1500]})
            error_path.write_bytes(raw)
            raise

    processes = []
    for index, record in enumerate(records):
        if record["complete"]:
            continue
        process = ctx.Process(target=child, args=(index, record), daemon=True)
        process.start()
        processes.append((index, process))

    def read_updates():
        changed = False
        for index, _ in processes:
            path = directory/("slice-"+str(index)+".json")
            if not path.exists():
                continue
            record = json.loads(path.read_bytes())
            decode(record)
            old = records[index]
            require(record["first_parent"] == old["first_parent"]
                    and record["stop_parent"] == old["stop_parent"]
                    and record["accepted_until_parent"] >= old["accepted_until_parent"],
                    "same source slice only advances at complete parent boundaries")
            if record != old:
                records[index] = record
                changed = True
        if changed:
            publish_slices(records)

    try:
        while any(process.is_alive() for _, process in processes):
            read_updates()
            if time.monotonic() >= deadline:
                stop_event.set()
                break
            time.sleep(0.2)
    finally:
        stop_event.set()
        # Child arithmetic can be inside one matrix call.  Allow one short
        # drain, then retain its last atomic complete scalar parent state.
        drain_deadline = time.monotonic()+20
        for _, process in processes:
            process.join(timeout=max(0, drain_deadline-time.monotonic()))
        for _, process in processes:
            if process.is_alive():
                process.terminate()
        for _, process in processes:
            process.join(timeout=5)
        read_updates()
        publish_slices(records)
    require(all(record["complete"] for record in records),
            "parallel source batch incomplete; all complete scalar slices retained")
    return [decode(record) for record in records]
