#!/usr/bin/env python3
"""Interpret a portable m3 design as one frozen physical geometry.

This adapter does not run a BVP, a tail solve, or a field correction.  It
reuses the original geometry loader, absorbs the design delta displacement
into cfg, and then constructs fixed=True with p0=log(q_actual/q_seed).
The numerical mean rule is declared from the original actual audit; GL6
height is an oracle rule, not a certified smooth primitive or true integral.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def load_model(config):
    path = Path(config["source_run"]).resolve()
    digest = sha(path)
    if config.get("source_run_sha256", digest) != digest:
        raise ValueError("The original design run changed")
    record = json.loads(path.read_text())
    if record.get("fixed_metric_refinement", False):
        raise ValueError("This entry expects the original portable design run")
    old_loader = load_module("_frozen_m3_design_loader",
                             Path(__file__).with_name("actual_m3_metric_model.py"))
    design = old_loader.load_model({"source_run": str(path)})
    design_p = np.asarray(record["raw_return"]["parameters"], float)
    design.initial(design_p)
    actual_q = float(design.support_amplitude)
    frozen_cfg = copy.deepcopy(design.cfg)
    frozen_cfg["delta"] += float(design_p[0])
    if frozen_cfg != record["frozen_profile"]:
        raise ValueError("Recorded frozen profile disagrees with actual delta")
    port = copy.deepcopy(design.port)
    obj = type(design)(frozen_cfg, port, float(design.q), int(design.M),
                       int(design.nt), True, float(record["warp_reference"]))
    obj.bcweights = np.asarray(design.bcweights, float).copy()
    parameters = design_p.copy()
    parameters[0] = math.log(actual_q/float(obj.seed_support_amplitude))
    controls = np.asarray(design.pscale)*design_p[1:]
    if not np.array_equal(np.asarray(design.pscale), np.asarray(obj.pscale)):
        parameters[1:] = controls/np.asarray(obj.pscale)
    obj.initial(parameters)
    actual_controls = np.asarray(obj._core.corrections, float)
    if not np.array_equal(actual_controls, controls):
        raise ValueError("Freezing changed physical support coefficients")
    if float(obj.support_amplitude) != actual_q:
        raise ValueError("Freezing changed the actual primary support amplitude")
    mean_nodes = int(record.get("prefix_audit", {}).get(
        "samples_psi", max(512, 16*(3*obj.M+1))))
    if int(config.get("mean_nodes", mean_nodes)) != mean_nodes:
        raise ValueError("Declare a different mean as a different object")
    obj.frozen_parameters = parameters.copy()
    obj.frozen_parameters.setflags(write=False)
    obj.frozen_mean_nodes = mean_nodes
    obj.frozen_design_object = design
    obj.frozen_design_parameters = design_p.copy()
    obj.frozen_geometry_contract = dict(
        source_run=str(path), source_run_sha256=digest,
        fixed_metric_refinement=True, modes=int(obj.M),
        profile=copy.deepcopy(frozen_cfg), q_gauge=float(obj.q),
        q_actual=actual_q, parameters=parameters.tolist(),
        parameter_zero_meaning="log(q_actual/q_seed_support_amplitude)",
        physical_controls=controls.tolist(),
        warp_reference=float(record["warp_reference"]),
        angular_chart=copy.deepcopy(record["angular_chart"]),
        physical_tail_parameters=copy.deepcopy(record["physical_tail_parameters"]),
        physical_tail_cut=copy.deepcopy(record["physical_tail_cut"]),
        mean_nodes=mean_nodes, height_quadrature_order=6,
        mean_scope="original finite periodic mean and GL6 height oracle; no true-primitive/C2 certificate",
        exact_lift_coefficient=1., bvp_or_tail_solver_invoked=False,
        complete_surface=False)
    return obj


def check_identity(obj, physical_path, raw_path):
    raw = np.load(raw_path)
    data = np.load(physical_path)
    physical = SimpleNamespace(
        x=data["x"], p=data["p"],
        sol=PPoly.construct_fast(data["c"], data["x"], extrapolate=True, axis=1))
    old, old_p = obj.frozen_design_object, obj.frozen_design_parameters
    if not np.array_equal(raw["p"], old_p) or not np.array_equal(data["p"], old_p):
        raise ValueError("Raw/physical parameter vector differs from its design run")
    new_p = np.asarray(obj.frozen_parameters)
    old.initial(old_p)
    obj.initial(new_p)
    old_flow, new_flow = old.flow(old_p[0]), obj.flow(new_p[0])
    s_nodes, _ = old.chart(raw["x"], old_p[0])
    t_nodes = obj.inverse_chart(s_nodes, new_p[0])
    t_nodes[0], t_nodes[-1] = 0., 1.
    if np.any(np.diff(t_nodes) <= 0):
        raise ValueError("The physical-node chart pullback is not ordered")
    s_back, _ = obj.chart(t_nodes, new_p[0])
    # Same physical field at the same physical s. No cubic remeshing or
    # Fourier truncation occurs in this identity check.
    s = np.unique(np.r_[np.linspace(0., old_flow.end, 25),
                        old_flow.breakpoints, old_flow.prefix_end, old_flow.end])
    s = s[(s >= 0) & (s <= old_flow.end)]
    N = int(obj.frozen_mean_nodes)
    old_basis = old_flow.basis(N)
    new_basis = new_flow.basis(N)
    errors = {name: 0. for name in
              ("pos","p1","p2","s1","s2","sp","spp","rho","rhop","v","vp","vs")}
    profile_error = rhs_error = mean_error = mean_derivative_error = 0.
    field_twojet_error = 0.
    for first in range(0, len(s), 8):
        section = s[first:first+8]
        Y, Yp, Ypp = (physical.sol(section, order) for order in (0,1,2))
        old_geo, new_geo = old_flow.geo(section, N), new_flow.geo(section, N)
        for name in errors:
            errors[name] = max(errors[name],
                               float(np.max(np.abs(old_geo[name]-new_geo[name]))))
        profile_error = max(profile_error, float(np.max(np.abs(
            np.asarray(old_flow.profile(section))-np.asarray(new_flow.profile(section))))))
        rhs_error = max(rhs_error, float(np.max(np.abs(
            old_flow.fun(section, Y, old_p)-new_flow.fun(section, Y, new_p)))))
        for name, derivative, basis_index in (
                ("pos",Y,0),("p1",Y,1),("p2",Y,2),
                ("s1",Yp,0),("sp",Yp,1),("s2",Ypp,0)):
            a = old_geo[name]+old.q*old_flow.values(derivative,old_basis[basis_index])
            b = new_geo[name]+obj.q*new_flow.values(derivative,new_basis[basis_index])
            field_twojet_error = max(field_twojet_error,
                                     float(np.max(np.abs(a-b))))
        a, _, da = old_flow.velocity_s(section,Y,Yp,old_basis[1],old_basis[2])
        b, _, db = new_flow.velocity_s(section,Y,Yp,new_basis[1],new_basis[2])
        mean_error = max(mean_error, float(np.max(np.abs(
            np.mean(a["V"][:,:,2],axis=1)-np.mean(b["V"][:,:,2],axis=1)))))
        mean_derivative_error = max(mean_derivative_error, float(np.max(np.abs(
            np.mean(da[:,:,2],axis=1)-np.mean(db[:,:,2],axis=1)))))
    heights_old = old_flow.height_integral(physical,s,N,6)
    fixed_physical = SimpleNamespace(x=physical.x,sol=physical.sol,p=new_p)
    heights_new = new_flow.height_integral(fixed_physical,s,N,6)
    return dict(
        scope="Finite identity diagnostic for the explicit fixed-parameter reinterpretation, not a new solution",
        source_physical_sha256=sha(physical_path), source_raw_sha256=sha(raw_path),
        radial_checks=len(s), angular=N,
        original_nodes=len(s_nodes),
        physical_chart_roundtrip_max=float(np.max(np.abs(s_back-s_nodes))),
        physical_nodes_vs_export_max=float(np.max(np.abs(s_nodes-physical.x))),
        complete_reference_jet_max=errors,
        complete_nonmean_field_twojet_max=field_twojet_error,
        profile_value_first_second_max=profile_error,
        physical_rhs_max=rhs_error, mean_velocity_max=mean_error,
        mean_acceleration_max=mean_derivative_error,
        original_gl6_height_max=float(np.max(np.abs(heights_old-heights_new))),
        inlet_max=float(np.max(np.abs(old.initial(old_p)-obj.initial(new_p)))),
        fixed_parameter_vector=new_p.tolist(),
        no_new_field_solve=True, no_new_tail_solve=True,
        original_gl6_is_true_primitive=False, rigorous_C2_identity_certificate=False,
        fixed_geometry_convergence_proven=False, complete_surface=False)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-run",type=Path,required=True)
    parser.add_argument("--outdir",type=Path,required=True)
    args=parser.parse_args()
    args.outdir.mkdir(parents=True,exist_ok=False)
    record=json.loads(args.source_run.read_text())
    config=dict(source_run=str(args.source_run.resolve()),
                source_run_sha256=sha(args.source_run),
                mean_nodes=int(record["prefix_audit"]["samples_psi"]))
    obj=load_model(config)
    physical=args.source_run.parent/"physical.npz"
    raw=args.source_run.parent/record["raw_return"]["file"]
    report=check_identity(obj,physical,raw)
    report["adapter_sha256"]=sha(__file__)
    report["frozen_contract"]=obj.frozen_geometry_contract
    for name,value in (("model-config.json",config),("identity.json",report)):
        (args.outdir/name).write_text(json.dumps(value,indent=2,allow_nan=False)+"\n")
    print(json.dumps({k:v for k,v in report.items()
                      if k not in ("frozen_contract","fixed_parameter_vector")},indent=2))


if __name__=="__main__":
    main()

