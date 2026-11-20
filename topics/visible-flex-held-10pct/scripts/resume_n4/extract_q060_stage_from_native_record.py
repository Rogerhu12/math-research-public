#!/usr/bin/env python3
"""Read a saved accepted tail and its existing native flow; never run a solver."""
import argparse
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import struct


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    return json.loads(gzip.decompress(path.read_bytes()) if path.suffix == ".gz" else path.read_text())


def checked(ref):
    if sha(ref["path"]) != ref["sha256"]:
        raise ValueError("Saved native record changed: " + ref["path"])
    return Path(ref["path"])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--checkpoint", type=Path, required=True)
    ap.add_argument("--native-record", type=Path, required=True)
    ap.add_argument("--stage", type=int, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    record = read(a.native_record)
    if record["status"] != "complete" or record["returncode"] != 0:
        raise ValueError("An actual completed native record is required.")
    inp, out = checked(record["input"]), checked(record["output"])
    meta_path, manifest_path = checked(record["static_metadata"]), checked(record["manifest"])
    meta, manifest = read(meta_path), read(manifest_path)
    saved = read(a.checkpoint)
    response = saved["response"]
    if not response.get("converged"):
        raise ValueError("This extraction requires an existing accepted finite response.")
    cp = response["checkpoint"]
    M, count = cp["parameters"]["modes"], len(meta["stages"])
    if not 0 <= a.stage < count or len(cp["states"]) != count + 1:
        raise ValueError("Checkpoint/stage layout mismatch")
    payload = inp.read_bytes()
    if payload[44:108].decode() != record["payload_token"]:
        raise ValueError("Native input token mismatch")
    maximum_input_difference = 0.0
    for row in meta["stages"]:
        values = struct.unpack_from("<" + "d" * (2 * M + 2), payload, row["initialOffset"])
        expected = cp["states"][row["stage"] + 1]
        if len(expected) != 2 * M or values[-2:] != (0.0, 0.0):
            raise ValueError("Unexpected saved mean slots")
        diff = max(abs(x - y) for x, y in zip(values[:2 * M], expected))
        maximum_input_difference = max(maximum_input_difference, diff)
    if maximum_input_difference != 0:
        raise ValueError("This native call did not evaluate the saved accepted states.")
    parser = Path(__file__).resolve().parents[1] / "resume_n4_tail/native_extended/probe_native_frozen_flow.py"
    spec = importlib.util.spec_from_file_location("saved_native_parser", parser)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rows = module.read_batch_output(out, record["payload_token"], M, count, record["withJac"])
    mean = [0.0, 0.0]
    exact_mean = [Fraction(0), Fraction(0)]
    for index in range(count - 1, a.stage, -1):
        for j in range(2):
            value = rows[index]["state"][2 * M + j]
            mean[j] += value
            exact_mean[j] += Fraction.from_float(value)
    stage = meta["stages"][a.stage]
    end = rows[a.stage]["state"]
    target = cp["states"][a.stage]
    defect = [end[j] / (1 if j < M else stage["portRatio"]) - target[j] for j in range(2 * M)]
    result = {
        "scope": __doc__, "status": "existing_native_flow_exact_input_states_matched",
        "source_sha256": sha(__file__), "parser_source_sha256": sha(parser),
        "checkpoint": {"path": str(a.checkpoint.resolve()), "sha256": sha(a.checkpoint),
                       "converged": True, "residual": response["residual"],
                       "cut_height": cp["cutHeight"], "config": saved["config"]},
        "native_record": {"path": str(a.native_record.resolve()), "sha256": sha(a.native_record)},
        "native_input": record["input"], "native_output": record["output"],
        "metadata": record["static_metadata"], "manifest": record["manifest"],
        "source_topic": manifest["source_topic"],
        "all_stage_input_maximum_difference": maximum_input_difference,
        "stage": stage, "state_inner": cp["states"][a.stage + 1],
        "state_outer": target, "native_stage_output": end,
        "native_stage_end_defect": defect,
        "inner_mean_perturbation_and_background": mean,
        "exact_sum_of_binary_inner_mean_increments": [str(v) for v in exact_mean],
        "mean_contract": "Two distinct saved local increments, accumulated from the finite deepest port in descending stage order. Slot 2M is perturbation mean; slot 2M+1 is background primitive. This is a numerical existing-flow primitive, not a newly certified continuous one.",
        "source_files": saved["source_sha256"],
        "finite_scope": meta["scope"], "bvp_solves_executed": 0,
    }
    a.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "stage": a.stage,
                      "all_stage_input_maximum_difference": maximum_input_difference,
                      "inner_means": mean,
                      "maximum_selected_stage_absolute_defect": max(map(abs, defect)),
                      "out_sha256": sha(a.out)}))


if __name__ == "__main__":
    main()
