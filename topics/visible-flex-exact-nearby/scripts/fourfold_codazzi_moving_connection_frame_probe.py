#!/usr/bin/env python3
"""Checkpointed full-R moving-connection geometry diagnostic.

This integrates the complete candidate's model connection, whose residual
difference from the actual physical-angle pullback is explicitly retained
in R133-supplement-moving-frame-with-complete-residual-and-mean.md.
No PDE solution, interval integration bound, closed surface, Hausdorff
lower bound, or reach certificate is asserted by this floating program.
Every actual PPoly interval is respected, with one-sided endpoint values.
The candidate is never extrapolated or angularly truncated.
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import math
import os
import sys
import time
import traceback
from pathlib import Path
from fractions import Fraction

import numpy as np
from flint import ctx

from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_compact_metric_frame_probe import angular_derivative
from fourfold_codazzi_moving_polynomial_system import COORDINATES
from fourfold_codazzi_moving_regular_endpoint_system import MovingRegularEndpoint
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_phase_codazzi_two_end_probe import save_npz_gz
from fourfold_phase_local_correction_probe import sha
from fourfold_phase_symmetric_geometry import load_exact_object

FINAL_CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"


def json_text(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def array_sha(value):
    return hashlib.sha256(np.ascontiguousarray(value).tobytes()).hexdigest()


def atomic_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + ".partial-" + str(os.getpid()))
    with temporary.open("w") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


class CompleteBlocks:
    """Immutable complete blocks form their own checkpoint chain."""

    def __init__(self, root, identity, resume):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.lock = (self.root / ".connection-lock").open("a")
        fcntl.flock(self.lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        self.identity = identity
        self.identity_text = json_text(identity)
        self.files = sorted(self.root.glob("block-*.npz"))
        if self.files and not resume:
            raise FileExistsError("complete blocks exist; use explicit --resume")
        self.previous = ""
        self.count = 0

    def recover(self, radial_count, angles):
        expected = radial_count - 1
        state = None
        summary = None
        for number, path in enumerate(self.files):
            if path.name != "block-%06d.npz" % number:
                raise ValueError("checkpoint block indices are not consecutive")
            with np.load(path, allow_pickle=False) as data:
                if str(data["identity"]) != self.identity_text:
                    raise ValueError("checkpoint source/candidate/grid identity differs")
                if str(data["previous_block_sha256"]) != self.previous:
                    raise ValueError("checkpoint chain hash differs")
                indices = data["indices"]
                points = data["geometry"]
                if (indices.ndim != 1 or len(indices) == 0
                        or not np.array_equal(indices, np.arange(expected, expected-len(indices), -1))
                        or int(indices[-1]) < 0
                        or points.shape != (len(indices), angles, 12)):
                    raise ValueError("incomplete or overlapping geometry block")
                if not np.all(np.isfinite(points)):
                    raise ValueError("nonfinite saved geometry")
                state = data["last_state"].copy()
                if state.shape != (angles, 12) or not np.all(np.isfinite(state)):
                    raise ValueError("incomplete saved terminal frame")
                if not np.array_equal(state[:, :3], points[-1, :, :3]):
                    raise ValueError("saved terminal position does not match the last row")
                if not np.array_equal(state[:, 9:12], points[-1, :, 3:6]):
                    raise ValueError("saved terminal frame normal does not match the last row")
                summary = json.loads(str(data["summary"]))
                expected = int(indices[-1]) - 1
            self.previous = sha(path)
            self.count = number + 1
        return state, expected, summary

    def append(self, indices, points, state, summary):
        if not indices:
            return
        path = self.root / ("block-%06d.npz" % self.count)
        if path.exists():
            raise FileExistsError("never overwrite a complete geometry block")
        temporary = path.with_name(path.name + ".partial-" + str(os.getpid()))
        with temporary.open("wb") as stream:
            np.savez_compressed(
                stream, identity=np.array(self.identity_text),
                previous_block_sha256=np.array(self.previous),
                indices=np.asarray(indices, dtype=np.int64),
                geometry=np.asarray(points, dtype=np.float64),
                last_state=np.asarray(state, dtype=np.float64),
                summary=np.array(json_text(summary)),
            )
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        self.previous = sha(path)
        self.files.append(path)
        self.count += 1


class Connection:
    def __init__(self, system, saved, nu):
        self.system = system
        self.nodes = np.asarray(saved["radial_nodes"])
        self.coefficients = np.asarray(saved["piece_coefficients"])
        self.nu = nu
        self.phi = (math.pi/2)*np.arange(system.angular_grid)/system.angular_grid

    def piece_at(self, radius):
        return np.clip(
            np.searchsorted(self.nodes, radius, side="right") - 1,
            0, len(self.nodes)-2,
        )

    def fields(self, radius, piece=None):
        radius = np.atleast_1d(np.asarray(radius, dtype=float))
        if np.any(radius < self.nodes[0]) or np.any(radius > self.nodes[-1]):
            raise ValueError("no radial extrapolation")
        if piece is None:
            piece = self.piece_at(radius)
        piece = np.broadcast_to(np.asarray(piece, dtype=int), radius.shape)
        dx = radius - self.nodes[piece]
        c = self.coefficients[:, piece, :]
        values = ((c[0]*dx[:, None]+c[1])*dx[:, None]+c[2])*dx[:, None]+c[3]
        z = self.system.moving_data(radius, values.T, [self.nu])
        a, gamma, beta, K, _, Cref, *_ = z["target"]
        u = self.system.alpha*z["U"]
        v, m, d = z["v"], z["mean"], z["drift"]
        if np.any(m >= 0) or np.any(v >= 0) or np.any(gamma <= 0):
            raise ValueError("sampled candidate leaves the negative moving chart")
        tau = d*v/m - gamma*u
        result = dict(
            a=a, gamma=gamma, beta=beta, K=K, Cref=Cref,
            u=u, v=v, mean=m, drift=d, tau=tau,
            p=beta*tau/gamma,
            q=a*(gamma*K*v+d*u/m),
            t=np.broadcast_to(a*d/m, u.shape),
            A=beta*v/(gamma*m), B=a*u/m,
            C=np.broadcast_to(a/m, u.shape),
            fx=np.broadcast_to(a*gamma, u.shape), fy=a*tau,
            angular_speed=a*v/m,
        )
        if not all(np.all(np.isfinite(x)) for x in result.values()):
            raise ValueError("nonfinite complete model connection")
        return result

    @staticmethod
    def at(fields, index):
        return {name: value[..., index] for name, value in fields.items()}

    @staticmethod
    def rhs(state, f):
        X, Y, N = state[:, 3:6], state[:, 6:9], state[:, 9:12]
        out = np.empty_like(state)
        out[:, :3] = f["fx"][:, None]*X + f["fy"][:, None]*Y
        out[:, 3:6] = f["p"][:, None]*Y + f["q"][:, None]*N
        out[:, 6:9] = -f["p"][:, None]*X + f["t"][:, None]*N
        out[:, 9:12] = -f["q"][:, None]*X - f["t"][:, None]*Y
        return out

    def step(self, state, outer, inner):
        # A grid interval contains no original PPoly join in its interior.
        middle = (outer+inner)/2
        cell = int(self.piece_at(middle))
        f = self.fields([outer, middle, inner], [cell, cell, cell])
        a, b, c = [self.at(f, j) for j in range(3)]
        h = inner-outer
        k1 = self.rhs(state, a)
        k2 = self.rhs(state+h*k1/2, b)
        k3 = self.rhs(state+h*k2/2, b)
        k4 = self.rhs(state+h*k3, c)
        return state+h*(k1+2*k2+2*k3+k4)/6

    def anchor(self):
        f = self.at(self.fields([self.nodes[-1]], [len(self.nodes)-2]), 0)
        theta = self.phi + self.system.primitive(f["v"]-f["mean"])/f["mean"]
        radial = f["beta"]/f["gamma"]
        vertical = -f["a"]*f["Cref"]
        co, si = np.cos(theta), np.sin(theta)
        z = np.zeros_like(co)
        state = np.zeros((len(co), 12))
        state[:, :3] = np.column_stack([f["a"]*co, f["a"]*si, z])
        state[:, 3:6] = np.column_stack([radial*co, radial*si, z+vertical])
        state[:, 6:9] = np.column_stack([-si, co, z])
        state[:, 9:12] = np.column_stack([vertical*co, vertical*si, z-radial])
        return state


def update_extreme(summary, kind, name, value, radius):
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("nonfinite diagnostic: " + name)
    table = summary[kind]
    if name not in table or (value > table[name] if kind == "max" else value < table[name]):
        table[name] = value
        summary["at"][kind+":"+name] = float(radius)


def observe(connection, radius, state, summary):
    """Observe both actual traces at every original PPoly join."""
    phi = connection.phi
    F, X, Y, N = [state[:, j:j+3] for j in (0, 3, 6, 9)]
    Fphi, Xphi, Yphi, Nphi = [
        angular_derivative(value, phi) for value in (F, X, Y, N)
    ]
    frame = np.stack([X, Y, N], axis=2)
    gram = np.einsum("nai,naj->nij", frame, frame)-np.eye(3)
    update_extreme(summary, "max", "frame_gram_error", np.max(abs(gram)), radius)
    index = int(connection.piece_at(radius))
    pieces = [index]
    node = int(np.searchsorted(connection.nodes, radius, side="left"))
    if (0 < node < len(connection.nodes)-1
            and connection.nodes[node] == radius):
        pieces = [node, node-1]
    normals = []
    for piece in pieces:
        f = connection.at(connection.fields([radius], [piece]), 0)
        Fr = f["fx"][:, None]*X + f["fy"][:, None]*Y
        cross = np.cross(Fphi, Fr)
        area = np.linalg.norm(cross, axis=1)
        if np.any(area <= 0):
            raise ValueError("sampled model reconstruction loses immersion")
        normal = cross/area[:, None]
        normals.append(normal)
        a, gamma, tau = f["a"], f["gamma"], f["tau"]
        ratio = f["v"]/f["mean"]
        expected_frame = (
            f["A"][:, None]*Y+f["B"][:, None]*N,
            -f["A"][:, None]*X+f["C"][:, None]*N,
            -f["B"][:, None]*X-f["C"][:, None]*Y,
        )
        frame_error = max(
            np.max(np.linalg.norm(got-want, axis=1))
            for got, want in zip((Xphi, Yphi, Nphi), expected_frame)
        )
        position_error = np.max(np.linalg.norm(
            Fphi-f["angular_speed"][:, None]*Y, axis=1
        ))
        model_rr = a*a*(gamma*gamma+tau*tau)
        model_rt = a*a*tau*ratio
        model_tt = a*a*ratio*ratio
        rr = np.sum(Fr*Fr, axis=1)
        rt = np.sum(Fr*Fphi, axis=1)
        tt = np.sum(Fphi*Fphi, axis=1)
        A = f["K"]*f["v"] + f["u"]**2/f["v"]
        B = f["u"]/f["v"]
        C = 1/f["v"]
        centre = (A+C)/2
        spread = np.sqrt(((A-C)/2)**2+B*B)
        curvature = np.maximum(abs(centre+spread), abs(centre-spread))
        maxima = dict(
            frame_angular_constraint=frame_error,
            position_angular_constraint=position_error,
            relative_radial_metric_error=np.max(abs(rr/model_rr-1)),
            relative_angular_metric_error=np.max(abs(tt/model_tt-1)),
            normalized_mixed_metric_error=np.max(abs(rt-model_rt)/np.sqrt(model_rr*model_tt)),
            formal_candidate_principal_curvature_abs=np.max(curvature),
            sampled_model_radial_speed=np.max(np.linalg.norm(Fr, axis=1)),
            sampled_reconstructed_angular_speed=np.max(np.linalg.norm(Fphi, axis=1)),
            sampled_connection_angular_speed=np.max(abs(f["angular_speed"])),
            sampled_v_upper=np.max(f["v"]),
        )
        minima = dict(
            sampled_reconstruction_cross_norm=np.min(area),
            negative_v_gap=np.min(-f["v"]),
            negative_mean_gap=-f["mean"],
            sampled_angle_derivative=np.min(ratio),
        )
        for key, value in maxima.items():
            update_extreme(summary, "max", key, value, radius)
        for key, value in minima.items():
            update_extreme(summary, "min", key, value, radius)
    if len(normals) == 1:
        normals.append(normals[0])
    # The two normals retain both one-sided geometry observations at a join.
    return np.column_stack([F, N, normals[0], normals[1]])


def scan_complete_blocks(store, radii, state, save_radial):
    waist = state.copy()
    height = float(np.mean(waist[:, 2]))
    waist[:, 2] -= height
    angle = math.pi/4
    witness = waist[0, :3].copy()
    witness[:2] = np.array([
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle), math.cos(angle)],
    ]) @ witness[:2]
    targets = []
    for quarter in range(4):
        angle = -quarter*math.pi/2
        c, s = math.cos(angle), math.sin(angle)
        point = np.array([
            c*witness[0]-s*witness[1],
            s*witness[0]+c*witness[1], witness[2],
        ])
        targets.append(point)
        targets.append(point*np.array([1., 1., -1.]))
    targets = np.asarray(targets)
    selected = set(np.unique(np.linspace(0, len(radii)-1, save_radial, dtype=int)).tolist())
    selected.update((0, len(radii)-1))
    chosen = []
    largest_norm = 0.
    least_actual_support = float("inf")
    least_frame_support = float("inf")
    nearest = float("inf")
    nearest_at = None
    minimum_outer_height = float("inf")
    for path in store.files:
        with np.load(path, allow_pickle=False) as data:
            indices = data["indices"]
            points = data["geometry"].copy()
        points[:, :, 2] -= height
        F, frameN = points[:, :, :3], points[:, :, 3:6]
        actualN = (points[:, :, 6:9], points[:, :, 9:12])
        largest_norm = max(largest_norm, float(np.max(np.linalg.norm(F, axis=2))))
        least_frame_support = min(
            least_frame_support, float(np.min(np.sum(F*frameN, axis=2)))
        )
        for normal in actualN:
            least_actual_support = min(
                least_actual_support, float(np.min(np.sum(F*normal, axis=2)))
            )
        distances = np.linalg.norm(F[:, :, None, :]-targets[None, None, :, :], axis=3)
        location = np.unravel_index(np.argmin(distances), distances.shape)
        if float(distances[location]) < nearest:
            nearest = float(distances[location])
            nearest_at = dict(
                radial_index=int(indices[location[0]]),
                radius=float(radii[indices[location[0]]]),
                phi_index=int(location[1]),
                inverse_rotation_and_reflection_target=int(location[2]),
            )
        mask = radii[indices] >= .25
        if np.any(mask):
            minimum_outer_height = min(minimum_outer_height, float(np.min(F[mask, :, 2])))
        for j, index in enumerate(indices):
            if int(index) in selected:
                chosen.append((int(index), points[j].copy()))
    chosen.sort(key=lambda item: item[0])
    report = dict(
        common_world_height_translation=-height,
        sampled_maximum_position_norm=largest_norm,
        twice_sampled_maximum_norm=2*largest_norm,
        sampled_one_sided_reconstructed_normal_support_min=least_actual_support,
        sampled_frame_normal_support_min=least_frame_support,
        reflected_fourfold_body_point_cloud_nearest_distance=nearest,
        nearest_distance_is_not_a_continuous_lower_bound=True,
        nearest_at=nearest_at,
        phase_witness=witness.tolist(),
        minimum_z_where_r_at_least_quarter=minimum_outer_height,
        waist_height_range=[float(waist[:, 2].min()), float(waist[:, 2].max())],
        waist_frame_X_distance_to_vertical=float(np.max(np.linalg.norm(
            waist[:, 3:6]-np.array([0., 0., 1.]), axis=1
        ))),
        waist_frame_Y_vertical_max=float(np.max(abs(waist[:, 8]))),
        waist_frame_N_vertical_max=float(np.max(abs(waist[:, 11]))),
        reflection_is_only_a_diagnostic_point_cloud_until_waist_jets_match=True,
        caps_beyond_R_and_fixed_markers_not_included=True,
    )
    return report, np.asarray([radii[i] for i, _ in chosen]), np.asarray([x for _, x in chosen])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--object", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    ap.add_argument("--candidate", type=Path, required=True)
    ap.add_argument("--expected-candidate-sha256", default=FINAL_CANDIDATE)
    ap.add_argument("--q-vector", type=Path, default=Path(
        "notes/2026-11-13-R133-regular-r25over8-q256-floating.json"))
    ap.add_argument("--angles", type=int, default=512)
    ap.add_argument("--step", type=float, default=.001)
    ap.add_argument("--checkpoint-dir", type=Path, required=True)
    ap.add_argument("--checkpoint-rows", type=int, default=64)
    ap.add_argument("--max-new-rows", type=int, default=512)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--save-radial", type=int, default=64)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--geometry", type=Path, required=True)
    args = ap.parse_args()
    started = time.monotonic()
    ctx.prec = 192
    ctx.cap = 6
    if args.out.exists() or args.geometry.exists():
        raise FileExistsError("preserve earlier reports and final sampled geometry")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.geometry.parent.mkdir(parents=True, exist_ok=True)
    outcome = dict(
        kind="complete_moving_model_connection_checkpoint_geometry_diagnostic",
        complete=False, failure=None, mathematical_certificate=False,
        source_sha256=sha(__file__),
        no_silent_orthogonalization_or_waist_projection=True,
        all_reported_geometry_values_are_floating_samples=True,
        physical_angle_residual_bridge_still_required=True,
        continuous_integrator_and_Fourier_alias_errors_not_certified=True,
    )
    try:
        if sha(args.candidate) != args.expected_candidate_sha256:
            raise ValueError("the explicitly requested complete candidate identity differs")
        saved = load_candidate(args.candidate)  # verifies every full shard SHA and interval
        meta = json.loads(str(saved["metadata"]))
        M = int(meta["modes"])
        nodes = np.asarray(saved["radial_nodes"])
        if meta["object_sha256"] != sha(args.object) or meta["coordinates"] != COORDINATES:
            raise ValueError("different exact object or moving chart")
        if (nodes[0] != 0 or nodes[-1] != 25/8
                or np.asarray(saved["piece_coefficients"]).shape != (4, len(nodes)-1, 2*M+1)):
            raise ValueError("the complete actual [0,25/8] polynomial is required")
        if args.expected_candidate_sha256 == FINAL_CANDIDATE and (M != 32 or len(nodes) != 6145):
            raise ValueError("the final candidate complete shape changed")
        if (args.angles <= 6*M or args.angles % 2
                or not 0 < args.step <= .01 or args.checkpoint_rows <= 0
                or args.max_new_rows <= 0 or args.save_radial < 2):
            raise ValueError("invalid complete diagnostic resolution")
        if (args.save_radial+2)*args.angles*12*8 > 4_800_000:
            raise ValueError("selected final sampled geometry exceeds the file budget")
        alpha, nu = float(meta["amplitude"]), float(meta["nu"])
        if (Fraction.from_float(alpha) != Fraction(meta["exact_float_amplitude"])
                or Fraction.from_float(nu) != Fraction(meta["exact_float_nu"])):
            raise ValueError("the candidate exact parameter metadata differs")
        geometry, _ = load_exact_object(args.object, 512)
        body = RotationalBodyTarget(geometry)
        graft = RotationalGraftTarget(geometry, args.object)
        system = MovingRegularEndpoint(
            geometry, M, args.angles, body, graft,
            q_path=args.q_vector, mean_boundary="outer",
        )
        system.alpha = alpha
        connection = Connection(system, saved, nu)
        radii = np.unique(np.r_[
            np.linspace(0., 25/8, int(np.ceil((25/8)/args.step))+1),
            nodes, .05, .18, .25, 3.,
        ])
        module_classes = list(type(system).mro())+[
            RotationalBodyTarget, RotationalGraftTarget, load_exact_object,
            angular_derivative, load_candidate, save_npz_gz, sha,
        ]
        modules = {}
        for cls in module_classes:
            module = sys.modules.get(cls.__module__)
            location = getattr(module, "__file__", None)
            if location and str(location).endswith(".py"):
                modules[cls.__module__] = sha(location)
        identity = dict(
            source_sha256=sha(__file__),
            candidate_sha256=sha(args.candidate), object_sha256=sha(args.object),
            q_vector_sha256=sha(args.q_vector), modules=modules,
            coordinates=COORDINATES, exact_alpha=meta["exact_float_amplitude"],
            exact_nu=meta["exact_float_nu"], complete_candidate_nodes=len(nodes),
            complete_candidate_modes=M, angles=args.angles,
            radial_grid_sha256=array_sha(radii), radial_grid_count=len(radii),
            max_requested_step=args.step, geometry_columns=[
                "position", "frame_normal", "sampled_right_normal", "sampled_left_normal"],
            numpy_version=np.__version__, python_version=sys.version,
            scipy_version=sys.modules["scipy"].__version__,
            flint_version=getattr(sys.modules["flint"], "__version__", None),
            thread_environment={name: os.environ.get(name) for name in (
                "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS")},
            same_model_connection_as_proved=True,
        )
        store = CompleteBlocks(args.checkpoint_dir, identity, args.resume)
        state, next_index, summary = store.recover(len(radii), args.angles)
        recovered_rows = len(radii)-1-next_index
        if summary is None:
            summary = dict(max={}, min={}, at={})
        buffer_indices, buffer_points = [], []
        new_rows = 0
        last_print = time.monotonic()
        if state is None:
            state = connection.anchor()
            next_index = len(radii)-1
        anchor_fields = connection.at(connection.fields([25/8], [len(nodes)-2]), 0)
        outcome["regular_anchor_unpaid_trace_differences"] = dict(
            sampled_physical_B_abs_max=float(np.max(abs(anchor_fields["u"]/anchor_fields["v"]))),
            sampled_physical_C_minus_reference_abs_max=float(np.max(abs(
                1/anchor_fields["v"]-anchor_fields["Cref"]))),
            complete_physical_mean_C_minus_reference=float(
                1/anchor_fields["mean"]-anchor_fields["Cref"]),
            rotational_frame_slope_identity_error=float(abs(
                (anchor_fields["beta"]/anchor_fields["gamma"])**2
                +(anchor_fields["a"]*anchor_fields["Cref"])**2-1)),
            true_cap_world_position_and_frame_difference_not_yet_paid=True,
        )
        outcome.update(
            identity=identity, recovered_complete_rows=recovered_rows,
            total_radial_rows=len(radii), checkpoint_directory=str(args.checkpoint_dir),
            final_candidate_is_original_ac1d=(args.expected_candidate_sha256 == FINAL_CANDIDATE),
        )
        # At recovery, state is at next_index+1. At a new run, the first
        # row is the exact declared anchor, and is observed without a step.
        fresh_anchor = recovered_rows == 0
        while next_index >= 0 and new_rows < args.max_new_rows:
            if not fresh_anchor:
                state = connection.step(state, radii[next_index+1], radii[next_index])
            fresh_anchor = False
            points = observe(connection, float(radii[next_index]), state, summary)
            buffer_indices.append(next_index)
            buffer_points.append(points)
            new_rows += 1
            next_index -= 1
            if len(buffer_indices) >= args.checkpoint_rows:
                store.append(buffer_indices, buffer_points, state, summary)
                buffer_indices, buffer_points = [], []
            if time.monotonic()-last_print > 20:
                print(dict(
                    completed_rows=len(radii)-1-next_index,
                    total_rows=len(radii), inward_radius=float(radii[next_index+1]),
                    saved_complete_blocks=store.count,
                    elapsed_seconds=time.monotonic()-started,
                ), flush=True)
                last_print = time.monotonic()
        if buffer_indices:
            store.append(buffer_indices, buffer_points, state, summary)
        outcome.update(
            new_complete_rows=new_rows, completed_rows=len(radii)-1-next_index,
            complete_block_count=store.count, last_complete_block_sha256=store.previous,
            sampled_connection_diagnostics=summary,
            row_prefix_only=(next_index >= 0), complete=(next_index < 0),
        )
        if next_index < 0:
            global_report, saved_r, samples = scan_complete_blocks(
                store, radii, state, args.save_radial
            )
            outcome["global_sampled_geometry"] = global_report
            save_npz_gz(
                args.geometry,
                r=saved_r, phi=connection.phi,
                F=samples[:, :, :3], frame_normal=samples[:, :, 3:6],
                sampled_right_normal=samples[:, :, 6:9],
                sampled_left_normal=samples[:, :, 9:12],
                metadata=np.array(json_text(dict(
                    identity=identity, diagnostic_only=True,
                    full_radial_blocks=str(args.checkpoint_dir),
                    all_original_body_pieces_used=True,
                    whole_closed_surface_not_yet_constructed=True,
                ))),
            )
            if args.geometry.stat().st_size > 5_000_000:
                raise ValueError("final geometry exceeded file budget; preserve it locally")
            outcome["sampled_geometry_path"] = str(args.geometry)
            outcome["sampled_geometry_sha256"] = sha(args.geometry)
        else:
            outcome["pause_reason"] = "explicit maximum new complete rows reached"
    except Exception as error:
        outcome["complete"] = False
        outcome["failure"] = dict(type=type(error).__name__, message=str(error))
        outcome["traceback"] = traceback.format_exc()
        raise
    finally:
        outcome["wall_seconds"] = time.monotonic()-started
        atomic_json(args.out, outcome)
    print(json.dumps(dict(
        complete=outcome["complete"], failure=outcome["failure"],
        completed_rows=outcome.get("completed_rows"),
        total_rows=outcome.get("total_radial_rows"),
        output=str(args.out),
    )), flush=True)


if __name__ == "__main__":
    main()
