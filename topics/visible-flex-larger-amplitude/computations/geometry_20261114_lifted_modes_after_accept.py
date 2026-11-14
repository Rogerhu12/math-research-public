#!/usr/bin/env python3
"""Actual full-DN acceptance to material readout and its own finite closed map.

This is a public-Actions consumer, not a solver or acceptance shortcut.
It reads the accepted complete state, measures physical material jets,
audits its cut spectrum and regenerates the actual accepted tail's radial
field before closing it.  No historical A geometry enters the pipeline.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time

from geometry_20261114_lifted_modes_saved_prefix import (
    actions_only, read, sha, validate_checkpoint)


HERE = Path(__file__).resolve().parent


def write(path, value):
    with Path(path).open("x") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")


def main():
    actions_only()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--port", type=Path, required=True)
    parser.add_argument("--tail-config", type=Path, required=True)
    parser.add_argument("--tail-response", type=Path)
    parser.add_argument("--source-topic", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--angles", type=int, nargs="+", default=[2048, 4096])
    parser.add_argument("--radial-subdivisions", type=int, nargs="+", default=[2, 4])
    parser.add_argument("--readout-levels", default="1,2,4")
    args = parser.parse_args()
    checkpoint = read(args.checkpoint)
    identity = validate_checkpoint(checkpoint)
    response_path = args.tail_response or args.checkpoint.parent/"actual-tail-final-audit.json.gz"
    actual = checkpoint["actual_tail"]
    if sha(response_path) != actual["final_response_sha256"]:
        raise ValueError("The supplied final tail is not this accepted full-DN response")
    if sha(args.tail_config) != actual["sources"]["input_config"]:
        raise ValueError("The tail configuration differs from this actual response")
    if read(args.port) != checkpoint["fixed_scalar_profile"]["geometry"]["complete_original_port"]:
        raise ValueError("The original full scalar port differs")
    if int(read(args.tail_config)["modes"]) != identity["actual_tail_modes"]:
        raise ValueError("Retain all actual material tail modes")
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError("Use a fresh post-acceptance output directory")
    sources = ["geometry_20261114_lifted_modes_saved_prefix.py",
               "geometry_20261114_lifted_modes_profile.py",
               "geometry_20261114_lifted_modes_readout.py",
               "geometry_20261114_lifted_modes_material_tail_packet.py",
               "geometry_20261114_lifted_modes_closed_assembly.py"]
    intent = dict(schema="independent-modes-after-accept-intent-v1", scope=__doc__,
        independent_field_modes=identity,
        input_sha256={str(p.resolve()):sha(p) for p in
                      (args.checkpoint, args.port, args.tail_config, response_path)},
        source_sha256={name:sha(HERE/name) for name in sources},
        driver_sha256=sha(__file__),
        physical_angles=args.angles, physical_radial_subdivisions=args.radial_subdivisions,
        actual_tail_radial_readout_levels=args.readout_levels,
        source_topic=str(args.source_topic.resolve()),
        new_BVP_or_DN_solve_requested=False, task_completed=False)
    write(args.out/"intent.json", intent)
    started = time.monotonic()
    commands = []

    def execute(label, command):
        log = args.out/(label+".log")
        print(json.dumps(dict(event="independent_modes_after_accept", stage=label,
            command=list(map(str, command)), log=str(log))), flush=True)
        before = time.monotonic()
        with log.open("x") as stream:
            result = subprocess.run(list(map(str, command)), stdout=stream,
                stderr=subprocess.STDOUT, env=dict(os.environ))
        row = dict(stage=label, returncode=result.returncode,
                   seconds=time.monotonic()-before, log=log.name)
        commands.append(row)
        write(args.out/(label+"-execution.json"), row)
        if result.returncode:
            raise RuntimeError("Actual post-acceptance readout failed at "+label+"; original log retained")

    prefix_report = args.out/"physical-material-prefix.json"
    execute("material-prefix", [sys.executable, HERE/"geometry_20261114_lifted_modes_readout.py",
        "--input", args.checkpoint, "--angles", *args.angles,
        "--radial-subdivisions", *args.radial_subdivisions, "--out", prefix_report])
    M = identity["actual_field_modes"]
    packet = args.out/"material-cut-packet"
    execute("material-cut", [sys.executable, HERE/"geometry_20261114_lifted_modes_material_tail_packet.py",
        "--input", args.checkpoint, "--angles", *args.angles,
        "--tail-modes", M, 2*M, "--out", packet])
    surface = args.out/"closed"/"surface"
    execute("finite-closed", [sys.executable, HERE/"geometry_20261114_lifted_modes_closed_assembly.py",
        "all", "--checkpoint", args.checkpoint, "--port", args.port,
        "--config", args.tail_config, "--tail-response", response_path,
        "--source-topic", args.source_topic, "--out-prefix", surface,
        "--readout-levels", args.readout_levels])
    assembly_path = Path(str(surface)+"-assembly.json")
    material, assembly = read(prefix_report), read(assembly_path)
    prefix_levels = material["levels"]
    pieces = assembly["sampled_piece_jets"]
    operator = max([level["metric_relative_operator_sample"] for level in prefix_levels]
                   +[row["metric_relative_operator_max"] for row in pieces.values()])
    component = max([level["metric_component_sample"] for level in prefix_levels]
                    +[row["metric_component_max"] for row in pieces.values()])
    curvature = max([level["curvature_sample"] for level in prefix_levels]
                    +[row["curvature"] for row in pieces.values()])
    summary = dict(schema="independent-modes-actual-finite-closed-readout-v1",
        independent_field_modes=identity, commands=commands,
        prefix_report=dict(file=prefix_report.name, sha256=sha(prefix_report)),
        material_packet=dict(file=str(packet/"summary.json"), sha256=sha(packet/"summary.json")),
        closed_assembly=dict(file=str(assembly_path), sha256=sha(assembly_path)),
        whole_closed_metric_relative_operator_sample_max=operator,
        whole_closed_metric_component_sample_max=component,
        combined_absolute_principal_curvature_sample_max=curvature,
        metric_norm_definition="spectral norm of g^(-1/2)(Gram-g)g^(-1/2), distinct from component maximum",
        sampled_operator_1e_minus_6_gate_passed=operator <= 1e-6,
        fixed_caps_reference="Their own fixed induced metric, including weak markers",
        old_mean_added=False, historical_A_tail_reused=False,
        full_continuous_metric_or_reach_certificate=False,
        same_g_nonlinear_refinement_demonstrated=False,
        actual_whole_surface_Hausdorff_gate_demonstrated=False,
        task_completed=False, seconds=time.monotonic()-started)
    write(args.out/"summary.json", summary)
    print(json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
