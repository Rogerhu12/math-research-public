#!/usr/bin/env python3
"""Physical material readout of an accepted independent-mode full-DN field.

Uses the same saved-y/saved-RHS/finite-ODE-second physical quintic as the
closed assembly.  Both normalized Gram components and their true relative
operator norm are reported.  Display meshes play no role in this readout.
Samples at two grids do not certify a continuous bound or fixed-g BVP
convergence; the scalar formula and source/field dimensions remain explicit.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import time

for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import numpy as np

import geometry_20261114_material_quintic_readout as material
from geometry_20261114_lifted_modes_saved_prefix import (
    LiftedModesSavedPrefix, actions_only, sha)


HERE = Path(__file__).resolve().parent


def main():
    actions_only()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--angles", type=int, nargs="+", default=[2048, 4096])
    parser.add_argument("--radial-subdivisions", type=int, nargs="+", default=[2, 4])
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if len(args.angles) != len(args.radial_subdivisions):
        raise ValueError("Specify one angular count for each radial subdivision level")
    started = time.monotonic()
    saved = LiftedModesSavedPrefix(args.input)
    M, N, x, core = saved.M, saved.N, saved.sol.x, saved.core
    if (any(count < 4*(M+1) or count & (count-1) for count in args.angles)
            or any(count < 1 for count in args.radial_subdivisions)):
        raise ValueError("Use powers-of-two material-angle grids resolving the complete field and positive subdivisions")
    major = 1+float(core.sum())
    minor = 1+float(np.sum(core*(-1.)**np.arange(1, M+1)))
    witness = np.array([0., major, 0.])
    levels = []
    for angular, subdivision in zip(args.angles, args.radial_subdivisions):
        phi, rho, rhop, inverse = material.material_angles(core, angular)
        if np.min(rho) <= 0:
            raise ValueError("The material-angle map lost regularity at a requested sample")
        evaluate = material.angular_jet(None, M, phi)
        co, si = np.cos(phi), np.sin(phi)
        operator_max = component_max = curvature_max = twice_norm = 0.
        min_determinant = min_distance = np.inf
        worst_operator = worst_curvature = None
        interval_rows = []
        for j in range(len(x)-1):
            row = dict(interval=j, s_left=float(x[j]), s_right=float(x[j+1]),
                       metric_relative_operator_sample=0., metric_component_sample=0.,
                       curvature_sample=0.)
            for k in range(subdivision+1):
                if j and k == 0:
                    continue
                if k == 0:
                    s = float(x[j])
                elif k == subdivision:
                    s = float(x[j+1])
                else:
                    s = float(np.longdouble(x[j])+(np.longdouble(x[j+1])-x[j])*k/subdivision)
                states = np.array([saved.quintic([s], d)[:, 0] for d in range(3)])
                values, first, second = evaluate(states)
                F, Fs, Fss = values
                Ft, Fst = first[0]/rho[:, None], first[1]/rho[:, None]
                Ftt = second[0]/rho[:, None]**2-first[0]*(rhop/rho**3)[:, None]
                a, _, _ = saved.profile(s)
                E = np.einsum("ij,ij->i", Fs, Fs)
                mixed = np.einsum("ij,ij->i", Fs, Ft)
                G = np.einsum("ij,ij->i", Ft, Ft)
                ee, ff, gg = E-1., mixed/a, G/a**2-1.
                component = np.maximum.reduce([abs(ee), abs(ff), abs(gg)])
                operator = (abs(ee+gg)+np.sqrt((ee-gg)**2+4*ff**2))/2
                determinant = E*G-mixed*mixed
                normal = np.cross(Fs, Ft)
                area = np.linalg.norm(normal, axis=1)
                if np.min(area) <= 0 or not np.all(np.isfinite(area)) or np.min(determinant) <= 0:
                    raise FloatingPointError("Nonregular physical sample at interval="+str(j)+", s="+repr(s))
                normal /= area[:, None]
                e = np.einsum("ij,ij->i", Fss, normal)
                f = np.einsum("ij,ij->i", Fst, normal)
                g = np.einsum("ij,ij->i", Ftt, normal)
                trace = (e*G+g*E-2*f*mixed)/determinant
                gauss = (e*g-f*f)/determinant
                curvatures = (abs(trace)+np.sqrt(np.maximum(0., trace*trace-4*gauss)))/2
                metric_value = float(operator.max())
                curvature_value = float(curvatures.max())
                if metric_value > operator_max:
                    at = int(np.argmax(operator))
                    operator_max = metric_value
                    worst_operator = dict(interval=j, s=s, theta=float(2*np.pi*at/angular),
                        phi=float(phi[at]), relative_operator=metric_value,
                        normalized_Gram_error=[float(ee[at]), float(ff[at]), float(gg[at])])
                if curvature_value > curvature_max:
                    at = int(np.argmax(curvatures))
                    curvature_max = curvature_value
                    worst_curvature = dict(interval=j, s=s, theta=float(2*np.pi*at/angular),
                        phi=float(phi[at]), absolute_principal_curvature=curvature_value)
                component_max = max(component_max, float(component.max()))
                xyz = np.stack([co*F[:, 0]-si*F[:, 1], si*F[:, 0]+co*F[:, 1], F[:, 2]], axis=1)
                min_distance = min(min_distance, float(np.linalg.norm(xyz-witness, axis=1).min()))
                twice_norm = max(twice_norm, 2*float(np.linalg.norm(xyz, axis=1).max()))
                min_determinant = min(min_determinant, float(determinant.min()))
                row["metric_relative_operator_sample"] = max(row["metric_relative_operator_sample"], metric_value)
                row["metric_component_sample"] = max(row["metric_component_sample"], float(component.max()))
                row["curvature_sample"] = max(row["curvature_sample"], curvature_value)
            interval_rows.append(row)
            if (j+1) % 100 == 0:
                print(json.dumps(dict(event="independent_modes_material_quintic", field_modes=M,
                    angles=angular, radial_subdivisions=subdivision, intervals=j+1,
                    metric_operator=operator_max, metric_component=component_max,
                    curvature=curvature_max, seconds=time.monotonic()-started)), flush=True)
        level = dict(angles=angular, radial_subdivisions=subdivision,
            radial_sample_count=(len(x)-1)*subdivision+1,
            metric_relative_operator_sample=operator_max, metric_component_sample=component_max,
            curvature_sample=curvature_max, minimum_metric_determinant_sample=min_determinant,
            witness_minimum_over_prefix_samples=min_distance,
            reflected_prefix_twice_max_sample_norm=twice_norm,
            witness_value_is_continuous_Hausdorff_lower_bound=False,
            diameter_value_is_whole_closed_D_upper=False,
            worst_metric=worst_operator, worst_curvature=worst_curvature,
            angle_inversion=inverse, interval_rows=interval_rows)
        levels.append(level)
        print(json.dumps({key:value for key,value in level.items() if key != "interval_rows"}), flush=True)
    report = dict(schema="independent-modes-full-state-material-readout-v1", scope=__doc__,
        mode_identity=saved.mode_identity, complete_saved_prefix_definition=saved.definition,
        input_sha256=sha(args.input), source_sha256=sha(__file__),
        scalar_specification=saved.rec["fixed_scalar_profile"]["geometry"],
        field_representation=saved.rec["field_representation"],
        M=M, base_angular=N, node_count=len(x), source_prefix_M=saved.mode_identity["actual_accepted_source_prefix_modes"],
        core_axis_support_gap=major-minor,
        cut_material_mean_012=[float(v[0]) for v in saved.mean_jets([saved.flow.end])],
        old_mean_added=False, scalar_controls_frozen=True,
        metric_operator_definition="spectral norm of [[E-1,F/a],[F/a,G/a^2-1]]",
        physical_field_definition="The identical complete saved-state physical quintic used by LiftedModesSavedPrefix and the closed assembly",
        levels=levels, seconds=time.monotonic()-started,
        numerical_readout_grid_refinement_only=True,
        new_fixed_g_BVP_refinement_created=False,
        continuous_metric_certificate=False, continuous_reach_certificate=False,
        closed_surface=False, task_completed=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")


if __name__ == "__main__":
    main()
