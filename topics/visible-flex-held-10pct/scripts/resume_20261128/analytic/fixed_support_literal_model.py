"""Narrow original-R53 fixed-support adapter preserving the source radial chart.

The Nov26 original fixed=True model is retained. This declared model kind
restores the literal chart of its real accepted original design anchor; it
does not relabel a warm phase family or accept any field without a solve.
"""
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np

KIND = "original_r53_fixed_support_literal_chart_v1"
SCRIPTS = Path(__file__).resolve().parents[2]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def chart_record(obj):
    return dict(chart_join=float(obj.chart_join),
                chart_reference_prefix=float(obj.chart_reference_prefix),
                chart_breaks=np.asarray(obj.chart_breaks).tolist())


def restore_chart(obj, record):
    if (not 0 < record["chart_join"] < 1 or record["chart_reference_prefix"] <= 0
            or not np.all(np.isfinite(record["chart_breaks"]))):
        raise ValueError("Invalid declared literal source chart")
    obj.chart_join = float(record["chart_join"])
    obj.chart_reference_prefix = float(record["chart_reference_prefix"])
    obj.chart_breaks = np.array(record["chart_breaks"], dtype=float)


def original_source_signature(record):
    legacy = module("_literal_signature_legacy", SCRIPTS/"resume_20261126/fixed_m3_branch_model.py")
    return legacy.original_source_signature(record)


def load_model(config):
    path = Path(config["source_run"]).resolve()
    record = json.loads(path.read_text())
    if record.get("model_kind") != KIND:
        raise ValueError("Require an honestly declared original-R53 literal-chart fixed model")
    origin = json.loads(Path(record["origin_design_run"]).read_text())
    if (origin.get("core_settings", {}).get("homotopy", 0) <= 0
            or record["frozen_profile"] != origin["frozen_profile"]
            or record["mean_nodes"] != origin["prefix_audit"]["samples_psi"]):
        raise ValueError("The actual design anchor, frozen physical metric or literal mean changed")
    legacy = module("_literal_geometry_legacy", SCRIPTS/"resume_20261126/fixed_m3_branch_model.py")
    original_module = legacy.module
    captured = {}

    def capture_module(name, file):
        result = original_module(name, file)
        if Path(file).name == "actual_m3_metric_model.py":
            original_load = result.load_model

            def load_actual(config):
                design = original_load(config)
                captured.update(chart_record(design))
                return design
            result.load_model = load_actual
        return result

    legacy.module = capture_module
    obj = legacy.load_model(config)
    if captured != record["frozen_literal_radial_chart"]:
        raise ValueError("The fixed model's literal chart differs from its actual design anchor")
    restore_chart(obj, captured)
    obj.relative_metric_loader_record.update(model_kind=KIND,
        frozen_literal_radial_chart=captured,
        source_literal_radial_chart_restored=True)
    return obj
