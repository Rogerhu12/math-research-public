#!/usr/bin/env python3
"""Fixed full-angle beta-squared rows from one actual collocation Jacobian.

The capture context observes the original CompleteLinearization's endpoint
Jacobian calls and returns every result unchanged.  No second complete
Jacobian is constructed.  Each selected Hermite query retains both actual
endpoint physical/control Jacobians, the complete rotating-frame q.jet
map, and the direct query control derivative.

This is a finite optimizer model on the original physical-phi grids.  It
does not replace the nonlinear all-domain checks or any scientific
acceptance condition.  It does not certify continuous angles or stations.
All numerical construction/checks run only in this public repo's Actions.
"""
from __future__ import annotations

import hashlib
import inspect
import json
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy
from scipy.interpolate import CubicHermiteSpline
from scipy.sparse.linalg import LinearOperator

from geometry_20261114_full_angle_domain_direction_probe import angular_values
from geometry_20261114_hermite_domain_constraints import hermite_weights


HERE = Path(__file__).resolve().parent
SCHEMA = "captured-full-angle-Hermite-domain-operator-v1"
INTERVALS = (473, 475, 477, 479, 480)
FRACTION = 0.17267316464601146
FROZEN = {
    "geometry_20261114_constrained_collocation.py":
        "70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8",
    "geometry_20261114_hermite_domain_constraints.py":
        "d9e004c827add0074c2e6dd6c854763c7157e5049cd5360c1f85ad440462f4ce",
    "geometry_20261114_full_angle_domain_direction_probe.py":
        "794788a17db22189b80d65b7def84f3515ca587ea59ffce96fe8887a071665e8",
    "geometry_20261114_full_dn_augmented.py":
        "f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e",
    "geometry_20261114_fft_frenet.py":
        "973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401",
    "geometry_20261114_r225_free_core_bvp.py":
        "a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08",
}


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Numerical use belongs to this public repository's GitHub Actions")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_identity(value):
    value = np.asarray(value)
    digest = hashlib.sha256()
    digest.update(str(value.shape).encode("ascii"))
    digest.update(b"\0")
    digest.update(value.dtype.str.encode("ascii"))
    digest.update(b"\0")
    digest.update(value.tobytes(order="C"))
    return dict(shape=list(value.shape), dtype=value.dtype.str,
        sha256=digest.hexdigest(), bytes=int(value.nbytes),
        definition="shape, NUL, actual dtype.str, NUL, actual C-order bytes")


def readonly(value):
    value = np.array(value, copy=True, order="C")
    value.setflags(write=False)
    return value


def real64(value, shape=None, name="array"):
    value = np.asarray(value)
    if value.dtype != np.dtype("float64") or (shape is not None and value.shape != shape):
        raise ValueError(f"{name} must retain the original real float64 shape {shape}")
    if not np.all(np.isfinite(value)):
        raise FloatingPointError(f"{name} is nonfinite")
    return value


def bits_equal(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return (a.shape == b.shape and a.dtype == b.dtype
        and a.tobytes(order="C") == b.tobytes(order="C"))


def source_identity():
    found = {name: sha(HERE / name) for name in FROZEN}
    if found != FROZEN:
        raise ValueError("An original numerical dependency changed; do not mix model identities")
    found[Path(__file__).name] = sha(__file__)
    return found


def function_identity(function):
    function = getattr(function, "__func__", function)
    path = inspect.getsourcefile(function)
    return dict(module=getattr(function, "__module__", None),
        qualname=getattr(function, "__qualname__", None),
        source_file=Path(path).name if path else None,
        source_sha256=sha(path) if path else None)


def state_identity(problem, state):
    return {name: array_identity(value) for name, value in (
        ("mesh", problem.x), ("augmented_y", state["y"]),
        ("augmented_f", state["f"]), ("coordinate_scale", problem.chart.scale))}


def _maximum(value):
    value = np.asarray(value)
    return float(np.max(abs(value), initial=0)) if np.all(np.isfinite(value)) else None


class EndpointJacobianCapture:
    """Observe selected pairs in the one original CompleteLinearization.

    Use:
        capture = EndpointJacobianCapture(problem, state)
        with capture:
            linear = CompleteLinearization(problem, state)
        domain = FullAngleDomainOperator(problem, state, capture)

    A shared endpoint appearing in two original chunk calls is retained
    separately whenever its actual J/P bytes differ.  In particular
    interval 479 and interval 480 use their own original chunk's node 480.
    """
    def __init__(self, problem, state, intervals=INTERVALS):
        require_actions()
        self.problem, self.state, self.flow = problem, state, problem.flow
        self.chart = problem.chart
        self.intervals = tuple(int(j) for j in intervals)
        if (not self.intervals or len(set(self.intervals)) != len(self.intervals)
                or any(j < 0 or j >= self.chart.m - 1 for j in self.intervals)):
            raise ValueError("Declare distinct actual mesh intervals")
        if not state["finite"]:
            raise FloatingPointError("Only capture a currently finite original complete model")
        real64(problem.x, (self.chart.m,), "mesh")
        real64(state["y"], (self.chart.m, self.flow.dimension), "augmented y")
        real64(state["f"], (self.chart.m, self.flow.dimension), "augmented f")
        real64(self.chart.scale, (self.chart.size,), "coordinate scale")
        if np.any(self.chart.scale <= 0):
            raise ValueError("The original coordinate scaling must remain positive")
        self.sources = source_identity()
        self.base_identity = state_identity(problem, state)
        self.functions = {
            "original_flow_jac": function_identity(self.flow.jac),
            "original_scalar_jets": function_identity(self.flow.scalar_jets),
            "original_q_jet": function_identity(self.flow.q.jet),
        }
        if self.functions["original_flow_jac"]["source_sha256"] != FROZEN[
                "geometry_20261114_full_dn_augmented.py"]:
            raise ValueError("Capture must observe the original complete augmented Jacobian")
        if self.functions["original_q_jet"]["source_sha256"] != FROZEN[
                "geometry_20261114_fft_frenet.py"]:
            raise ValueError("Use the actual frozen rotating-frame FFT jet")
        self.records, self.pool, self.calls = {}, {}, []
        self.linearization = None
        self._active, self.complete = False, False
        self.total_jacobian_calls = 0
        self._original = None
        self._wrapper = None

    def __enter__(self):
        if self._active or self.complete:
            raise RuntimeError("Use a fresh capture for each fixed A model")
        if getattr(self.flow.jac, "_full_angle_capture", False):
            raise RuntimeError("Do not nest captures on the same live flow")
        self._had_instance_jac = "jac" in self.flow.__dict__
        self._instance_jac = self.flow.__dict__.get("jac")
        self._original = self.flow.jac

        def observed(x, y):
            frame = sys._getframe(1)
            caller = dict(file=frame.f_code.co_filename, function=frame.f_code.co_name,
                line=int(frame.f_lineno), owner=frame.f_locals.get("self"),
                state=frame.f_locals.get("state"))
            result = self._original(x, y)
            self.total_jacobian_calls += 1
            self._capture(x, y, result, caller)
            return result

        observed._full_angle_capture = True
        self._wrapper = observed
        self.flow.jac = observed
        self._active = True
        return self

    def __exit__(self, error_type, error, traceback):
        overwritten = self.flow.jac is not self._wrapper
        if self._had_instance_jac:
            self.flow.jac = self._instance_jac
        else:
            del self.flow.jac
        self._active = False
        self._original = None
        self._wrapper = None
        if error_type is not None:
            return False
        if overwritten:
            raise RuntimeError("Another operation replaced the Jacobian during capture")
        missing = [j for j in self.intervals if j not in self.records]
        if missing:
            raise RuntimeError(f"The original A construction did not supply endpoint pairs {missing}")
        if state_identity(self.problem, self.state) != self.base_identity:
            raise ValueError("The fixed model state changed during the original A construction")
        self.complete = True
        return False

    def _endpoint(self, node, jac, position):
        n, flow = self.chart.n, self.flow
        full = np.asarray(jac[:, :, position])
        if full.shape != (flow.dimension, flow.dimension) or full.dtype != np.dtype("float64"):
            raise ValueError("Capture the original complete float64 augmented Jacobian")
        if (not np.all(np.isfinite(full))
                or np.any(full[:n, flow.core_slice] != 0)
                or np.any(full[n:, :] != 0)):
            raise ValueError("The finite original local core/constant-row structure changed")
        physical = readonly(full[:n, :n])
        parameter = readonly(full[:n, flow.parameter_slice])
        identities = dict(physical=array_identity(physical), parameter=array_identity(parameter))
        key = (int(node), identities["physical"]["sha256"], identities["parameter"]["sha256"])
        if key not in self.pool:
            self.pool[key] = dict(node=int(node), physical=physical, parameter=parameter,
                identity=identities)
        return self.pool[key]

    def _capture(self, x, y, jac, caller):
        x, y = np.asarray(x), np.asarray(y)
        if x.ndim != 1 or y.shape != (self.flow.dimension, len(x)):
            return
        matches = []
        for j in self.intervals:
            indices = np.flatnonzero(x == self.problem.x[j])
            for left in indices:
                right = int(left) + 1
                if right >= len(x):
                    continue
                if (bits_equal(x[left:right+1], self.problem.x[j:j+2])
                        and bits_equal(y[:, left:right+1], self.state["y"][j:j+2].T)):
                    matches.append((j, int(left), right))
        if not matches:
            return
        owner = caller["owner"]
        if (Path(caller["file"]).resolve() != (HERE / "geometry_20261114_constrained_collocation.py").resolve()
                or caller["function"] != "__init__"
                or getattr(owner, "problem", None) is not self.problem
                or caller["state"] is not self.state):
            raise ValueError("Selected J/P must come from the one original CompleteLinearization")
        if self.linearization is not None and owner is not self.linearization:
            raise ValueError("Do not mix endpoint Jacobians from two A constructions")
        self.linearization = owner
        if np.asarray(jac).shape != (self.flow.dimension, self.flow.dimension, len(x)):
            raise ValueError("The original Jacobian result has changed its tensor layout")
        call_number = len(self.calls)
        self.calls.append(dict(call_number=call_number,
            original_jacobian_call_number=self.total_jacobian_calls,
            source_line=caller["line"], stations=array_identity(x),
            station_count=len(x), first_station=float(x[0]), last_station=float(x[-1]),
            selected_intervals=[int(j) for j, _, _ in matches],
            original_return_value_unchanged=True))
        for j, left, right in matches:
            record = dict(interval=j, left=self._endpoint(j, jac, left),
                right=self._endpoint(j+1, jac, right), call_number=call_number)
            if j in self.records:
                old = self.records[j]
                if any(old[side]["identity"] != record[side]["identity"] for side in ("left", "right")):
                    raise ValueError("The same interval was captured with two different fixed J/P pairs")
            else:
                self.records[j] = record

    def assert_matches(self, problem, state):
        if not self.complete or self._active:
            raise RuntimeError("Complete the one original A construction before using its capture")
        if problem is not self.problem or state_identity(problem, state) != self.base_identity:
            raise ValueError("The B model must use the same mesh/state/scale as its captured A")

    def description(self):
        by_node = {}
        for entry in self.pool.values():
            by_node.setdefault(str(entry["node"]), []).append(entry["identity"])
        return dict(schema=SCHEMA, source_sha256=self.sources,
            runtime=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
                byteorder=sys.byteorder),
            original_functions=self.functions, base_identity=self.base_identity,
            intervals=list(self.intervals), original_jacobian_calls=self.total_jacobian_calls,
            captured_original_calls=self.calls,
            unique_endpoint_nodes=len(by_node), stored_endpoint_variants=len(self.pool),
            variants_per_node={key: len(value) for key, value in by_node.items()},
            endpoint_identities=by_node,
            interval_endpoint_identities={str(j): {
                side: self.records[j][side]["identity"] for side in ("left", "right")
            } for j in self.intervals if j in self.records},
            endpoint_pairs_bound_to_their_original_A_chunk=True,
            original_jacobian_return_values_unchanged=True,
            second_complete_Jacobian_constructed=False, complete=self.complete)


class FullAngleDomainOperator:
    """Immutable local rows on the full original scaled direction z.

    beta_squared has one row for every original q.N angle, in interval
    order.  Each local_blocks entry contains rows, B_left, B_right, B_p,
    global_columns, local_columns and row_slice.  The B_* views are already
    divided by chart.scale: do not apply S again.

    local_indices is the sorted union of used exact-coordinate columns.
    A later interval has two n-physical blocks and all k global controls;
    an inlet interval replaces the first physical block by the full free
    inlet-core chain.  Shared nodes and global parameters are scatter-added
    by both transposes.  No global dense matrix is allocated.
    """
    def __init__(self, problem, state, capture, fraction=FRACTION, input_identity=None):
        require_actions()
        capture.assert_matches(problem, state)
        self.problem, self.chart, self.flow = problem, problem.chart, problem.flow
        self.capture = capture
        self.intervals, self.fraction = capture.intervals, float(fraction)
        self.N, self.n, self.k = int(self.flow.q.N), self.chart.n, self.chart.k
        self.rows = len(self.intervals) * self.N
        self.shape = (self.rows, self.chart.size)
        self.base_identity = capture.base_identity
        self.input_identity = (json.loads(json.dumps(input_identity, allow_nan=False))
            if input_identity is not None else None)
        self._y = readonly(real64(state["y"], (self.chart.m, self.flow.dimension), "augmented y"))
        self._f = readonly(real64(state["f"], (self.chart.m, self.flow.dimension), "augmented f"))
        self._mesh = readonly(real64(problem.x, (self.chart.m,), "mesh"))
        self._scale = readonly(real64(self.chart.scale, (self.chart.size,), "coordinate scale"))
        if np.any(self._f[:, self.n:] != 0):
            raise ValueError("The exact constant core/control RHS rows must remain zero")
        core, control = self.flow.core_slice, self.flow.parameter_slice
        if (not np.all(self._y[:, core] == self._y[0, core])
                or not np.all(self._y[:, control] == self._y[0, control])):
            raise ValueError("The global core/control coordinate chart was lost")
        self.node_indices = readonly(np.unique(np.r_[self.intervals, np.asarray(self.intervals)+1]))
        self._queries, self.query_reports = [], []
        begin = time.monotonic()
        h00, h10, h01, h11 = hermite_weights(self.fraction)
        self.hermite_weights = (h00, h10, h01, h11)
        gd, ge, beta, direct = [], [], [], []
        for j in self.intervals:
            h = self._mesh[j+1] - self._mesh[j]
            station = float(self._mesh[j] + self.fraction*h)
            query = CubicHermiteSpline(self._mesh[j:j+2],
                self._y[j:j+2], self._f[j:j+2], axis=0)(station)
            values = angular_values(self.flow, station, query)
            d, e, Q, v, W = (values[name] for name in ("first", "second", "Q", "cross", "W"))
            a, nu = values["scalar"][:2]
            arrays = (query, d, e, Q, v, W, values["beta"], values["scalar"])
            if (not all(np.all(np.isfinite(value)) for value in arrays)
                    or a <= 0 or np.any(Q <= 0) or np.any(W <= 0)
                    or np.any(values["beta"] <= 0)):
                raise FloatingPointError("Every modeled original angle needs a positive finite base margin")
            factor = nu*nu/(a*a)
            gd.append((-6*factor*Q**2/W)[:, None]*d
                + (2*factor*Q**3/W**2)[:, None]*np.cross(e, v))
            ge.append((2*factor*Q**3/W**2)[:, None]*np.cross(v, d))
            ga = 2*nu*nu*Q**3/(a**3*W)
            gnu = -2*nu*Q**3/(a*a*W)
            controls = real64(np.asarray(self.flow.profile.control_jets(station)),
                (3, self.k), "complete query scalar control jets")
            direct.append(ga[:, None]*controls[0] + gnu[:, None]*controls[1])
            beta.append(values["beta"])
            algebraic = h00*self._y[j] + h*h10*self._f[j] + h01*self._y[j+1] + h*h11*self._f[j+1]
            self._queries.append(dict(interval=j, h=float(h), station=station, value=readonly(query)))
            self.query_reports.append(dict(interval=j, station=station, fraction=self.fraction,
                left=float(self._mesh[j]), right=float(self._mesh[j+1]),
                phi_grid="2*pi*arange(N)/N", N=self.N, a=float(a), returned_ap=float(nu),
                beta_squared_min=float(np.min(values["beta"])),
                beta_squared_min_angle_index=int(np.argmin(values["beta"])),
                original_normal_vs_cross_formula_max=_maximum(values["beta"]-values["cross_beta"]),
                original_spline_vs_Hermite_value_max=_maximum(query-algebraic),
                actual_original_spline_query=array_identity(query),
                scalar_control_jets=array_identity(controls)))
        gd, ge = np.stack(gd), np.stack(ge)
        direct = np.stack(direct)
        gamma = np.empty((len(self.intervals), self.N, self.n), dtype=np.float64)
        unit = np.zeros(self.n)
        jet_digest = hashlib.sha256()
        for column in range(self.n):
            unit[column] = 1.
            _, dcol, ecol = self.flow.q.jet(unit)
            real64(dcol, (self.N, 3), "original unit first jet")
            real64(ecol, (self.N, 3), "original unit second jet")
            jet_digest.update(int(column).to_bytes(8, "little"))
            jet_digest.update(dcol.tobytes(order="C"))
            jet_digest.update(ecol.tobytes(order="C"))
            gamma[:, :, column] = (np.einsum("anc,nc->an", gd, dcol)
                + np.einsum("anc,nc->an", ge, ecol))
            unit[column] = 0.
        if not np.all(np.isfinite(gamma)) or not np.all(np.isfinite(direct)):
            raise FloatingPointError("The complete physical/scalar query gradients are nonfinite")
        self.unit_jet_sha256 = jet_digest.hexdigest()
        self.factor_identities = [dict(interval=j,
            Gamma=array_identity(gamma[i]), Pi=array_identity(direct[i]))
            for i, j in enumerate(self.intervals)]
        # Preserve the actually compiled factors until artifact export.
        # They are not recomputed or used in any projection iteration.
        gamma.setflags(write=False)
        direct.setflags(write=False)
        self._factor_cache = tuple(dict(Gamma=gamma[i], Pi=direct[i])
            for i in range(len(self.intervals)))
        self.beta_squared = readonly(np.concatenate(beta))
        blocks, global_sets = [], []
        pstart = self.chart.physical_size + self.chart.free
        pcols = np.arange(pstart, self.chart.size, dtype=np.int64)
        for group, j in enumerate(self.intervals):
            g, h = gamma[group], self._queries[group]["h"]
            endpoint = capture.records[j]
            JL, JR = endpoint["left"]["physical"], endpoint["right"]["physical"]
            PL, PR = endpoint["left"]["parameter"], endpoint["right"]["parameter"]
            left = h00*g + h*h10*(g@JL)
            right = h01*g + h*h11*(g@JR)
            parameter = h*(h10*(g@PL) + h11*(g@PR)) + direct[group]
            if j:
                lcols = np.arange((j-1)*self.n, j*self.n, dtype=np.int64)
                lblock = left
                left_kind = "physical-node"
            else:
                lcols = np.arange(self.chart.physical_size, pstart, dtype=np.int64)
                lblock = left@self.chart.inlet
                left_kind = "exact-free-inlet-core"
            rcols = np.arange(j*self.n, (j+1)*self.n, dtype=np.int64)
            cols = np.concatenate((lcols, rcols, pcols))
            if len(set(cols.tolist())) != len(cols):
                raise ValueError("A query's local column layout must not duplicate global controls")
            row = np.concatenate((lblock, right, parameter), axis=1)
            row /= self._scale[cols][None, :]
            if not np.all(np.isfinite(row)):
                raise FloatingPointError("The compiled full-angle rows are nonfinite")
            row = readonly(row)
            left_count = len(lcols)
            block = dict(interval=j, rows=row,
                B_left=row[:, :left_count], B_right=row[:, left_count:left_count+self.n],
                B_p=row[:, left_count+self.n:],
                global_columns=readonly(cols),
                row_slice=slice(group*self.N, (group+1)*self.N),
                left_kind=left_kind, left_column_count=left_count,
                Gamma_identity=self.factor_identities[group]["Gamma"],
                Pi_identity=self.factor_identities[group]["Pi"])
            blocks.append(block)
            global_sets.append(cols)
        self.local_indices = readonly(np.unique(np.concatenate(global_sets)))
        for block in blocks:
            block["local_columns"] = readonly(np.searchsorted(self.local_indices, block["global_columns"]))
        self.local_blocks = tuple(blocks)
        self.local_shape = (self.rows, len(self.local_indices))
        self.build_seconds = time.monotonic() - begin
        self.block_identities = [dict(interval=block["interval"],
            rows=array_identity(block["rows"]),
            global_columns=array_identity(block["global_columns"]),
            local_columns=array_identity(block["local_columns"]))
            for block in self.local_blocks]
        model_identity = dict(schema=SCHEMA, sources=capture.sources,
            base=self.base_identity, fraction=self.fraction, intervals=self.intervals,
            N=self.N, beta_squared=array_identity(self.beta_squared),
            blocks=self.block_identities, original_unit_jet_sha256=self.unit_jet_sha256)
        self.model_sha256 = hashlib.sha256(json.dumps(model_identity,
            sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()
        # Gamma/Pi are build-time factors, not recomputed during projection.
        # Forward, transpose and all row actions use these identical frozen
        # compiled float64 blocks; no iteration performs Gamma @ J again.
        del gamma, direct, gd, ge

    def _vector(self, value, size, name):
        value = np.asarray(value)
        if value.shape != (size,) or np.iscomplexobj(value) or not np.all(np.isfinite(value)):
            raise ValueError(f"{name} requires one finite real vector of length {size}")
        return value

    def matvec(self, z):
        z = self._vector(z, self.chart.size, "scaled full direction")
        out = np.empty(self.rows)
        for block in self.local_blocks:
            out[block["row_slice"]] = block["rows"]@z[block["global_columns"]]
        return out

    def rmatvec(self, dual):
        dual = self._vector(dual, self.rows, "full-angle dual")
        out = np.zeros(self.chart.size)
        for block in self.local_blocks:
            # Within a block the indices are unique.  Across blocks this
            # is an intentional scatter-add for shared nodes/global p.
            out[block["global_columns"]] += block["rows"].T@dual[block["row_slice"]]
        return out

    def local_matvec(self, z):
        z = self._vector(z, len(self.local_indices), "scaled local direction")
        out = np.empty(self.rows)
        for block in self.local_blocks:
            out[block["row_slice"]] = block["rows"]@z[block["local_columns"]]
        return out

    def local_rmatvec(self, dual):
        dual = self._vector(dual, self.rows, "full-angle dual")
        out = np.zeros(len(self.local_indices))
        for block in self.local_blocks:
            out[block["local_columns"]] += block["rows"].T@dual[block["row_slice"]]
        return out

    def operator(self, local=False):
        return LinearOperator(self.local_shape if local else self.shape, dtype=np.float64,
            matvec=self.local_matvec if local else self.matvec,
            rmatvec=self.local_rmatvec if local else self.rmatvec)

    def description(self):
        return dict(schema=SCHEMA, model_sha256=self.model_sha256,
            source_sha256=self.capture.sources, input_identity=self.input_identity,
            base_identity=self.base_identity, capture=self.capture.description(),
            shape=list(self.shape), local_shape=list(self.local_shape),
            physical_modes=int(self.flow.M), physical_rows=self.n, global_controls=self.k,
            intervals=list(self.intervals), fraction=self.fraction, angular_grid_size=self.N,
            row_order="declared interval order, then original physical phi index 0..N-1",
            row_scaling="identity; beta_squared and B are both unscaled original margins",
            variable_scaling="B acts on z=S*coefficient_direction; compiled rows divide by S once",
            original_coordinate_scale=array_identity(self._scale),
            local_indices=array_identity(self.local_indices),
            beta_squared=array_identity(self.beta_squared),
            original_unit_jet_sha256=self.unit_jet_sha256,
            unit_jet_hash_recipe="for coefficient 0..n-1: uint64le index, actual float64 D1 C bytes, actual float64 D2 C bytes",
            query_gradients=self.factor_identities, compiled_blocks=self.block_identities,
            queries=self.query_reports, construction_seconds=self.build_seconds,
            stored_compiled_row_bytes=sum(block["rows"].nbytes for block in self.local_blocks),
            complete_query_factors_retained_until_artifact_export=True,
            query_physical_gradient="complete Gamma from original q.jet unit columns",
            query_direct_control_gradient="Pi=d_beta/da*control_value+d_beta/d_returned_ap*control_first",
            both_nodal_RHS_physical_and_parameter_chains_included=True,
            exact_inlet_chart_chain_included=bool(0 in self.intervals),
            other_explicit_local_core_columns_zero=True,
            shared_node_and_global_control_transposes_scatter_add=True,
            fixed_float_model="one frozen float64 row matrix per query; forward and transpose share these same bytes",
            no_claim_of_bitwise_identity_to_different_BLAS_or_FFT_contraction_orders=True,
            source_nonlinear_domain_checks_replaced=False,
            continuous_angle_or_all_station_certificate=False,
            new_scientific_acceptance_gate=False, native_tail_called=False)

    def verify(self, state, direction=None):
        """Actual adjoint/local and independent original complex-chain checks.

        direction, if supplied, is the actual full scaled LSMR direction.
        The thresholds are the existing implementation thresholds 5e-12
        and 5e-5.  They do not become new scientific acceptance gates.
        Only the unique selected endpoints are reevaluated by the original
        flow; every physical/core/control component of their lifted
        direction is retained.  No complete Jacobian is rebuilt.
        """
        require_actions()
        self.capture.assert_matches(self.problem, state)
        rng = np.random.default_rng(26520261114)
        reports = []
        for kind in ("all-coordinates", "shared-endpoints-and-controls", "controls-and-zero-support-core"):
            z = rng.standard_normal(self.chart.size)
            if kind == "shared-endpoints-and-controls":
                masked = np.zeros_like(z)
                masked[self.local_indices] = z[self.local_indices]
                z = masked
            elif kind == "controls-and-zero-support-core":
                z[:self.chart.physical_size] = 0
            w = rng.standard_normal(self.rows)
            Bz, BTw = self.matvec(z), self.rmatvec(w)
            left, right = float(Bz@w), float(z@BTw)
            denominator = max(1., float(np.linalg.norm(Bz)*np.linalg.norm(w)),
                float(np.linalg.norm(z)*np.linalg.norm(BTw)))
            local = self.local_matvec(z[self.local_indices])
            local_transpose = self.local_rmatvec(w)
            outside = np.ones(self.chart.size, dtype=bool)
            outside[self.local_indices] = False
            reports.append(dict(kind=kind, forward_dual=left, transpose_dual=right,
                normwise_adjoint_error=abs(left-right)/denominator,
                local_forward_relative_error=_maximum(local-Bz)/max(1., _maximum(Bz)),
                local_transpose_relative_error=_maximum(local_transpose-BTw[self.local_indices])
                    /max(1., _maximum(BTw)),
                transpose_outside_declared_support_max=_maximum(BTw[outside])))
        directions = []
        if direction is not None:
            directions.append(("actual-supplied-scaled-direction",
                np.array(self._vector(direction, self.chart.size, "actual scaled direction"), copy=True)))
        seeded = np.zeros(self.chart.size)
        seeded[self.local_indices] = rng.standard_normal(len(self.local_indices))
        # For later selected cells these global-core components must have
        # identically zero local action, while remaining present in A.
        seeded[self.chart.physical_size:self.chart.physical_size+self.chart.free] = rng.standard_normal(self.chart.free)
        directions.append(("seeded-local-physical-core-and-controls", seeded))
        complex_reports = []
        for kind, scaled in directions:
            coefficient = scaled/self._scale
            lifted = self.chart.lift_direction(coefficient)
            step = 1e-25
            chosen = self.node_indices
            augmented = self._y[chosen].astype(complex) + 1j*step*lifted[chosen]
            actual_rhs = self.flow(self._mesh[chosen], augmented.T).T
            if not np.all(np.isfinite(actual_rhs)):
                complex_reports.append(dict(kind=kind, finite=False,
                    reason="Original complete endpoint complex RHS is nonfinite"))
                continue
            direct = []
            for query in self._queries:
                j = query["interval"]
                positions = np.searchsorted(chosen, [j, j+1])
                actual_query = CubicHermiteSpline(self._mesh[j:j+2],
                    augmented[positions], actual_rhs[positions], axis=0)(query["station"])
                value = angular_values(self.flow, query["station"], actual_query)["beta"]
                direct.append(np.imag(value)/step)
            direct = np.concatenate(direct)
            predicted = self.matvec(scaled)
            finite = bool(np.all(np.isfinite(direct)) and np.all(np.isfinite(predicted)))
            difference = direct-predicted
            absolute = _maximum(difference) if finite else None
            denominator = max(1., _maximum(direct), _maximum(predicted)) if finite else None
            worst = int(np.argmax(abs(difference))) if finite else None
            complex_reports.append(dict(kind=kind, finite=finite,
                scaled_direction=array_identity(scaled),
                original_complex_derivative=array_identity(direct),
                compiled_derivative=array_identity(predicted),
                maximum_absolute_error=absolute,
                maximum_relative_error=absolute/denominator if finite else None,
                worst_row=worst,
                worst_interval=self.intervals[worst//self.N] if finite else None,
                worst_angle_index=worst % self.N if finite else None,
                full_augmented_original_RHS_used=True,
                unique_endpoint_count=len(chosen), complex_chart_expand_not_used=True))
        adjoint_error = max(row["normwise_adjoint_error"] for row in reports)
        local_error = max(max(row["local_forward_relative_error"],
            row["local_transpose_relative_error"], row["transpose_outside_declared_support_max"])
            for row in reports)
        complex_finite = all(row["finite"] for row in complex_reports)
        complex_error = (max(row["maximum_relative_error"] for row in complex_reports)
            if complex_finite else None)
        passed = bool(adjoint_error <= 5e-12 and local_error <= 5e-12
            and complex_finite and complex_error <= 5e-5)
        return dict(schema=SCHEMA, model_sha256=self.model_sha256,
            adjoint_and_local_checks=reports, original_complex_chain_checks=complex_reports,
            maximum_normwise_adjoint_error=adjoint_error,
            maximum_local_full_action_error=local_error,
            maximum_original_complex_chain_relative_error=complex_error,
            implementation_thresholds=dict(adjoint_and_local=5e-12, original_complex_chain=5e-5),
            implementation_check_passed=passed,
            actual_supplied_direction_checked=direction is not None,
            second_complete_Jacobian_constructed=False, native_tail_called=False,
            new_scientific_acceptance_gate=False,
            scope="selected original Hermite queries and full finite original phi grids only")

    def export(self, directory, row_chunk=256):
        """Preserve the actual fixed rows and endpoint J/P in small NPZ parts.

        This is an Actions artifact of the finite model, not a certificate.
        Every file is hashed in the manifest.  Publication remains the
        calling workflow's responsibility; no Git operation occurs here.
        """
        require_actions()
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        if self._factor_cache is None:
            raise RuntimeError("The complete query factors were already exported; retain the original manifest")
        row_chunk = int(row_chunk)
        if row_chunk < 1 or row_chunk > 256:
            raise ValueError("Keep each raw row-part at most 256 rows")
        files = []

        def save(name, **arrays):
            path = directory / name
            if path.exists():
                raise FileExistsError(f"Do not overwrite an existing fixed-model artifact: {path}")
            np.savez_compressed(path, **arrays)
            files.append(dict(path=name, sha256=sha(path), bytes=path.stat().st_size,
                arrays={key: array_identity(value) for key, value in arrays.items()}))

        save("base-and-local-layout.npz", mesh=self._mesh, y=self._y, rhs=self._f,
            coordinate_scale=self._scale, local_indices=self.local_indices,
            beta_squared=self.beta_squared, node_indices=self.node_indices)
        for group, block in enumerate(self.local_blocks):
            for left in range(0, self.N, row_chunk):
                right = min(self.N, left+row_chunk)
                save(f"query-{group:02d}-interval-{block['interval']:05d}-rows-{left:05d}-{right:05d}.npz",
                    rows=block["rows"][left:right], global_columns=block["global_columns"],
                    local_columns=block["local_columns"],
                    Gamma=self._factor_cache[group]["Gamma"][left:right],
                    Pi=self._factor_cache[group]["Pi"][left:right],
                    beta_squared=self.beta_squared[block["row_slice"]][left:right],
                    angle_indices=np.arange(left, right, dtype=np.int64))
        for index, entry in enumerate(self.capture.pool.values()):
            save(f"endpoint-{entry['node']:05d}-variant-{index:02d}.npz",
                physical_J=entry["physical"], parameter_P=entry["parameter"])
        manifest = self.description()
        manifest["files"] = files
        manifest["artifact_scope"] = "actual fixed finite B rows, complete Gamma/Pi, source identities and original A endpoint factors"
        path = directory / "manifest.json"
        if path.exists():
            raise FileExistsError("Do not overwrite a previous fixed-model manifest")
        path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False, allow_nan=False)+"\n")
        # All subsequent B/B^T/projection actions need only the 56 MB of
        # compiled rows.  Complete Gamma/Pi bytes now survive in artifacts.
        self._factor_cache = None
        return dict(directory=str(directory), manifest=str(path), manifest_sha256=sha(path),
            model_sha256=self.model_sha256, file_count=len(files)+1,
            total_file_bytes=sum(row["bytes"] for row in files)+path.stat().st_size)

