#!/usr/bin/env python3
"""Focused R53 implementation checks; no BVP or surface-existence claim.

This check source itself was saved without execution access. The JSON records
only the actual later run. Pass --support-source for the original, genuine
fixed_metric_mode3_core.py; no reconstructed coefficient metadata is accepted.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import traceback
import numpy as np


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def maximum_norm(a):
    return float(np.max(np.linalg.norm(a, axis=-1)))


def verify_factory(factory_builder, n, q, corrections, settings, label):
    factory = factory_builder(settings)
    core = factory(q, corrections, base_mode=n)
    T, L = 2.*math.pi/n, math.pi/n
    theta = np.linspace(.0013, 2.*math.pi+.0013, 73, endpoint=False)
    g = core.evaluate(theta)
    row = dict(label=label, base_mode=n, q=q, settings=settings,
               speed_error=float(np.max(np.abs(np.sum(g["Ft"]**2, axis=1)-1.))),
               closure_error=maximum_norm(
                   core.evaluate(np.array([0.]))["F"]-
                   core.evaluate(np.array([2.*math.pi]))["F"]),
               minimum_sampled_curvature=float(g["kappa"].min()),
               curvature_lower_bound=float(core.curvature_lower_bound))
    step = 2.e-6
    plus, minus = core.evaluate(theta+step), core.evaluate(theta-step)
    row["material_first_derivative_error"] = maximum_norm(
        (plus["F"]-minus["F"])/(2.*step)-g["Ft"])
    row["material_second_derivative_error"] = maximum_norm(
        (plus["Ft"]-minus["Ft"])/(2.*step)-g["Ftt"])
    if settings["homotopy"] == 1.:
        arc_theta = L+settings["halfwidth"]*np.linspace(-.99, .99, 29)
        arc = core.evaluate(arc_theta)
        normal = np.column_stack((np.cos(arc["phi"]), np.sin(arc["phi"]),
                                  np.zeros(len(arc_theta))))
        centers = arc["F"]-normal/core.k
        row["circle_curvature_error"] = float(np.max(np.abs(arc["kappa"]-core.k)))
        row["circle_center_error"] = maximum_norm(centers-centers[len(centers)//2])
        row["circle_phase_error"] = float(np.max(np.abs(
            arc["phi"]-(L+core.k*(arc_theta-L)))))
    jets = factory.parameter_jets(core, theta)
    params = np.r_[q, np.asarray(corrections, float)]
    fd = []
    for index in sorted(set((0, 1, len(params)-1))):
        h = 2.e-7
        pplus, pminus = params.copy(), params.copy()
        pplus[index] += h
        pminus[index] -= h
        gp = factory(pplus[0], pplus[1:], base_mode=n).evaluate(theta)
        gm = factory(pminus[0], pminus[1:], base_mode=n).evaluate(theta)
        errors = []
        for jet, key in zip(jets, ("F", "Ft", "Ftt")):
            delta = (gp[key]-gm[key])/(2.*h)
            errors.append(maximum_norm(delta-jet[index]) /
                          max(1., maximum_norm(jet[index])))
        fd.append(dict(parameter_index=index, relative_jet_errors=errors))
    row["parameter_finite_differences"] = fd
    flags = [
        row["speed_error"] < 2.e-12,
        row["closure_error"] < 2.e-10,
        row["material_first_derivative_error"] < 3.e-6,
        row["material_second_derivative_error"] < 3.e-6,
        row["minimum_sampled_curvature"]+1.e-8 >= row["curvature_lower_bound"],
        max(error for item in fd for error in item["relative_jet_errors"]) < 5.e-6,
    ]
    if settings["homotopy"] == 1.:
        flags.extend(row[key] < 3.e-10 for key in
                     ("circle_curvature_error", "circle_center_error", "circle_phase_error"))
    row["passed"] = bool(all(flags))
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--support-source", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    folder = Path(__file__).resolve().parent
    support_path = folder/"material_flattened_support_core.py"
    generic_path = folder/"material_flattened_generic_core.py"
    old = load_module(args.support_source, "_r53_original_support")
    adapter = load_module(support_path, "_r53_support_adapter")
    generic = load_module(generic_path, "_r53_generic_adapter")
    reference = old.PlanarSupportCore
    corrections = (.0002, -.00001, .0000002, 0., 0., 0., 0.)
    theta = np.linspace(0., 2.*np.pi, 127, endpoint=False)
    original = reference(.06, corrections, base_mode=3)
    identity = adapter.make_factory(reference, dict(homotopy=0.))(
        .06, corrections, base_mode=3)
    gi, go = identity.evaluate(theta), original.evaluate(theta)
    identity_passed = (type(identity) is type(original) and all(
        np.array_equal(gi[key], go[key]) for key in ("F", "Ft", "Ftt", "kappa")))
    report = dict(
        scope="R53 core implementation checks only; no BVP, metric tail or surface claim",
        source_sha256={str(path.name): hashlib.sha256(path.read_bytes()).hexdigest()
                       for path in (args.support_source, support_path, generic_path)},
        lambda0_original_type_and_arrays_identical=bool(identity_passed),
        rows=[])
    make_support = lambda settings: adapter.make_factory(reference, settings)

    def old_rho_jets(core, t):
        f = adapter._support_fields(core, t)
        k, ku, kuu = f["kappa"], f["kappa_u"], f["kappa_uu"]
        return dict(rho=1./k, rho_u=-ku/k**2,
                    rho_uu=2.*ku**2/k**3-kuu/k**2)

    make_generic = lambda settings: generic.make_factory(
        reference, settings, parameter_jets_provider=adapter.parameter_jets,
        rho_material_jets_provider=old_rho_jets,
        curvature_derivative_bounds_provider=adapter._support_curvature_derivative_bounds)
    cases = [
        (make_support, 3, .06, corrections,
         dict(homotopy=.02, curvature_blend=0., halfwidth=.21,
              transition=.25, target_curvature=.2), "support-m3-small-lambda"),
        (make_support, 3, .06, corrections,
         dict(homotopy=1., curvature_blend=0., halfwidth=.21,
              transition=.25, target_curvature=.2), "support-m3-circle-old-center-k"),
        (make_support, 3, .06, corrections,
         dict(homotopy=1., curvature_blend=1., halfwidth=.21,
              transition=.25, target_curvature=.2), "support-m3-circle-k02"),
        (make_generic, 4, .03, corrections[:5],
         dict(homotopy=.02, curvature_blend=0., halfwidth=.2,
              transition=.25, target_curvature=.2), "generic-m4-explicit-support-provider"),
    ]
    for case in cases:
        try:
            report["rows"].append(verify_factory(*case))
        except Exception as error:
            report["rows"].append(dict(label=case[-1], passed=False,
                                       error=str(error), traceback=traceback.format_exc()))
        print(json.dumps(report["rows"][-1]), flush=True)
    report["passed"] = bool(identity_passed and all(row["passed"] for row in report["rows"]))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
