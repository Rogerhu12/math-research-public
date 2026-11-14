#!/usr/bin/env python3
"""Attempt the full controlled scalar prefix with the original true tail DN.

The accepted M96 prefix supplies the unmodified warm prefix. Beyond it, an
explicit smooth taper to the complete-mode projection of a material-angle
circle is only an initial guess.
All 96 physical modes, all material tail rows, 96 constant core variables,
and three scalar controls enter the actual collocation problem. The original
separated QR and nonlinear Newton gates are used without altering their
source. Affine inner DN solves require a fresh true nonlinear tail recheck.

Even success here is a finite coupled prefix/tail calculation. It does not
certify continuous Fourier errors, a closed C2 assembly, global reach or an
all-time flex. Full mean and second-height seam errors are reported.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import traceback

import numpy as np
from scipy.integrate import solve_bvp
import scipy.integrate._bvp as backend
from scipy.interpolate import CubicHermiteSpline

import geometry_20261114_projected_core_bvp as original_solver
import geometry_20261114_separated_qr_bvp as original_qr
from geometry_20261114_full_dn_augmented import AugmentedFlow, SeparatedBoundary
from geometry_20261114_full_dn_boundary import FullDNBoundary, MaterialTrace, directional_check
from geometry_20261114_full_scalar_profile import CompleteProfile, read
from geometry_20261114_material_quintic_readout import material_angles
from geometry_20261114_public_free3 import FROZEN_SOURCES

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, data):
    path = Path(path)
    raw = (json.dumps(data, indent=None if path.suffix == ".gz" else 2, allow_nan=False) + "\n").encode()
    partial = path.with_name(path.name + ".tmp")
    partial.write_bytes(gzip.compress(raw, mtime=0) if path.suffix == ".gz" else raw)
    partial.replace(path)


def finite_max(value):
    value = np.asarray(value)
    return float(np.max(np.abs(value))) if value.size and np.all(np.isfinite(value)) else None


class AffineTail:
    def __init__(self, modes):
        self.T = modes
        self.anchor = None

    def set(self, height, response):
        slope = np.asarray(response["jets"]["slope"], dtype=float)
        J = np.asarray(response["heightJetJacobian"], dtype=float).reshape(3 * self.T + 2, self.T)[:self.T]
        if np.asarray(height).shape != (self.T,) or slope.shape != (self.T,) or not np.all(np.isfinite(J)):
            raise ValueError("A complete actual native tail response is required")
        self.anchor = (np.array(height, copy=True), slope.copy(), J.copy())

    def __call__(self, height):
        if self.anchor is None:
            raise RuntimeError("No actual nonlinear tail anchor has been solved")
        H, slope, J = self.anchor
        return dict(slope=slope + J @ (np.asarray(height) - H), jacobian=J,
                    actual_nonlinear_solve=False,
                    scope="Complete affine inner DN map at the most recent actual tail solve")


def load_client(module_path, config, sources, prefix, heap):
    spec = importlib.util.spec_from_file_location("full_dn_true_tail_client", module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    factory = getattr(module, "TailClient", getattr(module, "WeightedTailPort", None))
    if factory is None:
        raise TypeError("The actual tail module must export TailClient or WeightedTailPort")
    return factory(config, sources, prefix, node_heap=heap)


def scalar_spec(profile, port, parameters, accepted_sha256):
    return dict(schema="complete-controlled-scalar-profile-v1",
                accepted_prefix_sha256=accepted_sha256,
                base_prefix_geometry=profile.fixed_geometry,
                base_prefix_end=profile.prefix_end, base_prefix_M=profile.M,
                peak_curvature=profile.turn.K, tail_modes=profile.tail_modes,
                complete_original_port=port,
                frozen_design_parameters=np.asarray(parameters).tolist(),
                control_definition="64*width^2*x^3*(1-x)^3 with exact zero extension",
                canonical_material_metric="ds^2+a(s;frozen_design_parameters)^2*dtheta^2")


def prepared_guess(accepted, profile, flow, extension_step, taper_fraction):
    x = np.asarray(accepted["mesh"])
    y, dy = np.asarray(accepted["states"]), np.asarray(accepted["rhs"])
    interpolation = CubicHermiteSpline(x, y, dy, axis=0)
    end = profile.end
    extension = np.linspace(x[-1], end, int(np.ceil((end - x[-1]) / extension_step)) + 1)
    mesh = original_solver.merge_mesh(np.r_[x, profile.knots], extension)
    taper_end = profile.prefix_end + taper_fraction * profile.turn.length
    start_radius = profile.base_jet(profile.prefix_end)[0]
    anchor = y[-1].copy()
    iz = 2 * flow.M + 1
    mean = anchor[iz]
    anchor[iz] = 0
    core = np.asarray(accepted["core"]["coefficients"])
    frequency = 2 * np.arange(1, flow.M + 1)
    phi = 2 * np.pi * np.arange(flow.q.N) / flow.q.N
    phase_difference = (((1 - frequency ** 2) * core) / frequency) @ np.sin(frequency[:, None] * phi)
    material_circle = flow.q.project(np.column_stack((np.cos(phase_difference), np.sin(phase_difference), np.zeros(flow.q.N))))
    material_circle[iz:] = 0
    rho = 1 + ((1 - frequency ** 2) * core) @ np.cos(frequency[:, None] * phi)
    circle_derivative = flow.q.jet(material_circle)[1]
    circle_metric_error = finite_max(np.einsum("ij,ij->i", circle_derivative, circle_derivative) / rho ** 2 - 1)
    gx, gw = np.polynomial.legendre.leggauss(24)
    def background_height(s):
        # This mean is only a seed. It does not overwrite the accepted
        # nonaxisymmetric mean or assert that the extension solves the ODE.
        knots = sorted(set([profile.prefix_end, float(s),
                            *[v for v in profile.knots if profile.prefix_end < v < s]]))
        total = 0.
        for left, right in zip(knots[:-1], knots[1:]):
            points = (left + right) / 2 + (right - left) / 2 * gx
            speeds = np.array([profile.base_jet(v)[1] for v in points])
            if np.any(np.abs(speeds) >= 1):
                raise FloatingPointError("The seed's actual scalar profile leaves |a'|<1")
            total += (right - left) / 2 * (gw @ np.sqrt(1 - speeds ** 2))
        return mean + total
    def at(points):
        points = np.asarray(points)
        values = np.zeros((len(points), flow.dimension))
        for j, s in enumerate(points):
            if s <= profile.prefix_end:
                values[j, :flow.n] = interpolation(s)
            else:
                a = profile.base_jet(s)[0]
                u = min(1., (s - profile.prefix_end) / (taper_end - profile.prefix_end))
                weight = 1 - 10 * u ** 3 + 15 * u ** 4 - 6 * u ** 5
                values[j, :flow.n] = weight * (a / start_radius) * anchor
                values[j, :flow.n] += (1 - weight) * a * material_circle
                values[j, iz] = background_height(s)
            values[j, flow.core_slice] = core
        return values
    return mesh, at, dict(kind="accepted-prefix-then-explicit-taper-initial-guess",
                         taper_fraction=taper_fraction, taper_end=taper_end,
                         terminal_local_reference="theta circle: a*(cos(Theta_c(phi)-phi),sin(Theta_c(phi)-phi),0) in the rotating frame",
                         reference_projection_modes=flow.M, reference_projection_angles=flow.q.N,
                         projected_reference_angular_metric_max=circle_metric_error,
                         extension_is_a_solution=False, no_spectral_mode_removed=True)


def preflight(mesh, initial_at, flow, max_nodes):
    added = []
    for iteration in range(12):
        values = initial_at(mesh)
        derivative = flow(mesh, values.T)
        bad_nodes = ~np.all(np.isfinite(derivative), axis=0)
        if np.any(bad_nodes):
            raise FloatingPointError("The actual full-profile seed leaves the finite Frenet domain at nodes "
                                     + repr(mesh[bad_nodes].tolist()))
        h = np.diff(mesh)
        midpoint = (mesh[:-1] + mesh[1:]) / 2
        ym = (values[:-1] + values[1:]) / 2 - h[:, None] / 8 * (derivative[:, 1:] - derivative[:, :-1]).T
        fm = flow(midpoint, ym.T)
        bad = ~np.all(np.isfinite(fm), axis=0)
        if not np.any(bad):
            residual = values[1:] - values[:-1] - h[:, None] / 6 * (derivative[:, :-1] + derivative[:, 1:] + 4 * fm).T
            return mesh, values, derivative.T, residual, added
        new = midpoint[bad]
        if len(mesh) + len(new) > max_nodes:
            raise FloatingPointError("The complete initial domain needs more than the declared node budget")
        added.extend(new.tolist())
        mesh = original_solver.merge_mesh(mesh, new)
    raise FloatingPointError("The complete initial midpoint domain did not resolve")


def true_height(boundary, augmented_endpoint):
    flow_n, M = boundary.n, boundary.M
    core = augmented_endpoint[flow_n:flow_n + M]
    physical = augmented_endpoint[:flow_n]
    p = augmented_endpoint[flow_n + M:]
    derivative = boundary.rhs(boundary.profile.end, physical, p)
    trace = boundary.trace(core, physical[boundary.iz:], derivative[boundary.iz:])
    return boundary.eh * trace.height


def frozen_physical_residual(sol, flow):
    """Original Lobatto relative residual for the one frozen scalar metric.

SciPy sums squared residuals across state components; adding constant rows
does not dilute its tolerance. This extra check evaluates the physical
components using one constant endpoint p, also retaining any small nodal
residual caused by an incompletely constant augmented iterate.
    """
    parameters = sol.y[flow.parameter_slice, -1]
    def fun(x, y, unused):
        return flow.physical(x, y, np.repeat(parameters[:, None], len(x), axis=1))
    def curve(x, order=0):
        return sol.sol(x, order)[:flow.n]
    h = np.diff(sol.x)
    col, ym, f, fm = backend.collocation_fun(fun, sol.y[:flow.n], np.empty(0), sol.x, h)
    rms = backend.estimate_rms_residuals(fun, curve, sol.x, h, np.empty(0), 1.5 * col / h, fm)
    node = (curve(sol.x, 1) - f) / (1 + np.abs(f))
    node_square = np.sum(node * node, axis=0)
    rms = np.sqrt(rms * rms + .05 * (node_square[:-1] + node_square[1:]))
    return rms, f.T, finite_max(node)


def final_height_seam(boundary, flow, q, endpoint, response):
    y, core, parameters = endpoint[:flow.n], endpoint[flow.core_slice], endpoint[flow.parameter_slice]
    q.profile = lambda s: flow.profile.profile(s, parameters)
    yp, ypp = original_solver.finite_second_derivative(q, flow.profile.end, y)
    trace = boundary.trace(core, y[boundary.iz:], yp[boundary.iz:])
    phi, rho, _, info = material_angles(core, boundary.trace.N)
    cosine = np.cos(2 * np.arange(flow.M + 1)[:, None] * phi)
    mean = np.mean(cosine, axis=1)
    E, Ep = float(flow.profile.cut["E"]), float(flow.profile.cut["Ep"])
    native_first = np.asarray(response["jets"]["slope"])
    native_second = np.asarray(response["jets"]["second"])
    target_first = boundary.cut_scale * native_first
    target_second = boundary.eh * (native_second / E - Ep * native_first / (2 * E ** 2))
    first = trace.derivative_s
    second = trace.projection @ ypp[boundary.iz:]
    target_mean_first = boundary.cut_scale * float(response["jets"]["meanSlope"])
    target_mean_second = boundary.eh * (float(response["jets"]["meanSecond"]) / E
                         - Ep * float(response["jets"]["meanSlope"]) / (2 * E ** 2))
    return dict(scope="Actual finite ODE 0/1/2 height jets in the common material angle; Cartesian assembly remains separate.",
                nonmean_first_max=finite_max(first - target_first),
                nonmean_second_max=finite_max(second - target_second),
                mean_first_error=float(mean @ yp[boundary.iz:] - target_mean_first),
                mean_second_error=float(mean @ ypp[boundary.iz:] - target_mean_second),
                mean_prefix_first=float(mean @ yp[boundary.iz:]),
                mean_prefix_second=float(mean @ ypp[boundary.iz:]),
                mean_tail_first=target_mean_first, mean_tail_second=target_mean_second,
                angular_grid=boundary.trace.N, angle_inverse=info,
                remaining_angular_tail_error_certified=False, full_Cartesian_seam_certified=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--accepted", type=Path, required=True)
    parser.add_argument("--port", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--tail-client", type=Path)
    parser.add_argument("--tail-config", type=Path)
    parser.add_argument("--tail-source-root", type=Path)
    parser.add_argument("--warm", type=Path)
    parser.add_argument("--peak-curvature", type=float, default=2.5)
    parser.add_argument("--extension-step", type=float, default=.005)
    parser.add_argument("--taper-fraction", type=float, default=.4)
    parser.add_argument("--jac-workers", type=int, default=2)
    parser.add_argument("--max-nodes", type=int, default=1200)
    parser.add_argument("--material-angles", type=int, default=4096)
    parser.add_argument("--node-heap", type=int, default=1536)
    parser.add_argument("--tol", type=float, default=1e-6)
    parser.add_argument("--outer-iterations", type=int, default=8)
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Run the numerical problem only in this public repository's GitHub Actions")
    if args.tol != 1e-6 or not 0 < args.taper_fraction <= 1 or args.extension_step <= 0:
        raise ValueError("Retain the prescribed tolerance and a positive explicit seed taper")
    if not args.prepare_only and any(v is None for v in (args.tail_client, args.tail_config, args.tail_source_root)):
        raise ValueError("A true complete tail client, config and source tree are required")
    for filename, expected in FROZEN_SOURCES.items():
        if sha(HERE / filename) != expected:
            raise ValueError("The original mathematical source changed: " + filename)
    accepted, port = read(args.accepted), read(args.port)
    if (accepted.get("success") is not True or accepted.get("status") != 0
            or (accepted["M"], accepted["N"]) != (96, 1024)
            or not 0 <= accepted["collocation_rms_max"] <= 1e-6
            or not 0 <= accepted["boundary_residual_max"] <= 1e-11):
        raise ValueError("Start with the complete accepted M96/N1024 prefix")
    out, work = args.out.resolve(), args.work.resolve()
    out.mkdir(parents=True, exist_ok=True); work.mkdir(parents=True, exist_ok=True)
    if work == out or out in work.parents:
        raise ValueError("Large reproducible QR factors belong outside the uploaded output")
    profile = CompleteProfile(accepted, port, args.peak_curvature, accepted["M"])
    description = profile.description()
    law = accepted["original_metric_identity"]["law"]
    coefficients = np.asarray(accepted["core"]["coefficients"])
    q = original_solver.native.outward.FullCoreProbe(coefficients, accepted["M"], accepted["N"],
          law["velocity"], law["length"], law["k0"])
    q.profile = profile.profile
    original_solver.fixed.fft.enable_fft(q)
    flow = AugmentedFlow(q, profile, args.jac_workers)
    affine = AffineTail(profile.tail_modes)
    boundary = FullDNBoundary(profile, coefficients[:3], flow.point_rhs, flow.point_jacobian,
                              affine, angular=args.material_angles)
    separated = SeparatedBoundary(boundary)
    mesh, initial_at, guess_info = prepared_guess(accepted, profile, flow, args.extension_step, args.taper_fraction)
    if args.warm:
        warm = read(args.warm)
        warm_states = np.asarray(warm.get("augmented_states", warm["states"]))
        warm_rhs = np.asarray(warm.get("augmented_rhs", warm["rhs"]))
        warm_x = np.asarray(warm["mesh"])
        if warm_states.shape != (len(warm_x), flow.dimension) or warm_rhs.shape != warm_states.shape:
            raise ValueError("The warm state must retain all 389 augmented rows")
        if warm_x[0] != 0 or abs(warm_x[-1] - profile.end) > 1e-12:
            raise ValueError("The warm checkpoint belongs to another complete physical interval")
        warm_curve = CubicHermiteSpline(warm_x, warm_states, warm_rhs, axis=0)
        initial_at = warm_curve
        mesh = original_solver.merge_mesh(mesh, warm_x)
        guess_info = dict(kind="complete-unconverged-or-accepted-augmented-warm", sha256=sha(args.warm))
    state = dict(scope=__doc__, phase="preparing", source_sha256=sha(__file__),
                 accepted_input_sha256=sha(args.accepted), port_sha256=sha(args.port),
                 source_repository=os.environ.get("GITHUB_REPOSITORY"), source_commit=os.environ.get("GITHUB_SHA"),
                 scalar_profile=description, initial_guess=guess_info,
                 state_dimension=flow.dimension, physical_state_dimension=flow.n,
                 left_rows=separated.left_count, right_rows=profile.tail_modes,
                 frozen_original_sources=FROZEN_SOURCES, outer_history=[],
                 full_Cartesian_closed_surface=False, new_coupled_finite_acceptance=False)
    write(out / "driver-status.json", state)
    client = None
    begin = time.monotonic()
    try:
        mesh, initial, rhs, residual, additions = preflight(mesh, initial_at, flow, args.max_nodes)
        prepared = dict(scope="Full initial guess and finite-domain preflight; no BVP or true tail acceptance.",
                        M=flow.M, N=q.N, mesh=mesh.tolist(), states=initial.tolist(), rhs=rhs.tolist(),
                        augmented_states=initial.tolist(), augmented_rhs=rhs.tolist(),
                        initial_collocation_max=finite_max(residual), preflight_added_nodes=additions,
                        complete_scalar_profile=scalar_spec(profile, port, initial[-1, flow.parameter_slice], sha(args.accepted)),
                        success=False, complete_closed_surface=False)
        write(out / "prepared.json.gz", prepared)
        state.update(phase="prepared-full-interval", nodes=len(mesh),
                     initial_collocation_max=prepared["initial_collocation_max"], preflight_added_nodes=additions)
        write(out / "driver-status.json", state)
        print(json.dumps(dict(event="full-profile-prepared", end=profile.end, nodes=len(mesh),
                              initial_collocation_max=prepared["initial_collocation_max"])), flush=True)
        if args.prepare_only:
            return 0
        client = load_client(args.tail_client, args.tail_config, args.tail_source_root, out / "true-tail", args.node_heap)
        config = read(args.tail_config)
        if (int(config["modes"]), int(config["spacing"])) != (profile.tail_modes, 2):
            raise ValueError("The tail does not retain every requested even material mode")
        for key, expected in port["parameters"].items():
            if config.get(key) != expected:
                raise ValueError("The original physical tail metric parameter differs: " + key)
        for key in ("radius", "E", "Ep", "backgroundSlope", "backgroundSecond"):
            if not np.isclose(float(client.cut[key]), float(profile.cut[key]), rtol=2e-11, atol=2e-13):
                raise ValueError("The true tail uses another physical cut: " + key)
        frequency = 2 * np.arange(1, flow.M + 1)
        rho_cosine = np.cos(frequency[:, None] * (2 * np.pi * np.arange(args.material_angles) / args.material_angles))
        def bc(ya, yb):
            core = yb[flow.core_slice]
            if not np.all(np.isfinite(core)) or np.min(1 + ((1 - frequency ** 2) * core) @ rho_cosine) <= 0:
                return np.full(flow.dimension, np.nan)
            try:
                return separated(ya, yb)
            except FloatingPointError:
                return np.full(flow.dimension, np.nan)
            except RuntimeError as error:
                if str(error) != "Material angle inversion did not converge":
                    raise
                return np.full(flow.dimension, np.nan)
        backend.solve_newton = original_solver.released_newton
        original_solver.original_splu = original_qr.factor
        accepted_result = None
        for iteration in range(args.outer_iterations):
            height = true_height(boundary, initial[-1])
            response = client.solve(height, jacobian=True, audit=False)
            write(out / (f"outer-{iteration:02d}-anchor-tail.json.gz"), response)
            affine.set(height, response)
            state.update(phase="affine-inner-newton", current_outer_iteration=iteration)
            write(out / "driver-status.json", state)
            checkpoint = out / f"outer-{iteration:02d}-newton-checkpoint.json.gz"
            original_qr.enable(work, separated.left_count, chunk_size=16,
                               checkpoint=checkpoint, M=flow.M, N=q.N)
            sol = solve_bvp(flow, bc, mesh, initial.T, fun_jac=flow.jac, bc_jac=separated.jacobian,
                            tol=args.tol, bc_tol=1e-11, max_nodes=args.max_nodes, verbose=2)
            full_rhs = flow(sol.x, sol.y).T
            inner_bc = finite_max(bc(sol.y[:, 0], sol.y[:, -1]))
            rms = finite_max(sol.rms_residuals)
            pending = dict(scope="Actual augmented affine-inner iterate; true nonlinear tail acceptance pending.",
                           M=flow.M, N=q.N, mesh=sol.x.tolist(), states=sol.y.T.tolist(), rhs=full_rhs.tolist(),
                           augmented_states=sol.y.T.tolist(), augmented_rhs=full_rhs.tolist(),
                           complete_scalar_profile=scalar_spec(profile, port, sol.y[flow.parameter_slice, -1], sha(args.accepted)),
                           success=False, inner_success=bool(sol.success), status=int(sol.status),
                           message=sol.message, collocation_rms_max=rms, boundary_residual_max=inner_bc)
            write(out / f"outer-{iteration:02d}-pending.json.gz", pending)
            row = dict(iteration=iteration, inner_success=bool(sol.success), inner_status=int(sol.status),
                       message=sol.message, nodes=len(sol.x), collocation_rms_max=rms, affine_boundary_max=inner_bc)
            state["outer_history"].append(row)
            if not sol.success or rms is None or rms > args.tol or inner_bc is None or inner_bc > 1e-11:
                state.update(phase="inner-newton-not-accepted")
                write(out / "driver-status.json", state)
                return 2
            final_height = true_height(boundary, sol.y[:, -1])
            actual = client.solve(final_height, jacobian=True, audit=False)
            write(out / f"outer-{iteration:02d}-actual-tail.json.gz", actual)
            affine.set(final_height, actual)
            true_bc = finite_max(bc(sol.y[:, 0], sol.y[:, -1]))
            row.update(actual_nonlinear_boundary_max=true_bc, height_change_max=finite_max(final_height - height))
            write(out / "driver-status.json", state)
            if true_bc is not None and true_bc <= 1e-11:
                accepted_result = (sol, full_rhs, actual, true_bc, rms)
                break
            mesh, initial = sol.x, sol.y.T
        if accepted_result is None:
            state.update(phase="actual-tail-outer-iterations-exhausted")
            write(out / "driver-status.json", state)
            return 3
        sol, full_rhs, actual, true_bc, rms = accepted_result
        physical_rms, physical_rhs, physical_node_residual = frozen_physical_residual(sol, flow)
        physical_rms_max = finite_max(physical_rms)
        if physical_rms_max is None or physical_rms_max > args.tol:
            state.update(phase="frozen-physical-RMS-not-accepted", physical_RMS_max=physical_rms_max,
                         physical_node_relative_residual=physical_node_residual)
            write(out / "driver-status.json", state)
            return 4
        state["phase"] = "auditing-actual-tail-and-height-jets"
        write(out / "driver-status.json", state)
        actual = client.solve(true_height(boundary, sol.y[:, -1]), jacobian=True, audit=True)
        write(out / "actual-tail-final-audit.json.gz", actual)
        affine.set(true_height(boundary, sol.y[:, -1]), actual)
        audited_bc = finite_max(bc(sol.y[:, 0], sol.y[:, -1]))
        if audited_bc is None or audited_bc > 1e-11:
            state["phase"] = "audited-true-tail-boundary-not-accepted"
            write(out / "driver-status.json", state)
            return 4
        seam = final_height_seam(boundary, flow, q, sol.y[:, -1], actual)
        core = sol.y[1:flow.M + 1, 0]
        q.coefficients = core
        q.rho0 = 1 + ((1 - frequency ** 2) * core) @ q.C[1:]
        q.hmajor = 1 + float(core.sum()); q.hminor = 1 + float(np.sum(core * (-1.) ** np.arange(1, flow.M + 1)))
        q.gap = q.hmajor - q.hminor; q.witness = np.array([0., q.hmajor, 0.])
        rows = []
        for s, yy in zip(sol.x, sol.y.T):
            try:
                rows.append(q.stats(float(s), yy[:flow.n]))
            except Exception as error:
                rows.append(dict(s=float(s), error=repr(error)))
        valid_rows = [r for r in rows if "metric_sample" in r]
        spec = scalar_spec(profile, port, sol.y[flow.parameter_slice, -1], sha(args.accepted))
        result = dict(scope=__doc__, success=True, status=0, message="Full finite coupled nonmean DN accepted with actual tail audit; closure remains open.",
                      M=flow.M, N=q.N, fixed_modes=3, end=profile.end, seconds=time.monotonic() - begin,
                      mesh=sol.x.tolist(), states=sol.y[:flow.n].T.tolist(), rhs=physical_rhs.tolist(),
                      augmented_states=sol.y.T.tolist(), augmented_rhs=full_rhs.tolist(),
                      complete_scalar_profile=spec, fixed_scalar_profile=dict(geometry=spec),
                      original_metric_identity=accepted["original_metric_identity"],
                      parameters={k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()},
                      solved_metric_definition=dict(core_coefficients_binary64_exact_rational=[str(Fraction(float(v))) for v in core],
                                                    scalar_profile=spec,
                                                    material_coordinate="Common theta; g=ds^2+a(s)^2*dtheta^2."),
                      core=dict(coefficients=core.tolist(), axis_support_gap=q.gap,
                                rho_sample_min=float(q.rho0.min()), rho_sample_max=float(q.rho0.max())),
                      scalar_parameters=sol.y[flow.parameter_slice, -1].tolist(),
                      collocation_rms_max=rms, boundary_residual_max=audited_bc,
                      physical_frozen_control_RMS_max=physical_rms_max,
                      physical_node_relative_residual=physical_node_residual,
                      constant_core_state_drift=finite_max(sol.y[flow.core_slice] - core[:, None]),
                      constant_parameter_state_drift=finite_max(sol.y[flow.parameter_slice] - sol.y[flow.parameter_slice, -1:]),
                      actual_tail=dict(final_response_sha256=sha(out / "actual-tail-final-audit.json.gz"),
                                       cut=client.cut, sources=getattr(client, "sources", None)),
                      height_seam=seam, rows=rows,
                      summary=dict(metric_sample=max((r["metric_sample"] for r in valid_rows), default=None),
                                   kappa_sample=max((r["surface_kappa_sample"] for r in valid_rows), default=None),
                                   minimum_point_domain=min((r["margin"] for r in valid_rows), default=None),
                                   reflected_prefix_D_sample=2 * max((r["ball_radius_max"] for r in valid_rows), default=0)),
                      outer_history=state["outer_history"], source_sha256=sha(__file__),
                      full_Cartesian_closed_surface=False, same_metric_refinement=False)
        write(out / "actual.json.gz", result)
        state.update(phase="finite-full-DN-accepted-assembly-open", new_coupled_finite_acceptance=True,
                     actual_result_sha256=sha(out / "actual.json.gz"), height_seam=seam)
        write(out / "driver-status.json", state)
        return 0
    except Exception as error:
        state.update(phase="exception", exception=repr(error), traceback=traceback.format_exc())
        write(out / "driver-status.json", state)
        raise
    finally:
        if client is not None:
            client.close()
        state["elapsed_seconds"] = time.monotonic() - begin
        write(out / "driver-status.json", state)


if __name__ == "__main__":
    raise SystemExit(main())
