#!/usr/bin/env python3
"""Rebuild the actual portable m3 geometry model for a read-only metric audit.

load_model(config) accepts either the run.json object itself or
{"source_run": "/absolute/path/to/run.json"}. Files named by that actual command
must still be available in the same worker. No seed, BVP solve, tail solve,
parameter continuation or mode transfer is performed. Intended for a fresh
process, as the original portable loader installs source classes globally.

The physical PPoly and its parameter vector are loaded separately by
audit_full_relative_metric.load_physical. This source was saved unexecuted.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def load_model(config):
    if "source_run" in config:
        run_path = Path(config["source_run"]).resolve()
        record = json.loads(run_path.read_text())
    else:
        run_path = None
        record = dict(config)
    command = record["command"]

    def option(name, required=True):
        if name not in command:
            if required:
                raise ValueError("Actual run command lacks "+name)
            return None
        index = command.index(name)
        if index+1 >= len(command):
            raise ValueError("Incomplete option in actual run command: "+name)
        return command[index+1]

    source = Path(option("--source-topic"))
    short = Path(option("--short-bridge"))
    profile_path = Path(option("--profile"))
    chart_path = Path(option("--chart"))
    port_path = Path(option("--port"))
    cfg = json.loads(profile_path.read_text())
    chart = json.loads(chart_path.read_text())
    port = json.loads(port_path.read_text())
    port["cut"]["_prefix_bridge"] = cfg["prefix_bridge"]
    port["_sha256"] = _sha(port_path)
    if (cfg != record["physical_profile"] or chart != record["angular_chart"] or
            port["parameters"] != record["physical_tail_parameters"] or
            port["cut"] != record["physical_tail_cut"]):
        raise ValueError("The actual run's profile, chart or physical tail metric changed")
    if bool(record.get("fixed_metric_refinement", False)):
        raise ValueError(
            "This adapter handles the portable design constructor; fixed=True has a different p0 meaning")

    core_name = option("--core-module", required=False)
    core_config_name = option("--core-config", required=False)
    settings = (json.loads(Path(core_config_name).read_text())
                if core_config_name is not None else {})
    if core_name is not None and settings != record.get("core_settings"):
        raise ValueError("The actual run's material core settings changed")
    if core_name is not None:
        for file_name in (core_name, core_config_name):
            if file_name is None:
                continue
            file_path = Path(file_name)
            expected = record.get("inputs", {}).get(str(file_path.resolve()))
            if expected is not None and _sha(file_path) != expected:
                raise ValueError("The actual core provider or settings file changed")

    scripts = source/"scripts"
    coupler = _module("_metric_coupler", scripts/"db6f-prefix-coupled.py")
    _module("_metric_flat", scripts/"db6f-prefix-flat-profile.py").install(coupler.adaptive)
    coupler.adaptive.old.install_source(source/"repro/source-root")
    _module("_metric_short", short).install()
    _module("_metric_fourier_jac", scripts/"78718-prefix-fourier-jacobian.py").install(
        coupler.adaptive)
    factory = None
    if core_name is not None:
        factory = _module("_metric_actual_core", Path(core_name)).make_factory(settings)
        __import__("fixed_metric_mode3_core").PlanarSupportCore = factory
        __import__("fixed_metric_mode3_bvp").PlanarSupportCore = factory
    Flow, Base = coupler.adaptive.build_classes(chart)
    if factory is not None:
        # Same implementation and order as portable_prefix_continue.py.
        lib = Path(__file__).with_name("round_raw_lib")
        sys.path.insert(0, str(lib))
        from exact_core_lift import install_core_lift
        Base = install_core_lift(Flow, Base)
        if hasattr(factory, "jet_parameter_derivatives"):
            import analytic_adaptive_core_jac as analytic
            analytic.parameter_jets = lambda core, theta: core.jet_parameter_derivatives(theta)
            analytic.install(Base)
    modes = int(record["modes"])
    obj = Base(cfg, port, float(record["gauge_q"]), modes,
               int(record["angular"]), False, float(record["warp_reference"]))
    gates = record.get("gates", {})
    if "physical_bc_tol" in gates and "bc_tol" in gates:
        obj.bcweights = np.full(modes, gates["physical_bc_tol"]/gates["bc_tol"])
    obj.relative_metric_loader_record = dict(
        source_run=str(run_path) if run_path is not None else None,
        source_run_sha256=_sha(run_path) if run_path is not None else None,
        scope="same actual geometry construction; terminal boundary class is unnecessary for evaluation",
        profile_path=str(profile_path), chart_path=str(chart_path), port_path=str(port_path),
        core_module=core_name, core_settings=settings if factory is not None else None,
        exact_lift_installed=factory is not None,
        parameters_loaded_from_physical_npz_later=True,
        bvp_or_tail_solver_invoked=False)
    return obj
