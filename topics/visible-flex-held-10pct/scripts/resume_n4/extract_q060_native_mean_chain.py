#!/usr/bin/env python3
"""Bind one existing full native evaluation and its single cumulative mean chain."""
import argparse
import importlib.util
import json
from pathlib import Path
import struct

from extract_q060_stage_from_native_record import read, checked, sha


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checkpoint", type=Path, required=True)
    p.add_argument("--native-record", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    record, saved = read(a.native_record), read(a.checkpoint)
    if record["status"] != "complete" or record["returncode"] != 0 or not saved["response"].get("converged"):
        raise ValueError("A completed evaluation of an accepted finite response is required.")
    input_path, output_path = checked(record["input"]), checked(record["output"])
    metadata_path, manifest_path = checked(record["static_metadata"]), checked(record["manifest"])
    meta, manifest = read(metadata_path), read(manifest_path)
    cp = saved["response"]["checkpoint"]
    M, count = cp["parameters"]["modes"], len(meta["stages"])
    data = input_path.read_bytes()
    if data[44:108].decode() != record["payload_token"] or len(cp["states"]) != count + 1:
        raise ValueError("Saved evaluation token or dimensions differ")
    for row in meta["stages"]:
        initial = struct.unpack_from("<" + "d" * (2 * M + 2), data, row["initialOffset"])
        if list(initial[:2 * M]) != cp["states"][row["stage"] + 1] or initial[-2:] != (0.0, 0.0):
            raise ValueError("Saved native initial state differs at stage " + str(row["stage"]))
    parser = Path(__file__).resolve().parents[1] / "resume_n4_tail/native_extended/probe_native_frozen_flow.py"
    spec = importlib.util.spec_from_file_location("saved_native_parser", parser)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rows = module.read_batch_output(output_path, record["payload_token"], M, count, record["withJac"])
    means = [[0.0, 0.0] for _ in range(count + 1)]
    for index in range(count - 1, -1, -1):
        means[index] = [means[index + 1][j] + rows[index]["state"][2 * M + j] for j in range(2)]
    result = {"status": "all_saved_initial_states_matched_single_mean_chain",
              "source_sha256": sha(__file__), "parser_sha256": sha(parser),
              "checkpoint": {"path": str(a.checkpoint.resolve()), "sha256": sha(a.checkpoint)},
              "native_record": {"path": str(a.native_record.resolve()), "sha256": sha(a.native_record)},
              "native_input": record["input"], "native_output": record["output"],
              "metadata": record["static_metadata"], "manifest": record["manifest"],
              "source_topic": manifest["source_topic"], "source_files": saved["source_sha256"],
              "finite_scope": meta["scope"], "config": saved["config"],
              "mean_chain": means,
              "mean_contract": "Node k accumulates the existing native increments from stages N-1 down to k, in this fixed binary64 order. Slot0 is perturbation mean, slot1 is background primitive; the finite deepest node is the existing zero anchor. Every adjacent stage shares this one node array.",
              "native_stage_outputs": [row["state"] for row in rows],
              "all_stage_input_maximum_difference": 0.0,
              "bvp_solves_executed": 0, "shooting_iterations_executed": 0}
    a.out.write_text(json.dumps(result, separators=(",", ":")) + "\n")
    print(json.dumps({"status": result["status"], "nodes": count + 1,
                      "cut_means": means[0], "stage127_inner_means": means[128],
                      "output_sha256": sha(a.out)}))


if __name__ == "__main__":
    main()
