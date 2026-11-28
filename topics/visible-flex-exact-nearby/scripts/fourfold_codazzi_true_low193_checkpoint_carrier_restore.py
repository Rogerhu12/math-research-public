"""Necessary whole TF46120139018/1 carrier restoration, not a second proof run.

The complete 81 accepted records are copied from the immutable outcome.
The original matrices are usable ONLY after the whole packed-prefix hash,
whole canonical checkpoint hash and whole gzip hash all match that outcome.
No old source-map norm, HS target, signed trace or old owner is invoked.
Numerical imports and calls are restricted to the new public owner.
"""
from __future__ import annotations
import copy
import gzip
import hashlib
import json
import os
import platform
import sys
from pathlib import Path

RUN, ATTEMPT, PREFIX = "46120139018", "1", 81
ACTUAL_SHA = "5f1b15db26e603d9718ca9798ec704cc081b5b64d3ff22ff3cfcaaded030d65d"
EXECUTION_SHA = "2dbb23e378379a185e7e8abce731d87dc77881e585742c67849d5f95dfbc087a"
MANIFEST_SHA = "9bee97cd5e7a16d6535184ab0bfdd32c6c4c3ee14be32084a5ec6ed33ed84d13"
RAW_SHA = "3916928e630d814f8ec7e0d22b1470d0a9caa4f34150d1d7ccef8f185843d105"
GZIP_SHA = "c0718447c4ef8e8d50c11561eb24947903090a5db2306223ec56399ba4629f33"
PREFIX_SHA = "0be16da1dc652f830389b496eb87bb300a07dddcb564167fdbf9ef650b9ea8b6"
ROLES = ("ordinary_raw_low_source", "transformed_low_source",
         "low_second_kind_correction", "centre_high0_return_source")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def admit_complete_original(actual_raw, execution_raw, manifest_raw):
    """Metadata only. This does not turn the incomplete TF target into a proof."""
    require((len(actual_raw), sha(actual_raw)) == (57359, ACTUAL_SHA)
            and (len(execution_raw), sha(execution_raw)) == (63045, EXECUTION_SHA)
            and sha(manifest_raw) == MANIFEST_SHA, "three whole immutable original TF files")
    actual, execution, manifest = map(json.loads, (actual_raw, execution_raw, manifest_raw))
    require(actual["run_id"] == execution["run_id"] == RUN
            and actual["run_attempt"] == execution["run_attempt"] == ATTEMPT
            and actual["manifest_sha256"] == execution["manifest_sha256"] == MANIFEST_SHA
            and actual["kind"] == "complete_R149_true_low193_direct_flow_and_source_maps_v1"
            and actual["complete"] is actual["proved"] is False
            and execution["scientific_complete"] is False
            and actual["actual_returncode"] == execution["actual_child_returncode"] == 1
            and execution["child_timeout"] is False,
            "the original actual finite-pivot failure, not a successful inverse")
    require(actual["complete_current_file_receipts"] == execution["current_input_receipts"]
                == manifest["files"]
            and actual["scientific_modules"] == manifest["operation"]["scientific_module_binding"]
            and actual["certificate_parameters"] == manifest["operation"]["certificate_parameters"]
            and actual["parameters"] == manifest["parameters"]
            and actual["completed_targets"] == execution["completed_target_names"] == []
            and [x["name"] for x in actual["gates"]]
                == manifest["operation"]["complete_gate_names"][:21]
            and all(x["passed"] is True for x in actual["gates"]),
            "all original inputs, sources, parameters and exact accepted scope")
    ledger = actual["certificate"]["finite_pivots"]
    require(ledger["completed"] == PREFIX and len(ledger["left97"]) == PREFIX
            and ledger["right96"] == ledger["node_transversality"] == []
            and ledger["in_progress"]["phase"] == "left97"
            and ledger["in_progress"]["index"] == PREFIX
            and actual["failure"]["type"] == "ActualPivotFailure"
            and actual["failure"]["message"] == "actual left97 pivot 81: matrix is singular"
            and actual["certificate"]["true_model"] is None
            and actual["certificate"]["sources"] == {}, "all81 and only81 original accepted pivots")
    chain = hashlib.sha256(b"true_low193_pivots_v1").digest()
    for i, exponent in enumerate(ledger["left97"]):
        require(type(exponent) is int, "one original exact inverse-bound exponent")
        record = dict(phase="left97", index=i, dimension=97, inverse_norm_power2=exponent)
        chain = hashlib.sha256(chain+canonical(record)).digest()
    require(chain.hex() == ledger["whole_ordered_record_chain_sha256"],
            "whole accepted-prefix chronological ledger")
    checkpoint = actual["certificate"]["private_failure_checkpoint"]
    require(checkpoint["uncompressed_sha256"] == RAW_SHA
            and checkpoint["compressed_sha256"] == GZIP_SHA
            and checkpoint["whole_retained_private_prefix_sha256"] == PREFIX_SHA
            and checkpoint["uncompressed_bytes"] == 4955126
            and checkpoint["compressed_bytes"] == 842453
            and checkpoint["complete_private_payload_durable_after_runner_exit"] is False
            and checkpoint["arrays_published_to_git_Release_or_artifact"] is False,
            "complete original nondurable checkpoint identities")
    progress = actual["actual_progress"]
    require(progress["actual_left_cells_complete"] == PREFIX
            and progress["actual_right_cells_complete"] == progress["actual_source_cells_complete"] == 0
            and progress["new_targets_completed"] == progress["old_completed_targets_recomputed"] == 0
            and [x["new_cuts"] for x in progress["local_current_cell_refinements"]] == [8,16,32,64]
            and all(x["cell"] == PREFIX and x["previous_successful_cells_recomputed"] == 0
                    for x in progress["local_current_cell_refinements"]),
            "only the original failed current cell was refined")
    return {"actual": actual, "execution": execution, "manifest": manifest,
            "new_scientific_targets_evaluated": 0,
            "whole_prefix_carrier_not_yet_restored": True}


def check_original_module(module, role, manifest):
    spec = next(x for x in manifest["files"] if x["role"] == role)
    raw = Path(module.__file__).read_bytes()
    require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
            and hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
                == spec["git_blob_sha"], "unchanged whole original carrier definition: "+role)


def original_scalar(value):
    require(value.is_finite(), "finite original complete scalar carrier")
    mid, rad, exponent = value.mid_rad_10exp(48)
    return {"kind": "complete_decimal_ball_v1", "midpoint_integer": str(int(mid)),
            "radius_integer": str(int(rad)), "decimal_exponent": str(int(exponent)),
            "semantics": "the exact directed scalar lies in (midpoint +/- radius)*10^exponent"}


def packed_prefix_sha(store):
    chain = hashlib.sha256(b"true_low193_complete_private_packed_state_v1")
    for key in sorted(store.data):
        rows, cols, payload = store.data[key]
        chain.update(canonical({"key": key, "rows": rows, "cols": cols,
            "native_array_byte_order": sys.byteorder,
            "payload_bytes": len(payload)*payload.itemsize}))
        chain.update(payload.tobytes())
    return chain.hexdigest()


def restore_whole_prefix(api, flint, km, green, refined, flow, context, provider,
                         chart_specs, balances, admitted, private_directory,
                         progress=None):
    """Restore ONLY old necessary carriers; return after all three whole hashes.

    The caller prepared the original context at320bit, then the original
    refined context, charts and child provider at384bit, exactly as TF did.
    The old accepted records are never regenerated. Numerical inversion in
    the formula is carrier arithmetic; it creates no second accepted record.
    The new post81 owner must call its own genuinely different graph math.
    """
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public",
            "necessary numerical restoration only in own public Actions")
    require(platform.python_version() == "3.12.14" and flint.__version__ == "0.9.0"
            and flint.ctx.prec == 384 and sys.byteorder == "little"
            and platform.machine() == "x86_64"
            and all(os.environ.get(key) == "1" for key in
                    ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")),
            "the complete original deterministic runtime and directed packing")
    actual, manifest = admitted["actual"], admitted["manifest"]
    for module, role in ((km,"kernel_math"), (green,"low_centre_verified_green_math"),
                         (refined,"low_centre_refined_green_math"),
                         (flow,"true_low193_direct_flow_math")):
        check_original_module(module, role, manifest)
    require(context.reference_identity == actual["reference_identity"]
            and provider.context is context and len(context.domain.cells) == 1424
            and len(chart_specs) == 1425 and len(balances) == 155
            and all(context.domain.cells[i] == dict(parent_panel=i, slice=0, count=1)
                    for i in range(PREFIX+1)), "the exact original prefix domain and charts")
    store = refined.PackedMatrices(api, km, maximum_bytes=8589934592,
                                  maximum_decoded_entries=200000)
    # Passive copies of the raw local flows already formed by the necessary
    # recipe. They do not enter or change the original packed-prefix hash.
    # New graph algebra may consume these without reintegrating an old cell.
    raw_flows = refined.PackedMatrices(api, km, maximum_bytes=536870912,
                                      maximum_decoded_entries=200000)
    ix, iy = tuple(range(97)), tuple(range(97,193))
    Z = km.zeros(api,96,97)
    store.put(("true_temporary","Z",0),Z)
    local_statistics = []
    for i in range(PREFIX):
        chart = refined._chart(api,chart_specs[i],first=i == 0)
        next_chart = refined._chart(api,chart_specs[i+1])
        cuts = [context.domain.fone*j/4 for j in range(5)]
        local = flow.true_cell_packet(api,km,context,provider,i,cuts,balances[i],24,
                                      source_roles=ROLES)
        raw_flows.put(("restored_raw_forward",i),local["forward"])
        raw_flows.put(("restored_raw_backward",i),local["backward"])
        forward = refined.chart_left(api,km,next_chart,
            refined.chart_right(api,km,local["forward"],chart),inverse=True)
        backward = refined.chart_left(api,km,chart,
            refined.chart_right(api,km,local["backward"],next_chart),inverse=True)
        aa,ab = green.submatrix(km,forward,ix,ix),green.submatrix(km,forward,ix,iy)
        ba,bb = green.submatrix(km,forward,iy,ix),green.submatrix(km,forward,iy,iy)
        # Necessary exact original formula only: no observer, norm target,
        # old inverse exponent calculation or second scientific acceptance.
        inverse = green.directed_inverse(api,km,km.add(api,aa,km.multiply(api,ab,Z)))
        Z = km.multiply(api,km.add(api,ba,km.multiply(api,bb,Z)),inverse)
        store.put(("model","C",i),inverse)
        store.put(("true_temporary","backward",i),backward)
        store.put(("true_temporary","Z",i+1),Z)
        Z = store.get(("true_temporary","Z",i+1))
        store.put(("true_moment","output",i),local["true_moments"]["output"])
        for role in ROLES:
            store.put(("true_moment",role,i),local["true_moments"]["inputs"][role])
        local_statistics.append({key:local[key] for key in
            ("panel","subboxes","beta_sum_upper","beta2_sum_upper",
             "complete_raw_prefix_and_inverse_upper","largest_local_tail_upper")})
        if progress is not None:
            progress("necessary_original_TF_carrier_restoration", {
                "original_cells_restored":i+1,"required_original_cells":PREFIX,
                "original_accepted_records_copied":PREFIX,"new_old_target_records":0})
    require(store.metadata()["live_payload_bytes"] == 314059632
            and store.metadata()["entries_packed"] == 19628727
            and packed_prefix_sha(store) == PREFIX_SHA,
            "every original matrix, moment, key and packed entry matches the WHOLE old prefix")

    # Only the last failed candidate is needed for the full checkpoint SHA.
    # Its old4/8/16/32 failed attempts are neither inputs nor rerun targets.
    i = PREFIX
    chart,next_chart = refined._chart(api,chart_specs[i]),refined._chart(api,chart_specs[i+1])
    cuts = [context.domain.fone*j/64 for j in range(65)]
    local = flow.true_cell_packet(api,km,context,provider,i,cuts,balances[i],24,
                                  source_roles=ROLES)
    forward = refined.chart_left(api,km,next_chart,
        refined.chart_right(api,km,local["forward"],chart),inverse=True)
    aa,ab = green.submatrix(km,forward,ix,ix),green.submatrix(km,forward,ix,iy)
    failed_matrix = km.add(api,aa,km.multiply(api,ab,Z))
    matrices = {"last_attempted_actual_pivot":failed_matrix,
                "last_retained_complete_Z_at_node_81":Z}
    checkpoint = {"kind":"private_complete_true_low193_failure_state_v1",
        "manifest_sha256":MANIFEST_SHA,"run_id":RUN,"run_attempt":ATTEMPT,
        "finite_pivots":copy.deepcopy(actual["certificate"]["finite_pivots"]),
        "preparation_prefix":copy.deepcopy(actual["preparation_prefix"]),
        "matrices":{name:{"rows":value.rows,"cols":value.cols,
            "whole_decimal_balls":[[original_scalar(entry) for entry in row]
                                    for row in value.values]}
                    for name,value in matrices.items()}}
    raw = canonical(checkpoint)
    compressed = gzip.compress(raw,mtime=0)
    require((len(raw),sha(raw)) == (4955126,RAW_SHA)
            and (len(compressed),sha(compressed)) == (842453,GZIP_SHA),
            "both WHOLE original checkpoint hashes, never a selected submatrix or regenerated identity")
    destination = Path(private_directory)
    destination.mkdir(parents=True,exist_ok=True)
    path = destination/"private-true-low193-failed-matrix-and-last-Z.json.gz"
    require(not path.exists(),"one privately restored whole original checkpoint")
    path.write_bytes(compressed)
    require(path.read_bytes() == compressed and gzip.decompress(path.read_bytes()) == raw,
            "whole restored carrier saved and read back")
    return {"kind":"TF_complete_original81_carrier_restoration_v1",
        "private_store":store,"restored_Z81":Z,"last_failed_matrix":failed_matrix,
        "passively_saved_raw_flows":raw_flows,
        "local_statistics":local_statistics,"first_uncompleted_cell":PREFIX,
        "copied_original_pivot_ledger":copy.deepcopy(actual["certificate"]["finite_pivots"]),
        "receipt":{"whole_original_actual_sha256":ACTUAL_SHA,
            "whole_original_execution_sha256":EXECUTION_SHA,
            "whole_original_manifest_sha256":MANIFEST_SHA,
            "whole_packed_prefix_sha256":PREFIX_SHA,
            "whole_checkpoint_raw_sha256":RAW_SHA,"whole_checkpoint_gzip_sha256":GZIP_SHA,
            "passive_raw_flow_whole_payload_sha256":packed_prefix_sha(raw_flows),
            "passive_raw_flows_are_derived_carriers_not_original_accepted_records":True,
            "original_accepted_pivots_copied":PREFIX,"new_old_target_records":0,
            "old_complete_source_maps_HS_or_signed_trace_called":False,
            "failed_current_inverse_called":False,"private_arrays_published":False,
            "actual_low_hybrid_inverse_proved":False}}
