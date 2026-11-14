#!/usr/bin/env python3
"""Reproducible floating checks of the reconstructed exact-affine evaluator."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_phase_geometry import raw_phase_data
from fourfold_phase_symmetric_geometry import load_exact_object, SymmetricAffineGeometry


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--quarter-nodes", type=int, default=256)
    parser.add_argument("--fd-step", type=float, default=2e-6)
    args = parser.parse_args()
    g, _ = load_exact_object(args.object, args.quarter_nodes)
    x = np.array([0., .043, .12, .22, .238])
    theta = np.array([0., .11, .32, .65, 1.1])
    h = args.fd_step
    actual = g.paired_jets(x, theta)
    variation = g.variation_jets(x, theta)[0]
    principal = g.principal_quantities(x, theta, True)
    reference = raw_phase_data(g, g.solver, x, theta, True)
    principal_errors = {key:float(np.max(abs(principal[key]-reference[key])))
                        for key in ("m", "n", "m_theta", "n_theta")}
    principal_errors.update(G=float(np.max(abs(principal["G"]-reference["area"]**2))),
                            m_parameter=float(np.max(abs(principal["m_parameter"]-reference["m_columns"][0]))),
                            n_parameter=float(np.max(abs(principal["n_parameter"]-reference["n_columns"][0]))))
    gp = SymmetricAffineGeometry(g.frozen, g.direction, g.delta+h, g.nodes)
    gm = SymmetricAffineGeometry(g.frozen, g.direction, g.delta-h, g.nodes)
    fd = [float(np.max(abs((a-b)/(2*h)-v))) for a,b,v in zip(
        gp.paired_jets(x,theta)[:6], gm.paired_jets(x,theta)[:6], variation)]
    refined = SymmetricAffineGeometry(g.frozen, g.direction, g.delta, 2*g.nodes)
    diffs = [float(np.max(abs(a-b))) for a,b in zip(actual, refined.paired_jets(x, theta))]
    rotation = lambda z:np.stack((-z[...,1],z[...,0],np.zeros_like(z[...,0])),axis=-1)
    plus, minus = g.paired_jets(x,theta+h), g.paired_jets(x,theta-h)
    angular = {str((i,j)):float(np.max(abs((plus[i]-minus[i])/(2*h)+rotation(actual[i])-actual[j])))
               for i,j in ((0,2),(1,4),(2,5),(3,7),(4,8),(5,9))}
    reflection = [float(np.max(abs(a-b*np.array([1.,1.,-1.])*(-1)**order)))
                  for a,b,order in zip(actual,g.paired_jets(-x,theta),[0,1,0,2,1,0,3,2,1,0])]
    digest = lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
    report = dict(kind="floating_reconstructed_explicit_exact_affine_geometry_preflight",
                  object_sha256=digest(args.object),
                  run_source_sha256=digest(Path(__file__)),
                  geometry_source_sha256=digest(Path(__file__).with_name("fourfold_phase_symmetric_geometry.py")),
                  x=x.tolist(), physical_theta=theta.tolist(),
                  Q256_Q512_maxdifferences=diffs, quarter_nodes=g.nodes,
                  parameter_fd_step=h, parameter_fd_errors=fd,
                  angular_fd_errors=angular, reflection_differences=reflection,
                  principal_formula_comparison=principal_errors,
                  sampled_raw_N=principal["n"].tolist(),
                  sampled_target_K=g.radial_target_metric(x)["K"].tolist(),
                  scope="floating checks only; no directed tail/rounding/ODE certificate")
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({key:report[key] for key in ("Q256_Q512_maxdifferences", "parameter_fd_errors",
                                                "reflection_differences", "principal_formula_comparison")}), flush=True)


if __name__ == "__main__":
    main()
