#!/usr/bin/env python3
"""One actual branch with numerical integration restarted at radial knot cuts.

The exact geometry is unchanged. Nearby binary knots may be clustered for
numerical integration only; no smoothness claim across such clusters is made.
This tests reference residual cost, not a validated ODE solution.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
from types import SimpleNamespace

import numpy as np
from scipy.integrate import solve_ivp as scipy_solve_ivp

import fourfold_phase_exact_affine_nodes as runner
from fourfold_phase_conjugacy_nodes import evaluate_polynomial
from fourfold_phase_symmetric_geometry import load_exact_object


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def radial_cuts(frozen, root, tolerance):
    names = [key for key in frozen if re.fullmatch(
        r"phase_knots|base_knots|shift_knots|mean\d+_knots|height\d+_slope_knots", key)]
    all_knots = np.unique(np.concatenate([np.abs(frozen[key]) for key in names]))
    all_knots = all_knots[(all_knots > 0)&(all_knots < root)]
    groups = []
    for value in all_knots:
        if groups and value-groups[-1][0] <= tolerance:
            groups[-1].append(float(value))
        else:
            groups.append([float(value)])
    positive = np.array([group[0] for group in groups])
    cuts = np.r_[-positive[::-1], 0., positive]
    tau = np.r_[-np.pi/2, np.arcsin(cuts/root), np.pi/2]
    tau = np.unique(tau)
    return tau, dict(source_knot_fields=names, positive_input_knots=len(all_knots),
                     positive_clusters=len(groups), cluster_tolerance=tolerance,
                     largest_cluster_width=max((group[-1]-group[0] for group in groups),default=0.),
                     radial_cut_representatives=cuts.tolist(), tau_cuts=tau.tolist(),
                     semantics="integration mesh only; the exact input function is not altered and omitted close knots may still be crossed")


class KnotAlignedMap(runner.ExactAffineMap):
    def __init__(self, geometry, root, common, cuts, progress=None):
        super().__init__(geometry, root, common, progress)
        self.cuts = cuts

    def _solve_aligned(self, fun, interval, initial, **kwargs):
        start, finish = interval
        low, high = sorted(interval)
        interior = self.cuts[(self.cuts > low)&(self.cuts < high)]
        if finish < start:
            interior = interior[::-1]
        times = np.r_[start, interior, finish]
        current = np.array(initial, copy=True)
        time_rows, state_rows, interpolants = [], [], []
        for index, (left, right) in enumerate(zip(times[:-1], times[1:])):
            options = dict(kwargs)
            options["first_step"] = min(abs(right-left), options.get("max_step", np.inf))
            solved = scipy_solve_ivp(fun, (float(left), float(right)), current, **options)
            if not solved.success:
                return solved
            time_rows.append(solved.t if index == 0 else solved.t[1:])
            state_rows.append(solved.y if index == 0 else solved.y[:, 1:])
            interpolants.extend(solved.sol.interpolants)
            current = solved.y[:, -1]
        return SimpleNamespace(success=True, message="all numerical knot pieces completed",
                               t=np.concatenate(time_rows), y=np.concatenate(state_rows,axis=1),
                               sol=SimpleNamespace(interpolants=interpolants))

    def branch(self, *args, **kwargs):
        # The frozen branch implementation resolves its solver through its
        # module global. Replace only that in-memory callable for this one
        # process, restoring it even on failure; no frozen file is modified.
        original = runner.solve_ivp
        runner.solve_ivp = self._solve_aligned
        try:
            return super().branch(*args, **kwargs)
        finally:
            runner.solve_ivp = original


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object",type=Path,required=True)
    parser.add_argument("--root-certificate",type=Path,required=True)
    parser.add_argument("--dyadic-conjugacy",type=Path,required=True)
    parser.add_argument("--trace-stem",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--comparison-trace",type=Path)
    parser.add_argument("--total-nodes",type=int,default=516)
    parser.add_argument("--first-node",type=int,default=0)
    parser.add_argument("--count",type=int,default=43)
    parser.add_argument("--quarter-nodes",type=int,default=256)
    parser.add_argument("--cluster-tolerance",type=float,default=1e-13)
    parser.add_argument("--tolerance",type=float,default=2e-10)
    parser.add_argument("--progress",type=Path)
    args=parser.parse_args()
    geometry,definition=load_exact_object(args.object,args.quarter_nodes)
    root=json.loads(args.root_certificate.read_text())
    if (not root["proved"] or root["delta_binary64_hex"]!=definition["delta_hex"]
        or root["origin_inputs_sha256"]!=definition["origin_inputs"]["sha256"]
        or root["frozen_direction_sha256"]!=definition["direction"]["sha256"]):
        raise ValueError("root belongs to another exact affine object")
    cuts,cut_metadata=radial_cuts(geometry.frozen,root["root_center"],args.cluster_tolerance)
    common=dict(source_sha256=digest(args.object),object_file=str(args.object),
                origin_inputs_sha256=definition["origin_inputs"]["sha256"],
                curve_direction_sha256=definition["direction"]["sha256"],
                exact_delta_fraction=root["exact_delta_fraction"],
                root_certificate_sha256=digest(args.root_certificate),
                dyadic_conjugacy_sha256=digest(args.dyadic_conjugacy),
                run_source_sha256=digest(Path(__file__)),
                base_runner_source_sha256=digest(Path(runner.__file__)),
                geometry_source_sha256=digest(Path(__file__).with_name("fourfold_phase_symmetric_geometry.py")),
                integration_strategy="restart DOP853 at numerical radial knot representatives",
                knot_alignment=cut_metadata,total_initial_grid_nodes=args.total_nodes,
                first_node=args.first_node,ray_count=args.count,
                ode_rtol=args.tolerance,quarter_nodes=args.quarter_nodes)
    mapper=KnotAlignedMap(geometry,root["root_center"],common,cuts,args.progress)
    x=np.arange(args.total_nodes)*2*np.pi/args.total_nodes
    H=x+evaluate_polynomial(json.loads(args.dyadic_conjugacy.read_text()),x)
    initial=(H/4)[args.first_node:args.first_node+args.count]
    if len(initial)!=args.count:raise ValueError("requested initial nodes leave the grid")
    args.trace_stem.parent.mkdir(parents=True,exist_ok=True)
    result,traces=mapper.branch(initial,-1.,-np.pi/2,np.pi/2,args.tolerance,args.trace_stem)
    report=dict(kind="floating_numerical_knot_aligned_forward_reference_probe",**common,
                target_root=mapper.root,root_parameter_derivative=mapper.root_parameter_derivative,
                initial_angles=initial.tolist(),final_angles=result[0].tolist(),
                final_jacobian=result[1].tolist(),final_parameter_column=result[2].tolist(),
                traces=traces,rhs_calls=mapper.calls,
                limitations=["fresh floating branch, no ODE or interval residual certificate",
                    "close binary knot clustering changes only numerical partition, not the geometry",
                    "endpoint/root-quotient and finite primitive arithmetic costs remain unpaid"])
    if args.comparison_trace:
        comparison=runner.load_npz(args.comparison_trace)
        same=np.array_equal(comparison["initial_angles"],initial)
        if not same:raise ValueError("comparison branch has different floating initial angles")
        old_identity=json.loads(str(comparison["metadata"]))["identity"]
        for key in ("source_sha256","root_certificate_sha256","dyadic_conjugacy_sha256"):
            if old_identity[key]!=common[key]:raise ValueError("comparison uses different object/root/H")
        report["comparison"]=dict(trace_sha256=digest(args.comparison_trace),
            exact_saved_initial_angles_match=same,
            maximum_final_angle_difference=float(np.max(abs(result[0]-comparison["final_angles"]))),
            maximum_final_J_difference=float(np.max(abs(result[1]-comparison["final_jacobian"]))),
            maximum_final_parameter_difference=float(np.max(abs(result[2]-comparison["final_parameter_column"]))))
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps({key:report[key] for key in ("rhs_calls","comparison") if key in report}),flush=True)


if __name__=="__main__":main()
