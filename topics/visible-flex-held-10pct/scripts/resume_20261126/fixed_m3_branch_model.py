#!/usr/bin/env python3
"""Read-only reconstruction of a fixed-metric, unknown-core m3 branch.

The original portable adapter deliberately handles design p0=delta increment.
This adapter instead constructs fixed=True and retains p0=log(q_actual/q_seed).
It never solves a boundary problem and does not claim convergence.
"""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def option(record, name, required=True):
    command = record["command"]
    if name not in command:
        if required:
            raise ValueError("Original command lacks " + name)
        return None
    index = command.index(name)
    if index + 1 >= len(command):
        raise ValueError("Incomplete original option " + name)
    return command[index + 1]


def original_source_signature(record):
    """Compare actual source bytes, independent of relocated scratch roots."""
    signature = {}
    for path, expected in record.get("source_hashes", {}).items():
        if sha(path) != expected:
            raise ValueError("Original numerical source changed: " + path)
        key = Path(path).name
        if key in signature and signature[key] != expected:
            raise ValueError("Ambiguous original source basename: " + key)
        signature[key] = expected
    for flag in ("--core-module", "--core-config"):
        path = option(record, flag, required=False)
        if path is not None:
            expected = record.get("inputs", {}).get(str(Path(path).resolve()))
            actual = sha(path)
            if expected is not None and actual != expected:
                raise ValueError("Original core input changed: " + path)
            signature[flag] = actual
    return signature


def load_model(config):
    run_path = Path(config["source_run"]).resolve()
    record = json.loads(run_path.read_text())
    if record.get("fixed_metric") is not True or record.get("fixed_core") is not False:
        raise ValueError("Expected a declared fixed-metric unknown-core branch")
    if record.get("parameter_zero_meaning") != "log(q_actual/q_seed)":
        raise ValueError("Fixed parameter semantics are missing")
    original_path = Path(record["origin_design_run"])
    original = json.loads(original_path.read_text())
    signature = original_source_signature(original)
    if signature != record["frozen_source_signature"]:
        raise ValueError("The fixed problem's original sources changed")
    adapter = module("_fixed_branch_original_geometry", SCRIPTS/"resume_m3/actual_m3_metric_model.py")
    design = adapter.load_model(dict(source_run=str(original_path)))
    port_path = Path(record["linear_port_path"])
    port = json.loads(port_path.read_text())
    if sha(port_path) != record["linear_port_sha256"]:
        raise ValueError("The numerical port file changed")
    port["cut"]["_prefix_bridge"] = record["frozen_profile"]["prefix_bridge"]
    port["_sha256"] = sha(port_path)
    if (port["parameters"] != record["physical_tail_parameters"] or
            port["cut"] != record["physical_tail_cut"]):
        raise ValueError("The fixed physical tail metric changed")
    if (original["angular_chart"] != record["angular_chart"] or
            original.get("core_settings") != record["core_settings"] or
            original["gauge_q"] != record["gauge_q"] or
            original["warp_reference"] != record["warp_reference"]):
        raise ValueError("The fixed core/chart/gauge definition changed")
    obj = type(design)(copy.deepcopy(record["frozen_profile"]), port,
                       float(record["gauge_q"]), int(record["modes"]),
                       int(record["angular"]), True, float(record["warp_reference"]))
    obj.bcweights = np.full(obj.M, float(record["bc_normalization"]))
    obj.relative_metric_loader_record = dict(
        source_run=str(run_path), source_run_sha256=sha(run_path),
        origin_design_run=str(original_path), fixed_metric=True, fixed_core=False,
        parameter_zero_meaning="log(q_actual/q_seed)",
        mean_nodes=record["mean_nodes"],
        scope="Same frozen metric and original exact-lift geometry; no boundary solve",
        bvp_or_tail_solver_invoked=False)
    return obj
