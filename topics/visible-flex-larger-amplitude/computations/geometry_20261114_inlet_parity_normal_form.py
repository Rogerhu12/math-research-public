#!/usr/bin/env python3
"""R249 shared-node inlet parity normal form for an accepted complete field.

Only the first node's z value, horizontal s derivative and z second s
derivative are projected to zero.  The unique real quintic through the
shared binary-rational nodal jets defines the finite C2 field.  Floating
coefficients/evaluation approximate that definition; they are not claimed
to satisfy every polynomial identity bit for bit.  All other physical
nodes, the complete fixed scalar, material map, actual tail input and cut
nine jets are retained.  This postprocessing never creates BVP acceptance.

Numerical use is restricted to this public repository's Actions.  The
normalize_inlet(saved) API accepts either the v3 or the independent v4
SavedPrefix; read_saved dispatches without inventing active scalar rows.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib
import json
import math
import os
from fractions import Fraction as Q
from pathlib import Path
import sys
from types import SimpleNamespace

for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import numpy as np

import geometry_20261114_large_core_saved_prefix as original
import geometry_20261114_material_quintic_readout as material


HERE = Path(__file__).resolve().parent
SCHEMA = "shared-binary-node-inlet-parity-Hermite-normal-form-v1"
V3 = "complete-prefix-controls-independent-field-modes-v3"
V4 = "frozen-complete-scalar-same-metric-refinement-v4"
read, sha, actions_only = original.read, original.sha, original.actions_only
BERNSTEIN = ((Q(1), Q(2, 5), Q(1, 20)),
             (Q(5), Q(2), Q(1, 4)),
             (Q(20), Q(12), Q(2)))
LEFT_BASIS = ((Q(1), Q(0), Q(0), Q(-10), Q(15), Q(-6)),
              (Q(0), Q(1), Q(0), Q(-6), Q(8), Q(-3)),
              (Q(0), Q(0), Q(1, 2), Q(-3, 2), Q(3, 2), Q(-1, 2)))


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False).encode("utf-8")).hexdigest()


def array_sha(value):
    array = np.asarray(value, dtype="<f8", order="C")
    return hashlib.sha256(str(array.shape).encode("ascii") + b"\0" + array.tobytes()).hexdigest()


def exact_upper(value):
    value = Q(value)
    return dict(exact=str(value), binary64_upper=math.nextafter(float(value), math.inf))


def sqrt_upper(value, bits=80):
    """A rational upper square root; used only for conditional inequalities."""
    value = Q(value)
    if value < 0:
        raise ValueError("A square-root bound requires a nonnegative number")
    scale = 1 << bits
    whole = math.isqrt(value.numerator * scale * scale // value.denominator)
    if Q(whole * whole, scale * scale) < value:
        whole += 1
    return Q(whole, scale)


def _l1_angular(vector, M, derivative):
    """Euclidean world-vector Fourier bound, including the rotating XY frame."""
    values = [Q(float(v)) for v in vector]
    return (sum(Q((2*m+1)**derivative) * abs(values[m]) for m in range(M+1))
        + sum(Q((2*m+1)**derivative) * abs(values[M+m]) for m in range(1, M+1))
        + sum(Q((2*m)**derivative) * abs(values[2*M+1+m]) for m in range(M+1)))


def _patch_bounds(saved, differences, h):
    l1 = [[_l1_angular(v, saved.M, j) for j in range(3)] for v in differences]
    phi = [[sum(h**(k-i) * BERNSTEIN[i][k] * l1[k][j] for k in range(3))
            for j in range(3)] for i in range(3)]
    rho = Q(saved.rho_lower_exact)
    if rho <= 0:
        raise ValueError("Use the same positive complete-core material-inverse bound")
    rhop = sum(2*m*(4*m*m-1)*abs(Q(float(c))) for m, c in enumerate(saved.core, 1))
    theta = [[v[0], v[1]/rho, v[2]/rho**2 + v[1]*rhop/rho**3] for v in phi]
    return dict(derivative_order="row=s order 0,1,2; column=angle order 0,1,2",
        Bernstein_absolute_bounds=[[str(v) for v in row] for row in BERNSTEIN],
        delta_nodal_world_phi_L1=[[str(v) for v in row] for row in l1],
        world_phi_jet_bounds=[[exact_upper(v) for v in row] for row in phi],
        material_theta_jet_bounds=[[exact_upper(v) for v in row] for row in theta],
        rho_lower_exact=str(rho), rho_phi_absolute_upper_exact=str(rhop),
        continuous_bounds_for="Difference of the two exact shared-node Hermite normal forms; numerical evaluation errors are separate"), theta


def _exact_cell_witness(differences, h):
    """Check both endpoint jets of the correction using rational arithmetic."""
    delta = [[Q(float(v)) for v in row] for row in differences]
    coefficients = [[sum(h**k * LEFT_BASIS[k][j] * delta[k][m] for k in range(3))
                     for m in range(len(delta[0]))] for j in range(6)]
    checks = 0
    for order in range(3):
        for m in range(len(delta[0])):
            left = math.factorial(order)*coefficients[order][m]/h**order
            right = sum(Q(math.factorial(j), math.factorial(j-order))*coefficients[j][m]
                        for j in range(order, 6))/h**order
            if left != delta[order][m] or right != 0:
                raise AssertionError("The exact inlet Hermite correction failed its endpoint identity")
            checks += 2
    strings = [[str(v) for v in row] for row in coefficients]
    return dict(width_exact=str(h), correction_left_jets_exact=[[str(v) for v in row] for row in delta],
        exact_unit_interval_power_coefficients_sha256=canonical_sha(strings),
        exact_endpoint_component_identities_checked=checks,
        correction_right_0_1_2_jets_identically_zero=True)


def normalize_inlet(saved):
    """Mutate one SavedPrefix's finite readout, retaining its original record.

    The caller must use this same object/definition in its mesh and spatial
    cover.  The original accepted checkpoint is never edited or reclassified.
    """
    actions_only()
    if getattr(saved, "inlet_normalization", {}).get("enabled"):
        return saved
    old = saved.quintic
    x = np.asarray(saved.sol.x, float)
    if len(x) < 2 or x[0] != 0. or saved.n != 3*saved.M+2:
        raise ValueError("The original complete physical chart must start at its reflection inlet s=0")
    if any(v.shape != (len(x), saved.n) or not np.all(np.isfinite(v)) for v in old.nodal):
        raise ValueError("Retain all finite shared physical value/first/second nodal jets")
    nodal = [v.copy() for v in old.nodal]
    iz = 2*saved.M+1
    nodal[0][0, iz:] = 0.
    nodal[1][0, :iz] = 0.
    nodal[2][0, iz:] = 0.
    differences = np.asarray([v[0]-before[0] for v, before in zip(nodal, old.nodal)])
    new = original.PhysicalQuintic(x, *nodal)
    if (not all(np.array_equal(a[1:], b[1:]) for a, b in zip(old.nodal, new.nodal))
            or not np.array_equal(old.coefficients[1:], new.coefficients[1:])):
        raise AssertionError("The inlet normal form may not change another node or radial cell")
    h = Q(float(x[1]))-Q(float(x[0]))
    bounds, _ = _patch_bounds(saved, differences, h)
    witness = _exact_cell_witness(differences, h)
    reader_module = sys.modules[type(saved).__module__]
    record = dict(enabled=True, normal_form_schema=SCHEMA, theorem="R249",
        source_sha256=sha(__file__), original_input_sha256=sha(saved.path),
        source_reader_identity=dict(class_name=type(saved).__name__,
            source_file=Path(reader_module.__file__).name, source_sha256=sha(reader_module.__file__),
            mode_identity=copy.deepcopy(saved.mode_identity)),
        original_nodal_jet_sha256=[array_sha(v) for v in old.nodal],
        normal_form_nodal_jet_sha256=[array_sha(v) for v in new.nodal],
        first_cell=[0., float(x[1])], unchanged_after_s=float(x[1]),
        shared_node_jet_projection={"value": "Only all z0..zM coefficients at node 0 become zero",
            "first_s": "Only all r0..rM,t1..tM coefficients at node 0 become zero",
            "second_s": "Only all z0..zM coefficients at node 0 become zero"},
        exact_binary_node_definition="Each binary64 node and shared jet is an exact rational; each interval is its unique real quintic Hermite interpolant",
        first_cell_coefficient_identity_sha256=witness["exact_unit_interval_power_coefficients_sha256"],
        exact_endpoint_component_identities_checked=witness["exact_endpoint_component_identities_checked"],
        exact_reflection_inlet_C2_in_this_normal_form=True,
        literal_rounded_polynomial_C2_identity_certified=False,
        floating_evaluation_is_approximation_to_normal_form=True,
        every_other_node_and_cell_retained=True, complete_material_inverse_retained=True,
        cut_0_1_2_s_jets_and_all_angular_derivatives_retained=True,
        actual_tail_H_and_DN_input_retained=True, cut_material_mean_0_1_2_retained=True,
        single_planar_SE2_fit_input_retained=True, reflection_plane="z=0; the prefix gauge changes only XY",
        full_scalar_specification_sha256=canonical_sha(saved.rec["fixed_scalar_profile"]["geometry"]),
        fixed_scalar_formula_changed=False, original_accepted_checkpoint_edited=False,
        new_nonlinear_BVP_acceptance_created=False, exact_isometry_certified=False,
        closed_surface_C2_away_from_inlet_certified_here=False, continuous_patch_jet_bounds=bounds)
    saved.original_quintic = old
    saved.inlet_exact_correction_witness = witness
    saved.inlet_normalization = record
    saved.quintic = new
    saved.sol = SimpleNamespace(x=saved.sol.x, y=new.nodal[0].T, p=saved.sol.p, sol=new)
    saved.kind = "complete-full-state-material-quintic-with-inlet-parity-normal-form"
    saved.definition = copy.deepcopy(saved.definition)
    if "node_saved_vs_local_RHS_max" in saved.definition:
        saved.definition["original_node_saved_vs_local_RHS_max_before_normalization"] = saved.definition.pop("node_saved_vs_local_RHS_max")
    saved.definition.update(inlet_normalization=record,
        polynomial="Unique exact shared-binary-node physical Hermite quintic, with only the three inlet parity blocks projected as recorded",
        original_BVP_acceptance_is_source_provenance_only=True,
        numerical_postprocessing_is_not_a_resolved_BVP=True)
    return saved


def read_saved(checkpoint, normalize=True):
    actions_only()
    schema = read(checkpoint)["fixed_scalar_profile"]["geometry"].get("schema")
    if schema == V3:
        from geometry_20261114_lifted_modes_saved_prefix import LiftedModesSavedPrefix
        saved = LiftedModesSavedPrefix(checkpoint)
    elif schema == V4:
        from geometry_20261114_same_metric_saved_prefix import SameMetricSavedPrefix
        saved = SameMetricSavedPrefix(checkpoint)
    else:
        raise ValueError("Use a genuinely accepted complete v3 design or v4 same-metric field")
    return normalize_inlet(saved) if normalize else saved


def first_cell_scalar_lower(saved):
    """Use the original exact scalar quintics only if controls vanish here."""
    specification = saved.rec["fixed_scalar_profile"]["geometry"]
    if specification.get("schema") == V4:
        specification = specification["frozen_design_scalar_profile"]
    base = specification["base_prefix_geometry"]
    end = Q(float(saved.sol.x[1]))
    knots = base["knots"]
    if (Q(float(knots[0]["s"])) != 0 or Q(float(knots[-1]["s"])) < end
            or Q(float(specification["base_prefix_end"])) < end
            or any(Q(float(left)) < end for left, _ in specification["control_supports_binary64"])):
        return dict(available=False, reason="The whole first cell is not inside the original scalar-quintic prefix before every design control"), None
    jets = [[Q(float(row[key])) for key in ("a", "ap", "app")] for row in knots]
    jets[0] = list(material.base.fixed.exact_original_jet(base["initial_law"], 0.))
    controls, intervals = [], []
    for j in range(len(knots)-1):
        left, right = Q(float(knots[j]["s"])), Q(float(knots[j+1]["s"]))
        if left >= end:
            break
        h = right-left
        a, ap, app = jets[j]
        b, bp, bpp = jets[j+1]
        controls.extend((a, a+h*ap/5, a+2*h*ap/5+h*h*app/20,
                         b-2*h*bp/5+h*h*bpp/20, b-h*bp/5, b))
        intervals.append(j)
    lower = min(controls)
    if lower <= 0:
        return dict(available=False, reason="This original scalar Bernstein hull is not positive",
                    hull_lower_exact=str(lower)), None
    return dict(available=True, lower_exact=str(lower), original_scalar_intervals=intervals,
        proof="R249 scalar Bernstein convex hull on all original intervals meeting the first physical cell",
        first_original_knot_jet_recomputed_from_exact_original_law=True,
        all_design_controls_vanish_on_first_cell=True,
        scalar_formula_refitted=False), lower


def _statistics(evaluate, states, rho, rhop, a):
    value, first, second = evaluate(states)
    F, Fs, Fss = value
    Ft, Fst = first[0]/rho[:, None], first[1]/rho[:, None]
    Ftt = second[0]/rho[:, None]**2-first[0]*(rhop/rho**3)[:, None]
    E = np.einsum("ij,ij->i", Fs, Fs)
    mixed = np.einsum("ij,ij->i", Fs, Ft)
    G = np.einsum("ij,ij->i", Ft, Ft)
    ee, ff, gg = E-1., mixed/a, G/a**2-1.
    component = np.maximum.reduce([abs(ee), abs(ff), abs(gg)])
    operator = (abs(ee+gg)+np.sqrt((ee-gg)**2+4*ff**2))/2
    determinant = E*G-mixed*mixed
    normal = np.cross(Fs, Ft)
    area = np.linalg.norm(normal, axis=1)
    if not all(np.all(np.isfinite(v)) for v in (operator, determinant, area)):
        raise FloatingPointError("Nonfinite inlet physical readout")
    regular = bool(np.all(area > 0) and np.all(determinant > 0))
    curvature = None
    if regular:
        normal /= area[:, None]
        e = np.einsum("ij,ij->i", Fss, normal)
        f = np.einsum("ij,ij->i", Fst, normal)
        g = np.einsum("ij,ij->i", Ftt, normal)
        trace = (e*G+g*E-2*f*mixed)/determinant
        gauss = (e*g-f*f)/determinant
        curvature = (abs(trace)+np.sqrt(np.maximum(0., trace*trace-4*gauss)))/2
    jets = dict(pos=F, s1=Fs, p1=Ft, s2=Fss, sp=Fst, p2=Ftt)
    return dict(metric_operator=float(operator.max()), metric_component=float(component.max()),
        maximum_absolute_principal_curvature=float(curvature.max()) if regular else None,
        minimum_metric_determinant=float(determinant.min()), all_samples_immersed=regular,
        worst_operator_angular_index=int(np.argmax(operator)),
        worst_curvature_angular_index=int(np.argmax(curvature)) if regular else None), jets


def audit(arguments):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--angles", type=int, nargs="+", default=[2048, 4096])
    parser.add_argument("--radial-subdivisions", type=int, nargs="+", default=[16, 32])
    parser.add_argument("--old-metric-bound", type=float,
        help="Optional independently supplied continuous old operator bound; this audit does not establish that hypothesis")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(arguments)
    saved = read_saved(args.checkpoint)
    if (len(args.angles) != len(args.radial_subdivisions)
            or any(n < 4*(saved.M+1) or n & (n-1) for n in args.angles)
            or any(n < 1 for n in args.radial_subdivisions)):
        raise ValueError("Use paired positive radial subdivisions and resolving power-of-two angular grids")
    levels = []
    for angular, subdivision in zip(args.angles, args.radial_subdivisions):
        phi, rho, rhop, inversion = material.material_angles(saved.core, angular)
        evaluate = material.angular_jet(None, saved.M, phi)
        pair = {name:dict(metric_operator=0., metric_component=0.,
            maximum_absolute_principal_curvature=0., minimum_metric_determinant=math.inf,
            all_samples_immersed=True, worst_metric=None, worst_curvature=None) for name in ("original", "normalized")}
        jet_difference = {key:0. for key in ("pos", "s1", "p1", "s2", "sp", "p2")}
        inlet = {}
        h = np.longdouble(saved.sol.x[1])
        for k in range(subdivision+1):
            s = float(h*k/subdivision)
            outputs = {}
            for name, quintic in (("original", saved.original_quintic), ("normalized", saved.quintic)):
                states = np.array([quintic([s], order)[:, 0] for order in range(3)])
                result, jets = _statistics(evaluate, states, rho, rhop, saved.profile(s)[0])
                outputs[name] = jets
                target = pair[name]
                if result["metric_operator"] > target["metric_operator"]:
                    at = result["worst_operator_angular_index"]
                    target["worst_metric"] = dict(s=s, theta=float(2*np.pi*at/angular), phi=float(phi[at]))
                for key in ("metric_operator", "metric_component"):
                    target[key] = max(target[key], result[key])
                target["minimum_metric_determinant"] = min(target["minimum_metric_determinant"], result["minimum_metric_determinant"])
                target["all_samples_immersed"] &= result["all_samples_immersed"]
                if not result["all_samples_immersed"]:
                    target["maximum_absolute_principal_curvature"] = None
                elif target["maximum_absolute_principal_curvature"] is not None and result["maximum_absolute_principal_curvature"] > target["maximum_absolute_principal_curvature"]:
                    target["maximum_absolute_principal_curvature"] = result["maximum_absolute_principal_curvature"]
                    at = result["worst_curvature_angular_index"]
                    target["worst_curvature"] = dict(s=s, theta=float(2*np.pi*at/angular), phi=float(phi[at]))
                if k == 0:
                    inlet[name] = dict(z_value_sample=float(abs(jets["pos"][:, 2]).max()),
                        horizontal_Fs_sample=float(np.linalg.norm(jets["s1"][:, :2], axis=1).max()),
                        z_Fss_sample=float(abs(jets["s2"][:, 2]).max()))
            for key in jet_difference:
                jet_difference[key] = max(jet_difference[key], float(np.linalg.norm(outputs["normalized"][key]-outputs["original"][key], axis=1).max()))
        levels.append(dict(angles=angular, radial_subdivisions=subdivision,
            radial_samples=subdivision+1, angle_inversion=inversion, fields=pair,
            inlet_residual_samples=inlet, patch_six_jet_sample_max=jet_difference))
    scalar_bound, lower = first_cell_scalar_lower(saved)
    conditional = dict(continuous_old_metric_bound_established_here=False,
        formula="eta_new <= eta + 2*sqrt(1+eta)*epsilon + epsilon^2",
        epsilon_squared_formula="e10^2 + (e01/a_lower)^2", assumptions="a>=a_lower>0 and old normalized Gram operator error<=eta on the whole first cell")
    if lower is not None:
        jet_bounds = saved.inlet_normalization["continuous_patch_jet_bounds"]["material_theta_jet_bounds"]
        e10, e01 = Q(jet_bounds[1][0]["exact"]), Q(jet_bounds[0][1]["exact"])
        eps2 = e10*e10+(e01/lower)**2
        conditional["epsilon_squared_exact_upper"] = str(eps2)
        if args.old_metric_bound is not None:
            if not np.isfinite(args.old_metric_bound) or args.old_metric_bound < 0:
                raise ValueError("The supplied old metric bound must be finite and nonnegative")
            eta = Q(float(args.old_metric_bound))
            upper = eta+2*sqrt_upper((1+eta)*eps2)+eps2
            conditional.update(supplied_old_eta_exact=str(eta),
                new_eta_conditional_upper=exact_upper(upper),
                old_eta_is_external_hypothesis_not_a_sample_max=True)
    result = dict(schema="inlet-parity-normal-form-audit-v1", source_sha256=sha(__file__),
        input_sha256=sha(args.checkpoint), mode_identity=saved.mode_identity,
        complete_saved_prefix_definition=saved.definition,
        inlet_normalization=saved.inlet_normalization,
        exact_correction_witness=saved.inlet_exact_correction_witness,
        first_cell_fixed_scalar_lower_bound=scalar_bound,
        conditional_continuous_metric_cost=conditional,
        metric_operator_definition="spectral norm of [[E-1,F/a],[F/a,G/a^2-1]]",
        curvature_definition="largest absolute principal curvature from the same six physical jets and their actual Gram matrix",
        levels=levels, numerical_samples_are_continuous_bounds=False,
        original_accepted_checkpoint_edited=False, nonlinear_BVP_resolved=False,
        full_surface_curvature_bound=False, full_surface_reach_bound=False,
        all_other_closed_C2_seams_certified_here=False, task_completed=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    print(json.dumps(dict(event="inlet_parity_normal_form", output=str(args.out),
        first_cell=saved.inlet_normalization["first_cell"], levels=levels), allow_nan=False), flush=True)


def _annotate_output(data, saved, consumer_file):
    data["inlet_normalization"] = saved.inlet_normalization
    data["postprocessed_finite_field"] = True
    data["original_BVP_reaccepted_after_postprocessing"] = False
    data["inlet_normal_form_wrapper_sha256"] = sha(__file__)
    data["numerical_consumer_sha256"] = sha(consumer_file)
    data["actual_saved_prefix_constructor_sha256"] = saved.inlet_normalization["source_reader_identity"]["source_sha256"]
    if "independent_modes_saved_prefix_sha256" in data:
        data["independent_modes_saved_prefix_sha256"] = data["actual_saved_prefix_constructor_sha256"]
    if "limitations" in data:
        data["limitations"] = [row for row in data["limitations"] if not row.startswith("The inlet reflection's")]
        data["limitations"] = [
            "The original source retains its actual nonlinear DN acceptance; this postprocessed finite prefix is not a re-solved BVP. Its material projection and cut readout retain their own finite-resolution limitations."
            if row.startswith("The full nonlinear DN finite acceptance is retained") else row
            for row in data["limitations"]]
        data["limitations"].append("The inlet is exactly C2 in the recorded R249 shared-node real Hermite normal form. Rounded polynomial coefficients and floating evaluation are numerical approximations; other seams, metric and curvature retain their separate obligations.")


def delegated_readout(arguments):
    consumer = importlib.import_module("geometry_20261114_lifted_modes_readout")
    outputs = []
    def constructor(checkpoint):
        saved = read_saved(checkpoint)
        outputs.append(saved)
        return saved
    locate = argparse.ArgumentParser(add_help=False)
    locate.add_argument("--out", type=Path, required=True)
    options, _ = locate.parse_known_args(arguments)
    previous, argv = consumer.LiftedModesSavedPrefix, sys.argv
    consumer.LiftedModesSavedPrefix = constructor
    sys.argv = [__file__, *arguments]
    try:
        consumer.main()
        data = read(options.out)
        _annotate_output(data, outputs[-1], consumer.__file__)
        data["physical_field_definition"] = outputs[-1].definition["polynomial"]
        options.out.write_text(json.dumps(data, indent=2, allow_nan=False)+"\n")
    finally:
        consumer.LiftedModesSavedPrefix, sys.argv = previous, argv


def delegated_closed(arguments):
    consumer = importlib.import_module("geometry_20261114_lifted_modes_closed_assembly")
    previous_saved, previous_install, argv = consumer.LiftedModesSavedPrefix, consumer.install_consumer, sys.argv
    original_bindings = {name:getattr(consumer.original, name) for name in
        ("LargeCoreSavedPrefix", "load_bundle", "install_consumer", "_bundle", "_last_assembly")}
    def install(args):
        base = previous_install(args)
        original_write = base.write
        def write(path, data):
            # Let the frozen consumer install all its actual-tail metadata
            # and enforce exclusive creation first, then annotate that same
            # freshly created JSON with the precise reader/normal-form identity.
            original_write(path, data)
            if isinstance(data, dict):
                _annotate_output(data, consumer.original._bundle[0], consumer.__file__)
                Path(path).write_text(json.dumps(data, indent=2, allow_nan=False)+"\n")
        base.write = write
        return base
    consumer.LiftedModesSavedPrefix, consumer.install_consumer = read_saved, install
    sys.argv = [__file__, *arguments]
    try:
        consumer.main()
    finally:
        consumer.LiftedModesSavedPrefix, consumer.install_consumer, sys.argv = previous_saved, previous_install, argv
        for name, value in original_bindings.items():
            setattr(consumer.original, name, value)


def main():
    actions_only()
    if len(sys.argv) < 2 or sys.argv[1] not in ("audit", "readout", "closed"):
        raise SystemExit("Use audit --checkpoint ...; readout --input ...; or closed all|plan|render with the existing actual-tail arguments")
    {"audit": audit, "readout": delegated_readout, "closed": delegated_closed}[sys.argv[1]](sys.argv[2:])


if __name__ == "__main__":
    main()
