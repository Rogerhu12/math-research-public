"""R142 exact moment source norms with durable complete-parent scalar prefixes.

Pure arithmetic adapter: no imports, IO, entry point, or scientific execution.
A/B/K are source-independent same-model representations. Every accepted
source prefix covers complete original parents and ALL radial/193-atom
outputs. A restarted owner may materialize A/B/K and the root carry, but
must not call source_moments for an accepted parent/source prefix.
"""
PARENT_COUNT = 155
ATOM_COUNT = 193
SOURCE_ROLES = (
    "ordinary_raw_low_source", "transformed_low_source",
    "true_coefficient_defect", "low_second_kind_correction",
    "centre_high0_return_source",
)
SUM_KEYS = ("body_HS2_upper", "root97_HS2_upper", "outer96_HS2_upper")
PREFIX_KIND = "R142_complete_parent_source_integral_prefix_v1"
CONTRACT = "GM1_through17_exact_whole_cell_covariance_and_two_signed_triangles"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def _roles(roles):
    roles = tuple(roles)
    require(roles and len(set(roles)) == len(roles)
            and all(role in SOURCE_ROLES for role in roles),
            "distinct complete original source roles")
    return roles


def parent_partition(model):
    """Exact consecutive parent cells; no new radial or angular cutoff."""
    require(model.get("comparison_BVP_verified") is True
            and model.get("same_exact_parent_midpoint_model") is True,
            "complete unchanged comparison BVP")
    cells = model["context"].domain.cells
    counts = list(model["refined_plan"]["counts"])
    require(len(counts) == PARENT_COUNT
            and all(type(n) is int and n > 0 for n in counts)
            and sum(counts) == len(cells), "all155 original parent blocks")
    intervals, cursor = [], 0
    for parent, count in enumerate(counts):
        stop = cursor+count
        require(all(cells[i]["parent_panel"] == parent
                    and cells[i]["count"] == count
                    for i in range(cursor, stop)),
                "complete original parent with every genuine refined cell")
        intervals.append((cursor, stop))
        cursor = stop
    return tuple(intervals)


def _nonnegative_upper(api, value):
    require(value.is_finite(), "finite complete scalar upper enclosure")
    result = api.upper(value)
    require(bool(result >= api.zero), "nonnegative complete source-square upper")
    return result


def _state(api, model, roles, parent_count, sums, *, saved):
    partition = parent_partition(model)
    require(type(parent_count) is int and 0 <= parent_count <= PARENT_COUNT,
            "complete parent prefix cursor")
    roles = _roles(roles)
    require(set(sums) == set(roles), "all and only original source-prefix roles")
    values = {}
    for role in roles:
        require(set(sums[role]) == set(SUM_KEYS), "three complete source-square sums")
        values[role] = {key: _nonnegative_upper(api, sums[role][key])
                        for key in SUM_KEYS}
    return {"kind": PREFIX_KIND, "source_roles": roles,
        "complete_original_parent_count": PARENT_COUNT,
        "complete_parent_count": parent_count,
        "complete_refined_cell_count": 0 if not parent_count else partition[parent_count-1][1],
        "complete_model_cell_count": len(model["context"].domain.cells),
        "whole_output_atom_count": ATOM_COUNT,
        "all_real_radial_outputs_in_each_source_slice": True,
        "both_same_cell_signed_triangles_retained": True,
        "moments_contract": CONTRACT,
        "sums": values, "whole_saved_prefix_readback_used": bool(saved),
        "private_model_token": model["private_model_token"]}


def empty_prefix(api, model, roles):
    """Exact empty integrals; this is not evidence of a nonempty computation."""
    roles = _roles(roles)
    return _state(api, model, roles, 0,
                  {role: {key: api.zero for key in SUM_KEYS} for role in roles},
                  saved=True)


def bind_saved_prefix(api, model, roles, saved, *, whole_input_admitted):
    """Rebind a whole published prefix after owner source/manifest admission.

    The owner reads every saved decimal BALL, validates its finite endpoint,
    and passes its directed upper in saved['sums']. This function checks the
    mathematical cursor/schema. It does not turn a count/hash into a norm.
    """
    require(whole_input_admitted is True, "whole previous science/execution/source admitted")
    roles = _roles(roles)
    require(saved["kind"] == PREFIX_KIND
            and tuple(saved["source_roles"]) == roles
            and saved["complete_original_parent_count"] == PARENT_COUNT
            and saved["whole_output_atom_count"] == ATOM_COUNT
            and saved["all_real_radial_outputs_in_each_source_slice"] is True
            and saved["both_same_cell_signed_triangles_retained"] is True
            and saved["moments_contract"] == CONTRACT
            and saved["whole_saved_prefix_readback_used"] is True,
            "whole original complete-source-prefix semantics")
    state = _state(api, model, roles, saved["complete_parent_count"],
                   saved["sums"], saved=True)
    require(saved["complete_refined_cell_count"] == state["complete_refined_cell_count"]
            and saved["complete_model_cell_count"] == state["complete_model_cell_count"],
            "whole saved parent/refinement identity")
    return state


def prepare_shared_outputs_without_source_moments(
        api, km, core, moment, provider, model, prefix, progress=None):
    """Materialize GM.16 A/B/K from Q and comparison Green, with no source V.

    The existing provider's _prepare_parent computes H/Q template U only;
    _prepare_cell computes exactly its OL/OR. Neither _moments, packet,
    model_source_covariance nor source_moments is called.
    """
    parent_partition(model)
    require(provider.model is model and isinstance(prefix, tuple) and prefix,
            "same-model parent provider and distinct private namespace")
    before = provider.statistics["complete_parent_source_covariances_prepared"]
    store = model["private_store"]
    count = len(model["context"].domain.cells)
    keys = {name: prefix+(name,) for name in ("A", "B", "K")}
    or_key = prefix+("temporary_OR",)
    A = km.zeros(api, 97, 97)
    store.put(keys["A"]+(0,), A)
    for i in range(count):
        provider._prepare_parent(i)
        cell = provider._prepare_cell(i)
        require(cell["panel"] == i, "same exact node frame for source-independent output")
        store.put(or_key+(i,), cell["OR"])
        A = core.congruence(api, km, km.transpose(model["Uinv"][i]),
                           moment._add(api, km, A, cell["OL"]))
        store.put(keys["A"]+(i+1,), A)
        A = store.get(keys["A"]+(i+1,))
        if progress is not None and (i % 32 == 31 or i+1 == count):
            progress("source_independent_complete_left_output_covariances",
                     {"cells_complete": i+1, "cells": count,
                      "source_moments_evaluated": 0})
    provider.release_parent()
    B = km.zeros(api, 96, 96)
    K = core.output_gram(api, km, model["outer_atoms"])
    store.put(keys["B"]+(count,), B)
    store.put(keys["K"]+(count,), K)
    K = store.get(keys["K"]+(count,))
    for i in range(count-1, -1, -1):
        Dtranspose = km.transpose(model["Vinv"][i])
        right = core.congruence(api, km, Dtranspose, B)
        B = moment._add(api, km, store.get(or_key+(i,)), right)
        K = core.congruence(api, km, Dtranspose, K)
        store.put(keys["B"]+(i,), B)
        store.put(keys["K"]+(i,), K)
        B, K = store.get(keys["B"]+(i,)), store.get(keys["K"]+(i,))
        if progress is not None and (i % 32 == 0 or i+1 == count):
            progress("source_independent_complete_right_and_outer96_covariances",
                     {"cells_complete": count-i, "cells": count,
                      "source_moments_evaluated": 0})
    store.release(or_key)
    require(provider.statistics["complete_parent_source_covariances_prepared"] == before,
            "no completed source covariance or source moment repeated")
    return {"prefix": prefix, "keys": keys, "cells": count,
        "private_model_token": model["private_model_token"],
        "original_root97_and_outer96_retained": True,
        "source_covariance_or_source_moments_evaluated": False}


def stream_remaining_complete_parents(
        api, km, core, provider, model, shared, state, commit_prefix,
        retain_packet=None, progress=None):
    """Only missing parents are passed to provider.packet.

    commit_prefix must atomically save a complete candidate document, read
    every whole saved ball back, verify containment, then publish the SAME
    bytes as the formal prefix and return _state-shaped directed uppers.
    No parent is accepted merely because its packet/matrix was computed.
    """
    partition = parent_partition(model)
    roles = _roles(state["source_roles"])
    require(state["private_model_token"] is model["private_model_token"]
            and state["whole_saved_prefix_readback_used"] is True
            and shared["private_model_token"] is model["private_model_token"]
            and shared["cells"] == len(model["context"].domain.cells)
            and shared["original_root97_and_outer96_retained"] is True,
            "same complete model, source prefix and full output covariances")
    start = state["complete_parent_count"]
    require(state["complete_refined_cell_count"]
                == (0 if start == 0 else partition[start-1][1]),
            "accepted prefix ends at an exact original parent boundary")
    store, keys = model["private_store"], shared["keys"]
    root_carry = core.output_gram(api, km, model["root_atoms"])
    # This carries the old comparison observation. No source packet or
    # source-square contribution on an accepted parent is re-evaluated.
    for i in range(state["complete_refined_cell_count"]):
        root_carry = core.congruence(api, km, km.transpose(model["Uinv"][i]), root_carry)
        if progress is not None and (i % 64 == 63
                                    or i+1 == state["complete_refined_cell_count"]):
            progress("same_comparison_root97_carry_materialization",
                     {"cells_materialized": i+1,
                      "accepted_source_moments_recomputed": 0})
    for parent in range(start, PARENT_COUNT):
        first, stop = partition[parent]
        sums = {role: dict(state["sums"][role]) for role in roles}
        for i in range(first, stop):
            left = store.get(keys["A"]+(i,))
            right = core.congruence(api, km, km.transpose(model["Vinv"][i]),
                                    store.get(keys["B"]+(i+1,)))
            outer_carry = store.get(keys["K"]+(i,))
            for role in roles:
                packet = provider.packet(i, role)
                require(packet["panel"] == i and packet["source_role"] == role
                        and packet["private_model_token"] is model["private_model_token"]
                        and packet["same_panel_both_triangles_in_signed_complete_sum"] is True
                        and packet["whole_cell_covariance_moment_contract"] == "R141_GM1_through17"
                        and packet["true_cell_length_retained"] is True
                        and packet["varying_source_was_treated_as_constant"] is False,
                        "complete original whole-source moment packet")
                integral = packet["totals"]
                sums[role]["body_HS2_upper"] += (
                    core.positive_upper(api, core.trace_product(api, left, integral["IL"]))
                    +core.positive_upper(api, core.trace_product(api, right, integral["IR"]))
                    +packet["same_panel_complete_HS2_upper"])
                sums[role]["root97_HS2_upper"] += core.positive_upper(
                    api, core.trace_product(api, root_carry, integral["IL"]))
                sums[role]["outer96_HS2_upper"] += core.positive_upper(
                    api, core.trace_product(api, outer_carry, integral["IR"]))
                if retain_packet is not None:
                    retain_packet(role, packet)
            root_carry = core.congruence(api, km, km.transpose(model["Uinv"][i]), root_carry)
            if progress is not None:
                progress("unaccepted_current_parent_source_cells",
                         {"original_parent": parent, "cells_complete_in_parent": i-first+1,
                          "cells_in_parent": stop-first,
                          "accepted_parent_prefix": state["complete_parent_count"]})
        candidate = _state(api, model, roles, parent+1, sums, saved=False)
        saved = commit_prefix(candidate)
        require(saved["private_model_token"] is model["private_model_token"]
                and saved["whole_saved_prefix_readback_used"] is True
                and saved["kind"] == PREFIX_KIND
                and tuple(saved["source_roles"]) == roles
                and saved["complete_parent_count"] == parent+1
                and saved["complete_refined_cell_count"] == stop,
                "whole candidate read back before advancing the accepted cursor")
        for key in ("complete_original_parent_count", "complete_model_cell_count",
                    "whole_output_atom_count", "all_real_radial_outputs_in_each_source_slice",
                    "both_same_cell_signed_triangles_retained", "moments_contract"):
            require(saved[key] == candidate[key], "unchanged complete prefix metadata: "+key)
        checked = _state(api, model, roles, parent+1, saved["sums"], saved=True)
        for role in roles:
            for key in SUM_KEYS:
                require(bool(checked["sums"][role][key] >= candidate["sums"][role][key]),
                        "saved upper contains each complete accumulated source square")
        state = checked
        provider.release_parent()
        if progress is not None:
            progress("accepted_complete_parent_source_prefix",
                     {"complete_parents": parent+1, "parents": PARENT_COUNT,
                      "complete_refined_cells": stop,
                      "complete_source_roles": list(roles)})
    return state


def complete_norms_from_saved_prefix(api, core, moment, model, shared, state):
    """Six whole norm bounds follow only after all155 source slices exist."""
    require(state["private_model_token"] is model["private_model_token"]
            and state["complete_parent_count"] == PARENT_COUNT
            and state["complete_refined_cell_count"] == len(model["context"].domain.cells)
            and state["whole_saved_prefix_readback_used"] is True,
            "entire radial source domain saved and read back")
    result = {}
    for role in _roles(state["source_roles"]):
        body, root, outer = (state["sums"][role][key] for key in SUM_KEYS)
        value = {"source_role": role, "private_model_token": model["private_model_token"],
            "body_HS2_upper": body, "root97_HS2_upper": root, "outer96_HS2_upper": outer,
            "body_norm_upper": core.positive_upper(api, api.sqrt(body)),
            "atoms193_norm_upper": core.positive_upper(api, api.sqrt(root+outer)),
            "complete_norm_upper": core.positive_upper(api, api.sqrt(body+root+outer)),
            "complete_refined_cells": len(model["context"].domain.cells),
            "complete_parent_source_prefix_saved": True,
            "root97_stream_shared_by_all_batch_roles": True}
        if shared is not None:
            require(shared["private_model_token"] is model["private_model_token"],
                    "same optional complete point-output covariances")
            store, keys, count = model["private_store"], shared["keys"], shared["cells"]
            value["private_output_left_covariances"] = moment._StoredSequence(
                store, keys["A"], count+1)
            value["private_output_right_covariances"] = moment._StoredSequence(
                store, keys["B"], count+1)
        result[role] = value
    return result
