#!/usr/bin/env python3
"""Bind one accepted tail packet to its original mean chain and shared-R map.

No solve is performed. Large native records, stage arrays, and unique-node
indices remain on the runner. An unscaled reference H is not a coupled prefix
certificate or a claim of exact/full surface closure.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
from pathlib import Path
import struct
import subprocess
import sys
import time

from seam_cut_height_compatibility import load_packet


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[1]
HELPER_SHAS = {
    "extract_q060_native_mean_chain.py":
        "51edadb5ca1e2a6c36369c7965788065ff79ab44ce21a219c6d36e3aae896945",
    "export_q060_shared_r_tail_batch.mjs":
        "379848293df82db3125707a07864f4d8a1ce452f82947a84815c3d788fe64f27",
}


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    return {"path": str(Path(path).resolve()), "sha256": sha(path)}


def checked(reference):
    if sha(reference["path"]) != reference["sha256"]:
        raise ValueError("Bound runtime input changed: " + reference["path"])
    return read(reference["path"])


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     allow_nan=False).encode()).hexdigest()


def write(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def fresh_dir(path):
    path = Path(path).resolve()
    repo = TOPIC.parents[1]
    if path == repo or repo in path.parents:
        raise ValueError("Native/stage arrays must remain outside git")
    path.mkdir(parents=True, exist_ok=False)
    return path


def bind_height(packet, reference_path, key, factor, arithmetic):
    source, value = read(reference_path), None
    value = source
    for part in key.split("."):
        value = value[part]
    M = packet["config"]["modes"]
    if (not isinstance(value, list) or len(value) != M or
            not all(isinstance(x, (float, int)) and math.isfinite(x) for x in value)):
        raise ValueError("The bound reference does not contain a complete finite H")
    if not math.isfinite(factor) or not 0 < factor <= 1:
        raise ValueError("Warm factor must be explicit and lie in (0,1]")
    if arithmetic == "python":
        requested = [float(x) * factor ** (j + 1) for j, x in enumerate(value)]
    elif arithmetic == "numpy":
        import numpy as np
        requested = (np.asarray(value, dtype=float) *
                     factor ** np.arange(1, M + 1)).tolist()
    else:
        raise ValueError("Unknown original warm arithmetic")
    actual = packet["request"]["height"]
    cp = packet["response"]["checkpoint"]
    if requested != actual or cp["cutHeight"] != actual:
        raise ValueError("Accepted height is not the declared original request")
    return {
        "reference": ref(reference_path), "reference_key": key,
        "reference_height_sha256": canonical_sha(value),
        "requested_height_sha256": canonical_sha(actual),
        "factor": factor, "factor_exact_binary": str(Q.from_float(factor)),
        "original_arithmetic": arithmetic,
        "role": ("unscaled_reference_height_candidate" if factor == 1
                 else "warm_scaled_reference_height"),
        "unscaled_reference_request_verified": factor == 1,
        "prefix_coupling_verified": False, "exact_full_H_solution_proved": False,
    }


def state_match(record_path, packet):
    """Check exact accepted states with small seeks; hashing follows extraction."""
    record = read(record_path)
    if record.get("status") != "complete" or record.get("returncode") != 0:
        return False
    if not record.get("input") or not record.get("static_metadata"):
        return False
    meta = checked(record["static_metadata"])
    cp, M = packet["response"]["checkpoint"], packet["config"]["modes"]
    if len(meta["stages"]) + 1 != len(cp["states"]):
        return False
    with open(record["input"]["path"], "rb") as stream:
        stream.seek(44)
        if stream.read(64).decode("ascii") != record["payload_token"]:
            return False
        for row in meta["stages"]:
            stream.seek(row["initialOffset"])
            data = stream.read(8 * (2 * M + 2))
            if len(data) != 8 * (2 * M + 2):
                return False
            initial = struct.unpack("<" + "d" * (2 * M + 2), data)
            if (list(initial[:2 * M]) != cp["states"][row["stage"] + 1] or
                    initial[-2:] != (0.0, 0.0)):
                return False
    return True


def select_native(packet, explicit=None, directory=None):
    if bool(explicit) == bool(directory):
        raise ValueError("Give one native record or its containing native-runs directory")
    if explicit:
        if not state_match(explicit, packet):
            raise ValueError("Explicit native evaluation is not of these accepted states")
        return Path(explicit).resolve()
    candidates = sorted(Path(directory).rglob("*-record.json"),
                        key=lambda p: p.stat().st_mtime_ns, reverse=True)
    for candidate in candidates:
        if state_match(candidate, packet):
            return candidate.resolve()
    raise ValueError("No completed native evaluation exactly matches the accepted states")


def validate_packet_states(packet, M, spacing):
    cp, cfg = packet["response"]["checkpoint"], packet["config"]
    if M != 24 or spacing != 3 or cfg["quadrature"] != 512:
        raise ValueError("This original shared-R exporter requires M24/512/spacing3")
    if cp["parameters"]["modes"] != M or cp["parameters"]["spacing"] != spacing:
        raise ValueError("Checkpoint finite dimensions differ")
    if len(cp["states"]) != cp["parameters"]["depth"] + 1:
        raise ValueError("Incomplete finite checkpoint")
    if any(len(row) != 2 * M or not all(math.isfinite(x) for x in row)
           for row in cp["states"]):
        raise ValueError("Incomplete or nonfinite finite state")


def index_shared_nodes(manifest_path, mean_chain_path, outpath):
    manifest, chain = read(manifest_path), read(mean_chain_path)
    if manifest["status"] != "selected_stages_share_one_literal_R_C2_definition":
        raise ValueError("Shared-R construction did not finish")
    if manifest["input"] != ref(mean_chain_path):
        raise ValueError("Shared-R export used another original mean chain")
    S = len(chain["mean_chain"]) - 1
    files = {row["stage"]: row for row in manifest["files"]}
    if len(files) != len(manifest["files"]):
        raise ValueError("Duplicate exported stage")
    nodes = {}
    cut = deep = None
    for stage in sorted(files):
        entry, data = files[stage], checked(files[stage])
        if (data["stage"] != stage or
                data["status"] != "literal_R_stage_with_exact_common_boundary_two_jets" or
                data["sharing"]["mapHash"] != entry["mapHash"] or
                data["boundInput"] != manifest["input"]):
            raise ValueError("Stage identity or shared map hash changed")
        for index, local in ((stage + 1, 0), (stage, len(data["nodes"]) - 1)):
            node = data["nodes"][local]
            value = {"radius": node["radiusJS"], "coefficients": node["coefficients"]}
            digest = canonical_sha(value)
            if index in nodes and nodes[index]["value_sha256"] != digest:
                raise ValueError("Adjacent stages have different literal full two-jets")
            if [node["meanPerturbation"], node["meanBackground"]] != chain["mean_chain"][index]:
                raise ValueError("A shared node changed the original cumulative mean")
            nodes[index] = {
                "node": index, "R_exact_binary": str(Q.from_float(node["radiusJS"])),
                "value_sha256": digest, "stage_file": entry,
                "local_node_index": local, "canonical_definition": node["canonicalDefinition"],
                "mean_perturbation_exact_binary": str(Q.from_float(node["meanPerturbation"])),
                "mean_background_exact_binary": str(Q.from_float(node["meanBackground"])),
            }
            if index == 0:
                cut = nodes[index]
            if index == S:
                deep = nodes[index]
    all_stages = set(files) == set(range(S))
    if all_stages and len(nodes) != S + 1:
        raise ValueError("Complete stage selection lost a canonical boundary node")
    index = {
        "status": "exact_common_boundary_nodes_indexed",
        "manifest": ref(manifest_path), "mean_chain": ref(mean_chain_path),
        "finite_stage_count": S, "selected_stages": sorted(files),
        "all_stages_exported": all_stages, "unique_boundary_nodes": list(nodes.values()),
        "cut_node": cut, "deep_node": deep,
        "all_finite_stage_adjacencies_verified": all_stages,
        "internal_stage_knots": "Exact binary radius and two-jet arrays in each bound stage file.",
        "arrays_are_new_field_data": True,
    }
    write(outpath, index)
    return index


def export(args):
    start = time.monotonic()
    outdir = fresh_dir(args.outdir)
    background_record = TOPIC / "notes/2026-11-20-m3-m24-warm050-execution.json"
    packet, response, jets, spacing, M, arrays = load_packet(
        args.tail_response, args.source_port, background_record
    )
    validate_packet_states(packet, M, spacing)
    height = bind_height(packet, args.height_reference, args.height_reference_key,
                         args.warm_factor, args.height_arithmetic)
    native = select_native(packet, args.native_record, args.native_record_dir)
    native_data = read(native)
    native_manifest = checked(native_data["manifest"])
    source_topic = Path(native_manifest["source_topic"])
    for name, digest in packet["source_sha256"].items():
        if sha(source_topic / "scripts" / name) != digest:
            raise ValueError("Accepted packet source changed: " + name)
    for name, digest in HELPER_SHAS.items():
        if sha(TOPIC / "scripts/resume_n4" / name) != digest:
            raise ValueError("Analysed exporter/mean-chain source changed: " + name)
    summary_path = outdir / "geometry-bundle.json"
    summary = {
        "status": "running", "source": ref(__file__),
        "accepted_packet": ref(args.tail_response), "source_port": ref(args.source_port),
        "native_record": ref(native), "height_identity": height,
        "original_accepted_gate": {"converged": True, "residual": response["residual"],
                                   "solveTolerance": packet["config"]["solveTolerance"]},
        "source_files": packet["source_sha256"], "finite_scope": {"M": M, "quadrature": 512, "spacing": spacing},
        "original_BVP_solves": 0, "original_tail_solves": 0,
        "continuous_metric_certified": False, "closed_surface_proved": False,
    }
    write(summary_path, summary)
    chain_path = outdir / "original-native-mean-chain.json"
    extract = TOPIC / "scripts/resume_n4/extract_q060_native_mean_chain.py"
    batch = TOPIC / "scripts/resume_n4/export_q060_shared_r_tail_batch.mjs"
    stage_dir = outdir / "shared-R-stages"
    commands = [
        [sys.executable, str(extract), "--checkpoint", str(args.tail_response.resolve()),
         "--native-record", str(native), "--out", str(chain_path)],
        [args.node, str(batch), "--input", str(chain_path), "--outdir", str(stage_dir),
         "--stages", args.stages, "--degree", str(args.degree),
         "--difference-step", str(args.difference_step)],
    ]
    try:
        for number, command in enumerate(commands):
            with (outdir / ("step-" + str(number) + ".log")).open("w") as stream:
                subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT, check=True)
        node_index_path = outdir / "canonical-boundary-node-index.json"
        index = index_shared_nodes(stage_dir / "manifest.json", chain_path, node_index_path)
        summary.update(
            status="accepted_new_tail_shared_R_representation_exported",
            mean_chain=ref(chain_path), shared_R_manifest=ref(stage_dir / "manifest.json"),
            canonical_node_index=ref(node_index_path),
            all_stages_exported=index["all_stages_exported"],
            selected_stages=index["selected_stages"],
            complete_finite_C2_stage_chain=index["all_stages_exported"],
            actual_cut_stage_exported=index["cut_node"] is not None,
            actual_deep_anchor_exported=index["deep_node"] is not None,
            deep_collar_attached=False, commands=commands, seconds=time.monotonic() - start,
        )
    except Exception as exc:
        summary.update(status="failed", error=repr(exc), commands=commands,
                       seconds=time.monotonic() - start)
        write(summary_path, summary)
        raise
    write(summary_path, summary)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("tail-response", "source-port", "height-reference", "outdir"):
        parser.add_argument("--" + name, type=Path, required=True)
    native = parser.add_mutually_exclusive_group(required=True)
    native.add_argument("--native-record", type=Path)
    native.add_argument("--native-record-dir", type=Path)
    parser.add_argument("--height-reference-key", default="raw_return.candidate_H")
    parser.add_argument("--warm-factor", type=float, required=True)
    parser.add_argument("--height-arithmetic", choices=("python", "numpy"), required=True)
    parser.add_argument("--stages", default="all")
    parser.add_argument("--degree", type=int, default=192)
    parser.add_argument("--difference-step", type=float, default=.00005)
    parser.add_argument("--node", default="node")
    args = parser.parse_args()
    result = export(args)
    print(json.dumps({key: result[key] for key in (
        "status", "accepted_packet", "height_identity", "selected_stages",
        "all_stages_exported", "seconds"
    )}), flush=True)


if __name__ == "__main__":
    main()
