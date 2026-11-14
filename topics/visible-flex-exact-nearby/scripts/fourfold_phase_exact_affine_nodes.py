#!/usr/bin/env python3
"""Actual principal rays for one explicitly symmetric exact-affine R33 object.

Analytic parameter columns include both moving radial endpoints. Accepted
DOP853 steps and their dense polynomials are saved as finite dyadic reference
data for a separate residual proof. This runner itself remains floating.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import inspect
import io
import json
from pathlib import Path
import time

import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.integrate._ivp.rk import Dop853DenseOutput

from fourfold_circle_conjugacy import target_value
from fourfold_phase_conjugacy_nodes import evaluate_polynomial
from fourfold_phase_principal_map import PrincipalMap
from fourfold_phase_symmetric_geometry import load_exact_object


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_npz(path):
    raw = Path(path).read_bytes()
    if Path(path).suffix == ".gz":
        raw = gzip.decompress(raw)
    with np.load(io.BytesIO(raw), allow_pickle=False) as stored:
        return {name:stored[name].copy() for name in stored.files}


def packed_npz(arrays):
    stream = io.BytesIO()
    np.savez_compressed(stream, **arrays)
    raw = stream.getvalue()
    return (gzip.compress(raw, mtime=0), ".npz.gz") if len(raw) > 1_000_000 else (raw, ".npz")


def save_trace(stem, arrays):
    raw, suffix = packed_npz(arrays)
    if len(raw) <= 5_000_000:
        path = stem.with_suffix(suffix)
        path.write_bytes(raw)
        return [dict(path=str(path), sha256=digest(path), bytes=len(raw))]
    # Chunk by accepted steps, keeping each boundary state in both neighboring
    # chunks. A chunk is still one exact piecewise polynomial reference.
    refs = []
    count = len(arrays["dense_h"])
    for first in range(0, count, 128):
        last = min(first+128, count)
        piece = dict(arrays)
        for name in ("dense_t_old", "dense_h", "dense_y_old", "dense_F"):
            piece[name] = arrays[name][first:last]
        for name in ("accepted_tau", "accepted_state"):
            piece[name] = arrays[name][first:last+1]
        piece["initial_angles"] = piece["accepted_state"][0, 0]
        meta = json.loads(str(arrays["metadata"]))
        meta.update(first_accepted_segment=first, accepted_segment_stop=last)
        piece["metadata"] = np.array(json.dumps(meta, sort_keys=True))
        chunk, ext = packed_npz(piece)
        if len(chunk) > 5_000_000:
            raise ValueError("a 128-step trace chunk exceeds the repository limit")
        path = stem.with_name(stem.name+f".part{first:04d}").with_suffix(ext)
        # with_suffix would remove the part token; retain it explicitly.
        path = stem.parent/(stem.name+f".part{first:04d}"+ext)
        path.write_bytes(chunk)
        refs.append(dict(path=str(path), sha256=digest(path), bytes=len(chunk),
                         first_accepted_segment=first, accepted_segment_stop=last))
    return refs


class ExactAffineMap(PrincipalMap):
    def __init__(self, geometry, root, common, progress=None):
        self.geometry, self.solver, self.root = geometry, geometry.solver, float(root)
        self.calls, self.branches = 0, 0
        self.minimum_qbar, self.maximum_N = float("inf"), -float("inf")
        self.progress_file, self.started = progress, time.monotonic()
        self.common = common
        target = geometry.radial_target_metric([self.root], with_variations=True)
        self.root_parameter_derivative = float(-target["discriminant_columns"][0, 0]
                                              /target["target_discriminant_x"][0])
        self.endpoint_qbar = -.5*self.root*float(target["minus_K_x"][0])
        if self.endpoint_qbar <= 0:
            raise ValueError("nonpositive endpoint root quotient")

    def branch(self, theta, sign, start, finish, tolerance, stem):
        identity = dict(self.common, sign=float(sign), start=float(start), finish=float(finish),
                        root=self.root, ode_rtol=tolerance,
                        quarter_nodes=self.geometry.nodes)
        manifest = stem.with_suffix(".trace.json")
        if manifest.exists():
            saved = json.loads(manifest.read_text())
            if saved["identity"] != identity or not np.array_equal(saved["initial_angles"], theta):
                raise ValueError("saved branch is a different source/root/parameter/initial value")
            for ref in saved["traces"]:
                if digest(ref["path"]) != ref["sha256"]:
                    raise ValueError("saved branch trace SHA changed")
            self.maximum_N = max(self.maximum_N, saved["maximum_N"])
            self.minimum_qbar = min(self.minimum_qbar, saved["minimum_qbar"])
            self.calls += saved["rhs_calls"]
            self.branches += 1
            return tuple(np.asarray(saved[key]) for key in
                         ("final_angles", "final_jacobian", "final_parameter_column")), saved["traces"]
        count = len(theta)
        values = np.zeros((3, count))
        values[0] = theta
        before = self.calls
        start_raw = self.geometry.principal_quantities(np.full_like(theta, np.sign(start)*self.root), theta)
        start_speed = -start_raw["m"]/start_raw["n"]

        def fun(tau, flat):
            self.calls += 1
            state = flat.reshape(3, count)
            angle = state[0]
            x = self.root*np.sin(tau)
            sqk, cosine = self.ksquare(tau, x)
            qroot = sqk/cosine if cosine else np.sqrt(self.endpoint_qbar)
            raw = self.geometry.principal_quantities(np.full_like(angle, x), angle, columns=True)
            target = self.geometry.radial_target_metric([x], with_variations=True)
            m, n, G = (raw[key] for key in ("m", "n", "G"))
            mt, nt, Gt = (raw[key] for key in ("m_theta", "n_theta", "G_theta"))
            mp, np_, Gp = (raw[key] for key in ("m_parameter", "n_parameter", "G_parameter"))
            self.maximum_N = max(self.maximum_N, float(np.max(n/np.sqrt(G))))
            if np.max(n) >= 0 or np.min(G) <= 0:
                raise ValueError("actual N<0/immersion chart failed on a ray")
            b, w = -m/n, G/n
            bt, wt = -mt/n+m*nt/(n*n), Gt/n-G*nt/(n*n)
            bp, wp = -mp/n+m*np_/(n*n), Gp/n-G*np_/(n*n)
            kp = float(target["minus_K_columns"][0, 0])
            coefficient = self.root*cosine*(bt+sign*wt*sqk)
            forcing = (self.root*cosine*bp+sign*self.root*cosine*cosine*qroot*wp
                       +sign*self.root*w*kp/(2*qroot))
            result = np.stack((self.root*cosine*(b+sign*w*sqk), coefficient,
                               coefficient*state[2]+forcing))
            if self.progress_file and self.calls % 200 == 0:
                self.progress_file.write_text(json.dumps(dict(
                    status="running", rhs_calls=self.calls, branches=self.branches,
                    tau=float(tau), elapsed_seconds=time.monotonic()-self.started,
                    maximum_N=self.maximum_N, minimum_qbar=self.minimum_qbar,
                    current_trace_stem=str(stem)))+"\n")
            return result.ravel()

        solved = solve_ivp(fun, (start, finish), values.ravel(), method="DOP853",
                          rtol=tolerance, atol=tolerance/20,
                          max_step=abs(finish-start)/64, dense_output=True)
        if not solved.success:
            raise RuntimeError(solved.message)
        final = solved.y[:, -1].reshape(3, count)
        jacobian = np.exp(final[1])
        raw = self.geometry.principal_quantities(np.full_like(theta, np.sign(finish)*self.root), final[0])
        finish_speed = -raw["m"]/raw["n"]
        column = final[2]+self.root_parameter_derivative*(
            -jacobian*start_speed*np.sign(start)+finish_speed*np.sign(finish))
        interpolants = solved.sol.interpolants
        arrays = dict(
            accepted_tau=solved.t,
            accepted_state=solved.y.T.reshape(len(solved.t), 3, count),
            dense_t_old=np.array([p.t_old for p in interpolants]),
            dense_h=np.array([p.h for p in interpolants]),
            dense_y_old=np.stack([p.y_old.reshape(3, count) for p in interpolants]),
            dense_F=np.stack([p.F.reshape(7, 3, count) for p in interpolants]),
            initial_angles=theta.copy(), final_angles=final[0],
            final_jacobian=jacobian, final_parameter_column=column,
            metadata=np.array(json.dumps(dict(identity=identity,
                state_rows=["theta", "log_J", "fixed_x_parameter_variation"],
                dense_formula="nested reversed F, multiplying alternately by z and 1-z; then add y_old",
                scipy_version=scipy.__version__,
                scipy_dense_class_sha256=hashlib.sha256(inspect.getsource(Dop853DenseOutput).encode()).hexdigest(),
                root_parameter_derivative=self.root_parameter_derivative,
                maximum_N=self.maximum_N, minimum_qbar=self.minimum_qbar,
                floating_only=True), sort_keys=True)),
        )
        refs = save_trace(stem, arrays)
        record = dict(identity=identity, initial_angles=theta.tolist(),
                      final_angles=final[0].tolist(), final_jacobian=jacobian.tolist(),
                      final_parameter_column=column.tolist(), traces=refs,
                      accepted_steps=len(interpolants), rhs_calls=self.calls-before,
                      maximum_N=self.maximum_N, minimum_qbar=self.minimum_qbar)
        manifest.write_text(json.dumps(record, indent=2)+"\n")
        self.branches += 1
        print(json.dumps(dict(progress="exact-object branch saved", trace_stem=str(stem),
                              accepted_steps=len(interpolants), rhs_calls=self.calls,
                              elapsed_seconds=time.monotonic()-self.started)), flush=True)
        return (final[0], jacobian, column), refs

    def round_trip(self, theta, tolerance, directory, first):
        one, refs1 = self.branch(theta, -1., -np.pi/2, np.pi/2, tolerance,
                                 directory/f"block_{first:04d}_forward")
        two, refs2 = self.branch(one[0], 1., np.pi/2, -np.pi/2, tolerance,
                                 directory/f"block_{first:04d}_backward")
        return two[0], one[1]*two[1], two[1]*one[2]+two[2], refs1+refs2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object", type=Path, required=True)
    parser.add_argument("--root-certificate", type=Path, required=True)
    parser.add_argument("--dyadic-conjugacy", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--trace-dir", type=Path, required=True)
    parser.add_argument("--progress", type=Path)
    parser.add_argument("--target", choices=["D5", "D8"], default="D5")
    parser.add_argument("--rays", type=int, default=258)
    parser.add_argument("--block-size", type=int, default=43)
    parser.add_argument("--quarter-nodes", type=int, default=256)
    parser.add_argument("--tolerance", type=float, default=2e-9)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    geometry, definition = load_exact_object(args.object, args.quarter_nodes)
    root_data = json.loads(args.root_certificate.read_text())
    if not root_data["proved"] or not root_data["parameter_is_exact_binary64_singleton"]:
        raise ValueError("a proved singleton exact-affine root certificate is required")
    checks = [(root_data["origin_inputs_sha256"], definition["origin_inputs"]["sha256"]),
              (root_data["frozen_direction_sha256"], definition["direction"]["sha256"]),
              (Fraction(root_data["exact_delta_fraction"]), Fraction.from_float(geometry.delta))]
    if any(a != b for a, b in checks):
        raise ValueError("root certificate belongs to another mathematical object")
    common = dict(object_file=str(args.object), source_sha256=digest(args.object),
                  origin_inputs_sha256=definition["origin_inputs"]["sha256"],
                  curve_direction_sha256=definition["direction"]["sha256"],
                  exact_delta_fraction=str(Fraction.from_float(geometry.delta)),
                  parameter_coordinate="exact R57 affine delta, not the legacy p label",
                  root_certificate_sha256=digest(args.root_certificate),
                  dyadic_conjugacy_sha256=digest(args.dyadic_conjugacy),
                  run_source_sha256=digest(Path(__file__)),
                  geometry_source_sha256=digest(Path(__file__).with_name("fourfold_phase_symmetric_geometry.py")),
                  target=args.target, quarter_nodes=args.quarter_nodes)
    mapper = ExactAffineMap(geometry, root_data["root_center"], common, args.progress)
    definitions = json.loads(args.dyadic_conjugacy.read_text())
    rho, scale = target_value(args.target), 4.
    alpha = 2*np.pi*rho
    x = np.arange(args.rays)*2*np.pi/args.rays
    H = x+evaluate_polynomial(definitions, x)
    shifted_H = x+alpha+evaluate_polynomial(definitions, x+alpha)
    Hp = 1+evaluate_polynomial(definitions, x, 1)
    shifted_Hp = 1+evaluate_polynomial(definitions, x+alpha, 1)
    common.update(target_rotation=rho, angular_scale=scale, rays=args.rays,
                  ode_rtol=args.tolerance, block_size=args.block_size,
                  target_root=mapper.root, target_root_interval=root_data["root_interval"],
                  root_parameter_derivative=mapper.root_parameter_derivative,
                  family_convention="explicit symmetric exact-affine infinite R33; synchronous target g0(delta)")
    # The branch identity must include the final common metadata on every run.
    mapper.common = dict(common)
    args.trace_dir.mkdir(parents=True, exist_ok=True)
    blocks = []
    if args.resume and args.out.exists():
        previous = json.loads(args.out.read_text())
        if any(previous.get(key) != value for key, value in common.items()):
            raise ValueError("resume source/definition/root/grid/tolerance changed")
        if previous["status"] == "complete":
            print(json.dumps({"progress":"matching completed exact-affine map already saved"}), flush=True)
            return
        blocks = previous["completed_blocks"]
        if blocks:
            mapper.maximum_N = max(b["maximum_N"] for b in blocks)
            mapper.minimum_qbar = min(b["minimum_qbar"] for b in blocks)
        mapper.calls = previous["current_rhs_calls"]
    for first in range(sum(len(b["x"]) for b in blocks), args.rays, args.block_size):
        sl = slice(first, first+args.block_size)
        returned, jacobian, column, traces = mapper.round_trip(H[sl]/scale, args.tolerance, args.trace_dir, first)
        blocks.append(dict(first_index=first, x=x[sl].tolist(),
                           input_physical_angles=(H[sl]/scale).tolist(),
                           returned_physical_angles=returned.tolist(),
                           angular_derivative=jacobian.tolist(),
                           parameter_column_physical=column.tolist(),
                           maximum_N=mapper.maximum_N, minimum_qbar=mapper.minimum_qbar,
                           dense_traces=traces))
        args.out.write_text(json.dumps(dict(**common, status="partial", completed_blocks=blocks,
                                           current_rhs_calls=mapper.calls), indent=2)+"\n")
        print(json.dumps(dict(progress="actual exact-object H-node block saved",
                              completed_rays=first+len(returned))), flush=True)
    returned = np.concatenate([b["returned_physical_angles"] for b in blocks])
    jacobian = np.concatenate([b["angular_derivative"] for b in blocks])
    column = scale*np.concatenate([b["parameter_column_physical"] for b in blocks])
    error, errorprime = scale*returned-shifted_H, jacobian*Hp-shifted_Hp
    weighted = column/shifted_Hp
    report = dict(**common, status="complete", kind="floating_exact_affine_actual_ray_conjugacy_diagnostic",
                  completed_blocks=blocks, rhs_calls=mapper.calls,
                  conjugacy_error=error.tolist(), conjugacy_error_derivative=errorprime.tolist(),
                  parameter_column_normalized=column.tolist(), weighted_twist_integrand=weighted.tolist(),
                  sampled_error_max=float(np.max(abs(error))),
                  sampled_error_derivative_max=float(np.max(abs(errorprime))),
                  sampled_weighted_error_mean=float(np.mean(error/shifted_Hp)),
                  sampled_weighted_twist_mean=float(np.mean(weighted)),
                  sampled_twist_integrand_range=[float(weighted.min()), float(weighted.max())],
                  proposed_linear_parameter_correction=float(-np.mean(error/shifted_Hp)/np.mean(weighted)),
                  maximum_sampled_N=mapper.maximum_N, minimum_radial_qbar=mapper.minimum_qbar,
                  limitations=["fresh floating rays of the explicitly defined symmetric affine object",
                    "finite primitive approximation, trig/FFT rounding and numerical root quotient remain unpaid",
                    "root center is a reference approximation inside the proved root interval",
                    "analytic parameter source is integrated, including both moving endpoints; no FD column is substituted",
                    "stored dense polynomials are exact dyadic reference definitions, not certified ODE solutions",
                    "finite node residual/twist do not provide full complex-domain or Wiener bounds",
                    "no exact conjugacy, PDE inverse, closed flex, held or reach certificate"])
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    if args.progress:
        args.progress.write_text(json.dumps(dict(status="complete", rhs_calls=mapper.calls))+"\n")
    print(json.dumps({key:report[key] for key in ["status", "target_root", "root_parameter_derivative",
        "sampled_error_max", "sampled_error_derivative_max", "sampled_weighted_twist_mean"]}), flush=True)


if __name__ == "__main__":
    main()
