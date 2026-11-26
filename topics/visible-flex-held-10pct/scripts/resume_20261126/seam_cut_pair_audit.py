#!/usr/bin/env python3
"""Run the two bound cut audits once, keeping all coefficient data local."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ("source-run", "physical", "source-port", "short-bridge-source",
                 "tail-response", "out"):
        ap.add_argument("--" + name, type=Path, required=True)
    a = ap.parse_args()
    started = time.monotonic()
    out = a.out.resolve()
    repository = HERE.parents[3]
    if out == repository or repository in out.parents:
        raise ValueError("Generated cut data must stay outside the repository")
    details = out.parent / (out.stem + "-local")
    details.mkdir(parents=True, exist_ok=False)
    height_path, trace_path = details / "height.json", details / "bridge-trace.json"
    trace_npz = details / "bridge-trace.npz"
    height_source = HERE / "seam_cut_height_compatibility.py"
    trace_source = HERE / "seam_bridge_cut_trace.py"
    commands = [
        [sys.executable, str(height_source), "--tail-response", str(a.tail_response),
         "--source-port", str(a.source_port), "--out", str(height_path)],
        [sys.executable, str(trace_source), "--source-run", str(a.source_run),
         "--physical", str(a.physical), "--source-port", str(a.source_port),
         "--short-bridge-source", str(a.short_bridge_source),
         "--tail-packet", str(a.tail_response), "--out-npz", str(trace_npz),
         "--out", str(trace_path)],
    ]
    for index, command in enumerate(commands):
        with (details / f"audit-{index}.log").open("w") as log:
            returned = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT)
        if returned.returncode:
            print((details / f"audit-{index}.log").read_text(errors="replace")[-6000:], flush=True)
            return returned.returncode
    height = json.loads(height_path.read_text())
    trace = json.loads(trace_path.read_text())
    if height["input_sha256"] != trace["tail_height_comparison"]["packet_sha256"]:
        raise ValueError("The two audits did not read the same accepted packet")
    if height["source_port_sha256"] != trace["source_port_sha256"]:
        raise ValueError("The two audits did not read the same original port")
    result = dict(height)
    result.update(
        status="accepted_cut_pair_audit",
        height_audit_status=height["status"],
        pair_audit_source_sha256=sha(__file__),
        bridge_tail_trace={
            key: trace[key] for key in (
                "status", "source_sha256", "source_run_sha256", "physical_sha256",
                "source_port_sha256", "modes", "gauge_exact", "mean_nodes", "psi_sha256",
                "s_entry_exact", "s_cut_exact", "R_cut_exact", "mean_M", "mean_M_s",
                "literal_node_Frenet_root_lower", "height_mean_R_first",
                "height_mean_R_second", "horizontal_perturbation_R_jet_l1_upper",
                "height_nonzero_R_jet_l1_upper", "tail_height_comparison", "npz_sha256",
                "full_H_identity_certified_here", "Cartesian_C2_seam_certified_here",
                "absolute_cut_height_certified_here",
            )
        },
        local_artifacts={
            "height": {"path": str(height_path), "sha256": sha(height_path)},
            "bridge_trace": {"path": str(trace_path), "sha256": sha(trace_path)},
            "bridge_trace_npz": {"path": str(trace_npz), "sha256": sha(trace_npz)},
        },
        source_hashes={
            str(path): sha(path) for path in (Path(__file__), height_source, trace_source)
        },
        source_commands=commands,
        pair_seconds=time.monotonic() - started,
    )
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": result["status"],
        "branches_certified": result["branches"]["certified"],
        "bridge_mean_first_difference": trace["tail_height_comparison"]["mean_first_difference"],
        "bridge_mean_second_difference": trace["tail_height_comparison"]["mean_second_difference"],
        "complete_height_jet_gap_upper": trace["tail_height_comparison"]["complete_difference_R_jet_l1_upper"],
        "full_H_certified_here": False,
        "Cartesian_C2_seam_certified_here": False,
        "out_sha256": sha(out),
        "seconds": result["pair_seconds"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
