#!/usr/bin/env python3
"""Run the original full-DN/Newton problem from a real higher-mode preflight.

The accepted input remains the original M96/N1024 field.  This adapter
changes the new problem's field, angular and tail dimensions to those of
the separately prepared M112/T112/N2048 initial guess.  All physical/core
rows and the same three scalar controls are retained.  It calls the full
original outer true-tail loop, inner Newton/line-search/QR, tolerances,
frozen-physical RMS, complete final tail audit and height-seam readout.

No existing mathematical source is edited.  This adapter records its
setup bindings and the actual small QR system/SVD/linear residual.  The
unchanged original routine alone decides its finite acceptance; a closed
surface or a continuous-frequency certificate is not inferred from it.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import json
from pathlib import Path
import sys

import numpy as np
from scipy.interpolate import CubicHermiteSpline
from scipy.linalg import solve_triangular

import geometry_20261114_full_dn_solve as original
from geometry_20261114_full_dn_prefix_controls import rms_domain
from geometry_20261114_lifted_modes_prepare import validate_source, domain_minimum
from geometry_20261114_lifted_modes_profile import (
    LiftedModesPrefixProfile, SCHEMA, FIELD_SCHEMA, scalar_spec,
    reconstruct_profile, field_spec, sha)

HERE = Path(__file__).resolve().parent


def argument(name, *, remove=False):
    if name not in sys.argv:
        raise ValueError("This explicit full-DN adapter requires " + name)
    index = sys.argv.index(name)
    value = Path(sys.argv[index + 1])
    if remove:
        del sys.argv[index:index + 2]
    return value


def finite(value):
    value = np.asarray(value)
    return float(np.max(abs(value))) if value.size and np.all(np.isfinite(value)) else None


def install_qr_diagnostics(output, M, write):
    """Expose the original factor's complete reduced system, without edits."""
    base_factor = original.original_qr.DiskQRFactor
    physical, core_end, iz = 3 * M + 2, 4 * M + 2, 2 * M + 1
    factor_count = 0
    class DiagnosticFactor(base_factor):
        def finish(self):
            try:
                self._record_finish()
            except Exception as error:
                self._diagnostic_error("factor-SVD", error)
            # Mathematical factorization errors remain the original errors.
            # Diagnostic I/O or optional backtransport cannot veto a factor.
            return super().finish()

        def _diagnostic_error(self, stage, error):
            message = dict(stage=stage, exception=repr(error),
                           original_mathematical_operation_not_replaced=True)
            if not isinstance(getattr(self, "diagnostic", None), dict):
                self.diagnostic = {}
            self.diagnostic.setdefault("diagnostic_errors", []).append(message)
            try:
                write(output / f"reduced-{self.diagnostic_index:03d}.json", self.diagnostic)
            except Exception as log_error:
                print(json.dumps(dict(event="optional_QR_diagnostic_error", **message,
                                      diagnostic_write_exception=repr(log_error))), flush=True)

        def _record_finish(self):
            nonlocal factor_count
            factor_count += 1
            self.diagnostic_index = factor_count
            small = self.right @ self.U[-1]
            U, singular, Vh = np.linalg.svd(small, full_matrices=False)
            packet = output / f"reduced-{factor_count:03d}.npz"
            np.savez_compressed(packet, small=small, singular_values=singular, U=U, Vh=Vh,
                nullspace_left=self.U[0], nullspace_right=self.U[-1], boundary_right=self.right)
            modes = []
            for j in range(1, min(7, self.k + 1)):
                coordinate = Vh[-j].copy()
                endpoint = self.U[-1] @ coordinate
                initial, maximum, pdrift, cdrift = None, finite(endpoint), 0., 0.
                try:
                    for i in range(self.m - 2, -1, -1):
                        coordinate = solve_triangular(self.transport[i], coordinate, check_finite=False)
                        value = self.U[i] @ coordinate
                        if not np.all(np.isfinite(value)):
                            raise FloatingPointError("Nonfinite homogeneous backward transport")
                        maximum = max(maximum, finite(value))
                        pdrift = max(pdrift, float(np.max(abs(value[core_end:] - endpoint[core_end:]))))
                        cdrift = max(cdrift, float(np.max(abs(value[physical:core_end] - endpoint[physical:core_end]))))
                        if i == 0:
                            initial = value
                    transport_error = None
                except (ValueError, FloatingPointError, np.linalg.LinAlgError) as error:
                    transport_error = repr(error)
                modes.append(dict(singular_value=float(singular[-j]),
                    endpoint_physical_norm=float(np.linalg.norm(endpoint[:physical])),
                    endpoint_core_norm=float(np.linalg.norm(endpoint[physical:core_end])),
                    endpoint_scalar_parameters=endpoint[core_end:].tolist(), endpoint_z0=float(endpoint[iz]),
                    inlet_scalar_parameters=None if initial is None else initial[core_end:].tolist(),
                    homogeneous_state_max=maximum, constant_parameter_transport_drift=pdrift,
                    constant_core_transport_drift=cdrift, transport_error=transport_error))
            self.diagnostic = dict(factor=factor_count, field_modes=M, n=self.n, nodes=self.m,
                free_dimensions=self.k, reduced_condition=float(singular[0] / singular[-1]) if singular[-1] else None,
                singular_values=singular.tolist(),
                numerical_ranks={str(tol): int(np.sum(singular > tol * singular[0]))
                                 for tol in (1e-8, 1e-10, 1e-12, 1e-14, 1e-16)},
                smallest_six_directions=modes, packet=dict(file=str(packet), sha256=sha(packet)),
                original_factor_and_solve_unchanged=True, mathematical_rank_certified=False)
            write(output / f"reduced-{factor_count:03d}.json", self.diagnostic)
            return None

        def solve(self, rhs):
            answer = super().solve(rhs)
            if self.solve_count == 1:
                try:
                    self._record_first_solve(answer, rhs)
                except Exception as error:
                    self._diagnostic_error("linear-residual-location", error)
            return answer

        def _record_first_solve(self, answer, rhs):
            if self.solve_count == 1:
                values = answer.reshape(self.m, self.n)
                rhs = np.asarray(rhs)
                col = rhs[:(self.m - 1) * self.n].reshape(self.m - 1, self.n)
                worst = dict(absolute=0.)
                maxima = dict(physical=0., constant_core=0., constant_parameters=0.,
                              left_boundary=0., right_boundary=0.)
                for i in range(self.m - 1):
                    with np.load(self.directory / f"{i:05d}.npz") as block:
                        error = block["L"] @ values[i] + block["R"] @ values[i + 1] - col[i]
                    row = int(np.argmax(abs(error)))
                    if abs(error[row]) > worst["absolute"]:
                        worst = dict(absolute=float(abs(error[row])), interval=i, state_row=row)
                    for name, block in (("physical", slice(None, physical)),
                                        ("constant_core", slice(physical, core_end)),
                                        ("constant_parameters", slice(core_end, None))):
                        maxima[name] = max(maxima[name], float(np.max(abs(error[block]))))
                offset = (self.m - 1) * self.n
                left = self.left @ values[0] - rhs[offset:offset + self.nl]
                right = self.right @ values[-1] - rhs[offset + self.nl:]
                maxima["left_boundary"], maxima["right_boundary"] = finite(left), finite(right)
                self.diagnostic["first_original_linear_solve"] = dict(
                    residual_max_by_block=maxima, worst_collocation_row=worst, rhs_max=finite(rhs),
                    solution_max=finite(answer), scalar_parameter_step_at_inlet=values[0, core_end:].tolist(),
                    scalar_parameter_step_at_cut=values[-1, core_end:].tolist())
                write(output / f"reduced-{self.diagnostic_index:03d}.json", self.diagnostic)
            return answer
    original.original_qr.DiskQRFactor = DiagnosticFactor


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run numerical work in the public repository's Actions")
    # The only added CLI option binds the already completed implementation
    # response check.  All remaining arguments go to the original driver.
    response_path = argument("--response-check", remove=True)
    accepted_path, warm_path, output = argument("--accepted"), argument("--warm"), argument("--out")
    port_path = argument("--port")
    accepted, warm, response = original.read(accepted_path), original.read(warm_path), original.read(response_path)
    validate_source(accepted)
    M, N = int(warm["M"]), int(warm["N"])
    spec = warm["complete_scalar_profile"]
    if (warm.get("field_representation", {}).get("schema") != FIELD_SCHEMA
            or spec.get("schema") != SCHEMA or int(spec["field_modes"]) != M
            or int(spec["tail_modes"]) != M or int(spec["base_prefix_M"]) != int(accepted["M"])
            or spec["accepted_prefix_sha256"] != sha(accepted_path)
            or spec["base_prefix_geometry"] != accepted["fixed_scalar_profile"]["geometry"]
            or spec["complete_original_port"] != original.read(port_path)
            or warm["field_representation"] != field_spec(M, N)):
        raise ValueError("The complete prepared field/scalar/source identity does not match")
    frozen = reconstruct_profile(spec)
    if frozen.M != M or frozen.tail_modes != M:
        raise ValueError("The reconstructed scalar design lost its new field dimension")
    if (response.get("implementation_check_passed") is not True
            or response.get("verification_threshold") != 5e-5
            or response.get("prepared_sha256") != sha(warm_path)
            or response.get("accepted_sha256") != sha(accepted_path)
            or response.get("lifted_modes_implementation", {}).get("field_modes") != M
            or response.get("lifted_modes_implementation", {}).get("tail_modes") != M
            or response.get("lifted_modes_implementation", {}).get("angular_quadrature") != N):
        raise ValueError("Complete the original unrelaxed full boundary FD on this actual prepared field first")
    mesh = np.asarray(warm["mesh"])
    values = np.asarray(warm.get("augmented_states", warm["states"]))
    rhs = np.asarray(warm.get("augmented_rhs", warm["rhs"]))
    if values.shape != (len(mesh), 4 * M + 5) or rhs.shape != values.shape:
        raise ValueError("The complete warm lost a physical, core or scalar row")
    output.mkdir(parents=True, exist_ok=True)
    original_write = original.write
    source_names = ("geometry_20261114_full_dn_solve.py", "geometry_20261114_full_dn_augmented.py",
        "geometry_20261114_full_dn_boundary.py", "geometry_20261114_full_dn_prefix_controls.py",
        "geometry_20261114_lifted_modes_profile.py", "geometry_20261114_lifted_modes_prepare.py",
        "geometry_20261114_lifted_modes_response.py", "geometry_20261114_separated_qr_bvp.py")
    binding = dict(scope=__doc__, source_sha256=sha(__file__),
        original_and_adapter_sources_sha256={name: sha(HERE / name) for name in source_names},
        source_accepted_prefix=dict(M=int(accepted["M"]), N=int(accepted["N"]), sha256=sha(accepted_path)),
        field_modes=M, angular_quadrature=N, tail_modes=M, scalar_controls=3,
        warm_sha256=sha(warm_path), complete_BC_response_sha256=sha(response_path),
        unchanged_acceptance=dict(RMS=1e-6, BC=1e-11, original_Newton_and_line_search=True,
                                  true_new_dimension_tail_and_final_audit_required=True),
        source_prefix_relabelled=False)
    original_write(output / "lifted-modes-intent.json", binding)
    statistics_parameters = None
    def write(path, data):
        if isinstance(data, dict):
            name = Path(path).name
            if name in ("driver-status.json", "prepared.json.gz", "actual.json.gz") or name.endswith("-pending.json.gz"):
                data["field_representation"] = field_spec(M, N)
                data["source_accepted_prefix"] = binding["source_accepted_prefix"]
                data["lifted_modes_implementation"] = binding
            if name == "actual.json.gz":
                if statistics_parameters is None or not np.array_equal(
                        statistics_parameters, np.asarray(data["scalar_parameters"])):
                    # Do not publish statistics tied to an unspecified metric.
                    data["discarded_legacy_statistics"] = dict(
                        reason="The explicit frozen scalar statistics binding was not observed",
                        rows=data.pop("rows", []), summary=data.pop("summary", {}))
                else:
                    data["sampled_geometry_scalar_parameters"] = statistics_parameters.tolist()
                    data["sampled_geometry_scope"] = (
                        "Original finite-ODE point samples with an explicit copied frozen p*, "
                        "not zero-control statistics or continuous geometry certificates.")
        original_write(path, data)
    original.write = write
    original.scalar_spec = scalar_spec
    original.__file__, original.__doc__ = __file__, __doc__
    base_final_height_seam = original.final_height_seam
    def final_height_seam(boundary, flow, q, endpoint, response):
        nonlocal statistics_parameters
        result = base_final_height_seam(boundary, flow, q, endpoint, response)
        statistics_parameters = np.array(endpoint[flow.parameter_slice], copy=True)
        frozen_parameters = statistics_parameters.copy()
        # The original seam helper currently leaves this same frozen profile
        # in q as a side effect.  Make the later statistics binding explicit
        # and independent of a mutable view of the solver endpoint.
        q.profile = lambda s: flow.profile.profile(s, frozen_parameters)
        return result
    original.final_height_seam = final_height_seam
    original_constructor = original.original_solver.native.outward.FullCoreProbe
    def constructor(core, source_M, source_N, velocity, length, k0):
        if (int(source_M), int(source_N)) != (int(accepted["M"]), int(accepted["N"])):
            raise ValueError("The original accepted source identity changed inside setup")
        return original_constructor(np.pad(np.asarray(core), (0, M - source_M)),
                                    M, N, velocity, length, k0)
    original.original_solver.native.outward.FullCoreProbe = constructor
    def profile(source, port, peak, source_tail_modes):
        if int(source_tail_modes) != int(accepted["M"]) or peak != spec["peak_curvature"]:
            raise ValueError("The scalar formula cannot change when continuing the prepared field")
        return LiftedModesPrefixProfile(source, port, peak, M, supports=spec["control_supports_binary64"])
    original.CompleteProfile = profile
    curve = CubicHermiteSpline(mesh, values, rhs, axis=0)
    def prepared_guess(source, designed, flow, extension_step, taper_fraction):
        # The real prepared112 field is already available; do not rebuild an
        # extension or relabel the accepted96 file to pass the old constructor.
        return mesh.copy(), lambda x: curve(x), dict(kind="actual-complete-higher-mode-preflight-reused",
            warm_sha256=sha(warm_path), original_source_modes=int(accepted["M"]),
            current_field_modes=M, source_accepted_prefix_not_reclassified=True)
    original.prepared_guess = prepared_guess
    base_preflight = original.preflight
    def preflight(x, at, flow, max_nodes):
        additions, history = [], []
        for iteration in range(16):
            x, yy, ff, residual, new = base_preflight(x, at, flow, max_nodes)
            additions.extend(new)
            bad, checks = rms_domain(x, yy, ff, flow)
            report = dict(field_modes=M, angular_quadrature=N, history=history, added_nodes=additions)
            history.append(dict(iteration=iteration, nodes=len(x), invalid_RMS_points=len(bad), checks=checks))
            original_write(output / "RMS-domain-preflight.json", report)
            if not len(bad):
                trace = CubicHermiteSpline(x, yy, ff, axis=0)
                minima = dict(nodes=domain_minimum(flow, x, yy))
                for fraction in (.5, .5 - .5 * np.sqrt(3 / 7), .5 + .5 * np.sqrt(3 / 7)):
                    points = x[:-1] + fraction * np.diff(x)
                    minima[str(float(fraction))] = domain_minimum(flow, points, trace(points))
                report.update(complete_preflight_passed=True, actual_query_minima=minima)
                original_write(output / "RMS-domain-preflight.json", report)
                return x, yy, ff, residual, additions
            revised = original.original_solver.merge_mesh(x, bad)
            if len(revised) == len(x) or len(revised) > max_nodes:
                raise FloatingPointError("Actual RMS query domain exceeds the unchanged node budget")
            additions.extend(float(s) for s in revised if s not in set(x))
            x = revised
        raise FloatingPointError("Actual RMS query domain did not resolve")
    original.preflight = preflight
    install_qr_diagnostics(output, M, original_write)
    return original.main()


if __name__ == "__main__":
    raise SystemExit(main())
